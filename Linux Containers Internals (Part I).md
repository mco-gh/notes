Linux Containers Internals (Part I)

# [Linux Containers Internals (Part I)](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/)

**Namespaces** and **control groups** (cgroups) are responsible for the magic behind Linux containers. The support for namespaces initially appeared in **2.4.19** kernels (mount point/file system isolation), but there are now six different types of namespace abstractions in the mainline of the contemporary kernels. From the kernel’s perspective, a container is just another process with its own set of resources - file descriptors, process address space and processor’s state. For instance, a containerized **nginx** web server exposes **external PIDs** for its master and worker processes:

	[nedo@archrabbit]$ ps  -eo pid,comm,cmd | grep nginx
	4971 nginx           nginx: master process nginx -g daemon off;
	4987 nginx           nginx: worker process

From the output of the `ps` command it’s hard to differentiate containerized processes from other processes running on the host. We can provide another option to the `ps` command so it also shows the **cgroup** to which the process is bounded.

	[nedo@archrabbit]$ ps  -eo pid,comm,cmd,cgroup | grep nginx
	4971 nginx           nginx: master process nginx      9:blkio:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	8:net_cls:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	7:devices:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	6:pids:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	5:cpu,cpuacct:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	4:freezer:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	3:cpuset:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	2:memory:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	1:name=systemd:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326
	4987 nginx           nginx: worker process       9:blkio:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	8:net_cls:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	7:devices:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	6:pids:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	5:cpu,cpuacct:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	4:freezer:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	3:cpuset:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	2:memory:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326,
	1:name=systemd:/docker/91dfd31b99a29c145b2f183970fc9c197261c8381463330aef8c262abe751326

The output is much more verbose now, but we can see processes are attached to the cgroups of the **docker** hierarchy, and so assume those are running inside container.

Surprisingly, the life of a container starts by issuing a `clone` system call which creates a new process descriptor. The newborn process can share a number of resources with its parent process depending on the value of the `flags` argument. Typically, both child and parent share the same memory address space until one of them decides to write a new memory page, when a copy of that page is moved to the address space of the process which requested the write operation (this optimization technique is commonly known as **CoW**). Besides sharing the memory address space, they often share file descriptor table and file system information. However, the child process may ask for a separate system resource, including an isolated namespace by providing one of the following flags - `CLONE_NEWNS`, `CLONE_NEWPID`, `CLONE_NEWUSER`, `CLONE_NEWUTS`, `CLONE_NEWIPC`, `CLONE_NEWNET`. For each of them a new namespace is created and the child process becomes the member of that namespace. The perception of the process is to have its own instance of the system resource that’s only visible to the members of the same namespace. That could be analogous to how kernel provides an illusion to a process through processor virtualization and virtual memory that it’s the only running process on the system (when it’s actually sharing the CPU cycles and physical memory with another processes).

The process can call `unshare` system call as an alternative mechanism to namespace creation, as well as it can join an existing namespace via `setns` syscall. The latter needs a file descriptor that identifies a namespace to which the process would like to join (the process can obtain the after-mentioned file descriptor from `/proc/[pid]/ns`).

### File system isolation

Mount namespace isolates the set of **mount tables**. Thus, the collection of processes have a completely independent view of the file system hierarchy. The mount points are only visible to a group of processes of the same mount namespace and they don’t propagate to other mount namespaces, providing the ability to the process to have its own `rootfs`. To create a new mount namespace, we pass the `CLONE_NEWFS` flag to the `clone` syscall. In the example above, we allocate some memory for the child’s stack and pass the callback function that gets executed in the context of the child process. If the call to `clone` is successful, we’ll have a child process attached to a brand new mount namespace.

	fn main() {
	    let stack = &mut[0; 1024 * 1024];
	    match unsafe {
	        clone(child_cb,
	              stack.as_mut_ptr() as *mut c_void,
	              CLONE_NEWNS,
	              ptr::null_mut()
	        )
	    } {
	        -1 => panic!("unable to create child process"),
	        _ => {}
	    }
	}

However, because the child process inherits the copy of the parent’s mount namespace, an invocation to `pivot_root` is required to change the root file system of the process. One of the requirements of the `pivot_root` syscall enforces the file system directories that are about to be swapped, can’t share the same tree. Calling the `mount` function with `MS_BIND` flag get our way out.

**NOTE:**  `pivot_root` may also fail if the root file system is mounted as shared. To workaround that, run this command: `mount --make-rprivate /`

	fn pivot_root(rootfs: String) -> Result<(), &'static str> {
	    unsafe {
	        if mount(rootfs.as_ptr() as *const i8,
	                 rootfs.as_ptr() as *const i8,
	                 ptr::null(),
	                 MS_BIND,
	                 ptr::null()) != 0 {
	            return Err("unable to mount rootfs");
	        }
	        let oldrootfs = String::from(format!("{}/.oldrootfs", rootfs.clone()));
	        if !Path::new(&oldrootfs).exists() {
	            create_dir(oldrootfs.clone());
	        }
	        if sys_pivot_root(rootfs, oldrootfs) != 0 {
	            return Err("unable to change rootfs");
	        }
	        *// change to root directory*
	        Command::new("chdir").arg("/").spawn();
	        Ok(())
	    }
	}

### PID and IPC namespaces

Recall we mentioned the containerized **nginx’s** instance exposes its external PIDs on the host system. Besides that, every process inside container has an **internal** PID. This correspondes to a numeric value of `1` for the first process inside container which acts as the `init` process (waits for and reaps orphaned child processes). The isolation of the PID number space is the guarantee for different PID namespaces to be able to have processes with same PIDs. The PID namespace is created by passing the `CLONE_NEWPID` flag to the `clone` or `unshare` system calls.**IPC namespace** (which it’s name implies) isolate interprocess communication mechanisms such as **POSIX message queues** or **System V IPC** objects. Passing `CLONE_NEWIPC` flag to the `clone` system call creates an isolated IPC namespace.

Here is the full source code that illustrates the creation of new mount, PID and IPC namespaces. Note the code has been reduced to the minimum for simplicity reasons. It makes use of the `libc` crate to invoke the system calls through standard C library. If you are looking for a high level abstraction, check out [nix](https://github.com/nix-rust/nix).

	extern crate libc;

	use libc::{c_void,
	           c_int,
	           c_long,
	           clone,
	           mount,
	           syscall,
	           MS_BIND,
	           CLONE_NEWNS,
	           CLONE_NEWPID,
	           CLONE_NEWIPC};

	use std::ptr;
	use std::path::Path;
	use std::fs::create_dir;
	use std::process::Command;

	static SYSPIVOTROOT: c_long = 155;

	extern "C" fn child_cb(args: *mut c_void) -> c_int {
	    match pivot_root(String::from(rootfs)) {
	        Ok(()) => {
	            *// we are now inside container*
	            *// execute any command of your choice*
	            println!("{:?}",
	                     Command::new("cat").arg("/etc/issue").output());
	        },
	        Err(e) => {
	            println!("error: {}", e);
	        }
	    };
	    0
	}

	fn pivot_root(rootfs: String) -> Result<(), &'static str> {
	    unsafe {
	        if mount(rootfs.as_ptr() as *const i8,
	                 rootfs.as_ptr() as *const i8,
	                 ptr::null(),
	                 MS_BIND,
	                 ptr::null()) != 0 {
	            return Err("unable to mount rootfs");
	        }
	        let oldrootfs = String::from(format!("{}/.oldrootfs", rootfs.clone()));
	        if !Path::new(&oldrootfs).exists() {
	            create_dir(oldrootfs.clone());
	        }
	        if sys_pivot_root(rootfs, oldrootfs) != 0 {
	            return Err("unable to change rootfs");
	        }
	        *// change to root directory*
	        Command::new("chdir").arg("/").spawn();
	        Ok(())
	    }
	}

	fn sys_pivot_root(root: String, oldroot: String) -> c_long {
	    unsafe {
	        syscall(SYSPIVOTROOT, root.as_ptr(), oldroot.as_ptr())
	    }
	}

	fn main() {
	    let stack = &mut[0; 1024 * 1024];
	    match unsafe {
	        clone(child_cb,
	              stack.as_ptr() as *mut c_void,
	              CLONE_NEWNS | CLONE_NEWPID | CLONE_NEWIPC,
	              ptr::null_mut())
	    } {
	        -1 => panic!("unable to create child process"),
	        _ => {}
	    }
	}

* * *

#### Share on

- [**](https://twitter.com/intent/tweet?text=http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/)

- [**](https://www.facebook.com/sharer/sharer.php?u=http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/)

- [**](https://plus.google.com/share?url=http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/)

**Linux Containers Internals (Part I)** was published on May 29, 2017.

- [4 comments]()
- [**Rabbit Stack**](https://disqus.com/home/forums/rabbitstack/)
- [Login](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend  3](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
- [⤤  Share](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)

![Avatar](../_resources/7b2fde640943965cc88df0cdee365907.png)
Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_EfJ4DU336y/)

 [tom yu](https://disqus.com/by/disqus_EfJ4DU336y/)    •  [9 days ago](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/#comment-3343871606)

really cool post! i was learning on docker and rust, your post make a great insight for me

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/bhnedo/)

 [bhnedo](https://disqus.com/by/bhnedo/)  Mod  [*>* tom yu](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/#comment-3343871606)  •  [8 days ago](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/#comment-3344216070)

I'm glad that helped to learn something new about containers and the Rust lang as well. Kind regards.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_RVp9Usne3B/)

 [chris](https://disqus.com/by/disqus_RVp9Usne3B/)    •  [9 days ago](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/#comment-3343721085)

This is awesome! Your explanation hit just the right level for me. I'm a little surprised by the code examples but I presume those are Rust? I haven't used Rust but it looks perfectly straightforward. In any case, very clearly explained, thank you.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/bhnedo/)

 [bhnedo](https://disqus.com/by/bhnedo/)  Mod  [*>* chris](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/#comment-3343721085)  •  [8 days ago](http://rabbitstack.github.io/operating%20systems/linux-containers-internals-part-i/#comment-3344215382)

Hi [@chris](https://disqus.com/by/disqus_RVp9Usne3B/) . Thank you for the kind words. The code example are written in Rust (I should point out that explicitly). Regards. Nedim

## Also on **Rabbit Stack**

- [

### Of Unikernels and Containers

    - 5 comments •

    - a year ago•

[bhnedo—Frank Drebin thanks. I will look into it.](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Fvirtualization%2Fof-unikernels-and-containers%2F%3AJoUFOIjkrvmzs2ha4jhdsqsDzVI&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=4578202947&zone=thread&area=bottom&object_type=thread&object_id=4578202947)](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Fvirtualization%2Fof-unikernels-and-containers%2F%3AJoUFOIjkrvmzs2ha4jhdsqsDzVI&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=4578202947&zone=thread&area=bottom&object_type=thread&object_id=4578202947)

- [

### Deploying Cloud Foundry on OpenStack Juno and XenServer (Part I)

    - 2 comments •

    - 2 years ago•

[bhnedo—Hi,It seems like an issue with pygrub. Can you please provide the full error log?](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Fdeploying-cloud-foundry-on-openstack-juno-and-xenserver-part-i%2F%3AOA-GrLe0TK8aRFw0Av7ogXpSRqE&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=3475769792&zone=thread&area=bottom&object_type=thread&object_id=3475769792)](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Fdeploying-cloud-foundry-on-openstack-juno-and-xenserver-part-i%2F%3AOA-GrLe0TK8aRFw0Av7ogXpSRqE&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=3475769792&zone=thread&area=bottom&object_type=thread&object_id=3475769792)

- [

### Running a Storm cluster on SmartOS

    - 2 comments •

    - 2 years ago•

[Jason King—Any reason to not use a zone to run most of the components instead of installing a bunch of Linux VMs?](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Frunning-a-storm-cluster-on-smartos%2F%3AkyQekoUMwHwlctSQT4xowu3IsUs&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=3616810862&zone=thread&area=bottom&object_type=thread&object_id=3616810862)](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Frunning-a-storm-cluster-on-smartos%2F%3AkyQekoUMwHwlctSQT4xowu3IsUs&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=3616810862&zone=thread&area=bottom&object_type=thread&object_id=3616810862)

- [

### Spring Boot or Not to Spring Boot?

    - 1 comment •

    - 2 years ago•

[johaness vix— even though for experienced ones, spring boot its just a pile of crap. I only make sense for startups or small companies for the big ones …](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Fspring-boot-or-not-to-spring-boot%2F%3AfYOKSYc0Y7rWEChxxfIp3Bcp0ug&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=3769164451&zone=thread&area=bottom&object_type=thread&object_id=3769164451)](http://disq.us/url?url=http%3A%2F%2Frabbitstack.github.io%2Fspring-boot-or-not-to-spring-boot%2F%3AfYOKSYc0Y7rWEChxxfIp3Bcp0ug&imp=6t92mvb2qe32ou&prev_imp&forum_id=3430235&forum=rabbitstack&thread_id=5861523111&thread=3769164451&zone=thread&area=bottom&object_type=thread&object_id=3769164451)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=rabbitstack&t_u=http%3A%2F%2Frabbitstack.github.io%2Foperating%2520systems%2Flinux-containers-internals-part-i%2F&t_d=Linux%20Containers%20Internals%20(Part%20I)&t_t=Linux%20Containers%20Internals%20(Part%20I)&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=rabbitstack&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)