Spectral Normalization Explained

# Spectral Normalization Explained

## Jan 4, 2018•

There has been a lot of profession of “breaking the state of the art” within the generative adversarial networks community lately. Sometimes, it has been difficult to keep apart hyperbole from genuine innovations in GANs. However, in recent weeks an [OpenReview preprint](https://openreview.net/forum?id=B1QRgziT-) has caught the attention of Ian Goodfellow, the inventor of GANs. Goodfellow was impressed that the authors’ method managed to generate samples from all 1000 ImageNet classes *simultaneously*, the first demonstration of this achievement. The lack of diversity is a serious problem for GANs, and therefore this is a major milestone.

![SN-GAN CIFAR-10 Samples (my implementation)](../_resources/eb487463b8b9df0fa169b564d4014eef.png)

Samples from [my PyTorch implementation of spectral normalization GANs](https://github.com/christiancosgrove/pytorch-spectral-normalization-gan).

Spectral normalization is a deceptively simple concept, so let’s go through the argument outlined in the paper.

# The centrality of Lipschitz continuity in GANs

## Definition of Lipschitz continuity

Lipschitz continuity sounds like an arcane term only introduced in a mathematical analysis course, but it is actually a straightforward “nice” property of functions—even simpler to explain, perhaps, than the usual epsilon-delta continuity.

Suppose we have a GAN discriminator D:I→ℝD:I→R, where II is the space of images (e.g., ℝ32×32R32×32). Because both the domain and codomain of this function have inner products, we have a natural metric (distance function) in both spaces: the L2 distance.

If our discriminator is *KK-Lipschitz continuous*, then for all xx and yy in II,

||D(x)−D(y)||≤K||x−y||||D(x)−D(y)||≤K||x−y||

where |⋅||⋅| is the L2 norm. Here, if KK is a minimum, then it is called the *Lipschitz constant* of the discriminator.

(It’s easy to see that if I=ℝI=R, then Lipschitz continuity implies epsilon-delta continuity.)

Let’s look at the 1D case to illustrate Lipschitz continuity geometrically. Suppose D(x)=sin(x)D(x)=sin⁡(x). If DD is Lipschitz continuous, then we can draw a cone centered at every point on its graph such that the graph lies outside of this cone. (Drag the sliders below to verify this for yourself.)

JSXGraph v0.99.6 Copyright (C) see http://jsxgraph.org1234−1−2−3−41234−1−2−3−4
0,0
xx = 0.00
KK = 1.00
pol1
pol1

It’s clear that sinsin is 1-Lipschitz continuous. What about ReLU, our favorite activation function?

JSXGraph v0.99.6 Copyright (C) see http://jsxgraph.org1234−1−2−3−41234−1−2−3−4
0,0
\(x\) = 2.50
\(K\) = 1.28
pol1
pol1
This is also obviously 1-Lipschitz continuous.
JSXGraph v0.99.6 Copyright (C) see http://jsxgraph.org1234−1−2−3−41234−1−2−3−4
0,0
xx = 0.00
KK = 1.00
pol1
pol1

In fact, Leaky ReLU (with a leak value less than one) is 1-Lipschitz continuous. However, it is easy to come up with a counterexample:

JSXGraph v0.99.6 Copyright (C) see http://jsxgraph.org1234−1−2−3−41234−1−2−3−4
0,0
xx = 0.00
KK = 1.00
pol1
pol1
The function D(x)=x2D(x)=x2 is not Lipschitz continuous at all.

One interesting fact to notice from these examples is that if a 1D function is differentiable, then its Lipschitz constant is just the maximum value of its derivative. This gives a slightly more rigorous explanation of why x2x2 is not Lipschitz continuous: its derivative, 2x2x, is unbounded.

So, what is the justification for requiring that our discriminator be KK-Lipschitz? If we are training a Wasserstein GAN, then [Kantorovich-Rubinstein duality requires it](https://vincentherrmann.github.io/blog/wasserstein/). However, when we’re training using the standard KL-divergence loss, there’s a looser but still intuitive explanation. Just as *batch normalization* ensures that the signals within a neural net have well-behaved statistics—controlling the exploding gradient problem that plagues RNNs and deep feedforward networks—mandating Lipschitz continuity bounds the gradients in our discriminator.

## The multidimensional case

**Suppose we have a linear function A:ℝn→ℝmA:Rn→Rm**. This function could be the pre-activation operation of one layer in a multilayer perceptron. We can compute the *spectral norm* of this function, which is defined as the largest singular value of the matrix AA, i.e., the square root of the largest eigenvalue of ATAATA.

**What is the Lipschitz constant of this function, if it exists?** Since AA is linear, we can set our point of reference yy to zero (place our “cone” at zero). In other words, if AA is KK-Lipschitz at zero, then it is KK-Lipschitz everywhere. This simplifies the Lipschitz continuity requirement to

||Ax||≤K||x||||Ax||≤K||x||

for all x∈Ix∈I. This is equivalent to the statement

⟨Ax,Ax⟩≤K2⟨x,x⟩,∀x∈I⟨Ax,Ax⟩≤K2⟨x,x⟩,∀x∈I
which in turn is equivalent to
⟨(ATA−K2)x,x⟩≤0,∀x∈I.⟨(ATA−K2)x,x⟩≤0,∀x∈I.

If we expand xx in the orthonormal basis of eigenvectors of ATAATA (i.e., x=∑ixivix=∑ixivi), we can then write out this inner product explicitly:

⟨(ATA−K2)x,x⟩=⟨(ATA−K2)∑ixivi,∑jxjvj⟩=∑i∑jxixj⟨(ATA−K2)vi,vj⟩=∑i(λi−K2)x2i≤0⟹∑i(K2−λi)x2i≥0.⟨(ATA−K2)x,x⟩=⟨(ATA−K2)∑ixivi,∑jxjvj⟩=∑i∑jxixj⟨(ATA−K2)vi,vj⟩=∑i(λi−K2)xi2≤0⟹∑i(K2−λi)xi2≥0.

Note that since ATAATA is positive semidefinite, all the λiλis must be nonnegative. To guarantee the above sum to be nonnegative, each term must be nonnegative, so we have

K2−λi≥0 for all i=1…n.K2−λi≥0 for all i=1…n.

Since we choose KK to be the minimum value satisfying the above constraints, we immediately see that KK is the square root of the largest eigenvalue of ATAATA. **Therefore, the Lipschitz constant of a linear function is its largest singular value, or its *spectral norm***.

## Composition of functions

Analogously to the 1D case, it is easy to observe that the Lipschitz constant of a general differentiable function f:ℝn→ℝmf:Rn→Rm is the maximum spectral norm (maximum singular value) of its gradient over its domain.

||f||Lip=supxσ(∇f(x))||f||Lip=supxσ(∇f(x))

Now, let’s introduce a function g:ℝm→ℝlg:Rm→Rl. The underlying premise of the spectral normalization paper is that if we can find, or at least bound, the Lipschitz constant of the composition of ff and gg, then we can obtain a bound on the Lipschitz constant of an arbitrary multilayer discriminator, which is just a composition of linear maps and componentwise nonlinearities.

According to the chain rule, we have

∇(g∘f)(x)=∇g(f(x))∇f(x).∇(g∘f)(x)=∇g(f(x))∇f(x).

Remember that these gradients are just matrices being multiplied together. This suggests a promising approach: to find the spectral norm of a composition of functions, express it in terms of the spectral norm of the matrix product of its gradients. We can write the spectral norm (maximum singular value) in another convenient form:

σ(∇f(x))=sup||v||≤1||[∇f(x)]v||(1)(1)σ(∇f(x))=sup||v||≤1||[∇f(x)]v||

σ(∇(g∘f)(x))=sup||v||≤1||[∇g(f(x))][∇f(x)]v||(2)(2)σ(∇(g∘f)(x))=sup||v||≤1||[∇g(f(x))][∇f(x)]v||

Since the supremum in (1) is convex, we can bound the result in (2) as follows:

sup||v||≤1||[∇g(f(x))][∇f(x)]v||≤sup||u||≤1||[∇g(f(x))]u||sup||v||≤1||[∇f(x)]v||.sup||v||≤1||[∇g(f(x))][∇f(x)]v||≤sup||u||≤1||[∇g(f(x))]u||sup||v||≤1||[∇f(x)]v||.

In other words,
||g∘f||Lip≤||g||Lip||f||Lip.||g∘f||Lip≤||g||Lip||f||Lip.

This bound is provides the theoretical justification for spectral normalization outlined in the paper. The solution goes like this: if we can fix each of the factors in the right-hand side of this inequality to 1, then we can ensure that the discriminator is at most 1-Lipschitz. If we are training a Wasserstein GAN, this guarantees that Kantarovich-Rubenstein duality holds.

# Spectral normalization

Fixing the spectral norm of a layer is as straightforward as it sounds. *Spectral normalization*, proposed in this paper, simply replaces every weight WW with W/σ(W)W/σ(W). But how do we efficiently compute σ(W)σ(W), the largest singular value of WW? The answer is a cheap and effective technique called *power iteration*.

Suppose we have a linear map W:ℝn→ℝmW:Rn→Rm. Suppose we have a random vector in the domain of our matrix, v∈ℝnv∈Rn, and a vector in the codomain, u∈ℝmu∈Rm.

Let’s first consider vv. We can form the square matrix WTW:ℝn→ℝnWTW:Rn→Rn. *Power iteration* involves computing the recurrence relation

vt+1=WTWvt||WTWvt||vt+1=WTWvt||WTWvt||

we can unroll this recurrence relation:
vt=(WTW)tv||(WTW)tv||vt=(WTW)tv||(WTW)tv||

By the [spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem), we can write vv in an orthonormal basis of eigenvectors of WTWWTW. Let’s denote λ1…λnλ1…λn as the descending eigenvalues of WTWWTW and e1…ene1…en the corresponding eigenvectors.

Power iteration then consists of computing the following:

vt=(WTW)t∑iviei||(WTW)t∑iviei||=∑iviλtiei||∑iviλtiei||=v1λt1∑iviv1(λiλ1)tei||v1λt1∑iviv1(λiλ1)tei||.vt=(WTW)t∑iviei||(WTW)t∑iviei||=∑iviλitei||∑iviλitei||=v1λ1t∑iviv1(λiλ1)tei||v1λ1t∑iviv1(λiλ1)tei||.

Now note that since λ1λ1 is the largest eigenvalue of WTWWTW, upon power iteration limt→∞λiλ1=0limt→∞λiλ1=0 for i>1i>1. So, after many iterations of the above procedure, vtvt converges to e1e1. We call the intermediate computation Wvt||Wvt||=utWvt||Wvt||=ut. The power iteration procedure becomes:

ut+1=Wvtvt+1=WTut+1.ut+1=Wvtvt+1=WTut+1.

Since the singular values of WTWT and WW are the same, it must be that the spectral norm is σ(W)=λ1‾‾√=||Wv||σ(W)=λ1=||Wv||. Since ||u||||u|| is of unit length, we can conveniently compute the spectral norm as follows:

σ(W)=||Wv||=uTWv.σ(W)=||Wv||=uTWv.

Now, the algorithm of spectral normalization should appear simple. For every weight in our network, we randomly initialize vectors uu and vv. Because the weights change slowly, we only need to perform a single power iteration on the current version of these vectors for each step of learning; this is why spectral normalization is more computationally efficient than, say, [gradient penalty](https://arxiv.org/pdf/1704.00028.pdf).

[I’ve implemented a simple spectral normalization wrapper module in PyTorch](https://github.com/christiancosgrove/pytorch-spectral-normalization-gan). Feel free to try it out and see the effectiveness of spectral normalization GANs yourself.