On the Link Between Polynomials and Optimization

#   [On the Link Between Polynomials and Optimization](http://fa.bianp.net/blog/2020/polyopt/)

Part I: Residual Polynomials and the Chebyshev method.

By Fabian Pedregosa.

Category: [optimization](http://fa.bianp.net/category/optimization.html)

#[polynomials](http://fa.bianp.net/tag/polynomials.html) #[acceleration](http://fa.bianp.net/tag/acceleration.html)

Tue 07 April 2020

There's a fascinating link between minimization of quadratic functions and polynomials. A link that goes deep and allows to phrase optimization problems in the language of polynomials and vice versa. Using this connection, we can tap into centuries of research in the theory of polynomials and shed new light on old problems.

**Outline:**
[1. Introduction](http://fa.bianp.net/blog/2020/polyopt/#sec1)

[2. From Optimization to Polynomials](http://fa.bianp.net/blog/2020/polyopt/#sec2)

[3. Optimal Residual Polynomial](http://fa.bianp.net/blog/2020/polyopt/#sec3)

[4. The Chebyshev iterative method](http://fa.bianp.net/blog/2020/polyopt/#sec4)

[5. Convergence rate](http://fa.bianp.net/blog/2020/polyopt/#sec5)
[6. Conclusion](http://fa.bianp.net/blog/2020/polyopt/#sec6)
[7. References](http://fa.bianp.net/blog/2020/polyopt/#sec7)

## 1. Introduction

This post deals with a connection between optimization algorithms and polynomials. Our motivation is the problem of finding a vector x⋆∈Rd that minimizes the convex quadratic objective

f(x)=def12x⊤Hx+b⊤x ,(1)

where H is a positive definite square matrix.1 11 The quadratic assumption is made for the purpose of the analysis. All the discussed algorithms are applicable to any smooth (not necessarily quadratic) function. 1

A popular class of algorithms for this problem are *gradient-based methods*. These are methods in which the next iterate is a linear combination of the previous iterate and past gradients. In the next section we will see how we can identify any gradient-based method with a polynomial that determines the method's convergence speed. And vice-versa, we will see in section 3 that it's possible to do the inverse path and go from a (subset of) polynomials to optimization methods. Then we will use this connection to derive the Chebyshev iterative method, which forms the basis of some of the most used optimization methods such as Polyak momentum, which will be the topic of the second part of the next blog post.

### Pioneers of Scientific Computing

The ideas outlined in this post can be traced back to the early years of numerical analysis. Minimizing quadratic objective functions (or equivalently solving linear systems of equations) was one of the first applications of scientific computing, and while some methods like gradient descent (Cauchy, 1847)2 22 Cauchy, Augustin (1847) [“Méthode générale pour la résolution des systèmes d'équations simultanées”](https://gallica.bnf.fr/ark:/12148/bpt6k90190w/f406). *Comp. Rend. Sci. Paris*.2   3 33 Lemaréchal, Claude (2012) [“Cauchy and the gradient method”](https://www.math.uni-bielefeld.de/documenta/vol-ismp/40_lemarechal-claude.pdf). *Doc Math Extra*.3  and [Gauss-Seidel](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method#cite_note-1) predate the development of electronic computers, their algorithmic analysis as we know it today emerged during the 1940s and 1950s.

One of the first applications of the theory of polynomials to the solution of linear systems is development of the Chebyshev iterative method, developed independently by Flanders and Shortley, 4 44 Flanders, Donald A and Shortley, George (1950) [“Numerical determination of fundamental modes”](https://sci-hub.tw/10.1063/1.1699598). *Journal of Applied Physics*.4  Cornelius Lanczos,5 55 Lanczos, Cornelius (1952) [“Solution of systems of linear equations by minimized iterations”](https://nvlpubs.nist.gov/nistpubs/jres/049/1/V49.N01.A06.pdf). *J. Res. Nat. Bur. Standards*.5  and David Young6 66 Young, David (1953) [“On Richardson's method for solving linear systems with positive definite matrices”](https://doi.org/10.1002/sapm1953321243). *Journal of Mathematics and Physics*.6 , and further analyzed and popularized by Richard Varga7 77 Varga, Richard S (1957) [“A comparison of the successive overrelaxation method and semi-iterative methods using Chebyshev polynomials”](https://doi.org/10.1137/0105004). *Journal of the Society for Industrial and Applied Mathematics*.7  and Gene Golub.8 88 Golub, Gene H and Varga, Richard S (1961) [“Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods”](https://doi.org/10.1007/BF01386013). *Numerische Mathematik*.8  Shortly after the development of the Chebyshev iterative method, the field saw one of the most beautiful applications of the theory of orthogonal polynomials in numerical analysis, the conjugate gradient method.9 99 Hestenes, Magnus R and Stiefel, Eduard (1952) [“Methods of conjugate gradients for solving linear systems”](https://pdfs.semanticscholar.org/466d/addfb6340c28cb8da548007028c8cc5df687.pdf). *Journal of research of the National Bureau of Standards*.9

An excellent review on the topic is the 1959 book chapter “Theory of Gradient Methods” by H. Rutishauser,10 1010 Rutishauser, H. (1959) [“Theory of Gradient Methods”](https://doi.org/10.1007/978-3-0348-7224-9_2). *Refined Iterative Methods for Computation of the Solution and the Eigenvalues of Self-Adjoint Boundary Value Problems*.10   11 1111 ![](../_resources/bc4a9f2da4bd2463359eafd5e2e0cadd.png)

 [Heinz Rutishauser](https://en.wikipedia.org/wiki/Heinz_Rutishauser) (1918–1970). Among other contributions, he introduced a number of basic syntactic features to programming, notably the keyword "for" for a for loop, first as the German "für" in Superplan, next via its English translation "for" in ALGOL 58A. 11  which has stood remarkably well the test of time. For a more modern review, see the 1996 book by Bernd Fisher.12 1212 Fischer, Bernd (1996) [“Polynomial based iteration methods for symmetric linear systems”](https://doi.org/10.1007/978-3-663-11108-5). *Springer*.12

These ideas are still relevant today. Just in the last year, these tools have been used for example to develop accelerated decentralized algorithms,13 1313 Berthier, Raphaël and Bach, Francis and Gaillard, Pierre (2020) [“Accelerated Gossip in Networks of Given Dimension using Jacobi Polynomial Iterations”](https://doi.org/10.1137/19M1244822). *SIAM Journal on Mathematics of Data Science*.13   14 1414 Bach, Francis (2019) [“Polynomial magic I: Chebyshev polynomials”](https://francisbach.com/chebyshev-polynomials/). *Blog post*.14  to derive lower bounds15 1515 Arjevani, Yossi and Shalev-Shwartz, Shai and Shamir, Ohad (2016) [“On lower and upper bounds in smooth and strongly convex optimization”](http://www.jmlr.org/papers/volume17/15-106/15-106.pdf). *The Journal of Machine Learning Research*.15  and to develop methods that are optimal for the average-case.16 1616 Pedregosa, Fabian and Scieur, Damien (2020) [“Average-case Acceleration Through Spectral Density Estimation”](https://arxiv.org/pdf/2002.04756.pdf). *arXiv preprint arXiv:2002.04756*.16   17 1717 Lacotte, Jonathan and Pilanci, Mert (2020) [“Optimal Randomized First-Order Methods for Least-Squares Problems”](https://arxiv.org/pdf/2002.09488.pdf). *arXiv preprint arXiv:2002.09488*.17

## 2. From Optimization to Polynomials

In this section we will develop a method to assign to every optimization method a polynomial that determines its convergence. We will first motivate this approach through gradient descent and then generalize it to other methods.

### Motivation: Gradient Descent

Consider the gradient descent method that generates iterates following
xt+1=xt−2L+μ∇f(xt) ,(2)

where L and μ are the largest and smallest eigenvalue of H respectively. Our aim is to derive a bound on the error ∥xt+1−x⋆∥ as a function of the number of iterations t and the spectral properties of H.

By the first order optimality conditions, at the optimum we have ∇f(x⋆)=0 and so Hx⋆=−b. We can use this to write the gradient as ∇f(xt)=H(xt−x⋆). Subtracting x⋆ from both sides of the above equation we have

xt+1−x⋆=xt−2L+μH(xt−x⋆)−x⋆=(I−2L+μH)(xt−x⋆)=(I−2L+μH)2(xt−1−x⋆)=⋯=(I−2L+μH)t(x0−x⋆)(3)(4)(5)(6)

We now have an expression for xt+1−x⋆ in terms of the initial conditions x0−x⋆, and a polynomial of degree t in H. Taking (euclidean) norms on both sides and using Cauchy-Schwartz we have

∥xt+1−x⋆∥≤∥I−2L+μH∥t∥x0−x⋆∥≤maxλ∈[μ,L]|(1−2L+μλ)t|∥x0−x⋆∥(7)(8)

where the second inequality follows by the definition matrix 2-norm. In this bound, convergence is determined by the maximum absolute value of the polynomial

PGDt=def(1−2L+μλ)t .(9)

Below there's a plot of this polynomial, together with its maximum absolute value represented with a dashed line:

The residual polynomial for gradient descent, Pt(λ)=(1−2λ/(L+μ)). Only even degrees are displayed for visualization purposes.

 [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/fabianp/98b052553d5fc50c7c2d099360bb2df5/polynomials_acceleration.ipynb)  ![](../_resources/36bb5ccdd27866022055853bb57062a8.png)

As expected, as t increases, the polynomial goes to zero in the interval [μ,L]. Furthermore, the largest absolute value of the polynomial is achieved at the edges, and we can use this to bound its maximum value in [(8)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Agd_respol_bound). This leads to the following classical bound on the error:

∥xt−x⋆∥≤(L−μL+μ)t∥x0−x⋆∥ .(10)

### General Method

We now consider more general methods and will show how the previous approach generalizes to this setting. We will consider gradient-based method, that is, methods where the update is a linear combination of the current iterate, current gradient and previous iterates

xt+1=xt+∑i=0t−1c(t)i(xi−xi+1)+c(t)t∇f(xt) ,(11)

for some scalar values c(t)j. To this method, we will associate the following *residual polynomial*  Pt, which is a polynomial of degree t defined recursively as

Pt+1(λ)P0(λ)=(1+c(t)tλ)Pt(λ)+∑i=0t−1c(t)i(Pi(λ)−Pi+1(λ))=1 .(12)

Remark. By construction, all residual polynomials verify Pt(0)=1.

The following lemma shows how the residual polynomial can be useful in the analysis of optimization methods. In particular, it shows how to express the error (xt−x⋆) in terms of the residual polynomial:

*Lemma ( attr(text) ) * For any gradient-based method and any iteration t, we have

xt−x⋆=Pt(H)(x0−x⋆) .(13)

*Proof.*

We will prove this by induction. For t=0, we have P0(H)=I since P0 is a polynomial of degree zero and so x0−x⋆=I(x0−x⋆) is clearly true.

Suppose now it's true for t. We will show that this implies it's true for t+1. By definition of xt+1 in Eq. [(11)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Agradient_based) we have

yt+1=yt+∑i=0t−1c(t)i(xi−xi+1)+c(t)t∇f(xt)=(I−c(t)tH)yt+∑i=0t−1c(t)i(yi−yi+1)=(I−c(t)tH)Pt(H)y0+∑i=0t−1c(t)i(Pi(H)−Pi+1(H))y0=Pt+1(H)y0

where the second identity follows by the induction hypothesis and the last one by definition of the residual polynomial in [(12)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Adef_residual_polynomial).

 ◼

From the above lemma we can derive a bound that replaces the matrix polynomial by a scalar bound. For this, consider the [eigendecomposition](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix#Eigendecomposition_of_a_matrix) of H=QΛQT, where Q is orthonormal and Λ is a diagonal matrix with diagonal elements the eigenvalues of H. Then taking norms in [(13)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Aresidual_error) and using this decomposition we have

∥xt−x⋆∥=∥Pt(H)(x0−x⋆)∥≤∥Pt(H)∥∥x0−x⋆∥ (Cauchy-Schwartz)=∥Pt(Λ)∥∥x0−x⋆∥ (eigendecomposition)(14)(15)(16)

Finally, since Pt(Λ) is a diagonal matrix, its operator norm is given by its largest element. This leads to the following bound:

*Corollary ( attr(text) ) * Let μ and L be the smallest and largest eigenvalue of H respectively. Then for any gradient-based method with residual polynomial Pt, we have

∥xt−x⋆∥≤maxλ∈[μ,L]conditioningmax[L]|Pt(λ)|algorithmmax[L]∥x0−x⋆∥initialization .(17)

This Corollary will be very useful in the following as it constructs a bound on the distance to optimum based on the three aspects that most influence convergence:

- The algorithm enters this bound through its residual polynomial. The smaller image of the residual polynomial, the better. Of course, we have the constraint Pt(0)=1, which makes choosing this polynomial non-trivial.

- The conditioning of the problem enters through the eigenvalue interval [μ,L].

- The initialization enters through its distance to optimum.

Of the quantities in the above lemma, maxλ∈[μ,L]|Pt(λ)| determines the progress that the algorithm makes at each iteration. This quantity will be useful in the following to compare the convergence properties of different algorithm. We will refer to it as the *convergence rate* of a method.

*Remark ( attr(text) ) * All the convergence rates in this post are worst-case bounds. By this I mean that the bounds hold for *any* problem within a class (quadratic problems of the form [(1)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Aopt) in this post). However, for certain problems the empirical convergence often is better than the theoretical bound. Furthermore, these bounds don't say anything about the typical performance of a method, which is more representative of the actual performance of a method. In a recent work, [Damien](https://damienscieur.com/) and I explored the average-case complexity of optimization algorithms, first in the non-asymptotic regime18 1818 Pedregosa, Fabian and Scieur, Damien (2020) [“Average-case Acceleration Through Spectral Density Estimation”](https://arxiv.org/pdf/2002.04756.pdf). *arXiv preprint arXiv:2002.04756*.18  and then in the asymptotic one.19 1919 Scieur, Damien and Pedregosa, Fabian (2020) [“Universal Average-Case Optimality of Polyak Momentum”](https://arxiv.org/pdf/2002.04664.pdf). *arXiv preprint arXiv:2002.04664*.19  The average-case analysis of optimization algorithms will be the subject of a future post.

## 3. Optimal Residual Polynomial

In the previous section we've seen that the convergence rate of gradient descent is (L−μL+μ)t. *Is this the optimal convergence rate or can we do better?*

To answer these questions we will use a somewhat indirect approach. Instead of seeking directly the optimal method, we will instead seek the optimal *residual polynomial*, and then reverse-engineer the method from its polynomial. This technique turns out to be more appropriate since it will allow us to use known results for best approximation polynomials.

By optimal in this case I mean the polynomial with smallest convergence rate. This corresponds to solving the problem

argminPmaxλ∈[μ,L]|P(λ)|(18)

where the minimization is over all degree t residual polynomials. The normalization Pt(0)=1 of residual polynomials makes this problem non-trivial, as otherwise we could just choose Pt(λ)=0.

The residual polynomial that minimizes the above expression turns out to be intimately related to [Chebyshev polynomials](https://en.wikipedia.org/wiki/Chebyshev_polynomials), which are one of the most used families of polynomials in numerical analysis.20 2020 Chebyshev, Pafnuti (1853) [“Théorie des mécanismes connus sous le nom de parallélogrammes”](https://books.google.ca/books?id=IOrnAAAAMAAJ&lpg=PA537&ots=qK0s3q3LTN&dq=Th%C3%A9orie%20des%20m%C3%A9canismes%20connus%20sous%20le%20nom%20de%20parall%C3%A9logrammes&pg=PA538#v=onepage&q&f=false). *Imprimerie de l'Académie impériale des sciences*.20   21 2121 [![Pafnuty_Lvovich_Chebyshev.jpg](../_resources/4e9aeb2b17adb5e12a8fb5500018ecbf.jpg)](https://en.wikipedia.org/wiki/Pafnuty_Chebyshev#/media/File:Pafnuty_Lvovich_Chebyshev.jpg)Chebyshev polynomials bear the name of [Pafnuty Chebyshev](https://en.wikipedia.org/wiki/Pafnuty_Chebyshev) (1821-1894). He is considered to be a founding father of Russian mathematics and known for his work in the fields of probability ([Chebyshev inequality](https://en.wikipedia.org/wiki/Chebyshev%27s_inequality)), statistics, mechanics and number theory ([Bertrand-Chebyshev theorem](https://en.wikipedia.org/wiki/Bertrand%27s_postulate)). 21

*Definition ( attr(text) ) * The Chebyshev polynomials of the first kind T0,T1,… are defined by the recurrence relation

T0(λ)=1T1(λ)=λTk+1(λ)=2λTk(λ)−Tk−1(λ) .(19)(20)

Among the many properties of Chebyshev polynomials is that a shifted and normalized version of it achieves the optimal convergence rate. Most best polynomial approximation results assume the polynomials are defined in the interval [−1,1]. However, we are only interested in how the residual polynomials behave in the interval [μ,L], and so it will be useful to define the linear mapping

σ(λ)=L+μL−μ−2L−μλ(21)
that maps the interval [μ,L] onto [−1,1] with σ(μ)=1 and σ(L)=−1.

We can now introduce a theorem first proven that relates the convergence rate optimality to Chebyshev polynomials. It was first proven by Vladimir Markov22 2222 Markov, Vladimir (1916) [“Über Polynome, die in einem gegebenen Intervalle möglichst wenig von Null abweichen”](https://doi.org/10.1007/BF01456902). *Mathematische Annalen* ([Open access version](https://sci-hub.se/10.1007/BF01456902)).22   23 2323 [Vladimir Markov](https://en.wikipedia.org/wiki/Vladimir_Markov_(mathematician)) was a student of Chebyshev and brother of the famous [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov). Vladimir died of tuberculosis when he was only 25 year old.23  and later rediscovered by Flanders and Shortley.24 2424 Flanders, Donald A and Shortley, George (1950) [“Numerical determination of fundamental modes”](https://sci-hub.tw/10.1063/1.1699598). *Journal of Applied Physics*.24

*Theorem ( attr(text) ) * The following shifted Chebyshev polynomial has smallest maximum absolute value through the interval [μ,L] (where μ>0) among all residual polynomials of degree t:

Pchebt(λ)=defTt(σ(λ))Tt(σ(0)) .(22)
We will refer to this polynomial as the *residual Chebyshev polynomial.*

*Proof.*

It's [known](https://en.wikipedia.org/wiki/Chebyshev_polynomials#Roots_and_extrema) that the Chebyshev polynomial Tt has k+1 extreme points in the interval [−1,1], and the image of these extremal points is alternately positive and negative. Because of the definition of Pt in [(22)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Adef_residual_chebyshev), the numerator is a linear translation of [−1,1] into [μ,L] and so Pt reaches its extreme points t+1 times in the interval [μ,L], and again the image at these extremal points is alternately positive and negative. Now suppose that Rt is a residual polynomial with the same degree as Tt but with smaller maximum absolute value and let Q(λ)=defPt(λ)−Rt(λ).

Since by assumption R has smaller maximum absolute value than Pk, Q is alternatedly >0 and <0 at the extremal points of Tt. From the intermediate value theorem, this implies that Q has t zeros in the interval [μ,L]. However, since both Pt and Rt are residual polynomials, we also have Q(0)=Pt(0)−Rt(0)=0 and so Q would have t+1 zeros in the interval [0,L]. Since Q is a polynomial of degree t and non-zero by assumption, this cannot be true. We reached a contradiction induced by the assumption that Rt had smaller maximum absolute value, which proves the theorem.

 ◼

As we did for gradient descent, I find it interesting to visualize the residual polynomials. Below is the Chebyshev and gradient descent residual polynomial, together with their maximum absolute value (≡convergence rate) shown in dashed lines.

 Gradient descent and Chebyshev residual polynomials

 [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/fabianp/98b052553d5fc50c7c2d099360bb2df5/polynomials_acceleration.ipynb)  ![](../_resources/0fe3ccd8f1c8f48cd1766c139f8a054c.png)

As expected from the theory, the maximum of the Chebyshev polynomial (dashed orange line) is significatively smaller than that of the gradient descent residual polynomial, which translates into a faster convergence rate. We can also see from this plot that the Chebyshev residual polynomial, unlike gradietn descent, reaches its extremal value not just once in the edges, but t+1 times, a fact that was crucial argument in proving Markov's Theorem.

## 4. The Chebyshev iterative method

From the previous theorem we know that the Chebyshev residual polynomials are optimal in terms of their worst-case convergence rate. We will now derive the method associated with this polynomial. We will do this by deriving the recurrence of the residual polynomial, and then using the definition of residual polynomial to match the method's coefficients.

Let a=σ(0),b=σ(λ). Then using the three term recurrence of the Chebyshev polynomials we have

Pchebt+1(λ)=Tt+1(b)Tt+1(a)=2bTt(b)Tt+1(a)−Tt−1(b)Tt+1(a)=2bTt(a)Tt+1(a)Pchebt(λ)−Tt−1(a)Tt+1(a)Pchebt−1(λ) ,(23)(24)

where in the second identity we have multiplied and divided the first term by Tt(a) and the second term by Tt−1(a)

Now let ωt+1=def2aTt(a)Tt+1(a). Then we can rewrite the previous equation as
Pchebt+1(λ)=ωtbaPchebt(λ)−14b2ωtωt−1Pchebt−1(λ)(25)

We would now like to a cheap way to compute ωt. Using again the three term recurrence of Chebyshev polynomials on ω−1t+1 we have

ω−1t+1=Tt+1(a)2aTt(a)=2aTt(a)−Tt−1(a)2aTt(a)=1−ωt4a2(26)
and so the full recursion for the residual polynomial becomes

P0(λ)=1, P1(λ)=1−2L+μλωt+1=(1−ωt4a2)−1 (with ω1=2)Pchebt+1(λ)=ωt+1baPchebt(λ)−14b2ωt+1ωtPchebt−1(λ)(27)(28)(29)

where the value of ω1=2 comes from the definition ωt+1=2aTt+1(a)/Tt(a).

This gives a recurrence for the residual polynomial. We can then use the connection betwen optimization methods and residual polynomials [(12)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Adef_residual_polynomial), this time in reverse, to find the coefficients of the optimization method from its residual polynomial. Matching terms in Pt in the previous equation we have

1+λc(t)t−c(t)t−1=ωt+1ba=ωt+1(1−2L+μλ)(30)
and so matching terms in λ we get
c(t)t=−2ωt+1L+μc(t)t−1=1−ωt+1 .(31)

 **Chebyshev Iterative Method**
 **Input**: starting guess x0, ρ=L−μL+μ
 x1=x0−2L−μ∇f(x0)
 ω1=2
 **For**  t=1,2,…  compute
ωt+1xt+1=(1−ρ24ωt)−1=∑nxt+(1−ωt+1)(xt−1−xt)−ωt+12L+μ∇f(xt)(32)(33)

Remark. Although we initially considered a class of methods that can use all previous iterates, the optimal method only requires to store the last iterate and the difference vector xt−1−xt. This makes the method much more practical than if we had to store all previous gradients.

## 5. Convergence rate

By construction, the Chebyshev iterative method has an optimal worst-case convergence rate. But what is this optimal rate?

Since the maximum absolute value of the Chebyshev polynomials in [−1,1] is 1, the convergence rate for Pcheb in this case is

maxλ∈[μ,L]|Pchebt(λ)|=Tt(L+μL−μ)−1 .(34)

This is however not very helpful if we cannot evaluate the Chebyshev polynomial. Luckily, outside the interval [−1,1] they do admit the following [explicit expression](https://en.wikipedia.org/wiki/Chebyshev_polynomials#Explicit_expressions)

Tt(λ)=12[(λ+λ2−1−−−−−√)t+(λ–λ2−1−−−−−√)t].(35)
Setting λ=L+μL−μ and using the trivial bound λ–λ2−1−−−−−√>0 we have

Tt(L+μL−μ)≥12(L+μL−μ+(L+μL−μ)2−1−−−−−−−−−−√)t=12(L+μ+2μL√L−μ)t=12(L√+μ√L√−μ√)t ,(36)(37)(38)

where last identity follows from completing the square in the numerator and using the identity L−μ=(L−−√−μ−−√)(L−−√+μ−−√) in the denominator. We have hence computed the convergence rate associated with the Chebyshev residual polynomial:

Corollary. Let x1,x2,… be the iterates generated by the Chebyshev iterative method. Then we have the following bound

∥xt−x⋆∥≤2(L−−√−μ−−√L−−√+μ−−√)t∥x0−x⋆∥.(39)

Note that, unlike in the case of gradient descent, the term 2(L√−μ√L√+μ√) is not an exact convergence rate but rather a (more interpretable) bound on the convergence rate. The looseness in this case is due to the bound we used in [(36)](http://fa.bianp.net/blog/2020/polyopt/#mjx-eqn-eq%3Abound_chebyshev). This explains why under some choices of L, μ and t the rate is worse than that of gradient descent despite being the method with an optimal convergence rate.

Despite the looseness of the bound, we can see that the square root in the L and μ constants can in some circumstances make the convergence rate much smaller, specially in cases in which μ is much smaller than L, which is a common setting, since in machine learning μ is often very close to zero. Below is a comparison of the convergence rate

 Comparison of convergence rates bounds for gradient descent and Chebyshev.

 [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/fabianp/98b052553d5fc50c7c2d099360bb2df5/polynomials_acceleration.ipynb)  ![](../_resources/41de1305c26fc380da5f950458a108f4.png)

## 6. Conclusion

In this post we've seen how to assign a polynomial to any gradient-based optimization method, how to use this polynomial to obtain convergence guarantees and how to use it to derive optimal methods. Using this framework we've derived the Chebyshev iterative method.

In the next posts, I will relate Polyak momentum (aka HeavyBall) to this framework.

 **Thanks** to [Damien Scieur](https://damienscieur.com/) —polynomial wizzard and amazing collaborator—, [Courtney Paquette](https://cypaquette.github.io/), [Nicolas Le Roux](http://nicolas.le-roux.name/) and [Adrien Taylor](https://www.di.ens.fr/~ataylor/) —for encouragement and stimulating discussions—, [Francis Bach](http://francisbach.com/) —for pointers and [great writings](http://francisbach.com/) on this topic—, [Nicolas Loizou](https://scholar.google.co.uk/citations?user=mvDmzAQAAAAJ&hl=en), and [Waiss Azizian](https://scholar.google.fr/citations?user=oXxTTe8AAAAJ&hl=fr) for discussions.

* * *

## 7. References

- Rutishauser, H. (1959) [“Theory of Gradient Methods”](https://doi.org/10.1007/978-3-0348-7224-9_2). *Refined Iterative Methods for Computation of the Solution and the Eigenvalues of Self-Adjoint Boundary Value Problems*
- Arjevani, Yossi and Shalev-Shwartz, Shai and Shamir, Ohad (2016) [“On lower and upper bounds in smooth and strongly convex optimization”](http://www.jmlr.org/papers/volume17/15-106/15-106.pdf). *The Journal of Machine Learning Research*
- Bach, Francis (2019) [“Polynomial magic I: Chebyshev polynomials”](https://francisbach.com/chebyshev-polynomials/). *Blog post*
- Berthier, Raphaël and Bach, Francis and Gaillard, Pierre (2020) [“Accelerated Gossip in Networks of Given Dimension using Jacobi Polynomial Iterations”](https://doi.org/10.1137/19M1244822). *SIAM Journal on Mathematics of Data Science*
- Cauchy, Augustin (1847) [“Méthode générale pour la résolution des systèmes d'équations simultanées”](https://gallica.bnf.fr/ark:/12148/bpt6k90190w/f406). *Comp. Rend. Sci. Paris*
- Chebyshev, Pafnuti (1853) [“Théorie des mécanismes connus sous le nom de parallélogrammes”](https://books.google.ca/books?id=IOrnAAAAMAAJ&lpg=PA537&ots=qK0s3q3LTN&dq=Th%C3%A9orie%20des%20m%C3%A9canismes%20connus%20sous%20le%20nom%20de%20parall%C3%A9logrammes&pg=PA538#v=onepage&q&f=false). *Imprimerie de l'Académie impériale des sciences*
- Fischer, Bernd (1996) [“Polynomial based iteration methods for symmetric linear systems”](https://doi.org/10.1007/978-3-663-11108-5). *Springer*
- Flanders, Donald A and Shortley, George (1950) [“Numerical determination of fundamental modes”](https://sci-hub.tw/10.1063/1.1699598). *Journal of Applied Physics*
- Golub, Gene H and Varga, Richard S (1961) [“Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods”](https://doi.org/10.1007/BF01386013). *Numerische Mathematik*
- Hestenes, Magnus R and Stiefel, Eduard (1952) [“Methods of conjugate gradients for solving linear systems”](https://pdfs.semanticscholar.org/466d/addfb6340c28cb8da548007028c8cc5df687.pdf). *Journal of research of the National Bureau of Standards*
- Lacotte, Jonathan and Pilanci, Mert (2020) [“Optimal Randomized First-Order Methods for Least-Squares Problems”](https://arxiv.org/pdf/2002.09488.pdf). *arXiv preprint arXiv:2002.09488*
- Lanczos, Cornelius (1952) [“Solution of systems of linear equations by minimized iterations”](https://nvlpubs.nist.gov/nistpubs/jres/049/1/V49.N01.A06.pdf). *J. Res. Nat. Bur. Standards*
- Lemaréchal, Claude (2012) [“Cauchy and the gradient method”](https://www.math.uni-bielefeld.de/documenta/vol-ismp/40_lemarechal-claude.pdf). *Doc Math Extra*
- Markov, Vladimir (1916) [“Über Polynome, die in einem gegebenen Intervalle möglichst wenig von Null abweichen”](https://doi.org/10.1007/BF01456902). *Mathematische Annalen*
- Pedregosa, Fabian and Scieur, Damien (2020) [“Average-case Acceleration Through Spectral Density Estimation”](https://arxiv.org/pdf/2002.04756.pdf). *arXiv preprint arXiv:2002.04756*
- Scieur, Damien and Pedregosa, Fabian (2020) [“Universal Average-Case Optimality of Polyak Momentum”](https://arxiv.org/pdf/2002.04664.pdf). *arXiv preprint arXiv:2002.04664*
- Varga, Richard S (1957) [“A comparison of the successive overrelaxation method and semi-iterative methods using Chebyshev polynomials”](https://doi.org/10.1137/0105004). *Journal of the Society for Industrial and Applied Mathematics*
- Young, David (1953) [“On Richardson's method for solving linear systems with positive definite matrices”](https://doi.org/10.1002/sapm1953321243). *Journal of Mathematics and Physics*