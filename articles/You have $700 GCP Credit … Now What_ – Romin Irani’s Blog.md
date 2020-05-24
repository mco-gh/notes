You have $700 GCP Credit … Now What? – Romin Irani’s Blog

# You have $700 GCP Credit … Now What?

Several folks have approached me that they received [Google Cloud Platform](https://cloud.google.com/) credits during Google IO 2017 or in the last few months and they are not sure how to use the credit. This blog post is a direct result of that, where I thought of putting together 10 ways in which you could ***start ***utilizing that credit and learn more about [Google Cloud Platform](https://cloud.google.com/).

> Note: Make sure that you have redeemed your GCP credits via the link that was given to you and that you have created a Google Cloud Platform Billing Account with a credit card associated with it. Here is a > [> link](https://crunchify.com/how-to-redeem-google-cloud-platform-gcp-credit-in-admin-console/)>  on how you do that.

So what are things that you can do to put your credit to good use (in no order of importance):

### Learn the platform

If you are a new to the platform, the first question on your mind is where to begin? It is not an easy path to navigate and your point is well taken. But there is good help on the way in the form of Google Cloud Courses that are available on MOOC platforms like Coursera. I suggest that you start with those and the first course that you should do is [**Google Cloud Platform Fundamentals**](https://www.coursera.org/learn/gcp-fundamentals), which should take about 6–10 hours to complete.

Multiple courses on Google Cloud, including this basic one have just got started on Coursera and you should join one. Check out [my post](https://rominirani.com/google-cloud-courses-on-coursera-2581657f1217) on the courses available to take today.

Before you jump on to beginning a course, I suggest you watch a video that helps you navigate the Google Cloud Platform. This is important and will hold you in good stead for the points that come up next.

![](../_resources/3e4b0f68403f51ad32edbd3990a9fdb0.png)

### Learn Linux or spin up a few Virtual Machines (VMs)

Always wanted to learn Linux but have not got around to learning it? Or just want to practice a few Linux commands? Or better still, you need a Virtual Machine to try out a few things?

Well , [Google Compute Engine](https://cloud.google.com/compute/) can come to your rescue. It is the core piece of the Infrastructure as a Service (IaaS) that provides scalable and high-performance virtual machines.

Hey, what if you just want a Windows machine in the cloud? Sure — Google Compute Engine provides that too!

Check out these [quick starts on both Linux and Windows](https://cloud.google.com/compute/docs/quickstarts) (pick your choice .. both are good!):

- •[Linux VM](https://cloud.google.com/compute/docs/quickstart-linux)
- •[Windows VM](https://cloud.google.com/compute/docs/quickstart-windows)

> One of the coolest features (tools) that is available to you as you get more familiar with the Google Cloud Platform is your own Linux Developer Machine in the cloud that you can use to manage all your Google Cloud Platform Resources. It is called the > [> Google Cloud Shell](https://cloud.google.com/shell/docs/)>  and it sure is available to you. Check it out.

### Containers ! Containers! Containers!

![](../_resources/ad6e0d35e812473932d9777d55e8059c.png)

Image Reference: https://cdn.meme.am/cache/instances/folder573/500x/56291573/toy-story-everywhere-containers-containers-everywhere.jpg

You must have heard of how containers are revolutionizing the way to build, ship and run our applications. You have definitely heard about Docker but are still itching to try out some commands to see if it is working. Or you are already familiar with Docker and have now started to understand that you need to have Container Orchestration software like Kubernetes to let you define your application state and let Kubernetes take care of managing the fleet of machines to help serve your application (Distributed Systems Challenges — not an easy problem to solve but Kubernetes does it!).

If any of the above sounds interesting, you should get started and here are some pointers:

- •**Try out Docker**: The [Google Cloud Shell](https://cloud.google.com/shell/docs/) as pointed out earlier is your development machine in the cloud. It is a virtual machine that is created for you and setup with most tools that developers use today, including SDKs for multiple languages and yes, you guessed it right … Docker Tool. All you need to do is login to your Google Cloud Shell and you are all set. Once you have done that, check out a [Docker Tutorial](https://rominirani.com/docker-tutorial-series-a7e6ff90a023) and also understanding why it makes sense to learn Docker on a Cloud machine via this video by Ray Tsang:

![](../_resources/6bd1cfe039bdd732670b34af5516c2ce.png)

- •**Try out Kubernetes**: If you are familiar with Docker and want to learn more about the #1 Orchestration software for managing containers at scale, then why not try out learning the fundamentals by using Google Container Engine (GKE), which is a fully managed cluster. The fully managed aspect is very important since Google is responsible for running the managing the cluster, while you achieve distributed systems nirvana for your container apps. Where do you start? Take the [Google Container Engine Quick Start](https://cloud.google.com/container-engine/docs/quickstart) for a drive today.

### Code Labs

Who does not like code labs? These are fantastic hands-on tutorials that have been crafted by Google to introduce you to multiple areas of Google Cloud Platform. They range from 10 minutes to 120/150 minutes and you can take them from a place and at a time of your choice.

The Code Labs for Google Cloud are available here:

[***Google Codelabs*** Google Codelabscodelabs.developers.google.com](https://codelabs.developers.google.com/?cat=Cloud)[(L)](https://codelabs.developers.google.com/?cat=Cloud)

Try a few ones out and bookmark this for sure. Anytime you want to learn more about a service available in GCP, come back here.

> Access them anytime at > [> g.co/codelabs](https://g.co/codelabs)

### Functions as a Service

Developers are getting excited about [Serverless Architectures](https://martinfowler.com/articles/serverless.html) or Functions as a Service (FaaS). They are a new way in which you can architect your applications using functions, events and fully-managed cloud services at economies of scale and cost, that is fundamentally different from before.

Amazon Web Services with its [AWS Lambda](https://aws.amazon.com/lambda/) offering took a lead and has gained significant mind share, but did you know that GCP supports this via the [Google Cloud Functions](https://cloud.google.com/functions/) service?

The premise is simple on the surface. You can write your functions in JavaScript and then string them together in a process driven primarily via asynchronous events like a file getting uploaded to Google Cloud Storage, or triggering on demand, etc.

Currently, Google Cloud Functions supports JavaScript language only and you can get started with it via a couple of tutorials that I would suggest:

- •[HTTP Trigger tutorial](https://cloud.google.com/functions/docs/tutorials/http)
- •[Cloud Storage tutorial](https://cloud.google.com/functions/docs/tutorials/storage)

### Firebase

If you are a mobile developer, chances are that you have heard about [Firebase](https://firebase.google.com/). Firebase is now a complete platform and gone are the days when you only looked at it as a real-time database in the cloud. It provides a platform now for not just developing & testing your mobile application but also for growing and engaging your audience.

For those of you who would like an introduction to Firebase and understand the whole picture, take a look at this video first:

![](../_resources/0238fcdc2bc8c17060da8142ac21d792.png)

But what is key here is to understand that Firebase is now closely integrated with multiple Google Cloud Platform services. What this means is that since you have the GCP credits, start using them in conjunction with your Firebase driven application to take it to the next level.

You can use Google Cloud Storage aka GCS (this is mentioned in a later part of this article) in conjunction with Firebase. Store and serve large object content (attachments, audio, video, etc) from GCS in your Firebase App. We talked about Google Cloud Functions in the previous section. Guess what, [Firebase Cloud functions](https://firebase.google.com/docs/functions/) is the perfect integration of Serverless functions in conjunction with events that you would expect from your Firebase database. For e.g. Send an email (written as a function) if a new record is added to the subscriber database.

Look at all the use cases that Firebase Cloud Functions can enable:

[**What Can I Do with Cloud Functions? | Firebase** *Developers can use Cloud Functions to keep users engaged and up to date with relevant information about an app…*firebase.google.com](https://firebase.google.com/docs/functions/use-cases)[(L)](https://firebase.google.com/docs/functions/use-cases)

Check out this video too on building modern applications with Google Cloud Platform and Firebase:

![](../_resources/738dd781532a2ef9412b2e2298fac9e3.png)

### Big Data Processing

The world loves data and lots of it. But making sense out of data is the tough but extremely rewarding part. If you have been working with Big Data, the challenge is in handling large amounts of data in batch/stream mode, analyzing them, transforming it and more. Doing this at scale while running the complex infrastructure and software is not for everyone.

This is where Google Cloud Platform really shines with a fully-managed set of services in the Big Data space. Do you use Hadoop and Spark in your projects? If yes, try out Cloud Dataproc that spins up a Hadoop cluster in seconds, allowing you to run your Spark jobs and even tearing down the cluster once you are done with it. Magical? Try out this codelab:

[**Introduction to Cloud Dataproc: Hadoop and Spark on Google Cloud Platform** *Cloud Dataproc is a managed Spark and Hadoop service that lets you take advantage of open source data tools for batch…*codelabs.developers.google.com](https://codelabs.developers.google.com/codelabs/cloud-dataproc-starter/index.html#0)[(L)](https://codelabs.developers.google.com/codelabs/cloud-dataproc-starter/index.html#0)

Or better still, check out [Graham Polley](https://twitter.com/polleyg)’s article on Google Cloud Dataproc and the 17 minute train challenge:

[**Google Cloud Dataproc and the 17 minute train challenge** *My work commute My commute to and from work on the train is on average 17 minutes. It's the usual uneventful affair…*shinesolutions.com](https://shinesolutions.com/2015/10/14/google-cloud-dataproc-and-the-17-minute-train-challenge/)[(L)](https://shinesolutions.com/2015/10/14/google-cloud-dataproc-and-the-17-minute-train-challenge/)

Heard about BigQuery? If not, you must take a look at it. Consider it as your Analytics Warehouse in the Cloud (again fully managed) where you simply load your data and perform SQL queries on it that run magically in seconds across GBs and TBs of data. Behind the scenes, the queries are run for you across clusters but you don’t have to worry about that. You ask questions of your Big Data and you get the answers.

Don’t believe me? Check out this video on what BigQuery is about?

![](../_resources/ac499807a246323b9d3e75f2b3ea5782.png)

Google also makes available large datasets for you to simply query. Check these out:

[**Google BigQuery Public Datasets | BigQuery Documentation | Google Cloud Platform** *BigQuery is a fully managed data warehouse and analytics platform. The public datasets listed on this page are…*cloud.google.com](https://cloud.google.com/bigquery/public-data/)[(L)](https://cloud.google.com/bigquery/public-data/)

### Machine Learning

Machine Learning is all over the place and it is only a matter of time before it finds it way through most applications. But where do you start? You must have heard about the tons of mathematics that one needs to know to get started with it. The fact of the matter is that Google Cloud Platform provides a spectrum ranging from just using the Machine Learning APIs and then moving on to hosting your own Machine Learning models in the cloud.

I suggest that you first start off with using existing [Machine Learning APIs](https://cloud.google.com/products/machine-learning/) that provides powerful ammunition to anyone looking at addressing challenges that could involve:

- •Image Analysis ([Cloud Vision API](https://cloud.google.com/vision/))
- •Text Sentiment Analysis ([Cloud Natural Language API](https://cloud.google.com/natural-language/))
- •Voice to Text Translation ([Cloud Speech API](https://cloud.google.com/speech/))
- •Language Translation ([Cloud Translation API](https://cloud.google.com/translate/))
- •Video Analysis ([Cloud Video Intelligence API](https://cloud.google.com/video-intelligence/))

These APIs provide you a dead simple REST API to embed Machine Learning in your applications. Make no mistake that these REST APIs are front-ending powerful Machine Learning models that have been built over years with tons of training data thrown at them. The best part is that it is going to get better and more accurate over time, with improvements in terms of accuracy and latency being a given.

![](../_resources/9c73e3ed646c8595743f5d8e1c5fd46f.png)

If you are still on the fence, I suggest that you give this [Cloud Vision API](https://cloud.google.com/vision/) page a try. Go to Try the API section on the page. You will be impressed with the capability and then imagine if you had to build something like that. Instead, I suggest to stand on the shoulders of these great APIs and build the next Wow! application.

Get started with these videos to see the Machine Learning APIs in action:

![](../_resources/273ff27fe70a92bbc5f68e094157f811.png)

### Cloud Launcher

Say you want to run a Wordpress on Google Cloud or a MongoDB on Google Cloud or another popular application? The [Google Cloud Launcher](https://cloud.google.com/launcher/) is just that. It is the fastest way to get started with GCP and provides you production grade installations in just a few clicks.

Here are some popular solutions:

![](../_resources/5033b6f066f778a9785d3fe7daf67e04.png)

At the time of writing, there are 200+ solutions in the Google Cloud Marketplace that you can deploy with a few clicks. It includes Databases, Blog & CMS, Developer Tools, Operating Systems and more.

### Data Storage

Google Cloud Storage provides multiple data storage options depending on your needs. It provides the following:

- •Object Store called [Google Cloud Storage](https://cloud.google.com/storage/)
- •NoSQL database called [Cloud Datastore](https://cloud.google.com/datastore/)
- •Fully Managed MySQL and PostgreSQL(Beta) called [Cloud SQL](https://cloud.google.com/sql/)
- •Fully Managed Relational Database with strong consistency and horizontal scalability across regions called [Cloud Spanner](https://cloud.google.com/spanner/)

Pick your choice of storage based on the requirements that you might have. For example, if you need a relational database for your hobby project, go ahead and spin up a Cloud SQL instance.

Choosing a storage option is not an easy task. Google Cloud makes available a [guide](https://cloud.google.com/storage-options/) to help you make the decision. Definitely take a look, even if you don’t end up using this service for a refresher on storage options. Here is a great flowchart from the official documentation:

![](../_resources/38437739e22c64629288ea0bca0b3289.png)

### Platform as a Service (PaaS)

App Engine in my book was the original PaaS that led to a huge number of applications being written on the platform. The standard run time version of App Engine supports Java, Python, Go and PHP.

If you are looking to write an application and let Google (App Engine) do the hard work of provisioning the app for you and running it for you, give App Engine a serious look. Like all PaaS , there are certain restrictions in the way that you write your code, libraries that you can use,etc. but if you are fine with that adjustment, you can huge scale and a serverless way of running your application. And best of all, it is hosted on the Google network that spans the globe and is the best in class.

Want to know how easy it is to deploy a App Engine application to the cloud? Check out this video:

![](../_resources/25333bb427185e95b251d895a133bf5f.png)

Another talk that is very important is to understand what kind of application is best suited for the multiple options that are there on Google Cloud Platform i.e. Google Compute Engine, Google App Engine and Google Container Engine. This talk explains it well:

![](../_resources/ee190d57ef34b87bd4149a753d6b7fa2.png)

### Release an API

Web APIs changed the way applications talk to each other. It also allowed API only companies to thrive and chances are that you have definitely used some API or the other in your application.

But what about writing your own API and releasing it for your other applications (think mobile applications) or even the world? If you have an interesting idea for an API, I suggest that you go for it. [Google Cloud Endpoints](https://cloud.google.com/endpoints/) provides a great way for you to start writing and deploying your API for the world to use.

![](../_resources/d7eac52bbd37a83282ceb8c5cb6f19ad.png)

Google Cloud Endpoints provides you the ability to use their standard framework to write APIs or even using frameworks like Swagger. They are then hosted on Google infrastructure with logging and security all handled for you. Check out the Cloud Endpoints Quick Start that provides you multiple options of writing your APIs hosted on App Engine, Compute Engine, running in Docker or even in Kubernetes.

[**Tutorials | Cloud Endpoints | Google Cloud Platform** *Troubleshooting App Engine Flexible Deployment*cloud.google.com](https://cloud.google.com/endpoints/docs/tutorials)[(L)](https://cloud.google.com/endpoints/docs/tutorials)

If you believe that your idea for a utility API is too small, take inspiration from this article where a developer identified a need, built out an API and now sees over 250 million API requests for day:

[**How I Took an API Side Project to over 250 Million Daily Requests With a $0 Marketing Budget** *Finding someone to market an API is like finding a unicorn. They need the technical knowledge to understand the API in…*blog.ipinfo.io](https://blog.ipinfo.io/api-side-project-to-250-million-requests-with-0-marketing-budget-bb0de01c01f6)[(L)](https://blog.ipinfo.io/api-side-project-to-250-million-requests-with-0-marketing-budget-bb0de01c01f6)

To scale to that level, you will need to go with a platform that can scale and Google Cloud Platform is definitely one of those.

#### Parting notes

Remember that Google Cloud Platform comes with a generous free tier for most of its services, which means that if you are well within that tier in terms of resource usage, you will not be charged for it or in other words, you credit will remain intact. **But my whole purpose here is to get you started with some services** and eventually you end up liking it so much, that you move up the chain in terms of your usage and that’s when your credits will come in real handy.

If you are from the AWS or Azure world, one of the things that you absolutely need to help you jumpstart things on the Google Cloud Platform is a guide that can tell you what equivalent services are there on GCP. Check these guide out:

[**Map AWS services to Google Cloud Platform products | Google Cloud Platform Free Tier | Google Cloud…** *(2) AWS Elastic Beanstalk and App Engine are often described as similar offerings, but there are significant…*cloud.google.com](https://cloud.google.com/free/docs/map-aws-google-cloud-platform)[(L)](https://cloud.google.com/free/docs/map-aws-google-cloud-platform)

[**Map Microsoft Azure services to Google Cloud Platform products | Google Cloud Platform Free Tier …** *(1) Microsoft Azure App Services and App Engine are often described as similar offerings, but there are significant…*cloud.google.com](https://cloud.google.com/free/docs/map-azure-google-cloud-platform)[(L)](https://cloud.google.com/free/docs/map-azure-google-cloud-platform)

The above 10 suggestions form a short list of much more that you can do with Google Cloud Platform. In my experience, $700 in Cloud Credits is an extremely generous amount to learn and familiarize with various services available with Google Cloud Platform. As one of the leading Cloud Platforms available today, it pays to utilize that credit. Start now … you still have nearly 6 months to go for 2017 :-)