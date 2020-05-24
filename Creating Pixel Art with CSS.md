Creating Pixel Art with CSS

#  Creating Pixel Art with CSS

###     [  [401c789b-fc72-46c9-a16f-2f0a755d8823.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)  Jacque Schrag](https://dev.to/jnschrag)    [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 612 612' role='img' aria-labelledby='anfu585oi8hvdz8rwadhtcf13vqyaej9' class='icon-img js-evernote-checked' data-evernote-id='1131'%3e%3ctitle id='anfu585oi8hvdz8rwadhtcf13vqyaej9'%3etwitter logo%3c/title%3e%3cpath d='M612 116.258c-22.525 9.98-46.694 16.75-72.088 19.772 25.93-15.527 45.777-40.155 55.184-69.41-24.322 14.378-51.17 24.82-79.775 30.48-22.906-24.438-55.49-39.66-91.63-39.66-69.333 0-125.55 56.218-125.55 125.514 0 9.828 1.11 19.427 3.25 28.606-104.325-5.24-196.834-55.223-258.75-131.174-10.822 18.51-16.98 40.078-16.98 63.1 0 43.56 22.182 81.994 55.836 104.48-20.575-.688-39.926-6.348-56.867-15.756v1.568c0 60.806 43.29 111.554 100.692 123.104-10.517 2.83-21.607 4.398-33.08 4.398-8.107 0-15.947-.803-23.634-2.333 15.985 49.907 62.336 86.2 117.253 87.194-42.946 33.655-97.098 53.656-155.915 53.656-10.134 0-20.116-.612-29.944-1.72 55.568 35.68 121.537 56.484 192.44 56.484 230.947 0 357.187-191.29 357.187-357.188l-.42-16.253C573.87 163.525 595.21 141.42 612 116.257z'%3e%3c/path%3e%3c/svg%3e)](http://twitter.com/jnschrag)  Jun 12  ・6 min read

 [#css](https://dev.to/t/css)  [#tutorial](https://dev.to/t/tutorial)  [#art](https://dev.to/t/art)  [#beginners](https://dev.to/t/beginners)

I have always enjoyed looking at and creating pixel art. Before [online pixel makers](http://pixelartmaker.com/) were a thing, I used to spend hours making my own pixel art in Photoshop with the pencil tool. This article will show you how using CSS (and a tiny bit of HTML), you can use code to make your own pixel art creations.

##   [(L)](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#the-power-of-raw-boxshadow-endraw-) The Power of `box-shadow`

While it is 100% possible to create pixel art by creating a bunch of `<div>`s and changing their background color, that's a lot of `<div>`s to keep track of and copy if you want to reuse your pixel in multiple places. I prefer to create pixel art with a single `<div>`, which we can do thanks to the `box-shadow` property.

`box-shadow` is commonly used to create a drop shadow effect behind an element, like in the example below.

- [HTML](https://codepen.io/jschrag/embed/OYKPrM?height=600&default-tab=result&embed-version=2#html-box)
- [CSS](https://codepen.io/jschrag/embed/OYKPrM?height=600&default-tab=result&embed-version=2#css-box)
- [JS](https://codepen.io/jschrag/embed/OYKPrM?height=600&default-tab=result&embed-version=2#js-box)
- [Result](https://codepen.io/jschrag/embed/OYKPrM?height=600&default-tab=result&embed-version=2#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/jschrag/pen/OYKPrM)

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

How does that help us with creating the straight-edged pixel art? By removing the blur & spread parameters from the `box-shadow` definition, we can straighten out the sides of the shadow.

- [HTML](https://codepen.io/jschrag/embed/byXNOw?height=600&default-tab=result&embed-version=2#html-box)
- [CSS](https://codepen.io/jschrag/embed/byXNOw?height=600&default-tab=result&embed-version=2#css-box)
- [JS](https://codepen.io/jschrag/embed/byXNOw?height=600&default-tab=result&embed-version=2#js-box)
- [Result](https://codepen.io/jschrag/embed/byXNOw?height=600&default-tab=result&embed-version=2#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/jschrag/pen/byXNOw)

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

Next, we want to move the shadow so it is beside the block instead of being behind it. We can do this by adjusting the X- & Y-offset parameters according to the rules below.

**X-offset:**

- Positive value moves **right**
- Negative value moves **left**

**Y-offset:**

- Positive value moves **down**
- Negative value moves **up**

Shadows inherit their dimensions from the element they're applied to. To move the shadow to the right of the block, we need to set the X-offset to be the same as the width of the block: `20px`. If we change the Y-offset to `0`, the result looks like if we had two blocks sitting side-by-side.

- [HTML](https://codepen.io/jschrag/embed/byXNzw?height=600&default-tab=result&embed-version=2#html-box)
- [CSS](https://codepen.io/jschrag/embed/byXNzw?height=600&default-tab=result&embed-version=2#css-box)
- [JS](https://codepen.io/jschrag/embed/byXNzw?height=600&default-tab=result&embed-version=2#js-box)
- [Result](https://codepen.io/jschrag/embed/byXNzw?height=600&default-tab=result&embed-version=2#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/jschrag/pen/byXNzw)

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

It's starting to look like pixel art! But this only gives us two "pixels", and we're going to need a lot more than that. Thankfully, the `box-shadow` property isn't limited to just one effect. By separating our effects with a comma, we can create multiple pixel-looking shadows.

- [HTML](https://codepen.io/jschrag/embed/wbVaNy?height=600&default-tab=result&embed-version=2#html-box)
- [CSS](https://codepen.io/jschrag/embed/wbVaNy?height=600&default-tab=result&embed-version=2#css-box)
- [JS](https://codepen.io/jschrag/embed/wbVaNy?height=600&default-tab=result&embed-version=2#js-box)
- [Result](https://codepen.io/jschrag/embed/wbVaNy?height=600&default-tab=result&embed-version=2#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/jschrag/pen/wbVaNy)

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

Now that we know how we can use `box-shadow`, it's time to start making a real piece of pixel art.

##   [(L)](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#creating-a-pixel-cat) Creating a Pixel Cat

We're going to be creating a pixel version of Pusheen. If you're new to making pixel art, I recommend searching for existing art so you have a reference for where your pixels should be placed. I'm going to be recreating this version of pixel Pusheen.

[[199923bd-7afb-466a-92b9-c40c4ea941fe.webp](../_resources/bf4553aa8675a7d709faa3d11d71d624.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--poEcgs-b--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/64f3j9evqdoitxo9otol.png)

It is made up of 414 pixels (23 columns x 18 rows). To help me easily identify the individual pixels, I've used Photoshop to overlay a grid on the reference image.

[![w7abxzf9exyg0iultylq.png](../_resources/6387ff6d8cae6bf75c38a5a70185d285.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--JJnKg24y--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/w7abxzf9exyg0iultylq.png)

Although you could start drawing your pixel from anywhere, I'm going to start in the uppermost left corner so I don't have to worry about any negative offsets in my `box-shadow` effects.

I'm also going to use SASS instead of vanilla CSS to avoid writing 414 `box-shadow` declarations by hand. By utilizing a custom SASS function and lists, we can automate calculating the offset positions and make our code more DRY.

First, I’m going to make some modifications to our `#cat` block. Instead of applying the `box-shadow` to the block itself, I’m going to apply it to a pseudo element instead that is absolutely positioned relative to the block. Why? Because `box-shadow` doesn’t take up space, meaning if I were to put another element next to my cat block, it would sit on top of my shadows. If we make the size of the cat block the final size of our pixel art, we can avoid this problem, but we need the pseudo element to separately define the width/height of our pixels (remember, the size of the shadow is inherited from the element the box-shadow is applied to). This is what those changes look like:

	#cat {
	  position: relative;
	  width: calc(23 * #{$size}); // Pixel size * # of columns
	  height: calc(18 * #{$size}); // Pixel size * # of rows
	  margin: 1rem;

	  &::after {
	    content: '';
	    position: absolute;
	    top: 0;
	    left: 0;
	    width: $size;
	    height: $size;
	    // box-shadow will be applied here
	  }
	}

Next, let’s set up some variables.

	// The width/height of each of our "pixels".
	$size: 20px;

	// Colors
	$t: transparent;
	$black: #000;
	$gray: #cdc9cf;
	$dkgray: #a09da1;
	$pink: #ffa6ed;

Now we’re going to create a list to track what color each pixel should be. Starting on the left, let’s create a list for the first row.

	$first: ($t, $t, $t, $black, $t, $t, $t, $t, $black);

We could create new variables for each of the subsequent rows (`$second`, `$third`, etc.), but a better approach is to create a nested list, like so:

	$cat: (
	  ($t, $t, $t, $black, $t, $t, $t, $t, $black),// 1st Row
	  ($t, $t, $black, $gray, $black, $t, $t, $t, $t, $black, $gray, $black)// 2nd Row
	  // Additional rows
	);

The nested list approach has the benefit of providing us with all the information we need to generate our `box-shadow` effect for each of the cell: the X/Y positions to calculate our offset and the color of the shadow. We'll access that information with a custom "pixelize" function.

###   [(L)](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#writing-a-sass-function-to-draw-a-pixel) Writing a SASS Function to Draw a Pixel

Our "pixelize" function is going to do the heavy-lifting of turning our list of colors into usable `box-shadow` definitions. I've provided line-by-line explanations of what this function does below.

	@function pixelize($colors, $size) {
	  $result: '';
	  $numRows: length($colors);

	  @for $rowIndex from 1 through $numRows {
	    $y: ($rowIndex - 1);
	    $row: nth($colors, $rowIndex);
	    $numCols: length($row);

	    @for $cellIndex from 1 through $numCols {
	      $x: ($cellIndex - 1);
	      $color: nth($row, $cellIndex);

	      $sep: ', ';
	      @if $x == 0 and $y == 0 {
	        $sep: '';
	      }

	      $result: $result + '#{$sep}#{$x * $size} #{$y * $size} #{$color}'
	    }
	  }

	  $result: unquote($result);
	  @return $result;
	}

- Line 1: The function takes two arguments: the list of `$colors` and the `$size` that the pixels should be
- Line 2: Initializes our `$result` variable as a string. This is the variable the function will modify and return.
- Line 3: Returns the number of rows in the list using the built-in `length` function
- Line 5: Starts a loop that iterates X times, where X is the number of rows in our list. The `$rowIndex` will increment by 1 on each loop.
- Line 6: Calculates the Y-offset of all cells in that row. SASS Lists are index-1 (not index-0), so we subtract 1 from the current index so the 1st row has a Y-offset of 0, 2nd has Y-offset of 1, etc.
- Lines 7 & 8: Returns the value of the current list item (the list of colors for the row) & calculates its length to determine the number of columns in the row
- Line 10: Starts a loop to iterate over each column in the row
- Line 11 & 12: Calculates the X-offset of that cell & returns the corresponding color
- Lines 14-17: Sets the separator for the `box-shadow` effects, but removes it for the first cell to ensure a valid property value.
- Line 19: Updates the `$result` value to its existing value plus the new cell:
    - Separator
    - X position * `$size` = X-offset
    - Y position * `$size` = Y-offset
    - Color
- Line 23 & 24: `$result` is a string, so we use the `unquote` function to remove the containing quotes. Finally, return the result.

##   [(L)](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#the-final-result) The Final Result

Put it all together, and here is our final Pusheen pixel!

- [HTML](https://codepen.io/jschrag/embed/eaqpJO?height=600&default-tab=result&embed-version=2#html-box)
- [SCSS](https://codepen.io/jschrag/embed/eaqpJO?height=600&default-tab=result&embed-version=2#css-box)
- [JS](https://codepen.io/jschrag/embed/eaqpJO?height=600&default-tab=result&embed-version=2#js-box)
- [Result](https://codepen.io/jschrag/embed/eaqpJO?height=600&default-tab=result&embed-version=2#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/jschrag/pen/eaqpJO)

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

Pretty neat! With a little refactoring, the use of CSS Variables, & a smidge of JavaScript, we could even allow users to select their own colors for their cats.

I hope this post has inspired you to make your own pixel art. Even if it hasn't, I hope you've learned how you can use the `box-shadow` property to create some neat effects in your projects. If you're interested in seeing more pixel art, including examples of how to animate them, check out "[Fun Times with CSS Pixel Art](https://css-tricks.com/fun-times-css-pixel-art/)" by Geoff Graham on CSS-Tricks.

 [  [ef7358f9-e07c-423b-afdc-ce9505b22fb7.webp](../_resources/3b27fdec21f196a93dfe5903fb2a3824.webp)](https://dev.to/jnschrag)

#### [Jacque Schrag](https://dev.to/jnschrag)

I’m a web developer & data visualizer working at a think tank in D.C. I'm a self-taught dev trying to better my skills. My languages of choice are JavaScript & PHP.

 [@jnschrag](https://dev.to/jnschrag)  [  [d97dd8e5-26ef-40b9-b140-dcccbd8dc026.webp](../_resources/82fc7d7179170bd29bf81d640a6cb697.png) jnschrag](http://twitter.com/jnschrag)  [![twitter-logo-silhouette_1_letrqc.png](../_resources/b5b447835a04fca6fe7559db1f40b440.png) jacqueschrag.com](https://jacqueschrag.com/)

 [![info-77808966a58690cfaad3e8c7923a4d78d8fab5d87e1c3f73aef7670f290eb00c.png](../_resources/cc6ee306ec75fb01d87763e512604800.png)](https://dev.to/p/editor_guide)

 [(L)](https://dev.to/jnschrag/creating-pixel-art-with-css-3451)

 [![f451a206-11c8-4e3d-8936-143d0a7e65bb.png](../_resources/5c4e350d0bff761727662a75e9b0c310.jpg)     Ben Halpern](https://dev.to/ben)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/bendhalpern)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/benhalpern)

 [ Jun 12](https://dev.to/ben/comment/bm80)

Wow, I just learned so much about CSS

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm80)

 [  [b47e4ae2-83c8-4bd2-aa61-871f9602e356.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bm82)

Haha I hope it was useful information! I wondered if I was maybe going too much into the weeds, but ¯_(ツ)_/¯ It made me realize how much of this information I took for granted until it came time to write it down and I realized how many assumptions I was making about what people knew.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm82)

 [  [15162f40-18fd-4408-a59f-81627bc723d5.webp](../_resources/d9c07a6b61f6252d2e25e2bc88229f8e.webp)     john_horner](https://dev.to/john_horner1)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/john_horner1)

 [ Jun 12](https://dev.to/john_horner1/comment/bne4)

Nice! I'm not going to do the next-level thing but I'm sure someone is … write a *script* to create the SASS to create the CSS, a script which can be run on any image!

I did this a while ago, but it's the hard-grinding version of creating table cells with background colours:

[johnhorner.info/apple/](http://johnhorner.info/apple/)
I did it with Perl and ImageMagick but I bet there's a Python tool out there.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bne4)

 [  [7a06a950-5304-47f1-8256-ec54514feb44.webp](../_resources/8692492497345f465cc6d6e9f2f60a17.webp)     Ashley Sheridan](https://dev.to/ashleyjsheridan)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/AshleyJSheridan)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/AshleyJSheridan)

 [ Jun 14](https://dev.to/ashleyjsheridan/comment/bp12)

I actually did this myself with PHP as the generator: [ashleysheridan.co.uk/blog/Single+D...](http://www.ashleysheridan.co.uk/blog/Single+Div+CSS+Mona+Lisa)

Modern browsers with enough resources handled it quite well, even at a 1×1 pixel representation.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bp12)

 [![link-symbol_apfbll.png](../_resources/adc6fa109278231ff98f79875481dc2c.webp)     John Horner](https://dev.to/johnhorner)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/johnhorner)

 [ Jun 15](https://dev.to/johnhorner/comment/bppb)

Nice! I knew someone smart would have done this!
I’m on my phone right now so I can’t check your source.

- Does it optimise by re-using colours in a CLUT (colour lookup table)?
- Does it have a kind of RLE (run length encoding) where a stretch of two or more pixels the same colour are made into a single long element?

Those concepts are used to optimise the file size of GIFs. JPGs I don’t know. They’re more mysterious to me.

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bppb)

 [  [104853df-d91f-42af-a659-fa99c7b2e04f.webp](../_resources/8692492497345f465cc6d6e9f2f60a17.webp)     Ashley Sheridan](https://dev.to/ashleyjsheridan)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/AshleyJSheridan)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/AshleyJSheridan)

 [ Jun 15](https://dev.to/ashleyjsheridan/comment/c03d)

It doesn't have any optimization really, I might go back to it and update it, those are some good ideas.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c03d)

 [  [1cbe8942-4210-46b5-939b-876845976ab4.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 14](https://dev.to/jnschrag/comment/bp3n)

This is incredible! 27,000 lines of CSS for just the 4 examples on the page is nuts, although I believe it. Very cool!

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bp3n)

 [  [401c789b-fc72-46c9-a16f-2f0a755d8823.webp](../_resources/8692492497345f465cc6d6e9f2f60a17.webp)     Ashley Sheridan](https://dev.to/ashleyjsheridan)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/AshleyJSheridan)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/AshleyJSheridan)

 [ Jun 14](https://dev.to/ashleyjsheridan/comment/bpfk)

Yes, I would absolutely not recommend using the technique to the degree I pushed it! My blog post was just about seeing how far I could push it. I did do a full 1×1 example of the Mona Lisa shown there, but it was starting to slow the page down considerably, so I didn't make it part of the post. There is a link to the generator on github should you wish to try it out yourself though!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bpfk)

 [![64f3j9evqdoitxo9otol.png](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 13](https://dev.to/jnschrag/comment/bnf8)

Oh gosh all I can think is the Inception meme “we need to go deeper”. Although that would actually be really cool to be able to recreate any image via box-shadow. Although I wonder if you would hit a limit at how many box-shadow definitions you’re allowed to have before the browser can’t handle it anymore.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bnf8)

 [  [d3008a28-f31e-4a47-a099-f8e9c8bf1a98.webp](../_resources/d9c07a6b61f6252d2e25e2bc88229f8e.webp)     john_horner](https://dev.to/john_horner1)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/john_horner1)

 [ Jun 13](https://dev.to/john_horner1/comment/bnfe)

Only one way to find out!

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bnfe)

 [  [ffb162d1-4ffa-48dc-940d-7ad55ed0bd9a.webp](../_resources/fde666a79d290eacfbfc2e41786a4688.webp)     Hugh](https://dev.to/y6nh)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/y6nH)

 [ Jun 18](https://dev.to/y6nh/comment/c34o)

I tried to find that out — though these are conventional blurry shadows, not pixel art: [codepen.io/y6nH/pen/YRmVvZ](https://codepen.io/y6nH/pen/YRmVvZ) (click with shift or ctrl to add larger numbers).

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c34o)

 [  [3ed22381-b181-4def-a355-a2f5bbd487e0.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 18](https://dev.to/jnschrag/comment/c37i)

That's amazing. I stopped after 1500ish, so I didn't find the limit, but that's truly incredible just how much the browser can handle. Although I did start to notice a slow down in how quickly it rendered starting around 800ish.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c37i)

 [  [ce3b4766-9079-4428-8103-cc13e77ed22a.webp](../_resources/f3d07c8577d4a15c03615d500bcf2126.webp)     Laurie](https://dev.to/laurieontech)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/laurieontech)

 [ Jun 12](https://dev.to/laurieontech/comment/bm71)

This is so cool!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm71)

 [  [7163046a-b155-46a4-b767-2401464f1535.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bm7c)

Thank you!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm7c)

 [![704ffa56-bcf5-4450-ae6f-05c873b23fa5.jpg](../_resources/18bbb24dd7ec1bfae8dded189f5eaec2.jpg)     Clay Murray ️‍](https://dev.to/powerc9000)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/powerc9000)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/powerc9000)

 [ Jun 12](https://dev.to/powerc9000/comment/bma9)

Damn this is cool as hell. Didn't even know pseudo element could have box shadows.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bma9)

 [  [qhOHePW3.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmfd)

Yes! Another fun fact for you: the box-shadow property can be animated. Which means you can make moving pixels like this: [codepen.io/jschrag/pen/PrYrQE](https://codepen.io/jschrag/pen/PrYrQE)

But if you apply the box-shadow to a pseudo element & animate it, it actually becomes more performant in the browser. Here’s an article about that: [alligator.io/css/transition-box-sh...](https://alligator.io/css/transition-box-shadows/)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmfd)

 [  [bf05712b-fa1f-4a1d-9965-dcea210b4302.webp](../_resources/6ace4959f84fb0acdad8af6c5e981ad6.webp)     anpos231](https://dev.to/anpos231)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/anpos231)

 [ Jun 12](https://dev.to/anpos231/comment/bn5c)

From what I understand, this article is about creating an illusion of transforming box-shadow by changing it's opacity.

The problem with animating box-shadow is that it triggers repaints on every change.

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bn5c)

 [  [32f0773b-cee8-4bf6-9e71-bfbce64077a4.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bn62)

Good catch! Looks like I wasn't paying close enough attention. That said, if your animation has two states, one way to approach it would be to have two pseudo elements (`::before` for default state & `::after` for 2nd state) with `box-shadow` applied and alternate the opacity on those.

Or just make a gif. :)

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bn62)

 [![c0c013a8-7b5f-47d1-9e1b-3997106c7c81.jpeg](../_resources/26074702522ba1829694cb70a64da192.jpg)     David Wickes](https://dev.to/gypsydave5)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/gypsydave5)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/gypsydave5)

 [ Jun 12](https://dev.to/gypsydave5/comment/bncm)

> Or just make a gif. :)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bncm)

 [  [aca7d8f1-dd22-4456-a598-90ad6591de29.webp](../_resources/48d87abdd872da73f0e9be0f879c2297.webp)     willsmart](https://dev.to/willsmart)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/willsmart)

 [ Jun 19](https://dev.to/willsmart/comment/c40e)

Such a cool technique! Great post.

I noticed you're drawing a lot of transparent shadow pixels though, they're easily gotten rid of via something like:

Which might speed up rendering a bit (depending on the how many transparent pixels there are and if there are mysterious render optimisations in play).

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c40e)

 [  [05160132-486f-48c2-b996-df933a41583b.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 19](https://dev.to/jnschrag/comment/c42h)

Yes, drawing the transparent box-shadows aren't necessary, so that's a great improvement! Thanks for sharing. :D

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c42h)

 [  [eef6ca66-f468-47ef-a42b-2ef0f745235a.webp](../_resources/ba91c8a28dbfc866db67a4afacbda151.webp)     RolandCsibrei](https://dev.to/rolandcsibrei)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/RolandCsibrei)

 [ Jun 18](https://dev.to/rolandcsibrei/comment/c33h)

Cool approach even though it is incredibly insane to create pixel art with this technique. We need "crazy" developers like you to push the limits further and further. Thanks for sharing! Have a great day!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c33h)

 [  [4486bb38-e5f8-4312-8f7e-93476461d1ed.webp](../_resources/f2591e0ba26ed29b583a69c70eb41952.webp)     Colin Demaine](https://dev.to/demaine)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Demaine)

 [ Jun 13](https://dev.to/demaine/comment/bo1b)

The box-shadow technique is definitely a fun way to make pixel art with CSS. I like your approach in explaining the technique to make it simple and accessible. In comparison, my first attempt of using this technique was a bit extreme, to say the least: [codepen.io/demaine/full/rRvdJZ](https://codepen.io/demaine/full/rRvdJZ)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bo1b)

 [  [25c8c2bc-2cf5-4f7c-9a35-c5b94a9fbf7e.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 13](https://dev.to/jnschrag/comment/bo36)

I remember seeing this when you first created it! It’s so cool!! In another comment we were talking about the browser limits of using box-shadow for this kind of thing, so it’s great to see your piece and read how you addressed that issue.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bo36)

 [  [b099f6cd-8a95-4a78-9b95-1d4bce568189.webp](../_resources/126bcb7ceed6f7dd8425b6c432b6667c.webp)     Anton Istomin](https://dev.to/tailcall)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/tail-call)

 [ Jun 12](https://dev.to/tailcall/comment/bmcl)

There must be a webpack loader for that!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmcl)

 [  [108bbeb1-e521-4b02-be02-7dc8eab85d18.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmfg)

Haha I mean...there’s a webpack loader for everything else.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmfg)

 [  [d2c2dd5b-16e8-4d37-99b3-32cdcbdb9607.webp](../_resources/3ef8b602c3092e20e2374ffd1170c282.webp)     Jayme Edwards](https://dev.to/jaymeedwards)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jaymeedwards)

 [ Jun 13](https://dev.to/jaymeedwards/comment/bng2)

Super cute article (and artwork). Nice!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bng2)

 [  [e2a3dc5d-879f-4b4e-ab35-09915fd2dd2f.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 13](https://dev.to/jnschrag/comment/bo38)

Thanks! Can’t claim credit for the original artwork though, I found it online :)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bo38)

 [  [e1929696-cecb-435a-a96c-4e827810a47e.webp](../_resources/3ef8b602c3092e20e2374ffd1170c282.webp)     Jayme Edwards](https://dev.to/jaymeedwards)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jaymeedwards)

 [ Jun 13](https://dev.to/jaymeedwards/comment/bo4i)

Oops, guess I missed that. ‍♂️

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bo4i)

 [  [0fa4a5bf-93d2-4e96-92a9-d76e862b8138.webp](../_resources/fac2fa94d19a2919f4a8fcd8e551670f.webp)     Christopher Andert](https://dev.to/worksnakes)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WorkSnakes)

 [ Jun 12](https://dev.to/worksnakes/comment/bmjj)

I never thought to use box shadow multiple times on the same element. That's a nifty trick!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmjj)

 [  [7aac5bc0-feeb-4d8b-a435-5f71b1898ca2.webp](../_resources/374fb919dba45ebfc8aacded01a0951e.webp)     Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bml5)

Yeah! It's one way that you can create truly incredible CSS art like this [codepen.io/ivorjetski/pen/xMJoYO](https://codepen.io/ivorjetski/pen/xMJoYO)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bml5)

 [![ea97bb5b-928a-4f88-901a-471a1491e5e2.jpeg](../_resources/ff413e052c8b3bfa11ed56c020231be9.jpg)     Mobidi](https://dev.to/mobidi)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Mobidi)

 [ Jun 17](https://dev.to/mobidi/comment/c25b)

Really nice exercice ! Thanks, I'll try to make some :D

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c25b)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 17](https://dev.to/jnschrag/comment/c25c)

Thanks! Would love to see what you come up with! :)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c25c)

 [![ea97bb5b-928a-4f88-901a-471a1491e5e2.jpeg](../_resources/ff413e052c8b3bfa11ed56c020231be9.jpg)     Mobidi](https://dev.to/mobidi)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Mobidi)

 [ Jun 17](https://dev.to/mobidi/comment/c25g)

Oh and just changing the shape of your orignal pixel with a border radius seems to make some really cool stuff happens.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c25g)

 [   Harry McKillen](https://dev.to/harrymckillen)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/_hmck)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/harrymckillen)

 [ Jun 12](https://dev.to/harrymckillen/comment/bmo3)

I've been doing this for a little while, but without that great little pixelize function. Which I can now "borrow"!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmo3)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmpb)

Please do! Nobody should be writing that many box-shadow effects by hand

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmpb)

 [   Harry McKillen](https://dev.to/harrymckillen)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/_hmck)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/harrymckillen)

 [ Jun 13](https://dev.to/harrymckillen/comment/bo1h)

In lieu of sitting down to figure out how to break the problem apart, like a luddite, I do it! :) You've saved me a lot of time.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bo1h)

 [   Juan C. Andreu](https://dev.to/andreujuanc)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/andreujuanc)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/andreujuanc)

 [ Jun 12](https://dev.to/andreujuanc/comment/bmlo)

Is this pusheen but kitten? D:

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmlo)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmnl)

Kitten because it's small? If so, then yes!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmnl)

 [   Juan C. Andreu](https://dev.to/andreujuanc)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/andreujuanc)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/andreujuanc)

 [ Jun 12](https://dev.to/andreujuanc/comment/bmo5)

C:

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmo5)

 [   Conlin Durbin](https://dev.to/wuz)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/CallMeWuz)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/wuz)

 [ Jun 13](https://dev.to/wuz/comment/bnge)

This post is super awesome! Thanks for sharing!!!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bnge)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  Author

 [ Jun 13](https://dev.to/jnschrag/comment/bo39)

Thanks so much!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bo39)

 [   Allison Walker](https://dev.to/alliwalk)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/alliwalk)

 [ Jun 18](https://dev.to/alliwalk/comment/c3b4)

Very impressive!
BTW, the link to your github page doesn't seem to be working.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c3b4)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 18](https://dev.to/jnschrag/comment/c3c0)

Thanks!

Do you mean on my profile? If so, it's working fine for me. But if you're interested, it's [github.com/jnschrag](https://github.com/jnschrag)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c3c0)

 [   Allison Walker](https://dev.to/alliwalk)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/alliwalk)

 [ Jun 18](https://dev.to/alliwalk/comment/c3eo)

You're welcome.

Yes it goes to [jacqueschrag.com/](https://jacqueschrag.com/). I get a 404. Just FYI.

 [THREAD](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c3eo)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 18](https://dev.to/jnschrag/comment/c3h5)

Oh, you mean my personal site. Yeah, that's currently offline. :) Thanks for letting me know!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c3h5)

 [   Eric Davidson](https://dev.to/thebuffed)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/TheBuffED)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/erdavids)

 [ Jun 12](https://dev.to/thebuffed/comment/bm77)

Awesome! It's cool to get to a point technically that you can start recreating tools for your own use.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm77)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bm7b)

Thanks so much! I low-key wrote the article because I wanted to make the color switching tool at the end haha

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm7b)

 [   orlando ramirez](https://dev.to/oramirezperera)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/oramirezperera)

 [ Jun 16](https://dev.to/oramirezperera/comment/c0l9)

Hey, excellent post! really like it!.

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c0l9)

 [   Jakub Sarnowski](https://dev.to/sarneeh)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/sarneeh)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/sarneeh)

 [ Jun 18](https://dev.to/sarneeh/comment/c2o1)

This is amazing! :D Awesome work!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/c2o1)

 [   K-Sato](https://dev.to/ksato1995)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/K-Sato1995)

 [ Jun 12](https://dev.to/ksato1995/comment/bm99)

sick!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm99)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmff)

Thanks!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmff)

 [   dAVE Inden](https://dev.to/daveskull81)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/daveskull81)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/daveskull81)

 [ Jun 13](https://dev.to/daveskull81/comment/bokb)

This is awesome. A great example of the power of CSS and a preprocessor like SASS. Plus, pixel art is super cute and fun and makes for a great article topic in my opinion. Thanks for this article!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bokb)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 14](https://dev.to/jnschrag/comment/bp3k)

Thank you!! Glad you enjoyed it. :)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bp3k)

 [![54cacbee-ffe4-4db1-8796-c8307b7ab5fb.jpeg](../_resources/ba782c6bb556780282199c7399341b5c.jpg)     Celso Bessa](https://dev.to/celsobessa_90)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/celsobessa)

 [ Jun 13](https://dev.to/celsobessa_90/comment/bob5)

That is clever and neat!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bob5)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 13](https://dev.to/jnschrag/comment/bocb)

Thank you!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bocb)

 [   Unlimiter](https://dev.to/unlimiter)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Unlimiter)

 [ Jun 12](https://dev.to/unlimiter/comment/bnba)

Pretty smart. I like the idea!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bnba)

 [   anpos231](https://dev.to/anpos231)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/anpos231)

 [ Jun 12](https://dev.to/anpos231/comment/bn50)

WOW

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bn50)

 [   Rick Booth](https://dev.to/rixcy)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Rixcy)

 [ Jun 12](https://dev.to/rixcy/comment/bmpn)

So so good, I'll definitely be playing around with this when I get chance!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmpn)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bn0j)

Thanks! Would love to see any pixels you end up creating!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bn0j)

 [   Josh Vega](https://dev.to/jsvcycling)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jsvcycling)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Jsvcycling)

 [ Jun 12](https://dev.to/jsvcycling/comment/bmm3)

My mind literally just exploded with how awesome this is! Thanks for sharing!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmm3)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmnj)

Thanks so much!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmnj)

 [![0161b8ab-4d13-4fef-b5d6-03a8da31006b.jpg](../_resources/17a9a1ba24699a6f5f4cdacd224f9f86.jpg)     Steven Washington](https://dev.to/washingtonsteven)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/esaevian)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/washingtonsteven)

 [ Jun 12](https://dev.to/washingtonsteven/comment/bmkl)

This is amazing and adorable. Love it!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmkl)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bml8)

Thank you!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bml8)

 [   Lorenz ~ WebDEasy](https://dev.to/webdeasy)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebDEasy)

 [ Jun 12](https://dev.to/webdeasy/comment/bmka)

Very nice! Good work

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmka)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bml7)

Thanks so much!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bml7)

 [   Ananya Neogi](https://dev.to/ananyaneogi)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/_ananyaneogi)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/ananyaneogi)

 [ Jun 12](https://dev.to/ananyaneogi/comment/bmd6)

This is so cool!

I've always loved playing with pixel art and have spent way too much time at [Make 8-bit Art](https://make8bitart.com/)

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmd6)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmfj)

Thanks! There’s so many online tools for this it’s great. Although for whatever reason, I find using them more tedious, even though writing out the colors for all those cells wasn’t exactly quick lol

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmfj)

 [   aleBiagini](https://dev.to/alebiagini)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/aleBiagini)

 [ Jun 12](https://dev.to/alebiagini/comment/bmda)

Very Nice tut! Congratss

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmda)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmfh)

Thanks!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmfh)

 [   Meeooow](https://dev.to/jaeheonjee)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jaeheonjee)

 [ Jun 12](https://dev.to/jaeheonjee/comment/bm9p)

Funny ! really good article!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bm9p)

 [   Jacque Schrag](https://dev.to/jnschrag)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jnschrag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/jnschrag)  Author

 [ Jun 12](https://dev.to/jnschrag/comment/bmfe)

Haha thank you!!

 [REPLY](https://dev.to/jnschrag/creating-pixel-art-with-css-3451#/jnschrag/creating-pixel-art-with-css-3451/comments/new/bmfe)

 [VIEW FULL DISCUSSION (75 COMMENTS)](https://dev.to/jnschrag/creating-pixel-art-with-css-3451/comments)  [code of conduct](https://dev.to/code-of-conduct)-[report abuse](https://dev.to/report-abuse?url=http://dev.to/jnschrag/creating-pixel-art-with-css-3451)