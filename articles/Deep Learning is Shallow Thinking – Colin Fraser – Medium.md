Deep Learning is Shallow Thinking – Colin Fraser – Medium

# Deep Learning is Shallow Thinking

## Three Fundamental Things That Deep Learning Can’t Do

[![1*MtaL4xPr-IvvmU1bPbHlJw.jpeg](../_resources/eaa9d953a15b327c60c49aaa15014621.jpg)](https://medium.com/@colin.fraser?source=post_header_lockup)

[Colin Fraser](https://medium.com/@colin.fraser)
Nov 15, 2018·12 min read

AI is a huge and vague term that means different things to different people, but everyone agrees about one thing: AI is the future. Soon enough, AI will be driving all of our Ubers and directing our Netflix specials and delivering our Amazon prime orders. Indeed in many cases these things are already taking place to some extent.

The crown jewel of modern AI hype is the family of machine learning models called Deep Neural Networks, or more often these days, Deep Learning. Deep Learning has led to some truly astonishing examples of computers performing tasks previously thought to be only doable by humans.

![](../_resources/c286a9c5b25172614bfd9f3d33192c78.png)![0*rPy_InvBtZiiZVjA.jpg](../_resources/95e72f6773231044046aadd36e877a56.jpg)

Very Smart Computer (from [here](https://aws.amazon.com/rekognition/))

In particular, various forms of Deep Learning have proven so far to be very effective at [facial recognition](https://aws.amazon.com/rekognition/), [translation](https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation), [playing Go](https://en.wikipedia.org/wiki/AlphaGo#Algorithm), and [beating the first level of Super Mario](https://www.youtube.com/watch?v=qv6UVOQ0F44). And lots of other things too. These are tasks that seem really human, and things that have eluded programmers for a really long time. Many attempts have been made at using classical computer programming methods to accomplish these things, and they’ve all more-or-less failed. Deep Learning has been *by far* the most successful approach to these kinds of problems.

The language that surrounds Deep Learning is very evocative of human intelligence. It’s *learning*, and it’s *deep*. There are *perceptrons* or *neurons *and they are connected by *synapses* just like a brain. Major DL projects have names like *Google Brain *and *DeepMind*. It’s tempting to conclude that Deep Learning will bring us the HALs and Skynets and Datas that we’ve all been waiting for. But I’m skeptical that this is the case due to some things that Deep Learning is fundamentally missing from what I would personally call *intelligence*.

### Before we begin, a quick primer on what Deep Learning actually is

Deep Learning is a family of methods for doing supervised (well, usually supervised, and occasionally unsupervised, but I’ll focus on the supervised case here) machine learning. Supervised Machine Learning is the general problem of trying to make accurate predictions about some outcome by looking at past examples of it.

A common example is identifying parts of images. The Amazon Rekognition image in the previous part depicts the machine correctly identifying that the image contains a smile. In order to build a system that can do that using supervised machine learning, we would need to assemble a very large data set of images of people, with many of them smiling, and many others not. The general Supervised Machine Learning process is to then show the computer an image of someone smiling, and tell it “this person is smiling”, and then to show the computer an image of someone not smiling, and tell it “this person is not smiling”. Repeat this a few tens of thousands of times (or more), and hopefully at the end of it the computer has figured out the patterns that differentiate “this person is smiling” from “this person is not smiling”.

Of course, an image in a computer is really just a very long sequence of numbers. A color image that measures 28 × 28 pixels is stored in a computer as a list of 28×28×3=2,352 numbers, representing the intensities of the red, green, and blue pixel values for each of the 28×28=784 pixels of the image. Since it takes 2,352 numbers to describe a computer image of that size, we say that that type of data is 2,352 dimensional data. That’s a lot more dimensions than we are used to working with (3, maybe 4)! It is not at all straightforward to figure out where in those 2,352 dimensions lies the information about whether there is a smile. That limitation held back standard machine learning methods from doing things like smile detection for a really long time.

Deep Learning appears to have given us sophisticated ways of solving this particular problem, and the more general problem of dealing with high dimensional data. Deep Neural Networks can be programmed to do things like look at local regions of images in what seems like something close to how people look at images, rather than looking at images a single pixel at a time the way that computers traditionally do. That same trick has helped Deep Neural Networks perform well at all kinds of tasks involving high dimensional data, like other kinds of image classification, voice decoding, or text processing.

But it’s important to remember that the overall Deep Learning framework still works the exact same way as any other supervised machine learning method. You collect as many labelled examples of the outcome that you’re trying to predict as you can, and you show them to the Deep Learning network one at a time, along with the labels. The network tries to get good at predicting the labels from the examples with practice. Deep Learning is the best we have right now at learning in this way.

### The Things That Deep Learning Can’t Do

#### Basic Arithmetic

Remember how deep learning works: by example. We show the machine thousands of examples and hope it picks up the pattern. This is fundamentally antithetical to how mathematics works. In math, we set the rules first and use the rules to find examples. In machine learning, we look at examples and use them to infer the rules.

If you wanted to teach a neural network how to do basic arithmetic, you would begin by assembling thousands of examples of basic arithmetic problems. You would then show the problems to the machine, along with solutions. Maybe your list would look like

1 + 1 = 2
9 / 3 = 3
3 * 2 = 6
...
You’d want to make the list very long.

The truth is that no matter how you set it up, your neural network will almost surely not learn to *do *math problems. What it will do is memorize the training examples that you’ve given it, so that if you then ask it what 1 + 1 is, it will correctly give you 2, and if you ask it a question that is not far from a training example, it might get it almost right: if you ask what 1 + 2 is, it might give you something like 3.00002, which is close, but close doesn’t count in basic arithmetic. Or it might just give you something insane. And if you ask the neural network what 45 + 98 is — numbers far outside the range that we used for training — forget it. The results are entirely unpredictable.

[Here’s a recent example of a paper trying to tackle this very problem.](https://arxiv.org/abs/1808.00508) Researchers Trask et al. construct a new type of component to the classical deep learning framework to allow neural networks to “learn” basic arithmetic from examples. Neural networks that use the new layer perform significantly better at simple arithmetic problems than Neural networks without it — they get almost all of the problems almost right (except for division problems, which it still has a hard time with). I’ll repeat this: cutting edge research has deep neural networks that can *almost* correctly add, subtract, and multiply (but not divide).

This is not to bash this research, by the way. There are important reasons to want to see how well we can teach neural networks to do simple math, and the mechanism that the researchers came up with to get it done is very smart. They are smarter than me. And it’s not to bash neural networks either. It’s just that this shows that neural networks don’t *think* the way that a lot of people think they do. Neural networks “learn” to add by looking at thousands of examples of addition problems and trying to build a mathematical function that best approximates addition. This is not how people “learn” to add . You don’t start by showing a class of five-year-olds thousands of examples of math problems until they start to get the pattern. You show them one or two examples of math problems, explain the concepts underlying the problems, and focus on promoting understanding of those concepts. This is antithetical to how the current generation of Deep Learning works.

And this *human* mode of learning allows us to do things that are completely off limits to the neural network like reason about numbers to come up with novel true statements about them. Even if Trask et al. figure out how to teach a neural network to divide two numbers, that neural network won’t be able to take what it has “learned” about the nature of divisibility and determine that it implies that there are infinitely many prime numbers, [which Euclid did over 2000 years ago](https://en.wikipedia.org/wiki/Euclid%27s_theorem#Euclid%27s_proof). That’s just not what neural networks do.

#### Analogy and Metaphor

Analogies and metaphors are really really important to how people think about things. They are so important that often we don’t even notice that we’re using them. Take the first paragraph from the United States Declaration of Independence (emphasis mine).

> When in the Course of human events it becomes necessary for one people to **> dissolve the**>  political **> bands which have connected them **> with another and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature’s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to **> the separation.**

As Steven Pinker points out in *The Stuff of Thought*, there’s a sneaky metaphor in here that you might not notice if it weren’t pointed out for you: political alliances are physical bonds. Ending alliances is *dissolving bands *and inducing *separation*.

Metaphor and analogy allow us to take things we know about one domain and apply them to another. If I tell you that political alliances are like physical bonds, then you may be able to infer that, for instance, it must take some hard work to “break” them.

There are a lot more practical examples. What’s Canadian Football? Well, it’s *like* American Football, but with three downs instead of four. If you know the rules of American Football, congratulations, you can now sit down and watch a CFL game and understand everything that’s going on. Analogies to the rescue.

Deep Learning is very bad at this. The best neural networks are good at doing basically one task in one way, and can’t really use what they’ve learned previously to do new but related tasks. And I’m not talking about doing political philosophy or even watching football. I’m talking about very very simple analogies.

For instance, suppose there was a neural network trained to recognize dog breeds — if you want to build exactly that, [here’s a nice tutorial.](https://towardsdatascience.com/dog-breed-classification-hands-on-approach-b5e4f88c333e) As in the tutorial, you show the neural network 20 thousand pictures of dogs, each belonging to one of 120 breeds. If you follow the tutorial, you can build a model that does this pretty well, getting dog breeds right about 97% of the time or so.

But the model has never seen a Teacup Poodle before — only a Toy Poodle. If this were a person identifying dog breeds, I might say to that person, “well, a Teacup Poodle is *like* a Toy Poodle, except smaller”. I’d expect that that person, if they were already pretty good at identifying Toy Poodles, would instantly also be pretty good at identifying Teacup Poodles, because people are good at learning by analogy.

But there is no way in the framework of neural networks to do this. I can’t tell the neural network about a hypothetical breed that it’s never seen, and describe the breed in terms of breeds that it has seen.

What I would need to do using the supervised machine learning approach would be to find a few hundred photographs of teacup poodles, stick those onto the end of my 20,000 existing images, and have the network re-learn all 121 breeds from scratch.

(Some people will argue that there is something called Transfer Learning, which allows you to use neural networks previously trained at one big task to perform some special case of that task. But Transfer Learning is still not analogy. You don’t do transfer learning by telling the neural network that Teacup Poodles are like Toy Poodles but smaller. You do it in essentially the way described in the last paragraph. That’s still not using analogy.)

Again, this is exemplary of how the way that neural networks “learn” is so completely different from how it seems that humans learn. Neural networks “learn” by looking at vast quantities of data and extracting numerical patterns from that data, and we hope that the patterns that they extract correspond to the thing we’re trying to achieve. And this mode of learning is very good for doing some things. Neural networks can achieve superhuman ability at classifying images of dogs into a predetermined list of breeds. But that neural network doesn’t know what a dog is. It doesn’t know what anything is. It just knows that the presence of certain patterns in an image are highly correlated with the label `toy_poodle`. This is useful, but to me it is not intelligence.

And, I’m going out on a bit of a limb here, but I believe that the fact that human speech is so riddled with metaphor and analogy will prevent current deep learning methods from ever achieving an understanding of human speech in the vein of Data or Hal. The very best “speech recognition” tools that we have are still simply listening for key phrases as opposed to *understanding*. Same with chat bots. I think it’ll take a pretty drastic advance in machine learning — something that we have really never seen before — to get beyond simply listening for key phrases, which is the only thing that today’s neural networks can really do.

#### Causal Inference

This is one that humans are bad at too, but neural networks are even worse. Here’s an example that’s roughly taken from Judea Pearl’s [The Book Of Why](https://www.amazon.com/Book-Why-Science-Cause-Effect/dp/046509760X). Suppose you build a neural network using deep learning that predicts when customers are going to leave your company as a function of your historical prices, when the customer signed up, and all kinds of other stuff. Now you have a machine that, perhaps very accurately, can look at a customer, look at the price they’re paying, look at when they signed up, and whatever else you’ve shown it, and tell you the probability that that customer will leave.

Now you wonder: suppose I raise my prices by 15%. What would happen to my churn rate?

One thing you might do is plug 15% higher prices into your model and see what churn rate it predicts. But the truth is that your model is going to make a very bad guess, because it has no idea about causality.

The model might have observed an association between customer churn and your prices. Maybe when your prices have been higher, customer churn has been higher. But your model does not know if it is the high prices causing the high churn rate, or the high churn rate causing the high prices, or some third thing causing both.

It could be that setting a higher price caused the churn rate to increase, as customers found that the service was getting too expensive, in which case increasing the price will increase your churn rate. Or, it could be that a high churn rate caused you to lose money, requiring you to raise your prices. If this is the case, increasing the price might not actually affect your churn rate much. Or maybe, there was a recession that made your inputs more expensive and simultaneously caused people to stop buying your service. In that case it’s not clear what the relationship will be between your prices and the churn rate. Each of these stories would be seen the exact same way by the model.

Deep Learning is not built to do this kind of reasoning. As a rule, we don’t tell neural networks much about how the world works. We give them all the data we can find and tell them to go hunt for associations. And they are very good at finding those associations. But correlations on their own don’t tell us how causation works, and so models designed to seek out correlations can’t answer hypothetical questions like “what would happen if I did this?”.

We can tell the neural network *that* we increased our price in 2015, but we can’t tell the neural network *why* we increased our price in 2015. That’s just not part of the machinery of neural networks, or of machine learning in general. Neural networks are memorization machines. They are very good at finding associations and making predictions about those associations, but they are fundamentally incapable of thinking outside of the associations.

### Are you saying that AI can’t do any of these things?

No, but I don’t think AI is well defined, and a lot of people are confusing AI with Deep Learning these days. AI just refers to the thing where computers do things that seem smart. Neural networks sort of do that: they recognize faces and translate speech to text and play Mario and that seems smart. But they can’t add or learn by analogy or understand causality, and that doesn’t seem smart.

And it’s not that computers can’t do the things that I’ve described neural networks failing at here. Of course computers can do basic arithmetic. They are very good at it. But computers have been able to do basic arithmetic since, basically, the invention of computers. Deep learning has contributed approximately nothing to the ability of computers to do basic arithmetic. And in some ways computers can handle analogy and causal inference, too, although those are a little further behind than basic arithmetic.

I am saying that Deep Learning, in its current form, will not evolve into artificial general intelligence. Deep Learning is good at doing one kind of thing, and it does that thing miraculously well. That thing is to find associations in vast quantities of high dimensional data, and to model those associations. But that is not close to enough to become general intelligence.

That is not to say that Deep Learning can’t contribute to general intelligence, but if artificial general intelligence is a house, deep learning is just a brick (that’s an analogy that a neural network wouldn’t get). It will take a lot more components gluing neural networks together to form anything truly intelligent.