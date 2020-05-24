distributed-echo/README.md at master · mchmarny/distributed-echo

 executable file   103 lines (63 sloc)  3.71 KB

 [Raw](https://github.com/mchmarny/distributed-echo/raw/master/README.md)  [Blame](https://github.com/mchmarny/distributed-echo/blame/master/README.md)  [History](https://github.com/mchmarny/distributed-echo/commits/master/README.md)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-device-desktop js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='70'%3e%3cpath fill-rule='evenodd' d='M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z' data-evernote-id='705' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Open this file in GitHub Desktop](https://github.com/mchmarny/distributed-echo/blob/master/README.mdgithub-mac://openRepo/https://github.com/mchmarny/distributed-echo?branch=master&filepath=README.md)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='73'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='711' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#distributed-echo)distributed-echo

Simple Broadcast/Echo service for Cloud Run designed to demonstrate authenticated inter-service connectivity and measure latency between the different regions where this service is deployed.

[![diagram.png](../_resources/09dc0defe414910b7aa8c2d87796cd11.png)](https://github.com/mchmarny/distributed-echo/blob/master/img/diagram.png)

> The inter-region service invocation latency measurements do not account for the implicit "cold starts" of each service. You can minimize it though by creating more frequent Cloud Scheduler invocations

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='74'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='717' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#pre-requirements)Pre-requirements

If you don't have one already, start by creating new project and configuring your [Google Cloud SDK](https://cloud.google.com/sdk/docs/). Also, if you have not done so already, you will have [set up Cloud Run](https://cloud.google.com/run/docs/setup).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='75'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='720' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#config)Config

All the variables used in this service are defined in the [bin/config](https://github.com/mchmarny/distributed-echo/blob/master/bin/config) file. You can edit these to your preferred values.

- `SERVICE_NAME` (default: `distributed-echo`) is the name of the service deployed into Cloud Run. Combination of this name is also used for database, schedule, and user name.
- `SERVICE_IMAGE_VERSION` (default: `0.5.6`) is the version of the image that will be build to use in Cloud Run deployment
- `SERVICE_REGIONS` (default: `us-central1`, `us-east1`, `europe-west1`, `asia-northeast1`) is all the regions where this service should be deployed to Cloud Run
- `DB_REGION` (default: `regional-us-central1`) is the Spanner instance configuration value which will dictate the deployment regions (alt: `nam3`, `nam-eur-asia1`)
- `DB_NODES` (default: `3`) is the number of Spanner nodes in created in the above defied region (see: https://cloud.google.com/spanner/docs/instances)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='729' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#deployment)Deployment

> Note, to keep this readme short, I will be asking you to execute scripts rather than listing here complete commands. You should review each one of these scripts for content. This will also help you understand the individual commands so you can use them in the future.

First, start by creating IAM user and granting that user all the necessary roles.

bin/setup
Next, setup the Spanner instance and a DB
bin/db

With IAM account created and Spanner DB configured, the only thing that we are missing is the container image. You can build that image using the [bin/image](https://github.com/mchmarny/distributed-echo/blob/master/bin/image) script:

bin/image

With the image built, you can now deploy the Cloud Run service to all the regions defined in the [bin/config](https://github.com/mchmarny/distributed-echo/blob/master/bin/config) using using [bin/deploy](https://github.com/mchmarny/distributed-echo/blob/master/bin/deploy) script:

bin/deploy

Finally, use the [bin/schedule](https://github.com/mchmarny/distributed-echo/blob/master/bin/schedule) script to crate one Cloud Schedule "cron" per each service

bin/schedule

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='77'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='743' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#metrics)Metrics

You can monitor the metrics created by this service in one of two ways:

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='78'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='746' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#sql-query-spanner-database)SQL Query Spanner Database

The schema of the Spanner DB holding the metrics from this service is defined in the [bin/db](https://github.com/mchmarny/distributed-echo/blob/master/bin/db):

CREATE  TABLE  pings (
id STRING(MAX) NOT NULL,
target STRING(MAX) NOT NULL,
source STRING(MAX) NOT NULL,
sent TIMESTAMP  NOT NULL,
completed TIMESTAMP  NOT NULL,
duration INT64 NOT NULL) PRIMARY KEY (id)
You can query it using SQL

[![db.png](../_resources/f2b5ef846d6a663a6991e01c03b649a8.png)](https://github.com/mchmarny/distributed-echo/blob/master/img/db.png)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='79'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='752' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#stackdriver-time-series)Stackdriver Time Series

This service also records each "echo" ping in Stackdriver as a custom time series metric (`custom.googleapis.com/metric/echo-latency`)

[![metric.png](../_resources/99c27777495989352eda48230bec00d4.png)](https://github.com/mchmarny/distributed-echo/blob/master/img/metric.png)

You can group that series by the `source` and `target` labels to get a detail chart of the latency in between regions

[![chart.png](../_resources/0b64ebd969784f2dac916af90a80ec6a.png)](https://github.com/mchmarny/distributed-echo/blob/master/img/chart.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='80'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='758' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#cleanup)Cleanup

To cleanup all resources created by this sample execute
bin/cleanup

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='81'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='762' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/mchmarny/distributed-echo/blob/master/README.md#disclaimer)Disclaimer

This is my personal project and it does not represent my employer. I take no responsibility for issues caused by this code. I do my best to ensure that everything works, but if something goes wrong, my apologies is all you will get.