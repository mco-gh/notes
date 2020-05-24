Interactive: The top 2019 Wikipedia pages - Towards Data Science

# Interactive: The top 2019 Wikipedia pages

## [Wikimedia](https://medium.com/u/6abe4b8ebcd8?source=post_page-----d3b96335b6ae----------------------) has [published](https://medium.com/freely-sharing-the-sum-of-all-knowledge/wiki-most-popular-articles-of-2019-15b9257a0009) their list of most popular 2019 pages— but can we go deeper? Of course, here with BigQuery and Data Studio. And [play with the interactive dashboard](https://datastudio.google.com/c/reporting/1269fe12-a291-4656-b086-e21bbdb96db9).

[![0*ahXIMiIgudZTyqJS.jpeg](../_resources/44b4d082641e9d4f4a850d37c2f8b155.jpg)](https://towardsdatascience.com/@hoffa?source=post_page-----d3b96335b6ae----------------------)

[Felipe Hoffa](https://towardsdatascience.com/@hoffa?source=post_page-----d3b96335b6ae----------------------)

[Jan 22](https://towardsdatascience.com/interactive-the-top-2019-wikipedia-pages-d3b96335b6ae?source=post_page-----d3b96335b6ae----------------------) · 7 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='209'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='210' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/d3b96335b6ae/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='213'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='214' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/d3b96335b6ae/share/facebook?source=post_actions_header---------------------------)

Finding the top 10 Wikipedia pages by # of views is interesting, and [Wikimedia](https://medium.com/u/6abe4b8ebcd8?source=post_page-----d3b96335b6ae----------------------) already did the job and [published their numbers](https://medium.com/freely-sharing-the-sum-of-all-knowledge/wiki-most-popular-articles-of-2019-15b9257a0009):

![1*Lu0vhO3QqSZUp2NoChqpDw.png](../_resources/51465332d2eb2a4d5679261a0f44295f.png)
![1*Lu0vhO3QqSZUp2NoChqpDw.png](../_resources/8eb3d7f9948ff4543c86a25259f0627a.png)

Most popular Wikipedia pages according to Wikimedia [[dashboard with links](https://datastudio.google.com/c/reporting/1269fe12-a291-4656-b086-e21bbdb96db9/page/fHyBB)]

And how did these pages trend throughout the year? Check out this [interactive dashboard](https://datastudio.google.com/c/reporting/1269fe12-a291-4656-b086-e21bbdb96db9):

[Interactive Data Studio dashboard](https://datastudio.google.com/c/reporting/1269fe12-a291-4656-b086-e21bbdb96db9)— top 2019 Wikipedia pages

## The top 2019 movies

![1*DL-jSFQsSh07t_WbUUw2Hg.png](../_resources/51392d98c6663f010cdd456d976a5716.png)
![1*DL-jSFQsSh07t_WbUUw2Hg.png](../_resources/9446184a1a48f6405beca923dad898d1.png)
Top 2019 movies

In a year dominated by movies, Avengers got the top #1 overall. What’s interesting here is to look at the peak days — for example [Once Upon a Time in Hollywood](https://en.wikipedia.org/wiki/Once_Upon_a_Time_in_Hollywood) got more views throughout the months than [The Irishman](https://en.wikipedia.org/wiki/The_Irishman), but the latter had a way higher peak when published (December 2). Once Upon a Time barely shows up within the other giants, but is steadily accumulating a large number of views.

## Top 2019 series

![1*G9I33f_p9aGTi43SLIJakQ.png](../_resources/18b55c6da1567bfc2b51dc544a6ed897.png)
![1*G9I33f_p9aGTi43SLIJakQ.png](../_resources/8d2451ba6b547f230ff04a42744aca22.png)
Top 2019 series
Series also got a lot of attention. What’s notable here:

- People came back every week to check out the latest episode of [Game of Thrones](https://en.wikipedia.org/wiki/Game_of_Thrones).
- While the series [Chernobyl](https://en.wikipedia.org/wiki/Chernobyl_(miniseries)) attracted a lot of attention, it brought a lot more attention to the page detailing [the real disaster](https://en.wikipedia.org/wiki/Chernobyl_disaster) behind.
- The 3rd season of Stranger Things generated interest, but not as much as the other series in this list.
- [The Mandalorian](https://en.wikipedia.org/wiki/The_Mandalorian) and [The Witcher](https://en.wikipedia.org/wiki/The_Witcher_(TV_series)) captured the world’s attention at the end of 2019.

## Interesting people

![1*lHCTft5kZSzz0DpnE02Vkg.png](../_resources/e058bc0613bb36f545d8fd990bef92d6.png)
![1*lHCTft5kZSzz0DpnE02Vkg.png](../_resources/bc247eab3a1e9a0ce8b692bc8feef783.png)
Comparing interesting people

- [Ted Bundy](https://en.wikipedia.org/wiki/Ted_Bundy) was the top person on Wikipedia during 2019 — powered by the release of a Netflix series and then a movie. People seem fascinated by this character, making his page the #2 overall for 2019.
- Meanwhile, Donald Trump page only raised to #15 of 2019. It’s interesting to see that this page got 5% of its yearly pageviews on December 19th, day after impeachment.
- And Boris Johnson page raised to #48 — mainly powered by 2 days: when he became prime minister, and the December elections.

# How-to

## Loading the data

I [already published](https://medium.com/google-cloud/bigquery-lazy-data-loading-ddl-dml-partitions-and-half-a-trillion-wikipedia-pageviews-cd3eacd657b6) a post on how to load the Wikipedia pageviews into BigQuery. And now we are working to bring this dataset into the official [Google Cloud Public Datasets](https://cloud.google.com/public-datasets/) project (thanks [Marc Cohen](https://medium.com/u/1f225b5f22b2?source=post_page-----d3b96335b6ae----------------------) — check the [code](https://github.com/marcacohen/wikidata)).

## Finding the top pages

To get the top pages for 2019, a simple query will do:
SELECT title, SUM(views) total_views
FROM `bigquery-public-data.wikipedia.pageviews_2019`
WHERE wiki IN ('en', 'en.m')
AND datehour>='2019-01-01'
GROUP BY title
ORDER BY 2 DESC
LIMIT 10
![1*ZCHDHfZ81-51lEhepmMoZQ.png](../_resources/94d9a7eb6c7df6e3b66486826a76124d.png)
![1*ZCHDHfZ81-51lEhepmMoZQ.png](../_resources/9c4da382f85a03d68f681451581cbf8b.png)

This works — but we can make this query way faster than 40s if we filter out noise — for example, any hour with less than 4 pageviews, and default pages:

SELECT title, SUM(views) total_views
FROM `bigquery-public-data.wikipedia.pageviews_2019`
WHERE wiki IN ('en', 'en.m')
AND title NOT IN ('Main_Page','-','Wikipedia')
AND title NOT LIKE 'File%'
AND title NOT LIKE 'Special:%'
AND title NOT LIKE 'Portal:%'
AND datehour>='2019-01-01'
AND views>3
GROUP BY title
ORDER BY 2 DESC
LIMIT 10
![1*tLkEpiaQ-gJKhjq2FuFDGw.png](../_resources/c149e9dda3a4892b71469e54436f0133.png)
![1*tLkEpiaQ-gJKhjq2FuFDGw.png](../_resources/9d3be34a8309695c8a41b18e5eeae194.png)

Cool — that brings the query from 40s to 16s. But brings out the question — why is Simple_Mail_Transfer_Protocol a top page? Wikimedia’s Andrew G. West recommends filtering out any page that has most of its pageviews coming only from mobile or desktop to filter out spam.

## Extracting daily pageviews for visualizing

And then we want not only the top pages, but also the daily pageviews to build a chart in Data Studio. So we can write a query like this:

CREATE OR REPLACE TABLE `wikipedia_extracts.2019_top_en_daily_views`
ASWITH data AS (
SELECT * FROM

# fixing `bigquery-public-data.wikipedia.pageviews_2019`

`fh-bigquery.wikipedia_v3.pageviews_2019`
WHERE wiki IN ('en', 'en.m')
AND title NOT IN ('Main_Page','-','Wikipedia')
AND title NOT LIKE 'File%'
AND title NOT LIKE 'Special:%'
AND title NOT LIKE 'Portal:%'
AND views > 3
AND datehour > '2000-01-01'
)
, pivot_desktop_mobile AS (
SELECT title, DATE(datehour) date
, SUM(IF(wiki='en', views, null)) desktop
, SUM(IF(wiki='en.m', views, null)) mobile
FROM data
GROUP BY title, date
)
, top_year AS (
SELECT *, total_mobile/(total_desktop+total_mobile) ratio_mobile
FROM (
SELECT title, SUM(desktop+mobile) total_views
, SUM(desktop) total_desktop
, SUM(mobile) total_mobile
, ARRAY_AGG(STRUCT(date, desktop+mobile AS views)) arr
, ARRAY_AGG(date ORDER BY desktop+mobile DESC LIMIT 1)[OFFSET(0)] top_day
FROM pivot_desktop_mobile
WHERE mobile/(desktop+mobile) BETWEEN 0.05 AND 0.95
GROUP BY title
ORDER BY total_views DESC
LIMIT 200
)
)SELECT title, date, views
, STRUCT(
top_day, total_views, total_desktop, total_mobile
, total_mobile/(total_mobile+total_desktop) AS ratio_mobile
) AS stats
FROM top_year, UNNEST(arr)
![1*4BavXEPb5AdPHEeO7zltSA.png](../_resources/837b4450d6ffcb65226e1f5fff3f78b5.png)
![1*4BavXEPb5AdPHEeO7zltSA.png](../_resources/4945aaa06c72bcd3f0bb2782268e47d4.png)

913GB of data processed in 32 seconds. Impressive, but careful: this query will eat your monthly free TB.

That query stores the top 200 daily pageviews in a table we can connect to Data Studio plus BI Engine for a fast interactive user experience — as seen above.

## Cost savings

Going over 913GB of data in 32 seconds is impressive! But it can quickly generate a huge bill. Instead of running these queries, you should first extract the data you are interested in to a new table — and then your queries will be magnitudes cheaper. Check out [my Stack Overflow answer](https://stackoverflow.com/a/59472489/132438) to go through the steps that transform these terabyte queries into only 2.5GB queries.

First I’ll create a table with the daily extracts:
CREATE TABLE `wikipedia_extracts.2019_en_month_views`
ASWITH data AS (
SELECT *
FROM # fixing `bigquery-public-data.wikipedia.pageviews_2019`
`fh-bigquery.wikipedia_v3.pageviews_2019`
WHERE wiki IN ('en', 'en.m')
AND title NOT IN ('Main_Page','-','Wikipedia')
AND title NOT LIKE 'File%'
AND title NOT LIKE 'Special:%'
AND title NOT LIKE 'Portal:%'
AND views > 3
AND datehour > '2000-01-01'
)
, pivot_desktop_mobile AS (
SELECT title, DATE(datehour) day
, SUM(IF(wiki='en', views, null)) desktop
, SUM(IF(wiki='en.m', views, null)) mobile
, SUM(views) views
FROM data
GROUP BY title, day
)SELECT *
FROM pivot_desktop_mobile# 1 min 23 sec elapsed, 913 GB processed

Now you can write queries over this table — for example, to get the [top monthly pages](https://stackoverflow.com/a/59472489/132438):

WITH data AS (
SELECT DATE_TRUNC(day, MONTH) month, title, SUM(views) views
FROM `fh-bigquery.wikipedia_extracts.2019_en_month_views`
WHERE mobile/(desktop+mobile) BETWEEN 0.05 AND 0.95
GROUP BY 1,2
)SELECT FORMAT_DATE('2019-%m', month)
, ARRAY_AGG(STRUCT(title, views) ORDER BY views DESC LIMIT 5 ) top
FROM data
GROUP BY month
ORDER BY month# 21.2 sec elapsed, 17.3 GB processed
And this query only processed 17GB, instead of 913GB!
![1*LZcoCHsOIzzBo9tkiE6E3Q.png](../_resources/af29cb3d07ee2a4bdf6d974d7e54e06c.png)
![1*LZcoCHsOIzzBo9tkiE6E3Q.png](../_resources/a29d27cd6c9a09313e23fe0ba0515431.png)
Top 5 Wikipedia pages for each 2019 month

> When working with large tables, remember to extract data first, and write all your fun queries over that extract instead.

## How are the views of these pages distributed?

> The top 7.2% of Wikipedia pages earn 87% of all the monthly views:
![1*L4MFNnhL3ycpkRPI408dxg.png](../_resources/412fb889d982be5ca5612b44d82d071a.png)
![1*L4MFNnhL3ycpkRPI408dxg.png](../_resources/8c6a7d61746ce2d5b286c839c69d9796.png)
The top 7.2% of Wikipedia pages earn 87% of all the monthly views.

WITH wiki_prefixes AS (SELECT ['File:', 'Talk:', 'Template_talk:', 'Wikipedia:', 'Category:', 'User_talk:', 'Page:', 'Template:', 'Category_talk:' , 'User:', 'Author:', 'Portal:', 'Wikipedia_talk:', 'Portal_talk:', 'File_talk:', 'Draft:', 'Help:', 'Draft_talk:', 'en:', 'Book_talk:', 'Module:', 'MOS:', 'Special:', 'Book:'] x)SELECT fhoffa.x.int(POW(10, fhoffa.x.int(LOG10(views)))) views_min

, fhoffa.x.int(POW(10, fhoffa.x.int(1+LOG10(views)))) views_max
, COUNT(*) pages, SUM(viewS) total_views
, STRING_AGG(title ORDER BY views DESC LIMIT 3) sample_titles
FROM `fh-bigquery.wikipedia_extracts.201912_en_totals`
WHERE title NOT IN ('-', 'Main_Page')
AND (
title NOT LIKE '%:%'

OR REGEXP_EXTRACT(title, '[^:]*:') NOT IN UNNEST((SELECT(x) FROM wiki_prefixes))

)
GROUP BY 1,2
ORDER BY 1

# 7.2 sec elapsed, 805.8 MB processed)

# Next steps

It’s your turn to play with [BigQuery — you get a free terabyte of queries](https://towardsdatascience.com/bigquery-without-a-credit-card-discover-learn-and-share-199e08d4a064) every month, no credit card needed.

[ ## BigQuery without a credit card: Discover, learn and share  ###  If you ever had trouble signing up for BigQuery, worry no more — now it’s easier than ever to sign up and start…     ####  towardsdatascience.com](https://towardsdatascience.com/bigquery-without-a-credit-card-discover-learn-and-share-199e08d4a064)

How about looking for the top 5 Wikipedia pages for each month in your own language? We only did English here!

Did you know that the top [0.1% of Wikipedia pages get 25% of the views](https://towardsdatascience.com/inequality-how-to-draw-a-lorenz-curve-with-sql-bigquery-and-data-studio-c70824b0748d)? The bottom 80% get only 4%.

[ ## Inequality: How to draw a Lorenz curve with SQL, BigQuery, and Data Studio  ###  The top 0.1% of all Wikipedia pages earn 25% of the pageviews. The bottom 99% only get 42% of all the views. And the…     ####  towardsdatascience.com](https://towardsdatascience.com/inequality-how-to-draw-a-lorenz-curve-with-sql-bigquery-and-data-studio-c70824b0748d)

# Want more?

I’m Felipe Hoffa, a Developer Advocate for Google Cloud. Follow me on [@felipehoffa](https://twitter.com/felipehoffa), find my previous posts on [medium.com/@hoffa](https://medium.com/@hoffa), and all about BigQuery on [reddit.com/r/bigquery](https://reddit.com/r/bigquery).