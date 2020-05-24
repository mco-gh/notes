A Simple Way to Gather all Coronavirus Related Data with Python

# A Simple Way to Gather all Coronavirus Related Data with Python

## Simplicity is key.

[![2*hGvXTf0laRK-M-2f8dMaoQ.png](../_resources/f495fd4e101cdcbd7c0c7f4815280bd2.png)](https://towardsdatascience.com/@federicoriveroll?source=post_page-----19aa22167dea----------------------)

[Federico Riveroll](https://towardsdatascience.com/@federicoriveroll?source=post_page-----19aa22167dea----------------------)

[Mar 13](https://towardsdatascience.com/gather-all-the-coronavirus-data-with-python-19aa22167dea?source=post_page-----19aa22167dea----------------------) · 6 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='199'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='200' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

The recent **outburst of Coronavirus** disease confirmations is alarming.

Up to today (March 13th 2020) there are over [**126,343 confirmed cases of Coronavirus**](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)**.**

![1*b6IPidiW8-2odq5LA-A1gQ.png](../_resources/fa5ae1956026d011b7e45c4971eac920.png)
![1*b6IPidiW8-2odq5LA-A1gQ.png](../_resources/68535c03dcf9ec5dd4805bd5fd1918a4.png)

Taken from CSSE COVID-19 [live map](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)

# Objective

The objective of this article is to **get the needed data **for research and **gain proactive visibility** on COVID-19.

# Steps

- Step 1: Set up technical **prerequisites**
- Step 2: Gather **COVID-19** confirmed cases
- Step 3: Gather **News** of COVID
- Step 4: Gather **Financial** and other **Indicators**
- Step 5: **Blend all **the data together

# Step 1. Prerequisites

- Have Python 2.6+ or 3.1+ installed
- Install pandas, matplotlib, openblender and wordcloud(with pip)

$ pip install pandas OpenBlender matplotlib wordcloud

# Step 2. Gather COVID-19 confirmed cases

The CSSE is doing the amazing job of **uploading the daily data**  [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports). However, it is wildly **untidy** and on many different datasets, so** I sorted it and uploaded it as a single **OpenBlender [dataset](https://www.openblender.io/#/dataset/explore/5e6ac97595162921fda18076/or/35):

![1*hqwQwrk_6i2cShKQLQdn8Q.png](../_resources/462d76e5ce591ede6836bb1534f0c77e.png)
![1*hqwQwrk_6i2cShKQLQdn8Q.png](../_resources/b39b91850ef4764267c96613adc08d40.png)
Let’ pull the data **into a Pandas dataframe** by running this script:
from matplotlib import pyplot as plt
import OpenBlender
import pandas as pd
import json
%matplotlib inline
action = 'API_getObservationsFromDataset'parameters = {
'token':'**YOUR_TOKEN_HERE**',
'id_dataset':'5e6ac97595162921fda18076',
'date_filter':{
"start_date":"2020-01-01T06:00:00.000Z",
"end_date":"2020-03-11T06:00:00.000Z"},
'consumption_confirmation':'on'
}

df_confirmed = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)

df_confirmed.reset_index(drop=True, inplace=True)
df_confirmed.head(10)
![1*3R9GdV6NI3FGMZ9Zh_MFXA.png](../_resources/544f09be7cb88a4b58eea6147cfd378a.png)
![1*3R9GdV6NI3FGMZ9Zh_MFXA.png](../_resources/159104c1f994f30c3145d443a9138841.png)

- **Note**: To get a token you *need* to create an account on [openblender.io](https://www.openblender.io/#/welcome/or/35) (free), you’ll find it in the ‘Account’ tab on your profile icon.

So now we have the -aggregated by day and by location- number of **confirmed cases**, **deaths** and **recoveries**.

![0*pdbwvPfsv6qeLiG_.png](../_resources/2cbd402e70617f26c5e5684f37f90b64.png)
![0*pdbwvPfsv6qeLiG_.png](../_resources/824e40320163bb30cd90ccbde0f80ca7.png)

Here we can see the **outburst of confirmed cases** in Iran, Italy and Korea. We can also see Spain, France and Germany starting to **rise**.

# Step 3. Gather News of COVID-19

We’ll gather **COVID news** and texts from these sources: [ABC News](http://5d8848e59516294231c59581/), [Wall Street Journal](https://www.openblender.io/#/dataset/explore/5e2ef74e9516294390e810a9), [CNN News](https://www.openblender.io/#/dataset/explore/5d571b9e9516293a12ad4f5c) and[USA Today Twitter](https://www.openblender.io/#/dataset/explore/5e32fd289516291e346c1726) (you can look for other sources)

![0*zYZo9zT0N0VtI8S0.png](../_resources/ed8b1deef4449aae88566e9810a974a0.png)
![0*zYZo9zT0N0VtI8S0.png](../_resources/30358f05e2d7dc61cd36a367a51bc5c7.png)
So let’s fetch the data.
action = 'API_getOpenTextData'parameters = {
'token':'**YOUR_TOKEN_HERE**',
'consumption_confirmation':'on',
'date_filter':{"start_date":"2020-01-01T06:00:00.000Z",
"end_date":"2020-03-10T06:00:00.000Z"},
'sources':[

# Wall Street Journal

{'id_dataset' : '5e2ef74e9516294390e810a9',
'features' : ['text']},

# ABC News Headlines

{'id_dataset':"5d8848e59516294231c59581",
'features' : ["headline", "title"]},

# USA Today Twitter

{'id_dataset' : "5e32fd289516291e346c1726",
'features' : ["text"]},

# CNN News

{'id_dataset' : "5d571b9e9516293a12ad4f5c",
'features' : ["headline", "title"]}
],
'aggregate_in_time_interval' : {
'time_interval_size' : 60 * 60 * 24
},
'text_filter_search':['covid', 'coronavirus', 'ncov']

}

df_news = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)df_news.reset_index(drop=True, inplace=True)

Above, **we specified** the following:

- We selected our 4 **sources to gather data **from. Specifically, the feature columns with the text
- We specified we want data** from Jan 1st to today **(10th of March)
- We asked to aggregate the news into **24 hour groups** or observations
- We **filtered the news** which mentioned ‘covid’, ‘coronavirus’ or ‘ncov’

# Let's take a look

df_news.head(20)
![0*r6ClacVLOG28Dz8N.png](../_resources/f93b9f72e3af74fba47221fae776c367.png)
![0*r6ClacVLOG28Dz8N.png](../_resources/3233ac6071dd1d98a9279a0515a3ec87.png)

Every observation is the **aggregation of news by day**, we have the **source** which is the concatenation of all news into a string and the **source_lst** which is a list of the news of that interval.

The **timestamp** (which is returned as [unix timestamp](https://www.epochconverter.com/)) means the news happened **in the interval** from the prior timestamp to the current one (strictly before):

![0*98xbzdshiNlsnjtB.png](../_resources/e29ff8f4a47c3c564488ae0f96f46055.png)
![0*98xbzdshiNlsnjtB.png](../_resources/ac4eccded1fb67399aa4e9527fa9e86b.png)
Now let’s get the **mentions count **for some *countries of interest*.

interest_countries = ['China', 'Iran', 'Korea', 'Italy', 'France', 'Germany', 'Spain']for country in interest_countries:

df_news['count_news_' + country] = [len([text for text in daily_lst if country.lower() in text]) for daily_lst in df_news['source_lst']]df_news.reindex(index=df_news.index[::-1]).plot(x = 'timestamp', y = [col for col in df_news.columns if 'count' in col], figsize=(17,7), kind='area')

![0*RHagVzkChsA6ekHn.png](../_resources/c4278a688e8ad85d3d31db261c0d3be2.png)
![0*RHagVzkChsA6ekHn.png](../_resources/7e7d6f795c97324109271abe6440f206.png)
![0*3J-jyEGSbM49Lrwb](../_resources/77b2572388f2019c8c4a34ac06757f9f.png)
![1*cOHStEBs8c7I8pS6H1GB-A.png](../_resources/77b2572388f2019c8c4a34ac06757f9f.png)

Let’s look at a word cloud from the **last 20 days** of news. **optional step (if you want to install wordcloud*):

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGeneratorplt.figure()

plt.imshow(WordCloud(max_font_size=50, max_words=80, background_color="white").generate(' '.join([val for val in df['source'][0: 20]])), interpolation="bilinear")

plt.axis("off")
plt.show()plt.figure()

plt.imshow(WordCloud(max_font_size=50, max_words=80, background_color="white").generate(' '.join([val for val in df['source'][0: 20]])), interpolation="bilinear")

plt.axis("off")
plt.show()
![0*5YMPESvAE6rHtf8g.png](../_resources/8558ac998dcfaa169d7554c23b220d97.png)
![0*5YMPESvAE6rHtf8g.png](../_resources/1325484339ef4e8a5f4d671248ae35b8.png)
*The code above generated the last wordcloud of the image.

Keywords in the early news such as “mystery”, “investigating”, “dozens” **contrast with posterior keywords** such as “china”, “coronavirus”, “global”. And **even more** with the most recent ones: “New coronavirus”, “coronavirus epidemic”, “outbreak”, “cruise”, “novel coronavirus” etc..

# Step 4. Gather Financial and other Indicators

For this we can part from the Dow Jones Dataset and blend several others such as **exchange rates **(Yen, Euro, Pound), **material prices **(Crude Oil, Corn, Platinum, Tin), or **stock **(Coca Cola, Dow Jones).

action = 'API_getObservationsFromDataset'

parameters = {
'token':'**YOUR_TOKEN_HERE**',

'id_dataset':'5d4c14cd9516290b01c7d673', 'aggregate_in_time_interval':{"output":"avg","empty_intervals":"impute","time_interval_size":86400}, 'blends':[

#Yen vs USD

{"id_blend":"5d2495169516290b5fd2cee3","restriction":"None","blend_type":"ts","drop_features":[]}, # Euro Vs USD

{"id_blend":"5d4b3af1951629707cc1116b","restriction":"None","blend_type":"ts","drop_features":[]}, # Pound Vs USD

{"id_blend":"5d4b3be1951629707cc11341","restriction":"None","blend_type":"ts","drop_features":[]}, # Corn Price

{"id_blend":"5d4c23b39516290b01c7feea","restriction":"None","blend_type":"ts","drop_features":[]}, # CocaCola Price

{"id_blend":"5d4c72399516290b02fe7359","restriction":"None","blend_type":"ts","drop_features":[]}, # Platinum price

{"id_blend":"5d4ca1049516290b02fee837","restriction":"None","blend_type":"ts","drop_features":[]}, # Tin Price

{"id_blend":"5d4caa429516290b01c9dff0","restriction":"None","blend_type":"ts","drop_features":[]}, # Crude Oil Price

{"id_blend":"5d4c80bf9516290b01c8f6f9","restriction":"None","blend_type":"ts","drop_features":[]}],'date_filter':{"start_date":"2020-01-01T06:00:00.000Z","end_date":"2020-03-10T06:00:00.000Z"},

'consumption_confirmation':'on'

}df = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)

df.reset_index(drop=True, inplace=True)print(df.shape)
df.head()
![1*cDLr6DCpBWovjMR-UaNBGA.png](../_resources/3385de30e3e1cf84f8b949bb6424c1eb.png)
![1*cDLr6DCpBWovjMR-UaNBGA.png](../_resources/7774245e43122f6b4892056a3203e211.png)

So now we have** a single dataset** with daily observations of prices blended by time. If we want to compare them, we better normalize them between 0 and 1, so that we can better appreciate the patterns:

# Lets compress all into the (0, 1) domain

df_compress = df.dropna(0).select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).apply(lambda x: (x - x.min()) / (x.max() - x.min()))

df_compress['timestamp'] = df['timestamp']# Now we select the columns that interest us

cols_of_interest = ['timestamp', 'PLATINUM_PRICE_price', 'CRUDE_OIL_PRICE_price', 'COCACOLA_PRICE_price', 'open', 'CORN_PRICE_price', 'TIN_PRICE_price', 'PLATINUM_PRICE_price']

df_compress = df_compress[cols_of_interest]

df_compress.rename(columns={'open':'DOW_JONES_price'}, inplace=True)# An now let's plot them

from matplotlib import pyplot as plt
fig, ax = plt.subplots(figsize=(17,7))

plt = df_compress.plot(x='timestamp', y =['PLATINUM_PRICE_price', 'CRUDE_OIL_PRICE_price', 'COCACOLA_PRICE_price', 'DOW_JONES_price', 'CORN_PRICE_price', 'TIN_PRICE_price', 'PLATINUM_PRICE_price'], ax=ax)

![1*oTzJVZt4m-i1I5mvo3IaAw.png](../_resources/6f770ec216526656109a620778e30529.png)
![1*oTzJVZt4m-i1I5mvo3IaAw.png](../_resources/c2935b548a526871fca987a6c65233e9.png)

It’s interesting how **almost all of them** (except for the Tin price) follow a **similar pattern**.

# Step 5. Blend all the data together

Now, we will align the **COVID-19 confirmed cases**, the **coronavirus news **and the **economical indicators** data into **one single dataset** blended by time.

To blend the data let’s upload the datasets we created to OpenBlender:

# First the News Datasetaction = 'API_createDataset'parameters = {

'token':'**YOUR_TOKEN_HERE**',
'name':'Coronavirus News',
'description':'YOUR_DATASET_DESCRIPTION',
'visibility':'private',
'tags':[],
'insert_observations':'on',
'select_as_timestamp' : 'timestamp',
'dataframe':df_news.to_json()
}

OpenBlender.call(action, parameters)
![1*SG88vgqmc-J6-t3K4QnTnQ.png](../_resources/f91c1f710e8b4097037de2849d78b3d3.png)
![1*SG88vgqmc-J6-t3K4QnTnQ.png](../_resources/2e821b5969447671aa6a4133ff94328b.png)

# And now the Financial Indicatorsaction = 'API_createDataset'parameters = {

'token':'**YOUR_TOKEN_HERE**',
'name':'Financial Indicators for COVID',
'description':'YOUR_DATASET_DESCRIPTION',
'visibility':'private',
'tags':[],
'insert_observations':'on',
'select_as_timestamp' : 'timestamp',
'dataframe':df_compress.to_json()
}

OpenBlender.call(action, parameters)
![1*ZVXoQxZ_dNkbfTepkhrqcQ.png](../_resources/366742e5c1383b726c84076d899093c5.png)
![1*ZVXoQxZ_dNkbfTepkhrqcQ.png](../_resources/3ad6e5f740e6c8eb867feb166b3ac706.png)
**NOTE: you’ll want the ‘id_dataset’ for each dataset to use below.*

And now we just pull the initial COVID-19 dataset and we blend the new datasets we created by replacing the “id_dataset”.

action = 'API_getObservationsFromDataset'# ANCHOR: 'COVID19 Confirmed Cases'

# BLENDS: 'Coronavirus News', 'Financial Indicators for COVID'

parameters = {
'token':'**YOUR_TOKEN_HERE**',
'id_dataset':'5e6ac97595162921fda18076',
'date_filter':{
"start_date":"2020-01-01T06:00:00.000Z",
"end_date":"2020-03-11T06:00:00.000Z"} ,

},'filter_select' : {'feature' : 'countryregion', 'categories' : ['Italy']},'aggregate_in_time_interval':{"output":"avg","empty_intervals":"impute","time_interval_size":86400}, 'blends':[{"id_blend":"**YOUR_CORONA_NEWS_ID**","restriction":"None","blend_type":"ts","drop_features":[]},

{"id_blend":"**YOUR_FINANCIAL_INDICATORS_ID**","restriction":"None","blend_type":"ts","drop_features":[]}]

}df = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)

df.reset_index(drop=True, inplace=True)

Above we **selected observations for ‘Italy’**, **aggregated by day **in seconds (8640) and **blended the new data**.

df.head()

![1*cOHStEBs8c7I8pS6H1GB-A.png](../_resources/b9434badc62d7ff2fcf15830934fd3cc.png)

And now we have a dataset with the **daily information of all the data** blended by time!

**There is an enormous range of directions to go with this.**
Please post further findings.