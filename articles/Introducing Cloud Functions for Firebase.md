Introducing Cloud Functions for Firebase

## [Introducing Cloud Functions for Firebase](http://firebase.googleblog.com/2017/03/introducing-cloud-functions-for-firebase.html)

March 9, 2017

![Brendan Lim](../_resources/9cdc328e2b41393e8e8f25768b44006c.png)
**
Brendan Lim
**  *Product Manager*

Firebase started with the belief that apps could be built with mostly client code since it was, in many instances, easier and faster. However, there are still some cases where server code is needed, such as executing trusted code, authenticating to a third party API, or running battery intensive operations. In these instances, you had to stand up your own server —  until now.

Today we are excited to announce the beta launch of [**Cloud Functions for Firebase**](https://firebase.google.com/features/functions). It lets you write small pieces of JavaScript, deploy them to Google's Cloud infrastructure, and execute them in response to events from throughout the Firebase ecosystem. This has been the most requested feature since Firebase launched. The ability to extend and connect Firebase features using Cloud Functions makes Firebase more powerful, allowing you to do even more with your app without having to think about servers.

[Introducing Cloud Functions for Firebase](https://www.youtube.com/watch?v=vr0Gfvp5v1A)

Cloud Functions is a versatile tool for building your mobile app. Here are a just a few of the many tasks you can perform with the integrations available at launch:

**Firebase Analytics **integration lets you trigger a function when a specific conversion event is fired. You can create functions to automate growth and retention workflows for your mobile apps, all without ever needing to update your client code.

- [Send a notification with a coupon code](https://github.com/firebase/functions-samples/tree/master/coupon-on-purchase) to users who have just completed a purchase
- [Send a survey request to users](https://github.com/firebase/functions-samples/tree/master/survey-app-update) after they upgrade their app

**Firebase Authentication** integration lets you trigger a function when a new user is created or deleted.

- [Send an email to welcome new users](https://github.com/firebase/functions-samples/blob/master/quickstarts/email-users) immediately after they sign up
- [Clean up user associated data](https://github.com/firebase/functions-samples/blob/master/user-data-cleanup) from your Realtime Database when a user account is deleted

**Firebase Realtime Database **integration lets you trigger a function when data is created, updated, or deleted at a specific path in the database.

- [Send a notification using FCM](https://github.com/firebase/functions-samples/tree/master/fcm-notifications) when data is written to the database
- [Moderate and remove abusive language](https://github.com/firebase/functions-samples/blob/master/text-moderation) from data written to the database

**Cloud Storage** integration lets you trigger a function when an object is written, updated, or deleted within a particular storage bucket.

- [Resize and convert images](https://github.com/firebase/functions-samples/blob/master/quickstarts/thumbnails) when a new image has been uploaded to your Cloud Storage bucket
- [Moderate abusive images](https://github.com/firebase/functions-samples/blob/master/moderate-images) uploaded to Cloud Storage using the Cloud Vision API

**HTTP endpoint **integration gives your Cloud Function a URL that can be used as a[webhook](https://github.com/firebase/functions-samples/tree/master/minimal-webhook). These functions are triggered when a request is made to their own unique, secure URLs.

- [Post new GitHub commits](https://github.com/firebase/functions-samples/tree/master/github-to-slack) to a Slack channel
- [Process in-app payments](https://github.com/firebase/functions-samples/tree/master/stripe) using Stripe

We'll continue to add more integrations in the future.

*> "We were early testers of Cloud Functions for Firebase and were excited to see how easy it was to extend the Realtime Database to export data and integrate with other services."**

**> - Erling Mårtensson, Master Architect, Sony*

Cloud Functions for Firebase provides a first-class experience for Firebase developers, built on top of [Google Cloud Functions](https://cloud.google.com/functions). Cloud Functions are single-purpose JavaScript functions that are executed in a secure, managed Node.js environment. The Firebase SDK for Cloud Functions gives you an API that allows you to choose an event source (such as writes to Firebase Realtime Database at a specific data location) and implement a function that triggers on every matching event. Our SDK also works with TypeScript to support code completion and help you catch syntax errors early.

The SDK works in tandem with the [Firebase CLI](https://firebase.google.com/docs/cli/) to provide a seamless experience when deploying your functions. This tight integration allows you to deploy all of your functions using only a single command.

*> "Thanks to Cloud Functions for Firebase, I built a company with no permanent employees but myself (so far), with no serious scaling concerns, and no major costs maintaining or upgrading the backend as the app grows. It's something of a miracle."

**
**> - Paul Budnitz, Founder/CEO, > [> Wuu](http://wuu.co/)*

We can't wait to see what you build!

Labels:[Cloud](http://firebase.googleblog.com/search/label/Cloud) , [Firebase Analytics](http://firebase.googleblog.com/search/label/Firebase%20Analytics)