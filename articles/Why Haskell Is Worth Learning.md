Why Haskell Is Worth Learning

March 5, 2013
by:[Job Vranish](https://spin.atomicobject.com/author/vranish/)
[14 Comments](https://spin.atomicobject.com/2013/03/05/why-haskell/#comments)

# Why Haskell Is Worth Learning

When I recommend learning Haskell to the uninitiated, I often get asked: “Why Haskell?” “Is it a practical language?” and “Is it something I can actually *use*?” My answer is definitely **yes**.

Haskell isn’t my primary language at work (I mostly write C code for embedded systems), I’ve still found it incredibly useful. And even if I never used Haskell at work, I would still consider learning it as time well spent. So, why Haskell?

## 1. Haskell Plays Well with C

It turns out Haskell is a very powerful tool for helping you write C. Haskell has let me do things I would normally not even consider to be, umm, *practical*.

Say one of my coworkers wants to find all the places in a legacy codebase that a variable `foo` is used in the conditional of an `if`. Thanks to the awesome [language-c](http://hackage.haskell.org/package/language-c-0.4.2) library and Haskell’s generics, I can write a Haskell function that takes the path to a preprocessed C source as input and outputs the source locations (if any) like so:

|     |
| --- |
| parseAndFindFoos :: FilePath ->  IO  (Either ParseError [Position])parseAndFindFoos path = liftM (fmap findFooLocations)  (parseCFilePre path)<br>findFooLocations input =  fmap posOf (listify isIfOfInterest input)isIfOfInterest (CIf cond _ _ _)  =  not  (null  (listify isFooIdent cond))<br>isFooIdent (Ident name _ _)  = name ==  "foo" |

Not including the type signatures, that’s just 4 lines of Haskell! The type signatures are usually inferred anyway, but it’s customary to include them as doc strings.

This is just a blog-post-sized toy example. I’ve I use Haskell to do far more complicated things, like extracting the names and types of functions and global declarations or performing a transformation that inserts bounds checks or logging functions in expressions that match certain criteria. There are not many other languages that would let me do this as succinctly and quickly as Haskell does.

### I’m Not the Only One Making Tools for C in Haskell

One of my coworkers made an awesome tool called [plunge](https://github.com/sw17ch/plunge) that lets you compare preprocessed code c with the original and shows what each line in the original was processed into in the preprocessed version.

There’s also:

- [atom](http://hackage.haskell.org/package/atom) – A DSL that performs compile-time task scheduling and generates code with deterministic execution time and constant memory.
- [copilot](http://hackage.haskell.org/package/copilot-2.1.0) –  A stream (i.e., infinite lists) domain-specific language (DSL) in Haskell that compiles into embedded C.
- [ImProv](http://hackage.haskell.org/package/improve) – An imperative programming language for high-assurance applications. ImProve uses infinite state, unbounded model checking to verify programs adhere to specifications.

And **many** others.

## 2. Haskell Changes the Way You Think

I really think the most immediately practical side effect *snirk* of learning Haskell is that it forever changes the way you think about code. Yes, yes, I know this sounds like warm, fuzzy, vague BS, but I’m serious! Learning Haskell has had more of an impact on the way I code, and the way I think about code, than anything I learned in school and any of my on-the-job experience.

Have you ever tried to write a complex function without using any mutation? At first it’s quite painful. But once you get some practice, not only does it get much easier, but you start realizing that your functions can get broken apart into much smaller pieces than you originally thought possible. That complex function will turn out to be not all that complex at all; it can be written as just three simple functions composed together!

It’s like if you only played soccer with your right foot. And then one day your coach forbids you from using your right foot. At first you suck at everything. But eventually you become just as good at using your left foot as your right, you and end up being a much better soccer player.

Haskell is so different that it *forces* you to think about your code differently. This is part of why it’s a hard language to learn, but also why learning it is so advantageous.

## 3. Haskell’s Steep Learning Curve Is a Good Thing

The most common complaint people have when learning Haskell is the steep learning curve. And they’re right, it *does* have a steep learning curve. It’s like learning programing all over again. It takes a bit to unlearn the patterns you instinctively want to use. No mutation! Static Typing! OMG they’re passing the value returned from that function as one of its arguments! WTF is going on!?

The hard part about learning Haskell is not the complex things, it’s the simple things. Like Monads; Monads are *ridiculously simple*. They’re just a datatype with an instance implementation of two very simple functions. Most implementations are just one or two lines! It’s the comprehending the implications, usefulness, and power of these very simple things that takes so much work. Profound things take time to learn. This is ok. It means you’re learning something that’s worth learning.

**

> “Do you want to be locked into tricycles because they’re easy to learn?” – Douglas Englebart

**

Share this article:

- [Hackernews](https://news.ycombinator.com/submitlink?u=https://spin.atomicobject.com/2013/03/05/why-haskell/%23.VNUdMcs6UCk.hackernews&t=Why%20Haskell%20Is%20Worth%20Learning)
- [Twitter](https://twitter.com/intent/tweet?text=Why%20Haskell%20Is%20Worth%20Learning&url=https://spin.atomicobject.com/2013/03/05/why-haskell/%23.VNUemPABEaM.twitter&related=)
- [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://spin.atomicobject.com/2013/03/05/why-haskell/%23.VNUemgHMI00.facebook)
- [Googleplus](https://plus.google.com/share?url=https://spin.atomicobject.com/2013/03/05/why-haskell/%23.VNUerUAwXzw.google_plusone_share&t=Why%20Haskell%20Is%20Worth%20Learning)
- [Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https://spin.atomicobject.com/2013/03/05/why-haskell/%23.VNUeuSKf2A4.linkedin&title=Why%20Haskell%20Is%20Worth%20Learning&ro=false&summary=&source=)

Tagged: [c](https://spin.atomicobject.com/tag/c/)  [embedded](https://spin.atomicobject.com/tag/embedded/)  [haskell](https://spin.atomicobject.com/tag/haskell/)Posted  in [Functional Programming](https://spin.atomicobject.com/category/platforms-languages/funct-programming/)

# Related Posts

[(L)](https://spin.atomicobject.com/2017/04/26/ember-pure-computed-properties/)

# [Pure Computed Properties in Ember](https://spin.atomicobject.com/2017/04/26/ember-pure-computed-properties/)

by Shawn Anderson

[(L)](https://spin.atomicobject.com/2017/04/17/javascript-decorators-declaratively-extend-functions/)

# [Using Decorators to Declaratively Extend Functions](https://spin.atomicobject.com/2017/04/17/javascript-decorators-declaratively-extend-functions/)

by William Shawn

[(L)](https://spin.atomicobject.com/2017/03/15/typescript-generate-test-data/)

# [Factory.ts: A Factory Generator for Test Data Using TypeScript](https://spin.atomicobject.com/2017/03/15/typescript-generate-test-data/)

by Will Pleasant-Ryan