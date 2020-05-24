Novel math could bring machine learning to the next level

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='article__info-icon js-evernote-checked' data-evernote-id='628'%3e %3cstyle data-evernote-id='422' class='js-evernote-checked'%3e.agst16%7bfill:%23a5a6b7%7d%3c/style%3e%3cpath class='agst16 js-evernote-checked' d='M8 15.5c4.1 0 7.5-3.4 7.5-7.5S12.1.5 8 .5.5 3.9.5 8s3.4 7.5 7.5 7.5zM8 1.8c3.4 0 6.2 2.8 6.2 6.2s-2.8 6.2-6.2 6.2S1.8 11.4 1.8 8 4.6 1.8 8 1.8z' data-evernote-id='423'%3e%3c/path%3e%3cpath class='agst16 js-evernote-checked' d='M8.6 8.4l.1-.3V3.3H7.3v4.6L5.6 11l1.2.6z' data-evernote-id='424'%3e%3c/path%3e %3c/svg%3e)

September 2, 2019

# Novel math could bring machine learning to the next level

by Champalimaud Centre for the Unknown

 ![novelmathcou.jpg](../_resources/87349207450c0f9c5c05db8a00617639.jpg)

The new approach allows artificial intelligence to learn to recognize transformed images much faster. Credit: Diogo Matias

A team of Italian mathematicians, including a neuroscientist from the Champalimaud Centre for the Unknown (CCU), in Lisbon, Portugal, has shown that artificial vision machines can learn to recognize complex images more quickly by using a mathematical theory that was developed 25 years ago by one of this new study's co-authors. Their results have been published in the journal *Nature Machine Intelligence*.

In recent decades, machine vision performance has vastly improved. Artificial systems can now learn to recognize virtually any [human face](https://techxplore.com/tags/human+face/) or to identify any individual fish moving in a tank.

Such [machines](https://techxplore.com/tags/machines/) are, in fact, electronic models of networks of biological neurons, and their aim is to simulate the functioning of the brain, which excels at these visual tasks without any conscious effort on our part.

But how do these [artificial neural networks](https://techxplore.com/tags/artificial+neural+networks/) actually learn? In the case of face recognition, for instance, they do it by acquiring experience about what human faces look like in the form of a series of portraits. More specifically, after being digitized into a matrix of pixel values, each image is "crunched" inside the [neural network](https://techxplore.com/tags/neural+network/), which then extracts general, meaningful features from the set of sample faces (such as the eyes, mouth, nose, etc).

This [deep learning](https://techxplore.com/tags/deep+learning/) enables the machine to spit out another set of values, which will in turn enable it to identify a face it has never seen before in a databank of faces (much like a fingerprint database), and therefore predict who that face belongs to with great accuracy.

**The story of Clever Hans**

But before the neural network can perform this well, it is typically necessary to present it with thousands of faces (i.e. matrices of numbers). Moreover, though these machines have been increasingly successful at pattern recognition, the fact is that nobody really knows what goes on inside them as they learn tasks. They are basically black boxes.

What this means is that it is not possible to determine which or how many features the machine is actually extracting from the initial data—and not even how many of those features are really meaningful for face recognition.

"To illustrate this, consider the paradigm of the wise horse," says first author of the study Mattia Bergomi, who works in the Systems Neuroscience Lab at the CCU. The story, from the early years of the 20th century, concerns a horse in Germany called Clever Hans that his master claimed had learned to perform arithmetic and announce the result of additions, subtractions, etc. by stamping one of his front hooves on the ground the right number of times. Many people were convinced he could count; the horse was even reported by the *New York Times*. But then, in 1907, a German psychologist showed that the horse was, in fact, picking up unconscious cues in his master's body language that were telling it when to stop tapping.

"It's the same with machine learning; there is no control over how it works, or what it has learned during training," Bergomi explains. The machine, having no a priori knowledge of faces, just somehow does its stuff—and it works.

This led the researchers to ask whether there might be a way to inject some knowledge of the real world about faces or other objects into the neural network before training in order to cause it explore a more limited space of possible features instead of considering them all—including those that are impossible in the real world. "We wanted to control the space of learned features," Bergomi says. "It's similar to the difference between a mediocre chess player and an expert: The first sees all possible moves, while the latter only sees the good ones," he adds.

Another way of putting it, he says, is by saying that "our study addresses the following simple question: When we train a deep neural network to distinguish road signs, how can we tell the network that its job will be much easier if it only has to care about simple geometrical shapes such as circles and triangles?"

The scientists reasoned that this approach would substantially reduce training time—and importantly, give them a hint about what the machine might be doing to obtain its results. "Allowing humans to drive the learning process of learning machines is fundamental to move toward a more intelligible artificial intelligence and reduce the skyrocketing cost in time and resources that current neural networks require in order to be trained," he says.

**What's in a shape?**

An abstract [mathematical theory](https://techxplore.com/tags/mathematical+theory/) called topological data analysis (TDA) was key. The first steps in the development of TDA were taken in 1992 by the Italian mathematician Patrizio Frosini, co-author of the new study, currently at the University of Bologna. "Topology is one of the purest forms of math," says Bergomi. "And until recently, people thought that topology would not be applicable to anything concrete for a long time, until TDA became well-known in the last few years."

Topology is a sort of extended geometry that, instead of measuring lines and angles in rigid shapes (such as triangles, squares, cones, etc.), seeks to classify highly complex objects according to their shape. For a topologist, for example, a donut and a mug are the same object: one can be deformed into the other by stretching or compression.

Now, the thing is, current neural networks are not good at topology. For instance, they do not recognize rotated objects. To them, the same object will look completely different every time it is rotated. That is precisely why the only solution is to make these networks "memorize" each configuration separately—by the thousands. And it is precisely what the authors were planning to avoid by using TDA.

Think of TDA as being a mathematical tool for finding meaningful internal structure (topological features), in any complex object that can be represented as a huge set of numbers. This is accomplished by looking at the data through certain well-chosen "lenses," or filters. The data itself can be about faces, financial transactions or cancer survival rates. TDA makes it possible to teach a neural network to recognize faces without having to present it with each of the different orientations faces might assume in space. The machine will now recognize all faces as being a face, even in different rotated positions.

In their study, the scientists tested the benefits of combining machine learning and TDA by teaching a neural network to recognize hand-written digits. The results speak for themselves.

As these networks are bad topologists and handwriting can be very ambiguous, two different hand-written digits may prove indistinguishable for current machines—and conversely, they may identify two instances of the same hand-written digit as different. The task requires presenting the network, which knows nothing about digits in the real world, with thousands of images of each of the 10 digits written with all sorts of slants, calligraphies, etc.

To inject knowledge about digits, the team built a set of a priori features that they considered meaningful—in other words, a set of "lenses" through which the network would see the digits—and forced the machine to choose among these lenses to look at the images. The number of images (that is, the time) needed for the TDA-enhanced neural network to learn to distinguish fives from sevens, however badly written, while maintaining its predictive power, dropped down to less than 50.

"What we mathematically describe in our study is how to enforce certain symmetries, and this provides a strategy to build machine-learning agents that are able to learn salient features from a few examples by taking advantage of the knowledge injected as constraints," says Bergomi.

Does this mean that the inner workings of learning machines that mimic the brain will become more transparent in the future, enabling new insights on the inner workings of the brain itself? In any case, this is one of Bergomi's goals. "The intelligibility of artificial intelligence is necessary for its interaction and integration with biological intelligence," he says. He is currently working, in collaboration with his colleague Pietro Vertechi, on developing a new kind of neural [network](https://techxplore.com/tags/network/) architecture that will allow humans to swiftly inject high-level knowledge into these networks to control and speed up their training.

* * *

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' data-evernote-id='680' class='js-evernote-checked'%3e %3cpath d='M516.667 200H333.333V16.667C333.333 7.462 325.871 0 316.667 0h-100C207.462 0 200 7.462 200 16.667V200H16.667C7.462 200 0 207.462 0 216.667v100c0 9.204 7.462 16.666 16.667 16.666H200v183.334c0 9.204 7.462 16.666 16.667 16.666h100c9.204 0 16.667-7.462 16.667-16.666V333.333h183.333c9.204 0 16.667-7.462 16.667-16.666v-100c-.001-9.205-7.463-16.667-16.667-16.667z' data-evernote-id='485' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Explore further

 [All-optical diffractive neural network closes performance gap with electronic neural networks](https://phys.org/news/2019-08-all-optical-diffractive-neural-network-gap.html)

* * *

**More information:**Towards a topological–geometrical theory of group equivariant non-expansive operators for data analysis and machine learning, *Nature Machine Intelligence* (2019). [DOI: 10.1038/s42256-019-0087-3](http://dx.doi.org/10.1038/s42256-019-0087-3)

**Journal information:**[Nature Machine Intelligence](https://techxplore.com/journals/nature-machine-intelligence/)  [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' data-evernote-id='689' class='js-evernote-checked'%3e %3cpath d='M6.579.8L3.656 3.722a.44.44 0 0 0 .623.623L7.2 1.423V2.4a.4.4 0 0 0 .8 0v-2a.398.398 0 0 0-.4-.4h-2a.4.4 0 0 0 0 .8zM8 4.8V2.899v4.104c0 .55-.397.997-.887.997H.887C.397 8 0 7.553 0 7.003V.997C0 .447.397 0 .887 0h4.27H3.2a.4.4 0 1 1 0 .8H1.028C.9.8.8.92.8 1.067v5.866c0 .145.102.267.228.267h5.944c.127 0 .228-.12.228-.267V4.8a.4.4 0 1 1 .8 0z' fill-rule='evenodd' data-evernote-id='444' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://www.nature.com/natmachintell/)

Provided by Champalimaud Centre for the Unknown