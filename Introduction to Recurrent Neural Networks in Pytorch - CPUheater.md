Introduction to Recurrent Neural Networks in Pytorch - CPUheater

# Introduction to Recurrent Neural Networks in Pytorch

![RNN-logo-7.png](../_resources/28cbab3308c6d8b2068edb2d94d18f37.png)

This tutorial is intended for someone who wants to understand how Recurrent Neural Network works, no prior knowledge about RNN is required. We will implement the most simple RNN model – Elman Recurrent Neural Network. To get a better understanding of RNNs, we will build it from scratch using Pytorch tensor package and autograd library.

I assume that you have some understanding of feed-forward neural network if you are new to Pytorch and autograd library checkout my [tutorial](https://www.cpuheater.com/deep-learning/quick-introduction-to-pytorch/).

##### Elman Recurrent Neural Network

An Elman network was introduced by [Jeff Elman](https://en.wikipedia.org/wiki/Jeffrey_Elman), and was first published in a paper entitled [Finding structure in time](https://crl.ucsd.edu/~elman/Papers/fsit.pdf).  It’s just a  three-layer feed-forward network, in our case, input layer consist of one input neuron x1  and additional units called context neurons c1 … cn. Context neurons receive input from the hidden layer neurons, from previous time step. We have one context neuron per neuron in the hidden layer. Since the state from previous time step is provided as a part of the input, we can say that network has a form of memory, context neurons represent a memory.

![Elman-neural-network.png](../_resources/d323874be7306ca198ece10e5153847b.png)

##### Predicting the sine wave

We will train our RNN to learn sine function. During training we will be feeding our model with one data point at a time, that is why we need only input neuron  x1, and we want to predict the value at next time step. Our input sequence x consists of 20 data points, and the target sequence is the same as the input sequence but it ‘s shifted by one-time step into the future.

##### Implementing the model

We start by importing the necessary packages.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | importtorch<br>fromtorch.autograd importVariable<br>importnumpy asnp<br>importpylab aspl<br>importtorch.nn.init asinit |

Next, we’ll set the model hyperparameters,  the size of the input layer is set to 7, which means that we will have 6 context neurons and 1 input neuron, seq_length defines the length of our input and target sequence.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | dtype=torch.FloatTensor<br>input_size,hidden_size,output_size=7,6,1<br>epochs=300<br>seq_length=20<br>lr=0.1 |

Now we will generate the training data, where x is an input sequence and y is a target sequence.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | data_time_steps=np.linspace(2,10,seq_length+1)<br>data=np.sin(data_time_steps)<br>data.resize((seq_length+1,1))<br>x=Variable(torch.Tensor(data[:-1]).type(dtype),requires_grad=False)<br>y=Variable(torch.Tensor(data[1:]).type(dtype),requires_grad=False) |

We need to create two weight matrices, w1 of size (input_size, hidden_size) for input to hidden connections, and a w2 matrix of size (hidden_size, output_size) for hidden to output connection. Weights are initialized using a normal distribution with zero mean.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | w1=torch.FloatTensor(input_size,hidden_size).type(dtype)<br>init.normal(w1,0.0,0.4)<br>w1=Variable(w1,requires_grad=True)<br>w2=torch.FloatTensor(hidden_size,output_size).type(dtype)<br>init.normal(w2,0.0,0.3)<br>w2=Variable(w2,requires_grad=True) |

We can now define forward pass method, it takes input vector x, context_state vector and two weights matrices as arguments. We will create vector xh by concatenating input vector x with the context_state vector. We perform dot product between the xh vector and weight matrix w1, then apply tanh function as nonlinearity, which works better with RNN than sigmoid. Then we perform another dot product between new context_state and weight matrix w2. We want to predict continuous value, so we do not apply any nonlinearity at this stage.

Note that context_state vector will be used to populate context neurons at the next time step. That is why we return context_state vector along with the output of the network.

> This is where the magic happens, context_state vector summarizes the history of the sequence it has seen so far.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | defforward(x,context_state,w1,w2):<br>xh=torch.cat((input,context_state),1)<br>context_state=torch.tanh(xh.mm(w1))<br>out=context_state.mm(w2)<br>return(out,context_state) |

##### Training

Our training loop will be structured as follows.

- The outer loop iterates over each epoch. Epoch is defined as one pass of all training data. At the beginning of each epoch, we need to initialize our context_state vector with zeros.
- The inner loop runs through each element of the sequence. We run forward method to perform forward pass which returns prediction and context_state which will be used for next time step. Then we compute Mean Square Error (MSE),  which is a natural choice when we want to predict continuous values.  By running backward() method on the loss we calculating gradients, then we update the weights. We’re supposed to clear the gradients at each iteration by calling zero_() method otherwise gradients will be accumulated. The last thing we do is wrapping context_state vector in new Variable, to detach it from its history.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17 | foriinrange(epochs):<br>total_loss=0<br>context_state=Variable(torch.zeros((1,hidden_size)).type(dtype),requires_grad=True)<br>forjinrange(x.size(0)):<br>input=x[j:(j+1)]<br>target=y[j:(j+1)]<br>(pred,context_state)=forward(x,context_state,w1,w2)<br>loss=(pred-target).pow(2).sum()/2<br>total_loss+=loss<br>loss.backward()<br>w1.data-=lr*w1.grad.data<br>w2.data-=lr*w2.grad.data<br>w1.grad.data.zero_()<br>w2.grad.data.zero_()<br>context_state=Variable(context_state.data)<br>ifi%10==0:<br>print("Epoch: {} loss {}".format(i,total_loss.data[0])) |

The output generated during training shows how the loss is decreasing with every epoch, which is a good sign. Decaying loss means that our model is learning.

Epoch: 0 loss 2.777482271194458
Epoch: 10 loss 0.10264662653207779
Epoch: 20 loss 0.1178232803940773
…
Epoch: 280 loss 0.005524573381990194
Epoch: 290 loss 0.005174985621124506

##### Making Predictions

Once our model is trained, we can make predictions, at each step of the sequence we will feed the model with single data point and ask the model to predict one value at the next time step.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | context_state=Variable(torch.zeros((1,hidden_size)).type(dtype),requires_grad=False)<br>predictions=[]<br>foriinrange(x.size(0)):<br>input=x[i:i+1]<br>(pred,context_state)=forward(input,context_state,w1,w2)<br>context_state=context_state<br>predictions.append(pred.data.numpy().ravel()[0]) |

As you can see, our model did a pretty good job.

![pytorch-sin-wave.png](../_resources/ee551cebd2f581ad7bbe35f4140e9a14.png)

##### Conclusion

In this post we’ve implemented a basic RNN model from scratch using Pytorch. We learn how to apply RNN to simple sequence prediction problem. The [full code](https://github.com/cpuheater/pytorch_examples) is available on Github.

### Like this: