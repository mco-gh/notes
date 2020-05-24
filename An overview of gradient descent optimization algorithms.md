An overview of gradient descent optimization algorithms

 [optimization](https://ruder.io/tag/optimization/index.html)

# An overview of gradient descent optimization algorithms

Gradient descent is the preferred way to optimize neural networks and many other machine learning algorithms but is often used as a black box. This post explores how many of the most popular gradient-based optimization algorithms such as Momentum, Adagrad, and Adam actually work.

- ![](../_resources/39267d21c9da9ff2898f3fff0163b9c3.png)

## Sebastian Ruder

Read [more posts](https://ruder.io/author/sebastian/index.html) by this author.

 [![](../_resources/39267d21c9da9ff2898f3fff0163b9c3.png)](https://ruder.io/author/sebastian/index.html)

#### [Sebastian Ruder](https://ruder.io/author/sebastian/index.html)

 19 Jan 2016  • 28 min read

 ![loss_function_image_tumblr.png](../_resources/eeae87e80c8bd5774a79040cdab7297e.png)

This post explores how many of the most popular gradient-based optimization algorithms actually work.

Note: If you are looking for a review paper, this blog post is also available as an [article on arXiv](https://arxiv.org/abs/1609.04747).

Update 20.03.2020: Added a note on [recent optimizers](https://ruder.io/optimizing-gradient-descent/index.html#otherrecentoptimizers).

Update 09.02.2018: Added [AMSGrad](https://ruder.io/optimizing-gradient-descent/index.html#amsgrad).

Update 24.11.2017: Most of the content in this article is now also available as [slides](https://www.slideshare.net/SebastianRuder/optimization-for-deep-learning).

Update 15.06.2017: Added derivations of [AdaMax](https://ruder.io/optimizing-gradient-descent/index.html#adamax) and [Nadam](https://ruder.io/optimizing-gradient-descent/index.html#nadam).

Update 21.06.16: This post was posted to Hacker News. [The discussion](https://news.ycombinator.com/item?id=11943685) provides some interesting pointers to related work and other techniques.

Table of contents:

- [Gradient descent variants](https://ruder.io/optimizing-gradient-descent/index.html#gradientdescentvariants)
    - [Batch gradient descent](https://ruder.io/optimizing-gradient-descent/index.html#batchgradientdescent)
    - [Stochastic gradient descent](https://ruder.io/optimizing-gradient-descent/index.html#stochasticgradientdescent)
    - [Mini-batch gradient descent](https://ruder.io/optimizing-gradient-descent/index.html#minibatchgradientdescent)
- [Challenges](https://ruder.io/optimizing-gradient-descent/index.html#challenges)
- [Gradient descent optimization algorithms](https://ruder.io/optimizing-gradient-descent/index.html#gradientdescentoptimizationalgorithms)
    - [Momentum](https://ruder.io/optimizing-gradient-descent/index.html#momentum)
    - [Nesterov accelerated gradient](https://ruder.io/optimizing-gradient-descent/index.html#nesterovacceleratedgradient)
    - [Adagrad](https://ruder.io/optimizing-gradient-descent/index.html#adagrad)
    - [Adadelta](https://ruder.io/optimizing-gradient-descent/index.html#adadelta)
    - [RMSprop](https://ruder.io/optimizing-gradient-descent/index.html#rmsprop)
    - [Adam](https://ruder.io/optimizing-gradient-descent/index.html#adam)
    - [AdaMax](https://ruder.io/optimizing-gradient-descent/index.html#adamax)
    - [Nadam](https://ruder.io/optimizing-gradient-descent/index.html#nadam)
    - [AMSGrad](https://ruder.io/optimizing-gradient-descent/index.html#amsgrad)
    - [Other recent optimizers](https://ruder.io/optimizing-gradient-descent/index.html#otherrecentoptimizers)
    - [Visualization of algorithms](https://ruder.io/optimizing-gradient-descent/index.html#visualizationofalgorithms)
    - [Which optimizer to use?](https://ruder.io/optimizing-gradient-descent/index.html#whichoptimizertouse)
- [Parallelizing and distributing SGD](https://ruder.io/optimizing-gradient-descent/index.html#parallelizinganddistributingsgd)
    - [Hogwild!](https://ruder.io/optimizing-gradient-descent/index.html#hogwild)
    - [Downpour SGD](https://ruder.io/optimizing-gradient-descent/index.html#downpoursgd)
    - [Delay-tolerant Algorithms for SGD](https://ruder.io/optimizing-gradient-descent/index.html#delaytolerantalgorithmsforsgd)
    - [TensorFlow](https://ruder.io/optimizing-gradient-descent/index.html#tensorflow)
    - [Elastic Averaging SGD](https://ruder.io/optimizing-gradient-descent/index.html#elasticaveragingsgd)
- [Additional strategies for optimizing SGD](https://ruder.io/optimizing-gradient-descent/index.html#additionalstrategiesforoptimizingsgd)
    - [Shuffling and Curriculum Learning](https://ruder.io/optimizing-gradient-descent/index.html#shufflingandcurriculumlearning)
    - [Batch normalization](https://ruder.io/optimizing-gradient-descent/index.html#batchnormalization)
    - [Early Stopping](https://ruder.io/optimizing-gradient-descent/index.html#earlystopping)
    - [Gradient noise](https://ruder.io/optimizing-gradient-descent/index.html#gradientnoise)
- [Conclusion](https://ruder.io/optimizing-gradient-descent/index.html#conclusion)
- [References](https://ruder.io/optimizing-gradient-descent/index.html#references)

Gradient descent is one of the most popular algorithms to perform optimization and by far the most common way to optimize neural networks. At the same time, every state-of-the-art Deep Learning library contains implementations of various algorithms to optimize gradient descent (e.g. [lasagne's](https://lasagne.readthedocs.org/en/latest/modules/updates.html), [caffe's](http://caffe.berkeleyvision.org/tutorial/solver.html), and [keras'](http://keras.io/optimizers/) documentation). These algorithms, however, are often used as black-box optimizers, as practical explanations of their strengths and weaknesses are hard to come by.

This blog post aims at providing you with intuitions towards the behaviour of different algorithms for optimizing gradient descent that will help you put them to use. We are first going to look at the different variants of gradient descent. We will then briefly summarize challenges during training. Subsequently, we will introduce the most common optimization algorithms by showing their motivation to resolve these challenges and how this leads to the derivation of their update rules. We will also take a short look at algorithms and architectures to optimize gradient descent in a parallel and distributed setting. Finally, we will consider additional strategies that are helpful for optimizing gradient descent.

Gradient descent is a way to minimize an objective function J(θ)J(θ) parameterized by a model's parameters θ∈Rdθ∈Rd by updating the parameters in the opposite direction of the gradient of the objective function ∇θJ(θ)∇θJ(θ) w.r.t. to the parameters. The learning rate ηη determines the size of the steps we take to reach a (local) minimum. In other words, we follow the direction of the slope of the surface created by the objective function downhill until we reach a valley. If you are unfamiliar with gradient descent, you can find a good introduction on optimizing neural networks [here](https://cs231n.github.io/optimization-1/).

# Gradient descent variants

There are three variants of gradient descent, which differ in how much data we use to compute the gradient of the objective function. Depending on the amount of data, we make a trade-off between the accuracy of the parameter update and the time it takes to perform an update.

## Batch gradient descent

Vanilla gradient descent, aka batch gradient descent, computes the gradient of the cost function w.r.t. to the parameters θθ for the entire training dataset:

θ=θ−η⋅∇θJ(θ)θ=θ−η⋅∇θJ(θ).

As we need to calculate the gradients for the whole dataset to perform just *one* update, batch gradient descent can be very slow and is intractable for datasets that don't fit in memory. Batch gradient descent also doesn't allow us to update our model *online*, i.e. with new examples on-the-fly.

In code, batch gradient descent looks something like this:

	for i in range(nb_epochs):
	  params_grad = evaluate_gradient(loss_function, data, params)
	  params = params - learning_rate * params_grad

For a pre-defined number of epochs, we first compute the gradient vector `params_grad` of the loss function for the whole dataset w.r.t. our parameter vector `params`. Note that state-of-the-art deep learning libraries provide automatic differentiation that efficiently computes the gradient w.r.t. some parameters. If you derive the gradients yourself, then gradient checking is a good idea. (See [here](https://cs231n.github.io/neural-networks-3/) for some great tips on how to check gradients properly.)

We then update our parameters in the opposite direction of the gradients with the learning rate determining how big of an update we perform. Batch gradient descent is guaranteed to converge to the global minimum for convex error surfaces and to a local minimum for non-convex surfaces.

## Stochastic gradient descent

Stochastic gradient descent (SGD) in contrast performs a parameter update for *each* training example x(i)x(i) and label y(i)y(i):

θ=θ−η⋅∇θJ(θ;x(i);y(i))θ=θ−η⋅∇θJ(θ;x(i);y(i)).

Batch gradient descent performs redundant computations for large datasets, as it recomputes gradients for similar examples before each parameter update. SGD does away with this redundancy by performing one update at a time. It is therefore usually much faster and can also be used to learn online.

SGD performs frequent updates with a high variance that cause the objective function to fluctuate heavily as in Image 1.

 ![](../_resources/036efac99f9c1729a178cd0fe279679c.png)

Image 1: SGD fluctuation (Source: [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/f/f3/Stogra.png))

While batch gradient descent converges to the minimum of the basin the parameters are placed in, SGD's fluctuation, on the one hand, enables it to jump to new and potentially better local minima. On the other hand, this ultimately complicates convergence to the exact minimum, as SGD will keep overshooting. However, it has been shown that when we slowly decrease the learning rate, SGD shows the same convergence behaviour as batch gradient descent, almost certainly converging to a local or the global minimum for non-convex and convex optimization respectively.

Its code fragment simply adds a loop over the training examples and evaluates the gradient w.r.t. each example. Note that we shuffle the training data at every epoch as explained in [this section](https://ruder.io/optimizing-gradient-descent/index.html#shufflingandcurriculumlearning).

	for i in range(nb_epochs):
	  np.random.shuffle(data)
	  for example in data:
	    params_grad = evaluate_gradient(loss_function, example, params)
	    params = params - learning_rate * params_grad

## Mini-batch gradient descent

Mini-batch gradient descent finally takes the best of both worlds and performs an update for every mini-batch of nn training examples:

θ=θ−η⋅∇θJ(θ;x(i:i+n);y(i:i+n))θ=θ−η⋅∇θJ(θ;x(i:i+n);y(i:i+n)).

This way, it *a)* reduces the variance of the parameter updates, which can lead to more stable convergence; and *b)* can make use of highly optimized matrix optimizations common to state-of-the-art deep learning libraries that make computing the gradient w.r.t. a mini-batch very efficient. Common mini-batch sizes range between 50 and 256, but can vary for different applications. Mini-batch gradient descent is typically the algorithm of choice when training a neural network and the term SGD usually is employed also when mini-batches are used. Note: In modifications of SGD in the rest of this post, we leave out the parameters x(i:i+n);y(i:i+n)x(i:i+n);y(i:i+n) for simplicity.

In code, instead of iterating over examples, we now iterate over mini-batches of size 50:

	for i in range(nb_epochs):
	  np.random.shuffle(data)
	  for batch in get_batches(data, batch_size=50):
	    params_grad = evaluate_gradient(loss_function, batch, params)
	    params = params - learning_rate * params_grad

# Challenges

Vanilla mini-batch gradient descent, however, does not guarantee good convergence, but offers a few challenges that need to be addressed:

- Choosing a proper learning rate can be difficult. A learning rate that is too small leads to painfully slow convergence, while a learning rate that is too large can hinder convergence and cause the loss function to fluctuate around the minimum or even to diverge.
- Learning rate schedules [[1]](https://ruder.io/optimizing-gradient-descent/index.html#fn1) try to adjust the learning rate during training by e.g. annealing, i.e. reducing the learning rate according to a pre-defined schedule or when the change in objective between epochs falls below a threshold. These schedules and thresholds, however, have to be defined in advance and are thus unable to adapt to a dataset's characteristics [[2]](https://ruder.io/optimizing-gradient-descent/index.html#fn2).
- Additionally, the same learning rate applies to all parameter updates. If our data is sparse and our features have very different frequencies, we might not want to update all of them to the same extent, but perform a larger update for rarely occurring features.
- Another key challenge of minimizing highly non-convex error functions common for neural networks is avoiding getting trapped in their numerous suboptimal local minima. Dauphin et al. [[3]](https://ruder.io/optimizing-gradient-descent/index.html#fn3) argue that the difficulty arises in fact not from local minima but from saddle points, i.e. points where one dimension slopes up and another slopes down. These saddle points are usually surrounded by a plateau of the same error, which makes it notoriously hard for SGD to escape, as the gradient is close to zero in all dimensions.

# Gradient descent optimization algorithms

In the following, we will outline some algorithms that are widely used by the deep learning community to deal with the aforementioned challenges. We will not discuss algorithms that are infeasible to compute in practice for high-dimensional data sets, e.g. second-order methods such as [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization).

## Momentum

SGD has trouble navigating ravines, i.e. areas where the surface curves much more steeply in one dimension than in another [[4]](https://ruder.io/optimizing-gradient-descent/index.html#fn4), which are common around local optima. In these scenarios, SGD oscillates across the slopes of the ravine while only making hesitant progress along the bottom towards the local optimum as in Image 2.

|     |     |
| --- | --- |
|  ![without_momentum.gif](../_resources/2476080e4cdfd489ae64ae3ceeafe48b.gif)<br>Image 2: SGD without momentum |  ![with_momentum.gif](../_resources/b9388fd6e465d82687680f9d16edcd2b.gif)<br>Image 3: SGD with momentum |

Momentum [[5]](https://ruder.io/optimizing-gradient-descent/index.html#fn5) is a method that helps accelerate SGD in the relevant direction and dampens oscillations as can be seen in Image 3. It does this by adding a fraction γγ of the update vector of the past time step to the current update vector:

vt=γvt−1+η∇θJ(θ)θ=θ−vtvt=γvt−1+η∇θJ(θ)θ=θ−vt

Note: Some implementations exchange the signs in the equations. The momentum term γγ is usually set to 0.9 or a similar value.

Essentially, when using momentum, we push a ball down a hill. The ball accumulates momentum as it rolls downhill, becoming faster and faster on the way (until it reaches its terminal velocity if there is air resistance, i.e. γ<1γ<1). The same thing happens to our parameter updates: The momentum term increases for dimensions whose gradients point in the same directions and reduces updates for dimensions whose gradients change directions. As a result, we gain faster convergence and reduced oscillation.

# Nesterov accelerated gradient

However, a ball that rolls down a hill, blindly following the slope, is highly unsatisfactory. We'd like to have a smarter ball, a ball that has a notion of where it is going so that it knows to slow down before the hill slopes up again.

Nesterov accelerated gradient (NAG) [[6]](https://ruder.io/optimizing-gradient-descent/index.html#fn6) is a way to give our momentum term this kind of prescience. We know that we will use our momentum term γvt−1γvt−1 to move the parameters θθ. Computing θ−γvt−1θ−γvt−1 thus gives us an approximation of the next position of the parameters (the gradient is missing for the full update), a rough idea where our parameters are going to be. We can now effectively look ahead by calculating the gradient not w.r.t. to our current parameters θθ but w.r.t. the approximate future position of our parameters:

vt=γvt−1+η∇θJ(θ−γvt−1)θ=θ−vtvt=γvt−1+η∇θJ(θ−γvt−1)θ=θ−vt

Again, we set the momentum term γγ to a value of around 0.9. While Momentum first computes the current gradient (small blue vector in Image 4) and then takes a big jump in the direction of the updated accumulated gradient (big blue vector), NAG first makes a big jump in the direction of the previous accumulated gradient (brown vector), measures the gradient and then makes a correction (red vector), which results in the complete NAG update (green vector). This anticipatory update prevents us from going too fast and results in increased responsiveness, which has significantly increased the performance of RNNs on a number of tasks [[7]](https://ruder.io/optimizing-gradient-descent/index.html#fn7).

 ![](../_resources/b49bb6001f3c28798f240d64340ac226.png)

Image 4: Nesterov update (Source: [G. Hinton's lecture 6c](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf))

Refer to [here](https://cs231n.github.io/neural-networks-3/) for another explanation about the intuitions behind NAG, while Ilya Sutskever gives a more detailed overview in his PhD thesis [[8]](https://ruder.io/optimizing-gradient-descent/index.html#fn8).

Now that we are able to adapt our updates to the slope of our error function and speed up SGD in turn, we would also like to adapt our updates to each individual parameter to perform larger or smaller updates depending on their importance.

## Adagrad

Adagrad [[9]](https://ruder.io/optimizing-gradient-descent/index.html#fn9) is an algorithm for gradient-based optimization that does just this: It adapts the learning rate to the parameters, performing smaller updates

(i.e. low learning rates) for parameters associated with frequently occurring features, and larger updates (i.e. high learning rates) for parameters associated with infrequent features. For this reason, it is well-suited for dealing with sparse data. Dean et al. [[10]](https://ruder.io/optimizing-gradient-descent/index.html#fn10) have found that Adagrad greatly improved the robustness of SGD and used it for training large-scale neural nets at Google, which -- among other things -- learned to [recognize cats in Youtube videos](https://www.wired.com/2012/06/google-x-neural-network/). Moreover, Pennington et al. [[11]](https://ruder.io/optimizing-gradient-descent/index.html#fn11) used Adagrad to train GloVe word embeddings, as infrequent words require much larger updates than frequent ones.

Previously, we performed an update for all parameters θθ at once as every parameter θiθi used the same learning rate ηη. As Adagrad uses a different learning rate for every parameter θiθi at every time step tt, we first show Adagrad's per-parameter update, which we then vectorize. For brevity, we use gtgt to denote the gradient at time step tt. gt,igt,i is then the partial derivative of the objective function w.r.t. to the parameter θiθi at time step tt:

gt,i=∇θJ(θt,i)gt,i=∇θJ(θt,i).
The SGD update for every parameter θiθi at each time step tt then becomes:
θt+1,i=θt,i−η⋅gt,iθt+1,i=θt,i−η⋅gt,i.

In its update rule, Adagrad modifies the general learning rate ηη at each time step tt for every parameter θiθi based on the past gradients that have been computed for θiθi:

θt+1,i=θt,i−η√Gt,ii+ϵ⋅gt,iθt+1,i=θt,i−ηGt,ii+ϵ⋅gt,i.

Gt∈Rd×dGt∈Rd×d here is a diagonal matrix where each diagonal element i,ii,i is the sum of the squares of the gradients w.r.t. θiθi up to time step tt  [[12]](https://ruder.io/optimizing-gradient-descent/index.html#fn12), while ϵϵ is a smoothing term that avoids division by zero (usually on the order of 1e−81e−8). Interestingly, without the square root operation, the algorithm performs much worse.

As GtGt contains the sum of the squares of the past gradients w.r.t. to all parameters θθ along its diagonal, we can now vectorize our implementation by performing a matrix-vector product ⊙⊙ between GtGt and gtgt:

θt+1=θt−η√Gt+ϵ⊙gtθt+1=θt−ηGt+ϵ⊙gt.

One of Adagrad's main benefits is that it eliminates the need to manually tune the learning rate. Most implementations use a default value of 0.01 and leave it at that.

Adagrad's main weakness is its accumulation of the squared gradients in the denominator: Since every added term is positive, the accumulated sum keeps growing during training. This in turn causes the learning rate to shrink and eventually become infinitesimally small, at which point the algorithm is no longer able to acquire additional knowledge. The following algorithms aim to resolve this flaw.

## Adadelta

Adadelta [[13]](https://ruder.io/optimizing-gradient-descent/index.html#fn13) is an extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing learning rate. Instead of accumulating all past squared gradients, Adadelta restricts the window of accumulated past gradients to some fixed size ww.

Instead of inefficiently storing ww previous squared gradients, the sum of gradients is recursively defined as a decaying average of all past squared gradients. The running average E[g2]tE[g2]t at time step tt then depends (as a fraction γγ similarly to the Momentum term) only on the previous average and the current gradient:

E[g2]t=γE[g2]t−1+(1−γ)g2tE[g2]t=γE[g2]t−1+(1−γ)gt2.

We set γγ to a similar value as the momentum term, around 0.9. For clarity, we now rewrite our vanilla SGD update in terms of the parameter update vector ΔθtΔθt:

Δθt=−η⋅gt,iθt+1=θt+ΔθtΔθt=−η⋅gt,iθt+1=θt+Δθt

The parameter update vector of Adagrad that we derived previously thus takes the form:

Δθt=−η√Gt+ϵ⊙gtΔθt=−ηGt+ϵ⊙gt.

We now simply replace the diagonal matrix GtGt with the decaying average over past squared gradients E[g2]tE[g2]t:

Δθt=−η√E[g2]t+ϵgtΔθt=−ηE[g2]t+ϵgt.

As the denominator is just the root mean squared (RMS) error criterion of the gradient, we can replace it with the criterion short-hand:

Δθt=−ηRMS[g]tgtΔθt=−ηRMS[g]tgt.

The authors note that the units in this update (as well as in SGD, Momentum, or Adagrad) do not match, i.e. the update should have the same hypothetical units as the parameter. To realize this, they first define another exponentially decaying average, this time not of squared gradients but of squared parameter updates:

E[Δθ2]t=γE[Δθ2]t−1+(1−γ)Δθ2tE[Δθ2]t=γE[Δθ2]t−1+(1−γ)Δθt2.
The root mean squared error of parameter updates is thus:
RMS[Δθ]t=√E[Δθ2]t+ϵRMS[Δθ]t=E[Δθ2]t+ϵ.

Since RMS[Δθ]tRMS[Δθ]t is unknown, we approximate it with the RMS of parameter updates until the previous time step. Replacing the learning rate ηη in the previous update rule with RMS[Δθ]t−1RMS[Δθ]t−1 finally yields the Adadelta update rule:

Δθt=−RMS[Δθ]t−1RMS[g]tgtθt+1=θt+ΔθtΔθt=−RMS[Δθ]t−1RMS[g]tgtθt+1=θt+Δθt

With Adadelta, we do not even need to set a default learning rate, as it has been eliminated from the update rule.

## RMSprop

RMSprop is an unpublished, adaptive learning rate method proposed by Geoff Hinton in [Lecture 6e of his Coursera Class](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf).

RMSprop and Adadelta have both been developed independently around the same time stemming from the need to resolve Adagrad's radically diminishing learning rates. RMSprop in fact is identical to the first update vector of Adadelta that we derived above:

E[g2]t=0.9E[g2]t−1+0.1g2tθt+1=θt−η√E[g2]t+ϵgtE[g2]t=0.9E[g2]t−1+0.1gt2θt+1=θt−ηE[g2]t+ϵgt

RMSprop as well divides the learning rate by an exponentially decaying average of squared gradients. Hinton suggests γγ to be set to 0.9, while a good default value for the learning rate ηη is 0.001.

## Adam

Adaptive Moment Estimation (Adam) [[14]](https://ruder.io/optimizing-gradient-descent/index.html#fn14) is another method that computes adaptive learning rates for each parameter. In addition to storing an exponentially decaying average of past squared gradients vtvt like Adadelta and RMSprop, Adam also keeps an exponentially decaying average of past gradients mtmt, similar to momentum. Whereas momentum can be seen as a ball running down a slope, Adam behaves like a heavy ball with friction, which thus prefers flat minima in the error surface [[15]](https://ruder.io/optimizing-gradient-descent/index.html#fn15). We compute the decaying averages of past and past squared gradients mtmt and vtvt respectively as follows:

mt=β1mt−1+(1−β1)gtvt=β2vt−1+(1−β2)g2tmt=β1mt−1+(1−β1)gtvt=β2vt−1+(1−β2)gt2

mtmt and vtvt are estimates of the first moment (the mean) and the second moment (the uncentered variance) of the gradients respectively, hence the name of the method. As mtmt and vtvt are initialized as vectors of 0's, the authors of Adam observe that they are biased towards zero, especially during the initial time steps, and especially when the decay rates are small (i.e. β1β1 and β2β2 are close to 1).

They counteract these biases by computing bias-corrected first and second moment estimates:

^mt=mt1−βt1^vt=vt1−βt2m^t=mt1−β1tv^t=vt1−β2t

They then use these to update the parameters just as we have seen in Adadelta and RMSprop, which yields the Adam update rule:

θt+1=θt−η√^vt+ϵ^mtθt+1=θt−ηv^t+ϵm^t.

The authors propose default values of 0.9 for β1β1, 0.999 for β2β2, and 10−810−8 for ϵϵ. They show empirically that Adam works well in practice and compares favorably to other adaptive learning-method algorithms.

## AdaMax

The vtvt factor in the Adam update rule scales the gradient inversely proportionally to the ℓ2ℓ2 norm of the past gradients (via the vt−1vt−1 term) and current gradient |gt|2|gt|2:

vt=β2vt−1+(1−β2)|gt|2vt=β2vt−1+(1−β2)|gt|2

We can generalize this update to the ℓpℓp norm. Note that Kingma and Ba also parameterize β2β2 as βp2β2p:

vt=βp2vt−1+(1−βp2)|gt|pvt=β2pvt−1+(1−β2p)|gt|p

Norms for large pp values generally become numerically unstable, which is why ℓ1ℓ1 and ℓ2ℓ2 norms are most common in practice. However, ℓ∞ℓ∞ also generally exhibits stable behavior. For this reason, the authors propose AdaMax (Kingma and Ba, 2015) and show that vtvt with ℓ∞ℓ∞ converges to the following more stable value. To avoid confusion with Adam, we use utut to denote the infinity norm-constrained vtvt:

ut=β∞2vt−1+(1−β∞2)|gt|∞=max(β2⋅vt−1,|gt|)ut=β2∞vt−1+(1−β2∞)|gt|∞=max(β2⋅vt−1,|gt|)

We can now plug this into the Adam update equation by replacing √^vt+ϵv^t+ϵ with utut to obtain the AdaMax update rule:

θt+1=θt−ηut^mtθt+1=θt−ηutm^t

Note that as utut relies on the maxmax operation, it is not as suggestible to bias towards zero as mtmt and vtvt in Adam, which is why we do not need to compute a bias correction for utut. Good default values are again η=0.002η=0.002, β1=0.9β1=0.9, and β2=0.999β2=0.999.

## Nadam

As we have seen before, Adam can be viewed as a combination of RMSprop and momentum: RMSprop contributes the exponentially decaying average of past squared gradients vtvt, while momentum accounts for the exponentially decaying average of past gradients mtmt. We have also seen that Nesterov accelerated gradient (NAG) is superior to vanilla momentum.

Nadam (Nesterov-accelerated Adaptive Moment Estimation) [[16]](https://ruder.io/optimizing-gradient-descent/index.html#fn16) thus combines Adam and NAG. In order to incorporate NAG into Adam, we need to modify its momentum term mtmt.

First, let us recall the momentum update rule using our current notation :
gt=∇θtJ(θt)mt=γmt−1+ηgtθt+1=θt−mtgt=∇θtJ(θt)mt=γmt−1+ηgtθt+1=θt−mt

where JJ is our objective function, γγ is the momentum decay term, and ηη is our step size. Expanding the third equation above yields:

θt+1=θt−(γmt−1+ηgt)θt+1=θt−(γmt−1+ηgt)

This demonstrates again that momentum involves taking a step in the direction of the previous momentum vector and a step in the direction of the current gradient.

NAG then allows us to perform a more accurate step in the gradient direction by updating the parameters with the momentum step *before* computing the gradient. We thus only need to modify the gradient gtgt to arrive at NAG:

gt=∇θtJ(θt−γmt−1)mt=γmt−1+ηgtθt+1=θt−mtgt=∇θtJ(θt−γmt−1)mt=γmt−1+ηgtθt+1=θt−mt

Dozat proposes to modify NAG the following way: Rather than applying the momentum step twice -- one time for updating the gradient gtgt and a second time for updating the parameters θt+1θt+1 -- we now apply the look-ahead momentum vector directly to update the current parameters:

gt=∇θtJ(θt)mt=γmt−1+ηgtθt+1=θt−(γmt+ηgt)gt=∇θtJ(θt)mt=γmt−1+ηgtθt+1=θt−(γmt+ηgt)

Notice that rather than utilizing the previous momentum vector mt−1mt−1 as in the equation of the expanded momentum update rule above, we now use the current momentum vector mtmt to look ahead. In order to add Nesterov momentum to Adam, we can thus similarly replace the previous momentum vector with the current momentum vector. First, recall that the Adam update rule is the following (note that we do not need to modify ^vtv^t):

mt=β1mt−1+(1−β1)gt^mt=mt1−βt1θt+1=θt−η√^vt+ϵ^mtmt=β1mt−1+(1−β1)gtm^t=mt1−β1tθt+1=θt−ηv^t+ϵm^t

Expanding the second equation with the definitions of ^mtm^t and mtmt in turn gives us:

θt+1=θt−η√^vt+ϵ(β1mt−11−βt1+(1−β1)gt1−βt1)θt+1=θt−ηv^t+ϵ(β1mt−11−β1t+(1−β1)gt1−β1t)

Note that β1mt−11−βt1β1mt−11−β1t is just the bias-corrected estimate of the momentum vector of the previous time step. We can thus replace it with ^mt−1m^t−1:

θt+1=θt−η√^vt+ϵ(β1^mt−1+(1−β1)gt1−βt1)θt+1=θt−ηv^t+ϵ(β1m^t−1+(1−β1)gt1−β1t)

Note that for simplicity, we ignore that the denominator is 1−βt11−β1t and not 1−βt−111−β1t−1 as we will replace the denominator in the next step anyway. This equation again looks very similar to our expanded momentum update rule above. We can now add Nesterov momentum just as we did previously by simply replacing this bias-corrected estimate of the momentum vector of the previous time step ^mt−1m^t−1 with the bias-corrected estimate of the current momentum vector ^mtm^t, which gives us the Nadam update rule:

θt+1=θt−η√^vt+ϵ(β1^mt+(1−β1)gt1−βt1)θt+1=θt−ηv^t+ϵ(β1m^t+(1−β1)gt1−β1t)

## AMSGrad

As adaptive learning rate methods have become the norm in training neural networks, practitioners noticed that in some cases, e.g. for object recognition [[17]](https://ruder.io/optimizing-gradient-descent/index.html#fn17) or machine translation [[18]](https://ruder.io/optimizing-gradient-descent/index.html#fn18) they fail to converge to an optimal solution and are outperformed by SGD with momentum.

Reddi et al. (2018) [[19]](https://ruder.io/optimizing-gradient-descent/index.html#fn19) formalize this issue and pinpoint the exponential moving average of past squared gradients as a reason for the poor generalization behaviour of adaptive learning rate methods. Recall that the introduction of the exponential average was well-motivated: It should prevent the learning rates to become infinitesimally small as training progresses, the key flaw of the Adagrad algorithm. However, this short-term memory of the gradients becomes an obstacle in other scenarios.

In settings where Adam converges to a suboptimal solution, it has been observed that some minibatches provide large and informative gradients, but as these minibatches only occur rarely, exponential averaging diminishes their influence, which leads to poor convergence. The authors provide an example for a simple convex optimization problem where the same behaviour can be observed for Adam.

To fix this behaviour, the authors propose a new algorithm, AMSGrad that uses the maximum of past squared gradients vtvt rather than the exponential average to update the parameters. vtvt is defined the same as in Adam above:

vt=β2vt−1+(1−β2)g2tvt=β2vt−1+(1−β2)gt2

Instead of using vtvt (or its bias-corrected version ^vtv^t) directly, we now employ the previous vt−1vt−1 if it is larger than the current one:

^vt=max(^vt−1,vt)v^t=max(v^t−1,vt)

This way, AMSGrad results in a non-increasing step size, which avoids the problems suffered by Adam. For simplicity, the authors also remove the debiasing step that we have seen in Adam. The full AMSGrad update without bias-corrected estimates can be seen below:

mt=β1mt−1+(1−β1)gtvt=β2vt−1+(1−β2)g2t^vt=max(^vt−1,vt)θt+1=θt−η√^vt+ϵmtmt=β1mt−1+(1−β1)gtvt=β2vt−1+(1−β2)gt2v^t=max(v^t−1,vt)θt+1=θt−ηv^t+ϵmt

The authors observe improved performance compared to Adam on small datasets and on CIFAR-10. [Other experiments](https://fdlm.github.io/post/amsgrad/), however, show similar or worse performance than Adam. It remains to be seen whether AMSGrad is able to consistently outperform Adam in practice. For more information about recent advances in Deep Learning optimization, refer to [this blog post](https://ruder.io/deep-learning-optimization-2017/).

## Other recent optimizers

A number of other optimizers have been proposed after AMSGrad. These include AdamW [[20]](https://ruder.io/optimizing-gradient-descent/index.html#fn20), which fixes weight decay in Adam; QHAdam [[21]](https://ruder.io/optimizing-gradient-descent/index.html#fn21), which averages a standard SGD step with a momentum SGD step; and AggMo [[22]](https://ruder.io/optimizing-gradient-descent/index.html#fn22), which combines multiple momentum terms γγ; and others. For an overview of recent gradient descent algorithms, have a look at [this blog post](https://johnchenresearch.github.io/demon/).

## Visualization of algorithms

The following two animations (Image credit: [Alec Radford](https://twitter.com/alecrad)) provide some intuitions towards the optimization behaviour of most of the presented optimization methods. Also have a look [here](https://cs231n.github.io/neural-networks-3/) for a description of the same images by Karpathy and another concise overview of the algorithms discussed.

In Image 5, we see their behaviour on the contours of a loss surface ([the Beale function](https://www.sfu.ca/~ssurjano/beale.html)) over time. Note that Adagrad, Adadelta, and RMSprop almost immediately head off in the right direction and converge similarly fast, while Momentum and NAG are led off-track, evoking the image of a ball rolling down the hill. NAG, however, is quickly able to correct its course due to its increased responsiveness by looking ahead and heads to the minimum.

Image 6 shows the behaviour of the algorithms at a saddle point, i.e. a point where one dimension has a positive slope, while the other dimension has a negative slope, which pose a difficulty for SGD as we mentioned before. Notice here that SGD, Momentum, and NAG find it difficulty to break symmetry, although the two latter eventually manage to escape the saddle point, while Adagrad, RMSprop, and Adadelta quickly head down the negative slope.

|     |     |
| --- | --- |
|  ![contours_evaluation_optimizers.gif](../_resources/5d5166a3d3712e7c03af74b1ccacbeac.gif)<br>Image 5: SGD optimization on loss surface contours |  ![saddle_point_evaluation_optimizers.gif](../_resources/4a3b4a39ab8e5c556359147b882b4788.gif)<br>Image 6: SGD optimization on saddle point |

As we can see, the adaptive learning-rate methods, i.e. Adagrad, Adadelta, RMSprop, and Adam are most suitable and provide the best convergence for these scenarios.

Note: If you are interested in visualizing these or other optimization algorithms, refer to [this useful tutorial](http://louistiao.me/notes/visualizing-and-animating-optimization-algorithms-with-matplotlib/).

## Which optimizer to use?

So, which optimizer should you now use? If your input data is sparse, then you likely achieve the best results using one of the adaptive learning-rate methods. An additional benefit is that you won't need to tune the learning rate but likely achieve the best results with the default value.

In summary, RMSprop is an extension of Adagrad that deals with its radically diminishing learning rates. It is identical to Adadelta, except that Adadelta uses the RMS of parameter updates in the numinator update rule. Adam, finally, adds bias-correction and momentum to RMSprop. Insofar, RMSprop, Adadelta, and Adam are very similar algorithms that do well in similar circumstances. Kingma et al. [[14:1]](https://ruder.io/optimizing-gradient-descent/index.html#fn14) show that its bias-correction helps Adam slightly outperform RMSprop towards the end of optimization as gradients become sparser. Insofar, Adam might be the best overall choice.

Interestingly, many recent papers use vanilla SGD without momentum and a simple learning rate annealing schedule. As has been shown, SGD usually achieves to find a minimum, but it might take significantly longer than with some of the optimizers, is much more reliant on a robust initialization and annealing schedule, and may get stuck in saddle points rather than local minima. Consequently, if you care about fast convergence and train a deep or complex neural network, you should choose one of the adaptive learning rate methods.

# Parallelizing and distributing SGD

Given the ubiquity of large-scale data solutions and the availability of low-commodity clusters, distributing SGD to speed it up further is an obvious choice.

SGD by itself is inherently sequential: Step-by-step, we progress further towards the minimum. Running it provides good convergence but can be slow particularly on large datasets. In contrast, running SGD asynchronously is faster, but suboptimal communication between workers can lead to poor convergence. Additionally, we can also parallelize SGD on one machine without the need for a large computing cluster. The following are algorithms and architectures that have been proposed to optimize parallelized and distributed SGD.

## Hogwild!

Niu et al. [[23]](https://ruder.io/optimizing-gradient-descent/index.html#fn23) introduce an update scheme called Hogwild! that allows performing SGD updates in parallel on CPUs. Processors are allowed to access shared memory without locking the parameters. This only works if the input data is sparse, as each update will only modify a fraction of all parameters. They show that in this case, the update scheme achieves almost an optimal rate of convergence, as it is unlikely that processors will overwrite useful information.

## Downpour SGD

Downpour SGD is an asynchronous variant of SGD that was used by Dean et al. [[10:1]](https://ruder.io/optimizing-gradient-descent/index.html#fn10) in their DistBelief framework (predecessor to TensorFlow) at Google. It runs multiple replicas of a model in parallel on subsets of the training data. These models send their updates to a parameter server, which is split across many machines. Each machine is responsible for storing and updating a fraction of the model's parameters. However, as replicas don't communicate with each other e.g. by sharing weights or updates, their parameters are continuously at risk of diverging, hindering convergence.

## Delay-tolerant Algorithms for SGD

McMahan and Streeter [[24]](https://ruder.io/optimizing-gradient-descent/index.html#fn24) extend AdaGrad to the parallel setting by developing delay-tolerant algorithms that not only adapt to past gradients, but also to the update delays. This has been shown to work well in practice.

## TensorFlow

[TensorFlow](https://www.tensorflow.org/)  [[25]](https://ruder.io/optimizing-gradient-descent/index.html#fn25) is Google's recently open-sourced framework for the implementation and deployment of large-scale machine learning models. It is based on their experience with DistBelief and is already used internally to perform computations on a large range of mobile devices as well as on large-scale distributed systems. For distributed execution, a computation graph is split into a subgraph for every device and communication takes place using Send/Receive node pairs. However, the open source version of TensorFlow currently does not support distributed functionality (see [here](https://github.com/tensorflow/tensorflow/issues/23)).

Update 13.04.16: A distributed version of TensorFlow has [been released](https://googleresearch.blogspot.ie/2016/04/announcing-tensorflow-08-now-with.html).

## Elastic Averaging SGD

Zhang et al. [[26]](https://ruder.io/optimizing-gradient-descent/index.html#fn26) propose Elastic Averaging SGD (EASGD), which links the parameters of the workers of asynchronous SGD with an elastic force, i.e. a center variable stored by the parameter server. This allows the local variables to fluctuate further from the center variable, which in theory allows for more exploration of the parameter space. They show empirically that this increased capacity for exploration leads to improved performance by finding new local optima.

# Additional strategies for optimizing SGD

Finally, we introduce additional strategies that can be used alongside any of the previously mentioned algorithms to further improve the performance of SGD. For a great overview of some other common tricks, refer to [[27]](https://ruder.io/optimizing-gradient-descent/index.html#fn27).

## Shuffling and Curriculum Learning

Generally, we want to avoid providing the training examples in a meaningful order to our model as this may bias the optimization algorithm. Consequently, it is often a good idea to shuffle the training data after every epoch.

On the other hand, for some cases where we aim to solve progressively harder problems, supplying the training examples in a meaningful order may actually lead to improved performance and better convergence. The method for establishing this meaningful order is called Curriculum Learning [[28]](https://ruder.io/optimizing-gradient-descent/index.html#fn28).

Zaremba and Sutskever [[29]](https://ruder.io/optimizing-gradient-descent/index.html#fn29) were only able to train LSTMs to evaluate simple programs using Curriculum Learning and show that a combined or mixed strategy is better than the naive one, which sorts examples by increasing difficulty.

## Batch normalization

To facilitate learning, we typically normalize the initial values of our parameters by initializing them with zero mean and unit variance. As training progresses and we update parameters to different extents, we lose this normalization, which slows down training and amplifies changes as the network becomes deeper.

Batch normalization [[30]](https://ruder.io/optimizing-gradient-descent/index.html#fn30) reestablishes these normalizations for every mini-batch and changes are back-propagated through the operation as well. By making normalization part of the model architecture, we are able to use higher learning rates and pay less attention to the initialization parameters. Batch normalization additionally acts as a regularizer, reducing (and sometimes even eliminating) the need for Dropout.

## Early stopping

According to Geoff Hinton: "*Early stopping (is) beautiful free lunch*" ([NIPS 2015 Tutorial slides](http://www.iro.umontreal.ca/~bengioy/talks/DL-Tutorial-NIPS2015.pdf), slide 63). You should thus always monitor error on a validation set during training and stop (with some patience) if your validation error does not improve enough.

## Gradient noise

Neelakantan et al. [[31]](https://ruder.io/optimizing-gradient-descent/index.html#fn31) add noise that follows a Gaussian distribution N(0,σ2t)N(0,σt2) to each gradient update:

gt,i=gt,i+N(0,σ2t)gt,i=gt,i+N(0,σt2).
They anneal the variance according to the following schedule:
σ2t=η(1+t)γσt2=η(1+t)γ.

They show that adding this noise makes networks more robust to poor initialization and helps training particularly deep and complex networks. They suspect that the added noise gives the model more chances to escape and find new local minima, which are more frequent for deeper models.

# Conclusion

In this blog post, we have initially looked at the three variants of gradient descent, among which mini-batch gradient descent is the most popular. We have then investigated algorithms that are most commonly used for optimizing SGD: Momentum, Nesterov accelerated gradient, Adagrad, Adadelta, RMSprop, Adam, as well as different algorithms to optimize asynchronous SGD. Finally, we've considered other strategies to improve SGD such as shuffling and curriculum learning, batch normalization, and early stopping.

I hope that this blog post was able to provide you with some intuitions towards the motivation and the behaviour of the different optimization algorithms. Are there any obvious algorithms to improve SGD that I've missed? What tricks are you using yourself to facilitate training with SGD? **Let me know in the comments below.**

# Acknowledgements

Thanks to [Denny Britz](https://twitter.com/dennybritz) and [Cesar Salgado](https://twitter.com/cesarsvs) for reading drafts of this post and providing suggestions.

# Printable version and citation

This blog post is also available as an [article on arXiv](https://arxiv.org/abs/1609.04747), in case you want to refer to it later.

In case you found it helpful, consider citing the corresponding arXiv article as:

*Sebastian Ruder (2016). An overview of gradient descent optimisation algorithms. arXiv preprint arXiv:1609.04747.*

# Translations

This blog post has been translated into the following languages:

- [Japanese](http://postd.cc/optimizing-gradient-descent/)
- [Chinese](http://blog.csdn.net/google19890102/article/details/69942970)
- [Korean](https://brunch.co.kr/@chris-song/50)

Image credit for cover photo: [Karpathy's beautiful loss functions tumblr](http://lossfunctions.tumblr.com/)

* * *

1. H. Robinds and S. Monro, “A stochastic approximation method,” Annals of Mathematical Statistics, vol. 22, pp. 400–407, 1951. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref1)

2. Darken, C., Chang, J., & Moody, J. (1992). Learning rate schedules for faster stochastic gradient search. Neural Networks for Signal Processing II Proceedings of the 1992 IEEE Workshop, (September), 1–11. [http://doi.org/10.1109/NNSP.1992.253713](https://doi.org/10.1109/NNSP.1992.253713)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref2)

3. Dauphin, Y., Pascanu, R., Gulcehre, C., Cho, K., Ganguli, S., & Bengio, Y. (2014). Identifying and attacking the saddle point problem in high-dimensional non-convex optimization. arXiv, 1–14. Retrieved from [http://arxiv.org/abs/1406.2572](https://arxiv.org/abs/1406.2572)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref3)

4. Sutton, R. S. (1986). Two problems with backpropagation and other steepest-descent learning procedures for networks. Proc. 8th Annual Conf. Cognitive Science Society. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref4)

5. Qian, N. (1999). On the momentum term in gradient descent learning algorithms. Neural Networks : The Official Journal of the International Neural Network Society, 12(1), 145–151. [http://doi.org/10.1016/S0893-6080(98)00116-6](https://doi.org/10.1016/S0893-6080(98)00116-6)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref5)

6. Nesterov, Y. (1983). A method for unconstrained convex minimization problem with the rate of convergence o(1/k2). Doklady ANSSSR (translated as Soviet.Math.Docl.), vol. 269, pp. 543– 547. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref6)

7. Bengio, Y., Boulanger-Lewandowski, N., & Pascanu, R. (2012). Advances in Optimizing Recurrent Networks. Retrieved from [http://arxiv.org/abs/1212.0901](https://arxiv.org/abs/1212.0901)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref7)

8. Sutskever, I. (2013). Training Recurrent neural Networks. PhD Thesis. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref8)

9. Duchi, J., Hazan, E., & Singer, Y. (2011). Adaptive Subgradient Methods for Online Learning and Stochastic Optimization. Journal of Machine Learning Research, 12, 2121–2159. Retrieved from http://jmlr.org/papers/v12/duchi11a.html  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref9)

10. Dean, J., Corrado, G. S., Monga, R., Chen, K., Devin, M., Le, Q. V, … Ng, A. Y. (2012). Large Scale Distributed Deep Networks. NIPS 2012: Neural Information Processing Systems, 1–11. http://papers.nips.cc/paper/4687-large-scale-distributed-deep-networks.pdf  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref10)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref10:1)

11. Pennington, J., Socher, R., & Manning, C. D. (2014). Glove: Global Vectors for Word Representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, 1532–1543. [http://doi.org/10.3115/v1/D14-1162](https://doi.org/10.3115/v1/D14-1162)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref11)

12. Duchi et al. [3] give this matrix as an alternative to the *full* matrix containing the outer products of all previous gradients, as the computation of the matrix square root is infeasible even for a moderate number of parameters dd. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref12)

13. Zeiler, M. D. (2012). ADADELTA: An Adaptive Learning Rate Method. Retrieved from [http://arxiv.org/abs/1212.5701](https://arxiv.org/abs/1212.5701)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref13)

14. Kingma, D. P., & Ba, J. L. (2015). Adam: a Method for Stochastic Optimization. International Conference on Learning Representations, 1–13. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref14)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref14:1)

15. Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., & Hochreiter, S. (2017). GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium. In Advances in Neural Information Processing Systems 30 (NIPS 2017). [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref15)

16. Dozat, T. (2016). Incorporating Nesterov Momentum into Adam. ICLR Workshop, (1), 2013–2016. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref16)

17. Huang, G., Liu, Z., Weinberger, K. Q., & van der Maaten, L. (2017). Densely Connected Convolutional Networks. In Proceedings of CVPR 2017. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref17)

18. Johnson, M., Schuster, M., Le, Q. V, Krikun, M., Wu, Y., Chen, Z., … Dean, J. (2016). Google’s Multilingual Neural Machine Translation System: Enabling Zero-Shot Translation. arXiv Preprint arXiv:1611.0455. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref18)

19. Reddi, Sashank J., Kale, Satyen, & Kumar, Sanjiv. On the Convergence of Adam and Beyond. Proceedings of ICLR 2018. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref19)

20. Loshchilov, I., & Hutter, F. (2019). Decoupled Weight Decay Regularization. In Proceedings of ICLR 2019. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref20)

21. Ma, J., & Yarats, D. (2019). Quasi-hyperbolic momentum and Adam for deep learning. In Proceedings of ICLR 2019. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref21)

22. Lucas, J., Sun, S., Zemel, R., & Grosse, R. (2019). Aggregated Momentum: Stability Through Passive Damping. In Proceedings of ICLR 2019. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref22)

23. Niu, F., Recht, B., Christopher, R., & Wright, S. J. (2011). Hogwild! : A Lock-Free Approach to Parallelizing Stochastic Gradient Descent, 1–22. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref23)

24. Mcmahan, H. B., & Streeter, M. (2014). Delay-Tolerant Algorithms for Asynchronous Distributed Online Learning. Advances in Neural Information Processing Systems (Proceedings of NIPS), 1–9. Retrieved from http://papers.nips.cc/paper/5242-delay-tolerant-algorithms-for-asynchronous-distributed-online-learning.pdf  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref24)

25. Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., … Zheng, X. (2015). TensorFlow : Large-Scale Machine Learning on Heterogeneous Distributed Systems. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref25)

26. Zhang, S., Choromanska, A., & LeCun, Y. (2015). Deep learning with Elastic Averaging SGD. Neural Information Processing Systems Conference (NIPS 2015), 1–24. Retrieved from [http://arxiv.org/abs/1412.6651](https://arxiv.org/abs/1412.6651)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref26)

27. LeCun, Y., Bottou, L., Orr, G. B., & Müller, K. R. (1998). Efficient BackProp. Neural Networks: Tricks of the Trade, 1524, 9–50. [http://doi.org/10.1007/3-540-49430-8_2](https://doi.org/10.1007/3-540-49430-8_2)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref27)

28. Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009). Curriculum learning. Proceedings of the 26th Annual International Conference on Machine Learning, 41–48. [http://doi.org/10.1145/1553374.1553380](https://doi.org/10.1145/1553374.1553380)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref28)

29. Zaremba, W., & Sutskever, I. (2014). Learning to Execute, 1–25. Retrieved from [http://arxiv.org/abs/1410.4615](https://arxiv.org/abs/1410.4615)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref29)

30. Ioffe, S., & Szegedy, C. (2015). Batch Normalization : Accelerating Deep Network Training by Reducing Internal Covariate Shift. arXiv Preprint arXiv:1502.03167v3. [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref30)

31. Neelakantan, A., Vilnis, L., Le, Q. V., Sutskever, I., Kaiser, L., Kurach, K., & Martens, J. (2015). Adding Gradient Noise Improves Learning for Very Deep Networks, 1–11. Retrieved from [http://arxiv.org/abs/1511.06807](https://arxiv.org/abs/1511.06807)  [↩︎](https://ruder.io/optimizing-gradient-descent/index.html#fnref31)