The downfall of Functions and the rise of Knative

![1*kTloY4S5BXgQSiqy_BIXBA.jpeg](../_resources/c63230b87c7c10be947586b44c3b7a8d.jpg)
![1*kTloY4S5BXgQSiqy_BIXBA.jpeg](../_resources/ed5ffc5ace77067b5a0b88c9c08e4913.jpg)

# The downfall of Functions and the rise of Knative

[![1*uNKbKGEYfez8mALOK3N7BA.jpeg](../_resources/86a9a5d13bdc76357ffd7c478aa8ffea.jpg)](https://medium.com/@idoshamun)

[Ido Shamun](https://medium.com/@idoshamun)
Draft · 2 min read

So maybe the title is a little exaggerating but now you are here and I would like to introduces to Knative, the Kubernetes add-on for serverless workloads.

First thing first, let’s talk about Functions and why they exist. There is an everlasting trend to reduce the overhead of deploying applications. It started with the transition from on-prem servers to the cloud, to managed services and Kuberentes and now Functions. With Functions, developers can focus only on their code which will be triggered by an HTTP request or a Pub/Sub message. They don’t have to think about anything else, devops, operating systems, hardware, networking and configurations are things of the past. Write your code and deploy with a simple command. Sounds good isn’t it? So let me tell you what you cannot do with Functions and why this abstraction is one step too much. If your serverless task is CPU intensive or requires GPU to serve deep learning models for example, there is nothing you can. Long tasks? no can do, you are limited by the maximum timeout (9 minutes). Special networking requirements? guess what… I guess it will improve over time but at least for me I find many use cases which cannot be done with Functions. Just recently, Google provided VPC access to Functions which really opened it up to new use cases but it is still lacking. Do not get me wrong there are still many use cases where Functions can shine and really make it easy but you can get to a dead-end pretty soon.

## Enter Knative

A Kubernetes-based platform to build, deploy, and manage modern serverless workloads. It is still in early development stages but already offered as a managed service called Cloud Run, still in beta though. Knative provides the ability to scale a deployment to zero pods and react to HTTP requests and events on demand, just like Functions. Knative Serving is all about serverless HTTP triggers and Knative Eventing is focused on reacting to events from different sources (such as Google Pub/Sub). The Eventing project utilizes [cloudevents](https://cloudevents.io/), a spec for defining events, this way you can be agnostic to the event source. Although it requires a little bit more heavy lifting than actual Functions, such as writing YAML configurations and having a Kubernetes cluster (most of us already have it anyway), it opens you to all Kubernetes goodies. You can customize whatever you want if you need and still enjoy the serverless world. Again, it is not the same as Functions but for me it makes much more sense and flexibility. I am only in the beginning of my journey exploring Knative but it surely is exciting!