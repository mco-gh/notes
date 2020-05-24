Introducing Cloud Spanner: a global database service for mission-critical applications

## [Introducing Cloud Spanner: a global database service for mission-critical applications](https://cloudplatform.googleblog.com/2017/02/introducing-Cloud-Spanner-a-global-database-service-for-mission-critical-applications.html)

Tuesday, February 14, 2017
 By Deepti Srivastava, Product Manager for Cloud Spanner

[Cloud Spanner](https://www.youtube.com/watch?v=amcf6W2Xv6M)

Today, we’re excited to announce the public beta for [Cloud Spanner](https://cloud.google.com/spanner/), a globally distributed relational database service that lets customers have their cake and eat it too: [ACID](https://en.wikipedia.org/wiki/ACID) transactions and SQL semantics, without giving up horizontal scaling and high availability.

When building cloud applications, database administrators and developers have been forced to choose between traditional databases that guarantee transactional consistency, or NoSQL databases that offer simple, horizontal scaling and data distribution. Cloud Spanner breaks that dichotomy, offering both of these critical capabilities in a single, fully managed service.

> “*> Cloud Spanner presents tremendous value for our customers who are retailers, manufacturers and wholesale distributors around the world. With its ease of provisioning and scalability, it will accelerate our ability to bring cloud-based omni-channel supply chain solutions to our users around the world*> ,” > —>  John Sarvari, Group Vice President of Technology, > [> JDA](https://jda.com/)

JDA, a retail and supply chain software leader, has used [Google Cloud Platform](https://cloud.google.com/) (GCP) as the basis of its new application development and delivery since 2015 and was an early user of Cloud Spanner. The company saw its potential to handle the explosion of data coming from new information sources such as IoT, while providing the consistency and high availability needed when using this data.

Cloud Spanner rounds out our portfolio of database services on GCP, alongside Cloud SQL, Cloud Datastore and Cloud Bigtable.

As a managed service, Cloud Spanner provides key benefits to DBAs:

- Focus on your application logic instead of spending valuable time managing hardware and software
- Scale out your RDBMS solutions without complex sharding or clustering
- Gain horizontal scaling without migration from relational to NoSQL databases
- Maintain high availability and protect against disaster without needing to engineer a complex replication and failover infrastructure
- Gain integrated security with data-layer encryption, identity and access management and audit logging

With Cloud Spanner, your database scales up and down as needed, and you'll only pay for what you use. It features a simple [pricing model](https://cloud.google.com/spanner/pricing) that charges for compute node-hours, actual storage consumption (no pre-provisioning) and external network access.

Cloud Spanner keeps application development simple by supporting standard tools and languages in a familiar relational database environment. It’s ideal for operational workloads supported by traditional relational databases, including inventory management, financial transactions and control systems, that are outgrowing those systems. It supports distributed transactions, schemas and DDL statements, SQL queries and JDBC drivers and offers client libraries for the most popular languages, including Java, Go, Python and Node.js.

### More Cloud Spanner customers share feedback

Quizlet, an online learning tool that supports more than 20 million students and teachers each month, uses MySQL as its primary database; database performance and stability are critical to the business. But with users growing at roughly 50% a year, Quizlet has been forced to scale its database many times to handle this load. By splitting tables into their own databases (vertical sharding), and moving query load to replicas, it’s been able to increase query capacity — but this technique is reaching its limits quickly, as the tables themselves are outgrowing what a single MySQL shard can support. In its search for a more scalable architecture, Quizlet discovered Cloud Spanner, which will allow it to easily scale its relational database and simplify its application:

> “*> Based on our experience and performance testing, Cloud Spanner is the most compelling option we’ve seen to power a high-scale relational query workload. It has the performance and scalability of a NoSQL database, but can execute SQL so it’s a viable alternative to sharded MySQL. It’s an impressive technology and could dramatically simplify how we manage our databases.*> ” > — > Peter Bakkum, Platform Lead, > [> Quizlet](https://quizlet.com/blog/quizlet-cloud-spanner)

### The history of Spanner

For decades, developers have relied on traditional databases with a relational data model and SQL semantics to build applications that meet business needs. Meanwhile, NoSQL solutions emerged that were great for scale and fast, efficient data-processing, but they didn’t meet the need for strong consistency. Faced with these two sub-optimal choices that customers grapple with today, in 2007, a team of systems researchers and engineers at Google set out to develop a globally-distributed database that could bridge this gap. In 2012, we published the [Spanner research paper](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf) that described many of these innovations. The result was a database that offers the best of both worlds:

|     |
| --- |
| [![cloud-spanner-4.png](../_resources/9f9c23ab7d2b8c5fbf048cc1a1a06ce9.png)](https://4.bp.blogspot.com/-5S2-kW92CXU/WKIW2OzkU6I/AAAAAAAADls/uoCAoxdt2DEPPqC9FEGcl4qbwKsDFNJcQCLcB/s1600/cloud-spanner-4.png) |
| (click to enlarge) |

Remarkably, Cloud Spanner achieves this combination of features without violating the [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem). To understand how, [read this post](https://cloudplatform.googleblog.com/2017/02/inside-Cloud-Spanner-and-the-CAP-Theorem.html) by the author of the CAP Theorem and Google Vice President of Infrastructure, Eric Brewer.

Over the years, we’ve battle-tested Spanner internally with hundreds of different applications and petabytes of data across data centers around the world. At Google, Spanner supports tens of millions of queries per second and runs some of our most critical services, including [AdWords](https://research.google.com/pubs/pub41344.html) and Google Play.

If you have a MySQL or PostgreSQL system that's bursting at the seams, or are struggling with hand-rolled transactions on top of an eventually-consistent database, Cloud Spanner could be the solution you're looking for. Visit the [Cloud Spanner](https://cloud.google.com/spanner/) page to learn more and get started building applications on our next-generation database service.

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

103 comments

[![photo.jpg](../_resources/46d0e580386337d1385bccaa4ac6a5ad.jpg)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg](../_resources/186d06ac1ab64287ea9e7ef6f07d55b1.jpg)](https://apis.google.com/u/0/wm/1/107797272029781254158)

### [Artem Russakovskii](https://apis.google.com/u/0/wm/1/107797272029781254158) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+ArtemRussakovskii/posts/YM17hQ15FfE)  -  Shared publicly

Wow, incredibly impressive. I wish it was available outside of the +[Google Cloud](https://apis.google.com/117105793163182226623) for us mortals.

+
6
2
3
2

 ·
Reply
View all 9 replies

[![photo.jpg](../_resources/f9dc72c14740c04eab142fb76c18d82c.jpg)](https://plus.google.com/+RobBecker)

[Rob Becker](https://plus.google.com/+RobBecker)

[1 month ago](https://apis.google.com/u/0/wm/1/+ArtemRussakovskii/posts/YM17hQ15FfE)

+
1
2
1

I don't think it would ever be just a downloadable bit of software to run yourself. It works because Google has atomic clocks and GPS in all data centers to provide accurate time (according to Wired https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/)

[![photo.jpg.png](../_resources/e276b3c7a964ae1f19c288fe0bbf70e0.png)](https://plus.google.com/113916080900214949310)

[ximena parsons](https://plus.google.com/113916080900214949310)

[2 weeks ago](https://apis.google.com/u/0/wm/1/+ArtemRussakovskii/posts/YM17hQ15FfE)

+
0
1
0

+[Adam Sobotka](https://apis.google.com/103642560023879679157) I agree the transport overhead would be horendous

[![photo.jpg](../_resources/803741b9b988b57ed2e88beadc3bc928.jpg)](https://apis.google.com/u/0/wm/1/106642703522082805470)

### [eDesk HUB](https://apis.google.com/u/0/wm/1/106642703522082805470)

[1 week ago](https://apis.google.com/u/0/wm/1/106642703522082805470/posts/Y4EeaMcmaCU)  -  Shared publicly

Google has introduced a new database service, Cloud Spanner which can easily handle the enormous burst of data from new sources like IoT. Google Cloud Scanner will help organizations in handling SQL semantics without compromising on high availability of data. Enlist on eDesk HUB and win challenging projects in cloud computing domain. Registrations are open. https://goo.gl/kBJDs4  [#eDeskHUB](https://apis.google.com/s/%23eDeskHUB)  [#CloudSpanner](https://apis.google.com/s/%23CloudSpanner)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/bf7a808c230de450aa826caaa560ab15.jpg)](https://apis.google.com/u/0/wm/1/117220853931310837595)

### [Elston Technology Services, LLC](https://apis.google.com/u/0/wm/1/117220853931310837595)

[3 weeks ago](https://apis.google.com/u/0/wm/1/+ElstonTechnologyServicesLLCTempe/posts/DT89z7XH4hp)  -  Shared publicly

Via the wonderful people at Google... Introducing Cloud Spanner: a global database service for mission-critical applications

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/b8a6e8b13818ac951c28d184695b156d.jpg)](https://apis.google.com/u/0/wm/1/109539480056944416389)

### [Kivava Chang](https://apis.google.com/u/0/wm/1/109539480056944416389) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+KivavaChang/posts/6HaygMAWKcp)  -  Shared publicly

Google Cloud Platform Blog: Introducing Cloud Spanner: a global database service for mission-critical applications

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/366fe793d8ced66628aedb84dc2993f3.jpg)](https://plus.google.com/+PawanGuptaPatna)

[JMD Arts](https://plus.google.com/+PawanGuptaPatna)

[1 month ago](https://apis.google.com/u/0/wm/1/+KivavaChang/posts/6HaygMAWKcp)

+
0
1
0

Great Thanks your corporation

[![photo.jpg.png](../_resources/fba4bf97aeee78ceb8801341cba0b126.png)](https://apis.google.com/u/0/wm/1/113276861370213912415)

### [Lynn Langit](https://apis.google.com/u/0/wm/1/113276861370213912415)

[1 month ago](https://apis.google.com/u/0/wm/1/+LynnLangit/posts/Ai95M5Sg81Y)  -  Shared publicly

Very exciting release, congratulations to the team!
+
1
2
1

 ·
Reply

[![photo.jpg.png](../_resources/a5d344aa18b3bde0281f1aebc5175f2a.png)](https://apis.google.com/u/0/wm/1/115899664865909744502)

### [Alphabet Investor Relations](https://apis.google.com/u/0/wm/1/115899664865909744502) via Google+

[3 weeks ago](https://apis.google.com/u/0/wm/1/+alphabetir/posts/QD7ScCUWs1M)  -  Shared publicly

“Today, we’re excited to announce the public beta for Cloud Spanner, a globally distributed relational database service that lets customers have their cake and eat it too: ACID transactions and SQL semantics, without giving up horizontal scaling and high availability.”

+
8
9
8

[![photo.jpg](../_resources/06220ed49a9a1ddd0da13a70752183ff.jpg)](https://apis.google.com/u/0/wm/1/114233674199568482864)

### [Abraham Williams](https://apis.google.com/u/0/wm/1/114233674199568482864) shared this via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+AbrahamWilliams/posts/SjNYHVuLo4c)  -  Shared publicly

+
1
0
1
0

 ·
Reply

[![photo.jpg](../_resources/bae9b4de843b0c4623225b1d5fa8c6c8.jpg)](https://apis.google.com/u/0/wm/1/109826099655556298824)

### [Peter Svensson](https://apis.google.com/u/0/wm/1/109826099655556298824) shared this via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/109826099655556298824/posts/dEpqRbwob89)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/b6b907dd7664c365fd2c05ea04c03ef7.jpg)](https://apis.google.com/u/0/wm/1/104624785711551243230)

### [Sean Reifschneider](https://apis.google.com/u/0/wm/1/104624785711551243230) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+SeanReifschneider/posts/YcqEMJWStGB)  -  Shared publicly

ACID plus globally distributed? Sounds nice!
+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/831ba8e5332eeeea0670495799c6eb55.png)](https://apis.google.com/u/0/wm/1/112956600152684612161)

### [Inautilo · Hotspots for Online Professionals](https://apis.google.com/u/0/wm/1/112956600152684612161)

[1 month ago](https://apis.google.com/u/0/wm/1/+inautilo/posts/bMiFcEaxxL3)  -  Shared publicly

CODE: **Introducing Cloud Spanner · Google’s global database service for mission-critical applications** · by Deepti Srivastava [#launch](https://apis.google.com/s/%23launch)

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/87648c098242393c7da9a67e6acfc4f4.jpg)](https://apis.google.com/u/0/wm/1/106198938488976320720)

### [Jorge Garcia](https://apis.google.com/u/0/wm/1/106198938488976320720) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+JorgeGarciaDOT/posts/W5kd2TgaT6i)  -  Shared publicly

Introducing [#Cloud](https://apis.google.com/s/%23Cloud) Spanner a global [#Database](https://apis.google.com/s/%23Database) service for mission-critical apps, [goo.gl/sX1NFL](http://goo.gl/sX1NFL)  +[Google Cloud](https://apis.google.com/117105793163182226623)  [#datamanagement](https://apis.google.com/s/%23datamanagement)  +[Google](https://apis.google.com/116899029375914044550)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/ea7b6b4ab889be521a31fbe0a1d420c5.jpg)](https://apis.google.com/u/0/wm/1/104965709610835374619)

### [Juantomas Garcia](https://apis.google.com/u/0/wm/1/104965709610835374619) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+JuantomasGarcia/posts/VgavkkV4nmy)  -  Shared publicly

[#gde](https://apis.google.com/s/%23gde)  [#gcp](https://apis.google.com/s/%23gcp)  [#spanner](https://apis.google.com/s/%23spanner)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/f4971b8f0012b060239623d1deb3ec5e.jpg)](https://apis.google.com/u/0/wm/1/102550604876259086885)

### [Jun Mukai](https://apis.google.com/u/0/wm/1/102550604876259086885) shared this via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+JunMukai/posts/F4uZoy9T1i4)  -  Shared publicly

+
1
2
1

 ·
Reply

[![photo.jpg.png](../_resources/38ca43d3e5a375b7c5d9157d23c15122.png)](https://apis.google.com/u/0/wm/1/104591613207462212978)

### [Christoph Bartoschek](https://apis.google.com/u/0/wm/1/104591613207462212978)

[1 month ago](https://apis.google.com/u/0/wm/1/+ChristophBartoschek/posts/i53h8Z5fkAo)  -  Shared publicly

A truly great database system.
+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/3ca7cb09df2ff8f004b792d3c0c7b0bd.png)](https://apis.google.com/u/0/wm/1/115920589427923934675)

### [Third Eye Consulting Services & Solutions LLC.](https://apis.google.com/u/0/wm/1/115920589427923934675)

[1 week ago](https://apis.google.com/u/0/wm/1/+ThirdeyecssBigData/posts/aokWzEkcjCS)  -  Shared publicly

@Google launches [#CloudSpanner](https://apis.google.com/s/%23CloudSpanner): global database service for mission-critical applications

http://bit.ly/2mnvDqQ @googlecloud [#BigData](https://apis.google.com/s/%23BigData)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/75791615fdde7492d882d0d87b7a10de.jpg)](https://apis.google.com/u/0/wm/1/102939978075826122343)

### [TAO Yuichi (taoy)](https://apis.google.com/u/0/wm/1/102939978075826122343) via Google+

[3 weeks ago](https://apis.google.com/u/0/wm/1/102939978075826122343/posts/Jf1MkyyzKuZ)  -  Shared publicly

[![post_facebook_black_24dp.png](../_resources/85c6c37aa92d7ab94a91d97ebf1f0adb.png)](https://apis.google.com/u/0/wm/1/115899664865909744502)[Alphabet Investor Relations](https://apis.google.com/u/0/wm/1/115899664865909744502) originally shared [this](https://apis.google.com/u/0/wm/1/+alphabetir/posts/QD7ScCUWs1M)

“Today, we’re excited to announce the public beta for Cloud Spanner, a globally distributed relational database service that lets customers have their cake and eat it too: ACID transactions and SQL semantics, without giving up horizontal scaling and high availability.”

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/7970c5eac4a0c21e08eaa7f48d863eee.jpg)](https://apis.google.com/u/0/wm/1/106416611017130431707)

### [Qorbani](https://apis.google.com/u/0/wm/1/106416611017130431707)

[2 weeks ago](https://apis.google.com/u/0/wm/1/+Qorbani/posts/TDoUnbwp5jS)  -  Shared publicly

Google Cloud Spanner: a global database service for mission-critical applications

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/059a509e05660ea289900b06e93e7c82.jpg)](https://apis.google.com/u/0/wm/1/105879689363313749147)

### [Erwin Mayer](https://apis.google.com/u/0/wm/1/105879689363313749147)

[3 weeks ago](https://apis.google.com/u/0/wm/1/+ErwinMayer/posts/1YowfxbPLHy)  -  Shared publicly

Awesome! Introducing Cloud Spanner: a global database service for mission-critical applications

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/3ca7cb09df2ff8f004b792d3c0c7b0bd.png)](https://apis.google.com/u/0/wm/1/115920589427923934675)

### [Third Eye Consulting Services & Solutions LLC.](https://apis.google.com/u/0/wm/1/115920589427923934675)

[2 weeks ago](https://apis.google.com/u/0/wm/1/+ThirdeyecssBigData/posts/K7p9NTuoJfq)  -  Shared publicly

@Google launches [#CloudSpanner](https://apis.google.com/s/%23CloudSpanner): global database service for mission-critical applications

http://bit.ly/2lhRhrJ @googlecloud [#BigData](https://apis.google.com/s/%23BigData)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/af943d9cca960f9765a654c4d56df086.jpg)](https://apis.google.com/u/0/wm/1/114517098096868756492)

### [Raymond Hawkins](https://apis.google.com/u/0/wm/1/114517098096868756492)

[1 month ago](https://apis.google.com/u/0/wm/1/+RaymondHawkins/posts/VpKUwBvmq5z)  -  Shared publicly

Sounds really cool!

Am I understanding the pricing correctly that it'd be a minimum of around $650/month for just a single node? While an excellent service, this seems really steep compared to Cloud SQL.

+
9
10
9

 ·
Reply

[![photo.jpg](../_resources/db41207e933fe8d8d77917e8c62b36d5.jpg)](https://plus.google.com/+MatthewLenz)

[Matthew Lenz](https://plus.google.com/+MatthewLenz)

[1 month ago](https://apis.google.com/u/0/wm/1/+RaymondHawkins/posts/VpKUwBvmq5z)

+
1
2
1

That's nothing, look at the Big Table service. 0.65$/hour per node. Minimum 3 nodes.

[![photo.jpg](../_resources/168d57445c9cb01e56bc624e0945a276.jpg)](https://plus.google.com/+JeffreyTitusguitar)

[Jeffrey Titus](https://plus.google.com/+JeffreyTitusguitar)

[1 month ago](https://apis.google.com/u/0/wm/1/+RaymondHawkins/posts/VpKUwBvmq5z)

+
1
2
1

It might be just a **bit** more powerful than CloudSQL for the investment... as a start, take a look at transactions: https://cloud.google.com/spanner/docs/transactions

Show more

Labels:[Announcements](https://cloudplatform.googleblog.com/search/label/Announcements) , [Storage & Databases](https://cloudplatform.googleblog.com/search/label/Storage%20%26%20Databases)