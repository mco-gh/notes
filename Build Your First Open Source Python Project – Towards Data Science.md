Build Your First Open Source Python Project – Towards Data Science

# Build Your First Open Source Python Project

## A step-by-step guide to a working package

[![1*Asb9N4lW4pQN_Id2qwtPOA.jpeg](../_resources/67b44805623dec4f1b33b88620d4ccc7.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='211' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://towardsdatascience.com/@jeffhale?source=post_header_lockup)

[Jeff Hale](https://towardsdatascience.com/@jeffhale)

Feb 25·11 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='212'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

Every software developer and data scientist should go through the exercise of making a package. You’ll learn so much along the way.

Making an open source Python package may sound daunting, but you don’t need to be a grizzled veteran. You also don’t need an elaborate product idea. You do need persistence and time. Hopefully this guide will help you need less of both.

![](../_resources/b5372683f3ab84cc2b6128e2d4f73c01.png)![1*JPm5rhWjFh8IX-OL8TDMPg.jpeg](../_resources/c44cac0feb8853c0ca4eeadebbf7e262.jpg)

Build something beautiful

In this article, we’ll go through each step to make a basic Python package. In future articles we’ll set up automated tests and doc builds. We’ll also integrate other helpful apps to improve your package development. You can then expand what you’ve built to suit your needs.

This guide is for macOS with Python 3.7. Everything works now, but things change fast, so no guarantees if your reading this in 2030, or even 2020. Replace *my_package*, *my_file,* etc. with your own names.

Let’s get to it!

### Step 1: Make a Plan

We’re eventually planning to make a very simple library for use in a Python program. The package will allow the user to easily convert a Jupyter notebook into an HTML file or a Python script.

The first iteration of our package will allow a user to call a function that will print a statement.

Now that we know what we want to make, we need to decide what to call the package.

### Step 2: Name it

Naming things is tricky. Names should be unique, short, and memorable. They should also be all lowercase and definitely not have any dashes or other punctuation in them. Underscores are discouraged. When you’re building your package, check that the name is available on GitHub, Google, and PyPI.

If you have high hopes that your package will some day have 10,000 GitHub stars, then you might want to check if the name is available on social networks. In this example, I’m going to name my package *notebookc* because it’s available, short, and semi-descriptive.

### Step 3: Configure Environment

Make sure you have Python 3.7, GitHub, and Homebrew installed and configured. If you need any of those here are the details:

#### Python

Download Python 3.7 [here](https://www.python.org/downloads/) and install it.

#### GitHub

If you don’t have a GitHub account, go [here](https://github.com/join) and sign up for a free one. See how to install and configure Git [here](https://help.github.com/articles/set-up-git/). You want the command line tool. Follow the links to download it, install it, set your username, and set your commit email address.

#### Homebrew

Homebrew is a Mac-specific package manager. Install instructions are [here](https://brew.sh/).

![](../_resources/28ad8188db1e49d7c640b2dea388f520.png)![1*2gQlLVGIKJVq2AytXqAlEg.jpeg](../_resources/98a28e857f61d17a7495e4dfa3b722c7.jpg)

#### Venv

As of Python 3.6, it is recommended to use [*venv*](https://docs.python.org/3/library/venv.html)*  *to create your virtual environment for package development. There are many ways to manage virtual environments with Python and the recommendations have evolved. See discussion [here](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe), but beware going down this rabbit hole.

*venv* comes installed with Python since Python 3.3. Note that* venv* installs *pip* and *setuptools* into the virtual environment since Python 3.4 .

Create a Python 3.7 virtual environment with the following command:
`python3.7 -m venv my_env`

Replace *my_env* with any name you like. Activate your virtual environment like this:

`source my_env/bin/activate`

You should now see `(my_env)`— or whatever you named your virtual environment— to the far left in your terminal prompt.

When you’re finished with your development, deactivate your virtual environment with `deactivate`.

Now let’s take care of setting up things on GitHub.

### Step 4: Create Organization on GitHub

GitHub is the market leader in version control registries. GitLab and Bitbucket are other popular options. We’ll be using GitHub in this guide.

- •You’ll use Git and GitHub a bunch, so if you aren’t familiar, check out my article [here](https://towardsdatascience.com/learn-enough-git-to-be-useful-281561eef959?source=friends_link&sk=549f0155d272316b6f06fa6f7818beee).
- •Create a new organization on Github. Follow the prompts. I named my organization *notebooktoall.* You could create the repo under your own personal account, but part of the goal is to learn how to setup an open source project for the larger community.

![](../_resources/376f6c759fa9540cb249f0c178bd5b35.png)![1*GLNwgRXH3mxtsJdzcNTf3Q.png](../_resources/8b4480e7af1dd80ae8b8d2e2e1f897e8.png)

### Step 5: Set up GitHub Repo

Create a new repository. I named my repo *notebookc.*

![](../_resources/4ca22ef05dffc472e359e4edfe49b656.png)![1*XjMgCTPiir272NAwlVTKAQ.png](../_resources/4aaff334d00a65f10909046fdd4444f7.png)

Add a .*gitignore* from the dropdown list. Choose *Python* for your repository. The contents of your .*gitignore* file will match folders and file types to exclude from your Git repo. You can alter your .gitignore later to exclude other unnecessary or sensitive files.

I suggest you choose a license from the *Add a license* dropdown*. *The license*  *defines what users of your repository content can do. Some licenses are more permissive than others. Default copyright laws apply if no license is chosen. Learn more about licenses [here](https://help.github.com/articles/licensing-a-repository/).

For this project I chose the GNU General Public License v3.0 because it is popular, legit, and “guarantees end users the freedom to run, study, share and modify the software” — [source](https://en.wikipedia.org/wiki/GNU_General_Public_License).

![](../_resources/6ebdbbeeaa7cb919e0216719a28553f4.png)![1*WN237sm9SJYjOSUjGyVhiw.png](../_resources/dddd276a84ae1ea77eec5ab2e5eb1199.png)

### Step 6: Clone and Add Directories

Choose where you want to clone your repo locally and run the following:

`git clone [https://github.com/notebooktoall/notebookc.git](https://github.com/notebooktoall/notebook_convert.git)`

Substitute your organization and repo.

Move into your project folder with your desktop GUI or code editor. Or use the command line with `cd my-project` and then view your files with `ls —A`. Your initial folders and files should look like this:

.git
.gitignore
LICENSE
README.rst

Create a subfolder for your primary project files. I suggest you name this primary subfolder the same name as your package. Make sure the name doesn’t have any spaces in it.

Make a file named *__init__.py* in your primary subfolder. This file will remain empty for now. This file is necessary for the files in this folder to be imported.

Make another file with the same name as your primary subfolder with *.py* appended to it. My file is named *notebookc.py*. You could name this Python file whatever you like. Your package users will

My *notebookc* directory contents now look like this:
.git
.gitignore
LICENSE
README.rst
notebookc/__init__.py
notebookc/notebookc.py

### Step 7: Create and Install requirements_dev.txt

In the top level of your project directory, create a *requirements_dev.txt* file. Often this file is named *requirements.txt*. Calling it requirements_dev.txt highlights that these packages are only installed by project developers.

In requirements_dev.txt, specify that pip and [wheel](https://pythonwheels.com/) should be installed.

pip==19.0.3
wheel==0.33.1

Notice that we specify exact versions of these packages with double equals signs and full major.minor.micro version numbers.

![](../_resources/3e14343e833b8873cc5bffb8519f7b2a.png)![1*BtcBr_91Cod30MuZQSZKOA.jpeg](../_resources/d9d7d748db9ee27e4b46268cda838c7e.jpg)

Pin your package versions in requirements_dev.txt

A collaborator who forks the project repo and installs the pinned requirements_dev.txt packages with pip will have the same package versions you did. You know they will work for them. Also, Read The Docs will use this file to install packages when it builds your documentation.

In your activated virtual environment, install the packages in requirements_dev.txt with the following command:

`pip install -r requirements_dev.txt`

You’ll want to keep these packages updated as newer versions are released. For now, you can install whatever versions are newest by searching [PyPI](https://pypi.org/).

We’ll install a tool to help with this process in a future article. Follow [me](https://medium.com/@jeffhale) to make sure you don’t miss it.

### Step 8: Code and Commit

Let’s create a basic function for demonstration purposes. You can create your own awesome function later.

Type the following into your primary file (for me that’s *notebookc/notebookc/notebookc.py*):

![](../_resources/83a4a9371aa13f9813d380455ffc8205.png)

|     |     |
| --- | --- |
| 1   | def  convert(my_name): |
| 2   |  """ |
| 3   | Print a line about converting a notebook. |
| 4   | Args: |
| 5   | my_name (str): person's name |
| 6   | Returns: |
| 7   | None |
| 8   |  """ |
| 9   |     |
| 10  |  print(f"I'll convert a notebook for you some day, {my_name}.") |

 [view raw](https://gist.github.com/discdiver/8d4fecd04c417bf0698c2b9386443be2/raw/67972e668b9a5af312b933a3ea6cf0368991aba5/notebookc.py)  [notebookc.py](https://gist.github.com/discdiver/8d4fecd04c417bf0698c2b9386443be2#file-notebookc-py) hosted with ❤ by [GitHub](https://github.com/)

That’s our function in all its glory.

The docstrings begin and end with three consecutive double quotes. They’ll be used in later article to automatically create documentation.

Let’s commit our changes. See [this article](https://towardsdatascience.com/learn-enough-git-to-be-useful-281561eef959?source=friends_link&sk=549f0155d272316b6f06fa6f7818beee) if you’d like a Git workflow refresher.

### Step 9: Create setup.py

The *setup.py *file is the build script for your package. The *setup* function from Setuptools will build your package for upload to PyPI. Setuptools includes information about your package, your version number, and which other packages are required for users.

Here’s my example setup.py file:

|     |     |
| --- | --- |
| 1   | from setuptools import setup, find_packages |
| 2   |     |
| 3   | with  open("README.md", "r") as readme_file: |
| 4   | readme = readme_file.read() |
| 5   |     |
| 6   | requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"] |
| 7   |     |
| 8   | setup( |
| 9   |  name="notebookc", |
| 10  |  version="0.0.1", |
| 11  |  author="Jeff Hale", |
| 12  |  author_email="jeffmshale@gmail.com", |
| 13  |  description="A package to convert your Jupyter Notebook", |
| 14  |  long_description=readme, |
| 15  |  long_description_content_type="text/markdown", |
| 16  |  url="https://github.com/your_package/homepage/", |
| 17  |  packages=find_packages(), |
| 18  |  install_requires=requirements, |
| 19  |  classifiers=[ |
| 20  |  "Programming Language :: Python :: 3.7", |
| 21  |  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)", |
| 22  | ],  |
| 23  | )   |

 [view raw](https://gist.github.com/discdiver/bfa7a23fb3147442dd1229cd482103dd/raw/efd04a8a5cdfb3bfe5f752383664171418b4f8c4/setup.py)  [setup.py](https://gist.github.com/discdiver/bfa7a23fb3147442dd1229cd482103dd#file-setup-py) hosted with ❤ by [GitHub](https://github.com/)

Notice that *long_description* is set to the contents of your README.md file.

The* requirements* list specified in *setuptools.setup.install_requires* includes all necessary package dependencies for for your package to work.

Unlike the list of packages required for development in requirements_dev.txt, this list of packages should be as permissive as possible. Read more about why [here](https://stackoverflow.com/a/33685899/4590385).

Limit this *install_requires* list of packages to only wants needed — you don’t want to make users install unnecessary packages. Note that you only need to list packages that aren’t part of the Python standard library. Your user will have Python installed if they will be using your package.

Our package doesn’t require any external dependencies, so you can exclude the four packages listed aboveA collaborator who forks the project repo and installs the pinned packages with pip will have the same package versions you did. You know they will work.

Change the other setuptools information to match your package information. There are many other optional keyword arguments and classifiers — see a list [here](https://packaging.python.org/guides/distributing-packages-using-setuptools/). More in-depth guides to setup.py can be found [here](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and [here](https://github.com/kennethreitz/setup.py).

Commit your code to your local Git repo. Let’s get ready to build a package!

### Step 10: Build First Version

Twine is a collection of utilities for securely publishing Python packages on PyPI. Add the [Twine](https://pypi.org/project/twine/) package to the next blank line of *requirements_dev.txt *like so:

`twine==1.13.0`

Then install Twine into your virtual environment by reinstalling your requirements_dev.txt packages.

`pip install -r requirements_dev.txt`
Then run the following command to create your package files:
`python setup.py sdist bdist_wheel`

Multiple hidden folders should be created: *dist*, *build*, and — in my case — *notebookc.egg-info*. Let’s look at the files in the *dist* folder. The .whl file is the Wheel file — the built distribution. The .tar.gz file is the a source archive.

![](../_resources/ea122a3f48b390dbd99d82a75ddb27e2.png)![1*FDKdxTskSaRn1HtMHYT_3g.png](../_resources/2abde98a52110aa77e0f952e72be9008.png)

Wheel

On a user’s machine, pip will install packages as wheels whenever it can. Wheels are faster to install. When pip can’t install a wheel, it falls back on the source archive.

Let’s get ready to upload our wheel and source archive.

### Step 11: Create TestPyPI Account

[PyPI](https://pypi.org/) stands for Python Package Index. It’s the official Python package manager. *pip* grabs files from PyPI when they aren’t already installed locally.

![](../_resources/027bfbfa3bfdea906adf4f4813d922fd.png)![1*5z5dgdZPg4QORQ1794NFBw.png](../_resources/385b3e70f813b80c72027f65a0e16b7a.png)

PyPI

TestPyPI is a functioning test version of PyPI. Create a TestPyPI account [here](https://test.pypi.org/account/register/) and confirm your email address. Note that you’ll have separate passwords for uploading to the test site and official site.

### Step 12: Publish to TestPyPI

![](../_resources/23e7aefa692d976b1f56b03bf048914b.png)![1*N_OvcK2IwtZL2R-fThQAyw.jpeg](../_resources/8d4e21799b51c5a9b99446927519c52b.jpg)

Twine

Use [Twine](https://pypi.org/project/twine/) to securely publish your package to TestPyPI. Enter the following command — no modifications are necessary.

`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

You’ll be prompted for your username and password. Remember, TestPyPI and PyPI have different passwords!

If needed, fix any errors, make a new version number in setup.py, and delete the old build artifacts: the *build*, *dist*, and *egg* folders. Rebuild with `python setup.py sdist bdist_wheel` and re-upload with Twine. Having version numbers on TestPyPI that don’t signify anything isn’t a big deal — you’re the only one who will use those package versions.

Once you’ve successfully uploaded your package, let’s make sure you can install it and use it.

### Step 13: Verify Installation and Use

Create another tab in your terminal shell and make another virtual environment.
`python3.7 -m venv my_env`
Activate it.
`source my_env/bin/activate`

If you had uploaded your package to the official PyPI site you would then `pip install your-package`. We can retrieve the package from TestPypPI and install it with a modified command.

Here are the official instructions to install your package from [TestPyPI](https://packaging.python.org/guides/using-testpypi/):

> You can tell pip to download packages from TestPyPI instead of PyPI by specifying the — index-url flag

`pip install --index-url https://test.pypi.org/simple/ my_package`

> If you want to allow pip to also pull other packages from PyPI you can specify — extra-index-url to point to PyPI. This is useful when the package you’re testing has dependencies:

`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple my_package`

If your package has dependencies, use the second command and substitute your package name.

You should see the latest version of your package installed in your virtual environment.

To verify you can use your package, start an IPython session in your terminal with:

`python`

Import your function and call your function with a string argument. Here’s what my code looks like:

`from notebookc.notebookc import convert`
`convert(“Jeff”)`
I then see this output:
`I’ll convert a notebook for you some day, Jeff.`
Sure you will.
Alright, let’s upload our work to GitHub.

![1*B9r-WMdJ-m31kg-tzedWjw.png](../_resources/07dafe58c749fa6df5920fadcde7568f.png)

### Step 14: Push to GitHub

Make sure you have your code committed.
My *notebookc* project folder looks like this:
.git
.gitignore
LICENSE
README.md
requirements_dev.txt
setup.py
notebookc/__init__.py
notebookc/notebookc.py

Exclude any virtual environments you don’t want to upload. The Python .gitignore file that we chose when we made the repo should keep build artifacts from being indexed. You may need to delete your virtual environment folders.

Push your local branch to GitHub with `git push origin my_branch`.

### Step 15: Create and Merge PR

From your browser, navigate to GitHub. You should see an option to make a pull request. Keep pressing the green buttons to create and merge your PR, and delete your remote feature branch.

Back in your terminal, delete your local feature branch with `git branch -d my_feature_branch`.

We’ll add many more files and folders in future articles.
Let’s recap our steps.

### Recap: 15 Steps to a Working Package

1. 1 "."Make a Plan
2. 2 "."Name it
3. 3 "."Configure Environment
4. 4 "."Create Organization on Github
5. 5 "."Set up GitHub Repo
6. 6 "."Clone and Add Directories
7. 7 "."Create and Install *requirements_dev.txt*
8. 8 "."Code and Commit
9. 9 "."Create *setup.py*
10. 10 "."Build First Version
11. 11 "."Create TestPyPI Account
12. 12 "."Push to TestPyPI
13. 13 "."Verify Installation and Use
14. 14 "."Push to GithHub
15. 15 "."Create and Merge PR

### Wrap

I hope you found this guide to making and releasing your first Python package useful. If you did, please share it on your favorite social media channels so others can find it too.

In the next part in this series we’ll add tests, continuous integration, code coverage, and more. Follow [me](https://medium.com/@jeffhale) to make sure you don’t miss it!

I write about Python, Docker, data science, and other tech topics. If any of that’s of interest to you, read more [here](https://medium.com/@jeffhale).

Happy building!

![](../_resources/6796d2ee42ce50c06f59870ce329412e.png)![1*k7bWHsnX4F2d11E4Yn_Kng.jpeg](../_resources/8f99b450dafd2052606c701c9a26b09d.jpg)