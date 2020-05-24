How Does Spanner Avoid Single Point of Failures in Writes?

# How Does Spanner Avoid Single Point of Failures in Writes?

[![1*O8Ky4z8o_t8K0EwfnJ-M1A.jpeg](../_resources/94ceae5fa98a8c82d727b125bd3cf7cc.jpg)](https://medium.com/@rakyll?source=post_page-----4f7765cd894----------------------)

[Jaana Dogan](https://medium.com/@rakyll?source=post_page-----4f7765cd894----------------------)

[May 19](https://medium.com/google-cloud/how-does-spanner-avoid-single-point-of-failures-in-writes-4f7765cd894?source=post_page-----4f7765cd894----------------------) · 7 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='202'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='203' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/4f7765cd894/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='211'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='212' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/4f7765cd894/share/facebook?source=post_actions_header---------------------------)

Google’s [Spanner](https://cloud.google.com/spanner) is a relational database with 99.999% availability which translates to 5 mins of downtime a year. Spanner is a distributed system and can span multiple machines, multiple datacenters (and even geographical regions when configured). It splits the records automatically among its replicas and provides automatic failover. Unlike traditional failover models, Spanner doesn’t failover to a secondary cluster but can elect an available read-write replica as the new leader.

In relational databases, providing both high availability and high consistency in writes is a very hard problem. Spanner’s synchronous replication, and the use dedicated networking and [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) voting provides high availability without compromising consistency.

## High availability of reads vs writes

In traditional relational databases (e.g. MySQL or PostgreSQL), scaling and providing higher availability to reads is easier than writes. Read-only replicas provide a copy of the data read-only transactions can retrieve from. Data is replicated to the read-only replicas from a read-write master either synchronously or asynchronously.

In synchronous models, master synchronously writes to the read replicas at each write. Even though this model ensures that read-only replicas always have the latest data, it makes the writes quite expensive (and causes availability issues for writes) because the master has to write to all available replicas before it returns.

In asynchronous models, read-only replicas get the data from a stream or a replication log. Asynchronous models make writes faster but introduces a lag between the master and the read-only replicas. Users have to tolerate the lag and should be monitoring it to identify replication outages.

![1*mFqYWVw_E65LorCHbAX-GQ.png](../_resources/6069e14ee282458e276e1f968bc38760.png)
![1*mFqYWVw_E65LorCHbAX-GQ.png](../_resources/39ddc5a09d4c9e4c87a33367b6e38bad.png)
Synchronous vs asynchronous replication to read-only replicas.

While scaling reads can be addressed by having more read-only replicas, **scaling masters is a harder problem** without compromising data consistency. If a master fails, other(s) can provide data without users experiencing downtime but [multi-master replication](https://en.wikipedia.org/wiki/Multi-master_replication) is often implemented with asynchronous replication that negatively impacts the overall system by introducing:

- Looser consistency characteristics that violates ACID promises.
- Increased risk of timeouts and communication latency.
- Necessity for conflict resolution between two or more masters if conflicting updates happened but not communicated.

Due to the complexity and the fail modes multi-master replication introduces, it’s not a commonly preferred way of providing high availability in practice.

As an alternative, [high-availability clusters](https://en.wikipedia.org/wiki/High-availability_cluster) are a more popular choice. In this model, you’d have an entire cluster that can take over when the primary master goes down. Today, cloud providers implement this model to provide high availability features for their managed traditional relational database products.

![1*kppaURSo0vDe_qvf0Ycxmw.png](../_resources/aafea7bc117c04b0e3865e344f95ed6d.png)
![1*kppaURSo0vDe_qvf0Ycxmw.png](../_resources/7f34abba76c1ef03572451ef5004ec51.png)

An example model where secondary cluster can take over if primary has an outage, load balancer will point to the secondary and all writes and reads will be served from the secondary.

## Topology

Spanner doesn’t use high availability clusters but approaches to the problem from a different angle. A Spanner cluster* [contains](https://cloud.google.com/spanner/docs/replication#replica_types) multiple read-write, may contain some read-only and some witness replicas.

- Read-write replicas serve reads and writes.
- Read-only replicas serve reads.
- Witnesses don’t serve data but participate in leader election.

Read-only and witness replicas are only used for multi-regional Spanner clusters that can span across multiple geographical regions. Single region clusters only use read-write replicas. Each replica lives in a different zone in the region to avoid single point of failure due to zonal outages.

![1*PqSzVOJoC0qygwRwQAopLw.png](../_resources/a0e843e043a8155c6e0b1aaa29cbbcb8.png)
![1*PqSzVOJoC0qygwRwQAopLw.png](../_resources/9cf1f904077251973d120d7685aade2e.png)

The write is routed to the leader**. Then the write is synchronously replicated to other replicas.

## Splits

Spanner’s replication and sharding capabilities come from its splits. Spanner splits data to replicate and distribute them among the replicas. Split happens [automatically](https://cloud.google.com/spanner/docs/schema-and-data-model#load-based_splitting) when Spanner detects high read or high write load among the records. Each split is replicated and has a **leader replica**.

When a write arrives, we find the split the row is in. Then, we look for the leader of that split and route the write to the leader. This is *true* even in multi-region setups where user is geographically closer to another non-leader read-write replica. In the case of an outage of the leader, an available read-write replica is elected as the leader and user’s write is served from there.

![1*qimBK_B4NPAhmFkbxUEIDQ.png](../_resources/ef6634b3e58d5a4a2bfe6c771dce43fa.png)
![1*qimBK_B4NPAhmFkbxUEIDQ.png](../_resources/87b7d2d18c717c649c6b8f21757ef4d3.png)

Each split is replicated three times and only one of the replicas is the split leader. Each split may be located in a different machine, see [https://cloud.google.com/spanner/docs/whitepapers/life-of-reads-and-writes](https://cloud.google.com/spanner/docs/whitepapers/life-of-reads-and-writes#practical_example).

In order for a write to succeed, a leader need to synchronously replicate the change to the other replicas. But isn’t this impacting the availability of the writes negatively? If writes need to wait for all replicas to succeed, a replica can be a single point of failure because writes wouldn’t succeed until all replicas replicate the change.

This is where Spanner does something better. Spanner only requires *a majority of the Paxos voters to successfully write*. This allows writes to succeed even when a read-write replica goes down. Only the majority of the voters are required not all of the read-write replicas.

## Synchronous replication

As mentioned above, synchronous replication is hard and impacts the availability of the writes negatively. On the other hand when replication happens asynchronously, they cause inconsistencies, conflicts and sometimes data loss. For example, when a master becomes unavailable due to a networking issue, it may still have committed changes but might have not delivered them to the secondary master. If the secondary master updates the same records after a failover, data loss can happen or conflict resolution may be required. PostgreSQL provides [a variety](https://momjian.us/main/writings/pgsql/replication.pdf) of replication models with different tradeoffs. The tradeoffs summary below can give you a very high level idea of how many different concerns to worry about when designing replication models.

![1*Vwpl0Tmf2eqGzKQvPNQeOg.png](../_resources/72edd0a8a498b525a3e409a629c0a144.png)
![1*Vwpl0Tmf2eqGzKQvPNQeOg.png](../_resources/2f1e456e20e5b2df9f63bfb248cbf315.png)

A [summary](https://momjian.us/main/writings/pgsql/replication.pdf) of various PostgreSQL replication models and their tradeoffs.

Spanner’s [replication](https://cloud.google.com/spanner/docs/replication) is *synchronous*. Leaders have to synchronously communicate with other read/write replicas about the change and confirm it in order for a write to succeed.

## Two-phase commit (2PC)

While writes only affecting a single split uses a simpler and faster protocol, if two or more splits are required for a write transaction, [two-phase commit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) (2PC) is executed. 2PC is infamously known as “the anti-availability protocol” because it requires participation from all the replicas and any replica can be a single point of failure. Spanner still serves writes even if some of the replicas are unavailable, because only a majority of voting replicas are required in order to commit a write.

## Network

Spanner is a distributed system and is inherently affected by problems that are impacting distributed systems in general. Networking itself is a factor of outages in distributed systems. On the other hand, Google cites only [7.6%](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45855.pdf)of the Spanner failures were networking related. This is mostly because it runs on Google’s private network. Years of operational maturity, reserved resources, having control over upgrades and hardware makes networking not a significant source of outages. [Eric Brewer’s earlier article](https://cloud.google.com/blog/products/gcp/inside-cloud-spanner-and-the-cap-theorem) explains the role of networking in this case more in detail.

## Colossus

Spanner’s durability guarantees come from Google’s distributed file system, Colossus. Spanner also mitigates some more risk by depending on Colossus. The use of Colossus allows us to have the file storage decoupled from the database service. Spanner is a “shared nothing” architecture and because any server in a cluster can read from Colossus, replicas can recover quickly from whole-machine failures.

Colossus also provides replication and encryption. If a Colossus instance goes down, Spanner can still work on the data via the available Colossus instances. Colossus encrypts data and this is why Spanner provides encryption at rest by default out of the box.

![1*RO68d75Iu_rdYvhJkxSx1g.png](../_resources/56a5f8cc6125941ee2bf78c8c47af52f.png)
![1*RO68d75Iu_rdYvhJkxSx1g.png](../_resources/1942867701e0a9fe5afa44a6a0274c50.png)

Spanner read-write replicas hands off the data to Colossus where data is replicated for 3 times. Given there are three read-write replicas in a Spanner cluster, this means the data is replicated for 9 times.

## Automatic retries

As repeatedly mentioned above, Spanner is a distributed system and is not magic. It experiences more internal aborts and timeouts than traditional databases when writing. A common strategy in distributed systems in order to deal with partial and temporary failures is to retry. Spanner client libraries *provide automatic retries for read/write transactions*. In the following Go snippet, you see the APIs to create a read-write transaction. The client automatically retries the body if it fails due to aborts or conflicts:

import "cloud.google.com/go/spanner"_, err := client.ReadWriteTransaction(ctx, func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {

 **// User code here.**
})

One of the challenges of developing ORM framework support for Google Cloud Spanner was the fact most ORMs didn’t have automatic retries, therefore their APIs didn’t give developers a sense that they shouldn’t maintain any application state in the scope of a transaction. In contrast, Spanner libraries cares a lot of retries and makes an effort to automatically deliver them without creating extra burden to the user.

—

Spanner approaches to sharding and replication differently than traditional relational databases. It utilizes Google’s infrastructure and fine-tunes several traditionally hard problems to provide high availability without compromising consistency.

**Footnotes:**

(*) Google Cloud Spanner’s terminology for a cluster is an instance. I avoided to use “instance” because it is an overloaded term and might mean “replica” for the majority of the readers of this article.

(**) The write is routed to the *split* leader. Read the Splits section for more.

This article is archived at [spanner.fyi/ha-writes](https://spanner.fyi/ha-writes/).