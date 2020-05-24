Welcome to papermill — papermill 1.0.0 documentation

# Welcome to papermill[¶](https://papermill.readthedocs.io/en/latest/#welcome-to-papermill)

[![papermill.png](../_resources/087bbac58300ac5d38e541f4c3d661f2.png)](https://travis-ci.org/nteract/papermill)[![coverage.png](../_resources/1f9f52f54a712dea1ce2c030e34a7b7a.png)](https://codecov.io/github/nteract/papermill?branch=master)[![?version=latest](../_resources/157f1a87b7445d54ab29487382df1f42.png)](http://papermill.readthedocs.io/en/latest/?badge=latest)[![ybwovtw2](../_resources/2583c310a4b5ed37366252eeff6369f7.png)](https://mybinder.org/v2/gh/nteract/papermill/master?filepath=binder%2Fprocess_highlight_dates.ipynb)[![y7uz2eh9](../_resources/a2b7e4e8878bf8a69d8142416cefcf73.png)](https://mybinder.org/v2/gh/nteract/papermill/master?filepath=binder%2Fcli-simple%2Fcli_example.ipynb)[![code style-black-000000.png](../_resources/043096fba4312cdd2d0efb73b9212543.png)](https://github.com/ambv/black)

**Papermill** is a tool for parameterizing and executing Jupyter Notebooks.
Papermill lets you:

- **parameterize** notebooks
- **execute** notebooks

This opens up new opportunities for how notebooks can be used. For example:

- Perhaps you have a financial report that you wish to run with different values on the first or last day of a month or at the beginning or end of the year, **using parameters** makes this task easier.
- Do you want to run a notebook and depending on its results, choose a particular notebook to run next? You can now programmatically**execute a workflow** without having to copy and paste from notebook to notebook manually.

## Python Version Support[¶](https://papermill.readthedocs.io/en/latest/#python-version-support)

This library will support python 2.7 and 3.5+ until end-of-life for python 2 in 2020. After which python 2 support will halt and only 3.x version will be maintained.

## Documentation[¶](https://papermill.readthedocs.io/en/latest/#documentation)

These pages guide you through the installation and usage of papermill.

- [Installation](https://papermill.readthedocs.io/en/latest/installation.html)
- [Usage](https://papermill.readthedocs.io/en/latest/usage-workflow.html)
- [Parameterize](https://papermill.readthedocs.io/en/latest/usage-parameterize.html)
- [Execute](https://papermill.readthedocs.io/en/latest/usage-execute.html)
- [Store](https://papermill.readthedocs.io/en/latest/usage-store.html)
- [Command Line Interface](https://papermill.readthedocs.io/en/latest/usage-cli.html)
- [Extending papermill](https://papermill.readthedocs.io/en/latest/extending-overview.html)

## API Reference[¶](https://papermill.readthedocs.io/en/latest/#api-reference)

If you are looking for information about a specific function, class, or method, this documentation section will help you.

- [Reference](https://papermill.readthedocs.io/en/latest/reference/index.html)
    - [CLI](https://papermill.readthedocs.io/en/latest/reference/papermill-cli.html)
        - [papermill.cli](https://papermill.readthedocs.io/en/latest/reference/papermill-cli.html#module-papermill.cli)
        - [Command Line options](https://papermill.readthedocs.io/en/latest/reference/papermill-cli.html#command-line-options)
    - [Workflow](https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html)
        - [papermill.engines](https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html#module-papermill.engines)
        - [papermill.execute](https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html#module-papermill.execute)
        - [papermill.preprocess](https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html#module-papermill.preprocess)
    - [Language Translators](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html)
        - [Translators](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html#translators)
        - [Python](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html#python)
        - [R](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html#r)
        - [Julia](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html#julia)
        - [Scala](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html#scala)
        - [Functions](https://papermill.readthedocs.io/en/latest/reference/papermill-translators.html#functions)
    - [Input / Output](https://papermill.readthedocs.io/en/latest/reference/papermill-io.html)
        - [papermill.iorw](https://papermill.readthedocs.io/en/latest/reference/papermill-io.html#module-papermill.iorw)
    - [Storage](https://papermill.readthedocs.io/en/latest/reference/papermill-storage.html)
        - [Azure](https://papermill.readthedocs.io/en/latest/reference/papermill-storage.html#azure)
        - [AWS](https://papermill.readthedocs.io/en/latest/reference/papermill-storage.html#aws)
    - [Utilities](https://papermill.readthedocs.io/en/latest/reference/papermill-utilities.html)
        - [Utils](https://papermill.readthedocs.io/en/latest/reference/papermill-utilities.html#module-papermill.utils)
        - [Exceptions](https://papermill.readthedocs.io/en/latest/reference/papermill-utilities.html#module-papermill.exceptions)
        - [Log](https://papermill.readthedocs.io/en/latest/reference/papermill-utilities.html#module-papermill.log)
- [papermill.tests package](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html)
    - [Submodules](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#submodules)
    - [papermill.tests.test_abs module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-abs-module)
    - [papermill.tests.test_adl module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-adl-module)
    - [papermill.tests.test_cli module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-cli-module)
    - [papermill.tests.test_conf module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-conf-module)
    - [papermill.tests.test_engines module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#module-papermill.tests.test_engines)
    - [papermill.tests.test_exceptions module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-exceptions-module)
    - [papermill.tests.test_execute module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#module-papermill.tests.test_execute)
    - [papermill.tests.test_gcs module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#module-papermill.tests.test_gcs)
    - [papermill.tests.test_iorw module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-iorw-module)
    - [papermill.tests.test_parameterize module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#module-papermill.tests.test_parameterize)
    - [papermill.tests.test_preprocessor module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#module-papermill.tests.test_preprocessor)
    - [papermill.tests.test_s3 module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-s3-module)
    - [papermill.tests.test_translators module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-translators-module)
    - [papermill.tests.test_utils module](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#papermill-tests-test-utils-module)
    - [Module contents](https://papermill.readthedocs.io/en/latest/reference/papermill.tests.html#module-papermill.tests)

## Indices and tables[¶](https://papermill.readthedocs.io/en/latest/#indices-and-tables)

- [Index](https://papermill.readthedocs.io/en/latest/genindex.html)
- [Module Index](https://papermill.readthedocs.io/en/latest/py-modindex.html)
- [Search Page](https://papermill.readthedocs.io/en/latest/search.html)