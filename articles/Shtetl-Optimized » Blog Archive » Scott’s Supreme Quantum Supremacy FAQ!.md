Shtetl-Optimized » Blog Archive » Scott’s Supreme Quantum Supremacy FAQ!

## [Scott’s Supreme Quantum Supremacy FAQ!](https://www.scottaaronson.com/blog/?p=4317)

You’ve seen the stories—in the *Financial Times*, *Technology Review*, *CNET*, Facebook, Reddit, Twitter, or elsewhere—saying that a group at Google has now achieved quantum computational supremacy with a 53-qubit superconducting device. While these stories are easy to find, I’m not going to link to them here, for the simple reason that *none of them were supposed to exist yet*.

As the world now knows, Google is indeed preparing a big announcement about quantum supremacy, to coincide with the publication of its research paper in a high-profile journal (which journal? you can probably narrow it down to two). This will hopefully happen within a month.

Meanwhile, though, NASA, which has some contributors to the work, inadvertently posted an outdated version of the Google paper on a public website. It was there only briefly, but long enough to make it to the *Financial Times*, my inbox, and millions of other places. Fact-free pontificating about what it means has predictably proliferated.

The world, it seems, is going to be denied its clean “moon landing” moment, wherein the Extended Church-Turing Thesis gets experimentally obliterated within the space of a press conference. This is going to be more like the Wright Brothers’ flight—about which rumors and half-truths leaked out in dribs and drabs between 1903 and 1908, the year Will and Orville finally agreed to do public demonstration flights. (This time around, though, it thankfully won’t take *that* long to clear everything up!)

I’ve known about what was in the works for a couple months now; it was excruciating not being able to blog about it. Though sworn to secrecy, I couldn’t resist dropping some hints here and there (did you catch any?)—for example, in my recent [Bernays Lectures](https://www.scottaaronson.com/blog/?p=4301) in Zürich, a lecture series whose entire structure built up to the brink of this moment.

This post is not an official announcement or confirmation of anything. Though the lightning may already be visible, the thunder belongs to the group at Google, at a time and place of its choosing.

Rather, because so much misinformation is swirling around, what I thought I’d do here, in my role as blogger and “public intellectual,” is offer **Scott’s Supreme Quantum Supremacy FAQ**. You know, just in case you were randomly curious about the topic of quantum supremacy, or wanted to know what the implications would be if some search engine company based in Mountain View or wherever were *hypothetically* to claim to have achieved quantum supremacy.

Without further ado, then:
**Q1. What is quantum computational supremacy?**

Often abbreviated to just “quantum supremacy,” the term refers to the use of a quantum computer to solve *some* well-defined set of problems that would take orders of magnitude longer to solve with any currently known algorithms running on existing classical computers—and not for incidental reasons, but for reasons of asymptotic quantum complexity. The emphasis here is on being as sure as possible that the problem *really was* solved quantumly and *really is* classically intractable, and ideally achieving the speedup *soon* (with the noisy, non-universal QCs of the present or very near future). If the problem is also *useful* for something, then so much the better, but that’s not at all necessary. The Wright Flyer and the Fermi pile weren’t useful in themselves.

**Q2. If Google has indeed achieved quantum supremacy, does that mean that now [“no code is uncrackable”](https://mobile.twitter.com/AndrewYang/status/1175200727385464832), as Democratic presidential candidate Andrew Yang recently tweeted?**

No, it doesn’t. (But I still like Yang’s candidacy.)

There are two issues here. First, the devices currently being built by Google, IBM, and others have 50-100 qubits and no error-correction. Running Shor’s algorithm to break the RSA cryptosystem would require several thousand logical qubits. With known error-correction methods, that could easily translate into *millions* of physical qubits, and those probably of a higher quality than any that exist today. I don’t think anyone is close to that, and we have no idea how long it will take.

But the second issue is that, even in a hypothetical future with scalable, error-corrected QCs, on our current understanding they’ll only be able to crack *some* codes, not all of them. By an unfortunate coincidence, the public-key codes that they can crack include *most* of what we currently use to secure the Internet: RSA, Diffie-Hellman, elliptic curve crypto, etc. But symmetric-key crypto should only be minimally affected. And there are even candidates for public-key cryptosystems (for example, based on lattices) that no one knows how to break quantumly after 20+ years of trying, and some efforts underway now to start migrating to those systems. For more, see for example my [letter to Rebecca Goldstein](https://www.scottaaronson.com/blog/?p=3848).

**Q3. What calculation is Google planning to do, or has it already done, that’s believed to be classically hard?**

So, I can tell you, but I’ll feel slightly sheepish doing so. The calculation is: a “challenger” generates a random quantum circuit C (i.e., a random sequence of 1-qubit and nearest-neighbor 2-qubit gates, of depth perhaps 20, acting on a 2D grid of n = 50 to 60 qubits). The challenger then sends C to the quantum computer, and asks it apply C to the all-0 initial state, measure the result in the {0,1} basis, send back whatever n-bit string was observed, and repeat some thousands or millions of times. Finally, using its knowledge of C, the classical challenger applies a statistical test to check whether the outputs are consistent with the QC having done this.

So, this is not a problem like factoring with a single right answer. The circuit C gives rise to some probability distribution, call it DC, over n-bit strings, and the problem is to output samples from that distribution. In fact, there will typically be 2n strings in the support of DC—so many that, if the QC is working as expected, the same output will never be observed twice. A crucial point, though, is that the distribution DC is *not* uniform. Some strings enjoy constructive interference of amplitudes and therefore have larger probabilities, while others suffer destructive interference and have smaller probabilities. And even though we’ll only see a number of samples that’s tiny compared to 2n, we can *check* whether the samples preferentially cluster among the strings that are predicted to be likelier, and thereby build up our confidence that something classically intractable is being done.

So, tl;dr, the quantum computer is simply asked to apply a random (but known) sequence of quantum operations—not because we intrinsically care about the result, but because we’re trying to prove that it can beat a classical computer at *some* well-defined task.

**Q4. But if the quantum computer is just executing some random garbage circuit, whose only purpose is to be hard to simulate classically, then who cares? Isn’t this a big overhyped nothingburger?**

No. As I put it the other day, it’s not an everythingburger, but it’s certainly at least a somethingburger!

It’s like, have a little respect for the immensity of what we’re talking about here, and for the terrifying engineering that’s needed to make it reality. Before quantum supremacy, by definition, the QC skeptics can all laugh to each other that, for all the billions of dollars spent over 20+ years, *still* no quantum computer has even once been used to solve any problem faster than your laptop could solve it, or at least not in any way that depended on its being a quantum computer. In a post-quantum-supremacy world, that’s no longer the case. A superposition involving 250 or 260 complex numbers has been computationally harnessed, using time and space resources that are minuscule compared to 250 or 260.

I keep bringing up the Wright Flyer only because the chasm between what we’re talking about, and the dismissiveness I’m seeing in some corners of the Internet, is kind of breathtaking to me. It’s like, if you believed that useful air travel was fundamentally impossible, then seeing a dinky wooden propeller plane keep itself aloft wouldn’t refute your belief … *but it sure as hell shouldn’t reassure you either*.

Was I right to [worry](https://blogs.scientificamerican.com/cross-check/scott-aaronson-answers-every-ridiculously-big-question-i-throw-at-him/), years ago, that the constant drumbeat of hype about much less significant QC milestones would wear out people’s patience, so that they’d no longer care when something newsworthy finally did happen?

**Q5. Years ago, you scolded the masses for being super-excited about D-Wave, and its claims to get huge quantum speedups for optimization problems via quantum annealing. Today you scold the masses for *not* being super-excited about quantum supremacy. Why can’t you stay consistent?**

Because my goal is not to move the “excitement level” in some uniformly preferred direction, it’s to be right! With hindsight, would you say that I was mostly right about D-Wave, even when raining on that particular parade made me unpopular in some circles? Well, I’m trying to be right about quantum supremacy too.

**Q6. If quantum supremacy calculations just involve sampling from probability distributions, how do you check that they were done correctly?**

Glad you asked! This is the subject of a fair amount of theory that I and others developed over the last decade. I already gave you the short version in my answer to Q3: you check by doing statistics on the samples that the QC returned, to verify that they’re preferentially clustered in the “peaks” of the chaotic probability distribution DC. One convenient way of doing this, which Google calls the “linear cross-entropy test,” is simply to sum up Pr[C outputs si] over all the samples s1,…,sk that the QC returned, and then to declare the test a “success” if and only if the sum exceeds some threshold—say, bk/2n, for some constant b strictly between 1 and 2.

Admittedly, in order to apply this test, you need to *calculate* the probabilities Pr[C outputs si] on your classical computer—and the only known ways to calculate them require brute force and take ~2n time. Is that a showstopper? No, not if n is 50, and you’re Google and are able to handle numbers like 250 (although not 21000, which exceeds a [googol](https://en.wikipedia.org/wiki/Googol), har har). By running a huge cluster of classical cores for (say) a month, you can eventually verify the outputs that your QC produced in a few seconds—while also seeing that the QC was many orders of magnitude faster. However, this does mean that sampling-based quantum supremacy experiments are almost *specifically* designed for ~50-qubit devices like the ones being built right now. Even with 100 qubits, we wouldn’t know how to verify the results using all the classical computing power available on earth.

(Let me stress that this issue is specific to *sampling* experiments like the ones that are currently being done. If Shor’s algorithm factored a 2000-digit number, it would be easy to check the result by simply multiplying the claimed factors and running a primality test on them. Likewise, if a QC were used to simulate some complicated biomolecule, you could check its results by comparing them to experiment.)

**Q7. Wait. If classical computers can only check the results of a quantum supremacy experiment, in a regime where the classical computers can still simulate the experiment (albeit extremely slowly), then how do you get to claim “quantum supremacy”?**

Come on. With a 53-qubit chip, it’s perfectly feasible to see a speedup by a factor of many millions, in a regime where you can still directly verify the outputs, and also to see that the speedup is growing exponentially with the number of qubits, exactly as asymptotic analysis would predict. This isn’t marginal.

**Q8. Is there a mathematical proof that no fast classical algorithm could possibly spoof the results of a sampling-based quantum supremacy experiment?**

Not at present. But that’s not quantum supremacy researchers’ fault! As long as theoretical computer scientists can’t even prove basic conjectures like P≠NP or P≠PSPACE, there’s no hope of ruling out a fast classical simulation unconditionally. The best we can hope for are conditional hardness results. And we have indeed managed to prove some such results—see for example the [BosonSampling paper](https://arxiv.org/abs/1011.3245), or the [Bouland et al. paper](https://arxiv.org/abs/1803.04402) on average-case #P-hardness of calculating amplitudes in random circuits, or [my paper with Lijie Chen](https://arxiv.org/abs/1612.05903) (“Complexity-Theoretic Foundations of Quantum Supremacy Experiments”). The biggest theoretical open problem in this area, in my opinion, is to prove *better* conditional hardness results.

**Q9. Does sampling-based quantum supremacy have any applications in itself?**

When people were first thinking about this subject, it seemed pretty obvious that the answer was “no”! (I know because I was one of the people.) Recently, however, the situation has changed—for example, because of my [certified randomness protocol](https://www.scottaaronson.com/talks/certrand2.ppt), which shows how a sampling-based quantum supremacy experiment could almost immediately be repurposed to generate bits that can be *proven to be random* to a skeptical third party (under computational assumptions). This, in turn, has possible applications to proof-of-stake cryptocurrencies and other cryptographic protocols. I’m hopeful that more such applications will be discovered in the near future.

**Q10. If the quantum supremacy experiments are just generating random bits, isn’t that uninteresting? Isn’t it trivial to convert qubits into random bits, just by measuring them?**

The key is that a quantum supremacy experiment doesn’t generate *uniform* random bits. Instead, it samples from some complicated, correlated probability distribution over 50- or 60-bit strings. In my certified randomness protocol, the deviations from uniformity play a central role in how the QC convinces a classical skeptic that it really *was* sampling the bits randomly, rather than in some secretly deterministic way (e.g., using a pseudorandom generator).

**Q11. Haven’t decades of quantum-mechanical experiments–for example, the ones that violated the Bell inequality–already demonstrated quantum supremacy?**

This is purely a confusion over words. Those other experiments demonstrated other forms of “quantum supremacy”: for example, in the case of Bell inequality violations, what you could call “quantum correlational supremacy.” They did not demonstrate quantum *computational* supremacy, meaning doing something that’s infeasible to simulate using a classical computer (where the classical simulation has no restrictions of spatial locality or anything else of that kind). Today, when people use the phrase “quantum supremacy,” it’s generally short for quantum computational supremacy.

**Q12. Even so, there are countless examples of materials and chemical reactions that are hard to classically simulate, as well as special-purpose quantum simulators (like those of Lukin’s group at Harvard). Why don’t these already count as quantum computational supremacy?**

Under some people’s definitions of “quantum computational supremacy,” they do! The key difference with Google’s effort is that they have a *fully programmable *device—one that you can program with an arbitrary sequence of nearest-neighbor 2-qubit gates, just by sending the appropriate signals from your classical computer.

In other words, it’s no longer open to the QC skeptics to sneer that, sure, there are quantum systems that are hard to simulate classically, but that’s just because *nature* is hard to simulate, and you don’t get to arbitrarily redefine whatever random chemical you find in the wild to be a “computer for simulating itself.” Under any sane definition, the superconducting devices that Google, IBM, and others are now building are indeed “computers.”

**Q13. Did you (Scott Aaronson) invent the concept of quantum supremacy?**

No. I did play some role in developing it, which led to Sabine Hossenfelder among others [generously overcrediting me](http://backreaction.blogspot.com/2019/06/quantum-supremacy-what-is-it-and-what.html) for the whole idea. The term “quantum supremacy” was coined by John Preskill in 2012, though in some sense the core concept goes back to the beginnings of quantum computing itself in the early 1980s. In 1993, [Bernstein and Vazirani](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.655.1186&rep=rep1&type=pdf) explicitly pointed out the severe apparent tension between quantum mechanics and the Extended Church-Turing Thesis of classical computer science. Then, in 1994, the use of Shor’s algorithm to factor a huge number became the quantum supremacy experiment *par excellence*—albeit, one that’s still (in 2019) much too hard to perform.

The key idea of instead demonstrating quantum supremacy using a *sampling problem* was, as far as I know, first suggested by Barbara Terhal and David DiVincenzo, in a [farsighted paper](https://arxiv.org/abs/quant-ph/0205133) from 2002. The “modern” push for sampling-based supremacy experiments started around 2011, when Alex Arkhipov and I published our [paper on BosonSampling](https://arxiv.org/abs/1011.3245), and (independently of us) Bremner, Jozsa, and Shepherd published their [paper on the commuting Hamiltonians model](https://arxiv.org/abs/1005.1407). These papers showed, not only that “simple,” non-universal quantum systems can solve apparently-hard sampling problems, but also that an efficient classical algorithm for the same sampling problems would imply a collapse of the [polynomial hierarchy](https://en.wikipedia.org/wiki/Polynomial_hierarchy). Arkhipov and I also made a start toward arguing that even the *approximate* versions of quantum sampling problems can be classically hard.

As far as I know, the idea of “Random Circuit Sampling”—that is, generating your hard sampling problem by just picking a random sequence of 2-qubit gates in (say) a superconducting architecture—originated in an email thread that I started in December 2015, which also included John Martinis, Hartmut Neven, Sergio Boixo, Ashley Montanaro, Michael Bremner, Richard Jozsa, Aram Harrow, Greg Kuperberg, and others. The thread was entitled “Hard sampling problems with 40 qubits,” and my email began “Sorry for the spam.” I then discussed some advantages and disadvantages of three options for demonstrating sampling-based quantum supremacy: (1) random circuits, (2) commuting Hamiltonians, and (3) BosonSampling. After Greg Kuperberg chimed in to support option (1), a consensus quickly formed among the participants that (1) was indeed the best option from an engineering standpoint—and that, if the theoretical analysis wasn’t yet satisfactory for (1), then that was something we could remedy.

[**Update:** Sergio Boixo tells me that, internally, the Google group had been considering the idea of random circuit sampling since February 2015, even before my email thread. This doesn’t surprise me: while there are lots of details that had to be worked out, the idea itself is an extremely natural one.]

After that, the Google group did a huge amount of analysis of random circuit sampling, both theoretical and numerical, while [Lijie Chen and I](https://arxiv.org/abs/1612.05903) and [Bouland et al.](https://arxiv.org/abs/1803.04402) supplied different forms of complexity-theoretic evidence for the problem’s classical hardness.

**Q14. If quantum supremacy was achieved, what would it mean for the QC skeptics?**

I wouldn’t want to be them right now! They could retreat to the position that *of course* quantum supremacy is possible (who ever claimed that it wasn’t? surely not them!), that the real issue has always been quantum error-correction. And indeed, some of them have consistently maintained that position all along. But others, including my good friend Gil Kalai, are **on record, right here on this blog** predicting that even quantum supremacy can never be achieved for fundamental reasons. I won’t let them wiggle out of it now.

[**Update:** As many of you will have seen, Gil Kalai has [taken the position](https://gilkalai.wordpress.com/2019/09/23/quantum-computers-amazing-progress-google-ibm-and-extraordinary-but-probably-false-supremacy-claims-google/) that the Google result won’t stand and will need to be retracted. He asked for more data: specifically, a complete histogram of the output probabilities for a smaller number of qubits. This turns out to be already available, in a *[Science](https://arxiv.org/abs/1709.06678)*[paper from 2018](https://arxiv.org/abs/1709.06678).]

**Q15. What’s next?**

*If* it’s achieved quantum supremacy, then I think the Google group already has the requisite hardware to demonstrate my [protocol for generating certified random bits](https://www.scottaaronson.com/talks/certrand2.ppt). And that’s indeed one of the very next things they’re planning to do.

[**Addendum:** Also, of course, the evidence for quantum supremacy itself can be made stronger and various loopholes closed—for example, by improving the fidelity so that fewer samples need to be taken (something that Umesh Vazirani tells me he’d like to see), by having the circuit C be generated and the outputs verified by a skeptic external to Google. and simply by letting more time pass, so outsiders can have a crack at simulating the results classically. My personal guess is that the basic picture is going to stand, but just like with the first experiments that claimed to violate the Bell inequality, there’s still plenty of room to force the skeptics into a tinier corner.]

Beyond that, one obvious next milestone would be to use a programmable QC, with (say) 50-100 qubits, to do some *useful quantum simulation* (say, of a condensed-matter system) much faster than any known classical method could do it. A second obvious milestone would be to demonstrate the use of quantum error-correction, to keep an encoded qubit alive for longer than the underlying physical qubits remain alive. There’s no doubt that Google, IBM, and the other players will now be racing toward both of these milestones.

[**Update:** Steve Girvin reminds me that the Yale group [has already achieved](https://arxiv.org/abs/1602.04768) quantum error-correction “beyond the break-even point,” albeit in a bosonic system rather than superconducting qubits. So perhaps a better way to phrase the next milestone would be: achieve quantum computational supremacy *and* useful quantum error-correction in the same system.]

|     |
| --- |
|     |

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fwww.scottaaronson.com%2Fblog%2F%3Fp%3D4317&ref_src=twsrc%5Etfw&text=Scott%E2%80%99s%20Supreme%20Quantum%20Supremacy%20FAQ!&tw_p=tweetbutton&url=https%3A%2F%2Fwww.scottaaronson.com%2Fblog%2F%3Fp%3D4317)

[![](../_resources/4c1b1f0164c28fbfcf7134bc0f581c95.png) Follow](http://www.specificfeeds.com/follow)

[(L)](https://www.facebook.com/sharer/sharer.php?kid_directed_site=0&sdk=joey&u=https%3A%2F%2Fwww.scottaaronson.com%2Fblog%2F%3Fp%3D4317&display=popup&ref=plugin&src=share_button)

This entry was posted on Monday, September 23rd, 2019 at 3:28 pm	and is filed under [Announcements](https://www.scottaaronson.com/blog/?cat=31), [Bell's Theorem? But a Flesh Wound!](https://www.scottaaronson.com/blog/?cat=33), [Complexity](https://www.scottaaronson.com/blog/?cat=5), [Quantum](https://www.scottaaronson.com/blog/?cat=4). You can follow any responses to this entry through the [RSS 2.0](https://www.scottaaronson.com/blog/?feed=rss2&p=4317) feed.

Responses are currently closed, but you can [trackback](https://www.scottaaronson.com/blog/wp-trackback.php?p=4317) from your own site.