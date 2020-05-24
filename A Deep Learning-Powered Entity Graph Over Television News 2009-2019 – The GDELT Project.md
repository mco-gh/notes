A Deep Learning-Powered Entity Graph Over Television News 2009-2019 – The GDELT Project

# [A Deep Learning-Powered Entity Graph Over Television News 2009-2019](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/)

 ** December 9, 2019

   [![2019-global-entity-graph-geg-1064x410.png](../_resources/f2df327dfaa4273f3e1c0e69cfd59616.png)](https://blog.gdeltproject.org/a-deep-learning-powered-entity-graph-over-television-news-2009-2019/)

This past July we unveiled a massive decade-long non-consumptive [television news ngram dataset](https://blog.gdeltproject.org/announcing-the-television-news-ngram-datasets-tv-ngram/), offering one-word and two-word histograms at half hour resolution for television news coverage including CNN, MSNBC, Fox News and the evening news broadcasts of ABC, CBS and NBC back more than a decade and BBC News London for a third of a decade, using data from the Internet Archive's [Television News Archive](https://archive.org/details/tv) covering the period 2009-2019. Today we are excited to announce a powerful new non-consumptive semantic counterpart, using advanced deep learning natural language processing to identify the key concepts and entities covered on television news over the past decade.

Word histograms like ngrams are extremely powerful, surfacing subtle linguistic changes from [sentiment](https://blog.gdeltproject.org/charting-the-emotions-of-television-news-bigquery-tv-ngrams/) to [group dynamics](https://blog.gdeltproject.org/assessing-ourside-language-and-in-group-out-group-dynamics-in-television-news-using-ngrams/). At the same time, as words rather than concepts, they are limited to capturing surface-level [patterns in word usage](https://blog.gdeltproject.org/the-top-daily-terms-by-station-on-american-television-2009-2019-using-bigquery-and-tv-ngrams/) rather than understanding text at a semantic level. For example, "Donald Trump," "President Trump" and "POTUS 45" are all merely unrelated collections of independent words rather than a single common concept. A news broadcast referring to "President Trump" would therefore be seen as unrelated to a broadcast referring to "Donald Trump." Entity analysis would solve this.

What might it be like to use deep learning algorithms to "read" the closed captioning transcripts of more than a quarter-million broadcasts and compile a minute-by-minute summary of the key entities and concepts they mention, resolving spelling variants, alternative names and pronoun and noun references to common disambiguated entries? What kinds of deeper analyses, especially around disinformation and contested narratives research might be enabled by a rich deep learning-produced entity graph over television news?

To explore this further, the closed captioning of each broadcast was processed using Google's deep learning-powered [Cloud Natural Language API](https://cloud.google.com/natural-language/) to compile a list of all major concepts and entities within, using the surrounding context of each mention to disambiguate it. Thus, a mention of "Cambridge" in the UK will be distinguished from a mention of Cambridge, Massachusetts. A mention of "The Fed" will be recognized as an invocation of the US Federal Reserve, "Donald Trump" as being the same as "President Trump" and so on.

Even more powerfully, the Natural Language API performs complete pronoun and noun coreference resolution. An article that mentions "President Trump" and then repeatedly refers only to "the president" will see each of those subsequent references resolved back to "President Trump" – something not possible with traditional keyword analysis.

The result is a list of major concepts and entities (public figures, locations, organizations, events like the Arab Spring, publications like the Mueller Report and dates) found in each broadcast by minute, a unique identifier for each concept and even a link to its relevant Wikipedia page if available. In short, a non-consumptive minute-by-minute chronology of the topics and figures driving the news agenda across some of the world's most influential television news stations.

Using the unique IDs assigned to key concepts and entities, mentions on television news can be linked to mentions in [worldwide online news](https://blog.gdeltproject.org/announcing-the-global-entity-graph-geg-and-a-new-11-billion-entity-dataset/) and global [online news imagery](https://blog.gdeltproject.org/gdelt-visual-knowledge-graph-vgkg-v1-0-available/), making it possible to [connect](https://blog.gdeltproject.org/geg-vgkg-a-multimodal-master-list-of-30-million-visual-and-textual-entities/) the online and offline and textual and visual worlds. An emerging narrative can be tracked as it spreads across online and broadcast news, traverses languages and spans the visual and written word. For the first time it will be possible to track the most complete picture of the spread of contested narratives, disinformation and inorganic campaigns and compare them against authoritative, organic and uncontested narratives and bridging the textual world of online news with the visual world of television news.

Ultimately, a viral online meme that spread through online news coverage yesterday can be connected through this dataset to authoritative vetted mentions of the same event, topic and entities on television news. Similarly, complex framing questions can be answered, such as who are the major international political figures mentioned most frequently alongside discussions of Joe Biden and Ukraine compared with Rudy Giuliani and Ukraine, offering a rich understanding of narrative framing and agenda setting.

The dataset consists of one file per day, with the past three days (since shows can take up to 72 hours to finish processing) being updated every 30 minutes with a rolling 24 hour delay, similar to the [ngrams dataset](https://blog.gdeltproject.org/announcing-the-television-news-ngram-datasets-tv-ngram/) and the [Television Explorer](https://api.gdeltproject.org/api/v2/summary/summary?d=iatv) itself. Each file is in newline delimited JSON format, with each row representing one minute of a broadcast and containing an array of all of the entities identified by the API from that minute, ordered by their overall semantic salience to the broadcast as a whole.

- **date**. The date and time in UTC of a specific minute of a given broadcast, rounded to the minute.
- **iaShowId**. The unique identifier assigned by the Internet Archive to this broadcast.
- **station**. The station on which this broadcast aired.
- **showName**. The human-readable name of the show.
- **iaClipUrl**. The URL of the Internet Archive's Television News Archive page to view the clip of this minute of the broadcast.
- **entities**. A JSON array containing the list of distinct entities identified by the API for this minute of this broadcast. Multiple references to the same entity in this minute of same type are grouped together. Thus, if "White House" is mentioned 10 times in the article as type "Location" it will only appear once here, but if it is mentioned as a "Location" in some contexts and an "Organization" in others, it will appear twice, once for its Location context and once for its Organization context.
    - **name**. The entity as identified by the API. Note that this may be different from the actual literal utterance in the broadcast. A broadcast that mentions "Barack Obama" and then mentions "the president" the rest of the broadcast would list "Barack Obama" in this field for each of the subsequent mentions instead of the literal mention "the president."
    - **type**. The entity "[type](https://cloud.google.com/natural-language/docs/reference/rest/v1/Entity#type)" as determined by the API.
    - **mid**. Provides the unique Google-assigned ID for entities for which Google has assigned an identifier (typically only for well-known entities). Absent for entities without a MID. Note that the presence of a MID is typically accompanied by a wikipediaUrl entry, but not always and users should not assume that a MID guarantees a wikipediaUrl.
    - **wikipediaUrl**. Provides the URL of the Wikipedia entry for this entity if Google has mapped it to its corresponding Wikipedia page (typically only for well-known entities). Absent for entities without a Wikipedia mapping.
    - **numMentions**. The number of times this entity+type mapping was mentioned during this minute. Thus, if "Ebola" was mentioned 4 times in this minute, it will have a 4 in this field.
    - **avgSalience**. The average "salience" score for this entity across all its mentions during this minute, recording how central and "important" this specific mention was to the overall broadcast.

The complete set of daily files can be downloaded below (currently through November 30, 2019):

- http://data.gdeltproject.org/gdeltv3/iatv/geg/MASTERFILELIST.TXT  *(master list of all files)*

The dataset is also available in Google's BigQuery:

- https://bigquery.cloud.google.com/table/gdelt-bq:gdeltv2.geg_iatv

The current dataset runs July 2, 2009 through November 30, 2019. Later this month the dataset will be updated through present and automatically update hourly, with a 24 hour rolling delay.

We're tremendously excited to see the kinds of advanced cross-modality analyses you're able to do with this powerful new non-consumptive dataset!