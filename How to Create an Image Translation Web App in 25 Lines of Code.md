How to Create an Image Translation Web App in 25 Lines of Code

## Machine Learning

# How to Create an Image Translation Web App in 25 Lines of Code

## Adding Google Cloud Machine Learning capabilities to a web application

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='176' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='177' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*nCkjgcqLKiEtFwyXzfbZnQ.jpeg](../_resources/5df2d1068f0fab4a9ed99256093c1742.jpg)](https://medium.com/@renaud.tarnec?source=post_page-----e67460208d29----------------------)

[Renaud Tarnec](https://medium.com/@renaud.tarnec?source=post_page-----e67460208d29----------------------)

[Mar 12](https://medium.com/firebase-developers/how-to-create-an-image-translation-web-app-in-25-lines-of-code-e67460208d29?source=post_page-----e67460208d29----------------------) · 8 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='193'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='194' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

In this article, I will demonstrate how you can quickly develop a web application that “[OCRises](https://en.wikipedia.org/wiki/Optical_character_recognition)” an image and translates the resulting text by mixing and matching different Firebase and Google Cloud services: Cloud Functions, Firebase Extensions and Vision API.

Also, I will show how the core business logic of such an app can be implemented in no more that 25 lines of code!

# The Travel Translator Demo App

Not only will I share those 25 lines of code , but I am going to share the full source code of the web app shown below!

![1*_kFrqHiQAk4bXMxz2Vygtw.jpeg](../_resources/c199bdf9d25874f662bde9ad3198185f.jpg)
![1*_kFrqHiQAk4bXMxz2Vygtw.jpeg](../_resources/64ec27ad61bbe956e84bcd66cf7bb901.jpg)

As illustrated in the above screenshots, the *Travel Translator* web app allows taking a picture of a text in any language and getting back an English translation together with the identification of the original language.

This is particularly interesting when traveling abroad! You can easily translate signs, touristic leaflets, restaurant menus, etc.

* * *

*...*

You will find the source code for this fully functional Vue.js web application in this [GitHub repository](https://github.com/rtarnec/travel-translator), ready to be built and deployed to a web server of your choice (for example on [Firebase Hosting](https://firebase.google.com/docs/hosting)). Detailed configuration and deployment instructions are to be found in the repo’s `README` file.

In case you are not versed in Vue.js development or you don’t want to install the Vue CLI just for deploying a demo, **I will share the code of a single HTML page that implements exactly the same core business logic**.

# Adding Google Cloud ML Capabilities to Your App

Since Firebase and [Google Cloud Platform (GCP)](https://cloud.google.com/) share common infrastructure, it is easy to integrate Firebase with GCP products and services such as [App Engine](https://cloud.google.com/appengine/), [BigQuery](https://cloud.google.com/bigquery/) or [AI & Machine Learning products](https://cloud.google.com/products/machine-learning/).

To integrate Machine Learning capabilities into Android or iOS apps, mobile developers can use [ML Kit for Firebase](https://firebase.google.com/docs/ml-kit/), a “*mobile SDK that brings Google's machine learning expertise to Android and iOS apps in a powerful yet easy-to-use package*”. In particular, with ML Kit you can implement features like Text OCR, Text Translation, Face Detection, Barcodes Scanning, Smart Reply, etc. in your native mobile apps.

However, at the time of writing, ML Kit is only available for Android and iOS and therefore **you cannot use it in a web application**.

Luckily, this does not mean that you cannot integrate GCP Machine Learning capabilities in your web application: by using Cloud Function it is very easy, as I am going to demonstrate in this article with the [Vision API](https://cloud.google.com/vision).

# Application Architecture

The below diagram details the different elements and services composing the *Travel Translator* web app:

- A w**eb app** in the front-end, which interacts with a set of Firebase Services (the back-end)
- A [**Cloud Storage**](https://firebase.google.com/docs/storage) bucket
- A [**Cloud Firestore**](https://firebase.google.com/docs/firestore) database
- Two [**Cloud Functions**](https://firebase.google.com/docs/functions)
- The [**Google Cloud Vision API**](https://cloud.google.com/vision/docs)
- An instance of the [**“Translate Text” Extension**](https://firebase.google.com/products/extensions/firestore-translate-text)

![1*KiZxavjHmHNr9_VeBm0r3w.png](../_resources/d5b482d99f13ef6772441d8b4e7902d4.png)
![1*KiZxavjHmHNr9_VeBm0r3w.png](../_resources/de7ce440711a995258d02605eb81b288.png)
Let’s detail how all these components interact with each other.

1. From the web app, the user takes a picture which is then uploaded to Cloud Storage.

2. The web app then sets a listener to a Firestore document that will be created later and will contain the result of the translation.

3. As soon as the image file is uploaded to the Cloud Storage bucket, a Cloud Function is triggered.

4. This Cloud Function calls the Cloud Vision API in order to execute the OCR of the image. The Vision API gets the image by directly reading from the Cloud Storage bucket.

5. As soon as the Cloud Function receives back the result of the OCR, it creates a Firestore document with the text resulting from this OCR and the detected language of this text.

6. In turn, the Firebase Extension which is listening to documents created in Firestore executes the translation of the original text to English and saves it to the Firestore document. The listener that was set up in step 2 is triggered and the translation is displayed in the web app.

7. Behind the scene, a second Cloud Function, which is also listening to documents created in Firestore, deletes the image that was uploaded in step 1 in order to reduce the Cloud Storage cost.

**In summary, by taking advantage of the possibilities to set listeners offered by the Firestore Client SDKs and Cloud Functions (including Firebase Extensions) we can easily orchestrate the asynchronous processes executed by the different Firebase services.**

In the next sections we are going to dive into the code and configuration settings of the different app components.

* * *

*...*

# Implementation Details

## 1. Web Application

As already mentioned above you will find the source code of the *Travel Translator* demo web app in this [GitHub repository](https://github.com/rtarnec/travel-translator) . The core of the app business logic can be found at [lines 521 to 536](https://github.com/rtarnec/travel-translator/blob/02bdb2740d86757e8f0dbf2e575ebd6eeaa1a3c8/src/components/Translator.vue#L521-L536) of `Translator.vue`. Those lines implement steps #1 and #2 above.

In order to easily analyse this core business logic without being “distracted” by the rest of the Vue.js app code, you will find below the code of a very simple HTML page that implements this “core” code.

|     |     |
| --- | --- |
| 1   | <!DOCTYPE html> |
| 2   | <html  lang="en"> |
| 3   |  <head> |
| 4   |  <meta  charset="UTF-8" /> |
| 5   |  <title>Travel Translator</title> |
| 6   |  <script  src="https://www.gstatic.com/firebasejs/7.9.1/firebase-app.js"></script> |
| 7   |  <script  src="https://www.gstatic.com/firebasejs/7.9.1/firebase-firestore.js"></script> |
| 8   |  <script  src="https://www.gstatic.com/firebasejs/7.9.1/firebase-storage.js"></script> |
| 9   |  </head> |
| 10  |     |
| 11  |  <body> |
| 12  |  <script> |
| 13  |  // Initialize Firebase |
| 14  |  var  config  =  { |
| 15  |  apiKey: <your_project_config>, |
| 16  | projectId: <your_project_config>, |
| 17  | storageBucket: <your_project_config>, |
| 18  | appId: <your_project_config> |
| 19  |  }; |
| 20  |     |
| 21  |  firebase.initializeApp(config); |
| 22  |     |
| 23  |  function  handleFiles(files)  { |
| 24  |  const  file  =  files[0]; |
| 25  |  const  fileName  =  file.name; |
| 26  |  const  metadata  =  {  contentType: file.type  }; |
| 27  |     |
| 28  |  const  docRef  =  firebase.firestore().collection('ocrTranslations').doc(); |
| 29  |     |
| 30  |  const  uploadFileName  =  docRef.id  +  '.'  +  fileName.split('.').pop(); |
| 31  |  const  fileRef  =  firebase.storage().ref('img_to_ocr/'  +  uploadFileName); |
| 32  |     |
| 33  |  fileRef |
| 34  |  .put(file,  metadata) |
| 35  |  .then(()  =>  { |
| 36  |  this.firestoreDocListener  =  docRef.onSnapshot(doc  =>  { |
| 37  |  if  (doc.exists  &&  doc.data().hasOwnProperty('translated'))  { |
| 38  |  document.getElementById('displayTranslation').innerHTML  =  doc.data().translated.en; |
| 39  |  document.getElementById('displayOriginalLanguage').innerHTML  =  doc.data().originalLanguage; |
| 40  |  }  |
| 41  |  }); |
| 42  |  }) |
| 43  |  .catch(error  =>  { |
| 44  |  alert(error.message); |
| 45  |  }); |
| 46  |  }  |
| 47  |  </script> |
| 48  |  <input  type="file" id="input" onchange="handleFiles(this.files)" /> |
| 49  |  <div  id="displayOriginalLanguage"></div> |
| 50  |  <div  id="displayTranslation"></div> |
| 51  |  </body> |
| 52  | </html> |

 [view raw](https://gist.github.com/rtarnec/4f026b04450a0526cc41c35a6926b4ff/raw/ec993aa53f03aecf6b5acd12d3c7d668d6ae6a51/travelTranslator.html)  [travelTranslator.html](https://gist.github.com/rtarnec/4f026b04450a0526cc41c35a6926b4ff#file-traveltranslator-html) hosted with ❤ by [GitHub](https://github.com/)

Here is how it works:

1. The `body` of the HTML page contains one button for uploading a file and two `div`s. In the first `div` we will display the original language and in the second one the translated text.

2. In the JavaScript tag, after having initialised Firebase, we define the `handleFile()` function which is triggered upon file upload.

3. This function generates a new Firestore `[DocumentReference](https://firebase.google.com/docs/reference/js/firebase.firestore.DocumentReference)`, uses the resulting document ID to name the file to be uploaded and then uploads the file using the Cloud Storage `[put()](https://firebase.google.com/docs/reference/js/firebase.storage.Reference#put)` method.

4. When the `Promise` returned by the asynchronous `[put()](https://firebase.google.com/docs/reference/js/firebase.storage.Reference#put)` method resolves, a Firestore listener to the previously created document is set (via the `[onSnapshot()](https://firebase.google.com/docs/reference/js/firebase.firestore.DocumentReference#on-snapshot)` method).

5. In the listener we check if the Firestore document exists and has a `translated` field: if it the case, we write the content of the two `div`s.

We’re done! This is around 15 lines of code, without the configuration part and the carriage returns.

## 2. Translate Text Extension

Configuring the *Translate Text* Extension is quite easy: click on the *Extensions* menu item at the bottom of the vertical menu of the Firebase console.

![1*D_-Hw16hpouNpKRI66AMFg.png](../_resources/a5d050868f536ff12ee5c08b936dfb61.png)
![1*D_-Hw16hpouNpKRI66AMFg.png](../_resources/ff425d8588ad0a10a9ed4e1b8cc51a3e.png)
The Extensions page in Firebase Console

Then, in the *Translate Text* card, click on the *Install* button to install the extension into your app.

A four steps wizard opens. Proceed as follows:

- **Step 1: *Review APIs enabled and resources created*. **As its title says, this step simply informs you about the APIs and resource to be enabled or created. Simply click the *Next* button.
- **Step 2: *Set up billing*.** In order to use this extension, the Firebase project must be on the *Blaze* plan¹. Click on the *Upgrade Project* button, if needed.
- **Step 3: *Review access granted to this extension*.** Again, this step is an informative one, giving you more info on the new service account that will provide Cloud Firestore read/write access rights to the Extension. Just click on the *Next* button.
- **Step 4: *Configure extension*. **It is actually in this step that you really configure the Extension. As shown in the image below, you need to select `en` for the *Target language* (i.e. English, see the [codes/languages list](https://cloud.google.com/translate/docs/languages)), `ocrTranslations` for the *Collection path.* You can leave the other config options unchanged. Then, click on the *Install extension* button.

![1*KZ9KIMzSClsQTwWGiAKl2w.png](../_resources/71a72d9101248339fb90d2730c107506.png)
![1*KZ9KIMzSClsQTwWGiAKl2w.png](../_resources/a405bb80a42a47fae9bc772f7abb51ea.png)
Configuring the ***Translate Text*** Extension (Step 4)

Now that the extension is configured and installed, let’s have a look at the Cloud Functions.

## 3. Cloud Functions

The Cloud Functions code defines two Cloud Functions: `ocrImage` and `deleteFile`.

|     |     |
| --- | --- |
| 1   | const  functions  =  require('firebase-functions'); |
| 2   | const  admin  =  require('firebase-admin'); |
| 3   | const  vision  =  require('@google-cloud/vision'); |
| 4   |     |
| 5   | admin.initializeApp(); |
| 6   |     |
| 7   | exports.ocrImage  =  functions.storage.object().onFinalize(async  (object)  =>  { |
| 8   |     |
| 9   |  const  filePath  =  object.name;  // File path in the bucket. |
| 10  |  const  contentType  =  object.contentType;  // File content type. |
| 11  |     |
| 12  |  const  firestoreDocId  =  filePath.split("/")[1].split(".")[0]; |
| 13  |     |
| 14  |  try  { |
| 15  |  if  (!contentType.startsWith('image/'))  { |
| 16  |  await  admin.firestore().doc(`ocrTranslations/${firestoreDocId}`).set({  error: 'NOT_AN_IMAGE'  }); |
| 17  |  return null; |
| 18  |  }  |
| 19  |     |
| 20  |  const  visionClient  =  new  vision.ImageAnnotatorClient(); |
| 21  |  const  [result]  =  await  visionClient.textDetection(`gs://${object.bucket}/${object.name}`); |
| 22  |  const  detections  =  result.textAnnotations; |
| 23  |     |
| 24  |  const  input  =  detections[0].description; |
| 25  |  const  originalLanguage  =  detections[0].locale; |
| 26  |     |
| 27  |  await  admin.firestore().doc(`ocrTranslations/${firestoreDocId}`).set({ input, originalLanguage, filePath }); |
| 28  |     |
| 29  |  return null; |
| 30  |     |
| 31  |  }  catch  (error)  { |
| 32  |  console.log(error); |
| 33  |  return null; |
| 34  |  }  |
| 35  | })  |
| 36  |     |
| 37  | exports.deleteFile  =  functions.firestore |
| 38  |  .document('ocrTranslations/{docId}') |
| 39  |  .onCreate((snap,  context)  =>  { |
| 40  |  const  filePath  =  snap.data().filePath; |
| 41  |  const  file  =  admin.storage().bucket().file(filePath); |
| 42  |  return  file.delete(); |
| 43  |  }); |

 [view raw](https://gist.github.com/rtarnec/7b7604a06cb5b5e8d161309f063c1c9c/raw/b9e030cc5eec75892a39db110d3e84fa0762a74f/TravelTranslatorCloudFunctions.js)  [TravelTranslatorCloudFunctions.js](https://gist.github.com/rtarnec/7b7604a06cb5b5e8d161309f063c1c9c#file-traveltranslatorcloudfunctions-js) hosted with ❤ by [GitHub](https://github.com/)

Cloud Functions index.js file
Let’s detail how the `ocrImage` Cloud Function works.

1. We import the Cloud Functions and Admin SDK modules together with the [Node.js Client Library for the Cloud Vision API](https://www.npmjs.com/package/@google-cloud/vision) .

2. We initialize an `admin` app instance.

3. We then define the `ocrImage` Cloud Function which is triggered with an `[onFinalize](https://firebase.google.com/docs/reference/functions/providers_storage_.objectbuilder#onfinalize)` event handler, i.e. when a new object/file is successfully created in the Cloud Storage bucket.

4. From the file path we derive the ID of the Firestore document where we will store the result of the OCR.

5. Then, we declare an instance of an `[ImageAnnotatorClient](https://googleapis.dev/nodejs/vision/latest/v1.ImageAnnotatorClient.html)` and we call the `[textDetection()](https://googleapis.dev/nodejs/vision/latest/v1.ImageAnnotatorClient.html#textDetection)` method passing the URI of the Cloud Storage file. **With only those two lines** we trigger the image OCR and get the result in an `[AnnotateImageResponse](https://googleapis.dev/nodejs/vision/latest/google.cloud.vision.v1.html#.AnnotateImageResponse)` object².

6. Using the `textAnnotations` property of this object, we get an array of `[EntityAnnotations](https://googleapis.dev/nodejs/vision/latest/google.cloud.vision.v1.html#.EntityAnnotation)` and we simply need to call the `description` and `locale` properties of the first element of the array to get the text resulting from the OCR and its language code.

7. Then, those two values, together with the file path, are saved in a new Firestore document in the `ocrTranslations` collection.

Since this `ocrTranslations` collection is the collection the *Translate Text* extension listens on, when the new document is created the extension is triggered and, upon completion, adds the translated text to the Firestore document in the `translated` field.

It is then the turn of another listener to be triggered! The one that we set in the web app to detect when the translation text is added to the Firestore document that has the same ID as the file name. So, the web app gets the content of the Firestore document and displays the translated text, together with the original language code.

# **That’s it! **  **In approximately 25 lines of code we developed a web app that translates images.**

* * *

*...*

But wait… there was another Cloud Function in the Cloud Functions `index.js` file!

Yes indeed, we have the `deleteFile`**  **Cloud Function whose job it is to delete the image file in the Cloud Storage bucket as soon as the Firestore document is created. As a matter of fact, since the Firestore document is created with the translated text, we don’t need to keep the original image around anymore and can thus delete it.

So, the `deleteFile` Cloud Function simply reads the image path from the Firestore document and deletes the corresponding file³.

* * *

*...*
And that’s it!

If you have any question or suggestion, please leave a comment below. If you encounter any problem with the app configuration or deployment, do not hesitate to ask for help as well!

* * *

*...*

[1] More details on the Firebase pricing plans: https://firebase.google.com/pricing. Note that if you just want to test the *Travel Translator* app with some few images, it will most probably not incur any cost!

[2] More details in the Cloud Vision API documentation: https://cloud.google.com/vision/docs/ocr#text_detection_requests

[3] Note that we could have included this deletion task at the end of the `ocrImage` Cloud Function but, in order to avoid having an extra asynchronous task in this one, we have chosen to trigger another Cloud Function for the image deletion.