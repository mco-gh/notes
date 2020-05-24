Federated Clusters and Global Ingress with Kubernetes

## 1. Overview

Google Container Engine makes it easy to run docker containers in the cloud. Google Container Engine uses [Kubernetes](http://kubernetes.io/), an open source container scheduler, to ensure that your cluster is running exactly the way you want it to at all times.

Follow along this lab to learn how to launch multiple Kubernetes clusters, tie them together with a Federated control plane, and launch a Ingress controller with a single, globally addressable IP address.

### What you'll learn

- Launch multiple Kubernetes cluster with Google Container Engine
- Setup Federation for multiple Kubernetes clusters on Google Cloud
- Create an Ingress controller backed by the Google Cloud HTTP load balancer

### What you'll need

- A Google Cloud Platform Project
- A Browser, such [Chrome](https://www.google.com/chrome/browser/desktop/) or [Firefox](https://www.mozilla.org/firefox/)

#### How will you use this tutorial?

Read it through only

Read it and complete the exercises

#### How would rate your experience with Google Cloud Platform?

Novice

Intermediate

Proficient

# Federated Clusters and Global Ingress with Kubernetes

 22 min remaining

   *1*Overview    *2*Setup and Requirements    *3*Creating Clusters    *4*Setting up DNS and Global IP Address    *5*Create the Federation Control Plane    *6*Congratulations!

Did you find a mistake? [Please file a bug](https://github.com/googlecodelabs/feedback/issues/new?title=[cloud-mongodb-statefulset]:).

[(L)](https://codelabs.developers.google.com/codelabs/cloud-mongodb-federated-ingress/index.html?index=..%2F..%2Findex#)Window size:  x

Viewport size:  x