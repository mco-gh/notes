kynan/nbstripout

[![68747470733a2f2f7472617669732d63692e6f72672f6b796e616e2f6e6273747269706f75742e7376673f6272616e63683d6d6173746572](../_resources/087bbac58300ac5d38e541f4c3d661f2.png)](https://travis-ci.org/kynan/nbstripout)[![68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f6e6273747269706f75742e737667](../_resources/4237a3094672c623a8e8b74fe5e466f0.png)](https://pypi.python.org/pypi/nbstripout)[![68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6e6273747269706f75742e737667](../_resources/50e4a81d7ab7cd437687cd8f0127563b.png)](https://pypi.python.org/pypi/nbstripout)[![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667](../_resources/bf274daf5af5a120135584352c2c8181.png)](https://raw.githubusercontent.com/kynan/nbstripout/master/LICENSE.txt)[![68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6e6273747269706f75742e737667](../_resources/6962e6c509f335bea72b07f5af1dfe9f.png)](https://pypi.python.org/pypi/nbstripout)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='973' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#nbstripout-strip-output-from-jupyter-and-ipython-notebooks)nbstripout: strip output from Jupyter and IPython notebooks

Opens a notebook, strips its output, and writes the outputless version to the original file.

Useful mainly as a git filter or pre-commit hook for users who don't want to track output in VCS.

This does mostly the same thing as the Clear All Output command in the notebook UI.

Based on https://gist.github.com/minrk/6176788.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='65'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='979' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#screencast)Screencast

This screencast demonstrates the use and working principles behind the nbstripout utility and how to use it as a Git filter:

[![687474703a2f2f692e696d6775722e636f6d2f376f5148754a352e706e67](../_resources/0fe583c3fc64dc95b243e06fb2f9ba9c.png)](https://www.youtube.com/watch?v=BEMP4xacrVc)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='66'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='982' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#installation)Installation

You can download and install the latest version of `nbstripout` from [PyPI](https://pypi.io/), the Python package index, as follows:

pip install --upgrade nbstripout

When using the [Anaconda](https://www.continuum.io/anaconda-overview) Python distribution, install `nbstripout` via the[conda](http://conda.pydata.org/) package manager from [conda-forge](http://conda-forge.github.io/):

conda install -c conda-forge nbstripout

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='67'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='986' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#usage)Usage

Strip output from IPython / Jupyter notebook (modifies the files in-place):
nbstripout FILE.ipynb [FILE2.ipynb ...]
Force processing of non `.ipynb` files:
nbstripout -f FILE.ipynb.bak
Write to stdout e.g. to use as part of a shell pipeline:
cat FILE.ipynb | nbstripout > OUT.ipynb
or
nbstripout -t FILE.ipynb | other-command

Set up the git filter and attributes as described in the manual installation instructions below:

nbstripout --install
Set up the git filter using `.gitattributes`
nbstripout --install --attributes .gitattributes
Remove the git filter and attributes:
nbstripout --uninstall
Remove the git filter and attributes from `.gitattributes`:
nbstripout --uninstall --attributes .gitattributes

Check if `nbstripout` is installed in the current repository (exits with code 0 if installed, 1 otherwise):

nbstripout --is-installed

Print status of `nbstripout` installation in the current repository and configuration summary of filter and attributes if installed (exits with code 0 if installed, 1 otherwise):

nbstripout --status
Print the version:
nbstripout --version
Show this help page:
nbstripout --help

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1000' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#apply-retroactively)Apply retroactively

`nbstripout` can be used to rewrite an existing Git repository using`git filter-branch` to strip output from existing notebooks. This invocation uses `--index-filter` and operates on all ipynb-files in the repo:

git filter-branch -f --index-filter '
git checkout -- :*.ipynb
find . -name "*.ipynb" -exec nbstripout "{}" +
git add . --ignore-removal
'

If the repository is large and the notebooks are in a subdirectory it will run faster with `git checkout -- :<subdir>/*.ipynb`. You will get a warning for commits that do not contain any notebooks, which can be suppressed by piping stderr to `/dev/null`.

This is a potentially slower but simpler invocation using `--tree-filter`:

git filter-branch -f --tree-filter 'find . -name "*.ipynb" -exec nbstripout "{}" +'

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='69'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1005' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#keeping-some-output)Keeping some output

Do not strip the execution count/prompt number
nbstripout --keep-count
Do not strip the output
nbstripout --keep-output

To mark special cells so that the output is not striped, set the`"keep_output": true` metadata on the cell. To do this, select the "Edit Metadata" Cell Toolbar, and then use the "Edit Metadata" button on the desired cell to enter something like:

{
"keep_output": true,
}

Another use-case is to preserve initialization cells that might load customized CSS etc. critical for the display of the notebook. To support this, we also keep output for cells with:

{
"init_cell": true,
}

This is the same metadata used by the [init_cell nbextension](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/init_cell).

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='70'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1012' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#stripping-metadata)Stripping metadata

This is configurable via git config (--global) filter.nbstripout.extrakeys. An example would be:

git config --global filter.nbstripout.extrakeys '
metadata.celltoolbar metadata.kernel_spec.display_name
metadata.kernel_spec.name metadata.language_info.codemirror_mode.version
metadata.language_info.pygments_lexer metadata.language_info.version
metadata.toc metadata.notify_time metadata.varInspector
cell.metadata.heading_collapsed cell.metadata.hidden
cell.metadata.code_folding cell.metadata.tags cell.metadata.init_cell'

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='71'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1015' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#manual-filter-installation)Manual filter installation

Set up a git filter using nbstripout as follows:
git config filter.nbstripout.clean '/path/to/nbstripout'
git config filter.nbstripout.smudge cat
git config filter.nbstripout.required true
Create a file `.gitattributes` or `.git/info/attributes` with:
*.ipynb filter=nbstripout
Apply the filter for git diff of `*.ipynb` files:
git config diff.ipynb.textconv '/path/to/nbstripout -t'
In file `.gitattributes` or `.git/info/attributes` add:
*.ipynb diff=ipynb

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='72'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1021' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/kynan/nbstripout#mercurial-usage)Mercurial usage

Mercurial does not have the equivalent of smudge filters. One can use an encode/decode hook but this has some issues. An alternative solution is to provide a set of commands that first run `nbstripout`, then perform these operations. This is the approach of the [mmf-setup](http://bitbucket.org/mforbes/mmf_setup)package.