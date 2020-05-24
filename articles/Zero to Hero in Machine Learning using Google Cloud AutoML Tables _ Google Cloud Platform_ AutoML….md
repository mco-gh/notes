Zero to Hero in Machine Learning using Google Cloud AutoML Tables | Google Cloud Platform| AutoML…

# Zero to Hero in Machine Learning using Google Cloud AutoML Tables | Google Cloud Platform| AutoML Tables |

[![2*pp7s-YtxYcpZzEopMg8xqA.png](../_resources/253460077ec96bc6a157318d2da4a703.jpg)](https://medium.com/@IVaibhavMalpani?source=post_header_lockup)

[Vaibhav Malpani](https://medium.com/@IVaibhavMalpani)
Jun 8·5 min read

Want to produce state-of-the-art Machine Learning models with no prior knowledge?

Want to learn how to Build, Deploy and Scale your models on cloud without writing a single line of code?

![](../_resources/9073ef0fde355f58c14861e869587a65.png)![1*dWMQRjpeZZjwqBSbnf13Fw.jpeg](../_resources/53122eb5adf79dba0fc444bf7be4eed9.jpg)

### What is AutoML Tables?

AutoML Tables enables you to automatically build and deploy state-of-the-art machine learning models on structured data at massively increased speed and scale.

* * *

*...*

For this demo we will use public data from kaggle : [**Mobile Price Classification**](https://www.kaggle.com/iabhishekofficial/mobile-price-classification#train.csv)

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*a4CVdYG0GehvIJL3lMlKtQ.png](../_resources/71a9a4360f442b4bb7a30b8a9f3530ba.png)

At the time of writing this blog, AutoML takes data from bucket in the ***us-central1*** region.

So please select
Regional → us-central1(lowa)

![](../_resources/6bf1f2327f99debf687eb83db29acace.png)![1*NA5KD7wwBbA4FICMFxGevg.png](../_resources/b5da8e99e00b1ffcd71a045891d44b34.png)

Upload the train.csv and test.csv to the bucket created above.

Now that we have the data required in place, Let’s start building AutoML models from [***here***](https://console.cloud.google.com/automl-tables/datasets). In this problem you have to predict a price range based on other parameters. **Price range has value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost).**

* * *

*...*

### Steps to Build models using AutoML Tables:

1. 1.Create new Dataset
2. 2.Import Data
3. 3.Check Schema and Select a target from data
4. 4.Analyze features from data
5. 5.Train the data
6. 6.Evaluate your model
7. 7.Test your model

### **Create new Dataset:**

![](../_resources/efbc1f6ee51277029da0ab3de436dd13.png)![1*NIWTcBxh6mRjC2IQHBHRZA.png](../_resources/705867dc9232b6812675fb5c493a9ca5.png)

Give a name to your dataset and click “create dataset”. After the dataset is created, open it.

### Import Data:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*GhbT4mLkXrUL8tebj44c7Q.png](../_resources/56f9d7e65c734262888aa5b6a32149f5.png)

For this demo, we will import data from Cloud Storage.

Click on browse, select your training dataset (in this case: “train.csv”) and click on “IMPORT”

### Check Schema and Select a target from data

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*vCbSTPh8R8ewTpmO0bh-zw.png](../_resources/57ec95d94131701483cdc17f938e9b39.png)

After the data is imported, you can view the schema on the right side. On the left side, you would need to select the “target column”.

Target column is the column on which prediction needs to be done. Classification Model is created on the Target column.

In our demo, we need to predict a price range based on other parameters. So we selected “price_range” as our Target column. Select Continue to analyze your data.

### Analyze features from data:

On selecting the Analyze tab, you get to see the features and their types (Numeric, Categorical etc.).

### Train the data:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*fQs5x9xtlEyZO3dFpSFVTw.png](../_resources/2ab917e48ff53c52b5dc6d897df8376b.png)

Now select the “TRAIN” tab. you will find your model name already present.

Below that select number of node hours you need the model to be trained. If your model stops improving before the mentioned node hours, AutoML Tables will stop training and you’ll only be charged for the actual node hours used.

Model training costs **$19.32 per hour** of compute resources used to train your model, billed at the granularity of seconds.

![](../_resources/7eda29bf1b34fc0b285eec3c4adc3930.png)![1*PVZt7j3gNp_1C0ck4OFdCA.png](../_resources/12025716ce63382beab30f6d10bd3fe2.png)

**Suggested training time is related to the number of rows in your training data**

Now click on “Train model” and wait for a email from Google, mentioning that the Training is finished!

### Evaluate your model:

![](../_resources/7c670df7aec0a5ad60ef3847a98383a2.png)![1*w15yAfeFu8rUc2QmCN-GCQ.png](../_resources/9d4c9f223a8579eb6b5a1bf791b2fded.png)

At the top, You get to see all the high level information about performance of your model. We can see that the model has more than **97% Precision!!**

On the Evaluate tab, scroll down to get in-depth information about the your model.

![](../_resources/9bf2b56ef3820ff7b3929411ea5c85ca.png)![1*YlO45_I5PDwhHufOw1pb1g.png](../_resources/f1b894d1e6b5f8ce44d885ed181c1ae5.png)

#### **Confusion matrix**:

The confusion matrix helps you understand where misclassifications occur (which classes get “confused” with each other). Each row is a predicted class and each column is an observed class. The cells of the table indicate how often each classification prediction coincides with each observed class.

![](../_resources/baa3c1c0634c09a02d96db40d9c43d8a.png)![1*37Q3m1UM5O6C95yOP3X-Xw.png](../_resources/f8b91de93c4745e7f5e254f8702b2e8e.png)

#### **Feature importance**:

AutoML Tables tells you what features it found to be most important for building this model in the Feature importance graph. It is computed by measuring the impact that each feature has on the prediction, when perturbed across a wide spectrum of values sampled from the dataset. Review this information and ensure that all of the most important features make sense for your data.

As we can see in the above feature importance graph, price of mobile mainly does depend on RAM, Battery Power and Size of phone, but not on it being 3G or touch screen. So this feature importance graph makes sense of our data.

### Test your model:

Now moving to the most exciting part of Machine Learning i.e to see how your model actually work on test data.

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*qtATa8RPSQZgIcgS2Tz6Kg.png](../_resources/77f6d60f44cfae2a0705dfb6998fe565.png)

On the Predict Tab, we need to provide 2 things to test our model.
1. 1.Test Data (Input) on which the model needs to be tested.

2. 2.Google Bucket Storage location (Result directory) to save results after prediction.

Now select “Send Batch Prediction” to start the prediction. Time taken might differ from the number of rows in CSV.

After the prediction job you can see the result in the result directory. The folder name might look like “ prediction-mobile_price_calc_20190607101…”.

Below is the test.csv that we had given to the model.

![](../_resources/2e7c322a3be8498ce6443d57a5a469a3.png)![1*fDw7TbGpy4kPjq7qvpujwQ.png](../_resources/6b58d8d7c149be5b6f5b470c1b902c68.png)

**test.csv**

This is the result that we have got from the model.

![](../_resources/cfae7bd01ffd2a19be2d8ebfab6826b8.png)![1*-SzEJZuOY2Rhs40Ymtn45g.png](../_resources/8e657d306be19c683abc79e37d244603.png)

tables_1.csv

As you can see in the rightmost side, there are 4 new fields : **price_range_0_score, price_range_1_score, price_range_2_score, price_range_3_score. **Each field represent the possibility of itself being the answer.

Eg: For the 1st row, model is100% sure that the mobile’s price range would be 0 (low cost). Similarly, 3rd row has 99% possibility of being in price range 3 (very high cost).

### Congratulations!! You have successfully built and trained a Machine Learning model, without any code or any prior knowledge.

#### Interesting Case studies:

Fox Sports Australia predicts the fall of a wicket in live cricket matches with AutoML Tables : https://www.computerweekly.com/news/252461706/Fox-Sports-Australia-predicts-wickets-with-AutoML-Tables