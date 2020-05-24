Rough.js

# Rough.js

## Create graphics with a hand-drawn, sketchy, appearance

 [Examples](https://github.com/pshihn/rough/wiki/Examples)  [View on GitHub](https://github.com/pshihn/rough)  [Download](https://github.com/pshihn/rough/tree/master/dist)

# Rough.js

**Rough.js** is a light weight (9kB) graphics library that lets you draw in a *sketchy*, *hand-drawn-like*, style. The library defines primitives to draw lines, curves, arcs, polygons, circles, and ellipses. It also supports drawing [SVG paths](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths).

Rough.js works with both [Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) and [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG).

![cap_demo.png](../_resources/7ef010470844ed90018ecec7f21471a5.png)
[@RoughLib](https://twitter.com/RoughLib) on Twitter.

## Install

The latest Rough.js can be downloaded from the [dist folder](https://github.com/pshihn/rough/tree/master/dist).

or from npm:

	npm install --save roughjs

## Usage

![m1.png](../_resources/f4e52d128a083480982334a6af1ce1df.png)

	const rc = rough.canvas(document.getElementById('canvas'));
	rc.rectangle(10, 10, 200, 200); *// x, y, width, height*

or SVG

	const rc = rough.svg(svg);
	let node = rc.rectangle(10, 10, 200, 200); *// x, y, width, height*
	svg.appendChild(node);

### Lines and Ellipses

![m2.png](../_resources/19fe6f29ec7184648869246688e297e0.png)

	rc.circle(80, 120, 50); *// centerX, centerY, diameter*
	rc.ellipse(300, 100, 150, 80); *// centerX, centerY, width, height*
	rc.line(80, 120, 300, 100); *// x1, y1, x2, y2*

### Filling

![m3.png](../_resources/b5139a858239dbc086870eabe7fbce34.png)

	rc.circle(50, 50, 80, { fill: 'red' }); *// fill with red hachure*
	rc.rectangle(120, 15, 80, 80, { fill: 'red' });
	rc.circle(50, 150, 80, {
	  fill: "rgb(10,150,10)",
	  fillWeight: 3 *// thicker lines for hachure*
	});
	rc.rectangle(220, 15, 80, 80, {
	  fill: 'red',
	  hachureAngle: 60, *// angle of hachure,*
	  hachureGap: 8
	});
	rc.rectangle(120, 105, 80, 80, {
	  fill: 'rgba(255,0,200,0.2)',
	  fillStyle: 'solid' *// solid fill*
	});

### Sketching style

![m4.png](../_resources/d77ec02e5f1a59f1f4c82f45d841b923.png)

	rc.rectangle(15, 15, 80, 80, { roughness: 0.5, fill: 'red' });
	rc.rectangle(120, 15, 80, 80, { roughness: 2.8, fill: 'blue' });
	rc.rectangle(220, 15, 80, 80, { bowing: 6, stroke: 'green', strokeWidth: 3 });

### SVG Paths

![m5.png](../_resources/f4400467028b63f265274844ec11e1ba.png)

	rc.path('M80 80 A 45 45, 0, 0, 0, 125 125 L 125 80 Z', { fill: 'green' });
	rc.path('M230 80 A 45 45, 0, 1, 0, 275 125 L 275 80 Z', { fill: 'purple' });
	rc.path('M80 230 A 45 45, 0, 0, 1, 125 275 L 125 230 Z', { fill: 'red' });
	rc.path('M230 230 A 45 45, 0, 1, 1, 275 275 L 275 230 Z', { fill: 'blue' });

SVG Path with simplification:

![m9.png](../_resources/a416dadb9db7355643abd6586b3dec56.png)  ![m10.png](../_resources/92b9c8ed57f471e7c706fc9a9083c9d2.png)

## Using web workers

If you have [Workly](https://github.com/pshihn/workly) imported on your web page (~1k only), RoughJS will automatically offload all processing to a web worker - freeing up your main UI thread. This is great when creating complex drawings using RoughJs like maps. Read more about it [here](https://github.com/pshihn/rough/wiki/RoughJS-in-a-web-worker).

	<script src="https://cdn.jsdelivr.net/gh/pshihn/workly/dist/workly.min.js"></script>
	<script src="../../dist/rough.min.js"></script>

![m6.png](../_resources/2d629eb7c60ebb8f4f5bd3c742c0cfe0.png)
(source code for this map in examples)

## Examples

[View examples here](https://github.com/pshihn/rough/wiki/Examples)

## API & Documentation

[Full Rough.js API](https://github.com/pshihn/rough/wiki)

## Credits

Some of the core algorithms were adapted from [handy](https://www.gicentre.net/software/#/handy/) processing lib.

Algorithm to convert SVG arcs to Canvas [described here](https://www.w3.org/TR/SVG/implnote.html) was adapted from [Mozilla codebase](https://hg.mozilla.org/mozilla-central/file/17156fbebbc8/content/svg/content/src/nsSVGPathDataParser.cpp#l887)

## License

[MIT License](https://github.com/pshihn/rough/blob/master/LICENSE) (c) [Preet Shihn](https://twitter.com/preetster)

 Maintained by [Preet Shihn](https://twitter.com/preetster).

![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[< 1 min to Spreed]()