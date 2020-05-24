BigQuery: Set up limits and custom quotas through API

# BigQuery: Set up limits and custom quotas through API

[![2*ZX7q1RNRQv0wO4CklPa3CA.jpeg](../_resources/ae8cbbde0ede21905b84fc96a8d66110.jpg)](https://medium.com/@guillaume.blaquiere?source=post_page-----629f77438b7e----------------------)

[guillaume blaquiere](https://medium.com/@guillaume.blaquiere?source=post_page-----629f77438b7e----------------------)

[Jan 6](https://medium.com/google-cloud/bigquery-set-up-limits-and-custom-quotas-through-api-629f77438b7e?source=post_page-----629f77438b7e----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='188'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='189' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/629f77438b7e/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='192'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/629f77438b7e/share/facebook?source=post_actions_header---------------------------)

![1*16ymYv9B5qoHX1qRBFQIig.png](../_resources/d689158f3d62ab3f31efcfce88df9a96.png)
![1*16ymYv9B5qoHX1qRBFQIig.png](../_resources/6559a3920af9ffc08f4aa79241696de6.png)

BigQuery is the **petabytes scale data warehouse** on Google Cloud Platform. You can load a lot of data freely and easily, the storage cost is very affordable with an automatic switch to cold storage after 90 days.

When you use the **on-demand pricing, the cost is based on the volume of data that the query scans**  [(about $5 per TB for the cheaper location)](https://cloud.google.com/bigquery/pricing#on_demand_pricing) in your queries. And when **you have terabytes or petabytes, it can become expensive**!

# Cost optimizations

For optimizing the data organisation and reduce the volume of data that you scan, **you can clusterize and/or **[**partition your data on any fields**](https://medium.com/google-cloud/partition-on-any-field-with-bigquery-840f8aa1aaab?source=---------2------------------). You can also [**require the partition filter**](https://cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter) in the `where` clause of the queries. The objective is to force the requester to ask himself about the data scanned for optimizing the queries.

However, **nothing forces the requester to use the partitioned field smartly** or to **prevent a badly use of it**. Thereby, requiring the partition field in each request can be useless and the whole data can still be scanned.

# Custom quotas on volume of data scanned

To prevent the scanning of large volumes of data due to the lacks of partitioning or bad usages of partitions, Google allows to **set **[**custom quotas on volume of data**  **scanned** per user or per project. The quotas are reset to 0 every days at midnight, pacific time.](https://cloud.google.com/bigquery/docs/custom-quotas)

It’s easy to set a quota

- Go to [quotas page](https://console.cloud.google.com/iam-admin/quotas)
- Select only BigQuery service
- Look for `Query usage per day per user` or `Query usage per day` and select it *(click on line)*
- Click on `Edit Quotas`
- Set the limit on the right side, validate and `Submit`

![1*x8Fe5mE4GfgDzzTLRK_p5g.gif](../_resources/1b8334f50b2e0e01e220b297a77ce6f8.jpg)
![1*x8Fe5mE4GfgDzzTLRK_p5g.gif](../_resources/19f608e212999759691218b8ac948707.gif)
Set a custom quota with console
> Perfect per console, but how to do it at scale?

# Automate the quota limits

My company is global (50+ countries), thousands of GCP projects (3k+) and BigQuery tables (100k+), hundreds of subsidiaries, and lot of different internal and external IT teams and data scientists. With my colleagues at headquarters, we do a lot for** training, helping and assisting users for preventing mistakes and unexpected cost**. But it’s not enough.

![1*jOofcANGz5hNL-MerMkFqg.png](../_resources/6abfeb79f92e98c531b75010cc48aefb.png)
![1*jOofcANGz5hNL-MerMkFqg.png](../_resources/35d41b2cbde8fc8f90e4bfec2ac938c7.png)
BigQuery cost in 2019

Thereby, we decided to set a limit on all DEV and TEST projects, for production, it’s only when requested by the teams in charge of the project. For this, **we wanted to use the **[**service management API**](https://cloud.google.com/service-infrastructure/docs/service-management/reference/rest/)**  **and we tried all the documented endpoints… **It’s impossible to update quotas via API!!**

> How to update thousands of project? and how to apply this automatically on new ones?

# Undocumented API usage

Stuck in a dead end, I tried to understand **how the API worked in the console** thanks to the developer mode of Chrome and **I found a workaround.**

***Important note****: The following explanation is not documented by Google and can change or be blocked at any time, without warning. ****Use with caution.***

## The API principle

To invoke this API, use this URL. *Replace the *`*PROJECT_ID*`* with your own project ID.*

https://servicemanagement.googleapis.com/v1/services/[bigquery-json.googleapis.com/projectSettings/PROJECT_ID?updateMask=quotaSettings.consumerOverrides%5B%22QueryUsagePerDay%22%5D](http://bigquery-json.googleapis.com/projectSettings/gbl-imt-homerider-basguillaueb?updateMask=quotaSettings.consumerOverrides%5B%22QueryUsagePerDay%22%5D&alt=json)

*Replace the value *`*QueryUsagePerDay*`* with *`*QueryUsagePerUserPerDay*`* if you want to set the limit per user and not per project*

**The API is secured**, you have to present an HTTP Bearer access token with your request. The call **uses the HTTP verb **`**PATCH**` and you have to present `**application/json**`** content-type body**.

The limit is in MB. Here the body sets the limit to 150Tb per day on the project. *Replace the *`*PROJECT_ID*`* with your own project ID.*

{
"quotaSettings":
{
"adminOverrides":{},
"consumerOverrides":
{
"QueryUsagePerDay":
{
"limit":"151380224"
}
},
"force":true
},
"consumerProjectId":"PROJECT_ID",

"serviceName":"[bigquery-json.googleapis.com](http://bigquery-json.googleapis.com/)"

}

*Replace the value *`*QueryUsagePerDay*`* with *`*QueryUsagePerUserPerDay*`* if you want to set the limit per user and not per project*

## Put it all together

For experimenting this API, make a call with `curl`. Create a file with `data` as name and the previous body as content. Then, run this command (for example on Cloud Shell). *Replace the *`*PROJECT_ID*`* with your own project ID.*

curl -d @data \
-H "content-type: application/json" \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-X PATCH \

"https://servicemanagement.googleapis.com/v1/services/[bigquery-json.googleapis.com/projectSettings/PROJECT_ID?updateMask=quotaSettings.consumerOverrides%5B%22QueryUsagePerDay%22%5D](http://bigquery-json.googleapis.com/projectSettings/gbl-imt-homerider-basguillaueb?updateMask=quotaSettings.consumerOverrides%5B%22QueryUsagePerDay%22%5D&alt=json)"

The answer is the ID of the operation
{
"name": "operations/tmo-quf.9d6e6e04-28fd-4147-8fee-dea59764b5d0"
}
Check the console