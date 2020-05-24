What is the difference between Cloud Function and Firebase Functions?

 [up vote]()  2  [down vote]()  [favorite](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#)

**2**

Cloud functions and Firebase functiosn both look the same. Please describe the use case of each. In the both there is HTTP function is there.

In the **Cloud function**
[object Object]
and in the **Firebase function**
[object Object]
What is difference between both conncetion

 [![12d378e6a9788ab9c94bbafe242b82b4.jpg](../_resources/b13ce97eb502577efba4fd0e70c532d3.png)firebase](http://stackoverflow.com/questions/tagged/firebase)  [![tw3Uk.png](../_resources/a1ecb3755c4042bc7765946e592c514c.png)google-cloud-platform](http://stackoverflow.com/questions/tagged/google-cloud-platform)  [google-cloud-functions](http://stackoverflow.com/questions/tagged/google-cloud-functions)

|     |     |     |
| --- | --- | --- |
| [share](http://stackoverflow.com/q/42854865/1089189)\|[edit](http://stackoverflow.com/posts/42854865/edit)\|[flag](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#) |  [edited Mar 17 at 10:41](http://stackoverflow.com/posts/42854865/revisions)<br> [![5d55j.png](../_resources/250211b0330bfa615ad9aad094f39641.png)](http://stackoverflow.com/users/4625829/al)<br> [AL.](http://stackoverflow.com/users/4625829/al)<br> 9,96641954 | asked Mar 17 at 10:19<br> [![vobok.png](../_resources/3e06dacd4afbfbc7517f78d055406d65.jpg)](http://stackoverflow.com/users/4803607/muhammad-chhota)<br> [Muhammad chhota](http://stackoverflow.com/users/4803607/muhammad-chhota)<br> 25318 |

|     |     |
| --- | --- |
|     |  [upvote]() |
|     |  [flag]() |

 The term for Firebase is actually ***Cloud Functions for Firebase***, which is pretty much just Cloud Functions integrated with Firebase Services. – [AL.](http://stackoverflow.com/users/4625829/al)  [Mar 17 at 10:41](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#comment72816898_42854865)

|     |     |
| --- | --- |
|     |  [upvote]() |
|     |  [flag]() |

 So there is no difference between both? – [Muhammad chhota](http://stackoverflow.com/users/4803607/muhammad-chhota)  [Mar 17 at 11:39](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#comment72819077_42854865)

 [add a comment](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#)

 [start a bounty]()

## 1 Answer

 [active](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions?answertab=active#tab-top)  [oldest](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions?answertab=oldest#tab-top)  [votes](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions?answertab=votes#tab-top)

 [up vote]()  17  [down vote]()  accepted

There is no product called Firebase Functions.
There are three separate things:

1. Google Cloud Functions, which allow you to run snippets of JavaScript code in Google's infrastructure in response to events

2. Cloud Functions for Firebase, which triggers Google Cloud Functions based on events in Firebase (such as database or file writes, user creation, etc)

3. Firebase SDK for Cloud Functions, which includes a library (confusingly called [object Object]) that you use in your Functions code to access Firebase data (such as the snapshot of the data that was written to the database)

So Firebase provides a (relatively thin) wrapper around Google Cloud Functions, to make the latter product easier to use and integrate it with Firebase. In that senses it is similar to how Firebase integrates Google Cloud Storage into "Cloud Storage for Firebase" (formerly known as Firebase Storage).

If you're using Google Cloud Platform without Firebase, then you should use plain [Google Cloud Functions](https://cloud.google.com/functions/). If you're on Firebase or if you're a mobile developer interested in Cloud Functions, you should use [Cloud Functions for Firebase](https://firebase.google.com/docs/functions/).

|     |     |     |
| --- | --- | --- |
| [share](http://stackoverflow.com/a/42859932/1089189)\|[edit](http://stackoverflow.com/posts/42859932/edit)\|[flag](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#) |  [edited Mar 17 at 17:22](http://stackoverflow.com/posts/42859932/revisions) | answered Mar 17 at 14:19<br> [![photo.jpg](../_resources/bc6951353129960a48a356a70a7973e6.jpg)](http://stackoverflow.com/users/209103/frank-van-puffelen)<br> [Frank van Puffelen](http://stackoverflow.com/users/209103/frank-van-puffelen)<br> 104k10161195 |

|     |     |
| --- | --- |
|  2  |  [upvote]() |
|     |  [flag]() |

 confusingly-titled, indeed... – [drewmoore](http://stackoverflow.com/users/1988693/drewmoore)  [Mar 20 at 17:32](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#comment72919616_42859932)

 [add a comment](http://stackoverflow.com/questions/42854865/what-is-the-difference-between-cloud-function-and-firebase-functions/42859932#)

## Your Answer

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

 community wiki

## Not the answer you're looking for?	Browse other questions tagged [firebase](http://stackoverflow.com/questions/tagged/firebase)  [google-cloud-platform](http://stackoverflow.com/questions/tagged/google-cloud-platform)  [google-cloud-functions](http://stackoverflow.com/questions/tagged/google-cloud-functions) or [ask your own question](http://stackoverflow.com/questions/ask).