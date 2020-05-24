How to Think of Pandas Data Visualization If You’re Coming From Excel

# How to Think of Pandas Data Visualization If You’re Coming From Excel

## Building a Mental Model for Data Visualization in Pandas

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='183' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='184' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![2*kJ4z8uQhrlEwSdrwX2P7gA.jpeg](../_resources/d2adfd3a608d7899f9b6c8c7116686a6.jpg)](https://towardsdatascience.com/@iamkennethcpa?source=post_page-----7af9f933e212----------------------)

[Kenneth Infante](https://towardsdatascience.com/@iamkennethcpa?source=post_page-----7af9f933e212----------------------)

[May 2](https://towardsdatascience.com/how-to-think-of-pandas-data-visualization-if-youre-coming-from-excel-7af9f933e212?source=post_page-----7af9f933e212----------------------) · 5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='200'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='201' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='206'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='207' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/7af9f933e212/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='215'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='216' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/7af9f933e212/share/facebook?source=post_actions_header---------------------------)

![0*xzcWDbqJd_ExZWCZ](../_resources/2f41e3f221883fd297cc9e3ce631ed23.jpg)
![0*xzcWDbqJd_ExZWCZ](../_resources/741bde9a63084df6f1565b905e7fbbcd.jpg)

Photo by [Kristopher Roller](https://unsplash.com/@krisroller?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Having read a lot of tutorials on Pandas data visualization, I still can’t grasp the mechanics of it. Creating even a simple plot always requires me to look into the documentation.

And even after running the code and getting the plot right, it doesn’t make me confident to try it on my own. Perhaps, I’m looking for the familiarity of Excel. The connection between the plot and data just seems to be intuitive using the GUI.

With that in mind, can I somehow bring this to Pandas?

# Charting in Excel and Pandas

So what I did is to plot a simple line plot in Excel. Consider the following data (get it [here](https://github.com/kennethjhim/medium_pandas_data_viz_from_excel)).

![1*BjTfamk4mz-QndrS9UrU8w.png](../_resources/3a21bbe7a8686ab12d8470495be16358.png)
![1*BjTfamk4mz-QndrS9UrU8w.png](../_resources/6fc0ffc45f2675f88552f21221d5a241.png)
No. of Immigrants to Canada from China and India 1980–2013
Then I plot a line chart using the Excel’s Recommended Charts feature
![1*kqFNPgT203Q4ckk93kj_Uw.png](../_resources/cd45f12acbdf7c2825b53c60a614d01d.png)
![1*kqFNPgT203Q4ckk93kj_Uw.png](../_resources/9e06e7e0a138b35b2366bf26a66f3184.png)
Alright. Nice and Easy.
How about the same data but in a different format?
![1*xFczyvrUG-M6NA65YKli0w.png](../_resources/907c54b8c0a8c4318c5781308c470be2.png)
![1*xFczyvrUG-M6NA65YKli0w.png](../_resources/08a48af040b7bb0c7e563e0ee4f3fddb.png)
No. of Immigrants to Canada from China and India 1980–2013 (long-form)
Plotting this..
![1*oN57M-JrXi9egilyvfro8g.png](../_resources/158d50c24e21402c27846b128931d401.png)
![1*oN57M-JrXi9egilyvfro8g.png](../_resources/e3ec4519c4a2738d392a8b9a9443c683.png)
Ok. That’s a mess.
*How about in Pandas? Let’s plot the first dataframe.*
![1*DsuvJrzQtAF2_FH-Z62axg.png](../_resources/4520f18b597e94d500d180af155c9253.png)
![1*DsuvJrzQtAF2_FH-Z62axg.png](../_resources/f063a6cfc4735b2e271285bba145ee7d.png)
Ok. That works.
How about the second dataframe?
![1*7QGEsUZpdhfoU6WV9B1Gsw.png](../_resources/5a6c5b6b396672cbe2b6f5886df053e5.png)
![1*7QGEsUZpdhfoU6WV9B1Gsw.png](../_resources/498d304571a6a182926bd29e7d95c225.png)
Both the Excel and Pandas showed the same plot for both dataframes.
*It seems Excel and Pandas render plot the same way!* I’m on to something.

# Wide-form vs. Long-form Data

The data we have dealt a while ago are the wide-form and long-form data respectively.

Both are sensible patterns for storing data in a tabular format; briefly, the difference is this:

- wide-form data has one row per *independent variable*, with metadata recorded in the *row and column labels*.
- long-form data has one row per *observation*, with metadata recorded within the table as *values*.

And this was my aha! moment.

*> The wide-form has worked well with line chart because I’m basically plotting an independent variable (year) against its metadata (the Haiti and China series).*

Now, will this line of thinking work? Let’s found out.

# Creating Basic Plots with Pandas

Now, let’s try to create different plots for our wide-form data to test my hypothesis.

**Bar Chart**
![1*6E8k8sXzZnrlkvZP7CmnUg.png](../_resources/39efa12a31342d3dd5c36ebb44d98590.png)
![1*6E8k8sXzZnrlkvZP7CmnUg.png](../_resources/12f5d55873268d22b09d8a4261e9c57b.png)
**Area Plot**
![1*ShqpTjzvSzDshk3Lx_FNjQ.png](../_resources/c65249dd7d7e0ac89f7dc17f34c3fa91.png)
![1*ShqpTjzvSzDshk3Lx_FNjQ.png](../_resources/5d85e095efa13964335835e5920cde6d.png)
**Box Plots**
![1*KLN6SBNjcbRJaehra_fZ6A.png](../_resources/30b46b16afd0b2ba23529f4553389eb1.png)
![1*KLN6SBNjcbRJaehra_fZ6A.png](../_resources/5e23bb15953450691460d1ebc7ae387c.png)
**Histograms**
![1*9n_Hwy0U5Ems_x_wq4wKAg.png](../_resources/57c38509c79c939771c523a7848037ab.png)
![1*9n_Hwy0U5Ems_x_wq4wKAg.png](../_resources/4f3427b92ce55347bd3f85412be66f48.png)
**Scatter Plots**
![1*EbJ2VobPD8RgLKkL53kKVw.png](../_resources/9d9935a1d375de33d9929347e4f5ed5a.png)
![1*EbJ2VobPD8RgLKkL53kKVw.png](../_resources/a247da28b22d0cde15505c0eb4fb1fd0.png)
Eh? What’s going on?
Unfortunately, the scatter plot result in an error.

# My Second Aha Moment

So looking back to the previous plots, it’s now making sense.

*> If you’re plotting multiple Series against an independent variable, then you use the wide-form. Otherwise, use the long-form.*

Let’s test again this hypothesis and see if it holds true. Let’s do a scatter plot.

**Scatter Plot**
![1*qY0bB2wA89m8PUpHgWW9rA.png](../_resources/2f6bb08a35bab0ebef8f0b5303dc1082.png)
![1*qY0bB2wA89m8PUpHgWW9rA.png](../_resources/8ae4674597b4b0690c99e43c79faccb9.png)
Hooray! That works.

So I’m really not comparing two series in the scatter plot, rather I’m plotting the observation to see their distribution. The colors are optional and I can do the same without it.

![1*6FHTF4UpH0YlssjY3VbJZQ.png](../_resources/77f1f32672be06c14e6bd210be6eaacc.png)
![1*6FHTF4UpH0YlssjY3VbJZQ.png](../_resources/9b02d7456bd058da975eb352fa29c384.png)

# But There are Other Libraries Out There…

I chose to limit the plotting discussed here to the DataFrame's `plot` method.

When you’re new to Pandas coming From Excel, you want to evaluate quickly if you can reproduce the usual charts that you’re using in Excel to warrant the switch and continuous use of Pandas.

Besides, effective data analysis hinges with fast creation of plots; plot this, manipulate data, plot again, and so on. Hence, you’re going to be bogged down if I try to incorporate different plotting methods here.

> Take this as Pareto principle as applied to visualization — you only need to know 20% of the plotting techniques to get productive.

# Conclusion

In summary, data in wide-form works well when you’re comparing or plotting multiple Series against the same index. Otherwise, it’s better to stick with the long-form.

The workflow here is that you need to get the data first in the right form to get the desired plot which dictates the right format in the first place.

![1*FTeTclkKZzQRn7mA50BvVg.png](../_resources/41507f291d823bf3318efb10a2ccdebb.png)
![1*FTeTclkKZzQRn7mA50BvVg.png](../_resources/c4f5b36a5fd108676cb916e6519dc229.png)

Feedback loop between the data, plot, and you. (Brain gear icon from freesvg.org and plot icon from needpix.com)

Only then you could design or add elements to the plot to make it more appealing.

This is similar to Excel when doing data visualization. You have to get the right data first for Excel to spit out the right chart without the bells and whistles. Then you change chart elements, add title, etc. to more it more effective.

Rather than reading a lot of tutorials on Pandas data visualization, having a mental model of how the data corresponds to the plot makes data visualization more fun. The feedback loop between your mental model and tool makes learning more effective.

That’s it! Happy coding!

***Thank you for reading my article. Follow me on ***[***Twitter***](https://twitter.com/iamkennethcpa)*** and ***[***Linkedin***](https://www.linkedin.com/in/kennethinfante/)***.***