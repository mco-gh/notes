HiPlot: High-dimensional interactive plots made easy

[Developer tools](https://ai.facebook.com/blog/results/developer-tools/)|
[Research](https://ai.facebook.com/blog/results/research/)

# HiPlot: High-dimensional interactive plots made easy

January 31, 2020
Written by
Daniel Haziza, Jérémy Rapin, and Gabriel Synnaeve

Share

[ ![49677251_224845165108670_5875028237406437376_n.png](../_resources/80b4ce80909efba0304d88969ac5f873.png)  ![58764946_636345113498676_2571050526707810304_n.png](../_resources/544005436f43d734b3e9cdfb46eb3ed0.png)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fai.facebook.com%2Fblog%2Fhiplot-high-dimensional-interactive-plots-made-easy%2F)

[ ![49634112_369201477192293_9127330224449519616_n.png](../_resources/b166a0e4487b7d111bd20a0038c00760.png)  ![59062757_2688893087818609_1518278481098571776_n.png](../_resources/54b6ddfc9eae9f62c96d2b8254543cf7.png)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Ftext%3DHiPlot%253A%2BHigh-dimensional%2Binteractive%2Bplots%2Bmade%2Beasy%2Bhttps%253A%252F%252Fai.facebook.com%252Fblog%252Fhiplot-high-dimensional-interactive-plots-made-easy%252F&h=AT2EuZuPh9Geuf9YhbcSKyONdve9qtaROojCtCp4MptGuqxtn-mM4lenQPBs5ERYDzKIWWkeu6QmMfo5M4QKohZ8HNWCFTIx10axSUzL46QNw-4li6pvPAH9krQz5BEyE2RP3MHdpaNYc9YQ97Npox50QQpwFXKdYF_m189l9GQ)

## What it is:

HiPlot is a lightweight interactive visualization tool to help AI researchers discover correlations and patterns in high-dimensional data. It uses parallel plots and other graphical ways to represent information more clearly, and it can be run quickly from a Jupyter notebook with no setup required. HiPlot enables machine learning (ML) researchers to more easily evaluate the influence of their hyperparameters, such as learning rate, regularizations, and architecture. It can also be used by researchers in other fields, so they can observe and analyze correlations in data relevant to their work.

[*Parallel plots*](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FParallel_coordinates&h=AT0z-NOuMXECvedow6rUROu1BGmBUf7pN1xFyjHlpfZrfIjoYsz68wTJ0mtPYvZoZS-A-teXPUbnY00hk9upR_oprZOvKREXE70uhfPRWxhJ92wUyZuBl_S6MS4JUAUChQGYBmlsPO2qlDixoWYpnDW4OWSsSfR61hrjd9NESiA) are a convenient way to visualize and filter high-dimensional data. For example, suppose you are running multiple training tasks where each has two scalar parameters, coined dropout and lr, and one optimizer (taking either “SGD” or “Adam” as values), and from this you obtain a loss, which is yet another scalar. Each of the training tasks can be represented as a data point with values (dropout, lr, optimizer, loss). HiPlot will draw one vertical scaled axis each for dropout, lr, optimizer, and loss, and each training/data point is a continuous line that goes through its value on each of the axes. The results are shown here with three different data points, in red, blue, and black.

![84369719_211321020000252_7620460104202059776_n.png](../_resources/1d341ac7d8d621e7079bf7a7cf3ac599.png)

##  What it does:

HiPlot is designed to offer several advantages over other visualization tools:

- **Interactivity**. In HiPlot, parallel plots are interactive, which makes it easy to change the visualization for different use cases. For example, you can focus on experiments that take a range or value along one or several axes, set the color scheme according to yet another axis, reorder or remove axes, or extract a particular selection of data.

0:00

HD

We first chose to display only data points obtained after 20 or more epochs of training. Then, by slicing through the “loss” axis, we observed that larger learning rates led to better performance (perplexity). You can reproduce this example here: https://facebookresearch.github.io/hiplot/_static/demo/ml1.csv.html?hip.color_by=%22valid+ppl%22 .

- **Simplicity**. You can use HiPlot in two equally straightforward ways:

Through an IPython notebook. This will reproduce the first example plot above:

import hiplot as hip

data =  [{'dropout':0.1,  'lr':  0.001,  'loss':  10.0,  'optimizer':  'SGD'},  {'dropout':0.15,  'lr':  0.01,  'loss':  3.5,  'optimizer':  'Adam'},  {'dropout':0.3,  'lr':  0.1,  'loss':  4.5,  'optimizer':  'Adam'}]hip.Experiment.from_iterable(data).display(force_full_width=True)

Through a server with the “hiplot” command. You can then access it through http://127.0.0.1:5005/ and use it to visualize, manage, and share your experiments. The simple syntax also allows you to see multiple experiments at the same time.

- **Extendability**. By default, HiPlot’s web server can parse CSV or JSON files. You can also provide it with a custom Python parser that will convert your experiments into a HiPlot experiment.To help researchers performing hyperparameter searches, HiPlot is already compatible with the logs of open source Facebook AI libraries, such as [* wav2letter@anywhere*](https://ai.facebook.com/blog/online-speech-recognition-with-wav2letteranywhere/), our inference framework for online speech recognition; [* Nevergrad*](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebookresearch%2Fnevergrad&h=AT23HoLIuL2RNFGtkDk_20woNCiCLIOEumUwys4Fp9fjKaEtMxyqDMVIalt5IXGMqNyk_ZDy-7J_-NLYG7tjia7jNJ2omstbfCPU5J-CVzxkMsaCPv1hTqE4ty9uTmol9GSoGSWvEDjejYVcmjZ26Kl0jpB84PtA5gbN1S1bIg4), our open source tool for derivative-free optimization; and [* fairseq*](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fpytorch%2Ffairseq&h=AT2klc_5pMX0VnHriFPQv3CvM1G9oq8ucGMjzH9I_8uz_R_CCGnn8QbmNwvxeoZlJmw5IRBZAsXqB1OHRDAiamGmcu6Q55Blqz4Kma5-8RCtU_iGvyzk5unDKfH4kBC2RHzNA8KMyubmocJsQHoheUseDp6UR_yG6YV10N-6inc), our sequence modeling toolkit.

- Visualization for Population-Based Training. Current approaches to hyperparameter tuning include genetic algorithms such as Population-Based Training, where training tasks can be forked several times with different hyperparameters. Such experiments can be challenging to analyze and may contain bugs that are difficult to spot. With HiPlot, such experiments can be visualized, as its XY plot can render edges between related data points.

![84252794_193081178435200_6815649280938737664_n.png](../_resources/a97d51b996a5d8ea5207a5090aaf0645.png)

##  Why it matters:

ML models are getting ever more complex and often have many hyperparameters. At Facebook AI, we have been using HiPlot to explore and efficiently analyze hyperparameter tuning of deep neural networks with dozens of hyperparameters and more than 100,000 experiments. We hope this tool will enable other scientists and engineers to explore and make the most of their own experimental data, while also paving the way for more dynamic training methods, such as those inspired by genetic algorithms.

## **Get it on GitHub:**

[* https://github.com/facebookresearch/hiplot *](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebookresearch%2Fhiplot&h=AT353zeNtkUk53Fo579kxtER37-wKjlYk6IpOFwlDT8vM-S8I9IOnUbgBLoqMPz5WorL8PaD2ZXCsZzkeTBqp_FlLcqJzm8xeiM7OSgkFTDKIle0bfTtNS2DIGUsL7bt5z2yGBiGo256mSZ0ORuCP4HLjiwxTAIz8o3riSZk43M)

(Or install with pip install hiplot.)

## Written by

Daniel Haziza
Research Engineer
Jérémy Rapin
Research Engineer
Gabriel Synnaeve
Research Scientist

## Related posts

[Online speech recognition with wav2letter@anywhere](https://ai.facebook.com/blog/online-speech-recognition-with-wav2letteranywhere/)

January 13, 2020

[Nevergrad: An open source tool for derivative-free optimization](https://ai.facebook.com/blog/nevergrad-derivative-free-optimization/)

December 20, 2018

[VizSeq: A visual analysis toolkit for accelerating text generation research](https://ai.facebook.com/blog/vizseq-a-visual-analysis-toolkit-for-accelerating-text-generation-research/)

December 19, 2019

## Related Tags

[Developer tools](https://ai.facebook.com/blog/results/developer-tools/)
[Research](https://ai.facebook.com/blog/results/research/)
[Open Source](https://ai.facebook.com/blog/results/open-source/)
Research
[Research Areas](https://ai.facebook.com/research)
Developers
[Developer Tools](https://ai.facebook.com/tools)
Blog
[Read Blog](https://ai.facebook.com/blog)
Careers

[Join Our Team](https://www.facebook.com/careers/jobs?sub_teams[0]=Artificial%20Intelligence)

[ ![49780062_2239882272955938_7957149939224543232_n.png](../_resources/ec998bae8fdaebc996502fa64cf3ab10.png)  ![49661799_326312694636292_7293370538993385472_n.png](../_resources/544005436f43d734b3e9cdfb46eb3ed0.png)](https://www.facebook.com/facebookai)

[(L)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Ffacebookai&h=AT1zOW3TiSnTjd2rUv8VMFR2aSEXJkj3wFvoLFZFAE_DSAxJ7_uVYgCgVU30qZ9ChMCMd1MYdsQGHG0tUD4BPh3fMfoiQYn7V5_pNiIjY2dzM-RFJnDSH5-GryGga8_jI4thBCVawQGSiO2USAKEHvvLBwvgTFdKMoevdpArp1w)

[Privacy Policy](https://www.facebook.com/about/privacy/)
[Terms](https://www.facebook.com/policies/)
[Cookies](https://www.facebook.com/policies/cookies/)
[Create Ad](https://www.facebook.com/ads/create/)
Facebook © 2020