The Incredible Growth of Python | Stack Overflow

#  The Incredible Growth of Python

We [recently explored](https://stackoverflow.blog/2017/08/29/tale-two-industries-programming-languages-differ-wealthy-developing-countries/?utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python) how wealthy countries (those defined as [high-income](https://en.wikipedia.org/wiki/World_Bank_high-income_economy) by the World Bank) tend to visit a different set of technologies than the rest of the world. Among the largest differences we saw was in the programming language Python. When we focus on high-income countries, the growth of Python is even larger than it might appear from tools like [Stack Overflow Trends](https://insights.stackoverflow.com/trends?tags=python%2Cjavascript%2Cjava%2Cc%23%2Cphp%2Cc%2B%2B&utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python), or in other rankings that consider global software development.

In this post, we’ll explore the extraordinary growth of the Python programming language in the last five years, as seen by Stack Overflow traffic within high-income countries. The term “fastest-growing” can be [hard to define precisely](https://xkcd.com/1102/), but we make the case that **Python has a solid claim to being the fastest-growing major programming language.**

All the numbers discussed in this post are for **high-income countries**; they’re generally representative of trends in the United States, United Kingdom, Germany, Canada, and other such countries, which in combination make up about 64% of Stack Overflow’s traffic. Many other countries such as India, Brazil, Russia, and China also make enormous contributions to the global software development ecosystem, and this post is less descriptive of those economies, though we’ll see that Python has shown growth there as well.

It’s worth emphasizing up front that the number of users of a language isn’t a measure of the language’s quality: we’re *describing* the languages developers use, but not prescribing anything. (Full disclosure: I [used to program](https://stackoverflow.com/search?tab=newest&q=user%3a712603%20%5bpython%5d) primarily in Python, though I have since switched entirely to R).

### Python’s growth in high-income countries

You can see on [Stack Overflow Trends](https://insights.stackoverflow.com/trends?tags=python%2Cjavascript%2Cjava%2Cc%23%2Cphp%2Cc%2B%2B&utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python) that Python has been growing rapidly in the last few years. But for this post we’ll focus on high-income countries, and consider visits to questions rather than questions asked (this tends to give similar results, but has less month-by-month noise, especially for smaller tags).

We have data on Stack Overflow question views going back to late 2011, and in this time period we can consider the growth of Python relative to five other major programming languages. (Note that this is therefore a shorter time scale than the Trends tool, which goes back to 2008). These are currently six of the ten most-visited Stack Overflow tags in high-income countries; the four we didn’t include are CSS, HTML, Android, and JQuery.

June 2017 was the first month that **Python was the most visited tag on Stack Overflow within high-income nations**. This included being the most visited tag within the US and the UK, and in the top 2 in almost all other high income nations (next to either Java or JavaScript). This is especially impressive because in 2012, it was less visited than any of the other 5 languages, and has grown by 2.5-fold in that time.

Part of this is because of the seasonal nature of traffic to Java. Since it’s [heavily taught in undergraduate courses](https://stackoverflow.blog/2017/02/15/how-do-students-use-stack-overflow/), Java traffic tends to rise during the fall and spring and drop during the summer. Will it catch up with Python again by the end of the year? We can try forecasting the next two years of growth with a [model called “STL”](http://otexts.org/fpp2/sec-6-stl.html), which combines growth with seasonal trends to make a prediction about future values.

According to this model, Python could either stay in the lead or be overtaken by Java in the fall (it’s roughly within the variation of the model’s predictions), but it’s clearly on track to become the most visited tag in 2018. STL also suggests that JavaScript and Java will remain at similar levels of traffic among high income countries, just as they have for the last two years.

### What tags are growing the fastest overall?

The above was looking only at the six most-visited programming languages. Among other notable technologies, which are currently growing the fastest in high-income countries?

We defined the growth rate in terms of the ratio between 2017 and 2016 share of traffic. We decided to consider only programming languages (like Java and Python) and platforms (such as iOS, Android, Windows and Linux) in this analysis, as opposed to frameworks like [Angular](https://stackoverflow.com/questions/tagged/angular) or libraries like [TensorFlow](https://stackoverflow.com/questions/tagged/tensorflow) (although many of those showed notable growth that may be examined in a future post).

Because of the challenges in defining “fastest-growing” described in [this comic](https://xkcd.com/1102/), we compare the growth to the overall average in a [mean-difference plot](https://en.wikipedia.org/wiki/Bland%E2%80%93Altman_plot).

![tag_growth_scatter-1-1-1024x896.png](../_resources/337b0c36b14a6eca15230ab3c880ea3c.png)

With a 27% year-over year-growth rate, Python stands alone as a tag that is **both large and growing rapidly**; the next-largest tag that shows similar growth is R. We see that traffic to most other large tags has stayed pretty steady within high-income countries, with visits to Android, iOS, and PHP decreasing slightly. We previously examined some of the shrinking tags like Objective-C, Perl and Ruby in our [post on the death of Flash](https://stackoverflow.blog/2017/08/01/flash-dead-technologies-might-next/?utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python)). We can also notice that among functional programming languages, Scala is the largest and growing, while F# and Clojure are smaller and shrinking, with Haskell in between and remaining steady.

There’s an important omission from the above chart: traffic to TypeScript questions grew by an impressive 142% in the last year, enough that we left it off to avoid overwhelming the rest of the scale. You can also see that some other smaller languages are growing similarly or faster than Python (like R, Go and Rust), and there are a number of tags like Swift and Scala that are also showing impressive growth. How does their traffic over time compare to Python’s?

The growth of languages like R and Swift is indeed impressive, and TypeScript has shown especially rapid expansion in an even shorter time. Many of these smaller languages grew from getting almost no question traffic to become notable presences in the software ecosystem. But as this graph shows, it’s easier to show rapid growth when a tag started relatively small.

Note that we’re not saying these languages are in any way “competing” with Python. Rather, we’re explaining why we’d treat their growth in a separate category; these were lower-traffic tags to start with. Python is an unusual case for being **both one of the most visited tags on Stack Overflow and one of the fastest-growing ones**. (Incidentally, it is also accelerating! Its year-over-year growth has become faster each year since 2013).

### Rest of the world

So far in this post we’ve been analyzing the trends in high-income countries. Does Python show a similar growth in the rest of the world, in countries like India, Brazil, Russia and China?

Indeed it does.

![non_high_income_graph-1-1-1024x731.png](../_resources/249d4702302d3eacecac7ef907ab93bd.png)

Outside of high-income countries Python is *still* the fastest growing major programming language; it simply started at a lower level and the growth began two years later (in 2014 rather than 2012). In fact, the year-over-year growth rate of Python in non-high-income countries is slightly *higher* than it is in high-income countries. We don’t examine it here, but R, the [other language whose usage is positively correlated with GDP](https://stackoverflow.blog/2017/08/29/tale-two-industries-programming-languages-differ-wealthy-developing-countries/?utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python), is growing in these countries as well.

Many of the conclusions in this post about the growth and decline of tags (as opposed to the absolute rankings) in high-income countries hold true for the rest of the world; there’s a 0.979 Spearman correlation between the growth rates in the two segments. In some cases, you can see a “lagging” phenomenon similar to what happened with Python, where a technology was widely adopted within high-income countries a year or two before it expanded in the rest of the world. (This is an interesting phenomenon and may be the subject of a future blog post!)

### Next time

We’re not looking to contribute to any “language war.” The number of users of a language doesn’t imply anything about its quality, and certainly can’t tell you which language is [more appropriate for a particular situation](https://stackoverflow.blog/2011/08/16/gorilla-vs-shark/?utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python). With that perspective in mind, however, we believe it’s worth understanding what languages make up the developer ecosystem, and how that ecosystem might be changing.

This post demonstrated that Python has shown a surprising growth in the last five years, especially within high-income countries. In our next post, we’ll start to explore the *“why”*. We’ll segment the growth by country and by industry, and examine what other technologies tend to be used alongside Python (to estimate, for example, how much of the growth has been due to increased usage of Python for web development versus for data science).

In the meantime, if you work in Python and are looking to take the next step in your career, here are [some companies hiring Python developers right now on Stack Overflow Jobs](https://stackoverflow.com/jobs/developer-jobs-using-python?utm_source=so-owned&utm_medium=blog&utm_campaign=gen-blog&utm_content=blog-link&utm_term=incredible-growth-python).