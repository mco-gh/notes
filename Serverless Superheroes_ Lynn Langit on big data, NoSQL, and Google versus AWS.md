Serverless Superheroes: Lynn Langit on big data, NoSQL, and Google versus AWS

# Serverless Superheroes: Lynn Langit on big data, NoSQL, and Google versus AWS

![](../_resources/d6ab940e924d5d6f0956b2ef6589e746.png)![1*IhZjBEpASpnB_W4VrNE2tg.png](../_resources/bb3c47de57404633f698e576cef734cd.png)

**Welcome to “Serverless Superheroes”! ***

In this space, I chat with the toolmakers, innovators, and developers who are navigating the brave new world of “serverless” cloud applications.*

*For today’s edition, I chatted with Lynn Langit, a big data and cloud architect. Lynn is a Google Cloud Developer Expert, an *[*AWS Community Hero*](https://aws.amazon.com/heroes/)*, and a former Microsoft employee. The following interview has been edited and condensed for clarity.*

[**Forrest Brazeal**](https://twitter.com/forrestbrazeal)**: Most people I know focus only one cloud, but you seem to be good at everything! You speak all over the world and work with clients in AWS, Azure, and Google Cloud Platform. What does the word “serverless” mean to you and your clients?**

[Lynn Langit](https://twitter.com/lynnlangit): The common definition is “the end customer is not responsible for the server.” I actually have elevated that definition even further. I’ve been working closely with a friend named [Anton Delsink](https://twitter.com/antondelsink) who works with the Azure Stack.

We drove around Norway together on a recent trip and came up with this definition of serverless: “a service that abstracts away the management of containers.” So our new buzzword is “containerless”.

**You just blew my mind! So what is the future of containers? You don’t think customers will want to bring their own containers to FaaS platforms?**

I have a sound bite answer: I don’t care. To me, containers are the new VMs. All this frenzy about containers, and more specifically container management systems — look, somebody has to manage the things. I want to pay the cloud providers to do it so I don’t have to.

Now in reality, I don’t build a lot of pure serverless solutions for clients yet. Some people still prefer containers to serverless, and their reasons are usually portability and control. If you don’t have a compelling need for those options, and you can get value out of the serverless services, by all means go that way.

**You’re an expert on data in the cloud, and I’ve always thought the concept of “serverless” gets pretty slippery at the data layer. To me, part of the point of “serverless” architectures is that you pay only for the capacity you use, but a lot of the data services charge you by the hour (RDS) or for provisioned capacity (DynamoDB) so that you pay even if your service gets no traffic. Do you think a pay-by-query service like AWS Athena is the future?**

I think Google is taking the lead here. They’ve provided serverless or near-serverless data solutions out of the box for years. I mean, BigQuery’s been out since 2011. It’s a NoOps SQL-on-files type solution. Even Cloud Spanner — you set up an instance, but the only knob you have to turn is for utilization.

Once you hit a certain number they advocate getting more nodes, but that’s it. It’s very interesting that as Google is trying to add enterprise data warehouse functionality to BigQuery, stuff like granular security and streaming, AWS has so rapidly built out Athena and added integrations with services like Glue.

So my prediction is, as Google expands its data portfolio — as they did when adding BigTable — it’s going to push the other cloud providers like AWS to offer automatic tuning, fewer knobs to turn for RDS and RedShift and EMR. And I think you’ll see that sooner rather than later, because Google is really pushing them, and we’ve seen that AWS responds very quickly to any sort of competitive threats to their cloud dominance.

**Right, which is probably why they’ve invested so much in Aurora as a proprietary RDBMS. You mentioned Athena, which I’ve played with a bit. That service gets expensive very fast if you don’t use it optimally, architecting your data in a specific columnar fashion. Does this limit the usefulness of the service, or is it going to change things about the way people access serverless data?**

Well, Athena is best suited for a certain type of data. Ad hoc queries on log files, really. If you want high volume, you have to have some kind of compression.

But just like Docker and Lambda are hard for application developers to get their minds around — which is why we have events like [ServerlessConf](http://serverlessconf.io/) — I think it’s even harder for data professionals to get their minds around “serverless” or server-lite implementations. Because there is this whole history of DBAs managing clusters and such. So the new paradigm is scary, and I think DBAs tend to dig in their heels and resist.

I actually think that has hurt BigQuery adoption, which is why it’s been around since 2011 and only in 2016 did Amazon feel the need to come out with Athena. You and I both know they could have created it sooner, but the market wasn’t there.

**I think a lot of people (including some of those heel-digging DBAs) tend to associate “serverless” with “NoSQL”. In fact, I know people who believe the relational database is falling by the wayside, give or take a few things like financial applications that need transactional consistency. Do you think that’s a fair assumption? Why or why not?**

The NoSQL trend of the last few years has been really interesting to me. After all, when I worked at Microsoft I wrote books on SQL Server. I did a bunch of traditional data warehousing with OLTP and OLAP and all that. When I left Microsoft and went independent in 2011, there was a lot of hype around Hadoop and NoSQL. And what I often find is that it’s failed to deliver.

Most of my consulting engagements are around data in the cloud. People say “can you help us get business value out of NoSQL Database X?” And for many small to medium size businesses, I can’t. They don’t have the staff, the will, the need, to change.

Today, if a customer says they want to implement their own NoSQL stack, I really challenge them. I mean, sometimes they have some really strong Cassandra talent or something, but that’s a pretty rare exception. I see NoSQL as very overhyped and having very little business value. It raises a big red flag for me, and I’ve recovered a lot of failed NoSQL implementations, converted them to RDS.

**So to clarify, when you talk about NoSQL raising red flags, you mean people managing their own deployments rather than relying on managed services from a cloud provider?**

Partially. To be honest, I think a lot of the independent NoSQL products are going to go away. Either they’ll be bought up by Amazon or Microsoft or Google, or they’ll not be able to compete. It’s gonna be a really small space. I think Redis will survive, because they have some really unique aspects to their implementation. Cassandra, not sure.

I mean, I went through a period where I was obsessed with NoSQL. I did presentations — “NoSQL for the SQL Developer” — I really thought it was the future. But I’ve come to the conclusion that just like containers, NoSQL implementations are a distraction. Skip containers — go to functions. Skip Cassandra — go to DynamoDB or a managed relational service.

**So it sounds like you are not giving up on relational databases for serverless systems.**

Not at all. If a customer does have a use case for NoSQL, I will recommend the cloud provider’s NoSQL. But I remember one time I was an architect on an AWS IoT solution, where even the reference architecture used DynamoDB.

But they were having all sorts of problems, and one day I just decided to switch to Aurora. Freaked out everybody — they said, ”What are you doing?” I said, “What are we doing? We’re shipping a product.” And we did.

**Let’s say I wanted to build an application that needs to manage real time user state and transactional data, as well as providing data warehousing and big data processing on the back end. And I didn’t want to have to manage any database servers myself. If you could magically wave a wand and put the best services together from the various cloud providers to do this, how would you design the data layer?**

Let’s start with object storage. Although AWS has made great improvements to the S3 lifecycle management process, one thing I love about Google is that they have a unified API for Google Cloud Storage. The concept of AWS Glacier is included, so you have nearline, coldline, multi- and single-regional storage all wrapped up together, and it’s presented really simply. What I don’t like is that it’s missing some features of S3 — logging, versioning, metrics. So it’s kind of a tossup between a data lake on Google Cloud Storage or S3.

Next thing: streaming ingest. This is an area where I’m doing a lot of work right now. The systems that exist out there seem to be all running on Kafka. I personally like Kinesis — quick, easy, simple — and Google Cloud Pub/Sub’s good too. But there is feature differentiation between Kafka and the cloud pipes. I wish the cloud vendors would have more features of Kafka — I’m looking for that at re:Invent this year!

For ETL, some interesting things are happening. I haven’t been too much into AWS Glue yet. I actually love an ETL product made by [Matillion](https://www.matillion.com/). You can get their AMI on the AWS Marketplace. It’s sort of like SQL Server SSIS in a browser, so you have visual representation of the transformations, and your old-school DBA goes “Oh, that looks like my ETL tool!”

The long and short is — if you’re ETL-ing or ELT-ing, I prefer a tool rather than an API. Amazon really shines there. I don’t really like their native Data Pipeline, but they shine because of vendors like Matillion. On the other hand, Google requires you to code everything against their APIs, usually in Java.

And that’s been a *big *negative: Google is such a developer-focused cloud. You code everything first, and then the tools come later, if ever. Even though their cloud is really powerful and really scalable, that’s just not the paradigm. Whereas AWS is a DevOps cloud, and I think that’s been one of the drivers of their success, around data in particular, because the network admins and DBAs have more references.

In the relational layer, I really love Aurora and the rest of the RDS implementations. I’m interested in Spanner, but again it’s a case of Google taking their own products and releasing them, not understanding that the rest of the world doesn’t work at Google scale.

Like the fact that Spanner doesn’t support foreign keys, and then there’s no schema import and conversion tool. Who’s gonna take an existing enterprise application and change the relational schema? It’s just not happening. And the fact that Google doesn’t even address that makes me sad, because the fact is that Spanner is a stunningly beautiful technology.

This lack of making a complete product, even though Google is offering more in the data space, makes me tend to focus on Amazon. Although I do keep an eye on what Google is doing, because what Google is really doing is forcing Amazon to make better products. Good for customers, bad for Google.

And then finally in the realm of big data processing, it’s a real tossup between EMR and Cloud Dataproc. Google’s VMs are pre-warmed and so fast, they come up in seconds. I do a lot of prototyping, so that’s great for me. If you’re doing bursty workloads, you can use Preemptible, Google’s version of Spot. I wish AWS would update EMR, make it a bit more modern — I’m looking for that at re:Invent too. To be honest, right now I tend to just use [DataBricks](https://databricks.com/).

**What are some other ways that you think serverless can transform big data, and vice versa?**

ETL is still the big, bad problem in the world of data. I would like to see more ETL tools that include machine learning and statistics. “It looks like this data needs X.” “This schema is A and this schema is B. It looks like you need transformations of ABC.” Applying regular compute, but machine learning in particular, to ETL problems will be magical. It’ll be interesting to see what happens with Glue coming out.

The other thing is democratization of machine learning. I always confess when things are hard — that’s part of my brand. I’ve been working on understanding how to build TensorFlow and MXNet models that provide actual business value for over six months. So far I’m not able to do it. And the majority of people that I talk to, if they’re being honest, aren’t able to do it either. Most people can complete the Hello World-level examples, but there’s a missing translation layer between the samples and actually building business models.

I am really fascinated by the space, because in machine learning there are great serverless services, Rekognition API and Polly and Lex, and there will continue to be more of those. But how do we get to where the API and tools are mature enough that a business person who understands statistics can make a model? I think there’s a lot of API, tooling and visualization work to be done here.

**How do you think we in the cloud space can help make serverless more accessible to new learners?**

One way to learn serverless is to build an IoT use case. I really like building with Alexa — I’ve done it across the spectrum with kids, schoolteachers, even grumpy developers. I like the [Simple Beer Service](https://github.com/awslabs/simplebeerservice) too. Put people in an environment that’s fun, has a low cost to entry, and they’re going to say “Oh, I can actually do this!” I bring in Echo Dots because they disarm people.

Here’s the one aspect of serverless that we cannot lose sight of: this technology brings with it a tremendous amount of change. It’s scary; it’s disruptive. Failure to acknowledge that is just holding back the opportunities.

*Check back soon for another edition of Serverless Superheroes.*