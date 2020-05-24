Tutorial: How To Make an Animated Interactive Vue.js Slider

# Tutorial: How To Make an Animated Interactive Vue.js Slider

[![80.jpg](../_resources/06f996df96af1315e239d5c5f97fe246.jpg)](https://codepen.io/xdesro/)[Henry Desroches](https://codepen.io/xdesro/)[Pro](https://codepen.io/pro/)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon icon-x js-evernote-checked' data-evernote-id='359'%3e%3cpath d='M100 78.905L78.735 100 49.608 71.094 21.263 99.217 0 78.123 28.344 50 0 21.877 21.263.78l28.345 28.125L78.735 0 100 21.094 70.862 50z' data-evernote-id='269' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Follow](https://codepen.io/xdesro/post/tutorial-vue-slider#0)

|[**Henry Desroches's Posts**](https://codepen.io/xdesro/posts/published/)
Jun 4, 2019

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' data-evernote-id='369'%3e %3cpath d='M85.24 2.67C72.29-3.08 55.75 2.67 50 14.9 44.25 2 27-3.8 14.76 2.67 1.1 9.14-5.37 25 5.42 44.38 13.33 58 27 68.11 50 86.81 73.73 68.11 87.39 58 94.58 44.38c10.79-18.7 4.32-35.24-9.34-41.71z' data-evernote-id='157' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart icon-animator js-evernote-checked' data-evernote-id='371'%3e %3c/svg%3e)](https://codepen.io/xdesro/post/tutorial-vue-slider#0)

## [#](https://codepen.io/xdesro/post/tutorial-vue-slider#introduction-0)Introduction

So, I was looking for a fun example of UI interactivity to prototype on Codepen, and I stumbled upon [this really cool shot](https://dribbble.com/shots/6566320-Kalli-Hero) that [Alexsander Barhon](http://alexsanderbarhon.dribbble.com/) shared.

![dribbble-shot_1MB.gif](../_resources/2ded614bffde6bea6a077a5179bfcb66.gif)

It's a simple enough animation, with a really nice loading effect and staggered timeline that make it feel super fluid. I've been really into [Vue.js](https://vuejs.org/) lately, and this seemed like a perfect opportunity to code out a little app. Live your life, but I'm gonna use SCSS for style here.

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#tldr-1)Tl;dr

If you wanna skip the tutorial and get the source, scroll to the bottom of the post or just go check out the [finished pen](https://codepen.io/xdesro/pen/dEwMOq). This post is gonna go pretty in-depth on everything it took to get this running, including the foundational CSS, etc. If you're just looking for the [Vue Interactivity](https://codepen.io/xdesro/post/tutorial-vue-slider#interactivity-with-vuejs-12) or [Vue transitions section](https://codepen.io/xdesro/post/tutorial-vue-slider#animating-with-vuejs-transition-and-transition-group-15), that's cool too.

## [#](https://codepen.io/xdesro/post/tutorial-vue-slider#getting-started-2)Getting Started

When I'm building components like this, I always try to get markup and style in place before trying to futz with JavaScript. That way, I can focus on making things semantic and DRY without adding an additional layer of abstraction.

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#basic-html-structure-3)Basic HTML Structure

There's a bunch of different ways you could break this app down, but based on the way it animates in the Dribbble shot, I see it in three major components, and then a few sub-pieces:

![component-breakdown.png](../_resources/a9229661e161cee11d361ac3b08e6111.png)

The reason I keep the top navigation separate from the slider or sidebar is because it all animates in together and seems to generally serve the same purpose. There's definitely an argument to be made that the "kalli" logo is part of the slider and the "about" section is part of the sidebar, but for the sake of this demo, I'm gonna keep them separate.

Let's code it out:

HTML  `<div class="viewport">[[NEWLINE]]  <nav class="nav">[[NEWLINE]]    <div class="nav__brand">[[NEWLINE]]      <!-- Logo goes here. -->[[NEWLINE]]    </div>[[NEWLINE]]    <ul class="nav__list">[[NEWLINE]]      <!-- Nav items go here. -->[[NEWLINE]]    </ul>[[NEWLINE]]  </nav>[[NEWLINE]]  <main class="main">[[NEWLINE]]    <div class="main__slider">[[NEWLINE]]      <!-- Slides will go here -->[[NEWLINE]]    </div>[[NEWLINE]]    <div class="main__headline">[[NEWLINE]]      <!-- Headline here -->[[NEWLINE]]    </div>[[NEWLINE]]    <div class="main__nav">[[NEWLINE]]      <!-- Play video & social links will go here. -->[[NEWLINE]]    </div>[[NEWLINE]]  </main>[[NEWLINE]]  <aside class="aside">[[NEWLINE]]    <div class="aside__nav">[[NEWLINE]]      <!-- Our buttons to navigate the slides will go in here. -->[[NEWLINE]]    </div>[[NEWLINE]]    <div class="aside__slider">[[NEWLINE]]      <!-- Slider numero dos. No prob. -->[[NEWLINE]]    </div>[[NEWLINE]]    <div class="progress-indicator">[[NEWLINE]]      <!-- This is like that 01———03 thing in the bottom right. -->[[NEWLINE]]    </div>[[NEWLINE]]  </aside>[[NEWLINE]]</div>[[NEWLINE]]`

So far so good. I'm using BEM-*ish* classes for everything, because I like how easy it is to organize in your SCSS without increasing specificity. *(We typically want to avoid selectors like `.nav .list` or whatever, and sometimes Sass' nesting feature can make that an easy trap to fall into. `.nav__list` is just as clear and much easier to override/much less specific.)*

You'll also notice I'm assigning seemingly-duplicative classes like `.nav` to the `<nav>` element or `.aside` to the `<aside>`. I don't usually use tag name selectors for structural elements because it makes the CSS more dependent on the HTML structure.

**Don't worry about style just yet.** If we make sure our HTML is meaningful and well-structured without style, it'll be that much easier to write up the CSS.

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#primary-nav-4)Primary Nav

The navigation at the top has two distinct sections — the logo and the right-aligned nav items.

HTML  `<nav class="nav">[[NEWLINE]]  <div class="nav__brand">[[NEWLINE]]    <p>Logo</p>[[NEWLINE]]  </div>[[NEWLINE]]  <ul class="nav__list">[[NEWLINE]]    <li class="nav__list-item">About</li>[[NEWLINE]]    <li class="nav__list-item">More</li>[[NEWLINE]]  </ul>[[NEWLINE]]</nav>[[NEWLINE]]`

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#main-section-and-slider-5)Main Section & Slider

I want to keep the slider slides and headline separate, because they animate in different ways, but close enough that they're clearly related.

HTML  `<main class="main">[[NEWLINE]]  <div class="main__slider">[[NEWLINE]]    <img class="main__slide-image" src="slide1.jpg" />[[NEWLINE]]  </div>[[NEWLINE]]  <div class="main__headline">[[NEWLINE]]    <span class="main__headline-span">Simplicity is the ultimate sophistication.</span>[[NEWLINE]]  </div>[[NEWLINE]]  <div class="main__nav">[[NEWLINE]]    <p>Play Video</p>[[NEWLINE]]    <ul class="social-links">[[NEWLINE]]      <li class="social-links__item">[[NEWLINE]]        <a href="https://facebook.com">Fb</a>[[NEWLINE]]      </li>[[NEWLINE]]      <li class="social-links__item">[[NEWLINE]]        <a href="https://twitter.com/">Tw</a>[[NEWLINE]]      </li>[[NEWLINE]]      <li class="social-links__item">[[NEWLINE]]        <a href="https://www.linkedin.com/">In</a>[[NEWLINE]]      </li>[[NEWLINE]]    </ul>[[NEWLINE]]  </div>[[NEWLINE]]</main>[[NEWLINE]]`

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#aside-and-secondary-slider-6)Aside & Secondary Slider

I know we need two buttons that navigate forward and backward in the slider, a secondary container for the aside slider that we'll mark up in a similar way to the first slider, and a progress indicator. I think I'm gonna use pseudo-elements for the counter on the progress indicator, so I'll pass it the total number of slides via a `data-slides-count` attribute.

HTML  `<aside class="aside">[[NEWLINE]]  <div class="aside__nav">[[NEWLINE]]    <button class="aside__button">←</button>[[NEWLINE]]    <button class="aside__button">→</button>[[NEWLINE]]  </div>[[NEWLINE]]  <div class="aside__slider">[[NEWLINE]]    <img class="aside__slide-image" src="slide2.jpg" />[[NEWLINE]]  </div>[[NEWLINE]]  <ul class="progress-indicator" data-slides-count="03">[[NEWLINE]]    <li class="progress-indicator__bar"></li>[[NEWLINE]]  </ul>[[NEWLINE]]</aside>[[NEWLINE]]`

And that's the markup done. I really love coding these puppies in layers like this because now that I know that my HTML is sound, I don't have to worry about it again for a while.

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#basic-style-7)Basic Style

Let's get Sassy with it. In my initial iteration of this idea, I used CSS variables and other weird stuff, so if you're interested in that but have to support older browsers, it might be worth looking into a polyfill, or better yet, a *[ponyfill](https://jhildenbiddle.github.io/css-vars-ponyfill/#/). * This version of the tutorial doesn't include any of that crazy bonkers stuff.

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#responsive-css-8)"Responsive" CSS

I elected to use a pattern I lean on a lot for CodePens to make things "responsive", where I set a font size for the app using viewport units and then measure everything based on that root font size using `rem` units. It looks a little something like this *(note the `#{}` syntax for interpolating SCSS variables):*

SCSS  `$app-width: 95vmin;[[NEWLINE]]html {[[NEWLINE]]  font-size: calc(#{$app-width} / 100);[[NEWLINE]]}[[NEWLINE]].viewport {[[NEWLINE]]  width: $app-width;[[NEWLINE]]  height: calc(#{$app-width} * (9/16));[[NEWLINE]]}[[NEWLINE]]`

This block does a few things:

1. I've decided I want my app to be as large as possible without ever touching the edge of the screen, so I'll use `95vmin` to make sure it is always 95% of the width or the height of the screen (whichever is smaller).

2. In the `html` selector, I set the font size to be 1/100th of the width of the app — that way I know that `1rem` will always be 1% of the width of the app. (This obviously isn't required, I just like to have a very consistent and scalable unit to rely on when I'm making pens.)

3. I measured the sides of the app in the video on Dribbble, and found that the app's aspect ratio was 16/9. Thus, I've set the `.viewport` (which is the class I'll add to my app wrapper) width to `$app-width` and then set its height to `$app-width * (9/16)`, to ensure it is always the correct aspect ratio.

Let's keep trucking.

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#layout-style-9)Layout Style

We're gonna default to using CSS Grid for most of our layout problems, with some absolute positioning.

SCSS  `body {[[NEWLINE]]  display: grid;[[NEWLINE]]  place-items: center;[[NEWLINE]]}[[NEWLINE]].viewport {[[NEWLINE]]  position: relative;[[NEWLINE]]  display: grid;[[NEWLINE]]  grid-template-columns: 1fr 30rem;[[NEWLINE]]  // width, height...[[NEWLINE]]}[[NEWLINE]]`

That'll make the `<aside>` section 30% of the width of the app and the main slider will take up the rest of the available space. Let's do the nav next.

SCSS  `.nav {[[NEWLINE]]  padding: 5rem;[[NEWLINE]]  display: grid;[[NEWLINE]]  grid-auto-flow: column;[[NEWLINE]]  justify-content: space-between;[[NEWLINE]]  z-index: 1;[[NEWLINE]]  position: absolute;[[NEWLINE]]  top: 0;[[NEWLINE]]  left: 0;[[NEWLINE]]  right: 0;[[NEWLINE]]  &__list {[[NEWLINE]]    display: grid;[[NEWLINE]]    grid-auto-flow: column;[[NEWLINE]]    justify-content: space-between;[[NEWLINE]]    width: 20rem;[[NEWLINE]]    padding: 0; // Unset default ul padding. You could use a CSS reset too.[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

So here we've decided the nav itself will be a grid, but by giving it `position: absolute;` we're taking it out of the parent grid. *(Z-index just makes sure it's always the top-most element in the z-index stack.)* Then we use the ampersand selector to style the right-aligned nav as grid as well. Let's do the `<main>` section and its children.

SCSS  `.main {[[NEWLINE]]  display: grid;[[NEWLINE]]  grid-template-rows: 2fr 1fr;[[NEWLINE]]  grid-template-areas: "headline" "nav";[[NEWLINE]]  align-items: end;[[NEWLINE]]  &__slider {[[NEWLINE]]    position: absolute;[[NEWLINE]]    z-index: 0;[[NEWLINE]]    top: 0;[[NEWLINE]]    left: 0;[[NEWLINE]]    width: 70rem; (T[[NEWLINE]]    height: 100%;[[NEWLINE]]  }[[NEWLINE]]  &__headline {[[NEWLINE]]    padding: 5rem;[[NEWLINE]]    grid-area: headline[[NEWLINE]]  }[[NEWLINE]]  &__nav {[[NEWLINE]]    z-index: 1;[[NEWLINE]]    display: grid;[[NEWLINE]]    grid-template-columns: 1fr auto;[[NEWLINE]]    grid-area: nav;[[NEWLINE]]    width: 30rem;[[NEWLINE]]    padding: 3rem 5rem; // I'm using 3rem vertical instead of 5rem all around cause it just looks better [[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]].social-links {[[NEWLINE]]  display: grid;[[NEWLINE]]  grid-auto-flow: column;[[NEWLINE]]  grid-gap: 0.4rem;[[NEWLINE]]  align-items: center;[[NEWLINE]]}[[NEWLINE]]`

Movin' right along. Let's layout the `<aside>` element.

SCSS  `.aside {[[NEWLINE]]  position: relative;[[NEWLINE]]  display: grid;[[NEWLINE]]  padding: 5rem; // That DANG 5rem padding again....[[NEWLINE]]  $button-size: 10rem;[[NEWLINE]]  &__slider {[[NEWLINE]]    position: relative;[[NEWLINE]]    height: 25rem;[[NEWLINE]]    margin-top: 10rem;[[NEWLINE]]  }[[NEWLINE]]  &__button {[[NEWLINE]]    width: $button-size;[[NEWLINE]]    height: $button-size;[[NEWLINE]]  }[[NEWLINE]]  &__nav {[[NEWLINE]]    position: absolute;[[NEWLINE]]    bottom: 0;[[NEWLINE]]    left: -#{$button-size}[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

Same padding as the top nav, etc. here *(if I was a clever person perhaps I'd make it a Sass variable like I did with the button sizing but I am*  **not**  *so here we*  **go**, *baby).*

Looking pretty slick so far. This looks about how we initially broke down the Dribbble screenshot.

- [HTML](https://codepen.io/anon/embed/YbBogX?slug-hash=YbBogX&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_1#html-box)
- [SCSS](https://codepen.io/anon/embed/YbBogX?slug-hash=YbBogX&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_1#css-box)
- [Result](https://codepen.io/anon/embed/YbBogX?slug-hash=YbBogX&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_1#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='13' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='36' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/xdesro/pen/YbBogX)

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.
Next we'll add some more visual style to the app.

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#visual-spice-10)Visual Spice

So the first thing I'm gonna mention is that I don't actually know what font is in use here off-hand, so I'll be using instead this really nice sans-serif font called [Inter](https://rsms.me/inter/). Let's go ahead and include it in our style sheet.

SCSS  `@import url('https://rsms.me/inter/inter.css');[[NEWLINE]]html {[[NEWLINE]]  font-size: calc(#{$app-width} / 100);[[NEWLINE]]  font-family: "Inter", sans-serif;[[NEWLINE]]  @supports (font-variation-settings: normal) {[[NEWLINE]]    font-family: "Inter var", sans-serif;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

Let's style the pen a little bit so it's not just a bunch of white rectangles. We'll start with some variables and general app stuff.

SCSS  `$color--background: hsl(300, 3%, 15%); // Note the $block--modifier syntax. This is just personal preference. Just be consistent![[NEWLINE]]$color--primary: hsl(0, 0%, 100%); // White color for most of the app.[[NEWLINE]]$color--secondary: hsl(0, 0%, 90%); // Off-white for the progress indicator[[NEWLINE]]$color--neutral: hsl(0, 0%, 1%); // Nearly-black color for text.[[NEWLINE]][[NEWLINE]]body {[[NEWLINE]]  background-color: $color--background;[[NEWLINE]]}[[NEWLINE]].viewport {[[NEWLINE]]  background-color: $color--primary;[[NEWLINE]]  box-shadow: 0 1rem 2rem hsla(0, 0%, 0%, 0.2); [[NEWLINE]]}[[NEWLINE]]`

Next we'll do some placeholder images in this puppy and style up the slider.

In the HTML, we can use [source.unsplash.com](https://source.unsplash.com/) to get a random image that *generally* fits the size we want.

HTML  `<div class="main__slider">[[NEWLINE]]  <img class="main__slide-image"[[NEWLINE]]       src="https://source.unsplash.com/random/1350x1080" />[[NEWLINE]]</div>[[NEWLINE]]<!-- ... -->[[NEWLINE]]<div class="aside__slider">[[NEWLINE]]  <img class="aside__slide-image"[[NEWLINE]]       src="https://source.unsplash.com/random/1350x1080" />[[NEWLINE]]</div>[[NEWLINE]]`

In the SCSS, we'll use the same code for the images twice, so let's make it a `@mixin`. We'll include that for both slide images and use `overflow:hidden` for the wrapping slider elements.

SCSS  `@mixin slide-image {[[NEWLINE]]  position: absolute;[[NEWLINE]]  height: 100%;[[NEWLINE]]  object-fit: cover;[[NEWLINE]]}[[NEWLINE]].main {[[NEWLINE]]  // ...[[NEWLINE]]  &__slider {[[NEWLINE]]    //...[[NEWLINE]]    overflow: hidden;[[NEWLINE]]  }[[NEWLINE]]  &__slide-image {[[NEWLINE]]    @include slide-image;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]].aside {[[NEWLINE]]  //...[[NEWLINE]]  &__slider {[[NEWLINE]]    //...[[NEWLINE]]    overflow: hidden;[[NEWLINE]]  }[[NEWLINE]]  &__slide-image {[[NEWLINE]]    @include slide-image;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

I think the last two kinda strange parts of this are the social links and the progress indicator. Let's kick those off.

#### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#progress-indicator-11)Progress Indicator

In CSS grid, you can actually use pseudo elements as grid-level elements, and that works out great for this example, where the social links are divided by two dashes. We already set the social links up as a grid, but now lets place the pseudo-elements in that grid:

SCSS  `.social-links {[[NEWLINE]]  // ...[[NEWLINE]]  &:before,[[NEWLINE]]  &:after {[[NEWLINE]]    content: "";[[NEWLINE]]    display: block;[[NEWLINE]]    width: 1rem;[[NEWLINE]]    height: 0.1rem;[[NEWLINE]]    background: $color--primary;[[NEWLINE]]  }[[NEWLINE]]  &:before {[[NEWLINE]]    grid-column: 2;[[NEWLINE]]  }[[NEWLINE]]  &:after {[[NEWLINE]]    grid-column: 4;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

That looks about right to me!
![social-links.png](:/9da9ab489655f74eead6ba43e0cf7cdb)

Next let's do the progress indicator. We'll use pseudo elements for the numbers at the start and end, and use `<li>` elements in between to show which slide is currently active.

SCSS  `.progress-indicator {[[NEWLINE]]  // ...[[NEWLINE]]  &:before,[[NEWLINE]]  &:after {[[NEWLINE]]    color: $color--neutral;[[NEWLINE]]  }[[NEWLINE]]  &:before {[[NEWLINE]]    content: "01";[[NEWLINE]]  }[[NEWLINE]]  &:after {[[NEWLINE]]    content: attr(data-slides-count);[[NEWLINE]]  }[[NEWLINE]]  &__bar {[[NEWLINE]]    width: 1.5rem;[[NEWLINE]]    height: 0.2rem;[[NEWLINE]]    background: $color--secondary;[[NEWLINE]]    &--active {[[NEWLINE]]      background: $color--neutral;[[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

Remember when we used a data-attribute to set the slides count? Here's where it comes in handy. We can make that dynamic in the Vue step but for now we just did it manually.

HTML  `<ul class="progress-indicator" data-slides-count="03">[[NEWLINE]]`
Real nice:
![progress-indicator.png](../_resources/7b5d4fb23452d7e68147dec4655abb13.png)

I'll breeze through the rest of the styles we'll be adding. It's mostly simple visual stuff like setting colors or font sizes — no more weird grid hackery. After all that, our slider's about ready to become interactive!

- [HTML](https://codepen.io/anon/embed/wbOwNw?slug-hash=wbOwNw&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_2#html-box)
- [SCSS](https://codepen.io/anon/embed/wbOwNw?slug-hash=wbOwNw&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_2#css-box)
- [Result](https://codepen.io/anon/embed/wbOwNw?slug-hash=wbOwNw&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_2#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='13' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='36' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/xdesro/pen/wbOwNw)

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

## [#](https://codepen.io/xdesro/post/tutorial-vue-slider#interactivity-with-vuejs-12)Interactivity With Vue.js

The first thing we'll do is get Vue included and turn our "app" into an App™.

In CodePen, under the Javascript settings tab, you can add Vue as an external resource:

![vue-resource.png](../_resources/d5e2a578f3ab205c7d537e862625d293.png)

Once we've got Vue included, let's add an ID to the markup of the app and initialize a Vue instance.

HTML  `<div class="viewport" id="app">[[NEWLINE]]`

JavaScript  `const app = new Vue({[[NEWLINE]]  el: "#app"[[NEWLINE]]})[[NEWLINE]]`

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#adding-slides-13)Adding Slides

In our Vue instance, let's add some data for slides and a currently-active slide index, and then populate that data in the template markup.

JavaScript  `const app = new Vue({[[NEWLINE]]  el: "#app",[[NEWLINE]]  data() {[[NEWLINE]]    return {[[NEWLINE]]      currentActiveSlide: 0,[[NEWLINE]]      slides: [[[NEWLINE]]        {[[NEWLINE]]          headline: 'Lorem ipsum dolor sit amet',[[NEWLINE]]          img: 'https://source.unsplash.com/random/1350x1080'[[NEWLINE]]        },[[NEWLINE]]        {[[NEWLINE]]          headline: 'Consectetur adipiscing elit, sed do.',[[NEWLINE]]          img: 'https://source.unsplash.com/random/1350x1081'[[NEWLINE]]        },[[NEWLINE]]        {[[NEWLINE]]          headline: 'Eiusmod tempor incididunt ut labore.',[[NEWLINE]]          img: 'https://source.unsplash.com/random/1350x1082'[[NEWLINE]]        },[[NEWLINE]]      ][[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]})[[NEWLINE]]`

HTML  `<div class="main__slider">[[NEWLINE]]  <img v-for="(slide, index) of slides" :key="index" v-if="index === currentActiveSlide" class="main__slide-image" :src="slide.img" />[[NEWLINE]]</div>[[NEWLINE]]<div class="main__headline">[[NEWLINE]]  <span v-for="(slide, index) of slides" :key="index" v-if="index === currentActiveSlide" class="main__headline-span">{{ slide.headline }}</span>[[NEWLINE]]</div>[[NEWLINE]]`

You'll notice we didn't do anything for the slider in the `<aside>` section. That's because I want the aside slider to always show the slide directly after the currently active one, or show the first slide if we're at the end of the slides. I can do this with a Vue computed value we'll call `nextActiveSlide`.

JavaScript  `const app = new Vue({[[NEWLINE]]  // ...[[NEWLINE]]  computed: {[[NEWLINE]]    nextActiveSlide() {[[NEWLINE]]      return this.currentActiveSlide + 1 >= this.slides.length ? 0 : this.currentActiveSlide + 1;[[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]});[[NEWLINE]]`

And once we've got that we can do this in the template:

HTML  `<div class="aside__slider">[[NEWLINE]]  <img v-for="(slide, index) of slides" :key="index" v-if="index === nextActiveSlide" class="aside__slide-image"  :src="slide.img" />[[NEWLINE]]</div> [[NEWLINE]]`

Last thing to do is the progress indicator. We can do this all in the template, by creating as many progress bars as there are slides, and then conditionally adding a class if it should be active.

HTML  `<ul class="progress-indicator"[[NEWLINE]]    :data-slides-count="'0' + slides.length">[[NEWLINE]]  <li v-for="(slide,index) of slides"[[NEWLINE]]      :key="index"[[NEWLINE]]      :class="index === currentActiveSlide ? 'progress-indicator__bar  progress-indicator__bar--active' : 'progress-indicator__bar'"></li>[[NEWLINE]]</ul>[[NEWLINE]]`

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#navigating-between-slides-14)Navigating Between Slides

The actual slide navigation is pretty simple, thanks to Vue – it'll listen to the `currentActiveSlide` value and change everything we need based on that. We'll add a method to handle slide changes. I've elected to be kinda wordy with this method for the sake of readability, but you could be much more concise!

JavaScript  `const app = new Vue({[[NEWLINE]]  // ...[[NEWLINE]]  methods: {[[NEWLINE]]    // We'll pass the function either 1 or -1 to indicate which direction we'the slides will go[[NEWLINE]]    handleSlideChange(val) {[[NEWLINE]]      let direction;[[NEWLINE]]      const calculatedNextSlide = this.currentActiveSlide + val;[[NEWLINE]]      if (val > 0) {[[NEWLINE]]        direction = "next";[[NEWLINE]]      } else {[[NEWLINE]]        direction = "previous";[[NEWLINE]]      }[[NEWLINE]]      if (direction === "next" && calculatedNextSlide < this.slides.length) {[[NEWLINE]]        this.currentActiveSlide += val;[[NEWLINE]]      } else if (direction === "next") {[[NEWLINE]]        this.currentActiveSlide = 0;[[NEWLINE]]      } else if (direction === "previous" && calculatedNextSlide < 0) {[[NEWLINE]]        this.currentActiveSlide = this.slides.length - 1;[[NEWLINE]]      } else {[[NEWLINE]]        this.currentActiveSlide += val;[[NEWLINE]]      }[[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]});[[NEWLINE]]`

Then in our markup we'll update those buttons in the `<aside>` section so when clicked, they call that `handleSlideChange()` method.

HTML  `<div class="aside__nav">[[NEWLINE]]  <button class="aside__button"[[NEWLINE]]          @click="handleSlideChange(-1)">←</button>[[NEWLINE]]  <button class="aside__button"[[NEWLINE]]          @click="handleSlideChange(1)">→</button>[[NEWLINE]]</div>[[NEWLINE]]`

And just like that, we're all hooked up to data, slidin' around, and ready to animate.

- [HTML](https://codepen.io/anon/embed/EzMMvE?slug-hash=EzMMvE&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_3#html-box)
- [SCSS](https://codepen.io/anon/embed/EzMMvE?slug-hash=EzMMvE&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_3#css-box)
- [JS](https://codepen.io/anon/embed/EzMMvE?slug-hash=EzMMvE&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_3#js-box)
- [Result](https://codepen.io/anon/embed/EzMMvE?slug-hash=EzMMvE&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_3#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/xdesro/pen/EzMMvE)

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

1. https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.10/vue.min.js

## [#](https://codepen.io/xdesro/post/tutorial-vue-slider#animating-with-vuejs-transition-and-transition-group-15)Animating With Vue.js `<transition>` and `<transition-group>`

In Vue, you can use the `<transition>` component to trigger animations in CSS or fire JavaScript methods on state changes. We'll be handling all of our transitions with CSS this time around, but you can check [the exceptional Vue docs](https://vuejs.org/v2/guide/transitions.html) for more potential uses. The general flow is that

Let's start by transitioning the headline when you change slides with `<transition-group>`, which is best for list transitions.

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#transitioning-the-headline-16)Transitioning the Headline

The first step is to convert the `.main__headline` div into a `<transition-group>`:

HTML  `<transition-group tag="div" class="main__headline" name="main__headline-span" mode="out-in">[[NEWLINE]]  <span v-for="(slide, index) of slides" :key="index" v-if="index === currentActiveSlide" class="main__headline-span">{{ slide.headline }}</span>[[NEWLINE]]</transition-group>[[NEWLINE]]`

There are a few things going on here:

- We replaced the `<div>` element with a `<transition-group tag="div">` element. The group will render as a `<div>`.
- We gave that transition group a name of `main__headline-span` — what this means is that when a transition is occurring, it'll apply the transition classes to its children with this prefix. For example:
    - `.main__headline-span-enter-active`
    - `.main__headline-span-leave-to`

*(This will come in handy when we're writing our transition code in SCSS.)*

- We set the mode to "out-in" — this basically means the element that we're transitioning out will be completely transitioned out before we start transitioning in the new element.

Now we can write the CSS to make some magic happen.

SCSS  `// ...[[NEWLINE]].main {[[NEWLINE]]  // ...[[NEWLINE]]  &__headline-span {[[NEWLINE]]    position: absolute; // This is just to make sure there's no jumping around as we transition elements out and in.[[NEWLINE]]    width: 60rem; // We have to add this because we're absolutely positioning the headline-span[[NEWLINE]]    &-enter,[[NEWLINE]]    &-leave-to { // This is an easy way for us to keep the animation code with the component code. This selector outputs `.main__headline-span-enter, .main__headline-span-leave-to {}`[[NEWLINE]]      transform: translateY(1em);[[NEWLINE]]      opacity: 0;[[NEWLINE]]    }[[NEWLINE]]    &-enter-active,[[NEWLINE]]    &-leave-active {[[NEWLINE]]      transition: all 300ms;[[NEWLINE]]    }[[NEWLINE]]    &-enter-active {[[NEWLINE]]      transition-delay: 700ms; // This makes the new headline take just a moment to come in.[[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

### [#](https://codepen.io/xdesro/post/tutorial-vue-slider#transitioning-the-slides-using-clip-path-17)Transitioning The Slides Using `clip-path`

Let's use `<transition-group>` again to prepare the main and aside sliders to be animated.

HTML  `<!-- ... -->[[NEWLINE]]<transition-group tag="div" class="main__slider" name="main__slide-image" mode="out-in">[[NEWLINE]]  <img v-for="(slide, index) of slides" :key="index" v-if="index === currentActiveSlide" class="main__slide-image"[[NEWLINE]]    :src="slide.img" />[[NEWLINE]]</transition-group>[[NEWLINE]]`

Same as the previous example, we replace the slider wrapper `<div>` with a `<transition-group>` that gets the class of its children as a `name` attribute. That's all it takes. Let's write some more CSS.

I'd like to use the CSS `clip-path` property to transition the slides — I think it'll be the most visually-satisfying way to achieve that wipe that happens in the Dribbble shot. We're going to transition a `clip-path: polygon()` value. When a slide is active, the `clip-path` won't clip any of the image:

![clip-path.png](../_resources/5888043329cee960acdb932fd557b026.png)
Since we want to wipe from left-to-right, we need two different clip paths:

- Clipped to the left side ("enter" state): `polygon(0 0, 0 0, 0 100%, 0 100%)`
- Clipped to the right side ("leave-to" state): `polygon(100% 0, 100% 100%, 100% 100%, 100% 0)`

Let's implement that in our SCSS. We're reusing this animation for both sliders, so we'll make it a mixin. *(I also want a subtle zoom effect on the image.)*

SCSS  `@mixin clip-path-wipe {[[NEWLINE]]  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); // Specify the "slide visible" state[[NEWLINE]]  &-enter {[[NEWLINE]]    clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);[[NEWLINE]]    transform: scale(1.3);[[NEWLINE]]  }[[NEWLINE]]  &-leave-to {[[NEWLINE]]    clip-path: polygon(100% 0, 100% 0, 100% 100%, 100% 100%);[[NEWLINE]]    transform: scale(1.3);[[NEWLINE]]  }[[NEWLINE]]  &-enter-active {[[NEWLINE]]    transition: all 700ms;[[NEWLINE]]    transition-delay: 500ms;[[NEWLINE]]  }[[NEWLINE]]  &-leave-active {[[NEWLINE]]    transition: all 700ms;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

Now let's hook into this in the `<main>` slider.

SCSS  `.main {[[NEWLINE]]  // ...[[NEWLINE]]  &__slider {[[NEWLINE]]    // ...[[NEWLINE]]    background-color: $color--neutral; // This makes it so the slider background isn't just white.[[NEWLINE]]    width: 70rem; [[NEWLINE]]    overflow: hidden; // Make sure the image doesn't overflow when it scales up[[NEWLINE]]  }[[NEWLINE]]  &__slide-image {[[NEWLINE]]    // ...[[NEWLINE]]    @include clip-path-wipe;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

And again in the `<aside>` slider:

SCSS  `.aside {[[NEWLINE]]  // ...[[NEWLINE]]  &__slider {[[NEWLINE]]    background-color: $color--neutral;[[NEWLINE]]  }[[NEWLINE]]  &__slide-image {[[NEWLINE]]    // ...[[NEWLINE]]    @include clip-path-wipe;[[NEWLINE]]    &-leave-active {[[NEWLINE]]      transition-delay: 200ms; // Offset this animation slightly from the main slider[[NEWLINE]]    }[[NEWLINE]]    &-enter-active {[[NEWLINE]]      transition-delay: 600ms; // See above[[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

- [HTML](https://codepen.io/anon/embed/joREmZ?slug-hash=joREmZ&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_4#html-box)
- [SCSS](https://codepen.io/anon/embed/joREmZ?slug-hash=joREmZ&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_4#css-box)
- [JS](https://codepen.io/anon/embed/joREmZ?slug-hash=joREmZ&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_4#js-box)
- [Result](https://codepen.io/anon/embed/joREmZ?slug-hash=joREmZ&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_4#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/xdesro/pen/joREmZ)

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

1. https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.10/vue.min.js

## [#](https://codepen.io/xdesro/post/tutorial-vue-slider#conclusion-18)Conclusion

And just like that, we're all ready to rumble. If you wanted to, there are a couple of enhancements you could include:

- Write some CSS to transition the progress indicator a little more smoothly.
- Add a boolean `loaded` state to the Vue `data()`, and transition in the navigation and slider depending on whether `loaded === true` or not.
- Use [Vibrant.js](https://jariz.github.io/vibrant.js/) or similar to set the background of the slider to an accent color of the slider image!

If you end up giving this a shot or customizing it in any way, let me know on Twitter [@xdesro](https://i.ncredibly.online/)! I'd love to see it. Thanks for reading. As promised, [here's the finished pen](https://codepen.io/xdesro/pen/dEwMOq).

- [HTML](https://codepen.io/anon/embed/dEwMOq?slug-hash=dEwMOq&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_5#html-box)
- [SCSS](https://codepen.io/anon/embed/dEwMOq?slug-hash=dEwMOq&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_5#css-box)
- [JS](https://codepen.io/anon/embed/dEwMOq?slug-hash=dEwMOq&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_5#js-box)
- [Result](https://codepen.io/anon/embed/dEwMOq?slug-hash=dEwMOq&default-tab=result&height=700&theme-id=0&user=anon&name=cp_embed_5#result-box)

[EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='15' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='38' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/xdesro/pen/dEwMOq)

-
-
-

### External CSS

1. https://rsms.me/inter/inter.css

### External JavaScript

1. https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.10/vue.min.js
2. https://cdn.jsdelivr.net/npm/node-vibrant@3.2.0-alpha/dist/vibrant.min.js

*P.S. This is my first tutorial-style blog post — please let me know if you have any feedback or found any problems with the post! Thanks for reading.*

* * *

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' data-evernote-id='2176'%3e %3c/svg%3e)![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart icon-animator js-evernote-checked' data-evernote-id='2178'%3e %3c/svg%3e)](https://codepen.io/xdesro/post/tutorial-vue-slider#0)

2,365![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-eye js-evernote-checked' data-evernote-id='2182'%3e %3cpath d='M15.3 0C8.9 0 3.3 3.3 0 8.3c3.3 5 8.9 8.3 15.3 8.3s12-3.3 15.3-8.3C27.3 3.3 21.7 0 15.3 0zm0 14.5c-3.4 0-6.2-2.8-6.2-6.2C9 4.8 11.8 2 15.3 2c3.4 0 6.2 2.8 6.2 6.2 0 3.5-2.8 6.3-6.2 6.3z' data-evernote-id='87' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)3![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-comment js-evernote-checked' data-evernote-id='2185'%3e %3cpath d='M-391 291.4c0 1.5 1.2 1.7 1.9 1.2 1.8-1.6 15.9-14.6 15.9-14.6h19.3c3.8 0 4.4-.8 4.4-4.5v-31.1c0-3.7-.8-4.5-4.4-4.5h-47.4c-3.6 0-4.4.9-4.4 4.5v31.1c0 3.7.7 4.4 4.4 4.4h10.4v13.5z' data-evernote-id='68' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)45![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' data-evernote-id='2189'%3e %3c/svg%3e)

[Comments](https://codepen.io/xdesro/post/tutorial-vue-slider#post-comments)[Tags](https://codepen.io/xdesro/post/tutorial-vue-slider#post-tags)[Lovers](https://codepen.io/xdesro/post/tutorial-vue-slider#lovers)

1.

[![user-avatar-80x80-bdcd44a3bfb9a5fd01eb8b86f9e033fa1a9897c3a15b33adfc2649a002dab1b6.png](../_resources/ccef07d0d2207b9568de54d323d4197f.png)](https://codepen.io/FrenchCooder)

[Maxime](https://codepen.io/FrenchCooder)(@FrenchCooder)on[June 7, 2019](https://codepen.io/xdesro/post/tutorial-vue-slider#comment-id-9150)

Nice tutorial ! Well explained, good job for your first post :)

[1Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='2221'%3e %3c/svg%3e)]()

2.

[![80.jpg](../_resources/27e6a17cbf6b85754477b162fd734f68.jpg)](https://codepen.io/giuliamalaroda)

[Giulia Malaroda](https://codepen.io/giuliamalaroda)(@giuliamalaroda)on[June 7, 2019](https://codepen.io/xdesro/post/tutorial-vue-slider#comment-id-9151)

Incredibly well written article. Loved it! I'll wait for your next one ;)
Good job!!

[1Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='2242'%3e %3c/svg%3e)]()

3.

[![user-avatar-80x80-bdcd44a3bfb9a5fd01eb8b86f9e033fa1a9897c3a15b33adfc2649a002dab1b6.png](../_resources/ccef07d0d2207b9568de54d323d4197f.png)](https://codepen.io/000Bo)

[000Bo](https://codepen.io/000Bo)(@000Bo)on[June 8, 2019](https://codepen.io/xdesro/post/tutorial-vue-slider#comment-id-9158)

good!!!

[1Love![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-heart js-evernote-checked' width='11' height='11' data-evernote-id='2262'%3e %3c/svg%3e)]()

#### Leave a Comment[Markdown](https://daringfireball.net/projects/markdown/syntax) supported.Click @usernames to add to comment.

You must be [logged in](https://codepen.io/login/) to comment.