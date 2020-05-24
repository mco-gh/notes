An introduction to Support Vector Machines (SVM) | MonkeyLearn Blog

## An introduction to Support Vector Machines (SVM)

- [![](../_resources/f4df7768fb0c02ea8d05496da7fbf883.png)](https://monkeylearn.com/blog/wp-content/uploads/2017/06/Post_1e.png)

.

-
-

So you’re working on a text classification problem. You’re refining your training set, and maybe you’ve even tried stuff out using Naive Bayes. But now you’re feeling confident in your dataset, and want to take it one step further. Enter Support Vector Machines (SVM): a fast and dependable classification algorithm that performs very well with a limited amount of data.

Perhaps you have dug a bit deeper, and ran into terms like *linearly separable*, *kernel trick* and *kernel functions*. But fear not! The idea behind the SVM algorithm is simple, and applying it to natural language classification doesn’t require most of the complicated stuff.

Before continuing, we recommend reading [our guide to Naive Bayes classifiers](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/) first, since a lot of the things regarding text processing that are said there are relevant here as well.

Done? Great! Let’s move on.

## How does SVM work?

The basics of Support Vector Machines and how it works are best understood with a simple example. Let’s imagine we have two categories: *red* and *blue*, and our data has two [features](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/#feature-engineering): *x* and *y*. We want a classifier that, given a pair of *(x,y)* coordinates, outputs if it’s either *red *or *blue*. We plot our already labeled training data on a plane:

![a plane with two types of vectors in two clearly separated groups](../_resources/54bc4a6c75cedc94e6e62ff5311faddd.png)

A support vector machine takes these data points and outputs the hyperplane (which in two dimensions it’s simply a line) that best separates the categories. This line is the **decision boundary**: anything that falls to one side of it we will classify as *blue*, and anything that falls to the other as *red*.

![A plane with two groups of vectors separated with a line labeled "best hyperplane"](../_resources/d07eba048989392245383f3ce811a8dd.png)

But, what exactly is *the best* hyperplane? For SVM, it’s the one that maximizes the margins from both categories. In other words: the hyperlane (remember it’s a line in this case) whose distance to the nearest element of each category is the largest.

![A plane with two groups of vectors separated with a line labeled "best hyperplane", a line labeled "not as good" and lines illustrating the margins from each line to the closer data points](../_resources/fadd257756f9036cc96abb7e48a55f33.png)

You can check out [this video tutorial](https://www.youtube.com/watch?v=1NxnPkZM9bc) to learn exactly how this optimal hyperplane is found.

### Nonlinear data

Now this example was easy, since clearly the data was linearly separable — we could draw a straight line to separate *red* and *blue*. Sadly, usually things aren’t that simple. Take a look at this case:

![A plane with two types of vectors in two clearly separated groups, one in the middle and the other one around](../_resources/538295ec503d6bedc36e1941e3de3ae2.png)

It’s pretty clear that there’s not a linear decision boundary (a single straight line that separates both categories). However, the vectors are very clearly segregated and it looks as though it should be easy to separate them.

So here’s what we’ll do: we will add a third dimension. Up until now we had two dimensions: *x* and *y*. We create a new *z* dimension, and we rule that it be calculated a certain way that is convenient for us: *z = x² + y²* (you’ll notice that’s the equation for a circle).

This will give us a three dimensional space. Taking a slice of that space, it looks like this:

![The same data but looked at with another perspective, the data is now in two clearly separated groups](../_resources/5f50fbd72a4eb99885ea4ef45aaed5f0.png)

What can SVM do with this? Let’s see:

![The previous plane with a line separating both sets, labeled "best hyperplane"](../_resources/3a4f0e3a6e2947212869ad16f5eddfba.png)

That’s great! Note that since we are in three dimensions now, the hyperplane is a plane parallel to the *x* axis at a certain* z* (let’s say *z = 1*).

What’s left is mapping it back to two dimensions:

![The original dataset, with both classes separated by a circle](../_resources/707d354240b0ecc9e12609e6c84f1c9a.png)

And there we go! Our decision boundary is a circumference of radius 1, which separates both categories using SVM. Check out this 3d visualization to see another example of the same effect:

[SVM with polynomial kernel visualization](https://www.youtube.com/watch?v=3liCbRZPrZA)

[ 16. Learning: Support Vector MachinesMIT OpenCourseWare • 401K views49:34](https://www.youtube.com/watch?v=_PwhiWxHK8o)[ How SVM (Support Vector Machine) algorithm worksThales Sehn Körting • 274K views7:33](https://www.youtube.com/watch?v=1NxnPkZM9bc)[ Performing nonlinear classification via linear separation in higher dimensional spaceTeamGrizzly • 20K views1:07](https://www.youtube.com/watch?v=9NrALgHFwTo)[ For the Love of Physics (Walter Lewin's Last Lecture)For the Allure of Physics • 4.4M views1:01:26](https://www.youtube.com/watch?v=4a0FbQdH3dY)[ Amazon Jeff Bezos on Artificial Intelligence(AI), Cashless Store, Self-Driving Cars and Donald TrumpArtificial Intelligence • 70K views1:20:28](https://www.youtube.com/watch?v=VAM6b0UkEYw)[ Introduction to Support Vector Machine (SVM) and Kernel Trick (How does SVM and Kernel work?)Gopal Malakar • 8.1K views7:43](https://www.youtube.com/watch?v=ikt7Qze0czE)[ The Mandelbrot Set - The only video you need to see!TheBITK • 763K views21:19](https://www.youtube.com/watch?v=56gzV0od6DU)[ How to Learn Faster with the Feynman Technique (Example Included)Thomas Frank • 1.5M views5:48](https://www.youtube.com/watch?v=_f-qkGJBPts)[ Noam Chomsky (2017) "Advertising, Consumerism, and Human Nature"Noam Chomsky Videos • 7K views13:28](https://www.youtube.com/watch?v=pfi4yhGQ8hg)

![mqdefault.jpg](../_resources/de266680748030b21f31b9a5d2126b91.jpg)7:52

[The Halting Problem **Proof That Computers Can't Do Everything (The Halting Problem)**](https://www.youtube.com/watch?v=92WHN-pAFCs)

0:42 / 0:42
[(L)](https://www.youtube.com/watch?v=3liCbRZPrZA)

### The kernel trick

In our example we found a way to classify nonlinear data by cleverly mapping our space to a higher dimension. However, it turns out that calculating this transformation can get pretty computationally expensive: there can be a lot of new dimensions, each one of them possibly involving a complicated calculation. Doing this for every vector in the dataset can be a lot of work, so it’d be great if we could find a cheaper solution.

And we’re in luck! Here’s a trick: SVM doesn’t need the actual vectors to work its magic, it actually can get by only with the [dot products](https://en.wikipedia.org/wiki/Dot_product) between them. This means that we can sidestep the expensive calculations of the new dimensions! This is what we do instead:

- Imagine the new space we want:
    - z = x² + y²
- Figure out what the dot product in that space looks like:
    - *a · b = xa · xb  +  ya · yb  +  za · zb*
    - *a · b = xa · xb  +  ya · yb +  (xa² + ya²) · (xb² + yb²)*
- Tell SVM to do its thing, but using the new dot product — we call this a [**kernel function**](https://www.quora.com/What-are-Kernels-in-Machine-Learning-and-SVM).

That’s it! That’s the **kernel trick**, which allows us to sidestep a lot of expensive calculations. Normally, the kernel is linear, and we get a linear classifier. However, by using a nonlinear kernel (like above) we can get a nonlinear classifier without transforming the data at all: we only change the dot product to that of the space that we want and SVM will happily chug along.

Note that the kernel trick isn’t actually part of SVM. It can be used with other linear classifiers such as logistic regression. A support vector machine only takes care of finding the decision boundary.

## How can SVM be used with natural language classification?

So, we can classify vectors in multidimensional space. Great! Now, we want to apply this algorithm for text classification, and the first thing we need is a way to transform a piece of text into a vector of numbers so we can run SVM with them. In other words, which **features** do we have to use in order to classify texts using SVM?

The most common answer is word frequencies, [just like we did in Naive Bayes](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/#feature-engineering). This means that we treat a text as a bag of words, and for every word that appears in that bag we have a feature. The value of that feature will be how frequent that word is in the text.

This method boils down to just counting how many times every word appears in a text and dividing it by the total number of words. So in the sentence “All monkeys are primates but not all primates are monkeys” the word *monkeys* has a frequency of 2/10 = 0.2, and the word *but* has a frequency of 1/10 = 0.1 .

For a more advanced alternative for calculating frequencies, we can also use [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

Now that we’ve done that, every text in our dataset is represented as a vector with thousands (or tens of thousands) of dimensions, every one representing the frequency one of the words of the text. Perfect! This is what we feed to SVM for training. We can improve this by using preprocessing techniques, like [stemming](https://en.wikipedia.org/wiki/Lemmatisation), removing [stopwords](https://en.wikipedia.org/wiki/Stop_words), and using [n-grams](http://sebastianraschka.com/Articles/2014_naive_bayes_1.html#n-grams).

### Choosing a kernel function

Now that we have the feature vectors, the only thing left to do is choosing a kernel function for our model. Every problem is different, and the kernel function depends on what the data looks like. In our example, our data was arranged in concentric circles, so we chose a kernel that matched those data points.

Taking that into account, what’s best for natural language processing? Do we need a nonlinear classifier? Or is the data linearly separable? It turns out that it’s best to stick to a linear kernel. Why?

Back in our example, we had two features. Some real uses of SVM in other fields may use tens or even hundreds of features. Meanwhile, NLP classifiers use *thousands* of features, since they can have up to one for every word that appears in the training set. This changes the problem a little bit: while using nonlinear kernels may be a good idea in other cases, having this many features will end up making nonlinear kernels overfit the data. Therefore, it’s best to just stick to a good old linear kernel, which actually results in the best performance in these cases.

### Putting it all together

Now the only thing left to do is training! We have to take our set of labeled texts, convert them to vectors using word frequencies, and feed them to the algorithm — which will use our chosen kernel function — so it produces a model. Then, when we have a new unlabeled text that we want to classify, we convert it into a vector and give it to the model, which will output the category of the text.

## Final words

And that’s the basics of Support Vector Machines!
To sum up:

- A support vector machine allows you to classify data that’s linearly separable.
- If it isn’t linearly separable, you can use the kernel trick to make it work.
- However, for text classification it’s better to just stick to a linear kernel.

Compared to newer algorithms like neural networks, they have two main advantages: higher speed and better performance with a limited number of samples (in the thousands). This makes the algorithm very suitable for text classification problems, where it’s common to have access to a dataset of at most a couple of thousands of tagged samples.

For an in-depth explanation of this algorithm, check out [this excellent MIT lecture](https://www.youtube.com/watch?v=_PwhiWxHK8o). If you are interested in an explanation of other machine learning algorithm, check out our [practical explanation of Naive Bayes](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/). And for other articles on the topic, you might also like our [guide to natural language processing](https://monkeylearn.com/blog/the-definitive-guide-to-natural-language-processing/) and our [guide to machine learning](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/).

By [Bruno Stecanella](https://monkeylearn.com/blog/author/bruno/)|June 22nd, 2017|[News](https://monkeylearn.com/blog/category/news/)|[0 Comments](https://monkeylearn.com/blog/introduction-to-support-vector-machines-svm/#respond)

## About the Author: [Bruno Stecanella](https://monkeylearn.com/blog/author/bruno/)

![25738393f5c37a597f8e8e2717812ff5.jpg](../_resources/e38cebec32acb7de55991dc44dbe2c3b.jpg)

Engineering student and primate enthusiast. I write code and blog about monkeys. Sometimes about other stuff, too.

## Related Posts

- [![](../_resources/71d27a6791013ac060d6edc2ef968bed.png)](https://monkeylearn.com/blog/monkeylearn-zapier-integration/)

### [MonkeyLearn + Zapier Integration](https://monkeylearn.com/blog/monkeylearn-zapier-integration/)

- [![Picture of a naive monkey](../_resources/db346111b987fb0832fbf193f095fd6a.png)](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/)

### [A practical explanation of a Naive Bayes classifier](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/)

- [![](../_resources/c884d60b6cd4eddbf3d1018ce298f0cc.png)](https://monkeylearn.com/blog/analyzing-10-years-of-startup-news-with-machine-learning/)

### [Analyzing 10 years of startup news with Machine Learning  ### Analyzing startup news — part 3](https://monkeylearn.com/blog/analyzing-10-years-of-startup-news-with-machine-learning/)

- [![google-sheets-addon-machine-learning](../_resources/7ddc9baf41cc1cc69acdba5f094e2d90.png)](https://monkeylearn.com/blog/introducing-google-sheets-add-on-for-monkeylearn/)

### [Introducing Google Sheets add-on for MonkeyLearn](https://monkeylearn.com/blog/introducing-google-sheets-add-on-for-monkeylearn/)



###

## Leave A Comment