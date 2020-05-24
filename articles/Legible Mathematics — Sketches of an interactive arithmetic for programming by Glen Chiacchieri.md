Legible Mathematics — Sketches of an interactive arithmetic for programming by Glen Chiacchieri

# Legible Mathematics

## Sketches of an interactive arithmetic for programming

### [Glen Chiacchieri](http://glench.com/) | May 2014

Most arithmetic in modern programming environments looks like this:
 ![](../_resources/4757a3cd00337ebc1e45937a9a7870be.png)
Or this:
 ![](../_resources/2ab8f0c2a1647d2b78843a76e2b34c18.png)

Even these relatively simple equations take some work to decipher. The letters tend to blend together into a jumble of meaningless symbols. Consider an alternative from a prototype programming environment:

 ![](../_resources/f9d06f187697e25882e905f506095e08.png)

In this form, the structure of the equation is much clearer. But to me the problem isn't just that the first examples are badly formatted (missing spaces between operators, for example), or even that the environment isn't rendering those equations using the traditional notation taught in grade school. The main problem is that **the programming environment doesn't give us any way of understanding what the symbols are doing.**

Programmers have to imagine what each line does and how it does it. "Bugs" happen when this mental understanding doesn't match what's actually happening in the program, and because most current programming environments don't provide any feedback or tools for understanding program behavior, discovering and fixing bugs can be extremely difficult for experts and nearly impossible for beginners.

Programming environments aren't enough, though. Programming *languages* must provide powerful and understandable models for creating behavior. Here, I only address the environment. For more, see Bret Victor's [Inventing on Principle](http://worrydream.com/InventingOnPrinciple/) and [Learnable Programming](http://worrydream.com/LearnableProgramming/), both of which provided much of the inspiration for this essay.

To remove bugs — to correct misunderstandings of how programs work and make it much easier for beginners to learn — **our programming environments need to take program behavior out of programmers' heads and make it visible, tangible, and explorable.** In a word: *legible*.

How can our environments provide visual and interactive tools to make programs understandable for readers and writers? In this essay, I offer some clues from a prototype programming environment for arithmetic. My hope is that by exploring this fairly simple domain, I can inspire ideas for making more transparent environments for understanding and creating computer behavior.

## Understanding traditional notation

As hinted above, this programming environment supports traditional arithmetic notation:

![type.png](../_resources/92d19351acc8ab48f281014b62c39148.png)Hover or tap

Authors type arithmetic as they do today (using the `^`, `*`, `/`, `+`, `-` characters), and the environment will format expressions using traditional notation.

Though this notation has a long history (see [Cajori's A History of Mathematical Notations](https://archive.org/details/historyofmathema031756mbp) or [Wikipedia](http://en.wikipedia.org/wiki/History_of_mathematical_notation)), it's very unlikely that it's the "best" notation. For example, we should remember that it was developed for pencil and paper. Now that we have computational devices, we can invent ways of understanding arithmetic that take advantage of this medium. See Bret Victor's [Kill Math](http://worrydream.com/KillMath/).

But I think it's important to understand why we should even use this notation. Arithmetic notation was developed over *hundreds* of years. The notation is so successful that most people can't even imagine arithmetic another way. Compared to the anti-notation used in modern programming environments, we can start to see why.

 ![](../_resources/277f6d20212976e011b225e61dd497f8.png)

* *P*arentheses *E*xponents *M*ultiplication/*D*ivision *A*ddition/*S*ubtraction

When trying to understand an equation in the form above, we have to think through the order of operations (remember PEMDAS?*), mentally group the characters, and imagine how these parts combine.

But traditional notation does this all *visually*, creating mathematically meaningful groups of characters. This power to **visually decompose program behavior** is the real advantage of traditional notation, and our programming environments should do the same.

## Providing immediate feedback

Critically, rendering this notation **should happen instantly as you type**. There shouldn't be any compiling, switching to an output window, or delay of any kind.

To see one reason why immediate feedback is important, consider this example.

In the following demonstration I'm attempting to calculate the average cost of my electric bill over the past 3 months, a trivial program. In current programming environments, I might type something like this:

 ![](../_resources/b206d5ac5a1fb4a2f906edb7c904e984.png)

But because there's no feedback, I can't spot the very simple bug that becomes obvious in a better environment:

 ![](../_resources/5a9ff040009a040f7071980642eb52d6.png)
* An average of positive numbers can't be larger than its largest term.

I was trying to divide all three addition terms by the number of months, but only divided the last one by accident. Both the visual order of operations as well as the strange answer* provide immediate clues that something is wrong with my program and allow me to fix it with the addition of parentheses:

 ![](../_resources/a8399f5b47fdbce5cda2bba61bf0e509.png)

Of course, this example is extremely simple, but when we don't have immediate visual feedback, even trivial expressions like this can have bugs. If this line was part of a larger program, the bug could easily go unnoticed until much later, at which point all context is lost.

## Improving the notation

In fact, we can automatically show all kinds of useful visual feedback with our notation to make expressions as immediately understandable as possible.

For example, in this environment all numbers are automatically separated at their thousands places (noted with red markers here) to help convey magnitude:

 ![](../_resources/a1191a1b7ed37492aab8e4981eb2c6f8.png)
And likewise for places after the decimal:
 ![](../_resources/ab7268ebc924373c4a8e852faac657c9.png)

Terms that are evaluated together are grouped together, so the order of operations are made more visible:

 ![](../_resources/03816caf0b053ecf38623768f9d9be3e.png)

Notice above how the multiplied terms are grouped closer together to show that they're evaluated before being added to the rest of the expression.

Terms with exponents are grouped by themselves to suggest that they are evaluated before being multiplied or added:

 ![](../_resources/c821f5676435d3890935c077244e6474.png)

Thanks to [Soulver](http://www.acqualia.com/soulver/) for inspiring this feature.

The environment also supports labeling numbers:
 ![](../_resources/36cf24632996aca63c9c9ec2e8e85217.png)

Ideally, environments would automatically understand the data we're manipulating and provide appropriate tools and representations. I believe the [Wolfram Language](http://www.wolfram.com/wolfram-language/) is attempting this on some level, but more exploration of the problem is needed.

The labels don't affect the expression, but allow us to give additional meaning to our data. We rarely work with unitless numbers in our programs — all numbers mean *something*. At minimum, environments should let us label our data.

Finally, this environment supports variables.

A potential problem with this design for variable names is that it could make scanning and understanding an expression as a whole more difficult. Many environments will often use color to distinguish variables, but it's worth exploring alternatives.

 ![](../_resources/3f9e3b46680be0e4f5e8e46a70e938f6.png)

For an extreme take on this, see MIT's [Scratch](http://scratch.mit.edu/), which makes heavy use of shape and color to distinguish variables and control flow.

Variable names have a background color and border to visually distinguish them as separate entities. Observe that without this design, the variable names become less distinct:

 ![](../_resources/76f3954fcc72b1d762e0f0974ce9bdfc.png)

As with any good notation, ours must **visually distinguish meaningful parts of programs.**

## Showing the data

While the notation is important for showing the program's structure, we must also understand a program's data. For arithmetic, that means showing the values of an equation's subexpressions and variables.

In this environment, we can point to a subexpression with our cursor to see its value:

![hover.png](../_resources/623b56187c88a5612a857ab4150d31de.png)Hover or tap

This allows us to "peer into" an expression to see its internal behavior.

In paper arithmetic, we don't care much about the inner workings of expressions. It's assumed that what's written down is what we want. But in programming environments where we use abstract values in complex programs, we need to **see the data and how it changes.**

In the following example, we're trying to calculate the average speed of an object, but for some reason that speed is infinite.

![average_speed_point.png](../_resources/7e4344239b32194843a317df4a2de37b.png)Hover or tap

The answer is Infinity instead of a divide-by-zero error because JavaScript is crazy. A better language and environment would probably just tell you the denominator is 0 and try to show you why.

Inspecting the subexpressions, we find that the denominator is 0, meaning the two time samples are the same. From this, we know to look more closely at the time variables to find the program's bug. There's no need to *guess* the denominator is 0 — we can just see it.

## Showing the steps

Pointing to subexpressions gives us insight into individual parts of expressions, but viewing one part at a time is limiting. In this environment, hovering over the ![](../_resources/931a135c7fc32535073edea4808d8986.png) button next to an expression will show all the steps used to evaluate it:

Newly evaluated subexpressions are shown in black to aid in comparing steps.

![steps.png](../_resources/df65ecb58219b33fba82d331fe0a613e.png)Hover or tap

In this view, we can scan through an expression's entire execution to understand how it works or find where something went wrong. While most of us understand arithmetic's behavior already, **showing the steps leaves nothing to the imagination.** This may especially be useful for beginners who aren't yet familiar with a language's execution.

Reexamining the average-speed example above, we can use this feature to understand why the object's speed is unexpectedly infinite.

 ![](../_resources/557b034826d8ea8e4b9d19b445b0c97b.png)

In the last few steps we see again that the denominator is 0 because the time samples are the same.

## Showing everything with a new notation

Pointing to subexpressions shows only a single result at a time. The above drop-down shows all the steps taken to evaluate an expression, but with considerable redundancy. Here is an interesting notation that attempts to improve on both features:

![newnotation.png](../_resources/150a25e69272a3183c932efa407d8314.png)Hover or tap

For more on information design and avoiding interactivity, see [Edward Tufte](http://www.edwardtufte.com/tufte/books_vdqi) and the [Interactivity Considered Harmful](http://worrydream.com/MagicInk/#interactivity_considered_harmful) section of Bret Victor's [Magic Ink](http://worrydream.com/MagicInk/). For more about new notations for understanding programs, see [Chris Hancock's thesis](https://llk.media.mit.edu/papers/ch-phd.pdf).

Each subexpression is immediately annotated with the value it produces, allowing us to catch bugs even in the middle of typing. With this notation, **the system is completely transparent.** Nothing is hidden inside symbols or abstractions, and there is no need to interact with the system to see deeper. We can answer questions about the expression as fast as our eyes can move.

Using this feature to debug our average-speed example above, the expression's misbehavior is clear just by looking at it:

 ![](../_resources/982222d9b021e2a96a16fe5495999de5.png)
* It's somewhat distracting and space-inefficient, for instance.

While I don't expect this notation to be used all the time*, it does a wonderful job of showing an expression's structure and data with minimal interaction.

## Creating understandable expressions

A lot of the features so far have been about visually distinguishing parts of expressions, but we can also interactively break expressions down into more manageable pieces.

In the example below, I've written an expression for the volume of a rectangular prism, but perhaps I want to show that the first two terms represent the object's 2d base area:

![](../_resources/5304b2dbf43bd2ada3016f07a3ff881c.png)Hover or tap

This environment allows us to point to parts of a complicated expression and drag them off into their own variable so we can think about them separately.

## Answering what-if questions

Now that we can see an expression's internal behavior and data, we also need to explore the expression's unseen behavior to understand how programs react under different circumstances.

In this environment, we can scrub individual numbers to get a quick idea of how an expression reacts to changes in data:

![](../_resources/5fed8079880f175715d88e4ed262560b.png)Hover or tap

But more interestingly, we can also temporarily short-circuit subexpressions by changing their values:

![edit_subexpression.png](../_resources/250d8168bd68e0acca1253302ee41e27.png)Hover or tap

Together these features allow us to **quickly and reversibly test program behavior with varying data**.

Ted Nelson has been exploring, among other things, branching paths for writing with his [Project Xanadu](http://en.wikipedia.org/wiki/Project_Xanadu).

One of the most important questions *any* creator asks is *What would happen if this was different?* A graphic artist wants to know how different colors might affect the tone of an image, a musician wonders how altering a melody might change a piece, and a film editor wants to see how rearranging scenes in a film would look. **What-if questions are at the heart of creative exploration and our tools need to provide answers.** Programming is no different. Temporarily altering data is a small step in that direction, but much more exploration is needed.

Also interesting to consider is how these temporary experiments might be folded back into the program.

## Showing the entire behavior

Changing subexpression values is good for testing a small range of numbers, but to really understand the behavior of our expressions, we need to see how they react for *all* values.

Thanks to Omar Rizwan and his [Cruncher](http://rsnous.com/cruncher/) for the idea of plotting values.

This environment allows us to abstract a particular number or subexpression to see how its value affects the overall expression:

![](../_resources/94e7a62cb8bcfc40ffaa3ea37d437712.png)Hover or tap

Seeing this subexpression plotted against the result of the overall expression means we know how the expression reacts for every value. With this graph, we can completely understand what this subexpression does. There is no imagining or tedious manual testing. We can just see how it works.

Perhaps programming environments could even generate ranges of data before we ask and let us look over the results.

This ability to **see program behavior for ranges of inputs** could prove to be a powerful technique. In an environment for arithmetic, we can use a Cartesian plot to completely show the behavior of varying numbers. For other kinds of program data it's less clear how this could be done, but nonetheless should be explored.

## Conclusion

I've presented several features in this essay that were intended to render arithmetic's behavior visible and tangible. I've attempted to achieve this primarily through visual design, making expression behavior obvious with graphical techniques, but I've also added light interactive features to help programmers actively explore their programs. I think beginners and experts alike need these kinds of powerful visual and interactive tools to make programming easier to learn and easier to debug.

The ideas presented above are just a sketch, a glimmer on the horizon of understanding. I don't know how or if they'll scale to "real-world" programming, but I think they're worth considering. One day, I hope that these sorts of reactive environments are the norm, that anything resembling arithmetic today will feel hopelessly lifeless, even broken. But until then...

 ![](../_resources/4757a3cd00337ebc1e45937a9a7870be.png)

Thanks to [Chris Granger](http://www.chris-granger.com/), [Dave Mankoff](http://ohthehugemanatee.net/), Jake Brady, and Ada Munroe for their feedback on drafts of this essay and to [Josh Green](http://emailcoder.net/) for use of this background image.