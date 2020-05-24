Improving your data science workflow with Docker

# Introduction

## What is containerization?

Containerization is OS-level virtualization which does not require a full virtual machine (VM). This is not a new idea but it has recently gained widespread acceptance as tools mature and the barriers of entry into containerizing applications has been reduced.

### Ok, so why is that a big deal?

Well if you hang out with engineers you probably hear a lot of talk about containerization, Docker and microservices. The reason is that they address a lot of challenges simultaneously. For our purposes the biggest advantages of containerization are portability, lightweight and self-contained environments, and simplified versioning and dependency management.

## Getting started with Docker

Docker is the most popular containerization platform and it’s very simple to get started. It’s important to have a very basic understanding of how containerization works to avoid common mistakes, such as writing log files to your container layer. I’ll mention repeatedly concerns of image size, this is something that is always good to keep in mind since Docker is great for deploying applications but it is not always applicable as we’ll see in the examples.

### Terminology

First, let’s make sure we’re on the same page with a few terms. When discussing Docker we’ll usually talk about containers. A container is an instance of an image. A Dockerfile defines a set of instructions to build an image (`docker build`). The image can then be deployed or transported to any platform since it is self-contained (see above) and run as a container (`docker run`). I highly recommend you read [more about images and containers to understand how containers are represented](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/).

### Base Images

The first element you’ll encounter in any Dockerfile is a `FROM image:version` directive defining a base image to start your build with. The simplest of which would be `FROM scratch` which is a built in Docker image defining [an empty image](https://hub.docker.com/_/scratch/). Note that previous link is to [hub.docker.com](http://hub.docker.com/), this is a repository where users can publish base images which can then be pulled down, think of PyPI, with a `FROM` directive. For example, I can see there is [an ubuntu base image](https://hub.docker.com/_/ubuntu/) which I could start with by using `FROM ubuntu:17.10`. I will however advise you NOT to use ubuntu even if you are familiar with it. It is quite bloated for the purposes of running a container and most of the included features will not be used. For something similar to Ubuntu you can look at the [debian](https://hub.docker.com/r/library/debian/) base images which are only slightly smaller. A popular choice is [Alpine linux](https://hub.docker.com/_/alpine/) for it’s [small size](https://www.brianchristner.io/docker-image-base-os-size-comparison/). Alpine is 5MB compared to Ubuntu’s 188MB and Debian’s 125MB.

Also of interest is the prebuilt [python images](https://hub.docker.com/_/python/) but take note of the size of the version you’re using [here](https://hub.docker.com/_/python/tags/). The default versions are currently built on Debian Jessie and are therefore relatively large, `python:3` is 275MB, `python:3-slim` is 55MB and `python:3-alpine` is 31MB. Again as we talk about size you might think that 275MB is not very large but this is just a base image, any requirements your application has will be added on top of that and a lot of data science libraries are very bloated. Data science Docker images can quickly climb into the GB which will quickly diminish your deploy times. Of course this needs to be weighed against your runtime, taking an extra 30 seconds to copy a 1GB image may not matter if your algorithm takes hours to run.

### Running Commands

The next directive we’ll look at is the `RUN` command which allows us to run commands in our container at build time to get things setup the way we’d like. The one point I like to reinforce here is when defining `RUN` commands remember how images are defined as layers and that each `RUN` command will be a layer. This leads us to designing our `RUN` commands to do everything in a single `RUN` (layer) to [reduce the number of layers as is recommended to keep size down](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#minimize-the-number-of-layers).

### Volumes

Since Docker containers are made up of layers any data written to disk within a container will be written to the runtime layer. I’ll just go ahead and tell you that this runtime layer should be small for optimal performance ([more here](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/#copying-makes-containers-efficient)). The advice on that page is as follows

>

> for write-heavy applications, you should not store the data in the container. Instead, use Docker volumes, which are independent of the running container and are designed to be efficient for I/O. In addition, volumes can be shared among containers and do not increase the size of your container’s writable layer.

Now in data science we deal with, well, data and so most applications are what would be considered write heavy. Even verbose logging could be considered write-heavy as we’re talking on the order of MB here. This is where I advise you to always write two things to Docker volumes, results (intermediate and final) and logs. Not only for efficiency but also for sharing across containers. Data stored on Docker volumes will be accessible from any containers running on that host which greatly increases your options when designing parallelization strategies.

Defining Docker volumes is very simple, in your Dockerfile you can define a volume as `VOLUME /data`. Anything written to `/data` will now be persisted to disk. At runtime you can then also map this location to a specific location on the host (the default, on linux, is `/var/lib/docker`).

### Ports

In the case in which you need a port on the container accessible on the host you can expose a port using Docker’s `EXPOSE` command. You’ll see this in action in example 1 below.

### Container Orchestration and Beyond

Now once we have some images built there are tools which exist for organizing and running these containers across multiple machines. I won’t go into details here and there are lots of tools for container orchestration tools and they are rapidly evolving and you can check some of them out [here](https://github.com/GuillaumeRochat/container-orchestration-comparison).

# Use Cases

Congratulations, you’ve made it all the way to the fun part! Let’s get some containers running. If you haven’t already go ahead and [install Docker](https://docs.docker.com/engine/installation/) if you want to follow along. First, I’ll present Docker as a tool for improving our deployment of a predictive machine learning API to be more portable. Second, I’ll cover how you could create a Dockerized development environment to reduce repetitive machine setup time, as well as the drawbacks of this. Lastly, I’ll briefly introduce a concept of how Docker could be used to parallelize large data processing workloads to highlight to power of the tools we’ve learned about.

## #1: Deploying a machine learning api

Let’s build off a previous post (/python/deploying-machine-learning-models/) by Dockerizing a scikit-learn machine learning API so it can be more easily deployed.

	FROM python:2-slim
	# Copy in files
	WORKDIR /usr/src/app
	COPY requirements.txt ./
	COPY api.py ./
	COPY pipeline.pkl ./
	# Install deps
	RUN pip install --no-cache-dir -r requirements.txt
	# Expose our port to the world
	EXPOSE 5000
	# Run at container start
	CMD [ "python", "./api.py" ]

Let’s go through this to make sure we understand what each line does. First I’m starting with a `FROM` python version `2-slim`. I have chosen not to use the Alpine version because although it is smaller it does not handle any libraries with `libc` dependencies very well and we need numpy, it’s not impossible but let’s keep it simple to start. Next we’ll set our working directory, basically Docker’s version of `cd`. The python images all use `/usr/src/app`. We then copy the files we need into that directory and install our dependencies. Finally we expose our port so that at runtime it can be accessed. Finally there is a new directive, `CMD` which defines the command to run at container runtime. There are actually two ways to set container runtime behavior, `ENTRYPOINT` and `CMD`, they can be used together or separate. [Here](https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/) is a great explainer on the differences and how to choose a strategy based on your needs.

All of the code has been updated in the original directory with the api code [here](https://github.com/Raab70/Raab70.github.io/tree/master/_posts/code/2017-10-17-deploying-machine-learning-models) to also include a Dockerfile. So to follow along you’ll need to run `python create_model.py` to create the pipeline pickle to be loaded by the api. Then you can build the docker image with `docker build -t api .`, This will build an image from the Dockerfile in the current directory (What the `.` is for) and tag it with the name `api`. Once that finishes we’re ready to run our container with `docker run -p 15000:5000 api`. You should see the output of the api starting. Note that the `-p 15000:5000` just tells Docker to map the exposed port 5000 on the container to our local machine’s port 15000. Now we can hit our api just as we did before.

	$ curl -H 'Content-Type:application/json' -d '{"data": "Ferrari is the best sports car"}' localhost:15000
	{
	  "result": "rec.autos"
	}

The difference being now this image can be moved around to any other platform and contains everything we need to deploy our API. When we want to update it with a new version we can replace our running containers with a new version of the image that we’ve built and be sure that all files and dependencies are handled properly.

## #2: Containerized development

Next let’s look at another example, let’s say you want a container which can be used for development. There is an argument to be made in pre-building a container with everything needed for development to simplify getting started on a new machine. Doing so in a container allows for even greater portability than scripting which could run into issues say with different commands on OSX vs linux flavors so let’s give it a try. Let’s start by trying to define what we need for a development environment, I would argue that a decent environment would include the following:

- pandas

- scipy

- numpy

- scikit-learn

- matplotlib

- seaborn

- jupyter notebook

That sure does seem like a lot to get setup right? But wait, there is a great community around docker, what if we searched on docker hub for jupyter notebook? You would quickly find [this](https://hub.docker.com/r/jupyter/datascience-notebook/). The first section at the top says it gives you, `jupyter notebook, conda python 3, pandas, matplotlib, scipy, seaborn, scikit-learn, scikit-image, sympy, cython, patsy, statsmodel, cloudpickle, dill, numba, bokeh pre-installed`. Sounds like it’ll work for us. So how can we use this? Do we need to create a Dockerfile that just has `FROM jupyter/datascience-notebook`. Nope, Docker is smart enough that if we ask it to run an image which we don’t have, it’ll check and see if it’s in Docker hub. If it is, it’ll run it. Try running `docker run hello-world`. You’ll see that it actually pulls down an [official Docker hello-world image](https://hub.docker.com/_/hello-world/). So all we need to do is run `docker run jupyter/datascience-notebook` and boom. If you take a look you would [see that jupyter actually has a number of images](https://hub.docker.com/r/jupyter/), they even have a [tensorflow notebook](https://hub.docker.com/r/jupyter/tensorflow-notebook/). I’m actually a fan of the `jupyter/scipy-notebook` image as it doesn’t have any R packages which I won’t use installed. It doesn’t save much space though, both images come in at 2GB compressed. Even the `jupyter/minimal-notebook` which has no scientific packages installed is just a hair under 1GB at the time of writing. One thing to note is that these images use Ubuntu as their base image because the images are going to be big anyways, why not use the platform most people are familiar with. There’s no reason to cut corners with Alpine to save 100MB when you’re going to install 1.8GB of packages on top of it.

## #3: Distributed development

This one is a bit of a tease if you clicked down from the table of contents, I just want to whet your appetite here of the possibilities with the foundation that we’ve built. Going through a full example of this would probably be it’s own post but let’s take a second to look back on what we’ve learned. Imagine now that you’re training a model, any model, this model more than likely has hyperparameters which you want to optimize over. Maybe you’ve used `sklearn.model_selection.GridSearchCV`, it’s a great tool! But what if your model takes a few hours to train and you have hundreds or thousands of possible hyperparameter combinations. You can go to your boss and say you need one `c5.18xlarge` (72 cores/144GB RAM) and you can do it in a day for $72/day, or you could dockerize your training to read data in from S3 (or save throughput with shared disk storage) and read the parameters from an environment variable. Now you might think that this is a waste of time to get the 18 `c5.xlarge` you would need for your 72 cores it would still cost $72/day. However, now you can take advantage of your distributed environment and buy only a single node at on-demand pricing and use spot pricing for the rest of your fleet. Make sure your master runs on the on-demand node and it will only slow you down a small amount if your slave instances get terminated. `c5.xlarge` go for about to 6¢/hr on the spot market ($1.44/day) so you could fill out your fleet for $28.56 ([0.17 + 17*0.06]*24)

# Conclusion

There is a lot to be learned with Docker and most of it is not necessary for a data scientist to understand. A basic understanding of what Docker is and how containerization works can allow you to improve your workflow by leveraging these modern technologies. If yesterday I asked you to spin up a full fledged jupyter notebook environment with all the basic scientific python packages in a single command you would need some time. Now what if I said that it also had to work on every platform? You might even say it’s not possible. Here we’ve looked at just a couple of ways containers can make your life as a data scientist just a little bit easier and let you focus on getting the right model.