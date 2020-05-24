Programming with Python

   [![](../_resources/986a472f401451e5f26bd55d46f9f633.png)](https://software-carpentry.org/)  [Home](http://swcarpentry.github.io/python-novice-inflammation/index.html)

- [Code of Conduct](http://swcarpentry.github.io/python-novice-inflammation/CODE_OF_CONDUCT.html)

- [Setup](http://swcarpentry.github.io/python-novice-inflammation/setup/)

- [Episodes](http://swcarpentry.github.io/python-novice-inflammation/)

- [Extras](http://swcarpentry.github.io/python-novice-inflammation/)

- [License](http://swcarpentry.github.io/python-novice-inflammation/LICENSE.html)
- [Improve this page ✏](https://github.com/swcarpentry/python-novice-inflammation/edit/gh-pages/index.md)

# [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/index.html)

The best way to learn how to program is to do something useful, so this introduction to Python is built around a common scientific task:**data analysis**.

### Arthritis Inflammation

We are studying **inflammation in patients** who have been given a new treatment for arthritis, and need to analyze the first dozen data sets of their daily inflammation. The data sets are stored in[comma-separated values](http://swcarpentry.github.io/python-novice-inflammation/reference/#comma-separated-values) (CSV) format:

- each row holds information for a single patient,

- columns represent successive days.

The first three rows of our first file look like this:
Code

	0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
	0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
	0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1

So, we want to:

1. Calculate the average inflammation per day across all patients.

2. Plot the result to discuss and share with colleagues.
To do all that, we’ll have to learn a little bit about programming.
>

## > > Prerequisites

>

> You need to understand the concepts of **> files**>  and **> directories**>  and how to start a Python interpreter before tackling this lesson. This lesson sometimes references Jupyter Notebook although you can use any Python interpreter mentioned in the > [> Setup](http://swcarpentry.github.io/python-novice-inflammation/setup/)> .

>
> The commands in this lesson pertain to **> Python 3**> .

### Getting Started

To get started, follow the directions on the “[Setup](http://swcarpentry.github.io/python-novice-inflammation/setup/)” page to download data and install a Python interpreter.

## Schedule

|     |     |     |
| --- | --- | --- |
|     | [Setup](http://swcarpentry.github.io/python-novice-inflammation/setup/) | Download files required for the lesson |
| 00:00 | 1. [Analyzing Patient Data](http://swcarpentry.github.io/python-novice-inflammation/01-numpy/index.html) | How can I process tabular data files in Python? |
| 01:30 | 2. [Repeating Actions with Loops](http://swcarpentry.github.io/python-novice-inflammation/02-loop/index.html) | How can I do the same operations on many different values? |
| 02:00 | 3. [Storing Multiple Values in Lists](http://swcarpentry.github.io/python-novice-inflammation/03-lists/index.html) | How can I store many values together? |
| 02:30 | 4. [Analyzing Data from Multiple Files](http://swcarpentry.github.io/python-novice-inflammation/04-files/index.html) | How can I do the same operations on many different files? |
| 02:50 | 5. [Making Choices](http://swcarpentry.github.io/python-novice-inflammation/05-cond/index.html) | How can my programs do different things based on data values? |
| 03:20 | 6. [Creating Functions](http://swcarpentry.github.io/python-novice-inflammation/06-func/index.html) | How can I define new functions?<br>What’s the difference between defining and calling a function?<br>What happens when I call a function? |
| 03:50 | 7. [Errors and Exceptions](http://swcarpentry.github.io/python-novice-inflammation/07-errors/index.html) | How does Python report errors?<br>How can I handle errors in Python programs? |
| 04:20 | 8. [Defensive Programming](http://swcarpentry.github.io/python-novice-inflammation/08-defensive/index.html) | How can I make my programs more reliable? |
| 04:50 | 9. [Debugging](http://swcarpentry.github.io/python-novice-inflammation/09-debugging/index.html) | How can I debug my program? |
| 05:20 | 10. [Command-Line Programs](http://swcarpentry.github.io/python-novice-inflammation/10-cmdline/index.html) | How can I write Python programs that will work like Unix command-line tools? |
| 05:50 | Finish |     |

The actual schedule may vary slightly depending on the topics and exercises chosen by the instructor.

Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) 2018–2019 by [The Carpentries](https://carpentries.org/)

Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) 2016–2018 by [Software Carpentry Foundation](https://software-carpentry.org/)

[Edit on GitHub](https://github.com/swcarpentry/python-novice-inflammation/edit/gh-pages/index.md)/[Contributing](https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/CONTRIBUTING.md)/[Source](https://github.com/swcarpentry/python-novice-inflammation/)/[Cite](https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/CITATION)/[Contact](http://swcarpentry.github.io/python-novice-inflammation/index.htmlmailto:team@carpentries.org)

Using [The Carpentries style](https://github.com/carpentries/styles/) version [9.5.3](https://github.com/carpentries/styles/releases/tag/v9.5.3).