UNPIVOT multiple columns into tidy pairs with BigQuery and a SQL UDF

![1*RV19-MCMsD7HMMWD7He0QA.png](../_resources/5b3c02c5dc5d217d58a5841886f4085f.png)
![1*RV19-MCMsD7HMMWD7He0QA.png](../_resources/bf1152f843396999216988884d8327ec.png)

# UNPIVOT multiple columns into tidy pairs with BigQuery and a SQL UDF

## This post is for anyone dealing with time series in CSVs with one new column for each day. Having tidy data is important! Especially these days, several providers of public data have chosen to have one column per new day — making it really hard to analyze time series with SQL. Find in this post, a shared persistent BigQuery UDF to transform these hundreds of columns into tidy (date, value) pairs you can put to use.

[![0*ahXIMiIgudZTyqJS.jpeg](../_resources/44b4d082641e9d4f4a850d37c2f8b155.jpg)](https://towardsdatascience.com/@hoffa?source=post_page-----d9d0e74ce675----------------------)

[Felipe Hoffa](https://towardsdatascience.com/@hoffa?source=post_page-----d9d0e74ce675----------------------)

[Apr 20](https://towardsdatascience.com/how-to-unpivot-multiple-columns-into-tidy-pairs-with-sql-and-bigquery-d9d0e74ce675?source=post_page-----d9d0e74ce675----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='207'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='208' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/d9d0e74ce675/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='216'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='217' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/d9d0e74ce675/share/facebook?source=post_actions_header---------------------------)

As an example of non-tidy data, we can see how the Novel Coronavirus (COVID-19) Case (provided by JHU CSSE), and the [Apple Mobility Trends Reports](https://www.apple.com/covid19/mobility) tables look:

![1*14pRddVwnm6wAhzDL9MXcw.png](../_resources/a68dc367da327c04e178d585c58c143b.png)
![1*14pRddVwnm6wAhzDL9MXcw.png](../_resources/7ea72779141ba77ea5a225f5c572ba2e.png)
![1*sDYJDPd9RZAKUVc5N4QCpw.png](../_resources/e4a94f5c10a494d1831ca4ffed08f712.png)
![1*sDYJDPd9RZAKUVc5N4QCpw.png](../_resources/a8de1bbf5d91c9954a97799e1533a0e9.png)

JHU CSSE tables, Apple Mobility Trends Reports tables: One column per date. We don’t want that.

We don’t want multiple columns, each for one date. We want to have (date, value) pairs. Since this problem seems so common, I wrote two BigQuery persistent UDFs to solve this:

- `fhoffa.x.unpivot()`
- `fhoffa.x.cast_kv_array_to_date_float()`

Let’s review how they work.

## Unpivot with fhoffa.x.unpivot()

Just give `unpivot()` a full row, and the regex of how the name of each of the columns to unpivot look.

With the Apple tables:
SELECT a.geo_type, region, transportation_type, unpivotted
FROM `fh-bigquery.public_dump.applemobilitytrends_20200414` a
, UNNEST(fhoffa.x.unpivot(a, '_2020')) unpivotted
![1*OhTsAh0rsx-xu_VLqsb-uQ.png](../_resources/0f845b9612121f73d90a1855ed1f9e6c.png)
![1*OhTsAh0rsx-xu_VLqsb-uQ.png](../_resources/14d9de87facdaa63376c3286d37fee61.png)
Unpivotting Apple Mobility Trends
With the JHU tables:
SELECT province_state, country_region, unpivotted
FROM `bigquery-public-data.covid19_jhu_csse.confirmed_cases` a
, UNNEST(fhoffa.x.unpivot(a, '_[0-9]')) unpivotted
![1*lYDzMdjJJndmSWsgX8mYNA.png](../_resources/95d6afa3b180c6faa118a54371c0ac09.png)
![1*lYDzMdjJJndmSWsgX8mYNA.png](../_resources/1c8c088ece10270c747a53f3406eb4c0.png)
Unpivotting JHU tables

That’s so much better, but we are not done. How do we transform these values into dates and numbers?

## Cast arrays with cast_kv_array_to_date_float()

We can re-cast our unpivotted columns with `cast_kv_array_to_date_float()`.

What’s even more “infuriating” when casting these columns to dates is that they use different formats for encoding dates. You don’t have to worry as the UDF can take the date format as an input too.

For example, with the Apple tables:
SELECT a.geo_type, region, transportation_type, unpivotted.*
FROM `fh-bigquery.public_dump.applemobilitytrends_20200414` a

, UNNEST(fhoffa.x.cast_kv_array_to_date_float(fhoffa.x.unpivot(a, '_2020'), '_%Y_%m_%d')) unpivotted

![1*qQOflH8qT4E0wekrJwtL0w.png](../_resources/8b77aa662aff912516f90e6c598fd384.png)
![1*qQOflH8qT4E0wekrJwtL0w.png](../_resources/4dced9af9f538b041c6800ec911dd542.png)
Unpivotting and casting Apple Mobility Trends
And with the JHU tables:
SELECT province_state, country_region, unpivotted.*
FROM `bigquery-public-data.covid19_jhu_csse.confirmed_cases` a

, UNNEST(fhoffa.x.cast_kv_array_to_date_float(fhoffa.x.unpivot(a, '_[0-9]'), '_%m_%d_%y')) unpivotted

![1*1fegV_3iU-ldhMI5tiAe7Q.png](../_resources/759f3e6ecffb8ea9328bd58efb080de8.png)
![1*1fegV_3iU-ldhMI5tiAe7Q.png](../_resources/9c83f63b84902582389ccdb3b959c994.png)
Unpivotting and casting the JHU tables
See? These results look way tidier than the starting tables.

## Bonus: The covid19_usafacts.confirmed_cases table

Once we have these 2 UDFs, applying them to other tables becomes really easy:
SELECT county_fips_code, county_name, state, state_fips_code, unpivotted.*
FROM `bigquery-public-data.covid19_usafacts.confirmed_cases` a

, UNNEST(fhoffa.x.cast_kv_array_to_date_float(fhoffa.x.unpivot(a, '_[0-9]'), '_%m_%d_%y')) unpivotted

![1*ogwynrq4-D_oxjm9J3_UQw.png](../_resources/174457a45447c7d9ccc9b7a172aae3dc.png)
![1*ogwynrq4-D_oxjm9J3_UQw.png](../_resources/9bf7ca970e733ce3027788f8504c654e.png)
Unpivotting the`covid19_usafacts.confirmed_cases` table

# How-to

Check my previous post about [Persistent UDFs in BigQuery](https://medium.com/@hoffa/new-in-bigquery-persistent-udfs-c9ea4100fd83):

[ ## New in BigQuery: Persistent UDFs   ### User defined functions are a powerful way to extend BigQuery, but until now it has been a drag having to copy paste…    #### medium.com](https://medium.com/@hoffa/new-in-bigquery-persistent-udfs-c9ea4100fd83)

The source code for these 2 UDFs is:
CREATE OR REPLACE FUNCTION fhoffa.x.unpivot(x ANY TYPE, col_regex STRING)
AS ((

# https://medium.com/@hoffa/how-to-unpivot-multiple-columns-into-tidy-pairs-with-sql-and-bigquery-d9d0e74ce675

SELECT
ARRAY_AGG(STRUCT(
REGEXP_EXTRACT(y, '[^"]*') AS key
, REGEXP_EXTRACT(y, r':([^"]*)\"?[,}\]]') AS value
))
FROM UNNEST((
SELECT REGEXP_EXTRACT_ALL(json,col_regex||r'[^:]+:\"?[^"]+\"?') arr
FROM (SELECT TO_JSON_STRING(x) json))) y

));CREATE OR REPLACE FUNCTION fhoffa.x.cast_kv_array_to_date_float(arr ANY TYPE, date_format STRING)

AS ((

# https://medium.com/@hoffa/how-to-unpivot-multiple-columns-into-tidy-pairs-with-sql-and-bigquery-d9d0e74ce675

SELECT ARRAY_AGG(STRUCT(SAFE.PARSE_DATE(date_format, key) AS date, CAST(value AS FLOAT64) AS value))

FROM UNNEST(arr)
));

The secret motor behind this function: Transforming a whole row into JSON with `TO_JSON_STRING()` and then doing a `REGEXP_EXTRACT_ALL` over it.

## Historical note

My [previous solution](https://stackoverflow.com/a/27832362/132438) to UNPIVOT in BigQuery has received than 5k views on Stack Overflow:

[ ## How to unpivot in BigQuery?   #### stackoverflow.com](https://stackoverflow.com/a/27832362/132438)

## Next steps

Once I write documentation for these functions, and we settle on their definitive name — I’ll submit them to our shared repository with community UDFs (`[bqutil](https://github.com/GoogleCloudPlatform/bigquery-utils/tree/master/udfs/community)`).

[ ## GoogleCloudPlatform/bigquery-utils   ### This directory contains community contributed user-defined functions to extend BigQuery for more specialized usage…    #### github.com](https://github.com/GoogleCloudPlatform/bigquery-utils/tree/master/udfs/community)

# Want more?

Check[Google’s public dataset program](https://cloud.google.com/blog/products/data-analytics/free-public-datasets-for-covid19), featuring an increasing collection of COVID-19 related datasets in BigQuery:

[ ## Free public datasets for COVID-19 | Google Cloud Blog   ### Data always plays a critical role in the ability to research, study, and combat public health emergencies, and nowhere…    #### cloud.google.com](https://cloud.google.com/blog/products/data-analytics/free-public-datasets-for-covid19)

I’m Felipe Hoffa, a Developer Advocate for Google Cloud. Follow me on [@felipehoffa](https://twitter.com/felipehoffa), find my previous posts on [medium.com/@hoffa](https://medium.com/@hoffa), and all about BigQuery on [reddit.com/r/bigquery](https://reddit.com/r/bigquery).