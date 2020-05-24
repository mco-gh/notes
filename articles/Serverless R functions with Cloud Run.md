Serverless R functions with Cloud Run

#

Serverless R functions with Cloud Run

###

[eric.webp](../_resources/d9c53b98129ca0551996f07344b1288b.webp)
Eric Jinks — September 2nd, 2019

> [> Cloud Run with R – Hello World (GitHub)](https://github.com/Jinksi/cloudrun-helloworld-r)

If you're a JavaScript developer, using [serverless functions](https://en.wikipedia.org/wiki/Serverless_computing) can be a great way to create auto-scaling, cost-effective APIs. [Any](https://www.netlify.com/products/functions/)  [cloud](https://cloud.google.com/functions/)  [provider](https://azure.microsoft.com/en-us/services/functions/) who can host serverless functions will support JS and probably has solid workflows, allowing you to write the code and simply `git push` to deploy.

If you're a developer or data scientist working with [R](https://en.wikipedia.org/wiki/R_(programming_language)), you are not so lucky! R is not natively supported on any of the major serverless cloud providers (yet). Thankfully, there is a solution that is beginning to gain traction with cloud platforms called **Serverless Containers**. I am using [Google Cloud Run](https://cloud.run/) to host and manage serverless containers. Cloud Run provides a genorous 'free tier' so you can try it out without cost. It can be extended to utilise custom machine types, including GPU support, which can be critical if you are running Machine Learning tasks.

Serverless containers enable us to write code in any language and with any dependencies or libraries. We bundle up our functions into [Docker](https://www.docker.com/resources/what-container) containers, deploy them and pay only when they are running. If the function is getting hit with a spike in traffic, more containers will be spun up instantaneously to handle the workload and deallocated again once the task is complete.

## R on the backend

In my case, I was using R to generate geospatial map data that would be rendered using a frontend React web app. I used the R library [`plumber`](https://www.rplumber.io/) to create a REST API, exposing https endpoints handled by functions defined in `app.R`.

To define endpoints with `plumber`, parameters are defined by decorating R functions with special comments.

The function below will accept `POST` requests with `lat` and `lon` data, returning geojson data:

	# app.R

	library(geojsonio)

	#' Generates geojson containing 70 points surrounding central coordinate
	#' @param lat latitude of central coordinate
	#' @param lon longitude of central coordinate
	#' @post /geojson
	function(lat, lon){
	  lat <- as.numeric(lat)
	  lon <- as.numeric(lon)
	  maxRange <- 0.1
	  n <- 70

	  # Generate data
	  df <- data.frame(
	    lat = runif(n, min = lat - maxRange, max = lat + maxRange),
	    lon = runif(n, min = lon - maxRange, max = lon + maxRange),
	    magnitude = runif(n, min = 0, max = 1)
	  )

	  # create geojson string from dataframe
	  geojsonString <- geojson_json(df)

	  # data to return
	  geojsonString
	}

	print('app.R running')

`server.R` sets up the server to listen on a specific port. This also enables a [Swagger](https://swagger.io/) interface for exploring the REST API.

	# server.R

	library(plumber)
	# 'app.R' is the location of the file containing your endpoint functions
	r <- plumb("app.R")
	# get port number from environment variable
	port <- strtoi(Sys.getenv("PORT"))
	r$run(port=port, host='0.0.0.0', swagger=TRUE)

## Defining a Docker container

A `Dockerfile` is used to define the Docker container requirements, install R libraries and start our server script.

	# Use the official R image
	# https://hub.docker.com/_/r-base
	FROM r-base

	# Create and change to the app directory.
	WORKDIR /usr/src/app

	# Copy local code to the container image.
	COPY . .

	# Install any R packages
	RUN Rscript -e "install.packages('plumber')"

	EXPOSE 8080

	# Run the web service on container startup.
	CMD [ "Rscript", "server.R"]

If you have Docker installed locally, you can build and run this container using the following commands:

- Build: `docker build . -t 'cloudrun-r-helloworld'`
- Run: `docker run -p 8080:8080 -e PORT=8080 cloudrun-r-helloworld`

## Deploying to Cloud Run

Now that we have out Docker container ready to go, let's deploy our container to Cloud Run. There are a couple of ways we can do this, the [Cloud Run Docs](https://cloud.google.com/run/docs/quickstarts/build-and-deploy) explains the manual way to deploy. To summarise, we tell Cloud Build to build the docker image and push it to Container Registry, then use this image to deploy a new revision to Cloud Run.

If you want to get a clone of my hello world example deployed on Cloud Run quickly, click this Cloud Run Button:

[![button.png](../_resources/688b6a91ec3a9cc6232fe287cc194d11.png)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/Jinksi/cloudrun-helloworld-r.git)

> Take a look at the > [> Cloud Run Button repo](https://github.com/GoogleCloudPlatform/cloud-run-button)>  to create your own.

## Continuous deployment with `git push`

Rather than manually deploying, I prefer to commit my changes to a Git repository and let deployment happen *automagically*.

We can use Google's [Cloud Build](https://cloud.google.com/cloud-build/) to automate the deployment of our container each time we push to a git repo. You will need to have your code in a `git repo` hosted on Github or another cloud git repository.

> If you are running this for the first time, you may have to enable GCP Billing and APIs. See the > [> Cloud Run Docs](https://cloud.google.com/run/docs/continuous-deployment)

To use Cloud Build we create a `cloudbuild.yaml` file and commit it to the repository root folder.

	# cloudbuild.yaml

	# Replace $PROJECT_ID with your GCP project ID
	# Replace [SERVICE-NAME] with the desired Cloud Run service name (e.g. hello-world)
	# Replace [REGION] with the GCP region you are deploying to (e.g. asia-northeast1)

	steps:
	  # build the container image

	  - name: 'gcr.io/cloud-builders/docker'

	    args: ['build', '-t', 'gcr.io/$PROJECT_ID/[SERVICE-NAME]', '.']
	    # push the container image to Container Registry

	  - name: 'gcr.io/cloud-builders/docker'

	    args: ['push', 'gcr.io/$PROJECT_ID/[SERVICE-NAME]']
	    # Deploy container image to Cloud Run

	  - name: 'gcr.io/cloud-builders/gcloud'

	    args:
	      [
	        'beta',
	        'run',
	        'deploy',
	        '[SERVICE-NAME]',
	        '--image',
	        'gcr.io/$PROJECT_ID/[SERVICE-NAME]',
	        '--region',
	        '[REGION]',
	        '--platform',
	        'managed',
	        '--quiet',
	      ]
	images:

	  - gcr.io/$PROJECT_ID/[SERVICE-NAME]

Now to create a Cloud Build trigger:

1. Go to the [Cloud Build triggers page](https://console.cloud.google.com/cloud-build/triggers)

2. Click **Create Trigger**
3. Select your repository
4. Select `cloudbuild.yaml` in *Build Configuration*
5. Click **Create**
6. Push a change to your repository

7. Monitor build progress in the [Cloud Build console](https://console.cloud.google.com/cloud-build/builds)

Once this is setup, anytime you push to this repository, Cloud Build will build the Docker container and deploy a new revision to Cloud Run

[Read more in the Cloud Run docs](https://cloud.google.com/run/docs/continuous-deployment).

## Hello Cloud Run

Now that we have deployed our container to Cloud Run, we can sit back and be confident that our R functions will *just work* without having to manage servers, load balancing, etc.

In the [Cloud Run console](https://console.cloud.google.com/run), we can map our service to a custom domain, increase service memory allocation, view logs and usage stats, etc. Cloud Run also offers a generous [Free Tier](https://cloud.google.com/run/pricing) for each month.

Thanks for reading! I hope I've helped to show you how to get started running serverless R in Cloud Run. Let me know if you found this post useful or have any questions, and feel free to share it!

## More info:

- [Cloud Run with R – Hello World (GitHub)](https://github.com/Jinksi/cloudrun-helloworld-r)
- [Cloud Run docs](https://cloud.google.com/run/docs/)
- [plumber](https://www.rplumber.io/)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='PostFooter__Icon-sc-8qtojk-0-Twitter hjyQi js-evernote-checked' data-evernote-id='370'%3e%3cpath d='M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z' data-evernote-id='371' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Discuss on Twitter](https://mobile.twitter.com/search?q=https%3A%2F%2Fericjinks.com%2Fblog%2F2019%2Fserverless-R-cloud-run%2F) • [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='PostFooter__Icon-sc-8qtojk-0-GitHub ckUIhe js-evernote-checked' data-evernote-id='374'%3e%3cpath d='M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22' data-evernote-id='375' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Edit post on GitHub](https://github.com/Jinksi/ericjinks.com/edit/master/src/pages/blog/2019/serverless-R-cloud-run.md)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='Share--Icon Share__Icon-o8ccjj-1-Twitter dLJGLb js-evernote-checked' data-evernote-id='378'%3e%3cpath d='M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z' data-evernote-id='379' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

> If you liked this article and think others should read it, please
> share it on Twitter.