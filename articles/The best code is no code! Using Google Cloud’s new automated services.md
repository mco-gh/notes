The best code is no code! Using Google Cloud’s new automated services.

# The best code is no code! Using Google Cloud’s new automated services.

Here in Australia, we do a lot of work on Google Cloud Platform for one of the country’s largest ISPs, [Telstra](https://www.telstra.com.au/). Most of that work involves building data pipelines and running analytics off the back of them for their Media business unit. As you can well imagine, they generate a huge amount of data on a daily basis. We use tools like BigQuery, Cloud Dataflow and Data Studio to wrangle, manage, and understand that data.

On one such [project](https://shinesolutions.com/2014/05/07/shiners-interviewed-on-google-developer-channel-about-bigquery/) for Telstra, we saw an opportunity to delete three code repositories and finally rid ourselves of some of the headaches associated with maintaining those applications, all the while saving money on the operational costs.

We were able to replace the system comprising these repos with two new Google Cloud Platform services:

In this blog post, I’ll introduce you to those new services that Google have spun up, and how we were able to use them to replace our legacy applications. Who doesn’t like a good spring clean, huh?

# **Some background**

As a large digital publisher, Telstra manages ads for some major websites that receive a lot of traffic. We’re talking in the region of ~3-4 billion impressions per month here folks! Such sites include the official one for the biggest sport in Australia, the AFL ([http://afl.com.au](http://afl.com.au/)). They use[DoubleClick for Publishers](https://www.doubleclickbygoogle.com/) (DFP) to handle campaigns from companies that want to advertise on these sites. DFP serves the ads and records all the interactions (e.g. impressions and clicks) with those ads, creating “ad-serving logs” in the process.

Conveniently, DFP can be configured to export those massive log files to a Google Cloud Storage (GCS) bucket. Once in GCS, it’s pretty easy to load them into BigQuery for deeper analysis.

Using these DFP ad-serving logs, Telstra can use BI tools to create impactful dashboards/reports and draw insights from the data. Up until recently, they used[Tableau](https://www.tableau.com/) (among some other tools) to create them, however Tableau can’t talk to DFP directly. It can talk to BigQuery though. So, our applications had to take the data from DFP via GCS, and load it into BigQuery to achieve this. For more detail on how we did this, see a previous blog post [here](https://shinesolutions.com/2015/02/25/test-driving-google-cloud-dataflow-alpha/).

# **The original solution**

![pexels-photo-450278.jpg](../_resources/49b2ff2fac8d7aa06ab8cc124ff0ec94.jpg)

The solution we use evolved in response to requirements and new technology becoming available over time. For example, when Cloud Dataflow was integrated into our data pipelines[back in 2015](https://shinesolutions.com/2015/02/25/test-driving-google-cloud-dataflow-alpha/).

Run daily, the applications would:

1. Update the DFP[match tables](https://developers.google.com/doubleclick-publishers/docs/pqlreference#fetching-match-tables-with-pql) in BigQuery.

2. Read the DFP[log files](https://support.google.com/dfp_premium/answer/1733124?hl=en), transform them using a Dataflow pipeline and write the results to BigQuery.

3. Create aggregated tables of our transformed tables., which were then used to power the BI tools.

Here’s how each of those three steps looked:
1.

### ** Update DFP match tables in BigQuery**

Among the match tables we gathered were such things as Ad Units, Advertisers, Custom Targeting, Line Items and Orders. Nightly, our BigQuery match tables (in other words, mapping tables) were replaced with the up-to-date versions by calling the[DFP API](https://developers.google.com/doubleclick-publishers/docs/start) and creating the associated tables with the fields we needed. These match tables contain the mappings between id values to plain text values, dates and other information we needed to present the data to the end users.

1.

### ** Transform DFP log files using Dataflow then output to tables in BigQuery**

A Dataflow pipeline would run, reading any new log files from our bucket that hadn’t been processed since the previous day. During pipeline execution, the files were read in and our match tables (read in as [side inputs](https://cloud.google.com/dataflow/model/par-do#side-inputs)) were made available to the pipeline. Each log record would be enhanced with help of the side inputs adding e.g. names of Advertiser, Ad Unit, Line Item and information provided from Custom Targeting. The resulting transformed logs were written to BigQuery based on year and month.

1.

### ** Create aggregations of transformed tables as new tables**

Next, we would create aggregation tables on the transformed tables. Why? It gets the data into a suitable state for dashboard consumption. Also to save costs. Date Partitioned tables didn’t exist in BigQuery back then (it was introduced June 2016) and a monthly table of raw logs gets very large. And when you query a large table enough times, you will run up a big bill like[this.](https://shinesolutions.com/2016/08/11/automating-your-dismissal-with-bigquery/)

# **Drawbacks of this solution**

![codigo.png](../_resources/d70c24bd32cb6ea6055177d0e0a8a8d9.png)

Code! Too much darn code to maintain:

- **Maintaining code repositories:** The system was broken into 3 separate Java apps. I recall adding a new feature to the system and realising I had to make code changes to all 3 repos to have it function end-to-end.
- **Keeping up to date with new versions of APIs:** Every time DFP introduced a new version of their API (and deprecated an older one), we had to update the dependency in one of the code repos and check that it didn’t render some Java class we were using obsolete.
- [**Google Cloud outages**](https://status.cloud.google.com/)**:** Outages happened from time to time (OK, not that often) and tended to occur during interaction with BigQuery. When this would happen, the app couldn’t run to completion because it relied on reading and writing to BigQuery. If that happened we would have to kick it off again manually or just wait for the following night for it to catch up on 2 days instead.
- **Maintaining a server:** the VM was used simply for running cron jobs for a only a few hours each day, leaving it idle for the remainder of the day which was wasteful. The apps were executed from the server but e.g. the Dataflow pipelines were happening elsewhere in cloud-land once they were triggered.
- **BigQuery and Dataflow costs:** The queries and pipelines are quite pricey at this scale. If they weren’t run often it wouldn’t matter too much but they were being run daily which adds up.

# **New services from Google Cloud Platform**

![serverless-sohotrightnow](../_resources/133d591d20b13f2ee2dbb7860e667704.jpg)

Mugatu approves

We’ve seen a [trend recently](https://medium.com/slalom-engineering/serverless-the-new-cloud-trend-e2f163433431) as Cloud vendors move towards offering services that can replace existing infrastructure by removing the configuration and operations from the user, abstracting the details away so that the user can focus on the problem they are trying to solve.The benefit to the Cloud vendor is they can re-allocate those otherwise wasted compute resources elsewhere and the user ends up paying for what they use rather than what was provisioned.

So as part of that trend, Google has recently released these two new services:

## **Data Studio: DoubleClick for Publishers Connector**

[Data Studio](https://www.google.com/analytics/data-studio/) fulfils the BI criteria for creating dashboards and reports that Tableau was used for, with one important difference – [it can now talk directly to DFP](https://support.google.com/datastudio/answer/7572239).  The DFP connector is currently in private beta, so if you want to use it you will need to contact your DFP account team to get access –  however it should be widely available by the end of the year. Other connectors are also available in Data Studio e.g. for AdWords, BigQuery, Google Sheets, YouTube Analytics as well as some third party and community built connectors.

Hop into Data Studio. Once you have the DFP connector authorised you will see your networks there which you can choose from as your data source.

![blacked out data studio.png](../_resources/99bf5d9ccab6a4fbb5e9da57abd0de94.png)
Choosing your connector in Data Studio
![dfp.png](../_resources/6547de9b98063e88b54fc568cad17f92.png)
Fields from DFP connector

Using DFP as your connection, you will be provided some fields to choose from – some of which are auto aggregated like **total impressions** and **total clicks**. You will use these fields to populate your dashboard.

Below you can see an example dashboard generated using the DFP connector.

By the way – Data Studio is free! You only pay for the queries when talking to BigQuery, which we wish to bypass anyway.

![ob-report.png](../_resources/48799b61a40be5ffb9b4b7c38ff55105.png)

Data Studio dashboard sourced from DFP connector

## **BigQuery Data Transfer Service**

Telstra now uses Data Studio and the DoubleClick for Publishers Connector to make their dashboards and reports. However they still want to be able to use BigQuery for infrequent, impromptu queries and reports.

With our old solution not running anymore though, we are no longer generating any tables. To combat that, we set up a daily transfer using BigQuery’s Data Transfer Service to import the match tables and logs into a BigQuery dataset – no code needed.

**So what is it and how do you use it?**

The BigQuery Data Transfer Service automates data movement from SaaS applications to Google BigQuery on a scheduled, managed basis. It supports Adwords, DoubleClick Campaign Manager, DoubleClick for Publishers, and YouTube Content and Channel Owner Reports but I will only cover DFP here.

The service sends the DFP logs to BigQuery and keeps your match tables updated – you just nominate the destination dataset to send these tables, the name you want to call this transfer, the GCS bucket where the logs are stored and the network code. The logs are sent to partitions according to timestamp on the log file name.

![Screen Shot 2018-01-19 at 5.09.08 pm.png](../_resources/641852022857147f61bb1dfa955d7cac.png)
Some match tables and logs that end up in your BigQuery dataset
It allows a backfill of up to 60 days – DFP deletes any files over 60 days old.

The match tables that the Transfer Service supports are outlined[here](https://cloud.google.com/bigquery/docs/doubleclick-publisher-transfer) but the full list of tables is spread across a few separate links.

The Transfer Service for DFP is $100 a month per network then standard pricing applies for BigQuery storage and queries as usual.

**That is convenient but what’s the trade off? **

While we could previously query from the transformed or aggregated tables, where a lot of the processing had already taken place in our pipelines, we now have to query from the raw log tables, moving the processing into BigQuery using potentially long and complex SQL queries.

![Screen Shot 2018-01-19 at 4.40.30 pm.png](../_resources/b3fa24a9286853147311c6a116b2ab49.png)
Partitions contain records spanning across two dates

We also noticed two quirks with the transfer of logs into partitions in BigQuery.

1. Each date partition may contain records spanning across two dates like in our case.

2. The logs are loaded into partitions depending on the date in the name of the file – in our case the date was in PST (UTC -8) but the logs themselves were in AEST.

There isn’t much you can do about that – if it bothers you, technically you could reprocess them. Luckily this wasn’t an issue for us, it only makes the partitions a little bit messy as a result, e.g. we would just have to query multiple partitions to cover a full day of data.

# **Final thoughts**

These new services weren’t available to us when we started the project, so like many others[did](https://community.tableau.com/thread/153942), we rolled our own solution. Over time it evolved as we incorporated new technologies into it, gradually making things simpler, faster or more cost effective.

Now, all of the work takes place as managed services and interactions with a web browser – not a line of code in sight!

The cost savings from this recent move resulted in ~50% reduction of previous costs for our client, and that’s not even taking into consideration the hidden costs associated with code maintenance and support.

Darn good if you ask me.