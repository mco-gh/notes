CIX and the real history of the modern, commercial Internet

January 11, 2018
|

 By [Steven Vaughan-Nichols](https://www.hpe.com/us/en/insights/articles/the-real-history-of-the-modern-internet-1801.html#Bio)

# The real history of the modern Internet

 In 1989, the Internet was still largely used by researchers, academicians, and the military. By 1993, it was well on its way to being the Internet you know. Two developments made this happen: CIX, net neutrality's ancestor, and the web. Here's how it happened.

The transition from the Internet's 1960s ancestor, [ARPANET](https://www.livescience.com/20727-internet-history.html), to our Internet changed everything. Two developments made this happen. The first (and more obscure) event was the creation of the [Commercial Internet Exchange](http://www.emeraldinsight.com/doi/pdfplus/10.1108/eb047265) (CIX). The second change, which almost everyone knows, is the creation of the World Wide Web.

In 1989, you couldn't sell a cat on the Internet, never mind setting up an e-commerce site to sell books. Commercial enterprises were expressly forbidden from participating in any Internet activity.

Not that the activity was easy. If you wanted to work on the 'net, you used [character-based interfaces with arcane syntaxes](http://www.zdnet.com/article/before-the-web-the-internet-in-1991/) such as Telnet, FTP, Archie, and Gopher. An easy-to-use hypertext, graphical way to navigate was still years away. If you wanted to hang out, chat, or work online, you used [modem-driven online services](http://www.zdnet.com/article/before-the-web-online-services/) such as America Online (AOL), CompuServe, or GEnie.

### CIX and the single network

In the late 1980s, many TCP/IP networks joined together to form what we now refer to as “the Internet.” Besides ARPANET, these groups included the U.S. Department of Defense's [MILNET](http://searchnetworking.techtarget.com/definition/MILNET), academia's [CSNET](https://www.livinginternet.com/i/ii_csnet.htm), and the National Science Foundation's (NSF) research and educational network, [NSFNET](https://www.nsf.gov/news/special_reports/cyber/internet.jsp). At that point, the Internet was not for ordinary people or businesses. As users moved from the academic Internet into the "real" world—such as graduating from college and accepting their first jobs—they wanted Internet access.

That began to occur with the rise of commercial email systems. In 1989, the [Corporation for National Research Initiatives](https://www.cnri.reston.va.us/) (CNRI) developed an email gateway between NSFNET and the most popular business email system, [MCI Mail](https://fcw.com/articles/2007/02/26/remembering-mci-mail.aspx). The idea of emailing someone across computer networks exploded. (Initially, someone in Columbus, Ohio, drove magnetic tapes to and from CompuServe’s offices and a nearby university, taking “sneakernet” to an illogical extreme.) Soon, everyone was trying to connect their email systems to the Internet. They used both the eventual standard, the [RFC 822](https://www.ietf.org/rfc/rfc822.txt) user_name@domain.top-level-domain format we all use now, and a wild mix of other standards, such as [UUNET's Bang addressing](http://mm.iit.uni-miskolc.hu/Data/texts/NAG/subsection2_12_3_2.html) and X.400. But email was relatively simple.

More important, nobody could charge money for Internet access or allow any kind of commercial activities. The early Internet services dealt with the government, research institutions, or schools, not with individuals. The [Internet's acceptable use policies](https://w2.eff.org/Net_culture/Net_info/Technical/Policy/nsfnet.policy) forbade for-profit activities and "extensive use for private or personal business.”

[IBM](http://www-03.ibm.com/ibm/history/ibm100/us/en/icons/internetrise/breakthroughs/), [Merit Network](https://www.merit.edu/), and [MCI](http://www.mci.com/mcihome.jsp) provided business services over national and regional networks. To save money and expand their reach, in 1990 they formed the nonprofit [Advanced Network Services](http://anscorporate.com/) (ANS), which created the first commercial Internet backbone, [ANSNET](http://www.cs.sfu.ca/~tamaras/theInternetP2/ANSNET.html). This same wide-area network was also used by NSFNET, which needed more bandwidth. For the first time, that meant the corporate network and the older Internet were running on the same cables and routers.

ANSNET did more than increase the early Internet's backbone speed from T1's blazingly fast 1.544 megabits per second to T3's then-amazing 44.736 Mbps. In 1993, the NSF also agreed to let the trio of pioneering Internet companies form [ANS CO+RE Systems](https://www.nsf.gov/pubs/stis1993/oig9301/oig9301.txt), a for-profit corporation that sold corporate Internet access—as long as they didn't use it for advertising. Little did they know what was to come!

This agreement opened Pandora's box. Now, everyone wanted to know how to pay for the rapidly expanding network traffic, as data jumped from business to nonprofit networks and back again. To hash out these issues, a public mailing list, com-priv, was set up on an early Internet service provider, [PSI Network](http://www.psi-net.com/) (PSINet). From these conversations, three ISPs that were not part of ANSNET ([CERFNET](http://www.cerfnet.com/), PSINet, and [UUNET](https://www.americaninno.com/dc/uunet-mafia-early-employees-where-they-are-now/)), formed their own network of networks: the Commercial Internet Exchange (CIX).

Physically, at first, [CIX consisted of a single router](https://books.google.com/books?id=a3wkCQAAQBAJ&pg=PA80&lpg=PA80&dq=CIX+router+timeline&source=bl&ots=1GU9qizKJp&sig=qPuVP7Ir71gvqsfqNYBICsq0sV4&hl=en&sa=X&ved=0ahUKEwjqgYWJlfvXAhUK12MKHSV8DyQQ6AEINjAB%23v=onepage&q=CIX%20router%20timeline&f=false) that connected their three networks. Doesn't sound very grand, does it? Yet, according to Frank Dzubeck, president of Communications Network Architects, a Washington, D.C., consulting firm, this was the creation of the "[backbone of the Internet.](http://www.nytimes.com/2003/12/12/business/john-sidgmore-52-dies-headed-worldcom.html)"

That’s because so many other ISPs joined them. In no small part, this was because all the CIX companies agreed to charge each other a flat fee for sharing their network traffic, instead of charging a fee based on how much data was carried.

That was [the real beginning of net neutrality](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=388863), although Tim Wu wouldn't coin the phrase until 2003.

However, one ISP, ANS, wouldn't agree to peer—that is, to check traffic with CIX in a net revenue-neutral way. This made it impossible for some groups on one "side" of the Internet to connect with the others.

This troublesome situation continued until 1992, when Mitch Kapor, founder of Lotus Development and its killer-app Lotus 1-2-3 spreadsheet, became chairman of CIX. Kapor got the two sides to agree to a "great compromise." In the agreement, ANS and CIX [agreed to share traffic across each other's networks](https://w2.eff.org/effector/effect02.10). As Kapor said at the time, "In taking this significant step, we enable greater freedom from content restrictions on the Internet."

With CIX, commerce immediately started flooding the web. And it won't surprise you to know that spam was there from the start. While unsolicited commercial messages began even earlier, in 1994 a pair of Phoenix attorneys launched the first major commercial spam campaign about a Green Card Lottery.

Emerging technologies are changing our future. A new world is coming.

[Get the Technology.nxt Report](https://www.hpe.com/h20195/V2/GetDocument.aspx?docname=4AA6-7154ENW&jumpid=in_insights~510287587~technologynxt~sjvncix)

It wasn't until the web came along that e-commerce really started to gain traction. CIX laid the foundation for both great failures, like Pets.com, and great successes, such as Amazon.com.

CIX transformed the collective networks into [the Internet you know today](https://www.hpe.com/us/en/insights/articles/net-neutrality-repeal-what-does-that-mean-for-it-networks-the-cloud-and-the-iot-1710.html): a network in which you can go to any website in the world without worrying about the underlying network.

### The spinnerets of the web

That's a good thing because while ANS and CIX were working out the network and business kinks to unite the Internet and open it to anyone, [Tim Berners-Lee](https://www.w3.org/History/1989/proposal.html)[came up with the idea of the web](https://www.w3.org/History/1989/proposal.html), an Internet-based hypertext system.

It wasn't a new idea. Credit goes to Vannevar Bush in his July 1945 article, "[As We May Think](http://www.ps.uni-saarland.de/~duchier/pub/vbush/vbush.txt)." [Ted Nelson's 1960 Xanadu hypertext vision](http://www.xanadu.com/) also pointed toward the web. And, ironically, Apple could have been much bigger than it already is had it simply made the [Apple HyperCard](http://www.zdnet.com/blog/government/apples-lost-decade-hypercard-and-what-might-not-have-been-if-apple-then-was-like-apple-is-today/10185) network-aware.

Be that as it may, Berners-Lee is the individual who took the hypertext idea and turned it into the web reality. He did it not to share LOLCats images (however good an idea that might have been), but to help researchers share ideas at CERN, the European Particle Physics Laboratory.

Berners-Lee used [NeXT](http://www.zdnet.com/blog/open-source/between-apples-steve-jobs-next-years/9693), the BSD Unix-based computers that are the modern-day Mac's most direct ancestor, to create the first web server: [info.cern.ch](http://info.cern.ch/). With the help of Nicola Pellow, a visiting graduate student who created the first web browser, the World Wide Web was off to an inauspicious start in 1991 with the "publishing" of the CERN telephone directory.

It did not make a great first impression. Adoption was slow. It wasn't until 1993 that I wrote the first mass-market [review of the WEB.](http://practical-tech.com/network/wais-and-web-the-future-of-internet-data-searching/49/)

The web would have taken off without my help. With CIX and ANS making peace, ISPs sprang up throughout the world, offering Internet access at the unheard speed of 28.8 kilobits per second. The only thing needed now was access to [an easy-to-use program that would let users search](https://www.hpe.com/us/en/insights/articles/how-search-worked-before-google-1703.html) and play and work with what they found on the Internet.

Enter the graphic web browser.

The first popular graphical web browser was from the National Center for Supercomputing Applications at the University of Illinois at Urbana-Champaign. [Mosaic](http://www.ncsa.illinois.edu/Projects/mosaic.html), created by Marc Andreessen and Eric Bina, wasn't the first graphical web browser. [ViolaWWW](http://www.viola.org/), a Unix browser, takes that honor, and [Cello](http://www.favbrowser.com/cello-first-windows-web-browser) was the first Windows graphical web browser. What Mosaic had going for it was [it let you see images within pages](http://history-computer.com/Internet/Conquering/Mosaic.html). Earlier browsers could only show images as separate files. It was no contest: Mosaic would dominate the first browser war.

It wasn't easy for most people to use the Internet. Windows, the most popular desktop operating system, didn't natively support TCP/IP until Windows 95 appeared. If you wanted TCP/IP on Windows before then, you had to use the notoriously difficult [Trumpet Winsock](http://www.trumpet.com.au/) program. ([OS/2 had its own web browser built in](http://www.os2museum.com/wp/os2-history/os2-2-0/), which at the time was a real bragging point.)

Still, people loved the idea of the Internet. But none of that—not Facebook, Twitter, Internet memes, Netflix, or World of Warcraft—would exist if it hadn't been for CIX and the web.

CIX made the Internet open, available, and affordable for anyone. The web made the Internet's resources so easy to use that my 2-year-old grandson can play with it.

**Related link:**

[Burgers and the Evolution of Modern Business Intelligence](https://community.hpe.com/t5/Around-the-Storage-Block/Burgers-and-the-Evolution-of-Modern-Business-Intelligence/ba-p/6950434#.WyMWO6dKjIU)

This article/content was written by the individual writer identified and does not necessarily reflect the view of Hewlett Packard Enterprise Company.