yolossn/Prometheus-Basics: A beginner friendly introduction to prometheus 🔥

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='56'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='890' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#prometheus-basics)Prometheus-Basics

A beginner friendly introduction to prometheus.

 [![logo.png](../_resources/bc3ebd8f3ac51841be75cf5a27c01ddc.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/logo.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='57'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='894' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#table-of-contents)Table of Contents

1. [What is prometheus ?](https://github.com/yolossn/Prometheus-Basics#what-is-prometheus-)

2. [What are metrics and why is it important ?](https://github.com/yolossn/Prometheus-Basics#what-are-metrics-and-why-is-it-important)

3. [Basic Architecture of Prometheus](https://github.com/yolossn/Prometheus-Basics#basic-architecture-of-prometheus)

4. [Show me how it is done](https://github.com/yolossn/Prometheus-Basics#show-me-how-it-is-done)

5. [Types of metrics](https://github.com/yolossn/Prometheus-Basics#types-of-metrics)

6. [Create a simple exporter](https://github.com/yolossn/Prometheus-Basics#create-a-simple-exporter)

7. [References](https://github.com/yolossn/Prometheus-Basics#References)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='58'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='903' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#what-is-prometheus-)What is prometheus ?

Prometheus is a system monitoring and alerting system. It was opensourced by SoundCloud in 2012 and was incubated by Cloud Native Computing Foundation. Prometheus stores all the metrics data as time series, i.e metrics information is stored along with the timestamp at which it was recorded, optional key-value pairs called as labels can also be stored along with metrics.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='59'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='905' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#what-are-metrics-and-why-is-it-important)What are metrics and why is it important?

Metrics in layman terms is a standard for measurement. What we want to measure depends from application to application. For a web server it can be request times, for a database it can be CPU usage or number of active connections etc.

Metrics play an important role in understanding why your application is working in a certain way. If you run a web application and someone comes up to you and says that the application is slow. You will need some information to find out what is happening with your application. For example the application can become slow when the number of requests are high. If you have the request count metric you can spot the reason and increase the number of servers to handle the heavy load. Whenever you are defining the metrics for your application you must put on your detective hat and ask this question **what all information will be important for me to debug if any issue occurs in my application?**

Analogy: I always use this analogy to simply understand what a monitoring system does. When I was young I wanted to grow tall and to measure it I used height as a metric. I asked my dad to measure my height everyday and keep a table of my height on each day. So in this case my dad is my monitoring system and the metric was my height.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='60'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='909' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#basic-architecture-of-prometheus)Basic Architecture of Prometheus

The basic components of prometheus are:

- Prometheus Server (The server which scrapes and stores the metrics data).
- Client Library which is used to calculate and expose the metrics.
- Alert manager to raise alerts based on preset rules.

(Note: Apart from this prometheus has push gateways which I am not covering here).

 [![architecture.png](../_resources/9f85204251b058e2aa80aa0f9fd62bde.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/architecture.png)

Let's consider a web server as an example application. I want to extract a certain metric like the number of API calls processed by my web server. So I add certain instrumentation code using the prometheus client library and expose the metrics information. Now that my web server also exposes its metrics I want it to be scraped by prometheus. So I run prometheus separately and configure it to fetch the metrics from the web server which is listening on xyz IP address port 7500 at a specific time interval, say, every minute.

I set prometheus up and expose my web server to be accessible for the frontend or other client to use.

At 11:00 PM when I make the server open to consumption. Prometheus scrapes the count metric and stores the value as 0

By 11:01 PM one request is processed. The instrumentation logic in my code makes the count to 1. When prometheus scraps the metric the value of count is 1 now

By 11:02 PM two requests are processed and the request count is 1+2 = 3 now. Similarly metrics are scraped and stored

The user can control the frequency at which metrics are scraped by prometheus

| Time Stamp | Request Count (metric) |
| --- | --- |
| 11:00 PM | 0   |
| 11:01 PM | 1   |
| 11:02 PM | 3   |

(Note: This table is just a representation for understanding purposes. Prometheus doesn’t store the values in the exact format)

Prometheus also has a server which exposes the metrics which are stored by scraping. This server is used to query the metrics, create dashboards/charts on it etc. PromQL is used to query the metrics.

A simple Line chart created on my Request Count metric will look like this

 [![graph.png](../_resources/c8e8420ae4db9c0ca3ce634143b86a3b.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/graph.png)

I can scrape multiple metrics which will be useful to understand what is happening in my application and create multiple charts on them. Group the charts into a dashboard and use it to understand what is happening in my application.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='61'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='943' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#show-me-how-it-is-done)Show me how it is done.

Let’s get our hands dirty and setup prometheus. Prometheus is written using golang and all you need is the binary compiled for your operating system. Download the binary corresponding to your operating system from [here](https://prometheus.io/download/) and add the binary to your path.

Prometheus exposes its own metrics which can be consumed by itself or another prometheus server.

Now that we have Prometheus, the next step is to run it. All that we need is just the binary and a configuration file. Prometheus uses yaml files for configuration.

*prometheus.yml*
global: scrape_interval: 15s  scrape_configs:

- job_name: prometheus  static_configs:
- targets: ["localhost:9090"]

In the above configuration file we have mentioned the scrape_interval i.e how frequently you want prometheus to scrape the metrics. We have added scrape_configs which has a name and target to scrape the metrics from. Prometheus by default listens on port 9090. So I have added it.

> prometheus --config.file=prometheus.yml

 [![prometheus1.gif](../_resources/96ba938fb10ff6106687a202d3571db2.gif)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/prometheus1.gif)

Now we have Prometheus up and running and scraping its own metrics every 15s. Prometheus has standard exporters available to export metrics. Next we will run a node exporter which is an exporter for machine metrics and scrape the same using prometheus. Download node metrics exporter from [here](https://prometheus.io/download/#node_exporter)

There are many standard exporters available like node exporter you can find them [here](https://prometheus.io/docs/instrumenting/exporters)

**Run the node exporter in a terminal.**
> ./node_exporter

 [![node_exporter.png](../_resources/0c12eb29fcd431765d94fdf8c8f08f25.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/node_exporter.png)

Next Add node exporter to the list of scrape_configs
*node_exporter.yml*
global: scrape_interval: 15s  scrape_configs:

- job_name: prometheus  static_configs:
- targets: ["localhost:9090"] - job_name: node_exporter  static_configs:
- targets: ["localhost:9100"]

> prometheus --config.file=node_exporter.yml

 [![prometheus2.gif](../_resources/3666c806e7ba56d00021c5f93972a396.gif)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/prometheus2.gif)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='62'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='990' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#types-of-metrics)Types of metrics.

There are four types of metrics which prometheus client libraries support as of May 2020. They are:

1. Counter
2. Gauge
3. Histogram
4. Summary

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='63'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='998' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#counter)Counter:

Counter is a metric value which can only increase or reset i.e the value cannot reduce than the previous value. It can be used for metrics like number of requests, no of errors etc.

> go_gc_duration_seconds_count

 [![counter_example.png](../_resources/956963ae1827cb1fd32d3b889ba1f7ca.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/counter_example.png)

The rate() function takes the history of metrics over a time frame and calculates how fast value is increasing per second. Rate is applicable on counter values only.

> rate(go_gc_duration_seconds_count[5m])

 [![rate_example.png](../_resources/75fd4b6b66e08b3d0975867973d45972.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/rate_example.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1008' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#gauge)Gauge:

Gauge is a number which can either go up or down. It can be used for metrics like number of pods in a cluster, number of events in an queue etc.

> go_memstats_heap_alloc_bytes

 [![gauge_example.png](../_resources/83432b92a1ac9342e7da79bf2e5db462.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/gauge_example.png)

PromQL functions like max_over_time, min_over_time and avg_over_time can be used to query gauge metrics

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='65'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1015' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#histogram)Histogram

Histogram is a little complex metric type when compared to the ones we have seen. Histogram can be used for any calculated value which is counted based on bucket values, the buckets can be configured by the user. It is a cumulative metric and provides sum of all the values by default. This is applicable for metrics like request time, cpu temperature etc

Example: I want to observe the time taken to process api requests. Instead of storing the request time for each request, histogram metric allows us to approximate and store frequency of requests which fall into particular buckets. I define buckets for time taken like 0.3,0.5,0.7,1,1.2. So these are my buckets and once the time taken for a request is calculated I add the count to all the buckets which are higher than the value.

Lets say Request 1 for endpoint “/ping” takes 0.25 s. The count values for the buckets will be.

> /ping

| Bucket | Count |
| --- | --- |
| 0 - 0.3 | 1   |
| 0.3 - 0.5 | 1   |
| 0.5 - 0.7 | 1   |
| 0.7 - 1 | 1   |
| 1 - 1.2 | 1   |
| +Inf | 1   |

Note: +Inf bucket is added by default.

(Since histogram is a cumulative frequency 1 is added to all the buckets which are greater than the value)

Request 2 for endpoint “/ping” takes 0.4s The count values for the buckets will be this.

> /ping

| Bucket | Count |
| --- | --- |
| 0 - 0.3 | 1   |
| 0.3 - 0.5 | 2   |
| 0.5 - 0.7 | 2   |
| 0.7 - 1 | 2   |
| 1 - 1.2 | 2   |
| +Inf | 2   |

Since 0.4 lies in the seconds bucket(0.3-0.5) all the buckets above the calculated values count is increased. Histogram is used to find average and percentile values.

Let's see a histogram metric scraped from prometheus and apply few functions.
> prometheus_http_request_duration_seconds_bucket{handler="/graph"}

 [![histogram_example.png](../_resources/b3a8a8253b4e7a9038b25e8f9ffd2d5f.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/histogram_example.png)

histogram_quantile() function can be used to calculate calculate quantiles from histogram

 [![histogram_quantile_example.png](../_resources/533f6244fb23056a651185dd70f09aed.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/histogram_quantile_example.png)

The graph shows that the 90th percentile is 0.09, To find the histogram_quantile over last 5m you can use the rate() and time frame

> histogram_quantile(0.9, rate(prometheus_http_request_duration_seconds_bucket{handler="/graph"}[5m]))

 [![histogram_rate_example.png](../_resources/098eb110bf69d8e36812432b0e8484f4.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/histogram_rate_example.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='66'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1086' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#summary)Summary

Summary is similar to histogram and calculates quantiles which can be configured, but it is calculated on the application level hence aggregation of metrics from multiple instances of the same process is not possible. It is used when the buckets of a metric is not known beforehand and is highly recommended to use histogram over summary whenever possible. Calculating summary on the application level is also quite expensive and it is not recommended to be used.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='67'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1089' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#short-summary-on-metric-types)Short Summary on Metric Types:

 [![summary_of_metric_types.png](../_resources/69c285ec8f696ecec535665b57d215ce.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/summary_of_metric_types.png)

[Source](https://www.youtube.com/watch?v=nJMRmhbY5hY)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1092' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#create-a-simple-exporter)Create a simple exporter

We will create a request counter metric exporter using golang.
*server.go*

package main import ( "fmt"  "net/http") func  ping(w http.ResponseWriter, req  *http.Request){ fmt.Fprintf(w,"pong")

} func  main() { http.HandleFunc("/ping",ping) http.ListenAndServe(":8090", nil)

}

We have a simple server which when hit on localhost:8090/ping endpoint sends back pong

 [![server.png](../_resources/d8d14def036d84d3937a461db7fc8717.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/server.png)

Now we will add a metric to the server which will instrument the number of requests made to the ping endpoint.

We will use the counter metric type for this as we know the request count doesn’t go down and only increases.

Create a prometheus counter
var  pingCounter  =  prometheus.NewCounter(

prometheus.CounterOpts{ Name: "ping_request_count", Help: "No of request handled by Ping handler",

},
)

Next we update the ping Handler to increase the count of the counter using `pingCounter.Inc()`.

func  ping(w http.ResponseWriter, req  *http.Request) { pingCounter.Inc() fmt.Fprintf(w, "pong")

}
Next we register the counter to the Default Register and expose the metrics.

func  main() { prometheus.MustRegister(pingCounter) http.HandleFunc("/ping", ping) http.Handle("/metrics", promhttp.Handler()) http.ListenAndServe(":8090", nil)

}

The `prometheus.MustRegister` function registers the pingCounter to the default Register. To expose the metrics the golang prometheus client library provides the promhttp package.`promhttp.Handler()` provides a `http.Handler` which exposes the metrics registered in the Default Register.

*serverWithMetric.go*

package main import ( "fmt"  "net/http"  "github.com/prometheus/client_golang/prometheus"  "github.com/prometheus/client_golang/prometheus/promhttp") var  pingCounter  =  prometheus.NewCounter(

prometheus.CounterOpts{ Name: "ping_request_count", Help: "No of request handled by Ping handler",

},

) func  ping(w http.ResponseWriter, req  *http.Request) { pingCounter.Inc() fmt.Fprintf(w, "pong")

} func  main() { prometheus.MustRegister(pingCounter) http.HandleFunc("/ping", ping) http.Handle("/metrics", promhttp.Handler()) http.ListenAndServe(":8090", nil)

}

Now hit the localhost:8090/ping endpoint a couple of times and sending a request to localhost:8090 will provide the metrics.

 [![ping_count.png](../_resources/cbea90e4a0317cbc0bf8f48268504713.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/ping_count.png)

Here the ping_request_count shows that `/ping` endpoint was called 3 times.

The DefaultRegister comes with a collector for go runtime metrics and that is why we see other metrics like go_threads, go_goroutines etc.

We have built our first metric exporter. Let’s update our prometheus config to scrape the metrics from our server.

*simple_server.yml*
global: scrape_interval: 15s  scrape_configs:

- job_name: prometheus  static_configs:
- targets: ["localhost:9090"] - job_name: simple_server  static_configs:
- targets: ["localhost:8090"]

> prometheus --config.file=simple_server.yml

 [![prometheus3.gif](../_resources/b45b3221c32d1017f44907c05619f242.gif)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/prometheus3.gif)

Note:

- Make sure the authentication mechanism used by your application is supported by prometheus
- `promhttp.Handler` gzips the response, If you are using a gzip middleware then you must implement some skipper logic to avoid compressing the response twice.

Now that we have our server with `ping_request_count` metric let's create a visualization dashboard. For this, we will use [Grafana](https://grafana.com/). If you wonder why should one use Grafana when we can create graphs using Prometheus. The answer is that the graph that we use to visualize our queries is used for ad-hoc queries and debugging. Prometheus official docs suggest using Grafana or Console Templates for graphs. [Refer](https://prometheus.io/docs/visualization/browser/)

Console Templates is a way to create graphs using golang templates which I am not covering as it has a learning curve. Grafana is an analytics platform that allows you to query,visualize, and set alerts on your metrics. Comparatively Grafana is easy to use for a beginner.

Install Grafana by following the steps for your operating system from [here](https://grafana.com/docs/grafana/latest/installation/requirements/#supported-operating-systems).

Once Grafana is installed successfully go to [localhost:3000](http://localhost:3000/) and Grafana dashboard should be visible. The default username and password is `admin`.

 [![grafana_login.png](../_resources/e5940ba1af7aa3071b651d86e32c382c.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/grafana_login.png)

Let's add a source to grafana by clicking on the gear icon in the side bar and select Data Sources.

> ⚙>  > Data Sources

 [![grafana_add_source.png](../_resources/932f0bab66b8b5eac836f29a5ce73cc9.png)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/grafana_add_source.png)

If you see Grafana also supports multiple data sources other than Prometheus like graphite, postgreSQL etc.

> Adding Prometheus as Data Source

 [![grafana1.gif](../_resources/7055d052f29eb4c17a58cafa1dc74696.gif)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/grafana1.gif)

Now we have successfully added Prometheus as our data source.
> Creating our first dashboard

 [![grafana2.gif](../_resources/5b1c4f15d4cbf96496c05a1bda5e5b7d.gif)](https://github.com/yolossn/Prometheus-Basics/blob/master/images/grafana2.gif)

Tada  We have created our first dashboard using Grafana.

I hope I did justice to your time and helped you understand the basics of prometheus.

**Where to go from here:**

- It is important to understand PromQL extensively to take advantage of the metrics which one has collected. Remember the goal is not just to collect metrics but to derive answers for application related questions. [This](https://medium.com/@valyala/promql-tutorial-for-beginners-9ab455142085) is a very good resource to get started with PromQL.

To Do

- Integration with grafana to create dashboards
- Add code samples for all metric types.
- Explain about the concept of Service Discovery for integrating with kubernetes.
- Basic Alerting + Prometheus alerts vs Grafana alerts.
- Integrating alerts with tool like pagerduty.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='69'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1285' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/yolossn/Prometheus-Basics#references)References:

- https://prometheus.io/docs/
- https://www.robustperception.io/how-does-a-prometheus-histogram-work
- https://www.robustperception.io/how-does-a-prometheus-summary-work
- https://www.robustperception.io/how-does-a-prometheus-gauge-work
- https://www.robustperception.io/how-does-a-prometheus-counter-work
- https://www.youtube.com/watch?v=nJMRmhbY5hY
- https://godoc.org/github.com/prometheus/client_golang/prometheus