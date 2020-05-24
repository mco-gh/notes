GoogleCloudPlatform/skaffold

# Skaffold

Skaffold is a command line tool that facilitates continuous development for Kubernetes applications. You can iterate on your application source code locally then deploy to local or remote Kubernetes clusters. Skaffold handles the workflow for building, pushing and deploying your application. It can also be used in an automated context such as a CI/CD pipeline to leverage the same workflow and tooling when moving applications to production.

### Features

- No server-side component. No overhead to your cluster.
- Detect changes in your source code and automatically build/push/deploy.
- Image tag management. Stop worrying about updating the image tags in Kubernetes manifests to push out changes during development.
- Supports existing tooling and workflows. Build and deploy APIs make each implementation composable to support many different workflows.
- Support for multiple application components. Build and deploy only the pieces of your stack that have changed.
- Deploy regularly when saving files or run one off deployments using the same configuration.

### Pluggability

Skaffold has a pluggable architecture that allows you to choose the tools in the developer workflow that work best for you.[(L)](https://github.com/GoogleCloudPlatform/skaffold/blob/master/docs/img/plugability.png)

[![Plugability Diagram](../_resources/7a54703947a8389bc638af49747648ac.png)](https://github.com/GoogleCloudPlatform/skaffold/blob/master/docs/img/plugability.png)

## Operating modes

### skaffold dev

Updates your deployed application continually:

- Watches your source code and the dependencies of your docker images for changes and runs a build and deploy when changes are detected
- Streams logs from deployed containers
- Continuous build-deploy loop, only warn on errors

### skaffold run

Run runs a Skaffold pipeline once, exits on any errors in the pipeline.
Use for:

- Continuous integration or continuous deployment pipelines
- Sanity checking after iterating on your application

## Demo

[(L)](https://github.com/GoogleCloudPlatform/skaffold/blob/master/docs/img/intro.gif)

[![Demo](../_resources/e90038e8f85282620e9a90c7906adecd.gif)](https://github.com/GoogleCloudPlatform/skaffold/blob/master/docs/img/intro.gif)

## Getting Started with Local Tooling

For getting started with Google Kubernetes Engine and Container Builder [go here](https://github.com/GoogleCloudPlatform/skaffold/blob/master/docs/quickstart-gke.md). Otherwise continue below to get started with a local Kubernetes cluster.

### Installation

You will need the following components to get started with Skaffold:
1. skaffold

    - To download the latest Linux build, run:
        - `curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && chmod +x skaffold && sudo mv skaffold /usr/local/bin`
    - To download the latest OSX build, run:
        - `curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-darwin-amd64 && chmod +x skaffold && sudo mv skaffold /usr/local/bin`

2. Kubernetes Cluster
3. [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

    - Configure the current-context with your target cluster for development

4. docker
5. Docker image registry

    - Your docker client should be configured to push to an external docker image repository. If you're using a minikube or Docker for Desktop cluster, you can skip this requirement.
    - If you are using Google Container Registry (GCR), choose one of the following:

        1. Use `gcloud`'s Docker credential helper: Run [`gcloud beta auth configure-docker`](https://cloud.google.com/sdk/gcloud/reference/beta/auth/configure-docker)

        2. Install and configure GCR's standalone cred helper: [`docker-credential-gcr`](https://github.com/GoogleCloudPlatform/docker-credential-gcr#installation-and-usage)

        3. Run `gcloud docker -a` before each development session.

### Iterative Development

1. Clone this repostiory to get access to the examples.
git clone https://github.com/GoogleCloudPlatform/skaffold
1. Change directories to the `getting-started` example.
cd examples/getting-started
1. Run `skaffold dev`.
$ skaffold dev
Starting build...
Found [minikube] context, using local docker daemon.
Sending build context to Docker daemon 6.144kB
Step 1/5 : FROM golang:1.9.4-alpine3.7
---> fb6e10bf973b

Step 2/5 : WORKDIR /go/src/github.com/GoogleCloudPlatform/skaffold/examples/getting-started

---> Using cache
---> e9d19a54595b
Step 3/5 : CMD ./app
---> Using cache
---> 154b6512c4d9
Step 4/5 : COPY main.go .
---> Using cache
---> e097086e73a7
Step 5/5 : RUN go build -o app main.go
---> Using cache
---> 9c4622e8f0e7
Successfully built 9c4622e8f0e7
Successfully tagged 930080f0965230e824a79b9e7eccffbd:latest

Successfully tagged gcr.io/k8s-skaffold/skaffold-example:9c4622e8f0e7b5549a61a503bf73366a9cf7f7512aa8e9d64f3327a3c7fded1b

Build complete in 657.426821ms
Starting deploy...
Deploying k8s-pod.yaml...
Deploy complete in 173.770268ms
[getting-started getting-started] Hello world!
1. Skaffold has done the following for you:

- Build an image from the local source code
- Tag it with its sha256
- Sets that image in the Kubernetes manifests defined in `skaffold.yaml`
- Deploy the Kubernetes manifests using `kubectl apply -f`

1. You will see the output of the pod that was deployed:
[getting-started getting-started] Hello world!
[getting-started getting-started] Hello world!
[getting-started getting-started] Hello world!
Now, update `main.go`

diff --git a/examples/getting-started/main.go b/examples/getting-started/main.go

index 64b7bdfc..f95e053d 100644
--- a/examples/getting-started/main.go
+++ b/examples/getting-started/main.go
@@ -7,7 +7,7 @@ import (
func main() {
for {

- fmt.Println("Hello world!")

+ fmt.Println("Hello jerry!")
time.Sleep(time.Second * 1)
}
}

Once you save the file, you should see the pipeline kick off again to redeploy your application:

[getting-started getting-started] Hello jerry!
[getting-started getting-started] Hello jerry!

### Run a deployment pipeline once

There may be some cases where you don't want to run build and deploy continuously. To run once, use:

$ skaffold run

### More examples

## Community

- [skaffold-users mailing list](https://groups.google.com/forum/#!forum/skaffold-users)