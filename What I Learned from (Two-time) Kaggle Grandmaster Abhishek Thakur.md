What I Learned from (Two-time) Kaggle Grandmaster Abhishek Thakur

# *What I Learned from (Two-time) Kaggle Grandmaster Abhishek Thakur*

## Drawing insights from Abhishek Thakur’s NLP kernel

[![2*6mthBDRDZ9d2PPiMsNKAXw.jpeg](../_resources/6ff16a3de606ecaac4d4c7a0eaf270c0.jpg)](https://towardsdatascience.com/@jds2be?source=post_header_lockup)

[Dean Sublett](https://towardsdatascience.com/@jds2be)

May 30·5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='118'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

![](../_resources/3849bb2f94327688cb8f1f0f7c530ba2.png)![0*8aBkyFnpHhxCu6eZ](../_resources/81beadcabf95c121043d64e87f3179c5.jpg)

Photo by [Georgie Cobbs](https://unsplash.com/@georgie_cobbs?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

#### **Quick Bio**

Before his many data scientist stints in companies scattered throughout Germany, Abhishek Thakur earned his bachelor’s in electrical engineering at NIT Surat and his master’s in computer science at the University of Bonn. Currently, he holds the title of Chief Data Scientist at Norway’s boost.ai, a “software company that specializes in conversational artificial intelligence (AI).” But I’m most impressed by Abhishek’s Kaggle clout.

You can visit his Kaggle profile [here](https://www.kaggle.com/abhishek). Here’s a snapshot of his accolades:

- •Competitions Grandmaster (17 gold medals and an all-time high rank of #3 in the world)
- •Kernels Expert (he’s well within the top 1% of Kagglers)
- •Discussion Grandmaster (65 gold medals and an all-time high rank of #2 in the world)

I want to take a look at Abhishek’s tutorial, [Approaching (Almost) Any NLP Problem on Kaggle](https://www.kaggle.com/abhishek/approaching-almost-any-nlp-problem-on-kaggle). I’ve selected this kernel of Abhishek’s because I myself have been trying to learn more about natural language processing, and how could I resist learning with Kaggle’s Halloween-themed [Spooky Authors](https://www.kaggle.com/c/spooky-author-identification/data) dataset?

#### **Abhishek’s Approach to NLP**

I would highly encourage you to read this article alongside the kernel. And if you really want a firmer grasp of NLP or data science in general, be sure that you understand *every* line of Abhishek’s code by writing it yourself as you go through his kernel.

Just so we don’t forget — our task is to identify the **author **(EAP — Edgar Allen Poe; HPL — H.P. Lovecraft; MWS — Mary Wollstonecraft Shelley) of each sentence in the test set.

**1. Exploring the Data and Understanding the Problem**

After importing the necessary Python modules and the data, Abhishek calls the head() method on the data to see what the first five rows look like. Since Abhishek is a pro and this is an NLP problem, the **exploratory data analysis **(you’ll most often see this referred to as EDA) is shallow compared to problems involving numerical data. Data science newcomers might benefit from more thorough EDA. A solid exploration of the data can expose any missing values, let you know how much data cleaning you’ll have to do, and help inform your model-building decisions later in the problem.

Abhishek also reminds us that we’re tackling a **multiclass text classification problem**. It’s always a good idea not to lose sight of what we’re trying to accomplish! He notes what evaluation metric Kaggle will use to score submissions. For this competition, Kaggle used **multiclass log loss** to measure the performance of submitted models. Ideally, our multiclass classification model would have a log loss of 0. Here’s more on [log loss](http://wiki.fast.ai/index.php/Log_Loss), if you’re interested.

**2. Preprocessing**

Next, Abhishek uses the LabelEncoder() method from scikit-learn to assign an integer value to each author. By encoding the text labels of values in the **author **column with**  **integer values (0, 1, 2), Abhishek is making the data easier for his classification model to understand.

After encoding the **author **labels, Abhishek splits the data into training and validation sets using train_test_split from scikit-learn. He opts for a 90:10 train/validation split (the most frequently utilized splits in Python data science typically range from 70:30 to 80:20). So he intends to train the models on 90% of the sentences in the dataset, and then he’ll evaluate the accuracy of his models on the remaining 10% of the data.

**3. Building a Model**

Before creating his first model, Abhishek uses TF-IDF (Term Frequency — Inverse Document Frequency) on the data. TF-IDF will give weights to the words that appear in the sentences in the **text **column. So TF-IDF will helps us understand what words are important when we are trying to determine which author wrote a particular sentence — words such as “the” won’t be important for classifying *any *author because “the” appears frequently and doesn’t reveal much information, but a word like “Cthulhu,” for example, would be very important when classifying sentences written by H.P. Lovecraft. More about TF-IDF can be found [here](https://en.m.wikipedia.org/wiki/Tf%E2%80%93idf) and [here](https://www.quora.com/How-does-TfidfVectorizer-work-in-laymans-terms).

Running this TF-IDF on the data is a form of **feature extraction**. Here, we needed to derive some sort of significant predictor or feature of the data that would help us figure out which author wrote a particular sentence. With TF-IDF, we have a statistical measure of a word’s importance that can help us predict the author of the sentence.

After fitting the TF-IDF on both the training and validation sets, Abhishek prepares a logistic regression model. If this type of classification model is new to you, read [this](https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8) before continuing. After fitting the logistic regression model, Abhishek calculates the log loss of his logistic regression model (recall that he wrote the multiclass log loss function near the beginning of the kernel). The multiclass log loss function returns a log loss value of *0.626* for the logistic regression model. Although fitting TF-IDF and a logistic regression model gave us a good start, we can improve on this log loss score.

**4. Model Tweaking**

So we’re not satisfied with a log loss score of *0.626* and want to optimize this evaluation metric. From here, we could take a number of routes, and that’s exactly what Abhishek does. After we’ve explored and preprocessed our data, we’re left with many different combinations of feature extraction and model fitting. For example, Abhishek uses word counts for feature extraction instead of TF-IDF. With this feature extraction technique, his logistic regression model’s log loss score improves from *0.626 *to *0.528* — a whopping *0.098* improvement!

### **Summary**

Since Abhishek’s kernel grows increasingly more detailed from this point, I’ll let him do the heavy lifting with explaining the other classification models.

Here’s what we discussed:

- •**EDA**: Exploratory data analysis is crucial if we want to understand the dataset, and EDA can save us time when we begin building models
- •**Multiclass classification problems**: This type of problem requires us to predict which observations fall into which class, where each observation could fall into any one class of three or more classes
- •**Preprocessing**: We have to preprocess our data before we build any models. In this example, we needed to use LabelEndcoder() to transform the text labels into integer values for the sake of our models
- •**Feature Extraction**: Whenever we have a dataset of raw data (sentence excerpts in our example), we’ll need to derive some predictor that can help us determine how to classify our observations. Abhishek showed us how to use TF-IDF and word counts

From here, it’s up to us to extract features with high predictive power and to pick models that match the problem and optimize the metric we’re concerned with. Don’t be afraid to get your hands dirty and experiment with several models — you’re likely to fit a model that optimizes your evaluation metric through more experimentation. I hope after reading this that you better understand how to approach an NLP problem and that you, too, appreciate Abhishek’s work.

#### **Appendix**

[Abhishek’s Kaggle profile](https://www.kaggle.com/abhishek)

[Abhishek’s NLP kernel](https://www.kaggle.com/abhishek/approaching-almost-any-nlp-problem-on-kaggle)

[Spooky Authors dataset](https://www.kaggle.com/c/spooky-author-identification/data)

[What is log loss?](http://wiki.fast.ai/index.php/Log_Loss)
[What is TF-IDF?](https://en.m.wikipedia.org/wiki/Tf%E2%80%93idf)

[TF-IDF in layman’s terms](https://www.quora.com/How-does-TfidfVectorizer-work-in-laymans-terms)

[What is logistic regression?](https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8)

Here is all of Abhishek’s code that is referred to in this article. I want to reiterate that this is *not *my own work — this gist is intended to help beginners follow along to Abhishek’s NLP tutorial.

![](../_resources/be992776413fdf5f3d86308782370674.png)

|     |     |
| --- | --- |
| 1   | #  NOTE: THIS IS NOT MY OWN WORK |
| 2   | # This gist is a collection of code from Abhishek Thakur's Kaggle NLP tutorial, which can be found here: |
| 3   | # https://www.kaggle.com/abhishek/approaching-almost-any-nlp-problem-on-kaggle |
| 4   |     |
| 5   | # 1. Exploring the Data and Understanding the Problem # |
| 6   | import pandas as pd |
| 7   | import numpy as np |
| 8   | import xgboost as xgb |
| 9   | from tqdm import tqdm |
| 10  | from sklearn.svm import  SVC |
| 11  | from keras.models import Sequential |
| 12  | from keras.layers.recurrent import  LSTM, GRU |
| 13  | from keras.layers.core import Dense, Activation, Dropout |
| 14  | from keras.layers.embeddings import Embedding |
| 15  | from keras.layers.normalization import BatchNormalization |
| 16  | from keras.utils import np_utils |
| 17  | from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline |
| 18  | from sklearn.model_selection import GridSearchCV |
| 19  | from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer |
| 20  | from sklearn.decomposition import TruncatedSVD |
| 21  | from sklearn.linear_model import LogisticRegression |
| 22  | from sklearn.model_selection import train_test_split |
| 23  | from sklearn.naive_bayes import MultinomialNB |
| 24  | from keras.layers import GlobalMaxPooling1D, Conv1D, MaxPooling1D, Flatten, Bidirectional, SpatialDropout1D |
| 25  | from keras.preprocessing import sequence, text |
| 26  | from keras.callbacks import EarlyStopping |
| 27  | from nltk import word_tokenize |
| 28  | from nltk.corpus import stopwords |
| 29  | stop_words = stopwords.words('english') |
| 30  |     |
| 31  | train = pd.read_csv('../input/train.csv') |
| 32  | test = pd.read_csv('../input/test.csv') |
| 33  | sample = pd.read_csv('../input/sample_submission.csv') |
| 34  |     |
| 35  | train.head() |
| 36  |     |
| 37  | test.head() |
| 38  |     |
| 39  | sample.head() |
| 40  |     |
| 41  | def  multiclass_logloss(actual, predicted, eps=1e-15): |
| 42  |  """Multi class version of Logarithmic Loss metric. |
| 43  | :param actual: Array containing the actual target classes |
| 44  | :param predicted: Matrix with class predictions, one probability per class |
| 45  |  """ |
| 46  |  # Convert 'actual' to a binary array if it's not already: |
| 47  |  if  len(actual.shape) ==  1: |
| 48  | actual2 = np.zeros((actual.shape[0], predicted.shape[1])) |
| 49  |  for i, val in  enumerate(actual): |
| 50  | actual2[i, val] =  1 |
| 51  | actual = actual2 |
| 52  |     |
| 53  | clip = np.clip(predicted, eps, 1  - eps) |
| 54  | rows = actual.shape[0] |
| 55  | vsota = np.sum(actual * np.log(clip)) |
| 56  |  return  -1.0  / rows * vsota |
| 57  |     |
| 58  | # 2. Preprocessing # |
| 59  | lbl_enc = preprocessing.LabelEncoder() |
| 60  | y = lbl_enc.fit_transform(train.author.values) |
| 61  |     |
| 62  | xtrain, xvalid, ytrain, yvalid = train_test_split(train.text.values, y, |
| 63  |  stratify=y, |
| 64  |  random_state=42, |
| 65  |  test_size=0.1, shuffle=True) |
| 66  | print (xtrain.shape) |
| 67  | print (xvalid.shape) |
| 68  |     |
| 69  | # 3. Building a Model # |
| 70  | # Always start with these features. They work (almost) everytime! |
| 71  | tfv = TfidfVectorizer(min_df=3, max_features=None, |
| 72  |  strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}', |
| 73  |  ngram_range=(1, 3), use_idf=1,smooth_idf=1,sublinear_tf=1, |
| 74  |  stop_words  =  'english') |
| 75  |     |
| 76  | # Fitting TF-IDF to both training and test sets (semi-supervised learning) |
| 77  | tfv.fit(list(xtrain) +  list(xvalid)) |
| 78  | xtrain_tfv = tfv.transform(xtrain) |
| 79  | xvalid_tfv = tfv.transform(xvalid) |
| 80  |     |
| 81  | # Fitting a simple Logistic Regression on TFIDF |
| 82  | clf = LogisticRegression(C=1.0) |
| 83  | clf.fit(xtrain_tfv, ytrain) |
| 84  | predictions = clf.predict_proba(xvalid_tfv) |
| 85  |     |
| 86  | print ("logloss: %0.3f  "  % multiclass_logloss(yvalid, predictions)) |
| 87  |     |
| 88  | # 4. Model Tweaking # |
| 89  | ctv = CountVectorizer(analyzer='word',token_pattern=r'\w{1,}', |
| 90  |  ngram_range=(1, 3), stop_words  =  'english') |
| 91  |     |
| 92  | # Fitting Count Vectorizer to both training and test sets (semi-supervised learning) |
| 93  | ctv.fit(list(xtrain) +  list(xvalid)) |
| 94  | xtrain_ctv = ctv.transform(xtrain) |
| 95  | xvalid_ctv = ctv.transform(xvalid) |
| 96  |     |
| 97  | # Fitting a simple Logistic Regression on Counts |
| 98  | clf = LogisticRegression(C=1.0) |
| 99  | clf.fit(xtrain_ctv, ytrain) |
| 100 | predictions = clf.predict_proba(xvalid_ctv) |
| 101 |     |
| 102 | print ("logloss: %0.3f  "  % multiclass_logloss(yvalid, predictions)) |

 [view raw](https://gist.github.com/deansublett/4ab9ed401a747188b199b37b835b4611/raw/d6de89ed889a1d50e53c4b4d8941893a70c1396f/abhishek_NLP.py)  [abhishek_NLP.py](https://gist.github.com/deansublett/4ab9ed401a747188b199b37b835b4611#file-abhishek_nlp-py) hosted with ❤ by [GitHub](https://github.com/)

Credit to Abhishek Thakur for this NLP tutorial