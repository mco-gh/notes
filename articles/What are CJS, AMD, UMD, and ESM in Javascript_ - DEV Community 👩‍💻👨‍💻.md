What are CJS, AMD, UMD, and ESM in Javascript? - DEV Community 👩‍💻👨‍💻

#  What are CJS, AMD, UMD, and ESM in Javascript?

###     [  [6175aabf-bdde-4c09-86e4-b099cea27c9b.webp](../_resources/49da66749be79e972c089d5099981808.webp)  Igor Irianto](https://dev.to/iggredible)    [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](http://twitter.com/iggredible)  Jul 22 '19  *Updated on Mar 03, 2020*  ・4 min read

 [#javascript](https://dev.to/t/javascript)  [#modules](https://dev.to/t/modules)  [#cjs](https://dev.to/t/cjs)  [#esm](https://dev.to/t/esm)

In the beginning, Javascript did not have a way to import/export modules. This is a problem. Imagine writing your app in just one file - it would be nightmarish!

Then, people much, much smarter than me attempted to add modularity to Javascript. Some of them are **CJS, AMD, UMD, and ESM**. You may have heard some of them (there are other methods, but these are the big players).

I will cover high-level information: syntax, purpose, and basic behaviors. My goal is to help readers recognize when they see them in the wild .

#   [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#cjs) CJS

CJS is short for CommonJS. Here is what it looks like:

	//importing
	const doSomething = require('./doSomething.js');

	//exporting
	module.exports = function doSomething(n) {
	  // do something
	}

- Some of you may immediately recognize CJS syntax from node. That's because node [uses CJS module format](https://blog.risingstack.com/node-js-at-scale-module-system-commonjs-require/).
- CJS imports module synchronously.
- You can import from a library `node_modules` or local dir. Either by `const myLocalModule = require('./some/local/file.js')` or `var React = require('react');` works.
- When CJS imports, it will give you a **copy** of the imported object.
- CJS will not work in the browser. It will have to be transpiled and bundled.

#   [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#amd) AMD

AMD stands for Asynchronous Module Definition. Here is a sample code:

	define(['dep1', 'dep2'], function (dep1, dep2) {
	    //Define the module value by returning a value.
	    return function () {};
	});

or

	// "simplified CommonJS wrapping" https://requirejs.org/docs/whyamd.html
	define(function (require) {
	    var dep1 = require('dep1'),
	        dep2 = require('dep2');
	    return function () {};
	});

- AMD imports modules asynchronously (hence the name).
- AMD is [made for frontend](http://tagneto.blogspot.com/2011/04/on-inventing-js-module-formats-and.html) (when it was proposed) (while CJS backend).
- AMD syntax is less intuitive than CJS. I think of AMD as the exact opposite sibling of CJS.

#   [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#umd) UMD

UMD stands for Universal Module Definition. Here is what it may look like ([source](http://bob.yexley.net/umd-javascript-that-runs-anywhere/)):

	(function (root, factory) {
	    if (typeof define === "function" && define.amd) {
	        define(["jquery", "underscore"], factory);
	    } else if (typeof exports === "object") {
	        module.exports = factory(require("jquery"), require("underscore"));
	    } else {
	        root.Requester = factory(root.$, root._);
	    }
	}(this, function ($, _) {
	    // this is where I defined my module implementation

	    var Requester = { // ... };

	    return Requester;
	}));

- Works on front and back end (hence the name *universal*).
- Unlike CJS or AMD, UMD is more like a pattern to configure several module systems. Check [here](https://github.com/umdjs/umd/) for more patterns.
- UMD is usually used as a fallback module when using bundler like Rollup/ Webpack

#   [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#esm) ESM

ESM stands for ES Modules. It is Javascript's proposal to implement a [standard](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/) module system. I am sure many of you have seen this:

	import React from 'react';

Other sightings in the wild:

	import {foo, bar} from './myLib';

	...

	export default function() {
	  // your Function
	};
	export const function1() {...};
	export const function2() {...};

- Works in [many modern browsers](https://caniuse.com/#feat=es6-module)
- It has the best of both worlds: CJS-like simple syntax and AMD's async
- [Tree-shakeable](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/tree-shaking/), due to ES6's [static module structure](https://exploringjs.com/es6/ch_modules.html#static-module-structure)
- ESM allows bundlers like Rollup to [remove unnecessary code](https://dev.to/bennypowers/you-should-be-using-esm-kn3), allowing sites to ship less codes to get faster load.
- Can be called in HTML, just do:

	<script type="module">
	  import {func1} from 'my-lib';

	  func1();
	</script>

This may not work 100% in all browsers yet ([source](https://jakearchibald.com/2017/es-modules-in-browsers/)).

#   [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#summary) Summary

- ESM is the best module format thanks to its simple syntax, async nature, and tree-shakeability.
- UMD works everywhere and usually used as a fallback in case ESM does not work
- CJS is synchronous and good for back end.
- AMD is asynchronous and good for front end.

Thanks for reading, devs! In the future, I plan to write in depth about each module, especially ESM because it is packed with many awesomeness. Stay tuned!

Let me know if you notice any errors.

#   [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#resources) Resources:

- [basic js modules](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/)
- [CJS in nodejs](https://blog.risingstack.com/node-js-at-scale-module-system-commonjs-require/)
- [CJs-ESM comparison](https://jsmodules.io/cjs.html)
- [On inventing JS module formats and script loaders](http://tagneto.blogspot.com/2011/04/on-inventing-js-module-formats-and.html)
- [Why use AMD](https://requirejs.org/docs/whyamd.html)
- [es6 modules browser compatibility](https://caniuse.com/#feat=es6-module)
- [Reduce JS payloads with tree-shaking](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/tree-shaking/)
- [JS modules - static structure](https://exploringjs.com/es6/ch_modules.html#static-module-structure)
- [ESM in browsers](https://jakearchibald.com/2017/es-modules-in-browsers/)
- [ES Modules deep dive - cartoon](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/)
- [Reasons to use ESM](https://dev.to/bennypowers/you-should-be-using-esm-kn3)

 ![giphy.gif](../_resources/acc6fadb8c050e61cb4333f06a67a1e6.gif)
 **[dev.to](https://dev.to/enter)** now has dark mode.

Select **night theme** in the "misc" section of **[your settings](https://dev.to/enter)** ❤️

 [  [47473e61-1b78-449b-98eb-bc1593b02692.webp](../_resources/58d13d2f881a8fdc5f4d6e568ce5fc21.webp)](https://dev.to/iggredible)

#### [Igor Irianto](https://dev.to/iggredible)

Husband . Programmer . Vim .
Web Development should be explained as simple as possible, but no simpler

 [@iggredible](https://dev.to/iggredible)  [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='afhq9550unabb9xlp8nlk7ssi8m6oav3' class='crayons-icon js-evernote-checked' data-evernote-id='74'%3e%3ctitle id='afhq9550unabb9xlp8nlk7ssi8m6oav3' data-evernote-id='75' class='js-evernote-checked'%3eTwitter%3c/title%3e%3cpath d='M22.162 5.656a8.383 8.383 0 01-2.402.658A4.196 4.196 0 0021.6 4c-.82.488-1.719.83-2.656 1.015a4.182 4.182 0 00-7.126 3.814 11.874 11.874 0 01-8.62-4.37 4.168 4.168 0 00-.566 2.103c0 1.45.738 2.731 1.86 3.481a4.168 4.168 0 01-1.894-.523v.052a4.185 4.185 0 003.355 4.101 4.211 4.211 0 01-1.89.072A4.185 4.185 0 007.97 16.65a8.395 8.395 0 01-6.191 1.732 11.83 11.83 0 006.41 1.88c7.693 0 11.9-6.373 11.9-11.9 0-.18-.005-.362-.013-.54a8.495 8.495 0 002.087-2.165l-.001-.001z' fill='%2365bbf2' data-evernote-id='76' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)iggredible](http://twitter.com/iggredible)

 [![info-4bc41b236b6878aef63b8dd32fd80cc4d7d899d3c01be56b5cdff3779c9c0f22.png](../_resources/9b9a36d176ace21f100ba6f41b997b83.png)](https://dev.to/p/editor_guide)

 [(L)](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm)

 [  [f1139a3c-ddc2-4633-a64c-25bfd24fd23e.webp](../_resources/f7047e13a54d8d16e557b1838b6c8275.webp)     Austin S. Hemmelgarn](https://dev.to/ahferroin7)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](https://github.com/Ferroin)

 [ Jul 22 '19](https://dev.to/ahferroin7/comment/d9nk)

ES6 modules aren't asynchronous, at least not as they are in use right now most places. Put simply, unless you're using dynamic imports (see below), each import statement runs to completion before the next statement starts executing, and the process of fetching (and parsing) the module is part of that. They also don't do selective execution of module code like you seem to imply. `import {bar, baz} from './foo.js'` loads, parses, and runs all of './foo.js', then binds the exported entities named 'bar', and 'baz' to those names in the local scope, and only then does the next import statement get evaluated. They do, however, cache the results of this execution and do direct binding, so the above line called from separate files will produce multiple references to the single 'bar' and 'baz' entities.

Now, there is a way to make them asynchronous called 'dynamic import'. In essence, you use `import` as a function in the global scope, which then returns a Promise that resolves to the module you're importing once it's fetched and parsed. However, dynamic import support is somewhat limited right now (IE will never support it, Edge is only going to get it when they finish the switch to Chromium under the hood, and UC Browser, Opera Mini, and a handful of others still don't have it either), so you can't really use them if you want to be truly portable (especially since static imports (the original ES6 import syntax) are only valid at the top level, so you can't conditionally use them if you don't happen to have dynamic import support).

As a result of this, code built around ES6 modules is often slower than equivalent code built on AMD (or a good UMD syntax).

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/d9nk)

 [  [dbb2e809-5e9a-4d81-98a3-174bd0788b9a.webp](../_resources/49da66749be79e972c089d5099981808.webp)     Igor Irianto](https://dev.to/iggredible)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](https://twitter.com/iggredible)  Author

 [ Jul 22 '19](https://dev.to/iggredible/comment/d9pg)

Hi Austin, thanks for the reply! I appreciate you taking a lot of time to write this.

1. According to [this link](https://exploringjs.com/es6/ch_modules.html#_moduleshttps://exploringjs.com/es6/ch_modules.html#_modules), it says "ECMAScript 6 gives you the best of both worlds: The synchronous syntax of Node.js plus the asynchronous loading of AMD. ", and [this article](https://blog.logrocket.com/how-to-use-ecmascript-modules-with-node-js/) also says that " ESM is asynchronously loaded, while CommonJS is synchronous."

2. Regarding ESM speed, what I meant to say is that ESM creates static module structure ([source](https://exploringjs.com/es6/ch_modules.html#_benefit-faster-lookup-of-imports), [source](https://dev.to/bennypowers/you-should-be-using-esm-kn3)), allowing bundlers to remove unnecessary code. If we remove unnecessary codes using bundlers like webpack/ rollup, wouldn't this allow the shipping of less codes, and if we ship less code, we get faster load time? (btw, just reread the article, I definitely didn't mention rollup usage. Will revise that).

There is a good chance I am wrong (still learning about JS modules) or interpreted what I read incorrectly (also likely, happened before), but based on what I've read, ESM is async and ESM in overall is faster because it removes unnecessary code. I really appreciate your comment - it forced me to look up more stuff and do more research!

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/d9pg)

 [  [6930ce57-2b3e-46a3-83de-c0996ab37996.webp](../_resources/f7047e13a54d8d16e557b1838b6c8275.webp)     Austin S. Hemmelgarn](https://dev.to/ahferroin7)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](https://github.com/Ferroin)

 [ Jul 22 '19](https://dev.to/ahferroin7/comment/da02)

Digging a bit further myself, I think I know why I misunderstood the sync/async point. Put concretely based on looking further at the ES6 spec, the Node.js implementation of CJS, and the code for Require.js and Alameda):

- CJS executes imports as it finds them, blocking until they finish.
- ESM waits to execute any code in a module until all of it's imports have been loaded and parsed, then does the binding/side-effects stuff in the relative order that they happen.
- AMD also waits to run module code until it's dependencies are loaded and parsed, but it runs each dependency as it's loaded in the order in which they finish loading, instead of the order they're listed in the file.

So, in a way, we're kind of both right. The loading and parsing for ESM modules is indeed asynchronous, but the execution of the code in them is synchronous and serialized based on the order they are imported, while for AMD, even the execution of the code in the modules is asynchronous and based solely on the order they are loaded.

That actually explains why the web app I recently converted from uisng Alameda to ESM took an almost 80% hit to load times, the dependency tree happened to be such that that async execution provided by AMD modules actually significantly cut down on wait times.

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/da02)

 [  [dbb2e809-5e9a-4d81-98a3-174bd0788b9a.webp](../_resources/d7b36f29e77a51236d81b396ba5b6367.webp)     Eugene Karataev](https://dev.to/karataev)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](https://twitter.com/postepenno)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](https://github.com/karataev)

 [ Feb 15](https://dev.to/karataev/comment/lh0f)

Can you please clarify?
> When CJS imports, it will give you a copy of the imported object.
Let's say we have three files:

	// obj.js
	module.exports = {
	  a: 42
	};

	// bar.js
	const fooObj = require('./obj');

	console.log('obj from bar', fooObj);

	// index.js
	const obj = require('./obj');

	obj.a = 50;
	console.log('obj', obj);

	require('./bar');

Console output after run `node index.js`:

	obj { a: 50 }
	obj from bar { a: 50 }

It's clear that `index.js` and `bar.js` share the same object from `obj.js`.

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/lh0f)

 [   kafin](https://dev.to/salimkafin)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](https://twitter.com/salimkafin)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](https://github.com/kafinsalim)

 [ Jan 14](https://dev.to/salimkafin/comment/k8dn)

in this part, which you say can run in browser:

	<script type="module">
	  import {func1} from 'my-lib';

	  func1();
	</script>

where do it get `my-lib` from?

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/k8dn)

 [   Igor Irianto](https://dev.to/iggredible)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](https://twitter.com/iggredible)  Author

 [ Jan 14](https://dev.to/iggredible/comment/k8j3)

You can have local file that exports `func1`, say a js file 'my-lib.js' .
Then your import becomes :

	 import {func1} from './my-lib.js';

inside my-lib.js, have something like:

	export function func1() {
	  return `Hello func1!`;
	}

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/k8j3)

 [   Vadorequest](https://dev.to/vadorequest)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](https://github.com/Vadorequest)

 [ Mar 12](https://dev.to/vadorequest/comment/mg2l)

Another really good article, older, bug goes much more in-depth.

[hacks.mozilla.org/2018/03/es-modul...](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/)

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/mg2l)

 [   Igor Irianto](https://dev.to/iggredible)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](https://twitter.com/iggredible)  Author

 [ Mar 12](https://dev.to/iggredible/comment/mg95)

This is another good article. Good suggestion!

 [REPLY](https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm#/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm/comments/new/mg95)

 [code of conduct](https://dev.to/code-of-conduct)-[report abuse](https://dev.to/report-abuse?url=http://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm?i=i)