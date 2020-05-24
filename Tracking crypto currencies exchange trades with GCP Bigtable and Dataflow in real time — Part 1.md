Tracking crypto currencies exchange trades with GCP Bigtable and Dataflow in real time — Part 1

# Tracking Cryptocurrencies Exchange Trades with Google Cloud Platform in Real-Time — Part 1

[![0*w4UChhphNAcdlL_R.jpg](../_resources/4a8fd3f42a578267b224cb4f34fb1b84.jpg)](https://medium.com/@igalic?source=post_header_lockup)

[Ivo Galic](https://medium.com/@igalic)

Mar 13·7 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='225'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

**Authors:**  [Ivo Galic](https://goo.gl/crFQ17), [Mike Altarace](https://www.linkedin.com/in/mike-altarace-06a2b31/)

**Contributors: **[Daniel De Leo](https://www.linkedin.com/in/daniel-deleo/), [Morgante Pell](https://www.linkedin.com/in/morgante/), [Yonni Chen](https://www.linkedin.com/in/yonni-c-29425390/), [Stefan Nastic](https://www.linkedin.com/in/stefan-nastic/)

**TL;DR**: [GitHub Link](https://goo.gl/bB8CrU)

The last year has been like a roller coaster for the cryptocurrency market. At the end of 2017, the value of bitcoin (BTC) almost reached $20,000 USD, only to fall below $4,000 USD a few months later. What if there is a pattern in the high volatility of the cryptocurrencies market? If so, can we learn from it and get an edge on future trends? Is there a way to observe all exchanges in real time and visualize it on a single chart?

In this tutorial we will graph the trades, volume and time delta from trade execution until it reaches our system (an indicator of how close to real time we can get the data).

![](../_resources/43ef5fbca4093fff94c6c56631dc57e6.png)![1*YJKJkKdrd_eY8b6gUEMHsA.gif](../_resources/4f06b4324048da82aeb18a6675f38390.gif)

The goal of the tutorial — realtime multi exchange observer

To achieve that, as a first step, we need to capture as much real-time trading data as possible for analysis. However, the large amount of currency and exchange data requires a scalable system that can ingest and store such volume while keeping latency low. Failing to do so, the system will not stay in sync with the exchanges stream.

In this article, we will use Cloud Dataflow and Cloud Bigtable to satisfy those requirements. Dataflow will provide low latency data streaming ingestion capability while Bigtable will provide low latency storage and time series querying at scale.

### Requirements / Solutions

![](../_resources/bb6d7e92471fb8ae9fe4aef3d9122c95.png)![1*t4iA7Fl0DlHJ8y95tyT4-g.png](../_resources/70b314012196e5d16ae81f3b548e548d.png)

Architectural overview

The “usual” requirement for trading systems is low latency data ingestion. We extend this requirement with near real-time data storage and querying at scale. In the following list we will demonstrate what can be learned by conducting this tutorial:

1. 1 "."Ingest real-time trading data with low latency from globally scattered datasources / exchanges. Possibility to adopt data ingest worker pipeline location. Easily add additional trading pairs / exchanges. **Solution: **[**Dataflow**](https://cloud.google.com/dataflow/)** + **[**Xchange Reactive Websockets Framework**](https://github.com/bitrich-info/xchange-stream)

2. 2 "."Demonstrate an unbounded streaming source code that is runnable with multiple runners. **Solution: **[**Apache BEAM**](https://beam.apache.org/documentation/runners/capability-matrix/)

3. 3 "."Strong consistency + linear scalability + super low latency for querying the trading data. **Solution: **[**Bigtable**](https://cloud.google.com/bigtable/)

4. 4 "."Easy and automated setup with project template for orchestration. Example of dynamic variable insertion from Terraform template into the GCP compute instance. **Solution: **[**Terraform**](https://www.terraform.io/)

5. 5 "."Querying and visualization — Execute time series queries on Bigtable visualize it in on the webpage. **Solution: **[**Python Flask **](http://flask.pocoo.org/)**+ **[**Vis.js**](http://visjs.org/showcase/index.html)** + **[**Google BigTable Python Client**](https://github.com/googleapis/google-cloud-python/tree/master/bigtable)

### Architecture/How it works

The source code is written in **Java 8, Python 2.7, JavaScript **and we are using** Maven, PIP **for dependency/build management.

The code can be divided into five main framework units:

1. 1 "."**Data ingestion — **XChange Stream framework (G[ithub link](https://github.com/bitrich-info/xchange-stream)) **

**Java library providing a simple and consistent streaming API for interacting with Bitcoin and other cryptocurrency exchanges via WebSocket protocol. XChange library is providing new interfaces for streaming API. User can subscribe for live updates via reactive streams of RxJava library.

*We use this JAVA 8 framework to connect and configure some exchanges (BitFinex, Poloniex, BitStamp, OkCoin, Gemini, HitBTC, Binance…).

****  ***[***Link to the exchange / trading pair configuration code***](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/src/main/java/run/RunThePipeline.java#L127-L171)

2. 2 "."**Parallel processing — **Apache Beam (G[ithub link](https://github.com/apache/beam))**

**Apache Beam is an open source unified programming model to define and execute data processing pipelines, including ETL, batch and stream (continuous) processing. Supported runners: Apache Apex, Apache Flink, Apache Gearpump, Apache Samza, Apache Spark, and **Google Cloud Dataflow.

***We demonstrate how to create an unbounded streaming source/reader and manage basic watermarking, checkpointing and record id for data ingestion.

*[***Link to the bridge between BEAM and XChange Stream framework***](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/src/main/java/source/CryptoMarketTradeUnboundedReader.java#L108-L127)

3. 3 "."**BigTable sink** — Cloud Bigtable with Beam using the HBase API. (G[ithub link](https://github.com/GoogleCloudPlatform/cloud-bigtable-client/tree/master/bigtable-dataflow-parent/bigtable-hbase-beam)) Connector and writer to Bigtable.

*We explain here how to create a row key and create a Bigtable mutation function prior to writing to Bigtable.

*[***Link to the BigTable key creation / mutation function***](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/src/main/java/run/RunThePipeline.java#L68-L102)

4. 4 "."**Realtime API endpoint **— Flask web server at port:5000+ BigTable client ([GitHub link](https://github.com/googleapis/google-cloud-python/tree/master/bigtable)) will be used to query the Bigtable and serve as API endpoint.

[***Link to the BigTable query builder***](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/frontend/app.py#L38-L55) + [***results retrieval and sampling***](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/frontend/app.py#L62-L96)

5. 5 "."**JavaScript Visualization **— [Vis.JS](http://visjs.org/graph2d_examples.html) Flask template that will query the real-time API endpoint every 500ms.

[***Link to the HTML template file***](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/frontend/templates/streamingvisjs.html)

![](../_resources/bacd4c058079ffbc80dddcbf0dd7e75e.png)![1*9gKpSLQIp-BuYqIICIl8EQ.png](../_resources/eccf4344ded572967988dbd8f172fca9.png)

Flask web server will be run in the GCP VM instance

### Pipeline definition

![](../_resources/57fbc28a6da0f0b0935ea23072e92f82.png)![1*K_xqpJiagRF1mzFk6TJP3A.png](../_resources/3fbcba03b7835e7e4d56775956bf3052.png)

For every exchange + trading pair, we [create a different pipeline instance.](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/src/main/java/run/RunThePipeline.java#L175-L183) Pipeline consists of 3 steps:

1. 1 "."[UnboundedStreamingSource that contains ‘Unbounded Streaming Source Reader](https://github.com/galic1987/professional-services/tree/master/examples/cryptorealtime/src/main/java/source)’ *(bitStamp2)*

2. 2 "."[BigTable pre-writing mutation and key definition](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/src/main/java/run/RunThePipeline.java#L71-L102)

*(ETH-USD Mut2)*

3. 3 "."[BigTable write step](https://github.com/galic1987/professional-services/blob/master/examples/cryptorealtime/src/main/java/run/RunThePipeline.java#L180)  *(ETH-USD2)*

### Bigtable row key design decisions

Our DTO looks like this:

![](../_resources/fd23f0d5240d67453989b3eba2ce9f1d.png)![1*OX6wS8C6-uS9-6phzGDQZw.png](../_resources/beae2855c918b3c6000417f5564f47f5.png)

We formulated the row key structure in the following way: TradingCurrency#Exchange#SystemTimestampEpoch#SystemNanosTime.

E.g: a row key might look like **BTC/USD**#**Bitfinex**#**1546547940918**#**63187358085**

BTC/USD — Trading Pair
Bitfinex — Exchange

1546547940918 — Epoch timestamp ([more info](https://www.tutorialspoint.com/java/lang/system_currenttimemillis.htm))

63187358085 — System Nano time ([more info](https://docs.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime%28%29))

**Why do we add nanotime at our key end?**

Our design decision is to avoid multiple versions per row for different trades. Two DoFn mutations might execute in the same Epoch ms time if there is a streaming sequence of TradeLoad DTOs. NanoTime at the end will split Millisecond to an additional one million.

If this is not enough for your needs we recommend hashing the volume / price ratio and attaching the hash at the end of the row key.

Row cells will contain an exact schema replica of the exchange TradeLoad DTO (see earlier in the table above). This choice will help us go from a specific (trading pair) — (exchange) to less specific (timestamp — nanotime) and avoid hotspots when you query the data.

### Costs

This tutorial uses billable components of Google Cloud Platform, including: ***Dataflow, Compute Engine, Google Cloud Storage, BigTable***

We recommend to clean up the project after finishing this tutorial to avoid costs. Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

### Environment setup

Use [Terraform instructions](https://github.com/galic1987/cryptorealtime/blob/master/TERRAFORM-README.md) if you are familiar with Terraform, it can save you a lot of time. Otherwise, just continue.

We assume you have a Google Cloud Project associated with a billing account already (otherwise check out the [getting-started](https://cloud.google.com/gcp/getting-started/) section). Log into the console, and activate a cloud console session

![0*Czg3HJmm5NJfXutv](../_resources/4367b112d8db894b1ba27b547124c5ff.jpg)

We’ll need a VM to drive the creation of the pipeline so let’s create one with the following command:

|     |     |
| --- | --- |
| 1   | gcloud beta compute instances create crypto-driver \ |
| 2   | --zone=us-central1-a \ |
| 3   | --machine-type=n1-standard-1 \ |
| 4   | --subnet=default \ |
| 5   | --network-tier=PREMIUM \ |
| 6   | --maintenance-policy=MIGRATE \ |
| 7   | --service-account=$(gcloud iam service-accounts list --format='value(email)' --filter="compute") \ |
| 8   | --scopes=https://www.googleapis.com/auth/cloud-platform \ |
| 9   | --image=debian-9-stretch-v20181210 \ |
| 10  | --image-project=debian-cloud \ |
| 11  | --boot-disk-size=20GB \ |
| 12  | --boot-disk-type=pd-standard \ |
| 13  | --boot-disk-device-name=crypto-driver |

 [view raw](https://gist.github.com/galic1987/c69d46dea6102163c1ae02bdada973ca/raw/1b4f479e86d7ca3a026c60dbecf3455dc1751b0b/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/c69d46dea6102163c1ae02bdada973ca#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Note how we used the compute engine service account with cloud API scope, we need that to easily build up the environment.

Wait for the VM to come up and SSH into it.

Installing necessary tools like java, git, maven, pip, python 2.7 and [cloud bigtable command line tool](https://cloud.google.com/bigtable/docs/cbt-overview) cbt using the following command:

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | sudo -s |
| 2   | apt-get update && apt-get upgrade |
| 3   | apt -y install python2.7 python-pip openjdk-8-jdk git maven google-cloud-sdk-cbt |

 [view raw](https://gist.github.com/galic1987/f97121ec55f9f075be462aa8e2ce0e06/raw/4ca30c4de8b0782664057599c7c6c94265b80818/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/f97121ec55f9f075be462aa8e2ce0e06#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

We’ll now enable some APIs, create a Bigtable instance and a bucket:

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | export PROJECT=$(gcloud info --format='value(config.project)') |
| 2   | export ZONE=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/zone" -H "Metadata-Flavor: Google"\|cut -d/ -f4) |
| 3   | gcloud services enable bigtable.googleapis.com \ |
| 4   | bigtableadmin.googleapis.com \ |
| 5   | dataflow.googleapis.com \ |
| 6   | --project=${PROJECT} |
| 7   |     |
| 8   | gcloud bigtable instances create cryptorealtime \ |
| 9   | --cluster=cryptorealtime-c1 \ |
| 10  | --cluster-zone=${ZONE} \ |
| 11  | --display-name=cryptorealtime \ |
| 12  | --cluster-storage-type=HDD \ |
| 13  | --instance-type=DEVELOPMENT |
| 14  | cbt -instance=cryptorealtime createtable cryptorealtime families=market |

 [view raw](https://gist.github.com/galic1987/82bb5498470359b553dd52d0b3a44b58/raw/c185005c65cef182f6db7d861cc6b7ee69f6cb4c/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/82bb5498470359b553dd52d0b3a44b58#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

In this scenario, we use one column family called ‘market’ to simplify the schema design. For more on that you can read this [link](https://cloud.google.com/bigtable/docs/schema-design#column_families).

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | gsutil mb -p ${PROJECT} gs://realtimecrypto-${PROJECT} |

 [view raw](https://gist.github.com/galic1987/dabbff6b5624afcb046e011e3e6b6dcf/raw/55bfa11d97964184464d688aaa1377d92459470b/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/dabbff6b5624afcb046e011e3e6b6dcf#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Ready to go, clone the repo

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | git clone https://github.com/GoogleCloudPlatform/professional-services |

 [view raw](https://gist.github.com/galic1987/f0f56eafa8ece40e66b33f5246e7e77f/raw/7a1a01405573f9c6ce37d04e54c9e75402e07392/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/f0f56eafa8ece40e66b33f5246e7e77f#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Now we will build the pipeline

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | cd professional-services/examples/cryptorealtime |
| 2   | mvn clean install |

 [view raw](https://gist.github.com/galic1987/2db3a1b9cf612e1df5ec7027da386de0/raw/d5c2a099f0c684936a42975d7803d9bbc217d4eb/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/2db3a1b9cf612e1df5ec7027da386de0#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/ce9a128a5875b9ab75a8742e7975f75f.png)![1*URNjv2XnpBqidDPyakqMNA.png](../_resources/43fe8e99449f1cda1c4771abb9bc92b9.png)

You should see this at the end if everything is OK
Now we can finally start the pipeline

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | ./run.sh ${PROJECT} \ |
| 2   | cryptorealtime gs://realtimecrypto-${PROJECT}/temp \ |
| 3   | cryptorealtime market |

 [view raw](https://gist.github.com/galic1987/0f2e589c194c82d1fc76e0e8e50ff45d/raw/977e417061e8ffb6221666da11fb5721c81ce104/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/0f2e589c194c82d1fc76e0e8e50ff45d#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Please ignore illegal thread pool exceptions. After a few minutes we can observe the incoming trades by peeking into the Bigtable table.

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | cbt -instance=cryptorealtime read cryptorealtime |

 [view raw](https://gist.github.com/galic1987/43ae447df386acd4317942977668f652/raw/79daf054071df78720c2f3f92d5a94251aa8b68a/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/43ae447df386acd4317942977668f652#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/eddfbddc4dea45087cdcc48ec84b884b.png)![1*PUKBrQyCux-vdM-DlWid5Q.png](../_resources/b21818507756894549d6f94ab02abe73.png)

To observe the Dataflow pipeline navigate to[the console Dataflow page](https://console.cloud.google.com/dataflow?project=). And click the pipeline and view the Job status as Running:

![](../_resources/bcdc932792cc59bbeab7306e46805e69.png)![0*9BcmVHjoVHYHg-HZ](../_resources/a97dea908e92fa0cea8f7957ff22ee5f.png)

To run the Flask frontend server visualization navigate to frontend directory inside our VM and build the python package

### Visualization

Open firewall port 5000 for visualization:

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | gcloud compute --project=${PROJECT} firewall-rules create crypto-dashboard \ |
| 2   | --direction=INGRESS \ |
| 3   | --priority=1000 \ |
| 4   | --network=default \ |
| 5   | --action=ALLOW \ |
| 6   | --rules=tcp:5000 \ |
| 7   | --source-ranges=0.0.0.0/0 \ |
| 8   | --target-tags=crypto-console \ |
| 9   | --description="Open port 5000 for crypto visualization tutorial" |

 [view raw](https://gist.github.com/galic1987/ca20a13e8907cca1e4096eae7d599a10/raw/7d30fa78c2d6bd4db990d3651b9cc7efb65cb930/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/ca20a13e8907cca1e4096eae7d599a10#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Link VM with the firewall rule:

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | gcloud compute instances add-tags crypto-driver --tags="crypto-console" --zone=${ZONE} |

 [view raw](https://gist.github.com/galic1987/94af43d7eaf862ca87209a425945ad81/raw/b0df5738f5ae2f20188bb19bbc4373d657109c36/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/94af43d7eaf862ca87209a425945ad81#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Navigate to frontend directory

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | cd frontend/ |
| 2   | pip install -r requirements.txt --user |
| 3   | python app.py ${PROJECT} cryptorealtime cryptorealtime market |

 [view raw](https://gist.github.com/galic1987/863b052e9ce32562af82e007753f7c42/raw/c73d1d73e8a1a3555eba4efee91707445085b5dd/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/863b052e9ce32562af82e007753f7c42#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Find your external IP in[Compute console](https://console.cloud.google.com/compute/instances) and open it in your browser with port 5000 at the end e.g.

***http://external-ip:5000/stream***

You should be able to see the visualization of aggregated BTC/USD pair on several exchanges (without predictor part)

![](../_resources/43ef5fbca4093fff94c6c56631dc57e6.png)![1*YJKJkKdrd_eY8b6gUEMHsA.gif](../_resources/4f06b4324048da82aeb18a6675f38390.gif)

The goal of the tutorial — realtime ‘periscope’ multi exchange observer
Enjoy!

### Cleanup

To save on cost we can clean up the pipeline by running the following command

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | gcloud dataflow jobs cancel \ |
| 2   | $(gcloud dataflow jobs list \ |
| 3   | --format='value(id)' \ |
| 4   | --filter="name:runthepipeline*") |

 [view raw](https://gist.github.com/galic1987/4adc16b5c87cbfb2e35a847cf8f383a3/raw/b9dcdced84787291c55a1f46d6d77dc76617f88c/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/4adc16b5c87cbfb2e35a847cf8f383a3#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Empty and Delete the bucket:

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | gsutil -m rm -r gs://realtimecrypto-${PROJECT}/* |
| 2   | gsutil rb gs://realtimecrypto-${PROJECT} |

 [view raw](https://gist.github.com/galic1987/6a69101cdfb9ff97356773f3b9d63d7d/raw/9cf2bd372d00f99ba24ff6b4d8e261b13b2d5696/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/6a69101cdfb9ff97356773f3b9d63d7d#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Delete the Bigtable instance:

![](../_resources/ce3c62f97f43dab362eed1864646ade9.png)

|     |     |
| --- | --- |
| 1   | gcloud bigtable instances delete cryptorealtime |

 [view raw](https://gist.github.com/galic1987/010b534765dae4fb72fcf641f904d670/raw/744fc877a5d8f572020f3bb94d181f5dd0b855fe/gistfile1.txt)  [gistfile1.txt](https://gist.github.com/galic1987/010b534765dae4fb72fcf641f904d670#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com/)

Exit the VM and delete it from the console.

### Conclusion

In this article, we have discussed the most important design and technical decisions: i) how to set up and configure pipeline for ingesting real-time, time-series data from various crypto exchanges ii) how to design suitable data model, which facilitates querying and graphing at scale.

Finally, we have provided a tutorial on how to set up and deploy the proposed architecture using GCP. By following the tutorial steps we managed to establish a connection to multiple exchanges, subscribe to their trade feed, extract and transform these trades into a flexible format to be stored in Bigtable and to be graphed and analyzed.

If our readers show interest (please follow us to do so), we will extend the tutorial with the second part where we will build ML models to predict trends. Do not hesitate to ask questions in the comment section.