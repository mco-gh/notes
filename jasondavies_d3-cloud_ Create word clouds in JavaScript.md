jasondavies/d3-cloud: Create word clouds in JavaScript.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='115'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='901' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jasondavies/d3-cloud#word-cloud-layout)Word Cloud Layout

This is a [Wordle](http://www.wordle.net/)-inspired word cloud layout written in JavaScript. It uses HTML5 canvas and sprite masks to achieve near-interactive speeds.

See [here](http://www.jasondavies.com/wordcloud/) for an interactive demonstration along with implementation details.

[![687474703a2f2f7777772e6a61736f6e6461766965732e636f6d2f776f7264636c6f75642f616d617a696e672e706e67](../_resources/a698abe2c9e478b258460e6f273a63b4.png)](https://camo.githubusercontent.com/46d82c30560862777d6eef9d32c6d7f79a4dd934/687474703a2f2f7777772e6a61736f6e6461766965732e636f6d2f776f7264636c6f75642f616d617a696e672e706e67)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='116'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='906' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jasondavies/d3-cloud#usage)Usage

See the samples in `examples/`.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='117'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='909' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jasondavies/d3-cloud#api-reference)API Reference

[#](https://github.com/jasondavies/d3-cloud#cloud) d3.layout.**cloud**()
Constructs a new cloud layout instance.
[#](https://github.com/jasondavies/d3-cloud#on)  **on**(*type*, *listener*)

Registers the specified *listener* to receive events of the specified *type*from the layout. Currently, only "word" and "end" events are supported.

A "word" event is dispatched every time a word is successfully placed. Registered listeners are called with a single argument: the word object that has been placed.

An "end" event is dispatched when the layout has finished attempting to place all words. Registered listeners are called with two arguments: an array of the word objects that were successfully placed, and a *bounds* object of the form`[{x0, y0}, {x1, y1}]` representing the extent of the placed objects.

[#](https://github.com/jasondavies/d3-cloud#start)  **start**()

Starts the layout algorithm. This initialises various attributes on the word objects, and attempts to place each word, starting with the largest word. Starting with the centre of the rectangular area, each word is tested for collisions with all previously-placed words. If a collision is found, it tries to place the word in a new position along the spiral.

**Note:** if a word cannot be placed in any of the positions attempted along the spiral, it is **not included** in the final word layout. This may be addressed in a future release.

[#](https://github.com/jasondavies/d3-cloud#stop)  **stop**()
Stops the layout algorithm.

[#](https://github.com/jasondavies/d3-cloud#timeInterval)  **timeInterval**([*time*])

Internally, the layout uses `setInterval` to avoid locking up the browser’s event loop. If specified, **time** is the maximum amount of time that can be spent during the current timestep. If not specified, returns the current maximum time interval, which defaults to `Infinity`.

[#](https://github.com/jasondavies/d3-cloud#words)  **words**([*words*])

If specified, sets the **words** array. If not specified, returns the current words array, which defaults to `[]`.

[#](https://github.com/jasondavies/d3-cloud#size)  **size**([*size*])

If specified, sets the rectangular `[width, height]` of the layout. If not specified, returns the current size, which defaults to `[1, 1]`.

[#](https://github.com/jasondavies/d3-cloud#font)  **font**([*font*])

If specified, sets the **font** accessor function, which indicates the font face for each word. If not specified, returns the current font accessor function, which defaults to `"serif"`. A constant may be specified instead of a function.

[#](https://github.com/jasondavies/d3-cloud#fontStyle)  **fontStyle**([*fontStyle*])

If specified, sets the **fontStyle** accessor function, which indicates the font style for each word. If not specified, returns the current fontStyle accessor function, which defaults to `"normal"`. A constant may be specified instead of a function.

[#](https://github.com/jasondavies/d3-cloud#fontWeight)  **fontWeight**([*fontWeight*])

If specified, sets the **fontWeight** accessor function, which indicates the font weight for each word. If not specified, returns the current fontWeight accessor function, which defaults to `"normal"`. A constant may be specified instead of a function.

[#](https://github.com/jasondavies/d3-cloud#fontSize)  **fontSize**([*fontSize*])

If specified, sets the **fontSize** accessor function, which indicates the numerical font size for each word. If not specified, returns the current fontSize accessor function, which defaults to:

function(d) { return  Math.sqrt(d.value); }
A constant may be specified instead of a function.
[#](https://github.com/jasondavies/d3-cloud#rotate)  **rotate**([*rotate*])

If specified, sets the **rotate** accessor function, which indicates the rotation angle (in degrees) for each word. If not specified, returns the current rotate accessor function, which defaults to:

function() { return (~~(Math.random() *  6) -  3) *  30; }
A constant may be specified instead of a function.
[#](https://github.com/jasondavies/d3-cloud#text)  **text**([*text*])

If specified, sets the **text** accessor function, which indicates the text for each word. If not specified, returns the current text accessor function, which defaults to:

function(d) { return  d.text; }
A constant may be specified instead of a function.
[#](https://github.com/jasondavies/d3-cloud#spiral)  **spiral**([*spiral*])

If specified, sets the current type of spiral used for positioning words. This can either be one of the two built-in spirals, "archimedean" and "rectangular", or an arbitrary spiral generator can be used, of the following form:

// size is the [width, height] array specified in cloud.sizefunction(size) { // t indicates the current step along the spiral; it may monotonically  // increase or decrease indicating clockwise or counterclockwise motion.  return  function(t) { return [x, y]; };

}

If not specified, returns the current spiral generator, which defaults to the built-in "archimedean" spiral.

[#](https://github.com/jasondavies/d3-cloud#padding)  **padding**([*padding*])

If specified, sets the **padding** accessor function, which indicates the numerical padding for each word. If not specified, returns the current padding, which defaults to 1.

[#](https://github.com/jasondavies/d3-cloud#random)  **random**([*random*])

If specified, sets the internal random number generator, used for selecting the initial position of each word, and the clockwise/counterclockwise direction of the spiral for each word. This should return a number in the range `[0, 1)`.

If not specified, returns the current random number generator, which defaults to `Math.random`.

[#](https://github.com/jasondavies/d3-cloud#canvas)  **canvas**([*canvas*])

If specified, sets the **canvas** generator function, which is used internally to draw text. If not specified, returns the current generator function, which defaults to:

function() { return  document.createElement("canvas"); }

When using Node.js, you will almost definitely override this default, e.g. using the [canvas module](https://www.npmjs.com/package/canvas).