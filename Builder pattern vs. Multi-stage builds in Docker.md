Builder pattern vs. Multi-stage builds in Docker

# Builder pattern vs. Multi-stage builds in Docker

 24 March 2017 on [docker](https://blog.alexellis.io/tag/docker/), [bleeding-edge](https://blog.alexellis.io/tag/bleeding-edge/)

This post looks at two new PRs from the Docker project that vastly improve the developer experience for building small images efficiently.

> These changes are bleeding edge and are not available in a release yet, but I wanted to test them out.

A [Docker PR](https://github.com/docker/docker/pull/31257) has just been merged to enable multi-stage builds and a [second PR opened just after](https://github.com/docker/docker/pull/32063) that to improve the UX even further.

This is the first PR that adds multi-staged builds and has been merged.

This second PR improves the UX but was not yet merged at the time of writing.

### What was the builder pattern?

With a statically compiled language like Golang people tended to derive their Dockerfiles from the Golang "SDK" image, add source, do a build then push it to the Docker Hub. Unfortunately the size of the resulting image was quite large - at least 670mb.

A workaround which is informally called the *builder pattern* involves using two Docker images - one to perform a build and another to ship the results of the first build without the penalty of the build-chain and tooling in the first image.

	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
	golang              1.7.3               ef15416724f6        4 months ago        672MB

Golang isn't the only language that can benefit from using one base image to build assets and a second image to run them. My work with [Windows Containers](http://blog.alexellis.io/tag/windows/) also used this pattern to produce smaller images.

An example of the builder pattern:

1. Derive from a Golang base image with the whole runtime/SDK (Dockerfile.build)

2. Add source code
3. Produce a statically-linked binary

4. Copy the static binary from the image to the host (`docker create`, `docker cp`)

5. Derive from `SCRATCH` or some other light-weight image such as `alpine` (Dockerfile)

6. Add the binary back in
7. Push a tiny image to the Docker Hub

This normally meant having two separate Dockerfiles and a shell script to orchestrate all of the 7 steps above.

#### Example

Here's an example from my [href-counter](https://github.com/alexellis/href-counter) repository which is a Golang application used to count the internal/external anchor tags on a web-page.

I'll provide all the files so you can see how much extra work was needed to get a small Docker image. Underneath I'll show the new format.

*Dockerfile.build*

	FROM golang:1.7.3

	WORKDIR /go/src/github.com/alexellis/href-counter/

	RUN go get -d -v golang.org/x/net/html
	COPY app.go	.

	RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

*Dockerfile*

	FROM alpine:latest
	RUN apk --no-cache add ca-certificates

	WORKDIR /root/

	COPY app    .

	CMD ["./app"]

*build.sh*

	#!/bin/sh
	echo Building alexellis2/href-counter:build

	docker build --build-arg https_proxy=$https_proxy --build-arg http_proxy=$http_proxy \
	    -t alexellis2/href-counter:build . -f Dockerfile.build

	docker create --name extract alexellis2/href-counter:build
	docker cp extract:/go/src/github.com/alexellis/href-counter/app ./app
	docker rm -f extract

	echo Building alexellis2/href-counter:latest

	docker build --no-cache -t alexellis2/href-counter:latest .

### What are multi-stage builds?

Multi-stage builds give the benefits of the builder pattern without the hassle of maintaining three separate files:

	FROM golang:1.7.3

	WORKDIR /go/src/github.com/alexellis/href-counter/

	RUN go get -d -v golang.org/x/net/html
	COPY app.go	.

	RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

	FROM alpine:latest
	RUN apk --no-cache add ca-certificates

	WORKDIR /root/

	COPY --from=0 /go/src/github.com/alexellis/href-counter/app    .

	CMD ["./app"]

This is huge for developers and maintainers, especially when you support multiple Dockerfiles for different architectures such as the [Raspberry Pi](http://blog.alexellis.io/tag/raspberry-pi/).

The general syntax involves adding `FROM` additional times within your Dockerfile - whichever is the last `FROM` statement is the final base image. To copy artifacts and outputs from intermediate images use `COPY --from=<base_image_number>`

The second PR mentioned improves on this syntax and when merged would mean you can do something more like:

	FROM golang:1.7.3 as builder

	WORKDIR /go/src/github.com/alexellis/href-counter/

	RUN go get -d -v golang.org/x/net/html
	COPY app.go	.

	RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

	FROM alpine:latest
	RUN apk --no-cache add ca-certificates

	WORKDIR /root/

	COPY --from=builder /go/src/github.com/alexellis/href-counter/app    .

	CMD ["./app"]

### How can I try it out?

**Build Docker from master**

You can create a development build of Docker at any time by cloning the [docker/docker](https://github.com/docker/docker) repository and typing in `make tgz`. The resulting build will create binaries for you in the `bundles` folder.

Here's the build steps:

	$ git clone https://github.com/docker/docker
	$ cd docker
	$ make tgz

**Let's try the example**
Launch Docker within the container you built above:

- These steps prepare the new Docker version for use:

	$ docker run -v `pwd`/bundles:/go/src/github.com/docker/docker/bundles --privileged -ti docker-dev:master bash

The Docker development build creates an image called `docker-dev`. You can actually run Docker inside this image, which is what we'll do below:

	$ export PATH=$PATH:`pwd`/bundles/latest/dynbinary-daemon:`pwd`/bundles/latest/binary-client/
	$ dockerd &

- Now still within the container, clone my repository and initiate a build using the multi-step Dockefile:

	$ git clone https://github.com/alexellis/href-counter
	$ cd href-counter
	$ docker build -t href-counter . -f Dockerfile.multi

> the `-f`>  flag allows you to specify the name of a different Dockerfile.
Now run the Docker image:

	$ docker run -e url=https://www.alexellis.io/ multi
	{"internal":9,"external":5}

	$ docker run -e url=https://www.docker.com multi
	{"internal":97,"external":38}

Compare the differences in size between the resulting image and what we would have had if we used `FROM golang`:

	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE

	multi               latest              bcbbf69a9b59        6 minutes ago       10.3MB
	golang              1.7.3               ef15416724f6        4 months ago        672MB

**Wrapping up**

The builder pattern was effective as a work-around and would have created a binary of a similar size, but it was hard to maintain and very hard to use with Docker's automated build system.

If you need a small image - you should follow the builder pattern for now using the example above. Once the feature is released through the stable channel and made available for auto-builds on the Hub/Cloud I would switch over.

Follow me on Twitter for more Docker news and tutorials.

### Recent blog posts:

- [FaaS - a portable serverless framework for Docker](http://github.com/alexellis/faas)
- [Tutorial: Monitor your applications with Prometheus](http://blog.alexellis.io/prometheus-monitoring/)
- [Running ad-hoc containers on Docker Swarm](http://blog.alexellis.io/containers-on-swarm/)

*Update:*

> If you'd like to save time building Docker on your own machine, I've submitted a lab to > [> birthday.play-with-docker.com](http://birthday.play-with-docker.com/#intermediate)>  (which runs Docker in a webpage, with the master build) in the Intermediate section:

- [Docker Birthday labs: Intermediate section](http://birthday.play-with-docker.com/#intermediate)

 [(L)](https://blog.alexellis.io/author/alex/)

#### [Alex Ellis](https://blog.alexellis.io/author/alex/)

Read [more posts](https://blog.alexellis.io/author/alex/) by this author.

 https://www.alexellis.io/

#### Share this post

 [](https://twitter.com/intent/tweet?text=Builder%20pattern%20vs.%20Multi-stage%20builds%20in%20Docker&url=https://blog.alexellis.io/mutli-stage-docker-builds/)  [](https://www.facebook.com/sharer/sharer.php?u=https://blog.alexellis.io/mutli-stage-docker-builds/)  [](https://plus.google.com/share?url=https://blog.alexellis.io/mutli-stage-docker-builds/)

### Subscribe to alex ellis' blog

Get the latest posts delivered right to your inbox.

 or subscribe [via RSS](http://cloud.feedly.com/#subscription/feed/https://blog.alexellis.io/rss/) with Feedly!