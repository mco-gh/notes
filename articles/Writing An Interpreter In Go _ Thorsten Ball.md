Writing An Interpreter In Go | Thorsten Ball

#### NEW: Buy the **eBook bundle** and get two books!

[![](../_resources/ccfbab8d9627410da145961bec67f20a.png)](https://compilerbook.com/)

This book now has a sequel in which we take the next step in Monkey's evolution. You can buy both books together to get:

- **Writing An Interpreter In Go** and [Writing A Compiler In Go](https://compilerbook.com/) in one package for a **reduced bundle price**!

- Both books in **ePub (iBook), Mobi (Kindle), PDF and HTML**.

- The complete code presented in both books, including the Monkey interpreter from *Writing An Interpreter In Go* and the **Monkey bytecode compiler and virtual machine** from [Writing A Compiler In Go](https://compilerbook.com/).

 [Buy now for $50](https://gum.co/waiig_wacig_bundle?wanted=true)

#### Buy this book to learn:

- How to build an interpreter for a C-like programming language **from scratch**

- What a **lexer**, a **parser** and an **Abstract Syntax Tree (AST)** are and**how to build your own**

- What **closures** are and how and why they work

- What the **Pratt parsing technique** and a **recursive descent parser** is

- What others talk about when they talk about **built-in data structures**

- What **REPL** stands for and how to build one

##### Get a taste!

 [![](../_resources/5fb61d273a42bb00798123a7564b525e.png)](https://interpreterbook.com/sample.pdf)

 [(L)](https://interpreterbook.com/sample.pdf)

 [(L)](https://interpreterbook.com/toc.pdf)

#### Why this book?

This is the book I wanted to have a year ago. This is the book I couldn't find.**I wrote this book for you and me**.

So why should you buy it? What's different about it, compared to other interpreter or compiler literature?

- **Working code is the focus**. Code is not just found in the appendix. Code is the main focus of this book.

- **It's small!** It has around **200 pages** of which a great deal is readable, syntax-highlighted, working code.

- The code presented in the book is **easy to understand, easy to extend, easy to maintain.**

- **No 3rd party libraries!** You're not left wondering: "But how does tool X do that?" We won't use a tool X. We only use the Go standard library and write everything ourselves.

- **Tests!** The interpreter we build in the book is **fully tested!** Sometimes in TDD style, sometimes with the tests written after. You can easily run the tests to experiment with the interpreter and make changes.

>

>  "If you don’t know how compilers work, then you don’t know how computers work. If you’re not 100% sure whether you know how compilers work, then you don’t know how they work."

>

> — >   > [>  Steve Yegge, super famous programmer and blogger](http://steve-yegge.blogspot.de/2007/06/rich-programmer-food.html)>

>

>
>  "Start by writing an interpreter with me!"
>
> — >  Thorsten Ball, author of the book you're looking at
>

#### This book is for you if you…

- **learn by building** and **love to look under the hood**

- love programming and to **program for the sake of learning and joy**!

- are interested in **how your favorite, interpreted programming language works**

- **never took a compiler course in college**

- want to **get started** with interpreters or compilers…

- … but don't want to work through a **theory-heavy, 800 pages, 4 pounds compiler book** as a beginner

- kept screaming **"show me the code!"** when reading about interpreters and compilers

- always wanted to say: **"Holy shit, I built a programming language!"**

#### The Monkey Programming Language

 ![](../_resources/fdbd7b2d50777e140a7587530876828b.png)
The official Monkey logo

In this book we'll create an interpreter for the Monkey programming language. Monkey is a language especially designed for this book. **We will bring it to life by implementing its interpreter**.

Monkey looks like this:

	*// Bind values to names with let-statements*
	let version = 1;
	let name = "Monkey programming language";
	let myArray = [1, 2, 3, 4, 5];
	let coolBooleanLiteral = true;

	*// Use expressions to produce values*
	let awesomeValue = (10 / 2) * 5 + 30;
	let arrayWithValues = [1 + 1, 2 * 2, 3];

Monkey also supports function literals and we can use them to bind a function to a name:

	*// Define a `fibonacci` function*
	let fibonacci = fn(x) {
	  if (x == 0) {
	    0                *// Monkey supports implicit returning of values*
	  } else {
	    if (x == 1) {
	      return 1;      *// ... and explicit return statements*
	    } else {
	      fibonacci(x - 1) + fibonacci(x - 2); *// Recursion! Yay!*
	    }
	  }
	};

The data types we're going to support in this book are booleans, strings, hashes, integers and arrays. We can combine them!

	*// Here is an array containing two hashes, that use strings as keys and integers*
	*// and strings as values*
	let people = [{"name": "Anna", "age": 24}, {"name": "Bob", "age": 99}];

	*// Getting elements out of the data types is also supported.*
	*// Here is how we can access array elements by using index expressions:*
	fibonacci(myArray[4]);
	*// => 5*

	*// We can also access hash elements with index expressions:*
	let getName = fn(person) { person["name"]; };

	*// And here we access array elements and call a function with the element as*
	*// argument:*
	getName(people[0]); *// => "Anna"*
	getName(people[1]); *// => "Bob"*

That's not all though. Monkey has a few tricks up its sleeve. In Monkey functions are first-class citizens, they are treated like any other value. Thus we can use higher-order functions and pass functions around as values:

	*// Define the higher-order function `map`, that calls the given function `f`*
	*// on each element in `arr` and returns an array of the produced values.*
	let map = fn(arr, f) {
	  let iter = fn(arr, accumulated) {
	    if (len(arr) == 0) {
	      accumulated
	    } else {
	      iter(rest(arr), push(accumulated, f(first(arr))));
	    }
	  };

	  iter(arr, []);
	};

	*// Now let's take the `people` array and the `getName` function from above and*
	*// use them with `map`.*
	map(people, getName); *// => ["Anna", "Bob"]*

And, of course, Monkey also supports closures:

	*// newGreeter returns a new function, that greets a `name` with the given*
	*// `greeting`.*
	let newGreeter = fn(greeting) {
	  *// `puts` is a built-in function we add to the interpreter*
	  return fn(name) { puts(greeting + " " + name); }
	};

	*// `hello` is a greeter function that says "Hello"*
	let hello = newGreeter("Hello");

	*// Calling it outputs the greeting:*
	hello("dear, future Reader!"); *// => Hello dear, future Reader!*

**Yes! All of this works with the interpreter we build in the book!**

So, to summarize: Monkey has a C-like syntax, supports **variable bindings**,**prefix** and **infix** operators, has **first-class and higher-order functions**, can handle **closures** with ease and has **integers**,**booleans**, **arrays** and **hashes** built-in.

#### Readers are saying...

>

>  "Compilers was the most surprisingly useful university course I ever took. Learning to write a parser and runtime for a toy language helps take away a lot of "magic" in various parts of computer science. I recommend any engineer who isn't familiar with lexers, parsers, and evaluators to read Thorsten's book."

>   >   ![small](../_resources/3067a09748e679fc141b545925d1501e.jpg)>  Mitchell Hashimoto (> [> @mitchellh](https://twitter.com/mitchellh)> )

>  Founder of > [> HashiCorp](https://www.hashicorp.com/)>
>

>  "Amazing book! Besides satisfying my curiosity with clear writing and code examples, the book inspired me to apply those skills to a new http testing tool I’m working on."

>   >   ![small](../_resources/c1a847ac340dc3c1443845611c5f3d4e.jpg)>  Felix Geisendörfer (> [> @felixge](https://twitter.com/felixge)> )

>  Prolific Open Source Contributor, Creator of > [> GoDrone](http://godrone.readthedocs.io/en/latest/)> , Node.js Core Alumni

>

>  "Great book. I loved it because everything is built by hand, so you get to think about all the details, and it does so in a gradual way, which is didactic. The implementation itself is also nice and simple "

>   >   ![small](../_resources/b6631cd521c149fbada50278cc1f2360.jpg)>  Xavier Noria (> [> @fxn](https://twitter.com/fxn)> )

>  Everlasting student, Rails Core Team, Ruby Hero, Freelance, Live lover
>

>  "I really enjoyed the modern, practical approach of this book. Diving into the world of interpreters, by getting your hands dirty right from the beginning."

>   >   ![small](../_resources/8e0b0cf8af12f4ec3b121995c90ec4ba.jpg)>  Christian Bäuerlein (> [> @fabrik42](https://twitter.com/fabrik42)> )

>  Developer, Organizer & Curator of > [> MECHANICON](https://www.meetup.com/Mechanical-Keyboard-Meetup-Rhein-Main/)>

>

>  "This book demystifies and makes the topic of interpreters approachable and fun. Don't be surprised if you become a better Go programmer after working your way through it."

>   >   ![small](../_resources/ea28424f6deece321767f07e7a165a98.jpg)>  Johnny Boursiquot (> [> @jboursiquot](https://twitter.com/jboursiquot)> )

>  Go Programmer, > [> @BaltimoreGolang](https://twitter.com/BaltimoreGolang)>  Organizer, > [> @GolangBridge](https://twitter.com/GolangBridge)>  Core Member

>

>  "Great writing and explanations. The practical focus of the book kept me coding for a week straight. Definitely the best book to get into the magical world of compilers and interpreters."

>   >  Arthur Tabatchnic (> [> LinkedIn](https://www.linkedin.com/in/arthur-tabatchnic-ab694290)> )

>  Senior Cloud Solutions Developer
>

>  "We use parsers and interpreters on a daily basis, just think of JavaScript and JSON. This book not only helped me to better understand how they work but will come in handy the next time I have to implement a parser for an obscure data format."

>   >   ![small](../_resources/e730cb7a6a7c0e42ed7f8057a8810ef4.jpg)>  Robin Mehner (> [> @rmehner](https://twitter.com/rmehner)> )

>  Developer, Organizer of > [> BerlinJS](http://berlinjs.org/)> , > [> Reject.JS](http://rejectjs.org/)>  & > [> NodeCopter](http://www.nodecopter.com/)> .

>

>  "This book clearly, and elegantly explains the different pieces needed to make a language. From lexing and parsing to actually executing the code, this book does a great job explaining to the reader the purpose of each element and how they interact."

>   >  Lee Keitel (> [> lfkeitel](https://github.com/lfkeitel)> )
>  Systems Programmer & Network Technician
>

>  "I loved this book and it remains one of my favorite #golang books to this day."

>   >   ![small](../_resources/e041ea994e201acb3831a6d3439db6ca.jpg)>  Brian Downs (> [> @bdowns328](https://twitter.com/bdowns328)> )

>  Software Engineer & Organizer of > [> Golang Phoenix](https://twitter.com/golangphoenix)>

>

>  "I only wish this book was available ten years ago! At the time I was using Appel's Java book and trying wade through the dragon book too. It's so refreshing to have a TDD-based tutorial to learn the concepts in a language you might reasonably use to build an interpreter."

>   >   ![small](../_resources/9ee56a1a91d13357b6741ff0d75e7178.jpg)>  Robert Gravina (> [> @robertgravina](https://twitter.com/robertgravina)> )

>  Programmer
>

>  "This book is not only educational, but the code quality is incredible, which allows the reader to move seamlessly from chapter to chapter without the need to scratch their head over what the code means or how it works. It is cleanly separated, well optimized, highly readable, and very precise in its functionality. Because of this, it provides an excellent example for both novices and veterans of the Go programming language, and will serve readers beyond a purely intellectual understanding of programming language design and functionality; the code used in the book will also provide a solid foundation in Go programming that can be practically applied right away. This balance is tough to achieve, and made the book a joy to read."

>   >   ![small](../_resources/3593ddfcd6f6d5e4818a0149304463c3.jpg)>  Aaron Hnatiw (> [> @insp3ctre](https://twitter.com/insp3ctre)> )

>  Hacker, educator, software developer
>

>  "I was completely hooked by your book on writing an interpreter and read it in 3 days. It might be the best book on programming I've ever read, and I read a lot of them. I love how all of the concepts are explained simply through very readable code and I love how the product turned out so real and useful. I wish more books were written in this style and I look forward to diving into the sequel!"

>   >   ![small](../_resources/15693c1ce7abadbb4eaaff12e7316157.jpg)>  Ludvig Gislason (> [> @ludviggislason](https://twitter.com/ludviggislason)> )

>  Software Engineer
>

>  "Thorsten took a topic that is usually very dry and CS heavy and made it accessible and easy to understand. After reading this book I felt confident enough to write > [> Plush](https://github.com/gobuffalo/plush)> , the templating language I’ve always wanted in Go! If you have yet to read Thorsten's book, I can't recommend it enough. Please go and buy it!"

>   >   ![small](../_resources/db6ad0cc465e890d9199822ef66f4f8d.jpg)>  Mark Bates (> [> @markbates](https://twitter.com/markbates)> )

>  Creator of > [> gobuffalo.io](http://gobuffalo.io/)>
>

>  "Thorsten's writing style is fun and easy to understand with detailed explanations and even better code. Even if you've written an interpreter before, this book is a great refresher. I picked it up as > [> a project to learn Rust](https://www.influxdata.com/blog/rust-can-be-difficult-to-learn-and-frustrating-but-its-also-the-most-exciting-thing-in-software-development-in-a-long-time/)> , translating the example Go code into Rust as I read through. Lexers, parsers, and interpreters are such a fundamental part of CS, these skills are valuable to more than just programmers implementing programming languages. As a project for picking up a new language, this book is perfect because it only requires the standard library and has extensive test driven development, which means you get quick feedback as you go along. I highly recommend it for programmers wanting to learn more about lexers, parsers, and interpreters or Go programmers picking up a new language looking for a project to learn through."

>   >   ![small](../_resources/4a165608d401fce255aa0b9ecc71d380.jpg)>  Paul Dix (> [> @pauldix](https://twitter.com/pauldix)> )

>  CTO of > [> InfluxDB](https://www.influxdata.com/)>

#### Buy the **eBook** and you will get:

- The complete book in **ePub (iBook), Mobi (Kindle), PDF and HTML**.

- **The complete, working interpreter for the Monkey programming language!**

- **All the code presented in the book**, easily usable, organized by chapters, MIT licensed and including the complete test suite.

- **Free updates**: Once you buy the book you will get free updates for the lifetime of that edition of the book.

- **Money-Back-Guarantee**: I want you to enjoy this book. If you, for any reason, are not happy with it just send me an email. You'll keep what you bought and your money back.

 [Buy now for $29](https://gum.co/waiig?wanted=true)

#### Buy the **paperback** and you will get:

- The **physical** 260 pages paperback book

- **The complete, working interpreter for the Monkey programming language!**

- **All the code presented in the book**, easily usable, organized by chapters, MIT licensed and including the complete test suite.

- **Amazon Support**: the book is distributed through Amazon and you get to benefit by all the money-back-guarantees and shipping Amazon offers.

 [Buy now for $39](https://www.amazon.com/dp/300055808X)

#### NEW: Buy the **eBook bundle** and get two books!

[![](../_resources/ccfbab8d9627410da145961bec67f20a.png)](https://compilerbook.com/)

This book now has a sequel in which we take the next step in Monkey's evolution. You can buy both books together to get:

- **Writing An Interpreter In Go** and [Writing A Compiler In Go](https://compilerbook.com/) in one package for a **reduced bundle price**!

- Both books in **ePub (iBook), Mobi (Kindle), PDF and HTML**.

- The complete code presented in both books, including the Monkey interpreter from *Writing An Interpreter In Go* and the **Monkey bytecode compiler and virtual machine** from [Writing A Compiler In Go](https://compilerbook.com/).

 [Buy now for $50](https://gum.co/waiig_wacig_bundle?wanted=true)

#### FAQ

- **Do I need previous experience with interpreters or compilers?**

Absolutely not! On the contrary, this book was written for you!

- **Can I read the book even though I'm not a Go programmer?**

Yes! I wrote the book with the aim to keep the code as easy to understand as possible. If you are experienced in other programming languages you should be able to understand it. Take a look at the [free excerpt](https://interpreterbook.com/sample.pdf) - that's as advanced as the Go code gets.

- **Can I buy a bundle of the eBook and the paperback?**

I'm sorry to say it, but no, I cannot bundle eBooks with paperbacks. It's not that I don't want to (I do!) but I can't. The eBooks are sold and distributed through Gumroad, where I have a lot of influence on the process, but the paperback editions are being printed, sold and shipped by Amazon and I don't have many options there. I can't tell Amazon to bundle digital files with the paperback. Sorry!

- **I found a typo/mistake/error in the book. What now?**

Take a look at the [changelog](https://interpreterbook.com/changelog) to see whether I've already fixed it. If I haven't or you're not sure I have, please send me an email to**me @ thorstenball.com** — I really appreciate it!

- **Why isn't the book called "Writing An Interpreter In Golang"? Wouldn't that be better for SEO?**

Well, I always thought I could use the "Golang" somewhere on the landingpage, maybe in the FAQ or something.

- **The books are too expensive for me. Can you help me out?**

Sure, just send me a picture! I'm always fascinated by new places and love seeing where people live, so here's my proposal.

You go outside, take a picture of where you live and send it to me to**me @ thorstenball.com**. Tell me what you feel comfortable paying for the book(s) and we'll make that happen.

####  The Lost Chapter: A Macro System For Monkey

[![](../_resources/f890eba2643c06b52ad51a6f2b5c1188.png)](https://interpreterbook.com/lost)

More than half a year after publishing *Writing An Interpreter In Go* I decided to write another chapter. An additional chapter that's available to everyone:**free to read online or to download as an eBook.**

It's called *The Lost Chapter: A Macro System For Monkey* and can be thought of as the fifth chapter for *Writing An Interpreter In Go*. It builds directly upon the previous four and extends the Monkey interpreter as it stands at the end of the book.

In the chapter we add a fully-working Lisp-style macro system to Monkey, that's close to the way Elixir's macro system works. It looks like this:

	let unless = macro(condition, consequence, alternative) {
	  quote(if (!(unquote(condition))) {
	    unquote(consequence);
	  } else {
	    unquote(alternative);
	  });
	};

	unless(10 > 5, puts("not greater"), puts("greater"));
	*// outputs only: "greater"*

Building your own programming language is likely not something you do in your day job. But adding a fully working macro system? Well, that's not just unlikely, but **outright bizarre and, oh, so much fun!** Macros are code that that writes code. Can you imagine how much fun it is to write code that allows us to write code that writes code? Exactly!

 [Read*The Lost Chapter* for free](https://interpreterbook.com/lost)

#### About the author

![](../_resources/04ecdf208546ba167428a51a68c23c42.png)

Hi, my name is Thorsten Ball. I'm a programmer living in Germany. My whole professional life as a software developer I've been working with web technologies and have deployed Ruby, JavaScript, Go and even C code to production systems.

Maybe you've read one of my blog posts. Some of them are pretty popular. There's the one about [the Ruby Garbage Collector](http://thorstenball.com/blog/2014/03/12/watching-understanding-ruby-2.1-garbage-collector/). And the one about [the fork system call](http://thorstenball.com/blog/2014/06/13/where-did-fork-go/). If you haven't read one of them, then maybe the one about [forking processes in a multi-threaded environment](http://thorstenball.com/blog/2014/10/13/why-threads-cant-fork/).

I also give [talks about Unix software](https://www.youtube.com/watch?v=DGhlQomeqKc) and other topics. And I turned one talk into a [blog post](http://thorstenball.com/blog/2014/11/20/unicorn-unix-magic-tricks/) which got super popular and remains my favorite.

Writing an interpreter from scratch in Go has been one of the most enjoyable and fun things I ever did as a programmer. So I hope you enjoy this book as much as I enjoyed writing it.

If you want to know more about me, you can also visit [my blog and website](http://thorstenball.com/), check out my [GitHub profile](https://github.com/mrnugget) or even better: [follow @thorstenball on Twitter](https://twitter.com/thorstenball).

#### Any questions?

If you have any questions, send me an email. I promise, you'll make my day. I love getting email from you: **me @ thorstenball.com**