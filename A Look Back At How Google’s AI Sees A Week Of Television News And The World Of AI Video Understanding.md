A Look Back At How Google’s AI Sees A Week Of Television News And The World Of AI Video Understanding

337 views|Sep 3, 2019, 12:44pm

# A Look Back At How Google’s AI Sees A Week Of Television News And The World Of AI Video Understanding

[![53f0770ab13af971740d1d0d324da1f3](../_resources/aed8b3ef855951b14d5f80e652cabccb.png)](https://www.forbes.com/sites/kalevleetaru/)

[Kalev Leetaru](https://www.forbes.com/sites/kalevleetaru/)Contributor![](data:image/svg+xml,%3csvg class='fs-icon fs-icon--info js-evernote-checked' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60' data-evernote-id='535'%3e%3cpath fill='%23010101' d='M28.3 38.4h3.3v-10h-3.3v10zM30 13.3c-9.2 0-16.7 7.5-16.7 16.7S20.8 46.7 30 46.7 46.7 39.2 46.7 30 39.2 13.3 30 13.3zm0 30.1c-7.4 0-13.4-6-13.4-13.4s6-13.4 13.4-13.4 13.4 6 13.4 13.4-6 13.4-13.4 13.4zM28.3 25h3.3v-3.3h-3.3V25z' data-evernote-id='940' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[AI & Big Data](https://www.forbes.com/ai-big-data)
I write about the broad intersection of data and society.
-
-
-
![960x0.jpg](../_resources/44acc71e2b1f097a5c7060fd56704424.jpg)
Getty Images
Getty

This past May I worked with the Internet Archive’s [Television News Archive](https://archive.org/details/tv) to apply Google’s suite of cloud AI APIs to analyze a week of television news coverage to examine how AI “sees” television and what insights we might gain into the world of non-consumptive deep learning-powered video understanding. Using Google’s [video](https://cloud.google.com/video-intelligence/), [image](https://cloud.google.com/vision/), [speech](https://cloud.google.com/speech-to-text/) and [natural language](https://cloud.google.com/natural-language/) APIs as lenses, more than [600GB](https://blog.gdeltproject.org/ai-watching-television-news-deep-learning-meets-a-week-of-television/) of machine annotations trace how deep learning algorithms today [understand](https://www.forbes.com/sites/kalevleetaru/2019/05/21/what-does-ai-see-when-it-watches-a-week-of-television-news/) video. What lessons can we learn about the state of AI today and how it can be applied in creative ways to catalog and explore the vast world of video?

Working with the Internet Archive’s Television News Archive, a week of television news was selected covering CNN, MSNBC and Fox News and the morning and evening broadcasts of San Francisco affiliates KGO (ABC), KPIX (CBS), KNTV (NBC) and KQED (PBS) from April 15 to April 22, 2019, totaling 812 hours of television news. This week was selected due to it having two major stories, one national (the Mueller report release on April 18th) and one international (the Notre Dame fire on April 15th).

Each of Google’s production cloud AI APIs was applied to the video collection with all features enabled. Its [Video AI](https://cloud.google.com/video-intelligence/) API was run directly on the videos natively. To test the ability to analyze videos as [sampled](https://www.forbes.com/sites/kalevleetaru/2019/06/23/using-ai-to-analyze-video-as-imagery-the-impact-of-sampling-rate/) image sequences, each video was also split into 1fps samples and each still image analyzed through Google’s [Cloud Vision](https://cloud.google.com/vision/) API. The audio stream from each video was run through Google’s [Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/) API to test its automatic captioning and both the original station-provided captioning and the automatically generated transcripts were processed using Google’s [Natural Language](https://cloud.google.com/natural-language/) API.

Today In:[Innovation](https://www.forbes.com/Innovation)![](data:image/svg+xml,%3csvg class='fs-icon fs-icon--chevron-up js-evernote-checked' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 19.8 19.8' data-evernote-id='536'%3e%3cpath transform='rotate(45.001 12.615 10.187)' d='M7.9 9h9.5v2.4H7.9z' data-evernote-id='972' class='js-evernote-checked'%3e%3c/path%3e%3cpath transform='rotate(134.999 7.586 10.187)' d='M2.8 9h9.5v2.4H2.8z' data-evernote-id='973' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

Using AI algorithms to catalog and understand video rather than humans makes it possible to assess video at scale in non-consumptive fashion, opening the door to whole-archive explorations of the lenses through which we see the world.

Today the Television News Archive is analyzed primarily through [keyword search](http://blog.archive.org/2018/02/23/tv-news-record-television-explorer-2-0-shooting-coverage-more/) of the station-provided closed captioning, with a wide range of journalists using it to do [everything](https://fivethirtyeight.com/features/biden-is-still-leading-cable-news-coverage/) from [trace](https://www.washingtonpost.com/politics/2019/04/19/actually-mueller-report-showed-that-russia-did-affect-vote/) discussion of [topics](https://www.vox.com/2019/1/7/18171945/fox-news-shutdown-border-trump-data) over time to analyze the [distinctive language](https://fivethirtyeight.com/features/how-cable-news-reacted-to-the-cohen-hearing/) of each station. However, keyword search is limited by the simple fact that the searcher must already have an idea of what they are interested in – one can’t examine an entire corpus to ask what are the most “interesting” things within.

## PROMOTED

Insights - Teradata BrandVoice

 [ ###  Designing AI That Knows How You Feel]()

Teradata BrandVoice

 [ ###  Achieve Simplification through Sentience]()

UNICEF USA BrandVoice

 [ ###  Two Years After Hurricane Harvey, Educators Are Using Lessons Learned]()

Converting captioning to [ngram](https://blog.gdeltproject.org/announcing-the-television-news-ngram-datasets-tv-ngram/) word frequency histograms, it becomes possible to run a wide range of whole-archive analyses, from visualizing [emotions](https://www.forbes.com/sites/kalevleetaru/2019/08/07/charting-the-emotions-of-television-news-a-look-at-a-decade-of-anxiety-in-the-news/) like [anxiety](https://www.forbes.com/sites/kalevleetaru/2019/08/07/charting-the-emotions-of-television-news-a-look-at-a-decade-of-anxiety-in-the-news/) over time to assessing word [correlations](https://www.forbes.com/sites/kalevleetaru/2019/07/22/using-television-news-ngrams-to-explore-linguistic-correlation/) to measuring [speaking rates](https://www.forbes.com/sites/kalevleetaru/2019/08/07/how-fast-do-people-speak-on-television-news/) to surfacing the [defining topics](https://www.forbes.com/sites/kalevleetaru/2019/08/25/uncovering-the-language-defining-each-day-a-decade-of-television-news-through-ngrams/) of each day. Such analyses allow the data itself to speak, pointing to interesting or unexpected trends.

As powerful as they are, ngrams are still extremely limited, representing language as simple ordered lists of words and groups of words, rather than semantically meaningful entities.

Using Google’s Natural Language API, a broadcast transcript suddenly becomes more than a collection of mere words: it becomes a semantic list of high-order [entities](https://www.forbes.com/sites/kalevleetaru/2019/06/08/using-googles-speech-recognition-and-natural-language-apis-to-thematically-analyze-television/) and [topics](https://www.forbes.com/sites/kalevleetaru/2019/06/08/using-googles-speech-recognition-and-natural-language-apis-to-thematically-analyze-television/) and the dependency parse trees that relate and connect them, allowing broadcasts to be cataloged semantically rather than syntactically.

Closed captioning is far from perfect and the typographical errors and imperfect transcriptions of hand-keyed captioning can impact its ability to index a broadcast, from keyword search to ngrams to natural language analysis.

Automated speech recognition has advanced to the point that Google’s Speech-to-Text API now performs on par with human transcriptionists, achieving greater than [90% match](https://www.forbes.com/sites/kalevleetaru/2019/06/09/comparing-googles-ai-speech-recognition-to-human-captioning-for-television-news/) with human-typed captions. In fact, machine captioning is now so accurate that much of the difference between the human and machine captions comes from the greater [fidelity](https://www.forbes.com/sites/kalevleetaru/2019/06/09/comparing-googles-ai-speech-recognition-to-human-captioning-for-television-news/) and [accuracy](https://www.forbes.com/sites/kalevleetaru/2019/06/09/comparing-googles-ai-speech-recognition-to-human-captioning-for-television-news/) of the machine transcript.

Closed captioning isn’t the only source of text in news broadcasts. At any given moment there is typically a tweet’s worth of [onscreen text](https://www.forbes.com/sites/kalevleetaru/2019/05/21/ai-watches-television-news-a-tweets-worth-of-onscreen-text-every-second/) in the video portion of a broadcast. OCR’ing this text makes it possible to [keyword search](https://www.forbes.com/sites/kalevleetaru/2019/06/09/googles-vision-ai-found-two-hours-of-trumps-tweets-in-a-week-of-television-news/) all of this previously inaccessible text. Scanning for Twitter handles, it is possible to flag the more than two hours of [Trump tweets](https://www.forbes.com/sites/kalevleetaru/2019/06/09/googles-vision-ai-found-two-hours-of-trumps-tweets-in-a-week-of-television-news/) shown during the analyzed week. Converting this OCR’d text into ngram tables makes it possible to perform basic [topic modeling](https://www.forbes.com/sites/kalevleetaru/2019/05/22/using-ai-to-tally-the-top-onscreen-television-topics-via-ocr-and-ngrams/) of onscreen text over time.

Of course, what makes television news unique compared with the online journalism that forms the basis of most news analyses is the visual landscape that comprises the majority of its informational transfer. Television news conveys much of its narrative through the imagery that fills the screen and it is this visual component that truly showcases the power of deep learning to unlock new modalities.

Using Google’s Video AI and Cloud Vision APIs, each broadcast can be translated into a sequence of [topical annotations](https://www.forbes.com/sites/kalevleetaru/2019/05/22/using-ai-to-tally-the-top-onscreen-television-topics-via-ocr-and-ngrams/), recording the objects and activities onscreen moment by moment. In much the same way that natural language annotations of text convert transcripts from piles of words into meaningful semantic objects and activities, video annotations translate sequences of visual imagery into meaningful [catalog tags](https://www.forbes.com/sites/kalevleetaru/2019/06/01/using-ai-to-catalog-the-visual-narratives-of-a-week-of-television-news/) allowing videos to be understood through what they [depict](https://www.forbes.com/sites/kalevleetaru/2019/06/01/using-ai-to-catalog-the-visual-narratives-of-a-week-of-television-news/).

At the presentation level, questions like average [shot length](https://www.forbes.com/sites/kalevleetaru/2019/06/03/using-googles-video-ai-to-estimate-the-average-shot-length-in-television-news/) can be readily computed. Questions about the centrality of the [human face](https://www.forbes.com/sites/kalevleetaru/2019/05/21/ai-watching-television-news-the-importance-of-the-human-face-to-television-journalism/) to news coverage can also be trivially answered using such annotations, confirming that upwards of [70%](https://www.forbes.com/sites/kalevleetaru/2019/05/21/ai-watching-television-news-the-importance-of-the-human-face-to-television-journalism/) of television news features a human face in some way. Deeper questions like the [emotion](https://www.forbes.com/sites/kalevleetaru/2019/05/22/using-deep-learning-to-measure-the-facial-emotion-of-television/) conveyed by those [faces](https://www.forbes.com/sites/kalevleetaru/2019/05/22/using-deep-learning-to-measure-the-facial-emotion-of-television/) can also be understood, such as which station features the [angriest](https://www.forbes.com/sites/kalevleetaru/2019/05/22/using-deep-learning-to-measure-the-facial-emotion-of-television/) commentators.

Most deep learning approaches to content understanding focus on self-contained models in which all of the annotations applied to a video come from the model itself. Yet Cloud Vision API’s “[Web entities](https://cloud.google.com/vision/docs/detecting-web)” reverse image search offers the intriguing ability to effectively crowdsource the open Web for greater context about a particular video frame. Taking each frame of a video and searching the Web for appearances of it or a very similar depiction of the same subject makes it possible to [link](https://www.forbes.com/sites/kalevleetaru/2019/06/02/using-google-vision-apis-reverse-image-search-to-find-television-news-images-on-the-web/) the online and broadcast worlds. Most interestingly, it makes it possible to see how a given subject has been described across the Web over time, [enriching](https://www.forbes.com/sites/kalevleetaru/2019/06/03/crowdsourcing-web-imagery-through-ai-to-understand-television-news/) predefined model-produced annotations with the vastly larger and richer [context](https://www.forbes.com/sites/kalevleetaru/2019/06/01/using-google-vision-ais-reverse-image-search-to-richly-catalog-television-news/) of the human experience.

In the end, today’s off-the-shelf cloud AI offerings have reached the point where it is possible to simply make a few API calls to transform a week of television news into rich non-consumptive machine annotations that make a vast range of new explorations and analyses accessible to understand the lens through which we see the world around us in a whole new and non-consumptive light.

*I’d like to thank the Internet Archive and its Television News Archive, especially its Director Roger Macdonald. I’d like to thank Google for the use of its cloud, including its Video AI, Vision AI, Speech-to-Text and Natural Language APIs and their associated teams for their guidance.*

*Check outmy[website](https://www.kalevleetaru.com/).*

[![53f0770ab13af971740d1d0d324da1f3](../_resources/aed8b3ef855951b14d5f80e652cabccb.png)](https://www.forbes.com/sites/kalevleetaru/)

[Kalev Leetaru](https://www.forbes.com/sites/kalevleetaru/)

Based in Washington, DC, I founded my first internet startup the year after the Mosaic web browser debuted, while still in eighth grade, and have spent the last 20 year

...

- [Print]()
- [Site Feedback](https://www.forbes.com/mailto:feedback@forbes.com)
- [Tips](https://www.forbes.com/tips/)
- [Corrections](https://www.forbes.com/mailto:corrections@forbes.com?subject=Report%20Correction%3A%20Kalev%20Leetaru&body=Reporting%20Correction%20for%3A%0A%0ATitle%3A%20A%20Look%20Back%20At%20How%20Google%E2%80%99s%20AI%20Sees%20A%20Week%20Of%20Television%20News%20And%20The%20World%20Of%20AI%20Video%20Understanding%0AAuthor%3A%20Kalev%20Leetaru%0AURL%3A%20https%3A%2F%2Fwww.forbes.com%2Fsites%2Fkalevleetaru%2F2019%2F09%2F03%2Fa-look-back-at-how-googles-ai-sees-a-week-of-television-news-and-the-world-of-ai-video-understanding%2F%0A%0A--%0A%0AYour%20Name%3A%0ACorrection%20Request%3A%0A%0A--%0A%0AThank%20you%20for%20reporting%20a%20correction.%20Forbes%20staff%20will%20review%20your%20concern%20shortly.)
- [Reprints & Permissions](https://www.parsintl.com/publication/forbes/)
- [Terms](https://www.forbes.com/terms/)
- [Privacy](https://www.forbes.com/fdc/privacy.html)
- ©2019 Forbes Media LLC. All Rights Reserved.
- [AdChoices](http://preferences-mgr.truste.com/?pid=forbes01)