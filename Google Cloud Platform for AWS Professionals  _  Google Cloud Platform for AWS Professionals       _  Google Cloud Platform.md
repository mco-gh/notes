Google Cloud Platform for AWS Professionals  |  Google Cloud Platform for AWS Professionals       |  Google Cloud Platform

star_border
star_border
star_border
star_border
star_border

- [Documentation](https://cloud.google.com/docs/)

- chevron_right

 [Google Cloud Platform for AWS Professionals](https://cloud.google.com/docs/compare/aws)

#  Google Cloud Platform for AWS Professionals

*Updated June 29, 2016*

This guide is designed to equip professionals who are familiar with Amazon Web Services (AWS) with the key concepts required to get started with Google Cloud Platform. The guide compares Cloud Platform with AWS and highlights the similarities and differences between the two. In addition, the guide provides quick-reference mappings of AWS products, concepts, and terminology to the corresponding products, concepts, and terminology on Cloud Platform.

star**Note:** This guide doesn’t attempt to compare the syntax and semantics of the SDK, APIs, or command-line tools provided by AWS and Cloud Platform.

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)Why Google Cloud Platform?

For the past 15 years, Google has been building one of the fastest, most powerful, and highest-quality cloud infrastructures on the planet. Internally, Google uses this infrastructure for several high-traffic and global-scale services, including[Gmail](https://mail.google.com/),[Maps](https://www.google.com/maps),[YouTube](https://www.youtube.com/), and[Search](https://www.google.com/). Because of the size and scale of these services, Google has put a lot of work into optimizing its infrastructure and creating a suite of tools and services to manage it effectively. Google Cloud Platform puts this infrastructure and these management resources at your fingertips.

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)Regions and zones

Nearly all AWS products are deployed within **regions** located around the world. Each region comprises a group of data centers that are in relatively close proximity to each other. Amazon divides each region into two or more **availability zones**. Similarly, Cloud Platform divides its service availability into regions and zones that are located around the world. For a full mapping of Cloud Platform's global regions and zones, see [Cloud Locations](https://cloud.google.com/about/locations).

In addition, some Cloud Platform services are located at a multi-regional level rather than the more granular regional or zonal levels. These services include Google App Engine and Google Cloud Storage. Currently, the available multi-regional locations are United States, Europe, and Asia.

By design, each AWS region is isolated and independent from other AWS regions. This design helps ensure that the availability of one region doesn’t affect the availability of other regions, and that services within regions remain independent of each other. Similarly, Cloud Platform's regions are isolated from each other for availability reasons. However, Cloud Platform has built-in functionality that enables regions to synchronize data across regions according to the needs of a given Cloud Platform service.

AWS and Cloud Platform both have points of presence (POPs) located in many more locations around the world. These POP locations help cache content closer to end users. However, each platform uses their respective POP locations in different ways:

- AWS uses POPs to provide a content delivery network (CDN) service, Amazon CloudFront.
- Cloud Platform uses POPs to provide [Google Cloud CDN](https://cloud.google.com/cdn/) and to deliver built-in edge caching for services such as App Engine and Cloud Storage.

Cloud Platform's POPs connect to data centers through Google-owned fiber. This unimpeded connection means that Cloud-Platform-based applications have fast, reliable access to all of the services on Cloud Platform.

To summarize, AWS's location terms and concepts map to those of Cloud Platform as follows:

| Concept | AWS term | Google Cloud Platform term |
| --- | --- | --- |
| Cluster of data centers and services | Region | Region |
| Abstracted data center | Availability Zone | Zone |
| Edge caching | POP (just CloudFront) | POP (multiple services) |

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)Accounts, limits, and pricing

To use an AWS service, you must sign up for an AWS account. After you have completed this process, you can launch any service under your account within Amazon's stated limits, and these services are billed to your specific account. If needed, you can create billing accounts, and then create sub-accounts that roll up to them. In this way, organizations can emulate a standard organizational billing structure.

Similarly, Cloud Platform requires you to set up a Google account to use its services. However, Cloud Platform groups your service usage by[project](https://cloud.google.com/docs/overview/#projects) rather than by account. In this model, you can create multiple, wholly separate projects under the same account. In an organizational setting, this model can be advantageous, allowing you to create project spaces for separate divisions or groups within your company. This model can also be useful for testing purposes: once you're done with a project, you can delete the project, and all of the resources created by that project will be deleted as well.

AWS and Cloud Platform both have default *soft limits* on their services for new accounts. These soft limits are not tied to technical limitations for a given service—instead, they are in place to help prevent fraudulent accounts from using excessive resources, and to limit risk for new users, keeping them from spending more than intended as they explore the platform. If you find that your application has outgrown these limits, AWS and Cloud Platform provide straightforward ways to get in touch with the appropriate internal teams to raise the limits on their services.

Because pricing tends to change more often than core features or services, this set of articles will avoid pricing specifics where possible. However, each article will discuss the pricing model behind each service wherever helpful. For up-to-date price comparisons for your specific solution, use the[Amazon pricing calculator](https://calculator.s3.amazonaws.com/index.html)and [Cloud Platform calculator](https://cloud.google.com/products/calculator/) to see which configuration provides the best value in terms of flexibility, scalability, and cost.

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)Resource management interfaces

AWS and Cloud Platform each provide a command-line interface (CLI) for interacting with the services and resources. AWS provides the[Amazon CLI](https://aws.amazon.com/cli/), and Cloud Platform provides the [Cloud SDK](https://cloud.google.com/sdk/). Each is a unified CLI for all services, and each is cross-platform, with binaries available for Windows, Linux, and Mac OS X. In addition, in Cloud Platform, you can use the Cloud SDK in your web browser by using[Google Cloud Shell](https://cloud.google.com/shell/docs/).

AWS and Google Cloud Platform also provide web-based consoles. Each console allows users to create, manage, and monitor their resources. The console for Google Cloud Platform is located athttps://console.cloud.google.com/.

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)Service types

At a high level, cloud platforms begin by providing a set of baseline services: compute, storage, networking, and database services. AWS's baseline services include:

- *Compute*: Amazon Elastic Compute Cloud (EC2)
- *Storage*: Amazon Simple Storage Service (S3) and Amazon Elastic Block Store (EBS)
- *Networking*: Amazon Virtual Private Cloud (VPC)
- *Databases*: Amazon Relational Database Service (RDS) and Amazon DynamoDB

Cloud Platform's baseline services include:

- *Compute*: Google Compute Engine and Google App Engine
- *Storage*: Google Cloud Storage
- *Networking*: Google Cloud DNS and Google Cloud Interconnect
- *Databases*: Google Cloud SQL, Google Cloud Datastore, and Google Cloud Bigtable

Each platform then builds other higher-level services on top of these services. Typically, these higher-level services can be categorized as one of three types:

- *Application services*: Services designed to help optimize applications in the cloud. Examples include Amazon SNS and Google Cloud Pub/Sub.
- *Big data and analytics services*: Services designed to help process large amounts of data, such as Amazon Kinesis and Google Cloud Dataflow.
- *Management services*: Services designed to help you track the performance of an application. Examples include Amazon's CloudWatch and Google's Stackdriver Monitoring.

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)Service comparison

The following table provides a side-by-side comparison of the various services available on AWS and Cloud Platform.

| Service Category | Service | AWS | Google Cloud Platform |
| --- | --- | --- | --- |
| Compute | IaaS | Amazon Elastic Compute Cloud | [Google Compute Engine](https://cloud.google.com/compute/) |
|     | PaaS | AWS Elastic Beanstalk | [Google App Engine](https://cloud.google.com/appengine/) |
|     | Containers | Amazon Elastic Compute Cloud Container Service | [Google Container Engine](https://cloud.google.com/container-engine/) |
| Network | Load Balancer | Elastic Load Balancer | [Google Cloud Load Balancing](https://cloud.google.com/load-balancing/) |
|     | Peering | Direct Connect | [Google Cloud Interconnect](https://cloud.google.com/interconnect/) |
|     | DNS | Amazon Route 53 | [Google Cloud DNS](https://cloud.google.com/dns/) |
| Storage | Object Storage | Amazon Simple Storage Service | [Google Cloud Storage](https://cloud.google.com/storage/) |
|     | Block Storage | Amazon Elastic Block Store | [Google Compute Engine Persistent Disks](https://cloud.google.com/compute/docs/disks/persistent-disks) |
|     | Cold Storage | Amazon Glacier | [Google Cloud Storage Nearline](https://cloud.google.com/storage-nearline/) |
|     | File Storage | Amazon Elastic File System | [ZFS / Avere](http://www.averesystems.com/google-cloud-platform) |
| Database | RDBMS | Amazon Relational Database Service | [Google Cloud SQL](https://cloud.google.com/sql/) |
|     | NoSQL: Key-value | Amazon DynamoDB | [Google Cloud Datastore](https://cloud.google.com/datastore/), [Google Cloud Bigtable](https://cloud.google.com/bigtable/) |
|     | NoSQL: Indexed | Amazon SimpleDB | [Google Cloud Datastore](https://cloud.google.com/datastore/) |
| Big Data & Analytics | Batch Data Processing | Amazon Elastic MapReduce | [Google Cloud Dataproc](https://cloud.google.com/dataproc/), [Google Cloud Dataflow](https://cloud.google.com/dataflow/) |
|     | Stream Data Processing | Amazon Kinesis | [Google Cloud Dataflow](https://cloud.google.com/dataflow/) |
|     | Stream Data Ingest | Amazon Kinesis | [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) |
|     | Analytics | Amazon Redshift | [Google BigQuery](https://cloud.google.com/bigquery/) |
| Application Services | Messaging | Amazon Simple Notification Service | [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) |
| Management Services | Monitoring | Amazon CloudWatch | [Stackdriver Monitoring](https://cloud.google.com/monitoring/) |
|     | Deployment | AWS CloudFormation | [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager/) |

## [arrow_upward](https://cloud.google.com/docs/compare/aws/#top_of_page)What's next?

Check out the Google Cloud Platform for AWS Professionals articles for each service type:

- [Big Data](https://cloud.google.com/docs/compare/aws/big-data)
- [Compute](https://cloud.google.com/docs/compare/aws/compute)
- [Networking](https://cloud.google.com/docs/compare/aws/networking)
- [Storage](https://cloud.google.com/docs/compare/aws/storage)
- [Management](https://cloud.google.com/docs/compare/aws/management)
- [Application Services](https://cloud.google.com/docs/compare/aws/application-services)

Was this page helpful? Let us know how we did:
star_border
star_border
star_border
star_border
star_border

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.