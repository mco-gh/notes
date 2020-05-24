Mapping the whole internet with Hilbert curves

# Mapping the whole internet with Hilbert curves

The internet is big. [Really big](http://www.quotationspage.com/quote/33085.html). You just won’t believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think the /22 you got as a [LIR](https://www.ripe.net/manage-ips-and-asns/resource-management/faq/independent-resources/def-terms/what-is-a-local-internet-registry-lir) was big, but that’s just peanuts to the internet.

Well, actually, it wasn’t in the long run, that’s why we need IPv6. But that is a different story.

The point is, IPv4 (the most common deployed version of the IP protocol) sets its address limits at 2³² addresses. This means you have roughly 4.2 billion IP addresses to work with, except you don’t really, because large sections are not usable:

| IP Range | Use |
| --- | --- |
| 0.0.0.0/8 | Local System |
| 10.0.0.0/8 | Local LAN |
| 127.0.0.0/8 | Loopback |
| 169.254.0.0/16 | “Link Local” |
| 172.16.0.0/12 | Local LAN |
| 224.0.0.0/4 | Multicast |
| 240.0.0.0/4 | “Future use” |

The blocks ( shown as [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) ) above already wipe out 588,316,672 addresses, or about 13% of all addresses.

However giving the remaining 3,706,650,624 addresses, When you consider it, isn’t that many and is perfectly within reach of sending a packet to *every single one*.

Now. This isn’t the first time someone has done this, the internet has a considerable amount of “background noise” (unsolicited packets) on it. Mostly created by systems looking for other systems to hack.

![](../_resources/e1cf9de6da930b88874efea6123caa22.png)

Here we can see that port 23 is far higher (on a logarithmic scale) than any other port, and that is port is for [telnet](https://en.wikipedia.org/wiki/Telnet), commonly used in insecure routers and other IoT devices.

With that known, I speeded ahead and send a ICMP ping to every host on the internet to see how much of the internet responds to a ping (and thus indicating there is a connected computer on the other side of it)

After around a day later, I had sent 3.7 billion packets and had a large text file. Now we just had to find a way to draw it!

## Introducing Hilbert curves

The problem with displaying IP addresses, is that they are a single dimensional, they only move up and down, however humans are not good at looking at a large amount of single dimensional points. So there has to be a way to fill a 2 dimensional space that can also help the structure of the graph stay in shape.

Luckily maths has our back again, with [space filling curves](https://en.wikipedia.org/wiki/Space-filling_curve)

![](../_resources/b9d7bc19b3fa3ca196ad08a5fa6e764e.png)

For me it didn’t make much sense until I numbered the nodes it was passing though.

![](../_resources/c21ab80f6cdfac7dd6c17e38704bcd5b.png)

It took me even longer for me to fully get all of this until I realised. You can still show this same animation being unraveled into a single dimension again:

![](../_resources/0c160786398987b8bd189c987052a67d.png)

Anyway, now that we know these graphs work, we can start applying them to IP addresses!

Thankfully [there are tools that can already produce these graphs](https://github.com/measurement-factory/ipv4-heatmap) in relation to IP addresses so it is just a case of loading that data in and producing the graph:

	cat ping.txt | pcregrep -o1 ': (\d+\.\d+\.\d+\.\d+)' | ./ipv4-heatmap -a ./labels/iana/iana-labels.txt -o out.png

This renders a hilbert curve with a color gradient showing how many systems are online in that /24

and so I present, The IPv4 Internet on 16th April 2018:

[![](../_resources/6b6601ed72c3e9a55c76df5151679df3.png)](https://benjojo.co.uk/internet-2018.png)

You can click on the image for a lossless and full resolution version, however do be warned that it’s 9MB.

The last public scan I know if was in 2012 and was done by the Carna botnet, using this data we can easily see some changes.

![](../_resources/86875da61d84bfa5f83eb88137312d24.png)

In 2012 [RIPE](https://ripe.net/) had not even touched the 185.0.0.0/8, it would later become the block they would use for the last allocations, and would only give out a /22 of IP space to every new member of RIPE. This makes 185.0.0.0/8 odd looking among the other blocks, and there are no mass allocations, and so the blocks looks very “spotty” compared to others.

RIPE is not the only one to have completely used up blocks in this time. Below we see 3 different RIRs consume their blocks in the space of 6 years.

![](../_resources/d3e0937f7539fc610ae5d960d5ad86b7.png)

On top of all of this, I also did a bonus scan of a few APNIC IP blocks every 30 mins for 24 hours. The data from that allows you to see the internet “breathe” as clients come online in the morning and offline at night:

![](../_resources/510ae4628b59c93144637584ce87fe61.png)

One of the more interesting finds in this gif was a what looks like a dynamic IP pool from a ISP, showing clients come online for a short amount of time, and then connecting and getting a new IP address (hence more the more active IP addresses are “moving” during the day)

![](../_resources/2fc4367a5d90eb4a506612152124d79b.png)

Oh and if you were wondering what IPv6 looks like in this form and how much we are using already:

![](../_resources/e6c51fd0ed32f9a53cb5913f374c2007.png)

And if you enjoyed this, you will be glad to know that I am going to be at [Recurse Center](https://recurse.com/) in NY for the next 9 weeks! Meaning you can follow my [Twitter](https://twitter.com/benjojo12) or [RSS](https://blog.benjojo.co.uk/rss.xml) to keep up with the other silly (or sometimes sensible) things I will do!