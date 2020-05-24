Interview with Ken Thompson

  [![RSS](../_resources/ce0bdea0f69406d00319838285edbbbc.gif)](http://www.drdobbs.com/rss/open-source)

## Open Source

[**Tweet](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fwww.drdobbs.com%2Fopen-source%2Finterview-with-ken-thompson%2F229502480&ref_src=twsrc%5Etfw&related=dr_dobbs&text=Interview%20with%20Ken%20Thompson&tw_p=tweetbutton&url=http%3A%2F%2Fwww.drdobbs.com%2Fopen-source%2Finterview-with-ken-thompson%2F229502480&via=dr_dobbs)

|     |
| --- |
|     |

[inShare.](#)

[(L)](https://plus.google.com/share?app=110&url=http%3A%2F%2Fwww.drdobbs.com%2Fopen-source%2Finterview-with-ken-thompson%2F229502480)

[(L)](http://www.addthis.com/bookmark.php?v=250&winname=addthis&pub=Dr.Dobbs&source=tbx-250&lng=en-US&s=stumbleupon&url=http://www.drdobbs.com/open-source/interview-with-ken-thompson/229502480&title=Interview%20with%20Ken%20Thompson&ate=AT-Dr.Dobbs/-/fs-0/4d4fc3809f4d8545/1&sms_ss=1&at_xt=1&CXNID=2000001.5215456080540439074NXC&pre=http%3A%2F%2Fwww.drdobbs.com%2F&tt=0)[(L)](http://www.drdobbs.com/open-source/interview-with-ken-thompson/229502480#)[![rss.gif](../_resources/a7e0fc007b70e9f038ee9cc0a643e9c7.gif)](#) [![share_print_icon.gif](../_resources/0c486c5d68042fb93563cf2052461b70.gif)](http://www.drdobbs.com/article/print?articleId=229502480&siteSectionName=open-source)[Permalink](http://www.drdobbs.com/open-source/interview-with-ken-thompson/229502480#)

# Interview with Ken Thompson

By [**Andrew Binstock**](http://www.drdobbs.com/authors/Andrew-Binstock), May 18, 2011

[Post a Comment](http://www.drdobbs.com/open-source/interview-with-ken-thompson/229502480#disqus_thread)

The creator of UNIX discusses writing UNIX, the Go language, and collaborating with Dennis Ritchie

[The Japan Prize](http://www.japanprize.jp/en/index.html), one of the highest honors awarded for outstanding contribution to science and technology, was awarded jointly this year to Ken Thompson and Dennis Ritchie for the creation of UNIX. The prize is normally given to the recipients at a lavish banquet in Tokyo attended by the emperor. However, due to the April earthquake and tsunami, the prizes this year were distributed at the honorees' place of work. I was able to attend the ceremony for Ken Thompson, held at Google headquarters, where he currently works. After the ceremony, he consented to this exclusive interview.

* * *

***DDJ:*** Congratulations on winning this prize.
**KT:** Thanks.

### Developing UNIX

***DDJ:*** You've received a lot of awards over the years for UNIX. At what point in UNIX's development did it become clear it was going to be something much bigger than you'd anticipated?

**KT:** The actual magnitute, *that* no one could have guessed. I gather it's still growing now. I thought it would be useful to essentially anybody like me because it was not built for someone else or some third party. That was a perjorative term then. It was written for Dennis and me and our group to do its work. And I think it would have been useful to anybody who did the kind of work that we did. And therefore, I always thought it was something really good that was going to take off.

Especially the language [C]. The language grew up with one of the rewritings of the system and, as such, it became perfect for writing systems. We would change it daily as we ran into trouble building UNIX out of the language and we'd modify it for our needs.

***DDJ:*** A symbiosis of sorts…

**KT:** Yeah. It became the perfect language for what it was designed to do. I always thought the language and the system were widely applicable.

***DDJ:*** In the presentation today, it mentioned that UNIX was open source. Was UNIX open source from the beginning?

**KT:** Well there was no such term as "open source" then.

***DDJ:*** I was under the impression that UNIX really became open source with the Berkeley distribution.

**KT:** No, we charged $100, which was essentially the reproduction cost of the tape, and then send it out. And we distributed, oh, probably close to 100 copies to universities and others.

### Go Language

***DDJ:*** Skipping several decades of work, let's speak about Go. I was just at the Google I/O Conference, where it was announced that Go will be supported on the Google App Engine. Does that presage a wider adoption of Go within Google, or is it still experimental?

**KT:** It's expanding every day and not being forced down anybody's throat. It's hard to adopt it to a project inside of Google because of the learning curve. It's brand new and there aren't good manuals for it, except what's on the Web. And then, of course, its label of being experimental, so people are a little afraid. In spite of that, it's growing very fast inside of Google.

***DDJ:*** In the presentation before the awarding of the Japan Prize today, you were quoted on the distinction between reasearch and development. [The former, Thompson stated, was directionless, whereas development had a specific goal in mind.] So in that context, is Go experimental?

**KT:** Yes. When the three of us [Thompson, Rob Pike, and Robert Griesemer] got started, it was pure research. The three of us got together and decided that we hated C++. [laughter]

***DDJ:*** I think there'd be a lot of people who are with you on that.

**KT:** It's too complex. And going back, if we'd thought of it, we'd have done an object-oriented version of C back in the old days.

***DDJ:*** You're saying you would have?

**KT:** Yes, but we were not evangelists of object orientation. [Returning to Go,] we started off with the idea that all three of us had to be talked into every feature in the language, so there was no extraneous garbage put into the language for any reason.

***DDJ:*** It's a lean language, indeed.

### Collaboration with Dennis Ritchie

***DDJ:*** Returning to UNIX, for a moment, when you and Dennis worked together, how did that collaboration operate? Were you working side by side?

**KT:** I did the first of two or three versions of UNIX all alone. And Dennis became an evangelist. Then there was a rewrite in a higher-level language that would come to be called C. He worked mostly on the language and on the I/O system, and I worked on all the rest of the operating system. That was for the PDP-11, which was serendipitous, because that was the computer that took over the academic community.

***DDJ:*** Right.

**KT:** We collaborated every day. There was a lunch that we went to. And we'd talk over lunch. Then, at night, we each worked from our separate homes but we were in constant communication. In those days, we had mail and writ (pronounced 'write'), and writ would pop up on your screen and say there was a message from so-and-so.

***DDJ:*** So, IM essentially.

**KT:** Yes, IM. There was no doubt about that! And we discussed things from home with writ. We worked very well together and didn't collaborate a lot except to decide who was going to do what. Then we'd run and very independently do separate things. Rarely did we ever work on the same thing.

***DDJ:*** Was there any concept of looking at each other's code or doing code reviews?

**KT:** [Shaking head] We were all pretty good coders.
***DDJ:*** I suspect you probably were! [Laughter]

### SCM

***DDJ:*** Did you use any kind of source code management product when working together?

**KT:** No, those products really came later; after UNIX. We had something like it, which we called "the code motel" because you could check your code in but you couldn't check it out! So, really, no we didn't.

***DDJ:*** I bet you use SCM today in your work on Go.
**KT:** Oh, yes, Google makes us do that!