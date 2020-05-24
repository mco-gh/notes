Making Sense of the Metadata: Clustering 4,000 Stack Overflow tags with BigQuery k-means - Stack Overflow Blog

# Making Sense of the Metadata: Clustering 4,000 Stack Overflow tags with BigQuery k-means

[![4cfd811c2c01646a1e4f33fb9e68ab5c](../_resources/a756532542c16a1e852005e8a3bd8163.jpg)](https://stackoverflow.blog/authors/fhoffa/)[(L)](https://stackoverflow.blog/authors/fhoffa/)by [Felipe Hoffa](https://stackoverflow.blog/authors/fhoffa/) on July 24, 2019

 AddThis Sharing Buttons

[Share to Twitter![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-twitter-1' class='at-icon at-icon-twitter js-evernote-checked' style='fill: rgb(255%2c 255%2c 255)%3b width: 16px%3b height: 16px%3b' data-evernote-id='429'%3e%3ctitle id='at-svg-twitter-1' data-evernote-id='430' class='js-evernote-checked'%3eTwitter%3c/title%3e%3cg data-evernote-id='431' class='js-evernote-checked'%3e%3cpath d='M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336' fill-rule='evenodd' data-evernote-id='432' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to LinkedIn![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-linkedin-2' class='at-icon at-icon-linkedin js-evernote-checked' style='fill: rgb(255%2c 255%2c 255)%3b width: 16px%3b height: 16px%3b' data-evernote-id='436'%3e%3ctitle id='at-svg-linkedin-2' data-evernote-id='437' class='js-evernote-checked'%3eLinkedIn%3c/title%3e%3cg data-evernote-id='438' class='js-evernote-checked'%3e%3cpath d='M26 25.963h-4.185v-6.55c0-1.56-.027-3.57-2.175-3.57-2.18 0-2.51 1.7-2.51 3.46v6.66h-4.182V12.495h4.012v1.84h.058c.558-1.058 1.924-2.174 3.96-2.174 4.24 0 5.022 2.79 5.022 6.417v7.386zM8.23 10.655a2.426 2.426 0 0 1 0-4.855 2.427 2.427 0 0 1 0 4.855zm-2.098 1.84h4.19v13.468h-4.19V12.495z' fill-rule='evenodd' data-evernote-id='439' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to Facebook![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-facebook-3' class='at-icon at-icon-facebook js-evernote-checked' style='fill: rgb(255%2c 255%2c 255)%3b width: 16px%3b height: 16px%3b' data-evernote-id='443'%3e%3ctitle id='at-svg-facebook-3' data-evernote-id='444' class='js-evernote-checked'%3eFacebook%3c/title%3e%3cg data-evernote-id='445' class='js-evernote-checked'%3e%3cpath d='M22 5.16c-.406-.054-1.806-.16-3.43-.16-3.4 0-5.733 1.825-5.733 5.17v2.882H9v3.913h3.837V27h4.604V16.965h3.823l.587-3.913h-4.41v-2.5c0-1.123.347-1.903 2.198-1.903H22V5.16z' fill-rule='evenodd' data-evernote-id='446' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)33]()

![1*pSI04ezVMO279Tcmsuh7_A.png](../_resources/dd3cd439f5d7df6233236d3929a0e83e.png)

#### *How would you group more than 4,000 active Stack Overflow tags into meaningful groups? This is a perfect task for unsupervised learning and k-means clustering — and now you can do all this inside BigQuery. Let’s find out how.*

![1*pSI04ezVMO279Tcmsuh7_A.png](../_resources/dd3cd439f5d7df6233236d3929a0e83e.png)
Visualizing a universe of clustered tags.

[*Felipe Hoffa*](https://twitter.com/felipehoffa)* is a Developer Advocate for Google Cloud. In this post he works with *[*BigQuery*](http://cloud.google.com/bigquery)* – Google’s serverless data warehouse – to run k-means clustering over Stack Overflow’s published dataset, which is refreshed and uploaded to Google’s Cloud once a quarter. You can check out more about working with Stack Overflow data and BigQuery *[*here*](https://stackoverflow.blog/2016/12/15/you-can-now-play-with-stack-overflow-data-on-googles-bigquery/)* and *[*here*](https://towardsdatascience.com/bigquery-without-a-credit-card-discover-learn-and-share-199e08d4a064)*.*

## 4,000+ tags are a lot

These are the most active Stack Overflow tags since 2018 — they’re a lot. In this picture I only have 240 tags — how would you group and categorize 4,000+ of them?

# Tags with >180 questions since 2018

SELECT tag, COUNT(*) questions
FROM `fh-bigquery.stackoverflow_archive.201906_posts_questions`,
UNNEST(SPLIT(tags, '|')) tag
WHERE creation_date > '2018-01-01'
GROUP BY 1
HAVING questions>180
ORDER BY 2 DESC
![1*_p3SSvQnpVneA5kcFlHlEw.png](../_resources/c0d1455aa60ebfe8f34c5635f35d7518.png)
Top Stack Overflow tags by number of questions.

## Hint: Co-occurring tags

Let’s find tags that usually go together:
![image-768x332.png](../_resources/cf201250131f36dec5a70515ce1599e0.png)
Co-occurring tags on Stack Overflow questions
These groupings make sense:

- ‘javascript’ is related to ‘html’.
- ‘python’ is related to ‘pandas’.
- ‘c#’ is related to ‘.net’.
- ‘typescript’ is related to ‘angular’.
- etc…

So I’ll take these relationships and I’ll save them on an auxiliary table — plus a percentage of how frequently a relationship happens for each tag.

CREATE OR REPLACE TABLE `deleting.stack_overflow_tag_co_ocurrence`
AS
WITH data AS (
SELECT * FROM `fh-bigquery.stackoverflow_archive.201906_posts_questions`
WHERE creation_date > '2018-01-01'
), active_tags AS (
SELECT tag, COUNT(*) c
FROM data, UNNEST(SPLIT(tags, '|')) tag
GROUP BY 1
HAVING c>180
)
SELECT *, questions/questions_tag1 percent
FROM (
SELECT *, MAX(questions) OVER(PARTITION BY tag1) questions_tag1
FROM (
SELECT tag1, tag2, COUNT(*) questions
FROM data, UNNEST(SPLIT(tags, '|')) tag1, UNNEST(SPLIT(tags, '|')) tag2
WHERE tag1 IN (SELECT tag FROM active_tags)
AND tag2 IN (SELECT tag FROM active_tags)
GROUP BY 1,2
HAVING questions>30
)
)
![1*gWKNh4zxGmgLLInwsly2Dg.png](../_resources/7d57a6cd9628a9c3ab9740a270950d10.png)

# One-hot encoding

Now get ready for some SQL magic. BigQuery ML does a good job of hot-encoding strings, but it doesn’t handle arrays as I wish it did (stay tuned). So I’m going to create a string first that will define all the columns where I want to find co-occurrence. Then I can use that string to get a huge table, with a 1 for every time a tag co-occurs with the main one at least certain % of time. Let’s see first a subset of these results:

![image-1.png](../_resources/fffec84a35dfc2ce3dec3017c56d8589.png)
What you see here is a co-occurrence matrix:

- ‘javascript’ shows a relation to ‘php’, ‘html’, ‘css’, ‘node.js’, and ‘jquery’.
- ‘android’ shows a relation to ‘java’.
- ‘machine-learning’ shows a relation to ‘python’, but not the other way around.
- ‘multi-threading’ shows a relation to ‘python’, ‘java’, ‘c#’, and ‘android`
- ‘unit-testing’ a relation to almost every column here, except to ‘php’, ‘html’, ‘css’, and ‘jquery’.

You can reduce or augment the sensibility of these relations with the percent threshold:

SELECT tag1 ,IFNULL(ANY_VALUE(IF(tag2='javascript',1,null)),0) Xjavascript
,IFNULL(ANY_VALUE(IF(tag2='python',1,null)),0 ) Xpython
,IFNULL(ANY_VALUE(IF(tag2='java',1,null)),0) Xjava
,IFNULL(ANY_VALUE(IF(tag2='c#',1,null)),0) XcH
,IFNULL(ANY_VALUE(IF(tag2='android',1,null)),0) Xandroid
,IFNULL(ANY_VALUE(IF(tag2='php',1,null)),0) Xphp
,IFNULL(ANY_VALUE(IF(tag2='html',1,null)),0) Xhtml
,IFNULL(ANY_VALUE(IF(tag2='css',1,null)),0) Xcss
,IFNULL(ANY_VALUE(IF(tag2='node.js',1,null)),0) XnodeDjs
,IFNULL(ANY_VALUE(IF(tag2='jquery',1,null)),0) Xjquery
,SUM(questions) questions_tag1
FROM `deleting.stack_overflow_tag_co_ocurrence`
WHERE percent>0.03
GROUP BY tag1
ORDER BY questions_tag1 DESC LIMIT 100

## K-means clustering time

Now — instead of using this small table, let’s use the whole table to compute k-means with BigQuery.

With this line, I’m creating a one-hot encoding string that I can use later to define the 4,000+ columns I’ll use for k-means:

one_hot_big = client.query("""
SELECT STRING_AGG(

FORMAT("IFNULL(ANY_VALUE(IF(tag2='%s',1,null)),0)X%s", tag2, REPLACE(REPLACE(REPLACE(REPLACE(tag2,'-','_'),'.','D'),'#','H'),'+','P'))

) one_hot
FROM (
SELECT tag2, SUM(questions) questions
FROM `deleting.stack_overflow_tag_co_ocurrence`
GROUP BY tag2

# ORDER BY questions DESC

# LIMIT 10

)
""").to_dataframe().iloc[0]['one_hot']
And training a k-means model in BigQuery is really easy:
CREATE MODEL `deleting.kmeans_tagsubtag_50_big_a_01`
OPTIONS ( model_type='kmeans',
distance_type='COSINE',
num_clusters=50 )
AS
WITH tag_and_subtags AS (
SELECT tag1, %s
FROM `deleting.stack_overflow_tag_co_ocurrence`
WHERE percent>0.03
GROUP BY tag1
)
SELECT * EXCEPT(tag1) FROM tag_and_subtags
Now we wait — while BigQuery shows us the progress of our training:
![1*PJw22Qw-QyXU6WBNKZsLNg.png](../_resources/9155fdab7291e215e6eaacaa03082ced.png)
And when it’s done, we even get an evaluation of our model:

[Davies–Bouldin index](https://en.wikipedia.org/wiki/Davies%E2%80%93Bouldin_index?source=post_page---------------------------): 1.8530

[Mean squared distance](https://cloud.google.com/bigquery/docs/reference/rest/v2/models?source=post_page---------------------------#clusteringmetrics): 0.8174

## Performance note

Do we really need 4,000 one-hot encoded dimensions to obtain better clusters? Turns out that 500 are enough — and I like the results better. It also reduces the time for training the model in BigQuery from 24 minutes to 3. The same with only 30 dimensions lowers the time to 90 seconds — but I like the results better with 500. More on hyper-parameter tuning below.

![1*t-70lqtT8Oho-9x1k3QMiQ.png](../_resources/07683596a0e68207db30c5d33c0b0fe4.png)

500 one-hot encoded dimensions reduces time per iteration to 30 seconds, and a lower loss.

[Davies–Bouldin index](https://en.wikipedia.org/wiki/Davies%E2%80%93Bouldin_index?source=post_page---------------------------): 1.6910

[Mean squared distance](https://cloud.google.com/bigquery/docs/reference/rest/v2/models?source=post_page---------------------------#clusteringmetrics): 0.52332

## Get ready for the results: The 50 clusters are…

Now it’s time to see our results. I’ll even look out for some tags I’m interested in: How are `google`, `amazon`, and `azure` represented in each cluster?

These are the 50 groups that k-means clustering found — given the 1-hot encoding of related tags we did earlier in this post. Some results make a lot of sense — while others give great insight into what are the prevalent surrounding technologies to any Stack Overflow tag.

Naming each centroid is always a challenge. Here I used the top 5 centroid weight vectors — see how below.

**centroid 45: amazon-web-services, aws-lambda, amazon-s3, amazon-ec2, python**
—–

amazon-web-services, amazon-s3, aws-lambda, amazon-ec2, amazon-dynamodb, terraform, aws-sdk, amazon-cloudformation, amazon-redshift, aws-api-gateway, amazon-cognito, boto3, cloud, alexa, amazon-rds, amazon-elastic-beanstalk, amazon-ecs, alexa-skills-kit, amazon-cloudfront, serverless, aws-cli, amazon-iam, amazon-cloudwatch, elastic-beanstalk, amazon-sqs, serverless-framework, amazon-athena, aws-amplify, aws-appsync, amazon-sns, alexa-skill, amazon-route53, amazon, amazon-kinesis, amazon-sagemaker, autoscaling, amazon-elb, amazon-ses, aws-cognito, aws-iot, terraform-provider-aws, api-gateway, amazon-vpc, aws-serverless, aws-codepipeline, aws-codebuild, amazon-rds-aurora, bitnami, amazon-lex, aws-step-functions, aws-code-deploy, aws-iam, aws-fargate, dynamodb-queries, boto

amazon: amazon-cognito, amazon-ses, amazon-redshift, aws-lambda, amazon-ecs, amazon-s3, amazon-web-services, amazon-athena, aws-api-gateway, amazon-rds, amazon, amazon-cloudfront, amazon-lex, aws-iot, amazon-elb, aws-code-deploy, amazon-cloudwatch, aws-cli

**centroid 17: android, java, android-layout, android-recyclerview, kotlin
**—–

android, json, xml, kotlin, android-studio, android-recyclerview, android-layout, android-fragments, xslt, serialization, android-intent, retrofit2, android-activity, android-room, nullpointerexception, retrofit, gson, android-volley, textview, android-viewpager, xml-parsing, recycler-adapter, android-edittext, android-sqlite, protocol-buffers, xsd, deserialization, android-constraintlayout, android-asynctask, fragment, android-architecture-components, android-livedata, imageview, scrollview, android-databinding, android-glide, android-animation, xquery, xslt-1.0, android-jetpack, android-manifest, navigation-drawer, adapter, bottomnavigationview, xslt-2.0, android-toolbar, onclicklistener, android-tablayout, android-cardview, android-spinner, android-adapter, picasso, android-linearlayout, transformation, android-drawable, android-architecture-navigation, android-imageview, android-custom-view, json-deserialization, android-view, android-actionbar, searchview, biztalk, android-coordinatorlayout, android-lifecycle, android-softkeyboard, floating-action-button, recyclerview-layout, swipe, android-relativelayout, android-xml, android-collapsingtoolbarlayout, android-button, android-scrollview, saxon, android-nestedscrollview, android-styles, xml-namespaces, xsl-fo, android-fragmentactivity, android-dialogfragment, android-viewholder, xml-serialization

**centroid 7: android, java, javascript, ios, python
**—–

android-gradle, bluetooth, rx-java2, build.gradle, dependencies, rx-java, google-play, sdk, android-ndk, corda, video-streaming, android-emulator, libgdx, android-webview, apk, location, java-native-interface, google-play-services, dagger-2, adb, codenameone, android-8.0-oreo, google-places-api, android-notifications, android-studio-3.0, broadcastreceiver, speech-recognition, arcore, sharedpreferences, streaming, gps, android-service, version, coordinates, androidx, native, sms, here-api, android-camera, android-permissions, uri, android-mediaplayer, locale, vert.x, exoplayer, google-maps-markers, settings, alarmmanager, spinner, proguard, okhttp3, text-to-speech, okhttp, updates, android-camera2, android-source, whatsapp, nfc, share, inputstream, google-fabric, xmpp, calculator, manifest, wifi, mpandroidchart, android-9.0-pie, rx-android, call, android-workmanager, mp4, hls, video-processing, release, barcode, android-support-library, alertdialog, android-viewmodel, dji-sdk, barcode-scanner, filepath, sip, google-cloud-messaging, gradle-plugin, android-arrayadapter, screen, payment, toolbar, google-play-console, dagger, mp3, indexoutofboundsexception, ejabberd, httpurlconnection, libraries, android-proguard, coroutine, h.264, simpledateformat, jacoco, background-process, rtsp, offline, root, sensor, splash-screen, android-bluetooth, android-testing, android-resources, android-tv, emulation, android-bitmap, android-listview, multipart, chromecast, android-broadcastreceiver, video-capture, google-maps-android-api-2, pojo, android-canvas, visibility, broadcast, google-play-games, dao, kotlin-android-extensions, avd, lint, android-jobscheduler, android-library, kotlinx.coroutines, firebase-mlkit, expandablelistview, obfuscation, android-contentprovider, appcelerator, mvp, live-streaming, in-app-billing, android-context, audio-streaming, arabic, android-alertdialog, kotlin-coroutines, zxing, android-videoview, fingerprint, braintree, audio-recording, deprecated, job-scheduling, android-wifi, wear-os, bottom-sheet, android-things, device, marker, right-to-left, google-login, mobile-application, media-player, countdowntimer, opengl-es-2.0, nullable, face-detection, exoplayer2.x, android-8.1-oreo, beacon, drawable, gradlew, mapbox-android, classnotfoundexception, parcelable, android-keystore, voice-recognition, toast, aar, google-places, android-theme, android-progressbar, paging, accelerometer, playback, gradle-kotlin-dsl, samsung-mobile, photo, ibeacon, android-appcompat, noclassdeffounderror, branch.io, rtmp, sceneform, foreground-service, google-cast, appcelerator-titanium, android-widget, logcat, android-pendingintent, android-fileprovider, android-gps, sha1, jodatime, android-sensors, android-appbarlayout, surfaceview, mpeg-dash, android-mvvm

google: google-maps-android-api-2, google-play-services, google-fabric, google-places, google-places-api, google-play-console, google-cast, google-login, google-maps-markers, google-play-games, google-play, google-cloud-messaging

**centroid 28: angular, typescript, javascript, angular6, angular5
**—–

angular, typescript, angular6, angular5, rxjs, angular-material, angular7, service, observable, routing, angular-cli, components, angular-reactive-forms, karma-jasmine, primeng, ag-grid, angularfire2, angular-material2, ngrx, reactive-programming, httpclient, angular-ui-router, angular-routing, lazy-loading, rxjs6, ngfor, angular-forms, angular-httpclient, angular2-routing, angular-components, angular-router, rx-swift, ng-bootstrap, angular2-forms, angular-universal, angular2-template, angular-services, angular-directive, material, angular4-forms, ngx-bootstrap, typescript2.0, angular2-services, ngrx-store, subscription, rxjs5, angular2-directives, ngrx-effects, angular-material-6, angular-cli-v6, angular-http-interceptors, redux-observable, subscribe, angular-pipe, angular-promise, angular2-observables, reactivex, angular-ngmodel, angular-cdk, tsconfig

**centroid 20: apache-spark, java, scala, hadoop, python
**—–

apache-spark, scala, pyspark, apache-kafka, hadoop, apache-spark-sql, hive, cassandra, apache-flink, jupyter, hdfs, bigdata, playframework, spark-streaming, sbt, apache-nifi, hiveql, apache-kafka-streams, akka, hbase, pyspark-sql, mapreduce, kafka-consumer-api, rdd, spark-dataframe, amazon-emr, yarn, user-defined-functions, parquet, cassandra-3.0, cluster-computing, avro, databricks, apache-kafka-connect, aws-glue, spark-structured-streaming, flink-streaming, kerberos, apache-zookeeper, sqoop, confluent, presto, kafka-producer-api, impala, akka-stream, hadoop2, apache-spark-mllib, traits, apache-zeppelin, cloudera, datastax, apache-storm, distributed-computing, akka-http, data-modeling, apache-spark-dataset, guice, google-cloud-dataproc, gatling, jmx, hortonworks-data-platform, apache-pig, apache-spark-ml, oozie, azure-databricks, scalatest, cql, playframework-2.6, datastax-enterprise, phoenix, confluent-schema-registry, mesos, implicit, implicit-conversion, ksql, scala-collections, spark-submit, hdinsight, ambari

google: google-cloud-dataproc
amazon: amazon-emr, aws-glue
azure: azure-databricks
**centroid 12: bash, python, linux, shell, java
**—–

macos, ubuntu, ansible, ssh, raspberry-pi, terminal, vim, raspberry-pi3, subprocess, environment-variables, centos, console, command-line-interface, pipe, arguments, jq, homebrew, iot, applescript, printf, escaping, sftp, windows-subsystem-for-linux, raspbian, exec, redhat, stdout, zsh, alias, wget, eval, paramiko, filenames, glob, command-line-arguments, stdin, remote-access, sudo, file-permissions, slurm, putty, gpio, tar, tmux, rsync, expect, ksh, jsch, scp, ssh-tunnel, cat, portforwarding, openssh

**centroid 8: c#, .net, asp.net-core, .net-core, java
**—–

logging, exception, error-handling, azure-functions, reflection, configuration, azure-cosmosdb, f#, logstash, exception-handling, azure-web-sites, elastic-stack, azure-service-fabric, console-application, try-catch, wix, azure-application-insights, nunit, core, autofac, xunit, dapper, nest, nhibernate, dotnet-httpclient, nlog, httpwebrequest, serilog, log4net, inversion-of-control, identity, unity-container, webclient, blazor, .net-standard-2.0, system.reactive, clr, type-inference, asp.net-core-signalr, asp.net-core-identity, app-config, masstransit, fluentd, google-cloud-stackdriver, winston, .net-framework-version, ninject, .net-core-2.0, claims-based-identity, syslog, kestrel-http-server

google: google-cloud-stackdriver

azure: azure-cosmosdb, azure-web-sites, azure-functions, azure-application-insights, azure-service-fabric

**centroid 18: c#, asp.net, asp.net-mvc, asp.net-core, entity-framework
**—–

c#, asp.net, .net, asp.net-mvc, asp.net-core, .net-core, entity-framework, linq, asp.net-web-api, model-view-controller, iis, entity-framework-core, dependency-injection, razor, asp.net-core-2.0, asp.net-core-mvc, wcf, entity-framework-6, json.net, kendo-ui, asp.net-core-webapi, webforms, asp.net-mvc-5, identityserver4, asp.net-identity, asp.net-web-api2, asp.net-core-2.1, asp.net-mvc-4, signalr, odata, kendo-grid, automapper, c#-4.0, web-config, razor-pages, windows-services, moq, ado.net, aspnetboilerplate, ef-code-first, ef-core-2.0, asp.net-core-2.2, linq-to-sql, asp-classic, umbraco, ef-core-2.1, asp.net-ajax, ef-migrations, iis-8, connection-string, windows-authentication, linq-to-entities, repository-pattern, swashbuckle, npgsql, iis-7, dbcontext, hangfire, iis-10, iis-express, model-binding, ef-core-2.2, windows-server-2012, signalr-hub, iis-7.5, linq-to-xml

**centroid 10: c#, azure, python, java, javascript
**—–

azure, botframework, azure-sql-database, bots, azure-storage, chatbot, timeout, azure-storage-blobs, report, ssrs-2012, azure-data-factory, telegram-bot, azure-web-app-service, expression, azure-logic-apps, ibm-watson, refactoring, domain-driven-design, azureservicebus, gzip, azure-resource-manager, azure-iot-hub, twilio-api, azure-data-factory-2, azure-data-lake, vpn, azure-virtual-machine, microsoft-teams, luis, string-formatting, game-physics, google-assistant-sdk, ssrs-2008, game-development, ads, mesh, windows-7, virtual-reality, vuforia, microsoft-cognitive, azure-webjobs, azure-keyvault, azure-api-management, credentials, directx, facebook-messenger, collision-detection, arm-template, sprite, rdlc, game-engine, azure-search, azure-eventhub, physics, azure-blob-storage, desktop-application, factory, software-design, hololens, u-sql, installer, collision, azure-cli, reporting, google-home, azure-table-storage, azure-cognitive-services, unityscript, startup, azure-bot-service, mysql-connector, ienumerable, qnamaker, instantiation, builder, ssrs-tablix, azure-cosmosdb-sqlapi, azure-stream-analytics, quaternions, reportviewer, skype, azure-machine-learning-studio, azure-servicebus-queues, skype-for-business, ssrs-2008-r2, azure-virtual-network, win-universal-app, azure-log-analytics, unity5, csom, dialogflow-fulfillment

google: google-assistant-sdk, google-home

azure: azure-webjobs, azure-log-analytics, azure-virtual-machine, azure-sql-database, azure-api-management, azure-iot-hub, azure-web-app-service, azure-data-factory-2, azure-table-storage, azure-servicebus-queues, azure-bot-service, azure-virtual-network, azure-data-factory, azure-cognitive-services, azure-blob-storage, azure-storage-blobs, azure-logic-apps, azure-resource-manager

**centroid 44: c#, javascript, java, oauth-2.0, php
**—–

api, authentication, security, facebook, oauth-2.0, spring-security, cookies, jwt, azure-active-directory, cors, postman, microsoft-graph, login, oauth, microservices, active-directory, ldap, jhipster, authorization, passport.js, keycloak, token, azure-ad-b2c, single-sign-on, passwords, sharepoint-online, telegram, spring-security-oauth2, single-page-application, linkedin, google-signin, openid-connect, session-cookies, owin, csrf, auth0, google-oauth2, saml, access-token, linkedin-api, laravel-passport, saml-2.0, google-authentication, xss, azure-powershell, adal, basic-authentication, azure-ad-graph-api, session-variables, msal, oidc, openid, express-session, bearer-token, logout, refresh-token

google: google-authentication, google-signin, google-oauth2

azure: azure-ad-graph-api, azure-active-directory, azure-powershell, azure-ad-b2c

**centroid 19: c#, visual-studio, visual-studio-2017, .net, xamarin.forms
**—–

visual-studio, xamarin, xamarin.forms, visual-studio-2017, xaml, uwp, azure-devops, xamarin.android, build, reporting-services, tfs, ssis, xamarin.ios, nuget, visual-studio-2015, msbuild, crystal-reports, windows-installer, nuget-package, mono, cross-platform, azure-pipelines-release-pipeline, .net-standard, mvvmcross, visual-studio-2019, visual-studio-2010, c++-cli, visual-studio-2013, sql-server-data-tools, roslyn, resharper, publish, mstest, .net-assembly, visual-studio-2012, azure-devops-rest-api, tfs2017, azure-pipelines-build-task, visual-studio-mac, tfs2018, tfsbuild, visual-studio-extensions, visual-studio-debugging, visual-studio-app-center, csproj, tfs2015, vsix, azure-mobile-services, picker, tfvc, xamarin.uwp

azure: azure-devops, azure-devops-rest-api, azure-pipelines-release-pipeline, azure-mobile-services, azure-pipelines-build-task

**centroid 36: c#, wpf, winforms, javascript, vb.net
**—–

wpf, vb.net, winforms, user-interface, listview, charts, events, mvvm, datatable, checkbox, data-binding, datagridview, timer, sapui5, gridview, combobox, binding, drag-and-drop, menu, datagrid, knockout.js, popup, window, textbox, styles, treeview, listbox, telerik, uwp-xaml, devexpress, resources, vb6, user-controls, prism, viewmodel, controls, datetimepicker, webbrowser-control, cefsharp, panel, contextmenu, windows-10-universal, wpfdatagrid, windows-forms-designer, custom-controls, wpf-controls, richtextbox, clickonce, observablecollection, picturebox, mvvm-light, gdi+, menuitem, backgroundworker

**centroid 2: c++, c, python, linux, java
**—–

c++, c, c++11, templates, assembly, cmake, gcc, memory, opengl, arduino, makefile, visual-c++, boost, c++17, lua, compiler-errors, x86, linux-kernel, memory-management, compilation, memory-leaks, operating-system, io, c++14, fortran, arm, serial-port, cuda, char, language-lawyer, segmentation-fault, clang, linker, stack, gdb, garbage-collection, macros, stl, g++, kernel, embedded, byte, malloc, shared-libraries, out-of-memory, nodes, processing, usb, x86-64, stm32, double, cython, buffer, pthreads, mips, signals, operator-overloading, runtime, gtk, llvm, driver, include, opengl-es, cygwin, operators, bit-manipulation, structure, overloading, nasm, precision, gnu-make, ros, gstreamer, mingw, const, variadic-templates, eigen, heap, gtk3, embedded-linux, esp8266, linux-device-driver, compiler-construction, warnings, cpu, cross-compiling, clion, qt-creator, profiling, ctypes, std, codeblocks, intel, return-value, system, newline, sdl-2, microcontroller, system-calls, pass-by-reference, valgrind, boost-asio, reverse-engineering, dynamic-memory-allocation, move, linker-errors, googletest, c-preprocessor, heap-memory, static-libraries, function-pointers, sdl, template-meta-programming, benchmarking, arduino-uno, libcurl, interrupt, vtk, x86-16, compiler-optimization, constants, stdvector, 64-bit, binaryfiles, bit, swig, quicksort, shared-memory, eclipse-cdt, constexpr, primes, bitwise-operators, x11, shared-ptr, clang++, glfw, binary-search, header-files, singly-linked-list, arduino-esp8266, ld, i2c, main, multiple-inheritance, gnu, smart-pointers, ram, simd, declaration, esp32, preprocessor, elf, undefined-behavior, bison, qtquick2, sfinae, variadic-functions, mingw-w64, unique-ptr, avr, masm, free, typedef, doubly-linked-list, generic-programming, compiler-warnings, glibc, kernel-module, move-semantics, auto, bootloader, c-strings, inline-assembly, ncurses, mmap, stdmap, glm-math, qmake, bit-shift, endianness, cpu-registers, template-specialization, pid, operator-precedence, memory-address

google: googletest
**centroid 24: css, html, javascript, bootstrap-4, angular
**—–

html, css, jquery, html5, css3, bootstrap-4, twitter-bootstrap, flexbox, sass, datatables, highcharts, html-table, twitter-bootstrap-3, layout, frontend, datepicker, drop-down-menu, css-grid, bootstrap-modal, momentjs, responsive-design, modal-dialog, dropdown, grid, responsive, tabs, font-awesome, navbar, carousel, media-queries, themes, tooltip, alignment, overflow, less, css-position, react-bootstrap, border, accordion, dt, css-transforms, angular-ui-bootstrap, nav, z-index, grid-layout, utc, reactstrap, vertical-alignment, pseudo-element, linear-gradients, mixins, collapse, popover, angular-datatables, angular-flex-layout, centering

**centroid 31: delphi, c++, c#, winapi, windows
**—–

delphi, winapi, dll, mfc, com, firemonkey, firebird, c++builder, delphi-10.2-tokyo, pinvoke, pascal, indy

**centroid 25: django, python, django-models, django-rest-framework, python-3.x
**—–

django, django-models, django-rest-framework, django-views, django-forms, django-templates, django-admin, django-queryset, django-orm, django-urls, django-2.0, django-serializer, django-allauth, django-filter, django-class-based-views, django-migrations, serializer

**centroid 34: docker, kubernetes, python, google-cloud-platform, java
**—–

docker, go, kubernetes, elasticsearch, google-cloud-platform, docker-compose, google-app-engine, dockerfile, deployment, rabbitmq, google-cloud-storage, yaml, airflow, google-kubernetes-engine, containers, kibana, google-compute-engine, google-cloud-dataflow, drupal, virtual-machine, apache-beam, openshift, prometheus, ibm-cloud, grpc, docker-swarm, kubernetes-helm, grafana, gcloud, traefik, google-cloud-datastore, kubectl, load-balancing, google-cloud-sql, kubernetes-ingress, monitoring, google-cloud-pubsub, istio, minikube, nginx-reverse-proxy, speech-to-text, alpine, docker-machine, filebeat, google-translate, google-speech-api, iptables, stackdriver, docker-volume, docker-container, azure-aks, nginx-ingress, daemon, google-cloud-vision, google-vision, azure-kubernetes, google-cloud-composer, openshift-origin, kubeadm, dataflow, amazon-eks, service-accounts, rancher, docker-registry, docker-image, nfs, google-cloud-speech, kops, jupyterhub, rbac, google-cloud-endpoints, standard-sql, google-cloud-build, docker-networking

google: google-cloud-build, google-cloud-datastore, google-speech-api, google-cloud-dataflow, google-cloud-storage, google-cloud-platform, google-kubernetes-engine, google-cloud-sql, google-cloud-speech, google-compute-engine, google-cloud-composer, google-cloud-endpoints, google-cloud-vision, google-vision, google-cloud-pubsub, google-translate, google-app-engine

amazon: amazon-eks
azure: azure-aks, azure-kubernetes
**centroid 21: excel, vba, excel-vba, c#, python
**—–

excel, vba, excel-vba, google-sheets, ms-access, excel-formula, powerbi, outlook, sharepoint, ms-word, access-vba, office365, apache-poi, sap, dax, formatting, pivot-table, office-js, runtime-error, match, powerpoint, outlook-vba, formula, access, row, vsto, ssas, multiple-columns, powerquery, spreadsheet, vlookup, average, extract, userform, unique, ms-office, excel-2010, word-vba, ms-access-2010, excel-2016, rows, ms-access-2016, onedrive, openxml, powerbi-desktop, copy-paste, transpose, conditional-formatting, office-addins, office-interop, epplus, xlsxwriter, interop, phpspreadsheet, paste, shapes, offset, powerpivot, win32com, powerbi-embedded, export-to-excel, python-docx, countif, array-formulas, autofill, powerpoint-vba, activex, ms-access-2013, solver, m, business-intelligence, xls, ado, ssas-tabular, adodb, xlrd, delete-row, sumifs, openxml-sdk, excel-interop, add-in, excel-2013, worksheet, excel-addins

google: google-sheets
**centroid 4: git, github, jenkins, python, docker
**—–

git, jenkins, github, jenkins-pipeline, gitlab, continuous-integration, sonarqube, bitbucket, jenkins-plugins, gitlab-ci, devops, azure-pipelines, svn, version-control, phpstorm, webhooks, repository, travis-ci, jekyll, artifactory, atom-editor, jira, pipeline, github-pages, teamcity, slack, push, gitlab-ci-runner, git-bash, github-api, continuous-deployment, branch, nexus, circleci, workflow, git-merge, diff, jenkins-groovy, clone, git-submodules, gitignore, atlassian-sourcetree, pull-request, bitbucket-pipelines, patch, commit, git-branch, versioning, mercurial, gnupg, git-commit, gerrit, rebase, open-source, githooks, allure, ssh-keys, git-push

azure: azure-pipelines
**centroid 33: java, hibernate, spring, spring-boot, jpa
**—–

hibernate, jpa, spring-data-jpa, spring-data, solr, orm, transactions, spring-batch, wildfly, mapping, many-to-many, lucene, h2, entity, liquibase, jpql, ejb, hql, multi-tenant, persistence, spring-data-rest, hibernate-mapping, eclipselink, querydsl, one-to-many, spring-transactions, hikaricp, criteria, hibernate-criteria, gorm, ehcache, jpa-2.0, criteria-api, entitymanager, transactional

**centroid 39: java, python, c#, node.js, android
**—–

http, ssl, sockets, curl, server, networking, websocket, encryption, https, socket.io, proxy, openssl, tcp, ssl-certificate, cryptography, http-headers, certificate, localhost, udp, mqtt, connection, client, ip, reverse-proxy, network-programming, aes, rsa, port, tls1.2, chat, client-server, lets-encrypt, cloudflare, haproxy, real-time, virtualhost, wireshark, keystore, ipc, x509certificate, zeromq, bouncycastle, django-channels, tcpclient, http-proxy, serversocket, telnet, cryptojs, public-key-encryption, private-key, tcp-ip, x509, client-certificates, certbot, tor, multicast

**centroid 30: java, rest, spring, spring-boot, javascript
**—–

java, spring-boot, spring, rest, maven, eclipse, spring-mvc, tomcat, jsp, jdbc, web-services, soap, servlets, swagger, jackson, java-ee, thymeleaf, netbeans, web-applications, apache-camel, architecture, salesforce, spring-webflux, jersey, httprequest, jax-rs, wsdl, http-post, multipartform-data, tomcat8, soapui, response, resttemplate, cxf, httpresponse, rest-assured, api-design, struts2, soap-client, jstl, restsharp, spring-rest, spring-test, spring-restcontroller, jax-ws, put, endpoint, http-status-codes, struts, spring-web

**centroid 22: java, spring-boot, spring, maven, eclipse
**—–

gradle, intellij-idea, neo4j, jsf, jar, grails, jboss, spring-cloud, spring-integration, jaxb, internationalization, log4j, eclipse-plugin, swagger-ui, jms, websphere, ant, activemq, vaadin, spring-kafka, pom.xml, log4j2, project-reactor, weblogic, java-11, netty, jetty, maven-3, javamail, crud, java-9, spring-cloud-stream, couchbase, ibm-mq, weblogic12c, datasource, glassfish, hazelcast, logback, osgi, hybris, openapi, project, maven-plugin, netflix-eureka, mybatis, cloudfoundry, reactive, eclipse-rcp, swagger-2.0, slf4j, netflix-zuul, quartz-scheduler, jetbrains-ide, spring-boot-actuator, lombok, spring-jdbc, sonarqube-scan, war, cdi, javabeans, tomcat7, interceptor, swt, java-10, freemarker, spring-boot-test, aop, jdbctemplate, dependency-management, spring-cloud-config, aspectj, spring-aop, flyway, amqp, classpath, spring-jms, jackson-databind, spring-cloud-dataflow, spring-websocket, spring-amqp, pivotal-cloud-foundry, spring-cloud-netflix, cucumber-jvm, executable-jar, spring-integration-dsl, swagger-codegen, tomcat9, spring-data-redis, javadoc, jndi, consul, intellij-plugin, dto, maven-surefire-plugin, hystrix, stomp, bean-validation, gateway, mapstruct, birt, spring-tool-suite, properties-file, jackson2, camunda, springfox, spring-data-neo4j, spring-rabbitmq, spring-session, pydev, xtext, servlet-filters, payara, code-formatting, spring-cloud-gateway

google: google-maps
**centroid 15: javascript, angular, android, typescript, visual-studio-code
**—–

ionic-framework, npm, visual-studio-code, ionic3, google-maps, cordova, debugging, electron, nativescript, ionic4, ionic2, meteor, autocomplete, geolocation, cordova-plugins, markdown, vscode-settings, phonegap, ide, webstorm, vscode-extensions, decorator, editor, ionic-native, onesignal, keyboard-shortcuts, angular2-nativescript, xdebug, hybrid-mobile-app, intellisense, nativescript-angular, tslint, remote-debugging, html-framework-7, breakpoints, syntax-highlighting, vscode-debugger, pylint, ibm-mobilefirst, jsdoc, nativescript-vue, prettier, windbg, phonegap-plugins, code-snippets, inappbrowser, phonegap-build

**centroid 42: javascript, html, c#, android, python
**—–

unity3d, image, tkinter, svg, animation, canvas, three.js, chart.js, scroll, 3d, html5-canvas, camera, geometry, css-animations, bitmap, rotation, aframe, icons, glsl, shader, fabricjs, rendering, webgl, css-transitions, transform, png, scrollbar, transition, textures, blender, html2canvas, drawing, mask, linechart, draw, jquery-animate, angular-animations, konvajs, raycasting, webvr

**centroid 43: javascript, html, jquery, css, reactjs
**—–

d3.js, leaflet, google-maps-api-3, magento, magento2, ethereum, jquery-ui, cakephp, jinja2, primefaces, extjs, ember.js, fullcalendar, maps, ckeditor, mapbox, solidity, materialize, jquery-select2, dialog, angularjs-directive, recaptcha, openlayers, coldfusion, polymer, gis, react-apollo, styled-components, tinymce, progress-bar, geojson, javascript-events, position, apollo-client, undefined, addeventlistener, sharepoint-2013, semantic-ui, amcharts, web-deployment, joomla, settimeout, render, p5.js, openstreetmap, element, instagram-api, parent-child, liquid, mapbox-gl-js, focus, angularjs-ng-repeat, setinterval, react-admin, alert, polygon, dom-events, web-component, textarea, react-select, href, web3, contact-form-7, zoom, facebook-javascript-sdk, refresh, graphql-js, overlay, height, slick, content-security-policy, jqgrid, html5-audio, delay, anchor, blogger, html-select, child-process, jquery-plugins, width, html-lists, kendo-asp.net-mvc, loading, zurb-foundation, id, bind, whitespace, dropzone.js, onchange, semantic-ui-react, owl-carousel, media, video.js, hide, netlify, background-color, sticky, geocoding, native-base, webpage, inline, tampermonkey, slick.js, form-data, padding, ternary-operator, event-listener, facebook-messenger-bot, underscore.js, formik, jquery-validate, quill, dc.js, highlight, react-table, electron-builder, bulma, jquery-selectors, fullscreen, multi-select, innerhtml, slideshow, parallax, draggable, footer, styling, react-component, jquery-mobile, selector, swiper, infinite-scroll, contenteditable, sidebar, jquery-ui-datepicker, mobx-react, form-submit, shadow-dom, backbone.js, each, margin, html-form, mathjax, jquery-ui-autocomplete, viewport, c3.js, adsense, sweetalert2, web-development-server, keypress, jquery-ui-sortable, facebook-php-sdk, sweetalert, center, font-awesome-5, react-proptypes, placeholder, summernote, font-face, react-context, web-frontend, ref, css-float, parent, wysiwyg, getelementbyid, font-size, higher-order-functions, lifecycle, dropzone, partial-views, asyncstorage, wai-aria, spfx, custom-element, jstree, bootstrap-datepicker, line-breaks, react-dom, fancybox, css-tables, stylesheet, react-google-maps, react-leaflet, timepicker, option, facebook-marketing-api, gsap, crossfilter, draftjs, directive, fixed, show-hide

google: react-google-maps, google-maps-api-3
**centroid 1: javascript, python, html, java, android
**—–

wordpress, woocommerce, javafx, swing, google-bigquery, button, google-api, video, google-analytics, plugins, kivy, youtube, onclick, calendar, dynamics-crm, youtube-api, widget, background, slider, radio-button, event-handling, save, amp-html, compression, google-tag-manager, javafx-8, click, hover, fxml, analytics, display, firebase-analytics, mouseevent, resize, background-image, size, listener, google-analytics-api, cross-domain, toggle, jpeg, google-data-studio, google-adwords, rgb, submit, gif, pixel, crop, gallery, tiff, thumbnails, image-resizing, exif, user-experience, src, pillow

google: google-adwords, google-bigquery, google-api, google-tag-manager, google-data-studio, google-analytics-api, google-analytics

**centroid 26: javascript, reactjs, node.js, typescript, react-native
**—–

javascript, node.js, reactjs, firebase, react-native, flutter, firebase-realtime-database, webpack, dart, redux, google-cloud-firestore, ecmascript-6, react-redux, firebase-authentication, google-cloud-functions, jestjs, promise, async-await, react-router, firebase-cloud-messaging, import, push-notification, dialogflow, material-ui, module, react-navigation, react-native-android, expo, fetch, gulp, mocha, firebase-storage, actions-on-google, create-react-app, enzyme, material-design, jsx, flutter-layout, lodash, babel, navigation, es6-promise, node-modules, apollo, state, npm-install, babeljs, eslint, gatsby, react-native-ios, javascript-objects, react-router-v4, next.js, yarnpkg, webpack-4, react-hooks, redux-form, prestashop, firebase-security-rules, flowtype, react-router-dom, typescript-typings, webpack-dev-server, antd, redux-saga, redux-thunk, router, package.json, react-native-flatlist, firebase-admin, react-props, react-native-navigation, mobx, firebaseui, es6-modules, firebase-hosting, aurelia, pm2, immutability, serverside-rendering, action, setstate, gruntjs, requirejs, ecmascript-5, flutter-dependencies, ssr, react-native-firebase, angular-dart, es6-class, require, laravel-mix, arrow-functions, react-native-maps, npm-scripts, flutter-animation, workbox, firebase-cli, destructuring, babel-loader, immutable.js, minify, browserify, node-sass, nodemon, firebase-security, angularfire, reducers, loader, bower

google: google-cloud-functions, actions-on-google, google-cloud-firestore
**centroid 13: javascript, selenium, google-chrome, html, selenium-webdriver
**—–

selenium, google-chrome, selenium-webdriver, xpath, dom, google-chrome-extension, firefox, caching, automation, iframe, selenium-chromedriver, mobile, browser, internet-explorer, safari, webdriver, css-selectors, google-chrome-devtools, webrtc, progressive-web-apps, service-worker, local-storage, internet-explorer-11, html5-video, microsoft-edge, ignite, phantomjs, chromium, cross-browser, webdriverwait, capybara, screenshot, cpu-architecture, mobile-safari, firefox-addon, webkit, geckodriver, firefox-webextensions, google-chrome-headless, browser-cache, webdriver-io, v8, specflow, selenium-grid, html-agility-pack, memcached, guava, devtools, cucumber-java, headless, domdocument, extentreports, selenium-ide, watir, cache-control, google-chrome-app, browser-automation, rselenium, mozilla

google: google-chrome, google-chrome-headless, google-chrome-devtools, google-chrome-app, google-chrome-extension

**centroid 6: javascript, vue.js, vuejs2, vuex, webpack
**—–

vue.js, express, vuejs2, axios, vue-component, vuex, vuetify.js, xmlhttprequest, vue-router, nuxt.js, fetch-api, vue-cli, vue-cli-3, store, nuxt, bootstrap-vue, vue-test-utils, element-ui, vee-validate

**centroid 40: mongodb, node.js, javascript, python, express
**—–

mongodb, qt, mongoose, graphql, pyqt5, pyqt, mongodb-query, aggregation-framework, discord, qml, qt5, nosql, discord.js, discord.py, aggregate, ejs, handlebars.js, pymongo, backend, schema, mongoose-schema, mean-stack, sails.js, pug, nestjs, loopbackjs, pyqt4, spring-data-mongodb, multer, geospatial, mean, fs, aggregation, lookup, loopback, apollo-server, parse-server, pyside2, bcrypt, mongodb-.net-driver, document, pyside, qt-designer, mongoengine, body-parser, discord.py-rewrite, projection, mern, mongoose-populate, qthread, mlab, joi, passport-local, pyqtgraph, bson, sharding, express-handlebars

**centroid 5: multithreading, java, python, concurrency, c++
**—–

multithreading, asynchronous, parallel-processing, concurrency, multiprocessing, callback, queue, celery, jvm, task, python-asyncio, synchronization, dask, python-multiprocessing, thread-safety, locking, mpi, openmp, singleton, pickle, python-multithreading, opencl, future, threadpool, mutex, task-parallel-library, tornado, deadlock, aiohttp, atomic, wait, executorservice, semaphore, completable-future, handler, goroutine, channel, race-condition, volatile, pool, runnable, java-threads, synchronous, async.js, producer-consumer, synchronized, java.util.concurrent, blocking

**centroid 11: oracle, sql, plsql, oracle11g, database
**—–

oracle, plsql, stored-procedures, oracle11g, triggers, db2, oracle12c, sql-server-2014, oracle-sqldeveloper, oracle-apex, cursor, database-trigger, apex, oracle10g, sqlplus, oracle-apex-5.1, procedure, dynamic-sql, cx-oracle, oracle-adf, oracleforms, hierarchical-data, plsqldeveloper, oracle-apex-5

**centroid 38: pdf, html, python, php, c#
**—–

pdf, merge, webview, printing, fonts, r-markdown, download, base64, puppeteer, itext, hyperlink, latex, export, blob, imagemagick, ocr, pdf-generation, adobe, jspdf, pdfbox, itext7, embed, docx, digital-signature, wkhtmltopdf, fpdf, mpdf, tcpdf, dompdf, ghostscript, acrobat, pypdf2, reportlab

**centroid 9: php, laravel, laravel-5, mysql, javascript
**—–

php, laravel, ajax, laravel-5, codeigniter, validation, eloquent, session, file-upload, model, pagination, codeigniter-3, laravel-5.6, controller, laravel-5.5, migration, upload, laravel-5.7, laravel-blade, laravel-5.4, relational-database, laravel-5.2, php-7, relationship, lumen, middleware, php-7.2, octobercms, guzzle, image-uploading, laravel-5.8, algolia, query-builder, phpexcel, jobs, laravel-query-builder, laravel-5.3, roles, artisan, laravel-nova, php-carbon, laravel-4, laravel-5.1, homestead, pusher, laravel-eloquent, blade, laravel-routing, laravel-dusk, relation, shared-hosting, eager-loading

**centroid 47: php, wordpress, javascript, woocommerce, python
**—–

google-apps-script, email, notifications, google-drive-api, paypal, stripe-payments, gmail, smtp, attributes, wordpress-theming, google-calendar-api, google-visualization, google-oauth, google-sheets-api, product, phpmailer, youtube-data-api, advanced-custom-fields, gmail-api, hook-woocommerce, outlook-addin, metadata, google-sheets-formula, cart, html-email, google-app-maker, hook, exchangewebservices, payment-gateway, custom-post-type, exchange-server, checkout, e-commerce, sendgrid, field, content-management-system, nodemailer, categories, gsuite, google-form, admin, mailchimp, comments, web-hosting, outlook-web-addins, orders, wordpress-rest-api, customization, imap, google-docs, rss, custom-wordpress-pages, custom-taxonomy, shortcode, outlook-restapi, email-attachments, google-sheets-query, mailgun, google-api-php-client, woocommerce-rest-api, wordpress-gutenberg, google-apis-explorer, attachment, gmail-addons, price, sendmail, icalendar, blogs, registration, custom-fields, multisite, google-admin-sdk, shipping, gravity-forms-plugin, google-api-client, archive, pagespeed, smtplib, mime, meta, google-api-nodejs-client, contact-form, taxonomy, google-api-python-client, account, stock

google: google-sheets-api, google-docs, google-oauth, google-apps-script, google-sheets-query, google-sheets-formula, google-api-php-client, google-api-nodejs-client, google-visualization, google-admin-sdk, google-calendar-api, google-apis-explorer, google-api-python-client, google-form, google-app-maker, google-api-client, google-drive-api

**centroid 23: postgresql, sql, python, javascript, mysql
**—–

sqlite, flask, sqlalchemy, hyperledger-fabric, odoo, hyperledger, elixir, blockchain, hyperledger-composer, flask-sqlalchemy, sequence, couchdb, psycopg2, psql, postgis, pyodbc, knex.js, plpgsql, jsonb, jooq, typeorm, postgresql-9.5, ecto, postgresql-10, marshalling, connection-pooling, postgresql-9.6, database-replication, unmarshalling, pgadmin-4, pgadmin, recursive-query, postgresql-9.4, crosstab, go-gorm, database-backups, postgresql-9.3, rds, heroku-postgres

**centroid 35: python, java, c++, c#, windows
**—–

windows, powershell, batch-file, ffmpeg, audio, cmd, windows-10, path, stream, directory, process, vbscript, prolog, ftp, time-complexity, copy, command, zip, file-io, ocaml, scheduled-tasks, storage, big-o, binary-search-tree, registry, scheme, binary-tree, text-files, dynamic-programming, rename, exe, echo, command-prompt, hashtable, powershell-v3.0, filereader, batch-processing, wmi, stack-overflow, file-handling, windows-server-2016, windows-server-2012-r2, bufferedreader, taskscheduler, fstream, hyper-v, readfile, depth-first-search, fibonacci, ifstream, backtracking

**centroid 3: python, java, javascript, arrays, c#
**—–

arrays, string, list, function, loops, csv, algorithm, dictionary, performance, for-loop, file, sorting, class, object, if-statement, oop, haskell, recursion, pointers, variables, generics, java-8, matrix, rust, filter, optimization, indexing, math, lambda, arraylist, inheritance, input, multidimensional-array, search, random, vector, data-structures, time, struct, types, methods, while-loop, foreach, design-patterns, dynamic, functional-programming, collections, java-stream, sas, parameters, enums, nested, interface, constructor, linked-list, syntax, casting, tree, hashmap, binary, properties, scope, reference, type-conversion, floating-point, iterator, null, tuples, static, format, set, conditional, iteration, range, switch-statement, return, append, numbers, boolean, output, int, concatenation, polymorphism, hex, compare, initialization, namespaces, integer, pattern-matching, grouping, logic, key, filtering, parameter-passing, list-comprehension, apply, subset, global-variables, slice, vectorization, conditional-statements, combinations, scanf, java.util.scanner, character, lapply, comparison, this, 2d, override, counter, numpy-ndarray, permutation, user-input, rounding, nested-loops, abstract-class, instance, reduce, prototype, itertools, global, reverse, subclass, comparator, key-value, increment, min, infinite-loop, contains, do-while, associative-array, mergesort, abstract, indexof, break, bubble-sort

**centroid 48: python, java, javascript, r, php
**—–

typo3, wso2, clojure, sublimetext3, drupal-8, acumatica, jframe, docusignapi, teradata, emacs, netsuite, karate, verilog, jasper-reports, marklogic, sparql, vhdl, sympy, autodesk-forge, knitr, erlang, yocto, tcl, odoo-11, cakephp-3.0, mule, phoenix-framework, drupal-7, integration, racket, netlogo, autohotkey, uml, drools, node-red, stata, magento-1.9, common-lisp, aem, opencart, abap, line, python-sphinx, jtable, yii, pentaho, wagtail, coq, regex-lookarounds, slack-api, bioinformatics, openstack, perl6, antlr4, awt, rcpp, upgrade, tweepy, jpanel, macos-high-sierra, documentation, jsonschema, actionscript-3, vmware, wildcard, microsoft-dynamics, prestashop-1.7, typo3-8.x, zend-framework, lisp, gwt, elasticsearch-5, distance, smartcontracts, talend, wso2-am, slim, sfml, message-queue, computer-science, scenebuilder, yii2-advanced-app, rdf, inno-setup, fpga, flask-wtforms, bitcoin, clipboard, special-characters, unreal-engine4, hana, preg-replace, gdal, flash, nginx-config, wso2esb, system-verilog, arangodb, wso2is, netbeans-8, uuid, graphviz, liferay, omnet++, spatial, encode, powershell-v4.0, paypal-sandbox, http2, dynamics-365, local, ip-address, servicestack, hdf5, firewall, kdb, executable, linear-programming, add, orientdb, angularjs-scope, cplex, pymysql, xpages, phaser-framework, maya, powershell-v2.0, nginx-location, adfs, limit, abstract-syntax-tree, variable-assignment, elementtree, wav, mouse, splunk, asterisk, pandoc, publish-subscribe, simulink, webassembly, packages, complexity-theory, ansible-2.x, python-decorators, preg-match, regex-negation, minecraft, spotfire, nested-lists, pcre, gfortran, percentage, matching, monads, jbutton, gsub, numba, sitecore, watson-conversation, dropwizard, edit, frequency, vulkan, cdn, mime-types, wrapper, php-curl, jersey-2.0, scapy, converters, zapier, attributeerror, elm, console.log, web3js, kentico, moodle, intervals, anylogic, multilingual, logical-operators, glm, vlc, owl, autodesk-viewer, dojo, z3, arcgis, classloader, pyomo, sybase, antlr, md5, indexeddb, powerapps, data-conversion, http-status-code-403, web-worker, external, alfresco, airflow-scheduler, finance, typo3-9.x, cpu-usage, pouchdb, ibm-midrange, ping, truffle, qemu, dask-distributed, selection, apache-httpclient-4.x, jsonpath, sha256, coding-style, polymer-2.x, zipfile, vps, symbols, mediawiki, calculation, okta, smarty, blueprism, netcdf, zend-framework3, genetic-algorithm, snmp, repeat, plesk, signature, doxygen, qgis, dlib, jena, ckeditor4.x, tortoisesvn, face-recognition, message, number-formatting, dropbox, lm, default, spss, perforce, assert, uart, acl, symlink, suitescript2.0, kendo-ui-angular2, getter-setter, jira-rest-api, crm, sleep, indentation, prompt, analysis, lme4, ironpython, latitude-longitude, grammar, dotnetnuke, cqrs, gaussian, regex-greedy, koa, yum, numerical-methods, haskell-stack, scala-cats, hugo, rpc, priority-queue, openldap, popen, shapefile, var, partition, record, combinatorics, ada, nio, pentaho-data-integration, appium-ios, scheduling, pyautogui, snakemake, production-environment, lwjgl, computational-geometry, scaling, tabulator, lifetime, naming-conventions, jsf-2, lotus-notes, javac, numeric, odoo-8, modeling, salesforce-lightning, silverstripe, bookdown, websphere-liberty, virtualization, wxwidgets, ramda.js, hapijs, reload, marklogic-9, snapshot, hierarchy, server-side, cakephp-3.x, prestashop-1.6, schedule, unix-timestamp, difference, ontology, readline, configuration-files, opendaylight, block, wolfram-mathematica, rpm, logstash-grok, currency, mount, remote-server, destructor, nsis, captcha, feathersjs, code-generation, hardware, django-2.1, suitescript, typoscript, jython, trim, distributed-system, zabbix, vaadin8, nodemcu, magento2.2, string-matching, shuffle, ckeditor5, mixed-models, fedora, ipv6, new-operator, ember-data, llvm-clang, exit, webcam, str-replace, large-data, simplexml, rules, elasticsearch-aggregation, rhel, dsl, ethernet, event-sourcing, vimeo, hashset, date-formatting, zlib, standards, bamboo, converter, liferay-7, file-get-contents, solrcloud, servicenow, logstash-configuration, xhtml, virtual, pywin32, equals, intersection, micronaut, production, cs50, fopen, elasticsearch-6, lazy-evaluation, server-sent-events, extbase, translate, python-module, tabular, libreoffice, sml, private, apostrophe-cms, tostring, bitbake, actionlistener, restore, activiti, mypy, opencart-3, janusgraph, rank, multiplication, keyword, archlinux, optaplanner, imagick, informix, flex-lexer, photoshop, pyaudio, openlayers-3, reset, sentry, umbraco7, messaging, lotus-domino, fiddler, interactive, jlabel, folium, bigcommerce, transparency, nullreferenceexception, operator-keyword, tracking, keyboard-events, twitter-oauth, static-methods, polymer-3.x, prisma, mule-esb, string-comparison, counting, layout-manager, gherkin, inner-classes, docker-for-windows, checksum, imagemagick-convert, connect, php-7.1, sublimetext, wso2carbon, python-telegram-bot, react-native-router-flux, desktop, paypal-rest-sdk, php-5.6, division, typeclass, identityserver3, mapbox-gl, wix-react-native-navigation, sample, point-clouds, web-audio, vertica, java-time, mosquitto, dllimport, dump, covariance, cytoscape.js, cgal, r-package, installshield, eigen3, point-cloud-library, ngx-datatable, sampling, vapor, clojurescript, auto-increment, overlap, ibm-cloud-infrastructure, echarts, web-audio-api, hp-uft, office365api, ngx-translate, shortcut, paho, ember-cli, rfid, applet, swap, predicate, host, detox, cas, jsf-2.2, trigonometry, sandbox, beagleboneblack, filestream, numpy-broadcasting, xsd-validation, fgets, ghc, serenity-bdd, spi, duration, jna, unzip, fiware, rhel7, long-integer, pentaho-spoon, cpython, crystal-lang, assertion, string-concatenation, compatibility, java-module, fluid, meta-tags, wildfly-10, hashicorp-vault, apache-karaf, roblox, gurobi, install4j, development-environment, static-analysis, ffi, h5py, django-authentication, urlencode, directx-11, salt-stack, r-raster, pseudocode, hsqldb, django-celery, fatal-error, pywinauto, peewee, p2p, tinymce-4, mysql-5.7, openlayers-5, vis.js, palindrome, angular-template, resteasy, kable, quickbooks, monaco-editor, rdp, solrj, file-transfer, language-agnostic, mustache, java-7, naudio, velocity, wikidata, copy-constructor, countdown, wtforms, montecarlo, wso2ei, sitemap, stringbuilder, geoserver, joomla3.0, symbolic-math, bytecode, high-availability, sharepoint-2010, assign, semantic-web, rtf, vmware-clarity, odoo-12, informatica, volume, jit, monogame, super, eof, syncfusion, rust-cargo, dataweave, stack-trace, browser-sync, arduino-ide, blogdown, communication, rider, favicon, fill, processbuilder, biginteger, labview, resampling, normal-distribution, linear, angular4-router, hierarchical-clustering, drag, modbus, diagram, word, org-mode, admin-on-rest, equation, webrequest, tinkerpop3, restful-authentication, lib, tizen, user-agent, survival-analysis, point, fragment-shader, tableau-server, ansible-inventory, delete-file, code-injection, clickhouse, text-editor, kettle, angularjs-material, date-range, rpy2, complex-numbers, graphene-python, coded-ui-tests, midi, programming-languages, web-push, pine-script, equality, holoviews, sapply, quotes, jtextfield, emscripten, sas-macro, angular-http, varnish, phalcon, typing, freeze, opentok, password-protection, anonymous-function, resolution, remote-desktop, cryptocurrency, hpc, default-value, tsc, multiline, chromium-embedded, treemap, substitution, arm64, shutil, supervisord, at-command, interpreter, packet, google-search, dynamics-crm-online, can-bus, neo4j-apoc, ranking, httpserver, gsm, freebsd, centos6, yield, c++-winrt, fread, anypoint-studio, jboss7.x, type-hinting, wixcode, epoch, uninstall, autoit, smartcard, wikipedia, angular-service-worker, cosine-similarity, protege, schema.org, typescript-generics, dropbox-api, verification, composition, windows-server, using, hmac, dry, ag-grid-angular, median, messenger, rethinkdb, thingsboard, xilinx, named-pipes, office-ui-fabric, dynamics-crm-365, heroku-cli, date-format, imputation, jfreechart, wiremock, packaging, outliers, target, typo3-7.6.x, ngrok, audit, models, jboss-eap-7, moving-average, 32bit-64bit, strapi, views, silverstripe-4, rasa-core, content-type, event-loop, textinput, smoothing, surface, explode, getusermedia, 7zip, confidence-interval, watch, freertos, zend-framework2, circular-dependency, qliksense, repeater, cjk, clock, django-testing, pic, csrf-protection, shopping-cart, encapsulation, paypal-ipn, json-ld, cobol, key-bindings, relative-path, hashcode, thrift, bing-maps, localdate, dicom, netezza

google: google-search
**centroid 37: python, machine-learning, tensorflow, python-3.x, keras
**—–

tensorflow, numpy, keras, machine-learning, opencv, matlab, deep-learning, scikit-learn, image-processing, neural-network, scipy, nlp, pytorch, computer-vision, conv-neural-network, lstm, data-science, regression, classification, dataset, gpu, nltk, google-colaboratory, linear-regression, artificial-intelligence, object-detection, cluster-analysis, generator, spacy, interpolation, logistic-regression, svm, data-analysis, tesseract, random-forest, tensorflow-datasets, bazel, signal-processing, recurrent-neural-network, opencv3.0, fft, tensorboard, gensim, sparse-matrix, word2vec, cv2, h2o, cross-validation, tensor, caffe, xgboost, reshape, reinforcement-learning, stanford-nlp, linear-algebra, k-means, tensorflow-estimator, prediction, rnn, keras-layer, pca, probability, curve-fitting, decision-tree, text-mining, tensorflow-serving, loss-function, object-detection-api, google-cloud-ml, metrics, mathematical-optimization, image-segmentation, matrix-multiplication, autoencoder, tensorflow-lite, r-caret, text-classification, sentiment-analysis, scikit-image, convolution, training-data, categorical-data, tensorflow.js, knn, mnist, valueerror, sklearn-pandas, gradient-descent, weka, yolo, python-tesseract, word-embedding, feature-extraction, tokenize, emgucv, feature-selection, predict, coreml, similarity, normalization, one-hot-encoding, backpropagation, convolutional-neural-network, ode, lda, tf-idf, openai-gym, image-recognition, theano, naivebayes, rasa-nlu, detection, grid-search, data-mining, differential-equations, layer, torch, roc, mxnet, camera-calibration, topic-modeling, cudnn, kaggle, confusion-matrix, tensorflow2.0, doc2vec, distributed, embedding, tfrecord, recommendation-engine, multilabel-classification, ner

google: google-colaboratory, google-cloud-ml
**centroid 46: python, php, apache, python-3.x, ubuntu
**—–

apache, nginx, .htaccess, web, url, pip, anaconda, redirect, pycharm, dns, ubuntu-16.04, permissions, url-rewriting, package, mod-rewrite, installation, conda, centos7, ubuntu-18.04, debian, virtualenv, python-import, install, apache2, url-redirection, vagrant, webserver, virtualbox, cpanel, gunicorn, digital-ocean, http-status-code-404, config, hosting, subdomain, systemd, uwsgi, wamp, nvidia, setuptools, ubuntu-14.04, mod-wsgi, pipenv, url-routing, mamp, httpd.conf, environment, query-string, seo, wsgi, subdirectory, setup.py, wampserver, permalinks, pypi, apache2.4, lamp, apt, http-status-code-301, miniconda, http-redirect

**centroid 50: python, python-3.x, python-2.7, pandas, javascript
**—–

python, python-3.x, pandas, dataframe, python-2.7, web-scraping, datetime, parsing, beautifulsoup, post, python-requests, scrapy, request, pygame, python-3.6, pandas-groupby, encoding, unicode, get, utf-8, twitter, character-encoding, header, python-3.7, web-crawler, python-imaging-library, pyinstaller, spyder, tags, export-to-csv, typeerror, odoo-10, openpyxl, jsoup, regex-group, python-3.5, ascii, series, urllib, wxpython, lxml, turtle-graphics, xlsx, rvest, nan, argparse, python-2.x, mysql-python, datetime-format, kivy-language, emoji, importerror, screen-scraping, scrapy-spider, pyserial, html-parsing, python-xarray, flask-restful, tkinter-canvas, cheerio, frame, odoo-9, cx-freeze, twisted, tk, python-datetime, python-unicode, decoding, httr, tkinter-entry, timedelta

**centroid 16: python, unix, bash, sed, linux
**—–

regex, linux, bash, shell, unix, perl, awk, sed, text, replace, split, cron, command-line, grep, scripting, sh, find, substring, filesystems, notepad++, fork, posix, scheduler, cgi, delimiter, text-processing, aix, cut, solaris

**centroid 29: r, python, ggplot2, plot, matplotlib
**—–

r, matplotlib, ggplot2, dplyr, shiny, jupyter-notebook, plot, graph, time-series, statistics, colors, plotly, julia, rstudio, graphics, seaborn, cypher, tidyverse, bokeh, data-visualization, bar-chart, label, networkx, histogram, ipython, purrr, tidyr, visualization, gremlin, gnuplot, influxdb, igraph, shinydashboard, legend, heatmap, octave, graph-theory, simulation, data-manipulation, correlation, raster, plotly-dash, statsmodels, data-cleaning, na, matlab-figure, mutate, scatter-plot, boxplot, multi-index, stringr, dashboard, forecasting, scale, lubridate, r-plotly, missing-data, graph-databases, arima, pie-chart, graph-algorithm, jupyter-lab, axis, geopandas, shiny-server, distribution, breadth-first-search, sparklyr, bayesian, lag, sf, tibble, subplot, matplotlib-basemap, xts, contour, plyr, anova, axis-labels, shortest-path, shiny-reactivity, ggmap, dijkstra, figure, rlang, facet, ggplotly, zoo

**centroid 49: ruby, ruby-on-rails, ruby-on-rails-5, javascript, activerecord
**—–

ruby-on-rails, postgresql, ruby, heroku, redis, ruby-on-rails-5, yii2, hash, activerecord, routes, shopify, ruby-on-rails-4, rspec, rubygems, devise, chef, ruby-on-rails-3, bundle, rails-activestorage, associations, rails-activerecord, puppet, ruby-on-rails-5.2, metaprogramming, rspec-rails, activeadmin, bundler, coffeescript, shopify-app, sidekiq, carrierwave, passenger, sinatra, simple-form, nokogiri, cloudinary, capistrano, puma, webpacker, mongoid, actioncable, erb, haml, rake, paperclip, factory-bot

**centroid 41: sql, sql-server, mysql, database, postgresql
**—–

sql, mysql, sql-server, database, tsql, date, mysqli, join, select, group-by, mariadb, sequelize.js, pdo, phpmyadmin, sql-server-2008, data.table, count, sql-server-2012, xampp, database-design, duplicates, view, sum, timestamp, pivot, foreign-keys, sql-update, mysql-workbench, timezone, tableau, insert, ssms, odbc, constraints, sql-server-2016, etl, subquery, max, syntax-error, left-join, case, database-connection, decimal, inner-join, prepared-statement, full-text-search, database-migration, sql-order-by, query-optimization, sql-server-2008-r2, sql-server-2017, sql-insert, union, backup, aggregate-functions, where, partitioning, common-table-expression, distinct, query-performance, concat, oledb, innodb, replication, window-functions, sql-injection, mdx, primary-key, greatest-n-per-group, where-clause, database-performance, sql-delete, data-warehouse, rdbms, sql-like, database-administration, ddl, entity-relationship, bulkinsert, ssis-2012, calculated-columns, resultset, derby, database-schema, sql-server-2005, create-table, database-normalization, temp-tables

**centroid 14: swift, ios, xcode, objective-c, android
**—–

ios, swift, xcode, objective-c, uitableview, swift4, iphone, uicollectionview, facebook-graph-api, realm, bluetooth-lowenergy, twilio, core-data, cocoa, admob, cocoapods, alamofire, arkit, swift3, crash, uiview, tableview, localization, keyboard, autolayout, sprite-kit, frameworks, uiviewcontroller, augmented-reality, uikit, wkwebview, scenekit, accessibility, closures, in-app-purchase, instagram, xcode10, uinavigationcontroller, avfoundation, uibutton, apple-push-notifications, uiscrollview, uitextfield, delegates, crashlytics, app-store, uicollectionviewcell, ios11, protocols, macos-mojave, ios12, xcode9, storyboard, uinavigationbar, qr-code, uilabel, uiimageview, uitabbarcontroller, ipad, optional, decode, uiimage, cell, metal, segue, mapkit, deep-linking, swift4.2, parse-platform, codable, spotify, uitextview, avplayer, itunesconnect, facebook-login, gradient, touch, audiokit, cocoa-touch, textfield, assets, ios-simulator, uistackview, uisearchbar, uiwebview, grand-central-dispatch, firebase-dynamic-links, watchkit, voip, nslayoutconstraint, fastlane, uiimagepickercontroller, iphone-x, nsattributedstring, interface-builder, viewcontroller, uipickerview, nsuserdefaults, core-bluetooth, decodable, xctest, extension-methods, apple-watch, nsurlsession, core-location, code-signing, navigationbar, uialertcontroller, orientation, uigesturerecognizer, objectmapper, swift-playground, keychain, core-graphics, xib, uisearchcontroller, lldb, swift-protocols, avaudioplayer, tvos, cloudkit, shadow, appdelegate, contacts, statusbar, swift4.1, testflight, mkmapview, ios-autolayout, uibezierpath, gesture, uipageviewcontroller, health-kit, uitabbar, cllocationmanager, calayer, xcuitest, provisioning-profile, icloud, uicollectionviewlayout, geofire, uistoryboard, metalkit, pdfkit, plist, uiviewanimation, swifty-json, collectionview, uibarbuttonitem, ipa, xcode-ui-testing

**centroid 32: symfony, php, symfony4, javascript, mysql
**—–

forms, symfony, symfony4, composer-php, twig, doctrine, annotations, doctrine-orm, phpunit, symfony-3.4, translation, autowired, symfony-forms, sonata-admin, api-platform.com, fosuserbundle, swiftmailer, data-annotations, sonata

**centroid 27: testing, java, javascript, unit-testing, automated-tests
**—–

angularjs, unit-testing, testing, groovy, junit, jmeter, protractor, mockito, automated-tests, jasmine, mocking, cucumber, appium, pytest, testng, robotframework, integration-testing, cypress, performance-testing, android-espresso, code-coverage, e2e-testing, junit5, chai, python-unittest, junit4, sinon, karma-runner, ui-automation, load, appium-android, nightwatch.js, load-testing, tdd, katalon-studio, testcafe, jest, bdd, spock, powermockito, powermock, codeception, jmeter-plugins, rpa, qa, cucumberjs, jmeter-4.0, angular-test, robolectric

## Full code

The code I used to create and display the previous results:
clusters = 50
percent = '01'
one_hot_dimensions = 50

model = 'deleting.kmeans_tagsubtag_%s_big_a_%s_%s' % (clusters, percent,one_hot_dimensions)

clusters_temp_table = 'deleting.clusters_%s_result_a_%s_%s' % (clusters, percent, one_hot_dimensions)

one_hot_p = client.query("""
SELECT STRING_AGG(

FORMAT("IFNULL(ANY_VALUE(IF(tag2='%%s',1,null)),0)X%%s", tag2, REPLACE(REPLACE(REPLACE(REPLACE(tag2,'-','_'),'.','D'),'#','H'),'+','P')) ) one_hot

FROM (

SELECT tag2, SUM(questions) questions FROM `deleting.stack_overflow_tag_co_ocurrence`

GROUP BY tag2
ORDER BY questions DESC
LIMIT %s
)""" % one_hot_dimensions).to_dataframe().iloc[0]['one_hot']
client.query("""
CREATE OR REPLACE MODEL `%s` OPTIONS ( model_type='kmeans',
distance_type='COSINE',
num_clusters=%s )
AS
WITH tag_and_subtags AS (
SELECT tag1, %s
FROM `deleting.stack_overflow_tag_co_ocurrence`
WHERE percent>0.%s
GROUP BY tag1
)
SELECT * EXCEPT(tag1)
FROM tag_and_subtags
""" % (model, clusters, one_hot_p, percent)).to_dataframe()
df = client.query("""
CREATE OR REPLACE TABLE %s
AS
WITH tag_and_subtags AS (
SELECT tag1, MAX(questions) questions, %s
FROM `deleting.stack_overflow_tag_co_ocurrence`
WHERE percent>0.%s
GROUP BY tag1
)
SELECT centroid_id
, STRING_AGG(tag1, ', ' ORDER BY questions DESC) tags

, ARRAY_TO_STRING(ARRAY_AGG(IF(tag1 LIKE '%%google%%', tag1, null) IGNORE nulls LIMIT 18), ', ') google_tags

, ARRAY_TO_STRING(ARRAY_AGG(IF(tag1 LIKE '%%amazon%%' OR tag1 LIKE '%%aws%%', tag1, null) IGNORE nulls LIMIT 18), ', ') amazon_tags

, ARRAY_TO_STRING(ARRAY_AGG(IF(tag1 LIKE '%%azure%%', tag1, null) IGNORE nulls LIMIT 18), ', ') azure_tags

, COUNT(*) c
FROM ML.PREDICT(MODEL `%s` , (SELECT * FROM tag_and_subtags )
)
GROUP BY 1
ORDER BY c DESC
""" % (clusters_temp_table, one_hot_p, percent, model)).to_dataframe()
df = client.query("""
SELECT centroid_id, c, yep, tags
, IFNULL(google_tags, '') google_tags
, IFNULL(amazon_tags, '') amazon_tags
, IFNULL(azure_tags, '') azure_tags
FROM `%s` JOIN (
SELECT centroid_id

, STRING_AGG(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(feature,'_','-'),'D','.'),'H','#'),'P','+'), 'X', ''), ', ' ORDER BY numerical_value DESC LIMIT 5) yep

FROM ML.CENTROIDS(MODEL `%s`
)
GROUP BY 1
) USING(centroid_id)
ORDER BY yep
""" % (clusters_temp_table, model)).to_dataframe()
for index, row in df.iterrows():
print('centroid %s: %s\n-----' % (row['centroid_id'], row['yep']))
print(row['tags'])
print()
if row['google_tags']:
print('google: %s' % row['google_tags'])
if row['amazon_tags']:
print('amazon: %s' % row['amazon_tags'])
if row['azure_tags']:
print('azure: %s' % row['azure_tags'])
print('\n')

Note that I joined my results with `ML.CENTROIDS()` — which gives me the top differentiating occurring tags for each centroid — even if they are not part of each cluster.

## And that’s all it takes

Are you surprised by the results? Or surprised by how easy was to run our k-means modeling with BigQuery? Or curious for why I chose `distance-type: 'COSINE'` for this problem? Now it’s your turn to play :).

Check the [BigQuery docs for creating models](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create?source=post_page---------------------------) and the [k-means tutorial](https://cloud.google.com/bigquery-ml/docs/kmeans-tutorial?source=post_page---------------------------).

### Lak’s thoughts

How would you choose the best parameters? Check [Lak Lakshmanan](https://medium.com/u/247b0630b5d6?source=post_page---------------------------) post for [hyper-parameter tuning](https://towardsdatascience.com/how-to-do-hyperparameter-tuning-of-a-bigquery-ml-model-29ba273a6563?source=post_page---------------------------). Lak also had some interesting ideas about dimensionality reduction for clustering via matrix factorization — but we’ll leave that for a future post.

As an untested preview:*Once you have the co-occurrence of tag1 and tag2, treat it as a recommendation problem, i.e. tag2 is what tag1 liked percent of the time. Then, you can do matrix factorization:*

CREATE OR REPLACE MODEL deleting.tag1_tag2
OPTIONS (
model_type='matrix_factorization',
user_col='tag1', item_col='tag2', rating_col='percent10' )
AS
SELECT tag1, tag2, percent*10 AS percent10
FROM advdata.stack_overflow_tag_co_ocurrence

*From this matrix factorization, you will have tag1_factors and tag2_factors which are essentially an embedding of the tags learned from the data. Concatenate these and cluster it instead …*

SELECT feature, factor_weights
FROM ML.WEIGHTS( MODEL deleting.tag1_tag2 )
WHERE processed_input = 'tag1' and feature LIKE '%google%'

# Want more?

I’m Felipe Hoffa, a Developer Advocate for Google Cloud. Tweet me [@felipehoffa](https://twitter.com/felipehoffa), my previous posts on [medium.com/@hoffa](https://medium.com/@hoffa), and all about BigQuery on [reddit.com/r/bigquery](https://reddit.com/r/bigquery) – including [predicting when will Stack Overflow reply](https://towardsdatascience.com/when-will-stack-overflow-reply-how-to-predict-with-bigquery-553c24b546a3).

## Author

![4cfd811c2c01646a1e4f33fb9e68ab5c](../_resources/a756532542c16a1e852005e8a3bd8163.jpg)
Felipe Hoffa
Developer Advocate

Developer Advocate at Google Cloud. Originally from Chile, now in San Francisco and around the world. #BigQuery #bigdata #opendata.

[Author Archives](https://stackoverflow.blog/authors/fhoffa/)[Website](https://medium.com/@hoffa/)[Twitter](https://twitter.com/felipehoffa)[Stack Overflow](https://stackoverflow.com/users/132438/felipe-hoffa)[Youtube](https://www.youtube.com/playlist?list=PLG1fouPFF9lwF7l0tg81qUoJk4n3H5w5y)

## Tags

- [Code for a Living](https://stackoverflow.blog/code-for-a-living/)
- [Stackoverflow](https://stackoverflow.blog/tags/stackoverflow/)

## Related Articles

![lifeboat-630x450.jpg](../_resources/584a82ec9ff6693558dd5c78c2f36483.jpg)

## [Adios to Unfriendly Badges! Ahoy, Lifejacket and Lifeboat](https://stackoverflow.blog/2019/06/18/adios-to-unfriendly-badges-ahoy-lifejacket-and-lifeboat/)

[(L)](https://stackoverflow.blog/authors/jericson/)by [Jon Ericson](https://stackoverflow.blog/authors/jericson/) on June 18, 2019

Sometimes it’s helpful to look back at past decisions and reconsider them in a new light. As part of our ongoing efforts to make Stack Overflow more welcoming and inclusive,...

[Continue reading](https://stackoverflow.blog/2019/06/18/adios-to-unfriendly-badges-ahoy-lifejacket-and-lifeboat/)

## [Update to Security Incident [May 17, 2019]](https://stackoverflow.blog/2019/05/17/update-to-security-incident-may-17-2019/)

[(L)](https://stackoverflow.blog/authors/maryferguson/)by [Mary Ferguson](https://stackoverflow.blog/authors/maryferguson/) on May 17, 2019

Update (May 23, 2019): The affected 184 public network users have been notified via email. While we continue to investigate the recent attack to Stack Overflow, here is an update...

[Continue reading](https://stackoverflow.blog/2019/05/17/update-to-security-incident-may-17-2019/)

## [Security Update](https://stackoverflow.blog/2019/05/16/security-update/)

[(L)](https://stackoverflow.blog/authors/maryferguson/)by [Mary Ferguson](https://stackoverflow.blog/authors/maryferguson/) on May 16, 2019

Over the weekend, there was an attack on Stack Overflow. We have confirmed that some level of production access was gained on May 11. We discovered and investigated the extent...

[Continue reading](https://stackoverflow.blog/2019/05/16/security-update/)