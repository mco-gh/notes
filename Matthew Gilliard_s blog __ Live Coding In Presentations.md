Matthew Gilliard's blog || Live Coding In Presentations

# Live Coding In Presentations

  Oct 25, 2018

- [conference](http://blog.gilliard.lol/tags#conference)

- [devrel](http://blog.gilliard.lol/tags#devrel)

Today was a first for me. I have been to many conferences in my career but today was the first time that *every single talk* included a live-coded demo. I mean the speaker jumped out of their slide deck, opened a terminal window and started typing commands. One brave soul only had 3 slides: *Hello*, *Live Demo*, *Thanks for listening*.

![presentation-code.jpg](../_resources/72e16186c2c8ce850da4455cf36170e0.jpg)*[@mirocupak](https://twitter.com/mirocupak/) showing how it’s done*

I have to say that I absolutely love this style of presenting. Firstly seeing someone actually do *the thing* is 100x more meaningful to me than describing *the thing*. Then there’s a touch of authenticity that I’m listening to someone who really understands the technical side of what they’re talking about. And we shouldn’t forget the exciting risk that it might all go horribly wrong and be entertaining for all the wrong reasons.

Personally I try to keep some live demos and/or code in each of my talks, and frankly they take a lot of time to devise, set up and practise. A simple slideshow-and-talk would often be much quicker. And I often worry that I’m not doing it well/making some mistakes/being stupid, so after seeing so much live-coding in talks today I [asked for advice](https://twitter.com/MaximumGilliard/status/1055427965947928576) about doing it and am distilling my thoughts and those from the people kind enough to reply into a list of…

## Tips for live coding during a presentation

### Preparing the Scene

- **Know what is and isn’t relevant to your talk:** Time is of the essence (you have a lot to say after all) so make sure to keep the irrelevant bits as quick as possible, or better yet avoid them. Some sleight-of-hand is OK here.

- **Preparation I:** If you are working on a VM, have it booted beforehand. Unless your talk is actually about booting VMs, those 45 seconds are *just* long enough for the audience to lose focus on what you’re doing. I’m looking at you, Minikube.

- **Preparation II:** Install the tools you need beforehand. People don’t want to watch you run `apt install tree` or whatever it is. If you’re demoing on a fresh VM (which I like to do) then script the setup of the VM somehow, as you’ll likely be doing it several times. Your audience’s time is a coin to be spent wisely.

- **Resetting the environment:** You should also automate resetting all the files you need back to the state you want at the start of your talk. Usually there’s a config file that you’ve edited or some output logs which need tidying up. Just write a `prepare-for-demo.sh` or use `git reset --hard && git clean -fdx` and be done with it.

- **Preparing text files:** If you need several similar files (for example, several evolutions of the same config file), create them all in advance and give them discriptive names. Don’t be building them up by editing during the talk - your time is better spent talking about your topic. Jokes about how you find vi hard to use are not as evergreen as you might think. If your topic is ‘editing text files’ then disregard this advice.

- **Structuring your talk:** Compared to slides, it can be harder for the audience to follow the structure of a live coding section, and to catch up if they lose track. This is especially true for people who are new to your topic. I like to have a pretty clear agenda for my talks, even having numbered sections sometimes, so it’s (hopefully) easy to anchor what I’m doing in the overall story. I also jump back and forth between slides and the terminal quite frequently. Whatever your style, be thoughtful about how your audience can know where they are and what you’re doing.

### Terminal Trouble

- **Colour scheme:** I usually find black-on-white easier to read on cheap/weak projectors. If you get a chance to try it out beforehand then do so. Colourised terminals are wonderful to use up close but be aware that projectors aren’t as good as monitors, and other people may perceive colours differently to you. In any case make sure there is good contrast between the text and the background.

- **Font size:** Bigger is better, up to a point. In the 5 minutes before you start you can open a terminal and make it the right size. I enjoy running to the back of the room to check it myself as it gives me a chance to chat to people as they arrive and gives me some way to use up my nervous energy. Resizing the font on the fly is OK but it’s annoying if that also resizes the terminal window and you lose time dealing with that. Learn your keyboard shortcuts, and ask people at the back for a thumbs-up.

- **Font size II:** If the text is so large that lines wrap and it all becomes messy then you have a problem. What is the longest line in your demo? How does it look? Maybe you have to break it into multiple lines with backslashes. Learn what `ctrl-x-e` does in your shell.

- **Prompt:** I have spent more hours than I care to admit making a beautiful and info-dense CLI prompt. But in a presentation the calculations for the value of screen real estate are different. Something like `export PS1=$'conf-name:topic\n> '` has worked well for me in the past - people don’t usually care about the name of your cwd. If you have several demos, consider different prompts so that people can tell easily that you’re using a different terminal

- **Commands I:** Use `alias` judiciously. We all make a lot of typos, especially under pressure. `alias k=kubectl` goes a long way to fixing that (as well as saving time, and actually being a useful tip for your audience too).

- **Commands II:** Long commands - typing is slower than talking, and *a lot* slower than thinking. `ctrl-r` is your friend. I like to hashtag/comment my commands like:

	export JAVA_HOME=/home/mjg/tools/jdk/jdk-11 *#jdk11*

then `ctrl-r #jdk11` will find it easily. You can concentrate on explaining the important bits of the command without worrying about fat fingers. Try to not include unnecessary options and flags.

- **Showing file contents:** If you need to show what’s in a config file, or some source code, `cat` doesn’t cut it. I prefer something with syntax highlighting, like maybe vim or my new favourite: [bat](https://github.com/sharkdp/bat).

### Switching between code and slides

- **Making the switch**: I have yet to find a nicer way to do this than having the slides and terminal(s) on separate workspaces in i3wm. If you are using an inferior window manager (ie *any other* window manager) then you may be stuck with un-fullscreening the slides (which shows the ugly slide editing interface), alt-tabbing to the terminal and carrying on. Mac OS handles full-screen apps especially weirdly and is notably awful at this.

- **Why not both?** Once nice trick I have seen is to have a mostly-blank slide with a diagram in the corner and using a transparent background terminal on top of it, to show text and diagram at once. YMMV but it worked nicely when I saw it.

### Dealing with multiple monitors

- **Beware of the edges:** A lot of times there will be people who can’t see the whole screen. The bottom of the screen is especially likely to be hidden behind the head of the tall person in front, so try to keep the action in the top half if you can. `ctrl-l` is helpful here. Also, check if the projector is misaligned with the screen - you can often lose a couple of characters off the left or right.

- **Speaker notes, terminals and mirroring:** I face this problem often - I have some slides with speaker notes, so I need to use a dual-monitor setup for that part of my talk, but then during the coding part I *need* to see the terminal so I want the screens to be mirrored. This is tricky. The best AV setups will have a small front-of-house monitor showing you what’s on the big screen behind you, but smaller venues won’t have this and it’s very awkward to type onto a terminal that’s over your shoulder. If you’re on Linux then a couple of scripts with `xrandr` might do the job but it’s still fiddly. I would avoid any screen management GUI control panels as a waste of precious time. One interesting solution I saw was to use tmux with two terminal clients attached, one on the laptop screen and one on the big screen.

### When it goes wrong

- **It inevitably will go wrong, have a plan:** No matter how careful you are it’s easy to forget something, or do things in the wrong order. Have a sense of humour and be prepared to explain what *should* have happened. Don’t get carried away trying to debug it - often someone in the audience will have spotted your mistake so if the thing is critical then you can just ask. My worst experience of this was typo-ing a command which left a root-owned file in the cwd then docker refused to build images. I was at the point of blowing off the whole demo (which would have made for a crappy talk TBH) when some kind soul in the 3rd row schooled me on what I’d done.

- **Progress ##……..:** Do you depend on internet connectivity during your talk? Do you need to? I watched Kelsey Hightower deal with a dropped wifi connection during his DevNexus *keynote* by calmly tethering to his phone and making a joke about his data plan. Are you as smooth as Kelsey? Is there *any way at all* to do your demo without relying on internet connectivity? At least do all the big downloads in advance.

- **For irrecoverably bad situations:** I’m told that a hugely helpful thing to have in your back pocket, in case of total failure, is a video of you successfully doing *the thing*. I’ve never actually done this myself so if you have recommended tools for doing this then let me know - I’ve had both Quicktime and [Asciinema](https://asciinema.org/) recommended.

## Summarizing

OK this post has turned out to be wayyyy longer than I expected, but I hope it’s helpful. Thanks to all who contributed on Twitter and elsewhere. If you have more comments or suggestions please share, and Rock On with Live Coding in your talks!

Big thanks to [@NikhilNanivade](https://twitter.com/NikhilNanivade)  [@thomasj](https://twitter.com/thomasj)  [@reclaro](https://twitter.com/reclaro)  [@mirocupak](https://twitter.com/mirocupak)  [@KateStanley91](https://twitter.com/KateStanley91) and [@Spektor03](https://twitter.com/Spektor03) for help & inspiration.