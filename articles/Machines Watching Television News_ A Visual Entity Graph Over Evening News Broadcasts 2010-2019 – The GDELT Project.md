Machines Watching Television News: A Visual Entity Graph Over Evening News Broadcasts 2010-2019 – The GDELT Project

# [Machines Watching Television News: A Visual Entity Graph Over Evening News Broadcasts 2010-2019](https://blog.gdeltproject.org/machines-watching-television-news-a-visual-entity-graph-over-evening-news-broadcasts-2010-2019/)

 ** December 13, 2019

   [![2019-global-entity-graph-geg-1064x410.png](../_resources/f2df327dfaa4273f3e1c0e69cfd59616.png)](https://blog.gdeltproject.org/machines-watching-television-news-a-visual-entity-graph-over-evening-news-broadcasts-2010-2019/)

What would it look like to have machines watch a decade of ABC, CBS and NBC evening television news broadcasts and describe what they see, creating a minute-by-minute chronology of the visual themes and narratives that have defined global events 2010-2019? Today we are excited to unveil the results: a powerful new non-consumptive visual chronology, using data from the Internet Archive's [Television News Archive](https://archive.org/details/tv) and Google's [Cloud Video API](https://cloud.google.com/video-intelligence/) and building on our [pilot one week analysis](https://blog.gdeltproject.org/ai-watching-television-news-deep-learning-meets-a-week-of-television/) from earlier this year to watch more than 11,000 broadcasts and catalog the dominant visual themes and activities depicted over almost a decade of evening television news broadcasts.

Despite its rich visual-first nature, television news today is primarily explored through the modality of text. The Internet Archive's [Television News Archive](https://archive.org/details/tv) has been a leader in this space, helping to popularize timecoded keyword search of closed captioning transcripts in the library context and exploring new [research interfaces](https://api.gdeltproject.org/api/v2/summary/summary?d=iatv) to television. While these keyword search systems provide incredible opportunities for [exploring coverage trends](https://api.gdeltproject.org/api/v2/summary/summary?d=iatv) and can be read by textual deep learning systems to [catalog the things and themes](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/) they mention, at the end of the day, the very visual world that separates television from radio and the online world is absent from such analyses.

At the same time, the last few years have brought profound advances in machine vision, with algorithmic visual understanding moving from the research lab to production everyday use. What would it look like to have a state-of-the-art machine learning system watch a decade of television news broadcasts across "the big three" networks and catalog their visual themes?

Earlier this year we [explored this vision](https://blog.gdeltproject.org/ai-watching-television-news-deep-learning-meets-a-week-of-television/) using a single week of television news, demonstrating the [wealth of insights](https://www.forbes.com/sites/kalevleetaru/2019/09/03/a-look-back-at-how-googles-ai-sees-a-week-of-television-news-and-the-world-of-ai-video-understanding/) that become visible. What happens when this same approach is applied over almost a decade?

To explore these questions further, the half-hour evening television news broadcasts of ABC, CBS and NBC for July 2009 – November 2019 from the Internet Archive's [Television News Archive](https://archive.org/details/tv) were analyzed within a restricted access non-consumptive computational digital reference library using Google's [Cloud Video API](https://cloud.google.com/video-intelligence/), including its [labeling feature](https://cloud.google.com/video-intelligence/docs/analyze-labels) in which it visually analyzes each second of footage and assigns a list of predefined labels describing the objects and activities depicted within.

The end result is a list of the visual themes (primarily objects and activities) found in each broadcast by minute, charting its visual narratives. Such a chronology offers a powerful and unique counterpart to the [textual chronology](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/) of its closed captioning, allowing researchers for the first time to consider the visual dimension of television news.

What are the visual themes that are associated with the key narratives and events of the past decade? Through combining with the [captioning chronology](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/), it becomes possible to examine what kinds of imagery is typically depicted onscreen when a given topic is discussed and how that imagery has changed over the years. Longitudinal questions such as the amount of coverage by month over the past decade devoted to civil mobilizations like protests can also be explored for the first time. For example, using this new dataset it takes only a simple search to find that the two one-minute periods in the past decade with the most protest imagery were on [NBC at 5:39PM PST on February 11, 2017](https://archive.org/details/KNTV_20170212_013000_NBC_Nightly_News_With_Lester_Holt/start/540/end/600) and [ABC at 5:34PM PST on March 27, 2016](https://archive.org/details/KGO_20160328_003000_ABC_World_News/start/240/end/300), with 48 seconds and 46 seconds, respectively. This enables an entirely new approach to understanding visual narratives by using machines to sift through vast archives of video.

Perhaps most importantly, this new dataset will allow researchers to explore for the first time how a better understanding of the visual dimensions of news might help combat the spread of falsehoods and better assess the diffusion of contested narratives and inorganic campaigns. What might we learn from the rich visual processes of broadcast journalism that could be applied to help increase trust in digital journalism and contextualize the news in ways that combats misunderstanding and falsehood?

The dataset consists of one file per day, running from July 15, 2010 through November 30, 2019, similar to the [transcript-based entity graph](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/). Each file is in newline delimited JSON format, with each row representing one minute of a broadcast and containing an array of all of the visual entities identified by the Video API from that minute, ordered by the number of seconds they were depicted during that minute.

All annotations were performed using the "v1p3beta1" model of the Video API.

- **date**. The date and time in UTC of a specific minute of a given broadcast, rounded to the minute.
- **iaShowId**. The unique identifier assigned by the Internet Archive to this broadcast.
- **station**. The station on which this broadcast aired.
- **showName**. The human-readable name of the show.
- **iaClipUrl**. The URL of the Internet Archive's Television News Archive page to view the clip of this minute of the broadcast.
- **numOCRChars**. The total number of characters of text identified through OCR. The Video API performs [per-frame OCR](https://cloud.google.com/video-intelligence/docs/text-detection), which for the purposes of simplification we sample at 1fps and count the total number of identified characters and sum by minute.
- **numShotChanges**. The Video API identifies the number of [scene/camera transitions](https://cloud.google.com/video-intelligence/docs/analyze-shots). Given that broadcast evening news tends to use fixed camera positions, we instruct the Video API to assume a stationary camera, so this may overidentify camera transitions for field segments using a mobile camera.
- **numSpeakerChanges**. Using the Video API's "video" speech transcription model with [speaker diarization](https://cloud.google.com/video-intelligence/docs/transcription) enabled, we count the number of speaker transitions each minute.
- **numSpokenWords**. Using the Video API's "video" speech transcription model, we count the total number of [words spoken](https://cloud.google.com/video-intelligence/docs/transcription) each minute.
- **numDistinctEntities**. The total number of unique [visual entities](https://cloud.google.com/video-intelligence/docs/analyze-labels) (called "[labels](https://cloud.google.com/video-intelligence/docs/analyze-labels)" in the Video API's parlance) identified during the given minute. Multiple appearances of a given entity will be recorded as a single entry with "numSeconds" recording its total screen time.
- **entities**. A JSON array containing the list of distinct visual entities identified by the API for this minute of this broadcast. Multiple appearances of the same entity during this minute will be recorded as a single entry.
    - **name**. The human name of this visual entity such as "land vehicle" or "city."
    - **mid**. Provides the unique Google-assigned ID of this visual entity.
    - **numSeconds**. The total number of seconds during this minute (up to 60) in which this entity was depicted.
    - **categories**. An optional JSON array containing a list of distinct visual entities that represent the parent category headings for this entity in the overall visual taxonomy used by the Video API. For example, the entity "circle" will have "shape" in its categories list, representing that under Google's taxonomy, a "circle" is a kind of "shape." Not all entities have corresponding parent categories and some may have multiple parents categories.
        - **name**. The human name of this visual entity such as "land vehicle" or "city."
        - **mid**. Provides the unique Google-assigned ID of this visual entity.

The complete set of daily files can be downloaded below (currently through November 30, 2019):

- http://data.gdeltproject.org/gdeltv3/iatv/vgeg/MASTERFILELIST.TXT

The dataset is also available in Google's BigQuery:

- https://bigquery.cloud.google.com/table/gdelt-bq:gdeltv2.vgeg_iatv

Note that this is a preliminary dataset that may be missing some shows or have null or incomplete values for some fields, while some design decisions such as using a fixed camera definition may have unintended consequences depending on the balance of studio, fixed and mobile reporting composition in each broadcast. We are excited to explore this dataset alongside of you to learn how we can use machines to peer for the first time into the visual world of the news. Remember that this dataset was constructed entirely by machine, so you will undoubtedly encounter errors and all labels are the result of algorithmic decision, not human editorialization.

Stay tuned for a series of analyses and a human-friendly research interface to this data coming shortly!

We're tremendously excited to see the kinds of advanced multimodal visual analyses you're able to do with this powerful new non-consumptive dataset!