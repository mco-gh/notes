It's Time to Think Beyond Cloud Computing | Backchannel

![](../_resources/07b4c57bafb98eaa9e8e678d8bb08fd0.png)

**Fasten your harnesses**, because the era of cloud computing’s giant data centers is about to be rear-ended by the age of self-driving cars. Here’s the problem: When a self-driving car has to make snap decisions, it needs answers fast. Even slight delays in updating road and weather conditions could mean longer travel times or dangerous errors. But those smart vehicles of the near-future don’t quite have the huge computing power to process the data necessary to avoid collisions, chat with nearby vehicles about optimizing traffic flow, and find the best routes that avoid gridlocked or washed-out roads. The logical source of that power lies in the massive server farms where hundreds of thousands of processors can churn out solutions. But that won’t work if the vehicles have to wait the 100 milliseconds or so it usually takes for information to travel each way to and from distant data centers. Cars, after all, move fast.

![logo.png](../_resources/d4583cccd5f8670b32dd296ac224b87b.png)

[Jeremy Hsu](https://twitter.com/jeremyhsu) is a science and tech journalist based in New York.

———

[Sign up](https://www.wired.com/newsletter?name=backchannel) to get Backchannel's weekly newsletter.

That problem from the frontier of technology is why many [tech leaders](https://a16z.com/2016/12/16/the-end-of-cloud-computing/) foresee the need for a new “edge computing” network—one that turns the logic of today’s cloud inside out. Today the [$247 billion cloud computing industry](https://globenewswire.com/news-release/2017/07/28/1063840/0/en/The-Leading-Cloud-Providers-Continue-to-Run-Away-with-the-Market.html) funnels everything through massive centralized data centers operated by giants like Amazon, Microsoft, and Google. That’s been a smart model for scaling up web search and social networks, as well as streaming media to billions of users. But it’s not so smart for latency-intolerant applications like autonomous cars or mobile mixed reality.

“It’s a foregone conclusion that giant, centralized server farms that take up 19 city blocks of power are just not going to work everywhere,” says Zachary Smith, a double-bass player and Juilliard School graduate who is the CEO and cofounder of a New York City startup called Packet. Smith is among those who believe that the solution lies in seeding the landscape with smaller server outposts—those edge networks—that would widely distribute processing power in order to speed its results to client devices, like those cars, that can’t tolerate delay.

![](../_resources/176a2e8a63082e549cbf35b64af6cf46.png)

**Packet’s scattered micro datacenters** are nothing like the sprawling facilities operated by Amazon and Google, which can contain tens of thousands of servers and squat outside major cities in suburbs, small towns, or rural areas, thanks to their huge physical footprints and energy appetites. Packet’s centers often contain just a few server racks—but the company promises customers in major cities speedy access to raw computing power, with average delays of just 10 to 15 milliseconds (an improvement of roughly a factor of ten). That kind of speed is on the “must have” lists of companies and developers hoping to stream [virtual reality and augmented reality experiences to smartphones,](http://about.att.com/content/dam/innovationblogdocs/Enabling%20Mobile%20Augmented%20and%20Virtual%20Reality%20with%205G%20Networks.pdf) for example. Such experiences rely upon a neurological process—the vestibulo-ocular reflex—that coordinates eye and head movements. It occurs within seven milliseconds, and if your device takes 10 times that long to hear back from a server, forget about suspension of disbelief.

#### More From This Edition

- [     Roni Jacobson  This Big Beef Exposes The Ugly Underbelly of Vegan Vlogging](https://www.wired.com/story/this-big-beef-exposes-the-ugly-underbelly-of-vegan-vlogging/)
- [     Miranda Katz  Amazon's Turker Crowd Has Had Enough](https://www.wired.com/story/amazons-turker-crowd-has-had-enough/)
- [     Steven Levy  Facebook, Apple, and Google Will Hasten the Next Era of TV](https://www.wired.com/story/facebook-apple-and-google-will-hasten-the-next-era-of-tv/)
- [     Katie Orenstein  Letter Home from Camp Wolfram](https://www.wired.com/story/letter-home-from-camp-wolfram/)

Immersive experiences are just the start of this new kind of need for speed. Everywhere you look, our autonomously driving, drone-clogged, robot-operated future needs to shave more milliseconds off its network-roundtrip clock. For smart vehicles alone, Toyota noted that the amount of data flowing between vehicles and cloud computing services is estimated to [reach 10 exabytes per month by 2025](http://newsroom.toyota.co.jp/en/detail/18135029/).

Cloud computing giants haven’t ignored the lag problem. In May, Microsoft announced the testing of its new Azure IoT Edge service, intended to push some cloud computing functions onto developers’ own devices. Barely a month later, Amazon Web Services opened up general access to [AWS Greengrass](https://aws.amazon.com/greengrass/) software that similarly extends some cloud-style services to devices running on local networks. Still, these services require customers to operate hardware on their own. Customers who are used to handing that whole business off to a cloud provider may view that as a backwards step.

US telecom companies are also seeing their build-out of new [5G networks](https://www.wired.com/2016/08/the-next-generation-of-wireless-5g-is-all-hype/#.28rro7b9f)—which should eventually support faster mobile data speeds—as a chance to cut down on lag time. As the service providers expand their networks of cell towers and base stations, they could seize the opportunity to add server power to the new locations. In July, AT&T announced plans to build a mobile edge computing network based on 5G, with the goal of reaching “[single-digit millisecond latency](http://about.att.com/story/reinventing_the_cloud_through_edge_computing.html).” Theoretically, data would only need to travel a few miles between customers and the nearest cell tower or central office, instead of hundreds of miles to reach a cloud data center.

“Our network consists of over 5,000 central offices, over 65,000 cell towers, and even several hundred thousand distribution points beyond that, reaching into all the neighborhoods we serve,” says Andre Fuetsch, CTO at AT&T. “All of a sudden, all those physical locations become candidates for compute.”

ADVERTISING

[inRead invented by Teads](http://teads.tv/inread-outstream/)

AT&T claims it has a head start on rival telecoms because of its “network virtualization initiative,” which includes the software capability to automatically juggle workloads and make good use of idle resources in the mobile network, according to Fuetsch. It’s similar to how big data centers use virtualization to spread out a customer’s data processing workload across multiple computer servers.

Meanwhile, companies such as Packet might be able to piggyback their own machines onto the new facilities, too. ”I think we’re at this time where a huge amount of investment is going into mobile networks over the next two to three years,” Packet’s Smith says. “So it’s a good time to say ‘Why not tack on some compute?’” (Packet’s own funding comes in part from the giant Japanese telecom and internet conglomerate Softbank, which invested $9.4 million in 2016.) In July 2017, Packet [announced its expansion](https://www.packet.net/edge/) to Ashburn, Atlanta, Chicago, Dallas, Los Angeles, and Seattle, along with new international locations in Frankfurt, Toronto, Hong Kong, Singapore, and Sydney.

Packet is far from the only startup making claims on the edge. Austin-based Vapor IO has already begun building its own micro data centers alongside existing cell towers. In June, the startup announced its “[Project Volutus](https://www.vapor.io/project-volutus-official-release/)” initiative, which includes a partnership with Crown Castle, the largest US provider of shared wireless infrastructure (and a Vapor IO investor). That enables Vapor IO to take advantage of Crown Castle’s existing network of 40,000 cell towers and 60,000 miles of fiber optic lines in metropolitan areas. The startup has been developing automated software to remotely operate and monitor micro data centers to ensure that customers don’t experience interruptions in service if some computer servers go down, says Cole Crawford, Vapor IO’s founder and CEO.

![](../_resources/80c93684de18ba67f861c23b799d721f.png)

**Don’t look for the edge** to shut down all those data centers in Oregon, North Carolina, and other rural outposts: Our era’s digital cathedrals are not vanishing anytime soon. Edge computing’s vision of having “thousands of small, regional and micro-regional data centers that are integrated into the last mile networks” is actually a “natural extension of today’s centralized cloud,” Crawford says. In fact, the cloud computing industry has extended its tentacles toward the edge with content delivery networks such as Akamai, Cloudflare, and [Amazon CloudFront](https://aws.amazon.com/cloudfront/) that already use “edge locations” to speed up delivery of music and video streaming.

Nonetheless, the remote computing industry stands on the cusp of a “back to the future” moment, according to Peter Levine, general partner at the venture capital firm Andreessen Horowitz. In a 2016 [video presentation](https://a16z.com/2016/12/16/the-end-of-cloud-computing/), Levine highlighted how the pre-2000 internet once relied upon a decentralized network of PCs and client servers. Next, the centralized network of the modern cloud computing industry really took off, starting around 2005. Now, demand for edge computing is pushing development of decentralized networks once again (even as the public cloud computing industry’s growth is [expected](http://www.gartner.com/newsroom/id/3616417) to peak at 18 percent this year, before starting to taper off).

That kind of abstract shift is already showing up, unlocking experiences that could only exist with help from the edge. Hatch, a spinoff company from Angry Birds developer Rovio, has begun rolling out a subscription game streaming service that allows smartphone customers to instantly begin playing without waiting on downloads. The service offers low-latency multiplayer and social gaming features such as sharing gameplay via Twitch-style live-streaming. Hatch has been cagey about the technology it developed to slash the number of data-processing steps in streaming games, other than saying it [eliminates the need for video compression](https://venturebeat.com/2017/02/12/how-hatch-aims-to-transform-the-way-you-play-mobile-games/view-all/) and can do mobile game streaming at 60 frames per second. But when it came to figuring out how to transmit and receive all that data without latency wrecking the experience, Hatch teamed up with—guess who—Packet.

“We are one of the first consumer-facing use cases for edge computing,” says Juhani Honkala, founder and CEO of Hatch. “But I believe there will be other use cases that can benefit from low latency, such as AR/VR, self-driving cars, and robotics.”

Of course, most Hatch customers will not know or care about how those micro datacenters allow them to instantly play games with friends. The same blissful ignorance will likely surround most people who stream augmented-reality experiences on their smartphones while riding in self-driving cars 10 years from now. All of us will gradually come to expect new computer-driven experiences to be made available anywhere instantly—as if by magic. But in this case, magic is just another name for putting the right computer in the right place at the right time.

“There is so much more that people can do,” says Packet’s Smith, “than stare at their smartphones and wait for downloads to happen.” We want our computation *now*. And the edge is the way we’ll get it.

![](../_resources/67b798cf6ef87383d2d969d0c5d4b716.png)