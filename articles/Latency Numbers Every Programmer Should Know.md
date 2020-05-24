Latency Numbers Every Programmer Should Know

Latency Numbers Every Programmer Should Know

 [Raw](https://gist.github.com/jboner/2841832/raw/055989fb2067047dcdd5d5fd09b8c0fd5b46054b/latency.txt)

       [**latency.txt**Permalink](https://gist.github.com/jboner/2841832#file-latency-txt)

|     |     |
| --- | --- |
| 1   | Latency Comparison Numbers |
| 2   | -------------------------- |
| 3   | L1 cache reference 0.5 ns |
| 4   | Branch mispredict 5 ns |
| 5   | L2 cache reference 7 ns 14x L1 cache |
| 6   | Mutex lock/unlock 25 ns |
| 7   | Main memory reference 100 ns 20x L2 cache, 200x L1 cache |
| 8   | Compress 1K bytes with Zippy 3,000 ns 3 us |
| 9   | Send 1K bytes over 1 Gbps network 10,000 ns 10 us |
| 10  | Read 4K randomly from SSD* 150,000 ns 150 us ~1GB/sec SSD |
| 11  | Read 1 MB sequentially from memory 250,000 ns 250 us |
| 12  | Round trip within same datacenter 500,000 ns 500 us |
| 13  | Read 1 MB sequentially from SSD* 1,000,000 ns 1,000 us 1 ms ~1GB/sec SSD, 4X memory |
| 14  | Disk seek 10,000,000 ns 10,000 us 10 ms 20x datacenter roundtrip |
| 15  | Read 1 MB sequentially from disk 20,000,000 ns 20,000 us 20 ms 80x memory, 20X SSD |
| 16  | Send packet CA->Netherlands->CA 150,000,000 ns 150,000 us 150 ms |
| 17  |     |
| 18  | Notes |
| 19  | ----- |
| 20  | 1 ns = 10^-9 seconds |
| 21  | 1 us = 10^-6 seconds = 1,000 ns |
| 22  | 1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns |
| 23  |     |
| 24  | Credit |
| 25  | ------ |
| 26  | By Jeff Dean: http://research.google.com/people/jeff/ |
| 27  | Originally by Peter Norvig: http://norvig.com/21-days.html#answers |
| 28  |     |
| 29  | Contributions |
| 30  | ------------- |
| 31  | Some updates from: https://gist.github.com/2843375 |
| 32  | 'Humanized' comparison: https://gist.github.com/2843375 |
| 33  | Visual comparison chart: http://i.imgur.com/k0t1e.png |
| 34  | Animated presentation: http://prezi.com/pdkvgys-r0y6/latency-numbers-for-programmers-web-development/latency.txt |

 [![@dominictarr](../_resources/ff7983ea84ef11c9c5590f5589d459ff.jpg)](https://gist.github.com/dominictarr)

 **  [dominictarr](https://gist.github.com/dominictarr)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337081)

|     |
| --- |
| need a solar system type visualization for this, so we can really appreciate the change of scale. |

 [![@jboner](../_resources/b5ffa1cea9e3c12395a394f88d14e396.jpg)](https://gist.github.com/jboner)

  Owner This user is the owner of the gist.

 **  [jboner](https://gist.github.com/jboner)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337084)

|     |
| --- |
| I agree, would be fun to see. :-) |

 [![@pmanvi](../_resources/f49df0ce992bcd754a93bf6d65965999.png)](https://gist.github.com/pmanvi)

 **  [pmanvi](https://gist.github.com/pmanvi)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337087)

|     |
| --- |
| useful information & thanks |

 [![@dakull](../_resources/8e649181b445bb43d73324d401f2d640.jpg)](https://gist.github.com/dakull)

 **  [dakull](https://gist.github.com/dakull)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337118)

|     |
| --- |
| Looks nice kudos !<br>One comment about the Branch mispredict: if the cpu architecture is based on P4 or Bulldozer that would result in 20-30+ cycles on a mispredict that would translate to a much bigger number (and they do mispredict) :)<br>For SSD's would be something like:<br>Disk seek: 100 000 ns |

 [![@preinheimer](../_resources/5340d27d34a6a0181e3ec6aca77c3404.png)](https://gist.github.com/preinheimer)

 **  [preinheimer](https://gist.github.com/preinheimer)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337174)

|     |
| --- |
| Latency numbers between large cities: https://wondernetwork.com/pings/ |

 [![@alexismo](../_resources/4fe378f21227cd36297ccec10d4089e2.jpg)](https://gist.github.com/alexismo)

 **  [alexismo](https://gist.github.com/alexismo)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337180)

|     |
| --- |
| [@preinheimer](https://github.com/preinheimer) Asia & Australasia have it bad. |

 [![@gandalfar](../_resources/7595dd79683317392734705a35027e80.jpg)](https://gist.github.com/gandalfar)

 **  [gandalfar](https://gist.github.com/gandalfar)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337184)

|     |
| --- |
| From the same author: http://videolectures.net/wsdm09_dean_cblirs/ |

 [![@Eronarn](../_resources/a45b6d3759cea203124618469a3d6bfe.jpg)](https://gist.github.com/Eronarn)

 **  [Eronarn](https://gist.github.com/Eronarn)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337196)

|     |
| --- |
| "Latency numbers every programmer should know" - yet naturally, it has no information about humans!<br>http://biae.clemson.edu/bpc/bp/lab/110/reaction.htm |

 [![@hellerbarde](../_resources/fa8f9101cb5cc16cb243f973c553d6ec.png)](https://gist.github.com/hellerbarde)

 **  [hellerbarde](https://gist.github.com/hellerbarde)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337206)

|     |
| --- |
| maybe you want to incorporate some of this: https://gist.github.com/2843375 |

 [![@christopherscott](../_resources/0578862bdf9181de800bf334ff779151.png)](https://gist.github.com/christopherscott)

 **  [christopherscott](https://gist.github.com/christopherscott)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337208)

|     |
| --- |
| Curious to see numbers for SSD read time |

 [![@klochner](../_resources/f6cd7e0b7ab76b1bca367c382c8479c3.jpg)](https://gist.github.com/klochner)

 **  [klochner](https://gist.github.com/klochner)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337258)

|     |
| --- |
| I think the reference you want to cite is here: http://norvig.com/21-days.html#answers |

 [![@lucasces](../_resources/4c338732644ecddbb341441f5493c37c.png)](https://gist.github.com/lucasces)

 **  [lucasces](https://gist.github.com/lucasces)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337260)

|     |
| --- |
| This remind me of this Grace Hopper's video about Nanoseconds. Really worthy.<br>http://www.youtube.com/watch?v=JEpsKnWZrJ8 |

 [![@mikea](../_resources/fbd95d24510fd92b6dbd6d6f74c7a71f.jpg)](https://gist.github.com/mikea)

 **  [mikea](https://gist.github.com/mikea)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337297)

|     |
| --- |
| I find comparisons much more useful than raw numbers: https://gist.github.com/2844130 |

 [![@briangordon](../_resources/2f1148619dc825e73923d4d15ae28a0c.jpg)](https://gist.github.com/briangordon)

 **  [briangordon](https://gist.github.com/briangordon)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337374)

|     |
| --- |
| I'm surprised that mechanical disk reads are only 80x the speed of main memory reads. |

 [![@dakull](../_resources/8e649181b445bb43d73324d401f2d640.jpg)](https://gist.github.com/dakull)

 **  [dakull](https://gist.github.com/dakull)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337375)

|     |
| --- |
| my version : https://gist.github.com/2842457 includes SSD number, would love some more |

 [![@newphoenix](../_resources/1da4287a1c3c2a20be17bdbcbee3dbef.png)](https://gist.github.com/newphoenix)

 **  [newphoenix](https://gist.github.com/newphoenix)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337379)

|     |
| --- |
| Does L1 and L2 cache latency depends on processor type? and what about L3 cache. |

 [![@dakull](../_resources/8e649181b445bb43d73324d401f2d640.jpg)](https://gist.github.com/dakull)

 **  [dakull](https://gist.github.com/dakull)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337387)

|     |
| --- |
| Ofc it does ... those are averages I think. |

 [![@cayblood](../_resources/feaf1c6a04fbea061b0cb40a99dfc896.jpg)](https://gist.github.com/cayblood)

 **  [cayblood](https://gist.github.com/cayblood)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337493)

|     |
| --- |
| Would be nice to right-align the numbers so people can more easily compare orders of magnitude. |

 [![@jboner](../_resources/b5ffa1cea9e3c12395a394f88d14e396.jpg)](https://gist.github.com/jboner)

  Owner This user is the owner of the gist.

 **  [jboner](https://gist.github.com/jboner)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337499)

|     |
| --- |
| Good idea. Fixed. |

 [![@jhclark](../_resources/3b60d019367996dd1040313b0e5fa12d.jpg)](https://gist.github.com/jhclark)

 **  [jhclark](https://gist.github.com/jhclark)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337539)

|     |
| --- |
| And expanded even a bit more: https://gist.github.com/2845836 (SSD numbers, relative comparisons, more links) |

 [![@nicowilliams](../_resources/10178f99360413c36d5fb76baad2b292.png)](https://gist.github.com/nicowilliams)

 **  [nicowilliams](https://gist.github.com/nicowilliams)  ** commented [on May 31, 2012](https://gist.github.com/jboner/2841832#gistcomment-337551)

|     |
| --- |
| TLB misses would be nice to list too, so people see the value of large pages...<br>Context switches (for various OSes), ...<br>Also, regarding packet sends, that must be latency from send initiation to send completion -- I assume.<br>If you're going to list mutex lock/unlock, how about memory barriers?<br>Thanks! This is quite useful, particularly for flogging at others. |

 [![@lry](../_resources/b9a3246d59f17e5e5a82c55509416b6b.png)](https://gist.github.com/lry)

 **  [lry](https://gist.github.com/lry)  ** commented [on Jun 1, 2012](https://gist.github.com/jboner/2841832#gistcomment-337924)

|     |
| --- |
| Quick pie chart of data with scales in time (1 sec -> 9.5 years) for fun.<br>[Spreadsheet with chart](https://docs.google.com/spreadsheet/pub?key=0AnhVIbIC2eYjdDlqNUdJX0hfUVd5T1JLZFRjTEhtM3c&gid=0) |

 [![@vickychijwani](../_resources/0d2dfbb206a3a6e8fbeb9da5c1bb6811.jpg)](https://gist.github.com/vickychijwani)

 **  [vickychijwani](https://gist.github.com/vickychijwani)  ** commented [on Jun 1, 2012](https://gist.github.com/jboner/2841832#gistcomment-338405)

|     |
| --- |
| "Read 1 MB sequentially from disk - 20,000,000 ns". Is this with or without disk seek time? |

 [![@pgroth](../_resources/9e30d631baa6ce3a6ebb10f9607faf5a.jpg)](https://gist.github.com/pgroth)

 **  [pgroth](https://gist.github.com/pgroth)  ** commented [on Jun 1, 2012](https://gist.github.com/jboner/2841832#gistcomment-339001)

|     |
| --- |
| I made a fusion table for this at:<br>https://www.google.com/fusiontables/DataSource?snapid=S523155yioc<br>Maybe be helpful for graphing, etc. Thanks for putting this together |

 [![@jboner](../_resources/b5ffa1cea9e3c12395a394f88d14e396.jpg)](https://gist.github.com/jboner)

  Owner This user is the owner of the gist.

 **  [jboner](https://gist.github.com/jboner)  ** commented [on Jun 1, 2012](https://gist.github.com/jboner/2841832#gistcomment-339017)

|     |
| --- |
| Cool. Thanks.<br>Thanks everyone for all the great improvements. |

 [![@ayshen](../_resources/e52cfdac75d19b53101abcc15728f80e.png)](https://gist.github.com/ayshen)

 **  [ayshen](https://gist.github.com/ayshen)  ** commented [on Jun 2, 2012](https://gist.github.com/jboner/2841832#gistcomment-340259)

|     |
| --- |
| Here is a chart version. It's a bit hard to read, but I hope it conveys the perspective.<br>http://i.imgur.com/k0t1e.png |

 [![@gchatelet](../_resources/4ed1186ee7a7c431ed8f060ad57a8e34.jpg)](https://gist.github.com/gchatelet)

 **  [gchatelet](https://gist.github.com/gchatelet)  ** commented [on Jun 2, 2012](https://gist.github.com/jboner/2841832#gistcomment-340930)

|     |
| --- |
| It would also be very interesting to add memory allocation timings to that : ) |

 [![@PerWiklander](../_resources/bcad5632e82dde629857fbf9aea7999e.jpg)](https://gist.github.com/PerWiklander)

 **  [PerWiklander](https://gist.github.com/PerWiklander)  ** commented [on Jun 5, 2012](https://gist.github.com/jboner/2841832#gistcomment-342790)

|     |
| --- |
| How long does it take before this shows up in XKCD? |

 [![@talltyler](../_resources/28a75346b955f0164211851f48c10b64.jpg)](https://gist.github.com/talltyler)

 **  [talltyler](https://gist.github.com/talltyler)  ** commented [on Jun 5, 2012](https://gist.github.com/jboner/2841832#gistcomment-343095)

|     |
| --- |
| You guys are talking about is the powers of ten http://vimeo.com/819138 |

 [![@BillKress](../_resources/3e56862dd573cf51713c162b9f54c9cd.png)](https://gist.github.com/BillKress)

 **  [BillKress](https://gist.github.com/BillKress)  ** commented [on Jun 5, 2012](https://gist.github.com/jboner/2841832#gistcomment-343323)

|     |
| --- |
| If it does show up on xkcd it will be next to a gigantic "How much time it takes for a human to react to any results", hopefully with the intent to show people that any USE of this knowledge should be tempered with an understanding of what it will be used for--possibly showing how getting a bit from the cache is pretty much identical to getting a bit from china when it comes to a single fetch of information to show a human being. |

 [![@hellerbarde](../_resources/fa8f9101cb5cc16cb243f973c553d6ec.png)](https://gist.github.com/hellerbarde)

 **  [hellerbarde](https://gist.github.com/hellerbarde)  ** commented [on Jun 5, 2012](https://gist.github.com/jboner/2841832#gistcomment-343327)

|     |
| --- |
| [@BillKress](https://github.com/BillKress) yes, this is specifically for Programmers, to make sure they have an understanding about the bottlenecks involved in programming. If you know these numbers, you know that you need to cut down on disk access before cutting down on in-memory shuffling.<br>If you don't properly follow these numbers and what they stand for, you will make programs that don't scale well. That is why they are important on their own and (in this context) should not be dwarfed by human reaction times. |

 [![@PerWiklander](../_resources/bcad5632e82dde629857fbf9aea7999e.jpg)](https://gist.github.com/PerWiklander)

 **  [PerWiklander](https://gist.github.com/PerWiklander)  ** commented [on Jun 5, 2012](https://gist.github.com/jboner/2841832#gistcomment-343333)

|     |
| --- |
| [@BillKress](https://github.com/BillKress) If we were only concerned with showing information to a single human being at a time we could just as well shut down our development machines and go out into the sun and play. This is about scalability. |

 [![@klochner](../_resources/f6cd7e0b7ab76b1bca367c382c8479c3.jpg)](https://gist.github.com/klochner)

 **  [klochner](https://gist.github.com/klochner)  ** commented [on Jun 5, 2012](https://gist.github.com/jboner/2841832#gistcomment-343334)

|     |
| --- |
| this is getting out of hand, how do i unsubscribe from this gist? |

 [![@gemclass](../_resources/32fb7685148689f4b555c49faabb304c.png)](https://gist.github.com/gemclass)

 **  [gemclass](https://gist.github.com/gemclass)  ** commented [on Jun 7, 2012](https://gist.github.com/jboner/2841832#gistcomment-344727)

|     |
| --- |
| Saw this via @smashingmag . While you guys debate the fit for purpose, here is another visualization of your quick reference latency data with Prezi ow.ly/bnB7q |

 [![@briangordon](../_resources/2f1148619dc825e73923d4d15ae28a0c.jpg)](https://gist.github.com/briangordon)

 **  [briangordon](https://gist.github.com/briangordon)  ** commented [on Jul 3, 2012](https://gist.github.com/jboner/2841832#gistcomment-363275)

|     |
| --- |
| Does anybody know how to stop receiving notifications from a gist's activity? |

 [![@colin-scott](../_resources/58758bdcbd753d8570a0bc4ff4a3f2be.jpg)](https://gist.github.com/colin-scott)

 **  [colin-scott](https://gist.github.com/colin-scott)  ** commented [on Dec 25, 2012](https://gist.github.com/jboner/2841832#gistcomment-668520)

|     |
| --- |
| Here's a tool to visualize these numbers over time: http://www.eecs.berkeley.edu/~rcs/research/interactive_latency.html |

 [![@JensRantil](../_resources/f605107bef99577b9d2a70e6e1d492e2.jpg)](https://gist.github.com/JensRantil)

 **  [JensRantil](https://gist.github.com/JensRantil)  ** commented [on Jan 6, 2013](https://gist.github.com/jboner/2841832#gistcomment-706312)

|     |
| --- |
| I just created flash cards for this: https://ankiweb.net/shared/info/3116110484 They can be downloaded using the Anki application: [http://ankisrs.net](http://ankisrs.net/) |

 [![@JensRantil](../_resources/f605107bef99577b9d2a70e6e1d492e2.jpg)](https://gist.github.com/JensRantil)

 **  [JensRantil](https://gist.github.com/JensRantil)  ** commented [on Jan 14, 2013](https://gist.github.com/jboner/2841832#gistcomment-723269)

|     |
| --- |
| I'm also missing something like "Send 1MB bytes over 1 Gbps network (within datacenter over TCP)". Or does that vary so much that it would be impossible to specify? |

 [![@kofemann](../_resources/6022cde4c4f0c50e16945122257cfbd5.png)](https://gist.github.com/kofemann)

 **  [kofemann](https://gist.github.com/kofemann)  ** commented [on Feb 9, 2013](https://gist.github.com/jboner/2841832#gistcomment-770165)

|     |
| --- |
| If L1 access is a second, then:<br>L1 cache reference : 0:00:01<br>Branch mispredict : 0:00:10<br>L2 cache reference : 0:00:14<br>Mutex lock/unlock : 0:00:50<br>Main memory reference : 0:03:20<br>Compress 1K bytes with Zippy : 1:40:00<br>Send 1K bytes over 1 Gbps network : 5:33:20<br>Read 4K randomly from SSD : 3 days, 11:20:00<br>Read 1 MB sequentially from memory : 5 days, 18:53:20<br>Round trip within same datacenter : 11 days, 13:46:40<br>Read 1 MB sequentially from SSD : 23 days, 3:33:20<br>Disk seek : 231 days, 11:33:20<br>Read 1 MB sequentially from disk : 462 days, 23:06:40<br>Send packet CA->Netherlands->CA : 3472 days, 5:20:00 |

 [![@kofemann](../_resources/6022cde4c4f0c50e16945122257cfbd5.png)](https://gist.github.com/kofemann)

 **  [kofemann](https://gist.github.com/kofemann)  ** commented [on Feb 9, 2013](https://gist.github.com/jboner/2841832#gistcomment-770223)

|     |
| --- |
| You can add LTO4 tape seek/access time, ~ 55 sec, or 55.000.000.000 ns |

 [![@metakeule](../_resources/423441fbce415dae2f8bb2d03694ca47.png)](https://gist.github.com/metakeule)

 **  [metakeule](https://gist.github.com/metakeule)  ** commented [on Jul 29, 2013](https://gist.github.com/jboner/2841832#gistcomment-876375)

|     |
| --- |
| I'm missing things like sending 1K via Unix pipe/ socket / tcp to another process.<br>Has anybody numbers about that? |

 [![@shiplunc](../_resources/37a4cac2a3f93a546676277359853510.png)](https://gist.github.com/shiplunc)

 **  [shiplunc](https://gist.github.com/shiplunc)  ** commented [on Nov 27, 2013](https://gist.github.com/jboner/2841832#gistcomment-959178)

|     |
| --- |
| [@metakeule](https://github.com/metakeule) its easily measurable. |

 [![@mnem](:/876b7aaeb169d52ed31407786f011ed4)](https://gist.github.com/mnem)

 **  [mnem](https://gist.github.com/mnem)  ** commented [on Jan 9, 2014](https://gist.github.com/jboner/2841832#gistcomment-983163)

|     |
| --- |
| Related page from "Systems Performance" with similar second scaling mentioned by [@kofemann](https://github.com/kofemann): https://twitter.com/rzezeski/status/398306728263315456/photo/1 |

 [![@izard](../_resources/831a2e55d4bd2686a4dd2cf23490b112.jpg)](https://gist.github.com/izard)

 **  [izard](https://gist.github.com/izard)  ** commented [on May 29, 2014](https://gist.github.com/jboner/2841832#gistcomment-1237026)

|     |
| --- |
| L1D hit on a modern Intel CPU (Nehalem+) is at least 4 cycles. For a typical server/desktop at 2.5Ghz it is at least 1.6ns.<br>Fastest L2 hit latency is 11 cycles(Sandy Bridge+) which is 2.75x not 14x.<br>May be the numbers by Norwig were true at some time, but at least caches latency numbers are pretty constant since Nehalem which was 6 years ago. |

 [![@richa03](:/1ceeb758502c303d3d217c2f08a12c5d)](https://gist.github.com/richa03)

 **  [richa03](https://gist.github.com/richa03)  ** commented [on Aug 22, 2014](https://gist.github.com/jboner/2841832#gistcomment-1286379)

|     |
| --- |
| Please note that Peter Norvig first published this expanded version (at that location - http://norvig.com/21-days.html#answers) ~JUL2010 (see wayback machine). Also, note that it was "Approximate timing for various operations on a typical PC". |

 [![@pdjonov](../_resources/6a477bed167aa390a78d57b6d3d59a63.jpg)](https://gist.github.com/pdjonov)

 **  [pdjonov](https://gist.github.com/pdjonov)  ** commented [on Oct 3, 2014](https://gist.github.com/jboner/2841832#gistcomment-1311566)

|     |
| --- |
| One light-nanosecond is roughly a foot, which is considerably less than the distance to my monitor right now. It's kind of surprising to realize just how much a CPU can get done in the time it takes light to traverse the average viewing distance... |

 [![@junhe](../_resources/ea9fcc8465ee4c1a489cfe54e831c787.jpg)](https://gist.github.com/junhe)

 **  [junhe](https://gist.github.com/junhe)  ** commented [on Jan 16, 2015](https://gist.github.com/jboner/2841832#gistcomment-1374396)

|     |
| --- |
| [@jboner](https://github.com/jboner), I would like to cite some numbers in a formal publication. Who is the author? Jeff Dean? Which url should I cite? Thanks. |

 [![@weidagang](../_resources/3942baa7f00655cca2ab90987b186d7e.png)](https://gist.github.com/weidagang)

 **  [weidagang](https://gist.github.com/weidagang)  ** commented [on Jan 26, 2015](https://gist.github.com/jboner/2841832#gistcomment-1380503)

|     |
| --- |
| I'd like to see the number for "Append 1 MB to file on disk". |

 [![@dhartford](../_resources/e1328dba95f7bc4724c03f2df377b25a.png)](https://gist.github.com/dhartford)

 **  [dhartford](https://gist.github.com/dhartford)  ** commented [on Mar 11, 2015](https://gist.github.com/jboner/2841832#gistcomment-1410774)

|     |
| --- |
| The "Send 1K bytes over 1 Gbps network" doesn't feel right, if you were comparing the 1MB sequential read of memory, SSD, Disk, the Gbps network for 1MB would be faster than disk (x1024), that doesn't feel right. |

 [![@leotm](../_resources/5ec29a19bcc0c958b2680268e6c5c683.png)](https://gist.github.com/leotm)

 **  [leotm](https://gist.github.com/leotm)  ** commented [on May 2, 2015](https://gist.github.com/jboner/2841832#gistcomment-1444994)

|     |
| --- |
| A great solar system type visualisation: http://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html |

 [![@ali](../_resources/1cc88a32b48eada9ccc576647d2de68a.jpg)](https://gist.github.com/ali)

 **  [ali](https://gist.github.com/ali)  ** commented [on Sep 14, 2015](https://gist.github.com/jboner/2841832#gistcomment-1573607)

|     |
| --- |
| I turned this into a set of flashcards on Quizlet: https://quizlet.com/_1iqyko |

 [![@misgeatgit](../_resources/a22e939162ca2a17fba3ea0d86990fc9.png)](https://gist.github.com/misgeatgit)

 **  [misgeatgit](https://gist.github.com/misgeatgit)  ** commented [on Dec 11, 2015](https://gist.github.com/jboner/2841832#gistcomment-1646880)

|     |
| --- |
| Can you update the the Notes section with the following<br>1 ns = 10^-9 seconds<br>1 ms = 10^-3 seconds<br>Thanks. |

 [![@jboner](../_resources/b5ffa1cea9e3c12395a394f88d14e396.jpg)](https://gist.github.com/jboner)

  Owner This user is the owner of the gist.

 **  [jboner](https://gist.github.com/jboner)  ** commented [on Dec 13, 2015](https://gist.github.com/jboner/2841832#gistcomment-1648285)

|     |
| --- |
| [@misgeatgit](https://github.com/misgeatgit) Updated |

 [![@juhovuori](../_resources/bca5f8fe6976e0513c0b5c68c698a627.jpg)](https://gist.github.com/juhovuori)

 **  [juhovuori](https://gist.github.com/juhovuori)  ** commented [on Dec 25, 2015](https://gist.github.com/jboner/2841832#gistcomment-1657071)

|     |
| --- |
| Zippy is nowadays called snappy. Might be worth updating. Tx for the gist. |

 [![@georgevreilly](../_resources/9587ed53b08a2a05e88431c4f792805a.jpg)](https://gist.github.com/georgevreilly)

 **  [georgevreilly](https://gist.github.com/georgevreilly)  ** commented [on Jan 10, 2016](https://gist.github.com/jboner/2841832#gistcomment-1666819)

|     |
| --- |
| Several of the recent comments are spam. The links lead to sites in India which have absolutely nothing to do with latency. |

 [![@wenjianhn](../_resources/762adc05ae4f8b138bbc0800bdc58968.jpg)](https://gist.github.com/wenjianhn)

 **  [wenjianhn](https://gist.github.com/wenjianhn)  ** commented [on Jan 12, 2016](https://gist.github.com/jboner/2841832#gistcomment-1667825)

|     |
| --- |
| Are there any numbers about latency between NUMA nodes? |

 [![@vitaut](../_resources/1e4f50e6d345cbf050f682b0c5a4aae7.jpg)](https://gist.github.com/vitaut)

 **  [vitaut](https://gist.github.com/vitaut)  ** commented [on Jan 31, 2016](https://gist.github.com/jboner/2841832#gistcomment-1685309)

|     |
| --- |
| Sequential SSD speed is actually more like 500 MB/s, not 1000 MB/s for SATA drives (http://www.tomshardware.com/reviews/ssd-recommendation-benchmark,3269.html). |

 [![@BruceGooch](../_resources/02443cb359738ff20feb24c1799903b2.png)](https://gist.github.com/BruceGooch)

 **  [BruceGooch](https://gist.github.com/BruceGooch)  ** commented [on Mar 9, 2016](https://gist.github.com/jboner/2841832#gistcomment-1719190)

|     |
| --- |
| You really should cite the folks at Berkeley. Their site is interactive, has been up for 20 years, and it is where you "sourced" your visualization. http://www.eecs.berkeley.edu/~rcs/research/interactive_latency.html |

 [![@aerovistae](../_resources/95cc6ef191cfe4f9f090f83b581928cb.png)](https://gist.github.com/aerovistae)

 **  [aerovistae](https://gist.github.com/aerovistae)  ** commented [on Mar 10, 2016](https://gist.github.com/jboner/2841832#gistcomment-1720094)

|     |
| --- |
| Question~ do these numbers not vary from one set of hardware to the next? How can these be accurate for all different types of RAM, CPU, motherboard, hard drive, etc?<br>(I am primarily a front-end JS dev, I know little-to-nothing about this side of programming, where one must consider numbers involving RAM and CPU. Forgive me if I'm missing something obvious.) |

 [![@jlleblanc](../_resources/448b8d2a056969bb40f72ca3fc654029.jpg)](https://gist.github.com/jlleblanc)

 **  [jlleblanc](https://gist.github.com/jlleblanc)  ** commented [on Mar 21, 2016](https://gist.github.com/jboner/2841832#gistcomment-1729617)

|     |
| --- |
| The link to the animated presentation is broken, here's the correct one: http://prezi.com/pdkvgys-r0y6/latency-numbers-for-programmers-web-development |

 [![@keenkit](../_resources/b7766c027297f85857530d7e3859b31c.png)](https://gist.github.com/keenkit)

 **  [keenkit](https://gist.github.com/keenkit)  ** commented [on Aug 16, 2016](https://gist.github.com/jboner/2841832#gistcomment-1850139)

|     |
| --- |
| Love this one. |

 [![@profuel](../_resources/db85c03de2688330fb6fe2c4e5e7e17a.jpg)](https://gist.github.com/profuel)

 **  [profuel](https://gist.github.com/profuel)  ** commented [on Oct 5, 2016](https://gist.github.com/jboner/2841832#gistcomment-1890256)

Mentioned [object Object] : https://gist.github.com/2843375 is private or was removed.

can someone restore it?
Thanks!

 [![@trans](../_resources/d0cb8861aa7cdf0699507b1d7fe484f8.jpg)](https://gist.github.com/trans)

 **  [trans](https://gist.github.com/trans)  ** commented [on Oct 9, 2016](https://gist.github.com/jboner/2841832#gistcomment-1893619)

|     |
| --- |
| It would be nice to be able to compare this to computation times -- How long to do an add, xor, multiply, or branch operation? |

 [![@mpron](../_resources/2a11f0192cc78fbc1e1d09d9dc78d4a9.jpg)](https://gist.github.com/mpron)

 **  [mpron](https://gist.github.com/mpron)  ** commented [on Oct 12, 2016](https://gist.github.com/jboner/2841832#gistcomment-1896155) •  edited mpron edited this comment 7 months ago

|     |
| --- |
| Last year, I came up with this concept for an infographic illustrating these latency numbers with time analogies (if 1 CPU cycle = 1 second). Here was the result: http://imgur.com/8LIwV4C |

 [![@pawel-dubiel](../_resources/bb7b79d9124483c34cbd46fdaa0e3163.png)](https://gist.github.com/pawel-dubiel)

 **  [pawel-dubiel](https://gist.github.com/pawel-dubiel)  ** commented [on Jan 29](https://gist.github.com/jboner/2841832#gistcomment-1983273) •  edited pawel-dubiel edited this comment 3 months ago

|     |
| --- |
| Most of these number were valid in 2000-2001, right now some of these numbers are wrong by an order of magnitude. ( especially reading from main memory, as DRAM bandwidth doubles every 3 years ) |

 [![@maranomynet](../_resources/9b164568a7cfa01090f3829b648184e6.png)](https://gist.github.com/maranomynet)

 **  [maranomynet](https://gist.github.com/maranomynet)  ** commented [on Jan 31](https://gist.github.com/jboner/2841832#gistcomment-1985095)

[object Object], not [object Object]

 [![@GLMeece](../_resources/8fa619b215c2c26e709584428da1fe5d.jpg)](https://gist.github.com/GLMeece)

 **  [GLMeece](https://gist.github.com/GLMeece)  ** commented [on Jan 31](https://gist.github.com/jboner/2841832#gistcomment-1985124) •  edited GLMeece edited this comment 3 months ago

|     |
| --- |
| I realize this was published some time ago, but the following URLs are no longer reachable/valid:<br>- https://gist.github.com/2843375<br>- http://prezi.com/pdkvgys-r0y6/latency-numbers-for-programmers-web-development/latency.txt<br>However, the second URL should now be: https://prezi.com/pdkvgys-r0y6/latency-numbers-for-programmers-web-development/<br>Oh, and [@mpron](https://github.com/mpron) - nice! |

 [![@JustinNazari](../_resources/b890a667807c08ba08cba6c368321fac.jpg)](https://gist.github.com/JustinNazari)

 **  [JustinNazari](https://gist.github.com/JustinNazari)  ** commented [on Jan 31](https://gist.github.com/jboner/2841832#gistcomment-1985150)

|     |
| --- |
| Thank you [@jboner](https://github.com/jboner) |

 [![@GLMeece](../_resources/8fa619b215c2c26e709584428da1fe5d.jpg)](https://gist.github.com/GLMeece)

 **  [GLMeece](https://gist.github.com/GLMeece)  ** commented [on Jan 31](https://gist.github.com/jboner/2841832#gistcomment-1985152)

|     |
| --- |
| Note: I created [my own "fork" of this](https://gist.github.com/GLMeece/b00c9c97a06a957af7426b1be5bc8be6). |

 [![@ValerieAnne563](../_resources/5bf5510a6aa60c748550fe8c72e32572.jpg)](https://gist.github.com/ValerieAnne563)

 **  [ValerieAnne563](https://gist.github.com/ValerieAnne563)  ** commented [6 days ago](https://gist.github.com/jboner/2841832#gistcomment-2081915)

|     |
| --- |
| Thank you [@GLMeece](https://github.com/GLMeece) |

 [![@marcacohen](../_resources/c3a2ffa44015d8c7503ed773b9db1ffe.jpg)](https://gist.github.com/marcacohen)

  Attach files by dragging & dropping, selecting them, or pasting from the clipboard.

 [ Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/)