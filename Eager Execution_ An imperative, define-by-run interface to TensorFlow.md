Eager Execution: An imperative, define-by-run interface to TensorFlow

## [Eager Execution: An imperative, define-by-run interface to TensorFlow](https://research.googleblog.com/2017/10/eager-execution-imperative-define-by.html)

Tuesday, October 31, 2017
 Posted by Asim Shankar and Wolff Dobson, Google Brain Team

Today, we introduce eager execution for TensorFlow. Eager execution is an imperative, define-by-run interface where operations are executed immediately as they are called from Python. This makes it easier to get started with TensorFlow, and can make research and development more intuitive.

The benefits of eager execution include:

- Fast debugging with immediate run-time errors and integration with Python tools
- Support for dynamic models using easy-to-use Python control flow
- Strong support for custom and higher-order gradients
- Almost all of the available TensorFlow operations

Eager execution is available now as an experimental feature, so we're looking for feedback from the community to guide our direction.

To understand this all better, let's look at some code. This gets pretty technical; familiarity with TensorFlow will help.

## Using Eager Execution

When you enable eager execution, operations execute immediately and return their values to Python without requiring a Session.run(). For example, to multiply two matrices together, we write this:

import tensorflow as tfimport tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()x =  [[2.]]m = tf.matmul(x, x)

It’s straightforward to inspect intermediate results with print or the Python debugger.

print(m)# The 1x1 matrix [[4.]]

Dynamic models can be built with Python flow control. Here's an example of the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) using TensorFlow’s arithmetic operations:

a = tf.constant(12)counter =  0while  not tf.equal(a,  1):  if tf.equal(a %  2,  0): a = a /  2  else: a =  3  * a +  1  print(a)

Here, the use of the tf.constant(12) Tensor object will promote all math operations to tensor operations, and as such all return values with be tensors.

## Gradients

Most TensorFlow users are interested in automatic differentiation. Because different operations can occur during each call, we record all forward operations to a tape, which is then played backwards when computing gradients. After we've computed the gradients, we discard the tape.

If you’re familiar with the [autograd](https://github.com/HIPS/autograd) package, the API is very similar. For example:

def square(x):  return tf.multiply(x, x)grad = tfe.gradients_function(square)print(square(3.))  # [9.]print(grad(3.))  # [6.]

The gradients_function call takes a Python function square() as an argument and returns a Python callable that computes the partial derivatives of square() with respect to its inputs. So, to get the derivative of square() at 3.0, invoke grad(3.0), which is 6.

The same gradients_function call can be used to get the second derivative of square:

gradgrad = tfe.gradients_function(lambda x: grad(x)[0])print(gradgrad(3.))  # [2.]

As we noted, control flow can cause different operations to run, such as in this example.

def abs(x):  return x if x >  0.  else  -x

grad = tfe.gradients_function(abs)print(grad(2.0))  # [1.]print(grad(-2.0))  # [-1.]

### Custom Gradients

Users may want to define custom gradients for an operation, or for a function. This may be useful for multiple reasons, including providing a more efficient or more numerically stable gradient for a sequence of operations.

Here is an example that illustrates the use of custom gradients. Let's start by looking at the function *log(1 + ex)*, which commonly occurs in the computation of cross entropy and log likelihoods.

def log1pexp(x):  return tf.log(1  + tf.exp(x))grad_log1pexp = tfe.gradients_function(log1pexp)# The gradient computation works fine at x = 0.print(grad_log1pexp(0.))# [0.5]# However it returns a `nan` at x = 100 due to numerical instability.print(grad_log1pexp(100.))# [nan]

We can use a custom gradient for the above function that analytically simplifies the gradient expression. Notice how the gradient function implementation below reuses an expression (tf.exp(x)) that was computed during the forward pass, making the gradient computation more efficient by avoiding redundant computation.

@tfe.custom_gradientdef log1pexp(x): e = tf.exp(x)  def grad(dy):  return dy *  (1  -  1  /  (1  + e))  return tf.log(1  + e), grad

grad_log1pexp = tfe.gradients_function(log1pexp)# Gradient at x = 0 works as before.print(grad_log1pexp(0.))# [0.5]# And now gradient computation at x=100 works as well.print(grad_log1pexp(100.))# [1.0]

## Building models

Models can be organized in classes. Here's a model class that creates a (simple) two layer network that can classify the standard MNIST handwritten digits.

class  MNISTModel(tfe.Network):  def __init__(self):  super(MNISTModel,  self).__init__()  self.layer1 =  self.track_layer(tf.layers.Dense(units=10))  self.layer2 =  self.track_layer(tf.layers.Dense(units=10))  def call(self, input):  """Actually runs the model.""" result =  self.layer1(input) result =  self.layer2(result)  return result

We recommend using the classes (not the functions) in tf.layers since they create and contain model parameters (variables). Variable lifetimes are tied to the lifetime of the layer objects, so be sure to keep track of them.

Why are we using tfe.Network? A Network is a container for layers and is a tf.layer.Layer itself, allowing Network objects to be embedded in other Network objects. It also contains utilities to assist with inspection, saving, and restoring.

Even without training the model, we can imperatively call it and inspect the output:

# Let's make up a blank input imagemodel =  MNISTModel()batch = tf.zeros([1,  1,  784])print(batch.shape)# (1, 1, 784)result = model(batch)print(result)# tf.Tensor([[[ 0. 0., ...., 0.]]], shape=(1, 1, 10), dtype=float32)

Note that we do not need any placeholders or sessions. The first time we pass in the input, the sizes of the layers’ parameters are set.

To train any model, we define a loss function to optimize, calculate gradients, and use an optimizer to update the variables. First, here's a loss function:

def loss_function(model, x, y): y_ = model(x)  return tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_)

And then, our training loop:

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)for  (x, y)  in tfe.Iterator(dataset): grads = tfe.implicit_gradients(loss_function)(model, x, y) optimizer.apply_gradients(grads)

implicit_gradients() calculates the derivatives of loss_function with respect to all the TensorFlow variables used during its computation.

We can move computation to a GPU the same way we’ve always done with TensorFlow:

with tf.device("/gpu:0"):  for  (x, y)  in tfe.Iterator(dataset): optimizer.minimize(lambda: loss_function(model, x, y))

(Note: We're shortcutting storing our loss and directly calling the optimizer.minimize, but you could also use the apply_gradients() method above; they are equivalent.)

## Using Eager with Graphs

Eager execution makes development and debugging far more interactive, but TensorFlow graphs have a lot of advantages with respect to distributed training, performance optimizations, and production deployment.

The same code that executes operations when eager execution is enabled will construct a graph describing the computation when it is not. To convert your models to graphs, simply run the same code in a new Python session where eager execution hasn’t been enabled, as seen, for example, in the [MNIST example](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/eager/python/examples/mnist). The value of model variables can be saved and restored from checkpoints, allowing us to move between eager (imperative) and graph (declarative) programming easily. With this, models developed with eager execution enabled can be easily exported for production deployment.

In the near future, we will provide utilities to selectively convert portions of your model to graphs. In this way, you can fuse parts of your computation (such as internals of a custom RNN cell) for high-performance, but also keep the flexibility and readability of eager execution.

## How does my code change?

Using eager execution should be intuitive to current TensorFlow users. There are only a handful of eager-specific APIs; most of the existing APIs and operations work with eager enabled. Some notes to keep in mind:

- As with TensorFlow generally, we recommend that if you have not yet switched from queues to using tf.data for input processing, you should. It's easier to use and usually faster. For help, see [this blog post](https://developers.googleblog.com/2017/09/introducing-tensorflow-datasets.html) and [the documentation page](https://www.tensorflow.org/programmers_guide/datasets).
- Use object-oriented layers, like tf.layer.Conv2D() or Keras layers; these have explicit storage for variables.
- For most models, you can write code so that it will work the same for both eager execution and graph construction. There are some exceptions, such as dynamic models that use Python control flow to alter the computation based on inputs.
- Once you invoke tfe.enable_eager_execution(), it cannot be turned off. To get graph behavior, start a new Python session.

## Getting started and the future

This is still a preview release, so you may hit some rough edges. To get started today:

- Install the [nightly](https://github.com/tensorflow/tensorflow#installation) build of TensorFlow.
- Check out the [README](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/eager/README.md) (including known issues)
- Get detailed instructions in the eager execution [User Guide](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/eager/python/g3doc/guide.md)
- Browse the eager [examples in GitHub](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/eager/python/examples)
- Follow the [changelog](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/eager/README.md#changelog) for updates.

There's a lot more to talk about with eager execution and we're excited… or, rather, we're *eager* for you to try it today! [Feedback](https://github.com/tensorflow/tensorflow/issues/new) is absolutely welcome.

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

18 comments

[![photo.jpg.png](../_resources/90dc03288ae5273ac237ce19160eab19.png)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg.png](../_resources/f4914bb545dc0a6001befca5f7a06177.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)

### [Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/4sJnUnAgU5d)  -  Shared publicly

Check out the introduction of Eager Execution for [#TensorFlow](https://apis.google.com/s/%23TensorFlow)! https://goo.gl/1s7aZm

+
3
7
8
7

 ·
Reply

[![ic_w_post_gplus_black_24dp.png](../_resources/441cbb7966e7b6b7c013d10a2d98b1b5.png)](https://apis.google.com/u/0/wm/1/104441890571388637877)

### [Jadhav Dattatreya](https://apis.google.com/u/0/wm/1/104441890571388637877)

[2 days ago](https://apis.google.com/u/0/wm/1/104441890571388637877/posts/1At9mTi5g23)  -  Shared publicly

awesome!!!
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/2421dd693c5c689afc08f93290ae7791.jpg)](https://apis.google.com/u/0/wm/1/107633616774873306635)

### [Berita Intermezo](https://apis.google.com/u/0/wm/1/107633616774873306635) shared this

[3 days ago](https://apis.google.com/u/0/wm/1/107633616774873306635/posts/HQhAU2iQMHd)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/cac319efc92018cc7b7905e96355e89b.jpg)](https://apis.google.com/u/0/wm/1/115310532721161234725)

### [Atinesh Singh](https://apis.google.com/u/0/wm/1/115310532721161234725)

[16 hours ago](https://apis.google.com/u/0/wm/1/115310532721161234725/posts/jhskQjLet9c)  -  Shared publicly

Cool
+
0
1
0

 ·
Reply

[![post_twitter_black_24dp.png](../_resources/441cbb7966e7b6b7c013d10a2d98b1b5.png)](https://apis.google.com/u/0/wm/1/106396321599803769566)

### [choong33](https://apis.google.com/u/0/wm/1/106396321599803769566)

[2 days ago](https://apis.google.com/u/0/wm/1/106396321599803769566/posts/M7rEEvWia8n)  -  Shared publicly

Fantastic !
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/597b9af6d5d54a7f3c8f4327556075b5.jpg)](https://apis.google.com/u/0/wm/1/115710066729590930228)

### [I.J. Atencio](https://apis.google.com/u/0/wm/1/115710066729590930228) shared this

[1 day ago](https://apis.google.com/u/0/wm/1/+IJAtencio/posts/PbXVBgLJvFD)  -  [Machine Learning (Resources)](https://apis.google.com/u/0/wm/1/communities/107785538899595981479/stream/50068cb0-c205-4b33-8318-ca48a3f23ae7)

+
0
1
0

[![photo.jpg](../_resources/0c06feffce606d630e828fb5f495a05d.jpg)](https://apis.google.com/u/0/wm/1/101016012457565822382)

### [Kwan-yuet Ho](https://apis.google.com/u/0/wm/1/101016012457565822382) shared this via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+KwanyuetHo/posts/1evEegpwpvi)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/b1ad7da7558205a10773391a4db4a4bb.png)](https://apis.google.com/u/0/wm/1/104070495650441591893)

### [Andrés Leonardo Martínez Ortiz](https://apis.google.com/u/0/wm/1/104070495650441591893) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+Andr%C3%A9sLeonardoMart%C3%ADnezOrtiz/posts/53V2sZ5DZ22)  -  Shared publicly

Hooray! An eager execution for TensorFlow https://research.googleblog.com/2017/10/eager-execution-imperative-define-by.html  [#machinelearning](https://apis.google.com/s/%23machinelearning)  [#tensorflow](https://apis.google.com/s/%23tensorflow)  [#trends](https://apis.google.com/s/%23trends)

+
0
1
0

 ·
Reply

[(L)](https://apis.google.com/u/0/wm/1/111903479032532990230)

### [Hanoz Bhathena](https://apis.google.com/u/0/wm/1/111903479032532990230) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/111903479032532990230/posts/EkGaoBZjspL)  -  Shared publicly

THIS IS AWESOME!!!
+
0
1
0

 ·
Reply

[(L)](https://apis.google.com/u/0/wm/1/108666147887612117883)

### [Yan Kang](https://apis.google.com/u/0/wm/1/108666147887612117883)

[2 days ago](https://apis.google.com/u/0/wm/1/108666147887612117883/posts/emXJFwFKyH6)  -  Shared publicly

Good one
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/f4f8e193ae18d353f94e05e2b7b6b9f8.jpg)](https://apis.google.com/u/0/wm/1/102135785477686748429)

### [David Metcalfe](https://apis.google.com/u/0/wm/1/102135785477686748429) via Google+

[2 days ago](https://apis.google.com/u/0/wm/1/102135785477686748429/posts/APTpDZzD4wj)  -  Shared publicly

"Today, we introduce eager execution for TensorFlow. Eager execution is an imperative, define-by-run interface where operations are executed immediately as they are called from Python. This makes it easier to get started with TensorFlow, and can make research and development more intuitive.

The benefits of eager execution include:

- Fast debugging with immediate run-time errors and integration with Python tools
- Support for dynamic models using easy-to-use Python control flow
- Strong support for custom and higher-order gradients

Almost all of the available TensorFlow operations

- Eager execution is available now as an experimental feature, so we're looking for feedback from the community to guide our direction."

Read more
+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/f484991a8514b25ac3ad7b4e83a316d9.jpg)](https://apis.google.com/u/0/wm/1/112241126725016085461)

### [Ramesh Ch](https://apis.google.com/u/0/wm/1/112241126725016085461) shared this via Google+

[3 days ago](https://apis.google.com/u/0/wm/1/112241126725016085461/posts/NV1AYewsguV)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/3559e4e3b03625c2c3e6ae55996ac6e0.jpg)](https://apis.google.com/u/0/wm/1/103024283812759662406)

### [Saurabh Saxena](https://apis.google.com/u/0/wm/1/103024283812759662406) shared this via Google+

[3 days ago](https://apis.google.com/u/0/wm/1/+SaurabhSaxenaOne/posts/2yYkoryoRnR)  -  Shared publicly

+
0
1
0

 ·
Reply

[(L)](https://apis.google.com/u/0/wm/1/103694277569151255096)

### [Bob Smith](https://apis.google.com/u/0/wm/1/103694277569151255096)

[3 days ago](https://apis.google.com/u/0/wm/1/103694277569151255096/posts/eATVuxHpSWX)  -  Shared publicly

A copy of the example code in a Colab notebook --
https://colab.research.google.com/notebook#fileId=0B7I8C_4vGdF6REhrdHkycWRyMTg

This will allow you to experiment with TF eager directly in your browser -- no software install required.

+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/3a7d8c5ed620bf05c8ef300ca5360341.jpg)](https://apis.google.com/u/0/wm/1/105710778006023159587)

### [Suthat Ronglong](https://apis.google.com/u/0/wm/1/105710778006023159587) via Google+

[5 hours ago](https://apis.google.com/u/0/wm/1/+suthatronglong/posts/WSexhNJ2PEQ)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/4sJnUnAgU5d)

Check out the introduction of Eager Execution for [#TensorFlow](https://apis.google.com/s/%23TensorFlow)! https://goo.gl/1s7aZm

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/eaacde7c7b43e8ac1b764744011fe06d.jpg)](https://apis.google.com/u/0/wm/1/105471123380822891032)

### [Muhammad Sadeli](https://apis.google.com/u/0/wm/1/105471123380822891032) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+MuhammadSadeli/posts/ZDe5mWzZTkk)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/4sJnUnAgU5d)

Check out the introduction of Eager Execution for [#TensorFlow](https://apis.google.com/s/%23TensorFlow)! https://goo.gl/1s7aZm

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/cc27f3144567f67b4d929a97275d38bc.jpg)](https://apis.google.com/u/0/wm/1/114753028665775786510)

### [Lauren Weinstein](https://apis.google.com/u/0/wm/1/114753028665775786510) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+LaurenWeinstein/posts/gyNf7Xomjui)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/4sJnUnAgU5d)

Check out the introduction of Eager Execution for [#TensorFlow](https://apis.google.com/s/%23TensorFlow)! https://goo.gl/1s7aZm

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/144b0a5ebb26eff8100316b06e5b12de.png)](https://apis.google.com/u/0/wm/1/102055549887264985768)

### [Kazunori Sato](https://apis.google.com/u/0/wm/1/102055549887264985768) via Google+

[3 days ago](https://apis.google.com/u/0/wm/1/+KazunoriSato/posts/MAJazTogTc1)  -  Shared publicly

ChainerやPyTorchっぽいdefine-by-runが可能なTensorFlow Eagerをリリース。
Translate
+
1
2
1

 ·
Reply

Labels:[Google Brain](https://research.googleblog.com/search/label/Google%20Brain) , [Machine Learning](https://research.googleblog.com/search/label/Machine%20Learning) , [TensorFlow](https://research.googleblog.com/search/label/TensorFlow)