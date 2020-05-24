Does everyone hate your tweets? Google Cloud Platform NLP can help!

# Does everyone hate your tweets? Google Cloud Platform NLP can help!

[![0*9X5sEo81ZcoGPI8F](../_resources/01e3cac5b8e2115107ebda866b52f2ca.jpg)](https://medium.com/@elaina.hyde?source=post_header_lockup)

[Dr. Elaina Hyde](https://medium.com/@elaina.hyde)
Nov 5, 2018·6 min read

![](../_resources/c6829322cfae78499fa2b466f0324fd7.png)![1*Nd-7gxabJcL6EnPWHdWDiw.jpeg](../_resources/10d4edcd144dbb7dddea3e2c6540bb40.jpg)

Have you ever wondered just how your favourite tech company was ‘really’ doing? Wanted to track the hashtags you create or someone else’s on Twitter? Well, it turns out there is an easy way you can get access and run some very powerful Natural Language Processing (NLP) with very little training for your machine learning algorithms. We are going to use Python but we can avoid the nltk package altogether!

So, how do we get started? Well, firstly let’s pick one of the most common problems on Twitter, negative comments and posts. How can we track negativity over time in the things that we are interested in? For the purposes of this article, I am going to investigate the hashtag ‘#Google’. The first step is to be able to pull data off of Twitter and into the Google Cloud Platform (GCP).

Dealing with streaming data on GCP is easy if you write a small pipeline in Dataflow. Fortunately this pipeline process was recently published by Servian’s Graham Polley on Medium over [here](https://medium.com/weareservian/tweets-pipelines-gcp-and-poetry-how-did-it-get-to-this-2a6e47fb3f6a).

How are we going to build our pipeline? Following Graham’s article above, we can refer to the general solution on GCP (below).

![1*pYIqmUpA3AtLESPT0rkH4A.png](../_resources/fc0814f2b14c3a1b83215b6e5e0e3b48.png)

The General Process for a Solution of bringing real-time data into GCP (from GCP Official Icons and Sample Diagrams downloadable .pptx)

We are pulling twitter data in by picking a few of the tools shown above and using them to the best effect. In particular we concentrate on Dataflow and BigQuery. The Dataflow pipeline is the same type of pipeline used by Graham and is written in Java and uses Cloud Build to deploy. The JSON data can go directly into our Data Warehouse of BigQuery. It is necessary to set up a [developer account](https://developer.twitter.com/) with Twitter first, so if you are starting from scratch make sure to do that right away as it can take a few days to get approved.

Once our Twitter data is on GCP we can start to reap the benefits of the GCP architecture right away. Our data lands in BigQuery, one of my all time favourite data tools on GCP and hands down the best place to access data for analytics. The very fast querying of massive datasets is just what we need to easily process the tweets our pipeline pulls in. For more on BigQuery, pop over [here](https://cloud.google.com/bigquery/).

So now what? Well, prototyping any Machine Learning on GCP is very easy and get’s us to my second favourite tool of all time, Google Cloud Datalab**.** It’s so good sometimes it even ties with BigQuery. Datalab offers a Pythonic notebook interface in the GCP environment built on Jupyter. It has interfaces which make for easy SQL querying of BigQuery data, easy bash access, and lots of special commands that we won’t cover here, but check its [% commands](https://googledatalab.github.io/pydatalab/google.datalab%20Commands.html#) when you get a chance.

![1*z2SxpferJTRSTZya74r53A.png](../_resources/08eca52ad5715c845890460cccf47d35.png)
https://cloud.google.com/datalab/

Once we are running Datalab, we can dive right into Natural Language Processing (NLP). NLP uses algorithmic approaches to text to identify sentiment, extract information, and otherwise analyse text. These algorithms generally take a large amount of training and can be cumbersome to construct in traditional methods. However, we will circumvent all of this with the [Google NLP API](https://cloud.google.com/natural-language/).

The NLP API is a pre-trained machine learning algorithm that is behind such technology as Google Assistant, Google Translate and more. We will use it to extract polarity and magnitude from the tweets in our data. Polarity is how negative or positive a statement is, while the magnitude is how ‘strong’ that same statement is: *“I love Google Cloud Platform!”* would be a strongly positive statement, i.e. high magnitude and positive polarity**.**  *“Sometimes, but not always, I feel a little bit frustrated when I am trying to set my row keys in Bigtable.”* would be a weakly negative statement, i.e. low magnitude and negative polarity.

So what first? Inside Datalab we look at our BigQuery data:
![1*uY6hi0tHs1LiMoGV027ang.png](../_resources/914cf2b2975d39f1e5bffd8578619811.png)
Pipeline written from Twitter data into BigQuery

Once our data is read into a data frame in Python we can see that #Google occurs in 582/11030 tweets. We could wait for more data to stream in, but this is enough for our purposes. We call our data frame ‘google’ and to extract polarity and magnitude for all #Google tweets we just import build and run an `analyzeSentiment()` of each tweet.

![1*pCRxaLd7CZv9KC-0Hr9ImQ.png](../_resources/8eb84f22b64817ac578174a867d8daa5.png)
Calling the Google NLP API

Note, if you are doing this for the first time, you will need to set up an API key in your GCP account for the NLP API to be used. Now that we have all our data, we can look at magnitude and polarity over time for #Google.

![1*JMrtpKLChhY5A5DnWhfRMA.png](../_resources/4d5e56f0b28a58ed371515fcb50bab77.png)
Magnitude of #Google over a few minutes
![1*Pz2IZfaZJsD2kMNXUriabA.png](../_resources/aea974b8383742811bb5ccf7c25211f1.png)
Polarity of #Google over a few minutes

At first this looks very messy, but fortunately if we want to see how many ‘loves’ and ‘hates’ #Google**  **has over this period, we are actually only looking for strongly negative or positive tweets (high absolute polarity, and high magnitude). Our dataset shows the the spread in polarity and magnitude for our hashtag.

![1*KMx4hkZY3bfBlz1sP4rZvw.png](../_resources/38666f20c0e6fbd715a3df58ed7e7bb1.png)
#Google Polarity and Magnitude on Nov 1 2018

It looks like we have higher polarity (positive) tweets at the higher magnitudes (stronger statements) which is good to see for our #Google. Maybe not everyone hates our hashtag! We can look further by separating our tweets into loves and hates with simple Python and use data frames for easy plotting.

![1*o9kOQkXlEJlAPOXV187wKg.png](../_resources/77b068456cefd49c7f3294cd6ad36241.png)
loves (purple) and hates (red) from sentiment analysis

Looking at these in terms of total number of tweets we can see a problem with #Google right away.

![1*ygyQoCQ17FZjSznmhiXVww.png](../_resources/c6de8e225ef189dc6d984456f0cdd2e2.png)
Total type of each tweet

Firstly, weak tweets seem to dominate, also we are not getting as many (numerically) loves as hates. Does everyone hate our tweets?

Fortunately, if we investigate the loves and hates we can see a redeeming feature in our tweets. In particular, now that we have our loves and hates, we can see how they behave over time.

![1*XjZSDSUCVJkMkPXxjg-7HQ.png](../_resources/f6bd63909d37c7d5d799153a177dba67.png)
Magnitude of loves (green) and hates (black)

So does everyone hate #Google tweets? Fortunately, no! The loves in green above have the highest magnitude, i.e. the strongest sentiment. The hates in black have in general lower, towards our cutoff, values. So, there are a good deal of loves and hates, strong magnitude tweets, but they do fluctuate quite a good deal in the data we have managed to capture. Even though we have numerically more hates, it is the loves that have the strongest magnitude.

*> “There is always some madness in love. But there is also always some reason in madness.”*>

> – Friedrich Nietzsche
What’s next?

We could check any other hashtags we cared to invent, or even look for accounts that were tweeting the most positive or negative content, look for trends over time or even set up flagging. Now that our data is in BigQuery and we have set up Datalab, the sky (or the cloud in any case) is the limit.

Want to see more? The code for this investigation is on my GitHub account [here](https://github.com/AstroHyde/gcp-tweets-streaming-pipeline). Thanks for reading!