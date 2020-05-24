Announcing The WEB-PARTOFSPEECH Dataset: 101 Billion Words Part Of Speech Tagged And Dependency Tree Parsed Using Google’s NLP API – The GDELT Project

# [Announcing The WEB-PARTOFSPEECH Dataset: 101 Billion Words Part Of Speech Tagged And Dependency Tree Parsed Using Google's NLP API](https://blog.gdeltproject.org/announcing-the-web-partofspeech-dataset-101-billion-words-part-of-speech-tagged-and-dependency-tree-parsed-using-googles-nlp-api/)

 ** January 10, 2020

   [![2020-web-news-part-of-speech-1064x410.png](../_resources/f5a7678d8c805c8f510855b480a3a9b6.png)](https://blog.gdeltproject.org/announcing-the-web-partofspeech-dataset-101-billion-words-part-of-speech-tagged-and-dependency-tree-parsed-using-googles-nlp-api/)

Today we are immensely excited to announce a transformative new dataset for linguistic analysis: more than 101 billion tokens (words, word parts and punctuation) from a daily random sample of GDELT's total monitoring volume consisting of 100 million primarily English language online news articles from across the world from July 2016 through January 2020, with their [part of speech information](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token) (tag, aspect, case, form, gender, mood, number, person, proper, reciprocity, tense and voice) and [dependency parse label](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#dependencyedge), along with example snippets of each construction, all machine computed by Google's [Cloud Natural Language API](https://cloud.google.com/natural-language/).

This past Fall we announced a massive new [online news ngrams dataset](https://blog.gdeltproject.org/announcing-the-web-news-ngram-datasets-web-ngram/) computing [chargrams](https://blog.gdeltproject.org/announcing-the-web-ngram-character-ngram-datasets/), [unigrams](https://blog.gdeltproject.org/announcing-the-web-news-ngram-datasets-web-ngram/) and [bigrams](https://blog.gdeltproject.org/announcing-the-web-news-ngram-datasets-web-ngram/) for [152](https://blog.gdeltproject.org/announcing-the-web-ngram-character-ngram-datasets/)  [languages](https://blog.gdeltproject.org/the-languages-of-the-new-web-news-ngram-datasets-web-ngram/) across worldwide online news each day at 15 minute resolution. Ngrams offer an incredibly powerful lens through which to track the relative popularity of specific words phrases, but are limited by their inability to examine the context and usage of those terms. How often is the word "can" used as a noun describing "a can of soup" versus a verb arguing that "he can run very fast"? How often is the word "dogged" used as an adjective as in "dogged detective work" or "dogged determination" versus as a verb as in "has been dogged by" or "that dogged the start"? What are the various sentential roles a word takes as determined by its dependency tree parse? Such questions lie at the heart of linguistic analysis and are critical to everything from improving deep learning text understanding systems to cataloging the evolution of language itself.

To help answer these questions, today we are releasing this immense new dataset compiled using Google's [Cloud Natural Language API](https://cloud.google.com/natural-language/).

Every 15 minutes a small random sample of primarily English worldwide online news articles are selected from all online coverage GDELT monitored over the previous 15 minutes and annotated through the API, totaling around 70,000-100,000 articles per day. The API performs automatic language detection for each article and processes the entire document under the recognized language and thus mixed-language articles will typically be processed using the grammatical rules of the dominate language.

Once all articles from a given 15 minute interval have been processed by the API, the results are aggregated into a token-centric dataset. Each document token within the 15 minute period is concatenated into a hash key consisting of the case-sensitive token and all its computed attributes. Token case is preserved so that "Can" and "can" are treated differently in order to support linguistic assessments of capitalization rates and rules. All appearances of the token with the same set of attributes in that given 15 minutes are collapsed into a single record, with a "count" field recording how many times that given token construct appeared and an "examples" field offering up to five example snippets with their URL citations showing the word being used that way, with each snippet up to five tokens in length with the given token at center. Even if a given construct appears multiple times in a given URL, at most one example of each construct is selected from each article. Thus, an article that contains "can" in a verb sense multiple times will yield just a single example snippet of its noun usage, but if "can" appears multiple times as both a noun and a verb, one example each of the two usages will be included.

All attributes for each token for which the Cloud Natural Language API returned a value other than "UNKNOWN" are included. Note that not all attributes are applicable to all languages or forms.

Remember that these results are 100% machine assigned with no human review or correction. There will inevitably be some degree of error in these assignments, especially around rare and edge case grammatical constructs. If you come across particularly noteworthy errors, [please let us know](https://blog.gdeltproject.org/announcing-the-web-partofspeech-dataset-101-billion-words-part-of-speech-tagged-and-dependency-tree-parsed-using-googles-nlp-api/mailto:kalev.leetaru5@gmail.com)! Due to the way in which this dataset was constructed there will be some level of duplication in which examples from the same URL appear in multiple timeslots – the underlying processing workflow will shortly be revised to eliminate those.

What are the kinds of questions you can ask of the data?

Here's a trivial example of asking what parts of speech the word "dogged" appeared as on January 1, 2020:

> 

> SELECT token, posTag FROM `gdelt-bq.gdeltv2.web_pos` WHERE DATE(dateTime) = "2020-01-01" and token='dogged' group by token,posTag

> 
The result:

|     |     |
| --- | --- |
| **token** | **posTag** |
| dogged | ADJ |
| dogged | VERB |

It appears that on that day, the word "dogged" appeared as both an adjective and a verb.

What about its dependency roles that day?
> 

> SELECT token, dependencyLabel FROM `gdelt-bq.gdeltv2.web_pos` WHERE DATE(dateTime) = "2020-01-01" and token='dogged' group by token, dependencyLabel

> 

The result (with descriptions added from their definitions in the [Cloud Natural Language API documentation](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Label)):

|     |     |     |
| --- | --- | --- |
| **token** | **dependencyLabel** | **Description** |
| dogged | ACOMP | Adjectival complement |
| dogged | ADVCL | Adverbial clause modifier |
| dogged | AMOD | Adjectival modifier of an NP |
| dogged | CCOMP | Clausal complement of a verb or adjective |
| dogged | CONJ | Conjunct |
| dogged | PCOMP | The complement of a preposition is a clause |
| dogged | POBJ | Object of a preposition |
| dogged | RCMOD | Relative clause modifier |
| dogged | ROOT | Root |
| dogged | XCOMP | Open clausal complement |

Of course, the true power of this new dataset comes in actually being able to see the examples in-situ with all of their associated attributes.

Here's a sample of adjective usage:
> 

> SELECT * FROM `gdelt-bq.gdeltv2.web_pos` WHERE DATE(dateTime) = "2020-01-01" and token='dogged' and posTag='ADJ' LIMIT 1000

> 

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dateTime | count | token | lang | lemma | posTag | posAspect | posCase | posForm | posGender | posMood | posNumber | posPerson | posProper | posReciprocity | posTense | posVoice | dependencyLabel | examples.url | examples.context |
| 2020-01-01 12:45:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | http://www.thenewsherald.com/news/lincoln-park-man-has-family-ties-to-historic-mayflower-ship/article_14cdf9ce-2995-11ea-bfdb-ab1437f7e94b.html | determination and dogged detective work |
| 2020-01-01 20:30:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | CONJ | https://calgaryherald.com/entertainment/the-great-majority-of-our-new-years-resolutions-will-fail-and-yet-we-continue-to-make-them-nonetheless/wcm/4b0650b6-4990-47f7-8ab4-710bcf4cb8ee | large so dogged , so |
| 2020-01-01 20:30:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | POBJ | https://calgaryherald.com/entertainment/the-great-majority-of-our-new-years-resolutions-will-fail-and-yet-we-continue-to-make-them-nonetheless/wcm/4b0650b6-4990-47f7-8ab4-710bcf4cb8ee | large so dogged , so |
| 2020-01-01 20:30:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | ACOMP | https://calgaryherald.com/entertainment/the-great-majority-of-our-new-years-resolutions-will-fail-and-yet-we-continue-to-make-them-nonetheless/wcm/4b0650b6-4990-47f7-8ab4-710bcf4cb8ee | evidently not dogged or tenacious |
| 2020-01-01 22:45:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://indianexpress.com/article/opinion/columns/citizenship-amendment-act-nrc-mohan-bhagwat-6195387/ | underlying the dogged and insidious |
| 2020-01-01 22:30:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://news.sky.com/story/labour-leadership-sir-keir-starmer-takes-lead-in-race-to-replace-corbyn-poll-11899154 | Starmer 's dogged determination not |
| 2020-01-01 15:00:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://wusfnews.wusf.usf.edu/post/sunshine-savior-retiring-barbara-petersen-floridas-first-amendment-champion | for her dogged pursuit of |
| 2020-01-01 01:45:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://www.niemanlab.org/2019/12/a-smarter-conversation-about-how-and-why-fact-checking-matters/ | , where dogged reporters expose |
| 2020-01-01 13:30:00 UTC | 1   | dogged | en  | dogged | ADJ |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://www.sthelensstar.co.uk/news/18130841.highlights-challenges-saints-2020/ | shown some dogged determination , |

Requesting its verb usage is equally trivial:
> 

> SELECT * FROM `gdelt-bq.gdeltv2.web_pos` WHERE DATE(dateTime) = "2020-01-01" and token='dogged' and posTag='VERB' LIMIT 1000

> 

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dateTime | count | token | lang | lemma | posTag | posAspect | posCase | posForm | posGender | posMood | posNumber | posPerson | posProper | posReciprocity | posTense | posVoice | dependencyLabel | examples.url | examples.context |
| 2020-01-01 18:30:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | ROOT | https://sputniknews.com/latam/202001011077917429-panama-canal-reportedly-suffering-from-major-water-shortage-lacks-over-40-of-needed-volume/ | supply has dogged the Panama |
| 2020-01-01 23:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | CONJ | https://www.sott.net/article/426632-Is-the-shale-boom-running-on-fumes | long been dogged by a |
| 2020-01-01 13:15:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | ROOT | http://www.theprogressnews.com/news/state/editorial-roundup-pennsylvania/article_419717a7-f124-544b-a53e-93e7f8b8539d.html | are n't dogged by the |
| 2020-01-01 16:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | CONJ | https://www.the42.ie/jack-grealish-heel-var-villa-burnley-4950998-Jan2020/ | year was dogged by another |
| 2020-01-01 03:45:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://www.thisdaylive.com/index.php/2020/01/01/natures-gift-to-the-nation/ | with the dogged determination of |
| 2020-01-01 03:15:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | ROOT | https://tucson.com/news/state-and-regional/lawyers-want-state-to-cover-costs-of-monitoring-inmate-care/article_667da9a3-d5a5-5f39-89cf-6055ea73c274.html | has been dogged for several |
| 2020-01-01 14:45:00 UTC | 2   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | RCMOD | https://www.middleeastmonitor.com/20200101-embracing-palestine-how-to-combat-israels-misuse-of-antisemitism/ | which have dogged his leadership |
| 2020-01-01 12:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | ROOT | http://www.daijiworld.com/news/newsDisplay.aspx?newsID=658952 | is still dogged with massive |
| 2020-01-01 11:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | PCOMP | https://futaa.com/article/199551/arsenal-vs-manchester-united-here-s-where-to-place-your-bets | sides being dogged by inconsistency |
| 2020-01-01 04:15:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | ROOT | https://www.pensionplanpuppets.com/2019/12/31/21044975/recap-maple-leafs-win-a-wild-new-years-eve-game-minnesota | could have dogged it a |
| 2020-01-01 15:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | RCMOD | https://www.staradvertiser.com/2020/01/01/hawaii-news/ahead-in-2020-first-rail-segment-to-open-by-the-end-of-year/?HSA=3a53de7e21313deb43ec33ba0d2c5e21537960ec | has been dogged by years |
| 2020-01-01 02:15:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://www.havasunews.com/opinion/our-view-s-created-exciting-vision-for-the-s/article_bd8e3902-2c29-11ea-9fdb-47dc65f3c52b.html | thanks to dogged determination of |
| 2020-01-01 03:15:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | ROOT | http://www.xinhuanet.com/english/2020-01/01/c_138670076.htm | divide has dogged British politics |
| 2020-01-01 07:45:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | ROOT | https://www.yenisafak.com/en/world/trumps-2019-slaps-sanctions-on-iran-turkey-and-venezuela-and-supports-israel-3508633 | has been dogged by militant |
| 2020-01-01 12:45:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST | PASSIVE | ROOT | https://www.scotsman.com/arts-and-culture/edinburgh-festivals/edinburgh-council-leader-suggests-hogmanay-party-could-be-scaled-down-from-global-bucket-list-status-in-future-1-5069031 | have been dogged by controversies |
| 2020-01-01 16:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | AMOD | https://www.breitbart.com/national-security/2020/01/01/latin-america-socialists-regain-momentum-in-2019-despite-removal-of-bolivias-morales/ | him of dogged loyalty to |
| 2020-01-01 16:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     |     |     |     |     |     | PAST |     | ROOT | http://morungexpress.com/avian-world-record-india | is still dogged with massive |
| 2020-01-01 08:00:00 UTC | 1   | dogged | en  | dog | VERB |     |     |     |     | INDICATIVE |     |     |     |     | PAST |     | RCMOD | https://www.mirror.co.uk/3am/celebrity-news/cody-simpson-declares-love-miley-21193109 | rumours that dogged the start |

These are trivial examples of how the new dataset can be used!

The complete dataset is available as a set of gzipped newline-delimited JSON files and in BigQuery.

You can download all of the JSON files from:

- http://data.gdeltproject.org/gdeltv3/web/pos/MASTERFILELIST.TXT

The table is also available in Google's BigQuery:

- [gdelt-bq.gdeltv2.web_pos](https://console.cloud.google.com/bigquery?project=gdelt-bq&folder&organizationId&p=gdelt-bq&d=gdeltv2&t=web_pos&page=table)

The fields within are as follows:

- **dateTime**. The date and time (currently rounded to the nearest 15 minutes but in future may use higher precision) that GDELT processed the article through Google's [Cloud Natural Language API](https://cloud.google.com/natural-language/). Typically this is within 30 minutes of the article being published, but sometimes can take hours to days.
- **count**. Each document token is concatenated into a case-sensitive hash key consisting of all attribute fields as described earlier.
- **token**. The actual token itself as determined by the API. This is typically a word or punctuation mark.
- **lang**. The [Google-assigned language code](https://cloud.google.com/natural-language/docs/languages) for the article this word came from, representing the linguistic rules under which the word was processed. The API performs automatic language detection on each article and this code represents the language the API saw the article as and processed its contents under. Articles that contain words in multiple languages will be assigned a single language by the API, as recorded here.
- **lemma**. The token's [lemma](https://en.wikipedia.org/wiki/Lemma_%28morphology%29).
- **posTag**. The token's [part of speech](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Tag).
- **posAspect**. The token's [grammatical aspect](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Aspect).
- **posCase**. The token's [grammatical case](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Case).
- **posForm**. The token's [grammatical form](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Form).
- **posGender**. The token's [grammatical gender](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Gender).
- **posMood**. The token's [grammatical mood](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Mood).
- **posNumber**. The token's [grammatical number](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Number).
- **posPerson**. The token's [grammatical person](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Person).
- **posProper**. The token's [grammatical properness](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Proper).
- **posReciprocity**. The token's [grammatical reciprocity](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Reciprocity).
- **posTense**. The token's [grammatical tense](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Tense).
- **posVoice**. The token's grammatical [grammatical voice](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Voice).
- **dependencyLabel**. The token's [dependency parse label](https://cloud.google.com/natural-language/docs/reference/rest/v1/Token#Label).
- **examples**. An array of up to five example snippets from the given 15 minute period showing the word being used in the specified context. Each snippet is up to five tokens long, with the given token at the center flanked by the two preceding and two subsequent words. Each unique token+dateTime+attributes triplet will feature only a single example from a given URL even if the given usage appears multiple times in that article in order to maximize the number of distinct source examples.
    - **url**. The URL from which the example snippet comes.
    - **context**. A snippet of up to five tokens with the token in question at the center.

We're enormously excited to see what you can do with this immense new dataset!