CommonMark

# CommonMark

## A strongly defined, highly compatible specification of Markdown

##   [(L)](http://commonmark.org/#what)What is Markdown?

It’s a plain text format for writing structured documents, based on formatting conventions from email and usenet.

 [Learn Markdown in 60 Seconds](http://commonmark.org/help/)

##   [(L)](http://commonmark.org/#what)Who created Markdown?

It was [developed in 2004 by John Gruber](https://en.wikipedia.org/wiki/Markdown#History), who wrote the first markdown-to-html converter in Perl, and it soon became widely used in websites. By 2014 there were dozens of implementations in many languages.

##   [(L)](http://commonmark.org/#why)Why is CommonMark needed?

John Gruber’s [canonical description of Markdown’s syntax](http://daringfireball.net/projects/markdown/syntax) does not specify the syntax unambiguously.

In the absence of a spec, early implementers consulted the original `Markdown.pl` code to resolve these ambiguities. But `Markdown.pl` was quite buggy, and gave manifestly bad results in many cases, so it was not a satisfactory replacement for a spec. `Markdown.pl` was last updated December 17th, 2004.

Because there is no unambiguous spec, implementations have diverged considerably over the last 10 years. As a result, users are often surprised to find that a document that renders one way on one system (say, a GitHub wiki) renders differently on another (say, converting to docbook using Pandoc). To make matters worse, because nothing in Markdown counts as a “syntax error,” the divergence often isn’t discovered right away.

There’s no standard test suite for Markdown; [MDTest](https://github.com/michelf/mdtest/) is the closest thing we have. The only way to resolve Markdown ambiguities and inconsistencies is [Babelmark](http://johnmacfarlane.net/babelmark2/), which compares the output of 20+ implementations of Markdown against each other to see if a consensus emerges.

We propose a **standard, unambiguous syntax specification for Markdown**, along with a **suite of comprehensive tests** to validate Markdown implementations against this specification. We believe this is necessary, even essential, for the future of Markdown.

That’s what we call **CommonMark**. ![Markdown Logo](../_resources/e6935d7ed33a999823cc998c505961d1.png)

##   [(L)](http://commonmark.org/#who)Who are you?

We’re a group of Markdown fans who either work at companies with industrial scale deployments of Markdown, have written Markdown parsers, have extensive experience supporting Markdown with end users – or all of the above.

- **John MacFarlane**, jgm@berkeley.edu

- **David Greenspan**, david@meteor.com

- **Vicent Marti**, vicent@github.com

- **Neil Williams**, neil@reddit.com

- **Benjamin Dumke-von der Ehe**, ben@stackexchange.com

- **Jeff Atwood**, jatwood@codinghorror.com

##   [(L)](http://commonmark.org/#how)How can I help?

Exercise our [reference implementations](http://code.commonmark.org/), or [find a community implementation](https://github.com/jgm/CommonMark/wiki/List-of-CommonMark-Implementations) in your preferred environment or language. Provide [(L)](http://talk.commonmark.org/)feedback!

If a CommonMark implementation does not already exist in your preferred environment or language, try **implementing your own CommonMark parser**. One of our major goals is to [strongly specify Markdown](http://spec.commonmark.org/), and to eliminate the many old inconsistencies and ambiguities that made using Markdown so difficult. Did we succeed?

##   [(L)](http://commonmark.org/#where)Where can I find it?

###   [spec.commonmark.org](http://spec.commonmark.org/)

The CommonMark specification.

###   [code.commonmark.org](http://code.commonmark.org/)

Reference implementation and validation test suite on GitHub.

###   [talk.commonmark.org](http://talk.commonmark.org/)

Public discussion area and mailing list via [Discourse](http://www.discourse.org/).

###   [commonmark.org/help](http://commonmark.org/help)

Quick reference card and interactive tutorial for learning Markdown.

###   [try.commonmark.org](http://try.commonmark.org/)

Live testing tool powered by the reference implementation.

##   [(L)](http://commonmark.org/#when)When is the spec final?

The current version of the CommonMark spec is complete, and quite robust after a year of public feedback … but not quite final.

With your help, we plan to announce a finalized 1.0 spec and test suite in 2017.

<3