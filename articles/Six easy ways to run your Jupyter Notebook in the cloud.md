Six easy ways to run your Jupyter Notebook in the cloud

March 28, 2019 · [Python](https://www.dataschool.io/tag/python/)

# Six easy ways to run your Jupyter Notebook in the cloud

There are many ways to share a **static Jupyter notebook** with others, such as posting it on GitHub or sharing an nbviewer link. However, the recipient can only interact with the notebook file if they already have the Jupyter Notebook environment installed.

But what if you want to share a **fully interactive Jupyter notebook** that doesn't require any installation? Or, you want to create your own Jupyter notebooks without installing anything on your local machine?

In this post, I'm going to review six services you can use to **easily run your Jupyter notebook in the cloud**. All of them have the following characteristics:

- They don't require you to install anything on your local machine.
- They are completely free (or they have a free plan).
- They give you access to the Jupyter Notebook environment (or a Jupyter-like environment).
- They allow you to import and export notebooks using the standard .ipynb file format.
- They support the Python language (and most support other languages as well).

Since all of these are cloud-based services, none of them will work for you if you are restricted to working with your data on-premise.

## Table of Contents

- [Criteria for comparison](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#criteriaforcomparison)
- **In-depth reviews:**

    1. [Binder](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#1binder)

    2. [Kaggle Kernels](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#2kagglekernels)

    3. [Google Colaboratory (Colab)](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#3googlecolaboratorycolab)

    4. [Microsoft Azure Notebooks](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#4microsoftazurenotebooks)

    5. [CoCalc](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#5cocalc)

    6. [Datalore](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#6datalore)

- [How to choose the right service for you](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#howtochoosetherightserviceforyou)
- [Similar services which were not reviewed](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#similarserviceswhichwerenotreviewed)
- [My fact-checking process](https://www.dataschool.io/cloud-services-for-jupyter-notebook/#myfactcheckingprocess)

**Note:** If you just want a quick summary, check out the [comparison table](https://docs.google.com/spreadsheets/d/12thaaXg1Idr3iWST8QyASNDs08sjdPd6m9mbCGtHFn0/edit?usp=sharing).

* * *

## Criteria for comparison

Here are the criteria on which I compared each of the six services:

**Supported languages:** Does this service support any programming languages other than Python?

**Ability to install packages:** Does this service allow you to install additional packages (or a particular version of a package), beyond the ones that are already installed?

**Interface similarity:** If the service provides a "Jupyter-like" interface (rather than the native Jupyter interface), how similar is its interface to Jupyter? (This makes it easier for existing Jupyter users to transition to this service.)

**Keyboard shortcuts:** Does this service use the same keyboard shortcuts as the Jupyter Notebook?

**Missing features:** Is there anything that the Jupyter Notebook can do that this service does not support?

**Added features:** Is there anything this service can do that the Jupyter Notebook does not support?

**Ease of working with datasets:** How easy does this service make it to work with your own datasets?

**Internet access:** Does this service give you Internet access from within the Notebook, so that you can read data from URLs when necessary?

**Ability to work privately:** Does this service allow you to keep your work private?

**Ability to share publicly:** Does this service provide a way for you to share your work publicly?

**Ability to collaborate:** Does this service allow you to invite someone to collaborate on a notebook, and can the collaboration occur in real-time?

**Performance of the free plan:** What computational resources (RAM and CPU) does this service provide? Does it give you access to a GPU (which is useful for deep learning)? How much disk space is included? How long can a session run?

**Ability to upgrade for better performance:** Can you pay for this service in order to access more computational resources?

**Documentation and technical support:** Is the service well-documented? Can you get in touch with someone if you run into a problem?

* * *

## 1. Binder

![](../_resources/9ffac80f630dd13baf14dbcbd110b3b5.png)

[Binder](https://mybinder.org/) is a service provided by the Binder Project, which is a member of the Project Jupyter open source ecosystem. It allows you to input the URL of any public Git repository, and it will open that repository within the native Jupyter Notebook interface. You can run any notebooks in the repository, though any changes you make will not be saved back to the repository. You don't have to create an account with Binder and you don't need to be the owner of the repository, though the repository must include a configuration file that specifies its package requirements.

**Supported languages:** Python (2 and 3), R, Julia, and any other languages [supported by Jupyter](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

**Ability to install packages:** You can specify your exact package requirements using a [configuration file](https://mybinder.readthedocs.io/en/latest/config_files.html) (such as `environment.yml` or `requirements.txt`).

**Interface similarity:** Binder uses the native Jupyter Notebook interface.

**Keyboard shortcuts:** Binder uses all of the same keyboard shortcuts as Jupyter.

**Missing features:** None.
**Added features:** None.

**Ease of working with datasets:** If your dataset is in the same Git repository, then it will automatically be available within Binder. If your dataset is not in that repository but is available at any public URL, then you can add a [special file](https://github.com/binder-examples/getting-data) to the repository telling Binder to download your dataset. However, Binder does not support accessing private datasets.

**Internet access:** Yes.

**Ability to work privately:** No, since it only works with public Git repositories.

**Ability to share publicly:** Yes. You can share a URL that goes directly to [your Binder](https://mybinder.org/v2/gh/justmarkham/pycon-2018-tutorial/master?filepath=tutorial.ipynb), or someone can run your notebooks using the Binder website (as long as they know the URL of your Git repository).

**Ability to collaborate:** No. If you want to work with someone on the same notebook and your repository is hosted on GitHub, then you can instead use the normal pull request workflow.

**Performance of the free plan:** You will have access to up to 2 GB of RAM. There is no specific limit to the amount of disk space, though they ask you not to include "very large files" (more than a few hundred megabytes). Binder can be [slow to launch](https://mybinder.readthedocs.io/en/latest/faq.html#what-factors-influence-how-long-it-takes-a-binder-session-to-start), especially when it's run on a newly updated repository. Sessions will shut down after 20 minutes of inactivity, though they can run for 12 hours or longer. Binder has other [usage guidelines](https://mybinder.readthedocs.io/en/latest/user-guidelines.html), including a limit of 100 simultaneous users for any given repository.

**Ability to upgrade for better performance:** No. However, you do have the option of setting up your own [BinderHub](https://binderhub.readthedocs.io/en/latest/) deployment, which can provide the same functionality as Binder while allowing you to customize the environment (such as increasing the computational resources or allowing private files).

**Documentation and technical support:** Binder has extensive [documentation](https://mybinder.readthedocs.io/en/latest/). Community support is available via [Gitter chat](https://gitter.im/jupyterhub/binder) and a [Discourse forum](https://discourse.jupyter.org/), and product issues are tracked on [GitHub](https://github.com/jupyterhub/binderhub/issues).

**Conclusion:** If your notebooks are already stored in a public GitHub repository, Binder is the easiest way to enable others to interact with them. Users don't have to create an account, and they'll feel right at home if they already know how to use the Jupyter Notebook. However, you'll want to keep the performance limitations and user limits in mind!

* * *

## 2. Kaggle Kernels

![](../_resources/132a40718741bba2b8f16c8fc6b3bfa1.png)

[Kaggle](https://www.kaggle.com/) is best known as a platform for data science competitions. However, they also provide a free service called [Kernels](https://www.kaggle.com/kernels) that can be used independently of their competitions. After creating a Kaggle account (or logging in with Google or Facebook), you can create a Kernel that uses either a notebook or scripting interface, though I'm focusing on the notebook interface below.

**Supported languages:** Python (3 only) and R.

**Ability to install packages:**  [Hundreds of packages](https://github.com/Kaggle/docker-python) come pre-installed, and you can [install additional packages](https://www.kaggle.com/docs/kernels#modifying-a-kernel-specific-environment) using pip or by specifying the GitHub repository of a package. However, any additional packages you install will need to be reinstalled at the start of every session. Alternatively, you can ask Kaggle to include additional packages in their default installation.

**Interface similarity:** Visually, the Kernels interface looks quite different from the Jupyter interface. There's no menu bar or toolbar at the top of the screen, there's a collapsible sidebar on the right for adjusting settings, and there's a console docked below the notebook. However, working in the Kernels notebook actually feels very similar to working in the Jupyter Notebook, especially if you're comfortable with Jupyter's keyboard shortcuts. Also, note that a [redesigned interface](https://www.kaggle.com/product-feedback/83336) (shown in the screenshot above) will soon be released, which is more similar to the Jupyter interface and includes a simple menu bar.

**Keyboard shortcuts:** Kernels uses all of the same keyboard shortcuts as Jupyter.

**Missing features:**

- Because Kernels doesn't (yet) include a menu bar or a toolbar, many actions can only be done using keyboard shortcuts or the command palette.
- You can't download your notebook into other useful formats such as a Python script, HTML webpage, or Markdown file.

**Added features:**

- Kernels includes a lightweight version control system. Every time you want to save your work, there's a "commit" button which runs the entire notebook from top to bottom and adds a new version to the history. (You can keep working while this process takes place, which is essential for long-running notebooks.) Although you can't name the versions, you can display the "diff" between any two versions.
- Kernels allows you to selectively hide the input and/or output of any code cell, which makes it easy to customize the presentation of your notebook.

**Ease of working with datasets:** You can upload a dataset to Kaggle from your local computer, a URL, or a [GitHub repository](https://www.kaggle.com/product-feedback/77211), and it will be hosted for free by another Kaggle service called [Datasets](https://www.kaggle.com/datasets). You can make the dataset private or public. Any dataset you upload, as well as any public dataset uploaded by a Kaggle user, can be accessed by any of your Kernels. The maximum size of each dataset is 20 GB, and a single Kernel can access multiple datasets.

**Internet access:** Yes.
**Ability to work privately:** Yes.

**Ability to share publicly:** Yes. If you choose to make your Kernel [public](https://www.kaggle.com/justmarkham/tutorial), anyone can access it without creating a Kaggle account, and anyone with a Kaggle account can comment on your Kernel or copy it to their own account. Additionally, Kaggle also provides you with a [public profile page](https://www.kaggle.com/justmarkham), which displays all of your public Kernels and datasets.

**Ability to collaborate:** Yes. You can keep your Kernel private but invite specific Kaggle users to view or edit it. There's no real-time collaboration: It's more like working on separate copies of the Kernel, except that all commits are added to the same version history.

**Performance of the free plan:** You can access either a 4-core CPU with 17 GB of RAM, or a 2-core CPU with 14 GB of RAM plus a [GPU](https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu). You will have 5 GB of "saved" disk space and 17 GB of "temporary" disk space, though any disk space used by your dataset does not count towards these figures. Sessions will shut down after 60 minutes of inactivity, though they can run for up to 9 hours.

**Ability to upgrade for better performance:** No.

**Documentation and technical support:** Kernels has adequate [documentation](https://www.kaggle.com/docs/kernels). Support is available via a [contact form](https://www.kaggle.com/contact) and a [forum](https://www.kaggle.com/product-feedback).

**Conclusion:** As long as you're comfortable with a slightly cluttered interface (which has already been improved in the [redesign](https://www.kaggle.com/product-feedback/83336)), you'll have access to a high-performance environment in which it's easy to work with your datasets and share your work publicly (or keep it private). The included version control and collaboration features are also nice additions, though neither are fully-featured.

* * *

## 3. Google Colaboratory (Colab)

![](../_resources/cc5d092c63dc8e0f9d93f47b942cb9d7.png)

[Google Colaboratory](https://colab.research.google.com/), usually referred to as "Google Colab," is available to anyone with a Google account. As long as you are signed into Google, you can quickly get started by creating an empty notebook, uploading an existing notebook, or importing a notebook from any public GitHub repository. Your Colab notebooks are automatically saved in a special folder in your Google Drive, and you can even create new notebooks directly from Drive.

**Supported languages:** Python (2 and 3) and [Swift](https://github.com/tensorflow/swift/blob/master/Usage.md) (which was added in January 2019). Kernels can also be installed for other languages, though the installation process varies by language and is not well-documented.

**Ability to install packages:** Hundreds of packages come pre-installed, and you can [install additional packages](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb) using pip. However, any additional packages you install will need to be reinstalled at the start of every session.

**Interface similarity:** Visually, the Colab interface looks quite similar to the Jupyter interface. However, working in Colab actually feels very dissimilar to working in the Jupyter Notebook:

- Most of the menu items are different.
- Colab has changed some of the standard terminology ("runtime" instead of "kernel", "text cell" instead of "markdown cell", etc.)
- Colab has invented new concepts that you have to understand, such as "playground mode."
- Command mode and Edit mode in Colab work differently than they do in Jupyter.

**Keyboard shortcuts:** In Colab, most of the single letter keyboard shortcuts used by Jupyter (such as "a" to "insert cell above") have been changed to a multi-step process ("Ctrl+m" followed by "a"), though Colab does allow you to customize the shortcuts.

**Missing features:**

- Because the Colab menu bar is missing some items and the toolbar is kept very simple, some actions can only be done using keyboard shortcuts.
- You can't download your notebook into other useful formats such as an HTML webpage or Markdown file (though you can download it as a Python script).

**Added features:**

- Colab includes a lightweight version control system. It frequently saves the current state of your notebook, and you can browse through the revision history. However, you can't display the "diff" between versions, which means that you would have to do any comparisons manually.
- Colab allows you to add [form fields](https://colab.research.google.com/notebooks/forms.ipynb) to your notebook, which enables you to parameterize your code in an interactive way. However, these fields only work within Colab.
- When you create a section heading in your notebook, Colab makes every section collapsible and automatically creates a "table of contents" in the sidebar, which makes large notebooks easier to navigate.

**Ease of working with datasets:** You can upload a dataset to use within a Colab notebook, but it will automatically be deleted once you end your session. Alternatively, you can allow Colab to read files from your Google Drive, though it's [more complicated](https://colab.research.google.com/notebooks/snippets/drive.ipynb) than it should be. Colab also includes [connectors](https://colab.research.google.com/notebooks/io.ipynb) to other Google services, such as Google Sheets and Google Cloud Storage.

**Internet access:** Yes.
**Ability to work privately:** Yes.

**Ability to share publicly:** Yes. If you choose to make your notebook [public](https://colab.research.google.com/drive/1CLkPLk_nkGXxBnAXEPi26g19wjOCYoLg) and you share the link, anyone can access it without creating a Google account, and anyone with a Google account can copy it to their own account. Additionally, you can authorize Colab to save a copy of your notebook to GitHub or Gist and then share it from there.

**Ability to collaborate:** Yes. You can keep your notebook private but invite specific people to view or edit it (using Google's familiar sharing interface). You and your collaborator(s) can edit the notebook at the same time and see each other's changes, as well as add comments for each other (similar to Google Docs), though there's a 30-second lag between when you make changes and when collaborators will see them. Also, you are not actually sharing your environment with your collaborators (meaning there is no syncing of what code has been run), which significantly limits the usefulness of near real-time collaboration.

**Performance of the free plan:** Colab does give you access to a [GPU](https://colab.research.google.com/notebooks/gpu.ipynb) or a [TPU](https://colab.research.google.com/notebooks/tpu.ipynb). Otherwise, Google does not provide any specifications for their environments. If you connect Colab to Google Drive, that will give you up to 15 GB of disk space for storing your datasets. Sessions will shut down after 60 minutes of inactivity, though they can run for up to 12 hours.

**Ability to upgrade for better performance:** No. However, you do have the option of [connecting to a local runtime](https://research.google.com/colaboratory/local-runtimes.html), which allows you to execute code on your local hardware and access your local file system.

**Documentation and technical support:** Colab has minimal documentation, which is contained within an [FAQ page](https://research.google.com/colaboratory/faq.html) and a variety of [sample notebooks](https://colab.research.google.com/notebooks/welcome.ipynb). Support is available via [GitHub issues](https://github.com/googlecolab/colabtools/issues), and community support is available via [Stack Overflow](https://stackoverflow.com/questions/tagged/google-colaboratory).

**Conclusion:** The greatest strength of Colab is that it's easy to get started, since most people already have a Google account, and it's easy to share notebooks, since the sharing functionality works the same as Google Docs. However, the cumbersome keyboard shortcuts and the difficulty of working with datasets are significant drawbacks. The ability to collaborate on the same notebook is useful, but less useful than it could be since you're not sharing an environment.

* * *

## 4. Microsoft Azure Notebooks

![](../_resources/afc2946d41965de9435b9f21abdb4337.png)

To get started with [Azure Notebooks](https://notebooks.azure.com/), you first sign in with a Microsoft or Outlook account (or create one). The next step is to create a "project", which is structured identically to a GitHub repository: it can contain one or more notebooks, Markdown files, datasets, and any other file you want to create or upload, and all of these can be organized into folders. Also like GitHub, you can initialize a project with a README file, which will automatically be displayed on the project page. If your work is already stored on GitHub, you can import the entire repository directly into a project.

**Supported languages:** Python (2 and 3), R, and F#.

**Ability to install packages:** Hundreds of packages come pre-installed, you can [install additional packages](https://docs.microsoft.com/en-us/azure/notebooks/install-packages-jupyter-notebook) using pip or conda, and you can specify your exact package requirements using a [configuration file](https://docs.microsoft.com/en-us/azure/notebooks/quickstart-create-jupyter-notebook-project-environment) (such as `environment.yml` or `requirements.txt`).

**Interface similarity:** Azure uses the native Jupyter Notebook interface.

**Keyboard shortcuts:** Azure uses all of the same keyboard shortcuts as Jupyter.

**Missing features:** None.
**Added features:**

- The [RISE](https://rise.readthedocs.io/) extension comes pre-installed, which allows you to instantly [present your notebook](https://docs.microsoft.com/en-us/azure/notebooks/present-jupyter-notebooks-slideshow) as a live reveal.js-based slideshow.
- The [jupyter_contrib_nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/) package comes pre-installed, which gives you easy access to a collection of 50+ Jupyter Notebook extensions for enhancing the notebook interface.

**Ease of working with datasets:** You can upload a dataset to your project from your local computer or a URL, and it can be accessed by any notebook within your project. Azure also includes [connectors](https://docs.microsoft.com/en-us/azure/notebooks/access-data-resources-jupyter-notebooks) to other Azure services, such as Azure Storage and various Azure databases.

**Internet access:** Yes.
**Ability to work privately:** Yes.

**Ability to share publicly:** Yes. If you choose to make your project [public](https://notebooks.azure.com/justmarkham/projects/pycon-2018-tutorial), anyone can access it without creating a Microsoft account, and anyone with a Microsoft account can copy it to their own account. Additionally, Azure also provides you with a [public profile page](https://notebooks.azure.com/justmarkham) (very similar to a GitHub profile), which displays all of your public projects.

**Ability to collaborate:** No, though this is a [planned feature](https://github.com/Microsoft/AzureNotebooks/issues/6).

**Performance of the free plan:** You will have access to 4 GB of RAM and 1 GB of disk space (per project). Sessions will shut down after 60 minutes of inactivity, though they can run for 8 hours or longer.

**Ability to upgrade for better performance:** Yes. You can pay for an [Azure subscription](https://azure.microsoft.com/en-us/free/), though the [setup process](https://docs.microsoft.com/en-us/azure/notebooks/configure-manage-azure-notebooks-projects) is non-trivial and the [pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/) is complicated.

**Documentation and technical support:** Azure has extensive [documentation](https://docs.microsoft.com/en-us/azure/notebooks/). Support is available via [GitHub issues](https://github.com/microsoft/AzureNotebooks/issues).

**Conclusion:** The greatest strength of Azure Notebooks is its ease of use: the project structure (borrowed from GitHub) makes it simple to work with multiple notebooks and datasets, and the use of the native Jupyter interface means that existing Jupyter users will have an easy transition. However, the RAM and disk space are not particularly generous, and the lack of collaboration is a big gap in the functionality.

* * *

## 5. CoCalc

![](../_resources/4028f48f4cf0f8130f1e21ea256eed54.png)

[CoCalc](https://cocalc.com/), short for "collaborative calculation", is an online workspace for computation in Python, R, Julia, and many other languages. It allows you to create and edit Jupyter Notebooks, Sage worksheets, and LaTeX documents. After creating a CoCalc account, the first step is to create a "project", which can contain one or more notebooks, Markdown files, datasets, and any other file you want to create or upload, and all of these can be organized into folders. The project interface is a bit overwhelming at first, but it looks much more familiar once you create or open a notebook.

**Supported languages:** Python (2 and 3), R, Julia, and many other languages.

**Ability to install packages:**  [Hundreds of packages](https://cocalc.com/doc/software-python.html) come pre-installed. You can [install additional packages](https://doc.cocalc.com/howto/install-python-lib.html) using pip, but this is not available when using a free plan. Alternatively, you can ask CoCalc to include additional packages in their default installation.

**Interface similarity:** Although CoCalc does not use the native Jupyter Notebook interface (they rewrote it using React.js), the interface is very similar to Jupyter, with only a few minor modifications. You can actually [switch](https://doc.cocalc.com/jupyter.html#classical-versus-cocalc) to using the native Jupyter Notebook from within CoCalc, though it's not recommended since you would lose access to the most valuable CoCalc features ("time travel" and real-time collaboration, which are discussed below).

**Keyboard shortcuts:** CoCalc uses almost all of the same keyboard shortcuts as Jupyter.

**Missing features:** CoCalc does not [currently](https://github.com/sagemathinc/cocalc/issues/1930) support interactive widgets.

**Added features:**

- CoCalc includes a powerful version control feature called [time travel](https://cocalc.com/doc/jupyter-notebook.html#a-timetravel), which records all of your changes to the notebook in fine detail, and allows you to browse those changes using an intuitive slider control.
- CoCalc saves a backup of all of your project files every few minutes, which means you can recover older versions of your files if needed.
- CoCalc includes [additional features for instructors](https://doc.cocalc.com/teaching-instructors.html), such as the ability to distribute and grade assignments, and the ability to watch students while they work and chat with them about the assignment.

**Ease of working with datasets:** You can upload a dataset to your project from your local computer, and it can be accessed by any notebook within your project.

**Internet access:** No, this is not available when using a free plan.
**Ability to work privately:** Yes.

**Ability to share publicly:** Yes. If you choose to make your notebook [public](https://share.cocalc.com/share/81f7b76f-878a-4f00-b4d8-b475f007f3af/tutorial.ipynb?viewer=share) and you share the link, anyone can access it without creating a CoCalc account, and anyone with a CoCalc account can copy it to their own account.

**Ability to collaborate:** Yes. You can keep your notebook private but invite specific people to edit it. You and your collaborator(s) can edit the notebook at the same time and see each other's changes (and cursors) in real-time, as well as chat (using text or video) in a window next to the notebook. The status and the results of all computations are also synchronized, which means that everyone involved will experience the notebook in the same way.

**Performance of the free plan:** You will have access to a 1-core shared CPU with 1 GB of shared RAM, and 3 GB of disk space (per project). Sessions will shut down after 30 minutes of inactivity, though they can run for up to 24 hours.

**Ability to upgrade for better performance:** Yes. You can pay for a [CoCalc subscription](https://cocalc.com/policies/pricing.html), which starts at $14/month. Alternatively, you can install the [CoCalc Docker image](https://github.com/sagemathinc/cocalc-docker) on your own computer, which allows you to run a private multi-user CoCalc server for free.

**Documentation and technical support:** CoCalc has extensive [documentation](https://doc.cocalc.com/). Support is available via email and a contact form, and product issues are tracked on [GitHub](https://github.com/sagemathinc/cocalc/issues?q=is%3Aopen+is%3Aissue+label%3AA-jupyter).

**Conclusion:** The most compelling reasons to use CoCalc are the real-time collaboration and the "time travel" version control features, as well as the course management features (if you're an instructor). Although the interface is a bit cluttered, existing Jupyter users would have a relatively easy time transitioning to CoCalc. However, the free plan does have some important limitations (inability to install additional packages or access the Internet), and the performance of the free plan is modest.

* * *

## 6. Datalore

![](../_resources/d6a87c6836db23e1ef50f6f3da316b82.png)

[Datalore](https://datalore.io/) was created by JetBrains, the same company who makes PyCharm (a popular Python IDE). Getting started is as easy as creating an account, or logging in with a Google or JetBrains account. You can either create a new Datalore "workbook" or upload an existing Jupyter Notebook. Datalore workbooks are stored in a proprietary format, though it does support importing and exporting the standard .ipynb file format.

**Supported languages:** Python 3 only.

**Ability to install packages:** Hundreds of packages come pre-installed, and you can install additional packages using pip or conda, or by specifying the GitHub repository of a package.

**Interface similarity:** When you open Datalore, the interface does resemble a Jupyter Notebook in the sense that there are code and Markdown cells as well as output below those cells. However, there are some important differences between the Datalore and Jupyter interfaces:

- Cells (which Datalore calls "blocks") are not numbered, because the ordering of cells is enforced. In other words, all of your code must be written in the order in which you ultimately want it to run.
- The notebook (which Datalore calls a "workbook") can have multiple worksheets, similar to Google Sheets, which is a convenient way to break long workbooks into logical sections. If you create multiple worksheets in a workbook, all of the worksheets share the same environment. Because cell order is important in Datalore, the cells in the second worksheet are treated as coming after the cells in the first worksheet, the third worksheet comes after the second worksheet, and so on.
- There are many other interface differences, which are explained in the "added features" section.

**Keyboard shortcuts:** Keyboard shortcuts are available for most actions in Datalore, but the shortcuts are wildly different from those used by Jupyter.

**Missing features:**

- Datalore does not use the IPython kernel, and thus IPython magic functions and shell commands are not available. (However, optional access to the IPython kernel is a planned feature.)
- Because the Datalore menu bar is kept very simple and there's no toolbar, many actions can only be done using keyboard shortcuts.
- You can't download your workbook into other useful formats such as a Python script, HTML webpage, or Markdown file.
- Datalore does not support all of the commonly supported Markdown features in its Markdown cells. (However, improved Markdown support is a planned feature.)
- Datalore does not support interactive widgets.
- Datalore does not include multicursor support.

**Added features:**

- Cells are automatically run as you write them, which Datalore calls "live computation". This actually makes it easier to debug code as you write it, since you can see the results of your code immediately. (Live computation can be disabled, in which case you can manually trigger cells to run.)
- Because cells will always run in the order in which they are arranged, Datalore can track cell dependencies. This means that when a given cell is edited, Datalore will determine which cells below it are potentially affected and will immediately re-run those cells (assuming live computation is enabled). If the edit causes an error in a dependent cell, those errors will immediately be flagged.
- Datalore allows you to display cell inputs and outputs sequentially (like in Jupyter) or in "split view", in which case the inputs and outputs are in two separate panes. When using sequential view, Datalore also makes it easy to hide all inputs or hide all outputs.
- Datalore includes more "intelligence" than Jupyter in its code completion.
- As you write code, Datalore provides context-aware suggestions (called "intentions") for which actions you might want to take. For example, after typing the name of a DataFrame, the intentions might include "drop string columns", "histogram", and "train test split". When you click an intention, Datalore actually generates the code for you, which can be a useful way to learn the code behind certain tasks.
- Datalore includes a well-designed version control system. It frequently saves the current state of your workbook, and you can quickly browse the diffs between the current version and any past versions. You can also choose to add a message when saving the workbook, and then filter the list of versions to only include those versions with a message.
- Datalore gives you access to a plotting library called datalore.plot, which is very similar to R's ggplot2, though you can only use it inside of Datalore.

**Ease of working with datasets:** You can upload a dataset to your workbook from your local computer or a URL, but it can only be accessed by that particular workbook. This would be a significant annoyance if you work with the same dataset(s) across many workbooks. (However, sharing datasets between workbooks is a planned feature.)

**Internet access:** Yes.
**Ability to work privately:** Yes.
**Ability to share publicly:** No.

**Ability to collaborate:** Yes. You can keep your workbook private but invite specific people to view or edit it. You and your collaborator(s) can edit the notebook at the same time and see each other's changes (and cursors) in real-time. The status and the results of all computations are also synchronized, which means that everyone involved will experience the notebook in the same way.

**Performance of the free plan:** You will have access to a 2-core CPU with 4 GB of RAM, and 10 GB of disk space. Sessions will shut down after 60 minutes of inactivity, though there is no specific limit on the length of individual sessions. You can use the service for up to 120 hours per month.

**Ability to upgrade for better performance:** No, though there will soon be a paid plan which offers more disk space and a more powerful CPU (or GPU).

**Documentation and technical support:** Datalore has minimal documentation, which is contained within sample workbooks. Support is available via a [Discourse forum](https://forum.datalore.io/).

**Conclusion:** Rather than being an adaptation of the Jupyter Notebook, Datalore is more like a reinvention of the Notebook. It includes an innovative feature set, including live computation, dependency tracking, real-time collaboration, and built-in version control. However, existing Jupyter users may have a challenging time transitioning to Datalore, especially since cell ordering is enforced and all of the keyboard shortcuts are quite different. As well, Datalore currently includes some notable limitations, namely that workbooks can't be shared publicly and uploaded datasets can't be shared between workbooks.

* * *

## How to choose the right service for you

Out of the six options presented, there's not one clear "winner". Instead, the right choice for you will depend on your priorities. Below are my suggestions for what you should choose, based on your particular needs. (Note: You can also view this as a [comparison table](https://docs.google.com/spreadsheets/d/12thaaXg1Idr3iWST8QyASNDs08sjdPd6m9mbCGtHFn0/edit?usp=sharing).)

**You use a language other than Python:** Binder and CoCalc support tons of languages. Azure supports Python, R and F#, Kernels supports Python and R, Colab supports Python and Swift, and Datalore only supports Python.

**You need to use Python 2:** Binder, Colab, Azure, and CoCalc all support Python 2 and 3, whereas Kernels and Datalore only support Python 3.

**You work with non-standard packages:** Binder and Azure allow you to specify your exact package requirements using a configuration file. CoCalc and Datalore allow you to install additional packages, which will persist across sessions, though this is not available with CoCalc's free plan. Kernels and Colab also allow you to install additional packages, though they do not persist across sessions. Kernels and CoCalc accept user requests for which packages should be included in their default installation.

**You love the existing Jupyter Notebook interface:** Binder and Azure use the native Jupyter Notebook interface, and CoCalc uses a nearly identical interface. Kernels is visually different from Jupyter but works like it, whereas Colab is visually similar to Jupyter but does not work like it. Datalore is the furthest from the existing Jupyter Notebook.

**You are a heavy user of keyboard shortcuts:** Binder, Kernels, and Azure use the same keyboard shortcuts as Jupyter, and CoCalc uses almost all of the same shortcuts. Datalore uses completely different keyboard shortcuts, and Colab uses cumbersome multi-step keyboard shortcuts (though they can be customized).

**You prefer a point-and-click interface:** Binder, Azure, and CoCalc allow you to perform all actions by pointing and clicking, whereas Kernels, Colab, and Datalore require you to use keyboard shortcuts for certain actions.

**You want an integrated version control system:** CoCalc and Datalore provide the best interfaces for version control. Kaggle's version control system is more limited, and Colab's system is even more limited. Binder and Azure do not provide a version control system.

**You work with a lot of datasets:** Kernels works seamlessly with Kaggle Datasets, a full-featured (and free) service for hosting datasets of up to 20 GB each. CoCalc offers 3 GB of disk space per project, and any dataset you upload can be accessed by any notebook in your project. Azure has similar functionality, except it offers 1 GB of disk space per project. Datalore offers 10 GB of total disk space, though every dataset you upload has to be linked to a particular workbook. Colab will discard any datasets you upload when your session ends, unless you link Colab to your Google Drive. Binder is best for small datasets that are either stored in your Git repository or located at a public URL.

**Your project is already hosted on GitHub:** Binder can run your notebooks directly from GitHub, Azure will allow you to import an entire GitHub repository, and Colab can import a single notebook from GitHub. Kernels, CoCalc, and Datalore don't provide any similar functionality.

**You need to keep your work private:** All of the options except for Binder support working in private.

**You need to keep your data on-premise:** None of these cloud-based services allow you to keep your data on-premise. However, you can set up Binder or CoCalc on your own server, since BinderHub and the CoCalc Docker image are both open source, which would allow you to keep your data on-premise.

**You want to share your work publicly:** Binder creates the least friction possible when sharing, since people can view and run your notebook without creating an account. Kernels, Colab, Azure, and CoCalc allow you to share a URL for read-only access, while requiring users to create an account if they want to run your notebook. Kernels and Azure make sharing even easier by providing you with a public profile page. Datalore does not allow for public sharing.

**You need to collaborate with others:** CoCalc and Datalore support real-time collaboration. Colab supports collaborating on the same document, though it's not quite real-time and you're not sharing the same environment. Kernels supports a form of collaboration in which you're sharing a version history. Binder and Azure don't include any collaboration functionality, though with Binder it could easily occur through the normal GitHub pull request workflow.

**You want a high performance environment:** Kernels provides the most powerful environment (4-core CPU and 17 GB RAM), followed by Datalore (2-core CPU and 4 GB RAM), Azure (4 GB RAM), Binder (up to 2 GB RAM), and CoCalc (1-core CPU and 1 GB RAM). Colab does not provide specifications for its environment.

**You need access to a GPU:** Kernels and Colab both provide free access to a GPU. GPU access is available to paying customers of Azure and (soon) Datalore. GPU access is not available through Binder or CoCalc.

**You prefer to use a non-commercial tool:** Binder is the only option that is managed by a non-commercial entity.

* * *

## Similar services which were not reviewed

The following services are similar to the six options above, but were not included in my comparison:

- I didn't include any service that only provides access to JupyterLab, such as [Notebooks AI](https://notebooks.ai/), [Kyso](http://kyso.io/), and [CyVerse](http://learning.cyverse.org/projects/vice/en/latest/getting_started/about.html). (Note that Binder, Azure, and CoCalc all allow you to use JupyterLab instead of Jupyter Notebook if you prefer.)
- I didn't include [IBM Watson Studio Cloud](https://www.ibm.com/cloud/watson-studio) because the process of getting started is cumbersome, the interface is overly complicated, the free plan has lots of limitations, and there were lots of error messages during my testing.
- I didn't include [Gryd](https://gryd.us/) because the free plan requires an academic email address, and I didn't include [Code Ocean](https://codeocean.com/) because the free plan is severely limited without an academic email address.
- I didn't include [ZEPL](https://www.zepl.com/) because it doesn't allow you to export notebooks using the standard .ipynb format.
- I didn't include any paid services, such as [Saturn Cloud](https://www.saturncloud.io/), [Crestle.ai](https://www.crestle.ai/), [Paperspace](https://www.paperspace.com/), and [Salamander](https://salamander.ai/).

* * *

## My fact-checking process

This article is the result of 50+ hours of research, testing, and writing. In addition, I shared drafts of this article with the relevant teams from Binder, Kaggle, Google, Microsoft, CoCalc, and Datalore in March 2019. I received detailed feedback from all six companies/organizations (thank you!), which I incorporated into the article before publishing.

That being said, these services are constantly changing, and it's likely that some of this information will become outdated in the future. If you believe that something in this article is no longer correct, please leave a comment below, and I'd be happy to consider updating the article.

**P.S.** Want to master the Jupyter Notebook? [Subscribe to the Data School newsletter](https://www.dataschool.io/subscribe/) to find out when my new course launches!

- [  ![](data:image/svg+xml,%3csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='595' class='js-evernote-checked'%3e %3cpath transform='scale(0.014%2c-0.014) translate(0%2c-1670)' d='M1792 826v-794q0 -66 -47 -113t-113 -47h-1472q-66 0 -113 47t-47 113v794q44 -49 101 -87q362 -246 497 -345q57 -42 92.5 -65.5t94.5 -48t110 -24.5h1h1q51 0 110 24.5t94.5 48t92.5 65.5q170 123 498 345q57 39 100 87zM1792 1120q0 -79 -49 -151t-122 -123 q-376 -261 -468 -325q-10 -7 -42.5 -30.5t-54 -38t-52 -32.5t-57.5 -27t-50 -9h-1h-1q-23 0 -50 9t-57.5 27t-52 32.5t-54 38t-42.5 30.5q-91 64 -262 182.5t-205 142.5q-62 42 -117 115.5t-55 136.5q0 78 41.5 130t118.5 52h1472q65 0 112.5 -47t47.5 -113z' data-evernote-id='596' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)    Email](https://www.dataschool.io/cloud-services-for-jupyter-notebook/mailto:?subject=Six%20easy%20ways%20to%20run%20your%20Jupyter%20Notebook%20in%20the%20cloud&body=https://www.dataschool.io/cloud-services-for-jupyter-notebook/)

- [  ![](data:image/svg+xml,%3csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='601' class='js-evernote-checked'%3e %3cpath d='M27.825%2c4.783c0-2.427-2.182-4.608-4.608-4.608H4.783c-2.422%2c0-4.608%2c2.182-4.608%2c4.608v18.434 c0%2c2.427%2c2.181%2c4.608%2c4.608%2c4.608H14V17.379h-3.379v-4.608H14v-1.795c0-3.089%2c2.335-5.885%2c5.192-5.885h3.718v4.608h-3.726 c-0.408%2c0-0.884%2c0.492-0.884%2c1.236v1.836h4.609v4.608h-4.609v10.446h4.916c2.422%2c0%2c4.608-2.188%2c4.608-4.608V4.783z' data-evernote-id='602' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)    Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.dataschool.io/cloud-services-for-jupyter-notebook/)
- [  ![](data:image/svg+xml,%3csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='607' class='js-evernote-checked'%3e %3cpath d='M24.253%2c8.756C24.689%2c17.08%2c18.297%2c24.182%2c9.97%2c24.62c-3.122%2c0.162-6.219-0.646-8.861-2.32 c2.703%2c0.179%2c5.376-0.648%2c7.508-2.321c-2.072-0.247-3.818-1.661-4.489-3.638c0.801%2c0.128%2c1.62%2c0.076%2c2.399-0.155 C4.045%2c15.72%2c2.215%2c13.6%2c2.115%2c11.077c0.688%2c0.275%2c1.426%2c0.407%2c2.168%2c0.386c-2.135-1.65-2.729-4.621-1.394-6.965 C5.575%2c7.816%2c9.54%2c9.84%2c13.803%2c10.071c-0.842-2.739%2c0.694-5.64%2c3.434-6.482c2.018-0.623%2c4.212%2c0.044%2c5.546%2c1.683 c1.186-0.213%2c2.318-0.662%2c3.329-1.317c-0.385%2c1.256-1.247%2c2.312-2.399%2c2.942c1.048-0.106%2c2.069-0.394%2c3.019-0.851 C26.275%2c7.229%2c25.39%2c8.196%2c24.253%2c8.756z' data-evernote-id='608' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)    Twitter](http://twitter.com/home?status=Six%20easy%20ways%20to%20run%20your%20Jupyter%20Notebook%20in%20the%20cloud%20https://www.dataschool.io/cloud-services-for-jupyter-notebook/)
- [  ![](data:image/svg+xml,%3csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='613' class='js-evernote-checked'%3e %3cpath d='M25.424%2c15.887v8.447h-4.896v-7.882c0-1.979-0.709-3.331-2.48-3.331c-1.354%2c0-2.158%2c0.911-2.514%2c1.803 c-0.129%2c0.315-0.162%2c0.753-0.162%2c1.194v8.216h-4.899c0%2c0%2c0.066-13.349%2c0-14.731h4.899v2.088c-0.01%2c0.016-0.023%2c0.032-0.033%2c0.048 h0.033V11.69c0.65-1.002%2c1.812-2.435%2c4.414-2.435C23.008%2c9.254%2c25.424%2c11.361%2c25.424%2c15.887z M5.348%2c2.501 c-1.676%2c0-2.772%2c1.092-2.772%2c2.539c0%2c1.421%2c1.066%2c2.538%2c2.717%2c2.546h0.032c1.709%2c0%2c2.771-1.132%2c2.771-2.546 C8.054%2c3.593%2c7.019%2c2.501%2c5.343%2c2.501H5.348z M2.867%2c24.334h4.897V9.603H2.867V24.334z' data-evernote-id='614' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)    LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https://www.dataschool.io/cloud-services-for-jupyter-notebook/&title=Six%20easy%20ways%20to%20run%20your%20Jupyter%20Notebook%20in%20the%20cloud&summary=There%20are%20many%20ways%20to%20share%20a%20static%20Jupyter%20notebook%20with%20others,%20such%20as%20posting%20it%20on%20GitHub%20or%20sharing%20an%20nbviewer%20link.%20However,%20the%20recipient%20can%20only%20interact%20with%20the%20notebook%20file%20if%20they%20already%20have%20the%20Jupyter%20Notebook%20environment%20installed.%20But%20what%20if%20you%20want%20to%20share%20a...)

- [  ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='620' class='js-evernote-checked'%3e %3cpath d='M18.02 21.842c-2.029 0.052-2.422-1.396-2.439-2.446v-7.294h4.729V7.874h-4.71V1.592c0 0-3.653 0-3.714 0 s-0.167 0.053-0.182 0.186c-0.218 1.935-1.144 5.33-4.988 6.688v3.637h2.927v7.677c0 2.8 1.7 6.7 7.3 6.6 c1.863-0.03 3.934-0.795 4.392-1.453l-1.22-3.539C19.595 21.6 18.7 21.8 18 21.842z' data-evernote-id='621' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)    Tumblr](http://www.tumblr.com/share?v=3&u=https%3A%2F%2Fwww.dataschool.io%2Fcloud-services-for-jupyter-notebook%2F&t=Six%20easy%20ways%20to%20run%20your%20Jupyter%20Notebook%20in%20the%20cloud)

- [  ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='627' class='js-evernote-checked'%3e %3cg data-evernote-id='628' class='js-evernote-checked'%3e %3cpath d='M11.794 15.316c0-1.029-0.835-1.895-1.866-1.895c-1.03 0-1.893 0.865-1.893 1.895s0.863 1.9 1.9 1.9 C10.958 17.2 11.8 16.3 11.8 15.316z' data-evernote-id='629' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M18.1 13.422c-1.029 0-1.895 0.864-1.895 1.895c0 1 0.9 1.9 1.9 1.865c1.031 0 1.869-0.836 1.869-1.865 C19.969 14.3 19.1 13.4 18.1 13.422z' data-evernote-id='630' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M17.527 19.791c-0.678 0.678-1.826 1.006-3.514 1.006c-0.004 0-0.009 0-0.014 0c-0.004 0-0.01 0-0.015 0 c-1.686 0-2.834-0.328-3.51-1.005c-0.264-0.265-0.693-0.265-0.958 0c-0.264 0.265-0.264 0.7 0 1 c0.943 0.9 2.4 1.4 4.5 1.402c0.005 0 0 0 0 0c0.005 0 0 0 0 0c2.066 0 3.527-0.459 4.47-1.402 c0.265-0.264 0.265-0.693 0.002-0.958C18.221 19.5 17.8 19.5 17.5 19.791z' data-evernote-id='631' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M27.707 13.267c0-1.785-1.453-3.237-3.236-3.237c-0.793 0-1.518 0.287-2.082 0.761c-2.039-1.295-4.646-2.069-7.438-2.219 l1.483-4.691l4.062 0.956c0.071 1.4 1.3 2.6 2.7 2.555c1.488 0 2.695-1.208 2.695-2.695C25.881 3.2 24.7 2 23.2 2 c-1.059 0-1.979 0.616-2.42 1.508l-4.633-1.091c-0.344-0.081-0.693 0.118-0.803 0.455l-1.793 5.7 C10.548 8.6 7.7 9.4 5.6 10.75C5.006 10.3 4.3 10 3.5 10.029c-1.785 0-3.237 1.452-3.237 3.2 c0 1.1 0.6 2.1 1.4 2.69c-0.04 0.272-0.061 0.551-0.061 0.831c0 2.3 1.3 4.4 3.7 5.9 c2.299 1.5 5.3 2.3 8.6 2.325c3.228 0 6.271-0.825 8.571-2.325c2.387-1.56 3.7-3.66 3.7-5.917 c0-0.26-0.016-0.514-0.051-0.768C27.088 15.5 27.7 14.4 27.7 13.267z M23.186 3.355c0.74 0 1.3 0.6 1.3 1.3 c0 0.738-0.6 1.34-1.34 1.34s-1.342-0.602-1.342-1.34C21.844 4 22.4 3.4 23.2 3.355z M1.648 13.3 c0-1.038 0.844-1.882 1.882-1.882c0.31 0 0.6 0.1 0.9 0.209c-1.049 0.868-1.813 1.861-2.26 2.9 C1.832 14.2 1.6 13.8 1.6 13.267z M21.773 21.57c-2.082 1.357-4.863 2.105-7.831 2.105c-2.967 0-5.747-0.748-7.828-2.105 c-1.991-1.301-3.088-3-3.088-4.782c0-1.784 1.097-3.484 3.088-4.784c2.081-1.358 4.861-2.106 7.828-2.106 c2.967 0 5.7 0.7 7.8 2.106c1.99 1.3 3.1 3 3.1 4.784C24.859 18.6 23.8 20.3 21.8 21.57z M25.787 14.6 c-0.432-1.084-1.191-2.095-2.244-2.977c0.273-0.156 0.59-0.245 0.928-0.245c1.035 0 1.9 0.8 1.9 1.9 C26.354 13.8 26.1 14.3 25.8 14.605z' data-evernote-id='632' class='js-evernote-checked'%3e%3c/path%3e %3c/g%3e %3c/svg%3e)    Reddit](http://www.reddit.com/submit?url=https://www.dataschool.io/cloud-services-for-jupyter-notebook/)

- [  ![](data:image/svg+xml,%3csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' width='28px' height='28px' viewBox='0 0 28 28' enable-background='new 0 0 28 28' xml:space='preserve' data-evernote-id='637' class='js-evernote-checked'%3e %3cg data-evernote-id='638' class='js-evernote-checked'%3e %3cpath d='M14.703%2c15.854l-1.219-0.948c-0.372-0.308-0.88-0.715-0.88-1.459c0-0.748%2c0.508-1.223%2c0.95-1.663 c1.42-1.119%2c2.839-2.309%2c2.839-4.817c0-2.58-1.621-3.937-2.399-4.581h2.097l2.202-1.383h-6.67c-1.83%2c0-4.467%2c0.433-6.398%2c2.027 C3.768%2c4.287%2c3.059%2c6.018%2c3.059%2c7.576c0%2c2.634%2c2.022%2c5.328%2c5.604%2c5.328c0.339%2c0%2c0.71-0.033%2c1.083-0.068 c-0.167%2c0.408-0.336%2c0.748-0.336%2c1.324c0%2c1.04%2c0.551%2c1.685%2c1.011%2c2.297c-1.524%2c0.104-4.37%2c0.273-6.467%2c1.562 c-1.998%2c1.188-2.605%2c2.916-2.605%2c4.137c0%2c2.512%2c2.358%2c4.84%2c7.289%2c4.84c5.822%2c0%2c8.904-3.223%2c8.904-6.41 c0.008-2.327-1.359-3.489-2.829-4.731H14.703z M10.269%2c11.951c-2.912%2c0-4.231-3.765-4.231-6.037c0-0.884%2c0.168-1.797%2c0.744-2.511 c0.543-0.679%2c1.489-1.12%2c2.372-1.12c2.807%2c0%2c4.256%2c3.798%2c4.256%2c6.242c0%2c0.612-0.067%2c1.694-0.845%2c2.478 c-0.537%2c0.55-1.438%2c0.948-2.295%2c0.951V11.951z M10.302%2c25.609c-3.621%2c0-5.957-1.732-5.957-4.142c0-2.408%2c2.165-3.223%2c2.911-3.492 c1.421-0.479%2c3.25-0.545%2c3.555-0.545c0.338%2c0%2c0.52%2c0%2c0.766%2c0.034c2.574%2c1.838%2c3.706%2c2.757%2c3.706%2c4.479 c-0.002%2c2.073-1.736%2c3.665-4.982%2c3.649L10.302%2c25.609z' data-evernote-id='639' class='js-evernote-checked'%3e%3c/path%3e %3cpolygon points='23.254%2c11.89 23.254%2c8.521 21.569%2c8.521 21.569%2c11.89 18.202%2c11.89 18.202%2c13.604 21.569%2c13.604 21.569%2c17.004 23.254%2c17.004 23.254%2c13.604 26.653%2c13.604 26.653%2c11.89' data-evernote-id='640' class='js-evernote-checked'%3e%3c/polygon%3e %3c/g%3e %3c/svg%3e)    Google+](https://plus.google.com/share?url=https://www.dataschool.io/cloud-services-for-jupyter-notebook/)

- [  ![](data:image/svg+xml,%3csvg width='32px' height='28px' viewBox='0 0 32 28' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:sketch='http://www.bohemiancoding.com/sketch/ns' data-evernote-id='645' class='js-evernote-checked'%3e %3cpath d='M28.7817528%2c0.00172488695 C30.8117487%2c0.00431221738 31.9749312%2c1.12074529 31.9644402%2c3.10781507 C31.942147%2c6.67703739 32.1336065%2c10.2669583 31.8057648%2c13.8090137 C30.7147076%2c25.5813672 17.2181194%2c31.8996281 7.20714461%2c25.3808491 C2.71833574%2c22.4571656 0.196577202%2c18.3122624 0.0549495772%2c12.9357897 C-0.0342233715%2c9.5774348 0.00642900214%2c6.21519891 0.0300336062%2c2.85555035 C0.0405245414%2c1.1129833 1.21157517%2c0.0146615391 3.01995012%2c0.00819321302 C7.34746087%2c-0.00603710433 11.6775944%2c0.00431221738 16.0064164%2c0.00172488695 C20.2644248%2c0.00172488695 24.5237444%2c-0.00215610869 28.7817528%2c0.00172488695 L28.7817528%2c0.00172488695 Z M8.64885184%2c7.85611511 C7.38773662%2c7.99113854 6.66148108%2c8.42606978 6.29310958%2c9.33228474 C5.90114134%2c10.2969233 6.17774769%2c11.1421181 6.89875951%2c11.8276216 C9.35282156%2c14.161969 11.8108164%2c16.4924215 14.2976518%2c18.7943114 C15.3844131%2c19.7966007 16.5354102%2c19.7836177 17.6116843%2c18.7813283 C20.0185529%2c16.5495467 22.4070683%2c14.2982907 24.7824746%2c12.0327533 C25.9845979%2c10.8850542 26.1012707%2c9.56468083 25.1469132%2c8.60653379 C24.1361858%2c7.59255976 22.8449191%2c7.6743528 21.5890476%2c8.85191291 C19.9936451%2c10.3488554 18.3680912%2c11.8172352 16.8395462%2c13.3777945 C16.1342655%2c14.093159 15.7200114%2c14.0048744 15.0566806%2c13.3440386 C13.4599671%2c11.7484252 11.8081945%2c10.2060421 10.1262706%2c8.70001155 C9.65564653%2c8.27936164 9.00411403%2c8.05345704 8.64885184%2c7.85611511 L8.64885184%2c7.85611511 L8.64885184%2c7.85611511 Z' data-evernote-id='646' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)    Pocket](https://getpocket.com/save?url=https://www.dataschool.io/cloud-services-for-jupyter-notebook/)