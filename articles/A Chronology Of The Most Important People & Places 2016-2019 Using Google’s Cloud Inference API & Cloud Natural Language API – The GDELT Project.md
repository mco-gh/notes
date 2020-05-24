A Chronology Of The Most Important People & Places 2016-2019 Using Google’s Cloud Inference API & Cloud Natural Language API – The GDELT Project

# [A Chronology Of The Most Important People & Places 2016-2019 Using Google's Cloud Inference API & Cloud Natural Language API](https://blog.gdeltproject.org/a-chronology-of-the-most-important-people-places-2016-2019-using-googles-cloud-inference-api-cloud-natural-language-api/)

 ** December 5, 2019

   [![2018-google-cloud-inference-api-1064x410.png](../_resources/864b88e6641679880134ed55b97f5dfc.png)](https://blog.gdeltproject.org/a-chronology-of-the-most-important-people-places-2016-2019-using-googles-cloud-inference-api-cloud-natural-language-api/)

Yesterday we [showed](https://blog.gdeltproject.org/using-googles-cloud-inference-api-cloud-natural-language-api-to-create-a-trending-topics-timeline/) how Google's Cloud Inference API could be used to create a "[trending topics](https://blog.gdeltproject.org/using-googles-cloud-inference-api-cloud-natural-language-api-to-create-a-trending-topics-timeline/)" service by using Google's Cloud Natural Language API to live annotate global news coverage and surface the top entities trending over the course of a particular day. What would it look like to scale this exploration up, to apply the Cloud Inference API to more than 11 billion annotations by Google's Cloud Natural Language API over 100 million news articles spanning three years to surface the top people and locations most associated with each day of global news coverage from November 2016 through the end of September 2019?

GDELT's [Global Entity Graph](https://blog.gdeltproject.org/announcing-the-global-entity-graph-geg-and-a-new-11-billion-entity-dataset/) consists of more than 11 billion entity annotations compiled by Google's Cloud Natural Language API from a small random sample of 100 million English-language global news articles 2016-2019. Perhaps the most natural question arising from such a dataset is what were the people and places that defined the news each day over the last three years? It turns out that with a single query per day the Cloud Inference API can answer this question, creating a chronology of the people and places that defined the past third of a decade.

Last month we [showed](https://blog.gdeltproject.org/using-googles-cloud-inference-api-to-explore-the-natural-language-apis-annotations-of-100-million-news-articles/) how the [Inference API](https://blog.gdeltproject.org/using-googles-cloud-inference-api-to-explore-the-natural-language-apis-annotations-of-100-million-news-articles/) has the built-in ability to select a particular day and return the most [significant entries](https://blog.gdeltproject.org/using-googles-cloud-inference-api-to-explore-the-natural-language-apis-annotations-of-100-million-news-articles/) associated with that day, meaning it can answer our question right out of the box. Yesterday we expanded upon that ability to [build a chronology](https://blog.gdeltproject.org/using-googles-cloud-inference-api-cloud-natural-language-api-to-create-a-trending-topics-timeline/) of the most important people and places at 15 minute resolution for an entire day. The exact same query can be used to build a daily chronology over years.

The query below uses the special TED value to instruct the Inference API to examine a particular day, as expressed in days since January 1, 1970 (in this case "18002" indicates that April 16, 2019 is 18,001 days after January 1, 1970), taking less than a second to execute.

> 
> time curl -s -H "Content-Type: application/json" \
> -H "Authorization: Bearer $(gcloud auth print-access-token)" \

> https://infer.googleapis.com/v1/projects/[YOURPROJECTID]/datasets/gdeltbq_geg_v1:query \

> -d'{
> "name": "gdeltbq_geg_v1",
> "queries": [{
> "query": {
> "type": "TYPE_AND",
> "children": [
> {
> "type": "TYPE_TERM",
> "term": {
> "name": "ted",
> "value": "18002"
> }
> },
> ],
> },
> "distributionConfigs": {
> "dataName": "EntityLOCATION",
> "maxResultEntries": 15,
> "bgprobExp": 0.3
> }
> }]
> }' > RESULTS
> 

As the day after the Notre Dame fire, global news was dominated by the aftermath of the destruction, with the top locations being Notre Dame, US, Seine, Paris, France, New York, Ile de la Cite and Europe.

What would it look like to repeat this query for each day from November 11, 2016 (the start of the GEG entries that contain MID values) through September 30, 2019 (the current end of the GEG, though it will soon be updated daily).

Using a simple [PERL](http://data.gdeltproject.org/blog/2019-cloudinferenceapi-trendingtopics/infer_run_day.pl)  [script](http://data.gdeltproject.org/blog/2019-cloudinferenceapi-trendingtopics/infer_query_day.json) we did exactly that, asking the Inference API to return the top 15 most significant people and places of each day over that time period.

The final results can be downloaded as two TSV files:

- [Most Significant People By Day (November 2016 – September 2019)](http://data.gdeltproject.org/blog/2019-cloudinferenceapi-trendingtopics/201611-201909.trendingpersons.tsv)
- [Most Significant Places By Day (November 2016 – September 2019)](http://data.gdeltproject.org/blog/2019-cloudinferenceapi-trendingtopics/201611-201909.trendinglocations.tsv)

For example, internationally renowned climate change activist Greta Thunberg first appears in the Most Significant People list for a single day on [March 15, 2019](https://www.theguardian.com/environment/live/2019/mar/15/climate-strikes-2019-live-latest-climate-change-global-warming), the inaugural youth climate strike that she was the symbol of. She then appears again from September 20th through the 28th, as a massive wave of [climate change protests](https://actionnetwork.org/event_campaigns/us-climate-strikes) spread across the world. The intense media coverage of these protests briefly made her the most significant person in the world according to the English news sample in the GEG on September 20th and 21st. A search for [worldwide media coverage mentioning her name](https://api.gdeltproject.org/api/v2/summary/summary?d=web&t=summary&k=%22greta+thunberg%22&ts=full&svt=zoom&stc=yes&sta=list&c=1) shows that both March 15th and September 20-28 correspond to the [two vertical surges](https://api.gdeltproject.org/api/v2/summary/summary?d=web&t=summary&k=%22greta+thunberg%22&ts=full&svt=zoom&stc=yes&sta=list&c=1) in coverage about her.

In short, given only a date and asked to find the most significant people defining that day in the news, in less than a second the Inference API examined the temporal patterns of 11 billion entity references, compared their usage on that day to the rest of the past three years and identified the ones most associated with that day.

When using the two lists above keep in mind that the GDELT [Global Entity Graph](https://blog.gdeltproject.org/announcing-the-global-entity-graph-geg-and-a-new-11-billion-entity-dataset/) is built from a very small random sample of English language news coverage each day, so its representativeness of the totality of global events and narratives is very small compared to GDELT as a whole and its focus on English coverage will necessarily skew these results towards English speaking nations. At the same time, the ability to construct what amounts to a trending topics chronology over three years by simply feeding the Natural Language API's output through the Inference API showcases just how powerful this pairing of Google Cloud APIs truly is.

Putting this all together, we started with a random selection of 100 million news articles and used the Cloud Natural Language API to identify the people, places, organizations, locations, dates, events and other major entities within. We then handed the resulting database of more than 11 billion identified entities to the Cloud Inference API and using just a single query per day, constructed a complete chronology of the most significant people and places defining each day over the last three years.

In the end, from massive archive of text to polished chronology of the most important people and places of the past third of a decade required just plugging together two tools: Cloud Natural Language API and Cloud Inference API and letting the cloud do the rest.