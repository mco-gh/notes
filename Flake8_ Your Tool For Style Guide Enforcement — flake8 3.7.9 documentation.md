Flake8: Your Tool For Style Guide Enforcement — flake8 3.7.9 documentation

# Flake8: Your Tool For Style Guide Enforcement[¶](https://flake8.pycqa.org/en/latest/#flake8-your-tool-for-style-guide-enforcement)

## Quickstart[¶](https://flake8.pycqa.org/en/latest/#quickstart)

### Installation[¶](https://flake8.pycqa.org/en/latest/#installation)

To install **Flake8**, open an interactive shell and run:
python<version>  -m  pip  install  flake8

If you want **Flake8** to be installed for your default Python installation, you can instead use:

python  -m  pip  install  flake8
Note

It is **very** important to install **Flake8** on the *correct* version of Python for your needs. If you want **Flake8** to properly parse new language features in Python 3.5 (for example), you need it to be installed on 3.5 for **Flake8** to understand those features. In many ways, Flake8 is tied to the version of Python on which it runs.

### Using Flake8[¶](https://flake8.pycqa.org/en/latest/#using-flake8)

To start using **Flake8**, open an interactive shell and run:
flake8  path/to/code/to/check.py*# or*flake8  path/to/code/
Note

If you have installed **Flake8** on a particular version of Python (or on several versions), it may be best to instead run 	python<version> -m

	flake8.

If you only want to see the instances of a specific warning or error, you can*select* that error like so:

flake8  --select  E123,W503  path/to/code/
Alternatively, if you want to *ignore* only one specific warning or error:
flake8  --ignore  E24,W504  path/to/code/

Please read our user guide for more information about how to use and configure**Flake8**.

## FAQ and Glossary[¶](https://flake8.pycqa.org/en/latest/#faq-and-glossary)

- [Frequently Asked Questions](https://flake8.pycqa.org/en/latest/faq.html)
    - [When is Flake8 released?](https://flake8.pycqa.org/en/latest/faq.html#when-is-flake8-released)
    - [How can I help Flake8 release faster?](https://flake8.pycqa.org/en/latest/faq.html#how-can-i-help-flake8-release-faster)
    - [What is the next version of Flake8?](https://flake8.pycqa.org/en/latest/faq.html#what-is-the-next-version-of-flake8)
    - [Why does Flake8 use ranges for its dependencies?](https://flake8.pycqa.org/en/latest/faq.html#why-does-flake8-use-ranges-for-its-dependencies)
    - [Should I file an issue when a new version of a dependency is available?](https://flake8.pycqa.org/en/latest/faq.html#should-i-file-an-issue-when-a-new-version-of-a-dependency-is-available)
- [Glossary of Terms Used in Flake8 Documentation](https://flake8.pycqa.org/en/latest/glossary.html)

## User Guide[¶](https://flake8.pycqa.org/en/latest/#user-guide)

All users of **Flake8** should read this portion of the documentation. This provides examples and documentation around **Flake8**’s assortment of options and how to specify them on the command-line or in configuration files.

- [Using Flake8](https://flake8.pycqa.org/en/latest/user/index.html)
    - [Invoking Flake8](https://flake8.pycqa.org/en/latest/user/invocation.html)
    - [Configuring Flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)
    - [Full Listing of Options and Their Descriptions](https://flake8.pycqa.org/en/latest/user/options.html)
    - [Error / Violation Codes](https://flake8.pycqa.org/en/latest/user/error-codes.html)
    - [Selecting and Ignoring Violations](https://flake8.pycqa.org/en/latest/user/violations.html)
    - [Using Plugins For Fun and Profit](https://flake8.pycqa.org/en/latest/user/using-plugins.html)
    - [Using Version Control Hooks](https://flake8.pycqa.org/en/latest/user/using-hooks.html)
    - [Public Python API](https://flake8.pycqa.org/en/latest/user/python-api.html)
- [Flake8 man page](https://flake8.pycqa.org/en/latest/manpage.html)
    - [SYNOPSIS](https://flake8.pycqa.org/en/latest/manpage.html#synopsis)
    - [DESCRIPTION](https://flake8.pycqa.org/en/latest/manpage.html#description)
    - [OPTIONS](https://flake8.pycqa.org/en/latest/manpage.html#options)
    - [EXAMPLES](https://flake8.pycqa.org/en/latest/manpage.html#examples)
    - [SEE ALSO](https://flake8.pycqa.org/en/latest/manpage.html#see-also)
    - [BUGS](https://flake8.pycqa.org/en/latest/manpage.html#bugs)

## Plugin Developer Guide[¶](https://flake8.pycqa.org/en/latest/#plugin-developer-guide)

If you’re maintaining a plugin for **Flake8** or creating a new one, you should read this section of the documentation. It explains how you can write your plugins and distribute them to others.

- [Writing Plugins for Flake8](https://flake8.pycqa.org/en/latest/plugin-development/index.html)
    - [Getting Started](https://flake8.pycqa.org/en/latest/plugin-development/index.html#getting-started)

## Contributor Guide[¶](https://flake8.pycqa.org/en/latest/#contributor-guide)

If you are reading **Flake8**’s source code for fun or looking to contribute, you should read this portion of the documentation. This is a mix of documenting the internal-only interfaces **Flake8** and documenting reasoning for Flake8’s design.

- [Exploring Flake8’s Internals](https://flake8.pycqa.org/en/latest/internal/index.html)
    - [Contributing to Flake8](https://flake8.pycqa.org/en/latest/internal/contributing.html)
    - [Writing Documentation for Flake8](https://flake8.pycqa.org/en/latest/internal/writing-documentation.html)
    - [Writing Code for Flake8](https://flake8.pycqa.org/en/latest/internal/writing-code.html)
    - [Releasing Flake8](https://flake8.pycqa.org/en/latest/internal/releases.html)
    - [What Happens When You Run Flake8](https://flake8.pycqa.org/en/latest/internal/start-to-finish.html)
    - [How Checks are Run](https://flake8.pycqa.org/en/latest/internal/checker.html)
    - [Command Line Interface](https://flake8.pycqa.org/en/latest/internal/cli.html)
    - [Built-in Formatters](https://flake8.pycqa.org/en/latest/internal/formatters.html)
    - [Option and Configuration Handling](https://flake8.pycqa.org/en/latest/internal/option_handling.html)
    - [Plugin Handling](https://flake8.pycqa.org/en/latest/internal/plugin_handling.html)
    - [Utility Functions](https://flake8.pycqa.org/en/latest/internal/utils.html)

## Release Notes and History[¶](https://flake8.pycqa.org/en/latest/#release-notes-and-history)

- [Release Notes and History](https://flake8.pycqa.org/en/latest/release-notes/index.html)
    - [3.x Release Series](https://flake8.pycqa.org/en/latest/release-notes/index.html#x-release-series)
    - [2.x Release Series](https://flake8.pycqa.org/en/latest/release-notes/index.html#id1)
    - [1.x Release Series](https://flake8.pycqa.org/en/latest/release-notes/index.html#id2)
    - [0.x Release Series](https://flake8.pycqa.org/en/latest/release-notes/index.html#id3)

## General Indices[¶](https://flake8.pycqa.org/en/latest/#general-indices)

- [Index](https://flake8.pycqa.org/en/latest/genindex.html)
- [Index of Documented Public Modules](https://flake8.pycqa.org/en/latest/py-modindex.html)
- [Glossary of terms](https://flake8.pycqa.org/en/latest/glossary.html#glossary)