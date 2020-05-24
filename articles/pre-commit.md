pre-commit

#  Introduction [¶](https://pre-commit.com/#introduction)

Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

As we created more libraries and projects we recognized that sharing our pre-commit hooks across projects is painful. We copied and pasted unwieldy bash scripts from project to project and had to manually change the hooks to work for different project structures.

We believe that you should always use the best industry standard linters. Some of the best linters are written in languages that you do not use in your project or have installed on your machine. For example scss-lint is a linter for SCSS written in Ruby. If you’re writing a project in node you should be able to use scss-lint as a pre-commit hook without adding a Gemfile to your project or understanding how to get scss-lint installed.

We built pre-commit to solve our hook issues. It is a multi-language package manager for pre-commit hooks. You specify a list of hooks you want and pre-commit manages the installation and execution of any hook written in any language before every commit. pre-commit is specifically designed to not require root access. If one of your developers doesn’t have node installed but modifies a JavaScript file, pre-commit automatically handles downloading and building node to run eslint without root.

#  Installation [¶](https://pre-commit.com/#installation)

Before you can run hooks, you need to have the pre-commit package manager installed.

Using pip:
pip install pre-commit
Non-administrative installation:

- *to upgrade: run again, to uninstall: pass `uninstall` to python*
- *does not work on platforms without symlink support (windows)*

curl https://pre-commit.com/install-local.py | python -

In a python project, add the following to your requirements.txt (or requirements-dev.txt):

pre-commit
Using [homebrew](https://brew.sh/):
brew install pre-commit
Using [conda](https://conda.io/) (via [conda-forge](https://conda-forge.org/)):
conda install -c conda-forge pre-commit

##  Quick start [¶](https://pre-commit.com/#quick-start)

###  1. Install pre-commit [¶](https://pre-commit.com/#1-install-pre-commit)

- follow the [install](https://pre-commit.com/#install) instructions above
- `pre-commit --version` should show you what version you're using

$ pre-commit --version
pre-commit 2.2.0

###  2. Add a pre-commit configuration [¶](https://pre-commit.com/#2-add-a-pre-commit-configuration)

- create a file named `.pre-commit-config.yaml`
- you can generate a very basic configuration using[`pre-commit sample-config`](https://pre-commit.com/#pre-commit-sample-config)
- the full set of options for the configuration are listed [below](https://pre-commit.com/#plugins)
- this example uses a formatter for python code, however `pre-commit` works for any programming language
- other [supported hooks](https://pre-commit.com/hooks.html) are available

repos:-  repo:  https://github.com/pre-commit/pre-commit-hooks  rev:  v2.3.0  hooks:  -  id:  check-yaml  -  id:  end-of-file-fixer  -  id:  trailing-whitespace-  repo:  https://github.com/psf/black  rev:  19.3b0  hooks:  -  id:  black

###  3. Install the git hook scripts [¶](https://pre-commit.com/#3-install-the-git-hook-scripts)

- run `pre-commit install` to set up the git hook scripts

$ pre-commit installpre-commit installed at .git/hooks/pre-commit

- now `pre-commit` will run automatically on `git commit`!

###  4. (optional) Run against all the files [¶](https://pre-commit.com/#4-optional-run-against-all-the-files)

- it's usually a good idea to run the hooks against all of the files when adding new hooks (usually `pre-commit` will only run on the changed files during git hooks)

$ pre-commit run --all-files

[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.

[INFO] Initializing environment for https://github.com/psf/black.

[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.

[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...

Check Yaml...............................................................PassedFix End of Files.........................................................PassedTrim Trailing Whitespace.................................................Failed- hook id: trailing-whitespace- exit code: 1Files were modified by this hook. Additional output:

Fixing sample.py
black....................................................................Passed

- oops! looks like I had some trailing whitespace
- consider running that in [CI](https://pre-commit.com/#usage-in-continuous-integration) too

#  Adding pre-commit plugins to your project [¶](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project)

Once you have pre-commit installed, adding pre-commit plugins to your project is done with the `.pre-commit-config.yaml` configuration file.

Add a file called `.pre-commit-config.yaml` to the root of your project. The pre-commit config file describes what repositories and hooks are installed.

##  .pre-commit-config.yaml - top level [¶](https://pre-commit.com/#pre-commit-configyaml---top-level)

*new in 1.0.0*: The default configuration file top-level was changed from a list to a map. If you're using an old version of pre-commit, the top-level list is the same as the value of [`repos`](https://pre-commit.com/#pre-commit-configyaml---repos). If you'd like to migrate to the new configuration format, run[`pre-commit migrate-config`](https://pre-commit.com/#pre-commit-migrate-config) to automatically migrate your configuration.

[object Object]

A list of [repository mappings](https://pre-commit.com/#pre-commit-configyaml---repos).

[object Object]

(optional: default [object Object]) a mapping from language to the default[object Object] that should be used for that language. This will only override individual hooks that do not set [object Object].

For example to use [object Object] for [object Object] hooks:
default_language_version:  python:  python3.7
*new in 1.14.0*
[object Object]

(optional: default (all stages)) a configuration-wide default for the [object Object] property of hooks. This will only override individual hooks that do not set [object Object].

For example:
default_stages:  [commit,  push]
*new in 1.14.0*
[object Object]

(optional: default [object Object]) global file include pattern. *new in 1.21.0*.

[object Object]

(optional: default [object Object]) global file exclude pattern. *new in 1.1.0*.

[object Object]

(optional: default [object Object]) set to [object Object] to have pre-commit stop running hooks after the first failure. *new in 1.1.0*.

[object Object]

(optional: default [object Object]) require a minimum version of pre-commit.*new in 1.15.0*.

A sample top-level:
exclude:  '^$'fail_fast:  falserepos:-  ...

##  .pre-commit-config.yaml - repos [¶](https://pre-commit.com/#pre-commit-configyaml---repos)

The repository mapping tells pre-commit where to get the code for the hook from.

[object Object]
the repository url to [object Object] from
[object Object]
the revision or tag to clone at. *new in 1.7.0*: previously [object Object]
[object Object]

A list of [hook mappings](https://pre-commit.com/#pre-commit-configyaml---hooks).

A sample repository with all defaults present:

repos:-  repo:  https://github.com/pre-commit/pre-commit-hooks  rev:  v1.2.3  hooks:  -  ...

##  .pre-commit-config.yaml - hooks [¶](https://pre-commit.com/#pre-commit-configyaml---hooks)

The hook mapping configures which hook from the repository is used and allows for customization. All optional keys will receive their default from the repository's configuration.

[object Object]
which hook from the repository to use.
[object Object]

(optional) allows the hook to be referenced using an additional id when using [object Object].*new in 1.14.0*.

[object Object]
(optional) override the name of the hook - shown during hook execution.
[object Object]

(optional) override the language version for the hook. See [Overriding Language Version](https://pre-commit.com/#overriding-language-version).

[object Object]
(optional) override the default pattern for files to run on.
[object Object]
(optional) file exclude pattern.
[object Object]

(optional) override the default file types to run on. See[Filtering files with types](https://pre-commit.com/#filtering-files-with-types).

[object Object]
(optional) file types to exclude.
[object Object]
(optional) list of additional parameters to pass to the hook.
[object Object]

(optional) confines the hook to the [object Object], [object Object], [object Object],[object Object], [object Object], [object Object], or [object Object] stage. See[Confining hooks to run at certain stages](https://pre-commit.com/#confining-hooks-to-run-at-certain-stages).

[object Object]

(optional) a list of dependencies that will be installed in the environment where this hook gets run. One useful application is to install plugins for hooks such as [object Object].

[object Object]

(optional) if [object Object], this hook will run even if there are no matching files.

[object Object]

(optional) if [object Object], forces the output of the hook to be printed even when the hook passes. *new in 1.6.0*.

[object Object]
(optional) if present, the hook output will additionally be written to a file.
One example of a complete configuration:

repos:-  repo:  https://github.com/pre-commit/pre-commit-hooks  rev:  v1.2.3  hooks:  -  id:  trailing-whitespace

This configuration says to download the pre-commit-hooks project and run its trailing-whitespace hook.

##  Updating hooks automatically [¶](https://pre-commit.com/#updating-hooks-automatically)

You can update your hooks to the latest version automatically by running[`pre-commit autoupdate`](https://pre-commit.com/#pre-commit-autoupdate). By default, this will bring the hooks to the latest tag on the master branch.

#  Usage [¶](https://pre-commit.com/#usage)

Run `pre-commit install` to install pre-commit into your git hooks. pre-commit will now run on every commit. Every time you clone a project using pre-commit running `pre-commit install` should always be the first thing you do.

If you want to manually run all pre-commit hooks on a repository, run`pre-commit run --all-files`. To run individual hooks use`pre-commit run <hook_id>`.

The first time pre-commit runs on a file it will automatically download, install, and run the hook. Note that running a hook for the first time may be slow. For example: If the machine does not have node installed, pre-commit will download and build a copy of node.

$ pre-commit install
pre-commit installed at /home/asottile/workspace/pytest/.git/hooks/pre-commit
$ git commit -m "Add super awesome feature"

black....................................................................Passedblacken-docs.........................................(no files to check)SkippedTrim Trailing Whitespace.................................................PassedFix End of Files.........................................................PassedCheck Yaml...........................................(no files to check)SkippedDebug Statements (Python)................................................PassedFlake8...................................................................PassedReorder python imports...................................................Passedpyupgrade................................................................Passedrst ``code`` is two backticks........................(no files to check)Skippedrst..................................................(no files to check)Skippedchangelog filenames..................................(no files to check)Skipped[master 146c6c2c] Add super awesome feature

1 file changed, 1 insertion(+)

#  Creating new hooks [¶](https://pre-commit.com/#creating-new-hooks)

pre-commit currently supports hooks written in[many languages](https://pre-commit.com/#supported-languages). As long as your git repo is an installable package (gem, npm, pypi, etc.) or exposes an executable, it can be used with pre-commit. Each git repo can support as many languages/hooks as you want.

The hook must exit nonzero on failure or modify files in the working directory.

A git repo containing pre-commit plugins must contain a .pre-commit-hooks.yaml file that tells pre-commit:

[object Object]
the id of the hook - used in pre-commit-config.yaml.
[object Object]
the name of the hook - shown during hook execution.
[object Object]

the entry point - the executable to run. [object Object] can also contain arguments that will not be overridden such as [object Object].

[object Object]
the language of the hook - tells pre-commit how to install the hook.
[object Object]
(optional: default [object Object]) the pattern of files to run on.
[object Object]

(optional: default [object Object]) exclude files that were matched by [object Object].

[object Object]

(optional: default [object Object]) list of file types to run on. See[Filtering files with types](https://pre-commit.com/#filtering-files-with-types).

[object Object]

(optional: default [object Object]) exclude files that were matched by [object Object].

[object Object]

(optional: default [object Object]) if [object Object] this hook will run even if there are no matching files.

[object Object]

(optional) if [object Object], forces the output of the hook to be printed even when the hook passes. *new in 1.6.0*.

[object Object]

(optional: default [object Object]) if [object Object] no arguments will be passed to the hook.

[object Object]

(optional: default [object Object]) if [object Object] this hook will execute using a single process instead of in parallel. *new in 1.13.0*.

[object Object]

(optional: default [object Object]) description of the hook. used for metadata purposes only.

[object Object]

(optional: default [object Object]) see[Overriding language version](https://pre-commit.com/#overriding-language-version).

[object Object]

(optional: default [object Object]) allows one to indicate a minimum compatible pre-commit version.

[object Object]

(optional: default [object Object]) list of additional parameters to pass to the hook.

For example:

- id:  trailing-whitespace  name:  Trim Trailing Whitespace  description:  This hook trims trailing whitespace.  entry:  trailing-whitespace-fixer  language:  python  types:  [text]

##  Developing hooks interactively [¶](https://pre-commit.com/#developing-hooks-interactively)

Since the `repo` property of `.pre-commit-config.yaml` can refer to anything that `git clone ...` understands, it's often useful to point it at a local directory while developing hooks.

[`pre-commit try-repo`](https://pre-commit.com/#pre-commit-try-repo) streamlines this process by enabling a quick way to try out a repository. Here's how one might work interactively:

*note*: you may need to provide `--commit-msg-filename` when using this command with hook types `prepare-commit-msg` and `commit-msg`.

*new in 1.14.0*: a commit is no longer necessary to `try-repo` on a local directory. `pre-commit` will clone any uncommitted changes.

~/work/hook-repo $ git checkout origin/master -b feature

# ... make some changes

# new in 1.14.0: a commit is no longer necessary for `try-repo`

# In another terminal or tab

~/work/other-repo $ pre-commit try-repo ../hook-repo foo --verbose --all-files
===============================================================================
Using config:
===============================================================================
repos:

- repo: ../hook-repo

rev: 84f01ac09fcd8610824f9626a590b83cfae9bcbd
hooks:

- id: foo

===============================================================================
[INFO] Initializing environment for ../hook-repo.

Foo......................................................................Passed- hook id: foo- duration: 0.02sHello from foo hook!

##  Supported languages [¶](https://pre-commit.com/#supported-languages)

- [conda](https://pre-commit.com/#conda)
- [docker](https://pre-commit.com/#docker)
- [docker_image](https://pre-commit.com/#docker_image)
- [fail](https://pre-commit.com/#fail)
- [golang](https://pre-commit.com/#golang)
- [node](https://pre-commit.com/#node)
- [perl](https://pre-commit.com/#perl)
- [python](https://pre-commit.com/#python)
- [python_venv](https://pre-commit.com/#python_venv)
- [ruby](https://pre-commit.com/#ruby)
- [rust](https://pre-commit.com/#rust)
- [swift](https://pre-commit.com/#swift)
- [pygrep](https://pre-commit.com/#pygrep)
- [script](https://pre-commit.com/#script)
- [system](https://pre-commit.com/#system)

###  conda [¶](https://pre-commit.com/#conda)

*new in 1.21.0*

The hook repository must contain an `environment.yml` file which will be used via `conda env create --file environment.yml ...` to create the environment.

The `conda` language also supports `additional_dependencies` and will pass any of the values directly into `conda install`. This language can therefore be used with [local](https://pre-commit.com/#repository-local-hooks) hooks.

**Support:**  `conda` hooks work as long as there is a system-installed `conda`binary (such as [`miniconda`](https://docs.conda.io/en/latest/miniconda.html)). It has been tested on linux, macOS, and windows.

###  docker [¶](https://pre-commit.com/#docker)

The hook repository must have a `Dockerfile`. It will be installed via`docker build .`.

Running Docker hooks requires a running Docker engine on your host. For configuring Docker hooks, your `entry` should correspond to an executable inside the Docker container, and will be used to override the default container entrypoint. Your Docker `CMD` will not run when pre-commit passes a file list as arguments to the run container command. Docker allows you to use any language that's not supported by pre-commit as a builtin.

pre-commit will automatically mount the repository source as a volume using`-v $PWD:/src:rw,Z` and set the working directory using `--workdir /src`.

**Support:** docker hooks are known to work on any system which has a working`docker` executable. It has been tested on linux and macOS. Hooks that are run via `boot2docker` are known to be unable to make modifications to files.

See [this repository](https://github.com/pre-commit/pre-commit-docker-flake8)for an example Docker-based hook.

###  docker_image [¶](https://pre-commit.com/#docker_image)

A more lightweight approach to `docker` hooks. The `docker_image`"language" uses existing docker images to provide hook executables.

`docker_image` hooks can be conveniently configured as [local](https://pre-commit.com/#repository-local-hooks)hooks.

The `entry` specifies the docker tag to use. If an image has an`ENTRYPOINT` defined, nothing special is needed to hook up the executable. If the container does not specify an `ENTRYPOINT` or you want to change the entrypoint you can specify it as well in your `entry`.

For example:

- id:  dockerfile-provides-entrypoint  name:  ...  language:  docker_image  entry:  my.registry.example.com/docker-image-1:latest-  id:  dockerfile-no-entrypoint-1  name:  ...  language:  docker_image  entry:  --entrypoint my-exe my.registry.example.com/docker-image-2:latest# Alternative equivalent solution-  id:  dockerfile-no-entrypoint-2  name:  ...  language:  docker_image  entry:  my.registry.example.com/docker-image-3:latest my-exe

###  fail [¶](https://pre-commit.com/#fail)

*new in 1.11.0*

A lightweight `language` to forbid files by filename. The `fail` language is especially useful for [local](https://pre-commit.com/#repository-local-hooks) hooks.

The `entry` will be printed when the hook fails. It is suggested to provide a brief description for `name` and more verbose fix instructions in `entry`.

Here's an example which prevents any file except those ending with `.rst` from being added to the `changelog` directory:

- repo:  local  hooks:  -  id:  changelogs-rst  name:  changelogs must be rst  entry:  changelog filenames must end in .rst  language:  fail  files:  'changelog/.*(?<!\.rst)$'

###  golang [¶](https://pre-commit.com/#golang)

The hook repository must contain go source code. It will be installed via`go get ./...`. pre-commit will create an isolated `GOPATH` for each hook and the `entry` should match an executable which will get installed into the`GOPATH`'s `bin` directory.

**Support:** golang hooks are known to work on any system which has go installed. It has been tested on linux, macOS, and windows.

###  node [¶](https://pre-commit.com/#node)

The hook repository must have a `package.json`. It will be installed via`npm install .`. The installed package will provide an executable that will match the `entry` – usually through `bin` in package.json.

**Support:** node hooks work without any system-level dependencies. It has been tested on linux and macOS and *may* work under cygwin.

*new in 1.5.0*: windows is now supported for node hooks. Currently python3 only due to [a bug in cpython](https://bugs.python.org/issue32539).

###  perl [¶](https://pre-commit.com/#perl)

*new in 2.1.0*

Perl hooks are installed using the system installation of[cpan](https://perldoc.perl.org/5.30.0/cpan.html), the CPAN package installer that comes with Perl.

Hook repositories must have something that `cpan` supports, typically`Makefile.PL` or `Build.PL`, which it uses to install an executable to use in the `entry` definition for your hook. The repository will be installed via `cpan -T .` (with the installed files stored in your pre-commit cache, not polluting other Perl installations).

When specifying `additional_dependencies` for Perl, you can use any of the[install argument formats understood by `cpan`](https://perldoc.perl.org/5.30.0/CPAN.html#get%2c-make%2c-test%2c-install%2c-clean-modules-or-distributions).

**Support:** Perl hooks currently require a pre-existing Perl installation, including the `cpan` tool in `PATH`. It has been tested on linux, macOS, and Windows.

###  python [¶](https://pre-commit.com/#python)

The hook repository must be installable via `pip install .` (usually by either`setup.py` or `pyproject.toml`). The installed package will provide an executable that will match the `entry` – usually through `console_scripts` or`scripts` in setup.py.

**Support:** python hooks work without any system-level dependencies. It has been tested on linux, macOS, windows, and cygwin.

###  python_venv [¶](https://pre-commit.com/#python_venv)

*new in 1.9.0*

An alternate implementation of the [python](https://pre-commit.com/#python) language which uses the python 3 [`venv`](https://docs.python.org/3/library/venv.html) module. On many systems you need to additionally install the `python3-venv` system package to use this language. This is otherwise a drop-in replacement for the`python` language for situations where [`virtualenv` may not work](https://github.com/pre-commit/pre-commit/issues/631).

**Support:** python hooks work without any system-level dependencies. It has been tested on linux, macOS, windows, and cygwin. Only python3 environments can be created with this language.

###  ruby [¶](https://pre-commit.com/#ruby)

The hook repository must have a `*.gemspec`. It will be installed via`gem build *.gemspec && gem install *.gem`. The installed package will produce an executable that will match the `entry` – usually through`executables` in your gemspec.

**Support:** ruby hooks work without any system-level dependencies. It has been tested on linux and macOS and *may* work under cygwin.

###  rust [¶](https://pre-commit.com/#rust)

*new in 1.10.0*

Rust hooks are installed using the system installation of[Cargo](https://github.com/rust-lang/cargo), Rust's official package manager.

Hook repositories must have a `Cargo.toml` file which produces at least one binary ([example](https://github.com/chriskuehl/example-rust-pre-commit-hook)), whose name should match the `entry` definition for your hook. The repo will be installed via `cargo install --bins` (with the binaries stored in your pre-commit cache, not polluting your user-level Cargo installations).

When specifying `additional_dependencies` for Rust, you can use the syntax`{package_name}:{package_version}` to specify a new library dependency (used to build *your* hook repo), or the special syntax`cli:{package_name}:{package_version}` for a CLI dependency (built separately, with binaries made available for use by hooks).

**Support:** Rust hooks currently require a pre-existing Rust installation. It has been tested on linux, Windows, and macOS.

###  swift [¶](https://pre-commit.com/#swift)

The hook repository must have a `Package.swift`. It will be installed via`swift build -c release`. The `entry` should match an executable created by building the repository.

**Support:** swift hooks are known to work on any system which has swift installed. It has been tested on linux and macOS.

###  pygrep [¶](https://pre-commit.com/#pygrep)

*new in 1.2.0*

A cross-platform python implementation of `grep` – pygrep hooks are a quick way to write a simple hook which prevents commits by file matching. Specify the regex as the `entry`. The `entry` may be any python[regular expression](https://pre-commit.com/#regular-expressions). For case insensitive regexes you can apply the `(?i)` flag as the start of your entry, or use `args: [-i]`.

*new in 1.8.0*: For multiline matches, use `args: [--multiline]`.

**Support:** pygrep hooks are supported on all platforms which pre-commit runs on.

###  script [¶](https://pre-commit.com/#script)

Script hooks provide a way to write simple scripts which validate files. The`entry` should be a path relative to the root of the hook repository.

This hook type will not be given a virtual environment to work with – if it needs additional dependencies the consumer must install them manually.

**Support:** the support of script hooks depend on the scripts themselves.

###  system [¶](https://pre-commit.com/#system)

System hooks provide a way to write hooks for system-level executables which don't have a supported language above (or have special environment requirements that don't allow them to run in isolation such as pylint).

This hook type will not be given a virtual environment to work with – if it needs additional dependencies the consumer must install them manually.

**Support:** the support of system hooks depend on the executables.

#  Command line interface [¶](https://pre-commit.com/#command-line-interface)

All pre-commit commands take the following options:

- `--color {auto,always,never}`: whether to use color in output. Defaults to `auto`. *new in 1.18.0*: can be overridden by using`PRE_COMMIT_COLOR={auto,always,never}` or disabled using `TERM=dumb`.
- `-c CONFIG`, `--config CONFIG`: path to alternate config file
- `-h`, `--help`: show help and available options.

##  pre-commit autoupdate [options] [(L)](https://pre-commit.com/#pre-commit-autoupdate)  [¶](https://pre-commit.com/#pre-commit-autoupdate)

Auto-update pre-commit config to the latest repos' versions.
Options:

- `--bleeding-edge`: update to the bleeding edge of `master` instead of the latest tagged version (the default behaviour).
- `--freeze`: *new in 1.21.0*): Store "frozen" hashes in `rev` instead of tag names.
- `--repo REPO`: *new in 1.4.1*: Only update this repository. *new in 1.7.0*: This option may be specified multiple times.

Here are some sample invocations using this `.pre-commit-config.yaml`:

repos:-  repo:  https://github.com/pre-commit/pre-commit-hooks  rev:  v2.1.0  hooks:  -  id:  trailing-whitespace-  repo:  https://github.com/asottile/pyupgrade  rev:  v1.25.0  hooks:  -  id:  pyupgrade  args:  [--py36-plus]

$ : default: update to latest tag on default branch$ pre-commit autoupdate # by default: pick tagsUpdating https://github.com/pre-commit/pre-commit-hooks ... updating v2.1.0 -> v2.4.0.Updating https://github.com/asottile/pyupgrade ... updating v1.25.0 -> v1.25.2.$ grep rev: .pre-commit-config.yaml rev: v2.4.0 rev: v1.25.2

$ : update a specific repository to the latest revision of the default branch$ pre-commit autoupdate --bleeding-edge --repo https://github.com/pre-commit/pre-commit-hooksUpdating https://github.com/pre-commit/pre-commit-hooks ... updating v2.1.0 -> 5df1a4bf6f04a1ed3a643167b38d502575e29aef.$ grep rev: .pre-commit-config.yaml rev: 5df1a4bf6f04a1ed3a643167b38d502575e29aef rev: v1.25.0

$ : update to frozen versions$ pre-commit autoupdate --freezeUpdating https://github.com/pre-commit/pre-commit-hooks ... updating v2.1.0 -> v2.4.0 (frozen).Updating https://github.com/asottile/pyupgrade ... updating v1.25.0 -> v1.25.2 (frozen).$ grep rev: .pre-commit-config.yaml rev: 0161422b4e09b47536ea13f49e786eb3616fe0d7 # frozen: v2.4.0 rev: 34a269fd7650d264e4de7603157c10d0a9bb8211 # frozen: v1.25.2

##  pre-commit clean [options] [(L)](https://pre-commit.com/#pre-commit-clean)  [¶](https://pre-commit.com/#pre-commit-clean)

Clean out cached pre-commit files.
Options: (no additional options)

##  pre-commit gc [options] [(L)](https://pre-commit.com/#pre-commit-gc)  [¶](https://pre-commit.com/#pre-commit-gc)

*new in 1.14.0*
Clean unused cached repos.

`pre-commit` keeps a cache of installed hook repositories which grows over time. This command can be run periodically to clean out unused repos from the cache directory.

Options: (no additional options)

##  pre-commit init-templatedir DIRECTORY [options] [(L)](https://pre-commit.com/#pre-commit-init-templatedir)  [¶](https://pre-commit.com/#pre-commit-init-templatedir)

*new in 1.18.0*

Install hook script in a directory intended for use with`git config init.templateDir`.

Options:

- `-t {pre-commit,pre-merge-commit,pre-push,prepare-commit-msg,commit-msg,post-checkout}`,`--hook-type {pre-commit,pre-merge-commit,pre-push,prepare-commit-msg,commit-msg,post-checkout}`: which hook type to install.

Some example useful invocations:
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template

Now whenever a repository is cloned or created, it will have the hooks set up already!

##  pre-commit install [options] [(L)](https://pre-commit.com/#pre-commit-install)  [¶](https://pre-commit.com/#pre-commit-install)

Install the pre-commit script.
Options:

- `-f`, `--overwrite`: Replace any existing git hooks with the pre-commit script.
- `--install-hooks`: Also install environments for all available hooks now (rather than when they are first executed). See [`pre-commit install-hooks`](https://pre-commit.com/#pre-commit-install-hooks).
- `-t {pre-commit,pre-merge-commit,pre-push,prepare-commit-msg,commit-msg,post-checkout}`,`--hook-type {pre-commit,pre-merge-commit,pre-push,prepare-commit-msg,commit-msg,post-checkout}`: Specify which hook type to install.
- `--allow-missing-config`: Hook scripts will permit a missing configuration file.

Some example useful invocations:

- `pre-commit install`: Default invocation. Installs the pre-commit script alongside any existing git hooks.
- `pre-commit install --install-hooks --overwrite`: Idempotently replaces existing git hook scripts with pre-commit, and also installs hook environments.

##  pre-commit install-hooks [options] [(L)](https://pre-commit.com/#pre-commit-install-hooks)  [¶](https://pre-commit.com/#pre-commit-install-hooks)

Install all missing environments for the available hooks. Unless this command or`install --install-hooks` is executed, each hook's environment is created the first time the hook is called.

Each hook is initialized in a separate environment appropriate to the language the hook is written in. See [supported languages](https://pre-commit.com/#supported-languages).

This command does not install the pre-commit script. To install the script along with the hook environments in one command, use `pre-commit install --install-hooks`.

Options: (no additional options)

##  pre-commit migrate-config [options] [(L)](https://pre-commit.com/#pre-commit-migrate-config)  [¶](https://pre-commit.com/#pre-commit-migrate-config)

*new in 1.0.0*
Migrate list configuration to the new map configuration format.
Options: (no additional options)

##  pre-commit run [hook-id] [options] [(L)](https://pre-commit.com/#pre-commit-run)  [¶](https://pre-commit.com/#pre-commit-run)

Run hooks.
Options:

- `[hook-id]`: specify a single hook-id to run only that hook.
- `-a`, `--all-files`: run on all the files in the repo.
- `--files [FILES [FILES ...]]`: specific filenames to run hooks on.
- `--from-ref FROM_REF` + `--to-ref TO_REF`: run against the files changed between `FROM_REF...TO_REF` in git.
    - *new in 2.2.0*: prior to 2.2.0 the arguments were `--source` and`--origin`.
- `--show-diff-on-failure`: when hooks fail, run `git diff` directly afterward.
- `-v`, `--verbose`: produce hook output independent of success. Include hook ids in output.

Some example useful invocations:

- `pre-commit run`: this is what pre-commit runs by default when committing. This will run all hooks against currently staged files.
- `pre-commit run --all-files`: run all the hooks against all the files. This is a useful invocation if you are using pre-commit in CI.
- `pre-commit run flake8`: run the `flake8` hook against all staged files.
- `git ls-files -- '*.py' | xargs pre-commit run --files`: run all hooks against all `*.py` files in the repository.
- `pre-commit run --from-ref HEAD^^^ --to-ref HEAD`: run against the files that have changed between `HEAD^^^` and `HEAD`. This form is useful when leveraged in a pre-receive hook.

##  pre-commit sample-config [options] [(L)](https://pre-commit.com/#pre-commit-sample-config)  [¶](https://pre-commit.com/#pre-commit-sample-config)

Produce a sample `.pre-commit-config.yaml`.
Options: (no additional options)

##  pre-commit try-repo REPO [options] [(L)](https://pre-commit.com/#pre-commit-try-repo)  [¶](https://pre-commit.com/#pre-commit-try-repo)

*new in 1.3.0*

Try the hooks in a repository, useful for developing new hooks.`try-repo` can also be used for testing out a repository before adding it to your configuration. `try-repo` prints a configuration it generates based on the remote hook repository before running the hooks.

Options:

- `REPO`: required clonable hooks repository. Can be a local path on disk.
- `--ref REF`: Manually select a ref to run against, otherwise the `HEAD`revision will be used.
- `pre-commit try-repo` also supports all available options for[`pre-commit run`](https://pre-commit.com/#pre-commit-run).

Some example useful invocations:

- `pre-commit try-repo https://github.com/pre-commit/pre-commit-hooks`: runs all the hooks in the latest revision of `pre-commit/pre-commit-hooks`.
- `pre-commit try-repo ../path/to/repo`: run all the hooks in a repository on disk.
- `pre-commit try-repo ../pre-commit-hooks flake8`: run only the `flake8` hook configured in a local `../pre-commit-hooks` repository.
- See [`pre-commit run`](https://pre-commit.com/#pre-commit-run) for more useful `run` invocations which are also supported by `pre-commit try-repo`.

##  pre-commit uninstall [options] [(L)](https://pre-commit.com/#pre-commit-uninstall)  [¶](https://pre-commit.com/#pre-commit-uninstall)

Uninstall the pre-commit script.
Options:

- `-t {pre-commit,pre-merge-commit,pre-push,prepare-commit-msg,commit-msg}`,`--hook-type {pre-commit,pre-merge-commit,pre-push,prepare-commit-msg,commit-msg}`: which hook type to uninstall.

#  Advanced features [¶](https://pre-commit.com/#advanced-features)

##  Running in migration mode [¶](https://pre-commit.com/#running-in-migration-mode)

By default, if you have existing hooks `pre-commit install` will install in a migration mode which runs both your existing hooks and hooks for pre-commit. To disable this behavior, pass `-f` / `--overwrite` to the `install` command. If you decide not to use pre-commit, `pre-commit uninstall` will restore your hooks to the state prior to installation.

##  Temporarily disabling hooks [¶](https://pre-commit.com/#temporarily-disabling-hooks)

Not all hooks are perfect so sometimes you may need to skip execution of one or more hooks. pre-commit solves this by querying a `SKIP` environment variable. The `SKIP` environment variable is a comma separated list of hook ids. This allows you to skip a single hook instead of `--no-verify`ing the entire commit.

$  SKIP=flake8 git commit -m "foo"

##  pre-commit during commits [¶](https://pre-commit.com/#pre-commit-during-commits)

Running hooks on unstaged changes can lead to both false-positives and false-negatives during committing. pre-commit only runs on the staged contents of files by temporarily saving the contents of your files at commit time and stashing the unstaged changes while running hooks.

##  pre-commit during merges [¶](https://pre-commit.com/#pre-commit-during-merges)

The biggest gripe we’ve had in the past with pre-commit hooks was during merge conflict resolution. When working on very large projects a merge often results in hundreds of committed files. I shouldn’t need to run hooks on all of these files that I didn’t even touch! This often led to running commit with `--no-verify` and allowed introduction of real bugs that hooks could have caught.

pre-commit solves this by only running hooks on files that conflict or were manually edited during conflict resolution. This also includes files which were automatically merged by git. Git isn't perfect and this can often catch implicit conflicts (such as with removed python imports).

##  pre-commit during clean merges [¶](https://pre-commit.com/#pre-commit-during-clean-merges)

*new in 1.21.0* pre-commit can be used to manage [pre-merge-commit](https://git-scm.com/docs/githooks#_pre_merge_commit) hooks.

To use `pre-merge-commit` hooks with pre-commit, run:

$ pre-commit install --hook-type pre-merge-commitpre-commit installed at .git/hooks/pre-merge-commit

The hook fires after a merge succeeds but before the merge commit is created.

Note that you need to be using at least git 2.24 which added support for the pre-merge-commit hook.

##  pre-commit during push [¶](https://pre-commit.com/#pre-commit-during-push)

To use `pre-push` hooks with pre-commit, run:

$ pre-commit install --hook-type pre-pushpre-commit installed at .git/hooks/pre-push

During a push, pre-commit will export the following environment variables:

- `PRE_COMMIT_FROM_REF`: the remote revision that is being pushed to.
    - *new in 2.2.0* prior to 2.2.0 the variable was `PRE_COMMIT_SOURCE`.
- `PRE_COMMIT_TO_REF`: the local revision that is being pushed to the remote.
    - *new in 2.2.0* prior to 2.2.0 the variable was `PRE_COMMIT_ORIGIN`.
- `PRE_COMMIT_REMOTE_NAME`: *new in 2.0.0* which remote is being pushed to (for example `origin`)
- `PRE_COMMIT_REMOTE_URL`: *new in 2.0.0* the url of the remote that is being pushed to (for example `git@github.com:pre-commit/pre-commit`.

##  pre-commit for commit messages [¶](https://pre-commit.com/#pre-commit-for-commit-messages)

pre-commit can be used to manage [commit-msg](https://git-scm.com/docs/githooks#_commit_msg) hooks.

To use `commit-msg` hooks with pre-commit, run:

$ pre-commit install --hook-type commit-msgpre-commit installed at .git/hooks/commit-msg

`commit-msg` hooks can be configured by setting `stages: [commit-msg]`.`commit-msg` hooks will be passed a single filename -- this file contains the current contents of the commit message which can be validated. If a hook exits nonzero, the commit will be aborted.

*new in 1.16.0*: pre-commit can be used to manage [prepare-commit-msg](https://git-scm.com/docs/githooks#_prepare_commit_msg) hooks.

To use `prepare-commit-msg` hooks with pre-commit run:

$ pre-commit install --hook-type prepare-commit-msg`pre-commit installed at .git/hooks/prepare-commit-msg

`prepare-commit-msg` hooks can be used to create dynamic templates for commit messages. `prepare-commit-msg` hooks can be configured by setting`stages: [prepare-commit-msg]`. `prepare-commit-msg` hooks will be passed a single filename -- this file contains any initial commit message (e.g. from`git commit -m "..."` or a template) and can be modified by the hook before the editor is shown. A hook may want to check for `GIT_EDITOR=:` as this indicates that no editor will be launched. If a hook exits nonzero, the commit will be aborted.

##  pre-commit for switching branches [¶](https://pre-commit.com/#pre-commit-for-switching-branches)

*new in 2.2.0*: pre-commit can be used to manage [post-checkout](https://git-scm.com/docs/githooks#_post_checkout) hooks.

To use `post-checkout` hooks with pre-commit run:

$ pre-commit install --hook-type post-checkoutpre-commit installed at .git/hooks/post-checkout

`post-checkout` hooks can be used to perform repository validity checks, auto-display differences from the previous HEAD if different, or set working dir metadata properties. Since `post-checkout` doesn't operate on files, any hooks must set `always_run`:

- repo:  local  hooks:  -  id:  post-checkout-local  name:  Post checkout  always_run:  true  stages:  [post-checkout]  # ...

`post-checkout` hooks have three environment variables they can check to do their work: `$PRE_COMMIT_FROM_REF`, `$PRE_COMMIT_TO_REF`, and `$PRE_COMMIT_CHECKOUT_TYPE`. These correspond to the first, second, and third arguments (respectively) that are normally passed to a regular post-checkout hook from Git.

##  Confining hooks to run at certain stages [¶](https://pre-commit.com/#confining-hooks-to-run-at-certain-stages)

Since the `default_stages` top level configuration property of the`.pre-commit-config.yaml` file is set to all stages by default, when installing hooks using the `-t`/`--hook-type` option (see [pre-commit install [options]](https://pre-commit.com/#pre-commit-install)), all hooks will be installed by default to run at the stage defined through that option. for instance,`pre-commit install --hook-type pre-push` will install by default all hooks to run at the `push` stage.

Hooks can however be confined to a stage by setting the `stages` property in your `.pre-commit-config.yaml`. The `stages` property is an array and can contain any of `commit`, `merge-commit`, `push`, `prepare-commit-msg`,`commit-msg` and `manual`.

If you do not want to have hooks installed by default on the stage passed during a `pre-commit install --hook-type ...`, please set the `default_stages`top level configuration property to the desired stages, also as an array.

*new in 1.8.0*: An additional `manual` stage is available for one off execution that won't run in any hook context. This special stage is useful for taking advantage of `pre-commit`'s cross-platform / cross-language package management without running it on every commit. Hooks confied to `stages: [manual]` can be executed by running `pre-commit run --hook-stage manual <hookid>`.

##  Passing arguments to hooks [¶](https://pre-commit.com/#passing-arguments-to-hooks)

Sometimes hooks require arguments to run correctly. You can pass static arguments by specifying the `args` property in your `.pre-commit-config.yaml`as follows:

- repo:  https://github.com/pre-commit/pre-commit-hooks  rev:  v1.2.3  hooks:  -  id:  flake8  args:  [--max-line-length=131]

This will pass `--max-line-length=131` to `flake8`.

###  Arguments pattern in hooks [¶](https://pre-commit.com/#arguments-pattern-in-hooks)

If you are writing your own custom hook, your hook should expect to receive the `args` value and then a list of staged files.

For example, assuming a `.pre-commit-config.yaml`:

- repo:  https://github.com/path/to/your/hook/repo  rev:  badf00ddeadbeef  hooks:  -  id:  my-hook-script-id  args:  [--myarg1=1,  --myarg1=2]

When you next run `pre-commit`, your script will be called:
path/to/script-or-system-exe --myarg1=1 --myarg1=2 dir/file1 dir/file2 file3
If the `args` property is empty or not defined, your script will be called:
path/to/script-or-system-exe dir/file1 dir/file2 file3

##  Repository local hooks [¶](https://pre-commit.com/#repository-local-hooks)

Repository-local hooks are useful when:

- The scripts are tightly coupled to the repository and it makes sense to distribute the hook scripts with the repository.
- Hooks require state that is only present in a built artifact of your repository (such as your app's virtualenv for pylint).
- The official repository for a linter doesn't have the pre-commit metadata.

You can configure repository-local hooks by specifying the `repo` as the sentinel `local`.

local hooks can use any language which supports `additional_dependencies` or`docker_image` / `fail` / `pygrep` / `script` / `system`. This enables you to install things which previously would require a trivial mirror repository.

A `local` hook must define `id`, `name`, `language`, `entry`, and `files` /`types` as specified under [Creating new hooks](https://pre-commit.com/#new-hooks).

Here's an example configuration with a few `local` hooks:

- repo:  local  hooks:  -  id:  pylint  name:  pylint  entry:  pylint  language:  system  types:  [python]  -  id:  check-x  name:  Check X  entry:  ./bin/check-x.sh  language:  script  files:  \.x$  -  id:  scss-lint  name:  scss-lint  entry:  scss-lint  language:  ruby  language_version:  2.1.5  types:  [scss]  additional_dependencies:  ['scss_lint:0.52.0']

##  meta hooks [¶](https://pre-commit.com/#meta-hooks)

*new in 1.4.0*

`pre-commit` provides several hooks which are useful for checking the pre-commit configuration itself. These can be enabled using `repo: meta`.

- repo:  meta  hooks:  -  id:  ...

The currently available `meta` hooks:
[object Object]

ensures that the configured hooks apply to at least one file in the repository.*new in 1.4.0*.

[object Object]

ensures that [object Object] directives apply to *any* file in the repository.*new in 1.4.0*.

[object Object]

a simple hook which prints all arguments passed to it, useful for debugging.*new in 1.14.0*.

##  automatically enabling pre-commit on repositories [¶](https://pre-commit.com/#automatically-enabling-pre-commit-on-repositories)

*new in 1.18.0*

`pre-commit init-templatedir` can be used to set up a skeleton for `git`'s`init.templateDir` option. This means that any newly cloned repository will automatically have the hooks set up without the need to run`pre-commit install`.

To configure, first set `git`'s `init.templateDir` -- in this example I'm using `~/.git-template` as my template directory.

$ git config --global init.templateDir ~/.git-template$ pre-commit init-templatedir ~/.git-templatepre-commit installed at /home/asottile/.git-template/hooks/pre-commit

Now whenever you clone a pre-commit enabled repo, the hooks will already be set up!

$ git clone -q git@github.com:asottile/pyupgrade
$ cd pyupgrade
$ git commit --allow-empty -m 'Hello world!'

Check docstring is first.............................(no files to check)SkippedCheck Yaml...........................................(no files to check)SkippedDebug Statements (Python)............................(no files to check)Skipped...

`init-templatedir` uses the `--allow-missing-config` option from`pre-commit install` so repos without a config will be skipped:

$ git init sampleInitialized empty Git repository in /tmp/sample/.git/$  cd sample$ git commit --allow-empty -m 'Initial commit'`.pre-commit-config.yaml` config file not found. Skipping `pre-commit`.[master (root-commit) d1b39c1] Initial commit

##  Filtering files with types [¶](https://pre-commit.com/#filtering-files-with-types)

Filtering with `types` provides several advantages over traditional filtering with `files`.

- no error-prone regular expressions
- files can be matched by their shebang (even when extensionless)
- symlinks / submodules can be easily ignored

`types` is specified per hook as an array of tags. The tags are discovered through a set of heuristics by the[identify](https://github.com/chriskuehl/identify) library. `identify` was chosen as it is a small portable pure python library.

Some of the common tags you'll find from identify:

- `file`
- `symlink`
- `directory` - in the context of pre-commit this will be a submodule
- `executable` - whether the file has the executable bit set
- `text` - whether the file looks like a text file
- `binary` - whether the file looks like a binary file
- [tags by extension / naming convention](https://github.com/chriskuehl/identify/blob/master/identify/extensions.py)
- [tags by shebang (`#!`)](https://github.com/chriskuehl/identify/blob/master/identify/interpreters.py)

To discover the type of any file on disk, you can use `identify`'s cli:

$ identify-cli setup.py["file", "non-executable", "python", "text"]$ identify-cli some-random-file["file", "non-executable", "text"]$ identify-cli --filename-only some-random-file;  echo  $?1

If a file extension you use is not supported, please[submit a pull request](https://github.com/chriskuehl/identify)!

`types` and `files` are evaluated with `AND` when filtering. Tags within`types` are also evaluated using `AND`.

For example:
 files:  ^foo/  types:  [file,  python]
will match a file `foo/1.py` but will not match `setup.py`.

If you want to match a file path that isn't included in a `type` when using an existing hook you'll need to revert back to `files` only matching by overriding the `types` setting. Here's an example of using `check-json` against non-json files:

 - id:  check-json  types:  [file]  # override `types: [json]`  files:  \.(json|myext)$

Files can also be matched by shebang. With `types: python`, an `exe` starting with `#!/usr/bin/env python3` will also be matched.

As with `files` and `exclude`, you can also exclude types if necessary using`exclude_types`.

If you'd like to use `types` with compatibility for older versions[here is a guide to ensuring compatibility](https://github.com/pre-commit/pre-commit/pull/551#issuecomment-312535540).

##  Regular expressions [¶](https://pre-commit.com/#regular-expressions)

The patterns for `files` and `exclude` are python[regular expressions](https://docs.python.org/3/library/re.html#regular-expression-syntax)and are matched with [`re.search`](https://docs.python.org/3/library/re.html#re.search).

As such, you can use any of the features that python regexes support.

If you find that your regular expression is becoming unwieldy due to a long list of excluded / included things, you may find a[verbose](https://docs.python.org/3/library/re.html#re.VERBOSE) regular expression useful. One can enable this with yaml's multiline literals and the `(?x)` regex flag.

# ...  -  id:  my-hook  exclude:  >  (?x)^(  path/to/file1.py|  path/to/file2.py|  path/to/file3.py  )$

##  Overriding language version [¶](https://pre-commit.com/#overriding-language-version)

Sometimes you only want to run the hooks on a specific version of the language. For each language, they default to using the system installed language (So for example if I’m running `python3.7` and a hook specifies`python`, pre-commit will run the hook using `python3.7`). Sometimes you don’t want the default system installed version so you can override this on a per-hook basis by setting the `language_version`.

- repo:  https://github.com/pre-commit/mirrors-scss-lint  rev:  v0.54.0  hooks:  -  id:  scss-lint  language_version:  2.1.5

This tells pre-commit to use ruby `2.1.5` to run the `scss-lint` hook.
Valid values for specific languages are listed below:

- python: Whatever system installed python interpreters you have. The value of this argument is passed as the `-p` to `virtualenv`.
    - *new in 1.4.3*: on windows the[pep394](https://www.python.org/dev/peps/pep-0394/) name will be translated into a py launcher call for portability. So continue to use names like `python3` (`py -3`) or `python3.6` (`py -3.6`) even on windows.
- node: See [nodeenv](https://github.com/ekalinin/nodeenv#advanced).
- ruby: See [ruby-build](https://github.com/sstephenson/ruby-build/tree/master/share/ruby-build).

*new in 1.14.0*: you can now set `default_language_version` at the[top level](https://pre-commit.com/#pre-commit-configyaml---top-level) in your configuration to control the default versions across all hooks of a language.

default_language_version:  # force all unspecified python hooks to run python3  python:  python3  # force all unspecified ruby hooks to run ruby 2.1.5  ruby:  2.1.5

##  badging your repository [¶](https://pre-commit.com/#badging-your-repository)

you can add a badge to your repository to show your contributors / users that you use pre-commit!

[![pre--commit-enabled-brightgreen](../_resources/ee547cd34245bcd3f86b3fc0c92b3289.png)](https://github.com/pre-commit/pre-commit)

- Markdown:

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

- HTML:

<a  href="https://github.com/pre-commit/pre-commit"><img  src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"  alt="pre-commit"  style="max-width:100%;"></a>

- reStructuredText:

..  image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white :target: https://github.com/pre-commit/pre-commit :alt: pre-commit

- AsciiDoc:

image:https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white[pre-commit, link=https://github.com/pre-commit/pre-commit]

##  Usage in continuous integration [¶](https://pre-commit.com/#usage-in-continuous-integration)

pre-commit can also be used as a tool for continuous integration. For instance, adding `pre-commit run --all-files` as a CI step will ensure everything stays in tip-top shape. To check only files which have changed, which may be faster, use something like`pre-commit run --from-ref origin.HEAD --to-ref HEAD`

##  Managing CI Caches [¶](https://pre-commit.com/#managing-ci-caches)

`pre-commit` by default places its repository store in `~/.cache/pre-commit`-- this can be configured in two ways:

- `PRE_COMMIT_HOME`: if set, pre-commit will use that location instead.
- `XDG_CACHE_HOME`: if set, pre-commit will use `$XDG_CACHE_HOME/pre-commit`following the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).

###  travis-ci example [¶](https://pre-commit.com/#travis-ci-example)

cache:  directories:  -  $HOME/.cache/pre-commit

###  appveyor example [¶](https://pre-commit.com/#appveyor-example)

cache:-  '%USERPROFILE%\.cache\pre-commit'

###  azure pipelines example [¶](https://pre-commit.com/#azure-pipelines-example)

note: azure pipelines uses immutable caches so the python version and`.pre-commit-config.yaml` hash must be included in the cache key. for a repository template, see [asottile@job--pre-commit.yml].

jobs:-  job:  precommit  # ...  variables:  PRE_COMMIT_HOME:  $(Pipeline.Workspace)/pre-commit-cache  steps:  # ...  -  script:  echo "##vso[task.setvariable variable=PY]$(python -VV)"  -  task:  CacheBeta@0  inputs:  key:  pre-commit | .pre-commit-config.yaml | "$(PY)"  path:  $(PRE_COMMIT_HOME)

###  github actions example [¶](https://pre-commit.com/#github-actions-example)

**see the [official pre-commit github action](https://github.com/pre-commit/action)**

like [azure pipelines](https://pre-commit.com/#azure-pipelines-example), github actions also uses immutable caches:

 - name:  set PY  run:  echo "::set-env name=PY::$(python -VV | sha256sum | cut -d' ' -f1)"  -  uses:  actions/cache@v1  with:  path:  ~/.cache/pre-commit  key:  pre-commit|${{ env.PY }}|${{ hashFiles('.pre-commit-config.yaml') }}

##  Usage with tox [¶](https://pre-commit.com/#usage-with-tox)

[tox](https://tox.readthedocs.io/) is useful for configuring test / CI tools such as pre-commit. One feature of `tox>=2` is it will clear environment variables such that tests are more reproducible. Under some conditions, pre-commit requires a few environment variables and so they must be whitelisted.

When cloning repos over ssh (`repo: git@github.com:...`), `git` requires the`SSH_AUTH_SOCK` variable and will otherwise fail:

[INFO] Initializing environment for git@github.com:pre-commit/pre-commit-hooks.

An unexpected error has occurred: CalledProcessError: command: ('/usr/bin/git', 'fetch', 'origin', '--tags')

return code: 128
expected return code: 0
stdout: (none)
stderr:
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists.
Check the log at /home/asottile/.cache/pre-commit/pre-commit.log
Add the following to your tox testenv:
[testenv]passenv  =  SSH_AUTH_SOCK

Likewise, when cloning repos over http / https (`repo: https://github.com:...`), you might be working behind a corporate http(s) proxy server, in which case `git` requires the `http_proxy`,`https_proxy` and `no_proxy` variables to be set, or the clone may fail:

[testenv]passenv  =  http_proxy https_proxy no_proxy

##  Using the latest version for a repository [¶](https://pre-commit.com/#using-the-latest-version-for-a-repository)

`pre-commit` configuration aims to give a repeatable and fast experience and therefore intentionally doesn't provide facilities for "unpinned latest version" for hook repositories.

Instead, `pre-commit` provides tools to make it easy to upgrade to the latest versions with [`pre-commit autoupdate`](https://pre-commit.com/#pre-commit-autoupdate). If you need the absolute latest version of a hook (instead of the latest tagged version), pass the `--bleeding-edge` parameter to `autoupdate`.

`pre-commit` assumes that the value of `rev` is an immutable ref (such as a tag or SHA) and will cache based on that. Using a branch name (or `HEAD`) for the value of `rev` is not supported and will only represent the state of that mutable ref at the time of hook installation (and will *NOT* update automatically).

#  Contributing [¶](https://pre-commit.com/#contributing)

We’re looking to grow the project and get more contributors especially to support more languages/versions. We’d also like to get the .pre-commit-hooks.yaml files added to popular linters without maintaining forks / mirrors.

Feel free to submit bug reports, pull requests, and feature requests.

##  Contributors [¶](https://pre-commit.com/#contributors)

- website by [Molly Finkle](https://github.com/mfnkl)
- created by [Anthony Sottile](https://github.com/asottile)
- core developers: [Ken Struys](https://github.com/struys),[Chris Kuehl](https://github.com/chriskuehl)
- [framework contributors](https://github.com/pre-commit/pre-commit/graphs/contributors)
- [core hook contributors](https://github.com/pre-commit/pre-commit-hooks/graphs/contributors)
- and users like you!