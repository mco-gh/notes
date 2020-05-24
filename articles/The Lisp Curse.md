The Lisp Curse

The power of Lisp is its own worst enemy.

Here's a thought experiment to prove it: Take two programming languages, neither of which are object-oriented. Your mission, if you choose to accept it, is to make them object-oriented, keeping them backward-compatible with the original languages, modulo some edge cases. Inserting any pair of programming languages into this thought experiment will show that this is easier with some languages than with others. That's the point of the thought experiment. Here's a trivial example: Intercal and Pascal.

Now make this thought experiment interesting: Imagine adding object orientation to the C and Scheme programming languages. Making Scheme object-oriented is a sophomore homework assignment. On the other hand, adding object orientation to C requires the programming chops of Bjarne Stroustrup.

The consequences of this divergence in needed talent and effort cause *The Lisp Curse*:

 **Lisp is so powerful that problems which are technical issues in other programming languages are social issues in Lisp.**

* * *

Consider the case of Scheme, again. Since making Scheme object-oriented is so easy, many Scheme hackers have done so. More to the point, many *individual* Scheme hackers have done so. In the 1990s, this led to a veritable warehouse inventory list of object-oriented packages for the language. [The Paradox of Choice](http://en.wikipedia.org/wiki/The_Paradox_of_Choice%3A_Why_More_Is_Less), alone, guaranteed that none of them would become standard. Now that some Scheme implementations have their own object orientation facilities, it's not so bad. Nevertheless, the fact that many of these packages were the work of lone individuals led to problems which Olin Shivers wrote about in documenting the Scheme Shell, scsh.

Programs written by individual hackers tend to follow the scratch-an-itch model. These programs will solve the problem that the hacker, himself, is having without necessarily handling related parts of the problem which would make the program more useful to others. Furthermore, the program is sure to work on that lone hacker's own setup, but may not be portable to other Scheme implementations or to the same Scheme implementation on other platforms. Documentation may be lacking. Being essentially a project done in the hacker's copious free time, the program is liable to suffer should real-life responsibilities intrude on the hacker. As Olin Shivers noted, this means that these one-man-band projects tend to solve eighty-percent of the problem.

Dr. Mark Tarver's essay, [The Bipolar Lisp Programmer](http://www.lambdassociates.org/blog/bipolar.htm), has an apt description of this phenomenon. He writes of these lone-wolf Lisp hackers and their

>

>  ...inability to finish things off properly. The phrase 'throw-away design' is absolutely made for the > BBM>  and it comes from the Lisp community. Lisp allows you to just chuck things off so easily, and it is easy to take this for granted. I saw this 10 years ago when looking for a GUI to my Lisp. No problem, there were 9 different offerings. The trouble was that none of the 9 were properly documented and none were bug free. Basically each person had implemented his own solution and it worked for him so that was fine. This is a > BBM>  attitude; it works for me and I understand it. It is also the product of not needing or wanting anybody else's help to do something.

>

* * *

Once again, consider the C programming language in that thought experiment. Due to the difficulty of making C object oriented, only two serious attempts at the problem have made any traction: C++ and Objective-C. Objective-C is most popular on the Macintosh, while C++ rules everywhere else. That means that, for a given platform, the question of which object-oriented extension of C to use has already been answered definitively. That means that the object-orientated facilities for those languages have been documented, that integrated development environments are aware of them, that code libraries are compatible with them, and so forth.

Dr. Mark Tarver's essay on bipolar Lispers makes the point:

>

>  Now in contrast, the C/C++ approach is quite different. It's so damn hard to do anything with tweezers and glue that anything significant you do will be a real achievement. You want to document it. Also you're liable to need help in any C project of significant size; so you're liable to be social and work with others. You need to, just to get somewhere.

>

>  And all that, from the point of view of an employer, is attractive. Ten people who communicate, document things properly and work together are preferable to one > BBM>  hacking Lisp who can only be replaced by another > BBM>  (if you can find one) in the not unlikely event that he will, at some time, go down without being rebootable.

>

Therefore, those who already know C don't ask "What object system should I learn?" Instead, they use C++ or Objective-C depending on what their colleagues are using, then move on to "How do I use object-oriented feature *X*?" Answer: "Goog it and ye shall find."

* * *

Real Hackers, of course, have long known that object-oriented programming is not the panacea that its partisans have claimed. Real Hackers have moved on to more advanced concepts such as immutable data structures, type inferencing, lazy evaluation, monads, arrows, pattern matching, constraint-based programming, and so forth. Real Hackers have also known, for a while, that C and C++ are not appropriate for most programs that don't need to do arbitrary bit-fiddling. Nevertheless, the Lisp Curse still holds.

Some smug Lisp-lovers have surveyed the current crop of academic languages (Haskell, Ocaml, et cetera) and found them wanting, saying that any feature of theirs is either already present in Lisp or can be easily implemented — [and improved upon](http://www.reddit.com/r/programming/comments/ujj3/a_critique_of_abelson_and_sussman_or_why/cutzn) — with Lisp macros. They're probably right.

Pity the Lisp hackers.

* * *

Dr. Mark Tarver — twice-quoted, above — wrote a dialect of Lisp called [Qi](http://www.lambdassociates.org/). It is less than ten thousand lines of macros running atop Clisp. It implements most of the unique features of Haskell and OCaml. In some respects, Qi surpasses them. For instance, Qi's type inferencing engine is *Turing complete*. [In a world](http://www.wimp.com/theman/) where teams of talented academics were needed to write Haskell, one man, Dr. Tarver wrote Qi all by his lonesome.

Read that paragraph, again, and extrapolate.

* * *

 *Exercise for the reader*: Imagine that a strong rivalry develops between Haskell and Common Lisp. What happens next?

 *Answer*: The Lisp Curse kicks in. Every second or third serious Lisp hacker will roll his own implementation of lazy evaluation, functional purity, arrows, pattern matching, type inferencing, and the rest. Most of these projects will be lone-wolf operations. Thus, they will have eighty percent of the features that most people need (a different eighty percent in each case). They will be poorly documented. They will not be portable across Lisp systems. Some will show great promise before being abandoned while the project maintainer goes off to pay his bills. Several will beat Haskell along this or that dimension (again, a different one in each case), but their acceptance will be hampered by flame wars on the comp.lang.lisp Usenet group.

 *Endgame*: A random old-time Lisp hacker's collection of macros will add up to an undocumented, unportable, bug-ridden implementation of 80% of Haskell *because* Lisp is more powerful than Haskell.

* * *

The moral of this story is that **secondary and tertiary effects matter**. Technology not only affects what we can do with respect to technological issues, it also affects our social behavior. This social behavior can loop back and affect the original technological issues under consideration.

Lisp is a painfully eloquent exemplar of this lesson. Lisp is so powerful, that it encourages individual independence to the point of bloody-mindedness. This independence has produced stunningly good innovation as in the Lisp Machine days. This same independence also hampers efforts to revive the "Lisp all the way down" systems of old; no "Lisp OS" project has gathered critical mass since the demise of Symbolics and LMI.

One result of these secondary and tertiary effects is that, even if Lisp is the most expressive language ever, such that it is theoretically impossible to make a more expressive language, *Lispers will still have things to learn from other programming languages*. The Smalltalk guys taught everyone — including Lisp hackers — a thing or two about object oriented programming. The [Clean](http://www.discenda.org/Clean/) programming language and the [Mozart/Oz](http://www.mozart-oz.org/) combo may have a few surprises of their own.

* * *

The Lisp Curse does not contradict the maxim of [Stanislav Datskovskiy](http://www.loper-os.org/?p=69): **Employers much prefer that workers be fungible, rather than maximally productive.** Too true. With great difficulty does anyone plumb the venality of the managerial class. However, the last lines of his essay are problematic. To wit:

>

>  As for the “free software” world, it eagerly opposes industrial dogmas in rhetoric but not at all in practice. No concept shunned by cube farm hells has ever gained real traction among the amateur masses.

>

In a footnote, he offers Linux as an example of this unwillingness to pursue different ideas. To be sure, he has a point when it comes to [operating systems](http://slashdot.org/story/00/06/06/1151209/Systems-Research-Is-Dead) (the topmost comment, in particular, is infuriatingly obtuse). He does not have a point when it comes to programming languages. Python and Ruby were influenced by Lisp. Many of their fans express respect for Lisp and some of their interest has augmented the Lisp renaissance. With some justice, JavaScript has been described as "Scheme in C's clothing" despite originating in those [cube farm hells](http://www.jwz.org/tent-of-doom/).

Nevertheless, in spite of this influence, in both the corporate *and* open source worlds, Lisp still has only a fraction of the developer mind share which the current crop of advanced scripting languages have attracted. The closed-mindedness of MBA's cannot be the only explanation for this. The Lisp Curse has more explanatory power.

* * *

The free development environments available for Lisp further exemplify the Lisp Curse.

It's embarrassing to point this out, but it must be done. Forget about the Lisp Machine; we don't even have development systems that match what the [average](http://www.squeak.org/)  [Smalltalk](http://www.opencobalt.org/)  [hacker](http://www.pharo-project.org/home) takes for granted ("I've always felt Lisp is the superior language and Smalltalk is the superior environment." - [Ramon Leon](http://onsmalltalk.com/aha-moments-in-lisp)). Unless they pay thousands of dollars, Lisp hackers are still stuck with Emacs.

James Gosling, the author of the first Emacs that ran on Unix, [has correctly pointed out](http://www.computerworld.com.au/article/207799/don_t_use_emacs_says_java_father/) that Emacs has not fundamentally changed in more than twenty years. This is because the Emacs maintainers are still layering code atop a design which was settled back when Emacs was a grad-student project at the MIT AI Lab, i.e., when Emacs development was still being indirectly financed by the national debt. A Slashdotter may object that Emacs is already quite capable and can do anything that any other development environment can do, only better. Those [who have used](http://www.ymeme.com/zmacs-vs-emacs-manual.html) Lisp Machines say otherwise.

So why don't the Lisp hackers put the Smalltalk guys in their proper place? Why don't they make a free development system that calls to mind some of the lost glories of the LispM, even if they can't reproduce another LispM?

The reason why this doesn't happen is because of the Lisp Curse. Large numbers of Lisp hackers would have to cooperate with each other. Look more closely: Large numbers *of the kind of people who become Lisp hackers* would have to cooperate with each other. And they would have to cooperate with each other on a design which was not already a given from the beginning. And there wouldn't be any external discipline, such as a venture capitalist or other corporate master, to keep them on track.

Every project has friction between members, disagreements, conflicts over style and philosophy. These social problems are counter-acted by the fact that no large project can be accomplished otherwise. "We must all hang together, or we will all hang separately." But the expressiveness of Lisp makes this countervailing force much weaker; one can always start one's own project. Thus, individual hackers decide that the trouble isn't worth it. So they either quit the project, or don't join the project to begin with. This is the Lisp Curse.

One could even hack Emacs to get something that's *good enough*. Thus, the Lisp Curse is the ally of Worse is Better.

* * *

 **The expressive power of Lisp has drawbacks. There is no such thing as a free lunch.**