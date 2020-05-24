Build Your Own Neural Network in Go - Towards Data Science

# Build Your Own Neural Network in Go

## A beginner’s guide to building a simple neural network completely from scratch in Go language

[![2*ewCzdfYt04JS3sT4yGm59A.jpeg](../_resources/616fdf7da647a5d21a1373c9e225b7c7.jpg)](https://towardsdatascience.com/@dasaradhsk?source=post_page-----b98e2abcced3----------------------)

[Dasaradh S K](https://towardsdatascience.com/@dasaradhsk?source=post_page-----b98e2abcced3----------------------)

[Apr 13](https://towardsdatascience.com/neural-network-from-scratch-in-go-language-b98e2abcced3?source=post_page-----b98e2abcced3----------------------) · 5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='207'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='208' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='213'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='214' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/b98e2abcced3/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='222'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='223' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/b98e2abcced3/share/facebook?source=post_actions_header---------------------------)

# Introduction

In this tutorial, we’ll build a simple neural network (single-layer [perceptron](https://en.wikipedia.org/wiki/Perceptron)) in Golang, completely from scratch. We’ll also train it on sample data and perform predictions. Creating your own neural network from scratch will help you better understand what’s happening inside a neural network and the working of learning algorithms.

# What’s a Perceptron?

Perceptrons — invented by**  **[**Frank Rosenblatt **](https://en.wikipedia.org/wiki/Frank_Rosenblatt)in 1958, are the simplest neural network that consists of* n* number of inputs, only** one neuron** and **one output**, where *n* is the number of features of our dataset.

Hence, our single-layer perceptron consists of the following components
1. An **input layer* (x)***
2. An **output layer* (ŷ)***

3. A set of **weights *(w)*  **and a **bias**  ***(b)*** between these two layers

4. An **activation function* (σ) ***for the output layer. In this tutorial, we’ll be using the** sigmoid** activation function.

Our neural network is called a **single-layer perceptron (SLP) **as the neural network has only one layer of neurons. Neural networks with more than one layer of neurons are called **multi-layer perceptron (MLP)**.

(note epoch refers to one cycle through the full training dataset)

|     |     |
| --- | --- |
| 1   | type  Perceptron  struct { |
| 2   | input [][]float64 |
| 3   | actualOutput []float64 |
| 4   | weights []float64 |
| 5   | bias  float64 |
| 6   | epochs  int |
| 7   | }   |

 [view raw](https://gist.github.com/dasaradhsk/c16f606a6d974bdb194fba3f3f214db0/raw/c17b5b825e0fd3f459861e5f9fc51ae9a1eb2ab9/perceptron_struct.go)  [perceptron_struct.go](https://gist.github.com/dasaradhsk/c16f606a6d974bdb194fba3f3f214db0#file-perceptron_struct-go) hosted with ❤ by [GitHub](https://github.com/)

# Before we start

We’ll build our own functions for the following math operations — **vector addition**, **vector dot product** & scalar matrix multiplication.

|     |     |
| --- | --- |
| 1   | func  dotProduct(v1, v2 []float64) float64 { //Dot Product of Two Vectors of same size |
| 2   | dot  :=  0.0 |
| 3   | for  i  :=  0; i  <  len(v1); i++ { |
| 4   | dot  +=  v1[i] *  v2[i] |
| 5   | }   |
| 6   | return  dot |
| 7   | }   |
| 8   |     |
| 9   | func  vecAdd(v1, v2 []float64) []float64 { //Addition of Two Vectors of same size |
| 10  | add  :=  make([]float64, len(v1)) |
| 11  | for  i  :=  0; i  <  len(v1); i++ { |
| 12  | add[i] =  v1[i] +  v2[i] |
| 13  | }   |
| 14  | return  add |
| 15  | }   |
| 16  |     |
| 17  | func  scalarMatMul(s  float64, mat []float64) []float64 { //Multiplication of a Vector & Matrix |
| 18  | result  :=  make([]float64, len(mat)) |
| 19  | for  i  :=  0; i  <  len(mat); i++ { |
| 20  | result[i] +=  s  *  mat[i] |
| 21  | }   |
| 22  | return  result |
| 23  | }   |

 [view raw](https://gist.github.com/dasaradhsk/1c15bc02af40c00b462bfbc62106afc6/raw/89f73e17f8539ff9c58c9acc9814f9b31667687a/math.go)  [math.go](https://gist.github.com/dasaradhsk/1c15bc02af40c00b462bfbc62106afc6#file-math-go) hosted with ❤ by [GitHub](https://github.com/)

Initially, the weights of the neural network are set to random float values between 0 and 1 while the bias is set to zero.

|     |     |
| --- | --- |
| 1   | func (a  *Perceptron) initialize() { //Random Initialization |
| 2   | rand.Seed(time.Now().UnixNano()) |
| 3   | a.bias  =  0.0 |
| 4   | a.weights  =  make([]float64, len(a.input[0])) |
| 5   | for  i  :=  0; i  <  len(a.input[0]); i++ { |
| 6   | a.weights[i] =  rand.Float64() |
| 7   | }   |
| 8   | }   |

 [view raw](https://gist.github.com/dasaradhsk/0750272a249d9f74b41b563adab59f3a/raw/5c455534fc70f6866ac325aeaa29dd2afa5ff44e/random_initialize.go)  [random_initialize.go](https://gist.github.com/dasaradhsk/0750272a249d9f74b41b563adab59f3a#file-random_initialize-go) hosted with ❤ by [GitHub](https://github.com/)

# Forward Propagation

The process of passing the data through the neural network is known as forward-propagation or forward pass. The output the perceptron is

![1*ok5zJr_LlBuon7laKe1lNA.png](../_resources/dfde26517fb5ca21fc86a98871c25204.png)
![0*mn2qELpNIMtn9AOf.png](../_resources/666e3b35374a5e1f56f85ee563462df5.png)

In a nutshell, the**  **[**dot product**](https://en.wikipedia.org/wiki/Dot_product#Algebraic_definition)**  **of the** weight vector* (w)*** and the** input vector* (x)*** is added with the **bias (*b)*** and the sum is passed through an activation function. The output of the sigmoid activation function will be from 0 and 1.

|     |     |
| --- | --- |
| 1   | func (a  *Perceptron) sigmoid(x  float64) float64 { //Sigmoid Activation |
| 2   | return  1.0  / (1.0  +  math.Exp(-x)) |
| 3   | }   |
| 4   |     |
| 5   | func (a  *Perceptron) forwardPass(x []float64) (sum  float64) { //Forward Propagation |
| 6   | return  a.sigmoid(dotProduct(a.weights, x) +  a.bias) |
| 7   | }   |

 [view raw](https://gist.github.com/dasaradhsk/88398f243961fbdcb208eed89a8265f9/raw/dc346de896f1b1f91ee53a0c3c55c8eb14b380fb/forward_propogation.go)  [forward_propogation.go](https://gist.github.com/dasaradhsk/88398f243961fbdcb208eed89a8265f9#file-forward_propogation-go) hosted with ❤ by [GitHub](https://github.com/)

# The Learning Algorithm

The learning algorithm consists of two parts — Backpropagation and Optimization.

**Backpropagation**, short for *backward propagation of errors*, refers to the algorithm for computing the gradient of the loss function with respect to the weights. However, the term is often used to refer to the entire learning algorithm.

A*  ***loss function***  *is used to get an estimation of how far are we from our desired solution. Generally, *mean squared error *is chosen as the loss function for regression problems and *cross-entropy* for classification problems. To keep it simple, we’ll use **mean squared error** as our loss function. Also, we will not be calculating the MSE but directly calculate its gradient.

![1*pCw12LYgdMmazhPYye_BAw.png](../_resources/b414245c301608fe1470721f72629414.png)
![1*ok5zJr_LlBuon7laKe1lNA.png](../_resources/02322981633f9b9ec7c728778951bc23.png)

The gradient of the loss function is calculated using the [**chain rule**](https://en.wikipedia.org/wiki/Chain_rule)**. **The gradients of the loss function with respect to the weights and bias are calculated as follows.

![0*mn2qELpNIMtn9AOf.png](../_resources/3e986f37be13e6bad27124946bfb13f1.png)
![0*Id6nTzxzCcSELTXW.png](../_resources/5527f7c9e3467bf66d8c59cbdb6727e8.png)

(for the derivation of these expressions, check my article in which I have briefly explained the [math concepts behind neural networks](https://medium.com/datadriveninvestor/a-gentle-introduction-to-math-behind-neural-networks-6c1900bb50e1))

![0*hn0TsWnfUMoVU9ND.png](../_resources/fa9023721a2a3d2adc60239e964132b0.png)
![0*hn0TsWnfUMoVU9ND.png](../_resources/3dc295664740c43134ab179bcd2d6c8f.png)

[Image source](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)

**Optimization **is the selection of best weights and bias of the perceptron to get the desired results. Let’s choose [**gradient descent**](https://en.wikipedia.org/wiki/Gradient_descent) as our optimization algorithm. The weights and the bias are updated as follows till **convergence**.

![0*fTLbyPBgPafj5i5S.png](../_resources/2b889462698f7373859ee08d61e56d7a.png)
![0*fTLbyPBgPafj5i5S.png](../_resources/fdbdc5628d1c135882f023ee9d251be9.png)

**Learning rate***  *(*α*) is a hyperparameter which is used to control how much the weights and bias are changed. However, we will not be using the l*earning rate* in this tutorial.

|     |     |
| --- | --- |
| 1   | func (a  *Perceptron) gradW(x []float64, y  float64) []float64 { //Calculate Gradients of Weights |
| 2   | pred  :=  a.forwardPass(x) |
| 3   | return  scalarMatMul(-(pred-y)*pred*(1-pred), x) |
| 4   | }   |
| 5   |     |
| 6   | func (a  *Perceptron) gradB(x []float64, y  float64) float64 { //Calculate Gradients of Bias |
| 7   | pred  :=  a.forwardPass(x) |
| 8   | return  -(pred  -  y) *  pred  * (1  -  pred) |
| 9   | }   |
| 10  |     |
| 11  |     |
| 12  | func (a  *Perceptron) train() { //Train the Perceptron for n epochs |
| 13  | for  i  :=  0; i  <  a.epochs; i++ { |
| 14  | dw  :=  make([]float64, len(a.input[0])) |
| 15  | db  :=  0.0 |
| 16  | for  length, val  :=  range  a.input { |
| 17  | dw  =  vecAdd(dw, a.gradW(val, a.actualOutput[length])) |
| 18  | db  +=  a.gradB(val, a.actualOutput[length]) |
| 19  | }   |
| 20  | dw  =  scalarMatMul(2  /  float64(len(a.actualOutput)), dw) |
| 21  | a.weights  =  vecAdd(a.weights, dw) |
| 22  | a.bias  +=  db  *  2  /  float64(len(a.actualOutput)) |
| 23  | }   |
| 24  | }   |

 [view raw](https://gist.github.com/dasaradhsk/c75627c3f9c1f7cf93cf9083bfd157f4/raw/31f355d589991a2ddc653bedcc0877969b39b5e3/train.go)  [train.go](https://gist.github.com/dasaradhsk/c75627c3f9c1f7cf93cf9083bfd157f4#file-train-go) hosted with ❤ by [GitHub](https://github.com/)

# Assembling the Pieces

Now let’s train and make predictions out of our neural network on the following data. The data has three inputs and only one output belonging to two classes(0 and 1). Hence the data can be trained on our single-layer perceptron.

![0*Id6nTzxzCcSELTXW.png](../_resources/830b7c8633b6763db5de52817f8ce81e.png)
![1*HeV0UK3fxAD9dj5xdquvYg.png](../_resources/e3af00b80afa2aacd8b760f3977603ef.png)

As you can see, the output **Y** is only dependent on the input **X1**. Now we will train our neural network on the above data and check how it performs after **1000 epochs**. To make predictions, we have to just do a forward propagation with the test inputs.

|     |     |
| --- | --- |
| 1   | func  main() { |
| 2   | goPerceptron  :=  Perceptron{ |
| 3   | input: [][]float64{{0, 0, 1}, {1, 1, 1}, {1, 0, 1}, {0, 1, 0}}, //Input Data |
| 4   | actualOutput: []float64{0, 1, 1, 0}, //Actual Output |
| 5   | epochs: 1000, //Number of Epoch |
| 6   | }   |
| 7   | goPerceptron.initialize() |
| 8   | goPerceptron.train() |
| 9   | print(goPerceptron.forwardPass([]float64{0, 1, 0}), "\n") //Make Predictions |
| 10  | print(goPerceptron.forwardPass([]float64{1, 0, 1}), "\n") |
| 11  | }   |

 [view raw](https://gist.github.com/dasaradhsk/4a8a7cf27f4d4042f131f311e210191b/raw/41464c83c422b6c039b7bf6f19c743d56cd32e54/perceptron_main.go)  [perceptron_main.go](https://gist.github.com/dasaradhsk/4a8a7cf27f4d4042f131f311e210191b#file-perceptron_main-go) hosted with ❤ by [GitHub](https://github.com/)

![1*HeV0UK3fxAD9dj5xdquvYg.png](../_resources/0e090abad7fc8556bedd6dc08972ecea.png)
![1*pCw12LYgdMmazhPYye_BAw.png](../_resources/2036a81b4014f911aeeff0542527d9b6.png)

As we compare the predicted values with the actual values, we can see that our trained single-layer perceptron has performed well. We’ve successfully created a neural network and trained it to produce desirable results.

# What’s Next?

Now you’ve created your own neural network completely from scratch. Here are a few things you shall try next.

- Test on your **own data**
- Try other **activation function** besides the sigmoid function
- Calculate **MSE **after each epoch
- Try other **error function** besides the MSE
- Try creating a **multi-layer perceptron**

# Final Thoughts

I hope that you’ve learned a lot from creating your own neural network in Golang. I’ll be writing more on topics related to machine learning & deep learning and I’ll be hopefully covering **multi-layer perceptron** in my next article.