database partitioning - What's a good balance to decide when to partition a table in BigQuery? - Stack Overflow

When partitioning a table, you need to consider having enough data for each partition. Think of each partition like being a different file - and opening 365 files might be slower than having a huge one.

In this case, the table used for the benchmark has 1.6 GB of data for 2019 (until June in this one). That's 1.6GB/180 = 9 MB of data for each daily partition.

For such a low amount of data - arranging it in daily partitions won't bring much benefits. Consider partitioning the data by year instead. See the following question to learn how:

- [Partition by week/month//quarter/year to get over the partition limit?](https://stackoverflow.com/questions/56125048/partition-by-week-year-month-to-get-over-the-partition-limit)

Another alternative is not partitioning the table at all, and instead using clustering to sort the data by date. Then BigQuery can choose the ideal size of each block.

If you want to run your own benchmarks, do this:

	CREATE TABLE `temp.questions_partitioned`
	PARTITION BY DATE(creation_date)
	AS
	SELECT *
	FROM `fh-bigquery.stackoverflow_archive.201906_posts_questions`

vs no partitions, just clustering by date:

	CREATE TABLE `temp.questions_clustered`
	PARTITION BY fake_date
	CLUSTER BY creation_date
	AS

	SELECT *, DATE('2000-01-01') fake_date
	FROM `fh-bigquery.stackoverflow_archive.201906_posts_questions`

Then my query over the clustered table would be:

	SELECT sum(score)
	FROM `temp.questions_clustered`
	WHERE creation_date > "2019-01-01"

And it took 0.5 seconds, 17 MB processed.
Compared:

- Raw table: 1 sec, 270.7MB
- Partitioned: 2 sec, 14.3 MB
- Clustered: 0.5 sec, 17 MB

We have a winner! Clustering organized the daily data (which isn't much for this table) into more efficient blocks than strictly partitioning it by day.

It's also interesting to look at the execution details for each query on these tables:

**Slot time consumed**

- Raw table: 10.683 sec
- Partitioned: 7.308 sec
- Clustered: 0.718 sec

As you can see, the query over raw table used a lot of slots (parallelism) to get the results in 1 second. In this case 50 workers processed the whole table with multiple years of data, reading 17.7M rows. The query over the partitioned table had to use a lot of slots - but this because each slot was assigned smallish daily partitions, a reading that used 153 parallel workers over 0.9M rows. The clustered query instead was able to use a very low amount of slots. Data was well organized to be read by 57 parallel workers, reading 1.12M rows.

[![YPCmI.png](../_resources/0c15d427c28250bd4477dd082294d17f.png)](https://i.stack.imgur.com/YPCmI.png)

[![oA0Eb.png](../_resources/22a46340241e467c4a39e0dd61ad59fb.png)](https://i.stack.imgur.com/oA0Eb.png)

[![DPxKe.png](../_resources/efa45ad986f19ef74be6a15c7730b186.png)](https://i.stack.imgur.com/DPxKe.png)

See also:

- https://medium.com/google-cloud/bigquery-optimized-cluster-your-tables-65e2f684594b
- [How can I improve the amount of data queried with a partitioned+clustered table?](https://stackoverflow.com/questions/58175052/how-can-i-improve-the-amount-of-data-queried-with-a-partitionedclustered-table/58175053#58175053)
- [how clustering works in BigQuery](https://stackoverflow.com/questions/57966914/how-clustering-works-in-bigquery)