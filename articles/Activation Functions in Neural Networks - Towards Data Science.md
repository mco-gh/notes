Activation Functions in Neural Networks - Towards Data Science

#### Top highlight

# Activation Functions in Neural Networks

## Sigmoid, tanh, Softmax, ReLU, Leaky ReLU EXPLAINED !!!

[![1*Yfq1AFxdV07S9TMoogUx2g.png](../_resources/69480133341bffdb64b5961ee7c1ebf9.png)](https://towardsdatascience.com/@sagarsharma4244?source=post_page-----1cbd9f8d91d6----------------------)

[SAGAR SHARMA](https://towardsdatascience.com/@sagarsharma4244?source=post_page-----1cbd9f8d91d6----------------------)

[Sep 6, 2017](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6?source=post_page-----1cbd9f8d91d6----------------------) · 5 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='206'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='207' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/1cbd9f8d91d6/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='215'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='216' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/1cbd9f8d91d6/share/facebook?source=post_actions_header---------------------------)

![1*GIPiAdQyOa8wUOkHaL-MJg.gif](../_resources/e4f82a695cbeaf14f794fd09ce78f02a.jpg)
![1*GIPiAdQyOa8wUOkHaL-MJg.gif](../_resources/5e002275656b999cd9eb8c152c3265a2.gif)

## **What is Activation Function?**

> It’s just a thing function that you use to get the output of node. It is also known as **> Transfer Function**> .

* * *

*...*

## **Why we use Activation functions with Neural Networks?**

> It is used to determine the output of neural network like yes or no. It maps the resulting values in between 0 to 1 or -1 to 1 etc. (depending upon the function).

The Activation Functions can be basically divided into 2 types-
1. Linear Activation Function
2. Non-linear Activation Functions
**> FYI: The Cheat sheet is given below.**

* * *

*...*

## **Linear or Identity Activation Function**

As you can see the function is a line or linear. Therefore, the output of the functions will not be confined between any range.

![1*tldIgyDQWqm-sMwP7m3Bww.png](../_resources/da4d024a711c817da41f4be44e01f671.png)
![1*tldIgyDQWqm-sMwP7m3Bww.png](../_resources/fa75c2e0e19b347b3681b29d583cc28e.png)
**Fig: Linear Activation Function**
**Equation : **f(x) = x
**Range :** (-infinity to infinity)

It doesn’t help with the complexity or various parameters of usual data that is fed to the neural networks.

## **Non-linear Activation Function**

The Nonlinear Activation Functions are the most used activation functions. Nonlinearity helps to makes the graph look something like this

![1*cxNqE_CMez7vUIkcLUH8PA.png](../_resources/ec1c907250d44edfc1ac4ff04a32e38e.png)
![1*cxNqE_CMez7vUIkcLUH8PA.png](../_resources/af97d445f7d29de80d5e8dddad5f9a39.png)
**Fig: Non-linear Activation Function**

It makes it easy for the model to generalize or adapt with variety of data and to differentiate between the output.

The main terminologies needed to understand for nonlinear functions are:

**> Derivative or Differential: **> Change in y-axis w.r.t. change in x-axis.It is also known as slope.

**> Monotonic function:**>  A function which is either entirely non-increasing or non-decreasing.

The Nonlinear Activation Functions are mainly divided on the basis of their **range or curves**-

## **1. Sigmoid or Logistic Activation Function**

The Sigmoid Function curve looks like a S-shape.
![1*Xu7B5y9gp0iL5ooBj7LtWw.png](../_resources/100f0d3d047bb8c89c6ac73dde93815c.png)
![1*Xu7B5y9gp0iL5ooBj7LtWw.png](../_resources/07066668c05a556f1ff25040414a32b7.png)
**Fig: Sigmoid Function**

The main reason why we use sigmoid function is because it exists between **(0 to 1). **Therefore, it is especially used for models where we have to **predict the probability** as an output.Since probability of anything exists only between the range of **0 and 1,** sigmoid is the right choice.

The function is **differentiable**.That means, we can find the slope of the sigmoid curve at any two points.

The function is **monotonic **but function’s derivative is not.

The logistic sigmoid function can cause a neural network to get stuck at the training time.

The **softmax function** is a more generalized logistic activation function which is used for multiclass classification.

## **2. Tanh or hyperbolic tangent Activation Function**

tanh is also like logistic sigmoid but better. The range of the tanh function is from (-1 to 1). tanh is also sigmoidal (s - shaped).

![1*f9erByySVjTjohfFdNkJYQ.jpeg](../_resources/150b931650c5f9de80598ce1da0b7db0.png)
![1*f9erByySVjTjohfFdNkJYQ.jpeg](../_resources/943ade3a96ef815175fc8dc7823bc3e4.png)
**Fig: tanh v/s Logistic Sigmoid**

The advantage is that the negative inputs will be mapped strongly negative and the zero inputs will be mapped near zero in the tanh graph.

The function is **differentiable**.
The function is **monotonic** while its **derivative is not monotonic**.
The tanh function is mainly used classification between two classes.

> Both tanh and logistic sigmoid activation functions are used in feed-forward nets.

## **3. ReLU (Rectified Linear Unit) Activation Function**

The ReLU is the most used activation function in the world right now.Since, it is used in almost all the convolutional neural networks or deep learning.

![1*XxxiA0jJvPrHEJHD4z893g.png](../_resources/bf28870849329aa7fdd0f360c49d4e1b.png)
![1*XxxiA0jJvPrHEJHD4z893g.png](../_resources/dbd547fcd8927682c9d6350c2eb51108.png)
**Fig: ReLU v/s Logistic Sigmoid**

As you can see, the ReLU is half rectified (from bottom). f(z) is zero when z is less than zero and f(z) is equal to z when z is above or equal to zero.

**Range: **[ 0 to infinity)
The function and its derivative **both are**  **monotonic**.

But the issue is that all the negative values become zero immediately which decreases the ability of the model to fit or train from the data properly. That means any negative input given to the ReLU activation function turns the value into zero immediately in the graph, which in turns affects the resulting graph by not mapping the negative values appropriately.

## **4. Leaky ReLU**

It is an attempt to solve the dying ReLU problem
![1*A_Bzn0CjUgOXtPCJKnKLqA.jpeg](../_resources/1d5d90902f41f6aab3ccf1b3d7fcc949.jpg)
![1*A_Bzn0CjUgOXtPCJKnKLqA.jpeg](../_resources/13f4849a1715409d2efe8a9f41d36bbd.jpg)
**Fig : ReLU v/s Leaky ReLU**
Can you see the Leak?

The leak helps to increase the range of the ReLU function. Usually, the value of **a **is 0.01 or so.

When **a is not 0.01** then it is called **Randomized ReLU**.
Therefore the **range** of the Leaky ReLU is (-infinity to infinity).

Both Leaky and Randomized ReLU functions are monotonic in nature. Also, their derivatives also monotonic in nature.

## Why derivative/differentiation is used ?

> When updating the curve, to know in **> which direction**>  and **> how much**>  to change or update the curve depending upon the slope.That is why we use differentiation in almost every part of Machine Learning and Deep Learning.

![1*p_hyqAtyI8pbt2kEl6siOQ.png](../_resources/e28f6b741d30afca9f94ed2bbfd1c1e5.png)
![1*p_hyqAtyI8pbt2kEl6siOQ.png](../_resources/b66165260a16d1343cca3373bbbc9674.png)
**Fig: Activation Function Cheetsheet**
![1*n1HFBpwv21FCAzGjmWt1sg.png](../_resources/4fcc4d8a5876e8f5e8db73e0981caff1.png)
![1*n1HFBpwv21FCAzGjmWt1sg.png](../_resources/ae245b144ce02830e258ca46ad1d3063.png)
**Fig: Derivative of Activation Functions**

* * *

*...*
![1*B_EOC2l6EIKmgQRKJ4g_lg.gif](../_resources/0ebc7fb80cc05f2b2fb83da31dc1586b.jpg)
![1*B_EOC2l6EIKmgQRKJ4g_lg.gif](../_resources/a46637ecc69c657dc5a051f657f47328.gif)
I will be posting 2 posts per week so don’t miss the tutorial.

So, follow me on [Medium](https://medium.com/@sagarsharma4244), [Facebook](https://www.facebook.com/profile.php?id=100003188718299), [Twitter](https://twitter.com/SagarSharma4244), [LinkedIn](https://www.linkedin.com/in/sagar-sharma-232a06148/), [Google+](https://plus.google.com/u/0/+SAGARSHARMA4244), [Quora](https://www.quora.com/profile/Sagar-Sharma-71) to see similar posts.

Any comments or if you have any question, **write it in the comment.**
**Clap it! Share it! Follow Me!**
Happy to be helpful. kudos…..

* * *

*...*

# Previous stories you will love:

[ ## What is Linear Regression and How does it work? - theffork   ### It is a method used for predicting future values by finding a linear pattern in the previously given data. The linear…    #### theffork.com](https://theffork.com/what-is-linear-regression-and-how-does-it-work/)

[ ## What the Hell is “Tensor” in “TensorFlow”?   ### I didn’t know it…    #### hackernoon.com](https://hackernoon.com/what-the-hell-is-tensor-in-tensorflow-e40dbf0253ee)

[ ## Epoch vs Batch Size vs Iterations   ### Know your code…    #### towardsdatascience.com](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)

[ ## Monte Carlo Tree Search   ### MCTS For Every Data Science Enthusiast    #### towardsdatascience.com](https://towardsdatascience.com/monte-carlo-tree-search-158a917a8baa)

[ ## Policy Networks vs Value Networks in Reinforcement Learning   ### In Reinforcement Learning, the agents take random decisions in their environment and learns on selecting the right one…    #### towardsdatascience.com](https://towardsdatascience.com/policy-networks-vs-value-networks-in-reinforcement-learning-da2776056ad2)

[ ## TensorFlow Image Recognition Python API Tutorial   ### On CPU with Inception-v3(In seconds)    #### towardsdatascience.com](https://towardsdatascience.com/tensorflow-image-recognition-python-api-e35f7d412a70)

[ ## How to Send Emails using Python   ### Design Professional Mails using Flask!    #### medium.com](https://medium.com/@sagarsharma4244/how-to-send-emails-using-python-4293dacc57d9)