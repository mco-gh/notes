What is Google’s Cloud Platform? – Reto Meier – Medium

# What is Google’s Cloud Platform?

## Described without… help from marketing

Sadly, the Wikipedia entry for GCP is garbage, and while the official docs are pretty good, the marketing-dust sprinkled on them gives me a toothache.

As part of my re-self-introduction to Google’s Cloud Platform, I wrote an objective summary of GCP for my own reference. I have a conflict of interest, so I can’t fix the Wikipedia entry, but I *can* share what I wrote, so here it is.

* * *

*...*

### Google’s Cloud Platform

[Google Cloud Platform](https://cloud.google.com/) (GCP) is a collection of Google’s computing resources, made available via [services](https://medium.com/@retomeier/what-are-the-google-cloud-platform-services-285f1988957a) to the general public as a *public cloud* offering.

The GCP resources consist of physical hardware infrastructure — computers, hard disk drives, solid state drives, and networking — contained within [Google’s globally distributed data centers](https://en.wikipedia.org/wiki/Google_Data_Centers), where any of the components are custom designed using patterns similar to those available in the [Open Compute Project](https://techcrunch.com/2016/03/09/google-joins-the-open-compute-project/).

This hardware is made available to customers in the form of [virtualized](https://en.wikipedia.org/wiki/Virtualization) resources, such as [virtual machines](https://en.wikipedia.org/wiki/Virtual_machine) (VMs), as an alternative to customers building and maintaining their own physical infrastructure.

As a public cloud offering, software and hardware products are provided as integrated services that provide access to the underlying resources. GCP offers over 50 services including Infrastructure as a Service ([IaaS](https://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29)), Platform as a Service ([PaaS](https://en.wikipedia.org/wiki/Cloud_computing#Platform_as_a_service_.28PaaS.29)), and Software as a Service ([SaaS](https://en.wikipedia.org/wiki/Cloud_computing#Software_as_a_service_.28SaaS.29)) offerings in the categories of Compute, Storage & Databases, Networking, Big Data, Machine Learning, Identity & Security, and Management & Developer tools.

These services can be used independently or in combination for developers and IT professionals to construct their own, custom cloud-based infrastructure.

GCP is hosted on the same underlying infrastructure that Google uses internally for end-user products including Google Search and YouTube.

#### Regional Service Architecture

Each of Google Cloud Platform’s services and resources can be zonal, regional, or managed by Google across multiple regions.

![](../_resources/d6bab6f52efb11e5edf38377adf5cb3f.png)

A zone is a deployment area for resources within a region. Zones are isolated from each other to prevent outages from spreading between them, so each zones is considered a single [failure domain](https://en.wikipedia.org/wiki/Failure_domain) within a region.

Zonal resources operate within a single zone; if a zone becomes unavailable all of its resources are unavailable until service is restored. Regional resources are deployed with redundancy across zones within a region. Multi-regional services ([Google App Engine](https://en.wikipedia.org/wiki/Google_App_Engine), [Google Datastore](https://en.wikipedia.org/wiki/Google_Cloud_Datastore), [Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Storage), [Google BigQuery](https://en.wikipedia.org/wiki/BigQuery)) are managed by Google to be redundant and distributed within and across regions.

All GCP service instances are configured such that [maintenance events](https://cloud.google.com/compute/docs/regions-zones/regions-zones#maintenance) are transparent to applications and workloads via live migration. Live migration moves running virtual machine instances [out of the way of maintenance](http://www.rightscale.com/blog/cloud-industry-insights/google-compute-engine-live-migration-passes-test) that is being performed.

GCP services are [available](https://cloud.google.com/about/locations/) in 18 zones in 6 regions: Oregon, Iowa, South Carolina, Belgium, Taiwan, and Tokyo[¹](https://techcrunch.com/2016/11/08/konnichiwa-google-cloud-platform/).

In 2016, Google [announced](http://www.theregister.co.uk/2016/09/30/google_announces_eight_new_cloud_regions_new_support_model/) plans to make 22 zones and 8 new regions available in 2017: Sydney, Sao Paulo, Frankfurt, Mumbai, Singapore, London, Finland, and Northern Virginia.

Within each region, traffic tends to have round-trip network latencies of under 5ms on the 95th percentile.

> Note that like everything I publish on Medium, these are my views on GCP, and may not represent the opinions of my employer.

* * *

*...*
> Something missing or wrong? Add a comment!

#### Further Reading

- •[What are the Google Cloud Platform Services?](https://medium.com/@retomeier/what-are-the-google-cloud-platform-services-285f1988957a)
- •[An Annotated History of Google’s Cloud Platform](https://medium.com/@retomeier/an-annotated-history-of-the-google-cloud-platform-90b90f948920)