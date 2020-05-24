doitintl/bigquery-grafana

[![68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f646f6974696e746c2f62696771756572792d67726166616e612e7376673f7374796c653d737667](../_resources/92b617c91c923dda5702a4e71772fcb3.png)](https://github.com/doitintl/bigquery-grafana/stargazers)[![68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f646f6974696e746c2f62696771756572792d67726166616e612e7376673f7374796c653d737667](../_resources/7af459f72324d21650efbe216d8c398e.png)](https://camo.githubusercontent.com/d1d4e44871df7ad7e6fda62b3db1249539e41848/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f646f6974696e746c2f62696771756572792d67726166616e612e7376673f7374796c653d737667)[![68747470733a2f2f636972636c6563692e636f6d2f67682f646f6974696e746c2f62696771756572792d67726166616e612e7376673f7374796c653d737667](../_resources/2ab4d1a17079100647ba4e83e0f8c95f.png)](https://circleci.com/gh/doitintl/bigquery-grafana)[![68747470733a2f2f636f6465636c696d6174652e636f6d2f6769746875622f646f6974696e746c2f62696771756572792d67726166616e612f6261646765732f6770612e737667](../_resources/cdc7549615db0401e5262edfa3381eee.png)](https://codeclimate.com/github/doitintl/bigquery-grafana/coverage)[![68747470733a2f2f636f6465636c696d6174652e636f6d2f6769746875622f646f6974696e746c2f62696771756572792d67726166616e612f6261646765732f69737375655f636f756e742e737667](../_resources/56939af60df69dcaca27003d870ed0db.png)](https://codeclimate.com/github/doitintl/bigquery-grafana)[![68747470733a2f2f636f6465636f762e696f2f67682f646f6974696e746c2f62696771756572792d67726166616e612f6272616e63682f6d61737465722f67726170682f62616467652e737667](../_resources/6f5cd05fbfcbc06e71d08701ac4cce45.png)](https://codecov.io/gh/doitintl/bigquery-grafana/)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1116' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#status-ready-for-beta-testing)Status: Ready for Beta Testing

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='77'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1117' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#bigquery-datasource-for-grafana)BigQuery datasource for Grafana

BigQuery datasource plugin provide support for [BigQuery](https://cloud.google.com/bigquery/) as a backend database.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='78'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1120' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#quick-start)Quick start

There are multiple ways to install bigquery-grafana go to [INSTALL](https://github.com/doitintl/bigquery-grafana/blob/master/INSTALL.md) for more infromation.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='79'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1123' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#features)Features:

- Query setup
- Raw SQL editor
- Query formatting
- Macros support
- Additional functions
- Table view
- Annotations
- Sharded tables (`tablename_YYYYMMDD`)
- Partitioned Tables

**Plugin Demo:**

[![grafana-bigquery-demo.gif](../_resources/17904071bb5bf3624a5a5f451dc67b55.gif)](https://raw.githubusercontent.com/doitintl/bigquery-grafana/master/img/grafana-bigquery-demo.gif)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='80'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1137' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#adding-the-data-source-to-grafana)Adding the data source to Grafana

1. Open the side menu by clicking the Grafana icon in the top header.

2. In the side menu under the `Dashboards` link you should find a link named `Data Sources`.

3. Click the `+ Add data source` button in the top header.
4. Select `BigQuery` from the *Type* dropdown.

5. Upload or paste in the Service Account Key file. See below for steps on how to create a Service Account Key file.

> NOTE: If you're not seeing the `Data Sources`>  link in your side menu it means that your current user does not have the `Admin`>  role for the current organization.

| Name | Description |
| --- | --- |
| *Name* | The datasource name. This is how you refer to the datasource in panels & queries. |
| *Default* | Default datasource means that it will be pre-selected for new panels. |
| *Service Account Key* | Service Account Key File for a GCP Project. Instructions below on how to create it. |

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='81'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1166' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#authentication)Authentication

There are two ways to authenticate the BigQuery plugin - either by uploading a Google JWT file, or by automatically retrieving credentials from Google metadata server. The latter option is only available when running Grafana on GCE virtual machine.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='82'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1169' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#using-a-google-service-account-key-file)Using a Google Service Account Key File

To authenticate with the BigQuery API, you need to create a Google Cloud Platform (GCP) Service Account for the Project you want to show data for. A Grafana datasource integrates with one GCP Project. If you want to visualize data from multiple GCP Projects then you can give the service account permissions in each project or create one datasource per GCP Project.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='83'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1172' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#enable-apis)Enable APIs

The following APIs need to be enabled first:

- [BigQuery API](https://console.cloud.google.com/apis/library/bigquery-json.googleapis.com)

Click on the links above and click the `Enable` button:

[![bigquery_enable_api.png](../_resources/edf889e2f806c5b55f41afe3b4cfc24b.png)](https://github.com/doitintl/bigquery-grafana/blob/master/bigquery_enable_api.png)

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='84'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1179' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#create-a-gcp-service-account-for-a-project)Create a GCP Service Account for a Project

1. Navigate to the [APIs & Services Credentials page](https://console.cloud.google.com/apis/credentials).

2. Click on the `Create credentials` dropdown/button and choose the `Service account key` option.

[![createserviceaccountbutton.png](../_resources/a71ad7eb9d4b6e1bbcca6974e41d7510.png)](https://github.com/doitintl/bigquery-grafana/blob/master/createserviceaccountbutton.png)

3. On the `Create service account key` page, choose key type `JSON`. Then in the `Service Account` dropdown, choose the `New service account` option:

[![newserviceaccount.png](../_resources/90f994ef0d727541b19e631699eb6b84.png)](https://github.com/doitintl/bigquery-grafana/blob/master/newserviceaccount.png)

4. Some new fields will appear. Fill in a name for the service account in the `Service account name` field and then choose the `Monitoring Viewer` role from the `Role` dropdown:

[![bq_service_account_choose_role.png](../_resources/a3d5f76bb82ced31122e617109ebd9d7.png)](https://github.com/doitintl/bigquery-grafana/blob/master/bq_service_account_choose_role.png)

5. Click the Create button. A JSON key file will be created and downloaded to your computer. Store this file in a secure place as it allows access to your Stackdriver data.

6. Upload it to Grafana on the datasource Configuration page. You can either upload the file or paste in the contents of the file.

[![bq__grafana_upload_key.png](../_resources/07024b8dd98790deb714e9b661e808ed.png)](https://github.com/doitintl/bigquery-grafana/blob/master/bq__grafana_upload_key.png)

7. The file contents will be encrypted and saved in the Grafana database. Don't forget to save after uploading the file!

[![bq_grafana_key_uploaded.png](../_resources/c2313e112b1615ac1f5eab3b46d8cc1e.png)](https://github.com/doitintl/bigquery-grafana/blob/master/bq_grafana_key_uploaded.png)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='85'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1201' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#using-gce-default-service-account)Using GCE Default Service Account

If Grafana is running on a Google Compute Engine (GCE) virtual machine, it is possible for Grafana to automatically retrieve default credentials from the metadata server. This has the advantage of not needing to generate a private key file for the service account and also not having to upload the file to Grafana. However for this to work, there are a few preconditions that need to be met.

1. First of all, you need to create a Service Account that can be used by the GCE virtual machine. See detailed instructions on how to do that [here](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount).

2. Make sure the GCE virtual machine instance is being run as the service account that you just created. See instructions [here](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using).

3. Allow access to the `Stackdriver Monitoring API` scope. See instructions [here](https://github.com/doitintl/bigquery-grafana/blob/master/changeserviceaccountandscopes).

Read more about creating and enabling service accounts for GCE VM instances [here](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='86'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#build)Build

The build works with Yarn:

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='87'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1212' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#development-build)Development build

	yarn run run build:dev

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='88'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1214' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#production-build)Production build

	yarn run run build:prod

Tests can be run with Jest:

	yarn run test

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='89'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1217' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#contributing)Contributing

See the [Contribution Guide](https://github.com/doitintl/bigquery-grafana/blob/master/CONTRIBUTING.md).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='90'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1220' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/doitintl/bigquery-grafana#license)License

See the [License File](https://github.com/doitintl/bigquery-grafana/blob/master/LICENSE.md).