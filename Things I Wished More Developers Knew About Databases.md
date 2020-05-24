Things I Wished More Developers Knew About Databases

#### Top highlight

# Things I Wished More Developers Knew About Databases

[![1*O8Ky4z8o_t8K0EwfnJ-M1A.jpeg](../_resources/94ceae5fa98a8c82d727b125bd3cf7cc.jpg)](https://medium.com/@rakyll?source=post_page-----2d0178464f78----------------------)

[Jaana B. Dogan](https://medium.com/@rakyll?source=post_page-----2d0178464f78----------------------)

[Apr 21](https://medium.com/@rakyll/things-i-wished-more-developers-knew-about-databases-2d0178464f78?source=post_page-----2d0178464f78----------------------) · 19 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='181'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='182' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/2d0178464f78/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='190'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='191' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/2d0178464f78/share/facebook?source=post_actions_header---------------------------)

A large majority of computer systems have some state and are likely to depend on a storage system. My knowledge on databases accumulated over time, but along the way our design mistakes caused data loss and outages. In data-heavy systems, databases are at the core of system design goals and tradeoffs. Even though it is impossible to ignore how databases work, the problems that application developers foresee and experience will often be just the tip of the iceberg. In this series, I’m sharing a few insights I specifically found useful for developers who are not specialized in this domain.

1. You are lucky if 99.999% of the time network is not  a problem.
2. ACID has many meanings.
3. Each database has different consistency and isolation capabilities.
4. Optimistic locking is an option when you can’t hold a lock.
5. There are anomalies other than dirty reads and data loss.
6. My database and I don’t always agree on ordering.
7. Application-level sharding can live outside the application.
8. AUTOINCREMENT’ing can be harmful.
9. Stale data can be useful and lock-free.
10. Clock skews happen between any clock sources.
11. Latency has many meanings.
12. Evaluate performance requirements per transaction.
13. Nested transactions can be harmful.
14. Transactions shouldn’t maintain application state.
15. Query planners can tell a lot about databases.
16. Online migrations are complex but possible.
17. Significant database growth introduces unpredictability.

*Thanks much to Emmanuel Odeke, Rein Henrichs and others for their review and feedback on an earlier version this article.*

## You are lucky if 99.999% of the time network is not a problem.

It’s an open debate how reliable today’s networking is and how commonly systems experience downtime because of networking outages. The available research is limited and is often dominated by large organizations who have dedicated networking with custom hardware, as well as specialized staff.

With 99.999% service availability, Google cites only [7.6%](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45855.pdf) of Spanner (Google’s globally distributed database) issues are caused by networking even though it keeps crediting its dedicated networking as a core reason behind its availability. [Bailis’ and Kingsbury’s survey](https://cacm.acm.org/magazines/2014/9/177925-the-network-is-reliable/fulltext) from 2014 is challenging one of the [Fallacies of Distributed Computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) coined by Peter Deutsch in 1994. Is network really reliable?

We don’t have comprehensive survey outside of giants or over the public Internet. There is also not enough data from major providers how much of their customers issues can be traced back to networking problems. We often experience outages in large cloud provider’s networking stack can take parts of the Internet down for hours but these are only the high-impact events where a large number of visible customers are impacted. Networking outages might be affecting more cases even though not all events are making much noise. Cloud customers don’t necessarily have visibility into their problems either. When there is an outage, identifying it as a networking error caused in the provider is not possible. To them, third-party services are black boxes. Estimating the impact without being a major provider is not possible.

In comparison to what major players report on their systems, it might be safe to say you are lucky if networking issues represents a small percentage of your potential problems that cause outage. Networking still suffer from conventional issues such as hardware failures, topology changes, administrative configuration changes and power failures. But I recently learned that newly discovered problems such as [SHARK BITES](https://twitter.com/rakyll/status/1249891472993693696) (yes, shark bites) are a reality.

## ACID has many meanings.

ACID stands for atomicity, consistency, isolation, durability. These are the properties database transactions need to guarantee to their users for validity even in the event of crash, error, hardware failures and similar. Without ACID or similar contracts, application developers wouldn’t have a guidance on what’s their responsibility versus what the databases provide. Most relational transactional databases are trying to be ACID-compliant, but new approaches such as NoSQL movement gave birth to many databases without ACID transactions because they are expensive to implement.

When I was new in the industry, our tech lead was arguing whether ACID is an obsolete concept or not. It is fair to say ACID is considered a loose description instead of a strict implementation standard. Today, I find it mostly useful because it provides a category of problems (and a category of possible solutions).

NOT every database is ACID-compliant and among ACID-compliant databases, ACID can be interpreted differently. One of the reasons why ACID is implemented differently is the number of tradeoffs involved in implementing ACID capabilities. Databases might advertise themselves as ACID but might still have different interpretation in edge cases or how they handle “unlikely” events. Developers can at least learn at a high-level how databases implement things in order to have a proper understanding of fail modes and design tradeoffs.

One well-known debate is how ACID MongoDB is even after v4. MongoDB didn’t have [journaling](https://www.mongodb.com/blog/post/what-about-durability) support for a long time even though it was not committing data files to disk not more frequently (every 60 seconds) by default. Consider the following scenario, application makes two writes (w1 and w2). MongoDB was able to persist the change for the first write, but it fails to do it for w2 because it crashes due to a hardware failure.

![1*PT3Xi-fBznMiYtH9_EmJUA.png](../_resources/bc63a4ded615ff5349a8f3d9d0a8c031.png)
![1*2QPkOUcin02S3zX9BDz3qw.png](../_resources/bf9d91f7afbd9127909642296d7eb1ba.png)

An illustration of data loss if MongoDB crashes before it writes to the physical disk.

Committing to disk is an expensive process and by avoiding commits, they were claiming to be performant in writes while sacrificing durability. As of today, MongoDB has journaling but dirty writes still can affect the durability of data because they are committing journals at every 100ms by default. The same scenario is still possible for the durability of the journals and changes represented in those logs even though the risk is significantly less.

## Each database has different consistency and isolation capabilities.

Among ACID properties, consistency and isolation have the widest spectrum of different implementation details because the spectrum of tradeoffs is wider. Consistency and isolation are expensive capabilities. They require coordination and are increasing contention in order to keep data consistent. When having to horizontally scale among data centers (especially among different geographic regions), the problems become significantly harder. Providing high levels of consistency can be extremely hard as availability decreases and networking partitions happen more often. See the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) for a more general explanation of this phenomena. It is worth to also note that applications can handle a bit of inconsistency or programmers might have enough insights about the problem to add additional logic in the application to handle it without heavily relying on their database.

Databases often provide a variety of isolation layers so the application developers can pick the most cost effective one based on their tradeoffs. Weaker isolation can be faster but may introduce data races. Stronger isolation eliminates some potential data races but will be slower and might introduce contention that will slow down the database to a point it may cause outages.

[  ![1*x95aVFq-wMB6VrI9AD4k8Q.png](../_resources/f7acc419ddb33efe4dd3701acc21cad3.png) ![1*x95aVFq-wMB6VrI9AD4k8Q.png](../_resources/5059d3269aa8a9026c90c3fdc0ff31f6.png)](https://jepsen.io/consistency)

An overview of the existing concurrency models and the relationships between them.

The SQL standard only defines four isolation levels even though there are more levels theoretically and practically available. [jepson.io](https://jepsen.io/consistency) provides a compelling overview of the existing concurrency models if you need further reading. For example, Google’s Spanner guarantee external serializability with clock synchronization and even though this is a stricter isolation layer, it is not defined in the standard isolation layers.

The isolation levels mentioned in the SQL standard are:

- **Serializable** (most strict, expensive): A serializable execution produces the same effect as some serial execution of those transactions. A serial execution is one in which each transaction executes to completion before the next transaction begins. One note about *Serializable* level is that it is often implemented as “snapshot isolation” (e.g. Oracle) due to differences in interpretation and “snapshot isolation” is not represented in the SQL standard.
- **Repeatable reads**: Uncommitted reads in the current transaction are visible to the current transaction but changes made by other transactions (such as newly inserted rows) won’t be visible.
- **Read committed**: Uncommitted reads are not visible to the transactions. Only committed writes are visible but the phantom reads may happen. If another transaction inserts and commits new rows, the current transaction can see them when querying.
- **Read uncommitted** (least strict, cheap): Dirty reads are allowed, transactions can see not-yet-committed changes made by other transactions. In practice, this level could be useful to return approximate aggregates, such as COUNT(*) queries on a table.

Serializable level allows least opportunities for data races to happen although being the most expensive and introduces the most contention to the system. Other isolation levels are cheaper but increases the possibility of data races. Some databases allow you to set your isolation level, some databases are more opinionated about them and not necessarily supporting all of them.

Even though databases advertise their support for these isolation levels, a careful examination of their behavior may provide more insights on what the actually do.

![1*UUEYw0PyXpyGFcT9OsDeuA.png](../_resources/41b70e3550f20482710c03557aff54e6.png)
![1*UUEYw0PyXpyGFcT9OsDeuA.png](../_resources/dfdb14f642ce4abaa77a279be65ae129.png)

An overview of concurrency anomalies at different isolation levels per database.

Martin Kleppmann’s [hermitage](https://github.com/ept/hermitage) provides an overview of different concurrency anomalies and whether a database is able to handle it at a particular isolation level. Kleppmann’s research shows how isolation levels can be interpreted differently by database designers.

## Optimistic locking is an option when you can’t hold a lock.

Locks can be extremely expensive not only because they introduce more contention in your database but they might require consistent connections from your application servers to the database. Exclusive locks can be effected by network partitions more significantly and cause deadlocks that are hard to identify and resolve. In cases where being able to hold exclusive locks is not easy, optimistic locking is an option.

[Optimistic locking](https://convincedcoder.com/2018/09/01/Optimistic-pessimistic-locking-sql/#optimistic-locking-using-where) is a method when you read a row, you take note of a version number, last modified timestamps or its checksum. Then you can check the version hasn’t changed atomically before you mutate the record.

UPDATE products
SET name = 'Telegraph receiver', version = 2
WHERE id = 1 AND version = 1

Update to products table is going to affect 0 rows if another update has changed this row earlier. If no earlier updates have been done, it will affect 1 row and we can tell our update has succeeded.

## There are anomalies other than dirty reads and data loss.

When we are talking about data consistency, we primarily pay a lot of attention to possible race conditions that can lead to dirty reads and data loss. But anomalies with data are not just limited to them.

An example of this type of anomalies is write skews. Write skews are harder to identify because we are not actively looking for them. Write skews are caused not when dirty reads happen on writes or lost but logical constraints on data is compromised.

For example, assume a monitoring application that requires one person among their operators to be oncall all the times.

BEGIN tx1; BEGIN tx2;SELECT COUNT(*)
FROM operators
WHERE oncall = true;
0 SELECT COUNT(*)
FROM operators
WHERE oncall = TRUE;
0UPDATE operators UPDATE operators
SET oncall = TRUE SET oncall = TRUE
WHERE userId = 4; WHERE userId = 2;COMMIT tx1; COMMIT tx2;

In the situation above, there will be a write skew if two of the transactions successfully commit. Even though no dirty read or data loss happened, the integrity of data is lost because there are two people assigned to be oncall.

Serializable isolation, schema design or database constraints can be helpful to eliminate write skews. Developers need to be able to identify such anomalies during development to avoid data anomalies in production. Having said that, identifying write skews in code bases can be extremely hard. Especially in large systems, if different teams are responsible for building features based on same tables without talking to each other and examining how they access the data.

## My database and I don’t always agree on ordering.

One of the core capabilities databases offer is the ordering guarantees but ordering may be surprising to the application developer. Databases see transactions in the order they receive them not in the programming order developers see them. The order of the transaction execution is hard to predict especially in high-volume concurrent systems.

In development time, especially when working with non-blocking libraries, poor style and readability may contribute to the problem where users think transactions are executed sequentially even though they can arrive at the database at any order. The program below makes it look like T1 and T2 are going to be invoked sequentially, but if these functions are non-blocking and return immediately with a promise, the order of the invocation will be up to the time they have received at the database.

result1 = T1() // results are actually promises
result2 = T2()

If atomicity is required (to either fully commit or abort all operations) and the sequence matter, the operations in T1 and T2 should run in a single database transaction.

## Application-level sharding can live outside the application.

Sharding is a way to horizontally partition your database. Even though some databases can automatically partition data horizontally, some don’t or may not be good at it. When data architects/developers can predict how data is going to be accessed, they might create horizontal partitions at the user-land instead of delegating this work to their database. This is called application-level sharding.

The name, application-level sharding, often gives the wrong impression that sharding should live in the application services. Sharding capabilities can be implemented as a layer in front of your database. Depending on data growth and schema iterations, sharding requirements might get complicated. Being able to iterate on some strategies without having to redeploy application servers may be useful.

![1*8_yDPQbGxMb7Zv_UBs4pTQ.png](../_resources/1bfaa925f45206030defb6e0468d5928.png)
![1*8_yDPQbGxMb7Zv_UBs4pTQ.png](../_resources/db08e6a6cc8672ba23965c1a1ad4946f.png)

An example architecture where application servers are decoupled from the sharding service..

Having sharding as a separate service can increase your capabilities on iterating on sharding strategies without having to redeploy your applications. One such example of an application-level sharding system is [Vitess](https://youtu.be/OCS45iy5v1M?t=204). Vitess provides horizontal sharding for MySQL and allows clients to connect to it via the MySQL protocol and it shards the data on various MySQL nodes that don’t know about each other.

## AUTOINCREMENT’ing can be harmful.

AUTOINCREMENT’ing is a common way of generating primary keys. It’s not uncommon to see cases where databases are used as ID generators and there are ID-generation designated tables in a database. There are a few reasons why generating primary keys via auto-incrementing may not be not ideal:

- In distributed database systems, auto-incrementing is a hard problem. A global lock would be needed to be able to generate an ID. If you can generate a UUID instead, it would not require any collaboration between database nodes. Auto-incrementing with locks may introduce contention and may significantly downgrade the performance for insertions in distributed situations. Some databases like MySQL may require specific [configuration](https://www.percona.com/blog/2011/01/12/conflict-avoidance-with-auto_increment_incremen-and-auto_increment_offset/) and more attention to get things right in master-master replication. The configuration is easy to mess up and can lead to write outages.
- Some databases have partitioning algorithms based on primary keys. Sequential IDs may cause unpredictable hotspots and may overwhelm some partitions while others stay idle.
- The fastest way to access to a row in a database is by its primary key. If you have better ways to identify records, sequential IDs may make the most significant column in tables a meaningless value. Please pick a globally unique natural primary key (e.g. a username) where possible.

Please consider the impacts of auto-incremented IDs vs UUIDs on indexing, partitioning and sharding before you decide on what works better for you.

## Stale data can be useful and lock-free.

Multi-version concurrency control (MVCC) enables a lot of the consistency features we briefly discussed above. Some databases (e.g. Postgres, Spanner) uses MVCC to allow each transaction to see a snapshot, an older version of the database. Transactions against snapshots still can be serializable for consistency. When reading from an old snapshot, you read stale data.

Reading slightly stale data would be useful, for example when you are generating analytics from your data or calculating approximate aggregate values.

The first advantage of reading stale data would be latency (especially if your database is distributed among different geographical regions). The second advantage of a MVCC database is that it would allow read-only transactions to to be lock-free. A major advantage in a read-heavy application if the stale data can be tolerated.

![1*ePJGd32VU4esxofh5LP69Q.png](../_resources/345fe59462ef52c6708ab20f68279834.png)
![1*ePJGd32VU4esxofh5LP69Q.png](../_resources/d861b8c6e576424956c72422790b2521.png)

Application server reads 5-second old stale data from local replica even though the latest version is available on the other side of the Pacific Ocean.

Databases sweep the old versions automatically and in some cases, they allow you to do that on demand. For example, Postgres allows users to `VACUUM` on demand as well as automatically vacuuming once a while, and Spanner runs a garbage collector to get rid of the versions older than an hour.

## Clock skews happen between any clock sources.

The most well-hidden secret in computing is that all time APIs lie. Our machines don’t accurately know what the current time is. Our computers all contain a quartz crystal that produces a signal to tick time. But quartz crystals can’t accurately tick and drift in time, either faster or slower than the actual clock. Drift could be up to 20 seconds a day. The time on our computers need to be synchronized by the actual time every now and then for accuracy.

NTP servers are used for synchronization but synchronization itself could be delayed due to network. When synchronizing with an NTP server in the same data center can take time, syncing with a public NTP server may cause more skew.

Atomic and GPS clocks are better sources to determine the current time but they are expensive and need complicated setup that they cannot be installed on every machine. Given the limitations, in data centers, a multi-tiered approach is used. While atomic and/or GPS clocks are providing accurate timing, their time is broadcasted to the rest of the machines via secondary servers. This means every machine will be drifted from the actual current time with some magnitude.

There is more… Applications and databases often live in different machines (if not in different centers). Not just that database nodes distributed in a few machines won’t be able to agree on what the time is, application server clock and a database node clock won’t agree either.

Google’s TrueTime is following a different approach here. Most people think Google’s progress in clocks can be attributed to their use of atomic and GPS clocks, but that’s only the part of the story. This is what TrueTime does:

- TrueTime uses two different sources: GPS and atomic clocks. These clocks have different fail modes, hence using both of them is increasing the reliability.
- TrueTime has an unconventional API. It returns the time as an interval. The time could be in fact anywhere between the lower bound and the upper bound. Google’s distributed database Spanner then can wait until it is certain the current time is beyond a particular time. This method adds some latency to the system especially when the uncertainty advertised by masters are high but provides correctness even in a globally distributed situation.

![1*2QPkOUcin02S3zX9BDz3qw.png](../_resources/13e2be42f6e3a2427357887a37183d8e.png)
![1*PT3Xi-fBznMiYtH9_EmJUA.png](../_resources/16dfd31cb8a523b3b0344f9e2bd365f4.png)

Spanner components use TrueTime where TT.now() returns an interval, so Spanner can inject sleeps to ensure the current time has passed a particular timestamp.

As the confidence on the current time decreases, it means Spanner operations might take more time. This is why even though having accurate clocks would be impossible, it is still important to keep the confidence high for performance.

## Latency has many meanings.

If you ask ten people in a room what “latency” means, they may all have different answers. In databases, latency is often referred to “database latency” but not the latency client perceives. Client will see a latency of database latency and network latency. Being able to identify client and database latency is critical when debugging escalating problems. When collecting and displaying metrics, always consider having both.

## Evaluate performance requirements per transaction.

Sometimes databases advertise their performance characteristics and limitations in terms of write and read throughput and latency. Although this may give a high level overview of the major blockers, when evaluating a new database for performance, a more comprehensive approach is to evaluate critical operations (per query and/or per transaction) separately. Examples:

- Write throughput and latency when inserting a new row in to table X (with 50M rows) with given constraints and populating rows in related tables.
- Latency when querying the friends of friends of a user when average number of friends is 500.
- Latency of retrieving the top 100 records for the user timeline when user is subscribed to 500 accounts which has X entries per hour.

Evaluation and experimentation might contain such critical cases until you are confident that a database will be able to serve your performance requirements. A similar thumb of rule is also considering this breakdown when collecting latency metrics and setting SLOs.

Be careful about high cardinality when collecting metrics per operation. Use logs, even collection or distributed tracing if you need high cardinality debugging data. See [Want to Debug Latency?](https://medium.com/observability/want-to-debug-latency-7aa48ecbe8f7) for an overview on latency debugging methodologies.

## Nested transactions can be harmful.

Not every database supports nested transactions but when they do, nested transactions may cause surprising programming errors that are not always easy to identify until it becomes clear that you are seeing anomalies.

If you’d like to avoid nested transactions, client libraries can do work to detect and avoid nested transactions. If you can’t avoid them, you have to pay attention to avoid ending up surprising situations where committed transactions are accidentally aborted due to a child transaction.

Encapsulating transactions in different layers can contribute to surprising nested transaction cases and from a readability point-of-view, it might be hard to understand the intend. Take a look at the following program:

with newTransaction():
Accounts.create("609-543-222") with newTransaction():
Accounts.create("775-988-322")
throw Rollback();

What’s going to be the result of the code above? Is it going to rollback both of the transactions or only the inner one? What happens if we were relying on multiple layers of libraries that were encapsulating the transaction creation from us. Would we be able to identify and improve such cases?

Imagine a data-layer with several operations (e.g. newAccount) already is implemented in their own transactions. What happens when you run them in higher level business logic that runs in it own transaction? What would be the isolation and consistency characteristics would be?

function newAccount(id string) {
with newTransaction():
Accounts.create(id)
}

Instead of dealing with such open-ended questions, avoid nested transactions. Your data layer can still implement high level operations without creating their own transactions. Then, business logic can start transactions, run the operations on the transaction, commit or abort.

function newAccount(id string) {
Accounts.create(id)
}// In main application:with newTransaction():
// Read some data from database for configuration.
// Generate an ID from the ID service.
Accounts.create(id) Uploads.create(id) // create upload queue for the user.

## Transactions shouldn’t maintain application state.

Application developers might want to use application state in transactions to update certain values or tweaks the query parameters. One critical thing to consider is to having the scope right. Clients often retry the transactions when networking issues happen. If a transaction is relying on state that is mutated elsewhere, it might pick the wrong value depending on the possibility of the data races in the problem. Transactions should be careful about in-application data races.

var seq int64with newTransaction():
newSeq := atomic.Increment(&seq)
Entries.query(newSeq) // Other operations...

The transaction above will increase the sequence number each time it runs regardless of its end result. If commit fails due to network, on the second retry, it will query with a different sequence number.

## Query planners can tell about databases.

Query planners determine how your query is going to be executed in the database. They also analyze the queries and optimize them before running. Planners can only provide some possible estimations based on signals it has. How to tell how to find the results for the following query:

SELECT * FROM articles where author = "rakyll" order by title;
There are two ways to retrieve the results:

- **Full table scan**: We can go through every entry on the table and return the articles where author name is matching, then order.
- **Index scan**: We can use an index to find the matching IDs, retrieve those rows and then order.

Query planner’s role is to determine which strategy is the best option. Query planners have limited signals about what they can predict and might result in poor decisions. DBAs or developers can use them to diagnose and fine tune poorly performing queries. New releases of databases can tweak query planners and self-diagnosing them can help you when upgrading your database if new version introduces performance problems. Reports such as the slow query logs, latency problems, or stats on execution times could be useful to determine the queries to optimize.

Some metrics the query planner provides could be noisy, especially when it estimates latency or CPU time. As a supplement to query planners, tracing and execution path tools can be more useful to diagnose these issues even though not every database provides such tools.

## Online migrations are complex but possible.

Online, realtime or live migrations mean migrating from one database to another without downtime and compromising data correctness. Live migrations are easier if you you are migrating to the same database/engine, but can get more complicated when migrating to a new database with different performance characteristics and schema requirements.

There are different models when it comes to online migrations, here is [one](http://www.aviransplace.com/2015/12/15/safe-database-migration-pattern-without-downtime/#ixzz3vsEunxmA):

- Start doing dual writes to both databases. At this stage, new database won’t have all the data but will start seeing the new ones. Once you are confident about this step, you can move on to the second.
- Start enabling the read path to use both databases.
- Use the new database primarily for reads and writes.
- Stop writing to the old database although keep reading from the old database. At this point, new database still doesn’t have all the new data and you might need to fallback to the old database for old records.
- At this point, old database is read-only. Backfill the new database with the missing data from the old database. Once migration is complete, all the read and write paths can use the new database and the old database can be removed from your system.

If you need more caste studies, see Stripe‘s comprehensive [article](https://stripe.com/blog/online-migrations) on their migration strategy that follows this model.

## Significant database growth introduces unpredictability.

Database growth makes you experience unpredictable scale issues. The more we know about the internals of our databases, the less we might predict how they might scale but there are things we can’t predict.

With growth, previous assumptions or expectations on data size and network capacity requirements can become obsolete. This is when large scheme rewrites, large-scale operational improvements, capacity issues, deployment reconsiderations or migrating to other databases happen to avoid outage.

Don’t assume knowing a lot about the internals of your current database is the only thing you need, scale will introduce new unknowns. Unpredictable hotspots, uneven distribution of data, unexpected capacity and hardware problems, ever growing traffic and new network partitions will make you reconsider your database, your data model, your deployment model and the size of your deployment.

—

When I mentioned about potentially publishing this article, I already had five more items on my initial draft. Then, I received an overwhelming amount of new [ideas](https://twitter.com/rakyll/status/1249771259023392768) on what else to capture. I tried keep the scope limited to the least obvious problems that need the most attention. This doesn’t mean I won’t get to write more on this topic and won’t keep updating this document.