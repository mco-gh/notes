leandromoreira/digital_video_introduction

[![license](../_resources/8d679db4868d980a7b7ad443497beea2.bin)](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)

# [(L)](https://github.com/leandromoreira/digital_video_introduction#intro)Intro

A gentle introduction to video technology, although it's aimed at software developers / engineers, we want to make it easy **for anyone to learn**. This idea was born during a [mini workshop for newcomers to video technology](https://docs.google.com/presentation/d/17Z31kEkl_NGJ0M66reqr9_uTG6tI5EDDVXpdPKVuIrs/edit#slide=id.p).

The goal is to introduce some digital video concepts with a **simple vocabulary, lots of visual elements and practical examples** when possible, and make this knowledge available everywhere. Please, feel free to send corrections, suggestions and improve it.

There will be **hands-on** sections which require you to have **docker installed** and this repository cloned.

git clone https://github.com/leandromoreira/digital_video_introduction.gitcd digital_video_introduction

./setup.sh

**> WARNING**> : when you see a ` ./s/ffmpeg `>  or ` ./s/mediainfo `>  command, it means we're running a **> containerized version**>  of that program, which already includes all the needed requirements.

All the **hands-on should be performed from the folder you cloned** this repository. For the **jupyter examples** you must start the server ` ./s/start_jupyter.sh ` and copy the URL and use it in your browser.

# [(L)](https://github.com/leandromoreira/digital_video_introduction#index)Index

- [Intro](https://github.com/leandromoreira/digital_video_introduction#intro)
- [Index](https://github.com/leandromoreira/digital_video_introduction#index)
- [Basic terminology](https://github.com/leandromoreira/digital_video_introduction#basic-terminology)
    - [Other ways to encode a color image](https://github.com/leandromoreira/digital_video_introduction#other-ways-to-encode-a-color-image)
    - [Hands-on: play around with image and color](https://github.com/leandromoreira/digital_video_introduction#hands-on-play-around-with-image-and-color)
    - [DVD is DAR 4:3](https://github.com/leandromoreira/digital_video_introduction#dvd-is-dar-43)
    - [Hands-on: Check video properties](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-video-properties)
- [Redundancy removal](https://github.com/leandromoreira/digital_video_introduction#redundancy-removal)
    - [Colors, Luminance and our eyes](https://github.com/leandromoreira/digital_video_introduction#colors-luminance-and-our-eyes)
        - [Color model](https://github.com/leandromoreira/digital_video_introduction#color-model)
        - [Converting between YCbCr and RGB](https://github.com/leandromoreira/digital_video_introduction#converting-between-ycbcr-and-rgb)
        - [Chroma subsampling](https://github.com/leandromoreira/digital_video_introduction#chroma-subsampling)
        - [Hands-on: Check YCbCr histogram](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-ycbcr-histogram)
    - [Frame types](https://github.com/leandromoreira/digital_video_introduction#frame-types)
        - [I Frame (intra, keyframe)](https://github.com/leandromoreira/digital_video_introduction#i-frame-intra-keyframe)
        - [P Frame (predicted)](https://github.com/leandromoreira/digital_video_introduction#p-frame-predicted)
            - [Hands-on: A video with a single I-frame](https://github.com/leandromoreira/digital_video_introduction#hands-on-a-video-with-a-single-i-frame)
        - [B Frame (bi-predictive)](https://github.com/leandromoreira/digital_video_introduction#b-frame-bi-predictive)
            - [Hands-on: Compare videos with B-frame](https://github.com/leandromoreira/digital_video_introduction#hands-on-compare-videos-with-b-frame)
        - [Summary](https://github.com/leandromoreira/digital_video_introduction#summary)
    - [Temporal redundancy (inter prediction)](https://github.com/leandromoreira/digital_video_introduction#temporal-redundancy-inter-prediction)
        - [Hands-on: See the motion vectors](https://github.com/leandromoreira/digital_video_introduction#hands-on-see-the-motion-vectors)
    - [Spatial redundancy (intra prediction)](https://github.com/leandromoreira/digital_video_introduction#spatial-redundancy-intra-prediction)
        - [Hands-on: Check intra predictions](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-intra-predictions)
- [How does a video codec work?](https://github.com/leandromoreira/digital_video_introduction#how-does-a-video-codec-work)
    - [What? Why? How?](https://github.com/leandromoreira/digital_video_introduction#what-why-how)
    - [History](https://github.com/leandromoreira/digital_video_introduction#history)
        - [The born of AV1](https://github.com/leandromoreira/digital_video_introduction#the-born-of-av1)
    - [A generic codec](https://github.com/leandromoreira/digital_video_introduction#a-generic-codec)
    - [1st step - picture partitioning](https://github.com/leandromoreira/digital_video_introduction#1st-step---picture-partitioning)
        - [Hands-on: Check partitions](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-partitions)
    - [2nd step - predictions](https://github.com/leandromoreira/digital_video_introduction#2nd-step---predictions)
    - [3rd step - transform](https://github.com/leandromoreira/digital_video_introduction#3rd-step---transform)
        - [Hands-on: throwing away different coefficients](https://github.com/leandromoreira/digital_video_introduction#hands-on-throwing-away-different-coefficients)
    - [4th step - quantization](https://github.com/leandromoreira/digital_video_introduction#4th-step---quantization)
        - [Hands-on: quantization](https://github.com/leandromoreira/digital_video_introduction#hands-on-quantization)
    - [5th step - entropy coding](https://github.com/leandromoreira/digital_video_introduction#5th-step---entropy-coding)
        - [VLC coding](https://github.com/leandromoreira/digital_video_introduction#vlc-coding)
        - [Arithmetic coding](https://github.com/leandromoreira/digital_video_introduction#arithmetic-coding)
        - [Hands-on: CABAC vs CAVLC](https://github.com/leandromoreira/digital_video_introduction#hands-on-cabac-vs-cavlc)
    - [6th step - bitstream format](https://github.com/leandromoreira/digital_video_introduction#6th-step---bitstream-format)
        - [H264 bitstream](https://github.com/leandromoreira/digital_video_introduction#h264-bitstream)
        - [Hands-on: Inspect the H264 bitstream](https://github.com/leandromoreira/digital_video_introduction#hands-on-inspect-the-h264-bitstream)
    - [Review](https://github.com/leandromoreira/digital_video_introduction#review)
    - [How does H265 can achieve better compression ratio than H264?](https://github.com/leandromoreira/digital_video_introduction#how-does-h265-can-achieve-better-compression-ratio-than-h264)
- [Online streaming](https://github.com/leandromoreira/digital_video_introduction#online-streaming)
    - [General architecture](https://github.com/leandromoreira/digital_video_introduction#general-architecture)
    - [Progressive download and adaptive streaming](https://github.com/leandromoreira/digital_video_introduction#progressive-download-and-adaptive-streaming)
    - [Content protection](https://github.com/leandromoreira/digital_video_introduction#content-protection)
- [How to use jupyter](https://github.com/leandromoreira/digital_video_introduction#how-to-use-jupyter)
- [Conferences](https://github.com/leandromoreira/digital_video_introduction#conferences)
- [References](https://github.com/leandromoreira/digital_video_introduction#references)

# [(L)](https://github.com/leandromoreira/digital_video_introduction#basic-terminology)Basic terminology

An **image** can be thought of as a **2D matrix**. If we think about **colors**, we can extrapolate this idea seeing this image as a **3D matrix** where the **additional dimensions** are used to provide **color data**.

If we chose to represent these colors using the [primary colors (red, green and blue)](https://en.wikipedia.org/wiki/Primary_color), we define three planes: the first one for **red**, the second for **green**, and the last one for the **blue** color.

[![an image is a 3d matrix RGB](../_resources/91988b163874cf1226b3380c3d9d9a71.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/image_3d_matrix_rgb.png)

We'll call each point in this matrix **a pixel** (picture element). One pixel represents the **intensity** (usually a numeric value) of a given color. For example, a **red pixel** means 0 of green, 0 of blue and maximum of red. The **pink color pixel** can be formed with a combination of the three colors. Using a representative numeric range from 0 to 255, the pink pixel is defined by **Red=255, Green=192 and Blue=203**.

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#other-ways-to-encode-a-color-image)> Other ways to encode a color image

> Many other possible models may be used to represent the colors that make up an image. We could, for instance, use an indexed palette where we'd only need a single byte to represent each pixel instead of the 3 needed when using the RGB model. In such a model we could use a 2D matrix instead of a 3D matrix to represent our color, this would save on memory but yeild fewer color options.

> [![NES palette](../_resources/d72692a006b2e6827ef1857adf323787.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/nes-color-palette.png)

For instance, look at the picture down below. The first face is fully colored. The others are the red, green, and blue planes (shown as gray tones).

[![RGB channels intensity](../_resources/74c4c95d43e7ada5c1caa3929af045cd.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/rgb_channels_intensity.png)

We can see that the **red color** will be the one that **contributes more** (the brightest parts in the second face) to the final color while the **blue color** contribution can be mostly **only seen in Mario's eyes** (last face) and part of his clothes, see how **all planes contribute less** (darkest parts) to the **Mario's mustache**.

And each color intensity requires a certain amount of bits, this quantity is known as **bit depth**. Let's say we spend **8 bits** (accepting values from 0 to 255) per color (plane), therefore we have a **color depth** of **24 (8 * 3) bits** and we can also infer that we could use 2 to the power of 24 different colors.

**> It's great**>  to learn > [> how an image is captured from the world to the bits](http://www.cambridgeincolour.com/tutorials/camera-sensors.htm)> .

Another property of an image is the **resolution**, which is the number of pixels in one dimension. It is often presented as width × height, for example, the **4×4** image bellow.

[![image resolution](../_resources/7e46a91991018ce49b232384a7eecd82.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/resolution.png)

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-play-around-with-image-and-color)> Hands-on: play around with image and color

> You can > [> play around with image and colors](https://github.com/leandromoreira/digital_video_introduction/blob/master/image_as_3d_array.ipynb)>  using > [> jupyter](https://github.com/leandromoreira/digital_video_introduction#how-to-use-jupyter)>  (python, numpy, matplotlib and etc).

> You can also learn > [> how image filters (edge detection, sharpen, blur...) work](https://github.com/leandromoreira/digital_video_introduction/blob/master/filters_are_easy.ipynb)> .

Another property we can see while working with images or video is the **aspect ratio** which simply describes the proportional relationship between width and height of an image or pixel.

When people says this movie or picture is **16x9** they usually are referring to the **Display Aspect Ratio (DAR)**, however we also can have different shapes of individual pixels, we call this **Pixel Aspect Ratio (PAR)**.

[![display aspect ratio](../_resources/992d687033eb8b68fb70536ec9e1806f.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/DAR.png)

[![pixel aspect ratio](../_resources/431780f1d4a4d9d1f2a38d22e13f5555.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/PAR.png)

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#dvd-is-dar-43)> DVD is DAR 4:3

> Although the real resolution of a DVD is 704x480 it still keeps a 4:3 aspect ratio because it has a PAR of 10:11 (704x10/480x11)

Finally, we can define a **video** as a **succession of *n* frames** in **time** which can be seen as another dimension, *n* is the frame rate or frames per second (FPS).

[![video](../_resources/c610ac1a3cc25ab2da2d8f6943b992d8.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/video.png)

The number of bits per second needed to show a video is its **bit rate**. For example, a video with 30 frames per second, 24 bits per pixel, resolution of 480x240 will need **82,944,000 bits per second** or 82.944 Mbps (30x480x240x24) if we don't employ any kind of compression.

When the **bit rate** is nearly constant it's called constant bit rate (**CBR**) but it also can vary then called variable bit rate (**VBR**).

> This graph shows a constrained VBR which doesn't spend too many bits while the frame is black.

> [![constrained vbr](../_resources/628ea458529ab39dfb8b68f5e0bf9d2b.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/vbr.png)

In the early days, engineers came up with a technique for doubling the perceived frame rate of a video display **without consuming extra bandwidth**. This technique is known as **interlaced video**; it basically sends half of the screen in 1 "frame" and the other half in the next "frame".

Today screens render mostly using **progressive scan technique**. Progressive is a way of displaying, storing, or transmitting moving images in which all the lines of each frame are drawn in sequence.

[![interlaced vs progressive](../_resources/55729e5bfeff85eb2be932ac828cacd9.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/interlaced_vs_progressive.png)

Now we have an idea about how an **image** is represented digitally, how its **colors** are arranged, how many **bits per second** do we spend to show a video, if it's constant (CBR) or variable (VBR), with a given **resolution** using a given **frame rate** and many other terms such as interlaced, PAR and others.

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-video-properties)> Hands-on: Check video properties

> You can > [> check most of the explained properties with ffmpeg or mediainfo.](https://github.com/leandromoreira/introduction_video_technology/blob/master/enconding_pratical_examples.md#inspect-stream)

# [(L)](https://github.com/leandromoreira/digital_video_introduction#redundancy-removal)Redundancy removal

We learned that is not feasible to use video without any compression; **a single one hour video** at 720p resolution with 30fps would **require 278GB***. Since **using solely lossless data compression algorithms** like DEFLATE (used in PKZIP, Gzip, and PNG), **won't** decrease the required bandwidth sufficiently we need to find other ways to compress the video.

> *>  We found this number by multiplying 1280 x 720 x 24 x 30 x 3600 (width, height, bits per pixel, fps and time in seconds)

In order to do this, we can **exploit how our vision works**. We're better at distinguishing brightness than colors, the **repetitions in time**, a video contains a lot of images with few changes, and the **repetitions within the image**, each frame also contains many areas using the same or similar color.

## [(L)](https://github.com/leandromoreira/digital_video_introduction#colors-luminance-and-our-eyes)Colors, Luminance and our eyes

Our eyes are [more sensitive to brightness than colors](http://vanseodesign.com/web-design/color-luminance/), you can test it for yourself, look at this picture.

[![luminance vs color](../_resources/c0ba092313539d61821159c1ddbe6273.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/luminance_vs_color.png)

If you are unable to see that the colors of the **squares A and B are identical** on the left side, that's fine, it's our brain playing tricks on us to **pay more attention to light and dark than color**. There is a connector, with the same color, on the right side so we (our brain) can easily spot that in fact, they're the same color.

**> Simplistic explanation of how our eyes work**

> The > [> eye is a complex organ](http://www.biologymad.com/nervoussystem/eyenotes.htm)> , it is composed of many parts but we are mostly interested in the cones and rods cells. The eye > [> contains about 120 million rod cells and 6 million cone cells](https://en.wikipedia.org/wiki/Photoreceptor_cell)> .

> We will abuse of an **> oversimplification**> , let's try to put colors and brightness in the eye's parts function. The **> [> rod cells](https://en.wikipedia.org/wiki/Rod_cell)>  are mostly responsible for brightness**>  while the **> [> cone cells](https://en.wikipedia.org/wiki/Cone_cell)>  are responsible for color**> , there are three types of cones, each with different pigment, namely: > [> S-cones (Blue), M-cones (Green) and L-cones (Red)](https://upload.wikimedia.org/wikipedia/commons/1/1e/Cones_SMJ2_E.svg)> .

> Since we have much more rod cells (brightness) than cone cells (color), one can infer that we are more capable of distinguishing dark and light than colors.

> [![eyes composition](../_resources/45b4e53e2e5ae895086043e3f9154d64.jpg)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/eyes.jpg)

Once we know that we're more sensitive to **luma** (the brightness in an image) we can try to exploit it.

### [(L)](https://github.com/leandromoreira/digital_video_introduction#color-model)Color model

We first learned [how to color images](https://github.com/leandromoreira/digital_video_introduction#basic-terminology) work using **RGB model** but there are others models. In fact, there is a model that separates luma (brightness) from chrominance (colors) and it is known as **YCbCr***.

> *>  there are more models which do the same separation.

This color model uses **Y** to represent the brightness and two color channels **Cb** (chroma blue) and **Cr** (chrome red). The [YCbCr](https://en.wikipedia.org/wiki/YCbCr) can be derived from RGB and it also can be converted back to RGB. Using this model we can create full colored images as we can see down bellow.

[![ycbcr example](../_resources/bbf22a6d658c5219bce22f281076b0e9.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/ycbcr.png)

### [(L)](https://github.com/leandromoreira/digital_video_introduction#converting-between-ycbcr-and-rgb)Converting between YCbCr and RGB

Some may argue, how can we produce all the **colors without using the green**?

To answer this question we'll walk through a conversion from RGB to YCbCr. We'll use the coefficients from the **[standard BT.601](https://en.wikipedia.org/wiki/Rec._601)** that was recommended by the **[group ITU-R*](https://en.wikipedia.org/wiki/ITU-R)** . The first step is to **calculate the luma**, we'll use the constants suggested by ITU and replace the RGB values.

	Y = 0.299R + 0.587G + 0.114B

Once we had the luma, we can **split the colors** (chroma blue and red):

	Cb = 0.564(B - Y)
	Cr = 0.713(R - Y)

And we can also **convert it back** and even get the **green by using YCbCr**.

	R = Y + 1.402Cr
	B = Y + 1.772Cb
	G = Y - 0.344Cb - 0.714Cr

> *>  groups and standards are common in digital video, they usually define what are the standards, for instance, > [> what is 4K? what frame rate should we use? resolution? color model?](https://en.wikipedia.org/wiki/Rec._2020)

Generally, **displays** (monitors, TVs, screens and etc) utilize **only the RGB model**, organized in different manners, see some of them magnified below:

[![pixel geometry](../_resources/7f8b1d61eed3eae1f49344d44b1f2bfb.jpg)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/new_pixel_geometry.jpg)

### [(L)](https://github.com/leandromoreira/digital_video_introduction#chroma-subsampling)Chroma subsampling

Once we are able to separate luma from chroma, we can take advantage of the human visual system that is more capable of seeing luma than chroma. **Chroma subsampling** is the technique of encoding images using **less resolution for chroma than for luma**.

[![ycbcr subsampling resolutions](../_resources/ce83483aee177b6fb73e992f8c02c0ca.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/ycbcr_subsampling_resolution.png)

How much should we reduce the chroma resolution?! It turns out that there are already some schemas that describe how to handle resolution and the merge (` final color = Y + Cb + Cr `).

These schemas are known as subsampling systems (or ratios), they are identified by the numbers: **4:4:4, 4:2:3, 4:2:1, 4:1:1, 4:2:0, 4:1:0 and 3:1:1**. And each one of them defines how much should we discard in the chroma resolution as well as how we should merge the three planes (Y, Cb, Cr).

**> YCbCr 4:2:0 merge**

> Here's a merged piece of an image using YCbCr 4:2:0, notice that we only spend 12 bits per pixel.

> [![YCbCr 4:2:0 merge](../_resources/63c53bba17c0b3f676efa1e14b5215a0.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/ycbcr_420_merge.png)

You can see the same image encoded by the main chroma subsampling types, the first row of images are the final YCbCr while the last row of images shows the chroma resolution. It's indeed a great win for such small loss.

[![chroma subsampling examples](../_resources/04e87ee71e5587768d81350f43cd82b6.jpg)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/chroma_subsampling_examples.jpg)

Previously we had calculated that we needed [278GB of storage to keep a video file with one hour at 720p resolution and 30fps](https://github.com/leandromoreira/digital_video_introduction#redundancy-removal). If we use **YCbCr 4:2:0** we can cut **this size in half (139GB)*** but it is still far from the ideal.

> *>  we found this value by multiplying width, height, bits per pixel and fps. Previously we needed 24 bits, now we only need 12.

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-ycbcr-histogram)> Hands-on: Check YCbCr histogram

> You can > [> check the YCbCr histogram with ffmpeg.](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#generates-yuv-histogram)>  This scene has the more blue contribution which is showed by the > [> histogram](https://en.wikipedia.org/wiki/Histogram)> .

> [![ycbcr color histogram](../_resources/f21dec817f31aba5976e2df7e2c12ead.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/yuv_histogram.png)

## [(L)](https://github.com/leandromoreira/digital_video_introduction#frame-types)Frame types

Now we can move on and try to eliminate the **redundancy in time** but before that let's establish some basic terminology. Suppose we have a movie with 30fps, here are its first 4 frames.

[![ball 1](../_resources/8d812859ab22a2a616bae3494731267f.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_1.png)  [![ball 2](../_resources/eed3fceeb1f4aadd5db9655f83ccea3b.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_2.png)  [![ball 3](../_resources/ca7bd8b9a4781fd9396309c4820ad017.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_3.png)[![ball 4](../_resources/57d29eea2223160f57ddf3c2d1a1de3d.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_4.png)

We can see **lots of repetitions** within frames like **the blue background**, it doesn't change from frame 0 to frame 3. To tackle this problem we can **abstractly categorize** them as three types of frames.

### [(L)](https://github.com/leandromoreira/digital_video_introduction#i-frame-intra-keyframe)I Frame (intra, keyframe)

An I-frame (reference, keyframe, intra) is a **self-contained frame**. It doesn't rely on anything to be rendered, an I-frame looks similar to a static photo. The first frame is usually an I-frame but we'll see I-frames inserted regularly among other types of frames.

[[ball 1](../_resources/8d812859ab22a2a616bae3494731267f.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_1.png)

### [(L)](https://github.com/leandromoreira/digital_video_introduction#p-frame-predicted)P Frame (predicted)

A P-frame takes advantage of the fact that almost always the current picture can be **rendered using the previous frame.** For instance, in the second frame, the only change was the ball that moved forward. We can **rebuild frame 1, only using the difference and referencing to the previous frame**.

[(L)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_1.png) <- [(L)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_2_diff.png)

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-a-video-with-a-single-i-frame)> Hands-on: A video with a single I-frame

> Since a P-frame uses less data why can't we encode an entire > [> video with a single I-frame and all the rest being P-frames?](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#1-i-frame-and-the-rest-p-frames)

> After you encoded this video, start to watch it and do a **> seek for an advanced**>  part of the video, you'll notice **> it takes some time**>  to really move to that part. That's because a **> P-frame needs a reference frame**>  (I-frame for instance) to be rendered.

> Another quick test you can do is to encode a video using a single I-Frame and then > [> encode it inserting an I-frame each 2s](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#1-i-frames-per-second-vs-05-i-frames-per-second)>  and **> check the size of each rendition**> .

### [(L)](https://github.com/leandromoreira/digital_video_introduction#b-frame-bi-predictive)B Frame (bi-predictive)

What about referencing the past and future frames to provide even a better compression?! That's basically what a B-frame is.

[(L)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_1.png) <- [(L)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_2_diff.png) -> [(L)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_background_ball_3.png)

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-compare-videos-with-b-frame)> Hands-on: Compare videos with B-frame

> You can generate two renditions, first with B-frames and other with > [> no B-frames at all](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#no-b-frames-at-all)>  and check the size of the file as well as the quality.

### [(L)](https://github.com/leandromoreira/digital_video_introduction#summary)Summary

These frames types are used to **provide better compression**, we'll look how this happens in the next section, for now, we can think of **I-frame is expensive while P-frame is cheaper but the cheapest is the B-frame.**

[![frame types example](../_resources/e035c5b34eb286944d439c77d9d3357a.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/frame_types.png)

## [(L)](https://github.com/leandromoreira/digital_video_introduction#temporal-redundancy-inter-prediction)Temporal redundancy (inter prediction)

Let's explore the options we have to reduce the **repetitions in time**, this type of redundancy can be solved with techniques of **inter prediction**.

We will try to **spend fewer bits** to encode the sequence of frames 0 and 1.

[![original frames](../_resources/86ec01c4857f9297eb9182431c136f88.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/original_frames.png)

One thing we can do it's a subtraction, we simply **subtract frame 1 from frame 0** and we get just what we need to **encode the residual**.

[![delta frames](../_resources/ee9a0956b88a3d331f7500409ce3be49.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/difference_frames.png)

But if I tell you that there is a **better method** which uses even fewer bits?! First, let's treat the ` frame 0 ` as a collection of well-defined partitions and then we'll try to match the blocks from ` frame 0 ` on ` frame 1 `. We can think of it as **motion estimation**.

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#wikipedia---block-motion-compensation)> Wikipedia - block motion compensation

> "**> Block motion compensation**>  divides up the current frame into non-overlapping blocks, and the motion compensation vector **> tells where those blocks come from**>  (a common misconception is that the previous frame is divided up into non-overlapping blocks, and the motion compensation vectors tell where those blocks move to). The source blocks typically overlap in the source frame. Some video compression algorithms assemble the current frame out of pieces of several different previously-transmitted frames."

[![delta frames](../_resources/4bff46f315422f84ebdcf4753f932e42.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/original_frames_motion_estimation.png)

We could estimate that the ball moved from ` x=0, y=25 ` to ` x=6, y=26 `, the **x** and **y** values are the **motion vectors**. One **further step** we can do to save bits is to **encode only the motion vector difference** between the last block position and the predicted, so the final motion vector would be ` x=6 (6-0), y=1 (26-25) `

> In a real world situation, this **> ball would be sliced into n partitions**>  but the process is the same.

The objects on the frame **move in a 3D way**, the ball can become smaller when it moves to the background. It's normal that **we won't find the perfect match** to the block we tried to find a match. Here's a superposed view of our estimation vs the real picture.

[![motion estimation](../_resources/d143547d089bfc44093b95baf71c1875.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/motion_estimation.png)

But we can see that when we apply **motion estimation** the **data to encode is smaller** than using simply delta frame techniques.

[![motion estimation vs delta ](../_resources/1a65cc947a03aca00ab42b0c3cb1260c.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/comparison_delta_vs_motion_estimation.png)

You can [play around with these concepts using jupyter](https://github.com/leandromoreira/digital_video_introduction/blob/master/frame_difference_vs_motion_estimation_plus_residual.ipynb).

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-see-the-motion-vectors)> Hands-on: See the motion vectors

> We can > [> generate a video with the inter prediction (motion vectors) with ffmpeg.](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#generate-debug-video)

> [![inter prediction (motion vectors) with ffmpeg](../_resources/6d2f11445b946a8eb50987aa8f8848ac.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/motion_vectors_ffmpeg.png)

> Or we can use the > [> Intel Video Pro Analyzer](https://software.intel.com/en-us/intel-video-pro-analyzer)>  (which is paid but there is a free trial version which limits you to only the first 10 frames).

> [![inter prediction intel video pro analyzer](../_resources/a7a88614b06d40f44df1f85d2dee65a3.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/inter_prediction_intel_video_pro_analyzer.png)

## [(L)](https://github.com/leandromoreira/digital_video_introduction#spatial-redundancy-intra-prediction)Spatial redundancy (intra prediction)

If we analyze **each frame** in a video we'll see that there are also **many areas that are correlated**.

[![repetitions_in_space.png](../_resources/8b5caf176c9e3fc10f5a6f79381d2ee0.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/repetitions_in_space.png)

Let's walk through an example. This scene is mostly composed of blue and white colors.

[![smw_bg.png](../_resources/8cd8a9bc34afc7452c956d1404707c6d.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_bg.png)

This is an ` I-frame ` and we **can't use previous frames** to predict from but we still can compress it. We will encode the red block selection. If we **look at its neighbors**, we can **estimate** that there is a **trend of colors around it**.

[![smw_bg_block.png](../_resources/ffac612861f476bb67f838f86b0e1b24.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_bg_block.png)

We will **predict** that the frame will continue to **spread the colors vertically**, it means that the colors of the **unknown pixels will hold the values of its neighbors**.

[![smw_bg_prediction.png](../_resources/c2e625dcb4873ad39f40a4e3d19c1915.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_bg_prediction.png)

Our **prediction can be wrong**, for that reason we need to apply this technique (**intra prediction**) and then **subtract the real values** which gives us the residual block, resulting in a much more compressible matrix compared to the original.

[![smw_residual.png](:/295b859c8d17025264b51cc64932900b)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/smw_residual.png)

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-intra-predictions)> Hands-on: Check intra predictions

> You can > [> generate a video with macro blocks and their predictions with ffmpeg.](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#generate-debug-video)>  Please check the ffmpeg documentation to understand the > [> meaning of each block color](https://trac.ffmpeg.org/wiki/Debug/MacroblocksAndMotionVectors)> .

> [![intra prediction (macro blocks) with ffmpeg](../_resources/3cae4626a60488397d3d6a0922fd3f88.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/macro_blocks_ffmpeg.png)

> Or we can use the > [> Intel Video Pro Analyzer](https://software.intel.com/en-us/intel-video-pro-analyzer)>  (which is paid but there is a free trial version which limits you to only the first 10 frames).

> [![intra prediction intel video pro analyzer](../_resources/d56803c77fa79470eb99b1adfad57ab5.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/intra_prediction_intel_video_pro_analyzer.png)

# [(L)](https://github.com/leandromoreira/digital_video_introduction#how-does-a-video-codec-work)How does a video codec work?

## [(L)](https://github.com/leandromoreira/digital_video_introduction#what-why-how)What? Why? How?

**What?** It's a software / hardware that compresses or decompresses digital video. **Why?** Market and society demands higher quality videos with limited bandwidth or storage. Remember when we [calculated the needed bandwidth](https://github.com/leandromoreira/digital_video_introduction#basic-terminology) for 30 frames per second, 24 bits per pixel, resolution of a 480x240 video? It was **82.944 Mbps** with no compression applied. It's the only way to deliver HD/FullHD/4K in TVs and the Internet. **How?** We'll take a brief look at the major techniques here.

**> CODEC vs Container**

> One common mistake that beginners often do is to confuse digital video CODEC and > [> digital video container](https://en.wikipedia.org/wiki/Digital_container_format)> . We can think of **> containers**>  as a wrapper format which contains metadata of the video (and possible audio too), and the **> compressed video**>  can be seen as its payload.

> Usually, the extension of a video file defines its video container. For instance, the file ` video.mp4 `>  is probably a **> [> MPEG-4 Part 14](https://en.wikipedia.org/wiki/MPEG-4_Part_14)**>  container and a file named ` video.mkv `>  it's probably a **> [> matroska](https://en.wikipedia.org/wiki/Matroska)**> . To be completely sure about the codec and container format we can use > [> ffmpeg or mediainfo](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#inspect-stream)> .

## [(L)](https://github.com/leandromoreira/digital_video_introduction#history)History

Before we jump in the inner works of a generic codec, let's look back to understand a little better about some old video codecs.

The video codec [H261](https://en.wikipedia.org/wiki/H.261) was born in 1990 (technically 1988), and it was designed to work with **data rates of 64 kbit/s**. It already uses ideas such as chroma subsampling, macro block, etc. In the year of 1995, the **H263** video codec standard was published and continued to be extended until 2001.

In 2003 the first version of **H.264/AVC** was completed. In the same year, a company called **TrueMotion** released their video codec as a **royalty-free** lossy video compression called **VP3**. In 2008, **Google bought** this company, releasing **VP8** in the same year. In December of 2012, Google released the **VP9** and it's **supported by roughly ¾ of the browser market** (mobile included).

**[AV1](https://en.wikipedia.org/wiki/AOMedia_Video_1)** is a new video codec, **royalty-free**, open source being designed by the [Alliance for Open Media (AOMedia)](http://aomedia.org/) which is composed of the **companies: Google, Mozilla, Microsoft, Amazon, Netflix, AMD, ARM, NVidia, Intel, Cisco** among others. The **first version** 0.1.0 of the reference codec was **published on April 7, 2016**.

[![codec history timeline](../_resources/39a8a54eccdfdf22bd9a9de21bf145b3.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/codec_history_timeline.png)

#### > [(L)](https://github.com/leandromoreira/digital_video_introduction#the-birth-of-av1)> The birth of AV1

> Early 2015, Google was working on > [> VP10](https://en.wikipedia.org/wiki/VP9#Successor:_from_VP10_to_AV1)> , Xiph (Mozilla) was working on > [> Daala](https://xiph.org/daala/)>  and Cisco open-sourced its royalty-free video codec called > [> Thor](https://tools.ietf.org/html/draft-fuldseth-netvc-thor-03)> .

> Then MPEG LA first announced annual caps for HEVC (H265) and fees 8 times higher than H264 but soon they changed the rules again:

- **> no annual cap**> ,
- **> content fee**>  (0.5% of revenue) and
- **> per-unit fees about 10 times higher than h264**> .

> The > [> alliance for open media](http://aomedia.org/about-us/)>  was created by companies from hardware manufacturer (Intel, AMD, ARM , Nvidia, Cisco), content delivery (Google, Netflix, Amazon), browser maintainers (Google, Mozilla), and others.

> The companies had a common goal, a royalty-free video codec and then AV1 was born with a much > [> simpler patent license](http://aomedia.org/license/patent/)> . **> Timothy B. Terriberry**>  did an awesome presentation, which is the source of this section, about the > [> AV1 conception, license model and its current state](https://www.youtube.com/watch?v=lzPaldsmJbk)> .

> You'll be surprised to know that you can **> analyze the AV1 codec through your browser**> , go to > [http://aomanalyzer.org/

> [![av1 browser analyzer](../_resources/295c471aa94c1b264bc7ab7a358c84f8.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/av1_browser_analyzer.png)

> PS: If you want to learn more about the history of the codecs you must learn the basics behind > [> video compression patents](https://www.vcodex.com/video-compression-patents/)> .

## [(L)](https://github.com/leandromoreira/digital_video_introduction#a-generic-codec)A generic codec

We're going to introduce the **main mechanics behind a generic video codec** but most of these concepts are useful and used in modern codecs such as VP9, AV1 and HEVC. Be sure to understand that we're going to simplify things a LOT. Sometimes we'll use a real example (mostly H264) to demonstrate a technique.

## [(L)](https://github.com/leandromoreira/digital_video_introduction#1st-step---picture-partitioning)1st step - picture partitioning

The first step is to **divide the frame** into several **partitions, sub-partitions** and beyond.

[![picture partitioning](../_resources/b6d3c6bd855e75cd25d4c4de4671a7d7.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/picture_partitioning.png)

**But why?** There are many reasons, for instance, when we split the picture we can work the predictions more precisely, using small partitions for the small moving parts while using bigger partitions to a static background.

Usually, the CODECs **organize these partitions** into slices (or tiles), macro (or coding tree units) and many sub-partitions. The max size of these partitions varies, HEVC sets 64x64 while AVC uses 16x16 but the sub-partitions can reach sizes of 4x4.

Remember that we learned how **frames are typed**?! Well, you can **apply those ideas to blocks** too, therefore we can have I-Slice, B-Slice, I-Macroblock and etc.

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-check-partitions)> Hands-on: Check partitions

> We can also use the > [> Intel Video Pro Analyzer](https://software.intel.com/en-us/intel-video-pro-analyzer)>  (which is paid but there is a free trial version which limits you to only the first 10 frames). Here are > [> VP9 partitions](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#transcoding)>  analyzed.

> [![VP9 partitions view intel video pro analyzer ](../_resources/8baa0db04ed0f9c236601b3d65ad0629.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/paritions_view_intel_video_pro_analyzer.png)

## [(L)](https://github.com/leandromoreira/digital_video_introduction#2nd-step---predictions)2nd step - predictions

Once we have the partitions, we can make predictions over them. For the [inter prediction](https://github.com/leandromoreira/digital_video_introduction/blob/master/digital_video_introduction#temporal-redundancy-inter-prediction) we need **to send the motion vectors and the residual** and the [intra prediction](https://github.com/leandromoreira/digital_video_introduction/blob/master/digital_video_introduction#spatial-redundancy-intra-prediction) we'll **send the prediction direction and the residual** as well.

## [(L)](https://github.com/leandromoreira/digital_video_introduction#3rd-step---transform)3rd step - transform

After we get the residual block (` predicted partition - real partition `), we can **transform** it in a way that we can know which **pixels we can discard** but still keeping the **overall quality**. There are some transformations for this exact behavior.

Although there are [other transformations](https://en.wikipedia.org/wiki/List_of_Fourier-related_transforms#Discrete_transforms), we'll look more closely the discrete cosine transform (DCT). The [**DCT**](https://en.wikipedia.org/wiki/Discrete_cosine_transform) main features are:

- **converts** blocks of **pixels** into same-sized blocks of **frequency coefficients**.
- **compacts** energy, making it easy to eliminate spatial redundancy.
- is **reversible**, a.k.a. you can reverse to pixels.

> On 2 Feb 2017, Cintra, R. J. and Bayer, F. M have published their paper > [> DCT-like Transform for Image Compression Requires 14 Additions Only](https://arxiv.org/abs/1702.00817)> .

Don't worry if you didn't understand the benefits from every bullet point, we'll try to make some experiments in order to see the real value from it.

Let's take the following **block of pixels** (8x8):

[![pixel values matrix](../_resources/c6626751d19f318b7ed412602eba6493.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/pixel_matrice.png)

Which renders to the following block image (8x8):

[![pixel values matrix](../_resources/58ba36df5c006567297579cbb800c09d.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/gray_image.png)

When we **apply the DCT** over this block of pixels and we get the **block of coefficients** (8x8):

[![coefficients values](../_resources/a2533050c4d29f8fc021618aeae609c3.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/dct_coefficient_values.png)

And if we render this block of coefficients, we'll get this image:

[![dct coefficients image](../_resources/af7ddba468b20eaadc573eef64e2eed1.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/dct_coefficient_image.png)

As you can see it looks nothing like the original image, we might notice that the **first coefficient** is very different from all the others. This first coefficient is known as the DC coefficient which represents of **all the samples** in the input array, something **similar to an average**.

This block of coefficients has an interesting property which is that it separates the high-frequency components from the low frequency.

[![dct frequency coefficients property](../_resources/0ef0626ab19eeecd71bf9638a70821fb.jpg)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/dctfrequ.jpg)

In an image, **most of the energy** will be concentrated in the [**lower frequencies**](https://www.iem.thm.de/telekom-labor/zinke/mk/mpeg2beg/whatisit.htm), so if we transform an image into its frequency components and **throw away the higher frequency coefficients**, we can **reduce the amount of data** needed to describe the image without sacrificing too much image quality.

> frequency means how fast a signal is changing

Let's try to apply the knowledge we acquired in the test, we'll convert the original image to its frequency (block of coefficients) using DCT and then throw away part of the least important coefficients.

First, we convert it to its **frequency domain**.

[![coefficients values](../_resources/a2533050c4d29f8fc021618aeae609c3.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/dct_coefficient_values.png)

And then we discard part (67%) of the coefficients, mostly the bottom right part of it.

[![zeroed coefficients](../_resources/f397aa8c8711f2bc1e5fc7885b5848ee.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/dct_coefficient_zeroed.png)

And then we reconstruct the image from this discarded block of coefficients (remember, it needs to be reversible) and compare it to the original.

[![original vs quantized](../_resources/d45dd375053462442e0a7c9db249a872.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/original_vs_quantized.png)

As we can see it resembles the original image but it introduced lots of differences from the original, we **throw away 67.1875%** and we still were able to get at least something similar to the original. We could more intelligently discard the coefficients to have a better image quality but that's the next topic.

**> Each coefficient is formed using all the pixels**

> It's important to note that each coefficient doesn't directly map to a single pixel but it's a weighted sum of all pixels. This amazing graph shows how the first and second coefficient is calculated, using weights which are unique for each index.

> [![dct calculation](../_resources/edfd976ecbb997e9357572aff93358c5.jpg)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/applicat.jpg)

> Source: > [https://www.iem.thm.de/telekom-labor/zinke/mk/mpeg2beg/whatisit.htm

> You can also try to > [> visualize the DCT by looking at a simple image](https://github.com/leandromoreira/digital_video_introduction/blob/master/dct_better_explained.ipynb)>  formation over the DCT basis. For instance, here's the > [> A character being formed](https://en.wikipedia.org/wiki/Discrete_cosine_transform#Example_of_IDCT)>  using each coefficient weight.

> [![68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f352f35652f496463742d616e696d6174696f6e2e676966.gif](../_resources/e4cf46bbea104b3deb93c6eb30a0b027.gif)](https://camo.githubusercontent.com/ac2f3ff3a6e29112f3e7f51325cb7d3a2f08e377/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f352f35652f496463742d616e696d6174696f6e2e676966)

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-throwing-away-different-coefficients)> Hands-on: throwing away different coefficients

> You can play around with the > [> DCT transform](https://github.com/leandromoreira/digital_video_introduction/blob/master/uniform_quantization_experience.ipynb)> .

## [(L)](https://github.com/leandromoreira/digital_video_introduction#4th-step---quantization)4th step - quantization

When we throw away some of the coefficients, in the last step (transform), we kinda did some form of quantization. This step is where we chose to lose information (the **lossy part**) or in simple terms, we'll **quantize coefficients to achieve compression**.

How can we quantize a block of coefficients? One simple method would be a uniform quantization, we take a block and **divide it by a single value** (10) and round this value.

[![quantize](../_resources/98abb6aee9df7ea27eb68765eb13d9d2.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/quantize.png)

How can we **reverse** (re-quantize) this block of coefficients? We can do that by **multiplying the same value** (10) we divide it first.

[![re-quantize](../_resources/99d8d3811e3e2ff4691d69dc950b93d8.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/re-quantize.png)

This **approach isn't the best** because it doesn't take into account the importance of each coefficient, we could use a **matrix of quantizers** instead of a single value, this matrix can exploit the property of the DCT, quantizing most the bottom right and less the upper left, the [JPEG uses a similar approach](https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/jpegUpToQuant.html), you can check [source code to see this matrix](https://github.com/google/guetzli/blob/master/guetzli/jpeg_data.h#L40).

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-quantization)> Hands-on: quantization

> You can play around with the > [> quantization](https://github.com/leandromoreira/digital_video_introduction/blob/master/dct_experiences.ipynb)> .

## [(L)](https://github.com/leandromoreira/digital_video_introduction#5th-step---entropy-coding)5th step - entropy coding

After we quantized the data (image blocks/slices/frames) we still can compress it in a lossless way. There are many ways (algorithms) to compress data. We're going to briefly experience some of them, for a deeper understanding you can read the amazing book [Understanding Compression: Data Compression for Modern Developers](https://www.amazon.com/Understanding-Compression-Data-Modern-Developers/dp/1491961538/).

### [(L)](https://github.com/leandromoreira/digital_video_introduction#vlc-coding)VLC coding:

Let's suppose we have a stream of the symbols: **a**, **e**, **r** and **t** and their probability (from 0 to 1) is represented by this table.

|     | a   | e   | r   | t   |
| --- | --- | --- | --- | --- |
| probability | 0.3 | 0.3 | 0.2 | 0.2 |

We can assign unique binary codes (preferable small) to the most probable and bigger codes to the least probable ones.

|     | a   | e   | r   | t   |
| --- | --- | --- | --- | --- |
| probability | 0.3 | 0.3 | 0.2 | 0.2 |
| binary code | 0   | 10  | 110 | 1110 |

Let's compress the stream **eat**, assuming we would spend 8 bits for each symbol, we would spend **24 bits** without any compression. But in case we replace each symbol for its code we can save space.

The first step is to encode the symbol **e** which is ` 10 ` and the second symbol is **a** which is added (not in a mathematical way) ` [10][0] ` and finally the third symbol **t** which makes our final compressed bitstream to be ` [10][0][1110] ` or ` 1001110 ` which only requires **7 bits** (3.4 times less space than the original).

Notice that each code must be a unique prefixed code [Huffman can help you to find these numbers](https://en.wikipedia.org/wiki/Huffman_coding). Though it has some issues there are [video codecs that still offers](https://en.wikipedia.org/wiki/Context-adaptive_variable-length_coding) this method and it's the algorithm for many application which requires compression.

Both encoder and decoder **must know** the symbol table with its code, therefore, you need to send the table too.

### [(L)](https://github.com/leandromoreira/digital_video_introduction#arithmetic-coding)Arithmetic coding:

Let's suppose we have a stream of the symbols: **a**, **e**, **r**, **s** and **t** and their probability is represented by this table.

|     | a   | e   | r   | s   | t   |
| --- | --- | --- | --- | --- | --- |
| probability | 0.3 | 0.3 | 0.15 | 0.05 | 0.2 |

With this table in mind, we can build ranges containing all the possible symbols sorted by the most frequents.

[![initial arithmetic range](../_resources/81b9bb8a6ecebcc17b4bd68651c2db5b.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/range.png)

Now let's encode the stream **eat**, we pick the first symbol **e** which is located within the subrange **0.3 to 0.6** (but not included) and we take this subrange and split it again using the same proportions used before but within this new range.

[![second sub range](../_resources/deebbefc94af8dacd870ae19848c6fd0.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/second_subrange.png)

Let's continue to encode our stream **eat**, now we take the second symbol **a** which is within the new subrange **0.3 to 0.39** and then we take our last symbol **t** and we do the same process again and we get the last subrange **0.354 to 0.372**.

[![final arithmetic range](../_resources/3247b73e99caa1407f36fb5bb406ffa4.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/arithimetic_range.png)

We just need to pick a number within the last subrange **0.354 to 0.372**, let's choose **0.36** but we could choose any number within this subrange. With **only** this number we'll be able to recover our original stream **eat**. If you think about it, it's like if we were drawing a line within ranges of ranges to encode our stream.

[![final range traverse](../_resources/b1f2ccd76fdaf8c2fb05b5d665cac19f.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/range_show.png)

The **reverse process** (A.K.A. decoding) is equally easy, with our number **0.36** and our original range we can run the same process but now using this number to reveal the stream encoded behind this number.

With the first range we notice that our number fits at the slice, therefore, it's our first symbol, now we split this subrange again, doing the same process as before, and we'll notice that **0.36** fits the symbol **a** and after we repeat the process we came to the last symbol **t** (forming our original encoded stream *eat*).

Both encoder and decoder **must know** the symbol probability table, therefore you need to send the table.

Pretty neat, isn't? People are damn smart to come up with such solution, some [video codec uses](https://en.wikipedia.org/wiki/Context-adaptive_binary_arithmetic_coding) (or at least offers as an option) this technique.

The idea is to lossless compress the quantized bitstream, for sure this article is missing tons of details, reasons, trade-offs and etc. But [you should learn more](https://www.amazon.com/Understanding-Compression-Data-Modern-Developers/dp/1491961538/) as a developer. Newer codecs are trying to use different [entropy coding algorithms like ANS.](https://en.wikipedia.org/wiki/Asymmetric_Numeral_Systems)

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-cabac-vs-cavlc)> Hands-on: CABAC vs CAVLC

> You can > [> generate two streams, one with CABAC and other with CAVLC](https://github.com/leandromoreira/introduction_video_technology/blob/master/enconding_pratical_examples.md#cabac-vs-cavlc)>  and **> compare the time**>  it took to generate each of them as well as **> the final size**> .

## [(L)](https://github.com/leandromoreira/digital_video_introduction#6th-step---bitstream-format)6th step - bitstream format

After we did all these steps we need to **pack the compressed frames and context to these steps**. We need to explicitly inform to the decoder about **the decisions taken by the encoder**, such as bit depth, color space, resolution, predictions info (motion vectors, intra prediction direction), profile, level, frame rate, frame type, frame number and much more.

We're going to study, superficially, the H264 bitstream. Our first step is to [generate a minimal H264 * bitstream](https://github.com/leandromoreira/digital_video_introduction/blob/master/enconding_pratical_examples.md#generate-a-single-frame-h264-bitstream), we can do that using our own repository and [ffmpeg](http://ffmpeg.org/).

	./s/ffmpeg -i /files/i/minimal.png -pix_fmt yuv420p /files/v/minimal_yuv420.h264

> *>  ffmpeg adds, by default, all the encoding parameter as a **> SEI NAL**> , soon we'll define what is a NAL.

This command will generate a raw h264 bitstream with a **single frame**, 64x64, with color space yuv420 and using the following image as the frame.

> [![used frame to generate minimal h264 bitstream](../_resources/a05a134a196c6ae0ada0c6e5cd26f045.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/minimal.png)

### [(L)](https://github.com/leandromoreira/digital_video_introduction#h264-bitstream)H264 bitstream

The AVC (H264) standard defines that the information will be sent in **macro frames** (in the network sense), called **[NAL](https://en.wikipedia.org/wiki/Network_Abstraction_Layer)** (Network Abstraction Layer). The main goal of the NAL is the provision of a "network-friendly" video representation, this standard must work on TVs (stream based), the Internet (packet based) among others.

[![NAL units H264](../_resources/bbe7e36ea13034aa62bcc64a218ac107.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/nal_units.png)

There is a **[synchronization marker](https://en.wikipedia.org/wiki/Frame_synchronization)** to define the boundaries of the NAL's units. Each synchronization marker holds a value of ` 0x00 0x00 0x01 ` except to the very first one which is ` 0x00 0x00 0x00 0x01 `. If we run the **hexdump** on the generated h264 bitstream, we can identify at least three NALs in the beginning of the file.

[![synchronization marker on NAL units](../_resources/e0786c0ce510eb8457e36f4e8b4d9b54.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/minimal_yuv420_hex.png)

As we said before, the decoder needs to know not only the picture data but also the details of the video, frame, colors, used parameters, and others. The **first byte** of each NAL defines its category and **type**.

| NAL type id | Description |
| --- | --- |
| 0   | Undefined |
| 1   | Coded slice of a non-IDR picture |
| 2   | Coded slice data partition A |
| 3   | Coded slice data partition B |
| 4   | Coded slice data partition C |
| 5   | **IDR** Coded slice of an IDR picture |
| 6   | **SEI** Supplemental enhancement information |
| 7   | **SPS** Sequence parameter set |
| 8   | **PPS** Picture parameter set |
| 9   | Access unit delimiter |
| 10  | End of sequence |
| 12  | End of stream |
| ... | ... |

Usually, the first NAL of a bitstream is a **SPS**, this type of NAL is responsible for informing the general encoding variables like **profile**, **level**, **resolution** and others.

If we skip the first synchronization marker we can decode the **first byte** to know what **type of NAL** is the first one.

For instance the first byte after the synchronization marker is ` 01100111 `, where the first bit (` 0 `) is to the field **forbidden_zero_bit**, the next 2 bits (` 11 `) tell us the field **nal_ref_idc** which indicates whether this NAL is a reference field or not and the rest 5 bits (` 00111 `) inform us the field **nal_unit_type**, in this case, it's a **SPS** (7) NAL unit.

The second byte (` binary=01100100, hex=0x64, dec=100 `) of an SPS NAL is the field **profile_idc** which shows the profile that the encoder has used, in this case, we used the **[constrained high-profile](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC#Profiles)**, it's a high profile without the support of B (bi-predictive) slices.

[![SPS binary view](../_resources/ddcdf41595f86a4be9398062a1e5e86c.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/minimal_yuv420_bin.png)

When we read the H264 bitstream spec for an SPS NAL we'll find many values for the **parameter name**, **category** and a **description**, for instance, let's look at ` pic_width_in_mbs_minus_1 ` and ` pic_height_in_map_units_minus_1 ` fields.

| Parameter name | Category | Description |
| --- | --- | --- |
| pic_width_in_mbs_minus_1 | 0   | ue(v) |
| pic_height_in_map_units_minus_1 | 0   | ue(v) |

**> ue(v)**> : unsigned integer > [> Exp-Golomb-coded](https://pythonhosted.org/bitstring/exp-golomb.html)

If we do some math with the value of these fields we will end up with the **resolution**. We can represent a ` 1920 x 1080 ` using a ` pic_width_in_mbs_minus_1 ` with the value of ` 119 ( (119 + 1) * macroblock_size = 120 * 16 = 1920) `, again saving space, instead of encode ` 1920 ` we did it with ` 119 `.

If we continue to examine our created video with a binary view (ex: ` xxd -b -c 11 v/minimal_yuv420.h264 `), we can skip to the last NAL which is the frame itself.

[![h264 idr slice header](../_resources/97e6c667cbbd8e30e1d733386827f297.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/slice_nal_idr_bin.png)

We can see its first 6 bytes values: ` 01100101 10001000 10000100 00000000 00100001 11111111 `. As we already know the first byte tell us about what type of NAL it is, in this case, (` 00101 `) it's an **IDR Slice (5)** and we can further inspect it:

[![h264 slice header spec](../_resources/c11e2a414eafc209fd53df88623626d3.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/slice_header.png)

Using the spec info we can decode what type of slice (**slice_type**), the frame number (**frame_num**) among others important fields.

In order to get the values of some fields (` ue(v), me(v), se(v) or te(v) `) we need to decode it using a special decoder called [Exponential-Golomb](https://pythonhosted.org/bitstring/exp-golomb.html), this method is **very efficient to encode variable values**, mostly when there are many default values.

> The values of **> slice_type**>  and **> frame_num**>  of this video are 7 (I slice) and 0 (the first frame).

We can see the **bitstream as a protocol** and if you want or need to learn more about this bitstream please refer to the [ITU H264 spec.](http://www.itu.int/rec/T-REC-H.264-201610-I) Here's a macro diagram which shows where the picture data (compressed YUV) resides.

[![h264 bitstream macro diagram](../_resources/f16dd6c3bf8a6ea21b335adcfe876dca.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/h264_bitstream_macro_diagram.png)

We can explore others bitstreams like the [VP9 bitstream](https://storage.googleapis.com/downloads.webmproject.org/docs/vp9/vp9-bitstream-specification-v0.6-20160331-draft.pdf), [H265 (HEVC)](http://handle.itu.int/11.1002/1000/11885-en?locatt=format:pdf) or even our **new best friend**  [**AV1** bitstream](https://medium.com/@mbebenita/av1-bitstream-analyzer-d25f1c27072b#.d5a89oxz8), [do they all look similar? No](http://www.gpac-licensing.com/2016/07/12/vp9-av1-bitstream-format/), but once you learned one you can easily get the others.

### > [(L)](https://github.com/leandromoreira/digital_video_introduction#hands-on-inspect-the-h264-bitstream)> Hands-on: Inspect the H264 bitstream

> We can > [> generate a single frame video](https://github.com/leandromoreira/introduction_video_technology/blob/master/enconding_pratical_examples.md#generate-a-single-frame-video)>  and use > [> mediainfo](https://en.wikipedia.org/wiki/MediaInfo)>  to inspect its H264 bitstream. In fact, you can even see the > [> source code that parses h264 (AVC)](https://github.com/MediaArea/MediaInfoLib/blob/master/Source/MediaInfo/Video/File_Avc.cpp)>  bitstream.

> [![mediainfo details h264 bitstream](../_resources/1e9ee78ff20ea6f9b3eba52cf597ac2d.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/mediainfo_details_1.png)

> We can also use the > [> Intel Video Pro Analyzer](https://software.intel.com/en-us/intel-video-pro-analyzer)>  which is paid but there is a free trial version which limits you to only the first 10 frames but that's okay for learning purposes.

> [![intel video pro analyzer details h264 bitstream](../_resources/50a3886376a146b91e34d8ec402882a6.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/intel-video-pro-analyzer.png)

## [(L)](https://github.com/leandromoreira/digital_video_introduction#review)Review

We'll notice that many of the **modern codecs uses this same model we learned**. In fact, let's look at the Thor video codec block diagram, it contains all the steps we studied. The idea is that you now should be able to at least understand better the innovations and papers for the area.

[![thor_codec_block_diagram](../_resources/73339d976e79f9234e36216b9bdf7862.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/thor_codec_block_diagram.png)

Previously we had calculated that we needed [139GB of storage to keep a video file with one hour at 720p resolution and 30fps](https://github.com/leandromoreira/digital_video_introduction#chroma-subsampling) if we use the techniques we learned here, like **inter and intra prediction, transform, quantization, entropy coding and other** we can achieve, assuming we are spending **0.031 bit per pixel**, the same perceivable quality video **requiring only 367.82MB vs 139GB** of store.

> We choose to use **> 0.031 bit per pixel**>  based on the example video provided here.

## [(L)](https://github.com/leandromoreira/digital_video_introduction#how-does-h265-can-achieve-better-compression-ratio-than-h264)How does H265 can achieve better compression ratio than H264?

Now that we know more about how codecs work, then it is easy to understand how new codecs are able to deliver higher resolutions with less bits.

We will compare AVC and HEVC, let's keep in mind that it is almost always a trade off between more CPU cycles (complexity) and compression rate.

HEVC has bigger and more **partitions** (and **sub-partitions**) options than AVC, more **intra predictions directions**, **improved entropy coding** and more, all these improvement made H265 capable to compress 50% more than H264.

[![h264 vs h265](../_resources/d1dc51aa234a5a54b684f3bd732fdb55.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/avc_vs_hevc.png)

# [(L)](https://github.com/leandromoreira/digital_video_introduction#online-streaming)Online streaming

## [(L)](https://github.com/leandromoreira/digital_video_introduction#general-architecture)General architecture

[![general architecture](../_resources/dc4f059ab0e9463676e1f7767d48bfc9.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/general_architecture.png)

[TODO]

## [(L)](https://github.com/leandromoreira/digital_video_introduction#progressive-download-and-adaptive-streaming)Progressive download and adaptive streaming

[![progressive download](../_resources/bfcef5e2dd52f76d626d46659f0f4962.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/progressive_download.png)

[![adaptive streaming](../_resources/de2aff3b0228587aaa0102dc7c781ce4.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/adaptive_streaming.png)

[TODO]

## [(L)](https://github.com/leandromoreira/digital_video_introduction#content-protection)Content protection

[![token protection](../_resources/6b899a6733827b754751d4197e8bdadf.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/token_protection.png)

[![drm](../_resources/1cbff6618549174c0ee52eb97f20e78b.png)](https://github.com/leandromoreira/digital_video_introduction/blob/master/i/drm.png)

[TODO]

# [(L)](https://github.com/leandromoreira/digital_video_introduction#how-to-use-jupyter)How to use jupyter

Make sure you have **docker installed** and just run ` ./s/start_jupyter.sh ` and follow the instructions on the terminal.

# [(L)](https://github.com/leandromoreira/digital_video_introduction#conferences)Conferences

- [DEMUXED](https://demuxed.com/) - you can [check the last 2 events presentations.](https://www.youtube.com/channel/UCIc_DkRxo9UgUSTvWVNCmpA).

# [(L)](https://github.com/leandromoreira/digital_video_introduction#references)References

The richest content is here, it's where all the info we saw in this text was extracted, based or inspired by. You can deepen your knowledge with these amazing links, books, videos and etc.

- https://www.coursera.org/learn/digital/
- https://storage.googleapis.com/downloads.webmproject.org/docs/vp9/vp9-bitstream-specification-v0.6-20160331-draft.pdf
- http://iphome.hhi.de/wiegand/assets/pdfs/2012_12_IEEE-HEVC-Overview.pdf
- http://phenix.int-evry.fr/jct/doc_end_user/current_document.php?id=7243
- https://medium.com/@mbebenita/av1-bitstream-analyzer-d25f1c27072b#.d5a89oxz8
- https://arxiv.org/pdf/1702.00817v1.pdf
- https://people.xiph.org/~xiphmont/demo/daala/demo1.shtml
- https://people.xiph.org/~jm/daala/revisiting/
- https://people.xiph.org/~tterribe/pubs/lca2012/auckland/intro_to_video1.pdf
- https://xiph.org/video/vid1.shtml
- https://xiph.org/video/vid2.shtml
- https://www.youtube.com/watch?v=lzPaldsmJbk
- https://fosdem.org/2017/schedule/event/om_av1/
- http://ffmpeg.org/documentation.html
- https://trac.ffmpeg.org/wiki/Debug/MacroblocksAndMotionVectors
- http://www.itu.int/rec/T-REC-H.264-201610-I
- https://www.amazon.com/Understanding-Compression-Data-Modern-Developers/dp/1491961538/ref=sr_1_1?s=books&ie=UTF8&qid=1486395327&sr=1-1
- https://www.amazon.com/H-264-Advanced-Video-Compression-Standard/dp/0470516925
- https://www.amazon.com/Practical-Guide-Video-Audio-Compression/dp/0240806301/ref=sr_1_3?s=books&ie=UTF8&qid=1486396914&sr=1-3&keywords=A+PRACTICAL+GUIDE+TO+VIDEO+AUDIO
- https://www.amazon.com/Video-Encoding-Numbers-Eliminate-Guesswork/dp/0998453005/ref=sr_1_1?s=books&ie=UTF8&qid=1486396940&sr=1-1&keywords=jan+ozer
- http://www.cambridgeincolour.com/tutorials/camera-sensors.htm
- http://www.streamingmediaglobal.com/Articles/ReadArticle.aspx?ArticleID=116505&PageNum=1
- https://en.wikipedia.org/wiki/Intra-frame_coding
- https://en.wikipedia.org/wiki/Inter_frame
- http://stackoverflow.com/questions/38094302/how-to-understand-header-of-h264
- http://gentlelogic.blogspot.com.br/2011/11/exploring-h264-part-2-h264-bitstream.html
- https://trac.ffmpeg.org/wiki/Encode/H.264
- http://inst.eecs.berkeley.edu/~ee290t/sp04/lectures/02-Motion_Compensation_girod.pdf
- http://www.itu.int/ITU-T/recommendations/rec.aspx?rec=12904&lang=en
- http://stackoverflow.com/a/24890903
- https://cardinalpeak.com/blog/worlds-smallest-h-264-encoder/
- https://cardinalpeak.com/blog/the-h-264-sequence-parameter-set/
- https://codesequoia.wordpress.com/category/video/
- https://ffmpeg.org/ffprobe.html
- http://www.biologymad.com/nervoussystem/eyenotes.htm
- https://en.wikipedia.org/wiki/Photoreceptor_cell
- https://en.wikipedia.org/wiki/Cone_cell
- https://en.wikipedia.org/wiki/Rod_cell
- https://en.wikipedia.org/wiki/Presentation_timestamp
- https://www.linkedin.com/pulse/video-streaming-methodology-reema-majumdar
- https://leandromoreira.com.br/2016/10/09/how-to-measure-video-quality-perception/
- https://www.linkedin.com/pulse/brief-history-video-codecs-yoav-nativ
- http://www.slideshare.net/vcodex/a-short-history-of-video-coding
- https://en.wikibooks.org/wiki/MeGUI/x264_Settings
- http://www.slideshare.net/vcodex/introduction-to-video-compression-13394338
- https://www.lifewire.com/cmos-image-sensor-493271
- https://www.youtube.com/watch?v=9vgtJJ2wwMA
- https://developer.android.com/guide/topics/media/media-formats.html
- https://www.encoding.com/android/
- https://developer.apple.com/library/content/technotes/tn2224/_index.html
- http://www.lighterra.com/papers/videoencodingh264/
- http://www.slideshare.net/ManoharKuse/hevc-intra-coding
- http://www.slideshare.net/mwalendo/h264vs-hevc
- http://www.slideshare.net/rvarun7777/final-seminar-46117193
- http://x265.org/hevc-h265/
- http://www.compression.ru/video/codec_comparison/h264_2012/mpeg4_avc_h264_video_codecs_comparison.pdf
- http://vanseodesign.com/web-design/color-luminance/
- https://en.wikipedia.org/wiki/AOMedia_Video_1
- https://www.vcodex.com/h264avc-intra-precition/
- http://bbb3d.renderfarming.net/download.html
- http://www.slideshare.net/vcodex/a-short-history-of-video-coding
- https://www.iem.thm.de/telekom-labor/zinke/mk/mpeg2beg/whatisit.htm
- https://sites.google.com/site/linuxencoding/x264-ffmpeg-mapping
- https://www.encoding.com/http-live-streaming-hls/
- https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming
- http://www.adobe.com/devnet/adobe-media-server/articles/h264_encoding.html
- https://www.youtube.com/watch?v=Lto-ajuqW3w&list=PLzH6n4zXuckpKAj1_88VS-8Z6yn9zX_P6
- https://www.youtube.com/watch?v=LFXN9PiOGtY
- https://github.com/leandromoreira/encoding101
- https://cardinalpeak.com/blog/the-h-264-sequence-parameter-set/
- https://cardinalpeak.com/blog/worlds-smallest-h-264-encoder/
- https://tools.ietf.org/html/draft-fuldseth-netvc-thor-03
- https://prezi.com/8m7thtvl4ywr/mp3-and-aac-explained/
- http://www.slideshare.net/MadhawaKasun/audio-compression-23398426
- http://techblog.netflix.com/2016/08/a-large-scale-comparison-of-x264-x265.html
- http://yumichan.net/video-processing/video-compression/introduction-to-h264-nal-unit/
- http://www.springer.com/cda/content/document/cda_downloaddocument/9783642147029-c1.pdf
- http://www.red.com/learn/red-101/video-chroma-subsampling
- http://www.streamingmedia.com/Articles/Editorial/Featured-Articles/A-Progress-Report-The-Alliance-for-Open-Media-and-the-AV1-Codec-110383.aspx
- http://www.explainthatstuff.com/digitalcameras.html
- https://www.youtube.com/watch?v=LWxu4rkZBLw
- http://www.csc.villanova.edu/~rschumey/csc4800/dct.html
- https://en.wikipedia.org/wiki/File:H.264_block_diagram_with_quality_score.jpg
- https://softwaredevelopmentperestroika.wordpress.com/2014/02/11/image-processing-with-python-numpy-scipy-image-convolution/
- http://stackoverflow.com/a/24890903
- [http://www.hkvstar.com](http://www.hkvstar.com/)
- http://www.hometheatersound.com/
- http://web.ece.ucdavis.edu/cerl/ReliableJPEG/Cung/jpeg.html
- https://en.wikipedia.org/wiki/Pixel_aspect_ratio
- https://it.wikipedia.org/wiki/File:Pixel_geometry_01_Pengo.jpg
- https://en.wikipedia.org/wiki/Chroma_subsampling#/media/File:Colorcomp.jpg