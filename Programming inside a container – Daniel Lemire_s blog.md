Programming inside a container – Daniel Lemire's blog

# Programming inside a container

I have a small collection of servers, laptops and desktops. My servers were purchased and configured at different times. By design, they have different hardware and software configurations. I have processors from AMD, Intel, Ampere and Rockchip. I have a wide range of Linux distributions, both old and new. I also mostly manage everything myself, with some help from our lab technician for the initial setup.

The net result is that I sometimes end up with very interesting systems that are saddled with old Linux distributions. Reinstalling Linux and keeping it safe and secure is hard. Furthermore, even if I update my Linux distributions carefully, I may end up with a different Linux distribution than my collaborators, with a different compiler and so forth. Installing multiple different compilers on the same Linux distribution is time consuming.

So what can you do instead?

I could run virtual machines. With something like VirtualBox, you can run Linux inside Windows insider macOS. It is beautiful. But it is also slow and computationally expensive.

You can switch to containers, and Docker specifically, which have much less overhead. Docker is a ubiquitous tool in cloud computing. As a gross characterization, Docker allows you to run Linux inside Linux. It is a sandbox, but a sandbox that runs almost directly on the host. Unlike virtual machines, my tests show that on computationally intensive tasks, Docker containers run at “native speed” (bare metal). There are reports that system interaction is slower. Network connections and disk access is slower. For my purposes, it is fine.

If you must, you can also run Docker under macOS and Windows, though there will then be more overhead, I expect.

The idea of a container approach is to always start from a pristine state. So you define the configuration that your database server needs to have, and you launch it, in this precise state each time. This makes your infrastructure predictable.

It is not as perfect as it sounds. You still critically depend on the quality of the container you start from. Various hacking can be necessary if you need two applications with different requirements to run together in the same image.

Still, containers work well enough that they are basically sustaining our civilization: much of the cloud-based applications are based on containers one way or another.

Containers were built to deploy software into production. Programming inside containers is not directly supported: you will not find much documentation about it and there is simply not business model around it. What do I mean by “programming inside containers”? I mean that I’d to start a C programming project, decide that I will use the Linux Ubuntu 16.10 distribution and that I will compile and run my code under Linux Ubuntu 16.10, even though my server might be running a totally different Linux distribution (or might be under macOS).

The first problem is that your disk and the disk of the image built from the container are distinct. A running image does not have free access to the underlying server (the host). Remember that it is a sandbox.

So you can do all of your work **inside** the image. However, remember that the point of container technology is to always start from a pristine state. If you load up an image, do some work, and leave… your work is gone. Images are immutable by design. It is a great thing: you cannot easily mess up an image by tinkering with it accidentally.

You can, after doing some work inside an image, take a snapshot of the new state, commit it and create a new image from which you would start again. It is complicated and not practical.

What else could you do? What you can do instead is keep the image stateless, as images are meant to be. The image will only contain the compiler and build tools. There is no reason to change any of these tools. You will have all of your code in a directory, as you would normally do. To run and compile code, you will enter in the the image and run your commands. You can bind the repository from the host disk to the image just as you enter it.

This works much better, but there are glitches if you are issuing directly your docker command lines:

1. Depending on how Docker is configured on your machine, you may find that you are unable to read or write to the disk bound to the image from the image. A quickfix is to run the image with privileged access but it is normally frowned upon (and unnecessary).

2. The files that you create or modify from within the Docker image will appear on the host disk, often with strange file permissions. For example, maybe all of the files are owned by the root user. I had a research assistant that had a good workaround: he ran Linux as root all the time. I do not recommend such a strategy.

These glitches come from the strange way in which Docker deals with permissions and security. Contrary that what you mean read, it is not a simple matter of setting user and group identifiers: it may be sufficient on some systems but not on systems supporting Security-Enhanced Linux which require additional care.

And finally, you need to remember lots of complicated commands. If you are anything like me, you would rather not to have to think about Docker. You want to focus all of your attention on the code.

So the solution is to use a little script. In my case I use a bash script. [You can find it on GitHub](https://github.com/lemire/docker_programming_station). It handles messy commands and file permissions for you.

For years, I tried to avoid having to rely on a script, but it is simply unavoidable to work productively.

Basically, I copy two files at the root of the directory where I want to work (Dockerfile and run), and then I type:

./run bash

And that is all. I am now in a subshell, inside the host directory. I can run programs, compile them. I have complete access to a recent Ubuntu distribution. This works even under the ARM-based servers that I have.

The run script can take other commands as well, so I can use it as part of other scripts.

## Published by

![4b736113aa1557b9a110b5123d81d5f6](../_resources/3615e03a90327e1c11af0437e8875558.jpg)

### Daniel Lemire

A computer science professor at the University of Quebec (TELUQ). [View all posts by Daniel Lemire ](https://lemire.me/blog/author/lemire/)