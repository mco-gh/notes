Going #Serverless on Google Cloud Platform – Google Cloud Platform — Community – Medium

# Going #Serverless on Google Cloud Platform

Calling something serverless is so hot right now. Every developer tools company found out and suddenly everything is *#serverless*.

In fact, in the Google Cloud Next 17 Keynotes, so many things were called serverless. These products were amazing in their own right, but the word serverless was thrown around so loosely that it was cringeworthy at times.

As expected, [people are upset about this](https://medium.com/@cloud_opinion/googles-folly-d57166b40045).

![](../_resources/b154574787993d282cd370a30296ca90.png)

So what the hell is serverless? Again, everyone has their own opinions on what serverless is.

![](../_resources/f1df94a6ff6a33af2716fdd9b0324460.png)

![](../_resources/f1df94a6ff6a33af2716fdd9b0324460.png)

So maybe only Kelsey cares about this
So let me define *my* definition.

I’m going to break down “cloud” products into four different categories. The names are basically made up, but this is what makes sense to me.

#### 1) SaaS

SaaS products are ready to use out of the box by end users. There is nothing to provision. You either pay for what you use, or purchase bulk credits of some sort.

#### 2) Serverless

Serverless products are used by developers to build higher order products. There is nothing to provision, but there may be some knobs to tune the infrastructure. You pay for exactly what you use, nothing more.

#### 3) Managed

Managed products are used by developers to build higher order products. Developers need to provision capacity and tune things, but don’t need to maintain the infrastructure. You pay for excess infrastructure when it is not being used.

#### 4) IaaS

IaaS products mirror on-prem solutions, except you can provision resources in seconds/minutes instead of days/months. They require explicit provisioning and maintenance. You pay for excess infrastructure when it is not being used.

Do you agree with this categories?
Am I TOTALLY WRONG IN EVERY WAY!!?
Let me know in the comments!

* * *

*...*

I am going to map most of Google Cloud’s products to one of these four categories. Of course, arguments can be made to fit products in multiple categories, but I’m going to make the tough calls and put them in only one. I think this will make it very clear how I think about these categories.

* * *

*...*

### 1) SaaS

[**G Suite**](https://gsuite.google.com/)

The obvious entry into this category. G Suite is ready to be used by the end user, no need for developers to do anything. Of course, Apps Script can be considered serverless, but as it depends so much on the rest of G Suite, it feels right in this category.

[**Data Studio**](https://www.google.com/analytics/data-studio/)

Data studio lets you build dashboards for your Google Analytics, Cloud SQL, BigQuery, etc data. There is a lot of drag and drop involved, and end users can be productive without developer support.

* * *

*...*

### 2) Serverless

[**Cloud Functions**](https://cloud.google.com/functions)

The obvious entry into this category. AWS Lambda started the FaaS revolution, and Cloud Functions follows a similar pattern. You write your functions, specify when they trigger, tune how much memory/cpu is allocated per call, and deploy. Everything else is handled for you. You pay per function invocation, so it is exactly matched to your traffic.

[**Cloud Storage**](https://cloud.google.com/storage)Cloud Storage is similar to Google Drive, but isn’t usable by end users. It requires a developer to build higher order systems on top. You don’t provision anything, and pay for exactly what you use. You can tune the latency and price by choosing the bucket type (Nearline, Multi-Regional, etc).

[**App Engine Standard**](https://cloud.google.com/appengine/docs/standard/)The first Google Cloud product. Write your code, tune how much memory/cpu you want, and deploy. Everything else is handled for you. App Engine Standard scales to exactly match your traffic and scales to zero when you have none, so you pay for exactly what you use.

[**Cloud Datastore**](https://cloud.google.com/datastore)The first NoSQL database at Google Cloud. You don’t provision anything, just read and write data. You pay per read/write and for the exact storage you use, and it scales automatically.

[**Firebase Realtime Database / Hosting**](http://firebase.google.com/)Similar to Cloud Datastore, but used directly on the frontend. You don’t provision anything, just read and write data. You pay for data transfer and for the exact storage you use, and it scales automatically.

[**Cloud Firestore**](http://firebase.google.com/)This next generation database brings the best from Datastore and Firebase Realtime Database together. You can use it directly from the frontend like the Realtime Database and from the server like Datastore, and get advanced query support and strong consistency. You don’t provision anything, just read and write data. You pay per read/write and for the exact storage you use, and it scales automatically.

[**BigQuery**](https://cloud.google.com/bigquery/)**

**BigQuery is Google’s data warehouse service, letting users query TB of data with SQL. There is nothing to manage, just dump/stream your data in and query. You pay to store data and query data, no need to provision machines or storage or set up indexes.

[**Pub/Sub**](https://cloud.google.com/pubsub/)**

**Pub/Sub is Google’s many-to-many async messaging bus (think Apache Kafka or RabbitMQ). No need to provision anything, and it scales to millions of messages a second instantly. Pub/Sub charges per message, so you pay for exactly what you use.

[**Stackdriver (Logs, Monitoring, Debug, Tracing)**](https://cloud.google.com/stackdriver)

The Stackdriver tools let you access powerful tools without needs to set anything up. They are all have a free tier, but you can pay to monitor more resources and other clouds like AWS. There is nothing to provision or tune and you pay per resource monitored so there is no extra spending.

[**Cloud Dataflow**](https://cloud.google.com/dataflow/)

Cloud Dataflow uses Apache Beam to create fully managed ETL, batch processing, and streaming analytics pipelines. It autoscales to process your pipeline, and scales back to zero when there is no more work left.

#### 3) Managed

[**Kubernetes Engine**](https://cloud.google.com/container-engine/)**

**Google Kubernetes Engine creates a Kubernetes Cluster for you in one click. Google manages the Master and Nodes and auto-updates them for you. You have to provision a cluster ahead of time(though there are some auto-scaling capabilities) so you are paying for unused resources.

[**App Engine Flexible**](https://cloud.google.com/appengine/docs/flexible/)**

**App Engine Flexible is similar to Standard, but runs on VMs instead of a sandbox. While this gives it more “flexibility” over what it can run, you lose the “serverless” magic of standard. Auto-scaling and deploying is not as fast, but the biggest difference is you have to always have one VM instance running, meaning you are paying for unused resources.

[**Cloud SQL **](https://cloud.google.com/sql)Cloud SQL gives you managed MySQL and PostgreSQL instances. Google worries about backups, failover replication, etc, which reduces the operational overhead of running a database. While there are some auto-scaling capabilities, you need to provision a machine and disk ahead of time, which means paying for unused resources.

[**Cloud Bigtable**](https://cloud.google.com/bigtable)**

**Cloud Bigtable is Google’s HBase compatible NoSQL database. While storage scales automatically (you pick SSD or HDD), you need to choose how many nodes you want to tune performance. More nodes = more performance, but of course you can over/under provision.

[**Cloud Spanner**](https://medium.com/google-cloud/cloud.google.com/spanner)Cloud Spanner is similar to BigTable except it is globally consistent and relational instead of NoSQL. This is pretty magical! You need to choose how many nodes you want to tune performance. More nodes = more performance, but of course you can over/under provision.

[**Cloud Load Balancing (L4/L7)**](https://cloud.google.com/load-balancing)Both the L4 and L7 load balancers offered by Google Cloud are fully managed services that require no provisioning, pre-warming, or tuning. The only reason this is not in the Serverless category is you have to pay a flat rate to launch the load balancer regardless of how much traffic it handles.

[**Cloud Dataproc **](https://cloud.google.com/dataproc)Cloud Dataproc launches a managed Spark/Hadoop cluster. You need to specify how many VMs you want and tune them, but after that you can use the cluster without any additional setup. You pay for the VMs even when they are not being used.

[**Cloud Machine Learning Engine **](https://cloud.google.com/ml-engine/)Cloud Machine Learning Engine creates and manages a distributed TensorFlow cluster for you to train and serve your models on. You have to provision a cluster, but the cluster is fully managed and you can just submit jobs to it.

#### 4) IaaS

[**Compute Engine**](https://cloud.google.com/compute)**

**These are Linux and Windows VMs. While you can autoscale them using Managed Instance Groups, and you can do cool things like have the disks automatically grow, at the end of the day you are 100% responsible.

[**Cloud Launcher**](https://cloud.google.com/launcher)

Cloud Launcher lets you deploy pre-configured apps on Compute Engine. Though the initial setup is automatic, you are responsible for maintaining the servers and pay for unused resources.

What do you think? Does this make sense? Is this whole debate worth it? Is there something I missed? Please let me know!