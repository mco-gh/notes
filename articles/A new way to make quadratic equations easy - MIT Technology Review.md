A new way to make quadratic equations easy - MIT Technology Review

### [Humans and Technology](https://www.technologyreview.com/humans-and-technology/)

# A new way to make quadratic equations easy

## Many former algebra students have painful memories of struggling to memorize the quadratic formula. A new way to derive it, overlooked for 4,000 years, is so simple it eliminates the need.

by [Emerging Technology from the arXiv](https://www.technologyreview.com/profile/emerging-technology-from-the-arxiv/)

Dec 6, 2019

The ancient Babylonians were a remarkable bunch. Among many extraordinary achievements, they found a now-famous mathematical solution to an unpleasant challenge: paying tax.

The particular problem for the ordinary working Babylonian was this: Given a tax bill that has to be paid in crops, by how much should I increase the size of my field to pay it?

This problem can be written down as a quadratic equation of the form Ax2+Bx+C=0. And it is solved with this formula:

![first.png](../_resources/301494379a8f197b6cdb4fb29951515e.png)

Today, over 4,000 years later, millions of people have the quadratic formula etched into their minds thanks to the way mathematics is taught across the planet.

But far fewer people can derive this expression. That’s also due to the way mathematics is taught—the usual derivation relies on a mathematical trick, called “completing the square,” that is far from intuitive. Indeed, after the Babylonians, it took mathematicians many centuries to stumble across this proof.

Before and since, mathematicians have found a wide range of other ways to derive the formula. But all of them are also tricky and non-intuitive.

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 43.54 55.59' style='fill:%234a4a4a' data-evernote-id='527' class='js-evernote-checked'%3e%3cpolygon points='27.11 37.52 12.76 23.17 16.29 19.63 27.11 30.45 37.92 19.63 41.46 23.17 27.11 37.52' data-evernote-id='528' class='js-evernote-checked'%3e%3c/polygon%3e%3crect x='24.77' y='3.79' width='5' height='30' data-evernote-id='529' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M0%2c0H19.75c16.4%2c0%2c23.79%2c11.51%2c23.79%2c28s-7.93%2c27.6-24.34%2c27.6H0ZM19.05%2c51c13.29%2c0%2c19-8.94%2c19-23s-5.2-23.4-18.5-23.4H5.21V51Z' data-evernote-id='530' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M11.11%2c3.28h5.21V39.79H36.94v4.82H11.11Z' data-evernote-id='531' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

#### Sign up for **The Download** — your daily dose of what's up in emerging technology

Also stay updated on MIT Technology Review initiatives and events?
YesNo

So it’s easy to imagine that mathematicians must have exhausted the problem. There just can’t be a better way to derive the quadratic formula.

Enter Po-Shen Loh, a mathematician at Carnegie Mellon University in Pittsburgh, who has found a simpler way—one that appears to have gone unnoticed these 4,000 years.

Loh’s approach does not rely on completing the square or any other difficult mathematical tricks. Indeed, it is simple enough to work as a general method itself, meaning students need not remember the formula at all. “The derivation has the potential to demystify the quadratic formula for students worldwide,” he says.

The new approach is straightforward. It starts by observing that if a quadratic equation can be factorised in the following way :

Then the right-hand side equals 0 when x=R or when x=S. Then those would be the roots of quadratic.

Multiplying out the right hand side gives

This is true when -B=R+S and when C=RS.

Now here comes the clever bit. Loh points out that the numbers, R and S, add up to -B when their average is -B/2.

“So we seek two numbers of the form -B/2±z, where z is a single unknown quantity,” he says. We can then multiply these numbers together to get an expression for C. So

Then some simple rearranging gives

Which means that the solution for a quadratic equation is:

Voilà! That’s the quadratic formula.

[The more general version can be derived by dividing the equation Ax2+Bx+C=0 by A to give x2+B/Ax+C/A=0 and then repeating the above process.]

That’s a very significant improvement on the previous method, and Loh shows why with a simple example.

Find the roots of the following quadratic: x2 - 2x+4=0

The traditional method would be to work out values for A, B, and C and plug them into the quadratic formula. But Loh’s approach solves the problem intuitively. The first step is to think that the two roots of the equation must be equal to -B/2±z = 1±z

And because their product must be C=4, we can write:

So the roots are

Attempting the same problem using the traditional method is much trickier. Go on, give it a go! The new approach is much easier and more intuitive, not least because it doesn’t require the formula to be memorized at all.

An interesting question is why nobody has stumbled across and widely shared this method before.

Loh says he "would actually be very surprised if this approach has entirely eluded human discovery until the present day, given the 4,000 years of history on this topic, and the billions of people who have encountered the formula and its proof. Yet this technique is certainly not widely taught or known."

Loh has searched the history of mathematics for an approach that resembles his, without success. He has looked at methods developed by the ancient Babylonians, Chinese, Greeks, Indians, and Arabs as well as modern mathematicians from the Renaissance until today. None of them appear to have made this step, even though the algebra is simple and has been known for centuries.

So why now? Loh thinks it is related to the way the conventional approach proves that quadratic equations have two roots. “Perhaps the reason is because it is actually mathematically nontrivial to make the reverse implication: that always has two roots, and that those roots have sum −B and product C,” he says.

Loh, who is a mathematics educator and popularizer of some note, discovered his approach while analyzing mathematics curricula for schoolchildren, with the goal of developing new explanations. The derivation emerged from this process.

The question now is how widely it will spread and how quickly. To speed adoption, [Loh has produced a video about the method](https://www.youtube.com/watch?v=ZBalWWHYFQc&feature=youtu.be&list=PLqv4sKOD1bsUoSs-SbzlA2BE1tML4A33u). Either way, Babylonian tax calculators would surely have been impressed.

Ref: [arxiv.org/abs/1910.06709](https://arxiv.org/abs/1910.06709) : A Simple Proof of the Quadratic Formula

*Correction: We amended a sentence to say that the method has never been widely shared before and included a quote from Loh.*![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 288 287.99' class='jsx-671803276 glyph js-evernote-checked' data-evernote-id='654'%3e%3cpath d='M199.49%2c66.67%2c133%2c133.11H66.56V66.67Zm44.31%2c0-66.46%2c66.44V354.66h66.46V133.11H354.56V66.67Z' transform='translate(-66.56 -66.67)' class='jsx-671803276 js-evernote-checked' data-evernote-id='655'%3e%3c/path%3e%3c/svg%3e)