A detailed look at why mabl Chose Google Cloud Platform (GCP) over AWS

# A detailed look at why mabl Chose Google Cloud Platform (GCP) over AWS

 ![James Baldassari](../_resources/5ef548e9815bf11134ceca9056e3655c.png)

by   [James Baldassari](https://www.mabl.com/blog/author/james-baldassari) | Oct 30, 2017 |     2 Comments

 [AWS](https://www.mabl.com/blog/tag/aws)  [Google Cloud](https://www.mabl.com/blog/tag/google-cloud)  [machine learning](https://www.mabl.com/blog/tag/machine-learning)  [Modern Applications](https://www.mabl.com/blog/tag/modern-applications)

![A detailed look at why mabl Chose Google Cloud Platform (GCP) over AWS](../_resources/0ea5cb3f9851e1d29d42379e4731fb43.jpg)

As product development was beginning at [mabl](https://www.mabl.com/) in early 2017, we had to decide which cloud provider to use.  While we were most familiar with Amazon Web Services (AWS), we decided to invest some time exploring all of the options available to us.  Based on an initial set of requirements, we were able to narrow the list of candidates to just AWS and Google Cloud Platform (GCP).  We spent several weeks researching both and building prototypes to familiarize ourselves with features that we had not used before.  After a thorough and objective evaluation of both providers we decided unanimously to build on GCP.  In this blog post, I’ll describe some of the factors that went into that decision.

Included in this blog are detailed comparisons of specific GCP and AWS products including serverless compute, databases, analytics engines, as well as machine learning services.

## A little perspective

As a new software company, we faced many questions as we were familiarizing ourselves with the problem domain and developing our product concept:

1. What should the high-level architecture look like?
2. What languages, processes, and development tools should we use?
3. Where will our software run?

The first two topics are blog posts for another day.  Of the three, the third question has probably seen the most rapid change over the past 10 years.  The last time I participated in this exercise was in 2008.  To put that into perspective, 2008 was the same year that AWS EC2 went GA.  Back then AWS was not the 70+ service juggernaut it is today, *the cloud* had not yet entered into the common lexicon, and running your software on cloud-based infrastructure was by no means the obvious choice.  At that time the main options were:

1. Build out your own datacenter (or rent space from a collocation facility), and buy your own hardware

2. Rent bare metal servers on a monthly or yearly basis
3. Rent virtual private servers
4. Run VMs on AWS EC2

In only about 10 years we’ve seen the role of the cloud platform change from an interesting niche service the dominant deployment model for a large segment of software companies.  With that change we’ve also seen a huge increase in the cloud options available to us.  Our options today look something like this:

![Why We Chose Google Cloud](../_resources/99c6ecd3e064ea9d2a9a1de6d4b2514c.jpg)

I’m sure I’ve missed a few!  There are so many platforms available today that we felt obligated to set aside our preconceptions, forget what everybody else was doing, and make an objective decision about what platform was the best fit for *our* needs.

## The decision-making process

The first step in our process was to define our cloud requirements.  These are the services and features that we would most likely need based on our product requirements and high-level architecture:

- File storage
- Pub/sub messaging
- Scalable NoSQL database
- Auto-scaling platform for HTTP REST APIs
- Platform for executing tests, preferably container-based
- Hosting for static UI assets: JavaScript, CSS, images
- Framework for ETL and stream-based event processing
- Platform for storing and querying large amounts of semi-structured data
- Serverless event handling
- Production grade monitoring and logging

Given all the services we thought we would want we were able to quickly narrow down the list of candidates to AWS and GCP.  These are the services we might use in each cloud to build mabl:

|     |     |     |
| --- | --- | --- |
| **Service Type** | **AWS** | **GCP** |
| File storage | - S3<br>- Glacier | - Cloud Storage |
| Pub/sub messaging | - Kinesis<br>- SQS | - Pub/Sub |
| NoSQL database | - DynamoDB | - Datastore<br>- Bigtable |
| Auto-scaling HTTP endpoints | - Elastic Beanstalk | - AppEngine |
| Container services | - EC2 Container Service (ECS)<br>- EC2 Container Registry | - Google Container Engine (GKE)<br>- Google Container Registry |
| UI asset hosting | - S3<br>- CloudFront | - Firebase |
| Stream and batch processing | - Spark on EMR | - Dataflow<br>- Dataproc |
| Semi-structured storage/query | - RedShift | - BigQuery |
| Serverless | - Lambda | - Cloud Functions |
| Machine learning | - Amazon Machine Learning | - ML Engine<br>- Datalab |
| Monitoring | - CloudWatch | - Stackdriver |

It’s clear that both AWS and GCP had the full set of services that we needed, and we felt that we could deploy our software to either platform without resorting to any ugly workarounds.  Next, we decided to look at what differentiated some of these services as well as some non-technical factors that we couldn’t ignore.

###

### Prior experience

Most of the team had significant prior experience with AWS.  A couple people on the team had varying degrees of experience with GCP.

**Advantage: AWS**

###

### Developer community

While GCP has some large customers like SnapChat and Pokemon Go, AWS clearly has a larger developer community.  We looked at group membership and number of scheduled meetups for the two platforms on meetup.com to get a quick read on relative community engagement:

|     |     |     |
| --- | --- | --- |
|     | **Members ** | **Meetup Groups** |
| [Amazon Web Services](https://www.meetup.com/topics/amazon-web-services/) | 416,302 | 847 |
| [Google Cloud Platform](https://www.meetup.com/topics/google-cloud-platform/) | 72,914 | 150 |

The number of active questions on Stack Overflow shows a similar gap:

|     |     |
| --- | --- |
|     | **Active Questions: Stack Overflow** |
| [Amazon Web Services](https://stackoverflow.com/questions/tagged/amazon-web-services) | 46,812 |
| [Google Cloud Platform](https://stackoverflow.com/questions/tagged/google-cloud-platform) | 4,944 |

**Advantage: AWS**

###

### AWS Kinesis vs. GCP Pub/Sub

Pub/sub messaging is a critical requirement for many distributed, loosely coupled systems.  It can be used for anything from data ingestion to event handling and synchronization between subcomponents.  It has to scale, and it has to Just Work™.

The features of Kinesis and Pub/Sub are very similar.  They are essentially distributed queues with at-least-once delivery semantics supporting multiple publishers and multiple subscribers.  They both have a number of integrations with other services, such as allowing a serverless function to be a subscriber and to act on messages being published to the queue.  There are at least two significant ways in which these services differ, however:

1. Kinesis allows new subscribers to start reading messages in the past, up to the trim horizon (the oldest message retained by the stream).  Pub/Sub only allows a new subscription to start reading messages that were created *after* the subscription was created.  This isn’t a major issue for us at this point, but it does impose some limitations on how the service can be used.  Minor advantage to Kinesis.

2. Pub/Sub has a vastly superior scalability and cost model.  Huge advantage to Pub/Sub.

The pricing and scaling model for GCP’s Pub/Sub is simply pay-by-volume.  That’s it.  You don’t need to estimate your request rate or monitor usage and scale the service.  You don’t need to pay for capacity you aren’t using.  You just make as many requests as you need, and the service automatically scales to meet your needs.  If you’re a Kinesis user, think about how it would simplify your job if you didn’t have to worry about the dreaded *ProvisionedThroughputExceeded* error as your usage grows or you experience bursty traffic.  The alternative with Kinesis is to provision much more capacity than you need most of the time, but that requires paying for capacity you aren’t using.

Until recently, scaling Kinesis meant manually splitting or merging shards.  At my previous company I worked on a service that pushed over 100TB of records through Kinesis per day across hundreds of shards.  Scaling up the stream was a process that could take the majority of the day to complete, and if we were caught unprepared by an unexpected increase in throughput it meant that *some percentage of our records were being dropped* until the stream had scaled sufficiently to handle the throughput.  Of course there are buffer-and-replay strategies that can mitigate these types of issues, but that’s not a feature the Kinesis client libraries provide out of the box, so you’re going to have to build that capability yourself.  For very high throughput streams it may not even be practical to buffer messages to disk and retry for hours.

With GCP Pub/Sub we don’t have to worry about how the service scales or whether we’re leaving money on the table due to over-provisioned capacity.  We can focus on product features instead of operational issues.

**Advantage: GCP**

[![mabl early access](../_resources/1a6a4c401d43078a3919c0fa9a593392.png)](https://www.mabl.com/)

### AWS DynamoDB vs. GCP Datastore

Like in the Kinesis vs. Pub/Sub comparison, DynamoDB and Datastore share many common features, but Google seems to have eliminated some of the common pain points experienced by users of DynamoDB.  Both databases can be used as key-value stores or document stores.  They are both highly scalable.  Both support primary and secondary indexes.

The main feature in my opinion that sets Datastore apart from DynamoDB is again the scalability and pricing model.  Datastore is pay-by-request for reads, writes, and deletes.  Unlike DynamoDB, there is no need to provision read and write throughput capacity upfront.  Like Pub/Sub, with Datastore you will never see a *ProvisionedThroughputExceeded* error because scalability is managed automatically by GCP.  Another nice feature of Datastore is its native support for certain types of transactions which enable patterns such as conditional updates.

There are a couple of limitations in Datastore that are worth mentioning, however.  First, most operations in Datastore are [eventually consistent](https://cloud.google.com/datastore/docs/articles/balancing-strong-and-eventual-consistency-with-google-cloud-datastore/).  DynamoDB allows for both eventually consistent and strongly consistent reads (albeit at different price points), but Datastore does not provide that option at this time.  That being said, there are some design patterns (including the use of transactions) that minimize the impact of this consistency constraint in Datastore.

Another limitation of Datastore is its per-entity-group write limit of one write/sec.  In most cases what this means is that you cannot update the *same key/entity* more than once per second.  It’s generally not a good idea to design your data model such that the same key is updated frequently because it will lead to performance bottlenecks, but in some rare cases we have had to implement workarounds for hot keys that hit this limit.

After considering all characteristics and features of the two NoSQL databases we felt that Datastore was the better overall service than DynamoDB.  Note that there is another option in GCP: [Bigtable](https://cloud.google.com/bigtable/).  Bigtable is a massively scalable NosQL database that is API-compatible with HBase and powers many of Google’s own core products such as Search, Maps, and Gmail.  We aren’t using it at this point because we don’t yet have a use case that leverages Bigtable’s strengths, and Bigtable’s pricing model is not very cost effective at lower volumes.  Even though we don’t use Bigtable today, it’s good to know that we have it as an option for the future should our needs require it.

**Advantage: GCP**

###

### AWS EC2 Container Service (ECS) vs. GCP Google Container Engine (GKE)

Both AWS and GCP provide scalable services for running container-based workloads and for storing the containers themselves.  ECS advertises itself as a Docker-compatible container service that leverages proprietary AWS container orchestration technology.  By contrast, GKE is managed Kubernetes.  Since GKE is vanilla Kubernetes it’s possible to run our software on any Kubernetes cluster, even on AWS if we were to launch a Kubernetes cluster there.  That flexibility was attractive, and we felt like we weren’t being locked into one vendor with our choice

For more information on how we’re using GKE at [mabl](https://www.mabl.com/), check out our blog post on [Validating 100 Million Pages a Month with Kubernetes](https://www.mabl.com/blog/validating-100-million-pages-kubernetes).

**Advantage: GCP**

###

### AWS EMR + Spark vs. GCP Dataflow

We knew that we would have a couple of different use cases for data processing.  The primary use case was analyzing test execution events that came off a stream (Kinesis or Pub/Sub).  The analysis phase would consist of feature extraction, applying transformations to the data, and evaluating machine learning models.  The second use case we anticipated was reprocessing events that we had previously captured.  Reprocessing old events might be necessary to correct invalid conclusions from the initial analysis (e.g. due to a bug), or it could be that we added a new type of analysis and would like to update previously-generated insights with this new information.  We knew we would need a system that could perform both streaming and batch processing.

AWS Elastic Map Reduce (EMR) allows users to launch managed Hadoop clusters, including services that run on top of Hadoop such as MapReduce, Hive, Pig, and Spark.  When we investigated comparable services on GCP we found two that were similar to EMR: Dataproc and Dataflow.  Dataproc is the closest analog to EMR in that it is a managed Hadoop cluster that can run services like Spark.  Next we looked at Dataflow.

Dataflow is a GCP managed service that implements [Apache Beam](https://beam.apache.org/).  Beam describes itself as a unified programming model for data processing that includes language-specific SDKs.  In other words, it’s not a standalone service for executing data pipelines but rather a collection of interfaces and classes that a developer can use to specify *how* the pipeline should run and *what* it should do.  In order to execute a Beam pipeline you will need to use a *Runner*.  Fortunately there are many Runners to choose from, including Dataflow, [Apache Flink](https://flink.apache.org/), and even Spark!  The variety of available Runners was attractive to us because it meant that we could migrate away from Dataflow should we decide to for any reason, and we would not need to port our code to another system since EMR supports both Spark and Flink.

At this point we saw several options: Spark on EMR or Dataproc, and Beam on EMR or Dataflow.  The first question was whether we had a preference for Spark or Beam.   A detailed comparison of the two frameworks is out of scope for this blog post, but we intend to publish follow-up blogs or tech talk slides on that topic.

Beam had a bit of an advantage from the beginning because it came along several years after similar frameworks like Spark and Storm.  The Beam developers had the opportunity to address the shortcomings of other frameworks without having to deal with legacy APIs.  One significant improvement in Beam is that it has a unified batch and stream processing API, meaning that once your pipeline is defined it is possible to use that same pipeline for either a batch job or a streaming job.  By contrast, Spark is fundamentally a batch processing system with some streaming APIs layered on top.  The developer must choose ahead of time whether to build a batch job or a streaming job.  The streaming APIs work by *discretizing* the stream, accumulating it and chunking it into mini batches that are then handed off to the standard Spark batch processing APIs.  We preferred Beam’s unified model because we knew that we would need to run the same jobs in both streaming and batch modes.

Another consideration as we were evaluating AWS and GCP for data processing capabilities was whether there were any advantages to using Dataflow over EMR.  We liked that Dataflow was presented more as a managed service than a hosted cluster.  It’s simple to deploy Dataflow jobs: just execute the job using the Dataflow Runner.  Another nice feature of Dataflow is that in many cases it will migrate your existing pipelines to the new code seamlessly.  There is no need to stand up a new cluster and tear down the old cluster.  If your changes do not alter the structure of the pipeline significantly, Dataflow will swap in the new code transparently for you.  We saw that feature as a potential time saver and a benefit to operational reliability.  After considering all of our options we felt that Beam on Dataflow was the best choice for us.

**Advantage: GCP**

###

### AWS Machine Learning vs. GCP ML Engine

One of the main product requirements of mabl was to give our customers *actionable* insights about how their applications are behaving.  We use machine learning (ML) to filter out the noise around test executions and to distill those many data points down into insights about how an application’s behavior is changing over time.  This process involves using different ML techniques and several different classes of models.

When comparing AWS Machine Learning service to GCP’s ML Engine, we immediately noticed some significant limitations in the AWS offering.  First, and most significant for us, was that AWS ML only supports a single type of ML model: logistic regression.  While logistic regression models are useful for some applications, we knew that we would need to use other techniques as well.  The second limiting factor of AWS ML is that there is no way to export the models out of the service after they have been trained, so it’s not ideal for portability.

GCP’s ML Engine is more of a general purpose computation platform that can be used for training and evaluating any type of ML model.  ML Engine service is designed to facilitate TensorFlow model training and evaluation in a Python environment that is familiar to data scientists.  It can also be accessed via APIs and client libraries in other languages, so it’s possible to train models in Python and evaluate them in Java for example.  Datalab is essentially a variant of Jupyter that integrates easily with ML Engine, BigQuery, and other GCP services.  We concluded that the GCP suite of ML services would enable us to build the kind of powerful ML tools we would need to deliver valuable insights to our customers.

**Advantage: GCP**

###

### AWS Lambda vs. GCP Cloud Functions

While providing similar functionality, Lambda is a much more mature product at this point than Cloud Functions.  Lambda supports multiple languages while Cloud Functions only supports Node.js.  At the time of evaluation (and writing) Cloud Functions was still in beta.

**Advantage: AWS**

###

### Testing support

When I was developing features on AWS one of my biggest gripes was that it was almost impossible to test your code without actually deploying it to AWS and seeing it run there.  The best you could do was try to mock out some of the AWS client interfaces, but that never really gave me much confidence that my code would have the same behavior in AWS.  The AWS service with the best unit testing capability is probably DynamoDB.  There is a local emulator that can be run in conjunction with unit tests, and while there are some differences between the emulator and the real service, the emulator is good enough to give you at least some confidence that your DynamoDB client will work when it’s running in AWS.

By contract GCP has much better testing support in most of its products.  Datastore, AppEngine, Dataflow, and even Cloud Functions have utilities that allow them to be used locally in tests to verify their behavior before you deploy to GCP.  Some of these emulators are easier to integrate into automated tests than others, but being able to test some of our most critical cloud services locally is a big advantage.  These testing capabilities allow us to catch bugs much earlier in the development process, which is particularly important for a company built around the concept of automated software testing!

**Advantage: GCP**

###

### Infrastructure and software deployment automation

It’s fairly easy to build complete environments in AWS using CloudFormation or third-party tools like Terraform.  GCP’s equivalent to CloudFormation is Cloud Deployment Manager.  Unfortunately GCP’s Deployment Manager only supports a subset of GCP services and does not seem to be as mature as CloudFormation.  AWS definitely has the edge here.

With respect to deploying software (as opposed to infrastructure) the two platforms have very different approaches.  AWS provides some tools for deploying code (such as CodeDeploy for EC2), but not all AWS services have built-in functionality for deploying code.  GCP, by contrast, has a command-line tool called gcloud that is capable of managing most GCP services as well as deploying code changes.  However, AWS benefits greatly from its larger development community, and open-source tools like Ansible have a large library of modules for managing AWS deployments.

**Advantage: AWS**

##

## Decision time

Choosing a cloud platform was one of the most difficult product development decisions we’ve had to make at [mabl](https://www.mabl.com/).  Even a few years ago there would not have been much of a discussion.  It’s great to see so much innovation and competition in the cloud platform space!

As we discussed which platform to choose we were keenly aware that neither AWS nor GCP won in every category we thought was important.  That would have been too easy!  We certainly had a preference for the features and performance characteristics of some of the core GCP services we would be using such as Pub/Sub, Datastore, Dataflow, and ML Engine.  The biggest risks in choosing GCP in our minds were:

- Many GCP services were less mature than the corresponding AWS services, and in some cases the GCP services were still in beta
- GCP had a smaller developer community
- AWS was the proverbial *devil you know*.  When it came to AWS we all knew where the bodies were buried and how *not* to use certain services and features, knowledge you can only come by the hard way.  GCP no doubt had some of the same issues, but we didn’t know what they were or how severe they would be.

Thinking back to the factors that ultimately tilted the scales in GCP’s favor, it came down to a few main themes.  First, we believed that the GCP services that would be at the core of our product were better architected for scalability and would require less manual intervention on the part of engineers to keep them running smoothly as our business grows.  At mabl we all strive to be full-stack engineers who can contribute in all areas of the product, but as software developers we’re all more interested in Dev than Ops.  The second factor was GCP’s more powerful machine learning capabilities and our perception that they were both farther ahead and more committed than AWS when it came to ML services.  Third, we were less concerned about vendor lock-in on GCP since more of its services are built around open-source frameworks and APIs like Kubernetes and Apache Beam.  Lastly, we felt there were several aspects of GCP that would accelerate our development and facilitate debugging: better unit testing support, Stackdriver monitoring and logging, and Firebase for hosting our UI assets.

The modern day version of the old adage “Nobody ever got fired for buying IBM” has to be “Nobody ever got fired for choosing AWS.”  AWS is a mature cloud platform with many great services and a huge support community.  I have no doubt that AWS is the best choice for many organizations, but as we began product development at [mabl](https://www.mabl.com/) we had an obligation to build our software around the best platform for *our company* and *our users*.  We had to choose the cloud provider that we thought would maximize our development velocity, enable differentiating feature sets, and minimize operational overhead.  To be honest I think the entire team was expecting to evaluate both platforms and choose AWS (despite our founders coming from Google!), but after an objective evaluation of the two platforms, the decision was unanimous that GCP’s services were a better fit for our needs.

### Related posts:

1.   [Dan Belcher talks automated testing with Joe Colantonio on the TestTalks Podcast](https://www.mabl.com/blog/dan-belcher-talks-automated-testing-with-joe-colantonio-on-the-testtalks-podcast)

2.   [The Fundamentals of Integration Testing](https://www.mabl.com/blog/the-fundamentals-of-integration-testing)

3.   [Ministry of Testing Slides: Why mabl Chose Google Cloud Platform (GCP) over AWS.](https://www.mabl.com/blog/ministry-of-testing-slides-why-mabl-chose-google-cloud-platform-gcp-over-aws)

4.   [mabl modern developer news roundup](https://www.mabl.com/blog/mabl-modern-developer-news-roundup-2017)