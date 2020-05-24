Google Cloud Run - Minimizing Cold Starts - John Hanley

# [Google Cloud Run – Minimizing Cold Starts](https://www.jhanley.com/google-cloud-run-minimizing-cold-starts/)

[![animal-animal-photography-big-cat-2541239_800x450-768x432.jpg](../_resources/f51af83567008fb60d00ccac1b7ab8bb.jpg)](https://www.pexels.com/photo/photo-of-tiger-and-cub-lying-down-on-grass-2541239/)

## Introduction

This article discusses Google Cloud Run cold starts, what they are and how to avoid cold starts.

## What is Cold Start?

[Cloud Run](https://cloud.google.com/run/) is a stateless HTTP serverless container service that provides on-demand services that autoscales to zero instances. Cloud Run is based upon [Docker Containers](https://www.docker.com/resources/what-container) and [Knative](https://cloud.google.com/knative/). The first time that a Cloud Run instance starts running requires downloading the container image and starting the container. This time is called “cold start”. The opposite is “warm start” which means that the container is already running waiting for or already processing requests.

Cloud Run scales to zero instances when there is no traffic. After an unspecified time, Google will terminate unused Cloud Run containers. The next time a request arrives, a new container must be started and this requires time. How long? About two seconds.

## How can I minimize Cold Starts?

- If you use a dynamic language with dependent libraries, the load time for those modules adds latency during a cold start. Reduce startup latency in the following ways:
    - Minimize the number and size of dependencies to build a lean service.
    - Lazily load code that is infrequently used, if your language supports it.
    - Use code-loading optimizations such as PHP’s [composer autoloader optimization](https://getcomposer.org/doc/articles/autoloader-optimization.md).
- Use Global Variables
    - In Cloud Run, you cannot assume that service state is preserved between requests. However, Cloud Run does reuse individual container instances to serve ongoing traffic, so you can declare a variable in global scope to allow its value to be reused in subsequent invocations. Whether any individual request receives the benefit of this reuse cannot be known ahead of time. An example is creating the database connection at container cold start and then reusing that connection when processing requests.
- Minimize Container Image Size. This provides a number of benefits beyond decreasing cold start times:
    - Increased security vulnerability because more code is a larger attack surface.
    - Slower build time for your container image while many files are downloaded.
    - Slower deployment time for your service as the container image is prepared for use in a new revision.
    - Increased network egress costs with Container Registry if your container storage bucket is geographically distant from your service region.
- Periodically Poll your Cloud Run Service. You can use Google Cloud Scheduler to call your Cloud Run service on a scheduled basis. Although Google does not publish the length of time before a container is shut down, periodically calling Cloud Run will keep the containers warm. Select a polling time, such as one minute and then review Stackdriver logs under “Cloud Run Revision” to see if there are any messages about container termination or container starts. For example, with Python and Flask, when a container starts the message “Serving Flask app “app-name” (lazy-loading) is logged. This message means a container cold start. Another example is the message “This request caused a new container instance to be started and may thus take longer and use more CPU than a typical request.
- Do not allow your application to crash. This will cause the container to be terminated and a new container to be started. Within your code, process all errors and exceptions.

## Additional Information

- [Google Clou Run Development Tips](https://cloud.google.com/run/docs/tips)
- Ahmet’s [Curated unofficial FAQ for the new Google Cloud Run](https://github.com/ahmetb/cloud-run-faq#cold-starts)

## Credits

I write free articles about technology. Recently, I learned about [Pexels.com](https://www.pexels.com/) which provides free images. The image in this article is courtesy of [Waldemar Brandt](https://www.pexels.com/@wb2008) at Pexels.

#### John Hanley

[Author archive](https://www.jhanley.com/author/john-hanley/)[Author website](http://www.jhanley.com/)[@NeoPrimeAws on Twitter](http://www.twitter.com/NeoPrimeAws)

July 6, 2019
[Cloud](https://www.jhanley.com/category/cloud/)

[Container Cold Start](https://www.jhanley.com/tag/container-cold-start/), [Google Cloud Run](https://www.jhanley.com/tag/google-cloud-run/)

[Previous post](https://www.jhanley.com/google-cloud-http-load-balancer-file-upload-error/)[Next post](https://www.jhanley.com/google-cloud-platform-getting-started/)

### Leave a Reply