160+ Data Science Interview Questions - By Alexey Grigorev

 [(L)](https://hackernoon.com/@alexeygrigorev)
 [**Alexey Grigorev**](https://hackernoon.com/@alexeygrigorev)
Lead Data Scientist at OLX Group

 [**](https://twitter.com/Al_Grigor)  [**](https://www.linkedin.com/in/agrigorev/)  [**](https://github.com/alexeygrigorev)

# 160+ Data Science Interview Questions

March 1st 2020

 [** Tweet This](https://twitter.com/intent/tweet?text=160%2B%20Data%20Science%20Interview%20Questions&url=https%3A%2F%2Fhackernoon.com%2F160-data-science-interview-questions-415s3y2a&via=Al_Grigor&hashtags=machinelearning,datascience,interviewquestions)

 ![](../_resources/3138be0b61ee43086ba20b0b381693fa.png)

A typical interview process for a data science position includes multiple rounds. Often, one of such rounds covers theoretical concepts, where the goal is to determine if the candidate knows the fundamentals of machine learning.

In this post, I’d like to summarize all my interviewing experience  —  from both interviewing and being interviewed  —  and came up with a list of 160+ theoretical data science questions.

This includes the following topics:

- •Linear regression
- •Validation
- •Classification and logistic regression
- •Regularization
- •Decision trees
- •Random forest
- •Gradient boosting trees
- •Neural networks
- •Text classification
- •Clustering
- •Ranking: search and recommendation
- •Time series

The number of questions in this post might seem overwhelming  —  and it indeed is. Keep in mind that the interview flow is based on what the company needs and what you have worked with, so if you didn’t work with models in time series or computer vision, you shouldn’t get questions about them.

Important: don’t feel discouraged if you don’t know the answers to some of the interview questions. This is absolutely fine.

Finally, to make it simpler, I grouped the questions into three categories, based on difficulty:

- • easy
- •‍⭐️ medium
- • expert

That’s, of course, subjective, and it’s based only on my personal opinion.
Let’s start!
************
Supervised machine learning

- •What is supervised machine learning?

Linear regression

- •What is regression? Which models can you use to solve a regression problem?
- •What is linear regression? When do we use it?
- •What’s the normal distribution? Why do we care about it?
- •How do we check if a variable follows the normal distribution? ‍⭐️
- •What if we want to build a model for predicting prices? Are prices distributed normally? Do we need to do any pre-processing for prices? ‍⭐️
- •What are the methods for solving linear regression do you know? ‍⭐️
- •What is gradient descent? How does it work? ‍⭐️
- •What is the normal equation? ‍⭐️
- •What is SGD  —  stochastic gradient descent? What’s the difference with the usual gradient descent? ‍⭐️
- •Which metrics for evaluating regression models do you know?
- •What are MSE and RMSE?

Validation

- •What is overfitting?
- •How to validate your models?
- •Why do we need to split our data into three parts: train, validation, and test?
- •Can you explain how cross-validation works?
- •What is K-fold cross-validation?
- •How do we choose K in K-fold cross-validation? What’s your favorite K?

Classification

- •What is classification? Which models would you use to solve a classification problem?
- •What is logistic regression? When do we need to use it?
- •Is logistic regression a linear model? Why?
- •What is sigmoid? What does it do?
- •How do we evaluate classification models?
- •What is accuracy?
- •Is accuracy always a good metric?
- •What is the confusion table? What are the cells in this table?
- •What is precision, recall, and F1-score?
- •Precision-recall trade-off ‍⭐️
- •What is the ROC curve? When to use it? ‍⭐️
- •What is AUC (AU ROC)? When to use it? ‍⭐️
- •How to interpret the AU ROC score? ‍⭐️
- •What is the PR (precision-recall) curve? ‍⭐️
- •What is the area under the PR curve? Is it a useful metric? ‍⭐️
- •In which cases AU PR is better than AU ROC? ‍⭐️
- •What do we do with categorical variables? ‍⭐️
- •Why do we need one-hot encoding? ‍⭐️

Regularization

- •What happens to our linear regression model if we have three columns in our data: x, y, z  —  and z is a sum of x and y? ‍⭐️
- •What happens to our linear regression model if the column z in the data is a sum of columns x and y and some random noise? ‍⭐️
- •What is regularization? Why do we need it?
- •Which regularization techniques do you know? ‍⭐️
- •What kind of regularization techniques are applicable to linear models? ‍⭐️
- •How does L2 regularization look like in a linear model? ‍⭐️
- •How do we select the right regularization parameters?
- •What’s the effect of L2 regularization on the weights of a linear model? ‍⭐️
- •How L1 regularization looks like in a linear model? ‍⭐️
- •What’s the difference between L2 and L1 regularization? ‍⭐️
- •Can we have both L1 and L2 regularization components in a linear model? ‍⭐️
- •What’s the interpretation of the bias term in linear models? ‍⭐️
- •How do we interpret weights in linear models? ‍⭐️
- •If a weight for one variable is higher than for another  —  can we say that this variable is more important? ‍⭐️
- •When do we need to perform feature normalization for linear models? When it’s okay not to do it? ‍⭐️

Feature selection

- •What is feature selection? Why do we need it?
- •Is feature selection important for linear models? ‍⭐️
- •Which feature selection techniques do you know? ‍⭐️
- •Can we use L1 regularization for feature selection? ‍⭐️
- •Can we use L2 regularization for feature selection? ‍⭐️

Decision trees

- •What are the decision trees?
- •How do we train decision trees? ‍⭐️
- •What are the main parameters of the decision tree model?
- •How do we handle categorical variables in decision trees? ‍⭐️
- •What are the benefits of a single decision tree compared to more complex models? ‍⭐️
- •How can we know which features are more important for the decision tree model? ‍⭐️

Random forest

- •What is random forest?
- •Why do we need randomization in random forest? ‍⭐️
- •What are the main parameters of the random forest model? ‍⭐️
- •How do we select the depth of the trees in random forest? ‍⭐️
- •How do we know how many trees we need in random forest? ‍⭐️
- •Is it easy to parallelize training of a random forest model? How can we do it? ‍⭐️
- •What are the potential problems with many large trees? ‍⭐️
- •What if instead of finding the best split, we randomly select a few splits and just select the best from them. Will it work?
- •What happens when we have correlated features in our data? ‍⭐️

Gradient boosting

- •What is gradient boosting trees? ‍⭐️
- •What’s the difference between random forest and gradient boosting? ‍⭐️
- •Is it possible to parallelize training of a gradient boosting model? How to do it? ‍⭐️
- •Feature importance in gradient boosting trees  —  what are possible options? ‍⭐️
- •Are there any differences between continuous and discrete variables when it comes to feature importance of gradient boosting models?
- •What are the main parameters in the gradient boosting model? ‍⭐️
- •How do you approach tuning parameters in XGBoost or LightGBM?
- •How do you select the number of trees in the gradient boosting model? ‍⭐️

Parameter tuning

- •Which parameter tuning strategies (in general) do you know? ‍⭐️
- •What’s the difference between grid search parameter tuning strategy and random search? When to use one or another? ‍⭐️

Neural networks

- •What kind of problems neural nets can solve?
- •How does a usual fully-connected feed-forward neural network work? ‍⭐️
- •Why do we need activation functions?
- •What are the problems with sigmoid as an activation function? ‍⭐️
- •What is ReLU? How is it better than sigmoid or tanh? ‍⭐️
- •How we can initialize the weights of a neural network? ‍⭐️
- •What if we set all the weights of a neural network to 0? ‍⭐️
- •What regularization techniques for neural nets do you know? ‍⭐️
- •What is dropout? Why is it useful? How does it work? ‍⭐️

Optimization in neural networks

- •What is backpropagation? How does it work? Why do we need it? ‍⭐️
- •Which optimization techniques for training neural nets do you know? ‍⭐️
- •How do we use SGD (stochastic gradient descent) for training a neural net? ‍⭐️
- •What’s the learning rate?
- •What happens when the learning rate is too large? Too small?
- •How to set the learning rate? ‍⭐️
- •What is Adam? What’s the main difference between Adam and SGD? ‍⭐️
- •When would you use Adam and when SGD? ‍⭐️
- •Do we want to have a constant learning rate or we better change it throughout training? ‍⭐️
- •How do we decide when to stop training a neural net?
- •What is model checkpointing? ‍⭐️
- •Can you tell us how you approach the model training process? ‍⭐️

Neural networks for computer vision

- •How we can use neural nets for computer vision? ‍⭐️
- •What’s a convolutional layer? ‍⭐️
- •Why do we actually need convolutions? Can’t we use fully-connected layers for that? ‍⭐️
- •What’s pooling in CNN? Why do we need it? ‍⭐️
- •How does max pooling work? Are there other pooling techniques? ‍⭐️
- •Are CNNs resistant to rotations? What happens to the predictions of a CNN if an image is rotated?
- •What are augmentations? Why do we need them? What kind of augmentations do you know? How to choose which augmentations to use? ‍⭐️
- •What kind of CNN architectures for classification do you know?
- •What is transfer learning? How does it work? ‍⭐️
- •What is object detection? Do you know any architectures for that?
- •What is object segmentation? Do you know any architectures for that?

Text classification

- •How can we use machine learning for text classification? ‍⭐️
- •What is bag of words? How we can use it for text classification? ‍⭐️
- •What are the advantages and disadvantages of bag of words? ‍⭐️
- •What are N-grams? How can we use them? ‍⭐️
- •How large should be N for our bag of words when using N-grams? ‍⭐️
- •What is TF-IDF? How is it useful for text classification? ‍⭐️
- •Which model would you use for text classification with bag of words features? ‍⭐️
- •Would you prefer gradient boosting trees model or logistic regression when doing text classification with bag of words? ‍⭐️
- •What are word embeddings? Why are they useful? Do you know Word2Vec? ‍⭐️
- •Do you know any other ways to get word embeddings?
- •If you have a sentence with multiple words, you may need to combine multiple word embeddings into one. How would you do it? ‍⭐️
- •Would you prefer gradient boosting trees model or logistic regression when doing text classification with embeddings? ‍⭐️
- •How can you use neural nets for text classification?
- •How can we use CNN for text classification?

Clustering

- •What is unsupervised learning?
- •What is clustering? When do we need it?
- •Do you know how K-means works? ‍⭐️
- •How to select K for K-means? ‍⭐️
- •What are the other clustering algorithms do you know? ‍⭐️
- •Do you know how DBScan works? ‍⭐️
- •When would you choose K-means and when DBScan? ‍⭐️

Dimensionality reduction

- •What is the curse of dimensionality? Why do we care about it? ‍⭐️
- •Do you know any dimensionality reduction techniques? ‍⭐️
- •What’s singular value decomposition? How is it typically used for machine learning? ‍⭐️

Ranking and search

- •What is the ranking problem? Which models can you use to solve them? ‍⭐️
- •What are good unsupervised baselines for text information retrieval? ‍⭐️
- •How would you evaluate your ranking algorithms? Which offline metrics would you use? ‍⭐️
- •What is precision and recall at k? ‍⭐️
- •What is mean average precision at k? ‍⭐️
- •How can we use machine learning for search? ‍⭐️
- •How can we get training data for our ranking algorithms? ‍⭐️
- •Can we formulate the search problem as a classification problem? How? ‍⭐️
- •How can we use clicks data as the training data for ranking algorithms?
- •Do you know how to use gradient boosting trees for ranking?
- •How do you do an online evaluation of a new ranking algorithm? ‍⭐️

Recommender systems

- •What is a recommender system?
- •What are good baselines when building a recommender system? ‍⭐️
- •What is collaborative filtering? ‍⭐️
- •How we can incorporate implicit feedback (clicks, etc) into our recommender systems? ‍⭐️
- •What is the cold start problem? ‍⭐️
- •Possible approaches to solving the cold start problem? ‍⭐️

Time series

- •What is a time series?
- •How is time series different from the usual regression problem?
- •Which models do you know for solving time series problems? ‍⭐️
- •If there’s a trend in our series, how we can remove it? And why would we want to do it? ‍⭐️
- •You have a series with only one variable “y” measured at time t. How do predict “y” at time t+1? Which approaches would you use? ‍⭐️
- •You have a series with a variable “y” and a set of features. How do you predict “y” at t+1? Which approaches would you use? ‍⭐️
- •What are the problems with using trees for solving time series problems? ‍⭐️

That was a long list! I hope you found it useful. Good luck with your interviews!

The post is based on [this thread on Twitter](https://twitter.com/Al_Grigor/status/1230818076578459649). Do you know the answers? Consider contributing to [this github repository](https://github.com/alexeygrigorev/data-science-interviews/blob/master/theory.md)!

## Tags

 [#Machine Learning](https://hackernoon.com/tagged/machine-learning)  [#Data Science](https://hackernoon.com/tagged/data-science)  [#Interview Questions](https://hackernoon.com/tagged/interview-questions)  [#Careers](https://hackernoon.com/tagged/careers)  [#Tech Careers](https://hackernoon.com/tagged/tech-careers)  [#Coding Interviews](https://hackernoon.com/tagged/coding-interviews)  [#Recruiting](https://hackernoon.com/tagged/recruiting)  [#Hackernoon Top Story](https://hackernoon.com/tagged/hackernoon-top-story)

# Comments

 [Continue the Discussion **](https://community.hackernoon.com/t/35389)