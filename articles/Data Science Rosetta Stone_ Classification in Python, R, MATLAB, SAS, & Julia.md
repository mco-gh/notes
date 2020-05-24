Data Science Rosetta Stone: Classification in Python, R, MATLAB, SAS, & Julia

#  Data Science Rosetta Stone: Classification in Python, R, MATLAB, SAS, & Julia

 [2017-08-17](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html)

 [datascience](http://www.heatonresearch.com/categories/datascience/)

The discovery of the [Rosetta Stone](https://en.wikipedia.org/wiki/Rosetta_Stone) in 1799 allowed scholars to finally decipher ancient [Egyptian hieroglyphics](https://en.wikipedia.org/wiki/Egyptian_hieroglyphs). The actual content of the Rosetta stone is a very mundane government decree issued by the Egyptian government around 196 BC. The importance of the Rosetta stone is that this mundane decree was written in Ancient Egyptian using both hieroglyphic script and Demotic script, as well as Ancient Greek. The Ancient Greek allowed the translation of the Egyptian hieroglyphics. Sometimes it helps to see what you do not understand represented as what you do understand. The Rosetta Stone has become a metaphor for that which allows the decoding of something else.

![Computer Science Big-O Chart in R](../_resources/679971ae9b049bd169f34fe043f5980c.png)

This article attempts a “Rosetta stone” of data science by showing a simple classification in the following languages:

- [Python](https://www.continuum.io/downloads) - I use Anaconda Python.
- [R](https://www.r-project.org/about.html)
- [MATLAB](https://www.mathworks.com/) - See [Octave](https://www.gnu.org/software/octave/) for a free alternative.
- [SAS](https://www.sas.com/en_us/software/university-edition.html) - I used the free University edition.
- [Julia](https://julialang.org/)

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Titanic-Classification-Problem)Titanic Classification Problem

We will begin with a simple data science classification problem. Classification is where you would like the model to learn to identify a non-numeric outcome for input data. In this case, we would like to input information about passengers on the [RMS Titanic](https://en.wikipedia.org/wiki/RMS_Titanic) and get a prediction on if that passenger might survive. This is a binomial/binary prediction because there are two outcomes: survive (1) or perish (0). To perform this classification a GLM [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression) is used. This technique achieves approximately an 80% accuracy rate.

Considering the pandemonium that was the final hours of the RMS Titanic, an 80% accuracy rate is decent. Given the limited information on the passengers, you simply can’t predict everything. There will always be noise. Generally females had a much higher probability of survival than males. For females the class of their ticket was the second most important factor in survival. For males, *age* was the second most important factor. However, there is always noise/outliers. Consider [Miss Helen Loraine Allison](https://www.encyclopedia-titanica.org/titanic-victim/loraine-allison.html), a female 1st class passenger age 2. Simply by the numbers, she should have survived. But she did not. Somehow she was separated from her parents in the pandemonium that was the sinking Titanic. Trying to predict Helen’s death is not constructive. Similarly, [Mr. Karl Edwart Dahl](https://www.encyclopedia-titanica.org/titanic-survivor/charles-edward-dahl.html), a male 3rd class passenger age 45. Simply by the numbers, he should have died. But he did not. Likewise, trying to predict cases like Mr. Dahl is simply not productive. An 80% accuracy rate for Titanic is not bad.

The model used in these examples is a Logistic regression. There are more complex models, such as random forests, gradient boosted machines, or deep neural networks. However, because the purpose of this article is to highlight the languages, a relatively simple model was chosen.

Some common features to all languages will be mentioned here:

- **Age** - There are a number of missing ages. The Kaggle Titanic tutorial participants have found some very clever means of estimating missing ages. However, for this simple example we will simply fill in all missing ages with the median of the age.
- **Embarked** - There are two records where the port that the passenger embarked from is missing. These are simply filled in as the most common port (Southampton). Also, the three departure ports in Europe are encoded into dummy variables.
- **Dropped Fields** - The fields ‘Name’, ‘PassengerId’, ‘Ticket’, ‘Cabin’ are all dropped because they are not particularly predictive. Several published solutions do increase accuracy by using these fields. However, to keep this example relatively simple we will not use them.
- **Crossvalidation** - The data are split into a training set and validation set. The model is trained using the training set and evaluated using the validation set. This gives a better indication of how accurate the model is by evaluating it on data that it had not seen during training.

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Titanic-in-Python)Titanic in Python

The first language provided is Python 3.x. Python is a general purpose programming language that is widely used both by data scientists and software developers alike.

The first section simply imports the needed libraries and defines a convenience function that will encode dummy variables. [Pandas](http://pandas.pydata.org/) is used for all data preprocessing.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | import pandas as pd<br>import os<br>import numpy as np<br>from sklearn import metrics<br>from scipy.stats import zscore<br>path = "./data/"<br>def  encode_text_dummy(df, name):<br>dummies = pd.get_dummies(df[name])<br> for x in dummies.columns:<br>dummy_name = "{}-{}".format(name, x)<br>df[dummy_name] = dummies[x]<br>df.drop(name, axis=1, inplace=True) |

Next, we load the data set CSV and perform the preprocessing. Male and female are converted to 1 and 0. Some of the languages have a categorical type and do not require this conversion. *Embarked* is encoded to [dummies](https://en.wikipedia.org/wiki/One-hot) and missing values are filled in.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13 | filename_read = os.path.join(path,"titanic-dataset.csv")<br>df = pd.read_csv(filename_read,na_values=['NA','?'])<br>df.drop('Name',1,inplace=True)<br>df.drop('PassengerId',1,inplace=True)<br>df.drop('Ticket',1,inplace=True)<br>df.drop('Cabin',1,inplace=True)<br>df['Sex'].replace('female', 0,inplace=True)<br>df['Sex'].replace('male', 1,inplace=True)<br>med = df['Age'].median()<br>df['Age'].fillna(med,inplace=True)<br>df['Embarked'].fillna('S',inplace=True)<br>encode_text_dummy(df,'Embarked') |

Next, the data are setup for the logistic regression. Python requires that the predictors (*x*) be separated from the target (*y*). The target is whether the person survived or not. The predictors are all of the other values used to determine survival. Some languages will allow us to keep the predictors and target together. We also split the training and validation sets.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | from sklearn.linear_model import LogisticRegression<br>from sklearn.model_selection import train_test_split<br>x = df.as_matrix(['Pclass','Sex','Age','SibSp','Parch','Fare',<br> 'Embarked-C','Embarked-Q','Embarked-S'])<br>y = np.ravel(df.as_matrix(['Survived']))<br>x_train, x_test, y_train, y_test = train_test_split(<br>x, y, test_size=0.25, random_state=42) |

Next we setup the Logistic regression classifier and **fit** the model to the training set.

|     |     |
| --- | --- |
| 1<br>2<br>3 | classifier = LogisticRegression()<br>classifier.fit(x_train,y_train) |

Finally, we evaluate the accuracy of the model by having it predict the validation set.

|     |     |
| --- | --- |
| 1<br>2<br>3 | pred = classifier.predict(x_test)<br>score = metrics.accuracy_score(y_test, pred)<br>print("Accuracy score: {}".format(score)) |

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Titanic-in-R)Titanic in R

R and Python are the two heavyweights of open source data science. [According to KDDNuggets](http://www.kdnuggets.com/2016/06/r-python-top-analytics-data-mining-data-science-software.html), R is the most popular programming language for data science – but it is pretty close. R does win the award for the shortest program in this article. The small size of the R source code is a result of several sets that R handles for you.

The first section loads the data file and preprocesses the code.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | df = read.csv("./data/titanic-dataset.csv", header = TRUE)<br>drops <- c("PassengerId","Name", "Ticket", "Cabin")<br>df <- df[ , !(names(df) %in% drops)]<br>df$Age[is.na(df$Age)] <- median(df$Age, na.rm=TRUE)<br>df$Age[is.na(df$Embarked)] <- 'S' |

You will notice that unlike Python, R allows the *x* and *y* values to remain in the same dataframe. Additionally, there is no need to encode *sex* or *embarked*, because R loaded these values as factors (categoricals) and they are automatically encoded.

Next the training and validation sets are split.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | smp_size <- floor(0.75 * nrow(df))<br>set.seed(42)<br>train_ind <- sample(seq_len(nrow(df)), size = smp_size)<br>train <- df[train_ind, ]<br>test <- df[-train_ind, ] |

The Logistic regression model is created. R allows more of the GLM inner-workings to be specified than Python. Below you can see that we specify both the family (binomial, which means there are two outputs). Additionally, the link function is the logit, or logistic function.

|     |     |
| --- | --- |
| 1   | model <- glm(Survived ~.,family=binomial(link='logit'),data=train) |

The predictions are made. These predictions are all probabilities of survival. The **round** function ensures that any prediction >0.5 is treated as survival. Finally, the accuracy is calculated and displayed.

|     |     |
| --- | --- |
| 1<br>2<br>3 | pred <- predict(model,newdata=test,type='response')<br>pred_survived <- round(pred)<br>sprintf( "Accuracy: %f", sum(pred_survived == test$Survived) / nrow(test) ) |

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Titanic-in-MATLAB)Titanic in MATLAB

MATLAB is a commercial programming language that is favored by many areas of academia and industry. My primary exposure to MATLAB was in academia. I used MATLAB for several classes as an undergraduate. My phd advisor used MATLAB for many of his projects. The [free programming language Octave](https://www.gnu.org/software/octave/) is somewhat compatible with MATLAB.

In MATLAB, everything is a matrix. A single integer is just a matrix of height and width of 1. Semicolons tell MATLAB if you want the return value printed. A semicolon will suppress output to the console of the return value of a function. Julia makes similar use of the semicolon.

Like the previous examples, the first step is to load and preprocess the data. MATLAB does have a categorical type, and we use it for both *Embarked* and *Sex*. However, we will still need to encode these values. Unlike R, dummy variables are not automatically created for us.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10 | % Load the data<br>ds = readtable('titanic-dataset.csv');<br>% Handle missing ages<br>ds.Age(isnan(ds.Age)) = nanmean(ds.Age);<br>% Handle categoricals<br>ds.Embarked = categorical(ds.Embarked);<br>t = dummyvar(categorical(ds.Sex));<br>ds.Sex = t(:,1); |

MATLAB, just like Python, requires that the *x* and *y* be split into two variables.

|     |     |
| --- | --- |
| 1<br>2<br>3 | % Split X & Y.<br>y = ds(:,'Survived');<br>x = ds(:,{'Pclass','Sex','Age','SibSp','Parch','Fare'}); |

The dummy variables for *Embarked* are concatenated into the matrix.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | % Create training matrix (all numeric)<br>x = table2array(x);<br>x = horzcat(x,dummyvar(ds.Embarked));<br>y = table2array(y); |

Next, the training and validation sets are split.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | % Training & validation split<br>[trainInd,valInd] = divideblock(length(x),0.7,0.3);<br>x_train = x(trainInd,:);<br>y_train = y(trainInd,:);<br>x_val = x(valInd,:);<br>y_val = y(valInd,:); |

Just like the previous examples, a binomial logist regression is created and fit to the training.

|     |     |
| --- | --- |
| 1<br>2 | % Fit the model<br>model = glmfit(x_train,y_train,'binomial','link','logit'); |

Finally, the validation set is used to create predictions and accuracy is evaluated.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | % Predict and calculate accuracy.<br>pred = glmval(model,x_val,'logit');<br>pred = round(pred);<br>acc = (pred == y_val);<br>sum(acc)/length(acc) |

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Titanic-in-SAS)Titanic in SAS

SAS is a commercial language used to create statistical models. The first thing that you will notice about SAS is that the two primary statement are **PROC** and **DATA**. Both the **PROC** and **DATA** statements are ended by a **RUN** statement. A SAS program is essentially made up of **PROC** and **DATA** statements that pass data sets between each other. The data set is the only object type and it is stored to disk at each step.

SAS programs can have other statements beyond **PROC** and **DATA**, such as a macro language. However, the macro language functions as macros and effectively repeats **PROC** and **DATA** segments of the source file. A **PROC** statement calls a predefined SAS function. A **DATA** statement loops over a data set and modifies it.

The first step is to read in the CSV file. The **OUT** parameter specifies that the CSV file will be stored in a temporary binary file named train. Because SAS performs all operations on binary files, it does not require that everything fit into RAM. All of the other language examples from this article require everything to fit into RAM.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | /* Read the CSV */<br>PROC IMPORT DBMS=csv OUT=train REPLACE<br>DATAFILE="/folders/myfolders/titanic-dataset.csv";<br>GETNAMES=YES;<br>RUN; |

Next, the missing ages are filled in with their median values. This is done with a **DATA** statement that loops over the train data set that was just loaded in. The resulting data set is written to the same data set as the source. The **DATA** parameter specifies the input and the **OUT** parameter specifies the output.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | /* Fill in missing ages with median */<br>PROC STDIZE DATA=train OUT=train<br>METHOD=median reponly;<br>VAR Age;<br>RUN; |

Next, we will separate the training and validation set. The first step is to add a column, named *selected* to the *train* data set that specifies if it is part of the ultimate training set or not. This is done by using **PROC SURVEYSELECT**, a total of 70% of the data will have a *selected* variable with a value of 1. The input and output data sets are both *train*. The previous *train* data set (which held all rows) is replaced by a new *train* data set that contains only the training data.

Once the *train* data set has been properly labeled, it is split into two data sets that are named *train* and *validate*.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13 | /* Train/Validate split */<br>PROC SURVEYSELECT DATA=train outall OUT=train METHOD=srs SAMPRATE=0.7;<br>RUN;<br>DATA validate;<br>SET train;<br>IF selected = 0;<br>RUN;<br>DATA train;<br>SET train;<br>IF selected = 1;<br>RUN; |

Now that we have a *train* and *validation* data set we are ready to fit the Logistic regression. This fitting is performed with **PROC LOGISTIC**. The two categorical values, *Sex* and *Embarked* must be specified with the **CLASS** parameters. The **ref** setting means to encode as dummy variables.

The formula that we are regressing is that *Survived* is equal to some regression of *Sex*, *Age*, *Pclass*, *Parch*, *SibSp*, and *Embarked*. The model parameters themselves are written to a binary file called *model*. The **descending** flag specifies that the model will predict values of 1 (survived), as opposed to 0 (perished).

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | /* Fit the logit */<br>PROC LOGISTIC data=train outmodel=model descending;<br>CLASS Sex / PARAM=ref ;<br>CLASS Embarked / PARAM=ref ;<br>MODEL Survived = Sex Age Pclass Parch SibSp Embarked;<br>RUN; |

Now that the model has been fit, we can predict with another call to **PROC LOGISTIC**. This will create a data set named *pred* that contains the *validate* data set augmented with predictions. Because we are predicting a binary outcome, two additional columns are added to the data set: *P_1* specifies the probability that the person survived and *P_2* specifies the probability that the person perished. These two values sum to 1.0 for each row.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | /* Predict */<br>PROC LOGISTIC INMODEL=model;<br>SCORE DATA=validate OUT=pred;<br>RUN; |

Next a prediction data set is created where any *Survived* probability is greater than or equal to 0.5 is assumed to have survived is created. Only the *PassengerId*, *Survived*, and *P_1* columns are kept. Additionally, a new column named *pred_survived* is created that holds a value of 1 if the probability of survival was greater or equal than 0.5.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | /* Turn prediction probabilities into class values (threshold=.5) */<br>DATA pred;<br>SET PRED(KEEP = PassengerId Survived P_1);<br>pred_survived = ROUND(P_1);<br>RUN; |

Finally, a [confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) is generated that measures model performance. This will tells us the percent of survived and perished predictions that were correct.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | /* Evaluate */<br>proc freq data=pred;<br>tables Survived * pred_survived;<br>run; |

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Titanic-in-Julia)Titanic in Julia

Julia is a relatively new programming language that the data science community is showing increased support for. Julia can use advanced linear algebra packages to perform matrix operations with great performance; however, loops and traditional programming constructs will also perform at near C/C++ speed.

The first step is to read the CSV file into a **DataFrame**.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | using DataFrames;<br>using GLM;<br>df = readtable("./data/titanic-dataset.csv"); |

The usual preprocessing steps are performed. In Julia you will notice that function names and operators sometimes have a prefix/suffix, such as **!** or **.**. The ! suffix, such as **delete!** notes that this function will modify what is passed to it. The **.** prefix/suffix, such as .~ means that the not(~) is applied to each member of the vector, not the whole vector.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | delete!(df, :PassengerId);<br>delete!(df, :Name);<br>delete!(df, :Ticket);<br>delete!(df, :Cabin);<br>df[isna.(df[:Age]),:Age] = median(df[ .~isna.(df[:Age]),:Age])<br>df[isna.(df[:Embarked]),:Embarked] = "S"<br>pool!(df, [:Sex]);<br>pool!(df, [:Embarked]); |

Next we split the training and validation sets into *df_train* and *df_validate*.

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | split_pt = trunc(Int,size(df,1)*0.7) # 70% validation<br>shuffle_idx = sample(1:size(df,1),size(df,1));<br>df_train = df[1:split_pt,:];<br>df_validate = df[split_pt+1:size(df,1),:]; |

The model is created and the validation set is scored for prediction. The formula of the regression uses the same regression format as R. The prediction probabilities are rounded, just like the other languages. This rounding means that probabilities of survival of 0.5 and higher indicate survived (1); whereas, 0 indicates perished.

|     |     |
| --- | --- |
| 1<br>2<br>3 | model = glm(@formula(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked), df_train, Binomial(), LogitLink());<br>pred = predict(model,df_validate);<br>pred = convert(DataArray{Int}, round.(pred)); |

Finally we can report the accuracy.

|     |     |
| --- | --- |
| 1<br>2 | print("Accuracy: ")<br>println( sum(pred .== df_validate[:Survived]) / length(pred)) |

# [(L)](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#Final-Remarks)Final Remarks

Now you have seen a simple Logistic regression in Python, R, MATLAB, SAS, and Julia. You can see some of the parallels and differences between the languages. Python and MATLAB require that *x* and *y* be split; whereas, the others do not. Julia and R use a similar regression formula format.

There are other languages that are used for data science. I tried to focus on the mainstream. In the future, I may augment this article with additional languages. Are there any that you would like to see? Java, Javascript, and C# are candidates, as they are more mainstream IT languages.

 [** Share]()  [** Comments](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html#disqus_thread)

- [**  What are Tensors and why are they Flowing? (TensorFlow)](http://www.heatonresearch.com/2017/07/30/tensors.html)