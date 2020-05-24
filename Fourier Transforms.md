Fourier Transforms

![](../_resources/6c9a4cd6c197a8ba77417a32cc4c02b3.png)

# An Interactive Introduction to Fourier Transforms

Jez Swanson

Fourier transforms are a tool used in a whole bunch of different things. This is a explanation of what a Fourier transform does, and some different ways it can useful. And how you can make pretty things with it, like this thing:

![](../_resources/f8a42a89c3e493bc41651889ea63cfd2.png)

I'm going to explain how that animation works, and along the way explain Fourier transforms!

By the end you should have a good idea about

- What a Fourier transform does
- Some practical uses of Fourier transforms
- Some pointless but cool uses of Fourier transforms

We're going to leave the mathematics and equations out of it for now. There's a bunch of interesting maths behind it, but it's better to start with what it actually does, and why you'd want to use it first. If you want to know more about the how, there's some further reading suggestions below!

## So what is this thing?

Put simply, the Fourier transform is a way of splitting something up into a bunch of sine waves. As usual, the name comes from some person who lived a long time ago called Fourier.

Let’s start with some simple examples and work our way up. First up we're going to look at waves - patterns that repeat over time.

Here’s an example wave:
![](../_resources/fb90d4068db9adf56cf1f4e6f1b0a4b1.png)

This wavy pattern here can be split up into sine waves. That is, when we add up the two sine waves we get back the original wave.

![](../_resources/b56e46864134aa7236c41716f983be98.png)

The Fourier transform is a way for us to take the combined wave, and get each of the sine waves back out. In this example, you can almost do it in your head, just by looking at the original wave.

Why? Turns out a lot of things in the real world interact based on these sine waves. We usually call them the wave's frequencies.

The most obvious example is sound – when we hear a sound, we don’t hear that squiggly line, but we hear the different frequencies of the sine waves that make up the sound.

Being able to split them up on a computer can give us an understanding of what a person actually hears. We can understand how high or low a sound is, or figure out what note it is.

We can also use this process on waves that don't look like they're made of sine waves.

Let's take a look at this guy. It’s called a square wave.
![](../_resources/c53f05b5a1c5e151a26f257490222917.png)
It might not look like it, but it also can be split up into sine waves.
![](../_resources/46244898bd37e22f828865f13936eae4.png)

We need a lot of them this time – technically an infinite amount to perfectly represent it. As we add up more and more sine waves the pattern gets closer and closer to the square wave we started with.

![](../_resources/6be35524bdfad49d4505281a986da6f3.png)

*Drag the slider above to play with how many sine waves there are.*

Visually, you'll notice that actually the first few sine waves are the ones that make the biggest difference. With the slider halfway, we have the general shape of the wave, but it's all wiggly. We just need the rest of the small ones to make the wigglyness flatten out.

When you listen to the wave, you'll hear the sound get lower, because we're removing the higher frequencies.

This process works like that for any repeating line. Give it a go, try draw your own!

 ![](../_resources/95a6593f32acd19d0ea5747788fd64ee.png)
Draw here!
![](../_resources/d846a03dd368a516d8ee7d223ebb1b8f.png)

*Move the slider to see how as we add move sine waves, it gets closer and closer to your drawing*

Again, aside from the extra wigglyness, the wave looks pretty similar with just half of the sine waves.

We can actually use the fact that the wave is pretty similar to our advantage. By using a Fourier transform, we can get the important parts of a sound, and only store those to end up with something that's pretty close to the original sound.

Normally on a computer we store a wave as a series of points.
![](../_resources/befe0aa40f58e47c18c345e688b7a0c0.png)

What we can do instead is represent it as a bunch of sine waves. Then we can compress the sound by ignoring the smaller frequencies. Our end result won't be the same, but it'll sound pretty similar to a person.

![](../_resources/99e75faf24a9936f99e5692b6959bc50.png)

This is essentially what MP3s do, except they're more clever about which frequencies they keep and which ones they throw away.

So in this case, we can use Fourier transforms to get an understanding of the fundamental properties of a wave, and then we can use that for things like compression.

Ok, now let's dig more into the Fourier transform. This next part looks cool, but also gives you a bit more understanding of what the Fourier transform does. But mostly looks cool.

## Epicycles

Now at the start, I said it splits things into sine waves. The thing is, the sine waves it creates are not just regular sine waves, but they’re 3D. You could call them "complex sinusoids". Or just "spirals".

![](../_resources/ea0819303b7c724681690432197743d8.png)

If we take a look from the side, they look like sine waves. From front on, though, these look like circles.

![](../_resources/54817e039433204088339320fc836f63.png)

So far everything we’ve been doing has only required the regular 2D sine waves. When we do a Fourier transform on 2D waves, the complex parts cancel out so we just end up with sine waves.

But we can use the 3D sine waves to make something fun looking like this:
![](../_resources/58a2cd7c60dad2c6618c681948e717ed.png)
What’s going on here?

Well, we can think of the drawing as a 3D shape because of the way it moves around in time. If you imagine the hand being drawn by a person, the three dimensions represent where the tip of their pencil is at that moment. The x and y dimensions tell us the position, and then the time dimension is the time at that moment.

![](../_resources/9297679024ad38b815a78e71e31f8d01.png)

Now that we have a 3D pattern, we can't use the regular 2D sine waves to represent it. No matter how many of the 2D sine waves we add up, we'll never get something 3D. So we need something else.

What we can use is the 3D spiral sine waves from before. If we add up lots of those, we can get something that looks like our 3D pattern.

Remember, these waves look like circles when we look at them from front on. The name for the pattern of a circle moving around another circle is an epicycle.

![](../_resources/8606041452e0c9b4d9a2959062334e8d.png)

*Use the slider above to control how many circles there are.*

Like before, we get a pretty good approximation of our pattern with just a few circles. Because this is a fairly simple shape, all the last ones do is make the edges a little sharper.

All this applies to any drawing, really! Now it’s your chance to play around with it.

 ![](../_resources/d846a03dd368a516d8ee7d223ebb1b8f.png)
Draw here!

![](../_resources/d846a03dd368a516d8ee7d223ebb1b8f.png)

*Use the slider to control how many circles are used for your drawing*

Again, you'll see for most shapes, we can approximate them fairly well with just a small number of circles, instead of saving all the points.

Can we use this for real data? Well, we could! In reality we have another data format called SVG, which probably does a better job for the types of shapes we tend to create. So for the moment, this is really just for making cool little gifs.

![](:/4a372eff188ad7e1b3868e1f10c0cb0b)
There is another type of visual data that does use Fourier transforms, however.

## JPEGs

Did you know Fourier transforms can also be used on images? In fact, we use it all the time, because that's how JPEGs work! We're applying the same principles to images – splitting up something into a bunch of sine waves, and then only storing the important ones.

Now we're dealing with images, we need a different type of sine wave. We need to have something that no matter what image we have, we can add up a bunch of these sine waves to get back to our original image.

To do that, each of our sine waves will be images too. Instead of a wave that's a line, we now have images with black and white sections. To represent the size of a wave, each image will have more or less contrast.

We can also use these to represent color in the same way, but let's start with black-and-white images for now. To represent colorless images, we need some horizontal wave images,

![](../_resources/823f63f7dbc3f13d70e17722edac6145.png)
Along with some vertical wave images.
![](../_resources/2d39fc173d9089e3cf0aff2b3367ce05.png)

By themselves, just horizontal and vertical images aren't enough to represent the types of images we get. We also need some extra ones that you get by multiplying the two together.

![](../_resources/2d39fc173d9089e3cf0aff2b3367ce05.png)
×
![](../_resources/823f63f7dbc3f13d70e17722edac6145.png)
=
![](../_resources/74e3d6316bee251efc0a3fbea8971cb6.png)
For an 8x8 image, here are all the images we need.

 ![](../_resources/404cee9cb313d72d51b02bcdfbcc3433.png)  ![](../_resources/2d39fc173d9089e3cf0aff2b3367ce05.png)  ![](../_resources/1e550b041aed3395bac7ec37dcedc4b7.png)  ![](../_resources/6d9323902372431348ae12113a36e5d8.png)  ![](../_resources/15693dacbdc0007d751072e5dddd2246.png)  ![](../_resources/695a34926b1aa57820924a7f77288e1e.png)  ![](../_resources/1aef12418ec2eb740617b02a727b641c.png)  ![](../_resources/7b6169c790607d7769efbfcb1f933ebb.png)  ![](../_resources/823f63f7dbc3f13d70e17722edac6145.png)  ![](../_resources/74e3d6316bee251efc0a3fbea8971cb6.png)  ![](../_resources/7bbc338c8f4f63fb86319c1e762b02fe.png)  ![](../_resources/77102f18b819610bc45acc159cee3a13.png)  ![](../_resources/8a373b249a5aaca97c26b08b1c8f2ec1.png)  ![](../_resources/a2f1767498814b31b381cb4df03d9263.png)  ![](:/dc85df9f5c9d16e364ab4726a4a34340)  ![](../_resources/18062a2595d733afb2a76010b35313be.png)  ![](../_resources/4289f6e0cca895d93e3540b130f21426.png)  ![](../_resources/ceff7bc1b55e18bda9d9d14ce8dd752b.png)  ![](../_resources/fd063bac478ae26f9748df1392699f90.png)  ![](../_resources/c037fb44d2c17dc49b2661b747cae75d.png)  ![](../_resources/5f13e232be689239fa6420f1ea67fa19.png)  ![](../_resources/a32e4363ec1b9b3f200362dc04878755.png)  ![](../_resources/ec837aa7c36d7242e9ac65f1fc2485e2.png)  ![](../_resources/7ae8a9d30925bfb09d24142aee96555a.png)  ![](../_resources/594d7cb0e9fbd6550bc9af8283d10e97.png)  ![](../_resources/d701004db241eca0ed86ad888db3f1c3.png)  ![](../_resources/bc337c03b46f6497cb5feb6e585232e1.png)  ![](../_resources/33d8f02d83d59102b2d9021073a2a345.png)  ![](../_resources/0abafb33691279d60011060856b25474.png)  ![](../_resources/b754c6c81c80dc00f7f984bf250c66e1.png)  ![](../_resources/002b1650bc55dc3c17994fad2834b397.png)  ![](../_resources/434d36c40f72ec0d4044458c0748142c.png)  ![](../_resources/f19bb4eab1afe834d9717cceba988b1d.png)  ![](../_resources/5d20048ebfcd0dc328d5ec65a79264c5.png)  ![](../_resources/ce48ef972c208a4931f2c74c28459fc8.png)  ![](../_resources/777ffebb0b6f2c62db21a1def474acfc.png)  ![](../_resources/84a5f71f3b03d8627875a4c10b1a3707.png)  ![](../_resources/9467c1e489f5764db0fa113ec1cf439c.png)  ![](../_resources/cb81ea9faacb2768ca2d9244180456be.png)  ![](../_resources/6bcb7df384fd1c76af20cf1d4bf8058f.png)  ![](../_resources/2f1b1c7e9a53c382e10d23f0b7b19502.png)  ![](../_resources/4a5cc4ae3ac01e4d34f40181763aae72.png)  ![](../_resources/d08d9e50daf91c8df47985b8213102ce.png)  ![](../_resources/5e98f07a1f1116b3546d8cb1043fa806.png)  ![](../_resources/adf88bf118289310cbf00d93a49d4984.png)  ![](../_resources/fdc127aa76840a8a642cd90d24832ea9.png)  ![](../_resources/d8e475339e8dffbb2ff353b885002794.png)  ![](../_resources/c2671f61c62cada42e848c6b62c4b50f.png)  ![](../_resources/885df39b6bdf96ab719a6e0b38b11e6b.png)  ![](../_resources/f89f86f1e0cf231c60b763ddc2e55144.png)  ![](../_resources/59736b38e6aac92a274d5ef430efcecc.png)  ![](../_resources/fbe971cd2584175b1a59b60c7f65b3e7.png)  ![](../_resources/d7817adc45661f1b7b3127fe36cadfcc.png)  ![](../_resources/b24f7d6ac95ee8277fb6fdb90e894335.png)  ![](../_resources/ddb1ba8235954a413a0a0a25f9e84117.png)  ![](../_resources/ce2a540caeb6c9e913ee3944950a110e.png)  ![](../_resources/5b2900a6d440a7e5e0a267e69a3ac84b.png)  ![](../_resources/3f48653d21f6dc3d6f76199892b416b8.png)  ![](../_resources/aa5772885662a6cb188a5cad3ec4afa6.png)  ![](../_resources/f824f3968a8fa61977c03e772828a9b8.png)  ![](../_resources/919c4f1d217913ba139685ed70f5ab1c.png)  ![](../_resources/d7c9ab73cba9e802b75553d910bbb1fc.png)  ![](../_resources/dced84896bcec68536624b94f9dceeea.png)  ![](../_resources/53930c97edb9372a71afc4269cf06fb4.png)

If we take the images, adjust their contrast to the right amount, and then add them up we can create any image.

Let's start with this letter 'A'. It's pretty small, but we need it to be small otherwise we'll end up with too many other images.

![](../_resources/03801eef5991a2f98f65068796669549.png)

As we add more and more of these images, we end up with something that becomes closer and closer to the actual image. But I think you'll see the pattern here, as we get a reasonable approximation with just a few of them.

![](../_resources/53d210315b048ffc3a85bb13a8c63ead.png)

 ![](../_resources/92cf396943c5dd1b2981dfeb71755b4a.png)  ![](../_resources/80365ef1c5fd5069024a9cf2bd4f4495.png)  ![](../_resources/f835ee8ef8ddefca97c9bc628182174c.png)  ![](../_resources/6314909f1562e4288cdd1d785574fa71.png)  ![](../_resources/b00574f73ff0556b80476a13fb1c28c1.png)  ![](../_resources/f5a40118615cfd5c3c5fcffe6c2cb24c.png)  ![](../_resources/8c68d2c9f1406030256d51ea7245b66c.png)  ![](../_resources/14c4f01ada6f8665ab63d8cfd1b5c937.png)  ![](../_resources/eb111d7aecd4950c91a01f0bf14bacb8.png)  ![](../_resources/1c8bb3e21e4a34e6da3afc1f4b576630.png)  ![](../_resources/f2a997bd49883e5200210dce5e333554.png)  ![](../_resources/92ae586b072a0f35dbcf4ddd735c78ba.png)  ![](../_resources/677e9b9bfe58b5546943ba5069358281.png)  ![](../_resources/9258920e36a5bb628de8efd32ba7c0d5.png)  ![](../_resources/1454bf7c1e7631673f8bf088cd4ad18e.png)  ![](../_resources/1c74f564cc1820568ea579db4f7b8fd0.png)  ![](../_resources/cff4eb592caa58b77eb330ad5b933fc0.png)  ![](../_resources/bbc9b4c5e7310d77940f57adfa8fbe46.png)  ![](../_resources/d7ec5e878412663ece5348c896d40021.png)  ![close_icon.png](../_resources/ef520a4d650d4b7e0ca356ef825244ef.png)  ![](../_resources/a185730095b569c6d0e77dc37637418e.png)  ![](../_resources/f9c67461788c12f38d77112afa7ff822.png)  ![](../_resources/140a076dc62e61be3ede606a3bcb9892.png)  ![](../_resources/f929ab442c0dd031c3aefb2753892922.png)  ![](../_resources/21e8cd0d6e7c230aa87996ccc1563179.png)  ![](../_resources/efbe6e241fa75de5fc15980170cc7d21.png)  ![](../_resources/49d36c0cd2a6901757aab7f11b6778e0.png)  ![](../_resources/10a3418c56fafce364b64f6851d9c2d5.png)  ![](../_resources/bd2aaac052e3dd31f955c67ceb9662c3.png)  ![](../_resources/4b827bcc23edf0b7905e47a9062f3cfd.png)  ![](../_resources/7fa659025eb8f7c9a947310ef5b867df.png)  ![](../_resources/2148550e1f8d254263d86bc24c9b9171.png)  ![](../_resources/6fb655ac087eea6fb97c9b3d5da0e071.png)  ![](../_resources/666289d67b66d4067e64349cac511fcb.png)  ![](../_resources/fb36c4ed9075ff79e415ffb23c0c22ec.png)  ![](../_resources/4024fcfd6ce41417deaa9db735d9842b.png)  ![](../_resources/2fb9a639d20d26ab80a7324ca5335b5c.png)  ![](../_resources/7e9060abe288b97b16b62e985ec80831.png)  ![](../_resources/90f995e4e7e7b0d3b014e121bfb84afe.png)  ![](../_resources/f2dbd310cb89aac6bb9ebc8a7a5ad0b2.png)  ![](../_resources/56258c26385471618b2661424ebef179.png)  ![](../_resources/b7a1eca259e4bd3f85d1e52eb88ac15a.png)  ![](../_resources/5b9e734c70adf432e7365feac6a246a7.png)  ![](../_resources/4fc2b2814c2ae7b2638d47336944b701.png)  ![](../_resources/bcd2112ad258d2da69c4cdfdaf7172e4.png)  ![](../_resources/f4d849bb2755dca1ffa9c882571455a8.png)  ![](../_resources/96ba287025db1a267d4b12877cbdcc50.png)  ![](../_resources/ce04bb7a09fc54464d25b3f0453b8b89.png)  ![](../_resources/383eac126facd8039602cc4e5d50cfa3.png)  ![](../_resources/18bdcbb1bb65cab07f05746d6bc37d87.png)  ![](../_resources/d59aaca5af7ef86e651b47a7e213e835.png)  ![](../_resources/c8137ec902ad2b6912a7d8399749af40.png)  ![](../_resources/66cd6506cdbf0ded8960b4f25b18b92f.png)  ![](../_resources/ffa413594a2e2983124c02230cbda3ce.png)  ![](../_resources/6993259ce09fba68efd103653bdb38b7.png)  ![](../_resources/b47e66a0b81d5ce0f9de1be2e2eec041.png)  ![](../_resources/d77fbaa8d602a579ecc77e06109c5810.png)  ![](../_resources/43fc9979a053b5ed99668b74e8c7ff2a.png)  ![](../_resources/7d159f0fc2ecbd5add29af9654dfad14.png)  ![](../_resources/7c8fe7ca2bf3cbc52f347f9ffd097c63.png)  ![](../_resources/eaec13997e897b357099d68ab33a25eb.png)

For actual JPEG images there are a just few extra details.

The image gets broken up into 8x8 chunks, and each chunk gets split up separately. We use a set of frequencies to determine how light or dark each pixel is, and then another two sets for the color, one for red-green, and another for blue-yellow. The number of frequencies that we use for each chunk determines the quality of the JPEG.

Here's a real JPEG image, zoomed in so we can see the details. When we play with the quality levels we can see this process happen.

## Conclusion

So lets recap:

- Fourier transforms are things that let us take something and split it up into its frequencies.
- The frequencies tell us about some fundamental properties of the data we have
- And can compress data by only storing the important frequencies
- And we can also use them to make cool looking animations with a bunch of circles

This is just scratching the surface into some applications. The Fourier transform is an extremely powerful tool, because splitting things up into frequencies is so fundamental. They're used in a lot of fields, including circuit design, mobile phone signals, magnetic resonance imaging (MRI), and quantum physics!

## Questions for the curious

I skipped most of the math stuff here, but if you're interested in the underlying principles of how it works, here are some questions you can use to guide your research:

- How do you mathematically represent a Fourier transform?
- What's the difference between a continuous time Fourier transform and a discrete time Fourier transform?
- How do you computationally do a Fourier transform?
- How do you do a Fourier transform of a whole song? (Rather than just a single note.)

## Further 'reading'

To learn more, some really good resources you can check out are:

[An Interactive Guide To The Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)

A great article that digs more into the mathematics of what happens.

[But what is the Fourier Transform? A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY)

A great Youtube video by 3Blue1Brown, also explaining the maths of Fourier transforms from an audio perspective.

[A Tale of Math & Art: Creating the Fourier Series Harmonic Circles Visualization](https://alex.miller.im/posts/fourier-series-spinning-circles-visualization/)

Another article explaining how you can use epicycles to draw a path, explained from a linear algebra perspective.

[Fourier transform (Wikipedia)](https://en.wikipedia.org/wiki/Fourier_transform)

And of course, the Wikipedia article is pretty good too.

## The author

![](../_resources/f92c20a507f9077b6ffe836ea89736ed.png)

I'm Jez! Full time I work at a [search company](https://www.google.com/) in the Bay Area, and in my spare time I like making games and interactive code things like this!

This webpage is open-source, you can check out the code on [GitHub](https://github.com/Jezzamonn/fourier)! If you have any feedback or want to ask any questions, feel free to email me at [fourier@jezzamon.com](http://www.jezzamon.com/fourier/index.htmlmailto:fourier@jezzamon.com), or shoot me a tweet on [Twitter](https://twitter.com/jezzamonn).

If you want to see more of my work, check out my [homepage](http://www.jezzamon.com/), and if you want to see what I'm making next, you can follow my Twitter account, [@jezzamonn](https://twitter.com/jezzamonn)!

[5 min to Spreed]()