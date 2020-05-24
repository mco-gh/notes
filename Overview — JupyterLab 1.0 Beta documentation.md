Overview — JupyterLab 1.0 Beta documentation

- [Docs](http://jupyterlab.readthedocs.io/en/latest/index.html) »

- Overview

- [ Edit on GitHub](https://github.com/jupyterlab/jupyterlab//master/docs/source/getting_started/overview.rst)

- [![](../_resources/8577cb401e13403e40520bf45955ca39.png)Jupyter](https://jupyter.org/documentation) |

* * *

# Overview

JupyterLab is the next-generation web-based user interface for Project Jupyter. The beta release series of JupyterLab is stable for daily use.

![](../_resources/d60825ace85fb0b63059fa5d9a3f5b36.png)

JupyterLab enables you to work with documents and activities such as[Jupyter notebooks](http://jupyterlab.readthedocs.io/en/latest/user/notebook.html#notebook), text editors, terminals, and custom components in a flexible, integrated, and extensible manner. You can[arrange](http://jupyterlab.readthedocs.io/en/latest/user/interface.html#interface) multiple documents and activities side by side in the work area using tabs and splitters. Documents and activities integrate with each other, enabling new workflows for interactive computing, for example:

- [Code Consoles](http://jupyterlab.readthedocs.io/en/latest/user/code_console.html#code-console) provide transient scratchpads for running code interactively, with full support for rich output. A code console can be linked to a notebook kernel as a computation log from the notebook, for example.
- [Kernel-backed documents](http://jupyterlab.readthedocs.io/en/latest/user/documents_kernels.html#kernel-backed-documents) enable code in any text file (Markdown, Python, R, LaTeX, etc.) to be run interactively in any Jupyter kernel.
- Notebook cell outputs can be [mirrored into their own tab](http://jupyterlab.readthedocs.io/en/latest/user/notebook.html#cell-output-mirror), side by side with the notebook, enabling simple dashboards with interactive controls backed by a kernel.
- Multiple views of documents with different editors or viewers enable live editing of documents reflected in other viewers. For example, it is easy to have live preview of [Markdown](http://jupyterlab.readthedocs.io/en/latest/user/file_formats.html#markdown), [Delimiter-separated Values](http://jupyterlab.readthedocs.io/en/latest/user/file_formats.html#csv), or [Vega/Vega-Lite](http://jupyterlab.readthedocs.io/en/latest/user/file_formats.html#vega-lite) documents.

JupyterLab also offers a unified model for viewing and handling data formats. JupyterLab understands many file formats (images, CSV, JSON, Markdown, PDF, Vega, Vega-Lite, etc.) and can also display rich kernel output in these formats. See [File and Output Formats](http://jupyterlab.readthedocs.io/en/latest/user/file_formats.html#file-and-output-formats) for more information.

To navigate the user interface, JupyterLab offers [customizable keyboard shortcuts](http://jupyterlab.readthedocs.io/en/latest/user/interface.html#shortcuts) and the ability to use [key maps](http://jupyterlab.readthedocs.io/en/latest/user/interface.html#editor-keymaps)from vim, emacs, and Sublime Text in the text editor.

JupyterLab [extensions](http://jupyterlab.readthedocs.io/en/latest/user/extensions.html#user-extensions) can customize or enhance any part of JupyterLab, including new themes, file editors, and custom components.

JupyterLab is served from the same [server](https://jupyter-notebook.readthedocs.io/en/stable/) and uses the same[notebook document format](http://nbformat.readthedocs.io/en/latest/) as the classic Jupyter Notebook.

## Beta Series and Beyond

The developer API will evolve in beta releases and will stabilize in JupyterLab 1.0. We appreciate feedback on our [GitHub issues page](https://github.com/jupyterlab/jupyterlab/issues)as we evolve towards a stable extension development API for JupyterLab 1.0.

We plan to release JupyterLab 1.0 later in 2018. The beta releases leading up to 1.0 will focus on stabilizing the extension development API, UI/UX improvements, and additional core features. All releases in the beta series will be stable enough for daily usage.

JupyterLab 1.0 will eventually replace the classic Jupyter Notebook. Throughout this transition, the same notebook document format will be supported by both the classic Notebook and JupyterLab.

 [Next ](http://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html)  [ Previous](http://jupyterlab.readthedocs.io/en/latest/index.html)

* * *

© Copyright 2018, Project Jupyter.

The Jupyter Trademark is registered with the U.S. Patent & Trademark Office.  Revision `ba7715ad`.

Built with [Sphinx](http://sphinx-doc.org/) using a [theme](https://github.com/snide/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).