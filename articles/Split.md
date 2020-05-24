Split

[(L)](https://adactio.com/)

- [Journal](https://adactio.com/journal)
- [Links](https://adactio.com/links)
- [Articles](https://adactio.com/articles)
- [Notes](https://adactio.com/notes)
- [About](https://adactio.com/about)

# Split

## April 10th, 2019

When I talk about [evaluating technology](https://adactio.com/articles/12839) for front-end development, I like to draw a distinction between two categories of technology.

On the one hand, you’ve got the raw materials of the web: HTML, CSS, and JavaScript. This is what users will ultimately interact with.

On the other hand, you’ve got all the tools and technologies that help you produce the HTML, CSS, and JavaScript: pre-processors, post-processors, transpilers, bundlers, and other build tools.

Personally, I’m much more interested and excited by the materials than I am by the tools. But I think it’s right and proper that other developers are excited by the tools. A good balance of both is probably the healthiest mix.

I’m never sure what to call these two categories. Maybe the materials are the “external” technologies, because they’re what users will interact with. Whereas all the other technologies—that mosty live on a developer’s machine—are the “internal” technologies.

Another nice phrase is something I heard during [Chris’s talk at An Event Apart in Seattle](https://adactio.com/journal/14891), when he quoted [Brad](http://bradfrost.com/), who talked about [the front of the front end and the back of the front end](https://adactio.com/journal/14891#Brad%20says).

I’m definitely more of a front-of-the-front-end kind of developer. I have opinions on the quality of the materials that get served up to users; the output should be accessible and performant. But I don’t particularly care about the tools that produced those materials on the back of the front end. Use whatever works for you (or whatever works for your team).

As a user-centred developer, my priority is doing what’s best for end users. That’s not to say I don’t value [developer convenience](https://jeremy.codes/blog/defining-productivity/). I do. [But I *prioritise* user needs over developer needs](https://adactio.com/journal/13333). And in any case, those two needs don’t even come into conflict most of the time. Like I said, from a user’s point of view, it’s irrelevant what text editor or version control system you use.

Now, you could make the argument that anything that is good for developer convenience is automatically good for user experience because faster, more efficient development should result in better output. While that’s true in theory, I highly recommend Alex’s post, [The “Developer Experience” Bait-and-Switch](https://infrequently.org/2018/09/the-developer-experience-bait-and-switch/).

Where it gets interesting is when a technology that’s designed for developer convenience is made out of the very materials being delivered to users. For example, a CSS framework like Bootstrap is *made* of CSS. That’s different to a tool like Sass which *outputs* CSS. Whether or not a developer chooses to use Sass is irrelevant to the user—the final output will be CSS either way. But if a developer chooses to use a CSS framework, that decision has a direct impact on the user experience. The user must download the framework in order for the developer to get the benefit.

So whereas Sass sits at the back of the front end—where I don’t care what you use—Bootstrap sits at the front of the front end. For tools like that, I don’t think saying “use whatever works for you” is good enough. It’s got to be weighed against the cost to the user.

Historically, it’s been a similar story with JavaScript libraries. They’re written in JavaScript, and so they’re going to be executed in the browser. If a developer wanted to use jQuery to make their life easier, the user paid the price in downloading the jQuery library.

But I’ve noticed a welcome change with some of the bigger JavaScript frameworks. Whereas the initial messaging around frameworks like React touted the benefits of state management and the virtual DOM, I feel like that’s not as prevalent now. You’re much more likely to hear people—quite rightly—talk about the benefits of modularity and componentisation. If you combine that with the rise of Node—which means that JavaScript is no longer confined to the browser—then these frameworks can move from the front of the front end to the back of the front end.

We’ve certainly seen that at [Clearleft](https://clearleft.com/). We’ve worked on multiple React projects, but in every case, the output was server-rendered. Developers get the benefit of working with a tool that helps them. Users don’t pay the price.

For me, this question of whether a framework will be used on the client side or the server side is crucial.

Let me tell you about a Clearleft project that sticks in my mind. We were working with a big international client on a product that was going to be rolled out to students and teachers in developing countries. This was right up my alley! We did plenty of research into network conditions and typical device usage. That then informed a tight [performance budget](https://clearleft.com/posts/responsive-design-on-a-budget). Every design decision—from web fonts to images—was informed by that performance budget. We were producing lean, mean markup, CSS, and JavaScript. But we weren’t the ones implementing the final site. That was being done by the client’s offshore software team, and they insisted on using React. “That’s okay”, I thought. “React can be used server-side so we can still output just what’s needed, right?” Alas, no. These developers did everything client side. When the final site launched, the log-in screen alone required megabytes of JavaScript just to render a form. It was, in my opinion, entirely unfit for purpose. It still pains me when I think about it.

That was a few years ago. I think that these days it has become a lot easier to make the decision to use a framework on the back of the front end. Like I said, that’s certainly been the case on recent Clearleft projects that involved React or Vue.

It surprises me, then, when I see the question of server rendering or client rendering treated almost like an implementation detail. It might be an implementation detail from a developer’s perspective, but it’s a key decision for the user experience. The [performance cost](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4) of putting your entire tech stack into the browser can be enormous.

Alex Sanders from the development team at The Guardian published a post recently called [Revisiting the rendering tier](https://www.theguardian.com/info/2019/apr/04/revisiting-the-rendering-tier). In it, he describes how they’re moving to React. Now, if this were a move to *client*-rendered React, that would make a big impact on the user experience. The thing is, I couldn’t tell from the article whether React was going to be used in the browser or on the server. The article talks about “rendering”—which is something that browsers do—and “the DOM”—which is something that only exists in browsers.

[So I asked](https://www.theguardian.com/info/2019/apr/04/revisiting-the-rendering-tier#comment-127743952). It turns out that this plan is very much about generating HTML and CSS on the server before sending it to the browser. Excellent!

With that question answered, I’m cool with whatever they choose to use. In this case, they’re choosing to use CSS-in-JS (although, to be pedantic, there’s no C anymore so technically it’s SS-in-JS). As long as the “JS” part is JavaScript *on a server*, then it makes no difference to the end user, and therefore no difference to me. Not my circus, not my monkeys. For users, the end result is the same whether styling is applied via a selector in an external stylesheet or, for example, via an inline style declaration (and in some situations, a server-rendered CSS-in-JS solution might be *better* for performance). And so, as a user-centred developer, this is something that I don’t need to care about.

Except…

I have misgivings. But just to be clear, these misgivings have *nothing* to do with users. My misgivings are entirely to do with another group of people: the people who make websites.

There’s a second-order effect. By making React—or even JavaScript in general—a requirement for styling something on a web page, the barrier to entry is raised.

At least, *I* think that the barrier to entry is raised. I completely acknowledge that this is a subjective judgement. In fact, the reason why a team might decide to make JavaScript a requirement for participation might well be because they believe it makes it *easier* for people to participate. Let me explain…

It wasn’t that long ago that devs coming from a Computer Science background were deriding CSS for its simplicity, complaining that “it’s broken” and turning their noses up at it. That rhetoric, thankfully, is waning. Nowadays they’re far more likely to acknowledge that [CSS might be simple, but it isn’t easy](https://adactio.com/journal/12571). Concepts like the cascade and specificity are real head-scratchers, and any prior knowledge from imperative programming languages won’t help you in this declarative world—all your hard-won experience and know-how isn’t fungible. Instead, it seems as though all this cascading and specificity is butchering the modularity of your nicely isolated components.

It’s no surprise that programmers with this kind of background would treat CSS as damage and find ways to route around it. The many flavours of CSS-in-JS are testament to this. From a programmer’s point of view, this solution has made things easier. Best of all, as long as it’s being done on the server, there’s no penalty for end users. But now the price is paid in the diversity of your team. In order to participate, a Computer Science programming mindset is now pretty much a requirement. For someone coming from a more declarative background—with really good HTML and CSS skills—everything suddenly seems needlessly complex. And [as Tantek observed](https://tantek.com/2018/309/t1/complexity-reinforces-privilege):

>
> Complexity reinforces privilege.

The result is a form of gatekeeping. I don’t think it’s intentional. I don’t think it’s malicious. It’s being done with the best of intentions, in pursuit of efficiency and productivity. But these code decisions are reflected in hiring practices that exclude people with different but equally valuable skills and perspectives.

Rachel describes [HTML, CSS and our vanishing industry entry points](https://rachelandrew.co.uk/archives/2019/01/30/html-css-and-our-vanishing-industry-entry-points/):

>

> If we make it so that you have to understand programming to even start, then we take something open and enabling, and place it back in the hands of those who are already privileged.

I think there’s a comparison here with toxic masculinity. Toxic masculinity is obviously terrible for women, but it’s also really shitty for men in the way it stigmatises any male behaviour that doesn’t fit its worldview. Likewise, if the only people your team is interested in hiring are traditional programmers, then those programmers are going to resent having to spend their time dealing with semantic markup, accessibility, styling, and other disciplines that they never trained in. Heydon correctly identifies this as [reluctant gatekeeping](http://www.heydonworks.com/article/reluctant-gatekeeping-the-problem-with-full-stack):

>

> By assuming the role of the Full Stack Developer (which is, in practice, a computer scientist who also writes HTML and CSS), one takes responsibility for all the code, in spite of its radical variance in syntax and purpose, and becomes the gatekeeper of at least some kinds of code **> one simply doesn’t care about writing well**> .

This hurts everyone. It’s bad for your team. It’s even worse for the wider development community.

Last year, [I was asked](https://abookapart.com/blogs/press/get-to-know-jeremy-keith/) “Is there a fear or professional challenge that keeps you up at night?” I responded:

>

> My greatest fear for the web is that it becomes the domain of an elite priesthood of developers. I firmly believe that, as Tim Berners-Lee put it, “this is for everyone.” And I don’t just mean it’s for everyone to use—I believe it’s for everyone to make as well. That’s why I get very worried by anything that raises the barrier to entry to web design and web development.

I’ve described a number of dichotomies here:

- Materials vs. tools,
- Front of the front end vs. back of the front end,
- User experience vs. developer experience,
- Client-side rendering vs. server-side rendering,
- Declarative languages vs. imperative languages.

But the split that worries the most is this:

- The people who make the web vs. the people who are excluded from making the web.

2:39pm

Tagged with[frontend](https://adactio.com/journal/tags/frontend)[development](https://adactio.com/journal/tags/development)[javascript](https://adactio.com/journal/tags/javascript)[css](https://adactio.com/journal/tags/css)[privilege](https://adactio.com/journal/tags/privilege)[inclusion](https://adactio.com/journal/tags/inclusion)[tools](https://adactio.com/journal/tags/tools)[materials](https://adactio.com/journal/tags/materials)[exclusion](https://adactio.com/journal/tags/exclusion)[hiring](https://adactio.com/journal/tags/hiring)[dichotomy](https://adactio.com/journal/tags/dichotomy)[server](https://adactio.com/journal/tags/server)[client](https://adactio.com/journal/tags/client)[rendering](https://adactio.com/journal/tags/rendering)[developer](https://adactio.com/journal/tags/developer)[convenience](https://adactio.com/journal/tags/convenience)[split](https://adactio.com/journal/tags/split)[divide](https://adactio.com/journal/tags/divide)[gatekeeping](https://adactio.com/journal/tags/gatekeeping)[react](https://adactio.com/journal/tags/react)[cssinjs](https://adactio.com/journal/tags/cssinjs)[frameworks](https://adactio.com/journal/tags/frameworks)[libraries](https://adactio.com/journal/tags/libraries)

Also on[Medium](https://medium.com/@adactio/24cc2f33716c)

[« Newer](https://adactio.com/journal/15051)[Older »](https://adactio.com/journal/15030)

Have you published a response to this? Let me know the URL:

## Responses

### [Moritz Gießmann](https://twitter.com/MoritzGiessmann/status/1115993436983824384)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70488)Posted by[Moritz Gießmann](https://twitter.com/MoritzGiessmann/status/1115993436983824384)onWednesday, April 10th, 2019 at 3:02pm

### [Hidde](https://twitter.com/hdv/status/1115998466998714370)

‘For me, this question of whether a framework will be used on the client side or the server side is crucial.’ – [@adactio](https://twitter.com/adactio) on tech choices for which users pay the price vs those for which they don’t [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70495)Posted by[Hidde](https://twitter.com/hdv/status/1115998466998714370)onWednesday, April 10th, 2019 at 3:22pm

### [Tyler Gaw](https://twitter.com/tylergaw/status/1116008391137271813)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70497)Posted by[Tyler Gaw](https://twitter.com/tylergaw/status/1116008391137271813)onWednesday, April 10th, 2019 at 4:01pm

### [Andy Bell](https://twitter.com/andybelldesign/status/1116009689710460931)

> “There’s a second-order effect. By making React—or even JavaScript in general—a requirement for styling something on a web page, the barrier to entry is raised.” A must read by [@adactio](https://twitter.com/adactio)[adactio.com/journal/15050](https://adactio.com/journal/15050)[andy-bell.design/links/156/](https://andy-bell.design/links/156/)

[#](https://adactio.com/journal/15050#comment70496)Posted by[Andy Bell](https://twitter.com/andybelldesign/status/1116009689710460931)onWednesday, April 10th, 2019 at 4:06pm

### [Max Böck](https://twitter.com/mxbck/status/1116014794157563906)

This hits close to home for me. My pain with CSS-in-JS is not with JavaScript, it’s with client side rendering. As long as DX doesn’t come at the user’s expense: use whatever you like! [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70506)Posted by[Max Böck](https://twitter.com/mxbck/status/1116014794157563906)onWednesday, April 10th, 2019 at 4:27pm

### [Michael Scharnagl](https://twitter.com/justmarkup/status/1116016102704857088)

This! https://t.co/Dz0zWG5LnX[(L)](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70507)Posted by[Michael Scharnagl](https://twitter.com/justmarkup/status/1116016102704857088)onWednesday, April 10th, 2019 at 4:32pm

### [Michael Scharnagl](https://twitter.com/justmarkup/status/1116016102704857088)

This! https://t.co/Dz0zWG5LnX[(L)](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71323)Posted by[Michael Scharnagl](https://twitter.com/justmarkup/status/1116016102704857088)onWednesday, April 10th, 2019 at 4:32pm

### [Baldur Bjarnason @baldur@toot.cafe](https://twitter.com/fakebaldur/status/1116016430472990721)

“Adactio: Journal—Split” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70505)Posted by[Baldur Bjarnason @baldur@toot.cafe](https://twitter.com/fakebaldur/status/1116016430472990721)onWednesday, April 10th, 2019 at 4:33pm

### [sylvia villegas](https://twitter.com/svillegastweets/status/1116017162370654210)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70504)Posted by[sylvia villegas](https://twitter.com/svillegastweets/status/1116017162370654210)onWednesday, April 10th, 2019 at 4:36pm

### [Nick Dunn](https://twitter.com/nickdunn/status/1116028122774765568)

Oh [@adactio](https://twitter.com/adactio) has nailed it again. On rendering, styling, the developer experience, performance, caring about your users and keeping the barrier-to-entry for building the web lower than tech bros.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70510)Posted by[Nick Dunn](https://twitter.com/nickdunn/status/1116028122774765568)onWednesday, April 10th, 2019 at 5:20pm

### [Kevin Lawver](https://twitter.com/kplawver/status/1116039302931263488)

Super guy, [@adactio](https://twitter.com/adactio), nails it again. This is one of the most important things I’ve read on web development in a long time: [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70513)Posted by[Kevin Lawver](https://twitter.com/kplawver/status/1116039302931263488)onWednesday, April 10th, 2019 at 6:04pm

### [Gérard Thomas](https://twitter.com/koozcoo/status/1116053525828653056)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70516)Posted by[Gérard Thomas](https://twitter.com/koozcoo/status/1116053525828653056)onWednesday, April 10th, 2019 at 7:01pm

### [Chris Taylor](https://twitter.com/mrwiblog/status/1116058571484090370)

Jeremy, once again, explains what’s in my head better than I ever could.[(L)](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70517)Posted by[Chris Taylor](https://twitter.com/mrwiblog/status/1116058571484090370)onWednesday, April 10th, 2019 at 7:21pm

### [blog.jim-nielsen.com](https://blog.jim-nielsen.com/2019/thuoghts-on-jeremy-keiths-split/)

[#](https://adactio.com/journal/15050#comment70533)Thursday, April 11th, 2019 at 4:39am

### [GF♯E](https://twitter.com/sofimi/status/1116301865866522624)

The people who make the web vs. the people who are excluded from making the web. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70537)Posted by[GF♯E](https://twitter.com/sofimi/status/1116301865866522624)onThursday, April 11th, 2019 at 11:27am

### [Dan Christian](https://twitter.com/danchristians/status/1116302057055621120)

Important points from [@adactio](https://twitter.com/adactio) and gels with my thinking. This is why I see [@vuejs](https://twitter.com/vuejs) and its Single File Components as a way to provide a modern and inclusive development environment regardless of where you sit on the stack.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70538)Posted by[Dan Christian](https://twitter.com/danchristians/status/1116302057055621120)onThursday, April 11th, 2019 at 11:28am

### [Ruth John](https://twitter.com/Rumyra/status/1116302298668572672)

Fab read [@adactio](https://twitter.com/adactio) thank you![adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70536)Posted by[Ruth John](https://twitter.com/Rumyra/status/1116302298668572672)onThursday, April 11th, 2019 at 11:29am

### [Thain](https://twitter.com/ThainBBdL/status/1116306036095430657)

[adactio.com/journal/15050](https://adactio.com/journal/15050) Excellent article from [@adactio](https://twitter.com/adactio) . Since a few month I’m really worried about this.

[#](https://adactio.com/journal/15050#comment70539)Posted by[Thain](https://twitter.com/ThainBBdL/status/1116306036095430657)onThursday, April 11th, 2019 at 11:44am

### [Tobias Ljungström](https://twitter.com/midvintr/status/1116310932509134849)

[@adactio](https://twitter.com/adactio) With some very on-the-mark thoughts on web technologies and inclusion. [#webdev](https://twitter.com/search?q=%23webdev)  [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70541)Posted by[Tobias Ljungström](https://twitter.com/midvintr/status/1116310932509134849)onThursday, April 11th, 2019 at 12:04pm

### [Ralph Brandi](https://twitter.com/thereisnocat/status/1116311916299862016)

Yet again, [@adactio](https://twitter.com/adactio) says what’s been in my brain for a while. Important post on gatekeeping, priesthood, and the way we build web sites. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70544)Posted by[Ralph Brandi](https://twitter.com/thereisnocat/status/1116311916299862016)onThursday, April 11th, 2019 at 12:07pm

### [Katie Sylor-Miller](https://twitter.com/ksylor/status/1116312208517017601)

I really love this piece by the always insightful & thoughtful & wonderful [@adactio](https://twitter.com/adactio) : [adactio.com/journal/15050](https://adactio.com/journal/15050) really cuts through the hyperbole of our industry drama du jour

[#](https://adactio.com/journal/15050#comment70543)Posted by[Katie Sylor-Miller](https://twitter.com/ksylor/status/1116312208517017601)onThursday, April 11th, 2019 at 12:09pm

### [Refresh Detroit](https://twitter.com/refreshdetroit/status/1116312457755156482)

“As a user-centred developer, my priority is doing what’s best for end users.” [adactio.com/journal/15050](https://adactio.com/journal/15050) via [@adactio](https://twitter.com/adactio)

[#](https://adactio.com/journal/15050#comment70542)Posted by[Refresh Detroit](https://twitter.com/refreshdetroit/status/1116312457755156482)onThursday, April 11th, 2019 at 12:10pm

### [Russell Heimlich](https://twitter.com/kingkool68/status/1116318263133245441)

“The people who make the web vs. the people who are excluded from making the web.”[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70545)Posted by[Russell Heimlich](https://twitter.com/kingkool68/status/1116318263133245441)onThursday, April 11th, 2019 at 12:33pm

### [Arnaud Delafosse](https://twitter.com/arnauddelafosse/status/1116321016547094533)

“I’m much more interested and excited by the materials ([#HTML](https://twitter.com/search?q=%23HTML), [#CSS](https://twitter.com/search?q=%23CSS) & [#JS](https://twitter.com/search?q=%23JS)) than I am by the tools ..my priority is doing what’s best for end users.” Excellent (as always) and so relevant reflection on the state of front-end development by [@adactio](https://twitter.com/adactio)[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70546)Posted by[Arnaud Delafosse](https://twitter.com/arnauddelafosse/status/1116321016547094533)onThursday, April 11th, 2019 at 12:44pm

### [Stanley Jones](https://twitter.com/stanley00/status/1116325692654809090)

I like [@adactio](https://twitter.com/adactio)’s reframing of HTML vs JS as potential gatekeeping through complexity. The Web is for everyone and we should examine who gets left out by “requiring” knowledge of React, etc.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70547)Posted by[Stanley Jones](https://twitter.com/stanley00/status/1116325692654809090)onThursday, April 11th, 2019 at 1:02pm

### [Ariel Burone](https://twitter.com/aburone/status/1116327771565961216)

Get out of my head [@adactio](https://twitter.com/adactio)! [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70548)Posted by[Ariel Burone](https://twitter.com/aburone/status/1116327771565961216)onThursday, April 11th, 2019 at 1:10pm

### [Johanna Bates](https://twitter.com/hanabel/status/1116340955173412864)

I am super psyched that [@adactio](https://twitter.com/adactio) wrote about developer tool complexity as a form of gatekeeping This has been an ever-evolving internal conversation at [@Dev_Collab](https://twitter.com/Dev_Collab) & Jeremy is so eloquent on all the points, as usual [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70550)Posted by[Johanna Bates](https://twitter.com/hanabel/status/1116340955173412864)onThursday, April 11th, 2019 at 2:03pm

### [Eystein](https://twitter.com/iceMagic/status/1116341992047415296)

In which [@adactio](https://twitter.com/adactio) eloquently puts into words how I feel about the state of developer tools vs. user experience [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70552)Posted by[Eystein](https://twitter.com/iceMagic/status/1116341992047415296)onThursday, April 11th, 2019 at 2:07pm

### [Kevin Pennekamp](https://twitter.com/kevtiq/status/1116361291856326656)

Just putting this here.. [#frontofthefrontend](https://twitter.com/search?q=%23frontofthefrontend)[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70554)Posted by[Kevin Pennekamp](https://twitter.com/kevtiq/status/1116361291856326656)onThursday, April 11th, 2019 at 3:24pm

### [New Adventures](https://twitter.com/naconf/status/1116367847066865666)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70555)Posted by[New Adventures](https://twitter.com/naconf/status/1116367847066865666)onThursday, April 11th, 2019 at 3:50pm

### [dan sankey](https://twitter.com/electroblankets/status/1116395568618668032)

A cracking read on the importance of keeping tech stacks simple when building for the web.. from [@adactio](https://twitter.com/adactio)  [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70557)Posted by[dan sankey](https://twitter.com/electroblankets/status/1116395568618668032)onThursday, April 11th, 2019 at 5:40pm

### [Mark](https://twitter.com/markhuot/status/1116403240151781377)

Still thinking about this,[adactio.com/journal/15050](https://adactio.com/journal/15050)Development tooling, right to repair, etc… they all come from good places but drawing the line between progress and dangerous complexity is hard.

[#](https://adactio.com/journal/15050#comment70558)Posted by[Mark](https://twitter.com/markhuot/status/1116403240151781377)onThursday, April 11th, 2019 at 6:10pm

### [Keith Kurson](https://twitter.com/keithkurson/status/1116425633582600193)

really enjoyed reading this piece and see a lot of what we’re trying to do at glitch reflected. the internet should be for everyone to build. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70560)Posted by[Keith Kurson](https://twitter.com/keithkurson/status/1116425633582600193)onThursday, April 11th, 2019 at 7:39pm

### [Nick F](https://twitter.com/nickautomatic/status/1116441412139089921)

Here [@adactio](https://twitter.com/adactio) eloquently expresses a lot of concerns I share about the current state of front-end development - in particular, trade-offs around developer vs user experience, and complexity as (often unintentional) gatekeeping[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70561)Posted by[Nick F](https://twitter.com/nickautomatic/status/1116441412139089921)onThursday, April 11th, 2019 at 8:42pm

### [Justin McDowell](https://twitter.com/revoltpuppy/status/1116441931645460481)

Materials vs. tools. User experience vs. developer experience. Client-side rendering vs. server-side rendering. Front of the front end vs. back of the front end. Just a few of the many dichotomies on the web, and they themselves are an interconnected web: [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70562)Posted by[Justin McDowell](https://twitter.com/revoltpuppy/status/1116441931645460481)onThursday, April 11th, 2019 at 8:44pm

### [CSS-Tricks](https://twitter.com/css/status/1116480295203737600)

On the one hand, you’ve got the raw materials of the web: HTML, CSS, and JavaScript. This is what users will ultimately interact with. On the other hand, you’ve got all the tools and technologies that help you produce the HTML, CSS, and JavaScript.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70570)Posted by[CSS-Tricks](https://twitter.com/css/status/1116480295203737600)onThursday, April 11th, 2019 at 11:17pm

### [giglobus j](https://twitter.com/giglobus/status/1116481419868553216)

css: On the one hand, you’ve got the raw materials of the web: HTML, CSS, and JavaScript. This is what users will ultimately interact with. On the other hand, you’ve got all the tools and technologies that help you produce the HTML, CSS, and JavaScript.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70569)Posted by[giglobus j](https://twitter.com/giglobus/status/1116481419868553216)onThursday, April 11th, 2019 at 11:21pm

### [tams sokari](https://twitter.com/tamssokari/status/1116481750669123584)

Adactio: Journal—Split one of my fave writers / thinkers on the web writes about some of the divisions prevalent in today’s web. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70571)Posted by[tams sokari](https://twitter.com/tamssokari/status/1116481750669123584)onThursday, April 11th, 2019 at 11:22pm

### [Gilberto](https://twitter.com/gilbertoleon/status/1116491731694968834)

Y sí, eso de tener más herramientas de desarrollo sí tiende a alienar a la gente nueva [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70572)Posted by[Gilberto](https://twitter.com/gilbertoleon/status/1116491731694968834)onFriday, April 12th, 2019 at 12:02am

### [Roger Johansson](https://twitter.com/rogerjohansson/status/1116565840793485312)

Very happy that front-endified back-end stuff like React or Vue haven’t been forced upon me yet. If that day comes, I’m out.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70574)Posted by[Roger Johansson](https://twitter.com/rogerjohansson/status/1116565840793485312)onFriday, April 12th, 2019 at 4:56am

### [Гонзо](https://twitter.com/gonzomir/status/1116578811548540928)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050) чрез [@Inoreader](https://twitter.com/Inoreader)

[#](https://adactio.com/journal/15050#comment70575)Posted by[Гонзо](https://twitter.com/gonzomir/status/1116578811548540928)onFriday, April 12th, 2019 at 5:48am

### [43 North Design](https://twitter.com/43north/status/1116583914561130496)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70576)Posted by[43 North Design](https://twitter.com/43north/status/1116583914561130496)onFriday, April 12th, 2019 at 6:08am

### [Pinboard Popular](https://twitter.com/PinPopular/status/1116590801784463362)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70577)Posted by[Pinboard Popular](https://twitter.com/PinPopular/status/1116590801784463362)onFriday, April 12th, 2019 at 6:36am

### [Pinboard Popular](https://twitter.com/pinboard_pop/status/1116596829804646402)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70578)Posted by[Pinboard Popular](https://twitter.com/pinboard_pop/status/1116596829804646402)onFriday, April 12th, 2019 at 7:00am

### [twitter.com](https://twitter.com/evert_/status/1116612696378499073)

[#](https://adactio.com/journal/15050#comment70580)Friday, April 12th, 2019 at 8:04am

### [Craig Buckler](https://twitter.com/craigbuckler/status/1116615754697207808)

Essential reading for web developers by [@adactio](https://twitter.com/adactio): [adactio.com/journal/15050](https://adactio.com/journal/15050)“The performance cost of putting your tech stack into the browser can be enormous.” “By making React [or JavaScript] a requirement for styling something on a web page, the barrier to entry is raised.”

[#](https://adactio.com/journal/15050#comment70581)Posted by[Craig Buckler](https://twitter.com/craigbuckler/status/1116615754697207808)onFriday, April 12th, 2019 at 8:15am

### [Andrew Smith](https://twitter.com/somenice/status/1116618072473788417)

“Not my circus, not my monkeys.”[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70582)Posted by[Andrew Smith](https://twitter.com/somenice/status/1116618072473788417)onFriday, April 12th, 2019 at 8:24am

### [SDS Labs](https://twitter.com/vio1965/status/1116640686735069184)

Top story: Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050), see more [tweetedtimes.com/helikopterdsgn…](http://tweetedtimes.com/helikopterdsgn/must-follow-web-designers-2?s=tnp)[(L)](http://tweetedtimes.com/helikopterdsgn/must-follow-web-designers-2)

[#](https://adactio.com/journal/15050#comment70584)Posted by[SDS Labs](https://twitter.com/vio1965/status/1116640686735069184)onFriday, April 12th, 2019 at 9:54am

### [Focus Mobility](https://twitter.com/FocusMobility/status/1116640690300235781)

Top story: Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050), see more [tweetedtimes.com/helikopterdsgn…](http://tweetedtimes.com/helikopterdsgn/must-follow-web-designers-2?s=tnp)[(L)](http://tweetedtimes.com/helikopterdsgn/must-follow-web-designers-2)

[#](https://adactio.com/journal/15050#comment70585)Posted by[Focus Mobility](https://twitter.com/FocusMobility/status/1116640690300235781)onFriday, April 12th, 2019 at 9:54am

### [Ivan Frantar](https://twitter.com/ifrantar/status/1116645773385637889)

This is so spot on it makes me a tad emotional . Be [@adactio](https://twitter.com/adactio) - [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70583)Posted by[Ivan Frantar](https://twitter.com/ifrantar/status/1116645773385637889)onFriday, April 12th, 2019 at 10:14am

### [Daniel Martínez](https://twitter.com/Wakkos/status/1116660522219397121)

Finally an article that explains why I fight so much with developers as soon as the user is affected by their tools of choice. Users should not suffer your comfortable stack.[adactio.com/journal/15050](https://adactio.com/journal/15050)By [@adactio](https://twitter.com/adactio) (thanks!)

[#](https://adactio.com/journal/15050#comment70587)Posted by[Daniel Martínez](https://twitter.com/Wakkos/status/1116660522219397121)onFriday, April 12th, 2019 at 11:13am

### [Astrolabit](https://twitter.com/astrolabit/status/1116662065257754624)

Split (via [@adactio](https://twitter.com/adactio) ) [adactio.com/journal/15050](https://adactio.com/journal/15050) Kudos!

[#](https://adactio.com/journal/15050#comment70586)Posted by[Astrolabit](https://twitter.com/astrolabit/status/1116662065257754624)onFriday, April 12th, 2019 at 11:19am

### [Laurence Hughes](https://twitter.com/fuzzylogicx/status/1116667215145779202)

One of the best articles I’ve read on the state of (front end) web development in 2019 [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70590)Posted by[Laurence Hughes](https://twitter.com/fuzzylogicx/status/1116667215145779202)onFriday, April 12th, 2019 at 11:39am

### [Andrzej Kała](https://twitter.com/andrzejkala/status/1116681751743672322)

Interesting point of view from [@adactio](https://twitter.com/adactio) on current state of front end. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70594)Posted by[Andrzej Kała](https://twitter.com/andrzejkala/status/1116681751743672322)onFriday, April 12th, 2019 at 12:37pm

### [Brad Frost](https://twitter.com/brad_frost/status/1116693948049838080)

I think Split by [@adactio](https://twitter.com/adactio) is a very important read about web development. It’s well worth your time: [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70595)Posted by[Brad Frost](https://twitter.com/brad_frost/status/1116693948049838080)onFriday, April 12th, 2019 at 1:25pm

### [Tom Tinkerson](https://twitter.com/webrocker/status/1116696601857228802)

go read this thoughtful piece by [@adactio](https://twitter.com/adactio) I consider myself a frontend-designer, since I’m neither full stack (according to the CS view), nor front-of-frontend, but also not back-of-frontend only. but labels aside, I do care about the UX over DEVX.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70596)Posted by[Tom Tinkerson](https://twitter.com/webrocker/status/1116696601857228802)onFriday, April 12th, 2019 at 1:36pm

### [xnoɹǝʃ uɐıɹq](https://twitter.com/brianleroux/status/1116697268781047808)

Important read from [@adactio](https://twitter.com/adactio)  [adactio.com/journal/15050](https://adactio.com/journal/15050)Legit concerns. I love the idea “back of the front end”

[#](https://adactio.com/journal/15050#comment70597)Posted by[xnoɹǝʃ uɐıɹq](https://twitter.com/brianleroux/status/1116697268781047808)onFriday, April 12th, 2019 at 1:39pm

### [Danny](https://twitter.com/dbanksDesign/status/1116703459619721216)

Great read and well worth your time. “Complexity reinforces privilege.”[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70601)Posted by[Danny](https://twitter.com/dbanksDesign/status/1116703459619721216)onFriday, April 12th, 2019 at 2:03pm

### [nils binder ️‍](https://twitter.com/supremebeing09/status/1116705000535859200)

I think I like the term „front-of-frontend“ [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70598)Posted by[nils binder ️‍](https://twitter.com/supremebeing09/status/1116705000535859200)onFriday, April 12th, 2019 at 2:09pm

### [caitlynmayers](https://twitter.com/caitlynmayers/status/1116706993375469569)

There are many substantive topics in [@adactio](https://twitter.com/adactio)’s piece that pair well w/ messages in [@katholmes](https://twitter.com/katholmes)’ Mismatch. We must consider who and how we’re excluding. We must think about the choices we make for others. We must think about those who will come after us.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70602)Posted by[caitlynmayers](https://twitter.com/caitlynmayers/status/1116706993375469569)onFriday, April 12th, 2019 at 2:17pm

### [Francesco Improta](https://twitter.com/zetareticoli/status/1116707064989065216)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70600)Posted by[Francesco Improta](https://twitter.com/zetareticoli/status/1116707064989065216)onFriday, April 12th, 2019 at 2:18pm

### [Darrell Wilson](https://twitter.com/darrell_wilson/status/1116707288461578242)

This is an excellent post from [@adactio](https://twitter.com/adactio) the current state of front-end web development.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70599)Posted by[Darrell Wilson](https://twitter.com/darrell_wilson/status/1116707288461578242)onFriday, April 12th, 2019 at 2:18pm

### [Gary Storey](https://twitter.com/garystorey/status/1116718373445021696)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70603)Posted by[Gary Storey](https://twitter.com/garystorey/status/1116718373445021696)onFriday, April 12th, 2019 at 3:03pm

### [Erik Pavletic](https://twitter.com/EPavletic/status/1116743837584625664)

This take on the current state of all things frontend by Jeremy really resonates with me:[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70605)Posted by[Erik Pavletic](https://twitter.com/EPavletic/status/1116743837584625664)onFriday, April 12th, 2019 at 4:44pm

### [Wil Floyd](https://twitter.com/wflo/status/1116743987514236930)

Top story: Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050), see more [tweetedtimes.com/v/17740?s=tnp](http://tweetedtimes.com/v/17740?s=tnp)[(L)](http://tweetedtimes.com/v/17740)

[#](https://adactio.com/journal/15050#comment70604)Posted by[Wil Floyd](https://twitter.com/wflo/status/1116743987514236930)onFriday, April 12th, 2019 at 4:44pm

### [Dion Almaer](https://twitter.com/dalmaer/status/1116747694318313473)

“Personally, I’m much more interested and excited by the materials than I am by the tools. But I think it’s right and proper that other developers are excited by the tools. A good balance of both is probably the healthiest mix.” Welcome, the tent is large [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70606)Posted by[Dion Almaer](https://twitter.com/dalmaer/status/1116747694318313473)onFriday, April 12th, 2019 at 4:59pm

### [Jeff Pelletier](https://twitter.com/withinsight/status/1116792243765927936)

This, this, and more this. I agree with everything in this post by [@adactio](https://twitter.com/adactio). Walled gardening is perhaps the worst decision you can make for your team and users: [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70608)Posted by[Jeff Pelletier](https://twitter.com/withinsight/status/1116792243765927936)onFriday, April 12th, 2019 at 7:56pm

### [Roger Nyman](https://twitter.com/open8roger/status/1116801757898772481)

Great writing and inspiring for thought, as always [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70609)Posted by[Roger Nyman](https://twitter.com/open8roger/status/1116801757898772481)onFriday, April 12th, 2019 at 8:34pm

### [mkirkpat](https://twitter.com/mkirkpat/status/1116817703652610048)

Great article summarising state of things, associated concerns, across building people-centred services from a developer pov…good to learn as someone who is not a dev, but is interested in code, leaness, inclusivity, openness in everything we build [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70610)Posted by[mkirkpat](https://twitter.com/mkirkpat/status/1116817703652610048)onFriday, April 12th, 2019 at 9:37pm

### [Markus Schork](https://twitter.com/atelierschork/status/1116827692480049153)

Great article by ⁦[@adactio](https://twitter.com/adactio)⁩ on keeping the web open: everyone should have access it, but also to make it! Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70611)Posted by[Markus Schork](https://twitter.com/atelierschork/status/1116827692480049153)onFriday, April 12th, 2019 at 10:17pm

### [Dapo Olaopa](https://twitter.com/dpencilpusher/status/1116846154526994433)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050) by [@adactio](https://twitter.com/adactio)  [#frontend](https://twitter.com/search?q=%23frontend)  [#webdesign](https://twitter.com/search?q=%23webdesign)  [#webdev](https://twitter.com/search?q=%23webdev)

[#](https://adactio.com/journal/15050#comment70612)Posted by[Dapo Olaopa](https://twitter.com/dpencilpusher/status/1116846154526994433)onFriday, April 12th, 2019 at 11:30pm

### [Shawn Brackat](https://twitter.com/sbrack8t/status/1116857758807203840)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70613)Posted by[Shawn Brackat](https://twitter.com/sbrack8t/status/1116857758807203840)onSaturday, April 13th, 2019 at 12:16am

### [Damon Cook](https://twitter.com/dcook/status/1116888352987516928)

Such a relevant post. Lot’s to reflect on. Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70614)Posted by[Damon Cook](https://twitter.com/dcook/status/1116888352987516928)onSaturday, April 13th, 2019 at 2:18am

### [Adrian Roselli](https://twitter.com/aardrian/status/1116903484325007361)

I disagree with assertion that CSS rendered by JS on server has no impact on users. Inlined is not DRY, adds bloat.[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70615)Posted by[Adrian Roselli](https://twitter.com/aardrian/status/1116903484325007361)onSaturday, April 13th, 2019 at 3:18am

### [Ido Rosenthal](https://twitter.com/idoros/status/1116917476720283648)

This! The concept of moving everything to JS always seemed like a DX privilege to me. [@adactio](https://twitter.com/adactio) thank you so much for writing this. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70616)Posted by[Ido Rosenthal](https://twitter.com/idoros/status/1116917476720283648)onSaturday, April 13th, 2019 at 4:14am

### [Zander](https://twitter.com/MrMartineau/status/1116942101718142976)

What an excellent read. [@adactio](https://twitter.com/adactio) nails it again. I couldn’t agree more and I’m probably part of the problem… [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70620)Posted by[Zander](https://twitter.com/MrMartineau/status/1116942101718142976)onSaturday, April 13th, 2019 at 5:52am

### [Ignacio Villanueva](https://twitter.com/IgnaciodeNuevo/status/1116966846194958336)

Split: “When I talk about evaluating technology for front-end development, I like to draw a distinction between two categories of technology. HTML, CSS, and JavaScript. This is what users will ultimately interact with.”[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70621)Posted by[Ignacio Villanueva](https://twitter.com/IgnaciodeNuevo/status/1116966846194958336)onSaturday, April 13th, 2019 at 7:30am

### [Stéphanie Walter](https://twitter.com/WalterStephanie/status/1116989351492296704)

Split, [@adactio](https://twitter.com/adactio) wraps up some thoughts on “the front of the front end and the back of the front end”, beeing a user centric developer, how the gate keepers of a more computer science driven industry might us all[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70622)Posted by[Stéphanie Walter](https://twitter.com/WalterStephanie/status/1116989351492296704)onSaturday, April 13th, 2019 at 8:59am

### [Alexander Boldakov](https://twitter.com/boldakov/status/1117010151775641601)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70623)Posted by[Alexander Boldakov](https://twitter.com/boldakov/status/1117010151775641601)onSaturday, April 13th, 2019 at 10:22am

### [Chris Pearce](https://twitter.com/chris__pearce/status/1117013402994372608)

[@adactio](https://twitter.com/adactio) is bang on with Split: [adactio.com/journal/15050](https://adactio.com/journal/15050) & it’s definitely real. I’ve been using the term “front of the front” for a while now.

[#](https://adactio.com/journal/15050#comment70624)Posted by[Chris Pearce](https://twitter.com/chris__pearce/status/1117013402994372608)onSaturday, April 13th, 2019 at 10:35am

### [Martin Thiemann](https://twitter.com/martinthiemann/status/1117048925662384134)

“In order to participate, a Computer Science programming mindset is now pretty much a requirement. For someone coming from a more declarative background—with really good HTML and CSS skills—everything suddenly seems needlessly complex.” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70627)Posted by[Martin Thiemann](https://twitter.com/martinthiemann/status/1117048925662384134)onSaturday, April 13th, 2019 at 12:56pm

### [Michael Spellacy (Spell)](https://twitter.com/Spellacy/status/1117072632787214336)

Fantastic article by [@adactio](https://twitter.com/adactio)! Nail on head, as usual. Sadly, I’ve been a victim of the (male) gatekeeping he writes about. It is indeed shitty. “The people who make the web vs. the people who are excluded from making the web.”[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70634)Posted by[Michael Spellacy (Spell)](https://twitter.com/Spellacy/status/1117072632787214336)onSaturday, April 13th, 2019 at 2:30pm

### [Kevin Stewart](https://twitter.com/kstewart/status/1117073163139989510)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050) via [@instapaper](https://twitter.com/instapaper)

[#](https://adactio.com/journal/15050#comment70635)Posted by[Kevin Stewart](https://twitter.com/kstewart/status/1117073163139989510)onSaturday, April 13th, 2019 at 2:32pm

### [@kethinov@mastodon.social](https://twitter.com/kethinov/status/1117114295815430144)

Of the many things to praise about [@adactio](https://twitter.com/adactio)’s new piece, one thing in particular I want to highlight is it helps to illustrate that progressive enhancement is good not just because it benefits users but also because it helps minimize needless complexity. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70640)Posted by[@kethinov@mastodon.social](https://twitter.com/kethinov/status/1117114295815430144)onSaturday, April 13th, 2019 at 5:16pm

### [TTimes](https://twitter.com/twt04/status/1117129068196003843)

Top story: Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050), see more [tweetedtimes.com/TwtTimesTop?s=…](http://tweetedtimes.com/TwtTimesTop?s=tnp)[(L)](http://tweetedtimes.com/TwtTimesTop)

[#](https://adactio.com/journal/15050#comment70642)Posted by[TTimes](https://twitter.com/twt04/status/1117129068196003843)onSaturday, April 13th, 2019 at 6:14pm

### [webuproar](https://twitter.com/webuproar/status/1117155830711955456)

 [adactio.com/journal/15050?…](https://adactio.com/journal/15050?utm_source=webuproar) Split[(L)](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70643)Posted by[webuproar](https://twitter.com/webuproar/status/1117155830711955456)onSaturday, April 13th, 2019 at 8:01pm

### [Peter Müller](https://twitter.com/pmmueller/status/1117169801783382016)

As many times before, Jeremy Keith wrote something that’s really worth every minute spent reading. Thanks. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70644)Posted by[Peter Müller](https://twitter.com/pmmueller/status/1117169801783382016)onSaturday, April 13th, 2019 at 8:56pm

### [Sérgio Santos](https://twitter.com/s3rgiosan/status/1117185715048255488)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050) by [@adactio](https://twitter.com/adactio)

[#](https://adactio.com/journal/15050#comment70645)Posted by[Sérgio Santos](https://twitter.com/s3rgiosan/status/1117185715048255488)onSaturday, April 13th, 2019 at 10:00pm

### [Chris Pearce](https://twitter.com/chris__pearce/status/1117253384698941440)

Split by [@adactio](https://twitter.com/adactio) is spot on & well worth a read (all his stuff is).[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70646)Posted by[Chris Pearce](https://twitter.com/chris__pearce/status/1117253384698941440)onSunday, April 14th, 2019 at 2:28am

### [Steve Souders](https://twitter.com/Souders/status/1117449299292377094)

A beautifully written and insightful perspective from [@adactio](https://twitter.com/adactio) on tools, UX, and most importantly making THE Web something that *everyone* should be able to mold to be THEIR Web:[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70650)Posted by[Steve Souders](https://twitter.com/Souders/status/1117449299292377094)onSunday, April 14th, 2019 at 3:27pm

### [James Young](https://twitter.com/jydesign/status/1117807794739187719)

Adactio: Journal—Split: “If we make it so that you have to understand programming to even start, then we take something open and enabling, and place it back in the hands of those who are already privileged.” [adactio.com/journal/15050](https://adactio.com/journal/15050) by [@adactio](https://twitter.com/adactio)

[#](https://adactio.com/journal/15050#comment70670)Posted by[James Young](https://twitter.com/jydesign/status/1117807794739187719)onMonday, April 15th, 2019 at 3:12pm

### [Jacky](https://twitter.com/jackysee/status/1117984304385155073)

Adactio: Journal—Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70675)Posted by[Jacky](https://twitter.com/jackysee/status/1117984304385155073)onTuesday, April 16th, 2019 at 2:53am

### [Marco Hengstenberg](https://twitter.com/nice2meatu/status/1118096297263812608)

Herr [@adactio](https://twitter.com/adactio) Keith, I love your article![adactio.com/journal/15050](https://adactio.com/journal/15050)This is such an important article and most important to me is the final sentence: “But the split that worries the most is this: • The people who make the web vs. the people who are excluded from making the web.”

[#](https://adactio.com/journal/15050#comment70677)Posted by[Marco Hengstenberg](https://twitter.com/nice2meatu/status/1118096297263812608)onTuesday, April 16th, 2019 at 10:18am

### [Jennifer Robbins](https://twitter.com/jenville/status/1118161420351414272)

I love the way [@adactio](https://twitter.com/adactio) looks at things in this article: [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70678)Posted by[Jennifer Robbins](https://twitter.com/jenville/status/1118161420351414272)onTuesday, April 16th, 2019 at 2:37pm

### [ゆ](https://twitter.com/uknmr/status/1118217007172734977)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70703)Posted by[ゆ](https://twitter.com/uknmr/status/1118217007172734977)onTuesday, April 16th, 2019 at 6:18pm

### [mirthe.org](https://mirthe.org/2019/01/divide/)

[#](https://adactio.com/journal/15050#comment70711)Wednesday, April 17th, 2019 at 2:25pm

### [John Ossoway](https://twitter.com/ottomancer/status/1118552391798931457)

Really interesting article from [@adactio](https://twitter.com/adactio), grappling with interesting and important concepts around making the web. I’ve been trying to describe “front of the front end vs. back of the front end” for years, and finally here is the phrase I was looking for![adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70713)Posted by[John Ossoway](https://twitter.com/ottomancer/status/1118552391798931457)onWednesday, April 17th, 2019 at 4:30pm

### [Matt Hill](https://twitter.com/matthillco/status/1118801993701699584)

I’ve read this article a few times now since [@adactio](https://twitter.com/adactio) published it last week. It resontes with me so much: [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70720)Posted by[Matt Hill](https://twitter.com/matthillco/status/1118801993701699584)onThursday, April 18th, 2019 at 9:02am

### [Imani's Father](https://twitter.com/_idkjs/status/1118863007713497088)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70721)Posted by[Imani's Father](https://twitter.com/_idkjs/status/1118863007713497088)onThursday, April 18th, 2019 at 1:05pm

### [Proko Mountrichas](https://twitter.com/proko_moun/status/1119156593692516352)

Great read as always, from Jeremy Keith [adactio.com/journal/15050](https://adactio.com/journal/15050) and great chance to comment on entry barrier and privileges. 1/6

[#](https://adactio.com/journal/15050#comment70750)Posted by[Proko Mountrichas](https://twitter.com/proko_moun/status/1119156593692516352)onFriday, April 19th, 2019 at 8:31am

### [CityDale](https://twitter.com/CityDale/status/1119175286388658177)

This is for everyone… or is it? Great article by [@adactio](https://twitter.com/adactio) on [#webdevelopment](https://twitter.com/search?q=%23webdevelopment) , highlighting a worry of [#privilege](https://twitter.com/search?q=%23privilege) over entry level [#html](https://twitter.com/search?q=%23html)  [#css](https://twitter.com/search?q=%23css) and [#javascript](https://twitter.com/search?q=%23javascript)  [adactio.com/journal/15050](https://adactio.com/journal/15050) Thanks to Justin [@ResWebDes](https://twitter.com/ResWebDes) for the link

[#](https://adactio.com/journal/15050#comment70752)Posted by[CityDale](https://twitter.com/CityDale/status/1119175286388658177)onFriday, April 19th, 2019 at 9:45am

### [Paulo](https://twitter.com/arakno/status/1119501065358053376)

This [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70759)Posted by[Paulo](https://twitter.com/arakno/status/1119501065358053376)onSaturday, April 20th, 2019 at 7:20am

### [Peter Chapman](https://twitter.com/pychap/status/1119758987212099584)

Experiencing some real pain learning (unsuccessfully so far) styling in a JS environ (LitHTML), I appreciate this: [adactio.com/journal/15050](https://adactio.com/journal/15050) Like my young daughter struggling over a new flip routine, I’m currently stumped.

[#](https://adactio.com/journal/15050#comment70804)Posted by[Peter Chapman](https://twitter.com/pychap/status/1119758987212099584)onSunday, April 21st, 2019 at 12:25am

### [Ben Wong](https://twitter.com/benwong/status/1120837015367372801)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050) via [@instapaper](https://twitter.com/instapaper)

[#](https://adactio.com/journal/15050#comment70897)Posted by[Ben Wong](https://twitter.com/benwong/status/1120837015367372801)onTuesday, April 23rd, 2019 at 11:49pm

### [azu](https://twitter.com/azu_re/status/1120888720842903552)

見てる: “Adactio: Journal—Split” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70899)Posted by[azu](https://twitter.com/azu_re/status/1120888720842903552)onWednesday, April 24th, 2019 at 3:14am

### [pipopotamasu(村上大和)](https://twitter.com/pipopotamasu3/status/1120893585451151361)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70900)Posted by[pipopotamasu(村上大和)](https://twitter.com/pipopotamasu3/status/1120893585451151361)onWednesday, April 24th, 2019 at 3:33am

### [Takuji Shimokawa](https://twitter.com/shimokawa/status/1120931448867840000)

“But the split that worries the most is this: The people who make the web vs. the people who are excluded from making the web” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70902)Posted by[Takuji Shimokawa](https://twitter.com/shimokawa/status/1120931448867840000)onWednesday, April 24th, 2019 at 6:04am

### [Paul Jardine Web Design](https://twitter.com/pjwebdesign/status/1120968116777963520)

[#FrontEnd](https://twitter.com/search?q=%23FrontEnd) development has split over the last few years, and this article by [@adactio](https://twitter.com/adactio) offers an interesting take. I’m definitely someone more interested in the ‘materials’ of HTML/CSS/JS than the tools.[adactio.com/journal/15050](https://adactio.com/journal/15050)  [#webdevelopment](https://twitter.com/search?q=%23webdevelopment)  [#webdev](https://twitter.com/search?q=%23webdev)

[#](https://adactio.com/journal/15050#comment70906)Posted by[Paul Jardine Web Design](https://twitter.com/pjwebdesign/status/1120968116777963520)onWednesday, April 24th, 2019 at 8:30am

### [Reuben Walker, Mobile Atom Media](https://twitter.com/mobileatom/status/1121176566829125632)

Split: the front of the front end and the back of the front end vs the backend in [#WebDevelopment](https://twitter.com/search?q=%23WebDevelopment) - [adactio.com/journal/15050](https://adactio.com/journal/15050)  [adactio.com/journal/15050?…](https://adactio.com/journal/15050?utm_source=Responsive+Design+Weekly&utm_campaign=ac6dd361f0-RWD_Newsletter_356&utm_medium=email&utm_term=0_df65b6d7c8-ac6dd361f0-58971489&mc_cid=ac6dd361f0&mc_eid=00711a6d63)[(L)](https://adactio.com/journal/15050?mc_cid=ac6dd361f0&mc_eid=00711a6d63)

[#](https://adactio.com/journal/15050#comment70910)Posted by[Reuben Walker, Mobile Atom Media](https://twitter.com/mobileatom/status/1121176566829125632)onWednesday, April 24th, 2019 at 10:18pm

### [Yoshiya / ひのさわ / かた(肩)](https://twitter.com/kt3k/status/1121364210061996032)

react が web を作る人を2分してしまっているのではないか, みたいな話 [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70912)Posted by[Yoshiya / ひのさわ / かた(肩)](https://twitter.com/kt3k/status/1121364210061996032)onThursday, April 25th, 2019 at 10:43am

### [Vivian Farrell](https://twitter.com/viv_f/status/1122752318837903361)

Great exploration and mental model of current day web development. More ammo to take to decision makers who downplay the front end. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70965)Posted by[Vivian Farrell](https://twitter.com/viv_f/status/1122752318837903361)onMonday, April 29th, 2019 at 6:39am

### [Trinity Takei](https://twitter.com/TrinityTakei/status/1122857820762849281)

How to Think Like a Front-End Developer by Chris Coyier | [buff.ly/2UvoB4J](https://buff.ly/2UvoB4J)“You could imagine two people called front-end developers meeting, and having nothing in common to talk about” — [@adactio](https://twitter.com/adactio)[@chriscoyier](https://twitter.com/chriscoyier) calls this a “front-end identity crisis”.[(L)](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment70998)Posted by[Trinity Takei](https://twitter.com/TrinityTakei/status/1122857820762849281)onMonday, April 29th, 2019 at 1:39pm

### [tomkersten](https://twitter.com/tomkersten/status/1122877794663522306)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71000)Posted by[tomkersten](https://twitter.com/tomkersten/status/1122877794663522306)onMonday, April 29th, 2019 at 2:58pm

### [Zach Leatherman](https://twitter.com/zachleat/status/1122899200923131911)

“Maybe the materials are the ‘external’ technologies, because they’re what users will interact with. Whereas all the other technologies—that mostly live on a developer’s machine—are the ‘internal’ technologies.”—[@adactio](https://twitter.com/adactio) writes:[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71001)Posted by[Zach Leatherman](https://twitter.com/zachleat/status/1122899200923131911)onMonday, April 29th, 2019 at 4:23pm

### [Harmen Janssen](https://twitter.com/harmenjanssen/status/1122915530195775489)

A must read by [@adactio](https://twitter.com/adactio) on how your tech choices affect your users. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71003)Posted by[Harmen Janssen](https://twitter.com/harmenjanssen/status/1122915530195775489)onMonday, April 29th, 2019 at 5:28pm

### [Logan Franken](https://twitter.com/loganfranken/status/1123035635718090752)

I share a lot of the concerns here, but I’ve also met a lot of people who have found an *entry point* into tech via all of the new JS tools [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71017)Posted by[Logan Franken](https://twitter.com/loganfranken/status/1123035635718090752)onTuesday, April 30th, 2019 at 1:25am

### [Some(@cλbai)](https://twitter.com/_cybai/status/1123623102867369984)

[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71050)Posted by[Some(@cλbai)](https://twitter.com/_cybai/status/1123623102867369984)onWednesday, May 1st, 2019 at 4:19pm

### [DEVELOPER NEWZ](https://twitter.com/developernewz/status/1124051575331262464)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71067)Posted by[DEVELOPER NEWZ](https://twitter.com/developernewz/status/1124051575331262464)onThursday, May 2nd, 2019 at 8:42pm

### [freshmade](https://twitter.com/itsfreshmade/status/1124066420374024192)

Split [adactio.com/journal/15050?…](https://adactio.com/journal/15050?utm_source=dlvr.it&utm_medium=twitter) via [@chriscoyier](https://twitter.com/chriscoyier)[(L)](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71068)Posted by[freshmade](https://twitter.com/itsfreshmade/status/1124066420374024192)onThursday, May 2nd, 2019 at 9:41pm

### [Adam Tomat](https://twitter.com/adamtomat/status/1124218668949356545)

Absolutely love this article by [@adactio](https://twitter.com/adactio)“As a user-centred developer, my priority is doing what’s best for end users. That’s not to say I don’t value developer convenience. I do. But I prioritise user needs over developer needs.” Go read it [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71069)Posted by[Adam Tomat](https://twitter.com/adamtomat/status/1124218668949356545)onFriday, May 3rd, 2019 at 7:46am

### [Alessandro Casazza](https://twitter.com/imasterale/status/1124228417178755072)

Split [adactio.com/journal/15050](https://adactio.com/journal/15050)  [#webdesign](https://twitter.com/search?q=%23webdesign)  [#feedly](https://twitter.com/search?q=%23feedly)

[#](https://adactio.com/journal/15050#comment71070)Posted by[Alessandro Casazza](https://twitter.com/imasterale/status/1124228417178755072)onFriday, May 3rd, 2019 at 8:25am

### [Randy Hammons](https://twitter.com/optikinescant/status/1124318022750150657)

So much of this. [adactio.com/journal/15050](https://adactio.com/journal/15050) Wise observation from [@adactio](https://twitter.com/adactio) on ‘the great divide’ conversation.

[#](https://adactio.com/journal/15050#comment71094)Posted by[Randy Hammons](https://twitter.com/optikinescant/status/1124318022750150657)onFriday, May 3rd, 2019 at 2:21pm

### [Max Antonucci](https://twitter.com/Maxwell_Dev/status/1124396983656026112)

This [@adactioJournal](https://twitter.com/adactioJournal) on the different divides between areas of the [#frontend](https://twitter.com/search?q=%23frontend) is a great read. Read through it all! [#webdev](https://twitter.com/search?q=%23webdev)[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71097)Posted by[Max Antonucci](https://twitter.com/Maxwell_Dev/status/1124396983656026112)onFriday, May 3rd, 2019 at 7:35pm

### [Bryan Kearney](https://twitter.com/bryandavidk/status/1125046886463954945)

“Complexity reinforces privilege.” Damn. Great concept. Now apply it to other things besides computers and front-end design,[adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71101)Posted by[Bryan Kearney](https://twitter.com/bryandavidk/status/1125046886463954945)onSunday, May 5th, 2019 at 2:37pm

### [Fullstack Developer](https://twitter.com/FullstackDevJS/status/1125279047737647105)

Split [#Frontend](https://twitter.com/search?q=%23Frontend)  [#devTips](https://twitter.com/search?q=%23devTips)  [#Devlife](https://twitter.com/search?q=%23Devlife)  [#Design](https://twitter.com/search?q=%23Design)  [#Css](https://twitter.com/search?q=%23Css)  [#HTML](https://twitter.com/search?q=%23HTML)  [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71104)Posted by[Fullstack Developer](https://twitter.com/FullstackDevJS/status/1125279047737647105)onMonday, May 6th, 2019 at 6:00am

### [azu](https://twitter.com/azu_re/status/1125409870537060352)

Complexity reinforces privilege 複雑さは特権を強化する。 ReactやSSRなどフレームワークやツールによって二分されていく傾向が続いたばあいの問題 “Adactio: Journal—Sp…” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71106)Posted by[azu](https://twitter.com/azu_re/status/1125409870537060352)onMonday, May 6th, 2019 at 2:39pm

### [Jamie Klenetsky Fay](https://twitter.com/jamieklenetsky/status/1125491768554815488)

“My greatest fear for the web is that it becomes the domain of an elite priesthood of developers.” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71108)Posted by[Jamie Klenetsky Fay](https://twitter.com/jamieklenetsky/status/1125491768554815488)onMonday, May 6th, 2019 at 8:05pm

### [Matthew Cox](https://twitter.com/UXdesignman/status/1125494339331919872)

Interesting thoughts by [@adactio](https://twitter.com/adactio) on keeping the maker/hacker presence of the web instead of limiting ability-to-create to those with a CS degree. I totally agree, we should work to make it so that anyone with a text editor can create for the web. [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71109)Posted by[Matthew Cox](https://twitter.com/UXdesignman/status/1125494339331919872)onMonday, May 6th, 2019 at 8:15pm

### [Paul Jardine Web Design](https://twitter.com/pjwebdesign/status/1128246074827689985)

[#FrontEnd](https://twitter.com/search?q=%23FrontEnd) dev has split over the last few years, and this article offers an interesting perspective on the shift.[adactio.com/journal/15050](https://adactio.com/journal/15050) (by [@adactio](https://twitter.com/adactio))

[#](https://adactio.com/journal/15050#comment71271)Posted by[Paul Jardine Web Design](https://twitter.com/pjwebdesign/status/1128246074827689985)onTuesday, May 14th, 2019 at 10:30am

### [Tobias Sawitzki](https://twitter.com/tsawitzki/status/1129441516857024512)

Top article by [@adactio](https://twitter.com/adactio): “It surprises me when I see the question of server rendering or client rendering treated almost like an implementation detail. It might be an implementation detail from a developer’s perspective, but it’s a key decision for the UX” [adactio.com/journal/15050](https://adactio.com/journal/15050)

[#](https://adactio.com/journal/15050#comment71537)Posted by[Tobias Sawitzki](https://twitter.com/tsawitzki/status/1129441516857024512)onFriday, May 17th, 2019 at 5:40pm

### 2 Shares

[#](https://adactio.com/journal/15050#comment70559)Thursday, April 11th, 2019 at 7:41pm

[#](https://adactio.com/journal/15050#comment70641)Shared by[Aleksi Peebles](https://twitter.com/aleksip/status/1117014719112654848)onSaturday, April 13th, 2019 at 10:40am

### 5 Likes

[#](https://adactio.com/journal/15050#comment70532)Liked by[Trys Mudford](https://twitter.com/adactioJournal/status/1115989482656944128#favorited-by-46959723)onThursday, April 11th, 2019 at 3:52am

[#](https://adactio.com/journal/15050#comment70593)Friday, April 12th, 2019 at 12:40pm

[#](https://adactio.com/journal/15050#comment70607)Liked by[Sebas](https://twitter.com/adactioJournal/status/1115989482656944128#favorited-by-8398492)onFriday, April 12th, 2019 at 6:20pm

[#](https://adactio.com/journal/15050#comment70626)Liked by[Aleksi Peebles](https://twitter.com/adactioJournal/status/1115989482656944128#favorited-by-8388012)onSaturday, April 13th, 2019 at 10:54am

[#](https://adactio.com/journal/15050#comment71105)Liked by[Léonard Messier](https://twitter.com/adactioJournal/status/1115989482656944128#favorited-by-235066633)onMonday, May 6th, 2019 at 10:00am

### 2 Bookmarks

[#](https://adactio.com/journal/15050#comment70566)Bookmarked by[Chris Aldrich](https://boffosocko.com/2019/04/11/split-jeremy-keith/)onThursday, April 11th, 2019 at 1:31pm

[#](https://adactio.com/journal/15050#comment70567)Bookmarked by[Calum Ryan](https://calumryan.com/note/2561)onThursday, April 11th, 2019 at 10:59pm

### About this site

[Adactio](https://adactio.com/) is the online home of [Jeremy Keith](https://adactio.com/journal/15050mailto:jeremy@adactio.com), a web developer and author living and working in Brighton, England.

[Get in touch](https://adactio.com/contact/)

### Customise

Choose a theme…
[?](https://adactio.com/about/site/)
This is the plain vanilla look.

### Search

Search the journal:

- Peruse the [archive](https://adactio.com/journal/archive/)
- Browse the [tags](https://adactio.com/journal/tags/)

### Subscribe

You can subscribe to the [journal RSS feed](https://adactio.com/journal/rss) or you can follow [@adactioJournal](https://twitter.com/adactioJournal) on Twitter.

### Recommended reading

Hand-picked highlights from the archive.
-

#### [Split](https://adactio.com/journal/15050)

Materials and tools; client and server; declarative and imperative; inclusion and privilege.

-

#### [Web! What is it good for?](https://adactio.com/journal/9016)

Not absolutely nothing, but not absolutely everything either.
-

#### [Seams](https://adactio.com/journal/6786)

There is a crack, a crack in everything. That’s how the light gets in.
-

#### [Hyperdrive](https://adactio.com/journal/1283)

Last night in San Francisco.
-

#### [Design doing](https://adactio.com/journal/1376)

The opposite of design thinking.
-

#### [Iron Man and me](https://adactio.com/journal/1530)

The story of how one of my Flickr pictures came to be used in a Hollywood movie.

© 1998 - 2019 [Jeremy Keith](https://adactio.com/journal/15050mailto:jeremy@adactio.com).