An Intuitive Explanation to AutoEncoders – Towards Data Science

# An Intuitive Explanation to AutoEncoders

## and how to implement them in Keras

[![1*j3ikJ7by22rYNJmmvCoisw.jpeg](../_resources/4688cf28319c2186d7e96b8a0d68c80a.jpg)](https://towardsdatascience.com/@alimasri1991?source=post_header_lockup)

[Ali Masri](https://towardsdatascience.com/@alimasri1991)

Jun 4·4 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='121'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

![](../_resources/b9f970c88ffeeb3a1c4a494a806fb4ec.png)![0*WBW_TCGwzVTURL_p](../_resources/acfa4ea38fb769136de1693527e57adf.jpg)

Photo by [Aditya Chinchure](https://unsplash.com/@adityachinchure?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

### **Motivation**

Many of the recent deep learning models rely on extracting complex features from data. The goal is to transform the input from its raw format, to another representation calculated by the neural network. This representation contains features that describe hidden unique characteristics about the input.

Consider a dataset of people faces, where each input is an image of a person. The representation of an image in its raw format is too complex to be used by machines. Instead, why not make the neural network automatically calculate important features for each face, something maybe like: eye type, nose type, distance between eyes, nose position, etc. Well, this sounds interesting… Using these features, we could easily **compare two faces**,** find similar faces**, **generate new faces**, and many other interesting applications.

This concept is called **Encoding** since we are generating an encoded version of the data. In this article, we will learn more about encodings, how calculate them using **AutoEncoders**, and finally how to implement them in** Keras**.

### **AutoEncoders**

An **AutoEncoder **is a strange neural network, because both its input and output are the same. So, it is a network that tries to learn itself! This is crazy I know but you will see why this is useful.

Suppose we have the following neural network:

- •An input layer with 100 neurons
- •A Hidden layer with 3 neurons
- •An output layer with 100 neurons (same as the input layer)

![](../_resources/07fea2a7aab1348d3c671276c88af276.png)![1*KS9kYN-tC4vX_nDRGbsASA.png](../_resources/31d35eab63d4bd0de313c356d6df6c42.png)

Now what happens if we fit the neural network to take the input and tries to predict the same value in the output? Does not this mean that the network learned how to represent a 100-dimensions-input with only 3-dimensions *(number of neurons in the hidden layer)*, then to reconstruct the same input again? In addition, these 3-dimensions or features seem enough to represent what an input value describes. Well this is very interesting. It is like when compressing files. We reduce the file size, but we can uncompress it again and get the same data. In fact, it is not exactly the same data in AutoEncoders since they are lossy, but you got the point.

### **Objective**

We will use the famous **MNIST **digits dataset to demonstrate the idea. The goal is to generate a 2D encoding from a given 28*28 image. So, we are implementing a dimensionality reduction algorithm using AutoEncoders! Cool right? Let us start…

### **Time to Code**

First, we import the dataset:
from keras.datasets import mnist
(data, labels), (_, _) = mnist.load_data()
Need to reshape and rescale:
data = data.reshape(-1, 28*28) / 255.
Time to define the network. We need three layers:

- •An input layer with size 28*28
- •A hidden layer with size 2
- •An output layer with size 28*28

![](../_resources/768d7f57cb79a145ca7e9f1360deb6e6.png)![1*4DbvFZkPbABtA5sGWUTpcg.png](../_resources/5bf4575051182043c70c7561ab2136b4.png)

from keras import models, layers
input_layer = layers.Input(shape=(28*28,))
encoding_layer = layers.Dense(2)(input_layer)
decoding_layer = layers.Dense(28*28) (encoding_layer)
autoencoder = models.Model(input_layer, decoding_layer)

Let us compile and train… We will fit the model using a binary cross entropy loss between the pixel values:

autoencoder.compile('adam', loss='binary_crossentropy')
autoencoder.fit(x = data, y = data, epochs=5)
Did you notice the trick? **X = data** and **y = data** as well.

After fitting the model, the network is supposed to learn how to calculate the hidden encodings. But we still have to extract the layer responsible for this. In the following, we define a new model where we remove the final layer since we do not need it anymore:

encoder = models.Model(input_layer, encoding_layer)

Now instead of predicting the final output, we are predicting only the hidden representation. Look how we use it:

encodings = encoder.predict(data)

That is it! Now your *encodings *variable is an (n, m) array where n is the number of examples and m is the number of dimensions. The first column is the first feature and the second column is the second one. But what are those features? Actually, we do not know. We only know that they are well representatives of each input value.

Let us plot them and see what we get.

![](../_resources/c229d557c75c47988f5e0fb6f30cb493.png)![1*BEpdZIUNnNLtQMSfakeWLw.png](../_resources/f671f35d6c78d0b609e25479d52104ce.png)

Beautiful! See how the neural network learned the hidden features. Clearly it learned the different characteristics for each digit and how they are distributed in a 2D space. Now we could use these features for visualizations, clustering or any other purpose…

### **Final Thoughts**

In this article we learned about AutoEncoders and how to apply them for dimensionality reduction. AutoEncoders are very powerful and used in many modern neural network architectures. In future posts, you will learn about more complex Encoder/Decoder networks.