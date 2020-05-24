Knative + Buildpacks: Source code to container image without Dockerfile

# Knative + Buildpacks: Source code to container image without Dockerfile

[![1*0yYQX1dZSfPDCm_RWEsdoA.jpeg](../_resources/5e8122abd6b899100e5cd405590f68b1.jpg)](https://medium.com/@meteatamel?source=post_header_lockup)

[Mete Atamel](https://medium.com/@meteatamel)
May 16·3 min read

![](../_resources/077152f6dc44a6951387c0e356b2ab32.png)![1*Sj53JniX4gStXhMQ5MkEcQ.png](../_resources/bb54af67f793b5efaf77bdd038733b20.png)

![](../_resources/d806e663e1d842da554f1f26fcf25516.png)![1*hUr6dlRbTCHwoGbVZg3Ivg.png](../_resources/e721808fe9ff5c6b4e054757df007f82.png)

I previously [talked about](https://medium.com/google-cloud/hands-on-knative-part-3-d8731ad2f23d)  [Knative Build](https://github.com/knative/build) and how it enables you to go from source code to a container image in a repository. You can write your Build from scratch or you can rely on many of the [BuildTemplates](https://github.com/knative/build-templates) Knative already provides. For example, in my [Knative Tutorial](https://github.com/meteatamel/knative-tutorial), I [show](https://github.com/meteatamel/knative-tutorial/blob/master/docs/10.5-kanikobuildtemplate.md) how to install [Kaniko BuildTemplate](https://github.com/knative/build-templates/tree/master/kaniko) and use Kaniko to build container images.

You normally need to write a `Dockerfile`, so Knative Build (or Kaniko to be more precise) knows how to build the container image. Wouldn’t it be great if there was a an automatic way to build your app without having to define a `Dockerfile` ? Well, there is!

* * *

*...*

[Cloud Native Buildpacks](https://buildpacks.io/) is a project that provides a higher-level abstraction for building apps compared to Dockerfiles. [Cloud Native Buildpacks](https://buildpacks.io/) allow you to go from source code to a container image without having to define a `Dockerfile`. It does this with some auto-detection magic to figure out what language your code is written in and what kind of dependencies it has. In the end, you end up with a runnable app image without having to worry about the details of authoring and optimizing a `Dockerfile`.

The good news is that Knative has a [Buildpacks template](https://github.com/knative/build-templates/tree/master/buildpacks) that makes it really easy to use Buildpacks in your Knative Build. I show how to do this in my Knative Buildpacks Build Template [tutorial](https://github.com/meteatamel/knative-tutorial/blob/master/docs/10.7-buildpacksbuildtemplate.md) in detail but let’s recap here.

### Install the Buildpacks template

First, you need to install the Buildpacks template:

kubectl apply -f https://raw.githubusercontent.com/knative/build-templates/master/buildpacks/cnb.yaml

And check that the template is installed:
kubectl get buildtemplate

NAME AGE
buildpacks-cnb 1m

### Design the build

Next, let’s create a Build to build a sample Java app on GitHub ([sample-java-app](https://github.com/buildpack/sample-java-app.git)) using the build template. Create `build.yaml` file:

apiVersion: build.knative.dev/v1alpha1
kind: Build
metadata:
name: buildtemplate-buildpack-sample-java-app-gcr
spec:
source:
git:
url: https://github.com/buildpack/sample-java-app.git
revision: master
template:
name: buildpacks-cnb
arguments:

- name: IMAGE

value: gcr.io/knative-atamel/sample-java-app:buildpack

One thing you’ll notice is that the `sample-java-app` does not define a `Dockerfile`. Buildpacks will use its auto-detection to build the image and Knative will push it to the location specified in `IMAGE` argument (which is Google Container Registry in this case).

### Run the build

We can finally run the build:
kubectl apply -f build.yaml
After a few minutes, check that the build is succeeded:
kubectl get build
NAME SUCCEEDED
buildtemplate-buildpack-sample-java-app-gcr True
At this point, you should see the image pushed to Google Container Registry:

![](../_resources/deb0e8b667cb5a044d0a958a12b05a7c.png)![1*xGUemtlwcFlXCgvneo3OOg.png](../_resources/ff89e1a8a8959972ab98cbb85232c5a0.png)

* * *

*...*

Knative Build with Buildpacks is a great combination for building apps at a higher abstraction level compared to Dockerfiles!