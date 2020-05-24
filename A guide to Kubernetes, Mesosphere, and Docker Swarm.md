A guide to Kubernetes, Mesosphere, and Docker Swarm

 [**](https://insights.hpe.com/)

 [**](https://insights.hpe.com/)
 ![](../_resources/e0d528d54235e48f3e053b9b35e60ac0.jpg)
 February 15, 2017

# Container orchestration primer: Explaining Docker swarm mode, Kubernetes and Mesosphere

 Here's what you need to know about the three most popular container management programs.

Containers, a lightweight way to virtualize applications, are an important element of any DevOps plan. But how are you going to manage all of those containers? Container orchestration programs—[Kubernetes](https://kubernetes.io/),[Mesosphere Marathon](https://mesosphere.github.io/marathon/), and [Docker swarm mode](https://www.docker.com/products/docker-swarm)—make it possible to manage containers without tearing your hair out.

Before jumping into those, let's review the basics. Containers are the fastest growing cloud-enabling technology, [according to 451 Research](https://451research.com/report-long?icid=4095), primarily because containers use [far fewer system resources than do virtual machines](http://www.networkworld.com/article/3068392/cloud-storage/containers-vs-virtual-machines-how-to-tell-which-is-the-right-choice-for-your-enterprise.html) (VMs). After all, a VM runs not merely an operating system, but also a virtual copy of all the hardware that the OS needs to run. In contrast, containers demand just enough operating system and system resources for an application instance to run.

In terms your CFO can understand: That means you can run from four to 10 times as many server instances on the same computer hardware as you can using VMs. The result is that more applications can run on hardware you already have humming in your data center. What’s not to like?

In addition, and this is something sysadmins love, you can easily deploy applications with containers. “Containers give you instant application portability,” says James Bottomley, a leading Linux kernel developer.

While containers have been around since 2000 and FreeBSD jails, no one paid much attention until [Docker came along in 2013](http://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/). Then—bang!—everyone and his CTO wanted to deploy containers. In 2016 the [container technologies market generated $762 million in revenue](https://451research.com/images/Marketing/press_releases/Application-container-market-will-reach-2-7bn-in-2020_final_graphic.pdf), according to 451 Research.  By 2020, annual container revenue is expected to reach $2.7 billion, for a 40 percent compound annual growth rate.

There’s only two problems: How do you secure all those containers—a subject for another day—and how do you deploy and manage them?

### Containers need management

As with any other element of your cloud infrastructure, containers need to be monitored and controlled. Otherwise, you literally have no idea what’s running on your servers.

Containers like Docker can be used with DevOps tools such as[Puppet](http://puppetlabs.com/),[Chef](http://www.getchef.com/chef/), and[Ansible](http://www.ansible.com/home), but those tools are not optimized for containers. As[DataDog](https://www.datadoghq.com/), a cloud-monitoring company, points out in its report on[real-world Docker adoption](https://www.datadoghq.com/docker-adoption/), “Containers’ short lifetimes and increased density have[significant implications](https://www.datadoghq.com/blog/the-docker-monitoring-problem/) for infrastructure monitoring. They represent an order-of-magnitude increase in the number of things that need to be individually monitored.

Monitoring solutions that are host-centric, rather than role-centric, quickly become unusable.

There are two general types of monitoring tools. There's orchestration, a fancy term that refers to clustering and scheduling containers. Few developers dabble in orchestration. And then there's container management, which handles the administration tasks for containerized applications and application components.

Enter Docker swarm mode, Kubernetes and Mesosphere DC/OS. These open-source tools are not interchangeable, nor do they directly compete with each other. To one degree or another, all of them provide the following features:

- **Provisioning**: These tools can provision or schedule containers within a container cluster and launch them. Ideally, they spin up containers in the best VM depending on your requirements, such as resources and geographical location.
- **Configuration scripting**: Scripting permits you to load your specific application configurations into containers in the same way you might already be using [Juju Charms](https://jujucharms.com/), [Puppet Manifests](https://www.digitalocean.com/community/tutorials/configuration-management-101-writing-puppet-manifests), or [Chef recipes](https://docs.chef.io/recipes.html). Typically, these are written in YAML or JSON.
- **Monitoring**: The container management tools track and monitor containers’ health and hosts in the cluster. If they do their job,  the monitoring tool spins up a new instance when a container crashes. If a server fails, the tool restarts the containers on another host. The tools also run system health checks and report irregularities with the containers, the VMs they live in and the servers on which they run.
- **Rolling upgrades and rollback**: When you deploy a new version of the container, or the applications running within the containers, the container management tools automatically update them across your container cluster. If something goes wrong, they enable you to roll back to known good configurations.
- **Service discovery**: In old-style applications, you need to spell out explicitly where the software can find each service that’s required to run. Containers use [service discovery](https://docs.docker.com/docker-cloud/apps/service-links/) to find their appropriate resources.

Sound familiar? It should. As analyst Dan Kusnetzky points out, [containers work a lot like the service-oriented architecture](https://virtualizationreview.com/articles/2016/12/01/soa-in-disguise.aspx) (SOA) that got so much attention during the 2000s. SOA, for those of you who missed that technology, broke up applications into individual, stand-alone services. Its technical barrier: Network communications were an order of magnitude slower than inter-process communications. Containers run far faster than SOA because they tend to use resources on the same server. These tools help front-end applications, say a WordPress instance, dynamically discover its corresponding MySQL instance via DNS or a proxy.

- **Container policy management**: Where do you want containers to launch? How many should be assigned per CPU? All these questions and more can be answered by setting up the correct container policies.
- **Interoperability**: And, of course, containers should work with your existing IT management tools.

Finally, all three of these container management tools work with a variety of cloud platforms, including [OpenStack Magnum](https://wiki.openstack.org/wiki/Magnum) and [Azure Container Services](https://azure.microsoft.com/en-us/services/container-service/).

You could try to build your own container management program, but why re-invent the wheel? Besides, all three are built on open-source foundations; you can always add any feature you need. There is no value in starting from scratch.

So much for the generalities. Let’s get to the specifics.

### Docker swarm mode

If you’re new to containers, you probably started with Docker, which was the first container program to attract a large user base. Your natural instinct is to turn to a container manager built by the same people who designed your container infrastructure, which means Docker Swarm.

As of Docker 1.12, Docker’s go-forward model [is for orchestration to be built-in](https://blog.docker.com/2016/06/docker-1-12-built-in-orchestration/), which it calls swarm mode. Docker Swarm, Docker's standalone orchestrator, has taken a backseat to this built-in functionality. Swarm mode gives users control over the full application lifecycle, not just container clustering and scheduling.

The difference between Docker Swarm and swarm mode? With Docker 1.12, s[warm mode](https://docs.docker.com/engine/swarm/) is part of the Docker Engine. Scaling, container discovery, and security are all included with minimal setup. [Docker Swarm](https://docs.docker.com/swarm/overview/) is an older standalone product, which used to be used to cluster multiple Docker hosts. Swarm mode is Docker's built-in cluster manager.

Swarm mode uses single-node Docker concepts and extends them to Swarm.For example, to run a Docker cluster, you use the command ` run docker swarm init` to switch to swarm mode. To add more nodes, run `docker swarm join`.

In addition, Docker 1.12 and above and swarm mode include support for rolling updates, Transport Layer Security encryption between nodes, load balancing, and easy service abstraction.

In short, Docker swarm mode spreads a container load across multiple hosts, and it permits you to set up a swarm (that is, a cluster), on multiple host platforms. It also requires you to set up a few things on the host platform, including integration (so containers running on different nodes can communicate with each other) and segregation (to isolate and secure different container workloads). You'll need to work with virtual networks to address those needs.

### Kubernetes

Kubernetes is an open-source container manager that was originally developed at Google. Since Kubernetes rolled out, it’s been ported to Azure, DC/OS, and pretty much every cloud platform you can name. The one exception is [Amazon Web Services](https://aws.amazon.com/) (AWS), although [CoreOS](https://coreos.com/) enables users to deploy a [Kubernetes cluster](https://coreos.com/kubernetes/docs/latest/kubernetes-on-aws.html) on AWS.

Today, Kubernetes is hosted by the [Linux Foundation](https://www.linuxfoundation.org/)‘s [Cloud Native Computing Foundation](https://www.cncf.io/). In addition, there are Kubernetes distributions from numerous companies, including [Red Hat OpenShift](https://www.openshift.com/), the [Canonical Distribution of Kubernetes](https://www.ubuntu.com/cloud/kubernetes), [CoreOS Tectonic](https://tectonic.com/), and [Intel and Mirantis](https://www.mirantis.com/company/press-center/company-news/openstack-kubernetes-mirantis-collaborates-intel-google/).

Kubernetes offers a high degree of interoperability, as well as [self-healing](https://kubernetes.io/docs/user-guide/replication-controller/#what-is-a-replication-controller), [automated rollouts and rollbacks](https://kubernetes.io/docs/user-guide/deployments/#what-is-a-deployment), and [storage orchestration](https://kubernetes.io/docs/user-guide/persistent-volumes/). However, [load balancing is hard](https://techbeacon.com/one-year-using-kubernetes-production-lessons-learned) using Kubernetes. Eventually, Kubernetes [ingress](https://kubernetes.io/docs/user-guide/ingress/) will make it easy to run an external load balancer from inside Kubernetes, but that’s still a work in progress.

Kubernetes excels at automatically fixing problems. But it’s so good at it that containers can crash and be restarted so fast you don’t notice your containers are crashing. To address this, you need to add a centralized logging system.

### Mesosphere Marathon

Marathon is a container orchestration platform for Mesosphere’s [DC/OS](https://mesosphere.com/product/) and [Apache Mesos](https://mesos.apache.org/). DC/OS is a distributed operating system based on the Mesos distributed systems kernel. Mesos, in turn, is an open source cluster management system. Marathon (via its partner program, [Chronos](https://mesos.github.io/chronos/), a fault-tolerant job scheduler) provides management integration between your existing stateful applications and container-based stateless applications.

While Marathon has a user interface that makes you think of it as an application, it may be easier to view it as a framework for managing containers. That touches on the developer side of DevOps, because containers work with Marathon through a [REST API](https://mesosphere.github.io/marathon/docs/rest-api.html).

Marathon boasts many features, including [high availability](https://mesosphere.github.io/marathon/docs/high-availability.html), [service discovery](https://mesosphere.github.io/marathon/docs/service-discovery-load-balancing.html), and load balancing. If you run it on DC/OS, your applications also get virtual IP routing.

However, Marathon can run only on a software stack with Mesos. In addition, certain features (such as authentication) are only available with Marathon on top of DC/OS. This adds one more abstraction layer to your stack.

### Which one is right for you?

Ultimately, it depends on your needs. Mesos and Kubernetes are largely about [running clustered applications](https://stackoverflow.com/questions/27640633/docker-swarm-kubernetes-mesos-core-os-fleet/29017596#29017596). Mesos focuses on generic scheduling and plugging in multiple different schedulers. Google originally designed Kubernetes as an environment for building distributed applications from containers.

Docker swarm mode extends the existing Docker API to make a cluster of machines easier to use with a single Docker API. If your company has Docker professionals on staff, you’re probably already running swarm mode. If it’s working well for you, why bother to switch to another system? Marathon has the unique advantage of giving you one way (albeit a multi-tiered way) to handle both your containers and your older applications.

Fortunately, you can mix and match these programs to create the unique blend your company needs. All three can work well with each other. It’s not easy, but it is doable—and perhaps it’s a good way to explore the options.

### Container Management: Lessons for leaders

- To make the most of containers, you need a good container management program. The three primary applications are Kubernetes, Mesosphere, and Docker Swarm. While their features vary, all support container provisioning, monitoring, and management.
- In addition to container management, Mesosphere has features that help manage data centers.
- Docker Swarm mode aims to simplify Docker clustering by offering control over container scheduling. For instance, it constrains on which nodes a container can start, works with the Docker Remote API, and enables you to decide on which nodes in a cluster new containers should be scheduled.
- Kubernetes has broad industry partnerships, including Intel, Microsoft, Red Hat, and Mirantis.

**Are you looking for a one-stop solution for your Mesosphere environment? See how [combining Mesosphere's DC/OS technology with HPE infrastructure and service leadership](http://h22168.www2.hpe.com/us/en/partners/mesosphere/index.aspx) can leverage hybrid IT to run, deploy and manage distributed enterprise environments more efficiently.**

*Edited to correct definitions.*