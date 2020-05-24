Binder (beta)

#### (beta)

### Turn a GitHub repo into a collection of interactive notebooks

Have a repository full of Jupyter notebooks? With Binder, open those notebooks in an executable environment, making your code immediately reproducible by anyone, anywhere.

####   Build and launch a repository

   GitHub repo or URL

 Git branch, tag, or commit

 Path to a notebook file (optional)

 Copy the URL below and share your Binder with others:

Fill in the fields to see a URL for sharing your Binder.
 ![](../_resources/032cc861bddc9cd8b47021f8217c9b78.png)

 Copy the text below, then paste into your README to show a binder badge: ![](../_resources/5ba2c131a74eae2b645b6258f3c92228.png)    [](https://mybinder.org/#)

### How it works

 1

 Enter your repository information

Provide in the above form a URL or a GitHub repository that contains Jupyter notebooks, as well as a branch, tag, or commit hash. Launch will build your Binder repository. If you specify a path to a notebook file, the notebook will be opened in your browser after building.

 2

 We build a Docker image of your repository

Binder will search for a dependency file, such as requirements.txt or environment.yml, in the repository's root directory ([more details on more complex dependencies in documentation](http://mybinder.readthedocs.io/en/latest/using.html#preparing-a-repository-for-binder)). The dependency files will be used to build a Docker image. If an image has already been built for the given repository, it will not be rebuilt. If a new commit has been made, the image will automatically be rebuilt.

 3

 Interact with your notebooks in a live environment!

A [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/) server will host your repository's contents. We offer you a reusable link and badge to your live repository that you can easily share with others.