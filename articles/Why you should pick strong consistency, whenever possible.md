Why you should pick strong consistency, whenever possible

# Why you should pick strong consistency, whenever possible

By Mike Curtiss, Software Engineer, Cloud Spanner

Do you like complex application logic? We don’t either. One of the things we’ve learned here at Google is that application code is simpler and development schedules are shorter when developers can rely on underlying data stores to handle complex transaction processing and keeping data ordered. To quote the original Spanner paper, “we believe it is better to have application programmers deal with performance problems due to overuse of transactions as bottlenecks arise, rather than always coding around the lack of transactions.”1

Put another way, data stores that provide transactions and consistency across the entire dataset by default lead to fewer bugs, fewer headaches and easier-to-maintain application code.

### Defining database consistency

But to have an interesting discussion about consistency, it’s important to first define our terms. A quick look at different databases on the market shows that not all consistency models are created equal, and that some of the related terms can intimidate even the bravest database developer. Below is a short primer on consistency:

|     |     |     |
| --- | --- | --- |
| **Term** | **Definition** | **What Cloud Spanner Supports** |
| *Consistency* | Consistency in database systems refers to the requirement that any given database transaction must change affected data only in allowed ways. Any data written to the database must be valid according to all defined rules.2 | Cloud Spanner provides external consistency, which is strong consistency + additional properties (including serializability and linearizability). All transactions across a Cloud Spanner database satisfy this consistency property, not just those within a replica or region. |
| *Serializability* | Serializability is an isolation property of transactions, where every transaction may read and write multiple objects. It guarantees that transactions behave the same as if they had executed in some serial order. It's okay for that serial order to be different from the order in which transactions were actually run.3 | Cloud Spanner provides external consistency, which is a stronger property than serializability, which means that all transactions appear as if they executed in a serial order, even if some of the reads, writes and other operations of distinct transactions actually occurred in parallel. |
| *Linearizability* | Linearizability is a recency guarantee on reads and writes of a register (an individual object). It doesn’t group operations together into transactions, so it does not prevent problems such as write skew, unless you take additional measures such as materializing conflicts.4 | Cloud Spanner provides external consistency, which is a stronger property than linearizability, because linearizability does not say anything about the behavior of transactions. |
| *Strong Consistency* | All accesses are seen by all parallel processes (or nodes, processors, etc.) in the same order (sequentially)5<br>In some definitions, a replication protocol exhibits "strong consistency" if the replicated objects are linearizable. | The default mode for reads in Cloud Spanner is "strong," which guarantees that they observe the effects of all transactions that committed before the start of the operation, independent of which replica receives the read. |
| *Eventual Consistency* | Eventual consistency means that if you stop writing to the database and wait for some unspecified length of time, then<br>eventually all read requests will return the same value.6 | Cloud Spanner supports bounded stale reads, which offer similar performance benefits as eventual consistency but with much stronger consistency guarantees. |

Cloud Spanner, in particular, provides [external consistency](https://cloud.google.com/spanner/docs/true-time-external-consistency), which provides all the benefits of strong consistency plus serializability. All transactions (across rows, regions and continents) in a Cloud Spanner database satisfy the external consistency property, not just those within a replica. External consistency states that Cloud Spanner executes transactions in a manner that's indistinguishable from a system in which the transactions are executed serially, and furthermore, that the serial order is consistent with the order in which transactions can be observed to commit. External consistency is a stronger property than both [linearizability and serializability](https://dddpaul.github.io/blog/2016/03/17/linearizability-and-serializability/).

### Consistency in the wild

There are lots of use cases that call for [external consistency](https://cloud.google.com/spanner/docs/true-time-external-consistency). For example, a financial application might need to show users' account balances. When users make a deposit, they want to see the result of this deposit reflected immediately when they view their balance (otherwise they may fear their money has been lost!). There should never appear to be more or less money in aggregate in the bank than there really is. Another example might be a mail or messaging app: You click "send" on your message, then immediately view "sent messages" because you want to double check what you wrote. Without external consistency, the app’s request to retrieve your sent messages may go to a different replica that's behind on getting all state changes, and have no record of your message, resulting in a confusing and reduced user experience.

But what does it really mean from a technical standpoint to have external consistency? When performing read operations, external consistency means that you're reading the latest copy of your data in global order. It provides the ability to read the latest change to your data across rows, regions and continents. From a developer’s perspective, it means you can read a consistent view of the state of the entire database (not just a row or object) at any point in time. Anything less introduces tradeoffs and complexity in the application design. That in turn can lead to brittle, hard-to-maintain software and can cause innumerable maintenance headaches for developers and operators. Multi-master architectures and multiple levels of consistency are workarounds for not being able to provide the external consistency that Cloud Spanner does.

What’s the problem with using something less than external consistency? When you choose a relaxed/eventual consistency mode, you have to understand which consistency mode you need to use for each use case and have to hard code rigid transactional logic into your apps to guarantee the correctness and ordering of operations. To take advantage of "transactions" in database systems that have limited or no strong consistency across documents/objects/rows, you have to design your application schema such that you never need to make a change that involves multiple "things" at the same time. That’s a huge restriction and workarounds at the application layer are painful, complex, and often [buggy](http://www.bailis.org/papers/acidrain-sigmod2017.pdf).

Further, these workarounds have to be carried everywhere in the system. For example, take the case of adding a button to set your color scheme in an admin preferences panel. Even a simple feature like this is expected to be carried over immediately across the app and other devices and sessions. It needs a synchronous, strongly consistent update—or a makeshift way to obtain the same result. Using a workaround to achieve strong consistency at the application level adds a velocity-tax to every subsequent new feature—no matter how small. It also makes it really hard to scale the application dev team, because everyone needs to be an expert in these edge cases. With this example, a unit test that passes on a developer workstation does not imply it will work in production at scale, especially in high concurrency applications. Adding workarounds to an eventually consistent data store often introduces bugs that go unnoticed until they bite a real customer and corrupt data. In fact, you may not even recognize the workaround is needed in the first place.

Lots of application developers are under the impression that the performance hit of external or strong consistency is too high. And in some systems, that might be true. Additionally, we're firm believers that having choice is a good thing—as long as the database does not introduce unnecessary complexity or introduce potential bugs in the application. Inside Google, we aim to give application developers the performance they need while avoiding unnecessary complexity in their application code. To that end, we’ve been researching advanced distributed database systems for many years and have built a wide variety of data stores to get strong consistency just right. Some examples are Cloud Bigtable, which is strongly consistent within a row; Cloud Datastore, which is strongly consistent within a document or object; and Cloud Spanner, which offers strong consistency across rows, regions and continents with serializability. [Note: In fact, Cloud Spanner offers a stronger guarantee of external consistency (strong consistency + serializability), but we tend to talk about Cloud Spanner having strong consistency because it's a more broadly accepted term.]

###

Strongly consistent reads and Cloud Spanner

Cloud Spanner was designed from the ground up to serve strong reads (i.e., strongly consistent reads) by default with low latency and high throughput. Thanks to the unique power of [TrueTime](https://cloud.google.com/spanner/docs/true-time-external-consistency), Spanner provides strong reads for arbitrary queries without complex multi-phase consensus protocols and without locks of any kind. Cloud Spanner’s use of TrueTime also provides the added benefit of being able do global bounded-staleness reads.

Better yet, Cloud Spanner offers strong consistency for multi-region and regional configurations. Other globally distributed databases present a dilemma to developers: If they want to read the data from geographically distributed regions, they forfeit the ability to do strongly consistent reads. In these other systems, if a customer opts to have strongly consistent reads, then they forfeit the ability to do reads from remote regions.

To take maximum advantage of the external consistency guarantees that Cloud Spanner provides and to maximize your application's performance, we offer the following two recommendations:

1. Always use strong reads, whenever possible. Strong reads, which provide strong consistency, ensure that you are reading the latest copy of your data. Strong consistency makes application code simpler and applications more trustworthy.

2. If latency makes strong reads infeasible in some situations, then use reads with bounded-staleness to improve performance, in places where strong reads with the latest data are not necessary. Bounded-staleness semantics ensures you read a guaranteed prefix of the data (for example, within a specified period of time) that is consistent, as opposed to eventual consistency where you have no guarantees and your app can read almost anything forwards or back in time from when you queried it.

Foregoing strong consistency has some real risks. Strong reads across a database ensure that you're reading the latest copy of your data and that it maintains the referential integrity of the entire dataset, making it easier to reason about concurrent requests. Using weaker consistency models introduces the risk of software bugs and can be a waste of developer hours—and potentially—customer trust.

### What about writes?

Strong consistency is even more important for write operations—especially read-modify-write transactions. Systems that don't provide strong consistency in such situations create a burden for application developers, as there's always a risk of putting your data into an inconsistent state.

Perhaps the most insidious type of problem is write skew. In write skew, two transactions read a set of objects and make changes to some of those objects. However, the modifications that each transaction makes affect what the other transaction should have read. For example, consider a database for an airline based in San Francisco. It’s the airline’s policy to always have a free plane in San Francisco, in the event that this spare plane is needed to replace another plane with maintenance problems or for some other need. Imagine two transactions that are both reserving planes for upcoming flights out of San Francisco:

	Begin Transaction
	SELECT * FROM Airplanes WHERE location = "San Francisco" AND Availability = "Free";
	If number of airplanes is > 1:  # to enforce "one free plane" rule
	Pick 1 airplane
	Set its Availability to "InUse"
	Commit
	Else: Rollback

Without strong consistency (and, in particular, serializable isolation for these transactions), both transactions could successfully commit, thus potentially breaking our one free plane rule. There are many more situations where write skew can cause problems7.

Because Cloud Spanner was built from the ground up to be a relational database with strong, transactional consistency—even for complex multi-row and multi-table transactions—it can be used in many situations where a NoSQL database would cause headaches for application developers. Cloud Spanner protects applications from problems like write skew, which makes it appropriate for mission-critical applications in many domains including finance, logistics, gaming and merchandising.

### How does Cloud Spanner differ from multi-master replication?

One topic that's often combined with scalability and consistency discussions is multi-master replication. At its core, multi-master replication is a strategy used to reduce mean time to recovery for vertically scalable database systems. In other words, it’s a disaster recovery solution, and not a solution for global, strong consistency. With a multi-master system, each machine contains the entire dataset, and changes are replicated to other machines for read-scaling and disaster recovery.

In contrast, Cloud Spanner is a truly distributed system, where data is distributed across multiple machines within a replica, and also replicated across multiple machines and multiple data centers. The primary distinction between Cloud Spanner and multi-master replication is that Cloud Spanner uses [paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) to synchronously replicate writes out of region, while still making progress in the face of single server/cluster/region failures. Synchronous out-of-region replication means that consistency can be maintained, and strongly consistent data can be served without downtime, even when a region is unavailable—no acknowledged writes are delayed/lost due to the unavailable region. Cloud Spanner’s paxos implementation elects a leader so that it's not necessary to do time-intensive quorum reads to obtain strong consistency. Additionally, Cloud Spanner shards data horizontally across servers, so individual machine failures impact less data. While a node is recovering, replicated nodes on other clusters that contain that dataset can assume mastership easily, and serve strong reads without any visible downtime to the user.

### A strongly consistent solution for your mission-critical data

For storing critical, transactional data in the cloud, Cloud Spanner offers a unique combination of external, strong consistency, relational semantics, high availability and horizontal scale. Stringent consistency guarantees are critical to delivering trustworthy services. Cloud Spanner was built from the ground up to provide those guarantees in a high-performance, intuitive way. We invite you to try it out and learn more.

See more on [Cloud Spanner](https://cloud.google.com/spanner/) and [external consistency](https://cloud.google.com/spanner/docs/true-time-external-consistency).

* * *

**1 **https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf

**2 **https://en.wikipedia.org/wiki/Consistency_(database_systems)

**3 ** Kleppmann, Martin. Designing Data-Intensive Applications. O’Reilly, 2017, p. 329.

**4 **Kleppmann, Martin. Designing Data-Intensive Applications. O’Reilly, 2017, p. 329.

**5 ** https://en.wikipedia.org/wiki/Strong_consistency

**6 **Kleppmann, Martin. Designing Data-Intensive Applications. O’Reilly, 2017, p. 322.

**7 **Kleppmann, Martin. Designing Data-Intensive Applications. O'Reilly, 2017, p. 246.