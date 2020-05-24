A thread written by @fchollet

[**](https://twitter.com/fchollet/status/1105139360226140160)

 [![8FUPfeY0_400x400.jpg](../_resources/e611400ba5465c2e1ff89870716b55c9.jpg)](https://threader.app/@fchollet)

 [François Chollet](https://threader.app/@fchollet)  [@fchollet](https://threader.app/@fchollet)  Deep learning @google. Creator of Keras, neural networks library. Author of 'Deep Learning with Python'. Opinions are my own.  [Mar. 11, 2019](https://twitter.com/fchollet/status/1105139360226140160)  ** 3 min read

Are you a deep learning researcher? Wondering if all this TensorFlow 2.0 stuff you heard about is relevant to you?

This thread is a crash course on everything you need to know to use TensorFlow 2.0 + Keras for deep learning research. Read on!

 [![D1Y9xiNU0AAXez4.png](../_resources/8ba8550fb23dfbc95f53e06ed59b6464.png)](https://pbs.twimg.com/media/D1Y9xiNU0AAXez4.png)

1) The first class you need to know is `Layer`. A Layer encapsulates a state (weights) and some computation (defined in the `call` method).

 [![D1Y98h9VYAAMsO0.jpg](../_resources/e002ddf06b0b8aa03dfe5a8b2c8873d0.jpg)](https://pbs.twimg.com/media/D1Y98h9VYAAMsO0.jpg)

2) The `add_weight` method gives you a shortcut for creating weights.

3) It’s good practice to create weights in a separate `build` method, called lazily with the shape of the first inputs seen by your layer. Here, this pattern prevents us from having to specify `input_dim`:

 [![D1Y-krTVYAAiZI9.jpg](../_resources/3650a9389a8ca040f2c2080f65a574d6.jpg)](https://pbs.twimg.com/media/D1Y-krTVYAAiZI9.jpg)

4) You can automatically retrieve the gradients of the weights of a layer by calling it inside a GradientTape. Using these gradients, you can update the weights of the layer, either manually, or using an optimizer object. Of course, you can modify the gradients before using them.

 [![D1Y-tSmUwAAAixK.jpg](../_resources/96347f169e04cbc31d64d3ee4947f346.jpg)](https://pbs.twimg.com/media/D1Y-tSmUwAAAixK.jpg)

5) Weights created by layers can be either trainable or non-trainable. They're exposed in the layer properties `trainable_weights` and `non_trainable_weights`. Here's a layer with a non-trainable weight:

 [![D1Y--HqVAAAR_2V.jpg](../_resources/f8ecb2c2c3667d6f132331339d379ee6.jpg)](https://pbs.twimg.com/media/D1Y--HqVAAAR_2V.jpg)

6) Layers can be recursively nested to create bigger computation blocks. Each layer will track the weights of its sublayers (both trainable and non-trainable).

 [![D1Y_NTxUcAAfznr.jpg](../_resources/caec01f4caabe0ed87a69756a9602455.jpg)](https://pbs.twimg.com/media/D1Y_NTxUcAAfznr.jpg)

7) Layers can create losses during the forward pass. This is especially useful for regularization losses. The losses created by sublayers are recursively tracked by the parent layers.

 [![D1Y_hhSU4AAsJnO.jpg](../_resources/52b107bf6a9b1e3ad6f671fb9c989b0a.jpg)](https://pbs.twimg.com/media/D1Y_hhSU4AAsJnO.jpg)

8) These losses are cleared by the top-level layer at the start of each forward pass -- they don't accumulate. `layer.losses` always contain only the losses created during the *last* forward pass. You would typically use these losses by summing them when writing a training loop.

 [![D1Y_ymLVYAANNLZ.jpg](../_resources/191ec2f76eb2f83aafe2b6668149ff2d.jpg)](https://pbs.twimg.com/media/D1Y_ymLVYAANNLZ.jpg)

9) You know that TF 2.0 is eager by default. Running eagerly is great for debugging, but you will get better performance by compiling your computation into static graphs. Static graphs are a researcher's best friends! You can compile any function by wrapping it in a tf.function:

 [![D1ZAFPFVYAIgisO.jpg](../_resources/117441d67706db43ac5f0745bc459923.jpg)](https://pbs.twimg.com/media/D1ZAFPFVYAIgisO.jpg)

10) Some layers, in particular the `BatchNormalization` layer and the `Dropout` layer, have different behaviors during training and inference. For such layers, it is standard practice to expose a `training` (boolean) argument in the `call` method.

 [![D1ZAV0tUcAAm3DK.jpg](../_resources/aa404360b5e7d7b9e0656f23bf8164ae.jpg)](https://pbs.twimg.com/media/D1ZAV0tUcAAm3DK.jpg)

11) You have many built-in layers available, from Dense to Conv2D to LSTM to fancier ones like Conv2DTranspose or ConvLSTM2D. Be smart about reusing built-in functionality.

12) To build deep learning models, you don't have to use object-oriented programming all the time. All layers we've seen so far can also be composed functionally, like this (we call it the "Functional API"):

 [![D1ZA16gV4AEhPPP.jpg](../_resources/7dbcc2d7caf7334ef8596a71e99b6ebf.jpg)](https://pbs.twimg.com/media/D1ZA16gV4AEhPPP.jpg)

The Functional API tends to be more concise than subclassing, & provides a few other advantages (generally the same advantages that functional, typed languages provide over untyped OO development).

Learn more about the Functional API: [ https://www.tensorflow.org/alpha/guide/keras/functional …](https://www.tensorflow.org/alpha/guide/keras/functional)

However, note that the Functional API can only be used to define DAGs of layers -- recursive networks should be defined as `Layer` subclasses instead.

In your research workflows, you may often find yourself mix-and-matching OO models and Functional models.

That's all you need to get started with reimplementing most deep learning research papers in TensorFlow 2.0 and Keras!

Now let's check out a really quick example: hypernetworks.

A hypernetwork is a deep neural network whose weights are generated by another network (usually smaller).

Let's implement a really trivial hypernetwork: we'll take the `Linear` layer we defined earlier, and we'll use it to generate the weights of... another `Linear` layer.

 [![D1ZB6E_UwAIsj9x.jpg](../_resources/63fb4ccf46326e884fd188cb65178c6c.jpg)](https://pbs.twimg.com/media/D1ZB6E_UwAIsj9x.jpg)

Another quick example: implementing a VAE in either style, either subclassing (left) or the Functional API (right). I've posted this before. Find what works best for you!

 [![D1ZCX-vVYAMwT3g.jpg](../_resources/cd15b7930831bf56788b96ad69261f97.jpg)](https://pbs.twimg.com/media/D1ZCX-vVYAMwT3g.jpg)

 [![D1ZCbB8UwAAXdRc.jpg](../_resources/0d99799d300cccadb4724b97b93a078a.jpg)](https://pbs.twimg.com/media/D1ZCbB8UwAAXdRc.jpg)

This is the end of this thread. Play with these code examples in this Colab notebook: [ https://colab.research.google.com/drive/17u-pRZJnKN0gO5XZmq8n5A2bKGrfKEUg …](https://colab.research.google.com/drive/17u-pRZJnKN0gO5XZmq8n5A2bKGrfKEUg)

You can follow [@fchollet](https://twitter.com/intent/user?screen_name=fchollet).

 Share this threadBookmark

- [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://threader.app/thread/1105139360226140160)

- [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://threader.app/thread/1105139360226140160)

- [Twitter](https://twitter.com/intent/tweet/?text=A%20thread%20written%20by%20@fchollet%0A%0A%22Are%20you%20a%20deep%20learning%20researcher%3F%20Wondering%20if%20all%20this%20TensorFlow%202.0%20stuff%20you%20heard%20about%20is%20relevant%20to%20you%3FThis%20thread%20is%20a%20crash%20cou...%22%0A%0A&url=https://threader.app/thread/1105139360226140160)

- ![](../_resources/50b815d850e07127f3af943bf8619b2f.png)

____

Tip: mention [@threader_app](https://twitter.com/intent/user?screen_name=threader_app) on a Twitter thread with the keyword “compile” to get a link to it.

Enjoy Threader? [Sign up](https://threader.app/thread/1105139360226140160#).