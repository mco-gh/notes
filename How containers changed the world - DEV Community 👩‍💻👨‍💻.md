How containers changed the world - DEV Community 👩‍💻👨‍💻

A long, long time ago in a land not so far away, all programs on a computer lived together. They shared the same resources and privileges. If they were lucky, the operating system assigned CPU time fairly to each task. If they weren’t so lucky, they’d have to wait for competing tasks to give way.

Some tasks demanded root privileges, whether they deserved them or not. Others had arcane dependencies. Crucially, for us as developers, a framework, library, or tool would often demand a dependency that was incompatible with the version required by some other framework, library, or tool that we needed elsewhere.

These were dark times, friend.
Then came a solution. Containers.

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#what-are-containers-even) What are containers, even?

In a world where microservices reign and developers create ecosystems within ecosystems around ecosystems (yo dawg, I heard you like ecosystems, so I made an ecosystem for your ecosystem so you can ecosystem while you ecosystem), you’ve almost certainly worked with containers.

[![pgi5n5sqjwpq038xcqkk.jpg](../_resources/0e81e66c2f20822567442a77922107f8.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--m5Zb87Cr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/pgi5n5sqjwpq038xcqkk.jpg)

When you think of containers, you probably think of Docker on your dev laptop or Kubernetes in the cloud. Today it’s easy to take for granted a world in which computers can be both neatly and safely compartmentalised. And while one or two names have helped make the technology mainstream, the history of containers goes back much further than Docker’s launch in 2013.

In fact, this world has taken off so quickly, we can hardly **contain** our excitement! (sorry)

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#the-chroot-of-containers) The (ch)root of containers

Back in 1979, the Seventh Edition of Unix introduced chroot.

The purpose of chroot was to **ch**ange the **root** directory of a process to a different location in the filesystem. This isn’t quite what we think of as containerization today. There’s no separation of CPU time or memory. So, chroot isn’t technically virtual since the files for a process are simply “transposed” to another location. Nonetheless, changing the location of the files in that way was safer than having everything work on the same root.

One way to think of chroot is to think of riding on a freeway.

[![bw456e22n6uuhj9wyeun.jpg](../_resources/fe5d54c5c7c2fbbaf764f213cd72bc8f.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--ZLvLmAcx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/bw456e22n6uuhj9wyeun.jpg)

Each car has to share a single set of resources (the freeway) with all the other vehicles that are going in the same direction. However, two conventions prevent those vehicles from crashing into each other: one is the idea of maintaining a safe distance from the car in front and the other is that the freeway is divided into lanes. Lanes, in particular, mean that many more vehicles can safely occupy the same patch of highway. However, it’s only when everyone obeys the rules that lanes work: there isn’t a physical barrier. chroot is similar, in that it’s only by convention that one process doesn’t peer into the space given to other processes.

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#bad-behavior-leads-to-jails) Bad behavior leads to jails

chroot proved popular. It gained more uptake when the BSD respin of Unix implemented it in 1982. Eighteen years later, in 2000, the similarly named FreeBSD took the concept a step further with Jails.

[![94jkklc3nshpsfb4zghx.jpg](../_resources/122ea2841a977ae3e167c04528f24793.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--yxU-VlCM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/94jkklc3nshpsfb4zghx.jpg)

That name –– Jails –– isn’t accidental. One of the weaknesses of chroot was that it was pretty easy for a badly behaved process to break free of its directory and start messing with other chroots. Even with chroot-protected filesystems, networking, memory, and other resources are still shared between processes.

Jails, instead, were closer to a full virtualization of the host OS. They had their own superusers, files, process IDs, hostnames, and IP addresses. This made it easy to play around and break stuff for the first time without worrying about compromising the main machine. It also made it much harder for processes running in one jail to access whatever was running in other jails.

Roughly four years later, Sun Microsystems added something similar to their Solaris Unix-like operating system and called them Zones.

By that time, though, the world was turning more and more towards Linux. Linux admins, developers, and users looked on with envy as they saw their FreeBSD and Solaris counterparts safely compartmentalize their machines. That set in motion the technology that would make Docker possible.

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#hang-on-what-about-vms) Hang on, what about VMs?

Right now you might be thinking, “This is all very interesting but I remember having a virtualized OS back in the early 2000s”. And, yes, VMWare offered the world’s first x86 virtualization tool back in 1999. In fact, virtualization has been around since the IBM mainframes of the late 1960s.

But containerization is not virtualization. Sure, they often go hand in hand; such as when using Docker on a Mac. The crucial difference is that containers divide a single operating system into multiple distinct environments all using that same OS. Virtual machines, on the other hand, create functionally separate computers that can run entirely different operating systems from that of the host machine. As such, containers are very lightweight when compared to full VMs.

Want to run multi-tenant workloads safely all on the same version of Ubuntu? Use containers. Want to run Windows, FreeBSD, and CentOS machines on Ubuntu? Use virtual machines.

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#along-comes-lxc) Along comes LXC

The difference between chroot and containerisation as we think of it today requires functionality at the most fundamental level of the operating system. In Linux’s case, that came in the Linux kernel as control groups (known as cgroups). cgroups provide a way to isolate a set of processes from everything else that the kernel is running.

With cgroups in place, a Linux Jails-alike was made possible and LXC –– Linux Containers –– made its debut in 2008.

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#a-container-by-any-other-name) A container by any other name

Let’s take a step back, though, to a year or two before LXC, and take a quick look at Heroku and its dynos. Don’t be fooled by the name “dyno”; Heroku is fundamentally a container platform, it’s just that no one was calling them containers back when Heroku launched.

The early Heroku team set out to make it as easy to deploy Rails apps as, say, PHP was at the time. The easiest way to do that was to build a platform that took advantage of Linux’s new cgroups and build something like FreeBSD Jails. So, while the first lines of LXC were being written, Heroku built their own Linux containerization platform as the foundation for running multi-tenant workloads. Docker as we know it today started life in similar circumstances, as the internal containerization system for the dotCloud platform as a service provider.

By creating the first Linux-based production container platform, the Heroku team secured their own place in container history alongside the creators of chroot, Jails, and Kubernetes.

##   [(L)](https://dev.to/heroku/how-containers-changed-the-world-1jip?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=02-03-20#what-even-is-a-computer) What even is a computer?

At the risk of evoking a not too popular TV commercial for a tablet computer, containers have challenged our view as developers of what a computer even is. Just as x86 virtualization brought the mainframe’s multitenancy to commodity hardware, containers have solved several problems for developers and made newer architectures, such as microservices and serverless, much more practical.

For developers, the age of “it works on my machine” is largely over and dependency hell is increasingly an anachronism as containers provide replicable environments that can follow code from development, through testing, and into production.

Arguably, containers have done as much for developer productivity this decade as cloud computing and decentralized version control did in the previous. Up until the 2010s, a computer meant an electricity-hungry chunk of silicon and wires. Today, whether you’re using [Docker](https://www.docker.com/), deploying to [Heroku](https://www.heroku.com/), or orchestrating a [Kubernetes](https://kubernetes.io/docs/concepts/) cluster, containers have turned the notion of a computer into something much more ephemeral. And that’s truly wonderful. Thanks to containerization, a computer today could be pretty much anything so long as it works as the end point in a CI/CD pipeline.

*[Obligatory photo of shipping containers by chuttersnap](https://unsplash.com/@chuttersnap)

[Highway photo by Jake Blucker](https://unsplash.com/@jakeblucker)
[Jail cells photo by Emiliano Bar](https://unsplash.com/@emilianobar)*