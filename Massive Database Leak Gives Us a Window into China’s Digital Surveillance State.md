Massive Database Leak Gives Us a Window into China’s Digital Surveillance State

Earlier this month, security researcher Victor Gevers [found and disclosed](https://www.zdnet.com/article/chinese-company-leaves-muslim-tracking-facial-recognition-database-exposed-online/) an exposed database live-tracking the locations of about 2.6 million residents of Xinjiang, China, offering a window into what a digital surveillance state looks like in the 21st century.

Xinjiang is China’s largest province, and home to China’s Uighurs, a Turkic minority group. Here, the Chinese government has implemented [a testbed police state](https://www.economist.com/briefing/2018/05/31/china-has-turned-xinjiang-into-a-police-state-like-no-other) where an estimated 1 million individuals from these minority groups have been [arbitrarily detained](https://www.nytimes.com/2018/12/16/world/asia/xinjiang-china-forced-labor-camps-uighurs.html?module=inline). Among the detainees are [academics, writers, engineers](https://www.nytimes.com/2019/01/05/world/asia/china-xinjiang-uighur-intellectuals.html), and [relatives](https://www.nytimes.com/2019/02/17/world/asia/uighurs-china-internment-camps.html) of Uighurs in exile. Many Uighurs abroad worry for their [missing family members](https://www.nytimes.com/2019/02/17/world/asia/uighurs-china-internment-camps.html), who they haven’t heard from for several months and, in some cases, over a year.

Although relatively little news gets out of Xinjiang to the rest of the world, we’ve known for over a year that China has been testing facial-recognition tracking and alert systems [across Xinjiang](https://www.theguardian.com/world/2018/jan/18/china-testing-facial-recognition-surveillance-system-in-xinjiang-report) and mandating the collection of [biometric data](https://www.hrw.org/news/2017/12/13/china-minority-region-collects-dna-millions)—including DNA samples, voice samples, fingerprints, and iris scans—from all residents between the ages of 12 and 65. Reports from the province in 2016 indicated that Xinjiang residents can be questioned over the use of mobile and Internet tools; just having [WhatsApp or Skype](https://www.eff.org/deeplinks/2016/01/china-shows-how-backdoors-lead-software-censorship) installed on your phone is classified as “subversive behavior.” Since 2017, the authorities have instructed all Xinjiang mobile phone users to [install a spyware app](https://advox.globalvoices.org/2017/07/19/chinas-xinjiang-residents-are-being-forced-to-install-surveillance-apps-on-mobile-phones/) in order to “prevent [them] from accessing terrorist information.”

The prevailing evidence of mass detention centers and newly-erected surveillance systems shows that China has been [pouring billions of dollars](https://www.nytimes.com/2018/07/08/business/china-surveillance-technology.html) into physical and digital means of pervasive surveillance in Xinjiang and other regions. But it’s often unclear to what extent these projects operate as real, functional high-tech surveillance, and how much they are primarily intended as a sort of “security theater”: a public display of oppression and control to intimidate and silence dissent.

Now, this security leak shows just how extensively China is tracking its Xinjiang residents: how parts of that system work, and what parts don’t. It demonstrates that the surveillance is real, even as it raises questions about the competence of its operators.

### **A Brief Window into China’s Digital Police State**

Earlier this month, Gevers discovered an [insecure MongoDB database](https://www.zdnet.com/article/chinese-company-leaves-muslim-tracking-facial-recognition-database-exposed-online/) filled with records tracking the location and personal information of 2.6 million people located in the Xinjiang Uyghur Autonomous Region. The records include individuals’ national ID number, ethnicity, nationality, phone number, date of birth, home address, employer, and photos.

Over a period of 24 hours, 6.7 million individual GPS coordinates were streamed to and collected by the database, linking individuals to various public camera streams and identification checkpoints associated with location tags such as “hotel,” “mosque,” and “police station.” The GPS coordinates were all located within Xinjiang.

This database is owned by the company [SenseNets](http://www.sensenets.com/home/), a private AI company advertising facial recognition and crowd analysis technologies.

A couple of days later, Gevers reported a second [open database](https://twitter.com/0xDUDE/status/1098088887153512448) tracking the movement of millions of cars and pedestrians. Violations like jaywalking, speeding, and going through a red-light are detected, trigger the camera to take a photo, and ping a WeChat API, presumably to try and tie the event to an identity.

### **Database Exposed to Anyone with an Internet Connection for Half a Year**

China may have a working surveillance program in Xinjiang, but it’s a shockingly insecure security state. Anyone with an Internet connection had access to this massive honeypot of information.

Gevers also found evidence that these servers were previously accessed by other known global entities such as a [Bitcoin ransomware actor](https://twitter.com/0xDUDE/status/1096514846714224640), who had left behind entries in the database. To top it off, this server was also vulnerable to [several known exploits](https://techcrunch.com/2019/02/19/when-surveillance-meets-incompetence/).

In addition to this particular surveillance database, a Chinese cybersecurity firm revealed that at least [468 MongoDB servers](http://www.cert.org.cn/publish/main/8/2019/20190222091237849303324/20190222091237849303324_.html) had been exposed to the public Internet after Gevers and [other](https://twitter.com/MayhemDayOne/status/1098971838766555138) security researchers started reporting them. Among these instances: databases containing detailed information about remote access consoles owned by [China General Nuclear Power Group](https://twitter.com/0xDUDE/status/1098088887153512448), and GPS coordinates of [bike rentals](https://twitter.com/0xDUDE/status/1098088887153512448).

### **A Model Surveillance State for China**

China, like many other state actors, may simply be willing to [tolerate sloppy engineering](https://techcrunch.com/2019/02/19/when-surveillance-meets-incompetence/) if its private contractors can reasonably claim to be delivering the goods. Last year, the government spent an extra $3 billion on [security-related construction](https://www.reuters.com/article/us-china-xinjiang/security-spending-soars-in-chinas-troubled-xinjiang-region-report-idUSKCN1NB0AT) in Xinjiang, and the New York Times reported that China’s police planned to spend an [additional $30 billion](https://www.nytimes.com/2018/07/08/business/china-surveillance-technology.html) on surveillance in the future. Even poorly-executed surveillance is massively expensive, and Beijing is no doubt telling the people of Xinjiang that these investments are being made in the name of their own security. But the truth, revealed only through security failures and careful security research, tells a different story: China’s leaders seem to care little for the privacy, or the freedom, of millions of its citizens.

## Related Issues:

[International](https://www.eff.org/issues/international)

[Surveillance and Human Rights](https://www.eff.org/issues/surveillance-human-rights)

## Join EFF Lists

### Join Our Newsletter!

Email updates on news, actions, events in your area, and more.

## Related Updates

[![](../_resources/6b92e1f174907b451f20f626ce081772.png)](https://www.eff.org/deeplinks/2019/02/whats-emergency-keeping-international-requests-law-enforcement-access-secure-and)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Katitza Rodriguez](https://www.eff.org/about/staff/katitza-rodriguez) | February 21, 2019

### [What’s the Emergency? Keeping International Requests for Law Enforcement Access Secure and Safe for Internet Users](https://www.eff.org/deeplinks/2019/02/whats-emergency-keeping-international-requests-law-enforcement-access-secure-and)

Law enforcement access to data is in the middle of a profound [shake-up](https://www.eff.org/deeplinks/2018/04/us-cloud-act-and-eu-privacy-protection-race-bottom)  [across the globe](https://www.eff.org/deeplinks/2018/04/tale-two-poorly-designed-cross-border-data-access-regimes). States are pushing to get quicker, deeper, and more invasive access to personal data stored on the global Internet, and are looking to water down the international safeguards around privacy and due...

[![](../_resources/aff53bf12f6cc5e733bf9b1b4550f9ac.png)](https://www.eff.org/deeplinks/2019/01/brazil-2019-free-speech-and-privacy-crosshairs-what-are-threats)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Veridiana Alimonti](https://www.eff.org/about/staff/veridiana-alimonti), Annie Harrison | January 31, 2019

### [Brazil in 2019: Free Speech and Privacy in the Crosshairs. What Are the Threats?](https://www.eff.org/deeplinks/2019/01/brazil-2019-free-speech-and-privacy-crosshairs-what-are-threats)

Last year’s Brazilian elections were a victory for Jair Bolsonaro—a politician with *[highly controversial positions](https://www.economist.com/leaders/2018/09/20/jair-bolsonaro-latin-americas-latest-menace)* on the country's past military dictatorship and civil rights. Bolsonaro’s ascent to power and the beginning*[of his administration](https://www.nytimes.com/2019/01/09/opinion/editorials/jair-bolsonaro-brazil-trump.html)* in January has *[attracted international attention](https://www.economist.com/the-americas/2018/11/03/are-brazilians-ready-for-jair-bolsonaros-radicalism)* for their potential impact on human rights...

[![](../_resources/bb9d0909db95e4ab3d48458cecd4a6bd.png)](https://www.eff.org/deeplinks/2019/01/article-13-and-11-update-even-compromises-are-compromised-copyright-trainwreck)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Danny O'Brien](https://www.eff.org/about/staff/danny-obrien-0) | January 18, 2019

### [Article 13 and 11 Update: Even The Compromises are Compromised In This Copyright Trainwreck](https://www.eff.org/deeplinks/2019/01/article-13-and-11-update-even-compromises-are-compromised-copyright-trainwreck)

*Update, January 18: EU ministers have failed to [approve the compromise text](https://juliareda.eu/2019/01/copyright-hits_wall/)—with **Germany, Belgium, Poland, Sweden, Luxembourg**, **the Netherlands, Finland** and **Slovenia**, **Italy, Croatia, ** and **Portugal** all voting against the current Article 13/11 proposal.* Keep up the pressure! If you’re in the Czech Republic, Luxembourg, Germany, Poland, Sweden...

[![](../_resources/bb9d0909db95e4ab3d48458cecd4a6bd.png)](https://www.eff.org/deeplinks/2018/12/year-gdpr-2018s-most-famous-privacy-regulation-review)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Danny O'Brien](https://www.eff.org/about/staff/danny-obrien-0) | December 28, 2018

### [The Year of the GDPR: 2018’s Most Famous Privacy Regulation in Review](https://www.eff.org/deeplinks/2018/12/year-gdpr-2018s-most-famous-privacy-regulation-review)

To the extent that 260-page regulations can ever be said to be “famous,” Europe’s General Data Protection Regulation (GDPR) certainly had its moment in limelight in 2018. When it came into force on May 25, it was heralded by a flurry of emails from tech companies, desperate to re-establish their...

[![](../_resources/deee6e0bc326336f9cee3b43a21aab10.png)](https://www.eff.org/deeplinks/2018/12/bloggers-and-technologists-whose-voices-are-offline-2018-review)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Jillian C. York](https://www.eff.org/about/staff/jillian-york) | December 26, 2018

### [Bloggers and Technologists Whose Voices Are Offline: 2018 in Review](https://www.eff.org/deeplinks/2018/12/bloggers-and-technologists-whose-voices-are-offline-2018-review)

This year, we refocused our attention on [Offline](https://eff.org/offline), our project that seeks to raise awareness of and provide actions readers can take to support imprisoned bloggers, digital activists, and technologists. Originally launched in 2015, Offline currently features six individuals from four countries whose critical voices have been silenced by...

[![](../_resources/f3661e44e678fe4cdf0bb6684a59c8fb.png)](https://www.eff.org/deeplinks/2018/12/who-has-your-back-colombia-fourth-annual-report-fuels-progress-and-asks-more)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Veridiana Alimonti](https://www.eff.org/about/staff/veridiana-alimonti) | December 18, 2018

### [Who Has Your Back in Colombia? Fourth-Annual Report Fuels Progress and Asks For More](https://www.eff.org/deeplinks/2018/12/who-has-your-back-colombia-fourth-annual-report-fuels-progress-and-asks-more)

[Fundación Karisma](https://karisma.org.co/), Colombia’s leading digital rights organization, just launched its fourth annual ¿Dónde Estan Mis Datos? report in collaboration with EFF. The results are even more encouraging than the ones seen[in 2017](https://www.eff.org/deeplinks/2017/11/donde-estan-mis-datos-en-colombia-nuestro-tercer-informe-anual-muestra-el-progreso), with significant improvement in transparency - five companies published transparency reports, and four publicly explained...

[![](../_resources/09cdb5fa70b9fe7247872b723d570bc7.png)](https://www.eff.org/deeplinks/2018/12/facing-criticism-all-sides-eus-terrible-copyright-amendments-stumble-new-year)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Cory Doctorow](https://www.eff.org/about/staff/cory-doctorow) | December 13, 2018

### [Facing Criticism from All Sides, EU’s Terrible Copyright Amendments Stumble into the New Year](https://www.eff.org/deeplinks/2018/12/facing-criticism-all-sides-eus-terrible-copyright-amendments-stumble-new-year)

Today, EU negotiators in Strasbourg struggled to craft the final language of the Copyright in the Single Digital Market Directive, in their last possible meeting for 2019. They failed, thanks in large part to the Directive’s two most controversial clauses: Article 11, which requires paid licenses for linking to news...

[![](../_resources/a307b742d1e9c2f9d54b35a97448b263.png)](https://www.eff.org/deeplinks/2018/12/human-rights-groups-sundar-pichai-listen-your-employees-and-halt-project-dragonfly)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Danny O'Brien](https://www.eff.org/about/staff/danny-obrien-0) | December 10, 2018

### [Human Rights Groups to Sundar Pichai: Listen to Your Employees and Halt Project Dragonfly](https://www.eff.org/deeplinks/2018/12/human-rights-groups-sundar-pichai-listen-your-employees-and-halt-project-dragonfly)

EFF, as part of a coalition of over sixty other human rights groups led by [Human Rights Watch](https://www.hrw.org/news/2018/12/10/5-questions-google-about-controversial-china-search-project) and Amnesty International —[still have questions for Sundar Pichai](https://www.hrw.org/news/2018/12/10/open-letter-response-google-project-dragonfly-china-and-human-rights), Google’s CEO. Leaks and rumors continue to spread from Google about “Project Dragonfly,” a secretive plan to create a censored, trackable...

[![](../_resources/bd96d2ad35c4b1709ceba9e1a7de2ecb.png)](https://www.eff.org/deeplinks/2018/10/italy-steps-defend-eu-internet-users-against-copyright-filters-who-will-be-next)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Danny O'Brien](https://www.eff.org/about/staff/danny-obrien-0) | October 23, 2018

### [Italy Steps Up To Defend EU Internet Users Against Copyright Filters – Who Will Be Next?](https://www.eff.org/deeplinks/2018/10/italy-steps-defend-eu-internet-users-against-copyright-filters-who-will-be-next)

The latest news from Brussels: Italy is not happy with Article 13 or Article 11, and wants them gone. What is going on with Europe’s meme-filtering Article 13 (and the hyperlink-meddling Article 11)? After the proposals sneaked over the finish line in a close European Parliamentary vote in July, the...

[![](../_resources/eb37f46a70e3d7330d117ec521aceae6.png)](https://www.eff.org/deeplinks/2018/10/canada-chile-security-researchers-have-rights-our-new-report)

[Deeplinks Blog](https://www.eff.org/updates?type=blog) by [Katitza Rodriguez](https://www.eff.org/about/staff/katitza-rodriguez) | October 16, 2018

### [From Canada to Argentina, Security Researchers Have Rights—Our New Report](https://www.eff.org/deeplinks/2018/10/canada-chile-security-researchers-have-rights-our-new-report)

EFF is introducing a new [Coders' Rights](https://www.eff.org/issues/coders) project to connect the work of security research with the fundamental rights of its practitioners throughout the Americas. The project seeks to support the right of free expression that lies at the heart of researchers' creations and use of computer code to...