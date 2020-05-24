Google's AutoML And BigQuery ML: The Rise Of One-Click Hyperscale Machine Learning

4,892 views|May 28, 2019, 12:20pm

# Google's AutoML And BigQuery ML: The Rise Of One-Click Hyperscale Machine Learning

[![53f0770ab13af971740d1d0d324da1f3](../_resources/aed8b3ef855951b14d5f80e652cabccb.png)](https://www.forbes.com/sites/kalevleetaru/)

[Kalev Leetaru](https://www.forbes.com/sites/kalevleetaru/)Contributor![](data:image/svg+xml,%3csvg class='fs-icon fs-icon--info js-evernote-checked' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60' data-evernote-id='252'%3e%3cpath fill='%23010101' d='M28.3 38.4h3.3v-10h-3.3v10zM30 13.3c-9.2 0-16.7 7.5-16.7 16.7S20.8 46.7 30 46.7 46.7 39.2 46.7 30 39.2 13.3 30 13.3zm0 30.1c-7.4 0-13.4-6-13.4-13.4s6-13.4 13.4-13.4 13.4 6 13.4 13.4-6 13.4-13.4 13.4zM28.3 25h3.3v-3.3h-3.3V25z' data-evernote-id='703' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[AI & Big Data](https://www.forbes.com/ai-big-data)
I write about the broad intersection of data and society.
-
-
-

 [![https://blogs-images.forbes.com/kalevleetaru/files/2018/02/gcp_datacenter_BlueLights_ServerRow-1200x800.jpg](../_resources/329b276e2f8448b55334f359475810d5.jpg)](https://blogs.forbes.com/kalevleetaru/files/2018/02/gcp_datacenter_BlueLights_ServerRow.jpg)

Google Cloud data center (Google)
 Google

Two of the greatest obstacles to getting started with today’s deep learning systems have been the lack of truly “point and click” interfaces to creating new models and the immense complexities in scaling machine learning workflows to the production scales businesses work with. While there are tools that make creating new models more straightforward than writing reams of code, few permit the creation of truly production-grade systems built upon transfer learning from some of the world’s largest training datasets and bleeding edge algorithms and automated tuning workflows. Similarly, building massive scalable robust machine learning pipelines can be done with many different tools today, but the process is far from a point-and-click experience or a few lines of code. Google’s announcements over the last few years offer a glimpse into how the cloud is transforming the AI workflow experience.

Google’s approach to enabling one-click creation of state-of-the-art deep learning models can be seen through in its [AutoML](https://cloud.google.com/automl/) series of products. Today Google’s AutoML range includes [imagery](https://cloud.google.com/vision/), [video](https://cloud.google.com/video-intelligence/), [text](https://cloud.google.com/natural-language/), [translation](https://cloud.google.com/translate/) and even [numeric](https://cloud.google.com/automl-tables/) data. Each product leverages transfer learning to allow customers to build their models directly on top of Google’s massive training and algorithmic investments. In some cases, transfer learning can allow users to build new recognition models with as few as a few dozen examples.

The importance of transfer learning in jump-starting new models with minimal training data cannot be underestimated. One of the most costly and difficult aspects of deep learning and the greatest obstacle to successful implementations is the creation and careful curation of the massive archives of true and counter examples required to train new models. AutoML allows developers to effectively outsource that process to Google, building on top of models trained from its enormous training data investments.

Today In:[Innovation](https://www.forbes.com/ai-big-data)![](data:image/svg+xml,%3csvg class='fs-icon fs-icon--chevron-up js-evernote-checked' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 19.8 19.8' data-evernote-id='253'%3e%3cpath transform='rotate(45.001 12.615 10.187)' d='M7.9 9h9.5v2.4H7.9z' data-evernote-id='740' class='js-evernote-checked'%3e%3c/path%3e%3cpath transform='rotate(134.999 7.586 10.187)' d='M2.8 9h9.5v2.4H2.8z' data-evernote-id='741' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

Yet what makes AutoML so powerful is not just transfer learning. It is the automated workflow for constructing, tuning and optimizing the resulting models. AutoML is not merely a pre-built model ready to be built upon in TensorFlow with reams of code. It is a truly end-to-end automated creation pipeline, accepting a set of training data as input and outputting a final production-grade model without any further developer intervention. Developers do not need any understanding of deep learning concepts nor do they need to write a single line of code. In fact, line of business users could even conceivably begin using these tools to build the predictive, categorical and filtering models they need.

Similarly, scaling machine learning workflows, both training and execution, is increasingly difficult as the data sizes companies wish to analyze continue to grow. Most large companies have invested heavily in loading their data into large warehouses like BigQuery and have highly skilled analytics staff capable of writing complex SQL queries. The problem is that there has still historically been a massive gap between the analytic capabilities available natively in these warehouse platforms and the kinds of complex leading-edge machine learning tools companies wish to apply to them. Building these machine learning workflows requires specialized skillsets and technical architectures that are typically in preciously short demand at most companies.

PROMOTED

Insights - Teradata BrandVoice

 | Paid Program
 [ ###  DeepMap Is Helping Autonomous Cars Find Their Place In The World]()

Insights - Teradata BrandVoice

 | Paid Program
 [ ###  3 Analytics Startups Transforming Healthcare]()

UNICEF USA BrandVoice

 | Paid Program

 [ ###  Torn Apart By Hurricane Irma, A Family Is Still Picking Up The Pieces]()

Much as AutoML has begun to bring point-and-click simplicity to transfer learning and automated model construction, BigQuery has begun addressing the warehouse analytics gap through [BigQuery ML](https://cloud.google.com/bigquery/). Today BigQuery ML offers linear, binary logistic and multiclass logistic regression, along with k-means clustering. Most importantly, utilizing these models requires nothing more than SQL. No external tools, no data export, no specialization with machine learning toolkits. Just the same SQL skills corporate data analysts are already familiar with.

The ability to perform machine learning in-place offers numerous benefits, both in terms of ease of use and scalability and legal compliance in regulated industries that place stringent constraints on data movement outside designated warehouses.

Perhaps where BigQuery ML shines the brightest is its scalability. The ability to run models over entire live datasets, rather than the traditional process of small stale extracts makes it possible for companies to begin performing such ad hoc at-scale machine learning as part of their routine day-to-day business operations, rather than as special-purpose dedicated external pipelines.

Putting this all together, as deep learning is advancing beyond the research lab, cloud companies are steadily lowering the barriers to access to advanced machine learning technologies. The newest generation of point-and-click model creation tools like AutoML and warehouse-scale analytics like BigQuery ML offer a glimpse at a future in which machine learning becomes increasingly democratized.

In the end, the cloud is no longer just a place where AI experts go to pioneer the future or scarce deep learning engineers build exotic solutions. It is increasingly the place AI gets done and increasingly those AI solutions are going to be built by ordinary users harnessing tools like AutoML and BigQuery ML.

[![53f0770ab13af971740d1d0d324da1f3](../_resources/aed8b3ef855951b14d5f80e652cabccb.png)](https://www.forbes.com/sites/kalevleetaru/)

[Kalev Leetaru](https://www.forbes.com/sites/kalevleetaru/)

Based in Washington, DC, I founded my first internet startup the year after the Mosaic web browser debuted, while still in eighth grade, and have spent the last 20 year

...

- [Print]()
- [Site Feedback](https://www.forbes.com/mailto:feedback@forbes.com)
- [Tips](https://www.forbes.com/tips/)
- [Corrections](https://www.forbes.com/mailto:corrections@forbes.com?subject=Report%20Correction%3A%20Kalev%20Leetaru&body=Reporting%20Correction%20for%3A%0A%0ATitle%3A%20Google%27s%20AutoML%20And%20BigQuery%20ML%3A%20The%20Rise%20Of%20One-Click%20Hyperscale%20Machine%20Learning%0AAuthor%3A%20Kalev%20Leetaru%0AURL%3A%20https%3A%2F%2Fwww.forbes.com%2Fsites%2Fkalevleetaru%2F2019%2F05%2F28%2Fgoogles-automl-and-bigquery-ml-the-rise-of-one-click-hyperscale-machine-learning%2F%0A%0A--%0A%0AYour%20Name%3A%0ACorrection%20Request%3A%0A%0A--%0A%0AThank%20you%20for%20reporting%20a%20correction.%20Forbes%20staff%20will%20review%20your%20concern%20shortly.)
- [Reprints & Permissions](https://www.parsintl.com/publication/forbes/)
- [Terms](https://www.forbes.com/terms/)
- [Privacy](https://www.forbes.com/fdc/privacy.html)
- ©2019 Forbes Media LLC. All Rights Reserved.
- [AdChoices](http://preferences-mgr.truste.com/?pid=forbes01)