The Google Cloud Platform won’t box you in

# The Google Cloud Platform won’t box you in

Openness is a core differentiator, says Sam Ramji

[John Dix (Network World)](https://www.techworld.com.au/author/314520926/john-dix/articles)12 May, 2017 05:11

- [8Like](http://www.facebook.com/sharer.php?u=http%3A//www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/&t=The%20Google%20Cloud%20Platform%20won%E2%80%99t%20box%20you%20in)
- [35share](http://www.linkedin.com/shareArticle?mini=true&url=http%3A//www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/&title=The%20Google%20Cloud%20Platform%20won%E2%80%99t%20box%20you%20in)
- [Tweet](http://twitter.com/share?text=The%20Google%20Cloud%20Platform%20won%E2%80%99t%20box%20you%20in&url=http%3A//www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/)
- [+1](https://plus.google.com/share?url=http%3A//www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/)
- [print](https://www.techworld.com.au/article/print/619166/google-cloud-platform-won-t-box/)
- [email](https://www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/mailto:?subject=The%20Google%20Cloud%20Platform%20won%E2%80%99t%20box%20you%20in&body=http%3A//www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/)

[0 Comments](https://www.techworld.com.au/article/619166/google-cloud-platform-won-t-box/#art-comments_619166)

*Sam Ramji, who joined Google about six months ago as VP of Product Management for Google Cloud Platform (GCP), has deep roots in open source:  He was the founding CEO of Cloud Foundry Foundation and he designed and led Microsoft's open source strategy.  Network World Editor in Chief John Dix sat down with Ramji at the recent Red Hat Summit in Boston to discuss how Google is trying to differentiate its cloud service.*

![Sam Ramji, VP of Product Management for Google Cloud Platform (GCP)](../_resources/cbec66a82f3542b8d7e44b400cab219e.jpg)  Google

*Sam Ramji, VP of Product Management for Google Cloud Platform (GCP)*
**How would you characterize where Google is at this point with cloud?**

I’d say we’re very serious about enterprise and you can see the changes we’ve made, from network connectivity to on-premise services or supporting a particular standard like HIPAA. We just got our ISO 27001 certification, which required an enormous amount of effort. It’s been a big shift over the last couple of years to focus on the regulatory needs of enterprises, to focus on security, last mile connectivity, etc. It’s a big change for us.

**What’s the near-term challenge?  Scaling it out, completing the stack, earning your enterprise chops?**

Gaining enterprise credibility is something we’re heavily focused on.  The path to that often comes through a third party, and that’s a new thing for Google to learn.  So, a company that’s spending $100 million dollars with Accenture would really like Accenture to know how to do this thing on Google Cloud Platform (GCP). Google has historically been such a direct company that mastering the art of enterprise support through indirect work is novel.

I think our other challenge is awareness.  We are very competitive in the deals we’re in, but some people are still like, “Google has a cloud?”  I say, “Yeah, we’re actually the third biggest provider on the planet.  It runs in our data centers that support YouTube and the search engine.  It works really well.”  They’re like, “I’ll be damned.  That’s pretty cool.  Tell me more.”

To get to that “Tell me more” hook they have to know you exist, so one of the big things we’re working on this year is marketing.  We’re getting very disciplined and attacking the marketing awareness problem at a much larger scale.

On the product side, it’s fit and finish.  You look at platform quality for the enterprise and it’s often, “Is this particular thing supported?  Is it easy to go from step one to step two, or is that kind of a doozy?  How do we smooth that curve?”

**So, in terms of footprint, Google Cloud services are supported out of the same data centers running the rest of the Google offerings?**

Yes.  We also build new data centers, so it’s a mix.  But another thing that most people don’t know is we’re a network company.  We route 25%-40% of the world’s Internet traffic.  We own the fiber.  We’re very serious about network engineering, so a lot of the value of using Google’s cloud is getting access to our network.  Point-to-point speeds between customer workloads and different data centers are incredibly high because they’re using our fiber.  The points of presence we’ve built to support all of our consumer businesses are used by our enterprise business as well.  We have hundreds of POPs around the world that we own and can provision hardware into. We can make sure the network is doing intelligent caching and we can handle ingress and egress in sensible ways.

**You folks put a priority on being open.  Is that a key point of differentiation for you?**

I think so.  In recent technology history, the last 15-plus years, open platforms have grown the fastest.

In cloud, you need a rigorous definition of what open is. Every platform has a supply side and a demand side and you have to keep bootstrapping each one.  The supply side is, what are the third parties who want to build and provision their services through your platform?  The demand side, is what customers think about using it.

[![computerworld_logo.png](../_resources/0d6c1e5ee42074e78fb12d8ecccb75b2.png)](https://www.surveymonkey.com/r/networkprofessionalsurvey)![brandpost_type.png](../_resources/629830f45fe2b3afe814fc1e3dcd7b6e.png)[Network Professionals Survey with Computerworld Australia](https://www.surveymonkey.com/r/networkprofessionalsurvey)

[More from Computerworld »](https://www.techworld.com.au/brand-post/137/computerworld/)

Openness ends up being very useful for bootstrapping on both sides.  We help third-party ISVs adopt GCP, but we don’t require they only use GCP.  Many of them also deploy on-premises.  In fact, many of them are leading open-source companies. DataStax, for example, is the dominant vendor of Cassandra, and EnterpriseDB is the dominant vendor of Postgres SQL.  They have their own businesses and can support multiple clouds.  We’re another option.

We believe strongly in this idea of open cloud being no barrier to entry, no barrier to exit, as well as this sense of contributing to open standards and making sure they have control over their workload.

The biggest thing we’ve contributed here is Kubernetes. The first version of the cloud was linearly siloed and based on Amazon Machine Image (AMI) virtual machines.  They don’t work anywhere else.  It says so right in the name.

The next version of the cloud that we’re getting into now is being built on containers.  Docker is a common format and runtime for that.  There are dozens of ways to do containers, but as soon as you have a container instead of a VM the rest of the game changes.  You have an opportunity to have a lot more portability, as long as you can standardize how those containers get operated.  The term we use is orchestration.

Kubernetes is a container orchestration system we invented at Google, that we use in the Google Cloud Platform, which we open-sourced and gave away to the community, including the trademark, and put it into an open source foundation.  That is a practical demonstration of open source, I think.  We’ll have to watch the next few years to see what happens with market share, but in this case users are getting more control over where their workloads can run because they can say, “I’m going to run that on OpenShift on-premises using Red Hat, or I’m going to run it in GCP, or I can run it on Amazon, or I can run it on Microsoft.  Microsoft recently acquired a company called Deis which has been a leading contributor to Kubernetes.

I’d go so far as to say you probably don’t use the cloud without using containers now, at least a little bit, and we think that over the next three or four years containers will be the dominant form of workload in the cloud.  In the long run, the more effective we are in contributing to Kubernetes, the more popular that is running on all the clouds.

**How would you compare Google’s openness to what Amazon and Microsoft are doing? Isn’t everyone saying we’re open, we’re embracing the latest and greatest?**

Embracing the latest and greatest technologies and including open technology and being an open cloud are really distinct things.  Take Linux.  Linux is an open technology, but you could have a highly proprietary, closed access cloud that runs entirely on Linux.  Using the technology doesn’t make you open.  It’s not recursive.

If you look at the acquisitions we’ve made over the last few years, I think you can start to see this path towards our belief that companies will want to run their computing everywhere.  Just to take a few specific acquisitions, Stackdriver, Orbitera, Apigee, Quiklabs even, are all multi-cloud.  They run on Amazon, they run on Google, they run on Microsoft, and Apigee also runs on-premises. Broadening the aperture and being applicable in all these environments is a very different stance from what you’re seeing from the other hyperscale providers.

Probably my favorite recent quote was from Jim Zemlin, the head of the Linux Foundation, which is a nonprofit foundation committed to keeping Linux and other open-source technologies open.  He said Kubernetes is the Linux of the cloud.  That feels pretty good.  That makes a lot of sense because, wherever that technology is at some point in the future we’ll have an opportunity to compete for the business.  In a world where the whole cloud is running containers, we like our chances.

**Are you guys known for a particular workload or in a particular vertical market?**

Probably our most popular workload is data analytics and, of course, the cherry on top is machine learning.  That’s one of the things that I think is high value for enterprises to offload, and they trust that Google is very, very good at data analytics because they know we run our entire business on technologies that we both invented and that we’ve offered to the world.

In terms of verticals, obviously we have an advantage in retail, but we see a lot of media entertainment, we see a lot of financial services.  We’re doing a lot of work in healthcare.  One of the things that helps us in healthcare is our infrastructure is so advanced that we were able to get a HIPAA VAA certificate for our entire infrastructure rather than having to cordon off particular machines and say, those are the machines that are certified.

**How about the typical size of customer organizations.  Is the profile changing?  I presume you were originally popular with smaller shops.**

It’s definitely changing. We’re really starting to lead with the large enterprises. At Next we announced that HSBC, which is one of the three largest banks in the world, is moving a substantial part of their workload to us from their data centers. Schlumberger is another great example.  They’re the number one contractor in the oil and gas industry so they generate a tremendous amount of data.

### Join the TechWorld newsletter!

More about [(L)](https://www.techworld.com.au/company//)[EnterpriseDB](https://www.techworld.com.au/company/enterprisedb/)[Google](https://www.techworld.com.au/company/google/)[HSBC](https://www.techworld.com.au/company/hsbc/)[ISO](https://www.techworld.com.au/company/iso/)[John Dix](https://www.techworld.com.au/company/john_dix/)[Linux](https://www.techworld.com.au/company/linux/)[Microsoft](https://www.techworld.com.au/company/microsoft/)[Red Hat](https://www.techworld.com.au/company/red_hat/)