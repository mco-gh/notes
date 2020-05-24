My Python Development Environment, 2018 Edition « Jacob Kaplan-Moss

# My Python Development Environment, 2018 Edition

##   February 21, 2018

For years I’ve noodled around with various setups for a Python development environment, and never really found something I loved – until now.

My setup pieces together [pyenv](https://github.com/pyenv/pyenv), [pipenv](https://docs.pipenv.org/), and [pipsi](https://github.com/mitsuhiko/pipsi). It’s probably a tad more complex that is ideal for most Python users, but for the things I need, it’s perfect.

## My Requirements

I do have somewhat specific (maybe unusual?) requirements:

- I need to develop against multiple Python versions, including 2.7, various Python 3 versions (3.5 and 3.6, mostly), and PyPy.
- I work on many projects simultaneously, each with different sets of dependencies, so some sort of virtual environment or isolation is critical.
- I use multiple OSes: macOS at work, and Linux (well, Linux-ish - actually it’s[WSL](https://docs.microsoft.com/en-us/windows/wsl/about)) at home.
- I want to avoid using the System-provided Python. On macOS it’s too outdated. On Linux, the system Python is used by the OS itself, so if you hose your Python you can hose your system.
- I use a bunch Python-based CLI stuff, like [youtube-dl](https://rg3.github.io/youtube-dl/), [awscli](https://aws.amazon.com/cli/), [doc2dash](https://doc2dash.readthedocs.io/en/stable/), etc. I want to be able to install and use them without fussing around with activating environments, but I also don’t want their dependencies to clutter up a global installation.
- I deploy stuff mostly to Heroku (personal) and [cloud.gov](https://cloud.gov/) (work). I expect this not to change: I’m spoiled, and never want to manage my own infrastructure again.
- Although Docker meets all these requirements, I don’t really like using it. I find it slow, frustrating, and overkill for my purposes.

## The Setup

### 1. [pyenv](https://github.com/pyenv/pyenv)

**Why?** I need to run multiple Python versions, isolated from the system Python. [pyenv](https://github.com/pyenv/pyenv) makes it easy to install, manage, and switch between those multiple Pythons. As a bonus, [pipenv](https://docs.pipenv.org/) integrates with [pyenv](https://github.com/pyenv/pyenv) and will automatically install missing Python versions if they’re required by aPipfile.

On my Mac, I installed [pyenv](https://github.com/pyenv/pyenv) from Homebrew (brew install pyenv). On Linux, I used the Github installation technique documented in the[installation instructions](https://github.com/pyenv/pyenv#installation), which was easy and went smoothly.

Then, I installed some Python versions:
pyenv install 3.6.4
pyenv install 3.5.4
pyenv install 2.7.14
pyenv install pypy3.5-5.10.0
And made sure my default Python was set to the latest and greatest:
pyenv global 3.6.4

### 2. [pipsi](https://github.com/mitsuhiko/pipsi)

**Why?**  [pipsi](https://github.com/mitsuhiko/pipsi) lets me install Python-based CLI stuff (like [youtube-dl](https://rg3.github.io/youtube-dl/),[awscli](https://aws.amazon.com/cli/), [doc2dash](https://doc2dash.readthedocs.io/en/stable/), etc.) without those projects’ dependencies messing up my global Python.

Normally, installing [pipsi](https://github.com/mitsuhiko/pipsi) is easy:

curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python

However, at the time I’m writing this (late February 2018), this didn’t work for me; I needed to do some tweaking to get it to work. I followed the workarounds documented in issues [#124](https://github.com/mitsuhiko/pipsi/issues/124) and[#125](https://github.com/mitsuhiko/pipsi/issues/125). Hopefully this’ll be fixed shortly.

I didn’t do this, but it might be a good idea to install [pipsi](https://github.com/mitsuhiko/pipsi) using the system Python (i.e. run pyenv local system before running the installer). The downside is that this will use a potentially old-ass Python, but the upside is that you won’t break your [pipsi](https://github.com/mitsuhiko/pipsi) install if you delete a pyenv version (like upon an upgrade).

### 3. [pipenv](https://docs.pipenv.org/)

**Why?**  [pipenv](https://docs.pipenv.org/) handles dependency- and virtual-environment-management in a way that’s very intuitive (to me), and fits perfectly with my desired workflow.

The documentation covers a[few different ways to install pipenv](https://docs.pipenv.org/install/#installing-pipenv). Because I’m already using [pipsi](https://github.com/mitsuhiko/pipsi), I chose the[pipsi-based installation](https://docs.pipenv.org/install/#fancy-installation-of-pipenv):

pipsi install pew
pipsi install pipenv

## What it looks like in use

With this all together, all my use-cases are handled simply:

To start new projects, I just make a directory and type pipenv install ...to start installing my dependencies. Pipenv creates a Pipfile for me, and manages it, and I’m up and running.

To work on existing projects, I clone a repository and either run pipenv install (for projects that already have a Pipfile), or pipenv install -r requirements.txt (which as a side-effect automatically converts a the requirements file to a Pipfile).

If I need to switch Python versions, I run pyenv local <version> in my project directory. I can also add:

[requires]
python_version = "<version>"
to my Pipfile, and pipenv will enforce that version requirement.
When I want to install CLI stuff, I use pipsi:
pipsi install awscli
pipsi install doc2dash

# ... etc

When it comes time to deploy, both Heroku and [cloud.gov](https://cloud.gov/) will read and understand my Pipfile. If I need to deploy to something that doesn’t do Pipfile-based installs, I create a requirements.txt by runningpipenv lock --requirements.