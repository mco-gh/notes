Why We Moved to Google Cloud Platform, in Two Slides

# Why We Moved to Google Cloud Platform, in Two Slides

[![1*5hCNGnaojyQSOwcXJfLrjg.jpeg](../_resources/eb6c9e2da2d654475144c7a0c93bf52e.jpg)](https://blog.usejournal.com/@michaelames?source=post_header_lockup)

[Michael Ames](https://blog.usejournal.com/@michaelames)
Apr 4·3 min read

Six months after taking our shiny new enterprise health data warehouse live on a “safe bet,” traditional, on-premises data warehousing platform, we were mired in performance, stability, and maintenance issues. In desperation we kicked off a stealth-mode pilot project to measure the capabilities of Google Cloud Platform — especially BigQuery — against the on-premises system.

Three months later we walked away from our original investment, completed a full migration to Google Cloud, and have never looked back.

I get asked all the time how we did it. If you’d like an in-person deep dive, it will be the subject of my [speaking session](https://cloud.withgoogle.com/next/sf?session=CMP102) at Google Cloud Next this month. Or you can listen to the whole story [here](https://youtu.be/wdFo_CtQNfA?t=1166) as I told it a couple years ago. There’s drama. Politics. Steak (or not). It’s a wonder I didn’t lose my job.

But over time I’ve come to realize that much of the *why* came down to the data on just two slides:

![](../_resources/86b95e6840ff3395efebfc7dda313cfa.png)![1*41vBOqVXWINH3EWw28OFIg.png](../_resources/4a3718740d967b9b53a8565ed553e051.png)

Slide 1: The essential capability of any data warehousing platform is performance. BigQuery kicked butt over the on-premises system.

The core capability of any data warehousing system is performance. If it can’t keep up with demand, there is literally no other benefit that will make it a worthwhile investment. The left chart shows the 50% performance improvement we found in comparing performance for the daily slog of loading and integrating data from source systems. The right chart shows a particular analytical process — fuzzy matching millions of patient records to look for duplicates — and how it went from taking 8 hours to about 15 minutes.

I’m not kidding about this. We’ve operated this system in production for two years now and the performance holds up. If anything, it’s better.

![](../_resources/d7a1a5f3f2839312c23cfa16261faaa1.png)![1*cktAPKhy4PDy1peM2FRegA.png](../_resources/7a667da2ad9084bcd3f6a3a1f79871db.png)

Slide 2: 5-year total cost of ownership analysis showed that we’d get these performance benefits at a fraction of the cost.

I care a great deal about elegant architectures, scalability, innovative product development, etc. But it turns out a lot of other people whose opinions matter care much more about money. Particularly where we were walking away from a major initial investment, we knew the “money slide” had to be compelling. And it was.

With the savings we’d generate by moving to Google Cloud, we could complete the full migration and relaunch on the new platform *within our original budget.* We could eliminate our performance and maintenance headaches, improve our security posture, position ourselves for future innovation, and do it all *without asking for more money.*

That’s why we did it.

Later I’ll write about *how*, including how we convinced a team of security, legal, and compliance officers that their data was safer on the cloud; how important it was to rethink architecture to maximize benefits and minimize costs; and how liberating it feels to free yourself from infrastructure headaches and focus instead on innovation and delivering value.

Follow me on [Twitter](https://twitter.com/michaelames).

* * *

*...*

[![](../_resources/063340fb6951aaa14ed7c020a3f1d020.png)![1*f2IVAl0TbsfES9cFGYr40g.png](../_resources/c772a2233d6d6a6f4998d42331b87625.png)](https://usejournal.com/?utm_source=medium.com&utm_medium=noteworthy_blog&utm_campaign=guest_post_image)

Read this story later in [Journal](https://usejournal.com/?utm_source=medium.com&utm_medium=noteworthy_blog&utm_campaign=guest_post_read_later_text).

Wake up every Sunday morning to the week’s most noteworthy Tech stories, opinions, and news waiting in your inbox: [Get the noteworthy newsletter >](https://usejournal.com/newsletter/?utm_source=medium.com&utm_medium=noteworthy_blog&utm_campaign=guest_post_text)