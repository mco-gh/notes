PAAS comparison - Dokku vs Flynn vs Deis vs Kubernetes vs Docker Swarm (2017) by Jan Carlo Viray · 08 Feb 2017

# PAAS comparison - Dokku vs Flynn vs Deis vs Kubernetes vs Docker Swarm (2017)

 08 February 2017

This year (2017) is when container orchestration and technology will be standard and clear winners for different use cases will rise. Here are my personal notes on common paas technology, comparing Dokku vs Flynn vs Deis vs Kubernetes vs Docker Swarm.

**tldr**: Easy but no H/A? **Dokku**. Easy with H/A? **Flynn**. Easy with H/A and native out-of-the-box solution? **Docker Swarm**. Complex, but mature and scales infinitely - the big dawg? **Kubernetes**. Want to make the big dawg less scary but still use the big dawg? **Deis Workflow**.

Hacker News Discussion: [https://news.ycombinator.com/item?id=14531883](http://bit.ly/2r8jxAM)

## Dokku

The mini PaaS! It is more like the quick introduction to the wonderful world of PaaS. This can be run anywhere, even on a small single server. For simple deployments, this is wonderful. It however, does not scale to multiple clusters. Many are happy with it for their simple projects. Note that this is **single host** only, so “high availability” is non-existent. Want to have a PaaS in minutes? Choose Dokku!

**WHEN TO CHOOSE DOKKU**: for hobby and side projects that do not require high availability. Easy to deploy applications, with little to no devops needed.

## Flynn

The upgraded Dokku and is used by around a dozen companies. It can scale and has ability to be highly available, so there’s no single point of failure. It is noted as more production-ready than Dokku. Runs high availability databases within the platform in addition to stateless apps. Their goal is to have an easy to use unified solution, but at the cost of having a lot of components. Big plus: it has its own web dashboard! You can run in single server or scale out. It’s known for its flexibility and ease. This does not use CoreOS so you can run it on Ubuntu.

**WHEN TO CHOOSE FLYNN**: liked Dokku but need high availability and a web UI to manage your clusters? Choose this.

## Kubernetes

The big giant and the future of container orchestration. This is obviously the choice for more serious deployments. It is packed with 10 years of Google experience, plus it powered Pokemon Go deployment. This is undoubtly what you should choose if you are serious about scaling with container technology. Big caveit: it is very hard to setup that you will most likely want to host your application in a one-click solution that Google Cloud built.

**WHEN TO CHOOSE KUBERNETES**: you are serious pretty serious about deployment and you have serious scaling needs. You need something mature and battle-tested.

## Deis Workflow

Similar to Flynn but has more companies using it in production. It is built around the Kubernetes and Docker ecosystems. For v2, you need Kubernetes as your foundation. It provides a more developer-friendly workflow built on top of Kubernetes.

**WHEN TO CHOOSE DEIS WORKFLOW**: if you want a layer on top of Kubernetes that makes it easier to manage and deploy your applications and you don’t want to use Google Cloud.

## Docker Swarm

If you’re using Docker, you should have heard about Docker Swarm. It gives an out of the box solution for you, already preinstalled when you setup Docker. Check more on the official docs about this.

**WHEN TO CHOOSE DOCKER SWARM**: in my opinion, this has a very strong potential to be a contender against current solutions mentioned above but as of right now, it is still evolving.

## Conclusion

	Dokku           Hobby Projects / Prototypes that are not mission critical
	Flynn           Small Production Deployments
	Kubernetes      Huge Deployments and Mission Critical
	Deis Workflow   A friendlier workflow on top of Kubernetes
	Docker Swarm    Native

If you have any questions or comments, please post them below. If you liked this post, you can[share it with your followers](https://twitter.com/intent/tweet?url=http://www.jancarloviray.com/blog/paas-comparison-2017-dokku-flynn-deis-kubernetes-docker-swarm/&text=PAAS%20comparison%20-%20Dokku%20vs%20Flynn%20vs%20Deis%20vs%20Kubernetes%20vs%20Docker%20Swarm%20(2017)&via=jancarloviray) or [follow me on Twitter](https://twitter.com/jancarloviray)!