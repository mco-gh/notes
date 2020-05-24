Production Progressive Web Apps with JavaScript Frameworks | CSS-Tricks

#  Production Progressive Web Apps with JavaScript Frameworks

  By [ Sarah Drasner](https://css-tricks.com/author/sdrasner/)  On   May 27, 2017       [progressive web app](https://css-tricks.com/tag/progressive-web-app/)

This last week at Google I/O, Addy Osmani announced some amazing developer resources for creating Progressive Web Applications (PWAs) that prioritize performance with JavaScript Frameworks.

This was truly a team effort- a lot of people worked on these projects to get them going, and it's a really valuable contribution to the community. A lot of people want better performance for their framework of choice but can't get buy-in for time and resources to devote to this kind of endeavor. The ability to start with a baseline of high performance and good lighthouse scores is incredibly valuable, allowing developers to enjoy both the productivity and ergonomics of exciting frameworks, without sacrificing speed and user experience.

### [#](https://css-tricks.com/production-progressive-web-apps-javascript-frameworks/#article-header-id-0)Here are some of the highlights!

Addy created a site to explore some of the templates that they built out with the different PWA solutions, as a successor to the very popular TodoMVC, called HN PWA. You can explore [all of the demos and the GitHub repo here](https://hnpwa.com/). He then went through some major company implementations of each of the frameworks rebuilt as PWAs. Throughout a lot of the case studies that Addy features, the heavy-hitters in building for better web experiences lied in `link rel=preload`, `requestIdleCallback()`, and [HTTP2 Server Push](https://www.smashingmagazine.com/2017/04/guide-http2-server-push/). There were many mentions the [PRPL pattern](https://developers.google.com/web/fundamentals/performance/prpl-pattern/), in essence prioritizing what you're going to use first, by **Pushing** critical resources for the initial URL route, **Rendering** the initial route, **Pre-caching** remaining routes, and **Lazy-loading** and create remaining routes on demand. A lot of the performance wins were framed within the ability to be interactive on mobile within 5 seconds and trying to lower the overhead of the framework itself so that you had more time in that 5 seconds for your own application code.

#### [#](https://css-tricks.com/production-progressive-web-apps-javascript-frameworks/#article-header-id-1)React

React announced that Create React App will now be a PWA by default! This is a *big* win here. They now employ service workers with an offline-first caching strategy, code-splitting with dynamic import(), helpful overlays for errors, and it gives you **1.5s of headroom** for your application code. [More information](https://facebook.github.io/react/blog/2017/05/18/whats-new-in-create-react-app.html) on the release here.

#### [#](https://css-tricks.com/production-progressive-web-apps-javascript-frameworks/#article-header-id-2)Preact

Now has a CLI! Announced at the event, this is a pretty amazing development worth playing around with. You can [find the project here](https://github.com/developit/preact-cli). Among other really nice features you can read through in the readme, it has a 100/100 Lighthouse score out of the box, as well as a whopping **3s of headroom** to work on your own application code.

If you're not familiar with [Preact](https://preactjs.com/), it's an extremely fast 3kb React alternative with the same API, including the use of components & virtual DOM. It's similar to React, but the small filesize is central to the software design. The only caveat mentioned is that due to its emphasis on slim builds, there may be offerings in the React ecosystem that still need work for seamless integration. That said, Preact was the *clear winner* in performance here, so I wouldn't be surprised to see the community rally around this solution.

#### [#](https://css-tricks.com/production-progressive-web-apps-javascript-frameworks/#article-header-id-3)Vue

Vue announced a PWA template, offered directly from Vue-cli, which you can access easily with `vue init pwa`.

[Screen-Shot-2017-05-21-at-12.31.54-AM_ucysjm.webp](../_resources/7ffa76b6a9ecf18d5674678eefa97077.webp)

Among a lot of great offerings, it gives you two **2s of headroom** for application code on mobile, code-splitting with dynamic import(), service worker for offline caching, and JS chunks are preloaded or prefetched.

If you're not familiar with Vue, I've written up [a guide here](https://css-tricks.com/guides/vue/). I think Vue is an amazing piece of software, and the ability to strike all of the lighthouse credentials out of the gate is pretty incredible. This workflow makes it so easy to create beautiful and complex apps.

There are many more details that I didn't get to in this post, and Addy is a great speaker. He even created a video game for his talk. It's a worthwhile watch the whole way through, you can view it here:

### [#](https://css-tricks.com/production-progressive-web-apps-javascript-frameworks/#article-header-id-4)*Related*

[(L)](https://css-tricks.com/wordpress-pwas/)

#### [WordPress + PWAs](https://css-tricks.com/wordpress-pwas/)

One of the sessions from the Chrome Dev Summit, hosted by Das Surma and Daniel Walmsley. It's not so much about WordPress as it is about CMS powered sites that aren't really "apps", if there is such a thing, and the possibility of turning that site into a Progressive Web…

October 29, 2017

[(L)](https://css-tricks.com/practical-guide-progressive-web-apps-organisations-dont-know-anything-progressive-web-apps/)

#### [A practical guide to Progressive Web Apps for organisations who don’t know anything about Progressive Web Apps](https://css-tricks.com/practical-guide-progressive-web-apps-organisations-dont-know-anything-progressive-web-apps/)

Sally Jenkinson: Progressive Web Apps (sometimes referred to as PWAs, because everything in tech needs an acronym) is the encapsulating term for websites following a certain approach, that meet particular technical criteria. The "app" involvement in the name isn’t an accident – these creations share much of the functionality that…

January 30, 2017
[(L)](https://css-tricks.com/pwa-directory/)

#### [PWA Directory](https://css-tricks.com/pwa-directory/)

The other day I was watching an interview with Ade Oshineye where he discussed his work on the PWA Directory at Google, a showcase of progressive web apps. And it’s pretty neat! It lists a whole bunch of PWAs out there and you can filter them by Lighthouse metrics –…

April 25, 2017