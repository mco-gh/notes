Orchestrating the Cloud with Kubernetes

## 1. Introduction

In this Codelab you will learn how to:

- Provision a complete [Kubernetes](http://kubernetes.io/) cluster using [Google Container Engine](https://cloud.google.com/container-engine)
- Deploy and manage Docker containers using kubectl
- Break an application into microservices using Kubernetes' Deployments and Services.

Kubernetes is all about applications and in this codelab you will utilize the Kubernetes API to deploy, manage, and upgrade applications. In this part of the workshop you will use an example application called "app" to complete the labs.

[App](https://github.com/kelseyhightower/app) is hosted on GitHub and provides an example 12-Factor application. During this workshop you will be working with the following Docker images:

- [kelseyhightower/monolith](https://hub.docker.com/r/kelseyhightower/monolith) - Monolith includes auth and hello services.
- [kelseyhightower/auth](https://hub.docker.com/r/kelseyhightower/auth) - Auth microservice. Generates JWT tokens for authenticated users.
- [kelseyhightower/hello](https://hub.docker.com/r/kelseyhightower/hello) - Hello microservice. Greets authenticated users.
- [ngnix](https://hub.docker.com/_/nginx) - Frontend to the auth and hello services.

Kubernetes is an open source project (available on [kubernetes.io](http://kubernetes.io/)) which can run on many different environments, from laptops to high-availability multi-node clusters, from public clouds to on-premise deployments, from virtual machines to bare metal.

For the purpose of this codelab, using a managed environment such as Google Container Engine (a Google-hosted version of Kubernetes running on Compute Engine) will allow you to focus more on experiencing Kubernetes rather than setting up the underlying infrastructure.

# Orchestrating the Cloud with Kubernetes

 60 min remaining

   *1*Introduction    *2*Setup and Requirements    *3*Get the sample code    *4*Quick Kubernetes Demo    *5*Pods    *6*Creating Pods    *7*Interacting with Pods    *8*Services    *9*Creating a Service    *10*Adding Labels to Pods    *11*Deploying Applications with Kubernetes    *12*Creating Deployments    *13*Cleanup    *14*What's next?

[(L)](https://codelabs.developers.google.com/codelabs/cloud-orchestrate-with-kubernetes/index.html?index=..%2F..%2Findex#)Window size:  x

Viewport size:  x