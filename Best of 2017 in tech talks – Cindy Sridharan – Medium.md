Best of 2017 in tech talks – Cindy Sridharan – Medium

# Best of 2017 in tech talks

I usually publish a list of my favorite talks at the end of the year ([here’s](https://medium.com/@copyconstruct/best-of-2016-in-talks-7a4673bad544) the 2016 edition of this post). I’m a couple of weeks late, but all the same I decided to put together a list of my favorite talks from 2017 in no particular order. This list is by no means exhaustive and there are probably many gems from 2017 I’ll only discover in the future, but among the talks I attended or watched, these were some of the best.

1. **Simulating a Real World System in Go**, [Sameer Ajmani](https://twitter.com/sajma),

An *incredible*, *incredible* talk presented at [**dotGo**](https://www.dotgo.eu/) on the parallels between writing concurrent programs and the real world. Watch this, even if you’re not a Go programmer, for a fantastic primer on concurrency.

Video — https://www.youtube.com/watch?v=_YK0viplIl4
2. **Zebras all the way down**, [Bryan Cantrill](https://twitter.com/bcantrill)

From the inaugural [**UptimeConf**](https://uptime.events/). This talk has influenced my thinking about building observable and debuggable systems in more ways than I can imagine. If there’s *one* talk you watch from this list, make sure it’s this one.

Video — https://www.youtube.com/watch?v=fE2KDzZaxvE
3. **Requests Under the Hood**, [Cory Benfield](https://twitter.com/Lukasaoz)

This was a fantastic talk from **PyCon**, not so much about the [requests](https://github.com/requests/requests) library per se than about tradeoffs in programming, handling of exotic edge cases and an exercise in pragmatism.

Video — https://www.youtube.com/watch?v=ptbCIvve6-k
4. **The Memory Chronicles**, [Kavya Joshi](https://twitter.com/kavya719)
![resize.jpg](../_resources/0d4821b19677105d8352ceb5392b72f8.jpg)

It’s a **PyCon** talk by Kavya, which means by default it’s a *brilliant* talk. That should be reason enough for you to watch this talk. A fantastic dive into the internals of how CPython and Micropython manage memory differently.

Video — https://www.youtube.com/watch?v=d7qEzpnkWaY
5. **Measuring and Optimizing Tail Latency**, Kathryn McKinley

A phenomenal talk from **Strangeloop** on root-causing and optimizing tail latency in data center environments for a variety of workloads. I believe this was the opening Keynote.

Video — https://www.youtube.com/watch?v=_Zoa3xkzgFk

As an aside, Strangeloop is the one conference I’m absolutely hoping I can attend in 2018. I’ve never been before and it’s by far one of the best technical conferences in many, many regards.

6.** Modern Python Dictionaries — A confluence of a dozen great ideas,**  [Raymond Hettinger](https://twitter.com/raymondh)

Watch this talk even if you’re not a Python programmer. The first time I saw this talk was in December 2016 at the [SF Python meetup’s second annual holiday party](https://www.youtube.com/watch?v=p33CVV29OG8), but seeing it again at **PyCon** was no less delightful than the first time around. Raymond takes us back in time to the 70s and how technologies pioneered then in the field of database research are finding their way back into the modern era.

Video — https://www.youtube.com/watch?v=npw4s1QTmPg

7. **The Dictionary Even Mightier**, [Brandon Rhodes](https://twitter.com/brandon_rhodes)

Brandon Rhodes is one of my absolute favorite speakers. I look forward to PyCon every year only just to know what new talk he has in store. This is a sequel to his insanely popular PyCon 2010 talk [The Mighty Dictionary](https://www.youtube.com/watch?v=C4Kc8xzcA68), which was an amazing look at the internals of how dictionaries are implemented in Python.

Video — https://www.youtube.com/watch?v=66P5FMkWoVU
8. **Understanding Channels**, Kavya Joshi

My favorite talk of the year from **GopherCon**. A deep dive into the channel implementation in Go by one of my all time favorite speakers.

Video — https://www.youtube.com/watch?v=KBZlN0izeiY

9. **Predictive Load Balancing: Unfair but Faster and More Robust**, [Steve Gury](https://twitter.com/stevegury)

Another fantastic talk on detecting and mitigating tail latency issues from **Strangeloop**. It sheds light on the practicalities of client side load balancing at Netflix and proposes a way to calculate latency over a moving window of time by marrying ideas from game theory and queuing theory.

Video — https://www.youtube.com/watch?v=6NdxUY1La2I

10. **Stop Rate Limiting — Capacity Planning Done Right**, [Jon Moore](https://twitter.com/jon_moore)

Yet another great — and very approachable — talk from **Strangeloop** on the basics of Little’s Law and concurrency control, as well as the shortcomings of standard rate limiting. It proposes an adaptive, optimistic algorithm that works well with a constantly changing mix of elastic origin capacity, population of clients, and fluctuating usage.

Video — https://www.youtube.com/watch?v=m64SWl9bfvk

11. **Why we built our own distributed column store**, [Sam Stokes](https://twitter.com/samstokes)

Video — https://www.youtube.com/watch?v=tr2KcekX2kk

Surprising transparency into the internals of [Honeycomb](https://honeycomb.io/). Yet another fantastic **Strangeloop** talk on the tradeoffs that go into replicating a Facebook scale product at a small scale startup. If that doesn’t sound exciting enough, the talk’s worth a watch just to hear Sam speak. I remember discussing about this talk at another conference in early October in New York City with some of the attendees there, and one of the common points we kept circling back to was how the *delivery* of the talk truly made all the difference.

![resize.jpg](../_resources/290b29bc593d9a824e657ca7f2be147f.jpg)

12. **Scalability Is Quantifiable: The Universal Scalability Law**, [Baron Schwartz](https://twitter.com/xaprb)

A brilliant talk from [**LISA**](https://www.usenix.org/conference/lisa17/conference-program/presentation/schwartz) on the practical applications of the Universal Scalability Law as well how the law describes and predicts day to day system behavior.

Video — https://www.youtube.com/watch?v=lZU6RK0oazM

13. **Instrumenting Systems for Arbitrary Observability**, [Baron Schwartz](https://twitter.com/xaprb)

Video — [bit.ly/2zLBLiL](https://t.co/rXQUYzO9uk)
![resize.jpg](../_resources/d32ec32fcdd98ce207e9085eee10fee5.jpg)

If you’re ever wondered what does observable code look like? What instrumentation creates systems that are observable later in arbitrary ways, in circumstances you can’t foresee? And how can you make your systems observable? This [**Velocity New York**](https://conferences.oreilly.com/velocity/vl-ny/public/schedule/detail/61630) talk answers these questions and many more.

14. **Queueing Theory in Practice: Performance Modeling for the Working Engineer**, [Eben Freeman](https://twitter.com/_emfree_)

Another talk from [**LISA**](https://www.usenix.org/conference/lisa17/) and hands down the ***best*** talk I’ve watched on the topic of Queueing Theory.

> Kubernetes and similar cloud-native infrastructure make it easier than ever to adjust a service’s capacity based on variable demand. In practice, it’s still hard to take observed metrics, and translate them into quantitative predictions about what will happen to service performance as load changes. Resource limits are often chosen by guesstimation, and teams are likely to find themselves reacting to slowdowns and bottlenecks, rather than anticipating them. Queueing theory can help, by treating large-scale software systems as mathematical models. But it’s not easy to translate between real-world systems and textbook models. This talk will cover practical techniques for turning operational data into actionable predictions. We’ll show how to use results from queueing theory to develop a model of system performance. We’ll discuss what data to gather in production to better inform its predictions — for example, why it’s important to capture the shape of a latency distribution, and not just a few percentiles. We’ll also talk about some of the limitations and pitfalls of performance modeling.

Video — https://www.youtube.com/watch?v=yf6wSsOFqdI

15. **PyCon Closing Keynote**, [Kelsey Hightower](https://twitter.com/kelseyhightower)

This is an awe-inspiring talk where Kelsey deploys a Kubernetes cluster with a voice assistant. Watch it, just to see a master at the zenith of his craft.

Video — https://www.youtube.com/watch?v=u_iAXzy3xBA

16. **Go Anti-Patterns**, [Edward Muller](https://twitter.com/freeformz?lang=en)

A brilliant talk from **GopherCon** about all the common Go anti-patterns seen in the wild, from an explosion of tiny packages to gargantuan config structs to the dreaded `package util` to when and how not to use pointers.

Video — https://www.youtube.com/watch?v=ltqV6pDKZD8

17. **Debugging under fire: Keeping your head when systems have lost their mind, **[Bryan Cantrill](https://twitter.com/bcantrill)

Presented as a [**GOTO Chicago**](https://gotochgo.com/2017#about) Keynote, this is yet another doozy from Bryan Cantrill, building on some of the ideas presented in the previous talk. It explains better than any other talk I’ve watched why enshrining debuggability into applications is arguably the most important aspect of system design.

Video — https://www.youtube.com/watch?v=30jNsCVLpAE

18. **Monitoring Cloudflare’s Planet-Scale Edge Network with Prometheus**, [Matt Bostock](https://twitter.com/mattbostock)

This talk was first presented at the [August 2017 SF Prometheus meetup](https://www.meetup.com/SF-Prometheus-Meetup-Group/events/241917848/) I organized and it was probably the first time I’d heard of a Prometheus deployment of this scale. A fascinating talk about various decisions and tradeoffs that went into pulling this off, as well as the pain points that still remain.

![resize.jpg](../_resources/a444fc78acf78bc4ab0d3ef233f13234.jpg)

Video — https://promcon.io/2017-munich/talks/monitoring-cloudflares-planet-scale-edge-network-with-prometheus/

19. **Online Experimentation with Converged, Immutable Infrastructure**, [Tim Perrett](https://twitter.com/timperrett/)

A great talk on how experimentation is vastly more effective than pre-production testing for various scenarios. This greatly influenced my recent blog post [**Testing Microservices, the sane way**](https://medium.com/@copyconstruct/testing-microservices-the-sane-way-9bb31d158c16).

Video — https://www.youtube.com/watch?v=PyXF0k2DUG0&feature=youtu.be