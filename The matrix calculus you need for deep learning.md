The matrix calculus you need for deep learning

# The Matrix Calculus You Need For Deep Learning

*Brought to you by [explained.ai](http://explained.ai/)*

[Terence Parr](http://parrt.cs.usfca.edu/) and [Jeremy Howard](http://www.fast.ai/about/#jeremy)

(We teach in University of San Francisco's [MS in Data Science program](https://www.usfca.edu/arts-sciences/graduate-programs/data-science) and have other nefarious projects underway. You might know Terence as the creator of the [ANTLR parser generator](http://www.antlr.org/). For more material, see Jeremy's [fast.ai courses](http://course.fast.ai/) and University of San Francisco's Data Institute [in-person version of the deep learning course](https://www.usfca.edu/data-institute/certificates/deep-learning-part-one).)

[Printable version](https://arxiv.org/abs/1802.01528) (This HTML was generated from markup using [bookish](https://github.com/parrt/bookish))

**Abstract**

This paper is an attempt to explain all the matrix calculus you need in order to understand the training of deep neural networks. We assume no math knowledge beyond what you learned in calculus 1, and provide links to help you refresh the necessary math where needed. Note that you do **not** need to understand this material before you start learning to train and use deep learning in practice; rather, this material is for those who are already familiar with the basics of neural networks, and wish to deepen their understanding of the underlying math. Don't worry if you get stuck at some point along the way---just go back and reread the previous section, and try writing down and working through some examples. And if you're still stuck, we're happy to answer your questions in the [Theory category at forums.fast.ai](http://forums.fast.ai/c/theory). **Note**: There is a [reference section](https://explained.ai/matrix-calculus/index.html#reference) at the end of the paper summarizing all the key matrix calculus rules and terminology discussed here.

Contents

- [Introduction](https://explained.ai/matrix-calculus/index.html#intro)

- [Review: Scalar derivative rules](https://explained.ai/matrix-calculus/index.html#sec2)

- [Introduction to vector calculus and partial derivatives](https://explained.ai/matrix-calculus/index.html#sec3)

- [Matrix calculus](https://explained.ai/matrix-calculus/index.html#sec4)
    - [Generalization of the Jacobian](https://explained.ai/matrix-calculus/index.html#sec4.1)
    - [Derivatives of vector element-wise binary operators](https://explained.ai/matrix-calculus/index.html#sec4.2)
    - [Derivatives involving scalar expansion](https://explained.ai/matrix-calculus/index.html#sec4.3)
    - [Vector sum reduction](https://explained.ai/matrix-calculus/index.html#sec4.4)
    - [The Chain Rules](https://explained.ai/matrix-calculus/index.html#sec4.5)
- [The gradient of neuron activation](https://explained.ai/matrix-calculus/index.html#sec5)

- [The gradient of the neural network loss function](https://explained.ai/matrix-calculus/index.html#sec6)
    - [The gradient with respect to the weights](https://explained.ai/matrix-calculus/index.html#sec6.1)
    - [The derivative with respect to the bias](https://explained.ai/matrix-calculus/index.html#sec6.2)
- [Summary](https://explained.ai/matrix-calculus/index.html#sec7)

- [Matrix Calculus Reference](https://explained.ai/matrix-calculus/index.html#reference)
    - [Gradients and Jacobians](https://explained.ai/matrix-calculus/index.html#sec8.1)
    - [Element-wise operations on vectors](https://explained.ai/matrix-calculus/index.html#sec8.2)
    - [Scalar expansion](https://explained.ai/matrix-calculus/index.html#sec8.3)
    - [Vector reductions](https://explained.ai/matrix-calculus/index.html#sec8.4)
    - [Chain rules](https://explained.ai/matrix-calculus/index.html#sec8.5)
- [Notation](https://explained.ai/matrix-calculus/index.html#notation)

- [Resources](https://explained.ai/matrix-calculus/index.html#sec10)

## Introduction

Most of us last saw calculus in school, but derivatives are a critical part of machine learning, particularly deep neural networks, which are trained by optimizing a loss function. Pick up a machine learning paper or the documentation of a library such as [PyTorch](http://pytorch.org/) and calculus comes screeching back into your life like distant relatives around the holidays. And it's not just any old scalar calculus that pops up---you need differential *matrix calculus*, the shotgun wedding of [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) and [multivariate calculus](https://en.wikipedia.org/wiki/Multivariable_calculus).

Well... maybe *need* isn't the right word; Jeremy's courses show how to become a world-class deep learning practitioner with only a minimal level of scalar calculus, thanks to leveraging the automatic differentiation built in to modern deep learning libraries. But if you really want to really understand what's going on under the hood of these libraries, and grok academic papers discussing the latest advances in model training techniques, you'll need to understand certain bits of the field of matrix calculus.

For example, the activation of a single computation unit in a neural network is typically calculated using the dot product (from linear algebra) of an edge weight vector w with an input vector x plus a scalar bias (threshold): ![](../_resources/42fbc0e5e4ff838d90e96d878061b275.png). Function ![](../_resources/cd80e794da5168f63c2ba2907d6ef68d.png) is called the unit's *affine function* and is followed by a [rectified linear unit](https://goo.gl/7BXceK), which clips negative values to zero: ![](../_resources/b5a2e3a90eda319fcbf1459d38820f0f.png). Such a computational unit is sometimes referred to as an “artificial neuron” and looks like:

![](../_resources/5eaa9cfae544d714d3e9e693da53049a.png)

Neural networks consist of many of these units, organized into multiple collections of neurons called *layers*. The activation of one layer's units become the input to the next layer's units. The activation of the unit or units in the final layer is called the network output.

*Training* this neuron means choosing weights w and bias *b* so that we get the desired output for all *N* inputs x. To do that, we minimize a *loss function* that compares the network's final ![](../_resources/b50490e4874b77c88ed7ea207840f33a.png) with the ![](../_resources/f9998e135190bd6c297f47ff734e52b6.png) (desired output of x) for all input x vectors. To minimize the loss, we use some variation on gradient descent, such as plain [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (SGD), SGD with momentum, or [Adam](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam). All of those require the partial derivative (the gradient) of ![](../_resources/b50490e4874b77c88ed7ea207840f33a.png) with respect to the model parameters w and *b*. Our goal is to gradually tweak w and *b* so that the overall loss function keeps getting smaller across all x inputs.

If we're careful, we can derive the gradient by differentiating the scalar version of a common loss function (mean squared error):

![](../_resources/f1bceedb9aa6f623842c45bf2312a660.png)

But this is just one neuron, and neural networks must train the weights and biases of all neurons in all layers simultaneously. Because there are multiple inputs and (potentially) multiple network outputs, we really need general rules for the derivative of a function with respect to a vector and even rules for the derivative of a vector-valued function with respect to a vector.

This article walks through the derivation of some important rules for computing partial derivatives with respect to vectors, particularly those useful for training neural networks. This field is known as *matrix calculus*, and the good news is, we only need a small subset of that field, which we introduce here. While there is a lot of online material on multivariate calculus and linear algebra, they are typically taught as two separate undergraduate courses so most material treats them in isolation. The pages that do discuss matrix calculus often are really just lists of rules with minimal explanation or are just pieces of the story. They also tend to be quite obscure to all but a narrow audience of mathematicians, thanks to their use of dense notation and minimal discussion of foundational concepts. (See the annotated list of resources at the end.)

In contrast, we're going to rederive and rediscover some key matrix calculus rules in an effort to explain them. It turns out that matrix calculus is really not that hard! There aren't dozens of new rules to learn; just a couple of key concepts. Our hope is that this short paper will get you started quickly in the world of matrix calculus as it relates to training neural networks. We're assuming you're already familiar with the basics of neural network architecture and training. If you're not, head over to [Jeremy's course](http://course.fast.ai/) and complete part 1 of that, then we'll see you back here when you're done. (Note that, unlike many more academic approaches, we strongly suggest *first* learning to train and use neural networks in practice and *then* study the underlying math. The math will be much more understandable with the context in place; besides, it's not necessary to grok all this calculus to become an effective practitioner.)

*A note on notation*: Jeremy's course exclusively uses code, instead of math notation, to explain concepts since unfamiliar functions in code are easy to search for and experiment with. In this paper, we do the opposite: there is a lot of math notation because one of the goals of this paper is to help you understand the notation that you'll see in deep learning papers and books. At the [end of the paper](https://explained.ai/matrix-calculus/index.html#notation), you'll find a brief table of the notation used, including a word or phrase you can use to search for more details.

## Review: Scalar derivative rules

Hopefully you remember some of these main scalar derivative rules. If your memory is a bit fuzzy on this, have a look at [Khan academy vid on scalar derivative rules](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules).

| Rule | ![](../_resources/0a92a0c599b5296f09a66a6f833e428f.png) | Scalar derivative notation with respect to *x* | Example |
| --- | --- | --- | --- |
| **Constant** | *c* | ![](../_resources/74f403be4de924e7478d8e2c520a0fad.png) | ![](../_resources/965557a424533ac97f0caaa0887973bc.png) |
| **Multiplication by constant** | *cf* | ![](../_resources/d54478ff1fc6135581380469af758500.png) | ![](../_resources/eece42a3e571bbcb88bd9e337a54c393.png) |
| **Power Rule** | ![](../_resources/5cd870476398ce4bbbb302a3d530c26b.png) | ![](../_resources/7856ffdf577c6b237a287c74a1fca005.png) | ![](../_resources/5677911bf511121a8b017fd2f5ecd337.png) |
| **Sum Rule** | ![](../_resources/aa2252847fe5c3e5950fc0e0a4d9a40a.png) | ![](../_resources/96202480045f32262389c95c8c96561b.png) | ![](../_resources/475578cbd2056212c17428a3defbcfda.png) |
| **Difference Rule** | ![](../_resources/99556c773bbb4dae4b3f63937606c441.png) | ![](../_resources/7c406912169cd37ebbdc6f38c44f8141.png) | ![](../_resources/08e8cd5b630662a26505479b57c6ff15.png) |
| **Product Rule** | *fg* | ![](../_resources/d80755eb847c2b7803842af257bcf3dd.png) | ![](../_resources/74a3c847a6e15c105cb02057e12a3a77.png) |
| **Chain Rule** | ![](../_resources/290dfbaf469a3c91598c5fbfe6a7a62f.png) | ![](../_resources/366f84be0065d8715811c6cc52d65d39.png), let ![](../_resources/d6731fd596fa4458c994be40d089f354.png) | ![](../_resources/7f996bb3d95e8eac9cdd1e293fa836d5.png) |

There are other rules for trigonometry, exponentials, etc., which you can find at [Khan Academy differential calculus course](https://www.khanacademy.org/math/differential-calculus).

When a function has a single parameter, ![](../_resources/0a92a0c599b5296f09a66a6f833e428f.png), you'll often see ![](../_resources/caafa95c0fe8c6f9b448100d3e56039b.png) and ![](../_resources/24f8145bbf75ab0e0cb21b2f1885eca9.png) used as shorthands for ![](../_resources/1e85b2821b4472d49239281218814ab9.png). We recommend against this notation as it does not make clear the variable we're taking the derivative with respect to.

You can think of ![](../_resources/caf33477654033ee4aea2f929cba7a07.png) as an operator that maps a function of one parameter to another function. That means that ![](../_resources/1e85b2821b4472d49239281218814ab9.png) maps ![](../_resources/0a92a0c599b5296f09a66a6f833e428f.png) to its derivative with respect to *x*, which is the same thing as ![](../_resources/ff22bd41d08443ca1dbf4cf7b990fa25.png). Also, if ![](../_resources/0fbf3257c1e8f1c3d84ebbef2284701e.png), then ![](../_resources/fdf55fa1aff41b056d4efe015b6c3b47.png). Thinking of the derivative as an operator helps to simplify complicated derivatives because the operator is distributive and lets us pull out constants. For example, in the following equation, we can pull out the constant 9 and distribute the derivative operator across the elements within the parentheses.

![](../_resources/984ead7e0e40d5693b03622d91549aaf.png)

That procedure reduced the derivative of ![](../_resources/7b1be6b6cc672cc152b9f3e7728ac28a.png) to a bit of arithmetic and the derivatives of *x* and ![](../_resources/fb3b40bf0d82a8aea24915c687231648.png), which are much easier to solve than the original derivative.

## Introduction to vector calculus and partial derivatives

Neural network layers are not single functions of a single parameter, ![](../_resources/0a92a0c599b5296f09a66a6f833e428f.png). So, let's move on to functions of multiple parameters such as ![](../_resources/e143776bb936859a4513e9d9288478bb.png). For example, what is the derivative of *xy* (i.e., the multiplication of *x* and *y*)? In other words, how does the product *xy* change when we wiggle the variables? Well, it depends on whether we are changing *x* or *y*. We compute derivatives with respect to one variable (parameter) at a time, giving us two different *partial derivatives* for this two-parameter function (one for *x* and one for *y*). Instead of using operator ![](../_resources/caf33477654033ee4aea2f929cba7a07.png), the partial derivative operator is ![](../_resources/f8921b9df9c1fbe5ee7bdcc2344ac3ae.png) (a stylized *d* and not the Greek letter ![](../_resources/710459c72dd6a375523473fe1dbdff10.png)). So, ![](../_resources/495cd959887b867fa2288040448d9bf2.png) and ![](../_resources/1aa3c9690d53fa526df5360aa26093b8.png) are the partial derivatives of *xy*; often, these are just called the *partials*. For functions of a single parameter, operator ![](../_resources/f8921b9df9c1fbe5ee7bdcc2344ac3ae.png) is equivalent to ![](../_resources/caf33477654033ee4aea2f929cba7a07.png) (for sufficiently smooth functions). However, it's better to use ![](../_resources/caf33477654033ee4aea2f929cba7a07.png) to make it clear you're referring to a scalar derivative.

The partial derivative with respect to *x* is just the usual scalar derivative, simply treating any other variable in the equation as a constant. Consider function ![](../_resources/c6f753af6fd51a6925d03f704ed89b50.png). The partial derivative with respect to *x* is written ![](../_resources/9f2bc45a7d318e596db595a26924eeb1.png). There are three constants from the perspective of ![](../_resources/f8921b9df9c1fbe5ee7bdcc2344ac3ae.png): 3, 2, and *y*. Therefore, ![](../_resources/a1c2cf4878739bd0901f9d14a6eec797.png). The partial derivative with respect to *y* treats *x* like a constant: ![](../_resources/b8201b016cf429f08d434739f8d64207.png). It's a good idea to derive these yourself before continuing otherwise the rest of the article won't make sense. Here's the [Khan Academy video on partials](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives) if you need help.

To make it clear we are doing vector calculus and not just multivariate calculus, let's consider what we do with the partial derivatives ![](../_resources/c8e3e20507727ad809bde67552502de0.png) and ![](../_resources/41114bd00b536f601f2405b27cd1f100.png) (another way to say ![](../_resources/a38ae6d78bcaed3133fba8a46642d983.png) and ![](../_resources/da33a23d06dd5c75b788e820fba2c619.png)) that we computed for ![](../_resources/c6f753af6fd51a6925d03f704ed89b50.png). Instead of having them just floating around and not organized in any way, let's organize them into a horizontal vector. We call this vector the *gradient* of ![](../_resources/e143776bb936859a4513e9d9288478bb.png) and write it as:

![](../_resources/d843e7e29150e692075546bd95ecf278.png)

So the gradient of ![](../_resources/e143776bb936859a4513e9d9288478bb.png) is simply a vector of its partials. Gradients are part of the vector calculus world, which deals with functions that map *n* scalar parameters to a single scalar. Now, let's get crazy and consider derivatives of multiple functions simultaneously.

## Matrix calculus

When we move from derivatives of one function to derivatives of many functions, we move from the world of vector calculus to matrix calculus. Let's compute partial derivatives for two functions, both of which take two parameters. We can keep the same ![](../_resources/c6f753af6fd51a6925d03f704ed89b50.png) from the last section, but let's also bring in ![](../_resources/7974f3be325c435340d1b9145c2991f6.png). The gradient for *g* has two entries, a partial derivative for each parameter:

![](../_resources/82684e187274da4f3dbf027f276ba252.png)
and
![](../_resources/e7da325ef6d7b9e351046270a9e2e5b2.png)
giving us gradient ![](../_resources/4df43b683256cbe7671c11f05608f71f.png).

Gradient vectors organize all of the partial derivatives for a specific scalar function. If we have two functions, we can also organize their gradients into a matrix by stacking the gradients. When we do so, we get the *Jacobian matrix* (or just the *Jacobian*) where the gradients are rows:

![](../_resources/fa2b4584d59b96d21304842c37e09736.png)
Welcome to matrix calculus!

**Note that there are multiple ways to represent the Jacobian.** We are using the so-called [numerator layout](https://en.wikipedia.org/wiki/Matrix_calculus#Layout_conventions) but many papers and software will use the *denominator layout*. This is just transpose of the numerator layout Jacobian (flip it around its diagonal):

![](../_resources/fb8c488ad50990b3d433186a906bb60b.png)

### Generalization of the Jacobian

So far, we've looked at a specific example of a Jacobian matrix. To define the Jacobian matrix more generally, let's combine multiple parameters into a single vector argument: ![](../_resources/e64f2059e9c267f0f4da1aa713da07cf.png). (You will sometimes see notation ![](../_resources/3482eab950f4e0701ea0c5e5d1d62d29.png) for vectors in the literature as well.) Lowercase letters in bold font such as x are vectors and those in italics font like *x* are scalars. *xi* is the ![](../_resources/4ba2a94bc19244e873aa5df778c73170.png) element of vector x and is in italics because a single vector element is a scalar. We also have to define an orientation for vector x. We'll assume that all vectors are vertical by default of size ![](../_resources/a8c47612a968e265423c174e24e6e52f.png):

![](../_resources/652aa66188e7a98e6e10ba2368aec201.png)

With multiple scalar-valued functions, we can combine them all into a vector just like we did with the parameters. Let ![](../_resources/c372b733acc711e533a05bb39cfb0442.png) be a vector of *m* scalar-valued functions that each take a vector x of length ![](../_resources/a01e92ec1015dd6d6af62faa31d9ac9b.png) where ![](../_resources/a970da315f94909332f7a060678bb87d.png) is the cardinality (count) of elements in x. Each *fi* function within f returns a scalar just as in the previous section:

![](../_resources/ad8bb473cc8bfb077010f627d78fb9a0.png)

For instance, we'd represent ![](../_resources/c6f753af6fd51a6925d03f704ed89b50.png) and ![](../_resources/7974f3be325c435340d1b9145c2991f6.png) from the last section as

![](../_resources/58396dc65e9e05ffb5f42bc1d7a00a6b.png)

It's very often the case that ![](../_resources/a0eff4e23445de595b835050c915fef2.png) because we will have a scalar function result for each element of the x vector. For example, consider the identity function ![](../_resources/065bffa157d4a85665eb5f17e255985b.png):

![](../_resources/1c993041f5cfac33cdb7f63eddab46a4.png)

So we have ![](../_resources/a0eff4e23445de595b835050c915fef2.png) functions and parameters, in this case. Generally speaking, though, the Jacobian matrix is the collection of all ![](../_resources/e3b5313bcf68b163399236eed69780b6.png) possible partial derivatives (*m* rows and *n* columns), which is the stack of *m* gradients with respect to x:

![](../_resources/8cd6f06cae90c04f1cc0def42f116246.png)

Each ![](../_resources/aef5db581fc9fe9a79e76b3466c19dfb.png) is a horizontal *n*-vector because the partial derivative is with respect to a vector, x, whose length is ![](../_resources/a01e92ec1015dd6d6af62faa31d9ac9b.png). The width of the Jacobian is *n* if we're taking the partial derivative with respect to x because there are *n* parameters we can wiggle, each potentially changing the function's value. Therefore, the Jacobian is always *m* rows for *m* equations. It helps to think about the possible Jacobian shapes visually:

![](../_resources/6e4b83fdc4229a5046f722a708b0c0e4.png)

The Jacobian of the identity function ![](../_resources/c34a922603f2120fb614dc48eaf223d7.png), with ![](../_resources/8805bc8048c6adcea56553df09cfecb5.png), has *n* functions and each function has *n* parameters held in a single vector x. The Jacobian is, therefore, a square matrix since ![](../_resources/a0eff4e23445de595b835050c915fef2.png):

![](../_resources/15a97edea9ffafea830aa871bf9f3404.png)

Make sure that you can derive each step above before moving on. If you get stuck, just consider each element of the matrix in isolation and apply the usual scalar derivative rules. That is a generally useful trick: Reduce vector expressions down to a set of scalar expressions and then take all of the partials, combining the results appropriately into vectors and matrices at the end.

Also be careful to track whether a matrix is vertical, x, or horizontal, ![](../_resources/bc8289d9ec6d5039fb79c3b9ad8148bf.png) where ![](../_resources/bc8289d9ec6d5039fb79c3b9ad8148bf.png) means x transpose. Also make sure you pay attention to whether something is a scalar-valued function, ![](../_resources/fb650ac27063b47768e282bd60f5e443.png), or a vector of functions (or a vector-valued function), ![](../_resources/92ef59212e6160f191b60b8355c28885.png).

### Derivatives of vector element-wise binary operators

Element-wise binary operations on vectors, such as vector addition ![](../_resources/b3a633d62197e785a860e20bfe63b84f.png), are important because we can express many common vector operations, such as the multiplication of a vector by a scalar, as element-wise binary operations. By “element-wise binary operations” we simply mean applying an operator to the first item of each vector to get the first item of the output, then to the second items of the inputs for the second item of the output, and so forth. This is how all the basic math operators are applied by default in numpy or tensorflow, for example. Examples that often crop up in deep learning are ![](../_resources/fedcda10792f171aac4b146f99200aa1.png) and ![](../_resources/294a7dec4c998e1f3f8de0d3e1d96764.png) (returns a vector of ones and zeros).

We can generalize the element-wise binary operations with notation ![](../_resources/fe60f4f0c095f4f8f6e6f1ef525308bf.png) where ![](../_resources/862b33db7727cc63f5dda69876c94061.png). (Reminder: ![](../_resources/6533f94314a18ac171cfb9119c5e478f.png) is the number of items in *x*.) The ![](../_resources/fcf8c9ef80474ca36150c661ad56e679.png) symbol represents any element-wise operator (such as ![](../_resources/3e23221bee36e60e3ed09e8eefc3598e.png)) and not the ![](../_resources/d85f5746fd5db3e1ee6b7839621c1eb0.png) function composition operator. Here's what equation ![](../_resources/fe60f4f0c095f4f8f6e6f1ef525308bf.png) looks like when we zoom in to examine the scalar equations:

![](../_resources/465e26d90a9226b8d8e1ec7fe91351d0.png)

where we write *n* (not *m*) equations vertically to emphasize the fact that the result of element-wise operators give ![](../_resources/a0eff4e23445de595b835050c915fef2.png) sized vector results.

Using the ideas from the last section, we can see that the general case for the Jacobian with respect to w is the square matrix:

![](../_resources/98544cb968f7ae6130cb2102483ded36.png)
and the Jacobian with respect to x is:
![](../_resources/f168f1e2ea4b1245c299e43abd28b6c5.png)

That's quite a furball, but fortunately the Jacobian is very often a diagonal matrix, a matrix that is zero everywhere but the diagonal. Because this greatly simplifies the Jacobian, let's examine in detail when the Jacobian reduces to a diagonal matrix for element-wise operations.

In a diagonal Jacobian, all elements off the diagonal are zero, ![](../_resources/2ab08676b21aea81ab3138777901055c.png) where ![](../_resources/713e43bac69627865a0b30a43bf11f79.png). (Notice that we are taking the partial derivative with respect to *wj* not *wi*.) Under what conditions are those off-diagonal elements zero? Precisely when *fi* and *gi* are contants with respect to *wj*, ![](../_resources/15a8bbfc71a47376f08063139e9e4723.png). Regardless of the operator, if those partial derivatives go to zero, the operation goes to zero, ![](../_resources/968e6ddb2ccb67db56605acbc56ac0e9.png) no matter what, and the partial derivative of a constant is zero.

Those partials go to zero when *fi* and *gi* are not functions of *wj*. We know that element-wise operations imply that *fi* is purely a function of *wi* and *gi* is purely a function of *xi*. For example, ![](../_resources/b3a633d62197e785a860e20bfe63b84f.png) sums ![](../_resources/4e0678eba5d02eb73fd2dbdf9cbf37bb.png). Consequently, ![](../_resources/70b0b7c976045353981a96da60768548.png) reduces to ![](../_resources/6cef3520720402d54b7ab8f18ca9017d.png) and the goal becomes ![](../_resources/98d0cc9aa0758147faae8c664c126a8d.png). ![](../_resources/609e4104fb0d21722db1b91c52d1b854.png) and ![](../_resources/9a0d64a0131ddf6b5893a0aa7a6bd627.png) look like constants to the partial differentiation operator with respect to *wj* when ![](../_resources/713e43bac69627865a0b30a43bf11f79.png) so the partials are zero off the diagonal. (Notation ![](../_resources/609e4104fb0d21722db1b91c52d1b854.png) is technically an abuse of our notation because *fi* and *gi* are functions of vectors not individual elements. We should really write something like ![](../_resources/6594b76cbb300f15250086d09f3d7ab7.png), but that would muddy the equations further, and programmers are comfortable overloading functions, so we'll proceed with the notation anyway.)

We'll take advantage of this simplification later and refer to the constraint that ![](../_resources/5ba812c2a6d182b4c6667aa959f4aa21.png) and ![](../_resources/715d5b410ce1db128a96fcd0ad02f518.png) access at most *wi* and *xi*, respectively, as the *element-wise diagonal condition*.

Under this condition, the elements along the diagonal of the Jacobian are ![](../_resources/65edd72d8017c9253daa4efd73817daa.png):

![](../_resources/c17503c6c2ccff49926c351d790a9d16.png)
(The large “0”s are a shorthand indicating all of the off-diagonal are 0.)
More succinctly, we can write:
![](../_resources/4638bc11daa30516fa3b1d26a727ec1c.png)
and
![](../_resources/ae29564f5869a7966061e43f460a8aaa.png)

where ![](../_resources/519719d40505395dd8843516f8a402e2.png) constructs a matrix whose diagonal elements are taken from vector x.

Because we do lots of simple vector arithmetic, the general function ![](../_resources/48862f6bf2935a07c159bed7ce06a359.png) in the binary element-wise operation is often just the vector w. Any time the general function is a vector, we know that ![](../_resources/5ba812c2a6d182b4c6667aa959f4aa21.png) reduces to ![](../_resources/914452d6abf3d966f689ba264e98a1e0.png). For example, vector addition ![](../_resources/b3a633d62197e785a860e20bfe63b84f.png) fits our element-wise diagonal condition because ![](../_resources/94ab9bdc3a4f1259df2a89a90939a1b1.png) has scalar equations ![](../_resources/d7f673437e081c875f65619158324b7d.png) that reduce to just ![](../_resources/a996fd60ed889c7d0ceef0aaca7e0a24.png) with partial derivatives:

![](../_resources/23c4b155a8f50325f0dc9fe211b740e0.png)
![](../_resources/73c472e5e2db5f187f4cd7fc978d8f7d.png)

That gives us ![](../_resources/b4817af29654d205bdb09d9c1296cdfe.png), the identity matrix, because every element along the diagonal is 1. *I* represents the square identity matrix of appropriate dimensions that is zero everywhere but the diagonal, which contains all ones.

Given the simplicity of this special case, ![](../_resources/5ba812c2a6d182b4c6667aa959f4aa21.png) reducing to ![](../_resources/609e4104fb0d21722db1b91c52d1b854.png), you should be able to derive the Jacobians for the common element-wise binary operations on vectors:

![](:/b02123baca3749c648f39ca8593abe0c)
![](../_resources/98ba7c6698f312729733e8e51a0027c5.png)

The ![](../_resources/a4a688d99911db43b57bd8844a863bec.png) and ![](../_resources/f924fa4e8215494582cf8e7a397600ee.png) operators are element-wise multiplication and division; ![](../_resources/a4a688d99911db43b57bd8844a863bec.png) is sometimes called the *Hadamard product*. There isn't a standard notation for element-wise multiplication and division so we're using an approach consistent with our general binary operation notation.

### Derivatives involving scalar expansion

When we multiply or add scalars to vectors, we're implicitly expanding the scalar to a vector and then performing an element-wise binary operation. For example, adding scalar *z* to vector x, ![](../_resources/86e5a039fd68deede5cb8c5a3285e6e8.png), is really ![](../_resources/795455b858abfe67cc64eabae25a0376.png) where ![](../_resources/c34a922603f2120fb614dc48eaf223d7.png) and ![](../_resources/99f9310534639561603e7b09243f2ef7.png). (The notation ![](../_resources/f20ed389800745b4a7725c76833389c7.png) represents a vector of ones of appropriate length.) *z* is any scalar that doesn't depend on x, which is useful because then ![](../_resources/319679c228199e2a8e62e4718005d6b9.png) for any *xi* and that will simplify our partial derivative computations. (It's okay to think of variable *z* as a constant for our discussion here.) Similarly, multiplying by a scalar, ![](../_resources/8e7bf69fc86a690c97329a7964f78b65.png), is really ![](../_resources/5f8117cdc649a684f98f4dc6fbe3f5e3.png) where ![](../_resources/a4a688d99911db43b57bd8844a863bec.png) is the element-wise multiplication (Hadamard product) of the two vectors.

The partial derivatives of vector-scalar addition and multiplication with respect to vector x use our element-wise rule:

![](../_resources/016282b4685d9d4121b1a3ec40851a4a.png)

This follows because functions ![](../_resources/c34a922603f2120fb614dc48eaf223d7.png) and ![](../_resources/99f9310534639561603e7b09243f2ef7.png) clearly satisfy our element-wise diagonal condition for the Jacobian (that ![](../_resources/b02d765439e543c0f3b19198c7c2a779.png) refer at most to *xi* and ![](../_resources/ba2d62bdacbf4ce479471dc6701eb9c8.png) refers to the ![](../_resources/4ba2a94bc19244e873aa5df778c73170.png) value of the ![](../_resources/27a3d6f4acaed5c8e6b6594f7f20dea8.png) vector).

Using the usual rules for scalar partial derivatives, we arrive at the following diagonal elements of the Jacobian for vector-scalar addition:

![](../_resources/bdba36f2da6fef898ad647dfcec9b7c2.png)
So, ![](../_resources/d848f73ef234068eb66a5d935dbf0ab3.png).

Computing the partial derivative with respect to the scalar parameter *z*, however, results in a vertical vector, not a diagonal matrix. The elements of the vector are:

![](../_resources/9f16dd7e215d463a65a055d3fd1049cf.png)
Therefore, ![](../_resources/63c95ac408b4b8085a9be6c266fc5274.png).

The diagonal elements of the Jacobian for vector-scalar multiplication involve the product rule for scalar derivatives:

![](../_resources/d4cfa89bc0904a1bb94e06a06cc1a9ae.png)
So, ![](../_resources/28a870b528375b00b247e85a1468e874.png).

The partial derivative with respect to scalar parameter *z* is a vertical vector whose elements are:

![](../_resources/06e1d37daa58594e2bf622f1d1db2781.png)
This gives us ![](../_resources/936ef1393b19fd3aefac4dda49585fe9.png).

### Vector sum reduction

Summing up the elements of a vector is an important operation in deep learning, such as the network loss function, but we can also use it as a way to simplify computing the derivative of vector dot product and other operations that reduce vectors to scalars.

Let ![](../_resources/092285f24daf54fbc097098fffb7bed8.png). Notice we were careful here to leave the parameter as a vector x because each function *fi* could use all values in the vector, not just *xi*. The sum is over the **results** of the function and not the parameter. The gradient (![](../_resources/76fef36e19ae4baba1c7148d33bca0f5.png) Jacobian) of vector summation is:

![](../_resources/f874b6b2211ae646b4b5b23be8fa97b5.png)

(The summation inside the gradient elements can be tricky so make sure to keep your notation consistent.)

Let's look at the gradient of the simple ![](../_resources/ecb8a68cd33d978ae02c497c7c8c3d79.png). The function inside the summation is just ![](../_resources/8805bc8048c6adcea56553df09cfecb5.png) and the gradient is then:

![](../_resources/1dd1a85eca08e0df8c84b6495c6d39c5.png)

Because ![](../_resources/d03b32ab3e6b9639ed4951a254af5830.png) for ![](../_resources/713e43bac69627865a0b30a43bf11f79.png), we can simplify to:

![](../_resources/9cbe3bcebadc72187030c60a6a0b0c2d.png)

Notice that the result is a horizontal vector full of 1s, not a vertical vector, and so the gradient is ![](../_resources/4aac007050787131e09d9b5c9f35a1f0.png). (The *T* exponent of ![](../_resources/4aac007050787131e09d9b5c9f35a1f0.png) represents the transpose of the indicated vector. In this case, it flips a vertical vector to a horizontal vector.) It's very important to keep the shape of all of your vectors and matrices in order otherwise it's impossible to compute the derivatives of complex functions.

As another example, let's sum the result of multiplying a vector by a constant scalar. If ![](../_resources/f31d1f3a129df4eefda914c8af5fd1bd.png) then ![](../_resources/1006eb8642cd9dc45c6810276ef3249e.png). The gradient is:

![](../_resources/3db0c5096b076ecb6a9a73d75593af25.png)

The derivative with respect to scalar variable *z* is ![](../_resources/a625001bab9541459fc55d432713b4da.png):

![](../_resources/1bced80ae5489fb7187d397ace52fdd3.png)

### The Chain Rules

We can't compute partial derivatives of very complicated functions using just the basic matrix calculus rules we've seen so far. For example, we can't take the derivative of nested expressions like ![](../_resources/0ab32df17f4c38639b0532430d03ca3d.png) directly without reducing it to its scalar equivalent. We need to be able to combine our basic vector rules using what we can call the *vector chain rule*. Unfortunately, there are a number of rules for differentiation that fall under the name “chain rule” so we have to be careful which chain rule we're talking about. Part of our goal here is to clearly define and name three different chain rules and indicate in which situation they are appropriate. To get warmed up, we'll start with what we'll call the *single-variable chain rule*, where we want the derivative of a scalar function with respect to a scalar. Then we'll move on to an important concept called the *total derivative* and use it to define what we'll pedantically call the *single-variable total-derivative chain rule*. Then, we'll be ready for the vector chain rule in its full glory as needed for neural networks.

The chain rule is conceptually a divide and conquer strategy (like Quicksort) that breaks complicated expressions into subexpressions whose derivatives are easier to compute. Its power derives from the fact that we can process each simple subexpression in isolation yet still combine the intermediate results to get the correct overall result.

The chain rule comes into play when we need the derivative of an expression composed of nested subexpressions. For example, we need the chain rule when confronted with expressions like ![](../_resources/837acd73bb2be512c6656d960154577d.png). The outermost expression takes the *sin* of an intermediate result, a nested subexpression that squares *x*. Specifically, we need the single-variable chain rule, so let's start by digging into that in more detail.

#### Single-variable chain rule

Let's start with the solution to the derivative of our nested expression: ![](../_resources/1c648c1f45d0de8d51814b72c751a6a6.png). It doesn't take a mathematical genius to recognize components of the solution that smack of scalar differentiation rules, ![](../_resources/c3c90caf288b54d1b65737e4adeecf36.png) and ![](../_resources/2477f157389019c446278b75a1ddc73a.png). It looks like the solution is to multiply the derivative of the outer expression by the derivative of the inner expression or “chain the pieces together,” which is exactly right. In this section, we'll explore the general principle at work and provide a process that works for highly-nested expressions of a single variable.

Chain rules are typically defined in terms of nested functions, such as ![](../_resources/3656539465b674074604f1e8705400ae.png) for single-variable chain rules. (You will also see the chain rule defined using function composition ![](../_resources/97a12dfc9b29de20a829b0fc8c77573c.png), which is the same thing.) Some sources write the derivative using shorthand notation ![](../_resources/2c4b6e24ca5501ece76c164b8c56d242.png), but that hides the fact that we are introducing an intermediate variable: ![](../_resources/d6731fd596fa4458c994be40d089f354.png), which we'll see shortly. It's better to define the [single-variable chain rule](http://m.wolframalpha.com/input/?i=chain+rule) of ![](../_resources/290dfbaf469a3c91598c5fbfe6a7a62f.png) explicitly so we never take the derivative with respect to the wrong variable. Here is the formulation of the single-variable chain rule we recommend:

![](../_resources/1926b5c7d83fe87e1eb279adebd2333c.png)
To deploy the single-variable chain rule, follow these steps:

1. Introduce intermediate variables for nested subexpressions and subexpressions for both binary and unary operators; e.g., ![](../_resources/0f4cd95ef3fc7fde400484e0feebc890.png) is binary, ![](../_resources/fd68bd97760af0a72d2efceeecb31dea.png) and other trigonometric functions are usually unary because there is a single operand. This step normalizes all equations to single operators or function applications.

2. Compute derivatives of the intermediate variables with respect to their parameters.

3. Combine all derivatives of intermediate variables by multiplying them together to get the overall result.

4. Substitute intermediate variables back in if any are referenced in the derivative equation.

The third step puts the “chain” in “chain rule” because it chains together intermediate results. Multiplying the intermediate derivatives together is the common theme among all variations of the chain rule.

Let's try this process on ![](../_resources/778441dffd5a9cd607a77a65edd7f09b.png):

1. Introduce intermediate variables. Let ![](../_resources/d769d9c23bb5db8745f90214e57c7f6b.png) represent subexpression ![](../_resources/fb3b40bf0d82a8aea24915c687231648.png) (shorthand for ![](../_resources/df13ddbe67d8253c6eae51769703f57a.png)). This gives us:

![](../_resources/722b00131ac76493327fd08045f6cbe7.png)

The order of these subexpressions does not affect the answer, but we recommend working in the reverse order of operations dictated by the nesting (innermost to outermost). That way, expressions and derivatives are always functions of previously-computed elements.

2. Compute derivatives.![](../_resources/ddd1ef7dc246b679e3a11cf6fd6bca0f.png)
3. Combine.![](../_resources/0f1c8992b4d47c27f23502665d6e3230.png)
4. Substitute.![](../_resources/8be4097815422742dc11daad0b6db867.png)

Notice how easy it is to compute the derivatives of the intermediate variables in isolation! The chain rule says it's legal to do that and tells us how to combine the intermediate results to get ![](../_resources/2c8fa6a6f7d7e06736e8194e7f6e5cf3.png).

You can think of the combining step of the chain rule in terms of units canceling. If we let *y* be miles, *x* be the gallons in a gas tank, and *u* as gallons we can interpret ![](../_resources/6b574259649c758c3738c6ac8cd193b9.png) as ![](../_resources/f9b3ce30d67bb097a1373059a6b93cdf.png). The *gallon* denominator and numerator cancel.

Another way to to think about the single-variable chain rule is to visualize the overall expression as a dataflow diagram or chain of operations (or [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) for compiler people):

![](../_resources/a35aae1decef7ad6559258ec439e0905.png)

Changes to function parameter *x* bubble up through a squaring operation then through a *sin* operation to change result *y*. You can think of ![](../_resources/f578a5750e63d535ff38fd9f10381f97.png) as “getting changes from *x* to *u*” and ![](../_resources/ace04340a1b98691415048201e795f45.png) as “getting changes from *u* to *y*.” Getting from *x* to *y* requires an intermediate hop. The chain rule is, by convention, usually written from the output variable down to the parameter(s), ![](../_resources/6b574259649c758c3738c6ac8cd193b9.png). But, the *x*-to-*y* perspective would be more clear if we reversed the flow and used the equivalent ![](../_resources/876d6d4b0ff61f0ffc8e722ed93c25a1.png).

**Conditions under which the single-variable chain rule applies**. Notice that there is a single dataflow path from *x* to the root *y*. Changes in *x* can influence output *y* in only one way. That is the condition under which we can apply the single-variable chain rule. An easier condition to remember, though one that's a bit looser, is that none of the intermediate subexpression functions, ![](../_resources/70ea8052dfbeac5a4346ad3195449d82.png) and ![](../_resources/d1185189263109d146694b344d08138e.png), have more than one parameter. Consider ![](../_resources/df083eebc5ac0a553d93b2bc41f55f46.png), which would become ![](../_resources/8dacadaed4dbd3ab532b526936ed58d3.png) after introducing intermediate variable *u*. As we'll see in the next section, ![](../_resources/2dd35fdd4f91bf2d957877a4e966137e.png) has multiple paths from *x* to *y*. To handle that situation, we'll deploy the single-variable total-derivative chain rule.

As an aside for those interested in automatic differentiation, papers and library documentation use terminology *forward differentiation* and *backward differentiation* (for use in the back-propagation algorithm). From a dataflow perspective, we are computing a forward differentiation because it follows the normal data flow direction. Backward differentiation, naturally, goes the other direction and we're asking how a change in the output would affect function parameter *x*. Because backward differentiation can determine changes in all function parameters at once, it turns out to be much more efficient for computing the derivative of functions with lots of parameters. Forward differentiation, on the other hand, must consider how a change in each parameter, in turn, affects the function output *y*. The following table emphasizes the order in which partial derivatives are computed for the two techniques.

| Forward differentiation from *x* to *y* | Backward differentiation from *y* to *x* |
| --- | --- |
| ![](../_resources/876d6d4b0ff61f0ffc8e722ed93c25a1.png) | ![](../_resources/6b574259649c758c3738c6ac8cd193b9.png) |

Automatic differentiation is beyond the scope of this article, but we're setting the stage for a future article.

Many readers can solve ![](../_resources/837acd73bb2be512c6656d960154577d.png) in their heads, but our goal is a process that will work even for very complicated expressions. This process is also how [automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation) works in libraries like PyTorch. So, by solving derivatives manually in this way, you're also learning how to define functions for custom neural networks in PyTorch.

With deeply nested expressions, it helps to think about deploying the chain rule the way a compiler unravels nested function calls like ![](../_resources/89a52261501caf59de1fbfbcf0b155ef.png) into a sequence (chain) of calls. The result of calling function *fi* is saved to a temporary variable called a register, which is then passed as a parameter to ![](../_resources/46b1f9b27db49dd7e0baf6cca0570a4b.png). Let's see how that looks in practice by using our process on a highly-nested equation like ![](../_resources/1ced984b40faa8aebc1da1c1bc076f78.png):

1. Introduce intermediate variables.![](../_resources/210407124eb0f0de2138ad71799af978.png)
2.  Compute derivatives.![](../_resources/d238674db8d9e43e8e5cf30ad22ea772.png)
3.  Combine four intermediate values.![](../_resources/354b75b48721ca3337a646b5045fd99b.png)
4.  Substitute.![](../_resources/198f6bf31e7f20a5ca7a624912bfa3e0.png)

Here is a visualization of the data flow through the chain of operations from *x* to *y*:

![chain-tree.png](../_resources/36644e57431ae3b827e14f14b74d0cbb.png)

At this point, we can handle derivatives of nested expressions of a single variable, *x*, using the chain rule but only if *x* can affect *y* through a single data flow path. To handle more complicated expressions, we need to extend our technique, which we'll do next.

#### Single-variable total-derivative chain rule

Our single-variable chain rule has limited applicability because all intermediate variables must be functions of single variables. But, it demonstrates the core mechanism of the chain rule, that of multiplying out all derivatives of intermediate subexpressions. To handle more general expressions such as ![](../_resources/8ca9075ee336121f1e0c6d447e58d8ab.png), however, we need to augment that basic chain rule.

Of course, we immediately see ![](../_resources/67ef15d337136bc3340bfa4db388ea52.png), but that is using the scalar addition derivative rule, not the chain rule. If we tried to apply the single-variable chain rule, we'd get the wrong answer. In fact, the previous chain rule is meaningless in this case because derivative operator ![](../_resources/caf33477654033ee4aea2f929cba7a07.png) does not apply to multivariate functions, such as ![](../_resources/10d1306f9dc999dd075084cbadda39f2.png) among our intermediate variables:

![](../_resources/c973416837e0b7a510b5894632cbbf11.png)

Let's try it anyway to see what happens. If we pretend that ![](../_resources/771e398f52d891d0e17a306b894c02cf.png) and ![](../_resources/e49c4a69a2a11c99d9d9092d3cabe571.png), then ![](../_resources/10416d3d4861c87ee1aec8af5e215cad.png) instead of the right answer ![](../_resources/2c5b6275c68dd8c7ce7b459b3e0724be.png).

Because ![](../_resources/70cc5e10472e5e365bdbec86e59aff23.png) has multiple parameters, partial derivatives come into play. Let's blindly apply the partial derivative operator to all of our equations and see what we get:

![](../_resources/462102268da52ade2fc2fa8a9297e5fa.png)

Ooops! The partial ![](../_resources/fc54ce39661907099dead943e12e46b2.png) is wrong because it violates a key assumption for partial derivatives. When taking the partial derivative with respect to *x*, the other variables must not vary as *x* varies. Otherwise, we could not act as if the other variables were constants. Clearly, though, ![](../_resources/e666e0b449672f73687bc57540a9a46f.png) is a function of *x* and therefore varies with *x*. ![](../_resources/8f6b716e8e2a05701376170816eb0ae4.png) because ![](../_resources/63dfe271e66520119c216ffa3e88a062.png). A quick look at the data flow diagram for ![](../_resources/8e73a1f1eaf622b47305e38c86a821f4.png) shows multiple paths from *x* to *y*, thus, making it clear we need to consider direct and indirect (through ![](../_resources/a25532ddb0cf6dde13e06e02e12ab3fb.png)) dependencies on *x*:

![](../_resources/59196460df77841f0883f6a770658377.png)

A change in *x* affects *y* both as an operand of the addition and as the operand of the square operator. Here's an equation that describes how tweaks to *x* affect the output:

![](../_resources/9ad6cd83573d315dedc3f15abbb85c40.png)

Then, ![](../_resources/05cb873b4ace0afc07b248ed32e9a2fe.png), which we can read as “the change in *y* is the difference between the original *y* and *y* at a tweaked *x*.”

If we let ![](../_resources/b4925767ad4069a22e4e7217de5b4ee0.png), then ![](../_resources/8d3af6649beff0a37f5b60630ba4ba3e.png). If we bump *x* by 1, ![](../_resources/8cdff374593901a952e3a5c9ba953108.png), then ![](../_resources/540f30e957db541c34875643fc061cff.png). The change in *y* is not ![](../_resources/3ff78088a8f895d7a9a0689377c4d1bf.png), as ![](../_resources/00f83f51d0ff09ad044f8e8cd7d48b16.png) would lead us to believe, but ![](../_resources/802a797b5d436930af9d73bfa6b231a1.png)!

Enter the “law” of [total derivatives](https://en.wikipedia.org/wiki/Total_derivative), which basically says that to compute ![](../_resources/a62929911bc01059dfba952972943ce7.png), we need to sum up all possible contributions from changes in *x* to the change in *y*. The total derivative with respect to *x* assumes all variables, such as ![](../_resources/bff66ce7e7c315b5421ba31ab9ef165d.png) in this case, are functions of *x* and potentially vary as *x* varies. The total derivative of ![](../_resources/5f407f1e8a63f0af3abd50f8724ed024.png) that depends on *x* directly and indirectly via intermediate variable ![](../_resources/a25532ddb0cf6dde13e06e02e12ab3fb.png) is given by:

![](../_resources/63925d3e42fd9197eb589f76d6b00b62.png)
Using this formula, we get the proper answer:
![](../_resources/1bb91b8bd3139b0003d1fad582872a2f.png)

That is an application of what we can call the *single-variable total-derivative chain rule*:

![](../_resources/00d95d4500626831aeb59b5f1038966e.png)

The total derivative assumes all variables are potentially codependent whereas the partial derivative assumes all variables but *x* are constants.

There is something subtle going on here with the notation. All of the derivatives are shown as partial derivatives because *f* and *ui* are functions of multiple variables. This notation mirrors that of [MathWorld's notation](http://mathworld.wolfram.com/TotalDerivative.html) but differs from [Wikipedia](https://en.wikipedia.org/wiki/Total_derivative), which uses ![](../_resources/31881fe65193b535ac8aa63d2d0dbd90.png) instead (possibly to emphasize the total derivative nature of the equation). We'll stick with the partial derivative notation so that it's consistent with our discussion of the vector chain rule in the next section.

In practice, just keep in mind that when you take the total derivative with respect to *x*, other variables might also be functions of *x* so add in their contributions as well. The left side of the equation looks like a typical partial derivative but the right-hand side is actually the total derivative. It's common, however, that many temporary variables are functions of a single parameter, which means that the single-variable total-derivative chain rule degenerates to the single-variable chain rule.

Let's look at a nested subexpression, such as ![](../_resources/bbe3308aef95c496ab61359f0d7789ec.png). We introduce three intermediate variables:

![](../_resources/24c63413b6378222b0c39ce4a1155480.png)
and partials:
![](../_resources/80247edc5d0bdbc03dab32a9917d94bc.png)

where both ![](../_resources/b70225d6e4b585b16d0f7fdd9ba6aae6.png) and ![](../_resources/42afd2bc877635a8d50d31949a54f3fc.png) have ![](../_resources/6ef28a7e2f40a6c86d3031e83de6430b.png) terms that take into account the total derivative.

Also notice that the total derivative formula always **sums** versus, say, multiplies terms ![](../_resources/78263485b9465316b84caf11fc1cbd0a.png). It's tempting to think that summing up terms in the derivative makes sense because, for example, ![](../_resources/8b966aea39d479bfaa5653e0eadc4ceb.png) adds two terms. Nope. The total derivative is adding terms because it represents a weighted sum of all *x* contributions to the change in *y*. For example, given ![](../_resources/8d3f8cf2d4f5a331a597899bb57c41e0.png) instead of ![](../_resources/8b966aea39d479bfaa5653e0eadc4ceb.png), the total-derivative chain rule formula still adds partial derivative terms. (![](../_resources/381915e14541e21f523585048bac046d.png) simplifies to ![](../_resources/45d65346b50345fbd7d65a58cc692bf4.png) but for this demonstration, let's not combine the terms.) Here are the intermediate variables and partial derivatives:

![](../_resources/eba9acd4f88405546e37178cf7e531e3.png)
The form of the total derivative remains the same, however:
![](../_resources/df67b5e36886bb8cc99e467f9685b73a.png)

It's the partials (weights) that change, not the formula, when the intermediate variable operators change.

Those readers with a strong calculus background might wonder why we aggressively introduce intermediate variables even for the non-nested subexpressions such as ![](../_resources/fb3b40bf0d82a8aea24915c687231648.png) in ![](../_resources/071d5a3aa4a8c07d2dc59cd1d7d1e148.png). We use this process for three reasons: (i) computing the derivatives for the simplified subexpressions is usually trivial, (ii) we can simplify the chain rule, and (iii) the process mirrors how automatic differentiation works in neural network libraries.

Using the intermediate variables even more aggressively, let's see how we can simplify our single-variable total-derivative chain rule to its final form. The goal is to get rid of the ![](../_resources/99b129411f3c4c2761a2522f246ac1ca.png) sticking out on the front like a sore thumb:

![](../_resources/fffdf01205964f5660975d163e4718b5.png)

We can achieve that by simply introducing a new temporary variable as an alias for *x*: ![](../_resources/7f9fc4eb03e74630fbfa6cfb19b64da6.png). Then, the formula reduces to our final form:

![](../_resources/8c3161b2894158387179eb4f3080dda8.png)

This chain rule that takes into consideration the total derivative degenerates to the single-variable chain rule when all intermediate variables are functions of a single variable. Consequently, you can remember this more general formula to cover both cases. As a bit of dramatic foreshadowing, notice that the summation sure looks like a vector dot product, ![](../_resources/54dd96bf7c1d4a855066493b798ecf52.png), or a vector multiply ![](../_resources/dd04678d6d6f10e6f01672cba92b8200.png).

Before we move on, a word of caution about terminology on the web. Unfortunately, the chain rule given in this section, based upon the total derivative, is universally called “multivariable chain rule” in calculus discussions, which is highly misleading! Only the intermediate variables are multivariate functions. The overall function, say, ![](../_resources/55c53b2ac08cac98a1690087ba2f6074.png), is a scalar function that accepts a single parameter *x*. The derivative and parameter are scalars, not vectors, as one would expect with a so-called multivariate chain rule. (Within the context of a non-matrix calculus class, “multivariate chain rule” is likely unambiguous.) To reduce confusion, we use “single-variable total-derivative chain rule” to spell out the distinguishing feature between the simple single-variable chain rule, ![](../_resources/6b574259649c758c3738c6ac8cd193b9.png), and this one.

#### Vector chain rule

Now that we've got a good handle on the total-derivative chain rule, we're ready to tackle the chain rule for vectors of functions and vector variables. Surprisingly, this more general chain rule is just as simple looking as the single-variable chain rule for scalars. Rather than just presenting the vector chain rule, let's rediscover it ourselves so we get a firm grip on it. We can start by computing the derivative of a sample vector function with respect to a scalar, ![](../_resources/8cb8af993f6e713f006e4c759faf1e43.png), to see if we can abstract a general formula.

![](../_resources/58a9711fc3c44e7bc3767d3aad8dad97.png)

Let's introduce two intermediate variables, ![](../_resources/934f23685b08f9575857ee1eec3ebfc3.png) and ![](../_resources/f08b53bcf58162fd090a95753ca2727c.png), one for each *fi* so that *y* looks more like ![](../_resources/98ecd5a9e89e26a8f2aab53d6dd76941.png):

![](../_resources/7174a7d30864322b001a34f6b142edda.png)
![](../_resources/bada9591dcd03a4e55edcb568921faef.png)

The derivative of vector y with respect to scalar *x* is a vertical vector with elements computed using the single-variable total-derivative chain rule:

![](../_resources/fc357f2b2153743629711c1d2d944cc8.png)

Ok, so now we have the answer using just the scalar rules, albeit with the derivatives grouped into a vector. Let's try to abstract from that result what it looks like in vector form. The goal is to convert the following vector of scalar operations to a vector operation.

![](../_resources/2c06f896e6d09fdcd5873b279d09c191.png)

If we split the ![](../_resources/31052e8938a9e1a9d358814d5cc93506.png) terms, isolating the ![](../_resources/56924740565b3b39d3ea8509fa123b54.png) terms into a vector, we get a matrix by vector multiplication:

![](../_resources/02f3f3a80e42903cbf7fc5eab593f9aa.png)

That means that the Jacobian is the multiplication of two other Jacobians, which is kinda cool. Let's check our results:

![](../_resources/ee64fd11fc22d58bde4cbc397c052185.png)

Whew! We get the same answer as the scalar approach. This vector chain rule for vectors of functions and a single parameter appears to be correct and, indeed, mirrors the single-variable chain rule. Compare the vector rule:

![](../_resources/a4a76236b07938a9756fd3bdd83dd432.png)
with the single-variable chain rule:
![](../_resources/344104f9f4a7d19b57cf16e05b2275f4.png)

To make this formula work for multiple parameters or vector x, we just have to change *x* to vector x in the equation. The effect is that ![](../_resources/7c2878e653bb1a848da2897e6a99c9a7.png) and the resulting Jacobian, ![](../_resources/2875658466c2855441b7cc1a649ee17e.png), are now matrices instead of vertical vectors. Our complete *vector chain rule* is:

![](../_resources/243d5633bcbb808aa1ac9f98092ef33c.png)

The beauty of the vector formula over the single-variable chain rule is that it automatically takes into consideration the total derivative while maintaining the same notational simplicity. The Jacobian contains all possible combinations of *fi* with respect to *gj* and *gi* with respect to *xj*. For completeness, here are the two Jacobian components in their full glory:

![](../_resources/4ac94e3f2b6baa7c4bba4a0f8019094f.png)

where ![](../_resources/9263a13b82c62416901d8be43a5904c1.png), ![](../_resources/faa0ee63f59e7f18a524b6a971931a6f.png), and ![](../_resources/1cdda47c6199098c8d5a124326302807.png). The resulting Jacobian is  (an  matrix multiplied by a  matrix).

Even within this  formula, we can simplify further because, for many applications, the Jacobians are square () and the off-diagonal entries are zero. It is the nature of neural networks that the associated mathematics deals with functions of vectors not vectors of functions. For example, the neuron affine function has term  and the activation function is ; we'll consider derivatives of these functions in the next section.

As we saw in a previous section, element-wise operations on vectors w and x yield diagonal matrices with elements  because *wi* is a function purely of *xi* but not *xj* for . The same thing happens here when *fi* is purely a function of *gi* and *gi* is purely a function of *xi*:

![](../_resources/71faa3032f3097b5b941d1e08363d84b.png)
![](../_resources/d8a3419a68c081c6fbbca0df6a12c118.png)
In this situation, the vector chain rule simplifies to:
![](../_resources/d715206813c01a8fb1b2d0aaf7dda03a.png)

Therefore, the Jacobian reduces to a diagonal matrix whose elements are the single-variable chain rule values.

After slogging through all of that mathematics, here's the payoff. All you need is the vector chain rule because the single-variable formulas are special cases of the vector chain rule. The following table summarizes the appropriate components to multiply in order to get the Jacobian.

![](../_resources/4b47a26cb1ad671e0544aa7da59ece3f.png)

## The gradient of neuron activation

We now have all of the pieces needed to compute the derivative of a typical neuron activation for a single neural network computation unit with respect to the model parameters, w and *b*:

![](../_resources/1a64cc160581aa78201bd411f9cf8a66.png)

(This represents a neuron with fully connected weights and rectified linear unit activation. There are, however, other affine functions such as convolution and other activation functions, such as exponential linear units, that follow similar logic.)

Let's worry about *max* later and focus on computing ![](../_resources/39fad54a186a16fb45ee632b4f69e55d.png) and . (Recall that neural networks learn through optimization of their weights and biases.) We haven't discussed the derivative of the dot product yet, ![](../_resources/c6d07fee7cc68f54a1e99351d6e2be05.png), but we can use the chain rule to avoid having to memorize yet another rule. (Note notation *y* not y as the result is a scalar not a vector.)

The dot product  is just the summation of the element-wise multiplication of the elements: ![](../_resources/0fe27a01e81fe1e225db9b1ea9d9e264.png). (You might also find it useful to remember the linear algebra notation .) We know how to compute the partial derivatives of  and  but haven't looked at partial derivatives for . We need the chain rule for that and so we can introduce an intermediate vector variable u just as we did using the single-variable chain rule:

![](../_resources/80a29139bd4b42b6f07a864112d88f62.png)

Once we've rephrased *y*, we recognize two subexpressions for which we already know the partial derivatives:

![](../_resources/63285a0c8439e75f2291c1b63890d942.png)
The vector chain rule says to multiply the partials:
![](../_resources/391ae0b1804b4d17f0529d645fdb5fa1.png)

To check our results, we can grind the dot product down into a pure scalar function:

![](../_resources/6014bd2af6f765f50f5f94ec8a4e5fcc.png)
Then:
![](../_resources/e5e97b16e8ecf7c1d5e2ad7c8361d66b.png)
Hooray! Our scalar results match the vector chain rule results.

Now, let , the full expression within the *max* activation function call. We have two different partials to compute, but we don't need the chain rule:

![](../_resources/341d9875a44350a9515783b27cd22fdf.png)

Let's tackle the partials of the neuron activation, ![](../_resources/ad393261f5ce3d5449cbf4449ad6720e.png). The use of the  function call on scalar *z* just says to treat all negative *z* values as 0. The derivative of the max function is a piecewise function. When , the derivative is 0 because *z* is a constant. When , the derivative of the max function is just the derivative of *z*, which is :

![](../_resources/1cd949071a9a710bcea1dbf1efbcd899.png)

An aside on broadcasting functions across scalars. When one or both of the *max* arguments are vectors, such as , we broadcast the single-variable function *max* across the elements. This is an example of an element-wise unary operator. Just to be clear:

![](../_resources/88d46ecc15f82ddd0a874c1fef74b352.png)

For the derivative of the broadcast version then, we get a vector of zeros and ones where:

![](../_resources/b3c67e2423eadb5d01fa55ab5d103207.png)
![](../_resources/abf403ed5a1d1c54de4911a656e4ea1b.png)

To get the derivative of the ![](../_resources/b50490e4874b77c88ed7ea207840f33a.png) function, we need the chain rule because of the nested subexpression, . Following our process, let's introduce intermediate scalar variable *z* to represent the affine function giving:

![](../_resources/a8d601a987a9fb1eae573ee5a2f56832.png)
![](../_resources/2bdcbff723651a01ff51a569a0be84cd.png)
The vector chain rule tells us:
![](../_resources/8370327522211540bb4337c6ccfb4df6.png)
which we can rewrite as follows:
![](../_resources/27a832b6b23f4bc76c5d981ee1c4e621.png)
and then substitute  back in:
![](../_resources/d5122a3d38a2b1b0d785df3720ebb431.png)

That equation matches our intuition. When the activation function clips affine function output *z* to 0, the derivative is zero with respect to any weight *wi*. When , it's as if the *max* function disappears and we get just the derivative of *z* with respect to the weights.

Turning now to the derivative of the neuron activation with respect to *b*, we get:

Let's use these partial derivatives now to handle the entire loss function.

## The gradient of the neural network loss function

Training a neuron requires that we take the derivative of our loss or “cost” function with respect to the parameters of our model, w and *b*. Because we train with multiple vector inputs (e.g., multiple images) and scalar targets (e.g., one classification per image), we need some more notation. Let

![](../_resources/3bce0fb46f7eb2fc56932b796a0eacdf.png)
where , and then let
![](../_resources/af0eea56132f88fb29088d40df00c956.png)
where *yi* is a scalar. Then the cost equation becomes:
![](../_resources/7373182b9d6d89c9ddd1d7770a2171c8.png)
Following our chain rule process introduces these intermediate variables:
![](../_resources/8b6f4596da19687c466b96588e683dc9.png)
Let's compute the gradient with respect to w first.

### The gradient with respect to the weights

From before, we know:
![](../_resources/d06c4c8f600aa0408a4ae0181a08e9cb.png)
and
![](../_resources/aeebaed5c0fc1c5a9353bb21db837ffa.png)
Then, for the overall gradient, we get:
![](../_resources/a7ba73a1d1a93c2cc31f161bd210bc74.png)
To interpret that equation, we can substitute an error term  yielding:
![](../_resources/eeb3b81a46ab40aae8889ac809009d3c.png)

From there, notice that this computation is a weighted average across all xi in *X*. The weights are the error terms, the difference between the target output and the actual neuron output for each xi input. The resulting gradient will, on average, point in the direction of higher cost or loss because large *ei* emphasize their associated xi. Imagine we only had one input vector, , then the gradient is just . If the error is 0, then the gradient is zero and we have arrived at the minimum loss. If  is some small positive difference, the gradient is a small step in the direction of . If  is large, the gradient is a large step in that direction. If  is negative, the gradient is reversed, meaning the highest cost is in the negative direction.

Of course, we want to reduce, not increase, the loss, which is why the [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) recurrence relation takes the negative of the gradient to update the current position (for scalar learning rate ):

![](../_resources/3633fa5d6899926cdf1fb5f4afd0bebe.png)

Because the gradient indicates the direction of higher cost, we want to update x in the opposite direction.

### The derivative with respect to the bias

To optimize the bias, *b*, we also need the partial with respect to *b*. Here are the intermediate variables again:

![](../_resources/8b6f4596da19687c466b96588e683dc9.png)
We computed the partial with respect to the bias for equation  previously:
![](../_resources/1217a8e4721638b0fc129bf45d2ef802.png)
For *v*, the partial is:
![](../_resources/5c759cbce43e1bc5e24c0393046a4bfb.png)
And for the partial of the cost function itself we get:
![](../_resources/69ac1e1cf65ce68a5d687c79a211a480.png)
As before, we can substitute an error term:
![](../_resources/86abc7b460de24ccb9516302957f3eef.png)

The partial derivative is then just the average error or zero, according to the activation level. To update the neuron bias, we nudge it in the opposite direction of increased cost:

![](../_resources/bc8662c584bab005f934d74cc2e2ec04.png)

In practice, it is convenient to combine w and *b* into a single vector parameter rather than having to deal with two different partials: . This requires a tweak to the input vector x as well but simplifies the activation function. By tacking a 1 onto the end of x, ,  becomes .

This finishes off the optimization of the neural network loss function because we have the two partials necessary to perform a gradient descent.

## Summary

Hopefully you've made it all the way through to this point. You're well on your way to understanding matrix calculus! We've included a reference that summarizes all of the rules from this article in the next section. Also check out the annotated resource link below.

Your next step would be to learn about the partial derivatives of matrices not just vectors. For example, you can take a look at the matrix differentiation section of [Matrix calculus](https://atmos.washington.edu/~dennis/MatrixCalculus.pdf).

**Acknowledgements**. We thank [Yannet Interian](https://www.usfca.edu/faculty/yannet-interian) (Faculty in MS data science program at University of San Francisco) and [David Uminsky](http://www.cs.usfca.edu/~duminsky/) (Faculty/director of MS data science) for their help with the notation presented here.

## Matrix Calculus Reference

### Gradients and Jacobians

The *gradient* of a function of two variables is a horizontal 2-vector:
![](../_resources/d13353735f863407e61fd10fa614402b.png)

The *Jacobian* of a vector-valued function that is a function of a vector is an  ( and ) matrix containing all possible scalar partial derivatives:

The Jacobian of the identity function  is *I*.

### Element-wise operations on vectors

Define generic *element-wise operations* on vectors w and x using operator  such as :

![](../_resources/eef7b25847355c51b8e16fa4e18f17cd.png)
The Jacobian with respect to w (similar for x) is:
![](../_resources/98544cb968f7ae6130cb2102483ded36.png)

Given the constraint (*element-wise diagonal condition*) that  and  access at most *wi* and *xi*, respectively, the Jacobian simplifies to a diagonal matrix:

![](../_resources/4638bc11daa30516fa3b1d26a727ec1c.png)
Here are some sample element-wise operators:
![](../_resources/89eb09c10497d4a3460ffe988baabec0.png)

### Scalar expansion

Adding scalar *z* to vector x, , is really ![](../_resources/795455b858abfe67cc64eabae25a0376.png) where  and .

![](../_resources/d393030e19b60ff3c4f4cceae49f6401.png)
![](../_resources/4df43edaea8e5072ffdfccfb70fe9494.png)
Scalar multiplication yields:
![](../_resources/236aa0ef65400df0ff7b1ad9550e56e9.png)
![](../_resources/918b06cdfa94d31a978e4dc530083819.png)

### Vector reductions

The partial derivative of a vector sum with respect to one of the vectors is:
![](../_resources/409e7cac0a0571e329a6e77961d84d96.png)
For :

For  and , we get:

Vector dot product ![](../_resources/9fd395983eaa5e3323b51edee7f42d29.png). Substituting  and using the vector chain rule, we get:

![](../_resources/645bf2a2ebd6ea3b064543d15aaa59d0.png)
Similarly, .

### Chain rules

The *vector chain rule* is the general form as it degenerates to the others. When *f* is a function of a single variable *x* and all intermediate variables *u* are functions of a single variable, the single-variable chain rule applies. When some or all of the intermediate variables are functions of multiple variables, the single-variable total-derivative chain rule applies. In all other cases, the vector chain rule applies.

| Single-variable rule | Single-variable total-derivative rule | Vector rule |
| --- | --- | --- |
|     | ![](../_resources/a095c8e36938383996c533c91111f2ef.png) | ![](../_resources/821eb9ac87946bf3a74d9c8e9db020a1.png) |

## Notation

Lowercase letters in bold font such as x are vectors and those in italics font like *x* are scalars. *xi* is the  element of vector x and is in italics because a single vector element is a scalar.  means “length of vector x.”

The *T* exponent of  represents the transpose of the indicated vector.
is just a for-loop that iterates *i* from *a* to *b*, summing all the *xi*.
Notation  refers to a function called *f* with an argument of *x*.

*I* represents the square “identity matrix” of appropriate dimensions that is zero everywhere but the diagonal, which contains all ones.

constructs a matrix whose diagonal elements are taken from vector x.

The dot product  is the summation of the element-wise multiplication of the elements: ![](../_resources/0fe27a01e81fe1e225db9b1ea9d9e264.png). Or, you can look at it as .

Differentiation  is an operator that maps a function of one parameter to another function. That means that  maps  to its derivative with respect to *x*, which is the same thing as . Also, if , then ![](../_resources/fdf55fa1aff41b056d4efe015b6c3b47.png).

The partial derivative of the function with respect to *x*, , performs the usual scalar derivative holding all other variables constant.

The gradient of *f* with respect to vector x, , organizes all of the partial derivatives for a specific scalar function.

The Jacobian organizes the gradients of multiple functions into a matrix by stacking them:

![](../_resources/0f1eca4c92e729a83b2dc78d1966d023.png)

The following notation means that *y* has the value *a* upon  and value *b* upon .

![](../_resources/8c10e0891bfe22b8768ddd3c41d846fc.png)

## Resources

[Wolfram Alpha](http://www.wolframalpha.com/input/?i=D%5B%7Bx%5E2,+x%5E3%7D.%7B%7B1,2%7D,%7B3,4%7D%7D.%7Bx%5E2,+x%5E3%7D,+x%5D) can do symbolic matrix algebra and there is also a cool dedicated [matrix calculus differentiator](http://www.matrixcalculus.org/).

When looking for resources on the web, search for “matrix calculus” not “vector calculus.” Here are some comments on the top links that come up from a [Google search](https://www.google.com/search?q=matrix+calculus&oq=matrix+calculus):

- https://en.wikipedia.org/wiki/Matrix_calculus

The Wikipedia entry is actually quite good and they have a good description of the different layout conventions. Recall that we use the numerator layout where the variables go horizontally and the functions go vertically in the Jacobian. Wikipedia also has a good description of [total derivatives](https://en.wikipedia.org/wiki/Total_derivative), but be careful that they use slightly different notation than we do. We always use the  notation not *dx*.

- http://www.ee.ic.ac.uk/hp/staff/dmb/matrix/calculus.html

This page has a section on matrix differentiation with some useful identities; this person uses numerator layout. This might be a good place to start after reading this article to learn about matrix versus vector differentiation.

- https://www.colorado.edu/engineering/CAS/courses.d/IFEM.d/IFEM.AppC.d/IFEM.AppC.pdf

This is part of the course notes for “Introduction to Finite Element Methods” I believe by [Carlos A. Felippa](https://www.colorado.edu/engineering/CAS/courses.d/IFEM.d). His Jacobians are transposed from our notation because he uses denominator layout.

- http://www.ee.ic.ac.uk/hp/staff/dmb/matrix/calculus.html

This page has a huge number of useful derivatives computed for a variety of vectors and matrices. A great cheat sheet. There is no discussion to speak of, just a set of rules.

- https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf

Another cheat sheet that focuses on matrix operations in general with more discussion than the previous item.

- https://www.comp.nus.edu.sg/~cs5240/lecture/matrix-differentiation.pdf

A useful set of slides.

To learn more about neural networks and the mathematics behind optimization and back propagation, we highly recommend [Michael Nielsen's book](http://neuralnetworksanddeeplearning.com/chap1.html).

For those interested specifically in convolutional neural networks, check out [A guide to convolution arithmetic for deep learning](https://arxiv.org/pdf/1603.07285.pdf).

We reference the law of [total derivative](https://en.wikipedia.org/wiki/Total_derivative), which is an important concept that just means derivatives with respect to *x* must take into consideration the derivative with respect *x* of all variables that are a function of *x*.