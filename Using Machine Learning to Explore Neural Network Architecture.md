Using Machine Learning to Explore Neural Network Architecture

## [Using Machine Learning to Explore Neural Network Architecture](https://research.googleblog.com/2017/05/using-machine-learning-to-explore.html)

Wednesday, May 17, 2017
 Posted by Quoc Le & Barret Zoph, Research Scientists, Google Brain team

At Google, we have successfully applied deep learning models to many applications, from [image recognition](https://research.googleblog.com/2014/09/building-deeper-understanding-of-images.html) to [speech recognition](https://research.googleblog.com/2012/08/speech-recognition-and-deep-learning.html) to [machine translation](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html). Typically, our machine learning models are painstakingly designed by a team of engineers and scientists. This process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~1010 candidate networks! For this reason, the process of designing networks often takes a significant amount of time and experimentation by those with significant machine learning expertise.

|     |
| --- |
| [![image2.png](../_resources/e749d3385e98cab560b7a9ba043e729a.png)](https://3.bp.blogspot.com/-8Lsg0rnxl7k/WRtttN18MKI/AAAAAAAAB0o/KpHbFnYBmTYQ3dBjVLimPUkKphU_qLBfgCLcB/s1600/image2.png) |
| Our [GoogleNet](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43022.pdf) architecture. Design of this network required many years of careful experimentation and refinement from initial versions of convolutional architectures. |

To make this process of designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models. Among many algorithms we’ve studied, [evolutionary algorithms](https://arxiv.org/abs/1703.01041) [1] and [reinforcement learning algorithms](https://arxiv.org/abs/1611.01578) [2] have shown great promise. But in this blog post, we’ll focus on our reinforcement learning approach and the early results we’ve gotten so far.

In our approach (which we call "AutoML"), a controller neural net can propose a “child” model architecture, which can then be trained and evaluated for quality on a particular task. That feedback is then used to inform the controller how to improve its proposals for the next round. We repeat this process thousands of times — generating new architectures, testing them, and giving that feedback to the controller to learn from. Eventually the controller learns to assign high probability to areas of architecture space that achieve better accuracy on a held-out validation dataset, and low probability to areas of architecture space that score poorly. Here’s what the process looks like:

[![image3.png](:/cfe6763e7c92c3ace3fe5af97246c3a2)](https://1.bp.blogspot.com/-0nzARW3QtkA/WRtuVsUJ02I/AAAAAAAAB0s/t6ncpAH6VfIzkr2tWW8CnE6U2Es2Bs1BgCLcB/s1600/image3.png)

We’ve applied this approach to two heavily benchmarked datasets in deep learning: image recognition with [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) and language modeling with [Penn Treebank](https://catalog.ldc.upenn.edu/ldc99t42). On both datasets, our approach can design models that achieve accuracies on par with state-of-art models designed by machine learning experts (including some on our own team!).

So, what kind of neural nets does it produce? Let’s take one example: a recurrent architecture that’s trained to predict the next word on the Penn Treebank dataset. On the left here is a neural net designed by human experts. On the right is a recurrent architecture created by our method:

[![image1.png](../_resources/8f8b4d13562172bbba90c90aad3684f0.png)](https://3.bp.blogspot.com/-i_T7k1EMd9w/WRtucgbRx1I/AAAAAAAAB0w/ZKxPOsmZCt4hnqCT0nhhWyHRFdD-xssUgCLcB/s1600/image1.png)

The machine-chosen architecture does share some common features with the human design, such as using addition to combine input and previous hidden states. However, there are some notable new elements — for example, the machine-chosen architecture incorporates a multiplicative combination (the left-most blue node on the right diagram labeled “*elem_mult*”). This type of combination is not common for recurrent networks, perhaps because researchers see no obvious benefit for having it. Interestingly, a simpler form of this approach was [recently suggested](https://arxiv.org/pdf/1606.06630.pdf) by human designers, who also argued that this multiplicative combination can actually alleviate gradient vanishing/exploding issues, suggesting that the machine-chosen architecture was able to discover a useful new neural net architecture.

This approach may also teach us something about why certain types of neural nets work so well. The architecture on the right here has many channels so that the gradient can flow backwards, which may help explain why [LSTM RNNs](https://en.wikipedia.org/wiki/Long_short-term_memory) work better than standard [RNNs](https://en.wikipedia.org/wiki/Recurrent_neural_network).

Going forward, we’ll work on careful analysis and testing of these machine-generated architectures to help refine our understanding of them. If we succeed, we think this can inspire new types of neural nets and make it possible for non-experts to create neural nets tailored to their particular needs, allowing machine learning to have a greater impact to everyone.

**References**
**

** [1] [Large-Scale Evolution of Image Classifiers](https://arxiv.org/abs/1703.01041), *Esteban Real, Sherry Moore, Andrew Selle, Saurabh Saxena, Yutaka Leon Suematsu, Quoc Le, Alex Kurakin. International Conference on Machine Learning, 2017.*

[2] [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578), *Barret Zoph, Quoc V. Le. International Conference on Learning Representations, 2017.*

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

63 comments

[![photo.jpg](../_resources/46d0e580386337d1385bccaa4ac6a5ad.jpg)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg.png](../_resources/2282dca9047cf28c5685e2c33a1fcdd7.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)

### [Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) via Google+

[4 days ago](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)  -  Shared publicly

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
89
90
89

 ·
Reply

[![photo.jpg](../_resources/035272977b3af084fe9bcdced8402a05.jpg)](https://apis.google.com/u/0/wm/1/115785601687445616629)

### [Ward Plunet](https://apis.google.com/u/0/wm/1/115785601687445616629) via Google+

[4 days ago](https://apis.google.com/u/0/wm/1/+WardPlunet/posts/YPPkNUSXkoc)  -  Shared publicly

**Using Machine Learning to Explore Neural Network Architecture**

*At Google, we have successfully applied deep learning models to many applications, from image recognition to speech recognition to machine translation. Typically, our machine learning models are painstakingly designed by a team of engineers and scientists. This process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~1010 candidate networks! For this reason, the process of designing networks often takes a significant amount of time and experimentation by those with significant machine learning expertise. Our GoogleNet architecture. Design of this network required many years of careful experimentation and refinement from initial versions of convolutional architectures. To make this process of designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models. Among many algorithms we’ve studied, evolutionary algorithms [1] and reinforcement learning algorithms [2] have shown great promise. But in this blog post, we’ll focus on our reinforcement learning approach and the early results we’ve gotten so far.*

+
5
1
2
1

 ·
Reply

[![photo.jpg](../_resources/3a4926ea058faa36e18b6283077329ff.jpg)](https://apis.google.com/u/0/wm/1/111502245593180635268)

### [Claude Coulombe](https://apis.google.com/u/0/wm/1/111502245593180635268)

[3 days ago](https://apis.google.com/u/0/wm/1/111502245593180635268/posts/1Cwra7CwHFB)  -  [Deep Learning (Discussion)](https://apis.google.com/u/0/wm/1/communities/112866381580457264725/stream/fd58517b-5d7c-4328-9bc1-94982343d3c5)

Learn more about AutoML (learning how to build neural nets architecture using reinforcement learning).

+
19
20
19

View all 5 replies

[![photo.jpg](../_resources/b1b7c469b3d3b5a7ce9af0da97eee6e7.jpg)](https://plus.google.com/111502245593180635268)

[Claude Coulombe](https://plus.google.com/111502245593180635268)

[2 days ago (edited)](https://apis.google.com/u/0/wm/1/111502245593180635268/posts/1Cwra7CwHFB)

+
0
1
0

+[Pascal Gula](https://apis.google.com/108957518698206301122) It happens! Eventual Consistency in NoSQL Databases... I don't mind.

[![photo.jpg](../_resources/b1b7c469b3d3b5a7ce9af0da97eee6e7.jpg)](https://plus.google.com/111502245593180635268)

[Claude Coulombe](https://plus.google.com/111502245593180635268)

[2 days ago (edited)](https://apis.google.com/u/0/wm/1/111502245593180635268/posts/1Cwra7CwHFB)

+
0
1
0

A companion scientific paper: Abstract https://goo.gl/xYYsOO, Full PDF https://goo.gl/bPulqH

[![photo.jpg](../_resources/0f0de7d977406c7a60d17183d23470f6.jpg)](https://apis.google.com/u/0/wm/1/104517780196215805310)

### [Igor Gabrielan](https://apis.google.com/u/0/wm/1/104517780196215805310)

[2 days ago](https://apis.google.com/u/0/wm/1/+IgorGabrielan/posts/dnQRiwNQEvR)  -  Shared publicly

I sell domain names [brain.ai](http://brain.ai/)  [automl.ai](http://automl.ai/)  [baidu.ai](http://baidu.ai/)

+
0
1
0

 ·
Reply

[![photo.jpg](:/08b1760676e0d44b2d698cb2f6ff058a)](https://apis.google.com/u/0/wm/1/108030053459107859268)

### [Georg Curnutt](https://apis.google.com/u/0/wm/1/108030053459107859268)

[3 days ago](https://apis.google.com/u/0/wm/1/+GeorgCurnutt-WildeGeist-MEAUXBETA/posts/jkrpNctDg3R)  -  Shared publicly

In that last paragraph: " If we succeed, we think this can inspire new types of neural nets and make it possible for non-experts to create neural nets tailored to their particular needs, allowing machine learning to have a greater impact to everyone." So far the availability of Free and Open Source Software and access to Google is pretty good and I am confident we all will have some very functional Intelligent Machines in less than 5 years time. Very exciting times with everyone already working together to make this happen. I think you can edit that 'If we succeed' part out, I think you have succeeded. I am looking at what the near future of Embedded Ceramics alone can do for gathering various sensors data to provide so much more precise data to the picture. Text Editor projects like Atom, everything in repositories.... It will not be long now!

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/0f497a59f90fd353180c3a7e8e32a1a9.jpg)](https://apis.google.com/u/0/wm/1/104714717867434857440)

### [Viktor K (CS & IT)](https://apis.google.com/u/0/wm/1/104714717867434857440) shared this via Google+

[16 hours ago](https://apis.google.com/u/0/wm/1/+ViktorK-CSIT/posts/VudYfBDNvK5)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg.png](:/5f41bbf43afb659f690a4d4389c43843)](https://apis.google.com/u/0/wm/1/112740367348600290235)

### [Bin Chen](https://apis.google.com/u/0/wm/1/112740367348600290235)

[2 days ago](https://apis.google.com/u/0/wm/1/+PierrChen/posts/ajAhH2PuXBD)  -  Shared publicly

Great! ML scientists are out of job as well.

"We’ve applied this approach to two heavily benchmarked datasets in deep learning: image recognition with CIFAR-10 and language modeling with Penn Treebank. On both datasets, our approach can design models that achieve accuracies on par with state-of-art models designed by machine learning experts."

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/45859464afcb7413143319f4eac2d7aa.jpg)](https://apis.google.com/u/0/wm/1/117201017011104654079)

### [Rokesh Jankie](https://apis.google.com/u/0/wm/1/117201017011104654079)

[3 days ago](https://apis.google.com/u/0/wm/1/+RokeshJankie/posts/V3cL7ysSmrV)  -  Shared publicly

)Pretty impressive stuff... could be like "Inception" :)
+
0
1
0

 ·
Reply

[![photo.jpg](:/183c1b5d3836e925aa3bb9eb696632b3)](https://apis.google.com/u/0/wm/1/106281260066569019312)

### [María del Rosario Eguía](https://apis.google.com/u/0/wm/1/106281260066569019312)

[4 days ago](https://apis.google.com/u/0/wm/1/106281260066569019312/posts/VBCk3BcyC8g)  -  [YouTube Videos (Funny videos)](https://apis.google.com/u/0/wm/1/communities/117923543622735202046/stream/64e5fbd1-737d-4b58-ba09-e1863960b08b)

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
0
1
0

[![photo.jpg](../_resources/b9c31b879edccc21f1ea1f6e44c92c59.jpg)](https://apis.google.com/u/0/wm/1/103960976143004929775)

### [chmanish aol](https://apis.google.com/u/0/wm/1/103960976143004929775)

[4 days ago](https://apis.google.com/u/0/wm/1/103960976143004929775/posts/Pe7J1FiZ3dH)  -  [J G D👏 (Discussion)](https://apis.google.com/u/0/wm/1/communities/112841014109388609902/stream/438f1594-9a1e-464a-ac74-08f5d145ea7f)

[![photo.jpg](../_resources/e557d56714f9e18e7801064ac407148d.jpg)](https://apis.google.com/u/0/wm/1/115785601687445616629)[Ward Plunet](https://apis.google.com/u/0/wm/1/115785601687445616629) originally shared [this](https://apis.google.com/u/0/wm/1/+WardPlunet/posts/YPPkNUSXkoc)

**Using Machine Learning to Explore Neural Network Architecture**

*At Google, we have successfully applied deep learning models to many applications, from image recognition to speech recognition to machine translation. Typically, our machine learning models are painstakingly designed by a team of engineers and scientists. This process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~1010 candidate networks! For this reason, the process of designing networks often takes a significant amount of time and experimentation by those with significant machine learning expertise. Our GoogleNet architecture. Design of this network required many years of careful experimentation and refinement from initial versions of convolutional architectures. To make this process of designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models. Among many algorithms we’ve studied, evolutionary algorithms [1] and reinforcement learning algorithms [2] have shown great promise. But in this blog post, we’ll focus on our reinforcement learning approach and the early results we’ve gotten so far.*

+
4
5
4

[![photo.jpg](:/9a38bc5f4620e5782658c24ce528e2f4)](https://apis.google.com/u/0/wm/1/101849046032900967780)

### [Joe Gaspar](https://apis.google.com/u/0/wm/1/101849046032900967780) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+JoeGaspar/posts/iriWZhZRitW)  -  Shared publicly

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/6cfd76922a366a1f38124e5dd318e10c.jpg)](https://apis.google.com/u/0/wm/1/102545580595263766229)

### [Peter Senna Tschudin](https://apis.google.com/u/0/wm/1/102545580595263766229) via Google+

[1 day ago](https://apis.google.com/u/0/wm/1/+PeterSenna/posts/RfseRJZui5D)  -  Shared publicly

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/79a7b45b445f60eaee96cf3a565e870c.jpg)](https://apis.google.com/u/0/wm/1/117828903900236363024)

### [Daniel Estrada](https://apis.google.com/u/0/wm/1/117828903900236363024) via Google+

[3 days ago](https://apis.google.com/u/0/wm/1/+DanielEstrada/posts/ZmgrknPW3GM)  -  Shared publicly

[![photo.jpg](../_resources/e557d56714f9e18e7801064ac407148d.jpg)](https://apis.google.com/u/0/wm/1/115785601687445616629)[Ward Plunet](https://apis.google.com/u/0/wm/1/115785601687445616629) originally shared [this](https://apis.google.com/u/0/wm/1/+WardPlunet/posts/YPPkNUSXkoc)

**Using Machine Learning to Explore Neural Network Architecture**

*At Google, we have successfully applied deep learning models to many applications, from image recognition to speech recognition to machine translation. Typically, our machine learning models are painstakingly designed by a team of engineers and scientists. This process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~1010 candidate networks! For this reason, the process of designing networks often takes a significant amount of time and experimentation by those with significant machine learning expertise. Our GoogleNet architecture. Design of this network required many years of careful experimentation and refinement from initial versions of convolutional architectures. To make this process of designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models. Among many algorithms we’ve studied, evolutionary algorithms [1] and reinforcement learning algorithms [2] have shown great promise. But in this blog post, we’ll focus on our reinforcement learning approach and the early results we’ve gotten so far.*

+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/a40259522526c6b0e9417c5f3eee1748.jpg)](https://apis.google.com/u/0/wm/1/111043118013422370473)

### [Dean Chan (陈狄)](https://apis.google.com/u/0/wm/1/111043118013422370473) via Google+

[2 days ago](https://apis.google.com/u/0/wm/1/111043118013422370473/posts/THeBmiDSp76)  -  Shared publicly

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
0
1
0

[![photo.jpg](../_resources/a40259522526c6b0e9417c5f3eee1748.jpg)](https://apis.google.com/u/0/wm/1/111043118013422370473)

### [Dean Chan (陈狄)](https://apis.google.com/u/0/wm/1/111043118013422370473) via Google+

[2 days ago](https://apis.google.com/u/0/wm/1/111043118013422370473/posts/aNNnSrdZWwN)  -  Shared publicly

[![photo.jpg](../_resources/b1b7c469b3d3b5a7ce9af0da97eee6e7.jpg)](https://apis.google.com/u/0/wm/1/111502245593180635268)[Claude Coulombe](https://apis.google.com/u/0/wm/1/111502245593180635268) originally shared [this](https://apis.google.com/u/0/wm/1/111502245593180635268/posts/1Cwra7CwHFB)

Learn more about AutoML (learning how to build neural nets architecture using reinforcement learning).

+
0
1
0

[![photo.jpg](../_resources/05fb900ef8f455f1b867b707f19b932e.jpg)](https://apis.google.com/u/0/wm/1/100402450874702632243)

### [Lorenzo Pavesi](https://apis.google.com/u/0/wm/1/100402450874702632243) via Google+

[2 days ago](https://apis.google.com/u/0/wm/1/+LorenzoPavesi/posts/hytrr2nzWoR)  -  Shared publicly

[![photo.jpg](../_resources/b1b7c469b3d3b5a7ce9af0da97eee6e7.jpg)](https://apis.google.com/u/0/wm/1/111502245593180635268)[Claude Coulombe](https://apis.google.com/u/0/wm/1/111502245593180635268) originally shared [this](https://apis.google.com/u/0/wm/1/111502245593180635268/posts/1Cwra7CwHFB)

Learn more about AutoML (learning how to build neural nets architecture using reinforcement learning).

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/e9b3e43fdfca90bffa0de1d0656712f0.jpg)](https://apis.google.com/u/0/wm/1/104953398131149738549)

### [Shang Heng Wei (Shawn)](https://apis.google.com/u/0/wm/1/104953398131149738549) via Google+

[4 days ago](https://apis.google.com/u/0/wm/1/+ShangHengWei/posts/9jZ5wqjvx7H)  -  Shared publicly

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
2
3
2

 ·
Reply

[![photo.jpg.png](:/549bee076f40f48ffabe7c7ca9ed5b84)](https://apis.google.com/u/0/wm/1/111560169804673972133)

### [Fynder Enlil](https://apis.google.com/u/0/wm/1/111560169804673972133) via Google+

[3 days ago](https://apis.google.com/u/0/wm/1/+FynderEnlil/posts/HgD1cXuiWrn)  -  Shared publicly

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/a4041ab8ada16b82406106ce9ad9c297.jpg)](https://apis.google.com/u/0/wm/1/105167159715627693606)

### [Evgeniy Zheltonozhskiy](https://apis.google.com/u/0/wm/1/105167159715627693606)

[2 days ago](https://apis.google.com/u/0/wm/1/+EvgeniyZheltonozhskiy/posts/MHPfhZmGXhP)  -  Shared publicly

Are there any further work on the topic?
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/050ca25336ab77bafe049ad334956020.jpg)](https://apis.google.com/u/0/wm/1/107331470318041198804)

### [Georgе Stoyanov](https://apis.google.com/u/0/wm/1/107331470318041198804) via Google+

[3 days ago](https://apis.google.com/u/0/wm/1/+GeorgiStoyanov/posts/ij8marnsXAg)  -  Shared publicly

[![photo.jpg.png](../_resources/7d86b00d815e0a17dd169bb679f1f1a0.png)](https://apis.google.com/u/0/wm/1/117790530324740296539)[Research at Google](https://apis.google.com/u/0/wm/1/117790530324740296539) originally shared [this](https://apis.google.com/u/0/wm/1/+ResearchatGoogle/posts/5Raw67RdMGi)

The process of manually designing machine learning models is difficult because the search space of all possible models can be combinatorially large — a typical 10-layer network can have ~10^10 candidate networks! To make designing machine learning models much more accessible, we’ve been exploring ways to automate the design of machine learning models with an approach we call "AutoML". Learn more, below.

+
1
2
1

 ·
Reply

Show more

Labels:[Deep Learning](https://research.googleblog.com/search/label/Deep%20Learning) , [Google Brain](https://research.googleblog.com/search/label/Google%20Brain) , [Machine Learning](https://research.googleblog.com/search/label/Machine%20Learning)