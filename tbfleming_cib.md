tbfleming/cib

  clang running in browser (wasm)   https://tbfleming.github.io/cib/

 [wasm](https://github.com/topics/wasm)  [emscripten](https://github.com/topics/emscripten)  [clang](https://github.com/topics/clang)

- [  31 commits](https://github.com/tbfleming/cib/commits/master)

- [  3 branches](https://github.com/tbfleming/cib/branches)

- [  3 releases](https://github.com/tbfleming/cib/releases)

- [  1 contributor](https://github.com/tbfleming/cib/graphs/contributors)

1.   [  JavaScript  40.0%](https://github.com/tbfleming/cib/search?l=javascript)

2.   [  Python  22.0%](https://github.com/tbfleming/cib/search?l=python)

3.   [  C++  19.4%](https://github.com/tbfleming/cib/search?l=c%2B%2B)

4.   [  HTML  15.4%](https://github.com/tbfleming/cib/search?l=html)

5.   [  CMake  3.2%](https://github.com/tbfleming/cib/search?l=cmake)

 JavaScript  Python  C++  HTML  CMake

Clone or download

 [Upload files](https://github.com/tbfleming/cib/upload/master)  [Find file](https://github.com/tbfleming/cib/find/master)

 [New pull request](https://github.com/tbfleming/cib/pull/new/master)

  Latest commit [55fb45e](https://github.com/tbfleming/cib/commit/55fb45e3f532b079c992102c24eed4d6eb2549e5)  17 hours ago      [![@tbfleming](../_resources/87674f6a36aac05e5560e46d7f5aa408.png)](https://github.com/tbfleming)  [tbfleming](https://github.com/tbfleming)    [cib-003](https://github.com/tbfleming/cib/commit/55fb45e3f532b079c992102c24eed4d6eb2549e5)

|     |     |     |     |
| --- | --- | --- | --- |
|     |  [src](https://github.com/tbfleming/cib/tree/master/src) |    [vector and string](https://github.com/tbfleming/cib/commit/d8932692bc4d70a04a6c903cc74b2cc100c300d5) |  17 hours ago |
|     |  [.clang-format](https://github.com/tbfleming/cib/blob/master/.clang-format) |    [change format](https://github.com/tbfleming/cib/commit/04e63a467eb9cbdbe14f2b2ffea7337a2f4dbf9e) |  17 days ago |
|     |  [.gitignore](https://github.com/tbfleming/cib/blob/master/.gitignore) |    [clang.html](https://github.com/tbfleming/cib/commit/2205492d0f78968f9925c5d98470ebb3229758e8) |  11 days ago |
|     |  [README.md](https://github.com/tbfleming/cib/blob/master/README.md) |    [vector and string](https://github.com/tbfleming/cib/commit/d8932692bc4d70a04a6c903cc74b2cc100c300d5) |  17 hours ago |
|     |  [build.py](https://github.com/tbfleming/cib/blob/master/build.py) |    [cib-003](https://github.com/tbfleming/cib/commit/55fb45e3f532b079c992102c24eed4d6eb2549e5) |  17 hours ago |

###    README.md

## [(L)](https://github.com/tbfleming/cib#clang-in-browser-cib)Clang In Browser (cib)

Try it at https://tbfleming.github.io/cib/

I'm trying to see how far wasm can go. Is it possible to compile clang to wasm and have it generate code within the browser?

Current status:

- Works in Firefox 57 and Chrome 63
- `clang-format`: working
- `clang`: working for simple cases
- Running generated wasm: working for simple cases

Currently missing:

- Global constructors and destructors
- Standard library globals (e.g. `cin`, `cout`)
- RTTI, exception handling

## [(L)](https://github.com/tbfleming/cib#vm-for-building-clang)VM for building clang

- Create a fresh VM to build with. The build will probably fail if you already have emscripten or clang installed.
- Consider using a high thread-count VM; e.g. an EC2 c5.9xlarge.
- I put the repo in a dedicated volume while building; this aids using spot instances. 100 GB.

Ubuntu 16.04:

	sudo apt update
	sudo apt upgrade
	sudo apt install build-essential cmake ninja-build python nodejs-legacy libncurses-dev

## [(L)](https://github.com/tbfleming/cib#building-wasm-binaries)Building WASM binaries

	./build.py -a

This script:

- Clones needed repos
- Builds an llvm toolchain for targeting WASM
- Builds emscripten
- Invokes emscripten to:
    - set up environment
    - build emscripten's dependances
- Uses emscripten to build llvm libraries
- Builds the apps