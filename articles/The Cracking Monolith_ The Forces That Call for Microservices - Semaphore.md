The Cracking Monolith: The Forces That Call for Microservices - Semaphore

 [![4062b608b628a89adeb54ec61e464c32.png](../_resources/c3ccc8bf86e54a92c8977e2a1354540b.png)](https://semaphoreci.com/blog/2017/03/21/cracking-monolith-forces-that-call-for-microservices.html#)

- [Marko Anastasov](https://plus.google.com/111529563576682640659?rel=author)

- 21 Mar 2017

- Posted in [Semaphore Engineering Blog](https://semaphoreci.com/blog/tags/engineering.html)

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fsemaphoreci.com%2Fblog%2F2017%2F03%2F21%2Fcracking-monolith-forces-that-call-for-microservices.html&ref_src=twsrc%5Etfw&text=The%20Cracking%20Monolith%3A%20The%20Forces%20That%20Call%20for%20Microservices%20-%20Semaphore&tw_p=tweetbutton&url=https%3A%2F%2Fsemaphoreci.com%2Fblog%2F2017%2F03%2F21%2Fcracking-monolith-forces-that-call-for-microservices.html&via=semaphoreci)

# The Cracking Monolith: The Forces That Call for Microservices

 ![](../_resources/44ae6481868c9814974ca822ffc61b09.jpg)

The microservice architecture has recently been gaining traction, with many companies sharing their positive experiences with applying it. The early adopters have been tech behemoths such as Amazon and Netflix, or companies with huge user bases like SoundCloud. Based on the profiles of these companies and the assumption that there’s more complexity to running and deploying many things than to deploying a single application, many people understand microservices as an interesting idea that does not apply to them. It’s something that mere mortals could qualify for in the far distant future, if ever.

However, obsessing about “being ready” is rarely a good strategy in life. I think that it’s far more useful to first learn how to detect when the opposite approach — a monolithic application — is no longer optimal. The knowledge that helps us to recognize the need enables us to start taking action when the time comes for us to make the change. This and future posts on our blog will be based on our experience of scaling up Semaphore to manage tens of thousands of private CI jobs on a daily basis.

Overweight monoliths exhibit two classes of problems: degrading system performance and stability, and slow development cycles. So, whatever we do comes from the desire to escape these technical and consequently social challenges.

### The single point of fragility

Today’s typical large monolithic systems started off as web applications written in an MVC framework, such as Ruby on Rails. These systems are characterized by either being a single point of failure, or having severe bottlenecks under pressure.

Of course, having *potential* bottlenecks, or having an entire system that is a single point of failure is not inherently a problem. When you’re in month 3 of your MVP, this is fine. When you’re working in a team of a few developers on a client project which serves 100 customers, this is fine. When most of your app’s functionality are well-designed CRUD operations based on human input with a linear increase of load, things are probably going to be fine for a long time.

Also, there’s nothing inherently wrong about big apps. If you have one and you’re not experiencing any of these issues, there’s absolutely no reason to change your approach. You shouldn’t build microservices solely in the service of making the app smaller — it makes no sense to replace the parts that are doing their job well.

Problems begin to arise after your single point of failure has actually started failing under heavy load.

At that point, having a large attack surface can start keeping the team in a perpetual state of emergency. For example:

- An outage in non-critical data processing brings down your entire website. With Semaphore, we had events where the monolith was handling callbacks from many CI servers, and when that part of the system failed, it brought the entire service down.
- You moved all time-intensive tasks to one huge group of background workers, and keeping them stable gradually becomes a full-time job for a small team.
- Changing one part of the system unexpectedly affects some other parts even though they’re logically unrelated, which leads to some nasty surprises.

As a consequence, your team spends more time solving technical issues than building cool and useful stuff for your users.

### Slow development cycles

The second big problem is when making any change happen begins to take too much time.

There are some technical factors that are not difficult to measure. A good question to consider is how much time it takes your team to ship a hotfix to production. Not having a fast delivery pipeline is painfully obvious to your users in the case of an outage.

What’s less obvious is how much the slow development cycles are affecting your company over a longer period of time. How long does it take your team to get from an idea to something that customers can use in production? If the answer is weeks or months, then your company is vulnerable to being outplayed by competition.

Nobody wants that, but that’s where the compound effects of monolithic, complex code bases lead to.

**Slow CI builds**: anything longer than a few minutes leads to too much unproductive time and task switching. As a standard for web apps [we recommend setting the bar at 10 minutes](https://semaphoreci.com/blog/2017/03/02/what-is-proper-continuous-integration.html)and [we actually draw the line for you](https://semaphoreci.com/blog/2017/03/16/measure-and-improve-your-ci-speed.html). Slow CI builds are one of the first symptoms of an overweight monolith, but the good news is that a good CI tool can help you fix it. For example, on Semaphore you can [split your test suite into parallel jobs](https://semaphoreci.com/docs/running-tests-in-parallel.html), or [let Semaphore do the work for you automatically](https://semaphoreci.com/product/test-boosters), regardless of the sequential runtime of your build.

**Slow deployment**: this issue is typical for monoliths that have accumulated many dependencies and assets. There are often multiple app instances, and we need to replace each one without having downtime. Moving to container-based deployment can make things even worse, by adding the time needed to build and copy the container image.

**High bus factor on the old guard, long onboarding for the newcomers**: it takes months for someone new to become comfortable with making a non-trivial contribution in a large code base. And yet, all new code is just a small percentile of the code that has already been written. The idiosyncrasies of old code affect and constrain all new code that is layered on top of the old one. This leaves those who have watched the app grow with an ever-expanding responsibility. For example, having 5 developers that are waiting for a single person to review their pull requests is an indicator of this.

**Emergency-driven context switching**: we may have begun working on a new feature, but an outage has just exposed a vulnerability in our system. So, healing it becomes a top priority, and the team needs to react and switch to solving that issue. By the time they return to the initial project, internal or external circumstances can change and reduce its impact, perhaps even make it obsolete. A badly designed distributed system can make this even worse — hence one of the requirements for making one is having solid design skills. However, if all code is part of a single runtime hitting one database, our options for avoiding contention and downtime are very limited.

**Change of technology is difficult**: our current framework and tooling might not be the best match for the new use cases and the problems we face. It’s also common for monoliths to depend on outdated software. For example, GitHub upgraded to Rails 3 four years after it was released. Such latency can either limit our design choices, or generate additional maintenance work. For example, when the library version that you’re using is no longer receiving security updates, you need to find a way to patch it yourself.

### Decomposition for fun and profit

While product success certainly helps, a development team that’s experiencing all of these issues won’t have the highest morale. Nor will its people be able to develop their true potential.

All this can happen regardless of code quality. [Practicing behavior-driven development](https://semaphoreci.com/community/tutorials/behavior-driven-development)is not a vaccine against scaling issues.

The root cause is simple. A monolithic application grows multiple applications within itself, and it meets high traffic and large volumes of data.

Big problems are best solved by breaking them up into many smaller ones that are easier to handle. This basic engineering idea is what leads teams to start decomposing large monoliths into smaller services, and eventually into microservices. The ultimate goal is to go back to being creative and successful by enabling the team to develop useful products as quickly as possible.