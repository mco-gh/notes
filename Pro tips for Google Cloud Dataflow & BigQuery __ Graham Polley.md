Pro tips for Google Cloud Dataflow & BigQuery // Graham Polley

# Pro tips for Google Cloud Dataflow & BigQuery

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='icon icon-calendar js-evernote-checked' data-evernote-id='56'%3e %3ctitle data-evernote-id='57' class='js-evernote-checked'%3ecalendar%3c/title%3e %3crect x='3' y='4' width='18' height='18' rx='2' ry='2' data-evernote-id='58' class='js-evernote-checked'%3e%3c/rect%3e%3cline x1='16' y1='2' x2='16' y2='6' data-evernote-id='59' class='js-evernote-checked'%3e%3c/line%3e%3cline x1='8' y1='2' x2='8' y2='6' data-evernote-id='60' class='js-evernote-checked'%3e%3c/line%3e%3cline x1='3' y1='10' x2='21' y2='10' data-evernote-id='61' class='js-evernote-checked'%3e%3c/line%3e %3c/svg%3e) Dec 23, 2019

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='icon icon-clock js-evernote-checked' data-evernote-id='63'%3e %3ctitle data-evernote-id='64' class='js-evernote-checked'%3eclock%3c/title%3e %3ccircle cx='12' cy='12' r='10' data-evernote-id='65' class='js-evernote-checked'%3e%3c/circle%3e%3cpolyline points='12 6 12 12 16 14' data-evernote-id='66' class='js-evernote-checked'%3e%3c/polyline%3e %3c/svg%3e) 13 min read

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='icon icon-tag js-evernote-checked' data-evernote-id='68'%3e %3ctitle data-evernote-id='69' class='js-evernote-checked'%3etag%3c/title%3e %3cpath d='M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z' data-evernote-id='70' class='js-evernote-checked'%3e%3c/path%3e%3cline x1='7' y1='7' x2='7' y2='7' data-evernote-id='71' class='js-evernote-checked'%3e%3c/line%3e %3c/svg%3e)  [googlecloudplatform](https://polleyg.dev/tags/googlecloudplatform/)[clouddataflow](https://polleyg.dev/tags/clouddataflow/)[dataflow](https://polleyg.dev/tags/dataflow/)[bigquery](https://polleyg.dev/tags/bigquery/)[tips](https://polleyg.dev/tags/tips/)[costoptimization](https://polleyg.dev/tags/costoptimization/)

### More drivel

‘Tis the season to be kind and generous, or so I’ve been told. With that festive spirit in mind, I thought it would be a good idea to share my pro tips (and also some random fun facts) for Google Cloud Dataflow and BigQuery. These are the two tools on the Google Cloud stack that I’ve worked with the most, so I’ve accumulated quite a few of them along the way. I also felt the need to capture them in one central place, and make them easily accessible to myself and others. I’m getting old and forgetful, so this post will come in handy for me when I can’t remember if I should use Legacy or Standard SQL in BigQuery (spoiler: use Standard). It’s not an exhaustive list by any stretch of the imagination, and there’s no specific order or categorisation to them. However, you may notice a running theme of cost optimization throughout the post. That’s because I’m a miser. But, I also like saving our customers money, and helping them sidestep the pitfalls I’ve fallen into over the years.

If you’ve got a few tips of your own and would like them added, then please feel free to ping me on [Twitter](https://twitter.com/polley/). Likewise if you spot something that’s wrong.

Finally, apologies in advance for the wall of text coming up. Finding suitable images for black themes/background is beyond my lacklustre computering skillz.

### Cloud Dataflow:

If you’re new to Cloud Dataflow, I suggest starting [here](https://cloud.google.com/dataflow/) and reading the official docs first.

1. Develop locally using the `DirectRunner`, not on Google Cloud using the `DataflowRunner`. The `Direct Runner` allows you to run your pipeline locally, without the need to pay for worker pools on GCP.

2. When you want to shake-out a pipeline on a Google Cloud using the `DataflowRunner`, use a subset of data and just one small instance to begin with. There’s no need to spin up massive worker pools. That’s just a waste of money silly.

3. Assess the new-*ish*  [Dataflow Streaming Engine](https://cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine) and [Dataflow Shuffle](https://cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#dataflow-shuffle) services to see if reduced costs and performance gains can be made in your pipelines. Check region availability first though as not all are supported.

4. Dataflow has three SDKS. In order of maturity & feature parity: Java > Python > Go. Personally, I recommend to use the Java SDK whenever possible. Java also has strict type safety, so there’s that too y’all.

5. Beam SQL looks promising, but don’t use it in production just yet. It’s not ready, and it’s lacking some SQL features. As a side note, [Cloud Dataflow SQL](https://cloud.google.com/dataflow/docs/guides/sql/dataflow-sql-intro) (which is in alpha at time of writing) is based on Beam SQL. And if you want to go even deeper, Beam SQL is based on [Apache Calcite](https://calcite.apache.org/). It’s turtles all the way down folks.

6. This one *still* catches a lot of people out. Dataflow **is** available in Sydney. Don’t confuse it with the `Regional Endpoint`, which is different and **not** available in Sydney. The `Regional Endpoint` location is where your pipeline is orchested and controlled from, not where the actual worker VMs spin up to process your data. Got it? Great, let’s move on.

7. Keep your security team happy by turning off public IPs if you don’t need them. Simply set the `-usePublicIps=false` flag/parameter. Easy-peasy-lemon-squeezy.

8. Assess [FlexRS](https://cloud.google.com/dataflow/docs/guides/flexrs) for batch jobs. This feature uses a mix of regular and preemptible VMs, and might work out to be cheaper for you to use. Again, check region availability first though.

9. If left unspecified, Dataflow will pick a default instance type for your pipeline. For example, if it’s a streaming pipeline, it picks an `n1-standard-4` worker type. For most use cases you don’t need such big nodes. This will save you quite a bit of coin. Experiment with the instance size during shake-out and testing.

10. Cap the max number of instances for auto scaling. Experiment with the best number for your pipeline. Be cautious if you allow auto scaling with no cap on the max workers. Dataflow has been known to overprovision the worker pool for no apparent reason. I’ve seen this happen quite a bit. However, I do know that the Dataflow team have been working hard recently to make the auto scaling algorithm a lot sharper. Another option is to simply turn off auto scaling altogether if you know you won’t need it.

11. There was a bug with older versions of Dataflow where it would leave all its files behind in a GCS bucket. Err on the side of caution, and have a post processing step that always checks and deletes any temp buckets that were created during pipeline execution. Why? Because GCS costs can rack up quickly my friends.

12. When loading data/files from GCS, be sure to set [lifecycle policies](https://cloud.google.com/storage/docs/lifecycle) on your buckets (e.g. Coldline after N period), or delete the files altogether. Again, this reduces costs, which can creep up quickly on GCS. See #11 too.

13. Be wary when updating Dataflow streaming pipelines. You can do it, but Dataflow performs a [capability check](https://cloud.google.com/dataflow/docs/guides/updating-a-pipeline#CCheck) first. If the change is too complex, it will be rejected and the update will not happen.

14. Jobs can hang. It’s just software after all. Set up a monitor (e.g. Stackdriver) to alert your ops team if a job/pipeline that should only take predetermined period of time goes e.g. 5x over normal/expected execution time.

15. I’m yet to see Apache Beam run well on other runners like Flink and Spark in production at scale. If you’re doing this, and it’s working well for you, then please ping me. I’d love to hear about it. Seriously!

16. You don’t *have* to use [templates](https://cloud.google.com/dataflow/docs/guides/templates/overview) to pass runtime/dynamic parameters to your pipeline. Sometimes the `ValueProvider` framework that allows you to do this can be a little too opinionated and limiting. There’s nothing stopping you - in the case of the Java - running it as a fat JAR or even compiling and running from scratch. You can then pass whatever parameters you like. See [this](https://twitter.com/robertsahlin/status/1191990209417744384) Tweet from Robert Sahlin for some more deets. He knows what he’s doing.

17. Cloud Dataflow currently only runs in one zone. Some of the customers we work with require hot failover in the case of a zone going down. Until multi-zone is supported, you’ll need to engineer a workaround yourself e.g. set up Stackdriver monitoring to detect zonal problems, and automatically redeploy the pipeline to a healthy zone.

18. Test, test, and test some more. Make sure you write robust unit tests for your pipeline. There’s plenty of examples in the docs about how to test your Dataflow pipeline. You can use stubs/mocks in Java world. I don’t know how it works in Python.

19. Use the [*Dead Letter*](https://en.wikipedia.org/wiki/Dead_letter_queue) pattern to siphon off bad data. We like to dump our bad data into BigQuery and perform analysis on them as they come in. It could be bad data or just your dodgy code. Either way, catch it, log it, and then dead letter it. Simples y’all.

20. Remember, a `ParDo` can execute any arbitrary code you like. You just need to be smart about it e.g. don’t go creating a JDBC connection inside one of your `ParDos`! You can call out to other GCP services or web services from inside your `ParDo`. This is something that we do commonly, and it works well.

21. Familiarise yourself with the `@Setup`, `@ProcessBundle`, `@FinishBundle` and `@TearDown` methods/annotations, and don’t get them mixed up. You use them to solve different problems e.g. use `@Setup` to establish resource heavy network connections that can be reused. See [here](https://beam.apache.org/releases/javadoc/2.12.0/index.html?org/apache/beam/sdk/transforms/DoFn.Setup.html).

22. Fun fact: Cloud Dataflow is based on Apache Beam. We all know that. But, did you know that it’s all based on two internal products that Google built for themselves called [FlumeJava (batch)](https://research.google/pubs/pub35650/) and [Millwheel (streaming)](https://research.google/pubs/pub41378/)? Probably not, because you don’t need to know this stuff. I just find it interesting. Oh, and ever wondered what *“Beam”* stood for? Well, folklore has it that the *“B”* is for **B**atch and *“eam”* is for Str**eam**ing - alas a framework that can do both batch and streaming.

### BigQuery:

If you’re new to BigQuery, I suggest starting [here](https://cloud.google.com/bigquery/) and reading the official docs first.

1. Export all your [audit](https://cloud.google.com/bigquery/docs/reference/auditlogs/#stackdriver_logging_exports) and [billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery) logs back to BigQuery for analysis. I don’t know how many times this pattern has saved my butt.

2. Don’t be lazy with your SQL. Avoid `SELECT *` on big tables unless you absolutely have to. BigQuery charges on data scanned. The less columns you reference, the cheaper the query.

3. BigQuery likes wide, denormalized tables with nested and repeated data. So, [denormalise whenever possible](https://cloud.google.com/solutions/bigquery-data-warehouse#designing_schema) (also see [here](https://cloud.google.com/bigquery/docs/best-practices-performance-input#denormalize_data_whenever_possible)). However, that doesn’t mean BigQuery can’t handle normalised data and joins. It absolutely can. It just performs better on denormalized stuff because BigQuery is essentially an OLAP engine.

4. `LIMIT` does not reduce costs. It’s an anti-pattern. You still pay for the table scan. It will return your results quicker though.

5. Use [custom quotas](https://cloud.google.com/bigquery/docs/custom-quotas) to control costs when using on-demand. Also, use `max-bytes-billed` to control individual query costs. Gotta watch those greens!

6. Try to avoid ingestion-based [partitioning](https://cloud.google.com/bigquery/docs/partitioned-tables) if you can. It can get cumbersome when wrangling the data and working across multiple time zones. Instead, partition by a column instead. It’s more intuitive and easier to maintain. You can currently partition by date/timestamp or integer range.

7. Once you’ve partitioned your data, then [cluster](https://cloud.google.com/bigquery/docs/clustered-tables) it for a free turbo boost on your queries and some cost savings.

8. For partitioned tables, enforce users specify the partitioned column in their `WHERE` clause by using setting the `require-partition-filter` to `true`. Reduces cost and speeds up query time.

9. Contrary to popular belief, BigQuery’s storage layer is not GCS. It’s [Colossus](https://cloud.google.com/files/storage_architecture_and_challenges.pdf). GCS and BigQuery both use Colossus under the hood. Oh, and again, you don’t *need* to know this stuff, but it’s a fun fact: BigQuery uses Bigtable for its streaming engine, and Spanner for its metadata and query result preview. Ta-da!

10. [`dry-run`](https://cloud.google.com/bigquery/docs/dry-run-queries) is your friend. Use it! It checks that your query is syntactically correct and also estimates the cost of the query.

11. Keep an eye on the [materialized views](https://issuetracker.google.com/issues/62244996). It’s something that the BigQuery community have been waiting a long time for.

12. Set [TTLs on datasets/tables](https://cloud.google.com/bigquery/docs/managing-tables) when you know data won’t be needed after N period. If you want to archive even further, move it out to GCS coldline. It’s much cheaper.

13. Don’t `SELECT *` to preview data. Use `bq head` or `tabledata.list` instead.

14. BigQuery Machine Learning (BQML) is cool ‘n all, but dang [is it expensive](https://cloud.google.com/bigquery-ml/pricing#ml_on_demand_pricing)! At time of writing, it’s ~$470(AUD) p/TB when creating/training the model if you’re using the on-demand pricing model (it’s included as part of the flat-rate model). Be warned.

15. Don’t use streaming ingestion if you don’t have to. You need to pay for it. Batch loading is free on the other hand.

16. Enable the cache (24hrs). Remember that it’s not shared though. It’s per user, per project. Use something with a service/account in the middle if you want to share the cache i.e. a proxy.

17. Editing - **not querying** - a table resets the long-term storage discount counter. You’ll have to wait 90 days again if you do edit it. Bummer.

18. Be wary of 3rd party chrome plugins that promise to save you lots of money or improve the performance of your queries. They require elevated permissions on your GCP project(s), which might not fly with your security/privacy teams - especially at an enterprise level. I’m also dubious about their lofty claims.

19. Use the [Public Issue Tracker](https://issuetracker.google.com/savedsearches/559654) to raise feature requests and get your friends to star them. The BigQuery engineers and PMs hang out a lot there. Don’t comment with *”+1”*. Instead, actually star it to give it a proper vote.

20. Don’t use legacy SQL for new queries. No excuses - just don’t! If you’re running legacy SQL from the old days, get a plan together to migrate off it ASAP. It’s no longer maintained and nothing new is backported.

21. Put your SQL in source control. Don’t treat it as a 2nd class citizen. Integrate it into your CI/CD pipelines. That should be a no-brainer.

22. Use [SESSION_USER()](https://cloud.google.com/bigquery/docs/reference/standard-sql/security_functions#session_user) as a workaround to BigQuery not having row level permissions yet. Until it’s available you’ll need to do [this](https://stackoverflow.com/questions/29683423/how-do-i-give-different-users-access-to-different-rows-without-creating-separate) as recommended by Google.

23. Currently, BigQuery supports customer managed keys (CMEK), not customer supplied keys (CSEK). See [here](https://cloud.google.com/bigquery/docs/encryption-at-rest#cmek). Don’t confuse *’client side encryption’* with CSEK. They are not the same thing.

24. Avoid using the [native scheduled queries feature in BigQuery](https://cloud.google.com/bigquery/docs/scheduling-queries) if you can. I don’t like how they’ve implemented on top of the BigQuery Data Transfer Service (BQ-DTS). It raises too many concerns and questions by security teams - and rightly so. It also confuses people. Finally, they are tied to user accounts and very hard to untangle should the user/employee offboard the company, and not scalable. Instead use something like Cloud Scheduler + Cloud Build or Apache Airflow.

25. Instead of using Dataflow for ETL, look at BigQuery as perfectly good ETL tool in its own right. It’s also more performant. But, there are trade offs e.g. it’s easier to test code (Dataflow) than SQL etc.

26. BigQuery is not limitless. Data skews, too many joins, `ORDER BY` etc. will hurt performance and queries will fail. Keep your SQL lean. Watch [this](https://www.youtube.com/watch?v=UueWySREWvk) great video from Jordan Tigani for a deep dive on advanced techniques in BigQuery. It’s a classic.

27. Another fun fact is that all queries in BigQuery are performed in memory. Bam! That said, [a spill to disk](https://cloud.google.com/bigquery/query-plan-explanation#query_plan_information) is still possible on BigQuery when a slot is overwhelmed ;)

28. Assess the new [Storage API](https://cloud.google.com/bigquery/docs/reference/storage/) for quicker data retrieval. You need to pay for it though. Yikes!

29. [BI Engine](https://cloud.google.com/bi-engine/docs/overview) is currently very immature, but keep an eye on it as it grows up. Get ready to see Looker support, APIs etc. as time goes on, I guess.

30. Use [batch queries](https://cloud.google.com/bigquery/docs/running-queries#batch) when your queries are not time sensitive. They don’t count toward your 100 concurrent query limit.

31. Use approximate functions (within 1% of exact number) when you don’t need exact results e.g. `approx_count_distinct`. If you’re dealing with numbers in the tens of millions upwards, do you really need the answer to be exact? Who really cares if you’re stock trading system is out by a few cents. Oh wait..

32. BigQuery has [two pricing models](https://cloud.google.com/bigquery/pricing): on-demand and flat-rate. Learn the difference between the two of them. If your compute/analysis monthly bill is pushing north of $10K USD, then it’s time to look at flat-rate.

33. The [limits and quotas page](https://cloud.google.com/bigquery/quotas) are important to stay abreast of. However, some of them are soft limits. If you’re a big enough customer then they can be raised on per-case basis. Talk to your local Google rep.

34. Someone that I work with, and who’s a lot smarter than me, wrote a nifty little [open source tool for analysing all your BigQuery views](https://github.com/servian/bigquery-view-analyzer). It’s very handy indeed.

35. The `bq` command line tool is incredibly powerful. You can solve a lot of problems with it, quickly and easily. You hook in all your favourite Bash commands/tools using pipe. See [here](https://stackoverflow.com/questions/58988969/bigquery-longterm-storage-table-list/58994505#58994505) for an example. #shamelessplug

36. Google recently open sourced ZetaSQL, which is the SQL parser and analyzer that drives BigQuery (and others e.g. Spanner). ZetaSQL can be found [here](https://github.com/google/zetasql). This is very useful if you want to build, for example, a BigQuery test harness/framework ;)

37. You can use `FOR SYSTEM_TIME AS` restore previously deleted tables/rows. It supports up to 7 days in the past. Awww, snap! See [here](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#syntax).

38. BigQuery now has [scripting](https://cloud.google.com/bigquery/docs/reference/standard-sql/scripting), which allows you to do all sorts of funky stuff like send multiple statements to BigQuery in one request, use variables, tap into control flow statements such as `IF` and `WHILE`, and loops. Neat.

39. Just a few weeks ago, the BigQuery team announced that on-demand queries can [burst](https://cloud.google.com/bigquery/docs/release-notes#December_10_2019) through the default of 2000 concurrent slots *“when it can”*. I’d love to see more details released around how exactly BigQuery dertermines when it can burst. Very cool, nonetheless.