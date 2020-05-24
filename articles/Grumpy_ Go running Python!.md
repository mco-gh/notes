Grumpy: Go running Python!

## [Grumpy: Go running Python!](https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html)

Wednesday, January 4, 2017

Google runs millions of lines of Python code. The front-end server that drives [youtube.com](https://youtube.com/) and YouTube’s APIs is primarily written in Python, and it serves millions of requests per second! YouTube’s front-end runs on [CPython](https://en.wikipedia.org/wiki/CPython) 2.7, so we’ve put a ton of work into improving the runtime and adapting our application to work optimally within it. These efforts have borne a lot of fruit over the years, but we always run up against the same issue: it's very difficult to make concurrent workloads perform well on CPython.

To solve this problem, we investigated a number of other Python runtimes. Each had trade-offs and none solved the concurrency problem without introducing other issues.

![MeatGrinder.png](../_resources/1185d161baeea8c058cdd9ff06ecd14c.png)

So we asked ourselves a crazy question: What if we were to implement an alternative runtime optimized for real-time serving? Once we started going down the rabbit hole, [Go](http://golang.org/) seemed like an obvious choice of platform since its operational characteristics align well with our use case (e.g. lightweight threads). We wanted first class language interoperability and Go’s powerful runtime type reflection system made this straightforward. Python in Go felt very natural, and so Grumpy was born.

[Grumpy](http://grump.io/) is an experimental Python runtime for Go. It translates Python code into Go programs, and those transpiled programs run seamlessly within the Go runtime. We needed to support a large existing Python codebase, so it was important to have a high degree of compatibility with CPython (quirks and all). The goal is for Grumpy to be a drop-in replacement runtime for any pure-Python project.

Two design choices we made had big consequences. First, we decided to forgo support for C extension modules. This means that Grumpy cannot leverage the wealth of existing Python C extensions but it gave us a lot of flexibility to design an API and object representation that scales for parallel workloads. In particular, Grumpy has no [global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock), and it leverages Go’s garbage collection for object lifetime management instead of counting references. We think Grumpy has the potential to scale more gracefully than CPython for many real world workloads. Results from Grumpy’s synthetic Fibonacci benchmark demonstrate some of this potential:

![AJtJgMwyxN3KWnDrHW5JhersJGuf1SsR_lhhQoUY5gSMBjhV-BJo-vWh4JztqD7qq9pcr0JYT-niwehvDqvCmM8ZhCUAkgZFpviWnNKah5xGJCNGuMAGBdhYYhT3ZbN-HDfw_Fs3.png](../_resources/00524c95e7173af1851a17ef21003bdd.png)

Second, Grumpy is not an interpreter. Grumpy programs are compiled and linked just like any other Go program. The downside is less development and deployment flexibility, but it offers several advantages. For one, it creates optimization opportunities at compile time via static program analysis. But the biggest advantage is that interoperability with Go code becomes very powerful and straightforward: Grumpy programs can import Go packages just like Python modules! For example, the Python snippet below uses Go’s standard [net/http](https://golang.org/pkg/net/http/) package to start a simple server:

from __go__.net.http import ListenAndServe, RedirectHandler
handler = RedirectHandler('http://github.com/google/grumpy', 303)
ListenAndServe('127.0.0.1:8080', handler)

We’re excited about the prospects for Grumpy. Although it’s still alpha software, most of the language constructs and many core built-in types work like you’d expect. There are still holes to fill — many built-in types are missing methods and attributes, built-in functions are absent and the standard library is virtually empty. If you find things that you wish were working, file an issue so we know what to prioritize. Or better yet, submit a pull request.

Stay Grumpy!

*By Dylan Trotter, YouTube Engineering*

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

178 comments

[![photo.jpg](../_resources/46d0e580386337d1385bccaa4ac6a5ad.jpg)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg](:/8b2d9635d9ecd01018b3bc9a2f4f37f5)](https://apis.google.com/u/0/wm/1/115084300775078575434)

### [Tuatini GODARD](https://apis.google.com/u/0/wm/1/115084300775078575434)

[2 months ago](https://apis.google.com/u/0/wm/1/115084300775078575434/posts/GHwqX6AwRJD)  -  Shared publicly

This sad to see that Grumpy is mean to be a replacement of CPython 2.7 instead of CPython 3.x . I presume the code from youtube was written in python 2.x hence the reason but I hope we'll see Grumpy supporting python 3.x :)

+
7
7
8
7

[![photo.jpg.png](../_resources/6ebd1a2e9a3863373caa22456c53373d.png)](https://apis.google.com/u/0/wm/1/102168248469649733567)

### [Google Summer of Code](https://apis.google.com/u/0/wm/1/102168248469649733567) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/102168248469649733567/posts/dVZ2FGUqAzp)  -  Shared publicly

Grumpy, newly open-sourced, is an experimental Python runtime for Go that was built in pursuit of performance.

+
4
0
1
0

[![photo.jpg](../_resources/4c568a442d048011e398a75313e288ed.jpg)](https://apis.google.com/u/0/wm/1/116634425458974914726)

### [Andrew Cathrow](https://apis.google.com/u/0/wm/1/116634425458974914726) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+AndrewCathrow/posts/6SFgwoVYH8a)  -  Shared publicly

Interesting ...

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/b8a6e8b13818ac951c28d184695b156d.jpg)](https://apis.google.com/u/0/wm/1/109539480056944416389)

### [Kivava Chang](https://apis.google.com/u/0/wm/1/109539480056944416389) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+KivavaChang/posts/W1BbGrUfhEG)  -  Shared publicly

Google Open Source Blog: Grumpy: Go running Python!
+
2
3
2

 ·
Reply

[![photo.jpg.png](../_resources/80d63b22cda616f4e264043488c08a34.png)](https://apis.google.com/u/0/wm/1/100871979547563610033)

### [Timebender Technologies](https://apis.google.com/u/0/wm/1/100871979547563610033)

[2 months ago](https://apis.google.com/u/0/wm/1/+TimebenderIndia/posts/Yz8SLeViNkf)  -  Shared publicly

Google has built a transpiler to translate python code to Go. It sights youtube as one of the primary reasons. [#Go](https://apis.google.com/s/%23Go)

+
1
2
1

 ·
Reply

[![photo.jpg.png](../_resources/6e4194cd901b0187b7a4082f600e35d5.png)](https://apis.google.com/u/0/wm/1/105625286543794908607)

### [Stéphane Bégaudeau](https://apis.google.com/u/0/wm/1/105625286543794908607)

[2 months ago](https://apis.google.com/u/0/wm/1/+St%C3%A9phaneB%C3%A9gaudeau/posts/5DCS5vRvxzv)  -  Shared publicly

[#Grumpy](https://apis.google.com/s/%23Grumpy): Go running Python!
+
1
2
1

 ·
Reply

[![photo.jpg.png](../_resources/67ed1967f72fcd2956f4b17d60d89c6d.png)](https://plus.google.com/101176242539238803593)

[Epo Jemba](https://plus.google.com/101176242539238803593)

[2 months ago](https://apis.google.com/u/0/wm/1/+St%C3%A9phaneB%C3%A9gaudeau/posts/5DCS5vRvxzv)

+
0
1
0

oui j'ai vu celui ci dans la newletter golang. C'est une bonne nouvelle pour les data scientist

 ·  Translate

[![photo.jpg](../_resources/7b77c5fa4f5c5d56570450de0cc93c22.jpg)](https://apis.google.com/u/0/wm/1/104401121686781166984)

### [Wayne Radinsky](https://apis.google.com/u/0/wm/1/104401121686781166984) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+WayneRadinsky/posts/P9PLok8vEFH)  -  Shared publicly

A Python-to-Go transpiler has been developed by Google, and it's called Grumpy, possibly because Gopy isn't a word.

+
2
5
6
5

 ·
Reply
View all 21 replies

[![photo.jpg](../_resources/edb78e207dc8b3a2c1a14837f4ebf11f.jpg)](https://plus.google.com/+RahulBhaleraoX)

[Rahul Bhalerao](https://plus.google.com/+RahulBhaleraoX)

[2 months ago](https://apis.google.com/u/0/wm/1/+WayneRadinsky/posts/P9PLok8vEFH)

+
4
5
4

Gopy is actually a word in Hindi meaning girls from community based on cow usually associated with Krishna

[![uFp_tsTJboUY7kue5XAsGA=s28.png](../_resources/e276b3c7a964ae1f19c288fe0bbf70e0.png)](https://plus.google.com/107494142655872845970)

[Johnny Blaze](https://plus.google.com/107494142655872845970)

[1 month ago](https://apis.google.com/u/0/wm/1/+WayneRadinsky/posts/P9PLok8vEFH)

+
0
1
0

In need of a developers help please. I've gone through 5 phones in 3 weeks..

[![photo.jpg](../_resources/35804361e4ed7738955af115e0527d6d.jpg)](https://apis.google.com/u/0/wm/1/110688269947285629106)

### [Pedro Martinez-Julia](https://apis.google.com/u/0/wm/1/110688269947285629106) shared this

[2 months ago](https://apis.google.com/u/0/wm/1/+pedromartinezjulia/posts/TdJn4rAEEHY)  -  [Python (Other)](https://apis.google.com/u/0/wm/1/communities/103393744324769547228/stream/a87458f1-f557-40bd-9c16-08699bca02df)

[![photo.jpg](../_resources/f21c87831d0eb8edc0a8f63a9c655a1b.jpg)](https://apis.google.com/u/0/wm/1/111041329240690776808)[Christian Ledermann](https://apis.google.com/u/0/wm/1/111041329240690776808) originally shared [this](https://apis.google.com/u/0/wm/1/+ChristianLedermann/posts/LLDr26NFiXr)

+
1
2
3
2

 ·
Reply

[![photo.jpg](../_resources/5ee5a75ed480dde38812f353bbeec7fe.jpg)](https://plus.google.com/105629046150521140928)

[Stuart Walsh](https://plus.google.com/105629046150521140928)

[2 months ago](https://apis.google.com/u/0/wm/1/+pedromartinezjulia/posts/TdJn4rAEEHY)

+
1
2
1

Poor Python...I love Python you cruel man you .... :)

[![photo.jpg](../_resources/959f4729811bc43e37ac1a99c8a97f61.jpg)](https://apis.google.com/u/0/wm/1/109490193695947400246)

### [Jonathan Ⓥ](https://apis.google.com/u/0/wm/1/109490193695947400246)

[2 months ago](https://apis.google.com/u/0/wm/1/+JonathanLevinTKY/posts/eHrUvCFtmNo)  -  Shared publicly

Could I copy/paste my old python admin scripts into this?
+
0
1
0

[![photo.jpg](../_resources/6c188afb5c0169a676439dd92610b48e.jpg)](https://apis.google.com/u/0/wm/1/113305053140799805395)

### [William Caban](https://apis.google.com/u/0/wm/1/113305053140799805395) shared this via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+WilliamCaban/posts/6Zd2MmAgvjS)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](:/2a3dafcc21ca50e003e5e154f2c24f93)](https://apis.google.com/u/0/wm/1/111041329240690776808)

### [Christian Ledermann](https://apis.google.com/u/0/wm/1/111041329240690776808) shared this

[2 months ago](https://apis.google.com/u/0/wm/1/+ChristianLedermann/posts/LLDr26NFiXr)  -  [Scientific Python (Discussion)](https://apis.google.com/u/0/wm/1/communities/108773711053400791849/stream/054bf642-1c64-4a8a-9443-20b6d43e0e83)

+
1
8
9
8

[![photo.jpg](../_resources/3a176246f6da020251c1e78507b00a4f.jpg)](https://apis.google.com/u/0/wm/1/106548631604770110294)

### [Samuel Lampa](https://apis.google.com/u/0/wm/1/106548631604770110294)

[2 months ago](https://apis.google.com/u/0/wm/1/+SamuelLampa/posts/Mracwhs3SKv)  -  Shared publicly

This is cool and great news!
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/c978d84865641eb8bdb3297769b0a51c.jpg)](https://apis.google.com/u/0/wm/1/108934422033670472122)

### [Jeanderson Candido](https://apis.google.com/u/0/wm/1/108934422033670472122)

[2 months ago](https://apis.google.com/u/0/wm/1/+JeandersonBarros/posts/BauVT9gyUig)  -  Shared publicly

This sort of work is awesome in too many levels.
+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/17a06642e1f03d50c8501bf9410e33bf.jpg)](https://apis.google.com/u/0/wm/1/101600410893426272559)

### [ij liao](https://apis.google.com/u/0/wm/1/101600410893426272559) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+ijliao/posts/PjPjuEMCVTJ)  -  Shared publicly

圖超級可愛 (大誤)

[![photo.jpg](../_resources/d87cb63662178c562f6f600b030a19cc.jpg)](https://apis.google.com/u/0/wm/1/109539480056944416389)[Kivava Chang](https://apis.google.com/u/0/wm/1/109539480056944416389) originally shared [this](https://apis.google.com/u/0/wm/1/+KivavaChang/posts/W1BbGrUfhEG)

Google Open Source Blog: Grumpy: Go running Python!
+
4
5
4

 ·
Reply

[![photo.jpg](../_resources/862c90821405c034c19889ed01c7016e.jpg)](https://apis.google.com/u/0/wm/1/117298439357852062985)

### [Simon Waddington](https://apis.google.com/u/0/wm/1/117298439357852062985) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+SimonWaddington/posts/NJFBQX42CP8)  -  Shared publicly

Interesting - Google is working on their own Python runtime using the Go Language. I thought they had previously put a ton of effort into Python and decided they could not make Python any better.

+
1
5
6
5

 ·
Reply

[![photo.jpg.png](../_resources/410ca7999468502e7c58ab75479479ce.png)](https://apis.google.com/u/0/wm/1/101321692953625607315)

### [Hans “hansemann” Bickhofe](https://apis.google.com/u/0/wm/1/101321692953625607315) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+HansBickhofe1/posts/e7PcGy8Xt9V)  -  Shared publicly

[![photo.jpg](../_resources/d87cb63662178c562f6f600b030a19cc.jpg)](https://apis.google.com/u/0/wm/1/109539480056944416389)[Kivava Chang](https://apis.google.com/u/0/wm/1/109539480056944416389) originally shared [this](https://apis.google.com/u/0/wm/1/+KivavaChang/posts/W1BbGrUfhEG)

Google Open Source Blog: Grumpy: Go running Python!
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/62b6fdf4af56f5f4184420c817946fa8.jpg)](https://apis.google.com/u/0/wm/1/111964046271353300398)

### [Maik Zumstrull](https://apis.google.com/u/0/wm/1/111964046271353300398) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+MaikZumstrull/posts/4FEHRm1QKp6)  -  Shared publicly

So this is interesting.
+
8
9
8

 ·
Reply
View all 3 replies

[![photo.jpg.png](../_resources/e8bb930157b41802a3d50878891058b6.png)](https://plus.google.com/+PhilippKern)

[Philipp Kern](https://plus.google.com/+PhilippKern)

[2 months ago](https://apis.google.com/u/0/wm/1/+MaikZumstrull/posts/4FEHRm1QKp6)

+
0
1
0

Also Python 2 which you stopped using eons ago.

[![photo.jpg](../_resources/6bf3b7219e63455c490079d3bd2620ee.jpg)](https://plus.google.com/+DavidBremner)

[David Bremner](https://plus.google.com/+DavidBremner)

[2 months ago](https://apis.google.com/u/0/wm/1/+MaikZumstrull/posts/4FEHRm1QKp6)

+
0
1
0

+[Philipp Kern](https://apis.google.com/113183404404398001287) To be fair, pypy is also at 2 in the stable version, and is the only version of python I use seriously.

[![photo.jpg](../_resources/98a6bc95e14ddcc957af14de9e037e82.jpg)](https://apis.google.com/u/0/wm/1/111058509525230416006)

### [Jens Knutson](https://apis.google.com/u/0/wm/1/111058509525230416006) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+JensKnutson/posts/FMUN8dmyPBG)  -  Shared publicly

This looks very promising. I can't wait to see how it performs against something like PyPy once it's complete enough to run the same benchmark suites.

+
8
9
8

 ·
Reply

[![photo.jpg](../_resources/9d0667eaef24c6eda5462c3fe4a17eb4.jpg)](https://plus.google.com/106180029380769267770)

[Chunga Chan](https://plus.google.com/106180029380769267770)

[2 months ago (edited)](https://apis.google.com/u/0/wm/1/+JensKnutson/posts/FMUN8dmyPBG)

+
0
1
0

this tool can convert script to Go source file and which you can compile and run without runtime.

for running script on pypy needs runtime interpreter (about 200mb or more for each microservice) and a lot of memory.

[![photo.jpg](../_resources/06220ed49a9a1ddd0da13a70752183ff.jpg)](https://apis.google.com/u/0/wm/1/114233674199568482864)

### [Abraham Williams](https://apis.google.com/u/0/wm/1/114233674199568482864)

[2 months ago](https://apis.google.com/u/0/wm/1/+AbrahamWilliams/posts/SMeYaBjxcQm)  -  Shared publicly

Grumpy: Go running Python!
+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/98911e4adef9613313681da614b7ceca.jpg)](https://apis.google.com/u/0/wm/1/100254863773082540099)

### [Massimo Luciani](https://apis.google.com/u/0/wm/1/100254863773082540099) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/100254863773082540099/posts/GC2CMyS7GTc)  -  Shared publicly

Grumpy is an experimental Python runtime for Go. It translates Python code into Go programs, and those transpiled programs run seamlessly within the Go runtime.

+
2
3
2

 ·
Reply

Show more

Labels:[Go](https://opensource.googleblog.com/search/label/Go) , [open source release](https://opensource.googleblog.com/search/label/open%20source%20release) , [Python](https://opensource.googleblog.com/search/label/Python) , [releases](https://opensource.googleblog.com/search/label/releases)