How to make a self-destructing VM on Google Cloud Platform

# How to make a self-destructing VM on Google Cloud Platform

## Save money by launching compute instances with preset lifespans.

[![1*-21kGHhpo4t41Oo1yX3CEA.png](../_resources/864ee82937b5a9d9cfce08dc004e051d.png) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='96' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@davidstanke?source=post_header_lockup)

[Dave Stanke](https://medium.com/@davidstanke)
Feb 20·2 min read

A great thing about the cloud is that it’s super easy to spin up new virtual machines (VMs). A less-great thing is that it’s also super easy to *forget* about all those machines you spun up, and find yourself paying for things you don’t really need. In this post, I’ll show how to use [Google Compute Engine](https://cloud.google.com/compute/) (GCE) to make VMs (also called “instances” in GCE) that delete themselves after a specified period of time, so you can fire them up, and forget about them.

![](../_resources/edbf727a1332ec8eee62d474b319fd65.png)![1*cmfBgwed3-6FwXY3hDKwpg@2x.png](../_resources/e98d77ccd466e002f932b5e215e8c594.png)

### How it works

This technique makes use of GCE’s [Startup Script](https://cloud.google.com/compute/docs/startupscript) feature: when creating an instance, we provide a **startup script** in the `metadata-from-file` argument. As soon as the instance finishes booting, it executes the script, which begins the countdown to deletion. To achieve that, the script schedules a task using the linux `at` command: at the scheduled time, that task will instruct the GCE API to delete its host instance.

For additional flexibility, we can pass the self-destruct interval as a variable at instance creation time. This allows different lifespans for different purposes. We’ll use a GCE [custom metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom) field: when each instance is created, a field named `SELF_DESTRUCT_INTERVAL_MINUTES` is set on that instance. At startup, the instance will request its specified interval from the GCE metadata server, and will schedule its self-destruction accordingly.

### Try it out

In [**this GitHub repo**](https://github.com/davidstanke/samples/tree/master/self-destructing-vm), you‘ll find the [startup script](https://github.com/davidstanke/samples/blob/master/self-destructing-vm/self-destruct.sh), and a sample `gcloud` command to create a self-destructing instance. Here’s a portion of the command, with the tasty bits in bold:

gcloud compute instances create \
self-destructing-vm \
[...] \
** --metadata SELF_DESTRUCT_INTERVAL_MINUTES=2 \
--metadata-from-file startup-script=self-destruct.sh**

You can modify the instance name and zone to suit your needs. This command has been tested on Ubuntu 16.04 and 18.04, and will probably work with other Linux distros. (A similar technique can likely be used to make self-deleting Windows instances.)

### But *WHY IN THE WORLD *would I do that?!?

Because it’s fun! Like blowing bubbles and watching them pop. But also: sometimes we need assurance that resources we provision will be deprovisioned — so they don’t hang around forever, costing money. Perhaps, for Continuous Integration: as part of a CI pipeline, we can create a one-time-use environment and run tests against it. If the pipeline fails (as pipelines do), we know the environment will be automatically deleted in a reasonable timeframe.

*In an upcoming post, I’ll describe just that: a CI pipeline that uses self-destructing VMs as dedicated, ephemeral test environments. Check back soon!*