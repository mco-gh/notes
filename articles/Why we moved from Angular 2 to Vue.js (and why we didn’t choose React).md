Why we moved from Angular 2 to Vue.js (and why we didn’t choose React)

# Why we moved from Angular 2 to Vue.js (and why we didn’t choose React)

By Luis Elizondo

![](../_resources/d2e8495df8cd054e1e22a58b60f2c855.png)![1*PHmNXbvOfg5AHiMWWuaRXg.jpeg](../_resources/a19a86ce76d85c97c196f1a9e6042561.jpg)

At Rever (www.reverscore.com) we just released a new version of our web client using Vue.js. 641 commits and 16 weeks of intense development after with two resources, here we are, very proud of a decision we took a while ago.

8 months ago our web client was using Angular 2. To be precise, it was using Angular 2 beta 9. This was a product written by an outsourcing company and we were never fully happy with it on many levels, from UX/UI to the architecture, and to some level, with Angular 2 itself.

Before I continue, I admit that Angular 2 beta 9 is a different product than Angular 2.0, but that was exactly one of the problems. From beta9 to 2.0.0 there are 8 beta versions, 8 RC and the 2.0.0 version itself, 17 versions to upgrade in total. We did try to upgrade from beta 9 to 2.0.0 but too many things broke that made the upgrade non trivial. Also, about the same time we were questioning Angular 2 as our framework of choice, the Angular team decided to start working on Angular 4. While they promised it wouldn’t be too drastic, that meant that by the time we finished upgrading to Angular 2.0.0 we were going to need another upgrade. What a waste of time and limited resources.

The main thing we didn’t like and we still don’t like about Angular 2 is Typescript. I know Angular 2 can be used with Javascript but again, the decision to use Typescript was already taken and from what I understand, using pure Javascript with Angular 2 is not the ideal way you should be using Angular 2. In any case, getting rid of Typescript meant a full rewrite of the project.

I didn’t feel Typescript added substantial value and even worse, we noticed that our coding speed was reduced. With Typescript things that were really easy to do on Javascript like defining a simple object were more complicated to do on Typescript. I highly recommend you to read the following articles before you start using Typescript. It is not the right solution for everyone.

[**The Shocking Secret About Static Types** *The popularity of TypeScript has really exploded recently. I like TypeScript, and I like static types. I don’t use…*medium.com](https://medium.com/javascript-scene/the-shocking-secret-about-static-types-514d39bf30a3)[(L)](https://medium.com/javascript-scene/the-shocking-secret-about-static-types-514d39bf30a3)

[**Angular 2 vs React: The Ultimate Dance Off** *Most people who follow me know that I personally favor React, but of course I like my decisions to be educated, not…*medium.com](https://medium.com/javascript-scene/angular-2-vs-react-the-ultimate-dance-off-60e7dfbc379c)[(L)](https://medium.com/javascript-scene/angular-2-vs-react-the-ultimate-dance-off-60e7dfbc379c)

I still remember how easy to work with Angular 1 was, it certainly had it’s own problems, but it was nice to work with it compared to other frameworks, something that Angular 2 lost somewhere on the way. My conclusion about Angular 2 was simple**, the only thing Angular 1 and 2 share in common is the name, they are completely different frameworks.**

So consider that we had 17 versions to upgrade on a non-tested system, a lot of pressure from the business to write new features, lots of bugs and poorly written code, the original developers weren’t on the team anymore, only one developer (me) at the time with many other responsibilities, Typescript, problems with finding the right documentation since I was using a beta, and Angular 2 moving to version 4. The list of negatives started to accumulate very rapidly.

We made a decision, if we were going to spend that much time upgrading, we needed to see if we had other options first. And we did.

### **React**

The first obvious choice was react, because well, everybody is doing it and the ones who are not, are talking about it. So that was one option, certainly knowing that Facebook is behind it, helps. However, React itself is not a framework, you need to add extra stuff to make it shine.

### **Vue.js**

Vue.js was a new player, I never heard about it before although they just released version 2 back when we started to look at different options. At first it caught our attention, but it looked risky.

**Decision process**

We first started to define what our decision points were going to be. We knew the framework of our dreams would need to have the following:

1. 1It should be stable
2. 2Backed by a strong community or some big players
3. 3Good documentation or lots of questions on StackOverflow
4. 4Easy to learn
5. 5Integration with Bootstrap
6. 6Small size
7. 7Ideally it would allow us to reuse code
8. 8Coding speed test should be increased
9. 9Reactivity
10. 10Component based

After having our decision points decided, I had to get my hands dirty, so I gave both React and Vue.js a couple of days each to review each decision point that wasn’t going to be answered by Google. Since I knew nothing about any of them, at the end of two days I would reevaluate how far I got into rewriting some parts of the actual project we were going to migrate.

The parts I chose to rewrite were:
1. 1Some basic API calls
2. 2Two layouts for two different pages.
3. 3Reactivity for user related stuff
4. 4Login Forms and some content forms
5. 5One bootstrap modal

I was surprised by how far I got with Vue.js, in a couple of days I actually had a proof of concept to show up to the rest of the team and to my CTO. I got a good understanding of the basic concepts of Vue.js, defined a good and extendable architecture but most importantly I really enjoyed the experience of writing code with it and I felt I was doing it faster that with React.

React was a lot harder than I thought, choosing between Redux and MobX is more problematic than having one option that is well integrated with the framework like Vue.js and Vuex do. This is simple because when having no experience with a framework, it gives you more confidence knowing that a framework has an official library for doing something. By the way, I felt that reactivity was easier with Vuex than with Redux but probably that’s just a perception, like all learning curves.

JSX was also a problem since we could not reuse HTML code and Vue.js did allow us to do it to some extent. Vue files are actually pretty good to work with since I don’t like inline templates. React mixes both JSX/HTML with JS code which I just don’t like since I strongly believe in separation of concerns and it looks ugly IMHO.

#### **Coding speed**

Coding speed was an area Vue.js won by far, not having to learn JSX was of huge help. This speed was later confirmed when another developer joined the project and was contributing to the project in a matter of hours after a training session of about 1 hour.

This was extremely important for us and you can see it right away by opening a vue file. It contains a template section with HTML and tags that look similar to Angular 1 so if you did some Angular 1 it will be really familiar. A vue file also has a styles and pure javascript sections where you actually use javascript and you only need to learn a few things that about Vue.js to fully understand them. Understanding Vue.js properties like *methods*, *computed*, *properties*, *data* and *created* takes you to about 90% of what you need to understand to start coding, really easy.

#### **Documentation**

To have proper speed we needed good documentation and Vue.js documentation is superb. Guides, examples, questions and API are documented really well and cover all of the doubts we found during development. We were afraid to find Chinese documentation for many of the questions we would had but that was not the case, everything was available in English.

#### **Asking around**

Vue.js looked really good after more than a week of consideration but to my surprise, asking around was useless, since no one had used Vue.js before, the only comment I got was in the order of “*looks cool but I haven’t used it”*. React took the most mentions and Angular 2 came in a distant second place.

I started to look for local talent with Vue.js experience and I did find some who were really good so I started to think that I was not alone, my social techy circle was probably too small and I shouldn’t play enough attention to the fact that I didn’t know anyone in person working with Vue.js on production.

#### **Mobile**

At the time we were thinking about Vue.js vs React, we were also considering rewriting our mobile app and React Native looked like a really good choice. That was a big plus for React since Vue.js didn’t have anything remotely stable that resembles what React Native is trying to do, so the possibility of reusing code between the web and app clients was a huge plus, but I decided that I wasn’t going to consider possibilities that might or might not happen. After all, from my experience, with Node.js I reuse a really insignificant amount of code between the browser and the server.

#### **Licensing**

At the time I write this, there is great amount of discussion because Facebook changed the React license to BSD+Patents. According to Facebook, this license is meant to protect them from patent trolls. This was not primordial in our decision making process but I’m glad we didn’t go the React way since any noise related to Licenses is not a noise you want to hear.

In the end, Facebook being behind React might become a liability for the project instead of a strength, that is why it is usually better to have independent foundations or organizations in charge of a successful Open Source Software project. Facebook should do the right thing, take IBM as an example, when IBM bought Strongloop, they donated Express.js to the Node.js foundation where such an important software belongs. Pressure from the community and willingness from IBM to ensure the continuity of the software made it happen. Twitter is another good example, they released Bootstrap under the very permissive MIT License and no one is talking about License problems with Bootstrap.

#### **Final words**

Out of the many web pages I researched before making a decision, one graph caught my attention, the developer satisfaction on The state of Javascript survey that Sacha Greif [@sachagreif](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510) does every year. I admit, as the author does, that is not scientific survey but it does offer a good amount of information and this was later confirmed by our decision points when we had a clearer picture, specially about Vue.js since we knew nothing about it at the start of our research. You can read The State of Javascript on the following link.

[**The State Of JavaScript: Front-End Frameworks** *A few preliminary results*medium.com](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510)[(L)](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510)

![](../_resources/a01ed9077c652dcbcaf4e34703ab1867.png)![1*-ycXrPmBs7aJTD6Wyd18Xw.png](../_resources/42c42c53a07d0d4c7e8c6a6c5a05ac5f.png)

Overall, Vue.js was the the winner in our evaluation, it had many questions answered on Stack Overflow, the clearest official documentation of the three options, the smallest code base, integrates well with Bootstrap and learning that it was backed by strong projects like Laravel and a big company like Alibaba was a big plus. Not having a community as big as React’s was not a real factor since it was big enough.

Going with Vue.js was the right choice, it took me a while to convince my CTO but I’m grateful he always asked the right and tough questions and force me to be 100% sure of my decision, I was going to regret it if I made a mistake. I think there was a small part of him that wasn’t sure until he wrote a whole component and found it really easy.

In the end the whole decision process was really helpful, but the fact that I was able to learn really fast made a huge difference, call it gut feeling if you like, but learning something really fast gave me great confidence in the more complex problems that I knew I would face during actual development.

I’m not saying React is a bad choice, I’m surprised by how big the community is and there’s a good reason for it, but jQuery is bigger and that doesn’t make it a good framework / library for the project we wanted to do.

Vue.js is gaining momentum and we saw that during development which only reassured us that we took the right choice.

We value simplicity and Vue.js achieves that, this simplicity is reflected on the learning curve, the documentation and specially in coding speed. If you’re still confused or need more arguments, I encourage you to go and read the following link:

[**Comparison with Other Frameworks - Vue.js** *Vue.js - The Progressive JavaScript Framework*vuejs.org](https://vuejs.org/v2/guide/comparison.html)[(L)](https://vuejs.org/v2/guide/comparison.html)

*Rever (*[*www.reverscore.com*](https://www.reverscore.com/)*) is an online platform that enables companies to engage all their employees in frontline innovation every day. Rever demystifies innovation and makes it a daily habit for everyone. We are always recruiting, if you want to work with an amazing tech team, check out our opportunities at *[*https://reverscore.com/careers/*](https://reverscore.com/careers/)

***Luis Elizondo ****is the Lead Engineer at Rever where he does Backend and Frontend Web development. He’s also in charge of automation, infrastructure, systems architecture and security. He has more than 10 years of experience working with multiple programming languages, designing application architectures, automating processes and operations and administering servers on the cloud.*