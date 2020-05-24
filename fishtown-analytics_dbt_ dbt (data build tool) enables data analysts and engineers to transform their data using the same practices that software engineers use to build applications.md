fishtown-analytics/dbt: dbt (data build tool) enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

 [![dbt-horizontal.png](../_resources/073b8f73fe56a90303457d0dbef74891.png)](https://github.com/fishtown-analytics/dbt/blob/master/etc/dbt-horizontal.png?raw=true)

 [![68747470733a2f2f636f6465636c696d6174652e636f6d2f6769746875622f66697368746f776e2d616e616c79746963732f6462742f6261646765732f6770612e737667](../_resources/4b1a376cecaabf2fac85684e07732335.png)](https://codeclimate.com/github/fishtown-analytics/dbt)  [![68747470733a2f2f636972636c6563692e636f6d2f67682f66697368746f776e2d616e616c79746963732f6462742f747265652f6d61737465722e7376673f7374796c653d737667](../_resources/bf434b8e7fbc2c72bf22944000693d1d.png)](https://circleci.com/gh/fishtown-analytics/dbt/tree/master)  [![68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f763031727764337139316a6e7770396d2f6272616e63682f646576656c6f706d656e743f7376673d74727565](../_resources/c241c28aa0a0d4586acb5fd42799d37b.png)](https://ci.appveyor.com/project/DrewBanin/dbt/branch/development)  [![68747470733a2f2f736c61636b2e6765746462742e636f6d2f62616467652e737667](../_resources/9395826c1671ef3e64c5a65c8f498035.png)](https://slack.getdbt.com/)

**[dbt](https://www.getdbt.com/)** (data build tool) enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

[![dbt-arch.png](../_resources/65b0afa9ef1e802c788b7f6c77f1130e.png)](https://github.com/fishtown-analytics/dbt/blob/master/etc/dbt-arch.png?raw=true)

dbt can be used to [aggregate pageviews into sessions](https://github.com/fishtown-analytics/snowplow), calculate [ad spend ROI](https://github.com/fishtown-analytics/facebook-ads), or report on [email campaign performance](https://github.com/fishtown-analytics/mailchimp).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='99'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1183' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/fishtown-analytics/dbt#understanding-dbt)Understanding dbt

Analysts using dbt can transform their data by simply writing select statements, while dbt handles turning these statements into tables and views in a data warehouse.

These select statements, or "models", form a dbt project. Models frequently build on top of one another – dbt makes it easy to [manage relationships](https://docs.getdbt.com/docs/ref) between models, and [visualize these relationships](https://docs.getdbt.com/docs/documentation), as well as assure the quality of your transformations through [testing](https://docs.getdbt.com/docs/testing).

[![dbt-dag.png](../_resources/69e8e4e96c7efaaf3547983c3d67960d.png)](https://github.com/fishtown-analytics/dbt/blob/master/etc/dbt-dag.png?raw=true)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='100'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1188' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/fishtown-analytics/dbt#getting-started)Getting started

- [Install dbt](https://docs.getdbt.com/docs/installation)
- Read the [documentation](https://docs.getdbt.com/).
- Productionize your dbt project with [dbt Cloud](https://www.getdbt.com/)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='101'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1194' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/fishtown-analytics/dbt#find-out-more)Find out more

- Check out the [Introduction to dbt](https://dbt.readme.io/docs/introduction).
- Read the [dbt Viewpoint](https://dbt.readme.io/docs/viewpoint).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='102'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1199' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/fishtown-analytics/dbt#join-thousands-of-analysts-in-the-dbt-community)Join thousands of analysts in the dbt community

- Join the [chat](http://slack.getdbt.com/) on Slack.
- Find community posts on [dbt Discourse](https://discourse.getdbt.com/).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='103'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1204' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/fishtown-analytics/dbt#reporting-bugs-and-contributing-code)Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know on [Slack](http://slack.getdbt.com/), or open [an issue](https://github.com/fishtown-analytics/dbt/issues/new).
- Want to help us build dbt? Check out the [Contributing Getting Started Guide](https://github.com/fishtown-analytics/dbt/blob/dev/barbara-gittings/CONTRIBUTING.md)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='104'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/fishtown-analytics/dbt#code-of-conduct)Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).