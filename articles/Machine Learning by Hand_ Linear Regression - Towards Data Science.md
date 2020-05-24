Machine Learning by Hand: Linear Regression - Towards Data Science

# Machine Learning by Hand: Linear Regression

## Linear regression is a data scientist’s most basic and powerful tool. Let’s take a closer look at the Least Squares Line and Correlation Coefficient.

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='184' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='185' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*Qo9TvKOcDvOFqUAhPCyQCg.jpeg](../_resources/52b342489be4703ed72292a12fcfbed5.jpg)](https://towardsdatascience.com/@richardpeterson320?source=post_page-----ee7fe5a751bf----------------------)

[Richard Peterson](https://towardsdatascience.com/@richardpeterson320?source=post_page-----ee7fe5a751bf----------------------)

[Apr 11](https://towardsdatascience.com/linear-regression-by-hand-ee7fe5a751bf?source=post_page-----ee7fe5a751bf----------------------) · 6 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='201'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='202' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='207'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='208' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/ee7fe5a751bf/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='216'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='217' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/ee7fe5a751bf/share/facebook?source=post_actions_header---------------------------)

# Invention of Linear Regression

![1*a_LOmWEm2KHW4cpDho3A_w.png](../_resources/e288572d8c67baad4225aaf4747dfd8f.jpg)
![1*PZlezFfELTQbIz8Xoq-prA.jpeg](../_resources/340a45c79e25db19306450f16a928e64.jpg)

Photo by [Johannes Plenio](https://unsplash.com/@jplenio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/sailing-ships?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Linear regression is a form of linear algebra that was allegedly invented by Carl Friedrich Gauss (1777–1855), but was first published in a scientific paper by Adrien-Marie Legendre (1752–1833). Gauss used the least squares method to guess when and where the asteroid Ceres would appear in the night sky. (The Discovery of Statistical Regression, 2015) This was not a hobby project, this was a well-funded research project for the purpose of oceanic navigation, a highly competitive field that was sensitive to technological disruption.

* * *

*...*

# Principles of Linear Regression

Linear regression is a method for predicting ***y from x. ***In our case, ***y is the dependent variable, and x is the independent variable. ***We want to predict the value of **y **for a given value of **x.** Now, if the data were perfectly linear, we could simply calculate the slope intercept form of the line in terms ***y = mx+ b***. To predict ***y***, we would just plug in the given values of ***x and b.*** In the real world, our data will not be perfectly linear. It will likely be in the form of a cluster of data points on a **scatterplot**. From that scatterplot, we would like to determine, ***what is the line of best fit ***that describes the linear qualities of the data, and ***how well does the line fit the cluster of points?***

> Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. (> [*> Linear Regression*](http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm)> , n.d.)

# Scatterplots

Let’s make up some data to use as an example. The [relationship between Chimpanzee hunting party size and percentage of successful hunts](https://www.journals.uchicago.edu/doi/abs/10.1086/283318?journalCode=an) is well documented. (Busse, 1978) I am going to grab a few data points from Busse to use for this article, and plot the data using a seaborn scatterplot. Notice how the line I drew through the data does not fit it perfectly, but the points approximate a linear pattern? The line I drew through the data is the **Least Squares Line**, and is used to predict ***y values for given x values***. Using just a rudimentary Least Squares Line drawn by hand through the data, we could predict that a hunting party of 4 chimpanzees is going to be around 52% successful. We are not 100 percent accurate, but with more data, we would likely improve our accuracy. How well the data fits the **Least Squares Line** is the **Correlation Coefficient**.

![1*zPrANde5QS28vb30USMg6A.png](../_resources/0b82d0aa61e9bb14f2e7e1aefa4a73a4.png)
![1*zPrANde5QS28vb30USMg6A.png](../_resources/4b7566cd17ff4f9cfab37b50bfc35ac9.png)

# Least Squares Line

In the chart above, I just drew a line by hand through the data that I judged to be the best fit. We should calculate this line in slope intercept form ***y = mx + b*** to make true predictions. What we are seeking is a line where the differences between the line and each point are as small as possible. This is the line of best fit.

> The least squares line is defined as the line where the sum of the squares of the vertical distances from the data points to the line is as small as possible. (Lial, Greenwell and Ritchey, 2016)

The least squares line has two components: the slope ***m, ***and y-intercept ***b. ***We will solve for ***m*** first, and then solve for ***b. ***The equations for ***m ***and*** b ***are:

![1*5Bqrl8wpIdUQXT4l1iC87Q.png](../_resources/03b7c5dd9935a5da264bb886fc417bc4.png)
![1*a_LOmWEm2KHW4cpDho3A_w.png](../_resources/8cd14beabedfb65051a83e61eb899ffd.png)
Created in MS Word equation editor

That’s a lot of Sigmas (∑)!. But don’t worry, Sigma just means “change in”, such as “change in x,” symbolized by ∑x, which is just the sum of the x column, “Number of Chimpanzees.” We need to calculate ∑x, ∑y, ∑xy, ∑x², and ∑y². Each piece will then be fed into the equations for ***m*** and ***b. ***Create the below table based on our original dataset.

![1*EwvjzWR9YC_51QfrZHRArA.png](../_resources/a85b690cebf62a2f14ef73ab6bfb3ddd.png)
![1*EwvjzWR9YC_51QfrZHRArA.png](../_resources/91cf52af287762009ea13b4008cc29f0.png)

Now it is a simple matter to plug our Sigma values into the equation for ***m and b. n ***is the number of values in the dataset, which in our case is **8.**

![1*h4zYPIEs2GLHlw8pBSWTdw.png](../_resources/c094dc2f1248017f98ee164a229c9b06.png)
![1*h4zYPIEs2GLHlw8pBSWTdw.png](../_resources/5544ba197caaa597c4258131ddf8a5de.png)

There you have it! You can make predictions of ***y*** from given values of ***x ***using your equation: ***y = 5.4405x + 31.6429.****  *This means that our line starts out at **31.6429** and the y-values increase by **5.4405** percentage points for every 1 Chimpanzee that joins the hunting party. To test this out, let’s predict the percent hunt success for 4 chimpanzees.

***y = 5.4405(4)+31.6429***, which results in **y=53.4**

We just predicted the percentage of successful hunts for a chimpanzee hunting party based solely on knowledge of their group size, which is pretty amazing!

Let’s plot the least squares line over our previous scatterplot using python to show how it fits the data. `Seaborn.regplot()` is a great chart to use in this situation, but for demonstration purposes, I will manually create the ***y=mx+b line*** and lay it over the seaborn chart.

|     |     |
| --- | --- |
| 1   | # Import packages |
| 2   | import  pandas  as  pd |
| 3   | import  numpy  as  np |
| 4   | import  matplotlib.pyplot  as  plt |
| 5   | import  seaborn  as  sns |
| 6   |     |
| 7   | # Indedependent variable - number of chimpanzees in hunting party |
| 8   | x  =  np.array([1,2,3,4,5,6,7,8]) |
| 9   | # Dependent Variable - percent of successful hunts |
| 10  | y  =  np.array([30,45,51,57,60,65,70,71]) |
| 11  |     |
| 12  | df  =  pd.DataFrame({'Number of Chimpanzees':x,'Percent Successful Hunts':y}) |
| 13  |     |
| 14  | # Initialize the figure |
| 15  | plt.figure(figsize=(8,5)) |
| 16  | plt.title('Number of Chimpanzees vs Hunt Success - Least Squares Line') |
| 17  |     |
| 18  | # Scatterplot |
| 19  | sns.scatterplot(x='Number of Chimpanzees',y='Percent Successful Hunts',data=df).get_figure().savefig('Chimpanzee Hunt Sucess with Least Squares Line.png') |
| 20  |     |
| 21  | # Least Squares Line |
| 22  | x  =  np.linspace(1,8,100) |
| 23  | y  =  5.4405*x+31.6429 |
| 24  | plt.plot(x, y, '-g',label='y=5.4405x+31.6429') |

 [view raw](https://gist.github.com/rchardptrsn/dc3563124ee5ed85e672cd082ad85a09/raw/de182c5d34fc661c8bf8211c17dd26607f16c5ed/leastsquares.py)  [leastsquares.py](https://gist.github.com/rchardptrsn/dc3563124ee5ed85e672cd082ad85a09#file-leastsquares-py) hosted with ❤ by [GitHub](https://github.com/)

![1*010BzoCEYQCPYkAv7_SNUw.png](../_resources/7f8027b842de8a49ae4125e819728a6f.png)
![1*010BzoCEYQCPYkAv7_SNUw.png](../_resources/41ed7baf50c44c04c51934ae69b9edf5.png)

However, now that you can make predictions, you need to qualify your predictions with the **Correlation Coefficient**, which describes how well the data fits your calculated line.

* * *

*...*

# Correlation Coefficient

We use the Correlation Coefficient to determine if the least squares line is a good model for our data. If the data points are not linear, a straight line will not be the right model for prediction. **Karl Pearson** invented the Correlation Coefficient ***r***, which is between 1 and -1, and measures the strength of the linear relationship between two variables. (Lial, Greenwell and Ritchey, 2016) If ***r ***is exactly -1 or 1, it means the data fits the line *exactly, *and there is no deviation from the line. ***r=0*** means that there is no linear correlation. As ***r***  ***values*** approach zero, it means that association decreases as well.

The Correlation Coefficient is described by the formula
![1*jGDq9KCLaAgNfE4h8iDObQ.png](../_resources/9a6dd5dfa1e1d62ad52a2adfc8da7fbe.png)
![1*5Bqrl8wpIdUQXT4l1iC87Q.png](../_resources/50b7b0c6691156ed8d36ce1e609cd650.png)

Luckily, these Sigma values have already been calculated in our previous table. We simply plug them into our equation.

![1*PZlezFfELTQbIz8Xoq-prA.jpeg](../_resources/1cb9425c0cf91649888461e818e1c575.png)
![1*jGDq9KCLaAgNfE4h8iDObQ.png](../_resources/5c818939d4ca8c61ba0c65d2ad5b499c.png)

Our value is close to positive 1, which means that the data is highly correlated, and positive. You could have determined this from looking at the least squares line plotted over the scatterplot, but the Correlation Coefficient gives you scientific proof!

# Conclusion

Linear regression is one of the best machine learning methods available to a data scientist or a statistician. There are many ways to create a machine learning model using your programming skills, but it is definitely a good idea to familiarize yourself with the math used by the model.

## References

Busse, C. D. (1978). Do Chimpanzees Hunt Cooperatively? *The American Naturalist*, *112*(986), 767–770. https://doi.org/10.1086/283318

Lial, Greenwell and Ritchey (2016). *Finite Mathematics and Calculus with Applications, 10th Ed*. New York, NY: Pearson [ISBN-13 9780133981070].

*Linear Regression*. (n.d.). Retrieved April 11, 2020, from http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm

The Discovery of Statistical Regression. (2015, November 6). Priceonomics. http://priceonomics.com/the-discovery-of-statistical-regression/