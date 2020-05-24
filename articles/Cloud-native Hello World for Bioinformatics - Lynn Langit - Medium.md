Cloud-native Hello World for Bioinformatics - Lynn Langit - Medium

# Cloud-native Hello World for Bioinformatics

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='141' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='142' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*9RqVKz62VSoJ8ZcMWHI1AA.jpeg](../_resources/1ace5dcb106b8aac5286a5d2978abbb3.jpg)](https://medium.com/@lynnlangit?source=post_page-----d21458a0013f----------------------)

[Lynn Langit](https://medium.com/@lynnlangit?source=post_page-----d21458a0013f----------------------)

[Jan 2](https://medium.com/@lynnlangit/cloud-native-hello-world-for-bioinformatics-d21458a0013f?source=post_page-----d21458a0013f----------------------) · 7 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='161'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='162' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/d21458a0013f/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='165'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='166' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/d21458a0013f/share/facebook?source=post_actions_header---------------------------)

PART FOUR — Toward Serverless Pipelines with GCP

In the series to date, I’ve presented the general rationale for building quick start examples (or ‘Hello World’) for bioinformatics tools in [part one](https://medium.com/@lynnlangit/cloud-native-hello-world-for-bioinformatics-9cfabf2dd389).

In [part two](https://medium.com/@lynnlangit/cloud-native-hello-world-for-bioinformatics-53ecbcb9631b), I reviewed one such example for the VariantSpark library, runnable via smart templates in the AWS Marketplace.

In [part three](https://medium.com/@lynnlangit/cloud-native-hello-world-for-bioinformatics-7831aecc8d1a), I covered how to convert a locally runnable example to a reusable cloud example, by working with Google Cloud Platform custom Virtual Machine images running on Google Compute Engine.

In this part four, I will explore current work I am doing with a research group. In particular, I’ll cover some recent work on preparing researchers to work ‘cloud-natively.’

## What is a Cloud Native Data Pipeline?

In a word — it’s *‘serverless.’* Why? Because using scalable cloud services (via API endpoints) rather than creating, configuring and maintaining docker container or virtual machine images and their orchestration systems is simpler.

So, if this is the case, then why I have not covered serverless Hello World bioinformatics pipeline patterns yet in this series? To date I’ve only written about cloud-based Infrastructure as a Service (GCP GCE Virtual Machines) or Platform as a Service (AWS EMR). Why is that?

Serverless pipelining is indeed seductive, but also elusive…how do we get there from the current world of on-premise HPC clusters? What should the Hello World for cloud-native pipelining look like?

Of note is that despite work I’ve done with researchers to preview serverless pipeline examples — even using bioinformatics data — adoption of those serverless pipelining services remains low. In considering possible reasons for this, I was reminded [via work with my graduate students interns] that recent university Computer Science graduates are not taught the SQL query language (or anything about databases) in their CS courses at university. I assume this lack of familiarity with database concepts extends to bioinformatics researchers as well.

## Google Cloud BigQuery

BigQuery, a serverless SQL cloud service, has been available since 2011. Its scalable, pay-by-data-scanned serverless model seems perfect for variable, bursting genomics analysis pipelines. So why isn’t BigQuery (or other comparable services, such as AWS Athena) being widely used in genomic analysis pipelines?

The answer appears to be the query language — SQL. Although in many (most?) verticals I had previously worked in (i.e. fintech, adtech, gov’t….) relational databases and associated SQL queries have been pervasive for many years, bioinformatics research appears to differ.

Researchers, in my experience, use files (not data tables) and programming languages, such as R, Python or even Java, to build their data pipelines. While patterns such as cloud-based VM images or customized docker container and pipeline languages (such as Nextflow, CWL or WDL) are being used to move on premise (mostly HPC) genomics workloads to the cloud, I wonder…

> Could we move faster with serverless SQL?

Although I don’t have a large number of data points about the effectiveness of the serverless pattern for genomics, I do have some. In work that I’ve done with Dr. Denis Bauer and her team at CSIRO Bioinformatics in Sydney, Australia, they’ve had [multiple successes using serverless](https://bioinformatics.csiro.au/blog/converting-traditional-architecture-to-cloud-native-applications/) design patterns.

However, even they aren’t using BigQuery yet. Why not? I wondered.

## SQL for Bioinformatics

In summer 2019, I created an open source course on GitHub [‘gcp-for-bioinformatics’](https://github.com/lynnlangit/gcp-for-bioinformatics). Subsequently, I’ve received positive feedback from several research groups on this course. This course is based on my popular general introductory GCP course, hosted on Linked In Learning (‘[GCP Essential Training](https://www.linkedin.com/learning/google-cloud-platform-essential-training-3).’)

The difference between my LinkedIn GCP course and my Open Source GCP course is that the open source course uses sample data and example solutions specific to bioinformatics/genomics. For example in the open source course, I use .fasta, .bam, .vcf, etc.. files, rather than .csv, etc..

I looked around for an example course which would explain SQL query concepts using bioinformatics data. I found [this one](https://en.wikibooks.org/wiki/Data_Management_in_Bioinformatics/SQL_Exercises). Although it’s a good start, I felt like there were a number of limitations in this course. The first of which was that the example queries were too complex, lumping too many concepts together. Also there was no implementation (database set up) provided.

As a next step I considered, what would it look like to use this bioinformatics SQL course in a cloud-native way. The natural answer was to modify the course to work with Google Big Query. I thought it would be trivial to ‘covert’ the course for this purpose. Actually doing this though, took a bit longer…

## It’s the Data

The sample includes 5 ‘tables’ populated with a very small amount of data. Shown below is a screen capture of a portion of the example data. It’s a point key that this example data is very domain-specific to genomics.

![1*7qufmmUZS2vBnb14Gv4-QQ.png](../_resources/c38008f477ee84a1d8dcee5de61d0e38.png)
![1*7qufmmUZS2vBnb14Gv4-QQ.png](../_resources/ca9c48a80e5b3d183cf839cd8d23232b.png)

Bioinformatics source data from wikibooks example at https://en.wikibooks.org/wiki/Data_Management_in_Bioinformatics/SQL_Exercises

I wanted to use the Google BigQuery [**‘auto detect schema’**](https://cloud.google.com/bigquery/docs/schema-detect) feature to quickly convert this information to BigQuery dataset tables. First, I scraped and saved the data as local CSV files. Although I was eventually able to get this feature to work, I had to make a number of changes to the files. Changes included the following:

- remove the second line ‘ — — — ‘
- remove all leading & trailing white space in column names
- remove all leading & trailing white space in columns with string data
- add a numeric data column to table with only string columns

Once I made these changes, I was able to quickly upload the resulting CSV files to create tables in my BigQuery dataset. Next I wanted to make my dataset public so that it could be used in a tutorial. To do this, I clicked the ‘Share Dataset’ button and added `allUsers` and `allAuthenticatedUsers` to the **BigQuery Dataset Viewer** permissions for this dataset. The dataset is shown below in the BigQuery Web UI.

![1*pTH65CQePGLr6VA4W_aEzg.png](../_resources/3d04ca60f255d0ca5e05e249f96daf07.png)
![1*pTH65CQePGLr6VA4W_aEzg.png](../_resources/c8fa6ebde4256afc82f43c72e967432c.png)
Creating the public dataset example

## Testing the queries

In the next step of the course conversion, I began to test the query “answers” provided in the original sample. The first change I needed to make was to alter queries to fully qualify all references to the example tables (or views) in my public BigQuery dataset. I did this by updating the FROM portion of each SQL statement. To fully qualify an object in BigQuery, use this pattern <projectName>.<datasetName>.<tableOrViewName>.

This update was required due to the need for students who use my tutorial to be able to access my (public) dataset from within *their own GCP project*. The required change to each query looked like this:

OLD: SELECT * FROM experiments

NEW: SELECT * FROM `gcp-for-bioinformatics.sql_genomics_examples.experiments` AS experiments

Next I added more intermediate queries to better level the learning by providing examples that added concepts more gradually than the original example queries. Sometimes I just ‘broke apart’ the original answer queries, other times I re-wrote for clarity. I also changed the source data to make the results more meaningful.

## Adding Visuals

In teaching standard SQL syntax to hundreds of classroom students in the past, I found students benefited from visuals — particularly when they were learning JOIN queries. So I next created two quick reference charts. One for SQL Keywords and one for SQL JOIN queries. I tested the effectiveness of these charts, by posting them on Linked In. I got a quick positive response. For reference, these charts are shown below.

![1*UzSipt9_Eyc0PxZhFl9HaA.png](../_resources/aad19eb6e5740ea3bc0729e32837fb8e.png)
![1*UzSipt9_Eyc0PxZhFl9HaA.png](../_resources/aa3fa85eef67738b367d784f132f44d0.png)
SQL Keywords
![1*x4-hWcDbepg8d-vF63a4JA.png](../_resources/34787dae1d0a3361bbcba62cfb7221df.png)
![1*x4-hWcDbepg8d-vF63a4JA.png](../_resources/7ad85d72bbe22f63f37e350f20c07b85.png)
SQL JOIN Concepts

Next I added some screenshots of the tables involved in various types of joins — self-joins, two-table joins, etc.. You can see that in my screenshots, I took the time to highlight the table join columns. I’ll include one example below.

![1*UlXQexVIQzVTiypdAuulLg.png](../_resources/0bb6a99eb90e0057899072593246ca77.png)
![1*UlXQexVIQzVTiypdAuulLg.png](../_resources/77ed698631234940c00a8d65d4b5bf4f.png)
Illustrating a two-table SQL Join

As I continued to test all of the original queries, I noticed that some of the potential answers either weren’t supported, weren’t recommended (correlated subqueries) or didn’t work as written (EXCEPT syntax slightly differed) in BigQuery. So I updated those queries.

Additionally, I updated a couple of data points and query questions to make the flow a bit more natural (and pattern-based). Also I removed some redundant (and needlessly complex) content.

## Finishing Up

Then I added a short *‘how-to-get-started-with-BigQuery’ *section at the beginning of my tutorial with the goal of getting students running their first query within minutes of starting the tutorial. I also added some *‘learning more’* links at the end.

Finally, I pulled out all of the potential answers to the SQL Query questions in the document into a separate ‘answers’ file and linked the answers in the tutorial. I also added a *‘what could go wrong?*’ section at the beginning, explaining and showing the function of the query validator in the BigQuery query window.

At this point, I’ll release v1 of my ‘cloud-native-SQL’ tutorial with the name [“BigQuery Bioinformatics SQL Query Lessons”](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/1_Files_%26_Data/SQL-queries/SQLQuestions.md) (beginning of course shown below). I am considering creating a Jupyter notebook as well, but want to get more feedback.

![1*k_85EAb1nyVoQbBMlp4kaQ.png](../_resources/4f6627f566bf8b5cd1748c330d6a788b.png)
![1*k_85EAb1nyVoQbBMlp4kaQ.png](../_resources/6333ae428a45c2125db1533ca540ce6d.png)
Beginning of my revised (cloud-native) Hello World tutorial

Over the years, I’ve had a number of people ask me about the process I use to create ‘Hello World’ content. In writing this short article, I wanted to provide a view into the type of work I do when updating/creating technical content at this level.

Also, and this is a key point — the testing, organization and clarity that I added to the original lessons are aimed to improve the **usability** of the tutorial. The entire point of HelloWorld is this, right?

> If they can’t use it, it’s worthless
How did I do? Feedback welcomed.