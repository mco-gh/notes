Programmer's guide to polynomials and splines

# Programmer's guide to polynomials and splines

So you are a programmer. Why would you want to know about polynomials? One reason would be that this is the geometrical clay we can easily make different things of.

[Mathematical analysis explained with Python, blood, and TNT](http://wordsandbuttons.online/mathematical_analysis_explained_with_python_blood_and_tnt.html) shows how you can analyze and synthesize arbitrary functions as polynomials. But it doesn't even have to be functions. Sometimes you would want to model a spline out of some points or some properties like tangents of curvatures. Like when you want to do some animation; or nice video effect; or draw a curve that goes through the points you want; or build a surface that is flat in one place and curvy in another.

Polynomials or even polynomial splines might not *always* be the best tool for the job, but they possess some traits that programmers value. They are inherently simple, versatile, and, most noticeably, highly effective in terms of performance.

Let's say we have a polynomial like that:

P(x) = ax3 + bx2 + cx + d

It only takes 6 multiplications and 3 additions to calculate, and this is important because your model is meant to be calculated a lot. But even this can be reduced by using Horner's method. The same polynomial may be written as:

P(x) = ((ax+ b)x + c)x + d

And that's only 3 multiplications and 3 additions. See, we barely started, and you already learned how to throw away one-third of computation effort.

## Polynomial interpolation

Fitting an *n-*degree polynomial in exactly *n+1* points is called polynomial interpolation. There are several ways to do that. You can use [Newton polynomials](https://en.wikipedia.org/wiki/Newton_polynomial) or [Lagrange polynomials](https://en.wikipedia.org/wiki/Lagrange_polynomial). But the very basic way you can get an interpolating polynomial is by solving a linear system.

If a polynomial *P(x)* goes through the point *(xi, yi)* then, obviously enough, we can claim that *P(xi) = yi*. Say we want to fit a polynomial into a set of three points. This means that:

P(x1) = y1
P(x2) = y2
P(x3) = y3

Generally, we can not fit a straight line into three arbitrary points. We would have to bend it forming a parabola. Or, put in other words, 2-nd degree polynomial also known as quadric.

P(x1) = ax12 + bx1 + c = y1
P(x2) = ax22 + bx2 + c = y2
P(x3) = ax32 + bx3 + c = y3

Since we know *x*s and *y*s, we only have to solve the system for *(a, b, c)* coefficients and since it's a three-equation system with three variables, it should generally give us one and only one solution.

Here, try it yourself. This is the canvas with three points on. Please drag them to see what happens.

|     |     |
| --- | --- |
| **P(x) = ax2 + bx + c** | P(x1) = 1.002a + 1.00 b + c = 5.00<br>P(x2) = 4.502a + 4.50 b + c = 1.42<br>P(x3) = 5.982a + 5.98 b + c = 1.93 |
| a = 0.28, b = -2.54, c = 7.26<br>P(x) = 0.28x2 + -2.54x + 7.26 |

This is also a good mental model for understanding linear systems. Generally, you can't fit a straight line into three points just like you can't find a solution for *(n-1)* variables for n-equations system. But sometimes you can. It's when some of the points coincide or they all deliberately lie on a straight line.

And the vise versa it's even more exciting. We can fit an infinite number of parabolas into a set of only two points. We just can't choose between them, that's why we can't unambiguously solve an n-equations system for *(n+1)* variables.

But what if we can? What if we can introduce some additional criteria to choose the best fit?

## Synthesis

And this brings us to the domain of polynomial synthesis. In our case, it is something between polynomial series and polynomial interpolation. With polynomial series, we can model a function based on its derivatives at some point, and with synthesis, we can use both points and derivatives. And even more than that actually, but that's a whole different story.

Function's derivative is closely related to geometric properties of its plot. The first derivative sets a tangent, and the second one sets a curvature.

Let than say we want a function that goes through a pair of points and has a specific tangent in both points. We can easily synthesize this function as a polynomial.

Just like before, we would have to set a system of equations. Now we want four conditions, so we should pick a 3-rd degree polynomial — a cubic.

P(x1)' = 3ax12 + 2bx1 + c = dy1/dx
P(x1) = ax13 + bx12 + cx1 + d = y1
P(x2) = ax23 + bx22 + cx2 + d = y2
P(x2)' = 3ax22 + 2bx2 + c = dy2/dx

Some of the equations are formed from points and some from derivatives. You could also add integrals if you wanted to constraint some integral properties so this is a rather powerful technique.

But anyway this gives us something to form a smooth continuous function between two points with tangential constraints at these points. For now, let's stick to that.

|     |     |
| --- | --- |
| **P(x) = ax3 + bx2 + cx + d** | P(x1)' = 3.0a + 2.0b + 1.0c = -0.7<br>P(x1) = 1.0a + 1.0b + 1.0c 1.0d = 1.0<br>P(x2) = 190.1a + 33.1b + 5.8c 1.0d = 4.4<br>P(x2)' = 99.2a + 11.5b + 1.0c = 0.2 |
| a = -0.08, b = 0.93, c = -2.28, d = 2.43<br>P(x) = -0.08x3 + 0.93x2 + -2.28x + 2.43 |

Now you have a function with desirable properties between two points. But what if you have to fit a polynomial into many more points?

## Runge's phenomenon

One unpleasant property of polynomial interpolation is that the function tends to oscillate at both ends of the interval more and more with adding more points. This is called the Runge's phenomenon. It limits the use cases where simple polynomial interpolation is appropriate.

The other limitation is that interpolating polynomial is global, meaning that touching a single point causes all the function to change. Now combine this with the oscillations, and you have yourself a recipe for chaos.

## Chebyshev nodes

One way to mitigate this chaos would be to select a special grid for an interpolation: [Chebyshev nodes](https://en.wikipedia.org/wiki/Chebyshev_nodes). These are specially calculated *x* values that represent a projection of equidistant intervals from a semicircle with radius 1 onto the x-axis.

There is some interesting mathematical magic behind this, but pragmatically this disposition minimizes the Runge's phenomenon. Not that it makes interpolation completely predictable, but in the range *(-1; 1)* it now works more or less stable.

Of course, you can translate this range to any other range on x-axis using 1-dimensional affine transformation. It doesn't have to be always *(-1; 1)*.

But the interpolation is still global. The change in the first point still affects the function near the last one, although not so drastically.

## Splines

There are quite a lot of different types of splines, but they all share the common motivation. When, for some reason, global interpolation doesn't work for us, we can divide our interval into smaller ones, and we can then define separate interpolating functions for each of them. We only have to make sure they conjoin in their ends to provide continuity. If we guarantee continuity not only for our resulting piecewise function but for its first derivative as well, then the tangents of every piece would match, and the function's plot will seem smooth.

There is a definite classification for [the types of splines](https://en.wikipedia.org/wiki/Spline_(mathematics)#Representations_and_Names). For instance, here is a 2-piece polynomial spline. It is **cubic**, meaning that the polynomial in every piece is of third degree. It has **1-st derivative continuity**, since we make the pieces conjoint along with their tangents. It is **non-uniform**, since the length of the pieces' intervals is variable. It is **not natural**, since you can rule the derivatives at the end. And it is, of course, an **interpolating** spline since it goes exactly through the grid points we set up.

## Conclusion

It is highly unlikely that you would ever have to implement your own interpolation. There are a lot of ready-made solutions out there, most of the time you would only have to pick a right tool for the job. It's not all that hard, but the amount of unknown words and names may be overwhelming.

The purpose of this guide is to give you the very basic understanding of the ideas behind polynomials and splines. It is not at all comprehensive, in fact, there are whole books being written on every small chapter of this guide, so it's simply impossible to put it all in one small article. I hope, however, that the interactive experience from this piece will be helpful not only for the brief acknowledgment but, if necessary, will contribute to the understanding of some more advanced topics.

There are more words and buttons such as this on [wordsandbuttons.online](http://wordsandbuttons.online/index.html).

![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[4 min to Spreed]()