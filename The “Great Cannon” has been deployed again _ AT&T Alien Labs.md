The “Great Cannon” has been deployed again | AT&T Alien Labs

**Summary**

The [Great Cannon](https://citizenlab.ca/2015/04/chinas-great-cannon/) is a distributed denial of service tool (“DDoS”) that operates by injecting malicious Javascript into pages served from behind the [Great Firewall](https://en.wikipedia.org/wiki/Great_Firewall). These scripts, potentially served to millions of users across the internet, hijack the users’ connections to make multiple requests against the targeted site. These requests consume all the resources of the targeted site, making it unavailable:

[great-cannon-1.webp](../_resources/b5e56b564161adad803f48e0b1333167.webp)
**Figure 1:** Simplified diagram of how the Great Cannon operates

The Great Cannon was the subject of intense research after it was used to [disrupt access](https://www.theguardian.com/technology/2015/apr/13/great-cannon-china-internet-users-weapon-cyberwar) to the website Github.com in 2015. Little has been seen of the Great Cannon since 2015. However, we’ve recently observed new attacks, which are detailed below.

**Most recent attacks against LIHKG**

The Great Cannon is currently attempting to take the website [LIHKG](https://en.wikipedia.org/wiki/LIHKG) offline. LIHKG has been used to organize protests in Hong Kong. Using a [simple script](https://gist.github.com/chrisdoman/0555e2bdacbbba4ac6596ded74b9a80a) that uses data from [UrlScan.io](https://urlscan.io/), we identified new attacks likely starting Monday November 25th, 2019.

[Websites](https://urlscan.io/result/fe2c1bd6-f717-439e-b785-1208d290bb34/#transactions) are indirectly serving a malicious javascript [file](https://otx.alienvault.com/indicator/file/df28c245c720b66cace9ac6433debffb2186b67c9d6fd3320df374513dadb857) from either:

- http://push.zhanzhang.baidu.com/push.js; or
- http://js.passport.qihucdn.com/11.0.1.js

Normally these URLs serve standard analytics tracking scripts. However, for a certain percentage of requests, the Great Cannon swaps these on the fly with malicious code:

[great-cannon-4.webp](../_resources/bac6a3b7ddca9ed99b10e487ad31b019.webp)

**Figure 2: **[Malicious code](https://urlscan.io/responses/df28c245c720b66cace9ac6433debffb2186b67c9d6fd3320df374513dadb857/) served from the Great Cannon

The code attempts to repeatedly request the following resources, in order to overwhelm websites and prevent them from being accessible:

- http://lihkg.com/
- https://i.loli.net/2019/09/29/hXHglbYpykUGIJu.gif?t=
- https://na.cx/i/XibbJAS.gif?t=
- https://na.cx/i/UHr3Dtk.gif?t=
- https://na.cx/i/9hjf7rg.gif?t=
- https://na.cx/i/qKE4P2C.gif?t=
- https://na.cx/i/0Dp4P29.gif?t=
- https://na.cx/i/mUkDptW.gif?t=
- https://na.cx/i/ekL74Sn.gif?t=
- https://i.ibb.co/ZBDcP9K/LcSzXUb.gif?t=
- https://66.media.tumblr.com/e06eda7617fb1b98cbaca0edf9a427a8/tumblr_oqrv3wHXoz1sehac7o1_540.gif?t=
- https://na.cx/i/6hxp6x9.gif?t=
- https://live.staticflickr.com/65535/48978420208_76b67bec15_o.gif?t=
- https://i.lihkg.com/540/https://img.eservice-hk.net/upload/2018/08/09/181951_60e1e9bedea42535801bc785b6f48e7a.gif?t=
- https://na.cx/i/E3sYryo.gif?t=
- https://na.cx/i/ZbShS2F.gif?t=
- https://na.cx/i/LBppBac.gif?t=
- http://i.imgur.com/5qrZMPn.gif?t=
- https://na.cx/i/J3q35jw.gif?t=
- https://na.cx/i/QR7JjSJ.gif?t=
- https://na.cx/i/haUzqxN.gif?t=
- https://na.cx/i/3hS5xcW.gif?t=
- https://na.cx/i/z340DGp.gif?t=
- https://luna.komica.org/23/src/1573785127351.gif?t=
- https://image.ibb.co/m10EAH/Atsps_Smd_Pc.gif?t=
- https://img.eservice-hk.net/upload/2018/06/02/213756_d33e27ec27b054afcc911be1411b5e5a.gif?t=
- https://media.giphy.com/media/9LZTc9dQjAAL5jmuCK/giphy.gif?t=
- https://img.eservice-hk.net/upload/2018/06/13/171314_55de6aac9af0e3c086b83bf433493004.gif?t=
- https://i.lih.kg/540/https://i.lihkg.com/540/

These may seem like an odd selection of websites and memes to target, however these meme images appear on the LIHKG forums so the traffic is likely intended to blend in with normal traffic. The URLs are appended to the LIHKG image proxy url (eg; https://na.cx/i/6hxp6x9.gif becomes  https://i.lih.kg/540/https://na.cx/i/6hxp6x9.gif?t=6009966493) which causes LIHKG to perform the bandwidth and computationally expensive task of taking a remote image, changing its size, then serving it to the user.

**Impact**

It is unlikely these sites will be seriously impacted. Partly due to LIHKG sitting behind an anti-DDoS service, and partly due to some bugs in the malicious Javascript code that we won’t discuss here.

Still, it is disturbing to see an attack tool with the potential power of the Great Cannon used more regularly, and again causing collateral damage to US based services.

**Mitigations**

These attacks would not be successful if the following resources were served over HTTPS instead of HTTP:

- http://push.zhanzhang.baidu.com/push.js; or
- http://js.passport.qihucdn.com/11.0.1.js

You may want to consider blocking these URLs when not sent over HTTPS.
**Timeline of historical Great Cannon incidents**

Below we have described previous Great Cannon attacks, including previous attacks against LIHKG in September 2019.

**2015: GreatFire and GitHub**

During the 2015 attacks, DDoS scripts were sent in response to requests sent to a [number of domains](https://drive.google.com/file/d/0ByrxblDXR_yqeUNZYU5WcjFCbXM/view), for both Javascript and HTML pages served over HTTP from behind the Great Firewall.

A number of distinct stages and targets were identified:

- March 3 to March 6, 2015: Initial, [limited test firing](https://security.googleblog.com/2015/04/a-javascript-based-ddos-attack-as-seen.html) of the Great Cannon starts.
- March 10: Real attacks start against a Chinese-language news site (Sinasjs.cn).
- March 13: New attacks against an organization that monitors censorship (GreatFire.org).

[great-cannon-6.webp](../_resources/0db994a9f58f583fde0d050e1f7ed33a.webp)

**Figure 3:** Snippet of the code used in early Great Cannon attacks. Later scripts were improved to not require external Javascript libraries.

- March 25: Attacks against GitHub.com start, targeting content hosted from the site GreatFire.org and a Chinese edition of the New York Times. This resulted in a [global outage](https://threatpost.com/ddos-attack-on-github-linked-to-earlier-one-against-greatfire-org/111919/) of the GitHub service.

[great-cannon-2.webp](../_resources/02d73aa9813daf627e288a22257bb589.webp)
**Figure 4:** The URLs targeted in the attack against Github.com.

- March 26th - Attacks began using code hidden with the Javascript obfuscator “[packer](http://dean.edwards.name/packer/)”:

[great-cannon-3.webp](../_resources/0e2122c3b5feba644b1a686d1c89a9d4.webp)

**Figure 5:** Snippet of the obfuscated code. Current attacks continue to use the same obfuscation.

Research by [CitizenLab](https://citizenlab.ca/2015/04/chinas-great-cannon/) identified multiple likely points where the malicious code is injected. The Great Cannon operated probabilistically, injecting return packets to a certain percentage of requests for Javascript from certain IP addresses. As noted by commentators at the time, the same functionality could also be used to insert exploitation code to enable “[Man-on-the-side](https://en.wikipedia.org/wiki/Man-on-the-side_attack)” attacks to compromise key targets.

**2017 and onward: attacks against Mingjingnews**

In August 2017, Great Cannon attacks against a Chinese-language news website ([Mingjingnews.com](https://en.wikipedia.org/wiki/Duowei_News)) were [identified](https://stackoverflow.com/questions/45874555/what-is-randomly-replacing-baidu-tongji-analyticss-javascript-code-to-make-dd) by a user on Stack Overflow. The code in the 2017 attack is significantly re-written and is largely unchanged in the attacks seen in 2019.

[great-cannon-7.webp](../_resources/e7334c68932eb7da4fb85d38cff3beab.webp)
**Figure 6:** An excerpt of the code to target Mingjingnews.com in 2017.

We have continued to see [attacks against](https://urlscan.io/result/3fd5a719-24d9-42cd-ae10-87129ad87fd1/#transactions) Mingjingnews in the last year.

**2019: Attacks against Hong Kong democracy movement**

On August 31, 2019, the Great Cannon [initiated](https://globalvoices.org/2019/09/06/hong-kong-reddit-like-lihkg-faces-unprecedented-ddos-attacks-redirected-from-chinese-internet-companies/) an attack against a website (lihkg.com) used by members of the Hong Kong democracy movement to plan protests.

The Javascript code is very similar to the packer code used in the attacks against Mingjingnews observed in 2017 and onward, and the code was served from at least two locations:

- http://push.zhanzhang.baidu.com/push.js
- http://js.passport.qihucdn.com/11.0.1.js

Initial versions targeted a single page on lihkg.com.
[great-cannon-8.webp](../_resources/3c17b9ab8a9e9ac30d185a000ed308b7.webp)
**Figure 7:** The Javascript code originally targeting lihkg.com.

Later versions targeted multiple pages and attempted (unsuccessfully) to bypass DDoS mitigations that the website owners had implemented.

[great-cannon-5.webp](../_resources/c90b231cd1d287e7e07d8f1a4eecfb83.webp)
**Figure 8:** The Javascript code later targeting lihkg.com.
**Detection**

We detect the Great Cannon serving malicious Javascript with the following Suricata rules from AT&T Alien Labs and Emerging Threats Open.

alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"AV INFO JS File associated with Great Cannon DDoS"; flow:to_server,established; content:"GET"; http_method; content:"push.js"; http_uri; content:"push.zhanzhang.baidu.com"; http_host; flowbits:set,AVCannonDDOS; flowbits:noalert; classtype:misc-activity; sid:4001470; rev:1;)

alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"AV INFO JS File associated with Great Cannon DDoS"; flow:to_server,established; content:"GET"; http_method; content:"11.0.1.js"; http_uri; content:"js.passport.qihucdn.com"; http_host; flowbits:set,AVCannonDDOS; flowbits:noalert; classtype:misc-activity; sid:4001471; rev:1;)

alert http $EXTERNAL_NET any -> $HOME_NET any (msg:"AV INFO Potential DDoS attempt related to Great Cannon Attacks"; flow:established,to_client; content:"200"; http_stat_code; file_data; content:"isImgComplete"; flowbits:isset,AVCannonDDOS; reference:url,otx.alienvault.com/pulse/5d6d4da02ee2b6fbff703067; classtype:policy-violation; sid:4001473; rev:1;)

alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"AV INFO JS File associated with Great Cannon DDoS"; flow:to_server,established; content:"GET"; http_method; content:"hm.js"; http_uri; content:"hm.baidu.com"; http_host; flowbits:set,AVCannonDDOS; flowbits:noalert; classtype:misc-activity; sid:4001472; rev:1;)

ET WEB_CLIENT Great Cannon DDoS JS M1 sid:2027961
ET WEB_CLIENT Great Cannon DDoS JS M2 sid:2027962
ET WEB_CLIENT Great Cannon DDoS JS M3 sid:2027963
ET WEB_CLIENT Great Cannon DDoS JS M4 sid:2027964

Additional indicators and code samples are available in the Open Threat Exchange [pulse](https://otx.alienvault.com/pulse/5d6d4da02ee2b6fbff703067).

[![avatar_159_2.jpg](../_resources/0f25aca8f096145422fb26318d2c1db8.jpg)](https://cybersecurity.att.com/blogs/author/chris-doman)

**About the Author:**  Chris Doman, AlienVault

I've had a long interest in security, but joined the industry after winning the civilian section of the Department of Defense's forensics competition. I run a popular threat intelligence portal (ThreatCrowd.org) in my spare time, and hold a CCHIA (Certified Host Intrusion Analyst) from CREST and a degree in Computer Science from the University of Cambridge.

[Read more posts from Chris Doman ›](https://cybersecurity.att.com/blogs/author/chris-doman)

TAGS: [ddos](https://cybersecurity.att.com/blogs/tag/ddos), [great cannon](https://cybersecurity.att.com/blogs/tag/great+cannon)

[(L)](https://cybersecurity.att.com/blogs/tag/great+cannon)

[(L)](https://cybersecurity.att.com/blogs/tag/great+cannon)[‹ BACK TO ALL BLOGS](https://cybersecurity.att.com/blogs/labs-research)