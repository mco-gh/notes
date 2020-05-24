If You K8s, Please Try K9s… – Fernand Galiana – Medium

# If You K8s, Please Try K9s…

[![0*33OYX_TlQnHK_iaG.](../_resources/f52c4f95cbc2fddd03af3dae56db768d.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='70' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@fernand.galiana?source=post_header_lockup)

[Fernand Galiana](https://medium.com/@fernand.galiana)
Feb 2·2 min read

![](../_resources/2f3411e782eadb8cfd3386b9f3b8849d.png)![1*onX5uHAXqiwZS_kDozQm9Q.png](../_resources/3a460d4aec2f20555fb9ec0e5e3ea26d.png)

K9s Kubernetes CLI To Manage Your Clusters In Style!

Let’s face it, Kubernetes and its surrounding ecosystem is getting more and more complicated to operate. There are a multitude of tools one must wrangle to manage clusters. When I am working on a cluster, I need the ability to watch the various Kubernetes resources that I employ, dig into configuration, settings, as well as track down issues when things don’t quite go as expected. This flow typically entails aliasing overused commands, installing/operating single purpose CLI tools and custom bash scripts to keep some sanity, not say somewhat healthy wrists...

I know this technic is becoming controversial, but I typically develop code locally and against my local minikube instance and dockerize last. I usually don’t need the entire application deployed on my cluster to work on any given service. I find honing my code along with my configurations and resources manifests to be a continuum and not separate activities. Thus, my daily Kubernetes routine is to fire up one or more terminal windows, broken into various tabs/panes with a few watch commands monitoring the resources *du jour *along with open CLIs to issue kubectl and build commands.

One day, I was contemplating this brainwashed flow and realized it would be cool to have a simple CLI utility to watch K8s resources, switch between them, checkout manifests, logs, monitor events and exec into pods and hence eliminate most of my real estate sucking terminal panes…

And so, I wrote a tool about it ! It’s called [**K9s**](https://k9ss.io/)**  **and does just that.

![](../_resources/646d4f2cd8deb9b2c6c266558348e68d.png)![1*767GcXLX7n8oaKpfA_pWTQ.png](../_resources/75f6dfa2e3fc68be25608402d3614556.png)

K9s Pod View

This terminal based UI, monitors Kubernetes resources on a given interval (default 2s) and allows me to see what’s up with my clusters. I can quickly navigate between development and production clusters using **ctx<enter>** command. The CLI allows me to filter out by namespace and perform read only operations on most Kubernetes resources (still work in progress…). If I get stuck **?<enter>** list out all supported resources.

Of course, I find it useful and would like to share it with you and see what you think… Here is the link to the [repo](https://github.com/derailed/k9s) and install instructions.

Thank you for your time!