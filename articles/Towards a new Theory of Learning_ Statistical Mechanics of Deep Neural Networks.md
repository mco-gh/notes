Towards a new Theory of Learning: Statistical Mechanics of Deep Neural Networks

# Towards a new Theory of Learning: Statistical Mechanics of Deep Neural Networks

[December 3, 2019](https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/)  [Charles H Martin, PhD](https://calculatedcontent.com/author/charlesmartin14/)  [Uncategorized](https://calculatedcontent.com/category/uncategorized/)  [One comment](https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/#comments)

## Introduction

For the past year or two, we have talked a lot about how we can understand the properties of Deep Neural Networks by examining the spectral properties of the layer weight matrices ![latex.php](../_resources/502b071a96f05c030e5fa967a3229405.png). Specifically, we can form the correlation matrix

![latex.php](../_resources/b6d75295008bd815a9774256bb24c66a.png),
and compute the eigenvalues ![latex.php](../_resources/743cd6bb6c66c665b215271837070456.png)
![latex.php](../_resources/3c3c5a96c175d86791a9f234110a4f72.png).

By plotting the histogram of the eigenvalues (i.e the spectral density ![latex.php](../_resources/9eb39252bb19646e7b540f80ef04166c.png)), we can monitor the training process and gain insight into the implicit regularization and convergence properties of DNN. Indeed, we have identified

### 5+1 Phases of Training

![screen-shot-2019-11-29-at-10.28.02-pm.png](../_resources/c3d69c73265d699a20e8da7f8eb3b400.png)

Each of these phases roughly corresponds to a Universality class from Random matrix Theory (RMT). And as we shall see below, we can use RMT to develop a new theory of learning.

First, however, we note that for nearly every pretrained DNNs we have examined (over 450 in all) , the phase appears to be in somewhere between Bulk-Decay and/or Heavy-Tailed .

### Heavy Tailed Implicit Regularization

Moreover, for nearly all DNNs, the spectral density ![latex.php](../_resources/9eb39252bb19646e7b540f80ef04166c.png) can be fit to a truncated power law, with exponents frequently lying in the Fat Tailed range [2-4], and the maximum eigenvalue no larger than say 100

![latex.php](../_resources/de512570a2912e6aeec02df3a5b8d6c0.png)
![latex.php](../_resources/bb78b546e5e0cc41d2ee032cdcfe8df9.png),

Most importantly, in 80-90% of the DNN architectures studied, on average, smaller exponents ![latex.php](../_resources/c6c57f9d853bf631a4f4772b852a1860.png) correspond to smaller test errors.

###  DNN Capacity Metrics in Practice

Our empirical results suggest that the power law exponent can be used as (part of) a practical capacity metric. This led us to propose the ![latex.php](../_resources/18cdb2f70a93a9fcc69bdd39e5c0da6b.png) metric for DNNs:

![latex.php](../_resources/8a6ec907f65589e76ef1b2b576bf8c44.png)

where we compute the exponent ![latex.php](../_resources/c6c57f9d853bf631a4f4772b852a1860.png) and maximum eigenvalue ![latex.php](../_resources/66350c57a399eef1c7c0c60c9213c82f.png) for each layer weight matrix (and Conv2D feature maps), and then form the total DNN capacity as a simple weighted average of the exponents. Amazingly, this metric correlates very well with the reported test accuracy of pretrained DNNs (such as the VGG models, the ResNet models, etc)

![vgg-w_alphas.png](../_resources/6b4d6a388a32c4336406bb742963f107.png)

#### WeightWatcher

We have even built a open source, python command line tool–[weightwatcher](https://github.com/CalculatedContent/WeightWatcher)–so that other researchers can both reproduce and leverage our results

`pip install weightwatcher`

And we have a Slack Channel for those who want to ask questions, dig deeper, and/or contribute to the work. Email me, or [ping me on LinkedIn,](https://www.linkedin.com/in/charlesmartin14/) to join our vibrant group.

All of this leads to a very basic question:

## ***Why does this even work ?***

To answer this, we will go back to the foundations of the theory of learning, from the physics perspective, and rebuild the theory using in both our experimental observations, some older results from Theoretical Physics, and (fairly) recent results in Random Matrix Theory.

## Statistical Mechanics of Learning

Here, I am going to sketch out the ideas we are currently researching to develop a new theory of generalization for Deep Neural Networks. We have a lot of work to do, but I think we have made enough progress to present these ideas, informally, to flush out the basics.

**What do we seek ? ** A practical theory that can be used to predict the generalization accuracy of a DNN solely by looking at the trained weight matrices, without looking at the test data.

**Why ? ** Do you test a bridge by driving cars over it until it collapses ? Of course not! So why do we build DNNs and only rely on brute force testing ? Surely we can do better.

**What is the approach ?** We start with the classic Perceptron Student-Teacher model from Statistical Mechanics of the 1990s. The setup is similar, but the motivations are a bit different. We have discussed this model earlier here [Remembering Generalization in DNNs.](https://calculatedcontent.com/2018/04/01/rethinking-or-remembering-generalization-in-neural-networks/) from our paper [Understanding Deep Learning Requires Rethinking Generalization](https://arxiv.org/abs/1611.03530)[.](https://arxiv.org/abs/1611.03530)

Here, let us review the mathematical setup in some detail:

### the Student-Teacher model

We start with the simple model presented in chapter 2, [Engel and Van der Brock](https://books.google.com/books/about/Statistical_Mechanics_of_Learning.html?id=qVo4IT9ByfQC), interpreted in a modern context.

Here, we want to do something a little different, and use the formalism of Statistical Mechanics to both compute the average generalization error, and to interpret the global convergence properties of DNNs in light of this , giving us more insight into and to provide a new theory of [Why Deep Learning Works (as proposed in 2015)](https://calculatedcontent.com/2015/03/25/why-does-deep-learning-work/).

Suppose we have some trained or pretrained DNN (i.e. like VGG19). We want to compute the average / typical error that our Teacher DNN could make, just by examining the layer weight matrices. *Without peeking at the data.*

**Conjecture 1**: * We assume all layers are statistically independent, so that the average generalization capacity *![latex.php](../_resources/353ebf592c5d5856724c5eafd8f18c68.png) *(i.e. 1.0-error) is just the product of the contributions of from each layer weight matrix *![latex.php](../_resources/7296bd1e8d66cd2eebad79f279bf4544.png) .

![latex.php](../_resources/ac431924520e0ab4584230eb2a260f75.png)

**Example:** The Product Norm is a Capacity measure for DNNs from[traditional ML theory](https://arxiv.org/abs/1808.01174).

![latex.php](../_resources/7a8fa86d7d1bdebfebc539a54eda0082.png)

The Norm may be Frobenius Norm, the Spectral Norm, or even their ratio, the Stable Rank.

This independence assumption is probably not a great approximation but it gets us closer to a realistic theory. Indeed, even traditional ML theory recognizes this, and may use Path Norm to correct for this. For now, this will suffice.

**Caveat 1: **If we take the logarithm of each side, we can write the log Capacity as the sum of the layer contributions. More generally, we will express the log Capacity as a weighted average of some (as yet unspecified) log norm of the weight matrix.

![latex.php](../_resources/e04d297e80b1c1f0d6a1df75c3204d37.png)

#### *Capacity for a Single Layer*: Perceptron model

We now set up the classic Student-Teacher model for a Perceptron–with a slight twist. That is, from now on, we assume our models have 1 layer, like a Perceptron.

Let’s call our trained or pretrained DNN the Teacher **T**. The Teacher maps data to labels. Of course, there could be many Teachers which map the same data to the same labels. For **our** specific purposes here, we just fix the Teacher **T**. We imagine that the learning process is for us to learn all possible Student Perceptrons **J** that also map the data to the labels, in the same way as the Teacher.

But for a pretrained model, we have no data, and we have no labels. And that’s ok. Following Engle and Van der Brock (and also Engle’s 2001 paper ), consider the following Figure, which depicts the vector space representations of **T** and **J**.

![student-teacher.png](../_resources/c3d57c43cfba90239573cd54c3320526.png)

To compute the average generalization error, we write total error is the sum of all the errors over all possible Students **J** for a given Teacher **T**. And we model this error ![latex.php](../_resources/af4312cbe7da569bd2b7c1d62b3d3102.png) with the inverse (arc cosine) of the vector dot product between **J **and **T**:

![latex.php](../_resources/be23deac6fd918deaf62f2e59a995a26.png)

**For our purposes**, if instead of N-dim vectors, if we let **T** and **J** be NxM weight matrices, then the dot product becomes the Solid Angle ![latex.php](../_resources/db07ad4e379cc6f3a3b5ed427f26f967.png).

This formalism lets us use the machinery of Statistical Mechanics to write the total error as an integral over all possible Student vectors **J**, namely, the phase space volume ![latex.php](../_resources/8d12333f9cac61f6f27d36537fde83a8.png)  of our model:

![latex.php](../_resources/3304dcbabccfc00e073f1805b48b644a.png)

where the first delta function ![latex.php](../_resources/f26f461bff12b41c20a0c856f93c314b.png)  enforces the normalization condition, or spherical constraints, on the Student vectors** J**, and the second delta function ![latex.php](../_resources/940b6fb90cbd2084a77bbbc26fa7c301.png) is a kind of Energy potential..

The normalization can be subsumed into a general measure, as
![latex.php](../_resources/d16ef5fc650b52d29c313b922a51f96f.png)

which actually provides us a more general expression for the generalization error

![latex.php](../_resources/1c1902310c9ff332a03382ce4499fa79.png)

Now we will deviate from the classic Stat Mech approach of the 90s. In the original analysis, one wants to compute the phase space volume ![latex.php](../_resources/994f6dc264499d33e73b556ad81992e2.png) as a function of the macroscopic thermodynamic variables, such as the size of the training set, and study the learning behavior. We have reviewed this classic results in our[2017 paper.](https://arxiv.org/abs/1710.09553)

We note that, for the simple Perception, the Student and Teachers,:  ![latex.php](../_resources/9cf697e1d82cde4764ab3fc63b9b4b1f.png), are represented as N-dimensional vectors, and the interesting physics arises in the Ising Perception, when the elements are discrete:

**Continuous Perception**: ![latex.php](../_resources/d2b6ce71a3d40c25f5570da60f5b03f1.png) (unintersting behavior)

**Ising Perception**: ![latex.php](../_resources/42cef272deb458450cb4a1b3e7081d18.png) (phase transitions, requires Replica theory, …)

And in our early work, we propose how to interpret the expected phase behavior in light of experimental results (at Google) that seem to require [Rethinking Generalization](https://arxiv.org/abs/1611.03530). Here, we want to reformulate the Student-Teacher model in light of our own recent experimental studies of the spectral properties of real-world DNN weight matrices from production quality, pretrained models.

**Our Proposal:**  We let ![latex.php](../_resources/9cf697e1d82cde4764ab3fc63b9b4b1f.png) be strongly correlated (NxM) real matrices, with truncated, Heavy Tailed ESDs. Specifically, we assume that we know the Teacher **T** weight matrices exactly, and seek all Student matrices **J** that have the same spectral properties as the Teacher.

We can think of the class of Student matrices **J** as all matrices that are close to **T**. What we really want is the best method for doing this, that hasd been tested experimentally. Fortunately, Hinton and coworkers have recently revisited [Similarity of Neural Network Representations](https://arxiv.org/abs/1905.00414), and found the best matrix similarity method is

**Canonical Correlation Analysis (CCA): **  ![latex.php](../_resources/95be3a955b8de0dc6f7636f90e4d370d.png)

Using this, we generalize the Student-Teacher vector-vector overlap., or dot-product, to be the Solid-Angle between the **J **and **T** matrices:and plug this directly into our expression for the phase space volume ![latex.php](../_resources/2cf2206a4eaf4b8ff4e3885b349fc4ff.png). (and WLOG, we absorb the normalization N into the matrices, and now have ![latex.php](../_resources/dcda523c2ee447c37f7a6f45b332747e.png)

![latex.php](../_resources/50e136fe0510f47ef51f568905c3782e.png)

We now take the [Laplace Transform](https://www.youtube.com/watch?v=lI7fezJRPUw) of ![latex.php](../_resources/2cf2206a4eaf4b8ff4e3885b349fc4ff.png) which allows us to integrate over all possible errors ![latex.php](../_resources/af4312cbe7da569bd2b7c1d62b3d3102.png) that all possible Students might make:

![latex.php](../_resources/b36552bc5a28654068da6e4a6e4fe339.png)

Note: we need to actually integrate over ![latex.php](../_resources/2f471af5dbd33d1c22f87f95e181265d.png). Leaving this work aside for now, the Laplace Transform lets us convert the delta function to a exponential, giving

**Conjecture 2:*** We can write the layer matrix contribution to the total average generalization error as an integral over all possible (random) matrices **J** that resemble the actual (pre-)trained weight matrices ***T** (as given above).

![latex.php](../_resources/e56b4811e0424b971fbdaa8ecfac79fd.png)

Notice this expression resembles a classical partition function from statistical field theory: ![latex.php](../_resources/55ea7461ba50065b7fbf719ab0194602.png), except instead of integrating over the vector-valued **p** and **q** variables, we have to integrate over a class of random matrices** J**. This is the key observation, and requires some modern techniques to perform

### RMT and HCIZ Integrals

These kinds of integrals traditionally appeared in Quantum Field Theory and String Theory, but also in the context of[Random Matrix applied to Levy Spin Glasses](https://arxiv.org/abs/cond-mat/9801209), And it is this early work on Heavy Tailed Random Matrices that has motivated our empirical work. Here, to complement and extend our studies, we lay out an (incomplete) overview of the Theory.

These integrals are called Harish Chandra–Itzykson–Zuber (*HCIZ*) integrals. A good introductory reference on both RMT and HCIZ integrals the recent book [“A First Course in Random Matrix Theory”](https://physics-complex-systems.fr/wp-content/uploads/2019/03/Notes_chap1-13.pdf), although we will base our analysis here on the results of the [2008 paper by Tanaka,](https://iopscience.iop.org/article/10.1088/1742-6596/95/1/012002/pdf)

First, we need to re-arrange a little of the algebra. We will call **A** the Student correlation matrix:

![latex.php](../_resources/3183740ffc8fd6bc32ee56d396ad3f15.png)

and let **W**, **X** be the original weight and correlation matrices for our pretrained DNN, as above:

![latex.php](../_resources/17c96744f7fcab409b898865851e38de.png),
and then expand the CCA Similarity metric as
 ![latex.php](../_resources/b3b3c5eab4ceef98b6ebaf51bf5c4b3e.png)

We can now express the log HCIZ integral, in using Tanaka’s result, as an expectation value of all random Student correlations matrices **A** that *resemble*  **X**.

![latex.php](../_resources/bc6e26f9e69d742e7697e8d0e1739eb1.png)

And this can be expressed as a sum over Generating functions ![latex.php](../_resources/30678c74909e9e328f643be511be27e4.png) that depends only the statistical properties of the random Student weight matrices **A**. Specifically

![latex.php](../_resources/3be91ce9d2efa9c0de447ded1f8bd72d.png)

where ![latex.php](../_resources/ca062aa5f295d6141431f378b2d484b6.png) is the R-Transform from RMT.

**The R Transform** is like an inverse Green’s function (i.e a Contour Integral), and is also a cumulant generating function. As such, we can write ![latex.php](../_resources/2a808cd5c3bbfd7716cbfd641dbc3cf0.png) as a series expansion

![latex.php](../_resources/fd0d533c64e32f3e41f76f0703b1b2d9.png)

where ![latex.php](../_resources/1a980b66f02c4c52c0695a5e09740fd1.png) are ***Generalized Cumulants ***from RMT.

Now, since we expect the best Students matrices *resemble* the Teacher matrices, we expect the Student correlation matrix **A** to have similar spectral properties as our actual correlation matrices **X**. And this where we can use our classification of the*** 5+1 Phases of Training***. Whatever phase **X** is in, we expect all the **A** to be in as well, and we therefore expect the R-Transform of **A** to have the same functional form as **X**.

That is, if our DNN weight matrix has a Heavy Tailed ESD
 ![latex.php](../_resources/1c6bb8634e91ddfbd65326dfbb6884b0.png)

then we expect all of the students to likewise have a Heavy Tailed ESD, and with the same exponent (at least for now).

 ![latex.php](../_resources/02c627446ef9a1c93378addcc1da5116.png)
**Quenched **  **vs Annealed Averages**

Formally, we just say we are averaging over all Students **A**. More technically, what really want to do is fix some Student matrix (i.e. say **A** = diagonal **X**), and then integrate over all possible Orthogonal transformations **O **of **A** (see 6.2.3 of Potters and Bouchaud)

![latex.php](../_resources/802b9b80057a1a36db45bb5752aa50be.png)

Then, we integrate over all possible** A**~diag(**X**) , which would account for fluctuations in the eigenvalues. We conceptually assume this is the same as integrating over all possible Students **A**, and then taking the log.

The LHS is called the Quenched Average, and the RHS is the Annealed. Technically, they are not the same, and in traditional Stat Mech theory, this makes a big difference. In fact, in the original Student-Teacher model, we would also average over all Teachers, chosen uniformly (to satisfy the spherical constraints)

Here, we are doing RMT a little differently, which may not be obvious until the end of the calculation. We do not assume a priori a model for the Student matrices. That is, instead of fixing **A**=diag(**X**), we will fit the ESD of **X** to a *continuous* (power law) distribution ![latex.php](../_resources/26257105a72cf8084c19adc4cc8678c2.png) , and then *effectively sample* over all **A** as if we had drawn the eigenvalues of **A** from ![latex.php](../_resources/26257105a72cf8084c19adc4cc8678c2.png). (In fact, I suppose we could actually do this numerically instead of doing all this fancy math–but what fun is that?).

The point is, we want to find an expression for the HCIZ integral (i.e the layer / matrix contribution to the Generalization Error) that only depends on observations of **W**, the weight matrix of the pretrained DNN (our Teacher network). The result only depends on the eigenvalues of **X**, and the R-transform of **A** , which is parameterized by statistical information from** X**.

In principle, I supposed we could measure the generalized cumulants ![latex.php](../_resources/1299214fb5801329a19fe9f6e425edca.png) of **X**,. and assume we can plug these in for ![latex.php](../_resources/bc1c4ab5f02cef29965ec5c874dc16cd.png). We will do something a little easier.

Let us consider 2 classes of matrices as models for **X.**
**Gaussian (Wigner) Random Matrix: **Random-Like Phase
The R-Transform for Gaussian Random matrix is well known:
 ![latex.php](../_resources/0cd22aa2dc8bc55b73db7a52538f2230.png)
Taking the integral and plugging this into the Generating function, we get
 ![latex.php](../_resources/a7e23f685b44fd4a9a9fc3b8cc56e0f5.png)
 ![latex.php](../_resources/d931ec132d0c404f2586f180f426eac8.png)

So when **X** is Random-Like , the layer / matrix contribution is like the Frobenius Norm (but squared), and thus average Generalization Error is given by a Frobenius Product Norm (squared).

**Levy Random Matrix: ** Very Heavy Tailed Phase–but with

We don’t have results (yet) for the Very Heavy Tailed Phase with , but, a[s we have argued previously](https://arxiv.org/abs/1901.08278), due to finite size effects, we expect that the Very Heavy Tailed matrices appearing in DNNs will more resemble Levy Random matrices that the Random-Like Phase. So for now, we will close one eye and extend the results for  to .

The R-Transform for a Levy Random Matricx has been given by [Burda](https://arxiv.org/abs/0909.5228)

Taking the integral and plugging this into the Generating function, we get
 ![latex.php](../_resources/4b24af1f09f7f6e9afa0a3b70f278bde.png)
 ![latex.php](../_resources/d049b35f24ba70e07e3104146fa8ef7c.png)
**Towards our Heavy Tailed Capacity Metric**

1. Let us pull the power law exponent  out of the Trace, effectively ignoring cross terms in the sum over

![latex.php](../_resources/62b6af7c1317418420a34cbde1e597ab.png)

2. We also assume we can replace the Trace of  with its largest eigenvalue  , which is actually a good approximation for very heavy tailed Levy matrices, when

![latex.php](../_resources/e52f29e2d34d80b86d0dc03a1425d615.png)

This gives an simple expression for the HCIZ integral expression for the layer contribution to the generalization error

![latex.php](../_resources/880f8fba8af1ce7b24e37d8966054081.png)
Taking the logarithm of both sides, gives our expression
![latex.php](../_resources/3e13450924ff13cd6aad37c99cf5dead.png)

We have now derived the our Heavy Tailed Capacity metric using a matrix generalization of the classic Student Teacher model, with the help of some modern Random Matrix Theory.

**QED**

I hope this has convince you that there is still a lot of very interesting theory to develop for AI / Deep Neural Networks. And that you will stay tuned for the published form of this work. And remember…

`pip install weightwatcher`

A big thanks to [Michael Mahoney at UC Berkeley](https://www.stat.berkeley.edu/~mmahoney/) for collaborating with me on this work , and to [Mirco Milletari’](https://www.linkedin.com/in/mircomilletari/) (Microsoft), who has been extremely helpful. And to my good friend [Matt Lee](https://www.linkedin.com/in/matthew-w-lee/) (formerly managing director at BGI/Blackrock) for long discussions about theoretical physics, RMT, quant finance, etc., for encouraging us to publish.

### Share this:

- [Twitter](https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/?share=twitter&nb=1)
- [Facebook](https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/?share=facebook&nb=1)
- [LinkedIn](https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/?share=linkedin&nb=1)
- [More](https://calculatedcontent.com/2019/12/03/towards-a-new-theory-of-learning-statistical-mechanics-of-deep-neural-networks/#)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)
Be the first to like this.

### *Related*

[Free Energies and Variational Inference](https://calculatedcontent.com/2017/09/06/free-energies-and-variational-inference/)With 21 comments

[Power Laws in Deep Learning](https://calculatedcontent.com/2018/09/09/power-laws-in-deep-learning/)With 13 comments

[Why Deep Learning Works II: the Renormalization Group](https://calculatedcontent.com/2015/04/01/why-deep-learning-works-ii-the-renormalization-group/)In "Deep Learning"

## Post navigation

[«Previous Post: This Week in Machine Learning and AI: Implicit Self-Regularization](https://calculatedcontent.com/2019/04/07/this-week-in-machine-learning-and-ai-implicit-self-regularization/)