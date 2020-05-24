How video streaming works on the web: An introduction

# How video streaming works on the web: An introduction

> Note: this article is an introduction to video streaming in JavaScript and is mostly targeted to web developers. A large part of the examples here make use of HTML and modern JavaScript (ES6).

>  If you’re not sufficiently familiar with them, you may find it difficult to follow through, especially the code example.

> Sorry in advance for that.

### The need for a native video API

From the early to late 2000s, video playback on the web mostly relied on the flash plugin.

![1*MnU98AZYYD0aqjUtQtWHMQ.png](../_resources/d958f3ea99ffd79e3ceba0607eb17fd3.png)
![1*MnU98AZYYD0aqjUtQtWHMQ.png](../_resources/fba75902e5f11feafba7689245ea890d.png)

Screen warning that the user should install the flash plugin, at the place of a video

This was because at the time, there was no other mean to stream video on a browser. As a user, you had the choice between either installing third-party plugins like flash or silverlight, or not being able to play any video at all.

To fill that hole, the [WHATWG](https://en.wikipedia.org/wiki/WHATWG) began to work on a new version of the HTML standard including, between other things, video and audio playback *natively* (read here: without any plugin). This trend was even more accelerated following [Apple stance on flash for its products](https://www.apple.com/hotnews/thoughts-on-flash/).

This standard became what is now known as HTML5.
![1*D7JX0dvR-CWOa9ynsCIwqA.png](../_resources/4ddd2d9e778a814c5ce23a9f17fb4fd3.png)

The HTML5 Logo. HTML5 would be changing the way video are streamed on web pages
Thus HTML5 brought, between other things, the `<video>` tag to the web.

This new tag allows you to link to a video directly from the HTML, much like a `<img>` tag would do for an image.

This is cool and all but from a media website’s perspective, using a simple img-like tag does not seem sufficient to replace our good ol' flash:

- we might want to switch between multiple video qualities on-the-fly (like YouTube does) to avoid buffering issues
- live streaming is another use case which looks really difficult to implement that way
- and what about updating the audio language of the content based on user preferences while the content is streaming, like Netflix does?

Thankfully, all of those points can be answered *natively* on most browsers, thanks to what the HTML5 specification brought. This article will detail how today’s web does it.

### The video tag

As said in the previous chapter, linking to a video in a page is pretty straightforward in HTML5. You just add a video tag in your page, with few attributes.

For example, you can just write:
![resize.jpg](../_resources/2654e34d489309f487f3b0f6e017b0a0.jpg)

This HTML will allow your page to stream *some_video.mp4* directly on any browser that supports the corresponding codecs (and HTML5, of course).

Here is what it looks like:
![1*bfAhjyk_5XRnFsLHTLwaXA.png](../_resources/51c85cead3703140cf5d68201a76cc7e.png)

Simple page corresponding to the previous HTML code

This video tag also provides various APIs to e.g. play, pause, seek or change the speed at which the video plays.

Those APIs are directly accessible through JavaScript:

However, most videos we see on the web today display much more complex behaviors than what this could allow. For example, switching between video qualities and live streaming would be unnecessarily difficult there.

![1*r1IRKN1x9_FDqsgPy5_6VQ.png](../_resources/c0633c06270779a90bfdecf9c0140ef1.png)

YouTube displays some more complex usecases: quality switches subtitles a tightly controlled progressive-download of the video…

All those websites actually do still use the video tag. But instead of simply setting a video file in the *src* attribute, they make use of much more powerful web APIs, the **Media Source Extensions**.

### The Media Source Extensions

The “Media Source Extensions” (more often shortened to just “MSE”) is a specification from the W3C that most browsers implement today. It was created to allow those complex media use cases directly with HTML and JavaScript.

Those “extensions” add the **MediaSource** object to JavaScript. As its name suggests, this will be the source of the video, or put more simply, this is the object representing our video’s data.

![1*9ouQpEB7aG91e1PMJ3cDWg.png](../_resources/34d1f3fa5cb89b50b72cddd70e6cdef3.png)

The video is here “pushed” to the MediaSource, which provides it to the web page

As written in the previous chapter, we still use the HTML5 video tag. Perhaps even more surprisingly, we still use its *src* attribute. Only this time, we're not adding a link to the video, we're adding a link to the **MediaSource** object.

You might be confused by this last sentence. We’re not talking about an URL here, we’re talking about an abstract concept from the JavaScript language, how can it be possible to refer to it as an URL on a video tag, which is defined in the HTML?

To allow this kind of use cases the W3C defined the `URL.createObjectURL` static method. This API allows to create an URL, which will actually refer not to a resource available online, but directly to a JavaScript object created on the client.

This is thus how a MediaSource is attached to a video tag:

And that’s it! Now you know how the streaming platforms play videos on the Web!

… Just kidding. So now we have the MediaSource, but what are we supposed to do with it?

The MSE specification doesn’t stop here. It also defines another concept, the SourceBuffers.

### The Source Buffers

The video is not actually directly “pushed” into the MediaSource for playback, SourceBuffers are used for that.

A MediaSource contains one or multiple instances of those. Each being associated to a type of content.

To stay simple, let’s just say that we have only three possible types:

- *audio*
- *video*
- *both audio and video*

> In reality, a “type” is defined by its MIME type, which may also include information about the media codec(s) used

SourceBuffers are all linked to a single MediaSource and each will be used to add our video’s data to the HTML5 video tag directly in JavaScript.

As an example, a frequent use case is to have two source buffers on our MediaSource: one for the video data, and the other for the audio:

![1*qkggUw4dRuvp3cthW3F4sw.png](../_resources/4e1fe70756cf2840cf334ce2a18b2020.png)

Relations between the video tag, the MediaSource, the SourceBuffers and the actual data

Separating video and audio allows to also manage them separately on the server-side. Doing so leads to several advantages as we will see later. This is how it works:

And voila!

We’re now able to manually add video and audio data dynamically to our video tag.