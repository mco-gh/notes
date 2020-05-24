The Illustrated Self-Supervised Learning

# [The Illustrated Self-Supervised Learning](https://amitness.com/2020/02/illustrated-self-supervised-learning/)

Published February 25, 2020in illustration

Yann Lecun, in his [talk](https://www.youtube.com/watch?v=7I0Qt7GALVk&t=2639s), introduced the “cake analogy” to illustrate the importance of self-supervised learning. Though the analogy is debated([ref: Deep Learning for Robotics(Slide 96), Pieter Abbeel](https://orfe.princeton.edu/~alaink/SmartDrivingCars/PDFs/2017_12_xx_NIPS-keynote-final.pdf)), we have seen the impact of self-supervised learning in the Natural Language Processing field where recent developments (Word2Vec, Glove, ELMO, BERT) have embraced self-supervision and achieved state of the art results.

> “If intelligence is a cake, the bulk of the cake is self-supervised learning, the icing on the cake is supervised learning, and the cherry on the cake is reinforcement learning (> RL> ).”

Curious to know how self-supervised learning has been applied in the computer vision field, I read up on existing literature on self-supervised learning applied to computer vision through a [recent survey paper](https://arxiv.org/abs/1902.06162) by Jing et. al.

This post is my attempt to provide an intuitive visual summary of the patterns of problem formulation in self-supervised learning.

# The Key Idea

To apply supervised learning, we need enough labeled data. To acquire that, human annotators manually label data(images/text) which is both a time consuming and expensive process. There are also fields such as the medical field where getting enough data is a challenge itself.

![](../_resources/b0b4de4703f6de972c67c7e6e5ae0f0e.png)

This is where self-supervised learning comes into play. It poses the following question to solve this:

> Can we design the task in such a way that we can generate virtually unlimited labels from our existing images and use that to learn the representations?

![](../_resources/84683057a235f5cccc1528bd38c3e99c.png)

We replace the human annotation block by creatively exploiting some property of data to set up a supervised task. For example, here instead of labeling images as cat/dog, we could instead rotate them by 0/90/180/270 degrees and train a model to predict rotation. We can generate virtually unlimited training data from millions of images we have freely available.![](../_resources/b3fdf588612f5a0656aab85eab8be307.png)

# Existing Creative Approaches

Below is a list of approaches various researchers have proposed to exploit image and video properties and learn representation in a self-supervised manner.

# Learning from Images

## 1. **Image Colorization**

Formulation:

> What if we prepared pairs of (grayscale, colorized) images by applying grayscale to millions of images we have freely available?

![](../_resources/567988bb66a06ddcf9739045b0e4dbd1.png)

We could use an encoder-decoder architecture based on a fully convolutional neural network and compute the L2 loss between the predicted and actual color images.

![](../_resources/73c783b7b06c53b1aed709b3cce08787.png)

To solve this task, the model has to learn about different objects present in the image and related parts so that it can paint those parts in the same color. Thus, representations learned are useful for downstream tasks.![](../_resources/04ff82e9c7febeb7cd12567273b7fb07.png)

**Papers:**

[Colorful Image Colorization](https://arxiv.org/abs/1603.08511) | [Real-Time User-Guided Image Colorization with Learned Deep Priors](https://arxiv.org/abs/1705.02999) | [Let there be Color!: Joint End-to-end Learning of Global and Local Image Priors for Automatic Image Colorization with Simultaneous Classification](http://iizuka.cs.tsukuba.ac.jp/projects/colorization/en/)

## 2. **Image Superresolution**

Formulation:

> What if we prepared training pairs of (small, upscaled) images by downsampling millions of images we have freely available?

![](../_resources/ac0449d5e190a57c93606efbea7715d4.png)

GAN based models such as [SRGAN](https://arxiv.org/abs/1609.04802) are popular for this task. A generator takes a low-resolution image and outputs a high-resolution image using a fully convolutional network. The actual and generated images are compared using both mean-squared-error and content loss to imitate human-like quality comparison. A binary-classification discriminator takes an image and classifies whether it’s an actual high-resolution image(1) or a fake generated superresolution image(0). This interplay between the two models leads to generator learning to produce images with fine details.![](../_resources/18c66fef58b67673410998903688be4d.png)

Both generator and discriminator learn semantic features that can be used for downstream tasks.

**Papers**:

[Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802)

## 3. **Image Inpainting**

Formulation:

> What if we prepared training pairs of (corrupted, fixed) images by randomly removing part of images?

![](../_resources/f912d8e6298f85f297fdcb2a0785c2aa.png)

Similar to superresolution, we can leverage a GAN-based architecture where the Generator can learn to reconstruct the image while discriminator separates real and generated images.![](../_resources/51ef4b43a18e0d0e4ca05486bc7fe457.png)

For downstream tasks, [Pathak et al.](https://arxiv.org/abs/1604.07379) have shown that semantic features learned by such a generator give 10.2% improvement over random initialization on the [PASCAL  VOC 2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html) semantic segmentation challenge while giving <4% improvements over classification and object detection.

**Papers**:

[Context encoders: Feature learning by inpainting](https://arxiv.org/abs/1604.07379)

## 4. **Image Jigsaw Puzzle**

Formulation:

> What if we prepared training pairs of (shuffled, ordered) puzzles by randomly shuffling patches of images?

![](../_resources/75969798182217c617c8a6a0e190fd0a.png)

Even with only 9 patches, there can be 362880 possible puzzles. To overcome this, only a subset of possible permutations is used such as 64 permutations with the highest hamming distance.![](../_resources/2ae4de675c409af6ccecf746a803b69e.png)

Suppose we use a permutation that changes the image as shown below. Let’s use the permutation number 64 from our total available 64 permutations.![](../_resources/11ac86119255d966762ce5ae6ac0d274.png)

Now, to recover back the original patches, [Noroozi et al.](https://arxiv.org/abs/1603.09246)proposed a neural network called context-free network (CFN) as shown below. Here, the individual patches are passed through the same siamese convolutional layers that have shared weights. Then, the features are combined in a fully-connected layer. In the output, the model has to predict which permutation was used from the 64 possible classes. If we know the permutation, we can solve the puzzle.![](../_resources/ee69992fc7e3503e7f7df05bd4d9140f.png)

To solve the Jigsaw puzzle, the model needs to learn to identify how parts are assembled in an object, relative positions of different parts of objects and shape of objects. Thus, the representations are useful for downstream tasks in classification and detection.

**Papers**:

[Unsupervised learning of visual representations by solving jigsaw puzzles](https://arxiv.org/abs/1603.09246)

## 5. **Context Prediction**

Formulation:

> What if we prepared training pairs of (image-patch, neighbor) by randomly taking an image patch and one of its neighbors around it from large, unlabeled image collection?

![](../_resources/3fbca2f33e41ce75e2649268e58a02ac.png)

To solve this pre-text task, [Doersch et al.](https://arxiv.org/abs/1505.05192) used an architecture similar to that of a jigsaw puzzle. We pass the patches through two siamese ConvNets to extract features, concatenate the features and do a classification over 8 classes denoting the 8 possible neighbor positions.![](../_resources/9edce78ca731a8d93b68b18a1d7bd405.png)

**Papers**:

[Unsupervised Visual Representation Learning by Context Prediction](https://arxiv.org/abs/1505.05192)

## 6. **Geometric Transformation Recognition**

Formulation:

> What if we prepared training pairs of (rotated-image, rotation-angle) by randomly rotating images by (0, 90, 180, 270) from large, unlabeled image collection?

![](../_resources/9f05467d1d4f3323714245b6ede8648b.png)

To solve this pre-text task, [Gidaris et al.](https://arxiv.org/abs/1505.05192) propose an architecture where a rotated image is passed through a ConvNet and the network has to classify it into 4 classes(0/90/270/360 degrees).![](../_resources/6c5db499c72d6a6123f03df00c9ea9b5.png)

Though a very simple idea, the model has to understand location, types and pose of objects in an image to solve this task and as such, the representations learned are useful for downstream tasks.

**Papers**:

[Unsupervised Representation Learning by Predicting Image Rotations](https://arxiv.org/abs/1803.07728)

## 7. **Image Clustering**

Formulation:

> What if we prepared training pairs of (image, cluster-number) by performing clustering on large, unlabeled image collection?

![](../_resources/e7100e80e4223275845be9436bfd445e.png)

To solve this pre-text task, [Caron et al.](https://arxiv.org/abs/1807.05520) propose an architecture called deep clustering. Here, the images are first clustered and the clusters are used as classes. The task of the ConvNet is to predict the cluster label for an input image.![](../_resources/b3662e9d6e729c0af9e1d83199df7e10.png)

**Papers**:

[Deep clustering for unsupervised learning of visual features](https://arxiv.org/abs/1807.05520)

## 8. **Synthetic Imagery**

Formulation:

> What if we prepared training pairs of (image, properties) by generating synthetic images using game engines and adapting it to real images?

![](../_resources/e7e09eeda01087212484c50e2ae36b4c.png)

To solve this pre-text task, [Ren et al.](https://arxiv.org/pdf/1711.09082.pdf) propose an architecture where weight-shared ConvNets are trained on both synthetic and real images and then a discriminator learns to classify whether ConvNet features fed to it is of a synthetic image or a real image. Due to adversarial nature, the shared representations between real and synthetic images get better.![](../_resources/7187ea868d804dd76fbe61f4a84c640c.png)

# Learning from Videos

## 1. **Frame Order Verification**

Formulation:

> What if we prepared training pairs of (video frames, correct/incorrect order) by shuffling frames from videos of objects in motion?

![](../_resources/1d53106fcc09be475f907c6f9471624a.png)

To solve this pre-text task, [Misra et al.](https://arxiv.org/pdf/1711.09082.pdf) propose an architecture where video frames are passed through weight-shared ConvNets and the model has to figure out whether the frames are in the correct order or not. In doing so, the model learns not just spatial features but also takes into account temporal features.![](../_resources/4423348f3d0de8265511ab7121163fbf.png)

**Papers**:

[Shuffle and Learn: Unsupervised Learning using Temporal Order Verification](https://arxiv.org/abs/1603.08561)

## References

- Jing, et al. “[Self-Supervised Visual Feature Learning with Deep Neural Networks: A Survey.](https://arxiv.org/abs/1902.06162)”

Share on:[Twitter](https://twitter.com/intent/tweet?text=The%20Illustrated%20Self-Supervised%C2%A0Learning&url=https%3A//amitness.com/2020/02/illustrated-self-supervised-learning/&via=amitness)|[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A//amitness.com/2020/02/illustrated-self-supervised-learning/)|[Email](https://amitness.com/2020/02/illustrated-self-supervised-learning/mailto:?subject=The%20Illustrated%20Self-Supervised%C2%A0Learning&body=https%3A//amitness.com/2020/02/illustrated-self-supervised-learning/)

- [3 comments]()
- [**Amit Chaudhary's Blog**](https://disqus.com/home/forums/amit-chaudharys-blog/)
- [** Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  2](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

[(L)](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)

[![avatar92.jpg](../_resources/9f774d20a8353c1f2fa4caa059903b18.jpg)](https://disqus.com/by/moneyhustle/)

 [MONEY HUSTLE](https://disqus.com/by/moneyhustle/)    •  [5 days ago](https://amitness.com/2020/02/illustrated-self-supervised-learning/#comment-4815775049)

Thank you! ❤⭐⭐⭐⭐⭐

-

    - [−](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Nick  •  [6 days ago](https://amitness.com/2020/02/illustrated-self-supervised-learning/#comment-4814495834)

Thanks for the overview. It's still unclear at the beginning with your dog/cat classification example. Once you get the network to predict the rotation, how do solve the downstream task of knowing if the image is a dog or a cat?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)

[![avatar92.jpg](../_resources/d4362c9eda5a407f1829938523bbd93c.jpg)](https://disqus.com/by/amitness/)

 [Amit Chaudhary](https://disqus.com/by/amitness/)  Author  [*>* Nick](https://amitness.com/2020/02/illustrated-self-supervised-learning/#comment-4814495834)  •  [3 days ago](https://amitness.com/2020/02/illustrated-self-supervised-learning/#comment-4817385542)

Hi Nick,

Once the model has learned representations from the rotation task, you can fine-tune it for the cat-dog classification. Compared to a randomly initialized model, fine-tuning the self-supervised model will get better performance in fewer epochs and reach better performance a lot faster.

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=amit-chaudharys-blog&t_i=2020%2F02%2Fillustrated-self-supervised-learning%2F&t_u=https%3A%2F%2Famitness.com%2F2020%2F02%2Fillustrated-self-supervised-learning%2F&t_d=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&t_t=%0AThe%20Illustrated%20Self-Supervised%C2%A0Learning&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=amit-chaudharys-blog&utm_medium=Disqus-Footer)
- [*⚠*Do Not Sell My Data](https://disqus.com/data-sharing-settings/)