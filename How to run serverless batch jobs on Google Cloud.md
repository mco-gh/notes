How to run serverless batch jobs on Google Cloud

# How to run serverless batch jobs on Google Cloud

## Use AI Platform for functions that take longer than a couple of minutes

[![1*opbfQNyOl9EgY6qWxwj_Xw.jpeg](../_resources/2cceeb40aa41069476a4f6f7a8056c93.jpg)](https://medium.com/@lakshmanok?source=post_page-----ca45a4e33cb1----------------------)

[Lak Lakshmanan](https://medium.com/@lakshmanok?source=post_page-----ca45a4e33cb1----------------------)

[Sep 30](https://medium.com/google-cloud/how-to-run-serverless-batch-jobs-on-google-cloud-ca45a4e33cb1?source=post_page-----ca45a4e33cb1----------------------) · 2 min read

Cloud Functions, Cloud Run, AppEngine, etc. are not a good choice for long-lived functions, i.e., anything that takes longer than a couple of minutes to run (the services themselves impose a limit of 10 or 15 minutes, but that includes errors and retries, so your goal should be 2–3 minutes maximum). If you want to run a function that will take longer than this, what are your options?

![1*Ek5RG39Ky3XVKE3RaFoPVA.png](../_resources/f4340f18c059b8716363b9a777643825.png)
![1*Ek5RG39Ky3XVKE3RaFoPVA.png](../_resources/5216f3743a18a174d1b14922030645cd.png)
What if you want to run a long-running batch job in a serverless way?

Put your code in a Docker container. Run it using AI Platform. Schedule it using Cloud Scheduler.

## Custom containers in AI Platform Training

You can use AI Platform Training to [run any arbitrary Docker container](https://cloud.google.com/ml-engine/docs/custom-containers-training) — it doesn’t have to be a machine learning job. To have some arbitrary container executed on a GPU, you’d just do:

gcloud ai-platform jobs submit training gpu_function \
--scale-tier BASIC_GPU \
--region $REGION \
--master-image-uri gcr.io/$PROJECT_ID/some-image-name

This is just a REST API, so you have a variety of client libraries in a bunch of programming languages to invoke this from. There are no requirements for the container — just that it needs to have an entry point and that it is published in the container registry. It is possible to use custom machine types — see the [documentation](https://cloud.google.com/ml-engine/docs/custom-containers-training) for details.

## Concurrent autoscaling?

Being able to launch a custom container on a job-specific cluster satisfies a number of use cases for serverless functions. But not all of them. Specifically, another use case for serverless functions is concurrent autoscaling — we want to be able to receive multiple requests, and route them to the same machine and once that machine starts to get overwhelmed, we’d like to add more machines. If you need concurrent autoscaling and your tasks last longer than 2–3 minutes, the AI Platform Training solution will not work. You’ll need Kubernetes in that case, and it won’t be serverless.