Utilizing Google Cloud Data Fusion to support Data Engineering at ML6

# Utilizing Google Cloud Data Fusion to support Data Engineering at ML6

[![0*iv4Eb7DyAmcyky9X.](:/f8e1f195510ba5ad8dc2a9ac671b3e7e) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='120' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://blog.ml6.eu/@KoenVerschaeren?source=post_header_lockup)

[Koen Verschaeren](https://blog.ml6.eu/@KoenVerschaeren)
May 9·4 min read

There are various ways to do data engineering on [Google Cloud Platform](https://cloud.google.com/).

At [ML6](https://www.ml6.eu/) we often get the question of what tool is the best solution.

In a lot of cases, it’s not a straightforward decision because it depends on the type of data, data volume, requirements regarding data lineage and latency, preference and experience of the team, budget…

Over the next few months, we’ll have a look at the different tools and frameworks available on [Google Cloud Platform](https://cloud.google.com/). We’ll focus on a simple use case and try to highlight the features that increase productivity.

A few weeks ago I attended the [Google Cloud Data Fusion](https://blog.ml6.eu/google-cloud-data-fusion-how-ml6-can-bridge-the-data-gap-df914eb0fa18)training so let’s build a data set using the “new kid on the block”: [Cloud Data Fusion](https://cloud.google.com/data-fusion/).

* * *

*...*

A few months ago I discovered on [Bike Share Research](https://bikeshare-research.org/#bssid:antwerp)it’s easy to access the Antwerp Velo API. I’ve deployed a scraper written using [scrapy](https://scrapy.org/) on [Scrapinghub](https://scrapinghub.com/) to fetch the bike availability every 5 minutes and store the results in a JSON line file.

We’ll clean, combine the data with the latest master data and load the data into BigQuery and a Parquet file.

Setting up a [Cloud Data Fusion](https://cloud.google.com/data-fusion/) instance is an easy 3 step process as explained in the [documentation](https://cloud.google.com/data-fusion/docs/how-to/create-instance). It takes about 10–15 minutes for the instance to be available.

One of the task people, with a database / ETL background, struggle with is parsing JSON data.

Let’s check how Cloud Data Fusion simplifies this using the “Wrangler” transformation.

After you’ve selected a file in storage [Cloud Data Fusion](https://cloud.google.com/data-fusion/) samples a number of records and displays the data. Click on the arrow in the column and select Parse + JSON. Enter the depth and boom, the data is transformed into columns.

![](../_resources/de83ed0f7d2b6d087750238df7dff199.png)![1*B9JM-Cc6bwQuOiDkVARzHg.png](../_resources/68cfa3c462e9ec82333cac2dab7c7def.png)

![](../_resources/93f4fe51128e880b882c7886aefee837.png)![1*6_p79ScWC-2cc4jqqO4jgg.png](../_resources/155d5ad59cbbc67ca5adbbecc7e7bb55.png)

I added 6 more “directives” to drop certain columns and correct the data types.

![](../_resources/a4ad9247a2c1f0afc8be4bcb27cc6ec3.png)![1*_GIq0GZI5GOEdeY3CBIoaQ.png](../_resources/52c40220d468c1050f49d842930ccd9e.png)

In 7 clicks I transformed the raw JSON line file into the format needed for the next step.

One of the columns is a date timestamp in E[poch/UNIX format](https://www.epochconverter.com/).

The Parse — Date directive in Wrangler doesn’t support this yet but I found a plug-in in the hub that can do this.

![](../_resources/1e8ed505da3148bbc145ecd27f0defdf.png)![1*XXNMM1Jrh9pSfobUjILpvg.png](../_resources/b3e65d5b3e0f57a16571bb8eb597c7c7.png)

![](:/c85656b92d874486860a0a6d68261597)![1*rRtggZDRY8I1iypJnGTMmg.png](../_resources/8e3c78dc6402ae543706555adfe6631c.png)

In the Date Transform step, you specify the unix time stamp column and the date format you want to output.

![](../_resources/98869b20da097e663bad9533415704b4.png)![1*rjfV7XUuEiNr4umiMrJ4LA.png](../_resources/668205bf948e37efe416dd2524c189f4.png)

To parse the master data JSON I added another storage source and Wrangler transformation followed by a **joiner** to combine the date.

In this step, I renamed the columns to define the final schema.

![](../_resources/3c880bfd792f789fc23ce44f68eee26c.png)![1*5yNWlsE5mPoDta6BSdsP4w.png](../_resources/2a74e14e0b7640fa2ffa55f23cf0466d.png)

Using 2 sinks I write the data to a BigQuery table and Parquet file in storage.

![](../_resources/f79b37302ea3ea7fa7e03106b2519015.png)![1*NOX2LouWDMmT_VPlbq8-Gg.png](../_resources/218646f810fa22355ed59b2c17092469.png)

It’s easy to check that the transformations work as expected by running the job in preview mode.

![](../_resources/02878d01ff016c27619492bf0ea19108.png)![1*g531WXd0oQ7iUe6TGtuosQ.png](../_resources/012c2c6086412c7315b96656c9426ab6.png)

After the preview I save and deployed the job.

It takes about 6 minutes for the job to provision and 25 minutes to process about 9 million records with 1 master node and 2 workers.

This can be improved without any code changes by adding more workers.

![](../_resources/87c43825c407e2c410aa166b4dfa0ab2.png)![1*xpg38X_zH3n37_WemPLdWw.png](../_resources/a0730f963b4700d0c5a2390bfc5378c2.png)

### Conclusion

In this blog post, we only scratched the surface of [Google Cloud Data Fusion](https://cloud.google.com/data-fusion/). Transforming JSON files is a smooth process and certainly beats having to write JSONPath or code manually. It’s not as visual as the excellent JSON and XML mapper in Talend.

Managing the schema across all the steps works as expected.

I need to look into the capabilities of the custom transform in Wrangler because maybe the Unix timestamp to date conversion could be done without an additional transformation. It will be great to see a Parse Unix timestamp functionality because Unix timestamps are used a lot in IoT.

The BigQuery sink and sources need more functionality.
It’s essential to be able to set the create and write dispositions.
I also would like to have a SQL query option in the source.

It would be great to have specific BigQuery actions to for example execute a SQL statement, create/drop tables.

About ML6:

We are a team of AI experts and the fastest growing AI company in Belgium. With offices in Ghent, Amsterdam, Berlin and London, we build and implement self learning systems across different sectors to help our clients operate more efficiently. We do this by staying on top of research, innovation and applying our expertise in practice. To find out more, please visit [www.ml6.eu](http://www.ml6.eu/)