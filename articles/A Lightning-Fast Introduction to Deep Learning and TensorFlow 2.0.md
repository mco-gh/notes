A Lightning-Fast Introduction to Deep Learning and TensorFlow 2.0

# A Lightning-Fast Introduction to Deep Learning and TensorFlow 2.0

A hands-on guide to getting started with TensorFlow 2.0.

Vihar Kurama
|Expert Columnist

Machine learning engineer who writes regularly about machine learning and data science.

May 10, 2020
 Updated:  May 19, 2020

 [![](data:image/svg+xml,%3csvg focusable='false' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' data-evernote-id='1442' class='js-evernote-checked'%3e%3cpath d='M6.227 12.61h4.19v13.48h-4.19V12.61zm2.095-6.7a2.43 2.43 0 0 1 0 4.86c-1.344 0-2.428-1.09-2.428-2.43s1.084-2.43 2.428-2.43m4.72 6.7h4.02v1.84h.058c.56-1.058 1.927-2.176 3.965-2.176 4.238 0 5.02 2.792 5.02 6.42v7.395h-4.183v-6.56c0-1.564-.03-3.574-2.178-3.574-2.18 0-2.514 1.7-2.514 3.46v6.668h-4.187V12.61z' fill='%23FFF' data-evernote-id='1017' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)LinkedIn](https://builtin.com/#linkedin)  [![](data:image/svg+xml,%3csvg focusable='false' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' data-evernote-id='1443' class='js-evernote-checked'%3e%3cpath fill='%23FFF' d='M17.78 27.5V17.008h3.522l.527-4.09h-4.05v-2.61c0-1.182.33-1.99 2.023-1.99h2.166V4.66c-.375-.05-1.66-.16-3.155-.16-3.123 0-5.26 1.905-5.26 5.405v3.016h-3.53v4.09h3.53V27.5h4.223z' data-evernote-id='1019' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Facebook](https://builtin.com/#facebook)  [![](data:image/svg+xml,%3csvg focusable='false' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' data-evernote-id='1444' class='js-evernote-checked'%3e%3cpath fill='%23FFF' d='M28 8.557a9.913 9.913 0 0 1-2.828.775 4.93 4.93 0 0 0 2.166-2.725 9.738 9.738 0 0 1-3.13 1.194 4.92 4.92 0 0 0-3.593-1.55 4.924 4.924 0 0 0-4.794 6.049c-4.09-.21-7.72-2.17-10.15-5.15a4.942 4.942 0 0 0-.665 2.477c0 1.71.87 3.214 2.19 4.1a4.968 4.968 0 0 1-2.23-.616v.06c0 2.39 1.7 4.38 3.952 4.83-.414.115-.85.174-1.297.174-.318 0-.626-.03-.928-.086a4.935 4.935 0 0 0 4.6 3.42 9.893 9.893 0 0 1-6.114 2.107c-.398 0-.79-.023-1.175-.068a13.953 13.953 0 0 0 7.55 2.213c9.056 0 14.01-7.507 14.01-14.013 0-.213-.005-.426-.015-.637.96-.695 1.795-1.56 2.455-2.55z' data-evernote-id='1021' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Twitter](https://builtin.com/#twitter)  [![](data:image/svg+xml,%3csvg focusable='false' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' data-evernote-id='1445' class='js-evernote-checked'%3e%3cpath fill='%23FFF' d='M24.412 21.177c0-.36-.126-.665-.377-.917l-2.804-2.804a1.235 1.235 0 0 0-.913-.378c-.377 0-.7.144-.97.43.026.028.11.11.255.25.144.14.24.236.29.29s.117.14.2.256c.087.117.146.232.177.344.03.112.046.236.046.37 0 .36-.126.666-.377.918a1.25 1.25 0 0 1-.918.377 1.4 1.4 0 0 1-.373-.047 1.062 1.062 0 0 1-.345-.175 2.268 2.268 0 0 1-.256-.2 6.815 6.815 0 0 1-.29-.29c-.14-.142-.223-.23-.25-.254-.297.28-.445.607-.445.984 0 .36.126.664.377.916l2.778 2.79c.243.243.548.364.917.364.36 0 .665-.118.917-.35l1.982-1.97c.252-.25.378-.55.378-.9zm-9.477-9.504c0-.36-.126-.665-.377-.917l-2.777-2.79a1.235 1.235 0 0 0-.913-.378c-.35 0-.656.12-.917.364L7.967 9.92c-.254.252-.38.553-.38.903 0 .36.126.665.38.917l2.802 2.804c.242.243.547.364.916.364.377 0 .7-.14.97-.418-.026-.027-.11-.11-.255-.25s-.24-.235-.29-.29a2.675 2.675 0 0 1-.2-.255 1.052 1.052 0 0 1-.176-.344 1.396 1.396 0 0 1-.047-.37c0-.36.126-.662.377-.914.252-.252.557-.377.917-.377.136 0 .26.015.37.046.114.03.23.09.346.175.117.085.202.153.256.2.054.05.15.148.29.29.14.146.222.23.25.258.294-.278.442-.606.442-.983zM27 21.177c0 1.078-.382 1.99-1.146 2.736l-1.982 1.968c-.745.75-1.658 1.12-2.736 1.12-1.087 0-2.004-.38-2.75-1.143l-2.777-2.79c-.75-.747-1.12-1.66-1.12-2.737 0-1.106.392-2.046 1.183-2.818l-1.186-1.185c-.774.79-1.708 1.186-2.805 1.186-1.078 0-1.995-.376-2.75-1.13l-2.803-2.81C5.377 12.82 5 11.903 5 10.826c0-1.08.382-1.993 1.146-2.738L8.128 6.12C8.873 5.372 9.785 5 10.864 5c1.087 0 2.004.382 2.75 1.146l2.777 2.79c.75.747 1.12 1.66 1.12 2.737 0 1.105-.392 2.045-1.183 2.817l1.186 1.186c.774-.79 1.708-1.186 2.805-1.186 1.078 0 1.995.377 2.75 1.132l2.804 2.804c.754.755 1.13 1.672 1.13 2.75z' data-evernote-id='1023' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)link](https://builtin.com/#link)  [![](data:image/svg+xml,%3csvg focusable='false' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' data-evernote-id='1446' class='js-evernote-checked'%3e%3cpath fill='%23FFF' d='M26 21.25v-9s-9.1 6.35-9.984 6.68C15.144 18.616 6 12.25 6 12.25v9c0 1.25.266 1.5 1.5 1.5h17c1.266 0 1.5-.22 1.5-1.5zm-.015-10.765c0-.91-.265-1.235-1.485-1.235h-17c-1.255 0-1.5.39-1.5 1.3l.015.14s9.035 6.22 10 6.56c1.02-.395 9.985-6.7 9.985-6.7l-.015-.065z' data-evernote-id='1025' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Email](https://builtin.com/#email)

From navigating to a new place to picking out new music, algorithms have laid the foundation for large parts of modern life. Similarly, artificial intelligence is booming because it automates and backs so many products and applications. Recently, I addressed some [analytical](https://builtin.com/data-science/linear-regression-tensorflow)  [applications](https://builtin.com/data-science/guide-logistic-regression-tensorflow-20) for TensorFlow. In this article, I’m going to lay out a higher-level view of Google’s TensorFlow deep learning framework, with the ultimate goal of helping you to understand and build deep learning algorithms from scratch.

## **An Introduction to Deep Learning **

Over the past couple of decades, deep learning has evolved rapidly, leading to massive disruption in a range of industries and organizations. The term was coined in 1943 when Warren McCulloch and Walter Pitts created a computer model based on neural networks of a human brain, creating the first artificial neural networks (or ANNs). Deep learning now denotes a branch of machine learning that deploys data-centric algorithms in real-time.

Backpropagation is a popular algorithm that has had a huge impact in the field of deep learning. It allows ANNs to learn by themselves based on the errors they generate while learning. To further enhance the scope of an ANN, architectures like Convolutional Neural Networks, Recurrent Neural Networks, and Generative Networks have come into the picture. Before we delve into them, let’s first understand the basic components of a neural network.

### **Neurons and Artificial Neural Networks**

An artificial neural network is a representational framework that extracts features from the data it’s given. The basic computational unit of an ANN is the neuron. Neurons are connected using artificial layers through which the information passes. As the information flows through these layers, the neural network identifies patterns between the data. This type of processing makes ANNs useful for several applications, such as for prediction and classification.

Now let’s take a look at the basic structure of an ANN. It consists of three layers: the input layer; the output layer, which is always fixed or constant; and the hidden layer. Inputs initially pass through an input layer. This layer always accepts a constant set of dimensions. For instance, if we wanted to train a classifier that differentiates between dogs and cats, the inputs (in this case, images) should be of the same size. The input then passes through the hidden layers and the network updates the weights and recognizes the patterns. In the final step, we classify the data at the output layer.

### **Weights and Biases**

Every neuron inside a neural network is associated with parameters, weight and bias. The weight is an integer that controls the signals between any two neurons. If the output is desirable, meaning that the output is in proximity to the one that we expected it to produce, then the weights are ideal. If the same network is generating an erroneous output that’s far away from the actual one, then the network alters the weights to improve the subsequent results.

Bias, the other parameter, is the algorithm’s tendency to consistently learn the wrong thing by not taking into account all the information in the data. For the model to be accurate, bias needs to be low. If there are inconsistencies in the data set, like missing values, fewer data tuples, or erroneous input data, the bias would be high and the predicted values could be wrong.

### **Working of a Neural Network**

Before we get started with TensorFlow, let’s examine how a neural network produces an output with weights, biases, and input by taking a look at the first neural network, called Perceptron, which dates back to 1958. The Perceptron network is a simple binary classifier. Understanding how this works will allow us to comprehend the workings of a modern neuron.

The Perceptron network is a supervised machine learning technique that uses a binary classifier function by mapping a vector of binary variables to a single binary output. It works as follows:

1. Multiply the inputs (x1, x2, x3) of the network to their corresponding weights (w1, w2, w3).

2. Add the multiplied weights and inputs together. This is called the weighted sum, denoted by, x1*w1 + x2*w2 +x3*w3.

3. Apply the activation function. Determine whether the weighted sum is greater than a threshold (say, 0.5), if yes, assign 1 as the output, otherwise assign 0. This is a simple step function.

Of course, Perceptron is a simple neural network that doesn’t wholly consider all the concepts necessary for an end-to-end neural network. Therefore, let’s go over all the phases that a neural network has to go through to build a sophisticated ANN.

### **Input**

A neural network has to be defined with the number of input dimensions, output features, and hidden units. All these metrics fall in a common basket called hyperparameters. Hyperparameters are numeric values that determine and define the neural network structure.

Weights and biases are set randomly for all neurons in the hidden layers.

### **Feed Forward**

The data is sent into the input and hidden layers, where the weights get updated for every iteration. This creates a function that maps the input with the output data. Mathematically, it is defined as *y=f(x)*, where *y* is the output, *x* is the input, and *f* is the activation function.

For every forward pass (when the data travels from the input to the output layer), the loss is calculated (actual value minus predicted value). The loss is again sent back (backpropagation) and the network is retrained using a loss function.

### **Output Error**

The loss is gradually reduced using gradient descent and loss function.
The gradient descent can be calculated with respect to any weight and bias.

### **Backpropagation**

We backpropagate the error that traverses through each and every layer using the backpropagation algorithm.

### **Output**

By minimizing the loss, the network re-updates the weights for every iteration (One Forward Pass plus One Backward Pass) and increases its accuracy.

As we haven’t yet talked about what an activation function is, I’ll expand that a bit in the next section.

### **Activation Functions**

An activation function is a core component of any neural network. It learns a non-linear, complex functional mapping between the input and the response variables or output. Its main purpose is to convert an input signal of a node in an ANN to an output signal. That output signal is the input to the subsequent layer in the stack. There are several types of activation functions available that could be used for different use cases. You can find a list comprising the most popular activation functions along with their respective mathematical formulae [here](https://towardsdatascience.com/complete-guide-of-activation-functions-34076e95d044).

Now that we understand what a feed forward pass looks like, let’s also explore the backward propagation of errors.

### **Loss Function and Backpropagation**

During training of a neural network, there are too many unknowns to be deciphered. As a result, calculating the ideal weights for all the nodes in a neural network is difficult. Therefore, we use an optimization function through which we could navigate the space of possible ideal weights to make good predictions with a [trained neural network](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/).

We use a gradient descent optimization algorithm wherein the weights are updated using the backpropagation of error. The term “gradient” in gradient descent refers to an error gradient, where the model with a given set of weights is used to make predictions and the error for those predictions is calculated. The gradient descent optimization algorithm is used to calculate the partial derivatives of the loss function (errors) with respect to any weight *w* and bias *b.* In practice, this means that the error vectors would be calculated commencing from the final layer, and then moving toward the input layer by updating the weights and biases, i.e., backpropagation. This is based on differentiations of the respective error terms along each layer. To make our lives easier, however, these loss functions and backpropagation algorithms are readily available in neural network frameworks such as TensorFlow and PyTorch.

Moreover, a hyperparameter called learning rate controls the rate of adjustment of weights of a network with respect to the gradient descent. The lower the learning rate, the slower we travel down the slope (to reach the optimum, or so-called ideal case) while calculating the loss.

## **Mechanics of TensorFlow 2.0**

TensorFlow is a powerful neural network framework that can be used to deploy high-level machine learning models into production. It was open-sourced by Google in 2015. Since then, its popularity has increased, making it a common choice for building deep learning models. On October 1, a new, stable version got released, called TensorFlow 2.0, with a few major changes:

- **Eager Execution by Default**: Instead of creating tf.session(), we can directly execute the code as usual Python code. In TensorFlow 1.x, we had to create a TensorFlow graph before computing any operation. In TensorFlow 2.0, however, we can build neural networks on the fly.
- **Keras Included**: Keras is a high-level neural network built on top of TensorFlow. It is now integrated into TensorFlow 2.0 and we can directly import Keras as tf.keras, and thereby define our neural network.
- **TF Data Sets**: A lot of new data sets have been added to work and play with in a new module called tf.data.
- **1.0 Support**: All the existing TensorFlow 1.x code can be executed using TensorFlow 2.0; we need not modify any of our previous code.
- Major documentation and API cleanup changes have also been introduced.

The TensorFlow library was built based on computational graphs a runtime for executing such computational graphs. Now, let’s perform a simple operation in TensorFlow.

	a = 13

	b = 24

	prod = a * b

	sum = a + b

	result = prod / sum

	print(res)

Here, we declared two variables *a* and *b*. We calculated the product of those two variables using a multiplication operation in Python (*) and stored the result in a variable called prod. Next, we calculated the sum of *a* and *b* and stored them in a variable named sum. Lastly, we declared the result variable that would divide the product by the sum and then would print it.

This explanation is just a Pythonic way of understanding the operation. In TensorFlow, each operation is considered as a computational graph. This is a more abstract way of describing a computer program and its computations. It helps in understanding the primitive operations and the order in which they are executed. In this case, we first multiply *a* and *b*, and only when this expression is evaluated, we take their sum. Later, we take prod and sum, and divide them to output the result.

### **TensorFlow Basics**

To get started with TensorFlow, we should be aware of a few essentials related to computational graphs. Let’s discuss them in brief:

- **Variables and Placeholders**: TensorFlow uses the usual variables, which can be updated at any point of time, except that these need to be initialized before the graph is executed. Placeholders, on the other hand, are used to feed data into the graph from outside. Unlike variables, they don’t need to be initialized. Consider a Regression equation, *y = mx+c*, where *x* and *y* are placeholders, and *m* and *c* are variables.
- **Constants and Operations**: Constants are the numbers that cannot be updated. Operations represent nodes in the graph that perform computations on data.
- **Graph**: The backbone that connects all the variables, placeholders, constants, and operators.

## **Installing TensorFlow 2.0**

Prior to installing TensorFlow 2.0, it’s essential that you have Python on your machine. Let’s look at its installation procedure.

### **Python for Windows**

You can download it [here](https://www.python.org/downloads/windows/).

Click on the “Latest Python 3 release - Python x.x.x”. Select the option that suits your system (32-bit - [Windows x86 executable installer](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe), or 64-bit - [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe)). After downloading the installer, follow the instructions that are displayed on the set-up wizard. Make sure to add Python to your PATH using environment variables.

### **Python for OSX**

You can download it [here.](https://www.python.org/downloads/mac-osx/)

Click on the “Latest Python 3 release - Python x.x.x”. Select “[macOS 64-bit installer](https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg),” and run the file.

Python on OSX can also be installed using Homebrew (package manager).
To do so, type the following commands:

	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

	export PATH="/usr/local/bin:/usr/local/sbin:$PATH"

	brew update

	brew install python

### **Python for Debian/Ubuntu**

Invoke the following commands:

	$ sudo apt update

	$ sudo apt install python3-dev python3-pip

This installs the latest version of Python and pip in your system.

### **Python for Fedora**

Invoke the following commands:

	$ sudo dnf update

	$ sudo dnf install python3 python3-pip

This installs the latest version of Python and pip in your system.
After you’ve got Python, it’s time to install TensorFlow in your workspace.

To fetch the latest version, “pip3” needs to be updated. To do so, type the command:

`$ pip3 install --upgrade pip`
Now, install TensorFlow 2.0.
`$ pip3 install --user --upgrade tensorflow`

This automatically installs the latest version of TensorFlow onto your system. The same command is also applicable to update the older version of TensorFlow.

The argument tensorflow in the above command could be any of these:

- tensorflow — Latest stable release (2.x) for CPU-only.
- tensorflow-gpu — Latest stable release with [GPU support](https://www.tensorflow.org/install/gpu) (Ubuntu and Windows).
- tf-nightly — Preview build (unstable). Ubuntu and Windows include [GPU support](https://www.tensorflow.org/install/gpu).
- tensorflow==1.15 — The final version of TensorFlow 1.x.

To verify your install, execute the code:

	$ python3 -c "import tensorflow as tf; print('tensorflow version', tf.__version__);print(tf.add(1, 2));"

	The output should be printed as follows:

	tensorflow version 2.0.0

	tf.Tensor(3, shape=(), dtype=int32)

## **Setting up the Environment: Jupyter**

Now that you have TensorFlow on your local machine, Jupyter notebooks are a handy tool for setting up the coding space. Execute the following command to install Jupyter on your system:

`$ pip3 install jupyter`

## **Working on Tensor Data**

Now that everything is set up, let’s explore the basic fundamentals of TensorFlow.

Tensors have previously been used largely in math and physics. In math, a tensor is an algebraic object that obeys certain transformation rules. It defines a mapping between objects and is similar to a matrix, although a tensor has no specific limit to its possible number of indices. In physics, a tensor has the same definition as in math, and is used to formulate and solve problems in areas like fluid mechanics and elasticity.

Although tensors were not deeply used in computer science, after the machine learning and deep learning boom, they have become heavily involved in solving data crunching problems.

### **Scalars**

The simplest tensor is a scalar, which is a single number and is denoted as a rank-0 tensor or a 0th order tensor. A scalar has magnitude but no direction.

### **Vectors**

A vector is an array of numbers and is denoted as a rank-1 tensor or a 1st order tensor. Vectors can be represented as either column vectors or row vectors.

A vector has both magnitude and direction. Each value in the vector gives the coordinate along a different axis, thus establishing direction. It can be depicted as an arrow; the length of the arrow represents the magnitude, and the orientation represents the direction.

### **Matrices**

A matrix is a 2-D array of numbers where each element is identified by a set of two numbers, row and column. A matrix is denoted as a rank-2 tensor or a 2nd order tensor. In simple terms, a matrix is a table of numbers.

### **Tensors**

A tensor is a multi-dimensional array with any number of indices. Imagine a 3-D array of numbers, where the data is arranged as a cube: that’s a tensor. When it’s an *n*D array of numbers, that's a tensor as well. Tensors are usually used to represent complex data. When the data has many dimensions (>=3), a tensor is helpful in organizing it neatly. After initializing, a tensor of any number of dimensions can be processed to generate the desired outcomes.

## **Mathematics With Tensors**

TensorFlow represents tensors with ease using simple functionalities defined by the framework. Further, the mathematical operations that are usually carried out with numbers are implemented using the functions defined by TensorFlow.

Firstly, let’s import TensorFlow into our workspace. To do so, invoke the following command:

`import  tensorflow  as   tf`
This enables us to use the variable *tf *thereafter.

Now, let’s take a quick overview of the basic operations and math, and you can simultaneously execute the code in the Jupyter playground for a better [understanding of the concepts](https://www.tensorflow.org/api_docs/python/tf/Variable).

### **tf.Tensor**

The primary object in TensorFlow that you play with is *tf.Tensor*. This is a tensor object that is associated with a value. It has two properties bound to it: data type and shape. The data type defines the type and size of data that will be consumed by a tensor. Possible types include float32, int32, string, etc. Shape defines the number of dimensions.

**tf.Variable()**

The variable constructor requires an argument which could be a tensor of any shape and type. After creating the instance, this variable is added to the TensorFlow graph and can be modified using any of the assign methods. It is declared as follows:

`tf.Variable("Hello World!", tf.string)`
**Output**
`<tf.Variable 'Variable:0' shape=() dtype=string, numpy=b'Hello World!'>`
**tf.constant()**

	tf.constant() can take the following arguments:

	tf.constant(

	    value,

	    dtype=None,

	    shape=None,

	    name='Const'

	)

The tensor is populated with a value, dtype**,** and, optionally, a shape. This value remains constant and cannot be modified further.

The following code snippet explains the creation of a constant tensor:
`tf.constant([1,2,3,4], shape=(2,2))`
**Output**

`<tf.Tensor: id=180, shape=(2, 2), dtype=int32, numpy, array([[1, 2],  [3, 4]], dtype=int32)>`

A few basic operations to start with will give you a glimpse at how TensorFlow works.

### **Declaring a Scalar**

Rank-0 tensors can be declared as follows:
**Using tf.Variable**

	float_var = tf.Variable(19.99, tf.float32, name="float")

	int_var = tf.Variable(11, tf.int64)

	string_var = tf.Variable("Cookie", tf.string)

	print("{0}, {1}, {2}".format(float_var, int_var, string_var))

**Output**

`<tf.Variable 'float:0' shape=() dtype=float32, numpy=19.99>, <tf.Variable 'Variable:0' shape=() dtype=int32, numpy=11>, <tf.Variable 'Variable:0' shape=() dtype=string, numpy=b'Cookie'>`

The *name* parameter assigns an optional name to the tensor.
*The shape* was empty because the values being printed there are scalars.
**Using tf.constant**

	float_cons = tf.constant(19.99)

	int_cons = tf.constant(11, dtype=tf.int32)

	string_cons = tf.constant("Cookie", name="string")

	print("{0}, {1}, {2}".format(float_cons, int_cons, string_cons))

**Output**
`19.989999771118164, 11, b'Cookie'`
*b* around the word Cookie indicates that it is a bytes object.

### **Declaring a Vector**

Rank-1 tensors can be declared as follows:
**Using tf.Variable**

	float_var = tf.Variable([19.99], tf.float32, name="float")

	int_var = tf.Variable([11, 19], tf.int64)

	string_var = tf.Variable(["Cookie", "Monster"], tf.string)

	print("{0}, {1}, {2}".format(float_var, int_var, string_var))

**Output**

	<class 'tensorflow.python.ops.resource_variable_ops.ResourceVariable'>

	<tf.Variable 'float:0' shape=(1,) dtype=float32, numpy=array([19.99], dtype=float32)>, <tf.Variable 'Variable:0' shape=(2,) dtype=int32, numpy=array([11, 19], dtype=int32)>, <tf.Variable 'Variable:0' shape=(2,) dtype=string, numpy=array([b'Cookie', b'Monster'], dtype=object)>

*array* indicates that the output is a list of values.
**Using tf.constant**

	float_cons = tf.constant([19.99])

	int_cons = tf.constant([11, 19], dtype=tf.int32)

	string_cons = tf.constant(["Cookie", "Monster"], name="string")

	print("{0}, {1}, {2}".format(float_cons, int_cons, string_cons))

**Output**
`[19.99], [11 19], [b'Cookie' b'Monster']`

### **Declaring a Matrix**

Rank-2 tensors can be declared as follows:
**Using**  **tf.Variable**

	float_var=tf.Variable([[19.99],[11.11]],tf.float32,name="float")

	int_var = tf.Variable([[11, 19]], tf.int64)

	string_var=tf.Variable([["Cookie","Monster"],["Ice","Cream"]], tf.string)

	print("{0}, {1}, {2}".format(float_var, int_var, string_var))

**Output**

`<tf.Variable 'float:0' shape=(2, 1) dtype=float32, numpy= array([[19.99], [11.11]], dtype=float32)>, <tf.Variable 'Variable:0' shape=(1, 2) dtype=int32, numpy=array([[11, 19]], dtype=int32)>, <tf.Variable 'Variable:0' shape=(2, 2) dtype=string, numpy= array([[b'Cookie', b'Monster'],[b'Ice', b'Cream']], dtype=object)>`

The *shape* parameter in the output was initialized with the respective shapes of the declared tensors. The first one was a 2x1 matrix (2 rows and 1 column). The second one was a 1x2 matrix, and the 3rd one was a 2x2 matrix.

**Using tf.constant**

	float_cons = tf.constant([[19.99], [11.11]])

	int_cons = tf.constant([[11, 19]], dtype=tf.int32)

	string_cons = tf.constant([["Cookie", "Monster"], ["Ice", "Cream"]], name="string")

	print("{0}, {1}, {2}".format(float_cons, int_cons, string_cons))

**Output**

	[[19.99]

	[11.11]], [[11 19]], [[b'Cookie' b'Monster']

	[b'Ice' b'Cream']]

### **Basic Operations**

Now that we’ve thoroughly explored the initializations, have let’s perform some basic operations using TensorFlow.

**tf.zeros()/tf.ones()/tf.fill()**

tf.zeros() takes the shape as an argument and returns a tensor filled with zeros.

tf.ones() takes the shape as an argument and returns a tensor filled with ones.

tf.fill() allows initializing a tensor with a random value, not limiting to 0 or 1.

	zero_tensor = tf.zeros(2,dtype=tf.float32)

	print(zero_tensor)

	print(zero_tensor.numpy())

	one_tensor = tf.ones((2,2),dtype=tf.int32)

	print(one_tensor)

	print(one_tensor.numpy())

	fill_tensor = tf.fill((2,2),value=3.)

	print(fill_tensor)

	print(fill_tensor.numpy())

**Output**

	tf.Tensor([0. 0.], shape=(2,), dtype=float32)

	[0. 0.]

	tf.Tensor(

	[[1 1]

	 [1 1]], shape=(2, 2), dtype=int32)

	[[1 1]

	 [1 1]]

	tf.Tensor(

	[[3. 3.]

	 [3. 3.]], shape=(2, 2), dtype=float32)

	[[3. 3.]

	 [3. 3.]]

*zero_tensor, one_tensor, fill_tensor* are the references that point to the tensors created. To extract the values stored, *numpy()* was used. This returned *numpy.ndarray* objects.

**Slicing Tensors**
To access a value from a vector, invoke the following code:

	float_vector = tf.constant([2,2.3])

	float_vector.numpy()[0]

**Output**
`2.0`
*[0] *returned the value at the 0th index.
To access a value from a matrix, invoke the following code:

	string_matrix = tf.constant([["Hello", "World"]])

	string_matrix.numpy()[0,1]

**Output**
`b'World'`
*[0, 1] *returned the value present at the 0th row and 1st column.
To slice a matrix, invoke the following code:

	string_matrix = tf.constant([["Hello", "World", "!"], ["Tensorflow", "is", "here"]])

	print(string_matrix.numpy()[1, 2])

	print(string_matrix.numpy()[:1])

	print(string_matrix.numpy()[:, 1])

	print(string_matrix.numpy()[1, :])

**Output**

	b'here'

	[[b'Hello' b'World' b'!']]

	[b'World' b'is']

	[b'Tensorflow' b'is' b'here']

[1, 2] extracted the element present at the 1st row and 2nd column.
[:1] extracted the 1st row (all the rows before 1).
[:, 1] extracted the 1st column.
[1, :] extracted the 1st row.

### **Tensor Shape**

To access the shape of a tensor, invoke the following code:

	string_matrix = tf.constant([["Hello", "World", "!"], ["Tensorflow", "is", "here"]])

	string_matrix.shape

**Output**
`TensorShape([2, 3])`
There were two rows and three columns in the given tensor.

### **Math Operations**

Let’s look at a few math operations that can be implemented using TensorFlow.
**Element-Wise Math**

Here’s a code snippet that compares add, subtract, multiply, and division functions:

	x = tf.constant([2, 2, 2])

	y = tf.constant([3, 3, 3])

	print((x+y).numpy())

	print(tf.add(x, y).numpy())

	print((x-y).numpy())

	print(tf.subtract(x, y).numpy())

	print((x*y).numpy())

	print(tf.multiply(x, y).numpy())

	print((x/y).numpy())

	print(tf.divide(x, y).numpy())

**Output**

	[5 5 5]

	[5 5 5]

	[-1 -1 -1]

	[-1 -1 -1]

	[6 6 6]

	[6 6 6]

	[0.66666667 0.66666667 0.66666667]

	[0.66666667 0.66666667 0.66666667]

Both the operators and the TensorFlow functions gave identical outputs. All the operations were implemented element-wise.

**Tensor Reshape**

tf.reshape() returns a tensor that has values rearranged with respect to the shape given as an argument. Take a look at this code snippet:

	x = tf.constant([[1, 2, 3]])

	print(x.shape)

	x = tf.reshape(x, [3,1])

	print(x.shape)

	print(x.numpy())

	x = tf.reshape(x, [-1])

	print(x.shape)

	print(x.numpy())

**Output**

	(1, 3)

	(3, 1)

	[[1]

	 [2]

	 [3]]

	(3,)

	[1 2 3]

Initially, the shape of the tensor was (1, 3). It was then reshaped to (3, 1). When the tensor was reshaped to [-1], the size was computed such that the total size remained constant. To be precise, the shape flattened to a 1D array.

**Matrix Multiplication**

Let’s now see how Tensorflow does matrix multiplication using the following code snippet:

	x = tf.constant([[3., 3.]])

	y = tf.constant([[1., 2., 3.], [4., 5., 6.]])

	tf.matmul(x, y).numpy()

**Output**

	array([[15., 21., 27.]], dtype=float32)

	x’s shape was (1, 2) and y’s shape was (2, 3). When multiplied, the resultant shape was (1, 3).

## **TensorBoard**

TensorBoard is Tensorflow’s visualization tool kit. By simply integrating TensorBoard into your neural networks, you can track all the metrics recorded during the training process, and thereby estimate the performance of the neural network. Using TensorBoard, you can also view histograms of weights, biases, and other tensors as they change over time. This not only helps you in visualizing data but also assists you to tweak your neural network so that its performance and accuracy are high.

Many people out there are passionate about deep learning and artificial intelligence but aren’t sure of the prerequisites and basic fundamentals for getting started. This tutorial can help you carve your own path and serve as a guide while you build your own deep learning or machine learning models from scratch.

Expert Contributors

Built In’s expert contributor network publishes thoughtful, solutions-oriented stories written by innovative tech professionals. It is the tech industry’s definitive destination for sharing compelling, first-person accounts of problem-solving on the road to innovation.

[Learn More](https://builtin.com/contributors)