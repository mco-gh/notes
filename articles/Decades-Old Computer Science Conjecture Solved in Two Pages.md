Decades-Old Computer Science Conjecture Solved in Two Pages

###### [combinatorics](https://www.quantamagazine.org/tag/combinatorics/)

# Decades-Old Computer Science Conjecture Solved in Two Pages

The “sensitivity” conjecture stumped many top computer scientists, yet the new proof is so simple that one researcher summed it up in a single tweet.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='225' data-evernote-id='203' class='js-evernote-checked'%3e%3cpath fill='currentColor' d='M9.4 4.2h31.2c8.6 0 9.4 7 9.4 15.6s-.7 15.6-9.4 15.6h-2.2l-.9 9.4-18.8-9.4H9.4c-8.6 0-9.4-7-9.4-15.6S.7 4.2 9.4 4.2z' data-reactid='226' data-evernote-id='508' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) 11](https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/#comments)

###### Read Later

![Boolean-Sensitivity_2880x1620_Lede.gif](../_resources/0de9dd222e45806ebad5a334e821c397.gif)
[Dave Whyte](http://beesandbombs.com/) for Quanta Magazine

[ ![Klarreich_Erica1.jpg](../_resources/92dcb0047e0883624414d8b3959d9f32.jpg)    ### Erica Klarreich  *Contributing Correspondent*](https://www.quantamagazine.org/authors/erica-klarreich/)

* * *

*July 25, 2019*

* * *

[View PDF/Print Mode![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-l theme__accent ml05 js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='274' data-evernote-id='205'%3e%3cpath fill='currentColor' d='M39.9%2c27.5h4.9v22.4H0.1V5.1h22.4V10H5v35h35V27.5z M49.8%2c0.1h-2.4h-1H33.8V5h7.6L20.7%2c25.8l3.4%2c3.4L45%2c8.4v7.7h4.9V2.6L49.8%2c0.1z' data-reactid='275' data-evernote-id='543' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/#)

[combinatorics](https://www.quantamagazine.org/tag/combinatorics/)[computer science](https://www.quantamagazine.org/tag/computer-science/)[mathematics](https://www.quantamagazine.org/tag/mathematics/)

[![Audible_Article_320x600_Math.jpg](../_resources/cf42f0efe33aa759ffd905751679882a.jpg)](https://www.amazon.com/Prime-Number-Conspiracy-Biggest-Quanta/dp/B07SXBR9Y3/)

A [paper posted online](https://arxiv.org/abs/1907.00847) this month has settled a nearly 30-year-old conjecture about the structure of the fundamental building blocks of computer circuits. This “sensitivity” conjecture has stumped many of the most prominent computer scientists over the years, yet the new proof is so simple that one researcher summed it up in a [single tweet](https://twitter.com/BooleanAnalysis/status/1145837576487612416).

“This conjecture has stood as one of the most frustrating and embarrassing open problems in all of combinatorics and theoretical computer science,” wrote [Scott Aaronson](https://www.cs.utexas.edu/directory/scott-aaronson) of the University of Texas, Austin, in a [blog post](https://www.scottaaronson.com/blog/?p=4229). “The list of people who tried to solve it and failed is like a who’s who of discrete math and theoretical computer science,” he added in an email.

The conjecture concerns Boolean functions, rules for transforming a string of input bits (0s and 1s) into a single output bit. One such rule is to output a 1 provided any of the input bits is 1, and a 0 otherwise; another rule is to output a 0 if the string has an even number of 1s, and a 1 otherwise. Every computer circuit is some combination of Boolean functions, making them “the bricks and mortar of whatever you’re doing in computer science,” said [Rocco Servedio](http://www.cs.columbia.edu/~rocco/) of Columbia University.

*open-quote*

I find it hard to imagine that even God knows how to prove the Sensitivity Conjecture in any simpler way than this.

*close-quote*
Scott Aaronson

Over the years, computer scientists have developed many ways to measure the complexity of a given Boolean function. Each measure captures a different aspect of how the information in the input string determines the output bit. For instance, the “sensitivity” of a Boolean function tracks, roughly speaking, the likelihood that flipping a single input bit will alter the output bit. And “query complexity” calculates how many input bits you have to ask about before you can be sure of the output.

Each measure provides a unique window into the structure of the Boolean function. Yet computer scientists have found that nearly all these measures fit into a unified framework, so that the value of any one of them is a rough gauge for the value of the others. Only one complexity measure didn’t seem to fit in: sensitivity.

In 1992, [Noam Nisan](http://www.cs.huji.ac.il/~noam/) of the Hebrew University of Jerusalem and [Mario Szegedy](https://www.cs.rutgers.edu/~szegedy/), now of Rutgers University, [conjectured](https://dl.acm.org/citation.cfm?id=129757) that sensitivity does indeed fit into this framework. But no one could prove it. “This, I would say, probably was the outstanding open question in the study of Boolean functions,” Servedio said.

“People wrote long, complicated papers trying to make the tiniest progress,” said [Ryan O’Donnell](http://www.cs.cmu.edu/~odonnell/) of Carnegie Mellon University.

Now [Hao Huang](http://www.math.emory.edu/people/faculty/individual.php?NUM=397), a mathematician at Emory University, has proved the sensitivity conjecture with an ingenious but elementary two-page argument about the combinatorics of points on cubes. “It is just beautiful, like a precious pearl,” wrote [Claire Mathieu](https://www.di.ens.fr/ClaireMathieu.html), of the French National Center for Scientific Research, during a Skype interview.

Aaronson and O’Donnell both called Huang’s paper the “book” proof of the sensitivity conjecture, referring to [Paul Erdős’ notion](https://www.quantamagazine.org/gunter-ziegler-and-martin-aigner-seek-gods-perfect-math-proofs-20180319/) of a celestial book in which God writes the perfect proof of every theorem. “I find it hard to imagine that even God knows how to prove the Sensitivity Conjecture in any simpler way than this,” Aaronson [wrote](https://www.scottaaronson.com/blog/?p=4229).

## A Sensitive Matter

Imagine, Mathieu said, that you are filling out a series of yes/no questions on a bank loan application. When you’re done, the banker will score your results and tell you whether you qualify for a loan. This process is a Boolean function: Your answers are the input bits, and the banker’s decision is the output bit.

If your application gets denied, you might wonder whether you could have changed the outcome by lying on a single question — perhaps, by claiming that you earn more than $50,000 when you really don’t. If that lie would have flipped the outcome, computer scientists say that the Boolean function is “sensitive” to the value of that particular bit. If, say, there are seven different lies you could have told that would have each separately flipped the outcome, then for your loan profile, the sensitivity of the Boolean function is seven.

Computer scientists define the overall sensitivity of the Boolean function as the biggest sensitivity value when looking at all the different possible loan profiles. In some sense, this measure calculates how many of the questions are truly important in the most borderline cases — the applications that could most easily have swung the other way if they’d been ever so slightly different.

![Boolean_Sensitivity_FINAL560-1068x1720.jpg](../_resources/f2579ed161bbf2e5c9f561f3537ed949.jpg)

Lucy Reading-Ikkanda/Quanta Magazine

Sensitivity is usually one of the easiest complexity measures to compute, but it’s far from the only illuminating measure. For instance, instead of handing you a paper application, the banker could have interviewed you, starting with a single question and then using your answer to determine what question to ask next. The largest number of questions the banker would ever need to ask before reaching a decision is the Boolean function’s query complexity.

This measure arises in a host of settings — for instance, a doctor might want to send a patient for as few tests as possible before reaching a diagnosis, or a machine learning expert might want an algorithm to examine as few features of an object as possible before classifying it. “In a lot of situations — diagnostic situations or learning situations — you’re really happy if the underlying rule … has low query complexity,” O’Donnell said.

Other measures involve looking for the simplest way to write the Boolean function as a mathematical expression, or calculating how many answers the banker would have to show a boss to prove they had made the right loan decision. There’s even a quantum physics version of query complexity in which the banker can ask a “superposition” of several questions at the same time. Figuring out how this measure relates to other complexity measures has helped researchers understand the [limitations of quantum algorithms](https://www.quantamagazine.org/quantum-computers-struggle-against-classical-algorithms-20180201/).

With the single exception of sensitivity, computer scientists proved that all these measures are closely linked. Specifically, they have a polynomial relationship to each other — for example, one measure might be roughly the square or cube or square root of another. Only sensitivity stubbornly refused to fit into this neat characterization. Many researchers suspected that it did indeed belong, but they couldn’t prove that there were no strange Boolean functions out there whose sensitivity had an exponential rather than polynomial relationship to the other measures, which in this setting would mean that the sensitivity measure is vastly smaller than the other measures.

“This question was a thorn in people’s sides for 30 years,” Aaronson said.

## Cornering the Solution

Huang heard about the sensitivity conjecture in late 2012, over lunch with the mathematician [Michael Saks](http://sites.math.rutgers.edu/~saks/) at the Institute for Advanced Study, where Huang was a postdoctoral fellow. He was immediately taken with the conjecture’s simplicity and elegance. “Starting from that moment, I became really obsessed with thinking about it,” he said.

Huang added the sensitivity conjecture to a “secret list” of problems he was interested in, and whenever he learned about a new mathematical tool, he considered whether it might help. “Every time after I’d publish a new paper, I would always go back to this problem,” he said. “Of course, I would give up after a certain amount of time and work on some more realistic problem.”

![Hao-Huang_Yao-Yao-2000x1500-1720x1290.jpg](../_resources/40021275904c2fffc362aee5022fde4e.jpg)

The mathematician Hao Huang during a recent vacation in Lisbon.
Yao Yao

Huang knew, as did the broader research community, that the sensitivity conjecture could be settled if mathematicians could prove an easily stated conjecture about collections of points on cubes of different dimensions. There’s a natural way to go from a string of *n* 0s and 1s to a point on an *n*-dimensional cube: Simply use the *n* bits as the coordinates of the point.

For instance, the four two-bit strings — 00, 01, 10 and 11 — correspond to the four corners of a square in the two-dimensional plane: (0,0), (0,1), (1,0) and (1,1).  Likewise, the eight three-bit strings correspond to the eight corners of a three-dimensional cube, and so on in higher dimensions. A Boolean function, in turn, can be thought of as a rule for coloring these corners with two different colors (say, red for 0 and blue for 1).

In 1992, [Craig Gotsman](http://www.cs.technion.ac.il/~gotsman/), now of the New Jersey Institute of Technology, and [Nati Linial](http://www.cs.huji.ac.il/~nati/) of Hebrew University [figured out](https://dl.acm.org/citation.cfm?id=158788) that proving the sensitivity conjecture can be reduced to answering a simple question about cubes of different dimensions: If you choose any collection of more than half the corners of a cube and color them red, is there always some red point that is connected to many other red points? (Here, by “connected,” we mean that the two points share one of the outer edges of the cube, as opposed to being across a diagonal.)

*open-quote*

I expect that this fall it will be taught — in a single lecture — in every master’s-level combinatorics course.

*close-quote*
Claire Mathieu

If your collection contains exactly half the corners of the cube, it’s possible that none of them will be connected. For example, among the eight corners of the three-dimensional cube, the four points (0,0,0), (1,1,0), (1,0,1) and (0,1,1) all sit across diagonals from one another. But as soon as more than half the points in a cube of any dimension are colored red, some connections between red points must pop up. The question is: How are these connections distributed? Will there be at least one highly connected point?

In 2013, Huang started thinking that the best route to understanding this question might be through the standard method of representing a network with a matrix that tracks which points are connected and then examining a set of numbers called the matrix’s eigenvalues. For five years he kept revisiting this idea, without success. “But at least thinking about it [helped] me quickly fall asleep many nights,” he [commented](https://www.scottaaronson.com/blog/?p=4229#comment-1813116) on Aaronson’s blog post.

Then in 2018, it occurred to Huang to use a 200-year-old piece of mathematics called the Cauchy interlace theorem, which relates a matrix’s eigenvalues to those of a submatrix, making it potentially the perfect tool to study the relationship between a cube and a subset of its corners. Huang decided to request a grant from the National Science Foundation to explore this idea further.

Then last month, as he sat in a Madrid hotel writing his grant proposal, he suddenly realized that he could push this approach all the way to fruition simply by switching the signs of some of the numbers in his matrix. In this way, he was able to prove that in any collection of more than half the points in an *n*-dimensional cube, there will be some point that is connected to at least n‾√ of the other points — and the sensitivity conjecture instantly followed from this result.

When Huang’s paper landed in Mathieu’s inbox, her first reaction was “uh-oh,” she said. “When a problem has been around 30 years and everybody has heard about it, probably the proof is either very long and tedious and complicated, or it’s very deep.” She opened the paper expecting to understand nothing.

### Related:

* * *

1. 1.

##### [A 53-Year-Old Network Coloring Conjecture Is Disproved](https://www.quantamagazine.org/mathematician-disproves-hedetniemis-graph-theory-conjecture-20190617/)

2. 2.

##### [Mystery Math Whiz and Novelist Advance Permutation Problem](https://www.quantamagazine.org/sci-fi-writer-greg-egan-and-anonymous-math-whiz-advance-permutation-problem-20181105/)

3. 3.

##### [Decades-Old Graph Problem Yields to Amateur Mathematician](https://www.quantamagazine.org/decades-old-graph-problem-yields-to-amateur-mathematician-20180417/)

But the proof was simple enough for Mathieu and many other researchers to digest in one sitting. “I expect that this fall it will be taught — in a single lecture — in every master’s-level combinatorics course,” she messaged over Skype.

Huang’s result is even stronger than necessary to prove the sensitivity conjecture, and this power should yield new insights about complexity measures. “It adds to our toolkit for maybe trying to answer other questions in the analysis of Boolean functions,” Servedio said.

Most importantly, though, Huang’s result lays to rest nagging worries about whether sensitivity might be some strange outlier in the world of complexity measures, Servedio said. “I think a lot of people slept easier that night, after hearing about this.”

### Share this article

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='304' data-evernote-id='206'%3e%3cpath fill='currentColor' d='M13 16.5h5.1v-5c-.2-2.7.3-5.4 1.7-7.7 1.8-2.5 4.9-4 8-3.8 3.1-.1 6.2.2 9.2 1l-1.3 7.7C34.4 8.3 33 8 31.6 8c-2 0-3.8.7-3.8 2.7v5.9H36l-.6 7.5h-7.6V50h-9.6V23.9H13v-7.4z' data-reactid='305' data-evernote-id='666' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](http://www.facebook.com/sharer.php?u=https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='309' data-evernote-id='207'%3e%3cpath fill='currentColor' d='M50 9.9c-1.9.8-3.8 1.3-5.9 1.6 2.1-1.3 3.7-3.2 4.5-5.6-2 1.2-4.2 2-6.5 2.5-3.8-4.1-10.3-4.5-14.5-.8-2.8 2.5-4 6.3-3.1 10-8.2-.5-15.8-4.3-21-10.6-2.7 4.6-1.3 10.5 3.2 13.5C5 20.4 3.4 20 2 19.2c0 4.8 3.4 8.9 8.2 9.9-.9.2-1.8.4-2.7.3-.6 0-1.3-.1-1.9-.2 1.3 4.1 5.2 6.9 9.5 7C10.8 39.5 5.4 41 0 40.4c13.5 8.5 31.5 4.6 40.2-8.7 3-4.6 4.6-10 4.6-15.5v-1.3c2-1.3 3.7-3.1 5.2-5' data-reactid='310' data-evernote-id='669' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://twitter.com/share?url=https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/&text=Decades-Old%20Computer%20Science%20Conjecture%20Solved%20in%20Two%20Pages&via=QuantaMagazine)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' x='0px' y='0px' viewBox='0 0 50 50' enable-background='new 0 0 50 50' xml:space='preserve' data-reactid='314' data-evernote-id='208'%3e%3cg data-reactid='315' data-evernote-id='672' class='js-evernote-checked'%3e%3c!-- react-text: 316 --%3e %3c!-- /react-text --%3e%3cpath fill='currentColor' d='M20.6%2c38.5c-0.8%2c0-1.6%2c0.3-2.2%2c0.8L16%2c41.9c-1.1%2c1-2.4%2c1.6-3.9%2c1.6c-1.5%2c0-2.8-0.5-3.9-1.6c-0.5-0.5-0.9-1.1-1.2-1.8 c-0.3-0.7-0.4-1.4-0.4-2.1c0-0.7%2c0.1-1.4%2c0.4-2.1c0.3-0.7%2c0.7-1.2%2c1.2-1.8l9.1-9c1-0.9%2c2.2-1.8%2c3.8-2.7s3-0.7%2c4.3%2c0.7 c0.6%2c0.6%2c1.3%2c0.8%2c2.2%2c0.8s1.5-0.3%2c2.1-0.9c0.6-0.6%2c0.9-1.3%2c0.9-2.2s-0.3-1.6-0.9-2.2c-2.2-2.2-4.8-3.1-7.8-2.7 c-3%2c0.4-5.9%2c2-8.8%2c4.8l-9.2%2c9c-1.1%2c1.1-1.9%2c2.4-2.5%2c3.8C0.7%2c35%2c0.4%2c36.5%2c0.4%2c38c0%2c1.6%2c0.3%2c3%2c0.9%2c4.4c0.6%2c1.4%2c1.4%2c2.7%2c2.5%2c3.8 c1.1%2c1.1%2c2.4%2c2%2c3.8%2c2.5c1.4%2c0.6%2c2.9%2c0.8%2c4.4%2c0.8s2.9-0.3%2c4.3-0.8c1.4-0.6%2c2.7-1.4%2c3.8-2.5l2.5-2.5c0.6-0.6%2c0.9-1.3%2c0.9-2.1 s-0.3-1.6-0.9-2.2C22.1%2c38.8%2c21.4%2c38.5%2c20.6%2c38.5z' data-reactid='317' data-evernote-id='673' class='js-evernote-checked'%3e%3c/path%3e%3c!-- react-text: 318 --%3e %3c!-- /react-text --%3e%3cpath fill='currentColor' d='M48.7%2c7.9c-0.6-1.4-1.4-2.7-2.5-3.8c-2.4-2.4-5.1-3.6-8-3.7c-3-0.1-5.5%2c0.9-7.7%2c3.1l-3.1%2c3.1c-0.6%2c0.6-0.9%2c1.3-0.9%2c2.1 s0.3%2c1.6%2c0.9%2c2.2s1.3%2c0.9%2c2.2%2c0.9s1.6-0.3%2c2.2-0.8l3.1-3.1c1.2-1.1%2c2.4-1.5%2c3.7-1.3c1.3%2c0.3%2c2.5%2c0.9%2c3.4%2c1.9 c0.5%2c0.5%2c0.9%2c1.1%2c1.2%2c1.8c0.3%2c0.7%2c0.4%2c1.4%2c0.4%2c2.1c0%2c0.7-0.1%2c1.4-0.4%2c2.1c-0.3%2c0.7-0.7%2c1.2-1.2%2c1.8l-9.7%2c9.6 c-2.2%2c2.2-3.9%2c3.1-5.1%2c2.7s-2-0.8-2.4-1.3c-0.6-0.6-1.3-0.8-2.2-0.8s-1.5%2c0.3-2.1%2c0.9c-0.6%2c0.6-0.9%2c1.3-0.9%2c2.2s0.3%2c1.5%2c0.9%2c2.1 c1%2c1%2c2.1%2c1.8%2c3.2%2c2.3s2.4%2c0.7%2c3.6%2c0.7c1.5%2c0%2c3-0.4%2c4.6-1.1c1.6-0.7%2c3.1-1.9%2c4.6-3.4l9.8-9.6c1.1-1.1%2c1.9-2.4%2c2.5-3.8 c0.6-1.4%2c0.9-2.9%2c0.9-4.4C49.6%2c10.8%2c49.3%2c9.3%2c48.7%2c7.9z' data-reactid='319' data-evernote-id='674' class='js-evernote-checked'%3e%3c/path%3e%3c!-- react-text: 320 --%3e %3c!-- /react-text --%3e%3c/g%3e%3c/svg%3e)](https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/#0)

###### Copied!

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' x='0px' y='0px' viewBox='0 0 50 50' enable-background='new 0 0 50 50' xml:space='preserve' data-reactid='329' data-evernote-id='209'%3e%3cpath fill='currentColor' d='M25%2c29.5l-5.2-4.3L1.8%2c43.8h46L30.1%2c25.2L25%2c29.5z M32.6%2c23.2l17.2%2c17.9c0-0.2%2c0.1-0.3%2c0.1-0.5c0-0.2%2c0-0.4%2c0-0.6V9.1 L32.6%2c23.2z M0%2c9.1v31c0%2c0.2%2c0%2c0.4%2c0%2c0.6s0.1%2c0.3%2c0.1%2c0.5l17.3-17.8L0%2c9.1z M48.4%2c6.2H1.6L25%2c25L48.4%2c6.2z' data-reactid='330' data-evernote-id='682' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/mailto:?subject=Decades-Old%20Computer%20Science%20Conjecture%20Solved%20in%20Two%20Pages&body=The%20%E2%80%9Csensitivity%E2%80%9D%20conjecture%20stumped%20many%20top%20computer%20scientists,%20yet%20the%20new%20proof%20is%20so%20simple%20that%20one%20researcher%20summed%20it%20up%20in%20a%20single%20tweet.%0A%0Ahttps://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/)

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='336' data-evernote-id='210'%3e%3cpath fill='currentColor' d='M2.6%2c1.7C1.3%2c1.6%2c0.1%2c2.7%2c0%2c4.1c0%2c0.1%2c0%2c0.3%2c0%2c0.4v9.9c0%2c8.1%2c8%2c14.4%2c15%2c14.4c8-0.1%2c14.6-6.4%2c15-14.4v-10 c0.1-1.4-0.9-2.6-2.3-2.8c-0.2%2c0-0.4%2c0-0.5%2c0L2.6%2c1.7z M9%2c9.8l6%2c5.7l6-5.7c2.8-1.1%2c3.9%2c2%2c2.8%2c2.8L16%2c20.1c-0.6%2c0.3-1.3%2c0.3-1.9%2c0 l-7.9-7.5C5.2%2c11.5%2c6.5%2c8.4%2c9%2c9.8L9%2c9.8z' data-reactid='337' data-evernote-id='687' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://getpocket.com/save?url=https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/&title=Decades-Old%20Computer%20Science%20Conjecture%20Solved%20in%20Two%20Pages)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='341' data-evernote-id='211'%3e%3cpath fill='currentColor' d='M9.1%2c11v9.4h2.5c0.2%2c0%2c0.3-0.1%2c0.3-0.3c0%2c0%2c0%2c0%2c0%2c0v-9.2H9.3C9.2%2c10.8%2c9.1%2c10.9%2c9.1%2c11z' data-reactid='342' data-evernote-id='690' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='currentColor' d='M11.9%2c8.8V7.1H9.3C9.2%2c7.1%2c9%2c7.2%2c9%2c7.4c0%2c0%2c0%2c0%2c0%2c0v1.7h2.5c0.2%2c0%2c0.3-0.1%2c0.4-0.3C11.9%2c8.9%2c11.9%2c8.9%2c11.9%2c8.8 z' data-reactid='343' data-evernote-id='691' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='currentColor' d='M13.4%2c11v9.3h4.8v1.3h-4.4c-0.2%2c0-0.3%2c0.1-0.3%2c0.3c0%2c0%2c0%2c0%2c0%2c0v1.7h7.2c0.2%2c0%2c0.3-0.1%2c0.3-0.3c0%2c0%2c0%2c0%2c0-0.1 V10.7h-7.2C13.5%2c10.7%2c13.4%2c10.8%2c13.4%2c11C13.4%2c11%2c13.4%2c11%2c13.4%2c11z M16.1%2c13.1c0-0.2%2c0.1-0.3%2c0.3-0.3c0%2c0%2c0%2c0%2c0%2c0h1.7V18 c0%2c0.2-0.1%2c0.3-0.3%2c0.3c0%2c0%2c0%2c0%2c0%2c0h-1.7V13.1z' data-reactid='344' data-evernote-id='692' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='currentColor' d='M22.7%2c10.7c-0.2%2c0-0.3%2c0.1-0.3%2c0.3c0%2c0%2c0%2c0%2c0%2c0v9.3h4.8v1.3h-4.5c-0.2%2c0-0.3%2c0.1-0.3%2c0.3c0%2c0%2c0%2c0%2c0%2c0v1.7h7.3 c0.2%2c0%2c0.3-0.1%2c0.3-0.3c0%2c0%2c0%2c0%2c0%2c0V10.7H22.7z M27.2%2c18c0%2c0.2-0.1%2c0.3-0.3%2c0.4c0%2c0%2c0%2c0%2c0%2c0h-1.7v-5.2c0-0.2%2c0.1-0.3%2c0.3-0.3 c0%2c0%2c0%2c0%2c0%2c0h1.7V18z' data-reactid='345' data-evernote-id='693' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='currentColor' d='M5.1%2c7.1c-0.2%2c0-0.3%2c0.1-0.3%2c0.3c0%2c0%2c0%2c0%2c0%2c0v3.3H0.3C0.1%2c10.7%2c0%2c10.8%2c0%2c11c0%2c0%2c0%2c0%2c0%2c0v9.3h7.2 c0.2%2c0%2c0.3-0.1%2c0.3-0.3c0%2c0%2c0%2c0%2c0%2c0V7.1L5.1%2c7.1z M4.8%2c18c0%2c0.2-0.1%2c0.3-0.3%2c0.3c0%2c0%2c0%2c0%2c0%2c0H2.7v-5.2c0-0.2%2c0.1-0.3%2c0.3-0.3 c0%2c0%2c0%2c0%2c0%2c0h1.7L4.8%2c18z' data-reactid='346' data-evernote-id='694' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](http://digg.com/submit?url=https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='350' data-evernote-id='212'%3e%3cpath fill='currentColor' d='M12.9%2c18L3.2-0.1h4.4l5.7%2c11.5l0.3%2c0.6c0.1%2c0.2%2c0.2%2c0.4%2c0.3%2c0.7c0%2c0.1%2c0%2c0.2%2c0%2c0.2v0.2l0.4%2c0.9l0.5%2c0.7 l0.8-1.6l0.9-1.8l5.8-11.5h4.1l-9.8%2c18.3v11.7h-3.7V18z' data-reactid='351' data-evernote-id='697' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://news.ycombinator.com/submitlink?u=https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/&t=Decades-Old%20Computer%20Science%20Conjecture%20Solved%20in%20Two%20Pages)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='355' data-evernote-id='213'%3e%3cpath fill='currentColor' d='M30%2c0 0%2c0 0%2c30 10%2c30 10%2c20 20%2c20 20%2c10 30%2c10 z' data-reactid='356' data-evernote-id='700' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://share.flipboard.com/bookmarklet/popout?v=Decades-Old%20Computer%20Science%20Conjecture%20Solved%20in%20Two%20Pages&url=https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='ml05 icon icon-offset closed js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='358' data-evernote-id='214'%3e%3cpath fill='currentColor' d='M15%2c20.7c-0.1%2c0-0.3%2c0-0.4-0.1L0.3%2c10.7l0.9-1.2L15%2c19l13.8-9.5l0.9%2c1.2l-14.3%2c9.8C15.3%2c20.6%2c15.1%2c20.7%2c15%2c20.7 z' data-reactid='359' data-evernote-id='702' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

* * *

### Newsletter

*Get Quanta Magazine delivered to your inbox*

[(L)](https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/#newsletter)

[Most recent newsletter![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='ml05 icon js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='372' data-evernote-id='215'%3e%3cpath fill='currentColor' d='M50 25l-17.4-8.7v6.5H0v4.4h32.6v6.5' data-reactid='373' data-evernote-id='710' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](http://us1.campaign-archive2.com/home/?u=0d6ddf7dc1a0b7297c8e06618&id=f0cb61321c)