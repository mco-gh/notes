Compression Decompressed | The website of Jack Preston, Computerer

# Compression Decompressedor, Making Things Smaller: A Visual Introduction

Compression is everywhere. It's used to more efficiently store data on hard drives, send TV signals, transmit web pages like this one, stream Netflix videos, package up video games for distribution, the list is endless. Almost no significant area of modern computing exists that doesn't make use of compression technologies.

So what is it?

Whether you've been using desktop compression software for years, or never thought about it at all, this article will try to explain a little of what goes on under the hood when you squash a file or stream a video. We'll look into the answers to the big questions, and probably raise more new ones along the way.

What does it mean to compress something?
How can you make something smaller than it already is?
How do you practically go about doing that?
Let's get to work!
Toggle pointless gifs (yay!)

## The basics

Before we even go anywhere near computing and digital information, we can find a useful introduction to compression. Take the following word in English:

T1
r2
e3
e4

Counting up all the symbols we had to use to express that, we see that we used four:

T1
r2
e3
e4
4 characters
Fine, not bad. But what does it look like written in, say, Japanese?
木1
1 characters

Oho! Only one symbol! Have we expressed a different idea? A different piece of information? No. But we have managed to reduce the page-space required to write down the idea of a tree by 75%. So what have we done?

Nothing magical - we've just decided to express the idea in a different way. We've chosen a different, more efficient representation of the information. Spoiler: that'll turn out to be the most important concept of this piece, so pay attention.

## Yeah, OK, but what about pixel art?

I hear you cry! How does our example from written language above translate into the world of strictly-defined digital data? Let's think about a class of data that I hear is pretty popular these days - images. To keep things simple for now we're not going to try to compress a high resolution Instagram photo or anything. Instead, let's go for pixel art.

Pretty, no? I made it myself. That's a ten-by-ten grid of pixels, each with a colour we can represent by one character - 'B', 'Y' or 'G'.

How can we represent this digitally? A file storing this image in a pretty much raw form might have the following contents:

B1
B2
B3
B4
B5
B6
B7
B8
B9
B10
B11
B12
B13
B14
B15
B16
B17
Y18
B19
B20
B21
B22
B23
B24
B25
B26
Y27
Y28
Y29
B30
B31
B32
G33
G34
G35
B36
B37
Y38
B39
B40
B41
B42
G43
G44
G45
B46
B47
B48
B49
B50
G51
G52
G53
G54
G55
G56
B57
B58
B59
B60
G61
G62
G63
G64
G65
G66
B67
B68
B69
B70
G71
G72
G73
G74
G75
G76
G77
B78
B79
B80
G81
G82
G83
G84
G85
G86
G87
B88
B89
B90
G91
G92
G93
G94
G95
G96
G97
G98
G99
G100
100 characters

All we've done is write the corresponding colour character for each pixel, left to right, top to bottom. As you'd expect, this comes to 100 characters. Let's assume that means 100 bytes taken up on disk. Hopefully you agree this gives a pretty good upper bound on sensible size for a file representing this image - anything bigger would either be kind of pointless, or attempting to pack more information than just the image itself in (metadata or something).

Now, try a little thought experiment before you go any further. If I asked you to write, on paper, a representation of this image in less than 100 characters, how might you do it? Go ahead, mull it over with a cup of tea. I'll wait.

Toggle pointless gifs (yay!)
Got something? Good, me too.

I'm going to call my method run-length encoding, or RLE. Jks, I didn't come up with it and I don't get to name it. It's been around since at least the sixties as a basic compression technique. I'm willing to bet at least some of you literally came up with it just now.

Run-length encoding works by noticing something about the image file above. There are great big long stretches where we just write the same colour over and over again. Look at all those 'B's to kick it off! Surely this repetition is something we can squash down?

Of course we can! What if, instead of:
B1
B2
B3
B4
B5
B6
B7
B8
B9
B10
B11
B12
B13
B14
B15
B16
B17
17 characters
We wrote:
11
72
B3
3 characters

This seems promising. We've turned 17 characters into 3, just by abbreviating long repeated strings of the same character. These repetitive strings are called runs, by the way. Hence run-length encoding: we've encoded the data by writing down the length of its runs, instead of every element in them. No information has been lost in doing this. A very simple program that was able to render the previous file format should be easily modifiable to read our new format, and the image would look identical.

The live demo below displays the original image along with its long representation and its run-length encoded one.

Tap or click on any pixel to change its colour and observe the changes.

11
02
03
B4
4 characters
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
100 characters

[Neat! I'd better show my friends](https://twitter.com/intent/tweet?text=Explore%20data%20compression%20with%20live%2C%20interactive%20demos&url=https%3A%2F%2Funwttng.com%2Fcompression-decompressed&hashtags=&via=unwttng&related=unwttng)

You'll notice something if you play with it for a while: the amount we're able to compress the long form by is dependent on the image itself. If the whole thing's one solid block of one colour, or a few very long runs, we can get very small outputs. The smallest we can get this file using our version of run-length encoding is 4 bytes:

11
02
03
G4
4 characters

Another thing? This algorithm can go really really wrong. It can, in fact, make the file bigger than the raw pixel-by-pixel representation. Notice that it takes two characters to write '1B', or '1G'. What if your pixel art is just a mess of runs of length 1?

1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
B
1
G
1
Y
1
0
B
183 characters
Amazing.
Time to learn you some terminology.
Toggle pointless gifs (yay!)

## Compression ratio

How do we measure how well our compression algorithm is actually doing at making our data smaller? Well, it's pretty much how you might guess - we calculate the ratio of the data's uncompressed size to its compressed size.

If we take our 100 byte pixel art image and our algorithm compresses it down to 42 bytes, then we've managed a compression ratio of (100 / 42) ≈ 2.38. At its best, with the solid colour image, the algorithm managed a whopping compression ratio of (100 / 4) = 25! And with the single-pixel-per-run image designed to mess with the algorithm, it only managed (100 / 200) = 0.5. Protip: compression ratios less than 1 are frowned upon.

We can see that the compression ratio achieved by our basic RLE algorithm is incredibly sensitive to the structure of the input data. This is pretty common for such naive approaches. The algorithm makes a lot of assumptions about the shape of data it expects to find if it's to do a reasonable job - repeated, adjacent runs of the exact same byte must be present. A cleverer RLE implementation might attempt to run-length encode the data using repeated substrings.

T1
h2
i3
r4
t5
y6
-7
t8
h9
r10
e11
e12
 13
c14
o15
p16
i17
e18
s19
 20
o21
f22
 23
'24
B25
G26
Y27
'28
 29
f30
o31
l32
l33
o34
w35
e36
d37
 38
b39
y40
 41
o42
n43
e44
 45
m46
o47
r48
e49
 50
'51
B52
'53
53 characters

Hell, even writing it in English I managed a better ratio than 2! Couple this approach with a nice, concise file format and we're onto a bit of a winner compared to our first try.

## How small can you go?

This is a natural and very very very big question. After all, it seems only correct that a reasonably well-designed compression algorithm should be able to reduce any input by at least a bit (both the colloquial and technical meaning of a bit work just as well here).

Unfortunately, it's not that simple. Say we had an algorithm (let's call it A) that, given any input whatsoever, was capable of achieving a compression ratio of strictly greater than 1. It could be 2.5 for some inputs, it could be 1.000000002 for others.

If such an algorithm existed, we would be able to simply apply it, again and again, to an input - just run A(A(A(data))), and so on. Every time we applied it, the size of our data would decrease by at least one bit. It doesn't take a big leap to see that this would eventually take us down to a single bit, and even... zero bits?

Toggle pointless gifs (yay!)

That doesn't seem possible. And it isn't. Even without that recursive "proof" of the impossibility of such an algorithm, just think: with as few as nine different files, there's no possible way to compress them all (without throwing away information) down to, let's say, three bits each.

Three bits only gives us eight unique representations: 000, 001, 010, 100, 011, 101, 110, 111. Even if we had some super-powerful compression algorithm capable of taking the first eight of our files down to these unique representations, the compressed form of our ninth file would have to be one of them too! There aren't enough unique 3-bit representations to cover more than eight uncompressed pieces of data for a given algorithm.

Here's an important take-away: there is a hard limit to the compression ratio that any given algorithm can achieve on generic data. And you can't get round it by applying one algorithm until it stops being useful and then trying another one. This might eek out a little more compression (in fact, many established compression softwares do exactly this), but eventually you'll hit something you can't compress further. And, really, your repeated applications of different algorithms are just another compression algorithm. The rule still applies.

## Kolmogorov complexity

The disappointment doesn't stop there, either. It's not just the algorithms that have a theoretical limit on compression - the data itself has an inherent complexity.

Look at the following two strings:
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
24 characters
and:
m
a
r
w
n
c
t
c
m
w
n
o
q
n
i
f
n
l
f
z
n
a
l
k
24 characters

Exactly the same length, but one is just clearly more complex. You can see it easily, using your human brain. More concretely, we know for a fact we can apply basic RLE to the first one and take it down to at most three characters ("24a").

[Kolmogorov complexity](https://wikipedia.org/wiki/Kolmogorov_complexity) (the brain child of [Andrey Nikolaevich Kolmogorov](https://wikipedia.org/wiki/Andrey_Kolmogorov), a Soviet mathematician) captures this concept pretty well. It's far from the only measure of such things, but it serves well. The Kolmogorov complexity of a piece of data can be defined as the length of the shortest possible computer program capable of generating the data as output.

Obviously there's a good upper bound on the Kolmogorov complexity of any string 'S' - just write the program "return S". I'm being a bit reductive since the measure should include the length of the entire program - interpreter or compiled code included. But for the purposes of this discussion it'll do fine. Just think of it as the length of the shortest piece of code you could write to generate the data.

Kolmogorov complexity isn't particularly sensitive to your choice of programming language. It can be shown that choice of language for your program only impacts complexity by a constant factor. This is quite key: it tells us that no matter how you choose to express the data, there's a limit to how succinctly you can do it. Some data just needs more space to represent than a million green pixels, and always will.

## On loss

Don't give up hope, though. Everything we've covered so far has been what's referred to as lossless compression. Lossless compression is defined as any compression which allows the original data to be reconstructed perfectly from the compressed form. That is, if C is our compression algorithm, and D the corresponding decompression algorithm, we should expect D(C(x)) = x for any data x.

This is useful - when compressing written text such like literature or blog articles, tax archives, low-resolution pixel data, you almost certainly want to do it losslessly. In these applications, the exact content and ordering of every character is likely to be important.

But Other Options Are Available. Compression which makes no guarantee of perfectly reproduced data is known as lossy compression. And it is *everywhere*.

The use-cases for lossy compression are many. Human senses are very forgiving to error / patchy information. Any data which represents visuals or audio (or both) is a prime candidate for lossiness.

Need an example? Look at these two images of Barack Obama.
![](../_resources/fea77d5a0e1ec0dc6fbbdba22cd268dc.png)
![](../_resources/ec1dfeabd8077205723db57b5bf0dfc0.png)

The first of these is a roughly 335 kilobyte [PNG](https://wikipedia.org/wiki/Portable_Network_Graphics) file (PNG is a lossless image compression format). We'll treat it as our reference point. The second is the result of saving that PNG as a [JPEG](https://wikipedia.org/wiki/JPEG), very much a lossy format. It comes to around 22 kilobytes, meaning we've compressed the original image by a ratio of around 15, which is not at all bad.

Can you see the difference? Probably, just about. If you get all close to your screen and squint and turn your head a bit. If you look at the detail of his hairs, if you *literally pick hairs*, you can see some fuzziness where there was none. The point isn't that it's a perfect reproduction - the point is that it's good enough. When you're sending data over the internet, a fifteen times compression ratio is much more valuable than pixel-perfect imagery.

That's not to say it can't go wrong, though. JPEG has to throw out a lot of information to achieve that kind of compression, and whilst it attempts to do so pretty intelligently, you can push it too far. Play with the live demo below to see how quality can *really* drop off if you ask too much of JPEG, but also notice how much you can get away with before the image starts to look bad. As I said, your eyes are very forgiving.

![](../_resources/a04af5cc104f068b0995117694569d79.png)![](../_resources/609dbd2dc72a3d978768ccfaeb9450de.jpg)

Quality: 0

Video streaming services like Netflix or YouTube, audio streaming like Spotify and Soundcloud, all use lossy compression. Buffering or stalling content is an engagement killer, so these services go to any lengths possible to get some useful video or music over the network. You'll often see dynamically-compressed data coming to you - videos will begin heavily pixellated and will rapidly increase in quality as the site or app detects that your network can handle less lossily compressed data.

See all those Giphy gifs I've been using throughout this piece? Same thing happening there. Check out how they load on a slow connection (yes I took a gif of this loading process and embedded it using Giphy, problems?):

 [  [200w.webp](../_resources/c88baf02acef9d9368018ef2784bdcd0.webp) ''](https://giphy.com/gifs/l1J3QaZoHeNZ9JFU4)  [(L)](https://giphy.com/)


Share
 

Weird, right? First they load a low-quality still of the first frame of the gif. Then, once some bigger data is available, you start to get the gif. But you only get a few frames. Then you get more and more frames until you eventually have the entire gif rendering.

This is what modern, streaming media compression looks like: hybrid strategies designed almost exclusively to make sure you get fluid content in front of users in as few bytes (and therefore as little time) as possible. Lossless compression like our RLE on files above has its place, and is still at the core of many of the best desktop file archiving tools, but lossy compression is what gets Game of Thrones onto your telly box as smoothly and quickly as is feasible.

## Representation is everything

I think we need to call it day for now, but there's *a lot* more to be said about compression.

We've had a look at the basic ideas, and found an important philosophical nugget hidden amongst technicalities:

Images, text, video, music - no information has a single "true" or "raw" form. There are only more or less efficient ways of representing it.

Compression is about finding the more efficient ways to write down your data, and the most impressive compression is about finding a way to do that *no matter what the data is*.

Thanks for reading, and if you appreciate the effort that's gone into some of the live demos above, please feel free to share this with your friends.

[OMG this article I can't even](https://twitter.com/intent/tweet?text=If%20you%27ve%20ever%20wondered%20how%20compression%20works%2C%20this%20is%20your%20time&url=https%3A%2F%2Funwttng.com%2Fcompression-decompressed&hashtags=&via=unwttng&related=unwttng)

Hope you learned something!

[## Go home  What else is going on?](https://unwttng.com/home)[## Follow Jack  A god damn thrill ride or your money back](https://twitter.com/unwttng)