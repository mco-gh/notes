mdaines/viz.js

###    README.md

# [(L)](https://github.com/mdaines/viz.js#vizjs)Viz.js

This project is a Makefile for building [Graphviz](http://www.graphviz.org/) with [Emscripten](http://kripken.github.io/emscripten-site/) and a simple wrapper for using it in the browser.

## [(L)](https://github.com/mdaines/viz.js#become-a-patron)Become a Patron

Help make Viz.js better by [supporting me on Patreon](https://patreon.com/mdaines). Thank you!

## [(L)](https://github.com/mdaines/viz.js#getting-vizjs)Getting Viz.js

Install with Bower:

	normalbower install viz.js
	normal

Or with npm:

	normalnpm install viz.js
	normal

Or download the ` viz.js ` "binary" from the [releases page](https://github.com/mdaines/viz.js/releases).

## [(L)](https://github.com/mdaines/viz.js#lite-version)"Lite" Version

A smaller version of Viz.js can be downloaded from the [releases page](https://github.com/mdaines/viz.js/releases) and is available in the Bower package. ` viz-lite.js ` omits Expat and the NEATO layout plugin.

## [(L)](https://github.com/mdaines/viz.js#api)API

### [(L)](https://github.com/mdaines/viz.js#vizsrc-options-formatsvg-enginedot-scale-totalmemory16777216-)Viz(src, options={ format="svg", engine="dot", scale, totalMemory=16777216 })

- ` src ` is a string representing the graph to render in the [DOT language](http://www.graphviz.org/content/dot-language).
- ` options `
    - ` format ` sets the output format, and may be one of ` "svg" `, ` "xdot" `, ` "plain" `, ` "ps" `, ` "json" `, or ` "png-image-element" `.
    - ` engine ` sets the Graphviz engine to use, and may be one of ` "circo" `, ` "dot" `, ` "neato" `, ` "osage" `, or ` "twopi" `.
    - ` scale ` sets the scale factor for the ` "png-image-element" ` format. If this is not specified, ` window.devicePixelRatio ` will be used if available, and ` 1 ` if not.
    - ` totalMemory ` sets the total memory available for the Emscripten module instance. This should be a power of 2. The default of 16MB should be sufficient for most cases — only consider using a larger number if you run into the error "Cannot enlarge memory arrays".

Parses ` src ` and renders a graph according to the ` options ` given. Output is a string, except when using the "png-image-element" format, when it is returned as an instance of HTMLImageElement.

For example:

	normalresult = Viz("digraph { a -> b; }");
	result = Viz("digraph { a -> b; }", { format: "png-image-element", scale: 2 });
	result = Viz("graph { n0 -- n1 -- n2 -- n3 -- n0; }", { engine: "neato" });
	result = Viz("digraph { x -> y -> z; }", { format: "plain" });
	normal

If Graphviz encounters an error, Viz will throw an ` Error ` object with the error message.

### [(L)](https://github.com/mdaines/viz.js#vizsvgxmltopngimageelementsvgxml-scale-callback)Viz.svgXmlToPngImageElement(svgXml[, scale[, callback]])

- ` svgXml ` is an SVG XML string, as may be obtained from the ` Viz ` function using the ` "svg" ` format option.
- ` scale ` sets the scale factor for the output. If this is not specified, ` window.devicePixelRatio ` will be used if available, and ` 1 ` if not.
- ` callback ` is an optional Node-style callback. If specified, it is given two arguments, ` (err, image) `. If not specified, ` Viz.svgXmlToPngImageElement ` returns an instance of HTMLImageElement.

Converts ` svgXml ` to a PNG HTMLImageElement. If ` callback ` is specfied, ` image ` is loaded by the time the callback is invoked.

### [(L)](https://github.com/mdaines/viz.js#vizsvgxmltopngbase64svgxml-scale-callback)Viz.svgXmlToPngBase64(svgXml, scale, callback)

- ` svgXml ` is an SVG XML string, as may be obtained from the ` Viz ` function using the ` "svg" ` format option.
- ` scale ` sets the scale factor for the output. If this is given as ` undefined `, ` window.devicePixelRatio ` will be used if available, and ` 1 ` if not.
- ` callback ` is a Node-style callback. It is given two arguments, ` (err, data) `.

Converts ` svgXml ` to a PNG represented as a Base64 string. This function requires a callback, unlike ` svgXmlToPngImageElement `.

## [(L)](https://github.com/mdaines/viz.js#supported-graphviz-features)Supported Graphviz features

These engines are supported:

- circo
- dot
- fdp
- neato
- osage
- twopi

These formats are supported:

- svg
- xdot
- plain
- ps
- json

## [(L)](https://github.com/mdaines/viz.js#png-output)PNG output

Viz.js provides the ` "png-image-element" ` format in addition to the regular Graphviz formats. This returns an ` HTMLImageElement ` which can be inserted into the document.

	normalimage = Viz("digraph g { a -> b; }", { format: "png-image-element" });
	document.body.appendChild(image);
	normal

However, this won't work in a Web Worker context. In that case, ask for the ` "svg" ` format in the worker and convert using the accessory function ` Viz.svgXmlToPngImageElement ` in the window context. See tests/png.js for an example.

### [(L)](https://github.com/mdaines/viz.js#internet-explorer-support)Internet Explorer support

Internet Explorer 10 and 11 require [Fabric.js](http://fabricjs.com/) as an optional dependency for PNG output. Viz.js will look for a ` fabric ` object as a member of the global object with a ` loadSVGFromString() ` function and use that if present.

## [(L)](https://github.com/mdaines/viz.js#build)Build

To build from source, you will need to [install the Emscripten SDK](http://kripken.github.io/emscripten-site/docs/getting_started/index.html).

To download the sources and build everything:

	normalmake
	normal