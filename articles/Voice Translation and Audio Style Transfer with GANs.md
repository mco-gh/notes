Voice Translation and Audio Style Transfer with GANs

# Introduction

We have all heard about image **style transfer**: extracting the style from a famous painting and applying it to another image is a task that has been achcieved with a number of different methods. **Generative Adversarial Networks** (GANs in short) are also being used on images for generation, image-to-image translation and more.

![1*Y5iiD4zYn6NyyQVaPO9lnw.jpeg](../_resources/2ec5af2747a85b3d21bba20914f452eb.jpg)
![1*Y5iiD4zYn6NyyQVaPO9lnw.jpeg](../_resources/c55dff1433a85e8ec6d39ac4c77553f3.jpg)
Examples of image style transfer

But what about sound? On the surface, you might think that **audio is completely different from images**, and that all the different techniques that have been explored for image-related tasks can’t also be applied to sounds. But what if we could find a way to **convert audio signals** to image-like 2-dimensional representations?

As a matter of fact, yes we can! This kind of sound representation is what we call “**Spectrogram**”, and it is the key that will allow us to make use of algorithms specifically designed to work with images for our audio-related task.

![1*W2cxJev00kJJ2HIb1YGZFA.png](../_resources/e59a15935bf12eb52aba2e55c6055996.png)
![1*W2cxJev00kJJ2HIb1YGZFA.png](../_resources/5b673125ebf4d24249d8721bd5819914.png)

Spectrogram ([source](https://towardsdatascience.com/getting-to-know-the-mel-spectrogram-31bca3e2d9d0))

# Spectrograms

If you are new to the world of audio processing, you may be unfamiliar with what a spectrogram really is. Given a time-domain signal (1 dimension) we want to obtain a **time-frequency 2-dimensional representation**. To achieve that, we apply the Short-Time **Fourier Transform** (STFT) with a window of a certain length on the audio signal, only considering the squared magnitude of the result.

![1*LamxVKUATPaXkz_0mKH2rw.png](../_resources/cb856ab4f3b812200c2c4bc123f6167d.jpg)
![1*D9opNS4IOTHcS8iMNE_uPA.gif](../_resources/9863a74b24ca3f6df9baeed0a7de115c.gif)

Incredible illustration of how Time and Frequency correlate from the [MelNet paper page](https://sjvasquez.github.io/blog/melnet/)

In simpler terms, we divide our original** waveform** signal into chunks that overlap with one another, extract the magnitude of the **frequency** in the chunk (with a Fourier Transform), and each resulting vector is going to represent a column of our final spectrogram. The x axis of the spectrogram stands for **time**, while the y axis represents the **frequency**.

To make these spectrograms even more useful for our task, we convert each “pixel” (or magnitude value) to be in the **decibel scale**, taking the log of each value. Finally, we convert spectrograms to the **mel scale**, applying a mel filter bank, resulting in what are known as “**mel-spectrograms**”.

![1*lentsUBDgplmmVttKYIoyw.png](../_resources/069b8f2e94d4abfd5b4c815cba721cfa.png)
![1*lentsUBDgplmmVttKYIoyw.png](../_resources/aa145a89a9f768159a90bbcc8dafbad8.png)
Examples of mel-spectrograms with log-amplitude

This allows us to make the spectrogram representations **more sensible to our human understanding of sound**, highlighting the amplitudes and frequencies that us humans are more prone to hearing.

It is also extremely important to note that spectrograms can be** turned back **into “audible” **waveform** data: it won’t be a **perfect reconstruction** (phase information is missing in our magnitude spectrograms) but thanks to an algorithm called **Griffin-Lim** we are able to approximate phase and **recreate **realisticly sounding audio.

# Our Task

Now that we know how to represent sounds as images, let’s have some fun.

In this article I will explain how to build and train a system capable of performing **voice conversion** and any other kind of **audio style transfer** (for example converting a music genre to another). The method is heavily inspired by recent research in **image-to-image translation** using Generative Adversarial Networks, with the main difference consisting in applying all these techniques to **audio data**. As a bonus feature, we will be able to translate samples of **arbitrary length**, which is something that we don’t see very often in GAN systems.

To get you a bit hyped up for what you are about to learn, here is a **demo video **of the results we can achieve with this method.

In the demo video, you can listen to different **voice translation** examples and also a couple of **music genre conversions**, specifically from Jazz to Classical music. Sounds pretty good, doesn’t it?

# Choosing the Architecture

There are a number of different architectures from the computer vision world that are used for image-to-image translation, which is the task that we want to achieve with our **spectrogram representations** of audio (let’s say speech).

Image-to-image translation consists in **converting an image** from a domain A (pictures of cats for example) to a different domain B (pictures of dogs), while **keeping content information** from the original picture (the expression and pose of the cat). Our task is practically **the same**: we want to translate from speaker A to speaker B, while keeping the same **linguistic information** from speaker A (the generated speech should contain the **same words** as the original speech from speaker A).

![1*YMDlaxf_daCdyFy8w6swoQ.png](../_resources/be9d0c379cca4fed0659ed6f6f4c2a22.jpg)
![1*EWWm148aWAh7IX-9k2aS9g.jpeg](../_resources/a1a2392b2b82c85ab0d14b0d16e4a07c.jpg)
CycleGAN architecture

The **most famous** GAN architecture built for this goal may be **CycleGAN**, introduced in 2017 and widely used since then. While CycleGAN is very successful at translating between **similar domains** (similar shapes and contexts), such as from horses to zebras or from apples to oranges, it falls short when rained on very diverse domains, like from fishes to birds or from apples to carrots.

The cause of this **shortcoming** is the fact that CycleGAN heavily relies on **pixel-wise losses**, or in other words, its loss tends to minimize differences in pixel values of real and generated images: intuitively, when converting an image of an object (an apple for example) to a substantially different domain (carrot) we need to change the **main shape** of the original object, and **CycleGAN can’t help us** in this case.

![1*e1BweBQ8XeOTJWQoac1PpQ.png](../_resources/70c42f3ac415a55d96193fa38383e7be.png)
![1*e1BweBQ8XeOTJWQoac1PpQ.png](../_resources/7b507078143c5de39325642869cd4fa5.png)
CycleGAN translation example. (Zebra to Horse)

Spectrograms of speeches from different people (or spectrograms of musical pieces of different genres) can be very **visually different** from one another: thus we need to find a more general approach to the problem, one that does not involve being constrained by translating between visually similar domains.

![1*lentsUBDgplmmVttKYIoyw.png](../_resources/069b8f2e94d4abfd5b4c815cba721cfa.png)
![1*lentsUBDgplmmVttKYIoyw.png](../_resources/aa145a89a9f768159a90bbcc8dafbad8.png)

Spectrograms of different speakers or different music genres can be very visually different

# TraVeLGAN: our Solution

Originally introduced here, the **TraVeLGAN** (Transformation Vector Learning GAN) aims at solving exactly our problem.

![1*OBo-rvuda7bbHxprDv0lDg.png](../_resources/167bc3d531445ae09f329b91fe7c3392.png)
![1*OBo-rvuda7bbHxprDv0lDg.png](../_resources/381a3eaefb9d6bb6db1f1a6b0efd250e.png)
Examples of TraVeLGAN image-to-image translations with very different domains

In addition to a Generator and a Discriminator (or Critic), TraVeLGAN introduces a **Siamese network** (a network that encodes images into latent vectors) to allow translations between **substantially different domains** keeping a content relationship between the original and converted samples.

Let’s learn how TraVeLGAN exactly works.
![1*LsF_UEbfB7e1b3raB3XTmw.png](../_resources/bef604c51c4ed32dc2a55ffa0a5c014b.png)
![1*LsF_UEbfB7e1b3raB3XTmw.png](../_resources/4f70d4bc790f4913eb1640a341d1f3c2.png)
TraVeLGAN architecture

Our goal is to find a way to keep a **relationship** between the original and generated samples without relying on pixel-wise losses (such as the cycle-consistency constraint in CycleGAN), that would limit translations between visually similar domains. Thus, if we **encode** the images (or spectrograms) into **vectors** that capture their content information in an **organized latent space** we are able to maintain a relationship between these vectors instead of the whole images.

That’s exactly what a **siamese** network allows us to achieve. Originally used for the task of face recognition, the siamese network takes an **image as input **and **outputs a single vector** of length *vec_len. *Specifying with a loss function which image **encodings should be close** (images of the same face for example) in the vector space and which ones should be **far apart** (images of different faces) we are able to **organize the latent space** and make it useful for our goal.

![1*bLRvkrcYgoQWKQfqXWbfZg.jpeg](../_resources/e60b250520b1520b3d4e16ae151685c8.jpg)
![1*bLRvkrcYgoQWKQfqXWbfZg.jpeg](../_resources/984d9aeba5ae5369c242e4ae67d114c4.jpg)
The Siamese network encodes images into vectors

More specifically, we aim at keeping the **transformation vectors**  **between pairs of encodings** equal: this seems an extremely difficult concept to comprehend, but it is in fact quite easily **understandable**.

With *G(X)* as the translated image *X* (output of the generator), *S(X) *as the vector encoding of *X *and *A1, A2 *two images from the source domain *A*, the network must encode vectors such as:

***(S(A1)-S(A2)) =* (*S(G(A1)-S(G(A2)))***

In this way the transformation vector that connects encodings of a pair of source images **must be equal** to the transformation vector between the same pair translated by the generator.

This allows to **preserve semantic information** (differently from CycleGAN that preserves more geometric content information with its cycle-consistency constraint) in the translation, allowing the constraining of **more “abstract” relationships** between images of different domains.

Formally, to keep content information in the translation we will **minimize the euclidean distance and the cosine similarity** between the two transformation vectors, so that both **angle** and **magnitude** of the vectors get preserved.

![1*EWWm148aWAh7IX-9k2aS9g.jpeg](../_resources/01736ba93cee47379d5ea812c18740c4.png)
![1*LamxVKUATPaXkz_0mKH2rw.png](../_resources/94ffdeaa1996715e1cdd0e2a9e9f5f4e.png)
Formal TraVeL loss

Furthermore, it is important to clarify that both the **generator** and the **siamese** network **must cooperate** to achieve this objective. More specifically, the gradients of the TraVeL loss get **backpropagated** through **both of the networks** and their weights get updated accordingly. Thus, while the discriminator and the generator have an **adversarial objective** (they challenge one another to reach their goal), the siamese and the generator **help each other**, cooperating under the same rules.

In addition to this “content” loss, the generator will learn how to generate realistic samples thanks to a traditional **adversarial loss** (in my experiments I used the hinge loss).

If you are new to GANs and how they work, or if you want to **dive a little deeper **into how to preserve content information with a latent space, I recommend you **check out **[**my article** here](https://towardsdatascience.com/a-new-way-to-look-at-gans-7c6b6e6e9737) on how to apply the same techniques on a simple image-to-image translation task.

# Translating Audio Signals of Arbitrary Length

Now that we have explored a method that allows us to **preserve content **information in the translation, we need to understand how we can make the generator convert **samples** (spectrograms) that are **arbitrarily long**, without putting extra work on computation and training times.

Let’s say we have an audio signal: “extracting” the mel-spectrogram of the signal we obtain an **image with a single channel** (different from traditional 3 channels RGB images) with a **determined height**  *H* (that depends on the hop-size used for the STFT) and a **width**  *X* that **depends** on the original length of the audio sample.

However, working with images that have **variable dimensions** is known to be a **challenging** task, especially if we do not decide those dimensions beforehand. That’s why we will **split** all the spectrograms (of shape *XxH* with *X* that varies) into** chunks** with a **determined width**, let’s say *L*. Perfect! Our dataset now consists of source and target spectrograms with **known dimensions** (*LxH*), and we are ready to proceed to the next step.

![1*lentsUBDgplmmVttKYIoyw.png](../_resources/069b8f2e94d4abfd5b4c815cba721cfa.png)
![1*lentsUBDgplmmVttKYIoyw.png](../_resources/aa145a89a9f768159a90bbcc8dafbad8.png)
Each spectrogram in the dataset has a fixed height H and width L

Before creating our generator *G*, we need to specify the **dimensions of its inputs**, which in our case will be *(L/2)xH*. In other words G will accept spectrograms that have **half the width** of those in our dataset. Why? Because in this way we will be able to make G translate the **whole original**  *XxH*  **spectrograms** that we previously split up. Let’s discover how.

Our **training pipeline** will consist in the following actions:

1. **Split** the source *LxH* spectrograms** in half**, obtaining *(L/2)xH *spectrograms

2. **Feed the pairs** of halves to the generator and get the **translated pairs **as outputs

3. **Concatenate** the translated halves back to their **original shape** (*LxH*)

4. **Feed** the **translated** and the **target**  *LxH* spectrograms to the discriminator, making it **distinguish** one from the other and allowing the **adversarial training**.

![1*nxIk9RINFbJIia91ps5wTQ.png](../_resources/b0cf97fb93f5db03a70a55eb6dc01cab.png)
![1*nxIk9RINFbJIia91ps5wTQ.png](../_resources/3afc47616ad5b54e318af9e4d2e9b280.png)
Illustration of the training pipeline: splitting, converting and concatenating.

Making the discriminator inspect the **concatenated “fake” spectrograms** and **comparing** them to the **“real”** target ones forces the generator to generate samples that **when concatenated** together result in a **realistic **spectrogram.

In other words the translated *(L/2)xH* samples must not present any **discontinuity** on the edges that would make them **look unrealistic** to the discriminator. Thus, this important **constraint **on the generator is what allows us to translate audio signals of any length from one domain to the other.

After training, when wanting to **translate** an **arbitrary** spectrogram of shape *XxH* where *X*  **varies** and is given by the length of the original audio signal, this is what we will need to do:

1. **Split** the *XxH* spectrogram into *(L/2)xH* chunks, using padding if *X* is not perfectly divisible by *L/2*

2. **Feed** each *(L/2)xH* sample to the generator for translation

3. **Concatenate** the translated samples into the original *XxH* shape, cutting out the extra if padding was used.

The final translated sample, after turning it back to **waveform** with the Griffin-Lim algorithm, should not **present**  **discontinuities** and should present the **same style** as the target domain (a particular voice or music genre). Easy, isn’t it?

![1*UK4-kHx9vEwpPVuXkCysMg.png](../_resources/0c931b0a33ad54cf6a2bd1742b067039.png)
![1*UK4-kHx9vEwpPVuXkCysMg.png](../_resources/aaf2c75ab0eb39aa9d3c6c71058ff504.png)

Examples of source and converted spectrograms: the concatenated samples do not present discontinuities

# Putting Everything Together

We have previously learned how we can **preserve content** from the source audio sample (in the case of speech it would be the some **verbal information**, in the case of music it would be the particular **melody** of a song) without the constraint of translating between **visually similar domains** (spectrograms of different voices or music genres can be extremely visually **different**) and a **simple but effective** technique that allows us to convert samples of **arbitrary length**.

Now it is finally time to put everything **together**.
This is an **extract** from my paper that presents this technique:
![1*nxIk9RINFbJIia91ps5wTQ.png](../_resources/b0cf97fb93f5db03a70a55eb6dc01cab.png)
![1*nxIk9RINFbJIia91ps5wTQ.png](../_resources/3afc47616ad5b54e318af9e4d2e9b280.png)

Putting everything together: the siamese network helps preserve content keeping vector arithmetic between source and converted samples

> MelGAN-VC training procedure. We split spectrogram samples, feed them to the generator G, concatenate them back together and feed the resulting samples to the discriminator D to allow translation of samples of arbitrary length without discrepancies. We add a siamese network S to the traditional generator-discriminator GAN architecture to preserve vector arithmetic in latent space and thus have a constraint on low-level content in the translation. An optional identity mapping constraint is added in tasks which also need a preservation of high-level information (linguistic information in the case of voice translation).

Furthermore, we must add a **margin loss** for the siamese network to avoid it from **degenerating** into learning a **trivial function **to satisfy its objective. The margin loss keeps all the vectors produced by S far from one another, so that the network can’t associate the same exact vector to every input and must **learn meaningful relationships** creating a useful latent space.

![1*D9opNS4IOTHcS8iMNE_uPA.gif](../_resources/81c4356bc63c179d3508276164824f9f.png)
![1*YMDlaxf_daCdyFy8w6swoQ.png](../_resources/a3361c81a9506b3fb7c64e38efae6e88.png)
where delta is a fixed value and t is the transformation vector
Finally, here are the **formal losses** used to train the three networks:
![1*KSTLykfvvqcVdJfB49SljQ.png](../_resources/1f9b3616ffb881f0d2e815bdd35f594f.png)
![1*KSTLykfvvqcVdJfB49SljQ.png](../_resources/bd30d2169ed87103567d58093bf260b9.png)
Final losses for generator G, discriminator D, siamese network S

It is important to note that the added **identity constraint** (mean squared error between samples from the target domain and those same samples translated by the generator) is only useful in case of **voice translation**, where linguistic information must be preserved and where our **content loss **(based on the vector outputs of the siamese network) **struggles** to capture those **high level** information.

I recommend and invite you to read [**my full paper**](https://arxiv.org/abs/1910.03713) if you’re looking for more information on this particular technique or if you prefer a more **formal and methodical** explanation.

# Conclusion

Today we have learned how to perform **voice translation** and **audio style transfer** (such as music genre conversion) using a deep convolutional neural network architecture and a couple of **tricks and techniques** to achieve **realistic** translations on **arbitrarily long** audio samples.

We now know that we are able to **leverage** a large part of the **recent research** on deep learning for **computer vision** applications to also solve tasks related to **audio signals**, thanks to the image-equivalent spectrogram representation.

Finally, I would like to conclude by acknowledging the fact that **misusing** this and other techniques for **badly intentioned goals** is possible, especially in the case of **voice translation**. With the **rise** of powerful machine learning methods to create **realistic fake data** we should all be very **aware and cautious** when exploring and using this kind of algorithms: and while **the research won’t stop and shouldn’t be stopped**, we should also allocate resources and look into how to **detect the fake data** that we helped creating.

Thank you so much for **your precious attention**, have fun!

P.S. If you’re **interested in GANs** and GAN related **out-of-the-box ideas** and applications, you should also **check out**:

[***10 Lessons I Learned Training GANs for a Year***](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)***  ****(if you’re interested in tips and tricks to help you in the super challenging task that is training GANs)*

[***Style Transfer with GANs on HD Images***](https://towardsdatascience.com/style-transfer-with-gans-on-hd-images-88e8efcf3716)***  ****(where I use a similar technique to allow style transfer of large images with very little computation resources)*

[***A New Way to look at GANs***](https://towardsdatascience.com/a-new-way-to-look-at-gans-7c6b6e6e9737)***  ****(where I explore in great detail how a latent space works and how it can be leveraged for a image-to-image translation task)*

[***Synthesizing Audio with Generative Adversarial Networks***](https://towardsdatascience.com/synthesizing-audio-with-generative-adversarial-networks-8e0308184edd)***  ****(where I explore a paper that proposes the use of convolutional GANs to generate audio using raw waveform data and 1-dimensional convolutions)*