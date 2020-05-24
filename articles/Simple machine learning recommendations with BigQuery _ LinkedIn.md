Simple machine learning recommendations with BigQuery | LinkedIn

#  Simple machine learning recommendations with BigQuery

- Published on May 9, 2020

[  ![0](../_resources/f3a3f9a63b8c7b2cacc56b88372b793a.jpg)](https://www.linkedin.com/in/tlatum/)

[ ##  Thomas van Latum](https://www.linkedin.com/in/tlatum/)

  Google Cloud Architect & Data Engineer at g-company

[3 articles](https://www.linkedin.com/in/tlatum/detail/recent-activity/posts/)

One of the coolest features of BigQuery is the ability to create machine learning models only with SQL. Today I'm going to show you how to create simple recommendations using BigQuery's matrix factorization! The data we are going to use is a simple dataset containing the click behaviour of users.

![0](../_resources/855ab1d3444b9cd1d27e7dc76db985e1.png)
The dataset has a row for each click user that views a product on the website.

What we need for the recommendation is a rating so let's create a view containing the number of views per user, per product. Im using a materialized view so I don't have to worry about updates coming in in the source table.

CREATE MATERIALIZED VIEW orders.count_views AS

SELECT user_id, product_id, count(*) as views FROM `experiment-center.orders.product_views`

GROUP BY 1,2

Because number of clicks on a product are implicit ratings we will use BigQuery's implicit matrix factorization. There is an awesome guide about recommendations from [explicit movie ratings](https://cloud.google.com/bigquery-ml/docs/bigqueryml-mf-explicit-tutorial).

Now let's create our model using only SQL! Pro tip, to create a matrix factorization model you need to setup reservations in BigQuery this can be a complex process in some situations. If you need help with how to setup reservations in your organisation give me a shout.

CREATE OR REPLACE MODEL orders.implicit_reccomendation
OPTIONS
  (model_type='matrix_factorization',
   feedback_type='implicit',
   user_col='user_id',
   item_col='product_id',
   rating_col='rating',
   num_factors=5) AS
SELECT
  user_id,
  product_id,
  views / (select max(views) from orders.count_views) AS rating
FROM orders.count_views

For the model to work you need to specify the user, item and rating columns and the number of factors. Generally the lower the amount of unique combinations of users and items the lower number of factors you use. No worries BigQuery will warn you if your number of factors is too high! Also note that I've normalised the ratings to lie between 0 and 1. When the training is complete you get some nice graphics about the training phase.

![0](../_resources/f37266378f80be498252438a68ca85df.png)

### Let's create recommendations!

SELECT
  *
FROM
  ML.RECOMMEND(MODEL orders.implicit_reccomendation,
  (SELECT "94931308-2317-43ce-b1bc-e83e6d4fe581" as user_id))
  order by predicted_rating_confidence desc
![0](../_resources/c32be4fc255edc1a1b551a623da977c9.png)

Fun fact, in the dataset the product with the highest recommendation only received one click from this user! With this model you can create product recommendations for your users. You can even export this model to deploy in your machine learning pipeline!

There are optimisations that can be done with BigQuery ML, like adding l2 regularisation and the number of iterations. If you need help with creating or optimising your model or if you want to talk about other BigQuery ML options send me a message.

### Published by

[   ![0](../_resources/f3a3f9a63b8c7b2cacc56b88372b793a.jpg)](https://www.linkedin.com/in/tlatum/)

[Thomas van Latum](https://www.linkedin.com/in/tlatum/)

Google Cloud Architect & Data Engineer at g-company

Published • 1w

[3 articles](https://www.linkedin.com/in/tlatum/detail/recent-activity/posts/)

BigQuery allows us to create Machine Learning models using only SQL! With the matrix factorization now in Beta we can build a simple recommendation model![hashtag#machinelearning](https://www.linkedin.com/feed/hashtag/?keywords=%23machinelearning)  [hashtag#bigquery](https://www.linkedin.com/feed/hashtag/?keywords=%23bigquery)  [hashtag#sql](https://www.linkedin.com/feed/hashtag/?keywords=%23sql)  [hashtag#googlecloud](https://www.linkedin.com/feed/hashtag/?keywords=%23googlecloud)  [hashtag#googlecloudplatform](https://www.linkedin.com/feed/hashtag/?keywords=%23googlecloudplatform)

- ·

-

###  Reactions

- [![0](../_resources/ff225a6ddfdacdc665bf43092d35a188.jpg)  ![4apjgdq5oe23g1kq83ov0fzvd](../_resources/12b9948059fb127dd5f36e3b0469194a.png)](https://www.linkedin.com/in/elange1?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAANYEkkBci1KB3IY7pBuAFtfmVSExuvoSg4)

- [![0](../_resources/9c5640a1a0f332ffeeac47563cc9154f.jpg)  ![](../_resources/12b9948059fb127dd5f36e3b0469194a.png)](https://www.linkedin.com/in/sam-pitcher-84523b6b?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAA7OifUBt2FcyL9LVGC9DXWp8c1LvscfrxE)

- [![0](../_resources/18ae9cb9c85354f9fda0b89aa26f650b.jpg)  ![dac2q1ju00de2yxodwdu2hfz7](../_resources/12b9948059fb127dd5f36e3b0469194a.png)](https://www.linkedin.com/in/marissa-horst?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABkkOc4B1Yy33ElGRWKFkrB9b6OWZjUgIKs)

- [![0](../_resources/364805be1d159916e82446623e7a4138.jpg)](https://www.linkedin.com/in/nazmi-asri?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAA8cOyEB8FJ8g5s9x59nRryqDL84B8Abies)

- [![0](../_resources/83b2902cf45985c6d367c7a353688891.jpg)](https://www.linkedin.com/in/irajanpatel?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFf5xABgh3KCPJnDB5ROvMTFOu59j-jKaI)

- [![0](../_resources/8b3c409386abd1ec17157d0a57ab90e2.jpg)](https://www.linkedin.com/in/erikreiken?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAABuq5MBSBOGF_0_H1UcKt5qkStYnPYkdY8)

- [![0](../_resources/116a6e1629d23954595bb26b6c220474.png)](https://www.linkedin.com/company/vertabelo/?miniCompanyUrn=urn%3Ali%3Afs_miniCompany%3A10928843)

- [![0](../_resources/aa10677645becec70ba3de309350a604.jpg)](https://www.linkedin.com/in/jochen-abrams-a631a610?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAIp5GsB-qzv1XXILUZH45h5ItOyYMN9Uro)

- [![0](../_resources/6e88fb9b3851fc08607d26d3a89485a9.jpg)](https://www.linkedin.com/in/lennartbenoot?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAABxncoBSvN7PnrXkryXHMNeuS8KLwJh6a4)

- [![0](../_resources/73f89e2421a7fc1ccaf108fd83453d9c.jpg)](https://www.linkedin.com/in/jeroenhovinga?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAABKdHkB-BlUbQ9r0BFCE3Ls-Y0V34yjGOc)

-

###    6 Comments    Comments on Thomas van Latum’s article

 ![0](../_resources/439b6ff028aa67e7226e4a02d8b11473.jpg)

*Add a comment…*

[  ![0](../_resources/bf126dcac78d0291d4c5053e3369cde4.jpg)](https://www.linkedin.com/in/eftimiesilviudaniel/)  [ ###     Silviu Daniel Eftimie  • out of network3rd+     Senior Data Engineer at BMind Sales Maker Company S.L.](https://www.linkedin.com/in/eftimiesilviudaniel/)

 1w

Nice tutorial/post [Thomas van Latum](https://www.linkedin.com/in/ACoAAAvGgSUBhkRf6pWzNnaRv1VNI4lBSGlY61w/) . Back to '18, BigQuery ML catch my eye for his simplicity of doing ML with SQL. Great to see that it's evolving. Also I have 3 questions: - How much focus and dedication are allocated from BQ team on BQ ML part? - I would love to take a look & give it a spin on BQ ML with XGBoost, DNN & Build Time Series forecasting (Alpha) models. [BMIND](https://www.linkedin.com/company/10226436/) it's one of the partners of Google on all this pillars: Cloud, Analytics and Advertising.  - Can you recommend a tutorial/post/book related with BQ ML + TensorFlow custom models? (all the steps)

Thank you !

 ·

·

[  ![0](../_resources/f3a3f9a63b8c7b2cacc56b88372b793a.jpg)](https://www.linkedin.com/in/tlatum/)  [ ###     Thomas van Latum  • 2nd degree connection2nd     Google Cloud Architect & Data Engineer at g-company](https://www.linkedin.com/in/tlatum/)

 1w

Thanks [Silviu Daniel Eftimie](https://www.linkedin.com/in/ACoAAAMEA9EBa5S7Mqm72QobPodDKs275XD0a-A/), I don't know the dedication on BQ ML but the release notes show the dedication in my opinion: https://cloud.google.com/bigquery-ml/docs/release-notesI have not read a tutorial about custom TF models on BQ ML, I will put it on my list!

 ·

[  ![0](../_resources/c363be819a73ad26975db6300aa30088.jpg)](https://www.linkedin.com/in/fryjamie/)  [ ###     Jamie Fry  • 2nd degree connection2nd     Looker Tech Lead at Datatonic](https://www.linkedin.com/in/fryjamie/)

 6d

[Thomas van Latum](https://www.linkedin.com/in/ACoAAAvGgSUBhkRf6pWzNnaRv1VNI4lBSGlY61w/) feel free to chat to our ml engineers, we use custom TF on bq. (we are Google partner so same team!)

 ·

[(L)](https://www.linkedin.com/in/baumannrene/)  [ ###     René Baumann  • out of network3rd+     General Manager DACH & Nordics at smartphoto group](https://www.linkedin.com/in/baumannrene/)

 1w

Hi Thomas, nice. I didn't expect that this can be done with so few lines of code. Does Google evtl. indicate the minimum nbr. of products and, for each user clicks/views-product combination, the min. nbr of views or clicks required for model training and accuracy? Also interesting to know if you can include historical basket info for "pre-training".

 ·

·

[  ![0](../_resources/f3a3f9a63b8c7b2cacc56b88372b793a.jpg)](https://www.linkedin.com/in/tlatum/)  [ ###     Thomas van Latum  • 2nd degree connection2nd     Google Cloud Architect & Data Engineer at g-company](https://www.linkedin.com/in/tlatum/)

 1w

Hi René, thank you for your comment. More data is always better for accuracy! That being said sometimes average recommendations is better than no recommendations at all. About the the historical basket, (I suspect you mean historical shopping carts) you can definitely use this for training, a good recommendation system combines multiple recommendation models. Let's connect next week so we can discuss your use-case!

[ ![0](../_resources/f3a3f9a63b8c7b2cacc56b88372b793a.jpg)](https://www.linkedin.com/in/tlatum/)

[ ##  Thomas van Latum](https://www.linkedin.com/in/tlatum/)

### Google Cloud Architect & Data Engineer at g-company

### More from Thomas van Latum

- [ ![0](../_resources/6b56bf7cfe35570c3571f501bebe85fc.png)          BigQuery unnest and primary keys in Looker      Thomas van Latum on LinkedIn](https://www.linkedin.com/pulse/bigquery-unnest-primary-keys-looker-thomas-van-latum/)
- [ ![0](../_resources/6a33a2a7779457cbabbd620efb9c76f8.png)          Working with BigQuery's new materialized views in Looker     Thomas van Latum on LinkedIn](https://www.linkedin.com/pulse/working-big-querys-new-materialized-views-looker-thomas-van-latum/)