Displaying BigQuery results on Google Maps using Data Studio

# Displaying BigQuery results on Google Maps using Data Studio

## Data Studio has a Google Maps layer

[![2*TveVoapl-TEk-jBTrbis8w.jpeg](../_resources/626e47b377bc7f5939a518ba7353f15e.jpg)](https://medium.com/@lakshmanok?source=post_page-----bded264bfd53----------------------)

[Lak Lakshmanan](https://medium.com/@lakshmanok?source=post_page-----bded264bfd53----------------------)

[May 8](https://medium.com/google-cloud/displaying-bigquery-results-on-google-maps-using-data-studio-bded264bfd53?source=post_page-----bded264bfd53----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='209'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='210' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/bded264bfd53/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='218'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='219' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/bded264bfd53/share/facebook?source=post_actions_header---------------------------)

The [Google Mobility reports](https://www.google.com/covid19/mobility/) provide information on the extent to which visits to retail and recreation establishments has fallen due to COVID-19 related concerns and public health advice. But those reports give you the data as PDFs or a CSV.

What if you want a map that looks like this?
![1*276-JvGNgI9jwEmKKZZ4Qw.png](../_resources/41a2cf23faa1a174f776f6491669f729.png)
![1*276-JvGNgI9jwEmKKZZ4Qw.png](../_resources/bae4fc890fbba9ced5cf3569e32cbe65.png)

How visits to retail and recreation establishments vary across the USA. Green dots indicate counties where visits have fallen a lot and red dots indicate where visits are about the same.

## SQL Query

The Mobility data is in BigQuery as a public dataset, so go to https://console.cloud.google.com/BigQuery and run the following query:

WITH agg AS (
SELECT
MAX(date) AS latest_date
FROM `bigquery-public-data.covid19_google_mobility.mobility_report`
),latest_data AS (
SELECT

country_region_code, sub_region_1, sub_region_2, retail_and_recreation_percent_change_from_baseline

FROM `bigquery-public-data.covid19_google_mobility.mobility_report`, agg
WHERE date = agg.latest_date AND country_region_code = 'US'
AND retail_and_recreation_percent_change_from_baseline IS NOT NULL
),with_state_fips AS (
SELECT
state_fips_code AS sfc,
TRIM(REPLACE(sub_region_2, 'County', '')) AS trimmed_county_name,
retail_and_recreation_percent_change_from_baseline
FROM latest_data
JOIN `bigquery-public-data`.utility_us.us_states_area
ON sub_region_1 = state_name
)SELECT

CONCAT(ST_Y(ST_CENTROID(county_geom)),',',ST_X(ST_CENTROID(county_geom))) AS marker,

(100 + retail_and_recreation_percent_change_from_baseline) AS mobility
FROM with_state_fips
JOIN `bigquery-public-data`.utility_us.us_county_area
ON trimmed_county_name = county_name AND sfc = state_fips_code
The query above consists of these parts:
1. Find the latest date for which the mobility report is available
2. Pull latest data of every state/county in the US.

3. Use the state name (e.g., WA) to get the states FIPS code (e.g., 53) and massage the county name (e.g. King County) to get rid of the word County.

4. Join against a public dataset of county information to get the centroid of each county.

The resulting data looks like this:
![1*FMdQcuG7nJEatEpqtroQbA.png](../_resources/622a945560a08114e10101b7607d3b07.png)
![1*FMdQcuG7nJEatEpqtroQbA.png](../_resources/f1bc4c4a27dfd91264be7ff94971b68e.png)

## View in Data Studio

In the BigQuery web console, click the button to “Explore Data” and choose Data Studio.

Select the Google Maps layer (see figure below)
![1*sWMwcQeP5sfSn4Rd1rr-rQ.png](../_resources/6f2bd3c5989a5b16f7ffdb7cfd589fa3.png)
![1*sWMwcQeP5sfSn4Rd1rr-rQ.png](../_resources/0937afedd3b10736bb4d5615413a784a.png)

Change the Bubble location to “marker” and edit the type to be Geo > Latitude, Longitude.

Remove the Bubble size — we want all dots to be the same size.
Change the Bubble color field to be mobility.

Then, switch over to the Style tab. Increase the number of bubbles to 5000. Then, change the colors so that max=Red, medium=yellow, and min=green as shown below.

![1*AuapGQlPzatDhe4seB6P_Q.png](../_resources/6b71caa2bad4715d85bd669801140426.png)
![1*AuapGQlPzatDhe4seB6P_Q.png](../_resources/6d0509724f3a044a22c315563daf5b9a.png)

You will now have a dashboard that looks like the one at the beginning of this article. Let’s now build a dashboard that also shows the number of cases.

## Adding in confirmed cases

Use this query to join the confirmed case counts from the New York Times (it’s also public dataset in BigQuery):

CREATE TEMPORARY FUNCTION trim_county(sub_region_2 STRING)
AS (
TRIM(REPLACE(sub_region_2, 'County', ''))
);WITH agg AS (
SELECT
MAX(date) AS latest_date
FROM `bigquery-public-data.covid19_google_mobility.mobility_report`
),latest_data AS (
SELECT
country_region_code,
sub_region_1,
county AS trimmed_county_name,
retail_and_recreation_percent_change_from_baseline,
confirmed_cases
FROM `bigquery-public-data`.covid19_google_mobility.mobility_report, agg
JOIN `bigquery-public-data`.covid19_nyt.us_counties AS nyt

ON sub_region_1 = state_name AND trim_county(sub_region_2) = county AND mobility_report.date = nyt.date

WHERE nyt.date = agg.latest_date AND country_region_code = 'US'
AND retail_and_recreation_percent_change_from_baseline IS NOT NULL
),with_state_fips AS (
SELECT
state_fips_code AS sfc,
trimmed_county_name,
retail_and_recreation_percent_change_from_baseline,
confirmed_cases
FROM latest_data
JOIN `bigquery-public-data`.utility_us.us_states_area
ON sub_region_1 = state_name
)SELECT

CONCAT(ST_Y(ST_CENTROID(county_geom)),',',ST_X(ST_CENTROID(county_geom))) AS marker,

(100 + retail_and_recreation_percent_change_from_baseline) AS mobility,
LOG(confirmed_cases) AS log_cases
FROM with_state_fips
JOIN `bigquery-public-data`.utility_us.us_county_area
ON trimmed_county_name = county_name AND sfc = state_fips_code
Set up Data Studio to show bubble sizes based on log_cases:
![1*AixmZF4ZfzgNb4blBX7OCg.png](../_resources/aa27d68c1ffb69cd95eeedb2133de912.png)
![1*AixmZF4ZfzgNb4blBX7OCg.png](../_resources/cdd89698737c28a078395eb8b05cc2ae.png)
The result will look something like this:
![1*ZD2dt76c-Acsz71ChWE5-w.png](../_resources/04cd5830550212af70f9fd79a40a77ed.png)
![1*ZD2dt76c-Acsz71ChWE5-w.png](../_resources/e796a24e34c20a88f99b158638b53603.png)
Note the differences in behavior and outcomes between Colorado and Texas …

## Sharing

You can share this Data Studio dashboard just like you would share any Data Studio dashboard. Currently (thanks to [Felipe Hoffa](https://medium.com/u/279fe54c149a?source=post_page-----bded264bfd53----------------------) for the info), embedding a map is not possible.

Want to see a step-by-step tutorial? Check out this video from Felipe and [Yufeng G](https://medium.com/u/2a2ae028a675?source=post_page-----bded264bfd53----------------------):

Enjoy!