Building Your Next Serverless Application: The Complete Guide.

# Building Your Next Serverless Application: The Complete Guide.

![](:/8c1fb1255a264cbe16c879c3156615f8)![1*X7b6gJCWoxHOlApPaI82Rw.png](../_resources/b4eb0ec7caa49fdd43823f107dda578a.png)

The overall architecture of our serverless application

I bet you’ve already heard of Serverless architectures: The next evolution of Cloud computing. The term “Serverless” is actually an umbrella term of two areas in Cloud computing: Backend as a Service (BaaS) and Functions as a Service (FaaS).

With BaaS we’re breaking up our applications into smaller pieces and implementing some of those pieces entirely with external services. This is usually done with a call to an API (or [gRPC](https://grpc.io/) calls). One of the most popular Backends as a Service is Google’s [Firebase](https://firebase.google.com/), a realtime database (with a bunch of other cool features) for mobile and web applications.

Functions as a Service on the other hand, is another form of Compute as a Service: FaaS is a way of building and deploying server-side code, by simply deploying individual functions (hence the name) on the vendor-supplied FaaS platform.

* * *

*...*

Now that we agree on the correct definition of what a Serverless architecture actually is, **let’s build a complete “Serverless application”.**

* * *

*...*

The application we’re going to build is a chatbot that’s capable of extracting a text content from a picture (optionally translating it to different languages) and sending back the result to the user via SMS (or a phone call). Such application could be used to extract other useful information from a given image or even a video stream and sends SMS notifications to the user or a group of users.

I’m sure you are now thinking of a more interesting use case. If that’s the case, please let me know!

Let’s dive in…

* * *

*...*

### 1- Creating the Chatbot

For our use case, we would like to start a conversation with our agent (aka. “chatbot”) and provide it with something containing some text to be extracted and later analysed (a page from a book or a newspaper maybe?).

![](../_resources/e66b289069e4c71378f0fb0cad9d80f9.png)![1*J5OzRt3GnehKNplx28-0QA.png](../_resources/d72a2cb571bc39fd45794d320e6e35d5.png)

#### a- Creating the “dialog flow” for our agent

Since the “chatbot” part is not our main focus in this post, we will “Keep it simple, stupid” and design a quick conversation in DialogFlow, as follows:

1. 1Create an intent “read”.

2. 2Add a couple of user’s expressions, eg. “read this text” or “extract the text”.

3. 3Add a “read” action.
4. 4Enable the use of the webhook (see the fulfilment below).

![](../_resources/c2c5189664109109b1d16173df95b375.png)![1*_BAWQtc8uZhIMxh-PSu-Uw.png](../_resources/8ffce5492284fca001a07407992b20ba.png)

#### b- Implementing the agent logic

Let’s now code the logic for our agent that will actually take the picture.
First, we’ll need two utility functions:
1. 1`captureImage` a function that captures an image using the user’s camera.

2. 2`uploadImage` a function that uploads that image to the Google Cloud Storage (GCS).

Here the implementation of the `captureImage` function. This function is using a system utility `imagesnap` available on MacOS to actually access the camera, capture the image and store the image file under `/tmp/google-actions-reader-${Date.now()}.png` . This function then returns both the name and the file content in `base64` :

const fs = require('fs');
const child_process = require('child_process');
const Buffer = require('safe-buffer').Buffer;
/**
* Capture the image from the user computer's camera.
*/
function **captureImage**() {
return new Promise((res, rej) => {
const file = `/tmp/google-actions-reader-${Date.now()}.png`;
try {
child_process.execSync(`imagesnap -w 1 ${file}`);
const bitmap = fs.readFileSync(file);
res({
base64: new Buffer(bitmap).toString('base64'),
file
});
} catch (err) { rej(err); }
});
}

The next function `uploadImage` will simply upload that image to GCS in the `cloud-function-ocr-demo__image` bucket:

const child_process = require('child_process');
/**
* Uploads the file to GCS.
*
* @param {object} data The GCP payload metadata.
* @param {object} data.file The filename to read.
*/
function **uploadImage**(data) {
child_process.execSync(
`gsutil cp ${data.file} gs://cloud-function-ocr-demo__image`
);
return data.file.split('/').pop();
}

> Please note the name of the bucket `cloud-function-ocr-demo__image`> , we will need it later.

Now that we have our two utilities functions `captureImage` and `uploadImage` ready, let’s use them inside the **read** intent logic (remember this intent in the dialog from above?):

/**
* The "read" intent that will trigger the capturing and uploading
* the image to GSC.
*
* @param {object} app DialogflowApp instance object.
*/
function **readIntent**(app) {
 **captureImage**()
.then(**uploadImage**)
.then(content => {
app.tell(`I sent you an SMS with your content.`);
})
.catch(e => app.ask(`[ERROR] ${e}`) );
}
This `readIntent` will basically capture and then upload the image to GCS.

Now that we have all of the agent’s logic implemented, let’s create the main Cloud Function that will process DialogFlow’s requests:

const aog = require('actions-on-google');
const DialogflowApp = aog.DialogflowApp;
/**
* Handles the agent (chatbot) logic. Triggered from an HTTP call.
*
* @param {object} request Express.js request object.
* @param {object} response Express.js response object.
*/
module.exports.**assistant** = (request, response) => {
const app = new DialogflowApp({ request, response });
const actions = new Map();
actions.set('read', **readIntent**);
app.handleRequest(actions);
};

The `assistant` Cloud Function will be triggered from an HTTP call. This call will be made by DialogFlow if the user says, for example, “read this text” (as mentioned above) which is an expression defined in the **read** intent.

#### c- Deploying the assistant Cloud Function

> This section will serve as an example for the rest of this guide.

In order to deploy a Cloud Function, we can use the `gcloud` command with the following arguments:

`gcloud beta functions [[NEWLINE]]  deploy **<function-label> **[[NEWLINE]]  **<trigger-type>**`

 `--source **<source-code> **[[NEWLINE]]  --entry-point **<function-name>**`

1. 1`<function-label>` is a function label, this can be the same or different from `<function-name>`.

2. 2`<trigger-type>` is how your function is going to be triggered (topic, http, storage…etc).

3. 3`<source-code>` is the Google Cloud Repository where the source code of the function is hosted. **This can’t be some other public Git repository!**

4. 4`<function-name>` is the actual exported function name (in your code).

> You also can use a Google Cloud Storage bucket to host the source code of your function. But we’ll not cover this here.

Oh, by the way…

> Hosting your source code in a Google Cloud Repository (a Git repo) is a good idea if you have a continuous delivery strategy in your organisation.

In our case, here is the full command:
gcloud beta functions
deploy ocr-assistant

--source [https://source.developers.google.com/projects/](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)...

--trigger-http
--entry-point assistant

In case you are wondering, the Google Cloud Repository source has the following format:

[https://source.developers.google.com/projects/**<project-id>**/repos/**<repo-id>**/moveable-aliases/](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)**<branch-name>**

Once deployed, your function should be ready to be triggered:

![](../_resources/e67933477e975a4e5bd6d74d53db3478.png)

You also will be given a public URL, which looks like this:

[*https://us-central1-****<project-id>****.cloudfunctions.net/ocr-assistant*](https://us-central1-cloud-function-ocr-demo.cloudfunctions.net/ocr-assistant)

That’s the URL we will use in our DialogFlow project.

* * *

*...*

#### Gotcha!!

If you’ve been following carefully, you may have noticed that the `captureImage` function needs… well, access to a camera! This means that we won’t be able to deploy this specific function to the Google Cloud Platform. Rather, we will host it on our specific hardware, say a Raspberry PI (to make it simple), and use a different URL (obviously).

> You can use the > [> Google Cloud Function Emulator](https://cloud.google.com/functions/docs/emulator)>  to run your Cloud Functions locally. Please keep in mind that this is only for development purposes. **> Don’t use this for production applications.**

* * *

*...*

#### d- Adding the fulfilment URL

Let’s then add the fulfilment URL, which points to the `assistant` Cloud Function that will process the agent requests:

![](../_resources/7700c2e72b9451c7138d3ad1a1516da8.png)

* * *

*...*

Now, we’re done with the first part of our application which essentially consists of getting our image uploaded to the GCS.

### 2- Processing the image

Until now, we’ve only talked about Cloud Functions—FaaS. Let’s jump to the Backends as a Service (or BaaS) part.

We want to be able to extract some content from the image, a text in our case. We have tons of open source libraries to do that—[OpenCV](https://opencv.org/) or [Tensorflow](https://www.tensorflow.org/) just to name a few. Unfortunately, these libraries require us to have some sort of expertise in Machine Learning and Image (or Sound) processing. Hiring these expertise is not easy! Also, ideally, we don’t want to maintain this code and we want our solution to be able to automagically scale in case our application becomes popular. Said simply, we don’t want to manage this feature. Luckily, the Google Cloud Platform got us covered:

1. 1The [Google Vision API](https://cloud.google.com/vision/) allows us to extract the content.

2. 2Use the [Google Translation API](https://cloud.google.com/translate/) allows us to… well, translate the content.

Here is the sub-architecture of this feature:

![](../_resources/45b6a9b44d39afdfa9c8c871866e3f4e.png)

#### a- Extracting the content from the image

In order to be able to process the image, we need two functions:

1. 1`processImage` a Cloud Function that is triggered whenever a new image is uploaded to the GCS in the bucket `cloud-function-ocr-demo__image`.

2. 2`detectText` a function that will actually extract the text from the image using the Google Vision API.

Here is the implementation of `processImage` :
/**
* Cloud Function triggered by GCS when a file is uploaded.
*
* @param {object} event The Cloud Functions event.
* @param {object} event.data A Google Cloud Storage File object.
*/
exports.**processImage** = function processImage(event) {
let file = event.data;

return Promise.resolve()
.then(() => {
if (file.resourceState === 'not_exists') {
// This was a deletion event, we don't want to process this
return;
}

return **detectText**(file.bucket, file.name);
})
.then(() => {
console.log(`File ${file.name} processed.`);
});
};

The implementation of `detectText` function is straightforward (we will improve it later):

const vision = require('@google-cloud/vision')();
/**
* Detects the text in an image using the Google Vision API.
*
* @param {string} bucketName Cloud Storage bucket name.
* @param {string} filename Cloud Storage file name.
*/
function **detectText**(bucketName, filename) {
let text;

return **vision
.textDetection({
source: {
imageUri: `gs://${bucketName}/${filename}`
}
})**
.then(([detections]) => {
const annotation = detections.textAnnotations[0];
text = annotation ? annotation.description : '';
return Promise.resole(text);
});
}

We now need to deploy the `processImage` Cloud Function and we want it to be triggered whenever a new image is uploaded to the GCS in the `cloud-function-ocr-demo__image` bucket:

gcloud beta functions
deploy ocr-extract

--source [https://source.developers.google.com/projects/.](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)..

--trigger-bucket cloud-function-ocr-demo__image
--entry-point processImage

![](../_resources/277644ab7e495b86bd441f08c19fbfb1.png)

Let’s now add some translations…

#### b- Translating the text

Translating the extracted text will be triggered by a specific Google Cloud Pub/Sub topic `TRANSLATE_TOPIC` and will consist of two operations:

1. 1Detect the language of the extracted content. We’ll do this inside our previous `processImage` function. We could create another Cloud Function for this, but let’s not overcomplicate our architecture!

2. 2`translateText` : Translate that content to a given language.

Let’s improve our existing `processImage` Cloud Function with the language detection feature:

const vision = require('@google-cloud/vision')();
const translate = require('@google-cloud/translate')();
const config = require('./config.json');
/**
* Detects the text in an image using the Google Vision API.
*
* @param {string} bucketName Cloud Storage bucket name.
* @param {string} filename Cloud Storage file name.
* @returns {Promise}
*/
function **detectText**(bucketName, filename) {
let text;

return vision
.textDetection({
source: {
imageUri: `gs://${bucketName}/${filename}`
}
})
.then(([detections]) => {
const annotation = detections.textAnnotations[0];
text = annotation ? annotation.description : '';
return **translate.detect(text);**
})
.then(([detection]) => {
if (Array.isArray(detection)) {
detection = detection[0];
}

// Submit a message to the bus for each language
// we're going to translate to
 **const tasks = config.TO_LANG.map(lang => {
let topicName = config.TRANSLATE_TOPIC;
if (detection.language === lang) {
topicName = config.RESULT_TOPIC;
}
const messageData = {
text: text,
filename: filename,
lang: lang,
from: detection.language
};

return publishResult(topicName, messageData);
});

 **return Promise.all(tasks);
});
}
Let’s explain the new extra code we’ve added:

We first added a call to the Google Translation API in order to detect the main language of the extracted text `translate.detect(text);`. Then, in the next block, we basically iterate over the `config.TO_LANG` array we have in the configuration file, and publish a `TRANSLATE_TOPIC` with a specific payload containing the text content (`text`), the source language (`from`) and the target language we want to translate to (`lang`). If the source language is the same as the target language, we just publish `RESULT_TOPIC`.

* * *

*...*

#### A side note about the Google Cloud Pub/Sub

For convenience purposes, we’ve also included a new utility function `publishResult` whose responsible of publishing a Pub/Sub topic. It essentially uses the Google Cloud Pub/Sub API to create (if needed) and publish the given topic:

const pubsub = require('@google-cloud/pubsub')();
/**
* Publishes the result to the given pub-sub topic.
*
* @param {string} topicName Name of the topic on which to publish.
* @param {object} data The message data to publish.
*/
function **publishResult**(topicName, data) {
return pubsub
.topic(topicName)
.get({ autoCreate: true })
.then(([topic]) => topic.publish(data));
}

* * *

*...*

Let’s then create the `translateText` Cloud Function that will translate the extracted text:

const translate = require('@google-cloud/translate')();
const Buffer = require('safe-buffer').Buffer;
const config = require('./config.json');
/**
* Translates text using the Google Translate API.
* Triggered from a message on a Pub/Sub topic.
*
* @param {object} event The Cloud Functions event.
* @param {object} event.data The Cloud Pub/Sub Message object.
* @param {string} event.data.data The "data" property of
* the Cloud Pub/Sub Message.
* This property will be a base64-encoded string that
* you must decode.
*/
exports.**translateText** = function translateText(event) {
const pubsubMessage = event.data;
const jsonString = Buffer.from(
pubsubMessage.data, 'base64'
).toString();
const payload = JSON.parse(jsonString);

return Promise.resolve()
.then(() => {

const options = {
from: payload.from,
to: payload.lang
};

return **translate.translate(payload.text, options);**
})
.then(([translation]) => {
const messageData = {
text: translation,
filename: payload.filename,
lang: payload.lang
};

return **publishResult(config.RESULT_TOPIC, messageData);**
});
};

The implementation of this function is self explanatory: We call basically call the `translation.translate(payload.text, options);` and once we get the result, we publish the `RESULT_TOPIC` with a translated content.

It’s time now to deploy the `translateText` Cloud Function using the same command as before. This function will be triggered by the `TRANSLATE_TOPIC` topic, so we make sure to use that as a trigger type:

gcloud beta functions
deploy ocr-translate

--source [https://source.developers.google.com/projects/.](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)..

--trigger-topic TRANSLATE_TOPIC
--entry-point translateText

![](../_resources/dbe1c8e5f37d4ff980402af8900b825a.png)

#### c- Save the translated text

So far so good, we have now managed to capture the image, upload it the GCS, process it and extract the text and then translate it. The last step would be to save the translated text back to the GCS.

Here is the implementation of such function:
const storage = require('@google-cloud/storage')();
const Buffer = require('safe-buffer').Buffer;
const config = require('./config.json');
/**
* Saves the data packet to a file in GCS.
* Triggered from a message on a Pub/Sub topic.
*
* @param {object} event The Cloud Functions event.
* @param {object} event.data The Cloud Pub/Sub Message object.
* @param {string} event.data.data The "data" property of
* the Cloud Pub/Sub Message.
* This property will be a base64-encoded string that
* you must decode.
*/
exports.**saveResult** = function saveResult(event) {
const pubsubMessage = event.data;
const jsonString = Buffer.from(
pubsubMessage.data, 'base64'
).toString();
const payload = JSON.parse(jsonString);

return Promise.resolve()
.then(() => {
const bucketName = config.RESULT_BUCKET;
// Appends a .txt suffix to the image name.
const filename = renameFile(payload.filename, payload.lang);

 **const file = storage.bucket(bucketName).file(filename);**

 **return file.save(payload.text)
.then(_ => publishResult(config.READ_TOPIC, payload));**
});
};

The `saveResult` is triggered by the `RESULT_TOPIC` which is the topic holding the translated text. We simply use that payload and call the Google Cloud Storage API to store the content in a bucket called `config.RESULT_BUCKET` (which is `cloud-functions-orc-demo`). Once this is done, we publish the `READ_TOPIC` topic will trigger the next Cloud Function (see next section).

Time to deploy the `saveResult` Cloud Function using the same command as before. This function will be triggered by the `TRANSLATE_TOPIC` topic, so we make sure to use that as a trigger type:

gcloud beta functions
deploy ocr-save

--source [https://source.developers.google.com/projects/.](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)..

--trigger-topic `RESULT_TOPIC`
--entry-point saveResult

![](../_resources/0217fd9fbf19c73b1b33d0d0f180c8c7.png)

### 3- Send SMS notifications

Finally, we are now ready to read the translated text from the GCS and send it via SMS to the user’s phone.

![](../_resources/55cb76b4a2d8ac8bd130b9454d7af54c.png)

#### a- Reading the translated text from the GCS

Reading the file from the GCS is, again, a straightforward operation:
const Buffer = require('safe-buffer').Buffer;
/**
* Reads the data packet from a file in GCS.
* Triggered from a message on a Pub/Sub topic.
*
* @param {object} event The Cloud Functions event.
* @param {object} event.data The Cloud Pub/Sub Message object.
* @param {string} event.data.data The "data" property of
* the Cloud Pub/Sub Message.
* This property will be a base64-encoded string that
* you must decode.
*/
exports.**readResult** = function readResult(event) {
const pubsubMessage = event.data;
const jsonString = Buffer.from(
pubsubMessage.data, 'base64'
).toString();
const payload = JSON.parse(jsonString);
return Promise.resolve()
.then(() => **readFromBucket(payload)**)
.then(content => **sendSMS(content)**.then(_ => **call(content)**));
};

In the `readResult` function, we are using another utility function `readFromBucket` which, as the name suggests, reads the content from a given GCS bucket. Here is the detailed implementation:

const storage = require('@google-cloud/storage')();
const config = require('./config.json');
/**
* Reads the data packet from a file in GCS.
* Triggered from a message on a Pub/Sub topic.
*
* @param {object} payload The GCS payload metadata.
* @param {object} payload.filename The filename to read.
*/
function **readFromBucket**(payload) {
// Appends a .txt suffix to the image name.
const filename = renameFile(payload.filename, payload.lang);
const bucketName = config.RESULT_BUCKET;
** const file = storage.bucket(bucketName).file(filename);
** const chunks = [];

return new Promise((res, rej) => {
file
.createReadStream()
.on('data', chunck => {
chunks.push(chunck);
})
.on('error', err => {
rej(err);
})
.on('response', response => {
// Server connected and responded with
// the specified status and headers.
})
.on('end', () => {
// The file is fully downloaded.
res(chunks.join(''));
});
});
}

That’s simply it. Now, let’s deploy the `readResult` Cloud Function and make it triggers from the `READ_TOPIC` topic:

gcloud beta functions
deploy ocr-read

--source [https://source.developers.google.com/projects/.](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)..

--trigger-topic READ_TOPIC
--entry-point readResult

![](../_resources/b0a58ab61cf60dda7368f5c0c584a290.png)

**b- Sending SMS notifications**

When it comes to sending an SMS to the user’s phone, we use the awesome [Twilio](https://www.twilio.com/) service, which… just works!

> Using Twilio services require you create a developer account.
const Twilio = require('twilio');
const TwilioClient = new Twilio(
config.TWILIO.accountSid,
config.TWILIO.authToken
);
/**
* Sends an SMS using Twilio's service.
*
* @param {string} body The content to send via SMS.
*/
function **sendSMS**(body) {
return TwilioClient.messages
.create({
to: '+33000000000',
from: '+33000000000',
body: body || 'MESSAGE NOT FOUND'
});
}
**c- Making phone calls (BONUS)**

Sending the translated content via a phone call back to the user is a bit tricky as you need to provide two functions:

1. 1`call` which makes the phone call: **this actually calls the user!**

2. 2`twilioCalls` which is the HTTP endpoint that’s going to process the incoming calls made by the `call` function.

To demonstrate how this process would work, let’s first have a look at the `twilioCalls` implementation:

const Twilio = require('twilio');
const VoiceResponse = Twilio.twiml.VoiceResponse;
/**
* Handles the incoming Twilio call request.
* Triggered from an HTTP call.
*
* @param {object} request Express.js request object.
* @param {object} response Express.js response object.
*/
module.exports.**twilioCall** = function(request, response) {
return readFromBucket({
filename: 'twilio_user_33000000000.txt'
}).then(content => {
const twiml = new VoiceResponse();
twiml.say(`
<Say voice="woman">Hi, this is your extracted text:</Say>
<Pause length="1"></Pause>
<Say voice="woman">${content}</Say>
`);
res.writeHead(200, { 'Content-Type': 'text/xml' });
res.end(twiml.toString());
});
};

The `twilioCall` function is responsible of reading the file from the bucket and sending back an XML response built thanks to the Twilio Markup Language ([TwilioML](https://www.twilio.com/docs/api/twiml)).

You will then need to deploy this Cloud Function in order to get the public URL required by the `call` function:

gcloud beta functions
deploy ocr-twilio-call

--source [https://source.developers.google.com/projects/.](https://source.developers.google.com/projects/cloud-function-ocr-demo/repos/cloud-function-ocr-demo/moveable-aliases/master)..

--trigger-http
--entry-point twilioCall

![](../_resources/eb28a10c1160d116514d06315e2e8a64.png)

Once deployed, you will get a public URL like this:
https://us-central1-<projet-id>.cloudfunctions.net/ocr-twilio-call
Next, we’ll use that URL in the `call` function:
/**
* Triggers a call using Twilio's service.
*/
function call() {
return TwilioClient.api.calls
.create({
url: 'https://the-url-from-above/ocr-twilio-call',
to: '+33000000000',
from: '+33000000000'
});
}
Done! Now, you Twilio HTTP endpoint is ready for incoming calls.

### Wrapping up!

In this guide, we implemented a bunch of Cloud Functions that performed different tasks:

1. 1`assistant` processes the agent’s request coming from DialogFlow.
2. 2`processImage` extracts the text from the uploaded image.
3. 3`translateText` translates the extracted text to different languages.
4. 4`saveResult` saves the translated text to the GCS.
5. 5`readResult` reads the translated text from the files stored in the GCS.
6. 6`twilioCall` processes the incoming call requests.
Here is a recap of all the deployed Cloud Functions:

![](../_resources/7b34dc8367359af101caaeb9229d0546.png)

And here is again the complete architecture:

![](:/8c1fb1255a264cbe16c879c3156615f8)

#### Try it out

In order to test the application, we first need to deploy the DialogFlow agent. We choose to deploy it on the Google Assistant since our `assistant` Cloud Function is meant to process the Google Assistant requests. If you’d like to deploy to other services (Slack, Facebook, Twitter…etc) you just need to provide and deploy other Cloud Functions.

From the integration tab, choose the Google Assistant and click the **TEST** button:

![](../_resources/d0f3dbadf8d3ac10f637d33e1d6d85ea.png)

This will open up the Actions on Google simulator, allowing you to test your agent directly in the bowser. Alternatively, you can your phone or Google Home devices as well:

![](../_resources/06d9bfd7f29289fba17420ceeeb78ea7.png)

> Note the we gave our agent a name: shakespeare. We did that from the same simulator, in the overview panel.

As a sample text, we will use the following quote (by [Ziad K. Abdelnour](https://twitter.com/blackhawkinc)):

![](:/df17fc9546dfc96e6a54423d49eba9a1)
And… here is the SMS sent by our `readResult` function:

![](../_resources/7ba3c910d8730009973865865490cdf1.png)

### ⚠️ Important Notes ⚠️

1. 1In my sample code, I didn’t handle any error. **You should!**
2. 2In my sample code, I didn’t log anything. **You should!**
3. 3**In my sample code, I didn’t write unit tests. You should!**
Here is the complete source code:

[**manekinekko/serverless-application-demo** *Contribute to serverless-application-demo development by creating an account on GitHub.*github.com](https://github.com/manekinekko/serverless-application-demo)[(L)](https://github.com/manekinekko/serverless-application-demo)

* * *

*...*

#### Congratulations! You’ve just built your first true “Serverless” application! And, Happy New Year 2018 🎉✨🎁

* * *

*...*

*Follow me on Twitter *[*@manekinekko*](https://twitter.com/manekinekko)* to learn more about the Web and Cloud platforms.*