On Scaling Mental Models • Buttondown

#  On Scaling Mental Models

### 02/24/2020

## No Newsletter Next Week

I’ll be on vacation in the Caribbean, sipping drinks and juggling for Hermit crabs.

## The Actual Thing

I’m a vim user. I’ve used Vim for ten years now. Well, more like nine years: I didn’t use it in 2017. That’s because my employer started doing more pairing, and nobody could pair with me. It was bad enough for the Atom users, but even the other vimmers couldn’t pair with me. They’d press something expecting the vanilla vim action and get something completely unexpected. It’d drive them crazy.

So I switched to vscode. I didn’t customize it either beyond installing known plugins. It slowed me down, but it meant other people could work with me.

A historical paradox: lispers and smalltalkers said these languages were so much more powerful than anything else available. Paul Graham called Lisp a secret weapon. A couple people working in lisp could move so much faster than people with C++, blah blah etc etc. But most codebases written in Lisp or Smalltalk were moved off it later. The first version of Reddit was in lisp, but they [moved it to Python](https://redditblog.com/2005/12/05/on-lisp/?utm_source=hillelwayne&utm_medium=email&utm_campaign=on-scaling-mental-models). So how do we reconcile “these languages are super powerful” with “they fail at scale”?

The actual answer is probably something boring like “it’s not actually that much better” or “language choice was a proxy for some other confounding factor like programming experience”. But since Computer Things is my place for unedited, unresearched, crackpot ideas, I’m gonna propose the argument that “powerful languages don’t scale”.

(This isn’t a *new* idea. It’s similar to [The Lisp Curse](http://winestockwebdesign.com/Essays/Lisp_Curse.html?utm_source=hillelwayne&utm_medium=email&utm_campaign=on-scaling-mental-models), aka “technical problems become social problems”. But that doesn’t make it any less wildly speculative!)

Programming is an expression of how we think. We take the basic instructions and build abstractions over them. The more power you have in building abstractions, the more you can tailor those abstractions to your exact needs and exactly how *you think*. One example: what should `mydict1 + mydict2` do? It *could* just be an error, but in many cases it’s useful to merge dicts. If you merge dicts, there’s many different useful ways to handle duplicate keys:

- Raise an error, as before
- Have one dict’s choice override the other: `{a: 1} + {a: 'foo'} = {a: 'foo'}`
- Turn the key into a set of both dicts: `{a: 1} + {a: 'foo'} = {a: {1, 'foo'}}`
- Add the values if possible, otherwise fall back to something else: `{a: 1, b: 'foo'} + {a: 2, b: 'bar'} = {a: 3, b: 'foobar'}`
- Only add the values for certain types: `{a: 1, b: 'foo'} + {a: 2, b: 'bar'} = {a: 3, b: 'bar'}`

All of these *could* make sense, depending on your problem domain. In a sufficiently-expressive language, you can make it mean one of these things. Given the following two are equivalent *and* you know what `+` means, which of these is easier to read and write:

1. mydict1.merge(mydict2, handle_duplicates=(key, v1, v2) => v1 + v2)
2. mydict1 + mydict2

*If* you know what `+` means in that context. If you don’t then you’re screwed. While for case #1 you can at least puzzle it out.

This compounds. If you’re working by yourself, you can shape your code and environment to reflect your mental model. This makes it easy to quickly write terse, simple, maintainable code. But it’s hard for other people to work with you. They don’t share your mental model, and they don’t come in with all your initial assumptions. This is somewhat addressable if you all start working on the project together but falls apart when people join on later. The expressivity doesn’t scale. While with using a less expressive language, the working assumptions have to be explicitly built on as boilerplate and abstractions. Harder to work with your own, but easier to work with other people’s.

(Corollary: third party libraries can’t infect your code with their mental model. A coworker once spent hours tracking down a ruby bug that boiled down to “third party library monkey-patched a core method.)

(Corollary 2: It’s easier to write third-party tooling, since you can make more correct assumptions about other people’s code. Go gets flack for its simplicity but I think that simplicity is why there’s so much tooling.)

I like this because it also explains why I switched to VSCode and why most languages discourage macros and metaprogramming.

You just read issue #32 of [Computer Things](https://buttondown.email/hillelwayne).

Computer Things is brought to you by [Buttondown](https://buttondown.email/), the best way to start and run your newsletter.

**Subscribe to Computer Things:**

** Share on Facebook   ** Share on Twitter   ** Share via Email