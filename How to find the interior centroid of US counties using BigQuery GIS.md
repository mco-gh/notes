How to find the interior centroid of US counties using BigQuery GIS

# How to find the interior centroid of US counties using BigQuery GIS

## How to handle the problem of centroids being in the Great Lakes

[![2*AcTUjKyDttLHxHQFzOfbnw.jpeg](../_resources/356a1b72b3df6cfdc5a7f25659902493.jpg)](https://medium.com/@lakshmanok?source=post_page-----de396f0fad03----------------------)

[Lak Lakshmanan](https://medium.com/@lakshmanok?source=post_page-----de396f0fad03----------------------)

[Apr 16](https://medium.com/google-cloud/how-to-find-the-interior-centroid-of-us-counties-using-bigquery-gis-de396f0fad03?source=post_page-----de396f0fad03----------------------) · 5 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='183'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='184' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/de396f0fad03/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='192'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/de396f0fad03/share/facebook?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='25' height='25' viewBox='0 0 25 25' data-evernote-id='196' class='js-evernote-checked'%3e%3cpath d='M19 6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v14.66h.01c.01.1.05.2.12.28a.5.5 0 0 0 .7.03l5.67-4.12 5.66 4.13a.5.5 0 0 0 .71-.03.5.5 0 0 0 .12-.29H19V6zm-6.84 9.97L7 19.64V6a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v13.64l-5.16-3.67a.49.49 0 0 0-.68 0z' fill-rule='evenodd' data-evernote-id='197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fhow-to-find-the-interior-centroid-of-us-counties-using-bigquery-gis-de396f0fad03&source=post_actions_header--------------------------bookmark_header-)

*with *[*Eric Schmidt*](https://medium.com/@easchmidt)

Trying to plot county-by-county confirmed cases of COVID-19 data using a just-launched BigQuery dataset, we noticed a problem. Overall, the map seems fine:

![1*YNosTEUwlgj0mpz_AczyCw.png](../_resources/67b272678b4e8efaf89e9a84556c977f.png)
![1*YNosTEUwlgj0mpz_AczyCw.png](../_resources/87b78d98c2dceee71bb3b1b93be977e7.png)

## The problem caused by state-and-country maritime borders

In the case of maps, though, details are important. Every user of this map will zoom into to where they live. Any user who lives on the coastline of Upper Michigan will immediately notice a problem:

![1*uGO7mcdgCAuJOCOp1a-JEg.png](../_resources/33a82ccbc3744ee9e423c3f15bd53463.png)
![1*uGO7mcdgCAuJOCOp1a-JEg.png](../_resources/426401cee20b1b132eb320c246930836.png)
Note that their county’s data is in the water! Why is that?

It’s because US county boundaries go to the state or country boundary. Normally, that’s not a problem, but here, the border is the maritime boundary and is located halfway in the Great Lakes. Here’s another example, this time on the US-Canadian border:

![1*5O0B7Kvef1H6Y42a3XpIYw.png](../_resources/08325b7be94834f1f833ec742ef34127.png)
![1*5O0B7Kvef1H6Y42a3XpIYw.png](../_resources/c566f9f71b7f26f861103a052236bae8.png)

When you create maps like the confirmed cases of COVID-19, you want the marker to be where people live, not out in the water. In this article, I will show you how to create a map marker that is located in the centroid of the land part of the county.

## Idea 1: Coastlines

First idea is to do a spatial join against a dataset of coast-line boundaries and then find the intersection (common area) between the county boundaries and the coastline. This should give us the land areas only.

BigQuery has a public dataset of US geo boundaries, so we can do that:
WITH land_only AS (
SELECT
county_name,
 ** ST_Intersection**(county_geom, coastline_geom) AS county_geom
FROM `bigquery-public-data.geo_us_boundaries.counties`,
`bigquery-public-data.geo_us_boundaries.coastline`
WHERE state_fips_code = '26' -- Michigan
AND ST_Intersects(county_geom, coastline_geom)
)SELECT
county_name,
ST_Centroid(county_geom) AS map_marker,
county_geom
FROM land_only

We can visualize the result using BigQuery GeoViz and this tell us that the method didn’t work:

![1*xgS4SLt2LfsZynhAzh2n-w.png](../_resources/9ff69a0a0e83364c63483d3d41591d63.png)
![1*xgS4SLt2LfsZynhAzh2n-w.png](../_resources/cfff00c40c50f49fd42fffb43e693217.png)

Notice that the technique worked beautifully for the islands (because the islands are polygons), but not for the other counties because in general, the US coastline consists of multilines, and not polygons.

## Idea 2: Joining with zipcodes

US Zipcodes are actually a bounding box for a collection of postal routes. Since the post office will not deliver mail in the water, we can treat zipcode boundaries are comprising population areas.

Let’s look at what the zipcodes look like for each county:
SELECT
county,
TO_JSON_STRING(ARRAY_AGG(zip_code)) AS zip_codes,
FROM `bigquery-public-data`.geo_us_boundaries.zip_codes
WHERE state_fips_code = '26' -- Michigan
GROUP BY county

## 3. Cleaning up the zipcode data

We notice that some zipcodes (e.g. 49684) cover several counties:
![1*82BbyIEZcNr-we-h8KlbMg.png](../_resources/00d015ecdf57c4e4035560e1f94ed581.png)
![1*82BbyIEZcNr-we-h8KlbMg.png](../_resources/b6e80d166c46377e9b98e7197a5bc2fd.png)

So, we need to split the county field and put 49864 into every county. There is another problem. In some cases, the county name is written as Ostego, Ostego county, or ostego County. So, here’s a function that will do the necessary cleanup:

CREATE OR REPLACE FUNCTION advdata.cleanup_county_name(county_split STRING) AS
(
TRIM(REPLACE(UPPER(county_split), 'COUNTY', ''))
)

and create a table of counties to zipcodes, and make a union of all the geometries:

CREATE OR REPLACE TABLE advdata.michigan_zipcodes AS
SELECT
advdata.cleanup_county_name(county_split) AS county,
TO_JSON_STRING(ARRAY_AGG(zip_code)) AS zip_codes,
 **ST_Union**(ARRAY_AGG(zip_code_geom)) AS population_geom

FROM `bigquery-public-data`.geo_us_boundaries.zip_codes, UNNEST(SPLIT(county, ',')) AS county_split

WHERE state_fips_code = '26' -- Michigan
GROUP BY advdata.cleanup_county_name(county_split)

## 4. Creating markers

Now, we can do markers, one for each county by doing the intersection against the zipcode bounds:

CREATE OR REPLACE TABLE advdata.michigan_landareas ASWITH land_only AS (
SELECT
lsad_name, int_point_geom,
ST_Intersection(county_geom, population_geom) AS county_geom
FROM `bigquery-public-data.geo_us_boundaries.counties`
JOIN advdata.michigan_zipcodes
ON advdata.cleanup_county_name(lsad_name) = county
WHERE state_fips_code = '26' -- Michigan
)SELECT
lsad_name,
int_point_geom,
ST_Centroid(county_geom) AS map_marker,
county_geom
FROM land_only

After doing this, we now have table where, for each county, we have a map_marker point. We can use this to map any point-based county-level data.

## 5. Scale to do all states

The queries so far were for Michigan only, so that we could quickly try them out. Now, instead of hardcoding state_fips_code=’26', let’s do it for all the US states. We’ll store the results in a dataset named reference.

The county clean up function:

CREATE OR REPLACE FUNCTION reference.cleanup_county_name(county_split STRING) AS

(
TRIM(REPLACE(UPPER(county_split), 'COUNTY', ''))
)

Note the addition of state fips to the GROUP BY and removal of Michigan from where clause:

CREATE OR REPLACE TABLE reference.zipcodes AS
SELECT
state_fips_code,
reference.cleanup_county_name(county_split) AS county,
TO_JSON_STRING(ARRAY_AGG(zip_code)) AS zip_codes,
ST_Union(ARRAY_AGG(zip_code_geom)) AS population_geom

FROM `bigquery-public-data`.geo_us_boundaries.zip_codes, UNNEST(SPLIT(county, ',')) AS county_split

GROUP BY state_fips_code, reference.cleanup_county_name(county_split)
The same thing to the landareas query:

CREATE OR REPLACE TABLE reference.landareas AS# join back using state fips and county name

WITH land_only AS (
SELECT
counties.state_fips_code,
lsad_name, int_point_geom,
ST_Intersection(county_geom, population_geom) AS county_geom
FROM `bigquery-public-data.geo_us_boundaries.counties` as counties
JOIN reference.zipcodes as zips
ON reference.cleanup_county_name(lsad_name) = county
AND counties.state_fips_code = zips.state_fips_code
)SELECT
state_fips_code,
lsad_name,
int_point_geom,
ST_Centroid(county_geom) AS map_marker,
county_geom
FROM land_only
Finally, audit the table:
select area.* EXCEPT(county_geom), county.geo_id FROM
`covid19-analytics.reference.landareas` as area
FULL JOIN `bigquery-public-data.geo_us_boundaries.counties` as county
ON area.state_fips_code = county.state_fips_code
and area.lsad_name = county.lsad_name

It turns out that there are 7 counties that do not have geo information due to lack of zip code or missing information in the counties table.

Enjoy!