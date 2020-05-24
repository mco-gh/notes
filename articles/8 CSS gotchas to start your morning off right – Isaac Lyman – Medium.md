8 CSS gotchas to start your morning off right – Isaac Lyman – Medium

![](../_resources/ba9393bb6178be709cdb06bc7a1fbe66.png)![1*etHN0X12v4fjyQdRTMjqmg.png](../_resources/6202647f2108e0a11f13eeb8a3642bf4.png)

# 8 CSS gotchas to start your morning off right

In every community there’s a coming-of-age process, a rite of passage that every newcomer must experience before he or she can really be considered an insider. For the CSS community, it goes something like this:

> Hey, this page is almost perfect. Can you just center that icon vertically? I told the boss we can roll it live in five minutes.

For CSS junkies like me, lines like this provoke an involuntary nervous giggle, the kind of giggle you’ll hear if I tell you about the first time I got dumped or crashed my car. In the old days, before CSS Grid, before Flexbox, before “Computer Science” [got renamed to “Googling Stack Overflow,](http://www.theallium.com/engineering/computer-programming-to-be-officially-renamed-googling-stackoverflow/)” vertical centering was just something that CSS didn’t really do. It was like asking for a root beer float at McDonald’s. If you were persistent enough, eventually you’d get something that looked like what you wanted — but it would just be a polite facade, the veneer over a barely-contained puddle of disappointment.

![](../_resources/002606228444ed60fb2f481284b010c3.png)![1*NJ10ZGyIkj5vYTsnKzTy6A.jpeg](../_resources/6954c38c375112e42a3405f4b2daf8a8.jpg)

There were a few people who knew, offhand, five or six lines of clunky CSS that would do the trick. They were *janky* lines, too. It was commonly known that if you recited them backwards, they would summon the fiery apparition of Herbie the Love Bug. The people who had them memorized were totally obsessed; they were the Web 1.0 version of crossfitters and vegans. They weren’t much good for web development in general, but boy, did they ever know how to put something exactly between the top and bottom of a `<div>`. By the time their Stack Overflow answers on the subject became obsolete, they were able to cash out their reputation points and retire early. It was a charmed life. Their homes in Seattle (the primordial soup that Silicon Valley evolved from) have been preserved for posterity. You can go by any time and see how they lived. All their countertops are exactly waist-height. Their paintings hang with a margin of exactly 3.5 feet above and below. Their shower-heads are in the middle of the wall and spray upward and downward with equal pressure.

Anyway, CSS has a long history of providing frustrating and nonsensical solutions to the simplest problems of front-end design, while thoughtfully implementing one-line features to solve problems nobody cares about (ever heard of `mix-blend-mode`? Didn’t think so.) After a few years in the trenches, I’ve met my fair share of both. Following is a list of some of the biggest surprises you’re liable to face as a CSS newbie, and some advice for navigating them.

**1 — Vertical centering is hard**

Like I said, vertical centering used to be a messed-up gig. You had to relatively position something at 50% the height of its parent element, then give it a top margin of -50% of itself, and there was a special tax form you had to fill out, and sometimes the effect was only temporary and you had to cast it again a few days later.

These days, things are much better. If you use flexbox, you can set `align-items` or `justify-content` on the parent element (depending on its flex alignment) and you’re on your way.

You may be wondering what the `vertical-align` property does. The answer is “jack squat, except on an HTML table.” Never heard of HTML tables? That’s because they’re not cool. If you use them you can expect to be ostracized from the development community forever. Why? Because, much like the Spice Girls, they were way too popular in the 90’s and everyone got sick of them.

Some people claim that `vertical-align` also works on inline elements. These people are liars. You should run away from them.

**2 — **`**100%**`** of what, exactly?**

You may think that setting the `width` property to `100%` on any element will make it fill the entire horizontal space allotted to its parent element. But sometimes it won’t. Sorry, newbie.

First of all, this doesn’t work for inline elements (like `<span>` and `<i>`) and certain table elements. Second of all, it doesn’t work if its parent’s width isn’t explicitly specified — so good luck making it work inside an element that’s all funky-dory with flexbox. And lastly, `margin` properties are applied on top of the calculated width, so if your element has a margin on the left side, it’s gonna jut out like Aunt Marge’s pregnant belly.

![](../_resources/7d351503661b3ff1dfed43f7d9059a4c.png)![1*BLeceeV94FZuauUHVWLwtg.gif](../_resources/58088026ef62583c8b58489b45562c96.gif)

Trying to fit your content into a dynamically-sized <div>

Just save yourself some trouble and make really small websites. Hopefully you won’t have to make anything that’s 100% of anything else.

**3 — If you **`**float**`**, you will eventually **`**sink**`
Here’s a trick question for you:

> I have three sibling `<div>`> s. The first one is positioned with `float: left`> . The middle one is positioned with `float: right`> . The last one, like the first, is positioned with `float: left`> . Is this last `<div>`> :

> A) Aligned horizontally with the first two, but after both of them?
> B) On the row after the first two, on the far left side?
> C) On the row after the first two, on the far right side?

Think about it for a minute. Pop open your IDE of choice and try it, if you want.

The answer, as you may have discovered, is actually *D) None of the above*. The last div appears just to the right of the first one. That’s right, CSS will blatantly ignore the stated order of your HTML elements and just do whatever the heck it wants. Or, [as the CSS spec states](https://www.w3.org/TR/CSS2/visuren.html#floats):

> […] > CSS cares nothing for your whims. Nothing for your dreams. Nothing for your foolish allocations of space and time and meaning. To discover CSS is to discover a space void of progress, a universe with no moral absolutes where your carefully-planned DOM structure is just a scream into the endless void. […] Nowhere shall this sublimity of chaos be more evident than in the interaction of such properties as `float`> , `clear`> , and `display`> . You may say their names. You may vainly wish to invoke their powers. But tread lightly, because **> you*>   *> cannot*>   *> control them**> .

> Thus let it be written.
**4 — You can’t learn your way out of CSS problems**

As every seasoned web developer knows, CSS isn’t implemented according to a specification of rigid, predictable rules. If it were, we would all just learn the rules and go on to lead happy and successful lives. Rather, it’s built with a clever *O(N log N)* complexity algorithm at the core which ensures that the only correlative to your success with any one problem is the amount of time you’ve already spent messing around. That is, there’s no hard-and-fast rule about when to use `white-space: nowrap`, but multiple studies have found that it’s far more likely to work during the fifth hour of debugging than the first. And don’t bother trying to outsmart it: CSS can tell when you’re just going through the motions (cycling through properties, trying different values for `display` and `position`). The clock doesn’t start until you’re really upset.

In the course of your career you may meet people who self-identify as “CSS gurus.” They can solve styling problems instantly and they smile as they rattle off nonsensical reasons for why things work the way they do (they may use mystical phrases like “stacking context” and “clearfix” — these are minor deities of the CSS underworld). You should know that there’s nothing supernatural about these people. Through repeated exposure, meditation and self-flagellation they have learned to internalize enormous amounts of frustration in order to overclock CSS’s complexity algorithm. In other words, they experience the same amount of anger and hopelessness in five minutes of CSS debugging that you experience over several hours. In all likelihood, they aren’t smiling at you; their face is broken from the strain. Most of them will die of a triple heart attack by the time they’re 40.

**5 — **`**z-index**`** isn’t a real CSS attribute**

The first few times you stumble upon the `z-index` attribute, you’ll brighten immediately. “Wow!” you’ll think. “This solves all my problems!” After three hours wondering why it doesn’t do anything, you’ll realize that you were wrong. `z-index` isn’t a functioning CSS property. It’s a cruel joke.

![](../_resources/9721d9a5351040030f464b5803bf675f.png)
“Maybe z-index will work this time.”

Some believe that the maintainers of CSS penciled `z-index` into the spec in order to explore its possible use for situations where multiple elements share the same space; unfortunately, it is said, they never got around to specifying its behavior and it was only left in the documentation so that people would stop asking for it.

I find this legend to be a little too benevolent. During the centuries-long history of the curation of CSS, not a single maintainer has ever showed any interest in improving its usefulness (or in listening to its user base). It’s more plausible to me that `z-index` is a sort of never-ending rickroll, a prank call to every developer who tries their hand at styling web pages. I can see the maintainers now, mentoring young and talented developers, asking, “Have you tried `z-index`?” and then scurrying off red-faced to a bathroom stall to burst into fits of private laughter.

**6 — CSS doesn’t stand for “Cascading Style Sheets”**

Yes, you read that right. The whole “Cascading Style Sheets” rumor started with a rather dull article on The Onion that got picked up by Hacker News, shared, republished and remixed until the original was forgotten. The phrase has become such a central part of the discourse on CSS that even professional developers and conference presenters — people who ought to know better — propagate it endlessly.

CSS actually stands for “Ceaseless Screaming of the Sinner.” Contrary to popular belief, it predates the Internet by centuries. It was invented as a side project by Johann Wolfgang von Goethe while he was writing *Faust*, and he originally intended to integrate it into the play as the dramatic system of punishment administered to the condemned in his imagined hell. However, he ultimately abandoned the project when it proved to be so bleak and dismal that he feared it would ruin the entire play.

When Tim Berners-Lee invented the Internet a few hundred years later, as we all know, he did so in a tremendous hurry because he wanted to finish it before Y2K and the Dot-Com crash could destroy it. Lacking the time to compose a decent page styling mechanism, he grabbed the closest document he had on hand — a carbon-copy set of Goethe’s collected papers — and used the ancient system it described. His only changes were to translate each selector and property from German into English. If you want to see this Version 1 in its original form, you can look at the stylesheets for [craigslist.org](http://craigslist.org/), which, due to an unfortunate combination of now-forbidden styles on its `<body>` tag, is cursed to forever look like a geocities site hacked together in a single weekend by an ascetic monk.

**7 — CSS is a raging battle in the heart of the abyss**

If you become part of a modern web project more than six months old, you’ll probably discover several competing legions of CSS. There will be a couple of stylesheets from Bootstrap, a few from jQuery Mobile, a CSS reset, a bunch of Angular plugins, and hundreds of styles that are custom to the project. Do these styles work together harmoniously? Consult the following equation to calculate the probability:

> x = *> nope*> .

Those stylesheets are fighting tooth and nail for every last scrap of DOM. Only through exceptionally specific selectors and heavy-handed application of the `!important` hammer are the project’s maintainers able to keep order. And every time they write a new `<a>` or `<span>`, they again have to duke it out for its `color`, `font-size`, `padding`, and `outline`.

You may find that leaving this battle unattended can have serious consequences. Many times I’ve left work after finally getting a page to look right, only to return the next morning and find that an entire `<aside>` has disappeared (and only in Internet Explorer, famed for being the first piece of software to break every single Geneva Convention).

The sooner you learn this the better: CSS is both violent and ruthless. It doesn’t wait for commands and doesn’t respond to oversight. The longer you allow it to fester, the more aberrations it will produce. You cannot overpower it, but you may be able to outlast it. And if you can’t, maybe it’s time to transition into something less demanding, like embedded systems or financial programming.

**8 — CSS has a secret menu**

Have you ever ordered something from the secret menu at In-N-Out Burger? You probably discovered the reason that the menu is secret: it isn’t very good. For example, if you order fries “animal style”, they will literally shake the dandruff from a small rabbit onto your fries before you get them. True story.

CSS also has a secret menu, and it’s also not very good. For example, you’re probably familiar with these:

`height: 17.4px;`
`height: 2em;`
`height: 50%;`
And you may even have heard of this:
`height: 25vh;`

Which, like `z-index`, is more of a cruel joke than a functioning attribute. But have you heard of these?

`height: unset;`
`height: inherit;`

`height: There standeth Minos horribly, and snarls; examines the transgressions at the entrance; judges, and sends according as he girds him. (*The Inferno*, Canto V);`

I think it’s pretty obvious what each of these does. Needless to say, if you find yourself in a position where you need to use them, you’ve done something wrong already. You should go back and refactor your career.

* * *

*...*

With any luck, this list of CSS gotchas will save you some trouble the next time you have to style a web page. Good luck!