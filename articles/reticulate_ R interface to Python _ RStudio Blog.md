reticulate: R interface to Python | RStudio Blog

# reticulate: R interface to Python

### JJ Allaire

### 2018-03-26

Categories: [Packages](https://blog.rstudio.com/categories/packages)  [R Markdown](https://blog.rstudio.com/categories/r-markdown) Tags: [Packages](https://blog.rstudio.com/tags/packages)  [R Markdown](https://blog.rstudio.com/tags/r-markdown)  [Python](https://blog.rstudio.com/tags/python)  [reticulate](https://blog.rstudio.com/tags/reticulate)

We are pleased to announce the **reticulate** package, a comprehensive set of tools for interoperability between Python and R. The package includes facilities for:

![reticulated_python.png](../_resources/c9a80c134984d5939eda954f5d3a9082.png)

- Calling Python from R in a variety of ways including R Markdown, sourcing Python scripts, importing Python modules, and using Python interactively within an R session.
- Translation between R and Python objects (for example, between R and Pandas data frames, or between R matrices and NumPy arrays).
- Flexible binding to different versions of Python including virtual environments and Conda environments.

Reticulate embeds a Python session within your R session, enabling seamless, high-performance interoperability. If you are an R developer that uses Python for some of your work or a member of data science team that uses both languages, reticulate can dramatically streamline your workflow!

You can install the **reticulate** pacakge from CRAN as follows:

	install.packages("reticulate")

Read on to learn more about the features of reticulate, or see the [reticulate website](https://rstudio.github.io/reticulate) for detailed documentation on using the package.

## Python in R Markdown

The **reticulate** package includes a Python engine for [R Markdown](http://rmarkdown.rstudio.com/) with the following features:

- Run Python chunks in a single Python session embedded within your R session (shared variables/state between Python chunks)
- Printing of Python output, including graphical output from [matplotlib](https://matplotlib.org/).
- Access to objects created within Python chunks from R using the `py` object (e.g. `py$x` would access an `x` variable created within Python from R).
- Access to objects created within R chunks from Python using the `r` object (e.g. `r.x` would access to `x` variable created within R from Python)

Built in conversion for many Python object types is provided, including [NumPy](http://www.numpy.org/) arrays and [Pandas](https://pandas.pydata.org/) data frames. From example, you can use Pandas to read and manipulate data then easily plot the Pandas data frame using [ggplot2](http://ggplot2.org/):

![rmarkdown_engine_zoomed.png](../_resources/38da0074018980670a3d692c9a2eb82e.png)

Note that the reticulate Python engine is enabled by default within R Markdown whenever reticulate is installed.

See the [R Markdown Python Engine](https://rstudio.github.io/reticulate/articles/r_markdown.html) documentation for additional details.

## Importing Python modules

You can use the `import()` function to import any Python module and call it from R. For example, this code imports the Python `os` module and calls the `listdir()` function:

	library(reticulate)
	os <- import("os")
	os$listdir(".")

	 [1] ".git"             ".gitignore"       ".Rbuildignore"    ".RData"
	 [5] ".Rhistory"        ".Rproj.user"      ".travis.yml"      "appveyor.yml"
	 [9] "DESCRIPTION"      "docs"             "external"         "index.html"
	[13] "index.Rmd"        "inst"             "issues"           "LICENSE"
	[17] "man"              "NAMESPACE"        "NEWS.md"          "pkgdown"
	[21] "R"                "README.md"        "reticulate.Rproj" "src"
	[25] "tests"            "vignettes"

Functions and other data within Python modules and classes can be accessed via the `$` operator (analogous to the way you would interact with an R list, environment, or reference class).

Imported Python modules support code completion and inline help:
![reticulate_completion.png](../_resources/cc9c39978d7228db9f7afea9a1018f26.png)

See [Calling Python from R](https://rstudio.github.io/reticulate/articles/calling_python.html) for additional details on interacting with Python objects from within R.

## Sourcing Python scripts

You can source any Python script just as you would source an R script using the `source_python()` function. For example, if you had the following Python script *flights.py*:

	import pandas

	def read_flights(file):
	  flights = pandas.read_csv(file)
	  flights = flights[flights['dest'] == "ORD"]
	  flights = flights[['carrier', 'dep_delay', 'arr_delay']]
	  flights = flights.dropna()
	  return flights

Then you can source the script and call the `read_flights()` function as follows:

	source_python("flights.py")
	flights <- read_flights("flights.csv")

	library(ggplot2)
	ggplot(flights, aes(carrier, arr_delay)) + geom_point() + geom_jitter()

See the [`source_python()`](https://rstudio.github.io/reticulate/reference/source_python.html) documentation for additional details on sourcing Python code.

## Python REPL

If you want to work with Python interactively you can call the `repl_python()` function, which provides a Python REPL embedded within your R session. Objects created within the Python REPL can be accessed from R using the `py` object exported from reticulate. For example:

![python_repl.png](../_resources/b8807768a5700e060c2b8cb7b451831f.png)
Enter `exit` within the Python REPL to return to the R prompt.

Note that Python code can also access objects from within the R session using the `r` object (e.g. `r.flights`). See the [`repl_python()`](https://rstudio.github.io/reticulate/reference/repl_python.html) documentation for additional details on using the embedded Python REPL.

## Type conversions

When calling into Python, R data types are automatically converted to their equivalent Python types. When values are returned from Python to R they are converted back to R types. Types are converted as follows:

R
Python
Examples
Single-element vector
Scalar
[object Object], [object Object], [object Object], [object Object]
Multi-element vector
List
[object Object], [object Object]
List of multiple types
Tuple
[object Object]
Named list
Dict
[object Object], [object Object]
Matrix/Array
NumPy ndarray
[object Object]
Data Frame
Pandas DataFrame
[object Object]
Function
Python function
[object Object]
NULL, TRUE, FALSE
None, True, False
[object Object], [object Object], [object Object]

If a Python object of a custom class is returned then an R reference to that object is returned. You can call methods and access properties of the object just as if it was an instance of an R reference class.

## Learning more

The [reticulate website](https://rstudio.github.io/reticulate/) includes comprehensive documentation on using the package, including the following articles that cover various aspects of using reticulate:

- [Calling Python from R](https://rstudio.github.io/reticulate/articles/calling_python.html) — Describes the various ways to access Python objects from R as well as functions available for more advanced interactions and conversion behavior.
- [R Markdown Python Engine](https://rstudio.github.io/reticulate/articles/r_markdown.html) — Provides details on using Python chunks within R Markdown documents, including how call Python code from R chunks and vice-versa.
- [Python Version Configuration](https://rstudio.github.io/reticulate/articles/versions.html) — Describes facilities for determining which version of Python is used by reticulate within an R session.
- [Installing Python Packages](https://rstudio.github.io/reticulate/articles/python_packages.html) — Documentation on installing Python packages from PyPI or Conda, and managing package installations using virtualenvs and Conda environments.
- [Using reticulate in an R Package](https://rstudio.github.io/reticulate/articles/package.html) — Guidelines and best practices for using reticulate in an R package.
- [Arrays in R and Python](https://rstudio.github.io/reticulate/articles/arrays.html) — Advanced discussion of the differences between arrays in R and Python and the implications for conversion and interoperability.

## Why reticulate?

From the [Wikipedia](https://en.wikipedia.org/wiki/Reticulated_python) article on the reticulated python:

> The reticulated python is a speicies of python found in Southeast Asia. They are the world’s longest snakes and longest reptiles…The specific name, reticulatus, is Latin meaning “net-like”, or reticulated, and is a reference to the complex colour pattern.

From the [Merriam-Webster](https://www.merriam-webster.com/dictionary/reticulate) definition of reticulate:

> 1: resembling a net or network; especially : having veins, fibers, or lines crossing a reticulate leaf. 2: being or involving evolutionary change dependent on genetic recombination involving diverse interbreeding populations.

The package enables you to *reticulate* Python code into R, creating a new breed of project that weaves together the two languages.

 [← DT 0.4: Editing Tables, Smart Filtering, and More](https://blog.rstudio.com/2018/03/29/dt-0-4/) ⊹ [Platform Deprecation Strategy →](https://blog.rstudio.com/2018/03/07/platform-deprecation-strategy/)

### Search

You may subscribe by Email or the [RSS feed](https://blog.rstudio.com/index.xml).

Read our [privacy policy](https://www.rstudio.com/about/privacy-policy/)

### News & Events

Effective Application of the R Language — November 1-3 — Boston, MA [↪](https://earlconf.com/boston/)

rstudio::conf — Jan 31-Feb 1 — San Diego, CA [↪](http://rstudio.com/conference/)

### Categories

- [Arrow](https://blog.rstudio.com/categories/arrow) (1)

- [Featured](https://blog.rstudio.com/categories/featured) (24)

- [News](https://blog.rstudio.com/categories/news) (71)

- [Packages](https://blog.rstudio.com/categories/packages) (144)

- [R Markdown](https://blog.rstudio.com/categories/r-markdown) (15)

- [RStudio Connect](https://blog.rstudio.com/categories/rstudio-connect) (13)

- [RStudio IDE](https://blog.rstudio.com/categories/rstudio-ide) (54)

- [Shiny](https://blog.rstudio.com/categories/shiny) (61)

- [Training](https://blog.rstudio.com/categories/training) (47)

- [news](https://blog.rstudio.com/categories/news) (1)

- [rstudio::conf](https://blog.rstudio.com/categories/rstudioconf) (9)

- [shinyapps.io](https://blog.rstudio.com/categories/shinyapps.io) (10)

- [tidyverse](https://blog.rstudio.com/categories/tidyverse) (34)

### About RStudio

- [RStudio Home](https://www.rstudio.com/)

- [RStudio Support](https://support.rstudio.com/)

- [Contact Us](https://blog.rstudio.com/2018/03/26/reticulate-r-interface-to-python/mailto:info@rstudio.com)