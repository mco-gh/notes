Buying an IBM Mainframe

### Buying an IBM Mainframe

[May 18, 2019](https://blog.mainframe.dev/2019/05/buying-ibm-mainframe.html)

I bought an IBM mainframe for personal use. I am doing this for learning and figuring out how it works. If you are curious about what goes into this process, I hope this post will interest you.

I am not the first one by far to do something like this. There are some people on the internet that I know have their own personal mainframes, and I have drawn inspiration from each and every one of them. You should follow them if you are interested in these things:

- [@connorkrukosky](https://twitter.com/connorkrukosky)
- [@sebastian_wind](https://twitter.com/sebastian_wind)
- [@faultywarrior](https://twitter.com/faultywarrior)
- [@kevinbowling1](https://twitter.com/kevinbowling1)

This post is about buying an IBM z114 mainframe (picture 1) but should translate well to any of the IBM mainframes from z9 to z14.

|     |
| --- |
| [![img195.jpg](../_resources/e67f9560e8a8791d2b03f92a37df8d9f.jpg)](https://4.bp.blogspot.com/-5PsYByeA81o/XODd2rj-uwI/AAAAAAAAa-s/h097uWDqDjQpoVoJW7l_jUXJlhXYvul_gCLcBGAs/s1600/img195.jpg) |
| *Picture 1: An IBM z114 mainframe in all its glory<br>Source: IBM* |

##

What to expect of the process

Buying a mainframe takes time. I never spent so much time on a purchase before. In fact - I purchased my first apartment with probably less planning and research. Compared to buying an apartment you have no guard rails. You are left to your own devices to ensure the state of whatever thing you are buying as it likely is sold as-is. Unless you are buying refurbished the seller will likely have no idea of how to verify the item and might even lack the equipment to power it on.

You might end up having to read up on what items are supposed to be in the frame of your mainframe and request heaps of pictures of parts in order to verify the exact configuration. That was the case for me, which ended up being loads of fun - but something I had not expected when starting the search.

## Important items to investigate

There are some crucial facts you will want to verify in order to ensure that 1) you are not buying a bricked mainframe 2) the mainframe will fit the purpose.

### What model is it?

This should hopefully be pretty self-explanatory but you should verify the claimed model. My mainframe is 2818-M05 which is one CPC drawer, the M10 has two. Easy enough to spot in a picture.

### Are the Support Elements (SE) present? Are the credentials known?

The latest IBM mainframe (z14) comes with SEs that are 1U servers, but anything older has SEs that come as laptops fixed to the frame. The importance of these laptops cannot be understated. **If you do not have these laptops with the original software on them the mainframe is bricked**.

The important thing with the Support Elements is that they contain the license for running the mainframe. When a customer buys the mainframe from IBM they put a lot more hardware in the frame than the customer bought, generally called "Plan Ahead". The licenses installed in the SE ensures that the customer only has access to what they have paid for. This means no SE = no mainframe. This is also called LICCC (LICense Control Code).

Likewise, if you cannot login to the SE you cannot use the mainframe. IBM is rumored to have services to password reset the SE but I would not want to depend on that fact. On the other hand, anything can be hacked with local access to it so if you are up for a (bigger) challenge it should be possible and might even get you a discount on the mainframe. Luckily it seems common people are running with the default passwords so asking the seller to verify the login credentials of the ACSADMIN and SYSPROG user should be good enough.

### Is there a Hardware Management Console (HMC) included?

The Hardware Management Console is mostly to connect many mainframes into what is called an Ensemble, which if you're reading this is probably not something you will ever do with your mainframe, but it does have some other neat features like being able to be accessed from a browser remotely.

You do not need an HMC if you only wish to operate the mainframe when locally present. Otherwise getting an HMC might be a good idea. Sadly it requires Java in the z114 version but that is a price you have to pay. Maybe someday somebody writes a replacement for hobbyists to run without the need to use Java.

You can buy an HMC separately quite easily as long as you have the drivers needed. My z114 came with a 93G driver installation DVD to install HMCs with. I have been told it is important that the driver version of the HMC is the same as the mainframe. I have no idea what happens if it is not.

### What optics are in the FICON/OSA cards?

|     |
| --- |
| [![resize.jpeg](../_resources/f2696efd03f8ba8f64caac7c2a0279d4.jpg)](https://2.bp.blogspot.com/-YFG_sp5JSMQ/XODblf4w_5I/AAAAAAAAa-g/qtDHX6n8gM0K6ZV1O8S_vr-ZtOesCMQwgCLcBGAs/s1600/resize.jpeg) |
| *Picture 2: OSA card with CCIN 57E7*<br>*Photo by Vibrant Technologies* |

You will want to connect your mainframe to a bunch of various equipment. For that you need to figure out what optics are present in your mainframe.

If you look at the OSA card in picture 2 you can see it says 57E7 at the right side, that is called a Custom Card Identification Number (CCIN). With the CCIN in hand one can use the handy reference table called "IBM System z IO Feature Reference Table" to translate this to a product name. In the case for 57E7 we learn that it is a "OSA-Express4S GbE SX (PCIe)" with 2 ports using multi-mode (MM) and LC connectors.

### How much storage (memory)?

*Note: In the mainframe world what is usually referred to as memory in the PC world is called storage for historical reasons.*

*
*

|     |
| --- |
| [![memory.jpeg](../_resources/663b7b2194d21267d067289c739b3c95.jpg)](https://2.bp.blogspot.com/-Ql4tZOni0pY/XODn6jlnB3I/AAAAAAAAa_A/Ujl4XU6FsDkt9ZabdW1RoZ29E-n2HKHfwCLcBGAs/s1600/memory.jpeg) |
| *Picture 3: 4 GB DIMM module<br>Source: Vibrant Technologies* |

In my case photos from inside the CPC drawer showed 10x 45D8410 modules (picture 3). After some internet searching one can figure out that this is the feature 1605 for 4 GB RAM sticks and it had 10 of them - 40 GB raw, or 24 GB usable after accounting for overhead and redundancies (see *Table 2-4 z114 memory offerings, z114 Technical Guide*).

### What CPU (CP) capacity, configuration, and other features?

As mentioned above in the section about Support Elements, the IBM mainframes come with more physical capacity than probably is licensed so figuring out what capacity is licensed is in your interest. The 2818-M05 model is measured from A01 to Z05 where A-Z is the speed rating of the CPs and the number afterwards is the number of activated cores. Z05 being the fastest, A01 being the slowest. This number is a big deal as Z05 provides 3139 MIPS while A01 only provides 26 - i.e. less than 1% of the full capacity!

Figuring this out can be hard unless the seller can power on the machine and logon into the SE and check. If you are lucky there are some printed documentation for the mainframe that tells you at least what it used to have, even though it might have been upgraded (maybe even downgraded to reduce software licensing costs?) in the time since.

IBM can also check what the latest report they have on file says about the configured capacity, but that of course requires you to have a contact with IBM in place.

In addition to this the mainframe will also have a certain number IFL, ICF, zAAP, and/or zIIF cores licensed as well as a myriad of other features which may be of interest to know about. This again most likely requires logging in to the SE to check what those are.

### What is the shipping going to cost?

The 2818-M05 weighs at least 700 kg and is the size of a full ordinary server rack. Shipping is going to be a significant part of the purchase unless you are able to handle it yourself. I was quoted $8,000 for shipping between the US and Europe, and $3,500 inside Europe.

## Fun facts about power

A good thing to know is that the power supplies in these machines do not care that much about the incoming voltage. If you look at the PSU and read the z114 Physical Planning Manual (IMPP, GC28-6907-00) one can deduce that the mainframe is willing to accept practically any AC/DC between 200V-600V.

There is also a significant difference in power usage if you have Balanced versus Unbalanced Power. You can figure out if you have this by looking at pictures of how many Bulk Power Regulators (BPR) there are. If you only have one you have unbalanced single phase power. If you have all three, you have balanced power as far as I know. If you have two I assume you have unbalanced two-phased power. Balanced power does sound like a good thing, but if you only care about power consumption it adds something like 500 W to the power consumption according to IBM.

IBM has a nice power planner utility available for its mainframes, but it requires you to register and get approved for access to their [Resource Link](https://www-01.ibm.com/servers/resourcelink/svc03100.nsf?OpenDatabase) knowledge base.

This particular unit is configured with a single BPR, one I/O cage and one PCIe cage. The PCIe cage contains the FICON interfaces, and Gigabit Ethernet cards while the I/O cage contains only ESCON and some additional Gigabit Ethernet. ESCON is the predecessor to FICON and as I have no plans of running it I plan to disconnect the I/O cage, saving 700 W in the process.

My estimate is that the continuous consumption will be 1.7 kW. Pretty comfortable, and well within specification for attaching a 16A C20 connector straight to the mainframe.

|     |
| --- |
| [![cable.png](../_resources/0834b0bfbdf339a72a211e705eae409a.png)](https://4.bp.blogspot.com/-edPEEnxILA4/XODm7PK3eEI/AAAAAAAAa-4/9nc3cgJtk6cquwGPi8E7_7bnnlZMXHrRACLcBGAs/s1600/cable.png) |
| *Picture 4: Power cable 41U0108<br>Source: Allegro* |

I found a power cable used for z114 with bare wires (picture 4) which I will attach a C20 connector on. This should allow running the z114 without any issues more or less anywhere with a 16A outlet.

## Sourcing items

Odds are that you need some extra equipment like an storage array or maybe an HMC.

Items generally have three numbers associated with them. The Part Number (P/N), the Customer Card Identification Numbers (CCIN), and the Feature Code (FC). Not all items have all three, for example port fillers may only have a part number and devices that are required in the base version of the unit may not have a feature code. If an item has a feature code I assume it is likely that you will need to have that feature activated in your LICCC for the item to work. However, there are exceptions: mainframe memory banks on the z114 are not enforced - only the resulting capacity is capped if it is above the licensed maximum. The z114 System Overview documentation states:

> open-quote> Larger capacity cards may be used for repair actions and manufacturing substitution. LICCC will dial down to ordered size.> close-quote

The z114 Technical Guide also says:

> open-quote> Each DIMM has a size of 4 GB, 8 GB, or 16 GB, and there is no mixing of DIMM sizes on a processor drawer.> close-quote

This means that there are some leeway for some aspects. Be careful before you know what features you have and try to make an informed decision about what the risks are that the item you are thinking of purchasing will not work in the mainframe.

To find what items you can purchase one good source is the mainframe's part catalog. For z114 this is GC28-6908-00. It contains breakdowns of what optional features exist, how they are mounted, and where they would be present if they are already available. This makes it possible to determine if the feature is already present based on pictures. Granted, the document is far from rich in detail but it helped me loads to understand what different parts go where and how I would go about to e.g. source the battery backup feature if I so wanted.

When you have found an item you wish to purchase your best bet is eBay, AliExpress, or even Taobao. Refurbished sellers work as well but they of course charge premiums. Taobao has some otherwise hard to find parts. d-parts.ru and allegro.pl are two other sites that have some part numbers that you might need - I only ended up buying from the latter so I cannot say anything about the former.

## Disk storage

If all you want to run is zLinux and z/VM then you should be fine with a normal Fiber Channel SAN running FCP and SCSI. In IBM mainframe world these are called FB-512 or 9336 type Direct-Access Storage Device (DASD). However, z/OS does not work on these type of DASDs so if you want a mainframe capable of running z/OS you need what is called ECKD based storage. ECKD uses channels which are only available over FICON.

As one would expect for something that is mainframe specific, FICON storage with ECKD support is expensive. I found one provider that quoted me a bit north of $30,000 for their smallest entry-level unit, while I am being told that the larger vendors start at $100,000+.

There is a saving grace however. There are plenty of IBM DS6800 arrays floating around in the second hand market at $6,000 - $8,000. If you are a bit more adventurous there are even more in China on Taobao for $1,000 - $2,000 without disks, and $15 per disk. I managed to buy one on AliExpress for a significant discount as the seller did not have the equipment to ensure the system was working and offered me the item for $1,800 + shipping. Expensive, yes, but DASD is probably the most important accessory to your mainframe so it makes sense to splurge a little.

## Tape library

Commonly IBM mainframes use formats such as 3480, 3490, or 3590 devices for tape. A lot of mainframe concepts still revolve around tapes and as such it may be an interesting addition to your mainframe.

The industry appears to have embraced the cheap and comparatively fast disks as a contender to tapes in modern times, which has spawned a whole industry of virtual tape libraries. These can be found on the previously mentioned places on the internet. I got my hands on parts of an EMC DLm2000 environment that I am hoping to pick apart as well as some extra FICON cards. This particular solution works using NFS servers to store the tapes, so I am hopeful I can integrate it with FUSE and store my tapes directly on Google Cloud Storage or equivalent.

## Future ideas

The itch that itches the most is the fact that hobbyists need to pay a lot for FICON accessories like DASD. I understand that in the mainframe production environment DASD is extremely important and reliability and performance is key - but that is not the case for hobbyists.

Going forward one of the projects I am most excited about is to use the extra FICON cards from the tape library to build a Linux-based and open-source ECKD DASD array. I have spent some time looking at how FICON works and it is very similar to Fibre Channel, so similar in fact that I think it might be possible to use normal FC HBAs to interface with FICON. It will not be hardware accelerated but for hobbyists it should be more than enough. Expect more blog posts about FICON and running channel controllers in Linux going forward.

If the mainframe arrives safely and even powers on that is ;-).

|     |
| --- |
| [![60428185_286831035539315_7089869078633906176_n.jpg](../_resources/1b8c70c522f55ab5e1722853d3a878d5.jpg)](https://1.bp.blogspot.com/-NBTtHfF-xy0/XOEBVW0vuTI/AAAAAAAAa_M/S1TMKy0xvHcEn7MEs-qTpzuglqE-32hsQCLcBGAs/s1600/60428185_286831035539315_7089869078633906176_n.jpg) |
| *Picture 5: IBM z114 getting packed for transport* |

## Final Bill-of-Materials

This is what the purchase list contained in the end. I have removed some trivial details like LC-LC cables and power plugs from the otherwise complete list.

| Amount | Product | Price |
| --- | --- | --- |
| 1   | IBM 2818-M05 z114 | $12,000 |
| 1   | Datacenter Setup | $3,800 |
| 1   | IBM DS6800 | $2,710 |
| 2   | Brocade 5100 w/ FICON CUP | $1,750 |
| 1   | FICON Virtual Tape Library (DLm2000) | $1,315 |
| 2   | 41T8417 OSA-Express4S 10GbE LR (PCIe) | $640 |
| 1   | Arista DCS-7050S-52 | $529 |
| 1   | IBM System X3200 M3 (HMC) | $350 |
| 2   | Power cord | $220 |
| 24  | Brocade 8G FC SFP SM | $74 |
| 20  | Brocade 8G FC SFP MM | $58 |
| **Total** | $23,446 |