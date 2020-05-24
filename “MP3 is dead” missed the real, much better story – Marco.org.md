“MP3 is dead” missed the real, much better story – Marco.org

# [Marco.org](https://marco.org/)

I’m [Marco Arment](https://marco.org/about): a programmer, writer, podcaster, geek, and coffee enthusiast.

 [Apps](https://marco.org/apps) • [Podcast](http://atp.fm/) • [Twitter](https://twitter.com/marcoarment) • [About](https://marco.org/about)

##   [“MP3 is dead” missed the real, much better story](https://marco.org/2017/05/15/mp3-isnt-dead)

 May 15, 2017  [∞](https://marco.org/2017/05/15/mp3-isnt-dead)

If you [read](http://gizmodo.com/developers-of-the-mp3-have-officially-killed-it-1795205540)  [the](https://www.engadget.com/2017/05/12/mp3-is-dead-long-live-aac/)  [news](http://www.npr.org/sections/therecord/2017/05/11/527829909/the-mp3-is-officially-dead-according-to-its-creators), you may think the MP3 file format was recently officially “killed” somehow, and any remaining MP3 holdouts should all move to AAC now. These are all simple rewrites of[Fraunhofer IIS’ announcement](https://www.iis.fraunhofer.de/en/ff/amm/prod/audiocodec/audiocodecs/mp3.html) that they’re terminating the MP3 patent-licensing program.

[Very](https://512pixels.net/2017/05/the-mp3-isnt-dead/)  [few](https://sixcolors.com/post/2017/05/long-live-the-mp3/)  [people](https://motherboard.vice.com/en_us/article/mp3-is-not-dead) got it right. The others missed [what happened last month](https://en.wikipedia.org/wiki/MP3#Licensing.2C_ownership_and_legislation):

>

> If the longest-running patent mentioned in the aforementioned references is taken as a measure, then **> the MP3 technology became patent-free in the United States on 16 April 2017**>  when U.S. Patent 6,009,399, held by and administered by Technicolor, expired.

MP3 is no less alive now than it was last month or will be next year — the last known MP3 patents have simply expired.[1](https://marco.org/2017/05/15/mp3-isnt-dead#)[1](https://marco.org/2017/05/15/mp3-isnt-dead#fn:pFcz0p5c02)

So while there’s a debate to be had — in a moment — about whether MP3 should still be used today, Fraunhofer’s announcement has nothing to do with that, and is simply the ending of its patent-licensing program (because the patents have all expired) and a suggestion that we move to a newer, [still-patented](https://www.iis.fraunhofer.de/en/ff/amm/prod/audiocodec/audiocodecs/aaclc.html) format.

### Why still use MP3 when newer, better formats exist?

MP3 is very old, but it’s the same age as [JPEG](https://en.wikipedia.org/wiki/JPEG), which has also long since been surpassed in quality by [newer](https://en.wikipedia.org/wiki/JPEG_2000)  [formats](https://en.wikipedia.org/wiki/WebP). JPEG is still ubiquitous not because Engadget forgot to declare its death, but because it’s good enough and supported everywhere, making it the most *pragmatic* choice most of the time.[2](https://marco.org/2017/05/15/mp3-isnt-dead#)[2](https://marco.org/2017/05/15/mp3-isnt-dead#fn:pFcz0p5c0png)

AAC and other newer audio codecs can produce better quality than MP3, but the difference is [only significant at low bitrates](http://opus-codec.org/comparison/). At about 128 kbps or greater, the differences between MP3 and other codecs are very unlikely to be noticed, so it isn’t meaningfully better for personal music collections. For new music, get AAC if you want, but it’s not worth spending any time replacing MP3s you already have.

AAC makes a lot of sense for low- and medium-quality applications where bandwidth is extremely limited or expensive, like phone calls and music-streaming services, or as sound for video, for which it’s the most widely supported format.

It may seem to make sense for podcasts, but it doesn’t. Podcasters need to distribute a single file type that’s playable on the most players and devices possible, and though AAC is widely supported today, it’s *still* not as widely supported as MP3. So podcasters overwhelmingly choose MP3: among the 50 million podcast episodes in [Overcast’s](https://overcast.fm/) database, 92% are MP3, and within the most popular 500 podcasts, 99% are MP3.

And AAC is also still patent-encumbered, which prevents innovation, hinders support, restricts potential uses, and imposes burdensome taxes on anything that goes near it.

So while AAC does offer some benefits, it also brings additional downsides and costs, and the benefits aren’t necessary or noticeable in some major common uses. Even the file-size argument for lower bitrates is less important than ever in a world of ever-increasing bandwidth and ever-higher relative uses of it.[3](https://marco.org/2017/05/15/mp3-isnt-dead#)[3](https://marco.org/2017/05/15/mp3-isnt-dead#fn:pFcz0p5c0size)

Ogg Vorbis and [Opus](http://opus-codec.org/comparison/) offer similar quality advantages as AAC with ([probably](http://daringfireball.net/2007/04/wee_bit_more_on_aac)) no patent issues, which was necessary to provide audio options to free, open-source software and other contexts that aren’t compatible with patent licensing. But they’re not widely supported, limiting their useful applications.

Until a few weeks ago, there had never been an audio format that was small enough to be practical, widely supported, *and* had no patent restrictions, forcing [difficult choices](http://shaver.off.net/diary/2010/01/23/html5-video-and-codecs/) and [needless friction](http://stackoverflow.com/questions/4923136/why-doesnt-firefox-support-the-mp3-file-format-in-audio) upon the computing world. Now, at least for audio, that friction has officially ended. There’s finally a great choice without asterisks.

**MP3 is supported by everything, everywhere, and is now patent-free.** There has never been another audio format as widely supported as MP3, it’s good enough for almost anything, and now, *over twenty years* since it took the world by storm, it’s finally free.

* * *

1. There’s [some debate](http://www.tunequest.org/a-big-list-of-mp3-patents/20070226/) whether expirations of two remaining patents have happened yet. I’m not a patent lawyer, but the absolute latest interpretation would have the last one expire soon, on December 30, 2017. [↩︎](https://marco.org/2017/05/15/mp3-isnt-dead#fnref:pFcz0p5c02)

2. For photos and other image types poorly suited to PNG, of course. [↩︎](https://marco.org/2017/05/15/mp3-isnt-dead#fnref:pFcz0p5c0png)

3. Suppose a podcast debates switching from 64 kbps MP3 to 48 kbps AAC. That would only save about 7 MB per hour of content, which isn’t a meaningful amount of data for most people anymore (especially for podcasts, which are typically background-downloaded on Wi-Fi). Read the [Engadget](https://www.engadget.com/2017/05/12/mp3-is-dead-long-live-aac/) and [Gizmodo](http://gizmodo.com/developers-of-the-mp3-have-officially-killed-it-1795205540) articles, at 3.6 and 5.2 MB, respectively, and you’ve already spent more than that difference. Watch [a 5-minute YouTube video](https://www.youtube.com/watch?v=KW0eUrUiyxo) at default quality, and you’ll blow through about three times as much. [↩︎](https://marco.org/2017/05/15/mp3-isnt-dead#fnref:pFcz0p5c0size)

◆

Follow Marco.org posts: [Twitter](https://twitter.com/marco_org), [RSS feed](https://marco.org/rss), or the [alternate RSS feed](https://marco.org/rss2) in which link posts always point here first instead of their targets.

 [Follow @marcoarment on Twitter](https://twitter.com/marcoarment) if you’d like.

© 2006–2017 Marco Arment