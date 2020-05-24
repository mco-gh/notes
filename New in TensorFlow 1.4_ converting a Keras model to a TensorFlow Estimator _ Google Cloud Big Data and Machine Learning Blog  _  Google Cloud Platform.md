New in TensorFlow 1.4: converting a Keras model to a TensorFlow Estimator | Google Cloud Big Data and Machine Learning Blog  |  Google Cloud Platform

 ![](../_resources/6c87978deeaace9b956c3205f1927ee7.png)

## New in TensorFlow 1.4: converting a Keras model to a TensorFlow Estimator

Monday, December 18, 2017

*By Sara Robinson and Josh Gordon, Developer Advocates*

TensorFlow’s [1.4 release](https://developers.googleblog.com/2017/11/announcing-tensorflow-r14.html) brings many new features — one of our favorites is support for converting a Keras model to a TensorFlow [Estimator](https://www.tensorflow.org/programmers_guide/estimators) via the [model_to_estimator()](https://www.tensorflow.org/api_docs/python/tf/keras/estimator/model_to_estimator) method.

Why would you want to do this? By wrapping your Keras code in a Estimator, you can serve predictions using [TensorFlow Serving](https://www.tensorflow.org/serving/) or deploy your model on [Cloud ML Engine](https://cloud.google.com/ml-engine/docs/technical-overview), a managed service for [training](https://cloud.google.com/ml-engine/docs/training-steps) and [serving](https://cloud.google.com/ml-engine/docs/deploying-models) your TensorFlow models at scale. Using a TensorFlow Estimator, you can also take advantage of distributed training on [your own cluster](https://www.tensorflow.org/deploy/).

In this post, we’ll update [the code](https://github.com/tensorflow/workshops/tree/master/extras/keras-bag-of-words) we wrote in the article [building a text classification model with Keras](https://cloud.google.com/blog/big-data/2017/10/intro-to-text-classification-with-keras-automatically-tagging-stack-overflow-posts). If you haven’t read that blog post, we used Stack Overflow data from BigQuery to train a model to predict the tag of a Stack Overflow question. To jump to the code, find the full Jupyter notebook for this blog post [here](https://github.com/tensorflow/workshops/tree/master/extras/keras-to-estimator).

### Recap: our Keras model

To recap, let’s take a quick look at our Keras “bag of words” model for text classification from the previous post:

hdr_strong

	model = Sequential()
	model.add(keras.layers.Dense(512, input_shape=(max_words,), activation='relu'))
	model.add(Dense(num_labels, activation='softmax'))

We used the Keras Sequential model API, which lets us build a linear stack of layers. This model has two layers: an input layer where we feed the model our [Stack Overflow](https://cloud.google.com/bigquery/public-data/stackoverflow)  [post data](https://storage.googleapis.com/tensorflow-workshop-examples/stack-overflow-data.csv), and an output layer indicating the probability that a post belongs to a specific tag. The input data is a `vocab_size` vector for each post, with 0s and 1s indicating whether a post contains a certain word from our vocabulary. The output layer uses the [softmax](https://en.wikipedia.org/wiki/Softmax_function) activation function to generate a probability vector with 20 values, one for each possible tag.

Now we’ll convert this to an `[Estimator](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator)`.

### Converting our Keras model to a TensorFlow Estimator

We can convert our model to an Estimator with one line of code:
hdr_strong
`estimator_model = keras.estimator.model_to_estimator(keras_model=model)`

In order for this to work, we need to make just a few tweaks to the model we defined above. We’ll walk you through them below.

We can use the same input and output layers as the previous example, but we’ll need to convert our data to float32 since this is what the Estimator API expects:

hdr_strong

	x_train = tokenize.texts_to_matrix(train_posts).astype(np.float32)
	x_test = tokenize.texts_to_matrix(test_posts).astype(np.float32)

hdr_strong

	y_train = keras.utils.to_categorical(y_train, num_classes).astype(np.float32)
	y_test = keras.utils.to_categorical(y_test, num_classes).astype(np.float32)

Next, when we define our Dense input layer, we’ll add a parameter to name this layer (we’ll reference the layer by this name in the next step when we run training):

hdr_strong

	model.add(keras.layers.Dense(512, input_shape=(max_words,), activation='relu',
	  name="posts")) # Added a layer name

We’ll also add a name to the output layer before compiling the model:
hdr_strong

	model.add(keras.layers.Dense(num_classes, activation='softmax', name='labels'))

	model.compile(loss='categorical_crossentropy',
	              optimizer='adam',
	              metrics=['accuracy'])

Awesome, now we can call [model_to_estimator()](https://www.tensorflow.org/versions/master/api_docs/python/tf/keras/estimator/model_to_estimator) and we’ll be working with a TF [Estimator object](https://www.tensorflow.org/programmers_guide/estimators#advantages_of_estimators).

### Training our model

Since our model is now an Estimator, we’ll train and evaluate it a bit differently than we did in Keras. Instead of passing our features and labels to the model directly when we run training, we need to pass it an [input function](https://www.tensorflow.org/get_started/input_fn). In TensorFlow, input functions prepare data for the model by mapping raw input data to feature columns. [Feature columns](https://developers.googleblog.com/2017/11/introducing-tensorflow-feature-columns.html) define the types of data we’re feeding into the model, and in this example we have one feature column - the bag of words vector for each post.

We’ll use the `[numpy_input_fn](https://www.tensorflow.org/api_docs/python/tf/estimator/inputs/numpy_input_fn)` provided by the Estimators API in this example. The training input function takes a few parameters:

- `x`: the input features to our model, in our example this is the Stack Overflow posts as a vector the size of our vocabulary. x is an object: the key is the name of this feature column. Since we named our column “posts” above, we can reference it in our input function by the name posts_input.
- `y`: the labels for our model, in this case the correct tag for each post encoded as a one-hot vector the size of all possible tags in our model.
- There are a few optional parameters, including whether or not we should shuffle the data as we feed it to our model.

With these parameters in mind, we can now build our input function with the following code. The labels argument defaults to `None` since we won’t pass labels to the function when we generate a prediction using `.predict()`:

hdr_strong

	def input_function(features,labels=None,shuffle=False):
	    input_fn = tf.estimator.inputs.numpy_input_fn(
	        x={"posts_input": features},
	        y=labels,
	        shuffle=shuffle
	    )
	    return input_fn

To train our model, all we need to do is call `train()` and pass in the input function we just defined with our training data and labels:

hdr_strong
`estimator_model.train(input_fn=input_function(x_train, y_train, True))`

### Evaluating the accuracy of our model

Now that we’ve trained our model, we can evaluate its accuracy on our training data. We’ll use the same input function as above, this time passing it our test data instead of training data:

hdr_strong
`score = estimator_model.evaluate(input_function(x_test, labels=y_test))`

As expected, the model’s accuracy is the same as it was for our Keras model in the previous post (~81%). This post is focused on converting our model to an Estimator — if we wanted to  improve accuracy we could try tuning our model’s hyperparameters, changing our vocabulary size, or adding [dropout](https://en.wikipedia.org/wiki/Dropout_(neural_networks)) to our input layer.

### Generating predictions on our trained model

Next comes the most important part: using our trained model to generate a prediction on data it hasn’t seen before. We’ll use the first five examples from our test dataset. To make a prediction, we can simply call `.predict()` on our model passing it the five posts as a bag of words vector:

hdr_strong

	text_labels = encoder.classes_

	# We'll make predictions for the first five examples
	examples = x_test[:5]
	predictions = list(estimator_model.predict(input_function(examples)))

	# Print out the true and expected labelfor i in range(len(examples)):
	    prediction_array = predictions[i].values()[0]
	    predicted_label = text_labels[np.argmax(prediction_array)]
	    print('Actual label:' + test_tags.iloc[i])
	    print("Predicted label: " + predicted_label + "\n")

`predictions` is now a vector with the softmax probabilities for each possible Stack Overflow tag in our dataset. We take the index of the highest value from this vector, and then get the text label that corresponds with this index. That’s all: by calling `predict` with our input functions we’re able to generate predictions on our trained Estimator model!

### What’s next?

With our Keras model converted to an Estimator, we can now make use of [TensorFlow Serving](https://www.tensorflow.org/serving/) to serve predictions, or deploy our model to [Cloud ML Engine](https://cloud.google.com/ml-engine/docs/training-steps) (stay tuned for a future post!). Have questions or topics you’d like to see covered next? Let us know what you think in the comments, or find us on Twitter [@SRobTweets](https://twitter.com/srobtweets) and [@random_forests](https://twitter.com/random_forests).