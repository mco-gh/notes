Azure and AWS services compared - multicloud

# AWS to Azure services comparison

![](data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 13'%3E%3Cpath fill='%236e6e6e' d='M14 1v12H0V1h2V0h1v1h8V0h1v1h2zm-1 3V2h-1v1h-1V2H3v1H2V2H1v2h12zm0 1H1v7h12V5zm-7.8 6c.6 0 1.1-.1 1.4-.4.4-.3.5-.6.5-1.1 0-.3-.1-.5-.3-.7-.2-.2-.4-.4-.8-.4.6-.1 1-.5 1-1.2 0-.4-.1-.6-.4-.9S5.9 6 5.4 6s-.9.1-1.2.2v.9c.3-.2.6-.3.9-.3.5 0 .8.2.8.6s-.3.6-1 .6h-.4v.8h.4c.3 0 .6.1.8.2.2.1.3.3.3.5s0 .4-.2.5c-.2.1-.4.2-.6.2-.4 0-.8-.1-1.2-.3v.9c.3.1.7.2 1.2.2zm4.2-5c-.2.1-.4.3-.6.4-.3.2-.5.3-.8.3v.9h.3l.2-.1.2-.1c.2-.1.3-.1.3-.2V11h1V6h-.6z'/%3E%3C/svg%3E")03/24/2017•![](data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 13 13'%3E%3Cpath fill='%236e6e6e' d='M6.5 13c-1.2 0-2.2-.3-3.2-.9-1-.6-1.8-1.4-2.4-2.4-.6-.9-.9-2-.9-3.2 0-1.2.3-2.2.9-3.2.6-1 1.4-1.8 2.4-2.4.9-.6 2-.9 3.2-.9 1.2 0 2.2.3 3.2.9 1 .6 1.8 1.4 2.4 2.4.6 1 .9 2.1.9 3.2 0 1.2-.3 2.2-.9 3.2-.6 1-1.4 1.8-2.4 2.4-.9.6-2 .9-3.2.9zm0-12c-1 0-1.9.2-2.8.7-.8.5-1.5 1.2-2 2-.5.9-.7 1.8-.7 2.8s.2 1.9.7 2.8c.5.8 1.2 1.5 2 2s1.8.7 2.8.7 1.9-.2 2.8-.7 1.5-1.2 2-2c.5-.9.7-1.8.7-2.8s-.2-1.9-.7-2.8c-.5-.8-1.2-1.5-2-2-.9-.5-1.8-.7-2.8-.7zM10 7H7V3H6v5h4V7z'/%3E%3C/svg%3E")16 minutes to read•Contributors

- [![larry brader](../_resources/0180b81707781b6e00ca23d82cef7a99.jpg)](https://github.com/lbrader)
- [![Michael Crump](../_resources/e248a91fc777d4e893cc11c38f215710.png)](https://github.com/mbcrump)
- [![nlarin](../_resources/15499b845745f668e9388052a196143f.jpg)](https://github.com/niklarin)
- [![Kevin Lam](../_resources/ca574347f2ed1e8dbdab311d76bc3bcd.jpg)](https://github.com/kevinlam1)
- [![Cesar De la Torre](../_resources/c202aad4f4c0f6f0755450504be6da8e.jpg)](https://github.com/CESARDELATORRE)
- [all](https://github.com/mspnp/architecture-center/blob/master/docs/aws-professional/services.md)

### In this article

1. [Azure and AWS for multicloud solutions](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#azure-and-aws-for-multicloud-solutions)

2. [Marketplace](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#marketplace)

3. [Compute](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#compute)

4. [Storage](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#storage)

5. [Networking & Content Delivery](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#networking--content-delivery)

6. [Database](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#database)

7. [Analytics and big data](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#analytics-and-big-data)

8. [Intelligence](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#intelligence)

9. [Internet of things (IoT)](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#internet-of-things-iot)

10. [Management & monitoring](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#management--monitoring)

11. [Mobile services](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#mobile-services)

12. [Security, identity, and access](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#security-identity-and-access)

13. [Developer tools](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#developer-tools)

14. [Enterprise integration](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services#enterprise-integration)

[+]()

This article helps you understand how Microsoft Azure services compare to Amazon Web Services (AWS). Whether you are planning a multicloud solution with Azure and AWS, or migrating to Azure, you can compare the IT capabilities of Azure and AWS services in all categories.[+]()

In the following tables, there are multiple Azure services listed for some AWS services. The Azure services are similar to one another, but depth and breadth of capabilities vary.[+]()

[Download a PDF of the Azure & AWS Cloud Service Map](https://aka.ms/awsazureguide)[+]()

## Azure and AWS for multicloud solutions

As the leading public cloud platforms, Azure and AWS each offer businesses a broad and deep set of capabilities with global coverage. Yet many organizations choose to use both platforms together for greater choice and flexibility, as well as to spread their risk and dependencies with a multicloud approach. Consulting companies and software vendors might also build on and use both Azure and AWS, as these platforms represent most of the cloud market demand.[+]()

For an overview of Azure for AWS users, see [Introduction to Azure for AWS experts](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/index).[+]()

## Marketplace

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Marketplace | AWS Marketplace | [Azure Marketplace](https://azure.microsoft.com/marketplace/) | Easy-to-deploy and automatically configured third-party applications, including single virtual machine or multiple virtual machine solutions. |

## Compute

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Virtual servers | Elastic Compute Cloud (EC2) VMs | [Azure Virtual Machines](https://azure.microsoft.com/services/virtual-machines/) | Virtual servers allow users to deploy, manage, and maintain OS and server software. Instance types provide combinations of CPU/RAM. Users pay for what they use with the flexibility to change sizes. |
| ** ** | Amazon Lightsail | [Azure Virtual Machines & Images](https://azure.microsoft.com/services/virtual-machines/) | Collection of virtual machine templates to select from when building out your virtual machine. |
| Container management | EC2 Container Service (ECS) | [Azure Container Service](https://azure.microsoft.com/services/container-service/) | A container management service that supports Docker containers and allows users to run applications on managed instance clusters. It eliminates the need to operate cluster management software or design fault-tolerant cluster architectures. |
| ** ** | EC2 Container Registry | [Azure Container Registry](https://azure.microsoft.com/services/container-registry/) | Allows customers to store Docker formatted images. Used to create all types of container deployments on Azure. |
| Microservice-based applications | None | [Service Fabric](https://azure.microsoft.com/services/service-fabric/) | A compute service that orchestrates and manages the execution, lifetime, and resilience of complex, inter-related code components that can be either stateless or stateful. |
| Backend process logic | Lambda | [Functions](https://azure.microsoft.com/services/functions/) | Used to integrate systems and run backend processes in response to events or schedules without provisioning or managing servers. |
| ** ** | Lambda @ Edge | None | Runs Lambda functions on AWS Edge locations in response to CloudFront events. |
| Job orchestration | AWS Batch | [Azure Batch](https://azure.microsoft.com/services/batch/) | Orchestration of the tasks and interactions between compute resources that are needed when you require processing across hundreds or thousands of compute nodes. |
| Scalability | AWS Auto Scaling | [Virtual Machine Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-overview)<br>[Azure App Service Scale Capability (PAAS)](https://azure.microsoft.com/documentation/articles/web-sites-scale/)<br>[Azure AutoScaling](https://docs.microsoft.com/en-us/azure/app-service/app-service-environment-auto-scale) | Lets you automatically change the number of instances providing a particular compute workload. You set defined metric and thresholds that determine if the platform adds or removes instances. |
| Predefined templates | AWS Quick Start | [Azure Quickstart templates](https://azure.microsoft.com/documentation/templates/) | Community-led templates for creating and deploying virtual machine–based solutions. |

## Storage

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Object storage | Simple Storage Services (S3) | [Azure Storage—Block Blob (for content logs, files) (Standard—Hot)](https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/understanding-block-blobs--append-blobs--and-page-blobs#about-block-blobs) | Object storage service, for use cases including cloud applications, content distribution, backup, archiving, disaster recovery, and big data analytics. |
| Virtual Server disk infrastructure | Elastic Block Store (EBS) | [Azure Storage Disk—Page Blobs (for VHDs or other random-write type data)](https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/understanding-block-blobs--append-blobs--and-page-blobs#about-page-blobs)<br>[Azure Storage Disks—Premium Storage](https://azure.microsoft.com/services/storage/disks/) | SSD storage optimized for I/O intensive read/write operations. For use as high performance Azure virtual machine storage. |
| Shared file storage | Elastic File System | [Azure File Storage (file share between VMs)](https://azure.microsoft.com/services/storage/files/) | Provides a simple interface to create and configure file systems quickly, and share common files. It’s shared file storage without the need for a supporting virtual machine, and can be used with traditional protocols that access files over a network. |
| Archiving—cool storage | S3 IA Glacier | [Azure Storage—Standard Cool](https://docs.microsoft.com/en-us/azure/storage/storage-blob-storage-tiers) | Cool storage is a lower cost tier for storing data that is infrequently accessed and long-lived. |
| Backup | None | [Azure Backup](https://azure.microsoft.com/services/backup/) | Backup and archival solutions allow files and folders to be backed up and recovered from the cloud, and provide off-site protection against data loss. There are two components of backup—the software service that orchestrates backup/retrieval and the underlying backup storage infrastructure. |
| Hybrid storage | Storage Gateway | [StorSimple](https://azure.microsoft.com/services/storsimple/) | Integrates on-premises IT environments with cloud storage. Automates data management and storage, plus supports disaster recovery. |
| Bulk data transfer | AWS Import/Export Disk | [Import/Export](https://azure.microsoft.com/documentation/articles/storage-import-export-service/) | A data transport solution that uses secure disks and appliances to transfer large amounts of data. Also offers data protection during transit. |
| ** ** | AWS Import/Export Snowball<br>AWS Snowball Edge<br>AWS Snowmobile | None | Petabyte- to Exabyte-scale data transport solution that uses secure data storage devices to transfer large amounts of data into and out of the AWS cloud, at lower cost than Internet-based transfers. |
| Disaster recovery | None | [Site Recovery](https://azure.microsoft.com/services/site-recovery/) | Automates protection and replication of virtual machines. Offers health monitoring, recovery plans, and recovery plan testing. |

## Networking & Content Delivery

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Cloud virtual networking | Virtual Private Cloud | [Virtual Network](https://azure.microsoft.com/services/virtual-network/) | Provides an isolated, private environment in the cloud. Users have control over their virtual networking environment, including selection of their own IP address range, creation of subnets, and configuration of route tables and network gateways. |
| Cross-premises connectivity | AWS VPC Gateway | [Azure VPN Gateway](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) | Azure VPN Gateways connect Azure virtual networks to other Azure virtual networks, or customer on-premises networks (Site To Site). It also allows end users to connect to Azure services through VPN tunneling (Point To Site). |
| Domain name system management | Route 53 | [Azure DNS](https://azure.microsoft.com/services/dns/) | Manage your DNS records using the same credentials and billing and support contract as your other Azure services |
| ** ** | Route 53 | [Traffic Manager](https://azure.microsoft.com/services/traffic-manager/) | A service that hosts domain names, plus routes users to Internet applications, connects user requests to datacenters, manages traffic to apps, and improves app availability with automatic failover. |
| Content delivery network | CloudFront | [Azure Content Delivery Network](https://azure.microsoft.com/services/cdn/) | A global content delivery network that delivers audio, video, applications, images, and other files. |
| Dedicated network | Direct Connect | [ExpressRoute](https://azure.microsoft.com/services/expressroute/) | Establishes a dedicated, private network connection from a location to the cloud provider (not over the Internet). |
| Load balancing | Elastic Load Balancing | [Load Balancer](https://azure.microsoft.com/services/load-balancer/)<br>[Application Gateway](https://azure.microsoft.com/services/application-gateway/) | Automatically distributes incoming application traffic to add scale, handle failover, and route to a collection of resources. |

## Database

| Area | AWS Service | Azure Service | Description |
| --- | --- | --- | --- |
| Relational database | RDS | [SQL Database](https://azure.microsoft.com/services/sql-database/)<br>[Azure Database for MySQL](https://azure.microsoft.com/en-us/services/mysql/)<br>[Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/services/postgresql/) | Relational database-as-a-service (DBaaS) where the database resilience, scale, and maintenance are primarily handled by the platform. |
| NoSQL—document storage | DynamoDB | [Cosmos DB](https://azure.microsoft.com/services/documentdb/) | A globally distributed, multi-model database that natively supports multiple data models: key-value, documents, graphs, and columnar. |
| NoSQL—key/value storage | DynamoDB and SimpleDB | [Table Storage](https://azure.microsoft.com/services/storage/tables/) | A nonrelational data store for semi-structured data. Developers store and query data items via web services requests. |
| Caching | ElastiCache | [Azure Redis Cache](https://azure.microsoft.com/services/cache/) | An in-memory–based, distributed caching service that provides a high-performance store typically used to offload nontransactional work from a database. |
| Database migration | Database Migration Service (Preview) | [Azure Database Migration Service](https://azure.microsoft.com/en-us/campaigns/database-migration/) | Typically is focused on the migration of database schema and data from one database format to a specific database technology in the cloud. |

## Analytics and big data

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Elastic data warehouse | Redshift | [SQL Data Warehouse](https://azure.microsoft.com/services/sql-data-warehouse/) | A fully managed data warehouse that analyzes data using business intelligence tools. It can transact SQL queries across relational and nonrelational data. |
| Big data processing | Elastic MapReduce (EMR) | [HDInsight](https://azure.microsoft.com/services/hdinsight/) | Supports technologies that break up large data processing tasks into multiple jobs, and then combine the results to enable massive parallelism. |
| Data orchestration | Data Pipeline | [Data Factory](https://azure.microsoft.com/services/data-factory/) | Processes and moves data between different compute and storage services, as well as on-premises data sources at specified intervals. Users can create, schedule, orchestrate, and manage data pipelines. |
| ** ** | AWS Glue (Preview) | [Data Factory + Data Category](https://azure.microsoft.com/services/data-factory/) | Cloud-based ETL/data integration service that orchestrates and automates the movement and transformation of data from various sources. |
| Analytics | Kinesis Analytics | [Stream Analytics](https://azure.microsoft.com/services/stream-analytics/)<br>[Data Lake Analytics](https://azure.microsoft.com/services/data-lake-analytics/)<br>[Data Lake Store](https://azure.microsoft.com/services/data-lake-store/) | Storage and analysis platforms that create insights from large quantities of data, or data that originates from many sources. |
| Visualization | QuickSight (Preview) | [PowerBI](https://powerbi.microsoft.com/) | Business intelligence tools that build visualizations, perform ad hoc analysis, and develop business insights from data. |
| ** ** | None | [Power BI Embedded](https://azure.microsoft.com/services/power-bi-embedded/) | Allows visualization and data analysis tools to be embedded in applications. |
| Search | Elasticsearch Service | [Marketplace—Elasticsearch](https://azuremarketplace.microsoft.com/marketplace/apps?page=1&search=Elasticsearch) | A scalable search server based on Apache Lucene. |
| ** ** | CloudSearch | [Azure Search](https://azure.microsoft.com/services/search/) | Delivers full-text search and related search analytics and capabilities. |
| Machine learning | Machine Learning | [Machine Learning](https://azure.microsoft.com/services/machine-learning/) | Produces an end-to-end workflow to create, process, refine, and publish predictive models that can be used to understand what might happen from complex data sets. |
| Data discovery | None | [Data Catalog](https://azure.microsoft.com/services/data-catalog/) | Provides the ability to better register, enrich, discover, understand, and consume data sources. |
| ** ** | Amazon Athena | None | Provides a serverless interactive query service that uses standard SQL for analyzing databases. |

## Intelligence

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Conversational user interfaces virtual personal assistant | Alexa Skills Kits | [Cortana Intelligence Suite —Cortana Integration](https://azure.microsoft.com/suites/cortana-intelligence-suite/) | Services cover intelligence cognitive services, machine learning, analytics, information management, big data and dashboards and visualizations. |
| ** ** |     | [Microsoft Bot Framework + Azure Bot Service](https://dev.botframework.com/) | Builds and connects intelligent bots that interact with your users using text/SMS, Skype, Teams, Slack, Office 365 mail, Twitter, and other popular services. |
| Speech recognition | Amazon Lex | [Bing Speech API](https://azure.microsoft.com/services/cognitive-services/speech/) | API capable of converting speech to text, understanding intent, and converting text back to speech for natural responsiveness. |
| ** ** |     | [Language Understanding Intelligent Service (LUIS)](https://azure.microsoft.com/services/cognitive-services/language-understanding-intelligent-service/) | Allows your applications to understand user commands contextually. |
| ** ** |     | [Speaker Recognition API](https://azure.microsoft.com/services/cognitive-services/speaker-recognition/) | Gives your app the ability to recognize individual speakers. |
| ** ** |     | [Custom Recognition Intelligent Service (CRIS)](https://azure.microsoft.com/services/cognitive-services/custom-speech-service/) | Fine-tunes speech recognition to eliminate barriers such as speaking style, background noise, and vocabulary. |
| Text to Speech | Amazon Polly | [Bing Speech API](https://azure.microsoft.com/services/cognitive-services/speech/) | Enables both Speech to Text, and Text into Speech capabilities. |
| Visual recognition | Amazon Rekognition | [Computer Vision API](https://azure.microsoft.com/services/cognitive-services/computer-vision/) | Distills actionable information from images, generates captions and identifies objects in images. |
| ** ** |     | [Face API](https://azure.microsoft.com/services/cognitive-services/face/) | Detects, identifies, analyzes, organizes, and tags faces in photos. |
| ** ** |     | [Emotions API](https://azure.microsoft.com/services/cognitive-services/emotion/) | Recognizes emotions in images. |
| ** ** |     | [Video API](https://www.microsoft.com/cognitive-services/video-api) | Intelligent video processing produces stable video output, detects motion, creates intelligent thumbnails, detects and tracks faces. |

## Internet of things (IoT)

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Internet of Things | AWS IoT Other Services (Kinesis, Machine Learning, EMR, Data Pipeline, SNS, QuickSight) | [Azure IoT Suite (IoT Hub, Machine Learning, Stream Analytics, Notification Hubs, PowerBI)](https://azure.microsoft.com/suites/iot-suite/) | Provides a preconfigured solution for monitoring, maintaining, and deploying common IoT scenarios. |
| ** ** | AWS IoT | [Azure IoT Hub](https://azure.microsoft.com/services/iot-hub/) | A cloud gateway for managing bidirectional communication with billions of IoT devices, securely and at scale. |
| ** ** | AWS Greengrass - Software for Connected Devices | [Azure IoT Gateway SDK](https://azure.microsoft.com/services/iot-hub/iot-gateway-sdk/) | Contains the infrastructure and modules to create IoT gateway solutions. The SDK can be used and extended to create gateways tailored to any end-to-end scenario. |
| Streaming data | Kinesis Firehose<br>Kinesis Streams | [Event Hubs](https://azure.microsoft.com/services/event-hubs/) | Services that allow the mass ingestion of small data inputs, typically from devices and sensors, to process and route the data. |

## Management & monitoring

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Cloud advisor | Trusted Advisor | [Azure Advisor](https://azure.microsoft.com/services/advisor/) | Provides analysis of cloud resource configuration and security so subscribers can ensure they’re making use of best practices and optimum configurations. |
| Deployment orchestration (DevOps) | OpsWorks (Chef-based) | [Azure Automation](https://azure.microsoft.com/services/automation/) | Configures and operates applications of all shapes and sizes, and provides templates to create and manage a collection of resources. |
| ** ** | CloudFormation | [Azure Resource Manager](https://azure.microsoft.com/features/resource-manager/)<br>[VM extensions](https://azure.microsoft.com/documentation/articles/virtual-machines-windows-extensions-features/)<br>[Azure Automation](https://azure.microsoft.com/services/automation/) | Provides a way for users to automate the manual, long-running, error-prone, and frequently repeated IT tasks. |
| Management & monitoring (DevOps) | CloudWatch | [Azure portal](https://azure.microsoft.com/features/azure-portal/)<br>[Azure Monitor)](https://azure.microsoft.com/services/monitor/) | A unified console that simplifies building, deploying, and managing your cloud resources. |
| ** ** | CloudWatch | [Azure Application Insights + Azure Monitor](https://azure.microsoft.com/services/application-insights/) | An extensible analytics service that helps you understand the performance and usage of your live web application. It's designed for developers, to help you continuously improve the performance and usability of your app. |
| ** ** | AWS X-Ray | [Azure Application Insights + Azure Monitor](https://azure.microsoft.com/services/application-insights/) | An extensible application performance management service for web developers on multiple platforms. You can use it to monitor your live web application, detect performance anomalies, and diagnose issues with your app. |
| ** ** | AWS Usage and Billing Report | [Azure Billing API](https://docs.microsoft.com/en-us/azure/billing/billing-usage-rate-card-overview) | Services to help generate, monitor, forecast, and share billing data for resource usage by time, organization, or product resources. |
| ** ** | AWS Management Console | [Azure portal](https://azure.microsoft.com/features/azure-portal/) | A unified management console that simplifies building, deploying, and operating your cloud resources. |
| Administration | AWS Application Discovery Service | [Azure Log Analytics in Operations Management Suite](https://azure.microsoft.com/services/log-analytics) | Provides deeper insights into your application and workloads by collecting, correlating and visualizing all your machine data, such as event logs, network logs, performance data, and much more, from both on-premises and cloud assets. |
| ** ** | Amazon EC2 Systems Manager | [Microsoft Operations Management Suite—Automation and Control functionalities](https://www.microsoft.com/cloud-platform/operations-management-suite) | Enables continuous IT services and compliance through process automation and configuration management. You can transform complex and repetitive tasks with IT automation. |
| ** ** | AWS Personal Health Dashboard | [Azure Resource Health (Preview)](https://docs.microsoft.com/en-us/azure/resource-health/resource-health-overview) | Provides detailed information about the health of resources as well as recommended actions for maintaining resource health. |
| ** ** | Third Party | [Azure Storage Explorer](http://storageexplorer.com/) | Standalone app from Microsoft that allows you to easily work with Azure Storage data on Windows, Mac OS, and Linux. |

## Mobile services

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Pro app development | Mobile Hub | [Mobile Apps](https://azure.microsoft.com/services/app-service/mobile/)<br>[Xamarin Apps](https://azure.microsoft.com/features/xamarin/) | Provides backend mobile services for rapid development of mobile solutions, identity management, data synchronization, and storage and notifications across devices. |
| ** ** | Mobile SDK | [Mobile Apps](https://azure.microsoft.com/services/app-service/mobile/) | Provides the technology to rapidly build cross-platform and native apps for mobile devices. |
| ** ** | Cognito | [Mobile Apps](https://azure.microsoft.com/services/app-service/mobile/) | Provides authentication capabilities for mobile applications. |
| App testing | AWS Device Farm | [Xamarin Test Cloud (front end)](https://www.xamarin.com/test-cloud) | Provides services to support testing mobile applications. |
| Analytics | Mobile Analytics | [HockeyApp](https://azure.microsoft.com/services/hockeyapp/)<br>[Application Insights](https://azure.microsoft.com/services/application-insights/) | Supports monitoring, and feedback collection for the debugging and analysis of a mobile application service quality. |
| Enterprise mobility management | None | [Intune](https://www.microsoft.com/cloud-platform/microsoft-intune) | Provides mobile device management, mobile application management, and PC management capabilities from the cloud. |

## Security, identity, and access

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Authentication and authorization | Identity and Access Management (IAM) | [Azure Active Directory](https://azure.microsoft.com/documentation/articles/role-based-access-control-configure/)<br>[Azure Active Directory Premium](https://www.microsoft.com/cloud-platform/azure-active-directory) | Allows users to securely control access to services and resources while offering data security and protection. Create and manage users and groups, and use permissions to allow and deny access to resources. |
| ** ** | AWS Organizations | [Azure Subscription and Service Management + Azure RBAC](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits) | Security policy and role management for working with multiple accounts. |
| ** ** | Multi-Factor Authentication | [Multi-Factor Authentication](https://azure.microsoft.com/services/multi-factor-authentication/) | Helps safeguard access to data and applications while meeting user demand for a simple sign-in process. It delivers strong authentication with a range of verification options, allowing users to choose the method they prefer. |
| Information protection | None | [Azure Information Protection](https://www.microsoft.com/cloud-platform/azure-information-protection) | Service to help control and secure email, documents, and sensitive data that you share outside your company walls. |
| Encryption | Server-side encryption with Amazon S3 Key Management Service | [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/storage-service-encryption) | Helps you protect and safeguard your data and meet your organizational security and compliance commitments. |
| ** ** | Key Management Service<br>CloudHSM | [Key Vault](https://azure.microsoft.com/services/key-vault/) | Provides security solution and works with other services by providing a way to manage, create, and control encryption keys stored in hardware security modules (HSM). |
| Firewall | Web Application Firewall | [Application Gateway Web Application Firewall (preview)](https://azure.microsoft.com/updates/application-gateway-web-application-firewall-in-public-preview/) | A firewall that protects web applications from common web exploits. Users can define customizable web security rules. |
| Security | Inspector | [Security Center](https://azure.microsoft.com/services/security-center/) | An automated security assessment service that improves the security and compliance of applications. Automatically assess applications for vulnerabilities or deviations from best practices. |
| ** ** | Certificate Manager | [App Service Certificates available on the Portal](https://azure.microsoft.com/blog/internals-of-app-service-certificate/) | Service that allows customers to create, manage and consume certificates seamlessly in the cloud. |
| Directory services | AWS Directory Service + Windows Server Active Directory on AWS | [Azure Active Directory Domain Services + Windows Server Active Directory on Azure IaaS](https://azure.microsoft.com/services/active-directory/) | Comprehensive identity and access management cloud solution that provides a robust set of capabilities to manage users and groups. It helps secure access to on-premises and cloud applications, including Microsoft online services like Office 365 and many non-Microsoft SaaS applications. |
| ** ** | None | [Azure Active Directory B2C](https://azure.microsoft.com/services/active-directory-b2c/) | A highly available, global, identity management service for consumer-facing applications that scales to hundreds of millions of identities. |
| ** ** | AWS Directory Service | [Windows Server Active Directory](https://azure.microsoft.com/services/active-directory-ds/) | Services for supporting Microsoft Active Directory in the cloud. |
| Compliance | AWS Artifact | [Microsoft Service Trust Portal](https://www.microsoft.com/TrustCenter/STP/default.aspx) | Provides access to audit reports, compliance guides, and trust documents from across cloud services. |
| Security | AWS Shield | [Azure Marketplace—Security](https://azuremarketplace.microsoft.com/marketplace/apps?search=Security&page=1) | Provides cloud services with protection from distributed denial of services (DDoS) attacks. |

## Developer tools

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Media transcoding | Elastic Transcoder | [Media Services](https://azure.microsoft.com/services/media-services/) | Services that offer broadcast-quality video streaming services, including various transcoding technologies. |
| Email | Simple Email Service (SES) | [Marketplace—Email](https://azuremarketplace.microsoft.com/marketplace/apps?page=1&search=Email) | Services for integrating email functionality into applications. |
| Messaging | Simple Queue Service (SQS) | [Azure Queue Storage](https://azure.microsoft.com/services/storage/queues/) | Provides a managed message queueing service for communicating between decoupled application components. |
| Messaging | Simple Queue Service (SQS) | [Service Bus Queues, Topics, Relays](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-queues-topics-subscriptions) | Supports a set of cloud-based, message-oriented middleware technologies including reliable message queuing and durable publish/subscribe messaging. |
| Workflow | Simple Workflow Service (SWF) | [Logic Apps](https://azure.microsoft.com/services/logic-apps/) | Serverless technology for connecting apps, data and devices anywhere—on-premises or in the cloud for large ecosystems of SaaS and cloud based connectors. |
| API management | API Gateway | [API Management](https://azure.microsoft.com/services/api-management/) | A turnkey solution for publishing APIs to external and internal consumers. |
| Enterprise app integration | None | [Logic Apps](https://azure.microsoft.com/services/logic-apps/) | Provides out-of-the box trading partner management, cloud to on-premises, and line-of-business application integration for SAP, Oracle, SQL Server, and Websphere MQ. |
| Backend process logic | Lambda | [Web Jobs](https://docs.microsoft.com/en-us/azure/app-service-web/websites-webjobs-resources) | Technology to provide an easy way to run scripts or programs as background processes in an application context. |
| Application development | None | [Logic Apps](https://azure.microsoft.com/services/logic-apps/) | Connect apps, data, and devices anywhere—on-premises or in the cloud—with our large ecosystem of SaaS and cloud-based connectors that includes Salesforce, Office 365, Twitter, Dropbox, Google Services, and more. |
| ** ** | Elastic Beanstalk | [Web Apps (App Service)](https://azure.microsoft.com/services/app-service/web/)<br>[Cloud Services](https://azure.microsoft.com/services/cloud-services/)<br>[API Apps (App Service)](https://azure.microsoft.com/services/app-service/api/) | Managed hosting platforms providing easy to use services for deploying and scaling web applications and services. |
| ** ** | CodeDeploy<br>CodeCommit<br>CodePipeline | [Visual Studio Team Services](https://www.visualstudio.com/team-services/) | Developer tools for scripting application deployment. |
| ** ** | AWS Developer Tools | [Azure Developer Tools](https://azure.microsoft.com/tools/) | Collection of tools for building, debugging, deploying, diagnosing, and managing multi-platform, scalable apps and services. |
| ** ** | None | [Power Apps](https://powerapps.microsoft.com/) | Technology to rapidly build business solutions, connecting to existing services and data sources such as Excel, SharePoint, Dynamics 365, and more using a visual designer. |
| App testing | None | [Azure DevTest Labs (backend)](https://azure.microsoft.com/solutions/dev-test/) | Testing technology to build out heterogeneous solutions for testing cross-platform functionality to your dev/test environment. Integrates to a full DevOps Continuous Integration/Deployment with Visual Studio Online service and 3rd parties such as Jenkins, Chef, Puppet, CloudTest Lite, Octopus Deploy, and others. |
| App customer payment service | Amazon Flexible Payment Service and Amazon Dev Pay | None | Cloud service that provides developers a payment service for their cloud based applications. |
| Game development (cloud-based tools) | GameLift | None | AWS managed service for hosting dedicated game servers. |
| ** ** | Lumberyard | None | Game engine integrated with AWS and Twitch. |
| DevOps | AWS CodeBuild | [Visual Studio Team Services](https://azure.microsoft.com/services/visual-studio-team-services/) | Fully managed build service that supports continuous integration and deployment. |
| Backend process logic | AWS Step Functions | [Azure Logic Apps](https://azure.microsoft.com/services/logic-apps/) | Cloud technology to build distributed applications using out-of-the-box connectors to reduce integration challenges. Connect apps, data and devices on-premises or in the cloud. |
| Programmatic access | Command Line Interface | [Azure Command Line Interface (CLI)](https://azure.microsoft.com/documentation/articles/xplat-cli-install/)<br>[Azure PowerShell](https://azure.microsoft.com/documentation/articles/powershell-install-configure/) | Built on top of the native REST API across all cloud services, various programming language-specific wrappers provide easier ways to create solutions. |

## Enterprise integration

| Area | AWS service | Azure service | Description |
| --- | --- | --- | --- |
| Enterprise app integration | none | [Azure Logic Apps](https://azure.microsoft.com/services/logic-apps/) | Provides out of the box cloud to on-premises, trading partner management, and line-of-business application integration for SAP, Oracle, SQL Server, and Websphere MQ. |
| Enterprise application services | none | [Dynamics 365](https://www.microsoft.com/dynamics365/home) | Dynamics 365 delivers the full spectrum of CRM through five individual apps— Sales, Customer Service, Field Service, Project Service Automation, and Marketing —that work seamlessly together. |
| ** ** | Amazon WorkMail<br>Amazon WorkDocs | [Office 365](https://products.office.com/) | Fully integrated Cloud service providing communications, email, document management in the cloud and available on a wide variety of devices. |
| Content management in the cloud | None | [SharePoint Online](https://products.office.com/sharepoint) | Provides a collaborative way for individuals, teams, and organizations to intelligently discover, share, and collaborate on content from anywhere and on any device. |
| Commercial PAAS-IAAS-DBaaS framework | None | [Azure Stack](https://azure.microsoft.com/overview/azure-stack/) | A hybrid cloud platform that lets you deliver Azure services from your organization’s datacenter. |