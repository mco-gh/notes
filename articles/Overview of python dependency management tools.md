> Totally confused by all the tools for managing dependencies? Pip, venv, Docker, conda, virtualenvwrapper, pipenv, … Which one should you use? Why do we even have all these different tools? Can they work together?

# Overview of python dependency management tools
Totally confused by all the tools for managing dependencies? Pip, venv, Docker, conda, virtualenvwrapper, pipenv, … Which one should you use? Why do we even have all these different tools? Can they work together?

No wonder. The world of Python dependency management is a mess, but once you understand the tools and why they exist, it’s going to be easier to choose the one you want and deal with the others in environments where you can’t choose your favorite ones.

I’ll briefly describe each tool, why it’s created and the problems it’s tackling At the end of the post, you can find a table summarizing all the information and the usual setups people use.

Jump to: [pip](#pip) | [venv](#venv) | [pyenv](#pyenv) | [conda](#conda) | [pipenv](#pipenv) | [poetry](#poetry) | [Docker](#docker).  
[All solutions compared](#all-solutions-compared) | [Usual setups](#usual-setups)

pip
---

[Pip](https://pypi.org/project/pip/) (**p**ackage **i**nstaller for **p**ython) is the most basic package installer in the python land. It comes preinstalled with most python installations so it’s likely you never had to install it yourself.

Installing a package is as simple as running `pip install torch`. That command talks to PyPI (The Python Package Index), downloads the package, and makes it available to the current python installation.

It’s a very primitive tool. It knows nothing about different python versions or Jupyter kernels.

![](https://d33wubrfki0l68.cloudfront.net/8a4313bb248b64af524b847ca3c0d3cd84c877f8/21585/images/python-dependency-management/pip_install_requests.png "Pip just installs the package in whatever _site-packages_ directory active python installation is pointed to. In this case, it's one activated by pyenv - ~/.pyenv/versions/3.6.3/lib/python3.6/site-packages.")

Pip just installs the package in whatever \_site-packages\_ directory active python installation is pointed to. In this case, it's one activated by pyenv - ~/.pyenv/versions/3.6.3/lib/python3.6/site-packages.

Problems pip solves:

*   Installing python packages

venv
----

[venv](https://docs.python.org/3/library/venv.html) is a tool for creating lightweight virtual environments.

The most common use case is creating an environment per app. It makes sure apps don’t share packages between themselves and they don’t share packages with the system’s python installation. Each environment can use any version of the same package and they won’t collide.

![](https://d33wubrfki0l68.cloudfront.net/89adee9d95ed590faaa8ac008174297107f7a7cc/2a5a8/images/python-dependency-management/venv_install_requests_marked.png "Activating a virtual environment will make following pip installs belong to that virtual environment. You can also see that python run within virtual environment will look into site-packages within that virtual environment.")

Activating a virtual environment will make following pip installs belong to that virtual environment. You can also see that python run within virtual environment will look into site-packages within that virtual environment.

Problems venv solves:

*   Isolating packages between apps

#### How do venv and pip interact?

They’re both the part of standard python tooling, tackle very different problems, and play together really well. You’re encouraged to use pip for installing packages within virtual environments.

pyenv
-----

Python became a wildly popular language and all major operating systems started building on top of it and bundling it out of the box. That’s why you can just type `python` in your terminal on a freshly installed Linux or Mac OS without installing it yourself.

But user applications are built in python, too. And they often need a different version of python! Combination of these two created the need to somehow run different versions of python, depending on the application.

[Pyenv](https://github.com/pyenv/pyenv) was created to solve the problem of installing and switching between different versions of python on the same machine.

It’s a handy tool on developer machines because it keeps the system version of python (needed for the OS to run properly), but can install and switch between different versions for different applications (based on current path, user etc.).

Here’s an example of switching between system version and 3.6.3. Running pyenv local 3.6.3 will remember to activate version 3.6.3 next time you navigate to that directory.

![](https://d33wubrfki0l68.cloudfront.net/748e50fc5dfeb000b9994bc124d421e97752c044/5cbbc/images/python-dependency-management/pyenv_versions.png "Pyenv allows setting the python version for specific directories. That way, you don't have to change it every time you come back to the project.")

Pyenv allows setting the python version for specific directories. That way, you don't have to change it every time you come back to the project.

Problems pyenv solves:

*   Installing different python versions
*   Using different python versions in different contexts

#### How do pyenv and pip interact?

Pyenv and pip complement each other. You can consider pyenv being a container/shell for pip. Pip installs packages for the current python version, whatever pyenv sets it to. In fact, `pip` commands from two environments are different binaries and do not know each other.

![](https://d33wubrfki0l68.cloudfront.net/6930bbe76a9ed4dc398664e876d4a59fe33dcb7a/54b4d/images/python-dependency-management/pyenv_which_pip.png "Different python versions resolve pip3 differently.")

Different python versions resolve pip3 differently.

Conda
-----

_You may know this tool under different names - Anaconda or miniconda._

Once the scientific community started using python seriously, requirements for package management tools in python land increased. More specifically, python became too slow for some pure computational workloads so numpy and scipy were born. These libraries are not really written in python. They are written in C and just wrapped as a python library.

Compiling such libraries brings a set of challenges[1](#fn:conda-compiling-challenges) since they (more or less) have to be compiled on your machine for maximum performance and proper linking with libraries like glibc.

[Conda](https://docs.conda.io/en/latest/) was introduced as an all-in-one solution to manage python environments for the scientific community.

It took a different approach. Instead of using a fragile process of compiling libraries on your machine, libraries are precompiled and just downloaded when you request them. Unfortunately, the solution comes with a caveat - conda does not use PyPI, the most popular index of python packages.

Conda has its own package index with multiple channels ([anaconda channel](https://anaconda.org/anaconda/repo) is maintained by the creators of conda and the most reliable one). Anaconda channel isn’t as complete as PyPI and packages that do exist in both places are often few versions behind the PyPI. Other channels update packages faster, but I strongly suggest checking who maintains respective packages (often not library authors!).

![](https://d33wubrfki0l68.cloudfront.net/38680cf6db1289970f927865210d661582af537a/49599/images/python-dependency-management/conda_list.png "Conda environments encapsulate python, non-python binary (openssl), and python (werkzeug) packages. You can see that activating different environments can swap all of these.")

Conda environments encapsulate python, non-python binary (openssl), and python (werkzeug) packages. You can see that activating different environments can swap all of these.

Altogether, Conda is tackling these problems:

*   Managing different python versions
*   Managing different environments
*   Installing python packages
*   Compiling and installing non-python packages (think OpenSSL, CUDA drivers, etc.)

#### What are anaconda and miniconda?

Anaconda and miniconda are different distributions for conda tools. Miniconda aims to be as minimal as possible - it installs just python and the conda tool. Anaconda installs additional 160+ packages often used in data science workflows.

If you want a tight control of the environment you run, I suggest installing miniconda and building the environment with a bottom-up approach.

#### How does conda interact with pip and other tools?

Conda is a very powerful tool. It tackles many problems so it often clashes with other tools in some axes. It is possible to make conda work with other tools ([with pipenv for example](https://stackoverflow.com/questions/50546339/pipenv-with-conda)), but it requires deeper understanding of both tools, the python package loading, and is not something used very often.

There are two conda setup I’ve found reliable:

*   Conda as all-in-one solution
*   Conda for environment management and installing binary package + pip for python packages ([best practices for conda + pip](https://www.anaconda.com/blog/using-pip-in-a-conda-environment))

Pipenv
------

[Pipenv](https://github.com/pypa/pipenv) is a dev workflow tool, created by the author of popular requests package. Apart from making the common workflows slick and managing the file with requirements (Pipfile), pipenv tackles following problems:

*   Managing different python versions (through pyenv, if installed)
*   Managing different environments
*   Installing python packages
*   Environment reproducibility

It loads packages from PyPI so it does not suffer from the same problem as Conda does.

Pipenv is the first tool mentioned that tackles the environment reproducibility problem in a serious way. Standard ways of saving conda environments (environment.yml) and pip/venv (requirements.txt) tackle part of the problem: they contain versioned packages you’ve installed, but not versions of their dependencies. That leaves space for several classes of errors, including security issues.

![](https://d33wubrfki0l68.cloudfront.net/e3efdacb3196d5caca43b70fc3e0bb367d10fc76/2e02a/images/python-dependency-management/pipenv_first_install.png "Pipenv is really easy to use. First time you run pipenv install, it will create a virtual environment and set everything up for you. It knows which environment to use next time by the directory path.")

Pipenv is really easy to use. First time you run pipenv install, it will create a virtual environment and set everything up for you. It knows which environment to use next time by the directory path.

Pipenv seals package versions by maintaining Pipfile.lock file, containing specific versions of all packages used in the virtual environment.

#### How does pipenv work with pip and other tools?

Pipenv is a nice wrapper around pip and several other tools, which means that it interacts very well with pip. If you use `pipenv install <package>` instead of `pip install <package>`, it will save you several manual steps, though (changing Pipfile and Pipfile.lock).

Poetry
------

[Poetry](https://python-poetry.org/) - “python packaging and dependency management made easy”. Poetry is most similar to pipenv and they often compete for users. Main problems poetry is tackling are:

*   Managing different environments
*   Installing python packages
*   Environment reproducibility
*   Packaging and publishing python packages

You can see that it’s not that different from Pipenv. It’s recommended to [use it with pyenv](https://python-poetry.org/docs/managing-environments/). Once you do that, it tackles all the problems pipenv does, but also helps with creating python packages and publishing them to PyPI.

![](https://d33wubrfki0l68.cloudfront.net/ba698810be2f7420da33b1ba23de2b545f0bd8fb/01991/images/python-dependency-management/poetry_new.png "Poetry is more opinionated than pipenv. E.g., `poetry new` will create a minimal project structure. After that point, they are very similar.")

Poetry is more opinionated than pipenv. E.g., \`poetry new\` will create a minimal project structure. After that point, they are very similar.

#### How does poetry interact with other tools?

Poetry complements pyenv and together they form a complete solution for managing your workflows. Same as with pipenv, it uses PyPI for installing packages so there is no need to use pip once you start using poetry.

#### Pipenv or poetry?

If you wonder why there are two very similar tools, you’re not alone. The main technical difference is the way they resolve packages. It’s actually a very difficult problem and Poetry is superior in that dimension. When you’re installing a new package, it will figure out faster what exactly it has to do and generally, it will handle complex dependency graphs more gracefully.

My general advice is that you’ll be fine with either, just pick one if someone hasn’t done that already for the project you’re working on.

Docker
------

[Docker](https://www.docker.com/) has nothing to do with python dependency management, but people often talk about it in the same context so it’s definitely worth exploring what it does.

Docker is a tool to create, run, and manage containers. You can think of containers as very lightweight virtual machines. There is no virtualization, but they are very isolated from the rest of your operating systems. It was created as a general solution to package production software and run it in a reproducible, isolated way in the cloud.

You can run any of the tools I’ve explained in the Docker container. The nice thing about Docker is that the isolation it gives you dodges several problems. For example, the usual setup is that you run each app in a different container. That means you can install different python versions in there and they won’t know each other. Also, there’s no need for any virtual environment management since apps are isolated by design.

Docker is a great innovation that happened to the way we run software in production, but I don’t recommend it as the solution for python dependency management problems on dev machines.

There are several problems people struggle with when using Docker for dev environments:

*   It takes a significant performance hit on Windows and Mac OS
*   There is far more to learn than just basic conda/pipenv/poetry commands
*   Setting up IDEs to discover and debug app dependencies in Docker containers is often not trivial, which makes development more difficult
*   Installing libraries that deeply link with the underlying system (like CUDA drivers) can become quite tricky

![](https://d33wubrfki0l68.cloudfront.net/d03b7abfb2b4cb93c7edfecdfa41ee6b8ee8ea1a/302ca/images/python-dependency-management/dockerfile.png "Docker is completely agnostic of python or package management tools. This is an example of a Dockefile starting with base Python 3.6.3 image. Inside docker container, you can really use any of the solutions above. People often use just pip to install packages.")

Docker is completely agnostic of python or package management tools. This is an example of a Dockefile starting with base Python 3.6.3 image. Inside docker container, you can really use any of the solutions above. People often use just pip to install packages.

All solutions compared
----------------------

 

Installing python packages

Installing non-python packages

Managing python versions

Managing virtual environments

Environment reproducibility

pip

✅

✖\*

 

 

 

venv

 

 

 

✅

 

pyenv

 

 

✅

 

 

conda

✅

✅

✅\*

✅

 

pipenv (+pyenv)

✅

✅

 

✅

✅

poetry (+pyenv)

✅

✅

 

✅

✅

Docker

\*

\*

\*

\*

✅

\* Pip note: pip doesn’t handle installing non-python packages, but [pip wheels](https://pythonwheels.com/) removed the need to compile packages locally for most libraries, on most architectures

\* Conda note: Even though conda handles installing non-python packages, it can’t replace your system package manager (yum, apt-get) completely. Running your software on platforms like EC2 will still require installing some packages outside of conda.

\* Docker note: since Docker is very much agnostic of Python, you need some other tool inside your container to do these jobs.

Usual setups
------------

#### Pipenv (+ pyenv)

Easy to learn, great setup for managing all main problems around dependency management. Highly recommended. I use it whenever I’m setting up a new project.

#### Poetry (+ pyenv)

Same as pipenv, it brings a lot to the table with no major drawbacks.

#### Conda alone

Some people use the conda alone. The main problem with this setup is that some libraries are not available in conda channels so you have to resort to using conda + pip.

#### Conda + pip

Common setup, using conda for python version management, virtual environment management, and installing binary dependencies. Pip used for installing python packages. Unfortunately, I’ve mentioned it has its own problems, and conda in general is a very bulky tool.

This is often used because conda integrates very well with Jupyter through [nb\_conda\_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels) extension. I use this whenever I have to use conda in the environment somebody else has set up (like SageMaker).

#### Pyenv + pip + venv

Lightweight setup to manage different python versions and virtual environments. Lacks the solution for environment reproducibility, which is a problem for reliable production operation.