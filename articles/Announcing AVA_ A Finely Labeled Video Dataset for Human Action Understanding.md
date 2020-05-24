Announcing AVA: A Finely Labeled Video Dataset for Human Action Understanding

## [Announcing AVA: A Finely Labeled Video Dataset for Human Action Understanding](https://research.googleblog.com/2017/10/announcing-ava-finely-labeled-video.html)

Thursday, October 19, 2017
 Posted by Chunhui Gu & David Ross, Software Engineers

Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision, essential to applications such as personal video search and discovery, sports analysis, and gesture interfaces. Despite exciting breakthroughs made over the past years in [classifying](https://research.googleblog.com/2014/09/building-deeper-understanding-of-images.html) and [finding objects](https://research.googleblog.com/2017/06/supercharge-your-computer-vision-models.html) in images, recognizing human actions still remains a big challenge. This is due to the fact that actions are, by nature, less well-defined than objects in videos, making it difficult to construct a finely labeled action video dataset. And while many benchmarking datasets, e.g., [UCF101](http://crcv.ucf.edu/data/UCF101.php), [ActivityNet](http://activity-net.org/) and DeepMind’s [Kinetics](https://deepmind.com/research/open-source/open-source-datasets/kinetics/), adopt the labeling scheme of image classification and assign one label to each video or video clip in the dataset, no dataset exists for complex scenes containing multiple people who could be performing different actions.

In order to facilitate further research into human action recognition, we have released AVA, coined from “atomic visual actions”, a new dataset that provides multiple action labels for each person in extended video sequences. AVA consists of URLs for publicly available videos from YouTube, annotated with a set of 80 atomic actions (e.g. “walk”, “kick (an object)”, “shake hands”) that are spatial-temporally localized, resulting in 57.6k video segments, 96k labeled humans performing actions, and a total of 210k action labels. You can browse the [website](https://research.google.com/ava/) to explore the dataset and download annotations, and read our [arXiv paper](https://arxiv.org/abs/1705.08421) that describes the design and development of the dataset.

Compared with other action datasets, AVA possesses the following key characteristics:

- **Person-centric annotation.** Each action label is associated with a person rather than a video or clip. Hence, we are able to assign different labels to multiple people performing different actions in the same scene, which is quite common.
- **Atomic visual actions.** We limit our action labels to fine temporal scales (3 seconds), where actions are physical in nature and have clear visual signatures.
- **Realistic video material. **We use movies as the source of AVA, drawing from a variety of genres and countries of origin. As a result, a wide range of human behaviors appear in the data.

|     |
| --- |
| [![image1.gif](../_resources/371031e2f5d63adcb8eda806928b46dc.gif)](https://4.bp.blogspot.com/-F2rLgrB1t_s/Wee8Le1RF2I/AAAAAAAACGI/dWdfaRbROvcmvsE1X6zEfxd4qNDAlGaBACLcBGAs/s1600/image1.gif) |
| Examples of 3-second video segments (from [Video Source](https://www.youtube.com/watch?v=Z0FEElATNjk)) with their bounding box annotations in the middle frame of each segment. (For clarity, only one bounding box is shown for each example.) |

To create AVA, we first collected a diverse set of long form content from YouTube, focusing on the “film” and “television” categories, featuring professional actors of many different nationalities. We analyzed a 15 minute clip from each video, and uniformly partitioned it into 300 non-overlapping 3-second segments. The sampling strategy preserved sequences of actions in a coherent temporal context.

Next, we manually labeled all bounding boxes of persons in the middle frame of each 3-second segment. For each person in the bounding box, annotators selected a variable number of labels from a pre-defined atomic action vocabulary (with 80 classes) that describe the person’s actions within the segment. These actions were divided into three groups: pose/movement actions, person-object interactions, and person-person interactions. Because we exhaustively labeled all people performing all actions, the frequencies of AVA’s labels followed a long-tail distribution, as summarized below.

|     |
| --- |
| [![image3.png](../_resources/1d81227790822ef4e6a80fa787dda212.png)](https://2.bp.blogspot.com/-gd4_f0_LHRk/WeefYzqcCmI/AAAAAAAACFw/8G9FXVtYCzMcuhSv9cmVGNjHU3oOtNu1ACLcBGAs/s1600/image3.png) |
| Distribution of AVA’s atomic action labels. Labels displayed in the x-axis are only a partial set of our vocabulary. |

The unique design of AVA allows us to derive some interesting statistics that are not available in other existing datasets. For example, given the large number of persons with at least two labels, we can measure the co-occurrence patterns of action labels. The figure below shows the top co-occurring action pairs in AVA with their co-occurrence scores. We confirm expected patterns such as people frequently play instruments while singing, lift a person while playing with kids, and hug while kissing.

|     |
| --- |
| [![image2.png](../_resources/6fd2a1d60088193c5f50d6535b0a1b28.png)](https://2.bp.blogspot.com/-fZtqR07h9A0/WeefgpQRGpI/AAAAAAAACF4/EwmCNOwTBTYJvcUT79VNgHLqBunWqYyNACLcBGAs/s1600/image2.png) |
| Top co-occurring action pairs in AVA. |

To evaluate the effectiveness of human action recognition systems on the AVA dataset, we implemented an existing baseline deep learning model that obtains highly competitive performance on the much smaller [JHMDB dataset](http://jhmdb.is.tue.mpg.de/). Due to challenging variations in zoom, background clutter, cinematography, and appearance variation, this model achieves a relatively modest performance when correctly identifying actions on AVA (18.4% [mAP](https://en.wikipedia.org/wiki/Information_retrieval#Mean_average_precision)). This suggests that AVA will be a useful testbed for developing and evaluating new action recognition architectures and algorithms for years to come.

We hope that the release of AVA will help improve the development of human action recognition systems, and provide opportunities to model complex activities based on labels with fine spatio-temporal granularity at the level of individual person’s actions. We will continue to expand and improve AVA, and are eager to hear feedback from the community to help us guide future directions. Please join the AVA users [mailing list](https://groups.google.com/forum/#!forum/ava-dataset-users) to receive dataset updates as well as to send us emails for feedback.

**Acknowledgements**

The core team behind AVA includes Chunhui Gu, Chen Sun, David Ross, Caroline Pantofaru, Yeqing Li, Sudheendra Vijayanarasimhan, George Toderici, Susanna Ricco, Rahul Sukthankar, Cordelia Schmid, and Jitendra Malik. We thank many Google colleagues and annotators for their dedicated support on this project.

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

54 comments

[![photo.jpg.png](../_resources/90dc03288ae5273ac237ce19160eab19.png)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg.png](../_resources/f4914bb545dc0a6001befca5f7a06177.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)

### [Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)  -  Shared publicly

Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision. To help advance the state of the art, today we’re announcing the release of AVA, a dataset of finely-labeled atomic visual actions in video.

+
59
60
59

 ·
Reply

[![uFp_tsTJboUY7kue5XAsGA=s46.png](../_resources/ddad6fbc569f3477b41f6a32a433633b.png)](https://plus.google.com/+SigfredoZamorano)

[Sigfredo Zamorano](https://plus.google.com/+SigfredoZamorano)

[1 week ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)

+
1
2
1

Wow. This is a big challenge. Thanks for sharing +[Research at Google](https://apis.google.com/117790530324740296539).

[![photo.jpg.png](../_resources/64459b7f1b3c5519bd4f8e29958e729d.png)](https://plus.google.com/108476491967142053511)

[Multiling O Keyboard](https://plus.google.com/108476491967142053511)

[1 week ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)

+
0
1
0

This technology can be used for 🆂🅴🅲🆄🆁🅸🆃🆈　🅲🅰🅼🅴🆁🅰 too. Alert the guard if something suspicious going on.

[![photo.jpg](../_resources/b494cf71cd16175e56436000c2537740.jpg)](https://apis.google.com/u/0/wm/1/103172072345300450419)

### [Peggy K](https://apis.google.com/u/0/wm/1/103172072345300450419) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+PeggyKTC/posts/FiowapqL8Z7)  -  Shared publicly

**AVA: a video dataset for teaching computers to understand human actions**

For computers to be able to understand what is happening in a video, they need to be able to recognize human actions: watch a person or a TV, dance, answer a phone, hug, drink, eat, play a board game, sleep, talk, swim and so forth.

*To create AVA, we first collected a diverse set of long form content from YouTube, focusing on the “film” and “television” categories, featuring professional actors of many different nationalities. We analyzed a 15 minute clip from each video, and uniformly partitioned it into 300 non-overlapping 3-second segments. The sampling strategy preserved sequences of actions in a coherent temporal context.*

*Next, we manually labeled all bounding boxes of persons in the middle frame of each 3-second segment. For each person in the bounding box, annotators selected a variable number of labels from a pre-defined atomic action vocabulary (with 80 classes) that describe the person’s actions within the segment. These actions were divided into three groups: pose/movement actions, person-object interactions, and person-person interactions.*

The data also lets you see actions that frequently occur together.

*We confirm expected patterns such as people frequently play instruments while singing, lift a person while playing with kids, and hug while kissing.*

Browse the dataset:
https://research.google.com/ava/

One of the interesting things I notice is that some activities like "dance" actually include a variety of actions, some of which might be hard for a computer to distinguish from walking, running or hugging.

Learn more on the +[Research at Google](https://apis.google.com/117790530324740296539) blog:

https://research.googleblog.com/2017/10/announcing-ava-finely-labeled-video.html

+
5
6
7
6

 ·
Reply
View all 18 replies

[![photo.jpg.png](../_resources/f2ba68abec883cf23144269937aad631.jpg)](https://plus.google.com/113112109864907059463)

[XGN MLG](https://plus.google.com/113112109864907059463)

[3 days ago](https://apis.google.com/u/0/wm/1/+PeggyKTC/posts/FiowapqL8Z7)

+
0
1
0

M

[![post_twitter_black_24dp.png](../_resources/5f17ab8249d0131ec4b6c884c8f0982a.png)](https://plus.google.com/117584892248046307299)

[joey clayton](https://plus.google.com/117584892248046307299)

[1 day ago](https://apis.google.com/u/0/wm/1/+PeggyKTC/posts/FiowapqL8Z7)

+
0
1
0

DON'T SEND ME ANYMORE VIDEOS

[![photo.jpg.png](:/6776d34d59b0cf4a1c6eeb765d189858)](https://apis.google.com/u/0/wm/1/116279478726976353287)

### [Peter Teoh](https://apis.google.com/u/0/wm/1/116279478726976353287) via Google+

[12 hours ago](https://apis.google.com/u/0/wm/1/+PeterTeoh6969/posts/fWTieBG4xbk)  -  Shared publicly

https://research.googleblog.com/2017/10/announcing-ava-finely-labeled-video.html

+
0
1
0

 ·
Reply

[![post_facebook_black_24dp.png](../_resources/441cbb7966e7b6b7c013d10a2d98b1b5.png)](https://apis.google.com/u/0/wm/1/112000220562765955280)

### [Priyam Chatterjee](https://apis.google.com/u/0/wm/1/112000220562765955280)

[1 week ago](https://apis.google.com/u/0/wm/1/112000220562765955280/posts/56zjphPPMby)  -  Shared publicly

Unfortunate acronym :( AVA is a popular dataset for image aesthetics training: http://ieeexplore.ieee.org/document/6247954/

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/a77d3b4062a1d400a1d32712c74d6f10.jpg)](https://apis.google.com/u/0/wm/1/109136855341297709165)

### [Amy Unruh](https://apis.google.com/u/0/wm/1/109136855341297709165) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+AmyUnruh/posts/UXmKnGVcBgm)  -  Shared publicly

https://research.googleblog.com/2017/10/announcing-ava-finely-labeled-video.html

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/2421dd693c5c689afc08f93290ae7791.jpg)](https://apis.google.com/u/0/wm/1/107633616774873306635)

### [Berita Intermezo](https://apis.google.com/u/0/wm/1/107633616774873306635) shared this

[1 week ago](https://apis.google.com/u/0/wm/1/107633616774873306635/posts/BmrC3ZLNswJ)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/062e72151dfbc4d1ee1e5b72f940003b.jpg)](https://apis.google.com/u/0/wm/1/106505645235518117168)

### [Martin Peniak](https://apis.google.com/u/0/wm/1/106505645235518117168)

[3 days ago](https://apis.google.com/u/0/wm/1/+mpeniak/posts/CmSK87Evpx5)  -  Shared publicly

We've developed a state-of-the-art action recognition system achieving top performance on the most challenging action datasets. We have very recent publications available. Contact [www.cortexica.com](http://www.cortexica.com/) for more details.

+
1
2
1

[![photo.jpg](../_resources/f8686f327f8760b520e79ecb9849cf07.jpg)](https://apis.google.com/u/0/wm/1/103351208309622110554)

### [Octavio Herrera](https://apis.google.com/u/0/wm/1/103351208309622110554)

[1 week ago](https://apis.google.com/u/0/wm/1/103351208309622110554/posts/99EmLa3E7eY)  -  Shared publicly

So, soon enough, the videos and movies we stream with Chromecast might have advertising depending on the action being done by some person at that moment. Think, "drink CocaCola" when someone drinks Pepsi, or "Order this pizza now" when some domino's box is shown, etc ...

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/0fa217e8d75ae9d8efee6512937ddd6a.jpg)](https://apis.google.com/u/0/wm/1/109026702552951947304)

### [Xitao Zhang](https://apis.google.com/u/0/wm/1/109026702552951947304)

[4 days ago](https://apis.google.com/u/0/wm/1/109026702552951947304/posts/SBByfgjRe64)  -  Shared publicly

好玩！！
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/441cbb7966e7b6b7c013d10a2d98b1b5.png)](https://apis.google.com/u/0/wm/1/117495810352093334272)

### [CHARLENE KALEINA](https://apis.google.com/u/0/wm/1/117495810352093334272)

[4 days ago](https://apis.google.com/u/0/wm/1/117495810352093334272/posts/NDCAEgScu71)  -  Shared publicly

Perhaps you should teach humans how to understand machine actions and how machine actions are destroying thier humanity

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/3d6b90aec99359d0ac4aea9a7f8ee7c9.jpg)](https://apis.google.com/u/0/wm/1/108571452261887539484)

### [Jiqiang Zhou](https://apis.google.com/u/0/wm/1/108571452261887539484)

[5 days ago](https://apis.google.com/u/0/wm/1/108571452261887539484/posts/ZtpiuNvUgHf)  -  Shared publicly

great
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/de41239adf1a6766816168d0eb63cacd.jpg)](https://apis.google.com/u/0/wm/1/114165965714267690797)

### [Christos Malliopoulos](https://apis.google.com/u/0/wm/1/114165965714267690797) shared this via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+ChristosMalliopoulos/posts/EtzRNUJAVx5)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/9f19a0d5805658dbc3f5b483b646b43a.jpg)](https://apis.google.com/u/0/wm/1/114126308045090257233)

### [Emad Barsoum](https://apis.google.com/u/0/wm/1/114126308045090257233) shared this via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+EmadBarsoumPi/posts/fLBMHQ6DMpz)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/0de4ca2f18a0da7424b5384d2709722a.jpg)](https://apis.google.com/u/0/wm/1/117267219460476073993)

### [Cynthia Kay](https://apis.google.com/u/0/wm/1/117267219460476073993) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+CynthiaKayCastle/posts/1V6QfcJKrMZ)  -  Shared publicly

Announcing AVA: A Finely Labeled Video Dataset for Human Action Understanding
Thursday, October 19, 2017
Posted by Chunhui Gu & David Ross, Software Engineers

"Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision, essential to applications such as personal video search and discovery, sports analysis, and gesture interfaces. "

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/68bee3c3047f3ef6f5136f4fa14ba77e.png)](https://apis.google.com/u/0/wm/1/102951224065923126631)

### [Malte Steckmeister (Stecki)](https://apis.google.com/u/0/wm/1/102951224065923126631) shared this via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+MalteSteckmeister/posts/Y6rm5baVT29)  -  Shared publicly

+
0
1
0

 ·
Reply

[![uFp_tsTJboUY7kue5XAsGA=s28.png](../_resources/441cbb7966e7b6b7c013d10a2d98b1b5.png)](https://apis.google.com/u/0/wm/1/101864984180467819031)

### [tapazzal hosain](https://apis.google.com/u/0/wm/1/101864984180467819031) via Google+

[4 days ago](https://apis.google.com/u/0/wm/1/101864984180467819031/posts/LvEsEYYiKC5)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/103172072345300450419)[Peggy K](https://apis.google.com/u/0/wm/1/103172072345300450419) originally shared [this](https://apis.google.com/u/0/wm/1/+PeggyKTC/posts/FiowapqL8Z7)

**AVA: a video dataset for teaching computers to understand human actions**

For computers to be able to understand what is happening in a video, they need to be able to recognize human actions: watch a person or a TV, dance, answer a phone, hug, drink, eat, play a board game, sleep, talk, swim and so forth.

*To create AVA, we first collected a diverse set of long form content from YouTube, focusing on the “film” and “television” categories, featuring professional actors of many different nationalities. We analyzed a 15 minute clip from each video, and uniformly partitioned it into 300 non-overlapping 3-second segments. The sampling strategy preserved sequences of actions in a coherent temporal context.*

*Next, we manually labeled all bounding boxes of persons in the middle frame of each 3-second segment. For each person in the bounding box, annotators selected a variable number of labels from a pre-defined atomic action vocabulary (with 80 classes) that describe the person’s actions within the segment. These actions were divided into three groups: pose/movement actions, person-object interactions, and person-person interactions.*

The data also lets you see actions that frequently occur together.

*We confirm expected patterns such as people frequently play instruments while singing, lift a person while playing with kids, and hug while kissing.*

Browse the dataset:
https://research.google.com/ava/

One of the interesting things I notice is that some activities like "dance" actually include a variety of actions, some of which might be hard for a computer to distinguish from walking, running or hugging.

Learn more on the +[Research at Google](https://apis.google.com/117790530324740296539) blog:

https://research.googleblog.com/2017/10/announcing-ava-finely-labeled-video.html

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/1a75e9fa22a733f2900827d0c176e9da.jpg)](https://apis.google.com/u/0/wm/1/117069715888599808144)

### [Rahul Sukthankar](https://apis.google.com/u/0/wm/1/117069715888599808144) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+RahulSukthankar/posts/PCg5ZvQDNcp)  -  Shared publicly

New video dataset from our group -- encourage researchers to use it!

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)

Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision. To help advance the state of the art, today we’re announcing the release of AVA, a dataset of finely-labeled atomic visual actions in video.

+
6
7
6

 ·
Reply

[![photo.jpg](../_resources/874884f9f48b7e8d01d9d2282c6c63cc.jpg)](https://apis.google.com/u/0/wm/1/116852831691622764701)

### [على, نجاتى‎](https://apis.google.com/u/0/wm/1/116852831691622764701) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/116852831691622764701/posts/EKwMUAPbgH5)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)

Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision. To help advance the state of the art, today we’re announcing the release of AVA, a dataset of finely-labeled atomic visual actions in video.

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/01e644ebd208397521ebc950c159b07d.jpg)](https://apis.google.com/u/0/wm/1/102076128417589427747)

### [Greg Linden](https://apis.google.com/u/0/wm/1/102076128417589427747) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+GregLinden/posts/3edDj3YWmuL)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)

Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision. To help advance the state of the art, today we’re announcing the release of AVA, a dataset of finely-labeled atomic visual actions in video.

+
1
2
1

 ·
Reply

[![photo.jpg](:/112a512804feec929b66324fca761c8f)](https://apis.google.com/u/0/wm/1/106756946037071810677)

### [Tau-Mu Yi](https://apis.google.com/u/0/wm/1/106756946037071810677) via Google+

[1 week ago](https://apis.google.com/u/0/wm/1/+TauMuYi/posts/RXLLnukeBeT)  -  Shared publicly

[(L)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/DgYtNrLUhMs)

Teaching machines to understand human actions in videos is a fundamental research problem in Computer Vision. To help advance the state of the art, today we’re announcing the release of AVA, a dataset of finely-labeled atomic visual actions in video.

+
0
1
0

 ·
Reply

Show more

Labels:[Computer Vision](https://research.googleblog.com/search/label/Computer%20Vision) , [datasets](https://research.googleblog.com/search/label/datasets) , [video](https://research.googleblog.com/search/label/video)