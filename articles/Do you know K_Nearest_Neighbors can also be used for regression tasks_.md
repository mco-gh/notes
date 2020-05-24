Do you know K_Nearest_Neighbors can also be used for regression tasks?

# Do you know K_Nearest_Neighbors can also be used for regression tasks?

[![2*7zNnc7VbvtCoEGKrShCsMg.jpeg](../_resources/879a135f1d07de0645d717e193529a71.jpg)](https://towardsdatascience.com/@hemanthsaid7?source=post_page-----117da22bcac3----------------------)

[Hemanth Devarapati](https://towardsdatascience.com/@hemanthsaid7?source=post_page-----117da22bcac3----------------------)

[Nov 28](https://towardsdatascience.com/do-you-know-k-nearest-neighbors-can-also-be-used-for-regression-tasks-117da22bcac3?source=post_page-----117da22bcac3----------------------) · 6 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='189'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='190' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='195'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='196' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/117da22bcac3/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' viewBox='0 0 29 29' fill='none' class='q js-evernote-checked' data-evernote-id='199'%3e%3cpath d='M5 6.36C5 5.61 5.63 5 6.4 5h16.2c.77 0 1.4.61 1.4 1.36v16.28c0 .75-.63 1.36-1.4 1.36H6.4c-.77 0-1.4-.6-1.4-1.36V6.36z' data-evernote-id='200' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.76 20.9v-8.57H7.89v8.58h2.87zm-1.44-9.75c1 0 1.63-.65 1.63-1.48-.02-.84-.62-1.48-1.6-1.48-.99 0-1.63.64-1.63 1.48 0 .83.62 1.48 1.59 1.48h.01zM12.35 20.9h2.87v-4.79c0-.25.02-.5.1-.7.2-.5.67-1.04 1.46-1.04 1.04 0 1.46.8 1.46 1.95v4.59h2.87v-4.92c0-2.64-1.42-3.87-3.3-3.87-1.55 0-2.23.86-2.61 1.45h.02v-1.24h-2.87c.04.8 0 8.58 0 8.58z' fill='%23fff' data-evernote-id='201' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/117da22bcac3/share/linkedIn?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='204'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='205' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/117da22bcac3/share/facebook?source=post_actions_header---------------------------)

Yes, it is! Let’s understand this simple algorithm
![1*gC4Cr1MkXBMRgJSbHwHOpw.png](../_resources/26106f677d6462ce49db998249dfa58d.png)
![1*gC4Cr1MkXBMRgJSbHwHOpw.png](../_resources/5d01e91a203f431292206efd23e2ac44.png)
source: researchgate.net
**What is in it for you?**

This article will bring to light the simplest and easiest to understand ML algorithm — K Nearest Neighbours. It can be used for both classification and regression tasks but is more common in classification, so we will focus there and will see how it can be used as a regressor. The principles, though, can be used in both cases.

**Let’s talk data**

I’m not picking on any dataset this time as I usually do in my other articles. I pick datasets if there is a purpose that it will serve in giving me an opportunity to explain a concept or a pitfall or a methodology. Like I confessed this is the simplest of ML algorithms. I will use the breast cancer dataset which is bundled with sklearn.

**Is it that simple?**
Basically, here is the algorithm:
1. Define
2. Define a distance metric — usually Euclidean distance (2-norm distance)

3. For a new data point, find the nearest training points and combine their classes in some way — usually voting — to get a predicted class

That’s it!
**Benefits of KNN**

- It doesn’t really require any training in the traditional sense. You just need a fast way to find the nearest neighbors.
- Easy to understand

**Drawbacks of KNN**

- We need to define k, which is a hyper-parameter, so it can be tuned with cross-validation. A higher value for k increases bias and a lower value increases variance. Bias and variance are always on the see-saw so technically you can never hit two birds with one bullet. There has to be a trade-off.

**Pro tip: **In a model, if you have to reduce variance then introduce large training sets, this is not a viable option in every case. If you have to reduce bias then adding features(predictors) will help but at the expense of introducing additional variance. More tips in my [article](https://medium.com/analytics-vidhya/linear-regression-bottoms-up-approach-intro-to-spark-a-bonus-b923ae594323/#822e)

- Have to choose a distance metric and could get very different results depending on the metric. Again, you can use cross-validation.
- It doesn’t really offer insights into which features might be important.
- It can suffer from high dimensional data due to the curse of dimensionality.

**Basic assumption:**

- Data points that are close are similar for our target

**What is the curse of dimensionality?**

This is a melancholic expression but what it means is a higher order of dimensions in the data.

Why is this a problem? I heard you. We can’t visualize the data. Visualization is like a first world country problem which has more noise but is actually very trivial.

The bigger problem is when you increase the dimensions the data points to represent your data also increases and the data becomes more spread out. It is likely that close points are not much closer than the average distance, which means being close doesn't mean much. KNN works on the distance between data points hence it will make this algorithm inefficient.

If you are curious to know why this happens in an intuitive way. [Go here](https://blog.galvanize.com/how-to-manage-dimensionality/)

## Euclidean Distance

For vectors, q, and p that are being compared (these would be our feature vectors):

![1*F507EfvD_1GAA42iLcCANw.png](../_resources/54c61136920158d8d32820bf4e1fc4ab.png)
![1*F507EfvD_1GAA42iLcCANw.png](../_resources/d36c2c915c7277a33d90772d10cc8204.png)
Source: Wiki

This is not the end. There are many other distance metrics. I will discuss the nomenclature later in the article. The most preferred distance norm for this algorithm is either manhattan(1-norm) or euclidean(2-norm).

# **Model**

You can follow code [here](https://github.com/hdev7/medium-KNN-follow-up-code)
How do you fix the K value?

There is no scientific approach to determine one. We just have to do hit and trial. Grid search to the rescue, I have pipelined the KNNClassifier into a grid-search to know the best hyperparameters.

![1*MaWcXIQaGwT6W_vtL5XP2w.png](../_resources/ab323a4eaa354de050921b9444d8c415.png)
![1*MaWcXIQaGwT6W_vtL5XP2w.png](../_resources/eb54bcbdb421d1df7a566c2a1e446df5.png)
grid search report
Looks like K = 5 with uniform weight methodology works best in this case.

To understand more about classification metrics. Follow up on my [article](https://medium.com/analytics-vidhya/logistic-regression-bottoms-up-approach-feature-engineering-ideology-a-bonus-81807fa881be/#805e)

# Types of voting methods

- Majority Voting: After you take the nearest neighbors, you take a “vote” of those neighbors’ classes. The new data point is classified with whatever the majority class of the neighbors is. If you are doing binary classification, it is recommended that you use an odd number of neighbors to avoid tied votes. However, in a multi-class problem, it is harder to avoid ties. A common solution to this is to decrease until the tie is broken.
- Distance Weighting: Instead of directly taking votes of the nearest neighbors, you weight each vote by the distance of that instance from the new data point. A common weighting method is

![1*hPKdWHZNOTDNEKeRwimC6w.png](../_resources/1d77155405e3b83467b4cfd50d7e9f49.png)
![1*hPKdWHZNOTDNEKeRwimC6w.png](../_resources/07900bc933ce66f1429bdfe118881cf6.png)

or one over the distance between the new data point and the training point. The new data point is added into the class with the largest added weight. Not only does this decrease the chances of ties, but it also reduces the effect of a skewed representation of data.

# Distance Metrics

Euclidean distance, or the 2-norm, is a very common distance metric to use for -nearest neighbors. Any -norm can be used.

![1*5bhkOAtJkj_OW5ZiXJGtgA.png](../_resources/52957e55b1ee0937a05b69ed0dd21f1f.png)
![1*8Q34CStgbEFnEGg68ZMX6A.png](../_resources/ad646ecbdce5069b51f5ae795e835593.png)
p-norm

For categorical data, however, this can be a problem. For example, if we have encoded a feature for car color from red, blue, and green to 0, 1, 2, how can the “distance” between green and red be measured? You could make dummy variables, but if a feature has 15 possible categories, that means adding 14 more variables to your feature set, and we run into the curse of dimensionality. But be aware of the effect categorical features can have on your nearest neighbors classifier.

# Search Algorithm

Imagine the data set contains 2000 points. A brute-force search for the 3 nearest neighbors to one point does not take very long. But if the data set contains 2000000 points, a brute-force search can become quite costly, especially if the dimension of the data is large. Other search algorithms sacrifice an exhaustive search for faster run time. Structures such as [KDTrees](https://en.wikipedia.org/wiki/K-d_tree) or [Ball trees](https://en.wikipedia.org/wiki/Ball_tree) are used for faster run times. While we won’t dive into the details of these structures, be aware of them and how they can optimize your run time (although, training time does increase).

# Another type: Radius Neighbors Classifier

This is the same idea as a nearest neighbor classifier, but instead of finding the nearest neighbors, you find all the neighbors within a given radius. Setting the radius requires some domain knowledge; if your points are closely packed together, you’d want to use a smaller radius to avoid having nearly every point vote.

# KNN Regressor

To change our problem from classification to regressing, all we have to do is find the weighted average of the nearest neighbors. Instead of taking the majority class, we calculate a weighted average of these nearest values, using the same weighting method as above.

Let’s try predicting the area of tissue based on the other features using a KNN regressor. Follow code [here](https://github.com/hdev7/medium-KNN-follow-up-code)

![1*8Q34CStgbEFnEGg68ZMX6A.png](../_resources/36554af16c68c5ea03c882a04d2d3079.png)
![1*5bhkOAtJkj_OW5ZiXJGtgA.png](../_resources/57e5eb41dedd51e2dcd5cffa80435ae7.png)
Now you know why nobody uses it for regression tasks

# An application: Outlier Detection

In k-nearest neighbors, the data is naturally clustered. Within these clusters, we can find the average distance between points (either exhaustively or from the centroid of the cluster). If we find a few points that are much farther than the average distance to other points or to the centroid, it is reasonable (but not always correct) to think they could be outliers. We can use this process on new data points as well.