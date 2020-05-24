Tutorial: Implementing sci-kit learn’s Random Forest Classifier for the first time

[Josh Lawman](http://joshlawman.com/)

# Tutorial: Implementing sci-kit learn’s Random Forest Classifier for the first time

#### Published by [**Josh**](http://joshlawman.com/author/admin/) on September 18, 2017

This tutorial walks you through implementing sci-kit learn’s Random Forest Classifier on the Iris training set. It demonstrates the use of a few other functions from sci-kit learn such as train_test_split and classification_report.

Note: you will not be able to run the code unless you have sci-kit learn and pandas installed. If you don’t know how to do that or if you want to replicate the code yourself follow my tutorial to [set up Jupyter Notebook](http://joshlawman.com/getting-set-up-in-jupyter-notebooks-using-anaconda-to-install-the-jupyter-pandas-sklearn-etc/) first.

### 1. Import the dataset

We will be using the iris dataset (https://en.wikipedia.org/wiki/Iris_flower_data_set) to train our classifier. It comes preloaded with sci-kit learn (sklearn).

In [1]:
#Import datasetfrom  sklearn.datasets  import  load_irisiris  =  load_iris()

### 2. Prepare training and testing data

Each flower in this dataset contains the following features and labels

- features – measurements of the flower petals and sepals
- labels – the flower species (setosa, versicolor, or virginica) represented as a 0, 1, or 2.

Our train_test_split function will seperate the data as follows

- (features_train, labels_train) – 80% of the data prepared for training
- (features_test, labels_test) – 20% of the data prepared for making our predictions and evaluating our model

In [2]:
#Import train_test_splitfrom  sklearn.model_selection  import  train_test_split
In [3]:

features_train,  features_test,  labels_train,  labels_test  =  train_test_split(iris.data,iris.target,test_size=0.2,random_state=1)

### 3. Create and fit the Random Forest Classifier

This tutorial uses the RandomForestClassifier model for our predictions, but you can experiment with other classifiers. To do so, import another classifier and replace the relevant code in this section.

In [4]:
#Import classifierfrom  sklearn.ensemble  import  RandomForestClassifier
In [5]:

#Create an instance of the RandomForestClassifierrfc  =  RandomForestClassifier()

In [6]:

#Fit our model to the training features and labelsrfc.fit(features_train,labels_train)

Out[6]:
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
max_depth=None, max_features='auto', max_leaf_nodes=None,
min_impurity_decrease=0.0, min_impurity_split=None,
min_samples_leaf=1, min_samples_split=2,
min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
oob_score=False, random_state=None, verbose=0,
warm_start=False)

### 4. Make Predictions using Random Forest Classifier

In [7]:
rfc_predictions  =  rfc.predict(features_test)

* * *

**Understanding our predictions**

Our predictions will be an array of 0’s 1’s, and 2’s, depending on which flower our algorithm believes each set of measurements to represent.

In [8]:
print(rfc_predictions)

[0 1 1 0 2 1 2 0 0 2 1 0 2 1 1 0 1 1 0 0 1 1 2 0 2 1 0 0 1 2]

To intepret this, consider the first set of measurements in features_test:
In [9]:
print(features_test[0])

[ 5.8 4. 1.2 0.2]

Our model believes that these measurements correspond to a setosa iris (label 0).

In [10]:
print(rfc_predictions[0])

0

In this case, our model is correct, since the true label indicates that this was a setosa iris (label 0).

In [11]:
print(labels_test[0])

0

### 5. Evaluate our model

For this section we will import two metrics from sklearn: confusion_matrix and classification_report. They will help us understand how well our model did.

In [12]:

#Import pandas to create the confusion matrix dataframeimport  pandas  as  pd#Import classification_report and confusion_matrix to evaluate our modelfrom  sklearn.metrics  import  classification_report,  confusion_matrix

As seen in the confusion matrix below, most predictions are accurate but our model misclassified one specimen of versicolor (our model thought that it was virginca).

In [13]:

#Create a dataframe with the confusion matrixconfusion_df  =  pd.DataFrame(confusion_matrix(labels_test,  rfc_predictions),columns=["Predicted "  +  name  for  name  in  iris.target_names],index  =  iris.target_names)

In [14]:
confusion_df
Out[14]:

|     | Predicted setosa | Predicted versicolor | Predicted virginica |
| --- | --- | --- | --- |
| setosa | 11  | 0   | 0   |
| versicolor | 0   | 12  | 1   |
| virginica | 0   | 0   | 6   |

As seen in the classification report below, our model has 97% precision, recall, and accuracy.

In [15]:
print(classification_report(labels_test,rfc_predictions))

precision recall f1-score support
0 1.00 1.00 1.00 11
1 1.00 0.92 0.96 13
2 0.86 1.00 0.92 6
avg / total 0.97 0.97 0.97 30

* * *

### ** Note on the RandomForestClassifier from sklearn**

Documentation with full explanation of parameters and use: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html.

Some useful parameters to experiment with:

- min_samples_leaf (the minimum samles which can be put into each lef)
- n_estimators (the number of decision trains)
- max_features (the size of the subset of features to be examined at each split)

An optional feature to take advantage of:

- oob_score (a way of seeing how well the estimator did by cross-validiting on the “out of bag” data, i.e. the data

for each tree that was not used in the sample). This would be usefull if you didn’t want to split your dataset into a training dataset and a test dataset.

### Note on metrics

Check out wikipedia if confusion matrices are new (https://en.wikipedia.org/wiki/Confusion_matrix) or if you want explanation on precision and recall (https://en.wikipedia.org/wiki/Precision_and_recall).

Categories:[Algorithm Application](http://joshlawman.com/category/algorithm-application/)[sci-kit learn](http://joshlawman.com/category/sci-kit-learn/)

- [**](https://twitter.com/intent/tweet?url=http://joshlawman.com/implementing-the-random-forest-classifier-from-sci-kit-learn/&text=Tutorial:%20Implementing%20sci-kit%20learn%E2%80%99s%20Random%20Forest%20Classifier%20for%20the%20first%20time&hashtags=Algorithm%20Application,sci-kit%20learn)

* * *

###

### Leave a Reply

![](../_resources/888367cc7ae74ab0e323dff7e59830b2.jpg)

 Name *

 Email *

 Website

 What's on your mind?

 Notify me of follow-up comments by email.
 Notify me of new posts by email.

##### Categories

- [Algorithm Application](http://joshlawman.com/category/algorithm-application/)
- [Misc.](http://joshlawman.com/category/misc/)
- [sci-kit learn](http://joshlawman.com/category/sci-kit-learn/)

##### Recent Posts

- [Tutorial: Implementing sci-kit learn’s Random Forest Classifier for the first time](http://joshlawman.com/implementing-the-random-forest-classifier-from-sci-kit-learn/)
- [Getting set-up in Jupyter Notebooks (using Anaconda to install Jupyter, Pandas, SKLearn, etc)](http://joshlawman.com/getting-set-up-in-jupyter-notebooks-using-anaconda-to-install-the-jupyter-pandas-sklearn-etc/)
- [Coming soon](http://joshlawman.com/coming-soon/)

[![](../_resources/553f91dbd9891d59c0f9c5f7a212e62f.png)   ](http://joshlawman.com/implementing-the-random-forest-classifier-from-sci-kit-learn/mailto:jlawman@gmail.com)[![](../_resources/8740fd404314496220b64e12477fbac9.png)   ](https://www.linkedin.com/in/josh-lawman-9b2604136/)[![](../_resources/dcb05e67e1dc5a641fdc4d993e4e3b5e.png) ](https://github.com/jlawman)   [![](../_resources/5014e3bc7b236f3e7c95a62e8784e268.png)](https://twitter.com/joshlawman)