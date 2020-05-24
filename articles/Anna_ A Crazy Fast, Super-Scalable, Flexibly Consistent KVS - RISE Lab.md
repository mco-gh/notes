Anna: A Crazy Fast, Super-Scalable, Flexibly Consistent KVS - RISE Lab

# Anna: A Crazy Fast, Super-Scalable, Flexibly Consistent KVS

March 12, 2018[0 Comments](https://rise.cs.berkeley.edu/blog/anna-kvs/#respond)

![Anna's Hummingbird](../_resources/08e3d8f08be836c4859b33a84379d323.jpg)

A native of California, Anna's Hummingbird is the fastest animal alive relative to its size—a record established in [prior research from UC Berkeley](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817121/)

*This article cross-posted from the [DataBeta blog](https://databeta.wordpress.com/2018/03/09/anna-kvs/).*

There's fast and there's fast. This post is about Anna, a key/value database design from our team at Berkeley that's got phenomenal speed and buttery smooth scaling, with an unprecedented range of consistency guarantees. Details are in our [upcoming ICDE18 paper on Anna](http://db.cs.berkeley.edu/jmh/papers/anna_ieee18.pdf). [Conventional wisdom](https://research.google.com/people/jeff/WSDM09-keynote.pdf) (or at least Jeff Dean wisdom) says that you have to redesign your system every time you scale by 10x. As researchers, we asked the counter-cultural question: w*hat would it take to build a key-value store that would excel across many orders of magnitude of scale, from a single multicore box to the global cloud?*

Turns out this kind of curiosity can lead to a system with pretty interesting practical implications.

The key design point for answering our question centered on an ongoing theme in my research group over the last many years: designing distributed systems that avoid coordination. We've developed fundamental theory (the [CALM Theorem](http://db.cs.berkeley.edu/papers/sigrec10-declimperative.pdf)), language design ([Bloom](http://bloom-lang.net/)), program checkers ([Blazes](https://arxiv.org/pdf/1309.3324)), and transactional protocols ([HATs](https://arxiv.org/pdf/1302.0309.pdf), [Invariant Confluence](http://www.vldb.org/pvldb/vol8/p185-bailis.pdf)). But until now we hadn't demonstrated the kind of performance and scale these principles can achieve across both multicore and cloud environments. Consider that domino fallen.

> What would it take to build a key-value store that would excel across many orders of magnitude of scale, from a single multicore box to the global cloud?

*Side-note: Here's what you need to know about coordination. In every computer -- from a multicore chip on your phone to a cloud data center -- many threads of execution are running at once. Almost every piece of software you run wastes enormous time coordinating with other threads to "leave its swimlane" ... usually to modify bits of shared data. If each thread would just "stay in its swimlane", all the threads would run at full speed. Don't let anybody tell you otherwise (including peddlers of so-called "lock-free" data structures): updating shared data requires coordination and is a #GoSlow button for your software.*

Anna offers world-beating speed at many scales. The paper includes numbers showing it beating Redis by over 10x on a single AWS instance, and beating Cassandra by 10x across the globe on a standard interactive benchmark. To get down to the details, we also benchmarked Anna against stronger contenders on a single-node batch request benchmark, to really see how fast it could go at its core task of puts and gets. Here Anna beats the pants off the competition, including comparable "state of the art" performance-oriented KVS systems: it was up to 700x faster than [Masstree](https://pdos.csail.mit.edu/papers/masstree:eurosys12.pdf), up to 800x Intel's "lock-free" [TBB](https://www.threadingbuildingblocks.org/) hash table. In fairness, those systems provide linearizable consistency and Anna does not. But Anna was still up to 126x faster than a "hogwild"-style completely inconsistent C++ hashtable due to cache locality for private state, while providing quite attractive coordination-free consistency. And when you want to scale up to the cloud (which Anna does but those systems cannot), you can't realistically maintain linearizability anyhow. More on Anna's consistency models in a moment.

Anna gets its performance *and* its scalability from its fully coordination-free implementation of simple actors with private state, which only communicate[†](https://rise.cs.berkeley.edu/blog/anna-kvs/#footnote2) via background gossip. Essentially it's a distributed system deployed across cores as well as nodes. Coordination-freeness keeps every actor in its swimlane doing useful work: in high contention workloads we see 90% of Anna's cycles going toward serving requests. For the same workloads, systems like Masstree and Intel TBB get well below 10% of their cycles serving requests—that's because they spend over 90% of their waiting on coordination. However, even for low-contention workloads those systems suffer from processor cache misses due to shared memory.

I like Anna's speed, but what's also interesting is the palette of degrees of consistency Anna can achieve at that speed. A couple years back, we published the [HATs](https://arxiv.org/pdf/1302.0309.pdf) work showing that there is a rich space of distributed consistency and transactional isolation that can (in principle) be achieved coordination-free. This includes fairly rich things like causal consistency or Read Committed transactions. We get this rich consistency in Anna with a very clean codebase, by porting design patterns of [monotone lattice composition from Bloom](http://db.cs.berkeley.edu/papers/socc12-blooml.pdf) to C++. The state of each Anna actor is a monotone lattice composition. Anna is the first system to offer all these consistency levels, and the various choices *differ in only a couple dozen lines of C++ each*. And thank goodness—because simplicity is key to this kind of speed.

Anna is a prototype and we learned a ton doing it. I think the lessons of what we did apply well beyond key-value databases to any distributed system that manages internal state—basically everything. We're now actively working on an extended system, codename Bedrock, based on Anna. Bedrock will provide a hands-off, cost-effective version of this design in the cloud, which we'll be open-sourcing and supporting more aggressively. Watch this space!

Credits:

- [Chenggang Wu](https://github.com/cw75) was the fearless leader and key developer on Anna; [Jose Faleiro](http://www.jmfaleiro.com/) and I were involved in the design. Props to Chenggang!
- Thanks to old friends [Peter Bailis](http://bailis.org/) (of HATs fame) and [Neil Conway](http://www.neilconway.org/) (of Bloom lattice fame) for feedback on this post, which builds directly on their influential earlier work!

* * *

† One thing we did not have to think about much in Anna was fast asynch messaging across cores and nodes—we got this from a lightweight usage of [0MQ](http://zeromq.org/), which is fabulous. Hats off to the 0MQ team