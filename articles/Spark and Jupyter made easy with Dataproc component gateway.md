Spark and Jupyter made easy with Dataproc component gateway

# Spark and Jupyter made easy with Dataproc component gateway

## Use the new Dataproc optional components and component gateway features to easily set-up and use Jupyter Notebooks

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='149' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='150' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*X3JLC3UgCaufCvH72wlTOg.png](../_resources/ad138c0bcf364ad46ff723f77d2eb0a6.png)](https://medium.com/@tfayyaz?source=post_page-----fa91d48d6a5a----------------------)

[Tahir Fayyaz](https://medium.com/@tfayyaz?source=post_page-----fa91d48d6a5a----------------------)

Draft · 10 min read

![1*ITz23f880aFggnAT9sqoLw.png](../_resources/9e72ac8e552f913af58a661f4c90edee.png)
![1*ITz23f880aFggnAT9sqoLw.png](../_resources/5adf84042f69eedd6f1ed6619b347eef.png)
Apache Spark and Jupyter Notebooks architecture on Google Cloud

As a long time user and fan of Jupyter Notebooks I am always looking for the best ways to set-up and use notebooks especially in the cloud. I believe Jupyter Notebooks are the perfect tool for learning, prototyping and in some cases production of your data projects as they allow you to interactively run your code and immediately see your results.

You might have used Jupyter notebooks on your desktop in the past with Python but struggled with handling very large datasets. However with many kernels now available you can make use of Apache Spark for large-scale data processing in Jupyter but also continue to use your Python libraries in the same notebook.

However getting an Apache Spark cluster set-up with Jupyter Notebooks can be complicated and so in **Part 1** of the “**Apache Spark and Jupyter Notebooks on Cloud Dataproc” **series I wanted to show you how easy it is thanks to new features like [optional components](https://cloud.google.com/dataproc/docs/concepts/components/overview) and [component gateways](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways).

# Create a Dataproc cluster with Spark and Jupyter

You can create a Cloud Dataproc cluster using the Google Cloud Console, gcloud command line interface (CLI) or [Dataproc client libraries](https://cloud.google.com/dataproc/docs/reference/libraries).

In this post we will be using the gcloud CLI from the [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) where gcloud is already installed (If you’re new to Google Cloud view the [Getting Started with Cloud Shell & gcloud codelab](https://codelabs.developers.google.com/codelabs/cloud-shell/index.html?index=..%2F..index#2)).

Alternatively you can run the gcloud commands locally in a terminal window which requires installing the [gcloud SDK](https://cloud.google.com/sdk/gcloud).

To get started once in the cloud shell or your terminal window set your project ID where you will create your Dataproc cluster

gcloud config set project [PROJECT_ID]

## **Enable Dataproc, Compute, GCS and BigQuery APIs and IAM roles**

If you have Admin permissions run this command to enable all the APIs required in the **Apache Spark and Jupyter Notebooks on Cloud Dataproc **series of posts.

gcloud services enable dataproc.googleapis.com \
compute.googleapis.com \
storage-component.googleapis.com \
bigquery.googleapis.com \
bigquerystorage.googleapis.com

If you are not the admin and do not have the correct permissions ask the admin for your GCP organization or project to enable the APIs above and to also give you the correct [**Dataproc roles**](https://cloud.google.com/dataproc/docs/concepts/iam/iam#roles) to create and use your cluster.

## **Create a GCS bucket to be used by your Dataproc Cluster**

Create a Google Cloud Storage bucket in the region closest to your data and give it a unique name. This will be used for the Dataproc cluster.

export REGION=us-central1

export BUCKET_NAME=dataproc-spark-jupyter-<your-name>gsutil mb -c standard -l ${REGION} gs://${BUCKET_NAME}

## **Create your Dataproc Cluster with Jupyter & Component Gateway**

Run this gcloud command to create your cluster with all the necessary components to work with Jupyter on your cluster.

export REGION=us-central1
export ZONE=us-central1-a
export CLUSTER_NAME=spark-jupyter-1-5-<your-name>

export BUCKET_NAME=dataproc-spark-jupyter-<your-name>gcloud beta dataproc clusters create ${CLUSTER_NAME} \

--region=${REGION} \
--zone=${ZONE} \
--image-version=preview \
--master-machine-type=n1-standard-4 \
--worker-machine-type=n1-standard-4 \
--bucket=${BUCKET_NAME} \
--optional-components=ANACONDA,JUPYTER \
--enable-component-gateway \
--metadata 'PIP_PACKAGES=google-cloud-bigquery google-cloud-storage' \

--initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/python/pip-install.sh

## Flags used in gcloud dataproc create commad

Here is a breakdown of the flags used in the gcloud dataproc create command
--region=${REGION} \
--zone=${ZONE} \

Specifies the region and zone of where the cluster will be created. You can see the list of [available regions here.](https://cloud.google.com/compute/docs/regions-zones#available) Zone is optional unless if you are using n2 machine types when you must specify a zone.

--image-version=preview \

The image version to use. At the date of publishing this post using image version **preview** installs Dataproc version 1.5. You can see the list of [available versions here](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions).

--bucket=${BUCKET_NAME} \

Specify the Google Cloud Storage Bucket you created earlier to use for the Cluster. This is also where your notebooks will be stored.

If you do not supply a GCS bucket it will be created for you. You can delete and recreate your cluster and all your notebooks will still be saved in the Google Cloud Storage bucket.

--master-machine-type=n1-standard-4 \
--worker-machine-type=n1-standard-4 \
The machine types to use for your Dataproc Cluster.

***Note: Look out for future post in the series on recommendations for what machine types to use and how to enable auto-scaling***

--optional-components=ANACONDA,JUPYTER

Setting these values for [optional components](https://cloud.google.com/dataproc/docs/concepts/components/overview) will install all the necessary libraries for Jupyter and Anaconda (which is required for Jupyter notebooks) on your cluster.

--enable-component-gateway

Enabling [component gateway](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways) creates an App Engine link using Apache Knok and Inverting proxy which gives easy, secure and authenticated access to the Jupyter and JupyterLab web interfaces meaning you no longer need to create SSH tunnels.

It will also create links for other tools on the cluster including the Yarn Resource manager and Spark History Server which are useful for seeing the performance of your jobs and cluster usage patterns.

--metadata 'PIP_PACKAGES=google-cloud-bigquery google-cloud-storage'

--initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/python/pip-install.sh

Installs the latest versions of the [Google Cloud BigQuery python library](https://googleapis.dev/python/bigquery/latest/index.html) and the [Google Cloud Storage python library](https://googleapis.dev/python/storage/latest/client.html). These will be used to perform various tasks when working with BigQuery and GCS in your notebooks.

# Accessing Jupyter or JupyterLab web interfaces

Once the cluster is ready you can find the Component Gateway links to the Jupyter and JupyterLab web interfaces by running this gcloud command.

export REGION=us-central1

export CLUSTER_NAME=spark-jupyter-1-5-<your-name>gcloud beta dataproc clusters describe ${CLUSTER_NAME} \

--region=${REGION}
Which will show an output with the links in the following format.
clusterName: spark-jupyter-1-5-<your-name>
clusterUuid: XXXX-1111-2222-3333-XXXXXX
config:
configBucket: bucket-name
endpointConfig:
enableHttpPortAccess: true
httpPorts:

Jupyter: [https://](https://gsbrebdjijhgjlmsdqkc2byoua-dot-us-east1.dataproc.googleusercontent.com/jupyter/)[random-characters](https://gsbrebdjijhgjlmsdqkc2byoua-dot-us-east1.dataproc.googleusercontent.com/hdfs/dfshealth.html)[-dot-us-east1.dataproc.googleusercontent.com/jupyter/](https://gsbrebdjijhgjlmsdqkc2byoua-dot-us-east1.dataproc.googleusercontent.com/jupyter/)

JupyterLab: [https://](https://gsbrebdjijhgjlmsdqkc2byoua-dot-us-east1.dataproc.googleusercontent.com/jupyter/lab/)[random-characters](https://gsbrebdjijhgjlmsdqkc2byoua-dot-us-east1.dataproc.googleusercontent.com/hdfs/dfshealth.html)[-dot-us-east1.dataproc.googleusercontent.com/jupyter/lab/](https://gsbrebdjijhgjlmsdqkc2byoua-dot-us-east1.dataproc.googleusercontent.com/jupyter/lab/)

...

Alternatively you can find the Component Gateway links in the Google Cloud console for Dataproc by clicking on the cluster you created and going to the **Web Interfaces** tab.

![1*6eNJc6DjMbp6JPEvuHb5Lg.png](../_resources/16a6e8cfcbd97015288465bac8a6fd16.png)
![1*6eNJc6DjMbp6JPEvuHb5Lg.png](../_resources/96f43b9db96445a4019571a1f732bce3.png)

You will notice that you have access to Jupyter which is the classic notebook interface or [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) which is is described as the next-generation UI for Project Jupyter.

There are a lot of great new UI features in JupyterLab and so if you are new to using notebooks or looking for the latest improvements it is recommended to go with using JupyterLab as it will eventually replace the classic Jupyter interface according to the official docs.

# Python, R and Scala Kernels

![1*VewHWLFn1H4HsuKzX-iCEQ.png](../_resources/edf5b7bf92239a4d0dd15a47165931a2.png)
![1*VewHWLFn1H4HsuKzX-iCEQ.png](../_resources/e31a81b93b81d39445f94eab3dcbe442.png)

Based on the image version you selected when creating your Dataproc cluster you will have different kernels available:

- **Image version 1.3:** Python 2 and PySpark
- **Image version 1.4:** Python 3, PySpark (Python), R and Spylon (Scala)
- **Image version Preview (1.5):** Python 3, PySpark (Python), R and Spylon (Scala)

You should use image version 1.4 or above so that you can make use of the Python 3 kernel to run PySpark code or the Spylon kernel to run Scala code.

# Creating your first PySpark Jupyter Notebook

![1*v2gjZBDWZ7Hvx0ENZCx7VA.png](../_resources/d129d1f15a7c95d7721f7cc0f96807ca.png)
![1*v2gjZBDWZ7Hvx0ENZCx7VA.png](../_resources/113e1d959796c65ce60a44d31e1919f8.png)

From the launcher tab click on the Python 3 notebook icon to create a notebook with a Python 3 kernel (not the PySpark kernel) which allows you to configure the SparkSession in the notebook and include the [spark-bigquery-connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) required to use the [BigQuery Storage API](https://cloud.google.com/bigquery/docs/reference/storage).

Once your notebook opens in the first cell check the Scala version of your cluster so you can include the correct version of the spark-bigquery-connector jar.

**Input [1]:**
!scala -version
**Output [1]:**
![1*Yjv0b9CR1V2Beu-TK9d0ZA.png](../_resources/c9822fcd77ae83bd19ba089aa4b975f3.png)
![1*dOpjH7XG--f_a2BS1tYGgA.png](../_resources/78153688a64f86f755912abe810f755d.png)
Create a Spark session and include the spark-bigquery-connector jar
**Input [2]:**
**from**  **pyspark.sql**  **import** SparkSession
spark = SparkSession.builder \
.appName('Jupyter BigQuery Storage')\

.config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar') \

.getOrCreate()

Create a Spark DataFrame by reading in data from a public BigQuery dataset. This makes use of the [spark-bigquery-connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) and BigQuery Storage API to load the data into the Spark cluster.

If your Scala version is 2.11 use the following jar
gs://spark-lib/bigquery/spark-bigquery-latest.jar
If your Scala version is 2.12 use the following jar
gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar

We will create a Spark DataFrame and load data from the BigQuery public dataset for Wikipedia Pageviews. You will notice we are not running a query on the data as we are using the bigquery-storage-connector to load the data into Spark where the processing of the data will happen.

**Input [3]:**
table = "bigquery-public-data.wikipedia.pageviews_2020"df = spark.read \
.format("bigquery") \
.option("table", table) \
.load()df.printSchema()
**Output [3]:**
![1*-39EJWmJY1Xh_jFG8EJKyQ.png](:/768d13645ae6fc81d905bffd0f2e3c52)
![1*Yjv0b9CR1V2Beu-TK9d0ZA.png](../_resources/08638673e068d969125a29aaf0e459c5.png)
Create a new aggregated Spark DataFrame and print the schema
**Input [4]:**
df_agg = df \
.select('wiki', 'views') \
.where("datehour = '2020-03-03'") \
.groupBy('wiki') \
.sum('views')df_agg.printSchema()
**Output [4]:**
![1*dOpjH7XG--f_a2BS1tYGgA.png](../_resources/b76e3805235157c9fb91cc55809905d7.png)
![1*-39EJWmJY1Xh_jFG8EJKyQ.png](../_resources/2b7be43a0e2fd9667e797b4c8a93e5df.png)

Run the aggregation using the .show() function on the DataFrame which will start the Spark job to process the data and then show the output of the Spark DataFrame limited to the first 20 rows.

**Input [5]:**
df_agg.show()
**Output [5]:**
![1*OL1_dLe3K64fjsNrQ6TzAA.png](../_resources/be3f23929c67d757c27b4034d4abd4c1.png)
![1*OL1_dLe3K64fjsNrQ6TzAA.png](../_resources/aeeeb828348aa359c4e0ad2c870df4ad.png)

You should now have your first Jupyter notebook up and running on your Dataproc cluster. Give your notebook a name and it will be auto-saved to the GCS bucket used when creating the cluster. You can check this using the gsutil command.

export BUCKET_NAME=dataproc-spark-jupyter-<your-name>gsutil ls gs://${BUCKET_NAME}/notebooks/jupyter

# Example notebooks for more use cases

The next posts in this series will feature Jupyter notebooks with common Apache Spark patterns for loading data, saving data and plotting your data with various Google Cloud Platform products and open-source projects:

- Spark and BigQuery Storage API using Jupyter Notebooks on Dataproc
- Spark and Google Cloud Storage using Jupyter Notebooks on Dataproc
- Spark and Apache Iceberg using Jupyter Notebooks on Dataproc
- Plot Spark DataFrames using Pandas with Jupyter Notebooks on Dataproc

You can also access the [examples notebooks on Cloud Dataproc GitHub repo](http://github.com/GoogleCloudDataproc/cloud-dataproc/tree/master/notebooks)

# Giving the cluster’s service account access to data

In the example above we are accessing a public dataset but for your use case you will most likely be accessing your companies data with restricted access. The Jupyter notebook and Dataproc cluster will attempt to access data in Google Cloud Platform services using the service account of the underlying Google Computer Engine (GCE) VMs and not your own Google credentials.

You can see find the service account of your cluster by running this command to describe the master VM in GCE which will have the same name of your Dataproc cluster followed by **-m**

export ZONE=us-central1-a

export CLUSTER_NAME=spark-jupyter-1-5-<your-name>gcloud compute instances describe ${CLUSTER_NAME}-m \

--zone=${ZONE}

This will give a long list of attributes including the service account and scopes as shown in this example output.

serviceAccounts:-
email: <random-number>-compute@developer.gserviceaccount.com

scopes: - https://www.googleapis.com/auth/bigquery - https://www.googleapis.com/auth/bigtable.admin.table - https://www.googleapis.com/auth/bigtable.data - https://www.googleapis.com/auth/cloud.useraccounts.readonly - https://www.googleapis.com/auth/devstorage.full_control - https://www.googleapis.com/auth/devstorage.read_write - https://www.googleapis.com/auth/logging.write

Alternatively you can view the service account in the Google Cloud Console by going to the **VM Instances** tab in your Dataproc cluster and clicking on the master VM instance.

![1*bB_ttptnMvqJQ_7bE2Jc1A.png](../_resources/1abfc1cbdc12707b108abd9fc6c979d6.png)
![1*bB_ttptnMvqJQ_7bE2Jc1A.png](../_resources/0db9a8481d10ad4226827be3c0cc0096.png)

Once in the VM page scroll to the bottom and you will see the service account for the VM. This is the same service account for all VM instances in your cluster.

![1*vfz-qlUQEe1hFHHz6nTBdQ.png](../_resources/72ee20a374d5a63b9022d5a5e9a57e15.png)
![1*vfz-qlUQEe1hFHHz6nTBdQ.png](../_resources/f306fc0c9235f12e67a1b07920eb7647.png)

You should then give the service account the correct [**BigQuery IAM roles**](https://cloud.google.com/bigquery/docs/access-control#bigquery)** and **[**GCS IAM roles**](https://cloud.google.com/storage/docs/access-control/iam-roles) to access the BigQuery datasets or GCS buckets you need.

For more details on providing the correct access read this solution to [Help secure the pipeline from your data lake to your data warehouse.](https://cloud.google.com/solutions/help-secure-the-pipeline-from-your-data-lake-to-your-data-warehouse)

# Deleting your Dataproc cluster

Once you have have finished all of your work within the Jupyter Notebook and all Spark jobs have finished processing it is recommended to delete the Dataproc cluster which can be done via the Cloud Console or using this gcloud command:

export REGION=us-central1

export CLUSTER_NAME=spark-jupyter-<your-name> gcloud beta dataproc clusters delete ${CLUSTER_NAME} \

--region=${REGION} \

As mentioned before you can always delete and recreate your cluster and all your notebooks will still be saved in the Google Cloud Storage bucket which is not deleted when you delete your Dataproc cluster.

# What’s Next

- Look out for next post series which will cover using the bigquery-storage-connector in a Jupyter Notebook in more depth.
- Follow me here on medium (@tfayyaz) and on Twitter ([@tfayyaz](http://twitter.com/tfayyaz)) to hear more about the latest updates about Dataproc.
- Ask any questions in the comments or on Stackoverflow under the [google-cloud-dataproc](https://stackoverflow.com/questions/tagged/google-cloud-dataproc) tag.
- Have fun working with Spark and Jupyter Notebooks on Dataproc.