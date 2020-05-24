Using The Cloud To Explore The Linguistic Patterns Of Half A Trillion Words Of News Homepage Hyperlinks

615 views|Sep 2, 2019, 01:27pm

# Using The Cloud To Explore The Linguistic Patterns Of Half A Trillion Words Of News Homepage Hyperlinks

[![53f0770ab13af971740d1d0d324da1f3](../_resources/aed8b3ef855951b14d5f80e652cabccb.png)](https://www.forbes.com/sites/kalevleetaru/)

[Kalev Leetaru](https://www.forbes.com/sites/kalevleetaru/)Contributor![](data:image/svg+xml,%3csvg class='fs-icon fs-icon--info js-evernote-checked' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60' data-evernote-id='501'%3e%3cpath fill='%23010101' d='M28.3 38.4h3.3v-10h-3.3v10zM30 13.3c-9.2 0-16.7 7.5-16.7 16.7S20.8 46.7 30 46.7 46.7 39.2 46.7 30 39.2 13.3 30 13.3zm0 30.1c-7.4 0-13.4-6-13.4-13.4s6-13.4 13.4-13.4 13.4 6 13.4 13.4-6 13.4-13.4 13.4zM28.3 25h3.3v-3.3h-3.3V25z' data-evernote-id='908' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[AI & Big Data](https://www.forbes.com/ai-big-data)
I write about the broad intersection of data and society.
-
-
-
![960x0.jpg](../_resources/b016ed98fb3dc672268635a3607ae1aa.jpg)
Getty Images
Getty

When it comes to using “big data” to analyze the patterns of society, the conversation inevitably turns to social media. Yet the world’s news media actually offers larger and richer insights into global events, narratives, beliefs and emotions if one has the right tools to explore it. What would it look like to convert a year and a half of homepage hyperlinks totaling more than half a trillion words from worldwide news front pages in 110 languages into unigram and bigram ngram datasets with just three SQL queries, an open source language detector, one script and the power of the cloud and Google’s BigQuery platform? What new insights could we learn about what the world has been paying attention to, the linguistic patterns of the world’s journalists and the power of the cloud to analyze language?

Nine years ago “[culturomics](https://science.sciencemag.org/content/331/6014/176)” became a household term when researchers took five million historical books totaling 500 billion words in seven languages and converted them into ngram word frequency histograms, allowing anyone anywhere to chart the evolution of literary language over time. This new dataset sparked a renaissance in ngram-based linguistic analysis, dramatically broadening the accessibility of large-n analyses.

While books offer a powerful glimpse into literary language evolution over the centuries, they are also quite limited. In contrast, news media represents a real-time reflection of localized events, narratives, beliefs and emotions across the world, offering an unprecedented look into the lens through which we see the world around us.

Today In:[Innovation](https://www.forbes.com/Innovation)![](data:image/svg+xml,%3csvg class='fs-icon fs-icon--chevron-up js-evernote-checked' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 19.8 19.8' data-evernote-id='502'%3e%3cpath transform='rotate(45.001 12.615 10.187)' d='M7.9 9h9.5v2.4H7.9z' data-evernote-id='940' class='js-evernote-checked'%3e%3c/path%3e%3cpath transform='rotate(134.999 7.586 10.187)' d='M2.8 9h9.5v2.4H2.8z' data-evernote-id='941' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

The open data [GDELT Project](https://blog.gdeltproject.org/announcing-gdelt-global-frontpage-graph-gfg/) has monitored the homepages of more than 50,000 news outlets worldwide every hour since March 2018 through its [Global Frontpage Graph](https://blog.gdeltproject.org/announcing-gdelt-global-frontpage-graph-gfg/) (GFG), cataloging their links in an effort to understand global journalistic editorial decision-making. In contrast to traditional print and broadcast mediums, online outlets have theoretically unlimited space, allowing them to publish a story without displacing another. Their homepages, however, remain precious fixed real estate, carefully curated by editors that must decide which stories are the most important at any moment. Analyzing these decisions can help researchers better understand which stories each news outlet believed to be the most important to its readership at any given moment in time and how those decisions changed hour by hour.

Today the GFG catalogs more than 134 billion outlinks over the past year and a half totaling more than three quarters of a trillion datapoints. Among those is the wording of each of those 134 billion links, making it possible to understand homepage links as a new kind of measurement for exploring the global evolution of language.

## PROMOTED

Grads of Life BrandVoice

 [ ###  More Than What's On Paper: Support Is Key]()

Insights - Teradata BrandVoice

 [ ###  How PayPal Turns Customer Data Into Smoother, Safer Commerce]()

UNICEF USA BrandVoice

 [ ###  How UNICEF Helps Young Migrants In Central America, Mexico And The U.S.]()

Traditionally, analyzing large textual archives has been the domain of bespoke software written for the unique nuances of a given dataset and run on large clusters. Could off-the-shelf cloud analytics tools like Google’s BigQuery be used to create the equivalent of “instant ngrams” from large text corpora with just a few SQL queries instead of writing and executing code across a large cluster?

Simplistic analytic datasets like ngrams are theoretically trivial to construct: just break each document into words and convert into a frequency histogram for unigrams and run a rolling window over the text to construct bigrams and larger ngrams. Computationally, however, the difficulty lies in efficiently managing this extremely IO-intensive process and best distributing the shingling and hash table management across a large cluster of machines, while yielding code that is robust to machine failure, network interruptions, highly unbalanced data distribution and the like.

While it isn’t typically thought of as a text analytics solution, Google’s [BigQuery](https://cloud.google.com/bigquery/) platform was actually designed for precisely this use case: loading terabytes or petabytes of data into a set of tables and analyzing them in near-real-time using a single SQL query.

In this case, those 134 billion outlinks in the GFG collectively catalog 6.6TB of text containing just over 506 billion words and 399 billion two-word phrases. Due to URL changes and different redirects over time used by the homepages of the 50,000 monitored homepages, the GFG records 1.1 million distinct homepage URLs.

Creating a unique unigram [dataset](https://blog.gdeltproject.org/announcing-the-2018-2019-global-frontpage-graph-gfg-outlet-ngram-dataset/) for each of those one million homepages took just a single SQL query in BigQuery, processing all half trillion words in just over 28 minutes to yield just over 1.1 billion unique site-word pairings. A second SQL query was all it took to generate the bigram dataset, taking just two hours to generate one million separate bigram datasets.

Most importantly, BigQuery takes care of sharding the computation across a large cluster of machines in the background, transparently load balancing the execution and delivering the final results without the user having to do anything beyond typing in their SQL query and telling it where to write the results.

From the enormous bespoke [computation](https://science.sciencemag.org/content/331/6014/176) of culturomics a decade ago to a single SQL query and half an hour of computation using BigQuery today, the study of language has become effectively a point-and-click affair.

Using this dataset it is trivial to determine that “trump” was the 14th most common word on the Washington Post’s homepage over the past year and the most common non-stopword, while being the 23rd most common word on the New York Times’ homepage, at least through the hourly snapshots captured by the GFG.

What about per-language ngram datasets? Rather than creating ngrams for each homepage over time, what would it look like to aggregate them together by language, creating a linguistic histogram for each of the 110 represented languages, allowing researchers to understand the patterns of language across outlets?

While some news outlets contain text in multiple languages, most homepages are published predominately in a single language. To determine the [language](https://blog.gdeltproject.org/new-2018-2019-global-frontpage-graph-gfg-linguistic-inventory-sheet/) of each outlet, a single SQL query took just ten minutes to organize the half trillion words across their one million source outlets, then compile a sample of 100K of text per site. This sample was then exported as a CSV file and processed using Google’s [Chrome Language Detector 2](https://github.com/CLD2Owners/cld2) (CLD2) on a traditional virtual machine to estimate the primary language of each site, then the results imported back into BigQuery as a [lookup](https://blog.gdeltproject.org/new-2018-2019-global-frontpage-graph-gfg-linguistic-inventory-sheet/).

Finally, this lookup was used in the same way as the outlet-level ngrams, constructing a separate unigram and bigram dataset for each of the [110 languages](https://blog.gdeltproject.org/announcing-the-2018-2019-global-frontpage-graph-gfg-linguistic-ngram-dataset/) represented in the GFG, taking just 8 minutes to generate 110 distinct unigram datasets and just one hour to generate the 110 bigram datasets, one for each language.

Using this dataset it is possible to look at broad linguistic trends, such as words that appear across languages, shifts in word usage and the adoption of new word forms and simply comparing the popularity of various terms.

For example, “climate change” appeared 22,609,773 times across the monitored homepages in the last year and a half, while “global warming” was mentioned just 3,773,342 times, reinforcing that the former has become the phrase du jour.

While these examples just scratch the surface, the ability to transform half a trillion words from more than a million homepages in 110 languages into unigram and bigram ngram datasets with just three lines of SQL, one script and one off-the-shelf language detector showcases the power of the modern cloud and especially analytics platforms like Google’s BigQuery to revolutionize the quantitative study of language.

In the end, the transformation of a half-trillion-word ngram analysis from a bespoke computation a decade ago into a single line of SQL and a few minutes of computation today reminds us that even large-scale analyses are moving so close to real-time that we are fast approaching the ability of almost any analysis to transition from “what if” and “I wonder” to final analysis in just minutes with a single query.

*I’d like to thank Google for the use of Google Cloud resources including *[*BigQuery*](https://cloud.google.com/bigquery/)*.*

*Check outmy[website](https://www.kalevleetaru.com/).*

[![53f0770ab13af971740d1d0d324da1f3](../_resources/aed8b3ef855951b14d5f80e652cabccb.png)](https://www.forbes.com/sites/kalevleetaru/)

[Kalev Leetaru](https://www.forbes.com/sites/kalevleetaru/)

Based in Washington, DC, I founded my first internet startup the year after the Mosaic web browser debuted, while still in eighth grade, and have spent the last 20 year

...

- [Print]()
- [Site Feedback](https://www.forbes.com/mailto:feedback@forbes.com)
- [Tips](https://www.forbes.com/tips/)
- [Corrections](https://www.forbes.com/mailto:corrections@forbes.com?subject=Report%20Correction%3A%20Kalev%20Leetaru&body=Reporting%20Correction%20for%3A%0A%0ATitle%3A%20Using%20The%20Cloud%20To%20Explore%20The%20Linguistic%20Patterns%20Of%20Half%20A%20Trillion%20Words%20Of%20News%20Homepage%20Hyperlinks%0AAuthor%3A%20Kalev%20Leetaru%0AURL%3A%20https%3A%2F%2Fwww.forbes.com%2Fsites%2Fkalevleetaru%2F2019%2F09%2F02%2Fusing-the-cloud-to-explore-the-linguistic-patterns-of-half-a-trillion-words-of-news-homepage-hyperlinks%2F%0A%0A--%0A%0AYour%20Name%3A%0ACorrection%20Request%3A%0A%0A--%0A%0AThank%20you%20for%20reporting%20a%20correction.%20Forbes%20staff%20will%20review%20your%20concern%20shortly.)
- [Reprints & Permissions](https://www.parsintl.com/publication/forbes/)
- [Terms](https://www.forbes.com/terms/)
- [Privacy](https://www.forbes.com/fdc/privacy.html)
- ©2019 Forbes Media LLC. All Rights Reserved.
- [AdChoices](http://preferences-mgr.truste.com/?pid=forbes01)