Python in Visual Studio Code

[(L)](https://github.com/Microsoft/vscode-docs/blob/master/docs/languages/python.md)

# Python in Visual Studio Code

Working with Python in Visual Studio Code, using the [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), is simple, fun, and productive. The extension works with different Python interpreters as well as Anaconda. It leverages all of VS Code's power to provide auto complete and IntelliSense, linting, debugging, and unit testing, along with the ability to easily switch between Python environments, including virtual and conda environments.

## Install Python and the Python extension

The [tutorial](https://code.visualstudio.com/docs/python/python-tutorial) guides you through installing Python and using the extension.

## Autocomplete and IntelliSense

The Python extension supports code completion and Intellisense. [Intellisense](https://code.visualstudio.com/docs/editor/intellisense) is a general term for a number of features, including intelligent code completion (in-context method and variable suggestions) across all your files and for built-in and third-party modules.

IntelliSense quickly shows methods, class members, and documentation as you type, and you can trigger completions at any time with ⌃Space.

[python_python-debugging-placeholder.png](../_resources/81be11da281ab19c7007a464c3703d7f.bin)

## Linting

Linting analyzes your Python code for potential errors, making it easy to navigate to and correct different problems.

The Python extension can apply a number of different linters including Pylint, Pep8, Flake8, mypy, pydocstyle, prospector, and pylama. See [Linting](https://code.visualstudio.com/docs/python/linting).

## Debugging

No more `print` statement debugging! Set breakpoints, inspect data, and use the debug console as you run your program step by step. Debug a number of different type of Python applications, including multi-threaded, web, and remote applications.

For Python-specific details, including setting up your `launch.json` configuration, see [Debugging](https://code.visualstudio.com/docs/python/debugging). General VS Code debugging information is found in the [debugging document](https://code.visualstudio.com/docs/editor/debugging).

## Snippets

Snippets take productivity to the next level. You can configure [your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) and use snippets provided by an extension. Snippets appear in the same way as code completion ⌃Space.

## Environments

The Python extension automatically detects Python interpreters that are installed in standard locations. It also detects conda environments as well as virtual environments in the workspace folder. See [Configuring Python environments](https://code.visualstudio.com/docs/python/environments).

The current environment is shown on the left side of the Visual Studio Code status bar:

![](../_resources/595f4303e2ba41181bc435bbde9744d1.png)

This environment is used for IntelliSense, auto-completions, linting, formatting, and any other language-related feature other than debugging. It is also activated when you use [run Python in a terminal](https://code.visualstudio.com/docs/languages/python#_run-python-in-the-terminal).

To change the current interpreter, which includes switching to conda or virtual environments, click the interpreter on the status bar or use the **Python: Select Interpreter** command.

![](../_resources/08ee9afae7031c3a5562eb1dab4bce4f.png)

VS Code then prompts you with a list of detected environments as well as any you've added manually to your user settings (see [Configuring Python environments](https://code.visualstudio.com/docs/python/environments)).

## Run Python in the Terminal

The Python extension provides shortcuts to quickly run Python code in the current interpreter:

- From the editor: right-click anywhere in the editor and select **Run Python File in Terminal**. If invoked on a selection, only that selection is run.
- From Explorer: right-click a Python file and select **Run Python File in Terminal**.

You can also use the **Python: Create Terminal** command to create a terminal with the current environment activated.

## Unit testing

The Python extension supports [unit testing](https://code.visualstudio.com/docs/python/unit-testing) with the unittest, pytest, and nose test frameworks.

To run unit tests, you enable one of the frameworks in settings. Each framework also has specific settings, such as arguments that identify paths and patterns for test discovery.

Once discovered, VS Code provides a variety of commands (on the status bar, the command palette, and elsewhere) to run and debug tests, including ability to run individual test files and individual methods.

## Configuration

The Python extension provides a wide variety of settings for its various features. These are described on their relevant topics, such as [Editing code](https://code.visualstudio.com/docs/python/editing), [Linting](https://code.visualstudio.com/docs/python/linting), [Debugging](https://code.visualstudio.com/docs/python/debugging), and [Unit Testing](https://code.visualstudio.com/docs/python/unit-testing). The complete list is found in the [Settings reference](https://code.visualstudio.com/docs/python/settings-reference).

## Other popular Python extensions

Additional Python language support can be added to VS Code by installing other popular Python extensions. For Jupyter support, we recommend the "Jupyter" extension from Don Jayamanne.

1. Open the **Extensions** view (⇧⌘X).
2. Filter the extension list by typing 'python'.

[ ![Microsoft.VisualStudio.Services.Icons.Default](../_resources/1854b08961029295351e3d80e6f0d40d.png)   Python  9545.2K ms-python      Linting, Debugging (multi-threaded, remote), Inte...](https://marketplace.visualstudio.com/items?itemName=ms-python.python)[ ![Microsoft.VisualStudio.Services.Icons.Default](../_resources/bc61c007fc4b978c881a7a241a32ced3.png)   Code Runner  2993.8K formulahendry      Run C, C++, Java, JS, PHP, Python, Perl, Ruby, Go...](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)[ ![Microsoft.VisualStudio.Services.Icons.Default](../_resources/3e787b1c610f27459d3f3229c1edf80b.png)   MagicPython  700.9K magicstack      Syntax highlighter for cutting edge Python.](https://marketplace.visualstudio.com/items?itemName=magicstack.MagicPython)[ ![Microsoft.VisualStudio.Services.Icons.Default](../_resources/03968e0a8a2a48a69563bc140f75efca.png)   Python for VSCode  517.0K tht13      Python language extension for vscode](https://marketplace.visualstudio.com/items?itemName=tht13.python)

The extensions shown above are dynamically queried. Click on an extension tile above to read the description and reviews to decide which extension is best for you. See more in the [Marketplace](https://marketplace.visualstudio.com/vscode).

## Next steps

- [Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) - Walk through the core features of Python in VS Code.
- [Editing Python](https://code.visualstudio.com/docs/python/editing) - Learn about auto-completion, formatting, and refactoring for Python.
- [Basic Editing](https://code.visualstudio.com/docs/editor/codebasics) - Learn about the powerful VS Code editor.
- [Code Navigation](https://code.visualstudio.com/docs/editor/editingevolved) - Move quickly through your source code.

### Was this documentation helpful?

Last updated on 02/14/2018