Bug in Google's Bug Tracker Lets Researcher Access List of Company's Vulnerabilities

More From[Internet Insecurity](https://motherboard.vice.com/en_us/topic/internet-insecurity)

- [![1509119160122-shutterstock_432464806.jpeg](../_resources/2790d05d5904c02a5010d811ab91d06a.jpg)   T-Mobile Alerted ‘A Few Hundred Customers’ Targeted By Hackers](https://motherboard.vice.com/en_us/article/a37epb/t-mobile-alert-victims-sim-card-hack)
- [![1508967031739-equifax-illustration.jpeg](../_resources/a9161b86c3df6693fe377e663c55cbd0.jpg)   Equifax Was Warned](https://motherboard.vice.com/en_us/article/ne3bv7/equifax-breach-social-security-numbers-researcher-warning)
- [![1508961044732-shutterstock_218848288.jpeg](:/93ffad434a4b975985258e91b67a18db)   Infrastructure for the ‘Bad Rabbit’ Ransomware Appears to Have Shut Down](https://motherboard.vice.com/en_us/article/d3dp5q/infrastructure-for-the-bad-rabbit-ransomware-appears-to-have-shut-down)
- [![1508869311413-GettyImages-108196348.jpeg](../_resources/944a2df92f3806f9f6709a3067d9b829.jpg)   New Ransomware ‘Bad Rabbit’ Spreading Quickly Through Russia and Ukraine](https://motherboard.vice.com/en_us/article/59yb4q/bad-rabbit-petya-ransomware-russia-ukraine)

# Bug in Google's Bug Tracker Lets Researcher Access List of Company's Vulnerabilities

## A series of bugs allowed hackers to snoop into one of Google’s most sensitive internal systems.

- [[motherboard-tombstone.svg](../_resources/74c22bbfce3a24986248169c8f7a1cbc.bin)SHARE]()
- [[facebook-square.svg](../_resources/05263608ee3395a946eca7b32b971334.bin)TWEET]()

[![Lorenzo Franceschi-Bicchierai](../_resources/5823dc788478fa27a19aa46f595131d7.jpg)](https://motherboard.vice.com/en_us/contributor/lorenzo-franceschi-bicchierai)

 [Lorenzo Franceschi-Bicchierai](https://motherboard.vice.com/en_us/contributor/lorenzo-franceschi-bicchierai)

Oct 30 2017, 3:00pm

![1509375102358-shutterstock_691715200-copy.jpeg](../_resources/4672811c57c0dcbcda6a3b026ccb245a.jpg)

Image: Shutterstock. Composite: Jason Koebler/Motherboard

Google's platform to deal with bugs and unpatched vulnerabilities had a bug that allowed a security researcher to see a full list of known, unpatched vulnerabilities within Google, creating a kind of bug inception that could have led to more damaging hacks.

 [Alex Birsan](https://twitter.com/alxbrsn), a security researcher, found three vulnerabilities inside the Google Issue Tracker, the company's internal platform where employees keep track of requested features or unpatched bugs in Google's products. The largest one of these was one that allowed him to access the internal platform at all. The company has quickly patched the bugs found by Birsan, and there's no evidence anyone else found the bugs and exploited them.

Still, these were bad bugs, especially the one that gave him access to the bug-tracking platform, which could have provided hackers with a list of vulnerable targets at Google.

"Exploiting this bug gives you access to every vulnerability report anyone sends to Google until they catch on to the fact that you're spying on them," Birsan told Motherboard in an online chat. "Turning those vulnerability reports into working attacks also takes some time/skill. But the bigger the impact, the quicker it gets fixed by Google. So even if you get lucky and catch a good one as soon as it's reported, you still have to have a plan for what you do with it."

A Google spokesperson said in an email statement: "We appreciate Alex's report. We've patched the vulnerabilities that he reported, as well as their variants."

 ** Read more: **[** T-Mobile Website Allowed Hackers to Access Your Account Data With Just Your Phone Number**](https://motherboard.vice.com/en_us/article/wjx3e4/t-mobile-website-allowed-hackers-to-access-your-account-data-with-just-your-phone-number)

Access to the Google Issue Tracker—internally called Buganizer System—is normally limited to employees. External researchers can be granted access to specific threads, such as to the bugs they report. Birsan, however, found a way to circumvent the strict permissions and subscribe to any thread on the platform, allowing him to "see details about every issue in the database," [as he explained in a blog post](https://medium.com/@alex.birsan/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5).

Birsan found that Google had programmed a way for external researchers to remove themselves from email lists. This worked the way it was intended, removing the person from the thread, and sending the details of the bug as a final message. But this mechanism had a problem: it didn't actually check if the user requesting to be removed had permission to access the issue in question. So it was possible for anyone to "unsubscribe" from issue they were never subscribed to and thus learn the details of the vulnerability.

Advertisement

"You'd have a pretty good chance of compromising Google accounts if you had a few specific targets and threw every attack at them."

Still, there's a reason Google is generally known for its good corporate security: Birsan said that with the vulnerabilities he saw, it would have been very difficult or perhaps impossible to launch a widespread attack that affected even a fraction of Google's users.

"I believe you'd have a pretty good chance of compromising Google accounts if you had a few specific targets and threw every attack at them," Birsan told me. "But a large scale attack that puts hundreds/thousands of people at risk? Not so much."

There's no evidence anyone other than Birsan found this bug, and Google patched it within an hour of his report, according to Birsan. But such a platform is a juicy target for bad guys, especially sophisticated hackers and government spies. On Oct. 17, Reuters [revealed](https://www.reuters.com/article/us-microsoft-cyber-insight/exclusive-microsoft-responded-quietly-after-detecting-secret-database-hack-in-2013-idUSKBN1CM0D0) that hackers had breached Microsoft's internal database to track bugs into its own software in 2013.

Birsan found a total of three bugs in the platform. They are all patched now and he received rewards of $3,133.7, $5,000, and $7,500 for reporting them to Google.

 **  * Got a tip? You can contact this reporter securely on Signal at +1 917 257 1382, OTR chat at lorenzo@jabber.ccc.de, or email ***[**  * lorenzo@motherboard.tv***](https://motherboard.vice.com/en_us/article/evbvqj/bug-in-googles-bug-tracker-lets-researcher-access-list-of-companys-vulnerabilitiesmailto:lorenzo@motherboard.tv)

 **  * Get six of our favorite Motherboard stories every day *****[*by signing up for our newsletter.*](http://motherboard.club/)**

## Episode Info

##### Dear Future | S1 EP2

## Nuclear Fusion Energy: The Race to Create a Star on Earth

If the processes powering the fusion reactor at the Sun's core could be recreated on Earth, it would be one of the most important events in the history of our species. Nuclear fusion power plants could end our dependency on fossil fuels and provide a virtually limitless, highly efficient source of clean energy.

We went to two of the world's leading nuclear fusion research centers—Sandia National Labs in New Mexico and General Fusion outside Vancouver—to see how close we are to bringing the power of the stars down to Earth.

* * *

|     |     |
| --- | --- |
| Channel | Motherboard |
| Runtime | 11:05 |
| Host | Xavier Aaronson |
| Rating | TV-PG |

## Up Next

1

##### The 16 Project

### Meet the Lebron James of Weightlifting

![59b1a1ba0f817e2a11535d4c-1509469340994.jpg](../_resources/9aae0a7251849785cf3b8065389d6621.jpg)06:13

2

##### Eatin' It

### Going Local with Table Farm

![59259d988bd5c6e92027e597-1509468225330.jpg](../_resources/09c0d1b844828986d078395baa0e083d.jpg)09:03

3

##### Weediquette

### Possessed by Marijuana: The Camille Browne Case

![59f894d7177dd4323f14a04a-1509465966161.jpg](../_resources/854bd845ed0075d239577df5c07ec855.jpg)03:43

4

##### Waypoint Plays

### A Spooky 'Darkwood' Playthrough - Waypoint in the AM

![59f36de4177dd44d757e3733-1509466079975.jpg](../_resources/80c233f4152ae2f84158b4d559560248.jpg)1:02:09

5

##### American Conventions

### The Weird, Wild World of Skunk Owners

![59b7eae7530137992a801429-1509457926382.jpg](../_resources/9f69cfa79731ea9aa000a7cca32e3e21.jpg)21:52

6

##### The Untitled Action Bronson Show

### Kevin Gillespie, Meyhem Lauren

![59ef673f177dd4345f10648c-1509392139402.jpg](../_resources/be0da593951db560b96ee5c1daec3408.jpg)22:33

7

##### Desus & Mero

### The Legendary Rosie Perez

![59f79ea8177dd42093251851-1509418503501.jpg](../_resources/564a08809d65e1a75fc1d22bc9b39c7c.jpg)25:02

8

##### Desus & Mero

### Cardi B and Offset Are Now Engaged

![59f79d14177dd40db620ee11-1509418481146.jpg](../_resources/a5c37ea200aeed690c1ca737596683d5.jpg)02:01

9

##### Desus & Mero

### George Papadopoulos Pleads Guilty in Mueller Russia Probe

![1509418586820-dm-marked-2.jpeg](../_resources/318e452b4387cf981894b2913f78f304.jpg)02:04
10

##### Desus & Mero

### Paul Manafort Gets Indicted

![59f78940177dd45f2c422f71-1509418158660.jpg](../_resources/cd68d8771d5a731654c6d0a55f39d6e9.jpg)04:26

### Dear Future

## Nuclear Fusion Energy: The Race to Create a Star on Earth

11:05

![1487269334511-motherboard-logo-white3x.png](../_resources/a8d696b88db60bb2c9fbc00e824a02a3.png)

[twitter.svg](../_resources/0ddc9b9f6b172737987cd28e7283ba90.bin)

- [SHARE]()
- [TWEET]()
- [News](https://motherboard.vice.com/en_us/topic/news)
- [hacking](https://motherboard.vice.com/en_us/topic/hacking)
- [Google](https://motherboard.vice.com/en_us/topic/google)
- [cybersecurity](https://motherboard.vice.com/en_us/topic/cybersecurity)
- [hackers](https://motherboard.vice.com/en_us/topic/hackers)
- [bugs](https://motherboard.vice.com/en_us/topic/bugs)
- [Infosec](https://motherboard.vice.com/en_us/topic/infosec)
- [vulnerabilities](https://motherboard.vice.com/en_us/topic/vulnerabilities)
- [Tech news](https://motherboard.vice.com/en_us/topic/tech-news)
- [Bug Bounty](https://motherboard.vice.com/en_us/topic/bug-bounty)

Watch This Next

[ ![57058162ecd761cb01763dd8-1501606764457.jpg](../_resources/dc55444128b5f299e9bd3005dc883212.jpg)   12:42     High Speed Off-Roading in the Mojave Desert]()