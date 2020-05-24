Martin Görner on Twitter

1.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149749548471877632)

Great summer read: FCOS (Fully Convolutional One-Stage object detection)[https://arxiv.org/abs/1904.01355 ](https://t.co/KveoUWk15x)Simpler than the already simple RetinaNet architecture, with a couple of neat tricks. Pic below from paper, probably cherry-picked ![1f607.png](../_resources/e53e385a68363a25f1eccc9a6a6bb14b.png) but still impressive. Every orange is boxed.

 ![D_S6jolVUAAtigQ.png](../_resources/0b647e3d00d3992c2ef78bae8c26e331.png)

     4 replies          95 retweets          380 likes

2.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149760611519123457)

Neat trick #1: predicts a bounding box for every pixel directly. No more Anchor boxes, no more anchor box to ground truth pairing headaches. But, but, but, a single pixel can be in multiple bounding boxes. You canot predict a bounding box per pixel ?!? (see illust. from paper)

 ![D_TFHlOU8AAU7OU.png](../_resources/053655232483b5090d81c718db40ca04.png)

     1 reply          3 retweets          15 likes

3.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149761769969074176)

Neat trick #2: they specialize each level in the feature pyramid to predict only a given range of bounding box sizes. Now you can predict more than one box per pixel, as long as they have different sizes. Notice the five prediction heads in the architecture diagram from the paper

 ![D_TF0tjUEAElZkp.jpg](../_resources/3e5fd431bcd056d0d5284ad3b86c8c3e.jpg)

     1 reply          1 retweet          13 likes

4.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149762795228954624)

Neat trick #3: in addition to the boxes and classification score, there is an additional head predicting how close a pixel is to the center of an object.

 ![D_THG5pU4AEI4Wl.png](../_resources/3a557d44786d71c86dab95caf463e8ae.png)

     1 reply          1 retweet          12 likes

5.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149763504452198402)

This "center-ness" score is multiplied with the classification score in the loss to down-weight the usually low-quality predictions from pixels on the periphery of an object. The effect is clearly visible on this graph representing...

 ![D_THwTxUYAAZnpj.jpg](../_resources/c31e1d74d1be96c75d5fec5b57b6ba09.jpg)

     2 replies          2 retweets          6 likes

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)

A couple more pics from the paper (100% precision and recall on all pics, no cherry-picking, guaranteed ![1f643.png](../_resources/3f78478e42a277e1a57abeb0f1d36cb4.png)). Jokes aside, this is great.

 ![D_TJg8HUIAE8i8h.png](../_resources/3213cb2a84e64ec172bc561106bcc98b.png)

 ![D_TJiG9UYAAoeLC.png](../_resources/a73282c6e55ac1829b249b0f286f8bcc.png)

 ![D_TJi-cUEAUpZ5w.png](../_resources/e7c653faf8a87af9573edb2b910bbada.png)

 ![D_TJj42UEAELbGB.png](../_resources/7e2eb4e499fcfdc915284d513b2efdf9.png)

   12:43 PM - 12 Jul 2019

- [**16** Likes]()

- [![_ms7xAJA_normal.jpg](../_resources/b87012a910a3c2c366e57792a6303421.jpg)](https://twitter.com/guerwan)  [![CYfkUeUu_normal.jpg](../_resources/cf2be97138650c127eaba4ae98c26bca.jpg)](https://twitter.com/NicoChauvin74)  [![3303eaa6ced81f16b09a0f167468fb13_normal.jpeg](../_resources/7cfa9183acdf6026fd93ac83ff3db484.jpg)](https://twitter.com/imoracle)  [![BtxHWAVr_normal.jpg](../_resources/374550c40cd582092b119571df52c9d6.jpg)](https://twitter.com/AtlasMachiavel1)  [![_D3KeiRx_normal.jpg](../_resources/0f7416a719f6aadbb759b454c786e1d7.jpg)](https://twitter.com/evyborov)  [![usYWrHvB_normal.jpg](../_resources/e578cc0c0f397b62edcce4345491f1a9.jpg)](https://twitter.com/Rajesh23MD)  [![8GFC2IZI_normal.jpg](../_resources/ad89922756524109c79738244d4a503d.jpg)](https://twitter.com/Alex_da_Cunha)  [![IKJxLULJ_normal.jpg](../_resources/70d02efbc61e3e7b477201bfeacad10f.jpg)](https://twitter.com/Just_curiousPM)

     3 replies          0 retweets          16 likes

 ![mirror_normal.jpg](../_resources/a57789cc4b587ff517bf3cb07c9dd8d6.jpg)  Tweet text

Tweet your reply

1.
   New conversation
    1.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149768850184916992)

Quote from paper: "ResNet-50 is used as our backbone and the same hyper-parameters [as for] RetinaNet are used. [...] We argue that the performance of our detector can be improved further if the hyper-parameters are optimized for it." This was without hyper-parameter tuning ???

     4 replies          1 retweet          11 likes

    2.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149770799982583808)

Please grab a TPU pod and start hp-tuning! I am training a resnet50-based Retinanet in 20 min on a 128-core TPU-pod. With 20-min runs as well as multiple parallel runs on GCP's AI platform, there is a lot tuning that can be done. Disclosure: as most people know, I work for Google

     0 replies          0 retweets          9 likes

 End of conversation

2.
   New conversation
    1.

 [![wDWboVIN_bigger.jpg](../_resources/a786996fda8a1a905096a32b1201389e.jpg)    **Karanbir Chahal**‏ @**karanchahal96**](https://twitter.com/karanchahal96)  ·  [Jul 12](https://twitter.com/karanchahal96/status/1149788555310485506)

Replying to [@**martin_gorner**](https://twitter.com/martin_gorner)

This makes me really excited, do you have open source code for this ?

     1 reply          0 retweets          0 likes

    2.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149791544410402816)

Yes, the paper has a link.

     0 replies          0 retweets          0 likes

 End of conversation

3.
   New conversation
    1.

 [![yEoXyn5d_bigger.jpg](../_resources/81ddf4a4346006b2a5edd06d2848531b.jpg)    **Srishti  ‍**‏ @**_srishtiyadav**](https://twitter.com/_srishtiyadav)  ·  [Jul 12](https://twitter.com/_srishtiyadav/status/1149769922265808896)

Replying to [@**martin_gorner**](https://twitter.com/martin_gorner)

Yet to read the paper in detail but is it rotation invariant?

     1 reply          0 retweets          0 likes

    2.

 [![GeL6pDWb_bigger.jpg](../_resources/ef73b28459dbbb80c238b9931bf1e912.jpg)    **Martin Görner**‏ @**martin_gorner**](https://twitter.com/martin_gorner)  ·  [Jul 12](https://twitter.com/martin_gorner/status/1149772393197363200)

A detection network is rotation-invariant only if you train it to be, by having different rotations of the same obj. in the training dataset. For a better approach, see Geof Hinton's capsule networks, designed specifically to address this shortcoming. See

     1 reply          0 retweets          0 likes

    3.

 [![yEoXyn5d_bigger.jpg](../_resources/81ddf4a4346006b2a5edd06d2848531b.jpg)    **Srishti  ‍**‏ @**_srishtiyadav**](https://twitter.com/_srishtiyadav)  ·  [Jul 12](https://twitter.com/_srishtiyadav/status/1149774030406242304)

Interesting!

I always wondered why some of the popular CNNs : ResNet, Yolo, SSD etc. are not rotation invariant. I do occasionally blame the datasets too which usually don't have such training data, especially since it has significant usecase in arial images.

     0 replies          0 retweets          0 likes

 End of conversation

 