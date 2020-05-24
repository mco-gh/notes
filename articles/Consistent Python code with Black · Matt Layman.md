Consistent Python code with Black · Matt Layman

I have released a new Django podcast about learning Django. This new podcast, Django Riffs, is available at [djangoriffs.com](https://djangoriffs.com/).

 [#Black](https://www.mattlayman.com/tags/black/)  [#Code formatter](https://www.mattlayman.com/tags/code-formatter/)

# Consistent Python code with Black

 ![](../_resources/b4fa4ffd9d1540c08aac1a2f34d407c0.png)

Code formatting is the subject of millions of fiery, nerdy debates. Developers love to argue about code style because we read code a lot. The style matters because it affects readability.

We have examples of communities that benefit from a shared code style.

- The Go programming language has `gofmt` (i.e., “go format”) baked in as a core tool in the language. Their core team decided on a set of rules to use and everyone gets the benefit of reading code that looks very similar.[Learn more](https://blog.golang.org/go-fmt-your-code)
- The Python community rallied behind [PEP 8](https://www.python.org/dev/peps/pep-0008/)as the guide for what Python code should aspire to. PEP 8 adds a level of consistency which makes moving from one project to another feel natural.

If we drill into the Python example, we can see a difference compared to Go.`gofmt` is a *tool* that will automatically fix style errors. PEP 8 is a *style guide*. It is **not** a tool. The consequence of focusing on a style guide instead of a tool is that it’s possible to have inconsistent code.

Generally, the community answer to making PEP 8-style code was to use a lint tool like:

- [pycodestyle](http://pycodestyle.pycqa.org/en/latest/) (formerly call pep8)
- [flake8](http://flake8.pycqa.org/en/latest/)(flake8 is a wrapper that bundles pycodestyle and [pyflakes](https://pypi.org/project/pyflakes/) together).

These tools *report* the problems, but do not fix them. This puts the burden on the developer to fix the code.[1](https://www.mattlayman.com/blog/2018/python-code-black/#fn:1)A tool to *fix* style issues is a task perfectly suited for a computer to do automatically!

**> What happens when a project adopts a tool that *> automatically*> sets the code style?**

Now is the perfect time to introduce [Black](https://black.readthedocs.io/en/stable/).

*Black is like `gofmt` for Python.*While it’s not a tool that is officially endorsed by the Python core team, it does automatically format code.

Black’s formatting rules are a superset of PEP 8. If you choose to use Black, you get PEP 8 compliance for free, plus some other style choices that the Black team sees as helpful for making maintainable code.

The Black team touts the tool as “The Uncompromising Code Formatter.” Practically, this means that Black comes with very few configuration options to affect the style. Limiting options for code formatting is A Good Thing™. With few options, code from project to project that is Black formatted looks **very** similar.

By using Black, we get the benefit of code that is similar which allows us to focus more on the content than trip over unfamiliar styling choices.

> Commonly formatted code aids our brains to focus on the problem and code solution, rather than get distracted by code structure and minor stylistic differences.

## Using Black

To get started with the tool, install it with `pip`:
`$ pip install black`

I’d recommend installing Python packages into a virtual environment using [venv](https://docs.python.org/3/library/venv.html). You could also use a tool like [Pipenv](https://pipenv.readthedocs.io/en/latest/)to help you manage your Python project.

Once Black is installed, you will have a new command line tool called `black`available to you in your shell, and you’re ready to start!

(One word of caution before you try this yourself: Black *will* change your code files. If you only want to experiment with this, I strongly encourage you to use a version control tool like [Git](https://git-scm.com/)or work from a copy.)

Black can work on individual files or entire directories of Python code.

	$ black my_file.py
	All done! ✨  ✨
	1 file left unchanged.

	$ black my_package/
	All done! ✨  ✨
	108 file left unchanged.

Emoji. Cute.

When Black has nothing to change, the output is short and direct. When Black changes code, it summarizes the changes concisely.

	$ black my_package/
	reformatted /Users/matt/projects/my_package/some_file.py
	All done! ✨  ✨
	1 file reformatted, 107 files left unchanged.

I really like this output because it tells me everything that I might care about and leaves out noise that often sneak into tools like this.

It’s nice to run Black from the command line, but it would be even better to run straight from your editor. Thankfully, the documentation covers[editor configuration](https://github.com/ambv/black#editor-integration)for many popular editors (including my fav, Vim!).

After I installed the Black plugin for Vim, I modified my `vimrc`to format on save and I could immediately benefit from formatted code.

	" Run Black on save.
	autocmd BufWritePre *.py execute ':Black'

## Using Black on a team

The previous section looked at how to use Black on a personal level. How could a team of developers working on a project use Black together? Let’s consider two topics:

1. Black in Continuous Integration (CI)
2. Black as a Git pre-commit hook

### Black in Continuous Integration (CI)

If you’re working on a team to develop a software project and you’re *not* using Continuous Integration, then (please!) consider using a service like[Travis CI](https://travis-ci.org/)or[Circle CI](https://circleci.com/). After a bit of setup, Continuous Integration tools and services can save so much time by checking for bugs, running your tests automatically, and building your code.

One great use of CI is for lint checking. Lint is a category of software issues that automated tools are really good at reporting.

Can you guess where this is going? Black has a mode that directly supports CI checking!

	$ black --check my_package/
	would reformat /Users/matt/projects/my_package/some_file.py
	All done!
	1 file would be reformatted, 107 files would be left unchanged.

If you add Black to a CI build process with the `--check` option, the tool will report any code that does not adhere to the code format and fail the CI build. This may not sound like a good thing, but it is!

The check option helps ensure that the team produces consistently styled code. It is a guard that can keep code quality high.

### Black as a Git pre-commit hook

Git can run special scripts at various places in the Git workflow (which the system calls “hooks”). These scripts can do whatever you want and, in theory, can help a team with their development flow.

I used to think these hooks were not very useful to teams. My belief stemmed from a team’s inability to add these hook scripts to version control in a way that would apply the scripts for every team member.

Then I found [pre-commit](https://pre-commit.com/). pre-commit makes hook scripts extremely accessible to teams. How?

`$ pre-commit install`

With that one command, pre-commit installs everything a developer needs to make hooks accessible at a team level.`pre-commit install` is a bootstrapping command that inserts all the necessary scripts to let pre-commit manage it all.

After the install command executes, pre-commit will use a `.pre-commit-config.yaml` file to make decisions about what to do at the various Git hook points.

This gives power to a team since `.pre-commit-config.yaml`can be added to source control and the team can make shared configuration choices.

One of those configurations choices is… drumroll please… Black configuration! The details of this setup are explained in the [Version control integration](https://github.com/ambv/black#version-control-integration) section of the documentation, but the short version is to add the following to `.pre-commit-config.yaml`:

	repos:

	  - repo: https://github.com/ambv/black

	    rev: stable
	    hooks:

	    - id: black

	      language_version: python3.7

For any developer with pre-commit installed, commiting with Git will generate output like:

	$ git commit
	black....................................................................Failed
	hookid: black

	Files were modified by this hook. Additional output:

	reformatted my_package/some_file.py
	All done! ✨  ✨
	1 file reformatted.

It’s nice to catch code formatting problems in CI, and it’s even nicer to catch them before your code is committed to source control!

### Paint it Black

In this post, I showed you how you can use Black to format your code. It’s hard to express the value of consistent code formatting unless you’ve worked on a team, but I hope you can imagine the benefits of a shared style.

When using a tool for yourself, Black helps you review *your own* code in the future and have a consistent experience. To that end, we looked at how to set up the tool on your own.

Since the greatest benefits come for teams, I focused on two separate ways that teams can build Black into their workflow.

- Using Black in continuous integration can keep code style consistent before it is merged on a master branch.
- Using Black with pre-commit hooks for version control can keep style consistent before it is even committed to a repository.

Both of these patterns are effective ways to manage a team’s code style.

I think Black is a really great way to let software make our job as Python developers easier so I hope you’ll check it out!

* * *

1. This is not a knock on pycodestyle or flake8. I have been a happy user of flake8 for years and I’m glad it exists.

 [[return]](https://www.mattlayman.com/blog/2018/python-code-black/#fnref:1)

## Learn more about Python!

You can join my newsletter along with hundreds of other developers and get access to useful topics to help you learn more about Python and software development.

I’ll get you started with my Pythonic code email course. I hope you'll join up!

* indicates required

 Email Address *

 First Name *

 [![](../_resources/ce69fa05f85e673d8ff35689a7295a9a.png)   - #python    - #mobile    - #BeeWare    - #Python Frederick       ## Build Native Mobile Apps with Python (BeeWare)     You can build mobile applications with Python? Absolutely. At Python Frederick’s October 2018 presentation, Bob Marchese showed us how to use BeeWare, a suite of tools for building mobile apps (among other things). This post includes links to the YouTube presentation and his material.](https://www.mattlayman.com/blog/2018/build-mobile-python-apps-beeware/)

 [![](../_resources/00712cb42e8c943f40835a208ae9222a.png)   - #Hugo    - #static site generators    - #handroll       ## A tale of two site generators     I switched my website from a custom made tool, handroll, to a very popular static site generator, Hugo. Why would someone switch from something tailor-made to a different tool? I explore what I’ve learned from going my own way for many years.](https://www.mattlayman.com/blog/2018/tale-two-site-generators/)