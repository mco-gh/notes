Getting Started

## Getting Started

Pilosa supports an HTTP interface which uses JSON by default. Any HTTP tool can be used to interact with the Pilosa server. The examples in this documentation will use [curl](https://curl.haxx.se/) which is available by default on many UNIX-like systems including Linux and MacOS. Windows users can download curl [here](https://curl.haxx.se/download.html).

> Note that Pilosa server requires a high limit for open files. Check the documentation of your system to see how to increase it in case you hit that limit.

#### Starting Pilosa

Follow the steps in the [Install](https://www.pilosa.com/docs/installation/) document to install Pilosa. Execute the following in a terminal to run Pilosa with the default configuration (Pilosa will be available at `localhost:10101`):

	pilosa server

Let’s make sure Pilosa is running:

	curl localhost:10101/status

Which should output: `{"status":{"Nodes":[{"Host":":10101","State":"UP"}]}}`

#### Sample Project

In order to better understand Pilosa’s capabilities, we will create a sample project called “Star Trace” containing information about the top 1,000 most recently updated Github repositories which have “go” in their name. The Star Trace index will include data points such as programming language, tags, and stargazers—people who have starred a project.

Although Pilosa doesn’t keep the data in a tabular format, we still use the terms “columns” and “rows” when describing the data model. We put the primary objects in columns, and the properties of those objects in rows. For example, the Star Trace project will contain an index called “repository” which contains columns representing Github repositories, and rows representing properties like programming languages and tags. We can better organize the rows by grouping them into sets called Frames. So the “repository” index might have a “languages” frame as well as a “tags” frame. You can learn more about indexes and frames in the [Data Model](https://www.pilosa.com/docs/data-model) section of the documentation.

##### Create the Schema

Note: The queries in this section which are used to set up the indexes in Pilosa just the empty object on success: `{}` - if you would like to verify that a query worked as you expected, you can request the schema as follows:

	curl localhost:10101/schema
	{"indexes":null}

Before we can import data or run queries, we need to create our indexes and the frames within them. Let’s create the repository index first:

	curl localhost:10101/index/repository \
	     -X POST \
	     -d '{"options": {"columnLabel": "repo_id"}}'

Repository IDs are the main focus of the `repository` index, so we chose `repo_id` as the column label.

Let’s create the `stargazer` frame which has user IDs of stargazers as its rows:

	curl localhost:10101/index/repository/frame/stargazer \
	     -X POST \
	     -d '{"options": {"rowLabel": "stargazer_id",
	                      "timeQuantum": "YMD",
	                      "inverseEnabled": true}}'

Since our data contains time stamps for the time users starred repos, we set the *time quantum* for the `stargazer` frame in the options as well. Time quantum is the resolution of the time we want to use, and we set it to `YMD` (year, month, day) for `stargazer`.

We set `inverseEnabled` to `true` in order to allow queries over columns as well as rows.

Next up is the `language` frame, which will contain IDs for programming languages:

	curl localhost:10101/index/repository/frame/language \
	     -X POST \
	     -d '{"options": {"rowLabel": "language_id",
	                      "inverseEnabled": true}}'

##### Import Some Data

The sample data for the “Star Trace” project is at [Pilosa Getting Started repository](https://github.com/pilosa/getting-started). Download the `stargzer.csv` and `language.csv` files in that repo.

	wget https://raw.githubusercontent.com/pilosa/getting-started/master/stargazer.csv
	wget https://raw.githubusercontent.com/pilosa/getting-started/master/language.csv

Run the following commands to import the data into Pilosa:

	pilosa import -i repository -f stargazer stargazer.csv
	pilosa import -i repository -f language language.csv

Note that, both the user IDs and the repository IDs were remapped to sequential integers in the data files, they don’t correspond to actual Github IDs anymore. You can check out `language.txt` to see the mapping for languages.

##### Make Some Queries

> Note The Pilosa server comes with a > [> WebUI](https://www.pilosa.com/docs/webui/)>  for constructing queries in a browser. > [> localhost:10101](http://localhost:10101/)

Which repositories did user 14 star:

	curl localhost:10101/index/repository/query \
	     -X POST \
	     -d 'Bitmap(frame="stargazer", stargazer_id=14)'

What are the top 5 languages in the sample data:

	curl localhost:10101/index/repository/query \
	     -X POST \
	     -d 'TopN(frame="language", n=5)'

Which repositories were starred by user 14 and 19:

	curl localhost:10101/index/repository/query \
	     -X POST \
	     -d 'Intersect(Bitmap(frame="stargazer", stargazer_id=14), Bitmap(frame="stargazer", stargazer_id=19))'

Which repositories were starred by user 14 or 19:

	curl localhost:10101/index/repository/query \
	     -X POST \
	     -d 'Union(Bitmap(frame="stargazer", stargazer_id=14), Bitmap(frame="stargazer", stargazer_id=19))'

Which repositories were starred by user 14 and 19 and also were written in language 1:

	curl localhost:10101/index/repository/query \
	     -X POST \
	     -d 'Intersect(Bitmap(frame="stargazer", stargazer_id=14), Bitmap(frame="stargazer", stargazer_id=19), Bitmap(frame="language", language_id=1))'

Set user 99999 as a stargazer for repository 77777:

	curl localhost:10101/index/repository/query \
	     -X POST \
	     -d 'SetBit(frame="stargazer", repo_id=77777, stargazer_id=99999)'

#### What’s Next?

You can jump to [Data Model](https://www.pilosa.com/docs/data-model/) for an in-depth look at Pilosa’s data model, or [Query Language](https://www.pilosa.com/docs/query-language/) for more details about **PQL**, the query language of Pilosa. Check out the [Tutorials](https://www.pilosa.com/docs/tutorials/) for example implementations of real world use cases for Pilosa. Ready to get going in your favorite language? Have a peek at our small but expanding set of official [Client Libraries](https://www.pilosa.com/docs/client-libraries/).