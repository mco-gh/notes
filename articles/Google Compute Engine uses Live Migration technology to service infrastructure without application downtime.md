Google Compute Engine uses Live Migration technology to service infrastructure without application downtime

## [Google Compute Engine uses Live Migration technology to service infrastructure without application downtime](https://cloudplatform.googleblog.com/2015/03/Google-Compute-Engine-uses-Live-Migration-technology-to-service-infrastructure-without-application-downtime.html)

Tuesday, March 3, 2015

### **Introduction**

What’s remarkable about April 7th, 2014 isn’t what happened that day. It’s what didn’t.

That was the day the Heartbleed bug was revealed, and people around the globe scrambled to patch their systems against this zero-day issue, which came with already-proven exploits. In other public cloud platforms, customers were impacted by rolling restarts due to a requirement to reboot VMs. At Google, we quickly rolled out the fix to all our servers, including those that host [Google Compute Engine](https://cloud.google.com/compute/). And none of you, our customers, noticed. Here’s why.

We introduced [transparent maintenance](http://googlecloudplatform.blogspot.com/2013/12/google-compute-engine-is-now-generally-available.html) for Google Compute Engine in December 2013, and since then we’ve kept customer VMs up and running as we rolled out software updates, fixed hardware problems, and recovered from some unexpected issues that have arisen. Through a combination of datacenter topology innovations and live migration technology, we now move our customers running VMs out of the way of planned hardware and software maintenance events, so we can keep the infrastructure protected and reliable—without your VMs, applications or workloads noticing that anything happened.

### The Benefits of Transparent Maintenance

Our goal for live migration is to keep hardware and software updated across all our datacenters without restarting customers' VMs. Many of these maintenance events are disruptive. They require us to reboot the host machine, which, in the absence of transparent maintenance, would mean impacting customers’ VMs.

Here are a few of the issues we expected to address with live migration, and we have encountered all of these:

- Regular infrastructure maintenance and upgrades
- Network and power grid maintenance in the data centers
- Bricked memory, disk drives, and machines
- Host OS and BIOS upgrades
- Security-related updates, with the need to respond quickly
- System configuration changes, including changing the size of the host root partition, for storage of the host image and packages

We were pleasantly surprised to discover that live migration helped us deliver a better customer experience in the face of a much broader array of issues. In fact, our Site Reliability Engineers started using migration as a tool even before it was generally enabled; they found they could easily work around or mitigate potential breakages occurring in production.

Here are some of the *unexpected* issues that we encountered and worked around with live migration without impacting the running guests:

- **Flapping network cards** — Network cards were intermittently failing. We were able to repeatedly try the VM migrations and successfully migrate them. This even worked with partially-failing NICs.
- **Cascading battery/power supply issues** — Some overheating batteries were overheating the neighboring machines. We were able to migrate the VMs away before bringing down the machines to swap out their batteries.
- **A buggy update was pushed to production** — We halted the rollout, but not before it reached some of our production machines (it didn't manifest in our canary environment). The buggy software would’ve crashed VMs within a week. Instead, we migrated the VMs on the affected machines to other hosts that didn’t have the buggy software.
- **Unexpected host memory consumption** — One of our backend components consumed more memory than we had allocated and threatened to OOM (out of memory) the VMs. We migrated some VMs away from the over-loaded machines and avoided the OOM failures while patching the backend system to ensure it could not overrun its allocation.

### **Transparent Maintenance in Action**

We’ve done hundreds of thousands of migrations since introducing this functionality. Many VMs have been up since migration was introduced and all of them have been migrated multiple times.

The response from our customers has been very positive. During the early testing for migration, we engaged with Rightscale to see the impact of migrations. After we migrated all their VMs twice, they reported:

> “We took a look at our log files and all the data in the database and we saw…nothing unusual. In other words, if Google hadn’t told us that our instances had been migrated, we would have never known. All our logs and data looked normal, and we saw no changes in the RightScale Cloud Management dashboard to any of our resources, including the zone, instance sizes, and IP addresses.”

We worked with David Mytton at ServerDensity to live migrate a replicated MongoDB deployment. When the migration was done, David tweeted:

> “Just tested > [> @googlecloud](https://twitter.com/googlecloud)>  live migration of a > [> @MongoDB](https://twitter.com/MongoDB)>  replica set - no impact. None of the nodes noticed the primary was moved!”

In fact, Google has performed host kernel upgrades and security patches across its entire fleet without losing a single VM. This is quite a feat, given the number of components involved and factoring in that any one of them or their dependencies can fail or disappear at any point. During the migration, many of the components that comprise the VM (the disks, network, management software and so on) are duplicated on the source and target host machines. If any one of them fail at any point in the migration, either actively (e.g. by crashing) or passively (e.g. by disappearing), we back out of the migration cleanly without affecting the running VM.

### **How it works**

When migrating a running VM from one host to another, you need to move all the state from the source to the destination in a way that is transparent to the guest VM and anyone communicating with it. There are many components involved in making this work seamlessly, but the high-level steps are illustrated here:

[![Screen+Shot+2015-03-03+at+10.32.19+AM.png](../_resources/33e999941b567744c622021ce56f7b2b.png)](https://4.bp.blogspot.com/-l-PqUSyZd3A/VPYuF3vHj-I/AAAAAAAAA6U/jpCy0juePTE/s1600/Screen%2BShot%2B2015-03-03%2Bat%2B10.32.19%2BAM.png)

The process begins with a notification that VMs need to be evicted from their current host machine. The notification might start with a file change (e.g. a release engineer indicating that a new BIOS is available), Hardware Operations scheduling maintenance, an automatic signal from an impending hardware failure etc.

Our cluster management software constantly watches for such events and schedules them based on policies controlling the data centers (e.g. capacity utilization rates) and jobs (e.g. number of VMs for a single customer that could be migrated at once).

Once a VM is selected for migration, we provide a notification to the guest that a migration is [imminent](https://cloud.google.com/compute/docs/metadata#maintenanceevents). After a waiting period, a target host is selected and the host is asked to set up a new, empty “target” VM to receive the migrating “source” VM. Authentication is used to establish a connection between the source and target.

There are three stages involved in the VM’s migration:

1. During pre-migration brownout, the VM is still executing on the source, while most state is sent from the source to the target. For instance, we copy all the guest memory to the target, while tracking the pages that have been re-dirtied on the source. The time spent in pre-migration brownout is a function of the size of the guest memory and the rate at which pages are being dirtied.

2. During blackout, which is a very brief moment when the VM is not running anywhere, it is paused, and all the remaining state required to begin running the VM on the target is sent. We go into blackout when sending state during pre-migration brownout reaches a point of diminishing returns. We use an algorithm that balances numbers of bytes of memory being sent against the rate at which the guest VM is dirtying pages, amongst other things.

3. During post-migration brownout, the VM executes on the target. The source VM is present, and may be providing supporting functionality for the target. For instance, until the network fabric has caught up with the new location of the VM, the source VM provides forwarding services for packets to and from the target VM.

Finally, the migration is complete, and the system deletes the source VM. Customers can see that the migration took place in their [logs](https://cloud.google.com/compute/docs/instances#schedulingoptions).

Our goal for every transparent maintenance event is that not a single VM is killed. In order to meet that bar, we test live migration with a very high level of rigor. We’re using fault-injection to trigger failures at all the interesting points in the migration algorithm. We generate both active and passive failures for each component. At the peak of development testing (for months) we were doing tens of thousands of migrations every day.

Achieving this complex, multi-faceted process requires deep integration throughout the infrastructure and a powerful set of scheduling, orchestration and automation processes.

### **Conclusion**

Live migration technology lets us maintain our infrastructure in top shape without impacting our guest VMs. One of our reviewers even claimed we’ve granted VMs [immortality](http://www.theregister.co.uk/2013/11/14/google_live_vm_migration/). We’re able to keep our VMs running for long periods of time in the face of regular and unplanned maintenance requirements and in spite of the many issues that arise requiring the reboot of physical machines.

We’re fortunate that some of the recent security issues that have affected other cloud providers haven’t affected us, but if and when a new vulnerability affects our stack, we’ll be able to help keep Compute Engine protected without affecting our customers’ VMs.

-Posted by Miche Baker-Harvey, Tech Lead/Manager, VM Migration

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

1 comment

[![photo.jpg.png](../_resources/90dc03288ae5273ac237ce19160eab19.png)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![ic_w_post_gplus_black_24dp.png](../_resources/441cbb7966e7b6b7c013d10a2d98b1b5.png)](https://apis.google.com/u/0/wm/1/101783437495758438809)

### [Sam Damti](https://apis.google.com/u/0/wm/1/101783437495758438809)

[4 months ago](https://apis.google.com/u/0/wm/1/101783437495758438809/posts/bowgSwPZouc)  -  Shared publicly

Live migration sucks! Every time my vm wordpress site gets  "live" migrated, it crashes my site! I get an "error establishing database connection" until I sudo reboot. Last time my website was down for a week before I realized. I can't even get a support ticket because evidently I don't pay enough to warrant ANY "live" support. Way to look out for your customers. Keep your live migration and give me live support when YOU mess up my website for your own maintenance. Good job google.

+
1
2
1

 ·
Reply