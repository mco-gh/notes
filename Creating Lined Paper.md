Creating Lined Paper

# Creating Lined Paper

[![80.jpg](../_resources/fff81cb11f4d829c18a45f5c32a43732.jpg)](https://codepen.io/ceg9498/)[Emily Gagne](https://codepen.io/ceg9498/)

|[**Emily Gagne's Posts**](https://codepen.io/ceg9498/posts/published/)
Aug 13, 2019

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' data-evernote-id='294'%3e %3cpath d='M85.24 2.67C72.29-3.08 55.75 2.67 50 14.9 44.25 2 27-3.8 14.76 2.67 1.1 9.14-5.37 25 5.42 44.38 13.33 58 27 68.11 50 86.81 73.73 68.11 87.39 58 94.58 44.38c10.79-18.7 4.32-35.24-9.34-41.71z' data-evernote-id='157' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart icon-animator js-evernote-checked' data-evernote-id='296'%3e %3c/svg%3e)](https://codepen.io/ceg9498/post/creating-lined-paper#0)

## Introduction

My goal of this tutorial is to keep things as plain as possible so that it might be easier for beginning developers, and developers who may not have worked with my specific stack, to dig into quickly. Of course, feel free to use whatever technology, colors, fonts, etc. you like! That being said, let's get started.

### Contents

- [What's Needed](https://codepen.io/ceg9498/post/creating-lined-paper#whats-needed-2)
- [HTML & Some Basic CSS](https://codepen.io/ceg9498/post/creating-lined-paper#html-and-some-basic-css-3)
- [The Backgrounds](https://codepen.io/ceg9498/post/creating-lined-paper#the-backgrounds-6)
- [Adding Text](https://codepen.io/ceg9498/post/creating-lined-paper#adding-text-7)
- [BONUS: Adding Margins](https://codepen.io/ceg9498/post/creating-lined-paper#bonus-adding-margins-8)
- [Working Example](https://codepen.io/ceg9498/post/creating-lined-paper#working-example-9)

## What's Needed

Here I've included an outline of the types of code needed for this tutorial, from basic HTML elements to CSS properties to styling choices like colors and fonts.

- HTML
    - Block-level elements, such as `<div>` and `<header>`
    - Paragraph element `<p>`
    - Span elemenent `<span>`
- CSS
    - `position: relative`, along with top, right, bottom, & left.
    - `linear-gradient` & `repeating-linear-gradient`
    - `line-spacing`
- Other
    - Colors: Light Blue #9198E5, Pink (I just used the keyword `pink`), White (again, I used the keyword `white`)
    - Fonts: `cursive` for a handwritten feel or `monospace` for a typewriter feel.

## HTML & Some Basic CSS

The basic structure is two block-level elements, each with its own background `linear-gradient` and text.

### Structure

There's two ways to do this - you can either place the two block elements next to each other as sibling elements, or you can nest one inside the other. I've chosen to nest one inside the other.

 	<div class="card">

	 <header>
	  <span class="card-title">A Title</span>
	 </header>
	 <p class="card-text">Some body text</p>
	</div>

Here, the `<div>` defines the whole area of the paper, and the `<header>` defines the top margin.

### Sizing

I wanted to roughly match the dimensions of a typical index card. I chose to go with 3"x5" (about 7.5cm x 12.5cm), which I converted into pixels by multiplying by 100; 300px high and 500px wide. The header area of an index card isn't very big, so I went with 36px for that. It was all *very* scientific. The width of the `<header>` should be 100%, but as a block-level element, it will do this by default. So now our CSS should look like this:

 	.card {

	 width: 500px;
	 height: 300px;
	}
	header {
	 height: 36px;
	}

## The Backgrounds

Okay, now we have a couple of elements that are positioned and sized properly, but they have no background. Let's fix that.

For the `<header>`, I used `linear-gradient()` with white and pink, utilizing the color stops feature to manipulate the gradient into defined lines.

> Side Note: For the header, you could *> absolutely*>  specify something like `{ border-bottom: 2px solid pink }`>  instead of using a gradient. However, I chose to use the gradient because it allowed me to create an effect similar to ink bleed.

 	header {

	 height: 36px;
	 background: linear-gradient(
	  white, white 33px,
	  pink 35px, pink 36px);
	}

This code starts `white` at 0px (unspecified) and ends it at 33px. It then starts `pink` at 35px and ends it at 36px, which matches the height of my header. Between the two colors, there's a gap of 2px, which produces a slight white-to-pink gradient. This is my ink bleed effect.

Next, the background for `.card` should have a bunch of horizontal blue lines. `border-bottom` won't work here like it would on the header, and while you *could* write `linear-gradient()` to specify each line, that's a huge, frustrating waste of time! Instead, we'll use `repeating-linear-gradient()`, which works the same way but allows us to specify one section and then the CSS figures out the rest for us. Here's what mine looks like:

 	.card {

	 background: repeating-linear-gradient(
	  white, white 25px,
	  #9198e5 26px, #9198e5 27px
	 );
	}

This should look familiar, as it's almost exactly the same as what I used for `<header>`'s pink line. Note, however, that the white area isn't as high, and that the blue line has less bleed effect and therefore appears thinner (1px each instead of 2px bleed and 1px line). The white areas in the lined area are supposed to be shorter, and the lines less bold.

> Caution! A problem I encountered here was getting my first blue line to start an appropriate distance away from the pink line. My solution at the time was to play around with the spacing on my blue lines until I found something that looked good, but as I was writing this I suddenly remembered that `background-position`>  exists. So if you like the spacing on your blue lines, but the white gap between your pink and first blue line doesn't look good, you can use `background-position-y`>  to set it to start after your header area (set it to the height of the header). Time to take a short break and revise my code!

## Adding Text

When I first came up with the idea to create an index card display for text, adding the text is the part that both excited and scared me. I was excited because, if I could get it right, it would look *so cool!* But I was scared of it because I wasn't sure *how* to make it work. I'm certain there are other ways of doing it, but here's what I did; turns out it's pretty easy.

1. Added `position: relative` to `.card-title` and `.card-text`. These are the two items that will contain text, and we use the positioning to place them on the lines.

2. On `.card-title` I also set `top: 5px` and `left: 10px`. The `left` property could be replaced with a margin or padding property; using positioning isn't important. However, setting `top` to 5 pixels moves it down enough to sit right on that pink line without changing how the card looks.

3. On `.card-text` I had to add quite a few properties, so here's the whole block:

 	.card-text {

	 position: relative;
	 top: 30px;
	 font-size: 18px;
	 margin: 0 20px;
	 line-height: 27px;
	}

The real key to making all of this work is `line-height`: set it to match the height of your repeating gradient (for me, it was 27px), and the lines of text will have the same spacing as your blue lines do. In addition, you may need to play around with the value for `top`: I set it to 30px so my text would start on the second blue line. If you want it to start on the first blue line you'll have to set it to 3px, and if you changed the spacing entirely you'll have to tweak it until it's right.

You'll probably want your `font-size` to be smaller than the white area on your gradient, but not too much smaller or it might look strange.

The margin here could also be accomplished with padding, but keep in mind that `<p>` has a top-margin by default, which will change your `top` value.

## BONUS: Adding Margins

I've also included an example of how a loose-leaf sheet (lined paper with margins and punched holes) might be created, and I have here a few notes on the changes that I made.

- Sizes everywhere were changed, because the ratio of the paper is different and the size of the header is different.
- The structure of the HTML changes a little bit to include two more `<div>` elements for the margins.
    - I put these before the header in my structure.
    - On this type of paper, the margins are designated by pink lines, so I added a pink border to the inner edge of each `<div>`.
    - `float: left` and `float: right` allow them to sit next to the `<header>` and `<p>` without conflicting, but also mean I had to adjust the padding/margin property of `.sheet-title` and `.sheet-text` to account for that.
    - I also had to specify a width for `.sheet-text` so that it wouldn't interfere with my right margin.
- The first line on a sheet of this paper is usually blue rather than pink, so I changed the color used for `<header>`'s background gradient.
- Within the left margin `<div>` I included three more, which represent punched holes.
    - `background-color: #555` matches my body background
    - `height: 20px; width: 20px; border-radius: 50%` makes them 20px circles.
    - Each hole has `position: absolute` and `.l-margin` got `position: relative` added so that I could position each of them properly.

## Working Example

##### Edited August 20, 2019

@Oznog commented to point out a mistake I made, where I used IDs instead of classes. The edits to the post and example pen include:

- Changed #card to .card (id to class)
- Changed #title to .card-title and .sheet-title; also changed #text to .card-text and .sheet-text (generic id to specific class)

Anyone who wants to make something similar is, of course, free to use IDs or Classes as fits their needs.

Thanks for pointing it out!

* * *

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' data-evernote-id='464'%3e %3c/svg%3e)![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart icon-animator js-evernote-checked' data-evernote-id='466'%3e %3c/svg%3e)](https://codepen.io/ceg9498/post/creating-lined-paper#0)

1,908![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-eye js-evernote-checked' data-evernote-id='470'%3e %3cpath d='M15.3 0C8.9 0 3.3 3.3 0 8.3c3.3 5 8.9 8.3 15.3 8.3s12-3.3 15.3-8.3C27.3 3.3 21.7 0 15.3 0zm0 14.5c-3.4 0-6.2-2.8-6.2-6.2C9 4.8 11.8 2 15.3 2c3.4 0 6.2 2.8 6.2 6.2 0 3.5-2.8 6.3-6.2 6.3z' data-evernote-id='87' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)4![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-comment js-evernote-checked' data-evernote-id='473'%3e %3cpath d='M-391 291.4c0 1.5 1.2 1.7 1.9 1.2 1.8-1.6 15.9-14.6 15.9-14.6h19.3c3.8 0 4.4-.8 4.4-4.5v-31.1c0-3.7-.8-4.5-4.4-4.5h-47.4c-3.6 0-4.4.9-4.4 4.5v31.1c0 3.7.7 4.4 4.4 4.4h10.4v13.5z' data-evernote-id='68' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)74![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' data-evernote-id='477'%3e %3c/svg%3e)

[Comments](https://codepen.io/ceg9498/post/creating-lined-paper#post-comments)[Tags](https://codepen.io/ceg9498/post/creating-lined-paper#post-tags)[Lovers](https://codepen.io/ceg9498/post/creating-lined-paper#lovers)

1.

[![user-avatar-80x80-bdcd44a3bfb9a5fd01eb8b86f9e033fa1a9897c3a15b33adfc2649a002dab1b6.png](../_resources/1d311346ccfe0b8d209058de77807afd.png)](https://codepen.io/dbutchy)

[Dave Butchy](https://codepen.io/dbutchy)(@dbutchy)on[August 20, 2019](https://codepen.io/ceg9498/post/creating-lined-paper#comment-id-220255)

Thanks! - particularly for explaining the CSS.

[1Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='509'%3e %3c/svg%3e)]()

2.
[![80.jpg](../_resources/e3b58fc754667002ceec34367e7d2f06.jpg)](https://codepen.io/Oznog)

[Oznog](https://codepen.io/Oznog)(@Oznog)on[August 20, 2019](https://codepen.io/ceg9498/post/creating-lined-paper#comment-id-220261)

Coll Emily, but two identical id in the same page is an error. It would be necessary to add a class and two different IDs. Otherwise we are limited to one card per page...

Thanks!

[1Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='530'%3e %3c/svg%3e)]()

3.
[![80.jpg](../_resources/fff81cb11f4d829c18a45f5c32a43732.jpg)](https://codepen.io/ceg9498)

[Emily Gagne](https://codepen.io/ceg9498)(@ceg9498)on[August 20, 2019](https://codepen.io/ceg9498/post/creating-lined-paper#comment-id-220283)

[@Oznog](https://codepen.io/Oznog) Thanks so much for pointing that out! When I originally made this card, there was only supposed to be one card (therefore, one title and one body text) on the page, and I forgot to update it. Oops!

[Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='551'%3e %3c/svg%3e)]()

4.
[![80.jpg](../_resources/3b41a62c7bc70d158bfd54539bb6ba75.jpg)](https://codepen.io/tifcopi)

[tifcopi](https://codepen.io/tifcopi)(@tifcopi)on[August 20, 2019](https://codepen.io/ceg9498/post/creating-lined-paper#comment-id-220287)

Great explanations on each section!

[Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='571'%3e %3c/svg%3e)]()

#### Leave a Comment[Markdown](https://daringfireball.net/projects/markdown/syntax) supported.Click @usernames to add to comment.

You must be [logged in](https://codepen.io/login/) to comment.