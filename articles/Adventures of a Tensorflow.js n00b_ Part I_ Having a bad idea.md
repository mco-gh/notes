Adventures of a Tensorflow.js n00b: Part I: Having a bad idea

# *Adventures of a Tensorflow.js n00b: Part I: Having a bad idea*

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='52' height='58' viewBox='0 0 52 58' class='ca fo ji jj jk jl cv js-evernote-checked' data-evernote-id='120'%3e%3cpath d='M1.49 16.25A27.53 27.53 0 0 1 26 1.55V.45A28.63 28.63 0 0 0 .51 15.75l.98.5zM26 1.55a27.53 27.53 0 0 1 24.51 14.7l.98-.5A28.63 28.63 0 0 0 26 .45v1.1zm24.51 40.2A27.53 27.53 0 0 1 26 56.45v1.1a28.63 28.63 0 0 0 25.49-15.3l-.98-.5zM26 56.45a27.53 27.53 0 0 1-24.51-14.7l-.98.5A28.63 28.63 0 0 0 26 57.55v-1.1z' data-evernote-id='121' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)![1*iDQvKoz7gGHc6YXqvqWWZQ.png](../_resources/f0e9ff72b7b548cae2dd56f0254f6d39.png)](https://medium.com/@tensorflow?source=post_page-----25dc7f9ddc8e----------------------)

[TensorFlow](https://medium.com/@tensorflow?source=post_page-----25dc7f9ddc8e----------------------)

[Jul 9](https://medium.com/@tensorflow/adventures-of-a-tensorflow-js-n00b-part-i-having-a-bad-idea-25dc7f9ddc8e?source=post_page-----25dc7f9ddc8e----------------------) · 13 min read

*David Weinberger, an independent tech writer, is currently a writer in residence at Google’s *[*People + AI Research*](https://ai.google/pair)* (PAIR) initiative. During his ongoing residency, he is looking at machine learning technology within a broader context of social issues and ideas, and documenting his experiences using new ML tools, from *[*What-If*](https://pair-code.github.io/what-if-tool/)* to *[*Tensorflow.js*](https://www.tensorflow.org/js)*. His opinions are his own and do not necessarily reflect those of Google. (*[*Prior posts*](https://accelerate.withgoogle.com/ai-outside-in)*.)*

[TensorFlow.js](https://js.tensorflow.org/) lets you run Google’s open source library of tools for creating and running machine learning applications in a browser on your own computer.

Awesome. But there’s a lot packed into the phrase “lets you run,” especially when the “you” is me. You might as well say that a professionally provisioned kitchen lets me bake a wedding cake that’s a twelve meters tall replica of the Leaning Tower of Pisa, but the chances of my attempt staying up are nil.

So what are the chances that I, a hobbyist JavaScripter of the sort who gives variables names like thePhotoCounterThatWorks_UseThisOne, can succeed with TensorFlow.js? Yes, JavaScript is the language I am best at — [TensorFlow](https://tensorflow.org/) without the “.js” works with Python, which I am far worse at — but “best at” does not imply “good at.” (TensorFlow.js also lets users run machine learning models right in their browser, and as a friend of the open Web, I like browsers and keeping things local.)

I do have one secret superpower, however. As a temporary writer-in-residence at Google, I’m embedded in People + AI Research (PAIR), and am sitting just a few desks over from the developers who created TensorFlow.js. That puts me in a unique position to strain their patience by asking them an endless stream of embarrassingly clueless questions.

And here is the first lesson I’ve learned: They’re not saying “TensorFlow Jazz” as I at first thought. It’s definitely TensorFlow.js.

Personally, I prefer my [mishearing](http://www.kissthisguy.com/) of it.

## Why write this series of non-tutorials?

The aim of this series of posts is *not* to write a step-by-step TensorFlow.js tutorial. If that’s what you want, here’s [one](https://www.tensorflow.org/js/tutorials) from the project’s Web site. And here’s [one](https://rubikscode.net/2019/03/18/introduction-to-tensorflow-js-with-real-world-example/) from outside of the group.

Rather, I’m trying to understand, in a hands-on way, some of what’s entailed in creating a machine learning app. It’s not so I can go off and create more apps — I’m happy to leave that to the professionals — but so I have a better sense of how these apps work from the lowest level that contains no math. I’m particularly interested in two questions: First, just how weird is machine learning? Second, what sorts of choices do developers make as they shape a project?

For example, while tutorials generally start with an existing, well-worked data set, I want some sense of what goes into creating a data set. What does machine learning want from data, and how do the choices the developers make about data affect what the system learns? So, much of this series will consist of me floundering with data. My aim is to make as many mistakes as I can. So, it’s not going to be pretty. It is, however, going to be personally embarrassing, so it’s got that going for it.

I should note at the outset that I’m not going to deal in any depth with the [scary](https://www.propublica.org/article/bias-in-criminal-risk-scores-is-mathematically-inevitable-researchers-say) and [very real](https://www.nytimes.com/2016/06/26/opinion/sunday/artificial-intelligences-white-guy-problem.html) ways [innocent-seeming data sets](https://venturebeat.com/2018/12/21/researchers-expose-biases-in-datasets-used-to-train-ai-models/) and [algorithms](https://www.wired.com/story/the-real-reason-tech-struggles-with-algorithmic-bias/) can introduce [biases](https://youtu.be/QxuyfWoVV98) that lead machine learning applications to [reinforce or amplify existing social biases](https://www.bloomberg.com/opinion/articles/2018-10-16/amazon-s-gender-biased-algorithm-is-not-alone). Confronting, and mitigating, those biases requires understanding how machine learning operates in the first place, and that’s what this series tries to help with. (For more information, here’s [PAIR’s guidebook](https://ai.google/responsibilities/responsible-ai-practices/), and [Google’s Responsible AI Practices](https://ai.google/responsibilities/responsible-ai-practices/).)

## A series of unfortunate ideas

When I started writing this blog series, I hadn’t yet nailed down the exact project I’d undertake. I wanted to set the bar as low as possible, so I wasn’t aiming at something actually useful and certainly not original.

I thought about — in fact, started working on — a machine learning application that would do something fun, such as let you supply some adjectives and have it come up with a color palette. In particular, I wanted to use the sort of machine learning that takes in data and connects the dots into what’s known as an *artificial neural network*: a map of probabilistic correlations that can be huge and literally mind-bogglingly complex.

So I asked [Mahima Pushkarna](https://twitter.com/mahimapushkarna?lang=en), a visual designer with PAIR who sits across from me, about the idea. She pointed to [Design Seeds](https://www.design-seeds.com/), a site that identifies the six dominant colors in an image, turns them into a palette, and supplies a few evocative tags for each. The site seems to have about 15,000 palettes. So, I thought I could somehow acquire them all, run them and their tags through TensorFlow.js, and have the machine learning (ML) build a palette of colors based on any set of tags a user cares to choose. For example, you might ask it to build a palette based on the tags “calm,” “sparrow,” and “ooh la la!”, and the system would come up with six hues it has learned are related to those terms.

But I ran into some problems. First, the Design Seeds site doesn’t make its contents available for this sort of reuse, as is its right. But even if it did, the app I was proposing was a dumb idea. How could a user tell if a palette in fact did represent the tags “calm,” “sparrow” and “oohlala!”? (To see a version of this idea that works, and is also very funny, see [Janelle Shane’s paint naming AI](http://aiweirdness.com/post/160776374467/new-paint-colors-invented-by-neural-network). In fact, see [everything Janelle does](http://aiweirdness.com/).)

So, I came up with some even worse ideas. And then I changed tacks, going down a path for months that turned out to be based on some wrong assumptions, leading me at one point to give this series of posts the subtitle “A Complete Guide to Rookie Errors.”

## Collecting the wrong data

I respect [Flickr](https://www.flickr.com/) for having early on created a [commons of photos](https://www.flickr.com/commons) that can be freely shared, plus I’ve used [Flickr’s API](https://www.flickr.com/services/api/) ([application programming interface](https://www.mulesoft.com/resources/api/what-is-an-api)) before. An API lets you write a program that requests information from a site directly; the information is returned to you in a form easy for a program to digest, not wrapped up in a pretty Web page. So I decided to download a few thousand photos from the site.

Through Flickr’s API you request metadata about the photos: the title, author’s Flickr ID, user-created tags, the Web address where the photos are, and the like. So, I downloaded about three thousand of those metadata records, asking only for photos from the Recent Activity stream that are marked as openly re-usable (thank you, [Creative Commons](https://creativecommons.org/)!). I saved that metadata and used it to download the actual photos themselves. (For this learning project, I didn’t publish the data set or model. The final code is available for your amusement at [GitHub](https://github.com/dweinberger/desertOrJungle/).)

(By the way, downloading Flickr photos without its not-safe-for-work filter on is a fast lesson in why we need to be aware of gender issues and biases in our data sets.)

But the tags for the photo set were a mess. Flickr users tag photos for whatever reason they want — a place name, a feeling, a color, a person’s name, or, in [one case](https://www.flickr.com/photos/nicolesphoto/29911941917/in/datetaken/), a marriage proposal with each word inserted as a separate tag. The idiosyncratic nature of Flickr tagging is glorious, and I love Flickr for it, but it makes for a data set that lacks the consistency that would let machine learning see what a group of similarly-tagged photos have in common.

So I did some data clean-up.

I wrote a little JavaScript that counted the number of times each tag was used. The most-used tags noted what type of camera took the photo, information that’s unrelated to the content of the photos, so I lopped those tags off the list. If I were interested in seeing if neural networks[could look at an image and tell what type of camera took it](http://francescopochetti.com/given-picture-able-identify-camera-took/), that data would have been crucial. But since I seem to be aiming at having machine learning sort images according to their content, the camera info is just confusing. So, I shaved those tags off, as well as some others that had nothing to do with the photo’s content.

Then I saved the remaining top 200 tags. The least-used ones on the list were used nine times, so there would be at least nine photos for the machine learning system to examine for patterns peculiar to any particular tag. (If you’ve worked with machine learning systems, you can already see where I’m going wrong.) I then threw out any of the 3,000 photos that did not have at least one of those 200 tags attached to them. That left 1,906 images on which to train a system to recognize images that it had not been trained on.

Then, I wrote out files that contained the data about each of the photos that survived the filtering process. Each record contained the file name of the photo saved on my disk, the tags, the title the photographer applied to the photo, license information, the attribution, and information about where the photo lives on Flickr’s servers. (I expressed the data as [JSON](https://www.json.org/), the obvious choice.)

Why limit myself to photos with at least one of the top 200 tags? Because [Yannick Assogba](https://twitter.com/tafsiri) told me to. He’s one of the developers at PAIR, and he’s been incredibly patient with me as I prove that, yes, there are such things as dumb questions.

As Yannick pointed out, a tag that’s attached to just one photo is not going to be able to teach the ML system anything useful. It’d be like having 1,906 people each with a different first name fill in a standardized form about themselves. Asking “So, what does this tell us about people named Vivek?” will lead you to nothing beyond what that one Vivek entered on this form. It’s not going to tell you anything about the next Vivek you run into.

So, now I have about 2,000 photos and their top 200 tags. What shall I do with them? (Narrator: He’ll throw them out.)

## The app, version 0.01

Normally, people build ML systems to solve a problem. That then dictates what sort of data they need to collect.

I’m going in reverse. I don’t much care what I build. I’m just trying to learn. So, what does the data I have in hand lend itself to?

Here’s my idea for an app: The user will drag in a photo and the system will apply all of its machine learning smarts to figuring out which of the tags it knows about most likely applies to that image. Alert the VCs!

It will accomplish this by finding likenesses — patterns in the pixels — between the uploaded photo and the ones I trained the machine learning on. By analyzing the uploaded photo, the ML system will make a probabilistic judgment about which tags to suggest. Maybe I’ll call it WWFT: “What Would Flickr Tag?”

This app will not actually be useful to anyone, but it might serve as an example of machine learning. It will require the system to analyze my downloaded images to find similarities among the sets of pixels (also known as images) that share a tag.

What will count as similarities? That will depend on the algorithms I tell the system to apply and the type of neural network I have it build. I’ll obviously use algorithms designed for finding patterns among pixels and not among, say, words. The neural network might look for edges in the photos, or for similarities of colors or contrasts, or how fuzzy and green the lower left corners are, or I don’t know what. It’s not going to tell me what sorts of patterns it’s looking at if only because some of those patterns will not make sense according to the way that humans think about visual information. For example, for humans edges are not simply one pattern among others. To us, edges signify the boundaries of things, and we deeply care about things; edges are a crucial way we divide up the world to find meaning. To a neural network an edge is just a pattern of contiguous pixels that have pixels on either side of them that have more in common with one another than they do with the pixels on the other side of those contiguous pixels.

Beyond that, the ML doesn’t know what an edge is, or even that edges might be interesting. If edges help the ML sort the training data accurately, then it will pay attention to edges. If not, then not.

## Tag ML as “weird”

This is already making machine learning sound too much like how humans go about clustering photos. So [Emily Reif](https://ai.google/research/people/106150), another PAIR developer, took me a few steps further into the weirdness of ML, specifically neural networks, by asking me to imagine a pattern of pixels that makes sense to a human learning how to distinguish photos of, say, the Arctic and a jungle. We humans might note that brightness and two big expanses of relatively uniform color (probably white and blue) correlates well with photos tagged “Arctic” and not so well with photos of jungles.

![0*s0gNsgibnEjwWWx7](../_resources/392d5d92db839b39400e0afa2dfb6179.jpg)
![0*gNKDxGuXYaTFG_FN](../_resources/7fabe9ea7668c94757b3abed7a965d69.jpg)

Photo by [Markus Spiske](https://unsplash.com/photos/QFBLyqdUoD4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/arctic?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText). No rights reserved.

Of course, that won’t work for all Arctic photos, because we humans recognize some of them based on knowledge not in that pattern. For example:

![0*gNKDxGuXYaTFG_FN](../_resources/3dc72cd1d75c8a8c975b4eacfdaf2585.jpg)
![0*s0gNsgibnEjwWWx7](../_resources/9090611c21084e3501ce4fef1f2b2c61.jpg)

Photo by [Ruvim Miksanskiy](https://unsplash.com/photos/8bfbEaC4YpY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/arctic-seal?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) No rights reserved.

We recognize that that adorable pixel pattern depicts a seal, and we know — independent of the photo — that seals are found in polar regions. A machine learning system trained on photos of Arctic landscapes would not start off knowing any such facts.

Nevertheless, given Emily’s sample algorithm — two big blocks of color is a probabilistic indicator of an Arctic photo — we humans might draw a graph for ourselves that looks at those features of the photos in our training set to see if they cluster photos accurately enough for our purposes. Let’s say this is what we get:

![0*P774ZvkpygBnBU-V](../_resources/717e643bdf96827689b0e755f378aaba.png)
![0*P774ZvkpygBnBU-V](../_resources/6e586b680621d0c432a98a93c462452d.png)

Well, that worked out super well, which is an advantage of creating an over-simplified example. Not only do those two axes cleanly divide the two types of photos, these are axes we humans understand.

Of course, what we count as “two uniformities” is complex and at least somewhat arbitrary. Suppose there’s one very big blue splotch and a little white one, but both the colors are quite uniform and untextured. Suppose they’re both big but not as uniform. Suppose one is yellow and the other is brown. We’ll want to choose criteria that result in good, clean clustering.

But it gets more complex, for the machine learning system doesn’t come into the process with ideas like brightness and uniformity in mind, much less a preconceived notion of what to look for when trying to tell a jungle from an icescape. It just knows about numbers. With images, the numbers represent the three colors that compose each pixel of an image: how much red, green, and blue. The ML paws through this big bucket of numbers looking for correlations.

Emily then makes the weirdness of ML more apparent. First, she points out that you could rotate the prior chart any degree you want and it will still work separating the jungles from the Arctics:

![0*tSE2MvzxRMwqnaKu](../_resources/19aeba9a7f962cbb888eacfae165cd86.png)
![0*tSE2MvzxRMwqnaKu](../_resources/9498d0926a389c53797e6b3816a66c6b.png)

This view does just as well in separating the two types of photos. But — and here’s the point — what would you label the new vertical and horizontal axes? The *2-block uniformity of the brightness* and the *brightness of the 2-block uniformity*? The latter of those phrases seems to make some sense, but does the first? There’s no particular reason why it should. ML’s axes express mathematical relationships among the elements in that big bucket of numbers — a relationship that may not correspond to the vectors human cultures and languages use to organize our thinking and perceptions. ML doesn’t care whether we humans have words or concepts for the mathematical relationships it notices.

And then Emily takes the next step into the vortex: We’ve been separating images via two-dimensional charts, but if that’s all it takes to learn how to distinguish jungle from Arctic photos, then you probably don’t need machine learning. But not all Arctic photos have two uniform blocks, nor are all those uniform blocks the same. An ML system looks at many possible mathematical relationships among the pixels. Even a modest layer in a neural network will note 128 of them. If we wanted to make a chart of these, it would be 128-dimensional. We humans cannot imagine that, but machine learning systems don’t have imaginations. They just have math, and that math can handle a whole heck of a lot of dimensions.

* * *

The many-dimensional models machine learning systems build for themselves are complex for sure. But before I can let machine learning scour my sample images for relationships that I may not have words for, I have to write a little viewer that will let me enter a tag and show me all the photos with that tag, so I can verify that I didn’t bollix up the data.

That should be simple, right?
Right?

*Find out in David’s next post in which he learns how difficult it can be to figure out what data a machine learning system can learn from …*

## ***Series outline***

*Part 1: Having a bad idea. *Getting an initial idea of how the availability and nature of data can shape the machine learning apps we build. Also: ML can be weird in how it “thinks” about data.

*Part 2: The machine trains me. *We have images and tags. But what’s the right combination for training the machine learning? Images with multiple tags? Choose one tag per image? If so, which? What sorts of information do we want the tags to convey?

*Part 3: How machine learning trains itself, or, That’s one hot array! *Getting further into the details of providing image data in the way my chosen algorithms want it. Baby-stepping through the machine learning process. Meaningful tags become semantics-free “one hot arrays.” Also: Human intuition vs. machine learning.

*Part 4: Learning from the data. *Montage-based failures at training the system. Accuracy and validation accuracy. Over-fitting. Finally: success!

*Part 5: Tuning the data and the training. *Convolutional networks. Hyperparameters and the many ways in which human beings control the training of an AI system. Writing a JavaScript application that uses the trained model.

*Part 6: Having a bad idea. *How do we define success? Lessons learned.