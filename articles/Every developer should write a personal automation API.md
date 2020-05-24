Every developer should write a personal automation API

#  Every developer should write a personal automation API

###   [  [anotherdevblog profile image](../_resources/b225b4e9396ae3e4d6873a674ba8c9ea.webp) Matthew Watkins](https://dev.to/anotherdevblog)  [(L)](http://github.com/anotherdevblog)  Nov 20, 2016

 [#dev](https://dev.to/t/dev)  [#api](https://dev.to/t/api)  [#ifttt](https://dev.to/t/ifttt)

## IFTTT, the building block of personal automation

[[IFTTT Logo](../_resources/1cc758d1a3f557eb818ff11110541808.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--VVvNVYaH--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/ifttt-logo.png)

A few years ago I fell in love with [If This Then That](https://ifttt.com/) (IFTTT). It's a remarkable, free service that lets you build simple rules for hundreds of apps, web services, IOT devices, and more. It's a great concept, and so amazing that I could not do it justice in this post. If you're not familiar with IFTTT (or the new Microsoft-hosted competitor, [Flow](https://flow.microsoft.com/en-us/)), drop what you are doing and go check them out right now. Seriously, I can wait.

IFTTT filled a gap in my digital life I hadn't thought to fill before. But after using it for a while, I found myself itching for an even higher level of customization. I wanted to transform outputs, to chain rules together, and to add condition statements. Basically, I wanted IFTTT to be a free, hosted cron job executor with a nice UI, mobile apps, and hundreds of libraries I could use. I loved the simplicity of the rudimentary rules engines they offered, but I wanted more. I suspect many developers felt the same way.

[[Maker Logo](../_resources/ddc9d1aa4060d10f7326ab8679936817.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--QXrc0VEY--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/maker-logo.jpg)

Luckily, IFTTT heard the voice of the devs and added the [Maker Channel](https://ifttt.com/maker), opening up endless possibilities. Think of it as a very simple, standardized API endpoint for IFTTT itself-- an HTTP API shell around all of the apps/services that IFTTT supports. You know all those times you wish there was some simple API around some service you use that doesn't require tons of setup and OAuth and SDKs and documentation? Well, you're welcome.

Between being able to receive requests and being able to call out to arbitrary HTTP endpoints, too, the Maker channel gives you all you need to build any automation you can dream of. Need some inspiration? Here are some of the things I'm doing with my API.

## Ideas for your own API

### Location reporting

[![Location image](../_resources/c2160c585d331efb94b1054b10b9dcab.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--auB4t4T4--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/location-map.jpg)

I installed [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) on the my phone and my wife's phone and setup a rule so that each time our phones connect to or disconnect from a Wifi network, and every few minutes when we're not connected to Wifi, our phones call out to my API and report its location and connected network.

On the API end, I group each person into home or away. From there you can track history, see the most recent location, etc. This by itself is a neat, bare-bones alternative to a more full-featured, third-party app like Life360 or Google+ location widgets. Helpful for emergencies (or alibis), but mainly crucial for the next piece.

### Smart home automation

[[Smart home image](../_resources/a04901c400fd1ff2ad9311dfa3d8a863.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--4KdOfp8Q--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/smart-home.jpg)

We have a smart alarm system and thermostat both compatible with IFTTT. When my API detects that all phones have reported back as being "away," it automatically arms our alarm system and turns the thermostat to away mode. The minute any one of us pulls into the driveway, our phones connect to the Wifi and report back to the API that we are home. The API disarms the system and sets the thermostat to home mode before we even make it into the house. In addition to location-based home/away automation, I wrote a cron job to toggle the alarm and thermostat between night and day mode as well.

I've found that the glass break sensor in our alarm system is super sensitive. I've had it go off when it hears the ice dispenser. Or plates clinking together. Or when I sneeze. So I also installed a simple HTTP request app on my Pebble watch to allow to me disarm the alarm with the press of a button on my wrist.

In the event that the alarm goes off and is not silenced within a minute, a text message is sent to a tech-savvy relative living nearby letting them know that if they don't receive a call from us, there may be a problem. I set up an SOS feature on the watch that does the same thing.

### Build monitoring

[[Siren image](../_resources/724313e19faad9ef9b50c98cc560f6c3.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--XbYmHdL5--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/siren-light.jpg)

Most build monitoring systems have some sort of post-build hook that you can use to attach to your API nicely. But even if not, almost all will send out emails with every build. That's where I'm at with my current job. I filter all build messages to a specific folder of my work Gmail and have a script check that folder every minute for any new build messages. It looks at the message and parses it to determine the current state of the build and if I contributed to it. If it's broken and I have contributed, it hits out to my API to send me a threatening message to my phone and watch via [Pushbullet](https://www.pushbullet.com/).

### Site uptime monitoring

[[404 image](../_resources/d95d23ab7435a8b102fe7649a2b3db95.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--YWyCcpTT--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/404-page.jpg)

Recently a homework-critical web resource at school started going through a nasty bout of server issues. A lot. So I added an API cron job to query [UptimeRobot](https://uptimerobot.com/) for the status of that resource and post to the class Slack channel when that site went down or came back up again. That way we could all go start doing other things while we wait for the site to come back up instead of hitting refresh over and over again.

### Automated stock management

[[stocks image](../_resources/07974d562df3508e8dda28f33f64e0c9.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--unAHIxyh--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/stocks.jpg)

Yes, IFTTT has a very basic integration for monitoring individual stocks. But the depth of the data you get is quite sad. So, I added functionality to my API to maintain a list of stock symbols I'm watching and query the the richer data for those symbols every few minutes from the [practically undocumented Yahoo Finance API](http://www.jarloo.com/yahoo_finance/). When the stocks move into certain high/low thresholds of the 52-week highs/lows, I get notified in case I want to buy or sell.

**Bonus tip:** For the truly daring, I hear you can supposedly automate the whole thing with your [Robinhood](https://robinhood.com/) account and its [secret API](https://github.com/sanko/Robinhood). The free trades makes the deal almost perfect if you can get it automated right. But if you're going to go through that hassle, just sign up with [Quantopian](https://www.quantopian.com/) and do it the right way.

### General data querying

[[DB image](../_resources/f5b0382d66896f96042d7901a9707eb4.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--5GeZu3WW--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/db.png)

Really, anything becomes an API if you want it to. Let me give you an example. Before my wife and I gave in and got a second car, I would take the bus from school to work every day. But depending on where I was and what time it was, I had various options of which routes came to which stops at which times. And trying to piece together 4 different route schedules every day was a nightmare.

So I entered all the schedule information into a Google spreadsheet for the routes and stops I cared about. Then I added functionality to the API to query the next arriving buses/locations and added a trigger for that action to my smart watch. Get out of class, press a button, and I receive a notification letting me know exactly which buses would be arriving at which stops next and when they would get me to my workplace. Simple yet super helpful.

### Remote shutdown/restart your computer

[[Remote computer control image](../_resources/e2a0c6bac41cb776c6d69e0701dc0235.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--QLS2FTYq--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/laptop-remote.jpg)

If my work machine has been unused for longer than a few hours, it stops responding to RDP connections. No friggin clue why. I've gone down the "check your power settings" route and the BIOS route and… nothing. Even looked at a possible network issue with the docking firmware.

Fortunately, the machine still receives and responds to all other network traffic in this state. But TeamViewer, LogMeIn, and Chrome Remote Desktop are big No-nos. So I wrote a quick Windows task that-- you guessed it-- queries my API to ask every 5 minutes to ask whether it needs to restart. This is a very temporary workaround (I sincerely hope), but so far it's been useful (and frequently used) enough that this particular action has earned a place as a DO button widget on my phone's home screen.

## Writing your own API

So, how do you write your API? What stack will you use? What about hosting? If you already own a personal website running the stack of your choice, mazel tov. But if not, I have a good, powerful, free alternative to suggest:

If you don't want to go through the hassle of setting up your own server and are comfortable with JavaScript, check out [Google Apps Script](https://developers.google.com/apps-script/) as an option for your API. Scripts you write can be configured to execute functions you select on a schedule, and and can act like a server in processing HTTP requests, calling other APIs, and largely running whatever code you want. Additionally, they come with built-in libraries to let you interact with your account's Google Calendar, Gmail, Drive, Docs, and basically anything else.

On the other hand, if you want an actual, proper server environment but still don't want to pay anything, check out the many providers offering tiny but free Linux VMs. [Cloud 9](https://c9.io/) is probably my favorite in that arena. Extra points if you load .NET Core on your Linux VM and write your API in beautiful C## [just because you can](http://www.hanselman.com/blog/PublishingAnASPNETCoreWebsiteToACheapLinuxVMHost.aspx) :) Azure, AWS, and others are fine options, too.

I ended up going down the Google Apps Script route. I had used Google Apps Script before when writing [GmailSnooze](https://chrome.google.com/webstore/detail/gmail-snooze/alpijhhgggjdfchmlhofhifceddjdlaf), so I was already fairly comfortable with it, and even on my personal account, I haven't even come close to hitting their rate limits and haven't had any issues with reliability. So far no regrets. If you want to try your hand at Google Apps Script, I'll be writing about how I set up my personal API in [my next post](https://dev.to/personal-automation-api/part-1-getting-started/). Stay tuned.

## Is it worth it?

As I've worked on this personal API project, I've often thought of Randall Munroe's famous automation effort graph:

[[Automation Graph](../_resources/d5eec5a6c7bc4bac98004b241dfe9080.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--M31EjT1p--/c_limit,f_auto,fl_progressive,q_auto,w_880/http://anotherdevblog.net/assets/images/xkcd-automation-time-graph.png)

I often ask myself, "How much time have I really saved compared to the original task? Am I just going down an automation rabbit hole?" I know that for some aspects, the automation has been convenient, but not life-changing. And some definitely took way too many hours debugging and rewriting to get just right. But as I add each new feature to my API, the next one becomes even easier to implement.

Most importantly though, my very way of thinking has changed. Every time a thought pops into my heads that starts with "Man, I wish I didn't have to…" it usually ends with "... could I automate this somehow?" And really, that's what software development is all about. We spend all day at work tinkering and automating and fine-tuning and improving various aspects of our business. How often do we take a few minutes to see what we could do to apply that to our lives? Who knows, you might find a way to automate just the right thing, and it ends up being the next big thing.

Uh-oh, my watch just buzzed. Got to go fix the build :)

* * *

*This post first appeared on [Another Dev Blog](http://anotherdevblog.net/personal-automation-api/every-developer-should-write-a-personal-automation-api/)*

 [  [anotherdevblog profile](../_resources/2bc44556fd721a43ba0b9bbc3d8cf28e.webp)](https://dev.to/anotherdevblog)

#### [Matthew Watkins](https://dev.to/anotherdevblog)

Husband, father, developer, blogger

 [  [github](../_resources/43298f53fbd00b8582fd1a9a7adf1197.png) anotherdevblog](http://github.com/anotherdevblog)  [  [link](../_resources/b5b447835a04fca6fe7559db1f40b440.png) www.anotherdevblog.net](http://www.anotherdevblog.net/)

 [  [info-e41d8339284ee95aee60021abfd0f2cecd660193460eaf6b58f0c71b36770668.svg](../_resources/205670474f5aad8dbf662ded7fc9c695.bin)](https://dev.to/p/editor_guide)

 [![github-logo_m841aq.png](../_resources/b225b4e9396ae3e4d6873a674ba8c9ea.webp)     Matthew Watkins](https://dev.to/anotherdevblog)  [[Github logo](../_resources/df260fd254a319e41da3fa114ff9bce1.bin)](http://github.com/anotherdevblog)

 [Feb 11](https://dev.to/anotherdevblog/comment/34h)

Yes. There is an Android app for IFTTT that makes various aspects of your phone a source for triggers and actions. As far as your personal automation API, you can issue requests to it with a lot of different apps. I personally use Trigger. I continue this series on writing a personal automation API on my blog if you want more details:

[anotherdevblog.net](http://anotherdevblog.net/)

 [REPLY](https://dev.to/anotherdevblog/every-developer-should-write-a-personal-automation-api#/anotherdevblog/every-developer-should-write-a-personal-automation-api/comments/new/34h)

 [  [location-map.jpg.webp](../_resources/33c9703a322ebb1bbc817c81c212667c.webp)     Ash](https://dev.to/fatima_alansari)  [[Github logo](../_resources/df260fd254a319e41da3fa114ff9bce1.bin)](http://github.com/fatima-alansari)

 [Dec 23](https://dev.to/fatima_alansari/comment/1mnj)

I hate to be "that guy", but if anyone steals your or your wife's phone they can just go up to your place and waltz right in undoing the security system, with the way you set up the home automation. Please rethink that, for your family's safety.

Great post though :3 got me thinking of a few things to do

 [REPLY](https://dev.to/anotherdevblog/every-developer-should-write-a-personal-automation-api#/anotherdevblog/every-developer-should-write-a-personal-automation-api/comments/new/1mnj)

 [  [laptop-remote.jpg.webp](../_resources/bafc574ff94042b5779e2d5424a6bb37.webp)     Oliver Cole](https://dev.to/olivercole)  [(L)](http://github.com/OliverCole)

 [Dec 23](https://dev.to/olivercole/comment/1mo7)

Definitely check out Huginn - [github.com/huginn/huginn/](https://github.com/huginn/huginn/)

 [REPLY](https://dev.to/anotherdevblog/every-developer-should-write-a-personal-automation-api#/anotherdevblog/every-developer-should-write-a-personal-automation-api/comments/new/1mo7)

 [   Tesla](https://dev.to/wpdevvy)  [(L)](http://twitter.com/wpDevvy)
 [Feb 10](https://dev.to/wpdevvy/comment/32o)

Thanks for the amazing article. Is there a way to trigger custom scripts on an android with IFTTT?

 [REPLY](https://dev.to/anotherdevblog/every-developer-should-write-a-personal-automation-api#/anotherdevblog/every-developer-should-write-a-personal-automation-api/comments/new/32o)

 [![cd6a59ac-b1b8-4e0c-9656-53e366152d97.jpeg](../_resources/d2861e164277166a9620885a203f1be3.jpg)     nino-porcino](https://dev.to/nippur72)  [(L)](http://github.com/nippur72)

 [Dec 23](https://dev.to/nippur72/comment/1mo2)

years ago there was on{X} by Microsoft and it was fantastic until it was deprecated :-(

 [REPLY](https://dev.to/anotherdevblog/every-developer-should-write-a-personal-automation-api#/anotherdevblog/every-developer-should-write-a-personal-automation-api/comments/new/1mo2)

 [code of conduct](https://dev.to/code-of-conduct)-[report abuse](https://dev.to/report-abuse?url=http://dev.to/anotherdevblog/every-developer-should-write-a-personal-automation-api)