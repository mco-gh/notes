Vim Is Saving Me Hours of Work When Writing Books & Courses

Updated on February 12th, 2019 in [#dev-environment,](https://nickjanetakis.com/blog/tag/dev-environment-tips-tricks-and-tutorials)  [#linux](https://nickjanetakis.com/blog/tag/linux-tips-tricks-and-tutorials)

# Vim Is Saving Me Hours of Work When Writing Books & Courses

![](../_resources/8f6b2cf5fe209d4e4ef665329c512421.png)

## When writing a book or course, you deal with hundreds of thousands of words and Vim helps you manage that in a sane way.

 **Quick Jump: **  [What's Involved with Creating a Course?](https://nickjanetakis.com/blog/vim-is-saving-me-hours-of-work-when-writing-books-and-courses#what-s-involved-with-creating-a-course)  |  [Dealing with File Names](https://nickjanetakis.com/blog/vim-is-saving-me-hours-of-work-when-writing-books-and-courses#dealing-with-file-names)  |  [Adding Polish to Screencasts without Editing](https://nickjanetakis.com/blog/vim-is-saving-me-hours-of-work-when-writing-books-and-courses#adding-polish-to-screencasts-without-editing)

As I get closer to finishing a course I’m working on, I try to think of ways to improve my workflow so that the next course is easier to create.

That means evaluating everything from audio and video hardware, to code editors and even [operating systems](https://nickjanetakis.com/blog/i-tried-linux-as-my-main-dev-environment-but-was-forced-back-to-windows).

**This article is focused on organizing and dealing with large amounts of text**. This could apply to books, courses, notes or anything really.

After having used terminal Vim + tmux together inside of WSL for the last 2 weeks I’m already more productive than with my previous VSCode set up.

[tmux](https://nickjanetakis.com/blog/who-else-wants-to-boost-their-productivity-with-tmux) is especially useful for anyone who juggles multiple projects. I’m always switching between freelance dev work, my blog, open source projects, side projects and courses. Being able to hit a tmux hotkey to flip to any given project and have everything be immediately loaded and ready to go is awesome.

I was doing that before with tmux and VSCode, but opening and moving around VSCode to the right size was always something I had to do manually.

That might sound trivial, but it’s not. Every time you do it, it puts you into a negative mindset where you think *“sigh, now I have to visually organize this again”*.

One of the biggest drawbacks to Windows is how tedious it is to manage window layouts, which is funny given the OS is called Windows. Ever since I tried i3 as a window manager on Linux, I simply can’t go back to anything else.

So for the last few weeks while writing my course I’ve been looking for ways to replicate as much as i3 as possible within Windows and using terminal Vim inside of WSL along with tmux gets me close for doing anything in a terminal.

So that’s one of the main reasons why I chose to give Vim a shot. It wasn’t necessarily due to VSCode as an editor being too limiting, although I did eventually find it to be unsuitable after I really thought about improving my course creation workflow.

### What’s Involved with Creating a Course?

It’s a multi-month investment that is comparable to writing a book, except there’s additional complexity added because you’re not just writing something that people will read.

For example, with a book, you have a table of contents, chapters and then text that belongs to each chapter. You can write your book in whatever format you prefer and then export it to PDF when you’re done. You only need to worry about what the PDF looks like.

A course is pretty similar to that. It has a table of contents, sections and lessons. The sections are just a way to group up lessons, and the lessons are text based scripts that you plan to deliver on video.

For example, the course I’m currently working on now has 24 sections and 158 lessons. Each of these lessons have about 2,000 words. There’s roughly 300,000 words of text and the course isn’t done yet.

Each one of those lessons will eventually be turned into a video that’s anywhere between 2 and 20 minutes long. It really comes down to how many words were written for that lesson.

So now let’s talk about some of the problems I deal with to organize this content.

All of the below problems are in the context of what I was doing before I started using Vim and at the end I will go over how I addressed them with Vim.

### Dealing with File Names

My current approach to all of this is to create a `scripts` folder for a specific course and inside of that folder I create individual folders for each section and in those section folders I have individual files for each lesson.

It looks like this:

	├── 001-introduction-and-setup
	│   ├── 001-welcome.txt
	│   ├── 002-downloading-the-starter-files.txt
	│   ├── 003-tooling-setup.txt
	├── 002-foobar
	│   ├── 004-example.txt

In other words, I manually order each section and lesson with a number, and the lesson numbers don’t get reset for each section. It goes from 1 all the way until the last lesson.

Things get even more interesting too because I also have a separate git repo that has numbered folders that match up to a specific lesson. It’s really important that the lesson numbers and the git repo folder numbers line up in the end.

But, as you can probably see, this approach is terrible for when you need to add a lesson into the middle of the course. Imagine adding a lesson in after number 50 which is now 51. That means you need to manually increment every lesson after 50 by 1 which sucks.

On that note, it’s nearly impossible to come up with a final table of contents up front for a course because the lessons aren’t possible to predict.

I need to write the scripts and play with it as I go. I don’t even come up with a lesson’s title until I’m done writing it, and since the duration of the video is important, the number of words in the lesson really dictates when one lesson flows into the next.

To help combat that problem right now what I typically do is create a single file for each section, write out all of the lesson scripts for that whole section and when I’m really happy with it then I break it up into manually numbered files.

So that’s how I deal with things now. I number things manually and try to reduce the chances of having to add in lessons later. If I do have to add one in (which happened twice during this course so far), I bite the bullet and rename everything manually.

Another pain point with this approach is if I want to change a lesson title, I need to go to the file system and change the file name manually. This might seem like a minor thing, but it adds friction to the writing process. It really does.

Lastly, on a regular basis I’m always making sure that one lesson flows nicely into the next one, so if I’m working on lesson 5, I often open up lesson 4, scroll to the bottom of the file, read what I wrote and then make sure I start lesson 5 in a way that flows naturally. It’s a lot of jumping between files.

#### Potentially Solving Some of These Problems with My Existing Tools

I played around with the idea of not numbering them at all while keeping a separate YAML table of contents file around. Then I could write a little Python script to read in that TOC file and programatically number all of the sections and lessons when the course is done.

I’m sure I could get that to work but now I need to keep a separate table of contents in sync with the actual files. Dealing with the file names themselves is annoying enough and this solution doesn’t address that. It just seems like adding more fuel to the fire.

Although it is worth mentioning, unlike a book, a course isn’t just a single exported PDF file. I want people to be able to stream the course on my site, which means there needs to be a table of contents created within the course platform’s back-end.

Ultimately that is what people will be interacting with, not these script files directly, so really these section folders and lesson files on my dev box don’t need to exist. They just need to be numbered so I can associate them to folder numbers in a git repo.

#### Ideal Solution in a Perfect World

It would be really nice if I didn’t have to think about the ordering of the sections and lessons beyond what order they appear in the code editor.

Basically, if I have a list of lessons like this:
1. Welcome
2. Downloading the Starter Files
3. Tooling Setup

I only want to deal with the lesson titles in a human readable way and not deal with numbers. If I wanted to rename a lesson, it only gets renamed in that one spot and if I wanted to move a lesson down, I would only have to move the line down and the lesson numbers would get automatically updated.

On that note, if I add a new lesson somewhere in between, all of the other lessons below it would get their numbers adjusted. This goes for section numbers too. But keep in mind, the lesson numbers would be indexed across all sections. Each section wouldn’t have its own separate index of lessons.

I also don’t want to deal with manually having to create a `tooling-setup.txt` file.

Another important thing is lesson isolation. If I click into or expand the Tooling Setup lesson, I only want to see that lesson’s text, but at the same time, maybe sometimes I would want to see the previous or next lesson’s text so I can quickly see how they start and end.

With that said, it’s not just isolation to help keep me focused. It would be nice to be able to jump to the start, middle or end of the lesson and not have it apply to the entire section or course. Especially when searching for text.

But on that note, being able to operate on the entire course’s text at times would be super handy. For example, I could search for phrases like “for example” to see how many times I’m saying that, and try to use alternative phrases to make things sound a bit less systematic.

Truthfully I don’t read these scripts word for word when I deliver the video. They are mainly to help me organize my thoughts, but I do use them as a guide when recording the videos.

#### Solving the Problem with Vim

I wrote the above ideal solution before I even knew what editor and tools I was going to use. I think this is a great way to discover not only what the problem is, but how you can solve it.

One of the only technical books I ever read was [SICP](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs) (Structure and Interpretation of Computer Programs) and in that book they talk about a concept called “wishful thinking”.

In the context of the book, they talk about designing your software under the assumption that certain libraries or functions will exist before you write them. This lets you focus on designing the API of your application and fill in the details later.

That’s kind of what I did here, but in a different context.

##### Creating one massive 300,000 word file:

I started to think about the problem in reference to my ideal solution. A big component of my overall problem was dealing with individual file names.

So why not just eliminate the files in the first place and use 1 large file?

I didn’t have a giant file to test this on but it only took a few seconds to create one based on the files I already had. I just opened a Bash prompt in WSL and ran `cat */*.txt > all.md`.

Now I had a 300,000 word markdown file that was roughly 1.5MB in size. I decided to try opening it with my existing VSCode set up and Vim. In both cases I kept plugins enabled and both editors had plugins to deal with markdown.

**Surprisingly enough VSCode** opened this file pretty quickly. It only took about 3 seconds and even typing into the file felt just as fast as a smaller file.

However, just having the file open without doing anything used 50% of my overall CPU on an i5 3.2ghz quad core and jumped to 65% when typing.

That’s not really going to cut it. This is a file I’m going to have open every day for months. It can’t overtake my entire computer. By the way, it also used 800MB of RAM but honestly I don’t mind that too much since I have 16GB of RAM.

**So then I opened the same file in Vim**. Vim took about the same amount of time to open, but it used less than 10MB of RAM, 0% CPU when open and jumped to 3-4% CPU load when typing in the middle of the document.

It felt just as fast to type into as it did with a smaller file. It even handled typing ** to start bold text with markdown and it was instant, even while it was bolding 300,000 words.

That was a much better result than I could have asked for, especially since Vim is directly running inside of WSL which is known to be pretty slow. I imagine it would have been even faster on a native Linux system.

##### Setting up a realistic worst case scenario:

What if I had a 900,000 word file? There’s really no way I would end up with more than 500,000 words in a course but I figured it would be a good idea to see what happens.

900,000 words took 10 seconds to open with Vim, but once I was in everything felt just as good as the 300,000 word file. There was about a half second delay going in and out of insert mode, but that was the only difference. RAM and CPU usage was roughly the same.

In case you’re curious, VSCode performed about the same as it did with 300k words too. In this case, VSCode actually opened up the file quite a bit faster than Vim, but then again, this is 100% due to Vim running in WSL, while VSCode was running in Windows directly.

##### Navigating around sections and lessons in a single big file:

There’s no point comparing VSCode anymore since I’m not going to be using it, so this will be focused specifically on Vim.

The [vim-markdown](https://github.com/plasticboy/vim-markdown) plugin is absolutely fantastic and really makes all of this doable.

**I’m someone who typically doesn’t like code folding, but code folding turned out to be the best thing ever** for this approach and the vim-markdown plugin has first class support for dealing with folding based on markdown headers.

That means I can open the file with all folds closed, and then jump to the lesson I want to work on and unfold it within seconds. It works out beautifully.

This plugin also supports jumping between headers using `[[` and `]]`, so I can easily jump to previous and next lessons.

Vim is also aware of how code folds work, so you can perform searches and manipulate text for only the folds that are open. This gives me everything I wanted from my ideal solution because if I want to act on the whole file, I can just hit a hotkey to unfold everything.

Plus on top of all of that, there’s [fzf.vim](https://github.com/junegunn/fzf.vim) which lets you fuzzy search lines in the buffer (among other things). It’s a superb choice for finding phrases. Seriously, [junegunn](https://github.com/junegunn) is an amazing author of developer productivity tools. He made FZF and a few other tools.

Epic.

##### Numbering sections and lessons:

The vim-markdown plugin also happens to have a handy command called `:Toc` which will create an entire table of contents based on your headers. This TOC is generated in a separate buffer, and you can even click on the headers to jump to the area in the real markdown file.

This behavior is pretty much exactly what I want. I don’t need to know the lesson numbers all the time. It’s only when I want to know the count, or want to tie a lesson number back into a git folder number outside of Vim.

Currently the plugin doesn’t support numbering the headers in the TOC output, so I [opened an issue on GitHub](https://github.com/plasticboy/vim-markdown/issues/413), but this problem is solvable for now, it’s just a little less integrated.

For example, all of my sections use `#` and all of my lessons use `##` so all it takes is a little Bash magic to parse the file. For example, you could grep through the file and pull out lines that start with `#` and now you have a list of all sections, etc..

I haven’t come up with a perfect script yet but I’m 100% sure it’s possible and that’s all I care about for now. Who knows, by the time I finish my current course maybe the author of vim-markdown will build this into his plugin.

##### Improving scroll speed in large files:

In WSL I noticed with relative line numbers that scrolling around even small files with 100 lines was very slow. We’re talking multiple seconds of lag between scrolling and seeing the cursor move.

It turns out relative line numbers were mostly to blame but I didn’t want to lose them. After applying both of the settings below, scrolling became fast again, even in a 900,000 word file. It was funny seeing a file with over 100,000 lines.

	set lazyredraw
	set regexpengine=1

##### Speeding up code folding:

By default code folding inside of the 300,000 word file was unbearably slow. Even just having the file open made it pretty much unusable but after a little bit of research I found a plugin that worked perfectly.

Adding the [FastFold](https://github.com/Konfekt/FastFold) plugin to my vimrc instantly fixed the problem. It went from unusable to awesome. It basically changes when folds are updated.

### Adding Polish to Screencasts without Editing

When it comes to creating courses on technical topics such as programming you find yourself spending a lot of time recording your code editor.

This is where you’ll be looking at, writing and explaining code on video.

When recording I often use a very large font size and a noticeable cursor so it’s easier to follow what I’m talking about but one thing I started to do recently was add in special effects to emphasis text after I record the video.

![post-production-highlight-text-e2ce658d64b02568810f4e27fc4bd0421a2d620ae9e220bc40aeb0af04a6cdb6.jpg](../_resources/5865fb267bd17724de9dc1dcaaf27320.jpg)

For example, after I record the video, during the editing phase I would often dim most of the screen and highlight a specific area of the code just to make it even more clear on what we’re talking about.

I’ve gotten a lot of people say they really liked this effect, and a number of people have said my [Dive into Docker course](https://diveintodocker.com/?utm_source=nj&utm_medium=website&utm_campaign=/blog/vim-is-saving-me-hours-of-work-when-writing-books-and-courses) was the highest production quality course they’ve ever taken.

However, this production quality comes at a price. It takes a long time to go through hours of video and manually highlight the areas I want.

It just so happens Vim has a plugin called [limelight.vim](https://github.com/junegunn/limelight.vim) that lets you do this in real time. It is written by the same author who made FZF.

![68747470733a2f2f7261772e6769746875622e636f6d2f6a756e6567756e6e2f692f6d61737465722f6c696d656c696768742e676966](../_resources/ee7c266a1cdae6b984b365ba094fd131.gif)

It automatically highlights the area where your cursor is, and you can tweak things like the dimmed color and opacity so you can make it look great with any color theme.

This means I can turn on limelight and not have to manually add dims and highlights to the screen in post production editing. This alone saves hours. At the moment VSCode has nothing like this, but I imagine it could be made. I know there’s an Emacs port of it.

I’m going to give that a shot when I’m ready to record my upcoming course.

In the end, I’m really happy to have given Vim a second chance. I wrote it off a long time ago but now it’s chalking up to be one of the most important tools in my tool chain to write code and create courses. Expect more Vim posts to come in the future.

**What Vim tips do you have for writing? Let me know below.**