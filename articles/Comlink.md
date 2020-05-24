Comlink

# Comlink

## An RPC library for the web

 **Comlink** allows you to expose JavaScript values from one realm to another – only requiring a `postMessage()`-like channel.

# Site

	const worker = new Worker('worker.js');
	const expensive = Comlink.proxy(worker);
	const result = await expensive();

# Worker

	function expensive() {
	  for(let i = 0; i < 1e12; i++)
	    sum += /* …omg so much maths… */
	  return sum;
	}
	Comlink.expose(expensive, self);

 **Comlink** works with windows, WebWorkers, ServiceWorkers and iFrames. You can `expose()` pretty much anything – including objects, classes or class instances.

# Quickstart

## Select format:

  Module format:    Minified:

### CDN URL

 `https://cdn.jsdelivr.net/npm/comlinkjs/comlink.es6.min.js`  [ Download](https://cdn.jsdelivr.net/npm/comlinkjs/comlink.es6.min.js)  [ Code on GitHub](https://github.com/GoogleChrome/comlink)

## Include:

`import {Comlink} from './comlink.es6.js';`

Built with 🦁 by [Surma](https://twitter.com/DasSurma). Code on [GitHub](https://github.com/GoogleChrome/comlink). Header heavily inspired by [SS16 Virtuoso](http://ss16.thevirts.com/). Icons by [Simple Icons](https://simpleicons.org/) and [Alex Fuller](https://thenounproject.com/alexfuller/).