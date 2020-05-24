SpeedCurve | Third party blame game

# Third party blame game

WEDNESDAY 15TH OF MAY 2019

Our third party metrics and dashboard have had an exciting revamp. With new metrics like blocking CPU, you can now see exactly who is really to blame for a crappy user experience. We've also given you the ability to monitor individual third parties over time and create performance budgets for them.

## It's not you, it's me

Or is it really you, and not me? We now automatically group all the requests in our third party waterfall chart, letting you easily identify all the third party services used on your website.

[![third_party_waterfall.png](../_resources/de7d2c7173f8d9371c28162918e5b8a6.jpg)](https://speedcurve.com/demo/thirdparty/?b=chrome&cs=lg&d=30&dc=2&de=1&ds=1&r=us-west-1&s=299&u=906&share=39tfnozeq94p1o0hndk1kpbg4vb7cg)

For each third party, you get the number of requests and size for each content type. There's also a first party comparison you can toggle on/off to see what proportion of your requests come from first party vs third party.

![latest_third_party_requests.png](../_resources/90b23ed2f0126c08aa2be6e9f8e32e9d.jpg)

## Blocking JS, CSS & CPU

People love to hate on third parties and blame all their user experience issues on them.

> Look at all those requests, it must be them!

We don't believe that just looking at the number of requests or the size of requests a third party makes is a good enough indicator that they are a bad actor. A well-built web page that manages its requests can easily negate any issues by delaying those request till after the page is rendered and interactive.

**What really matters is how a third party might be blocking the rendering or the interactivity of the page. **

So for each third party, we show you if it includes any blocking JS or CSS requests. This tells you if the rendering of the page is being delayed by a blocking request from a third party. We also look for any blocking CPU caused by a third party. Blocking CPU is any JS function that takes longer than 50ms (also known as a [long task](https://github.com/w3c/longtasks)), which often leads to [page jank.](https://speedcurve.com/blog/measuring-jank-and-ux/) Blocking CPU stops your users from smoothly interacting with your page and delays other metrics like [First CPU Idle](https://developers.google.com/web/tools/lighthouse/audits/first-cpu-idle) and [Time To Interactive.](https://github.com/WICG/time-to-interactive#definition) These third party blocking metrics are a far better indicator of who might be causing real issues on your page.

In this example, Vidible has 594ms of blocking CPU, causing jank on the page, while all the other third parties don't trigger any signifiant CPU activity at all. This helps you quickly focus in on which third parties are causing real user experience problems.

[![latest_third_party_cpu.png](../_resources/f66d09d1914e8e2a34c0fae671b66c6d.jpg)](https://speedcurve.com/demo/thirdparty/?b=chrome&cs=lg&d=30&dc=2&de=1&ds=1&r=us-west-1&s=299&u=906&share=39tfnozeq94p1o0hndk1kpbg4vb7cg)

## Collect the evidence!

For any third party in your waterfall, you can turn on "Track History" and we'll collect detailed third party metrics every time we run a test. You can then monitor a third party over time and set performance budgets and alerts. This is a great way to keep an eye on any changes a third party might be making and alerting you to impacts on your page. You could even agree to an SLA with a third party and then use SpeedCurve to monitor and enforce it, keeping everyone honest and on the same page.

[![third_party_history.png](../_resources/90308d738a28925d672bcae83332a574.jpg)](https://speedcurve.com/demo/thirdparty/?b=chrome&cs=lg&d=30&dc=2&de=1&ds=1&r=us-west-1&s=299&u=906&share=39tfnozeq94p1o0hndk1kpbg4vb7cg)

## Track any request

Even though it's called third party, you can actually build your own custom filters and track any group of requests you like. You can even track the history and set performance budget and get alerts for a single request. If your task is to trim down a specific JS request and make sure its size or CPU usage is within budget, then you can setup a specific filter and monitor your improvements.

![third_party_custom.png](../_resources/2551b7b33a13bd58576ab07d94a7feaa.jpg)

## Contribute

We used to have our own in-house library for identifying third parties but we've now switched to [third-party-web](https://github.com/patrickhulce/third-party-web) by Patrick Hulce, which has a quickly growing list of third parties. Many people in the perf community, such as Simon Hearne of [requestmap](https://simonhearne.com/2015/find-third-party-assets/) fame, have been identifying and contributing third parties to third-party-web – and we've recently added a bunch, too! If you see any "Unrecognized Third Party" requests in your waterfall charts, then you can [contribute them to the project.](https://github.com/patrickhulce/third-party-web#contributing)

## Getting started

If you already use SpeedCurve, then you can start tracking your third parties straight away in your Settings or on the Synthetic > Third Party dashboard. Otherwise, [kick off a free trial](https://speedcurve.com/setup/trial/) to see if it's a third party that's eating up your bandwidth and CPU, or your own requests.

[third party](https://speedcurve.com/blog/tag/third-party/)  [jank](https://speedcurve.com/blog/tag/jank/)  [RSS](https://speedcurve.com/blog/rss/)

- [0 comments]()
- [**SpeedCurve**](https://disqus.com/home/forums/speedcurve/)
- [Login](https://disqus.com/embed/comments/?base=default&f=speedcurve&t_u=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fthird-party-blame-game%2F&t_d=Third%20party%20blame%20game&t_t=Third%20party%20blame%20game&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  1](https://disqus.com/embed/comments/?base=default&f=speedcurve&t_u=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fthird-party-blame-game%2F&t_d=Third%20party%20blame%20game&t_t=Third%20party%20blame%20game&s_o=default#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=speedcurve&t_u=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fthird-party-blame-game%2F&t_d=Third%20party%20blame%20game&t_t=Third%20party%20blame%20game&s_o=default#)

![blockquote.69435f6faa8c7a193456c46bcb7fb1ed.png](../_resources/7b2fde640943965cc88df0cdee365907.png)

Start the discussion…

![strikethrough.ced68e63961c6bc0e072ce907906b252.png](../_resources/c6501c3f7d72fc1b6c5c664055aa9562.png)

![link.5ef9a39f22ce49f926e304567b9d611b.png](../_resources/a07b7e1fcec6807578565deaf67fee1b.png)

![underline.59f82f5f5bbed90fd72132ef98662fe3.png](../_resources/81c01ba2374c675c3aeaaa782bf2e78c.png)

![spoiler.eff5de8f72591c5ceeb4fa26a117c6d1.png](../_resources/f7efeff64e3b50b6ed3ac56e033c7093.png)

![attach.03c320b14aa9c071da30c904d0a0827f.png](../_resources/77ac7d224499e3ad46945902c341b126.png)

![noavatar92.7b2fde640943965cc88df0cdee365907.png](../_resources/c004e6b74d78957de021cd89afcfb140.png)

![italic.a6e1da4a89899ae5e87db9ded9f84d5b.png](../_resources/1a93c9927335a0e22c1e2f44320b38f3.png)

![bold.cb366e6a49396fb0e47a01df277563c8.png](../_resources/7b7516fe3c1d4c3b33fd1a97f4371bc8.png)

[![code.8f558a246aa4e9c41ef343f72f012f01.png](../_resources/e1832a588b49918e9acc6d7c3c680534.png)](https://disqus.com/embed/comments/?base=default&f=speedcurve&t_u=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fthird-party-blame-game%2F&t_d=Third%20party%20blame%20game&t_t=Third%20party%20blame%20game&s_o=default#)

![gif-picker.df38180f2d048c25fe42a2b440ff863e.png](../_resources/5006a22ded0c9cbb1ffb485f61457686.png)

###### Log in with

-
-
-
-

######  or sign up with Disqus

?

### Disqus is a discussion network

- Disqus never moderates or censors. The rules on this community are its own.
- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

Be the first to comment.

## Also on **SpeedCurve**

- [

### The average web page is 3MB. How much should we care?

    - 17 comments •

    - 2 years ago

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Patrice Midori —  Good article if you have fiber optics. We still have DSL 1MB/S so .... a 3 MB page, i just don't load it fully, …](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fweb-performance-page-bloat%2F&key=7R8Yr25GYIz7GnFv5UQ6BQ)](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fweb-performance-page-bloat%2F&key=7R8Yr25GYIz7GnFv5UQ6BQ)

- [

### SpeedCurve | Rendering Metrics

    - 6 comments •

    - a year ago

[![avatar92.jpg](../_resources/a3576d12de2b9a1551bdb7a33530342c.jpg) benhastings —  Synthetic monitoring falls into the category of services that tools like Webpagetest afford to site …](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Frendering-metrics%2F&key=mSYz9oJktKbApYhrdmP_tg)](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Frendering-metrics%2F&key=mSYz9oJktKbApYhrdmP_tg)

- [

### An analysis of Chromium's paint timing metrics

    - 5 comments •

    - 8 months ago

[![avatar92.jpg](../_resources/1887d60fff2e2860900aace56f73a5b3.jpg) jason —  Oh that way I understand, I just got stuck on how to run a synthetic test for real users because the metrics are …](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fan-analysis-of-chromiums-paint-timing-metrics%2F&key=qbbUG98iYLswxbWJ-tbuUA)](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fan-analysis-of-chromiums-paint-timing-metrics%2F&key=qbbUG98iYLswxbWJ-tbuUA)

- [

### Metrics from 1M Sites

    - 1 comment •

    - 5 months ago

[![avatar92.jpg](:/90f303ad2699cd92a944dd7d11c1e721) Julio C. Guevara —  Hi Steve, very interesting insight. I am working on something fairly similar right now. I am …](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fmetrics-from-1m-sites%2F&key=vTDrS9Pm0bk_LFmzBEPjjA)](https://disq.us/?url=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fmetrics-from-1m-sites%2F&key=vTDrS9Pm0bk_LFmzBEPjjA)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=speedcurve&t_u=https%3A%2F%2Fspeedcurve.com%2Fblog%2Fthird-party-blame-game%2F&t_d=Third%20party%20blame%20game&t_t=Third%20party%20blame%20game&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=speedcurve&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)