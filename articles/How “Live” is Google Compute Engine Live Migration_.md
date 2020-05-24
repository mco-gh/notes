How “Live” is Google Compute Engine Live Migration?

# How “Live” is Google Compute Engine Live Migration?

Google Compute Engine offers a really unique technology called “Live Migration” which keeps your instances running even when a host undergo downtime such as during software or hardware update. Google Compute Engine migrates your running instance to another physical host in the same network zone rather than requiring your instances to be rebooted.

Live Migration helps Google to perform maintenance which is integral to keeping infrastructure protected and reliable without interrupting any of your instances. The Live Migration is a very cool feature, and Google claims that:

*> “your instance might experience a short period of decreased performance, although generally, most instances should not notice any difference.*> ”

Naturally, we wanted to test this claim ;-) Fortunately, you can easily simulate a maintenance event on an instance by using either the *gcloud* command-line tool or an API call, i.e.

`gcloud beta compute instances simulate-maintenance-event [INSTANCE_NAME] \[[NEWLINE]]    --zone [ZONE]`

OR

`POST https://www.googleapis.com/compute/beta/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]/simulateMaintenanceEvent`

To make our test more real-life, we have decided to generate some load on our test instance and then to initiate a Live Migration event and see how it effects our instance.

Using [Cloud Launcher](https://cloud.google.com/launcher/), we created a n1-standard-1 machine running nginx (by Bitnami). For load generation, we have decided to use [K6](https://k6.io/) — developer centric open source load testing tool written in Go. We have opted to store test results with InfluxDB and visualize them with Grafana.

Here is our script:

![](../_resources/8182467ba82056bd65b42f571f900f66.png)
To start generating the load, we ran K6 as following:

k6 run — out influxdb=[http://x.x.x.x:8086/myk6db](http://10.128.0.10:8086/myk6db) — vus 50 — duration 10m — rps 6000 test.js

After about 60 seconds we started the maintenance event simulation.

![](../_resources/8bb93892d6e718bed8c5bcdafd7fa358.png)

![](../_resources/1ff3102f17d0a0c6526e0db992412477.png)

As you can see, during a period of about 2 seconds, the response time was significantly higher and our instance did not handle any requests at that time. However, there are no errors and the client has been served during the migration.

We have repeated the same test on a bigger instance (n1-standard-4):

![](../_resources/21c7578d01df7f3d0fb7e15d7f0343f8.png)

![](../_resources/4cf1e4f349a204e5ea9444e50fecde73.png)

Finally, another test on even larger instance serving 10k requests per second (comparing to the 6k in previous tests).

![](../_resources/90313e91801546b3d9230b8f670f41a1.png)

![](../_resources/c5618d05d2eec66647e48f1a47f17d99.png)

As you can see from the charts, the behavior stays consistent across workloads and instances of different types. You can expect about 2s during which your instance will not respond during the live migration, however no connections will be dropped and we id not observed any errors during our tests.

Live Migration is a cool and unique feature in the public cloud and it’s the default option when creating a instances in Google Compute Engine, and now you can test how your app will behave during live migration.

Want more stories? Check our blog on [Medium](http://blog.doit-intl.com/), or [follow Aviv on Twitter](https://twitter.com/avivl).