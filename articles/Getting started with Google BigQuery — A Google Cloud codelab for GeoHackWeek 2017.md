Getting started with Google BigQuery — A Google Cloud codelab for GeoHackWeek 2017

# Getting started with Google BigQuery — A Google Cloud codelab for GeoHackWeek 2017

Hello [GeoHackWeek 2017](https://geohackweek.github.io/ghw2017/) attendees. In this [codelabs](https://g.co/codelabs)-style tutorial, we’ll walk through some of the [public datasets](https://cloud.google.com/public-datasets/) available on Google Cloud Platform (GCP) and use some of the tools available for analyzing geospatial data.

### Before you begin

Hopefully you have a Google account with GCP project set up for it. If not, check out the [preliminary tutorial](https://geohackweek.github.io/preliminary/02-gcp-tutorial/).

Once you have a GCP project with billing enabled (by starting a free trial or using a coupon, for example), you can move on to the next steps.

### About these public datasets

There are several places to look for [public datasets](https://cloud.google.com/public-datasets/) hosted by Google.

- •[Earth Engine public datasets](https://earthengine.google.com/datasets/)
- •[Google Cloud Platform public datasets](https://console.cloud.google.com/launcher/browse?filter=solution-type:dataset) — new datasets are getting loaded here, but others are documented on the product documentation.
- •[Google BigQuery public datasets](https://cloud.google.com/bigquery/public-data/) — structured datasets, queryable via SQL.
- •[Cloud Storage public datasets](https://cloud.google.com/storage/docs/public-datasets/) — raster data, including Landsat data.

The dataset we’ll be exploring is the [New York City Citi Bike trips dataset](https://cloud.google.com/bigquery/public-data/nyc-citi-bike).

### Browse the NYC Citi Bike Trips dataset in Google BigQuery

View the table in BigQuery by opening it in the [BigQuery Web UI](https://cloud.google.com/bigquery/bigquery-web-ui) at https://bigquery.cloud.google.com/table/bigquery-public-data:new_york.citibike_trips?tab=schema

You’ll see a what columns are in the table, as well as some buttons to do some operations on the table.

[Don’t do a SELECT * in BigQuery](https://stackoverflow.com/a/23991604), instead use the preview button to get a sample of some rows in the table.

![](../_resources/ff50ec456ab04c339506ba16ab416a7f.png)![0*tI5G7G9ogDQ_6dZ1..png](../_resources/c27a4d4469bbfe370de3fe18728ce97e.png)

Use the preview button to get a feel for the data.

### Compose a BigQuery query

For our first query, let’s find out which stations are the most popular destinations.

Click the **Compose query** button.

![](../_resources/7840c222289d972784a01102884983e2.png)

We are going to use [standard SQL syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/), which we need to enable in the options. Click the **Show options** button and uncheck the option to use legacy SQL syntax.

![](../_resources/c5d2bf5fb6f7c2f23666304c7b706fd8.png)
Use standard SQL syntax for the queries in this tutorial.
Now, enter the query text to find the most popular Citi Bike destinations.

![](../_resources/a1a5c6c9a0c8439e963bed6f42006e46.png)

Then click the **Run query** button.

In a few seconds, you should see a table of stations, sorted by how frequently they appear in the trips table.

Why does it say “1.15 GB processed”? This means that BigQuery scanned that many bytes to calculate the results of this query. The [first 1 TB of processing is free per month](https://cloud.google.com/bigquery/pricing#free-tier).

### More complex queries

In another article, I [use this dataset to find popular destinations for groups versus single riders](https://medium.com/@TimSwast/what-are-the-most-popular-citibike-destinations-for-nyc-couples-1baf646fbba).

![](../_resources/a1a5c6c9a0c8439e963bed6f42006e46.png)

### Visualizing query results

One way to [visualize the results of BigQuery queries is to use Cloud Datalab](https://cloud.google.com/bigquery/docs/visualize-datalab).

First, open the Google Cloud Platform console: [https://console.cloud.google.com](https://console.cloud.google.com/)

Then, open [Google Cloud Shell](https://cloud.google.com/shell/) using the shell icon in the top-right corner.

![](../_resources/6e4b9fd762d641d9af1cb39ede36a478.png)
Enter the command to create a new instance of Datalab.
*> datalab create geohackweek*

![](../_resources/d7b9b6420791af1a7d22db81cfe0aad4.png)
Connect to your new instance using the Web Preview feature.

![](../_resources/1415dba942656c90877169451fb9cb5e.png)

This will open a Jupyter notebook environment with some customizations for working with Google Cloud. To access Google BigQuery from Datalab, you can use the *pandas.io.gbq* (also known as [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/)) package.

> dataframe = pandas.io.gbq.read_gbq(
> ‘SELECT 1’, project_id=’myproj’, dialect=’standard’)

[Datalab also has built-in IPython magic commands](http://googledatalab.github.io/pydatalab/datalab.magics.html) for working with BigQuery and other Google Cloud APIs.

### Shutting down your Datalab instance

To save on costs, you can stop your Datalab instance when you are not using it.
> datalab stop geohackweek
This will shutdown the instance, but won’t remove it or its storage.
To start it back up and reconnect, use the connect command.
> datalab connect geohackweek

If you are completely done with your instance and have backed up your notebooks, you can delete the instance completely with the delete command.

> datalab delete geohackweek

### Additional Resources

- •[Combining BigQuery with the Google Maps API](https://codelabs.developers.google.com/codelabs/bigquery-maps-api/#0) — A codelab that uses User Defined Functions in BigQuery to do spatial queries and then visualize the results using Google Maps.
- •[More resources for visualizing data](https://medium.com/@TimSwast/visualizing-big-data-with-google-cloud-fe323a03f85c) — My talk at Google Cloud Next 2017 and the visualization demos I did for that.