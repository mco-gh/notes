An intro to web components with otters – Monica Dinculescu

#   [An intro to web components with otters](https://meowni.ca/posts/web-components-with-otters/)

June 6, 2017

![everyone keeps talking about web components, but huh?](../_resources/8d0b756fb9931851e13c959ce348f21b.png)

I work on a library called [Polymer](https://polymer-project.org/), which helps you write web components faster and easier. This is awesome, but it’s only awesome if **you** (yes, YOU) know what a web component is, and know that you want to write one. So here’s a story about what these things are and teaches you how to use them without showing you 10 pages of docs and getting you to install tools and CLIs. Maybe it’s for you. Maybe it isn’t. In either case, it has otters.

- [Why should you care?](https://meowni.ca/posts/web-components-with-otters/#why-should-you-care)

- [Thinking about your app](https://meowni.ca/posts/web-components-with-otters/#thinking-about-your-app)

- [Where do web components live?](https://meowni.ca/posts/web-components-with-otters/#where-do-web-components-live)

- [Polyfills and you](https://meowni.ca/posts/web-components-with-otters/#polyfills-and-you)

- [1. I want to use someone else’s web component in my app](https://meowni.ca/posts/web-components-with-otters/#1-i-want-to-use-someone-elses-web-component-in-my-app)

    - [1. Install the web component](https://meowni.ca/posts/web-components-with-otters/#1-install-the-web-component)

    - [Status check](https://meowni.ca/posts/web-components-with-otters/#status-check)

    - [2. Import it in the app](https://meowni.ca/posts/web-components-with-otters/#2-import-it-in-the-app)

    - [3. Insert it somewhere in the app](https://meowni.ca/posts/web-components-with-otters/#3-insert-it-somewhere-in-the-app)

    - [Status check](https://meowni.ca/posts/web-components-with-otters/#status-check-1)

- [2. I want to write a web component to use in my app](https://meowni.ca/posts/web-components-with-otters/#2-i-want-to-write-a-web-component-to-use-in-my-app)

- [That’s all there is!](https://meowni.ca/posts/web-components-with-otters/#thats-all-there-is)

## Why should you care?

Web components aren’t a new library or framework, they’re a new browser feature, and they let you write *encapsulated* and *reusable*  *components* (more [details](https://www.webcomponents.org/introduction)). If you’ve ever used an `<input>` element, I like to think of it as the OG web component, because it’s exactly that. The thing is that before web components came around, you had to wait on all browsers to agree on a new element (like, a date picker). And even after they agreed on a new element, it took them yeaaaaars to implement it. `<input type="date">`was drafted in 2011 – today, 6 years later, not all browsers have implemented it! With web components, **web developers** get to write such elements, so that you don’t have to wait for 10 years before all browsers agree that they should implement a date picker. P cool, right?

- A **component** is a bunch of code that fits logically together, kinda like a unit of functionality. This could be a simple widget like a fancy button or a date picker, or a more complex UI setup like “a responsive blog layout”

- **Encapsulated** means that an element’s styles and children are scoped to itself, so you can’t accidentally break what it looks like by using CSS haphazardly in your app

- **Reusable** means that if you have a web component, no matter how you wrote it, you should be able to use it in any other app, regardless of how it’s built (eg, a React app). This is different than, say, a React component, which you can’t just use in an Angular app without bringing all of React with you

    - Using other people’s web components is nice because it means you get to write less code, and you can use someone else’s code. Also, when I say “using web components”, I literally mean writing something like `<emoji-picker></emoji-picker>`, that just works out of the box. Remember, a custom element is just an open source `<input>` – whatever you can do with `<input>` you could do with a custom element.

    - Writing your own web component is nice because splitting your app in smaller pieces makes it more manageable. Sharing your own web component with others means that they could write less code and use yours! Sharing is caring <3

![so i can write <emoji-picker>, yay!](../_resources/5f98192c002ed6d6abe6ab66a3c9c8e2.png)

You write web components in ES6 JavaScript. Polymer is a JavaScript library that’s like jQuery for web components – you import it, it gives you a bunch of helper functions and saves you writing a lot of boilerplate code.

Also, bad habit: people (and me, I am those people) tend to use “custom element” and “web component” interchangeably. If you’re pedantic, they mean different things. Don’t be pedantic, it makes the otters sad.

![sad otter because it's getting well-actuallied](../_resources/776bed541ff3a25be445f1847f855e17.png)

## Thinking about your app

If you’re starting to think about using web components in your app, there’s basically 2 situations you could be in, and I tend to reason about each differently

1. I want to use someone else’s web component in my app

2. I want to write a web component to use in my app

There’s other things that you might eventually care about, such as making your application production ready, and improving its performance. They are super important topics, but if you’ve never used a web component before, they’re also not the most important topics for you **right now**.

![is this magic? nah it's prolly just undocumented code](../_resources/eb53d41dab39cd5611e6d2823d2c96b0.png)

## Where do web components live?

![in otter space!](../_resources/659a86440f78b16752fe32f32eb8eabb.png)

Web components tend to have dependencies on other web components, so you need a package manager to herd all them cats. Most of the web components out there use [`bower`](https://bower.io/). Another popular one is [npm](https://www.npmjs.com/) – you could think of `npm` as a package manager for your server code and `bower` for your client, and it wouldn’t be entirely incorrect.

The reason why you need a package manager and not just “download this element in a zip file” is that unless that element is really simple, it might have dependencies, and they’ll have dependencies, and that’s a thing for machines and not otters. If you really don’t want to use `bower`, then you’ll have to sort out flattening your dependency tree on your own using something like `webpack`. This is not the tutorial for you.

If you look up `bower` on the web you’ll hear things like “but bower is deprecated now” (which is true, but it’s also been unmaintained for like a year and it worked fine, so nothing is really new on that front) and “but why not npm” (because you can only have one version of the same web component in your app, and that’s hard if your dependency tree is not flat. You probably don’t actually care this).

![attenshun attenshun installation instructions](../_resources/f33fb5ee9067932258c5b3edc2d1357d.png)

To [install](https://bower.io/#install-bower)  `bower`, a package manager, you must first install `npm`, a package manager. Take a moment for a concerned sigh, but install it anyway. Upshot: I promise this is the only tool I will ask you to install.

If you want to find otter web components, [WebComponents.org](https://www.webcomponents.org/) is a universal catalog of web components (but not a package manager, because that would be cray). Go check it out.

## Polyfills and you

![anotter digression](../_resources/2d081455340049e42a0973b34bdbf93e.png)

Not all browsers implement features at the same rate, which means while you’re waiting for them to catch up, you need to care about polyfills. Fun fact: you know how when you have a hole in a wall, you have to put spackling paste in it to make the wall look like a wall again? Polyfilla is a brand of spackling, and that’s exactly what a polyfill is – it fills a hole in the browser, so that it looks even from the outside.

You have two choices:

- Ignore polyfills for now and just use Chrome to test your app, but know it’s going to be hella broken on other browsers

- Care about polyfills, and include the [polyfill](https://meowni.ca/posts/web-components-with-otters/github.com/webcomponents/webcomponentsjs) in your app. Spoilers: it’s just a `<script src="some-path/webcomponents-lite.js"></script>` include.

in your applications’s `<head>` tag![whadya think? we otter get to the code!](../_resources/cdfc35b19bbe783b2a31be611e445e14.png)

## 1. I want to use someone else’s web component in my app

Ok cool, so here we are. You have a web site, and you want to use someone else’s web widget in it. Let’s say that thing is [paper-button](https://www.webcomponents.org/element/PolymerElements/paper-button) which is a super fancy looking Material Design button. It’s beauty and it’s grace, it’s Miss United States.

Here is a [glitch app](https://glitch.com/edit/#!/use-custom-element) if you want to follow along at home. Glitch is an online code editor, where you can build apps and modify other people’s – which is why it’s great for this example!

We need to do 3 things:

### 1. Install the web component

- We do this by adding a `dependency` to our `bower.json` file. If you don’t already have a `bower.json` file (who can blame you), create one by running `bower init`, and answering the wizard’s questions. They kind of look like this, though, spoiler alert: there’s no actual wizard 😭 ![screenshot of the bower init wizard](../_resources/55d24b77eeec545550fa78104e2d0a1b.png)

- To add `paper-button` as a dependency, you can either run`bower install --save PolymerElements/paper-button#^2.0.0` or by manually adding it to the `bower.json` file in its `dependencies` section:

	"dependencies": {
	  "paper-button": "PolymerElements/paper-button#^2.0.0"
	}

- Because I promised you no magic: `^2.0.0` just means “the latest version between 2.0.0 to 3.0.0”. The reason I picked that version is that it’s the latest one.

- If you manually added the element to `bower.json`, you need to actually install it, so run `bower install`.

### Status check

Right now you should have a `bower_components` folder created, that contains a whole bunch of folders, one of which is called `paper-button`.

### 2. Import it in the app

This basically tells the browser where to find the definition for what this `paper-button` tag is.

Much like how you import a CSS stylesheet with

	<link rel="stylesheet" href="/style.css">

You import a web component with an **HTML import**:

	 <link rel="import" href="/bower_components/paper-button/paper-button.html">

### 3. Insert it somewhere in the app

Drop a `<paper-button>Click me</paper-button>` somewhere in your html page.

### Status check

Your `index.html` should basically look like this:

	<!DOCTYPE html>
	<html>
	  <head>
	    <!-- Load the polyfill so that the demo works everywhere -->
	    <script src="/bower_components/webcomponentsjs/webcomponents-lite.js"></script>

	    <!-- Import the custom element so that the browser knows what it means -->
	    <link rel="import" href="/bower_components/paper-button/paper-button.html">
	  </head>
	  <body>
	    <h1>Oh, hi there</h1>
	    <p>Have you seen this fancy button?</p>

	    <!-- Use the custom element! -->
	    <paper-button>Click me</paper-button>
	  </body>
	</html>

See that line about loading the `webcomponents-lite` polyfill? That’s the bit that makes the demo work in browsers that don’t have web components yet 😎. If you want to see what your app looks like without the polyfill, just comment out that line and open your app in something like Firefox! It’s a good thing to try out.

If we run that demo, it should look like this, plus or minus some copy and styles that I’ve added:

# Oh, hi there

Have you seen this fancy button?
 Click me
 [Remix this in Glitch](https://glitch.com/)

Now, say it together with the otters!![bower summary](../_resources/643b28be8388a2e75e08b361c9464bf2.png)

You could, of course, add JavaScript to that custom element, like you would with any other `<button>` or `<input>`. I could’ve added something like this:

	document.querySelector('paper-button').addEventListener('click', function() {
	  alert('you did a click!');
	});

## 2. I want to write a web component to use in my app

Now that we know how to import someone else’s custom element, let’s write our own! Up until now we haven’t actually talked about Polymer at all. You can totally write web components *without* Polymer; you’ll just have to write a lot more boilerplate, and I don’t want that to turn you off web components.

The Polymer site actually has an awesome [getting started](https://www.polymer-project.org/2.0/start/first-element/intro) tutorial, if you’d rather read that. But while I have you here, you’ll get the otter way.

In Polymer, every custom element is like a taco (bear with me). There’s something called a `dom-module` (which is actually a custom element itself) that holds 2 things in it:

1. the `<template>`, or what your element looks like (html and css). A `<template>` is an HTML element that’s inert – when the browser sees

2. a `<script>`, which is what your element does.

**Sidebar**: This is one of the advantages of using Polymer – without Polymer, you’d have to construct all your HTML and CSS in JavaScript, and somehow add it to your custom element. Polymer makes it easier for you to point at an implementation, and at a bunch of HTML/CSS and say “that look goes with that code”.

We add all our code to an `.html` file (because remember: we’re going to do an HTML import to bring it in our app later). It ends up looking like this:

	<dom-module id="my-element">
	  <template>
	    <!-- Any CSS your element needs for styling -->
	    <style>
	      /* This is a special selector that styles the element itself */
	      :host { ... }
	      /* Use the usual CSS selectors for its children */
	      p { *color*: tomato; }
	    </style>

	    <!-- that <p> style there applies here -->
	    <p>I should be a nice red!</p>
	  </template>

	  <script>
	    // Every custom element is an ES6 class.
	    // This is the implementation of the element.
	    class MyElement extends Polymer.Element {
	      ...
	    }

	    // Every custom element needs to be registered.
	    // This tells the browser that the <happy-thing>
	    // tag uses _this_ implementation.
	    customElements.define(MyElement.is, MyElement);
	  </script>
	</dom-module>

I tend to put one element per `html` file, and then name the file after the tag of the element, so I can keep track of it. I would save that into a `my-element.html` file, and then import it in our app, just as before with:

	<link rel="import" href="my-element.html">

Now, what goes *inside* your custom element is really up to you. The way I write elements is

- by either knowing ahead of time what that element should do (“I need an emoji-picker, so it should be a text field with a button and when you click on that button, you get a list of emoji”),

- or I am working on the app, and at some point there’s just too much HTML/CSS in the same place that looks like it can just be modularized away (“oh, all this code just deals with writing a tweet, it should probably just go into a `<new-tweet>` element”)

As a slightly more complicated example, I made a `<happy-thing>` element in this[glitch app](https://glitch.com/edit/#!/polymer-custom-element) (check out the [code](https://glitch.com/edit/#!/polymer-custom-element?path=public/happy-thing.html:1:0)). It basically takes whatever content you give to it, and when you hover over, it does a little shimmy animation:

#  A <happy-thing> with ✨Polymer✨!

This is a custom element that takes an emoji and makes it happy when you hover it!

 🐶  🙈

You can technically put anything inside of it, like an input or a button!   omg!

I also made that element with [plain JavaScript](https://glitch.com/edit/#!/simple-custom-element), without Polymer, if you want to compare it. You’ll notice the second example has a lot more boilerplate code, which Polymer abstracted out for you.

## That’s all there is!

I hope this helped! Here’s some other links to get you going:

- Google developers [blog post](https://developers.google.com/web/fundamentals/getting-started/primers/customelements) on custom elements

- The Polymer [getting started](https://www.polymer-project.org/2.0/start/) tutorial

- The Polymer [quick tour](https://www.polymer-project.org/2.0/start/quick-tour) of features

- A Polymer [cheat sheet](https://meowni.ca/posts/polymer-2-cheatsheet/)

- The Polymer [docs](https://www.polymer-project.org/2.0/docs/devguide/feature-overview)

![let me know if this was useful to you! cause i'm otter here](../_resources/69635a3729b622143c95b86299d358fb.png)