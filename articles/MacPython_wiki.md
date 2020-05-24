MacPython/wiki

# Spinning wheels

Matthew Brett edited this page on Apr 11, 2015 · [22 revisions](https://github.com/MacPython/wiki/wiki/Spinning-wheels/_history)

[Wheels](http://legacy.python.org/dev/peps/pep-0427/) are the new standard binary installation format for Python.

Many projects provide wheels now : [http://pythonwheels.com](http://pythonwheels.com/)

However, only some of these wheels are binary wheels.

## Binary wheels on OSX

In the old days, pip would only install binary wheels on Windows. But, on[January 1st 2014](http://pip.readthedocs.org/en/latest/news.html), pip started installing matching binary wheels for OSX ([the relevant pull request](https://github.com/pypa/pip/pull/1278)).

Some popular projects that already have such wheels are:

## Question: will pip give me a broken wheel?

"Matching binary wheels" are wheels with a filename that matches the installing pip's Python version, Python ABI version, and the [platform tag](http://legacy.python.org/dev/peps/pep-0425/#platform-tag).

At first, [some worried](https://github.com/pypa/pip/pull/1278) that this tag system might cause trouble for people installing OSX binary wheels into unusual Python versions, such as homebrew and macports.

In practice though, the platform tag does a good job of preventing pip from installing a wheel that won't work.

Here's an example wheel filename:`numpy-1.8.0-cp27-none-macosx_10_6_intel.whl`. The name splits at dashes into:

- numpy (package name)
- 1.8.0 (package version)
- cp27 (CPython 2.7 - Python version)
- none (Python ABI number - only applies to Pythons >= 3)
- macosx_10_6_intel (platform tag)

The platform tag comes from the output of `python -c "import distutils.util; print(distutils.util.get_platform())"` on the platform *building* the wheel. I ([MB](http://matthew.dynevor.org/)) built`numpy-1.8.0-cp27-none-macosx_10_6_intel.whl` with Python 2.7 from a Python.org binary installer on an OSX 10.9 machine. The OSX platform tag further breaks down to:

- macosx
- 10_6 (the version of the SDK used to compile Python)
- intel (short-hand for a fat binary containing x86_64 and i386 objects)

As you see, the SDK part of the tag is not from the OSX running on the machine I (MB) was building from but from the distutils configuration on the Python I was building for. In this case I was building for a Python.org binary, and that Python.org binary gave `macosx-10.6-intel` from distutils`get_platform()`.

Up until pip 6.0, for pip to accept the wheel as matching its own platform, these values have to match exactly. Meaning, that the Python running pip on the installing machine has to have a value from`distutils.util.get_platform()` that matches `macosx_10_6_intel` exactly (after converting dots and dashes to underscores).

Here are some values of `distutils.util.get_platform()` for different Pythons on OSX:

Python source
Python version
OSX version
[object Object]
Python.org
2.7
10.9
macosx-10.6-intel
System Python
2.7
10.9
macosx-10.9-intel
Macports
2.7
10.9
macosx-10.9-x86_64
Homebrew
2.7
10.9
macosx-10.9-x86_64
Python.org
3.4
10.9
macosx-10.6-intel
Python.org
2.7
10.7
macosx-10.6-intel
System Python
2.7
10.7
macosx-10.7-intel

You get the idea. Python.org Pythons all use the 10.6 SDK, and have fat (x86_64 and i386) architecture in them. System Pythons use the SDK for the OSX they ship with, and also have fat architecture. Homebrew and Macports Python have the SDK for the OSX they are installing on, and x86_64 architecture only.

This tells us two things. First - wheels built with Python.org Python will have platform tags that *only* match other Python.org Python installations, for pip < 6.0. So, for pip < 6.0, pip won't install them into system Python (wrong SDK) or homebrew or macports Python (wrong SDK and different architecture). Second, the Python.org wheels will in fact have the correct architecture and compatible SDK for all the other Pythons listed. Why? Because having a fat binary includes having x86_64, so is compatible with x86_64-only builds. Stuff compiled with the 10.6 SDK should also be compatible with stuff built against later SDK versions (up to and including 10.9). You can demonstrate this to yourself by renaming the wheel above to - for example -`numpy-1.8.0-cp27-none-macosx_10_9_x86_64.whl` and then installing into a homebrew python on OSX 10.9. Sure enough, it installs, imports and tests without problem.

## Answer: no, pip will be very careful to give you a matching wheel

Python.org wheels are safe to distribute because:

1. pip < 6.0 will only install the wheel into a Python.org Python by default and

2. The architecture and SDK versions are in fact compatible with system Python, homebrew Python and macports Python.

In fact, because it is possible to work out which wheels are compatible between Pythons, Min Ragan-Kelley proposed that pip should recognize that prior SDKs match later OSX versions, and fat binaries should match sensible single architectures ([PR](https://github.com/pypa/pip/pull/1465) and[discussion](https://mail.python.org/pipermail/distutils-sig/2014-March/023977.html)). This change was merged into the pip master branch on June 12 2014 and was released as part of pip 6.0.

## So - nothing can go wrong with OSX binary wheels?

Strange to say, things can go wrong with wheels as for any binary distribution. Here are some things that can go wrong, and how to fix them:

### Linking to external libraries that some machines do not have

All Python extensions link against OSX system libraries, but these are carefully managed to be ABI compatible between OSX versions, and you should not run into problems with these.

You can use the [delocate utility](https://github.com/matthew-brett/delocate)to check which libraries you are linking against. For example, this is the result of running `delocate-listdeps --all` on a [binary wheel](https://nipy.bic.berkeley.edu/scipy_installers/tornado-3.2-cp27-none-macosx_10_6_intel.whl) for the [tornado](https://github.com/facebook/tornado) library:

	/usr/lib/libSystem.B.dylib

This library is present and ABI compatible for all of OSX versions 10.6 and higher.

If you build a complicated Python extension it may link against some external libraries elsewhere on the system. [scipy](https://github.com/scipy/scipy) is one example; it links to the gfortran runtime libraries, whereever it finds them. Here's the output of `delocate-listdeps --all` for a scipy wheel built naively on a standard OSX 10.9 system using gfortran from homebrew:

	/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
	/usr/lib/libSystem.B.dylib
	/usr/lib/libstdc++.6.dylib
	/usr/local/Cellar/gfortran/4.8.2/gfortran/lib/libgcc_s.1.dylib
	/usr/local/Cellar/gfortran/4.8.2/gfortran/lib/libgfortran.3.dylib
	/usr/local/Cellar/gfortran/4.8.2/gfortran/lib/libquadmath.0.dylib

Again, the libraries in `/System` and `/usr/lib` will be present on OSX >= 10.6, but of course the libraries in `/usr/local/Cellar/gfortran` will only be present if someone has installed gfortran via homebrew. If I distribute this wheel, it will only work for someone who has installed these libraries. The`delocate` utility can usually fix this by copying the dynamic libraries into the wheel and relinking the extensions.

## Other stuff that might happen but we haven't yet seen

Some people have reported that binaries built with an earlier SDK (such as 10.3) on a later OSX OS (such as 10.9) do not in fact work on earlier versions of OSX, as they should ([see comment on pip PR](https://github.com/pypa/pip/pull/1465#issuecomment-37094250)). I have not myself (MB) run into this problem with the 10.6 SDK. For safety, it is best to build binaries such as wheels on the same OSX versions as the SDK. For example, if you are building wheels targeting the 10.6 SDK, try and build the wheels on a machine running 10.6. I don't know of any reports of problems using these binaries on later OSX versions.

There was [some worry](https://github.com/pypa/pip/pull/1465#issuecomment-36954741) on a pip pull-request discussion that it might be possible to get Python confused with wheels built against different C++ runtime libraries. Min RK [couldn't make this problem happen](https://github.com/pypa/pip/pull/1465#issuecomment-36958931) with test-cases, so we are currently working on the assumption that this is not an issue. Obviously it doesn't come up if you're not using C++.

## The answer is always the same - test

If in doubt - test. For example, put your wheels up on a server somewhere (examples of this are [Min RKs machine](http://kerbin.bic.berkeley.edu/wheelhouse), [the nipy server](https://nipy.bic.berkeley.edu/scipy_installers)) and then test the wheels with something like:

	NIPY_URL=https://nipy.bic.berkeley.edu/scipy_installers
	pip install --find-links $NIPY_URL tornado

Do this in virtualenvs with different Pythons and on different OSX versions. If you run into trouble, let us know via the [Python Mac special interest group mailing list](https://www.python.org/community/sigs/current/pythonmac-sig) and we'll try to help. At very least, we'd really like to know.

## Practical example of building wheels for a project

As we've seen, the MacPython Python distributions are the best to build against, because they use the 10.6 SDK (and hence are compatible with OSX versions from 10.6) and they have dual architectures (i386 and x86_64). This makes the resulting wheel compatible with system Python, homebrew and macports.

### Install MacPythons

Install:

- MacPython 2.7
- MacPython 3.3
- MacPython 3.4

### Install pips

For MacPython 2.7 and 3.3 you'll need an up-to-date pip (3.4 comes with pip):

- Download `get-pip.py`
- Install pip

	  export MACPIES=/Library/Frameworks/Python.framework/Versions
	  $MACPIES/2.7/bin/python get-pip.py
	  $MACPIES/3.3/bin/python3 get-pip.py

See instructions at http://pip.readthedocs.org/en/latest/installing.html

### Install wheel

	$MACPIES/2.7/bin/pip install wheel
	$MACPIES/3.3/bin/pip3 install wheel
	$MACPIES/3.4/bin/pip3 install wheel

### Build wheels

Here I'm building wheels for `markupsafe`:

	cd markupsafe
	rm -rf build
	$MACPIES/2.7/bin/python setup.py bdist_wheel
	rm -rf build
	$MACPIES/3.3/bin/python3 setup.py bdist_wheel
	rm -rf build
	$MACPIES/3.4/bin/python3 setup.py bdist_wheel

You should now have three wheels in your distribution directory (usually`dist`). In my case:

	dist/MarkupSafe-0.23-cp27-none-macosx_10_6_intel.whl
	dist/MarkupSafe-0.23-cp33-cp33m-macosx_10_6_intel.whl
	dist/MarkupSafe-0.23-cp34-cp34m-macosx_10_6_intel.whl

### Check wheels for external dependencies that need shipping

	pip install delocate
	delocate-listdeps dist/*.whl

Markupsafe wheels have no dependencies outside the system library paths, so you get something like this:

	dist/MarkupSafe-0.23-cp27-none-macosx_10_6_intel.whl:
	dist/MarkupSafe-0.23-cp33-cp33m-macosx_10_6_intel.whl:
	dist/MarkupSafe-0.23-cp34-cp34m-macosx_10_6_intel.whl:

If your project does have some dependencies from the analysis above, then:

	mkdir fixed_wheels
	delocate-wheel -w fixed_wheels dist/*.whl

Finally, if you want to make the wheel installable on any platform by pip < 6.0, you might want to rename the wheels to express the fact that they will work on system Python and homebrew / macports for 10.9. For example, you might rename `MarkupSafe-0.23-cp27-none-macosx_10_6_intel.whl` to`MarkupSafe-0.23-cp27-none-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.whl`. There's a script to do that in [this gist](https://gist.github.com/matthew-brett/51bdd3c817bd6541b950)

This renaming is no longer required with pip >= 6.0.

### Upload to pypi

Finally, you can upload these to pypi, maybe using[twine](https://pypi.python.org/pypi/twine). Then you will go green here:http://pythonwheels.com/

## Automating wheel builds with travis

We (the MacPython organization) support some other projects building OSX wheels using travis-ci.org; feel free to contact us if you'd like help too.

See [Wheel building](https://github.com/MacPython/wiki/wiki/Wheel-building) for details.