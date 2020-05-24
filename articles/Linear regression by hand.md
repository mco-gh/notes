Linear regression by hand

# Linear regression by hand

> … most companies would be taking a huge step forward if they got somebody who knows how to do linear regression.

> — > [> Hacker News user ‘mindcrime’ on the necessary skills for data science](https://news.ycombinator.com/item?id=14772549)

When you have ![x_1, \ldots, x_k](../_resources/6093f8930bc5f1f2e4dfc3bf8c5ec0fd.png) predictors of a scalar-valued outcome ![y](../_resources/ecc7003d239697bbcf91725e6ffe8fbe.png) with observations indexed by ![i](../_resources/305c5048c128cac0066f3b008bfc2dbb.png) and residuals denoted ![\varepsilon](../_resources/646878713b59605f0ca75d8ec91216a2.png), a model of the form

![y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_k x_{ik} + \varepsilon_i](../_resources/319a44b69a11cf3b52793d71e279b755.png)

or (equivalently) in matrix notation

![\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}](../_resources/2deadc03f04a07ea78d17b84428d2962.png)

is best[1] estimated using [ordinary least squares](https://en.wikipedia.org/wiki/Ordinary_least_squares), the workhorse of linear regression. The underlying math is a fair bit of matrix algebra which, when all is said and done, returns

![\boldsymbol{\hat{\beta}} = \left(\mathbf{X^\prime X}ight)^{-1} \mathbf{X^\prime y}.](../_resources/3e2ad8ed3facf558d92475a5cebcfb36.png)

**This was the one equation my graduate school program director urged every student to know by heart.**

*X prime X inverse X prime y*, “prime” meaning [transpose](http://mathworld.wolfram.com/Transpose.html), yields OLS estimates of linear regression coefficients. On the left-hand side, the hat symbol denotes an estimate from a sample as opposed to a true value in the population.

We can walk through a real-data example using `mtcars`, an automobile-themed dataset built into R. Regressing fuel economy (mpg) on weight (wt) and number of cylinders (cyl),

![\text{mpg}_i = \beta_0 + \beta_1 \text{wt}_i + \beta_2 \text{cyl}_i + \varepsilon_i,](../_resources/afbcaa6c681d4166c0c6acf153b123d1.png)

by
1
[object Object][object Object][object Object][object Object]
will give you

Estimate Std. Error t value Pr(>|t|) (Intercept) 39.6863 1.7150 23.141 < 2e-16 ***

wt -3.1910 0.7569 -4.216 0.000222 ***
cyl -1.5078 0.4147 -3.636 0.001064 **

wherein the estimates (first column of numbers) from top to bottom correspond to

![\boldsymbol{\hat{\beta}} = \begin{bmatrix} \hat{\beta_0} \\  \hat{\beta_1} \\  \hat{\beta_2} \end{bmatrix}.](../_resources/53bde3d26681c66fb97f0a0fa70dd916.png)

Per the foregoing all-important equation, only two objects are necessary to compute the estimates manually: (1) the matrix ![\mathbf{X}](../_resources/8d70960ca5e6e38556ed93bc3f5efcd1.png) and (2) the vector ![\mathbf{y}](../_resources/93382cbe69d0873b2aba87ba636133e1.png). Both are easy to extract from `mtcars`.

1
2
3
4
5
6
7
8
9
10
11
[object Object]
[object Object][object Object][object Object]
[object Object]
[object Object]
[object Object]

[object Object][object Object][object Object][object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object]
[object Object]
[object Object][object Object][object Object]

Given [\mathbf{X}](../_resources/8d70960ca5e6e38556ed93bc3f5efcd1.png) and , all that’s left are matrix operations. Mathematically they are described in [this tutorial from Harvey Mudd College](https://www.math.hmc.edu/calculus/tutorials/matrixalgebra/). Computationally, `t()` transposes, `solve()` inverts, and `%*%` multiplies matrices.

Now for the moment of truth—*X prime X inverse X prime y*.
1

[object Object][object Object][object Object][object Object][object Object][object Object]

[,1]
1 39.686261
wt -3.190972
cyl -1.507795

This formula doesn’t get us *p*-values [but who needs those anyway](https://www.nature.com/news/psychology-journal-bans-p-values-1.17001).

* * *

[1] OLS is BLUE—the [best linear unbiased estimator](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem)—under certain assumptions that are very important but beyond the scope of this post.