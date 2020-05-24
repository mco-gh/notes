donnemartin/system-design-primer

# [(L)](https://github.com/donnemartin/system-design-primer#the-system-design-primer)The System Design Primer

 [![687474703a2f2f692e696d6775722e636f6d2f6a6a3341354e382e706e67.png](../_resources/91bf37640db35d2794b83c0e453a1afd.png)](https://camo.githubusercontent.com/e45e39c36eebcc4c66e1aecd4e4145112d8e88e3/687474703a2f2f692e696d6775722e636f6d2f6a6a3341354e382e706e67)

## [(L)](https://github.com/donnemartin/system-design-primer#motivation)Motivation

> Learn how to design large scale systems.
> Prep for the system design interview.

### [(L)](https://github.com/donnemartin/system-design-primer#learn-how-to-design-large-scale-systems)Learn how to design large scale systems

Learning how to design scalable systems will help you become a better engineer.

System design is a broad topic. There is a **vast amount of resources scattered throughout the web** on system design principles.

This repo is an **organized collection** of resources to help you learn how to build systems at scale.

### [(L)](https://github.com/donnemartin/system-design-primer#learn-from-the-open-source-community)Learn from the open source community

This is an early draft of a continually updated, open source project.

[Contributions](https://github.com/donnemartin/system-design-primer#contributing) are welcome!

### [(L)](https://github.com/donnemartin/system-design-primer#prep-for-the-system-design-interview)Prep for the system design interview

In addition to coding interviews, system design is a **required component** of the **technical interview process** at many tech companies.

**Practice common system design interview questions** and **compare** your results with **sample solutions**: discussions, code, and diagrams.

Additional topics for interview prep:

- [Study guide](https://github.com/donnemartin/system-design-primer#study-guide)
- [How to approach a system design interview question](https://github.com/donnemartin/system-design-primer#how-to-approach-a-system-design-interview-question)
- [System design interview questions, **with solutions**](https://github.com/donnemartin/system-design-primer#system-design-interview-questions-with-solutions)
- [Object-oriented design interview questions, **with solutions**](https://github.com/donnemartin/system-design-primer#object-oriented-design-interview-questions-with-solutions)
- [Additional system design interview questions](https://github.com/donnemartin/system-design-primer#additional-system-design-interview-questions)

## [(L)](https://github.com/donnemartin/system-design-primer#anki-flashcards)Anki flashcards

 [![687474703a2f2f692e696d6775722e636f6d2f7a6443416b42332e706e67.png](../_resources/ad9aec05c86cd7d42ca246a31d2e73a2.png)](https://camo.githubusercontent.com/75b5cf737556050871218226ea211256f19f3a40/687474703a2f2f692e696d6775722e636f6d2f7a6443416b42332e706e67)

The provided [Anki flashcard decks](https://apps.ankiweb.net/) use spaced repetition to help you retain key system design concepts.

- [System design deck](https://github.com/donnemartin/system-design-primer/blob/master/resources/flash_cards/System%20Design.apkg)
- [System design exercises deck](https://github.com/donnemartin/system-design-primer/blob/master/resources/flash_cards/System%20Design%20Exercises.apkg)
- [Object oriented design exercises deck](https://github.com/donnemartin/system-design-primer/blob/master/resources/flash_cards/OO%20Design.apkg)

Great for use while on-the-go.

## [(L)](https://github.com/donnemartin/system-design-primer#contributing)Contributing

> Learn from the community.
Feel free to submit pull requests to help:

- Fix errors
- Improve sections
- Add new sections

Content that needs some polishing is placed [under development](https://github.com/donnemartin/system-design-primer#under-development).

Review the [Contributing Guidelines](https://github.com/donnemartin/system-design-primer/blob/master/CONTRIBUTING.md).

## [(L)](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics)Index of system design topics

> Summaries of various system design topics, including pros and cons. **> Everything is a trade-off**> .

> Each section contains links to more in-depth resources.

 [![687474703a2f2f692e696d6775722e636f6d2f6a7255424146372e706e67.png](../_resources/3343b461ea0b971703b1a6ee598b823a.png)](https://camo.githubusercontent.com/14f76dab28dfbfa12ea6b02c6bd0ec726fc17306/687474703a2f2f692e696d6775722e636f6d2f6a7255424146372e706e67)

- [System design topics: start here](https://github.com/donnemartin/system-design-primer#system-design-topics-start-here)
    - [Step 1: Review the scalability video lecture](https://github.com/donnemartin/system-design-primer#step-1-review-the-scalability-video-lecture)
    - [Step 2: Review the scalability article](https://github.com/donnemartin/system-design-primer#step-2-review-the-scalability-article)
    - [Next steps](https://github.com/donnemartin/system-design-primer#next-steps)
- [Performance vs scalability](https://github.com/donnemartin/system-design-primer#performance-vs-scalability)
- [Latency vs throughput](https://github.com/donnemartin/system-design-primer#latency-vs-throughput)
- [Availability vs consistency](https://github.com/donnemartin/system-design-primer#availability-vs-consistency)
    - [CAP theorem](https://github.com/donnemartin/system-design-primer#cap-theorem)
        - [CP - consistency and partition tolerance](https://github.com/donnemartin/system-design-primer#cp---consistency-and-partition-tolerance)
        - [AP - availability and partition tolerance](https://github.com/donnemartin/system-design-primer#ap---availability-and-partition-tolerance)
- [Consistency patterns](https://github.com/donnemartin/system-design-primer#consistency-patterns)
    - [Weak consistency](https://github.com/donnemartin/system-design-primer#weak-consistency)
    - [Eventual consistency](https://github.com/donnemartin/system-design-primer#eventual-consistency)
    - [Strong consistency](https://github.com/donnemartin/system-design-primer#strong-consistency)
- [Availability patterns](https://github.com/donnemartin/system-design-primer#availability-patterns)
    - [Fail-over](https://github.com/donnemartin/system-design-primer#fail-over)
    - [Replication](https://github.com/donnemartin/system-design-primer#replication)
- [Domain name system](https://github.com/donnemartin/system-design-primer#domain-name-system)
- [Content delivery network](https://github.com/donnemartin/system-design-primer#content-delivery-network)
    - [Push CDNs](https://github.com/donnemartin/system-design-primer#push-cdns)
    - [Pull CDNs](https://github.com/donnemartin/system-design-primer#pull-cdns)
- [Load balancer](https://github.com/donnemartin/system-design-primer#load-balancer)
    - [Active-passive](https://github.com/donnemartin/system-design-primer#active-passive)
    - [Active-active](https://github.com/donnemartin/system-design-primer#active-active)
    - [Layer 4 load balancing](https://github.com/donnemartin/system-design-primer#layer-4-load-balancing)
    - [Layer 7 load balancing](https://github.com/donnemartin/system-design-primer#layer-7-load-balancing)
    - [Horizontal scaling](https://github.com/donnemartin/system-design-primer#horizontal-scaling)
- [Reverse proxy (web server)](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)
    - [Load balancer vs reverse proxy](https://github.com/donnemartin/system-design-primer#load-balancer-vs-reverse-proxy)
- [Application layer](https://github.com/donnemartin/system-design-primer#application-layer)
    - [Microservices](https://github.com/donnemartin/system-design-primer#microservices)
    - [Service discovery](https://github.com/donnemartin/system-design-primer#service-discovery)
- [Database](https://github.com/donnemartin/system-design-primer#database)
    - [Relational database management system (RDBMS)](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)
        - [Master-slave replication](https://github.com/donnemartin/system-design-primer#master-slave-replication)
        - [Master-master replication](https://github.com/donnemartin/system-design-primer#master-master-replication)
        - [Federation](https://github.com/donnemartin/system-design-primer#federation)
        - [Sharding](https://github.com/donnemartin/system-design-primer#sharding)
        - [Denormalization](https://github.com/donnemartin/system-design-primer#denormalization)
        - [SQL tuning](https://github.com/donnemartin/system-design-primer#sql-tuning)
    - [NoSQL](https://github.com/donnemartin/system-design-primer#nosql)
        - [Key-value store](https://github.com/donnemartin/system-design-primer#key-value-store)
        - [Document store](https://github.com/donnemartin/system-design-primer#document-store)
        - [Wide column store](https://github.com/donnemartin/system-design-primer#wide-column-store)
        - [Graph Database](https://github.com/donnemartin/system-design-primer#graph-database)
    - [SQL or NoSQL](https://github.com/donnemartin/system-design-primer#sql-or-nosql)
- [Cache](https://github.com/donnemartin/system-design-primer#cache)
    - [Client caching](https://github.com/donnemartin/system-design-primer#client-caching)
    - [CDN caching](https://github.com/donnemartin/system-design-primer#cdn-caching)
    - [Web server caching](https://github.com/donnemartin/system-design-primer#web-server-caching)
    - [Database caching](https://github.com/donnemartin/system-design-primer#database-caching)
    - [Application caching](https://github.com/donnemartin/system-design-primer#application-caching)
    - [Caching at the database query level](https://github.com/donnemartin/system-design-primer#caching-at-the-database-query-level)
    - [Caching at the object level](https://github.com/donnemartin/system-design-primer#caching-at-the-object-level)
    - [When to update the cache](https://github.com/donnemartin/system-design-primer#when-to-update-the-cache)
        - [Cache-aside](https://github.com/donnemartin/system-design-primer#cache-aside)
        - [Write-through](https://github.com/donnemartin/system-design-primer#write-through)
        - [Write-behind (write-back)](https://github.com/donnemartin/system-design-primer#write-behind-write-back)
        - [Refresh-ahead](https://github.com/donnemartin/system-design-primer#refresh-ahead)
- [Asynchronism](https://github.com/donnemartin/system-design-primer#asynchronism)
    - [Message queues](https://github.com/donnemartin/system-design-primer#message-queues)
    - [Task queues](https://github.com/donnemartin/system-design-primer#task-queues)
    - [Back pressure](https://github.com/donnemartin/system-design-primer#back-pressure)
- [Communication](https://github.com/donnemartin/system-design-primer#communication)
    - [Transmission control protocol (TCP)](https://github.com/donnemartin/system-design-primer#transmission-control-protocol-tcp)
    - [User datagram protocol (UDP)](https://github.com/donnemartin/system-design-primer#user-datagram-protocol-udp)
    - [Remote procedure call (RPC)](https://github.com/donnemartin/system-design-primer#remote-procedure-call-rpc)
    - [Representational state transfer (REST)](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest)
- [Security](https://github.com/donnemartin/system-design-primer#security)
- [Appendix](https://github.com/donnemartin/system-design-primer#appendix)
    - [Powers of two table](https://github.com/donnemartin/system-design-primer#powers-of-two-table)
    - [Latency numbers every programmer should know](https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know)
    - [Additional system design interview questions](https://github.com/donnemartin/system-design-primer#additional-system-design-interview-questions)
    - [Real world architectures](https://github.com/donnemartin/system-design-primer#real-world-architectures)
    - [Company architectures](https://github.com/donnemartin/system-design-primer#company-architectures)
    - [Company engineering blogs](https://github.com/donnemartin/system-design-primer#company-engineering-blogs)
- [Under development](https://github.com/donnemartin/system-design-primer#under-development)
- [Credits](https://github.com/donnemartin/system-design-primer#credits)
- [Contact info](https://github.com/donnemartin/system-design-primer#contact-info)
- [License](https://github.com/donnemartin/system-design-primer#license)

## [(L)](https://github.com/donnemartin/system-design-primer#study-guide)Study guide

> Suggested topics to review based on your interview timeline (short, medium, long).

[![Imgur](../_resources/5223751f86f5ee7e3938e092e5081b41.png)](https://camo.githubusercontent.com/eb92600aa3bb1314b33edd0204da8428d4d3a493/687474703a2f2f692e696d6775722e636f6d2f4f66566c6c65782e706e67)

**Q: For interviews, do I need to know everything here?**
**A: No, you don't need to know everything here to prepare for the interview**.
What you are asked in an interview depends on variables such as:

- How much experience you have
- What your technical background is
- What positions you are interviewing for
- Which companies you are interviewing with
- Luck

More experienced candidates are generally expected to know more about system design. Architects or team leads might be expected to know more than individual contributors. Top tech companies are likely to have one or more design interview rounds.

Start broad and go deeper in a few areas. It helps to know a little about various key system design topics. Adjust the following guide based on your timeline, experience, what positions you are interviewing for, and which companies you are interviewing with.

- **Short timeline** - Aim for **breadth** with system design topics. Practice by solving **some** interview questions.
- **Medium timeline** - Aim for **breadth** and **some depth** with system design topics. Practice by solving **many** interview questions.
- **Long timeline** - Aim for **breadth** and **more depth** with system design topics. Practice by solving **most** interview questions.

|     | Short | Medium | Long |
| --- | --- | --- | --- |
| Read through the [System design topics](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics) to get a broad understanding of how systems work | 👍  | 👍  | 👍  |
| Read through a few articles in the [Company engineering blogs](https://github.com/donnemartin/system-design-primer#company-engineering-blogs) for the companies you are interviewing with | 👍  | 👍  | 👍  |
| Read through a few [Real world architectures](https://github.com/donnemartin/system-design-primer#real-world-architectures) | 👍  | 👍  | 👍  |
| Review [How to approach a system design interview question](https://github.com/donnemartin/system-design-primer#how-to-approach-a-system-design-interview-question) | 👍  | 👍  | 👍  |
| Work through [System design interview questions with solutions](https://github.com/donnemartin/system-design-primer#system-design-interview-questions-with-solutions) | Some | Many | Most |
| Work through [Object-oriented design interview questions with solutions](https://github.com/donnemartin/system-design-primer#object-oriented-design-interview-questions-with-solutions) | Some | Many | Most |
| Review [Additional system design interview questions](https://github.com/donnemartin/system-design-primer#additional-system-design-interview-questions) | Some | Many | Most |

## [(L)](https://github.com/donnemartin/system-design-primer#how-to-approach-a-system-design-interview-question)How to approach a system design interview question

> How to tackle a system design interview question.

The system design interview is an **open-ended conversation**. You are expected to lead it.

You can use the following steps to guide the discussion. To help solidify this process, work through the [System design interview questions with solutions](https://github.com/donnemartin/system-design-primer#system-design-interview-questions-with-solutions) section using the following steps.

### [(L)](https://github.com/donnemartin/system-design-primer#step-1-outline-use-cases-constraints-and-assumptions)Step 1: Outline use cases, constraints, and assumptions

Gather requirements and scope the problem. Ask questions to clarify use cases and constraints. Discuss assumptions.

- Who is going to use it?
- How are they going to use it?
- How many users are there?
- What does the system do?
- What are the inputs and outputs of the system?
- How much data do we expect to handle?
- How many requests per second do we expect?
- What is the expected read to write ratio?

### [(L)](https://github.com/donnemartin/system-design-primer#step-2-create-a-high-level-design)Step 2: Create a high level design

Outline a high level design with all important components.

- Sketch the main components and connections
- Justify your ideas

### [(L)](https://github.com/donnemartin/system-design-primer#step-3-design-core-components)Step 3: Design core components

Dive into details for each core component. For example, if you were asked to [design a url shortening service](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md), discuss:

- Generating and storing a hash of the full url
    - [MD5](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md) and [Base62](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md)
    - Hash collisions
    - SQL or NoSQL
    - Database schema
- Translating a hashed url to the full url
    - Database lookup
- API and object-oriented design

### [(L)](https://github.com/donnemartin/system-design-primer#step-4-scale-the-design)Step 4: Scale the design

Identify and address bottlenecks, given the constraints. For example, do you need the following to address scalability issues?

- Load balancer
- Horizontal scaling
- Caching
- Database sharding

Discuss potential solutions and trade-offs. Everything is a trade-off. Address bottlenecks using [principles of scalable system design](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics).

### [(L)](https://github.com/donnemartin/system-design-primer#back-of-the-envelope-calculations)Back-of-the-envelope calculations

You might be asked to do some estimates by hand. Refer to the [Appendix](https://github.com/donnemartin/system-design-primer#appendix) for the following resources:

- [Use back of the envelope calculations](http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelope-calculations-to-choo.html)
- [Powers of two table](https://github.com/donnemartin/system-design-primer#powers-of-two-table)
- [Latency numbers every programmer should know](https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know)

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading)Source(s) and further reading

Check out the following links to get a better idea of what to expect:

- [How to ace a systems design interview](https://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/)
- [The system design interview](http://www.hiredintech.com/system-design)
- [Intro to Architecture and Systems Design Interviews](https://www.youtube.com/watch?v=ZgdS0EUmn70)

## [(L)](https://github.com/donnemartin/system-design-primer#system-design-interview-questions-with-solutions)System design interview questions with solutions

> Common system design interview questions with sample discussions, code, and diagrams.

> Solutions linked to content in the ` solutions/ `>  folder.

| Question |     |
| --- | --- |
| Design Pastebin.com (or Bit.ly) | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md) |
| Design the Twitter timeline (or Facebook feed)<br>Design Twitter search (or Facebook search) | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md) |
| Design a web crawler | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md) |
| Design Mint.com | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/mint/README.md) |
| Design the data structures for a social network | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/social_graph/README.md) |
| Design a key-value store for a search engine | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/query_cache/README.md) |
| Design Amazon's sales ranking by category feature | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/sales_rank/README.md) |
| Design a system that scales to millions of users on AWS | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/scaling_aws/README.md) |
| Add a system design question | [Contribute](https://github.com/donnemartin/system-design-primer#contributing) |

### [(L)](https://github.com/donnemartin/system-design-primer#design-pastebincom-or-bitly)Design Pastebin.com (or Bit.ly)

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md)

[![Imgur](../_resources/aa0cac4f358b9ed53835c603375e44d4.png)](https://camo.githubusercontent.com/4aee2d26ebedc20e7fa07a2c30780e332fa29f2c/687474703a2f2f692e696d6775722e636f6d2f346564584730542e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-the-twitter-timeline-and-search-or-facebook-feed-and-search)Design the Twitter timeline and search (or Facebook feed and search)

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md)

[![Imgur](../_resources/3343b461ea0b971703b1a6ee598b823a.png)](https://camo.githubusercontent.com/14f76dab28dfbfa12ea6b02c6bd0ec726fc17306/687474703a2f2f692e696d6775722e636f6d2f6a7255424146372e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-a-web-crawler)Design a web crawler

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md)

[![Imgur](../_resources/f1cb31b48ff34e3723a6ad7524227125.png)](https://camo.githubusercontent.com/ba21a95852d1cf7bb64c8c4622a79d1d5a20d344/687474703a2f2f692e696d6775722e636f6d2f625778507451412e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-mintcom)Design Mint.com

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/mint/README.md)

[![Imgur](../_resources/b2775ebc5a98096a7234542351e0a4c6.png)](https://camo.githubusercontent.com/12fea5f9324f74189a9cd983b02239c68615b67e/687474703a2f2f692e696d6775722e636f6d2f563571353776552e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-the-data-structures-for-a-social-network)Design the data structures for a social network

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/social_graph/README.md)

[![Imgur](../_resources/91f79885f8f4ef4232a271afae299709.png)](https://camo.githubusercontent.com/16d78e51c2e2949e23122f4c26afe5886f82a96f/687474703a2f2f692e696d6775722e636f6d2f636443763567372e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-a-key-value-store-for-a-search-engine)Design a key-value store for a search engine

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/query_cache/README.md)

[![Imgur](../_resources/e96790ad7f8430205226c8884039e432.png)](https://camo.githubusercontent.com/b6439861687b9a0fc62d0149a364082643ebaf86/687474703a2f2f692e696d6775722e636f6d2f346a39396d68652e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-amazons-sales-ranking-by-category-feature)Design Amazon's sales ranking by category feature

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/sales_rank/README.md)

[![Imgur](../_resources/31df1c005753a9e23e8a651ef4d6ddb2.png)](https://camo.githubusercontent.com/a56f5600f7ae29dc0c2e436b8e4e4b55c44d6894/687474703a2f2f692e696d6775722e636f6d2f4d7a45785030362e706e67)

### [(L)](https://github.com/donnemartin/system-design-primer#design-a-system-that-scales-to-millions-of-users-on-aws)Design a system that scales to millions of users on AWS

[View exercise and solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/scaling_aws/README.md)

[![Imgur](../_resources/91bf37640db35d2794b83c0e453a1afd.png)](https://camo.githubusercontent.com/e45e39c36eebcc4c66e1aecd4e4145112d8e88e3/687474703a2f2f692e696d6775722e636f6d2f6a6a3341354e382e706e67)

## [(L)](https://github.com/donnemartin/system-design-primer#object-oriented-design-interview-questions-with-solutions)Object-oriented design interview questions with solutions

> Common object-oriented design interview questions with sample discussions, code, and diagrams.

> Solutions linked to content in the ` solutions/ `>  folder.
**> Note: This section is under development**

| Question |     |
| --- | --- |
| Design a hash map | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/hash_table/hash_map.ipynb) |
| Design a least recently used cache | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/lru_cache/lru_cache.ipynb) |
| Design a call center | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/call_center/call_center.ipynb) |
| Design a deck of cards | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/deck_of_cards/deck_of_cards.ipynb) |
| Design a parking lot | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/parking_lot/parking_lot.ipynb) |
| Design a chat server | [Solution](https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/online_chat/online_chat.ipynb) |
| Design a circular array | [Contribute](https://github.com/donnemartin/system-design-primer#contributing) |
| Add an object-oriented design question | [Contribute](https://github.com/donnemartin/system-design-primer#contributing) |

## [(L)](https://github.com/donnemartin/system-design-primer#system-design-topics-start-here)System design topics: start here

New to system design?

First, you'll need a basic understanding of common principles, learning about what they are, how they are used, and their pros and cons.

### [(L)](https://github.com/donnemartin/system-design-primer#step-1-review-the-scalability-video-lecture)Step 1: Review the scalability video lecture

[Scalability Lecture at Harvard](https://www.youtube.com/watch?v=-W9F__D3oY4)

- Topics covered:
    - Vertical scaling
    - Horizontal scaling
    - Caching
    - Load balancing
    - Database replication
    - Database partitioning

### [(L)](https://github.com/donnemartin/system-design-primer#step-2-review-the-scalability-article)Step 2: Review the scalability article

[Scalability](http://www.lecloud.net/tagged/scalability)

- Topics covered:
    - [Clones](http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones)
    - [Databases](http://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database)
    - [Caches](http://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache)
    - [Asynchronism](http://www.lecloud.net/post/9699762917/scalability-for-dummies-part-4-asynchronism)

### [(L)](https://github.com/donnemartin/system-design-primer#next-steps)Next steps

Next, we'll look at high-level trade-offs:

- **Performance** vs **scalability**
- **Latency** vs **throughput**
- **Availability** vs **consistency**

Keep in mind that **everything is a trade-off**.

Then we'll dive into more specific topics such as DNS, CDNs, and load balancers.

## [(L)](https://github.com/donnemartin/system-design-primer#performance-vs-scalability)Performance vs scalability

A service is **scalable** if it results in increased **performance** in a manner proportional to resources added. Generally, increasing performance means serving more units of work, but it can also be to handle larger units of work, such as when datasets grow.[1](http://www.allthingsdistributed.com/2006/03/a_word_on_scalability.html)

Another way to look at performance vs scalability:

- If you have a **performance** problem, your system is slow for a single user.
- If you have a **scalability** problem, your system is fast for a single user but slow under heavy load.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-1)Source(s) and further reading

- [A word on scalability](http://www.allthingsdistributed.com/2006/03/a_word_on_scalability.html)
- [Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)

## [(L)](https://github.com/donnemartin/system-design-primer#latency-vs-throughput)Latency vs throughput

**Latency** is the time to perform some action or to produce some result.
**Throughput** is the number of such actions or results per unit of time.

Generally, you should aim for **maximal throughput** with **acceptable latency**.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-2)Source(s) and further reading

- [Understanding latency vs throughput](https://community.cadence.com/cadence_blogs_8/b/sd/archive/2010/09/13/understanding-latency-vs-throughput)

## [(L)](https://github.com/donnemartin/system-design-primer#availability-vs-consistency)Availability vs consistency

### [(L)](https://github.com/donnemartin/system-design-primer#cap-theorem)CAP theorem

 [![687474703a2f2f692e696d6775722e636f6d2f62674c4d4932752e706e67.png](../_resources/c96b4a59d6427236e4eac4317902e8b5.png)](https://camo.githubusercontent.com/13719354da7dcd34cd79ff5f8b6306a67bc18261/687474703a2f2f692e696d6775722e636f6d2f62674c4d4932752e706e67)

 *[Source: CAP theorem revisited](http://robertgreiner.com/2014/08/cap-theorem-revisited)*

In a distributed computer system, you can only support two of the following guarantees:

- **Consistency** - Every read receives the most recent write or an error
- **Availability** - Every request receives a response, without guarantee that it contains the most recent version of the information
- **Partition Tolerance** - The system continues to operate despite arbitrary partitioning due to network failures

*Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability.*

#### [(L)](https://github.com/donnemartin/system-design-primer#cp---consistency-and-partition-tolerance)CP - consistency and partition tolerance

Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs require atomic reads and writes.

#### [(L)](https://github.com/donnemartin/system-design-primer#ap---availability-and-partition-tolerance)AP - availability and partition tolerance

Responses return the most recent version of the data, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs allow for [eventual consistency](https://github.com/donnemartin/system-design-primer#eventual-consistency) or when the system needs to continue working despite external errors.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-3)Source(s) and further reading

- [CAP theorem revisited](http://robertgreiner.com/2014/08/cap-theorem-revisited/)
- [A plain english introduction to CAP theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem/)
- [CAP FAQ](https://github.com/henryr/cap-faq)

## [(L)](https://github.com/donnemartin/system-design-primer#consistency-patterns)Consistency patterns

With multiple copies of the same data, we are faced with options on how to synchronize them so clients have a consistent view of the data. Recall the definition of consistency from the [CAP theorem](https://github.com/donnemartin/system-design-primer#cap-theorem) - Every read receives the most recent write or an error.

### [(L)](https://github.com/donnemartin/system-design-primer#weak-consistency)Weak consistency

After a write, reads may or may not see it. A best effort approach is taken.

This approach is seen in systems such as memcached. Weak consistency works well in real time use cases such as VoIP, video chat, and realtime multiplayer games. For example, if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.

### [(L)](https://github.com/donnemartin/system-design-primer#eventual-consistency)Eventual consistency

After a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously.

This approach is seen in systems such as DNS and email. Eventual consistency works well in highly available systems.

### [(L)](https://github.com/donnemartin/system-design-primer#strong-consistency)Strong consistency

After a write, reads will see it. Data is replicated synchronously.

This approach is seen in file systems and RDBMSes. Strong consistency works well in systems that need transactions.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-4)Source(s) and further reading

- [Transactions across data centers](http://snarfed.org/transactions_across_datacenters_io.html)

## [(L)](https://github.com/donnemartin/system-design-primer#availability-patterns)Availability patterns

There are two main patterns to support high availability: **fail-over** and **replication**.

### [(L)](https://github.com/donnemartin/system-design-primer#fail-over)Fail-over

#### [(L)](https://github.com/donnemartin/system-design-primer#active-passive)Active-passive

With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.

The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic.

Active-passive failover can also be referred to as master-slave failover.

#### [(L)](https://github.com/donnemartin/system-design-primer#active-active)Active-active

In active-active, both servers are managing traffic, spreading the load between them.

If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers.

Active-active failover can also be referred to as master-master failover.

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-failover)Disadvantage(s): failover

- Fail-over adds more hardware and additional complexity.
- There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.

### [(L)](https://github.com/donnemartin/system-design-primer#replication)Replication

#### [(L)](https://github.com/donnemartin/system-design-primer#master-slave-and-master-master)Master-slave and master-master

This topic is further discussed in the [Database](https://github.com/donnemartin/system-design-primer#database) section:

- [Master-slave replication](https://github.com/donnemartin/system-design-primer#master-slave-replication)
- [Master-master replication](https://github.com/donnemartin/system-design-primer#master-master-replication)

## [(L)](https://github.com/donnemartin/system-design-primer#domain-name-system)Domain name system

 [![687474703a2f2f692e696d6775722e636f6d2f494f794c6a34692e6a7067.jpg](../_resources/52192ffc8c1bc69cff4e117113690460.jpg)](https://camo.githubusercontent.com/fae27d1291ed38dd120595d692eacd2505cd3a9c/687474703a2f2f692e696d6775722e636f6d2f494f794c6a34692e6a7067)

 *[Source: DNS security presentation](http://www.slideshare.net/srikrupa5/dns-security-presentation-issa)*

A Domain Name System (DNS) translates a domain name such as [www.example.com](http://www.example.com/) to an IP address.

DNS is hierarchical, with a few authoritative servers at the top level. Your router or ISP provides information about which DNS server(s) to contact when doing a lookup. Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays. DNS results can also be cached by your browser or OS for a certain period of time, determined by the [time to live (TTL)](https://en.wikipedia.org/wiki/Time_to_live).

- **NS record (name server)** - Specifies the DNS servers for your domain/subdomain.
- **MX record (mail exchange)** - Specifies the mail servers for accepting messages.
- **A record (address)** - Points a name to an IP address.
- **CNAME (canonical)** - Points a name to another name or ` CNAME ` (example.com to [www.example.com](http://www.example.com/)) or to an ` A ` record.

Services such as [CloudFlare](https://www.cloudflare.com/dns/) and [Route 53](https://aws.amazon.com/route53/) provide managed DNS services. Some DNS services can route traffic through various methods:

- [Weighted round robin](http://g33kinfo.com/info/archives/2657)
    - Prevent traffic from going to servers under maintenance
    - Balance between varying cluster sizes
    - A/B testing
- Latency-based
- Geolocation-based

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-dns)Disadvantage(s): DNS

- Accessing a DNS server introduces a slight delay, although mitigated by caching described above.
- DNS server management could be complex, although they are generally managed by [governments, ISPs, and large companies](http://superuser.com/questions/472695/who-controls-the-dns-servers/472729).
- DNS services have recently come under [DDoS attack](http://dyn.com/blog/dyn-analysis-summary-of-friday-october-21-attack/), preventing users from accessing websites such as Twitter without knowing Twitter's IP address(es).

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-5)Source(s) and further reading

- [DNS architecture](https://technet.microsoft.com/en-us/library/dd197427(v=ws.10).aspx)
- [Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [DNS articles](https://support.dnsimple.com/categories/dns/)

## [(L)](https://github.com/donnemartin/system-design-primer#content-delivery-network)Content delivery network

 [![687474703a2f2f692e696d6775722e636f6d2f683954417547492e6a7067.jpg](../_resources/a5d9b5886e616ac9edddbd85b4a684ba.jpg)](https://camo.githubusercontent.com/853a8603651149c686bf3c504769fc594ff08849/687474703a2f2f692e696d6775722e636f6d2f683954417547492e6a7067)

 *[Source: Why use a CDN](https://www.creative-artworks.eu/why-use-a-content-delivery-network-cdn/)*

A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JSS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:

- Users receive content at data centers close to them
- Your servers do not have to serve requests that the CDN fulfills

### [(L)](https://github.com/donnemartin/system-design-primer#push-cdns)Push CDNs

Push CDNs receive new content whenever changes occur on your server. You take full responsibility for providing content, uploading directly to the CDN and rewriting URLs to point to the CDN. You can configure when content expires and when it is updated. Content is uploaded only when it is new or changed, minimizing traffic, but maximizing storage.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

### [(L)](https://github.com/donnemartin/system-design-primer#pull-cdns)Pull CDNs

Pull CDNs grab new content from your server when the first user requests the content. You leave the content on your server and rewrite URLs to point to the CDN. This results in a slower request until the content is cached on the server.

A [time-to-live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) determines how long content is cached. Pull CDNs minimize storage space on the CDN, but can create redundant traffic if files expire and are pulled before they have actually changed.

Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-cdn)Disadvantage(s): CDN

- CDN costs could be significant depending on traffic, although this should be weighed with additional costs you would incur not using a CDN.
- Content might be stale if it is updated before the TTL expires it.
- CDNs require changing URLs for static content to point to the CDN.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-6)Source(s) and further reading

- [Globally distributed content delivery](http://repository.cmu.edu/cgi/viewcontent.cgi?article=2112&context=compsci)
- [The differences between push and pull CDNs](http://www.travelblogadvice.com/technical/the-differences-between-push-and-pull-cdns/)
- [Wikipedia](https://en.wikipedia.org/wiki/Content_delivery_network)

## [(L)](https://github.com/donnemartin/system-design-primer#load-balancer)Load balancer

 [![687474703a2f2f692e696d6775722e636f6d2f6838316e39694b2e706e67.png](../_resources/9ae0d0b17d66320605125cce873ed2e6.png)](https://camo.githubusercontent.com/21caea3d7f67f451630012f657ae59a56709365c/687474703a2f2f692e696d6775722e636f6d2f6838316e39694b2e706e67)

 *[Source: Scalable system design patterns](http://horicky.blogspot.com/2010/10/scalable-system-design-patterns.html)*

Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:

- Preventing requests from going to unhealthy servers
- Preventing overloading resources
- Helping eliminate single points of failure

Load balancers can be implemented with hardware (expensive) or with software such as HAProxy.

Additional benefits include:

- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
    - Removes the need to install [X.509 certificates](https://en.wikipedia.org/wiki/X.509) on each server
- **Session persistence** - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions

To protect against failures, it's common to set up multiple load balancers, either in [active-passive](https://github.com/donnemartin/system-design-primer#active-passive) or [active-active](https://github.com/donnemartin/system-design-primer#active-active) mode.

Load balancers can route traffic based on various metrics, including:

- Random
- Least loaded
- Session/cookies
- [Round robin or weighted round robin](http://g33kinfo.com/info/archives/2657)
- [Layer 4](https://github.com/donnemartin/system-design-primer#layer-4-load-balancing)
- [Layer 7](https://github.com/donnemartin/system-design-primer#layer-7-load-balancing)

### [(L)](https://github.com/donnemartin/system-design-primer#layer-4-load-balancing)Layer 4 load balancing

Layer 4 load balancers look at info at the [transport layer](https://github.com/donnemartin/system-design-primer#communication) to decide how to distribute requests. Generally, this involves the source, destination IP addresses, and ports in the header, but not the contents of the packet. Layer 4 load balancers forward network packets to and from the upstream server, performing [Network Address Translation (NAT)](https://www.nginx.com/resources/glossary/layer-4-load-balancing/).

### [(L)](https://github.com/donnemartin/system-design-primer#layer-7-load-balancing)layer 7 load balancing

Layer 7 load balancers look at the [application layer](https://github.com/donnemartin/system-design-primer#communication) to decide how to distribute requests. This can involve contents of the header, message, and cookies. Layer 7 load balancers terminates network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.

At the cost of flexibility, layer 4 load balancing requires less time and computing resources than Layer 7, although the performance impact can be minimal on modern commodity hardware.

### [(L)](https://github.com/donnemartin/system-design-primer#horizontal-scaling)Horizontal scaling

Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called **Vertical Scaling**. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.

#### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-horizontal-scaling)Disadvantage(s): horizontal scaling

- Scaling horizontally introduces complexity and involves cloning servers
    - Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
    - Sessions can be stored in a centralized data store such as a [database](https://github.com/donnemartin/system-design-primer#database) (SQL, NoSQL) or a persistent [cache](https://github.com/donnemartin/system-design-primer#cache) (Redis, Memcached)
- Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-load-balancer)Disadvantage(s): load balancer

- The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
- Introducing a load balancer to help eliminate single points of failure results in increased complexity.
- A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-7)Source(s) and further reading

- [NGINX architecture](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
- [HAProxy architecture guide](http://www.haproxy.org/download/1.2/doc/architecture.txt)
- [Scalability](http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones)
- [Wikipedia](https://en.wikipedia.org/wiki/Load_balancing_(computing))
- [Layer 4 load balancing](https://www.nginx.com/resources/glossary/layer-4-load-balancing/)
- [Layer 7 load balancing](https://www.nginx.com/resources/glossary/layer-7-load-balancing/)
- [ELB listener config](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html)

## [(L)](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)Reverse proxy (web server)

 [![687474703a2f2f692e696d6775722e636f6d2f6e3431417a66662e706e67.png](../_resources/ba520c5acba9d1ea9398837076b479db.png)](https://camo.githubusercontent.com/e88216d0999853426f72b28e41223f43977d22b7/687474703a2f2f692e696d6775722e636f6d2f6e3431417a66662e706e67)

 *[Source: Wikipedia](https://upload.wikimedia.org/wikipedia/commons/6/67/Reverse_proxy_h2g2bob.svg)*

A reverse proxy is a web server that centralizes internal services and provides unified interfaces to the public. Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client.

Additional benefits include:

- **Increased security** - Hide information about backend servers, blacklist IPs, limit number of connections per client
- **Increased scalability and flexibility** - Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration
- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
    - Removes the need to install [X.509 certificates](https://en.wikipedia.org/wiki/X.509) on each server
- **Compression** - Compress server responses
- **Caching** - Return the response for cached requests
- **Static content** - Serve static content directly
    - HTML/CSS/JS
    - Photos
    - Videos
    - Etc

### [(L)](https://github.com/donnemartin/system-design-primer#load-balancer-vs-reverse-proxy)Load balancer vs reverse proxy

- Deploying a load balancer is useful when you have multiple servers. Often, load balancers route traffic to a set of servers serving the same function.
- Reverse proxies can be useful even with just one web server or application server, opening up the benefits described in the previous section.
- Solutions such as NGINX and HAProxy can support both layer 7 reverse proxying and load balancing.

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-reverse-proxy)Disadvantage(s): reverse proxy

- Introducing a reverse proxy results in increased complexity.
- A single reverse proxy is a single point of failure, configuring multiple reverse proxies (ie a [failover](https://en.wikipedia.org/wiki/Failover)) further increases complexity.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-8)Source(s) and further reading

- [Reverse proxy vs load balancer](https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/)
- [NGINX architecture](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
- [HAProxy architecture guide](http://www.haproxy.org/download/1.2/doc/architecture.txt)
- [Wikipedia](https://en.wikipedia.org/wiki/Reverse_proxy)

## [(L)](https://github.com/donnemartin/system-design-primer#application-layer)Application layer

 [![687474703a2f2f692e696d6775722e636f6d2f7942355359776d2e706e67.png](../_resources/3c601ae1fbfaa18076be561b875fa04c.png)](https://camo.githubusercontent.com/feeb549c5b6e94f65c613635f7166dc26e0c7de7/687474703a2f2f692e696d6775722e636f6d2f7942355359776d2e706e67)

 *[Source: Intro to architecting systems for scale](http://lethain.com/introduction-to-architecting-systems-for-scale/#platform_layer)*

Separating out the web layer from the application layer (also known as platform layer) allows you to scale and configure both layers independently. Adding a new API results in adding application servers without necessarily adding additional web servers.

The **single responsibility principle** advocates for small and autonomous services that work together. Small teams with small services can plan more aggressively for rapid growth.

Workers in the application layer also help enable [asynchronism](https://github.com/donnemartin/system-design-primer#asynchronism).

### [(L)](https://github.com/donnemartin/system-design-primer#microservices)Microservices

Related to this discussion are [microservices](https://en.wikipedia.org/wiki/Microservices), which can be described as a suite of independently deployable, small, modular services. Each service runs a unique process and communicates through a well-defined, lightweight mechanism to serve a business goal. [1](https://smartbear.com/learn/api-design/what-are-microservices)

Pinterest, for example, could have the following microservices: user profile, follower, feed, search, photo upload, etc.

### [(L)](https://github.com/donnemartin/system-design-primer#service-discovery)Service Discovery

Systems such as [Zookeeper](http://www.slideshare.net/sauravhaloi/introduction-to-apache-zookeeper) can help services find each other by keeping track of registered names, addresses, ports, etc.

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-application-layer)Disadvantage(s): application layer

- Adding an application layer with loosely coupled services requires a different approach from an architectural, operations, and process viewpoint (vs a monolithic system).
- Microservices can add complexity in terms of deployments and operations.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-9)Source(s) and further reading

- [Intro to architecting systems for scale](http://lethain.com/introduction-to-architecting-systems-for-scale)
- [Crack the system design interview](http://www.puncsky.com/blog/2016/02/14/crack-the-system-design-interview/)
- [Service oriented architecture](https://en.wikipedia.org/wiki/Service-oriented_architecture)
- [Introduction to Zookeeper](http://www.slideshare.net/sauravhaloi/introduction-to-apache-zookeeper)
- [Here's what you need to know about building microservices](https://cloudncode.wordpress.com/2016/07/22/msa-getting-started/)

## [(L)](https://github.com/donnemartin/system-design-primer#database)Database

 [![687474703a2f2f692e696d6775722e636f6d2f586b6d3543587a2e706e67.png](../_resources/be2f670bbf9f85752fc876b05e867a10.png)](https://camo.githubusercontent.com/15a7553727e6da98d0de5e9ca3792f6d2b5e92d4/687474703a2f2f692e696d6775722e636f6d2f586b6d3543587a2e706e67)

 *[Source: Scaling up to your first 10 million users](https://www.youtube.com/watch?v=vg5onp8TU6Q)*

### [(L)](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)Relational database management system (RDBMS)

A relational database like SQL is a collection of data items organized in tables.

**ACID** is a set of properties of relational database [transactions](https://en.wikipedia.org/wiki/Database_transaction).

- **Atomicity** - Each transaction is all or nothing
- **Consistency** - Any transaction will bring the database from one valid state to another
- **Isolation** - Executing transactions concurrently has the same results as if the transactions were executed serially
- **Durability** - Once a transaction has been committed, it will remain so

There are many techniques to scale a relational database: **master-slave replication**, **master-master replication**, **federation**, **sharding**, **denormalization**, and **SQL tuning**.

#### [(L)](https://github.com/donnemartin/system-design-primer#master-slave-replication)Master-slave replication

The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.

 [![687474703a2f2f692e696d6775722e636f6d2f4339696f47746e2e706e67.png](../_resources/a7e66c26d2c3247b11cc32e7e8d8ce56.png)](https://camo.githubusercontent.com/6a097809b9690236258747d969b1d3e0d93bb8ca/687474703a2f2f692e696d6775722e636f6d2f4339696f47746e2e706e67)

 *[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-master-slave-replication)Disadvantage(s): master-slave replication

- Additional logic is needed to promote a slave to a master.
- See [Disadvantage(s): replication](https://github.com/donnemartin/system-design-primer#disadvantages-replication) for points related to **both** master-slave and master-master.

#### [(L)](https://github.com/donnemartin/system-design-primer#master-master-replication)Master-master replication

Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.

 [![687474703a2f2f692e696d6775722e636f6d2f6b7241484c47672e706e67.png](../_resources/347d5a7116f860877f3988d22f24e176.png)](https://camo.githubusercontent.com/5862604b102ee97d85f86f89edda44bde85a5b7f/687474703a2f2f692e696d6775722e636f6d2f6b7241484c47672e706e67)

 *[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-master-master-replication)Disadvantage(s): master-master replication

- You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
- Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
- Conflict resolution comes more into play as more write nodes are added and as latency increases.
- See [Disadvantage(s): replication](https://github.com/donnemartin/system-design-primer#disadvantages-replication) for points related to **both** master-slave and master-master.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-replication)Disadvantage(s): replication

- There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
- Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
- The more read slaves, the more you have to replicate, which leads to greater replication lag.
- On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
- Replication adds more hardware and additional complexity.

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-replication)Source(s) and further reading: replication

- [Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)
- [Multi-master replication](https://en.wikipedia.org/wiki/Multi-master_replication)

#### [(L)](https://github.com/donnemartin/system-design-primer#federation)Federation

 [![687474703a2f2f692e696d6775722e636f6d2f553371563333652e706e67.png](../_resources/b1c4683a3ab0eea1d9cf95fc6170c777.png)](https://camo.githubusercontent.com/6eb6570a8b6b4e1d52e3d7cc07e7959ea5dac75f/687474703a2f2f692e696d6775722e636f6d2f553371563333652e706e67)

 *[Source: Scaling up to your first 10 million users](https://www.youtube.com/watch?v=vg5onp8TU6Q)*

Federation (or functional partitioning) splits up databases by function. For example, instead of a single, monolithic database, you could have three databases: **forums**, **users**, and **products**, resulting in less read and write traffic to each database and therefore less replication lag. Smaller databases result in more data that can fit in memory, which in turn results in more cache hits due to improved cache locality. With no single central master serializing writes you can write in parallel, increasing throughput.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-federation)Disadvantage(s): federation

- Federation is not effective if your schema requires huge functions or tables.
- You'll need to update your application logic to determine which database to read and write.
- Joining data from two databases is more complex with a [server link](http://stackoverflow.com/questions/5145637/querying-data-by-joining-two-tables-in-two-database-on-different-servers).
- Federation adds more hardware and additional complexity.

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-federation)Source(s) and further reading: federation

- [Scaling up to your first 10 million users](https://www.youtube.com/watch?v=vg5onp8TU6Q)

#### [(L)](https://github.com/donnemartin/system-design-primer#sharding)Sharding

 [![687474703a2f2f692e696d6775722e636f6d2f775538783549642e706e67.png](../_resources/60f5df987fb2b031eb64457e572f41e6.png)](https://camo.githubusercontent.com/1df78be67b749171569a0e11a51aa76b3b678d4f/687474703a2f2f692e696d6775722e636f6d2f775538783549642e706e67)

 *[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

Sharding distributes data across different databases such that each database can only manage a subset of the data. Taking a users database as an example, as the number of users increases, more shards are added to the cluster.

Similar to the advantages of [federation](https://github.com/donnemartin/system-design-primer#federation), sharding results in less read and write traffic, less replication, and more cache hits. Index size is also reduced, which generally improves performance with faster queries. If one shard goes down, the other shards are still operational, although you'll want to add some form of replication to avoid data loss. Like federation, there is no single central master serializing writes, allowing you to write in parallel with increased throughput.

Common ways to shard a table of users is either through the user's last name initial or the user's geographic location.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-sharding)Disadvantage(s): sharding

- You'll need to update your application logic to work with shards, which could result in complex SQL queries.
- Data distribution can become lopsided in a shard. For example, a set of power users on a shard could result in increased load to that shard compared to others.
    - Rebalancing adds additional complexity. A sharding function based on [consistent hashing](http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html) can reduce the amount of transferred data.
- Joining data from multiple shards is more complex.
- Sharding adds more hardware and additional complexity.

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-sharding)Source(s) and further reading: sharding

- [The coming of the shard](http://highscalability.com/blog/2009/8/6/an-unorthodox-approach-to-database-design-the-coming-of-the.html)
- [Shard database architecture](https://en.wikipedia.org/wiki/Shard_(database_architecture))
- [Consistent hashing](http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html)

#### [(L)](https://github.com/donnemartin/system-design-primer#denormalization)Denormalization

Denormalization attempts to improve read performance at the expense of some write performance. Redundant copies of the data are written in multiple tables to avoid expensive joins. Some RDBMS such as [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) and Oracle support [materialized views](https://en.wikipedia.org/wiki/Materialized_view) which handle the work of storing redundant information and keeping redundant copies consistent.

Once data becomes distributed with techniques such as [federation](https://github.com/donnemartin/system-design-primer#federation) and [sharding](https://github.com/donnemartin/system-design-primer#sharding), managing joins across data centers further increases complexity. Denormalization might circumvent the need for such complex joins.

In most systems, reads can heavily number writes 100:1 or even 1000:1. A read resulting in a complex database join can be very expensive, spending a significant amount of time on disk operations.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-denormalization)Disadvantage(s): denormalization

- Data is duplicated.
- Constraints can help redundant copies of information stay in sync, which increases complexity of the database design.
- A denormalized database under heavy write load might perform worse than its normalized counterpart.

###### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-denormalization)Source(s) and further reading: denormalization

- [Denormalization](https://en.wikipedia.org/wiki/Denormalization)

#### [(L)](https://github.com/donnemartin/system-design-primer#sql-tuning)SQL tuning

SQL tuning is a broad topic and many [books](https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=sql+tuning) have been written as reference.

It's important to **benchmark** and **profile** to simulate and uncover bottlenecks.

- **Benchmark** - Simulate high-load situations with tools such as [ab](http://httpd.apache.org/docs/2.2/programs/ab.html).
- **Profile** - Enable tools such as the [slow query log](http://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html) to help track performance issues.

Benchmarking and profiling might point you to the following optimizations.

##### [(L)](https://github.com/donnemartin/system-design-primer#tighten-up-the-schema)Tighten up the schema

- MySQL dumps to disk in contiguous blocks for fast access.
- Use ` CHAR ` instead of ` VARCHAR ` for fixed-length fields.
    - ` CHAR ` effectively allows for fast, random access, whereas with ` VARCHAR `, you must find the end of a string before moving onto the next one.
- Use ` TEXT ` for large blocks of text such as blog posts. ` TEXT ` also allows for boolean searches. Using a ` TEXT ` field results in storing a pointer on disk that is used to locate the text block.
- Use ` INT ` for larger numbers up to 2^32 or 4 billion.
- Use ` DECIMAL ` for currency to avoid floating point representation errors.
- Avoid storing large ` BLOBS `, store the location of where to get the object instead.
- ` VARCHAR(255) ` is the largest number of characters that can be counted in an 8 bit number, often maximizing the use of a byte in some RDBMS.
- Set the ` NOT NULL ` constraint where applicable to [improve search performance](http://stackoverflow.com/questions/1017239/how-do-null-values-affect-performance-in-a-database-search).

##### [(L)](https://github.com/donnemartin/system-design-primer#use-good-indices)Use good indices

- Columns that you are querying (` SELECT `, ` GROUP BY `, ` ORDER BY `, ` JOIN `) could be faster with indices.
- Indices are usually represented as self-balancing [B-tree](https://en.wikipedia.org/wiki/B-tree) that keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time.
- Placing an index can keep the data in memory, requiring more space.
- Writes could also be slower since the index also needs to be updated.
- When loading large amounts of data, it might be faster to disable indices, load the data, then rebuild the indices.

##### [(L)](https://github.com/donnemartin/system-design-primer#avoid-expensive-joins)Avoid expensive joins

- [Denormalize](https://github.com/donnemartin/system-design-primer#denormalization) where performance demands it.

##### [(L)](https://github.com/donnemartin/system-design-primer#partition-tables)Partition tables

- Break up a table by putting hot spots in a separate table to help keep it in memory.

##### [(L)](https://github.com/donnemartin/system-design-primer#tune-the-query-cache)Tune the query cache

- In some cases, the [query cache](http://dev.mysql.com/doc/refman/5.7/en/query-cache) could lead to [performance issues](https://www.percona.com/blog/2014/01/28/10-mysql-performance-tuning-settings-after-installation/).

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-sql-tuning)Source(s) and further reading: SQL tuning

- [Tips for optimizing MySQL queries](http://20bits.com/article/10-tips-for-optimizing-mysql-queries-that-dont-suck)
- [Is there a good reason i see VARCHAR(255) used so often?](http://stackoverflow.com/questions/1217466/is-there-a-good-reason-i-see-varchar255-used-so-often-as-opposed-to-another-l)
- [How do null values affect performance?](http://stackoverflow.com/questions/1017239/how-do-null-values-affect-performance-in-a-database-search)
- [Slow query log](http://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html)

### [(L)](https://github.com/donnemartin/system-design-primer#nosql)NoSQL

NoSQL is a collection of data items represented in a **key-value store**, **document-store**, **wide column store**, or a **graph database**. Data is denormalized, and joins are generally done in the application code. Most NoSQL stores lack true ACID transactions and favor [eventual consistency](https://github.com/donnemartin/system-design-primer#eventual-consistency).

**BASE** is often used to describe the properties of NoSQL databases. In comparison with the [CAP Theorem](https://github.com/donnemartin/system-design-primer#cap-theorem), BASE chooses availability over consistency.

- **Basically available** - the system guarantees availability.
- **Soft state** - the state of the system may change over time, even without input.
- **Eventual consistency** - the system will become consistent over a period of time, given that the system doesn't receive input during that period.

In addition to choosing between [SQL or NoSQL](https://github.com/donnemartin/system-design-primer#sql-or-nosql), it is helpful to understand which type of NoSQL database best fits your use case(s). We'll review **key-value stores**, **document-stores**, **wide column stores**, and **graph databases** in the next section.

#### [(L)](https://github.com/donnemartin/system-design-primer#key-value-store)Key-value store

> Abstraction: hash table

A key-value store generally allows for O(1) reads and writes and is often backed by memory or SSD. Data stores can maintain keys in [lexicographic order](https://en.wikipedia.org/wiki/Lexicographical_order), allowing efficient retrieval of key ranges. Key-value stores can allow for storing of metadata with a value.

Key-value stores provide high performance and are often used for simple data models or for rapidly-changing data, such as an in-memory cache layer. Since they offer only a limited set of operations, complexity is shifted to the application layer if additional operations are needed.

A key-value store is the basis for more complex system systems such as a document store, and in some cases, a graph database.

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-key-value-store)Source(s) and further reading: key-value store

- [Key-value database](https://en.wikipedia.org/wiki/Key-value_database)
- [Disadvantages of key-value stores](http://stackoverflow.com/questions/4056093/what-are-the-disadvantages-of-using-a-key-value-table-over-nullable-columns-or)
- [Redis architecture](http://qnimate.com/overview-of-redis-architecture/)
- [Memcached architecture](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)

#### [(L)](https://github.com/donnemartin/system-design-primer#document-store)Document store

> Abstraction: key-value store with documents stored as values

A document store is centered around documents (XML, JSON, binary, etc), where a document stores all information for a given object. Document stores provide APIs or a query language to query based on the internal structure of the document itself. *Note, many key-value stores include features for working with a value's metadata, blurring the lines between these two storage types.*

Based on the underlying implementation, documents are organized in either collections, tags, metadata, or directories. Although documents can be organized or grouped together, documents may have fields that are completely different from each other.

Some document stores like [MongoDB](https://www.mongodb.com/mongodb-architecture) and [CouchDB](https://blog.couchdb.org/2016/08/01/couchdb-2-0-architecture/) also provide a SQL-like language to perform complex queries. [DynamoDB](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/decandia07dynamo.pdf) supports both key-values and documents.

Document stores provide high flexibility and are often used for working with occasionally changing data.

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-document-store)Source(s) and further reading: document store

- [Document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database)
- [MongoDB architecture](https://www.mongodb.com/mongodb-architecture)
- [CouchDB architecture](https://blog.couchdb.org/2016/08/01/couchdb-2-0-architecture/)
- [Elasticsearch architecture](https://www.elastic.co/blog/found-elasticsearch-from-the-bottom-up)

#### [(L)](https://github.com/donnemartin/system-design-primer#wide-column-store)Wide column store

 [![687474703a2f2f692e696d6775722e636f6d2f6e3136694f476b2e706e67.png](../_resources/060b2652f1966b8d39aa3cecf208e88e.png)](https://camo.githubusercontent.com/823668b07b4bff50574e934273c9244e4e5017d6/687474703a2f2f692e696d6775722e636f6d2f6e3136694f476b2e706e67)

 *[Source: SQL & NoSQL, a brief history](http://blog.grio.com/2015/11/sql-nosql-a-brief-history.html)*

> Abstraction: nested map ` ColumnFamily<RowKey, Columns<ColKey, Value, Timestamp>> `

A wide column store's basic unit of data is a column (name/value pair). A column can be grouped in column families (analogous to a SQL table). Super column families further group column families. You can access each column independently with a row key, and columns with the same row key form a row. Each value contains a timestamp for versioning and for conflict resolution.

Google introduced [Bigtable](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/chang06bigtable.pdf) as the first wide column store, which influenced the open-source [HBase](https://www.mapr.com/blog/in-depth-look-hbase-architecture) often-used in the Hadoop ecosystem, and [Cassandra](http://docs.datastax.com/en/archived/cassandra/2.0/cassandra/architecture/architectureIntro_c.html) from Facebook. Stores such as BigTable, HBase, and Cassandra maintain keys in lexicographic order, allowing efficient retrieval of selective key ranges.

Wide column stores offer high availability and high scalability. They are often used for very large data sets.

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-wide-column-store)Source(s) and further reading: wide column store

- [SQL & NoSQL, a brief history](http://blog.grio.com/2015/11/sql-nosql-a-brief-history.html)
- [Bigtable architecture](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/chang06bigtable.pdf)
- [HBase architecture](https://www.mapr.com/blog/in-depth-look-hbase-architecture)
- [Cassandra architecture](http://docs.datastax.com/en/archived/cassandra/2.0/cassandra/architecture/architectureIntro_c.html)

#### [(L)](https://github.com/donnemartin/system-design-primer#graph-database)Graph database

 [![687474703a2f2f692e696d6775722e636f6d2f664e636c3635672e706e67.png](../_resources/a4aded7d49d545f742794b52efa8b101.png)](https://camo.githubusercontent.com/bf6508b65e98a7210d9861515833afa0d9434436/687474703a2f2f692e696d6775722e636f6d2f664e636c3635672e706e67)

 *[Source: Graph database](https://en.wikipedia.org/wiki/File:GraphDatabase_PropertyGraph.png)*

> Abstraction: graph

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.

Graphs databases offer high performance for data models with complex relationships, such as a social network. They are relatively new and are not yet widely-used; it might be more difficult to find development tools and resources. Many graphs can only be accessed with [REST APIs](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest).

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-graph)Source(s) and further reading: graph

- [Graph database](https://en.wikipedia.org/wiki/Graph_database)
- [Neo4j](https://neo4j.com/)
- [FlockDB](https://blog.twitter.com/2010/introducing-flockdb)

#### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-nosql)Source(s) and further reading: NoSQL

- [Explanation of base terminology](http://stackoverflow.com/questions/3342497/explanation-of-base-terminology)
- [NoSQL databases a survey and decision guidance](https://medium.com/baqend-blog/nosql-databases-a-survey-and-decision-guidance-ea7823a822d#.wskogqenq)
- [Scalability](http://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database)
- [Introduction to NoSQL](https://www.youtube.com/watch?v=qI_g07C_Q5I)
- [NoSQL patterns](http://horicky.blogspot.com/2009/11/nosql-patterns.html)

### [(L)](https://github.com/donnemartin/system-design-primer#sql-or-nosql)SQL or NoSQL

 [![687474703a2f2f692e696d6775722e636f6d2f775847714735662e706e67.png](../_resources/383b1dc746b7c83ddd385c9525739bf5.png)](https://camo.githubusercontent.com/a6e2e844765c9d5382d9c9b64ef7693977981646/687474703a2f2f692e696d6775722e636f6d2f775847714735662e706e67)

 *[Source: Transitioning from RDBMS to NoSQL](https://www.infoq.com/articles/Transition-RDBMS-NoSQL/)*

Reasons for **SQL**:

- Structured data
- Strict schema
- Relational data
- Need for complex joins
- Transactions
- Clear patterns for scaling
- More established: developers, community, code, tools, etc
- Lookups by index are very fast

Reasons for **NoSQL**:

- Semi-structured data
- Dynamic or flexible schema
- Non relational data
- No need for complex joins
- Store many TB (or PB) of data
- Very data intensive workload
- Very high throughput for IOPS

Sample data well-suited for NoSQL:

- Rapid ingest of clickstream and log data
- Leaderboard or scoring data
- Temporary data, such as a shopping cart
- Frequently accessed ('hot') tables
- Metadata/lookup tables

##### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-sql-or-nosql)Source(s) and further reading: SQL or NoSQL

- [Scaling up to your first 10 million users](https://www.youtube.com/watch?v=vg5onp8TU6Q)
- [SQL vs NoSQL differences](https://www.sitepoint.com/sql-vs-nosql-differences/)

## [(L)](https://github.com/donnemartin/system-design-primer#cache)Cache

 [![687474703a2f2f692e696d6775722e636f6d2f51367a32344c612e706e67.png](../_resources/9a4060913d7622ab7ebeda06443f1339.png)](https://camo.githubusercontent.com/7acedde6aa7853baf2eb4a53f88e2595ebe43756/687474703a2f2f692e696d6775722e636f6d2f51367a32344c612e706e67)

 *[Source: Scalable system design patterns](http://horicky.blogspot.com/2010/10/scalable-system-design-patterns.html)*

Caching improves page load times and can reduce the load on your servers and databases. In this model, the dispatcher will first lookup if the request has been made before and try to find the previous result to return, in order to save the actual execution.

Databases often benefit from a uniform distribution of reads and writes across its partitions. Popular items can skew the distribution, causing bottlenecks. Putting a cache in front of a database can help absorb uneven loads and spikes in traffic.

### [(L)](https://github.com/donnemartin/system-design-primer#client-caching)Client caching

Caches can be located on the client side (OS or browser), [server side](https://github.com/donnemartin/system-design-primer#reverse-proxy), or in a distinct cache layer.

### [(L)](https://github.com/donnemartin/system-design-primer#cdn-caching)CDN caching

[CDNs](https://github.com/donnemartin/system-design-primer#content-delivery-network) are considered a type of cache.

### [(L)](https://github.com/donnemartin/system-design-primer#web-server-caching)Web server caching

[Reverse proxies](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server) and caches such as [Varnish](https://www.varnish-cache.org/) can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.

### [(L)](https://github.com/donnemartin/system-design-primer#database-caching)Database caching

Your database usually includes some level of caching in a default configuration, optimized for a generic use case. Tweaking these settings for specific usage patterns can further boost performance.

### [(L)](https://github.com/donnemartin/system-design-primer#application-caching)Application caching

In-memory caches such as Memcached and Redis are key-value stores between your application and your data storage. Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. RAM is more limited than disk, so [cache invalidation](https://en.wikipedia.org/wiki/Cache_algorithms) algorithms such as [least recently used (LRU)](https://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used) can help invalidate 'cold' entries and keep 'hot' data in RAM.

Redis has the following additional features:

- Persistence option
- Built-in data structures such as sorted sets and lists

There are multiple levels you can cache that fall into two general categories: **database queries** and **objects**:

- Row level
- Query-level
- Fully-formed serializable objects
- Fully-rendered HTML

Generally, you should try to avoid file-based caching, as it makes cloning and auto-scaling more difficult.

### [(L)](https://github.com/donnemartin/system-design-primer#caching-at-the-database-query-level)Caching at the database query level

Whenever you query the database, hash the query as a key and store the result to the cache. This approach suffers from expiration issues:

- Hard to delete a cached result with complex queries
- If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell

### [(L)](https://github.com/donnemartin/system-design-primer#caching-at-the-object-level)Caching at the object level

See your data as an object, similar to what you do with your application code. Have your application assemble the dataset from the database into a class instance or a data structure(s):

- Remove the object from cache if its underlying data has changed
- Allows for asynchronous processing: workers assemble objects by consuming the latest cached object

Suggestions of what to cache:

- User sessions
- Fully rendered web pages
- Activity streams
- User graph data

### [(L)](https://github.com/donnemartin/system-design-primer#when-to-update-the-cache)When to update the cache

Since you can only store a limited amount of data in cache, you'll need to determine which cache update strategy works best for your use case.

#### [(L)](https://github.com/donnemartin/system-design-primer#cache-aside)Cache-aside

 [![687474703a2f2f692e696d6775722e636f6d2f4f4e6a4f52716b2e706e67.png](../_resources/e1704f13ec71e6767a1685de61128fcb.png)](https://camo.githubusercontent.com/7f5934e49a678b67f65e5ed53134bc258b007ebb/687474703a2f2f692e696d6775722e636f6d2f4f4e6a4f52716b2e706e67)

 *[Source: From cache to in-memory data grid](http://www.slideshare.net/tmatyashovsky/from-cache-to-in-memory-data-grid-introduction-to-hazelcast)*

The application is responsible for reading and writing from storage. The cache does not interact with storage directly. The application does the following:

- Look for entry in cache, resulting in a cache miss
- Load entry from the database
- Add entry to cache
- Return entry

	normaldef get_user(self, user_id):
	    user = cache.get("user.{0}", user_id)
	    if user is None:
	        user = db.query("SELECT * FROM users WHERE user_id = {0}", user_id)
	        if user is not None:
	            cache.set(key, json.dumps(user))
	    return user
	normal

[Memcached](https://memcached.org/) is generally used in this manner.

Subsequent reads of data added to cache are fast. Cache-aside is also referred to as lazy loading. Only requested data is cached, which avoids filling up the cache with data that isn't requested.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-cache-aside)Disadvantage(s): cache-aside

- Each cache miss results in three trips, which can cause a noticeable delay.
- Data can become stale if it is updated in the database. This issue is mitigated by setting a time-to-live (TTL) which forces an update of the cache entry, or by using write-through.
- When a node fails, it is replaced by a new, empty node, increasing latency.

#### [(L)](https://github.com/donnemartin/system-design-primer#write-through)Write-through

 [![687474703a2f2f692e696d6775722e636f6d2f3076426330684e2e706e67.png](../_resources/b43afe5eba3255a6518f780614fa6b0c.png)](https://camo.githubusercontent.com/56b870f4d199335ccdbc98b989ef6511ed14f0e2/687474703a2f2f692e696d6775722e636f6d2f3076426330684e2e706e67)

 *[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:

- Application adds/updates entry in cache
- Cache synchronously writes entry to data store
- Return

Application code:

	normalset_user(12345, {"foo":"bar"})
	normal

Cache code:

	normaldef set_user(user_id, values):
	    user = db.query("UPDATE Users WHERE id = {0}", user_id, values)
	    cache.set(user_id, user)
	normal

Write-through is a slow overall operation due to the write operation, but subsequent reads of just written data are fast. Users are generally more tolerant of latency when updating data than reading data. Data in the cache is not stale.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-write-through)Disadvantage(s): write through

- When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. Cache-aside in conjunction with write through can mitigate this issue.
- Most data written might never read, which can be minimized with a TTL.

#### [(L)](https://github.com/donnemartin/system-design-primer#write-behind-write-back)Write-behind (write-back)

 [![687474703a2f2f692e696d6775722e636f6d2f72675372766a472e706e67.png](../_resources/960e8fe4187a91d24c267a7ee6333510.png)](https://camo.githubusercontent.com/8aa9f1a2f050c1422898bb5e82f1f01773334e22/687474703a2f2f692e696d6775722e636f6d2f72675372766a472e706e67)

 *[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

In write-behind, tha application does the following:

- Add/update entry in cache
- Asynchronously write entry to the data store, improving write performance

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-write-behind)Disadvantage(s): write-behind

- There could be data loss if the cache goes down prior to its contents hitting the data store.
- It is more complex to implement write-behind than it is to implement cache-aside or write-through.

#### [(L)](https://github.com/donnemartin/system-design-primer#refresh-ahead)Refresh-ahead

 [![687474703a2f2f692e696d6775722e636f6d2f6b78746a7167452e706e67.png](../_resources/f91bca9fa309beb3f9233bd96a027bde.png)](https://camo.githubusercontent.com/49dcb54307763b4f56d61a4a1369826e2e7d52e4/687474703a2f2f692e696d6775722e636f6d2f6b78746a7167452e706e67)

 *[Source: From cache to in-memory data grid](http://www.slideshare.net/tmatyashovsky/from-cache-to-in-memory-data-grid-introduction-to-hazelcast)*

You can configure the cache to automatically refresh any recently accessed cache entry prior to its expiration.

Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.

##### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-refresh-ahead)Disadvantage(s): refresh-ahead

- Not accurately predicting which items are likely to be needed in the future can result in reduced performance than without refresh-ahead.

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-cache)Disadvantage(s): cache

- Need to maintain consistency between caches and the source of truth such as the database through [cache invalidation](https://en.wikipedia.org/wiki/Cache_algorithms).
- Need to make application changes such as adding Redis or memcached.
- Cache invalidation is a difficult problem, there is additional complexity associated with when to update the cache.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-10)Source(s) and further reading

- [From cache to in-memory data grid](http://www.slideshare.net/tmatyashovsky/from-cache-to-in-memory-data-grid-introduction-to-hazelcast)
- [Scalable system design patterns](http://horicky.blogspot.com/2010/10/scalable-system-design-patterns.html)
- [Introduction to architecting systems for scale](http://lethain.com/introduction-to-architecting-systems-for-scale/)
- [Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)
- [Scalability](http://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache)
- [AWS ElastiCache strategies](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Strategies.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Cache_(computing))

## [(L)](https://github.com/donnemartin/system-design-primer#asynchronism)Asynchronism

 [![687474703a2f2f692e696d6775722e636f6d2f353447597353782e706e67.png](../_resources/ddcaa93459da99671d385753f631a64d.png)](https://camo.githubusercontent.com/c01ec137453216bbc188e3a8f16da39ec9131234/687474703a2f2f692e696d6775722e636f6d2f353447597353782e706e67)

 *[Source: Intro to architecting systems for scale](http://lethain.com/introduction-to-architecting-systems-for-scale/#platform_layer)*

Asynchronous workflows help reduce request times for expensive operations that would otherwise be performed in-line. They can also help by doing time-consuming work in advance, such as periodic aggregation of data.

### [(L)](https://github.com/donnemartin/system-design-primer#message-queues)Message queues

Message queues receive, hold, and deliver messages. If an operation is too slow to perform inline, you can use a message queue with the following workflow:

- An application publishes a job to the queue, then notifies the user of job status
- A worker picks up the job from the queue, processes it, then signals the job is complete

The user is not blocked and the job is processed in the background. During this time, the client might optionally do a small amount of processing to make it seem like the task has completed. For example, if posting a tweet, the tweet could be instantly posted to your timeline, but it could take some time before your tweet is actually delivered to all of your followers.

**Redis** is useful as a simple message broker but messages can be lost.

**RabbitMQ** is popular but requires you to adapt to the 'AMQP' protocol and manage your own nodes.

**Amazon SQS**, is hosted but can have high latency and has the possibility of messages being delivered twice.

### [(L)](https://github.com/donnemartin/system-design-primer#task-queues)Task queues

Tasks queues receive tasks and their related data, runs them, then delivers their results. They can support scheduling and can be used to run computationally-intensive jobs in the background.

**Celery** has support for scheduling and primarily has python support.

### [(L)](https://github.com/donnemartin/system-design-primer#back-pressure)Back pressure

If queues start to grow significantly, the queue size can become larger than memory, resulting in cache misses, disk reads, and even slower performance. [Back pressure](http://mechanical-sympathy.blogspot.com/2012/05/apply-back-pressure-when-overloaded.html) can help by limiting the queue size, thereby maintaining a high throughput rate and good response times for jobs already in the queue. Once the queue fills up, clients get a server busy or HTTP 503 status code to try again later. Clients can retry the request at a later time, perhaps with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff).

### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-asynchronism)Disadvantage(s): asynchronism

- Use cases such as inexpensive calculations and realtime workflows might be better suited for synchronous operations, as introducing queues can add delays and complexity.

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-11)Source(s) and further reading

- [It's all a numbers game](https://www.youtube.com/watch?v=1KRYH75wgy4)
- [Applying back pressure when overloaded](http://mechanical-sympathy.blogspot.com/2012/05/apply-back-pressure-when-overloaded.html)
- [Little's law](https://en.wikipedia.org/wiki/Little%27s_law)
- [What is the difference between a message queue and a task queue?](https://www.quora.com/What-is-the-difference-between-a-message-queue-and-a-task-queue-Why-would-a-task-queue-require-a-message-broker-like-RabbitMQ-Redis-Celery-or-IronMQ-to-function)

## [(L)](https://github.com/donnemartin/system-design-primer#communication)Communication

 [![687474703a2f2f692e696d6775722e636f6d2f354b656f6351732e6a7067.jpg](../_resources/3012dddf9f02def96ddd408b3bbb55a1.jpg)](https://camo.githubusercontent.com/1d761d5688d28ce1fb12a0f1c8191bca96eece4c/687474703a2f2f692e696d6775722e636f6d2f354b656f6351732e6a7067)

 *[Source: OSI 7 layer model](http://www.escotal.com/osilayer.html)*

### [(L)](https://github.com/donnemartin/system-design-primer#hypertext-transfer-protocol-http)Hypertext transfer protocol (HTTP)

HTTP is a method for encoding and transporting data between a client and a server. It is a request/response protocol: clients issue requests and servers issue responses with relevant content and completion status info about the request. HTTP is self-contained, allowing requests and responses to flow through many intermediate routers and servers that perform load balancing, caching, encryption, and compression.

A basic HTTP request consists of a verb (method) and a resource (endpoint). Below are common HTTP verbs:

| Verb | Description | Idempotent* | Safe | Cacheable |
| --- | --- | --- | --- | --- |
| GET | Reads a resource | Yes | Yes | Yes |
| POST | Creates a resource or trigger a process that handles data | No  | No  | Yes if response contains freshness info |
| PUT | Creates or replace a resource | Yes | No  | No  |
| PATCH | Partially updates a resource | No  | No  | Yes if response contains freshness info |
| DELETE | Deletes a resource | Yes | No  | No  |

*Can be called many times without different outcomes.

HTTP is an application layer protocol relying on lower-level protocols such as **TCP** and **UDP**.

- [HTTP](https://www.nginx.com/resources/glossary/http/)
- [README](https://www.quora.com/What-is-the-difference-between-HTTP-protocol-and-TCP-protocol)

### [(L)](https://github.com/donnemartin/system-design-primer#transmission-control-protocol-tcp)Transmission control protocol (TCP)

 [![687474703a2f2f692e696d6775722e636f6d2f4a6441736476472e6a7067.jpg](../_resources/8916d8c034ec6e4cfd44d54ea29c3708.jpg)](https://camo.githubusercontent.com/821620cf6aa83566f4def561e754e5991480ca8d/687474703a2f2f692e696d6775722e636f6d2f4a6441736476472e6a7067)

 *[Source: How to make a multiplayer game](http://www.wildbunny.co.uk/blog/2012/10/09/how-to-make-a-multi-player-game-part-1/)*

TCP is a connection-oriented protocol over an [IP network](https://en.wikipedia.org/wiki/Internet_Protocol). Connection is established and terminated using a [handshake](https://en.wikipedia.org/wiki/Handshaking). All packets sent are guaranteed to reach the destination in the original order and without corruption through:

- Sequence numbers and [checksum fields](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Checksum_computation) for each packet
- [Acknowledgement](https://en.wikipedia.org/wiki/Acknowledgement_(data_networks)) packets and automatic retransmission

If the sender does not receive a correct response, it will resend the packets. If there are multiple timeouts, the connection is dropped. TCP also implements [flow control](https://en.wikipedia.org/wiki/Flow_control_(data)) and [congestion control](https://en.wikipedia.org/wiki/Network_congestion#Congestion_control). These guarantees cause delays and generally results in less efficient transmission than UDP.

To ensure high throughput, web servers can keep a large number of TCP connections open, resulting in high memory usage. It can be expensive to have a large number of open connections between web server threads and say, a [memcached](https://github.com/donnemartin/system-design-primer#memcached) server. [Connection pooling](https://en.wikipedia.org/wiki/Connection_pool) can help in addition to switching to UDP where applicable.

TCP is useful for applications that require high reliability but are less time critical. Some examples include web servers, database info, SMTP, FTP, and SSH.

Use TCP over UDP when:

- You need all of the data to arrive intact
- You want to automatically make a best estimate use of the network throughput

### [(L)](https://github.com/donnemartin/system-design-primer#user-datagram-protocol-udp)User datagram protocol (UDP)

 [![687474703a2f2f692e696d6775722e636f6d2f797a44724a74412e6a7067.jpg](../_resources/b832b76b9344d4957f980bc74f3888ea.jpg)](https://camo.githubusercontent.com/47eb14c0a2dff2166f8781a6ce8c7f33d4c33da8/687474703a2f2f692e696d6775722e636f6d2f797a44724a74412e6a7067)

 *[Source: How to make a multiplayer game](http://www.wildbunny.co.uk/blog/2012/10/09/how-to-make-a-multi-player-game-part-1/)*

UDP is connectionless. Datagrams (analogous to packets) are guaranteed only at the datagram level. Datagrams might reach their destination out of order or not at all. UDP does not support congestion control. Without the guarantees that TCP support, UDP is generally more efficient.

UDP can broadcast, sending datagrams to all devices on the subnet. This is useful with [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) because the client has not yet received an IP address, thus preventing a way for TCP to stream without the IP address.

UDP is less reliable but works well in real time use cases such as VoIP, video chat, streaming, and realtime multiplayer games.

Use UDP over TCP when:

- You need the lowest latency
- Late data is worse than loss of data
- You want to implement your own error correction

#### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-tcp-and-udp)Source(s) and further reading: TCP and UDP

- [Networking for game programming](http://gafferongames.com/networking-for-game-programmers/udp-vs-tcp/)
- [Key differences between TCP and UDP protocols](http://www.cyberciti.biz/faq/key-differences-between-tcp-and-udp-protocols/)
- [Difference between TCP and UDP](http://stackoverflow.com/questions/5970383/difference-between-tcp-and-udp)
- [Transmission control protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [User datagram protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [Scaling memcache at Facebook](http://www.cs.bu.edu/~jappavoo/jappavoo.github.com/451/papers/memcache-fb.pdf)

### [(L)](https://github.com/donnemartin/system-design-primer#remote-procedure-call-rpc)Remote procedure call (RPC)

 [![687474703a2f2f692e696d6775722e636f6d2f6946344d6b62352e706e67.png](../_resources/5e898a05b56aae238ad4d2b308afac49.png)](https://camo.githubusercontent.com/1a3d7771c0b0a7816d0533fffeb6eeeb442d9945/687474703a2f2f692e696d6775722e636f6d2f6946344d6b62352e706e67)

 *[Source: Crack the system design interview](http://www.puncsky.com/blog/2016/02/14/crack-the-system-design-interview/)*

In an RPC, a client causes a procedure to execute on a different address space, usually a remote server. The procedure is coded as if it were a local procedure call, abstracting away the details of how to communicate with the server from the client program. Remote calls are usually slower and less reliable than local calls so it is helpful to distinguish RPC calls from local calls. Popular RPC frameworks include [Protobuf](https://developers.google.com/protocol-buffers/), [Thrift](https://thrift.apache.org/), and [Avro](https://avro.apache.org/docs/current/).

RPC is a request-response protocol:

- **Client program** - Calls the client stub procedure. The parameters are pushed onto the stack like a local procedure call.
- **Client stub procedure** - Marshals (packs) procedure id and arguments into a request message.
- **Client communication module** - OS sends the message from the client to the server.
- **Server communication module** - OS passes the incoming packets to the server stub procedure.
- **Server stub procedure** - Unmarshalls the results, calls the server procedure matching the procedure id and passes the given arguments.
- The server response repeats the steps above in reverse order.

Sample RPC calls:

	normalGET /someoperation?data=anId

	POST /anotheroperation
	{
	  "data":"anId";
	  "anotherdata": "another value"
	}
	normal

RPC is focused on exposing behaviors. RPCs are often used for performance reasons with internal communications, as you can hand-craft native calls to better fit your use cases.

Choose a Native Library aka SDK when:

- You know your target platform.
- You want to control how your "logic" is accessed
- You want to control how error control happens off your library
- Performance and end user experience is your primary concern

HTTP APIs following **REST** tend to be used more often for public APIs.

#### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-rpc)Disadvantage(s): RPC

- RPC clients become tightly coupled to the service implementation.
- A new API must be defined for every new operation or use case.
- It can be difficult to debug RPC.
- You might not be able to leverage existing technologies out of the box. For example, it might require additional effort to ensure [RPC calls are properly cached](http://etherealbits.com/2012/12/debunking-the-myths-of-rpc-rest/) on caching servers such as [Squid](http://www.squid-cache.org/).

### [(L)](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest)Representational state transfer (REST)

REST is an architectural style enforcing a client/server model where the client acts on a set of resources managed by the server. The server provides a representation of resources and actions that can either manipulate or get a new representation of resources. All communication must be stateless and cacheable.

There are four qualities of a RESTful interface:

- **Identify resources (URI in HTTP)** - use the same URI regardless of any operation.
- **Change with representations (Verbs in HTTP)** - use verbs, headers, and body.
- **Self-descriptive error message (status response in HTTP)** - Use status codes, don't reinvent the wheel.
- **[HATEOAS](http://restcookbook.com/Basics/hateoas/) (HTML interface for HTTP)** - your web service should be fully accessible in a browser.

Sample REST calls:

	normalGET /someresources/anId

	PUT /someresources/anId
	{"anotherdata": "another value"}
	normal

REST is focused on exposing data. It minimizes the coupling between client/server and is often used for public HTTP APIs. REST uses a more generic and uniform method of exposing resources through URIs, [representation through headers](https://github.com/for-GET/know-your-http-well/blob/master/headers.md), and actions through verbs such as GET, POST, PUT, DELETE, and PATCH. Being stateless, REST is great for horizontal scaling and partitioning.

#### [(L)](https://github.com/donnemartin/system-design-primer#disadvantages-rest)Disadvantage(s): REST

- With REST being focused on exposing data, it might not be a good fit if resources are not naturally organized or accessed in a simple hierarchy. For example, returning all updated records from the past hour matching a particular set of events is not easily expressed as a path. With REST, it is likely to be implemented with a combination of URI path, query parameters, and possibly the request body.
- REST typically relies on a few verbs (GET, POST, PUT, DELETE, and PATCH) which sometimes doesn't fit your use case. For example, moving expired documents to the archive folder might not cleanly fit within these verbs.
- Fetching complicated resources with nested hierarchies requires multiple round trips between the client and server to render single views, e.g. fetching content of a blog entry and the comments on that entry. For mobile applications operating in variable network conditions, these multiple roundtrips are highly undesirable.
- Over time, more fields might be added to an API response and older clients will receive all new data fields, even those that they do not need, as a result, it bloats the payload size and leads to larger latencies.

### [(L)](https://github.com/donnemartin/system-design-primer#rpc-and-rest-calls-comparison)RPC and REST calls comparison

| Operation | RPC | REST |
| --- | --- | --- |
| Signup | **POST** /signup | **POST** /persons |
| Resign | **POST** /resign<br>{<br>"personid": "1234"<br>} | **DELETE** /persons/1234 |
| Read a person | **GET** /readPerson?personid=1234 | **GET** /persons/1234 |
| Read a person’s items list | **GET** /readUsersItemsList?personid=1234 | **GET** /persons/1234/items |
| Add an item to a person’s items | **POST** /addItemToUsersItemsList<br>{<br>"personid": "1234";<br>"itemid": "456"<br>} | **POST** /persons/1234/items<br>{<br>"itemid": "456"<br>} |
| Update an item | **POST** /modifyItem<br>{<br>"itemid": "456";<br>"key": "value"<br>} | **PUT** /items/456<br>{<br>"key": "value"<br>} |
| Delete an item | **POST** /removeItem<br>{<br>"itemid": "456"<br>} | **DELETE** /items/456 |

 *[Source: Do you really know why you prefer REST over RPC](https://apihandyman.io/do-you-really-know-why-you-prefer-rest-over-rpc/)*

#### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-rest-and-rpc)Source(s) and further reading: REST and RPC

- [Do you really know why you prefer REST over RPC](https://apihandyman.io/do-you-really-know-why-you-prefer-rest-over-rpc/)
- [When are RPC-ish approaches more appropriate than REST?](http://programmers.stackexchange.com/a/181186)
- [REST vs JSON-RPC](http://stackoverflow.com/questions/15056878/rest-vs-json-rpc)
- [Debunking the myths of RPC and REST](http://etherealbits.com/2012/12/debunking-the-myths-of-rpc-rest/)
- [What are the drawbacks of using REST](https://www.quora.com/What-are-the-drawbacks-of-using-RESTful-APIs)
- [Crack the system design interview](http://www.puncsky.com/blog/2016/02/14/crack-the-system-design-interview/)
- [Thrift](https://code.facebook.com/posts/1468950976659943/)
- [Why REST for internal use and not RPC](http://arstechnica.com/civis/viewtopic.php?t=1190508)

## [(L)](https://github.com/donnemartin/system-design-primer#security)Security

This section could use some updates. Consider [contributing](https://github.com/donnemartin/system-design-primer#contributing)!

Security is a broad topic. Unless you have considerable experience, a security background, or are applying for a position that requires knowledge of security, you probably won't need to know more than the basics:

- Encrypt in transit and at rest.
- Sanitize all user inputs or any input parameters exposed to user to prevent [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting) and [SQL injection](https://en.wikipedia.org/wiki/SQL_injection).
- Use parameterized queries to prevent SQL injection.
- Use the principle of [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).

### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-12)Source(s) and further reading

- [Security guide for developers](https://github.com/FallibleInc/security-guide-for-developers)
- [OWASP top ten](https://www.owasp.org/index.php/OWASP_Top_Ten_Cheat_Sheet)

## [(L)](https://github.com/donnemartin/system-design-primer#appendix)Appendix

You'll sometimes be asked to do 'back-of-the-envelope' estimates. For example, you might need to determine how long it will take to generate 100 image thumbnails from disk or how much memory a data structure will take. The **Powers of two table** and **Latency numbers every programmer should know** are handy references.

### [(L)](https://github.com/donnemartin/system-design-primer#powers-of-two-table)Powers of two table

	normalPower           Exact Value         Approx Value        Bytes
	---------------------------------------------------------------
	7                             128
	8                             256
	10                           1024   1 thousand           1 KB
	16                         65,536                       64 KB
	20                      1,048,576   1 million            1 MB
	30                  1,073,741,824   1 billion            1 GB
	32                  4,294,967,296                        4 GB
	40              1,099,511,627,776   1 trillion           1 TB
	normal

#### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-13)Source(s) and further reading

- [Powers of two](https://en.wikipedia.org/wiki/Power_of_two)

### [(L)](https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know)Latency numbers every programmer should know

	normalLatency Comparison Numbers
	--------------------------
	L1 cache reference                           0.5 ns
	Branch mispredict                            5   ns
	L2 cache reference                           7   ns                      14x L1 cache
	Mutex lock/unlock                          100   ns
	Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
	Compress 1K bytes with Zippy            10,000   ns       10 us
	Send 1 KB bytes over 1 Gbps network     10,000   ns       10 us
	Read 4 KB randomly from SSD*           150,000   ns      150 us          ~1GB/sec SSD
	Read 1 MB sequentially from memory     250,000   ns      250 us
	Round trip within same datacenter      500,000   ns      500 us
	Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
	Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
	Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
	Read 1 MB sequentially from disk    30,000,000   ns   30,000 us   30 ms 120x memory, 30X SSD
	Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

	Notes
	-----
	1 ns = 10^-9 seconds
	1 us = 10^-6 seconds = 1,000 ns
	1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns
	normal

Handy metrics based on numbers above:

- Read sequentially from disk at 30 MB/s
- Read sequentially from 1 Gbps Ethernet at 100 MB/s
- Read sequentially from SSD at 1 GB/s
- Read sequentially from main memory at 4 GB/s
- 6-7 world-wide round trips per second
- 2,000 round trips per second within a data center

#### [(L)](https://github.com/donnemartin/system-design-primer#latency-numbers-visualized)Latency numbers visualized

[![687474703a2f2f692e696d6775722e636f6d2f6b307431652e706e67.png](../_resources/53f2718fba6c8ea3aa4022cd50b8c0de.png)](https://camo.githubusercontent.com/77f72259e1eb58596b564d1ad823af1853bc60a3/687474703a2f2f692e696d6775722e636f6d2f6b307431652e706e67)

#### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-14)Source(s) and further reading

- [Latency numbers every programmer should know - 1](https://gist.github.com/jboner/2841832)
- [Latency numbers every programmer should know - 2](https://gist.github.com/hellerbarde/2843375)
- [Designs, lessons, and advice from building large distributed systems](http://www.cs.cornell.edu/projects/ladis2009/talks/dean-keynote-ladis2009.pdf)
- [Software Engineering Advice from Building Large-Scale Distributed Systems](https://static.googleusercontent.com/media/research.google.com/en//people/jeff/stanford-295-talk.pdf)

### [(L)](https://github.com/donnemartin/system-design-primer#additional-system-design-interview-questions)Additional system design interview questions

> Common system design interview questions, with links to resources on how to solve each.

| Question | Reference(s) |
| --- | --- |
| Design a file sync service like Dropbox | [youtube.com](https://www.youtube.com/watch?v=PE4gwstWhmc) |
| Design a search engine like Google | [queue.acm.org](http://queue.acm.org/detail.cfm?id=988407)<br>[stackexchange.com](http://programmers.stackexchange.com/questions/38324/interview-question-how-would-you-implement-google-search)<br>[ardendertat.com](http://www.ardendertat.com/2012/01/11/implementing-search-engines/)<br>[stanford.edu](http://infolab.stanford.edu/~backrub/google.html) |
| Design a scalable web crawler like Google | [quora.com](https://www.quora.com/How-can-I-build-a-web-crawler-from-scratch) |
| Design Google docs | [code.google.com](https://code.google.com/p/google-mobwrite/)<br>[neil.fraser.name](https://neil.fraser.name/writing/sync/) |
| Design a key-value store like Redis | [slideshare.net](http://www.slideshare.net/dvirsky/introduction-to-redis) |
| Design a cache system like Memcached | [slideshare.net](http://www.slideshare.net/oemebamo/introduction-to-memcached) |
| Design a recommendation system like Amazon's | [hulu.com](http://tech.hulu.com/blog/2011/09/19/recommendation-system.html)<br>[ijcai13.org](http://ijcai13.org/files/tutorial_slides/td3.pdf) |
| Design a tinyurl system like Bitly | [n00tc0d3r.blogspot.com](http://n00tc0d3r.blogspot.com/) |
| Design a chat app like WhatsApp | [highscalability.com](http://highscalability.com/blog/2014/2/26/the-whatsapp-architecture-facebook-bought-for-19-billion.html) |
| Design a picture sharing system like Instagram | [highscalability.com](http://highscalability.com/flickr-architecture)<br>[highscalability.com](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html) |
| Design the Facebook news feed function | [quora.com](http://www.quora.com/What-are-best-practices-for-building-something-like-a-News-Feed)<br>[quora.com](http://www.quora.com/Activity-Streams/What-are-the-scaling-issues-to-keep-in-mind-while-developing-a-social-network-feed)<br>[slideshare.net](http://www.slideshare.net/danmckinley/etsy-activity-feeds-architecture) |
| Design the Facebook timeline function | [facebook.com](https://www.facebook.com/note.php?note_id=10150468255628920)<br>[highscalability.com](http://highscalability.com/blog/2012/1/23/facebook-timeline-brought-to-you-by-the-power-of-denormaliza.html) |
| Design the Facebook chat function | [erlang-factory.com](http://www.erlang-factory.com/upload/presentations/31/EugeneLetuchy-ErlangatFacebook.pdf)<br>[facebook.com](https://www.facebook.com/note.php?note_id=14218138919&id=9445547199&index=0) |
| Design a graph search function like Facebook's | [facebook.com](https://www.facebook.com/notes/facebook-engineering/under-the-hood-building-out-the-infrastructure-for-graph-search/10151347573598920)<br>[facebook.com](https://www.facebook.com/notes/facebook-engineering/under-the-hood-indexing-and-ranking-in-graph-search/10151361720763920)<br>[facebook.com](https://www.facebook.com/notes/facebook-engineering/under-the-hood-the-natural-language-interface-of-graph-search/10151432733048920) |
| Design a content delivery network like CloudFlare | [cmu.edu](http://repository.cmu.edu/cgi/viewcontent.cgi?article=2112&context=compsci) |
| Design a trending topic system like Twitter's | [michael-noll.com](http://www.michael-noll.com/blog/2013/01/18/implementing-real-time-trending-topics-in-storm/)<br>[snikolov .wordpress.com](http://snikolov.wordpress.com/2012/11/14/early-detection-of-twitter-trends/) |
| Design a random ID generation system | [blog.twitter.com](https://blog.twitter.com/2010/announcing-snowflake)<br>[github.com](https://github.com/twitter/snowflake/) |
| Return the top k requests during a time interval | [ucsb.edu](https://icmi.cs.ucsb.edu/research/tech_reports/reports/2005-23.pdf)<br>[wpi.edu](http://davis.wpi.edu/xmdv/docs/EDBT11-diyang.pdf) |
| Design a system that serves data from multiple data centers | [highscalability.com](http://highscalability.com/blog/2009/8/24/how-google-serves-data-from-multiple-datacenters.html) |
| Design an online multiplayer card game | [indieflashblog.com](http://www.indieflashblog.com/how-to-create-an-asynchronous-multiplayer-game.html)<br>[buildnewgames.com](http://buildnewgames.com/real-time-multiplayer/) |
| Design a garbage collection system | [stuffwithstuff.com](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/)<br>[washington.edu](http://courses.cs.washington.edu/courses/csep521/07wi/prj/rick.pdf) |
| Add a system design question | [Contribute](https://github.com/donnemartin/system-design-primer#contributing) |

### [(L)](https://github.com/donnemartin/system-design-primer#real-world-architectures)Real world architectures

> Articles on how real world systems are designed.

 [![687474703a2f2f692e696d6775722e636f6d2f5463556f3266772e706e67.png](../_resources/cfa8960bc8e53fbd412042f566081390.png)](https://camo.githubusercontent.com/b7c71be73fb466344c2d773178ae74e3fbb1dcc6/687474703a2f2f692e696d6775722e636f6d2f5463556f3266772e706e67)

 *[Source: Twitter timelines at scale](https://www.infoq.com/presentations/Twitter-Timeline-Scalability)*

**Don't focus on nitty gritty details for the following articles, instead:**

- Identify shared principles, common technologies, and patterns within these articles
- Study what problems are solved by each component, where it works, where it doesn't
- Review the lessons learned

| Type | System | Reference(s) |
| --- | --- | --- |
| Data processing | **MapReduce** - Distributed data processing from Google | [research.google.com](http://static.googleusercontent.com/media/research.google.com/zh-CN/us/archive/mapreduce-osdi04.pdf) |
| Data processing | **Spark** - Distributed data processing from Databricks | [slideshare.net](http://www.slideshare.net/AGrishchenko/apache-spark-architecture) |
| Data processing | **Storm** - Distributed data processing from Twitter | [slideshare.net](http://www.slideshare.net/previa/storm-16094009) |
|     |     |     |
| Data store | **Bigtable** - Distributed column-oriented database from Google | [harvard.edu](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/chang06bigtable.pdf) |
| Data store | **HBase** - Open source implementation of Bigtable | [slideshare.net](http://www.slideshare.net/alexbaranau/intro-to-hbase) |
| Data store | **Cassandra** - Distributed column-oriented database from Facebook | [slideshare.net](http://www.slideshare.net/planetcassandra/cassandra-introduction-features-30103666) |
| Data store | **DynamoDB** - Document-oriented database from Amazon | [harvard.edu](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/decandia07dynamo.pdf) |
| Data store | **MongoDB** - Document-oriented database | [slideshare.net](http://www.slideshare.net/mdirolf/introduction-to-mongodb) |
| Data store | **Spanner** - Globally-distributed database from Google | [research.google.com](http://research.google.com/archive/spanner-osdi2012.pdf) |
| Data store | **Memcached** - Distributed memory caching system | [slideshare.net](http://www.slideshare.net/oemebamo/introduction-to-memcached) |
| Data store | **Redis** - Distributed memory caching system with persistence and value types | [slideshare.net](http://www.slideshare.net/dvirsky/introduction-to-redis) |
|     |     |     |
| File system | **Google File System (GFS)** - Distributed file system | [research.google.com](http://static.googleusercontent.com/media/research.google.com/zh-CN/us/archive/gfs-sosp2003.pdf) |
| File system | **Hadoop File System (HDFS)** - Open source implementation of GFS | [apache.org](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) |
|     |     |     |
| Misc | **Chubby** - Lock service for loosely-coupled distributed systems from Google | [research.google.com](http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en/us/archive/chubby-osdi06.pdf) |
| Misc | **Dapper** - Distributed systems tracing infrastructure | [research.google.com](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36356.pdf) |
| Misc | **Kafka** - Pub/sub message queue from LinkedIn | [slideshare.net](http://www.slideshare.net/mumrah/kafka-talk-tri-hug) |
| Misc | **Zookeeper** - Centralized infrastructure and services enabling synchronization | [slideshare.net](http://www.slideshare.net/sauravhaloi/introduction-to-apache-zookeeper) |
|     | Add an architecture | [Contribute](https://github.com/donnemartin/system-design-primer#contributing) |

### [(L)](https://github.com/donnemartin/system-design-primer#company-architectures)Company architectures

| Company | Reference(s) |
| --- | --- |
| Amazon | [Amazon architecture](http://highscalability.com/amazon-architecture) |
| Cinchcast | [Producing 1,500 hours of audio every day](http://highscalability.com/blog/2012/7/16/cinchcast-architecture-producing-1500-hours-of-audio-every-d.html) |
| DataSift | [Realtime datamining At 120,000 tweets per second](http://highscalability.com/blog/2011/11/29/datasift-architecture-realtime-datamining-at-120000-tweets-p.html) |
| DropBox | [How we've scaled Dropbox](https://www.youtube.com/watch?v=PE4gwstWhmc) |
| ESPN | [Operating At 100,000 duh nuh nuhs per second](http://highscalability.com/blog/2013/11/4/espns-architecture-at-scale-operating-at-100000-duh-nuh-nuhs.html) |
| Google | [Google architecture](http://highscalability.com/google-architecture) |
| Instagram | [14 million users, terabytes of photos](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html)<br>[What powers Instagram](http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances) |
| Justin.tv | [Justin.Tv's live video broadcasting architecture](http://highscalability.com/blog/2010/3/16/justintvs-live-video-broadcasting-architecture.html) |
| Facebook | [Scaling memcached at Facebook](https://cs.uwaterloo.ca/~brecht/courses/854-Emerging-2014/readings/key-value/fb-memcached-nsdi-2013.pdf)<br>[TAO: Facebook’s distributed data store for the social graph](https://cs.uwaterloo.ca/~brecht/courses/854-Emerging-2014/readings/data-store/tao-facebook-distributed-datastore-atc-2013.pdf)<br>[Facebook’s photo storage](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf) |
| Flickr | [Flickr architecture](http://highscalability.com/flickr-architecture) |
| Mailbox | [From 0 to one million users in 6 weeks](http://highscalability.com/blog/2013/6/18/scaling-mailbox-from-0-to-one-million-users-in-6-weeks-and-1.html) |
| Pinterest | [From 0 To 10s of billions of page views a month](http://highscalability.com/blog/2013/4/15/scaling-pinterest-from-0-to-10s-of-billions-of-page-views-a.html)<br>[18 million visitors, 10x growth, 12 employees](http://highscalability.com/blog/2012/5/21/pinterest-architecture-update-18-million-visitors-10x-growth.html) |
| Playfish | [50 million monthly users and growing](http://highscalability.com/blog/2010/9/21/playfishs-social-gaming-architecture-50-million-monthly-user.html) |
| PlentyOfFish | [PlentyOfFish architecture](http://highscalability.com/plentyoffish-architecture) |
| Salesforce | [How they handle 1.3 billion transactions a day](http://highscalability.com/blog/2013/9/23/salesforce-architecture-how-they-handle-13-billion-transacti.html) |
| Stack Overflow | [Stack Overflow architecture](http://highscalability.com/blog/2009/8/5/stack-overflow-architecture.html) |
| TripAdvisor | [40M visitors, 200M dynamic page views, 30TB data](http://highscalability.com/blog/2011/6/27/tripadvisor-architecture-40m-visitors-200m-dynamic-page-view.html) |
| Tumblr | [15 billion page views a month](http://highscalability.com/blog/2012/2/13/tumblr-architecture-15-billion-page-views-a-month-and-harder.html) |
| Twitter | [Making Twitter 10000 percent faster](http://highscalability.com/scaling-twitter-making-twitter-10000-percent-faster)<br>[Storing 250 million tweets a day using MySQL](http://highscalability.com/blog/2011/12/19/how-twitter-stores-250-million-tweets-a-day-using-mysql.html)<br>[150M active users, 300K QPS, a 22 MB/S firehose](http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html)<br>[Timelines at scale](https://www.infoq.com/presentations/Twitter-Timeline-Scalability)<br>[Big and small data at Twitter](https://www.youtube.com/watch?v=5cKTP36HVgI)<br>[Operations at Twitter: scaling beyond 100 million users](https://www.youtube.com/watch?v=z8LU0Cj6BOU) |
| Uber | [How Uber scales their real-time market platform](http://highscalability.com/blog/2015/9/14/how-uber-scales-their-real-time-market-platform.html) |
| WhatsApp | [The WhatsApp architecture Facebook bought for $19 billion](http://highscalability.com/blog/2014/2/26/the-whatsapp-architecture-facebook-bought-for-19-billion.html) |
| YouTube | [YouTube scalability](https://www.youtube.com/watch?v=w5WVu624fY8)<br>[YouTube architecture](http://highscalability.com/youtube-architecture) |

### [(L)](https://github.com/donnemartin/system-design-primer#company-engineering-blogs)Company engineering blogs

> Architectures for companies you are interviewing with.
> Questions you encounter might be from the same domain.

- [Airbnb Engineering](http://nerds.airbnb.com/)
- [Atlassian Developers](https://developer.atlassian.com/blog/)
- [Autodesk Engineering](http://cloudengineering.autodesk.com/blog/)
- [AWS Blog](https://aws.amazon.com/blogs/aws/)
- [Bitly Engineering Blog](http://word.bitly.com/)
- [Box Blogs](https://www.box.com/blog/engineering/)
- [Cloudera Developer Blog](http://blog.cloudera.com/blog/)
- [Dropbox Tech Blog](https://tech.dropbox.com/)
- [Engineering at Quora](http://engineering.quora.com/)
- [Ebay Tech Blog](http://www.ebaytechblog.com/)
- [Evernote Tech Blog](https://blog.evernote.com/tech/)
- [Etsy Code as Craft](http://codeascraft.com/)
- [Facebook Engineering](https://www.facebook.com/Engineering)
- [Flickr Code](http://code.flickr.net/)
- [Foursquare Engineering Blog](http://engineering.foursquare.com/)
- [GitHub Engineering Blog](http://githubengineering.com/)
- [Google Research Blog](http://googleresearch.blogspot.com/)
- [Groupon Engineering Blog](https://engineering.groupon.com/)
- [Heroku Engineering Blog](https://engineering.heroku.com/)
- [Hubspot Engineering Blog](http://product.hubspot.com/blog/topic/engineering)
- [High Scalability](http://highscalability.com/)
- [Instagram Engineering](http://instagram-engineering.tumblr.com/)
- [Intel Software Blog](https://software.intel.com/en-us/blogs/)
- [Jane Street Tech Blog](https://blogs.janestreet.com/category/ocaml/)
- [LinkedIn Engineering](http://engineering.linkedin.com/blog)
- [Microsoft Engineering](https://engineering.microsoft.com/)
- [Microsoft Python Engineering](https://blogs.msdn.microsoft.com/pythonengineering/)
- [Netflix Tech Blog](http://techblog.netflix.com/)
- [Paypal Developer Blog](https://devblog.paypal.com/category/engineering/)
- [Pinterest Engineering Blog](http://engineering.pinterest.com/)
- [Quora Engineering](https://engineering.quora.com/)
- [Reddit Blog](http://www.redditblog.com/)
- [Salesforce Engineering Blog](https://developer.salesforce.com/blogs/engineering/)
- [Slack Engineering Blog](https://slack.engineering/)
- [Spotify Labs](https://labs.spotify.com/)
- [Twilio Engineering Blog](http://www.twilio.com/engineering)
- [Twitter Engineering](https://engineering.twitter.com/)
- [Uber Engineering Blog](http://eng.uber.com/)
- [Yahoo Engineering Blog](http://yahooeng.tumblr.com/)
- [Yelp Engineering Blog](http://engineeringblog.yelp.com/)
- [Zynga Engineering Blog](https://www.zynga.com/blogs/engineering)

#### [(L)](https://github.com/donnemartin/system-design-primer#sources-and-further-reading-15)Source(s) and further reading

- [kilimchoi/engineering-blogs](https://github.com/kilimchoi/engineering-blogs)

## [(L)](https://github.com/donnemartin/system-design-primer#under-development)Under development

Interested in adding a section or helping complete one in-progress? [Contribute](https://github.com/donnemartin/system-design-primer#contributing)!

- Distributed computing with MapReduce
- Consistent hashing
- Scatter gather
- [Contribute](https://github.com/donnemartin/system-design-primer#contributing)

## [(L)](https://github.com/donnemartin/system-design-primer#credits)Credits

Credits and sources are provided throughout this repo.
Special thanks to:

- [Hired in tech](http://www.hiredintech.com/system-design/the-system-design-process/)
- [Cracking the coding interview](https://www.amazon.com/dp/0984782850/)
- [High scalability](http://highscalability.com/)
- [checkcheckzz/system-design-interview](https://github.com/checkcheckzz/system-design-interview)
- [shashank88/system_design](https://github.com/shashank88/system_design)
- [mmcgrana/services-engineering](https://github.com/mmcgrana/services-engineering)
- [System design cheat sheet](https://gist.github.com/vasanthk/485d1c25737e8e72759f)
- [A distributed systems reading list](http://dancres.github.io/Pages/)
- [Cracking the system design interview](http://www.puncsky.com/blog/2016/02/14/crack-the-system-design-interview/)

## [(L)](https://github.com/donnemartin/system-design-primer#contact-info)Contact info

Feel free to contact me to discuss any issues, questions, or comments.

My contact info can be found on my [GitHub page](https://github.com/donnemartin).

## [(L)](https://github.com/donnemartin/system-design-primer#license)License

	normalCreative Commons Attribution 4.0 International License (CC BY 4.0)

	http://creativecommons.org/licenses/by/4.0/
	normal