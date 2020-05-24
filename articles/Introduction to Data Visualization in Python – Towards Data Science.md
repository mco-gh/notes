Introduction to Data Visualization in Python – Towards Data Science

# Introduction to Data Visualization in Python

## How to make graphs using Matplotlib, Pandas and Seaborn

[![1*-za8S8j0FQi1qTsRI8MvXA.jpeg](../_resources/54184fca1d8dfc26f2313477b28f17a2.jpg)](https://towardsdatascience.com/@gilberttanner?source=post_header_lockup)

[Gilbert Tanner](https://towardsdatascience.com/@gilberttanner)
Jan 23·9 min read

![](../_resources/648cf51e827193c29b92b620ff60c120.png)![0*hzU1K3AH2u6n4wPw](../_resources/a021839faab82270100b5ae6acd980c7.jpg)

Figure 1: Photo by [Lukas Blazek](https://unsplash.com/@goumbik?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Data visualization is the discipline of trying to understand data by placing it in a visual context, so that patterns, trends and correlations that might not otherwise be detected can be exposed.

Python offers multiple great graphing libraries that come packed with lots of different features. No matter if you want to create interactive, live or highly customized plots python has a excellent library for you.

To get a little overview here are a few popular plotting libraries:

- •[**Matplotlib:**](https://matplotlib.org/)**  **low level, provides lots of freedom
- •[**Pandas Visualization:**](https://pandas.pydata.org/pandas-docs/stable/visualization.html)**  **easy to use interface, built on Matplotlib
- •[**Seaborn:**](https://seaborn.pydata.org/)**  **high-level interface, great default styles
- •[**ggplot:**](http://ggplot.yhathq.com/)**  **based on R’s ggplot2, uses [Grammar of Graphics](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448)
- •[**Plotly:**](https://plot.ly/python/)**  **can create interactive plots

In this article, we will learn how to create basic plots using Matplotlib, Pandas visualization and Seaborn as well as how to use some specific features of each library. This article will focus on the syntax and not on interpreting the graphs, which I will cover in another blog post.

In further articles, I will go over interactive plotting tools like Plotly, which is built on D3 and can also be used with JavaScript.

* * *

*...*

### Importing Datasets

In this article, we will use two datasets which are freely available. The [Iris](https://archive.ics.uci.edu/ml/datasets/iris) and [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews) dataset, which we can both load in using pandas `read_csv` method.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | import pandas as pd |
| 2   | iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']) |
| 3   | print(iris.head()) |

 [view raw](https://gist.github.com/TannerGilbert/624c750d81dde98b4e072d20f9c3546a/raw/3ff3397c608dd170137fffbf2446912a04358488/load_iris.py)  [load_iris.py](https://gist.github.com/TannerGilbert/624c750d81dde98b4e072d20f9c3546a#file-load_iris-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/622287a203c17e222ad500763642fe91.png)![1*sl_B5DS5rHD1kDvrg3qllg.png](../_resources/b25fc1e434b9ac70f5903beb837aa596.png)

Figure 2: Iris dataset head

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0) |
| 2   | wine_reviews.head() |

 [view raw](https://gist.github.com/TannerGilbert/f685178e439ac93297f71f350d3b9d5c/raw/d8513ff27a2cdc5da6ad2dd163b5d5551ff8543b/load_wine_reviews.py)  [load_wine_reviews.py](https://gist.github.com/TannerGilbert/f685178e439ac93297f71f350d3b9d5c#file-load_wine_reviews-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/aadc9046b54ee9bbacf89fc47522800f.png)![1*DHn89aKqAruVzVsGqEdZYg.png](../_resources/442895bebe2ffced08dc20ec6b7e4550.png)

Figure 3: Wine Review dataset head

* * *

*...*

### Matplotlib

Matplotlib is the most popular python plotting library. It is a low level library with a Matlab like interface which offers lots of freedom at the cost of having to write more code.

To install Matplotlib pip and conda can be used.
pip install matplotlib
or
conda install matplotlib

Matplotlib is specifically good for creating basic graphs like line charts, bar charts, histograms and many more. It can be imported by typing:

`import matplotlib.pyplot as plt`

#### Scatter Plot

To create a scatter plot in Matplotlib we can use the `scatter` method. We will also create a figure and an axis using `plt.subplots` so we can give our plot a title and labels.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # create a figure and axis |
| 2   | fig, ax = plt.subplots() |
| 3   |     |
| 4   | # scatter the sepal_length against the sepal_width |
| 5   | ax.scatter(iris['sepal_length'], iris['sepal_width']) |
| 6   | # set a title and labels |
| 7   | ax.set_title('Iris Dataset') |
| 8   | ax.set_xlabel('sepal_length') |
| 9   | ax.set_ylabel('sepal_width') |

 [view raw](https://gist.github.com/TannerGilbert/e704df78594d740151a9b3d8ca3400b5/raw/77d8b648ae265dd299e5ec226b4a9126c9a32462/matplotlib_simple_scatterplot.py)  [matplotlib_simple_scatterplot.py](https://gist.github.com/TannerGilbert/e704df78594d740151a9b3d8ca3400b5#file-matplotlib_simple_scatterplot-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/28b5b572a1e2abb932d0731f0920e2aa.png)![1*wHJsVsCZsIN2mvYOGhIcCA.png](../_resources/1d4b5481ee38dd904d991320819fd215.png)

Figure 4: Matplotlib Scatter plot

We can give the graph more meaning by coloring in each data-point by its class. This can be done by creating a dictionary which maps from class to color and then scattering each point on its own using a for-loop and passing the respective color.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # create color dictionary |
| 2   | colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'} |
| 3   | # create a figure and axis |
| 4   | fig, ax = plt.subplots() |
| 5   | # plot each data-point |
| 6   | for i in  range(len(iris['sepal_length'])): |
| 7   | ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i],color=colors[iris['class'][i]]) |
| 8   | # set a title and labels |
| 9   | ax.set_title('Iris Dataset') |
| 10  | ax.set_xlabel('sepal_length') |
| 11  | ax.set_ylabel('sepal_width') |

 [view raw](https://gist.github.com/TannerGilbert/751330e316bfeaf72e831670c6a7fe99/raw/b1dfab41b5b073ab2b60c5b5d68c1df3737b87bb/matplotlib_simple_scatterplot_with_colors.py)  [matplotlib_simple_scatterplot_with_colors.py](https://gist.github.com/TannerGilbert/751330e316bfeaf72e831670c6a7fe99#file-matplotlib_simple_scatterplot_with_colors-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/729942a5927fe9cfa1dacc54f6ca273c.png)![1*g7ZE1by6rcM27ulB45h3eA.png](../_resources/89fbe3226e92ed9c68b2ab53127efbbf.png)

Figure 5: Scatter Plot colored by class

#### Line Chart

In Matplotlib we can create a line chart by calling the `plot` method. We can also plot multiple columns in one graph, by looping through the columns we want, and plotting each column on the same axis.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # get columns to plot |
| 2   | columns = iris.columns.drop(['class']) |
| 3   | # create x data |
| 4   | x_data =  range(0, iris.shape[0]) |
| 5   | # create figure and axis |
| 6   | fig, ax = plt.subplots() |
| 7   | # plot each column |
| 8   | for column in columns: |
| 9   | ax.plot(x_data, iris[column]) |
| 10  | # set title and legend |
| 11  | ax.set_title('Iris Dataset') |
| 12  | ax.legend() |

 [view raw](https://gist.github.com/TannerGilbert/4465a959a833b92fc03b8061d61e3497/raw/40e0df878e837baa722c7d9c0aa8383911e07a04/matplotlib_simple_linechart.py)  [matplotlib_simple_linechart.py](https://gist.github.com/TannerGilbert/4465a959a833b92fc03b8061d61e3497#file-matplotlib_simple_linechart-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/e0bc7d7ee7db3d65e228321f3fcd223c.png)![1*7_h8orPIGV42e5AIWF-7bA.png](../_resources/b608a97532e12a8ed93b957440035d45.png)

Figure 6: Line Chart

#### Histogram

In Matplotlib we can create a Histogram using the `hist` method. If we pass it categorical data like the points column from the wine-review dataset it will automatically calculate how often each class occurs.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # create figure and axis |
| 2   | fig, ax = plt.subplots() |
| 3   | # plot histogram |
| 4   | ax.hist(wine_reviews['points']) |
| 5   | # set title and labels |
| 6   | ax.set_title('Wine Review Scores') |
| 7   | ax.set_xlabel('Points') |
| 8   | ax.set_ylabel('Frequency') |

 [view raw](https://gist.github.com/TannerGilbert/80860db304ebf10263678bbde4312bed/raw/c768f3f9d0dbbacab4d61130a2c3bb0c068ccbab/matplotlib_simple_histogram.py)  [matplotlib_simple_histogram.py](https://gist.github.com/TannerGilbert/80860db304ebf10263678bbde4312bed#file-matplotlib_simple_histogram-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/af452747b955abb76862d43c9abd8cf1.png)![1*uNfH13lMewuE-n2XNbWGiw.png](../_resources/873cfc575b9b87131923c2e56100e19b.png)

Figure 7: Histogram

#### Bar Chart

A bar-chart can be created using the `bar` method. The bar-chart isn’t automatically calculating the frequency of a category so we are going to use pandas `value_counts` function to do this. The bar-chart is useful for categorical data that doesn’t have a lot of different categories (less than 30) because else it can get quite messy.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # create a figure and axis |
| 2   | fig, ax = plt.subplots() |
| 3   | # count the occurrence of each class |
| 4   | data = wine_reviews['points'].value_counts() |
| 5   | # get x and y data |
| 6   | points = data.index |
| 7   | frequency = data.values |
| 8   | # create bar chart |
| 9   | ax.bar(points, frequency) |
| 10  | # set title and labels |
| 11  | ax.set_title('Wine Review Scores') |
| 12  | ax.set_xlabel('Points') |
| 13  | ax.set_ylabel('Frequency') |

 [view raw](https://gist.github.com/TannerGilbert/11dafc99f0e6a63056a7abc6fd0722e0/raw/5503d7a5007ce1c3bf890e528b4c11cdeae54a16/matplotlib_simple_barchart.py)  [matplotlib_simple_barchart.py](https://gist.github.com/TannerGilbert/11dafc99f0e6a63056a7abc6fd0722e0#file-matplotlib_simple_barchart-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/39f040de970f9cbabec704ac61a082af.png)![1*XZNu7gvDaXYb7-xJ6PXNIQ.png](../_resources/e86bb936d82237c3153f0e5c9c4eb227.png)

Figure 8: Bar-Chart

* * *

*...*

### Pandas Visualization

Pandas is a open source high-performance, easy-to-use library providing data structures, such as dataframes, and data analysis tools like the visualization tools we will use in this article.

Pandas Visualization makes it really easy to create plots out of a pandas dataframe and series. It also has a higher level API than Matplotlib and therefore we need less code for the same results.

Pandas can be installed using either pip or conda.
pip install pandas
or
conda install pandas

#### Scatter Plot

To create a scatter plot in Pandas we can call `<dataset>.plot.scatter()` and pass it two arguments, the name of the x-column as well as the name of the y-column. Optionally we can also pass it a title.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset') |

 [view raw](https://gist.github.com/TannerGilbert/eccb1544e6655c22d8607c9b76ffc6f7/raw/971a761b8f3ba40fe201bc86e4d38339dc44135d/pandas_simple_scatterplot.py)  [pandas_simple_scatterplot.py](https://gist.github.com/TannerGilbert/eccb1544e6655c22d8607c9b76ffc6f7#file-pandas_simple_scatterplot-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/5866872d59ae562c5cfe9a2b5264c5fa.png)![1*rKWbvmZnJi4PDwkMt2tQ5g.png](../_resources/cd415cdf2a010c08ce53ed0aac7b5e2f.png)

Figure 9: Scatter Plot

As you can see in the image it is automatically setting the x and y label to the column names.

#### Line Chart

To create a line-chart in Pandas we can call `<dataframe>.plot.line()`. Whilst in Matplotlib we needed to loop-through each column we wanted to plot, in Pandas we don’t need to do this, because it automatically plots all available numeric columns (at least if we don’t specify a specific column/s).

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | iris.drop(['class'], axis=1).plot.line(title='Iris Dataset') |

 [view raw](https://gist.github.com/TannerGilbert/719fff93fad8a1de1e6959b7d91b24f7/raw/4391e7a671444e7bbff625a975a150def419c8f6/pandas_simple_linechart.py)  [pandas_simple_linechart.py](https://gist.github.com/TannerGilbert/719fff93fad8a1de1e6959b7d91b24f7#file-pandas_simple_linechart-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/e0bc7d7ee7db3d65e228321f3fcd223c.png)![1*7_h8orPIGV42e5AIWF-7bA.png](../_resources/b608a97532e12a8ed93b957440035d45.png)

Figure 10: Line Chart

If we have more than one feature Pandas automatically creates a legend for us, as can be seen in the image above.

#### Histogram

In Pandas we can create a Histogram with the `plot.hist` method. There aren’t any required arguments but we can optionally pass some like the bin size.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | wine_reviews['points'].plot.hist() |

 [view raw](https://gist.github.com/TannerGilbert/ac6a919bb10e943a39cd5635fd2b9019/raw/037e2fa76fc63878546e1e1fea37bb0caee5e3df/pandas_simple_histogram.py)  [pandas_simple_histogram.py](https://gist.github.com/TannerGilbert/ac6a919bb10e943a39cd5635fd2b9019#file-pandas_simple_histogram-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/67498365ff27117967f8a19fae6fe4f1.png)![1*beVHz116spOm-r5OYunZoA.png](../_resources/7d009a2d507db937616722e29f005e77.png)

Figure 11: Histogram
It’s also really easy to create multiple histograms.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | iris.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20) |

 [view raw](https://gist.github.com/TannerGilbert/5624dd6398a7bb2ac52a8beb347082c6/raw/9884d7872bf905b48c8f08bbbb311cbfc94f0427/pandas_multiple_histograms.py)  [pandas_multiple_histograms.py](https://gist.github.com/TannerGilbert/5624dd6398a7bb2ac52a8beb347082c6#file-pandas_multiple_histograms-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/3bb71e0fd3660a40a9ae2d246a7da78d.png)![1*xwANpRZID0XPhr4ESfS6qg.png](../_resources/acb1adcd038e6a79e195e726d8591e93.png)

Figure 12: Multiple Histograms

The `subplots` argument specifies that we want a separate plot for each features and the `layout` specifies the number of plots per row and column.

#### Bar Chart

To plot a bar-chart we can use the `plot.bar()` method, but before we can call this we need to get our data. For this we will first count the occurrences using the `value_count()` method an then sort the occurrences from smallest to largest using the `sort_index()` method.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | wine_reviews['points'].value_counts().sort_index().plot.bar() |

 [view raw](https://gist.github.com/TannerGilbert/b29eaa33ebf75ce708de241b2984a931/raw/cde38ba44335d8134cbb927ec041e653d85c401c/pandas_simple_barchart_vertical.py)  [pandas_simple_barchart_vertical.py](https://gist.github.com/TannerGilbert/b29eaa33ebf75ce708de241b2984a931#file-pandas_simple_barchart_vertical-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/881709be5b31db7414726da82d999766.png)![1*OcOW7mKcLv4c71jNY40qiA.png](../_resources/5d9cb7c6a51e9840cde303d4abc98977.png)

Figure 13: Vertical Bar-Chart

It’s also really simple to make a horizontal bar-chart using the `plot.barh()` method.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | wine_reviews['points'].value_counts().sort_index().plot.barh() |

 [view raw](https://gist.github.com/TannerGilbert/2fbc3696a1d1fbf37a55ba526f2a268c/raw/a3b9f740b72665543ad464667b49222478323cdc/pandas_simple_barchart_horizontal.py)  [pandas_simple_barchart_horizontal.py](https://gist.github.com/TannerGilbert/2fbc3696a1d1fbf37a55ba526f2a268c#file-pandas_simple_barchart_horizontal-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/12ba34d37267ee6135c7c54cfa423df3.png)![1*z9vf-rjL7Ty0T68DIWzlng.png](../_resources/a3e051b0848467b89ee8d4d909ac6c58.png)

Figure 14: Horizontal Bar-Chart
We can also plot other data then the number of occurrences.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar() |

 [view raw](https://gist.github.com/TannerGilbert/2bd6b9e031f7f1ed4818a9a0556158ab/raw/b4f34b11512453329efdcc0d173b0f4d0629fbac/pandas_simple_barchart_vertical_2.py)  [pandas_simple_barchart_vertical_2.py](https://gist.github.com/TannerGilbert/2bd6b9e031f7f1ed4818a9a0556158ab#file-pandas_simple_barchart_vertical_2-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/33f4fcdf56638b1ec9e060b53c5b706d.png)![1*AoST_ulRv6JvmmLFPqgK4w.png](../_resources/1cadbe9f1bdde06bb6b55e70c9d063ee.png)

Figure 15: Countries with the most expensive wine(on average)

In the example above we grouped the data by country and then took the mean of the wine prices, ordered it, and plotted the 5 countries with the highest average wine price.

* * *

*...*

### Seaborn

Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for creating attractive graphs.

Seaborn has a lot to offer. You can create graphs in one line that would take you multiple tens of lines in Matplotlib. It’s standard designs are awesome and it also has a nice interface for working with pandas dataframes.

It can be imported by typing:
`import seaborn as sns`

#### Scatter plot

We can use the `.scatterplot` method for creating a scatterplot, and just as in Pandas we need to pass it the column names of the x and y data, but now we also need to pass the data as an additional argument because we aren’t calling the function on the data directly as we did in Pandas.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.scatterplot(x='sepal_length', y='sepal_width', data=iris) |

 [view raw](https://gist.github.com/TannerGilbert/c176a0642f7b1de64a5a64766c631cd2/raw/f87a01645d37e576c75550aa962ab1beaeca1403/seaborn_simple_scatterplot.py)  [seaborn_simple_scatterplot.py](https://gist.github.com/TannerGilbert/c176a0642f7b1de64a5a64766c631cd2#file-seaborn_simple_scatterplot-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/f4f30ca0a58a29314bf5afcaf95044fd.png)![1*paa5lGLVyCPzuzxM0g1hCg.png](../_resources/4f3efe8435043eadda451b3cd7623097.png)

Figure 16: Scatterplot

We can also highlight the points by class using the `hue` argument, which is a lot easier than in Matplotlib.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.scatterplot(x='sepal_length', y='sepal_width', hue='class', data=iris) |

 [view raw](https://gist.github.com/TannerGilbert/21589cd4313a7c47824541fc1a16d07d/raw/84d9db672ecb2393ccc619559f9a9fbcdba6fda0/seaborn_simple_scatterplot_colored.py)  [seaborn_simple_scatterplot_colored.py](https://gist.github.com/TannerGilbert/21589cd4313a7c47824541fc1a16d07d#file-seaborn_simple_scatterplot_colored-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/945648bac312006bf2c04cd3323a6171.png)![1*WpOCsT4LhXv2PE6_Kntw9A.png](../_resources/20f0e8ae85a460e408c05b06f4877ca6.png)

Figure 17: Scatterplot colored by class

#### Line chart

To create a line-chart the `sns.lineplot` method can be used. The only required argument is the data, which in our case are the four numeric columns from the Iris dataset . We could also use the `sns.kdeplot` method which rounds of the edges of the curves and therefore is cleaner if you have a lot of outliers in your dataset.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.lineplot(data=iris.drop(['class'], axis=1)) |

 [view raw](https://gist.github.com/TannerGilbert/c8c6ba5a36819760fc93ee456f0237c0/raw/8149cfed20a12178bad9aad6d562b55b7a734ab0/seaborn_simple_linechart.py)  [seaborn_simple_linechart.py](https://gist.github.com/TannerGilbert/c8c6ba5a36819760fc93ee456f0237c0#file-seaborn_simple_linechart-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/d4d3a5b33f279614852e8a019eb432d2.png)![0*dDnPHTxd_0hiZloL](../_resources/7476ffaaa987c0c7e9df43d5e15892dc.png)

Figure 18: Line Chart

#### Histogram

To create a histogram in Seaborn we use the `sns.distplot` method. We need to pass it the the column we want to plot and it will calculate the occurrences itself. We can also pass it the number of bins, and if we want to plot a gaussian kernel density estimate inside the graph.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.distplot(wine_reviews['points'], bins=10, kde=False) |

 [view raw](https://gist.github.com/TannerGilbert/ff44ccae18fd07685c1a1c58a405a4b6/raw/a51f44b593d925a802802b604ee025570c2e9884/seaborn_simple_histogram.py)  [seaborn_simple_histogram.py](https://gist.github.com/TannerGilbert/ff44ccae18fd07685c1a1c58a405a4b6#file-seaborn_simple_histogram-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/a45e6e22e14e0d0ca85438f98a5b0b62.png)![1*3bXHuQVWK8W9EgdxgCrzLg.png](../_resources/29cdd0893d6f8c8814a8ba26a044df65.png)

Figure 19: Histogram

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.distplot(wine_reviews['points'], bins=10, kde=True) |

 [view raw](https://gist.github.com/TannerGilbert/aaa258a724bda5dcee567f1f26437444/raw/f2e93250e9ba70aa2ff94221e05c53317f946181/seaborn_simple_histogram_with_gaussian.py)  [seaborn_simple_histogram_with_gaussian.py](https://gist.github.com/TannerGilbert/aaa258a724bda5dcee567f1f26437444#file-seaborn_simple_histogram_with_gaussian-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/752aef7bf8fa500a33282d90f11a24e3.png)![1*icIVAWYElWDkzCdB1BuE6g.png](../_resources/6adac3f8a90696be1c2bc7b1e5aa52fb.png)

Figure 20: Histogram with gaussian kernel density estimate

#### Bar chart

In Seaborn a bar-chart can be created using the `sns.countplot` method and passing it the data.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.countplot(wine_reviews['points']) |

 [view raw](https://gist.github.com/TannerGilbert/6cb8d4613816d9a7e8e00c262c101f7e/raw/8166a74e913ba2a7b7a8f6ce7b8d7843f509439a/seaborn_simple_bar_chart.py)  [seaborn_simple_bar_chart.py](https://gist.github.com/TannerGilbert/6cb8d4613816d9a7e8e00c262c101f7e#file-seaborn_simple_bar_chart-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/1837cef94c06bf9b82987fa154074368.png)![1*JK28mO0Ph0WI4BpGAolBkg.png](../_resources/2f6b328abc05f4fd58cade4eae161ac8.png)

Figure 21: Bar-Chart

### Other graphs

Now that you have a basic understanding of the Matplotlib, Pandas Visualization and Seaborn syntax I want to show you a few other graph types that are useful for extracting insides.

For most of them Seaborn is the go to library because of its high level interface that allows for the creation of beautiful graphs in just a few lines of code.

#### Box plots

A Box Plot is graphical method of displaying the [five-number summary](https://en.wikipedia.org/wiki/Five-number_summary). We can create box plots using seaborns `sns.boxplot` method and passing it the data as well as the x and y column name.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | df = wine_reviews[(wine_reviews['points']>=95) & (wine_reviews['price']<1000)] |
| 2   | sns.boxplot('points', 'price', data=df) |

 [view raw](https://gist.github.com/TannerGilbert/a15f5a59c3caacfb5e4718ceb6d082c2/raw/1b9ed1c7917dd76f79fd46d64a79fbcad9092c30/seaborn_boxplot.py)  [seaborn_boxplot.py](https://gist.github.com/TannerGilbert/a15f5a59c3caacfb5e4718ceb6d082c2#file-seaborn_boxplot-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/c01a31e0711c23f3a9037bf8972646ee.png)![0*Zsl-nF0hT9BrMFp4](../_resources/7ed50bcd39e8abb3c6cec88513b19af9.png)

Figure 22: Boxplot

Box Plots, just like bar-charts are great for data with only a few categories but can get messy really quickly.

#### Heatmap

A Heatmap is a graphical representation of data where the individual values contained in a [matrix](https://en.wikipedia.org/wiki/Matrix_%28mathematics%29) are represented as colors. Heatmaps are perfect for exploring the correlation of features in a dataset.

To get the correlation of the features inside a dataset we can call `<dataset>.corr()` , which is a Pandas dataframe method. This will give use the [correlation matrix](https://www.displayr.com/what-is-a-correlation-matrix/).

We can now use either Matplotlib or Seaborn to create the heatmap.
Matplotlib:

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # get correlation matrix |
| 2   | corr = iris.corr() |
| 3   | fig, ax = plt.subplots() |
| 4   | # create heatmap |
| 5   | im = ax.imshow(corr.values) |
| 6   |     |
| 7   | # set labels |
| 8   | ax.set_xticks(np.arange(len(corr.columns))) |
| 9   | ax.set_yticks(np.arange(len(corr.columns))) |
| 10  | ax.set_xticklabels(corr.columns) |
| 11  | ax.set_yticklabels(corr.columns) |
| 12  |     |
| 13  | # Rotate the tick labels and set their alignment. |
| 14  | plt.setp(ax.get_xticklabels(), rotation=45, ha="right", |
| 15  |  rotation_mode="anchor") |

 [view raw](https://gist.github.com/TannerGilbert/a13560bfd75ad12d8af6b92a1938e97a/raw/6a68a61c932afec26e7cf5a194b521821aaa9ad2/matplotlib_heatmap.py)  [matplotlib_heatmap.py](https://gist.github.com/TannerGilbert/a13560bfd75ad12d8af6b92a1938e97a#file-matplotlib_heatmap-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/8022ec6175a6acbb995f764ab2ea21dd.png)![1*Y73510z5S8jbBtAdhuU0-A.png](../_resources/d6d2cbc1dc9a3cb37fe1bdea8e285d75.png)

Figure 23: Heatmap without annotations
To add annotations to the heatmap we need to add two for loops:

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | # get correlation matrix |
| 2   | corr = iris.corr() |
| 3   | fig, ax = plt.subplots() |
| 4   | # create heatmap |
| 5   | im = ax.imshow(corr.values) |
| 6   |     |
| 7   | # set labels |
| 8   | ax.set_xticks(np.arange(len(corr.columns))) |
| 9   | ax.set_yticks(np.arange(len(corr.columns))) |
| 10  | ax.set_xticklabels(corr.columns) |
| 11  | ax.set_yticklabels(corr.columns) |
| 12  |     |
| 13  | # Rotate the tick labels and set their alignment. |
| 14  | plt.setp(ax.get_xticklabels(), rotation=45, ha="right", |
| 15  |  rotation_mode="anchor") |
| 16  |     |
| 17  | # Loop over data dimensions and create text annotations. |
| 18  | for i in  range(len(corr.columns)): |
| 19  |  for j in  range(len(corr.columns)): |
| 20  | text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2), |
| 21  |  ha="center", va="center", color="black") |

 [view raw](https://gist.github.com/TannerGilbert/26e50b5ed116eef7da62205da1ffebf3/raw/a8b3bf072e189d3445e5bd030bd04788472983c4/matplotlib_heatmap_with_annotations.py)  [matplotlib_heatmap_with_annotations.py](https://gist.github.com/TannerGilbert/26e50b5ed116eef7da62205da1ffebf3#file-matplotlib_heatmap_with_annotations-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/12044c65c5c880f541dc27f5981ad475.png)![1*djE6fjLgvNR8id_9-TQQvQ.png](../_resources/45bea858c603380f4c0bd011bfb68290.png)

Figure 24: Heatmap with annotations
Seaborn makes it way easier to create a heatmap and add annotations:

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.heatmap(iris.corr(), annot=True) |

 [view raw](https://gist.github.com/TannerGilbert/e3d02071fd7817300f79fc9396e5511d/raw/f3d4c6074da8044476da5cac42330ba0c4399eb4/seaborn_heatmap.py)  [seaborn_heatmap.py](https://gist.github.com/TannerGilbert/e3d02071fd7817300f79fc9396e5511d#file-seaborn_heatmap-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/e3b1dc4842576ebf0aedeb76dcb3cb22.png)![1*nFikwCXWGr8vD95CGPBB4Q.png](../_resources/84e11402168816b4bebee6cb1b005602.png)

Figure 25: Heatmap with annotations

#### Faceting

Faceting is the act of breaking data variables up across multiple subplots, and combining those subplots into a single figure.

Faceting is really helpful if you want to quickly explore your dataset.

To use one kind of faceting in Seaborn we can use the `FacetGrid` . First of all we need to define the `FacetGrid` and pass it our data as well as a row or column, which will be used to split the data. Then we need to call the `map `function on our `FacetGrid` object and define the plot type we want to use, as well as the column we want to graph.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | g = sns.FacetGrid(iris, col='class') |
| 2   | g = g.map(sns.kdeplot, 'sepal_length') |

 [view raw](https://gist.github.com/TannerGilbert/baf3a2cfc538c93268fe272ce837e52a/raw/41c6628e2fabb0aea726cda08d9d48170e3740e7/seaborn_faceting.py)  [seaborn_faceting.py](https://gist.github.com/TannerGilbert/baf3a2cfc538c93268fe272ce837e52a#file-seaborn_faceting-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/12081ad73a8603d8631ba4e7f4ce19a5.png)![0*5hVqRSiIBn7VxvdC](../_resources/1903ef7c70691bb6891457c3349e8ba4.png)

Figure 26: Facet-plot

You can make plots a lot bigger and more complicated than the example above. You can find a few example [here](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html).

#### Pairplot

Lastly I will show you Seaborns `pairplot` and Pandas `scatter_matrix` , which enable you to plot a grid of pairwise relationships in a dataset.

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | sns.pairplot(iris) |

 [view raw](https://gist.github.com/TannerGilbert/1930ed08d2292757290574a53712c0f9/raw/255f17052ab2aac7dee92ab3f1fe793bf70c161d/seaborn_pairplot.py)  [seaborn_pairplot.py](https://gist.github.com/TannerGilbert/1930ed08d2292757290574a53712c0f9#file-seaborn_pairplot-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/4286eaa03932a7863b8604008e014e56.png)![0*KcPZIjL_6IA3WjVs](../_resources/14bb274e45c1c38fa486c16ef024cd42.png)

Figure 27: Pairplot

![](../_resources/14e92a52da697f93e7053264ab3586ba.png)

|     |     |
| --- | --- |
| 1   | from pandas.plotting import scatter_matrix |
| 2   |     |
| 3   | fig, ax = plt.subplots(figsize=(12,12)) |
| 4   | scatter_matrix(iris, alpha=1, ax=ax) |

 [view raw](https://gist.github.com/TannerGilbert/124904f9edc03834cc06e9b50337e989/raw/1180861d49a0c49d98dbb1c170ce4a6e5c43f8a7/pandas_scatter_matrix_exampel.py)  [pandas_scatter_matrix_exampel.py](https://gist.github.com/TannerGilbert/124904f9edc03834cc06e9b50337e989#file-pandas_scatter_matrix_exampel-py) hosted with ❤ by [GitHub](https://github.com/)

![](../_resources/fd5850fbae3dfa75f6d02243ae85ed83.png)![1*HxQS2-d8kG4m1i2Q3m88dA.png](../_resources/2d655441babea186c40fbef8d483a009.png)

Figure 28: Scatter matrix

As you can see in the images above these techniques are always plotting two features with each other. The diagonal of the graph is filled with histograms and the other plots are scatter plots.

* * *

*...*

### Recommended Reading

[**Scraping Reddit data** *How to scrape data from Reddit using the Python Reddit API Wrapper(PRAW)*towardsdatascience.com](https://towardsdatascience.com/scraping-reddit-data-1c0af3040768)[(L)](https://towardsdatascience.com/scraping-reddit-data-1c0af3040768)

* * *

*...*

### Conclusion

Data visualization is the discipline of trying to understand data by placing it in a visual context, so that patterns, trends and correlations that might not otherwise be detected can be exposed.

Python offers multiple great graphing libraries that come packed with lots of different features. In this article we looked at Matplotlib, Pandas visualization and Seaborn.

If you liked this article consider subscribing on my [Youtube Channel](https://www.youtube.com/channel/UCBOKpYBjPe2kD8FSvGRhJwA) and following me on social media.

The code covered in this article is available as a [Github Repository](https://github.com/TannerGilbert/Articles/tree/master/Introduction%20to%20Data%20Visualization%20in%C2%A0Python).

If you have any questions, recommendations or critiques, I can be reached via [Twitter](https://twitter.com/Tanner__Gilbert) or the comment section.