4 Reasons Why I’m Choosing Plotly as My Main Visualization Library

# 4 Reasons Why I’m Choosing Plotly as My Main Visualization Library

## Take your Visualizations to the 21st Century

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='177' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='178' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*VmdbajrpX9nwOc9UtkV3Yg.png](../_resources/2120e742685752023c6ded05626f9d07.png)](https://towardsdatascience.com/@radecicdario?source=post_page-----dc4a961a402f----------------------)

[Dario Radečić](https://towardsdatascience.com/@radecicdario?source=post_page-----dc4a961a402f----------------------)

[Mar 23](https://towardsdatascience.com/4-reasons-why-im-choosing-plotly-as-the-main-visualization-library-dc4a961a402f?source=post_page-----dc4a961a402f----------------------) · 5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='194'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='195' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

It can be difficult to choose a perfect data visualization platform, as it will heavily depend on which programming language you are the best at, or if you are even willing to use programming languages to make visualizations — as it’s not mandatory.

![1*NW9SbRMThR8jQT7d-JIZQg.jpeg](../_resources/7551d592ac49c7312152fe789711d165.jpg)
![1*NW9SbRMThR8jQT7d-JIZQg.jpeg](../_resources/600aba3391d9dbd631a178282c753f9b.jpg)

In a world of so many great plotting libraries — especially for the JavaScript users — today I will explain to you why I’m choosing **Plotly **over everything else.

It might not be something you’ll agree with, but give me a couple of minutes of your time to read through the arguments — it will be worth your time.

Before beginning, I’d just want to say that I’m in no way, shape, or form affiliated with developers behind Plotly nor I’ve been contributing with the development. This article is purely based on** personal experience **and is aimed to help you with choosing a perfect visualization library for your project.

With that being said, let’s jump into the reasons why you’re here.

* * *

*...*

# #1. It’s Python

Now, you’ll consider this as a benefit only if you know Python already — but since you’re reading a Data Science blog I’m assuming you are.

Python’s syntax is clear, clean, and easy to use, and Plotly is no exception. Just take a look at how little code is needed to produce a simple **bubble chart**:

import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(
x=[1, 2, 3, 4],
y=[10, 11, 12, 13],
mode=’markers’,
marker=dict(size=[40, 60, 80, 100],
color=[0, 1, 2, 3])
))
fig.show()
Running this code will produce a visually appealing chart shown below:
![1*Hqi35RtKLqlK5YShYRkI3Q.png](../_resources/7fd47a981869475bdba43cb66ddfaabe.png)
![1*Hqi35RtKLqlK5YShYRkI3Q.png](../_resources/579cb5844a8ff3ebe154336f02fd0a03.png)
From the [docs](https://plot.ly/python/line-and-scatter/)

It’s not a secret that I’m a fan of Python syntax, but if you aren’t, you can still use Plotly with *R* and *JavaScript*. Nevertheless, let’s proceed to the next point.

* * *

*...*

# #2. It’s Interactive

If you’ve followed the first point and executed the provided code, then you’re already aware that visualizations in Plotly are interactive.

![0*zRyV0a6s3tdCijG5](../_resources/4f942093c61909bb1dcfffd25c266ced.jpg)
![0*Lvq6aNacBUulLUa_](../_resources/05163dca0e9e221c013548c231af6fdb.jpg)

Photo by [Isaac Smith](https://unsplash.com/@isaacmsmith?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Maybe that’s not a huge thing to you if you’re coming from a JavaScript background, but it’s a huge thing for anyone coming from Python. Visualizations made through `Matplotlib` are not interactive, and look pretty much worse by default than default visualizations from Plotly.

You **don’t need to specify** that you want your chart to be interactive, but you sure can tweak what is visible on hover.

More on that in later articles, there are many more to come in this Plotly series.

* * *

*...*

# #3. Clear Syntax

Your Plotly chart will have a `Figure` object, populated with:

- `Data` object
- `Layout` object

As you might figure, you’ll put the data which makes the charts in the `data`, and in `layout` you’ll specify how the chart should look like. Let’s take a look at an example.

Let’s make a few **imports **first:
import numpy as np
np.random.seed(42)
import plotly.offline as pyo
import plotly.graph_objs as go
Now let’s define the **data **which will go into the chart:
x = np.random.randint(1, 101, 100)
y = np.random.randint(1, 101, 100)data = [go.Scatter(
x=x,
y=y,
mode='markers',
)]

That’s it. This will create a scatter plot from random integers on both the x-axis and the y-axis. Now let’s define the **layout**:

layout = go.Layout(
title=’Plot title’,
xaxis=dict(title=’X-Axis’),
yaxis=dict(title=’Y-Axis’),
hovermode=’closest’
)
And now let’s put everything into a `Figure` object and plot it:
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

If you ask me that was as clean as data visualization can be. If you were to take this code, put it in a single `.py` script and run it, the visualization would be saved as a `html` file and automatically opened in your browser:

![1*fC_1_DiIRwUu0JsGPI-QeQ.png](../_resources/f7a0195fb37607b7c02812ac43bebe68.png)
![1*fC_1_DiIRwUu0JsGPI-QeQ.png](../_resources/8151dddb6e724e26230ef1f74ae56c08.png)

Not too shabby, but we’ll dive much deeper into styling in the following articles.

* * *

*...*

# #4. Dashboards

If you know some basic HTML and CSS then it’s very easy to incorporate multiple charts into a single, good-looking dashboard.

![0*Lvq6aNacBUulLUa_](../_resources/3abe73f9ba5d15f91f22144a3afadf9a.jpg)
![0*zRyV0a6s3tdCijG5](../_resources/2a0fac6404ff7175b631f351e018560d.jpg)

Photo by [Carlos Muza](https://unsplash.com/@kmuza?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Plotly charts can be incorporated with `Dash`, a framework for building **web applications**.

Here’s a paragraph from the official documentation:

> Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It’s particularly suited for anyone who works with data in Python.

This `React` part will transform your app into a **Single Page Application**, meaning that there won’t be those awkward refreshes upon clicking on stuff. And all of this without knowing any web development. Awesome.

We won’t dive into dashboard development now, but few articles down the road will cover it in depth.

If you can’t wait to see what can be produced with `Dash`, here’s the official **gallery**:

[ ## Dash Enterprise   ### Dash Enterprise    #### Dash Enterprisedash-gallery.plotly.host](https://dash-gallery.plotly.host/Portal/)

* * *

*...*

# Before you go

I’m perfectly fine with looking at the tabular data. But a big part of my job is **presenting **findings and conclusion to others, and every single time showing a chart will be a far more effective method.

In the next month or so I’ve decided to publish 10-ish articles that will cover Plotly and Dash front to back, making sure that data visualization won’t be a painful process to you in the future.

Thanks for reading and stay tuned.