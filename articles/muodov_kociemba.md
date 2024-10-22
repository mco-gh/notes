muodov/kociemba

[![68747470733a2f2f7472617669732d63692e6f72672f6d756f646f762f6b6f6369656d62612e7376673f6272616e63683d6d6173746572](../_resources/6e77b43080c94e06849fc7e456ad1329.png)](https://travis-ci.org/muodov/kociemba)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='87'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='958' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#kociemba)kociemba

This Python package contains two equivalent implementations (in C and Python) of Herbert Kociemba's two-phase algorithm for solving Rubik's Cube. Original Java implementation can be found here: http://kociemba.org/download.htm.

These ports are pretty straightforward (not to say dumb) and most probably can be optimized. But they have been extensively tested in our Rubik's cube solving machines ([FAC System Solver](https://blog.zok.pw/hacking/2015/08/18/fac-rubik-solver/) and [Meccano Rubik's Shrine](http://blog.zok.pw/hacking/2016/08/12/meccano-rubiks-shrine/)), so be confident the algorithm is working.

**NB** please note that two-phase algorithm does not guarantee that the produced solution is the shortest possible. Instead, it gives you a "good enough" solution in a very short time. You can implement additional checks on top of this library, for example, to not produce any moves if the cube is already solved.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='88'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='963' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#installation)Installation

This package is published on PyPI and can be installed with:
`$ pip install kociemba`
It was tested under Python 2.7 and 3.3+.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='89'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='968' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#unix-based-systems)Unix-based systems

You might need to install libffi system library beforehand. For example, on Debian-based distributions (e.g. Raspbian) you would run `sudo apt-get install libffi-dev`.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='90'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='971' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#windows)Windows

Library should work on Windows, however it is not automatically tested at this moment: Travis CI [doesn't have windows support](https://github.com/travis-ci/travis-ci/issues/2104).

Normal `pip install kociemba` (or `pip3 install kociemba` for Python 3.3+) should work, but you will need to install free build tools from Microsoft first. Check the following links:

- for Python 2.7: https://www.microsoft.com/en-us/download/details.aspx?id=44266
- for Python 3: https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='91'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='978' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#usage)Usage

The package exposes just one function `solve()`, which accepts a cube definition string and returns a solution string in standard notation (see below). Optional second argument allows solving to a specific pattern.

>>>  import kociemba>>> kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')u"D2 R' D' F2 B D R2 D2 R' F2 D' F2 U' B2 L2 U2 D R2 U">>> kociemba.solve('FLBUULFFLFDURRDBUBUUDDFFBRDDBLRDRFLLRLRULFUDRRBDBBBUFL', 'BBURUDBFUFFFRRFUUFLULUFUDLRRDBBDBDBLUDDFLLRRBRLLLBRDDF')u"R' D2 R' U2 R F2 D B2 U' R F' U R2 D L2 D' B2 R2 B2 U' B2"

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='92'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='982' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#standalone-tool)Standalone tool

When installing with pip, `kociemba` will also register a command line tool with the same name. So you can also use it like this:

`$ kociemba <cubestring>`

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='93'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='986' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#cube-string-notation)Cube string notation

The names of the facelet positions of the cube (letters stand for Up, Left, Front, Right, Back, and Down):

	             |************|
	             |*U1**U2**U3*|
	             |************|
	             |*U4**U5**U6*|
	             |************|
	             |*U7**U8**U9*|
	             |************|
	 ************|************|************|************
	 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
	 ************|************|************|************
	 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
	 ************|************|************|************
	 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
	 ************|************|************|************
	             |************|
	             |*D1**D2**D3*|
	             |************|
	             |*D4**D5**D6*|
	             |************|
	             |*D7**D8**D9*|
	             |************|

A cube definition string "UBL..." means that in position U1 we have the U-color, in position U2 we have the B-color, in position U3 we have the L color etc. according to the order `U1`, `U2`, `U3`, `U4`, `U5`, `U6`, `U7`, `U8`, `U9`, `R1`, `R2`,`R3`, `R4`, `R5`, `R6`, `R7`, `R8`, `R9`, `F1`, `F2`, `F3`, `F4`, `F5`, `F6`, `F7`, `F8`, `F9`, `D1`, `D2`, `D3`, `D4`, `D5`, `D6`, `D7`, `D8`, `D9`, `L1`, `L2`, `L3`, `L4`,`L5`, `L6`, `L7`, `L8`, `L9`, `B1`, `B2`, `B3`, `B4`, `B5`, `B6`, `B7`, `B8`, `B9`.

So, for example, a definition of a solved cube would be `UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB`

Solution string consists of space-separated parts, each of them represents a single move:

- A single letter by itself means to turn that face clockwise 90 degrees.
- A letter followed by an apostrophe means to turn that face counterclockwise 90 degrees.
- A letter with the number 2 after it means to turn that face 180 degrees.

e.g. **`R U R’ U R U2 R’ U`**

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='94'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='997' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#c-version)C version

C sources reside in the `ckociemba` folder. Running `make` inside this directory will compile a standalone binary. It accepts a cube representation as a command line argument, and writes the solution to the standard output. You can, of course, use `ckociemba` sources directly in your projects.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='95'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1000' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#performance)Performance

When possible, `kociemba` will use C implementation under the hood. If something goes wrong (C version cannot be imported) it will automatically fall back to pure-Python implementation. However, it will be much slower.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='96'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1003' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#testing)Testing

To run the tests, clone the repository and run:
`$ python setup.py test`

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='97'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1007' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/muodov/kociemba#thanks-to)Thanks to

- @jarheadjoe for his contribution to Windows support