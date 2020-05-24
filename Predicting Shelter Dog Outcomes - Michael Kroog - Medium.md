Predicting Shelter Dog Outcomes - Michael Kroog - Medium

# Predicting Shelter Dog Outcomes

[![0*1tfCilKTTycB_SZT](../_resources/bc1f0c7fb8fae7945b79f47476538eef.png)](https://medium.com/@michaelkroog?source=post_page-----db014269004f----------------------)

[Michael Kroog](https://medium.com/@michaelkroog?source=post_page-----db014269004f----------------------)

[Jul 25](https://medium.com/@michaelkroog/predicting-shelter-dog-outcomes-db014269004f?source=post_page-----db014269004f----------------------) · 8 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='156'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='157' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/db014269004f/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='160'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='161' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/db014269004f/share/facebook?source=post_actions_header---------------------------)

![1*zhT3XhIojGbV_v0QUk60Pw.png](../_resources/e43460a6237336bc02876cb1757ebf00.jpg)
![1*NxyUCBCQh7CCzv2sT_Or6w.jpeg](../_resources/3ea516480c073cabdcbb6b24ae6247a2.jpg)

Gummy was adopted from a kill shelter [@gummythepit](https://www.instagram.com/gummythepit/?hl=en)

# Project Goals:

- Predict 3 outcome classes (Adopted, Euthanized, Returned to Owner)
- Find the strongest contributing factors to the Adoption outcome class
- Create dashboards and organize shelter data to increase adoptions

# Helping Shelter Dogs

My two adopted shelter dogs inspired me to explore whether I could predict shelter dog outcomes. Every person/family has their own reasons for why they adopt dogs, but I believe one of their reasons is common to my own — they are looking for the right dog to fit their lifestyle. I personally visited a number of shelters looking for the right dog that would fit my lifestyle and while it took some time, but I ultimately did find the perfect dogs. Throughout my search, I realized that every dog I encountered had its own story and own personality and unfortunately, sometimes these stories and personalities make it difficult for a dog to find a home.

Despite these stories and personalities, I know from experience that the dog a person meets in a shelter is not necessarily who that dog actually is. Shelters are a highly stressful environment for dogs and when a shelter dog has the security of a home and a family that cares about them, the dog tends to flourish. Therefore, my goal was to give every single shelter dog a chance to find a home by using Data Science tools to help shelters customize their adoption efforts to maximize their adoptions. By using the methods discussed below, I was able to discern which dogs were less likely to be adopted and measures that can be taken to increase their chances of adoption.

# **The Data**

![1*NxyUCBCQh7CCzv2sT_Or6w.jpeg](../_resources/614aa229786eecaa099d66523d304252.png)
![1*zhT3XhIojGbV_v0QUk60Pw.png](../_resources/91b6efe3f0e3f795cefa31ee370c6b0b.png)
Class Imbalance

I found datasets from three different shelters that I cleaned and compiled into one dataframe. I yielded over 100,000 records, but only five variables that were common to all three shelters. The cleaned data also had a slight class imbalance with a ratio of approximately 4:3:3 for the Adopted, Euthanized and Returned to Owner classes. With the class imbalance being so slight I decided against resampling or SMOTE since it might introduce some bias into the models (discussed in more detail below) and instead, I chose the F1 scoring metric. The F1 score also helped to balance the high cost of a False Positive or False Negative, since I am predicting the outcomes of dogs lives both of these results are important. For instance, spending resources trying to help a dog that is classified as Euthanized, but actually won’t be, takes away from dogs that will be Euthanized. And a dog that is classified as not Euthanized, but is actually going to be Euthanized will be missing an opportunity to find a home. In addition, I used multiple algorithms to baseline as a way of seeing which algorithms would work best given the slight class imbalance.

# **Modeling**

![1*vECSMkuOr5sGPUIwdw98HA.png](../_resources/a661a5d2879d0f6fb3cc2bcb55456388.png)
![1*vECSMkuOr5sGPUIwdw98HA.png](../_resources/d57cc6823244eefeb8bd269a55e444a9.png)
Baseline Scores

I started baseline modeling with Naive Bayes, Logistic Regression and Random Forest. Although I knew some of these algorithms weren’t ideal for a Multiclass Classification problem, it was still a valuable way to learn how and why they didn't produce great results. I cross validated with all models, but the results weren’t great. Naive Bayes resulted in an F1 Score of 0.37, Logistic Regressions resulted in a score of 0.56 and Random Forest resulted in a score 0.65. I didn’t believe that Naive Bayes or Logistic Regression were the right algorithms for this problem. While Random Forest would probably score higher with parameter tuning, I decided to focus on using XGBoost because it most likely would provide a higher-scoring model. With an F1 Score of 0.68, the XGBoost baseline score was only slightly higher than the Random Forest one. Although an F1 Score of 0.68 is not too bad, I decided to introduce some complexity into the model to increase the score. I tried feature engineering on the data to increase the number of features and spent time finding additional data on the relevant features that I could use to help train the model based on my experience of being a dog owner of two rescue dogs. Specifically, I focused on features that seemed to factor into adopters’ decisions to adopt dogs — weight or size, breed popularity, age at outcome and breed group. I used Beautiful Soup and Selenium to scrape data containing all of this information and was able to increase the features of the data from five to 22. After scraping the data, I trained the XGBoost model on the updated data set, which included the engineered features, and I was able to get a baseline F1 score of 0.82 with XGBoost.

# **Tuning and Analysis**

XGBoost allowed me to plot out feature importance and the results were interesting. Only a few of the features were largely responsible for the construction of the trees within the model, while many of the features had low importance.

![1*aGgOJiQMi64USzqYuXX0Vw.png](../_resources/5c7e364937cc8dcdf2bb75020cb35df0.png)
![1*aGgOJiQMi64USzqYuXX0Vw.png](../_resources/bb64b2201b767bb608db6cdef49668f3.png)

XGBoost’s built in feature importance scores revealed some interesting if not peculiar results. The highest score according to ‘gain’ was the binary feature ‘Sterilized’. According to the data a dogs spayed or neutered status was recored at the time of the outcome. I found it odd that the highest scoring feature was ‘Sterilized’ because I believe many shelters have a policy of sterilizing dogs before adoption. But for dogs that are going to be euthanized, it wouldn’t make sense to sterilize them first. If there was a very high percentage of one outcome type and one of the binary results of the feature then this signal may skew the model. I found that this was the case. Just over 97% of adopted dogs and just over 20% of euthanized dogs were sterilized. The model captured the signal in this feature and thinks that sterilization is a strong predictor for the outcome class. For these reasons I decided to retrain the model without this feature.

After the ‘Sterilized’ feature removed and I tuned the model and it yielded an F1 Score of 0.96. The strongest contributing factor was now dog breed, with American Pit Bull Terrier being the strongest type of breed. Since dog breed inherently contains size, weight and group type — all of which are individual features in the data set — it makes sense that this would have a high feature importance. I decided to drop dog breed as a feature and retrain the model in order to see how each individual feature effected the outcome of the model. If some of these features have a low importance score I could drop them and reduce the complexity of the model.

XGBoost’s feature importance method was helpful and I reduced the number of features from 22 down to nine without changing the F1 Score. The final nine features used in my model were the following: ‘Age at Outcome’, ‘Outcome Type’, ‘Pure’, ‘Percent Breed Outcome Year’, ‘Group’, ‘Rank 2017’, ‘Median Life Expectancy’, ‘Size’, ‘Mean Weight Breed’ and ‘Mean Age at Outcome Breed’. However, I was still curious on how each feature effected the models prediction of each class, in a positive or negative way. Even though it wasn’t listed as the most important, I wanted to take a closer look at ‘Age at Outcome’, because I thought it would be helpful to understand how age and in what way it effected the model’s output.

![1*me4S-xb7Du9pcCBnxy91IQ.png](../_resources/16e0afc0ec2699f66ad5898d6eee3c32.png)
![1*me4S-xb7Du9pcCBnxy91IQ.png](../_resources/1021614fe090a58c702f8836509e6a2c.png)

Partial Density Plot Showing the Strength of the ‘Age at Outcome’ Feature for Two Classes (class 0 = Adopted, class 1 = Euthanized)

I used PDPBox to generate a Partial Density Plot of ‘Age at Outcome’ for two classes Adopted and Euthanized (class 0 and class 1 respectively). The above graph can be a little hard to read, I will describe it below.

**X/Y Axis:**
Dog Age at Outcome in years/Positive or negative strength of the feature.
**Blue Lines:**
Individual data points(100 per plot).
**Yellow/Black Line:**
Strength of the feature per dog age.

I found it interesting to look at the feature like this even though the results were a little unsurprising. The plot on the left shows that for Adopted dogs the feature has a little positive influence on the models output with peak strength at 0.16 years or about two months and starts to decline and turn negative after seven years. The plot on the right shows age for Euthanized dogs is mostly negative until around seven years where it starts to turn positive. From a practical standpoint this makes sense as younger dogs especially puppies are valued and therefore more likely to be adopted, while dogs that are older and possibly sick are more likely to be euthanized.

# **Practical Application**

During my search for shelter data, I came across an organization called Shelter Animals Count ([https://www.shelteranimalscount.org](https://www.shelteranimalscount.org/)). Their mission statement is noble and they are looking to collect data from shelters across the county and to maintain an accurate database of animal counts and outcomes. I recommend looking at their website to get the full picture of their goals.

I believe their idea could be taken a step further by standardizing intake data (i.e., to compile a wide range of specific data that can be used to make predictions) collected on dogs across shelters and this data could be shared to one database. Shelters could use my model and by collecting more data, it can be even more useful and accurate in predicting outcomes and finding markers for adoption.

In addition to predicting outcomes, by having a large standardized database of dog features and locations, shelters could make recommendations to potential adopters on where to find the right type of dog. Dogs could be transported to sister shelters in regions where there may be a deficit of a desired breed type. Analyzing comprehensive data may also show trends in dog preference by region, certain types of dogs may find it harder to be adopted in certain areas, for example large working breeds may be easier to adopt in the suburbs as opposed to the cities were recreational space is limited.

The video below shows a Tableau dashboard of a hypothetical shelter dog database and the ability to select different characteristics to find a potential adopter and adoptee match.

Tableau Dashboard Video — https://vimeo.com/348496815a

Please head to my github repository to view the Jupiter notebooks for this project — https://github.com/m-kroog/Predicting-Shelter-Dog-Outcomes