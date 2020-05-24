How can I improve the amount of data queried with a partitioned+clustered table?

0

I have a BigQuery table - day partitioned, and clustered. However, it still uses a lot of data when I run queries over it. How is this possible?

 [google-bigquery](https://stackoverflow.com/questions/tagged/google-bigquery)  [database-partitioning](https://stackoverflow.com/questions/tagged/database-partitioning)  [clustered-index](https://stackoverflow.com/questions/tagged/clustered-index)

[share](https://stackoverflow.com/q/58175052)|[improve this question](https://stackoverflow.com/posts/58175052/edit)

asked 2 days ago

 [![QJxe1.jpg](../_resources/26d2c96c7cd2bedc73c3e673a0e0b376.jpg)](https://stackoverflow.com/users/132438/felipe-hoffa)

 [Felipe Hoffa](https://stackoverflow.com/users/132438/felipe-hoffa)
 26.1k33 gold badges6363 silver badges148148 bronze badges

 [add a comment]()

##  1 Answer

 [active](https://stackoverflow.com/questions/58175052/how-can-i-improve-the-amount-of-data-queried-with-a-partitionedclustered-table?answertab=active#tab-top)  [oldest](https://stackoverflow.com/questions/58175052/how-can-i-improve-the-amount-of-data-queried-with-a-partitionedclustered-table?answertab=oldest#tab-top)  [votes](https://stackoverflow.com/questions/58175052/how-can-i-improve-the-amount-of-data-queried-with-a-partitionedclustered-table?answertab=votes#tab-top)

1

Sometimes no partitions, or weekly/monthly/yearly partitions will work way better than having a daily partitioned table + clustering.

This because each cluster of data in BigQuery has a minimum size. If each day of data in a daily partitioned table has less than that amount of data, you won't see any benefits at all from clustering your table.

For example, let's create a table with 30+ years of weather. I will partition this table by month (to fit multiple years into one table):

	CREATE TABLE `temp.gsod_partitioned`
	PARTITION BY date_month
	CLUSTER BY name
	AS
	SELECT *, DATE_TRUNC(date, MONTH) date_month
	FROM `fh-bigquery.weather_gsod.all`

Now, let's run a query over it - using the clustering field `name`:

	SELECT name, state, ARRAY_AGG(STRUCT(date,temp) ORDER BY temp DESC LIMIT 5) top_hot, MAX(date) active_until
	FROM `temp.gsod_partitioned`
	WHERE name LIKE 'SAN FRANC%'
	AND date > '1980-01-01'
	GROUP BY 1,2
	ORDER BY active_until DESC
	# (2.3 sec elapsed, 3.1 GB processed)

Now, let's do this over an identical table - partitioned by a fake date (so no partitioning really), and clustered by the same column:

	SELECT name, state, ARRAY_AGG(STRUCT(date,temp) ORDER BY temp DESC LIMIT 5) top_hot, MAX(date) active_until
	FROM `fh-bigquery.weather_gsod.all`
	WHERE name LIKE 'SAN FRANC%'
	AND date > '1980-01-01'
	GROUP BY 1,2
	ORDER BY active_until DESC
	# (1.5 sec elapsed, 62.8 MB processed)

Only 62.8 MB of data (vs 3.1GB) were processed!

This because clustering without partitions is much more efficient on tables that don't have a lot of GB per day.

Bonus: Clustered by geo:

	SELECT name, state, ARRAY_AGG(STRUCT(date,temp) ORDER BY temp DESC LIMIT 5) top_hot, MAX(date) active_until
	FROM `fh-bigquery.weather_gsod.all_geoclustered`
	WHERE date > '1980-01-01'
	AND ST_DISTANCE(point_gis, ST_GEOGPOINT(-122.465, 37.807)) < 40000
	GROUP BY 1,2
	ORDER BY ST_DISTANCE(ANY_VALUE(point_gis), ST_GEOGPOINT(-122.465, 37.807))
	# (2.1 sec elapsed, 100.7 MB processed)

[share](https://stackoverflow.com/a/58175053)|[improve this answer](https://stackoverflow.com/posts/58175053/edit)

 [edited 17 hours ago](https://stackoverflow.com/posts/58175053/revisions)

answered 2 days ago

 [(L)](https://stackoverflow.com/users/132438/felipe-hoffa)

 [Felipe Hoffa](https://stackoverflow.com/users/132438/felipe-hoffa)
 26.1k33 gold badges6363 silver badges148148 bronze badges

 [add a comment]()

##  Your Answer

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

### Sign up or [log in](https://stackoverflow.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f58175052%2fhow-can-i-improve-the-amount-of-data-queried-with-a-partitionedclustered-table%23new-answer)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon native iconGoogle js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='995'%3e%3cpath d='M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18z' fill='%234285F4' data-evernote-id='1050' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17z' fill='%2334A853' data-evernote-id='1051' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07z' fill='%23FBBC05' data-evernote-id='1052' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3z' fill='%23EA4335' data-evernote-id='1053' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Google

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon iconFacebook js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='996'%3e%3cpath d='M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5z' fill='%234167B2' data-evernote-id='1016' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Facebook

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon native iconLogoGlyphXSm js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='997'%3e%3cpath d='M14 16v-5h2v7H2v-7h2v5h10z' fill='%23BCBBBB' data-evernote-id='1054' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M12.09.72l-1.21.9 4.5 6.07 1.22-.9L12.09.71zM5 15h8v-2H5v2zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16zm-7.7-1.47l6.85 3.19.63-1.37-6.85-3.2-.63 1.38zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46z' fill='%23F48024' data-evernote-id='1055' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Email and Password

### Post as a guest

 Name

 Email
Required, but never shown

** By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public), [privacy policy](https://stackoverflow.com/legal/privacy-policy) and [cookie policy](https://stackoverflow.com/legal/cookie-policy)  **

## Not the answer you're looking for? Browse other questions tagged [google-bigquery](https://stackoverflow.com/questions/tagged/google-bigquery)  [database-partitioning](https://stackoverflow.com/questions/tagged/database-partitioning)  [clustered-index](https://stackoverflow.com/questions/tagged/clustered-index) or [ask your own question](https://stackoverflow.com/questions/ask).