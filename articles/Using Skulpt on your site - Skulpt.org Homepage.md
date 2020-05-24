Using Skulpt on your site - Skulpt.org Homepage

# Get Started with Skulpt

Getting Started with Skulpt is easy!

- [Embed skulpt](http://skulpt.org/using.html#embed) into your exsiting webpage or blog

- [Add skulpt directly to your HTML](http://skulpt.org/using.html#html) for a custom integration

- For even more control, teach Skulpt to [import your own custom modules](http://skulpt.org/using.html#modules)

Need some inspiration for a project? Just want to learn or teach Python? Head over to the [Gallery](http://skulpt.org/gallery.html) to see how great educational projects are using Skulpt

## Embed Skulpt

If you want to embed a nice looking bit of code that your users can edit, Trinket.io can help you with that! You can put together the example on their site, and then generate the code for an iframe that you can embed in your page.

Users can **** Remix ** your example and save their work to a free Trinket account.

Use the Share button in the trinket above to get embed code. More information on embeeding trinkets [here](http://docs.trinket.io/getting-started).

## Using Skulpt with HTML

Want the compiled js to include in your site? Everything you need is in this zip: [skulpt-dist](https://github.com/skulpt/skulpt-dist/archive/master.zip). After adding `skulpt.js` or `skulpt-min.js` and `skulpt-stdlib.js` to your project, load the Javascript just before the </body> closing tag.

|     |     |
| --- | --- |
| 1   | <script  src="js/skulpt.min.js"  type="text/javascript"></script> |
| 2   | <script  src="js/skulpt-stdlib.js"  type="text/javascript"></script> |

 [view raw](https://gist.github.com/eah13/c3495f93f57b333bcb2f/raw/277cc531efcf6d1d20fc2c68dbf08cc04ddc0cf5/gistfile1.html)  [gistfile1.html](https://gist.github.com/eah13/c3495f93f57b333bcb2f#file-gistfile1-html) hosted with ❤ by [GitHub](https://github.com/)

We’re working on getting skulpt onto popular CDNs so you can load them straight from there.

Once your HTML is loading Skulpt, here's a really simple example to get you going. You can copy and paste or grab the code from [this gist](https://gist.github.com/4650616).

|     |     |
| --- | --- |
| 1   | <html> |
| 2   | <head> |
| 3   | <script  src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"  type="text/javascript"></script> |
| 4   | <script  src="http://www.skulpt.org/js/skulpt.min.js"  type="text/javascript"></script> |
| 5   | <script  src="http://www.skulpt.org/js/skulpt-stdlib.js"  type="text/javascript"></script> |
| 6   |     |
| 7   | </head> |
| 8   |     |
| 9   | <body> |
| 10  |     |
| 11  | <script  type="text/javascript"> |
| 12  | // output functions are configurable. This one just appends some text |
| 13  | // to a pre element. |
| 14  | function  outf(text) { |
| 15  |  var mypre =  document.getElementById("output"); |
| 16  |  mypre.innerHTML  =  mypre.innerHTML  + text; |
| 17  | }   |
| 18  | function  builtinRead(x) { |
| 19  |  if (Sk.builtinFiles  ===  undefined  \|\|  Sk.builtinFiles["files"][x] ===  undefined) |
| 20  |  throw  "File not found: '"  + x +  "'"; |
| 21  |  return  Sk.builtinFiles["files"][x]; |
| 22  | }   |
| 23  |     |
| 24  | // Here's everything you need to run a python program in skulpt |
| 25  | // grab the code from your textarea |
| 26  | // get a reference to your pre element for output |
| 27  | // configure the output function |
| 28  | // call Sk.importMainWithBody() |
| 29  | function  runit() { |
| 30  |  var prog =  document.getElementById("yourcode").value; |
| 31  |  var mypre =  document.getElementById("output"); |
| 32  |  mypre.innerHTML  =  ''; |
| 33  |  Sk.pre  =  "output"; |
| 34  |  Sk.configure({output:outf, read:builtinRead}); |
| 35  | (Sk.TurtleGraphics  \|\| (Sk.TurtleGraphics  = {})).target  =  'mycanvas'; |
| 36  |  var myPromise =  Sk.misceval.asyncToPromise(function() { |
| 37  |  return  Sk.importMainWithBody("<stdin>", false, prog, true); |
| 38  | }); |
| 39  |  myPromise.then(function(mod) { |
| 40  |  console.log('success'); |
| 41  | },  |
| 42  |  function(err) { |
| 43  |  console.log(err.toString()); |
| 44  | }); |
| 45  | }   |
| 46  | </script> |
| 47  |     |
| 48  | <h3>Try This</h3> |
| 49  | <form> |
| 50  | <textarea  id="yourcode"  cols="40"  rows="10">import turtle |
| 51  |     |
| 52  | t = turtle.Turtle() |
| 53  | t.forward(100) |
| 54  |     |
| 55  | print "Hello World" |
| 56  | </textarea><br /> |
| 57  | <button  type="button"  onclick="runit()">Run</button> |
| 58  | </form> |
| 59  | <pre  id="output" ></pre> |
| 60  | <!-- If you want turtle graphics include a canvas --> |
| 61  | <div  id="mycanvas"></div> |
| 62  |     |
| 63  | </body> |
| 64  |     |
| 65  | </html> |

 [view raw](https://gist.github.com/bnmnetp/4650616/raw/7981066795ea2592c516456c1103e3194a24643c/simpleskulpt.html)  [simpleskulpt.html](https://gist.github.com/bnmnetp/4650616#file-simpleskulpt-html) hosted with ❤ by [GitHub](https://github.com/)

## Using Custom Modules

This new feature lets you create and host your own modules for use in Skulpt. The following gist shows how to include one of them in a page.

### Customizing modules after import

If you want to customize how a module behaves you can use the ``onAfterImport`` hook. Here is a gist of how the trinket guys do it.

|     |     |
| --- | --- |
| 1   | Sk.onAfterImport  =  function(library) { |
| 2   |  switch(library) { |
| 3   |  case  'pygal': |
| 4   |  // make charts render instantly |
| 5   |  Highcharts.setOptions({ |
| 6   | plotOptions: { |
| 7   | series: { |
| 8   | animation:  false |
| 9   | }   |
| 10  | }   |
| 11  | }); |
| 12  |  break; |
| 13  |  case  'turtle': |
| 14  |  // make turtle draw instantly |
| 15  |  Sk.tg.defaults.animate  =  false; |
| 16  |  Sk.tg.Turtle.prototype.speed  =  function() {} |
| 17  |  Sk.tg.Turtle.prototype.delay  =  function() {} |
| 18  |  break; |
| 19  | }   |
| 20  | }   |

 [view raw](https://gist.github.com/bzwheeler/8a5a833ee2a6a7d2c7ba/raw/ac6a3ef66af6e353a862c2d4dce2bdf7eaeec169/gistfile1.js)  [gistfile1.js](https://gist.github.com/bzwheeler/8a5a833ee2a6a7d2c7ba#file-gistfile1-js) hosted with ❤ by [GitHub](https://github.com/)

### Releases

#### [0.10.0](https://api.github.com/repos/skulpt/skulpt/releases/1480498)

This latest release contains a lot of goodness. - You can now inherit from builtin types including Exceptions! - Major cleanup of numeric types - Bug fixes for iteration when using subclasses with our without `__getitem__` - Bug fixes and more completeness to lookups of dunder methods - complex type is added - brun command added to skulpt for easy access to in-browser debug - Many Many minor bug fixes.

#### [0.9.10](https://api.github.com/repos/skulpt/skulpt/releases/1362206)