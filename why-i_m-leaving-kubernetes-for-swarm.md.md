why-i'm-leaving-kubernetes-for-swarm.md

 [Raw](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647/raw/618a92c5d1a6973d0592e72997691adde37c50d6/why-i'm-leaving-kubernetes-for-swarm.md)

       [**why-i'm-leaving-kubernetes-for-swarm.md**Permalink](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#file-why-i-m-leaving-kubernetes-for-swarm-md)

I have been an aggressive Kubernetes evangelist over the last few years. It has been the hammer with which I have approached almost all my deployments, and the one tool I have mentioned (shoved down clients throats) in almost all my foremost communications with clients, and it was my go to choice when I was mocking my first startup (saharacluster.com).

A few weeks ago Docker 1.13 was released and I was tasked with replicating a client's Kubernetes deployment on Swarm, more specifically testing running compose on Swarm.

And it was a dream!

All our apps were already dockerised and all I had to do was make a few modificatons to an existing compose file that I had used for testing before prior said deployment on Kubernetes.

And, with the ease with which I was able to expose our endpoints, manage volumes, handle networking, deploy and tear down the setup. I in all honesty see no reason to not use Swarm. No mission-critical feature, or incredibly convenient really nice to have feature in Kubernetes that I'm going to miss; except perhaps the Kube admin dashboard, and heapster but even those have ready replacements. Weave scope for Kube admin (admittedly not as pretty) and I could easily setup my own ELK to monitor my containers.

The moment it dawned on me how simple swarm was, was when I realised that all I had to do to expose an nginx service publicly was to publish the ports in my compose file. It hit me again when I attempted to create a number of replicas for the nginx service fully expecting to run into this Kubernetes like error [Pod Deploy - Failed to fit in any node - PodFitsHostPorts](https://github.com/openshift/origin/issues/) that has frustrated me before, but no. It worked! It just worked! And to boot Docker intelligently loadbalanced the requests from all my nodes (nginx was accessible from all the node ips in the Swarm at port 80/443) to the various containers in the service.

Anyone who has used Kubernetes on any long-term large-scale project knows what a pain this is. If you're not on AWS or GCE and can't create a Loadbalancer service, where Kubernetes will provision an elastic ip address for your service (which you have to pay for), and you're not okay with having to access your service on a weird random port between default:30000-32767, then you have to deal with the fickle beast that is Kubernetes Ingresses. To elaborate on how many steps it takes to come close to replicating what I had achieved on Swarm with three lines in my compose file.

You'd have to do the following on Kubernetes
1) Create the ingress controller

2) Work on your Kubernetes yaml spec and define an ingress resource jumping around from the various documentation sources online

3) A bit of trial and error here to get to where you can create your ingress without error

4) Realising that to use paths i.e. example.com/path you have to create a "path" directory in the friggin /usr/share/nginx/html in the nginx container

Full docs here [Kubernetes Ingresses](https://kubernetes.io/docs/user-guide/ingress/s)

In short, exposing services to the outside world in Kubernetes is a pain! While with Docker however all it takes is

	normalservices:
	  nginx:
	    ports:

	      - "80:80"
	      - "443:443"

	    ...
	normal

And it works! It just works!
**How to use volumes in Swarm**

	normalversion: '3'
	volumes:
	  poc:
	services:
	  redis:
	    volumes:

	      - poc:/redis

	normal

**How to use volumes in Kubernetes :(**

1) Create the pv [sample](https://gist.github.com/jonathan-kosgei/4b53a26cb4918d9069aed52f10419a74)

2) Create the pvc [sample](https://gist.github.com/jonathan-kosgei/92efd04157533702c7d2ca718177e52f)

3) Create the deployment specifying your pvc [sadness sample](https://gist.github.com/jonathan-kosgei/603df37a60b09a3e308bf498ae484511)

**Configs**

I am incredibly appreciative of how easily I can eyeball my entire deployment in Swarm, ports, volumes, services, dependencies, images etc etc as all the config is in one docker-compose.yml file of reasonable length as opposed to the countless files covering everything from pvs, pvcs, deployments, statefulsets etc in Kubernetes. You can define everything in one file in Kubernetes but it won't do much for readability.

[Think how many lines you need to pore through to get to the container image you're using]

**Deploying and cleaning up**

You have to run ` kubectl create -f ` more than once. You know it. I know it. (Unless of course you put everything into one file and trade your readability for convenience).

With compose on Swarm however, all you have to do is:` docker stack deploy --compose-file=docker-compose.yml <stack-name> `You could delete your app's entire namespace in Kubernetes to cleanup, but what if that's not you want? Or you didn't have the foresight to deploy your app in a separate namespace? You'd again have to run a number of ` kubectl delete -f ` commands to delete everything. You could run ` kubectl delete -f ` on a single directory with all your app's kube config files in there. You could do that. Or you could use Swarm and be able to,` docker stack rm <stack-name> `And have a life.

**BONUS:**
**Pure Docker goodness**

It is beyond satisying to use Docker and only Docker. To spin up a fresh vm and install Docker and only Docker. And be able to do everything you need. I have spent countless hours writing salt files and ansible playbooks to automate installing Kubernetes. You could use kargo, or kops, but all I have to do to start a Swarm cluster is install Docker and run ` docker Swarm init `. What more could anyone want!

**What Kubernetes could do:**

Humans should not have to write/read config files. If there was a way I could easily deploy a Kubernetes cluster (Hint: Make up-to-date repositories for your software available from the distros repos), and not have to write any configs, that would be great.

 [![@ecliptik](../_resources/f3df9f0d7a3327fac1e47adf855d245f.jpg)](https://gist.github.com/ecliptik)

 **  [ecliptik](https://gist.github.com/ecliptik)  ** commented [21 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2009432)

Have you looked at [Rancher](http://rancher.com/)? It uses [object Object] as the base for it's Cattle orchestration, and adds in a few additions, but the syntax is the same.

I also support k8s orchestration, and spins all the supporting services up without having to write any configs.

The UI and API is nice too.

 [![@jonathan-kosgei](../_resources/803bb72216bbac408f865feace3b5ae6.jpg)](https://gist.github.com/jonathan-kosgei)

  Owner This user is the owner of the gist.

 **  [jonathan-kosgei](https://gist.github.com/jonathan-kosgei)  ** commented [20 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2010787) •  edited jonathan-kosgei edited this comment 20 days ago

|     |
| --- |
| [@ecliptik](https://github.com/ecliptik) admittedly I haven't, though there's a lot of buzz around it. Sounds like an interesting solution, to be able to use docker-compose syntax on kubernetes. There's also kompose https://kubernetes.io/docs/tools/kompose/ which is pretty much what its name implies. |

 [![@ErickStaal](../_resources/903c53f74be790154bebb18734c67ed6.png)](https://gist.github.com/ErickStaal)

 **  [ErickStaal](https://gist.github.com/ErickStaal)  ** commented [18 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2011557)

|     |
| --- |
| Kubernetes, Swarm, etc. are just tools to attain a business goal. However, whatever Docker Inc. does with Swarm, many people will stay with Kubernetes:<br>1. No vendor lock-in. (i.e. support for rkt, etc. available for k8s). Only docker, docker, docker is bad for the container ecosystem. Vendor independent orchestration is the way forward.<br>2. K8s has very good admin tools, which is very important to businesses.<br>3. Also k8s has strong developments around serverless (e.g. fission) and orchestrating vm's. How's Docker Swarm doing here?<br>Swarm looks to me a quite nice tool for everyone who only lives in Dockerland. When one's world is wider, Kubernetes remains for now the way to go. |

 [![@mynameiswhm](../_resources/5fe34b8476292dbaac53aea44fc65cff.png)](https://gist.github.com/mynameiswhm)

 **  [mynameiswhm](https://gist.github.com/mynameiswhm)  ** commented [18 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2012465)

> You have to run [object Object]>  more than once. You know it. I know it.
[object Object]

 [![@puja108](../_resources/67473b0be25f55e260038fe7296fcb55.jpg)](https://gist.github.com/puja108)

 **  [puja108](https://gist.github.com/puja108)  ** commented [17 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2013310)

|     |
| --- |
| Most of what you mention is on the operations side of things. If you get Kubernetes managed and Ingress Controller and Storage Classes have been set up for you, all that is left is managing the admittedly huge amount of YAMLs and all the boilerplate that comes with them. There's kompose (mentioned above) that is being worked on more recently, and that basically does what you want above. I know there's also other efforts by various people in the community to make deployment definitions easier.<br>Generally, I agree though that UX is bad in Kubernetes, there's a general lack of "making it easy for the user" and also lots of confusion around where to find the fitting documentation (e.g. with an NGINX Ingress Controller you have to look at 3 different places and at the right commits for your deployed release to find the right flags you can set). It seems there never was a focus on this. It's something we as a community need to work on more.<br>What I fear with Docker Swarm is on the one side the lock-in and with that being helplessly exposed to any decision Docker will make in the future, be that what you need or not. On the other side it's also that Kubernetes has a reason for its complexity and the power it gives you with things like being able to have all kinds of other services (e.g. headless) make it able to cope with lots of strange use cases that are out of the ordinary. |

 [![@srgrn](../_resources/e0ab4ee1b4899f69cbe59a821c62419d.png)](https://gist.github.com/srgrn)

 **  [srgrn](https://gist.github.com/srgrn)  ** commented [11 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2018933)

|     |
| --- |
| Well, I have a quick question, how did you made the volumes work for you?<br>I have rebuilt the development environment i use and i have the latest docker engine and compose however it keeps saying that volumes are not supported in swarmmode, and it is similar to what the docs are specifying. |

 [![@parity3](../_resources/e044c5751396396db92d3a4bae4de52a.png)](https://gist.github.com/parity3)

 **  [parity3](https://gist.github.com/parity3)  ** commented [8 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2021671)

|     |
| --- |
| The drawbacks of vendor lock-in are reduced when the vendor is providing the service to you both for free, and open-source. There is the reasoning that the vendor's agenda can influence the swarm project's direction to sway you toward using Docker Enterprise.. but as soon as swarm becomes less usable as a free service, people will be able to run their containers just fine on rancher/kube/etc without much headache? The idea is to engineer your applications/platform so that it keeps all of its abstractions at the docker container level (at least the ones that can exist there) instead of higher up; then you won't be locked in by swarm or any other container-management-management system. To sum up, I suspect that for many situations what kube/rancher/others excel at, are either not being used correctly or not needed at all for many app platforms/companies. I would guess that a lot of that differentiation comes from the apparent need for massive horizontal scaling performance (I mean, it's so cool to be a big boy right?) but that is really a think-about-later task vs other more immediately pressing needs/benefits docker can fulfill like team collaboration/versioning/deployment/security/automation/devops/redundancy/failure tolerance/dependency separation/etc... |

 [![@ncresswell](../_resources/a05297010c82897751fc4c812ff6d876.jpg)](https://gist.github.com/ncresswell)

 **  [ncresswell](https://gist.github.com/ncresswell)  ** commented [8 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2021750)

|     |
| --- |
| Have you tried Portainer.io as a front end UI for Swarmmode? Makes swarm insanely easy to use.. |

 [![@aofry](../_resources/0a24f2b6f074a9ff085cae15da3db78c.png)](https://gist.github.com/aofry)

 **  [aofry](https://gist.github.com/aofry)  ** commented [8 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2022464)

|     |
| --- |
| I never got compose. Its nice for dev & POC but when you get to micro services describing your full system in one file with the load balancer configuration is just a big pile.<br>In my point of view, Docker guys are building the tooling for Dev and Google and K8S guys are building the tooling for ops (or production mindset) first. |

 [![@rajcheval](../_resources/3ae19ebd139940ef9b49de109fb4e55d.jpg)](https://gist.github.com/rajcheval)

 **  [rajcheval](https://gist.github.com/rajcheval)  ** commented [7 days ago](https://gist.github.com/jonathan-kosgei/dac620fed9d9aeec35050bcc0a146647#gistcomment-2023146)

|     |
| --- |
| Docker swarm is easy to get started with. Trouble starts when you are performance testing a solution that leverages routing mesh and networking. We were running in to issues related to routing mesh. These issues appear in 15 minute load tests with 50 concurrent users. Upgrade to the latest version of Swarm Docker version 17.03 as it resolved many issues for us. |

 [![@marcacohen](../_resources/c3a2ffa44015d8c7503ed773b9db1ffe.jpg)](https://gist.github.com/marcacohen)

  Attach files by dragging & dropping, selecting them, or pasting from the clipboard.

 [ Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/)