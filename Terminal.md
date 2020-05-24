Terminal

# Browser Shell

 **tl;dr** a Linux VM mounting a JS filesystem with a Service Worker web server.

## Overview

The following is an experiment in impractical computing. It needs something more than a few tweets or a blog post to explain. So I've made you a demo of a number of interconnected projects I've been working on, all underpinned by the central idea of a **browser filesystem**. Everything you're about to see and do is going to happen in your browser, in JavaScript, and thanks to lots of features of the modern web platform. And, since a demo is supposed to get straight to the point, I'll pause my explanation here and give you a quick tour. Below that I'll explain how everything works.

If you're on mobile, or a slower machine, I put a short [screencast on YouTube](https://youtu.be/TFxpPbNDlJw) that might work better for you.

### Terminal to A Linux VM Mounting Shared Filesystem

The first part is a functional terminal to a [custom embedded Linux](https://github.com/humphd/browser-vm) running in the browser. As it boots, it's going to mount a [JS filesystem](https://github.com/filerjs/filer) in `/mnt`—this same filesystem is also accessible outside the VM, both in the window (open your `console` and you can run [node's fs methods](https://github.com/filerjs/filer#filesystem-instance-methods)) and in a Service Worker, where I'm [running a web server](https://github.com/humphd/nohost) (see below).

As far as Linux is concerned, it's just a normal filesystem, and you can do the usual things, for example:

- `cd /mnt`

- `ls -lah`

- `cat readme.txt`

- `mkdir files`

- `cp hello-world.html files/index.html`

- `vi files/index.html` (or use `nano`)

Try it yourself. Once it's booted, click the terminal and try working with `/mnt`. Clicking away, or hitting the *pause* button will suspend the VM, hitting *play* will resume it.

 *play_circle_outline*  *pause_circle_outline*

W

![](../_resources/380ed8ca4db7f498bbd525bfae2ac40a.png)![](../_resources/ef05d9d1038eef47b6e3407d29913464.png)![](../_resources/ef05d9d1038eef47b6e3407d29913464.png)![](../_resources/ef05d9d1038eef47b6e3407d29913464.png)

The filesystem and the VM will survive a reboot (reload of the page) without losing any data. The filesystem lives in indexeddb, and the VM's initial CPU and RAM state are stored in Cache Storage.

### Web Server to Shared Filesystem

The second part of this demo is a [static web server](https://github.com/humphd/nohost), hosting the shared filesystem from a Service Worker. Any file or directory you create in Linux under `/mnt` can be accessed via the web server at the `[/fs](https://humphd.github.io/fs)` route. For example, if you want to browse to a file called `/hello-world.html` you need to use the URL `[/fs/hello-world.html](https://humphd.github.io/fs/hello-world.html)`.

To make this a bit more obvious, I've created a simple iframe-based web browser that's serving the `[/fs/](https://humphd.github.io/fs/)` route. You can try creating/modifying things in Linux, and refreshing the iframe browser to see the changes, and view the files. I've also created a few files to get you started.

 *arrow_back*  *arrow_forward*  *refresh*  *home*

# Index of /

| ![](../_resources/7c210cb87b298e3a65cebde6d82ae9a3.png) | **Name** | **Last modified** | **Size** | **Description** |
| --- | --- | --- | --- | --- |
| * * * |
| ![](../_resources/dab77ea46ce02f72e2071751c49eed0c.png) | [Parent Directory](https://humphd.github.io/browser-shell/fs/) |     | -   |     |
| ![](../_resources/66aa1862ab7016e2b717d2cb32566ea5.png) |  [readme.txt](https://humphd.github.io/browser-shell/fs/readme.txt) | 27-Apr-2019 10:59 | 82  |     |
| ![](../_resources/66aa1862ab7016e2b717d2cb32566ea5.png) |  [hello-world.html](https://humphd.github.io/browser-shell/fs/hello-world.html) | 27-Apr-2019 10:59 | 20  |     |
|     |  [hi](https://humphd.github.io/browser-shell/fs/hi) | 28-Apr-2019 21:54 | 1   |     |
|     |  [marc](https://humphd.github.io/browser-shell/fs/marc) | 28-Apr-2019 21:56 | 1   |     |
|     |  [Screen Shot 2019-04-28 at 8.57.43 PM.png](https://humphd.github.io/browser-shell/fs/Screen%20Shot%202019-04-28%20at%208.57.43%20PM.png) | 28-Apr-2019 22:0 | 107K |     |
| * * * |

nohost (Web Browser Server)

Because a Service Worker doesn't need to be run in a page, you could also navigate to these URLs manually (i.e., you don't need this page, or this iframe). Again, there's no server. It's just JavaScript handling network requests with data from indexeddb. It looks like Apache because that's my how I grew up on the web, and it just felt right to use that style.

### Import Files to the Browser Filesystem

If you want to try adding arbitrary files yourself, you can also drag-and-drop them here. NOTE: nothing is uploaded to a server, everything lives in `indexeddb`. Whatever you add here will show up in `/mnt` in the VM, and in the `/` directory in the web server.

 *folder*

### Drop files here to be imported...

## Discussion

Now that you've got the general idea, let me spend some time talking about how it works, and what I had to build for each of the pieces.

### Origins

The entire thing is born out of an idea I'm fascinated with, namely, putting a filesystem in the browser. I've been chasing this idea since 2014 in one way or another. I got started on it when I was [porting Adobe's Brackets desktop code editor](https://blog.humphd.org/thimble-and-bramble/) to the browser for Mozilla's Thimble project. To do that, I needed to trick the app into thinking there was a full filesystem in the browser. A [friend](https://twitter.com/modeswitch) told me about a project he'd started to create a JS filesystem running on top of [indexeddb](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) called [Filer](https://github.com/filerjs/filer). I started hacking on it with him, and never really stopped. Filer works really well, and we used it in Thimble to handle millions of files in browsers all over the world for many years.

 ![](../_resources/bafebf6f2d5ec9068b20975f772c895a.png)

Since then I've continued to improve and extend Filer, building out the necessary [node.js `fs`](https://nodejs.org/api/fs.html) compatibility, which has grown a lot. While doing this work, one of the things I always wanted was a full command-line shell that I could use to create, view, and modify the files in the filesystem. Having an API you can code against is nice, but as a regular user of filesystems, I wanted a shell. I toyed with the idea of creating one from scratch, but decided it might be faster to just figure out how to get Linux running in the browser, and have it mount the Filer filesystem somehow.

### Hardware

As you've just seen, this isn't such a crazy idea (or, it's crazy, but doable!). To make it work, I first needed virtualized hardware running in the browser, something that is relatively easy to come by in 2019. I'm using a version of the amazing [v86](https://github.com/copy/v86) project that I've [modified for the task](https://github.com/humphd/v86/tree/filer-9p-lastknowngood). My v86 virtualized hardware is much like any number of old Linux boxes I've used since the mid-90s:

- x86 Pentium I

- 32M RAM

- CD-ROM Drive (I load and boot my VM as an ISO)

- Serial port connected to my terminal (I'm using [xtermjs](https://xtermjs.org/))

### Kernel I/O Support

Next I needed a way to mount my filesystem within Linux. I asked [Fabian](https://github.com/copy/), the creator of v86, for some guidance, and he suggested that I could probably modify some code that was created as part of the [jor1k OpenRISC 1000 emulator](https://github.com/s-macke/jor1k), and also included in v86. In both jor1k and v86, this filesystem allowed loading data over XMLHttpRequests from a remote server. In my case, I'd need to rework it to wrap my Filer filesystem API.

The idea is one that you may have [encountered in other virtual machines](https://www.linux-kvm.org/page/9p_virtio), where a host OS shares a filesystem with a guest VM. Often this is done using [virtio](https://www.ibm.com/developerworks/library/l-virtio/index.html), where hardware layers are abstracted. Linux supports a special [v9fs](https://www.kernel.org/doc/Documentation/filesystems/9p.txt) filesystem, which allows using a virtio transport to mount a [Plan 9](https://9p.io/plan9/)  [9p remote filesystem](https://en.wikipedia.org/wiki/9P_(protocol)).

 [![](../_resources/9ed02f926a3868d82dbb62cab1ad46d2.png)](https://9p.io/plan9/glenda.html) I think the fact that this project involved me working on something related to [Plan 9](https://9p.io/plan9/) is a big part of why I put up with it for so long. I've always loved Plan 9, and its "simple file protocol, 9p", and here was a chance to implement it!

Getting this to work took me quite a while. The [9p docs](https://9p.io/sys/man/5/INDEX.html) are terse, but clear if you spend enough time with them. There are lots of [9p implementations in various languages](http://9p.cat-v.org/implementations) that I read as well. I learned a lot by studying [chaos/diod](https://github.com/chaos/diod), [arm-js](https://github.com/ozaki-r/arm-js), [jor1k](https://github.com/s-macke/jor1k), and [v86](https://github.com/copy/v86).

By far the best thing I found on the web related to implementing the 9p protocol was a [series of blog posts from 2015](https://blog.aqwari.net/9p/index.html) about writing a 9p server in Go. The [protocol parsing post](https://blog.aqwari.net/9p/parsing/) was particularly useful to me. Debugging a failing virtio/9p implementation in JS, as it silently fails deep inside a Linux kernel running in an emulated VM in the browser, is not the most fun I've ever had. But eventually, I got it. If you're at all interested in what the protocol steps are like, reload this page with `?debug` on the URL, and open your `console` while you work with the `/mnt` directory. I have no doubt that if you press hard enough on the Linux terminal above, you'll likely uncover bugs, which you can [file if you like](https://github.com/humphd/browser-shell/issues/new).

### Operating System

My next hurdle was to create an operating system that would have all the bits I needed, and nothing I didn't. It also needed to be small, load my virtio kernel module, and include various startup scripts for the serial port setup, filesystem mount, etc.

The v86 project has a bunch of [pre-made OSes you can boot](https://github.com/copy/v86#demos). A number of these had aspects I needed, but none of them was exactly what I wanted. I needed to make my own Linux distro for running in the browser.

I wasted a lot of time on this. While I'm happy to spend hours nursing a failing program and deal with ridiculous levels of complexity in my tooling, my feeling about an OS is that it should work invisibly. I don't enjoy configuring or debugging them.

After a bunch of research, I ended up deciding to use [Buildroot](https://buildroot.org/) to create an "embedded" Linux distro. Most people use Buildroot to create a custom Linux kernel and OS config for small, on-board computers (e.g., a BeagleBoard) that get loaded via SD card. In my case, I needed my OS to run in a similarly constrained environment (i.e., v86 and the browser). The parallels were close enough, so I dove in.

 ![](../_resources/f69b59d9445a306d7ce73431a4a21104.png)

The [Buildroot docs](https://buildroot.org/downloads/manual/manual.html) are really well done, but long. They also have great [training material](https://bootlin.com/doc/training/buildroot/buildroot-slides.pdf), and there are some excellent talks on YouTube, like [this one](https://www.youtube.com/watch?v=1PfthHCfudY). I found it took me a long time to fill in the gaps in my knowledge that the docs/talks seemed to assume, since many people coming to Buildroot probably already have more extensive Linux and Kernel config knowledge than I did.

Eventually I created [my own Buildroot v86 board config and a Docker container](https://github.com/humphd/browser-vm) to automate the build process. I spent a bunch of time [stripping down the Kernel config](https://github.com/humphd/browser-vm/blob/master/buildroot-v86/board/v86/linux.config) to get rid of unnecessary drivers and bloat, but I'm sure there's [more space saving that could be done](https://github.com/humphd/browser-vm/issues/1). The end result is an [ISO file](https://github.com/humphd/browser-vm/releases/) with a custom Linux kernel, Plan 9 filesystem sharing, a root filesystem and shell using [BusyBox](https://busybox.net/), and [startup scripts](https://github.com/humphd/browser-vm/tree/master/buildroot-v86/board/v86/rootfs_overlay/etc) to get the serial terminal working and `/mnt` mounted to the browser filesystem. The browser downloads it and boots it as a CD-ROM.

### Web Server

Having the ability to host a filesystem in indexeddb, and work with it via a shell, the next thing I needed was a way to serve and execute these files in the browser. I spent a long time trying to figure out a way to leverage networking, ZMODEM, or some other protocol out of the Linux VM to the browser, so I could interact with what was running within the VM. In the end, this seemed like a dead-end, and I decided it made more sense to simply serve these files in response to network requests. The browser already knows how to parse and render web technologies, so there's no point trying to do better.

I'd actually built a few versions of this for Mozilla's Thimble in the past. My first iteration used [Blob URLs](https://developer.mozilla.org/en-US/docs/Web/API/Blob) and regex to rewrite HTML, CSS, and JS files, swapping relative paths to files in the filesystem for functioning Blob URLs. Once Service Workers were more widely supported in browsers, I rewrote things to use proper network requests for URLs, which got content from the database instead of the network.

For this, [my third iteration](https://github.com/humphd/nohost), I used [Workbox](https://github.com/GoogleChrome/workbox) to simplify my Service Worker code, and then created some simple routing to watch for URLs using `[/fs/](https://humphd.github.io/fs/)` and then satisfy them with content from the filesystem. The fact that indexeddb is accessible in both window and worker contexts make sharing data this way really easy.

The only extra thing I did this time was to spend some time reducing the size of the code necessary to maintain the list of MIME types I need in my server. Previously I've used [mime-db](https://github.com/jshttp/mime-db) and [mime-types](https://github.com/jshttp/mime-types), which are comprehensive, but massive to include in a browser. In the end I wrote some code to build my own, [browser-mime](https://github.com/humphd/browser-mime).

My solution was to use [Puppeteer](https://pptr.dev/) to process every MIME type in [mime-db](https://github.com/jshttp/mime-db), one by one, and create empty files of each type to see if the browser would parse/render them, or instead offer to download them. I found that I was able to use the [Navigation Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming) to determine whether a page load occurred (i.e., the browser knew how to process this type), or if the stream was simply downloaded to the user's OS (i.e., type not supported by the browser). This info allowed me to come up with a [much reduced MIME db](https://github.com/humphd/browser-mime/blob/master/dist/browser-mime-db.json) that I can bundle with my Service Worker, and which only includes things the browser is likely to parse/render, letting everything else get downloaded as an `application/octet-stream`.

### Conclusion

In the end, this is the solution to a problem you don't have. I get that. And yet, it was so much fun to get working, I had to share it with you. I *love* making browsers do new tricks. I wanted to put this page together to show what's possible by connecting some of the different things I've been thinking about and working on, specifically:

- [Filer](https://github.com/filerjs/filer) browser filesystem

- [browser-vm](https://github.com/humphd/browser-vm) Buildroot v86 board config and Docker container

- [browser-mime](https://github.com/humphd/browser-mime) MIME types for browsers

- [nohost](https://github.com/humphd/nohost) browser web server

- [browser-shell](https://github.com/humphd/browser-shell) everything in one page, this site

The techniques I've outlined above are only going to become more realistic as we move forward. [WebAssembly](https://webassembly.org/) is pushing the limits of what's possible in the browser yet again. Running complex code like VMs in the browser is going to get faster. For example, a few weeks ago [jor1k got a WASM CPU rewrite](https://github.com/s-macke/jor1k/commit/5075e059c0f06dadeafe7740bb5561c194dca87c).

Being able to use the same page to create, edit, serve, and execute code seems like an idea that could have many interesting uses. It wouldn't be hard to hook up a few more "editor" apps to this site, and have them all share the same filesystem. You could even run them out of the filesystem if that made sense. Combine this with any of the various web p2p protocols for sharing data between browsers, and you could build some really cool and useful applications.

If you're interested in the potential of a browser filesystem, you should [get in touch](https://twitter.com/humphd). I'd love to keep doing more with Filer, I think it has so much potential. Right now it's just a side passion, but I'd love for it to be more.

Thanks for checking this out. If you have thoughts you can [let me know on GitHub](https://github.com/humphd/browser-shell).

 *David Humphrey ([@humphd](https://twitter.com/humphd)), April 2019.*