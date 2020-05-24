Revisiting the rendering tier

[Digital Blog](https://www.theguardian.com/info/series/digital-blog)
[Information](https://www.theguardian.com/info)

# Revisiting the rendering tier

From 62,783 lines of Sass to CSS-in-JS. Introducing the new server rendering layer for theguardian.com

Alex Sanders
Alex Sanders is a lead software engineer at the Guardian
Thu 4 Apr 2019 10.44 BSTLast modified on Mon 8 Apr 2019 08.50 BST

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='-2 -2 32 32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--facebook__svg inline-share-facebook__svg inline-icon__svg js-evernote-checked' data-evernote-id='299'%3e %3cpath d='M17.9 14h-3v8H12v-8h-2v-2.9h2V8.7C12 6.8 13.1 5 16 5c1.2 0 2 .1 2 .1v3h-1.8c-1 0-1.2.5-1.2 1.3v1.8h3l-.1 2.8z'%3e%3c/path%3e %3c/svg%3e)](https://www.facebook.com/dialog/share?app_id=180444840287&href=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%3FCMP%3Dshare_btn_fb)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='-2 -2 32 32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--twitter__svg inline-share-twitter__svg inline-icon__svg js-evernote-checked' data-evernote-id='300'%3e %3cpath d='M21.3 10.5v.5c0 4.7-3.5 10.1-9.9 10.1-2 0-3.8-.6-5.3-1.6.3 0 .6.1.8.1 1.6 0 3.1-.6 4.3-1.5-1.5 0-2.8-1-3.3-2.4.2 0 .4.1.7.1l.9-.1c-1.6-.3-2.8-1.8-2.8-3.5.5.3 1 .4 1.6.4-.9-.6-1.6-1.7-1.6-2.9 0-.6.2-1.3.5-1.8 1.7 2.1 4.3 3.6 7.2 3.7-.1-.3-.1-.5-.1-.8 0-2 1.6-3.5 3.5-3.5 1 0 1.9.4 2.5 1.1.8-.1 1.5-.4 2.2-.8-.3.8-.8 1.5-1.5 1.9.7-.1 1.4-.3 2-.5-.4.4-1 1-1.7 1.5z'%3e%3c/path%3e %3c/svg%3e)](https://twitter.com/intent/tweet?text=Revisiting%20the%20rendering%20tier&url=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%3FCMP%3Dshare_btn_tw)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--email__svg inline-share-email__svg inline-icon__svg js-evernote-checked' data-evernote-id='301'%3e %3cpath d='M23.363 20.875H8.637v-8.938l6.545 5.687h1.637l6.544-5.687v8.938zm-1.635-9.75L16 16l-5.728-4.875h11.456zM23.363 9.5H8.637L7 11.125v9.75L8.637 22.5h14.727L25 20.875v-9.75L23.363 9.5z'%3e%3c/path%3e %3c/svg%3e)](https://www.theguardian.com/info/2019/apr/04/revisiting-the-rendering-tiermailto:?subject=Revisiting%20the%20rendering%20tier&body=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%3FCMP%3Dshare_btn_link)

![](data:image/svg+xml,%3csvg width='12' height='12' viewBox='0 0 12 12' xmlns='http://www.w3.org/2000/svg' data-evernote-id='302' class='js-evernote-checked'%3e%3cpath d='M10.073 8.4c-.475 0-.906.19-1.225.497l-5.308-2.676.015-.221-.015-.221 5.308-2.676c.319.308.75.497 1.225.497.982 0 1.778-.806 1.778-1.8s-.796-1.8-1.778-1.8-1.778.806-1.778 1.8l.016.233-5.299 2.675c-.32-.313-.755-.507-1.236-.507-.982 0-1.778.806-1.778 1.8s.796 1.8 1.778 1.8c.48 0 .915-.194 1.236-.507l5.299 2.675-.016.233c0 .994.796 1.8 1.778 1.8s1.778-.806 1.778-1.8-.796-1.8-1.778-1.8zm0-7.68c.588 0 1.067.484 1.067 1.08 0 .596-.479 1.08-1.067 1.08s-1.067-.484-1.067-1.08c0-.596.479-1.08 1.067-1.08zm0 10.56c-.588 0-1.067-.484-1.067-1.08 0-.596.479-1.08 1.067-1.08s1.067.484 1.067 1.08c0 .596-.479 1.08-1.067 1.08z'%3e%3c/path%3e%3c/svg%3e)Shares

38

[ ### ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' data-evernote-id='303' class='js-evernote-checked'%3e%3cpath d='M13 0l1 1v7l-1 1h-6l-2 3h-1v-3h-2l-1-1v-7l1-1h11z'%3e%3c/path%3e%3c/svg%3e)  Comments   9](https://www.theguardian.com/info/2019/apr/04/revisiting-the-rendering-tier#comments)

[ ![3500.jpg](../_resources/783af7ccdc14efbe67bb82f2fca32153.jpg)  ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22' class='centered-icon__svg rounded-icon__svg article__fullscreen__svg modern-visible__svg inline-expand-image__svg inline-icon__svg js-evernote-checked' data-evernote-id='304'%3e %3cpath d='M3.4 20.2L9 14.5 7.5 13l-5.7 5.6L1 14H0v7.5l.5.5H8v-1l-4.6-.8M18.7 1.9L13 7.6 14.4 9l5.7-5.7.5 4.7h1.2V.6l-.5-.5H14v1.2l4.7.6'%3e%3c/path%3e %3c/svg%3e)](https://www.theguardian.com/info/2019/apr/04/revisiting-the-rendering-tier#img-1)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='11' height='10' viewBox='0 0 11 10' class='hide-until-tablet__svg inline-triangle__svg inline-icon__svg js-evernote-checked' data-evernote-id='306'%3e %3cpath fill-rule='evenodd' d='M5.5 0L11 10H0z'%3e%3c/path%3e %3c/svg%3e)The road to a better developer experience is long and winding. Photograph: Arnd Wiegmann/Reuters

The 2019 incarnation of [theguardian.com](https://www.theguardian.com/uk) began life around six years ago, starting out as an m-dot and gradually scaling up both its breakpoints and page views until it rendered the entire site.

At the time of writing, it has gone from 0 to 62,783 lines of Sass. That Sass generates tens of thousands of rules that are intended to describe a maintainable set of responses to business and design problems.

Individually, they represent half a decade’s considered decisions made by skilful and dedicated engineers.

In sum, though, they present a precarious, teetering, maintenance nightmare.
Advertisement

In what way? For one, it is significantly easier to add new CSS than to edit or delete it.

Secondly, it has become unclear how you should approach making edits.

Some of our selectors are utilities that describe presentation (e.g. *.hide-on-mobile*) and others describe features (e.g. *.facia-card*). When a new feature is introduced that derives its visual style from an existing feature, there are multiple approaches you could copy from: for example should you reuse existing rules or should you duplicate them?

Both approaches are in the code base, and both have their drawbacks.

If you reuse something, you will end up having to override parts of it to capture any differences and be bound to any (potentially unwitting) updates to the original.

If you duplicate something, you will not inherit any updates to the original that you *did* want, and the page becomes heavier: it takes longer and costs the reader more to download, the render tree takes longer to generate and the CSSOM takes up more memory.

You could extract the commonalities into new utility selectors, but then suppose someone else needs to borrow aspects of the look for an unrelated new feature and they decide to duplicate one of the previous two instances, to keep their feature safe from unrelated updates. When the original feature needs a design tweak, all three are out of sync, and the second is also now (probably) broken.

At this point, you are certain that whatever you do, you cannot delete any of it, because no one can really understand how everything interrelates. In order to avoid breaking anything, you would need to know all features on the site, how they *should* look and how they *will* look following your change.

Advertisement

You *do* know, however, that if you add some new rules, guarded by their BEM selectors, you (probably) will not break anything and nothing will break you, so that becomes the easiest thing to do.

This is pretty much where we are now.

To compound this, as the CSS has become more and more thorny, the appetite for features and experiment across the Guardian has grown. These are largely managed by teams devoted to quarter-length OKRs who need to iterate rapidly and safely.

A complex system of styling that ultimately is only safe if you add to it cannot sustain this. It leads to poor performance on our readers devices, which ultimately devalues both their reading experience and the journalism, and is unpleasant to develop.

## So what now?

To address this, and avoid ending up back here in a few years time, we need to understand how we got here in the first place.

When it was conceived, the existing site was built by around ten developers using state of the art tooling and techniques (one developer was even dedicated to maintaining an internal CSS framework and took a special interest in changes that made use of it).

As engineering focus shifted from creating a website to iterating aspects of it, the number of people touching the code and the breadth of their changes swelled. It is no longer feasible for one person to act as gatekeeper. With six years of developer turnover, it has also become harder and harder to understand the context of your change in the wider codebase: what can you do? what have other people done? what should you do?

As time goes by, these questions become harder and harder to answer, and the reason for that is their answers are based on *conventions*.

## The problem with Convention

Systems that try to contain complexity over long periods of time by convention will inevitably tend toward entropy, because one significant characteristic of convention is that it is trivially simple to break one.

You do not even need to be malicious. A convention is not [a line in the sand](https://github.com/guardian/frontend#core-development-principles-lines-in-the-sand). You can have a very good case for breaking or stretching one, but once a convention is no longer fully observed, subsequent cases for breaking or stretching it are automatically stronger, because the convention is already weakened. The more this happens, the weaker it gets.

In our case, the conventions that were in place to encourage simplicity became hazy. For example, our Sass is meant to follow to BEM, but in instances where the design requirements would create too many selectors, it defaults back to the cascade.

Advertisement

At the same time, any edits are assumed to be sympathetic to performance, because that has long been another convention. But an OKR team dedicated to moving a revenue metric might reasonably justify privileging conversions over page speed or longer-term development, especially if the feature is short-lived or the trade-off is small.

The consequence of our reliance on convention to manage this is that our Sass has become too hard to work with, and CSS too big to send down the wire.

## What could we do?

We could deal with the Sass by being stricter about our adherence to BEM, effectively working in a hyper-modular style, implementing extremely strict coupling of selectors to DOM elements i.e. thinking in components. This would mean you could be sure that your edits affected only the elements you knew your selectors targeted, and you could also know that if you deleted a template you could delete the relevant Sass.

This would resolve maintainability at the expense of performance: the amount of duplication and number of selectors would rocket.

Around the time we first started looking at this, atomic CSS frameworks started to appear. Approaches like Yahoo’s [Atomic CSS](https://acss.io/) and Adam Morse’s [Tachyons](https://tachyons.io/) mean you can be sure the CSS you ship to your user will be very, very small, almost as small as it could possibly be.

Since they require you to style elements themselves, rather than create rules that apply to elements, they make maintenance much easier too. Presentation is directly coupled to content – if you update or delete a template, nothing else is affected. In the case of Atomic CSS, unused declarations will not even be generated.

Both these approaches were very appealing, but very hard for us to adopt with our existing stack. Our HTML is generated by Twirl templates in Play, which is written in Scala. This means Atomic CSS, which manages your templates with Node, would be very difficult to install.

At the same time, the Scala in Play is compiled to Java binaries. While this means Play is very fast in production, editing a template in development requires some recompilation before you can see the change, often taking up to ten seconds. Using a system like Tachyons, which requires you to style your elements directly using the class attribute, would be incredibly slow for us.

Both of these would also require a total rewrite of our templates, and the imposition of a new development style. If we could find a way to apply the thinking in the atomic approaches to a hyper-modular style of writing Sass, we could retain the familiarity of the stack while fixing the problems.

## False start

Advertisement

Looking through our various stylesheets and thinking about the atomic approach, it occurred to us that all of our shipping CSS must be reducible to a set of unique declarations.

If we could have recreated the site by replacing our Sass with a set of pre-existing functional classes (Tachyons-style), then we ought to be able to modify the Atomic CSS approach such that we could keep our existing Sass, rewrite it in part to *require* duplication (and so make edits safe) but analyse the resulting stylesheets and selector usage during the production build process to reduce that duplication to single-use utility classes?

In development we could just serve an enormous stylesheet, meaning no Scala recompilation and keeping the existing live Sass recompilation and dev tools pipeline.

Then in production, we ought to be able to ‘atomise’ our CSS to unique instances of declarations during compilation, build a map from the original rules to the unique ones, and use that in the Twirl templates at the point we write out the class attribute.

We created an [‘atomised CSS’ postcss plugin](https://sndrs.github.io/atomised-css-repl) that would take a normal stylesheet and return an atomised one, and a method for using that map in the Twirl templates, and for a while shipped [a tiny instance of it](https://github.com/guardian/frontend/pull/13549) in production.

It was designed so that any selectors which could not be atomised (anything which is not a single class, basically) would pass straight through, so *in theory* we should have been able to add it without making any changes to the Sass, getting the benefits where immediately possible and being to able to gradually remove all the more complex selectors till everything was atomised.

The ‘in theory’ bit was the scary part! This technique meant *completely* re-writing the stylesheet long after the last developer had touched the source code. In order to ship that with confidence, we would need to write a test suite that compared the effects of the original to the atomised stylesheets, on a DOM that captured a control and variant for each possible path in the original. That is not an impossible task, but at the point we started to write that, we really had to ask ourselves if this was the smartest approach!

## CSS in JS

We knew these problems were already being solved, by more and smarter people, in JavaScript land, but we were still working with a model where the DOM, CSS and JS all exist autonomously. At no point in their lifecycles is either aware of the other. The DOM is the source of truth when it comes to the content (everything is server-rendered) but the intentions expressed in the CSS and JS are only realised if *their* assumptions about the DOM are correct.

Advertisement

That is, in this way of working, the DOM, CSS and JS all interoperate entirely by *contract*. Which is to say, an acknowledgement that the humans who write the code will maintain certain conventions:

-

the DOM must provide hooks for the JS, which must encounter a DOM it understands

-

the JS might patch the DOM to reflect a new state, but that needs to be in a way that the CSS can style

-
the CSS must be able to accommodate whatever DOM it encounters

As we saw earlier, this means updates to the site need to understand the technical context of each edit, not just how they resolve a domain problem.

In turn, this makes updates more complicated to complete and increases the likelihood of bugs going to production.

More importantly for us, since the processes which generate our CSS and HTML understand nothing about each other, any optimisations like isolating critical CSS are at best error-prone and at worst impossible.

The beauty of the work being done on the various CSS-in-JS frameworks is that the*  *JS takes over managing the DOM *and* the CSS on both the client and the server.

It is a completely different way of thinking: instead of writing code for the *browser* to interpret, you write code that tells your *framework* how you want things to look behave, and *it* takes care of generating the code for the browser for you.

In this way of working, the codebase starts to become a more human-oriented description of how you want to solve domain problems, not a browser-oriented one. By abstracting browser-level code away, it becomes easier for a developer to do the right thing rather than the wrong thing. The architecture, and our performance and maintainability requirements, are managed by the framework, not the engineer.

So that is what we are doing. After a lot of trialing we have settled (for now at least) on [moving our rendering tier to React and Emotion](https://github.com/guardian/dotcom-rendering). This will doubtless generate a *new* set of challenges, but we expect that they should at least solve the set we have right now.

There are other blog posts to be written on how we settled on these two; how we will fit it into the stack; and how we’ve progressed since we started this project.

##  Since you’re here…

… we have a small favour to ask. More people are reading and supporting our independent, investigative reporting than ever before. And unlike many news organisations, we have chosen an approach that allows us to keep our journalism accessible to all, regardless of where they live or what they can afford.

The Guardian is editorially independent, meaning we set our own agenda. Our journalism is free from commercial bias and not influenced by billionaire owners, politicians or shareholders. No one edits our editor. No one steers our opinion. This is important as it enables us to give a voice to those less heard, challenge the powerful and hold them to account. It’s what makes us different to so many others in the media, at a time when factual, honest reporting is critical.

Every contribution we receive from readers like you, big or small, goes directly into funding our journalism. This support enables us to keep working as we do – but we must maintain and build on it for every year to come. **Support The Guardian from as little as £1 – and it only takes a minute. Thank you.**

 [Support The Guardian](https://support.theguardian.com/uk/contribute?REFPVID=jvusl24dsfbj5v1rsdmn&INTCMP=gdnwb_copts_memco_kr1_epic_ask_four_earning_control&acquisitionData=%7B%22source%22%3A%22GUARDIAN_WEB%22%2C%22componentId%22%3A%22gdnwb_copts_memco_kr1_epic_ask_four_earning_control%22%2C%22componentType%22%3A%22ACQUISITIONS_EPIC%22%2C%22campaignCode%22%3A%22gdnwb_copts_memco_kr1_epic_ask_four_earning_control%22%2C%22abTest%22%3A%7B%22name%22%3A%22ContributionsEpicAskFourEarning%22%2C%22variant%22%3A%22control%22%7D%2C%22referrerPageviewId%22%3A%22jvusl24dsfbj5v1rsdmn%22%2C%22referrerUrl%22%3A%22https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%22%7D)

 ![payment-methods.png](../_resources/2db3a266287f452355b68d4240df8087.png)

Topics

- [Information/](https://www.theguardian.com/info)
- [Digital Blog/](https://www.theguardian.com/info/series/digital-blog)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='-2 -2 32 32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--facebook__svg inline-share-facebook__svg inline-icon__svg js-evernote-checked' data-evernote-id='307'%3e %3cpath d='M17.9 14h-3v8H12v-8h-2v-2.9h2V8.7C12 6.8 13.1 5 16 5c1.2 0 2 .1 2 .1v3h-1.8c-1 0-1.2.5-1.2 1.3v1.8h3l-.1 2.8z'%3e%3c/path%3e %3c/svg%3e)](https://www.facebook.com/dialog/share?app_id=180444840287&href=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%3FCMP%3Dshare_btn_fb)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='-2 -2 32 32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--twitter__svg inline-share-twitter__svg inline-icon__svg js-evernote-checked' data-evernote-id='308'%3e %3cpath d='M21.3 10.5v.5c0 4.7-3.5 10.1-9.9 10.1-2 0-3.8-.6-5.3-1.6.3 0 .6.1.8.1 1.6 0 3.1-.6 4.3-1.5-1.5 0-2.8-1-3.3-2.4.2 0 .4.1.7.1l.9-.1c-1.6-.3-2.8-1.8-2.8-3.5.5.3 1 .4 1.6.4-.9-.6-1.6-1.7-1.6-2.9 0-.6.2-1.3.5-1.8 1.7 2.1 4.3 3.6 7.2 3.7-.1-.3-.1-.5-.1-.8 0-2 1.6-3.5 3.5-3.5 1 0 1.9.4 2.5 1.1.8-.1 1.5-.4 2.2-.8-.3.8-.8 1.5-1.5 1.9.7-.1 1.4-.3 2-.5-.4.4-1 1-1.7 1.5z'%3e%3c/path%3e %3c/svg%3e)](https://twitter.com/intent/tweet?text=Revisiting%20the%20rendering%20tier&url=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%3FCMP%3Dshare_btn_tw)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--email__svg inline-share-email__svg inline-icon__svg js-evernote-checked' data-evernote-id='309'%3e %3cpath d='M23.363 20.875H8.637v-8.938l6.545 5.687h1.637l6.544-5.687v8.938zm-1.635-9.75L16 16l-5.728-4.875h11.456zM23.363 9.5H8.637L7 11.125v9.75L8.637 22.5h14.727L25 20.875v-9.75L23.363 9.5z'%3e%3c/path%3e %3c/svg%3e)](https://www.theguardian.com/info/2019/apr/04/revisiting-the-rendering-tiermailto:?subject=Revisiting%20the%20rendering%20tier&body=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier%3FCMP%3Dshare_btn_link)
- [Share on LinkedIn![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--linkedin__svg inline-share-linkedin__svg inline-icon__svg js-evernote-checked' data-evernote-id='310'%3e %3cpath d='M10.576 7.985a1.57 1.57 0 0 1 0 3.137 1.568 1.568 0 0 1 0-3.137zm-1.353 4.327h2.706v8.704H9.223v-8.704zm4.403 0h2.595v1.19h.037c.361-.685 1.244-1.407 2.56-1.407 2.737 0 3.243 1.803 3.243 4.147v4.774h-2.702v-4.232c0-1.01-.02-2.308-1.406-2.308-1.408 0-1.623 1.1-1.623 2.235v4.305h-2.704v-8.704'%3e%3c/path%3e %3c/svg%3e)](http://www.linkedin.com/shareArticle?mini=true&title=Revisiting%20the%20rendering%20tier&url=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier)
- [Share on Pinterest![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' width='32' height='32' class='rounded-icon__svg centered-icon__svg social-icon__svg social-icon--pinterest__svg inline-share-pinterest__svg inline-icon__svg js-evernote-checked' data-evernote-id='311'%3e %3cpath d='M16.363 8C12.133 8 10 11.13 10 13.74c0 1.582.58 2.988 1.823 3.512.204.086.387.003.446-.23.04-.16.137-.568.18-.737.06-.23.037-.312-.127-.513-.36-.436-.588-1-.588-1.802 0-2.322 1.684-4.402 4.384-4.402 2.39 0 3.703 1.508 3.703 3.522 0 2.65-1.136 4.887-2.822 4.887-.93 0-1.628-.795-1.405-1.77.268-1.165.786-2.42.786-3.262 0-.752-.39-1.38-1.2-1.38-.952 0-1.716 1.017-1.716 2.38 0 .867.284 1.454.284 1.454l-1.146 5.006c-.34 1.487-.05 3.31-.026 3.493.014.108.15.134.21.05.09-.117 1.223-1.562 1.61-3.006.108-.41.625-2.526.625-2.526.31.61 1.215 1.145 2.176 1.145 2.862 0 4.804-2.693 4.804-6.298C22 10.54 19.763 8 16.363 8'%3e%3c/path%3e %3c/svg%3e)](http://www.pinterest.com/pin/find/?url=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier)
- [Reuse this content](https://syndication.theguardian.com/automation/?url=https%3A%2F%2Fwww.theguardian.com%2Finfo%2F2019%2Fapr%2F04%2Frevisiting-the-rendering-tier&type=article&internalpagecode=5481949)