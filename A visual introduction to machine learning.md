A visual introduction to machine learning

# A visual introduction to machine learning

![](../_resources/439c0241c2ca613723718f47eba576bf.png):

In machine learning, computers apply **statistical learning** techniques to automatically identify patterns in data. These techniques can be used to make highly accurate predictions.

*Keep scrolling.* Using a data set about homes, we will create a machine learning model to distinguish homes in New York from homes in San Francisco.

Scroll

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='40' height='10' data-evernote-id='71' class='js-evernote-checked'%3e %3cpath d='M0%2c0L40%2c0L20%2c10Z' fill='%23000' stroke='none' data-evernote-id='190' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

* * *

##  First, some intuition

Let’s say you had to determine whether a home is in ** San Francisco** or in **New York**. In machine learning terms, categorizing data points is a **classification** task.

Since San Francisco is relatively hilly, the elevation of a home may be a good way to distinguish the two cities.

Based on the home-elevation data to the right, you could argue that a home above 73 meters should be ** classified** as one in San Francisco.

* * *

##  Adding nuance

Adding another **dimension** allows for more nuance. For example, New York apartments can be extremely expensive per square foot.

So visualizing elevation *and* price per square foot in a **scatterplot** helps us distinguish lower-elevation homes.

The data suggests that, among homes at or below 73 meters, those that cost more than $19,116.7 per square meter are in New York City.

Dimensions in a data set are called **features**, **predictors**, or **variables**. 1

* * *

##  Drawing boundaries

You can visualize your elevation (>73 m) and price per square foot (>$19,116.7) observations as the boundaries of regions in your scatterplot. Homes plotted in the green and blue regions would be in San Francisco and New York, respectively.

Identifying boundaries in data using math is the essence of statistical learning.

Of course, you’ll need additional information to distinguish homes with lower elevations *and* lower per-square-foot prices.

* * *

The dataset we are using to create the model has 7 different dimensions. Creating a model is also known as **training** a model.

On the right, we are visualizing the variables in a **scatterplot matrix** to show the relationships between each pair of dimensions.

There are clearly patterns in the data, but the boundaries for delineating them are not obvious.

* * *

##  And now, machine learning

Finding patterns in data is where machine learning comes in. Machine learning methods use statistical learning to identify boundaries.

One example of a machine learning method is a **decision tree**. Decision trees look at one variable at a time and are a reasonably accessible (though rudimentary) machine learning method.

* * *