Floating Point Visually Explained

[**FABIEN SANGLARD'S WEBSITE**](http://fabiensanglard.net/)
* * *

[ABOUT](http://fabiensanglard.net/about)  [EMAIL](http://fabiensanglard.net/contact/index.html)  [RSS](http://fabiensanglard.net/rss.xml)  [DONATE](https://paypal.me/fabiensanglard)

August 29, 2017

**Floating Point Visually Explained**

* * *

 [fp.webp](../_resources/bc6df6390ef4c959c4a85f6453e1f89b.webp)

While I was writing a book about Wolfenstein 3D[[1]](http://fabiensanglard.net/floating_point_visually_explained/index.html#footnote_1), I wanted to vividly demonstrate how much of a handicap it was to work without floating points. My personal attempts at understanding floating points using canonical[[2]](http://fabiensanglard.net/floating_point_visually_explained/index.html#footnote_2) articles[[3]](http://fabiensanglard.net/floating_point_visually_explained/index.html#footnote_3) were met with significant resistance from my brain.

I tried to find a different way. Something far from (−1)S∗1.M∗2(E−127)(−1)S∗1.M∗2(E−127) and its mysterious exponent/mantissa. Possibly a drawing since they seem to flow through my brain effortlessly.

I ended up with what follows and I decided to include it in the book. I am not claiming this is my invention but I have never seen floating points explained this way so far. I hope it will helps a few people like me who are a bit allergic to mathematic notations.

**How Floating Point are usually explained**

* * *

In the C language, floats are 32-bit container following the IEEE 754 standard. Their purpose is to store and allow operations on approximation of real numbers. The way I have seen them explained so far is as follow. The 32 bits are divided in three sections:

- 1 bit S for the sign
- 8 bits E for the exponent
- 23 bits for the mantissa

![](../_resources/851267793dcd01e4bb7c7c0e5db8f933.png)
*Floating Point internals.*![](../_resources/2de5eaba2c8ca09832c0cf05543210da.png)

*The three sections of a floating Point number.*So far, so good. Now, how numbers are interpreted is usually explained with the formula:

(−1)S∗1.M∗2(E−127)(−1)S∗1.M∗2(E−127)
*How everybody hates floating point to be explained to them.*

This is usually where I flip the table. Maybe I am allergic to mathematic notation but something just doesn't click in my brain when I read this. It feels like learning to [draw a owl](http://fabiensanglard.net/floating_point_visually_explained/01.jpg).

>  Floating-point arithmetic is considered an esoteric subject by many people.

>
> - David Goldberg

**A different way to explain...**

* * *

Although correct, this way of explaining floating point usually leaves some of us completely clueless. I blame this dreadful notation for discouraging legions of programmers, scaring them to the point where they never looked back to understand how floating point actually works.

Fortunately, there is a different way to explain it. Instead of Exponent, think of a Window between two consecutive power of two integers. Instead of a Mantissa, think of an Offset within that window.

![](../_resources/4ee433de84cdbc3ed545c78f87894df8.png)

*The three sections of a floating Point number.*The window tells within which two consecutive power-of-two the number will be: [0.5,1], [1,2], [2,4], [4,8] and so on (up to [21272127,21282128]). The offset divides the window in 223=8388608223=8388608 buckets. With the window and the offset you can approximate a number. The window is an excellent mechanism to protect from overflowing. Once you have reached the maximum in a window (e.g [2,4]), you can "float" it right and represent the number within the next window (e.g [4,8]). It only costs a little bit of precision since the window becomes twice as large.

The next figure illustrates how the number 6.1 would be encoded. The window must start at 4 and span to next power of two, 8. The offset is about half way down the window.

![](../_resources/475ec87ff44f0ef7a73ab5b637d38277.png)

*Value 6.1 approximated with floating point.*
**Precision**

* * *

How much precision is lost when the window covers a wider range? Let's take an example with window [1,2] where the 8388608 offsets cover a range of 1 which gives a precision of (2−1)8388608=0.00000011920929(2−1)8388608=0.00000011920929. In the window [2048,4096] the 8388608 offsets cover a range of (4096−2048)=2048(4096−2048)=2048 which gives a precision (4096−2048)8388608=0.0002(4096−2048)8388608=0.0002.

**An other example**

* * *

Let's take an other example with the detailed calculations of the floating point representation of a number we all know well: 3.14.

- The number 3.14 is positive →S=0→S=0.
- The number 3.14 is between the power of two 2 and 4 so the floating window must start at 2121  →E=128→E=128 (see formula where window is 2(E−127)2(E−127)).
- Finally there are 223223 offsets available to express where 3.14 falls within the interval [2-4]. It is at 3.14−24−2=0.573.14−24−2=0.57 within the interval which makes the offset M=223∗0.57=4781507M=223∗0.57=4781507

Which in binary translates to:

- S = 0 = 0b
- E = 128 = 10000000b
- M = 4781507 = 10010001111010111000011b

![](../_resources/954d2506a37ac3ffeb980790fb549f5c.png)

*3.14 floating point binary representation.*The value 3.14 is therefore approximated to 3.1400001049041748046875. The corresponding value with the ugly formula:

3.14=(−1)0∗1.57∗2(128−127)3.14=(−1)0∗1.57∗2(128−127)

And finally the graphic representation with window and offset:

![](../_resources/e1638dfdf76f4d8ad36f2e3c96548ec0.png)
 *3.14 window and offset.*

I hope that helped :) !
**Blast from the past**

* * *

[BOX_IntelBOX387SX20.webp](../_resources/23287da5d039d30551aa95f78f47ba1c.webp)

Since floating point units were so slow, why did the C language end up with float and double types ? After all, the machine used to invent the language (PDP-11) did not have a floating point unit! The manufacturer (DEC) had promised to Dennis Ritchie and Ken Thompson the next model would have one. Being astronomy enthusiasts they decided to add those two types to their language.

***Trivia:*** People who really wanted a hardware floating point unit in 1991 could buy one. The only people who could possibly want one back then would have been scientists (as per Intel understanding of the market). They were marketed as "Math CoProcessor". Performance were average and price was outrageous (200 USD in 1993 equivalent to 350 USD in 2016.). As a result, sales were mediocre.

**References**

* * *

|     |     |     |     |
| --- | --- | --- | --- |
| [^](http://fabiensanglard.net/floating_point_visually_explained/index.html#back_1) | [1] | Source : | [Game Engine Black Book: Wolfenstein 3D](http://fabiensanglard.net/gebb/index.html) |
| [^](http://fabiensanglard.net/floating_point_visually_explained/index.html#back_2) | [2] | Source : | [Wikipedia, Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| [^](http://fabiensanglard.net/floating_point_visually_explained/index.html#back_3) | [3] | Source : | [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) |

* * *

*