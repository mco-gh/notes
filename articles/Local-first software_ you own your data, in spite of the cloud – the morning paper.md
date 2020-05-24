Local-first software: you own your data, in spite of the cloud – the morning paper

# Local-first software: you own your data, in spite of the cloud

[November 20, 2019](https://blog.acolyer.org/2019/11/20/local-first-software/) ~ [adriancolyer](https://blog.acolyer.org/author/adriancolyer/)

[Local-first software: you own your data, in spite of the cloud](https://martin.kleppmann.com/papers/local-first.pdf) Kleppmann et al., *Onward! ’19*

Watch out! If you start reading this paper you could be lost for hours following all the interesting links and ideas, and end up even more dissatisfied than you already are with the state of software today. You might also be inspired to help work towards a better future. I’m all in :).

### The rock or the hard place?

On the one-hand we have ‘cloud apps’ which make it easy to access our work from multiple devices and to collaborate online with others (e.g. Google Docs, Trello, …). On the other hand we have good old-fashioned native apps that you install on your operating system (a dying breed? See e.g. [Brendan Burns’ recent tweet](https://twitter.com/brendandburns/status/1194820433142374400?s=21)). Somewhere in the middle, but not-quite perfect, are online (browser-based) apps with offline support.

The primary issue with cloud apps (the SaaS model) is *ownership* of the data.
> ”

> Unfortunately, cloud apps are problematic in this regard. Although they let you access your data anywhere, all data access must go via the server, and you can only do the things that the server will let you do. In a sense, you don’t have full ownership of that data— the cloud provider does.

Services [do get shut down](https://ourincrediblejourney.tumblr.com/)[1](https://blog.acolyer.org/2019/11/20/local-first-software/#fn-9299-1), or pricing may change to your disadvantage, or the features evolve in a way you don’t like and there’s no way to keep using an older version.

With a traditional OS app[2](https://blog.acolyer.org/2019/11/20/local-first-software/#fn-9299-2) you have much more control over the data (the files on your file system at least, which if you’re lucky might even be in an open format). But you have other problems, such as easy access across all of your devices, and the ability to collaborate with others.

### Local-first software ideals

The authors coin the phrase “local-first software” to describe software that retains the ownership properties of old-fashioned applications, with the sharing and collaboration properties of cloud applications.

> ”

> In local-first applications… we treat the copy of the data on your local device — your laptop, tablet, or phone — as the primary copy. Servers still exist, but they hold secondary copies of your data in order to assist with access from multiple devices. As we shall see, this change in perspective has profound implications…

Great local-first software should have seven key properties.

1. **It should be fast.** We don’t want to make round-trips to a server to interact with the application. Operations can be handled by reading and writing to the local file system, with data synchronisation happening in the background.

2. **It should work across multiple devices.** Local-first apps keep their data in local storage on each device, but the data is also synchronised across all the devices on which a user works.

3. **It should work without a network.** This follows from reading and writing to the local file system, with data synchronisation happening in the background when a connection is available. That connection could be peer-to-peer across devices, and doesn’t have to be over the Internet.

4. **It should support collaboration.** “*In local-first apps, our ideal is to support real-time collaboration that is on par with the best cloud apps today, or better. Achieving this goal is one of the biggest challenges in realizing local-first software, but we believe it is possible.*“

5. **It should support data access for all time.** On one level you get this if you retain a copy of the original application (and an environment capable of executing it). Even better is if the local app using open / long lasting file formats. See e.g. the [Library of Congress recommended archival formats](https://www.loc.gov/preservation/resources/rfs/TOC.html).

6. **It should be secure and private by default.** “*Local-first apps can use end-to-end encryption so that any servers that store a copy of your files only hold encrypted data they cannot read*.”

7. **It should give the user full ownership and control of their data.** “*…we mean ownership in the sense of user agency, autonomy, and control over data. You should be able to copy and modify data in any way, write down any thought, and no company should restrict what you are allowed to do.*“

### How close can we get today?

Section 3 in the paper shows how a variety of different apps/technologies stack up against the local-first ideals.

![localfirst-table-1.jpeg](../_resources/5279420af5bf4e49de9253e025f7d6c8.jpg)

The combination of Git and GitHub gets closest, but nothing meets the bar across the board.

> ”

> … we speculate that web apps will never be able to provide all the local-first properties we are looking for, due to the fundamental thin-client nature of the platform. By choosing to build a web app, you are choosing the path of data belonging to you and your company, not to your users.

Mobile apps that use local storage combined with a backend service such as [Firebase and its Cloud Firestore](https://firebase.google.com/) take us closer to the local-first ideal, depending on the way the local data is treated by the application. CouchDB also gets an honourable mention in this part of the paper, only being let down by the difficulty of getting application-level conflict resolution right.

### CRDTs to the rescue?

> ”

> We have found some technologies that appear to be promising foundations for local-first ideals. Most notably the family of distributed systems algorithms called Conflict-free Replicated Data Types (CRDTs)… the special thing about them is that they are multi-user from the ground up… CRDTs have some similarity to version control systems like Git, except that they operate on richer data types than text files.

While most industrial usage of CRDTs has been in server-centric computing, the [Ink & Switch research lab](https://www.inkandswitch.com/) have been exploring how to build collaborative local-first client applications built on top of CRDTs. One of the fruits of this work is an open-source JavaScript CDRT implementation called [Automerge](https://github.com/automerge/automerge) which brings CRDT-style merge operations to JSON documents. Used in conjunction with the [dat:// networking stack](https://dat.foundation/) the result is [Hypermerge](https://github.com/automerge/hypermerge).

> ”

> Just as packet switching was an enabling technology for the Internet and the web, or as capacitive touchscreens were an enabling technology for smart phones, so we think CRDTs may be the foundation for collaborative software that gives users full ownership of their data.

### The brave new world

The authors built three (fairly advanced) prototypes using this CRDT stack: a Trello clone called [Trellis](https://github.com/automerge/trellis/releases), a collaborative drawing program, and a ‘mixed-media workspace’ called PushPin (Evernote meets Pinterest…).

If you have 2 minutes and 10 seconds available, it’s well worth watching this short [video showing Trellis in action](https://youtu.be/L9fdyDlhByM). It really brings the vision to life.

In section 4.2.4 of the paper the authors share a number of their learnings from building these systems:

- **CRDT technology works** – the Automerge library did a great job and was easy to use.
- **The user experience with offline work is splendid**.
- **CRDTs combine well with reactive programming** to give a good developer experience. “*The result of [this combination] was that all of our prototypes realized real-time collaboration and full offline capability with little effort from the application developer*.”
- In practice, **conflicts are not as significant a problem as we feared**. Conflicts are mitigated on two levels: first, Automerge tracks changes at a fine-grained level, and second, “*users have an intuitive sense of human collaboration and avoid creating conflicts with their collaborators*.”
- **Visualising document history is important** (see the Trellis video!).
- **URLs are a good mechanism for sharing**
- **Cloud servers still have their place for discovery, backup, and burst compute**.

Some challenges:

- **It can be hard to reason about how data moves between peers**.
- **CRDTs accumulate a large change history, which creates performance problems**. (This is an issue with state-based CRDTs, as opposed to operation-based CRDTs).

> ”

> Performance and memory/disk usage quickly became a problem because CRDTs store all history, including character-by-character text edits. These pile up, but can’t be easily truncated because it’s impossible to know when someone might reconnect to your shared document after six months away and need to merge changes from that point forward.

It feels like some kind of log-compaction with a history watermark (e.g., after n-months you might not be able to merge in old changes any more and will have to do a full resync to the latest state) could help here?

- **P2P technologies aren’t production ready yet** (but “feel like magic” when they do work).

### What can you do today?

You can take incremental steps towards a local-first future by following these guidelines:

- Use aggressive caching to improve responsiveness
- Use syncing infrastructure to enable multi-device access
- Embrace offline web application features (Progressive Web Apps)
- Consider [Operational Transformation](https://dl.acm.org/citation.cfm?doid=289444.289469) as the more mature alternative to CRDTs for collaborative editing
- Support data export to standard formats
- Make it clear what data is stored on device and what is transmitted to the server
- Enable users to back-up, duplicate, and delete some or all of their documents (outside of your application?)

I’ll leave you with a quote from section 4.3.4:
> ”

> If you are an entrepreneur interested in building developer infrastructure, all of the above suggests an interesting market opportunity: “Firebase for CRDTs.”

* * *

1. This link to ‘Our Incredible Journey’ handily provides a good example— it will take you first to a page announcing that [Tumblr has been acquired by Automattic](https://reclaimthenet.org/wordpress-automattic-buys-tumblr/), on which you can agree to the new terms of service should you wish. [![21a9.png](../_resources/b2661048e7467482154fb73607a9ecaf.png)](https://blog.acolyer.org/2019/11/20/local-first-software/#fnref-9299-1)

2. Not the new breed of OS apps that are really just wrapped browsers over an online service [![21a9.png](../_resources/b2661048e7467482154fb73607a9ecaf.png)](https://blog.acolyer.org/2019/11/20/local-first-software/#fnref-9299-2)

### Share this:

- [Twitter](https://blog.acolyer.org/2019/11/20/local-first-software/?share=twitter&nb=1)
- [LinkedIn](https://blog.acolyer.org/2019/11/20/local-first-software/?share=linkedin&nb=1)
- [Email](https://blog.acolyer.org/2019/11/20/local-first-software/?share=email&nb=1)
- [Print](https://blog.acolyer.org/2019/11/20/local-first-software/#print)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)

- [![fd47e6bba1f42ecacf2e7af9e4c5fb52](:/b36439ccd3ca14bafa7f590f17da7929)](https://en.gravatar.com/preslavrachev)
- [![fc0bf9568a426ef665bd3f422a574d9f](:/2160bec62a800d1969aefe5e68c30baa)](https://en.gravatar.com/akamaozu)
- [![da4101678b83abf35c0dc35834377192](../_resources/5e6f6963242b7fd2e32773a1cdb871c4.png)](https://en.gravatar.com/americaoncoffee)
- [![2787fb5d846cbdf70e15c9a48bd29ecd](../_resources/95c0ee369613cfe6706abfd9041c76b6.png)](https://en.gravatar.com/programmablesystems)
- [![d88d8f3026bd55f1c996712be0972348](../_resources/f5963a3360598e652dbd26d532822944.png)](https://en.gravatar.com/juliusgamanyi)

[5 bloggers](https://widgets.wp.com/likes/index.html?ver=20190321#) like this.

### *Related*

[Gray failure: the Achilles' heel of cloud-scale systems](https://blog.acolyer.org/2017/06/15/gray-failure-the-achilles-heel-of-cloud-scale-systems/)In "Distributed Systems"

[Declarative assembly of web applications from pre-defined concepts](https://blog.acolyer.org/2019/12/04/declarative-assembly-of-web-applications-from-pre-defined-concepts/)In "Software Engineering"

[How not to structure your database-backed web applications: a study of performance bugs in the wild](https://blog.acolyer.org/2018/06/28/how-_not_-to-structure-your-database-backed-web-applications-a-study-of-performance-bugs-in-the-wild/)In "Performance"

Posted in [Uncategorized](https://blog.acolyer.org/category/uncategorized/)[Distributed Systems](https://blog.acolyer.org/tag/distributed-systems/)[Software Engineering](https://blog.acolyer.org/tag/software-engineering/)