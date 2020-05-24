Introducing TensorFlow Probability – TensorFlow – Medium

# Introducing TensorFlow Probability

## *Posted by: Josh Dillon, Software Engineer; *[*Mike Shwe*](http://twitter.com/mikeshwe)*, Product Manager; and *[*Dustin Tran*](http://dustintran.com/)*, Research Scientist — on behalf of the TensorFlow Probability Team*

At the 2018 TensorFlow Developer Summit, we [announced](https://medium.com/tensorflow/highlights-from-tensorflow-developer-summit-2018-cd86615714b2) TensorFlow Probability: a probabilistic programming toolbox for machine learning researchers and practitioners to quickly and reliably build sophisticated models that leverage state-of-the-art hardware. You should use TensorFlow Probability if:

- •You want to build a *generative model *of data, reasoning about its hidden processes.
- •You need to quantify the *uncertainty* in your predictions, as opposed to predicting a single value.
- •Your training set has a large number of features relative to the number of data points.
- •Your data is structured — for example, with groups, space, graphs, or language semantics — and you’d like to capture this structure with prior information.
- •You have an inverse problem* — *see this [TFDS’18 talk](https://www.youtube.com/watch?v=Bb1_zlrjo1c) for reconstructing fusion plasmas from measurements.

TensorFlow Probability gives you the tools to solve these problems. In addition, it inherits the strengths of TensorFlow such as automatic differentiation and the ability to scale performance across a variety of platforms: CPUs, GPUs, and TPUs.

### What’s in TensorFlow Probability?

Our stack of probabilistic ML tools provides modular abstractions for probabilistic reasoning and statistical analysis in the TensorFlow ecosystem.

![](../_resources/251dced6116903a24ce08b7420428721.png)![0*19BJhsJ-2DzQ7fFH.](../_resources/a7f50261b38e37c490c5f1cd7e436cd7.png)

*An overview of TensorFlow Probability. The probabilistic programming toolbox provides benefits for users ranging from Data Scientists and Statisticians to all TensorFlow Users.*

**Layer 0: TensorFlow**. Numerical operations. In particular, the LinearOperator class enables matrix-free implementations that can exploit special structure (diagonal, low-rank, etc.) for efficient computation. It is built and maintained by the TensorFlow Probability team and is now part of `[tf.linalg](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/linalg)` in core TF.

**Layer 1: Statistical Building Blocks**

- •Distributions (`[tf.contrib.distributions](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/distributions/python/ops)`, `[tf.distributions](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/distributions)`): A large collection of probability distributions and related statistics with batch and [broadcasting](https://docs.scipy.org/doc/numpy-1.14.0/user/basics.broadcasting.html) semantics.
- •Bijectors (`[tf.contrib.distributions.bijectors](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/distributions/python/ops/bijectors)`): Reversible and composable transformations of random variables. Bijectors provide a rich class of transformed distributions, from classical examples like the [log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution) to sophisticated deep learning models such as [masked autoregressive flows](https://arxiv.org/abs/1705.07057).

(See the [*TensorFlow Distributions* whitepaper](https://arxiv.org/abs/1711.10604) for more information.)

**Layer 2: Model Building**

- •Edward2 (`[tfp.edward2](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/edward2)`): A probabilistic programming language for specifying flexible probabilistic models as programs.
- •Probabilistic Layers (`[tfp.layers](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/layers)`): Neural network layers with uncertainty over the functions they represent, extending TensorFlow Layers.
- •Trainable Distributions (`[tfp.trainable_distributions](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/trainable_distributions.py)`): Probability distributions parameterized by a single Tensor, making it easy to build neural nets that output probability distributions.

**Layer 3: Probabilistic Inference**

- •Markov chain Monte Carlo (`[tfp.mcmc](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/mcmc)`): Algorithms for approximating integrals via sampling. Includes [Hamiltonian Monte Carlo](https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo), random-walk Metropolis-Hastings, and the ability to build custom transition kernels.
- •Variational Inference (`[tfp.vi](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/vi)`): Algorithms for approximating integrals via optimization.
- •Optimizers (`[tfp.optimizer](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/optimizer)`): Stochastic optimization methods, extending TensorFlow Optimizers. Includes [Stochastic Gradient Langevin Dynamics](http://www.icml-2011.org/papers/398_icmlpaper.pdf).
- •Monte Carlo (`[tfp.monte_carlo](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/monte_carlo.py)`): Tools for computing Monte Carlo expectations.

**Layer 4: Pre-made Models and Inference **(analogous to [TensorFlow’s pre-made Estimators](https://www.tensorflow.org/programmers_guide/estimators))

- •Bayesian structural time series (*coming soon*): High-level interface for fitting time-series models (i.e., similar to R’s BSTS package).
- •Generalized Linear Mixed Models (*coming soon*): High-level interface for fitting mixed-effects regression models (i.e., similar to R’s lme4 package).

The TensorFlow Probability team is committed to supporting users and contributors with cutting-edge features, continuous code updates, and bug fixes. We’ll continue to add end-to-end examples and tutorials.

### Let’s see some examples!

#### Linear Mixed Effects Models with Edward2

A linear mixed effects model is a simple approach for modeling structured relationships in data. Also known as a *hierarchical linear model*, it shares statistical strength across groups of data points in order to improve inferences about any individual one.

As demonstration, consider the InstEval data set from the popular [lme4 package in R](https://cran.r-project.org/package=lme4), which consists of university courses and their evaluation ratings. Using TensorFlow Probability, we specify the model as an Edward2 probabilistic program (`tfp.edward2`), [which extends Edward](http://edwardlib.org/). The program below reifies the model in terms of its generative process.

import tensorflow as tf
from tensorflow_probability import edward2 as ed
def model(features):

# Set up fixed effects and other parameters.

intercept = tf.get_variable("intercept", [])
service_effects = tf.get_variable("service_effects", [])
student_stddev_unconstrained = tf.get_variable(
"student_stddev_pre", [])
instructor_stddev_unconstrained = tf.get_variable(
"instructor_stddev_pre", [])

# Set up random effects.

 **student_effects = ed.MultivariateNormalDiag(
loc=tf.zeros(num_students),
scale_identity_multiplier=tf.exp(
student_stddev_unconstrained),
name="student_effects")
instructor_effects = ed.MultivariateNormalDiag(
loc=tf.zeros(num_instructors),
scale_identity_multiplier=tf.exp(
instructor_stddev_unconstrained),
name="instructor_effects")**

# Set up likelihood given fixed and random effects.

 **ratings = ed.Normal(
loc=(service_effects * features["service"] +
tf.gather(student_effects, features["students"]) +
tf.gather(instructor_effects, features["instructors"]) +
intercept),
scale=1.,
name="ratings")**
return ratings

The model takes as input a features dictionary of “service”, “students”, and “instructors”; they are vectors where each element describes an individual course. The model regresses on these inputs, posits latent random variables, and returns a distribution over the courses’ evaluation ratings. TensorFlow session runs on this output will return a generation of the ratings.

Check out the [”Linear Mixed Effects Models”](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Linear_Mixed_Effects_Models.ipynb) tutorial for details on how we train the model using the [tfp.mcmc.HamiltonianMonteCarlo](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/mcmc/hmc.py) algorithm, and how we explore and interpret the model using posterior predictions.

#### Gaussian Copulas with TFP Bijectors

A [Copula](https://en.wikipedia.org/wiki/Copula_%28probability_theory%29) is a multivariate probability distribution for which the marginal probability distribution of each variable is uniform. To build a copula using TFP intrinsics, one can use Bijectors and TransformedDistribution. These abstractions enable easy creation of complex distributions, for example:

import tensorflow_probability as tfp
tfd = tfp.distributions
tfb = tfp.distributions.bijectors

# Example: Log-Normal Distribution

log_normal = tfd.TransformedDistribution(
distribution=tfd.Normal(loc=0., scale=1.),
bijector=**tfb.Exp**())

# Example: Kumaraswamy Distribution

Kumaraswamy = tfd.TransformedDistribution(
distribution=tfd.Uniform(low=0., high=1.),
bijector=**tfb.Kumaraswamy**(
concentration1=2.,
concentration0=2.))

# Example: Masked Autoregressive Flow

# https://arxiv.org/abs/1705.07057

shift_and_log_scale_fn = **tfb.masked_autoregressive_default_template**(
hidden_layers=[512, 512],
event_shape=[28*28])
maf = tfd.TransformedDistribution(
distribution=tfd.Normal(loc=0., scale=1.),
bijector=**tfb.MaskedAutoregressiveFlow**(
shift_and_log_scale_fn=shift_and_log_scale_fn))

The [“Gaussian Copula”](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Gaussian_Copula.ipynb) creates a few custom Bijectors and then shows how to easily build several different copulas. For more background on distributions, see [“Understanding TensorFlow Distributions Shapes.”](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Understanding_TensorFlow_Distributions_Shapes.ipynb) It describes how to manage shapes for sampling, batch training, and modeling events.

#### Variational Autoencoder with TFP Utilities

A variational autoencoder is a machine learning model which uses one learned system to represent data in some low-dimensional space and a second learned system to restore the low-dimensional representation to what would have otherwise been the input. Because TF supports automatic differentiation, black-box variational inference is a breeze! Example:

import tensorflow as tf
import tensorflow_probability as tfp

# Assumes user supplies `likelihood`, `prior`, `surrogate_posterior`

# functions and that each returns a

# tf.distribution.Distribution-like object.

elbo_loss = **tfp.vi.monte_carlo_csiszar_f_divergence(
 **f=**tfp.vi.kl_reverse**, # Equivalent to "Evidence Lower BOund"
p_log_prob=lambda z: likelihood(z).log_prob(x) + prior().log_prob(z),
q=surrogate_posterior(x),
num_draws=1)
train = tf.train.AdamOptimizer(
learning_rate=0.01).minimize(elbo_loss)

To see more details, check out our [variational autoencoder](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vae) example!

#### Bayesian Neural Networks with TFP Probabilistic Layers

A Bayesian neural network is a neural network with a prior distribution over its weights and biases. It provides improved uncertainty about its predictions via these priors. A Bayesian neural network can also be interpreted as an infinite ensemble of neural networks: the probability assigned to each neural network configuration is according to the prior.

As demonstration, consider the CIFAR-10 dataset which has features (images of shape 32 x 32 x 3) and labels (values from 0 to 9). To fit the neural network, we’ll use [variational inference](https://en.wikipedia.org/wiki/Variational_Bayesian_methods), which is a suite of methods to approximate the neural network’s posterior distribution over weights and biases. Namely, we use the recently published [Flipout estimator](https://arxiv.org/abs/1803.04386) in the TensorFlow Probabilistic Layers module (`tfp.layers`).

import tensorflow as tf
import tensorflow_probability as tfp
model = tf.keras.Sequential([
tf.keras.layers.Reshape([32, 32, 3]),
tfp.layers.Convolution2DFlipout(
64, kernel_size=5, padding='SAME', activation=tf.nn.relu),
tf.keras.layers.MaxPooling2D(pool_size=[2, 2],
strides=[2, 2],
padding='SAME'),
tf.keras.layers.Reshape([16 * 16 * 64]),
tfp.layers.DenseFlipout(10)
])
logits = model(features)
neg_log_likelihood = tf.nn.softmax_cross_entropy_with_logits(
labels=labels, logits=logits)
kl = sum(model.get_losses_for(inputs=None))
loss = neg_log_likelihood + kl
train_op = tf.train.AdamOptimizer().minimize(loss)

The model object composes neural net layers on an input tensor, and it performs stochastic forward passes with respect to probabilistic convolutional layer and probabilistic densely-connected layer. The function returns an output tensor with shape given by the batch size and 10 values. Each row of this tensor represents the logits (unconstrained probability values) that each data point belongs to one of the 10 classes.

For training, we build the loss function, which comprises two terms: the expected negative log-likelihood and the KL divergence. We approximate the expected negative log-likelihood via Monte carlo. The KL divergence is added via regularizer terms which are arguments to the layers.

`tfp.layers` can also be used with [eager execution](https://www.tensorflow.org/programmers_guide/eager) using the tf.keras.Model class.

class MNISTModel(tf.keras.Model):
def __init__(self):
super(MNISTModel, self).__init__()
 **self.dense1 = tfp.layers.DenseFlipout(units=10)
self.dense2 = tfp.layers.DenseFlipout(units=10)**
def call(self, input):
"""Run the model."""
result = self.dense1(input)
result = self.dense2(result)

# reuse variables from dense2 layer

result = self.dense2(result)
return result
model = MNISTModel()

### Getting started

To get started with probabilistic machine learning in TensorFlow, just run:
pip install --user --upgrade tfp-nightly

For all the code and details, check out [github.com/tensorflow/probability](https://github.com/tensorflow/probability). We’re excited to collaborate with you via GitHub, whether you’re a user or contributor!