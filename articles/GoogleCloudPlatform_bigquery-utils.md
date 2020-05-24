GoogleCloudPlatform/bigquery-utils

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='60'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='821' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/bigquery-utils#bigquery-utils)BigQuery Utils

BigQuery is a serverless, highly-scalable, and cost-effective cloud data warehouse with an in-memory BI Engine and machine learning built in. This repository provides useful utilities to assist you in migration and usage of BigQuery.

[![687474703a2f2f677374617469632e636f6d2f636c6f75647373682f696d616765732f6f70656e2d62746e2e737667](../_resources/e31bcb4fb712e12e39c7cdbec8f8894f.png)](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fbigquery-utils.git)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='61'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='825' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/bigquery-utils#getting-started)Getting Started

This repository is broken up into:

- [Scripts](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/scripts) - Python, Shell, & SQL scripts
    - [billing](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/scripts/billing) - Example queries over the GCP billing export
- [UDFs](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/udfs) - User-defined functions for common usage as well as migration
    - [community](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/udfs/community) - Community contributed user-defined functions
    - [teradata](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/udfs/migration/teradata) - UDFs which mimic the behavior of proprietary functions in Teradata
- [Views](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/views) - Views over system tables such as audit logs or the`INFORMATION_SCHEMA`
    - [query_audit](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/views/audit/query_audit.sql) - View to simplify querying the audit logs which can be used to power dashboards ([example](https://codelabs.developers.google.com/codelabs/bigquery-pricing-workshop/#0)).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='62'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='839' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/bigquery-utils#public-udfs)Public UDFs

All UDFs within this repository will be automatically created under the `bqutil` project under publicly shared datasets. Queries can then reference the shared UDFs via `bqutil.<dataset>.<function>()`.

[![public_udf_architecture.png](../_resources/9f751584d4cf250bfb6be74bbc21cba6.png)](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/images/public_udf_architecture.png?raw=true)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='63'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='843' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/bigquery-utils#contributing)Contributing

See the contributing [instructions](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/CONTRIBUTING.md) to get started contributing.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='846' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/bigquery-utils#license)License

All solutions within this repository are provided under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license. Please see the [LICENSE](https://github.com/GoogleCloudPlatform/bigquery-utils/blob/master/LICENSE) file for more detailed terms and conditions.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='65'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='849' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/bigquery-utils#disclaimer)Disclaimer

This repository and its contents are not an official Google Product.