BigQuery + Cloud Functions: how to run your queries as soon as a new Google Analytics table is available

# BigQuery + Cloud Functions: how to run your queries as soon as a new Google Analytics table is available

## A step-by-step guide on how to make sure your tables, dashboards and data transfers are always up-to-date

[![2*jcEDHiDJO06Ohn0CmuNg3w.jpeg](../_resources/69bfd85aa6fe64c2b409f7ad3cd0a864.jpg)](https://towardsdatascience.com/@marieke91?source=post_page-----17fbb62f8aaa----------------------)

[Marieke Pots](https://towardsdatascience.com/@marieke91?source=post_page-----17fbb62f8aaa----------------------)

[Mar 27](https://towardsdatascience.com/bigquery-cloud-functions-how-to-run-your-queries-as-soon-as-a-new-google-analytics-table-is-17fbb62f8aaa?source=post_page-----17fbb62f8aaa----------------------) · 5 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='200'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='201' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/17fbb62f8aaa/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='209'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='210' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/17fbb62f8aaa/share/facebook?source=post_actions_header---------------------------)

![1*VcWWrLv-TCm6_iSK9lkCQw.png](../_resources/4f100b8f3004dfb9011e3a551c07642d.png)
![1*VcWWrLv-TCm6_iSK9lkCQw.png](../_resources/1309e0cb3570488f6d5df982da6556ef.png)

* * *

*...*

If you have your Google Analytics view linked to BigQuery, you are probably enjoying the advantages it brings. There is no sampling in your data, you can bring in third-party data, you have more control over your data and much more.

But, there was one thing bothering me. And maybe it is bothering you too. The exact time of the daily export from Google Analytics to the BigQuery table(ga_sessions_YYYYMMDD) can be somewhat unpredictable. This makes it is impossible to run scheduled queries on this dataset without taking a small risk.

- *You might set your scheduled queries too early. *If, for some reason, the Google Analytics export is delayed, you might miss a day of data. You will have to manually correct this every time this happens. Or you might consider using the intraday table. But this might not be as ideal either, since Google states: “Data for the current day is not final until the daily import is complete. You may notice differences between intraday and daily data” (see the documentation [here](https://support.google.com/analytics/answer/3437719?hl=en&ref_topic=3416089)).
- *You might set your scheduled queries too late.* You might be safe if the exports are delayed in this case. But, your underlying tables for your dashboards and/or possible transfers to other data systems may not be as up to date as they need to be for your decision makers.

Of course, in these uncertain times of Corona, you might call this a first-world-problem. But because it is a problem that I can help fix, I will take you through a step by step guide on how to run your scheduled queries in the exact minute that a new daily export from Google Analytics is ready. The result is a much more fail-proof set-up in which your tables and dashboards are always as up-to-date as they can possibly be.

The steps that we will be taking are:

1. Create a filter in Cloud Logging that isolates the daily log that confirms that a new Google Analytics table is ready.

2. Set up a Cloud Pub/Sub topic that collect these daily logs.

3. Deploy a Cloud Function that runs your scheduled query in BigQuery as soon as the Pub/Sub topic is being updated with a new log.

* * *

*...*

# Step 1. Cloud Logging

- OK. The first thing to do is to open [Cloud Logging](https://console.cloud.google.com/logs).
- Choose ‘Convert to advanced filter’, by clicking on the little dropdown arrow on the right side of the search field. At least, that’s where it was at the time of this writing .
- You can copy/paste the code below to create a filter that will isolate the logs that confirm that a new Google Analytics table (ga_sessions_YYYYMMDD) has been created. Do not forget to fill in your own dataset ID and project ID in the first two lines.

protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.load.destinationTable.datasetId="[REPLACE_WITH_YOUR_DATASET_ID]"protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.load.destinationTable.projectId="REPLACE_WITH_YOUR_PROJECT_ID"protoPayload.authenticationInfo.principalEmail="[analytics-processing-dev@system.gserviceaccount.com](https://towardsdatascience.com/bigquery-cloud-functions-how-to-run-your-queries-as-soon-as-a-new-google-analytics-table-is-17fbb62f8aaamailto:analytics-processing-dev@system.gserviceaccount.com)"protoPayload.methodName="jobservice.jobcompleted"protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.load.destinationTable.tableId:"ga_sessions"NOT protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.load.destinationTable.tableId:"ga_sessions_intraday"

- If you adjust the timeframe to the last 7 days, you should now see one message for each day. In the screenshot below, you see the unpredictability of the exact time of the export. In this example, sometimes the table was ready before 2pm and sometimes it’s after 3pm. If your screen looks like this, you are ready to go to the next step!

![1*kP0c8th5aBFmEiESLBj8Tg.png](../_resources/8abeeaf09ebbc77974830ec4d02b53c3.png)
![1*kP0c8th5aBFmEiESLBj8Tg.png](../_resources/1b80732322b13522d41b0fabbc6b9a26.png)
Screenshot made in Google Logging

* * *

*...*

# Step 2. Cloud Pub/Sub

Pub/Sub stands for Publish–Subscribe and can be considered as a messaging system between systems. In this case, we want to create a new Pub/Sub topic that collects the logs that we isolated in the previous step. This way, a message will be collected every time a new Google Analyicts table is available.

- Click on “Create Sink” in the screenshot above.
- You can be as creative as you want to be when entering a sink name.
- Choose “Pub/Sub” as Sink service.
- Choose to create a new Cloud Pub/Sub Topic and give it a name that you can remember in the next step.
- Click ‘Create Sink’ and you are ready for the next step.

![1*fQnpkCA6p2ZwEg89Bivezw.png](../_resources/830e88d0f77d06993777e4ee8e3cc981.png)
![1*fQnpkCA6p2ZwEg89Bivezw.png](../_resources/105242194ddbda96f62a4898b76d9153.png)
Screenshot in Google Logging: creating a pub/sub sink and topic

* * *

*...*

# Step 3. Cloud Functions

In this last step we will create a Cloud Function (written in Python) that runs every time the Pub/Sub topic is triggered. The function then sends a request to the [BigQuery DataTransfer API](https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest) to start a manual transfer run on one of your scheduled (on demand) SQL queries.

- Open up [Cloud Functions](https://console.cloud.google.com/functions)
- Choose to create a new function.
- Choose “Cloud Pub/Sub” as trigger and select the Pub/Sub topic that you created in the previous step.
- Choose “Python 3.7” (or perhaps higher if you read this in the future ) as runtime.

![1*TdK4OjLL2SdHmvGAVTf6oA.png](../_resources/c80cad5e2b1b5480bf7b91a8aa05c1b4.png)
![1*TdK4OjLL2SdHmvGAVTf6oA.png](../_resources/5b7d2a3d20af9b46d90f16072b2eb0dc.png)
Screenshot of how to set up the Google Cloud Function

- Copy/paste the code below, and put this in the “Main.py” file.

|     |     |
| --- | --- |
| 1   | import  time |
| 2   | from  google.protobuf.timestamp_pb2  import  Timestamp |
| 3   | from  google.cloud  import  bigquery_datatransfer_v1 |
| 4   |     |
| 5   | def  runQuery (parent, requested_run_time): |
| 6   |  client  =  bigquery_datatransfer_v1.DataTransferServiceClient() |
| 7   |  projectid  =  '[enter your projectId here]'  # Enter your projectID here |
| 8   |  transferid  =  '[enter your transferId here]'  # Enter your transferId here |
| 9   |  parent  =  client.project_transfer_config_path(projectid, transferid) |
| 10  |  start_time  =  bigquery_datatransfer_v1.types.Timestamp(seconds=int(time.time() +  10)) |
| 11  |  response  =  client.start_manual_transfer_runs(parent, requested_run_time=start_time) |
| 12  |  print(response) |
| 13  |     |
| 14  | # do not forget to put google-cloud-bigquery-datatransfer>=0.1 in the requirements.txt |

 [view raw](https://gist.github.com/marieke91/1ea713caf6a5213585c8697a41ee3095/raw/a6043c4b907fd8b43372ebdbac454cd3b9185120/cloudfunction_datatransfer.py)  [cloudfunction_datatransfer.py](https://gist.github.com/marieke91/1ea713caf6a5213585c8697a41ee3095#file-cloudfunction_datatransfer-py) hosted with ❤ by [GitHub](https://github.com/)

- Replace the project ID and the transfer ID with the details of the scheduled query that you want to run.
- You can find these IDs in the configuration tab of your [scheduled query](https://console.cloud.google.com/bigquery/scheduled-queries) The resource name shows a URL in which you will find both IDs: “*projects/[THIS_IS_YOUR_PROJECT_ID)/locations/us/transferConfigs/[THIS IS YOUR TRANSFER_ID]*”.
- In this case, I’m assuming that you have already created the scheduled query that you want to run. If you have not, this is the time to [create your scheduled query](https://cloud.google.com/bigquery/docs/scheduling-queries) in BigQuery. It’s best to have the queries set to run ‘on demand’, otherwise it might run too often.
- Add the little piece of code below in ‘Requirements.txt’, so that it has all the packages it needs to run the Python Code.

google-cloud-bigquery-datatransfer>=0.1

- Set “runQuery” as the function to execute.
- Click on deploy!

# And now: enjoy the automation

If you have correctly set up everything, your scheduled query will now start to run as soon as a new daily table has been exported to BigQuery! This means that you can sit back, relax and enjoy that your Google Analytics data is always as fresh as it can be.

*If you have any tips, comments or questions, do not hesitate to ask me in the comments below.*