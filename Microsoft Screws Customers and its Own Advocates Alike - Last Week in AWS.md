Microsoft Screws Customers and its Own Advocates Alike - Last Week in AWS

- [Skip to primary navigation](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#genesis-nav-primary)
- [Skip to content](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#genesis-content)
- [Skip to primary sidebar](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#genesis-sidebar-primary)

 [![last-week-in-aws-logo.png](../_resources/cba35714e9cc5dd242b07fb47e047d14.png)](https://www.lastweekinaws.com/)

- [The Newsletter](https://www.lastweekinaws.com/newsletter)
- [The Blog](https://www.lastweekinaws.com/blog/)
- [The Podcast](https://www.screaminginthecloud.com/)
- [Products](https://www.lastweekinaws.com/products/)
- [Services](https://www.lastweekinaws.com/services/)
- [About](https://www.lastweekinaws.com/about/)
- [![Contact.png](../_resources/625b5fb613bda141303f268823d0aade.png)![platyprint-yellow.png](../_resources/acd518b245efed4a43e00138596dbded.png)](https://www.lastweekinaws.com/contact/)

##### The Blog

#  Microsoft Screws Customers and its Own Advocates Alike

 ![Calendar.png](../_resources/9275c9344c585dc6bd8b2a579799d07c.png)  08.13.2019

 ![overlay-white.png](../_resources/57fede0ad6a139a31551d3a5c70c0e3a.png)

![link-arrow-yellow.png](../_resources/f47643d31204cb7eb50237c38744b249.png)

[(L)](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#)[Share](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#)

Share on Facebook
![link-arrow.png](../_resources/86d646b488cdccfdd612ea5eaaddd039.png)

[(L)](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#)[Tweet](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#)

Tweet this
![linkedin-blue.png](../_resources/11ee3bc8181957651adec2464619dd51.png)

[(L)](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#)[Share](https://www.lastweekinaws.com/blog/microsoft-screws-customers-and-its-own-advocates-alike/#)

Share on LinkedIn

Today’s Microsoft is a brand-new company; the bad old days of Microsoft being an anti-competitive bully are dead and buried. After all, isn’t that why they spent $7.5 billion to [acquire GitHub](https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/), [released VS Code](https://techcrunch.com/2015/04/29/microsoft-shocks-the-world-with-visual-studio-code-a-free-code-editor-for-os-x-linux-and-windows/) (which remains one of the best cross-platform IDEs I’ve ever seen) for free, and hired [a hundred of the best people in our industry as advocates](https://developer.microsoft.com/en-us/advocates/index.html)?

They’ve turned the corner on their anticompetitive past; no longer are they bullies. It’s a kinder, friendlier Microsoft.

But then on Aug. 1, 2019, the Old Microsoft reared its ugly head.

The company made a move that left some of us wondering whether anything had really changed at all by announcing a licensing change that’s a clear shot at AWS’s dominance (which is fine!)—just at the expense of their customers (which is absolutely not fine!).

Now, I’m not suggesting that everything Microsoft has said for the past few years was a lie. The Ballmer-era folks for the worst of Microsoft’s tendencies are still there and apparently just flexed a bit while Satya Nadella was looking the other way. This announcement, combined with the great stuff they’re doing (some of which I mentioned above!), tells the tale of internal struggle.

# What exactly happened?

You can read the details of [their licensing changes](https://www.microsoft.com/en-us/licensing/news/updated-licensing-rights-for-dedicated-cloud) yourself if you’d like. But let me warn you: It’s dry and it’s not immediately clear what the hullabaloo is about.

Let me break it down for you in a way that a human being has a hope of understanding.

The short version: You’ll now potentially be taxed for running Windows Server on any cloud that isn’t Azure.

The longer version is complex, nuanced, and exceeds my attention span, so I point you to [The Register’s excellent summary](https://www.theregister.co.uk/2019/08/05/microsoft_licensing_windows_clouds/) instead. Pack a lunch.

To be clear, any licenses purchased before Oct. 1, 2019 aren’t subject to the new restrictions. But exactly how many folks are buying all the licenses they’ll ever need to the point they don’t need to purchase more ever again? No healthy company, that’s for certain.

# This is bad for customers

Surprise!

After Oct. 1, licenses you purchase for your Windows workloads become significantly more expensive to run in any cloud provider that isn’t Microsoft Azure. All of your budget planning, all of your resource forecasts? Throw them into the garbage and start over.

What can you do? You’re not likely to either migrate off of Windows or change cloud providers before Oct. 1. So if you’re like most customers, you’re probably going to take one on the chin. You might buy a pile of licenses before Oct. 1 which are subject to the old restrictions instead of the new ones. But that’s not exactly how most companies like to do procurement.

I’m sure you won’t remember this feeling when your next vendor selection project kicks off, right?

# This is bad for the cloud industry

I certainly don’t expect Microsoft to shed too many tears over this one, but this feels like Microsoft using its market dominance in one area (Windows Server licensing) to make life more difficult for its competitors in another market (cloud computing).

The problem Microsoft faces is that AWS built a cloud that’s smashing them in the market. [IDC states that almost twice as many Windows workloads run in AWS as do in Azure](https://d1.awsstatic.com/analyst-reports/IDC_Slide_WindowsonAWS_JM181015.pdf). Azure is [demonstrably less durable](https://www.geekwire.com/2019/microsoft-may-cloud-computing-azure-reliability-lagging-competition/) than other providers, yet that seems to not really affect market perception much.

To state it a lot more bluntly: Whenever Azure takes an outage, I don’t see a whole lot of websites dropping off of the internet. This implies that their growing userbase isn’t people migrating production workloads to Azure but rather people migrating old Sharepoint and Exchange servers. Think “traditional corporate IT.”

Rather than trying to win customers with a better product offering (which I want them to do—I don’t want to see an Amazonian monoculture any more than Microsoft does!), they’re trying to hamfistedly win business from their historical best customers by rolling out underhanded pricing changes that wreck those customers’ planned budgets. This results in customers making subpar choices for their workloads in service of a licensing model from yesteryear–and potentially dismissing public cloud entirely due to misplaced cost concerns.

# This is bad for Microsoft

When I reached out to my friends at Azure and asked them for off-the-record comments on this, the overwhelming response went something like this: “Wait, what are you talking about? We did *what* with licenses?! You’re kidding me. Let me get back to you.”

This brings me to a point that I haven’t seen anyone else articulate yet.

Microsoft is easily spending north of $20 million a year on its Azure Advocates program. These are people steeped in the industry—folks the rest of us admire and celebrate. These individuals have invested time, energy, and love in reassuring all of us that the Microsoft of old—the bully, the anticompetitive jerk, the Oracle you can’t avoid—was dead and gone, replaced by a new cuddlier, friendlier company.

I believed them. I still do.

What has me incensed is that this change suddenly turns those incredibly well-intentioned people into unknowing corporate propagandists. What are those of us who’ve believed their transformation narrative to think?

I hope and trust that this is an aberrant behavior that’ll quickly be rectified as leadership realizes that Microsoft’s actions have consequences, and that dumb moves like this can rapidly erode the delicate acceptance that Microsoft is increasingly finding among the developer community.

If not, I suppose Azure’s new logo could come to define how Microsoft was perceived in the past and will be perceived in the future: as an enormous A-hole.

![Azure.png](../_resources/1164cb1d38372eb1b8668d52cd93d538.png)

## Primary Sidebar

![corey-about-headshot.png](../_resources/edc2f18a380b2ecc1878cfda2b0c5493.png)

#### About the Author

Corey helps companies address their horrifying AWS bills by both reducing the dollars spent and helping  them understanding what they’re paying for.

![twitter-icon-blue.png](../_resources/dd4bd5e3aa19462f64f4fd30c1ad85d2.png)

#### Sign up for the Newsletter

Stay up to date on the latest AWS news, opinions, and tools, all lovingly sprinkled with a bit of snark.

- Email*

* * *

### You might also like

 [More From the Blog](https://www.lastweekinaws.com/blog/)

 [![83702763_l-350x200.jpg](../_resources/f45b4677c268fba7fe2c07f0808df4a9.jpg)](https://www.lastweekinaws.com/blog/why-i-turned-down-an-aws-job-offer/)

##   [Why I Turned Down an AWS Job Offer](https://www.lastweekinaws.com/blog/why-i-turned-down-an-aws-job-offer/)

 ![dot-divider-yellow.png](../_resources/dd4bd5e3aa19462f64f4fd30c1ad85d2.png)

I once turned down a job offer from AWS, who told me my reasoning was preposterous. Last week they did exactly what I was afraid of.

 [![facebook-icon-blue.png](../_resources/fdf37d5b1d3b413da79c68c694c027ce.png)Read More](https://www.lastweekinaws.com/blog/why-i-turned-down-an-aws-job-offer/)

 [![39892079_l-350x200.jpg](../_resources/75c452b77cfd2430f8824c37d167e33d.jpg)](https://www.lastweekinaws.com/blog/observerless-the-hottest-new-thing-in-monitoring-youre-already-doing/)

##   [Observerless: The hottest new thing in monitoring you’re already doing](https://www.lastweekinaws.com/blog/observerless-the-hottest-new-thing-in-monitoring-youre-already-doing/)

Settle the monitoring vs observability debate by adopting Observerless principles–it’s the the hottest new thing in monitoring you’re already doing.

 [Read More](https://www.lastweekinaws.com/blog/observerless-the-hottest-new-thing-in-monitoring-youre-already-doing/)

 [![billie-tableflip.png](../_resources/cb92ad747a27176848107badf42c87f3.png)](https://www.lastweekinaws.com/blog/capitalones-capitaltwo-day/)

##   [CapitalOne’s CapitalTwo Day](https://www.lastweekinaws.com/blog/capitalones-capitaltwo-day/)

CapitalOne’s data breach isn’t their fault, but they could have done more than they did to prevent it.

 [Read More](https://www.lastweekinaws.com/blog/capitalones-capitaltwo-day/)

 ![overlay-lightblue.png](../_resources/0ed178982299386cf0f84aa8d500964d.png)

 ![newsletter-icon.png](../_resources/09fdeed3b82b05ed5bc8559bd691dfc2.png)

### Get the Newsletter!

Stay up to date on the latest AWS news, opinions, and tools, all lovingly sprinkled with a bit of snark.

- ![newsletter-signup-shadow.png](../_resources/32ccc03253601484ea3a713d043cc203.png)Email*

We help companies fix their AWS bill by making it smaller and less horrifying.

 [**](https://twitter.com/QuinnyPig)  [**](https://linkedin.com/in/coquinn)  [**](https://www.lastweekinaws.com/feed/)

- [The Newsletter](https://www.lastweekinaws.com/newsletter/)
- [The Blog](https://www.lastweekinaws.com/blog/)
- [The Podcast](https://www.screaminginthecloud.com/)
- [Services](https://www.lastweekinaws.com/services/)
- [Products](https://www.lastweekinaws.com/products/)
- [Sponsorship](https://www.lastweekinaws.com/sponsorship/)
- [About Us](https://www.lastweekinaws.com/about/)
- [Contact](https://www.lastweekinaws.com/contact/)

![Platypus-footer.png](../_resources/acb0e0e6a10541f30ac7bb079e4c5b32.png)

© 2019 The Duckbill Group. All Rights Reserved. [Privacy Policy](https://www.lastweekinaws.com/privacy-policy/)  [Cookie Policy](https://www.lastweekinaws.com/cookie-policy/)