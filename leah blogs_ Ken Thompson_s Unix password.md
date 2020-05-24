leah blogs: Ken Thompson's Unix password

##    09oct2019 ·   [Ken Thompson's Unix password](https://leahneukirchen.org/blog/archive/2019/10/ken-thompson-s-unix-password.html)

Somewhere around 2014 I found an [/etc/passwd](https://github.com/dspinellis/unix-history-repo/blob/BSD-3-Snapshot-Development/etc/passwd) file in some dumps of the BSD 3 source tree, containing passwords of all the old timers such as Dennis Ritchie, Ken Thompson, Brian W. Kernighan, Steve Bourne and Bill Joy.

Since the DES-based[crypt(3)](https://minnie.tuhs.org/cgi-bin/utree.pl?file=V7/usr/man/man3/crypt.3)algorithm used for these hashes is well known to be weak (and limited to at most 8 characters), I thought it would be an easy target to just crack these passwords for fun.

Well known tools for this are [john](https://www.openwall.com/john/)and [hashcat](https://hashcat.net/wiki/).

Quickly, I had cracked a fair deal of these passwords, many of which were very weak. (Curiously, `bwk` used `/.,/.,`, which is easy to type on a QWERTY keyboard.)

However, `ken`s password eluded my cracking endeavor. Even an exhaustive search over all lower-case letters and digits took several days (back in 2014) and yielded no result. Since the algorithm was developed by Ken Thompson and Robert Morris, I wondered what’s up there. I also realized, that, compared to other password hashing schemes (such as NTLM), crypt(3) turns out to be quite a bit slower to crack (and perhaps was also less optimized).

Did he really use uppercase letters or even special chars? (A 7-bit exhaustive search would still take over 2 years on a modern GPU.)

The topic [came up again](https://inbox.vuxu.org/tuhs/tqkjt9nn7p9zgkk9cm9d@localhost/T/#m160f0016894ea471ae02ee9de9a872f2c5f8ee93)earlier this month on [The Unix Heritage Society](https://www.tuhs.org/)mailing list, and I [shared my results](https://inbox.vuxu.org/tuhs/87bluxpqy0.fsf@vuxu.org/) and frustration of not being able to break `ken`s password.

Finally, today this secret [was resolved](https://inbox.vuxu.org/tuhs/CACCFpdx_6oeyNkgH_5jgfxbxWbZ6VtOXQNKOsonHPF2=747ZOw@mail.gmail.com/) by Nigel Williams:

	From: Nigel Williams <nw@retrocomputingtasmania.com>
	Subject: Re: [TUHS] Recovered /etc/passwd files

	ken is done:

	ZghOT0eRm4U9s:p/q2-q4!

	took 4+ days on an AMD Radeon Vega64 running hashcat at about 930MH/s
	during that time (those familiar know the hash-rate fluctuates and
	slows down towards the end).

This is a chess move in [descriptive notation](https://en.wikipedia.org/wiki/Descriptive_notation), and the beginning of [many common openings](https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._d4). It fits very well to Ken Thompson’s [background in computer chess](https://www.chessprogramming.org/index.php?title=Ken_Thompson).

I’m very happy that this mystery has been solved now and I’m pleased of the answer.

**[Update 16:29: fix comment on chess.]**
NP: Mel Stone—By Now