Replacing the Jet Engine While Still Flying | Jen Simmons

# Replacing the Jet Engine While Still Flying

by Jen Simmons
January 4, 2017

Safari runs on Webkit. Chrome runs on Blink. And Firefox runs on [Gecko](https://en.wikipedia.org/wiki/Gecko_(software)). Which is old. Like really old. I think it’s the oldest rendering engine still in wide use.

Of course, after two decades of experience, we now have Mor Better Ideas™ about how to make a browser rendering engine (and software in general). So for the past several years, Mozilla’s been working on a brand new, top-secret engine. Except it’s totally not top-secret. Never was. At another company it would have been a top-secret project. At [Mozilla](https://www.mozilla.org/en-US/), it’s all done out in the open.

The project is called [Servo](https://servo.org/). It was started as an experiment. It’s coded in a new programming language called [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language)). (Gecko is written in C++.) And it’s open source. You can [totally help us make it](https://github.com/servo/servo).

So what does this mean for Firefox? Well, first, I’m talking about the [rendering engine](https://en.wikipedia.org/wiki/Web_browser_engine) here, not the whole browser. (The rendering engine is the part of the browser that parses and displays each webpage. Which is separate from stuff like tools for managing bookmarks, the URL/search bar, and the menus of Firefoxy things.) If we could snap a finger and magically replace Gecko all at once, normal people would have no idea it’d happened — well, except for the fact websites would load insanely fast. Insanely. Fast. Because Mor Better Ideas™.

The trick of the thing comes with figuring out how to switch from the old rendering engine to a new one. You can’t just do it all at once. It’s like figuring out how to replace a jet engine on a jet that’s still flying. I guess we could land the plane, let all the passengers disembark so they can wander over and take other planes, and not provide any service for a while while we change the engines out… but no — no, we can’t do that. Not gonna happen.

We could keep flying the current plane, while starting from scratch and building an entirely new plane on the ground — special ordering every nut, every bolt, designing a new cockpit, and waiting many years before we to get to fly that plane. But we don’t want to do that either. We already have a giant plane. And it’s a pretty good plane. We should keep using it. We just want a new engine on that plane. As soon as we can get it.

Enter [Quantum](https://medium.com/mozilla-tech/a-quantum-leap-for-the-web-a3b7174b3c12#.9ehkei6jb), the codename for [the project](https://wiki.mozilla.org/Quantum) to figure out how to replace the engine on our still-flying plane. One piece of it is called [Quantum Style](https://wiki.mozilla.org/Stylo)  (aka, Stylo) — that’s where we transition from having Gecko render all the CSS, to using Quantum for CSS. Quantum Style morphs Gecko and Servo together, asking each to do the job they do best. Because, actually, even though it’s been around for 20 years, Gecko does some pretty amazing things, and we want to keep leveraging The Good Parts. New isn’t always better.

At some point in mid-2017, all new CSS will be built with Quantum plane parts, not Gecko. Going forward, it will be much easier and more enjoyable to implement new CSS properties. Which makes it easier for folks in the open source community to contribute. Which makes new things come out faster.

This next year should be a good one for [Firefox](https://www.mozilla.org/en-US/firefox/new/). If you haven’t tried it in a while, do. After refocusing in 2015 and laying groundwork in 2016, Mozilla has setup Firefox to impress over the course of 2017.

*UPDATE: This article has also been published [in French](https://blog.mozfr.org/post/2017/01/Remplacer-moteur-avion-en-plein-vol) and [in Persian](http://rokaweb.ir/%d8%a7%d8%ae%d8%a8%d8%a7%d8%b1/%d8%a7%d8%ae%d8%a8%d8%a7%d8%b1-%d8%af%d9%86%db%8c%d8%a7%db%8c-%d9%88%d8%a8/%d8%aa%d8%b9%d9%88%db%8c%d8%b6-%d9%85%d9%88%d8%aa%d9%88%d8%b1-%d8%ac%d8%aa-%d8%af%d8%b1-%d9%87%d9%86%da%af%d8%a7%d9%85-%d9%be%d8%b1%d9%88%d8%a7%d8%b2/).*