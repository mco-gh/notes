amueller/word_cloud

[![Build Status](../_resources/64f1b7ce47060cdfca7ac94338e92294.png)](https://travis-ci.org/amueller/word_cloud)[[licence](../_resources/d86a5391b195dac6a3ddd15a2a70188f.bin)](https://github.com/amueller/word_cloud/blob/master/LICENSE)[[DOI](../_resources/990308b08003c7cdf87327097f8ab7a4.bin)](https://zenodo.org/badge/latestdoi/21369/amueller/word_cloud)

# [(L)](https://github.com/amueller/word_cloud#word_cloud)word_cloud

A little word cloud generator in Python. Read more about it on the [blog post](http://peekaboo-vision.blogspot.de/2012/11/a-wordcloud-in-python.html) or the [website](http://amueller.github.io/word_cloud/). The code is Python 2, but Python 3 compatible.

## [(L)](https://github.com/amueller/word_cloud#installation)Installation

Fast install:

	pip install wordcloud

If you are using conda, it might be even easier to use anaconda cloud:

	conda install -c https://conda.anaconda.org/amueller wordcloud

For a manual install get this package:

	wget https://github.com/amueller/word_cloud/archive/master.zip
	unzip master.zip
	rm master.zip
	cd word_cloud-master

Install the package:

	python setup.py install

#### [(L)](https://github.com/amueller/word_cloud#installation-notes)Installation notes

##### [(L)](https://github.com/amueller/word_cloud#windows)Windows

If you're having trouble with pip installation on windows, you can find a .whl file at:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

##### [(L)](https://github.com/amueller/word_cloud#ubuntu)Ubuntu

If the installation of the package fails, due to a missing ` pyconfig.h ` file, you need to install the python-dev package.

For Python 2.*

	sudo apt-get install python-dev

For Python 3.*

	sudo apt-get install python3-dev

## [(L)](https://github.com/amueller/word_cloud#examples)Examples

Check out [examples/simple.py](https://github.com/amueller/word_cloud/blob/master/examples/simple.py) for a short intro. A sample output is:

[![Constitution](../_resources/ad9f01bf9c1b3b486cf05ded70b81f7a.png)](https://github.com/amueller/word_cloud/blob/master/examples/constitution.png)

Or run [examples/masked.py](https://github.com/amueller/word_cloud/blob/master/examples/masked.py) to see more options. A sample output is:

[![Alice in Wonderland](../_resources/56acc4ec085ba37f708561a7743d76f5.png)](https://github.com/amueller/word_cloud/blob/master/examples/alice.png)

Getting fancy with some colors:[![Parrot with rainbow colors](../_resources/a2b4e3115d0f051c9c4e68f399bac705.png)](https://github.com/amueller/word_cloud/blob/master/examples/parrot.png)

## [(L)](https://github.com/amueller/word_cloud#command-line-usage)Command-line usage

The ` wordcloud_cli.py ` tool can be used to generate word clouds directly from the command-line:

	$ wordcloud_cli.py --text mytext.txt --imagefile wordcloud.png

If you're dealing with PDF files, then ` pdftotext `, included by default with many Linux distribution, comes in handy:

	$ pdftotext mydocument.pdf - | wordcloud_cli.py --imagefile wordcloud.png

In the previous example, the ` - ` argument orders ` pdftotext ` to write the resulting text to stdout, which is then piped to the stdin of ` wordcloud_cli.py `.

Use ` wordcloud_cli.py --help ` so see all available options.

## [(L)](https://github.com/amueller/word_cloud#used-in)Used in

### [(L)](https://github.com/amueller/word_cloud#reddit-cloud)Reddit Cloud

[Reddit Cloud](https://github.com/amueller/reddit-cloud) is a Reddit bot which generates word clouds for comments in submissions and user histories. You can see it being operated on[/u/WordCloudBot2](http://www.reddit.com/user/WordCloudBot2) ([top posting](http://www.reddit.com/user/WordCloudBot2/?sort=top)).

[![A Reddit Cloud sample](../_resources/055e8a62d3f073e6e9dfb3378a4ad728.png)](https://camo.githubusercontent.com/e7a55193fe612dd34579c61c71937712b54bcb63/687474703a2f2f692e696d6775722e636f6d2f7463625a6e4b572e706e67)

### [(L)](https://github.com/amueller/word_cloud#chat-stats-twitchtv)Chat Stats (Twitch.tv)

[Chat Stats](https://github.com/popcorncolonel/Chat_stats) is a visualization program for Twitch streams, which generates word clouds for comments made by Twitch users in the chat. It also creates various charts and graphs pertaining to concurrent viewership and chat rate over time.

[![Chat Stats Sample](../_resources/fa71a63ea522ddfb572c1778ee4db1c0.png)](https://camo.githubusercontent.com/db08a05e4a2eac646ceb62169b471d9c772d1aa3/687474703a2f2f692e696d6775722e636f6d2f7842637a6b30782e706e67)

### [(L)](https://github.com/amueller/word_cloud#twitter-word-cloud-bot)Twitter Word Cloud Bot

[Twitter Word Cloud Bot](https://github.com/defacto133/twitter-wordcloud-bot) is a twitter bot which generates word clouds for twitter users when it is mentioned with a particular hashtag.[Here](https://twitter.com/wordnuvola) you can see it in action, while [here](http://defacto133.imgur.com/all/)you can see all the word clouds generated so far.

### [(L)](https://github.com/amueller/word_cloud#other)[other]

*Send a pull request to add yours here.*

## [(L)](https://github.com/amueller/word_cloud#issues)Issues

Using Pillow instead of PIL might might get you the [` TypeError: 'int' object is not iterable ` problem](http://peekaboo-vision.blogspot.de/2012/11/a-wordcloud-in-python.html#bc_0_28B) also showcased on the blog.

## [(L)](https://github.com/amueller/word_cloud#licensing)Licensing

The wordcloud library is MIT licenced, but contains DroidSansMono.ttf, a true type font by Google, that is apache licensed. The font is by no means integral, and any other font can be used by setting the ` font_path ` variable when creating a ` WordCloud ` object.