How to schedule a BigQuery ETL job with Dataprep – Google Cloud Platform - Community – Medium

# How to schedule a BigQuery ETL job with Dataprep

[![1*opbfQNyOl9EgY6qWxwj_Xw.jpeg](../_resources/82b40723e7711e1d7c4c1c4a681d209a.jpg)](https://medium.com/@lakshmanok?source=post_header_lockup)

[Lak Lakshmanan](https://medium.com/@lakshmanok)
Jan 21, 2018·4 min read

The BigQuery user interface lets you do all kinds of things — run an interactive query, save as Table, export to table, etc. — but there is no way (yet!) to schedule a query to run at a specific time or periodicity. Graham Polley’s been on a roll lately, coming up with [four workarounds](https://shinesolutions.com/2018/01/21/scheduling-bigquery-jobs-this-time-using-cloud-storage-cloud-functions/) that are all serverless and involve other GCP products. But he’s missed what, in my mind, is the clear winner for ETL jobs — it’s flexible, it’s powerful, it involves no coding, and it’s likely you’ll want it in your toolkit even after the BigQuery team rolls out the ability to run scheduled queries.

To be clear: once BigQuery has scheduled queries, you want to use that, so that you can keep your data in BigQuery and take advantage of its scale and power. However, if you are doing transformations (the T in ETL), then consider this approach:

1. 1 "."In the BigQuery UI, save the desired query as a View.

2. 2 "."In Cloud Dataprep, write a new recipe, with a BigQuery source. Optionally, add some transforms to your recipe. For example, you might want to add some formulas, de-deduplications, transformations, etc.

3. 3 "."Export result of transformation to a BigQuery table or CSV file on Cloud Storage

4. 4 "."Schedule the Dataprep flow to run periodically

If the UI is different when you try to replicate the steps, just hunt around a bit. The functionality is likely to be there, just in a different place.

![](../_resources/2c26db7e949b0616e3f8e4e569386136.png)![1*MHl6GKkrTznD4z6Jhg02CQ.png](../_resources/eeb7a6cf3e078e7eda2d8663c2abcd67.png)

Scheduling a Query to run periodically is easy, really.

### 1. Save BigQuery query as View

I’m going to demonstrate using a query that pulls recent weather from a public dataset of weather, so type this into the BigQuery UI and then save as View:

#standardSQL
SELECT
date,
MAX(prcp) AS prcp,
MAX(tmin) AS tmin,
MAX(tmax) AS tmax
FROM (
SELECT
wx.date AS date,
IF (wx.element = 'PRCP',
wx.value/10,
NULL) AS prcp,
IF (wx.element = 'TMIN',
wx.value/10,
NULL) AS tmin,
IF (wx.element = 'TMAX',
wx.value/10,
NULL) AS tmax
FROM
`bigquery-public-data.ghcn_d.ghcnd_2018` AS wx
WHERE
id = 'USW00094846'
AND DATE_DIFF(CURRENT_DATE(), wx.date, DAY) < 15 )
GROUP BY
date
ORDER BY
date ASC

![](../_resources/afe1ab489dcb5e4665337d85906381c9.png)![1*_0_JONH5UDEmy1Gr_amOXQ.png](../_resources/a31ccca0a5642727b0aa0b4738c48dc4.png)

Save the query as a view

### 2. In Cloud Dataprep, write a new recipe

![](../_resources/134f64ed1359fe3074204104e31d1c4a.png)![1*_Kk5E1b9Cgh3QV925oJPXA.png](../_resources/dc92cedf2db30626c41b70e79874839d.png)

Step 1: Launch Dataprep from the GCP web console

#### Create a new flow

![](../_resources/905551d0b30e4d4cf70f23e65e961f0a.png)![1*FQbKNQgWisnW5zLJj_jPiQ.png](../_resources/5cf4684eaf82c7622db359e4447808e6.png)

Recipes are part of a flow

#### Import BigQuery view as Dataprep dataset

Click on Import Datasets and follow the UI flow to get to your BigQuery dataset and import your newly created current_weather view as a Dataprep dataset.

![](../_resources/e147002a52d194d04082bc773eb42fa3.png)![1*KoU1hYVUZ4qlLfPc02JhxA.png](../_resources/29710066b8f5225c47f116436a5ada52.png)

Import the current_weather BigQuery View as a Dataprep Dataset

#### Add a new recipe and edit it

![](../_resources/06c04451690b2803b3c98f094151004d.png)![1*k-4EGQsWcHpA-kaVuxWofQ.png](../_resources/4d2bf1d018a266afc0682cff51e61800.png)

Add steps to the recipe

#### Add recipe steps to further transform the data

After you click on “Edit recipe”, Dataprep will pull out a sample of your dataset and show you the columns, their distributions, etc.

![](../_resources/82c72c260ad05c91f95f56a73c14dd05.png)![1*iD8MPrHPMHh5D7vwb-faZg.png](../_resources/1dacfb0a712876dbc2b616c455ad3eac.png)

Click on the blue plus button to add a step to the recipe. We’ll remove any rows where the data columns are empty:

![](../_resources/6a70a8bc43488b1439750bbc3cb8a9b9.png)![1*xIFtuiF39KT7uNrGNMc9jg.png](../_resources/6fabbf221d0b7299fe304163fceb3fa2.png)

Writing a delete transform to delete rows that match a criterion

Note that as you write the formula, Dataprep shows you which rows/columns will be affected.

### 3. Run the job to Export the data

Click on “Run job”. The default is to create a CSV file on Cloud Storage, but we can change this to BigQuery by clicking on the pencil (“Edit”) icon:

![](../_resources/c650320f97e3a026cf77187b9640867f.png)![1*joXAykcZmetL5PiJfUe16g.png](../_resources/da9416160d8b8675ed583936489ef36b.png)

Change the output of the job to write to your dataset in BigQuery

Click on “Run job” to run it once. Here, we ask the job to drop and replace the table each run, but as you can see, there are other options. This runs as a Dataflow job, i.e. at scale and distributed.

![](../_resources/13d0271a6048cec7cd7d9f77ab34591c.png)![1*W0DcIcE9q8vLssqCSYZGsA.png](../_resources/22c2e42c607b9f0a05337c37061c3e7b.png)

Dataprep flows run as Dataflow jobs! You don’t need to write Java/Python to use Dataflow.

### 4. Schedule the job to run periodically

Go to the “Flows” section of the Dataprep UI and click on the three buttons next to your new Flow. You’ll see an option to add a schedule:

![](../_resources/1b0028b57fee0d22ea5c94734786f0df.png)![1*UkmEPAThKkLvh239pZkl8Q.png](../_resources/ffea3b61db3ab755067b78c41f914c37.png)

Options include daily, weekly, etc. but also a crontab format for further flexibility:

![](../_resources/3fce7be632a99672797de4069b1091f1.png)![1*9xS5Yvz0BQCJQD8E6x3Bzg.png](../_resources/32d23d36b340a383f0b3ff386149726f.png)

Scheduling the job to run periodically
And that’s it!