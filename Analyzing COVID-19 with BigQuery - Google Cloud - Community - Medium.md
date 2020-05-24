Analyzing COVID-19 with BigQuery - Google Cloud - Community - Medium

# Analyzing COVID-19 with BigQuery

## Using the free BigQuery public dataset for analysis and planning

[![2*AcTUjKyDttLHxHQFzOfbnw.jpeg](../_resources/356a1b72b3df6cfdc5a7f25659902493.jpg)](https://medium.com/@lakshmanok?source=post_page-----13701a3a785----------------------)

[Lak Lakshmanan](https://medium.com/@lakshmanok?source=post_page-----13701a3a785----------------------)

[Mar 30](https://medium.com/google-cloud/analyzing-covid-19-with-bigquery-13701a3a785?source=post_page-----13701a3a785----------------------) · 6 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='210'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='211' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/13701a3a785/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='219'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='220' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/13701a3a785/share/facebook?source=post_actions_header---------------------------)

Johns Hopkins maintains a dataset of COVID-19 confirmed cases and have made it free in the form of [a CSV file](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv) for academic and research use. In an effort to make the data easier to query and analyze, Google Cloud is making it [publicly available in BigQuery](https://console.cloud.google.com/marketplace/details/johnshopkins/covid19_jhu_global_cases). BigQuery has a [sandbox](https://towardsdatascience.com/bigquery-without-a-credit-card-discover-learn-and-share-199e08d4a064) through which you can try it out without having to sign up for Google Cloud (or having to provide a credit card).

As a special case, this BigQuery dataset is [free to query](https://cloud.google.com/blog/products/data-analytics/free-public-datasets-for-covid19)even outside the free tier (until Sep 2020). If you join the COVID-19 data against any other datasets, the first 1 TB of querying per month of those other datasets is free and included in the sandbox program.

# Querying and plotting the data

Go to https://console.cloud.google.com/bigquery and type in:
SELECT
date, SUM(confirmed) num_reports
FROM `bigquery-public-data.covid19_jhu_csse.summary`
WHERE country_region = 'Italy'
GROUP BY date
ORDER BY date ASC
The first few rows of the query returned:
![1*X-IH5XjTjYcUwQ0Ml_qtow.png](../_resources/d64664a66e33f23ada0d5058e49f1a03.png)
![1*X-IH5XjTjYcUwQ0Ml_qtow.png](../_resources/f06ffdff054e1050fb4429a6fa06ea5b.png)
while the last few rows were:
![1*PJtrWJyUr-VsqVW2tZ7tSQ.png](../_resources/e470db61bf5be15643ddc89587fba515.png)
![1*PJtrWJyUr-VsqVW2tZ7tSQ.png](../_resources/4e059c9f4da52def7d71491b1b158dd4.png)

showing the rapid growth of confirmed cases in Italy. Click on the “Explore with Data Studio” button and in Data Studio, do the following two steps:

1. Select the icon for “Smoothed Time Series Chart” (see red oval in the graph below)

2. Change the metric to “num_reports”
You will get a graph like this:
![0*EnkLNyIYw7kZNAIZ](../_resources/f0882cbd1787226efc0390440dcc7038.png)
![0*EnkLNyIYw7kZNAIZ](../_resources/0b65198263cf05c8c3c44160e93e54df.png)

The data is global, so we can do the same thing for Singapore, but here let’s use the geospatial capability of BigQuery:

SELECT
date, SUM(confirmed) num_reports
FROM `bigquery-public-data.covid19_jhu_csse.summary`
WHERE ST_Distance(ST_GeogPoint(longitude, latitude),
ST_GeogPoint(103.8, 1.4)) < 200*1000 -- 200km
GROUP BY date
ORDER BY date ASC
This shows a much slower growth (note the Y-axis):
![0*dwBn5rq_78f_Ik7M](../_resources/050b889d2d2a7f45672f18889d44d2c7.png)
![0*dwBn5rq_78f_Ik7M](../_resources/cf328046a7e17f6efeffb4ae1fdebc7a.png)

# Mapping the data with BigQuery GeoViz

To get county-level data (US-only), you can use the fips code in the data. *(Note: the JHU started capturing county-level info just a couple of days ago, and their schema doesn’t seem to be stable. If these queries don’t work, please check the column names and values in the BigQuery table).*

Go to BigQuery GeoViz at https://bigquerygeoviz.appspot.com/ and type in the following query to get the latest confirmed numbers from each county:

WITH cases_by_county AS (
SELECT
fips,
ARRAY_AGG(confirmed ORDER BY date DESC LIMIT 1)[OFFSET(0)] as num_cases
FROM `bigquery-public-data`.covid19_jhu_csse.summary
GROUP BY fips
)SELECT
num_cases,
ST_CENTROID(county_geom) AS map_marker
FROM
cases_by_county
JOIN
`bigquery-public-data`.geo_us_boundaries.counties
ON fips = CONCAT(state_fips_code, county_fips_code)

The map starts out looking like this (i.e, just a small red point at each reporting county’s center point):

![0*VHQw3k-EfVRcM9o8](../_resources/ad851915b1e5750fb4d0c2e72caa356b.png)
![0*VHQw3k-EfVRcM9o8](../_resources/bcef2cbcef250177cd12f3be21777faf.png)
Go into the Style section and select these:

- Change fillColor to be data-driven and change the dialog as follows (the domain is logarithmic, and the range is hue-based):

![0*fbSELL03etpbBDK2](../_resources/cb587d38e91e38991ac404029039a236.png)
![0*fbSELL03etpbBDK2](../_resources/830bdca47787c896a47b44cf84372719.png)

- In the fillOpacity dialog, change the value to be 0.4.
- Change the circleRadius to also be logarithmic and data-driven:

![0*erIhqgLFYzfqjY8K](../_resources/b0a7417fd4d4e9b42bdad98d8b26be81.png)
![0*erIhqgLFYzfqjY8K](../_resources/ef89190e23fafd3e2263e0aa8562a1fa.png)

to get a better looking plot where the radius depends on the number of confirmed cases.

![0*8eq5DWLSYNrXNzQS](../_resources/479259a302596dfdc84734aed06af493.png)
![0*8eq5DWLSYNrXNzQS](../_resources/804272fb89ca854bb3a995ec4d34627a.png)

# Extrapolating the trend

BigQuery incorporates machine learning algorithms and time-series prediction methods. These are not epidemiological models, just extrapolations of current trends. However, even extrapolations can be useful for planning purposes. So, let’s see how to extrapolate current trends.

I’ll first illustrate this for Japan (see this article for a primer on [how to do time series prediction in BigQuery](https://medium.com/@lakshmanok/how-to-do-time-series-forecasting-in-bigquery-af9eb6be8159)). First create a dataset named advdata to hold the output model. Then, type in:

CREATE OR REPLACE MODEL advdata.numreports_forecast
OPTIONS(model_type='ARIMA',
time_series_data_col='num_reports',
time_series_timestamp_col='date') AS
SELECT
date, SUM(confirmed) num_reports
FROM `bigquery-public-data.covid19_jhu_csse.summary`
WHERE country_region = 'Japan'
GROUP BY date
ORDER BY date ASC

*Note that at the time I’m writing this, the ARIMA model is in alpha. Contact your Google Cloud sales rep to get your project whitelisted.*

This creates a time series extrapolation model. We can now get a 14-day forecast from it by doing:

SELECT * FROM
ML.FORECAST(MODEL advdata.numreports_forecast,
STRUCT(14 AS horizon, 0.9 AS confidence_level))

This yields (again, please note that this is simply an extrapolation of the current trend — for true predictions, please consult a epidemiologist!):

![1*ucOlOqCsfkKK07h3Ch_XdA.png](../_resources/15c9cb8d4847572b5a3a8f2cff2c55e9.png)
![1*ucOlOqCsfkKK07h3Ch_XdA.png](../_resources/6231bbfd6d4153864e09562a707b909d.png)

We picked Japan for a reason — because we’re doing time-series predictions using the [ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average) model, we needed a stable/periodic trend. The US is exhibiting exponential growth, and is not a good candidate for ARIMA if we use the raw values.

To use the ARIMA model for places like the US, we should take the log of the number of reports and fit a trend to it. Here’s a query that will do that:

CREATE OR REPLACE MODEL advdata.numreports_forecast
OPTIONS(model_type='ARIMA',
time_series_data_col='log_num_reports',
time_series_timestamp_col='date') AS
SELECT
date, LOG(SUM(confirmed)) log_num_reports
FROM `bigquery-public-data.covid19_jhu_csse.summary`
WHERE country_region = 'US'
GROUP BY date
ORDER BY date ASC
;
SELECT
* , EXP(forecast_value) AS forecast_numreports
FROM ML.FORECAST(MODEL advdata.numreports_forecast,
STRUCT(14 AS horizon, 0.9 AS confidence_level))
This yields:
![0*dwBn5rq_78f_Ik7M](../_resources/050b889d2d2a7f45672f18889d44d2c7.png)
![0*dwBn5rq_78f_Ik7M](../_resources/cf328046a7e17f6efeffb4ae1fdebc7a.png)

Again, we wish to reiterate that this curve is simply an extrapolation of the current trend — for true predictions that take into account preventative measures, hospital capacity, community transmission, etc., you should consult an epidemiologist!

# Getting a daily forecast

To get a daily forecast, we can create a script out of the two queries. This is as simple as writing the two SQL statements one after the other, making sure to end the first one with a semicolon. Then, click on “Schedule query” to run this every day:

![0*NgNnCDVxqctsYhs_](../_resources/41f868c310f1463d9598b8cc5c15e48a.png)
![0*NgNnCDVxqctsYhs_](../_resources/44f0d698469c5df98a15e94aa43426f0.png)
Stay safe!

# Closing comments and action items

1. Please follow the guidance of public health authorities. In the US, that is the [CDC](https://www.cdc.gov/coronavirus/2019-nCoV/index.html). At the time this article was written, the primary guidance was to [flatten the curve](http://www.flattenthecurve.com/). Please do your part and stay home and away from large gatherings.

2. Having ready access to the data supports a lot of analytical needs, but realize that it is quite possible that your interpretation of the data is wrong. Please consult experts in public health before making any life-or-death decisions or recommending any decision based on your analysis.

3. The extrapolation trends are just that — extrapolations. The number of reports can be affected by more testing, and also by interventions such as “flatten the curve”. So, use the extrapolations for planning purposes (“what happens if the current trend persists, and nothing changes”) but realize that the world **will** change and the forecast **will** be wrong.

4. BigQuery is free without a credit card (within the free tier). If you add a credit card **make sure** to [set cost controls](https://stackoverflow.com/questions/52831056/how-do-i-turn-on-cost-controls-on-bigquery).

*I don’t speak for my employer. This is not official Google work. Thanks to Felipe Hoffa for many insightful comments, and Amir Hormati for the GeoViz plot settings. Any errors that remain are mine, of course.*