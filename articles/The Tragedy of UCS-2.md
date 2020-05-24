The Tragedy of UCS-2

Apropos of nothing, I'd like to tell you a tale. It's not an original tale, but it's one of my favorites. It's a true tale about standardization, computers, the Unicode consortium, and a few companies.

I'm far from the first person to write about it. However, it's been on my mind lately, and I keep restating it, so I'm formalizing it here in my blog.

* * *

#### Next day major edit

I generally tend to continually improve my blog posts, even after publishing, and tend not to make a note of the changes as they're usually minor. However, this one isn't: I realized I used the terms "character", "char", and "codepoint", as I am a Java developer through and through and these things have defined meanings to me.

However, outside that context, especially in the context of formal Unicode, the words are ambiguous or even meaningless. I've amended the post to use the proper terms "code unit" and "codepoint". This post deals a level lower than font rendering and never describes "glyphs" or "extended grapheme clusters" — those're for another day. Remaining usages of "character" are in reference to legacy codepages where this term is unambiguous, or for actual Unicode terms with similarly well-defined meanings.

If you are unaware of the proper terminology, which, considering you're reading a post about Unicode history, is likely: A "code unit" is one, well, unit, in an encoding scheme. In UTF-8, a code unit is 8 bits. In UTF-16, it's 16 bits. A "codepoint" is the index of a particular abstract character within Unicode, without regard to how it's encoded.

Anyway. Back to your regularly scheduled post...

* * *

A long time ago, at least in computer time, in the far-flung era of 1989, the Unicode working group was really starting to get going. They were hawking their brand new universal character set, one that would end the code page mess once and for all, making characters show up as the same on every computer, regardless of its language or operating system.

This time is important because this is when Sun Microsystems, Microsoft, and NeXT (whose NeXTSTEP was later used as the basis for Mac OS X) got on the Unicode bandwagon.

Unicode was a wonderful vision of the future where every computer works great together. They wrote on holy parchment of a character set, encoded in 16 bits, that would be plenty of room to encode every script in modern use, and then some.

And so, Sun, Microsoft, and NeXT built this new universal character set into their then up-and-coming software APIs. Sun with Java, Microsoft with Win32, and NeXT, with, well, NeXTSTEP. Strings were no longer collections of 8-bit, or heaven forbid, 7-bit code units. No, they were now 16-bit, so they could encode*every script* and bring this vision of the future to fruition.

You see, this future vision was so great because 16 bits is only double the size of 8 bits, so it was an easy sell to become compatible with *every language in the world* by simply doubling your code unit size. It's not that much of a loss of space; it's worth it!

## It was not meant to be

If you're reading this in modern times, it's likely you know this is not what happened.

Around 1996, the Unicode consortium decided that no, 16 bits was not enough. They had decided that Unicode should not encode all modern scripts in use today, but instead *every script to have ever been created by humans*. (The reason for this decision is interesting and complex enough for an entire separate post, so I will gloss over it for now.) However, all these products had already codified 16-bit code units. They couldn't simply *unship* their products and go back to 8-bit code units and use Plan9's UTF-8.

So... they made a compromise. That compromise is UTF-16.

You see, these programs were made with the expectation 16 bits could cover every codepoint in Unicode, 1:1, without translation. 65536 codepoints, after all, is a ton! This "encoding", or lack thereof, is called UCS-2. The **U**niversal**C**haracter **S**et, represented using **2** bytes, without transformation.

UTF-8, and UTF-16, are **U**nicode **T**ransformation **F**ormats, in **8** and**16** bits, respectively. They represent a way of *transforming* the UCS to fit in various code unit sizes.

UCS-2 can only represent the first 65536 codepoints of Unicode, also known as the *Basic Multilingual Plane*.

### A tangent: Planes and blocks

Unicode is split up into *planes*, and those planes are further split up into*blocks*.

A block is 256 codepoints. A plane is 256 blocks. Therefore, a plane is 65536 codepoints.

Planes further than the Basic Multilingual Plane, or BMP, are referred to as*supplementary planes*. The first of which is, fittingly, called the*Supplementary Multilingual Plane*.

Supplementary planes, especially those containing high-codepoint Private Use Area codepoints or emojis, are sometimes referred to as *Astral planes* to jokingly represent their sometimes poor support in programs. Programs, almost invariably, originally designed to use UCS-2.

## Right then. Back to what we were talking about

So, these software developers were in a pickle. UCS-2 wasn't enough for all of Unicode anymore, but they can't just stop using it after all these third-party developers started using their APIs.

As said, the compromise solution here was UTF-16. UTF-8, as you may know, encodes arbitrary Unicode codepoints with 1 to 4 bytes, by using specially assigned values to represent *pieces* of larger values. These pieces are put together by a *decoder* to create a Unicode (or UCS) codepoint.

To put this plan into action, a large portion of the BMP was dedicated to so called *surrogate pairs* - fake, non-characters that represent *half* of a supplementary plane Unicode codepoint. Two UTF-16 code units, a "surrogate pair", consisting of two "surrogates" of opposite halves, in the correct order, represent a codepoint in a supplementary plane, all the way up to U+10FFFF.

The reason they encoded these non-characters into Unicode instead of making them a quirk of the transformation format, like UTF-8, is that these programs were built for UCS-2; they expected each code unit to be *one codepoint*. So, by assigning codepoints to these surrogates, this wasn't *wrong*, and programs could continue to assume UCS-2 without breaking *too* spectacularly.

However, this ruined the point of UCS-2. We were back where we started; one code unit is no longer one codepoint, as UCS-2 promised. So we're stuck with double the code unit size, and we *still* need to carefully manipulate our strings and decode/encode them.

This is the worst of both worlds.

## What about the dream of a fixed size encoding?

Fixed size encoding lives on in the usually-hilariously-impractical UCS-4. (I've used it a few times when I'm too lazy to fumble with UTF-16 or UTF-8.)

It wastes *immense* amounts of memory, weighing in at, you guessed it, 4 bytes per code unit. However, it can represent every single Unicode codepoint, from U+000000 to U+10FFFF. (You may notice that's only 21 bits; the remaining 11 bits in UCS-4 are always zero, but few machines have a 24-bit integer type, so that precludes a UCS-3 from existing.)

## The aftermath

### Win32

Windows, being such a popular platform, and therefore having a lot of... not very good developers, making software for it, has become somewhat well-known for having filenames and other such things with malformed UTF-16, such as a surrogate pair in the wrong order, or only one half of a surrogate pair, due to naive string manipulation code that expects UCS-2, not UTF-16. This has resulted in the creation of [WTF-8](https://simonsapin.github.io/wtf-8/), which stands for Wobbly Transformation Format, not what *you* thought it stood for. Sheesh.

WTF-8 is UTF-8, but capable of encoding malformed UTF-16 surrogates, to faithfully reproduce these broken strings on systems that use UTF-8.

### Java

Java uses lots of strings. I mean, what doesn't use lots of strings? They're pretty essential.

UTF-16's space wasting has become such a problem that the JVM (is gaining the ability to)  *gained the ability to, in JDK 9,* transparently represent strings in memory as *Latin-1*, a legacy codepage, if possible.

JavaScript inherits Java's UTF-16 conundrum since it faithfully steal- er,*borrows*, many things from Java.

## Wait, what about Unix/Linux?

Unix and Linux conveniently sidestepped this whole issue by just shrugging their shoulders and going "eh, a `char` has no defined encoding, it's just a number.".

Everyone just kinda went with it and UTF-8 was slowly adopted. However, this means a program may emit [mojibake](https://en.wikipedia.org/wiki/Mojibake) if fed a legacy codepage and it doesn't check an `LC_*` environment variable to be sure of the encoding in use.

## And so...

That's a somewhat dramatic and fact-checked retelling of what I've apparently decided to call *The Tragedy of UCS-2*. I hope it was... interesting?

* * *

Support me

*Please consider donating to support my ventures, including these blog posts. This site is and will forever be ad-free.*

- ![](../_resources/bf611f0fa5391afe70d1ce1bfca4ed54.png)[PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=96VY9R4Q5EGLQ&source=url) (one-time or recurring)
- ![](../_resources/1328aac4f73335c345cbe5054e861364.png)[Square Cash](https://cash.app/$unascribed) (one-time, needs account)
- ![](../_resources/4f7265169bc445a70434d5c538e5bc1f.png)[Liberapay](https://liberapay.com/unascribed) (recurring, needs account, anonymous)
- ![](../_resources/5d1e82c82e66f5205741120329c4097e.png)[Patreon](https://patreon.com/unascribed) (recurring, needs account, rewards)