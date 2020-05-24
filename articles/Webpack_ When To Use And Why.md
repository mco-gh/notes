Webpack: When To Use And Why

# Webpack: When To Use And Why

**TL;DR** It took me a long time to understand Webpack and how it fits in the build process. This is what I wish someone had told me.

## What is Webpack?

How does Webpack compare to Grunt, Gulp, Browserify, Brunch, etc? What's a "development server?" What on earth is `require("coffee!./cup.coffee");`?

Stop it.

Webpack is a **build tool that puts *all* of your assets, including Javascript, images, fonts, and CSS, in a dependency graph.** Webpack lets you use `require()` in your source code to point to local files, like images, and decide how they're processed in your final Javascript bundle, like replacing the path with a URL pointing to a CDN.

## Should I Use Webpack?

If you're building a complex Front End™ application with many **non-code static assets** such as CSS, images, fonts, etc, then **yes, Webpack will give you great benefits.**

If your application is fairly small, and you don't have many static assets and you only need to build one Javascript file to serve to the client, then **Webpack might be more overhead than you need.**

## A Brief History of the Dependency Graph

Webpack gives us a dependency graph. What does that mean?

In the early days, we "managed" Javascript dependencies by including files in a specific order:

	<script src="jquery.min.js"></script>
	<script src="jquery.some.plugin.js"></script>
	<script src="main.js"></script>

This was too slow because of excess HTTP requests. We graduated to concatenating and minifying our scripts in a build step:

	// build-script.js
	var scripts = [
	    'jquery.min.js',
	    'jquery.some.plugin.js',
	    'main.js'
	].concat().uglify().writeTo('bundle.js');

	// Everything our app needs!
	<script src="bundle.js"></script>

This still **relied on the order of concatenated files**. Even worse, the code could only communicate through global variables! The first script declared a global `jQuery` variable, then `jquery.some.plugin.js` created a new global, or modified the global `jQuery` object. Yuck.

Now we use CommonJS or ES6 modules to put our Javascript in a true **dependency graph.** We make small files that explicitly describe what they need. It's a Good Thing™!

	// Version.js
	module.exports = { version: 1.0 };

	// App.js
	var config = require('./Version.js');
	console.log('App Version:', config.version);

The browser doesn't support `require()`, so we use a build tool to transform the above files into a "bundled" file that the browser can execute properly.

## What Does Webpack Actually Do?

Webpack lets you use `require()` on **local "static assets,"** meaning non-code files.

	<img src={ require('../../assets/logo.png') } />

Wait, you can't `require()` images in Javascript! What's going on?

When you run Webpack, it searches through all of your code for `require()` calls. It compares the path string `../../assets/logo.png` to the **"loader" configuration** you specify.

	loaders: [
	    { test: /.png$/, loader: "file" }
	]

In this example, when you `require()` file paths ending in `.png` (matching the above regular expression), Webpack sends that file to the **file loader**.

The file loader does two things. In the bundled Javascript code, it replaces the `require()` call with a URL string, making it valid Javascript. The string depends on how you configure Webpack. Maybe it becomes a CDN URL, like `cdn.mysite.com/logo.png`.

The file loader also spits out `logo.png` into some local folder you specify, like `dist/`. Now you simply upload the contents of `dist/` to your CDN, deploy your new code, and the image is guaranteed to load on your site.

![](../_resources/009ff1182be750eb35b19930a573c07e.png)  **Key concept:** The `require('logo.png')` source code never actually gets executed in the browser (nor in Node.js). Webpack builds a new Javascript file, replacing `require()` calls with valid Javascript code, such as URLs. The bundled file is what's executed by Node or the browser.

## What About Browserify, Grunt, Gulp…?

Webpack puts your static assets (and source code) in a true dependency graph. **Grunt and Gulp** are only tools for working with files, and have no concept of a depdency graph.

[Browserify](http://browserify.org/) is mainly a tool to transform `require()` calls that work in Node.js into calls that work in the browser. It's a dependency graph for your source code only. There's some plugins like [Parcelify](https://github.com/rotundasoftware/parcelify) to manage some static assets, but you have go to out of your way to make it work.

After using Webpack to manage static assets, **I see no reason to switch back to Grunt, Gulp nor Browserify.** Webpack's core idea of a dependency graph is what makes it so powerful and useful.

## The Good

Static assets in a dependency graph offers many benefits. Here's a few:

- **Dead asset elimination.** This is killer, especially for CSS rules. You only build the images and CSS into your `dist/` folder that your application actually needs.
- **Easier code splitting.** For example, because you know that your file `Homepage.js` only requires specific CSS files, Webpack could easily build a `homepage.css` file to greatly reduce initial file size.
- **You control how assets are processed.** If an image is below a certain size, you could [base64 encode it](https://developer.mozilla.org/en-US/docs/Web/API/WindowBase64/Base64_encoding_and_decoding) directly into your Javascript for fewer HTTP requests. If a JSON file is too big, you can load it from a URL. You can `require('./style.less')` and it's automaticaly parsed by Less into vanilla CSS.
- **Stable production deploys.** You can't accidentally deploy code with images missing, or outdated styles.
- Webpack will slow you down at the start, but give you **great speed benefits** when used correctly. You get hot page reloading. True CSS management. CDN cache busting because Webpack automatically changes file names to hashes of the file contents, etc.

Webpack is the **main build tool adopted by the React community.** This makes finding help easier, and understanding Webpack more valuable.

## The Bad

Webpack isn't perfect and has some pitfalls.

- **The documentation is awful.** I won't sugarcoat this. The language is often confusing, [such as](http://webpack.github.io/docs/what-is-webpack.html) "webpack takes modules with dependencies and generates static assets representing those modules." What? Even the page layout is problematic, with random sidebar entries you can't click on, and animated logos while you're trying to read.
- The **source code** is [similarly painful](https://github.com/webpack/webpack/issues/824).
- **Configuring Webpack** is a minefield for newcomers. The configuration file syntax is confusing. It's best to look at [established examples](https://github.com/erikras/react-redux-universal-hot-example/blob/master/webpack/dev.config.js) from any [boilerplate project](https://github.com/gaearon/react-hot-boilerplate). Also check out the new [webpack-validator](https://www.npmjs.com/package/webpack-validator) library.
- Webpack is **maintained mostly by [one person](https://github.com/sokra).** The rapid community adoption and the [thrust into the spotlight](https://www.youtube.com/watch?v=VkTCL6Nqm6Y) means the ecosystem lags far behind the maturity of React. This has side effects, such as the poor quality of the documentation.
- Webpack introduces a nasty **mini language in a string:**  `require("!style!css!less!bootstrap/less/bootstrap.less");` This syntax is almost never used, and [barely explained](http://webpack.github.io/docs/using-loaders.html#loaders-in-require), but it's all over the documentation. This string language is one of of Webpack's biggest design flaws in my opinion.

## What's The "Dev Server"?

Webpack comes with a built in "[dev server](https://webpack.github.io/docs/webpack-dev-server.html)"; a small [express](https://www.npmjs.com/package/express) app for local development. You simply include one Javascript tag pointed to the server, like `localhost:8080/assets/bundle.js`, and get live code updating and asset management for free.

For large projects, **Webpack isn't worth using without the dev server.**

## Stop Programming With Globals

Traditional Front End™ programming relies mainly on **global variables.** CSS rules all exist in a global namespace. Applying CSS rules to elements relies on manually lining up the contents of global strings (selectors) correctly. A hard coded image path is a global, and you can't statically analyze your codebase to find outdated, moved, or deleted images. Using a custom font in your CSS means you globally defined that font file somewhere, and you better hope you loaded it at the right time!

Stop being a human compiler. Use a dependency graph.

## That's It!

If this post helped you understand the maze of Webpack information better, consider following me [on Twitter](https://twitter.com/andrewray) or [buying me a coffee](https://www.coinbase.com/andrewray) :).

 09 Apr 2016 on [tech](http://blog.andrewray.me/tag/tech/)

#### Andy Ray

*  *  *  *

#### Share this post

 [](https://twitter.com/share?text=Webpack%3A%20When%20To%20Use%20And%20Why%20by%20@andrewray&url=http://blog.andrewray.me/webpack-when-to-use-and-why/)  [](https://www.facebook.com/sharer/sharer.php?u=http://blog.andrewray.me/webpack-when-to-use-and-why/)  [](https://plus.google.com/share?url=http://blog.andrewray.me/webpack-when-to-use-and-why/)