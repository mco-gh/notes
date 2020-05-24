3 Great Options for Persistent Storage with Cloud Run

# 3 Great Options for Persistent Storage with Cloud Run

[![0*vZQScZPEM5ke_9Sf.jpeg](../_resources/123dc6d98e0ea4898a851cdbcbaf196e.jpg)](https://medium.com/@granttimmerman?source=post_page-----f1581ee05164----------------------)

[Grant Timmerman](https://medium.com/@granttimmerman?source=post_page-----f1581ee05164----------------------)

[Jan 13](https://medium.com/google-cloud/3-great-options-for-persistent-storage-with-cloud-run-f1581ee05164?source=post_page-----f1581ee05164----------------------) · 2 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='192'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/f1581ee05164/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='196'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/f1581ee05164/share/facebook?source=post_actions_header---------------------------)

![1*DXgJRJt9Q0Moo2t4RgBrEg.png](../_resources/3c057b66eeb4ceb418f0c391e5ba79c3.png)
![1*DXgJRJt9Q0Moo2t4RgBrEg.png](../_resources/f1ebc0c00eff4843f95cc4ae0dcd36cc.png)
Cloud Run with Cloud Storage, Cloud Firestore, and Cloud SQL

Cloud Run is a managed compute platform that automatically scales your **stateless containers**. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most — building great applications.

However, most applications are **stateful**. As a developer, how can you permanently store images, database records, and other pieces of data?

In this article, we’ll discuss 3 example ways in which you can store data on Google Cloud Platform with Cloud Run.

# Storage with Google Cloud

There are a variety of ways to store data on Google Cloud, depending on your application’s needs. In this imaginary application, let’s create a e-commerce shoe store. Here are three storage options we’ll use for storing different kinds of data:

## Cloud Storage

For storing **files/objects **such as images and video, or archival backups, [Google Cloud Storage](https://cloud.google.com/storage/docs) is an excellent option for this type of data. Here’s an example code snippet in Node that can be used with Cloud Run:

|     |     |
| --- | --- |
| 1   | // Imports the Google Cloud client library |
| 2   | const  {Storage}  =  require('@google-cloud/storage'); |
| 3   |     |
| 4   | // Creates a client |
| 5   | const  storage  =  new  Storage(); |
| 6   |     |
| 7   | async  function  uploadFile(req,  res)  { |
| 8   |  // Uploads a local file to the bucket |
| 9   |  await  storage.bucket(res.query.bucket).upload(req.query.filename,  { |
| 10  |  // Support for HTTP requests made with `Accept-Encoding: gzip` |
| 11  |  gzip: true, |
| 12  |  // By setting the option `destination`, you can change the name of the |
| 13  |  // object you are uploading to a bucket. |
| 14  |  metadata: { |
| 15  |  // Enable long-lived HTTP caching headers |
| 16  |  // Use only if the contents of the file will never change |
| 17  |  // (If the contents will change, use cacheControl: 'no-cache') |
| 18  |  cacheControl: 'public, max-age=31536000', |
| 19  |  }, |
| 20  |  }); |
| 21  |     |
| 22  |  console.log(`${filename} uploaded to ${bucket}.`); |
| 23  | }   |

 [view raw](https://gist.github.com/grant/62edeae5ffdb5f6ca328209f54f948ab/raw/7b277172a355083db01076a08cff42ec0b092ecf/index.js)  [index.js](https://gist.github.com/grant/62edeae5ffdb5f6ca328209f54f948ab#file-index-js) hosted with ❤ by [GitHub](https://github.com/)

Uploading a file to Google Cloud Storage

## Cloud Firestore

For storing **unstructured** data, or creating a flexible, NoSQL, cloud database, [Cloud Firestore](https://firebase.google.com/docs/firestore) is a great solution for mobile, web, and server development. In this sample, we want to store flexible JSON objects for shoe data:

|     |     |
| --- | --- |
| 1   | // Create a Firebase client |
| 2   | const  admin  =  require('firebase-admin'); |
| 3   | admin.initializeApp({ |
| 4   |  credential: admin.credential.applicationDefault() |
| 5   | }); |
| 6   |     |
| 7   | const  db  =  admin.firestore(); |
| 8   | async  function  uploadDoc(req,  res)  { |
| 9   |  // Create a reference to the shoes doc. |
| 10  |  let  shoesDoc  =  db.collection('products').doc('shoes'); |
| 11  |  // Add a shoe |
| 12  |  shoesDoc.set({ |
| 13  |  name: 'gshoe', |
| 14  |  size: 11.5, |
| 15  |  colors: ['blue',  'red',  'yellow',  'green'] |
| 16  |  }); |
| 17  | }); |

 [view raw](https://gist.github.com/grant/22e37ee1534271208d83007aba69db39/raw/1aad42dbe3210295cefedfb000fa3d07074dbba1/index.js)  [index.js](https://gist.github.com/grant/22e37ee1534271208d83007aba69db39#file-index-js) hosted with ❤ by [GitHub](https://github.com/)

Adding a doc/JSON record to Firestore

## Cloud SQL

For storing **structured** data in a RDBMS, such as MySQL, PostgreSQL, and SQL Server, [Cloud SQL](https://cloud.google.com/sql/) can connect to a nice interface for storing and querying your data. Here created a customer table where we can use familiar SQL to create powerful queries:

|     |     |
| --- | --- |
| 1   | const  mysql  =  require('promise-mysql'); |
| 2   |     |
| 3   | // Create a pooled connection to MySQL |
| 4   | let  pool; |
| 5   | const  createPool  =  async  ()  =>  { |
| 6   |  pool  =  await  mysql.createPool({ |
| 7   |  user: process.env.DB_USER,  // e.g. 'my-db-user' |
| 8   |  password: process.env.DB_PASS,  // e.g. 'my-db-password' |
| 9   |  database: process.env.DB_NAME,  // e.g. 'my-database' |
| 10  |  // If connecting via unix domain socket, specify the path |
| 11  |  socketPath: `/cloudsql/${process.env.CLOUD_SQL_CONNECTION_NAME}`, |
| 12  |  // If connecting via TCP, enter the IP and port instead |
| 13  |  // host: 'localhost', |
| 14  |  // port: 3306, |
| 15  |     |
| 16  |  //... |
| 17  |  }); |
| 18  | };  |
| 19  | createPool(); |
| 20  |     |
| 21  | async  function  readCustomers(req,  res)  { |
| 22  |  // Get the 5 newest customers. |
| 23  |  const  customers  =  await  pool.query( |
| 24  |  'SELECT id, name FROM customers ORDER BY id DESC LIMIT 5' |
| 25  |  ); |
| 26  |  res.send({ customers }); |
| 27  | }   |

 [view raw](https://gist.github.com/grant/5b841fbbff9775228d56ba27c6727830/raw/89c7f9b1070ddeb10383d48434015d95d13578cd/index.js)  [index.js](https://gist.github.com/grant/5b841fbbff9775228d56ba27c6727830#file-index-js) hosted with ❤ by [GitHub](https://github.com/)

Reading from a Cloud SQL table

> Note: See > [*> Connecting to Cloud SQL from Cloud Run (fully managed)*](https://cloud.google.com/sql/docs/mysql/connect-run)>  for full documentation on how to connect and use these services together.

Those are 3 storage options for storing data in GCP. Other products include [Cloud Filestore](https://cloud.google.com/filestore/), [Cloud Storage for Firebase](https://firebase.google.com/docs/storage), and [Cloud Memorystore](http://cloud%20memorystore/) among [other databases](https://cloud.google.com/products/databases/).

# Other Tips

Sometimes your data storage could use more configuration. Here are two tips:

- Cloud Run’s **“Max Instances”** feature can limit the number of instances handling running your service. This, in turn, can rate limit the number of requests to your storage service. [Read more](https://cloud.google.com/run/docs/configuring/max-instances).
- **Cloud Tasks** with rate limits per queue can be placed in front of a Cloud Run service to smooth out rapid or jerky requests. [Read more](https://cloud.google.com/tasks/).

# References

Thanks for reading. If you are looking for more reading about storing data with GCP, are some links:

- [Solution: Google Cloud’s Data Management Products](http://cloud.google.com/solutions/data-management)
- [Tutorial: Processing Images with Cloud Run and Cloud Storage](https://cloud.google.com/run/docs/tutorials/image-processing)