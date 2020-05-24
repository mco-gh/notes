Poetry - Python dependency management and packaging made easy.

![](../_resources/97bc81c7ca4c195c1c0fc4dc6bb6b723.png)

##### Python packaging and dependency management made easy

# Poetry

 **

	$ poetry add pendulum
	Using version ^1.4 for pendulum

	Updating dependencies
	Resolving dependencies..........

	Package operations: 4 installs, 0 updates, 0 removals

	Writing lock file

	  - Installing tzlocal (1.5.1)
	  - Installing python-dateutil (2.6.1)
	  - Installing pytzdata (2018.3)
	  - Installing pendulum (1.4.2)

###### Deterministic builds

# Develop

Poetry comes with all the tools you might need to manage your projects in a deterministic way.

##### Package with ease

# Build

Easily build and package your projects with a single command.

Supports source distribution and wheels.

	$ poetry build

	Building poetry (0.4.2)

	- Building sdist
	- Built poetry-0.4.2.tar.gz

	- Building wheel
	- Built poetry-0.4.2-py3-none-any.whl

##### Share your work

# Publish

Make your work known by publishing it to PyPI

You can also publish on private repositories

	$ poetry publish

	Publishing poetry (0.4.2) to PyPI

	  - Uploading poetry-0.4.2.tar.gz 100%
	  - Uploading poetry-0.4.2-py3-none-any.whl 58%

	$ poetry show --tree
	requests-toolbelt 0.8.0 A utility belt for advanced users...
	└── requests <3.0.0,>=2.0.1
	    ├── certifi >=2017.4.17
	    ├── chardet >=3.0.2,<3.1.0
	    ├── idna >=2.5,<2.7
	    └── urllib3 <1.23,>=1.21.1

	$ poetry show --outdated
	pendulum 1.4.2   1.4.5 Python datetimes made easy.
	django   1.11.11 2.0.3 A high-level Python Web framework ...
	requests 2.18.4  1.4.5 Python HTTP for Humans.

###### Check the state of your dependencies

# Track

Having an insight of your project's dependencies is just one command way.

 **

###### Dependency resolver

Poetry comes with an exhaustive dependendency resolver, which will always find a solution if it exists.

And get a detailed explanation if no solution exists.

 **

###### Isolation

Poetry either uses your setup virtualenvs or creates its own to always be isolated from your system.

The behavior is configurable.

 **

###### Intuitive CLI

Poetry's commands are intuitive and easy to use, with sensible defaults while still being configurable.

Soon extensible with a plugin system

### * I built Poetry because I wanted the **one** tool to manage my Python projects from start to finish. I wanted something reliable and intuitive that the community could use and enjoy. *

#### Sébastien Eustace

###   [Poetry](https://poetry.eustace.io/)

###### Documentation

- [Introduction](https://poetry.eustace.io/docs/)

- [Basic Usage](https://poetry.eustace.io/docs/basic-usage/)

- [Libraries](https://poetry.eustace.io/docs/libraries/)

- [Commands](https://poetry.eustace.io/docs/cli/)

- [Repositories](https://poetry.eustace.io/docs/repositories/)

- [Versions](https://poetry.eustace.io/docs/versions/)

###### ** Github

- [Issues](https://github.com/sdispater/poetry/issues)

Copyright © 2018. All Rights Reserved