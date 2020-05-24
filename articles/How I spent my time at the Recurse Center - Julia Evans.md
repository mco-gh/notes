How I spent my time at the Recurse Center - Julia Evans

# How I spent my time at the Recurse Center

I went to the Recurse Center a while ago now (4 years ago) but I’m interested in the topic of “how do I accomplish a lot in a short amount of time” again so I wanted to revisit how I spent my time there because I learned a lot. I don’t know if this will be interesting to anyone but me but I often think about things by blogging, so here you go :)

The [Recurse Center](https://www.recurse.com/) is a place where you go for 12 weeks and spend all your time working on getting better at programming. To learn more about it I recommend the [user’s manual](https://www.recurse.com/manual).

The days are numbered 1-46 because when I was there Monday-Thursday were the only “mandatory” days. So 12 weeks is 48 days, minus 2 for some reason.

Here’s how I spent those 46 days (in order). (I know this because I [wrote a blog post every day I was there](https://jvns.ca/categories/hackerschool/)). Some of this is probably [retconned](https://en.wikipedia.org/wiki/Retroactive_continuity) at least a little bit :)

- **Day 1-3**: Work on a tiny shell in bash ([here’s the source](https://github.com/jvns/_dash/blob/master/dash.c))
- meanwhile: Learn what a shell does. Learn some basics of the Linux kernel does. Tom teaches me about netcat. Netcat is awesome, wow.
- **Day 4-6**: Learn what a Linux kernel module is. Write a couple of beginner kernel modules.
- **Day 7**: Consider learning Clojure / writing a bittorrent client in Clojure. Write a clojure echo server & decide against continuing down that path
- **Day 8-10**: Pair with Allison on her bytecode interpreter, go to a talk on Julia & open source, feel confused about what I’m going to do next
- **Day 11-16**: Implement gunzip in Julia and demo it ([gzip + poetry = awesome](https://jvns.ca/blog/2013/10/24/day-16-gzip-plus-poetry-equals-awesome/)). https://github.com/jvns/gzip.jl.
- **Day 17-18**: Read some of [Hacking : The Art of Exploitation](https://www.nostarch.com/hacking2.htm). (which is a GREAT BOOK). Do some experimentation with buffer overflows & ARP cache poisoning.
- **Day 19-20**: Get interested in networking. Talk to Jari & Brian about networking. Implement traceroute in Python
- **Day 21-27**: Work on a TCP stack in Python. (https://github.com/jvns/teeceepee)
- **Day 28-29**: Philip Guo is a resident. Inspired to make https://visualize-your-git.herokuapp.com/. (web projects were against my personal rules for being at the recurse center but I did it anyway)
- **Day 30-33**: Have fun with making music with Clojure. Write a webserver with Lyndsey that lets a crowd of people play music on your computer (https://github.com/jvns/magical-orchestra)
- **Day 34-46**: Work on writing a tiny operating system in Rust (https://github.com/jvns/puddle)

Overall:

- 13 days on writing a mini Rust OS (500 lines of Rust). https://github.com/jvns/puddle
- 9 days on learning about networking & writing a TCP stack in Python (200 lines of Python + tests). https://github.com/jvns/teeceepee
- 6 days on gzip in Julia (360 lines of Julia). https://github.com/jvns/gzip.jl
- 3 days on writing a shell in C (250 lines of C, with Daphne). https://github.com/jvns/_dash
- 3 days writing fun kernel modules (200 lines of C). https://github.com/jvns/kernel-module-fun
- 2 days on a git workflow visualization tool (150 lines of Python). https://github.com/jvns/git-workflow
- 5 days on Clojure & having fun making music in Clojure (250 lines of Clojure, with Lyndsey). https://github.com/jvns/magical-orchestra
- 2 days reading a hacking book and experimenting with buffer overflows / ARP cache poisoning. (no code)
- 3 days not working on any specific project

adds up to a Recurse Center batch!

To be clear I don’t think that it’s **necessary** to spend all your time working on a Specific Project. My partner went to RC and spent most of his time not working on any specific project and still got a lot of out of it. People spend their time at RC in totally different ways and that’s okay!

some observations:

- I wrote maybe 50-100 lines of code a day on average.
- I didn’t like it when I wasn’t working on a “project”.
- I was pretty comfortable with web development / machine learning basics before RC, so I completely avoided working on those things. I focused on stuff I thought seemed hard/scary (networking/security/operating systems/writing a shell/compression). Clojure / the git visualization tool were exceptions to this, those I just thought were fun.
- The stuff I learned about at RC 4 years ago is still a lot of the same stuff I’m excited about today.
- There were a lot of things I worked on for only 2-3 days (like “write kernel modules”). Some of those things I learned a LOT from.
- I spent almost all of my time (all except 5 days) working on projects I could demo and talk about easily. But nothing I made was really that polished or anything.
- I was pretty concerned with getting a job after, a big part of why I blogged about what I was learning was that I wanted to get a cool job after the Recurse Center and so my blog was my “media strategy”. I spent 1-2 hours a day writing (which was a lot) but I did get a cool job after.
- on the other hand I was lucky that I didn’t really *need* to get a job immediately after RC, I could have easily afforded to spend a few months job hunting. So I had space to focus on learning/programming.
- all the people at RC were really amazing (other recursers / residents / facilitators). For example Lindsey encouraged me to work on writing an OS in Rust and that turned out to be a great idea. And the facilitators were always extremely enthusiastic/positive about helping me debug weird problems I had.
- Today I have a really positive attitude about debugging (what are we going to learn TODAY?!). I think I learned that from the RC facilitators <3 (like I’d ask Allison “hi can you help me debug this weird thing” and she would be SO HELPFUL)

I think this media strategy approach (“everything I do has to be a cool thing I can demo and write about”) thing is pretty weird and I don’t know that I recommend it. It worked for me though, I think it maybe helped keep me focused/motivated. I think “blog every day” isn’t actually an approach that works for most people though :).

### RC is awesome

looking back I think some of the most important things I learned at RC were:

- debugging is fun and interesting
- systems/networking/linux are extremely cool and not really that hard to get started with even if you only know a little bit of C. Like Tom told me about netcat on Day 2 and I am still VERY EXCITED about networking :)
- I learned some about unknown-unknowns – things that I didn’t know existed and wouldn’t really have thought to ask about (strace! netcat! system calls!)
- writing about what I’m learning is really fun

Want a weekly digest of these blog posts?

[Tweet](https://twitter.com/share)
[»Cool vim feature: sessions!](https://jvns.ca/blog/2017/09/10/vim-sessions/)