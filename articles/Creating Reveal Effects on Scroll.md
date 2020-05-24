Creating Reveal Effects on Scroll

#  Creating Reveal Effects on Scroll

###     [![slfth2p9wq0wdf50xtus.png](../_resources/237d46d8565709cf246bcecd62fd51ee.webp)  Katherine Kato](https://dev.to/kathykato)    [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 612 612' class='icon-img js-evernote-checked' data-evernote-id='169'%3e%3cpath d='M612 116.258c-22.525 9.98-46.694 16.75-72.088 19.772 25.93-15.527 45.777-40.155 55.184-69.41-24.322 14.378-51.17 24.82-79.775 30.48-22.906-24.438-55.49-39.66-91.63-39.66-69.333 0-125.55 56.218-125.55 125.514 0 9.828 1.11 19.427 3.25 28.606-104.325-5.24-196.834-55.223-258.75-131.174-10.822 18.51-16.98 40.078-16.98 63.1 0 43.56 22.182 81.994 55.836 104.48-20.575-.688-39.926-6.348-56.867-15.756v1.568c0 60.806 43.29 111.554 100.692 123.104-10.517 2.83-21.607 4.398-33.08 4.398-8.107 0-15.947-.803-23.634-2.333 15.985 49.907 62.336 86.2 117.253 87.194-42.946 33.655-97.098 53.656-155.915 53.656-10.134 0-20.116-.612-29.944-1.72 55.568 35.68 121.537 56.484 192.44 56.484 230.947 0 357.187-191.29 357.187-357.188l-.42-16.253C573.87 163.525 595.21 141.42 612 116.257z'%3e%3c/path%3e%3c/svg%3e)](http://twitter.com/kato_katherine)  Feb 26  ・4 min read

 [#css](https://dev.to/t/css)  [#javascript](https://dev.to/t/javascript)  [#animation](https://dev.to/t/animation)  [#webdev](https://dev.to/t/webdev)

In this tutorial I would like to share on how to create block reveal effects on scroll. The effect consists of solid colored block decreasing in size and revealing text or an image.

These reveal effects can be used to create engaging and fresh interactions for UI components such as image sliders. I created this slider using a similar wipe animation:

[![viwjnn7xxxjwcr0622mh.gif](../_resources/4da6b93234cb480d27279989b0c4c988.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--VcREsZdy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/viwjnn7xxxjwcr0622mh.gif)

View it on [CodePen](https://codepen.io/kathykato/pen/MqYVOq).

I will be showing you how to create this effect with CSS and [Animate on Scroll (AOS)](https://michalsnik.github.io/aos/), a JavaScript library for animating elements on scroll as a user enters the viewport.

* * *

##   [(L)](https://dev.to/kathykato/creating-reveal-effects-on-scroll-31o6#getting-started) Getting started

Let’s begin by adding the Animate on Scroll library to the project. Include the aos.css in `<head>` tag:

	<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

And aos.js before the closing `<body>` tag:

	<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

Once added, initialize AOS:

	AOS.init();

##   [(L)](https://dev.to/kathykato/creating-reveal-effects-on-scroll-31o6#creating-the-reveal-block) Creating the reveal block

First we will create the reveal block for revealing text underneath. We will be grabbing text from [Doggo Ipsum](https://doggoipsum.com/), a lorem ipsum generator from doggo lingo.

	<div class="reveal-holder">
	  <div class="reveal-block"></div>
	  <h1 class="heading">Maximum borkdrive</h1>
	</div>

The `.reveal-holder` class is a container for the solid color block element and text. The styling for these classes are:

	.reveal-holder {
	  position: relative;
	  display: inline-block;
	  overflow: hidden;
	}

	.reveal-block {
	  position: absolute;
	  top: 0;
	  width: 100%;
	  height: 101%;
	  background: white;
	}

This is for the block to cover and reveal an element properly. Having the height of the `.reveal-block` class to 101% is important here:

[[78d36cc6-f40e-45b9-b3cc-4fb07c6862f3.webp](../_resources/37864609de37ba3973ce86de42f9fa3f.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--WvoSBJV5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/slfth2p9wq0wdf50xtus.png)

Setting the height to 100% results in the reveal block not completely over images after window resizing. Having the `overflow` CSS property set to hidden for the `.reveal-holder` class helps prevent anything outside the element's content from clipping.

##   [(L)](https://dev.to/kathykato/creating-reveal-effects-on-scroll-31o6#using-css-transitions) Using CSS transitions

Animations are set using the `data-aos` attribute. For example, to reveal an element from the right, add the attribute to the `.reveal-block` class in the HTML:

	<div class="reveal-block" data-aos="reveal-right"></div>

And CSS:

	[data-aos="reveal-right"] {
	  transform: scaleX(1);
	  transform-origin: 100% 0%;
	  transition-property: transform;
	  transition-delay: 0.5s;
	}

	[data-aos="reveal-right"].aos-animate {
	  transform: scaleX(0);
	}

The `transform` CSS property is using the `scaleX()` function to the `.reveal-block` element in order for the block to resize when animated. The `transform-origin` property sets the point of the transformation, which in this case is at 100% 0% or right left. This is what causes the block to animate by decreasing in size. The `transition-property` sets the transition effect to be applied and `transition-delay` sets the transition to wait based on the value set.

Add these options to the `AOS.init()` function to make the animation play once:

	AOS.init({
	  once: true
	});

The animations will now play once on scroll! Here is how it should look so far:

[![hldvndy5gvzlyhnh00s3.gif](../_resources/b3aed65e991f7524711501443455601d.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--RGYTmWfc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/hldvndy5gvzlyhnh00s3.gif)

To add this same effect to images, it is a similar process. Replace the text with an image in HTML:

	<div class="reveal-holder">
	  <div class="reveal-block" data-aos="reveal-left"></div>
	  <img src="pomeranian.jpg" alt="Pomeranian">
	</div>

To make the reveal effect slide to the left from the right, edit the `transform-origin` to 0% 100%:

	[data-aos="reveal-left"] {
	  ...
	  transform-origin: 0% 100%;
	  ...
	}

##   [(L)](https://dev.to/kathykato/creating-reveal-effects-on-scroll-31o6#animating-pseudoelements) Animating pseudo-elements

We will be using pseudo-elements to the `.reveal-block` class to create a more stylish reveal animation.

Start by modifying the CSS for the `.reveal-block` class:

	.reveal-block {
	  position: absolute;
	  top: 0;
	  width: 100%;
	  height: 101%;
	  background: white;
	}

	.reveal-block::before {
	  position: absolute;
	  content: '';
	  top: 0;
	  left: 0;
	  right: 0;
	  bottom: 0;
	  background: lightgray;
	  transition-property: transform;
	  transition-duration: 0.5s;
	}

The `::before` pseudo-element is its own element, acting like another `.reveal-block` but can be set with its own properties, such as background color or positioning.

Add a `.right` class to `.reveal-block` like so:

	<div class="reveal-block right" data-aos="reveal-right"></div>

This will help when with animating with pseudo-elements. The CSS being:

	.reveal-block.right::before {
	  transform: scaleX(0);
	  transform-origin: 0% 100%;
	}

	.reveal-block.right.aos-animate::before {
	  transform: scaleX(1);
	}

This is the result:

[![h5ej2exro7gvds0v1gq0.gif](../_resources/ab60a4da4edd2b5658927bd0460f5dcb.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--DG0CNV7b--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/h5ej2exro7gvds0v1gq0.gif)

Looks great! All that is left is to hide elements from appearing before scroll. To do this, we will add an data-aos attribute to the `.reveal-holder` class:

	<div class="reveal-holder" data-aos="reveal-item">...</div>

And the accompanying CSS:

	[data-aos="reveal-item"] {
	  visibility: hidden;
	  transition-property: visibility;
	  transition-duration: 0s;
	}

	[data-aos="reveal-item"].aos-animate {
	  visibility: visible;
	}

##   [(L)](https://dev.to/kathykato/creating-reveal-effects-on-scroll-31o6#wrapping-up) Wrapping up

Scroll-triggered animations such as block reveal effects can be an immersive and elegant interaction to reveal content. I hope this tutorial helped you learn not only how these animations are done, but also understanding what is exactly happening to make this animation work.

A live demo is available on [CodePen](https://codepen.io/kathykato/pen/PLwBez). I also created a [GitHub repository](https://github.com/kathykato/reveal-effects) with the code. Happy coding!