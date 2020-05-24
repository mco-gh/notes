Google's distributed computing for dummies trains ResNet-50 in under half an hour | ZDNet

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' data-evernote-id='344' class='js-evernote-checked'%3e%3cpath d='M13 2c3.469 0 2 5 2 5s5-1.594 5 2v9h-12v-16h5zm.827-2h-7.827v20h16v-11.842c0-2.392-5.011-8.158-8.173-8.158zm-9.827 22v-20h-2v22h18v-2h-16z'%3e%3c/path%3e%3c/svg%3e) must read:   [Microsoft to start nagging users in April about the January 2020 Windows 7 end-of-support deadline](https://www.zdnet.com/article/microsoft-to-start-nagging-users-in-april-about-the-january-2020-windows-7-end-of-support-deadline/)

# Google's distributed computing for dummies trains ResNet-50 in under half an hour

Google's new "TF-Replicator" technology is meant to be drop-dead simple distributed computing for AI researchers. A key benefit of the technology can be that it takes dramatically less time to reach benchmark results on standard tasks such as ImageNet.

 [![tiernan-ray-author.jpg](../_resources/2513123112882b9af3f723538a733232.jpg)](https://www.zdnet.com/meet-the-team/us/tiernan1/)

By [Tiernan Ray](https://www.zdnet.com/meet-the-team/us/tiernan1/) | March 8, 2019 -- 23:29 GMT (23:29 GMT) | Topic: [Artificial Intelligence](https://www.zdnet.com/topic/artificial-intelligence/)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='comment-bubble js-evernote-checked' data-evernote-id='345'%3e%3cpath d='M16%2c0c8.8%2c0%2c16%2c5.3%2c16%2c11.9c0%2c2.9-2.2%2c6.3-4.6%2c8.3l2.3%2c7.2l-6.9-4.7c-2.1%2c0.7-4.3%2c1.1-6.8%2c1.1 c-8.8%2c0-16-5.3-16-11.9C0%2c5.3%2c7.2%2c0%2c16%2c0z'%3e%3c/path%3e%3c/svg%3e)0](https://www.zdnet.com/article/googles-distributed-computing-for-dummies-trains-restnet-50-in-half-an-hour/#comments-ab5fdc66-90de-468e-a346-c46e60570988)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='facebook js-evernote-checked' data-evernote-id='346'%3e%3cpath d='M15.2%2c11.1H9.6V7c0-1.2%2c1.3-1.5%2c1.9-1.5c0.6%2c0%2c3.6%2c0%2c3.6%2c0V0L11%2c0C5.4%2c0%2c4.1%2c4.1%2c4.1%2c6.7v4.4H0v5.6h4.1 c0%2c7.3%2c0%2c15.2%2c0%2c15.2h5.5c0%2c0%2c0-8.1%2c0-15.2h4.7L15.2%2c11.1z'%3e%3c/path%3e%3c/svg%3e)]()

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='linkedin js-evernote-checked' data-evernote-id='347'%3e%3cpath d='M24%2c8c-5.1%2c0.1-7.7%2c3.8-8%2c4V8h-6v24h6V18c0-0.5%2c1.3-4.6%2c6-4c2.5%2c0.2%2c3.9%2c3.5%2c4%2c4v14l6%2c0V15.4 C31.7%2c13%2c30.5%2c8.1%2c24%2c8z M0%2c32h6V8H0V32z M3%2c0C1.3%2c0%2c0%2c1.3%2c0%2c3s1.3%2c3%2c3%2c3c1.7%2c0%2c3-1.3%2c3-3S4.7%2c0%2c3%2c0z'%3e%3c/path%3e%3c/svg%3e)]()

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='twitter js-evernote-checked' data-evernote-id='348'%3e%3cpath d='M32.5%2c3.4c-0.5%2c0.3-2.2%2c1-3.7%2c1.1c1-0.6%2c2.4-2.4%2c2.8-3.9c-0.9%2c0.6-3.1%2c1.6-4.2%2c1.6c0%2c0%2c0%2c0%2c0%2c0 C26.1%2c0.9%2c24.4%2c0%2c22.5%2c0c-3.7%2c0-6.7%2c3.2-6.7%2c7.2c0%2c0.6%2c0.1%2c1.1%2c0.2%2c1.6h0C11%2c8.7%2c5.1%2c6%2c1.8%2c1.3c-2%2c3.8-0.3%2c8%2c2%2c9.5 c-0.8%2c0.1-2.2-0.1-2.9-0.8c0%2c2.5%2c1.1%2c5.8%2c5.2%2c7c-0.8%2c0.5-2.2%2c0.3-2.8%2c0.2c0.2%2c2.1%2c3%2c4.9%2c6%2c4.9c-1.1%2c1.3-4.7%2c3.8-9.3%2c3 c3.1%2c2%2c6.7%2c3.2%2c10.5%2c3.2c10.8%2c0%2c19.2-9.4%2c18.7-21.1c0%2c0%2c0%2c0%2c0%2c0c0%2c0%2c0-0.1%2c0-0.1c0%2c0%2c0-0.1%2c0-0.1C30.2%2c6.4%2c31.5%2c5.1%2c32.5%2c3.4z'%3e%3c/path%3e%3c/svg%3e)]()

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='envelope js-evernote-checked' data-evernote-id='349'%3e%3cg%3e%3cpath d='M12 12.713l-11.985-9.713h23.97l-11.985 9.713zm0 2.574l-12-9.725v15.438h24v-15.438l-12 9.725z'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()

Is it better to be as accurate as possible in machine learning, however long it takes, or pretty darned accurate in a really short amount of time?

For DeepMind researchers Peter Buchlovsky and colleagues, the choice was to go for speed of learning over theoretical accuracy.

Revealing this week a new bit of technology, called "TF-Replicator," the researchers said they were able to reach the accuracy of the top benchmark results on the familiar ImageNet competition in under half an hour, using 32 of Google's Tensor Processing Unit chips operating in parallel. The debut of Replicator comes as Google this week [previewed the 2.0 version of TensorFlow.](https://www.zdnet.com/article/google-launches-tensorflow-2-0-alpha/)

The results from using TF-Replicator, the authors claim, approached the best results from some other projects that used many more GPUs, including prior work that employed 1,024 of Nvidia's "Tesla P100" GPUs.

The implication of the TF-Replicator project is that such epic engineering of GPUs can now be achieved with a few lines of Python code that haven't been specially tuned for any particular hardware configuration.

![google-tf-replicator-patterns-2019.png](../_resources/3a821f2b914722abdcae6a9697bf886e.png)

TF-Replicator can make multiple "workers" that either share a compute graph, as on the left, or have separate compute graphs of their own, as on the right.

DeepMind

The trick is basically to make Parallel Distributed Computing for Dummies, if you will. A set of new functions have been added to Google's TensorFlow framework that, DeepMind claims, "trivializes the process of building distributed machine learning systems" by letting researchers "naturally define their model and run loop as per the single-machine setting."

**Also: **[**Google launches TensorFlow 2.0 Alpha**](https://www.zdnet.com/article/google-launches-tensorflow-2-0-alpha/)

5 IoT trends to watch this year

The IoT has become a source of real-world applications with transformative potential.

Sponsored by Interact

The system is more flexible than a previous TensorFlow approach, [called an "estimator,"](https://www.tensorflow.org/guide/estimators) which imposed restrictions on the ways models are built. While that system was predisposed to production environments, the Google approach is for the R&D lab, for making new kinds of networks, so it's designed to be more flexible.

It's also meant to be much simpler to program than previous attempts at parallelism, such as "Mesh-TensorFlow," [introduced last year by Google's Brain unit](https://papers.nips.cc/paper/8242-mesh-tensorflow-deep-learning-for-supercomputers.pdf) as a separate language to specify distributed computing.

The research, "TF-Replicator: Distributed Machine Learning For Researchers," is [posted on the arXiv pre-print server](https://arxiv.org/abs/1902.00465), and [there's also a blog post by DeepMind](https://deepmind.com/blog/tf-replicator-distributed-machine-learning/).

The working assumption in the paper is that they want to get to state-of-the-art results fast rather than to try and push the limit in terms of accuracy. As the authors point out, "Instead of attempting to improve classification accuracy, many recent papers have focused on reducing the time taken to achieve some performance threshold (typically ∼75% Top-1 accuracy)," using ImageNet benchmarks, and, in most cases, training the common "ResNet-50" neural network.

**Also: **[**Google says 'exponential' growth of AI is changing nature of compute**](https://www.zdnet.com/article/google-says-exponential-growth-of-ai-is-changing-nature-of-compute/)**  **

This rush to get to good results is known as "weak scaling," where the network is trained "in fewer steps with very large batches," grouping the data in sets of multiple thousands of examples.

Hence, the need to parallelize models to be able to work on those batches simultaneously across multiple cores and multiple GPUs or TPUs.

The authors set out to build a distributed computing system that would handle tasks ranging from classification to making fake images via generative adversarial networks (GANs) to reinforcement learning, while reaching the threshold of competent performance faster.

The authors write that a researcher doesn't need to know anything about distributed computing. The researcher specifies their neural net as a "replica," a thing that is designed to run on a single computer. That replica can be automatically multiplied to separate instances running in parallel on multiple computers provided that the author includes two Python functions to their TensorFlow code, called "input_fn" and "step_fn." The first one calls a dataset to populate each "step" of a neural network. That makes it possible to parallelize the work on data across different machines. The other function specifies the computation to be performed, and can be used to parallelize the neural network operations across many machines.

![tensorflowgraphbuilding-2019.png](../_resources/d0f4e2a6cfb34f3e359531f5c18b5519.png)

how TF-Replicator builds the compute graph on multiple machines, leaving the "placeholder" functions in the graph where communications will need to be filled in later, here represented by the dotted lines.

DeepMind.

The authors note they had to overcome some interesting limitations. For example, communications between computing nodes can be important for things such as gathering up all the gradient descent computations happening across multiple machines.

That can be challenging to engineer. If a single "graph" of a neural network is distributed across many computers, what's known as "in-graph replication," then problems can arise because parts of the compute graph may not yet be constructed, which frustrates dependencies between the computers. "One replica's step_fn can call a primitive mid graph construction," they write, referring to the communications primitives. "This requires referring to data coming from another replica that itself is yet to be built."

Their solution is to put "placeholder" code in the compute graph of each machine, which "can be re-written once all replica subgraphs are finalized."

![tf-replicator-imagenet-results-2019.png](../_resources/7ed79102064fe23a0a90354e3b04d9cc.png)

Results of various configurations of TF-Replicator for the ImageNet tasks on different configurations of hardware.

DeepMind

###  Must read

- ['AI is very, very stupid,' says Google's AI leader](https://www.cnet.com/news/ai-is-very-stupid-says-google-ai-leader-compared-to-humans/?ftag=CMG-01-10aaa1b) (CNET)
- [How to get all of Google Assistant's new voices right now](https://www.cnet.com/how-to/how-to-get-all-google-assistants-new-voices-right-now/?ftag=CMG-01-10aaa1b) (CNET)
- [Unified Google AI division a clear signal of AI's future](https://www.techrepublic.com/article/unified-google-ai-division-a-clear-signal-of-ais-future-in-tech-industry/?ftag=CMG-01-10aaa1b) (TechRepublic)
- [Top 5: Things to know about AI](https://www.techrepublic.com/article/top-5-things-to-know-about-ai/?ftag=CMG-01-10aaa1b) (TechRepublic)

* * *

The authors describe results across various benchmark tests. In the case of the ResNet-50 ImageNet task, "we are able to match the published 75.3% Top-1 accuracy in less than 30 minutes of training," they write, adding that "these results are obtained using the standard TF-Replicator implementation, without any systems optimization specific to ImageNet classification."

On a GAN task, producing images, "We leverage TF-Replicator to train on much larger batches than can fit on a single GPU, and find that this leads to sizable gains in sample quality."

In the realm of reinforcement learning, they trained a simulated "agent" of movable joints to navigate various tasks. "A single TPUv2 device (8 cores across 4 chips) provides competitive performance compared to 8 NVLink- connected Tesla V100 GPUs," they write.

There are some interesting implications for future design of neural networks from this kind of distributed computing. For instance, in the case of reinforcement learning, rather than constructing higher-level representations of the robot's joints and their "velocities," they write, "the scalability of TF-Replicator allows us to quickly solve these tasks purely from pixel observations."

"Massive scalability," write the authors, with hundreds and thousands of layers in a neural network, is going to be more and more important in deep learning. TF-Replicator is Google's answer to the question of how researchers can more rapidly develop and iterate those big networks, starting from their workbench laptop, and spreading to distributed systems, with the least hassle.

 [Best of MWC 2019: Cool tech you can buy or...](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/)  [SEE FULL GALLERY](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/)

 [![1tb-microsd-cnet.jpg](../_resources/9031291dc0d51816904d6b38e85f3a79.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/)

 [![blackberry-key2-red-cnet.jpg](../_resources/3401ccaf93a4181f2eca7a0aa122c2c9.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/2/)

 [![hololens-cnet.png](../_resources/1a465c3fac89eb1003d4c5bbb8a4f81e.png)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/3/)

 [![htc-5g-hub-cnet.jpg](../_resources/ff63eecfc2f2988d012ebf6c6d308d12.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/4/)

 [![huawei-mate-x-cnet.jpg](../_resources/7047aa006d41a06c1cf983d0ed466f36.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/5/)

 [![lg-g8-thinq-cnet.jpg](../_resources/d4fe3c753b442f1912c70e23a9d75d54.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/6/)

 [![lg-v50-thinq-cnet.jpg](../_resources/79999f937eb360fdaf5a6239ccd21f1e.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/7/)

 [![matebook-x-pro-2019-cnet.jpg](../_resources/a14e88d6191ac8ac699516af1a80d154.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/8/)

 [![nubia-alpha-aim-cnet.png](:/6f28ae414b110bbf8d9c751455321cc2)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/9/)

 [![nokia-210-cnet.jpg](../_resources/4d6cc62417d4b0f84d33fb9c88aa3253.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/10/)

 [![nokia-9-cnet.jpg](../_resources/83271c48977738c03e41c0ba405daf62.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/11/)

 [![samsung-galaxy-s10-cnet.jpg](../_resources/b081559679e947c841c91b03c6b26c2a.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/12/)

 [![samsung-galaxy-s10-5g-cnet.jpg](../_resources/74ac648efafb713006239c4ee7e296d9.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/13/)

 [![samsung-galaxy-fold-cnet.jpg](../_resources/b126063faca2046f3817aefb78d24bae.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/14/)

 [![sony-xperia-1-cnet.jpg](../_resources/7680be48f9a456b2e5be09501cb17274.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/15/)

 [![vivov15pro-cnet.jpg](../_resources/98ddd613116372f2243de5bbdbece3d3.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/16/)

 [![xiaomi-m9-cnet.jpg](../_resources/5d3fd8720b14d11670bb97d445373498.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/17/)

 [![xiaomi-mi-mix-3-cnet.jpg](../_resources/06f787f097c0a59bb85d980cf11b395a.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/18/)

 [![zte-axon-10-cnet.jpg](../_resources/a630547817b3bca9f8f9b72b4cd8e621.jpg)](https://www.zdnet.com/pictures/best-of-mwc-cool-tech-you-can-buy-or-pre-order/19/)

1 - 5 of 19

   [NEXT![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='caret js-evernote-checked' data-evernote-id='350'%3e%3cg%3e%3cpath d='M0.6%2c27.4c0.8%2c0.8%2c2%2c0.8%2c2.8%2c0l12-12c0.8-0.8%2c0.8-2%2c0-2.8l-12-12C3%2c0.2%2c2.5%2c0%2c2%2c0C1.5%2c0%2c1%2c0.2%2c0.6%2c0.6 c-0.8%2c0.8-0.8%2c2%2c0%2c2.8L11.2%2c14L0.6%2c24.6C-0.2%2c25.4-0.2%2c26.6%2c0.6%2c27.4z'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()

###  Previous and related coverage:

[**What is AI? Everything you need to know**](https://www.zdnet.com/article/what-is-ai-everything-you-need-to-know-about-artificial-intelligence/)

An executive guide to artificial intelligence, from machine learning and general AI to neural networks.

[**What is deep learning? Everything you need to know**](https://www.zdnet.com/article/what-is-deep-learning-everything-you-need-to-know/)

The lowdown on deep learning: from how it relates to the wider field of machine learning through to how to get started with it.

[**What is machine learning? Everything you need to know**](https://www.zdnet.com/article/what-is-machine-learning-everything-you-need-to-know/)

This guide explains what machine learning is, how it is related to artificial intelligence, how it works and why it matters.

[**What is cloud computing? Everything you need to know about**](https://www.zdnet.com/article/what-is-cloud-computing-everything-you-need-to-know-from-public-and-private-cloud-to-software-as-a/)

An introduction to cloud computing right from the basics up to IaaS and PaaS, hybrid, public, and private cloud.

###  Related stories:

- [Google's AI surfs the "gamescape" to conquer game theory](https://www.zdnet.com/article/googles-ai-surfs-the-gamescape-to-conquer-game-theory/)
- [This is what AI looks like (as sketched by AI) ](https://www.zdnet.com/article/this-is-what-ai-looks-like-as-sketched-by-ai/)
- [Google's DeepMind teams with leading 3D game dev platform](https://www.zdnet.com/article/googles-deepmind-teams-with-leading-3d-game-dev-platform-unity/)
- [DeepMind's AI spots early signs of eye disease ](https://www.zdnet.com/article/deepminds-ai-spots-early-signs-of-eye-disease/)

### Related Topics:

 [Big Data Analytics](https://www.zdnet.com/topic/big-data/)  [Digital Transformation](https://www.zdnet.com/topic/digital-transformation/)  [CXO](https://www.zdnet.com/topic/cxo/)  [Internet of Things](https://www.zdnet.com/topic/internet-of-things/)  [Innovation](https://www.zdnet.com/topic/innovation/)  [Enterprise Software](https://www.zdnet.com/topic/enterprise-software/)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='comment-bubble js-evernote-checked' data-evernote-id='352'%3e%3c/svg%3e)0](https://www.zdnet.com/article/googles-distributed-computing-for-dummies-trains-restnet-50-in-half-an-hour/#comments-ab5fdc66-90de-468e-a346-c46e60570988)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='facebook js-evernote-checked' data-evernote-id='353'%3e%3c/svg%3e)]()

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='linkedin js-evernote-checked' data-evernote-id='354'%3e%3c/svg%3e)]()

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='twitter js-evernote-checked' data-evernote-id='355'%3e%3c/svg%3e)]()

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='envelope js-evernote-checked' data-evernote-id='356'%3e%3c/svg%3e)]()

[by Taboola](https://popup.taboola.com/en/?template=colorbox&utm_source=cbsinteractive-zdnet&utm_medium=referral&utm_content=alternating-thumbnails-a:ZDNETarticleDesktop/Tablet-Below%20Article%20Thumbnails:)

[Sponsored Links](https://popup.taboola.com/en/?template=colorbox&utm_source=cbsinteractive-zdnet&utm_medium=referral&utm_content=alternating-thumbnails-a:ZDNETarticleDesktop/Tablet-Below%20Article%20Thumbnails:)

Recommended For You

[(L)](https://assetbackedinvestments.com/?utm_source=taboola&utm_medium=Old)[£10,000 Minimum Investment, Fully Insured Fixed Rate BondAsset Backed Investments](https://assetbackedinvestments.com/?utm_source=taboola&utm_medium=Old)

Undo

[(L)](http://comparehearingaids.org/news/?code=NATO&utm_source=Taboola&utm_medium=Native&utm_campaign=Taboola&utm_term=cbsinteractive-zdnet)[Camden: Don't Book Your Hearing Test Until You Read ThisCompare Hearing Aids](http://comparehearingaids.org/news/?code=NATO&utm_source=Taboola&utm_medium=Native&utm_campaign=Taboola&utm_term=cbsinteractive-zdnet)

Undo

[(L)](https://responsiblelife.co.uk/rms/lifetime-mortgage.php?source=TB&medium=RMS-LM&term=rms-rll-native-desktop-myths&utm_source=taboola&utm_medium=referral&utm_campaign=1921874)[Married & Over 69? Don't Fall For The Equity Release MythsRetirement Mortgage Service](https://responsiblelife.co.uk/rms/lifetime-mortgage.php?source=TB&medium=RMS-LM&term=rms-rll-native-desktop-myths&utm_source=taboola&utm_medium=referral&utm_campaign=1921874)

Undo

[(L)](http://digitalcrab.co.uk/?c=4608&a=929&s3=CjBhMzQ0NTNlZS0yMjlhLTQwNjEtOTlmNy0xOGM1MmYwMzA5MzgtdHVjdDE3NDY0NzISHGRpZ2l0YWxveXN0ZXItcG9tZnVuZXJhbHMtc2M&s2=5b376f%7Ccbsinteractive-zdnet&s1=TB_POM_TABLET_4-SB)[Incredible Funeral Plan Sweeps CamdenMoney Advice Club](http://digitalcrab.co.uk/?c=4608&a=929&s3=CjBhMzQ0NTNlZS0yMjlhLTQwNjEtOTlmNy0xOGM1MmYwMzA5MzgtdHVjdDE3NDY0NzISHGRpZ2l0YWxveXN0ZXItcG9tZnVuZXJhbHMtc2M&s2=5b376f%7Ccbsinteractive-zdnet&s1=TB_POM_TABLET_4-SB)

Undo

[(L)](https://marktexpert.com/uk-pure-eco-spa?utm_source=taboola&utm_medium=referral&utm_campaign=taboola_uk_desk_pes3&utm_site=cbsinteractive-zdnet&utm_siteid=1039694&utm_thumbnail=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F032eb0d3d15670945dad7979edd90060.png&utm_title=Thousands+of+Brits+Are+Switching+To+This+New+Shower+Head)[Thousands of Brits Are Switching To This New Shower HeadMarktexpert](https://marktexpert.com/uk-pure-eco-spa?utm_source=taboola&utm_medium=referral&utm_campaign=taboola_uk_desk_pes3&utm_site=cbsinteractive-zdnet&utm_siteid=1039694&utm_thumbnail=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F032eb0d3d15670945dad7979edd90060.png&utm_title=Thousands+of+Brits+Are+Switching+To+This+New+Shower+Head)

Undo

[(L)](https://www.insiderlifestyles.com/breaking-uks-biggest-jackpot-of-megamillionsgbp-set-for-dayoftheweekuppermm-mm-evergreen-v1-98p-holiday-uk/?oid=NativeMMSuper98&utm_source=taboolaUK&utm_campaign=UK-MM-Tonight-D-V1-98p-B&W-1779290&utm_medium=cbsinteractive-zdnet&utm_term=Breaking%3A+Tonight%27s+%C2%A3401m*+Mega+Jackpot+Sends+UK+Into+Lottery+Betting+Frenzy)[Breaking: Tonight's £401m* Mega Jackpot Sends UK Into Lottery Betting FrenzyLotto Go](https://www.insiderlifestyles.com/breaking-uks-biggest-jackpot-of-megamillionsgbp-set-for-dayoftheweekuppermm-mm-evergreen-v1-98p-holiday-uk/?oid=NativeMMSuper98&utm_source=taboolaUK&utm_campaign=UK-MM-Tonight-D-V1-98p-B&W-1779290&utm_medium=cbsinteractive-zdnet&utm_term=Breaking%3A+Tonight%27s+%C2%A3401m*+Mega+Jackpot+Sends+UK+Into+Lottery+Betting+Frenzy)

Undo

[(L)](https://go.babbel.com/engmag-a1059-15minperday-cd-gbr-tb/1_gbr_tab_cd?utm_source=Taboola&utm_medium=CON&utm_campaign=CD_GBRALL_gEN_cUK_15MinPerDay&utm_term=cbsinteractive-zdnet)[Language expert tells the secret to learning a language in 15 mins a dayBabbel](https://go.babbel.com/engmag-a1059-15minperday-cd-gbr-tb/1_gbr_tab_cd?utm_source=Taboola&utm_medium=CON&utm_campaign=CD_GBRALL_gEN_cUK_15MinPerDay&utm_term=cbsinteractive-zdnet)

Undo

[(L)](https://otty.com/products/the-otty-hybrid-mattress?variant=7683067609139&utm_source=taboola&utm_medium=referral)[The £450 Mattress That The UK Is LovingThe Otty Mattress](https://otty.com/products/the-otty-hybrid-mattress?variant=7683067609139&utm_source=taboola&utm_medium=referral)

Undo

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='comment-bubble js-evernote-checked' data-evernote-id='357'%3e%3c/svg%3e)Show Comments](https://www.zdnet.com/article/googles-distributed-computing-for-dummies-trains-restnet-50-in-half-an-hour/#comments-ab5fdc66-90de-468e-a346-c46e60570988)

## More from Tiernan Ray

- [ ![screen-shot-2019-03-07-at-2-29-22-pm.png](../_resources/e2216f898f65755991000cc74ab55e6a.png)](https://www.zdnet.com/article/startup-clari-pushes-speed-and-scale-of-ai-to-tie-enterprise-data-together/)

Artificial Intelligence

[Startup Clari pushes ‘speed and scale’ of AI to tie enterprise data together](https://www.zdnet.com/article/startup-clari-pushes-speed-and-scale-of-ai-to-tie-enterprise-data-together/)

- [ ![openai-neuro-mmo-game-grid.png](../_resources/43d8cb06c1011fb8f795e72928e6f13e.png)](https://www.zdnet.com/article/battle-of-the-ai-agents-atari-versus-mmorpg/)

Artificial Intelligence

[Battle of the AI Agents: Atari Versus MMORPG](https://www.zdnet.com/article/battle-of-the-ai-agents-atari-versus-mmorpg/)

- [ ![berkeley-online-meta-learning-tasks-feb-2019.png](../_resources/da8865bf8c81bb9320106e32e3e700aa.png)](https://www.zdnet.com/article/a-berkeley-mash-up-of-ai-approaches-promises-continuous-learning/)

Artificial Intelligence

[A Berkeley mash-up of AI approaches promises continuous learning](https://www.zdnet.com/article/a-berkeley-mash-up-of-ai-approaches-promises-continuous-learning/)

- [ ![leaf-neural-net-assembly-feb-2019.png](../_resources/f10dca70089bd6dcf12f8432346142b8.png)](https://www.zdnet.com/article/cognizant-tech-explores-the-evolution-of-ai/)

Artificial Intelligence

[IT leader Cognizant evolves AI beyond 'hill climbing'](https://www.zdnet.com/article/cognizant-tech-explores-the-evolution-of-ai/)

## Newsletters

   **ZDNet Announce UK** ZDNet's Announcements newsletter offers a mix of stories, special offers and members-only benefits.

   [ SeeAll](https://www.zdnet.com/newsletters/)

## More Resources

- [IBM's Db2 in a Multi-Cloud World - The Data Layer](https://leadgen-cbslnk.cnet.com/redir?edition=en&ursuid=&devicetype=desktop&pagetype=article&assettitle=google%27s+distributed+computing+for+dummies+trains+resnet-50+in+under+half+an+hour&assettype=content_article&topicguid=&viewguid=245bce8f-ff29-44f0-aeb1-260dc59c1ece&docid=33166079&promo=2150&ftag_cd=LGN22ef1e6&spotname=right-rail&destUrl=https%3A%2F%2Fwww.techrepublic.com%2Fresource-library%2Fwhitepapers%2Fibm-s-db2-in-a-multi-cloud-world-the-data-layer%2F%3Fpromo%3D2150%26ftag%3DLGN22ef1e6%26cval%3Dright-rail%26source%3Dzdnet&ctag=medc-right-rail&siteId=2&rsid=cnetzdnetglobalsite&sl=en&sc=uk&assetguid=ab5fdc66-90de-468e-a346-c46e60570988&q=&cval=33166079;2150&ttag=&bhid=)

###   Webcasts from   [IBM](https://www.techrepublic.com/resource-library/company/ibm/)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='play_alt js-evernote-checked' data-evernote-id='358'%3e %3cg%3e%3cpath d='M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2 7v10l7-5-7-5z'%3e%3c/path%3e%3c/g%3e %3c/svg%3e)Watch Now](https://leadgen-cbslnk.cnet.com/redir?edition=en&ursuid=&devicetype=desktop&pagetype=article&assettitle=google%27s+distributed+computing+for+dummies+trains+resnet-50+in+under+half+an+hour&assettype=content_article&topicguid=&viewguid=245bce8f-ff29-44f0-aeb1-260dc59c1ece&docid=33166079&promo=2150&ftag_cd=LGN22ef1e6&spotname=right-rail&destUrl=https%3A%2F%2Fwww.techrepublic.com%2Fresource-library%2Fwhitepapers%2Fibm-s-db2-in-a-multi-cloud-world-the-data-layer%2F%3Fpromo%3D2150%26ftag%3DLGN22ef1e6%26cval%3Dright-rail%26source%3Dzdnet&ctag=medc-right-rail&siteId=2&rsid=cnetzdnetglobalsite&sl=en&sc=uk&assetguid=ab5fdc66-90de-468e-a346-c46e60570988&q=&cval=33166079;2150&ttag=&bhid=)

- [Webcast: IBM's Db2 in a Multi-Cloud World - The Data Layer](https://leadgen-cbslnk.cnet.com/redir?edition=en&ursuid=&devicetype=desktop&pagetype=article&assettitle=google%27s+distributed+computing+for+dummies+trains+resnet-50+in+under+half+an+hour&assettype=content_article&topicguid=&viewguid=245bce8f-ff29-44f0-aeb1-260dc59c1ece&docid=33166080&promo=2150&ftag_cd=LGN22ef1e6&spotname=right-rail&destUrl=https%3A%2F%2Fwww.techrepublic.com%2Fresource-library%2Fwhitepapers%2Fwebcast-ibm-s-db2-in-a-multi-cloud-world-the-data-layer%2F%3Fpromo%3D2150%26ftag%3DLGN22ef1e6%26cval%3Dright-rail%26source%3Dzdnet&ctag=medc-right-rail&siteId=2&rsid=cnetzdnetglobalsite&sl=en&sc=uk&assetguid=ab5fdc66-90de-468e-a346-c46e60570988&q=&cval=33166080;2150&ttag=&bhid=)

###   Webcasts from   [IBM](https://www.techrepublic.com/resource-library/company/ibm/)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='play_alt js-evernote-checked' data-evernote-id='359'%3e %3c/svg%3e)Watch Now](https://leadgen-cbslnk.cnet.com/redir?edition=en&ursuid=&devicetype=desktop&pagetype=article&assettitle=google%27s+distributed+computing+for+dummies+trains+resnet-50+in+under+half+an+hour&assettype=content_article&topicguid=&viewguid=245bce8f-ff29-44f0-aeb1-260dc59c1ece&docid=33166080&promo=2150&ftag_cd=LGN22ef1e6&spotname=right-rail&destUrl=https%3A%2F%2Fwww.techrepublic.com%2Fresource-library%2Fwhitepapers%2Fwebcast-ibm-s-db2-in-a-multi-cloud-world-the-data-layer%2F%3Fpromo%3D2150%26ftag%3DLGN22ef1e6%26cval%3Dright-rail%26source%3Dzdnet&ctag=medc-right-rail&siteId=2&rsid=cnetzdnetglobalsite&sl=en&sc=uk&assetguid=ab5fdc66-90de-468e-a346-c46e60570988&q=&cval=33166080;2150&ttag=&bhid=)

- [NetScout: How to Analyze and Reduce the Risk of DDoS Attacks](https://leadgen-cbslnk.cnet.com/redir?edition=en&ursuid=&devicetype=desktop&pagetype=article&assettitle=google%27s+distributed+computing+for+dummies+trains+resnet-50+in+under+half+an+hour&assettype=content_article&topicguid=&viewguid=245bce8f-ff29-44f0-aeb1-260dc59c1ece&docid=33165724&promo=2150&ftag_cd=LGN22ef1e6&spotname=right-rail&destUrl=https%3A%2F%2Fwww.techrepublic.com%2Fresource-library%2Fwhitepapers%2Fnetscout-how-to-analyze-and-reduce-the-risk-of-ddos-attacks%2F%3Fpromo%3D2150%26ftag%3DLGN22ef1e6%26cval%3Dright-rail%26source%3Dzdnet&ctag=medc-right-rail&siteId=2&rsid=cnetzdnetglobalsite&sl=en&sc=uk&assetguid=ab5fdc66-90de-468e-a346-c46e60570988&q=&cval=33165724;2150&ttag=&bhid=)

###   White Papers from   [NetScout Systems](https://www.techrepublic.com/resource-library/company/netscout-systems/)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='paperclip js-evernote-checked' data-evernote-id='360'%3e %3cg%3e%3cpath d='M21.586 10.461l-10.05 10.075c-1.95 1.949-5.122 1.949-7.071 0s-1.95-5.122 0-7.072l10.628-10.585c1.17-1.17 3.073-1.17 4.243 0 1.169 1.17 1.17 3.072 0 4.242l-8.507 8.464c-.39.39-1.024.39-1.414 0s-.39-1.024 0-1.414l7.093-7.05-1.415-1.414-7.093 7.049c-1.172 1.172-1.171 3.073 0 4.244s3.071 1.171 4.242 0l8.507-8.464c.977-.977 1.464-2.256 1.464-3.536 0-2.769-2.246-4.999-5-4.999-1.28 0-2.559.488-3.536 1.465l-10.627 10.583c-1.366 1.368-2.05 3.159-2.05 4.951 0 3.863 3.13 7 7 7 1.792 0 3.583-.684 4.95-2.05l10.05-10.075-1.414-1.414z'%3e%3c/path%3e%3c/g%3e %3c/svg%3e)Read Now](https://leadgen-cbslnk.cnet.com/redir?edition=en&ursuid=&devicetype=desktop&pagetype=article&assettitle=google%27s+distributed+computing+for+dummies+trains+resnet-50+in+under+half+an+hour&assettype=content_article&topicguid=&viewguid=245bce8f-ff29-44f0-aeb1-260dc59c1ece&docid=33165724&promo=2150&ftag_cd=LGN22ef1e6&spotname=right-rail&destUrl=https%3A%2F%2Fwww.techrepublic.com%2Fresource-library%2Fwhitepapers%2Fnetscout-how-to-analyze-and-reduce-the-risk-of-ddos-attacks%2F%3Fpromo%3D2150%26ftag%3DLGN22ef1e6%26cval%3Dright-rail%26source%3Dzdnet&ctag=medc-right-rail&siteId=2&rsid=cnetzdnetglobalsite&sl=en&sc=uk&assetguid=ab5fdc66-90de-468e-a346-c46e60570988&q=&cval=33165724;2150&ttag=&bhid=)

## Related Stories

- ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 28' data-evernote-id='361' class='js-evernote-checked'%3e%3cg%3e%3cpath d='M0.6%2c27.4c0.8%2c0.8%2c2%2c0.8%2c2.8%2c0l12-12c0.8-0.8%2c0.8-2%2c0-2.8l-12-12C3%2c0.2%2c2.5%2c0%2c2%2c0C1.5%2c0%2c1%2c0.2%2c0.6%2c0.6 c-0.8%2c0.8-0.8%2c2%2c0%2c2.8L11.2%2c14L0.6%2c24.6C-0.2%2c25.4-0.2%2c26.6%2c0.6%2c27.4z'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)

1of3

- ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 28' data-evernote-id='362' class='js-evernote-checked'%3e%3cg%3e%3cpath d='M0.6%2c27.4c0.8%2c0.8%2c2%2c0.8%2c2.8%2c0l12-12c0.8-0.8%2c0.8-2%2c0-2.8l-12-12C3%2c0.2%2c2.5%2c0%2c2%2c0C1.5%2c0%2c1%2c0.2%2c0.6%2c0.6 c-0.8%2c0.8-0.8%2c2%2c0%2c2.8L11.2%2c14L0.6%2c24.6C-0.2%2c25.4-0.2%2c26.6%2c0.6%2c27.4z'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)
- [ ![istock-1035921538survey.jpg](../_resources/8f3c0c41b3d624829f7f765117f07b61.jpg)](https://www.zdnet.com/article/survey-managing-ai-and-ml-in-the-enterprise/)

[​Survey: Managing AI and ML in the enterprise](https://www.zdnet.com/article/survey-managing-ai-and-ml-in-the-enterprise/)

Take this short, multiple choice survey and tell us how your company's managing its AI/ML plans.

- [ ![screen-shot-2019-03-12-at-3-17-54-pm.png](../_resources/d28fe1c913f256446010dff1deb12ff2.png)](https://www.zdnet.com/article/transcription-service-otter-launches-enterprise-app-for-teams/)

[Transcription service Otter launches enterprise app for teams](https://www.zdnet.com/article/transcription-service-otter-launches-enterprise-app-for-teams/)

The Otter app uses AI and machine learning to render accurate transcripts that identify speakers, suggest keywords, and allow keyword searching.

- [ ![artificial-intelligence.jpg](../_resources/bacd0746c7987c78b6df6f959c66ccee.jpg)](https://www.zdnet.com/article/automl-democratizing-and-improving-ai/)

[AutoML is democratizing and improving AI](https://www.zdnet.com/article/automl-democratizing-and-improving-ai/)

Once a niche technology, Automated Machine learning (AutoML) is now a thing. Helping non-data scientists do simple AI, and helping trained data scientists do complex work ever-faster, ...

- [ ![nvidia-mellanox-2.png](../_resources/b7224200232fec93d18fc811da58c3e6.png)](https://www.zdnet.com/article/nvidias-purchase-of-mellanox-turns-up-heat-on-intel-rivalry-data-center-ambitions/)

[Nvidia's purchase of Mellanox turns up heat on Intel rivalry, data center ambitions](https://www.zdnet.com/article/nvidias-purchase-of-mellanox-turns-up-heat-on-intel-rivalry-data-center-ambitions/)

Nvidia's $6.9 billion purchase of Mellanox highlights the company's bet that next-gen data center architecture will revolve around data and artificial intelligence. ...

- [ ![lg-uplus-5g-autonomous.jpg](../_resources/b86408a61fb42b581b3e3a700572377e.jpg)](https://www.zdnet.com/article/lg-uplus-hanyang-successfully-trails-5g-autonomous-car-in-seoul/)

[LG Uplus and Hanyang successfully trial 5G autonomous car in Seoul](https://www.zdnet.com/article/lg-uplus-hanyang-successfully-trails-5g-autonomous-car-in-seoul/)

South Korean telco LG Uplus and Hanyang University successfully tested their 5G-connected autonomous vehicle on the streets of Seoul.

- [ ![istock-811236334.jpg](../_resources/319cd4cc7f3bfbedfa3969b19f64b1e0.jpg)](https://www.zdnet.com/article/asx-listed-appen-to-spend-around-au340m-on-ai-startup-figure-eight/)

[ASX-listed Appen to spend around AU$340m on AI startup Figure Eight](https://www.zdnet.com/article/asx-listed-appen-to-spend-around-au340m-on-ai-startup-figure-eight/)

Appen will issue new shares to raise AU$285 million to fund the majority of the Figure Eight Technologies acquisition.

- [ ![google-home-hub.jpg](../_resources/baa540723d0ac1c922cf1c5cf110310f.jpg)](https://www.zdnet.com/article/google-brings-assistants-continued-conversation-feature-to-smart-displays/)

[Google brings Assistant's "continued conversation" feature to smart displays](https://www.zdnet.com/article/google-brings-assistants-continued-conversation-feature-to-smart-displays/)

The feature lets users engage in a conversation with the voice-activated assistant without prefacing each statement with "Hey Google."

- [ ![2019-03-08-07-48-23.jpg](../_resources/a4b69831d122b064eacd5f500d8531be.jpg)](https://www.zdnet.com/article/scaleway-launches-eur1-per-hour-cloud-nvidia-tesla-p100-gpu-instances/)

[Scaleway launches €1 per hour cloud Nvidia Tesla P100 GPU instances](https://www.zdnet.com/article/scaleway-launches-eur1-per-hour-cloud-nvidia-tesla-p100-gpu-instances/)

Need access to high-performance cloud-based GPU instances? Scaleway is offering access to Nvidia Tesla P100 GPUs at a highly competitive price.

- [ ![screen-shot-2019-03-07-at-2-29-22-pm.png](../_resources/b80d15df140fb639eef7553c8f0b45b8.png)](https://www.zdnet.com/article/startup-clari-pushes-speed-and-scale-of-ai-to-tie-enterprise-data-together/)

[Startup Clari pushes ‘speed and scale’ of AI to tie enterprise data together](https://www.zdnet.com/article/startup-clari-pushes-speed-and-scale-of-ai-to-tie-enterprise-data-together/)

Enterprise software startup Clari builds models of business deals using machine learning to enhance the pursuit of revenue. The company is extending its reach to more and more systems ...