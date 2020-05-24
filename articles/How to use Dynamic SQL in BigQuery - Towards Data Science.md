How to use Dynamic SQL in BigQuery - Towards Data Science

# How to use Dynamic SQL in BigQuery

## Format a string, and use EXECUTE IMMEDIATE

[![2*TveVoapl-TEk-jBTrbis8w.jpeg](../_resources/e0667f99a34a0e07e07c4d841ae06366.jpg)](https://towardsdatascience.com/@lakshmanok?source=post_page-----8c04dcc0f0de----------------------)

[Lak Lakshmanan](https://towardsdatascience.com/@lakshmanok?source=post_page-----8c04dcc0f0de----------------------)

[May 20](https://towardsdatascience.com/how-to-use-dynamic-sql-in-bigquery-8c04dcc0f0de?source=post_page-----8c04dcc0f0de----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='bo js-evernote-checked' data-evernote-id='307'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='308' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/8c04dcc0f0de/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='bo js-evernote-checked' data-evernote-id='316'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='317' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/8c04dcc0f0de/share/facebook?source=post_actions_header---------------------------)

Let’s say that we want to find the number of confirmed COVID cases over the past 3 days in various Canadian provinces. There is a BigQuery public dataset with information published by Johns Hopkins, and we can query it as follows:

SELECT
*
FROM `bigquery-public-data`.covid19_jhu_csse.confirmed_cases
WHERE country_region LIKE 'Canada'
We get:
![1*yuMeF9N1BYx3ihDWxd-KrA.png](../_resources/0d898b2067d6ff0e4a19a0311ff7fbe0.png)
![1*yuMeF9N1BYx3ihDWxd-KrA.png](../_resources/e4c4fcccf1567fdc346cb1f7add6cc90.png)
There is a column for every date

Yikes! There is a column for every date. How do we find the last three days for which there is data?

![1*oC_Quv3n-MB1USKLPU0rgQ.png](../_resources/fa18285b7e3eb1da1e53e190392b0da8.jpg)
![1*TT5hKdI7Uzvso1qJUYWlEA.jpeg](../_resources/e5c877ffe3ec2a4a48f88b70496002d4.jpg)

Dynamic SQL in BigQuery! Image by [Jim Semonik](https://pixabay.com/users/44833-44833/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=166539) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=166539)

## Information Schema to get columns

We can use INFORMATION_SCHEMA to get the list of columns and find the last three days using:

SELECT
column_name,
parse_date('_%m_%d_%y', column_name) AS date
FROM
`bigquery-public-data`.covid19_jhu_csse.INFORMATION_SCHEMA.COLUMNS
WHERE
table_name = 'confirmed_cases' AND
STARTS_WITH(column_name, '_')
ORDER BY date DESC LIMIT 3
This returns:
![1*blgS__1fPnab6PJM1oFVBw.png](:/4e8340fc2dc4ce58ebd745d2032cc0fc)
![1*blgS__1fPnab6PJM1oFVBw.png](../_resources/8834ff22a02234b854d1587ce869240d.png)
Latest days in the table

## Creating a dynamic SQL statement

You can run a dynamic SQL statement using EXECUTE IMMEDIATE. For example, suppose we have a variable with the column name _5_18_20, this is how to use it to execute a SELECT statement:

DECLARE col_0 STRING;
SET col_0 = '_5_18_20';**EXECUTE IMMEDIATE**  **format**("""
SELECT
country_region, province_state,
 ** %s** AS cases_day0
FROM `bigquery-public-data`.covid19_jhu_csse.confirmed_cases
WHERE country_region LIKE 'Canada'
ORDER BY cases_day0 DESC
""", **col_0);**

Look carefully at the query above. First of all, because I’m declaring a variable, etc., this is a BigQuery script where each statement ends with a semicolon.

I am then using BigQuery’s [string format function](https://cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#format_string) to create the statement I want to run. Because I am passing in a string, I specify %s in the format string and pass in col_0.

The result consists of two stages:
![1*TT5hKdI7Uzvso1qJUYWlEA.jpeg](../_resources/5f14e22c2e397c89d8ac60b8e4fb028c.png)
![1*oC_Quv3n-MB1USKLPU0rgQ.png](../_resources/f3bf231d625636add91db0656db5a3a7.png)
with the result of the second stage being:
![1*RkGz_db3LAgaWo_KH7oJrw.png](../_resources/5842f9d1b05cf80a1ed4e4abda7a858c.png)
![1*RkGz_db3LAgaWo_KH7oJrw.png](../_resources/c852ab3a00069d005a4237643d8db9e9.png)

## Scripting the last 3 days

We can combine the above three ideas — INFORMATION_SCHEMA, scripting, and EXECUTE IMMEDIATE to get the data for the past 3 days.

DECLARE columns ARRAY<STRUCT<column_name STRING, date DATE>>;SET columns = (
WITH all_date_columns AS (
SELECT column_name, parse_date('_%m_%d_%y', column_name) AS date
FROM `bigquery-public-data`.covid19_jhu_csse.INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'confirmed_cases' AND STARTS_WITH(column_name, '_')
)

SELECT ARRAY_AGG(STRUCT(column_name, date) ORDER BY date DESC LIMIT 3) AS columns

FROM all_date_columns
);EXECUTE IMMEDIATE format("""
SELECT
country_region, province_state,
%s AS cases_day0, '%t' AS date_day0,
%s AS cases_day1, '%t' AS date_day1,
%s AS cases_day2, '%t' AS date_day2
FROM `bigquery-public-data`.covid19_jhu_csse.confirmed_cases
WHERE country_region LIKE 'Canada'
ORDER BY cases_day0 DESC
""",
columns[OFFSET(0)].column_name, columns[OFFSET(0)].date,
columns[OFFSET(1)].column_name, columns[OFFSET(1)].date,
columns[OFFSET(2)].column_name, columns[OFFSET(2)].date
);
The steps:

- Declare columns as an array variable that will store the column name and date for the 3 most recent days
- Set columns to be the result of the query to get 3 days. Notice that I’m doing an ARRAY_AGG so that I get the complete resultset stored in one variable.
- Format the query. Note that I am using `%t` to represent a timestamp (see the String format documentation for details), and passing in six parameters.

The result is:
![1*_IlsqIV0kH7qePvcz6eF0w.png](../_resources/a8389dbc451a8abb6104bcc6c78ceb1e.png)
![1*_IlsqIV0kH7qePvcz6eF0w.png](../_resources/74db803b01a903420ba8ed4f163ce287.png)

## Execute Immediate USING

Instead of using String format, you can do named variables as follows:
EXECUTE IMMEDIATE """
SELECT country_region, province_state, _5_18_20 AS cases
FROM `bigquery-public-data`.covid19_jhu_csse.confirmed_cases
WHERE country_region LIKE [**@country**](http://twitter.com/country)
ORDER BY cases DESC LIMIT 3
"""
**USING 'Canada' AS country;**
You can also do positional variables using question marks:
EXECUTE IMMEDIATE """
SELECT country_region, province_state, _5_18_20 AS cases
FROM `bigquery-public-data`.covid19_jhu_csse.confirmed_cases
WHERE country_region **LIKE ?**
ORDER BY cases DESC **LIMIT ?**
"""
**USING 'Canada', 3;**

The USING clause is tricky in some situations. For example, the following doesn’t work:

*EXECUTE IMMEDIATE """
SELECT country_region, province_state, ? AS cases -- PROBLEM!!!
FROM `bigquery-public-data`.covid19_jhu_csse.confirmed_cases
WHERE country_region LIKE ?
ORDER BY cases DESC LIMIT ?
"""
USING '_5_18_20', 'Canada', 3; -- DOESNT WORK!!!!*
That’s because the first parameter gets interpreted as:
*'_5_18_20' AS cases*

So, you can’t pass in a column name through USING. Hence, I recommend using String FORMAT() to create the query to execute immediately because it doesn’t have these problems.

## What’s next? PIVOT(), that’s what!

The Dynamic SQL feature was released on BigQuery’s 10th birthday. Here’s a video featuring some BigQuery friends wishing it a happy birthday:

The [very first user](https://groups.google.com/g/bigquery-discuss/c/vQ96W1HZFj4) thread from 10 years ago raves about processing 60B records in a few seconds and muses about near-real-time queries (the more things change …). In that same thread is the first feature request … for pivots:

![1*voryfyUPWmT_XZmbiPSe1Q.png](../_resources/047726f6b29de9a8dceb474276357a41.png)
![1*voryfyUPWmT_XZmbiPSe1Q.png](../_resources/788d96eba5d220491077e128e919b5b0.png)

Dynamic SQL finally makes this possible and [Felipe Hoffa](https://medium.com/u/279fe54c149a?source=post_page-----8c04dcc0f0de----------------------) has promised he’ll write a function to finally be able to PIVOT() inside BigQuery - stay tuned.

Enjoy!

*Thanks to my colleague *[*Jagan R. Athreya*](https://medium.com/u/ac51b9da0e54?source=post_page-----8c04dcc0f0de----------------------)* for useful discussions on USING and the suggestion to use FORMAT and to *[*Felipe Hoffa*](https://medium.com/u/279fe54c149a?source=post_page-----8c04dcc0f0de----------------------)* for the walk down nostalgia lane.*