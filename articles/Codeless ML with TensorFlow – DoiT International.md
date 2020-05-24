Codeless ML with TensorFlow – DoiT International

# Codeless ML with TensorFlow

[![1*sKREfePenX4FxtYE5wFwgw.jpeg](../_resources/150c8ef6b72a17c3c22d1468c10caf35.jpg)](https://blog.doit-intl.com/@gidutz?source=post_header_lockup)

[Gad Benram](https://blog.doit-intl.com/@gidutz)

Jul 2·3 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='89'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

*Advances in AI frameworks enable developers to create and deploy deep learning models with as little effort as clicking a few buttons on the screen. Using a UI or an API based on Tensorflow Estimators, models can be built and served without writing a single line of machine learning code.*

![](../_resources/02621c92bcc772ed3fe5d8772dc54505.png)![0*RyyK3bja967kHYim](../_resources/39356a17199af1f48ab34e1755f98e23.jpg)

Photo by [Adi Goldstein](https://unsplash.com/@adigold1?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

70 years ago, only a handful of experts knew how to create computer programs, because the process of programming required very high theoretical and technical specialization. Over the years, humans have created increasingly higher levels of abstraction and encapsulation of programming, allowing less-skilled personnel to create software with very basic tools (see[Wix](https://www.wix.com/) for example). The exact same process occurs these days with machine learning — only it advances extremely faster. In this blog post we will write down a simple script that will generate a full machine learning pipeline.

### Truly codeless?

This post contains two types of code. The first is a SQL query to generate the dataset — this is the part of the code could be replaced by tools like [Google Cloud Dataprep](https://cloud.google.com/dataprep/). The other type involves API calls using a Python client library — all of these actions are available through the AI platform UI. When I say codeless, I mean that at no point will you need to import TensorFlow or other ML libraries.

In this demo, I will use the[Chicago Taxi Trips](https://console.cloud.google.com/marketplace/details/city-of-chicago-public-data/chicago-taxi-trips) open dataset in Google BigQuery to predict the travel time of a taxi based on pickup location, desired drop-off, and the time of ride start. The model will be trained and deployed using Google Cloud services that wrap Tensorflow.

The entire code sample can be found in[this GitHub repository.](https://github.com/doitintl/ml-specialization-examples/tree/master/chicago_travel_time)

### Extract Features using BigQuery

Based on an EDA shown[in this notebook](https://github.com/doitintl/ml-specialization-examples/blob/master/chicago_travel_time/EDA.ipynb), I created a SQL query to generate a training dataset:

|     |     |
| --- | --- |
| 1   | WITH dataset AS( SELECT |
| 2   |     |
| 3   | EXTRACT(HOUR FROM trip_start_timestamp) trip_start_hour |
| 4   | , EXTRACT(DAYOFWEEK FROM trip_start_timestamp) trip_start_weekday |
| 5   | , EXTRACT(WEEK FROM trip_start_timestamp) trip_start_week |
| 6   | , EXTRACT(DAYOFYEAR FROM trip_start_timestamp) trip_start_yearday |
| 7   | , EXTRACT(MONTH  FROM trip_start_timestamp) trip_start_month |
| 8   | , (trip_miles *  1.60934 ) / ((trip_seconds + .01) / (60  *  60)) trip_speed_kmph |
| 9   | , trip_miles |
| 10  | , pickup_latitude |
| 11  | , pickup_longitude |
| 12  | , dropoff_latitude |
| 13  | , dropoff_longitude |
| 14  | , pickup_community_area |
| 15  | , dropoff_community_area |
| 16  | , ST_DISTANCE( |
| 17  | (ST_GEOGPOINT(pickup_longitude,pickup_latitude)), |
| 18  | (ST_GEOGPOINT(dropoff_longitude,dropoff_latitude))) air_distance |
| 19  | , CAST (trip_seconds AS FLOAT64) trip_seconds |
| 20  |  FROM  `bigquery-public-data.chicago_taxi_trips.taxi_trips` |
| 21  |  WHERE  RAND() < (3000000/112860054) --sample maximum ~3M records |
| 22  |  AND trip_start_timestamp <  '2016-01-01' |
| 23  |  AND pickup_location IS  NOT  NULL |
| 24  |  AND dropoff_location IS  NOT  NULL) |
| 25  |  SELECT |
| 26  | trip_seconds |
| 27  | , air_distance |
| 28  | , pickup_latitude |
| 29  | , pickup_longitude |
| 30  | , dropoff_latitude |
| 31  | , dropoff_longitude |
| 32  | , pickup_community_area |
| 33  | , dropoff_community_area |
| 34  | , trip_start_hour |
| 35  | , trip_start_weekday |
| 36  | , trip_start_week |
| 37  | , trip_start_yearday |
| 38  | , trip_start_month |
| 39  |  FROM dataset |
| 40  |  WHERE trip_speed_kmph BETWEEN 5  AND  90 |

 [view raw](https://gist.github.com/gidutz/86c701c621e48860c8ab135df56a8076/raw/3892967093fbc0df7d23060353979ec9a4211104/extract_features.sql)  [extract_features.sql](https://gist.github.com/gidutz/86c701c621e48860c8ab135df56a8076#file-extract_features-sql) hosted with ❤ by [GitHub](https://github.com/)

feature extraction script

In the repo, you will be able to see how I execute the query using a python client and export it to GCS.

**Important! **In order for the AI platform to build a model with this data, the first column must be the target variable and the CSV export should not contain a header.

### **Submit hyper-parameter tuning job and deploy**

After I have my dataset containing a few hundred thousand rides, I define a simple neural network architecture based on the TensorFlow Estimator API, with parameters space to search. This specific spec will create a 3 hidden-layers neural network that solves a regression task (the expected trip time). It will launch 50 trials to search optimal settings for the learning rate, regularization factors, and maximum steps.

|     |     |
| --- | --- |
| 1   | {   |
| 2   |  "scaleTier": "CUSTOM", |
| 3   |  "masterType": "standard_gpu", |
| 4   |  "args": [ |
| 5   |  "--preprocess", |
| 6   |  "--validation_split=0.2", |
| 7   |  "--model_type=regression", |
| 8   |  "--hidden_units=120,60,60", |
| 9   |  "--batch_size=128", |
| 10  |  "--eval_frequency_secs=128", |
| 11  |  "--optimizer_type=ftrl", |
| 12  |  "--use_wide", |
| 13  |  "--embed_categories", |
| 14  |  "--dnn_learning_rate=0.001", |
| 15  |  "--dnn_optimizer_type=ftrl" |
| 16  | ],  |
| 17  |  "hyperparameters": { |
| 18  |  "goal": "MINIMIZE", |
| 19  |  "params": [ |
| 20  | {   |
| 21  |  "parameterName": "max_steps", |
| 22  |  "minValue": 100, |
| 23  |  "maxValue": 60000, |
| 24  |  "type": "INTEGER", |
| 25  |  "scaleType": "UNIT_LINEAR_SCALE" |
| 26  | },  |
| 27  | {   |
| 28  |  "parameterName": "learning_rate", |
| 29  |  "minValue": 0.0001, |
| 30  |  "maxValue": 0.5, |
| 31  |  "type": "DOUBLE", |
| 32  |  "scaleType": "UNIT_LINEAR_SCALE" |
| 33  | },  |
| 34  | {   |
| 35  |  "parameterName": "l1_regularization_strength", |
| 36  |  "maxValue": 1, |
| 37  |  "type": "DOUBLE", |
| 38  |  "scaleType": "UNIT_LINEAR_SCALE" |
| 39  | },  |
| 40  | {   |
| 41  |  "parameterName": "l2_regularization_strength", |
| 42  |  "maxValue": 1, |
| 43  |  "type": "DOUBLE", |
| 44  |  "scaleType": "UNIT_LINEAR_SCALE" |
| 45  | },  |
| 46  | {   |
| 47  |  "parameterName": "l2_shrinkage_regularization_strength", |
| 48  |  "maxValue": 1, |
| 49  |  "type": "DOUBLE", |
| 50  |  "scaleType": "UNIT_LINEAR_SCALE" |
| 51  | }   |
| 52  | ],  |
| 53  |  "maxTrials": 50, |
| 54  |  "maxParallelTrials": 10, |
| 55  |  "hyperparameterMetricTag": "loss", |
| 56  |  "enableTrialEarlyStopping": True |
| 57  | },  |
| 58  |  "region": "us-central1", |
| 59  |  "jobDir": "{JOB_DIR}", |
| 60  |  "masterConfig": { |
| 61  |  "imageUri": "gcr.io/cloud-ml-algos/wide_deep_learner_gpu:latest" |
| 62  | }   |
| 63  | }   |

 [view raw](https://gist.github.com/gidutz/5408bb93d0e6ab7fe9fc5cb4a82447cc/raw/1701a85854fedcfdebf2b6422f3ad6e2b4dfb748/hyper_param_spec.json)  [hyper_param_spec.json](https://gist.github.com/gidutz/5408bb93d0e6ab7fe9fc5cb4a82447cc#file-hyper_param_spec-json) hosted with ❤ by [GitHub](https://github.com/)

Provided the spec above I can use a Python client to launch a training job:

|     |     |
| --- | --- |
| 1   |     |
| 2   | def  train_hyper_params(cloudml_client, training_inputs): |
| 3   |     |
| 4   | job_name =  'chicago_travel_time_training_{}'.format(datetime.utcnow().strftime('%Y%m%d%H%M%S')) |
| 5   | project_name =  'projects/{}'.format(project_id) |
| 6   | job_spec = {'jobId': job_name, 'trainingInput': training_inputs} |
| 7   | response = cloudml_client.projects().jobs().create(body=job_spec, |
| 8   |  parent=project_name).execute() |
| 9   |  print(response) |

 [view raw](https://gist.github.com/gidutz/f166148d84c4d4beb98bc13b831b6284/raw/1a69f5a70455e8a4207c21288e7f571a876ba98d/submit_train.py)  [submit_train.py](https://gist.github.com/gidutz/f166148d84c4d4beb98bc13b831b6284#file-submit_train-py) hosted with ❤ by [GitHub](https://github.com/)

I use the API client to monitor the job run, and, when the job is done, I deploy and test the model.

|     |     |
| --- | --- |
| 1   | def  create_model(cloudml_client): |
| 2   |  """ |
| 3   | Creates a Model entity in AI Platform |
| 4   | :param cloudml_client: discovery client |
| 5   |  """ |
| 6   | models = cloudml_client.projects().models() |
| 7   | create_spec = {'name': model_name} |
| 8   |     |
| 9   | models.create(body=create_spec, |
| 10  |  parent=project_name).execute() |
| 11  |     |
| 12  |     |
| 13  | def  deploy_version(cloudml_client, job_results): |
| 14  |  """ |
| 15  | Deploying the best trail's model to AI platform |
| 16  | :param cloudml_client: discovery client |
| 17  | :param job_results: response of the finished AI platform job |
| 18  |  """ |
| 19  | models = cloudml_client.projects().models() |
| 20  |     |
| 21  | training_outputs = job_results['trainingOutput'] |
| 22  | version_spec = { |
| 23  |  "name": model_version, |
| 24  |  "isDefault": False, |
| 25  |  "runtimeVersion": training_outputs['builtInAlgorithmOutput']['runtimeVersion'], |
| 26  |     |
| 27  |  # Assuming the trials are sorted by performance (best is first) |
| 28  |  "deploymentUri": training_outputs['trials'][0]['builtInAlgorithmOutput']['modelPath'], |
| 29  |  "framework": training_outputs['builtInAlgorithmOutput']['framework'], |
| 30  |  "pythonVersion": training_outputs['builtInAlgorithmOutput']['pythonVersion'], |
| 31  |  "autoScaling": { |
| 32  |  'minNodes': 0 |
| 33  | }   |
| 34  | }   |
| 35  |     |
| 36  | versions = models.versions() |
| 37  | response = versions.create(body=version_spec, |
| 38  |  parent='{}/models/{}'.format(project_name, model_name)).execute() |
| 39  |  return response |

 [view raw](https://gist.github.com/gidutz/70b126b2a7d561e9d5f7f232d8f754eb/raw/d8e14dc53d9b1b9e20617911269c6ccb5f0e552c/deploy_model.py)  [deploy_model.py](https://gist.github.com/gidutz/70b126b2a7d561e9d5f7f232d8f754eb#file-deploy_model-py) hosted with ❤ by [GitHub](https://github.com/)

With this, I completed the deployment of a machine learning pipeline using only API calls.

### Get predictions

In order to get predictions, I load part of the test set records to the memory and send it to the deployed version for inference:

|     |     |
| --- | --- |
| 1   | def  validate_model(): |
| 2   |  """ |
| 3   | Function to validate the model results |
| 4   |  """ |
| 5   | df_val = pd.read_csv('{}/processed_data/test.csv'.format(job_dir)) |
| 6   |     |
| 7   |  # Submit only 10 samples to the server, ignore the first column (=target column) |
| 8   | instances = [", ".join(x) for x in df_val.iloc[:10, 1:].astype(str).values.tolist()] |
| 9   | service = discovery.build('ml', 'v1') |
| 10  | version_name =  'projects/{}/models/{}'.format(project_id, model_name) |
| 11  |     |
| 12  |  if model_version is  not  None: |
| 13  | version_name +=  '/versions/{}'.format(model_version) |
| 14  |     |
| 15  | response = service.projects().predict( |
| 16  |  name=version_name, |
| 17  |  body={'instances': instances} |
| 18  | ).execute() |
| 19  |     |
| 20  |  if  'error'  in response: |
| 21  |  raise  RuntimeError(response['error']) |
| 22  |     |
| 23  |  return response['predictions'] |

 [view raw](https://gist.github.com/gidutz/e786c430c5ea767b1bec01bcee03a863/raw/beefb9f2e0a34550ff03fe397f74be54eb015459/predict.py)  [predict.py](https://gist.github.com/gidutz/e786c430c5ea767b1bec01bcee03a863#file-predict-py) hosted with ❤ by [GitHub](https://github.com/)

Getting predictions

Want more stories? Check our blog on [Medium](http://blog.doit-intl.com/), or [follow Gad on Twitter](https://twitter.com/gadbenram).

*Thanks to Adam Horowitz for technical advisory*