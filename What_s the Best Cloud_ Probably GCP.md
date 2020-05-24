What's the Best Cloud? Probably GCP

[‹ Inside Quizlet](https://quizlet.com/blog)

132[Thanks!Don't Move!High Five?](https://quizlet.com/blog/whats-the-best-cloud-probably-gcp/#)

[(L)](https://quizlet.com/blog/whats-the-best-cloud-probably-gcp/#)[(L)](https://quizlet.com/blog/whats-the-best-cloud-probably-gcp/#)

#

What's the Best Cloud? Probably GCP

Engineering · Posted by [Peter](https://quizlet.com/team/peter-bakkum)March 10, 2016

*In 2015 we migrated Quizlet from our legacy host to a large cloud provider. AWS is the default choice for most companies, but after comparing the options, we went with Google Cloud Platform (GCP). This is a summary of our analysis.*

Quizlet is now the [~50th biggest website in the U.S.](https://www.quantcast.com/quizlet.com) in terms of traffic. Our technical infrastructure of 200 cloud machines supports 200,000 transactions a minute on an average day with significant shifts in traffic that depend on the school calendar. All those transactions are students learning on Quizlet and we have a responsibility to make sure that their experience is stable and performant. If Quizlet goes down it's like ripping a textbook out of students' hands in the middle of class, so we make our cloud infrastructure and deployment a top priority. Outside of employee compensation, cloud spend is Quizlet's biggest expense. Even minor tweaks to our infrastructure can cost us tens of thousands of dollars a month.

![image.png.jpeg](../_resources/6576770face08274883250f3296dc62f.jpg)

In early 2015, we realized that the long-term success of our infrastructure required us to move from our existing cloud provider. This presented a somewhat rare opportunity to carefully analyze existing cloud providers and consider how we wanted to run our infrastructure. Anecdotally, very few organizations holistically compare cloud providers.

**What cloud is the best long-term bet for Quizlet?**
We approached this problem in several ways:

- Analyzing the cloud provider market and narrowing our focus to Amazon Web Services and Google Cloud Platform.
- Benchmarking the features we care most about; price and performance for CPU, memory, networking, and disk technology.
- Understanding the long-term trends in the industry and the roadmap and potential of AWS and GCP.
- Modelling our costs on both clouds.

After stepping through the analysis and weighing our options we chose Google Cloud Platform. We believe GCP has better core technology, in particular its networking and disk technology. Additionally, GCP's pricing model is better in almost every respect than AWS's. Though AWS has a much larger user base and ecosystem, we have more confidence in GCP's product roadmap and future potential, given the strength of its existing technology. Ultimately it was difficult to imagine not choosing the platform with the better tech and better pricing, so GCP was the winner.

AWS seems to be the default choice for a lot of customers, but it's still early days for the cloud market. Cloud providers are consolidating into an oligopoly of massively scaled competitors, and Google is one of the few players capable of competing at that level. It's in a unique position of leveraging internal technology to compete with other public clouds, which is just now beginning to bear fruit.

In this post, I'll describe our reasons for moving to a new cloud, our viewpoint on the cloud provider market, and our methodology for comparing AWS and GCP, which is focused on EC2 and GCE, the compute product of both clouds. A public cloud is a complex product; It's difficult to compare them fairly and your case may be different than ours. Regardless, I hope our analysis will be useful in deciding which cloud you run on.

On August 1st, 2015, Quizlet switched over to run completely on GCP. Our cloud is the foundation for our application, and our biggest vendor, so we're heavily incentivized to pick and run on the best available cloud provider. In other words, we bet our future performance and stability when we decided on a cloud, and we picked GCP in a self-interested analysis. Now that we're running on GCP, it's also in our interest for more developers and companies to understand its advantages and use it - hence this post.

## Why would we migrate clouds?

Cloud platforms are sticky by nature and most cloud operators never switch after reaching a certain scale. In the most common case, you write your application on a cloud and then grow up with it. At greater scale it sometimes then makes sense to migrate from the cloud to your own datacenter. Running your entire operation in the cloud and then switching to a different one is painful, doesn't immediately improve your product, and you need to believe you'll get a big win to make it worth it.

From 2007 to 2015 Quizlet ran on Joyent, a cloud platform built on SmartOS, which is a Solaris fork (Joyent also offers Linux hosting). Joyent has a strong engineering team, and SmartOS is ahead of its time in many ways. Joyent also provided us with the best support you could hope for in a cloud platform.

Why would we switch from a cloud with great technology and support to something unknown?

- We need a Linux-first cloud. In the past 10 years, Linux has devastatingly won as the server OS, so much so that a lot of software is now targeted specifically at Linux, with “Unix” as an afterthought. There was overhead for us in running on a non-standard platform - several services we run needed to be tweaked specifically for SmartOS, and some applications wouldn't compile.
- Our thesis on cloud providers is: the market will consolidate to a few massively-scaled participants. Quizlet's traffic has grown at least 50% a year for the past 7 years. If this trend continues then our cloud footprint will inevitably scale up as well. It's imperative that Quizlet run on one of the massively-scaled winners of the market.

Our next step was to to evaluate the cloud provider landscape and decide on the best cloud from which to operate Quizlet.

## The Cloud Provider Landscape

AWS sits comfortably within “no one ever got fired for picking” territory in the public cloud market. But it's still early days in that space, and there are a number of smaller players and recent entrants hoping to gain market share. Who will win the market? There are two keys to competing as a public cloud: technology and scale.

The scale at which modern cloud platforms can operate has increased tremendously, and drives the economics of the business. If you run a large platform it's obvious that the cost of providing a CPU resource can be brought down by buying and operating in bulk. This will be the most important factor in shaking out the cloud provider marketplace since there's a positive feedback loop of greater scale enabling lower prices. Cloud instance prices appear to decline exponentially - the observed trend is 13% year over year since 2007. If you can't match the scale of your competitors, then your margin will effectively be pushed into negative territory. Thus, there will be an oligopoly of public cloud providers that operate at massive scale and the smaller competitors will die off or become irrelevant.

[AWS Revenue Growth](../_resources/5e80e4a7bd6077e1799d8e666300f964.webp)

*AWS revenue growth, driven by growth in the cloud market, demonstrates the future potential of the market. [Source](http://www.nextplatform.com/2016/02/01/how-long-can-aws-keep-climbing-its-steep-growth-curve/)*

There exists some threshold of infrastructure size at which it makes sense for a company to buy its own hardware, and another break point at which owning entire data centers makes sense. These thresholds rise as the costs of cloud hosting decrease, and there's been a corresponding shift of customers into the cloud (AWS is growing 40-50% year-over-year). At this point in 2016, if you don't have any specialized requirements, there are very few cases where it makes sense not to run a new tech business in the cloud.

New technology has also played a role in the public cloud pricing trend. CPUs have continued to roughly obey Moore's law, and we've seen continued increases in disk density plus the switch from traditional magnetic hard drives to SSDs. The upshot being that performance relative to price for CPU and disk resources continues to climb. The next couple steps of this are already visible - we're about to get Skylake processors and widespread access to non-volatile memory devices.

Up to now, cloud providers have had access to most of the same hardware, but competitors will inevitably begin to compete more on the proprietary technology they offer. The largest cloud providers now order customized Intel CPUs, for example. Application-level services offered to cloud customers have become differentiators as well; BigQuery has shown that deep database expertise can be leveraged into a compelling public cloud product.

[Cloud Price Decline](../_resources/96fa0357cb70f68bebcbf7cabe325b07.webp)

*The price of running a single standard cloud compute core has declined significantly since first introduced. These machines guarantee the user a single cloud CPU with 3.75 GB of memory. The last 3 years have seen GCP's entry into the market. AWS 3-year Reserved Instances remain the cheapest, but are a very restrictive model and involve a large upfront payment. Arguably reserving an instance for 3 years negates many of the benefits of using the cloud at all. [Data](https://docs.google.com/spreadsheets/d/1C25QpfCrf_NRIQa6ubQkg_Ry_NLewWdW-jLjah2TdIY)*

As the market consolidates on participants with the best technology who reach massive scale, the winners will emerge. This will likely be AWS, Azure, and GCP in the U.S. and Europe, with Asia split between them and whoever wins China, currently led by Alibaba. For technology businesses which require competitive pricing, platform sophistication, and the possibility of reaching scale, you will choose among these options.

I'd place enterprise/consulting focused clouds like IBM and Oracle in a different category - their customer acquisition is very different than public clouds like AWS, though it's clear IBM is attempting to shift towards that category. Oracle, in particular, seems to have only a very loose concept of what “Cloud” means. There will also be niche players such as DigitalOcean who thrive by reaching scale in a different market. For DigitalOcean, this appears to be hobbyist developers.

The cloud vendor market is consolidating, but the mechanism is that a few vendors are getting very big, while the others are static or shrinking. If you operate a small cloud, then you're competing in a market where your competitors are able to consistently drop prices 13% every year, which is brutal. For example, Rackspace appears to be struggling to compete with higher-scale competitors. It's doubtful there will be many acquisitions of full-stack public clouds, since the underlying technology between platforms is so different; Rackspace has twice looked at selling themselves to no avail.

To state all of this more abstractly - most of the computer processing that we as humans perform will be done in one of several very very large computers optimized for energy and cost (cloud providers). The computers outside of that domain, such as in mobile devices, will be much smaller and optimized very differently. This is an exaggeration, but it's useful to understand direction of the market.

## Cloud Technology Trends

Cloud computing platforms have many well-defined concepts they share. A compute node, for example. Likewise, these companies have been subject to the same hardware landscape, and thus share much of their hardware stack in common, like Intel CPUs. To differentiate themselves and gain a competitive advantage, vendors will compete more on technology, and in fact this is well underway. Here's where we see the next few rounds of technological competition taking us.

**Trend 1: Cloud vendor/customer interaction is moving to higher-level interfaces.**

Amazon in particular has added a number of products that implement interfaces higher up the stack than a vanilla EC2 instance. For example, Amazon's Relational Data Store (RDS) replaces a database that a cloud operator might otherwise need to run on his/her own. Rather than an OS-level interface (Linux), the developer is interacting with the cloud at an application-level interface (MySQL wire protocol). AWS Lambda is another example of this. This will continue happening.

Application-level cloud services tend to be take-it-or-leave-it; if they work for you, then they save development and maintenance time, but the tradeoff is less control over your infrastructure. For example, there are fewer configuration and optimization possibilities if you're running MySQL RDS versus running MySQL yourself. If RDS works for you, that's great, otherwise you manage MySQL on your own. Every higher-level service offered by cloud vendors implies this tradeoff, as does using a cloud at all.

As these services mature and optimize for greater scale in the normal case, the services fit a wider array of client use-cases and tuning for your own application is less important. In several years time there will be very few reasons not to use a hosted database service, even for very high throughput use-cases. This means cloud customers will spend less time interacting with OS-level interfaces and more time with application-level interfaces. The role of the infrastructure engineer can effectively be automated.

**Trend 2: Cloud vendor infrastructure / hardware behind client-facing interfaces will become increasingly specialized in proprietary ways.**

If your clients are interacting with an up-the-stack interface like the MySQL wire protocol, they effectively care only about the SLA of that interface, rather than the infrastructure behind it. This means the service can be optimized specifically for that SLA, from the software down to the hardware layer. Thus, cloud vendors will compete on completely proprietary technology behind the client-facing layer of the platform. We've already seen several cases of this:

- Amazon EC2 C4 (Amazon's Haswell-generation package) instances use proprietary CPUs, customized by Intel specifically for AWS. I suspect Google has a similar deal. [Source](https://aws.amazon.com/blogs/aws/new-c4-instances/)
- Amazon Glacier uses a proprietary storage technology to provide very low-cost storage with an SLA that access may take several hours. It's been widely speculated what sort of technology powers it - basically no one knows for sure how it works. Google's Nearline storage has a similar SLA and pricing structure, and is also proprietary. [Source](http://www.itproportal.com/2013/11/09/one-of-techs-most-elusive-mysteries-the-secret-of-amazon-glacier/)
- Google's software-defined networking platform, called Jupiter, is completely proprietary and though some details have been published, no other vendor has access to it. Users interact with it through a configuration API that exposes firewall rules and network routes. This is notable because of how much Google has invested in its networking technology - it uses custom hardware switches, for example. [Source](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p183.pdf)

There's no reason this trend will stop - cloud vendors can compete on price and performance, privately optimizing their entire stack, and the scale of operating tens of millions of machines and service instances will magnify the cost benefits of such optimization. This trend means that we're possibly a few years away from much of the computing that we do as software developers being on proprietary and to-some-degree secret hardware.

**Trend 3: Cloud virtualization will move down the stack.**

The most common interface through which developers interact now with cloud resources is the Linux OS. If you believe that cloud vendors are incentivized to optimize everything behind client-facing interfaces then it's likely we'll also start to see OS-level virtualization, rather than Xen or KVM. This optimization applies to both higher-level (application) interfaces, and an OS-level interface. Stick with me on this one.

The low-hanging fruit here is that cloud host machines are running an average of 2+ Linux kernels. Let's say that number is *k*. If you're the CTO of AWS you can run a calculation that you operate a total number of *kn* kernels, where *n* is the total number of machines you operate (in the millions or tens of millions for the largest platforms). If you think about the total energy cost of running this many kernels plus the virtualization overhead in the *entire* cloud, it's staggering. You probably then say “KVM/Xen virtualization costs us [huge number] gigawatt-hours per month, we should optimize this.”

There is a dual win in moving from KVM or Xen-type virtualization to kernel-level virtualization - you run fewer kernels and there is less overhead between the clients and hardware. In fact, containerization is already an increasingly popular Linux feature, and an interface like Docker that would play well in this world. The problem is that Linux containers lack the durability necessary for multi-tenant operation in the cloud, where your co-tenant could be a malicious actor.

Thus, AWS or GCP will develop a proprietary durable kernel-level virtualization technology which can be run at lower-cost than more traditional cloud virtualization. In fact, Joyent has already operated this kind of technology in the cloud for years, using SmartOS rather than Linux. Kernel-virtualization will mean that clients will operate containers rather than virtual machines, and container packaging will be important.

At some point one of these platforms is going to really and truly drop the containerization hammer. EC2 / GCE deployment at that point will look different than now, but it will probably dovetail with existing containerization technology. Until that point using containers in a public cloud arguably doesn't carry much benefit.

--

The cloud market is still relatively young. The current landscape of providers, with Azure and GCP only recently becoming serious competitors, means that platform technology development is far from over, even for basic features like compute virtualization technology. Choosing a cloud in this environment means thinking about who has the capacity to build the best technology in the long-term.

# Picking Among the Options

Quizlet's footprint is large enough that it was worth it to perform a real investigation of the public cloud options (AWS, GCP, Azure). I suspect relatively few organizations actually do a serious evaluation of cloud vendors and there doesn't seem to be much publicly available information comparing clouds. This is partly because switching clouds is so painful once you reach scale, and partly because it's only recently that Azure and GCP could even be considered viable AWS competitors. For companies that have grown up in the cloud and are happy with their current vendor, the costs versus benefits of migrating are usually prohibitive. It would be surprising if Netflix ever leaves AWS.

We initially narrowed down our evaluation to AWS and GCP. AWS is the default, Azure was eliminated since it's a Linux-second cloud and we don't use any other Microsoft products, and GCP was included as a good second option. Our take on IBM is that some of the Softlayer options are interesting, but overall the cloud hasn't reached the sophistication of the others, and will likely always be targeted towards enterprise IBM customers.

## Evaluating GCP

In the mid-2000s both Amazon and Google released cloud hosting services. While Amazon gave developers OS-level access with EC2, Google chose to present an application-level interface with App Engine. Google's decision may have been prescient given the up-the-stack direction of things in general, but proved too restrictive to be useful for most developers. It was the wrong bet.

AWS experienced massive growth through the rest of the 2000s, while Google lacked a comparable product. In the early 2010s this began to change. Google Cloud Platform started out as a division of App Engine, offering Google Compute Engine, an EC2 competitor. Then App Engine and the newly formed Google Cloud Platform organizations eventually switched places in the corporate hierarchy, with App Engine now being considered a division GCP.

Google now has a suite of products very comparable to whats available on Amazon. Here's a comparison of the wording on similar platform features between the two clouds:

| AWS (Amazon Web Services) | GCP (Google Cloud Platform) |
| --- | --- |
| EC2 (Elastic Compute Cloud) | GCE (Google Compute Engine) |
| SQS (Simple Queue Service) | Cloud Pub/Sub |
| Redshift | BigQuery |
| S3 (Simple Storage Service) | GCS (Google Cloud Storage) |
| DynamoDB | Cloud Datastore / BigTable |
| RDS (Relational Database Service) / Aurora | Cloud SQL |

The reason it is able to compete in the cloud marketplace is that Google has run at massive scale for its own operations for over a decade and has developed strong proprietary technology that it can now leverage for the public cloud. Operating an internal infrastructure is obviously different than operating a cloud, but this infrastructure means Google has a strong tailwind as it deploys cloud products. For example, Google probably has the best network (both internal and CDN) in the world, developed for its own operations, and now useful for routing cloud traffic. BigQuery is another example; it's a sophisticated analytical database used internally by Google, then deployed for public consumption.

If there will be an oligopoly of cloud vendors, then Google is one of the few companies with the scale and resources to legitimately compete. Even with an existing massive infrastructure, this is still an expensive market to compete in, and part of using GCP is convincing yourself that Google will invest 5+ years in really entering the market. We believe this to be true, given their investments in GCP engineering and leadership. Google Cloud CTO Urs Hölzle has said publicly that “One day, this could be bigger than ads. Certainly, in terms of market potential, it is.” Diane Greene now leads the division that includes GCP - from our perspective it’s nice to know that the cloud division has a seat on the Google Board of Directors.

## Dimensions of Comparison

As noted above, AWS and GCP offer a number of comparable peripheral features. S3 and GCS are effectively the same product, as are SQS and Cloud Pub/Sub. Amazon RDS and Aurora are more advanced than Google Cloud SQL - but after testing we realized we'd need to manage our MySQL databases ourselves anyway. It became clear that the compute product (EC2/GCE) was the most important element of both products to us, since managing compute VMs is the biggest component in our infrastructure engineering time and overall cloud expenditure. So we focused most on comparing EC2 and GCE and sliced our comparison into the dimensions we cared most about; we narrowed down to the bread-and-butter platform features, like CPU, network speed, disk throughput, and how much these things cost.

It's tough to fairly compare these things. Some of our measures are fairly simplistic - our intent was to poke at many factors of both platforms and get a sense of all of them. I'm including them to explain how we decided on GCP as our cloud, rather than as a definitive reference of cross-cloud performance. A cloud platform is a complex product, and if you're deciding among clouds I'd encourage you to test these for yourself. Note these tests were conducted in January and February 2015, but pricing has updated.

**CPU**

CPU performance is basically identical between AWS and GCP. The biggest factor in performance is which processor generation you're running. At the time I'm writing this, both platforms are switching their machines from the Ivy Bridge generation to Haswell. AWS does this by releasing a new machine package - in this case all the machine types prefixed with a 4, such as c4.large, are Haswell-generation. GCP upgrades processor generation on the zone level, so certain zones in the us-central-1 region are Haswell.

Both platforms employ virtualization technology that imposes overhead on CPU-intensive operations. During testing, we couldn't tell much difference in the effective performance, so our conclusion is that it's not worth thinking about.

It's worth noting that GCP is more extreme in the resources you get for compute-optimized instances. The 4-core AWS compute optimized option, a c4.xlarge, gives you 7.5 GB memory. The equivalent GCP package, the n1-highcpu-4, only has 3.6 GB of memory, and is priced about 32% cheaper.

[CPU Performance Normalized by Price](../_resources/c8217ade5a384747c7a569c0751f9d3e.webp)

GCP offers the cheaper option for raw CPU performance. The x-axis is a simple benchmark of hashes generated per second. Processors on AWS and GCP perform about the same, so GCP's advantage in this space is a function of its pricing model. You see higher CPU capacity relative to price on GCP, in both normal and CPU-optimized instances.

The numbers above were calculated with the following benchmark: `openssl speed -multi 24 blowfish`. This counts how many hashes of varying sizes can be calculated in a given time period. Though thats oversimplifying the problem somewhat, I like this approach because it's transparent and easy, and we've observed that it's strongly correlated with our actual application performance.

**Memory**

Like CPU, memory performance is equivalent on both platforms, so any advantage is in pricing model.

[MB per Annualized Dollar](../_resources/a1bec16787d5de897bc30628f8142ae3.webp)

Optimizing on memory, AWS has an advantage in terms of capacity relative to price. Chalk this up to particularly aggressive pricing on the r3 package, their memory-optimized option.

**Networking**

The real highlight of GCP is the networking technology, which is similar to Amazon's VPC but much higher capacity for many machine types. Amazon optimizes certain machine types for 10 Gbit networking and provides very little in the way of documentation for networking capacity on their other instances. Google's documentation, on the other hand, explains that a node is allocated 2 Gbit/s per CPU core up to 10 Gbits/s, so that an n1-standard-4 machines has a ceiling of 8 Gbit/s.

Both platforms let you run a vLAN with your own local address space and cap out at 10 Gbit/s for networking throughput for a single node. In practice, however, we observe much better networking performance for most of our machines on GCP.

[Intra-zone Observed Bandwidth](../_resources/b59a1e0f5427d86f79695d5c2bc0cc2a.webp)

GCP does roughly 7x better for the comparison of 4-core machines, but for the largest machine sizes networking performance is roughly equivalent. This chart shows our observed results on an iperf performance test between nodes of the same type and same zone in AWS (with the appropriate network driver) and GCP. For this mid-size machine type we also observed much faster external-file transfer speeds.

For some infrastructures, networking performance for machines of this size might not make as much difference. Quizlet runs a number of mid-size machines with significant network traffic, so for us it's very useful to have higher capacity without running oversized machines. For example, our load balancers don't have any CPU-intensive operations to perform but have significant network throughput, so GCP's network capacity allows us to run a smaller instance size and save money. Amazon's standard response on this question is that if you're concerned about networking performance then you should be using larger instance types.

Here's some magic:

	$ traceroute google.com
	traceroute to google.com (74.125.193.139), 30 hops max, 60 byte packets
	1 ig-in-f139.1e100.net (74.125.193.139) 0.865 ms 0.847 ms 0.838 ms

Software-defined networking means that google.com appears to be one hop away, which probably isn't physically true.

Google probably has the best networking technology on the planet. The internally-developed Jupiter Stack is exposed to public cloud customers through the cloud API, which we found simpler and more powerful than AWS's VPC configuration. VPC permissions to enable one machine access to another, for example, are notoriously tedious to manipulate.

Another useful feature for us is that Google peers its egress traffic directly with Cloudflare, which Quizlet uses for CDN and DDoS protection. The peering deal has performance benefits and has significantly decreased the cost of our traffic egress.

**Disk Performance**

Disks are complex to compare directly, because the platforms offer such different options - but we prefer the GCP ones. Here's a comparison of the theoretical disk limits described for both platforms, considering only SSDs.

| Technology | Size (GB) | R throughput<br>(MB/s) | W throughput<br>(MB/s) | R IOPS | W IOPS | Price / Month |
| --- | --- | --- | --- | --- | --- | --- |
| **GCP** |
| SSD | 750 | 240 | 240 | 15,000 | 15,000 | $128 |
| Local SSD SCSI | 750 | 780 | 548 | 200,025 | 140,025 | $164 |
| Local SSD NVMe | 750 | 1328 | 705 | 339,975 | 180,000 | $164 |
| **AWS** |
| SSD | 750 | 160 | 160 | 2,250 | 2,250 | $90 |
| Provisioned IOPS | 750 | 320 | 320 | 15,000 | 15,000 | $1038 |
| i2.xlarge | 800 |     |     | 35,000 | 35,000 | $624 |

I've assumed 15,000 IOPS for the provisioned IOPS drive, which could go up to 20,000. Note also that the AWS vanilla SSDs can burst up to 3,000 additional IOPS. The i2.xlarge type above is a machine package, meaning it's price includes the entire machine cost, not just the disk cost. We spent time benchmarking magnetic and SSD drives on both platforms and found that the performance was in line with the published numbers. We haven't benchmarked Local SSDs.

On GCP you pay slightly more for the vanilla SSD, but get far superior performance. Running a high-throughput database on AWS inevitably means a Provisioned IOPS drive or an optimized instance type, which drives the cost up. Comparing GCP's SSDs with AWS Provisioned IOPS yields a surprising price difference.

GCP also offers Local SSD storage, which gives you the option to trade durability for power. These drives risk data loss if there is a problem on the instance, unlike the other SSD options. AWS i2 machines are optimized for disk throughput, but use ephemeral drives, meaning they also lack durability. AWS has other machine types optimized for workloads like sequential reading (useful for Hadoop jobs), that may improve the overall price you would pay for your application.

The price/performance ratio of disks has a significant effect on our overall cloud spend. Our primary data store is comprised of 8 large MySQL machines serving several terabytes of production data. At any given time, we also run around 14 machines with high-throughput disk caches serving static assets. Given the data above, it's clear why we prefer Google disk technology.

**Disk Snapshotting**

One other difference we noticed when examining disk performance was the speed of disk snapshotting on GCP. This feature copies a full copy of a disk at a moment in time, shipping it elsewhere for storage. It is particularly useful for backing up data, since it's a fairly lightweight operation. Both platforms enable SSD disk snapshots through their API and web console.

We tested snapshotting with 400 GB SSD drives given 300 GB of random data. On AWS, we observed snapshot times around 8 hours, while on GCP the same operation takes about 6 minutes. I'll spare you the chart. This is, like, a lot different. I asked a very patient intern to test this until we could figure out what we were doing wrong on AWS. It appears this is really a difference in core disk technology; GCP's disks are much better at snapshotting.

Snapshotting is a pretty minor dimension in the overall cloud platform comparison but we're happy to have it as a feature, and it's enabled a much simpler architecture for our MySQL backups.

**Default Images**

Early in our process of picking a cloud, we made the decision to run CentOS 7 as our Linux distribution. We assumed running the distribution of our choice would be a solved problem on both platforms, but we ended up preferring GCE's system for packaging distributions. While AWS officially supports only its own Amazon Linux AMI and relies on community distributions for other flavors, Google made the decision to officially support a number of these themselves, including CentOS, Ubuntu, and CoreOS. We now run a recent CentOS 7 image configured by Google.

Having officially supported images is nicer than you might think. Amazon Linux AMI comes preinstalled with the ixgbe network drivers, for example, which are required for optimal networking performance on AWS. The problem is that Amazon Linux AMI is a fork of CentOS 6, which is the only official option and is beginning to show its age - many newer packages are harder to install on it, and it uses Upstart to manage processes. Community images have filled the gap for newer distributions, but these aren't managed as well as an Amazon-managed version might be. For example, the community-managed CentOS 7 package wasn't yet available to run on Amazon's c4 package when we were testing it. You can always generate your own custom images, of course, but Google makes it painless to press a button and get the distribution you want. What it comes down to is - do you think you'll have fewer problems building your own Linux image, or using one configured and optimized by the cloud platform provider?

**Live Migration**

Another key difference between EC2 and GCE is how they manage platform-level upgrades, such as improvements to the virtualization technology. While Amazon attempts to keep things as static as possible, Google has architected its cloud with the assumption it will be constantly making updates and upgrades. Doing this smoothly means that GCE needs the capability to transparently move a running VM between hardware nodes, a technology called live migration. This is somewhat mind boggling - it means moving running machine state, such as live memory pages and network connections, to a new host machine. The VM continues executing during this operation, except for a brief blackout period.

This is important for several reasons. On EC2, if a node has a hardware problem, it will likely mean that you'll need to restart your virtual machine. On GCE, if a hardware problem is detected early enough, the platform will attempt to migrate your virtual machine to a new node without requiring any action from the customer, and without interrupting applications that are running on it. On EC2, if the virtualization technology needs to be updated, it will likely require a machine restart. There was a bad case of this in September 2014, when a bug was found in the Xen Virtualization technology used on EC2, which meant customers had to reboot a large number of EC2 VMs by a deadline. This kind of reboot storm basically isn't necessary on GCE.

--

Our conclusion from comparing EC2 and GCE on technology was that networking and disk performance are better on GCP, and the other factors are pretty similar. We believe this is a reflection of Google's cloud development model. Most of GCP's technology was developed internally and has high standards of reliability and performance. It means that creating corresponding cloud products is a matter of exposing internal tools, rather than developing completely new ones. The outcome of that process seems to be that the user gets better performance.

**Pricing**
The GCP pricing model is much, much better than AWS.

The AWS and GCP sticker prices are pretty similar. Both platforms offer an hourly price for instances and a long-term discount option. On AWS you get a discount by buying Reserved Instances, which gives you a ~35-45% discount for purchasing instances with a 1 or 3 year lock-in. On GCP you get a similar discount (to 1-year reserved instances) with Sustained-use Pricing, which lowers prices on the margin the longer you run a node. The difference here is the GCP discount is automatic, while the AWS discount requires a decision to commit to running a node for some time period, plus an up-front payment.

We modelled our annual cloud spend on both platforms for several years into the future. After planning the ~200 instances we would run on each cloud and factoring in the above price discounts, plus our spend on network egress, disk allocations, support pricing, and the amount these would increase based on our traffic predictions, the final estimates were within 10% of one another (GCP was cheaper).

This comparison examined GCP's sustained pricing models against AWS 1-year Reserved Instances. It's difficult to factor in all of the elements of a cloud into the pricing model - for example it's hard to say how much less we spend because we get better networking on mid-size GCP machines. The pricing on these two clouds is similar enough that price comparisons assuming 100% reserved instances with these parameters are basically a wash.

[Sustained use pricing curve](../_resources/818e0e6fe31369c055cce7982dc721b4.webp)

*This shows the GCE sustained use pricing curve. Note that the discount is automatic. [Source](https://cloud.google.com/compute/pricing)*

This estimate, however, doesn't really reflect real-world spend - it's virtually impossible to run reserved instances for 100% of your infrastructure. It's hard to quantify this, but I would guess that most companies operating on AWS reserve only reserve 50-80% of their instances. Buying a reserve involves a decision to commit to run a certain node type for at least a year, along with an upfront payment ($10,000+ for larger types), which means that it's a finance optimization and probably doesn't happen every day. So if you're running on AWS, you probably spend a lot on On-Demand instances even though there are large discounts to be had, which can add up to a difference of tens or hundreds of thousands of dollars. On GCP this is automatic.

It's hard to overemphasize how much friendlier GCP pricing is, and how poorly the AWS model works. Amazon's rhetoric for why you should run cloud vs self-hosted infrastructure is the additional agility you get; You can elastically spin up and shut down capacity whenever you want. Reserved Instance pricing effectively negates this advantage, and running all your instances On-Demand is extremely expensive in comparison. So you're left with the decision to over-spend or lock yourself in. In practice, you'll probably run some machines reserved and some on-demand. [1](https://quizlet.com/blog/whats-the-best-cloud-probably-gcp/#footnote1)

In summary - despite the similar list prices, you would likely spend significantly less on a GCP infrastructure than a comparable AWS infrastructure.

**Community and Momentum**

By far the most significant advantage of Amazon is that it has the biggest base of users. This helps in a lot of ways:

- The sheer quantity of online content associated with platform; When you have a problem you can probably punch the issue into Google and see a Stack Overflow discussion or read a blog post about it.
- 3rd-party vendors deploy their products to the most popular cloud first. This means that some services may be unavailable, or less well maintained.
- New hires are more likely to be familiar with AWS than any other platform.

How important is it to be on the most popular cloud? Part of the decision is weighing this factor against others. Another factor is gauging what the community will look like in the future.

Though it's currently less feature-rich than AWS, Google has rapidly deployed new GCP features over the past few years and now has pace on releasing new products. Given its cadence, plus our (limited) understanding of its roadmap, we think GCP will grow more compelling relative to its competitors as time goes on. There are still many proprietary Google technologies that have yet to be productized for public consumption.

## Final Decision

Everyone involved unanimously picked GCP. It came down to this: we believe the core technology is better.

Though it has fewer users and services than AWS, we realized that bread and butter platform technology / performance is more important and we felt more confident in Google's core compute instance, networking, and disk technology. As a bonus: GCP's pricing is strictly better than AWS. It's certainly a bet to run our infrastructure on the less popular cloud, but it's hard to imagine performing our analysis and then not choosing the best technology and pricing.

Given the technology and pricing on GCP, we expect its growth will accelerate, and it will acquire both individual developers and enterprise customers. Will it ever be bigger than AWS? Perhaps not, but our thesis is the overall market will be dominated by several huge clouds, and GCP will be one of them.

## Switching Over

We switched Quizlet's infrastructure to run on GCP on 8/1/2015, before our back to school rush of traffic. Switching over to GCP was a large project which we'll cover in detail in a forthcoming blog post. Overall it was a smooth transition and we're very glad that we picked GCP as our provider - we've received excellent support and scaled up our deployment with few incidents. We're also looking forward to several unreleased GCP features that will arrive soon.

Of the issues we've had with GCP, these are the ones worth mentioning:

- The account security model isn't as sophisticated yet as that on AWS. For example, many permissions are assigned on the machine level. This is a clunky system, because permissions there aren't very granular, and they can't be added or revoked after a machine is created. I suspect that we'll see a number of changes to this in the future.
- Past live migrations have caused application disruptions on a few of our instances that intensively use a lot of memory, such as our MySQL and Memcached VMs. Google has been continually optimizing the live migration technology and we've seen this issue mostly disappear.

It's a short list, and we're glad we switched to GCP.
[Quizlet All-time Traffic](../_resources/11e00a2d360414369f798047074ae089.webp)

*This chart shows our weekly unique visitors since 2007. We'll continue scaling up our infrastructure as our traffic increases. [Source](https://www.quantcast.com/quizlet.com)*

If the cloud market is still in a period of rapid expansion, and Google is one of a few companies able to compete at scale, and GCP is built on a substrate of superior technology, then our conclusion is that it will gain market-share and mind-share. We'll see small companies that start out on GCP grow into larger customers, and we'll see large customers switch onto it. If you're involved in one of those decision points, it's in your interest to evaluate the options for yourself.

Ultimately it was a bet to move Quizlet to GCP - a significant one, given how deeply our product depends on cloud infrastructure. Switching over was a time consuming and complex process, but was the right decision for our business. We made that bet based on our belief in its core technology. The engineers who work on GCP also believe in its technology and we expect that Google will continue putting huge amounts of investment in its cloud infrastructure, as it always has. As a GCP product manager explained to us, “Ferraris aren't cheap.” Whether you believe in GCP's technology or not, I think it's certainly worth evaluating if you're picking a cloud.

**Footnotes**

[1](): I would speculate that AWS uses its Reserved Instance pricing model for several reasons: upfront payments, stickiness, capacity planning.

- Amazon gets an upfront cash payment for a reserved instance which it can invest immediately in its own business. That's a nice funding model.
- Reserved Instances effectively lock customers in for some time period. You're much less likely to switch clouds if you've already payed for instances for a 3 year timeframe.
- RIs help with AWS capacity planning, since AWS knows for sure that a certain percentage of its capacity will be used stretching into the future. The tradeoff is they'll give you a discount if you can help them plan for the future. Google doesn't have that advantage, but I suspect gets around this by performing a simple statistical calculation based on the age of the instances running in its cloud. If a machine has been running for 2 years, for example, it's very likely to be running for at least another month. Google also runs very significant capacity for its own private infrastructure, which means that capacity planning for their cloud business could be less important than for Amazon.

None of the logic behind Reserved Instances, other than the price, helps you as a customer.