Linux debugging tools I love - Julia Evans

# Linux debugging tools I love

•[favorite](https://jvns.ca/categories/favorite) •

I gave a talk this weekend about debugging tools I love (here are [the slides](https://speakerdeck.com/jvns/systems-programming-is-for-everyone), such as they are). I think of these tools like a swiss army knife – if something on your system is wrong or slow, in any programming language, knowing how to use them can really help you out. I’ve written pretty extensively on this, but I didn’t have a central list to refer to. So! Here’s the list of my current favorite tools. There are only 5! I’ve used all of them (except opensnoop) to debug actual problems.

tcpdump and wireshark and opensnoop are also things that you can have on OS X.

### strace

A tool that traces system calls. My favorite thing. I have a bunch of posts with examples of how to use it on this blog. If you want to read what I think of it you should read the fanzine reference that you can read [here](https://jvns.ca/blog/2015/04/15/strace-zine/).

strace is pretty broadly useful, but keep in mind it can really slow down your programs.

I would be remiss if I did not mention the even-more-awesome dtrace. Colin Jones has a [nice introduction](https://blog.8thlight.com/colin-jones/archive.html).

### dstat

A really simple tool that prints out how much data got sent over the network / written to disk every second. This is great when you suspect something is going on with network/disk usage and want to see what’s happening in real time.

There’s also iostat and netstat and atop and a bunch of other tools, but dstat is my favorite.

### tcpdump + wireshark

For spying on network traffic. I wrote an introduction explaining how to use them in [tcpdump is amazing](https://jvns.ca/blog/2016/03/17/tcpdump-is-amazing/).

When using these, it really helps to have a basic understanding of how networking works. Luckily the basics (“what’s the difference between IP and TCP and HTTP? what’s a network packet?”) are totally possible to pick up :D.

### perf

Have a C program and want to know which functions it’s spending the most time in? `perf` is a sampling profiler for Linux that can tell you that.

`perf top` gives you a live view of which functions are running right now, just like `top`. I like to use `perf top` no matter what language my programs are written in, just to see if I can understand anything from it. Sometimes it works!

node.js has built-in support for using perf to show you which Node function is running right now. You can also get this for JVM programs with perf-map-agent.

Brendan Gregg’s website has the best [introduction to perf](http://www.brendangregg.com/perf.html) I know.

You can use perf to generate amazing [flame graphs](http://www.brendangregg.com/flamegraphs.html) like this:

[flamegraph.svg](../_resources/48745ab32557c438e6e11023e3068afa.bin)

### opensnoop

Opensnoop is a new script that you can get as of Ubuntu 16.04. It’s a delightfully simple tool – it just shows you which files are being opened right now on your computer. And it’s fast, unlike strace!

opensnoop also exists on OS X and does basically the same thing.

Go to the [iovisor/bcc](https://github.com/iovisor/bcc) repo on github for installation instructions. It works using eBPF, which is a new thing that I will not explain yet here but Brendan Gregg has been writing about enthusiastically for some time. You don’t need to know how it works to use it, though :).

Want a weekly digest of these blog posts?

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fjvns.ca%2Fblog%2F2016%2F07%2F03%2Fdebugging-tools-i-love%2F&ref_src=twsrc%5Etfw&text=Linux%20debugging%20tools%20I%20love%20-%20Julia%20Evans&tw_p=tweetbutton&url=https%3A%2F%2Fjvns.ca%2Fblog%2F2016%2F07%2F03%2Fdebugging-tools-i-love%2F&via=b0rk)

[«How do HTTP requests get sent to the right place?](https://jvns.ca/blog/2016/07/14/whats-sni/)[»PolyConf 2016](https://jvns.ca/blog/2016/07/03/polyconf-2016/)