Welcome to Workbox

 ![Small Workbox Logo](../_resources/ed7a9d0f645c20f98697215becc7b6ee.png)

- [Get Started](https://workboxjs.org/#get-started)

- [Examples](https://workboxjs.org/examples/)

- [How Tos](https://workboxjs.org/how_tos/)

- Reference

- [Github](https://github.com/GoogleChrome/workbox)

##### JavaScript Libraries for Progressive Web Apps

# Get Started

## Choose your build tool to get started:

 [![Install Workbox's Webpack plugin](../_resources/57dd3b3017985c08f9221445f18057cd.png)](https://workboxjs.org/get-started/webpack.html)  [![Install Workbox to work with Gulp](../_resources/0db639501dad436f3e77553a41b0c2db.png)](https://workboxjs.org/get-started/gulp.html)  [![Install Workbox to work with NPM Scripts](../_resources/8300c833785076156473309830c7876b.png)](https://workboxjs.org/get-started/npm-script.html)

## Not using a build tool?

Install our command-line interface:

	$ npm install workbox-cli --global

	# Generate a service worker with some smart defaults
	$ workbox-cli generate:sw

## Want to work directly in your service worker?

We support that too with workbox-sw.

	$ npm install --save workbox-sw

Then reference the file from your service worker:

	importScripts('/node_modules/workbox-sw/build/workbox-sw.vX.X.X.prod.js');

# Features

## Easy precaching

	importScripts('/node_modules/workbox-sw/build/workbox-sw.vX.X.X.prod.js');

	const workboxSW = new WorkboxSW();
	workboxSW.precache([
	  {
	    url: '/index.html',
	    revision: 'bb121c',
	  }, {
	    url: '/styles/main.css',
	    revision: 'acd123',
	  }, {
	    url: '/scripts/main.js',
	    revision: 'a32caa',
	  }
	]);

## Powerful debugging support

![Example of Workbox Logging.](../_resources/f089df49745e4c41f732ad07e450094b.png)

## Comprehensive caching strategies

	const workboxSW = new WorkboxSW();
	const networkFirst = workboxSW.strategies.networkFirst();
	workboxSW.router.registerRoute('/schedule', networkFirst);

- *- *Cache only

- *- *Network only

- *- *Cache first, falling back to network

- *- *Network first, falling back to cache

- *- *Cache, with network update

## The next version of sw-precache & sw-toolbox

Workbox is a rethink of our previous service worker libraries with a focus on modularity. It aims to reduce friction with a unified interface, while keeping the overall library size small. Same great features, easier to use and cross-browser compatible.

 [![Workbox Logo](../_resources/18ad4cff8550bedd4a3c1fb2e3b47443.png)](https://workboxjs.org/)

 [![Twitter Logo](../_resources/2f0117fe5c1cfe6de9f065a1538de79b.png)](https://twitter.com/ChromiumDev)  [![Github Logo](../_resources/dcf1473b9390d8c0b7de65476214c81e.png)](https://github.com/GoogleChrome/workbox)

 [![Google Developers Logo](../_resources/831786c21071e8c13883bbcb16a58a25.png)](https://developers.google.com/web/)

This page has been updated. Please refresh the page.