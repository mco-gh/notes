Benefits of using tmux - lessons from streamlining a development environment

# Benefits of using tmux - lessons from streamlining a development environment

   [Keegan Lowenstein](https://twitter.com/keeganlow) in [Engineering](https://blog.bugsnag.com/category/engineering) on November 8, 2016

Before I started using tmux, I’d hear it mentioned frequently. It always sounded cool, and while there’s no shortage of great information on the web about what tmux is, it was never entirely clear to me how it would dramatically improve my development workflow. After using tmux for a few years, I’ve come to rely on its ability to streamline several aspects of my development process. Thanks to tmux, my workflow is now more organized, more automated, and easier to customize. My hope is that by sharing a few concrete examples of how tmux has helped me, it may help others better understand what might be gained by taking tmux for a spin.

This post assumes that you’re familiar with the basic vocabulary of tmux, concepts like sessions, panes, and windows. A tmux window functions much like a terminal tab; a session is a collection of related windows (think tabs); and each window can be split into horizontal or vertical sections called panes. Each pane behaves as if it were its own terminal, sourcing your dotfiles, managing distinct environment variables, and so on. For a more comprehensive intro,[here’s](http://tmuxp.readthedocs.io/en/latest/about_tmux.html#text-based-window-manager)a great resource to get you up to speed.

### Less Lost Work

We’ve all been there, that unfortunate keystroke or click that results in the unintentional loss of a crucial terminal window, gone with it a collection of attached processes: dev servers, text editors, REPLs and their state, ssh sessions, etc.

At best, losing a crucial terminal window is a minor distraction; at worst, it means a substantial context switch, delaying the work you were doing while you put the pieces back together.

With tmux you can detach from a session without losing that session’s state. This means if you accidentally quit your terminal, all is not lost. You just have to run `tmux attach` and you’re back in business.

![tmux-attach-example.gif](../_resources/78304da342f9640b2f4227bda47f1fac.gif)

This struck me as a minor benefit at first, but over the years this has saved me from quite a few headaches. If you rely heavily on the terminal for your development workflow, this benefit might be reason enough to give tmux a try.

### Automated Development Environment Creation

Before I started using tmux, whenever I needed a local development environment, I’d follow the same general set of steps:

- open a terminal

- cd to the project directory

- open an editor

- start a REPL

- start a build or compilation process

- start a few services

- tail a log file or two

In retrospect, I spent too long repeating these steps manually before I considered automation. With tmux I discovered how easy it is to automate the startup of a customized, terminal-based development environment. Tmux sessions are 100% scriptable, meaning you can create custom scripts that spin up the exact terminal state you need to start working on a given project.

These days, getting a dev environment spun up for any of the projects I work on takes only one command. This is especially great if you work on several projects, or if you have projects that you dip in and out of occasionally.

The following image series shows how with one tmuxp command (more on tmuxp in a bit) we can launch an entire environment for basic rails development: an editor, an adjacent shell for running git commands and tests, a running local web server, and a REPL.

![](../_resources/2098966033c607b3fbe15306b53a0682.png)
![](../_resources/8df1c41b32767517fc815decb14df8f8.png)
![](../_resources/1f59d5a058306d0e6446d18952173aa7.png)

I’ve noticed several benefits to being able to quickly spin up dev environments:

- reduced context switching overhead

- a more organized development process overall

- less time spent reorganizing windows and tabs, which leads to…

### Addressing Terminal Tab Sprawl

A key benefit of scripting each project’s dev environment has been an increase in organization. The terminal is the central tool in my development workflow. From text editing, to running tests to managing server processes, from git to ssh, the list goes on and on. Though I’d always start off with sound conventions for which processes ran where, each context switch between projects, each one-off task, carried with it the risk of leaving my terminal environment in a less organized state. Over time, I’d find myself with a growing collection of tabs and windows, which became increasingly confusing. Leading to questions like:

- “which window was that ssh session in again?”

- “which of these 5 tabs titled ‘bash’ did i run that command in?”

#### Codified Convention

Using tmux, I’ve restored order. Thanks to scripting my development environment startup for each project I work on, processes that I typically want to have running always run in a predictable place. And conveniently, if I ever find that things have gotten a little disorganized - if I’ve opened a few too many windows to handle one-off tasks, for example - I can kill the tmux session and bring up a fresh one with only two commands.

How you choose to use tmux to help you stay organized is up to you. I prefer using one session per project (i.e., git repo). For each project I work on, I have a script that launches a development environment and starts any necessary services, using the same general organization scheme for each session:

- first session window: editor (left pane), shell (right pane, for running tests, git commands)

- second window: server process

- third window: additional processes, workers

- additional windows: anything additional required to run or work on the given project.

#### Lowering Automation Cost

Building the habit of scripting tmux sessions was a key to getting more out of tmux; automation is great, but it’s important that it be easy to add tmux scripts for new projects as you take them on. A good goal is to develop a workflow where scripting a session configuration is just as easy as, if not easier than, setting up the session once manually.

If you like, you can script tmux sessions using only shell scripts containing several [tmux commands](http://man.openbsd.org/OpenBSD-current/man1/tmux.1). You can get pretty far with `tmux new-session`, `tmux send-keys`, `tmux new-window`, etc. For a quick introduction to scripting tmux directly (and as a very approachable intro to tmux in general), I’d suggest the book [tmux: Productive Mouse-Free Development](https://pragprog.com/book/bhtmux/tmux). Further, I strongly recommend you take time to get comfortable with a tool like[tmuxinator](https://github.com/tmuxinator/tmuxinator) or[tmuxp](https://github.com/tony/tmuxp). These tools will dramatically simplify the process of managing tmux sessions, making it easier to build the habit of specifying and automating dev environments for all of the projects you work on.

#### Lower Context Switching Overhead

Using tmux to manage dev environments for all of your projects means you’re always just one command away from having a local dev environment spun up exactly the way you like. This is also really nice after a system restart, one command and you’re back to work.

If you’re like me and you’re often jumping between codebases, tmux’s `<prefix> s` command is a huge help. This brings up a list of active sessions allowing you to quickly jump into another session (all without using your mouse). A few keystrokes and you’re working on an entirely different codebase; everything is how you left it; everything is where you expect it to be.

### Final Thoughts

The benefits of tmux covered in this post are only the beginning. The more you rely on the terminal in your development workflow, the greater the potential that you’ll find a tool like tmux to be really useful. Whether you give tmux a try or not, it’s worth considering if there are optimizations in the spirit of those discussed here that might help level up your own development workflow.

* * *

Many thanks to [Nicholas Marriott](https://tmux.github.io/), [Brian P. Hogan](https://pragprog.com/book/bhtmux/tmux), [Tony Narlock](https://leanpub.com/the-tao-of-tmux), and [Pete Doherty](http://peterdohertys.website/) for their thoughtful feedback on earlier versions of this post, and more importantly for their contributions to the world of tmux.

* * *

*This blog is part 1 in a series on [tmux](https://tmux.github.io/). Read part 2 on using tmux with vim: [tmux and vim - even better together](https://blog.bugsnag.com/tmux-and-vim/).*

 **🚀 Bugsnag is hiring!** · https://www.bugsnag.com/jobs/