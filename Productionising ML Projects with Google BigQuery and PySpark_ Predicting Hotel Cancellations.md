Productionising ML Projects with Google BigQuery and PySpark: Predicting Hotel Cancellations

# Productionising ML Projects with Google BigQuery and PySpark: Predicting Hotel Cancellations

## All too often, data scientists get caught up in the exploratory phase of data science — i.e. running multiple models on a particular dataset and optimising for accuracy.

[![1*Q6Sw7SNJts1yA8DH5jvKLQ.jpeg](../_resources/be070635a3fcb8396a95e19b374a2ad1.jpg)](https://towardsdatascience.com/@firstclassanalyticsmg?source=post_page-----8bf94fdc4af----------------------)

[Michael Grogan (MGCodesandStats)](https://towardsdatascience.com/@firstclassanalyticsmg?source=post_page-----8bf94fdc4af----------------------)

[Apr 18](https://towardsdatascience.com/productionising-ml-projects-with-google-bigquery-and-pyspark-predicting-hotel-cancellations-8bf94fdc4af?source=post_page-----8bf94fdc4af----------------------) · 4 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='195'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='196' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='201'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='202' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/8bf94fdc4af/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='210'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='211' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/8bf94fdc4af/share/facebook?source=post_actions_header---------------------------)

The exploratory phase of machine learning is undoubtedly important. Making sure that a model runs correctly and has predictive power is necessary before investing significant time and resources into the production process.

However, there is always the risk of spending too much time on this phase and not enough on production. That is to say, collating data from multiple sources and making sure that the infrastructure is suitable for working with large data streams.

Here is an example of an ML pipeline built for predicting hotel cancellations with a Gradient Boosting Classifier. Two models for two different hotels (H1 and H2) are built and run in this example.

# Pipeline

Specifically, the pipeline is set up as follows:

1. The hotel cancellation table is downloaded from a Google BigQuery database into a Jupyter Notebook with pythonbq — a Python client for BigQuery.

2. A Spark session is initialised using pyspark. The relevant data transformations are conducted to allow the GBTClassifier to work with the relevant data.

3. An 80/20 train-test split is conducted to allow the model to assess performance on an unseen portion of the training set.

4. Model predictions are converted from a Spark to pandas Data Frame, and then exported to CSV. These predictions are then read back into the Jupyter Notebook, and a confusion matrix is generated to assess model accuracy.

![0*Najj05v0KWuh7G12.png](../_resources/e767f663e8d0b0f37925a9e8151e451c.png)
![0*Najj05v0KWuh7G12.png](../_resources/b3f551548721f7f62b50073b285ed179.png)

# Google BigQuery

Firstly, the relevant CSV file for H1 can be uploaded to a Google BigQuery and stored as a table.

![0*S5zkQlNeJmBZonEu.png](../_resources/261d888dbc621c259000827a86c1e074.png)
![0*S5zkQlNeJmBZonEu.png](../_resources/4577120a20222e1ac5a1c52c955fe99e.png)
Source: Google BigQuery

In this case, the “Automatically Detect” option for Schema is selected, and the table is generated.

Here is the table as displayed in Google BigQuery:
![0*7G3Db-DG4agaTqv-.png](../_resources/16ea248a3194ebacda0f38dac9ec6865.png)
![0*7G3Db-DG4agaTqv-.png](../_resources/e1d63f1d6cb57549a695d205b463820c.png)
Source: Google BigQuery

# Interaction with Pyspark

Spark is specifically designed for handling “big data”. While the size of the datasets in this example are still of a suitable size to be run with models inherent to Python itself, one assumes that as more data is added to the database, it will eventually be necessary to use Spark in order to efficiently process these big data batches. Moreover, Spark is better suited to working with data that is being streamed and updated constantly.

A Spark session is initialised with pyspark, and pythonbq is used to load data from BigQuery:

import pyspark
conf = pyspark.SparkConf()conf.set('spark.local.dir', 'path')

sc = pyspark.SparkContext(conf=conf)from pythonbq import pythonbqmyProject=pythonbq(

bq_key_path='json_file',
project_id='project_id'
)
Here is a display of the table in Jupyter Notebook:
![1*Ylcwc0CDJCA0CwWs_2iHxw.png](../_resources/0897cb09f270c6fc29d15a067051a370.png)
![1*Ylcwc0CDJCA0CwWs_2iHxw.png](../_resources/f65cfbfe4b353a927c1bd558721653fa.png)
The relevant features and output label are loaded:
from pyspark.ml import Pipeline

from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler

categoricalColumns = ["Country", "MarketSegment", "ArrivalDateMonth", "DepositType", "CustomerType"]stages = []

for categoricalCol in categoricalColumns:

stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + "Index")

encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])

stages += [stringIndexer, encoder]label_stringIdx = StringIndexer(inputCol="IsCanceled", outputCol="label")

stages += [label_stringIdx]numericCols = ["LeadTime", "ArrivalDateYear", "ArrivalDateWeekNumber", "ArrivalDateDayOfMonth", "RequiredCarParkingSpaces"]

assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler]

# GBTClassifier

The GBTClassifier (or Gradient Boosting Classifier) can now be loaded for training with the relevant data.

from pyspark.ml.classification import GBTClassifier

partialPipeline = Pipeline().setStages(stages)
pipelineModel = partialPipeline.fit(dataset)
preppedDataDF = pipelineModel.transform(dataset)gbtClassifier = GBTClassifier()
trainedModel = gbtClassifier.fit(preppedDataDF)

Upon splitting the data 80% training and 20% test, the classifier can be trained.

gbtModel = gbtClassifier.fit(trainingData)
predictions = gbtModel.transform(testData)
selected = predictions.select("label", "prediction", "probability")
Let’s evaluate the model.
from pyspark.ml.evaluation import BinaryClassificationEvaluator
evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction")
evaluator.evaluate(predictions)
The model returns an evaluation of 0.9131.

The predictions can now be converted into a Pandas dataframe and exported to CSV:

selected.toPandas().to_csv('h1predictions.csv')

Upon importing the predictions once again, here is a confusion matrix with the results.

![0*2_jmSq5piwGOFJ3-.png](../_resources/76e0104cab9562caf24c40963ebcc16e.png)
![0*vf6zVG60E3kqKjQa.png](../_resources/99e2ff4673319a70837faf3a8021ffc8.png)

Overall f1-score accuracy is 84%, while a recall of 66% indicates that the model correctly identifies 66% of customers who cancel their hotel booking.

The same procedure is run for the H2 table — here are the confusion matrix results.

![0*vf6zVG60E3kqKjQa.png](../_resources/a3e49aa2e9ef87e234b8831430272749.png)
![0*2_jmSq5piwGOFJ3-.png](../_resources/249ae455b8024cfa461896aae4b0f834.png)
The f1-score accuracy comes in at 94%, while recall comes in at 79%.

# Conclusion

In this example, we have seen:

- How to populate a table in Google BigQuery
- Interact a Jupyter Notebook with a BigQuery database
- Implement a Gradient Boosting Classifier using pyspark.ml

Many thanks for your time — any thoughts or feedback are greatly appreciated!

The relevant GitHub repository for this example can be found [here](https://github.com/MGCodesandStats/hotel-modelling/tree/master/notebooks%20and%20datasets/spark), and you can also find more of my data science content at [michael-grogan.com](https://michael-grogan.com/).