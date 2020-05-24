A Gentle Guide to Machine Learning | MonkeyLearn Blog

## A Gentle Guide to Machine Learning

- [![](../_resources/967fbc9f13f5a236655a7e4d5f9a1ef6.png)](https://monkeylearn.com/blog/wp-content/uploads/2015/08/stone-tool-crop.png)

.

-
-

Machine Learning is a subfield within Artificial Intelligence that builds algorithms that allow computers to learn to perform tasks from data instead of being explicitly programmed.

Got it? We can make machines learn to do things! The first time I heard that, it blew my mind. That means that we can program computers to learn things by themselves!

The ability of learning is one of the most important aspects of intelligence. Translating that power to machines, sounds like a huge step towards making them more intelligent. And in fact, Machine Learning is the area that is making most of the progress in Artificial Intelligence today; being a trendy topic right now and pushing the possibility to have more intelligent machines.

This post will try to give the novice reader a brief introduction to Machine Learning. I’ll give a general overview of important concepts, applications and challenges when working with Machine Learning. It’s not the goal of this post to give a formal or exhaustive description about the topic, but to give some initial concepts to invite the reader to continue investigating.

## **The real thing about Machine Learning**

Alright, not all is as beautiful as it sounds, Machine Learning has its limits. Still, we can’t build intelligent machines like *Data* from *Star Trek* or *Hal 9000* from *2001 a Space Odyssey*. However, we have plenty of examples of **real world applications** where Machine Learning works like a charm. The following are some of the most common categories of practical Machine Learning applications:

### **Image Processing**

Image processing problems basically have to analyze images to get data or do some transformations. Some examples are:

- **Image tagging**, like in Facebook, when the algorithm automatically detects that your face or the face of your friends appear in a photo. Basically a Machine Learning algorithm learns from the photos you manually tag.
- **Optical Character Recognition** (OCR), when algorithms learn to transform a manuscript or scanned text document into a digital version. The algorithm has to learn to transform an image of a written character into the corresponding digital letter.
- **Self-driving cars**: part of the mechanisms that allow cars to drive by themselves use image processing. A Machine Learning algorithm learns where’s the edge of the road, if there’s a stop sign or a car is approaching by looking at each frame taken by a video camera.

### **Text Analysis**

Text analysis are processes where we extract or classify information from text, like tweets, emails, chats, documents, etc. Some popular examples are:

- **Spam filtering**, one of the most known and used text classification applications (assign a category to a text). Spam filters learn to classify an email as spam or ham depending on the content and the subject.
- **Sentiment Analysis**, another application of text classification where an algorithm must learn to classify an opinion as positive, neutral or negative depending on the mood expressed by the writer.
- **Information Extraction**, from a text, learn to extract a particular piece of information or data, for example, extracting addresses, entities, keywords, etc.

### **Data Mining**

Data mining is the process of discovering patterns or making predictions from data. The definition is a bit generic, but think of it as mining useful information from a huge table in a database. Each row would be our training instances, and each column a feature. We may be interested in predicting a new column in that table based on the rest of the columns, or discover patterns to group the rows. For example:

- **Anomaly detection**: detect outliers, for example for credit card fraud detection, you could detect which transactions are outliers from the usual purchasing pattern of a user.
- **Association rules**: for example, in a supermarket or e-commerce site, you can discover customer purchasing habits by looking at which products are bought together. This information can be used for marketing purposes.
- **Grouping**: for example, in a SaaS platform, group users by their behaviour or their profile.
- **Predictions**: predict a variable (column in a database) from the rest of the variables. For example, you could predict the credit score of new customers in a bank based by learning from the profiles and credit score of current customers.

### **Video Games & Robotics**

Video games and robotics have been a huge field where Machine Learning has been applied. In general we have an agent (game character or robot) that has to move within an environment (a virtual environment in a video game or physical environment in the case of robots). Machine Learning then can be used to allow the agent to perform tasks, like moving in an environment while avoiding obstacles or enemies. A very popular Machine Learning technique used in these cases is [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning), where the agent learns to perform a task by learning from the reinforcement of the environment (the reinforcement is negative if it hits an obstacle or positive if it gets to the goal).

## **Alright, I got the value of Machine Learning, but how does it work?**

One of the first books I read about Machine Learning about ten years ago was [*Machine Learning* by Tom Mitchell](http://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077/ref=sr_1_10?ie=UTF8&qid=1440450490&sr=8-10&keywords=machine+learning). This book was written in 1997, but the general concepts remain valid today.

From that book, I like the following formal definition about Machine Learning:

*A computer program is said to learn to perform a ****task T**** from ****experience E****, if its performance at task T, as measured by a ****performance metric P****, improves with experience E over time.*

For example, an artificial game player that has to play chess (task T), could learn by looking at previous chess matches or playing against a tutor (experience E). It’s performance P can be measured by counting the percentage of games won against a human.

Let’s picture that in a couple of more examples:

- **Example 1**: A system that given an image, it has to say if Barack Obama’s face appears in that image (the generalization would be like Facebook’s auto tagging).
- **Example 2**: A system that given a tweet, tells if it talks with a positive or negative mood.
- **Example 3**: A system that given some person’s profile, assigns a score representing the probability of that person paying a credit loan.

In example 1, the task is to detect when Barack Obama’s face appears in an image. The experience could be a set of images where Barack Obama’s face appears and others where it doesn’t appear. The performance could be measured as the percentage of new images that our system correctly tags.

In example 2, the task is to assign the sentiment of a tweet. The experience could be a set of tweets and their corresponding sentiment. The performance could be measured as the percentage of new tweets that our system correctly classifies.

In example 3, the task is to assign a credit score. The experience could be a set of user profiles with their corresponding credit scores. The performance could be measured as the squared error (the difference between the predicted and expected score).

In order to allow the algorithm to learn to transform the input to the desired output, you have to provide what is called training instances or **training examples**, which in Mitchell’s definition are defined as experience E. A training set is a set of instances that will work as examples from which the Machine Learning algorithm will learn to perform the desired task. Pretty intuitive, isn’t it? It’s like when you show a little baby how to throw a ball, you throw the ball a couple of times to show him how to do it, and by looking at those examples, he starts to learn to do it himself.

Every training instance usually is represented as a fixed set of attributes or **features**. The features are the way to characterize each instance. For instance, in example 1, an image could be characterized by the gray level of each of its pixels. In example 2, a tweet could be characterized by the words that appear in the tweet. In example 3, a credit record could be represented by the age of the person, the salary, the profession, etc.

Calculating and selecting the proper features to represent an instance is one of the most important tasks when working with Machine Learning, we’ll take a look at this point later in this post.

## **Categories of Machine Learning algorithms**

At this point we have to talk about two general categories of Machine Learning algorithms: **Supervised Learning** or **Unsupervised Learning **algorithms. The main difference between both approaches resides in the way we feed training examples to our algorithm, how the algorithm uses them and the type of problems they solve.

### **Supervised Learning**

In the case of [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning), the Machine Learning algorithm can be seen as a process that has to transform a particular input to a desired output.

The Machine Learning process then has to learn how to transform every possible input to the correct/desired output, so each training example has the particular input and the desired output.

In the example about the artificial chess player, our input would be a particular chess board state, and the output would be the best possible movement in that situation.

Depending on the type of output, we have two subtypes of supervised learning:

#### **Classification**

When the output value belongs to a discrete and finite set, we’re talking about a [classification](https://en.wikipedia.org/wiki/Statistical_classification). Example 2 can be solved as a classification problem, the output is a finite set of options: positive, negative or neutral. In this case, our training examples will look like:

[![table1](../_resources/167f08048be02bee8cfbb5f74516dd0b.png)](https://blog.monkeylearn.com/wp-content/uploads/2015/08/table1.png)

#### **Regression**

When the output value is a continuous number, for example, a probability, then we’re talking about a [regression](https://en.wikipedia.org/wiki/Regression_analysis) problem. Example 3 is a regression as the result is a number between 0 and 1 that represents the probability that a person will pay his debts. In this case, our training examples will look like:

[![table2](../_resources/afae51200bc8e747072e5020a4455709.png)](https://blog.monkeylearn.com/wp-content/uploads/2015/08/table2.png)

Supervised learning is the most popular category of Machine Learning algorithms. The disadvantage of using this approach is that for every training example, we have to provide the correct output, and in many cases, this is quite expensive. For example, in the case of sentiment analysis, if we need 10,000 training examples (tweets), we would have to tag each tweet with the correct sentiment (positive, negative or neutral). That would require a group of humans to read and tag each tweet (quite a time consuming and boring task). This is usually a very **common bottleneck for Machine Learning** algorithms: gather quality tagged training data.

### **Unsupervised Learning**

There’s a second category of Machine Learning algorithms called [unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning). In this case, the training examples only need to be the input to the algorithm, but not the desired output. The typical use case is to discover the hidden structure and relations between the training examples. A typical example are [clustering algorithms](https://en.wikipedia.org/wiki/Cluster_analysis), where we learn to find similar instances or groups of instances (clusters). E.g.: we have a news article and we want to get similar ones to recommend. Some clustering algorithms like [K-means](https://en.wikipedia.org/wiki/K-means_clustering) “learn” to do that by only looking at the input.

## **Machine Learning algorithms**

Ok, here’s when the math and logic comes to action. In order to transform an input to a desired output we can use different models. Machine Learning is not a unique type of algorithm, perhaps you heard about Support Vector Machines, Naive Bayes, Decision Trees or Deep Learning. Those are different Machine Learning algorithms that try to solve the same problem: learn to transform every input to the correct output.

Those different Machine Learning algorithms use different paradigms or techniques to do the learning process and represent the knowledge of what they have learned.

But before we go ahead and talk about each algorithm, a common principle is that, Machine Learning algorithms try to** make generalizations**. That is, they try to explain something with the simplest theory, a principle known as the [Occam’s razor](https://en.wikipedia.org/wiki/Occam%27s_razor). Every Machine Learning algorithm, regardless of the paradigm it uses, will try to create the simplest hypothesis (the one that makes fewest assumptions) that explains most of the training examples.

There are lot of Machine Learning algorithms, but let’s briefly mention three of the most popular ones:

- **Support Vector Machines**: The model tries to build a set of hyperplanes in a high dimensional space that tries to separate instances of different classes by getting the largest separation between the nearest instances from different classes. The concept intuitively is simple, but the model can be very complex and powerful. In fact, for some domains it is one of the best Machine Learning algorithms you can use nowadays.
- **Probabilistic Models**: these models usually try to predict the correct response by modeling the problem with a probability distribution. Perhaps the most popular algorithms in this category are [Naive Bayes classifiers](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), that use the Bayes theorem alongside with strong independence assumptions between the features. One of their advantages besides being a simple yet powerful model, is that they return not only the prediction but also the degree of certainty, which can be very useful.
- **Deep Learning**: is a new trend in Machine Learning based on the very known [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network) models. Neural networks have a connectionist approach, they try to emulate (in a very simplified way) the way the brain works. Basically they consist of a huge set of interconnected neurons (the basic unit of processing), organized in various layers. Deep learning has, in a few words, developed new structures with deeper layers and improved the learning algorithms to not only try to learn but also to build structures to represent the most important features automatically with higher levels of abstraction.

## **Important aspects when dealing with Machine Learning**

Again, Machine Learning sounds like a beautiful concept, and it is, but there are some processes involved that are not so automatic. In fact, many times manual steps are required when designing the solution. Nevertheless, they are of **huge importance** in order to obtain decent results. Some of those aspects are:

### **Which type of Machine Learning algorithm should I use?**

**Supervised or unsupervised?**

Do you have tagged data? That is, the input with its corresponding output? In that case you can apply supervised learning algorithms. If not, perhaps unsupervised algorithms can solve the problem.

**Classification, regression or clustering?**

That mainly depends on what you’re trying to solve. If you want to tag data (assign a tag within a discrete set of options), classification may be the right option. If on the other hand, you need to assign a number, for example a score, regression may be the best option for you. Perhaps what you need is to recommend similar products to users depending on what they are currently looking at in an e-commerce site, in that case clustering could be the best option for you.

**Deep Learning, SVM, Naive Bayes, Decision Trees… which one is the best?**

The answer for me is: none of them. Obviously Deep Learning and Support Vector Machines have demonstrated they are the most powerful and versatile in different applications. But take into account that depending on the particular application, some Machine Learning algorithms may be a better choice than others. Just see which are their individual strengths and try them!

### **Feature engineering**

Feature engineering is the process by which we extract and select the most important features to be used to represent our training examples and instances to be processed by our Machine Learning algorithm. This process is one of the most important aspects of Machine Learning (and sometimes not given enough credit and importance).

Pay attention to that: if you don’t provide quality features to your algorithm, the results will be bad, no matter if you use the best Machine Learning algorithm out there. It’s like trying to learn to read with your eyes in complete darkness, you won’t be able to do that, no matter how intelligent you are.

#### **Feature extraction**

In order to feed the Machine Learning algorithm with data, you usually have to transform the raw data into something that the algorithm can ‘understand’. That process is known as **feature extraction**. Usually we’re talking about transforming the raw data into a vector of features.

In example 1, how do we feed the Machine Learning algorithm with an image?

Well, a straightforward approach would be to transform the image into a vector where each component is the gray value of each pixel in the image. So, each component or feature, would be a number between say 0 and 255, 0 being black, 255 white and the range between 1 to 254 the possible shades of gray.

This approach may work, but perhaps it would work better if we provide higher level features:

- Does the image contain the face of a person?
- What’s the skin color?
- What’s the eye color?
- Does the face have hair?
- …

Those are higher level features, that feed the algorithm with more knowledge than just the gray level of each pixel (and their calculation may be done by other Machine Learning algorithms!). By providing higher level features we’re ‘helping’ the Machine Learning algorithm with better information to learn to decide if my or someone else’s face appears in an image.

If we provide better feature extraction:

- We’ll have more chances that our algorithm will learn to perform the desired task.
- We may need less training examples to learn.
- As a result, we may reduce dramatically the time needed to train our model.

#### **Feature selection**

Sometimes (not to say mostly), the features that we selected to feed our algorithm may be useless. For example, when trying to tag the sentiment of a tweet, we could add the length of the tweet as a feature, the time of the day the tweet was written, etc. Those features may be useful or not, and there are automatic methods to figure out which of them are the most useful. Intuitively, **feature selection algorithms** use techniques to score each feature and return only they most valuable ones according to that score.

Another important thing to keep in mind is: avoid using huge feature sets. One may be tempted to add all the possible features to the model and let the algorithm just learn. But that’s not a good idea, as we add more features to represent our instances, the dimension of the space increases, making it more sparse. Intuitively, as we get more features, we have to get much many instances to represent a decent amount of the combinations. This is a very common problem known as the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality), as the complexity of the model grows, the number of training examples needed grows exponentially, and believe me, that’s a problem.

### **Training examples**

So, you have to feed the Machine Learning algorithm with training examples. Depending on the problem you want to solve, we may be talking in the order of hundreds, thousands, millions or billions of training examples. Besides, it’s very important to keep the quality of the examples, if you feed the algorithm with wrong examples, the chances to obtain good results are low.

Collecting quality data in huge volumes to train Machine Learning algorithms is usually an expensive thing to do. Unless you already have tagged data, you may have to manually tag the data yourself or pay others to do that. Some tools to try to solve that are **crowdsourcing platforms** where you can find labor to do the job. Also **bootstrapping** is a way to try to make tagging more efficient by using your own Machine Learning model to help you.

The general rule regarding training examples is: the more quality training data you can gather, the better results you may get.

### **Testing examples and performance metrics**

After we train a Machine Learning algorithm, we have to test how well it performs. This is super important, otherwise you won’t know if your model actually learned anything!

The concept is simple, we use a **testing set**, a set of instances not contained in the training set. Basically we’ll input every testing example to our model and see if it performs as expected. In the case of supervised learning classification, we just input each testing instance and check if the outputs are what we expected. If our model returns the correct output on 95% of the testing examples, we say that our model has an accuracy of 95%.

It’s important to remember that the training and testing sets of instances must be disjoint, this is the only way to test the generalization and prediction power of your model. You may have very good results by measuring the accuracy in your training data, but get poor results when measuring in a separate testing set. That problem is known as [overfitting](https://en.wikipedia.org/wiki/Overfitting), that is, the algorithm overfits the training examples and has a poor predictive power. Usually the way to avoid that is to try to use a simpler model with less features, simplify the model and use a bigger and more representative training set.

Accuracy is the most basic metric, you should also look at other metrics like [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall) which will tell you how well the algorithm performs on each class (when working with supervised learning classification). [Confusion matrices](https://en.wikipedia.org/wiki/Confusion_matrix) are a great tool to see where our classification algorithm is ‘confusing’ predictions.

For regression and clustering problems you have other sets of metrics that will allow to see if your algorithm is performing well.

### **Performance**

In real world applications, if you have to deploy a solution in production, you will have to build a robust and performant solution. In the case of Machine Learning applications, this can be a complex task. First, you have to select the Machine Learning framework, which is not easy as not all programming languages have strong tools on that. Python and [Scikit-learn](http://scikit-learn.org/) are good examples of a programming language where a strong Machine Learning framework was built.

Having chosen your framework, performance issues may arise. Depending on the amount of data, complexity and algorithm designed, it may take large amounts of computing power and memory to run the training process. You’ll probably have to run multiple trainings until you get decent results. Besides, usually you may be retraining your model to cover new instances and keep improving its accuracy.

In order to train huge models and get fast results when using it, we’re usually talking of various GBs of RAM and multi-core machines to parallelize the processing.

These are mostly practical issues, but definitively important ones if you want to deploy a real Machine Learning solution in production.

## **Final words**

That’s it, a brief overview of what Machine Learning is about. There are plenty of other real world applications not covered here, plenty of other Machine Learning algorithms and concepts to talk about, but we leave the reader to do his/her own research on that.

Machine Learning is powerful but hard, the difficulties and aspects to take into account described in this post are just the tip of the iceberg.

Usually a certain background in computer science and in particular, Machine Learning is required to obtain decent results. One can end very disappointed by the many difficulties to solve before getting on track.

This is why we created [MonkeyLearn](http://www.monkeylearn.com/), to democratize the access to Machine Learning technologies applied to text analysis. To avoid reinventing the wheel and allow every software developer or entrepreneur to quickly get practical results. These are our main challenges, to abstract the end user of all of these problems, ranging from Machine Learning complexities to practical scalability issues to make just plug and play Machine Learning.

Hope you enjoyed this post! Just drop me a line if you have any questions or comments!

By [Raúl Garreta](https://monkeylearn.com/blog/author/raul/)|August 27th, 2015|[Guides](https://monkeylearn.com/blog/category/guides/)|[25 Comments](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/#comments)

## About the Author: [Raúl Garreta](https://monkeylearn.com/blog/author/raul/)

![3f6e517b10e5ebff6bfb1066395361ed.png](../_resources/7c8af1a0bbaf99d6519f1521a1e9b850.png)

MonkeyLearn Co-Founder & CEO. Machine Learning and Natural Language Processing expert. Author of "Learning scikit-learn: Machine Learning in Python".

## Related Posts

- [![](../_resources/57b1b7254f41332961217c9c0b1880c0.png)](https://monkeylearn.com/blog/how-to-create-text-classifiers-machine-learning/)

### [How to create text classifiers with Machine Learning](https://monkeylearn.com/blog/how-to-create-text-classifiers-machine-learning/)

- [![](../_resources/db76c76a441d0d8acb6fdc292b9cdcd9.png)](https://monkeylearn.com/blog/training-sentiment-analysis-classifier-using-web-scraping-visual-tool/)

### [Training a sentiment analysis classifier using a web scraping visual tool](https://monkeylearn.com/blog/training-sentiment-analysis-classifier-using-web-scraping-visual-tool/)

- [![Analyzing #first7jobs tweets with MonkeyLearn and R](../_resources/219d1be758bccf94240eac3b898ff033.jpg)](https://monkeylearn.com/blog/analyzing-first7jobs-tweets-monkeylearn-r/)

### [Analyzing #first7jobs tweets with MonkeyLearn and R](https://monkeylearn.com/blog/analyzing-first7jobs-tweets-monkeylearn-r/)

- [![Building a Twitter bot with PHP and Machine Learning](../_resources/b9245a01a2844abf25bcd9547c84b6bd.png)](https://monkeylearn.com/blog/building-twitter-bot-with-php-machine-learning/)

### [Building a Twitter bot with PHP and Machine Learning](https://monkeylearn.com/blog/building-twitter-bot-with-php-machine-learning/)



## 25 Comments

1. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Rodrigo**August 28, 2015 at 11:04 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=733#respond)

Te agradezco y te felicito, es una muy buena introducción a Machine Learning, yo estoy trabajando desde hace un año con procesamiento de lenguaje natural y esta perfectamente bien explicado este articulo.

    - ![3f6e517b10e5ebff6bfb1066395361ed.png](../_resources/5c34070a31c983875132c11577a40db0.png)

**Raúl Garreta**August 28, 2015 at 1:15 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=734#respond)

Gracias Rodrigo, me alegro que hayas disfrutado de la guía!
2. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[Hassan Askari](https://www.facebook.com/app_scoped_user_id/1182717768421970/)**August 29, 2015 at 2:58 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=736#respond)

Best article on Machine learning I have read so far. Hats off to you, Raúl Garreta!!!

#intuitive
#understandable
#interesting
Cheers.

    - ![3f6e517b10e5ebff6bfb1066395361ed.png](../_resources/5c34070a31c983875132c11577a40db0.png)

**Raúl Garreta**August 30, 2015 at 5:16 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=740#respond)

Thanks Hassan! Glad you enjoyed the post, we’ll be continuing the series with more practical applications and thoughts.

Cheers,

        - ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Ian Doolan**November 22, 2016 at 12:41 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1582#respond)

Fantastic article, extremely well put together.

            - ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**chioma**May 6, 2017 at 11:46 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1801#respond)

Very helpful. Great one. I am completely new in NLP, still looking at Unsupervised morphology induction but the language is a low resource one. my problem is of small training data size. i cannot apply some modern techniques

3. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[dagosti](http://gravatar.com/dagosti)**September 13, 2015 at 10:41 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=772#respond)

Great article
4. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[vibhanshu sharma](https://plus.google.com/105755887868956795464)**September 15, 2015 at 10:49 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=783#respond)

Short and sweet, what a good article to tell people about machine learning.
5. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[Scott](https://twitter.com/mediocrescottt)**October 14, 2015 at 7:37 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=849#respond)

Thanks! What a great article. Where can I read more?

    - ![60a1dee98c468dc34224522382da38a6.jpg](../_resources/174528bda92e2784afdf5584b1a80d90.jpg)

**[Federico Pascual](http://www.tryolabs.com/)**October 16, 2015 at 2:39 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=854#respond)

Hey Scott, glad you liked the guide. Stay tuned, we have a couple of new posts coming that are in the same spirit.

Meanwhile, you might be interested in these other posts:

– [Sentiment Analysis APIs Benchmark](http://blog.monkeylearn.com/sentiment-analysis-apis-benchmark/)

– [The future of AI is on the Cloud](https://blog.monkeylearn.com/the-future-of-ai-is-on-the-cloud/)

– [Analyzing news headlines across the globe with Kimono and MonkeyLearn](http://blog.monkeylearn.com/are-you-getting-the-whole-story-analyzing-news-headlines-across-the-globe-with-kimono-and-monkeylearn/)

– [Understanding users through Twitter data and machine learning](https://blog.twitter.com/2015/guest-post-understanding-users-through-twitter-data-and-machine-learning)

– [Sentiment analysis with machine learning and web scraped data](http://blog.monkeylearn.com/kimono-monkeylearn-sentiment-analysis-with-machine-learning-and-web-scraped-data/)

– [How to Create an Employment Analytics Visualization in Less Than 10 Minutes](http://blog.monkeylearn.com/how-to-create-an-employment-analytics-visualization-in-less-than-10-minutes/)

Cheers!
6. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[Sonit Singh](https://www.facebook.com/app_scoped_user_id/10206696775035661/)**October 31, 2015 at 6:54 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=875#respond)

Wonderful explanation and great examples! Great work.
7. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[Selvakumar Gna](https://plus.google.com/+selvakumar735)**November 30, 2015 at 3:09 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=890#respond)

Nice article. very easy to understand for new person in this area of research work..

8. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Durairaj Gopal**January 23, 2016 at 11:28 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=912#respond)

Nice article ,it is very usefull to me
9. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[ed fernandez (@efernandez)](http://twitter.com/efernandez)**April 11, 2016 at 1:10 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1159#respond)

Hola Raul, felicidades por vuestro trabajo, gran proyecto, me gustaría hablar con vosotros. Estoy en Palo Alto, somos una VC boutique, dadme un email de contacto y os doy contexto. Un saludo

10. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[Fernando Lopez Bello (@fer_lopezbello)](http://twitter.com/fer_lopezbello)**April 25, 2016 at 8:28 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1194#respond)

Excelente síntesis, saludos.
11. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**[Sergei Makhmodov](http://daxtra.com/)**May 11, 2016 at 9:16 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1221#respond)

Great article, I enjoyed reading it!
12. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**veena**June 14, 2016 at 12:05 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1339#respond)

Thanks for sharing with us. Best article
13. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**dilipbobby**August 16, 2016 at 2:14 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1433#respond)

good one 🙂
14. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Amzee**October 3, 2016 at 1:13 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1499#respond)

best article ive read so far
Do you help coding in Matlab?
Im working on Extreme Learning Machines..Pls help
15. ![d6e4553c82cb0a0cedf8224126d92950.jpg](../_resources/42a13fb7d4b9cf50c40589bcc5de450a.jpg)

**Mark Kaghazgarian**November 16, 2016 at 7:38 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1575#respond)

That was really interesting way to explain one of the most complicated tech concept in a few simple words. Nice job!

16. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Raven Markus**February 12, 2017 at 1:14 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1732#respond)

One of the best intro to ML.
17. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Shivaprasada varanashi**March 31, 2017 at 4:03 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1786#respond)

Good article for a better understanding on the basics
18. ![5eac7d380927d82dc9bffb55798d1270.jpg](../_resources/16b5bf34e29550f6f23fa731d34a4061.jpg)

**Sva**April 20, 2017 at 8:58 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=1793#respond)

Great article, putting everything into perspective
19. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**John Rhmny**June 5, 2017 at 7:55 am[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=2032#respond)

Great intro to ML, good job!
20. ![a564d50192b0ccb75ce363fac0d4f826.jpg](../_resources/9014c024eaec3061c237a3c0fb2f4583.jpg)

**Claire**June 15, 2017 at 1:39 pm[- Reply](https://monkeylearn.com/blog/a-gentle-guide-to-machine-learning/?replytocom=2216#respond)

It is very inspiring!

###

## Leave A Comment