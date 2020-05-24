journal.stuffwithstuff.com

#   [Crafting "Crafting Interpreters"](http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/)

 [↩](http://journal.stuffwithstuff.com/2018/05/19/40-songs/)

#### [April 05, 2020](http://journal.stuffwithstuff.com/archive)  [book](http://journal.stuffwithstuff.com/category/book)  [language](http://journal.stuffwithstuff.com/category/language)  [personal](http://journal.stuffwithstuff.com/category/personal)

It took three years and 200,000 words more than I expected, but my second book, [Crafting Interpreters](http://craftinginterpreters.com/), is complete. I finished the third draft of the last chapter today, marking the last of around 1,400 days of continuous writing.

This book was *much* harder than my [first book](http://gameprogrammingpatterns.com/), along every axis. It’s larger, more technically complex, much more deeply intertwined, and it had the misfortune of aligning with a really difficult period in my life. Today feels less like coasting past the finish line at the Tour de France, arms raised in triumph, and more like dragging myself onto the beach, clutching sand in relief after a storm-thrashed ordeal at sea.

Before I get into all that, I have a minor confession to make. When I finished my first book, I wrote [a long post](http://journal.stuffwithstuff.com/2014/04/22/zero-to-95688-how-i-wrote-game-programming-patterns/) about how I cobbled together enough willpower to reach the end of the last page. Everything in there is true, but there is one fact I superstitiously omitted.

Halfway through writing Game Programming Patterns, I discovered a new passion: programming languages. It had been a long time since a topic ignited my brain to the same degree, and I was *on fire*. I spent basically every free hour (and many not-so-free hours – sorry, family) designing and hacking on programming languages. I read [every book I could get my hands on](https://twitter.com/munificentbob/status/901543375945388032), [went to conferences](http://journal.stuffwithstuff.com/2010/07/23/what-i-learned-at-the-emerging-languages-camp/), [blogged](http://journal.stuffwithstuff.com/category/language/), I even *dreamed* about programming languages. This infatuation was the main reason I stopped working on my first book for two years.

I have a personality quirk where when I’m excited about something I just *have*to teach it to other people. Hermione Granger, arm waving feverishly to get the teacher’s attention, is my spirit animal. It was inevitable that I would write something about interpreters. But I couldn’t just drop one half-finished book to start another. I have gigs of unfinished projects laying around, but – maybe because the completed chapteres were already online – I couldn’t bear to abandon Game Programming Patterns.

So I made a promise to myself. If I finished that book, then I would let myself write a second book on interpreters. In part because of that promise, I *did*manage to complete the chapters, and then [the print and eBook editions](http://journal.stuffwithstuff.com/2014/11/03/bringing-my-web-book-to-print-and-ebook/). What I thought was merely a hobby and personal goal turned out to be a[life-changing experience](http://journal.stuffwithstuff.com/2014/11/20/how-my-book-launch-went/). My little self-published vanity project has[hundreds of five-star reviews](https://www.amazon.com/dp/0990582906), and has been translated to Korean, Japanese, Chinese, German, and Polish. The book did so much better than I expected that I’m still not sure how to process it, beyond feeling immense gratitude to everyone who read it, bought a copy, or cheered me on.

## The Seed of a Book

Once I finished the print edition of “Game Programming Patterns”, I took some time off. But it didn’t take too long for that itch to write about interpreters to come back. I knew exactly what I was getting into with writing a book now, how hard the grind can be. At first, I just noodled around. I wasn’t committed to doing anything. It was more just a sort of recreational intellectual exercise. If I *were* to do a book, what would it look like? You know,*hypothetically speaking*.

The very first note I wrote to myself said:

	high-level goal: a *small* book that builds a complete, efficient
	interpreter. instead of a wide text about programming language*s*,
	it is a single path through the language space. aim for 60k words.

My first book was almost 90,000 words, and I didn’t want to hike a trail that long again. I also had a meta-goal to make programming languages more approachable, and I figured a short text would help. I had this vision of something you could literally hold in your hand or have open next to your laptop while you followed along.

To make a small book, I needed a small language and a small implementation. One of my other side projects was [a scripting language named Wren](http://wren.io/). Wren is written in C, with a simple single-pass bytecode compiler inspired by Lua. Building Wren taught me how much functionality you can pack into a few thousand lines of clean C code.

For this hypothetical book, I figured a bytecode VM in C like that would be a great fit. It would also give me the chance to cover a bunch of really fun topics like stack-based VMs, object representation, and garbage collection. But Wren wasn’t the right language. I like Wren (obviously), but it has some design quirks that I think make it a better language for *users* but maybe not for teaching. For the book, I wanted a dynamically-typed scripting language in the vein of languages like JavaScript, Python, and Lua.

I started tinkering on a new toy language, tentatively named “Vox”. The goal was to keep things as simple as possible without taking any shortcuts around the hard problems in implementing a language. I wanted a rich expression and statement syntax to cover parsing. First-class functions and closures because they are powerful and challenging to implement efficiently. Classes and methods because that paradigm is so prevalent but omitted by many compiler books.

At some point, I realized that dropping readers straight into C was too unfriendly of an introduction. It’s hard to teach high-level concepts like parsing and name resolution while also tracking pointers and managing memory. OK, so we’ll build *two* interpreters. First a simple one in a high-level language, focused on concepts. Then a second bytecode VM in C to focus on performance and low-level implementation techniques.

Somehow, I didn’t notice that maybe this “handbook” wasn’t going to be as pocket-sized as I hoped.

My first choice for the high-level implementation language was JavaScript. I implemented most of a Vox interpreter in JS, but never really liked it. I wanted to write the interpreter in an object-oriented style because there are techniques like the visitor pattern for doing language stuff in OOP that aren’t covered well elsewhere. Doing OOP in JS means deciding whether to use classes or a prototypal style. The former is cleaner but infuriates some segment of readers. The latter is verbose and confusing to those not already steeped in prototypes.

Also, I missed static types. People reading code in a book don’t get the luxury of seeing the code in a debugger where they can see what values are in various variables. Static type annotations in the code help.

So I switched to Java. I don’t love Java but it seemed like the least biased choice for a statically typed object-oriented language. I found you can tame a lot of its infamous verbosity by simply not programming in 1990s enterprise Java style. Maybe it’s not idiomatic to have public fields, but it’s a hell of a lot shorter.

In parallel, I started building the bytecode VM in C, porting over bits of Wren’s implementation and stripping out the Wren-specific stuff. I spent the spring and summer of 2016 circling between these three pieces – the design of Vox itself, the Java interpreter, and the C bytecode VM. This was a delightful, satisfying period of time. The three parts played off each other in challenging ways. Sometimes I would change the language to make one interpreter simpler, but find doing so made the other interpreter more complex. Other times I’d hit on some trick that made everything get smaller and cleaner.

## Getting Back on the Horse

I remember the exact moment I committed to writing the book. I was stuck on a tricky language design problem: constructor syntax. I knew I wanted classes, which meant some way to construct instances. Adding a `new` keyword felt too special-purpose for my minimal language. I like Smalltalk and Ruby’s approach of making `new` be a method on the class object itself, but that requires metaclasses and a lot of other machinery.

I was struggling to find a way to add instantiation without making the language much bigger. Then I remembered JavaScript’s thing where you can simply invoke a “class” as if it were a function to create new instances. That has all sorts of weird baggage in JavaScript because everything does in JS, but the concept and syntax were perfect. I already had first-class classes. And I already had closures which meant a function call syntax that could be applied to arbitrary expressions. So “constructors” just became what you got when you invoked a class.

I felt like Vox had gelled, like it *was* a language now. And my two implementations were coming along well too. I was surprised by how few hacks or ugly corners I ran into. The codebases kind of fell together and the more I tweaked them, the nicer they got. It felt more like I had discovered them than that I had created them. It would be a shame to *not* write the book and put them out there into the world. They wanted me to.

I committed to writing the book, and I restarted my rule of writing every single day.

I had a few thousand lines of pretty Java and C code, but how do I turn that into a book that can be read in linear order? Compact codebases tend to be highly intertwined with many cyclic dependencies. I didn’t want readers to have to slog through ten chapters before they could even run `main()`.

This was the real technical challenge of writing the book – how do I take two implementations of the same language, and break them into incremental pieces that I can build up a chapter at a time?

I made this problem harder for myself because of the meta-goal I had. One reason I didn’t get into languages until later in my career was because I was intimidated by the reputation compilers have as being only for hardcore computer science wizard types. I’m a college dropout, so I felt I wasn’t smart enough, or at least wasn’t educated enough to hack it. Eventually I discovered that those barriers existed only in my mind and that anyone *can* learn this.

My main overarching goal of the book is to pass on that feeling, to get readers to understand there’s no magic in there and nothing keeping them out. To nail that conceit, I wanted to include *every single line of code* used by the interpreters in the book. No parser generators, nothing left as an exercise for the reader. If you type in all of the code in the book, you get two complete, working interpreters. No tricks.

So not only did I need to break these two interpreters into chapters, I needed to do it without any cheating. I wanted a hard guarantee that at the end of each chapter, you had a program that you could type in, compile, run, and do something with. I knew I wouldn’t be able to verify this manually, so it was time to create some tools.

## A Bespoke Build System

I [wrote my first book in Markdown](https://github.com/munificent/game-programming-patterns/tree/master/book). I slapped together [a tiny Python script](https://github.com/munificent/game-programming-patterns/blob/master/script/format.py) that converts the Markdown to HTML and transcludes the code snippets which are stored in separate C++ files. When I started my second book, I took that script and started growing it. It evolved throughout writing the book, but in the end, here is how it works.

All of the code for the interpreters are stored in separate source files. I have a [Java project](https://github.com/munificent/craftinginterpreters/tree/master/java/com/craftinginterpreters) that contains the complete Java interpreter that you get by the end of that part of the book. Likewise, there’s a [C project](https://github.com/munificent/craftinginterpreters/tree/master/c) for the bytecode VM. I can edit and build those in an IDE, run tests, debug them, etc. They’re real programs.

Meanwhile, the text of the book is [authored in Markdown](https://github.com/munificent/craftinginterpreters/tree/master/book), one file per chapter, just like my first book. To include a snippet of code in the book, I put a tag in the Markdown like this:

	Which can be any of:

	^code is-alpha

	Once we've found an identifier, we scan the rest of it using:

Here, the `^code` line says “look up the snippet named ‘is-alpha’ and insert it here.” When the build script generates the HTML for this chapter, it goes off and hunts through the code for that snippet. Over in the code, special comments delimit snippets. The one included here looks like this:

	//> Scanning on Demand is-alpha
	static bool isAlpha(char c) {
	  return (c >= 'a' && c <= 'z') ||
	         (c >= 'A' && c <= 'Z') ||
	          c == '_';
	}
	//< Scanning on Demand is-alpha

The `//>` line begins the snippet and says what chapter the snippet appears in and the name of the snippet. The `//<` line ends the snippet. Pretty straightforward.

This let me build the book, but didn’t ensure that the thing I built actually worked. So I wrote a separate script that instead of building the *book*, builds*programs*. For each chapter, it collects *all* of the snippets that appear in that chapter and the previous ones and writes them out to separate source files. In other words, it produces a separate interpreter, one for each chapter, containing only the code that readers have seen so far.

I put together a Makefile to build those per-chapter versions of each interpreter to make sure they compiled. Of course, compiling successfully doesn’t mean they do anything *useful*. Writing a single correct interpreter is hard. Writing thirty of them – there are [thirty chapters](http://craftinginterpreters.com/contents.html) in the book – is much harder.

I had already harvested a little [test runner](https://github.com/munificent/craftinginterpreters/blob/master/util/test.py) from Wren and ported most of Wren’s tests over to be [Lox tests](https://github.com/munificent/craftinginterpreters/tree/master/test). (I changed the name of the language in the book since there was already a language out there named “Vox.”). I took that test runner and extended it to be able to run the tests on each chapter’s version of the interpreters. Of course, the tests don’t all pass – the interpreters aren’t complete! So I added metadata to track which tests I expected to pass by which point in the book. With this in place, I could automatically verify that the code I was showing readers did exactly what I expected.

### More Complex Snippets

The snippet markers look pretty straightforward, and in many cases they are. But reality tends to get messier and I didn’t allow myself to sweep any of that mess under nearby rugs. Some changes don’t just *add* code to the interpreter. I try to minimize it, but often you need to *replace* some existing code. A few lines of code may appear in chapter 5 and then later get superseded in chapter 9 by something more powerful.

Obviously, I can’t jam both of those snippets into the same source file and expect it to compile. Remember, the source files that I hand author are themselves valid Java and C programs that I can build and run. If a function contained several versions of its body mixed together, odds are slim that the compiler will like what it sees.

So, for any piece of code that later gets replaced – in other words code that is not part of the very final version of each interpreter – there is a different snippet syntax:

	static void concatenate() {
	/* Strings concatenate < Garbage Collection concatenate-peek
	  ObjString* b = AS_STRING(pop());
	  ObjString* a = AS_STRING(pop());
	*/
	//> Garbage Collection concatenate-peek
	  ObjString* b = AS_STRING(peek(0));
	  ObjString* a = AS_STRING(peek(1));
	//< Garbage Collection concatenate-peek

	  int length = a->length + b->length;
	  char* chars = ALLOCATE(char, length + 1);
	  memcpy(chars, a->chars, a->length);
	  memcpy(chars + a->length, b->chars, b->length);
	  chars[length] = '\0';
	}

This block comment contains a snippet of code. The header indicates that this snippet is named “concatenate” and first appears in the “Strings” chapter. Then, later, it gets removed when the “concatenate-peek” snippet in the “Garbage Collection” chapter appears. In other words, that latter snippet replaces the previous two lines.

By storing the code for this snippet inside a block comment, I ensure that the code as it is in the raw source file is still valid. In some places where the interpreter gets revised multiple times, the code can get pretty complex. Here is the `main()` function of the bytecode VM:

	int main(int argc, const char* argv[]) {
	//> A Virtual Machine main-init-vm
	  initVM();

	//< A Virtual Machine main-init-vm
	/* Chunks of Bytecode main-chunk < Scanning on Demand args
	  Chunk chunk;
	  initChunk(&chunk);
	*/
	/* Chunks of Bytecode main-constant < Scanning on Demand args

	  int constant = addConstant(&chunk, 1.2);
	*/
	/* Chunks of Bytecode main-constant < Chunks of Bytecode main-chunk-line
	  writeChunk(&chunk, OP_CONSTANT);
	  writeChunk(&chunk, constant);

	*/
	/* Chunks of Bytecode main-chunk-line < Scanning on Demand args
	  writeChunk(&chunk, OP_CONSTANT, 123);
	  writeChunk(&chunk, constant, 123);
	*/
	/* A Virtual Machine main-chunk < Scanning on Demand args

	  constant = addConstant(&chunk, 3.4);
	  writeChunk(&chunk, OP_CONSTANT, 123);
	  writeChunk(&chunk, constant, 123);

	  writeChunk(&chunk, OP_ADD, 123);

	  constant = addConstant(&chunk, 5.6);
	  writeChunk(&chunk, OP_CONSTANT, 123);
	  writeChunk(&chunk, constant, 123);

	  writeChunk(&chunk, OP_DIVIDE, 123);
	*/
	/* A Virtual Machine main-negate < Scanning on Demand args
	  writeChunk(&chunk, OP_NEGATE, 123);
	*/
	/* Chunks of Bytecode main-chunk < Chunks of Bytecode main-chunk-line
	  writeChunk(&chunk, OP_RETURN);
	*/
	/* Chunks of Bytecode main-chunk-line < Scanning on Demand args

	  writeChunk(&chunk, OP_RETURN, 123);
	*/
	/* Chunks of Bytecode main-disassemble-chunk < Scanning on Demand args

	  disassembleChunk(&chunk, "test chunk");
	*/
	/* A Virtual Machine main-interpret < Scanning on Demand args
	  interpret(&chunk);
	*/
	//> Scanning on Demand args
	  if (argc == 1) {
	    repl();
	  } else if (argc == 2) {
	    runFile(argv[1]);
	  } else {
	    fprintf(stderr, "Usage: clox [path]\n");
	    exit(64);
	  }

	  freeVM();
	//< Scanning on Demand args
	/* A Virtual Machine main-free-vm < Scanning on Demand args
	  freeVM();
	*/
	/* Chunks of Bytecode main-chunk < Scanning on Demand args
	  freeChunk(&chunk);
	*/
	  return 0;
	}

Maintaining this is not super fun. But, thankfully, I have a build and test system to tell me when I break something.

## Slicing Up the Interpreters

So I had a tool that could let me split the interpreters across the chapters. If it was possible to break these interpreters into chapters at all, it would let me do so. Now I just had to figure out where to carve the seams. This was the most technically challenging part of the book writing process. I wasn’t sure if it was going to work at all.

I spent several weeks sketching out potential lists of chapters, sprinkling snippet markers throughout the code, and seeing if the result built. I’d get a compile error because a snippet in an early chapter tried to call a function in some later chapter and I would have to go back and reorganize things. I hand-drew dependency graphs between language features and tried to untangle them.

Here’s an example of what this was like:
1. To teach functions I want show that recursion works.

2. But to have recursive functions I need control flow. Otherwise, every recursive function recurses infinitely without a base case. So control flow has to come before functions.

3. For control flow, I need side effects so that I can show that a certain code path is *not* taken. The obvious way to do side effects is to have a`print()` function that displays output.

4. But I don’t have functions yet. That’s a cycle. Crap.

Sometimes I had to change the language itself to break cycles. The above example is why Lox has a built in print *statement* instead of a print *function*. Because that way we can introduce the print statement before control flow, which is in turn before functions.

I had to break a couple of cycles like that but, eventually, to my surprise, I got it all sorted out. I had a complete list of chapters for both interpreters. Every line of code was sorted into a snippet that belonged to one of those chapters. I could build and run each chapter’s code. Best of all, each chapter had a reasonably coherent concept and a roughly similar amount of code.

Before, I felt like I had a language and code that wanted to get out there into the world. Now I felt like I had a book.

Or, at least, I had all of the *code* for a book.

## A Chapter at a Time

I wrote my first book one chapter at a time. I drafted, edited, illustrated each chapter and put it online before moving to the next one. Serial publishing for the digital age. I really loved that process. It helped build an audience for the book and gave me incremental feedback which made the book better and kept me going. I don’t think I could write a whole book in the dark.

I intended to publish this book the same way, but the deeply interconnected nature of the chapters made that much harder. I didn’t want to discover a problem with the code in chapter 28 that forced me to tweak things in an earlier chapter that readers had already read. I didn’t want to paint myself into a corner or invalidate any previously-published material.

The entire time I was designing the language, coding the interpreters, and splitting the codebases into chapters, I had not done any actual writing. Just lots of hacking on code through the summer of 2016. It was, honestly, a blast. The programming part is definitely the fun part, and it was a joy to tinker on the code and figure out how to break it into chapters. Sort of like making a jigsaw puzzle and solving it at the same time.

After a few months, it was all there. Every single line of code for the entire book. A complete list of chapters. And I hadn’t written a single word of prose. In theory, “all” that remained was writing some text to explain the code I had already written along with some pictures. But, for me at least, English is a much more taxing language to write than C or Java. I had all of the difficult work ahead of me, and all of the fun was done.

## Illustrating by Hand

Well, not all of the fun. I did still have the illustrations to do. With my last book, I hand-drew little sketchy diagrams to show various bits of architecture. I wanted even more illustrations for this book to make the concepts less abstract, less opaque. Unlike a videogame, you can’t *see* a garbage collector doing its thing. Visual metaphors really help.

I liked the hand-drawn look. It furthered my meta-goal of making the material more approachable, more human. But I wanted to up the quality. I wanted them to be more intricate and contain more information. I wanted the drawings to be more detailed. Less like margin doodles and more like, well, *illustrations*. Maybe even some lowercase letters.

The ultimate goal for me is a print book, so I stuck with black and white ink. I wanted a tighter, more “spidery” style, so I got some technical pens. People often ask me what programs I used for the illustrations, assuming I did them all digitally. Here are the main tools I used:

 ![](../_resources/2cc32f5ce94f07d9dc74421a428bb919.png)

I went with Pigma Microns in 01 and 005. If I were doing it again, I think I’d do Faber-Castell Pitt pens.

There are two kinds of illustrations in the books: diagram-like ones that show meaningful information, and drawings that are for metaphors or just to be silly jokes. The process is different for each.

I draw each diagram in pencil on graph paper. That lets me erase and move things around until I get it where I like:

 ![](../_resources/49b3ab8a4888726aee9aa6e5e49fb912.png)

All of the vertical and horizontal lines in the illustrations generally fall on the graph paper rules or halfway between them.

Then I tape a piece of tracing paper on top and draw over it in ink:
 ![](../_resources/fde41dbd5d648b296040b56aeb25cd05.png)

I make mistakes sometimes, usually when lettering like “upvaluels” here. I fix that in Photoshop after scanning.

I hand letter everything. It takes a *long* time. I used to do graphic design, and I have this weird tic where any time I see something that looks handwritten, I look for multiple instances of the same letter to see if they are different or if the design just used a handwriting font. It’s almost always a handwriting font and I die a little inside to see the illusion evaporate.

Well, this is *my* damned book and no reader will ever feel that disappointment. Every single fucking letter in every one of the illustrations was hand lettered and is unique.

 ![](../_resources/c4712c92e810b051d066d4520ca864a6.png)
Here is the hand-lettered logotype for the book. Each “R” is different!

Also, if that’s not obsessive enough, I spent time *changing my own handwriting*to better match the text font of the book. I taught myself to write double-story “a” and “g” letters and practiced by filling pages of paper with the same letter over and over.

 ![](../_resources/0074c4361fa5d1b89d57689f6a18de29.png)

Look at the loop under the “g” in “filling” and the finial on the “a” in “apples”.

I also wanted to make sure that the illustrations and text matched each other across the book. To give the text a consistent size, I printed a little height guide:

 ![](../_resources/4384830c6fad8b77364b9a8c1f7b63ef.png)

The dotted line indicates the x-height. I picked a ratio for that to match the fonts I use for text and code.

I slid this paper under the tracing paper and lettered on top of those lines to keep the metrics the same across the book.

To keep the diagram size and line thickness consistent, each illustration has a pair of registration marks a fixed distance apart:

 ![](../_resources/443e8fdbcb696f1de224a261b1b83788.png)
The little marks that the pencils are pointing at.

I scan each illustration into Photoshop for clean up and processing. I use those marks when cropping to ensure that the image maintains the right size relative to other images.

I recorded a video of the whole process if you want to see it in action:

Even in timelapse, it takes a long time.

Writing this all out makes me sound like a crazy person. What the hell am I doing with my life? Or, more importantly, what *could I have been doing* instead of doing all that?

Too late now, I guess. The picture-like drawings have a different workflow since they don’t have a lot of straight lines or align to a grid.

 ![](../_resources/73cd2907dbc228473673ebf2e6f0b46c.png)
How will readers understand what a stack is without this helpful illustration?

I draw those on regular sketch paper using a non-photo blue pencil. Then I ink on top of that. I scan the paper in RGB and use the blue channel, which mostly makes the blue pencil marks disappear.

 ![](../_resources/6a6626b9e89d828d1bd6ff5c9c4db1af.png)

The sketch paper bleeds the ink more than I like but I didn’t want to change paper partway through the book, so I stuck with it.

It’s a lot of work for each image, and this doesn’t include all of the work after scanning it. And I wanted a lot of them. By the end, I had this stack of paper:

 ![](../_resources/8457c6e98425b473499d20d7131fe280.png)
Such a small image for so much work.

I went through two full pads of tracing paper, two pads of graph paper, a sketch pad, and several pens. I drew 181 illustrations.

## Writing is Suffering

I had the code, and I had a process for illustrations. The remaining work was just writing all the words and drawing all the pictures. So that’s what I did. I started at chapter one and started writing. For each chapter, I wrote an outline and then a first draft. I did an editing pass over that to fix all the major problems. Then a second pass where I read the whole chapter out loud to fix cadence and other stuff.

This is the same process I used for the first book. I stumbled onto something that worked, so I wasn’t about to mess it up. I posted each chapter online, and then spent a day fixing bugs that readers noticed. Then I moved on to the next chapter.

I wrote. And wrote. And wrote. Every single day. Every now and then I would have a trip or something where I couldn’t write. As with my first book, I would bank days by writing multiple sessions per day beforehand and then spend those banked days on days that I didn’t write. But for the most part, I wrote every day.

In the blog post I wrote after my first book, I whined about how I had to write on days when I traveled for work, on holidays, when the kids had sniffles. At the time, it truly was one of the hardest things I’ve ever done.

This time was something else entirely. I wrote the day my grandfather died (peacefully, unsurprisingly) and the day my aunt died (tragically, days after retiring). I wrote the day I found out my Mom had cancer and my children saw me cry for the first time. I was flying to Louisiana to keep my Mom company when I turned on my phone during the layover and discovered a dear friend had had a stroke. I wrote that evening. I woke up the next day and found out she had died. I wrote that morning sitting next to my brother in the waiting room of the hospital while my Mom got her PET scan.

The morning of my friend’s memorial service, I wrote in the hotel. Later that day, I openly sobbed in front of a room full of people. The next day, my wife found out her aunt had terminal cancer. I wrote on the flight home.

See that dog up there in my profile photo? That’s Ginny. She’s on the back cover of my first book. Her myriad health problems finally [caught up with her](https://twitter.com/munificentbob/status/1100898048811491328)last spring. People sometimes ask, “When did you know you were an adult?” For me it was the day I made the call to put my dog down. The hardest part was watching my kids say goodbye to her. I’m tearing up now writing about it. I ran my fingers through Ginny’s silky fur as the sedatives took her away. I only got through 59 words that afternoon.

I wrote the day the US somehow elected a racist, abusive, corrupt demagogue, and every day afterwards as I saw my country and others turn towards hate and authoritarianism. I wrote while climate change and income inequality worsened. And now here I am writing at home on the same desk where I work now, quarantined like most of you all, hoping to survive the worst pandemic the world has seen in a century.

This is not about how disciplined I was. Because during what have been some of the worst years of my life, a weird inversion happened. It’s not that I was going through that shit and still writing *in addition to* it. I *had* to keep writing. Writing was one thing I could still control in the face of many things I could not. If I could make it through the book, maybe I could make it through the other things too. If I had skipped a day it would have meant that the cancer or the deaths beat me that day, that they were stronger than me. I feared what it would mean to me to let go.

I got through these four years and kept writing, but I paid a price. When I read the earlier chapters, they have a whimsy and light-heartedness that later chapters lack. We’re all going through dark times, and I don’t *feel* light. The past few years left a mark on me, and that mark shows up in the book. I miss the goofier person I used to be, sometimes. But I’d like to believe that maybe the person I am now is a little more honest. Maybe some of those jokes were a mask.

And, thankfully, Mom is in remission.

Psychological self examination aside, I did keep up the writing. Which is good because, *man* did I underestimate this book. I was aiming for 60,000 words and hoped to get it done in about a year. Here I am four years later sitting on a quarter of a million words.

People sometimes ask what it’s like writing something that big. I’ve been asking myself that for the past couple of weeks. And the weird thing is, *I don’t know.* I’ve had my head down for the past four years and haven’t looked past the next paragraph or two the entire time. What does it feel like to write an email or draw a picture? Writing the book felt like that. I just happened to do it over and over again. I feel like a marathon runner who’s been watching his feet the whole time and didn’t even notice when he stumbled over the finish line.

## And Now What?

“Crafting Interpreters” is complete now. I had to stop here for a minute and look at that sentence. I’ve been working on this book every day for around 1,400 days. I can’t *wait* to take a break. So that’s the next step. My plan was to finish the book right before spring break and enjoy a week on the beach with family.

That beach trip went the way of so many other plans in early 2020, but I still intend to take a long break. I don’t know if you noticed, but we all have a lot of other shit to deal with right now. I’m going to relax.

Every morning since 2016, I’ve woken up with a task I had to do. Until I got my writing done for the day, it was on my mind, weighing me down. Writing left me drained. If you’ve ever had a newborn, you know the feeling of always having to carry the baby around. After a while, it’s like you forget what it’s like to have *two* free arms. I’ve been carrying this baby for four years, so I’m looking forward to having both arms for a while.

Once I’m recharged, the real fun starts. Having the book online is important, but for me, “Crafting Interpreters” was always meant to be a *book* with pages and a cover. So after a long bout of editing and bug fixing, I’m going to get started doing the page layout for the print edition. I love graphic design, and I can’t wait to hold it in my hands.

If you’d like to hold it in *your* hands when it comes out, I have [a mailing list](https://mailchi.mp/afd054e73140/robertnystrom) where I’ll let you know when the book is done. In the meantime, I think I’ve earned some rest.

 [**](http://www.reddit.com/submit?url=http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters//)  [**](http://news.ycombinator.com/submitlink?u=http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters//&t=Crafting%20%22Crafting%20Interpreters%22)  [**](http://twitter.com/share?url=http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/&text=%22Crafting%20%22Crafting%20Interpreters%22%22%20%40munificentbob)  [**](http://www.facebook.com/share.php?u=http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/)  [**](https://plus.google.com/share?url=http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/)  [**](http://journal.stuffwithstuff.com/rss.xml)

- [29 comments]()
- [**journal**](https://disqus.com/home/forums/journal-stuffwithstuff/)
- [** Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend  18](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

[(L)](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/26b3ddf03f6503698c74a91d62490f38.jpg)](https://disqus.com/by/disqus_E2KC8HADOh/)

 [Mohammed Hamed](https://disqus.com/by/disqus_E2KC8HADOh/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862508081)  •  edited

Congratulations!!!

I really appreciate your perseverance. Very well written content, unveiling the concepts behind the black magic.

I enjoyed your style of writing and illustrations.
Can't wait to get my hands on the print book.
Enjoy your break and stay safe!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/0ed5ae73c09c4cfd62f5b1e70275c9a2.jpg)](https://disqus.com/by/Wikzo/)

 [Wikzo](https://disqus.com/by/Wikzo/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863123544)

Just wanted to say big congrats with finishing the book. I read Game Programming Patterns some years ago and really enjoyed it. In fact, it's one of the only programming books I really recommend to other people.

The new book is not really for me, but nevertheless it has been fascinating following your progress.

Wishing you all the best!
A game developer from Denmark.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)
Wes  •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862731229)

Thank you for not only writing this excellent book, but also sharing some insight into how you made it and how it's affected you as an author.

Having gone through my own somewhat obsessive 20+ love-of-compilers journey, and can honestly say that Crafting Interpreters is one of the best resources out there -- not (just) for technical content, but for helping provide motivation and encouragement through good humor and a friendly style.

Thanks again for writing the books that you do, and for providing them free online. That's such a great service you've done for the whole computer science community. I can't wait to get a paper copy whenever they are available.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/9fe591276bc20bbffde8e0082b675852.jpg)](https://disqus.com/by/arthurcousseau/)

 [Arthur Cousseau](https://disqus.com/by/arthurcousseau/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863966923)  •  edited

You're a legend!
Loved Game Programming Patterns.

I've just read the first two chapters of Crafting Interpreters and I love it already.

Can't wait to hold it in my hands too!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/8c6b0aa9c40c235d766a976155f27449.jpg)](https://disqus.com/by/mkgiles/)

 [mkgiles](https://disqus.com/by/mkgiles/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863450837)

I just want to say that this post is an inspiration.

The past few years have really been difficult for all of us and you had a lot more personal difficulty on top of all of that. To read that you wrote every day through it all changed my perspective on how someone can deal with a time of crisis and turmoil.

Reading Crafting Interpreters has been a source of joy for me as a CS student the past few months I've been reading it. Between the excitement of learning new techniques and concepts and the humanised, natural approach it was written, I flew through each chapter and waited impatiently for the next. You have definitely accomplished your goal of passing your excitement for the field onto at least one person, though I'm sure I'm not the only one.

While I'll miss getting regular notifications in my inbox on new chapters, I look forward to having a physical book in my hands with all the wisdom and whimsy you've poured into this project over the course of the past three years.

Thank you for all your hard work, enjoy your break and I look forward to seeing more from you when you've recharged.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/4a861049238780e2a8b7b9641367ac53.jpg)](https://disqus.com/by/ideaholic/)

 [ideaholic](https://disqus.com/by/ideaholic/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4862962287)

Great day in life :) Thanks for the book and especially for this post - really interesting to know all that details about your insights and the process of writing book on such complex topic.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/ff163cddc74d3592cd4affc4d4d74560.jpg)](https://disqus.com/by/disqus_zBqKtIoOBy/)

 [Gianluca Ciccarelli](https://disqus.com/by/disqus_zBqKtIoOBy/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862914478)  •  edited

Bob,

I've been thanking you for writing this monumental book already a few times during those past four years. So many things have happened, and your e-mails kept arriving in my mailbox saying "A new chapter of Crafting Interpreters is ready!" (I'm quoting from feeble memory, I realize the titles might be slightly different) -- and every time I felt magic was still flowing strong in the world.

I want to thank you once more for the profound inspiration you've been and still are to me and others who benefit from your munificence.

(And this post is a treasure. Hand-drawn illustrations? WOW.)
Can't wait to have that printed copy in my hands!
-- Gian

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![avatar92.jpg](../_resources/1fac2f862d3cb26c67b9f4192953b79c.jpg)](https://disqus.com/by/shauryab98/)

 [shaurya](https://disqus.com/by/shauryab98/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862896136)

Thank you for your herculean efforts. Stay strong.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/lj_miranda/)

 [Lj Miranda](https://disqus.com/by/lj_miranda/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862833254)

Congratulations! I'm still in Chapter 6 but I can't wait to finish it this year (or the next). Thanks for inspiring me three years ago, I was still a student back then. Now I'm working!

Looking forward to the print version of the book :) Stay safe!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/JustCodin/)

 [JustCodin](https://disqus.com/by/JustCodin/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862827492)

Wow. Huge congratulations. And I'm sorry to hear of all the pain you endured while writing the book; that's an immense drive and level of perseverance. Very well written blog post. I skimmed parts of your book online and it looks great. I'm looking forward to reading more of your writing.

I can relate with working on a large projects by yourself as I've been working on [Kontxt](https://disq.us/url?url=https%3A%2F%2Fkontxt.io%3AMWfgJM5G0t9UXq3NUJVeYf-Q2XQ&cuid=968811) every day for 3 years which enhances websites (and documents) with real-time collaborative features like inline highlights, comments, polls, etc. Check it out. I think it could be useful on your blogs and the online versions of your books.

P.S. I have family members who share your last name. Who knows, maybe we're related. Haha. Keep it up fam! :)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/xk0nsid/)

 [Siddharth Yadav](https://disqus.com/by/xk0nsid/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862825570)

I would really like to thank you for you effort for this book. I have been following it since day one and even to me it feels like a chapter by chapter journey. I have been so much excited about compilers & interpreters for so long and this book opens up the black box so well. I don't think I can thank you enough for this. I really appreciate all the hard work that you did to complete the book. A very sincere thank you.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/davidcortesi/)

 [Owns_Six_Fedoras](https://disqus.com/by/davidcortesi/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862641716)

> I had to keep writing. Writing was one thing I could still control in the face of many things I could not.

That's a great insight. It probably explains a lot of great art.

On a more trivial matter, the print statement? You might have had the cake and et it also, by calling the statement something else that reflected its use at that pedagogical point, like the annotate statement, or the document statement, and given it a restricted domain, like only string literals. Then print() with full functionality comes in due course. (Gee, thanks, man, where were you in 2017?)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/shavenwarthog/)

 [shavenwarthog](https://disqus.com/by/shavenwarthog/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862631716)

Thanks so much for writing this book! And yes, you sound like a crazy person :)

To be clear, I'm starting this journey myself, sketching out my first book. Question: in my experience startup companies, and developers, can't stand books, they rarely even understand what they are and their benefits. Who did you write this book for? Yourself? Devs in other industries?

I found "Threaded Interpretive Languages" book (on the implementation of Forth) completely fascinating, and will buy your book because it sounds great. Thanks!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/joker_vd/)

 [Joker_vD](https://disqus.com/by/joker_vd/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862434106)

Well, that's... overwhelming. I don't remember if it's a joke, or an actual story, but one runner described how running and winning the marathon felt like this: "At start, it was hard. Then, it became harder and harder". So, congratulations on finishing the book despite everything that life have thrown at you. I wish you to have nice and relaxing rest. Take care of yourself and your family.

And thank you for this 4-year journey through programming language concepts, various kinds of desserts and breakfasts, exquisite hand-crafted illustrations, and enthralling writing; it was truly inspiring.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_BQ78Cccce1/)

 [エラリー　ジャンクリストフ](https://disqus.com/by/disqus_BQ78Cccce1/)    •  [7 hours ago](http://journal.stuffwithstuff.com/#comment-4866004956)

Thank you for this beautiful post.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/upriser/)

 [upriser](https://disqus.com/by/upriser/)    •  [a day ago](http://journal.stuffwithstuff.com/#comment-4864705774)

Thanks Bob!
Your book is a masterpiece.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/warrenbare/)

 [Gronk](https://disqus.com/by/warrenbare/)    •  [a day ago](http://journal.stuffwithstuff.com/#comment-4864522293)

Haha. I literally just finished comparing letters (s is a good one) on your drawing to make sure you were telling the truth, when I saw the next paragraph said this:

>  I have this weird tic where any time I see something that looks handwritten, I look for multiple instances of the same letter to see if they are different or if the design just used a handwriting font.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/jeremy_cheung/)

 [Jeremy Cheung](https://disqus.com/by/jeremy_cheung/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4864229287)

Really thanks for your hard work, learned a lot, appreciated.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_IV4HkedpDk/)

 [Ian](https://disqus.com/by/disqus_IV4HkedpDk/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4864211271)

Big thumbs up, I am learning a lot from your work at home during this COVID-19. Stay safe! Hope to see a physical book!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

reod  •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863647206)

I'm jealous, man. Tremendous amount of high quality work.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/tyoungjr/)

 [tyoungjr](https://disqus.com/by/tyoungjr/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863404545)

Really inspiring, congratulations!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/dwaynesummerfield/)

 [Dwayne Summerfield](https://disqus.com/by/dwaynesummerfield/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863308443)

Seems like you successfully reverse engineered literate programming.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/greg_tomkins/)

 [Greg Tomkins](https://disqus.com/by/greg_tomkins/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863129298)

Amazing book. It is weird that you invested so much effort in hand-lettering but I guess the important thing is that it mattered to you.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_derXpH9k7C/)

 [Ron](https://disqus.com/by/disqus_derXpH9k7C/)    •  [2 days ago](http://journal.stuffwithstuff.com/#comment-4863080759)

Well done.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/muhammadazeez/)

 [Muhammad Azeez](https://disqus.com/by/muhammadazeez/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862829696)

Congratulations and thank you! Crafting Interpreters was what made me interested in programming languages. It's a very interesting part of computer science that doesn't get enough love.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/jonforrest/)

 [Jon Forrest](https://disqus.com/by/jonforrest/)    •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862673396)

Trivial typos:
1) " you can’t see a garbage collector
doing it’s thing. ->
"you can’t see a garbage collector
doing its thing."
2) "Less margin doodles" ->
"fewer margin doodles"

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/bob_nystrom/)

 [Bob Nystrom](https://disqus.com/by/bob_nystrom/)    [*>* Jon Forrest](http://journal.stuffwithstuff.com/#comment-4862673396)  •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862810230)

Fixed, thanks!

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/jeanjordaan/)

 [Jean Jordaan](https://disqus.com/by/jeanjordaan/)    [*>* Jon Forrest](http://journal.stuffwithstuff.com/#comment-4862673396)  •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862805653)  •  edited

3) "read the whole chapter out load" ->
"read the whole chapter out loud"

Awesome work, I really appreciated following along with the progress of the book.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/bob_nystrom/)

 [Bob Nystrom](https://disqus.com/by/bob_nystrom/)    [*>* Jean Jordaan](http://journal.stuffwithstuff.com/#comment-4862805653)  •  [3 days ago](http://journal.stuffwithstuff.com/#comment-4862810328)

Fixed! :)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=journal-stuffwithstuff&t_u=http%3A%2F%2Fjournal.stuffwithstuff.com%2F2020%2F04%2F05%2Fcrafting-crafting-interpreters%2F&t_d=journal.stuffwithstuff.com&t_t=journal.stuffwithstuff.com&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=journal-stuffwithstuff&utm_medium=Disqus-Footer)
- [*⚠*Do Not Sell My Data](https://disqus.com/data-sharing-settings/)