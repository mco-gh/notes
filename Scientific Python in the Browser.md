Scientific Python in the Browser

#   [Scientific Python in the Browser](http://droettboom.com/blog/2018/04/04/python-in-the-browser/)

 Date    ** Wed 04 April 2018  Tags[python](http://droettboom.com/tag/python.html) /[data science](http://droettboom.com/tag/data-science.html)

**Summary:** An early report on getting the scientific Python stack compiled to WebAssembly.

## Data Science in the Browser

Shortly after starting at Mozilla in January, I became aware of Hamilton Ulmer and Brendan Colloran's [Iodide](https://github.com/iodide-project/iodide)project, an experiment to build a data science notebook based on web technologies. Unlike Jupyter notebooks, the computation happens in the browser, with direct access to Web API technologies like the DOM. Sharing a notebook is as simple as passing around a single HTML file, since there's no server side to worry about. It's not out to replace Jupyter notebooks, but rather to exist in a different design tradeoff space that makes it more suitable the sharing and collaboration.

Since it targets the browser, the programming language of Iodide is, of course, Javascript. While there are a number of libraries for doing data science in Javascript, such as [numjs](https://github.com/nicolaspanel/numjs) and [scijs](http://scijs.net/packages/), they aren't as widely used or as battle-tested as the scientific Python or R ecosystems. Nonetheless, I think "data science in Javascript" is an interesting area to explore, particularly since Javascript has some of the best JIT compilers of any dynamic language. This advantage allows writing both high-level orchestration and low-level numeric code in the same language, side-stepping the notorious "two language problem" in scientific Python. (In Python land, most of the core scientific libraries have significant chunks of code in lower level languages such as C, FORTRAN or [Cython](http://cython.org/) for performance reasons.) Combining Javascript's great compiler technology, and perhaps adding a smattering of transpilation to fix some syntactic issues, is really promising, and Iodide as a project is exploring that space.

Nonetheless, we received frequent feedback that Iodide "looks really cool, but I wish I could use the Python (or R) tools I'm familiar with." I understood in theory that it should be possible to compile the Python interpreter into[WebAssembly](http://webassembly.org/) in order to run it in the browser. There are already a few projects that do this: ([cpython-emscripten](https://github.com/dgym/cpython-emscripten), [micropython javascript support](https://github.com/micropython/micropython/pull/3575), [pypyjs](http://pypyjs.org/)). Unfortunately, I couldn't find a project that included a practical scientific Python stack including [Numpy](http://numpy.org/) and friends. I was concerned about the amount of effort it would take to build such a thing, and also whether the result would be performant enough to be useful. In February, we had a conversation with some folks who work on WebAssembly tooling at Mozilla, and they were pretty bullish that it wouldn't be too hard. Based on their optimism, I gave it a shot, and starting with dgym's [cpython-emscripten](https://github.com/dgym/cpython-emscripten) as a basis, I had the basic parts of a Python interpreter working in WebAssembly in a couple of days. Of course, going from that to a working Numpy took much longer, but thanks to some help from Alon Zakai and others, Numpy is working, too. With that done, it has been much easier getting other libraries higher up the stack to work, including preliminary support for Pandas.

### Tight integration

One thing that sets this implementation apart from other Python-in-the-browser projects I've come across is the ability to easily pass and share objects between Python and Javascript.

The basic Python data types (None, bool, int, float, str, bytes, list and dict) are transparently converted to and from their Javascript equivalents. Other types, including Numpy arrays, are wrapped in a proxy that allows Javascript to call their methods and access their items and attributes. Vice versa, Javascript objects are wrapped in a Python proxy. These proxies allow objects to be shared on both sides of the language barrier without copying, which is particularly important for large Numpy arrays.

Say, for example, you had a value in Javascript:
*// javascript*secret  =  "Wklv#lv#olnh#pdjlf$"
You could use it from Python by using the from js import ... syntax:

*# python*from  js  import  secretdecoded  =  ''.join(chr(ord(x)  -  3)  for  x  in  secret)

And then send data back to the Javascript side using pyodide.pyimport:
*// javascript*var  decoded  =  pyodide.pyimport("decoded")

One of the coolest side effects of this design is that Python has complete access to the Web API, so it can manipulate the DOM, use HTML Canvas, access webcams or audio and all the other cool things you can do from Javascript in a browser.

For example, changing the browser tab's title is as simple as importingwindow and setting an attribute:

from  js  import  windowwindow.title  =  "My mind is blown"

### What works

Most of the Python standard library works. The most notable exceptions are:

- subprocess: since the browser isn't an OS, it can't spawn new processes.
- socket: access to raw network sockets would break the browser security model. There are a lot of networking-related things in the standard library built on socket that therefore also don't work.
- All of the browser sandboxing still applies, so you can't access the local filesystem. However, by calling through Javascript, you do have access toXMLHttpRequest and browser local storage. Eventually, Python wrappers around this functionality [should be written](https://github.com/iodide-project/pyodide/issues/19) to make those operations feel more like they do in native Python.

Within Numpy, all of the core functionality works, but there's no support forlong double (but those are pretty niche). There are still some low-level compiler bugs that prevent the FFT stuff from compiling, but that should eventually resolve.

### How fast is it?

To answer this question, I reached for a few existing Python and Numpy benchmarks:

- The venerable [pystone](https://svn.python.org/projects/python/trunk/Lib/test/pystone.py), which ships with CPython.
- Serge Guelton's set of [numpy benchmarks](https://github.com/serge-sans-paille/numpy-benchmarks/).

These benchmarks probably fall into the trap of being a little too "synthetic". I would have preferred to also use the [Python Performance Benchmark Suite](http://pyperformance.readthedocs.io/index.html), which aims to be a little closer to "real world", but it has a significant number of dependencies and would need to be adapted to work on a platform without subprocess before it could be used in this context. Nonetheless, I think these benchmarks offer a useful approximation for now.

The [benchmarks](https://github.com/iodide-project/pyodide/tree/master/benchmark/benchmarks/)were run on the same machine in the native CPython implementation and in Firefox Nightly using selenium. The following figure shows how many times slower the WebAssembly implementation is.

**EDIT 2018-04-10:** The original results posted here inadvertently included Numpy import time in the WebAssembly times (but not in the native times). These have now been corrected above. There is some improvement in the results, but not in a best or worst case. You can see the original results[here](http://droettboom.com/images/pyodide-benchmarks-2018-04-09.svg).

The results are interesting. For benchmarks that spend most of their time in Numpy routines, such as [harris](https://github.com/iodide-project/pyodide/tree/master/benchmark/benchmarks/harris.py)or [rosen](https://github.com/iodide-project/pyodide/tree/master/benchmark/benchmarks/rosen.py), runtime is at par with the native-compiled Python. When WebAssembly rocks, it really, really rocks. Unfortunately, for other benchmarks that spend a lot of time looping or making function calls in Python, runtimes can be as much as 35 times slower. I have an unsubstantiated hunch that this is due to the use of Emscripten's [EMULATE_FUNCTION_POINTER_CASTS](https://kripken.github.io/emscripten-site/docs/porting/guidelines/function_pointer_issues.html#asm-pointer-casts)option which is required to make all of the function pointer calls that CPython does work correctly.

**UPDATE 2018-04-11:** My hunch was wrong, and I was able to get to the bottom of the root cause and significantly speed up these benchmarks. See my post[Profiling WebAssembly](http://droettboom.com/blog/2018/04/11/profiling-webassembly/) for more info.

### Future directions

I'd love to see improvements to the toolchain that close the performance gap. At this point, I don't personally know enough to anticipate how much work is involved.

Another current limitation is that all of the packages you anticipate you might need must be compiled and wrapped into a single large data file that is downloaded in its entirety to your browser before anything can start. It would be great to modularize that, so that packages are downloaded on demand. Related to that, it would also be helpful to modularize the build system so that individual packages can be added more independently. [Conda build](https://github.com/conda/conda-build) could potentially serve as a basis for that.

### Check it out

The easiest way to play with this is to visit the [example Pyodide notebook](https://iodide-project.github.io/pyodide-demo/python.html) (EDIT: This link was fixed to a working version). (Note that this only works on Firefox right now. Chrome support is [pending](https://github.com/iodide-project/pyodide/issues/17)).

You can also get involved at [pyodide github repository](https://github.com/iodide-project/pyodide/). Note that while Pyodide grew out of the needs of Iodide, there's nothing Iodide-specific about it, and it should be useful in other contexts where you want to embed a scientific Python stack in the browser. I'm pretty new to WebAssembly and I'd love any help, advice or comments to make this better.

* * *

## Comments