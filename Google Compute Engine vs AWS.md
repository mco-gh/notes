Google Compute Engine vs AWS

### Google Compute Engine vs AWS

I've been using AWS to build full stack application hosting solutions for a while now.  I've picked up a couple of AWS certifications along the way.  My typical solutions use VPC (with VPN), EC2, EBS, S3, CloudFormation to build a complete solution for a customer.

As with most things, price matters.  It is a big factor for me as my customers are very cost conscious. AWS and Google have similar pricing at this point.  Since I spent all of the up front time automating around AWS, I need a pretty compelling reason to move to or start using Google Compute Engine.  I imagine many are in the same boat.

However, if I were starting fresh without any investments to worry about (my time), I would seriously consider Google Compute Engine vs AWS.  I'm considering moving workloads.

Here's are comparisons of comparable AWS and GCP services, where Google has a leg up - based off of the latest Google Cloud Next '17 announcements:

## Committed Use Discounts vs. AWS Reserved Instances

Committed Use Discounts let you buy blocks of CPU and Memory up front for 1 or 3 years.  That committed use purchase is subtracted from whatever your actual usage is for the month.  You don't have to pre-determine the instance size/type which is so much more flexible than what you would do at AWS.  If you have a solution that requires 16 vCPUs across 8 instances, you just buy 16 vCPUs and then deploy your instances.  If you need to resize some servers, you aren't stuck trying to figure out what you can translate a m4.large and a c4.xlarge to.  Why can Google do this?  My assumption is that there is no "ECU" equivalent with Google Compute Engine.  A vCPU is a vCPU is a vCPU.  At AWS, a m4 vCPU is not the same as a c4 vCPU or a t2 vCPU.  Now, I tend to use t2 instances quite a bit and can leverage those low cst instances.

## Cross-region Networking

At AWS, a VPC is limited to a region and each subnet is locked down to a certain AZ.  At Google, a network ("VPC") is global.  Subnets are at the region level.  This allows you to build a global architecture very easily without having to figure out VPNs between regions.

## Geo-Redundant Volume Snapshots

At AWS, you have to automate copying volume snapshots between regions.  At Google, they are managed at the global level.  Now, I have not yet found specific language that says that snapshots are replicated between regions but I assume they are.  A Google volume snapshot costs the same as Geo-Redundant object storage ($0.026/GB) so that might be the evidence we need to say with confidence that these snapshots are replicated across regions.

This is the language from the GCP docs:

"Compute Engine stores multiple copies of each snapshot redundantly across multiple locations with automatic checksums to ensure the integrity of your data. You cannot share snapshots across projects."

https://cloud.google.com/compute/docs/disks/create-snapshots

## Geo-Redundant S3

This is a pretty hot topic right now based on the latest AWS S3 outage in us-east-1.  If you had your bucket at Google and they had a regional outage, would you have gone down?  Based on their description of the geo-redundant storage class, nope.

 "Multi-Regional Storage is *geo-redundant*, which means Cloud Storage stores your data redundantly in at least two regions separated by at least 100 miles within the multi-regional location of the bucket. This ensures maximum availability of your data, even in the event of large-scale disruptions, such as natural disasters. In order to provide geo-redundancy, Cloud Storage utilizes multiple Google data centers within a given multi-regional location"

- Price per GB @ AWS: $.023 (Single Region)
- Price per GB @ GCP: $.026 (Geo-Redundant)

All Google Cloud Storage has 99.999999999% durability.
https://cloud.google.com/storage/docs/storage-classes

You can accomplish the equivalent high availability with AWS S3 using CloudFront+Route53. But, it isn't something you can get out of the "box".

## Dealing with Hardware Failures - GCP vs AWS

Google Compute Engine can live-migrate your instances across servers without having to shut down. How many notices have you received from AWS saying that your instance is on degraded hardware and you need to shut it down and power it back up to move to different hardware?  Unless a server spontaneously fails, hardware monitors preemptively move your instances to healthy servers without any downtime.

Posted byUnknownat[Sunday, March 12, 2017](http://www.brianbeaulieu.com/2017/03/google-compute-engine-review.html)

[Email This](https://www.blogger.com/share-post.g?blogID=5393535928086230051&postID=4716710264108887936&target=email)[BlogThis!](https://www.blogger.com/share-post.g?blogID=5393535928086230051&postID=4716710264108887936&target=blog)[Share to Twitter](https://www.blogger.com/share-post.g?blogID=5393535928086230051&postID=4716710264108887936&target=twitter)[Share to Facebook](https://www.blogger.com/share-post.g?blogID=5393535928086230051&postID=4716710264108887936&target=facebook)[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=5393535928086230051&postID=4716710264108887936&target=pinterest)

|     |
| --- |
| Recommend this on Google |

Labels:[Cloud](http://www.brianbeaulieu.com/search/label/Cloud)