Binder: an awesome tool for hosting Jupyter notebooks - Julia Evans

# Binder: an awesome tool for hosting Jupyter notebooks

Thanks to a [pull request](https://github.com/jvns/pandas-cookbook/pull/62) today, I learned about a thing called Binder!! https://mybinder.org/.

Binder is a tool that lets other people easily launch an interactive copy of your Jupyter notebooks. I am SO STOKED that this exists, I have wanted it forever.

Here’s my [pandas cookbook on Binder](https://mybinder.org/v2/gh/jvns/pandas-cookbook/master). You’ll need to wait for it to load and click ‘cookbook’ to try it out.

### what’s a Jupyter notebook?

Jupyter notebooks (formerly called IPython notebooks) are an awesome way to combine code and text and images into an interactive document. I especially love them for doing data analysis – it’s basically life changing.

Here’s an [example notebook analyzing some Montreal bike path data I made in 2013](https://nbviewer.jupyter.org/github/jvns/talks/blob/master/2013-04-mtlpy/pistes-cyclables.ipynb). You can see both the code, some explanations, and the output of the code all in one place!!

### jupyter notebooks are easy to share online

If you want to share a Jupyter notebook on the internet, it’s super super easy (I just did it above!). There are at least 2 different services you can use (github and nbviewer)

- post a link to it on GitHub https://github.com/jvns/talks/blob/master/2013-04-mtlpy/pistes-cyclables.ipynb. Github has a built-in renderer for jupyter notebooks which is GREAT.
- Put it on GitHub and use [https://nbviewer.jupyter.org](https://nbviewer.jupyter.org/) to share it https://nbviewer.jupyter.org/github/jvns/talks/blob/master/2013-04-mtlpy/pistes-cyclables.ipynb

nbviewer and github have both done this for a long time. This is great. But nbviewer isn’t interactive – it shows you a read-only version. So you can’t edit the code and experiment!

### sharing interactive copies is important!

I used to occasionally run free Python intro data science workshops: we’d install pandas + the Jupyter notebook, do some fun data analysis, learn the basics. Here’s how it would go:

1. write a bunch of materials before the workshop
2. try to write really good installation instructions in advance
3. go to the workshop. Someone is running Windows and I didn’t prepare for that
4. struggle through installation with everyone and mostly survive

Having to install a bunch of software really sucks when you’re trying to get started with a new thing. And getting the scientific Python stack set up can be a pain (though tools like Anaconda definitely made it a lot easier)

Today there’s actually software designed for exactly this use case – you can set up[JupyterHub](https://jupyterhub.readthedocs.io/en/latest/) on a server and have your workshop attendees sign into it. This didn’t exist when I was running workshops but it exists now and it looks awesome. You still need to set up the server which is nontrivial but that seems way better than supporting 30 people through installation issues.

### binder = amazing

[Binder](https://mybinder.org/) lets you easily host interactive Jupyter notebooks and let anyone on the internet use them interactively immediately! It uses JupyterHub under the hood.

If you want to try it out, you can do that right now:

1. Go to https://mybinder.org/v2/gh/jvns/pandas-cookbook/master (which will launch the github.com/jvns/pandas-cookbook repository)

2. Wait for it to build and click ‘launch’

3. click ‘cookbook’, click a notebook, and play around! There’s an “A quick tour of the IPython Notebook” notebook which shows off some of the basic features.

It apparently uses Kubernetes + Docker under the hood which is interesting! It must be much much more expensive to run than the read-only services, but it’s such a useful and cool thing! I hope it continues to exist.

There’s also the [colaboratory](https://colab.research.google.com/) by Google which is kinda the same thing, but it doesn’t work with github and only supports Chrome so it is less exciting to me. But still cool!

Want a weekly digest of these blog posts?

[Tweet](https://twitter.com/share)

[«Operating a Kubernetes network](https://jvns.ca/blog/2017/10/10/operating-a-kubernetes-network/)[»Glitch: write fun small web projects instantly](https://jvns.ca/blog/2017/11/13/glitch--write-small-web-projects-easily/)