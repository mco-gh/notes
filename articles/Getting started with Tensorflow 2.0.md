Getting started with Tensorflow 2.0

#  Getting started with Tensorflow 2.0

###     [![8423a837-0586-47e0-9d48-b5549b0466cb.jpg](../_resources/01db7c619136cd541c863d068af7c544.jpg)  Apoorva Dave](https://dev.to/apoorvadave)    [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 612 612' role='img' aria-labelledby='a9m46ona7ndsy4gyli1ia62vaj4qis5s' class='icon-img js-evernote-checked' data-evernote-id='205'%3e%3ctitle id='a9m46ona7ndsy4gyli1ia62vaj4qis5s'%3etwitter logo%3c/title%3e%3cpath d='M612 116.258c-22.525 9.98-46.694 16.75-72.088 19.772 25.93-15.527 45.777-40.155 55.184-69.41-24.322 14.378-51.17 24.82-79.775 30.48-22.906-24.438-55.49-39.66-91.63-39.66-69.333 0-125.55 56.218-125.55 125.514 0 9.828 1.11 19.427 3.25 28.606-104.325-5.24-196.834-55.223-258.75-131.174-10.822 18.51-16.98 40.078-16.98 63.1 0 43.56 22.182 81.994 55.836 104.48-20.575-.688-39.926-6.348-56.867-15.756v1.568c0 60.806 43.29 111.554 100.692 123.104-10.517 2.83-21.607 4.398-33.08 4.398-8.107 0-15.947-.803-23.634-2.333 15.985 49.907 62.336 86.2 117.253 87.194-42.946 33.655-97.098 53.656-155.915 53.656-10.134 0-20.116-.612-29.944-1.72 55.568 35.68 121.537 56.484 192.44 56.484 230.947 0 357.187-191.29 357.187-357.188l-.42-16.253C573.87 163.525 595.21 141.42 612 116.257z'%3e%3c/path%3e%3c/svg%3e)](http://twitter.com/apoorva_dave)  [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='438.549' height='438.549' viewBox='0 0 438.549 438.549' role='img' aria-labelledby='anlnkc5ptjoi0bk2qcc1b0i0elixquj9' class='icon-img js-evernote-checked' data-evernote-id='206'%3e%3ctitle id='anlnkc5ptjoi0bk2qcc1b0i0elixquj9'%3egithub logo%3c/title%3e%3cpath d='M409.132 114.573c-19.608-33.596-46.205-60.194-79.798-79.8C295.736 15.166 259.057 5.365 219.27 5.365c-39.78 0-76.47 9.804-110.062 29.408-33.596 19.605-60.192 46.204-79.8 79.8C9.803 148.168 0 184.853 0 224.63c0 47.78 13.94 90.745 41.827 128.906 27.884 38.164 63.906 64.572 108.063 79.227 5.14.954 8.945.283 11.42-1.996 2.474-2.282 3.71-5.14 3.71-8.562 0-.57-.05-5.708-.144-15.417-.098-9.71-.144-18.18-.144-25.406l-6.567 1.136c-4.187.767-9.47 1.092-15.846 1-6.375-.09-12.992-.757-19.843-2-6.854-1.23-13.23-4.085-19.13-8.558-5.898-4.473-10.085-10.328-12.56-17.556l-2.855-6.57c-1.903-4.374-4.9-9.233-8.992-14.56-4.093-5.33-8.232-8.944-12.42-10.847l-1.998-1.43c-1.332-.952-2.568-2.1-3.71-3.43-1.143-1.33-1.998-2.663-2.57-3.997-.57-1.335-.097-2.43 1.428-3.29 1.525-.858 4.28-1.275 8.28-1.275l5.708.853c3.807.763 8.516 3.042 14.133 6.85 5.615 3.807 10.23 8.755 13.847 14.843 4.38 7.807 9.657 13.755 15.846 17.848 6.184 4.093 12.42 6.136 18.7 6.136 6.28 0 11.703-.476 16.273-1.423 4.565-.95 8.848-2.382 12.847-4.284 1.713-12.758 6.377-22.56 13.988-29.41-10.847-1.14-20.6-2.857-29.263-5.14-8.658-2.286-17.605-5.996-26.835-11.14-9.235-5.137-16.896-11.516-22.985-19.126-6.09-7.614-11.088-17.61-14.987-29.98-3.9-12.373-5.852-26.647-5.852-42.825 0-23.035 7.52-42.637 22.557-58.817-7.044-17.318-6.38-36.732 1.997-58.24 5.52-1.715 13.706-.428 24.554 3.853 10.85 4.284 18.794 7.953 23.84 10.995 5.046 3.04 9.09 5.618 12.135 7.708 17.706-4.947 35.977-7.42 54.82-7.42s37.116 2.473 54.822 7.42l10.85-6.85c7.418-4.57 16.18-8.757 26.26-12.564 10.09-3.806 17.803-4.854 23.135-3.14 8.562 21.51 9.325 40.923 2.28 58.24 15.035 16.18 22.558 35.788 22.558 58.818 0 16.178-1.958 30.497-5.853 42.966-3.9 12.47-8.94 22.457-15.125 29.98-6.19 7.52-13.9 13.85-23.13 18.985-9.233 5.14-18.183 8.85-26.84 11.135-8.663 2.286-18.416 4.004-29.264 5.146 9.894 8.563 14.842 22.078 14.842 40.54v60.237c0 3.422 1.19 6.28 3.572 8.562 2.38 2.278 6.136 2.95 11.276 1.994 44.163-14.653 80.185-41.062 108.068-79.226 27.88-38.16 41.826-81.126 41.826-128.906-.01-39.77-9.818-76.454-29.414-110.05z'%3e%3c/path%3e%3c/svg%3e)](http://github.com/apoorva-dave)  May 18  ・5 min read

 [#machinelearning](https://dev.to/t/machinelearning)  [#python](https://dev.to/t/python)  [#beginners](https://dev.to/t/beginners)  [#datascience](https://dev.to/t/datascience)

Part of "Beginning with Machine Learning" series

 [(L)](https://dev.to/apoorvadave/beginning-with-machine-learning---part-1-pbl)  [(L)](https://dev.to/apoorvadave/regression-in-machine-learning---part-2-30bb)  [(L)](https://dev.to/apoorvadave/regression-from-scratch---wine-quality-prediction-3245)  [(L)](https://dev.to/apoorvadave/classification-in-machine-learning-1c5n)  [(L)](https://dev.to/apoorvadave/classification-from-scratchmammographic-mass-classification-3dg7)  [(L)](https://dev.to/apoorvadave/getting-started-with-tensorflow-2-0-2h3n)

Tensorflow is an open source platform for machine learning. Using tensorflow, we can easily code, build and deploy our machine learning models.

Tensorflow 2.0 focuses on simplicity and ease of use, featuring updates like:
1. Easy model building with Keras.
2. Robust model deployment in production on any platform.
3. Powerful experimentation for research.
4. Simplifying the API by cleaning up deprecated APIs and reducing duplication.

This article is for those who want to know how they can start with Tensorflow 2.0. It will help you to create your own image classification model in less than an hour! So let’s get started

#   [(L)](https://dev.to/apoorvadave/getting-started-with-tensorflow-2-0-2h3n#setting-up-tensorflow-20) Setting up Tensorflow 2.0

Install Tensorflow 2.0 package using pip -

	pip install tensorflow==2.0.0-alpha0

To verify if it is installed correctly, try importing tensorflow and checking its version. (It should point to 2.0.0-alpha0)

#   [(L)](https://dev.to/apoorvadave/getting-started-with-tensorflow-2-0-2h3n#keras-overview) Keras Overview

Before we can start with tensorflow, we should have a brief overview of what is Keras. Keras is a high-level neural networks API, written in Python and is capable of running on top of TensorFlow, CNTK, or Theano. Using Keras is extremely user-friendly and it helps you build a model in no time.

The core data structure of Keras is a model, a way to organize layers. The simplest type of model is the Sequential model, a linear stack of layers.

`Sequential` model is defined as:

	from keras.models import Sequential
	model = Sequential()

Stacking layers using `.add()`:

	from keras.layers import Dense
	model.add(Dense(units=64, activation='relu', input_dim=100))
	model.add(Dense(units=10, activation='softmax'))

Once the model building is complete, its learning process can be configured with `.compile()`:

	model.compile(loss='categorical_crossentropy',
	              optimizer='sgd',
	              metrics=['accuracy'])

To know more on Keras follow the [link](https://www.tensorflow.org/alpha/guide/keras/overview)

#   [(L)](https://dev.to/apoorvadave/getting-started-with-tensorflow-2-0-2h3n#classification-on-fashion-mnist-dataset) Classification on Fashion MNIST dataset

We are ready to build our very own classification model! This is like “Hello World” in tensorflow

We have taken **Fashion MNIST dataset** that has 70,000 grayscale images in 10 categories. Each image in the dataset is a type of clothing garment in a resolution of 28 by 28 pixels.

Do the necessary imports

	import tensorflow as tf
	from tensorflow import keras
	import numpy as np
	import matplotlib.pyplot as plt

The dataset can be directly loaded from `keras.datasets`

	fashion_mnist = keras.datasets.fashion_mnist
	(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

The training set `train_images` has 60k images while `test_images` has 10k images. Each image is a 28x28 array, with pixel values ranging from 0 to 255. The labels are an array of integers, ranging from 0 to 9 which correspond to the class of clothing. 0 corresponds to T-shirt/top, 1 to trouser and so on. These 10 classes of clothing type are mapped to `class_names`

	class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

Scaling the train and test images so that pixel values for both train and test images are between 0 and 1.

	train_images = train_images / 255.0
	test_images = test_images / 255.0

You can plot the first 10 images to check the data.

	plt.figure(figsize=(10,10))
	for i in range(10):
	    plt.subplot(5,5,i+1)
	    plt.xticks([])
	    plt.yticks([])
	    plt.grid(False)
	    plt.imshow(train_images[i], cmap=plt.cm.binary)
	    plt.xlabel(class_names[train_labels[i]])
	plt.show()

[![57972036-2f3acb80-79b3-11e9-864e-c99adf9f4e81.png](../_resources/43dd9f538917b6064bd203442a8803ec.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--HaXIlmJ4--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/19779081/57972036-2f3acb80-79b3-11e9-864e-c99adf9f4e81.png)

Fashion MNIST (first 10 images of train set)

Building a Sequential model using keras

	model = keras.Sequential([
	    keras.layers.Flatten(input_shape=(28, 28)),
	    keras.layers.Dense(128, activation='relu'),
	    keras.layers.Dense(10, activation='softmax')
	])

While dealing with images in neural networks we need to flatten the 2D array of 28 by 28 to a 1D array (of 28 * 28 = 784 pixels). `tf.keras.layers.Flatten` layer performs this task. After this layer, there are two dense layers (fully connected) with 128 and 10 neurons respectively. Softmax activation function in the last layer returns an array of 10 values which correspond to the probability scores that sum to 1. **The class for which we get the highest probability is assigned to the input image.**

Compiling model

	model.compile(optimizer='adam',
	              loss='sparse_categorical_crossentropy',
	              metrics=['accuracy'])

1. *Loss function* — This measures how accurate the model is during training. We want to minimize this function.

2. *Optimizer* — This is how the model is updated based on the data it sees and its loss function.

3. *Metrics* — Used to monitor the training and testing steps. accuracy measures the fraction of the images that are correctly classified.

Training the model

	model.fit(train_images, train_labels, epochs=5)

To start training, we call the `model.fit` method to fit the model to training data.

Evaluating accuracy on `test_images`

	test_loss, test_acc = model.evaluate(test_images, test_labels)
	print('\nTest accuracy:', test_acc)

With this simple model, we achieve an accuracy of ~0.86
Making predictions on `test images`

	predictions = model.predict(test_images)
	predictions[0]

`predictions[0]` gives the probability scores for the 1st test image. We can check the maximum probability or the class which our model has predicted.

	np.argmax(predictions[0])

It gives a value 9 which shows that the model has identified this image to be an ankle boot, or `class_names[9]`. We can verify this result by checking `test_labels[0]` which also has a value 9. This shows that our model was able to predict the correct value for the first test image :)

This is it! You have your classification model build with Tensorflow 2.0 and Keras up and running in no time. You can play with the code to check the impacts on changing loss function, the number of epochs, optimizer. In case it is needed, you can have a look for the code for this in my Github [repo](https://github.com/apoorva-dave/Image-Classification-Tensorflow2.0)

#   [(L)](https://dev.to/apoorvadave/getting-started-with-tensorflow-2-0-2h3n#google-colab) Google Colab

Colaboratory allows us to use and share Jupyter notebooks with others without having to download, install, or run anything on your own computer other than a browser. All our notebooks are saved on Google Drive. In Colabs, the code is executed in a virtual machine dedicated to our account. Virtual machines are recycled when idle for a while and have a maximum lifetime enforced by the system. We many times face issue in training our models. It can easily be done using Colab as it provides free GPU and TPU. To setup Colab you can follow the [link](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c)

This is a very brief overview of getting started with Tensorflow 2.0. I am myself in the process of learning, as I learn I will be writing on how can we do regression, text-classification, saving models, transfer learning, tensors and operations Do show some ❤ if you found the article helpful. Stay tuned for more tensorflow!

Part of "Beginning with Machine Learning" series

 [(L)](https://dev.to/apoorvadave/beginning-with-machine-learning---part-1-pbl)  [(L)](https://dev.to/apoorvadave/regression-in-machine-learning---part-2-30bb)  [(L)](https://dev.to/apoorvadave/regression-from-scratch---wine-quality-prediction-3245)  [(L)](https://dev.to/apoorvadave/classification-in-machine-learning-1c5n)  [(L)](https://dev.to/apoorvadave/classification-from-scratchmammographic-mass-classification-3dg7)  [(L)](https://dev.to/apoorvadave/getting-started-with-tensorflow-2-0-2h3n)