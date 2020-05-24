The scientist who spots fake videos

*Nature*|News: Q&A

### Sharing

- [![Print](../_resources/62bfd4e0ded7c3aaf13f7742ffe41af4.gif)](#)

-

#### [![Share/bookmark](../_resources/ce2f04c58cf5d4ca17679ec0e519029a.gif)](#)

# The scientist who spots fake videos

Hany Farid discusses how to detect image manipulations — and the increasing sophistication of forgers.

- [Elizabeth Gibney](https://www.nature.com/news/the-scientist-who-spots-fake-videos-1.22784#auth-1)

06 October 2017

## Article tools

[Rights & Permissions](https://s100.copyright.com/AppDispatchServlet?author=Elizabeth+Gibney&title=The+scientist+who+spots+fake+videos&publisherName=NPG&contentID=10.1038%2Fnature.2017.22784&publicationDate=10%2F06%2F2017&publication=Nature+News)

![](../_resources/e256a9ae33e86e1014aac51da42754bc.jpg)
Eli Burakian/Dartmouth College
Hany Farid.

Hany Farid, a computer scientist at Dartmouth College in Hanover, New Hampshire, specialises in detecting manipulated images and videos. Farid, who provides his services to clients as varied as universities, media organizations, and law courts, says that image manipulation is becoming both more frequent and more sophisticated. He spoke to *Nature* about the arms race to stay ahead of the forgers.

## Where do you start when trying to spot a fake image?

One simple but powerful technique is reverse image search. You give the image to a site such as Google Image Search or TinEye, and they show you all other instances of it. A [project at Columbia University](http://www.ee.columbia.edu/ln/dvmm/memex/index.html#About), in New York City, is taking this to the next level, and starting to find parts of images that have been repurposed from other images**. **

****
**
> “I’ve seen the technology get good enough that I’m now very concerned”

**

****Generally, we think about which patterns, geometries, colours or structures are going to be disrupted when someone manipulates a photo. For example, when people add an object into a scene, we know that where they put the shadow is usually wrong. A viral video called [Golden Eagle Snatches Kid](https://www.youtube.com/watch?v=CE0Q904gtMI) from 2012 is one of my favourite examples. It took us only 15 minutes of analysis to show shadow inconsistencies: the eagle and baby were computer-generated.

## What about if fake images make only slight tweaks?

There are a number of analyses we can do. In a colour picture, every pixel needs three values — corresponding to the amounts of red, green and blue at that point. But in most cameras, every pixel records just one colour, and the camera fills in the gaps by taking the average values of the pixels around it. This means that, for any given colour in an image, each missing pixel has a particular correlation with its neighbours, which will be destroyed if we add or airbrush something, and we can detect that**.

**Another technique is JPEG compression. Almost every image is stored in a JPEG file, which throws away some information to save on storage. There is a huge amount of variation in how each camera does that. If a JPEG is unpacked — opened in Photoshop — and then put back together, it is always repackaged slightly differently, and we can detect that. I wish you could just upload any image and we could tell you if it’s real or not, but it’s still a very difficult process and requires expertise to understand different components.

## Who uses your digital forensic services?

I do analysis for organisations such as the Associated Press, Reuters, and *The New York Times*. There are only a handful of academics worldwide who are specialists in this, so it doesn’t scale — and that means you can only do the analysis of really high-stakes images. But there are efforts under way to scale this up. Last year, the US Defense Advanced Research Projects Agency (DARPA) got into this game with a [large project](https://www.darpa.mil/program/media-forensics) of which I’m part. Over the next five years they’re trying to create a system that will allow you to analyse hundreds of thousands of images a day. It’s a very ambitious programme.

I also do a lot of work in the courts. For example, here in the United States, child pornography is illegal, but computer-generated child pornography counts as 'protected speech' under the First Amendment. If someone’s arrested they might say that the offending image isn’t real, and I might have to prove that it is. I also get lots of e-mails from people about photo hoaxes — almost daily.

## Do you apply your techniques to scientific papers?

I have worked on many cases of scientific misconduct, hired by universities conducting internal investigations. When I visited the US Office of Research Integrity recently, they asked me “how do we get our hands on automated tools?” The reality is we’re still not there. But creating something that uses some of the tools, such as clone detection, which looks to see whether parts of an image have been copied and pasted from elsewhere, would be possible as a semi-automated process looking at dozens, not millions, of images a day. It’s something my colleagues and I are thinking about, and it’s a small but not insignificant part of the DARPA programme.

## How about fake videos?

Researchers are now able to splice together footage to create videos of famous people seeming to say things they never said — for instance, [this video of President Obama](https://na01.safelinks.protection.outlook.com/?url=http%3A%2F%2Ffutureoffakenews.com%2F&data=02%7C01%7CHany.Farid%40dartmouth.edu%7C99cdc415649647d8c9f008d4f4655b5e%7C995b093648d640e5a31ebf689ec9446f%7C0%7C0%7C636402163572640647&sdata=9HhC%2FNxrb9JIPwpwxHIoGjZd8bZVHsP7fP9xqlZPAog%3D&reserved=0). And they can create fake images or short videos using machine learning techniques: in particular, [generative adversarial networks](https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.nature.com%2Fnews%2Fastronomers-explore-uses-for-ai-generated-images-1.21398&data=02%7C01%7CHany.Farid%40dartmouth.edu%7C99cdc415649647d8c9f008d4f4655b5e%7C995b093648d640e5a31ebf689ec9446f%7C0%7C0%7C636402163572640647&sdata=DCWL29NaKM73X%2BabDBN%2FLg%2BDOUbwt%2BOKqOmRvIBlf%2FA%3D&reserved=0) (GANs), which learn to generate fake content. These pit a network that generates fake content against a ‘classifer’ network that attempts to discriminate between real and fake content, so that the faking network rapidly improves.

I’ve seen the technology get good enough that I’m now very concerned. In 5 or 10 years, this is going to get really good. At some point we will reach a stage where we can generate realistic video, with audio, of a world leader, and that’s going to be very disconcerting. I would say that the field of digital forensics is now behind in video.

## How can you detect fake video?

JPEG compression has an analogous construct in video, which is a bit harder to detect because video uses a more sophisticated version. Another approach is to use machine learning for detection. But we’re taking an approach similar to what we do with images — which is based on the observation that computer-generated content lacks the imperfections that are present in a recorded video. It’s created in almost too perfect a world. So one of the things we look at is, are we not seeing the statistical and geometric patterns we’d expect to see in the physical world?

Another technique is based on some [beautiful work by William Freeman and colleagues at the Massachusetts Institute of Technology in Cambridge](http://people.csail.mit.edu/mrub/vidmag/#people), who showed how if you magnify really small changes in a video of a person, you can see subtle changes in the colours in their face that correspond to their pulse rate. We showed that you can use this to distinguish real people from computer-generated people.

## Couldn’t machine learning algorithms learn to include these features?

Perhaps in principle. But in practice, these algorithms have limited time and training data, and there is little control over which features a neural network will pick up on to discriminate between real and fake videos. A GAN is only trying to fool the classifier it’s trained on. That’s no guarantee that it will learn all aspects of what makes an image or video real or fake, or that it will fool another classifier.

My adversary will have to implement all the forensic techniques that I use, so that the neural network can learn to circumvent these analyses: for example, by adding a pulse in. In that way, I’ve made their job a little harder.

It’s an arms race. As we are developing faster, folks are creating more sophisticated technology to augment audio, images and video. The way this is going to end is that you take the ability to create a perfect fake out of the hands of the amateur. You make it harder, so it takes more time and skill, and there’s a greater risk of getting caught.

Nature
doi:10.1038/nature.2017.22784

# [Related stories and links](#)

## From nature.com

-

# [Image doctoring must be halted](https://www.nature.com/doifinder/10.1038/546575a)

28 June 2017
-

# [Astronomers explore uses for AI-generated images](https://www.nature.com/doifinder/10.1038/542016a)

01 February 2017
-

# [Problematic images found in 4% of biomedical papers](https://www.nature.com/doifinder/10.1038/nature.2016.19802)

22 April 2016
-

# [The image detective who roots out manuscript flaws](https://www.nature.com/doifinder/10.1038/nature.2015.17749)

12 June 2015

# Author information

For the best commenting experience, [please login or register as a user](https://www.nature.com/foxtrot/svc/login?type=commenting) and agree to our [Community Guidelines](https://www.nature.com/info/community-guidelines.html). You will be re-directed back to this page where you will see comments updating in real-time and have the ability to recommend comments to other users.

[Comments]()

# Comments  [Subscribe to comments](https://naturenews.disqus.com/the_scientist_who_spots_fake_videos/latest.rss)

There are currently no comments.