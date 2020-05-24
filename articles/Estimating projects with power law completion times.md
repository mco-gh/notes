Estimating projects with power law completion times

# The longer it has taken, the longer it will take

Posted on [21 December 2015](https://www.johndcook.com/blog/2015/12/21/power-law-projects/) by [John](https://www.johndcook.com/blog/author/john/)

Suppose project completion time follows a Pareto (power law) distribution with parameter α. That is, for *t* > 1, the probability that completion time is bigger than *t* is *t*-α. (We start out time at *t* = 1 because that makes the calculations a little simpler.)

Now suppose we know that a project has lasted until *t*0 so far. Then the expected finish time is α*t*0/(α-1) and so the expected additional time is *t*0/(α-1). Note that both are proportional to *t*0. So the longer it has taken, the longer it will take. If the project is running late, you can expect the time remaining to be even more than the expected time before the project started. The finish line is moving away from you!

For example, suppose α = 2 (in applications of power laws, α is often between 1 and 3) and you’re measuring time in years. When the project starts at *t* = 1, it is expected to take one year, until *t* = 2. Now suppose you’re starting the second year and the project isn’t done. Now it’s expected to finish at *t* = 4, two more years. When you started, the project was supposed to take a year. One year later, it has taken a year, and should be expected to take two more years. I said “should be expected” rather than “is expected” because no one would believe such an estimate. (Ever heard of the [Big Dig](https://en.wikipedia.org/wiki/Big_Dig)? Or other [megaprojects](http://www.econtalk.org/archives/2015/05/bent_flyvbjerg.html)?)

Note that we have computed the conditional probability given only the time it has taken so far, and *no other information*. If you know more, for example maybe you know that some specific pieces have been completed, then you should use that information.

This is related to the [Lindy effect](https://www.johndcook.com/blog/2012/12/17/the-lindy-effect/). The longer a cultural artifact has been around, the longer it is expected to last into the future.

* * *

For daily posts on probability, follow [@ProbFact](https://twitter.com/probfact) on Twitter.

[![](../_resources/16e150c01c3521fd16f05cd6615e513c.png)](https://twitter.com/probfact)

Categories : [Software development](https://www.johndcook.com/blog/category/software-development/)  [Statistics](https://www.johndcook.com/blog/category/statistics/)

Tags : [Probability and Statistics](https://www.johndcook.com/blog/tag/probability-and-statistics/)

Bookmark the [permalink](https://www.johndcook.com/blog/2015/12/21/power-law-projects/)