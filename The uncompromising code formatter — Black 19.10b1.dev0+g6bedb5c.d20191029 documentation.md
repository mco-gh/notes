The uncompromising code formatter — Black 19.10b1.dev0+g6bedb5c.d20191029 documentation

# The uncompromising code formatter[¶](https://black.readthedocs.io/en/stable/#the-uncompromising-code-formatter)

By using *Black*, you agree to cede control over minutiae of hand-formatting. In return, *Black* gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

*Black* makes code review faster by producing the smallest diffs possible. Blackened code looks the same regardless of the project you’re reading. Formatting becomes transparent after a while and you can focus on the content instead.

Try it out now using the [Black Playground](https://black.now.sh/).
Note:

[Black is beta](https://black.readthedocs.io/en/stable/installation_and_usage.html#note-this-is-a-beta-product).

## Testimonials[¶](https://black.readthedocs.io/en/stable/#testimonials)

**Dusty Phillips**, [writer](https://smile.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dusty+phillips):

*> Black is opinionated so you don’t have to be.*

**Hynek Schlawack**, creator of [attrs](https://www.attrs.org/), core developer of Twisted and CPython:

*> An auto-formatter that doesn’t suck is all I want for Xmas!*
**Carl Meyer**, [Django](https://www.djangoproject.com/) core developer:
*> At least the name is good.*

**Kenneth Reitz**, creator of [requests](http://python-requests.org/)and [pipenv](https://docs.pipenv.org/):

*> This vastly improves the formatting of our code. Thanks a ton!*

## Contents[¶](https://black.readthedocs.io/en/stable/#contents)

- [Installation and usage](https://black.readthedocs.io/en/stable/installation_and_usage.html)
    - [Installation](https://black.readthedocs.io/en/stable/installation_and_usage.html#installation)
    - [Usage](https://black.readthedocs.io/en/stable/installation_and_usage.html#usage)
    - [Command line options](https://black.readthedocs.io/en/stable/installation_and_usage.html#command-line-options)
    - [NOTE: This is a beta product](https://black.readthedocs.io/en/stable/installation_and_usage.html#note-this-is-a-beta-product)
- [The *Black* code style](https://black.readthedocs.io/en/stable/the_black_code_style.html)
    - [How *Black* wraps lines](https://black.readthedocs.io/en/stable/the_black_code_style.html#how-black-wraps-lines)
    - [Line length](https://black.readthedocs.io/en/stable/the_black_code_style.html#line-length)
    - [Empty lines](https://black.readthedocs.io/en/stable/the_black_code_style.html#empty-lines)
    - [Trailing commas](https://black.readthedocs.io/en/stable/the_black_code_style.html#trailing-commas)
    - [Strings](https://black.readthedocs.io/en/stable/the_black_code_style.html#strings)
    - [Numeric literals](https://black.readthedocs.io/en/stable/the_black_code_style.html#numeric-literals)
    - [Line breaks & binary operators](https://black.readthedocs.io/en/stable/the_black_code_style.html#line-breaks-binary-operators)
    - [Slices](https://black.readthedocs.io/en/stable/the_black_code_style.html#slices)
    - [Parentheses](https://black.readthedocs.io/en/stable/the_black_code_style.html#parentheses)
    - [Call chains](https://black.readthedocs.io/en/stable/the_black_code_style.html#call-chains)
    - [Typing stub files](https://black.readthedocs.io/en/stable/the_black_code_style.html#typing-stub-files)
- [pyproject.toml](https://black.readthedocs.io/en/stable/pyproject_toml.html)
    - [What on Earth is a `pyproject.toml` file?](https://black.readthedocs.io/en/stable/pyproject_toml.html#what-on-earth-is-a-pyproject-toml-file)
    - [Where *Black* looks for the file](https://black.readthedocs.io/en/stable/pyproject_toml.html#where-black-looks-for-the-file)
    - [Configuration format](https://black.readthedocs.io/en/stable/pyproject_toml.html#configuration-format)
    - [Lookup hierarchy](https://black.readthedocs.io/en/stable/pyproject_toml.html#lookup-hierarchy)
- [Editor integration](https://black.readthedocs.io/en/stable/editor_integration.html)
    - [Emacs](https://black.readthedocs.io/en/stable/editor_integration.html#emacs)
    - [PyCharm/IntelliJ IDEA](https://black.readthedocs.io/en/stable/editor_integration.html#pycharm-intellij-idea)
    - [Wing IDE](https://black.readthedocs.io/en/stable/editor_integration.html#wing-ide)
    - [Vim](https://black.readthedocs.io/en/stable/editor_integration.html#vim)
    - [Visual Studio Code](https://black.readthedocs.io/en/stable/editor_integration.html#visual-studio-code)
    - [SublimeText 3](https://black.readthedocs.io/en/stable/editor_integration.html#sublimetext-3)
    - [Jupyter Notebook Magic](https://black.readthedocs.io/en/stable/editor_integration.html#jupyter-notebook-magic)
    - [Python Language Server](https://black.readthedocs.io/en/stable/editor_integration.html#python-language-server)
    - [Atom/Nuclide](https://black.readthedocs.io/en/stable/editor_integration.html#atom-nuclide)
    - [Kakoune](https://black.readthedocs.io/en/stable/editor_integration.html#kakoune)
    - [Other editors](https://black.readthedocs.io/en/stable/editor_integration.html#other-editors)
- [blackd](https://black.readthedocs.io/en/stable/blackd.html)
    - [Usage](https://black.readthedocs.io/en/stable/blackd.html#usage)
    - [Protocol](https://black.readthedocs.io/en/stable/blackd.html#protocol)
- [Version control integration](https://black.readthedocs.io/en/stable/version_control_integration.html)
- [Ignoring unmodified files](https://black.readthedocs.io/en/stable/ignoring_unmodified_files.html)
- [Contributing to *Black*](https://black.readthedocs.io/en/stable/contributing.html)
    - [Bird’s eye view](https://black.readthedocs.io/en/stable/contributing.html#bird-s-eye-view)
    - [Technicalities](https://black.readthedocs.io/en/stable/contributing.html#technicalities)
    - [Hygiene](https://black.readthedocs.io/en/stable/contributing.html#hygiene)
    - [Finally](https://black.readthedocs.io/en/stable/contributing.html#finally)
- [Show your style](https://black.readthedocs.io/en/stable/show_your_style.html)
- [Change Log](https://black.readthedocs.io/en/stable/change_log.html)
    - [19.10b0](https://black.readthedocs.io/en/stable/change_log.html#b0)
    - [19.3b0](https://black.readthedocs.io/en/stable/change_log.html#id1)
    - [18.9b0](https://black.readthedocs.io/en/stable/change_log.html#id2)
    - [18.6b4](https://black.readthedocs.io/en/stable/change_log.html#b4)
    - [18.6b3](https://black.readthedocs.io/en/stable/change_log.html#b3)
    - [18.6b2](https://black.readthedocs.io/en/stable/change_log.html#b2)
    - [18.6b1](https://black.readthedocs.io/en/stable/change_log.html#b1)
    - [18.6b0](https://black.readthedocs.io/en/stable/change_log.html#id3)
    - [18.5b1](https://black.readthedocs.io/en/stable/change_log.html#id4)
    - [18.5b0](https://black.readthedocs.io/en/stable/change_log.html#id5)
    - [18.4a4](https://black.readthedocs.io/en/stable/change_log.html#a4)
    - [18.4a3](https://black.readthedocs.io/en/stable/change_log.html#a3)
    - [18.4a2](https://black.readthedocs.io/en/stable/change_log.html#a2)
    - [18.4a1](https://black.readthedocs.io/en/stable/change_log.html#a1)
    - [18.4a0](https://black.readthedocs.io/en/stable/change_log.html#a0)
    - [18.3a4](https://black.readthedocs.io/en/stable/change_log.html#id6)
    - [18.3a3](https://black.readthedocs.io/en/stable/change_log.html#id7)
    - [18.3a2](https://black.readthedocs.io/en/stable/change_log.html#id8)
    - [18.3a1](https://black.readthedocs.io/en/stable/change_log.html#id9)
    - [18.3a0](https://black.readthedocs.io/en/stable/change_log.html#id10)
- [Developer reference](https://black.readthedocs.io/en/stable/reference/reference_summary.html)
    - [*Black* classes](https://black.readthedocs.io/en/stable/reference/reference_classes.html)
    - [Enums](https://black.readthedocs.io/en/stable/reference/reference_classes.html#enums)
    - [*Black* functions](https://black.readthedocs.io/en/stable/reference/reference_functions.html)
    - [*Black* exceptions](https://black.readthedocs.io/en/stable/reference/reference_exceptions.html)
- [Authors](https://black.readthedocs.io/en/stable/authors.html)