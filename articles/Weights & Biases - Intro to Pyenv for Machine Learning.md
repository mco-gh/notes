Weights & Biases - Intro to Pyenv for Machine Learning

22
Jul
2019
/
Adrian Swanberg, Software Engineer

# Intro to Pyenv for Machine Learning

#### TL;DR

If you’re doing machine learning and tired of python dependency hell, use pyenv!

If you jump between a lot of different machine learning projects, you probably find yourself running something like **pip install -r requirements.txt** quite often. By default, **pip install** puts libraries in your systemwide libraries folder. If one of your projects has requirements that conflicts with another, switching to that project and running **pip install** will effectively break your other project by modifying the systemwide python libraries it needs to run.

Worse yet, many projects haven’t fully moved to python3 yet! So you may find yourself juggling systemwide requirements across python2 and python3.

A lot of folks use docker for this type of workflow issue. You spin up a container from an image that has python2 or python3 tools already installed, and then install your requirements in that container. You then just use a new container for every project. That’s a totally fine way to do things! But using docker means incurring a bit of overhead (especially on mac, where you don’t quite get native performance), and is perhaps overkill for just this use case (assuming you’re mostly just working alone and don’t need to [solve reproducibility for you and your teammates](https://www.wandb.com/articles/towards-reproducibility)).

Instead of configuring a unique docker container for each project, how about a unique python environment? What if you could just run **pip install**, and have the resulting libraries installed somewhere *local* to the project you’re working on?

I’ve been using **pyenv-virtualenv** to accomplish just that. **pyenv** is a utility that manages several python installations and virtual environments for you. **pyenv** can install different versions of python in isolation from each other, *and* create virtual environments for each of your projects. Once a project is associated with a specific virtual environment, running python inside that project resolves to the correct version of python with the correct libraries installed every time.

#### Let’s walk through an example.

First, you’ll want to install pyenv. There are several ways to do this depending on whether you’re running MacOS or Linux (a Windows version exists too, though it may not work exactly as described here), but the simplest way that works in any unix-like OS is to simply run:

> $ curl https://pyenv.run | bash

Assuming your OS already has python installed, running pyenv versions should now show the system python installation.

> $ pyenv versions
> * system

Let’s find a project to work on. As a simple example, I’ll use the starter code for W&B’s [superres benchmark](https://app.wandb.ai/wandb/superres/benchmark).

> $ git clone https://github.com/wandb/superres.git
> Cloning into 'superres'...
> ...
> $ cd superres

All the code in this repo happens to run fine on python3, so let’s now install python3 in pyenv.

>  $ pyenv install 3.6.8
> <Lots of output follows. Should eventually succeed.>
> $ pyenv versions
> * system
>   3.6.8

The output of **pyenv versions** is telling us that pyenv now sees two versions of python: the default system installation you had before pyenv, and version 3.6.8. It’s also saying that system python is the current active version. We can prove this to ourselves by asking pyenv which python binary would run if we were to invoke python right now.

> $ pyenv which python
> /usr/bin/python # or similar
Let’s try switching to python 3.6.8 and running that same command.
> $ pyenv shell 3.6.8
> $ pyenv which python
> $HOME/.pyenv/versions/3.6.8/bin/python

Now we can run python and we know we’ll get version 3.6.8. We’re almost fully set up. Now let’s create a virtualenv for this superres project.

> $ pyenv virtualenv 3.6.8 superres
> <Some output follows.>
> $ pyenv versions
>   system
> * 3.6.8 (set by PYENV_VERSION environment variable)
>   3.6.8/envs/superres
>   superres

It looks like we now have four environments, but don’t worry, superres is just an alias for "3.6.8/envs/superres", so there are actually only three.

#### What did running this virtualenv command actually do?

It basically “forked” (without copying or reinstalling) the installation for version 3.6.8, and created a new subdirectory where we can install packages to the *superres *environment only.

On to the last step: associating this project with our *superres *environment.
> $ pyenv shell --unset # Undoes our previous pyenv shell command.
> $ pyenv local superres

This creates a file in your current directory called .python-version, which contains the name of the environment we want to use whenever we’re in this directory. Let’s test that everything works as expected.

> $ cd ..

> $ pyenv versions # In the previous folder, we should default to system python.

> * system
>   3.6.8
>   3.6.8/envs/superres
>   superres
> $ cd superres
> $ pyenv versions
>   system
>   3.6.8
>   3.6.8/envs/superres
> * superres (set by /superres/.python-version)

Now we can run **pip install -r requirements.txt** and trust that everything will get installed only in the superres environment!

> $ pip install -r requirements.txt
> <Lots of output follows.>

> $ pip show tensorflow # Let's prove to ourselves the installation is really local.

> <...>

> Location: $HOME/.pyenv/versions/3.6.8/envs/superres/lib/python3.6/site-packages

> <...>

You can now repeat the steps starting at **pyenv virtualenv <version> <virtualenv name>** for each project, and your dependencies will never get mixed up again!

# Weights & Biases

We're building lightweight, flexible experiment tracking tools for deep learning. Add a couple of lines to your python script, and we'll keep track of your hyperparameters and output metrics, making it easy to compare runs and see the whole history of your progress. Think of us like GitHub for deep learning.**

**

# Partner Program

We are building our library of deep learning articles, and we're delighted to feature the work of community members. [Contact Carey](https://www.wandb.com/articles/pyenv-for-mlmailto:carey@wandb.com?subject=W%26B%20Partner%20Program) to learn about opportunities to share your research and insights.**

**
[Try our free tools for experiment tracking →](http://app.wandb.ai/)

Contact us at info@wandb.com       [Privacy Policy       ](https://www.wandb.com/privacy)[Terms of Service](https://www.wandb.com/terms)