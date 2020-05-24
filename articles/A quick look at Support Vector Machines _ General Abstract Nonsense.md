A quick look at Support Vector Machines | General Abstract Nonsense

# A quick look at Support Vector Machines

Mar 19, 2017   #[machine-learning](https://generalabstractnonsense.com/tags/machine-learning)

Support Vector Machines (SVMs) are a popular machine learning algorithm with lots of usages and I learned something quite amazing about them. But first let me tell you what SVMs do.

Imagine we have data points of two different classes:
![](../_resources/423f05b4f0a8a245d157bfc8c015e963.png)

A support vector machine can take that data as input and find a line that separates it. We call this line the decision boundary. But there are many separating lines, which one is the best? SVMs are going to choose the line that maximises the margin. Margin is the distance between the separating line and the nearest point of either of the two classes.

![](../_resources/57a44d1f824dfa4cd4f2ab8452145c67.png)

The intuition behind trying to maximise the margin is that a decision boundary with a smaller margin is more prone to overfitting, while a larger margin makes the result more robust.

# Non-linear data

Now look at this data:
![](../_resources/5bcb8e8a1e08ddc1b8935fb231dd37d3.png)

Given what we’ve seen so far we’d think an SVM couldn’t separate this, as there just isn’t a good separating line for this data.

But there’s a trick! It works like this: we’ll add a new feature to the data. So far we had 2 features, xx and yy, and we’re gonnna add one more. In this example I’ll conveniently choose a value for the new feature that I know works: x2+y2x2+y2

So now we have three dimensions and the zz axis has value x2+y2x2+y2. This is equal to the distance of each point from the origin.

![](../_resources/a66579b7276ff9df9ada018bb5122d78.png)
Is this now linearly separable?
![](../_resources/fe1d2dc0ba90a577045a4b599c84bacb.png)

And the answer is yes, there is a hyperplane that can separate the pink from the blue points.

The next step is to take this solution and go back to the original two-dimensional space. Since this line on the zz axis has an equation of x2+y2=somethingx2+y2=something it corresponds to a circle:

![](../_resources/efc75184427ae72b8f88bdf7d8b224eb.png)

# What we did

Here’s what we did:
![](../_resources/0f1673a66240688cb4f02a84e9183b94.png)
That’s pretty cool!

# Another example

One more example, this time using pen and paper.
Imagine we have this data:
![](../_resources/1b25d5d6f47eb3db1f8bedcd27e7d89d.jpg)

The pink and blue points are not linearly separable. We’re going to do the same trick and add a new feature. This time we’ll choose z=|x|z=|x|. So there is a zz axis on which the points have height equal to the absolute value of xx.

To do this with the paper I’m going to fold on the yy axis and then raise the sides by 45 degrees.

![](../_resources/2770363911feb6dc1e88e4b1402912ba.jpg)
Is this data now linearly separable?

It’s not very easy to see, but yes. I’m going to demonstrate that using a plastic folder as a hyperplane.

![](../_resources/20f83616cea4f12c74f38f4472c08757.jpg)

Finally we’re going to take this solution and map it back to the original two-dimensional space by unfolding the paper.

![](../_resources/a9f977f30f6b820cb58e6c0a57536c8d.jpg)
We now got a non-linear separation of the data.

# Code

That’s all pretty fun, but in real life you don’t really get to come up with new features like that.

There are some so called kernel functions, which take a low dimensional feature space and map it to a higher dimensional feature space, but do so in a computationally effective way using the so called kernel trick. I don’t understand them well enough, but I know that scikit-learn comes with a bunch of [kernels](http://scikit-learn.org/stable/modules/svm.html#svm-kernels) that can be used out of the box.

Here’s an example of creating some data similarly shaped to the example above and separating it using an SVM:

	from sklearn.svm import SVC
	import numpy as np
	import matplotlib.pyplot as plt
	from mlxtend.plotting import plot_decision_regions

	# create some V shaped data
	np.random.seed(6)
	X = np.random.randn(200, 2)
	y = X[:, 1] > np.absolute(X[:, 0])
	y = np.where(y, 1, -1)

	# train a Support Vector Classifier using the rbf kernel
	svm = SVC(kernel='rbf', random_state=0, gamma=0.5, C=10.0)
	svm.fit(X, y)
	plot_decision_regions(X, y, svm, markers=['o', 'x'], colors='blue,magenta')
	plt.show()

which outputs:
![](../_resources/72f68b23490e3690ad2aefdaf83257cb.png)