koalaman/shellcheck

[![68747470733a2f2f7472617669732d63692e6f72672f6b6f616c616d616e2f7368656c6c636865636b2e7376673f6272616e63683d6d6173746572](../_resources/087bbac58300ac5d38e541f4c3d661f2.png)](https://travis-ci.org/koalaman/shellcheck)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='605'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1731' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#shellcheck---a-shell-script-static-analysis-tool)ShellCheck - A shell script static analysis tool

ShellCheck is a GPLv3 tool that gives warnings and suggestions for bash/sh shell scripts:

[![terminal.png](../_resources/9a16645cd773877b3fc99ffc85e7578d.png)](https://github.com/koalaman/shellcheck/blob/master/doc/terminal.png)

The goals of ShellCheck are

- To point out and clarify typical beginner's syntax issues that cause a shell to give cryptic error messages.
- To point out and clarify typical intermediate level semantic problems that cause a shell to behave strangely and counter-intuitively.
- To point out subtle caveats, corner cases and pitfalls that may cause an advanced user's otherwise working script to fail under future circumstances.

See [the gallery of bad code](https://github.com/koalaman/shellcheck/blob/master/README.md#user-content-gallery-of-bad-code) for examples of what ShellCheck can help you identify!

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='606'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1744' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#table-of-contents)Table of Contents

- [How to use](https://github.com/koalaman/shellcheck#how-to-use)
    - [On the web](https://github.com/koalaman/shellcheck#on-the-web)
    - [From your terminal](https://github.com/koalaman/shellcheck#from-your-terminal)
    - [In your editor](https://github.com/koalaman/shellcheck#in-your-editor)
    - [In your build or test suites](https://github.com/koalaman/shellcheck#in-your-build-or-test-suites)
- [Installing](https://github.com/koalaman/shellcheck#installing)
- [Compiling from source](https://github.com/koalaman/shellcheck#compiling-from-source)
    - [Installing Cabal](https://github.com/koalaman/shellcheck#installing-cabal)
    - [Compiling ShellCheck](https://github.com/koalaman/shellcheck#compiling-shellcheck)
    - [Running tests](https://github.com/koalaman/shellcheck#running-tests)
- [Gallery of bad code](https://github.com/koalaman/shellcheck#gallery-of-bad-code)
    - [Quoting](https://github.com/koalaman/shellcheck#quoting)
    - [Conditionals](https://github.com/koalaman/shellcheck#conditionals)
    - [Frequently misused commands](https://github.com/koalaman/shellcheck#frequently-misused-commands)
    - [Common beginner's mistakes](https://github.com/koalaman/shellcheck#common-beginners-mistakes)
    - [Style](https://github.com/koalaman/shellcheck#style)
    - [Data and typing errors](https://github.com/koalaman/shellcheck#data-and-typing-errors)
    - [Robustness](https://github.com/koalaman/shellcheck#robustness)
    - [Portability](https://github.com/koalaman/shellcheck#portability)
    - [Miscellaneous](https://github.com/koalaman/shellcheck#miscellaneous)
- [Testimonials](https://github.com/koalaman/shellcheck#testimonials)
- [Ignoring issues](https://github.com/koalaman/shellcheck#ignoring-issues)
- [Reporting bugs](https://github.com/koalaman/shellcheck#reporting-bugs)
- [Contributing](https://github.com/koalaman/shellcheck#contributing)
- [Copyright](https://github.com/koalaman/shellcheck#copyright)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='607'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1775' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#how-to-use)How to use

There are a number of ways to use ShellCheck!

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='608'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1778' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#on-the-web)On the web

Paste a shell script on [https://www.shellcheck.net](https://www.shellcheck.net/) for instant feedback.

[ShellCheck.net](https://www.shellcheck.net/) is always synchronized to the latest git commit, and is the easiest way to give ShellCheck a go. Tell your friends!

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='609'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1782' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#from-your-terminal)From your terminal

Run `shellcheck yourscript` in your terminal for instant output, as seen above.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='610'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1785' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#in-your-editor)In your editor

You can see ShellCheck suggestions directly in a variety of editors.

- Vim, through [ALE](https://github.com/w0rp/ale), [Neomake](https://github.com/neomake/neomake), or [Syntastic](https://github.com/scrooloose/syntastic):

[![vim-syntastic.png](../_resources/403843e55137f4e98b82d325c2f19327.png)](https://github.com/koalaman/shellcheck/blob/master/doc/vim-syntastic.png).

- Emacs, through [Flycheck](https://github.com/flycheck/flycheck) or [Flymake](https://github.com/federicotdn/flymake-shellcheck):

[![emacs-flycheck.png](../_resources/f34a8f93b4c083c9b550723df46824c3.png)](https://github.com/koalaman/shellcheck/blob/master/doc/emacs-flycheck.png).

- Sublime, through [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter-shellcheck).
- Atom, through [Linter](https://github.com/AtomLinter/linter-shellcheck).
- VSCode, through [vscode-shellcheck](https://github.com/timonwong/vscode-shellcheck).
- Most other editors, through [GCC error compatibility](https://github.com/koalaman/shellcheck/blob/master/shellcheck.1.md#user-content-formats).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='611'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1803' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#in-your-build-or-test-suites)In your build or test suites

While ShellCheck is mostly intended for interactive use, it can easily be added to builds or test suites. It makes canonical use of exit codes, so you can just add a `shellcheck` command as part of the process.

For example, in a Makefile:

	check-scripts:
	    # Fail if any of these files have warnings
	    shellcheck myscripts/*.sh

or in a Travis CI `.travis.yml` file:

	script:
	  # Fail if any of these files have warnings

	  - shellcheck myscripts/*.sh

Services and platforms that have ShellCheck pre-installed and ready to use:

- [Travis CI](https://travis-ci.org/)
- [Codacy](https://www.codacy.com/)
- [Code Climate](https://codeclimate.com/)
- [Code Factor](https://www.codefactor.io/)

Services and platforms with third party plugins:

- [SonarQube](https://www.sonarqube.org/) through [sonar-shellcheck-plugin](https://github.com/emerald-squad/sonar-shellcheck-plugin)

Most other services, including [GitLab](https://about.gitlab.com/), let you install ShellCheck yourself, either through the system's package manager (see [Installing](https://github.com/koalaman/shellcheck#installing)), or by downloading and unpacking a [binary release](https://github.com/koalaman/shellcheck#installing-the-shellcheck-binary).

It's a good idea to manually install a specific ShellCheck version regardless. This avoids any surprise build breaks when a new version with new warnings is published.

For customized filtering or reporting, ShellCheck can output simple JSON, CheckStyle compatible XML, GCC compatible warnings as well as human readable text (with or without ANSI colors). See the[Integration](https://github.com/koalaman/shellcheck/wiki/Integration) wiki page for more documentation.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='612'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1820' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#installing)Installing

The easiest way to install ShellCheck locally is through your package manager.
On systems with Cabal (installs to `~/.cabal/bin`):

	cabal update
	cabal install ShellCheck

On systems with Stack (installs to `~/.local/bin`):

	stack update
	stack install ShellCheck

On Debian based distros:

	apt-get install shellcheck

On Arch Linux based distros:

	pacman -S shellcheck

or get the dependency free [shellcheck-static](https://aur.archlinux.org/packages/shellcheck-static/) from the AUR.

On Gentoo based distros:

	emerge --ask shellcheck

On EPEL based distros:

	yum -y install epel-release
	yum install ShellCheck

On Fedora based distros:

	dnf install ShellCheck

On FreeBSD:

	pkg install hs-ShellCheck

On OS X with homebrew:

	brew install shellcheck

On OpenBSD:

	pkg_add shellcheck

On openSUSE

	zypper in ShellCheck

Or use OneClickInstall - https://software.opensuse.org/package/ShellCheck
On Solus:

	eopkg install shellcheck

On Windows (via [scoop](http://scoop.sh/)):

	scoop install shellcheck

From Snap Store:

	snap install --channel=edge shellcheck

From Docker Hub:

docker pull koalaman/shellcheck:stable # Or :v0.4.7 for that version, or :latest for daily buildsdocker run -v "$PWD:/mnt" koalaman/shellcheck myscript

or use `koalaman/shellcheck-alpine` if you want a larger Alpine Linux based image to extend. It works exactly like a regular Alpine image, but has shellcheck preinstalled.

Alternatively, you can download pre-compiled binaries for the latest release here:

- [Linux, x86_64](https://storage.googleapis.com/shellcheck/shellcheck-stable.linux.x86_64.tar.xz) (statically linked)
- [Linux, armv6hf](https://storage.googleapis.com/shellcheck/shellcheck-stable.linux.armv6hf.tar.xz), i.e. Raspberry Pi (statically linked)
- [Windows, x86](https://storage.googleapis.com/shellcheck/shellcheck-stable.zip)

or see the [storage bucket listing](https://shellcheck.storage.googleapis.com/index.html) for checksums, older versions and the latest daily builds.

Distro packages already come with a `man` page. If you are building from source, it can be installed with:

	pandoc -s -t man shellcheck.1.md -o shellcheck.1
	sudo mv shellcheck.1 /usr/share/man/man1

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='613'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1849' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#travis-ci)Travis CI

Travis CI has now integrated ShellCheck by default, so you don't need to manually install it.

If you still want to do so in order to upgrade at your leisure or ensure the latest release, follow the steps to install the shellcheck binary, bellow.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='614'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1853' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#installing-the-shellcheck-binary)Installing the shellcheck binary

*Pre-requisite*: the program 'xz' needs to be installed on the system.
To install it on debian/ubuntu/linux mint, run `apt install xz-utils`.
To install it on Redhat/Fedora/CentOS, run `yum -y install xz`.

export scversion="stable"  # or "v0.4.7", or "latest"wget -qO- "https://storage.googleapis.com/shellcheck/shellcheck-"${scversion}".linux.x86_64.tar.xz"  | tar -xJv

cp shellcheck-"${scversion}"/shellcheck /usr/bin/
shellcheck --version

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='615'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1860' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#compiling-from-source)Compiling from source

This section describes how to build ShellCheck from a source directory. ShellCheck is written in Haskell and requires 2GB of RAM to compile.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='616'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1863' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#installing-cabal)Installing Cabal

ShellCheck is built and packaged using Cabal. Install the package `cabal-install` from your system's package manager (with e.g. `apt-get`, `brew`, `emerge`, `yum`, or `zypper`).

On MacOS (OS X), you can do a fast install of Cabal using brew, which takes a couple of minutes instead of more than 30 minutes if you try to compile it from source.

	brew install cask
	brew cask install haskell-platform
	cabal install cabal-install

On MacPorts, the package is instead called `hs-cabal-install`, while native Windows users should install the latest version of the Haskell platform from https://www.haskell.org/platform/

Verify that `cabal` is installed and update its dependency list with

	$ cabal update

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='617'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1869' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#compiling-shellcheck)Compiling ShellCheck

`git clone` this repository, and `cd` to the ShellCheck source directory to build/install:

	$ cabal install

Or if you intend to run the tests:

	$ cabal install --enable-tests

This will compile ShellCheck and install it to your `~/.cabal/bin` directory.
Add this directory to your `PATH` (for bash, add this to your `~/.bashrc`):
export PATH="$HOME/.cabal/bin:$PATH"
Log out and in again, and verify that your PATH is set up correctly:
$ which shellcheck~/.cabal/bin/shellcheck

On native Windows, the `PATH` should already be set up, but the system may use a legacy codepage. In `cmd.exe`, `powershell.exe` and Powershell ISE, make sure to use a TrueType font, not a Raster font, and set the active codepage to UTF-8 (65001) with `chcp`:

	> chcp 65001
	Active code page: 65001

In Powershell ISE, you may need to additionally update the output encoding:

	> [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='618'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1880' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#running-tests)Running tests

To run the unit test suite:

	$ cabal test

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='619'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1883' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#gallery-of-bad-code)Gallery of bad code

So what kind of things does ShellCheck look for? Here is an incomplete list of detected issues.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='620'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1886' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#quoting)Quoting

ShellCheck can recognize several types of incorrect quoting:

echo  $1  # Unquoted variablesfind . -name *.ogg # Unquoted find/grep patternsrm "~/my file.txt"  # Quoted tilde expansionv='--verbose="true"'; cmd $v  # Literal quotes in variablesfor  f  in  "*.ogg"  # Incorrectly quoted 'for' loopstouch $@  # Unquoted $@echo  'Don't forget to restart!' # Singlequote closed by apostropheecho 'Don\'t try this at home' # Attempting to escape '  in  ''echo  'Path is $PATH'  # Variables in single quotestrap  "echo Took ${SECONDS}s" 0 # Prematurely expanded trap

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='621'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1891' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#conditionals)Conditionals

ShellCheck can recognize many types of incorrect test statements.

[[ n != 0 ]] # Constant test expressions[[ -e  *.mpg ]] # Existence checks of globs[[ $foo==0 ]] # Always true due to missing spaces[[ -n  "$foo  " ]] # Always true due to literals[[ $foo  =~  "fo+" ]] # Quoted regex in =~[ foo =~ re ] # Unsupported [ ] operators[ $1  -eq  "shellcheck" ] # Numerical comparison of strings[ $n  &&  $m ] # && in [ .. ][ grep -q foo file ] # Command without $(..)[[ "$$file"  ==  *.jpg ]] # Comparisons that can't succeed((  1  -lt 2  ))  # Using test operators in ((..))

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='622'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1895' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#frequently-misused-commands)Frequently misused commands

ShellCheck can recognize instances where commands are used incorrectly:

grep '*foo*' file # Globs in regex contextsfind . -exec foo {} && bar {} \;  # Prematurely terminated find -execsudo echo  'Var=42'  > /etc/profile # Redirecting sudotime --format=%s sleep 10 # Passing time(1) flags to time builtinwhile  read h;  do ssh "$h" uptime # Commands eating while loop inputalias archive='mv $1 /backup'  # Defining aliases with argumentstr -cd '[a-zA-Z0-9]'  # [] around ranges in trexec foo;  echo  "Done!"  # Misused 'exec'find -name \*.bak -o -name \*~ -delete # Implicit precedence in find# find . -exec foo > bar \; # Redirections in findf() { whoami; }; sudo f # External use of internal functions

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='623'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1902' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#common-beginners-mistakes)Common beginner's mistakes

ShellCheck recognizes many common beginner's syntax errors:

var = 42 # Spaces around = in assignments$foo=42 # $ in assignmentsfor  $var  in  *;  do ... # $ in for loop variablesvar$n="Hello"  # Wrong indirect assignmentecho  ${var$n}  # Wrong indirect referencevar=(1, 2, 3) # Comma separated arraysarray=( [index] = value ) # Incorrect index initializationecho  $var[14] # Missing {} in array referencesecho  "Argument 10 is $10"  # Positional parameter misreferenceif  $(myfunction);  then ..;  fi  # Wrapping commands in $()else  if othercondition;  then .. # Using 'else if'f;  f() { echo  "hello world; } # Using function before definition[ false ] # 'false' being trueif ( -f file ) # Using (..) instead of test

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='624'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1906' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#style)Style

ShellCheck can make suggestions to improve style:

[[ -z  $(find /tmp | grep mpg) ]] # Use grep -q insteada >> log; b >> log; c >> log # Use a redirection block insteadecho  "The time is `date`"  # Use $() insteadcd dir; process *;  cd ..;  # Use subshells insteadecho $[1+2] # Use standard $((..)) instead of old $[]echo  $(($RANDOM  %  6))  # Don't use $ on variables in $((..))echo  "$(date)"  # Useless use of echocat file | grep foo # Useless use of cat

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='625'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1910' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#data-and-typing-errors)Data and typing errors

ShellCheck can recognize issues related to data and typing:

args="$@"  # Assigning arrays to stringsfiles=(foo bar);  echo  "$files"  # Referencing arrays as stringsdeclare -A arr=(foo bar) # Associative arrays without indexprintf  "%s\n"  "Arguments: $@."  # Concatenating strings and arrays[[ $#  > 2 ]] # Comparing numbers as stringsvar=World;  echo  "Hello " var # Unused lowercase variablesecho  "Hello $name"  # Unassigned lowercase variablescmd |  read bar;  echo  $bar  # Assignments in subshellscat foo | cp bar # Piping to commands that don't readprintf  '%s: %s\n' foo # Mismatches in printf argument count

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='626'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1914' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#robustness)Robustness

ShellCheck can make suggestions for improving the robustness of a script:

rm -rf "$STEAMROOT/"*  # Catastrophic rmtouch ./-l; ls *  # Globs that could become optionsfind . -exec sh -c 'a && b {}'  \;  # Find -exec shell injectionprintf  "Hello $name"  # Variables in printf formatfor  f  in  $(ls *.txt);  do  # Iterating over ls outputexport MYVAR=$(cmd)  # Masked exit codescase  $version  in 2.*) :;; 2.6.*) # Shadowed case branches

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='627'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1919' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#portability)Portability

ShellCheck will warn when using features not supported by the shebang. For example, if you set the shebang to `#!/bin/sh`, ShellCheck will warn about portability issues similar to `checkbashisms`:

echo {1..$n} # Works in ksh, but not bash/dash/shecho {1..10} # Works in ksh and bash, but not dash/shecho -n 42 # Works in ksh, bash and dash, undefined in shtrap  'exit 42' sigint # Unportable signal speccmd &> file # Unportable redirection operatorread foo < /dev/tcp/host/22 # Unportable intercepted filesfoo-bar() { ..; } # Undefined/unsupported function name[ $UID  = 0 ] # Variable undefined in dash/shlocal var=value # local is undefined in shtime sleep 1 | sleep 5 # Undefined uses of 'time'

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='628'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1923' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#miscellaneous)Miscellaneous

ShellCheck recognizes a menagerie of other issues:

PS1='\e[0;32m\$\e[0m '  # PS1 colors not in \[..\]PATH="$PATH:~/bin"  # Literal tilde in $PATHrm “file” # Unicode quotesecho  "Hello world"  # Carriage return / DOS line endingsecho hello \   # Trailing spaces after \var=42 echo  $var  # Expansion of inlined environment#!/bin/bash -x -e # Common shebang errorsecho  $((n/180*100))  # Unnecessary loss of precisionls *[:digit:].txt # Bad character class globssed 's/foo/bar/' file > file # Redirecting to inputwhile  getopts  "a" f;  do  case  $f  in  "b") # Unhandled getopts flags

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='629'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1928' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#testimonials)Testimonials

> At first you're like "shellcheck is awesome" but then you're like "wtf are we still using bash"

Alexander Tarasikov,[via Twitter](https://twitter.com/astarasikov/status/568825996532707330)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='630'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1933' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#ignoring-issues)Ignoring issues

Issues can be ignored via environmental variable, command line, individually or globally within a file:

https://github.com/koalaman/shellcheck/wiki/Ignore

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='631'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1937' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#reporting-bugs)Reporting bugs

Please use the GitHub issue tracker for any bugs or feature suggestions:
https://github.com/koalaman/shellcheck/issues

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='632'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1941' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#contributing)Contributing

Please submit patches to code or documentation as GitHub pull requests! Check out the [DevGuide](https://github.com/koalaman/shellcheck/wiki/DevGuide) on the ShellCheck Wiki.

Contributions must be licensed under the GNU GPLv3. The contributor retains the copyright.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='633'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1945' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#copyright)Copyright

ShellCheck is licensed under the GNU General Public License, v3. A copy of this license is included in the file [LICENSE](https://github.com/koalaman/shellcheck/blob/master/LICENSE).

Copyright 2012-2018, Vidar 'koala_man' Holen and contributors.
Happy ShellChecking!

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='634'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1950' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/koalaman/shellcheck#other-resources)Other Resources

- The wiki has [long form descriptions](https://github.com/koalaman/shellcheck/wiki/Checks) for each warning, e.g. [SC2221](https://github.com/koalaman/shellcheck/wiki/SC2221).
- ShellCheck does not attempt to enforce any kind of formatting or indenting style, so also check out [shfmt](https://github.com/mvdan/sh)!