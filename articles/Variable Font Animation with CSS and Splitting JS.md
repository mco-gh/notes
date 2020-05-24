Variable Font Animation with CSS and Splitting JS

- [css](https://css-irl.info/tags/css/)
- [animation](https://css-irl.info/tags/animation/)
- [typography](https://css-irl.info/tags/typography/)
- [javascript](https://css-irl.info/tags/javascript/)

# Variable Font Animation with CSS and Splitting JS

13 August, 2019

A little while ago I made an animated variable font demo on [Codepen](https://codepen.io/michellebarker/pen/bPEWGK). In this article I’ll explain what variable fonts are, how they can be animated with CSS, and how I created a breathing effect with CSS and a little bit of Javascript.

- [HTML](https://codepen.io/michellebarker/embed/bPEWGK/?height=391&theme-id=0&default-tab=result#html-box)
- [CSS](https://codepen.io/michellebarker/embed/bPEWGK/?height=391&theme-id=0&default-tab=result#css-box)
- [JS](https://codepen.io/michellebarker/embed/bPEWGK/?height=391&theme-id=0&default-tab=result#js-box)
- [Result](https://codepen.io/michellebarker/embed/bPEWGK/?height=391&theme-id=0&default-tab=result#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/michellebarker/pen/bPEWGK)

# BBBrrreeeaaattthhhiiinnnggg

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

## Introducing variable fonts

Variable fonts are exciting new development in web typography. Instead of multiple font files to load different variants of a particular font, variable fonts allow us to load all of the variations from a single file. In most cases this is a big performance win (although the file tends to be larger than a regular font file on its own, so it’s best to only use a variable font if you actually need it).

### One font, many variations

Instead of a handful of font weights that are only available in multiples of 100 (e.g. `font-weight: 600`), variable fonts provide a range of values, all from a single file. The weight can be varied anywhere within that range. So `font-weight: 372` is perfectly valid!

### Axes of variation

Weight is just one of the [axes of variation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#Introducing_the_'variation_axis') (although probably the most common one). Variable fonts can come with different axes too. There are a number of [registered axes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#Registered_axes_and_existing_CSS_attributes), which correspond to a four-letter tag:

- weight (`wght`)
- width (`wdth`)
- italic (`ital`)
- slant (`slnt`)
- optical size (`opsz`)

These correspond to CSS properties and values:

- `font-weight`
- `font-stretch`
- `font-style`
- `font-style`
- `font-optical-sizing`

Not all variable fonts contain all of these axes of variation. Many contain just one or two.

They can also be accessed using the `font-variation-settings` property. This property enables us to not only adjust the standard axes, but custom axes as well. So `font-weight` could be specified in two ways:

`font-weight: 372;`
or
`font-variation-settings: 'wght' 372;`

We could use `font-weight` to provide a fallback for browsers that do not support variable fonts.

## Custom axes

Custom axes provide the type designer with infinite scope for creativity! A custom axis of variation could be literally anything – some, like *x-height*, might be fairly common for a typeface, but there are many more creative possibilities.

Custom axes can be accessed with the `font-variation-settings` property but, unline standard axes, their four-letter tag name must be uppercase. The variable font [Movement](http://www.nmtype.com/movement) by NM Type provides a custom axis called *space*, which controls the curvture of the letterforms.

`font-variation-settings: 'wght' 200, 'SPAC' 118;`
Try playing around with the different axes in this demo:

- [HTML](https://codepen.io/michellebarker/embed/xxKGyvd/?height=360&theme-id=0&default-tab=result#html-box)
- [CSS](https://codepen.io/michellebarker/embed/xxKGyvd/?height=360&theme-id=0&default-tab=result#css-box)
- [Result](https://codepen.io/michellebarker/embed/xxKGyvd/?height=360&theme-id=0&default-tab=result#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='13' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='36' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/michellebarker/pen/xxKGyvd)

# Oh hello there

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

## Animating a variable font with CSS

`font-variation-settings` is animatable, and because it covers a range of values rather than increments of 100, we can get some really nice effects with simple CSS transitions or keyframe animations. The font *IBM Plex Sans* has two axes of variation: weight and width. The following code sets a 1s looping animation of both axes:

	h1 {
		font-variation-settings: 'wght' 100, 'wdth' 85;
		animation: breathe 4000ms infinite forwards;
	}

	@keyframes breathe {
		60% {
			font-variation-settings: 'wght' 700, 'wdth' 100;
		}

		100% {
			font-variation-settings: 'wght' 100, 'wdth' 85;
		}
	}

This gives the effect of our text breathing in and out!

- [HTML](https://codepen.io/michellebarker/embed/rExyEE/?height=370&theme-id=0&default-tab=result#html-box)
- [CSS](https://codepen.io/michellebarker/embed/rExyEE/?height=370&theme-id=0&default-tab=result#css-box)
- [Result](https://codepen.io/michellebarker/embed/rExyEE/?height=370&theme-id=0&default-tab=result#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='13' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='36' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/michellebarker/pen/rExyEE)

# Breathing

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

Alternatively, this could be a nice hover effect with a transition instead of an animation.

## Staggering the animation

Instead of our entire text animating at the same rate, it might be nice to have our letterforms animate in sequence. We *could* wrap each letter of our text in a `<span>` and set a `animation-delay` on each one:

	<h1>
		<span>B</span>
		<span>r</span>
		<span>e</span>
		<span>a</span>
		<span>t</span>
		<span>h</span>
		<span>i</span>
		<span>n</span>
		<span>g</span>
	</h1>
	h1 span:nth-child(2) {
		animation-delay: 400ms;
	}

	h1 span:nth-child(3) {
		animation-delay: 800ms;
	}

	h1 span:nth-child(4) {
		animation-delay: 1200ms;
	}
	/* etc...*/

This would be a bit laborious to write (although we could use Sass to help us), and it wouldn’t be very maintainable if we decided to change our text content at a later date.

But if we don’t mind using just a little bit of Javascript, there’s a great library called [Splitting.js](https://splitting.js.org/) that is perfect for this!

## Splitting

Splitting’s primary use case is for animating text, although it’s also possible to split grids and layouts for some cool effects. To use it we need to include the library in our project, then set a `data-splitting` attribute on the element we’d like to animate:

`<h1 data-splitting>Breathing</h1>`
Now the JS we need to write is very simple:
`Splitting()`

Splitting then splits our text element into a series of `<span>`s, each with a class, a data-attribute and a custom property definition with a value of the character index, which we can then access in our CSS:

	<span class="word" data-word="Breathing" style="--word-index:0;">
		<span class="char" data-char="B" style="--char-index:0;">B</span>
		<span class="char" data-char="r" style="--char-index:1;">r</span>
		<span class="char" data-char="e" style="--char-index:2;">e</span>
		<span class="char" data-char="a" style="--char-index:3;">a</span>
		<span class="char" data-char="t" style="--char-index:4;">t</span>
		<span class="char" data-char="h" style="--char-index:5;">h</span>
		<span class="char" data-char="i" style="--char-index:6;">i</span>
		<span class="char" data-char="n" style="--char-index:7;">n</span>
		<span class="char" data-char="g" style="--char-index:8;">g</span>
	</span>

In order to create a sequential animation, we can use `calc()` to calculate the `animation-delay` value for each letter from the custom property:

	h1 .char {
		--delay: calc((var(--char-index) + 1) * 400ms);
		animation: breathe 4000ms infinite both;
		animation-delay: var(--delay);
	}

That massively cuts down on the CSS we need to write, and means that we could change the text later on and still have our animation work perfectly!

## Resources

### [MDN’s Variable Fonts Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#Variable_Fonts_what_they_are_and_how_they_differ)

MDN’s guide is a great resource for learning about variable fonts and how to use them

### [V-Fonts](https://v-fonts.com/)

V-Fonts is a listing of hundreds of variable fonts, including their variations axes and where to find them. It includes a mixture of paid and free/open source fonts, and is a great place to find samples for using in demos if you don’t want to fork out big bucks just yet.

### [Axis-Praxis](https://www.axis-praxis.org/)

Axis-Praxis is a playground for experimenting with variable fonts and understanding some of the creative possibilities. It includes some really interesting and creative samples!

### [VariableFonts.dev](https://variablefonts.dev/)

Variablefonts.dev is a project by [Mandy Michael](https://twitter.com/mandy_kerr), who is well-known in the CSS world for creating awe-inspiring demos with variable fonts and speaking about them all over the world.