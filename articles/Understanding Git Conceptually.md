Understanding Git Conceptually

# Understanding Git Conceptually

 **Navigation**
 **[Home](https://www.sbf5.com/~cduan/)**
 [Downloads](https://www.sbf5.com/~cduan/download/)
 [Technical Writings](https://www.sbf5.com/~cduan/technical/)
 [Non-Technical Writings](https://www.sbf5.com/~cduan/writings/)
 [Miscellaneous](https://www.sbf5.com/~cduan/misc/)
 [Links](https://www.sbf5.com/~cduan/links.shtml)
 [Help](https://www.sbf5.com/~cduan/nav-help.shtml)
 [BBQ and Fried Chicken](http://cd2dc.tumblr.com/about)

[Introduction](https://www.sbf5.com/~cduan/technical/git/)[1: Repositories](https://www.sbf5.com/~cduan/technical/git/git-1.shtml)[2: Branching](https://www.sbf5.com/~cduan/technical/git/git-2.shtml)[3: Merging](https://www.sbf5.com/~cduan/technical/git/git-3.shtml)[4: Collaborating](https://www.sbf5.com/~cduan/technical/git/git-4.shtml)[5: Rebasing](https://www.sbf5.com/~cduan/technical/git/git-5.shtml)

## Introduction

This is a tutorial on the [Git](http://git.or.cz/) version control system.

Git is quickly becoming one of the most popular version control systems in use. There are plenty of tutorials on Git already. How is this one different?

## A Story

When I first started using Git, I read plenty of tutorials, as well as the user manual. Though I picked up the basic usage patterns and commands, I never felt like I grasped what was going on “under the hood,” so to speak. Frequently this resulted in cryptic error messages, caused by my random guessing at the right command to use at a given time. These difficulties worsened as I began to need more advanced (and less well documented) features.

After a few months, I started to understand those under-the-hood concepts. Once I did, suddenly everything made sense. I could understand the manual pages and perform all sorts of source control tasks. Everything that seemed so cryptic and obscure now was perfectly clear.

## Understanding Git

The conclusion I draw from this is that **you can only really use Git if you understand how Git works.** Merely memorizing which commands you should run at what times will work in the short run, but it’s only a matter of time before you get stuck or, worse, break something.

Half of the existing resources on Git, unfortunately, take just that approach: they walk you through which commands to run when, and expect that you should do fine if you just mimic those commands. The other half does go through all the concepts, but from what I have seen, they explain Git in a manner that assumes you already understand how Git works.

This tutorial, then, will take a **conceptual approach** to Git. My goal will be, first and foremost, to explain the Git universe and its objectives, and secondarily to illustrate how to use Git commands to manipulate that universe.

- I will begin by describing the Git data model, the repository.
- From there I will describe the various operations Git provides for manipulating the repository, starting from the simplest (adding data to a repository) and moving through the more complex operations of branching and merging.
- I will then discuss how to use Git in a collaborative setting.
- Finally I will look at the Git rebase function, which provides an alternative to merging, and consider its pros and cons.

[Go on to the next page: Repositories](https://www.sbf5.com/~cduan/technical/git/git-1.shtml)

Copyright © 2000-2019 Charles Duan.

My e-mail address is “website.comments” (without the quotes) followed by an @ symbol, my first initial and last name concatenated, a dot, and “com.”