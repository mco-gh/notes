The Google Brain team — Looking Back on 2016

## [The Google Brain team — Looking Back on 2016](https://research.googleblog.com/2017/01/the-google-brain-team-looking-back-on.html)

Thursday, January 12, 2017

 Posted by Jeff Dean, Google Senior Fellow, on behalf of the entire Google Brain team

The [Google Brain team](https://g.co/brain)'s long-term goal is to create more intelligent software and systems that improve people's lives, which we pursue through both pure and applied research in a variety of different domains. And while this is obviously a long-term goal, we would like to take a step back and look at some of the progress our team has made over the past year, and share what we feel may be in store for 2017.

**Research Publications**

One important way in which we assess the quality of our research is through publications in top tier international machine learning venues like [ICML](https://research.googleblog.com/2016/06/icml-2016-research-at-google.html), [NIPS](https://research.googleblog.com/2016/12/nips-2016-research-at-google.html), and [ICLR](https://research.googleblog.com/2016/05/research-at-google-and-iclr-2016.html). Last year our team had a total of 27 accepted papers at these venues, covering a wide ranging set of topics including [program synthesis](https://arxiv.org/abs/1511.04834), [knowledge transfer from one network to another](https://arxiv.org/abs/1511.05641), [distributed training of machine learning models](https://openreview.net/pdf?id=D1VDZ5kMAu5jEJ1zfEWL), [generative models for language](https://openreview.net/forum?id=D1VVBv7BKS5jEJ1zfxJg), [unsupervised learning for robotics](http://papers.nips.cc/paper/6161-unsupervised-learning-for-physical-interaction-through-video-prediction), [automated theorem proving](http://papers.nips.cc/paper/6280-deepmath-deep-sequence-models-for-premise-selection), [better theoretical understanding of neural networks](http://papers.nips.cc/paper/6427-toward-deeper-understanding-of-neural-networks-the-power-of-initialization-and-a-dual-view-on-expressivity), [algorithms for improved reinforcement learning](http://jmlr.org/proceedings/papers/v48/gu16.html), and many others. We also had numerous other papers accepted at conferences in fields such as natural language processing ([ACL](http://acl2017.org/), [CoNNL](http://www.conll.org/)), speech ([ICASSP](http://www.ieee-icassp2017.org/)), vision ([CVPR](http://cvpr2017.thecvf.com/)), robotics ([ISER](http://www.iser2016.org/)), and computer systems ([OSDI](https://www.usenix.org/conference/osdi16)). Our group has also submitted 34 papers to the upcoming [ICLR 2017](https://openreview.net/group?id=ICLR.cc/2017/conference), a top venue for cutting-edge deep learning research. You can learn more about our work in our list of papers, [here](https://research.google.com/pubs/BrainTeam.html).

**Natural Language Understanding**

Allowing computers to better understand human language is one key area for our research. In late 2014, three Brain team researchers published a paper on [Sequence to Sequence Learning with Neural Networks](https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf), and demonstrated that the approach could be used for machine translation. In 2015, we showed that this this approach could also be used for [generating captions for images](http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Vinyals_Show_and_Tell_2015_CVPR_paper.html), [parsing sentences](http://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf), and [solving computational geometry problems](https://arxiv.org/abs/1506.03134). In 2016, this previous research (plus many enhancements) culminated in Brain team members worked closely with members of the Google Translate team to wholly [replace the translation algorithms powering Google Translate](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html) with a completely end-to-end learned system ([research paper](https://arxiv.org/abs/1609.08144)). This new system closed the gap between the old system and human quality translations by up to 85% for some language pairs. A few weeks later, we showed how the system could do “[zero-shot translation](https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html)”, learning to translate between languages for which it had never seen example sentence pairs ([research paper](https://arxiv.org/abs/1611.04558)). This system is now deployed on the production Google Translate service for a growing number of language pairs, giving our users higher quality translations and allowing people to communicate more effectively across language barriers. Gideon Lewis-Kraus documented this translation effort (along with the history of deep learning and the history of the Google Brain team) in “[The Great A.I. Awakening](http://www.nytimes.com/2016/12/14/magazine/the-great-ai-awakening.html)”, an in-depth article that appeared in *The NY Times Magazine* in December, 2016.

**Robotics**

Traditional robotics control algorithms are carefully and painstakingly hand-programmed, and therefore embodying robots with new capabilities is often a very laborious process. We believe that having robots automatically learn to acquire new skills through machine learning is a better approach. Last year, we collaborated with researchers at [[X]](http://x.company/) to demonstrate how robotic arms could [learn hand-eye coordination](https://research.googleblog.com/2016/03/deep-learning-for-robots-learning-from.html), pooling their experiences to teach themselves more quickly ([research paper](https://arxiv.org/abs/1603.02199)). Our robots made about 800,000 grasping attempts during this research. Later in the year, [we explored three possible ways for robots to learn new skills](https://research.googleblog.com/2016/10/how-robots-can-acquire-new-skills-from.html), through reinforcement learning, through their own interaction with objects, and through human demonstrations. We’re continuing to build on this work in our goals for making robots that are able to flexibly and readily learn new tasks and operate in messy, real-world environments. To help other robotics researchers, we have [made multiple robotics datasets publicly available](https://sites.google.com/site/brainrobotdata/home).

**Healthcare**

We are excited by the potential to use machine learning to augment the abilities of doctors and healthcare practitioners. As just one example of the possibilities, in a [paper](http://jamanetwork.com/journals/jama/article-abstract/2588763) published in the *Journal of the American Medical Association* ([JAMA](http://jamanetwork.com/journals/jama)), we demonstrated that a machine-learning driven system for diagnosing diabetic retinopathy from a retinal image could perform on-par with board-certified ophthalmologists. With more than 400 million people at risk for blindness if early symptoms of diabetic retinopathy go undetected, but too few ophthalmologists to perform the necessary screening in many countries, this technology could help ensure that more people receive the proper screening. We are also doing work in other medical imaging domains, as well as investigating the use of machine learning for other kinds of medical prediction tasks. We believe [that machine learning can improve the quality and efficiency of the healthcare experience for doctors and patients](https://g.co/brain/healthcare), and we’ll have more to say about our work in this area in 2017.

**Music and Art Generation**

Technology has always helped define how people create and share media — consider the printing press, film or the electric guitar. Last year we started a project called [Magenta](https://magenta.tensorflow.org/) to [explore the intersection of art and machine intelligence](https://research.googleblog.com/2016/02/exploring-intersection-of-art-and.html), and the potential of using machine learning systems to augment human creativity. Starting with music and image generation and moving to areas like text generation and VR, Magenta is advancing the state-of-the-art in generative models for content creation. We’ve helped to organize a [one-day symposium](http://grayarea.org/event/art-machine-learning-symposium/) on these topics and [supported an art exhibition of machine generated art](http://grayarea.org/event/deepdream-the-art-of-neural-networks/). We’ve explored a variety of topics in [music generation](https://magenta.tensorflow.org/2016/07/15/lookback-rnn-attention-rnn/) and [artistic style transfer](https://magenta.tensorflow.org/2016/11/01/multistyle-pastiche-generator/), and [our jam session demo won the Best Demo Award at NIPS 2016](https://magenta.tensorflow.org/2016/12/16/nips-demo/).

**AI Safety and Fairness**

As we develop more powerful and sophisticated AI systems and deploy them in a wider variety of real-world settings, we want to ensure that these systems are both safe and fair, and we also want to build tools to help humans better understand the output they produce. In the area of AI safety, in a cross-institutional collaboration with researchers at Stanford, Berkeley, and OpenAI, we published a [white paper on Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) (see the [blog post here](https://research.googleblog.com/2016/06/bringing-precision-to-ai-safety.html)). The paper outlines some specific problems and areas where we believe there is real and foundational research to be done in the area of AI safety. One aspect of safety on which we are making progress is the protection of the privacy of training data, obtaining [differential privacy guarantees](https://arxiv.org/abs/1607.00133), most recently via [knowledge transfer techniques](https://arxiv.org/abs/1610.05755). In addition to safety, as we start to rely on AI systems to make more complex and sophisticated decisions, we want to ensure that those decisions are fair. In [a paper on equality of opportunity in supervised learning](https://arxiv.org/abs/1610.02413) (see the [blog post here](https://research.googleblog.com/2016/10/equality-of-opportunity-in-machine.html)), we showed how to optimally adjust any trained predictor to prevent one particular formal notion of discrimination, and the paper illustrated this with a case study based on FICO credit scores. To make this work more accessible, we also [created a visualization to help illustrate and interactively explore the concepts from the paper](https://research.google.com/bigpicture/attacking-discrimination-in-ml/).

**TensorFlow**

In November 2015, we [open-sourced an initial version of TensorFlow](https://research.googleblog.com/2015/11/tensorflow-googles-latest-machine_9.html) so that the rest of the machine learning community could benefit from it and we could all collaborate to jointly improve it. In 2016, TensorFlow became [the most popular machine learning project on GitHub](https://github.com/tensorflow/tensorflow), with over 10,000 commits by more than 570 people. [TensorFlow’s repository of models](https://github.com/tensorflow/models) has grown with contributions from the community, and there are also [more than 5000 TensorFlow-related repositories](https://github.com/search?q=tensorflow) listed on GitHub alone! Furthermore, TensorFlow has been widely adopted by [well-known research groups and large companies](https://www.tensorflow.org/#companies-using-tensorflow) including [DeepMind](https://research.googleblog.com/2016/04/deepmind-moves-to-tensorflow.html), and applied towards or some unusual applications like [finding sea cows Down Under](https://blog.google/topics/machine-learning/could-machine-learning-save-sea-cow/) and [sorting cucumbers in Japan](https://cloud.google.com/blog/big-data/2016/08/how-a-japanese-cucumber-farmer-is-using-deep-learning-and-tensorflow).

We’ve made [numerous performance improvements](https://github.com/tensorflow/tensorflow/blob/master/RELEASE.md), [added support for distributed training](https://research.googleblog.com/2016/04/announcing-tensorflow-08-now-with.html), brought TensorFlow to [iOS](https://petewarden.com/2016/09/27/tensorflow-for-mobile-poets/), [Raspberry Pi](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/pi_examples/) and [Windows](https://developers.googleblog.com/2016/11/tensorflow-0-12-adds-support-for-windows.html), and integrated TensorFlow with widely-used [big data infrastructure](https://github.com/tensorflow/ecosystem). We’ve extended [TensorBoard](https://www.tensorflow.org/how_tos/summaries_and_tensorboard/), TensorFlow’s visualization system with improved tools for visualizing [computation graphs](https://www.tensorflow.org/versions/master/how_tos/graph_viz/) and [embeddings](https://research.googleblog.com/2016/12/open-sourcing-embedding-projector-tool.html). We’ve also made TensorFlow accessible from [Go](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/go/README.md), [Rust](https://github.com/tensorflow/rust/blob/master/README.md) and [Haskell](https://github.com/tensorflow/haskell/blob/master/README.md), released [state-of-the-art image classification models](https://research.googleblog.com/2016/08/improving-inception-and-image.html), [Wide and Deep](https://research.googleblog.com/2016/06/wide-deep-learning-better-together-with.html) and answered thousands of questions on [GitHub](https://github.com/tensorflow/tensorflow/issues), [StackOverflow](http://stackoverflow.com/questions/tagged/tensorflow) and the [TensorFlow mailing list](https://groups.google.com/a/tensorflow.org/forum/#!forum/discuss) along the way. [TensorFlow Serving](https://research.googleblog.com/2016/02/running-your-models-in-production-with.html) simplifies the process of serving TensorFlow models in production, and for those working in the cloud, [Google Cloud Machine Learning](https://cloud.google.com/ml/) offers TensorFlow as a managed service.

Last November, we [celebrated TensorFlow’s one year anniversary as an open-source project](https://research.googleblog.com/2016/11/celebrating-tensorflows-first-year.html), and presented a [paper on the computer systems aspects of TensorFlow](https://www.usenix.org/conference/osdi16/technical-sessions/presentation/abadi) at [OSDI](https://www.usenix.org/conference/osdi16), one of the premier computer systems research conferences. In collaboration with our colleagues in the compiler team at Google we’ve also been hard at work on a [backend compiler for TensorFlow called XLA](https://www.tensorflow.org/versions/master/experimental/xla/), an alpha version of which was recently [added to the open-source release](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler).

**Machine Learning Community Involvement**

We also strive to educate and mentor people in how to do machine learning and how to conduct research in this field. Last January, Vincent Vanhoucke, one of the research leads in the Brain team, developed and worked with Udacity to make available a [free online deep learning course](https://www.udacity.com/course/deep-learning--ud730) ([blog announcement](https://research.googleblog.com/2016/01/teach-yourself-deep-learning-with.html)). We also put together [TensorFlow Playground](http://playground.tensorflow.org/), a fun and interactive system to help people better understand and visualize how very simple neural networks learn to accomplish tasks.

In June we welcomed our first class of 27 [Google Brain Residents](https://g.co/brainresidency), selected from more than 2200 applicants, and [in seven months they have already conducted significantly original research, helping to author 21 research papers](https://research.googleblog.com/2017/01/google-brain-residency-program-7-months_5.html). In August, many Brain team members took part in a [Google Brain team Reddit AMA (Ask Me Anything) on r/MachineLearning](https://www.reddit.com/r/MachineLearning/comments/4w6tsv/ama_we_are_the_google_brain_team_wed_love_to/) to answer the community’s questions about machine learning and our team. Throughout the year, we also hosted 46 student interns (mostly Ph.D. students) in our group to conduct research and work with our team members.

**Spreading Machine Learning within Google**

In addition to the public-facing activities outlined above, we have continued to work within Google to spread machine learning expertise and awareness throughout our many product teams, and to ensure that the company as a whole is well positioned to take advantage of any new machine learning research that emerges. As one example, we worked closely with our platforms team to provide specifications and high level goals for Google’s Tensor Processing Unit (TPU), a [custom machine learning accelerator ASIC that was discussed at Google I/O](https://cloudplatform.googleblog.com/2016/05/Google-supercharges-machine-learning-tasks-with-custom-chip.html). This custom chip provides an order of magnitude improvement for machine learning workloads, and is heavily used throughout our products, including for [RankBrain](https://www.bloomberg.com/news/articles/2015-10-26/google-turning-its-lucrative-web-search-over-to-ai-machines), for the recently launched [Neural Machine Translation system](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html), and for the [AlphaGo](https://deepmind.com/research/alphago/) match against Lee Sedol in Korea last March.

All in all, 2016 was an exciting year for the Google Brain team and our many collaborators and colleagues both within and outside of Google, and we look forward to our machine learning research having significant impact in 2017!

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

83 comments

[![photo.jpg](../_resources/46d0e580386337d1385bccaa4ac6a5ad.jpg)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg](../_resources/6e969a30d096fed8cf9f7db8441070f7.jpg)](https://apis.google.com/u/0/wm/1/118227548810368513262)

### [Jeff Dean](https://apis.google.com/u/0/wm/1/118227548810368513262) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+JeffDean/posts/cW7TsbWFcHJ)  -  Shared publicly

**The Google Brain team — Looking Back on 2016**

I wrote up a blog post about the work the Google Brain team has been doing over 2016. I'm really excited to work with such great colleagues! In writing this up, it's pretty remarkable to me that nearly every other sentence has one or a few links to many more details on significant and impactful work.

+
99
100
99

 ·
Reply
View all 4 replies

[![photo.jpg](../_resources/9b3a5525636bc2000c4c170d7f312123.jpg)](https://plus.google.com/100018059588528410640)

[Napatsanun Kulpatwattana](https://plus.google.com/100018059588528410640)

[1 month ago](https://apis.google.com/u/0/wm/1/+JeffDean/posts/cW7TsbWFcHJ)

+
1
2
1

Thank you very much for your kindness and all Google Teacher everyone for all of your kindness support to my improvement Technology skills and gave me a big changing of my life.

[![photo.jpg](../_resources/78ea8ff700e0b8e9089b43680b8d3705.jpg)](https://plus.google.com/+IgorGabrielan)

[Igor Gabrielan](https://plus.google.com/+IgorGabrielan)

[1 month ago](https://apis.google.com/u/0/wm/1/+JeffDean/posts/cW7TsbWFcHJ)

+
0
1
0

I make a website [pr.ai](http://pr.ai/) and a catalogue of domain names *.ai [anguilla-ai.com](http://anguilla-ai.com/) .

Now I am selling a domain name [brain.ai](http://brain.ai/) on an auction https://sedo.com/search/details/?aid=214265

To continue to trade at a price higher than ten thousand dollars, you need to get certified here

https://sedo.com/member/membercert

[![photo.jpg.png](../_resources/2282dca9047cf28c5685e2c33a1fcdd7.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)

### [Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/X2DMxSz8HWp)  -  Shared publicly

The Google Brain team's ([g.co/brain](http://g.co/brain)) long-term goal is to create more intelligent software and systems that improve people's lives, which we pursue through both pure and applied research in a variety of different domains. And while this is obviously a long-term goal, we would like to take a step back and look at some of the progress our team has made over the past year.

+
8
0
1
0

 ·
Reply

[![photo.jpg](../_resources/0489a3d63239367672a3bb7d20585c76.jpg)](https://plus.google.com/+KrisKitchen)

[Kris Kitchen](https://plus.google.com/+KrisKitchen)

[2 months ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/X2DMxSz8HWp)

+
0
1
0

2017 is going to get WIERD.

[![photo.jpg](../_resources/9504a588f7dd3374430415b13b852528.jpg)](https://plus.google.com/105434550285118450631)

[K.W. Mc.](https://plus.google.com/105434550285118450631)

[2 months ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/X2DMxSz8HWp)

+
0
1
0

I won't hold you back

[![photo.jpg](../_resources/b4237724ff78ceed94b4bddd9db6b79f.jpg)](https://apis.google.com/u/0/wm/1/106515636986325493284)

### [Bill Slawski](https://apis.google.com/u/0/wm/1/106515636986325493284) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+BillSlawski/posts/M3KyJAUHHog)  -  Shared publicly

What did the Google Brain team do in 2015? They appear to have been very active in bringing machine learning to Google.

+
8
9
8

 ·
Reply

[![photo.jpg](../_resources/d6d03d2ddfab3d66672146fa762253ff.jpg)](https://apis.google.com/u/0/wm/1/111578115386716207492)

### [Vincent Vanhoucke](https://apis.google.com/u/0/wm/1/111578115386716207492) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+VincentVanhoucke/posts/EgoqA7SA2Gw)  -  Shared publicly

A look back at what we've been up to in 2016.
+
1
6
7
6

 ·
Reply

[![photo.jpg.png](../_resources/b36cc8f1efc98b26064f903ad154e42b.png)](https://plus.google.com/+SigfredoZamorano)

[Sigfredo Zamorano](https://plus.google.com/+SigfredoZamorano)

[2 months ago](https://apis.google.com/u/0/wm/1/+VincentVanhoucke/posts/EgoqA7SA2Gw)

+
0
1
0

Great mix of applied intelligence,
congratulations all for the great work!

[![photo.jpg.png](../_resources/a5d344aa18b3bde0281f1aebc5175f2a.png)](https://apis.google.com/u/0/wm/1/115899664865909744502)

### [Alphabet Investor Relations](https://apis.google.com/u/0/wm/1/115899664865909744502) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+alphabetir/posts/P44gppjM2wk)  -  Shared publicly

“The Google Brain team's long-term goal is to create more intelligent software and systems that improve people's lives, which we pursue through both pure and applied research in a variety of different domains. And while this is obviously a long-term goal, we would like to take a step back and look at some of the progress our team has made over the past year, and share what we feel may be in store for 2017.”

+
7
8
7

[![photo.jpg](../_resources/2b512ebe4a7868832664a1a423516e04.jpg)](https://apis.google.com/u/0/wm/1/114173171541798495279)

### [Olaf Kopp](https://apis.google.com/u/0/wm/1/114173171541798495279)

[1 month ago](https://apis.google.com/u/0/wm/1/114173171541798495279/posts/4Y1RpbMWu4G)  -  Shared publicly

Research Blog: The Google Brain team — Looking Back on 2016 http://bit.ly/2jxtEyp

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/5cb4edd7a5ef821b96ea24367c3689bb.jpg)](https://apis.google.com/u/0/wm/1/103726934922431809458)

### [Aufgesang Inbound Marketing GmbH - Online Marketing Agentur Hannover](https://apis.google.com/u/0/wm/1/103726934922431809458)

[1 month ago](https://apis.google.com/u/0/wm/1/+AufgesangInboundOnlineMarketingHannover/posts/fvN5sKkXT9K)  -  Shared publicly

Research Blog: The Google Brain team — Looking Back on 2016 http://bit.ly/2jxtEyp

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/f3e61b397e52c5c7126f28c0f89b7db3.png)](https://apis.google.com/u/0/wm/1/113620843208208725814)

### [Ersin Esen](https://apis.google.com/u/0/wm/1/113620843208208725814) shared this via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+ErsinEsen/posts/QWTVfhzTvKH)  -  Shared publicly

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/5f6161a3b13b0fb7c5bb727e14737097.jpg)](https://apis.google.com/u/0/wm/1/110661035666522301036)

### [Eddie J](https://apis.google.com/u/0/wm/1/110661035666522301036)

[2 months ago](https://apis.google.com/u/0/wm/1/+EddieJ/posts/DNnduXJUEYe)  -  Shared publicly

Good work people! TensorFlow is amazing software, I think I will be using it for many years going forward. I didn't even know about TensorBoard until now. This will help me convince my mentor that TF is capable like Spark. I also wasn't aware there was a TF ASIC, I hope this will also be made available when the timing is right.

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/1706383a689604d45f9d8bd38275ff00.jpg)](https://apis.google.com/u/0/wm/1/102169659907195979238)

### [SEM Deutschland - AdWords Agentur & SEO Agentur Hannover](https://apis.google.com/u/0/wm/1/102169659907195979238)

[1 month ago](https://apis.google.com/u/0/wm/1/102169659907195979238/posts/79Lz3HuRb5v)  -  Shared publicly

Research Blog: The Google Brain team — Looking Back on 2016 http://bit.ly/2jxtEyp

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/42bede1f021dfe18a32290c43198fa47.jpg)](https://apis.google.com/u/0/wm/1/116301771956368440783)

### [Kopp Online Marketing Consulting - SEO & Content Marketing aus Hannover](https://apis.google.com/u/0/wm/1/116301771956368440783)

[1 month ago](https://apis.google.com/u/0/wm/1/+KoppOnlineMarketingConsultingHannover/posts/9TbkH6AWy1C)  -  Shared publicly

Research Blog: The Google Brain team — Looking Back on 2016 http://bit.ly/2jxtEyp

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/2f33997b4c5b9e5370dac424dd4eeae6.jpg)](https://apis.google.com/u/0/wm/1/108537601590134698281)

### [Martin J Brown Jr](https://apis.google.com/u/0/wm/1/108537601590134698281) via Google+

[2 months ago (edited)](https://apis.google.com/u/0/wm/1/108537601590134698281/posts/BEDvzby4vSc)  -  Shared publicly

https://research.googleblog.com/2017/01/the-google-brain-team-looking-back-on.html

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/53b7873e6dddd1d720926e7dbaeac68f.jpg)](https://apis.google.com/u/0/wm/1/112919583805985089145)

### [सौरभ भारती (Shaurabh Bharti)](https://apis.google.com/u/0/wm/1/112919583805985089145) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/+%E0%A4%B8%E0%A5%8C%E0%A4%B0%E0%A4%AD%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4%E0%A5%80/posts/57eBx1CYpNK)  -  Shared publicly

doing well [#ai](https://apis.google.com/s/%23ai)
+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/a55d619cff502d62bb4c52adf2d6dce8.png)](https://apis.google.com/u/0/wm/1/116074053458628889701)

### [Mike Schuster](https://apis.google.com/u/0/wm/1/116074053458628889701) via Google+

[2 months ago (edited)](https://apis.google.com/u/0/wm/1/+MikeSchuster/posts/1ses1TgeC4y)  -  Shared publicly

Summary of Google Brain in 2016

https://research.googleblog.com/2017/01/the-google-brain-team-looking-back-on.html

+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/22f51c429c9ad20d856252e00c74a1a9.jpg)](https://apis.google.com/u/0/wm/1/108894756914123773179)

### [Pedro Matias](https://apis.google.com/u/0/wm/1/108894756914123773179)

[1 month ago](https://apis.google.com/u/0/wm/1/+PedromatiasCoUk/posts/QbqoQLkQfh2)  -  Shared publicly

The Google Brain team — Looking Back on 2016
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/fdc91904800dd2ee65b53cde06ce2eef.jpg)](https://apis.google.com/u/0/wm/1/105641278830115115974)

### [Alexey Slepov](https://apis.google.com/u/0/wm/1/105641278830115115974)

[2 months ago](https://apis.google.com/u/0/wm/1/+AlexeySlepov/posts/CWbiNgGUB2F)  -  Shared publicly

"We believe that having robots automatically learn to acquire new skills through machine learning is a better approach" (Robotics section)

Could you share your forsight what are possible problems if a robot capable "to acquire new skills" will be able to learn a skill to create a bomb, commit a terroristic act, etc. thinking that it no more than just learned a new way to do its job (housekeeping, security, baby sitting)

+
0
1
0

 ·
Reply

[![photo.jpg.gif](../_resources/af4ddb143471729383a1f9c86108bce8.gif)](https://apis.google.com/u/0/wm/1/104396090596774051846)

### [Web-App Developer](https://apis.google.com/u/0/wm/1/104396090596774051846) shared this via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/104396090596774051846/posts/7XXRLzjqqTS)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/bd21cb7cf4c63d8b84255d4784ddcbe3.jpg)](https://apis.google.com/u/0/wm/1/117050651698767370248)

### [SEO](https://apis.google.com/u/0/wm/1/117050651698767370248) via Google+

[2 months ago](https://apis.google.com/u/0/wm/1/117050651698767370248/posts/P9xLWsBVBTC)  -  Shared publicly

**Google Brain Team ~ Machine Learning!**

[#google](https://apis.google.com/s/%23google)  [#machinelearning](https://apis.google.com/s/%23machinelearning)

[![photo.jpg](../_resources/8be54629d256d43c7db2cf65b416287e.jpg)](https://apis.google.com/u/0/wm/1/106515636986325493284)[Bill Slawski](https://apis.google.com/u/0/wm/1/106515636986325493284) originally shared [this](https://apis.google.com/u/0/wm/1/+BillSlawski/posts/M3KyJAUHHog)

What did the Google Brain team do in 2015? They appear to have been very active in bringing machine learning to Google.

+
7
8
7

 ·
Reply

[![photo.jpg](../_resources/b1eb33ebefd40e846d25fd76761b0c1d.jpg)](https://apis.google.com/u/0/wm/1/100951470216680850958)

### [Monika Schmidt](https://apis.google.com/u/0/wm/1/100951470216680850958) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+MonikaSchmidt/posts/URJyxMHQmhd)  -  Shared publicly

**Google Brain - How Is It Working?**

[#googlebrain](https://apis.google.com/s/%23googlebrain)  [#AI](https://apis.google.com/s/%23AI)

[![photo.jpg](../_resources/4dd5cb862a1ad4b609e1d67c9e87a7fd.jpg)](https://apis.google.com/u/0/wm/1/118227548810368513262)[Jeff Dean](https://apis.google.com/u/0/wm/1/118227548810368513262) originally shared [this](https://apis.google.com/u/0/wm/1/+JeffDean/posts/cW7TsbWFcHJ)

**The Google Brain team — Looking Back on 2016**

I wrote up a blog post about the work the Google Brain team has been doing over 2016. I'm really excited to work with such great colleagues! In writing this up, it's pretty remarkable to me that nearly every other sentence has one or a few links to many more details on significant and impactful work.

+
1
2
1

 ·
Reply

[![photo.jpg.png](../_resources/d5c8462e9c307578fa4148a3069563dc.png)](https://apis.google.com/u/0/wm/1/108969588554905275852)

### [Android Lovers - Apps, Google & Mobile Tech](https://apis.google.com/u/0/wm/1/108969588554905275852)

[2 months ago](https://apis.google.com/u/0/wm/1/108969588554905275852/posts/CNaFCo6tT4t)  -  [SEO+ - Search Engine Optimization / Website Design (Google)](https://apis.google.com/u/0/wm/1/communities/109827412704845128980/stream/556216da-1e1d-44e2-80aa-cd87a2f54617)

**Google Brain Team ~ Machine Learning!**

 [#google](https://apis.google.com/s/%23google)   [#machinelearning](https://apis.google.com/s/%23machinelearning)

[![photo.jpg](../_resources/8be54629d256d43c7db2cf65b416287e.jpg)](https://apis.google.com/u/0/wm/1/106515636986325493284)[Bill Slawski](https://apis.google.com/u/0/wm/1/106515636986325493284) originally shared [this](https://apis.google.com/u/0/wm/1/+BillSlawski/posts/M3KyJAUHHog)

What did the Google Brain team do in 2015? They appear to have been very active in bringing machine learning to Google.

+
8
9
8

View 1 reply

Show more

Labels:[Deep Learning](https://research.googleblog.com/search/label/Deep%20Learning) , [Google Brain](https://research.googleblog.com/search/label/Google%20Brain) , [Machine Learning](https://research.googleblog.com/search/label/Machine%20Learning)