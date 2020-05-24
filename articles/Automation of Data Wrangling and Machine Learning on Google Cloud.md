Automation of Data Wrangling and Machine Learning on Google Cloud

# Automation of Data Wrangling and Machine Learning on Google Cloud

## Using Cloud Dataprep, Cloud Composer and BigQuery ML

[![2*MFu2XaVt4VQdGqOD_y4nHQ.png](../_resources/cdbf57a90737f2d91cd1a85ab0ac46e7.png)](https://medium.com/@aosterloh34?source=post_page-----7de6a80fde91----------------------)

[Alex Osterloh](https://medium.com/@aosterloh34?source=post_page-----7de6a80fde91----------------------)

[Apr 15](https://medium.com/google-cloud/automation-of-data-wrangling-and-machine-learning-on-google-cloud-7de6a80fde91?source=post_page-----7de6a80fde91----------------------) · 5 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='198'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='199' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/7de6a80fde91/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='207'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='208' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/7de6a80fde91/share/facebook?source=post_actions_header---------------------------)

I recently read this [blog post](https://cloud.google.com/blog/products/data-analytics/how-to-orchestrate-cloud-dataprep-jobs-using-cloud-composer) on using the [**Cloud Dataprep** API](https://cloud.google.com/dataprep/docs/html/API-JobGroups-Create-v4_145281446) to trigger automated wrangling jobs with Cloud Composer (based on Apache Airflow).

I took the concept of using the **BigQuery**  [public dataset](https://cloud.google.com/bigquery/public-data?csw=1) on US birth stats (to play with the data first, see [post](https://medium.com/@ImJasonH/exploring-natality-data-with-bigquery-ed9b7fc6478a) by [Jason](https://medium.com/u/4a0637341451?source=post_page-----7de6a80fde91----------------------) on using the data with **BigQuery**). Except that this time, in addition to cleaning the data I added a step to train a linear regression model using **BigQuery ML** (see [documentation](https://cloud.google.com/bigquery-ml/docs/bigqueryml-natality) for more).

![1*bVImfaIn58ocGfNuTiNTdg.png](../_resources/a89d01f3723b3b5375d538e7f0dbbbe5.png)
![1*bVImfaIn58ocGfNuTiNTdg.png](../_resources/2161d25fcd7af325ad64ed197465caea.png)
**As shown above I will use:**
1. **Cloud Dataprep (Trifacta Service)** to
import and wrangle a 14GB public dataset on birth stats with 137M records
2. **BigQuery ML** to
train a linear regression model on the cleaned data
3. **Cloud Composer** to
automate both steps above

# 1. Let’s get some data

In most projects, Data Professionals don’t usually deal with straightforward **BigQuery** datasets, but instead they find themselves dealing with different kinds of data as found in the wild. To bring this example closer to reality, we will export this **BigQuery** dataset as CSV into a Google Cloud Storage bucket. Looking at the data in **BigQuery** you can see there are 31 columns and some of the data has missing values. To train our model later to predict baby weight, we only need a handful of features (columns). Also we want to ignore records that have missing or wrong values (e.g. a mother having 99 alcoholic drinks per week even beats my best college days; also, giving birth in week 99 is [unlikely among humans](https://www.livescience.com/33086-what-animal-has-the-longest-pregnancy.html)).

![1*V28VWOjvhg0_pcF5tf3xeg.png](../_resources/5fe60d846c9960e2632dc91578979e39.png)
![1*V28VWOjvhg0_pcF5tf3xeg.png](../_resources/b363416dc3206aa08507b650eee8f0ea.png)
Data shows more columns than we need and many missing or wrong values

# 2. Clean the data

I am using **Cloud Dataprep**, a managed service by **Trifacta** for wrangling, cleaning and preparing structured and unstructured data. In just 2 minutes I can take a 137M record file, delete all but 5 columns and filter out all rows that have missing or wrong values. All with a nice and tidy interface and by simple pointing and clicking. You can save all these steps into a *recipe* which will let you repeatedly and consistently apply them later. Running the *recipe* takes another 20+ minutes to execute all the transformations using **Cloud **[**Dataflow**](https://cloud.google.com/dataflow), a managed service on Google cloud for stream and batch data processing.

![1*J_Njk4dVQCOWpehwBWqpyA.png](../_resources/623ad0592102fccd050902f114669bef.png)
![1*J_Njk4dVQCOWpehwBWqpyA.png](../_resources/1c8f8faf397a1fbcfb75412b4367040f.png)
Just select the columns you want to keep and choose to ‘Delete others’

Next in **Cloud Dataprep** I can identify missing values by clicking on the black area underneath the column name adding the *Delete Rows *step to my wrangling *recipe*.

![1*xj1fd92hwK6s95h9OqMaUg.png](../_resources/08f0c9ee00058ac05d5e1993465b0279.png)
![1*xj1fd92hwK6s95h9OqMaUg.png](../_resources/80a77bcb309e2b4d723171d00777576c.png)

It’s easy to remove records with missing or wrong values, or replace values with e.g. mean

Of course you can do far more sophisticated transformations, split e.g. semistructured data into multiple columns, add new columns with derived values or join datasets from different sources. To execute the pipelines I click *Run Job* top right where I then select an output destination. In this case I choose to write to a new **BigQuery **table, as we want to train a model using **BigQuery ML** in the next step.

![1*_MkWlhWLDhc_GZ-LCP_hUQ.png](../_resources/48f387b565d65757e0a47ff573b632d8.png)
![1*_MkWlhWLDhc_GZ-LCP_hUQ.png](../_resources/6b11d688bb561c9607230bb90d889a53.png)

Output of the pipeline execution shows e.g. the auto-scaling feature of Cloud Dataflow

# 3. Let’s train a machine learning model

Now that we have a cleaned set of the data in **BigQuery,** we can train a model using **BigQuery ML**. I will not go into details here, as this is explained in detail, using the same dataset, in the [**BigQuery ML** documentation](https://cloud.google.com/bigquery-ml/docs/bigqueryml-natality).

![1*0-ArbmYGe-IK3g6CcN7VPw.png](../_resources/35f8bff07926ab86e0abd9230e507cb1.png)
![1*0-ArbmYGe-IK3g6CcN7VPw.png](../_resources/e0046917c06b0bac89718dc95e1c6ba4.png)
Calling ML.PREDICT on some test data to predict baby weight

**Spoiler alert: the model trained on the cleaned data performs better than the model of the original dataset**

# 4. Finally, let’s automate everything

Assuming your input data changes daily (like COVID-19 cases), you would need to manually run the steps above or write some script/code to trigger the following steps:

1. Calling the **Dataprep API** with the recipe ID and auth token
2. Wait for the **Dataflow** job to finish
3. Train a new version of the model with **BigQuery ML**

Automating this process would also require deploying the code somewhere, configuring scheduling/triggers, contemplating error handling, retrials with exponential backoff, automated retries, and more.

Or…(insert drumroll)… we could use Cloud Composer instead. Cloud Composer is a managed version of Apache Airflow for orchestrating data pipelines. Airflow defines orchestration steps using Python DAGs (directed acyclic graph). It’s mostly boilerplate code that defines parameters, order of execution and dependencies between the steps. My colleague [Tahir Fayyaz](https://medium.com/u/61dbd674077e?source=post_page-----7de6a80fde91----------------------) wrote a [nice post on working with Airflow and BigQuery](https://cloud.google.com/blog/products/gcp/how-to-aggregate-data-for-bigquery-using-apache-airflow).

![1*NeRkE2HnQbOZrAmWQaHnlQ.png](../_resources/889602762bd17cb27b0a19750f52a99e.png)
![1*NeRkE2HnQbOZrAmWQaHnlQ.png](../_resources/75659165ba1175dfc232b114d8b9b70f.png)

The simple DAG has basically 2 steps: First run the Dataprep job using Cloud Dataflow (then wait for completion) and when done, create a new linear regression model using BigQuery ML

Here is my example (abbreviated) code on [GitHub](https://github.com/aosterloh/natality-bqml-composer-dataprep/blob/master/dataprep-bqml-pipeline_v7.py) that you see below.

import Airflow
...default_args = {
'owner': 'Alex Osterloh',
'depends_on_past': False,
...
'schedule_interval': '[@daily](http://twitter.com/daily)'
}...#common DAG parameters like scheduling
with airflow.DAG(
'natality_bq_model_v8',
default_args=default_args,

# Not scheduled, trigger only

schedule_interval=None,
user_defined_macros={
'json': json
}
) as dag:# Trigger Dataprep via HTTP POST call
run_dataprep_task = SimpleHttpOperator(
task_id='run_dataprep_job',
endpoint='/v4/jobGroups',
data=json.dumps({"wrangledDataset": {"id": int(recipe_id)}}),
....
)# Wait for Dataprep job to finish
wait_for_dataprep_job_to_complete = HttpSensor(
task_id='wait_for_dataprep_job_to_complete',

endpoint='/v4/jobGroups/{{ json.loads(ti.xcom_pull(task_ids="run_dataprep_job"))["id"] }}?

.....
)# Train new model using BigQuery ML
bigquery_run_sql = bigquery_operator.BigQueryOperator(
task_id='bq_run_sql',
....
sql='''
CREATE OR REPLACE MODEL `<project-name>.natality_bqml.natality_model_v7`
OPTIONS
(model_type='linear_reg', input_label_cols=['weight_pounds']) AS
SELECT
weight_pounds,
is_male,
gestation_weeks,
mother_age,
CAST(mother_race AS string) AS mother_race
FROM
`thatistoomuchdata.natality_data_us.natality_data_clean_model_v6`
WHERE
weight_pounds IS NOT NULL
AND RAND() < 0.001
'''
)# Define the task dependencies
run_dataprep_task >> wait_for_dataprep_job_to_complete >> bigquery_run_sql

# Next steps

If you are into data automation, machine learning and jazz, I summed everything up in this 6 minute video, enjoy.

*Thanks *[*Felipe*](https://www.linkedin.com/in/felipemartina/)* for helping me get the wording right. This is not official Google work. Let me know if I missed something.*