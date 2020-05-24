Microservices at Netflix: Lessons for Architectural Design

[Blog](https://www.nginx.com/blog/)
[Tech](https://www.nginx.com/category/tech/)
[Tony Mauro](https://www.nginx.com/blog/author/tony/)
·
February 19, 2015

# Adopting Microservices at Netflix: Lessons for Architectural Design

![icon-tag.png](../_resources/d6379731bcdcb79a73d8624e46e0b7e0.png)

[microservices](https://www.nginx.com/blog/tag/microservices/), [containers](https://www.nginx.com/blog/tag/containers/), [Netflix](https://www.nginx.com/blog/tag/netflix/), [content delivery network (CDN)](https://www.nginx.com/blog/tag/content-delivery-network-cdn/)

- [    twitter](https://twitter.com/intent/tweet?text=Adopting+Microservices+at+Netflix%3A+Lessons+for+Architectural+Design+by+%40nginx+https%3A%2F%2Fwww.nginx.com%2Fblog%2Fmicroservices-at-netflix-architectural-best-practices%2F)

- [  linkedin](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.nginx.com%2Fblog%2Fmicroservices-at-netflix-architectural-best-practices%2F&title=Adopting+Microservices+at+Netflix%3A+Lessons+for+Architectural+Design&summary=In+some+recent+blog+posts%2C+we%E2%80%99ve+explained+why+we+believe+it%26%238217%3Bs+crucial+to+adopt+a+four-tier+application+architecture+in+which+applications+are+developed+and+deployed+as+sets+of+microservices.+It%26%238217%3Bs+becoming+increasingly+clear+that+if+you+keep+using+development+processes+and+application+architectures+that+worked+just+fine+ten+years+ago%2C+you+simply+can%26%238217%3Bt+move+fast+%5B%26hellip%3B%5D)

- [    hackernews](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fwww.nginx.com%2Fblog%2Fmicroservices-at-netflix-architectural-best-practices%2F&t=Adopting%20Microservices%20at%20Netflix:%20Lessons%20for%20Architectural%20Design&text=In%20some%20recent%20blog%20posts,%20we%E2%80%99ve%20explained%20why%20we%20believe%20it%E2%80%99s%20crucial%20to%20adopt%20a%20four-tier%20application%20architecture%20in%20which%20applications%20are%20developed%20and%20deployed%20as%20sets%20of%20microservices.%20It%E2%80%99s%20becoming%20increasingly%20clear%20that%20if%20you%20keep%20using%20development%20processes%20and%20application%20architectures%20that%20worked%20just%20fine%20ten%20years%20ago,%20you%20simply%20can%E2%80%99t%20move%20fast%20[%E2%80%A6])

- [  facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.nginx.com%2Fblog%2Fmicroservices-at-netflix-architectural-best-practices%2F)

- [ google+](https://plus.google.com/share?url=https%3A%2F%2Fwww.nginx.com%2Fblog%2Fmicroservices-at-netflix-architectural-best-practices%2F)

- [     reddit](http://www.reddit.com/submit?url=https%3A%2F%2Fwww.nginx.com%2Fblog%2Fmicroservices-at-netflix-architectural-best-practices%2F&title=Adopting+Microservices+at+Netflix%3A+Lessons+for+Architectural+Design&text=In+some+recent+blog+posts%2C+we%E2%80%99ve+explained+why+we+believe+it%26%238217%3Bs+crucial+to+adopt+a+four-tier+application+architecture+in+which+applications+are+developed+and+deployed+as+sets+of+microservices.+It%26%238217%3Bs+becoming+increasingly+clear+that+if+you+keep+using+development+processes+and+application+architectures+that+worked+just+fine+ten+years+ago%2C+you+simply+can%26%238217%3Bt+move+fast+%5B%26hellip%3B%5D)

In some recent blog posts, we’ve explained why we believe it’s crucial to adopt a [four-tier application architecture](https://www.nginx.com/blog/time-to-move-to-a-four-tier-application-architecture/?utm_source=microservices-at-netflix-architectural-best-practices&utm_medium=blog&utm_campaign=Microservices) in which applications are developed and deployed as sets of [microservices](https://www.nginx.com/blog/building-microservices-free-ebook-oreilly-nginx/?utm_source=microservices-at-netflix-architectural-best-practices&utm_medium=blog&utm_campaign=Microservices). It’s becoming increasingly clear that if you keep using development processes and application architectures that worked just fine ten years ago, you simply can’t move fast enough to capture and hold the interest of mobile users who can choose from an ever-growing number of apps.

Switching to a microservices architecture creates exciting opportunities in the marketplace for companies. For system architects and developers, it promises an unprecedented level of control and speed as they deliver innovative new web experiences to customers. But at such a breathless pace, it can feel like there’s not a lot of room for error. In the real world, you can’t stop developing and deploying your apps as you retool the processes for doing so. You know that your future success depends on transitioning to a microservices architecture, but how do you actually do it?

![Netflix_Logo_Digital+Video](../_resources/d86602a653f887d2f686ddc5f9ad5c64.png)Fortunately for us, several early adopters of microservices are now generously sharing their expertise in the spirit of open source, not only in the form of published code but in conference presentations and blog posts. [Netflix](http://netflix.com/) is a leading example. As the Director of Web Engineering and then Cloud Architect, Adrian Cockcroft oversaw the company’s transition from a traditional development model with 100 engineers producing a monolithic DVD-rental application to a microservices architecture with many small teams responsible for the end-to-end development of hundreds of microservices that work together to stream digital entertainment to millions of Netflix customers every day. Now a Technology Fellow at Battery Ventures, [Cockcroft](http://www.battery.com/our-team/member/adrian-cockcroft/) is a prominent evangelist for microservices and cloud‑native architectures, and serves on the NGINX Technical Advisory Board.

In a two-part series of blog posts, we’ll present top takeaways from two talks that Cockcroft delivered last year, at the first annual NGINX conference in October and at a Silicon Valley Microservices Meetup a couple months earlier. (The complete [video recordings](https://www.nginx.com/blog/microservices-at-netflix-architectural-best-practices/#videos) are also well worth watching.)

- This post defines microservices architecture and outlines some best practices for designing one.
- [Adopting Microservices at Netflix: Lessons for Team and Process Design](https://www.nginx.com/blog/adopting-microservices-at-netflix-lessons-for-team-and-process-design/?utm_source=microservices-at-netflix-architectural-best-practices&utm_medium=blog&utm_campaign=Microservices) discusses why and how to adopt a new mindset for software development and reorganize your teams around it.

## What is a Microservices Architecture?

Cockcroft defines a microservices architecture as a *service-oriented architecture composed of loosely coupled elements that have bounded contexts*.

*Loosely coupled* means that you can update the services independently; updating one service doesn’t require changing any other services. If you have a bunch of small, specialized services but still have to update them together, they’re not microservices because they’re not loosely coupled. One kind of coupling that people tend to overlook as they transition to a microservices architecture is database coupling, where all services talk to the same database and updating a service means changing the schema. You need to split the database up and denormalize it.

The concept of *bounded contexts* comes from the book *Domain Driven Design* by Eric Evans. A microservice with correctly bounded context is self-contained for the purposes of software development. You can understand and update the microservice’s code without knowing anything about the internals of its peers, because the microservices and its peers interact strictly through APIs and so don’t share data structures, database schemata, or other internal representations of objects.

If you’ve developed applications for the Internet, you’re already familiar with these concepts, in practice if not by name. Most mobile apps talk to quite a few backend services, to enable its users to do things like share on Facebook, get directions from Google Maps, and find restaurants on Foursquare, all within the context of the app. If your mobile app were tightly coupled with those services, then before you could release an update you would have to talk to all of their development teams to make sure that your changes aren’t going to break anything.

When working with a microservices architecture, you think of other internal development teams like those Internet backends: as external services that your microservice interacts with through APIs. The commonly understood “contract” between microservices is that their APIs are stable and forward compatible. Just as it’s unacceptable for the Google Maps API to change without warning and in such a way that it breaks its users, your API can evolve but must remain compatible with previous versions.

## Best Practices for Designing a Microservices Architecture

Cockcroft describes his role as Cloud Architect at Netflix not in terms of controlling the architecture, but as discovering and formalizing the architecture that emerged as the Netflix engineers built it. The Netflix development team established several best practices for designing and implementing a microservices architecture.

### Create a Separate Data Store for Each Microservice

Do not use the same backend data store across microservices. You want the team for each microservice to choose the database that best suits the service. Moreover, with a single data store it’s too easy for microservices written by different teams to share database structures, perhaps in the name of reducing duplication of work. You end up with the situation where if one team updates a database structure, other services that also use that structure have to be changed too.

Breaking apart the data can make data management more complicated, because the separate storage systems can more easily get out sync or become inconsistent, and foreign keys can change unexpectedly. You need to add a tool that performs [master data management](http://en.wikipedia.org/wiki/Master_data_management) (MDM) by operating in the background to find and fix inconsistencies. For example, it might examine every database that stores subscriber IDs, to verify that the same IDs exist in all of them (there aren’t missing or extra IDs in any one database). You can write your own tool or buy one. Many commercial relational database management systems (RDBMSs) do these kinds of checks, but they usually impose too many requirements for coupling, and so don’t scale.

### Keep Code at a Similar Level of Maturity

Keep all code in a microservice at a similar level of maturity and stability. In other words, if you need to add or rewrite some of the code in a deployed microservice that’s working well, the best approach is usually to create a new microservice for the new or changed code, leaving the existing microservice in place. [Editor’s note: This is sometimes referred to as the [immutable infrastructure](http://highops.com/insights/immutable-infrastructure-what-is-it/) principle.] This way you can iteratively deploy and test the new code until it is bug free and maximally efficient, without risking failure or performance degradation in the existing microservice. Once the new microservice is as stable as the original, you can merge them back together if they really perform a single function together, or if there are other efficiencies from combining them. However, in Cockcroft’s experience it is much more common to realize you should split up a microservice because it’s gotten too big.

### Do a Separate Build for Each Microservice

Do a separate build for each microservice, so that it can pull in component files from the repository at the revision levels appropriate to it. This sometimes leads to the situation where various microservices pull in a similar set of files, but at different revision levels. That can make it more difficult to clean up your codebase by decommissioning old file versions (because you have to verify more carefully that a revision is no longer being used), but that’s an acceptable trade-off for how easy it is to add new files as you build new microservices. The asymmetry is intentional: you want introducing a new microservice, file, or function to be easy, not dangerous.

### Deploy in Containers

Deploying microservices in containers is important because it means you just need just one tool to deploy everything. As long as the microservice is in a container, the tool knows how to deploy it. It doesn’t matter what the container is. That said, Docker seems very quickly to have become the de facto standard for containers.

### Treat Servers as Stateless

Treat servers, particularly those that run customer-facing code, as interchangeable members of a group. They all perform the same functions, so you don’t need to be concerned about them individually. Your only concern is that there are enough of them to produce the amount of work you need, and you can use autoscaling to adjust the numbers up and down. If one stops working, it’s automatically replaced by another one. Avoid “snowflake” systems in which you depend on individual servers to perform specialized functions.

Cockcroft’s analogy is that you want to think of servers like cattle, not pets. If you have a machine in production that performs a specialized function, and you know it by name, and everyone gets sad when it goes down, it’s a pet. Instead you should think of your servers like a herd of cows. What you care about is how many gallons of milk you get. If one day you notice you’re getting less milk than usual, you find out which cows aren’t producing well and replace them.

## Netflix Delivery Architecture is Built on NGINX

Netflix is a longtime user of the open source NGINX software and became the first customer of NGINX, Inc. after it incorporated in 2011. Indeed, [Netflix chose NGINX](https://www.nginx.com/press/nginx-inc-consulted-netflix-open-connect-initiative/?utm_source=microservices-at-netflix-architectural-best-practices&utm_medium=blog&utm_campaign=Microservices) as the heart of its delivery infrastructure, [Open Connect](https://openconnect.itp.netflix.com/software/index.html), one of the largest content delivery networks (CDNs) in the world. With the ability to serve thousands, and sometimes millions, of requests per second, NGINX and NGINX Plus are optimal solutions for high-performance HTTP delivery and enable companies like Netflix to offer high-quality digital experiences to millions of customers every day.

## Video Recordings

### Fast Delivery

nginx.conf2014, October 2014

[Fast Delivery: Adrian Cockcroft @nginxconf 2014](https://www.youtube.com/watch?v=5qJ_BibbMLw)

### Migrating to Microservices, Part 1

Silicon Valley Microservices Meetup, August 2014

[Migrating to Microservices by Adrian Cockroft (Part 1)](https://www.youtube.com/watch?v=1wiMLkXz26M)

### Migrating to Microservices, Part 2

Silicon Valley Microservices Meetup, August 2014

[Migrating to Microservices by Adrian Cockroft (Part 2)](https://www.youtube.com/watch?v=ebCtNmTVIJY)