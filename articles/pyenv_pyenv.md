pyenv/pyenv

# [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#command-reference)Command Reference

Like ` git `, the ` pyenv ` command delegates to subcommands based on its first argument.

The most common subcommands are:

- [` pyenv commands `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-commands)
- [` pyenv local `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local)
- [` pyenv global `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)
- [` pyenv shell `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell)
- [` pyenv install `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-install)
- [` pyenv uninstall `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-uninstall)
- [` pyenv rehash `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-rehash)
- [` pyenv version `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-version)
- [` pyenv versions `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-versions)
- [` pyenv which `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-which)
- [` pyenv whence `](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-whence)

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-commands)` pyenv commands `

Lists all available pyenv commands.

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local)` pyenv local `

Sets a local application-specific Python version by writing the version name to a ` .python-version ` file in the current directory. This version overrides the global version, and can be overridden itself by setting the ` PYENV_VERSION ` environment variable or with the ` pyenv shell `command.

	$ pyenv local 2.7.6

When run without a version number, ` pyenv local ` reports the currently configured local version. You can also unset the local version:

	$ pyenv local --unset

Previous versions of pyenv stored local version specifications in a file named ` .pyenv-version `. For backwards compatibility, pyenv will read a local version specified in an ` .pyenv-version ` file, but a` .python-version ` file in the same directory will take precedence.

### [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local-advanced)` pyenv local ` (advanced)

You can specify multiple versions as local Python at once.

Let's say if you have two versions of 2.7.6 and 3.3.3. If you prefer 2.7.6 over 3.3.3,

	$ pyenv local 2.7.6 3.3.3
	$ pyenv versions
	  system
	* 2.7.6 (set by /Users/yyuu/path/to/project/.python-version)
	* 3.3.3 (set by /Users/yyuu/path/to/project/.python-version)
	$ python --version
	Python 2.7.6
	$ python2.7 --version
	Python 2.7.6
	$ python3.3 --version
	Python 3.3.3

or, if you prefer 3.3.3 over 2.7.6,

	$ pyenv local 3.3.3 2.7.6
	$ pyenv versions
	  system
	* 2.7.6 (set by /Users/yyuu/path/to/project/.python-version)
	* 3.3.3 (set by /Users/yyuu/path/to/project/.python-version)
	  venv27
	$ python --version
	Python 3.3.3
	$ python2.7 --version
	Python 2.7.6
	$ python3.3 --version
	Python 3.3.3

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)` pyenv global `

Sets the global version of Python to be used in all shells by writing the version name to the ` ~/.pyenv/version ` file. This version can be overridden by an application-specific ` .python-version ` file, or by setting the ` PYENV_VERSION ` environment variable.

	$ pyenv global 2.7.6

The special version name ` system ` tells pyenv to use the system Python (detected by searching your ` $PATH `).

When run without a version number, ` pyenv global ` reports the currently configured global version.

### [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global-advanced)` pyenv global ` (advanced)

You can specify multiple versions as global Python at once.

Let's say if you have two versions of 2.7.6 and 3.3.3. If you prefer 2.7.6 over 3.3.3,

	$ pyenv global 2.7.6 3.3.3
	$ pyenv versions
	  system
	* 2.7.6 (set by /Users/yyuu/.pyenv/version)
	* 3.3.3 (set by /Users/yyuu/.pyenv/version)
	$ python --version
	Python 2.7.6
	$ python2.7 --version
	Python 2.7.6
	$ python3.3 --version
	Python 3.3.3

or, if you prefer 3.3.3 over 2.7.6,

	$ pyenv global 3.3.3 2.7.6
	$ pyenv versions
	  system
	* 2.7.6 (set by /Users/yyuu/.pyenv/version)
	* 3.3.3 (set by /Users/yyuu/.pyenv/version)
	  venv27
	$ python --version
	Python 3.3.3
	$ python2.7 --version
	Python 2.7.6
	$ python3.3 --version
	Python 3.3.3

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell)` pyenv shell `

Sets a shell-specific Python version by setting the ` PYENV_VERSION `environment variable in your shell. This version overrides application-specific versions and the global version.

	$ pyenv shell pypy-2.2.1

When run without a version number, ` pyenv shell ` reports the current value of ` PYENV_VERSION `. You can also unset the shell version:

	$ pyenv shell --unset

Note that you'll need pyenv's shell integration enabled (step 3 of the installation instructions) in order to use this command. If you prefer not to use shell integration, you may simply set the` PYENV_VERSION ` variable yourself:

	$ export PYENV_VERSION=pypy-2.2.1

### [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell-advanced)` pyenv shell ` (advanced)

You can specify multiple versions via ` PYENV_VERSION ` at once.

Let's say if you have two versions of 2.7.6 and 3.3.3. If you prefer 2.7.6 over 3.3.3,

	$ pyenv shell 2.7.6 3.3.3
	$ pyenv versions
	  system
	* 2.7.6 (set by PYENV_VERSION environment variable)
	* 3.3.3 (set by PYENV_VERSION environment variable)
	$ python --version
	Python 2.7.6
	$ python2.7 --version
	Python 2.7.6
	$ python3.3 --version
	Python 3.3.3

or, if you prefer 3.3.3 over 2.7.6,

	$ pyenv shell 3.3.3 2.7.6
	$ pyenv versions
	  system
	* 2.7.6 (set by PYENV_VERSION environment variable)
	* 3.3.3 (set by PYENV_VERSION environment variable)
	  venv27
	$ python --version
	Python 3.3.3
	$ python2.7 --version
	Python 2.7.6
	$ python3.3 --version
	Python 3.3.3

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-install)` pyenv install `

Install a Python version (using [` python-build `](https://github.com/pyenv/pyenv/tree/master/plugins/python-build)).

	Usage: pyenv install [-f] [-kvp] <version>
	       pyenv install [-f] [-kvp] <definition-file>
	       pyenv install -l|--list

	  -l/--list             List all available versions
	  -f/--force            Install even if the version appears to be installed already
	  -s/--skip-existing    Skip the installation if the version appears to be installed already

	  python-build options:

	  -k/--keep        Keep source tree in $PYENV_BUILD_ROOT after installation
	                   (defaults to $PYENV_ROOT/sources)
	  -v/--verbose     Verbose mode: print compilation status to stdout
	  -p/--patch       Apply a patch from stdin before building
	  -g/--debug       Build a debug version

To list the all available versions of Python, including Anaconda, Jython, pypy, and stackless, use:

	$ pyenv install --list

Then install the desired versions:

	$ pyenv install 2.7.6
	$ pyenv install 2.6.8
	$ pyenv versions
	  system
	  2.6.8
	* 2.7.6 (set by /home/yyuu/.pyenv/version)

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-uninstall)` pyenv uninstall `

Uninstall a specific Python version.

	Usage: pyenv uninstall [-f|--force] <version>

	   -f  Attempt to remove the specified version without prompting
	       for confirmation. If the version does not exist, do not
	       display an error message.

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-rehash)` pyenv rehash `

Installs shims for all Python binaries known to pyenv (i.e.,` ~/.pyenv/versions/*/bin/* `). Run this command after you install a new version of Python, or install a package that provides binaries.

	$ pyenv rehash

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-version)` pyenv version `

Displays the currently active Python version, along with information on how it was set.

	$ pyenv version
	2.7.6 (set by /home/yyuu/.pyenv/version)

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-versions)` pyenv versions `

Lists all Python versions known to pyenv, and shows an asterisk next to the currently active version.

	$ pyenv versions
	  2.5.6
	  2.6.8
	* 2.7.6 (set by /home/yyuu/.pyenv/version)
	  3.3.3
	  jython-2.5.3
	  pypy-2.2.1

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-which)` pyenv which `

Displays the full path to the executable that pyenv will invoke when you run the given command.

	$ pyenv which python3.3
	/home/yyuu/.pyenv/versions/3.3.3/bin/python3.3

## [(L)](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-whence)` pyenv whence `

Lists all Python versions with the given command installed.

	$ pyenv whence 2to3
	2.6.8
	2.7.6
	3.3.3