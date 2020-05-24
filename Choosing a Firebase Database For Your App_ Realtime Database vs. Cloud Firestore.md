Choosing a Firebase Database For Your App: Realtime Database vs. Cloud Firestore

# Choosing a Firebase Database For Your App: Realtime Database vs. Cloud Firestore

[Development](https://savvyapps.com/blog/topics/development)[Tips](https://savvyapps.com/blog/topics/tips)

Over the last few years Firebase has seen success with what's now called its [Realtime Database](https://firebase.google.com/docs/database/), a tool that allows developers to set up and provision a back-end database as a service more easily. For example, we previously shared our experience at Savvy Apps with Realtime Database on [Google's Firebase blog](https://firebase.googleblog.com/2017/09/sprynt-launches-eco-friendly-free.html) for our work with [Sprynt](https://savvyapps.com/work/sprynt). Developers continue to choose Realtime Database because of its low barrier of entry, low maintenance costs, and fast queries. The system certainly isn't without its drawbacks, however, leading to others looking at alternatives to Firebase.

Firebase sought to attract a wider audience with their release of a separate backend named [Cloud Firestore](https://firebase.google.com/docs/firestore/). While Cloud Firestore supports many features that Realtime Database developers have been wanting for years, it's not a pure “version 2.0.” Instead it's a totally different architecture that focuses on different priorities like complex querying and data integrity.

Savvy has had the chance to work with both systems in fully-operational, real-world environments and we want to share what we've learned working with both of these services. We'll cover in detail the differences, strengths, and weaknesses of each, as well as what updates Firebase released for both since they announced Cloud Firestore. We hope this guide will help you evaluate the use of Realtime Database or Cloud Firestore in projects of your own.

*Want to jump straight to our conclusions to find out which platform is right for you? Go straight to our summary of the [pros and cons of using Realtime Database vs. Cloud Firestore](https://savvyapps.com/blog/firebase-realtime-database-vs-cloud-firestore-for-your-app#realtime-database-vs-cloud-firestore-a-pros-cons-summary).*

## Getting to Know Realtime Database and Cloud Firestore

Before we discuss the differences, let's lay down the basics. We'll cover the core features of Realtime Database and Cloud Firestore first to make it easier to draw a meaningful comparison between the two.

### What You Should Know About Realtime Database

Realtime Database is a cloud-hosted [NoSQL](https://www.mongodb.com/nosql-explained) database with SDK support for iOS, Android, and the web. It easily integrates with Firebase's other tools for authentication, file storage, analytics and others. This tool stores data in JSON documents, so everything is either a key or a value. Data synchronization uses web sockets, allowing for very snappy transactions. Realtime Database also handles updates for you when a device is offline, syncing changes for you when the network reconnects.

Developers love how quickly they can set up a Realtime Database backend and not have to worry about things like deployments, hardware, uptime, and scalability. You can have a pretty robust backend server running in just a few minutes, letting you focus on the fun and unique parts of your app.

Realtime Database requires you to write most of your system's application code on the client. This approach could be a positive or negative aspect depending on how you look at it. You have to handle most logic in your client applications, which means duplicating code across Android, iOS, and web unless you build a Firebase Cloud Function to handle requests. If you do that, though, you lose out on a lot of the built-in Realtime SDK features.

This client logic also requires you to write your own data validation. Realtime Database has no concepts of data types. It will let you save values as strings or numbers, or nested objects and arrays of strings and numbers to any field you want. The arrays, however, are really just objects with indices used as keys. It's completely up to you to manage these data types yourself.

Queries fire and respond in near real time using Realtime Database, and it works beautifully. That is, as long as you've thoroughly planned out your data structure in a way to support all the queries you want to make, and will ever want to make, in your apps. That's no small feat. Even though it's fast, Realtime Database only supports queries on one field. Many users were disappointed to find that querying for data does not support many of the features developers are accustomed to using in more traditional relational databases.

Realtime Database's suggested solution to this is flattening and denormalizing data. This is easier said than done when you need to track all of the locations a data element was copied into in case that data element ever gets updated. It's also difficult when supporting brand new features down the road without having to massively refactor your existing data schema.

### What You Should Know About Cloud Firestore

We can start to see why Realtime Database isn't a favorable solution for everybody. So what did Firebase do differently when designing Cloud Firestore?

Cloud Firestore is the newer “flagship” database that leans more in the direction of traditional relational schema hierarchy. The NoSQL database is organized into collections. These collections hold documents, which hold more collections (subcollections) and data fields. A document is a single JSON object structure that can hold nested subcollections of more documents or key-value pairs of data. Collections and documents can roughly be thought of as tables and rows in a relational database, since that's typically how you'll be using them.

The fields inside a document now have types (yay!) including strings, numbers, boolean, objects, arrays, null values, date timestamps, geopoints, and shallow references to other documents. This alone is a huge benefit for developers managing data integrity and catching bugs related to mismatching types. References can also help circumvent some data denormalization, reducing the number of locations you'll need to manage duplicated data. While you cannot query across subcollections or inside references, you can use these references to directly fetch a local document's related data.

Cloud Firestore also offers more robust querying support than Realtime Database. We'll dive more into this later.

## What Realtime Database and Cloud Firestore Have in Common

Given that Realtime Database and Cloud Firestore are both Firebase products, it's not surprising that they have a lot in common. Both are easy to include in a project with very few setup steps. They both tie in nicely with Firebase's suite of other services, including each other. With one Firebase project, you can set up both a Realtime Database and Cloud Firestore for your clients to leverage. Other services include file storage, Cloud Functions, authentication, crash reporting, analytics, and [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/). We've successfully used all of these tools on various projects over the years, and most of these features can be used standalone without a Realtime Database or Cloud Firestore database, if desired.

Both platforms also expose their data to admin users via the Firebase Console. The console follows the same paradigm in both databases, and allows you to browse top level nodes/collections and drill down into your data until you find what you're looking for. Neither platform allows for much more exploration than that. It's useful in situations when you know the keys of the objects you want to see and can jump to them directly. Realtime Database and Cloud Firestore allow you to add/edit/delete data (and specify types in Cloud Firestore), which is handy when you're starting out.

Realtime Database and Cloud Firestore focus on speed and efficiency. They allow you to easily set up listeners that can trigger either cloud code or local client code when important data is modified, giving users lightning-fast updates. These updates can even be made offline and synchronized.

You can also combine several important operations together into batches or transactions. These are important for ensuring multi-step processes don't leave your data in bad shape if they fail halfway through. Last but not least, both implement security through Firebase Rules, which is simply a configuration document that determines what locations have restricted read/write permissions.

## Key Differences Between Realtime Database and Cloud Firestore

Next we'll tackle the important factors and differences you'll need to consider when evaluating these two solutions.

### Querying Support

Arguably the biggest enhancement over Realtime Database is Cloud Firestore's more robust querying support. Where Realtime Database queries only allow for a single sorting parameter or condition to fetch on, Cloud Firestore allows you to find records matching multiple field comparisons. The comparison operators Cloud Firestore uses are >, >=, ==, =<, <.

While some compound queries require indexes, Cloud Firestore can create these (with some work required by you). If you attempt to execute a query that requires an index, the query will fail, but it will give you a URL to give the Firebase Console to generate the index. It would be nice if this was more streamlined, because running API queries you know will fail and then copying and pasting the URLs one at time is not fun, but neither is creating each index manually. Also, although arrays are now a first-class data type, querying arrays is still not supported out of the box.

Due to Realtime Database's simplistic data structure, you can run queries looking for fields that begin with your query (or end with your query if you store a set of your strings in reverse). This is not supported in Cloud Firestore. Instead, you will have to use one of the aforementioned comparison operators (e.g. > or >=) in your query, which may or may not be equivalent depending on the data you're fetching. The most obvious use case for this feature in Realtime Database is responsive search results for users typing into a search field for something they are particularly interested in. Where this feature works great with one line of code in Realtime Database, you'll have to write some more intricate search functions when looking for straightforward prefix matching on Cloud Firestore.

### Importing/Exporting Data

One terrific feature Realtime Database provides that is missing from Cloud Firestore is an easy way to import/export data (via simple JSON files) in the Firebase Console. This feature is helpful when migrating data, for example from a development environment to staging environment. It also can be a useful tool when non-developers need to add/edit data in the database quickly; no need for scripts or an API, just a couple button clicks and you can upload totally new datasets for your app to consume.

Alternatively, you can take advantage of a neat [announcement](https://firebase.googleblog.com/2017/12/read-and-write-your-realtime-database.html) that Realtime Database made recently: the ability to use the Firebase Command Line Interface (CLI) tools to script and automate data migrations and querying. With the CLI tools, you won't have to worry about using the limited Console dashboard very often at all.

Unfortunately, in Cloud Firestore, admins are stuck adding/editing/deleting documents, collections and fields one by one in the console. You can mitigate this with a few set up steps configuring the RESTful API or Cloud Functions in Cloud Firestore, but that's extra work you'd have to be willing to take on.

### Real-Time Updates

As we mentioned earlier, Realtime Database's primary focus is on real-time updates via web sockets, which is a great way to handle user presence in social or collaborative apps. Realtime Database gives developers the tools they need to determine which users are actively online using the app in real time. Although Cloud Firestore can set up data listeners, detecting presence is not supported in Cloud Firestore natively and will require Realtime Database to implement a solution.

### Cost Structure

Don't forget to consider the differences in each platform's cost structure and how that relates to the data architecture you'll need in your app. You can see the [full breakdown in pricing here](https://firebase.google.com/pricing/), but there's more you should consider.

The main takeaway is that Realtime Database costs increase with the total amount of data you send via database read/write operations, regardless of how many API calls that may take. Cloud Firestore costs increase for every API call you make, regardless of how much data you send/receive. This means that if you're planning on having lots of small transactions like location updates or live chat messages, you'll favor using Realtime Database. On the other hand, if you plan on making more traditional RESTful requests where the app makes fewer calls with larger responses, you'll prefer Cloud Firestore.

Luckily, these use cases match up with the preferable cost structure. There is one caveat to each platform, however, that you may need to consider. Every query you make with Realtime Database is a deep query. This means it will return all nested child nodes and all of their child nodes, etc. So you need to carefully plan your architecture to avoid pulling unnecessary data repeatedly as well as paying for that data transfer with every query. On the flip side, every query you make in Cloud Firestore is shallow, returning only top level data and references. This requires you to make subsequent API calls (and incur subsequent charges per call) for nested data. The tiered plans are quite generous for both databases, so while it may not matter immediately, you should consider them for long-term success with your app.

### Data Structure

With the cost structures for both solutions in mind, you're almost always aiming to design a flat, denormalized data structure in Realtime Database. This structure will let your app focus on lots of small, fast real-time queries that will impress your users.

Cloud Firestore will not match the speed of Realtime Database, even with its own real-time listeners. The tradeoff is that Cloud Firestore will give you improved query support, reference data types, shallow queries, and the collection-document-subcollection paradigm allowing you to nest data freely while keeping a normalized data. This improves scalability without reducing performance as might happen in Realtime Database when trying to manage every instance of a de-normalized entity.

There's a caveat, though. You cannot query across subcollections in Cloud Firestore, preventing you from nesting everything you might want to. This means you must execute your query on a single collection or subcollection and cannot look across documents for values of nested fields. For this reason, you'll probably still keep a relatively flat data structure in Cloud Firestore too.

### Working with the SDKs

Another important distinction to note is that most developers will feel more at home using the Cloud Firestore SDK rather than the Realtime Database SDK. Since collections and documents will feel more familiar to developers with a SQL background, creating and executing Cloud Firestore queries will come more naturally than working with Realtime Database's listeners.

Writing your queries for Realtime Database will require some planning and new mindset. This is because every query in Realtime Database is a listener, which can be fired once and closed or fired once and kept open for future updates. The listener will always fire immediately with a response of the current state of the results, which may not always be what you want, leading to some gymnastics of ignoring the results you don't care about but responding to the new updates you do care about. Keeping a heavily denormalized dataset in Realtime Database also means preparing for when the situations when seemingly simple updates made by users will have to trigger a multitude of other updates to copies of that data in other nodes across your database.

### Tried and True Versus New and Shiny

Finally, it may be obvious but worth mentioning that these two products are at different stages of their lifecycles. Realtime Database has been around for years and thoroughly vetted by developers in many successful projects. It's received many important updates and additions over time, as well as regular bug fixes and enhancements. Cloud Firestore, on the other hand, is only six months old as of March 2018 and still in beta.

In those six months, we've seen some cool new features on the Realtime Database side including [multi-database sharding](https://firebase.googleblog.com/2017/11/easier-scaling-with-multi-database.html) and [security enhancements](https://firebase.googleblog.com/2018/01/introducing-query-based-security-rules.html), but updates to Cloud Firestore have been almost exclusively dedicated to bug fixing. This is only natural, and it will likely take some time before they start making large feature improvements to Cloud Firestore at the same rate as Realtime Database.

## What's Missing From Both Realtime Database and Cloud Firestore?

Before you rush off to build your next Firebase app, let's touch on some of the features that neither Realtime Database nor Cloud Firestore currently support. We mentioned that Cloud Firestore improved querying support, but it still has a long way to go to compete with the query options you'd get in a SQL database framework.

You'll notice that both platforms do not allow for “not equal to” queries. This means you'll have to be explicit for any singular value you're looking for or make multiple queries looking for multiple singular values and combining the results yourself either on the client or in a Firebase Cloud Function to obtain an equivalent result set. This is because Firebase wants to keep queries fast, but it can be a pain to deal with if you really need this feature in your app.

Another missing native query filter is a “string containing string” query. This means that you can't efficiently search blocks of text or partially match strings in your dataset. You can solve this by introducing a third party indexing service like Algolia or ElasticSearch, as [recommended](https://firebase.google.com/docs/firestore/solutions/search) by Firebase, but that solution is far from ideal. Also, although Cloud Firestore allows you to query on multiple fields, neither platform can query for data with more than one range filter restriction. For example, you couldn't search for a user with a score greater than 9,000 in the last 24 hours.

All of the above query limitations wouldn't be so annoying to deal with if only the platform provided a way to execute logical “or” compound queries. Alas neither Realtime Database nor Cloud Firestore will allow you append “or” queries together. This can be cumbersome to deal with depending on your data, as the only real alternative is to make all the individual queries yourself (locally or in a Cloud Function) and stitch the results together. Just another reason why a little bit of schema architecture planning can go a long way to avoid extraneous amounts of queries like this.

The final limitation to mention in both platforms is a lack of projection queries. Projection queries are convenient when you want to limit the amount of fields to return to the client during a query. If your entity contains dozens of key-value pairs, but you only happen to care about one of them at the moment, you'll have to fetch and parse the entire object in Firebase to read the single value you need.

## Realtime Database vs. Cloud Firestore: A Pros & Cons Summary

Rather than act as a replacement for the other, Realtime Database and Cloud Firestore provide options so developers can choose the database that suits their needs and still leverage the large ecosystem of other Google and Firebase services in their own systems.

### Why Choose Realtime Database

- You want a system that can easily track multiple live “streams” of data in realtime. Examples include live chat, location based events, realtime games or collaboration.
- You expect to be making a lot of small writes/reads to the database.
- You're fine with handling JSON data objects, while validating type yourself.
- You do not foresee any need for complex queries on your dataset.
- You're ready to manage a flat and heavily denormalized database.

### Why Choose Cloud Firestore

- You want to build an app that offers a lot more than the real-time features. You can always leverage both backends together if you need to incorporate an important real-time feature.
- You want a more traditional data schema, but desire to retain the ability of realtime listeners as well as the multitude of other Firebase platform features.
- You expect to make few but large CRUD operations.
- You want to be able to query data on multiple fields.

## Concluding Note

Hopefully this guide has been helpful in your quest to build an awesome Firebase app. Or perhaps let you realize that Firebase is not the solution you need for your next project. At Savvy Apps, we've had success with both Realtime Database and Cloud Firestore, but only after we weighed out all the options available first. Each project you take on will require careful consideration and planning, otherwise you'll lose time and money trying to shoehorn a solution out of the wrong tools. We'd love to hear how you've used either solution. Reach out to us on [Twitter](http://twitter.com/savvyapps) and [Facebook](https://www.facebook.com/savvyapps/) and check back for more Firebase resources.

#### Join 20,000+ Other Readers

Sign up to be notified of new blog posts and be the first to receive helpful app goodies from Savvy Apps!

Email*
March 7, 2018 By: **Matt Tea**![](../_resources/0eeb86e86a21c2d0026ea8261d3d3a60.jpg)

Matthew Tea is a developer with a passion for quality, tested code. He's a team player with a strong desire to learn new and upcoming technologies.