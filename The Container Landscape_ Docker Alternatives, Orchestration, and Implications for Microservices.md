The Container Landscape: Docker Alternatives, Orchestration, and Implications for Microservices

# The Container Landscape: Docker Alternatives, Orchestration, and Implications for Microservices

![](../_resources/e707d0496b323b9b2f5e8109863aafec.jpg)

 *|* Posted by   [Kai Wähner](https://www.infoq.com/profile/Kai-W%C3%A4hner)   on Nov 20, 2016. Estimated reading time: 11 minutes *|*[ 2 Discuss](https://www.infoq.com/articles/container-landscape-2016#theCommentsSection)

- Share

- [![Share](../_resources/5571b0f25fad0a3fd9eceb16493bc139.gif)](https://www.addthis.com/bookmark.php?v=250&username=infoq)

- |

- [(L)](https://www.infoq.com/articles/container-landscape-2016#)

- [(L)](https://www.infoq.com/articles/container-landscape-2016#)

- [(L)](https://www.infoq.com/articles/container-landscape-2016#)

- [(L)](https://www.infoq.com/articles/container-landscape-2016#)

- [(L)](https://www.infoq.com/articles/container-landscape-2016#)

-

- ["Read later"](http://www.infoq.com/articles/container-landscape-2016)

- ["Reading List"](https://www.infoq.com/showbookmarks.action)

|     |
| --- |
| ## Key takeaways<br>- The container technology market is becoming crowded. Various technologies are competing for share of this emerging market<br>- Orchestration of containers is key for successful deployment and operation of containers in production.<br>- This article examines the various container technology platforms and tooling currently available<br>- Several cloud vendor services allow quick adoption and elastic scalability of container deployments, with varying degrees of ‘lock-in’<br>- We recommend that developers create the business logic of their microservices in a vendor -and platform- agnostic approach in order to be resilient to future developments within the container technology domain |

I attended a great event organized by [Microservices Meetup Berlin](http://www.meetup.com/Microservices-Meetup-Berlin): “[Orchestrating Microservices](http://www.meetup.com/Microservices-Meetup-Berlin/events/233416012/)”. They invited experts from various companies (Google, Microsoft, Amazon, Mesosphere, CoreOS, DigitalOcean) to present container technologies respectively cloud services and how they orchestrate container-based microservices. This article extends the content of the event and gives an overview about many different alternatives, their differences and the potential future of container tooling. The container war has just begun!

## Definition – Container Technologies and Orchestration Engines

If you do not live behind the moon you have probably heard of Docker and all the hype around it. However, we’ll begin with a short definition of two key container-based application concepts in order to establish a shared understanding:

-
  Related Vendor Content

### [Factors: The Reference Guide for Planning, Building & Releasing Apps](https://www.infoq.com/vendorcontent/show.action?vcr=4425&primaryTopicId=1893&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Fcontainer-landscape-2016&utm_source=infoq&utm_medium=VCR&utm_campaign=vcr_articles_click&utm_content=embedded)

### [Best Practices for Expanding Quality into the Build Cycle](https://www.infoq.com/vendorcontent/show.action?vcr=4387&primaryTopicId=1893&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Fcontainer-landscape-2016&utm_source=infoq&utm_medium=VCR&utm_campaign=vcr_articles_click&utm_content=embedded)

### [Monitor JavaScript errors using Site24x7 Real User Monitoring (RUM)](https://www.infoq.com/vendorcontent/show.action?vcr=4454&primaryTopicId=1893&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Fcontainer-landscape-2016&utm_source=infoq&utm_medium=VCR&utm_campaign=vcr_articles_click&utm_content=embedded)

### [How to build a CI/CD pipeline with Terraform](https://www.infoq.com/vendorcontent/show.action?vcr=4403&primaryTopicId=1893&vcrPlace=EMBEDDED&pageType=ARTICLE_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Farticles%2Fcontainer-landscape-2016&utm_source=infoq&utm_medium=VCR&utm_campaign=vcr_articles_click&utm_content=embedded)

### [Top 10 AWS Cloud Security Risks](https://www.infoq.com/infoq/url.action?i=15750&t=f)

Related Sponsor

 [![evident-io-logo-rsb1-032017.png](../_resources/42b207c06258ad85853124e9a5397527.png)](https://www.infoq.com/infoq/url.action?i=15752&t=f)

Evident.io helps organizations improve security visibility and simplify compliance across their public cloud infrastructure with the [**Evident Security Platform**](https://www.infoq.com/infoq/url.action?i=15772&t=f).

Containers run as a group of [namespaced processes](https://www.infoq.com/articles/build-a-container-golang) within a Linux operating system, avoiding the overhead of starting and maintaining virtual machines. Key differentiators of containers compared to VMs are the packaging format and portability being created as fit for purpose for modern infrastructure, and therefore lowering footprint and startup times, and providing repeatability, better resource utilization of servers and better integration into the whole development ecosystem (such as Continuous Integration/Delivery lifecycle). See [Microservices, Containers and Clout-Native Architectures](https://www.voxxed.com/blog/2016/06/microservices-containers-cloud-native-architectures-middleware/)” for more details.

- Orchestration includes especially the [following tasks](http://www.slideshare.net/sawjd/apache-mesos-and-the-new-open-source-architecture-of-the-modern-datacenter): Scheduling (placement, replication / scaling, resurrection, rescheduling,, upgrades, downgrades), resource management (memory, CPU, volumes, ports, IPs, images) and service management (i.e. orchestrating several containers together using labels, groups, namespaces, load balancing, readiness checking). I quoted [Mesophere](https://docs.google.com/presentation/d/1-0_04QMlI93fv4ubr6hrN2c4ZHBbRPft9GMzyrqJmI8) for this definition.

If you are still unsure about container orchestration, please watch this fascinating 8 min video: “[The Illustrated Children's Guide to Kubernetes](https://www.youtube.com/watch?v=4ht22ReBjno)”. This is one of the best technology videos I have ever seen! Worth watching even if you understand the concepts already.

## Container Alternatives and Cloud Services for Orchestration

Plenty of container alternatives and corresponding cloud services are available on the market that orchestrate microservices (and therefore the underlying containers). Container technologies and orchestration engines are usually used closely together. Often, they are built into the same tooling. Cloud offerings, where “users pay only for the resources - such as compute instances, load balancing and scheduling capabilities - that they use” are called [CaaS (Container as a Service)](http://searchitoperations.techtarget.com/definition/Containers-as-a-Service-CaaS).

The following list contains the differentiating container platform feature sets with different pros and cons. Also note that the following is – of course – not a complete list of container and orchestration offerings (but hopefully shows most of the currently relevant options):

- Docker is the container technology with most public traction and is “almost” a de facto container standard right now. Docker is open source with several vendors behind it. Though, Docker Inc. is the one “official” company controlling the project. They also recently [added the orchestration engine Docker Swarm to the main container project](https://blog.docker.com/2016/06/docker-1-12-built-in-orchestration/). Others like Red Hat and IBM contribute to the open source code. Various vendors offer support, consulting and cloud services (such as a public or private Docker Registry).
- [Core OS’ rkt](https://github.com/coreos/rkt) (pronounced “rocket”) is another container technology emerging together with its container orchestration engine [Fleet](https://coreos.com/using-coreos/clustering/). It is a low-level framework built directly on [systemd](https://wiki.freedesktop.org/www/Software/systemd/), often used as “foundation layer” for higher-level solutions. rkt focuses on security, composability (e.g. native Unix integration), and standards / compatibility – as differentiator to Docker. rkt also can run Docker images natively and has native Kubernetes integration via “[rktnetes](https://coreos.com/rkt/docs/latest/using-rkt-with-kubernetes.html)”. CoreOS therefore also offers an “Enterprise Kubernetes Solution” called [Tectonic](https://tectonic.com/). This might be very important for future adoption in more projects.
- [Cloud Foundry’s Garden](https://blog.pivotal.io/pivotal-cloud-foundry/features/cloud-foundry-container-technology-a-garden-overview) Garden is used under the hood of the open source PaaS CloudFoundry. As many relevant software vendors like IBM, SAP or Pivotal base their PaaS strategy on CloudFoundry, Garden containers get used by many enterprises “under the hood”. In contrary to Docker and rkt, there is no real market outside of CloudFoundry for Garden containers.
- [Kubernetes](https://www.infoq.com/articles/kubernetes.io) is an orchestration engine for containers with a huge community behind it. This project was released as open source by Google earlier in the year; with many other contributors including software vendors like Red Hat, CoreOS or Mesosphere. Kubernetes is open to run different container technologies such as Docker (mostly used today) or CoreOS’ rkt (pronounced “rocket”). The two most well-known offerings of Kubernetes are: [Google Container Engine](https://cloud.google.com/container-engine/) (public Kubernetes service) and Red Hat’s open source PaaS [OpenShift](https://www.openshift.com/) (based on Kubernetes, for hybrid cloud deployments). The latter adds some useful features on top of Kubernetes like an enhanced web user interface and an automated ‘source-to-deployment’ system that does not require knowledge about the underlying container and Docker subsystems.
- [Amazon AWS ECS](https://aws.amazon.com/ecs/): This is a public CaaS to manage Docker images (that can be stored in the accompanying ECS Registry), run Docker containers (ECS Runtime) and schedule / orchestrate / monitor these container instances (AWS CloudWatch). These can also be combined with other AWS services like Elastic Load Balancer (AWS ELB), Virtual Private Connection (AWS VPC) or Identity and Access Management (AWS IAM). AWS Simplified Workflow is also tightly integrated with AWS ECS to use Docker CLI commands (e.g. push, pull, list, tag).
- (Docker) CaaS Cloud Offerings are available by other cloud vendors, too. [Microsoft Azure Container Service (ACS)](https://azure.microsoft.com/en-us/services/container-service/) works together with Docker Swarm or Apache Mesos’ based DC/OS as container orchestration engine. Rancher Labs [Rancher](http://rancher.com/rancher/) also supports Docker Swarm, Kubernetes and Apache Mesos. Note that most CaaS have in common that you still have to create server instances (e.g. AWS EC2) first. You pay for the server instances where your CaaS container instances run on, instead of just paying for the container instances itself. If you want to pay by container instance, you need to leverage a “serverless architecture” (discussed later). Docker Inc also offers Docker cloud services, including [Docker Cloud](https://www.docker.com/products/docker-cloud) to deploy and manage Dockerized applications and [Docker Datacenter](https://www.docker.com/products/docker-datacenter) to integrate Docker into the enterprise software supply chain.
- Apache Mesos’ based DC/OS is a “distributed operation system” running on private and public cloud infrastructure that abstracts the resources of a cluster of machines and provides common services, i.e. it handles as cluster resource negotiator. It runs below the orchestration layer (Swarm, Kubernetes, et al), and is a complementary tool, therefore. Apache Mesos is intended for large scale and multi-use of different clusters on top of it. You “just” need to implement Mesos’ framework interface. Several frameworks are supported already, e.g. Docker or rkt containers via [Marathon](https://mesosphere.github.io/marathon/), batch processing via [Chronos](https://mesos.github.io/chronos/), but also big data solutions like Apache Hadoop, Apache Spark, Apache Kafka. [Mesosphere](https://mesosphere.com/) is the company behind Apache Mesos. They offer an open source distribution called DC/OS, which leverages Apache Mesos under the hood; this is comparable to Apache Hadoop and its distributions like Cloudera or Hortonworks.
- [Flockport](https://www.flockport.com/) is a startup focused on building an App store based on LXC containers that users can deploy in seconds on any server, any cloud and any provider. Flockport is focused on simplicity, making things just work, giving users a cloud-like flexibility of portables instances and workloads that can be moved across servers easily. There is a great blog post explaining “[the key differences between LXC and Docker](https://www.flockport.com/lxc-vs-docker/)”.
- [DigitalOcean](https://www.digitalocean.com/) is a cloud infrastructure provider which allows developers to build and deploy microservices by creating so-called Droplets (i.e. units of work) on their global cloud data centers, plus leveraging block storage and networking features. A droplet can be an instance of an operating system image, but also a Docker container application. DigitalOcean takes care of provisioning, monitoring and other platform requirements for the Droplets. It can be combined with different orchestration tools such as Docker Swarm, Kubernetes, Apache Mesos or Dokku (a Docker-powered mini-Heroku PaaS). Therefore, DigitalOcean is more like a IaaS - comparable to AWS EC2 - but focusing on ease-of-use to deploy and run your microservices clusters.
- [Microsoft Azure Service Fabric](https://azure.microsoft.com/en-us/services/service-fabric/) is a microservices framework and container orchestration engine. It is not dependent on Microsoft Azure, but also usable on premise and in other clouds (therefore, the term “Azure” is a little bit misleading in the product name). Service Fabric leverages Docker for container management on both Linux and Windows containers. It allows to use different programming languages (e.g. C#, Java, Powershell) and is supposed to support more container technologies in addition to Docker and also other programming languages in the future.
- Serverless Container Architectures: An emerging concept providing a service to deploy “real” functional-style cloud-native microservices. The main idea is to reach 100% utilization. Thus, you just pay by function call (see e.g. [AWS Lambda](https://aws.amazon.com/lambda/), [Google Cloud Functions](https://cloud.google.com/functions/), [Microsoft Azure Functions](https://azure.microsoft.com/en-us/services/functions/)), which differs to CaaS offerings where you still have to manage the underlying operating system instances yourself (i.e. run, scale, utilize and pay). However, serverless offerings usually support only function calls of a few programming languages like Java or Python. [IBM OpenWhisk](http://www.ibm.com/cloud-computing/bluemix/openwhisk/) and [funktion](https://github.com/fabric8io/funktion) (sponsored by Red Hat / JBoss) are two serverless vendor-agnostic open source offerings which also support Docker containers to realize serverless container architectures. While OpenWhisk is becoming a “real product offering”, I see funktion more as small framework without much commitment these days. Hopefully, the big cloud vendors will also provide Docker containers in the foreseeable future.

## Container Wars with Various Technologies

As you can see, there is so many different technologies, frameworks and cloud services available on the market for container packaging and orchestration. The above is not even a complete list, and there are still new ones emerging.

Therefore, the key lessons learned from this event (from developer’s perspective): Do not focus on developing code for the container under the hood. Care instead about the business logic. Implement your microservices in a vendor agnostic way.

Do not make the same fault as we all did with J2EE / Java EE where all vendors used the same standard specifications, but still offered many vendor-dependent features and “added value” in their specific “standard implementation”. Migration, i.e. deployment to another Java EE application server was a lot of efforts (re-development, testing, …); sometimes a complete re-write was easier and faster.

Docker has huge momentum today. However, there exist some doubts about what the future will bring. Several software vendors are not happy with the power of Docker Inc. as company behind Docker. For example, putting Docker Swarm Mode into the main Docker project made other orchestration vendors like Red Hat or Google unhappy, because they focus on Kubernetes as container orchestration tool. Therefore, these vendors created a new open source project “[cri-o](https://github.com/kubernetes-incubator/cri-o)” to [run containers in Kubernetes without Docker](http://thenewstack.io/oci-building-way-kubernetes-run-containers-without-docker/). Read the following InfoWorld article for more about the latest discussion of forking the current Docker project into an independent open source project: “[New Red Hat project looks a lot like a Docker fork](http://www.infoworld.com/article/3123412/application-development/new-red-hat-project-looks-a-lot-like-a-docker-fork.html)”.

## Combining Differing Container Technologies and Tools

Note, that the discussed technologies and tools can also work together very well. Often, they are really complementary. There is not always a need for war!

For example, a Kubernetes cluster can manage pods with different container technologies such as Docker or rkt in parallel. Another example is Apache Mesos, which can manage different clusters – including plain Docker Swarm clusters, Kubernetes clusters, but also big data clusters using frameworks like Apache Hadoop or Apache Spark. Though, note that this is not a trivial configuration! Just as side note: Even [Apache Hadoop will offer Docker support soon](https://twitter.com/KaiWaehner/status/780697629134946304) to deploy independent components such as Apache Kafka or Apache Spark in their own container instances (I saw the roadmap at [Hortonwork’s roadshow](http://hortonworks.com/roadshow/) last week where they presented their future Hadoop strategy).

## The Future of Containers: To Standardise or Not?

Let’s see what the future brings regarding a potential Docker fork, and regarding all the discussions about standardization of container technologies. The following three options exist for next years:

1. Docker gets the de facto standard
2. Different technologies spread out in parallel; maybe including a Docker fork

3. Container technologies become (at least partly) standardized) and different technologies respectively vendors adopt the standard

Let’s hope that #3 will happen… Several initiatives and discussions are going on these days, including appc ([App Container specification](https://github.com/appc/spec)), CNI ([Container Network Interface](https://github.com/containernetworking/cni)), CNCF ([Cloud Native Computing Foundation](https://cncf.io/)) or OCI ([Open Container Initiative](https://www.opencontainers.org/). For instance, the OCI tries to standardize container image definitions. Docker, CoreOS, Google, Red Hat, Facebook, Amazon and others work together here.

## Conclusion: Develop Container-Agnostic Microservices

This article discussed plenty of different fantastic container technologies, orchestration platforms and cloud services. All of them have their pros and cons. In addition, the market is evolving quickly.

The key conclusion for now: Develop the business logic of your microservices in a vendor-agnostic approach to be future-safe and have fun leveraging all the great advantages and features of microservices and container technologies in opposite to monoliths and heavyweight virtual machines. The article “[Can we avoid cloud-vendor lock in?](http://aaronallport.com/2016/03/23/can-we-avoid-cloud-vendor-lock-in.html)” elaborates this in more detail.

In summary, no matter if you develop your business logic within a microservice with source code (using technologies such as Java, .Net or Go) or visual coding (such as middleware technologies), you should be able to develop it once and be able to deploy it in different containers, test environments or cloud providers without re-developing it or even having to change the technology you chose before.

## About the Author

**![Kai-Wahner.jpg](../_resources/2f1d33bd46e4536679099d1c3138630f.jpg)Kai Wähner** is Technology Evangelist and Community Director for TIBCO Software - a leading provider of integration and analytics middleware. His main area of expertise lies within the fields of Big Data, Advanced Analytics, Machine Learning, Integration, SOA, Microservices, BPM, Cloud, Internet of Things and Programming Languages such as Java EE, Groovy or Golang. He regularly write about new technologies, articles and conference talks on his [blog](http://www.kai-waehner.de/).

- [Personas]()
- [**Development**](https://www.infoq.com/development)
- [**Architecture & Design**](https://www.infoq.com/architecture-design)
- [**DevOps**](https://www.infoq.com/Devops)
- [Topics]()
- [Containers](https://www.infoq.com/Containers)
- [PaaS](https://www.infoq.com/PaaS)
- [Infrastructure](https://www.infoq.com/Infrastructure)
- [Docker](https://www.infoq.com/docker-2)
- [Cloud Computing](https://www.infoq.com/cloud-computing)
- [Orchestration](https://www.infoq.com/orchestration)

Related Editorial

###   [A Comparison of Some Container Orchestration Options](http://www.infoq.com/news/2017/02/compare-container-orchestration?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)

###   [Docker 1.13 Released with Improved CLI, Compose-File Support for Swarm Mode, and Secrets API](http://www.infoq.com/news/2017/01/docker-1.13?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)

###   [Deliver Docker Containers Continuously on AWS](http://www.infoq.com/presentations/docker-ecs-aws?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)

###   [Public Docker Image Vulnerability Research Findings Released](http://www.infoq.com/news/2017/03/docker-image-vulnerabilities?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)

###   [Running Docker Containers Securely in Production](http://www.infoq.com/news/2016/12/containers-secure-production?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)

### Tell us what you think

Community comments   [Watch Thread](#)

 [**Nice overview**   by Sebastian Schmidt Posted Nov 23, 2016 10:11](https://www.infoq.com/articles/container-landscape-2016#anch142326)

 [**Re: Nice overview**   by Daniel Bryant Posted Nov 28, 2016 09:55](https://www.infoq.com/articles/container-landscape-2016#anch142403)

 **Nice overview**    Nov 23, 2016 10:11 by ["Sebastian Schmidt"](https://www.infoq.com/profile/Sebastian-Schmidt.3)

Hi Kay, thanks for that overview to container land.

Looking at flockport.com it seems a bit outdated. Do you know of current developement in that area and of that company? LXC seems to be actively maintained, but the flockport website is not very active...

- [Like](https://www.infoq.com/articles/container-landscape-2016#)

- [Reply](#)

- [Back to top](https://www.infoq.com/articles/container-landscape-2016#)

 **Re: Nice overview**    Nov 28, 2016 09:55 by ["Daniel Bryant"](https://www.infoq.com/profile/Daniel-Bryant)

Hi Sebastian,

Canonical are doing interesting things with LXD, which builds upon LXC: [linuxcontainers.org/lxd/](https://linuxcontainers.org/lxd/)

Best wishes,

Daniel

- [Like](https://www.infoq.com/articles/container-landscape-2016#)

- [Reply](#)

- [Back to top](https://www.infoq.com/articles/container-landscape-2016#)

RELATED CONTENT

- [Deliver Docker Containers Continuously on AWS](http://www.infoq.com/presentations/docker-ecs-aws?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   May 25, 2017  [![Phil.JPG.jpg](../_resources/e95c661c8d5642ae1cfe212bc90adfc3.jpg)](http://www.infoq.com/presentations/docker-ecs-aws?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Continuous Delivery with Kubernetes the Hard Way](http://www.infoq.com/articles/continuous-delivery-kubernetes?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   May 30, 2017  [![GettyImages-654388878 copy.jpg](../_resources/be667a8f5fc9468cd0852b54626fbe57.jpg)](http://www.infoq.com/articles/continuous-delivery-kubernetes?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)
- [Elevating Builds into a Container](http://www.infoq.com/articles/elevating-builds-into-containers?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   Dec 29, 2016  [![article-logo.jpg](../_resources/05c5d4fdcb89f36e4cb8d60e8d58a6ed.jpg)](http://www.infoq.com/articles/elevating-builds-into-containers?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)
- [Ocado Technology Releases “Kubermesh”, a Prototype Self-Provisioning Mesh Network Kubernetes Cluster](http://www.infoq.com/news/2017/06/kubermesh-ocado?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   Jun 04, 2017
- [Mesos: A State-of-the-art Container Orchestrator](http://www.infoq.com/presentations/mesos-api?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jan 07, 2017  [![Jie.JPG.jpg](../_resources/d3239914cc30f90b965e535e76daf438.jpg)](http://www.infoq.com/presentations/mesos-api?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Red Hat to Acquire Codenvy to Extend DevOps Tools Capability](http://www.infoq.com/news/2017/05/red-hat-acquires-codenvy?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   May 31, 2017
- [Datacenter Operators: Bumpy Ride Running Containers on Infrastructure Built for VMs](http://www.infoq.com/news/2017/05/diamanti-named-cool-vendor?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   May 23, 2017
- [Dev to Prod in Five Minutes: Is Your Company Ready?](http://www.infoq.com/presentations/embracing-containers?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   May 27, 2017  [![Car.JPG.jpg](../_resources/0ca05fc8c359dbfbc928aaaaa1f7abb1.jpg)](http://www.infoq.com/presentations/embracing-containers?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [When Containers Attack!](http://www.infoq.com/presentations/history-full-stack-engineers?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   May 27, 2017  [![Anne.JPG.jpg](../_resources/3268193f8701ca9c27b82c99849193f2.jpg)](http://www.infoq.com/presentations/history-full-stack-engineers?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [cgroupv2: Linux's New Unified Control Group System](http://www.infoq.com/presentations/cgroup-v2?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   May 27, 2017  [![CHris.JPG.jpg](../_resources/6af8967083b4838d65207715eab9f935.jpg)](http://www.infoq.com/presentations/cgroup-v2?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Introducing Sock Shop: A Cloud Native Reference Application](http://www.infoq.com/articles/sock-shop?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   May 25, 2017  [![logo.jpg](../_resources/79ab52ea66dff9124d84385c489a8035.jpg)](http://www.infoq.com/articles/sock-shop?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)

SPONSORED CONTENT

- [![](../_resources/00b6c5f720d6a0ec5980576daf9f38d9.jpg)](https://www.infoq.com/vendorcontent/show.action?vcr=4357&utm_source=infoq&utm_medium=related_content_sponsored_link&utm_campaign=relatedContent_sponsored_articles_clk&utm_content=top)[Rugged DevOps - 10 Ways to Embed Security into DevOps Patterns](https://www.infoq.com/vendorcontent/show.action?vcr=4357&utm_source=infoq&utm_medium=related_content_sponsored_link&utm_campaign=relatedContent_sponsored_articles_clk&utm_content=top)

This eBook provides advice from 10 SecDevOps leaders on how to bake security into DevOps practices rather than treating it as an afterthought.

- [![](../_resources/42623879fbbd096f981bf9a54b63b364.jpg)](https://www.infoq.com/vendorcontent/show.action?vcr=4458&utm_source=infoq&utm_medium=related_content_sponsored_link&utm_campaign=relatedContent_sponsored_articles_clk&utm_content=top)[16 Ways to Protect Your Cloud from Ransomware](https://www.infoq.com/vendorcontent/show.action?vcr=4458&utm_source=infoq&utm_medium=related_content_sponsored_link&utm_campaign=relatedContent_sponsored_articles_clk&utm_content=top)

In this ebook, we look at the different pieces of the cloud stack and address their unique security needs with precautions that enterprises should take to make their environment far more resistant to ransomware threats.

Sponsored by[![evident-io-logo-rsb1-032017.png](../_resources/42b207c06258ad85853124e9a5397527.png)](https://www.infoq.com/infoq/url.action?i=15752&t=f)

RELATED CONTENT

- [Examining the Internals of a Serverless Platform: Moving towards a ‘Zero-Friction’ PaaS](http://www.infoq.com/articles/serverless-internals?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   Apr 07, 2017  [![GettyImages-523399194-copy.jpeg](../_resources/f021c2ff6b28e0fc8efcc184e6d46e1c.jpg)](http://www.infoq.com/articles/serverless-internals?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)
- [A Security Approach for a Cloudy World: An Interview with Pete Cheslock](http://www.infoq.com/articles/security-cloud-cheslock?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   Mar 17, 2017  [![LOGO-b.jpeg](../_resources/84875cd6b91b9bff73f1147b75036704.jpg)](http://www.infoq.com/articles/security-cloud-cheslock?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)
- [Architecting for Failure in a Containerized World](http://www.infoq.com/presentations/architecture-failure-container?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Feb 16, 2017  [![Tom.JPG.jpg](../_resources/ab2a97e2a33dcc8944c4d5c3c55791b7.jpg)](http://www.infoq.com/presentations/architecture-failure-container?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Petabytes Scale Analytics Infrastructure @Netflix](http://www.infoq.com/presentations/netflix-big-data-infrastructure?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Feb 16, 2017  [![doi.JPG.jpg](../_resources/fc5908d1ac3a65ec3db6857818f8d318.jpg)](http://www.infoq.com/presentations/netflix-big-data-infrastructure?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Orchestrate All the Things! with Spring Cloud Data Flow](http://www.infoq.com/presentations/orchestrate-spring-cloud-data-flow?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jan 20, 2017  [![doi.JPG.jpg](../_resources/2fc72c90ed2275eb97504805d57e3b1e.jpg)](http://www.infoq.com/presentations/orchestrate-spring-cloud-data-flow?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Amazon ECS: a Platform to Run Production Containers](http://www.infoq.com/presentations/amazon-ecs?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jan 08, 2017  [![Uta.JPG.jpg](../_resources/34a895e9f793f02d9eb36b37540fcc79.jpg)](http://www.infoq.com/presentations/amazon-ecs?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Elastic Efficient Execution of Varied Containers](http://www.infoq.com/presentations/netflix-containers-2016?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jan 07, 2017  [![Sha.JPG.jpg](../_resources/35d5c515f6297c3585ae869a4e83aa3d.jpg)](http://www.infoq.com/presentations/netflix-containers-2016?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Roundtable: The Role of Enterprise Architecture in a Cloudy World](http://www.infoq.com/articles/enterprise-architecture-cloud?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   Apr 04, 2017  [![GettyImages-595347768-copy.jpeg](../_resources/16cc5f901155a80e8c300d920fcc4e9d.jpg)](http://www.infoq.com/articles/enterprise-architecture-cloud?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)
- [Introduction to DocumentDB](http://www.infoq.com/presentations/documentdb?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Dec 26, 2016  [![Brian.JPG.jpg](../_resources/9c5e6a7f1b741cf40e29565f51557519.jpg)](http://www.infoq.com/presentations/documentdb?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Using FlameGraphs to Illuminate the JVM](http://www.infoq.com/presentations/flamegraphs?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jun 14, 2017  [![Nit.JPG.jpg](../_resources/5eb53c16a938e33bad7ee728dd993087.jpg)](http://www.infoq.com/presentations/flamegraphs?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Introducing FaunaDB Serverless Cloud](http://www.infoq.com/articles/faunadb-serverless?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   Jun 14, 2017  [![LOGO-FAUNA.jpg](../_resources/a96ea1fe4b4c0e609fb352b7ebeb3a72.jpg)](http://www.infoq.com/articles/faunadb-serverless?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)

RELATED CONTENT

- [Enhancing Google Maps with Deep Learning and Street View](http://www.infoq.com/news/2017/06/google-maps-deep-learning-street?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   Jun 14, 2017
- [Event Sourcing on the JVM](http://www.infoq.com/presentations/event-sourcing-jvm?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jun 14, 2017  [![Gre.JPG.jpg](../_resources/8c60e2b9522f8b7ce96b685ecbe15dc3.jpg)](http://www.infoq.com/presentations/event-sourcing-jvm?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Building a Startup within a Bank - Q&A with Peterjan van Nieuwenhuizen](http://www.infoq.com/news/2017/06/startup-within-bank?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   Jun 13, 2017
- [RepreZen Releases KaiZen Open-Source Editor and Parser for Open API 3.0](http://www.infoq.com/news/2017/06/reprezen-kaizen?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   Jun 13, 2017
- [Introducing Reladomo - Enterprise Open Source Java ORM, Batteries Included! (Part 2)](http://www.infoq.com/articles/Reladomo-Open-Source-ORM-Part2?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_text)   Jun 13, 2017  [![logo-java.jpg](../_resources/007a22412eb630dc39539ada783437fd.jpg)](http://www.infoq.com/articles/Reladomo-Open-Source-ORM-Part2?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=articles_link&utm_content=link_image)
- [Safari 11 Adds Missing Features, Improves Privacy by Default](http://www.infoq.com/news/2017/06/safari-11-announced-with-webrtc?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   Jun 12, 2017
- [Distributed Systems Theory for Practical Engineers](http://www.infoq.com/news/2017/06/distributed-systems-theory?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=news_link&utm_content=link_text)   Jun 12, 2017
- [The Morning Paper Issue 5 - Computer Science Applied](http://www.infoq.com/minibooks/emag-the-morning-paper-5?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=minibooks_link&utm_content=link_text)   Jun 12, 2017  [![image-small-logo.jpeg](../_resources/b444ee6f7602d62cb6b9cb00ee68ac49.jpg)](http://www.infoq.com/minibooks/emag-the-morning-paper-5?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=minibooks_link&utm_content=link_image)
- [Boost Business Agility with Contemporary HR Practices](http://www.infoq.com/presentations/hr-agile?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jun 12, 2017  [![Fab.JPG.jpg](../_resources/999f17351389c39eb14e8e19782f45e5.jpg)](http://www.infoq.com/presentations/hr-agile?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [Innovation Agility – Who Says the Corporate Behemoth Can’t Achieve](http://www.infoq.com/presentations/innovation-agility?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jun 12, 2017  [![Iq.JPG.jpg](../_resources/aedfb06e3e113404ace3258edc8deee8.jpg)](http://www.infoq.com/presentations/innovation-agility?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)
- [C# 7](http://www.infoq.com/presentations/c-sharp-7?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_text)   Jun 12, 2017  [![Jon.JPG.jpg](../_resources/4b11325a7f567463bc6def2771648412.jpg)](http://www.infoq.com/presentations/c-sharp-7?utm_campaign=rightbar_v2&utm_source=infoq&utm_medium=presentations_link&utm_content=link_image)

### InfoQ Weekly Newsletter

Join a community of over 250 K senior developers by signing up for our newsletter

[![click2view_en.png](../_resources/dc8df6f0b8512988c19d373723b404cf.png)](https://www.infoq.com/newsletter_sample.html)