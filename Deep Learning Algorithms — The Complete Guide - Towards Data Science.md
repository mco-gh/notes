Deep Learning Algorithms — The Complete Guide - Towards Data Science

# Deep Learning Algorithms — The Complete Guide

## An in-depth look at the world of deep learning.

[![1*GfL34oZT9toWlXesrzHgyw.png](../_resources/a918651e898c585b3b197f148fdbd84b.png)](https://towardsdatascience.com/@oleksii_kh?source=post_page-----ce020bd47ecc----------------------)

[Oleksii Kharkovyna](https://towardsdatascience.com/@oleksii_kh?source=post_page-----ce020bd47ecc----------------------)

[Apr 7](https://towardsdatascience.com/deep-learning-algorithms-the-complete-guide-ce020bd47ecc?source=post_page-----ce020bd47ecc----------------------) · 11 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='202'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='203' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='208'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/ce020bd47ecc/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='217'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='218' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/ce020bd47ecc/share/facebook?source=post_actions_header---------------------------)

![0*X-8JujhipM_LwaJS.jpeg](../_resources/29640560be7fb236e92b65935cb53f3e.jpg)
![0*X-8JujhipM_LwaJS.jpeg](../_resources/7b56137d5dc10f38c7a74c6ac8c4853d.jpg)
Credit: https://unsplash.com/

Deep learning is a hyponym in relation to “machine learning”, which in turn is a hyponym in relation to artificial intelligence. Over the past few years, the term of deep learning has appeared too often: the most widespread use case is image processing. And although the face recognition function has existed for a long time, there is no limit to perfection.

It seems chaotic for someone who wants to start from scratch deep learning. How to understand how it works? Instead of the hype terms, let’s talk about real algorithms and maybe the good old mathematics behind them. My main goal is to give you a general idea of the field and help you understand what algorithm you should use in each specific case. A maximum of non-boring explanations, a minimum of complex phrases. Let’s dive into serious material.

Let’s roll.

# Neural networks: basics

Neural networks are a computing system with interconnected nodes that work more like the neurons in a human brain. These neurons process and transmit information between themselves. Each neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.

![0*b-64yAvDuBSI6-uU](../_resources/1c18b428095b82d4afa2a0df919296a9.png)
![0*b-64yAvDuBSI6-uU](../_resources/8358935e31a36479334d04c9e92e8fb0.png)

Credit: [*http://www.sci.utah.edu/*](http://www.sci.utah.edu/~beiwang/teaching/cs6965-fall-2019/Lecture15-DeepLearningVis.pdf)

What is the difference between the deep learning algorithm and a typical neural network? The most obvious difference: the neural network used in deep learning has more hidden layers. These layers are between the first, or input, and last, output, layer of neurons. Moreover, it is not necessary to connect all neurons at different levels to each other.

If you are not yet well-oriented in this, I suggest you get familiar with the basics of neural networks. One of my previous articles — [A Comprehensive Guide to Neural Networks for Beginners](https://towardsdatascience.com/a-comprehensive-guide-on-neural-networks-for-beginners-a4ca07cee1b7) — will be a great option for this.

# 9 Deep Learning algorithms you should know

![0*vBqCwUB7ldqNAhaS](../_resources/83c7a23dfa754d927aaf70fbb9968ecb.png)
![0*vBqCwUB7ldqNAhaS](../_resources/dfac76e9f4756874163eb8071ed0a612.png)
Credit: https://unsplash.com/

Now let’s talk about more complex things. Deep learning algorithms, or put it differently, mechanisms that allow us to use this cutting-edge technology:

**#1 Backpropagation**

The backpropagation algorithm is a popular supervised algorithm for training feedforward neural networks for supervised learning. Essentially, backpropagation evaluates the expression for the derivative of the cost function as a product of derivatives between each layer from left to right — “backwards” — with the gradient of the weights between each layer being a simple modification of the partial products (the “backwards propagated error”).

We feed the network with data, it produces an output, we compare that output with a desired one (using a loss function) and we readjust the weights based on the difference. And repeat. And repeat. The adjustment of weights is performed using a non-linear optimization technique called stochastic gradient descent.

Let’s say that for some reason we want to identify images with a tree. We feed the network with any kind of images and it produces an output. Since we know if the image has actually a tree or not, we can compare the output with our truth and adjust the network. As we pass more and more images, the network will make fewer and fewer mistakes. Now we can feed it with an unknown image, and it will tell us if the image contains a tree. Pretty cool, right?

Great article to go deeper: [Neural networks and back-propagation explained in a simple way](https://medium.com/datathings/neural-networks-and-backpropagation-explained-in-a-simple-way-f540a3611f5e)

**#2 Feedforward Neural Networks (FNN)**

Feedforward Neural Networks are usually fully connected, which means that every neuron in a layer is connected with all the other neurons in the next layers. The described structure is called Multilayer Perceptron and originated back in 1958. Single-layer perceptron can only learn linearly separable patterns, but a multilayer perceptron is able to learn non-linear relationships between the data.

The goal of a feedforward network is to approximate some function f. , **ﬁ**, = (x) maps an input x to a category y. A feedforward network deﬁnes a mapping y = f(x;θ) and learns the value of the parameters θ that result in the best function approximation.

![0*wCJvkSsJyDozgbZT](../_resources/0bb2e848a4b65ae36175c084e5e5c8c4.png)
![0*wCJvkSsJyDozgbZT](../_resources/1d13193cccf1ff259d2bb18ae323110f.png)

Credit: [*http://www.sci.utah.edu/*](http://www.sci.utah.edu/~beiwang/teaching/cs6965-fall-2019/Lecture15-DeepLearningVis.pdf)

These models are called feedforward because information ﬂows through the function being evaluated from x, through the intermediate computations used to deﬁne f, and ﬁnally to the output y. There are no feedback connections in which outputs of the model are fed back into itself. When feedforward neural networks are extended to include feedback connections, they are called recurrent neural networks.

**#3 Convolutional Neural Networks (CNN)**

ConvNets have been successful in identifying faces, objects, and traffic signs apart from powering vision in robots and self-driving cars.

From the Latin convolvere, “to convolve” means to roll together. For mathematical purposes, convolution is the integral measuring of how much two functions overlap as one passes over the other. Think of convolution as a way of mixing two functions by multiplying them.

![0*J3-ipcs1yy0tumgG](../_resources/6c4f97c675b6a84a979773fc0f57d531.gif)
![0*J3-ipcs1yy0tumgG](../_resources/6c4f97c675b6a84a979773fc0f57d531.gif)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

The green curve shows the convolution of the blue and red curves as a function of t, the position indicated by the vertical green line. The gray region indicates the product g(tau)f(t-tau) as a function of t, so its area as a function of t is precisely the convolution.”

The product of those two functions’ overlap at each point along the x-axis is their convolution. So in a sense, the two functions are being “rolled together.”

![0*suj-5_H0zV8do2AV](../_resources/333b0c3db5113c9ddca5d2ffc3195ada.png)
![0*suj-5_H0zV8do2AV](../_resources/72561515d6032dd51c2eab3965b7d05f.png)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

In a way, they try to regularize feedforward networks to avoid overfitting (when the model learns only pre-seen data and can’t generalize), which makes them very good in identifying spatial relationships between the data.

Another great article I will certainly recommend — [The best explanation of Convolutional Neural Networks on the Internet!](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8)

**#4 Recurrent Neural Networks (RNN)**

Recursive neural networks are very successful in many NLP tasks. The idea of RNN is to consistently use information. In traditional neural networks, it is understood that all inputs and outputs are independent. But for many tasks this is not suitable. If you want to predict the next word in a sentence, it is better to consider the words preceding it.

RNNs are called recurrent because they perform the same task for each element of the sequence, and the output depends on previous calculations. Another interpretation of RNN: these are networks that have a “memory” that takes into account prior information.

![0*3MnprCUhI7IQbEDF](../_resources/096570bb240fa7a9f64feb83c3a52517.png)
![0*3MnprCUhI7IQbEDF](../_resources/cbfe076d3b826b4b63625ac57c455fcf.png)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

The diagram above shows that the RNN is deployed to a complete network. By sweep, we simply write out the network for complete consistency. For example, if the sequence is a sentence of 5 words, the sweep will consist of 5 layers, a layer for each word.

The formulas that define the calculations in RNN are as follows:

- x_t — input at time step t. For example, x_1 may be a one-hot vector corresponding to the second word of a sentence.
- s_t is the hidden state in step t. This is the “memory” of the network. s_t depends, as a function, on previous states and the current input x_t: s_t = f (Ux_t + Ws_ {t-1}). The function f is usually non-linear, for example tanh or ReLU. s _ {- 1}, which is required to compute the first hidden state, is usually initialized to zero (zero vector).
- o_t — exit at step t. For example, if we want to predict a word in a sentence, the output may be a probability vector in our dictionary. o_t = softmax (Vs_t)

**Generation of image descriptions**

Together with convolutional neural networks, RNNs were used as part of the model for generating descriptions of unlabeled images. The combined model combines the generated words with the features found in the images:

![0*tt7yJIwafTYdOIqD](../_resources/170ac8be5aaa702320671efb2a030dd1.png)
![0*tt7yJIwafTYdOIqD](../_resources/00e6d4260cf8176c986f6f85d060ffdb.png)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

It is also not impossible not to mention that the most commonly used type of RNNs are LSTMs, which capture (store) long-term dependencies much better than RNNs. But don’t worry, LSTMs are essentially the same as RNNs, they just have a different way of calculating the hidden state.

The memory in LSTM is called cells, and you can think of them as black boxes that accept the previous state h_ {t-1} and the current input parameter x_t as input. Inside, these cells decide which memory to save and which to erase. Then they combine the previous state, current memory and input parameter.

These types of units are very effective in capturing (storing) long-term dependencies.

**#5 Recursive Neural Network**

Recursive Neural Networks are another form of recurrent networks with the difference that they are structured in a tree-like form. As a result, they can model hierarchical structures in the training dataset.

They are traditionally used in NLP in applications such as Audio to text transcription and sentiment analysis because of their ties to binary trees, contexts, and natural-language-based parsers. However, they tend to be much slower than Recurrent Networks

**#6 AutoEncoders**

Auto encoders are direct distribution neural networks that restore the input signal at the output. Inside they have a hidden layer, which is a code that describes the model. Auto encoders are designed to not be able to accurately copy the input to the output. Usually, they are limited in the dimension of the code (it is smaller than the dimension of the signal) or fined for activation in the code. The input signal is restored with errors due to coding losses, but in order to minimize them, the network is forced to learn to select the most important features.

![0*UlEytRs7TaraxQeb](../_resources/6dc80d28b8f998e1a989f2effc5bdab3.png)
![0*UlEytRs7TaraxQeb](../_resources/69e31d884363d39c587b0507648d2e6c.png)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

Auto encoders can be used for pre-training, for example, when there is a classification task, and there are too few marked pairs. Or to lower the dimension in the data for later visualization. Or when you just need to learn to distinguish between the useful properties of the input signal.

Moreover, some of their developments (which will also be described later), such as variational auto-encoder (VAE), as well as its combination with competing generative networks (GAN), give very interesting results and are now at the forefront of the science of generative models.

**#7 Deep Belief Networks and Restricted Boltzmann Machines**

Restricted Boltzmann Machine is a stochastic neural network (neural network meaning we have neuron-like units whose binary activations depend on the neighbors they’re connected to; stochastic meaning these activations have a probabilistic element) consisting of:

- One layer of** visible units** (users’ movie preferences whose states we know and set);
- One layer of** hidden units **(the latent factors we try to learn); and
- A **bias unit** (whose state is always on, and is a way of adjusting for the different inherent popularities of each movie).

Furthermore, each visible unit is connected to all the hidden units (this connection is undirected, so each hidden unit is also connected to all the visible units), and the bias unit is connected to all the visible units and all the hidden units.

![0*u69WdVKxXLX_M-XF](../_resources/683a76c7177e5cae4561cdf7b690d67f.png)
![0*u69WdVKxXLX_M-XF](../_resources/ecd242064dccd0288894d2894fab57a3.png)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

To make learning easier, we restrict the network so that no visible unit is connected to any other visible unit and no hidden unit is connected to any other hidden unit.

Multiple RBM can be stacked to form a Deep Belief Network. They look exactly like Fully Connected layers, but they differ in how they are trained.

**#8 Generative Adversarial Networks (GAN)**

GANs are becoming a popular ML model for online retail sales because of their ability to understand and recreate visual content with increasingly remarkable accuracy. Use cases include:

- Filling in images from an outline.
- Generating a realistic image from text.
- Producing photorealistic depictions of product prototypes.
- Converting black and white imagery into color.

In video production, GANs can be used to:

- Model patterns of human behavior and movement within a frame.
- Predict subsequent video frames.
- Create deepfake

A generative adversarial network (GAN) has two parts:

- The** generator** learns to generate plausible data. The generated instances become negative training examples for the discriminator.
- The **discriminator** learns to distinguish the generator’s fake data from real data. The discriminator penalizes the generator for producing implausible results.

The first step in establishing a GAN is to identify the desired end output and gather an initial training dataset based on those parameters. This data is then randomized and input into the generator until it acquires basic accuracy in producing outputs.

![0*FEcOLgMXMG3b8QrE](:/10f42aceb36a9793310ea98bb4ed6a08)
![0*FEcOLgMXMG3b8QrE](../_resources/d1e92b4bd414ac03e722783e3efa01df.png)
Credit: [Mathworld.](https://mathworld.wolfram.com/)

After this, the generated images are fed into the discriminator along with actual data points from the original concept. The discriminator filters through the information and returns a probability between 0 and 1 to represent each image’s authenticity (1 correlates with real and 0 correlates with fake). These values are then manually checked for success and repeated until the desired outcome is reached.

**#9 Transformers**

Transformers are also very new, and they are mostly used in language applications as they are starting to make recurrent networks obsolete. They based on a concept called attention, which is used to force the network to focus on a particular data point.

Instead of having overly complex LSTM units, you use Attention mechanisms to weigh different parts of the input based on their significance. The attention mechanism is nothing more than another layer with weights and its sole purpose is to adjust the weights in a way that prioritizes segments of inputs while deprioritizing others.

Transformers, in fact, consist of a number of stacked encoders (form the encoder layer), a number of stacked decoders (the decoder layer) and a bunch of attention layers (self- attentions and encoder-decoder attentions)

![0*5ZXbjtYEc3ebp_TH](../_resources/fc29c78f2bcba2e9a6220c458c59d412.png)
![0*5ZXbjtYEc3ebp_TH](../_resources/3f05f0a6806c07e0fbf9b97aee07e8af.png)

Credit: [*http://jalammar.github.io/illustrated-transformer/*](http://jalammar.github.io/illustrated-transformer/)

Transformers are designed to handle ordered sequences of data, such as natural language, for various tasks such as machine translation and text summarization. Nowadays BERT and GPT-2 are the two most prominent pretrained natural language systems, used in a variety of NLP tasks, and they are both based on Transformers.

**#10 Graph Neural Networks**

Unstructured data are not a great fit for Deep Learning in general. And there are many real-world applications where data are unstructured and organized in a graph format. Think social networks, chemical compounds, knowledge graphs, spatial data.

Graph Neural Networks purpose is to model Graph data, meaning that they identify the relationships between the nodes in a graph and produce a numeric representation of it. Just like an embedding. So, they can later be used in any other machine learning model for all sorts of tasks like clustering, classification, etc.

………………………

*If you do anything cool with this information, leave a response in the comments below or reach out at any time on my *[*Instagram*](https://www.instagram.com/miallez/)* and *[*Medium*](https://medium.com/@oleksii_kh)* blog. Also welcome to visit my *[*Linkedin*](https://www.linkedin.com/in/kharkovinaalexey/)*.*