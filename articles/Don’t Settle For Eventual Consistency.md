Don’t Settle For Eventual Consistency

# Don’t Settle For Eventual Consistency

[February 17, 2017](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/)|  [rayokota](https://yokota.blog/author/rayokota/)|

This week Google released Cloud Spanner[1](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-1), a publicly available version of their Spanner database. This completes the public release of their 3 main databases, Bigtable (released as Cloud Bigtable), Megastore (released as Cloud Datastore), and Spanner. Spanner is the culmination of Google’s research in data stores, which provides a globally distributed, relational database that is both strongly consistent and highly available.

But doesn’t the CAP theorem state that we have to choose consistency over availability, or availability over consistency? Over the years, Google has been arguing that you can have both strong consistency and high availability, and that you don’t have to settle for eventual consistency. In fact, all 3 of Google’s data stores are strongly consistent systems.

#### Some Background

In 2000, Brewer came up with the CAP conjecture[2](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-2), which was later proved as a theorem by Gilbert and Lynch[3](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-3). It states that you can choose only 2 of the 3 properties:

- C: consistency (or linearizability)
- A: 100% availability (in the context of network partitions)
- P: tolerance of network partitions

Later Coda Hale made the point that you can’t sacrifice partition tolerance, so really the choice is between CP and AP (and not CA)[4](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-4).

#### What is the tradeoff?

According to the CAP theorem, when you choose a data store, you must choose either an AP system (that is eventually consistent) or a CP system (that is strongly consistent). But Google would argue the following points:

1. In AP systems, client code becomes more complex and error-prone in order to deal with inconsistencies.

2. AP systems are not 100% available in practice.
3. CP systems can be made to be highly available in practice.

4. From the above 3 points, when you choose availability over consistency, you are not gaining 100% availability but you are losing consistency and you are gaining complexity.

Let’s drill down into these points.

#### Client complexity

Here is what Google has to say about using AP systems:

“We also have a lot of experience with eventual consistency systems at Google. In all such systems, we find developers spend a significant fraction of their time building extremely complex and error-prone mechanisms to cope with eventual consistency and handle data that may be out of date. We think this is an unacceptable burden to place on developers and that consistency problems should be solved at the database level.”[5](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-5)

This has led Google to focus on data stores that are CP.

#### AP systems in practice

Many engineers are confused about the definition of “availability” in the CAP theorem. Most engineers think of availability in terms of a service level agreement (SLA) or a service level objective (SLO), which is typically measured in “9s”. However, as Kleppmann has pointed out, the “availability” in the CAP theorem is not a measurement or a metric, but a liveness property of an algorithm.[6](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-6) I am going to distinguish between the two types of availability by referring to them as “effective availability” and “algorithmic availability”.

- Effective availability: the empirically measured percentage of successful requests over some period, often measured in “9s”.
- Algorithmic availability: a liveness property of an algorithm where every request to a non-failing node must eventually return a valid response.

The CAP theorem is only concerned with algorithmic availability.  An algorithmic availability of 100% does not guarantee an effective availability of 100%. The algorithmic availability from the CAP theorem only applies if both the implementation and the execution of the algorithm is without error. In practice, most outages to an AP system are not due to network issues, which the algorithm can handle, but rather to implementation defects, user errors, misconfiguration, resource limits, and misbehaving clients. Google found that in Spanner only 7.6% of its errors were network-related, whereas 52.5% of errors were user-related (such as overload and misconfiguration) and 13.3% of errors were due to bugs. Google actually refers to these errors as “incidents” since they were able to prevent most of them from affecting availability.[7](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-7)

At Yammer we have experience with AP systems, and we’ve seen loss of availability for both Cassandra and Riak for various reasons.  Our AP systems have not been more reliable than our CP systems, yet they have been more difficult to work with and reason about in the presence of inconsistencies.  Other companies have also seen outages with AP systems in production.[8](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-8) So in practice, AP systems are just as susceptible as CP systems to outages due to issues such as human error and buggy code, both on the client side and the server side.

#### CP systems in practice

With Spanner, Google is able to attain an availability of 5 “9s”, which is 5.26 minutes of downtime per year.[7](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-7) Likewise, Facebook uses HBase, another CP system based on Bigtable, and claims to be able to attain an availability of between 4 to 5 “9s”.[9](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-9) In practice, mature CP systems can be made to be highly available. In fact, due to its strong consistency and high availability, Google refers to Spanner as “effectively” CA, which means they are focusing on effective availability (a practical measure) and not algorithmic availability (a theoretical property).

#### A bad tradeoff?

With an AP system, you are giving up consistency, and not really gaining anything in terms of effective availability, the type of availability you really care about.  Some might think you can regain strong consistency in an AP system by using strict quorums (where the number of nodes written + number of nodes read > number of replicas).  Cassandra calls this “tunable consistency”.  However, Kleppmann has shown that even with strict quorums, inconsistencies can result.[10](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-10)  So when choosing (algorithmic) availability over consistency, you are giving up consistency for not much in return, as well as gaining complexity in your clients when they have to deal with inconsistencies.

#### Summary

There’s nothing wrong with using an AP system in general. An AP system might exhibit the lower latencies that you require (such as with a cache), or perhaps your data is immutable so you don’t care as much about strong consistency, or perhaps 99.9% consistency is “good enough”.[11](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fn-517-11) These are all valid reasons for accepting eventual consistency.  However, in practice AP systems are not necessarily more highly available than CP systems, so don’t settle for eventual consistency in order to gain availability. The availability you think you will be getting (effective) is not the availability you will actually get (algorithmic), which will not be as useful as you might think.

* * *

1. D. Srivastava. [Introducing Cloud Spanner: a global database service for mission-critical applications](https://cloudplatform.googleblog.com/2017/02/introducing-Cloud-Spanner-a-global-database-service-for-mission-critical-applications.html), 2017 [[↩](../_resources/0a1b64d0eb2783edb6ef2bcca2b158e8.bin)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-1)

2. E. Brewer. Towards robust distributed systems. Proceedings of the 19th Annual ACM Symposium on Principles of Distributed Computing, Portland, OR, 2000 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-2)

3. S. Gilbert, N. Lynch. Brewer’s conjecture and the feasibility of consistent, available, partition-tolerant web services. ACM SIGACT News 33(2), 2002 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-3)

4. C. Hale. [You Can’t Sacrifice Partition Tolerance](https://codahale.com/you-cant-sacrifice-partition-tolerance/), 2010 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-4)

5.  J. Corbett, J. Dean, M. Epstein, A. Fikes, C. Frost, JJ Furman, S. Ghemawat, A. Gubarev, C. Heiser, P. Hochschild, W. Hsieh, S. Kanthak, E. Kogan, H. Li, A. Lloyd, S. Melnik, D. Mwaura, D. Nagle, S. Quinlan, R. Rao, L. Rolig, Y. Saito, M. Szymaniak, C. Taylor, R. Wang, and D. Woodford. Spanner: Google’s Globally-Distributed Database. Proceedings of OSDI ‘12: Tenth Symposium on Operating System Design and Implementation, Hollywood, CA, October, 2012 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-5)

6. M. Kleppmann. [A Critique of the CAP Theorem](https://arxiv.org/abs/1509.05393), 2015 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-6)

7. E. Brewer. [Spanner, TrueTime, and the CAP Theorem](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45855.pdf), 2017 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-7)  [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/517-7)

8. D. Nadolny. [PagerDuty: One Year of Cassandra Failures](http://www.slideshare.net/planetcassandra/pagerduty-one-year-of-cassandra-failures), 2015 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-8)

9. Z. Fong, R. Shroff. [HydraBase – The evolution of HBase@Facebook](https://code.facebook.com/posts/321111638043166/hydrabase-the-evolution-of-hbase-facebook/), 2014 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-9)

10. M. Kleppmann. Designing Data-Intensive Applications, Chapter 9, p 328, 2017 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-10)

11. P. Bailis, A. Ghodsi. Eventual consistency today: limitations, extensions, and beyond. Commun. ACM 56(5), 55–63, 2013 [(L)](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/#fnref-517-11)

### Share this:

- [Twitter](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/?share=twitter&nb=1)
- [Facebook23](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/?share=facebook&nb=1)
- [Google](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/?share=google-plus-1&nb=1)

-
[Like](https://widgets.wp.com/likes/#)

- [![Richard Startin](../_resources/4cf4a4c02a4b7bdf780f1093dc23c230.jpg)](https://en.gravatar.com/richardstartin)

One blogger likes this.

[Don’t Settle For Eventual Consistency](https://yokota.blog/2017/02/17/dont-settle-for-eventual-consistency/)