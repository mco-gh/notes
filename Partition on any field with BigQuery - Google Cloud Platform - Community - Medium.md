Partition on any field with BigQuery - Google Cloud Platform - Community - Medium

# Partition on any field with BigQuery

[![2*ZX7q1RNRQv0wO4CklPa3CA.jpeg](../_resources/ae8cbbde0ede21905b84fc96a8d66110.jpg)](https://medium.com/@guillaume.blaquiere?source=post_page-----840f8aa1aaab----------------------)

[guillaume blaquiere](https://medium.com/@guillaume.blaquiere?source=post_page-----840f8aa1aaab----------------------)

[Dec 16](https://medium.com/google-cloud/partition-on-any-field-with-bigquery-840f8aa1aaab?source=post_page-----840f8aa1aaab----------------------) · 6 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='188'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='189' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/840f8aa1aaab/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='192'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/840f8aa1aaab/share/facebook?source=post_actions_header---------------------------)

![0*eDEy4S8zFfYnRt1X.png](../_resources/f02688a2a389b532b6127e0efdfa6f01.png)
![0*eDEy4S8zFfYnRt1X.png](../_resources/d0ae7d3b9d896d70d470bc2f2452e930.png)

Data are critical for companies. Many of them have more data than the capability to process them. And, sadly, a** lot of values sleep in databases.**

BigQuery is a Google Cloud Platform product which address this topic. **BigQuery is a petabyte scale data warehouse** and you can query terabytes of data in seconds and you can **unlock the power of your sleeping data**.

# Pricing model and partitioning concern

BigQuery comes with 2 pricing model: **on-demand** and **flat-rate**

With the **flat-rate model**, you commit a number of “[slots](https://cloud.google.com/bigquery/docs/slots)” (unit of computational capacity) and you know in advance the bill that you will pay. The first flat-rate commitment is quite high ($10k per month), **it’s recommended for big data companies.**

With the **on-demand model**, you are charged on the volume of data that you scan. This model is well **adapted for startup, medium and small companies.** Because of “*more data you scan, more you pay*”, for limiting the costs, the data have to be optimized for reducing the read data. For this, BigQuery **allows to partition the data for narrowing the volume of data **scanned.

*Note: it’s important to differentiate the volume of data scanned and the volume of data returned. A *`*limit*`* at the end of a query limit the result not the volume scanned.*

# Partition and clustering

The** partition and clustering are 2 features that allow you to narrow the volume of data** that you scan in your database.

Until now, partitioning was only possible of date: [**either on a timestamp field**](https://cloud.google.com/bigquery/docs/creating-column-partitions)** or **[**by ingestion time**](https://cloud.google.com/bigquery/docs/creating-partitioned-tables)**; both with a day granularity**. Like this, a partition like a “*sub-table”, *was created for each day. When you looked for a data, simply specify the date (or the date range) **for query only the interesting partition and scan only the relevant data**.

Clustering is a finer grain optimization inside the partition, l**ike composite indexes in relational database**. [Felipe Hoffa](https://medium.com/u/279fe54c149a?source=post_page-----840f8aa1aaab----------------------) (Google Cloud Developer Advocate) has released a great articles on this

# Integer Range Partitioning

In December 2019, Google has released a **new partition capability: **[**Integer range partitioning**](https://cloud.google.com/bigquery/docs/creating-integer-range-partitions). This feature allow you to store all the values of a same range in the same partition

You have to define the min and max values, and the range size. That’s all, the sharding is made for you! **You have user ID, zip code, geo coordinates, (…) the partitioning works for you**!

> But, what about if I don’t have numeric or date values?

* * *

*...*

# Create your customized partition

By allowing the integer partitioning,** BigQuery allows you to partition on any fields**: Float, String, Date,… For achieving this you** have to transform your partition field into an integer** value when you storing and you querying your data.

## Partition on string field

> If I don’t have numeric user ID in my database, only emails as ID, how can you partition this table?

For this, **BigQuery has a lot of built-in functions** and one of them is [Farm-Fingerprint](https://cloud.google.com/bigquery/docs/reference/standard-sql/hash_functions#farm_fingerprint) hash function. This function transform your input into a signed INT64 value. Don’t hope to have 1e+19 partitions for fine tuning your billing. According with** BigQuery limits and quotas, **[**you are limited to 4000 partitions per table**](https://cloud.google.com/bigquery/quotas#partitioned_tables)**.**

So, according with this limit, you can create the most optimized table partitioning like this

![1*2NhUbAUw_fRGUlkvATIoWg.png](../_resources/ed5e958150c5dd6fdd3162cb7b73a9e3.png)
![1*2NhUbAUw_fRGUlkvATIoWg.png](../_resources/9f3407d55de1feaec4be26a26284f550.png)

Now, you have up to 4000 partitions on this table. Fill it with the right values in the partition fields

INSERT INTO `data.string_partitioned_table`
VALUES ("string_example",
ABS(MOD(FARM_FINGERPRINT("string_example"),4000)))

For retrieving the data according with the correct partition, by using the same partition values processing

SELECT *
FROM `data.string_partitioned_table`
WHERE integer_partition_field =
ABS(MOD(FARM_FINGERPRINT("string_example"),4000))

## Need a partition per hour?

**BigQuery timestamp partitioning is today limited to the day granularity **and you can’t have a finer grain, for example, for having hour partitioning granularity.

For this, the integer partitioning can easily address this topic. **We simply have to transform the timestamp** thanks to a built-in BigQuery function `UNIX_SECONDS `that converts timestamp in Seconds, an integer!

*Note: this also works milliseconds and microseconds.*
Start by defining your first partition. Here `2020-01-01 12am`.
select UNIX_SECONDS(TIMESTAMP("2020-01-01 00:00:00"))#Result
1577836800

Then, add 4000 hours to it for getting your max upper bound *(about 166 days). *Remember, BigQuery is limited to 4000 partitions

select UNIX_SECONDS(TIMESTAMP_ADD(
TIMESTAMP("2020-01-01 00:00:00"), INTERVAL 4000 HOUR)
)#Result
1592236800

Now create your table with your lower and upper bounds in Seconds, and 1 hour of interval -> 3600 seconds

![1*F3wvdY8g2eby1v4UdDpu2g.png](../_resources/7039a9929603107864f72d2a007b6832.png)
![1*F3wvdY8g2eby1v4UdDpu2g.png](../_resources/1c23d1cfe2a8ac721bd2ac7e0de03a50.png)

Now, you have up to 4000 partitions on this table. Fill it with the right values in the partition fields

INSERT INTO `data.hourly_partitioned_table`
VALUES (TIMESTAMP("2020-03-28 08:00:00"),
UNIX_SECONDS(TIMESTAMP("2020-03-28 08:00:00")))

For retrieving the data according with the correct partition, by using the same partition values processing

SELECT *
FROM `data.hourly_partitioned_table`
WHERE integer_partition_field =
UNIX_SECONDS(TIMESTAMP("2020-03-28 08:00:00"))

In addition, the partition are sequential and **you can search for a range of hours** like this

SELECT *
FROM `data.hourly_partitioned_table`
WHERE integer_partition_field >
UNIX_SECONDS(TIMESTAMP("2020-03-28 08:00:00"))
AND integer_partition_field <=
UNIX_SECONDS(TIMESTAMP("2020-03-28 18:00:00"))

* * *

*...*

# Limitations and constraints

In addition of the **limitation of 4000 partitions **possibles in BigQuery, the s**olution implies to add an extra partitioning field and to store it in your table**. This partition field has to be set correctly for activating the partitioning. By the way, when you perform ingestion, you have 2 solutions

- Fill in the partition field either before the the load job, or into your code before the stream insert
- Load the data into BigQuery, and perform an *INSERT SELECT* of these data.

## Fill in partition field before the load

The **solution requires a pre-processing** either the files before the load jobs, or in additional step before a streaming insert in your code.

- For the string field type, `FARM_FINGERPRINT` is an open source hash function and you can reuse it easily.
- For the date field type, the transformation of timestamp in seconds is a standard transformation in all Time libraries.

If** you use a**  **custom transformation or hash**, keep in mind that the value of the partition field, made before the insert into BigQuery, must be reusable in your BigQuery queries. [*User Defined Function (UDF)*](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions)* can help for this.*

## Perform INSERT-SELECT

If **you don’t want to perform a pre-processing**, you can load the data *as-is* into BigQuery temporary table and then **perform a request INSERT-SELECT into the final destination table**.

# For string partitioning

INSERT INTO `data.string_partitioned_table`
SELECT string_field,
ABS(MOD(FARM_FINGERPRINT(string_field),4000))
FROM `data.string_partitioned_table_temp`# For hourly partitioning
INSERT INTO `data.hourly_partitioned_table`
SELECT date, UNIX_SECONDS(date)
FROM `data.hourly_partitioned_table_temp`
This solution has several constraint

- You have to query the data in the temporary table, and thereby **you have to pay for this query**.
- You are limited, today, a**t **[**1000 **](https://cloud.google.com/bigquery/quotas#standard_tables)`[**INSERTs**](https://cloud.google.com/bigquery/quotas#standard_tables)`[** per day and per table**](https://cloud.google.com/bigquery/quotas#standard_tables), same limit as load jobs per day and per table.
- You have to manage the temporary table, thereby you **have to delete them after the insert select**.

* * *

*...*

# Partition any fields

However, the new** BigQuery feature opens new use cases and push furthers the current limits**.

Now, you can **optimize the cost of your queries in the most relevant way according with your data types and structures**. The partitioning is no longer limited to days or integers!