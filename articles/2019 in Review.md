2019 in Review

# 2019 in Review

[![LgLb--Of_200x200.jpg](../_resources/44f5ae28ecf3114297804a3ef794b0f0.jpg)rauchg](https://twitter.com/rauchg)January 2, 2020 (6d ago)*27,170* views

*This post is a quick summary of the evolution of [our company](https://zeit.co/), our [open-source work](https://nextjs.org/), interesting news and lessons in product design and engineering throughout 2019.*

## [#](https://rauchg.com/2020/2019-in-review#static-is-the-new-dynamic)Static is the new Dynamic

Throughout 2019 we have continued to see the growth of the *JAMstack*. The idea is quite simple: Any website or app you [build](https://nextjs.org/) and [deploy](https://zeit.co/) will use the stack of client-side *J*avaScript, *A*PIs, and *M*arkup.

By now, client-side JavaScript (like React and Vue) and APIs (like REST and GraphQL) are quite mainstream, but my favorite part is the assumption that your markup will be **static**.

First: Why Static?

- -Static is **globally fast**. When you deploy, we can *hoist* all your static assets to a global CDN network. By removing the server from the equation, we can also maximize availability by reducing and even altogether eliminating cache misses.
- -Static is **consistently fast**. It gives you "O(1) [TTFB](https://en.wikipedia.org/wiki/Time_to_first_byte)", which is a fancy way of saying you get stable and predictable latency to the first byte of the screen. Always, because no code, servers, sockets, or databases are involved.
- -Static is **always online**. This should [not be surprising](https://twitter.com/rauchg/status/1210294503216578560), but servers frequently go down and [involve complex rollout schemes](https://kccncna19.sched.com/event/Uads/the-gotchas-of-zero-downtime-traffic-w-kubernetes-leigh-capili-weaveworks)[[1]](https://rauchg.com/2020/2019-in-review#f1), while static files are trivially cacheable and simple to serve. The odds of you getting paged during the holidays because a "static asset can't be served from a CDN" are basically zero.

Second: Really, Static? I have *dynamic* needs.
Servers are not going away, but they are *moving around and hiding*.

- -**Static Site Generation (SSG)** can be thought of moving around the servers and taking them away from the hot path. Instead of putting a server in between the user's request and the response, we compute the response ahead of time.

This subtle shift pays back handsomely. One, anything that could go wrong, goes wrong at build time, maximizing **availability**. Two, we compute once and re-use, minimizing **database or API load**. Three, the resulting static HTML is **fast**.

- -**Client-side *J*S and *A*PIs** that get executed later, once the static markup and code is downloaded and executed, allow for effectively infinite dynamism.

Pre-computing all pages is not always possible[[2]](https://rauchg.com/2020/2019-in-review#f2), nor desirable. For example, when dealing with data that is *not* shared between all users and we wouldn't want to cache at the edge[[3]](https://rauchg.com/2020/2019-in-review#f3).

## [#](https://rauchg.com/2020/2019-in-review#next-the-next-frontier)Next.js, the next frontier

Next.js has continued to grow in adoption and now powers the likes of Hulu, Tencent News, Twitch, AT&T, Auth0 and the [list goes on](http://nextjs.org/showcase).

Thanks to its simplicity, it's a compelling all-in-one solution for the full straddle of JAMstack: from a static landing page, to very large websites, to fully dynamic applications.

The "secret sauce" continues to be its simple `pages/` system inspired by `cgi-bin` and throwing `.php` files in a FTP webroot.

A page is *just* a React component. The simplest Next.js app is `pages/index.js` which will serve the route `/`:

`export default () => <div>Hello World</div>`
But here's what happened in 2019:

- -Pages can be defined like this: `pages/r/[subreddit].js`, which will allow you to define dynamic path segments with no configuration or custom servers.
- -If a given page is static and has no [server-side data props](https://nextjs.org/blog/next-9#automatic-static-optimization), `next build` will output just "boring" static `.html`
- -If you define [static data props](https://github.com/zeit/next.js/issues/9524), we can fetch data at build time for a certain page, but crucially also "explode" dynamic path segments into many discrete pages.
- -If you create `pages/api/myApi.js`, you are basically defining a [serverless function](https://nextjs.org/blog/next-9#api-routes) that can return anything you want, which will most likely be a JSON API.

In short, Next.js is now a comprehensive, hybrid framework, supporting the full spectrum of JAMstack with a *per-page granularity*.

Role
Provided by
J
Client-side JS injected via React Hooks (state, event listeners, effects)
A
API pages inside the [object Object] directory.
M

Pages with no data dependencies (like the simple example above) or pages with static data deps that trigger build-time static site generation.

Furthermore, Next.js has been *uncompromising* in its commitment to backwards-compatibility. Servers (SSR) are still fully supported and no apps have been harmed as part of this evolution.

## [#](https://rauchg.com/2020/2019-in-review#deploying-jamstack)Deploying the JAMstack

We think there's enormous value in empowering teams to instantly build and deploy JAMstack websites, with no servers or infra to manage or configure.

True to our style, deploying any static site (like just a `index.html`) or more complex and full-featured frameworks like Next.js, Gatsby, Gridsome, … begins with just:

	$  now
	✅ Preview: [https://blog-p2pe8jedz.now.sh](https://blog-p2pe8jedz.now.sh/)

Use `npm i -g now` to install

The [ZEIT Now](https://zeit.co/) platform gives you a comprehensive workflow with built-in CI/CD and global CDN, that are carefully optimized for production-grade dynamic sites.

A salient feature is the transition we are seeing **away from code *review*** into **deployment *preview***.

Code review is undeniably important (specially [speedy code review](https://google.github.io/eng-practices/review/reviewer/speed.html)), but nothing beats teams collaborating by sharing URLs to the *actual* sites that are being worked on and experiencing them directly.

By setting up a [Git integration](https://zeit.co/github), every single `git push` gets its own live deployment URL. Thanks to the simplifications granted by the model, deployments are orders of magnitude faster to build, deploy and serve than when using servers or containers, which only adds to the great team-wide collaboration experience.

![71661231-7bb9f800-2d45-11ea-8aab-e030bcd16012.png](../_resources/c7196bdf8cfedd701b75e0e65e26d091.png)

Every push and branch gets its own deploy URL

## [#](https://rauchg.com/2020/2019-in-review#testing-the-jamstack)The Deploy URL, the Center of Gravity

An interesting consequence of being able to deploy so fast and so frequently is that it completely changes **testing and quality assurance**.

Every URL like `[https://blog-p2pe8jedz.now.sh](https://blog-p2pe8jedz.now.sh/)`, a preview deployment of this blog as I was writing this post, is a **real, production-like environment** just like the `rauchg.com` one.

This means that instead of running tests that make all kinds of assumptions about the environment (like mocking it), we can instead test the *real thing*. As real as it gets.

A new spin on [an old classic](https://twitter.com/rauchg/status/807626710350839808?lang=en)

The most natural form of "e2e testing" is experiencing the end result itself by visiting the URL. Sharing it with customers, co-workers and your manager.

But in 2019, we also witnessed the incredible power of delegating automated testing against this URL to other services.

![71646947-a3c63e80-2ce6-11ea-957c-c8f0f15ff176.png](../_resources/218dd912c1d731034920b1d504941f17.png)

The URL as the center of the app-building universe

When you install our [GitHub app](https://zeit.co/github), we don't just register a "Check" like other CI providers in the pull request. We also say: *this is a **deployment**, here is the URL*.

In *parallel*, a series of assurance checks can then be run against that prod-ready URL. This includes, but is not limited to:

- -**Browser Testing**, simulating user journeys and real interactions
- -**Screenshot Testing**, to automatically prevent visual regressions
- -**HTTP Assertion Testing**, requesting APIs or pages and verifying the outputs
- -**Manual QA**, with designated reviewers who approve the PR.

![71647154-46cc8780-2cea-11ea-8fe6-b9380c0c918b.png](../_resources/551b16036539bcd984ff073cdbf7de9d.png)

Checks are automatically run against the deploy URL

## [#](https://rauchg.com/2020/2019-in-review#flaky-tests-flaky-ux)Flaky Tests mean Flaky UX

When it comes to testing, I've found myself referencing this insight quite frequently:

As developers, we might sometimes be too quick to place the blame on tools (or the [aether](https://en.wikipedia.org/wiki/Aether_(classical_element))) and just press the restart button.

But the truly important question to ask is: what if it had been one of your customers, instead of an automated test? Would they not have had a *flaky* experience? Would it be ok to tell them to press F5 and try again?

## [#](https://rauchg.com/2020/2019-in-review#serverless-upgrades-itself)Serverless means infrastructure that upgrades itself

Serverless is an exciting trend that has resisted a universal definition. Asking what serverless *really* means probably got you 5 different answers in 2018, and 10 different answers in 2019.

However, a defining characteristic that I've become a fan of is that serverless means your **infrastructure upgrades itself**.

This includes everything from upgrading the operating system, to patching the system's OpenSSL, to bumping the version of the Node.js function runtime.

This wonderful effect is particularly pronounced for databases. It's one thing to upgrade the infrastructure of *stateless* code execution, but dealing with data is a whole new challenge that I'm glad we no longer have to deal with[[4]](https://rauchg.com/2020/2019-in-review#f4).

## [#](https://rauchg.com/2020/2019-in-review#hyrums-law)Hyrum's Law

I recently learned about [Hyrum's Law](https://www.hyrumslaw.com/), which states:

> With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.

Which obviously has a *relevant xkcd* as prior art:

![workflow.png](../_resources/29f80260aa6eb0f5020cced255e32721.png)
There is always an xkcd for that

## [#](https://rauchg.com/2020/2019-in-review#microservices-complex-unavailable)Microservices increase complexity and reduce availability

Microservices allow you to break down a service's dependencies into independently deployable units.

The problem? The assurances that were previously statically guaranteed by the compiler or runtime for a given piece of software are now gone. What was before a unit becomes a distributed system.

Not only are microservices harder to *manage* than, say, a static blob of code together with its dependencies inside a function or container, but odds are they are also **less available**.

This should already be obvious from at least one angle: introducing an *additional* network hop can only make things worse.

Kevin Mahoney has provided a new [neat mathematical illustration](http://kevinmahoney.co.uk/articles/microservices-and-availability/) of the availability problem of inter-connecting services:

> Take the example where service C depends on services A and B[…]

> If A has an availability of 0.8 (80%) and B 0.95 (95%), C will have a best case of 0.8 (80%), an average case of 0.8 × 0.95 = 0.76 (76%), and a worst case of 1 - ((1 - 0.8) + (1 - 0.95)) = 0.75 (75%)

Making your serverless functions "monolithic" offers a compelling solution to this problem. Statically bind the dependencies of each function ([Next.js API routes](https://nextjs.org/blog/next-9#api-routes) and the Go compiler do this) and avoid introducing unneeded service hops of your own.

## [#](https://rauchg.com/2020/2019-in-review#native-means-platform-fidelity)Native means Platform Fidelity, not Native Code

The word "native" has always bothered me. No one can seem to agree on a definition, but we all agree that "native apps" are always optimal.

Many people are quick to write off attempting to write a desktop app or mobile app in JavaScript on the basis that it's *not native*. Sometimes the word is used to indicate that JS can't compile down to an executable binary that's native to the platform.

I propose the following alternative definition of native: **an app that behaves to the quality standards of the platform it's deployed to**.

This explains why Electron has been so successful in re-purporsing the web stack to the Desktop platform. [A well engineered Electron app](https://www.zdnet.com/article/slacks-desktop-client-gets-major-performance-improvements-after-codebase-rewrite/) will give you "native" platform fidelity, regardless of programming language.

To achieve platform fidelity, it's obvious one must have access to the platform APIs. This makes **mobile web "apps"** a *non-starter* in achieving the coveted "native" status, especially on iOS Safari.

It has nothing to do with performance or JS and HTML, and everything to do with being altogether unable to deliver on the standards of what a *real* app can do on the platform[[5]](https://rauchg.com/2020/2019-in-review#f5).

Native performance with JS + native code

This means it's only a matter of time before React Native (and [similar technologies](https://github.com/Tencent/Hippy)) replicate the success that Electron has had on desktop.

A React Native app can achieve full platform fidelity (it can exhibit great performance with [solid engineering](https://blog.discordapp.com/how-discord-achieves-native-ios-performance-with-react-native-390c84dcd502) while being unconstrained in API capabilities). Crucially, like Electron, it offers a cohesive development experience, a universal programming language, a shared module and component system, seamless updates and faster deployments, with both (macOS) iOS and ([Windows](https://www.theverge.com/2019/6/24/18715202/microsoft-bill-gates-android-biggest-mistake-interview)) Android support to boot.

While SwiftUI is certainly exciting, RN, like Electron, has a tremendous economic advantage

## [#](https://rauchg.com/2020/2019-in-review#settings-are-for-successful-products)Settings are for successful products

Great products usually start with a dead simple onboarding journey that minimizes or entirely eliminates options.

From a startup evolution or product management perspective, another way of considering this wisdom is: absolutely resist adding options until **substantial evidence of success without them** exists.

## [#](https://rauchg.com/2020/2019-in-review#game-engineering-inspiration)Game engineering continues to show the way

When React was [being introduced](http://codewinds.com/podcast/004.html), it was interesting to hear that the inspiration wasn't previous libraries like jQuery, but rather an altogether different system:

> React gets some of its inspiration from how game engines achieve awesome performance in their rendering pipeline

What striked me about this wonderful talk about how [Marvel's Spiderman](https://www.youtube.com/watch?v=KDhKyIZd3O8) was created is how much more we can learn.

Insomniac Games' Elan Ruskin on Spider Man's various technical accomplishments

The most striking part of it is the careful planning around the well-understood limits of the platform that lead to a great user experience.

Today, at large, this kind of rigor is absent from web engineering practice, even though the boundaries exist and are well documented.

Developers understand these figures. How about our tools and platforms?

So far, we have mostly been *suggested* limits. Examples include: warnings in webpack's colorful output for oversized bundles, scoring systems like WebPageTest and Lighthouse, and the constant reminder and enticement that more speed means more success for your business (in the form of better Google rankings and the [Amazon 100ms rule](https://www.gigaspaces.com/blog/amazon-found-every-100ms-of-latency-cost-them-1-in-sales/)).

AMP, although controversial, is a *systematic*, rather than *suggested* answer to the performance problem. It's very hard, maybe impossible, to create a slow AMP experience, due to the smart constraints and built-in well-optimized components[[6]](https://rauchg.com/2020/2019-in-review#f6).

Along the same lines, I'm optimistic about the introduction of [**Never-Slow Mode**](https://www.infoq.com/news/2019/02/chrome-never-slow-mode/), which is a more general solution than AMP, with a shared focus on performance. Like [AMP on Next.js](https://nextjs.org/blog/next-8-1#amp-in-nextjs), I reckon it will be a *mode* many will be interested in adopting.

## [#](https://rauchg.com/2020/2019-in-review#notion-is-fancy)Notion: the *fanciest* datastructure

When [announcing Trello](https://www.joelonsoftware.com/2012/01/06/how-trello-is-different/), Joel Spolsky famously conjectured:

**> The great horizontal killer applications are actually just fancy data structures.**

> Spreadsheets are not just tools for doing “what-if” analysis. They provide a specific data structure: a table. Most Excel users never enter a formula. They use Excel when they need a table. The gridlines are the most important feature of Excel, not recalc.

In 2019, I fell in love with [Notion](https://www.notion.so/), which you can think of an all-in-one company/personal wiki + full MS Office-like suite.

That you could have *one tool* to solve such a wide array of problems sounds impossible, let alone for a small startup. But the secret to its success lies in its elegant, flexible and **user-transparent** datastructure.

Notion's datastructure could be explained as: a mutable, realtime graph of documents structured as a list of known blocks.

All apps are backed by datastructures, but the critical ingredient seems to be the ability to perform [direct manipulation](https://www.nngroup.com/articles/direct-manipulation/) on them, which requires that the **topology is completely transparent and obvious to the end user**.

![71637284-d0228200-2c36-11ea-8042-a26d9c3c4954.png](../_resources/fbe59eb39efc643e318d0529bac05788.png)

The Notion UI. Every UI element is mutable and hyperlinkable

On the left hand side, Notion's sidebar puts you in direct contact with the graph the documents are organized as. You are free to arrange pages into trees and sub-trees of your choosing. On the right hand side, the different block types are trivial to create, edit, re-arrange and most importantly: **combine**.

In the old world, a table is not thought of as a *block*, but a document that you boot Excel or Google Spreadsheets to visualize. Instead, combining headings, paragraphs, tables, databases, lists, etc to your liking inside any document, which you link to and open with the same realtime collaborative app, strikes me as a revolution whose time has finally come.

## [#](https://rauchg.com/2020/2019-in-review#inputs-should-look-like-inputs)Breaking: inputs should look like inputs

This one should not come as much of a shocker, but [alas](https://twitter.com/paulg/status/1209874543713640448).

But Google does it!

It [only took](https://twitter.com/mrcoreysimons/status/1191547435513864192?s=21) 600 participants, 2 designers, 1 researcher to confirm: **inputs should look like inputs**.

![71637360-488a4280-2c39-11ea-906a-24f9d8b9a7aa.png](../_resources/028c94592dd15442ce1c3f201d655c28.png)

Some revenue-centric folks have known the ideal input design forever

## [#](https://rauchg.com/2020/2019-in-review#shared-cdns-caches-are-busted)Shared CDNs have their caches busted

A remarkable change to anyone who was hoping we could "share React" or "share jQuery" by an ad-hoc agreement of a common CDN and URL inside a `<script>` tag.

The whole idea has [been busted](https://www.jefftk.com/p/shared-cache-is-going-away).

## [#](https://rauchg.com/2020/2019-in-review#all-code-is-wrong)All Code is Wrong

Another year, another great opportunity to remember that most of your code is likely wrong. We got to hear this from the famed creator of Fornite:

Writing great, correct, fast and reliable code is very hard. Assume it's all wrong.

As a reminder, **[if it's not fast and reliable, then it is wrong](https://twitter.com/garybernhardt/status/1007699924866093056)**. When things are not fast, it's like an implicit confirmation that they are wrong. Deeply wrong:

> […] The slowness is like an off smell. I don’t trust the application as much as I would if it didn’t slow down on such a small text file. 5,000 words is nothing. Faith is tested: It makes me wonder how good the sync capabilities are. It makes me wonder if the application will lose data.

> Speed and reliability are often intuited hand-in-hand. Speed can be a good proxy for general engineering quality

> – Craig Mod on > [> Fast software, the Best software](https://craigmod.com/essays/fast_software/)

## [#](https://rauchg.com/2020/2019-in-review#get-busy-demoing)Get busy demoing

I continue to marvel at the incredible product-improving and life-improving power of giving demos frequently. Giving frequent demos was an essential part of creating the iPhone:

Don't be afraid to (fail) demo.

## [#](https://rauchg.com/2020/2019-in-review#nocode-lowcode-merge)NoCode and LowCode are real, and they are on a collision course

It's easy to dismiss the hype around NoCode and LowCode as just hype, but I think there's a lot to it.

For one: the less code you write, the easier to maintain, and [the less likely](https://rauchg.com/2020/2019-in-review#testing-the-jamstack) that [it will be wrong](https://rauchg.com/2020/2019-in-review#all-code-is-wrong). Next.js is a clear example of this. Our data-fetching[[7]](https://rauchg.com/2020/2019-in-review#f7) library [SWR](https://swr.now.sh/) is another. [Zero-config deployments](https://zeit.co/blog/zero-config), another.

I suspect 2020 and the years to come will see LowCode solutions (like React, Vue, [Svelte](https://svelte.dev/)…) continue to gain traction by making it simple and [succinct](https://twitter.com/mweststrate/status/1055532227939966976?lang=en) to share UI and behavior (e.g.: as UI *components* or *[hooks](https://reactjs.org/docs/hooks-intro.html)*).

We will also [see](https://divjoy.com/) the [rise](https://www.framer.com/development) of [visual](https://blocks-ui.com/)  [tools](https://builderx.io/) to [bring](https://codesandbox.io/)  [those](https://shift.studio/)  [primitives](https://www.modulz.app/)  [together](https://tinacms.org/) more [efficiently](https://teleporthq.io/), including the capability to bring reusable components from either a canonical component system or a global shared library.

## [#](https://rauchg.com/2020/2019-in-review#hw-merges-with-sw)More Hardware that merges with our Software

After ARM gave us a [JS-optimized instruction](https://twitter.com/gparker/status/1047246359261106176), Samsung is [giving us key-value optimized SSDs](https://www.anandtech.com/show/14839/samsung-announces-standardscompliant-keyvalue-ssd-prototype).

## [#](https://rauchg.com/2020/2019-in-review#roll-everything-like-code)Everything is code. Roll everything like code

Applying a configuration change? Review it, roll it gradually and most importantly: mistrust it, just like [you mistrust code](https://rauchg.com/2020/2019-in-review#all-code-is-wrong).

## [#](https://rauchg.com/2020/2019-in-review#wasm-fast)Webassembly is faster than you thought

For a while I've been excited about the **universal** potential of webassembly. It turns out it's even better than I anticipated: when disabling sandboxing, webassembly can [match 95% the speed of native code](https://innative.dev/news/introducing-innative/)

> WebAssembly isn’t just a way to run C++ in a web browser, it’s a chance to reinvent how we write programs, and build a radical new foundation for software development

## [#](https://rauchg.com/2020/2019-in-review#quic-is-fast)QUIC (HTTP/3) is faster than you thought

Uber [deployed QUIC at scale](https://eng.uber.com/employing-quic-protocol/), obtaining remarkable results.

> The results from this experiment showed that QUIC consistently and very significantly outperformed TCP in terms of latency when downloading the HTTPS responses on the devices. Specifically, we witnessed a 50 percent reduction in latencies across the board, from the 50th percentile to 99th percentile.

![71637892-31068600-2c48-11ea-8810-461f9295228f.png](../_resources/579f239d06ecfb2052d0230d82d64190.png)

Percentage improvements in tail-end latencies (95th and 99th percentile)

## [#](https://rauchg.com/2020/2019-in-review#stablecoins-not-bitcoin)We are interested in stablecoins not bitcoin…

… seems to be the new "we like [blockchain not bitcoin](https://www.coindesk.com/love-blockchain-just-bitcoin)".

The president of the European Central Bank said the word "stablecoin" in 2019. That was a twist I wasn't expecting.

## [#](https://rauchg.com/2020/2019-in-review#zoom-works-better)Zoom just works better

[Zoom went public](https://www.businessinsider.com/zoom-files-to-go-public-2019-3). Its differentiator? **It works better**.

## [#](https://rauchg.com/2020/2019-in-review#google-oss-pratices)Google's engineering practices go open-source

Google's engineering practices were [open-sourced on GitHub](https://github.com/google/eng-practices). My favorite part? The emphasis on [speedy code-review](https://google.github.io/eng-practices/review/reviewer/speed.html):

**> At Google, we optimize for the speed at which a team of developers can produce a product together**> , as opposed to optimizing for the speed at which an individual developer can write code. The speed of individual development is important, it’s just not as important as the velocity of the entire team.

Further, Google's cryptography practices were "open-sourced" in a tweet:

## [#](https://rauchg.com/2020/2019-in-review#aws-reliability-patterns)AWS shares how they build ultra-reliable services

AWS architect Colm MacCárthaigh shares 10 patterns for controlling the cloud and ensuring its reliability:

If you don't fancy watching the video, read the tweet storm

1. [^](https://rauchg.com/2020/2019-in-review#s1) Servers can be so hard to roll out without downtime that a keynote at this year's KubeCon starts with the glaring admission: **"Noticing your customers receive 503's every now-and-then?"**. By not needing to rotate pods, shut down containers, handle signals, wait for grace periods, configure and execute liveliness probes… static is also **faster and safer to roll**.

2. [^](https://rauchg.com/2020/2019-in-review#s2) When the set of pages to pre-compute is too large and would make build times prohibitive, it's still probably a good idea to pre-compute your most critical public pages, and do the rest *asynchronously*.

3. [^](https://rauchg.com/2020/2019-in-review#s3) Crucially, websites and apps that serve the same static markup and code to all users have a drastically simpler security model, which means… static is also **more secure**.

4. [^](https://rauchg.com/2020/2019-in-review#s4) Our infrastructure makes use of CosmosDB, a serverless database by Microsoft Azure with remarkably (consistent) low-latency and effectively infinite horizontal scalability.

5. [^](https://rauchg.com/2020/2019-in-review#s5) Perhaps the most fundamental way in which a mobile web app on iOS Safari cannot ever be "native" like an app is in the way the viewport size is dynamic and shifts as you scroll to reveal different toolbars.

6. [^](https://rauchg.com/2020/2019-in-review#s6) Speaking of [native](https://rauchg.com/2020/2019-in-review#native-means-platform-fidelity), I intuit that, rather than native code generation, native mobile apps owe their generally better performance to the a rich standard library of well-optimized UI components. Go, when compared to Node.js+npm, has similarly demonstrated the success of a great stdlib for common, performance-critical needs.

7. [^](https://rauchg.com/2020/2019-in-review#s7) What you do in [one line of SWR](https://swr.now.sh/#basic-data-loading), you tend to do in a few dozen lines of Redux.