CockroachDB 1.0 is Production-Ready

[product](https://www.cockroachlabs.com/categories/product/) /
May 10, 2017

# CockroachDB 1.0 is Production-Ready

by[Spencer Kimball](https://www.cockroachlabs.com/author/spencer-kimball/)
![](../_resources/27ce55cf2982de0583603550d45ffa16.png)

Today, we are pleased to announce the release of CockroachDB 1.0, the first open source, cloud-native SQL database. We’re also announcing a series B fundraise from investors who share our vision. The launch of 1.0 marks our graduation from beta to a production-ready database, designed to power business at any scale from the startup to the enterprise.

A brief introduction is in order. While databases aren’t generally considered the most thrilling subject in technology news, ignoring them would be a mistake. Understanding the ongoing evolution of databases brings into focus a ruthless arms race between what businesses need to do with data, and what existing technologies struggle to provide. The most insistent pressures have forced databases alternatively to become faster, bigger, and more reliable. Then again: faster, bigger, and more reliable. And the cycle continues.

We’re seeing just such an evolution in 2017. Some folks refer to it as “NewSQL”. It’s a combination of making general purpose relational database systems (RDBMSs) both bigger and more reliable. CockroachDB earns its NewSQL stripes by providing distributed SQL to accommodate ever-larger data sizes and multi-active availability, a new model for high availability (HA). These capabilities establish a fundamentally better standard for deploying global cloud services.

With customers already in production, including Baidu and Heroic Labs, and more than 100,000 downloads since our beta release, we are happy to additionally announce our series B raise of $27M, led by Satish Dharmaraj of Redpoint Ventures, joined by Benchmark, FirstMark Capital, GV (formerly Google Ventures), Index Ventures, and Work-Bench. Satish will make a valuable addition to our investor and advisory team. Among many other things, he both founded and ran Zimbra, an open source company which successfully competed with an industry Goliath: Microsoft. This latest round provides the capitalization to match the size of both the challenge and the opportunity ahead.

## CockroachDB 1.0

CockroachDB is a cloud-native SQL database for building global, scalable cloud services that survive disasters. But what does “cloud-native” actually mean? We believe the term implies horizontal scalability, no single points of failure, survivability, automatable operations, and no platform-specific encumbrances.

To realize these product goals, development over the past year has focused on three critical areas: distributed SQL to support small and large use cases alike and scale seamlessly between them; multi-active availability for always-consistent high availability; and flexible deployment for automatable operations in virtually any environment.

### Distributed SQL

Relational databases offering SQL have traditionally been constrained to single-node deployments. The difficulty of scaling SQL workloads is clear from the meteoric rise of NoSQL databases over the past decade. NoSQL databases promised scale (and simplicity), and they delivered. However, adoption remains a small fraction of the total database market, and growth has slowed. One reason is that NoSQL solutions sacrifice guarantees, common to SQL, that make life simpler for programmers. No ACID transactions or read consistency, along with the requirement to learn a custom query and data modification language, can be significant barriers to adoption.

CockroachDB provides scale without sacrificing SQL functionality. It offers fully-distributed ACID transactions, zero-downtime schema changes, and support for secondary indexes and foreign keys. It works out of the box with many popular ORM frameworks by supporting an industry standard SQL dialect. In addition, release 1.0 introduces a distributed query execution engine, enabling distributed JOINs to support analytics queries that speed up linearly as nodes are added to your cluster.

We recently demonstrated a use case with Baidu processing 2 billion inserts a day for one of the top ten largest global internet companies. This rate of transactions continued regardless of artificially-induced “chaos” events, which caused significant concurrent re-replication and rebalancing across the cluster.

### Multi-Active Availability

“High availability” (HA) is a crucial capability. If your database is not available, then the services that rely on it won’t be either. Until now, most database HA solutions have sacrificed consistency for performance. However, when networks and nodes fail in the real world, applications will read incorrect data, and write values that disappear into thin air. Speed makes for great benchmarks, but it must be a secondary consideration when working with mission-critical data.

CockroachDB takes a different approach to HA, putting consistency first, where it belongs. We call it “multi-active availability”, because it’s an evolution in high availability from active-active replication. Instead of eventual consistency, it employs strongly-consistent consensus-based replication, which uses three or more active replicas, any of which can begin serving read/write client traffic. Unlike primary-secondary replication, which maintains 50% (or more) of all resources as idle replication targets, multi-active availability dynamically utilizes all available resources. Unlike active-active replication, multi-active availability will not read or write inconsistently and doesn’t require conflict resolution.

One customer of ours, one of the largest online gaming companies in the world, was looking for a solution to serve consistent reads and writes across continents. With multi-active availability, nodes geographically closest to their users are able to serve queries, significantly reducing latency.

### Flexible Deployments

Even the best technology is only as useful as its weakest operational link. If it can’t be easily deployed and operated, it will have trouble thriving in production. We made architectural and operational simplicity a priority from the start. That simplicity means CockroachDB can be managed both with popular datacenter orchestration technologies like Kubernetes and Docker Swarm, and even manually, meaning it can flexibly fit into any custom operational environment.

CockroachDB can be run on premise or on any public cloud, deployed in hybrid cross-cloud configurations, and migrated between clouds with zero downtime. This gives companies a powerful degree of flexibility, distinctly absent from the vendor lock-in associated with using a proprietary database as a service.

At the OpenStack Interop conference yesterday in Boston, CockroachDB was deployed live across 15 private clouds, demonstrating significant portability and flexibility. A video of the demo is below:

##

###

[Interop Challenge](https://www.youtube.com/watch?v=nBXXLNIwAoo)

[  Kubernetes and CockroachDB  OpenStack Foundation • 278 views  6:57](https://www.youtube.com/watch?v=PIePIsskhrw)[  The Police’s Andy Summers opens up on his rocky relationship with Sting  HitFix • 97K views  6:50](https://www.youtube.com/watch?v=F0ncAdeyOKw)[  Here's What a $300,000 Rolls-Royce Was Like... in 1996  Doug DeMuro • 1.2M views  18:13](https://www.youtube.com/watch?v=cnAUnGjMd5U)[  AT&T Container Strategy and OpenStack's Role in It  OpenStack Foundation • 95 views  34:53](https://www.youtube.com/watch?v=rYRiH3HZFN4)[  David Duchovny & Gillian Anderson Explain their 90's Tension  Jimmy Kimmel Live • 1M views  3:11](https://www.youtube.com/watch?v=BgEN1t4jPRE)[  The Magic of Not Giving a F*** | Sarah Knight | TEDxCoconutGrove  TEDx Talks • 356K views  12:37](https://www.youtube.com/watch?v=GwRzjFQa_Og)[  Patented Weed Wacker Outboard boat motor attachment! Water Whizz  Water Whizz • 378K views  2:41](https://www.youtube.com/watch?v=CZQlkFjfIHM)[  Funniest Leadership Speech ever!  SpecificDusty • 3M views  5:09](https://www.youtube.com/watch?v=SA7bKo4HRTg)[  Bruce Springsteen Picks His Top 5 Favorite Springsteen Songs  The Late Show with Stephen Colbert • 493K views  5:32](https://www.youtube.com/watch?v=W8CsEqYCg68)[  Bra-less Liz Hurley befuddles Billy Connolly at the BAFTAs!  TaggleElgate • 6.2M views  2:04](https://www.youtube.com/watch?v=9BkwnGq2yaA)[  Phil Collins Takes The Drum Quiz - The Jonathan Ross Show  The Jonathan Ross Show • 383K views  5:52](https://www.youtube.com/watch?v=kSTDgBSvJs4)[  Mark Cuban Can't Stop Laughing At Fox' Tucker Carlson Talking About Trump  Jon Snow - The Viral Network • 1.6M views  8:00](https://www.youtube.com/watch?v=I3HImBMyQ6k)

5:10 / 12:05
[(L)](https://www.youtube.com/watch?v=nBXXLNIwAoo)

## Commercial Offering: CockroachDB Enterprise

Working at enterprise-scale in production means that operational workloads must be run with minimal downtime and with multiple failsafes. In addition to support for zero-downtime, rolling upgrades and certificate rotation, we are happy to announce a feature available specifically as part of our CockroachDB Enterprise offering: distributed, incremental backup and restore.

This feature is intended to serve customers with large data sets and exacting production requirements. Distributed backup / restore parallelizes backup and restore tasks across all nodes in the cluster. Incremental backups enable efficient periodic updates to full backups. Data is written to and restored from any configurable storage sink, such as blob stores offered by AWS, GCP, and Azure.

Because periodic backup and restore is a best practice for anyone running a service on top of a database, a non-distributed option for backup / restore is available for free in the CockroachDB Core offering.

## The Future

We’ve come to a significant milestone. Release 1.0 is the production-ready debut of the world’s first open source, cloud-native SQL database. But this is just table stakes. The most interesting future challenge is to tackle problems bedeviling the world’s fastest growing and largest companies, which are struggling to build global services. How do you build data architectures able to serve customers on multiple continents, while presenting your operators and application developers with what looks like a single, logical database? How do you both minimize latencies and provide the foundation for compliance with rapidly evolving data sovereignty laws?

Our first significant step in this direction will be a geo-partitioning feature, which will enable row-level control of geographic replication, keeping your customers’ data next to your customers. While CockroachDB already supports flexible geographic replication at table and database granularities, geo-partitioning will allow any column or columns in a table to serve as partition keys. This makes it possible to relocate a customer from Sydney to London with a simple SQL UPDATE statement. Transactions and queries that span partitions will be handled transparently by CockroachDB. We expect a beta version of this capability in late 2017!

## Where Rubber Meets Road

We’ve taken pains to test CockroachDB in many environments, with different workloads, and with various manufactured (and unmanufactured!) chaos events. We’ve also made significant progress on performance. However, to paraphrase Donald Rumsfeld, there are both known unknowns and worse, unknown unknowns in our immediate future.

This is the point at which the rubber meets the road for CockroachDB, and we expect that the wider set of users, use cases, and environments will highlight deficiencies in our product. In accordance, we expect to devote significant resources to this “ruggedization” phase. While release 1.1 won’t be ready until October 2017, point releases along the way will further stabilize the 1.0 release.

For release 1.1, expect additional SQL coverage, better diagnostic tools, and significant performance improvements.

We look forward to welcoming new users to CockroachDB with our 1.0 release. And we’re committed to making you successful both now, and in the future, by continually expanding CockroachDB’s capabilities to keep your business well ahead of the curve.

We will be in [San Francisco on Thursday, May 11](https://bit.ly/sf-cockroachdb1dot0) and in [NYC on Wednesday, May 17](https://bit.ly/nyc-cockroachdb-1dot0) for our CockroachDB user groups. Our CTO Ben Darnell will cover what went into the 1.0, so come give us your feedback.

![](../_resources/868210463e0a98b5727f6890294efa70.png)

## Subscribe to our blog to get posts to your inbox

[beta](https://www.cockroachlabs.com/tags/beta)[1.0](https://www.cockroachlabs.com/tags/1.0)[distributed SQL](https://www.cockroachlabs.com/tags/distributed%20SQL)[cloud-native](https://www.cockroachlabs.com/tags/cloud-native)[multi-active availability](https://www.cockroachlabs.com/tags/multi-active%20availability)[release](https://www.cockroachlabs.com/tags/release)[SQL](https://www.cockroachlabs.com/tags/SQL)[CockroachDB Core](https://www.cockroachlabs.com/tags/CockroachDB%20Core)[CockroachDB Enterprise](https://www.cockroachlabs.com/tags/CockroachDB%20Enterprise)

## Share

[![](../_resources/b54c17e275b4af549918b7a0165cb473.png)](https://www.facebook.com/sharer.php?u=https%3a%2f%2fwww.cockroachlabs.com%2fblog%2fcockroachdb-1-0-release%2f)[![](../_resources/95f66634896457a7687f34aafbab05db.png)](https://twitter.com/share?url=https%3a%2f%2fwww.cockroachlabs.com%2fblog%2fcockroachdb-1-0-release%2f)[![](../_resources/83d585412f941ffaee7e4664855a86a8.png)](https://www.reddit.com/submit?url=https%3a%2f%2fwww.cockroachlabs.com%2fblog%2fcockroachdb-1-0-release%2f)

## Subscribe to our blog

## What's inside CockroachDB Core?

[Read the product specs](https://www.cockroachlabs.com/product/cockroachdb-core/)