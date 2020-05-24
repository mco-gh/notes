8 surprising facts about real Docker adoption

***Updated April 2017.** Earlier editions of this article were published in [October 2015](https://www.datadoghq.com/docker-adoption-2015/) and [June 2016](https://www.datadoghq.com/docker-adoption-2016/). *

#### With thousands of companies using Datadog to track their infrastructure, we can see software trends emerging in real time. Today we're excited to share our latest research into true Docker adoption—no hype, just the facts.

Docker is probably the most talked-about infrastructure technology of the past few years. We started this project to investigate how much Docker is used in production, and how fast real adoption is growing. We found the answers to these questions—and more that we discovered along the way—to be fascinating.

The research that follows was based on a sample of 10,000 companies, and 185 million containers in real-world use. As far as we know, this is the largest and most accurate review of Docker adoption that has ever been published.

Throughout this article we refer to companies' adoption status: "adopted", "dabbling", or "abandoned". Our method for determining adoption status is described in the [Methodology](https://www.datadoghq.com/docker-adoption/#methodology) section below.

ONE
![dd_dockerlisticle2017_b1_v2.png](../_resources/e0531645c4360d33152f580618f7ca5d.png)

## Real Docker Adoption Has

Increased 40% in One Year

At the beginning of March 2016, 13.6 percent of Datadog's customers had adopted Docker. One year later that number has grown to 18.8 percent. That's almost 40 percent market-share growth in 12 months.

[![docker-2017-1_v3.png](../_resources/a7232bf95e3f6aaa4d1a6aee2fe755cc.png)](https://datadog-prod.imgix.net/img/docker-2017-1_v3.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=New%20@datadoghq%20study%20of%20185%20million%20containers%3A%20%23Docker%20adoption%20is%20up%2040%25%20in%20one%20year%20dtdg.co/dckr-adopt%231%20https%3A//twitter.com/dd_docker/status/854175115227136000/photo/1&)

TWO
![dd_dockerlisticle2017_b2.png](../_resources/e221aaf54754edbeaa39d95e0e95df3a.png)

## Docker Now Runs on 15%

of the Hosts We Monitor

This is an impressive fact: Two years ago, Docker had about 3 percent market share, and now it's running on 15 percent of the hosts we monitor.

The graph below illustrates that the Docker growth rate was somewhat variable early on, but began to stabilize around the fall of 2015. Since that time, Docker usage has climbed steadily and nearly linearly, and it now runs on roughly one in six hosts that Datadog monitors.

[![docker-2017-2_v2.png](../_resources/f66a23e67fda5c55171614ee809053c7.png)](https://datadog-prod.imgix.net/img/docker-2017-2_v2.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=Docker%20now%20runs%20on%2015%25%20of%20the%20hosts%20@datadoghq%20monitors.%20More%20%23docker%20adoption%20stats%3A%20http%3A//dtdg.co/dckr-adopt%232%20https%3A//twitter.com/dd_docker/status/854175086437335040/photo/1&)

THREE
![dd_dockerlisticle2017_b3_v2.png](../_resources/a58903f9997faeea17315936d1a446f9.png)

## Larger Companies

Are Still Leading Adoption

The knock on larger companies is that they tend to be slower to move. But in the case of Docker, we've seen larger companies leading the way since the first edition of this report in 2015. The more hosts a company uses, the more likely it is to have tried Docker. Nearly 60 percent of organizations running 500 or more hosts are classified as Docker dabblers or adopters.

Whereas previous editions of this report showed organizations with large numbers of hosts clearly driving Docker adoption, the latest data shows that organizations with midsize host counts (100–499 hosts) have made significant gains. Adoption rates for companies with medium and large host counts are now nearly identical.

*Editorial conclusion: Docker first gained a foothold by solving the unique needs of large organizations, but is now finding use as a general-purpose platform at companies of all sizes.*

[![docker-2017-3_v3.png](../_resources/4cd41d2b5c36f7bccd24a0daba4e1ae1.png)](https://datadog-prod.imgix.net/img/docker-2017-3_v3.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=Larger%20companies%20are%20leading%20the%20%23docker%20trend%2C%20according%20to%20latest%20@datadoghq%20research%3A%20http%3A//dtdg.co/dckr-adopt%233%20https%3A//twitter.com/dd_docker/status/854175042988593152/photo/1&)

FOUR
![dd_dockerlisticle2017_b4.png](../_resources/669f6b41d3af560718786caee3e32e23.png)

## Orchestrators Are Taking Off

As Docker increasingly becomes an integral part of production environments, organizations are seeking out tools to help them effectively manage and orchestrate their containers. As of March 2017, roughly 40 percent of Datadog customers running Docker were also running [Kubernetes](https://www.datadoghq.com/blog/monitoring-kubernetes-era/), Mesos, [Amazon ECS](https://www.datadoghq.com/blog/3-clear-trends-in-ecs-adoption/), Google Container Engine, or another orchestrator. Additional organizations may be using Docker's built-in orchestration capabilities, but that functionality did not generate uniquely identifiable metrics that would allow us to reliably measure its use at the time of this report.

Among organizations running Docker and using AWS, Amazon ECS is a popular choice for orchestration, as would be expected: more than 35 percent of those companies use ECS. But we also see significant usage of other orchestrators (especially Kubernetes) at companies running AWS infrastructure.

[![docker-2017-4_v3.png](../_resources/d25fc962c70a2622d8bb7d90501fcccf.png)](https://datadog-prod.imgix.net/img/docker-2017-4_v3.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=New%20@datadoghq%20data%3A%2040%25%20of%20companies%20using%20%23docker%20now%20use%20one%20or%20more%20orchestration%20tools%20http%3A//dtdg.co/dckr-adopt%234%20https%3A//twitter.com/dd_docker/status/854175013808877568/photo/1&)

FIVE
![dd_dockerlisticle2017_b5_v2.png](../_resources/d0cf7c95b89232fded908923df7bd564.png)

## Adopters Quintuple Their

Container Count within 9 Months

Docker adopters nearly quintuple the average number of running containers they have in production between their first and tenth month of usage. This internal-usage growth rate is quite linear, and shows no signs of tapering off after the tenth month. In another indication of the robustness of this finding, this pattern of growth among adopters has remained steady since our previous report last year.

[![docker-2017-5.png](../_resources/7757fef4621c99c112e3d018dc10c627.png)](https://datadog-prod.imgix.net/img/docker-2017-5.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=New%20from%20@datadoghq%3A%20Companies%20that%20adopt%20%23docker%20increase%20container%20count%205x%20w/in%209%20months%3A%20http%3A//dtdg.co/dckr-adopt%235%20https%3A//twitter.com/dd_docker/status/854174980845817856/photo/1&)

SIX
![dd_dockerlisticle2017_b6.png](../_resources/207346bfcef8542ef1ca33bf0494b950.png)

## The Most Widely Used Images Are

NGINX, Redis, and Elasticsearch
The most common technologies running in Docker are:

1. **NGINX:** Docker is being used to contain a lot of HTTP servers, it seems. NGINX has been a perennial contender on this list since we began tracking image use in 2015.

2. **Redis:** This popular key-value data store is often used as an in-memory database, message queue, or cache.

3. **Elasticsearch:** Full-text search continues to increase in popularity, cracking the top 3 for the first time.

4. **Registry:** 18% of companies running Docker are using Registry, an application for storing and distributing other Docker images. Registry has been near the top of the list in each edition of this report.

5. **Postgres:** The increasingly popular open source relational database edges out MySQL for the first time in this ranking.

6. **MySQL:** The most widely used open source database in the world continues to find use in Docker infrastructure. Adding the MySQL and Postgres numbers, it appears that using Docker to run relational databases is surprisingly common.

7. **etcd:** The distributed key-value store is used to provide consistent configuration across a Docker cluster.

8. **Fluentd:** This open source "unified logging layer" is designed to decouple data sources from backend data stores. This is the first time Fluentd has appeared on the list, displacing Logspout from the top 10.

9. **MongoDB:** The widely-used NoSQL datastore.

10. **RabbitMQ:** The open source message broker finds plenty of use in Docker environments.

[![docker-2017-6_v2.png](../_resources/d637b841cd93fbbbf9722119db789665.png)](https://datadog-prod.imgix.net/img/docker-2017-6_v2.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=Latest%20@datadoghq%20%23Docker%20image%20leaderboard%3A%20NGINX%2C%20Redis%2C%20Elasticsearch...%20Full%20list%20here%3A%20http%3A//dtdg.co/dckr-adopt%236%20https%3A//twitter.com/dd_docker/status/854174946410606592/photo/1&)

SEVEN
![dd_dockerlisticle2017_b7_v3.png](../_resources/8965d285ccd5ccc4838e9d5fa4878490.png)

## Docker Hosts Often Run

Seven Containers at a Time

The median company that adopts Docker runs seven containers simultaneously on each host, up from five containers nine months ago. This finding seems to indicate that Docker is in fact commonly used as a lightweight way to share compute resources; it is not solely valued for providing a knowable, versioned runtime environment. Bolstering this observation, 25% of companies run an average of 14+ containers simultaneously.

[![docker-2017-7.png](../_resources/d04a77d58528f375af930e018c3686b9.png)](https://datadog-prod.imgix.net/img/docker-2017-7.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=Typical%20%23Docker%20host%20now%20runs%207%20containers%20at%20a%20time.%20Latest%20@datadoghq%20research%3A%20http%3A//dtdg.co/dckr-adopt%237%20https%3A//twitter.com/dd_docker/status/854174899690246144/photo/1&)

EIGHT
![dd_dockerlisticle2017_b8_v2.png](../_resources/f5a331060a7010cc5643732864444fa6.png)

## Containers Churn 9x

Faster Than VMs

At companies that adopt Docker, containers have an average lifespan of 2.5 days, while across all companies, traditional and cloud-based VMs have an average lifespan of 23 days.

Container orchestration ([see fact 4](https://www.datadoghq.com/docker-adoption/#4)) appears to have a strong effect on container lifetimes, as the automated starting and stopping of containers leads to a higher churn rate. In organizations running Docker with an orchestrator, the typical lifetime of a container is less than one day. At organizations that run Docker *without* orchestration, the average container exists for 5.5 days.

Containers' short lifetimes and increased density have [significant implications](https://www.datadoghq.com/blog/the-docker-monitoring-problem/) for infrastructure monitoring. They represent an order-of-magnitude increase in the number of things that need to be individually monitored. Monitoring solutions that are host-centric, rather than role-centric, quickly become unusable. We thus expect Docker to continue to drive the [sea change in monitoring practices](https://www.datadoghq.com/blog/2016-monitoring-at-scale/) that the cloud began several years ago.

[![docker-2017-8_v2.png](../_resources/0c01985c56b4bb3262ea6f177842a961.png)](https://datadog-prod.imgix.net/img/docker-2017-8_v2.png)

[*w* TWEET](https://twitter.com/intent/tweet?text=Containers%20churn%209x%20faster%20than%20VMs.%20More%20@datadoghq%20research%20into%20%23docker%20adoption%20and%20use%3A%20http%3A//dtdg.co/dckr-adopt%238%20https%3A//twitter.com/dd_docker/status/854174851862581252/photo/1&)

# METHODOLOGY

## Population

As noted in the introduction, we compiled usage data from a sample of 10,000 companies and 185 million containers, so this is almost certainly the largest and most accurate review of Docker adoption that has ever been published. However, while [Datadog's customers](https://www.datadoghq.com/customers/) span most industries, and run the gamut from startups to Fortune 100s, they do have some things in common. First, they take their software infrastructure seriously, and second they tend to be public and private cloud users. All the results in this article are biased by the fact that the data comes from our customers, a large but imperfect sample of the entire global market. Caveat lector.

## Averages

When we talk about average numbers within our customer base (for example, the average container lifespan) we are not actually talking about the mean value within the population. Rather we compute the average for each customer individually, and then report the median customer’s number. We found that when we took a true average, results were unduly skewed by unusual Docker practices employed by relatively few companies. For example, using a container as a queueable unit of work could cause individual companies to use thousands of containers per hour.

## Adoption Segments

This article categorizes companies as Docker "adopters", "dabblers", and "abandoners". Each company is recategorized at the end of each month, based on their Docker activity that month.

- **Adopter:** the average number of containers running during the month was at least 50% the number of distinct hosts run, or there were at least as many distinct containers as distinct hosts run during the month.
- **Dabbler:** used Docker during the month, but did not reach the "adopter" threshold.
- **Abandoner:** a currently active company that used Docker in the past, but hasn't used it at all in the last month.

Note that the adoption-segmentation thresholds are not derived from a natural grouping within the data; the data covers a continuous spectrum of use. Rather we used numbers that we felt would be intuitively meaningful to our readers.

Interestingly, the findings in this article are surprisingly resilient to different adoption-segmentation thresholds. For example, regardless of whether the adopter threshold is lower (25% containers on average, or 0.75x distinct containers compared to hosts) or higher (75% containers on average, or 1.5x distinct containers compared to hosts), most findings are unaltered:

- **Fact #1:** Real adoption is still up ~40% in one year.
- **Fact #2:** Adoption segmentation is not relevant to these findings.
- **Fact #3:** These graphs change very little under different thresholds. Companies with large and medium host counts still lead Docker adoption, with nearly identical adoption rates. And companies with large numbers of hosts remain more likely than those with small or midsize host counts to have tried Docker.
- **Fact #4:** Adoption segmentation is not relevant to these findings.
- **Fact #5:** Adopters still roughly 5x their container use between month 1 and month 10.
- **Fact #6:** Adoption segmentation is not relevant to these findings.
- **Facts #7, 8:** Results are not altered.

## Counting

Containers running only the Datadog Agent were excluded from this investigation, so Docker hosts that were only running the Agent were also excluded.

## Fact #1

We thought maybe we were seeing such a large increase in Docker use on Datadog precisely because Datadog is good at monitoring Docker. Maybe new Docker growth was fueled by new customers who needed Docker monitoring and came to Datadog specifically for that purpose. However, when we created cohorts of longtime Datadog customers, we saw almost identical adoption percentages.

## Fact #2

For each technology we monitor, we exclude from this calculation the organizations that are in the top 1% of its users. In other words, if a small number of companies use a particular technology in an unusual way, and use it quite heavily, they are excluded from the calculation.

Note, too, that the same basic shape of the "Percent hosts running Docker" graph persists even if we limit our population to Docker-using companies, or if we exclude the top 5%, 10%, or 25% of the Docker-using companies. In all cases, the percentage of hosts running Docker has been increasing steadily since late 2015.

## Fact #3

This finding is resilient to different infrastructure-size cut-points. Whether the cut-points are halved or doubled, the relative shape of the graph hardly changes, and the conclusion is exactly the same.