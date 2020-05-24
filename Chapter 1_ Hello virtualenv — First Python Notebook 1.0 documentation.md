Chapter 1: Hello virtualenv — First Python Notebook 1.0 documentation

# Chapter 1: Hello virtualenv

The [virtualenv environment manager](http://www.virtualenv.org/en/latest/) makes it possible to create an isolated corner of your computer where all the Python tools you use to build an application are sealed off.

Why do you need this?

By developing each of your Python projects inside a separate virtual environment, you can:You can:

- Juggle different versions of the same Python libraries without a conflict.
- Easily install your project on another machine, as can your colleagues
- Quickly copy your code to a server that publishes pages on the Internet.

For those reasons, virtualenv has become one of the most popular ways to manage Python projects. Alternatives include its more complex cousins [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) and [conda](https://conda.io/docs/index.html).

Note

All that said, working within a virtual environment is not required. At first, it might even feel like a hassle. But in the long run, you will be glad you did it. And you don’t have to take my word for it, you can read discussions on [StackOverflow](https://conda.io/docs/index.html) and [Reddit](https://www.reddit.com/r/Python/comments/2qq1d9/should_i_always_use_virtualenv/).

Learn how to create your first virtualenv by following this video or the written instructions below.

[Hello virtualenv [SCREENCAST]](https://www.youtube.com/watch?v=t1vJzFbmfv8)

## Create a code directory to store all your work

Before we create your first virtualenv, the first step is to create a common folder where all you of your projects will be stored starting with this one.

Open your [command-line interface](http://www.firstpythonnotebook.org/prerequisites/cli.html), which will start you off in your home directory. Enter the following command and press enter to see all of the folders there now.

ls

Next use the [mkdir](https://en.wikipedia.org/wiki/Mkdir) to create a new directory for your code. In the same style as the Desktop, Documents and Downloads folders included by most operating system, we will name this folder Code.

mkdir Code

To verify it’s worked, you can open in your file explorer and navigate to your home folder.

## Create a virtualenv to store this project

Next use your terminal to navigate into the new directory with the [cd](https://en.wikipedia.org/wiki/Cd_(command)) command.

cd Code

Now use the virtualenv command to create a new virtual environment. This is a one time thing necessary to initialize a new environment.

virtualenv first-python-notebook

If you inspect the new directory this command created in your file explorer, you will see that it has generated a set of folders inside. They are the basic tools that make the virtual environment work and include a complete copy of the Python programming language just for this project.

## Activate the virtualenv

Now use cd jump into the directory that was created created.
cd first-python-notebook

Now the trickiest part. Each time you want to begin working on a virtualenv project, you need to start off by “activating” it inside your terminal.

The activation program is called activate. It was created inside the new folders in this directory. You will need to run it each and every time you start work in this environment.

On Mac OSX the program is inside a folder called bin. You can easily run it from your terminal by using the [source](https://en.wikipedia.org/wiki/Source_(command)) command.

source bin/activate

Fun fact: The source command has a shorter nickname if you don’t want to type as much. It is simply a period.

. bin/activate

On Windows the activate script is inside a folder called Scripts. You will need to move into that folder, run the script, and then back out to the folder we are in now.

First move into the folder.
cd Scripts
Activate the environment. If you are in Cygwin, it will be something like this.
If you are in the default Windows command prompt, more like this.
activate
Then move back to where we were before.
cd ..

You can verify that your virtualenv is running by using the [which](https://en.wikipedia.org/wiki/Which_(Unix)) command to ask your computer what installation of Python it is currently using.

which python

If you are in your virtualenv, it should return a path leading to the same folder inside your virtualenv as activate. My looks like this:

/home/ben/Code/first-python-notebook/bin/python

## Reactivate the virtualenv

You will need to remember to activate your virtualenv environment every time you log on to your computer and start work on this project. Before we move on, let’s take a moment to practice this routine.

Quit out of your command-line interface. Reopen it.

This new terminal will not be activated and working inside your virtual environment. You can verify this by using the which command again.

which python

This time, you are likely to see a path to your computer system’s global installation of Python, which we do not want to use on this project. Here’s what mine looks like (yours will be slightly different):

/usr/bin/python

We need to repeat the steps above to enter your new virtual environment and activate it.

First navigate into your code folder.
cd Code
Then into your virtualenv folder
cd first-python-notebook

Now activate your virtual environment with the source command. In you’re on Mac OSX, let’s use the shorter version this time.

. bin/activate
If you’re on Windows, here’s the routine again.
cd Scripts
. .\activatecd ..

Finally, verify the process has succeeded using the which command. It should now return a path leading to your virtual environment.

which python

That’s it for this chapter. You’ve successfully created your first virtual environment. Now let’s put it to use.