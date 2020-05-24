Comparing the speed of VM creation and SSH access of cloud providers

 [**](https://twitter.com/share?text=Comparing%20the%20speed%20of%20VM%20creation%20and%20SSH%20access%20of%20cloud%20providers&url=http://blog.cloud66.com/part-2-comparing-the-speed-of-vm-creation-and-ssh-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-packet-cloud-a-and-microsoft-azure/)  [**](https://www.facebook.com/sharer/sharer.php?u=http://blog.cloud66.com/part-2-comparing-the-speed-of-vm-creation-and-ssh-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-packet-cloud-a-and-microsoft-azure/)  [**](https://news.ycombinator.com/submitlink?t=Comparing%20the%20speed%20of%20VM%20creation%20and%20SSH%20access%20of%20cloud%20providers&u=http://blog.cloud66.com/part-2-comparing-the-speed-of-vm-creation-and-ssh-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-packet-cloud-a-and-microsoft-azure/)  [**](http://www.reddit.com/submit)

 [← All Articles](http://blog.cloud66.com/)

# Comparing the speed of VM creation and SSH access of cloud providers

 ![Kasia Hoffman](../_resources/7e1262ec0783e85b2150e7d69a32a901.jpg)  [Kasia Hoffman](http://blog.cloud66.com/author/kasia/)  07 June 2016

###### Part 2: Benchmarking the performance of AWS, DigitalOcean, Linode, Vexxhost, Google Cloud, Rackspace, Packet, Cloud A and Microsoft Azure.

![](../_resources/96d0bdd4285dd441372d0389d6c20d64.jpg)

This blog post provides updated figures for the data [published in my article last year (Part 1)](http://blog.cloud66.com/ready-steady-go-the-speed-of-vm-creation-and-ssh-key-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-and-microsoft-azure/). For those unfamiliar with the article, the objective of my piece is to measure two processes: the speed of VM creation and the time it takes to access the Secure Shell (SSH) key between Cloud 66 cloud vendors (AWS, DigitalOcean, Linode, Vexxhost, Microsoft Azure, Cloud A, Packet, Rackspace and Google Cloud). Additionally, it reviews both of these processes on a year-on-year basis, as a comparative benchmark report.

The article is based on Cloud 66 internal data collections [via our Birdseye tool](http://blog.cloud66.com/introducing-birdseye-a-public-cloud-dashboard/). The data included in this article was collected between March 2015 and June 2016, compared to my *Part 1* article, where the data included was collected between January 2014 and March 2015.

#### Which cloud vendor posts the quickest performance?

From a speed perspective, the clear leader in creating VM and SSH access is Google Cloud. This provider takes on average 39" seconds to complete both processes. Google Cloud is closely followed by Vexxhost (43"s), Linode (53"s) and AWS (61"s)

The rest of the cloud vendors had slower average results - for example, Cloud A takes 1'04" seconds, DigitalOcean 1'39" seconds, Rackspace 1'49" seconds, and Microsoft Azure takes 2'35" seconds to fire up a box and let you in with SSH. Rounding up the score on the slower end was Packet with 9'51" seconds, noting that they were the only bare metal cloud provider in the mix.

**Note**: *Since the last article about ‘Speed of VM creation and SSH access' Cloud 66 has integrated with new cloud providers: [Cloud A, a Canadian cloud provider](http://blog.cloud66.com/cloud66-clouda-partnership/) and [Packet, who offer bare metal cloud services](http://blog.cloud66.com/cloud66-containers-on-packet-bare-metal-cloud/). Both of these clouds will be included in this article for data capture purposes, but outside the context of providing a year-on-year comparison.*

![](../_resources/e78b4256fcb07684c0b6ca073767ddf6.png)

*Table 1: The X axis represents the time in seconds and Y axis represents the cloud provider.*

The data shows that Google Cloud is more than 4 times faster than Microsoft Azure or Rackspace in completing both processes. Table 1 does not include Packet, as it's a bare-metal only cloud service and therefore naturally has longer processing times than virtual cloud counterparts.

#### What's quicker? Creation of VM or SSH access?

Next, I evaluated the speed of VM creation separately from the time it took for the first SSH access to the server for each cloud vendor.

**First, let’s look at the speed of VM creation**
![](../_resources/685a9748c65ec40e3ee15fa7409a1be9.png)

*Table 2: A snapshot chart for VM creation. The X axis represents the time from March 2015-June 2016 and the Y axis the speed in seconds.*

If we compare the total speed results (the time of creating a VM and the time it takes to grant the first SSH access) with just the speed results of the VM creation alone, we can notice a strong positive correlation. Google Cloud is the fastest and Microsoft Azure is the slowest amongst virtual clouds, followed by bare-metal cloud provider, Packet with 9'50" seconds.

The time of the VM creation amongst virtual clouds varies from 15" seconds to up to 2'35" seconds depending on the cloud vendor. For instance, Google Cloud is 5 times faster than DigitalOcean and 9 times faster than Microsoft Azure in the VM creation process. The top three clouds with the fastest VM creation speed are Google Cloud (15"s), AWS (23"s) and Cloud A (37"s).

**Now let's check the time it takes for the first SSH access**
![](../_resources/5d431496ef58b7de20272e4b3892a3cf.png)

*Table 3: SSH access snapshot. The X axis represents the time from March 2015-June 2016 and the Y axis the speed in seconds.*

It's generally faster to establish the first SSH access than the time it takes to create a VM. Most cloud vendors take under 30" seconds to allow the first SSH access. If we look at Vexxhost for example, it takes 43 seconds to create a VM but only 2" seconds for the first SSH access. This gives Vexxhost an overall speed of 47" seconds, placing them second amongst our cloud providers.

Although Google Cloud and AWS are the speed leaders in VM creation, they're the slowest in granting SSH access for the first time out of all cloud vendors. However, this does not influence the overall result.

Lastly, although Packet takes 9'50" seconds overall, it is the fastest cloud taking only 1 second for SSH access to occur.

#### Does geography matter?

Cloud vendors at Cloud 66 cover different regions in the world, therefore making it difficult to compare them like for like. Therefore, I’ll tackle regional comparisons by reviewing the following geographies: Europe, Asia and Oceania, and the Americas to find out which cloud provider works best in which region.

##### EUROPE

Six out of nine Cloud 66 cloud providers have data centres in Europe, including AWS, Microsoft Azure, Rackspace, Linode, Google Cloud and DigitalOcean.

From all of the Google Cloud regions, the West Europe-1-b region is the fastest, completing the VM creation and SSH access in 30" seconds. This is closely followed by AWS Europe with 59" seconds.

Linode is the fastest cloud vendor in the London region (1'03" seconds). Other alternatives are DigitalOcean (1'17" seconds) and Rackspace (1'52" seconds).

DigitalOcean is present in the Amsterdam region, with the speed of VM creation and SSH access taking anywhere between 1'22" seconds, to up to 1'47" seconds.

Frankfurt was added as a new region by DigitalOcean (1'20" seconds) and Linode (1'50" seconds) at the end of last year. DigitalOcean came up the fastest in the region.

*Note: [Packet just announced a new data centre in Amsterdam.](https://www.packet.net/blog/packet-launches-in-sunnyvale-and-amsterdam/)

##### ASIA AND OCEANIA

Six out of nine Cloud 66 cloud providers have data centres in Asia and Oceania, including AWS, Microsoft Azure, Rackspace, Linode, Google Cloud and DigitalOcean.

Out of all Google Cloud regions, the Asian region has the slowest speed results (between 36" to 46" seconds). Nevertheless, Google Cloud is still a leader in the Asia region.

In Japan, the fastest cloud provider in AWS (Tokyo: 1'01" second), followed by Linode (Tokyo: 1'38" seconds) and Microsoft Azure (2'27" seconds). For Microsoft Azure, Japan is the second fastest region they provide service for.

In Singapore, again AWS is the speed leader with 1'04" seconds, followed by Linode (1'20" seconds) and DigitalOcean (1'29" seconds).

The fastest cloud provider in Australia is AWS (Sydney: 1'04" seconds), then Rackspace (Sydney: 1'51" seconds) and lastly Microsoft Azure with 2 data centres: Australia East (2'27" seconds) and Australia South-East (2'28" seconds).

###### AMERICAS

All nine cloud providers cover the Americas region, with the main focus on US, Canada and a small presence in South America.

**US:**

In the US Central region, Google Cloud is able to create VM and open SSH access from between 31" and 38" seconds, whereas Microsoft Azure is nearly 5 times slower (2'36" seconds).

AWS covers the US East and West regions and completes both processes from between 53" seconds to a minute. The US- East-1-b is the fastest region services by Google Cloud (30" seconds).

DigitalOcean's speed varies from between 1'27" seconds to 2'26" seconds in the New York region. Linode VM creation and SSH access is done in approximately a minute. You can also use bare-metal provider Packet in New York (9'51" seconds).

Rackspace provides the quickest VM creation and SSH access in North Virginia (1'13" seconds), followed by the Chicago region (2'03" seconds), Dallas (2'09" seconds).

**Canada:**

Cloud 66 partners with two Canadian cloud providers Cloud A and Vexxhost. Cloud A takes 1'03" seconds to create VM and SSH access, whereas Vexxhost takes between 45' seconds to a minute. DigitalOcean also has one data center in Toronto that takes 1'35' seconds processing time.

**South America:**

AWS covers the South America East region, where the speed of VM creation and SSH access is 1'01" second.

#### VM creation and SSH access year-on-year comparison

![](../_resources/bd5ea50c151a3180c61f896d2eb6c720.png)

*Table 4: The year-on-year cloud performance comparison. The X axis represents time in seconds, the Y axis represents cloud providers. The light grey bars represent the period from January 2014 - March 2015, and the dark grey bars represent the period from March 2015 - June 2016.*

The rank of cloud providers hasn't changed since last year and Google Cloud is still the fastest and Microsoft Azure is the slowest performance-wise. Interestingly, the majority of cloud providers are slower than the previous year by approximately 15" seconds for Azure, 10" seconds for AWS, DigitalOcean and Google Cloud. Linode and Vexxhost are quicker by up to 5" seconds and there's a significant speed improvement by approximately 20" seconds from Rackspace.

Packet and Cloud A are not included in this table, as they were only added last year, and therefore we don't have data covering the 2014/15 period.

The content of this blog post is based on the Cloud 66 internal data collected via our Birdseye metrics tool. Please feel free to contact us if you have any questions or any additional data which could be added to the data points in this post.

* * *

If you have any questions or any additional data, don't hesitate to [get in touch](http://blog.cloud66.com/part-2-comparing-the-speed-of-vm-creation-and-ssh-access-on-aws-digitalocean-linode-vexxhost-google-cloud-rackspace-packet-cloud-a-and-microsoft-azure/mailto:kasia@cloud66.com).

##### Try Cloud 66 for Free, No credit card required

[Get Started Now](https://app.cloud66.com/users/sign_up?utm_source=blog&utm_medium=navigationbar&utm_campaign=blog-navigation)

[Request a Demo](https://www.cloud66.com/demo-request?utm_source=blog&utm_medium=navigationbar&utm_campaign=blog-navigation)

 [← All Articles](http://blog.cloud66.com/)