Nine simple steps for better-looking python code - Towards Data Science

# Nine simple steps for better-looking python code

[![0*bS3ijAgMMpl2Nui2.](../_resources/5cc3cd34f9b94f631f2c01e07a052c74.jpg)](https://towardsdatascience.com/@iglovikov?source=post_page-----87e5d9d3b1cf----------------------)

[Vladimir Iglovikov](https://towardsdatascience.com/@iglovikov?source=post_page-----87e5d9d3b1cf----------------------)

[Apr 9](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf?source=post_page-----87e5d9d3b1cf----------------------) · 9 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='196'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='202'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='203' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/87e5d9d3b1cf/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='211'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='212' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/87e5d9d3b1cf/share/facebook?source=post_actions_header---------------------------)

![1*pVTPFHcasXqnlKlH0--YJg.jpeg](../_resources/56ed2c200f9723983eaf4b6c8a1d7f96.jpg)
![1*pVTPFHcasXqnlKlH0--YJg.jpeg](../_resources/8cccf224ddbf7a00515959384eede1ac.jpg)

Source [Comfreak](https://pixabay.com/photos/work-workaholic-writer-programmer-1627703/), via [pixabay](https://pixabay.com/photos/work-workaholic-writer-programmer-1627703/). (Pixabay Licence)

Regularly, I look at the code that supplements academic papers, released datasets, or analyzes the solutions to the [Kaggle](https://www.kaggle.com/) competitions.

My great respect to the researchers that share the code to reproduce their results as well as people who participate in Machine Learning (ML) competitions and share their solutions.

The code is better than the lack of it, but I believe the readability of it could be improved.

The code that I see reminds me of the code that I was writing in academia. I did not like it. This was one of the reasons why I moved to industry. Being able to write code in the modern world is becoming as important as knowing the English language.

The best way to become a better programmer is to join a company with high coding standards. Still, in this blog post, I will talk about the situation when you are working on the codebase alone.

The target audience for this text is researchers, data scientists, and junior software developers.

Becoming a better programmer is a continuous process. The more code you write, the better you become.

I will not tell you how to become good, I will talk on how to make your code look better with a few simple tweaks to your development process.

By simple, I mean easy to implement, less than 5 minutes on each step, and the changes should force you to do things better.

We are lazy. If something falls in the category “nice to do,” we will find many valid reasons to avoid doing it. Things that you are forced work better. First, you will do them because you do not have a choice, later it becomes natural.

Another reason is that decision making sucks willpower. You spend a bit of willpower on a small decision and, as a result, increase chances to oversleep the gym the next morning. When we force behavior, we save precious energy. For those that are interested, the book “[Willpower: Rediscovering the Greatest Human Strength](https://www.goodreads.com/book/show/11104933-willpower?ac=1&from_search=true&qid=8HO9fH0aji&rank=1)” extensively talks on the topic.

## **1. Use version control to track changes in your code**

Versioning your code looks like an obvious must-have, but it is not. In graduate school, my advisor was a very bright person who developed an algorithm to perform Quantum Monte Carlo of the Hubbard model. The code is used by many researchers all over the world to advance theoretical Condensed Matter Physics. When I started to work with it, I was surprised that there was no centralized repository. The exchange of the code was via email. Bugfixes and new features that one scientist developed did not propagate to other users. Besides, I have seen how my colleagues use different folders for code versioning.

Code versioning and using centralized repositories at [GitHub](https://github.com/) or other services is a must-have. Many researchers are doing this, but if you step away from Computer Science, most of the professors and graduate students are in the phase of versioning with folders and sending code in the emails.

**Q:** When do you need to start using git for your project?
**A:** From the first line of the code.

**Q**: When do you need to create a repository at GitHub and push the code there?

**A:** From the first line of the code. If you believe that your code cannot be shared publically due to legal or other reasons, create a private repository. In all other cases, go for the public repo.

It is a mistake when people wait until the code looks good before making it public. Many of my colleagues felt very insecure that there will be non-perfect code in their GitHub repository. They were concerned that people will assume that they are bad programmers. Realistically, no one will judge you. In addition, every code that you write now will look bad when you look at it in six months.

A private repository is better than no repository. The public repository is better than private.

I also like how participants in Kaggle competitions release their pipelines after the contest is over. This is a good habit that will help them as well as the community.

Besides, there is a tool called [Sourcegraph](https://sourcegraph.com/) that allows you to perform the search in the code across all public Github repositories. Extremely convenient. It makes you more productive.

*Links:*

- [Lecture: version control and git](https://www.youtube.com/watch?time_continue=3540&v=2sjqTHE0zok&feature=emb_logo)
- [Pro-git book](https://git-scm.com/book/en/v2)
- [Git from inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out)
- [A successful Git Branching model](https://nvie.com/posts/a-successful-git-branching-model/)

## 2. Do not push to the master branch

When you work in a team, you do not push directly to the master branch. You create a separate branch, work in it, create a pull request (PR), merge the pull request to master. This is more involved than a direct push to master. The reason is that to merge the pull request, your changes should pass various checks. A manual check is a code review by your collaborator. Automatic checks include syntax, style, tests, etc.

When you work alone, you do not have a luxury of the code review, but the power of the automatic checks is still here.

*It is essential is to adjust settings at GitHub so that you will not be able to push to master even if you want. As we discussed above, this prevents slipping and saves willpower energy.*

## **3. Use continuous integration / continuous delivery (CI/CD) systems**

Going through the procedure of creating branches and merging is an overhead. The main reason is that it allows performing checks on the code changes. After you set up the continuous integration system, every pull request that you create will be checked, and the pull request will be merged only after all checks passed.

There are many services that provide CI/CD functionality. GitHub Actions, CircleCi, Travis, Buildkite, etc

I would recommend GitHub Actions. It is free, works both on private and public repositories, easy to setup.

All of this may sound very complex, but in practice, you just need to add a config file to the repository.

- Example [Simple](https://github.com/ternaus/iglovikov_helper_functions/blob/master/.github/workflows/ci.yml): My library with helper functions. I check code style, formatting, and run tests.
- Example [Complex](https://github.com/albumentations-team/albumentations/blob/master/.github/workflows/ci.yml): In the Albumentations library we check syntax, code style, run tests, check the automatic documentation build and we do it for different python versions and operation systems Linux, Windows, Mac OS

*Important! You need to change settings in the GitHub repo so that you will not be able to merge requests without all checks being in the green zone.*

*Links:*

- Blog post: [Martin Fowler about Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)
- Tutorial: [Setting up continuous integration using GitHub Actions](https://help.github.com/en/actions/building-and-testing-code-with-continuous-integration/setting-up-continuous-integration-using-github-actions)
- Book: [Project Phoenix](https://www.goodreads.com/book/show/17255186-the-phoenix-project?ac=1&from_search=true&qid=5m7kj2hM2r&rank=1). Well written book that describes the chaos in the companies before the introduction of CI/CD and other modern practices.

## **4. Code formatters**

There are many ways to format the same piece of code.

- How many spaces to have between the functions?
- How long could be the lines in the code be?
- What is the ordering of imports?
- What kind of quotes should be used to define a string?
- Etc

There are tools called[code formatters.](https://github.com/rishirdua/awesome-code-formatters) If you run them on your code, they will modify the code to fit the requirements of the formatter.

General type formatters:

1. [YAPF](https://github.com/google/yapf): very flexible, you can configure it to fit the desired style.

2. [Black:](https://black.readthedocs.io/en/stable/) non-flexible. Only the length of the line could be configured.

Pick one and add it to your CI/CD config. I like **black**. It makes all my projects and projects that use black to look the same.

Code formatters decrease context switching which makes the reading of the code easier.

There are more specific formatters. For example**  **[**isort**](https://github.com/timothycrosley/isort). Isort simply sorts imports.

You will need to run formatters in two places:

1. In CI/CD. Here you run it in a check mode: formatters will tell you that there are files that they would like to format, but the code will stay the same.

2. Locally before committing the changes. It will reformat your code.
*Links:*

- [Yapf](https://github.com/google/yapf)
- [Black](https://github.com/psf/black)
- [Isort](https://github.com/timothycrosley/isort)
- Blog post: [Consistent python code with Black](https://www.mattlayman.com/blog/2018/python-code-black/)
- Blog post: [Auto formatters for python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)

## **5. Pre-commit hook**

In the previous step, we talked about how important it is to run formatters locally before commit.

Say, we use **black** and **isort**.
We need to run:
black .isort

This is annoying. A better solution would be to create a bash script with these commands, say “code_formatter.sh” and run it.

Creating such scripts is a popular approach, but the issue is that, again, people will not do it unless you force them.

There is a better solution called the [pre-commit hook](https://pre-commit.com/). The idea is similar to bash script, but things that you want to run before every commit will run exactly when you do

git commit -m “<commit message>”

This looks like a small difference, but it is not. With pre-commit, your behavior is enforced, and, as we discussed above, it works better.

**Q**: PyCharm performs good formatting. Why do I need a pre-commit hook?

**A**: You may forget to format your code with PyCharm. Besides, when you have two or more people, you want to be sure that their formatting is the same. For the pre-commit hook, all people will have the same config that is a part of your repository. I would recommend doing both, having a pre-commit hook and formatting the code with a PyCharm.

Q: What if I do not perform commits from the console but do it directly from PyCharm?

A: You can configure PyCharm to run pre-commit hook on every commit.
*Links:*

- [Pre-commit hook](https://pre-commit.com/)

## **6. Linters**

Tools that do not change your code but inspect it and look for possible issues called linters. The most common is [**flake8**](https://flake8.pycqa.org/en/latest/)**.**

It can look for:

- [Pep8 errors and warnings.](http://pep8.readthedocs.org/en/latest/intro.html#error-codes)
- [Consistent naming convention.](https://github.com/PyCQA/pep8-naming)
- [The cyclomatic complexity of your functions.](https://github.com/PyCQA/mccabe)
- And other things with a set of a [plugins](https://github.com/DmytroLitvinov/awesome-flake8-extensions).

It is a powerful tool, and I recommend adding it to your CI/CD config as well as in the pre-commit hook.

*Links:*

- [Flake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/en/latest/)
- [Flake8 extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)

## **7. Mypy: static type checker**

Starting from Python 3, you can add type annotations to the functions in your code. It is optional but highly recommended.

One reason is that it is much easier to read the code that has type annotations.

When you see in the code:
x: pd.DataFrame
It is much more informative than just
x

Of course, you should not name your variables as “x” in the first place. Still, in this blog post, I am talking about simple, automatic ways to improve the code, and good naming is a bit harder than simple. :)

Type annotations are optional. The code works well without them. There is a tool called [Mypy](https://mypy.readthedocs.io/en/stable/) which checks:

- type annotations for functions and input parameters
- consistency between variable types and operations on them

This is a very useful tool. All big tech companies use to check every pull request of their python code.

It forces you to write the code that is easier to read, to rewrite overly complicated, badly written functions and helps to identify bugs.

Mypy checks should be added to CI/CD and pre-commit hook.
*Links:*

- [Mypy documentation](https://mypy.readthedocs.io/en/stable)
- Blog post: [Mypy Optional static typing for python](https://medium.com/@thabraze/mypy-optional-static-typing-for-python-dbc53b82f1ef)
- Blog post: [Mypy and Continuous integration sequence](https://medium.com/@quinn.dougherty92/mypy-and-continuous-integration-sequence-part-1-mypy-and-type-hints-ae69f66b6d9e)

## **8. More checks to pre-commit hook**

You may extend your pre-commit hook with many different things.

- Removing trailing whitespaces.
- The end of the file is at the end of the new line.
- Sorting requirements txt.
- Checking yaml files for the correct format.
- etc

You can create your own hooks for code formatting and checks that should happen automatically.

*Link:*

- [Pre-commit hook: plugins](https://pre-commit.com/#plugins)

## **9. External tools**

There are tools like [Deepsource.io](https://deepsource.io/) and [Deepcode.ai](https://www.deepcode.ai/) that could be used as an additional check for the automatic code review of the pull request.

They are free for public repositories. I do not see any reason why not to enable them for your public code.

*Links:*

- [Deepsource](https://deepsource.io/)
- [Deepcode](https://www.deepcode.ai/)

# **Conclusion**

If a person implements at least some of these techniques, his/her code will become easier to read.

But this is only the first step.
There are other standard techniques like:

- [Unit tests](https://towardsdatascience.com/writing-test-for-the-image-augmentation-albumentation-library-a73d7bc1caa7)
- Unit tests with Hypothesis
- Python environments
- Building packages
- Dockerization
- Automatic documentation
- etc

But they could not be enforced as easy as steps that I described above. Hence we will leave them to another time. :)

P.S. For those readers that have problems implementing the techniques that I described, feel free to ping me, and I will extend the corresponding points.