Writing RNNs in Tensorflow

# Writing RNNs in Tensorflow

Jul 10, 2017

In this post I’ll talk through the pieces of the tensorflow API most relevant to building recurrent neural networks. The tensorflow documentation is great for explaining how to build standard RNNs, but it falls a little flat for building highly customized RNNs.

I’ll use the network described in [Hierarchical Multiscale Recurrent Neural Networks](https://arxiv.org/abs/1609.01704v2)by Chung et al. as an example of a fairly non-standard RNN. There’s an open-source implementation of that network [on github](https://github.com/n-s-f/hierarchical-rnn).

## The basics

In this section I’ll provide a quick overview of the tools available to create standard RNNs in tensorflow.

#### Standard RNN Cells

If you need a standard[RNN](https://www.tensorflow.org/versions/r1.0/api_docs/python/tf/contrib/rnn/BasicRNNCell),[GRU](https://www.tensorflow.org/versions/r1.0/api_docs/python/tf/contrib/rnn/GRUCell), or[LSTM](https://www.tensorflow.org/versions/r1.0/api_docs/python/tf/contrib/rnn/BasicLSTMCell), tensorflow has you covered. The API contains these pre-written cells, all of which extend the base class[RNNCell](https://www.tensorflow.org/versions/r1.0/api_docs/python/tf/contrib/rnn/RNNCell). Their [tutorial](https://www.tensorflow.org/tutorials/recurrent) on RNNs gives a good overview of how to use these cells, so I won’t spend much time here. If you are completely new to RNNs in tensorflow, it may be a good idea to review that tutorial before continuing.

One thing that is worth pointing out about their tutorial is their use of the[MultiRNNCell](https://www.tensorflow.org/versions/r1.0/api_docs/python/tf/contrib/rnn/MultiRNNCell). This is a class that is constructed with a list of objects that extend RNNCell. It is used for creating multi-layered RNNs, where the lowest layer gets fed in the input, then each subsequent layer gets fed the output of the previous layer, and the output of the last layer is the output of the network at a given timestep. If you want to pass information between layers in a different way, you’ll need a custom multicell. We’ll come back to this later.

Note that MutliRNNCell itself extends RNNCell as well, so it can be used anywhere any other RNNCell can be used.

#### Dynamic v. Unrolled RNNs

I find it easiest to think about RNNs when they are unrolled. In tensorflow, this means that we rebuild an identical computational graph for each timestep, and pass the hidden state(s) from one timestep forward to the next manually, as it were.

This is the approach taken the [tensorflow tutorial model](https://github.com/tensorflow/models/blob/master/tutorials/rnn/ptb/ptb_word_lm.py#L155-L157). The upside to this approach is that it is easy to think about, and it is flexible. If you want to process the hidden states from one time step in any way before you pass them on, you can easily put more nodes in the graph to do so.

There are two major downsides. First, a graph composed in this way has to be fixed length, which means you’ll have to rebuild the graph for different length signals, or pad them out with zeros. Neither solution is great.

Second, large graphs take much longer to build and consume much more RAM. Depending on the constraints of your computing environment, this could be prohibitive.

The [tf.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)function will transform your RNNCell into a dynamically generated graph that passes the state, whatever that may be, from one time step to the next, and keeps track of the outputs. If you have other needs, [tf.scan](https://www.tensorflow.org/api_docs/python/tf/scan) can serve a similar purpose more flexibly, as we will see later.

## Novel RNN Configurations

In this section, I’ll review some available options for creating RNNs with less standard architectures.

#### Extending RNNCell Directly

If you need a network that’s a little different from any of the standard implementations, you can extend RNNCell directly. You can use your own subclass with the MultiRNNCell class described above as well as the [DropoutWrapper](https://www.tensorflow.org/api_docs/python/tf/contrib/rnn/DropoutWrapper)and other predefined RNNCell wrappers.

Extending RNNCell means overriding at least the `state_size` property, the`output_size` property, and the `call` method. Tensorflow’s prebuilt cells internally represent state either as a signal tensor or as a tuple of tensors. If it is a single tensor, it gets broken down into cell and hidden states (or whatever the case may be) upon entry into the cell, and then the new states are stuck back together at the end.

I’ve found it simpler to treat cell state as a tuple. In this case, the`state_size` property is just a tuple with the lengths of whichever states you’re keeping track of. `output_size` is the length of the output of the cell. The `call` function is where the logic of your cell will live. RNNCell’s`__call__` method will wrap your `call` method and help with scoping and other logistics.

In order for your subclass to be a valid RNNCell, the `call` method must accept parameters `input` and `state`, and return a tuple of `output, new_state`, where`state` and `new_state` must have the same form.

Note that if you construct a new RNNCell that you want to use with tensorflow variables that already exist in your tensorflow session, you can pass a`_reuse=True` argument in to the parent constructor within your `__init__`method. If the variables already exist but you do not pass `_reuse=True`, you’ll get an error because tensorflow will neither overwrite existing variables or reuse them without explicit instruction.

For reference, the [HMLSTMCell](https://github.com/n-s-f/hierarchical-rnn/blob/master/hmlstm/hmlstm_cell.py)class is an RNNCell used to represent one cell of the Hierarchical and Multiscale RNN mentioned above. Its implementation covers all the main points above.

That code also makes use of an undocumented function in the `rnn_cell_impl`module called `_linear`, which is used in most of the baked in RNNCell subclasses. This is a little risky, because it’s clearly not meant for outside use, but it’s a useful little function that handles matrix multiplication and addition of weights and biases.

#### Unusual Multilayered RNNs

If you’re building a multi-layered RNN where the layers don’t simply pass their output up from layer to layer, you’ll have to build your own version of a MultiCell. Much like the built in MultiRNNCell, your multicell should extend RNNCell.

In this case the cell state will be a list, where each element is the cell state at the layer corresponding to its index.

Writing your own multicell is useful in two cases. First, in the case where you want to do something to the result of one layer before you pass it into the cell at the next layer, but you don’t want to execute that operation for the lowest layer (otherwise you could just build it into the cell).

Second, it’s useful if there’s information from the previous time step that you need to distribute among the different layers, but that doesn’t fit neatly into the paradigm of passing along state from one time step to the next.

For example, in the hierarchical multiscall LSTM, each cell expects to receive the hidden state from the layer above it at the previous time step as part of its input. This doesn’t neatly fit the standard idea of stacked RNNs, so we can’t use the usual MultiRNNCell. For reference, here is the implementation of the [MultiHMLSTMCell](https://github.com/n-s-f/hierarchical-rnn/blob/master/hmlstm/multi_hmlstm_cell.py).

#### Building Dynamic RNNs with tf.scan

The Hierarchical Multiscale LSTM network calls for the hidden states to be fed into some output network. We’ve already seen that this HMLSTM network doesn’t neatly fit into the tensorflow RNN paradigm because of how it handles passing information between layers; now we’ve hit another obstacle. Instead of considering the last output of the last layer the output of the network, we need to pass the hidden states of all layers through another network to get the output we really care about. Not only that, we care about the value of some of the indicator neurons, which are treated as cell state.

For these reasons, we can’t use the `tf.dynamic_rnn` network, which returns only the output at each time step and the final state.

`tf.scan`, instead, takes an arbitrary function and a ordered collection of elements. It then applies the function to each element in the collection, keeping track of some accumulator. It returns an ordered collection of the value of the accumulator at each step in the process.

This is perfect for a more customized RNN. Because you get to define the function, you can manipulate the inputs, outputs, and states however you so choose. Afterwards, you get a full accounting of the state at every time step, rather than just the output.

In the case of the HMLSTM, we use these states to keep track of the boundary detection, and we also map over them to obtain the final predictions.

[Here’s](https://github.com/n-s-f/hierarchical-rnn/blob/master/hmlstm/hmlstm_network.py#L221-L270)the code for reference.

## Conclusion

In this post, we looked at the standard tools for dealing with RNNs in tensorflow, and explored some more flexible options to use when those tools fall short.