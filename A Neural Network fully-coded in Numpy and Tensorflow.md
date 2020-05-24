A Neural Network fully-coded in Numpy and Tensorflow

# A Neural Network fully-coded in Numpy and Tensorflow

## Super simple, can’t be any easier, code provided

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='171' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='172' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![1*pPoZZfAIf7o7nJ1MLrzeXA.jpeg](../_resources/d0497b7d5b5b3980b5fae4ba33110d24.jpg)](https://medium.com/@assaad.moawad?source=post_page-----cc275c2b14dd----------------------)

[Assaad MOAWAD](https://medium.com/@assaad.moawad?source=post_page-----cc275c2b14dd----------------------)

[Dec 16, 2019](https://medium.com/datathings/a-neural-network-fully-coded-in-numpy-and-tensorflow-cc275c2b14dd?source=post_page-----cc275c2b14dd----------------------) · 2 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='188'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='189' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='194'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='195' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/cc275c2b14dd/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='203'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='204' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/cc275c2b14dd/share/facebook?source=post_actions_header---------------------------)

![0*M-CUH7fVBUX06gHJ.jpg](../_resources/8f2090f917977634ccd4c4a86417555e.jpg)
![0*M-CUH7fVBUX06gHJ.jpg](../_resources/2758994188de23e9c11c4c4d9a8f702d.jpg)

[In a previous post](https://medium.com/datathings/neural-networks-and-backpropagation-explained-in-a-simple-way-f540a3611f5e), we explained the mechanics behind Neural networks. In this post we will show a basic implementation in pure Numpy, and in TensorFlow.

As we previously explain, neural networks execution have 4 main steps:
1. Forward step (where we go from inputs to outputs)
2. Loss function (where we compare the calculated outputs with real outputs)

3. Backward step (where we calculate the first delta at the loss function and then back-propagate)

4. Optimization step (where we update the internal weights with deltas and learning rate)

![0*xRtlN3b-3HY1n-Rb.png](../_resources/58158399d6740d14a8e1d36d96b9be0e.png)
![0*xRtlN3b-3HY1n-Rb.png](../_resources/d2aebc690beb3bf9842400f4e06e309b.png)
Neural networks step-by-step

The easiest way to do a full working example, is to take only one operator (matrix multiplication), one loss function (RMSE), one optimizer(gradient descent) and execute a full running example.

**def** forwardMult(A,B):
 **return** np.matmul(A,B)

**def** backwardMult(dC,A,B,dA,dB):
dA += np.matmul(dC,np.matrix.transpose(B))
dB += np.matmul(np.matrix.transpose(A),dC)

*#Loss example in forward and backward (RMSE)*
**def** forwardloss(predictedOutput,realOutput):
 **if**(predictedOutput.shape == realOutput.shape):
loss = np.mean( 0.5*np.square(predictedOutput - realOutput))
 **else** :
print("Shape of arrays not the same")
 **return** loss

**def** backwardloss(predictedOutput,realOutput):
 **if**(predictedOutput.shape == realOutput.shape):
deltaOutput = (predictedOutput - realOutput)/predictedOutput.size
 **else** :
print("Shape of arrays not the same")
 **return** deltaOutput

*#Optimizer example (SGD)*
**def** updateweights(W,dW,learningRate):
W -= learningRate * dW

The full code can be found in [Numpy here](https://github.com/assaad/neuralnet_example/blob/master/NN_in_pure_numpy.ipynb), in [Tensorflow here](https://github.com/assaad/neuralnet_example/blob/master/NN_in_pure_TF.ipynb), and a [comparision between both here](https://github.com/assaad/neuralnet_example/blob/master/Compare_numpy_TF.ipynb).

The [repo](https://github.com/assaad/neuralnet_example) is made available on GitHub as a tutorial to understand how a neural network works.