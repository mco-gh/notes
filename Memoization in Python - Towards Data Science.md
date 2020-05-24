Memoization in Python - Towards Data Science

# Memoization in Python

## Introduction to Memoization

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='184' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='185' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*jaDCzaMpvRadb_aUH-Gw3Q.png](../_resources/670441894d090c49cd976772842a5ac7.png)](https://towardsdatascience.com/@spierre91?source=post_page-----57c0a738179a----------------------)

[Sadrach Pierre, Ph.D.](https://towardsdatascience.com/@spierre91?source=post_page-----57c0a738179a----------------------)

[Apr 8](https://towardsdatascience.com/memoization-in-python-57c0a738179a?source=post_page-----57c0a738179a----------------------) · 5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='201'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='202' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='207'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='208' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/57c0a738179a/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='216'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='217' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/57c0a738179a/share/facebook?source=post_actions_header---------------------------)

![1*FVoZ2l7PdWq8oy1ABCIhpA.jpeg](../_resources/4e7fb3487dc5e3c9d6a36d1ff4dadc49.jpg)
![1*FVoZ2l7PdWq8oy1ABCIhpA.jpeg](../_resources/971a3a6191e593138517c79be881ad5d.jpg)
[Source](https://www.pexels.com/photo/camera-photography-vintage-travel-46794/)

Memoization is a term introduced by Donald Michie in 1968, which comes from the latin word memorandum (to be remembered). Memoization is a method used in computer science to speed up calculations by storing (remembering) past calculations. If repeated function calls are made with the same parameters, we can store the previous values instead of repeating unnecessary calculations. In this post, we will use memoization to find terms in the Fibonacci sequence.

Let’s get started!

First, let’s define a recursive function that we can use to display the first *n *terms in the Fibonacci sequence. If you are unfamiliar with recursion, check out this article: [*Recursion in Python*](https://towardsdatascience.com/recursion-in-python-b026d7dde906)*.*

As a reminder, the Fibonacci sequence is defined such that each number is the sum of the two previous numbers. For example, the first 6 terms in the Fibonacci sequence are 1, 1, 2, 3, 5, 8. We can define the recursive function as follows:

def fibonacci(input_value):
if input_value == 1:
return 1
elif input_value == 2:
return 1
elif input_value > 2
return fibonacci(input_value -1) + fibonacci(input_value -2)

Here we specify the base cases, which say that if the input value is equal to 1 or 2, return 1. If the input value is greater than 2, return recursive function calls summing the previous two Fibonacci values.

Now, let’s print the first 10 terms:
for i in range(1, 11):
print("fib({}) = ".format(i), fibonacci(i))
![1*LBhatMQDWtw9GAKBValTJw.png](:/dae91dc67758bc06026cca9cb732e305)
![1*LBhatMQDWtw9GAKBValTJw.png](../_resources/cb711d2e3b5fd21ef48376c855f4f02d.png)
This seems to run fine. Now, let’s try displaying the first 200 terms:
for i in range(1, 201):
print("fib({}) = ".format(i), fibonacci(i))
![1*LCgCkenrcK36Tvamd5KEfA.png](../_resources/3b2c931430b934512b8bde9bd8ea5173.png)
![1*LCgCkenrcK36Tvamd5KEfA.png](../_resources/d781809b4501d80f6e32e133b2a01c53.png)

What we’ll find is that after fib(20) subsequent calculations take significantly longer than previous calculations. This is because with each subsequent calculation we are doing repeated work.

Consider how the recursive function is calculating each term:
fib(1) = 1
fib(2) = 1
fib(3) = fib(1) + fib(2) = 2
fib(4) = fib(3) + fib(2) = 3
fib(5) = fib(4) + fib(3) = 5

Notice, for fib(5) we are repeating the calculation of fib(4) and fib(3). If we had a way of remembering/storing those values upon calculating them, we’d avoid repeating calculations. This forms the motivation for the memoization method.

Let’s now walk through the steps of implementing the memoization method. To proceed, let’s initialize a dictionary:

fibonacci_cache = {}

Next, we will define our memoization function. First, we check if the input, which will be the dictionary key, exists in the dictionary. If the key is present we return the value corresponding to the input/key:

def fibonacci_memo(input_value):
if input_value in fibonacci_cache:
return fibonacci_cache[input_value]

Next, we define the base cases, which correspond to the two first values. If the input value is 1 or 2 then we set the value to 1:

def fibonacci_memo(input_value):
... if input_value == 1:
value = 1
elif input_value == 2:
value = 1

Next, we consider the recursive cases. If the input is greater than 2, we set the value equal to the sum of the previous two terms:

def fibonacci_memo(input_value):
...
elif input_value > 2:
value = fibonacci_memo(input_value -1) + fibonacci_memo(input_value -2)
At the end we store the value in our dictionary and return the value:
def fibonacci_memo(input_value):
...
fibonacci_cache[input_value] = value
return value
The full function is:
def fibonacci_memo(input_value):
if input_value in fibonacci_cache:
return fibonacci_cache[input_value]
if input_value == 1:
value = 1
elif input_value == 2:
value = 1
elif input_value > 2:
value = fibonacci_memo(input_value -1) + fibonacci_memo(input_value -2)
fibonacci_cache[input_value] = value
return value
Now, let’s try displaying the first 200 terms with our new function:
for i in range(1, 201):
print("fib({}) = ".format(i), fibonacci_memo(i))
![1*UcIyB8pxaTLEcQvpROAW6A.png](../_resources/3182600236e2f39e0b23b645b5ee1d23.png)
![1*UcIyB8pxaTLEcQvpROAW6A.png](../_resources/029b216d20fb51658690a4b4d562cf17.png)

Upon running our script, we see that we arrived at the 200th term in the sequence rather quickly.

There is a simpler way to implement memoization using less code. Let’s consider our original recursive function:

def fibonacci(input_value):
if input_value == 1:
return 1
elif input_value == 2:
return 1
elif input_value > 2
return fibonacci(input_value -1) + fibonacci(input_value -2)

We can import a decorator from the ‘functools’ module, called ‘lru_cache’, that allows us to cache our values. The name stands for “least recently used cache”. We can achieve the same performance as our ‘fibonacci_memo’ method using this decorator:

from functools import lru_cache[@lru_cache](http://twitter.com/lru_cache)(maxsize = 1000)

def fibonacci(input_value):
if input_value == 1:
return 1
elif input_value == 2:
return 1
elif input_value > 2

return fibonacci(input_value -1) + fibonacci(input_value -2)for i in range(1, 201):

print("fib({}) = ".format(i), fibonacci(i))
![1*UcIyB8pxaTLEcQvpROAW6A.png](../_resources/3182600236e2f39e0b23b645b5ee1d23.png)
![1*UcIyB8pxaTLEcQvpROAW6A.png](../_resources/029b216d20fb51658690a4b4d562cf17.png)

We see that we achieve similar performance. I’ll stop here but I encourage you to play around with the code yourself.

# CONCLUSIONS

To summarize, in this post we discussed the memoization method in python. First, we showed how the naive implementation of a recursive function becomes very slow after calculating many terms in the Fibonacci sequence. We then defined a new method where we stored past values that we’ve calculated in a dictionary. This leads to a significant speedup in calculations. We then discussed the ‘lru_cache’ decorator which allowed us to achieve a similar performance as our ‘fibonacci_memo’ method with less code. If you’re interested in learning more about memoization, I encourage you to check out [Socratica’s YouTube tutorials](https://www.youtube.com/watch?v=Qk0zUZW-U_M&t=302s). I hope you found this post useful/interesting. The code in this post is available on [GitHub](https://github.com/spierre91/medium_code/blob/master/data_structures_and_algorithms/memo_fibonacci.py). Thank you for reading!