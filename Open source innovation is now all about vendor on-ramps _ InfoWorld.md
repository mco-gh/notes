Open source innovation is now all about vendor on-ramps | InfoWorld

# Open source innovation is now all about vendor on-ramps

### AWS, Microsoft, and Google are all racing to figure out how to turn their innovations into open source on-ramps to their proprietary services

![highway on-ramps](../_resources/6b3d24ad98636a5fa077b945dc9d1c44.jpg)

[Jayswipe](https://commons.wikimedia.org/wiki/File:Looking_over_CMJ_from_Hopetoun_Street_Bridge.JPG)

-
-
-
-
-
-
-
By[Matt Asay](https://www.infoworld.com/author/Matt-Asay/)
InfoWorld
Nov 30, 2017 3:00 AM

In the enterprise world, open source has long been a bit tentative. Starting in the early 2000s, various vendors started contributing bits and pieces of code, careful not to give away anything *too* valuable, all while hoping for positive marketing effect. It was, as [Stephen Walli wrote](http://stephesblog.blogs.com/my_weblog/2007/05/core_complement.html) in 2007, a matter of gifting complementary technology to secure potential customers’ interest in the core of your business.

It mostly didn’t work.
Content Continues Below
Ad

**[ Discover [2017’s best open source software for enterprise: The Bossie Award winners](https://www.infoworld.com/article/3227918/bossies-2017-the-best-of-open-source-software-awards.html#tk.ifw-infsb). | Track the latest trends in open source with InfoWorld’s [Open Source Report newsletter](https://www.infoworld.com/newsletters/signup.html#tk.ifw-infsb). ]**

Today, open source has become a primary driver of innovation, but we’re still too tentative in our contributions. Much of the most impressive innovation is being hatched at the public cloud vendors, specifically Amazon Web Services, Microsoft Azure, and Google Cloud (“AMG,” as [Bernard Golden calls them](http://bernardgolden.com/2017/11/amg-q317-cloud-financials-foretell-disruption/)), with [TensorFlow](https://www.infoworld.com/article/3237304/whats-new-in-tensorflow-machine-learning.html), [Kubernetes](https://www.infoworld.com/article/3207686/how-to-get-started-with-kubernetes.html), and more being contributed to the wider open source community.

But in a world where operations—not code—matter most, the AMG trio could contribute *all* their code without hurting their business, and with potentially much positive effect.

So why aren’t they?

## The innovation factories don’t benefit open source builders

DealPosts

- [![pre black friday](../_resources/47a75679222404218c2a2a6db017e4aa.jpg)](https://www.infoworld.com/article/3239787/mobile/need-stocking-stuffers-see-amazons-highest-rated-tech-deals-under-25-deal-alert.html)[Need Stocking Stuffers? See Amazon's Highest Rated Tech Deals Under $25 - Deal Alert](https://www.infoworld.com/article/3239787/mobile/need-stocking-stuffers-see-amazons-highest-rated-tech-deals-under-25-deal-alert.html)
- [![portable charger](../_resources/6b551ed0469c9e54e2b94391b7ce20b2.jpg)](https://www.infoworld.com/article/3237987/mobile/today-75-off-lumina-5200-mah-portable-power-bank-charger-deal-alert.html)[Today, 75% off Lumina 5200 mAh Portable Power Bank Charger - Deal Alert](https://www.infoworld.com/article/3237987/mobile/today-75-off-lumina-5200-mah-portable-power-bank-charger-deal-alert.html)
- [![august lock](../_resources/912dd17c1d75a6d60e424943afbaef26.jpg)](https://www.infoworld.com/article/3237469/home-tech/11-off-august-smart-lock-pro-with-connect-bundle-deal-alert.html)[11% off August Smart Lock Pro With Connect Bundle - Deal Alert](https://www.infoworld.com/article/3237469/home-tech/11-off-august-smart-lock-pro-with-connect-bundle-deal-alert.html)

Among legacy software bellwethers, growth has largely dried up, as Golden points out. HPE is forecasting less than 1 percent growth, while IBM has taken to trumpeting its mainframe business when it wants to signal innovation. Oracle may scrape together 5.5 percent growth, as some [analysts speculate](https://seekingalpha.com/article/4127685-oracle-tries-end-2017-clouds), buoyed by its aggressive push into the cloud.

Content Continues Below
Ad

The cloud is, of course, where all the growth is happening. Combined, the AMG trio has about 60 percent annual growth rate for the public cloud, or 600 percent growth over five years. That’s huge.

But the real story isn’t about growth. You might think that all that growth provides a great foundation for open source innovation, including contributions from the likes of AMG to the community that can be built on for the greater good. After all, as Golden highlights, the AMG triumvirate has “capabilities that no other user or tech vendor on the planet has, and those capabilities can be leveraged to deliver innovation unobtainable anywhere else.”

But Golden also notes the AMG innovation, even when open-sourced, doesn’t really help the community at large:

> Similar to Google’s unique ability to deliver [its Spanner] database technology are AMG offerings in these areas: IoT, event processing, machine learning, and commercial blockchain applications. I predict all of them will be the province of AMG and nobody else. Each requires investment and technical savvy beyond any other commercial entity. The recently announced intent by GE to get out of hosting its Predix business and rely on AWS and Azure is telling in this regard—if GE can’t afford to run an industrial-scale offering, who can? There is still tremendous innovation available in software, but it’s located at the interface of scale, investment, and technical > [> nous](https://en.wikipedia.org/wiki/Nous)> , which are the bailiwick of AMG.

In short: All this innovation is available to *buy*; none of it is available to build. Not for mere mortals, anyway.

Google is deliberating whether to open-source its Spanner technology. [CockroachDB](https://www.infoworld.com/article/3195773/open-source-sql-database-cockroachdb-hits-10.html), spawned by a former Googler, is already working on its own open source Spanner. As good as it is, however, it’s not Spanner. Spanner depends on TrueTime, a powerful way of coordinating resources in disparate places. No one but Google has this technology, although AWS and Microsoft could conceivably build it. Pretty much no one else on Earth could.

Content Continues Below
Ad

Now, multiply Spanner across a range of possible projects, from Google’s TensorFlow to [AWS Lambda](https://www.infoworld.com/article/3204669/aws-lambda-tutorial-how-amazons-serverless-functions-work.html) to Microsoft’s [Cosmos DB](https://www.infoworld.com/article/3223728/nosql-standouts-the-best-key-value-databases-compared.html). These companies could give you the code (and, in the case of TensorFlow, Google already has), but having the code won’t make you operate like the AMG.

As Golden colorfully describes: “Maintaining the position that making the code available realistically enables someone else to implement Spanner functionality would be like someone handing me a pair of running shoes like the ones Usain Bolt wears and telling me that I can now run a 9.58-second 100 meters. Bolt has the genetics, the training regimen, the ecosystem, and the single-minded drive of a great athlete. Me? I’ve got a pair of sneakers.”

More than a decade ago, Jeremy Zawodny (then at Yahoo) [took me to task](http://jeremy.zawodny.com/blog/archives/007112.html) for suggesting his company (and Google) should open-source more code. He rightly pointed out that it’s not that simple and, as he (and Google’s Chris DiBona) had said at OSCON earlier, what would be the point? Giving away a bunch of code that is tightly bound to Yahoo’s infrastructure wouldn’t really give you much insight into how to operate that code like Yahoo. Instead, it might just render you frustrated.

## Where the action is: Open-sourcing more on-ramps

Since then, Google in particular has figured out how to both open-source code in a useful way *and* make it pay. As Server Density CEO [David Mytton has underlined](http://www.infoworld.com/article/3072569/cloud-computing/googles-cloud-strategy-becomes-clearer-with-tensorflow.html), Google hopes to “standardize machine learning on a single framework and API,” namely TensorFlow, then supplement it “with a service that can [manage] it all for you more efficiently and with less operational overhead,” namely Google Cloud.

By open-sourcing TensorFlow and backing it with machine-learning-heavy Google Cloud, Google has open-sourced a great on-ramp to future revenue.

Content Continues Below
Ad

My question: why not do this with the rest of its code?

The simple answer is “Because it’s a lot of work.” That is, Google could open-source everything tomorrow without any damage to its revenue, but the code itself would provide other providers and enterprises only limited ability to *increase* their revenue unless Google did all the necessary prep work to make it useful to mere mortals not running superhuman Google infrastructure.

This is the trick that AWS, Microsoft, and Google are all racing to figure out today. Not open source, per se, because that’s the easy table stakes. No, the AMG trio are figuring out how to turn their innovations into open source on-ramps to their proprietary services.

Companies used to lock up their code to sell it. Today, it’s the opposite: They need to open it up to make their ability to operate the code at scale more valuable. For them.

Content Continues Below
Ad