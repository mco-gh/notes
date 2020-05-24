Spanner, the Google Database That Mastered Time, Is Now Open to Everyone

- [**]()
- [**]()

![SpannerTA-686869005.jpg](../_resources/b6ebe8f01b2ea2a2a8f2540377563670.jpg)
Slide:  1 /  of  1.Caption: Getty Images

[Skip Article Header. Skip to: Start of Article.](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/#start-of-content)

- Author: Cade Metz.[Cade Metz](https://www.wired.com/author/cade_metz/)[Business](https://www.wired.com/category/business/)
- Date of Publication: 02.14.17.02.14.17
- Time of Publication: 12:00 pm.12:00 pm

# Spanner, the Google Database That Mastered Time, Is Now Open to Everyone

- [**]()
- [**]()

![Aerial View of Chicago, IL, USA](../_resources/46bd97c3d955a663954cfe61fca21c19.jpg)
 Getty Images

About a decade ago, a handful of Google’s most talented engineers [started building a system](https://www.wired.com/2012/11/google-spanner-time/) that seems to defy logic.

Called Spanner, it was the first global database, a way of storing information across millions of machines in dozens of data centers spanning multiple continents, and it now underpins everything from Gmail to AdWords, the company’s primary moneymaker. But it’s not just the size of this creation that boggles the mind. The real trick is that, even though Spanner stretches across the globe, it behaves as if it’s in one place.

Google can change company data in one part of this database—running an ad, say, or debiting an advertiser’s account—without contradicting changes made on the other side of the planet. What’s more, it can readily and reliably replicate data across multiple data centers in multiple parts of the world—and seamlessly retrieve these copies if any one data center goes down. For a truly global business like Google, such transcontinental consistency is enormously powerful.

#### Related Stories

- [![The Epic Story of Dropbox's Exodus From the Amazon Cloud Empire](../_resources/aee78fbcd85e846b476d3ecfca6561e1.jpg) Cade Metz ##### The Epic Story of Dropbox’s Exodus From the Amazon Cloud Empire](https://www.wired.com/2016/03/epic-story-dropboxs-exodus-amazon-cloud-empire/)

* * *

- [![Dell. EMC. HP. Cisco. These Tech Giants Are the Walking Dead](../_resources/3c976930e0a2dff7f19623c301571fa5.jpg) Cade Metz ##### Dell. EMC. HP. Cisco. These Tech Giants Are the Walking Dead](https://www.wired.com/2015/10/meet-walking-dead-hp-cisco-dell-emc-ibm-oracle/)

* * *

- [![Google's Cloud Investments are Finally Starting to Pay Off](../_resources/3eea77a9c92246ed0bed2914d0265908.jpg) Klint Finley ##### Google’s Cloud Investments are Finally Starting to Pay Off](https://www.wired.com/2016/07/googles-cloud-investments-finally-starting-pay-off/)

* * *

Before Spanner, this didn’t seem possible. Machines couldn’t keep databases [consistent](https://en.wikipedia.org/wiki/Consistency_(database_systems)) without constant and heavy communication, and communication across the globe took much too long. You know, the speed of light and all that. Google’s engineers needed something like the [the ansible](https://en.wikipedia.org/wiki/Ansible), a fictional device that first appeared in Ursula Le Guin’s 1966 novel [*Rocannon’s World*](https://en.wikipedia.org/wiki/Rocannon%27s_World) and became a sci-fi trope. The ansible can instantly send information across any distance, defying both time and space. Spanner isn’t the ansible. It can’t shrink space. But it works because those engineers found a way to harness time.

No one else has ever built a system like this. No one else has taken hold of time in the same way. And now Google is offering this technology to the rest of the world as [a cloud computing service](https://www.wired.com/2014/03/urs-google-story/).

Google believes this can provide some added leverage in its battle with Microsoft and Amazon for supremacy in the increasingly important cloud computing market, just because Spanner is unique. And some agree. “If they offer it, people will want it, and people will use it,” says Peter Bailis, an assistant professor of computer science at Stanford University who specializes in massively distributed software systems. But as others point out: Few businesses have the same needs as Google.

### Trusting Time

In the past, if you built a system that spanned hundreds of machines and multiple data centers, you followed an important rule: Don’t trust time. If a system involved communication between many machines in many different places, time would vary from machine to machine, just because time—precise time—is a hard thing to keep. Services like the [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) aimed to provide machines with a common reference point. But this worked only so well, mainly because networks are slow. It takes time to send the time.

For Google, this was a problem. If a database spanned multiple regions, it couldn’t ensure that transactions in one part of the world lined up with transactions in another. It couldn’t get a truly global picture of its operations. It couldn’t seamlessly replicate data cross regions or quickly retrieve replicated data when it was needed. So [Google’s top engineers](https://www.wired.com/2012/08/google-as-xerox-parc/) found a way to trust time.

[**![wired_dropbox-s-big-play.jpg](../_resources/a98ee91419f84471e6d945e94b0cb9c7.jpg)  Related Video Game of Clouds: Dropbox Declares Independence From Amazon](https://www.wired.com/video/2016/03/dropbox-s-big-play/)

Part of the trick is that they equipped Google’s data centers with a series of [GPS receivers](https://en.wikipedia.org/wiki/Global_Positioning_System) and [atomic clocks](https://en.wikipedia.org/wiki/Atomic_clock). The GPS receivers, much like the one in your cell phone, grab the time from various satellites orbiting the globe, while the atomic clocks keep their own time. Then they shuttle their time readings to master servers in each data center. These masters constantly trade readings in an effort to settle on a common time.

A margin of error still exists, but thanks to so many readings, the masters can bootstrap a far more reliable timekeeping service. “This gives you faster-than-light coordination between two places,” says Peter Mattis, a former Google engineer who founded CockroachDB, a startup working to build an [open source version of Spanner](https://www.wired.com/2014/07/cockroachdb/).

Google calls this timekeeping technology TrueTime, and only Google has it. Drawing on a [celebrated research paper](https://research.google.com/archive/spanner.html) Google released in 2012, Mattis and CockroachDB have duplicated many other parts of Spanner—but not TrueTime. Google can pull this off only because of its massive global infrastructure.

### A Changing World

To be sure, a few others could build a similar service, namely Amazon and Microsoft. But they haven’t yet. With help from TrueTime, Spanner has provided Google with a competitive advantage in so many different markets. It underpins not only AdWords and Gmail but more than 2,000 other Google services, including Google Photos and the Google Play store. Google gained the ability to juggle online transactions at an unprecedented scale, and thanks to Spanner’s extreme form of data replication, it was able to keep its services up and running with unprecedented consistency.

Now Google wants a different kind of competitive advantage in the cloud computing market. It hopes to convince customers that Spanner provides an easier way of running a global business, a easier way of replicating their data across multiple regions and, thus, guard against outages. The rub is that few businesses are truly global. But Google is betting its new service will give customers the freedom to expand as time goes on. Among them is JDA, a company that helps businesses oversee their supply chains, which is now testing Spanner. “The volume of data—and velocity with which that data is coming at us—is amplifying significantly,” says JDA group vice president John Sarvari.

Spanner could also be useful in the financial markets, allowing big banks to more efficiently track and synchronize trades happening across the planet. And Google says it’s already in talks with large financial institutions about this kind of thing. Traditionally, many banks were wary of handling trades in the cloud for reasons of security and privacy. But those attitudes are softening. A few years ago, Spanner was something only Google needed. Now, Google is banking on change.

[Go Back to Top. Skip To: Start of Article.](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/#start-of-content)

- [#Amazon](https://www.wired.com/tag/amazon/)
- [#cloud](https://www.wired.com/tag/cloud-2/)
- [#databases](https://www.wired.com/tag/databases/)
- [#google](https://www.wired.com/tag/google/)
- [#microsoft](https://www.wired.com/tag/microsoft/)
- [#Spanner](https://www.wired.com/tag/spanner/)

[Skip Social. Skip to: Latest News.](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/#latest-news-list)

-

#### Share

- [**Share32016](https://www.facebook.com/sharer/sharer.php?t=Spanner%2C+the+Google+Database+That+Mastered+Time%2C+Is+Now+Open+to+Everyone&u=https%3A%2F%2Fwww.wired.com%2F2017%2F02%2Fspanner-google-database-harnessed-time-now-open-everyone%2F?mbid=social_fb_onsiteshare)
- [**Tweet](https://twitter.com/intent/tweet?text=No%20one%20else%20has%20ever%20built%20a%20system%20like%20this.&related=cademetz&url=https%3A%2F%2Fwww.wired.com%2F2017%2F02%2Fspanner-google-database-harnessed-time-now-open-everyone%2F?mbid=social_twitter_onsiteshare&via=WIRED)
- [**Comment54](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/#article-comments)
- [**Email](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/mailto:?subject=WIRED:%20Spanner,%20the%20Google%20Database%20That%20Mastered%20Time,%20Is%20Now%20Open%20to%20Everyone&body=Check%20out%20this%20great%20article%20I%20read%20on%20WIRED:%0D%0A%0D%0AAbout%20a%20decade%20ago,%20a%20handful%20of%20Google%27s%20most%20talented%20engineers%20started%20building%20a%20system%20that%20seems%20to%20defy%20logic.%0D%0A%0D%0Ahttps://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/?mbid=email_onsiteshare)

[Skip Social. Skip to: Latest News.](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/#latest-news-list)

-

#### Share

- [**Share32016](https://www.facebook.com/sharer/sharer.php?t=Spanner%2C+the+Google+Database+That+Mastered+Time%2C+Is+Now+Open+to+Everyone&u=https%3A%2F%2Fwww.wired.com%2F2017%2F02%2Fspanner-google-database-harnessed-time-now-open-everyone%2F?mbid=social_fb_onsiteshare)
- [**Tweet](https://twitter.com/intent/tweet?text=No%20one%20else%20has%20ever%20built%20a%20system%20like%20this.&related=cademetz&url=https%3A%2F%2Fwww.wired.com%2F2017%2F02%2Fspanner-google-database-harnessed-time-now-open-everyone%2F?mbid=social_twitter_onsiteshare&via=WIRED)
- [**Comment54](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/#article-comments)
- [**Email](https://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/mailto:?subject=WIRED:%20Spanner,%20the%20Google%20Database%20That%20Mastered%20Time,%20Is%20Now%20Open%20to%20Everyone&body=Check%20out%20this%20great%20article%20I%20read%20on%20WIRED:%0D%0A%0D%0AAbout%20a%20decade%20ago,%20a%20handful%20of%20Google%27s%20most%20talented%20engineers%20started%20building%20a%20system%20that%20seems%20to%20defy%20logic.%0D%0A%0D%0Ahttps://www.wired.com/2017/02/spanner-google-database-harnessed-time-now-open-everyone/?mbid=email_onsiteshare)