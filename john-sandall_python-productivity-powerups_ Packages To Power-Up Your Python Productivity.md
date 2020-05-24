john-sandall/python-productivity-powerups: Packages To Power-Up Your Python Productivity

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='57'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='808' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/john-sandall/python-productivity-powerups#python-productivity-power-ups)Python Productivity Power-Ups

This was created for the PyDataUK May Talks which you can watch in YouTube here: https://www.youtube.com/watch?v=C1hqHk1SfrA. If you would like to skip to this talk [please use this link](https://youtu.be/C1hqHk1SfrA?t=1851).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='58'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='811' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/john-sandall/python-productivity-powerups#code)Code

You can find the notebook from the presentation here: [Python Productivity Power-Ups](https://github.com/john-sandall/python-productivity-powerups/blob/master/notebooks/Python%20Productivity%20Power-Ups.ipynb)

The packages featured were:
1. tqdm: https://pypi.org/project/tqdm/
2. black: https://pypi.org/project/black/
3. nb-black: https://pypi.org/project/nb-black/
4. isort: https://github.com/timothycrosley/isort
5. logaru: https://github.com/Delgan/loguru
6. joblib: https://joblib.readthedocs.io/en/latest/

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='59'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='822' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/john-sandall/python-productivity-powerups#load-the-environment-using-pip-tools)Load the environment using pip-tools

	# Activate environment
	workon python-productivity-powerups

	# Update packages from requirements.txt
	pip-sync

	# Install new package & update requirements.txt
	pip install new-package-name
	pip freeze  # to check version number

	# copy paste package & version to requirements.in
	pip-compile requirements.in
	pip-sync

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='60'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='824' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/john-sandall/python-productivity-powerups#setup)Setup

	# Install virtualenv
	pip install virtualenv

	# Install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
	pip install virtualenvwrapper
	# Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs by adding following to .zshrc
	zshconfig
	#    # "Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs"
	#    export WORKON_HOME=$HOME/.virtualenvs
	#    export PROJECT_HOME=$HOME/code
	#    source /usr/local/bin/virtualenvwrapper.sh
	source ~/.zshrc
	source /usr/local/bin/virtualenvwrapper.sh
	# Now let's make a virtualenv
	mkvirtualenv venv
	workon venv
	# Commands `workon venv`, `deactivate`, `lsvirtualenv` and `rmvirtualenv` are useful
	# WARNING: When you brew install formulae that provide Python bindings, you should not be in an active virtual environment.
	# (https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md)
	deactivate

	# Create virtualenv & install packasges
	mkvirtualenv numberphile
	pip install python-productivity-powerups
	pip-sync
	python -m ipykernel install --user --name python-productivity-powerups --display-name "Python (python-productivity-powerups)"

* * *

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='61'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='826' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/john-sandall/python-productivity-powerups#license)License

[![68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d6e632d73612f342e302f38387833312e706e67](../_resources/44c7d2e043428bc130a424d81c2caebc.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).