Calculus Explained with pics and gifs - 0a.io -

 ![ian-espinosa-311604-unsplash.jpg](../_resources/afce188e174844a10ac0ea0148deaffc.jpg)

#

 [  ](https://0a.io/)

##   [0a.io](https://0a.io/)

 [**](https://archy.sh/)  [**](https://twitter.com/archyisnotdead)  [ABOUT](https://0a.io/about.html)

##

##   [Copy Link](#)  [Back to Home Page](https://0a.io/)

 ![](../_resources/de09ffaeb263c24d74cc1adfcaaeb75a.png)

 [Moonlit Night (1914) by Emil Nolde](https://www.wikiart.org/en/Search/Moonlit%20Night%20Emil%20Nolde)

 October 27 2014

##  Calculus Explained with pics and gifs

  by [Archy Will He 魏何阿奇](https://twitter.com/archyisnotdead)

**> PROLOGUE **

> Among the things I managed to teach myself after dropping out of school at the age of 16 was calculus. Before I knew what calculus is, merely hearing its name gave me the impression that it is one of the most complicated things in maths, and that I could not possibly learn it by looking into the freely-available resources online.

>
>  I was wrong.
>

>  It turned out that back then I had a rather naive view of what mathematics is about. Understanding calculus is not hard at all. It is simply a matter of whether you have stumbled upon the right resources to learn it. If you have difficulty understanding it, you are probably learning it the wrong way.

>

>  I am nowhere near being an “expert” in calculus (or anything like that). I don’t really apply calculus to solve problems on a daily basis. To put it bluntly I am just a kid who writes about things he knew by heart so it may be used to help with those who are having a hard time learning it.

>
>  Archy,
>  Oct 2014

Calculus is just a fanciful name for the study of change in maths. Calculus in general refers to the branch of maths that was made famous by Newton in the 17th century. Don’t confuse it with [Lambda calculus](http://en.wikipedia.org/wiki/Lambda_calculus), [propositional calculus](http://en.wikipedia.org/wiki/Propositional_calculus), and [unicorns](http://www.amazon.com/gp/product/0385375557/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0385375557&linkCode=as2&tag=0aarhe-20&linkId=G75NU4TLDFAYKFK2), which are completely different things.

To understand calculus, one needs to be able to visualize the concepts of *function*, *limit*, *differentiation*, and *integration*.

● ● ●

### 1. What is a function?

A *function* can be seen as a machine that takes in value and gives you back another value. It is what we use in maths to map numbers (input) to other numbers (output).

![](../_resources/3e5133cd49e8ec4ce298a0124a38e738.png)
f(input)=outputf(input)=output
A function is normally defined by an equation like this:
f(x)=x+10f(x)=x+10
Now if you put 2 into this function you will get 12 in return.
f(2)=12f(2)=12

> The set of numbers that you can put into a function is known as the > [> domain](http://en.wikipedia.org/wiki/Domain_of_a_function)>  of the function. If you’d like to have a more in-depth understanding of function (e.g. its formal definition), check out > [> my article on set theory](http://0a.io/0a-explains-set-theory-and-axiomatic-systems-with-pics-and-gifs)> . (You will probably love it!)

### 2. What is a limit?

A *limit* is the number you are “expected” to get from a function (or algebraic expression) when it takes in a certain input. By “expected” it is referring to the expectation of the output when xx “approaches” a certain value.

Here is an example where the limit (the expected output) is the same as the actual output.

limx→25x25=1limx→25x25=1

The limit above is often read as “the limit of 5x255x25 as xx approaches 2 is 1”. You can visualize “xx approaches 2” as a dot moving along the graph towards where x=2x=2 (and, as you can see, y=1y=1).

![limit.gif](../_resources/0efd2a74a5ada90131944f21c1c24cf7.gif)
Now take this function for example:
f(x)=(x2−3x)2x−3f(x)=(x2−3x)2x−3

Division by 0 is undefined. We would get undefinedundefined when we put 3 into the function.

f(3)=(32−3⋅3)23−3=undefinedf(3)=(32−3⋅3)23−3=undefined
This is also why there is a hole in the graph of f(x)f(x).
![](../_resources/506cafb07e6021ab06a11b676722af51.png)

But looking at the graph, we can see that 0 is the expected value when xx approaches 3.

limx→3f(x)=0limx→3f(x)=0

To compute the limit when the actual output is undefined, in normal case we simply need to simplify the algebraic expression to avoid division by 0. And then put the value xx is approaching into the function as xx.

(x2−3x)2x−3=x4−6x3+9x2x−3=x2(x−3)2x−3=x2(x−3)(x2−3x)2x−3=x4−6x3+9x2x−3=x2(x−3)2x−3=x2(x−3)

limx→3(x2−3x)2x−3=limx→3x2(x−3)=32(3−3)=0limx→3(x2−3x)2x−3=limx→3x2(x−3)=32(3−3)=0

If you would like to learn more about limit, feel free to check out my essay [What do we talk about when we talk about limit](https://0a.io/chapter1/what-do-we-talk-about-when-we-talk-about-limit.html).

### 3. What is differentiation?

Differentiation is a fanciful name for the process of obtaining a *derivative*. And a derivative is a function that gives you the “slope” (or rate of change) of another function at a certain point.

Basically, differentiation can be seen as a machine that takes in a function and gives you back another function.

![](../_resources/26e0c044a7b57343c4557fcf907e3433.png)

We all know that the slope of a linear equation/function has a constant value. It has the same rate of change at every point on the line. So the graph of a linear equation/function is indeed a straight line.

![](../_resources/c12ec7c4588a0ee6a8ebc2768127694f.png)

For every value of 1 added to the input, a value of the slope (in this case, 4) would be added to the output.

![](../_resources/8d3e810cdeacec56c08ef20afe0fbb76.png)

The change between input and output is always in the ratio of 1 to mm, where mm is the value for the slope. Adding 0.1 to the input will trigger a change of +0.1m+0.1m in the output, etc.

f(5)f(6)f(5.1)f(5.02)=8=f(5)+1×4=12=f(5)+0.1×4=8.4=f(5)+0.02×4=8.08f(5)=8f(6)=f(5)+1×4=12f(5.1)=f(5)+0.1×4=8.4f(5.02)=f(5)+0.02×4=8.08

But this is only true for linear function. For functions that are not linear, every point doesn’t have a constant rate of change. Take a look at the function f(x)=2xf(x)=2x.

![](../_resources/31d14e870ad190b1c0a8079e8d0b873c.png)
f(3)f(4)f(5)f(6)f(7)=8=16=32=64=128f(3)=8f(4)=16f(5)=32f(6)=64f(7)=128
![](../_resources/115e0468bd9ef6c14b56ae6dbe70aa5f.png)

This is when we cannot use a constant to represent the “slope”: we need to use a function that gives us different “slope” (rate of change) at different point. Or rather, we shouldn’t even call it a “slope” anymore since the rate of change is not constant. We call it derivative.

If you are still trying to get your head around what it means by “the rate of change is not constant”, imagine a cat at rest starts to accelerate constantly at 1m/s21m/s2. Three seconds later it would be moving at the speed of 3m/s3m/s. So far the rate of change in its speed is constant. But when the cat begins to slow down, the rate of change would no longer be constant.

### 4. How to find the derivative of a function?

The rate of change at a certain point in the function can be visualized as a straight line across the point.

![](../_resources/800a05b1692ba67e30872a38f13733cb.png)

> This is normally called the > [> tangent line at a certain point](http://en.wikipedia.org/wiki/Tangent)> .

Since a non-linear function doesn’t have a constant rate of change, it means that every point of the function needs a different straight line to represent the rate of change.

![](../_resources/6ecb4a869a3725fefff8dc07dc99d1aa.png)

To find the derivative of a function is to find another function that will output a value at every point, which can be represented by a corresponding straight line.

> The rate of change at point > x> x>  is therefore sometimes also known as the derivative at point > x> x> .

To get the straight line that represents the derivative at a certain point, one way to do it is to first locate 2 different points on the graph and draw a line across them.

![](../_resources/42b789b4f1d11eaeed1fe2b67636ad65.png)

> Some people refer to this line as a > [> secant line](http://en.wikipedia.org/wiki/Secant_line)> .

This line represents a value. It represents the rate of change if the 2 points belong to a linear function.

![](../_resources/c713bc984ebc5cabc3761191ff8a9136.png)

But now this function is not linear. So this line is not accurate at all if we try to use it to represent the rate of change at any one of the 2 points.

Apparently, the closer the 2 points are, the more accurate the line is in representing the rate of change at any one point.

![](../_resources/02197bb6369a6e85be0ffd2a51ef150d.png)
![](../_resources/80e9a7e62c8e676b468e0b8ac77a4fff.png)

With that in mind, let’s start off with a line that cuts across 2 points (A and B), and shift the line accordingly as we shift B towards A along the graph. By the time B is at the same point as A, we would have a line that can accurately represent the rate of change at point A - we would have a line that represents the derivate of the function at point A.

![dot_closer.gif](../_resources/a6fb1502ebb8ed5c3468b92a75eaf6d0.gif)

By turning the process above into a function (denoted by f′(x)f′(x)), this function would be the derivative of the function of the graph (denoted by f(x)f(x)).

slopef′(x)=yB−yAxB−xA=limh→0f(x+h)−f(x)(x+h)−xslope=yB−yAxB−xAf′(x)=limh→0f(x+h)−f(x)(x+h)−x

Here we are denoting the coordinate of point B as (x+h,f(x+h))(x+h,f(x+h)). And what we are doing is obtaining a value for the straight line (the “slope”/derivative) at point A as we shift point B to A by making hh approach 0. So the coordinate becomes (x+0,f(x+0))(x+0,f(x+0)), which is the coordinate for point A.

![dot_closer2.gif](../_resources/95441f05830776ace29378336c9a985d.gif)
> This is the modern definition of derivative in terms of limit.

> Besides > f> ′> (> x> )> f> ′> (> x> )>   > [aka Lagrange’s notation]> , here is another common notation for differentiation:

> d> d> x> f> (> x> )> d> d> x> f> (> x> )

> [> Gottfried Wilhelm Leibniz](http://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz)> , a great German mathematician, came up with this notation in the 17th century when he was still alive. He came up with it by seeing > d> x> d> x>  as an > [> infinitesimal (infinitely small)](http://en.wikipedia.org/wiki/Infinitesimal)>  change in > x> x>  [the input of > f> (> x> )> f> (> x> )> ]. And the single > d> d>  at the numerator here is supposed to be merged with > f> (> x> )> f> (> x> )>  to indicate an infinitesimal change in > f> (> x> )> f> (> x> )>  [the output of > f> (> x> )> f> (> x> )> ]. > d> d> x> f> (> x> )> d> d> x> f> (> x> )>  is sometimes written as > d> y> d> x> d> y> d> x> , where > y> y>  stands for the output of > f> (> x> )> f> (> x> )> .

> This is actually a more > [> ancient](http://en.wikipedia.org/wiki/Criticism_of_non-standard_analysis)>  way of defining a derivative: a derivative tells you the rate of change of the output at an infinitesimal scale as the input changes. Therefore it is > d> y> d> y>  [or > d>  > f> (> x> )> d>  > f> (> x> )> ] divided by > d> x> d> x>  - an infinitesimal change in > f> (> x> )> f> (> x> )> , divided by an infinitesimal change in > x> x> . So we are defining derivative in terms of a fraction (> d> y> d> x> d> y> d> x> ) here, instead of a limit.

> We call this way of thinking about derivative > [> non-standard analysis](http://en.wikipedia.org/wiki/Non-standard_analysis)> .

Let’s say we want to get the derivative of x3x3. The straightforward way to do it is to compute the limit.

ddxx3=lima→0(x+a)3−x3(x+a)−x=lima→0a(3x2+a(3x+a))a=lima→03⋅x2+a(3x+a)=3⋅x2+0(3x+0)=3⋅x2ddxx3=lima→0(x+a)3−x3(x+a)−x=lima→0a(3x2+a(3x+a))a=lima→03⋅x2+a(3x+a)=3⋅x2+0(3x+0)=3⋅x2

But we can speed up the process by using shortcuts like this.
ddxxnddxx3=n(xn−1)=3(x3−1)=3⋅x2ddxxn=n(xn−1)ddxx3=3(x3−1)=3⋅x2
Here is a list of famous shortcuts for differentiation.
ddxc=0ddxc=0

 ddxcf(a)=cddxf(a)ddxcf(a)=cddxf(a)

 ddxx=1ddxx=1

 ddxcx=cddxcx=c

 “Power rule”
 ddxxn=nx(n−1)ddxxn=nx(n−1)

 “Sum rule”
 ddxf(x)+g(x)=f′(x)+g′(x)ddxf(x)+g(x)=f′(x)+g′(x)

 “Product rule”
 ddxf(x)⋅g(x)=f′(x)g(x)+g′(x)f(x)ddxf(x)⋅g(x)=f′(x)g(x)+g′(x)f(x)

 “Chain rule”
 ddxf(g(x))=f′(g(x))g′(x)ddxf(g(x))=f′(g(x))g′(x)

 “Quotient rule”
 ddxf(x)g(x)=f′(x)g(x)−g′(x)f(x)g(x)2ddxf(x)g(x)=f′(x)g(x)−g′(x)f(x)g(x)2

 ddx1x=−f′(x)x2ddx1x=−f′(x)x2
ddxc1ax=c1axln(c1)addxc1ax=c1axln(c1)a

 ddxex=exln(e)=exddxex=exln(e)=ex

 ddxxx=xx(1+ln(x))ddxxx=xx(1+ln(x))

 ddxlogc(x2)=1x2lncddxlogc⁡(x2)=1x2ln⁡c

 ddxln(x1)=1x1ddxln(x1)=1x1

 ddxln(|x|)=1xddxln(|x|)=1x

 ddxsin(x)=cos(x)ddxsin(x)=cos(x)

 ddxcos(x)=−sin(x)ddxcos(x)=−sin(x)

 ddxtan(x)=−sec2(x)ddxtan(x)=−sec2(x)

 ddxsec(x)=sec(x)tan(x)ddxsec(x)=sec(x)tan(x)

 ddxcsc(x)=−csc(x)cot(x)ddxcsc(x)=−csc(x)cot(x)

 ddxcot(x)=−csc2(x)ddxcot(x)=−csc2(x)

 cc is a constant. c1c1 is a constant >0>0.
 nn is an integer.
 x1x1 is a variable >0>0.
 x2x2 is a variable >0>0 but ≠1≠1.

These shortcuts can all be derived from the limit of f(x+h)−f(x)(x+h)−xf(x+h)−f(x)(x+h)−x above. They are sometimes referred to as [“differentiation rules”](http://en.wikipedia.org/wiki/Differentiation_rules). Calling them “rules” certainly makes them sound like some fundamental principles in calculus, but the truth is they are merely shortcuts to speed things up.

● ● ●

### 5. Introducing anti-differentiation

I shall now introduce a new concept called *anti-differentiation*. It is just the inverse of differentiation. It can be seen as a machine that takes in a function, g(x)g(x), and give you back another function, f(x)f(x), whose derivative is g(x)g(x). Here, g(x)g(x) is known as the *anti-derivative* of f(x)f(x).

![](../_resources/d9ebd70f6b153f6be4f07a6ae1d1eda0.png)

Apparently, we will get the same derivative when differentiating functions that are only different at the part where it adds (or subtracts) a constant.

ddxx2+100ddxx2+49ddxx2=2x=2x=2xddxx2+100=2xddxx2+49=2xddxx2=2x

As shown above, we can see that no matter what the constant is, it would always give us back the same function if we differentiate it. So, in order to be technically correct, we would need to put a placeholder, +C+C, in the end of the function to indicate that the anti-derivative can be any function that plus some constant (or minus some constant for cases when CC is negative).

f(x)ddxg(x)g(x)=2x=f(x)=x2+Cf(x)=2xddxg(x)=f(x)g(x)=x2+C

### 6. What is integration?

Integration is a fanciful name for the process of finding *integral*. Integral here is referring to either *indefinite integral*, or *definite integral*. (Therefore sometimes we say indefinite integration or definite integration just to be specific.)

*Indefinite integral* is fundamentally equivalent to anti-derivative. They are basically the same thing.

![](../_resources/913e8e1d1416c339a5cfc8c8a7538a8c.png)
ddxf(x)+C=g(x)∫g(x) dx=f(x)+Cddxf(x)+C=g(x)∫g(x) dx=f(x)+C

> This is shown in the > [>  first fundamental theorem of calculus](http://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus)> .

> The > d> x> d> x>  in the equation indicates that > x> x>  is the input we are integrating > g> (> x> )> g> (> x> )>  with respect to. A function can take in more than one input [e.g. > f> (> x> ,> q> )> => x> 2> +> q> 3> f> (> x> ,> q> )> => x> 2> +> q> 3> ] so there are times when it is crucial to specify which input we are integrating the function with respect to [e.g. Is it > x> x>  or > q> q> ? Integrating the function with respect to a different input would give us a different result].

*Definite integral* can be defined as the difference between 2 identical anti-derivatives that take in different inputs.

∫bag(x) dx=f(b)−f(a)∫abg(x) dx=f(b)−f(a)
This is often read as “the definite integral of g(x) from a to b”.

> This definition of definite integral is derived from the > [>  second fundamental theorem of calculus](http://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus)> .

> a> a>  here is sometimes referred to as the lower limit, while > b> b>  is referred to as the upper limit.

Here is another way to define what a definite integral is. Imagine you want to find out the area of the region under a curve in a graph.

![](../_resources/dd1e7eb9ceaa64a31ca07ee95ae21995.png)
![](../_resources/6b8e02a160a45e72472a15abad70dd71.png)

You can approximate the area of the region by drawing rectangles under the curve and adding the area of these rectangles together. The smaller the width of the rectangle is, the more rectangle there would be, and the more accurate the approximation would be.

![](../_resources/551bf1bda5b113616bf1aec600e2cf23.png)
![](../_resources/76b44cd2426f15ecfea0e9db3f7674fb.png)

This can actually be written into a summation. Here nn is the number of rectangles.

∑i=1n(b−an)⋅g(a+b−ani)∑i=1n(b−an)⋅g(a+b−ani)

> This is known as the > [> Riemann sum](http://mathworld.wolfram.com/RiemannSum.html)> . > b> −> a> n> b> −> a> n>  is the width of each rectangle, and > g> (> a> +> b> −> a> n> i> )> g> (> a> +> b> −> a> n> i> )>  is the height.

We would be able to find the actual value for the area if we get the limit as nn, the number of rectangle, goes to *infinity*. Infinity here can be imagined as a theoretically enormous number that is bigger than every real number on the [number line](http://en.wikipedia.org/wiki/Number_line). This limit is another way of defining *definite integral*.

![ri.gif](../_resources/e303b005957bed706bb90a1a32fc3b30.gif)
∫bag(x) dx=limn→∞∑i=1n(b−an)⋅g(a+b−ani)∫abg(x) dx=limn→∞∑i=1n(b−an)⋅g(a+b−ani)

> Integral defined in this way is often known as > [> Riemann integral](http://en.wikipedia.org/wiki/Riemann_integral)> . When the limit exists, we say the function is Riemann-integrable. When a function is not Riemann-integrable, it doesn’t mean it is completely not integrable. It really just depends on how we define “integral”. In a branch of maths known as > [> real analysis](http://en.wikipedia.org/wiki/Real_analysis)> , integration is normally defined > [> in the Lebesgue’s way](http://en.wikipedia.org/wiki/Lebesgue_integration)> , different from the Riemann’s way above. Functions that can be integrated in the Lebesgue’s way are Lebesgue-integrable. One typical example for a function that is not Riemann-integrable but Lebesgue-integrable is the > [> nowhere continuous function](http://en.wikipedia.org/wiki/Nowhere_continuous_function)> .

In the limit above, we are getting the area of region underneath the graph of g(x)g(x) from AA to BB. And this is actually equivalent to “stacking up” the rate of changes of its anti-derivative, f(x)f(x), at every point from AA to BB. Therefore we are actually getting the difference between f(a)f(a) and f(b)f(b). This is why definite integral of g(x)g(x) is able to give us the area from point AA to BB in the graph of g(x)g(x): definite integral is giving us the overall change in value from f(a)f(a) to f(b)f(b).

![](../_resources/1bc6a49d38fa99aa2e7194ab437694fa.png)
![](../_resources/e6e5100415da7414e9978a177c13796e.png)
![](../_resources/0e6aa98a6d75888290f4ed69887b66d5.png)

> This is precisely why > d> x> d> x>  is there as a part of the integral notation > ∫> f> (> x> )>  > d> x> ∫> f> (> x> )>  > d> x> . In the logic that differentiation is defined as > d> f> (> x> )> d> x> => g> (> x> )> d> f> (> x> )> d> x> => g> (> x> )> , we can see that > g> (> x> )>  > d> x> => d> f> (> x> )> g> (> x> )>  > d> x> => d> f> (> x> )> , where > d> d>  is an infinitesimal change interpreted as > 1> ∞> 1> ∞> . The relation of every > x> x>  and > y> y>  in the function > f> (> x> )> f> (> x> )>  [how > x> x>  changes affects > y> y>  changes, vice versa] can therefore be constructed by indeterminately> 1>  summing up> 2>  the infinite number of infinitesimal “slices” of its derivative > g> (> x> )> g> (> x> )> , with each infinitesimal “slice” being a nonspecific> 3>   > y> y> 4>  multiplied by an infinitesimal change in > x> x> , > d> x> d> x> , that governs the value of the corresponding > y> y> .

>  indeterminately> 1> : this is why it is called *> indefinite*>  integration. We are getting a result in terms of a variable, rather than getting an actual value. summing up> 2> : this is what > ∫> ∫>  indicates in the notation. nonspecific> 3> : thus it is *> indefinite*>  integration. What matters is the relation in terms of > x> x> , not the actual value. > y> y> 4> : this > y> y>  is the > y> y>  from > g> (> x> )> g> (> x> )> .

### 7. How to find the definite integral of a function from aa to bb?

Computing the limit of a Riemann sum can really be a tedious thing to do. So what we normally do is to find the indefinite integral first before putting aa and bb into the indefinite integral and getting the difference between them (using the definition of definite integral from the 2nd fundamental theorem of calculus mentioned above).

g(x)=x4∫g(x) dx=x55+C∫32g(x) dx=355−255=42.2g(x)=x4∫g(x) dx=x55+C∫23g(x) dx=355−255=42.2

Of course, it is [not always necessary to get the indefinite integral first (it is possible to arrive at an answer after some transformations of the definite integral)](http://math.stackexchange.com/q/710175/65082).

### 8. How to find the indefinite integral (anti-derivative) of a function?

Apparently, we can reverse the differentiation shortcuts/rules above and turn them into integration shortcuts/rules. But sometimes a little bit of creativity is required for integration. Let’s take a look at the reverse-[chain-rule](http://en.wikipedia.org/wiki/Chain_rule).

f′(g(x))g′(x)=ddxf(g(x))f′(g(x))g′(x)=ddxf(g(x))

Things don’t always come in a perfect bundle. To use reverse-chain-rule, most of the time we need to see the algebraic structure as f′(g(x))f′(g(x)) and compute g′(x)g′(x) on our own.

f′(g(x))=1g′(x)⋅ddxf(g(x))f′(g(x))=1g′(x)⋅ddxf(g(x))
Here is an example. Let’s say we need to solve this indefinite integral.
∫3(2x+1)2dx∫3(2x+1)2dx
We can see f′(x)f′(x) as 3x23x2 and g(x)g(x) as 2x+12x+1.
∫3(2x+1)2dx=∫f′(g(x))dx∫3(2x+1)2dx=∫f′(g(x))dx

What we need to do now is to obtain f(x)f(x) by integrating f′(x)f′(x), and obtain g′(x)g′(x) by differentiating g(x)g(x).

f(x)=∫f′(x) dx=∫3x2 dx=−3xf(x)=∫f′(x) dx=∫3x2 dx=−3x
g′(x)=ddxg(x)=ddx2x+1=2g′(x)=ddxg(x)=ddx2x+1=2
∫3(2x+1)2dx=1g′(x)⋅f′(g(x))=12⋅−32x+1+C∫3(2x+1)2dx=1g′(x)⋅f′(g(x))=12⋅−32x+1+C

So if we need to solve the definite integral ∫103(2x+1)2dx∫013(2x+1)2dx, we just put the two values into the indefinite integral and get the difference like this:

∫ba3(2x+1)2 dx∫103(2x+1)2 dx=12⋅(−32⋅b+2−−32⋅a+2)=12⋅(−32⋅1+2−−32⋅0+2)=12⋅2=1∫ab3(2x+1)2 dx=12⋅(−32⋅b+2−−32⋅a+2)∫013(2x+1)2 dx=12⋅(−32⋅1+2−−32⋅0+2)=12⋅2=1

> This technique (reversing chain rule) is known as > [> integration by substitution](http://en.wikipedia.org/wiki/Integration_by_substitution)> , or, > u> u> -substitution, where > g> (> x> )> g> (> x> )>  is often written as > u> u> .

> The truth is: finding an indefinite integral can be really hard sometimes. Aside from the fact that there isn’t an “absolute” way of humanly doing it, there is actually a rigorous mathematical reason behind it. The set of functions we humans love to do differentiation on is normally closed under differentiation. This means if we differentiate a function, we should anticipate to get back a similar function (e.g. differentiating an > [> elementary function](http://en.wikipedia.org/wiki/Elementary_function)>  gives us back an elementary function). But it is not the case for integration. It is possible to integrate an elementary function, and get a non-elementary function in return (e.g > ∫> e> x> 2> d> x> ∫> e> x> 2> d> x>  ). And as we can see, definite integration is more of a local operation, while indefinite integration is a global operation. This is why sometimes it makes more sense to solve a definite integral using transformations and techniques, arriving at the answer without having to compute the indefinite integral. There are respected individuals (e.g. > [> Vladimir Reshetnikov](http://math.stackexchange.com/users/19661/vladimir-reshetnikov)> , > [> Cleo](http://math.stackexchange.com/users/97378/cleo)>  on Maths StackExchange) who are amazingly good at it.

● ● ●

### 9. Bonus: Partial derivative

When a function has more than one input value, we call it a multivariable function.

f(x1,x2)=3x1+x2f(x1,x2)=3x1+x2

> The graphs of functions that take in 1 input are lines in a 2D plane, while the graphs of functions that take in 2 inputs are surfaces in a 3D space, etc.

To differentiate functions like this, we find the derivative with respect to one of the variables (denoted by xixi in this case). This type of derivative is known as a partial derivative.

∂∂xif(x1,x2..xi..xn)∂∂xif(x1,x2..xi..xn)

Finding a partial derivative is very similar to finding a normal derivative: we get the limit as x approaches 0. But instead of having just f(x+a)−f(x)f(x+a)−f(x), we have f(x1,x2..xi+a..xn)−f(x1,x2..xi..xn)f(x1,x2..xi+a..xn)−f(x1,x2..xi..xn), since the function takes in more than one input.

   ∂∂xif(x1,x2..xi..xn)=lima→0f(x1,x2..xi+a..xn)−f(x1,x2..xi..xn)(xi+a)−xi   ∂∂xif(x1,x2..xi..xn)=lima→0f(x1,x2..xi+a..xn)−f(x1,x2..xi..xn)(xi+a)−xi

To do a partial differentiation, we simply pretend that other variables in the function are constants as we differentiate the function with respect to the chosen input. Here is an example.

f(x,a,b,c)∂∂xf(x,a,b,c)=x5+2ax+10b9+loga(c)=∂∂x(x5+2ax+10C9+logC(C))=∂∂x(x5+2Cx+C)=5x4+2C=5x4+2af(x,a,b,c)=x5+2ax+10b9+loga(c)∂∂xf(x,a,b,c)=∂∂x(x5+2ax+10C9+logC(C))=∂∂x(x5+2Cx+C)=5x4+2C=5x4+2a

added on 29th Oct, at 5PM (SG Timezone, +8): [edited a couple of times around 8 30PM to express the idea of tangent space in a more clear and concise way. And corrected some mistakes I made in the analogy of tangent plane.]  Upon differentiating the function, we need to replace the remaining CC back with the corresponding variables.

g(x,a,b,c)=∂∂xf(x,a,b,c)=5x4+2C=5x4+2ag(x,a,b,c)=∂∂xf(x,a,b,c)=5x4+2C=5x4+2a

Basically, ∂∂xf(x,a,b,c)∂∂xf(x,a,b,c) tells you about how an infinitesimal change in the input xx would affect the output f(x,a,b,c)f(x,a,b,c) when aa, bb and cc remains unchangeable. To get the numerical value for the derivative, it is sometimes necessary to put an actual value into these variables.

g(1,2,0,0)g(1,3,0,0)=629=631g(1,2,0,0)=629g(1,3,0,0)=631

The derivative of functions with 1 input at one point (x,f(x)x,f(x)) can be represented by a [tangent lines](http://mathworld.wolfram.com/TangentLine.html) when xx is specified. Meanwhile, the representation for the derivative of functions with 2 inputs at points(x1,x2,f(x1,x2)x1,x2,f(x1,x2)) where x1x1 is specified is a plane ([tangent plane](http://mathworld.wolfram.com/TangentPlane.html)), for functions with 3 input it is a [3D space](http://en.wikipedia.org/wiki/Three-dimensional_space) (3D [tangent space](http://en.wikipedia.org/wiki/Tangent_space)), etc.

> In normal differentiation (single-input functions). To obtain a numerical value for the rate of change at a certain point is to obtain the slope of the tangent line at that point: there is only 1 slope because there is only one single line going across one single > [> point](http://en.wikipedia.org/wiki/Point_(geometry))> , > (> x> ,> f> (> x> )> )> (> x> ,> f> (> x> )> )> . To do it we just need to specify > x> x>  since > f> (> x> )> f> (> x> )>  is only dependent on > x> x> .

> The graph of a two-variable function is a 2 dimensional surface in 3 dimensional space, so each point can be represented by > (> x> 1> ,> x> 2> ,> f> (> x> 1> ,> x> 2> )> )> (> x> 1> ,> x> 2> ,> f> (> x> 1> ,> x> 2> )> )> , where the value of > f> (> x> 1> ,> x> 2> )> f> (> x> 1> ,> x> 2> )>  is dependent to both > x> 1> x> 1>  and > x> 2> x> 2> .

> The derivative with respect to any one of the variable (e.g. > x> 1> x> 1> ) when the variable (this case, > x> 1> x> 1> ) is specific is a value dependent to > f> (> x> 1> ,> x> 2> )> f> (> x> 1> ,> x> 2> )>  and > x> 2> x> 2> . So it is no longer a tangent line across one point, but a tangent plane across infinitely many points whose > x> 1> => the specific value> x> 1> => the specific value> . This is why, if we want to get an actual numerical value for the slope, we need to specify > x> 2> x> 2> .

> The same applies to tangent of higher dimensions.

If you are interested in learning more about calculus, check out [Calculus One](https://www.coursera.org/learn/calculus1) by [Jim Fowler](https://www.coursera.org/instructor/jimfowler) on [Coursera](http://coursera.com/). It is truly amazing for beginners. For courses that cover more advanced topics in calculus and other areas of maths that use calculus, check out the ones by [MIT OpenCourseWare](http://ocw.mit.edu/index.htm). You’d probably find [Pauls Online Notes](http://tutorial.math.lamar.edu/Classes/CalcI/CalcI.aspx) useful too.

##

 ![irina-568205-unsplash.jpg](../_resources/a80aa8845954d1fa4891fe68a2eb57d3.jpg)

#

###  0a.io: handcrafted by [Archy](https://0a.io/about.html)

 [vi3w_s0urce **](https://github.com/archywillhe/0a.io)

###  _