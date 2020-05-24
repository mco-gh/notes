5 Reasons to Read Hands-On Machine Learning by Aurélien Géron (Book Review) - ML in Production

# 5 Reasons to Read Hands-On Machine Learning by Aurélien Géron (Book Review)

![handson4-1.jpg](../_resources/02f9231ed071abf7ee7470a3ba1620db.jpg)

Reading a book is one way to learn a new skill, but real mastery only comes from **doing** the thing you’re trying to learn. That’s why whenever someone asks me how to learn machine learning, the first resource I recommend them is [“Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems”](https://amzn.to/2QL6Rz2) by [Aurélien Géron](https://sg.linkedin.com/in/aurelien-geron).

Aurélien Géron worked as a Product Manager at YouTube where he led the development of machine learning for video classification. His experience as a practitioner is evident in Hands-On Machine Learning as each chapter is filled with practical advice and realistic techniques for building machine learning models in industry.

Here are 5 reasons why [Hands-On Machine Learning](https://amzn.to/2QL6Rz2) is hands-down my favorite resource for learning how to build machine learning models.

*This post may contain affiliate links. Please read my [disclosure](http://mlinproduction.com/disclosure/) for more info.*

## Reason 1: Applied Material That Can Be Used When Building Models in Production

The number one reason I love Hands-On Machine Learning is because of the sheer amount of practical, applied ML information that you can use directly when building models. The chapters are filled with examples demonstrating how to use Python libraries like pandas, scikit-learn, and tensorflow to preprocess data, split datasets for training and validation, and build models.

And the author, Aurélien Géron, doesn’t waste any time getting into useful material; in chapter 2 he presents an end-to-end project and discusses how to frame the problem, explore the data, preprocess the inputs, and select, fine-tune, and deploy a model. He does a fantastic job of explaining the "process" of machine learning along with presenting and explaining the accompanying code very clearly so that the reader is aware of what he’s doing, why he’s doing it, and how to do it.

His emphasis on applied material really stands out in the chapter on training deep neural networks. Training neural nets is very different from training classical algorithms like random forests.

Techniques like batch normalization and dropout have been developed to get around specific neural net problems like exploding or vanishing gradients. Géron explains these problems and demonstrates how to solve them with the right techniques. If you’re looking to learn more about deep learning, I would say that this chapter alone is worth the price of the book!

**

> “It is generally not a good idea to train a very large [Deep Neural Network] from scratch: instead, you should always try to find an existing neural network that accomplishes a similar task to the one you are trying to tackle, then just reuse the lower layers of this network: this is called transfer learning.” pg 287

**

## Reason 2: Perfect Amount of Theory & References

For several years after college, I thought that the only way to properly learn a technical topic was to read the densest, most mathematically rigorous textbook on that subject I could find. This is almost certainly a byproduct of my undergrad studies in pure maths, where reading the most theoretical treatment of a subject was required.

But this habit plagued me when I started to learn about machine learning, not least because the prevailing (but incorrect) opinion is that ML is about math and that being good at ML means being a good mathematician. For years I struggled trying to read entire "math-y" ML books, but this approach was very limiting. Those books didn’t teach me how to apply the concepts to real datasets, which is much more important when doing ML in industry, and I usually gave up a few chapters in.

I’ve already mentioned that Hands-On ML is filled with applied material demonstrating how to use the algorithms and techniques on real world datasets. But the text also shines because it blends the perfect amount of theory with the applied content.

When discussing gradient descent, for instance, the author begins with an intuitive explanation of the algorithm and visualizes the effect of learning rates on the algorithm’s ability to converge.

By the time the mathematical formula for gradient descent shows up, I already had a good mental model of what the algorithm was doing. The equation was followed by a Python implementation of the algorithm, which really solidified my understanding of the material.

![gradient_descent.png](../_resources/893917ec507d1c07a1c40ae6047de80b.png)

*Implementation of Gradient Descent from *[*Hands-on Machine Learning*](https://github.com/ageron/handson-ml/blob/master/04_training_linear_models.ipynb)*.*

The text is also filled with references to journal papers, youtube videos, and other books that dig deeper into each of the individual topics. I found these especially useful in the deep learning chapters. Read and understand these references within the context of Hands on ML was much easier for me than reading the references on their own. Being able to read and understand journal papers is an invaluable skill for ML practitioners, and this book helps improve that skill.

**

> “In a 2015 paper, Serget Ioffe and Christian Szegedy proposed a technique called Batch Normalization (BN) to address the vanishing/exploding gradients problems, and more generally the problem that the distribution of each layer’s inputs changes during training, as the parameters of the previous layers change.” pg 282

**

## Reason 3: Excellent Exercises

As I mentioned, real mastery of a skill comes from **doing** the thing you’re trying to learn. And the closer these actions map on to the real domain, the faster you’ll attain that mastery. The exercises included at the end of each chapter provide terrific opportunities for practicing the techniques and concepts taught. And I found that many of these exercises are very similar to the sorts of tasks I do every day as a data scientist.

For instance, many of the exercises ask you to build different types of models and try different preprocessing techniques on particular datasets. These exercises are precisely how applied machine learning happens when building a model in industry. You start with a set of ideas, implement each one, and monitor how those changes impact the predictive performance of the model.

One aspect of the exercises I found really engaging is that the questions encourage you to "play" with code. For example, one exercise asks readers to apply different transformations to MNIST digits in order to augment the dataset. This is very informative from an ML perspective because it helps readers learn the effect of data augmentation, a technique that’s heavily used in computer vision (and other applications of ML), on predictive performance. But it’s also addictive and leaves you with a feeling of accomplishment – both of which are really useful for learning a topic.

**

> “Use t-SNE to reduce the MNIST dataset down to two dimensions and plot the result using Matplotlib. You can use a scatterplot using 10 different colors to represent each image’s target class.” pg 225

**

## Reason 4: Splits Classical ML & Deep Learning

The book is organized in two parts, with part one teaching classical machine learning while part two is focused on deep learning using Tensorflow. Individually, both parts are terrificly written. But it’s the sheer combination of both styles of ML in a single book which makes this text an excellent resource for several different audiences.

The first part of the book, which focuses on classical machine learning algorithms like linear models, support vector machines, and tree-based ensembles is perfect for machine learning novices. The author introduces readers to important ideas like over and underfitting and illustrates the end-to-end model building process with code in early chapters.

The blend of theory and practical exercises are a great way for newbies to learn the concepts while also applying the lessons to data. These readers will benefit from learning the fundamentals in the first half of the book before moving on to deep learning in the second half.

The second part of the book provides a thorough grounding in modern deep learning methods. Each chapter progresses through feedforward, convolutional, and recurrent neural networks and several chapters focus on the Tensorflow library. Again, each chapter contains great exercises forcing readers to apply the lessons learned. Readers who already have a background in classical machine learning can focus on the second part of the book but can use the first half as a reference.

**

> “Don’t jump into deep waters too hastily: while Deep Learning is no doubt one of the most exciting areas in Machine Learning, you should master the fundamentals first. Deep Learning is best suited for complex problems such as image recognition, speech recognition, or natural language processing, provided you have enough data, computing power, and patience.” pg xvi

**

## Reason 5: Very Friendly Style with Helpful Code and Figures

Last but not least, I recommend this book because of it’s friendly style. Machine learning can be an intimidating topic for people, especially if you’re coming from a nontechnical background. But the entire book reads much more like a series of blog posts rather than a textbook, which makes it enjoyable to read and easier to stick with.

And like many popular online blog posts, the book is filled with relevant graphs and figures that help readers understand each topic. For example, the chapters on classification algorithms often include plots of the decision boundaries learned by the model – visual representations of how a model distinguishes between different classes. These visualizations are super helpful for seeing how different choices of hyperparameters or algorithms impact the classification decision.

The best part of the figures is that each one was generated through Python code and all of this code is included within the book’s [Github repository](https://github.com/ageron/handson-ml). This helps readers learn ML concepts as well as tips for creating different plots with matplotlib and sklearn!

![decision_boundaries.png](../_resources/f618d0ef406d4a01297c321e44d21bd9.png)

*Decision Boundaries for different decision trees. Pg 187*

## Conclusion

[Hands-On Machine Learning](https://amzn.to/2QL6Rz2) is a fantastic resource for learning how to build machine learning models. The book is comprehensive, written in a friendly style, and contains excellent exercises, making it a great introduction to the field but also a useful reference text. It’s worth noting that a [new edition of the book](https://amzn.to/2TeAwSR) was recently published in October 2019. This edition is updated for Tensorflow 2.0, which now features the Keras library.

Interested in hearing my thoughts on the latest news, resources, tools, and books on machine learning? Then **subscribe to my weekly newsletter below**. One email a week for all the ML info you need.

Join the Newsletter

Each Tuesday I send out my weekly newsletter and latest blog posts. Subscribe to get my best content.

We won't send you spam. Unsubscribe at any time.

[Powered By ConvertKit](https://convertkit.com/?utm_source=dynamic&utm_medium=referral&utm_campaign=poweredby&utm_content=form)

![cc4e858e31735f434c648dbd1d0b0866](../_resources/89f301ba27fcd25a53fe877506d0dd92.png)Author   [Luigi](https://mlinproduction.com/author/luigi/)/Posted on [January 15, 2020](https://mlinproduction.com/hands-on-machine-learning-by-aurelien-geron-book-review/)/Categories [Book Review](https://mlinproduction.com/category/book-review/)