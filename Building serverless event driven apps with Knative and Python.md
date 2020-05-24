Building serverless event driven apps with Knative and Python

![1*fWtVse6DItxvOBowU85Www.png](../_resources/a1b7e024e0ba63b4b69525fa78792520.png)

# Building serverless event driven apps with Knative and Python

[![0*YnRFGedts8yaO8qf.](../_resources/572bd2e1b9184e4de97523d2efc32031.jpg)](https://blog.elegantmonkeys.com/@ronnagar?source=post_header_lockup)

[Ron Nagar](https://blog.elegantmonkeys.com/@ronnagar)
Jun 12·3 min read

### Knative Introduction

Knative is an extension to [Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) that provides a set of tools to deploy serverless workload.

Knative is built by the following major components:

1. 1.[Build](https://knative.dev/docs/build) — Source-to-container build orchestration.

2. 2.[Eventing](https://knative.dev/docs/eventing) — Management and delivery of events.

3. 3.[Serving](https://knative.dev/docs/serving) — Request-driven compute that can scale to zero.

In this article, we will focus on the Eventing component. It provides infrastructure for serverless event driven architecture which runs your container when an event is fired. Knative Eventing supports different event sources (such as GitHub events, Pub/Sub, etc) and you can even write your own custom [event source](https://knative.dev/docs/eventing/samples/).

We chose Knative instead of other traditional serverless platforms (Functions, Lambda, etc) for the following reasons:

1. 1.It is powered by containers, meaning you can write code however you like, in every language or framework, with every module you need as long as you can make a container out of it. Usually, other serverless platforms limit you to specific runtime environments which they support.

2. 2.Resources are fully customizable (CPU, GPU, networking, etc…), as long as your Kubernetes cluster is equipped with the relevant resources you are good to go. Just like every Kubernetes deployment, you have to state what resources you need. Other serverless solutions limit the resources, these limitations are often a no-go for us.

3. 3.No timeout limit so you can deploy long-running processes (data analysis, image processing and what not). This is impossible to achieve with other serverless platforms as they usually have a timeout limit.

4. 4.The Eventing component uses [cloudevents](https://cloudevents.io/) as the spec for publishing the events. Basically, it helps us writing an event source agnostic code. We just have to understand the payload of the event but do not have to integrate directly with the event source or parse the event differently.

However, it is not all roses and butterflies and we have to also mention the downside. Knative is still in a very early stage (as of today the latest version is 0.6), meaning the API may change along the way and upgrades may break your deployments. Compared to other serverless solution it is more cumbersome to write all these Kubernetes YAMLs and install everything.

This is why we isolate Knative to its own cluster and do not mix our day-to-day cluster with the Knative one. We connect relevant services with VPC and load balancers.

### Knative Eventing and Python

Our primary use case for using Knative is to run long CPU-bound data analysis processes when new data arrives in the system. As most data analysis tasks, they were written in Python by our data science team. Unfortunately, Knative Eventing examples are in Go and the only library available for easily bootstrapping a Knative Eventing project is again Go. We understood that we have to create a similar open-source library for Python so others may utilize it as well. After a bit of research and digging into the Go library code, we realized that all we need to implement is an HTTP server which listens to POST requests and parse the cloudevents payload. Behind the scenes, Knative Eventing utilizes Knative Serving and upon an event is fired a POST request to the Knative Eventing container. We are glad to share our open source project, [python-kncloudevents](https://github.com/elegantmonkeys/python-kncloudevents), for easily integrating Python and Knative Eventing[.](https://github.com/elegantmonkeys/python-kncloudevents)

The usage of python-kncloudevents is very simple, All you need to do is to write a function that receives cloudevents as a parameter. To access the event data you can just call the Data function of the cloudevent. Now to run your function when the event is fired all you need to do is to create *CloudeventsServer* instance and run *start_receiver* function that accepts your function.

![](../_resources/2b263c794af6e2cb2914218e3d1287f9.png)

|     |     |
| --- | --- |
| 1   | import sys |
| 2   | from kncloudevents import CloudeventsServer |
| 3   | import logging |
| 4   |     |
| 5   | logging.basicConfig(stream=sys.stdout, level=logging.INFO) |
| 6   |     |
| 7   |     |
| 8   | def  run_event(event): |
| 9   |  try: |
| 10  | logging.info(event.Data()) |
| 11  |  except  Exception  as e: |
| 12  | logging.error(f"Unexpected error: {e}") |
| 13  |  raise |
| 14  |     |
| 15  |     |
| 16  | client = CloudeventsServer() |
| 17  | client.start_receiver(run_event) |

 [view raw](https://gist.github.com/ron212/e9e38bb7cb92222e86c15d4f5cb069d9/raw/2e90ebea4a568ba9d47db15fc49713ac4092a794/event_display.py)  [event_display.py](https://gist.github.com/ron212/e9e38bb7cb92222e86c15d4f5cb069d9#file-event_display-py) hosted with ❤ by [GitHub](https://github.com/)

### Conclusion

Knative is great for building serverless workload that needs flexibility in resources, runtime and duration. Knative allows building event driven architecture agnostic to your dependencies and environment.

If you need to run event based processes which demand a customized environment, Knative is the right choice for you. If you want to build quick and simple functions, the managed serverless platforms like Functions or Lambda might fit you as well.

Enjoy hacking!