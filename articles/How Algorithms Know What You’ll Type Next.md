How Algorithms Know What You’ll Type Next

[Skip to main content](https://pudding.cool/2019/04/text-prediction/#content)

# How  Algorithms  Know  What  You’ll  Type  Next

By[**Wessel Stoop**](https://pudding.cool/author/wessel-stoop)&[**Antal van den Bosch**](https://pudding.cool/author/antal-van-den-bosch)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='feather feather-arrow-down-circle js-evernote-checked' data-evernote-id='204'%3e%3ccircle cx='12' cy='12' r='10' data-evernote-id='205' class='js-evernote-checked'%3e%3c/circle%3e%3cpolyline points='8 12 12 16 16 12' data-evernote-id='206' class='js-evernote-checked'%3e%3c/polyline%3e%3cline x1='12' y1='8' x2='12' y2='16' data-evernote-id='207' class='js-evernote-checked'%3e%3c/line%3e%3c/svg%3e)

If you have ever typed something on a smartphone, you have likely seen it attempt to predict what you’ll write next. This article is about how text predictors work, and how crucial the input language dataset is for the resulting predictions. To see how this in action, we will predict tweets by four Twitter accounts: Barack Obama, Justin Timberlake, Kim Kardashian, and Lady Gaga.

To be able to make useful predictions, a text predictor needs as much knowledge about language as possible, often done by *machine learning*. We will look at a simple yet effective algorithm called *k Nearest Neighbours*. This works by looking at the last few words you wrote and comparing these to all groups of words seen during the training phase. It outputs the best guess of what followed groups of similar words in the past.

Here is an example of using *k Nearest Neighbours* to predict tweet text. After choosing a person and an example tweet, move the slider to various positions in the text and it will automatically detect the last *trigram* (group of three words). It creates a database of trigrams from all tweets from that account, then searches for similar ones. The best matching trigrams will be displayed, along with the word that most often followed them.

### k Nearest Neighbours

Pick a Twitter account
![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png)
![](../_resources/0f946c25887ac8654c883b16fb2db823.png)
![](../_resources/4af3aff369db95597cce7a6fb65966e5.png)
![](../_resources/ada09d53d84cac9813412369a6e54037.png)
Pick an example tweet
[1]()[2]()[3]()[4]()[5]()

Slide back and forth

Up early for a workout before the kids wake|
Best matching group of words from history

|     |     |
| --- | --- |
| 1.  | the kids to → Turks |
| 2.  | the kids in → honor |
| 3.  | the only person → on |

This approach is called *context-sensitive text prediction*. A downside of this technique is that it depends on similar groups of words being available in order to make a prediction. To go from this to a text predictor that would be good enough to be used in practice, we need two more things:

- As a backup, a list of words frequently used by the author
- Limiting the pool of probable predictions based on what the user already typed so far. For example, it does not make sense to predict the word “the” if the user typed “ca.”

The resulting predictor is a very simple statistical language model. It is built entirely of example language data—put in different data, get another model with new predictions. One way to see this is to let the models of our four celebrities predict each other’s tweets:

### Language Model with Example Data

Pick a Twitter account
![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png)
![](../_resources/0f946c25887ac8654c883b16fb2db823.png)
![](../_resources/4af3aff369db95597cce7a6fb65966e5.png)
![](../_resources/ada09d53d84cac9813412369a6e54037.png)
Pick an example tweet
[1]()[2]()[3]()[4]()[5]()

Slide back and forth

Chicago raising its minimum wage is another reminder: Congress needs to keep up and #RaiseTheWage for hard-working Americans nationwide|

Best predictions by language models
![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png)
@barackobama
![](../_resources/0f946c25887ac8654c883b16fb2db823.png)
@jtimberlake
![](../_resources/4af3aff369db95597cce7a6fb65966e5.png)
@kimkardashian
![](../_resources/ada09d53d84cac9813412369a6e54037.png)
@ladygaga

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| 1   | nationwid | nation. | nail | nationwid |
| 2   | nation. | nation | nails!!! | nation |
| 3   | nationall | nation. | name | nature |

As expected, the model using the same author’s data usually makes the best prediction. This follows the general idea in machine learning: when the desired output is more similar to the data used to create the model (i.e., the training data), the better the results. Put simply, you are your own best language predictor.

Instead of eyeballing which model works better, we can measure the models and count the number of correctly guessed characters. The percentages below indicate how accurately each Twitter account model is at predicting an account’s next words.

### Language Model with User Data

Pick a Twitter account
![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png)
![](../_resources/0f946c25887ac8654c883b16fb2db823.png)
![](../_resources/4af3aff369db95597cce7a6fb65966e5.png)
![](../_resources/ada09d53d84cac9813412369a6e54037.png)
Pick a Language model

|     |     |
| --- | --- |
| ![](../_resources/ada09d53d84cac9813412369a6e54037.png) | @ladygaga<br>44% |
| ![](../_resources/0f946c25887ac8654c883b16fb2db823.png) | @jtimberlake<br>32% |
| ![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png) | @barackobama<br>29% |
| ![](../_resources/4af3aff369db95597cce7a6fb65966e5.png) | @kimkardashian<br>29% |

Pick Example tweet
[1]()[2]()[3]()[4]()[5]()

33%

of the characters in this tweet were correctly predicted by the language model of @ladygaga

Ignore voices that aim to divide us, this only leads to more violence between people. We must unite as humans, where we are all the same.

The percentages above can serve as boundaries of what is possible with this technique. Again, the more similar two Twitter accounts are, the more likely they are to correctly predict each other's tweets. Justin Timberlake and Lady Gaga are each other's best predictors. Barack Obama and Kim Kardashian, on the other hand, are each other's worst predictors.

This may not be the case for individual tweets. For example, Kim Kardashian's tweet about “working together with organizations” was predicted better by the language model of Barack Obama than her own. In other words, “you are your own best language predictor” is more of a tendency than a hard rule.

Our examples have been active Twitter accounts with thousands of tweets. But how do we solve for people with less data? Look to the language from the people around you. People who talk to each other tend to speak more alike, an idea that could be very useful in this case.

We can simulate this effect on Twitter by following @ mentions as a loose proxy for “people who talk to each other a lot.” These are the conversation participants of our four Twitter accounts that they mentioned most frequently (more than 10 times):

- @BarackObama: @VP (17 mentions)
- @jtimberlake: @ChrisStapleton (16 mentions), @AnnaKendrick47 (15 mentions), @jimmyfallon (15 mentions)
- @KimKardashian: @MakeupByMario (18 mentions), @khloekardashian (13 mentions)
- @ladygaga: @itstonybennett (30 mentions), @MarkRonson (16 mentions), @faspiras (15 mentions)

These Twitter “friends” are of course highly dependent on the way Twitter is used; whereas Lady Gaga and Justin Timberlake often address colleagues and other celebrities, Barack Obama almost exclusively uses Twitter address larger groups of people.

Let’s take a look at how these “friend” models perform.

### Language Model with 'Friend' Data

Pick a Twitter account
![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png)
![](../_resources/0f946c25887ac8654c883b16fb2db823.png)
![](../_resources/4af3aff369db95597cce7a6fb65966e5.png)
![](../_resources/ada09d53d84cac9813412369a6e54037.png)
Pick a Language model

|     |     |
| --- | --- |
| ![](../_resources/b303c0fda9f256ec32d9656b6f41dffb.png) | @barackobama<br>59% |
| ![](../_resources/45335cb8a5e30f7c92d4fd21e2f47ea0.png) | @VP<br>36% |
| ![](../_resources/ada09d53d84cac9813412369a6e54037.png) | @ladygaga<br>33% |
| ![](../_resources/0f946c25887ac8654c883b16fb2db823.png) | @jtimberlake<br>32% |
| ![](../_resources/4af3aff369db95597cce7a6fb65966e5.png) | @kimkardashian<br>27% |

Pick Example tweet
[1]()[2]()[3]()[4]()[5]()

52%

of the characters in this tweet were correctly predicted by the language model of @VP

Chicago raising its minimum wage is another reminder: Congress needs to keep up and #RaiseTheWage for  hard-working Americans nationwide.

In terms of accuracy, “Friend” models rank directly after the personal models in almost all cases. Part of this effect is explained by overlapping topics: the models of Justin Timberlake and Lady Gaga are probably good at predicting each other’s tweets because they are both tweeting about topics like songs, concerts and fans. Something similar is likely happening with the predictions of @VP (Vice President) for the tweets of Obama. Although Obama only mentioned @VP when it was still being used by Joe Biden, the tweets of current Vice President Mike Pence are still good predictors because of their political nature. Overlapping topics, however, are not the whole story. Research has shown that even if you look at filler words, such as “the”, “but”, “and”, “is”, etc., [tweets by friends are still better](http://www.aclweb.org/anthology/E/E14/E14-1034.pdf)  [predictors than tweets by random people](https://www.narcis.nl/publication/RecordID/oai%3Arepository.ubn.ru.nl%3A2066%2F155926/coll/person/id/5/Language/en).

This technique makes it possible to make predictions of what somebody wants to say, even if we have no previous material of a particular person. This can be the case if somebody has word finding problems (aphasia) or cannot move their speech organs (because of, for example, paralysis). A word predictor can be of great help to such a person, and it can be trained with the language of the people around them, an idea known as “language transplantation”.

There you have it: a simple technique for language prediction and how playing the inputs—the training material—can influence the resulting predictions. It is not only a matter of feeding the predictor with language, but also of making sure this language is similar to the language it will need to predict. Even without an understanding of language, text predictors work g

Was this your jam? Preach.

|     |
| --- |
|     |

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fpudding.cool%2F2019%2F04%2Ftext-prediction%2F&ref_src=twsrc%5Etfw&text=How%20Algorithms%20Know%20What%20You%E2%80%99ll%20Type%20Next&tw_p=tweetbutton&url=https%3A%2F%2Fpudding.cool%2F2019%2F04%2Ftext-prediction%2F)

[![](../_resources/258331d19b200d0d2b7c9aa6ffe7f418.png) The Rise of Hyphenated Last Names in Pro Sports](https://pudding.cool/2019/05/hyphens)[![](../_resources/e54ab629c2f96f69ab1e6a61dabd904a.png) The NBA Has a Defensive Three Seconds Problem](https://pudding.cool/2019/05/three-seconds)[![](../_resources/88d6f056b1afa9fc751a948e782abc78.png) Colorism in High Fashion](https://pudding.cool/2019/04/vogue)[![](../_resources/7f50633c622ebda379b67180ee5a6ef3.png) Why Budapest, Warsaw, and Lithuania split themselves in two](https://pudding.cool/2019/04/eu-regions)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%23000000' stroke='currentColor' stroke-width='.2' stroke-linecap='round' stroke-linejoin='round' class='feather feather-facebook js-evernote-checked' data-evernote-id='689'%3e%3cpath d='M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z' data-evernote-id='690' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  FACEBOOK](https://facebook.com/pudding.viz/)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='%23000' stroke='currentColor' stroke-width='0' stroke-linecap='round' stroke-linejoin='round' class='feather feather-twitter js-evernote-checked' data-evernote-id='694'%3e%3cpath d='M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z' data-evernote-id='695' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  TWITTER](https://twitter.com/puddingviz/)
- [![](data:image/svg+xml,%3csvg width='24' height='24' version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 24 24' enable-background='new 0 0 24 24' xml:space='preserve' data-evernote-id='699' class='js-evernote-checked'%3e %3cpath d='M17%2c23H7c-3.3%2c0-6-2.7-6-6V7c0-3.3%2c2.7-6%2c6-6h10c3.3%2c0%2c6%2c2.7%2c6%2c6v10C23%2c20.3%2c20.3%2c23%2c17%2c23z M7%2c3C4.8%2c3%2c3%2c4.8%2c3%2c7v10 c0%2c2.2%2c1.8%2c4%2c4%2c4h10c2.2%2c0%2c4-1.8%2c4-4V7c0-2.2-1.8-4-4-4H7z' data-evernote-id='700' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M12%2c17c-1.1%2c0-2.1-0.3-3-1c-1.1-0.8-1.8-2-2-3.3C6.7%2c10%2c8.6%2c7.4%2c11.3%2c7c0.5-0.1%2c1-0.1%2c1.5%2c0c2.2%2c0.3%2c3.9%2c2%2c4.2%2c4.2l0%2c0 c0.2%2c1.3-0.1%2c2.6-0.9%2c3.7c-0.8%2c1.1-2%2c1.8-3.3%2c2C12.5%2c16.9%2c12.3%2c17%2c12%2c17z M12%2c9c-0.1%2c0-0.3%2c0-0.4%2c0c-1.6%2c0.2-2.8%2c1.8-2.5%2c3.4 c0.2%2c1.6%2c1.8%2c2.8%2c3.4%2c2.5c0.8-0.1%2c1.5-0.5%2c2-1.2s0.7-1.4%2c0.6-2.2l0%2c0c-0.2-1.3-1.2-2.3-2.5-2.5C12.3%2c9%2c12.2%2c9%2c12%2c9z' data-evernote-id='701' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M17.5%2c7.5c-0.3%2c0-0.5-0.1-0.7-0.3c-0.1-0.1-0.2-0.2-0.2-0.3c-0.1-0.1-0.1-0.2-0.1-0.4c0-0.3%2c0.1-0.5%2c0.3-0.7 c0.4-0.4%2c1-0.4%2c1.4%2c0c0.2%2c0.2%2c0.3%2c0.4%2c0.3%2c0.7c0%2c0.1%2c0%2c0.3-0.1%2c0.4s-0.1%2c0.2-0.2%2c0.3C18%2c7.4%2c17.8%2c7.5%2c17.5%2c7.5z' data-evernote-id='702' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)  INSTAGRAM](https://www.instagram.com/pudding.cool)
- [![](data:image/svg+xml,%3csvg version='1.1' id='Layer_1' width='24' height='24' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 24 24' enable-background='new 0 0 24 24' xml:space='preserve' data-evernote-id='706' class='js-evernote-checked'%3e %3cg data-evernote-id='707' class='js-evernote-checked'%3e %3cpath stroke-linecap='round' stroke-linejoin='round' d=' M15.7%2c3.3c-3.7%2c0-6.8%2c3-6.8%2c6.8c0%2c3.7%2c3%2c6.7%2c6.8%2c6.7c3.7%2c0%2c6.7-3%2c6.7-6.7C22.4%2c6.3%2c19.4%2c3.3%2c15.7%2c3.3' data-evernote-id='708' class='js-evernote-checked'%3e%3c/path%3e %3crect x='3.7' y='3.3' stroke-linecap='round' stroke-linejoin='round' width='3.3' height='18' data-evernote-id='709' class='js-evernote-checked'%3e%3c/rect%3e %3c/g%3e %3c/svg%3e)  PATREON](https://patreon.com/thepudding/)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='feather feather-mail js-evernote-checked' data-evernote-id='713'%3e%3cpath d='M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z' data-evernote-id='714' class='js-evernote-checked'%3e%3c/path%3e%3cpolyline points='22%2c6 12%2c13 2%2c6' data-evernote-id='715' class='js-evernote-checked'%3e%3c/polyline%3e%3c/svg%3e)  NEWSLETTER](http://eepurl.com/czym6f)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' class='feather feather-info js-evernote-checked' data-evernote-id='719'%3e%3ccircle cx='12' cy='12' r='10' data-evernote-id='720' class='js-evernote-checked'%3e%3c/circle%3e%3cline x1='12' y1='16' x2='12' y2='12' data-evernote-id='721' class='js-evernote-checked'%3e%3c/line%3e%3cline x1='12' y1='8' x2='12' y2='8' data-evernote-id='722' class='js-evernote-checked'%3e%3c/line%3e%3c/svg%3e)  ABOUT](https://pudding.cool/about)

 ![](data:image/svg+xml,%3csvg version='1.1' id='wordmark' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 200 50' style='enable-background:new 0 0 200 50%3b' xml:space='preserve' data-evernote-id='725' class='js-evernote-checked'%3e %3cg data-evernote-id='726' class='js-evernote-checked'%3e %3cpath class='st0 js-evernote-checked' d='M153.2%2c9.5c1.5%2c0%2c2.8%2c1.3%2c2.8%2c2.8s-1.3%2c2.8-2.8%2c2.8s-2.8-1.3-2.8-2.8S151.7%2c9.5%2c153.2%2c9.5z' data-evernote-id='727'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M150.3%2c17.3h5.6v18.2h-5.6V17.3z' data-evernote-id='728'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M80.2%2c9.5h-1.9h-7v19.3v6.7h5.6v-6.7v-1.4h1.4h1.9c4.9%2c0%2c8.9-4%2c8.9-8.9S85.2%2c9.5%2c80.2%2c9.5z M80.2%2c21.8h-1.9 h-1.4v-1.4v-3.8v-1.4h1.4h1.9c1.8%2c0%2c3.3%2c1.5%2c3.3%2c3.3C83.5%2c20.3%2c82.1%2c21.8%2c80.2%2c21.8z' data-evernote-id='729'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M108.8%2c17.6h-5.6v8.9c0%2c1.8-1.5%2c3.3-3.3%2c3.3s-3.3-1.5-3.3-3.3v-8.9H91v8.9c0%2c4.9%2c4%2c8.9%2c8.9%2c8.9s8.9-4%2c8.9-8.9 V17.6z' data-evernote-id='730'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M167.2%2c17.6c-4.9%2c0-8.9%2c4-8.9%2c8.9v8.9h5.6v-8.9c0-1.8%2c1.5-3.3%2c3.3-3.3s3.3%2c1.5%2c3.3%2c3.3v8.9h5.6v-8.9 C176.1%2c21.6%2c172.1%2c17.6%2c167.2%2c17.6z' data-evernote-id='731'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M122.8%2c16.2v1.4h-1.4h-1.9c-4.9%2c0-8.9%2c4-8.9%2c8.9s4%2c8.9%2c8.9%2c8.9h1.9h7V16.2V9.5l-5.6%2c3.3 C122.8%2c12.8%2c122.8%2c16.2%2c122.8%2c16.2z M122.9%2c24.6v3.8v1.4h-1.4h-1.9c-1.8%2c0-3.3-1.5-3.3-3.3s1.5-3.3%2c3.3-3.3h1.9h1.4V24.6z' data-evernote-id='732'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M142.4%2c16.2v1.4H141h-1.9c-4.9%2c0-8.9%2c4-8.9%2c8.9s4%2c8.9%2c8.9%2c8.9h1.9h7V16.2V9.5l-5.6%2c3.3V16.2z M142.5%2c24.6v3.8 v1.4H141h-1.9c-1.8%2c0-3.3-1.5-3.3-3.3s1.5-3.3%2c3.3-3.3h1.9h1.4v1.4H142.5z' data-evernote-id='733'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M186.8%2c17.6c-4.9%2c0-8.9%2c4-8.9%2c8.9s4%2c8.9%2c8.9%2c8.9h1.9h1.4v1.4v0.9v1.4v1.4c0%2c1.8-1.5%2c3.3-3.3%2c3.3 s-3.3-1.5-3.3-3.3V38l-5.6%2c3.3c0.4%2c4.5%2c4.2%2c8.1%2c8.9%2c8.1c4.9%2c0%2c8.9-4%2c8.9-8.9v-1.4v-2.3V17.6h-7H186.8z M190.1%2c23.4v1.4v3.8V30h-1.4 h-1.9c-1.8%2c0-3.3-1.5-3.3-3.3s1.5-3.3%2c3.3-3.3h1.9C188.7%2c23.4%2c190.1%2c23.4%2c190.1%2c23.4z' data-evernote-id='734'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M31.7%2c17.6c-1.2%2c0-2.3%2c0.2-3.3%2c0.6V9.5l-5.6%2c3.3v13.7v2v6.9h5.6v-6.9l0%2c0v-2c0-1.8%2c1.5-3.3%2c3.3-3.3 c1.8%2c0%2c3.3%2c1.5%2c3.3%2c3.3v8.9h5.6v-8.9C40.6%2c21.6%2c36.6%2c17.6%2c31.7%2c17.6z' data-evernote-id='735'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M20.9%2c9.5H3.1v5.6h6.1v20.3h5.6V15.1h6.1V9.5z' data-evernote-id='736'%3e%3c/path%3e %3cpath class='st0 js-evernote-checked' d='M51.4%2c30.2c-0.4%2c0-1.2-0.1-1.8-0.4l5.2-2.1l5.6-2.3l-1-2.3l-0.1-0.2c-0.1-0.3-0.3-0.6-0.5-1 c-0.1-0.1-0.1-0.2-0.2-0.3c0%2c0%2c0-0.1-0.1-0.1l-0.1-0.1l-0.1-0.1c-1.6-2.2-4-3.5-6.7-3.7l0%2c0H51c-4.9%2c0-8.9%2c4-8.9%2c8.9 c0%2c0.4%2c0%2c0.9%2c0.1%2c1.4l0%2c0V28c0%2c0%2c0%2c0%2c0%2c0.1c0%2c0%2c0%2c0%2c0%2c0.1c0%2c0.3%2c0.1%2c0.5%2c0.2%2c0.8v0.1v0.1c0.1%2c0.3%2c0.2%2c0.7%2c0.4%2c1v0.1v0.1 c0.1%2c0.3%2c0.3%2c0.5%2c0.4%2c0.8c0%2c0.1%2c0.1%2c0.1%2c0.1%2c0.2l0%2c0c0.1%2c0.2%2c0.3%2c0.4%2c0.4%2c0.6c0%2c0%2c0%2c0%2c0%2c0.1c0%2c0%2c0%2c0.1%2c0.1%2c0.1l0.1%2c0.1 c1.7%2c2.1%2c4.4%2c3.4%2c7.2%2c3.4h6.1v-5.2C57.6%2c30.2%2c53.7%2c30.2%2c51.4%2c30.2L51.4%2c30.2z M59.3%2c22.9L59.3%2c22.9L59.3%2c22.9z M47.7%2c25.7 L47.7%2c25.7l-0.2%2c0.1c0.2-1.9%2c1.8-3.5%2c3.7-3.5c0.9%2c0%2c1.8%2c0.4%2c2.4%2c0.9L49.3%2c25L47.7%2c25.7L47.7%2c25.7z' data-evernote-id='737'%3e%3c/path%3e %3c/g%3e %3c/svg%3e)

[The Pudding](https://pudding.cool/) is a digital publication that explains ideas debated in culture with visual essays.

The Pudding® is made in Brooklyn, NY; Seattle, WA; and Great Barrington, MA.