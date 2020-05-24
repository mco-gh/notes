Skulpt

# Skulpt

 ![Skulpt](../_resources/bfd4f05a377a6e0d3c8690e92e373ad7.png)

## Python. Client side.

Skulpt is an *entirely in-browser* implementation of Python.

No preprocessing, plugins, or server-side support required, just write Python and reload.

## Demo

The code is run entirely in your browser, so don't feel obligated to "crash the server", you'll only stub your toe. [Help](http://www.skulpt.org/#), or examples: [1](http://www.skulpt.org/#)  [2](http://www.skulpt.org/#)  [3](http://www.skulpt.org/#)  [4](http://www.skulpt.org/#)  [5](http://www.skulpt.org/#)  [6](http://www.skulpt.org/#)  [7](http://www.skulpt.org/#)  [8](http://www.skulpt.org/#). Ctrl-Enter to run.

9
import turtle
​
t = turtle.Turtle()
​
for c in ['red', 'green', 'yellow', 'blue']:
t.color(c)
t.forward(75)
t.left(90)

xxxxxxxxxx
        Skulpt Debugger
-----------------------------------
type 'help' for looking at commands
-----------------------------------
​

1
​

Output: ([clear](http://www.skulpt.org/#))

## Interactive:

This is a very cool new feature that is just getting off the ground. This would be a great project to jump in and help out on!

Python 2.6(ish) (skulpt, Sun Feb 18 2018 08:05:25 GMT+0000 (GMT))

[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36] on MacIntel

Don't type "help", "copyright", "credits" or "license" unless you've assigned something to them

​

## Your Very Own Copy

Want to give it a shot? Grab it with git:

git clone https://github.com/skulpt/skulpt.git

Or download it like this: [skulpt-latest.tar.gz](http://www.skulpt.org/static/dist/skulpt-latest.tar.gz) or like this: [skulpt-latest.zip](http://www.skulpt.org/static/dist/skulpt-latest.zip)

## What's New?

- Suspensions! This may not mean a lot to you, but trust me its going to be big. Suspensions provide the foundation for the asynchronous execution we need to build an interactive debugger, a smoother turtle module, enhanced urllib and other cool features. For developers you should check out the time module and the suspensions.txt file under doc/.

- Stub implementations of the standard library modules. You will now get an unimplemented exceptions rather than some other file not found error.

- General cleanup and standardization of the code. See the short description of the coding standards in the CONTRIBUTING file

- Loads of bugfixes: [see](https://github.com/skulpt/skulpt/compare/0.9.2...0.9.4)

- slice() function implemented. And improvements to list slicing.

- string and operator module added.

- Keyword arguments for sorted()

- text() function in processing

By these awesome people: [Brad Miller](https://github.com/bnmnetp), [Scott Rixner](https://github.com/rixner), [Albert-Jan Nijburg](https://github.com/albertjan), [Marie Chatfield](https://github.com/mchat), [Isaac Dontje Lindell](https://github.com/isaacdontjelindell), [jaspervdg](https://github.com/jaspervdg), [Ethan Steinberg](https://github.com/Lalaland), [Jeff-Tian](https://github.com/Jeff-Tian), [Meredydd Luff](https://github.com/meredydd) and [Leszek Swirski](https://github.com/LeszekSwirski)

## Skulpt in the Wild

If you have a project that uses skulpt and would like me to link to it here, let me know on our github page.

## Skulpt on [Coursera](http://www.coursera.org/)

## Getting Started

If you want to embed a nice looking bit of code that your users can edit, Trinket.io can help you with that! You can put together the example on their site, and then generate the code for an iframe that you can embed in your page!

If you want to roll your own page, Getting started with skulpt on your own page can seem a little intimidating, but here's a really simple example that gets you going. You can copy and paste or grab the code from [this gist](https://gist.github.com/4650616).

|     |     |
| --- | --- |
|     | <html> |
|     | <head> |
|     | <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script> |
|     | <script src="http://www.skulpt.org/static/skulpt.min.js" type="text/javascript"></script> |
|     | <script src="http://www.skulpt.org/static/skulpt-stdlib.js" type="text/javascript"></script> |
|     | </head> |
|     | <body> |
|     | <script type="text/javascript"> |
|     | // output functions are configurable. This one just appends some text |
|     | // to a pre element. |
|     | function outf(text) { |
|     | var mypre = document.getElementById("output"); |
|     | mypre.innerHTML = mypre.innerHTML + text; |
|     | }   |
|     | function builtinRead(x) { |
|     | if (Sk.builtinFiles === undefined \|\| Sk.builtinFiles["files"][x] === undefined) |
|     | throw "File not found: '" + x + "'"; |
|     | return Sk.builtinFiles["files"][x]; |
|     | }   |
|     | // Here's everything you need to run a python program in skulpt |
|     | // grab the code from your textarea |
|     | // get a reference to your pre element for output |
|     | // configure the output function |
|     | // call Sk.importMainWithBody() |
|     | function runit() { |
|     | var prog = document.getElementById("yourcode").value; |
|     | var mypre = document.getElementById("output"); |
|     | mypre.innerHTML = ''; |
|     | Sk.pre = "output"; |
|     | Sk.configure({output:outf, read:builtinRead}); |
|     | (Sk.TurtleGraphics \|\| (Sk.TurtleGraphics = {})).target = 'mycanvas'; |
|     | var myPromise = Sk.misceval.asyncToPromise(function() { |
|     | return Sk.importMainWithBody("<stdin>", false, prog, true); |
|     | }); |
|     | myPromise.then(function(mod) { |
|     | console.log('success'); |
|     | },  |
|     | function(err) { |
|     | console.log(err.toString()); |
|     | }); |
|     | }   |
|     | </script> |
|     | <h3>Try This</h3> |
|     | <form> |
|     | <textarea id="yourcode" cols="40" rows="10">import turtle |
|     | t = turtle.Turtle() |
|     | t.forward(100) |
|     | print "Hello World" |
|     | </textarea><br /> |
|     | <button type="button" onclick="runit()">Run</button> |
|     | </form> |
|     | <pre id="output" ></pre> |
|     | <!-- If you want turtle graphics include a canvas --> |
|     | <div id="mycanvas"></div> |
|     | </body> |
|     | </html> |

## Helping out!

Skulpt surely isn't done yet.

If you want to check out a list of bugs, or add to it, or see what's been fixed recently, you can head over to the always-euphemistic-sounding [issues page](http://github.com/skulpt/skulpt/issues).

If you are interested in contributing to skulpt in any way, check out this new [how to contribute](https://github.com/skulpt/skulpt/blob/master/CONTRIBUTING.md) document.

If you'd like to chit-chat, [there's a list for that](http://groups.google.com/group/skulpt).

If you would like to help with coding, these new and improved [developer docs](http://www.skulpt.org/static/ProgMan/index.html) will help get you started.

## Third Party Modules

This new feature lets you create and host your own modules for use in Skulpt. The following gist shows how to include one of them in a page.

|     |     |
| --- | --- |
|     | // This snippet shows the cool new functionality added by @bzwheeler and the team at trinket.io |
|     | // You can now develop and host your own modules for skulpt, and set up a page to make those |
|     | // modules available as in the following. |
|     | Sk.externalLibraries = { |
|     | numpy : { |
|     | path: 'http://example.com/static/primeronoo/skulpt/external/numpy/__init__.js', |
|     | dependencies: ['/static/primeronoo/skulpt/external/deps/math.js'], |
|     | },  |
|     | matplotlib : { |
|     | path: '/static/primeronoo/skulpt/external/matplotlib/__init__.js' |
|     | },  |
|     | "matplotlib.pyplot" : { |
|     | path: '/static/primeronoo/skulpt/external/matplotlib/pyplot/__init__.js', |
|     | dependencies: ['/static/primeronoo/skulpt/external/deps/d3.min.js'], |
|     | },  |
|     | "arduino": { |
|     | path: '/static/primeronoo/skulpt/external/arduino/__init__.js' |
|     | }   |
|     | };  |

## Customizing modules after import

If you want to customize how a module behaves you can use the ``onAfterImport`` hook. Here is a gist of how the trinket guys do it.

|     |     |
| --- | --- |
|     | Sk.onAfterImport = function(library) { |
|     | switch(library) { |
|     | case 'pygal': |
|     | // make charts render instantly |
|     | Highcharts.setOptions({ |
|     | plotOptions: { |
|     | series: { |
|     | animation: false |
|     | }   |
|     | }   |
|     | }); |
|     | break; |
|     | case 'turtle': |
|     | // make turtle draw instantly |
|     | Sk.tg.defaults.animate = false; |
|     | Sk.tg.Turtle.prototype.speed = function() {} |
|     | Sk.tg.Turtle.prototype.delay = function() {} |
|     | break; |
|     | }   |
|     | }   |

## License

Skulpt may be licensed under:

1. The [MIT license](http://www.opensource.org/licenses/mit-license.php).

2. Or, for compatibility with Python, the [PSFLv2](http://www.opensource.org/licenses/PythonSoftFoundation.php).

Please note that this dual license only applies to the part of Skulpt that is included in the runtime, and not necessarily to surrounding code for build processing or testing. Tests are run using [V8](http://code.google.com/p/v8/), and [Closure Compiler](http://code.google.com/closure/compiler/), and some test code is taken from the [tinypy](http://www.tinypy.org/) and [Python](http://www.python.org/) test suites, which may be distributed under different licensing terms.

## About

The Father of skulpt is Scott Graham, you can find his blog here: [personal page (and blog)](http://www.h4ck3r.net/)

My own personal page and blog is [Reputable Journal](http://reputablejournal.com/)

Yes, I know how "sculpt" is spelled. The correct spelling was thoroughly reserved according to ICANN and search engines.