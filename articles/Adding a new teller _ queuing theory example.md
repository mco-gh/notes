Adding a new teller | queuing theory example

# What happens when you add a new teller?

Posted on [21 October 2008](https://www.johndcook.com/blog/2008/10/21/what-happens-when-you-add-a-new-teller/) by [John](https://www.johndcook.com/blog/author/john/)

Suppose a small bank has only one teller. Customers take an average of 10 minutes to serve and they arrive at the rate of 5.8 per hour. What will the expected waiting time be? What happens if you add another teller?

We assume customer arrivals and customer service times are random (details later). With only one teller, customers will have to wait nearly **five hours** on average before they are served. But if you add a second teller, the average waiting time is not just cut in half; it goes down to about **3 minutes**. The waiting time is reduced by a factor of 93x.

Why was the wait so long with one teller? There’s not much slack in the system. Customers are arriving every 10.3 minutes on average and are taking 10 minutes to serve on average. If customer arrivals were exactly evenly spaced and each took exactly 10 minutes to serve, there would be no problem. Each customer would be served before the next arrived. No waiting.

The service and arrival times have to be very close to their average values to avoid a line, but that’s not likely. On average there will be a long line, 28 people. But with a second teller, it’s not likely that even two people will arrive before one of the tellers is free.

Here are the technical footnotes. This problem is a typical example from queuing theory. Customer arrivals are modeled as a Poisson process with λ = 5.8/hour. Customer service times are assumed to be exponential with mean 10 minutes. (The Poisson and exponential distribution assumptions are common in queuing theory. They simplify the calculations, but they’re also realistic for many situations.) The waiting times given above assume the model has approached its steady state. That is, the bank has been open long enough for the line to reach a sort of equilibrium.

Queuing theory is fun because it is often possible to come up with surprising but useful results with simple equations. For example, for a single server queue, the expected waiting time is λ/(μ(μ – λ)) where λ the the arrival rate and μ is the service rate. In our example, λ = 5.8 per hour and μ = 6 per hour. Some applications require more complicated models that do not yield such simple results, but even then the simplest model may be a useful first approximation.

**Related post**: [Server utilization: Joel on queueing](https://www.johndcook.com/blog/2009/01/30/server-utilization-joel-on-queuing/)

For daily posts on probability, follow [@ProbFact](https://twitter.com/probfact) on Twitter.

[![](../_resources/16e150c01c3521fd16f05cd6615e513c.png)](https://twitter.com/probfact)
Categories : [Math](https://www.johndcook.com/blog/category/math/)
Tags : [Queueing theory](https://www.johndcook.com/blog/tag/queueing-theory/)

Bookmark the [permalink](https://www.johndcook.com/blog/2008/10/21/what-happens-when-you-add-a-new-teller/)