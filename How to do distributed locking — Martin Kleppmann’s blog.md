How to do distributed locking — Martin Kleppmann’s blog

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&ref_src=twsrc%5Etfw&related=martinkl&text=How%20to%20do%20distributed%20locking&tw_p=tweetbutton&url=https%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&via=martinkl)

# How to do distributed locking

Published by Martin Kleppmann on 08 Feb 2016.

As part of the research for [my book](http://dataintensive.net/), I came across an algorithm called [Redlock](http://redis.io/topics/distlock) on the[Redis](http://redis.io/) website. The algorithm claims to implement fault-tolerant distributed locks (or rather,[leases](https://pdfs.semanticscholar.org/a25e/ee836dbd2a5ae680f835309a484c9f39ae4e.pdf) [1]) on top of Redis, and the page asks for feedback from people who are into distributed systems. The algorithm instinctively set off some alarm bells in the back of my mind, so I spent a bit of time thinking about it and writing up these notes.

Since there are already [over 10 independent implementations of Redlock](http://redis.io/topics/distlock) and we don’t know who is already relying on this algorithm, I thought it would be worth sharing my notes publicly. I won’t go into other aspects of Redis, some of which have already been critiqued[elsewhere](https://aphyr.com/tags/Redis).

Before I go into the details of Redlock, let me say that I quite like Redis, and I have successfully used it in production in the past. I think it’s a good fit in situations where you want to share some transient, approximate, fast-changing data between servers, and where it’s not a big deal if you occasionally lose that data for whatever reason. For example, a good use case is maintaining request counters per IP address (for rate limiting purposes) and sets of distinct IP addresses per user ID (for abuse detection).

However, Redis has been gradually making inroads into areas of data management where there are stronger consistency and durability expectations – which worries me, because this is not what Redis is designed for. Arguably, distributed locking is one of those areas. Let’s examine it in some more detail.

## What are you using that lock for?

The purpose of a lock is to ensure that among several nodes that might try to do the same piece of work, only one actually does it (at least only one at a time). That work might be to write some data to a shared storage system, to perform some computation, to call some external API, or suchlike. At a high level, there are two reasons why you might want a lock in a distributed application:[for efficiency or for correctness](http://research.google.com/archive/chubby.html) [2]. To distinguish these cases, you can ask what would happen if the lock failed:

- **Efficiency:** Taking a lock saves you from unnecessarily doing the same work twice (e.g. some expensive computation). If the lock fails and two nodes end up doing the same piece of work, the result is a minor increase in cost (you end up paying 5 cents more to AWS than you otherwise would have) or a minor inconvenience (e.g. a user ends up getting the same email notification twice).

- **Correctness:** Taking a lock prevents concurrent processes from stepping on each others’ toes and messing up the state of your system. If the lock fails and two nodes concurrently work on the same piece of data, the result is a corrupted file, data loss, permanent inconsistency, the wrong dose of a drug administered to a patient, or some other serious problem.

Both are valid cases for wanting a lock, but you need to be very clear about which one of the two you are dealing with.

I will argue that if you are using locks merely for efficiency purposes, it is unnecessary to incur the cost and complexity of Redlock, running 5 Redis servers and checking for a majority to acquire your lock. You are better off just using a single Redis instance, perhaps with asynchronous replication to a secondary instance in case the primary crashes.

If you use a single Redis instance, of course you will drop some locks if the power suddenly goes out on your Redis node, or something else goes wrong. But if you’re only using the locks as an efficiency optimization, and the crashes don’t happen too often, that’s no big deal. This “no big deal” scenario is where Redis shines. At least if you’re relying on a single Redis instance, it is clear to everyone who looks at the system that the locks are approximate, and only to be used for non-critical purposes.

On the other hand, the Redlock algorithm, with its 5 replicas and majority voting, looks at first glance as though it is suitable for situations in which your locking is important for *correctness*. I will argue in the following sections that it is *not* suitable for that purpose. For the rest of this article we will assume that your locks are important for correctness, and that it is a serious bug if two different nodes concurrently believe that they are holding the same lock.

## Protecting a resource with a lock

Let’s leave the particulars of Redlock aside for a moment, and discuss how a distributed lock is used in general (independent of the particular locking algorithm used). It’s important to remember that a lock in a distributed system is not like a mutex in a multi-threaded application. It’s a more complicated beast, due to the problem that different nodes and the network can all fail independently in various ways.

For example, say you have an application in which a client needs to update a file in shared storage (e.g. HDFS or S3). A client first acquires the lock, then reads the file, makes some changes, writes the modified file back, and finally releases the lock. The lock prevents two clients from performing this read-modify-write cycle concurrently, which would result in lost updates. The code might look something like this:

	*// THIS CODE IS BROKEN*
	function writeData(filename, data) {
	    var lock = lockService.acquireLock(filename);
	    if (!lock) {
	        throw 'Failed to acquire lock';
	    }

	    try {
	        var file = storage.readFile(filename);
	        var updated = updateContents(file, data);
	        storage.writeFile(filename, updated);
	    } finally {
	        lock.release();
	    }
	}

Unfortunately, even if you have a perfect lock service, the code above is broken. The following diagram shows how you can end up with corrupted data:

![](../_resources/27f027bdfd7a762b99262dce80dc9e6b.png)

In this example, the client that acquired the lock is paused for an extended period of time while holding the lock – for example because the garbage collector (GC) kicked in. The lock has a timeout (i.e. it is a lease), which is always a good idea (otherwise a crashed client could end up holding a lock forever and never releasing it). However, if the GC pause lasts longer than the lease expiry period, and the client doesn’t realise that it has expired, it may go ahead and make some unsafe change.

This bug is not theoretical: HBase used to [have this problem](http://www.slideshare.net/enissoz/hbase-and-hdfs-understanding-filesystem-usage) [3,4]. Normally, GC pauses are quite short, but “stop-the-world” GC pauses have sometimes been known to last for[several minutes](http://blog.cloudera.com/blog/2011/02/avoiding-full-gcs-in-hbase-with-memstore-local-allocation-buffers-part-1/) [5] – certainly long enough for a lease to expire. Even so-called “concurrent” garbage collectors like the HotSpot JVM’s CMS cannot fully run in parallel with the application code – even they [need to stop the world](https://mechanical-sympathy.blogspot.co.uk/2013/07/java-garbage-collection-distilled.html) from time to time [6].

You cannot fix this problem by inserting a check on the lock expiry just before writing back to storage. Remember that GC can pause a running thread at *any point*, including the point that is maximally inconvenient for you (between the last check and the write operation).

And if you’re feeling smug because your programming language runtime doesn’t have long GC pauses, there are many other reasons why your process might get paused. Maybe your process tried to read an address that is not yet loaded into memory, so it gets a page fault and is paused until the page is loaded from disk. Maybe your disk is actually EBS, and so reading a variable unwittingly turned into a synchronous network request over Amazon’s congested network. Maybe there are many other processes contending for CPU, and you hit a [black node in your scheduler tree](https://twitter.com/aphyr/status/682077908953792512). Maybe someone accidentally sent SIGSTOP to the process. Whatever. Your processes will get paused.

If you still don’t believe me about process pauses, then consider instead that the file-writing request may get delayed in the network before reaching the storage service. Packet networks such as Ethernet and IP may delay packets *arbitrarily*, and [they do](https://queue.acm.org/detail.cfm?id=2655736) [7]: in a famous[incident at GitHub](https://github.com/blog/1364-downtime-last-saturday), packets were delayed in the network for approximately 90 seconds [8]. This means that an application process may send a write request, and it may reach the storage server a minute later when the lease has already expired.

Even in well-managed networks, this kind of thing can happen. You simply cannot make any assumptions about timing, which is why the code above is fundamentally unsafe, no matter what lock service you use.

## Making the lock safe with fencing

The fix for this problem is actually pretty simple: you need to include a *fencing token* with every write request to the storage service. In this context, a fencing token is simply a number that increases (e.g. incremented by the lock service) every time a client acquires the lock. This is illustrated in the following diagram:

![](../_resources/055a89da2e05f6eeda6cd29ba1418c92.png)

Client 1 acquires the lease and gets a token of 33, but then it goes into a long pause and the lease expires. Client 2 acquires the lease, gets a token of 34 (the number always increases), and then sends its write to the storage service, including the token of 34. Later, client 1 comes back to life and sends its write to the storage service, including its token value 33. However, the storage server remembers that it has already processed a write with a higher token number (34), and so it rejects the request with token 33.

Note this requires the storage server to take an active role in checking tokens, and rejecting any writes on which the token has gone backwards. But this is not particularly hard, once you know the trick. And provided that the lock service generates strictly monotonically increasing tokens, this makes the lock safe. For example, if you are using ZooKeeper as lock service, you can use the `zxid`or the znode version number as fencing token, and you’re in good shape [3].

However, this leads us to the first big problem with Redlock: *it does not have any facility for generating fencing tokens*. The algorithm does not produce any number that is guaranteed to increase every time a client acquires a lock. This means that even if the algorithm were otherwise perfect, it would not be safe to use, because you cannot prevent the race condition between clients in the case where one client is paused or its packets are delayed.

And it’s not obvious to me how one would change the Redlock algorithm to start generating fencing tokens. The unique random value it uses does not provide the required monotonicity. Simply keeping a counter on one Redis node would not be sufficient, because that node may fail. Keeping counters on several nodes would mean they would go out of sync. It’s likely that you would need a consensus algorithm just to generate the fencing tokens. (If only [incrementing a counter](https://twitter.com/lindsey/status/575006945213485056) was simple.)

## Using time to solve consensus

The fact that Redlock fails to generate fencing tokens should already be sufficient reason not to use it in situations where correctness depends on the lock. But there are some further problems that are worth discussing.

In the academic literature, the most practical system model for this kind of algorithm is the[asynchronous model with unreliable failure detectors](http://courses.csail.mit.edu/6.852/08/papers/CT96-JACM.pdf) [9]. In plain English, this means that the algorithms make no assumptions about timing: processes may pause for arbitrary lengths of time, packets may be arbitrarily delayed in the network, and clocks may be arbitrarily wrong – and the algorithm is nevertheless expected to do the right thing. Given what we discussed above, these are very reasonable assumptions.

The only purpose for which algorithms may use clocks is to generate timeouts, to avoid waiting forever if a node is down. But timeouts do not have to be accurate: just because a request times out, that doesn’t mean that the other node is definitely down – it could just as well be that there is a large delay in the network, or that your local clock is wrong. When used as a failure detector, timeouts are just a guess that something is wrong. (If they could, distributed algorithms would do without clocks entirely, but then [consensus becomes impossible](https://www.cs.princeton.edu/courses/archive/fall07/cos518/papers/flp.pdf) [10]. Acquiring a lock is like a compare-and-set operation, which [requires consensus](https://cs.brown.edu/~mph/Herlihy91/p124-herlihy.pdf) [11].)

Note that Redis [uses `gettimeofday`](https://github.com/antirez/redis/blob/edd4d555df57dc84265fdfb4ef59a4678832f6da/src/server.c#L390-L404), not a [monotonic clock](https://linux.die.net/man/2/clock_gettime), to determine the [expiry of keys](https://github.com/antirez/redis/blob/f0b168e8944af41c4161249040f01ece227cfc0c/src/db.c#L933-L959). The man page for `gettimeofday`  [explicitly says](https://linux.die.net/man/2/gettimeofday) that the time it returns is subject to discontinuous jumps in system time – that is, it might suddenly jump forwards by a few minutes, or even jump back in time (e.g. if the clock is [stepped by NTP](https://www.eecis.udel.edu/~mills/ntp/html/clock.html) because it differs from a NTP server by too much, or if the clock is manually adjusted by an administrator). Thus, if the system clock is doing weird things, it could easily happen that the expiry of a key in Redis is much faster or much slower than expected.

For algorithms in the asynchronous model this is not a big problem: these algorithms generally ensure that their *safety* properties always hold, [without making any timing assumptions](http://www.net.t-labs.tu-berlin.de/~petr/ADC-07/papers/DLS88.pdf) [12]. Only *liveness* properties depend on timeouts or some other failure detector. In plain English, this means that even if the timings in the system are all over the place (processes pausing, networks delaying, clocks jumping forwards and backwards), the performance of an algorithm might go to hell, but the algorithm will never make an incorrect decision.

However, Redlock is not like this. Its safety depends on a lot of timing assumptions: it assumes that all Redis nodes hold keys for approximately the right length of time before expiring; that the network delay is small compared to the expiry duration; and that process pauses are much shorter than the expiry duration.

## Breaking Redlock with bad timings

Let’s look at some examples to demonstrate Redlock’s reliance on timing assumptions. Say the system has five Redis nodes (A, B, C, D and E), and two clients (1 and 2). What happens if a clock on one of the Redis nodes jumps forward?

1. Client 1 acquires lock on nodes A, B, C. Due to a network issue, D and E cannot be reached.

2. The clock on node C jumps forward, causing the lock to expire.

3. Client 2 acquires lock on nodes C, D, E. Due to a network issue, A and B cannot be reached.

4. Clients 1 and 2 now both believe they hold the lock.

A similar issue could happen if C crashes before persisting the lock to disk, and immediately restarts. For this reason, the Redlock documentation [recommends delaying restarts](http://redis.io/topics/distlock#performance-crash-recovery-and-fsync) of crashed nodes for at least the time-to-live of the longest-lived lock. But this restart delay again relies on a reasonably accurate measurement of time, and would fail if the clock jumps.

Okay, so maybe you think that a clock jump is unrealistic, because you’re very confident in having correctly configured NTP to only ever slew the clock. In that case, let’s look at an example of how a process pause may cause the algorithm to fail:

1. Client 1 requests lock on nodes A, B, C, D, E.

2. While the responses to client 1 are in flight, client 1 goes into stop-the-world GC.

3. Locks expire on all Redis nodes.

4. Client 2 acquires lock on nodes A, B, C, D, E.

5. Client 1 finishes GC, and receives the responses from Redis nodes indicating that it successfully acquired the lock (they were held in client 1’s kernel network buffers while the process was paused).

6. Clients 1 and 2 now both believe they hold the lock.

Note that even though Redis is written in C, and thus doesn’t have GC, that doesn’t help us here: any system in which the *clients* may experience a GC pause has this problem. You can only make this safe by preventing client 1 from performing any operations under the lock after client 2 has acquired the lock, for example using the fencing approach above.

A long network delay can produce the same effect as the process pause. It perhaps depends on your TCP user timeout – if you make the timeout significantly shorter than the Redis TTL, perhaps the delayed network packets would be ignored, but we’d have to look in detail at the TCP implementation to be sure. Also, with the timeout we’re back down to accuracy of time measurement again!

## The synchrony assumptions of Redlock

These examples show that Redlock works correctly only if you assume a *synchronous* system model – that is, a system with the following properties:

- bounded network delay (you can guarantee that packets always arrive within some guaranteed maximum delay),

- bounded process pauses (in other words, hard real-time constraints, which you typically only find in car airbag systems and suchlike), and

- bounded clock error (cross your fingers that you don’t get your time from a [bad NTP server](http://xenia.media.mit.edu/~nelson/research/ntp-survey99/)).

Note that a synchronous model does not mean exactly synchronised clocks: it means you are assuming a [*known, fixed upper bound*](http://www.net.t-labs.tu-berlin.de/~petr/ADC-07/papers/DLS88.pdf) on network delay, pauses and clock drift [12]. Redlock assumes that delays, pauses and drift are all small relative to the time-to-live of a lock; if the timing issues become as large as the time-to-live, the algorithm fails.

In a reasonably well-behaved datacenter environment, the timing assumptions will be satisfied *most*of the time – this is known as a [partially synchronous system](http://www.net.t-labs.tu-berlin.de/~petr/ADC-07/papers/DLS88.pdf) [12]. But is that good enough? As soon as those timing assumptions are broken, Redlock may violate its safety properties, e.g. granting a lease to one client before another has expired. If you’re depending on your lock for correctness, “most of the time” is not enough – you need it to *always* be correct.

There is plenty of evidence that it is not safe to assume a synchronous system model for most practical system environments [7,8]. Keep reminding yourself of the GitHub incident with the[90-second packet delay](https://github.com/blog/1364-downtime-last-saturday). It is unlikely that Redlock would survive a [Jepsen](https://aphyr.com/tags/jepsen) test.

On the other hand, a consensus algorithm designed for a partially synchronous system model (or asynchronous model with failure detector) actually has a chance of working. Raft, Viewstamped Replication, Zab and Paxos all fall in this category. Such an algorithm must let go of all timing assumptions. That’s hard: it’s so tempting to assume networks, processes and clocks are more reliable than they really are. But in the messy reality of distributed systems, you have to be very careful with your assumptions.

## Conclusion

I think the Redlock algorithm is a poor choice because it is “neither fish nor fowl”: it is unnecessarily heavyweight and expensive for efficiency-optimization locks, but it is not sufficiently safe for situations in which correctness depends on the lock.

In particular, the algorithm makes dangerous assumptions about timing and system clocks (essentially assuming a synchronous system with bounded network delay and bounded execution time for operations), and it violates safety properties if those assumptions are not met. Moreover, it lacks a facility for generating fencing tokens (which protect a system against long delays in the network or in paused processes).

If you need locks only on a best-effort basis (as an efficiency optimization, not for correctness), I would recommend sticking with the [straightforward single-node locking algorithm](http://redis.io/commands/set) for Redis (conditional set-if-not-exists to obtain a lock, atomic delete-if-value-matches to release a lock), and documenting very clearly in your code that the locks are only approximate and may occasionally fail. Don’t bother with setting up a cluster of five Redis nodes.

On the other hand, if you need locks for correctness, please don’t use Redlock. Instead, please use a proper consensus system such as [ZooKeeper](https://zookeeper.apache.org/), probably via one of the [Curator recipes](https://curator.apache.org/curator-recipes/index.html)that implements a lock. (At the very least, use a [database with reasonable transactional guarantees](https://www.postgresql.org/).) And please enforce use of fencing tokens on all resource accesses under the lock.

As I said at the beginning, Redis is an excellent tool if you use it correctly. None of the above diminishes the usefulness of Redis for its intended purposes. [Salvatore](http://antirez.com/) has been very dedicated to the project for years, and its success is well deserved. But every tool has limitations, and it is important to know them and to plan accordingly.

If you want to learn more, I explain this topic in greater detail in [chapters 8 and 9 of my book](http://dataintensive.net/), now available in Early Release from O’Reilly. (The diagrams above are taken from my book.) For learning how to use ZooKeeper, I recommend [Junqueira and Reed’s book](http://shop.oreilly.com/product/0636920028901.do) [3]. For a good introduction to the theory of distributed systems, I recommend [Cachin, Guerraoui and Rodrigues’ textbook](http://www.distributedprogramming.net/) [13].

*Thank you to [Kyle Kingsbury](https://aphyr.com/), [Camille Fournier](https://twitter.com/skamille), [Flavio Junqueira](https://twitter.com/fpjunqueira), and[Salvatore Sanfilippo](http://antirez.com/) for reviewing a draft of this article. Any errors are mine, of course.*

**Update 9 Feb 2016:**  [Salvatore](http://antirez.com/), the original author of Redlock, has[posted a rebuttal](http://antirez.com/news/101) to this article (see also[HN discussion](https://news.ycombinator.com/item?id=11065933)). He makes some good points, but I stand by my conclusions. I may elaborate in a follow-up post if I have time, but please form your own opinions – and please consult the references below, many of which have received rigorous academic peer review (unlike either of our blog posts).

## References

[1] Cary G Gray and David R Cheriton: “[Leases: An Efficient Fault-Tolerant Mechanism for Distributed File Cache Consistency](https://pdfs.semanticscholar.org/a25e/ee836dbd2a5ae680f835309a484c9f39ae4e.pdf),” at *12th ACM Symposium on Operating Systems Principles* (SOSP), December 1989.[doi:10.1145/74850.74870](https://dx.doi.org/10.1145/74850.74870)

[2] Mike Burrows: “[The Chubby lock service for loosely-coupled distributed systems](http://research.google.com/archive/chubby.html),” at *7th USENIX Symposium on Operating System Design and Implementation* (OSDI), November 2006.

[3] Flavio P Junqueira and Benjamin Reed:[*ZooKeeper: Distributed Process Coordination*](http://shop.oreilly.com/product/0636920028901.do). O’Reilly Media, November 2013. ISBN: 978-1-4493-6130-3

[4] Enis Söztutar: “[HBase and HDFS: Understanding filesystem usage in HBase](http://www.slideshare.net/enissoz/hbase-and-hdfs-understanding-filesystem-usage),” at *HBaseCon*, June 2013.

[5] Todd Lipcon: “[Avoiding Full GCs in Apache HBase with MemStore-Local Allocation Buffers: Part 1](http://blog.cloudera.com/blog/2011/02/avoiding-full-gcs-in-hbase-with-memstore-local-allocation-buffers-part-1/),” blog.cloudera.com, 24 February 2011.

[6] Martin Thompson: “[Java Garbage Collection Distilled](https://mechanical-sympathy.blogspot.co.uk/2013/07/java-garbage-collection-distilled.html),” mechanical-sympathy.blogspot.co.uk, 16 July 2013.

[7] Peter Bailis and Kyle Kingsbury: “[The Network is Reliable](https://queue.acm.org/detail.cfm?id=2655736),”*ACM Queue*, volume 12, number 7, July 2014.[doi:10.1145/2639988.2639988](https://dx.doi.org/10.1145/2639988.2639988)

[8] Mark Imbriaco: “[Downtime last Saturday](https://github.com/blog/1364-downtime-last-saturday),” github.com, 26 December 2012.

[9] Tushar Deepak Chandra and Sam Toueg: “[Unreliable Failure Detectors for Reliable Distributed Systems](http://courses.csail.mit.edu/6.852/08/papers/CT96-JACM.pdf),”*Journal of the ACM*, volume 43, number 2, pages 225–267, March 1996.[doi:10.1145/226643.226647](https://dx.doi.org/10.1145/226643.226647)

[10] Michael J Fischer, Nancy Lynch, and Michael S Paterson: “[Impossibility of Distributed Consensus with One Faulty Process](https://www.cs.princeton.edu/courses/archive/fall07/cos518/papers/flp.pdf),”*Journal of the ACM*, volume 32, number 2, pages 374–382, April 1985.[doi:10.1145/3149.214121](https://dx.doi.org/10.1145/3149.214121)

[11] Maurice P Herlihy: “[Wait-Free Synchronization](https://cs.brown.edu/~mph/Herlihy91/p124-herlihy.pdf),”*ACM Transactions on Programming Languages and Systems*, volume 13, number 1, pages 124–149, January 1991.[doi:10.1145/114005.102808](https://dx.doi.org/10.1145/114005.102808)

[12] Cynthia Dwork, Nancy Lynch, and Larry Stockmeyer: “[Consensus in the Presence of Partial Synchrony](http://www.net.t-labs.tu-berlin.de/~petr/ADC-07/papers/DLS88.pdf),”*Journal of the ACM*, volume 35, number 2, pages 288–323, April 1988.[doi:10.1145/42282.42283](https://dx.doi.org/10.1145/42282.42283)

[13] Christian Cachin, Rachid Guerraoui, and Luís Rodrigues:[*Introduction to Reliable and Secure Distributed Programming*](http://www.distributedprogramming.net/), Second Edition. Springer, February 2011. ISBN: 978-3-642-15259-7,[doi:10.1007/978-3-642-15260-3](https://dx.doi.org/10.1007/978-3-642-15260-3)

Join the discussion about this article [on Hacker News](https://news.ycombinator.com/item?id=11059738).

Sponsored Links

[(L)](http://insurance.expertsinmoney.com/brilliant-way-to-pay-off-your-funeral?utm_campaign=2174153&utm_content=266745624&cid=5ae98e450587e&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5ae98e450587e-B2C-FP-UK-EiM-May-D&platform=Desktop&utm_term=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2F025_1000x600_81b6d9147d290f1a6af6ddf38ddb89c0.png&network=disqus-widget-safetylevel20longtail09&title=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick)[If You Were Born Before 1950, Funeral Directors Hope You Don't Know This Easy TrickExperts in Money Insurance Quotes](http://insurance.expertsinmoney.com/brilliant-way-to-pay-off-your-funeral?utm_campaign=2174153&utm_content=266745624&cid=5ae98e450587e&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5ae98e450587e-B2C-FP-UK-EiM-May-D&platform=Desktop&utm_term=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2F025_1000x600_81b6d9147d290f1a6af6ddf38ddb89c0.png&network=disqus-widget-safetylevel20longtail09&title=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick)

Undo

[(L)](http://medicalmatters.com/trending/celebrity-kids-clones-same-age/?utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&utm_campaign=2943710&utm_term=Remember+Catherine+Zeta-Jones%27+Daughter%3F+Try+Not+To+Gasp+When+You+See+Her+Now&utm_content=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F67087f41c63bc0c7223bc2c4ce434761.jpg)[Remember Catherine Zeta-Jones' Daughter? Try Not To Gasp When You See Her NowMedical Matters](http://medicalmatters.com/trending/celebrity-kids-clones-same-age/?utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&utm_campaign=2943710&utm_term=Remember+Catherine+Zeta-Jones%27+Daughter%3F+Try+Not+To+Gasp+When+You+See+Her+Now&utm_content=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F67087f41c63bc0c7223bc2c4ce434761.jpg)

Undo

[(L)](https://www.directexpose.com/amazing-bewitched-facts/?utm_source=talas&utm_campaign=Da_TS_DE_UK_D_BewitchedFacts_CTRBlock_v9_2509-The+controversial+Scene+That+Took+%E2%80%98Bewitched%E2%80%99+Off+Air-https%3A%2F%2Fstorage.googleapis.com%2Fcaw-uploads%2Fb0cc1cbaf09138e55afe8e8a92453485.jpeg&utm_term=disqus-widget-safetylevel20longtail09&utm_medium=Da_TS_DE_UK_D_BewitchedFacts_CTRBlock_v9_2509&utm_content=newnext)[The controversial Scene That Took ‘Bewitched’ Off AirDirectExpose](https://www.directexpose.com/amazing-bewitched-facts/?utm_source=talas&utm_campaign=Da_TS_DE_UK_D_BewitchedFacts_CTRBlock_v9_2509-The+controversial+Scene+That+Took+%E2%80%98Bewitched%E2%80%99+Off+Air-https%3A%2F%2Fstorage.googleapis.com%2Fcaw-uploads%2Fb0cc1cbaf09138e55afe8e8a92453485.jpeg&utm_term=disqus-widget-safetylevel20longtail09&utm_medium=Da_TS_DE_UK_D_BewitchedFacts_CTRBlock_v9_2509&utm_content=newnext)

Undo

[(L)](http://laser.lasik-eyes.co.uk/pioneering-laser-eye-surgery?utm_campaign=2134389&utm_content=280429079&cid=5cbf148eb186d&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5cbf148eb186d-B2C-LE-UK-LAS-2-D&platform=Desktop&utm_term=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fle-blonde_1000x600_ad923e34d6eeaa8e482262cebb5a8073.png&network=disqus-widget-safetylevel20longtail09&title=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden)[New Laser Eye Surgery Causing Sensation in CamdenLasik Eyes](http://laser.lasik-eyes.co.uk/pioneering-laser-eye-surgery?utm_campaign=2134389&utm_content=280429079&cid=5cbf148eb186d&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5cbf148eb186d-B2C-LE-UK-LAS-2-D&platform=Desktop&utm_term=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fle-blonde_1000x600_ad923e34d6eeaa8e482262cebb5a8073.png&network=disqus-widget-safetylevel20longtail09&title=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden)

Undo

[(L)](http://www.ancestry.co.uk/s96768/t32729/rd.ashx?utm_source=Taboola&utm_medium=cpc&utm_campaign=96768&utm_content=Do+You+Come+From+Royalty%3F+Your+Last+Name+May+Tell+You._http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F62c76dce56a6991bc902d4c12df33b45.jpg&utm_term=disqus-widget-safetylevel20longtail09)[Do You Come From Royalty? Your Last Name May Tell You.Ancestry](http://www.ancestry.co.uk/s96768/t32729/rd.ashx?utm_source=Taboola&utm_medium=cpc&utm_campaign=96768&utm_content=Do+You+Come+From+Royalty%3F+Your+Last+Name+May+Tell+You._http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F62c76dce56a6991bc902d4c12df33b45.jpg&utm_term=disqus-widget-safetylevel20longtail09)

Undo

[(L)](http://solarpanels.theecoexperts.co.uk/5-reasons-to-install-solar-panels?utm_campaign=2099530&utm_content=281697663&cid=543d2f1d48ce4&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=543d2f1d48ce4-B2C-SP-UK-EE-Cost-D&platform=Desktop&utm_term=Camden%3A+Is+This+The+Newest+Solar+Technology%3F&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fsept_09_1000x600_8b48f468d3caa5108c7bdc0e5a4041d3.png&network=disqus-widget-safetylevel20longtail09&title=Camden%3A+Is+This+The+Newest+Solar+Technology%3F)[Camden: Is This The Newest Solar Technology?TheEcoExperts Solar Quotes](http://solarpanels.theecoexperts.co.uk/5-reasons-to-install-solar-panels?utm_campaign=2099530&utm_content=281697663&cid=543d2f1d48ce4&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=543d2f1d48ce4-B2C-SP-UK-EE-Cost-D&platform=Desktop&utm_term=Camden%3A+Is+This+The+Newest+Solar+Technology%3F&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fsept_09_1000x600_8b48f468d3caa5108c7bdc0e5a4041d3.png&network=disqus-widget-safetylevel20longtail09&title=Camden%3A+Is+This+The+Newest+Solar+Technology%3F)

Undo

- [45 comments]()
- [**Martin Kleppmann's Blog**](https://disqus.com/home/forums/martinkl/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  7](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

[(L)](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/climbsocial/)

 [climbsocial](https://disqus.com/by/climbsocial/)    •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3571487983)

Hi Martin, now that Kafka 0.11 has support for transactions could we use it in some way shape or form for distributed locks? Perhaps using an event sourced pattern where an aggregate tracks who is locking it?

I have a particularly complex use-case where multiple resources are to be locked together for the purpose of a group-related operation, so I'm looking at many different options. Postgres seems like a safe bet, but if I can take advantage of Kafka transactions that would be great.

Thanks for the article!

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* climbsocial](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3571487983)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3572991399)

Not knowing all the details of your requirements it's hard to give an unequivocal answer, but my guess is that Kafka transactions are irrelevant here. The main feature of Kafka transactions is to allow you to atomically publish messages to several topic-partitions. I don't see how that would help you implement a distributed lock.

I am not sure Kafka is really the right tool for this particular purpose, although if you really want to use it, then I would suggest routing all lock requests through a single topic-partition. The monotonically increasing offset that Kafka assigns to messages in a partition could then be used for fencing.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/climbsocial/)

 [climbsocial](https://disqus.com/by/climbsocial/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3572991399)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3575197581)

Thanks Martin! The last part you mentioned is along the lines of what I was thinking: Aggregates would each map to a single topic-partition. A client may then attempt to lock (for correctness) one or more aggregates in a transaction. The assumption is that having "exactly-once" guarantees would help with updating these aggregates together, for example updating their "lockedBy", "lockedAt" properties.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/antirez/)

 [antirez](https://disqus.com/by/antirez/)    •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2507835184)

Note for the readers: that there is an error in the way the Redlock algorithm is used in the blog post: the final step after the majority is acquired, is to check if the total time elapsed is already over the lock TTL, and in such a case the client does not consider the lock as valid. This makes Redlock immune from client <-> lock-server delays in the messages, and makes every other delay *after* the lock validity is tested as any other GC pause during the processing of the locked resource. This is also equivalent to what happens, when using a remote lock server, if the "OK, you have the lock" reply from the server remains in the kernel buffers since the socket pauses before reading it. So where in this blog post its assumed that network delays or GC pauses during the lock acquisition stage are a problem, there is an error.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* antirez](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2507835184)  •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2507868571)

This is correct, I had overlooked that additional clock check after messages are received. However, I believe that the additional check does not substantially alter the properties of the algorithm:

- Large network delay between the application and the shared resource (the thing that is protected by the lock) can still cause the resource to receive a message from an application process that no longer holds the lock, so fencing is still required.
- A GC pause between the final clock check and the resource access will not be caught by the clock check. As I point out in the article: "Remember that GC can pause a running thread at any point, including the point that is maximally inconvenient for you".
- All the dependencies on accuracy of clock measurement still hold.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/antirez/)

 [antirez](https://disqus.com/by/antirez/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2507868571)  •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2507989318)  •  edited

Hello Martin, thanks for your reply. Network delays between the app and the shared resource, and a GC pause *after* the check, but before doing the actual work, are all conceptually exactly the same as the "point 1" of your argument, that is, GC pauses (or other pauses) make the algo require an incremental token. So, regarding the safety of the algorithm itself, the only remaining thing would be the dependency on clock drifts, that can be argued depending on point of view. So I'm sorry to have to say that IMHO the current version of the article, by showing the wrong implementation of the algorithm, and not citing the equivalence of GC pauses processing the shared resource, with GC pauses immediately after the token is acquired, does not provide a fair picture.

            -

                - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/MarutSingh/)

 [MarutSingh](https://disqus.com/by/MarutSingh/)    [*>* antirez](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2507989318)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2829759406)

Bottom line is for an application programmer like me this implementation looks doubtful enough not to use it in production systems. If this does not work perfectly then can introduce bugs which will be impossible to fix.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/dmuth/)

 [Douglas Muth](https://disqus.com/by/dmuth/)    •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2503115182)

"Instead, please use a proper consensus system such as ZooKeeper, probably."
I literally skimmed the entire article for this part. :-)
That said, it's a good writeup, and very informative. Thanks for sharing!

-

Sponsored Links

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_k7E53SgxqG/)

 [李涛](https://disqus.com/by/disqus_k7E53SgxqG/)    •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3420253444)

Today, I learn and think about the "redlock:. I am very agree you!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/yegor256/)

 [Yegor Bugayenko](https://disqus.com/by/yegor256/)    •  [3 months ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4509079795)  •  edited

You may also find [www.stateful.co](http://disq.us/url?url=http%3A%2F%2Fwww.stateful.co%3A2ikNJgJoM530qMfVuUk7Bmk1DMM&cuid=407339) interesting (I'm a developer), which provided free hosted locks for distributed applications. I'm using it in a number of multi-server apps.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/stIncMale/)

 [Valentin Kovalenko](https://disqus.com/by/stIncMale/)    •  [8 months ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4315236175)

Hi Martin ([@Martin Kleppmann](https://disqus.com/by/martinkl/) ), it seems to me that in order for the storage system which is protected by a distributed lock manager (DLM) to be able to participate in fencing, it has to be able to resolve concurrent requests on its own, because it must support the following operation (yes, the whole thing is a single operation, essentially compare-and-set (CAS)):

read the last-seen-fencing-number & compare it with the incoming-fencing-number, store the incoming-fencing-number if it is greater than the last-seen-fencing-number or reject the request with the incoming-fencing-number otherwise.

If a storage system can’t do such an operation, then the system can’t benefit from fencing. But if the system can do this, then such a system is able to resolve concurrent requests on its own because it has CAS, and the DLM becomes completely redundant for correctness purposes for such a system. Am I crazy, or am I correct? :)

It would be very cool if we could clarify this.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_MXWB1KFyVz/)

 [Ben](https://disqus.com/by/disqus_MXWB1KFyVz/)    •  [a year ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4166630576)  •  edited

Can someone explain to me how distributed locks work at all? Let's assume that 2 seperate people on the internet ask two seperate loadbalanced webservers to solve the same problem at the exact same milisecond. Well, both of the web servers ask for a lock at the exact same milisecond. With latency, how can you be certain the lock will be distributed correctly to only one of the resources?

if A asks for a lock and redis sees there is no lock set
and B asks for a lock and redis sees there is no lock set
wouldn't it try to give both of them the lock?

I guess this is where the delay comes in..force a delayed response to ensure you only give the lock to one of them?

Sorry if it sounds noob but I'd love to understand.

I have been solving concurrency problems by pushing all of my actions I want performed into a queue and having a single consumer go through them in order. It works pretty well, but obviously it is relatively slow.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/adrianpetre/)

 [Adrian Petre](https://disqus.com/by/adrianpetre/)    •  [a year ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4116924998)

Please respond to the comment http://disq.us/p/1w33vj3 on Is Redlock safe? ([http://antirez.com/news/101)](http://disq.us/url?url=http%3A%2F%2Fantirez.com%2Fnews%2F101%29%3AhRe4NhygbhyBvUNBvlSBBg30bIQ&cuid=407339),

Thank you!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

This comment was marked as spam.

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Mike S.  [*>* Mike S.](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3839501821)  •  [a year ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3839505928)

...from outdated clocks on locks between commodity box.

-

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/santosh_banerjee/)

 [eternal_solver](https://disqus.com/by/santosh_banerjee/)    •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3779425511)

Great post! Nicely explains the fundamentals of distributed locking from a generic standpoint, besides the Redlock specific details. I stumbled upon this while researching on Curator's distributed locking recipe.

Have you had any experience with that?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* eternal_solver](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3779425511)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3779941256)

I have not used Curator, but a quick look at the docs [https://curator.apache.org/...](https://disq.us/url?url=https%3A%2F%2Fcurator.apache.org%2Fcurator-recipes%2Fshared-lock.html%3ACO-r-sskfzCmKa3TNYIF_ePGd50&cuid=407339) shows that the acquire() method does not return any value that could be used for fencing. That suggests to me that the Curator lock is not safe.

More generally with ZooKeeper you can use the zxid or the version number on the ZNode for fencing. Seems a bit problematic of Curator to not expose that value.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/santosh_banerjee/)

 [eternal_solver](https://disqus.com/by/santosh_banerjee/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3779941256)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3780954046)  •  edited

"More generally with ZooKeeper you can use the zxid or the version number on the ZNode for fencing"

This is indeed similar to what I'm thinking about doing. In fact I'm thinking about having each client create a child znode under a well known znode, say /root/app_name with the name lock_hostName ,where hostName is the name of the physical node hosting the client. At any point in time, there could be just one child underneath /root/app. Then every time, a client successfully acquires a lock, it'd check for existence of children of /root/app. If there's none, the lock is legitimate (in the sense that it was NOT obtained by the current client due to a split brain kind of situation caused by the loss of connectivity of the previous lock owning client with ZK). Under such conditions, the current client can proceed with the work (that can be done by only ONE process at a time), and finally removes the child zNode before releasing the lock. If on the other hand, the client discovers a child under /root/app, it should throw up its arms and generate a FATAL alert, that should probably be resolved with manual intervention.

Sorry for the long post. But, may be you can share some valuable feedback/thoughts on this approach.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_4XL2VvzyaB/)

 [Rick O'Shea](https://disqus.com/by/disqus_4XL2VvzyaB/)    •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3616299450)

Redis works but should be approaches with caution for anything involving more than one instance and even more than one concurrent writer. Simply look at his 5 year odyssey just to implement existing concurrency patterns and even then with limited success. I think if he was honest he would put himself in the category of "creator of stick-figures in crayon" compared to an animator or graphics artist, to use an analogy. I'm guessing it was trial and error since actually understanding the algorithms was a bridge too far. It's just that stick-figures in crayon hit 90% of the initial use-cases, and to be early is sometimes better than being good.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_hAZF2XHFOH/)

 [서지웅](https://disqus.com/by/disqus_hAZF2XHFOH/)    •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3430020292)

great post! may i translate this article to korean?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/hackerwins/)

 [hackerwins](https://disqus.com/by/hackerwins/)    [*>* 서지웅](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3430020292)  •  [a year ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3930963777)

Hi 지웅. I'd like to see your Korean version of this article. Did you translate this?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* 서지웅](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3430020292)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3438258615)

Sure, all articles on this site are licensed under creative commons: [https://creativecommons.org...](https://disq.us/url?url=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby%2F3.0%2F%3AhHH3YfmlMahEiwvB7IuN0L7RiIg&cuid=407339) — you're welcome to translate it, and please include a link back to the original here.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/huaqingli/)

 [Huaqing Li](https://disqus.com/by/huaqingli/)    •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3428581309)

Hi [@Martin Kleppmann](https://disqus.com/by/martinkl/) , there is one confusion I'd like to hear your thoughts about. In the red lock solution, a client is considered to successfully acquire the lock should get locks from the majority of the redis masters(that is at least N/2+1 out of N redis instances). I'm expecting a more clear definition of the 'majority'. As in the scenario where there are 5 redis instances and 3 of them are down, then for all the clients, it is impossible that anyone would get the more than half of the locks. So should we always check how are running redis instances before we acquire a lock? But if so, every client may get different result at different time.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* Huaqing Li](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3428581309)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3438266277)

The definition of "majority" assumes that you know how many redis instances you have (N), which would typically be part of your fixed configuration of the system. Given that you know N, a majority requires that you get votes from more than half of the instances. If 3 out of 5 instances are down, that does not mean N=2; it is still the case that N=5. In this case you will not be able to get the three required votes, and so you will not be able to acquire the lock. You don't need to explicitly check whether an instance is down, because a crashed instance is handled exactly the same way as an instance you cannot reach due to a network problem, or an instance that fails to vote for any other reason.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/huaqingli/)

 [Huaqing Li](https://disqus.com/by/huaqingli/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3438266277)  •  [2 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3440102192)

That makes sense to me. I probably missed something about the solution to it, is it introduced in your article? Thx!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/johnmullaney/)

 [John Mullaney](https://disqus.com/by/johnmullaney/)    •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2904654122)

Why should the fencing token need to be monotonically increasing?

Wouldn't it just need to be different on each operation? E.g., couldn't a UUID be used? The key thing is checking whether the write token value is equal to the current token value. Less-thans and greater-thans wouldn't come into it.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* John Mullaney](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2904654122)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906225078)

The storage system that checks the fencing tokens doesn't know when a new client is granted the lock, it can only go by the token. If you used a UUID and a request turned up with a UUID that has never been seen before, how would the storage system know what to do? Perhaps the lock has been granted to a new client, so the new UUID should be accepted and the old UUID should be blocked. But perhaps the UUID is from a client that acquired the lock and then immediately paused before it was able to make any requests; in that case, a third client will have already acquired the lock, and the previously-unseen UUID should be blocked. Using monotonically increasing fencing tokens solves this conundrum.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/johnmullaney/)

 [John Mullaney](https://disqus.com/by/johnmullaney/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906225078)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906502380)

Thanks, I see. hm... though now I wonder if locks/leases aren't needlessly complex for correctness. If I'm understanding this, the locking assumes the storage system provides (a) a reliable check of a token value coming in with the write request and (b) does the check as part of an atomic check-write operation.

With that, a storage system could ensure correctness without a lock service like this: it maintains a current token value for a resource. A client reads this token value along with the resource. With the write operation the client sends along a two part token: the first part is the original token value and second part is a new unique value. It must be unique so it is a UUID. The storage system, in its check-write atomic operation checks that the first part of the token matches the resource's current token value. If it matches the the second part of the incoming token is written as the new current token value of the resource (along with the rest of the write operation). If it doesn't match, the write fails.

I think that's correctness where the only assumptions are the uniqueness of the tokens provided by the clients with the write operations and the atomicity of the storage service's check-write operation -- no locking/leasing assumed.

???? (It would be very awkward to put question marks at the end of all the sentences, but please take all this as a question!)

The use of a lock/lease system, then, would be to answer the question: is something already intending to modify the resource? (Which is a question of efficiency, of course.)

[see more]()

            -

                - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* John Mullaney](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906502380)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906524301)

What you describe is a viable approach, and it is quite similar to the causal context used in Riak, for example. If all you care about is managing writes to a storage system, you're right that a lock/lease may be overkill.

In general, I'd say that people call for a leasing system if there needs to be one instance of some process for some reason. For example, perhaps you have a process that sends out a bunch of emails, and you only want exactly one instance of that process running (zero instances would mean no emails sent, multiple instances would mean duplicate emails).

In this blog post, I have tried to draw attention to the fact that in the presence of process pauses, you have to think about the interaction between different stateful systems. The nature of these interactions depends on the particulars of your application, of course.

These blog comments aren't really a great medium for such subtle discussion, so for further details I'd like to politely refer you to my book [http://dataintensive.net/](http://disq.us/url?url=http%3A%2F%2Fdataintensive.net%2F%3A4kd0xhkJ6Gv-XYiBpSaIuKhQ2po&cuid=407339) :)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/idelvall/)

 [idelvall](https://disqus.com/by/idelvall/)    •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2896435423)

Great post! But I think a clarification has to be made regarding fencing tokens: What happens in the (unlikely) case that client 2 also suffers a STW pause and they write with increasing successive tokens?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* idelvall](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2896435423)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906226639)

The storage system simply maintains the ‘ratchet’ that the token can only stay the same or increase, but not decrease. Thus, if client 2 pauses and client 3 acquires the lock, client 2 will have a lesser token. If client 3 has already made a request to the storage service, client 1 and 2 will both be blocked.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/idelvall/)

 [idelvall](https://disqus.com/by/idelvall/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906226639)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906334748)  •  edited

what I mean is:
client 1 acquires lock
client 1 stops
client 1 lock expires
client 2 acquires lock
client 2 stops
client 1 resumes and writes to storage
client 2 resumes and writes to storage

This is more unlikely than the scenario you presented, but still possible, and breaks the desired "correctness" since both writes are accepted.

            -

                - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* idelvall](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906334748)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906370031)

Oh, I see what you mean now. Yes, you have a good point — that scenario does look risky. To reason about it properly, I think we would need to make some assumptions about the semantics of the write that occurs under the lock; I think it would probably turn out to be safe in some cases, but unsafe in others. I will think about it some more.

In consensus algorithms that use epochs/ballot numbers/round numbers (which have a similar function to the fencing token), the algorithm works because the type of write is constrained. Thus, Paxos for example can maintain the invariant that if one node decides x, no other node will decide a value other than x, even in the presence of arbitrary pauses. If unconstrained writes were allowed, the safety property could be violated.

Perhaps it would be useful to regard a storage system with fencing token support as participating in an approximation of a consensus algorithm, but further protocol constraints would be required to make it safe in all circumstances?

                -

                    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/idelvall/)

 [idelvall](https://disqus.com/by/idelvall/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906370031)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906513725)  •  edited

After some thinking, this is how I would do it:
In lock manager:

- If since last released lock, no other (later) has been expired, then next returned token is an "ordinary token" (incrementing the previous one)
- Otherwise, the next returned token is a "paired token" containing major/minor information, being major: the current token numbering, and minor: the numbering of the first token not released at this time

In lock-aware resources:

- Keep record of the highest accepted token
- If the current token is ordinary then behave as usual (rejecting when it's not greater than the highest)
- If the current token is paired (granted after some others expiration) then accept only if its minor number is greater than highest known

This would be consistent with my previous example:
-client 1 acquires lock (token: "1")
-client 1 stops
-client 1 lock expires
-client 2 acquires lock (token "2:1", meaning "lock 2 given after 1 expired")
-client 2 stops
-client 1 resumes and writes to storage
-storage accepts token and sets the highest known to "1"
-client 2 resumes and writes to storage
-storage rejects token "2:1" since "1" is not greater than highest ("1")
what do you think?

[see more]()

                    -

                        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/stIncMale/)

 [Valentin Kovalenko](https://disqus.com/by/stIncMale/)    [*>* idelvall](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906513725)  •  [10 months ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4228415526)

This approach means that the storage would reject all requests after the expiration of lock (token: 1) except for the client 1 requests until client 1 explicitly goes and releases the expired lock (token: 1). And this would eliminate the lock expiration idea: despite a lock can expire, the whole system (lock management + the storage) still must wait for it to be released if the owner of the lock made at least one request to the storage.

                        -

                            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/idelvall/)

 [idelvall](https://disqus.com/by/idelvall/)    [*>* Valentin Kovalenko](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4228415526)  •  [10 months ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4229250948)

No, this approach doesn't mean that.

First, let's clarify this idea was made in the context of fencing tokens (locking without making any timing assumptions, accepting a token only based on its value and the value of the previous accepted one).

Once the expiration of the first lock would occur, the locking system would give the lock to client 2 (token 2), but whatever comes first at the write operation would succeed. If 2 comes first, 1 is disabled automatically by the ordinary case (monotonically increasing verification), but if 1 comes first, 2 would be disabled by the new "paired" case

                    -

                        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* idelvall](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906513725)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906529686)

Interesting idea. Seems plausible at first glance, but it's the kind of subtle protocol that would benefit from a formal proof of correctness. In these distributed systems topics it's terribly easy to accidentally overlook some edge-case.

                        -

                            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_99oWdWDvSL/)

 [Jeff Jeff](https://disqus.com/by/disqus_99oWdWDvSL/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906529686)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3183738196)

This actually looks a lot like the algorithm proposed in the paper "On Optimistic Methods for Concurrency Control" by Kung and Robinson, 1981 ([http://www.eecs.harvard.edu...](http://disq.us/url?url=http%3A%2F%2Fwww.eecs.harvard.edu%2F%7Ehtk%2Fpublication%2F1981-tods-kung-robinson.pdf%29%3Ay8BWJX1NcSjkjkEbQajJHdC0nWg&cuid=407339)

I believe that this paper addresses the exact issues that [@idelvall](https://disqus.com/by/idelvall/) mentioned and also includes a formal proof. Additionally, in the case proposed as long as client 1 and client 2 have no conflicts in what they are writing then both would still be permitted, however in this case if there was a conflict then client 2 would be rejected prior to starting its write. Would be interested in hearing your thoughts on this though.

                            -

                                - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                                - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_ZqHiTV1AVL/)

 [AMIT JAIN](https://disqus.com/by/disqus_ZqHiTV1AVL/)    [*>* Jeff Jeff](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3183738196)  •  [3 months ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4524425326)

[http://www.eecs.harvard.edu...](http://disq.us/url?url=http%3A%2F%2Fwww.eecs.harvard.edu%2F%7Ehtk%2Fpublication%2F1981-tods-kung-robinson.pdf%3A1LKTFtjJXGaI58ek0YHwFPMXQe8&cuid=407339)

                            -

                                - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                                - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/adrianpetre/)

 [Adrian Petre](https://disqus.com/by/adrianpetre/)    [*>* Jeff Jeff](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-3183738196)  •  [a year ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-4116706781)

[@Jeff Jeff](https://disqus.com/by/disqus_99oWdWDvSL/)
hi, the link is broken

                        -

                            - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
                            - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/idelvall/)

 [idelvall](https://disqus.com/by/idelvall/)    [*>* Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906529686)  •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2906578124)  •  edited

Agreed, just an idea. I'll take a look into Chubby's paper and see how they handle this

-

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_5HZAVOXC1V/)

 [Jaimie](https://disqus.com/by/disqus_5HZAVOXC1V/)    •  [3 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2653350523)

This is a really good resource if someone is learning for distributed locking. Here's a good example on how to use it in a distributed cache.

[http://blogs.alachisoft.com...](http://disq.us/url?url=http%3A%2F%2Fblogs.alachisoft.com%2Fncache%2Fdistributed-locking%2F%3AGazRe4O8bPh2bCQEvqfwXdxveCM&cuid=407339)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Russell  •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2504270218)

"that that" in paragraph

"However, Redlock is not like this. Its safety depends on a lot of timing assumptions: it assumes that all Redis nodes hold keys for approximately the right length of time before expiring; that that the network delay is small compared to the expiry duration; and that process pauses are much shorter than the expiry duration."

Great article though, I'm just being an editor :P

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/martinkl/)

 [Martin Kleppmann](https://disqus.com/by/martinkl/)  Mod  [*>* Russell](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2504270218)  •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2504353657)

Thanks! Fixed.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Srdjan  •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2504050591)

Great write up. Especially in terms of distilling the theory into examples. Perhaps it would be worth reiterating (in the paragraph before the conclusion) that paxos, raft et al are still safe even if the system degenerates into the async model, but progress is no longer guaranteed (i.e. Likeness)

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Srdjan  [*>* Srdjan](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2504050591)  •  [4 years ago](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html#comment-2504051898)

Autocorrect killed me :) likeness = liveness

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=martinkl&t_i=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_u=http%3A%2F%2Fmartin.kleppmann.com%2F2016%2F02%2F08%2Fhow-to-do-distributed-locking.html&t_d=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&t_t=How%20to%20do%20distributed%20locking%20%E2%80%94%20Martin%20Kleppmann%E2%80%99s%20blog&s_o=default#)
- [*d*](https://publishers.disqus.com/engage?utm_source=martinkl&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)

Sponsored Links

[(L)](http://medicalmatters.com/trending/celebrity-kids-clones-same-age/?utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&utm_campaign=2943710&utm_term=Remember+Catherine+Zeta-Jones%27+Daughter%3F+Try+Not+To+Gasp+When+You+See+Her+Now&utm_content=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F67087f41c63bc0c7223bc2c4ce434761.jpg)[Remember Catherine Zeta-Jones' Daughter? Try Not To Gasp When You See Her NowMedical Matters](http://medicalmatters.com/trending/celebrity-kids-clones-same-age/?utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&utm_campaign=2943710&utm_term=Remember+Catherine+Zeta-Jones%27+Daughter%3F+Try+Not+To+Gasp+When+You+See+Her+Now&utm_content=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F67087f41c63bc0c7223bc2c4ce434761.jpg)

Undo

[(L)](http://www.horizontimes.com/worldwide/lgbt-celebrities?utm_medium=taboola&utm_source=taboola&utm_campaign=ta-ht-lgbt-couples-des-uk-1609&utm_term=disqus-widget-safetylevel20longtail09)[17+ Actors You Didn't Know Were Gay - No. 8 Will Shock WomenHorizontimes](http://www.horizontimes.com/worldwide/lgbt-celebrities?utm_medium=taboola&utm_source=taboola&utm_campaign=ta-ht-lgbt-couples-des-uk-1609&utm_term=disqus-widget-safetylevel20longtail09)

Undo

[(L)](http://www.ancestry.co.uk/s96768/t32729/rd.ashx?utm_source=Taboola&utm_medium=cpc&utm_campaign=96768&utm_content=Do+You+Come+From+Royalty%3F+Your+Last+Name+May+Tell+You._http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F62c76dce56a6991bc902d4c12df33b45.jpg&utm_term=disqus-widget-safetylevel20longtail09)[Do You Come From Royalty? Your Last Name May Tell You.Ancestry](http://www.ancestry.co.uk/s96768/t32729/rd.ashx?utm_source=Taboola&utm_medium=cpc&utm_campaign=96768&utm_content=Do+You+Come+From+Royalty%3F+Your+Last+Name+May+Tell+You._http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F62c76dce56a6991bc902d4c12df33b45.jpg&utm_term=disqus-widget-safetylevel20longtail09)

Undo

[(L)](http://laser.lasik-eyes.co.uk/pioneering-laser-eye-surgery?utm_campaign=2134389&utm_content=280429079&cid=5cbf148eb186d&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5cbf148eb186d-B2C-LE-UK-LAS-2-D&platform=Desktop&utm_term=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fle-blonde_1000x600_ad923e34d6eeaa8e482262cebb5a8073.png&network=disqus-widget-safetylevel20longtail09&title=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden)[New Laser Eye Surgery Causing Sensation in CamdenLasik Eyes](http://laser.lasik-eyes.co.uk/pioneering-laser-eye-surgery?utm_campaign=2134389&utm_content=280429079&cid=5cbf148eb186d&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5cbf148eb186d-B2C-LE-UK-LAS-2-D&platform=Desktop&utm_term=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fle-blonde_1000x600_ad923e34d6eeaa8e482262cebb5a8073.png&network=disqus-widget-safetylevel20longtail09&title=New+Laser+Eye+Surgery+Causing+Sensation+in+Camden)

Undo

[(L)](http://insurance.expertsinmoney.com/brilliant-way-to-pay-off-your-funeral?utm_campaign=2174153&utm_content=266745624&cid=5ae98e450587e&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5ae98e450587e-B2C-FP-UK-EiM-May-D&platform=Desktop&utm_term=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2F025_1000x600_81b6d9147d290f1a6af6ddf38ddb89c0.png&network=disqus-widget-safetylevel20longtail09&title=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick)[If You Were Born Before 1950, Funeral Directors Hope You Don't Know This Easy TrickExperts in Money Insurance Quotes](http://insurance.expertsinmoney.com/brilliant-way-to-pay-off-your-funeral?utm_campaign=2174153&utm_content=266745624&cid=5ae98e450587e&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=5ae98e450587e-B2C-FP-UK-EiM-May-D&platform=Desktop&utm_term=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2F025_1000x600_81b6d9147d290f1a6af6ddf38ddb89c0.png&network=disqus-widget-safetylevel20longtail09&title=If+You+Were+Born+Before+1950%2C+Funeral+Directors+Hope+You+Don%27t+Know+This+Easy+Trick)

Undo

[(L)](http://solarpanels.theecoexperts.co.uk/5-reasons-to-install-solar-panels?utm_campaign=2099530&utm_content=281697663&cid=543d2f1d48ce4&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=543d2f1d48ce4-B2C-SP-UK-EE-Cost-D&platform=Desktop&utm_term=Camden%3A+Is+This+The+Newest+Solar+Technology%3F&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fsept_09_1000x600_8b48f468d3caa5108c7bdc0e5a4041d3.png&network=disqus-widget-safetylevel20longtail09&title=Camden%3A+Is+This+The+Newest+Solar+Technology%3F)[Camden: Is This The Newest Solar Technology?TheEcoExperts Solar Quotes](http://solarpanels.theecoexperts.co.uk/5-reasons-to-install-solar-panels?utm_campaign=2099530&utm_content=281697663&cid=543d2f1d48ce4&utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail09&campaign=543d2f1d48ce4-B2C-SP-UK-EE-Cost-D&platform=Desktop&utm_term=Camden%3A+Is+This+The+Newest+Solar+Technology%3F&utm_content=https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2F44dd7285-cd6a-4a0f-9085-8137587509a3%2Fsept_09_1000x600_8b48f468d3caa5108c7bdc0e5a4041d3.png&network=disqus-widget-safetylevel20longtail09&title=Camden%3A+Is+This+The+Newest+Solar+Technology%3F)

Undo