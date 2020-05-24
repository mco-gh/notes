Deploy your side-projects at scale for basically nothing - Google Cloud Run - Alex Olivier | cloud native product manager in london

# Deploy your side-projects at scale for basically nothing - Google Cloud Run

I have built hundreds of side projects over the years and finding a place to manage and deploy them all has always been tricky. From the early days of a GoDaddy hosting package with random PHP files in folders, through having a persistent [DigitalOcean](https://m.do.co/c/d4ea2452cd3c) droplet running, and event running a bare minimum [Kubernetes](https://kubernetes.io/) cluster on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/) - I’ve never been satisfied with the outcome.

I have a few requirements when it comes to down deploying random side projects:

1. Fully-managed - I don’t want to have to worry about servers anymore - it’s 2020 after all - and I want serverless all the things

2. Cheap - These projects aren’t making me money so need to keep costs down

3. Language agnostic - One day I maybe playing with something in Node, then next Python, the next Go.

4. Scalable - in the unlikely something does takeoff, I don’t want to have to worry about it falling over

Thankfully, I’ve found a solution that I am happy with - [Google Cloud Run](https://cloud.google.com/run/).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='280' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='281' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#what-is-google-cloud-run)What is Google Cloud Run?

Google is terrible at marketing…

> Cloud Run is a fully managed compute platform that automatically scales your stateless containers. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most—building great applications.

What is means is you can give it a docker container (technically any OCI compatible container) and it will deploy, run and scale it.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='282' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='283' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#why-is-it-good)Why is it good?

If we evaluate this by my requirements:

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='284' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='285' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#fully-managed)Fully Managed

After using [Cloud Run](https://cloud.google.com/run/) for over a year now I have never had to touch a server, VM, cluster or anything else. This is truly a deploy and forget service.

Due to it being fully managed there are a few requirements to make your application compatible. The only real one you have to worry about it to ensure your application runs an HTTP server and listens on the port set in the `PORT` environment variable that is present at runtime of your container.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='286' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='287' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#cheap)Cheap

The beauty of [Cloud Run](https://cloud.google.com/run/) is that it is only ‘running’ your container when it gets traffic. The pricing model is setup that you only pay for the CPU/memory/network bandwidth used when your app is getting requests.

It achieves this by deploying your app on demand when traffic hits the domain name they give you, it hangs around for a bit (undetermined) until after traffic stops, and the the app is torn down. The other way to look at this is autoscaling - when there is no traffic, it scales to 0.

There is a cost in the form of time - if you app takes time to ‘setup’ when it starts up, you will be making your users wait as [Cloud Run](https://cloud.google.com/run/) scales up your application from 0 to 1+ instances. From my own use I’ve found this to be negligible though.

Due to this pricing model I’ve never paid for than a few cents - yes CENTS - a month for all my side projects (10+ deployed currently). This is a factor of the little traffic I get to them so you may need to do the maths for yours - the [pricing page is here](https://cloud.google.com/run/#pricing).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='288' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='289' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#language-agnostic)Language Agnostic

As [Cloud Run](https://cloud.google.com/run/) takes any container image and deploys it, you can use any language you want. Be it Node, Go, Java, PHP or something entirely obscure, as long as it speaks HTTP and listens on the port defined in the `PORT` environment variable, [Cloud Run](https://cloud.google.com/run/) doesn’t care what you do inside the container.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='290' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='291' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#scalable)Scalable

I am yet to have a side project go ‘viral’ but I am confident that should such event occur, [Cloud Run](https://cloud.google.com/run/) will handle it. The service will create more and more instances of your application up to the limit you defined (currently the cap is 1000 instances).

As long as you have architected your application to be stateless - storing data in something like a database (eg [CloudSQL](https://cloud.google.com/sql/)) or object storage (eg [Cloud Storage](https://cloud.google.com/storage/)) - then you are good to go. Do consider if any services you depend on can handle the traffic should this scenario occur though.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='292' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='293' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#simple-nodejs-example)Simple Node.js Example

Enough chat, let’s write some code.

If we take the most basic example of a Node.js Express app serving some JSON - this could be an API server for your statically deployed React frontend example.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='294' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='295' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#the-application)The Application

You have your usual Node application code - something like:

	const express = require('express')
	const app = express()
	const port = process.env.PORT || 3000

	app.get('/', (req, res) => {
	  res.json({
	    message: 'Hello World'
	  })
	})

	app.listen(port, () => console.log(`Example app listening on port ${port}!`))1234567891011

This is the bare-minimum to run an HTTP server in Node - in this case when you hit the root path, it returns a JSON with a “Hello World” message. The only ‘special’ bit in this is line 3 where we grab the port number we tell express to listen to from the environment variable if it exists - this will be provided by the Cloud Run service at execution time.

Next we need a `Dockerfile` to create our docker image from:

	FROM node:10

	# Create app directory
	WORKDIR /usr/src/app

	# Install app dependencies
	COPY package*.json ./
	RUN npm install

	COPY . .
	CMD ["node", "server.js"]1234567891011

This is a barebones `Dockerfile` which uses the `node:10` base image, copies our `package.json` file in, installs our dependencies and then will run our `server.js` file upon running the container.

With that set now it is time to build & deploy.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='299' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='300' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#building--pushing-our-image)Building & Pushing our Image

[Google Cloud Run](https://cloud.google.com/run/) requires our images to be in the [Google Container Registry](https://cloud.google.com/container-registry/) of our project for easiest access. As such, you will need to have this enabled on your Google Cloud Project - you can find out how to do this here. You will also need the [`gcloud` CLI](https://cloud.google.com/sdk/gcloud/) installed on your machine and logged into your account - then run `gcloud auth configure-docker` to setup `gcloud` to work with docker.

Now to build, tag and push our image to the repository. Your container tag will need to be in the following format:

`gcr.io/[gcp-project]/[app-name]:latest`

Where `[gcp-project]` is your Google Cloud Project name eg `my-project` and `[app-name]` is the name of your container eg `cloud-run-demo`

You then build:
`docker build -t gcr.io/[gcp-project]/[app-name]:latest .`
and then push:
`docker push gcr.io/[gcp-project]/[app-name]:latest`

If everything worked without errors, you can now move onto deploying via Cloud Run.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='301' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='302' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#deploying-on-cloud-run)Deploying on Cloud Run

You can do this via the `gcloud` CLI (using `gcloud beta run ...` commands or my preferred way, the Google Cloud Console.

Start by going to the Cloud Run section of your Google Cloud Console:

     [cloud-run-url.webp](../_resources/008024e33df71d44ba4d68597908bb83.webp)

Next press the `Create Service` button at the top:

     [cloud-run-new-service.webp](../_resources/47f8f522c2ea35b939d53c6ba5d82532.webp)

Here you need to select the container image that you just pushed - pressing the `Select` link in the box will open the picker which will show all the images in your Google Container Registry instance:

     [cloud-run-dashboard.webp](../_resources/e0dc095ff2f27fd45f74ce1e2f8519f9.webp)

Once your image is selected a few other options to populate:

- Deployment Platform - for this example we want a fully managed offering so select `Cloud Run` and your desired region. Go for the region closest to where your users will be.
- Service Name - Give your service a name so you can look it up later
- Authentication - Decide if you want your service to be authentication via Cloud IAM or not. For all my projects, I want people to access them so check `Allow Unauthenticated Invocations`

There are some more advanced options to set things like custom environment variables, scaling limits and memory caps, but the default is fine for most thing.

Hit `Create` and your service will be deployed. If you get any errors at this point it usually means your application isn’t listening on the `PORT` environment variable. Double check this by running the container image locally and passing in the variable.

Behind the scenes [Cloud Run](https://cloud.google.com/run/) is deploying your image and will given you an HTTP endpoint listed in the top of the page:

     [cloud-run-select-image.webp](../_resources/908a3b08e0268be5bec2a3e2d9960a25.webp)

All the [Cloud Run](https://cloud.google.com/run/) URLs end in `run.app`. Hitting this endpoint in your browser should return you the response from your server running in the container.

Your app is now fully deployed in a managed service. You can start throwing as much traffic at is as you wish, all without worrying about infrastructure, scaling, or maintenance and all for a very very small cost. The dream!

There are a number of advanced areas of Cloud Run which I make use of which maybe topics for future posts:

- Continuous Deployment from [Cloud Build](https://cloud.google.com/cloud-build/)
- [Domain Mapping](https://cloud.google.com/run/docs/mapping-custom-domains) for using my own domain names
- Connecting to [CloudSQL](https://cloud.google.com/sql/) for database storage
- Authentication using [Cloud IAM](https://cloud.google.com/iam/)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='323' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='324' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless#conclusion)Conclusion

Hopefully you’ve got a better idea of what [Cloud Run](https://cloud.google.com/run/) is, why it is so powerful and how it can help you with deploying all sorts of crazy side-projects for very little money and hassle.

Hit me much on Twitter [@alexolivier](https://twitter.com/alexolivier) if you have any questions or want to talk more.