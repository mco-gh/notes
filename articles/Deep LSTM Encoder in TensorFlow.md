Deep LSTM Encoder in TensorFlow

# Sentiment Analysis with TensorFlow

 08 June 2016 on [tensorflow](http://domkaukinen.com/tag/tensorflow/)

### Hello

This was a short project I took on to attempt to understand the ins and outs of TensorFlow. I made a lot of mistakes along the way to get to where I am now, so I'm going to focus on those mistakes for this post. I've open sourced the code [here](https://github.com/inikdom/neural-sentiment); you can clone it, and run it (if you have the dependencies).

The model I used can be found in this [paper](https://cs224d.stanford.edu/reports/HongJames.pdf), I also referenced this [tutorial](http://deeplearning.net/tutorial/lstm.html).

#### Data Preparation

I think the biggest source of my problems, and greatest time sink was in the data pre-processing and data handling. Overall it was a great learning experience.

I used the [Stanford Large Review Movie Set](http://ai.stanford.edu/~amaas/data/sentiment/)

Because of the relatively small size of the dataset (about 200mb), I chose to load it all into memory. This was done because my thinking was it would be faster than loading from disk. In reality, to generalize this to a larger dataset I would probably save each batch to disk, then load each batch as needed. I would probably use a queue on a separate thread to load more than one batch into memory to ensure every time a new batch is needed there will be one in memory ready to go. This is a consideration for a future project though.

The original data preprocessing was very inefficient. More specifically It was taking 10-30 minutes depending on how much of the data I was using. This was on a macbook air.

In the interest of trying something new, I decided to parallelize the data pre-processing. Of course Python has a built in library that makes this very easy. The processes did not even need to communicate with each other to get a huge speedup! A quick example how to do this if you're curious:

	from multiprocessing import Process, Lock

	dirCount = 0
	processes = []
	lock = Lock()

	#Each directory has a different set of files
	for d in dirs:
	    p = Process(target=dataProcessingFunction, args=
	      (foo1, foo2, etc...))
	        p.start()
	        processes.append(p)

	#Now we wait for each process to finish its' job
	    for p in processes:
	        if p.is_alive():
	            p.join()

One issue however is that sometimes two process' may attempt to access a critical resource at the same time, in which case a lock is necessary. Here is an example locking std.out:

	lock.acquire()
	print "Processing: {0} the {1}th file... on process \{2}".format(f, count, pid)
	lock.release()

As expected, even with the short amount of code above, with each new process I was able to approximately halve the processing time. The limit on this is up to the limit of cores on you processor, and your algorithm complexity.

Another important aspect of data preprocessing was finding a good value to choose for a maximum sequence length. Each text input varies in length, but TensorFlow is expecting a tensor input, which does not have jagged dimensions (jagged meaning its' elements would have different lengths). I used a histogram plot with matplotlib to get an idea for how long the sequences are. The results for this specific dataset were:

![](../_resources/c26550316d7c392185e8d6d5c20bdb2d.png)

I was able to use this information to decrease my maximum sequence length from 500 to 200. Sequences shorter than 200 now get padded with $PAD$ token up to length 200, and sequences more than 200 will get truncated to length 200.

In the future I would like to add bucketing, to allow multiple sequence lengths.

#### Using TensorFlow

Using TensorFlow was frustrating at first, but I grew to really like it. Overall I'm very glad I took the time to learn it. I'm going to share a few tips and tricks I learned.

It may seem at first that TensorFlow is hard to debug/verify correctness of code. The reason for this is that you define placeholders in Python code for TensorFlow to generate your graph at runtime. This makes it slightly more difficult to debug or get things like the shape of a tensor. If you are having trouble with tensor operations (ex/ tf.slice, tf.concat, tf.reshape, tf.pack, etc..) I recommend testing the numpy equivalent function. Here is a small example of averaging the hidden states over time.

	#encoder_states is a list of hidden states across time
	#Pack combines the list of tensors to one tensor
	concat_states =  tf.pack(encoder_states)

	# Average the hidden states across time
	avg_states = tf.reduce_mean(concat_states, 0)

	#Splits the output and hidden state vectors
	_, final_state = tf.split(1,2,avg_states)

	#The slice grabs the avg hidden state of the last layer
	final_state = tf.slice(final_state, [0,hidden_size*(num_layers - 1)], [-1,hidden_size])

The reason this works is there appears to be a 1 to 1 mapping between the numpy array functions and the TensorFlow array ops. In fact in the TensorFlow documentation they are often referenced to compare. This saved me a lot of trial and error guesswork, especially as someone new to tensor manipulation with these sort of libraries.

If, like me, you are new to tensor manipulation I highly recommend playing around with numpy arrays in a Python terminal. You should get comfortable with indexing, reshaping, slicing, and concatenating 3-dimensional tensors. I think I may provide a blog post in and of itself on the topic.

The second tip I can offer is to read through the TensorFlow repository on GitHub for operations and libraries you are using. In particular I referenced the [Translation Example](https://tensorflow.googlesource.com/tensorflow/+/master/tensorflow/models/rnn/translate/translate.py). They have pretty good code commenting throughout, and the translation demo in particular is a solid example of loading in data and iterating over it.

#### TensorFlow Issues

I really only have one complaint about TensorFlow, but it is simultaneously a positive thing too. TensorFlow updates and breaks previous code. I found even over the course of this project `rnn.rnn()` was updated to only return the last hidden state, rather than all hidden states over time.

I had to drop the use of `rnn.rnn()` in favor of a manual encoder to get information of all hidden states across time.

Be mindful when you make a project, it is likely the Python API can change.

#### Data Visualizations

I used tensorboard to get some visualizations. This was a very cool feature of TensorFlow. They make it very easy to automatically store and plot the data, enabling a single command line argument to be given to launch the interactive gui. I think the main benefits to using tensorboard over plotting values over time with something like gnuplot or matplotlib are two-fold:

1. It handles the serialization of the data and automatic plotting (sightly less work than making your own plotting tool wrapper).

2. You can visualize your graph automatically, which to my knowledge other plotting tools can't do.

I recommend reading this [tutorial](http://newtips.co/st/questions/34471563/logging-training-and-validation-loss-in-tensorboard.html) for plotting train and test loss separately. This saved me a lot of time.

Here is the accuracy plotted over time (from TensorBoard):
![accuracy graph](../_resources/4a7b963744547b24f6f098f69faa76a7.png)

#### Training Results and User Testing

So far the best model I've trained is about 85% accurate as measured with the test data, using a binary classification. I'm quite happy with the results, since this is right in line with the paper I read (link at beginning).

Assuming the same dataset is used, these two things may improve accuracy:
1. Pre-load word2vec parameters into embedding layer.
2. Continue my hyper parameter search.

I trained this model on a Titan X for 250 epochs, it took about 0.18s per batch, and it finished training between the time I went to sleep and woke up.

#### Conclusions about TensorFlow

I definitely recommend trying out TensorFlow. There is a bit of learning curve, but once you get the hang of the programming style it becomes pretty easy, especially using the Python API. There are enough examples on GitHub, and documentation to be able to make some really powerful stuff. I think it also highly valuable that you can build the project for Java or C++. For that reason alone TensorFlow is a really powerful option.

#### What's Next

I have my 'mostly' complete seq2seq chatbot done, but am still working on training the model. My next post should cover that.

I also made a realization doing the sentiment analyzer. Data is valuable. Very very valuable. I used the same open dataset that many other people have used in the past. I am beginning to think however, that curating custom datasets is more valuable in the long run than the actual deep learning software. The focus of my future blogs may be more on curating custom datasets than the actual deep learning code.

#### [Dominik Kaukinen](http://domkaukinen.com/author/dominik/)

I am an undergraduate Mechatronics engineering student. My biggest interest right now is deep learning. I'm probably going to making some blogs about my foray into deep learning / embedded systems.

 Canada

#### Share this post

 [](https://twitter.com/intent/tweet?text=Sentiment%20Analysis%20with%20TensorFlow&url=http://domkaukinen.com/sentiment-analysis-with-tensorflow/)  [](https://www.facebook.com/sharer/sharer.php?u=http://domkaukinen.com/sentiment-analysis-with-tensorflow/)  [](https://plus.google.com/share?url=http://domkaukinen.com/sentiment-analysis-with-tensorflow/)