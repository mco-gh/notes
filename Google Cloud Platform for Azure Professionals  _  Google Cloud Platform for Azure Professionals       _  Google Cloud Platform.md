Google Cloud Platform for Azure Professionals  |  Google Cloud Platform for Azure Professionals       |  Google Cloud Platform

star_border
star_border
star_border
star_border
star_border

- [Documentation](https://cloud.google.com/docs/)

- chevron_right

 [Google Cloud Platform for Azure Professionals](https://cloud.google.com/docs/compare/azure)

#  Google Cloud Platform for Azure Professionals

*Updated July 18, 2017*

This guide is designed to equip professionals who are familiar with Microsoft Azure with the key concepts required to get started with Google Cloud Platform. The guide compares Cloud Platform with Azure and highlights the similarities and differences between the two. In addition, the guide provides quick-reference mappings of Azure products, concepts, and terminology to the corresponding products, concepts, and terminology on Cloud Platform.

This guide doesn't attempt to compare the syntax and semantics of the SDK, APIs, or command-line tools provided by Azure and Cloud Platform.

star**Note:** This set of articles compares Cloud Platform services to Azure services as they are used in the Resource Manager deployment model. The articles do not discuss Azure's deprecated classic deployment model.

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Why Google Cloud Platform?

For the past 15 years, Google has been building one of the fastest, most powerful, and highest-quality cloud infrastructures on the planet. Internally, Google uses this infrastructure for several high-traffic and global-scale services, including[Gmail](https://mail.google.com/),[Maps](https://www.google.com/maps),[YouTube](https://www.youtube.com/), and[Search](https://www.google.com/). Because of the size and scale of these services, Google has put a lot of work into optimizing its infrastructure and creating a suite of tools and services to manage it effectively. Google Cloud Platform puts this infrastructure and these management resources at your fingertips.

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Regions and zones

As with Azure, Google Cloud Platform products are deployed within**regions** located around the world. Each region comprises one or more data centers that are in close geographical proximity to each other. Cloud Platform further divides availability into **zones**, which are isolated locations within a region.

star**Note:** For a full mapping of Cloud Platform's global regions and zones, see[Cloud Locations](https://cloud.google.com/about/locations).

In addition, some Cloud Platform services replicate and serve data at a multi-regional level rather than the more granular regional or zonal levels. These services include Google App Engine and Google Cloud Storage Multi-Regional. Currently, the available multi-regional locations are United States, Europe, and Asia.

### Isolation and availability

By design, Azure pairs regions that are on the same continent and are physically isolated from each other by at least 300 miles into availability sets. Azure encourages users to architect their systems and applications around these pairs, creating an active-active recovery setup for availability and isolation purposes. In addition, some Azure services, such as Blob service, have replication options that automatically replicate data across paired regions.

Cloud Platform employs a similar strategy for isolation and availability, isolating regions from each other for availability reasons. Cloud Platform does not prescribe specific regional pairings; however, as with Azure, you must architect your application across multiple regions if you want to achieve high availability. Also like Azure, some Cloud Platform services, such as Cloud Storage Multi-Regional, have built-in multi-regional synchronization.

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Accounts and quotas

To use an Azure service, you must either sign up for an Azure account or add Azure to your existing Microsoft Account. After you set up your Azure account, you can create a subscription within the account, and then launch services within that subscription. Each Azure account can support multiple subscriptions, and each subscription can use its own billing account if needed.

Cloud Platform's model is similar to that of Azure. You gain access to Cloud Platform services by setting up a Google account, and you launch services within[projects](https://cloud.google.com/docs/overview/#projects), which are functionally similar to subscriptions on Azure. If needed, you can choose to group your projects by organization as well. See[Cloud Platform Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)for more information.

Azure and Cloud Platform both have default soft limits on their services for new accounts. These soft limits are not tied to technical limitations for a given service. Instead, they are in place to help prevent fraudulent accounts from using excessive resources, and to limit risk for new users, keeping them from spending more than intended as they explore the platform. If you find that your application has outgrown these limits, Azure and Cloud Platform provide straightforward ways to get in touch with the appropriate internal teams to raise the limits on their services.

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Pricing

Because pricing tends to change more often than core features or services, this set of articles avoids pricing specifics where possible. However, each article discusses the pricing model behind each service wherever helpful. For up-to-date price comparisons for your specific solution, use the[Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/)and[Cloud Platform calculator](https://cloud.google.com/products/calculator/)to see which configuration provides the best value in terms of flexibility, scalability, and cost.

### Discount pricing

Azure and Cloud Platform each provide discounts for a subset of their respective services, but through different mechanisms.

You can get discounts on various Azure services through your Microsoft Enterprise Agreement by committing to a base-wide installation of one or more Microsoft Server or Cloud components with full Software Assurance coverage. If you don't have a Microsoft Enterprise Agreement, you might also be able to get discounted rates through a reseller.

Cloud Platform provides sustained-use discounts on a per-service basis based on your monthly usage. For example, Google Compute Engine offers sustained-use discounts based on the cumulative number of hours a given virtual machine runs in a given month. If your resource usage is steady and predictable, you can also get heavily discounted rates through[committed-use discounts](https://cloud.google.com/compute/pricing#committed_use). Committed-use discounts allow you to purchase a specific number of virtual CPUs (vCPUs) and amount of memory at up to a 57% discount over full prices, depending on the duration you commit to.

### Support plans

Azure and Cloud Platform approach their support plans in different ways. Azure bundles their support levels into five different subscription tiers. These tiers range from Pay-As-You-Go, a free tier that provides basic account support and online help resources, to Premier Support, which is Azure's most comprehensive support tier.

As with Azure, Cloud Platform provides basic account support and online help resources free of charge. However, you purchase Cloud Platform's paid support services separately rather than with a specific account or project. For more information, see[Support](https://cloud.google.com/support/).

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Resource management interfaces

Azure and Cloud Platform each provide command-line interfaces (CLIs) for interacting with services and resources. Azure provides both the[Azure CLI](https://azure.github.io/projects/clis/), which is a cross-platform tool, and a set of[Azure cmdlets](https://github.com/azure/azure-powershell)that you can install and use through Windows PowerShell. Cloud Platform provides a set of command-line tools through the[Cloud SDK](https://cloud.google.com/sdk/), a cross-platform toolkit.

Azure and Google Cloud Platform also provide web-based consoles. Each console allows users to create, manage, and monitor their resources. The console for Google Cloud Platform is located athttps://console.cloud.google.com/. You can also use the Cloud SDK in your web browser by using[Google Cloud Shell](https://cloud.google.com/shell/docs/).

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Service types

At a high level, cloud platforms begin by providing a set of baseline services: compute, storage, networking, and database services. Azure's baseline services include:

- *Compute*: Azure virtual machines, Azure App Service
- *Storage*: Azure Blob service, Azure virtual hard disks (VHDs)
- *Networking*: Azure virtual network (VNet)
- *Databases*: Azure Cloud SQL Database, Azure SQL Data Warehouse, Azure Table Storage, CosmosDB

Cloud Platform's baseline services include:

- *Compute*: Google Compute Engine, Google App Engine
- *Storage*: Google Cloud Storage, Compute Engine persistent disks
- *Networking*: Virtual Private Cloud (VPC) network
- *Databases*: Google Cloud SQL, Google Cloud Datastore, Google Cloud Bigtable

Each platform then builds other higher-level services on top of these services. Typically, these higher-level services can be categorized as one of three types:

- *Application services*: Services designed to help optimize applications in the cloud. Examples include Azure Service Bus and Google Cloud Pub/Sub.
- *Big data and analytics services*: Services designed to help process and interpret large amounts of data, such as Azure HDInsight and Google Cloud Dataflow.
- *Management services*: Services designed to help you manage your application and track its performance. Examples include Azure Application Insights and Google Stackdriver Monitoring.

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)Service comparison

The following table provides a side-by-side comparison of the various services available on Azure and Cloud Platform.

| Service category | Service | Azure | Cloud Platform |
| --- | --- | --- | --- |
| Compute | IaaS | Virtual Machines | [Google Compute Engine](https://cloud.google.com/compute/) |
|     | PaaS | App Service, Cloud Services | [Google App Engine](https://cloud.google.com/appengine/) |
|     | Containers | Azure Container Service, Azure Service Fabric | [Google Container Engine](https://cloud.google.com/container-engine/) |
|     | Serverless functions | Functions | [Google Cloud Functions](https://cloud.google.com/functions/) |
| Network | Virtual networks | Azure VNets | [VPC networks](https://cloud.google.com/vpc/) |
|     | Load Balancer | Azure Load Balancer, Application Gateway | [Google Cloud Load Balancing](https://cloud.google.com/load-balancing/) |
|     | Dedicated Interconnect | ExpressRoute | [Google Cloud Interconnect](https://cloud.google.com/interconnect/) |
|     | DNS | Azure DNS | [Google Cloud DNS](https://cloud.google.com/dns/) |
|     | CDN | Azure CDN | [Google Cloud CDN](https://cloud.google.com/cdn/) |
| Storage | Object Storage | Azure Blob Storage | [Google Cloud Storage Multi-regional, Google Cloud Storage Regional](https://cloud.google.com/storage/) |
|     | Block Storage | Disk Storage | [Google Compute Engine persistent disks](https://cloud.google.com/persistent-disk/) |
|     | File Storage | Azure File Storage | N/A* |
|     | Reduced-availability Storage | Azure Cool Blob Storage | [Google Cloud Storage Nearline](https://cloud.google.com/storage/archival/) |
|     | Archival Storage | N/A | [Google Cloud Storage Coldline](https://cloud.google.com/storage/archival/) |
| Database | RDBMS | SQL Database | [Google Cloud SQL](https://cloud.google.com/sql/), [Google Cloud Spanner](https://cloud.google.com/spanner/) |
|     | NoSQL: Key-value | Table Storage | [Google Cloud Datastore](https://cloud.google.com/datastore/), [Google Cloud Bigtable](https://cloud.google.com/bigtable/) |
|     | NoSQL: Indexed | CosmosDB | [Google Cloud Datastore](https://cloud.google.com/datastore/) |
| Big Data & Analytics | Batch Data Processing | HDInsight, Batch | [Google Cloud Dataproc](https://cloud.google.com/dataproc/), [Google Cloud Dataflow](https://cloud.google.com/dataflow/) |
|     | Stream Data Processing | Stream Analytics | [Google Cloud Dataflow](https://cloud.google.com/dataflow/) |
|     | Stream Data Ingest | Event Hubs, Service Bus | [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) |
|     | Analytics | Data Lake Analytics, Data Lake Store | [Google BigQuery](https://cloud.google.com/bigquery/) |
| Application Services | Messaging | Service Bus | [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) |
| Management Services | Monitoring | Application Insights | [Stackdriver Monitoring](https://cloud.google.com/monitoring/) |
|     | Logging | Application Insights | [Stackdriver Logging](https://cloud.google.com/logging/) |
|     | Deployment | Azure Resource Manager | [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager/) |

star* While Google Cloud Platform doesn't provide a native filer service, you can set up a filer-like system in several ways. For details, see [File Servers on Google Compute Engine](https://cloud.google.com/solutions/filers-on-compute-engine).

## [arrow_upward](https://cloud.google.com/docs/compare/azure/#top_of_page)What's next?

[Next: Compute](https://cloud.google.com/docs/compare/azure/compute)

Was this page helpful? Let us know how we did:
star_border
star_border
star_border
star_border
star_border

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.