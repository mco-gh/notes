Turn Python Scripts into Beautiful ML Tools

# Turn Python Scripts into Beautiful ML Tools

## Introducing Streamlit, an app framework built for ML engineers

[![2*p1XpZztbSsl7q45ooNneSQ.jpeg](../_resources/f4b96b152b6a66c74fd088123e85fff2.jpg)](https://towardsdatascience.com/@adrien.g.treuille?source=post_page-----ddba3357eace----------------------)

[Adrien Treuille](https://towardsdatascience.com/@adrien.g.treuille?source=post_page-----ddba3357eace----------------------)

[Oct 1](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace?source=post_page-----ddba3357eace----------------------) · 7 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='179'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='180' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

![1*p3XPm-x0TUIuMmQQa4mjHQ.gif](../_resources/f4475f8cf521a4887e731a9932779d66.jpg)
![1*Mbn2SxozueUkGKPW1NJkOw.gif](../_resources/93c74d5e21ef307e195441e5c1cbddd7.gif)

Coding a semantic search engine with real-time neural-net inference in 300 lines of Python.

In my experience, every nontrivial machine learning project is eventually stitched together with bug-ridden and unmaintainable internal tools. These tools — often a patchwork of Jupyter Notebooks and Flask apps — are difficult to deploy, require reasoning about client-server architecture, and don’t integrate well with machine learning constructs like Tensorflow GPU sessions.

I saw this first at Carnegie Mellon, then at Berkeley, Google X, and finally while building autonomous robots at Zoox. These tools were often born as little Jupyter notebooks: the sensor calibration tool, the simulation comparison app, the LIDAR alignment app, the scenario replay tool, and so on.

As a tool grew in importance, project managers stepped in. Processes sprouted. Requirements flowered. These solo projects gestated into scripts, and matured into gangly maintenance nightmares.

![1*5BWfc_oBn2yypksY8-QuKA.png](../_resources/59acac42bdd98b481f87d8bded86a2d6.png)
![1*5BWfc_oBn2yypksY8-QuKA.png](../_resources/b3ff43ec42afca678052b28289f4fb5c.png)
The machine learning engineers’ ad-hoc app building flow.

When a tool became crucial, we **called in the tools team**. They wrote fluent Vue and React. They blinged their laptops with stickers about declarative frameworks. They had a *design process*:

![1*hNO5NYKjcsEV7jIpEaz8Eg.png](../_resources/f00b45ab633f7f852eb1136acc1446b5.png)
![1*hNO5NYKjcsEV7jIpEaz8Eg.png](../_resources/e7f2e26469b28af150220825d58ad34e.png)
The tools team’s clean-slate app building flow.

Which was awesome. But these tools all needed new features, like weekly. And the tools team was supporting ten other projects. They would say, “we’ll update your tool again in two months.”

So we were back to building our own tools, deploying Flask apps, writing HTML, CSS, and JavaScript, and trying to version control everything from notebooks to stylesheets. So my old Google X friend, Thiago Teixeira, and I began thinking about the following question: **What if we could make building tools as easy as writing Python scripts?**

We wanted machine learning engineers to be able to create beautiful apps without needing a tools team. These internal tools should arise as a natural byproduct of the ML workflow. Writing such tools should *feel* like training a neural net or performing an ad-hoc analysis in Jupyter! At the same time, we wanted to preserve all of the flexibility of a powerful app framework. We wanted to create beautiful, performant tools that engineers could show off. Basically, we wanted this:

![1*gdD55KRcRVRvfjsQ_Ls-XA.png](../_resources/77299475d1a000f00a8ecc61683a3f69.png)
![1*gdD55KRcRVRvfjsQ_Ls-XA.png](../_resources/d078fce8af76aa09bdf9334264f8cfff.png)
The Streamlit app building flow.

With an amazing beta community including engineers from Uber, Twitter, Stitch Fix, and Dropbox, we worked for a year to create [Streamlit](https://streamlit.io/), a [completely free and open source](https://github.com/streamlit/streamlit/) app framework for ML engineers. With each prototype, the core principles of Streamlit became simpler and purer. They are:

**#1: Embrace Python scripting.** Streamlit apps are really just scripts that run from top to bottom. There’s no hidden state. You can factor your code with function calls. If you know how to write Python scripts, you can write Streamlit apps. For example, this is how you write to the screen:

import streamlit as stst.write('Hello, world!')
![1*VNqEOqFJQl5fB7Z0ed5lMw.png](../_resources/c52557fa9625d8bd66f685cd867af544.png)
![1*VNqEOqFJQl5fB7Z0ed5lMw.png](../_resources/2dfded9d8aa35e0672169e19872cf1cf.png)
Nice to meet you.

**#2: Treat widgets as variables. **There are *no callbacks in Streamlit*! Every interaction simply reruns the script from top to bottom. This approach leads to really clean code:

import streamlit as stx = st.slider('x')
st.write(x, 'squared is', x * x)
![1*h8BwonRrhnh3KtjO5cDEcA.png](../_resources/a7e6cb46b4593c846ab30e47568d29df.png)
![1*h8BwonRrhnh3KtjO5cDEcA.png](../_resources/86f34ef58ebccefc2aa109a01db6aa91.png)
An interactive Streamlit app in three lines of code.

**#3: Reuse data and computation. **What if you download lots of data or perform complex computation? The key is to *safely reuse* information across runs. Streamlit introduces a cache primitive that behaves like a persistent, immutable-by-default, data store that lets Streamlit apps safely and effortlessly reuse information. For example, this code** downloads data only once** from the [Udacity Self-driving car project](https://github.com/udacity/self-driving-car), yielding a simple, fast app:

|     |     |
| --- | --- |
| 1   | import streamlit as st |
| 2   | import pandas as pd |
| 3   |     |
| 4   | # Reuse this data across runs! |
| 5   | read_and_cache_csv = st.cache(pd.read_csv) |
| 6   |     |
| 7   | BUCKET  =  "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/" |
| 8   | data = read_and_cache_csv(BUCKET  +  "labels.csv.gz", nrows=1000) |
| 9   | desired_label = st.selectbox('Filter to:', ['car', 'truck']) |
| 10  | st.write(data[data.label == desired_label]) |

 [view raw](https://gist.github.com/treuille/c633dc8bc86efaa98eb8abe76478aa81/raw/2019640b6a9ff5da5ab6d5b11b3345ddc764b285/cache_example.py)  [cache_example.py](https://gist.github.com/treuille/c633dc8bc86efaa98eb8abe76478aa81#file-cache_example-py) hosted with ❤ by [GitHub](https://github.com/)

Using st.cache to persist data across Streamlit runs. To run this code, please [follow these instructions](https://gist.github.com/treuille/c633dc8bc86efaa98eb8abe76478aa81#gistcomment-3041475).

![1*vLvk0xZUVEx1GcrzYhWxXQ.png](../_resources/2b1fcb87dfd0e56dff33307d68149eb6.png)
![1*vLvk0xZUVEx1GcrzYhWxXQ.png](../_resources/5a8820a6fd9e42a2fea9927462cf2cf8.png)
The output of running the st.cache example above.
In short, Streamlit works like this:
1. The entire script is run from scratch for each user interaction.
2. Streamlit assigns each variable an up-to-date value given widget states.
3. Caching allows Streamlit to skip redundant data fetches and computation.
Or in pictures:
![1*l4gxFYEZnRhysQ_QWIVJgA.png](../_resources/626e0181486758f39d0e8293b290f6a6.png)
![1*l4gxFYEZnRhysQ_QWIVJgA.png](../_resources/ea3c00bad7de1ac56628a95f7b78d9e6.png)

User events trigger Streamlit to rerun the script from scratch. Only the cache persists across runs.

If this sounds intriguing, you can try it right now! Just run:
$ pip install --upgrade streamlit

$ streamlit hello** You can now view your Streamlit app in your browser.**  **Local URL:**  [http://localhost:8501](http://localhost:8501/)

 **Network URL:**  [http://10.0.1.29:8501](http://10.0.1.29:8501/)

This will automatically pop open a web browser pointing to your local Streamlit app. If not, just click the link.

![1*_Btm7O0pYqAk_enXUPECLw.png](../_resources/edecd1df8345e827105d151d6abfab79.png)
![1*_Btm7O0pYqAk_enXUPECLw.png](../_resources/41de32945b70f463438626934c3e7049.png)

To see more examples like this fractal animation, run **streamlit hello** from the command line.

* * *

*...*
Ok. Are you back from playing with fractals? Those can be mesmerizing.

The simplicity of these ideas does not prevent you from creating incredibly rich and useful apps with Streamlit. During my time at Zoox and Google X, I watched as self-driving car projects ballooned into gigabytes of visual data, which needed to be searched and understood, including running models on images to compare performance. Every self-driving car project I’ve seen eventually has had entire teams working on this tooling.

Building such a tool in Streamlit is easy. [This Streamlit demo](http://github.com/streamlit/demo-self-driving) lets you perform semantic search across the entire [Udacity self-driving car photo dataset](https://github.com/udacity/self-driving-car), visualize human-annotated ground truth labels, and **run a complete neural net (**[**YOLO**](https://pjreddie.com/darknet/yolo/)**) in real time **from within the app [1].

![1*Mbn2SxozueUkGKPW1NJkOw.gif](../_resources/e48e59754fd456aed6d98d137cd36b34.jpg)
![1*p3XPm-x0TUIuMmQQa4mjHQ.gif](../_resources/207eacf298f38250fc29565bed9d2bd7.gif)

This 300-line Streamlit demo combines semantic visual search with interactive neural net inference.

The whole app is a completely self-contained, 300-line Python script, most of which is machine learning code. In fact, there are [only 23 Streamlit calls in the whole app](https://github.com/streamlit/demo-self-driving/blob/master/app.py). You can run it yourself right now!

$ pip install --upgrade streamlit opencv-python
$ streamlit run
https://raw.githubusercontent.com/streamlit/demo-self-driving/master/app.py

* * *

*...*

As we worked with machine learning teams on their own projects, we came to realize that these simple ideas yield a number of important benefits:

**Streamlit apps are pure Python files. **So you can use your favorite editor and debugger with Streamlit.

![1*4KMALKoeS_3TUSBn0ryzYg.png](../_resources/3cc75796baf3ea7cf5958c9f1f0ccb13.png)
![1*4KMALKoeS_3TUSBn0ryzYg.png](../_resources/e0a3002caa1e4bfdd3512067d2bcb362.png)

My favorite layout for writing Streamlit apps has VSCode on the left and Chrome on the right.

**Pure Python scripts work seamlessly with Git** and other source control software, including commits, pull requests, issues, and comments. Because Streamlit’s underlying language is pure Python, you get all the benefits of these amazing collaboration tools for free .

![0*pY7e7BLPI2atT_-V](../_resources/b20df46d0be92b59fbbaf2b7881f684f.png)
![0*pY7e7BLPI2atT_-V](../_resources/f9b80f38638733921e5d21821707c1d9.png)

Because Streamlit apps are just Python scripts, you can easily version control them with Git.

**Streamlit provides an immediate-mode live coding environment.** Just click *Always rerun* when Streamlit detects a source file change.

![1*P3vtLk-HGeCRH_Gu5B5ifg.png](../_resources/0b72acbd1891a38493cd3faea9c1e909.png)
![1*P3vtLk-HGeCRH_Gu5B5ifg.png](../_resources/1a9db21bcd28f2b5ae8abf330ef7ad08.png)
Click “Always rerun” to enable live coding.

**Caching simplifies setting up computation pipelines. **Amazingly, chaining cached functions automatically creates efficient computation pipelines! Consider [this code](https://gist.github.com/treuille/ac7755eb37c63a78fac7dfef89f3517e) adapted from our [Udacity demo](https://github.com/streamlit/demo-self-driving):

|     |     |
| --- | --- |
| 1   | import streamlit as st |
| 2   | import pandas as pd |
| 3   |     |
| 4   | @st.cache |
| 5   | def  load_metadata(): |
| 6   |  DATA_URL  =  "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz" |
| 7   |  return pd.read_csv(DATA_URL, nrows=1000) |
| 8   |     |
| 9   | @st.cache |
| 10  | def  create_summary(metadata, summary_type): |
| 11  | one_hot_encoded = pd.get_dummies(metadata[["frame", "label"]], columns=["label"]) |
| 12  |  return  getattr(one_hot_encoded.groupby(["frame"]), summary_type)() |
| 13  |     |
| 14  | # Piping one st.cache function into another forms a computation DAG. |
| 15  | summary_type = st.selectbox("Type of summary:", ["sum", "any"]) |
| 16  | metadata = load_metadata() |
| 17  | summary = create_summary(metadata, summary_type) |
| 18  | st.write('## Metadata', metadata, '## Summary', summary) |

 [view raw](https://gist.github.com/treuille/ac7755eb37c63a78fac7dfef89f3517e/raw/568cc2d190c2f96b2a8a7aaf6fa444d68bde630e/caching_DAG_example.py)  [caching_DAG_example.py](https://gist.github.com/treuille/ac7755eb37c63a78fac7dfef89f3517e#file-caching_dag_example-py) hosted with ❤ by [GitHub](https://github.com/)

A simple computation pipeline in Streamlit. To run this code, please [follow these instructions](https://gist.github.com/treuille/ac7755eb37c63a78fac7dfef89f3517e#gistcomment-3041436).

Basically, the pipeline is load_metadata → create_summary. Every time the script is run **Streamlit only recomputes whatever subset of the pipeline is required to get the right answer**. Cool!

![1*e0-z12L0pXYlCE5OM3n6LA.png](../_resources/377e50ab4cf70d851f97f13f9f3c93d0.png)
![1*e0-z12L0pXYlCE5OM3n6LA.png](../_resources/ed90d389327556740d2dffc2ba425b96.png)

To make apps performant, Streamlit only recomputes whatever is necessary to update the UI.

**Streamlit is built for GPUs. **Streamlit allows direct access to machine-level primitives like TensorFlow and PyTorch and complements these libraries. For example in this demo, Streamlit’s cache stores the entire [NVIDIA celebrity face GAN](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of) [2]. This approach enables nearly instantaneous inference as the user updates sliders.

![1*188SkUE1onGcpQIuSZsiMQ.gif](../_resources/f6efd6a930909908887c6d7cac4ba26b.jpg)
![1*188SkUE1onGcpQIuSZsiMQ.gif](../_resources/4e14ad510088b54615cdb7cb20c2099c.gif)

This Streamlit app demonstrates [NVIDIA celebrity face GAN](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of) [2] model using [Shaobo Guan’s TL-GAN](https://blog.insightdatascience.com/generating-custom-photo-realistic-faces-using-ai-d170b1b59255) [3].

**Streamlit is a free and open-source library rather than a proprietary web app**. You can serve Streamlit apps on-prem without contacting us. You can even run Streamlit locally on a laptop without an Internet connection! Furthermore, existing projects can adopt Streamlit incrementally.

![1*nyOMWYNcM9mPTU5mHf1CxQ.png](../_resources/c80400e2c026eb203d1b67be1c30c8a8.png)
![1*nyOMWYNcM9mPTU5mHf1CxQ.png](../_resources/a31b16fb4e11f0edfec0e6c336a68278.png)

Several ways incrementally adopt Streamlit. (Icons courtesy of [fullvector / Freepik](https://www.freepik.com/free-vector/computer-technology-isometric-icon-server-room-digital-device-set-element-design-pc-laptop_4103157.htm).)

* * *

*...*

This just scratches the surface of what you can do with Streamlit. One of the most exciting aspects of Streamlit is how these primitives can be easily composed into complex apps that look like scripts. There’s a lot more we could say about how our architecture works and the features we have planned, but we’ll save that for future posts.

![1*wmwwsWkOHzsYLe8pB2RzBA.png](../_resources/13bb05ce7c4e1f90c9ca844e50e11942.png)
![1*wmwwsWkOHzsYLe8pB2RzBA.png](../_resources/63794575c702631cdac92eb4cee92b6c.png)
*Block diagram of Streamlit’s components. More coming soon!*

We’re excited to finally share Streamlit with the community today and see what you all build with it. We hope that you’ll find it easy and delightful to turn your Python scripts into beautiful ML apps.

* * *

*...*

*Thanks to Amanda Kelly, Thiago Teixeira, TC Ricks, Seth Weidman, Regan Carey, Beverly Treuille, Geneviève Wachtell, and Barney Pell for their helpful input on this article.*

**References:**

[1] J. Redmon and A. Farhadi, *YOLOv3: An Incremental Improvement *(2018), arXiv.

[2] T. Karras, T. Aila, S. Laine, and J. Lehtinen, *Progressive Growing of GANs for Improved Quality, Stability, and Variation* (2018), ICLR.

[3] S. Guan, *Controlled image synthesis and editing using a novel TL-GAN model *(2018), Insight Data Science Blog.