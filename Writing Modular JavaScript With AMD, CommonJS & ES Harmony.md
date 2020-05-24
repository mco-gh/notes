Writing Modular JavaScript With AMD, CommonJS & ES Harmony

# Writing Modular JavaScript With AMD, CommonJS & ES Harmony

 Written by: [Addy Osmani](http://twitter.com/addyosmani)  Technical Review: [Andrée Hansson](http://twitter.com/peolanha)

 WITH SPECIAL THANKS TO [JAMES BURKE](http://twitter.com/jrburke), [JOHN HANN](http://twitter.com/unscriptable) AND [THOMAS DAVIS](http://twitter.com/neutralthoughts)

 [Tweet](http://twitter.com/share)

[(L)](https://plus.google.com/share?app=110&url=https%3A%2F%2Faddyosmani.com%2Fwriting-modular-js%2F)

## Modularity The Importance Of Decoupling Your Application

When we say an application is **modular**, we generally mean it's composed of a set of highly decoupled, distinct pieces of functionality stored in modules. As you probably know, [loose coupling](http://arguments.callee.info/2009/05/18/javascript-design-patterns--mediator/) facilitates easier maintainability of apps by removing *dependencies* where possible. When this is implemented efficiently, its quite easy to see how changes to one part of a system may affect another.

Unlike some more traditional programming languages however, the current iteration of JavaScript ([ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)) doesn't provide developers with the means to import such modules of code in a clean, organized manner. It's one of the concerns with specifications that haven't required great thought until more recent years where the need for more organized JavaScript applications became apparent.

Instead, developers at present are left to fall back on variations of the [module](http://www.adequatelygood.com/2010/3/JavaScript-Module-Pattern-In-Depth) or [object literal](http://blog.rebeccamurphey.com/2009/10/15/using-objects-to-organize-your-code) patterns. With many of these, module scripts are strung together in the DOM with namespaces being described by a single global object where it's still possible to incur naming collisions in your architecture. There's also no clean way to handle dependency management without some manual effort or third party tools.

Whilst native solutions to these problems will be arriving in [ES Harmony](http://wiki.ecmascript.org/doku.php?id=harmony:modules), the good news is that writing modular JavaScript has never been easier and you can start doing it today.

In this article, we're going to look at three formats for writing modular JavaScript: **AMD**, **CommonJS** and proposals for the next version of JavaScript, **Harmony**.

## Prelude A Note On Script Loaders

It's difficult to discuss AMD and CommonJS modules without talking about the elephant in the room - [script loaders](http://msdn.microsoft.com/en-us/scriptjunkie/hh227261). At present, script loading is a means to a goal, that goal being modular JavaScript that can be used in applications today - for this, use of a compatible script loader is unfortunately necessary. In order to get the most out of this article, I recommend gaining a **basic understanding** of how popular script loading tools work so the explanations of module formats make sense in context.

There are a number of great loaders for handling module loading in the AMD and CJS formats, but my personal preferences are [RequireJS](http://requirejs.org/) and [curl.js](https://github.com/unscriptable/curl). Complete tutorials on these tools are outside the scope of this article, but I can recommend reading John Hann's post about [curl.js](http://unscriptable.com/index.php/2011/03/30/curl-js-yet-another-amd-loader/) and James Burke's [RequireJS](http://requirejs.org/docs/api.html) API documentation for more.

From a production perspective, the use of optimization tools (like the RequireJS optimizer) to concatenate scripts is recommended for deployment when working with such modules. Interestingly, with the [Almond](https://github.com/jrburke/almond) AMD shim, RequireJS doesn't need to be rolled in the deployed site and what you might consider a script loader can be easily shifted outside of development.

That said, James Burke would probably say that being able to dynamically load scripts after page load still has its use cases and RequireJS can assist with this too. With these notes in mind, let's get started.

## AMD A Format For Writing Modular JavaScript In The Browser

The overall goal for the AMD (Asynchronous Module Definition) format is to provide a solution for modular JavaScript that developers can use today. It was born out of Dojo's real world experience using XHR+eval and proponents of this format wanted to avoid any future solutions suffering from the weaknesses of those in the past.

The AMD module format itself is a proposal for defining modules where both the module and dependencies can be [asynchronously](http://dictionary.reference.com/browse/asynchronous) loaded. It has a number of distinct advantages including being both asynchronous and highly flexible by nature which removes the tight coupling one might commonly find between code and module identity. Many developers enjoy using it and one could consider it a reliable stepping stone towards the [module system](http://wiki.ecmascript.org/doku.php?id=harmony:modules) proposed for ES Harmony.

AMD began as a draft specification for a module format on the CommonJS list but as it wasn't able to reach full concensus, further development of the format moved to the [amdjs](https://github.com/amdjs) group.

Today it's embraced by projects including Dojo (1.7), MooTools (2.0), Firebug (1.8) and even jQuery (1.7). Although the term *CommonJS AMD format* has been seen in the wild on occasion, it's best to refer to it as just AMD or Async Module support as not all participants on the CJS list wished to pursue it.

**Note:** There was a time when the proposal was referred to as Modules Transport/C, however as the spec wasn't geared for transporting existing CJS modules, but rather, for defining modules it made more sense to opt for the AMD naming convention.

### Getting Started With Modules

The two key concepts you need to be aware of here are the idea of a `define` method for facilitating module definition and a `require` method for handling dependency loading. *define* is used to define named or unnamed modules based on the proposal using the following signature:

1. define(
2.  module_id /*optional*/,
3.   [dependencies]  /*optional*/,
4.  definition function  /*function for instantiating the module or object*/
5. );

As you can tell by the inline comments, the `module_id` is an optional argument which is typically only required when non-AMD concatenation tools are being used (there may be some other edge cases where it's useful too). When this argument is left out, we call the module anonymous.

When working with anonymous modules, the idea of a module's identity is DRY, making it trivial to avoid duplication of filenames and code. Because the code is more portable, it can be easily moved to other locations (or around the file-system) without needing to alter the code itself or change its ID. The `module_id` is equivalent to folder paths in simple packages and when not used in packages. Developers can also run the same code on multiple environments just by using an AMD optimizer that works with a CommonJS environment such as [r.js](https://github.com/jrburke/r.js/).

Back to the define signature, the dependencies argument represents an array of dependencies which are required by the module you are defining and the third argument ('definition function') is a function that's executed to instantiate your module. A barebone module could be defined as follows:

#### Understanding AMD: define()

1. // A module_id (myModule) is used here for demonstration purposes only
2.
3. define('myModule',
4.   ['foo',  'bar'],
5.   // module definition function
6.   // dependencies (foo and bar) are mapped to function parameters
7.   function  ( foo, bar )  {
8.   // return a value that defines the module export
9.   // (i.e the functionality we want to expose for consumption)
10.
11.   // create your module here
12.   var myModule =  {
13.  doStuff:function(){
14.  console.log('Yay! Stuff');
15.   }
16.   }
17.
18.   return myModule;
19. });
20.
21. // An alternative example could be..
22. define('myModule',
23.   ['math',  'graph'],
24.   function  ( math, graph )  {
25.
26.   // Note that this is a slightly different pattern
27.   // With AMD, it's possible to define modules in a few
28.   // different ways due as it's relatively flexible with
29.   // certain aspects of the syntax
30.   return  {
31.  plot:  function(x, y){
32.   return graph.drawPie(math.randomGrid(x,y));
33.   }
34.   }
35.   };
36. });

*require* on the other hand is typically used to load code in a top-level JavaScript file or within a module should you wish to dynamically fetch dependencies. An example of its usage is:

#### Understanding AMD: require()

1. // Consider 'foo' and 'bar' are two external modules
2. // In this example, the 'exports' from the two modules loaded are passed as
3. // function arguments to the callback (foo and bar)
4. // so that they can similarly be accessed
5.
6. require(['foo',  'bar'],  function  ( foo, bar )  {
7.   // rest of your code here
8.  foo.doSomething();
9. });

#### Dynamically-loaded Dependencies

1. define(function  (  require  )  {
2.   var isReady =  false, foobar;
3.
4.   // note the inline require within our module definition
5.   require(['foo',  'bar'],  function  (foo, bar)  {
6.  isReady =  true;
7.  foobar = foo()  + bar();
8.   });
9.
10.   // we can still return a module
11.   return  {
12.  isReady: isReady,
13.  foobar: foobar
14.   };
15. });
16.

#### Understanding AMD: plugins

The following is an example of defining an AMD-compatible plugin:
1. // With AMD, it's possible to load in assets of almost any kind
2. // including text-files and HTML. This enables us to have template
3. // dependencies which can be used to skin components either on
4. // page-load or dynamically.
5.
6. define(['./templates',  'text!./template.md','css!./template.css'],
7.   function( templates,  template  ){
8.  console.log(templates);
9.   // do some fun template stuff here.
10.   }
11. });

**Note:** Although css! is included for loading CSS dependencies in the above example, it's important to remember that this approach has some caveats such as it not being fully possible to establish when the CSS is fully loaded. Depending on how you approach your build, it may also result in CSS being included as a dependency in the optimized file, so use CSS as a loaded dependency in such cases with caution.

#### Loading AMD Modules Using require.js

1. require(['app/myModule'],
2.   function( myModule ){
3.   // start the main module which in-turn
4.   // loads other modules
5.   var  module  =  new myModule();
6.   module.doStuff();
7. });

#### Loading AMD Modules Using curl.js

1. curl(['app/myModule.js'],
2.   function( myModule ){
3.   // start the main module which in-turn
4.   // loads other modules
5.   var  module  =  new myModule();
6.   module.doStuff();
7. });

#### Modules With Deferred Dependencies

1. // This could be compatible with jQuery's Deferred implementation,
2. // futures.js (slightly different syntax) or any one of a number
3. // of other implementations
4. define(['lib/Deferred'],  function(  Deferred  ){
5.   var defer =  new  Deferred();
6.   require(['lib/templates/?index.html','lib/data/?stats'],
7.   function(  template, data ){
8.  defer.resolve({  template:  template, data:data });
9.   }
10.   );
11.   return defer.promise();
12. });

#### Why Is AMD A Better Choice For Writing Modular JavaScript?

- Provides a clear proposal for how to approach defining flexible modules.

- Significantly cleaner than the present global namespace and `<script>` tag solutions many of us rely on. There's a clean way to declare stand-alone modules and dependencies they may have.

- Module definitions are encapsulated, helping us to avoid pollution of the global namespace.

- Works better than some alternative solutions (eg. CommonJS, which we'll be looking at shortly). Doesn't have issues with cross-domain, local or debugging and doesn't have a reliance on server-side tools to be used. Most AMD loaders support loading modules in the browser without a build process.

- Provides a 'transport' approach for including multiple modules in a single file. Other approaches like CommonJS have yet to agree on a transport format.

- It's possible to lazy load scripts if this is needed.

**Related Reading**
[The RequireJS Guide To AMD](http://requirejs.org/docs/whyamd.html)

[What's the fastest way to load AMD modules?](http://unscriptable.com/index.php/2011/09/21/what-is-the-fastest-way-to-load-amd-modules/)

[AMD vs. CJS, what's the better format?](http://unscriptable.com/index.php/2011/09/30/amd-versus-cjs-whats-the-best-format/)

[AMD Is Better For The Web Than CommonJS Modules](http://blog.millermedeiros.com/2011/09/amd-is-better-for-the-web-than-commonjs-modules/)

[The Future Is Modules Not Frameworks](http://unscriptable.com/code/Modules-Frameworks/)

[AMD No Longer A CommonJS Specification](http://groups.google.com/group/commonjs/browse_thread/thread/96a0963bcb4ca78f/cf73db49ce267ce1?lnk=gst#)

[On Inventing JavaScript Module Formats And Script Loaders](http://tagneto.blogspot.com/2011/04/on-inventing-js-module-formats-and.html)

[The AMD Mailing List](http://groups.google.com/group/amd-implement)

### AMD Modules With Dojo

Defining AMD-compatible modules using Dojo is fairly straight-forward. As per above, define any module dependencies in an array as the first argument and provide a callback (factory) which will execute the module once the dependencies have been loaded. e.g:

1. define(["dijit/Tooltip"],  function(  Tooltip  ){
2.   //Our dijit tooltip is now available for local use
3.   new  Tooltip(...);
4. });

Note the anonymous nature of the module which can now be both consumed by a Dojo asynchronous loader, RequireJS or the standard [dojo.require()](http://docs.dojocampus.org/dojo/require) module loader that you may be used to using.

For those wondering about module referencing, there are some interesting gotchas that are useful to know here. Although the AMD-advocated way of referencing modules declares them in the dependency list with a set of matching arguments, this isn't supported by the Dojo 1.6 build system - it really only works for AMD-compliant loaders. e.g:

1. define(["dojo/cookie",  "dijit/Tooltip"],  function( cookie,  Tooltip  ){
2.   var cookieValue = cookie("cookieName");
3.   new  Tree(...);
4. });

This has many advances over nested namespacing as modules no longer need to directly reference complete namespaces every time - all we require is the 'dojo/cookie' path in dependencies, which once aliased to an argument, can be referenced by that variable. This removes the need to repeatedly type out 'dojo.' in your applications.

**Note:** Although Dojo 1.6 doesn't officially support user-based AMD modules (nor asynchronous loading), it's possible to get this working with Dojo using a number of different script loaders. At present, all Dojo core and Dijit modules have been transformed to the AMD syntax and improved overall AMD support will likely land between 1.7 and 2.0.

The final gotcha to be aware of is that if you wish to continue using the Dojo build system or wish to migrate older modules to this newer AMD-style, the following more verbose version enables easier migration. Notice that dojo and dijit and referenced as dependencies too:

1. define(["dojo",  "dijit",  "dojo/cookie",  "dijit/Tooltip"],  function(dojo, dijit){

2.   var cookieValue = dojo.cookie("cookieName");
3.   new dijit.Tooltip(...);
4. });

### AMD Module Design Patterns (Dojo)

If you've followed any of my previous posts on the benefits of design patterns, you'll know that they can be highly effective in improving how we approach structuring solutions to common development problems. [John Hann](http://twitter.com/unscriptable) recently gave an excellent presentation about AMD module design patterns covering the Singleton, Decorator, Mediator and others. I highly recommend checking out his [slides](http://unscriptable.com/code/AMD-module-patterns/) if you get a chance.

Some samples of these patterns can be found below:
**Decorator pattern:**
1. // mylib/UpdatableObservable: a decorator for dojo/store/Observable

2. define(['dojo',  'dojo/store/Observable'],  function  ( dojo,  Observable  )  {

3.   return  function  UpdatableObservable  ( store )  {
4.
5.   var observable = dojo.isFunction(store.notify)  ? store :
6.   new  Observable(store);
7.
8.  observable.updated =  function(  object  )  {
9.  dojo.when(object,  function  ( itemOrArray)  {
10.  dojo.forEach(  [].concat(itemOrArray),  this.notify,  this  );
11.   };
12.   };
13.
14.   return observable;  // makes `new` optional
15.   };
16. });
17.
18.
19. // decorator consumer
20. // a consumer for mylib/UpdatableObservable
21.
22. define(['mylib/UpdatableObservable'],  function  ( makeUpdatable )  {
23.   var observable, updatable, someItem;
24.   // ... here be code to get or create `observable`
25.
26.   // ... make the observable store updatable
27.  updatable = makeUpdatable(observable);  // `new` is optional!
28.
29.   // ... later, when a cometd message arrives with new data item
30.  updatable.updated(updatedItem);
31. });
32.
**Adapter pattern**
1. // 'mylib/Array' adapts `each` function to mimic jQuery's:
2. define(['dojo/_base/lang',  'dojo/_base/array'],  function  (lang, array)  {
3.   return lang.delegate(array,  {
4.  each:  function  (arr,  lambda)  {
5.  array.forEach(arr,  function  (item, i)  {
6.   lambda.call(item, i, item);  // like jQuery's each
7.   })
8.   }
9.   });
10. });
11.
12. // adapter consumer
13. // 'myapp/my-module':
14. define(['mylib/Array'],  function  ( array )  {
15.  array.each(['uno',  'dos',  'tres'],  function  (i, esp)  {
16.   // here, `this` == item
17.   });
18. });
19.

### AMD Modules With jQuery

#### The Basics

Unlike Dojo, jQuery really only comes with one file, however given the plugin-based nature of the library, we can demonstrate how straight-forward it is to define an AMD module that uses it below.

1. define(['js/jquery.js','js/jquery.color.js','js/underscore.js'],
2.   function($, colorPlugin, _){
3.   // Here we've passed in jQuery, the color plugin and Underscore
4.   // None of these will be accessible in the global scope, but we
5.   // can easily reference them below.
6.
7.   // Pseudo-randomize an array of colors, selecting the first
8.   // item in the shuffled array
9.   var shuffleColor = _.first(_.shuffle(['#666','#333','#111']));
10.
11.   // Animate the background-color of any elements with the class
12.   // 'item' on the page using the shuffled color
13.  $('.item').animate({'backgroundColor': shuffleColor });
14.
15.   return  {};
16.   // What we return can be used by other modules
17.   });

There is however something missing from this example and it's the concept of registration.

#### Registering jQuery As An Async-compatible Module

One of the key features that landed in jQuery 1.7 was support for registering jQuery as an asynchronous module. There are a number of compatible script loaders (including RequireJS and curl) which are capable of loading modules using an asynchronous module format and this means fewer hacks are required to get things working.

As a result of jQuery's popularity, AMD loaders need to take into account multiple versions of the library being loaded into the same page as you ideally don't want several different versions loading at the same time. Loaders have the option of either specifically taking this issue into account or instructing their users that there are known issues with third party scripts and their libraries.

What the 1.7 addition brings to the table is that it helps avoid issues with other third party code on a page accidentally loading up a version of jQuery on the page that the owner wasn't expecting. You don't want other instances clobbering your own and so this can be of benefit.

The way this works is that the script loader being employed indicates that it supports multiple jQuery versions by specifying that a property, `define.amd.jQuery` is equal to true. For those interested in more specific implementation details, we register jQuery as a named module as there is a risk that it can be concatenated with other files which may use AMD's `define()` method, but not use a proper concatenation script that understands anonymous AMD module definitions.

The named AMD provides a safety blanket of being both robust and safe for most use-cases.

// Account for the existence of more than one global // instances of jQuery in the document, cater for testing // .noConflict()

var jQuery = this.jQuery || "jQuery", $ = this.$ || "$",
originaljQuery = jQuery,
original$ = $,
amdDefined;
define(['jquery'] , function ($) {
$('.items').css('background','green');
return function () {};
});

// The very easy to implement flag stating support which // would be used by the AMD loader

define.amd = {
jQuery: true
};

#### Smarter jQuery Plugins

I've recently discussed some ideas and examples of how jQuery plugins could be written using Universal Module Definition ([UMD](https://github.com/umdjs)) patterns [here](http://coding.smashingmagazine.com/2011/10/11/essential-jquery-plugin-patterns/). UMDs define modules that can work on both the client and server, as well as with all popular script loaders available at the moment. Whilst this is still a new area with a lot of concepts still being finalized, feel free to look at the code samples in the section title *AMD && CommonJS* below and let me know if you feel there's anything we could do better.

#### What Script Loaders & Frameworks Support AMD?

In-browser:

- RequireJS [http://requirejs.org](http://requirejs.org/)
- curl.js http://github.com/unscriptable/curl
- bdLoad http://bdframework.com/bdLoad
- Yabble http://github.com/jbrantly/yabble
- PINF http://github.com/pinf/loader-js
- (and more)

##### Server-side:

- RequireJS [http://requirejs.org](http://requirejs.org/)
- PINF http://github.com/pinf/loader-js

### AMD Conclusions

The above are very trivial examples of just how useful AMD modules can truly be, but they hopefully provide a foundation for understanding how they work.

You may be interested to know that many visible large applications and companies currently use AMD modules as a part of their architecture. These include [IBM](http://www.ibm.com/) and the [BBC iPlayer](http://www.bbc.co.uk/iplayer/), which highlight just how seriously this format is being considered by developers at an enterprise-level.

For more reasons why many developers are opting to use AMD modules in their applications, you may be interested in [this](http://tagneto.blogspot.com/2011/04/on-inventing-js-module-formats-and.html) post by James Burke.

## CommonJS A Module Format Optimized For The Server

[CommonJS](http://www.commonjs.org/) are a volunteer working group which aim to design, prototype and standardize JavaScript APIs. To date they've attempted to ratify standards for both [modules](http://www.commonjs.org/specs/modules/1.0/) and [packages](http://wiki.commonjs.org/wiki/Packages/1.0). The CommonJS module proposal specifies a simple API for declaring modules server-side and unlike AMD attempts to cover a broader set of concerns such as io, filesystem, promises and more.

### Getting Started

From a structure perspective, a CJS module is a reusable piece of JavaScript which exports specific objects made available to any dependent code - there are typically no function wrappers around such modules (so you won't see `define` used here for example).

At a high-level they basically contain two primary parts: a free variable named `exports` which contains the objects a module wishes to make available to other modules and a `require` function that modules can use to import the exports of other modules.

#### Understanding CJS: require() and exports

1. // package/lib is a dependency we require
2. var lib =  require('package/lib');
3.
4. // some behaviour for our module
5. function foo(){
6.  lib.log('hello world!');
7. }
8.
9. // export (expose) foo to other modules
10. exports.foo = foo;

#### Basic consumption of exports

1. // define more behaviour we would like to expose
2. function foobar(){
3.   this.foo =  function(){
4.  console.log('Hello foo');
5.   }
6.
7.   this.bar =  function(){
8.  console.log('Hello bar');
9.   }
10. }
11.
12. // expose foobar to other modules
13. exports.foobar = foobar;
14.
15.
16. // an application consuming 'foobar'
17.
18. // access the module relative to the path
19. // where both usage and module files exist
20. // in the same directory
21.
22. var foobar =  require('./foobar').foobar,
23.  test =  new foobar();
24.
25. test.bar();  // 'Hello bar'
26.

#### AMD-equivalent Of The First CJS Example

1. define(['package/lib'],  function(lib){
2.
3.   // some behaviour for our module
4.   function foo(){
5.  lib.log('hello world!');
6.   }
7.
8.   // export (expose) foo for other modules
9.   return  {
10.  foobar: foo
11.   };
12. });

#### Consuming Multiple Dependencies

##### app.js

1. var modA =  require('./foo');
2. var modB =  require('./bar');
3.
4. exports.app =  function(){
5.  console.log('Im an application!');
6. }
7.
8. exports.foo =  function(){
9.   return modA.helloWorld();
10. }

##### bar.js

1. exports.name =  'bar';

##### foo.js

1. require('./bar');
2. exports.helloWorld =  function(){
3.   return  'Hello World!!''
4. }

#### What Loaders & Frameworks Support CJS?

##### In-browser:

- curl.js http://github.com/unscriptable/curl
- SproutCore 1.1 [http://sproutcore.com](http://sproutcore.com/)
- PINF http://github.com/pinf/loader-js
- (and more)

##### Server-side:

- Node[http://nodejs.org](http://nodejs.org/)
- Narwhal https://github.com/tlrobinson/narwhal
- Perseverehttp://www.persvr.org/
- Wakandahttp://www.wakandasoft.com/

#### Is CJS Suitable For The Browser?

There are developers that feel CommonJS is better suited to server-side development which is one reason there's currently a level of **disagreement** over which format should and will be used as the de facto standard in the pre-Harmony age moving forward. Some of the arguments against CJS include a note that many CommonJS APIs address server-oriented features which one would simply not be able to implement at a browser-level in JavaScript - for example, *io*, *system* and *js* could be considered unimplementable by the nature of their functionality.

That said, it's useful to know how to structure CJS modules regardless so that we can better appreciate how they fit in when defining modules which may be used everywhere. Modules which have applications on both the client and server include validation, conversion and templating engines. The way some developers are approaching choosing which format to use is opting for CJS when a module can be used in a server-side environment and using AMD if this is not the case.

As AMD modules are capable of using plugins and can define more granular things like constructors and functions this makes sense. CJS modules are only able to define objects which can be tedious to work with if you're trying to obtain constructors out of them.

Although it's beyond the scope of this article, you may have also noticed that there were different types of 'require' methods mentioned when discussing AMD and CJS.

The concern with a similar naming convention is of course confusion and the community are currently split on the merits of a global require function. John Hann's suggestion here is that rather than calling it 'require', which would probably fail to achieve the goal of informing users about the different between a global and inner require, it may make more sense to rename the global loader method something else (e.g. the name of the library). It's for this reason that a loader like curl.js uses `curl()` as opposed to `require`.

**Related Reading**

[Demystifying CommonJS Modules](http://dailyjs.com/2010/10/18/modules/)

[JavaScript Growing Up](http://www.slideshare.net/davidpadbury/javascript-growing-up)

[The RequireJS Notes On CommonJS](http://requirejs.org/docs/commonjs.html)

[Taking Baby Steps With Node.js And CommonJS - Creating Custom Modules](http://elegantcode.com/2011/02/04/taking-baby-steps-with-node-js-commonjs-and-creating-custom-modules/)

[Asynchronous CommonJS Modules for the Browser](http://www.sitepen.com/blog/2010/07/16/asynchronous-commonjs-modules-for-the-browser-and-introducing-transporter/)

[The CommonJS Mailing List](http://groups.google.com/group/commonjs)

## AMD && CommonJS Competing, But Equally Valid Standards

Whilst this article has placed more emphasis on using AMD over CJS, the reality is that both formats are valid and have a use.

AMD adopts a browser-first approach to development, opting for asynchronous behaviour and simplified backwards compatability but it doesn't have any concept of File I/O. It supports objects, functions, constructors, strings, JSON and many other types of modules, running natively in the browser. It's incredibly flexible.

CommonJS on the other hand takes a server-first approach, assuming synchronous behaviour, no global *baggage* as John Hann would refer to it as and it attempts to cater for the future (on the server). What we mean by this is that because CJS supports unwrapped modules, it can feel a little more close to the ES.next/Harmony specifications, freeing you of the `define()` wrapper that AMD enforces. CJS modules however only support objects as modules.

Although the idea of yet another module format may be daunting, you may be interested in some samples of work on hybrid AMD/CJS and Univeral AMD/CJS modules.

#### Basic AMD Hybrid Format (John Hann)

1. define(  function  (require, exports,  module){
2.
3.   var shuffler =  require('lib/shuffle');
4.
5.  exports.randomize =  function( input ){
6.   return shuffler.shuffle(input);
7.   }
8. });

#### AMD/CommonJS Universal Module Definition (Variation 2, [UMDjs](https://github.com/umdjs/umd))

1. /**
2.  * exports object based version, if you need to make a
3.  * circular dependency or need compatibility with
4.  * commonjs-like environments that are not Node.
5.  */
6. (function  (define)  {
7.   //The 'id' is optional, but recommended if this is
8.   //a popular web library that is used mostly in
9.   //non-AMD/Node environments. However, if want
10.   //to make an anonymous module, remove the 'id'
11.   //below, and remove the id use in the define shim.
12.  define('id',  function  (require, exports)  {
13.   //If have dependencies, get them here
14.   var a =  require('a');
15.
16.   //Attach properties to exports.
17.  exports.name = value;
18.   });

19. }(typeof define ===  'function'  && define.amd ? define :  function  (id, factory)  {

20.   if  (typeof exports !==  'undefined')  {
21.   //commonjs
22.  factory(require, exports);
23.   }  else  {
24.   //Create a global function. Only works if
25.   //the code does not have dependencies, or
26.   //dependencies fit the call pattern below.
27.  factory(function(value)  {
28.   return window[value];
29.   },  (window[id]  =  {}));
30.   }
31. }));

#### Extensible UMD Plugins With (Variation by myself and Thomas Davis).

##### core.js

1. // Module/Plugin core
2. // Note: the wrapper code you see around the module is what enables
3. // us to support multiple module formats and specifications by
4. // mapping the arguments defined to what a specific format expects
5. // to be present. Our actual module functionality is defined lower
6. // down, where a named module and exports are demonstrated.
7.
8. ;(function  ( name, definition ){
9.   var theModule = definition(),
10.   // this is considered "safe":
11.  hasDefine =  typeof define ===  'function'  && define.amd,
12.   // hasDefine = typeof define === 'function',
13.  hasExports =  typeof  module  !==  'undefined'  &&  module.exports;
14.
15.   if  ( hasDefine ){  // AMD Module
16.  define(theModule);
17.   }  else  if  ( hasExports )  {  // Node.js Module
18.   module.exports = theModule;

19.   }  else  {  // Assign to common namespaces or simply the global object (window)

20.   (this.jQuery ||  this.ender ||  this.$ ||  this)[name]  = theModule;
21.   }
22. })(  'core',  function  ()  {
23.   var  module  =  this;
24.   module.plugins =  [];
25.   module.highlightColor =  "yellow";
26.   module.errorColor =  "red";
27.
28.   // define the core module here and return the public API
29.
30.   // this is the highlight method used by the core highlightAll()
31.   // method and all of the plugins highlighting elements different
32.   // colors
33.   module.highlight =  function(el,strColor){
34.   // this module uses jQuery, however plain old JavaScript
35.   // or say, Dojo could be just as easily used.
36.   if(this.jQuery){
37.  jQuery(el).css('background', strColor);
38.   }
39.   }
40.   return  {
41.  highlightAll:function(){
42.   module.highlight('div',  module.highlightColor);
43.   }
44.   };
45.
46. });

##### myExtension.js

1. ;(function  ( name, definition )  {
2.   var theModule = definition(),
3.  hasDefine =  typeof define ===  'function',
4.  hasExports =  typeof  module  !==  'undefined'  &&  module.exports;
5.
6.   if  ( hasDefine )  {  // AMD Module
7.  define(theModule);
8.   }  else  if  ( hasExports )  {  // Node.js Module
9.   module.exports = theModule;

10.   }  else  {  // Assign to common namespaces or simply the global object (window)

11.
12.
13.   // account for for flat-file/global module extensions
14.   var obj =  null;
15.   var namespaces = name.split(".");
16.   var scope =  (this.jQuery ||  this.ender ||  this.$ ||  this);
17.   for  (var i =  0; i < namespaces.length; i++)  {
18.   var packageName = namespaces[i];
19.   if  (obj && i == namespaces.length -  1)  {
20.  obj[packageName]  = theModule;
21.   }  else  if  (typeof scope[packageName]  ===  "undefined")  {
22.  scope[packageName]  =  {};
23.   }
24.  obj = scope[packageName];
25.   }
26.
27.   }
28. })('core.plugin',  function  ()  {
29.
30.   // define your module here and return the public API
31.   // this code could be easily adapted with the core to
32.   // allow for methods that overwrite/extend core functionality
33.   // to expand the highlight method to do more if you wished.
34.   return  {
35.  setGreen:  function  ( el )  {
36.  highlight(el,  'green');
37.   },
38.  setRed:  function  ( el )  {
39.  highlight(el, errorColor);
40.   }
41.   };
42.
43. });

##### app.js

1. $(function(){
2.
3.   // the plugin 'core' is exposed under a core namespace in
4.   // this example which we first cache
5.   var core = $.core;
6.
7.   // use then use some of the built-in core functionality to
8.   // highlight all divs in the page yellow
9.  core.highlightAll();
10.
11.   // access the plugins (extensions) loaded into the 'plugin'
12.   // namespace of our core module:
13.
14.   // Set the first div in the page to have a green background.
15.  core.plugin.setGreen("div:first");
16.   // Here we're making use of the core's 'highlight' method
17.   // under the hood from a plugin loaded in after it
18.
19.   // Set the last div to the 'errorColor' property defined in
20.   // our core module/plugin. If you review the code further down
21.   // you'll see how easy it is to consume properties and methods
22.   // between the core and other plugins
23.  core.plugin.setRed('div:last');
24. });

## ES Harmony Modules Of The Future

[TC39](http://www.ecma-international.org/memento/TC39.htm), the standards body charged with defining the syntax and semantics of ECMAScript and its future iterations is composed of a number of very intelligent developers. Some of these developers (such as [Alex Russell](http://twitter.com/slightlylate)) have been keeping a close eye on the evolution of JavaScript usage for large-scale development over the past few years and are acutely aware of the need for better language features for writing more modular JS.

For this reason, there are currently proposals for a number of exciting additions to the language including flexible [modules](http://wiki.ecmascript.org/doku.php?id=harmony:modules) that can work on both the client and server, a [module loader](http://wiki.ecmascript.org/doku.php?id=harmony:module_loaders) and [more](http://wiki.ecmascript.org/doku.php?id=harmony:proposals). In this section, I'll be showing you some code samples of the syntax for modules in ES.next so you can get a taste of what's to come.

**Note: ** Although Harmony is still in the proposal phases, you can already try out (partial) features of ES.next that address native support for writing modular JavaScript thanks to Google's [Traceur](http://code.google.com/p/traceur-compiler/) compiler. To get up and running with Traceur in under a minute, read this [getting started](http://code.google.com/p/traceur-compiler/wiki/GettingStarted) guide. There's also a JSConf [presentation](http://traceur-compiler.googlecode.com/svn/branches/v0.10/presentation/index.html) about it that's worth looking at if you're interested in learning more about the project.

### Modules With Imports And Exports

If you've read through the sections on AMD and CJS modules you may be familiar with the concept of module dependencies (imports) and module exports (or, the public API/variables we allow other modules to consume). In ES.next, these concepts have been proposed in a slightly more succinct manner with dependencies being specified using an `import` keyword. `export` isn't greatly different to what we might expect and I think many developers will look at the code below and instantly 'get' it.

- **import** declarations bind a module's exports as local variables and may be renamed to avoid name collisions/conflicts.
- **export** declarations declare that a local-binding of a module is externally visible such that other modules may read the exports but can't modify them. Interestingly, modules may export child modules however can't export modules that have been defined elsewhere. You may also rename exports so their external name differs from their local names.

1. module staff{
2.   // specify (public) exports that can be consumed by
3.   // other modules
4.   export  var baker =  {
5.  bake:  function( item ){
6.  console.log('Woo! I just baked '  + item);
7.   }
8.   }
9. }
10.
11. module skills{
12.   export  var specialty =  "baking";
13.   export  var experience =  "5 years";
14. }
15.
16. module cakeFactory{
17.
18.   // specify dependencies
19.   import baker from staff;
20.
21.   // import everything with wildcards
22.   import  *  from skills;
23.
24.   export  var oven =  {
25.  makeCupcake:  function( toppings ){
26.  baker.bake('cupcake', toppings);
27.   },
28.  makeMuffin:  function( mSize ){
29.  baker.bake('muffin', size);
30.   }
31.   }
32. }

### Modules Loaded From Remote Sources

The module proposals also cater for modules which are remotely based (e.g. a third-party API wrapper) making it simplistic to load modules in from external locations. Here's an example of us pulling in the module we defined above and utilizing it:

1. module cakeFactory from  'http://addyosmani.com/factory/cakes.js';
2. cakeFactory.oven.makeCupcake('sprinkles');
3. cakeFactory.oven.makeMuffin('large');

### Module Loader API

The module loader proposed describes a dynamic API for loading modules in highly controlled contexts. Signatures supported on the loader include `load( url, moduleInstance, error) ` for loading modules, `createModule( object, globalModuleReferences)` and [others](http://wiki.ecmascript.org/doku.php?id=harmony:module_loaders). Here's another example of us dynamically loading in the module we initially defined. Note that unlike the last example where we pulled in a module from a remote source, the module loader API is better suited to dynamic contexts.

1. Loader.load('http://addyosmani.com/factory/cakes.js',
2.   function(cakeFactory){
3.  cakeFactory.oven.makeCupcake('chocolate');
4.   });

### CommonJS-like Modules For The Server

For developers who are server-oriented, the module system proposed for ES.next isn't just constrained to looking at modules in the browser. Below for examples, you can see a CJS-like module proposed for use on the server:

1. // io/File.js
2. export  function open(path)  {  ...  };
3. export  function close(hnd)  {  ...  };
1. // compiler/LexicalHandler.js
2. module file from  'io/File';
3.
4. import  { open, close }  from file;
5. export  function scan(in)  {
6.   try  {
7.   var h = open(in)  ...
8.   }
9.   finally  { close(h)  }
10. }
1. module lexer from  'compiler/LexicalHandler';
2. module stdlib from  '@std';
3.
4. //... scan(cmdline[0]) ...

### Classes With Constructors, Getters & Setters

The notion of a class has always been a contentious issue with purists and we've so far got along with either falling back on JavaScript's [prototypal](http://javascript.crockford.com/prototypal.html) nature or through using frameworks or abstractions that offer the ability to use *class* definitions in a form that desugars to the same prototypal behavior.

In Harmony, classes come as part of the language along with constructors and (finally) some sense of true privacy. In the following examples, I've included some inline comments to help you understand how classes are structured, but you may also notice the lack of the word 'function' in here. This isn't a typo error: TC39 have been making a conscious effort to decrease our abuse of the `function` keyword for everything and the hope is that this will help simplify how we write code.

1. class  Cake{
2.
3.   // We can define the body of a class' constructor
4.   // function by using the keyword 'constructor' followed
5.   // by an argument list of public and private declarations.
6.  constructor( name, toppings, price, cakeSize ){
7.   public name = name;
8.   public cakeSize = cakeSize;
9.   public toppings = toppings;
10.   private price = price;
11.
12.   }
13.
14.   // As a part of ES.next's efforts to decrease the unnecessary
15.   // use of 'function' for everything, you'll notice that it's
16.   // dropped for cases such as the following. Here an identifier
17.   // followed by an argument list and a body defines a new method
18.
19.  addTopping( topping ){
20.   public(this).toppings.push(topping);
21.   }
22.
23.   // Getters can be defined by declaring get before
24.   // an identifier/method name and a curly body.
25.   get allToppings(){
26.   return  public(this).toppings;
27.   }
28.
29.   get qualifiesForDiscount(){
30.   return  private(this).price >  5;
31.   }
32.
33.   // Similar to getters, setters can be defined by using
34.   // the 'set' keyword before an identifier
35.   set cakeSize( cSize ){
36.   if( cSize <  0  ){
37.   throw  new  Error('Cake must be a valid size -
38.  either small, medium or large');
39.   }
40.   public(this).cakeSize = cSize;
41.   }
42.
43.
44. }

### ES Harmony Conclusions

As you can see, ES.next is coming with some exciting new additions. Although Traceur can be used to an extent to try our such features in the present, remember that it may not be the best idea to plan out your system to use Harmony (just yet). There are risks here such as specifications changing and a potential failure at the cross-browser level (IE9 for example will take a while to die) so your best bets until we have both spec finalization and coverage are AMD (for in-browser modules) and CJS (for those on the server).

**Related Reading**

[A First Look At The Upcoming JavaScript Modules](http://www.2ality.com/2011/03/first-look-at-upcoming-javascript.html)

[David Herman On JavaScript/ES.Next (Video)](http://blog.mozilla.com/dherman/2011/02/23/my-js-meetup-talk/)

[ES Harmony Module Proposals](http://wiki.ecmascript.org/doku.php?id=harmony:modules)

[ES Harmony Module Semantics/Structure Rationale](http://wiki.ecmascript.org/doku.php?id=harmony:modules_rationale)

[ES Harmony Class Proposals](http://wiki.ecmascript.org/doku.php?id=harmony:classes)

## Conclusions And Further Reading A Review

In this article we've reviewed several of the options available for writing modular JavaScript using modern module formats. These formats have a number of advantages over using the (classical) module pattern alone including: avoiding a need for developers to create global variables for each module they create, better support for static and dynamic dependency management, improved compatibility with script loaders, better (optional) compatibility for modules on the server and more.

In short, I recommend trying out what's been suggested today as these formats offer a lot of power and flexibility that can help when building applications based on many reusable blocks of functionality.

And that's it for now. If you have further questions about any of the topics covered today, feel free to hit me up on [twitter](http://twitter.com/addyosmani) and I'll do my best to help!

Copyright Addy Osmani, 2012. All Rights Reserved.