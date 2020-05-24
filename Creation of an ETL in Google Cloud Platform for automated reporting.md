Creation of an ETL in Google Cloud Platform for automated reporting

# Creation of an ETL in Google Cloud Platform for automated reporting

## Learn how to create your own serverless and fully scalable ETL for automated reporting using PyTrends as an example

[![0*ro7yJM7_Rxxk4kda](../_resources/de1c81d8bef834fe86aa48c401b958a1.jpg)](https://towardsdatascience.com/@alex.masip?source=post_page-----8a0309ee8a78----------------------)

[Alex Masip](https://towardsdatascience.com/@alex.masip?source=post_page-----8a0309ee8a78----------------------)

[Apr 22](https://towardsdatascience.com/creation-of-an-etl-in-google-cloud-platform-for-automated-reporting-8a0309ee8a78?source=post_page-----8a0309ee8a78----------------------) · 9 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='198'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='199' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/8a0309ee8a78/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='207'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='208' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/8a0309ee8a78/share/facebook?source=post_actions_header---------------------------)

![1*q-MNaFFUqC-iENL0TB3_rw.png](../_resources/dd4c7eb01741a4056734ab573ad8f6c9.png)
![1*q-MNaFFUqC-iENL0TB3_rw.png](../_resources/02c80c8fd5b00ec4d9e152c5f0b7830a.png)
The final report based on PyTrends data

*As an initial note, it is important to mention that this article is coauthored by *[*Alberto Vargas*](https://medium.com/@a.vargas.pina)* and Alex Masip. Medium doesn’t have a coauthor option yet, so you should blame both of us :)*

We are both part of the Data department at [Labelium](https://www.labelium.com/). As a Data department inside a media agency, we have constant demands for the development and update of reports of all kinds, with a very eclectic selection of data sources.

Therefore, we had the pushing need to develop a standard ETL process that would meet the following requirements:

- Be fully automated, without the need for intervention from Data department resources once the report is delivered.
- Be able to ingest any type of data source and any update condition.
- Keep it inside GCP, as it is our main working stack.

What we explain in this article is the step-by-step of how we implemented it, the reasons for choosing each of the different tools and some useful tips along the way. The use case that will help illustrate the whole process is an automated report of the Search Engine Index extracted from Google Trends using PyTrends. The brands and keywords selected are a wide selection aimed at showing the effect of the Covid crisis on the search habits of Spanish internet users. The report updates automatically every Monday at 08:05 Spanish time (GMT+1).

It is important to note that this specific report could have been automated using a much simpler solution, for example executing the needed python code by launching a VM with a startup script. But the goal was to develop and test an ETL that would work on any scenario regardless of the specific update conditions.

This is a basic schema of the ETL:
![1*mBnix6ZnHsf3fiKHAdPz5Q.png](../_resources/179a904c54c8a1999b3e92e755700610.png)
![1*lDdJgdVDnlQwvKYYjnsIgQ.png](../_resources/3d21b9cca91934d510c0417258afce92.png)
ETL

In the next section, we will go into detail on everything regarding the PyTrends implementation for this specific report. If you are just interested in the automation part, you can jump directly to the Automation section.

* * *

*...*

# PyTrends

You can find all the code on [**this GitHub**](https://github.com/albertovpd/pytrends_cloud_function_example).

If you would prefer a step-by-step guide, just follow along with us.

To better understand what Pytrends is, how it works, and its limitations, we strongly recommend these articles: C[ategories](https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories), [Pytrends documentation](https://pypi.org/project/pytrends/), [a great tutorial](https://searchengineland.com/learn-how-to-chart-and-track-google-trends-in-data-studio-using-python-329119), [how it works](https://www.karinakumykova.com/2019/03/calculate-search-interest-with-pytrends-api-and-python/) and/or [this article](https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f).

Hurray! Now that you are an expert on Pytrends, let’s do the script.

The most important thing to remember, for this or any other code you want to activate through Cloud Functions, is that you are working on a completely serverless architecture. If you are not used to typical software development best practices and want to apply best practices on a notebook-based work-flow, we highly recommend the [Jupyter Notebook Manifesto](https://cloud.google.com/blog/products/ai-machine-learning/best-practices-that-can-improve-the-life-of-any-developer-using-jupyter-notebooks). These are Cloud Function *compulsory* architecture standards:

- Forget subfolders, all scripts must be in the same folder.
- The output folder must be called “**../tmp**”, so while developing, create a tmp folder above your current one. You will not need it in the end as Cloud Function will create one.

Our choice is to use 4 scripts:

- main.py calls the working scripts through***  ****runpy.*
- download_pytrends.py, requests the required info from *pytrends*.
- upload_gcs.py uploads the new info to GCS through *gcsfs.*
- remove_files.py erase all collected data.

* * *

*...*

# Scripts

Remember to create a requirements.txt file to specify the libraries you need:

|     |     |
| --- | --- |
| 1   | gcsfs==0.6.1 |
| 2   | pandas==1.0.3 |
| 3   | pytrends==4.7.2 |
| 4   | importlib-metadata==1.6.0 |

 [view raw](https://gist.github.com/alex-labelium/8e63578b5b06fa6abc1b6a3c3081c842/raw/a49d3101d6a4a6cc9ad0ef4bda896866ee7a1b81/requeriments.txt)  [requeriments.txt](https://gist.github.com/alex-labelium/8e63578b5b06fa6abc1b6a3c3081c842#file-requeriments-txt) hosted with ❤ by [GitHub](https://github.com/)

And all the imports:

|     |     |
| --- | --- |
| 1   | import  runpy |
| 2   | import  os |
| 3   | from  os  import  listdir |
| 4   | from  os.path  import  isfile, join |
| 5   | import  gcsfs |
| 6   | import  pandas  as  pd |
| 7   | import  random |
| 8   | import  pytrends |
| 9   | from  pytrends.request  import  TrendReq |
| 10  | import  time  as  timer |
| 11  | import  datetime |
| 12  | from  datetime  import  datetime, date, time, timedelta |

 [view raw](https://gist.github.com/alex-labelium/2bc9da92b18604fd2569dc0fdd376da9/raw/00594128df46864dc3759992a7003d1cdb26e9fb/imports.py)  [imports.py](https://gist.github.com/alex-labelium/2bc9da92b18604fd2569dc0fdd376da9#file-imports-py) hosted with ❤ by [GitHub](https://github.com/)

main.py

|     |     |
| --- | --- |
| 1   | def  main (data,context):processes= ("download_pytrends.py","upload_gcs.py","remove_files.py")for  p  in  processes: |
| 2   | exec(open(p).read())if  __name__  ==  "__main__":main('data','context') |

 [view raw](https://gist.github.com/alex-labelium/8a728079ca46b74f0164eaa6622f54b2/raw/831ef9ac5e0e9dd116fe5d9f56904c7bf9d776dc/main.py)  [main.py](https://gist.github.com/alex-labelium/8a728079ca46b74f0164eaa6622f54b2#file-main-py) hosted with ❤ by [GitHub](https://github.com/)

- download_pytrends.py

|     |     |
| --- | --- |
| 1   | # date |
| 2   | yesterday=(datetime.now()-timedelta(days=1)).date() |
| 3   | week_ago=(datetime.now()-timedelta(days=8)).date() |
| 4   | dates=str(week_ago) +  " "  +  str(yesterday)# keywords |
| 5   | keywords=[ ["keyword"],cat_number,["keyword"],cat_number...etc]# creating dataframe and saving it |
| 6   | df  =  tracking_in_time_keywords(companies) #this is a function I describe belowdf.to_csv("../tmp/your_csv.csv") |

 [view raw](https://gist.github.com/alex-labelium/28cec3b8b3af2cd8cbde02d1a8d2197e/raw/3a7faf2301dc1ef0d9d83cc2301359f61bb611c9/download_pytrends.py)  [download_pytrends.py](https://gist.github.com/alex-labelium/28cec3b8b3af2cd8cbde02d1a8d2197e#file-download_pytrends-py) hosted with ❤ by [GitHub](https://github.com/)

Using the keywords-category code, we make sure every keyword is compared with the top keyword of its category. Creating a list of several keywords will give you results relative to that keyword, not the non-listed ones.

- The function to request the info, based on [**this one**](https://searchengineland.com/learn-how-to-chart-and-track-google-trends-in-data-studio-using-python-329119):

|     |     |
| --- | --- |
| 1   | def  tracking_in_time_keywords(kw_list):pytrends  =  TrendReq(hl='country', tz=0) |
| 2   | future_dataframe={}c=1 |
| 3   | for  i  in  range(len(kw_list)): |
| 4   | if  i%2==0: |
| 5   | try: |
| 6   | print("Requesting ",str(kw_list[i]))pytrends.build_payload(kw_list[i], cat=kw_list[i+1],timeframe=dates, geo='country', gprop='')future_dataframe[c]=pytrends.interest_over_time() |
| 7   | future_dataframe[c].drop(['isPartial'], axis=1,inplace=True) |
| 8   | c+=1 |
| 9   | result  =  pd.concat(future_dataframe, axis=1)# this is for intense API requesting |
| 10  | secs=int(random.randrange(10, 50)) |
| 11  | print("Sleeping {} seconds before requesting ".format(secs), str(kw_list[i]))timer.sleep(secs) |
| 12  | print("Done")except:print("***","\n","Error with ",kw_list[i],"or not enough trending percentaje","\n","***")df1=result.unstack(level=-1) |
| 13  | df2=pd.DataFrame(df1)return  df2 |

 [view raw](https://gist.github.com/alex-labelium/b1df6af4b69b7fa3135afddc15b7a637/raw/2082c76c98eef4ef5f925215962840658aa555bf/function.py)  [function.py](https://gist.github.com/alex-labelium/b1df6af4b69b7fa3135afddc15b7a637#file-function-py) hosted with ❤ by [GitHub](https://github.com/)

*Unstack(level=-1)* is used to structure all keywords in the same column. It will be useful when plotting results in Data Studio.

We can now interact with Google Cloud Storage. This took a bit of fiddling, as not everything is documented in the gcsfs library documentation:

|     |     |
| --- | --- |
| 1   | fs  =  gcsfs.GCSFileSystem(token='your token name.json' ,project='your project name in GCP')# upload |
| 2   | with  fs.open('your bucket/your csv name.csv') as  youralias:df  =  pd.read_csv(youralias)fs.upload("../tmp/csv_you_just_created.csv",'your bucket/your csv name.csv') |

 [view raw](https://gist.github.com/alex-labelium/d2d7a96fccc5e4be1aae5dd3d0b54351/raw/8bdb7d4d1aad03d45c1a8c67d8067d59013501b9/gcsfs.py)  [gcsfs.py](https://gist.github.com/alex-labelium/d2d7a96fccc5e4be1aae5dd3d0b54351#file-gcsfs-py) hosted with ❤ by [GitHub](https://github.com/)

- remove_files.py erase all collected data:

|     |     |
| --- | --- |
| 1   | import  os |
| 2   | from  os  import  listdir |
| 3   | from  os.path  import  isfile, join#list of csvs |
| 4   | only_csv  = [f  for  f  in  listdir("../tmp") if  isfile(join("../tmp", f))] |
| 5   | [os.remove("../tmp/{}".format(e)) for  e  in  only_csv] |
| 6   | print(only_csv," removed ../tmp folder clean") |

 [view raw](https://gist.github.com/alex-labelium/f54b1a0be296df83ab83bf1232c00173/raw/6996cfe72044c1dc182f5d3e04b9e4ea9881ce23/remove_files.py)  [remove_files.py](https://gist.github.com/alex-labelium/f54b1a0be296df83ab83bf1232c00173#file-remove_files-py) hosted with ❤ by [GitHub](https://github.com/)

For our purposes we have several csvs, so we created a list.

We now have a full working PyTrends implementation that pushes the csv to Google Cloud Storage.

Before moving to the automation part, a couple of quick tips:

- Keep in mind how much data you are requesting through PyTrends and the timeouts you use in order to not get temporarilly banned.
- Google Trends information is noisy and not fully stable. That is by design; do not be surprised if the same query yields different results. Just keep in mind that Google Trends information is great for spotting global trends, but nothing else. It is not designed to give highly dependent information for deep data analysis.

* * *

*...*

# Automation

## The extraction phase

The main pipe is:
Cloud Scheduler > Cloud Pub/Sub > Cloud Functions

As we were discussing at the start, it is indeed overengineered for this specific use case. There is no need to use Cloud Pub/Sub and we could have used a simpler or more traditional and compact solution. But we wanted to create a pipeline that would allow us to trigger the update of the report in a very broad scope of scenarios and that would scale very easily.

Cloud Pub/Sub is the event and global messaging system from GCP. It offers fully automated scaling and provisioning. It is very helpful for us because it easily allows us to integrate the report automation as part of the global workflow of any application. If you need to streamline any type of real time analytics, it is worth a look.

The other key element in the pipeline is Cloud Functions. In this particular use case, Cloud Functions executes the python code that triggers PyTrends to update the data on Google Cloud Storage, as we saw in the previous section. Cloud Functions is GCP’s event-driven serverless compute platform. I’m sure you can very clearly see the trend by now: aiming for a completely serverless event-driven architecture.

These are the step-by-step instructions to setup this phase; it is extremely easy to do:

- Create a job on Cloud Scheduler:

![1*UwhHmMph0NVtWdDPAIotOw.png](../_resources/b8903d8dc633287799062045b28d88d1.png)
![1*UwhHmMph0NVtWdDPAIotOw.png](../_resources/84328315c2aaac18a3719c2b0a7b1e12.png)
Creating a job on Cloud Scheduler

The are only two things to keep in mind here: 1) for frequency you need to use the classical unix-cron format; 2) remember to specify Pub/Sub as your target.

- Go to Pub/Sub and create a new topic, according to the topic you established on Cloud Scheduler:

![1*2kpnwOPxb9d7j5F1MPek9Q.png](../_resources/4012a41a3381f8e61b2c9b6050e1e3a1.png)
![1*2kpnwOPxb9d7j5F1MPek9Q.png](../_resources/434a11851d9b3806b14a2ec140b24d68.png)
Creating a topic on Pub/Sub

This will be triggered by Cloud Scheduler and in turn will trigger the cloud function.

The only thing left to do is to setup the cloud function. Cloud Functions allows us to execute code in python, Node.js or Go. In our case, we are using a python script, so we need to set up the options accordingly:

![1*kWT8rxMSXJnPAcdp00JYoQ.png](../_resources/a071c97fbab88d742b21a6e649402f36.png)
![1*kWT8rxMSXJnPAcdp00JYoQ.png](../_resources/ae82a36e8f51b397b079ad84142982bb.png)
Creating the cloud function

You will need to specify pub/sub as trigger. Choose the topic you created previously on pub/sub, upload the zip file with your python code and select main as your function. Remember to also point to the correct stage bucket on GCS you want to use for staging.

Remember also that the zip file has to include all the scripts in the root folder (no extra folders!), including the requirements.txt file. In addition, main.py is your initiator script.

As a side note, it is important to mention that Cloud Functions has limitations, according to the use case it is designed for. For example, the maximum timeout is 540 seconds. If you need to execute code for longer periods, Cloud Functions is not your ideal tool. It may make sense to look into App Engine (maybe triggered by a cloud function if you need that flexibility).

You can see the advanced options here:
![1*Hp2AqP7tvkZ0cZzPxgXXww.png](../_resources/38b58c480395e6af825e0a248447a932.png)
![1*Hp2AqP7tvkZ0cZzPxgXXww.png](../_resources/e3eea1005d2596f203d11d71547d97af.png)
Cloud Functions advanced options

As you can see, you can change the timeout, change network options, add environment variables, etc. For this specific use case, the default options work well for us.

## Transforming and loading data for visualization

With the data extracted, updated and stored where we want it, we can move to the next phase: getting that data ready for reporting.

We will pull the data from Cloud Storage with Dataprep, schedule its publication on BigQuery and generate our Data Studio report from BigQuery.

Dataprep is a data preparation solution based on [Trifacta Wrangler](https://www.trifacta.com/products/wrangler-editions/) and it’s fully integrated on GCP. It’s very visual and easy to use. If you prefer to work directly with SQL recipes and have complex data transformation needs that you need automated, we highly recommend [Dbt](https://www.getdbt.com/). We use it internally to transform Google Ads data for its use in BigQuery and it’s great.

But for this specific use case, Dataprep will serve us well.
Start by creating a new flow:
![1*lDdJgdVDnlQwvKYYjnsIgQ.png](../_resources/b58be26273e6b329dc8ae2063d0d3023.png)
![1*WXA0zVwEPYKwsYs_VjMfmw.png](../_resources/5954904b50d23a1300435258ee364de2.png)
Creating a flow in Dataprep
Then, import the data to work with:
![1*sxuvnHyZ2ph8WTQ2gLIHUQ.png](../_resources/ec3684827008a0f1b4f4b0fc56a21d6c.png)
![1*sxuvnHyZ2ph8WTQ2gLIHUQ.png](../_resources/8bb685c6f90cc8277ceb236500647896.png)
Importing data on Dataprep
You can upload data directly from your computer, Cloud Storage or BigQuery.

For our use case, we will choose the file in the bucket in GCS that our python script (executed by Cloud Functions) is generating.

This will open a new flow in Dataprep. We will see a small preview and start to add our recipe:

![1*8GERmJQoG96dYEpsgpqZjQ.png](../_resources/aa2f5c36baa4ff16cff20dde7c4a46f1.png)
![1*8GERmJQoG96dYEpsgpqZjQ.png](../_resources/5302ed9da7a27ce09a8b48423a9e2520.png)
Imported data on Dataprep

Once we begin to edit the recipe, we can start working on the data. We will get the different columns of our csv with some descriptive information and we can edit the data as we wish. This will generate the recipe (the full sequence of steps we have taken to transform the data).

![1*Da0PB9ZOfXGgLpHoDl-kfw.png](../_resources/e45ae497c5692741b293383032833fd8.png)
![1*Da0PB9ZOfXGgLpHoDl-kfw.png](../_resources/83585c0b3124db306d3c565f8ff5fb49.png)
A csv on Dataprep

When we are ready, we can hit *run job*, which will execute our instructions on dataflow:

![1*qLfc-zWAo-syy8ovjx_7Nw.png](../_resources/98b59c905de0eeaf171060d87c049863.png)
![1*qLfc-zWAo-syy8ovjx_7Nw.png](../_resources/17dc0e447c6f34aee85c0f3705feb717.png)

By default, it will generate a csv, but we want the result in BigQuery. To do so, we just need to select *Add Publishing Action *and choose a dataset on BigQuery.

We can also select create/replace, append or truncate, as applicable. Since we want to continuously update the same dataset on BigQuery, we will schedule the job and choose append.

We have now automated the updating of the dataset on BigQuery that we will use as the base for our Data Studio report. The only thing remaining is to add the data source on Data Studio (Resources menu — manage data sources):

![1*WXA0zVwEPYKwsYs_VjMfmw.png](../_resources/8c4dc5e0a5a69c3170ab5b92813c032f.png)
![1*mBnix6ZnHsf3fiKHAdPz5Q.png](../_resources/dd84bbb9c26910bff0d505c5cdb743ed.png)
Adding a new data source on Data Studio

The advantage of using BigQuery as the data source for Data Studio is that we can use BigQuery BI Engine, which is an in-memory analysis service. It gives extremely fast query response and, most importantly for a reporting application, it allows high concurrency.

You can check the final report here: [2020–2019 Search Engine Index Comparison — Spain](https://datastudio.google.com/open/1qyJweNLTKll6VLq1h2G8HRYMwHd-oUUC)

On the first page, you have a brief selection of relevant Spanish companies and can filter by company. On the second page, you can do the same using a selection of keywords representing different sectors. The goal is basically to give a quick glimpse of the Covid-19 effect on search habits on different sectors. It updates automatically every Monday at 08:05 Spanish time (GMT+1). As mentioned in the PyTrends section, you have to remember the quality of Google Trends data, especially in terms of consistency. It is only designed to give a very broad overview of the main tendencies and in that respect, it’s great.

# Conclusions

We hope you have found this little exercise useful and informative. Our main goal was to showcase the possibilities that GCP offers in terms of report automation and how easy it is to set up a fully automated serverless and scalable architecture that can be customized for a wide variety of use cases and data sources.

Needless to say, there are many different paths or tools you could use to accomplish a similar task, many of them less complex in terms of architecture. But in our opinion, this exercise serves as a good starting point to explore on your own and design your ideal solution.