Animated line drawing in SVG - JakeArchibald.com

# Animated line drawing in SVG

  Posted 29 July 2013 using tired fingers

I like using diagrams as a way of showing information flow or browser behaviour, but large diagrams can be daunting at first glance. When I gave talks about [the Application Cache](http://www.dailymotion.com/video/xwsc3y_application-cache-by-jake-archibald_tech) and [rendering performance](http://vimeo.com/69385032) I started with a blank screen and made the diagrams appear to [draw themselves bit by bit](http://vimeo.com/69385032#t=4m15s) as I described the process. Here's how it's done:

## Paths in SVG

Paths in SVG are defined in a format that competes with regex in terms of illegibility:

<path  fill="none"  stroke="deeppink"  stroke-width="14"  stroke-miterlimit="0"  d="M11.6 269s-19.7-42.4 6.06-68.2 48.5-6.06 59.1 12.1l-3.03 28.8 209-227s45.5-21.2 60.6 1.52c15.2 22.7-3.03 47-3.03 47l-225 229s33.1-12 48.5 7.58c50 63.6-50 97-62.1 37.9"/>

I use [Inkscape](http://inkscape.org/) to create the non-human-readable bits of SVG. It's a tad clunky, but it gives you an SVG DOM view as you edit the document, rather than using its own format and only offering SVG as an export format like Adobe Illustrator.

Each part of the `d` attribute is telling the renderer to move to a particular point, start a line, draw a Bézier curve to another point, etc etc.

The prospect of animating this data so the line progressively draws is, well, terrifying. Thankfully we can cheat. Along with things like colour & width, you can make an SVG path dashed and control the offset of the dash:

<path  stroke="#000"  stroke-width="4.3"  fill="none"  d="…"  stroke-dasharray=""  stroke-dashoffset="0.00"/>

 dasharray:

 dashoffset:

`stroke-dasharray` lets you specify the length of the rendered part of the line, then the length of the gap. `stroke-dashoffset` lets you change where the dasharray starts.

Drag both sliders up to their maximum, then slowly decrease the dashoffset. Voilà, you just made the line draw! 988.01 roughly the length of the line which you can get from the DOM:

var  path  =  document.querySelector('.squiggle-container path');path.getTotalLength();  // 988.0062255859375

## Animating it

The easiest way to animate SVG is using CSS animations or transitions. The downside is it doesn't work in IE, if you want IE support you'll need to use [`requestAnimationFrame`](https://developer.mozilla.org/en-US/docs/Web/API/window.requestAnimationFrame) and update the values frame by frame with script.

Avoid using SMIL, it also [isn't supported in IE](http://caniuse.com/#feat=svg-smil) and doesn't perform well in Chrome & Safari (I'll do a separate post on this).

I'm going to use CSS transitions, so the demos won't work in IE. Unfortunately I couldn't come up with a solid feature detect for transitions on SVG elements, IE has all the properties, it just doesn't work.

In the first example I used SVG attributes to define the dash, but you can do the same thing in CSS. Most [SVG presentational attributes have identical CSS properties](http://www.w3.org/TR/SVG/styling.html).

var  path  =  document.querySelector('.squiggle-animated path');var  length  =  path.getTotalLength();// Clear any previous transitionpath.style.transition  =  path.style.WebkitTransition  =  'none';// Set up the starting positionspath.style.strokeDasharray  =  length  +  ' '  +  length;path.style.strokeDashoffset  =  length;// Trigger a layout so styles are calculated & the browser// picks up the starting position before animatingpath.getBoundingClientRect();// Define our transitionpath.style.transition  =  path.style.WebkitTransition  =  'stroke-dashoffset 2s ease-in-out';// Go!path.style.strokeDashoffset  =  '0';

Using `getBoundingClientRect` to trigger layout is a bit of a hack, but it works. Unfortunately, if you modify a style twice in the same JavaScript execution without forcing a synchronous layout inbetween, only the last one counts. I wrote about this issue in more detail & how the Web Animations API will save the day over at [Smashing Magazine](http://coding.smashingmagazine.com/2013/03/04/animating-web-gonna-need-bigger-api/).

I usually trigger a layout by accessing `offsetWidth`, but that doesn't appear to work on SVG elements in Firefox.

## More fun with dashes

[Lea Verou](http://lea.verou.me/) used a similar technique to [create a loading spinner](http://dabblet.com/gist/6089395) similar to Chrome's. [Josh Matz](https://twitter.com/joshmatz) and [El Yosh](https://twitter.com/El_Yosh) expanded on this to create [this funky cube animation](http://dabblet.com/gist/6089409).

So far we've been using `stroke-dasharray` to create a bit of line followed by a gap, but you can create more complex patterns by adding more numbers. For instance, here's Justin Bieber's autograph, where the line is morse code for "Christ our saviour":

## Further reading

- [`visibility: visible` undoes a parent element's `visibility: hidden`](https://jakearchibald.com/2014/visible-undoes-hidden/)
- [Don't use flexbox for overall page layout](https://jakearchibald.com/2014/dont-use-flexbox-for-page-layout/)