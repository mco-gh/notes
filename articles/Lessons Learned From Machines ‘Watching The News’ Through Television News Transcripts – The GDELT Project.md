Lessons Learned From Machines ‘Watching The News’ Through Television News Transcripts – The GDELT Project

# [Lessons Learned From Machines 'Watching The News' Through Television News Transcripts](https://blog.gdeltproject.org/lessons-learned-from-machines-watching-the-news-through-television-news-transcripts/)

 ** December 9, 2019

   [![2019-global-entity-graph-geg-1064x410.png](../_resources/f2df327dfaa4273f3e1c0e69cfd59616.png)](https://blog.gdeltproject.org/lessons-learned-from-machines-watching-the-news-through-television-news-transcripts/)

What would it look like to let machines "[watch](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/)" a decade of television news by reading their closed captioning transcripts? Would these text-only transcripts, lacking the visual cues of the onscreen world, still provide sufficient information for machines to generate a rough topical [chronology](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/) of the topics and things discussed by the news over the past decade? What would the end result look like and what lessons might we learn along the way?

To explore the idea of having machines "watch" a decade of television news, Google's [Cloud Natural Language API](https://cloud.google.com/natural-language/) was used to read through more than a quarter million broadcast transcripts covering CNN, MSNBC, Fox News and the evening news broadcasts of ABC, CBS and NBC over more than a decade and BBC News London for a third of a decade, using data from the Internet Archive's [Television News Archive](https://archive.org/details/tv).

In all, the machines read through the closed captioning of more than [270,000 hours of television news](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/), able to analyze an hour-long broadcast in just over a second and identifying over [410 million entities](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/), in the process creating a non-consumptive minute-by-minute chronology of the topics and things that defined television news coverage of the past decade.

What lessons did we learn along the way?

Perhaps the most important lesson of all was the potential of coreference resolution to fundamentally transform how we search, analyze and understand the unique narrative style of television news.

Unlike online news, the dialog of television news, especially when incorporating guest speakers, often takes the form of stream of consciousness narration, relying heavily on pronoun and noun references. For example, a broadcast that initially mentions "Donald Trump" may refer to "President Trump", "Trump, "the president" or just "him" in subsequent mentions. Keyword searches of closed captions won't turn up mentions of "the president" or "him" as being references to Trump, since they look only at the literal words that were spoken.

Take the example text "President Trump was back in Washington today. The president made several announcements. He also unveiled a new economic proposal, which he announced through his Twitter account." A traditional keyword search for mentions of "Trump" would return only a single match for this entire snippet since the literal word "Trump" appears only once. In contrast, the Cloud Natural Language API correctly identifies "the president", "his" and the two "he"'s as all referring back to Donald Trump, yielding five total mentions of Donald Trump.

Over the course of an entire broadcast, this coreference resolution entirely transforms our ability to identify entity mentions. Take the 7-8AM PST [broadcast](https://archive.org/details/CNNW_20180101_150000_CNN_Newsroom_With_John_Berman_and_Poppy_Harlow) of CNN Newsroom With John Berman And Poppy Harlow on January 1, 2018. Then-President Obama is referenced throughout the broadcast as "Barack Obama," "President Obama," "Obama" and simply "President." The Cloud Natural Language API examines the entire broadcast and the context of every name and reference to understand that mentions of "the president" refer to Barack Obama and correctly identifies all four as references to Obama, resolving them to a common unique identifier and providing a URL to his Wikipedia page.

Similarly, mentions of "Arlen Specter" in that same broadcast are connected to mentions of "Senator Specter" and even mentions of just the word "Senator" by itself are identified as invocations of Senator Specter.

References are even correctly localized throughout the broadcast. Thus, "Congressman" in one portion of the broadcast is understood to refer to Ron Paul, while in a subsequent part of the broadcast, references to "Congressman" are resolved to "Joe Sestak," along with "Congressman Sestak" and just plain "Sestak."

In short, coreference resolution fundamentally changes our ability to understand and navigate television news.

How does the lack of capitalization in closed captioning and ASR results affect entity recognition?

Unlike online news coverage, closed captioning transcripts typically lack any semblance of capitalization – they are traditionally either all lowercase or all uppercase. In contrast, entity extraction algorithms typically take capitalization into account as a signal to help them understand entity boundaries. Automatic capitalization models attempt to restore capitalization to human typed captioning and machine generated speech recognition and range from traditional statistical to neural models. Yet even today's best models are far from perfect and this capitalization error can affect most entity extraction systems.

In the case of the Cloud Natural Language API, its need to correctly handle all-caps headlines in traditional textual documents means it actually performs quite well on all-capitalized text, relying on grammatical and semantic cues to delineate entity boundaries. While the lack of capitalization hints means it performs slightly less accurately than on correctly capitalized text, after extensive benchmarking we concluded that uppercasing lowercase transcripts and avoiding the use of automatic capitalization models, allowing the API to rely exclusively on grammatical and semantic cues, yielded the best accuracy.

In the end, the contextualized and localized coreference resolution capabilities of today's deep learning NLP systems like Cloud Natural Language API will allow us to entirely reimagine how we search, analyze and understand television news.