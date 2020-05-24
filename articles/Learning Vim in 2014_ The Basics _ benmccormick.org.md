Learning Vim in 2014: The Basics | benmccormick.org

##### June 30, 2014

# Learning Vim in 2014: The Basics

Do you want to be efficient writing code? Using Vim can be a powerful help. Using it has let me move more effectively through the process of writing and editing code. But getting to where I am now was frustrating. Vim resources are scattered across the web, and contain a lot of different advice. It’s tough to figure out how to make Vim work for you. In my next few posts, I’m going to talk about the process of learning a 23 year old programming power tool, and what you need to know in 2014 to be productive with Vim. Today I’ll start with the basics, stuff that goes back all the way to the 1970s, and we’ll grow from there.

### Why has Vim Survived?

Vim has been around for a while. Originally released in 1991 as an improvement on vi (which had been around since 1976), it has outlasted a generation of programmers. The software world has changed a lot since 1991. So why do people still use it?

Vim provides a system for editing text that is quite simply more powerful than its modern graphical based alternatives. It asks a lot of its users. To use Vim effectively you have to internalize the syntax for many commands that have better affordances on other editors. But you’re rewarded with a friction-free editing environment. Vi’s commands are fast, composable, and powerful. So let’s get started.

### Step 0: Setup

The first thing you need to do is install a copy of Vim. If you’re on a Linux or Mac system, there is likely already a system copy, but it is probably not up to date. So use your system’s package manager to get the latest version (7.4 at the time of this writing). For Mac users I recommend using [Homebrew](http://brew.sh/) to download [MacVim](https://code.google.com/p/macvim/). Windows users can download the latest executable on [Vim.org](http://www.vim.org/download.php).

The second thing you’ll need is a vimrc (the file vim uses for configuration). These files can become quite extensive, setting up many different options, configurations, and plugins. But we’re going to start simple. Download [this minimal vimrc file](https://gist.github.com/benmccormick/4e4bc44d8135cfc43fc3) and install it in the appropriate directory for your OS as instructed. If you already have a .vimrc file but don’t understand it, I’d recommend saving it elsewhere and using a minimal one for now. You can then build it out as you learn more.

### Step 1: Learn the Syntax

Just like a programming language, the first thing to learn for Vim is the basic syntax. Vim has a built in tool to help you get comfortable called vimtutor. It’s a text file set up to help you learn to navigate Vim. Once vim is installed you can run it by calling vimtutor on unix-style systems. On Windows you can follow the instructions [here](http://superuser.com/questions/270938/how-to-run-vimtutor-on-windows). It will take you through a series of 7 lessons that will familiarize you with the basic commands.

Vim has rather non-standard commands, and it may be frustrating at first adapting to its different terminology and conventions. The payoff comes slowly, but it does come.

#### Modes

The most important thing to understand is that Vim is a modal editor. At any given time you’re in one of 6 modes. You will have different abilities and keystrokes available to you in each of these modes. For right now the key modes to understand are Normal Mode, Insert Mode, and Command line Mode.

Normal Mode is the default mode. It’s roughly equivalent to the state that other editors are in when you’re holding down the ctrl or cmd keys. Instead of entering text onto the screen, different keys trigger different commands. Initially this is a bit weird. Those of us coming from other editors or IDEs are used to being able to type text by default. The thought is that adding text is the primary task in a text editor. But Vim treats adding text as sitting on equal footing with editing, deleting and manipulating existing text, and starts us in a mode where we can quickly make any change. To steal an analogy from Drew Neil, normal mode is the opportunity to take our paintbrush off the canvas while we decide our next stroke.

Insert mode is the equivalent of most editor’s normal state. When you type a key in normal mode, it appears on the screen. You can enter insert mode by pressing ` i ` in visual mode, and exit it by hitting ` <esc> `.

Command line mode lets you enter ex-commands, a command line language that complements normal modes shortcuts. You enter it by hitting ` : ` in normal mode. Important commands are ` :w ` to write (save) a file, and ` :q! ` to quit.

The above commands, and an understanding of the modes are enough for you to survive in Vim, and treat it as a sort of awkward Notepad clone. You can edit files, save them, and quit. Going through vimtutor will introduce you to many more commands, and a few more modes. But you can learn those at your own pace. Right now you want to see what taking time to learn this awkward unfamiliar syntax can buy you.

### Step 2: Learn the Language

Vim’s key commands are different than you’ll find in other editors like Sublime Text. They’re not a series of standalone actions that you can do one after another to get what you want. Instead they form a language.

Vim statements are made up of actions and motions. The actions are what you’re trying to do, the motions are where you want to do them.

For example let’s take the ` d ` action. ` d ` deletes. You can delete a single character by typing ` dl `. You can delete 2 characters by typing ` d2l `. You can delete a whole line by typing ` dd `, or delete inside a word by typing ` diw `.

Once you learn the d action, you can use it with every motion you know. Similarly, when you learn a new motion, you can then use it with every action you know.

So if somebody shows me the ` y ` action and tells me that it yanks (copies) text, I’ll know I can yank a character with ` yl ` a line with ` yy ` and inside the current word with ` yiw `. Each new Vim command is a tool in your toolbox, and since the tools build off of each other they become exponentially more valuable.

### Step 3: Learn the Mindset

Vim can make you hyper-efficient. But to get there you need to know more than just the command combinations available. You have to shift your mindset. Vim commands aren’t just easy to learn, they’re designed to be repeatable. Bram Moolenar, Vim’s creator has listed out [7 habits of effective text editing](http://www.moolenaar.net/habits.html). The second habit, don’t type it twice, is a pretty good summary of the “Vim Way” of doing things.

Vim provides a bunch of ways to avoid repetition. I’ll get into them in another post. For now though, let’s take a look at ` . `, the dot command. The dot command repeats the last action you’ve taken. For instance, you can use ` ciw ` to change a word, hit ` <esc> ` to return to normal mode, then move to another word and type ` . ` to replace that word as well. You are able to avoid retyping the replacement word as well as the ` ciw ` command. You can run the whole replace with one keystroke, regardless of what words you’re replacing. Like other Vim commands, the dot command is small on its own, but gains power as you add more tools to your toolbox.

### More Resources

If you enjoyed this article you’ll probably also enjoy

- [Practical Vim](http://www.amazon.com/gp/product/1934356980/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1934356980&linkCode=as2&tag=benmccormicko-20&linkId=FE3JFKHYVRYCUOVS)![ir.gif](../_resources/accba0b69f352b4c9440f05891b015c5.gif): This amazing book by Drew Neil, the creator of [Vimcasts](http://vimcasts.org/) was the single best resource I found as I learned Vim. I highly recommend it for anyone who uses Vim.
- [Everyone Who Tried to Convince Me to use Vim was Wrong](http://yehudakatz.com/2010/07/29/everyone-who-tried-to-convince-me-to-use-vim-was-wrong/): This blog post is another take on how to start learning Vim, by Yehuda Katz, the prolific developer who’s a core member of the Rails, EmberJS, and jQuery teams.
- [Janus](https://github.com/carlhuda/janus): Janus is another Yehuda Katz project. It’s a starting configuration for Vim meant to make it feel more comfortable for developers who want to come in and be productive immediately. I personally found that it didn’t work for me. The plugin list overwhelmed me and prevented me from learning the basics. But it may be a better fit for some people and is a great place to look to see configuration ideas and plugins that you can try out on your own.

* * *

* * *

Thanks for taking the time to read this post! Software tooling is one of the main topics of this blog, so if you enjoyed the post, please consider subscribing by using the feed, Twitter or my mailing list.

###### EMAIL

###### RSS

[*Created with Sketch.*  RSS](https://benmccormick.org/rss/)

###### TWITTER

Site Feed:

[**Follow **@benmccormickorg**](https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=benmccormickorg&tw_p=followbutton)

Personal Feed:

[**Follow **@ben336**](https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=ben336&tw_p=followbutton)

###### You Might Also Like:

### [Learning Vim in 2014](https://benmccormick.org/learning-vim-in-2014/?readNext=true#title)

A series of beginner level articles on Vim

* * *

### [Vim Workflows: File Switching](https://benmccormick.org/2014/11/10/vim-workflows-file-switching-strategies/?readNext=true#title)

A look at the different approaches you can take to managing files in Vim

* * *

### [Learning Vim in 2014: Vim as Language](https://benmccormick.org/2014/07/02/learning-vim-in-2014-vim-as-language/?readNext=true#title)

An explanation of the grammar behind Vim

* * *

- [0 comments]()
- [**Ben McCormick**](https://disqus.com/home/forums/benmccormick/)
- [Login](https://disqus.com/embed/comments/?base=default&version=aadcd4f143849a30b1bb7a63b4e78edd&f=benmccormick&t_u=http%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&t_e=Learning%20Vim%20in%202014%3A%20The%20Basics&t_d=Learning%20Vim%20in%202014%3A%20The%20Basics&t_t=Learning%20Vim%20in%202014%3A%20The%20Basics&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend](https://disqus.com/embed/comments/?base=default&version=aadcd4f143849a30b1bb7a63b4e78edd&f=benmccormick&t_u=http%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&t_e=Learning%20Vim%20in%202014%3A%20The%20Basics&t_d=Learning%20Vim%20in%202014%3A%20The%20Basics&t_t=Learning%20Vim%20in%202014%3A%20The%20Basics&s_o=default#)
- [⤤Share](https://disqus.com/embed/comments/?base=default&version=aadcd4f143849a30b1bb7a63b4e78edd&f=benmccormick&t_u=http%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&t_e=Learning%20Vim%20in%202014%3A%20The%20Basics&t_d=Learning%20Vim%20in%202014%3A%20The%20Basics&t_t=Learning%20Vim%20in%202014%3A%20The%20Basics&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&version=aadcd4f143849a30b1bb7a63b4e78edd&f=benmccormick&t_u=http%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&t_e=Learning%20Vim%20in%202014%3A%20The%20Basics&t_d=Learning%20Vim%20in%202014%3A%20The%20Basics&t_t=Learning%20Vim%20in%202014%3A%20The%20Basics&s_o=default#)

![Avatar](../_resources/713bb211dca17435d03c079149496a65.webp)
Start the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&version=aadcd4f143849a30b1bb7a63b4e78edd&f=benmccormick&t_u=http%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&t_e=Learning%20Vim%20in%202014%3A%20The%20Basics&t_d=Learning%20Vim%20in%202014%3A%20The%20Basics&t_t=Learning%20Vim%20in%202014%3A%20The%20Basics&s_o=default#)

Be the first to comment.

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe  *✔*](https://disqus.com/embed/comments/?base=default&version=aadcd4f143849a30b1bb7a63b4e78edd&f=benmccormick&t_u=http%3A%2F%2Fbenmccormick.org%2F2014%2F06%2F30%2Flearning-vim-in-2014-the-basics%2F&t_e=Learning%20Vim%20in%202014%3A%20The%20Basics&t_d=Learning%20Vim%20in%202014%3A%20The%20Basics&t_t=Learning%20Vim%20in%202014%3A%20The%20Basics&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=benmccormick&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)

[noavatar92.7b2fde640943965cc88df0cdee365907.png.webp](../_resources/3a8e81a1424aeb37b1609aa61b270038.bin)![449266.gif](../_resources/9606fa62df0ffe87253f3baf418f0e42.png)[ema](../_resources/6d22e4f2d2057c6e8d6fab098e76e80f.gif)