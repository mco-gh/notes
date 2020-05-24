Python in Visual Studio Code – November 2019 Release | Python

# Python in Visual Studio Code – November 2019 Release

![e0d7650ba7150f535076b3cd0a1c5846](../_resources/261bf0b08c94e3ca5b6d2e8562a94c4f.png)
Luciana

November 18th, 2019

We are pleased to announce that the November 2019 release of the Python Extension for Visual Studio Code is now available. You can  [download the Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Marketplace, or install it directly from the extension gallery in Visual Studio Code. If you already have the Python extension installed, you can also get the latest update by restarting Visual Studio Code. You can learn more about  [Python support in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)   in the documentation.

In this release we focused mostly on product quality. We closed a total of 60 issues, 39 of them being bug fixes. However, we’re also pleased to deliver delightful features such as:

- Add imports “quick fix” when using the Python Language Server
- Altair plot support
- Line numbers in the Notebook Editor.

If you’re interested, you can check the full list of improvements in our [changelog](https://github.com/Microsoft/vscode-python/blob/master/CHANGELOG.md).

# Add Imports “Quick Fix” when using the Python Language Server

We’re excited to announce that we have brought the magic of automatic imports to Python developers in VS Code by way of an add imports quick fix. Automatic imports functionality was one of the most requested features on our GitHub repo ([GH21](https://github.com/microsoft/vscode-python/issues/21)), and when you enable the Microsoft Language Server, you will get this new functionality. To enable the Language Server, add the setting *“python.jediEnabled**”*: false[toyour settings.json file](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations).

The add imports quick fix within VS Code is triggered via a code action lightbulb. To use the quick fix, begin typing a package name within the editor for which you do not have an import statement at the header of the file. You will notice that if a code action is available for this package (i.e. you have a module installed within your environment with the name you’ve supplied), a yellow squiggle will appear. If you hover over that text, a code action lightbulb will appear indicating that an ’import’ code action is available for the package. You’ll see a list of potential imports (again, based on what’s installed within your environment), allowing you to choose the package that you wish to import.

[![Nov19-AutoImportsPathZoom.gif](../_resources/82c970c42cdc7bbe20ae6778e7ee8578.gif)](https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2019/11/Nov19-AutoImportsPathZoom.gif)

The add imports code action will also recognize some of the most popular abbreviations for the following Python packages: numpy as np, tensorflow as tf, pandas as pd, matplotlib.pyplot as plt, matplotlib as mpl, math as m, scipy.io as spio, and scipy as sp.

[![Nov19-AutoImportsFull.gif](../_resources/12e7da6a51254b2085c7d5b935a49ef2.gif)](https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2019/11/Nov19-AutoImportsFull.gif)

The import suggestion list is ordered such that all import statements that appear at the top of the list are package (or module) imports; those that appear lower in the list are import statements for additional modules and/or members (e.g. classes, objects, etc.) from specified packages.

[![Nov19-ImportSys-1.png](../_resources/84690349860159e928be0d6d7a525a21.png)](https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2019/11/Nov19-ImportSys-1.png)

Make sure you have linting enabled since this functionality is tied to the Language Server linting capability. You can enable linting by opening the Command Palette (**View**  **> Command Palette…**), running the “Python: Enable Linting” command and selecting “On” in the drop-down menu.

# Altair plots support

The Notebook Editor and the Python Interactive window now both support rendering plots built with [Altair](https://altair-viz.github.io/index.html),  a declarative statistical visualization library for Python.

[![Nov19-Altair-768x704.png](../_resources/14dc365cefd20b9144ec101df26fc59c.png)](https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2019/11/Nov19-Altair.png)

# Line Numbers in the Notebook Editor

Line numbers are now supported in the notebook editor. On selected code cells, you can toggle the line numbers by pressing the “L” key.

[![Nov19-Lines-768x204.png](../_resources/8b1c47810840c83344f90012606adc05.png)](https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2019/11/Nov19-Lines.png)

# Other Changes and Enhancements

We have also added small enhancements and fixed issues requested by users that should improve your experience working with Python in Visual Studio Code. Some notable changes include:

- Fix running a unittest file to not execute only the first test. (thanks [Nikolay Kondratyev](https://github.com/kondratyev-nv/)). ([#4567](https://github.com/Microsoft/vscode-python/issues/4567))
- Added commands translation for Farsi and Turkish (thanks [Nikronic](https://github.com/Nikronic)). ([#8092](https://github.com/Microsoft/vscode-python/issues/8092))
- Added command translations for Turkish (thanks [alioguzhan](https://github.com/alioguzhan/)). ([#8320](https://github.com/Microsoft/vscode-python/issues/8320))
- Place all plots on a white background regardless of theme. ([#8000](https://github.com/Microsoft/vscode-python/issues/8000))

We are continuing to A/B test new features, so if you see something different that was not announced by the team, you may be part of the experiment! To see if you are part of an experiment, you can check the first lines in the Python extension output channel. If you wish to opt-out of A/B testing, you can open the user settings.json file (**View **> **Command Palette…** and run **Preferences: Open Settings (JSON)**) and set the “*python.experiments.enabled*” setting to *false*.

Be sure to [download the Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code now to try out the above improvements. If you run into any problems, [please file an issue](https://github.com/microsoft/vscode-python/issues/new/choose) on the [Python VS Code GitHub](https://github.com/Microsoft/vscode-python) page.

![e0d7650ba7150f535076b3cd0a1c5846](../_resources/40fc89b8b3f9584051e34101f5df8c78.png)

##### [Luciana de Melo e Abud](https://devblogs.microsoft.com/python/author/luabudmicrosoft-com/)

Program Manager, Python extension in Visual Studio Code

**Follow Luciana**   [**](https://twitter.com/luumelo14)[**](https://github.com/luabud)[**](https://devblogs.microsoft.com/python/author/luabudmicrosoft-com/feed/)