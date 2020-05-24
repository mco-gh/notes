15 Docker Commands You Should Know – Towards Data Science

# 15 Docker Commands You Should Know

## Part 5 of *Learn Enough Docker to be Useful*

[![1*FjId1jWOkaOu1lrpZOyI8A.jpeg](../_resources/079d6da263a06b3683b8825f7468eead.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='174' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://towardsdatascience.com/@jeffhale?source=post_header_lockup)

[Jeff Hale](https://towardsdatascience.com/@jeffhale)
Feb 5·9 min read

In this article we’ll look at 15 Docker CLI commands you should know. If you haven’t yet, check out the rest of this series on [Docker concepts](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b), [the ecosystem](https://towardsdatascience.com/learn-enough-docker-to-be-useful-1c40ea269fa8), [Dockerfiles](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5), and [keeping your images slim](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e). In Part 6 we’ll explore data with Docker. I’ve got a series on Kubernetes in the works too, so follow me to make sure you don’t miss the fun!

There are about a billion Docker commands (give or take a billion). The [Docker docs](https://docs.docker.com/engine/reference/commandline/cli/) are extensive, but overwhelming when you’re just getting started. In this article I’ll highlight the key commands for running vanilla Docker.

![](../_resources/03c151b9333c131f736a93bc37bf1690.png)![1*e91PqDA0DJI9kgwaXfxngg.jpeg](../_resources/030ad3898fa650dababf8540ecf69685.jpg)

Fruit theme

At risk of taking the food metaphor thread running through these articles too far, let’s use a fruit theme. Veggies provided sustenance in the [article on slimming down our images](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e). Now tasty fruits will give us nutrients as we learn our key Docker commands.

### Overview

Recall that a Docker image is made of a Dockerfile + any necessary dependencies. Also recall that a Docker container is a Docker image brought to life. To work with Docker commands, you first need to know whether you’re dealing with an image or a container.

- •**A Docker image either exists or it doesn’t.**
- •**A Docker container either exists or it doesn’t.**
- •**A Docker container that exists is either running or it isn’t.**

Once you know what you’re working with you can find the right command for the job.

#### Commmand Commonalities

Here are a few things to know about Docker commands:

- •All Docker CLI commands start with `docker` then a space and then the command. For example, `docker version` will give you the specifics of the Docker version you’re running.
- •A command referring to a specific container or image requires the name or id of that container or image.

For example, `docker run my_app` is the command to build and run the container named *my_app*. I’ll use the name `my_container` to refer to a generic container throughout the examples. Same goes for `my_image`, `my_tag`, etc.

I’ll provide the command alone and then with common flags, if applicable. A flag with two dashes in front is the full name of the flag. A flag with one dash is a shortcut for the full flag name. For example, `-p` is short for the `--port` flag.

![](../_resources/1254fed13d5d3470a0baadb6904b6259.png)![1*GXCbJUG6G2EgcUAA4oxX2Q.png](../_resources/6fc33dbb4419974bbbf47cd64565e7e6.png)

Flags provide options to commands

The goal is to help these commands and flags stick in your memory and for this guide to serve as a reference. This guide is current for Linux and Docker Engine Version 18.09.1 and API [version 1.39](https://docs.docker.com/engine/api/version-history/).

First, we’ll look at commands for containers and then we’ll look at commands for images. Volumes will be covered in the next article. Here’s the list of 15 commands to know.

#### Containers

`create` — Create a container from an image.
`start `— Start an existing container.
`run` — Create a new container and start it.
`ps` — List running*  *containers.
`logs` — Print logs.
`stop` — Gracefully stop running container.
`kill` —Stop main process in container abruptly.
`rm`— Delete stopped container.

#### Images

`build `— Build an image.
`login` — Log in to a remote registry.
`push` — Push an image to a remote registry.
`image(s)` — List images.
`history` — See intermediate image info.
`inspect` — See lots of info about the image, including the layers.
`rmi` — Delete an image.

### Containers

#### Container Beginnings

The terms create, start, and run all have similar semantics in everyday life. But each is a separate Docker command that creates and/or starts a container. Let’s look at creating a container first.

`**docker create my_repo/my_image:my_tag**` — Create a container from an image.

I’ll shorten `my_repo/my_image:my_tag`**  **to `my_image` for the rest of the article.

There are [a lot of possible flags](https://docs.docker.com/engine/reference/commandline/create/#parent-command) you could pass to `create`.

`**docker create -a STDIN my_image**`
`-a` is short for `--attach`. Attach the container to STDIN, STDOUT or STDERR.
Now that we’ve created a container let’s start it.
`**docker start my_container**` — Start an existing container.

Note that the container can be referred to by either the container’s ID or the container’s name.

`**docker start my_container**`

![](../_resources/0930d994314c04bee7a4c90326accc14.png)![1*hdLjLfbTWcXQIjgy2D2t0A.jpeg](../_resources/f311caefd066c716d8a63091db456d6e.jpg)

Start

Now that you know how to create and start a container, let’s turn to what’s probably the most common Docker command. It combines both `create` and `start` into one command: `run`.

`**docker run my_image**`** **—** **Create a new container and start it. It also has [a lot of options](https://docs.docker.com/engine/reference/commandline/run/#parent-command). Let’s look at a few.

`**docker run -i -t -p 1000:8000 --rm my_image**`
`-i` is short for `--interactive`. Keep STDIN open even if unattached.

`-t`is short for`--tty`. Allocates a pseudo [terminal](http://en.wikipedia.org/wiki/Pseudo_terminal) that connects your terminal with the container’s STDIN and STDOUT.

You need to specify both `-i` and `-t` to then interact with the container through your terminal shell.

`-p` is short for `--port`. The port is the interface with the outside world.`1000:8000` maps the Docker port 8000 to port 1000 on your machine. If you had an app that output something to the browser you could then navigate your browser to `localhost:1000` and see it.

`--rm` Automatically delete the container when it stops running.
Let’s look at some more examples of `run`.
`**docker run -it my_image my_command**`

`sh` is a command you could specify at run time.`sh` will start a shell session inside your container that you can interact with through your terminal. `sh` is preferable to `bash` for Alpine images because Alpine images don’t come with `bash` installed. Type `exit` to end the interactive shell session.

Notice that we combined `-i` and `-t` into `-it`.
`**docker run -d my_image**`

`-d` is short for `--detach`. Run the container in the background. Allows you to use the terminal for other commands while your container runs.

#### Checking Container Status

If you have running Docker containers and want to find out which one to interact with, then you need to list them.

`**docker ps**` — List running*  *containers. Also provides useful information about the containers.

`**docker ps -a -s**`
`-a` is short for `-all`. List all containers (not just running ones).
`-s` is short for `--size`. List the size for each container.
`**docker logs my_container**` — Print a container’s logs.

![](../_resources/b3961bef641cab60254227d6c72bc57a.png)![1*icdqfkCNhA8mhJ82ctt54Q.jpeg](../_resources/caa7f1f526f0e2fa030afe90da72b94f.jpg)

Logs. Not sure how virtual logs are related. Maybe via reams of paper?

#### Container Endings

Sometimes you need to stop a running container.

`**docker stop my_container**` — Stop one or more running containers gracefully. Gives a default of 10 seconds before container shutdown to finish any processes.

Or if you are impatient:

`**docker kill my_container**` — Stop one or more running containers abruptly. It’s like pulling the plug on the TV. Prefer `stop` in most situations.

`d**ocker kill $(docker ps -q)**` — Kill all running containers.

![](../_resources/423dffe66d0fe18cd24d3d8bf6cda5ce.png)![1*z04O3uNyI_so53j0hqIjhg.jpeg](../_resources/c7f700a549306334ebad18ef77b30e7a.jpg)

docker kill cockroach
Then you delete the container with:
`**docker rm my_container**` — Delete one or more containers.

`**docker rm $(docker ps -a -q)**` — Delete all containers that are not running.

Those are the eight essential commands for Docker containers.

To recap, you first create a container. Then, you start the container. Or combine those steps with `docker run my_container`. Then, your app runs. Yippee!

Then, you stop a container with `docker stop my_container`. Eventually you delete the container with `docker rm my_container`.

Now, let’s turn to the magical container-producing molds called images.

### Images

Here are seven commands for working with Docker images.

#### Developing Images

`**docker build -t my_repo/my_image:my_tag .**` — Build a Docker image named *my_image* from a Dockerfile and the files located at the specified path or URL.

`-t` is short for tag. Tells docker to tag the image with the provided tag. In this case *my_tag .*

The `.` (period) at the end of the command tells Docker to build the image with the files in the current working directory.

![](../_resources/40ccffbb8a4ba5e159eb68468991315e.png)![1*pzypY32qru9mOB-qOb4Evw.jpeg](../_resources/bdb6372fe256b3c5640061dfa1dff5f7.jpg)

Build it

Once you have an image built you want to `push` it to a remote registry so it can be shared and pulled down as needed. Assuming you want to use [Docker Hub](https://hub.docker.com/), go there in your browser and create an account. It’s free.

`**docker login**` — Log in to a Docker registry. Enter your username and password when prompted.

![](../_resources/c8d2cf9bbaa9eb500293899f1ac18ad2.png)![1*ZgMR-_PYuu3ghNyPzLHrGA.jpeg](../_resources/d4084f3163611f4c295b5b5a4e3087e0.jpg)

Push
`**docker push my_repo/my_image:my_tag**` — Push an image to a registry.
Once you have some images you might want to inspect them.

#### Inspecting Images

![](../_resources/5a48e083e4ad729be14fb10822735b31.png)![1*bldenADzHHFGZa8e3XVXUA.png](../_resources/630b315aa2b921eaec0cb130ae7776d1.png)

Inspection time

`**docker image ls**` — List all your images. Shows you the size of each image, too.

`**docker images**` — List all *local *images.

`**docker history my_image**` — Display an image’s intermediate images with sizes and how they were created.

`**docker inspect my_image**` — Show lots of details about your image, including the layers that make up the image.

Sometimes you’ll need to clean up your images.

#### Removing Images

`**docker rmi my_image**` — Delete the specified image. If the image is stored in a remote repository, the image will still be available there.

`**docker rmi $(docker images -a -q)**` — Delete all images. Careful with this one! Note that images that have been pushed to a remote registry will be preserved — that’s one of the benefits of registries.

Now you know most essential Docker image-related commands. We’ll cover data-related commands in the next article.

![](../_resources/56f1deba3f8f59969b0ad6f0d81880ac.png)![1*oWepBSWQY6jQ4AndB5F5CA.jpeg](../_resources/dc0ad5ffae5c8a09b8f10f212b866401.jpg)

Commands are like fruit — nutritious and delicious. Err. Yeah.

### Wrap

If you are just getting started with Docker, these are the three most important commands:

`**docker run my_image**` — Create a new container and start it. You’ll probably want some flags here.

`**docker build -t my_repo/my_image:my_tag .**` — Build an image.
`**docker push my_repo/my_image:my_tag**` — Push an image to a remote registry.
Here’s the larger list of 15 essential Docker commands:

#### Containers

`create` — Create a container from an image.
`start`— Start an existing container.
`run` — Create a new container and start it.
`ps` — List running*  *containers.
`logs` — Print logs.
`stop` — Gracefully stop a running container.
`kill` —Stop main process in container abruptly.
`rm`— Delete stopped container.

#### Images

`build `— Build an image.
`login` — Log in to a remote registry.
`push` — Push an image to a remote registry.
`image(s)` — List images.
`history` — See intermediate image info.
`inspect` — See lots of info about the image, including the layers.
`rmi` — Delete an image.

To view the CLI reference when using Docker just enter the command `docker` in the command line. You can also see the reference [here](https://docs.docker.com/engine/reference/commandline/cli/). Additionally, [this GitHub repo](https://github.com/wsargent/docker-cheat-sheet) has a nice cheat sheet for Docker commands.

Now you can really build things with Docker! As my daughter might say in emoji: . Which I think translates to “Cool!” So go forth and play with Docker!

If you missed the earlier articles in this series, check them out. Here’s the first one:

[**Learn Enough Docker to be Useful** *Part 1: The Conceptual Landscape*towardsdatascience.com](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)[(L)](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)

In the final article in this series we’ll spice things up with a discussion of data in Docker. Follow me to make sure you don’t miss it!

I hope you found this article helpful. If you did, please give it some love on your favorite social media channels. Docker on!