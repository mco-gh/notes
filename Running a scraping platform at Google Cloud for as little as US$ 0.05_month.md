Running a scraping platform at Google Cloud for as little as US$ 0.05/month

# Running a scraping platform at Google Cloud for as little as US$ 0.05/month

[![1*nYM23DWVeNFv2K3MouIBIw.jpeg](../_resources/3f08b4b540faf87fd85291b08278c36c.jpg)](https://medium.com/@irio?source=post_page-----6d9658982f04----------------------)

[Irio Musskopf](https://medium.com/@irio?source=post_page-----6d9658982f04----------------------)

[Sep 27](https://medium.com/@irio/running-a-scraping-platform-at-google-cloud-for-as-little-as-us-0-05-month-6d9658982f04?source=post_page-----6d9658982f04----------------------) · 6 min read

I was recently faced with the problem of finding an apartment in Berlin. Following my previous experience in this same effort, I decided to automate the task and write a software to send me an alert of the best deals. In this article, I explain how I built the foundations of this platform.

![1*pYrsDWO8Q-hHDrBHe6PMtg.jpeg](../_resources/0d1f3c14cbc6dcfa5f34cf146e23497c.jpg)
![1*pYrsDWO8Q-hHDrBHe6PMtg.jpeg](../_resources/96422704dd6d643e2a02680ed1c9b422.jpg)

Photo taken by [dronepicr](https://www.flickr.com/photos/132646954@N02/40858786523)

**The platform I've written is a Go application deployed to Google Cloud using Terraform. Also, it has Continuous Deployment from a private GitHub repository.**

* * *

*...*
After a quick research, I came to the following list of platforms to monitor:

- eBay Kleinanzeigen
- ImmobilienScout24
- Immowelt
- Nestpick

A few hours later, I have a Go binary that does everything I need to run the application locally. It uses a web scraping framework called [Colly](https://github.com/gocolly/colly) to browse all the platforms listings, extract basic attributes, and export to CSV files in the local filesystem.

Since I didn’t want to maintain the application running locally, my first choice would be to get a cheap instance at [Google Cloud](https://cloud.google.com/). Once I had this rented virtual machine, I could write a startup script to compile the app from GitHub, and set up a crontab to scrape the platforms on a daily basis.

Probably the best decision for this specific project, but could I use this personal problem as an opportunity to explore the integration of Google Cloud services?

Since, in the past, I was involved in multiple projects involving some sort of scraping application, I believed it was worth the effort. I could easily reuse this setup in the future.

My architecture started with a few premises:

- It should use Google Cloud services.
- It should support data collection every few minutes, even though I would start collecting only once a day.
- It should be as cost-effective as a cheap droplet at DigitalOcean (US$ 5).
- It should be easy to deploy. Ideally, it should implement Continuous Deployment.
- It should support to trigger a data collection process over demand — e.g., after an HTTP POST request.

My hypothesis was that I didn't need a virtual machine running 24/7; thus, it should not cost the same as a full month price. In fact, my application was able to download all the properties I was interested in under 3 minutes, so I expected something significantly lower.

# The architecture

![1*eSekmsMBKDdoNugqDvMMww.png](../_resources/dfc5ffa647df8c545520ed662bb6e5b3.png)
![1*eSekmsMBKDdoNugqDvMMww.png](../_resources/698cd57ea2bdf9daa01adbed75b89cfc.png)

My exploration through the latest Google Cloud services resulted in finding [Cloud Run](https://cloud.google.com/run/), a service that “run(s) stateless containers on a fully managed environment or in your own GKE cluster.” Still classified as a beta product by Google Cloud, it is built on top of [Knative](https://knative.dev/) and [Kubernetes](https://kubernetes.io/). The key proposal is its pricing model: it charges in chunks of milliseconds rather than hours of runtime.

With a few tweaks, my Go application was wrapped in a Docker container to be runnable by Cloud Run. Once it gets a HTTP POST request, it collects attributes from all the advertised properties and publishes as CSV files to a Google Storage bucket. For my use case, I created two possible ways to hit this endpoint: an Internet-accessible address so I can trigger it whenever I want, and through Cloud Scheduler, which is configured to hit it once a day.

# The application

The application is fairly simple: it consists of an HTTP server with a single endpoint. On every hit, it scrapes all the platforms and saves results in CSVs inside a Storage bucket.

![1*FmZEzqlusjW54DnfX9xtqA.png](../_resources/475273cee91e10b99d0bd191f390aae3.png)
![1*FmZEzqlusjW54DnfX9xtqA.png](../_resources/ba4588da024a83e7142187a7376fe173.png)

## ./main.go

![1*TarFriZVRgIrDDs02Qt8yA.png](../_resources/f473a9a519f9c1a8e50f7a8a46af40fc.png)
![1*TarFriZVRgIrDDs02Qt8yA.png](../_resources/8cf19ab8e57b4f24afad6e40c42d0b65.png)

## ./Dockerfile

![1*onH1PJ5pjYf5-PB2BoqzZA.png](../_resources/355ca277e1836c6b842891b4ef0e3a3d.png)
![1*onH1PJ5pjYf5-PB2BoqzZA.png](../_resources/8f06baa1743c359dccab00c4809edd21.png)

Other application files can be found in [this Gist](https://gist.github.com/Irio/3da6ee4dea8cad6613c1337a15044f09). All the feedback is appreciated, as this is one of my first Go projects.

# The deployment

1. [Install Terraform](https://www.terraform.io/).

2. [Install Google Cloud CLI](https://cloud.google.com/sdk/docs/quickstarts) and sign in to your account *with

****$ gcloud auth login***

3. [Create a Google Cloud project](https://console.cloud.google.com/projectcreate) and configure the CLI to use it with

**$ gcloud config set project PROJECT_NAME**

4. [Create a Google Cloud Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts) for using with Terraform, giving it the “Owner” role.

5. Create and download a JSON key for this new service account. Place it in **deployment/credentials.json**

6. [Enable the following Cloud APIs](https://console.developers.google.com/apis/library):

* App Engine Admin API
* Cloud Build API
* Cloud Run API
* Cloud Scheduler API

7. [Give appropriate roles](https://console.cloud.google.com/iam-admin/iam) to the API service account ending with **@cloudbuild.gserviceaccount.com**:

* Cloud Run Admin
* Cloud Run Service Agent

8. Create a [Cloud Source Repository](https://source.cloud.google.com/repo/new) based on your GitHub repository.

9. Set appropriate variable values in **terraform.tfvars**.

Now with permissions already given, use Terraform to set up the rest of the infrastructure.

**$ cd deployment
$ terraform init
$ terraform apply**

The initial deployment may take about five minutes since Terraform waits for Cloud Run to build and start before configuring Cloud Scheduler.

Since Cloud Run is still in beta — with API endpoints in alpha stage —I was not able to declare all the infrastructure in Terraform files. As a temporary workaround, I’ve written a couple of auxiliary bash scripts that trigger the Cloud API through its CLI command. Fortunately, all this happens in background when a developer triggers **terraform apply**.

* * *

*...*

# The result

Every day, without any human interaction, Cloud Scheduler creates a new folder with a number of CSV files with the most recently available apartments in my city.

![1*Dsf0wgbMdWFuFTJRKeBFng.png](../_resources/8cf49ba57c80f654daf3d7b6385f2b8b.png)
![1*Dsf0wgbMdWFuFTJRKeBFng.png](../_resources/523f94102ed332c1386dbec064f3db66.png)

# The costs

Not all the services in use are available in the [official calculator](https://cloud.google.com/products/calculator/#id=2e6bb472-7ce9-4dd2-a2b9-15502f810fb9). Either way, I've made a rough estimation for my personal use, considering an unrealistic number of one deployment each day.

## Cloud Storage — US$ 0.02/month

- Location: US
- Class A operations: 4*30 = 120
- 1st month
- Storage: 2MB*30 = 60MB
- 12nd month
- Storage: 2MB*365 = 730MB

## Cloud Run — US$ 0.00/month

- Location: us-east1
- Cpu allocated: 1
- Memory allocated: 1GB
- Concurrent requests per container instance: 1
- Execution Time per Request (ms): 5000
- Outbound Network Bandwidth per request execution (KB): 1000
- Requests per Month: 30

## Cloud Build — US$ 0.00/month

- free quota of 120 builds-minutes/day
- 4 build-minutes/day

## Container Registry — US$ 0.02–0.19/month

- $0.026/GB
- 1st month
- 20MB*30 = 600MB
- 600/1024 * 0.026 = 0.02
- 12nd month
- Storage: 20MB*365 = 7300MB
- 7300/1024 * 0.026 = 0.19

## Cloud Source Repositories — US$ 0.00/month

- free quota of 5 project-users
- 1 project

## Cloud Scheduler — US$ 0.00/month

- free quota of 3 free jobs/month
- 1 job

* * *

*...*

For comparison, an f1-micro instance — with 0.6GB of RAM — running over a full month on Google Cloud, is included in the free tier; a g1-small instance, with 1.7GB, would cost US$ 13.80 per month. Also, it is reasonable to consider the cost could decrease or increase depending on how accurate were my initial assumptions and further optimizations.