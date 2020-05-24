Map AWS services to Google Cloud Platform products  |  Google Cloud Platform Free Tier       |  Google Cloud Platform

star_border
star_border
star_border
star_border
star_border

- [Google Cloud Platform Free Tier](https://cloud.google.com/free/)

#  Map AWS services to Google Cloud Platform products

If you are familiar with Amazon Web Services (AWS), a quick way to understand what the various Google Cloud Platform services do is to map them to AWS services that offer similar functionality.

Because Google and Amazon take different approaches in building cloud services, any mapping between the two can only be a rough guide. The following table only lists services that have a useful mapping between the two platforms.

| Amazon Web Services | Google Cloud Platform |
| --- | --- |
| Compute |
| Amazon EC2 |  [Google Compute Engine](https://cloud.google.com/compute/)  ([1](https://cloud.google.com/free/docs/map-aws-google-cloud-platform#footnote-1)) |
| Amazon EC2 Container Service |  [Google Container Engine](https://cloud.google.com/container-engine/) |
| AWS Elastic Beanstalk |  [Google App Engine](https://cloud.google.com/appengine/)  ([2](https://cloud.google.com/free/docs/map-aws-google-cloud-platform#footnote-2)) |
| AWS Lambda |  [Google Cloud Functions](https://cloud.google.com/functions/) |
| Storage |
| Amazon Glacier and Amazon S3 Standard - Infrequent Access |  [Google Cloud Storage Nearline](https://cloud.google.com/storage-nearline/) |
| Amazon S3 |  [Google Cloud Storage Standard](https://cloud.google.com/storage/docs/standard-storage) |
| Amazon EC2 Container Registry |  [Google Container Registry](https://cloud.google.com/container-registry/) |
| Database |
| Amazon DynamoDB |  [Google Cloud Datastore](https://cloud.google.com/datastore/) or [Google Cloud Bigtable](https://cloud.google.com/bigtable/) |
| Amazon RDS | [Google Cloud SQL](https://cloud.google.com/sql/) |
| Big data |
| Amazon EMR and AWS Data Pipeline |  [Google Cloud Dataflow](https://cloud.google.com/dataflow/) and [Google Cloud Dataproc](https://cloud.google.com/dataproc/) |
| Amazon Kinesis and Amazon Simple Queue Service (SQS) |  [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) |
| Amazon Redshift |  [Google BigQuery](https://cloud.google.com/bigquery/) |
| Monitoring |
| Amazon CloudWatch |  [Google Cloud Monitoring](https://cloud.google.com/monitoring/) and [Google Cloud Logging](https://cloud.google.com/logging/docs/) |
| Networking |
| Amazon Elastic Load Balancing |  [Google Cloud Load Balancing](https://cloud.google.com/compute/docs/load-balancing/) ([HTTP/HTTPS Load Balancing](https://cloud.google.com/compute/docs/load-balancing/http/) and [Network Load Balancing](https://cloud.google.com/compute/docs/load-balancing/network/)) |
| Amazon Route 53 |  [Google Cloud DNS](https://cloud.google.com/dns/) and [Google Domains](http://domains.google.com/) |
| AWS Direct Connect ([3](https://cloud.google.com/free/docs/map-aws-google-cloud-platform#footnote-3)) |  [Google Cloud Interconnect](https://cloud.google.com/interconnect/) |
| Identity & Security |
| AWS Identity and Access Management (IAM) |  [Google Cloud Identity & Access Management (Cloud IAM)](https://cloud.google.com/iam/) |
| AWS Organizations |  [Google Cloud Resource Manager](https://cloud.google.com/resource-manager/) |
| AWS Key Management Service (KMS) |  [Google Cloud Key Management Service (Cloud KMS)](https://cloud.google.com/kms/) |
| Amazon Inspector |  [Google Cloud Security Scanner](https://cloud.google.com/security-scanner/) |
| Deployment |
| AWS CloudFormation |  [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager/) |

(1) Compute Engine has auto-scaling, load balancing, and monitoring of unmanaged VMs.

(2) AWS Elastic Beanstalk and App Engine are often described as similar offerings, but there are significant differences in their approaches. Both offer auto-scaling, load balancing, monitoring, etc., but unlike App Engine, Elastic Beanstalk requires the typical system administration that raw VMs require (OS updates, etc.). App Engine is a platform as a service (PaaS), meaning that it's fully managed, so all of these administrative tasks are handled by Google. The basic App Engine setup includes built-in services such as Task Queues, Memcache, Users API, and more.

(3) AWS Direct Connect may vary significantly from Google Cloud Interconnect in terms of connectivity options, service providers, and available locations.

Was this page helpful? Let us know how we did:
star_border
star_border
star_border
star_border
star_border

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated September 6, 2017.