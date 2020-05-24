How to export a BigQuery ML model and deploy it for online prediction

# How to export a BigQuery ML model and deploy it for online prediction

## Exporting a BigQuery ML model in TensorFlow SavedModel format and deploying to Cloud AI Platform Predictions

[![2*TveVoapl-TEk-jBTrbis8w.jpeg](../_resources/e0667f99a34a0e07e07c4d841ae06366.jpg)](https://towardsdatascience.com/@lakshmanok?source=post_page-----a7e4d44c4c93----------------------)

[Lak Lakshmanan](https://towardsdatascience.com/@lakshmanok?source=post_page-----a7e4d44c4c93----------------------)

[May 18](https://towardsdatascience.com/how-to-export-a-bigquery-ml-model-and-deploy-it-for-online-prediction-a7e4d44c4c93?source=post_page-----a7e4d44c4c93----------------------) · 3 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='bo js-evernote-checked' data-evernote-id='243'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='244' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/a7e4d44c4c93/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='bo js-evernote-checked' data-evernote-id='252'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='253' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/a7e4d44c4c93/share/facebook?source=post_actions_header---------------------------)

In this article, I will show you to export a BigQuery ML model into TensorFlow’s SavedModel format. This will allow you to deploy the model into any environment that supports TensorFlow Serving. I’ll demonstrate this using Cloud AI Platform Predictions, and show you how to invoke the online prediction.

## 1. Train a BigQuery ML model

First, of course, we need a BigQuery ML model. For simplicity, I’ll use a simple linear model on the same London Bicycles dataset used in our book “[BigQuery: The Definitive Guide](https://www.amazon.com/Google-BigQuery-Definitive-Warehousing-Analytics/dp/1492044466)”.

![1*RLLDTbxQ14iLPdwS6VOd9A.jpeg](../_resources/96f45d5586a727b5e7ac6df51959a034.jpg)
![1*RLLDTbxQ14iLPdwS6VOd9A.jpeg](../_resources/4029d58cd2e1afb6bd9a8ced3fb4709e.jpg)

First, create a dataset in the EU location to hold the trained model (you can run this command in CloudShell, or you can do this from the BigQuery console; just make sure to select EU as the location):

bq show ch09eu || bq mk --location=EU ch09eu
Next, run this query in the BigQuery console:
CREATE OR REPLACE MODEL ch09eu.bicycle_model_linear
OPTIONS(input_label_cols=['duration'], model_type='linear_reg')
ASSELECT
duration
, start_station_name

, IF(EXTRACT(dayofweek FROM start_date) BETWEEN 2 and 6, 'weekday', 'weekend') as dayofweek

, FORMAT('%02d', EXTRACT(HOUR FROM start_date)) AS hourofday
FROM `bigquery-public-data`.london_bicycles.cycle_hire

This creates a model called bicycle_model_linear which takes 3 inputs (start_station_name, dayofweek, hourofday) to predict the duration in seconds.

## 2. Try out a batch prediction in SQL

Let’s try invoking the model in BigQuery itself. To do that, run this query:
SELECT * FROM ML.PREDICT(MODEL ch09eu.bicycle_model_linear,(
SELECT
'Vauxhall Cross, Vauxhall' AS start_station_name
, 'weekend' as dayofweek
, '17' AS hourofday)
)
This returns:
![1*dU-Xksy8FE1tBvhP5i3P2Q.png](../_resources/d742c7b2909f43355b9d41e19c8dc084.png)
![1*dU-Xksy8FE1tBvhP5i3P2Q.png](../_resources/b52ca6a4a19ce06457d75c0abadb5c75.png)

As you can see, the predicted duration for a ride that starts in Vauxhall at 5pm on a weekend is 1329 seconds.

## 3. Export the model to Google Cloud Storage

Let’s download the model from BigQuery as a TensorFlow SavedModel. To do that, run these commands from CloudShell:

PROJECT=$(gcloud config get-value project)
BUCKET=${PROJECT}-eu
gsutil mb -l eu gs://${BUCKET}
bq extract -m ch09eu.bicycle_model_linear \
gs://${BUCKET}/bqml_model_export/bicycle_model_linear

What the command does is to create a bucket named xyz-eu where xyz is your project name. Then, we invoke bq extract to export the model to GCS.

When the command finishes, check what files have been exported:
gsutil ls gs://${BUCKET}/bqml_model_export/bicycle_model_linear/
When I did it, I got:
gs://ai-analytics-solutions-eu/bqml_model_export/bicycle_model_linear/

gs://ai-analytics-solutions-eu/bqml_model_export/bicycle_model_linear/saved_model.pb

gs://ai-analytics-solutions-eu/bqml_model_export/bicycle_model_linear/assets/

gs://ai-analytics-solutions-eu/bqml_model_export/bicycle_model_linear/variables/

This is the TensorFlow SavedModel format. You can deploy it to any TF Serving environment for online prediction. On GCP, the fully managed serving environment for TensorFlow/xgboost/PyTorch/etc. models is Cloud AI Platform (CAIP) Predictions.

## 4. Deploy the model to Cloud AI Platform predictions

To deploy the model, [download deploy.sh from the GitHub](https://github.com/GoogleCloudPlatform/bigquery-oreilly-book/blob/master/blogs/bqml_model_export/deploy.sh) repository for the book and run it:

./deploy.sh gs://${BUCKET}/bqml_model_export/bicycle_model_linear \
europe-west1 london_bicycles bqml

What deploy.sh does is to create a model and model version in CAIP Predictions and then deploy to it.

Deploying the model can take 4–5 minutes, so monitor [https://console.cloud.google.com/ai-platform/models/london_bicycles/versions](https://console.cloud.google.com/ai-platform/models/$MODEL_NAME/versions) to make sure that the model is deployed before going to the next step.

## 5. Try out online predictions

Create a file named input.json with the input we want to send the model. You can do this from CloudShell by typing in:

cat > input.json
Then, at the prompt, type in:

{"start_station_name": "Vauxhall Cross, Vauxhall", "dayofweek": "weekend", "hourofday": "17"}

Finally, hit Ctrl-D to get back to the prompt.
Send input.json to CAIP Predictions using:
gcloud ai-platform predict --model london_bicycles \
--version bqml --json-instances input.json
When I did this, I got back:
PREDICTED_LABEL
[1329.178180269723]

This is the same duration that we got when we did batch prediction in BigQuery ML.

CAIP Predictions exposes a REST API that takes JSON and so it can be invoked from any language that can make a web service call.

Enjoy!

## Next steps:

1. Check out the [queries and code](https://github.com/GoogleCloudPlatform/bigquery-oreilly-book/tree/master/blogs/bqml_model_export) on GitHub.

2. Read our [book on BigQuery](https://www.amazon.com/Google-BigQuery-Definitive-Warehousing-Analytics/dp/1492044466)

3. Check out the [documentation](https://cloud.google.com/bigquery-ml/docs/exporting-models) and [tutorial](https://cloud.google.com/bigquery-ml/docs/export-model-tutorial) on model export