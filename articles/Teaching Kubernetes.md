Teaching Kubernetes

# Teaching Kubernetes

February 19, 2017

*This post made it to the front page of [Hacker News](https://news.ycombinator.com/item?id=13679705). Thanks for the comments and other discussion! I really appreciate the feedback. I’ve updated the first lesson’s outline to cover a use case overview and relevant tech comparisons. I forgot that one in the outline, but it’s included in the course.*

I recently finished my “Introduction to Kubernetes” course for [CloudAcademy](http://cloudacademy.com/). It should be published in a few weeks if you’d like to check it out. You can take the course under a free trial if you don’t already have an account on [CloudAcademy](http://cloudacademy.com/). The course coincides with mentoring and training I’ve been doing in my full-time job. It’s a good time to reflect on *why* I created the course the way I did and my objectives when teaching Kubernetes to newcomers.

## Goal

My goal is **teach people already working with containers how to deploy their existing applications to Kubernetes**. Let me unpack that. The target audience is people working with containers (hopefully in a production environment). They have experience dealing with problems such as scaling their deployment processes; internal networking; handling traffic from the public internet; autoscaling containers; and general bit and bobs that come from operating a non-monolithic container architecture. Deploying the overwhelming majority of applications to Kubernetes requires `Deployments` and `Services`. These two resources get you *really* far. It’s something like 70% of the 80/20 rule. So what’s the remaining 10%?

`Deployments` manage `Pods`. Odds are you’ll need init containers, liveness/readiness probes, volumes, and configuration maps along the way. Also, We don’t exist in a vacuum. Kubernetes itself is *not* enough. We all lean on supporting projects to achieve our goals–specifically projects like [Helm](https://helm.sh/) and [kops](https://github.com/kubernetes/kops). Thus, it’s vital to educate people on key players in the ecosystem they can leverage throughout their Kubernetes journey.

Hitting the sweet 80/20 sweet spots means teaching people how to use Kubernetes’ features for most application scenarios, what it cannot do, and key projects ecosystem that round out a full stack perspective.

## Outline

I prefer the bottom up approach because it builds foundational understanding required to climb the abstraction ladder. Kubernetes describes its problem space with a unique vernacular. The course starts here by explaining Kubernetes using it’s own vernacular. Personally, I think this most important area because people cannot communicate fluently without sharing the same vernacular. The course moves on to hands on exercises now that there’s a common language to discuss what’s going on. This starts with pods.

Pods are Kubernetes lowest building block. Step one is introduce pods and discuss how to access pods with services. Then scale out from a single pod, to multicontainer pods, multiple pods, and N-tier applications. The last lessons rounds on the remaining 10%.

Here’s my outline for a ~80 minute video course or ~1 day workshop:

1. Feature Overview and Vernacular

    - Kubernetes features

    - Kubernetes use cases

    - Kubernetes vs Docker Swarm vs DCOS vs ECS

    - Technical architecture (introduce the “scheduler” concept)

    - Terminology (~15 in total), Emphasis on:

        1. Pod

        2. Deployment

        3. Service

        4. Replica

        5. Cluster

        6. Resource

2. Pods & Service

    - Create a pod w/nginx

    - Make nginx `curl`‘able via a service

3. Multi-Container Pods & Service Discovery

    - Deploy the [sample application](https://gitlab.com/slashdeploy/microservice-example) in a single pod

    - Demonstrate inter-pod networking

    - Describe why a single pod does not make sense from a scaling perspective

    - Split the sample application into 3 tiers

    - Demonstrate cross pod service discovery

    - Jump off by asking how could to scale out this application

4. Deployments

    - Convert previous lesson’s pods to deployments

    - Demonstrate scaling by setting replicas

    - Configure autoscaling via `kubectl autoscale`

    - Demonstrate pausing, resuming, and undoing rollouts

5. Probes & Init Containers

    - Demonstrate how to block the app tier pods until the data store is ready

    - Clarify difference between liveness & readiness probes

    - Test container liveness with probes

    - Test container readiness with probes

6. Volumes

    - Introduce volume claims

    - Create a persistent volume for use with the data tier

7. Secrets & ConfigMaps

    - Create a secret token and populate an environment variable

    - Create a config map and populate environment variable from values

8. 10% Wrap Up

    - Clarify shortcuts we took in the course and better production practices

    - Ecosystem support tools for end users and operations engineers

    - Production preparedness

    - Grab bag for anything else to complete the 10%

I’m happy with the way the course turned out and using remixes of the outline for other purposes. People seem to learn a lot and end up confident in exploring more on their own. Feel free to use my outline to teach yourself Kubernetes or as a base to teach others.

Good luck out there. Happy teaching & happy learning!

 ![Adam Hawkins](../_resources/d3f294f9830f28b9fa2fa172b4456ac4.jpg)    [Adam Hawkins](http://blog.slashdeploy.com/2017/02/19/teaching-kubernetes/mailto:ahawkins@slashdeploy.com)

 [@adman65](https://twitter.com/adman65)