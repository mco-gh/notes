nbinteract

# nbinteract[¶](https://www.nbinteract.com/index.html#nbinteract)

`nbinteract` is a Python package that provides a command-line tool to generate interactive web pages from Jupyter notebooks. It allows [Jupyter widgets](https://github.com/jupyter-widgets/ipywidgets/) to remain interactive even when the notebook is converted to static HTML by using [Binder servers](http://mybinder.org/) as the computational backend.

`nbinteract` also provides Python functions for simple, interactive plots. These interactions are driven by data, not callbacks, allowing authors to focus on the logic of their programs.

`nbinteract` is useful for:

- Data scientists that want to create simple interactive blog posts without having to know / work with Javascript.
- Instructors that want to include interactive examples in their textbooks.
- Students that want to publish data analysis that contains interactive demos.

## Converting Notebooks[¶](https://www.nbinteract.com/index.html#Converting-Notebooks)

From the command line:

*# Run on the command line to convert the notebook into a publishable HTML page.**#**# nbinteract {NOTEBOOK.ipynb} -s {BINDER_SPEC}**#**# Replace {BINDER_SPEC} with a Binder spec in the format**# {username}/{repo}/{branch} (e.g. SamLau95/nbinteract-image/master).**# The branch is optional; if omitted, defaults to `master`**#**# Replace {NOTEBOOK.ipynb} with the name of the notebook file to convert.**#**# For example:*nbinteract homepage.ipynb -s SamLau95/nbinteract-image

After initializing a GitHub repo and running `nbinteract init`, you may omit the Binder spec and simply write:

nbinteract homepage.ipynb

For more information on Binder specs and conversion, see the [tutorial](https://www.nbinteract.com/tutorial/tutorial_intro.html) which has a complete walkthrough on publishing a notebook to the web.

## Plotting[¶](https://www.nbinteract.com/index.html#Plotting)

Most plotting functions from other libraries (e.g. `matplotlib`) take data as input. `nbinteract`'s plotting methods instead take in functions that return data.

In the example below, the `normal` function generates data that we then plot using `nbi.hist()`.

import  numpy  as  npimport  nbinteract  as  nbidef  normal(mean,  sd):  '''Returns 1000 points drawn at random fron N(mean, sd)'''  return  np.random.normal(mean,  sd,  1000)normal(10,  1.0)

array([11.10032294, 8.01737258, 8.84975049, ..., 9.86721442,
11.06511688, 10.88371858])

*# Plot aesthetics*options  =  {  'xlim':  (-2,  12),  'ylim':  (0,  0.7),  'bins':  20}*# Pass in the `normal` function and let user change mean and sd.**# Whenever the user interacts with the sliders, the `normal` function**# is called and the returned data are plotted.*nbi.hist(normal,  mean=(0,  10),  sd=(0,  2.0),  options=options)*# Clicking the Show widget button below loads all widgets on the page.**# Widgets will automatically load for all subsequent pages until you close**# the tab/window.*

Simulations are easy to create using `nbinteract`. In this simulation, we roll a die and plot the running average of the rolls. We can see that with more rolls, the average gets closer to the expected value: 3.5.

rolls  =  np.random.choice([1,  2,  3,  4,  5,  6],  size=300)averages  =  np.cumsum(rolls)  /  np.arange(1,  301)def  x_vals(num_rolls):  return  range(num_rolls)*# The function to generate y-values gets called with the**# x-values as its first argument.*def  y_vals(xs):  return  averages[:len(xs)]

nbi.line(x_vals,  y_vals,  num_rolls=(1,  300))

## Installation[¶](https://www.nbinteract.com/index.html#Installation)

Using `pip`:

pip install nbinteract*# The next two lines can be skipped for notebook version 5.3 and above*jupyter nbextension enable --py --sys-prefix widgetsnbextension

jupyter nbextension enable --py --sys-prefix bqplot

You may now import the `nbinteract` package in Python code and use the `nbinteract` CLI command to convert notebooks to HTML pages.

## Documentation[¶](https://www.nbinteract.com/index.html#Documentation)

Access the tutorials, examples, and documentation for `nbinteract` using the links in the sidebar.

## Feedback[¶](https://www.nbinteract.com/index.html#Feedback)

If you have any questions or comments, send us a message on the [Gitter channel](https://gitter.im/nbinteract/Lobby/). We appreciate your feedback!