Stream Twitter Data into BigQuery with Cloud Dataprep

![](../_resources/ef9cb7db16fd6f446e02b70e53e94c50.png)![1*KbR3sE6WRNsUqJGV_-wKIg.png](../_resources/c72fa0e7aff35da3164f234f1d7cde8e.png)

# Stream Twitter Data into BigQuery with Cloud Dataprep

## Inspired by [Lakshmanan V](https://medium.com/@lakshmanok)’s [article](https://medium.com/google-cloud/how-to-schedule-a-bigquery-etl-job-with-dataprep-b1c314883ab9) to show just a couple extra features

[![0*yX2jdQm0avMc2u66.](../_resources/f69ad12ad07bdfa01464a25e05af8dc0.jpg)](https://medium.com/@jeremylorino?source=post_header_lockup)

[Jeremy Lorino](https://medium.com/@jeremylorino)
Jan 30, 2018·3 min read

> All code mentioned here can be found in my > [> git repo](https://github.com/jeremylorino/gcp-dataprep-bigquery-twitter-stream)> . Contribute, steal, or do nothing with it — your choice ;)

Let’s see how much data we can get by listening to [Twitter’s Streaming API](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview). I will break the code out into chunks to explain, but again all of this is included in the [git repo](https://github.com/jeremylorino/gcp-dataprep-bigquery-twitter-stream).

#### Listen to streaming Twitter data

Below we are utilizing a *TwitterStream* helper class that takes an Array of keywords that will filter the real-time tweet stream.

![](../_resources/1595f6db94e1f5ec171c16dcf2235d92.png)

Configure stream listener with Twitter keyword filters

Then we bind an event listener to the data event that is emitted from the *TwitterStream* instance from above. This listener will capture all tweets emitted as JSON and buffer them into a working array. Once the buffer is full, a copy of the working array is saved to the configured Google Cloud Storage bucket via *StorageProvider*; and the working array is cleared to allow for more tweets.

![](../_resources/1595f6db94e1f5ec171c16dcf2235d92.png)

And don’t forget your *config.json*. Fill in your GCP project id, the location of your default application credentials, twitter app credentials, and storage bucketName.

![](../_resources/1595f6db94e1f5ec171c16dcf2235d92.png)

#### Import Cloud Storage folder to Dataprep

Open the [Google Cloud Platform dashboard](https://console.cloud.google.com/) — choose from the top left menu; *Dataprep*.

> It is normal at the *> very*>  bottom of the list — unless you have pinned it to your favorites.

![](../_resources/134f64ed1359fe3074204104e31d1c4a.png)![1*3JLO3y2zBibEG3DnmHSDnQ.png](../_resources/dc92cedf2db30626c41b70e79874839d.png)

Quick video on importing your dataset. For real, it is quick.

![](../_resources/693e9ba9fceec0283181c953fb6634fa.png)

Import dataset

#### Wrangle newly imported dataset

Cloud Dataprep’s awesomeness is complemented by the fact that it would like you to “wrangle” your data. Particularly appealing to myself being a Texan.

There are at least 10,000 in-depth Cloud Dataprep articles, I will stick to the basics.

![](../_resources/443ee74218be21fde0d413181044800f.png)![1*cjuDzO2aUEm0-1l0iAb1xg.png](../_resources/4360fa2058e9ba15703d3988ccc8e691.png)

Now run that job yo. (top right)

![](../_resources/0822bb15ecaeb784a027359a0d76683e.png)![1*QqBd8sVf3Di6--Q184IWiA.png](../_resources/84c4b18e289f4e18bbc7748f302c1247.png)

* * *

*...*

#### Schedule Dataprep ETL to BigQuery

The best part about this little setup we are about to walk through; we are selecting a “folder” inside of a Cloud Storage bucket. Each time the flow runs it will pull all the files inside the folder and consider those files as the dataset to wrangle. So as the TwitterStream collector runs and dumps files into Cloud Storage Dataprep will continuously be able to get the latest and greatest.

![](../_resources/027794c95e5ef11a1e9d7b4cfc03adde.png)![1*jQkX8tFaX3Sk0mw1qSEX4A.png](../_resources/f2611dce22076d4649d8d2954f89a015.png)

Add a schedule to your flow

![](../_resources/ffdfb10dcf7c0742828a605a4372152b.png)![1*8T9wCNtsZXIjwMj2l8OcxQ.png](../_resources/d3de6c77c2c69a3ec9696466a99d1931.png)

Every hour; 15 minutes past the hour

![](../_resources/76b2e21591dca3b49143cfb41ba8417a.png)![1*9lL-pHRVWY3o68T6RL4qsg.png](../_resources/ddf7d26febc19ba161d34ca10ef57a25.png)

Select a BigQuery dataset

![](../_resources/c2e905f178d5da77722e117e26e2a782.png)![1*6xGI_LxmkT4N4pq75EDvjA.png](../_resources/addb4a4cf4411c622afc9c930e0a48ba.png)

Select ‘Create a new table’

![](../_resources/bce97ccbd0fa294344230c1bde4076cc.png)![1*sv_hvURYFAWTA5_wEffm6g.png](../_resources/638684e0a19f60040228eb510501acb1.png)

Select ‘Create a new table every run’

![](../_resources/21e08b2a3ca630df8b026daa83f461bf.png)![1*1kKwFK34XaxeVgj5dFC2KA.png](../_resources/0c7b4850c5bbef2d8f34f0e79b1e4ebc.png)

End result

* * *

*...*
> Next time…Visualize with Datastudio

![](../_resources/ef9cb7db16fd6f446e02b70e53e94c50.png)![1*KbR3sE6WRNsUqJGV_-wKIg.png](../_resources/5b33f3c9566375ce01494233527708e1.png)