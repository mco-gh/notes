ES6 Modules in Chrome M61+ – Dev Channel – Medium

# ES6 Modules in Chrome M61+

![](../_resources/1f182a531ae4f9e4858b41570fb53cac.png)

ES6 modules are now supported in Chrome, [from 61 onwards](https://www.chromestatus.com/features/5365692190687232)—they also work in older versions, but you’ll have to enable the *Experimental Web **Platform* flag in `chrome:flags`. Chrome now joins many other modern browsers which also [include support, some behind flags](http://caniuse.com/#feat=es6-module). 🚩

Modules are an important part of building any web application which comprises more than trivial script. The JavaScript community has developed impressive workarounds —[ read all about their history in a 2012 post by @addyosmani](https://addyosmani.com/writing-modular-js/)— but there’s huge benefit in using the platform itself*.*

#### *What are the basics?*

Modules must be eventually included in your HTML with `type="module"`, which can appear as an inline or external script tag. See the example —

<script type="module" src="module.js"></script>
<script type="module">
// or an inline script
import {helperMethod} from './providesHelperMethod.js';
helperMethod();
</script>
// providesHelperMethod.js
export function helperMethod() {
console.info(`I'm helping!`);
}

- •Modules are [deferred](https://developer.mozilla.org/en/docs/Web/HTML/Element/script#attr-defer), and only run after a document is loaded
- •The `import` and `export` statements can only appear at the top-level of a file and cannot include variables, so the full import graph can be determined trivially — a bit like C/C++ `#include` or Python `import`
- •All module code is run in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) — aka `'use strict';`

For more technical reading on ES6 Modules, see [Ponyfoo](https://ponyfoo.com/articles/es6-modules-in-depth) or [Jake’s blog](https://jakearchibald.com/2017/es-modules-in-browsers/).

### The High Water Mark for All Browsers

The most interesting part of ES6 modules is that they are only supported by modern, ‘evergreen’ browsers. Their release represents a seachange in they way we build and release JavaScript.

![](../_resources/81b01966b74a9a00e4b1684a30e5942f.png)

[Browsers with ES6 Module support](http://codepen.io/samthor/pen/MmvdOM), May 2017 — **Chrome implies other Chromium-based browsers, like Opera and Samsung *Internet

Legacy browsers that do not support ES6 modules will ignore module code, and only load `script` tags with an empty type or `type="text/javascript"`.

This is an amazing 🌊 water mark— if you ship code via ES6 modules, **you can use modern JavaScript features *without* compiling, or polyfills** — both which can slow down modern browsers or result in larger binary sizes.

And that’s huge — not just to speed up your development process 🛠️, but also for your growing set of users who can support ES6 modules. 🎉

### You can use ES6 modules in production, today

As of writing, only Safari has shipped support for ES6 modules. By the time you read this, the other major browsers might have released the feature publicly —Edge, Firefox and Chrome (as titled*!*) are all behind flags.

If you ship ES6 modules today, there’s *no downside*— you won’t affect legacy browsers — and only those users on supported browsers (or perhaps for developers, testing with the flag enabled) will benefit.

#### 1. Build and ship your code using ES6 modules

Create a project — with a clear entry point, that will be included by your HTML — that uses `import` and `export` to place your code into modules.

// index.html
<script type="module" src="main.js"></script>
// main.js
import {x} from ./foo.js
x().then(y => log(y));
// foo.js
export async function x() {
let y = await fetch('...');
y = await y.json();
return y;
}

For browsers that support ES6 modules, you’re done. This will also shorten your development cycle — you’ll literally not have to compile at all to test changes in any JavaScript, just reload and go.

#### 2. Use tools to compile ES6 modules for legacy browsers

[Rollup](https://github.com/rollup/rollup) ‘rolls up’ ES6 modules into a single file.

![](../_resources/ab61ad8b0aeace93b462a805b990d1ba.png)

Rollup [won’t transpile away](https://github.com/rollup/rollup/wiki/pkg.module#wait-it-just-means-import-and-export--not-other-future-javascript-features) new JavaScript features for very old, ES5-only browsers. It does nothing with ES6 — ignoring `await`, `async` , etc.

(Next, you’ll need to pass your code to Babel, Traceur, or Google’s Closure Compiler to do the remaining ES6 → ES5 compile steps— [see Google for more](https://www.google.com/search?q=compile+es6+to+es5) — this is pretty well documented, but out of scope of this post).

#### 2a. Ship code to legacy browsers

Once you’ve rolled up your ES6 and transpiled it to ES5, ship it as normal, but add the `nomodule` attribute. This lets modern browsers know to ignore this code — it will never even be fetched from the network.

<script nomodule src="compiled.js"></script>

⚠️ **There’s one caveat **— Safari 10.1 & Mobile Safari 10.3 don’t understand `nomodule`, although it’s fixed for its next release. [Include this snippet](https://gist.github.com/samthor/64b114e4a4f539915a95b91ffd340acc) in a regular `script` tag before using `nomodule`.

(This omission doesn’t affect other browsers — [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=1330900) and [Edge](https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/10525830/) don’t support `nomodule` yet either, but their module support is still behind a flag, so no regular users will ever be effected.)

#### (optional) 3. Ship a ‘rolled up’ ES6 module file

As a browser parses your ES6 module code, it will discover a tree of dependencies that it needs to fetch in order to execute your code.

![](../_resources/2e68329eca265f2df1501c746badd7ad.png)

As `index.html` only knows about `/main.js`, it will have to fetch it completely before fetching `/depA.js` and `/depB.js` — and so on. This can cause a number of requests, measurable as ‘request chains’ —

![](../_resources/39ec19015c657eb30cd0a4dc333233e4.png)

**What’s the solution?** Instead of sending many files in production, you can just use Rollup to generate a single, modern ES6 file — and serve that via `<script type="module">` .

This might seem counter-intuitive 🤔 — I’m removing ES6 modules but still shipping *as a module*? But remember that support for “ES6 modules” can be used as just a high water mark — **“ES6 modules” gives you the confidence, *and the mechanism*, to send modern JavaScript to your clients****.**

### What are the caveats?

If you’re building ES6 modules, you won’t be able to import any code that isn’t written in ES6 module format — you’ll experience all *side effects* of code you import — but e.g. `module.exports` from commonJS isn’t somehow magically converted to `export`. 🎩

ES6 modules are therefore great for projects you mostly control, but could be a challenge if you’re depending on the wider ecosystem at large — unless the project you depend on exports itself using the platform syntax.

### Summary

Modern JavaScript features are great, and can increase your productivity — I personally can’t wait to write only `async` and `await` when I work with promises , for example— and I’m so excited to actually ship that ES6 code to modern browsers (while still having a sensible answer for legacy browsers).

I hope this article has given you a push to go forward and update your toolchain — or given you thoughts for your next project. *#UseThePlatform*

#### Feedback?

Please leave comments, queries and insights on Medium — or find me on [Twitter](https://twitter.com/samthor). Thanks for reading! 🕵️