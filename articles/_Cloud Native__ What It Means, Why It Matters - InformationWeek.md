'Cloud Native': What It Means, Why It Matters - InformationWeek

# 'Cloud Native': What It Means, Why It Matters

"Cloud native" is starting to mean a set of specific things about how business will run on software, Cloud Foundry CEO Sam Ramji explains.

[![Why Cloud Security Beats Your Data Center](../_resources/9914747c9d1c9b3f075155fa79b4ccf1.jpg)](http://www.informationweek.com/cloud/infrastructure-as-a-service/why-cloud-security-beats-your-data-center/d/d-id/1321354)

Why Cloud Security Beats Your Data Center
*(Click image for larger view and slideshow.)*

When HP announced July 28 that it was [acquiring ActiveState's PaaS business](http://www.informationweek.com/cloud/platform-as-a-service/hp-buys-activestates-paas-stackato/d/d-id/1321519), senior vice president Bill Hilf said it was doing so in part to bridge the gap between traditional IT and "cloud-native applications."

The term "cloud-native applications" is not only finding its way more frequently into announcements, it's also gaining currency as a phrase that sums up where a lot of enterprise developers and operations staff think they are headed. "Cloud native" is not merely a buzzword; it's also enshrined in its own foundation -- the [Cloud Native Computing Foundation](https://cncf.io/news/announcement/2015/07/new-cloud-native-computing-foundation-drive-alignment-among-container), launched July 21.

For those unsure of what the term means, here's a primer on why it's the term du jour and why it's often used to sum up a set of goals and priorities that used to be the province of a Google or Facebook.

[![(Image: Andrey Prokhorov/iStockphoto)](../_resources/a5ba3836d5a0ddf553fbf6805bf53977.jpg)](https://www.informationweek.com/cloud/platform-as-a-service/cloud-native-what-it-means-why-it-matters/d/d-id/1321539?image_number=1)

(Image: Andrey Prokhorov/iStockphoto)

At the heart of "cloud-native" lie Linux, Linux containers, and the concept of applications assembled as microservices in containers. Indeed, the Linux Foundation launched the Cloud Native Computing Foundation. But cloud-native means a lot more than implementing Linux clusters and running containers. It's a term that recognizes that getting software to work in the cloud requires a broad set of components that work together. It also requires an architecture that departs from traditional enterprise application design. The Cloud Native Computing Foundation is going to try to make it simpler to assemble these moving parts.

**[Want to learn more about containers? See [Docker Adds Container Networking, Deployment Options](http://www.informationweek.com/cloud/docker-adds-container-networking-deployment-options/d/d-id/1320996?itc=edit_in_body_cross).]**

That task is daunting enough that Sam Ramji, CEO of the Cloud Foundry Foundation, gave a talk on the meaning of "cloud-native" during the annual [Open Source Convention](http://www.oscon.com/) (OSCON) held July 20-24. Ramji is a veteran of fitting dissimilar parts together, having once lead Microsoft's internal efforts at coordinating its code base with open source code and contributing to open source projects. If nothing else, that qualifies him to explain how to avoid some of the pitfalls of what constitutes cloud native.

The Cloud Native Computing Foundation was launched on the heels of the Open Container Initiative, announced June 22, a seemingly overlapping group. Ramji kept hearing people ask why there are so many foundations and how the technologies work together, so he rewrote his OSCON address to answer those questions. And as a result, he said, "I've gotten some of the most positive feedback of any talk I've ever given."

Here are some of the points he made.

1. Cloud computing relies heavily on open source code; open source has won out over commercial code for next-generation applications, even inside the enterprise. Promising open source projects attract venture capital which encourages a project to form a company that wraps itself around the code and starts to monetize it. "We used to share code, improve it, and build it for reputation's sake," Ramji said in his OSCON keynote. Now an open source project can be an element of competition between startup companies and contributing companies who want to be able to adopt it for their own advantage. Foundations are formed when a project becomes so important that multiple vendors are willing to back it, provided no single one of them controls it. All participants want to move the code to a neutral plane, where they can share in it without one gaining control or competitive advantage. The growth of open source foundations is a result of the larger, direct role that startup economics tends to play in a project without multiple vendors, said Ramji.

2. One example is Docker, the Linux container company. "Docker has taken over the world," and its success generated unease among developers with other ideas for containers, leading to the well-known competition between Docker and CoreOS's Rocket. IT managers told Ramji they would have to conduct a nine-month project to figure out which one to use. He responded, "that doesn't sound fast" in a business world that has to constantly adjust to changing conditions. "Sometimes competition leads to innovation and sometimes it gets destructive," he told the OSCON attendees. Companies don't want to get bogged down in deciding between competing open source projects. On June 22, Docker and CoreOS both got behind the Open Container Initiative  and agreed to adhere to a common container file format and a common runtime to simplify future tasks for enterprise container adopters.

3. The drive of open source projects today is not simply to create an alternative to commercial code. It's now driven by the need for "continuous innovation," by business needs that can be adapted with frequent software adjustments in any week or even through the space of a day. "Zynga used to say they deployed code 40 times a day. Now Amazon says it deploys code every seven seconds. Why do we do it? We do it to run in the cloud, to connect to any device," to constantly update applications in the cloud to adjust to business needs, Ramji said. There can't be continuous innovation if developers and operations staffs spend much of their time trying to figure out how open source code components will work together. Cloud Foundry, Docker, Kubernetes (the Google-spawned container orchestration system), Mesos (container cluster management used by Twitter, Apple, and Airbnb) and other container projects have continuous innovation as their underlying goal. "If we can bring it all together, if we can work to harmonize Kubernetes and Mesos together, we can re-imagine schedulers as plug-ins," Ramji continued, and use them as they're needed.

4. Single-vendor open source projects won't behave in this fashion. They'll be run by developers who have been given stock options by venture capitalists to press their momentary advantage. Only multi-vendor projects that are creating a new platform or set of components that work together will have the chance to grow into both a major project and a major force for change in cloud usage, he predicted.

5. Cloud-native applications are meant to function "in a world of cloud computing that is ubiquitous and flexible." Applications can be developed on a cloud platform, then deployed to different clouds where supporting software stacks will help them run at scale.

6. Cloud-native applications amount to "prescriptive software stacks" designed to work together for enterprises that are too busy to assemble components themselves, Ramji concluded. To get there, companies will build microservices -- discrete application services -- each running in its own container, then connect them via a network to build the application they want. Cloud native means "rebalancing the roadmap toward user-driven systems" that use standardized parts and follow standardized deployment and operational procedures.

[![imgad.jpg](../_resources/486a713f6d550826f7f718e23a80deda.jpg)](http://adclick.g.doubleclick.net/pcs/click%253Fxai%253DAKAOjss4iV5C-ZCh4JwXZsD3cl_OKwhDK7oYHcCDc2K6QVvhsQxwyV4cTnBv5Kddk5jqQ8WmILMJsZCZ2bQVnjXBU1F1wSAgL6r1D1LBgfO0XPRm-Rmk3AQU4FzUuCiidkolPizljd1kj56iPQkI91Lyt9jECwgLEPryX0srivyJVHz1UByQVrsS_oapfH-rkEnRNJzksHIgRxXpgx94AFIZAedn_ai4NqmaiHbaKCXomeB8Wizzw0X6W8nXPpTJ1kbY35mRJK2P31Uix8soIJFkZZlhL0ylLjv0%2526sig%253DCg0ArKJSzPLq31NWbovYEAE%2526urlfix%253D1%2526adurl%253Dhttp://allanalytics.com/lecture.asp%3Fdoc_id%3D282466%26cid%3Dmp_iw_natvad)

Sponsored Content

[Today's Tech Challenges: AI Machines, Humans, & Moral Dilemmas](http://adclick.g.doubleclick.net/pcs/click%253Fxai%253DAKAOjss4iV5C-ZCh4JwXZsD3cl_OKwhDK7oYHcCDc2K6QVvhsQxwyV4cTnBv5Kddk5jqQ8WmILMJsZCZ2bQVnjXBU1F1wSAgL6r1D1LBgfO0XPRm-Rmk3AQU4FzUuCiidkolPizljd1kj56iPQkI91Lyt9jECwgLEPryX0srivyJVHz1UByQVrsS_oapfH-rkEnRNJzksHIgRxXpgx94AFIZAedn_ai4NqmaiHbaKCXomeB8Wizzw0X6W8nXPpTJ1kbY35mRJK2P31Uix8soIJFkZZlhL0ylLjv0%2526sig%253DCg0ArKJSzPLq31NWbovYEAE%2526urlfix%253D1%2526adurl%253Dhttp://allanalytics.com/lecture.asp%3Fdoc_id%3D282466%26cid%3Dmp_iw_natvad)

No sooner do machine learning and Artificial Intelligence (AI) enter the more mainstream marketplace than questions begin to arise about whether these technologies are making things better or are they contributing to society's problems?

Sponsored By SAS

Its proponents will still need to provide more examples of how this set of ideas works in practice, but "cloud native" will enable a constantly shifting software infrastructure that keeps companies oriented toward their customers and able to compete. Since 2000, 52% of the Fortune 500 has turned over, Ramji noted. Continuous innovation and deployment of fresh software is one of the few measures that will keep a company from becoming the next to drop off the list.

For more on Ramji's keynote, view his [slides](http://www.slideshare.net/CloudFoundryFoundation/cloud-foundry-ceo-sam-ramji-2015-oscon-keynote) on SlideShare or a [video of his talk](https://www.linkedin.com/pulse/cloud-native-foundry-docker-kubernetes-sam-ramji) he published on LinkedIn.

*Charles Babcock is an editor-at-large for InformationWeek and author of Management Strategies for the Cloud Revolution, a McGraw-Hill book. He is the former editor-in-chief of Digital News, former software editor of Computerworld and former technology editor of Interactive ... [View Full Bio](http://www.informationweek.com/author-bio.asp?author_id=115)*

[Comment](http://www.informationweek.com/cloud/platform-as-a-service/cloud-native-what-it-means-why-it-matters/d/d-id/1321539#msgs)  |

[Email This](#)  |

[Print](http://www.informationweek.com/cloud/platform-as-a-service/cloud-native-what-it-means-why-it-matters/d/d-id/1321539?print=yes)  |

[RSS](http://www.informationweek.com/rss_simple.asp)

INSIGHTS  Sponsored Content

![1568176135_5456272549001_5456266357001-vs.jpg](../_resources/6044d6b627dc162fed0033f1bb5675fd.jpg)

[Change and Community in Analytics](http://adclick.g.doubleclick.net/pcs/click%253Fxai%253DAKAOjst0_AvDV1zswuGziEdt5nnrSWbi2-rpgfxzFIm5qc7oOzoZgLAIeMTq2oWMTw8PhMcb6HAN8YRoWVSrV953KpJr1lU88kofyS2egeGCxyl-832LRQaEtXVciB7tmHDpfEk4eyKgDqQYTB_qpUvlNQ3feWPgo88mzJvq8VVe8wk7W5lxYhshBk7_UiaoDJ8kHGVWjNFJtVHUUfZMvqDN3QfwufGYUyAPMewx-WcmgoueAWWZe2mpV_lX71IyWo5G_IfVg7mdlhCJNLkoXx7k3FqGAXaWNFT1%2526sig%253DCg0ArKJSzB5WJ43B5Yh7EAE%2526urlfix%253D1%2526adurl%253Dhttp://www.informationweek.com/big-data/change-and-community-in-analytics/v/d-id/1328942)

Pierre DeBois, Founder of Zimana Analytics stops by the InformationWeek News Desk to share his experience writing for All Analytics, and what he's learned by being a part of this online analytics community.

[Learn More](http://adclick.g.doubleclick.net/pcs/click%253Fxai%253DAKAOjst0_AvDV1zswuGziEdt5nnrSWbi2-rpgfxzFIm5qc7oOzoZgLAIeMTq2oWMTw8PhMcb6HAN8YRoWVSrV953KpJr1lU88kofyS2egeGCxyl-832LRQaEtXVciB7tmHDpfEk4eyKgDqQYTB_qpUvlNQ3feWPgo88mzJvq8VVe8wk7W5lxYhshBk7_UiaoDJ8kHGVWjNFJtVHUUfZMvqDN3QfwufGYUyAPMewx-WcmgoueAWWZe2mpV_lX71IyWo5G_IfVg7mdlhCJNLkoXx7k3FqGAXaWNFT1%2526sig%253DCg0ArKJSzB5WJ43B5Yh7EAE%2526urlfix%253D1%2526adurl%253Dhttp://www.informationweek.com/big-data/change-and-community-in-analytics/v/d-id/1328942)

More Insights

Webcasts

[Securing Your Endpoints from Ransomware & Other Trending Attacks](https://webinar.darkreading.com/2363?keycode=sbx&cid=smartbox_techweb_webcast_8.500000746)

[Open Source: The Benefits & Challenges](https://webinar.informationweek.com/3258?keycode=sbx&cid=smartbox_techweb_webcast_8.500000745)

[More Webcasts](http://www.informationweek.com/webinar_upcoming.asp)
White Papers

[[Cloud Infrastructure] Top 5 Things You Need to Know Before You Build or Upgrade](http://www.informationweek.com/whitepaper/data-centers/networking/top-five-things-you-need-to-know-before-building-or-upgrading-your-cloud-infrastructure/380823?cid=smartbox_techweb_whitepaper_14.500002803)

[Need to Accelerate DevOps Delivery Cycles? Find Out How](http://www.informationweek.com/whitepaper/applications/network-and-systems-management/how-to-accelerate-devops-delivery-cycles/389613?cid=smartbox_techweb_whitepaper_14.500002882)

[More White Papers](http://www.informationweek.com/whitepaper)
Reports

[Guide to DevOps: Continuous Delivery & Automation](http://www.informationweek.com/whitepaper/applications/network-and-systems-management/the-dzone-guide-to-devops-continuous-delivery-and-automation/389693?cid=smartbox_techweb_analytics_7.300005729)

[Low Latency Data Center Interconnect Using Infinera & Arista](http://www.informationweek.com/whitepaper/data-centers/networking/research-report-low-latency-data-center-interconnect-using-infinera-and-arista/388503?cid=smartbox_techweb_analytics_7.300005725)

[More Reports](http://www.informationweek.com/whitepaper/company/detail/109)