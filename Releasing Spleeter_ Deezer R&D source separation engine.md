Releasing Spleeter: Deezer R&D source separation engine

# Releasing Spleeter: Deezer Research source separation engine

[![1*e9uIY-WEVlJirD1fU0yWvA.jpeg](../_resources/57d09016f13186d36c5867352ba70134.jpg)](https://deezer.io/@manuel.moussallam?source=post_page-----2b88985e797e----------------------)

[Manuel Moussallam](https://deezer.io/@manuel.moussallam?source=post_page-----2b88985e797e----------------------)

[Nov 4](https://deezer.io/releasing-spleeter-deezer-r-d-source-separation-engine-2b88985e797e?source=post_page-----2b88985e797e----------------------) · 5 min read

![1*aA2Xgd-TerQ8_kF0IARTyg.png](../_resources/c9ec39a52a6367e74c2e72d1b3ed936a.png)
![1*aA2Xgd-TerQ8_kF0IARTyg.png](../_resources/37417cc48dc7fd89744a09b6a8a583b6.png)

## In a nutshell

We are releasing [**Spleeter**](http://github.com/deezer/spleeter) to help the research community in Music Information Retrieval (MIR) leverage the power of a state-of-the-art source separation algorithm. It comes in the form of a Python Library based on [Tensorflow](https://www.tensorflow.org/), with pretrained models for 2, 4 and 5 stems separation. **Spleeter** will be presented and live-demoed at the 2019 [ISMIR conference](https://ismir2019.ewi.tudelft.nl/) in Delft.

## **A brief overview of source separation**

While not a broadly known topic, the problem of source separation has interested a large community of music signal researchers for a couple of decades now. It starts from a simple observation: music recordings are usually a mix of several individual instrument tracks (lead vocal, drums, bass, piano etc..). The task of music source separation is: given a mix can we recover these separate tracks (sometimes called *stems*)? This has many potential applications: think remixes, upmixing, active listening, educational purposes, but also pre-processing for other tasks such as transcription.

![1*j1WakLQXuQkJCXlRk0xt5g.jpeg](../_resources/76ac109b4caf7b7826ba13d0d64cb5ed.jpg)
![1*j1WakLQXuQkJCXlRk0xt5g.jpeg](../_resources/47e68493c3776ba43830d7c45bd070f6.jpg)

From a Mix of many instruments, a source separation engine like **Spleeter** outputs a set of individual tracks or stems.

Interestingly, our brain is very good at isolating instruments. Just focus on one of the instrument of [this track](https://www.deezer.com/track/2124880) (say the lead vocal for instance) and you will be able to *hear* it quite distinctively from the others. Yet that’s not really separation, you still hear all the other parts. In many cases, it may not be possible to exactly recover the individual tracks that have been mixed together. The challenge is thus to approximate them the best we can, that is to say as close as possible to the originals without creating too much distortions.

For years, a lot of strategies have been explored, by dozens of brilliant research teams from all over the world. If you’re interested in this fascinating journey you should go read [this literature overview,](https://sigsep.github.io/literature/) or [this one](http://zafarrafii.com/Publications/Rafii-Liutkus-Stoter-Mimilakis-FitzGerald-Pardo%20-%20An%20Overview%20of%20Lead%20and%20Accompaniment%20Separation%20in%20Music%20-%202018.pdf). The pace of progress has recently made some giant leaps, mainly due to advances in machine learning methods. To keep track, people have been comparing their algorithm in [international evaluation campaigns](https://sisec18.unmix.app/#/). That’s how we know that **Spleeter** performances match those of the best proposed algorithms.

Additionally, **Spleeter** is *very* fast. If you are running the GPU version you can expect separating **100x faster than real-time **which makes it a good option to process large datasets.

## What can I do with Spleeter ?

Quite a lot I’d say. If you’re a researcher working on Music Information Retrieval and have always considered that source separation artifacts made it unsuitable as a pre-processing step in your pipeline... Well, you should probably reconsider and try **Spleeter**. If you are a music hacker and want to build something awesome using **Spleeter**, then go ahead. Actually **Spleeter** is [MIT-Licensed](https://opensource.org/licenses/MIT) so you are *really* free to use it in any way you want. It goes without saying that if you plan to use **Spleeter** on copyrighted songs, make sure you get proper authorization from right owners beforehand.

## How can I use Spleeter ?

Under the hood, **Spleeter** is a fairly complex and crafted engine but we’ve worked hard to make it really easy to use. The actual separation can be achieved with a [single command line](https://github.com/deezer/spleeter/wiki/2.-Getting-started#usage), and it should work on your laptop regardless of your Operating System. For more advanced users, there is a python API class called `[Separator](https://github.com/deezer/spleeter/wiki/4.-API-Reference#separator)` that you can manipulate directly into your usual pipeline.

We’ve tried hard to come up with a [thorough documentation](https://github.com/Deezer/spleeter/wiki). Don’t hesitate to give us feedback, point out issues or suggest improvement through the traditional github tools!

* * *

*...*

## **Why release Spleeter ?**

Short answer: we use it for our research and think other might want too.

We’ve been working on source separation for a long time (and we already had a [publication at ICASSP 2019](https://ieeexplore.ieee.org/document/8683555)). We have benchmarked **Spleeter** against [Open-Unmix](https://sigsep.github.io/open-unmix/) -another open-source model recently released by a research team from Inria- and reported [slightly better performances](http://archives.ismir.net/ismir2019/latebreaking/000036.pdf) with increased speed (note that the training dataset is not the same).

One of the hard limitations faced by MIR researchers is the lack of publicly available datasets due to copyright issues. Here at **Deezer**, we have access to a fairly large catalog that we’ve been leveraging to build **Spleeter**. Since we can not share this data, turning it into an accessible tool is a way for us to make our research reproducible by everyone. On a more ethical standpoint, we feel there should not be an unfair competition between researchers based on their access to copyrighted material or lack thereof.

Last but not least, training this kind of models requires a lot of time and energy. By doing it once and sharing the result, we hope to save others some trouble and resources.

## A final word

Since we released **Spleeter**, we have received numerous feedback, most of them very positive and we’re thrilled to see all that attention given to our work. A few of these reactions may however be a little over-enthusiastic, so let’s just restate a few things. **Spleeter** is a neat tool, but in no way do we claim to have “*solved*” source separation. Hundreds of researchers and engineers working for decades have made the advances and built the tools on which **Spleeter** is based. It’s our contribution to a vivid, ever-growing and open ecosystem and hopefully something others will build upon too.

Finally, it’s worth pointing out that music mixing is a fine art and that mastering sound engineers are artists in their own rights. Obviously we do not intend to harm their work in any manner or affect anyone’s credit. When you use **Spleeter**, please do so responsibly.

That being said, happy hacking everyone!

[ ## Ready to rock?  ###  Join an agile, lean and passionate team and help us change the face of music and tech — Check our open roles!     ####  www.deezerjobs.com](https://www.deezerjobs.com/en/jobs?utm_source=deezerio&utm_medium=blogpost&utm_campaign=releasing_spleeter&source=post_page-----2b88985e797e----------------------)