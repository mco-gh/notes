Why I don't use web components

#  Why I don't use web components

###     [  [cf5f93a6-933f-4203-ac6b-40eb59a08289.webp](../_resources/eee1cbca3d999e5bfbdd67b11ff8d889.webp)  Rich Harris](https://dev.to/richharris)    [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 612 612' role='img' aria-labelledby='arcb9k84l8ple1lr3dt4nmacg7h5nm6z' class='icon-img js-evernote-checked' data-evernote-id='1353'%3e%3ctitle id='arcb9k84l8ple1lr3dt4nmacg7h5nm6z'%3etwitter logo%3c/title%3e%3cpath d='M612 116.258c-22.525 9.98-46.694 16.75-72.088 19.772 25.93-15.527 45.777-40.155 55.184-69.41-24.322 14.378-51.17 24.82-79.775 30.48-22.906-24.438-55.49-39.66-91.63-39.66-69.333 0-125.55 56.218-125.55 125.514 0 9.828 1.11 19.427 3.25 28.606-104.325-5.24-196.834-55.223-258.75-131.174-10.822 18.51-16.98 40.078-16.98 63.1 0 43.56 22.182 81.994 55.836 104.48-20.575-.688-39.926-6.348-56.867-15.756v1.568c0 60.806 43.29 111.554 100.692 123.104-10.517 2.83-21.607 4.398-33.08 4.398-8.107 0-15.947-.803-23.634-2.333 15.985 49.907 62.336 86.2 117.253 87.194-42.946 33.655-97.098 53.656-155.915 53.656-10.134 0-20.116-.612-29.944-1.72 55.568 35.68 121.537 56.484 192.44 56.484 230.947 0 357.187-191.29 357.187-357.188l-.42-16.253C573.87 163.525 595.21 141.42 612 116.257z'%3e%3c/path%3e%3c/svg%3e)](http://twitter.com/Rich_Harris)  [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='438.549' height='438.549' viewBox='0 0 438.549 438.549' role='img' aria-labelledby='amazk0vo9bfjrwh78a80htjutavd02iy' class='icon-img js-evernote-checked' data-evernote-id='1354'%3e%3ctitle id='amazk0vo9bfjrwh78a80htjutavd02iy'%3egithub logo%3c/title%3e%3cpath d='M409.132 114.573c-19.608-33.596-46.205-60.194-79.798-79.8C295.736 15.166 259.057 5.365 219.27 5.365c-39.78 0-76.47 9.804-110.062 29.408-33.596 19.605-60.192 46.204-79.8 79.8C9.803 148.168 0 184.853 0 224.63c0 47.78 13.94 90.745 41.827 128.906 27.884 38.164 63.906 64.572 108.063 79.227 5.14.954 8.945.283 11.42-1.996 2.474-2.282 3.71-5.14 3.71-8.562 0-.57-.05-5.708-.144-15.417-.098-9.71-.144-18.18-.144-25.406l-6.567 1.136c-4.187.767-9.47 1.092-15.846 1-6.375-.09-12.992-.757-19.843-2-6.854-1.23-13.23-4.085-19.13-8.558-5.898-4.473-10.085-10.328-12.56-17.556l-2.855-6.57c-1.903-4.374-4.9-9.233-8.992-14.56-4.093-5.33-8.232-8.944-12.42-10.847l-1.998-1.43c-1.332-.952-2.568-2.1-3.71-3.43-1.143-1.33-1.998-2.663-2.57-3.997-.57-1.335-.097-2.43 1.428-3.29 1.525-.858 4.28-1.275 8.28-1.275l5.708.853c3.807.763 8.516 3.042 14.133 6.85 5.615 3.807 10.23 8.755 13.847 14.843 4.38 7.807 9.657 13.755 15.846 17.848 6.184 4.093 12.42 6.136 18.7 6.136 6.28 0 11.703-.476 16.273-1.423 4.565-.95 8.848-2.382 12.847-4.284 1.713-12.758 6.377-22.56 13.988-29.41-10.847-1.14-20.6-2.857-29.263-5.14-8.658-2.286-17.605-5.996-26.835-11.14-9.235-5.137-16.896-11.516-22.985-19.126-6.09-7.614-11.088-17.61-14.987-29.98-3.9-12.373-5.852-26.647-5.852-42.825 0-23.035 7.52-42.637 22.557-58.817-7.044-17.318-6.38-36.732 1.997-58.24 5.52-1.715 13.706-.428 24.554 3.853 10.85 4.284 18.794 7.953 23.84 10.995 5.046 3.04 9.09 5.618 12.135 7.708 17.706-4.947 35.977-7.42 54.82-7.42s37.116 2.473 54.822 7.42l10.85-6.85c7.418-4.57 16.18-8.757 26.26-12.564 10.09-3.806 17.803-4.854 23.135-3.14 8.562 21.51 9.325 40.923 2.28 58.24 15.035 16.18 22.558 35.788 22.558 58.818 0 16.178-1.958 30.497-5.853 42.966-3.9 12.47-8.94 22.457-15.125 29.98-6.19 7.52-13.9 13.85-23.13 18.985-9.233 5.14-18.183 8.85-26.84 11.135-8.663 2.286-18.416 4.004-29.264 5.146 9.894 8.563 14.842 22.078 14.842 40.54v60.237c0 3.422 1.19 6.28 3.572 8.562 2.38 2.278 6.136 2.95 11.276 1.994 44.163-14.653 80.185-41.062 108.068-79.226 27.88-38.16 41.826-81.126 41.826-128.906-.01-39.77-9.818-76.454-29.414-110.05z'%3e%3c/path%3e%3c/svg%3e)](http://github.com/Rich-Harris)  Jun 20  ・7 min read

 [#html](https://dev.to/t/html)  [#webcomponents](https://dev.to/t/webcomponents)

For my first post on dev.to I thought I'd write about a nice, safe topic that's free of controversy: web components.

I'm mostly writing this for my future self, so that I have something to point to next time someone asks why I'm a web component skeptic, and why [Svelte](https://svelte.dev/) doesn't compile to custom elements by default. (It *can* compile to CEs, and it can consume CEs as evidenced by its perfect score on [Custom Elements Everywhere](https://custom-elements-everywhere.com/).)

None of this should be taken as criticism of the hard work that has been done on web components. It's possible that I have made some errors in this post, in which case I'd welcome corrections.

Nor am I saying that you shouldn't use web components. They *do* have valid use cases. I'm just explaining why *I* don't.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#1-progressive-enhancement) 1. Progressive enhancement

This may be an increasingly old-fashioned view, but I think that websites should work without JavaScript wherever possible. Web components don't.

That's fine for things that are intrinsically interactive, like a custom form element (`<cool-datepicker>`), but it's not fine for your nav bar. Or consider a simple `<twitter-share>` element that encapsulates all the logic for constructing a [Twitter web intent](https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/guides/web-intent.html) URL. I could [build it in Svelte](https://svelte.dev/repl/98aa20d4cb3d40dabfef7d8dae183b85?version=3.5.2) and it would generate server-rendered HTML like this:

	<a target="_blank" noreferrer href="..." class="svelte-1jnfxx">
	  Tweet this
	</a>

In other words, a bog-standard `<a>` element, in all its accessible glory.

With JavaScript enabled, it progressively enhances — rather than opening a new tab, it opens a small popup window instead. But without, it still works fine.

By contrast, the web component HTML would look something like this...

	<twitter-share text="..." url="..." via="..."/>

...which is useless and inaccessible, if JS is disabled or somehow broken, or the user is on an older browser.

The `class="svelte-1jnfxx"` is what enables encapsulated styles without Shadow DOM. Which brings me onto my next point:

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#2-css-in-err-js) 2. CSS in, err... JS

If you want to use Shadow DOM for style encapsulation, you have to include your CSS in a `<style>` element. The only practical way to do so, at least if you want to avoid FOUC, is to have the CSS in a string in the JavaScript module that defines the custom element.

This runs counter to the performance advice we've been given, which can be summarised as 'less JavaScript, please'. The CSS-in-JS community in particular has been criticised for not putting CSS in `.css` files, and yet here we are.

In future, we may be able to use [CSS Modules](https://github.com/w3c/webcomponents/issues/759) alongside [Constructable Stylesheets](https://developers.google.com/web/updates/2019/02/constructable-stylesheets) to solve this problem. And we may be able to use `::theme` and `::part` to style things inside Shadow DOM. But these aren't free of problems either.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#3-platform-fatigue) 3. Platform fatigue

>
>
>   ![bFyXy8Pu_normal.jpeg](../_resources/08851da3cd4332267fce0aebb0a3e084.jpg)>
>  Rich Harris
>
>  @rich_harris
>

>   ![twitter-99c56e7c338b4d5c17d78f658882ddf18b0bbde5b3f42f84e7964689e7e8fb15.svg](../_resources/c18ec23a3c01d86cfa67394e730d657b.png)>

>
>

>   > [> @calebwilliams12](https://twitter.com/calebwilliams12)>  This is a pet peeve of mine though — we've been touting this stuff as The Future for years, but in order to catch up with *the present* we need to stuff the platform to the gills with all these new features, deepening the moat around existing browsers

>
>  17:55 PM - 19 Jun 2019
>

>   > [>   [146201.webp](../_resources/be5f9b2f9fd849f43dc7b0e00c63d36c.png)> ](https://twitter.com/intent/tweet?in_reply_to=1141404066704232448)>   > [>   [fcbdfbd6-175c-4925-9454-61d1306f126c.webp](../_resources/086b96e7d4eb27889967cbcc7ba13f76.png)> ](https://twitter.com/intent/retweet?tweet_id=1141404066704232448)>  0 > [>   [29c8326d-aa86-4c6b-ae21-d092e111c7c8.webp](../_resources/29fbef58fc72d4865aa4458658d4005a.png)> ](https://twitter.com/intent/like?tweet_id=1141404066704232448)>  3

>

At the time of writing, there are 61,000 open issues on [https://crbug.com](https://crbug.com/), the Chromium bug tracker, which reflects the enormous complexity of building a modern web browser.

Every time we add a new feature to the platform, we increase that complexity — creating new surface area for bugs, and making it less and less likely that a new competitor to Chromium could ever emerge.

It also creates complexity for developers, who are encouraged to learn these new features (some of which, like HTML Imports or the original Custom Elements spec, never catch on outside Google and end up being removed again.)

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#4-polyfills) 4. Polyfills

It doesn't help that you need to use polyfills if you want to support all browsers. It *really* doesn't help that the literature on [Constructable Stylesheets](https://developers.google.com/web/updates/2019/02/constructable-stylesheets), written by a Googler (hi Jason!), doesn't mention that they're a Chrome-only feature. (The [three spec editors](https://wicg.github.io/construct-stylesheets/) are all Googlers. Webkit [seem to have some doubts](https://github.com/mozilla/standards-positions/issues/103#issuecomment-494181931) about some aspects of the design.)

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#5-composition) 5. Composition

It's useful for a component to be able to control when (or whether) its slotted content is rendered. Suppose we wanted to use the [`<html-include>` element](https://github.com/justinfagnani/html-include-element) to show some documentation from the network when it became visible:

	<p>Toggle the section for more info:</p>
	<toggled-section>
	  <html-include src="./more-info.html"/>
	</toggled-section>

Surprise! Even though you didn't toggle the section open yet, the browser already requested `more-info.html`, along with whatever images and other resources it links to.

That's because slotted content renders *eagerly* in custom elements. It turns out that most of the time you want slotted content to render *lazily*. Svelte v2 adopted the eager model in order to align with web standards, and it turned out to be a major source of frustration — we couldn't create an equivalent to React Router, for example. In Svelte v3 we abandoned the custom element composition model and never looked back.

Unfortunately this is just a fundamental characteristic of the DOM. Which brings us to...

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#6-confusion-between-props-and-attributes) 6. Confusion between props and attributes

Props and attributes are basically the same thing, right?

	const button = document.createElement('button');

	button.hasAttribute('disabled'); // false
	button.disabled = true;
	button.hasAttribute('disabled'); // true

	button.removeAttribute('disabled');
	button.disabled; // false

I mean, almost:

	typeof button.disabled; // 'boolean'
	typeof button.getAttribute('disabled'); // 'object'

	button.disabled = true;
	typeof button.getAttribute('disabled'); // 'string'

And then there are the names that don't match...

	div = document.createElement('div');

	div.setAttribute('class', 'one');
	div.className; // 'one'

	div.className = 'two';
	div.getAttribute('class'); // 'two'

...and the ones that just don't seem to correspond at all:

	input = document.createElement('input');

	input.getAttribute('value'); // null
	input.value = 'one';
	input.getAttribute('value'); // null

	input.setAttribute('value', 'two');
	input.value; // 'one'

But we can live with those quirks, because *of course* some things will be lost in translation between a string format (HTML) and the DOM. There's a finite number of them, and they're documented, so at least you can learn about them given enough time and patience.

Web components change that. Not only are there no longer any guarantees about the relationship between attributes and props, but as a web component author, you're (presumably?) supposed to support both. Which means you see this sort of thing:

	class MyThing extends HTMLElement {
	  static get observedAttributes() {
	    return ['foo', 'bar', 'baz'];
	  }

	  get foo() {
	    return this.getAttribute('foo');
	  }

	  set foo(value) {
	    this.setAttribute('foo', value);
	  }

	  get bar() {
	    return this.getAttribute('bar');
	  }

	  set bar(value) {
	    this.setAttribute('bar', value);
	  }

	  get baz() {
	    return this.hasAttribute('baz');
	  }

	  set baz(value) {
	    if (value) {
	      this.setAttribute('baz', '');
	    } else {
	      this.removeAttribute('baz');
	    }
	  }

	  attributeChangedCallback(name, oldValue, newValue) {
	    if (name === 'foo') {
	      // ...
	    }

	    if (name === 'bar') {
	      // ...
	    }

	    if (name === 'baz') {
	      // ...
	    }
	  }
	}

Sometimes you see things go the other way — `attributeChangedCallback` invoking the property accessors instead. Either way, the ergonomics are disastrous.

Frameworks, by contrast, have a simple and unambiguous way to pass data into a component.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#7-leaky-design) 7. Leaky design

This point is a bit more nebulous, but it weirds me out that `attributeChangedCallback` is just a method on the element instance. You can literally do this:

	const element = document.querySelector('my-thing');
	element.attributeChangedCallback('w', 't', 'f');

No attribute changed, but it will behave as though it did. Of course, JavaScript has always provided plenty of opportunities for mischief, but when I see implementation details poke through like that I always feel as though they're trying to tell us that the design isn't quite right.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#8-the-dom-is-bad) 8. The DOM is bad

Ok, we've already established that the DOM is bad. But it's hard to overstate what an awkward interface it is for building interactive applications.

A couple of months back, I wrote an article called [Write less code](https://svelte.dev/blog/write-less-code), intended to illustrate how Svelte allows you to build components more efficiently than frameworks like React and Vue. But I didn't compare it against the DOM. I should have.

To recap, here's a simple `<Adder a={1} b={2}/>` component:

	<script>
	  export let a;
	  export let b;
	</script>

	<input type="number" bind:value={a}>
	<input type="number" bind:value={b}>

	<p>{a} + {b} = {a + b}</p>

That's the whole thing. Now, let's build the same thing as a web component:

	class Adder extends HTMLElement {
	  constructor() {
	    super();

	    this.attachShadow({ mode: 'open' });

	    this.shadowRoot.innerHTML = `
	      <input type="number">
	      <input type="number">
	      <p></p>
	    `;

	    this.inputs = this.shadowRoot.querySelectorAll('input');
	    this.p = this.shadowRoot.querySelector('p');

	    this.update();

	    this.inputs[0].addEventListener('input', e => {
	      this.a = +e.target.value;
	    });

	    this.inputs[1].addEventListener('input', e => {
	      this.b = +e.target.value;
	    });
	  }

	  static get observedAttributes() {
	    return ['a', 'b'];
	  }

	  get a() {
	    return +this.getAttribute('a');
	  }

	  set a(value) {
	    this.setAttribute('a', value);
	  }

	  get b() {
	    return +this.getAttribute('b');
	  }

	  set b(value) {
	    this.setAttribute('b', value);
	  }

	  attributeChangedCallback() {
	    this.update();
	  }

	  update() {
	    this.inputs[0].value = this.a;
	    this.inputs[1].value = this.b;

	    this.p.textContent = `${this.a} + ${this.b} = ${this.a + this.b}`;
	  }
	}

	customElements.define('my-adder', Adder);

Yeah.

Note also that if you change `a` and `b` in the same instant, it will result in two separate updates. Frameworks don't generally suffer from this issue.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#9-global-namespace) 9. Global namespace

We don't need to dwell on this one too much; suffice it to say that the dangers of having a single shared namespace have been well understood for some time.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#10-these-are-all-solved-problems) 10. These are all solved problems

The biggest frustration of all is that we already have really good component models. We're still learning, but the basic problem — keep the view in sync with some state by manipulating the DOM in a component-oriented fashion — has been solved for years.

Yet we're adding new features to the platform just to bring web components to *parity* with what we can already do in userland.

Given finite resources, time spent on one task means time not spent on another task. Considerable energy has been expended on web components despite a largely indifferent developer population. What could the web have achieved if that energy had been spent elsewhere?

 [  [9c032011-98cb-4523-b727-9ca9a9c9a060.webp](../_resources/94cdf6a0b8df40c219d950ba89881a9d.webp)](https://dev.to/richharris)

#### [Rich Harris](https://dev.to/richharris)

I like turtles

 [@richharris](https://dev.to/richharris)  [  [3f6a64df-e503-4b40-ad89-7d4f5db3b8fa.webp](../_resources/82fc7d7179170bd29bf81d640a6cb697.png) Rich_Harris](http://twitter.com/Rich_Harris)  [  [e6bffa0e-35ca-4b80-aa39-7ad97023a2f8.webp](../_resources/43298f53fbd00b8582fd1a9a7adf1197.png) Rich-Harris](http://github.com/Rich-Harris)

 [![info-77808966a58690cfaad3e8c7923a4d78d8fab5d87e1c3f73aef7670f290eb00c.png](../_resources/cc6ee306ec75fb01d87763e512604800.png)](https://dev.to/p/editor_guide)

 [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia)

 [  [PZV6gErH.webp](../_resources/f3ab714e51cb383e71ecab4a4ef7f438.webp)     Mattia Astorino](https://dev.to/equinusocio)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/equinusocio)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/equinusocio)

 [ Jun 20](https://dev.to/equinusocio/comment/c5j0)

I'm sorry, but no, most of the points you defined are extracted from a bad usage of the technology. Then:

**1 is not true.**
You can progressive enhance web components even with js disabled.

[googlechromelabs.github.io/howto-c...](https://googlechromelabs.github.io/howto-components/howto-tabs/)

**2 is not true.**

You don't have to put all the style inside the shadow dom, only the style that should not be composable or accessibile. Just like private ts functions.

You have a lot of flexibility then. I suggest to check this and define the context of your web component.

[css-tricks.com/making-web-componen...](https://css-tricks.com/making-web-components-for-different-contexts)

Another thing, host elements are exposed and fully customizable by external css and you should work on this. Again only the private and functional/structural css should be inside the shadow tree.

[codepen.io/equinusocio/pen/vMOqBO](https://codepen.io/equinusocio/pen/vMOqBO)

CSS-in-JS is not a problem while you write real CSS and generate it inside a css file or embedd it inside a `<style>` tag. The problem of the first css-in-js tools was the fact that you had to write pseudo css json-like and put it inline. Now, any modern css-in-js solution allows you write standard css and put it inside a separated file.

**3 and 4 was true until 2018**

Right now all the modern browsers fully support the v1 spec. This mean all the webkit and chromium based browsers (including edge). No polyfill needed for modern development, and if you have to support old browsers you're probably already using polyfill for js things so what's the problem? You just choosed a new technology to develop for old browsers.

**5 is normal and it make totally sense.**

Slotted elements don't live inside the shadow-tree where you put the `<slot>` tag, they live in the light-dom, and as any html element in light dom (for example inside the document) they are rendered immediately. Web components are custom html element, if you want to add a lazy behaviour, you have to implement it for your component, like as you do it right now with any lazyload js library.

**6 This is true for the whole HTML**

These issues are related to HTML and you have them with any framework if you work with plain attributes and not on top of abstractions.

* * *

Web components are not React, Vue or Svelte components, they are not logical containers, they are true html elements that live in the document and they should be used like any other html element. Taking a web component and comparing it to an abstracted svelte component is totally misleading. They do different things.

I like sveltejs and i think it's a good framework on top of good abstraction, you don't need to write falsy things about other technologies.

##   [(L)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#im-not-here-to-tell-web-components-are-the-solution-or-that-they-are-better-than-other-tools-but-i-dont-like-content-that-compare-two-different-things-and-claim-that-one-is-totally-bad-compared-to-the-other) I'm not here to tell web components are the solution or that they are better than other tools. But i don't like content that compare two different things and claim that one is totally bad compared to the other.

Cheers!

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5j0)

 [  [1299370.webp](../_resources/eee1cbca3d999e5bfbdd67b11ff8d889.webp)     Rich Harris](https://dev.to/richharris)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Rich_Harris)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Rich-Harris)  Author

 [ Jun 20](https://dev.to/richharris/comment/c617)

Thanks for the comment. We could go back and forth for a long time saying which parts of the other's post were wrong and which were based on misunderstandings, but I'll limit myself to this: if you're saying 'this is just how it is with the DOM/HTML', then you're making my argument for me!

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c617)

 [  [83edacde-94e8-41b9-8175-be422fa8a087.webp](../_resources/f3ab714e51cb383e71ecab4a4ef7f438.webp)     Mattia Astorino](https://dev.to/equinusocio)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/equinusocio)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/equinusocio)

 [ Jun 20](https://dev.to/equinusocio/comment/c61l)

If we bring the topic at this level, you have all of these problem everywhere on the web platform, independently from the tool/framework used. React, Svelte, Vue, Angular... they all work on the web platform, they work with HTML, CSS and JS and share the same platform issues. So web components too share the same issue, but they can't be compared to what you do with React or Svelte. [As i wrote here](https://css-tricks.com/making-web-components-for-different-contexts/) web components are on a lower layer, they aren't an abstraction that generate DOM, they are HTML elements, you write real representation of the DOM (and relative issues) through new html elements, not "logical" components.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c61l)

 [![github-logo_m841aq.png](../_resources/7d2c519fa83de509063fe3cb712052b7.webp)     Josep M Sobrepere](https://dev.to/josepot)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Joseptec)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/josepot)

 [ Jun 21](https://dev.to/josepot/comment/c7a2)

Ok, so I'm a bit confused now...

If I understood what you said correctly, then you agree on the fact that web-components are just leaky abstractions built on top of other leaky abstractions, right?

Now, what you are saying is that they can't be compared with React or Svelte, because React, Svelte, Vue... do provide non leaky APIs that "hide" the platform by treating it as an implementation detail.

So, the aim of JS Component libraries is to make "the platform" an implementation detail, because we want non broken abstractions. We want to have clean contracts that allow us to encapsulate functionality, so that we can have composable and reusable things to work with, without having to worry too much about the leaky web-platform. That's (at least in part) why JS Component libraries were created, right?

But then the platform became jealous because we were "hiding" it. So one day it came out and said:

> Wait a second! I see that you like to encapsulate functionality and stuff, right? But you don't have to ignore me for doing that! Please, let me create another leaky abstraction for you... Let's call it web-components! Now, please, please, please do not compare them with those things that hide my flaws. Just accept the fact that I'm broken and that I can only produce broken stuff. Just love my new broken abstraction as it is, ok? We all have flaws...

I think that I get it now. You have more compassion for the web-platform than I do. You feel sorry for it.

I have to say that I really respect your unconditional love towards the platform! But I don't share that feeling, at all.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c7a2)

 [  [11105e31-a564-4990-b7dc-e0c70440c2a9.webp](../_resources/e9ca33ccb3d38cfced0d85e186859bb7.webp)     PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 21](https://dev.to/paulmaly/comment/c6gg)

***1 is not true.***

We can't render WCs on the server and WCs not work without JS enabled. Do you ever try to create an isomorphic (universal) web app using WCs? It's the hardest part even if you work with some framework on top of this.

Also, there are many problems with forms, focus/selection, SVGs, etc.
***3 and 4 was true until 2018***

A problem that polyfills are not the same. One thing when you need to polyfill a simple feature or maybe transpile some new language features. But WCs polyfills always worked bad because this's a thing which hard to polyfill properly. Modern browsers are great and I really love that they're supported WCs well, but we'll ***never*** get rid of old browsers.

A simple example close to me - how often you're changing your TVs? Not so often than your phone, right? Our company working with TVs and I know that most TVs in the world (I'm talking about smart TVs of course. Today it's tricky to buy a TV without this feature) comes from 2014-16 years. There are no updates, so seems we'll live with these devices a long time.

***5 is normal and it make totally sense.***

It makes sense but bad DX. In Svelte 2 we had many problems with this ***standard*** behavior.

***6 This is true for the whole HTML***

True and it's hard to reconcile with it. HTML is really old standard and it was created in a time when no one could ever imagine how we'll use it. Constraints of HTML is the weakest part of WCs.

Writing a whole web app using WCs is too hard and even impossible nowadays. Actually, it's not a choice ***frameworks vs WCs***. The main idea to use WCs as additional HTML elements inside of frameworks templates and it's good. We can name it ***leaf-components*** or just ***html tags***. Btw, because of Svelte uses ***html-first*** approach, it's very simple and convenient to use WCs in Svelte apps. The main problem today is the majority of existing WCs right now depending on Polymer and it's an ecosystem.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6gg)

 [  [8a28674d-0446-466d-aa60-9ffb528fd940.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6gp)

- 1 You can serve both Custom Elements and built-in extends with the server
- 3 and 4 are covered by my polyfills that work even on those TVs
- 5 can be easily simplified
- 6 you can have tiny abstractions on top and solve most things.

Everything is described in here:

[gist.github.com/WebReflection/71ae...](https://gist.github.com/WebReflection/71aed0c811e2e88e3cd3c647213f0e6c)

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6gp)

 [  [4a401302-d733-4f81-87a1-09b5f88c2279.webp](../_resources/e9ca33ccb3d38cfced0d85e186859bb7.webp)     PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 21](https://dev.to/paulmaly/comment/c6j8)

1) Actually, I've no idea what is ***heresy***, but I already read your article. There you show up a very simple case where whole component html representation could be rendered using just props (data-attributes). It's nice, but real cases of web app and especially isomorphic web apps are harder to implement in this way.

WCs logic can be smeared in the whole component. We can't execute WC on the server without some kind of DOM emulation or without using stuff like Headless Chrome (prerender). All these solutions work not really performant.

For example, Svelte, because it's a compiler, can calculate most of the things in buildtime and in SSR mode just concatenate the strings which are very efficient.

3, 4) Perhaps your polyfills work great, but I've used official WC polyfills by Google and it work awful.

5) Your example still too simple to agree with your ideas. Even if we leave DX to the side, in Svelte 2 we lived without ***scoped slots***. So we couldn't bound some parent component state to the slot without proxying it through a top-level component. It was making really complicated creation of the composition of components which should work as one, like Tabs or similar, because of common logic for switching tabs should be in the parent component, but styles and hide/show logic inside each tab component. I mean markup like this:

	<Tabs>
	  <Tab>Tab 1</Tab>
	  <Tab>Tab 2</Tab>
	  <Tab>Tab 3</Tab>
	  <Panel>Tab 1 Content</Panel>
	  <Panel>Tab 2 Content</Panel>
	  <Panel>Tab 3 Content</Panel>
	</Tabs>

It's impossible to implement something similar in WC without manual manipulating a slot contents. Check this example: [googlechromelabs.github.io/howto-c...](https://googlechromelabs.github.io/howto-components/howto-tabs/) It's a exact nightmare.

With ***scoped slots*** we can pass a part of the state of component to the child components to give a signal which tab is active now. But unfortunately, WCs doesn't support ***scoped slots*** as any other kind of communications between parent and slotted (child) components except direct DOM manipulations which are awful.

6) What do you mean ***tiny***? Lit-html weight is 3.5Kb which is whole Preact. Lit-element already 6.8Kb. Is it still a tiny? Heresy - 8.3Kb, Haunted - 5.1Kb. All gzipped. Are we still talking about ***tiny abstractions*** or about frameworks? All these libs based on WCs, so seems most of the work already done, but why they're weighted so damn much? Things like Preact or AppRun includes whole components system but their weight comparable. All these WCs based solutions just solve WCs problems, so seems there're just tons of these problems probably.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6j8)

 [  [173813.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6jd)

1) heresy-ssr is the serer side isomorphic version of heresy. I've been there already with hyperHTML and viperHTML, one of the fastest Hacker News PWAs, if not the fastest, is in viperHTML

3, 4) there is no official polyfill, only one polyfill promoted more than others. The fact Google AMP project itself used my polyfill should already put an end to "the official polyfill" meme: all Custom Elements based projects that succeeded from 2014 used my poly, 'cause it's more compatible, and lighter, and it polyfills builtin extends too.

5) you don't need scoped slots to achieve that, not sure why that use case has to be complicated at all.

6) my libraries have multiple versions: fully polyfilled so no extra anything is needed, only for latest browsers, with ES5 compatible syntax, with polyfills fallbacks to vaporware (the whole ungap.github.io story).

The only reason *my* libraries are around 5K, but heresy wraps them with extra goodness, which nicely fits in ~2.5K, is that my libraries comes without string attached: all browsers are compatible out of the box, including old mobile, old IEs, etc.

If I could drop every single trick used to fix MS Edge or IE issues, the Safari and Firefox gotcha with Template Literals, and all other quirks I had to fix for every browser here or there, the size would be more like 3K, but then again, as long as any helper that can be used to create with ease tons of components, without ever repeating common patterns, I'm ok in shipping everything included in about 10K and call it a day: that's sill 1/6th of React, if I remember correctly, and the more browsers evolve and fix their internal issues or vanish (IE, MSEdge), the smaller and faster my libraries will become.

On top of that, my libraries requires zero tooling to work via plain standards, that means teams can use these at any time, no toolchain requirements, and I've been in enough teams in my 20 years of programming to value this part almost more than anything else.

Add simplicity, performance, and pretty much everything based on standards, except when it's more convenient doing alternatively, you have the reason my libraries are 5 to 8K, and my poly 1 to 2K. That's the entire payload to unleash all the things the Web platform could do, and beyond (see heresy-ssr, which on cold start, which is the only first time a new template is encountered, is not super slick, but after that, rendering time goes around `0.03` milliseconds, so it's pretty damn good).

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6jd)

 [  [32768.webp](../_resources/e9ca33ccb3d38cfced0d85e186859bb7.webp)     PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 21](https://dev.to/paulmaly/comment/c72c)

1) Ok, so, how you render ShadowDOM on server-side?
3, 4) Maybe I just missed it. Could you please share a link to your polyfill?

5) Could you please describe how can I use WCs to implement these Tabs without scoped slots and manual dom querying in slotted content? I really want to enjoy your solution.

6) Seems, now I know why I not heard about ***heresy***. I see the first release was in April. If it's good as you describe, it should become really popular. So, let's give it some time and will get in touch later to discuss it. ;-)

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c72c)

 [  [87d3bad7-5cb7-43ed-8b87-9d7e981b6096.webp](../_resources/e7c1c68e938a931a88a4e8c738dab578.webp)     Junk](https://dev.to/oenonono)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Oenonono)

 [ Jun 21](https://dev.to/oenonono/comment/c6pm)

I assure you that we will be rid of old browsers one day. People said this about IE 5 and IE 6 and when was the last time you supported IE 8?

IE is the slowest to fall out of usage, but eventually it does. Every. Single. Time.

There are plenty of real problems, no need to grasp at straws.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6pm)

 [  [68a0c3f9-ffaf-4e9b-a826-682af4181bd5.webp](../_resources/e9ca33ccb3d38cfced0d85e186859bb7.webp)     PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 21](https://dev.to/paulmaly/comment/c71b)

I believe you missed my point about TVs. If someone bought TV in 2017 he'll change it after 10 years, maybe later. So, we'll need to support it in the next 8 years. It's called *never*.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c71b)

 [![](../_resources/e7c1c68e938a931a88a4e8c738dab578.webp)  Junk](https://dev.to/oenonono)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Oenonono)

 [ Jun 22](https://dev.to/oenonono/comment/c7c7)

What? That doesn't make even the slightest bit of sense. Are you saying 10 years is "never"?

It's clearly 10 years.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c7c7)

 [  [0c944c45-d834-4b24-85eb-53c4da3901cd.webp](../_resources/e9ca33ccb3d38cfced0d85e186859bb7.webp)     PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 22](https://dev.to/paulmaly/comment/c7no)

I mean, 10 years ago we didn’t know what’s SPA, nor Angular, WCs was no trace yet. After 10 years WCs may not be already. 10 years is infinity for web development.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c7no)

 [  [1c43b95c-73c5-4d4c-8e37-e5a33d5b3526.webp](../_resources/e7c1c68e938a931a88a4e8c738dab578.webp)     Junk](https://dev.to/oenonono)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Oenonono)

 [ Jun 23](https://dev.to/oenonono/comment/c896)

Your perspective is valid, but not complete. Look wider. In 2009 there were things like SPAs, it just wasn't as formalized and the term just wasn't coined yet.

I've been doing web development for 20 years. My career has not been two times infinity years long. If it had I'd think you'd listen to me about this. I'd be effectively God.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c896)

 [  [ce5e2a56-ae8d-496d-af16-683cc57d2f9a.webp](../_resources/470870430eb2146e8c107cfd62bed94b.webp)     John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c5ph)

This says it better than I did yesterday. Thanks.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5ph)

 [  [4de82561-ff1c-41fc-ad1d-4f3d95f5772f.webp](../_resources/f3ab714e51cb383e71ecab4a4ef7f438.webp)     Mattia Astorino](https://dev.to/equinusocio)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/equinusocio)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/equinusocio)

 [ Jun 20](https://dev.to/equinusocio/comment/c601)

Do you have a link?

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c601)

 [  [462a72fc-3e33-4bcd-be4e-3a4b016e16c4.webp](../_resources/470870430eb2146e8c107cfd62bed94b.webp)     John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c60c)

Started here in Twitter land [twitter.com/Rich_Harris/status/114...](https://twitter.com/Rich_Harris/status/1141186166089244674?s=09), and of course ballooned from there.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c60c)

 [  [fa392b61-cc0d-44d0-a823-a11b071daab5.webp](../_resources/f7366ed29a3f8434fd1626d275af8dba.webp)     Michael J. Ryan](https://dev.to/tracker1)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/tracker1)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/tracker1)

 [ Jun 20](https://dev.to/tracker1/comment/c64h)

I actually don't mind the object/json style syntax so much... I use react-jss via material-ui mostly, and that generates the appropriate stylesheet and adds it to the header. I've played with abstracting it out, but including it in the JS payload works for the applications (not public sites) that I mostly work on.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c64h)

 [![f451a206-11c8-4e3d-8936-143d0a7e65bb.png](../_resources/5c4e350d0bff761727662a75e9b0c310.jpg)     Ben Halpern](https://dev.to/ben)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/bendhalpern)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/benhalpern)

 [ Jun 20](https://dev.to/ben/comment/c5lb)

For some more interesting discussion, this is a good thread:

 [ ![f451a206-11c8-4e3d-8936-143d0a7e65bb.png](../_resources/e8580ce5a0e18779c78cabfe67786e27.jpg)](https://dev.to/ben)  [  ## Why the React community is missing the point about Web Components    ### Ben Halpern ・ Nov 7 '18 ・ 1 min read      #webdev  #webcomponents  #bestofdev  #javascript](https://dev.to/ben/why-the-react-community-is-missing-the-point-about-web-components-1ic3)

(The title is me reporting on the sentiment of others, I haven't necessarily made up my mind on all of this)

[@dan_abramov](https://dev.to/dan_abramov)'s comment:

 [![f46e43c2-f4f0-4787-b34e-a310cecc221a.jpg](../_resources/cbb2831d6e44d62f8e3af50ba0cf8161.jpg)](https://dev.to/dan_abramov)  [Dan Abramov](https://dev.to/dan_abramov)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/dan_abramov)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/gaearon)

 [Nov 7 '18](https://dev.to/dan_abramov/comment/6kdc)

A few quick points from my perspective. (I work on React.)

1. We're not opposed to supporting web components better. The problem is that there's no single "web component community". There are multiple subcommunities. You mention "web component libraries" in the post. These libraries don't agree on a single standard so React would need to pick a side in debates like "how does server rendering work with web components". Whatever we pick will have large downstream effects, and our reluctance to support more has to do with being *careful* (see [1] note below) about the semantics — not somehow being at odds with web components per se.

2. As I mentioned in the previous point (and you mentioned in the post), there are multiple "web component libraries". As far as I can see many of the criticisms of React would apply to such libraries as well. I don't think the way to counteract "DOM FUD" is to introduce "library FUD". If you're using a library for defining and updating your web components declaratively, you're not following a conceptually different approach from using React.

3. Saying "you can do everything with WCs that you can do in React" is double edged. Yes, of course, you can do anything — because we haven't actually agreed upon any constraints. If the constraint is "you don't use a React-like library on top" I think you'll find there's plenty of things that are very hard to do with an imperative abstraction like vanilla WC APIs. We've done a few talks about what using React as a unifying abstraction lets us do (such as non-blocking rendering, or dynamically loading UI code without degrading user experience). You might want to check them out ([youtube.com/watch?v=nLF0n9SACd4](https://www.youtube.com/watch?v=nLF0n9SACd4), [youtube.com/watch?v=ByBPyMBTzM0](https://www.youtube.com/watch?v=ByBPyMBTzM0)). Of course, you *can* do these things if you use a library like React on top of WCs. But that negates the argument that you don't need React-like libraries for this.

To sum up: we'd be happy to support WCs better in React. We don't want to rush it, and want to make sure this support is well thought-out. Additionally, we believe there are many things that raw imperative WC APIs don't give you — and for them something like React would be appropriate even in a WC world. Finally, there's this myth going around that once you write React code, you can't reuse it as web components. That's not true — and as you can see from the documentation it's a few lines of code: [reactjs.org/docs/web-components.ht...](https://reactjs.org/docs/web-components.html#using-react-in-your-web-components)

Hope that makes sense, and provides some additional context!

> [1]: For example, if I'm not mistaken, the semantics chosen by Preact make introducing a new standard property to DOM base element potentially a breaking change for the web. We try to avoid such problems if possible — precisely because React *> did*>  learn from MooTools and we don't want to do another mistake like what happened with `Array.prototype.flatten()`> .

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5lb)

 [  [92d6b6d1-4d69-46fb-ae22-d6fd1501bef8.webp](../_resources/8a2271326b1320ef6651b2042584094f.webp)     aaron hans](https://dev.to/nopatternaaron)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/nopatternaaron)

 [ Jun 20](https://dev.to/nopatternaaron/comment/c5k9)

This is a good article and I love your work on svelte and with the NY Times.

I got interested in Web Components when working at a large company maintaining several web applications built with different frameworks. It was fun to be able to create separate, lightweight components that could upgrade pieces of different applications without taking on the responsibility of rewriting too much at a time. When we used Web Components we skipped the shadow DOM because of some issues with forms that cross the light and shadow barrier and the weight of the shadow DOM polyfill. We namespaced our component's CSS rules by prefixing them with the custom element name during a build step. Skipping the shadow DOM also allowed us to do server side rendering of our web components relatively easily using jsdom on an AWS Lambda.

I currently use Web Components at a small startup where we create a search widget government websites embed into their pages. We can deliver a small code footprint which encapsulates a ton of functionality with easy integration steps that supports browsers down to IE11.

Neither of these cases refute your points but they are common examples where Web Components shine.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5k9)

 [  [f8b11ec7-6fda-48e3-91c0-087cdfc894c2.webp](../_resources/eee1cbca3d999e5bfbdd67b11ff8d889.webp)     Rich Harris](https://dev.to/richharris)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Rich_Harris)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Rich-Harris)  Author

 [ Jun 20](https://dev.to/richharris/comment/c61c)

Thank you — yep, there are definitely cases where they shine. It's interesting that you had those issues with shadow DOM — in the early days, shadow DOM was kind of the whole point of web components, but I've seen a lot of people back out for similar reasons. Now we see long-running debates about where and whether to use shadow DOM, and whether a given thing belongs in shadow DOM or light DOM. Feels like that distinction has created a lot of extra complexity.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c61c)

 [  [70d09b60-c2f5-4542-8d57-8e849a7bace7.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6h3)

Shadow DOM is controversial because it plays bad with SSR, and its polyfill is not really specs compliant.

To style Custom Elements you also don't need anything different than you do already, and surely you don't need Shadow DOM at all to have Custom Elements.

Maybe Shadow DOM was sold as the true Web Components must do magic, but since 2014 I've never used it, and never needed it.

We ship Custom Elements to dozen million users, and we never used once `attachShadow`.

*TL;DR* the debate about Shadow DOM is pretty simple: don't use Shadow DOM if you target legacy browsers without native Custom Elements V1 support, or use very constrained and simple variants of the spec, like the `attachshadow` library that works down to IE9.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6h3)

 [![](../_resources/e7c1c68e938a931a88a4e8c738dab578.webp)  Junk](https://dev.to/oenonono)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Oenonono)

 [ Jun 21](https://dev.to/oenonono/comment/c702)

Shadow DOM is my favorite part, despite its problems. Custom Elements are just interface for me. I get so much use out content distribution. It's the most important part other than style scoping.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c702)

 [![f451a206-11c8-4e3d-8936-143d0a7e65bb.png](../_resources/5c4e350d0bff761727662a75e9b0c310.jpg)     Ben Halpern](https://dev.to/ben)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/bendhalpern)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/benhalpern)

 [ Jun 20](https://dev.to/ben/comment/c5kl)

I agree with a lot of this, but also feel like the jury is still out on some of it as well. My approach, luckily, is to wade in shallow water and see where things go. I would be nervous about getting too deep into webcomponents.

Though I know this is bound to create debate.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5kl)

 [  [e3673320-9042-4066-aef3-d5704daa2681.webp](../_resources/efab7cfc04aefc1992e41a65bed32998.webp)     Steve Belovarich](https://dev.to/steveblue)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/iplayitofflegit)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/steveblue)

 [ Jun 20](https://dev.to/steveblue/comment/c64c)

I agree with some of the points here about WC implementation but I don’t agree with the presentation.

3) is irrelevant. Spec is and should be a living document so naturally we’ll have to change as spec changes. We should be critical of spec. There is an opportunity to change because it is a living document.

4) I haven’t used a tool in the past decade that didn’t require a polyfill at one time or another. It’s true browsers should implement custom elements uniformly and they don’t, including custom elements v1. Browser vendors could definitely get better at this. I don’t think this argument holds weight if literally any level of sophistication in web development requires a polyfill.

10) Yes, but the nasty side effect is multiple component models leads to division in the greater web community. That’s a problem we don’t talk about enough. We have an opportunity to learn and grow together but can’t when everyday a new library comes out. So instead of Platform fatigue we end up with JavaScript fatigue. I’m not talking about Svelte necessarily, I actually think Svelte is a novel reaction to other JS libraries. The other side effect is no one bothers to learn DOM or vanilla JS because at an early stage in their education they become reliant on the popular JS library. That’s not good for anyone. We end up with a ton of engineers who don’t know how things work under the hood.

8) is so reductive I don’t know where to start. If DOM is bad, then why go into web development? We should just stop everything. Everyone go home. DOM is bad.

Web Components IMHO should have a framework wrapper to make problems like you talk about go away. That doesn’t make them bad, that is the function of every JS library. Make DOM easier to work with. No news there.

Rich, instead of bashing technologies like this perhaps it’s better for everyone if you extol the virtues of Svelte in a context that does address the limitations of DOM, but please frame it in a way that is less divisive.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c64c)

 [  [ec8bdcd8-598c-4204-97af-d2a15a4b5525.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6h8)

> Web Components IMHO should have a framework wrapper
I guess that's Polymer, but they kinda failed at selling WCs too.

My approach is still Custom Elements based (no umbrella, just the juicy bit), and tiny wrapper to simplify every task mentioned in here.

You can find more [in this gist of mine](https://gist.github.com/WebReflection/71aed0c811e2e88e3cd3c647213f0e6c)

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6h8)

 [![](../_resources/efab7cfc04aefc1992e41a65bed32998.webp)  Steve Belovarich](https://dev.to/steveblue)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/iplayitofflegit)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/steveblue)

 [ Jun 21](https://dev.to/steveblue/comment/c6hc)

I made a feeble attempt here too.
[readymade-ui.github.io/readymade/](https://readymade-ui.github.io/readymade/)

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6hc)

 [  [19f46f30-366f-4dfa-8d9f-9a2f0cb9426d.webp](../_resources/59d72902cb0b5dda2ccbdd535875b511.webp)     rhymes](https://dev.to/rhymes)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/rhymes_)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/rhymes)

 [ Jun 21](https://dev.to/rhymes/comment/c6mp)

what about Stencil?

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6mp)

 [  [aa94bd6f-f69d-4ee3-960b-6d5967f0f717.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6o1)

The moment you need tools to make anything work at all, it's the moment you are already far away from Web standards, and you are allowed to do whatever you want, like in Svelte, and other libraries, case.

Stencil One does not compete with standards anymore, rather with React/JSX, IMHO.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6o1)

 [  [feaf3d88-7357-4f1f-8a80-a386d106c2ca.webp](../_resources/59d72902cb0b5dda2ccbdd535875b511.webp)     rhymes](https://dev.to/rhymes)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/rhymes_)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/rhymes)

 [ Jun 21](https://dev.to/rhymes/comment/c6o4)

Isn't Stencil just a layer on WebComponents, like Polymer?

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6o4)

 [![twitter-logo-silhouette_1_letrqc.png](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6o6)

not at all [infoq.com/news/2019/06/stencil-ion...](https://www.infoq.com/news/2019/06/stencil-ionic-web-component-1.0)

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6o6)

 [  [7d408f4c-6cbc-43f6-8861-3ef917e4bd25.webp](../_resources/efab7cfc04aefc1992e41a65bed32998.webp)     Steve Belovarich](https://dev.to/steveblue)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/iplayitofflegit)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/steveblue)

 [ Jun 21](https://dev.to/steveblue/comment/c70d)

Stencil is the best option by far for design systems.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c70d)

 [  [92d6b6d1-4d69-46fb-ae22-d6fd1501bef8.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c710)

I'd give [heresy](https://github.com/WebReflection/heresy/#readme) a chance too, it works out of the box on client/SSR and since it needs zero real DOM to work, it might easily end up on NativeScript or similar too

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c710)

 [  [4905cc43-82e8-452f-85b2-740c6a14cb1c.webp](../_resources/59d72902cb0b5dda2ccbdd535875b511.webp)     rhymes](https://dev.to/rhymes)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/rhymes_)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/rhymes)

 [ Jun 21](https://dev.to/rhymes/comment/c713)

The article keeps saying Stencil compiles to Web Components, that's what I meant

Yeah it's more than that but the final product is WC.
Anyway, frontend has so many tools

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c713)

 [  [default_profile_4.webp](../_resources/eb9fd48266850719a85346e22c41ea03.webp)     Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c71c)

[![g48eglda4sqbh8jzktq2.png](../_resources/ea1f4f214b631e042abb3cc39ffd0610.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--LYCpIBfr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/g48eglda4sqbh8jzktq2.png)

almost nothing you see in that definition is standard:

- decorators are not there yet
- `@Prop() first: string;` makes literally no sense on JS
- the JSX return in the render also makes no sense

Stencil One is basically the most hybrid thing of them all, and once it compiles to "standrd JS", it needs a global `defineCustomElements` to be useful at all.

One can't really ship portable components like this, or can they?

The good news, is that it might target also NativeScript or similar platforms (I'd imagine React native, due JSX in the render), but the bad one is that Stencil One is far away from being a standard based way to develop anything, 'cause it needs, for those parts, mandatory toolchain that is not part of standard Web development.

I hope I've clarified a bit more, happy to answer further, if necessary.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c71c)

 [  [72610a92-2685-423b-9cc8-2c5d06895b17.webp](../_resources/59d72902cb0b5dda2ccbdd535875b511.webp)     rhymes](https://dev.to/rhymes)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/rhymes_)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/rhymes)

 [ Jun 21](https://dev.to/rhymes/comment/c72h)

> I hope I've clarified a bit more, happy to answer further, if necessary.

Ok got it, I thought that Stencil's output was just pure web components, that's it.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c72h)

 [  [9cdf4927-8e13-4628-a68a-56c140cdb220.webp](../_resources/470870430eb2146e8c107cfd62bed94b.webp)     John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c5pm)

This sounds so much like a framework author saying mine is better, web component and their libraries don't measure up. Again, this points to turf more than facts. Why feel the need to throw trash in someone else's backyard, while praising your own. I've said that svelte addresses solutions be it in it's own way. If you like it, use it. And I make that recommendation sincerely. Not with "I'm not saying you shouldn't use web components, but here's why they're a bad solution.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5pm)

 [   Rich Harris](https://dev.to/richharris)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Rich_Harris)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Rich-Harris)  Author

 [ Jun 20](https://dev.to/richharris/comment/c61h)

The headline of this post is 'Why I don't use web components'. And I clearly say that I'm explaining my personal choices. But sure — if you don't think the substantive criticisms I've raised are important, then I'm not going to waste energy trying to change your mind.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c61h)

 [   John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c61k)

Okay, Rich.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c61k)

 [   Jonathan Speek](https://dev.to/jonathanspeek)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/JonSpeek)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/JonathanSpeek)

 [ Jun 20](https://dev.to/jonathanspeek/comment/c5nk)

I'm genuinely curious what others are using to solve the real world problem of consuming a design system's components in existing applications that are in various tech stacks? Suppose you're building components to be used in Angular, React, Vue, [whatever hot new framework].

Are you using Stencil to build Web Components? Is Svelte viable?

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5nk)

 [   John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c5pf)

I think a major point is that web components are low level API that are unconcerned about where they live. At least with LitElement based web components that we've built. I can't speak for every method used to create them because I believe lit-element and lit-html were built with the goal of eventually making those libraries unnecessary as more gaps get filled in browser specs.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5pf)

 [   Ryan DeBeasi](https://dev.to/rdebeasi)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/rdebeasi)

 [ Jun 20](https://dev.to/rdebeasi/comment/c60d)

I'm super curious about this as well.

A few months ago, I worked on a design system project where we faced this question and decided to focus on CSS only, at least to start. We followed [Bulma](https://bulma.io/)'s example and instructed developers to add classes like `is-active` or `is-loading` using a framework of their choice. More complicated functionality will probably require web components or something similar - think data tables, date pickers, etc. - but vanilla CSS isn't a bad place to start.

Here are some examples of what other design systems are doing:

- Salesforce's Lightning Design System [uses web components](https://developer.salesforce.com/docs/component-library/documentation/lwc/lwc.get_started_introduction) alongside its own component system.
- The developers of Red Hat's PatternFly [decided to focus on React](https://blog.patternfly.org/patternfly/js-framework-for-patternfly-4/) after [experimenting with web components](https://developers.redhat.com/blog/2016/08/09/are-web-components-in-the-future-for-patternfly-2/). I think the PatternFly web components may have become the basis for [RHElements](https://rhelements.github.io/).
- [Material Components for Web](https://material.io/develop/web/) is built on (web components) CSS and vanilla JavaScript. It just left beta in March. There are [Material Design implementations](https://material.io/collections/developer-tutorials/#) for Java, Swift, Web, Angular, etc.
    - Edit: This design system uses vanilla JS. The [web component implementation](https://github.com/material-components/material-components-web-components) of Material Design components is still a work in progress.
- IBM's [Carbon Design System](https://www.carbondesignsystem.com/getting-started/developers/vanilla) offers implementations in React, Vue, Angular, and vanilla JS. The vanilla JS version looks a bit like Bootstrap's JS implementation; it doesn't appear to use web components.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c60d)

 [   Jonathan Speek](https://dev.to/jonathanspeek)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/JonSpeek)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/JonathanSpeek)

 [ Jun 20](https://dev.to/jonathanspeek/comment/c60m)

Carbon looks to be [experimenting](https://github.com/carbon-design-system/carbon-custom-elements)

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c60m)

 [   Steven Vachon](https://dev.to/stevenvachon)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/stevenvachon)

 [ Jun 21](https://dev.to/stevenvachon/comment/c731)

I think you're approaching web components from the wrong perspective. They are not yet complete and as such are not yet suited for architecting a vanilla application. They are, however, very useful in small, reusable cross-framework libraries.

I'll address each of your points:

1. How much progressive enhancement do you need when the app's JS is either not available (disabled) or still being downloaded? I think that CSS' `:defined` pseudo-class is sufficient for styling the light tree of an element that has—or will have—a `shadowRoot`. You can also use a fallback design such as `<select is="super-list">`.

2. What "problems" does `::part()` have?
3. Um, yeah, let's not move the web platform forward. Drivel.

4. No one said that you should use web components for a project that supports IE9/etc. You'd have a ton of polyfills already for that target and probably terribly outdated CSS practices if not using terrible CSS polyfills.

5. Using existing web components today would still require some form of a wrapper to nicely handle data wiring, and with that, you'd probably have something to handle templating. In which case, this point is a non-issue.

6. You don't have to write components this way, but it is nice and complete to be consistent with standard elements. See my thoughts at the very top of this comment.

7. Maybe it will support private methods when that proposal is stage 4. Not a big deal.

8. See my thoughts at the very top of this comment.

9. I can see how this could be an issue for architecting an application. However, see my thoughts at the very top of this comment.

10. They're solved with tools that are not part of an official specification which serves the entire web community. Such frameworks serve opinionated sub-communities. The web component specification has always been taking the best ideas from these frameworks and will continue to do so until we no longer need any of them.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c731)

 [![3b77b692-a6c9-4664-b042-68c3f573880b.jpg](../_resources/c092bb1aa32ca9bde0be23fb698f4514.jpg)     Ferit](https://dev.to/fokusman)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/FokusMan)

 [ Jun 20](https://dev.to/fokusman/comment/c5je)

Isn't the push for Web Components mainly coming from one big browser vendor as some sort of "owning the web", as now developers moved on to non-Google tooling ?

I have the observation that the push for some web standards is also a commercial one. If only Chrome moves heavily into that direction and the rest (safari, firefox) is doing it more cautiously we will end up again in a weird situation where:

- Hype driven developers produce applications only for Chrome,
- the rest is getting "Move to Chrome" Banners...

It is not proven by data, yet I see many non-googlers sharing doubts about WC vs. Googlers talking about it as the "only good solution".

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5je)

 [   Mattia Astorino](https://dev.to/equinusocio)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/equinusocio)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/equinusocio)

 [ Jun 20](https://dev.to/equinusocio/comment/c5k7)

This is a widley discussed spec. Chrome was just the first vendor implementing the spec v0 and made polyfills. Other vendors refused to implement a draft spec and they all waited for the v1. Now is widely accepted and implemented. No one forced people to use web components v0 or polymer...

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5k7)

 [![3b77b692-a6c9-4664-b042-68c3f573880b.jpg](../_resources/c092bb1aa32ca9bde0be23fb698f4514.jpg)     Ferit](https://dev.to/fokusman)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/FokusMan)

 [ Jun 20](https://dev.to/fokusman/comment/c5md)

As I argued,

If a big Browser vendor who owns the biggest search engine, has one of the largest resources and blogs to push topics, pushes it, people will jump on that.

I used worked on multiple projects in the past with shadow dom v0 , native WCs and polymer.

Developers (Humans) are as much as everyone bound to their Bias, FOMOs etc. so it is not about actively forcing but passively pushing. I think you just undervalue the power of influence and hype in developer communities.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5md)

 [   Mattia Astorino](https://dev.to/equinusocio)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/equinusocio)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/equinusocio)

 [ Jun 20](https://dev.to/equinusocio/comment/c5na)

I think hype is just a question of self-control. But you're right, not everyone can remain outside the hype-loop

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5na)

 [   Dmitrii 'Mamut' Dimandt](https://dev.to/dmitriid)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/dmitriid)

 [ Jun 20](https://dev.to/dmitriid/comment/c5p8)

Including Google themselves. They re-implemented the whole of Youtube with v0 spec which now causes problems in some browsers.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5p8)

 [   Alan Dávalos](https://dev.to/alangdm)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/alangdm)

 [ Jun 21](https://dev.to/alangdm/comment/c6bc)

This is no longer true, youtube has already migrated to Polymer v3 which is based on the v1 web components standards so it no longer has any problems with the latest versions of all browsers (except edge but that's already not a problem as long as you use the chromium-based build)

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6bc)

 [   John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c60o)

If Google had that much "push" we'd still be using HTML Imports. There's no Google conspiracy, and getting agreement to ship a change is daunting, it's open to public comments and suggestions.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c60o)

 [   Junk](https://dev.to/oenonono)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Oenonono)

 [ Jun 21](https://dev.to/oenonono/comment/c705)

No. Specifications only become recommendations when MULTIPLE VENDORS implement them.

Every major browser vendor gave input to and agreed to Web Components.

The web community and web standards have been working on how to allow developers to extend HTML for at least 20 years.

That is what Custom Elements are.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c705)

 [   John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 21](https://dev.to/hyperpress/comment/c74l)

I mean the whole thing started with MS HTC and FF XBL. So the idea of web components goes way back.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c74l)

 [![e3e34cdb-2bee-490d-bd80-90fdb3630083.png](../_resources/5067141dab2eb7f28b1f6d6239073fcd.jpg)     Aki Rodić](https://dev.to/akirodic)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/akirodic)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/arodic)

 [ Jun 21](https://dev.to/akirodic/comment/c6fa)

I respectfully disagree with most of your arguments. I understand that some of the features of the platform frustrate you. Lets start from the beginning.

1 Progressive enhancement) If you think that websites should work progressively even in browsers without javascript, then web components are not for you. I'd say even the older browsers such as IE are not really suitable for web components. Sure, you can use polyfils but that defeats the purpose. So lets get this out of the way, web components are only meant to be used in browsers that natively support them (and also support javascript).

2 CSS in, err... JS) I gotta say I do agree with problems of CSS encapsulation in Shadow DOM. That is why I don't use the Shadow DOM and its the least favorite feature web components to me. Still I don't mind that it is there, and I'm sure it will be useful in some cases. As for having CSS in files that don't have .css extension... you are free to put your CSS wherever you want, you can also put it in you html file. There is nothing in web components preventing you to do it the old-fashioned way. It is just more convenient to develop in a modular way and have code organized a bit differently even if it means `<style>` strings in your js. Personally, I like it.

3 Platform fatigue) Totally right. It would be much easier for browser developers if no new features are added. It was much easier when we had Adobe Flash. On the other hand, it was Adobe Flash.

4 Polyfills) Also agree (see point 1). Never use polyfills. Web components should be used only on browsers that natively support it. If you are developing a product that needs to work in IE, do not use web components. Period.

5 Composition) This is not really a web component feature. Its just how DOM works. The problem you solved with svelte, you can still solve using custom elements. Also, this is a problem to be solved on a higher level application framework/library. Alternatively, you can make a custom element that solve this problem for you and then reuse it.

6 Confusion between props and attributes) Again, this is not specific to web components. It sucks and I know. It also sucks that attributes are so expensive in general compared to properties. Personally, I developed my framework to rely mostly on properties and ignore attributes by default because in most cases I don't use them. Sometimes I reflect properties to attributes but only as a CSS selector. Almost never do I listen to attribute changes, but in some rare cases I do. Focusing on properties only, helps with this problem a lot.

7 Leaky design) Not a significant issue.
8 The DOM is bad) It is also good. So is CSS.

9 Global namespace) Since you can only register one element of the same name, I think this kind of makes sense.

10 These are all solved problems) If you really believe that, there is no argument to make you think otherwise. I think it comes down to what you think web applications should be capable of. Personally, I think web should one day be able to do everything that native platforms do except: better, faster, more efficient, with better user and developer experience.

A lot of people see web as a platform for static documents with hyperlinks as it once was while others see it as the future of computation. Where on this spectrum are you? According to your writings, I'd guess somewhere in the middle leaning towards former.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6fa)

 [   Ryan Edge](https://dev.to/chimon1984)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/chimon1984)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/chimon2000)

 [ Jun 20](https://dev.to/chimon1984/comment/c5i5)

Is it possible to inject Svelte components into an existing app without compiling them as web components?

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5i5)

 [   Rich Harris](https://dev.to/richharris)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Rich_Harris)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Rich-Harris)  Author

 [ Jun 20](https://dev.to/richharris/comment/c5il)

Yep, by default they compile to regular JavaScript classes

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5il)

 [   Ryan Edge](https://dev.to/chimon1984)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/chimon1984)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/chimon2000)

 [ Jun 20](https://dev.to/chimon1984/comment/c5jn)

Ah ok, we have been looking into using Stencil for some shared components. I assumed you could do this with Svelte but I couldn't find any examples.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5jn)

 [   John Teague](https://dev.to/hyperpress)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/jtteag)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/hyperpress)

 [ Jun 20](https://dev.to/hyperpress/comment/c5o0)

But even though Rich built in a way to compile for web components in Svelte, which at least admits the need to address them, he tells you it's not recommended.

 [THREAD](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5o0)

 [   PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 21](https://dev.to/paulmaly/comment/c6fm)

It's just a ***nice to have*** thing. Svelte is a compiler, so it can just change a *target* of compilation to WC. But not really many people in the community really use this opportunity.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6fm)

 [   PaulMaly](https://dev.to/paulmaly)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PaulMaly)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PaulMaly)

 [ Jun 21](https://dev.to/paulmaly/comment/c6fh)

Please check this example of integration ***existing*** Svelte component (Twitter Card widget) to React application created with CRA: [github.com/PaulMaly/react-svelte](https://github.com/PaulMaly/react-svelte)

Example a little bit outdated, but the main idea doesn't change.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6fh)

 [   Andrew Wooldridge](https://dev.to/triptych)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/triptych)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/triptych)

 [ Jun 20](https://dev.to/triptych/comment/c5j8)

Thank you for the thoughtful and insightful article. I hope posts like this can help change the atmosphere of web development and help us build something better.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5j8)

 [   Rong Sen Ng](https://dev.to/motss)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/igarshmyb)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/motss)

 [ Jun 20](https://dev.to/motss/comment/c5l3)

It's totally acceptable as Web Components isn't perfect yet and it's a pretty low level API that can help you solve part of the problems unlike frameworks. But it's totally worth exploring on WC again in the near future. It's a great article BTW.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5l3)

 [   Nayeem Rahman](https://dev.to/mnayeem)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/M-Nayeem)

 [ Jun 20](https://dev.to/mnayeem/comment/c620)

2: Last I checked, you can use `<link rel="stylesheet"...` in a Shadow tree.

I like to have `@import url("/global.css");` or something similar at the top of any component's stylesheet to implement global themes. A nice and modular solution compared to selectors that penetrate Shadow DOM's.

Edit: Nevermind, I googled FOUC.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c620)

 [   Jochen Bedersdorfer](https://dev.to/beders)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/beders)

 [ Jun 20](https://dev.to/beders/comment/c5pk)

It just blows my mind that after all these years, the very obvious problem that you stated yourself: "But it's hard to overstate what an awkward interface it is for building interactive applications."

has not been tackled.

The browser was made to display hypertext media. The DOM was based on that idea.

If we want interactive apps in the browser, why isn't there an alternative to the DOM for interactive apps? Why isn't there a DOMv4?

Why can't we let go of HTML as the outer shell of an application?
We are down to 2 or 3 major browser engines. Time to renovate.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c5pk)

 [   Phil Ashby](https://dev.to/phlashgbg)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/PhlashGBG)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/PhlashGBG)

 [ Jul 1](https://dev.to/phlashgbg/comment/cghl)

Late to the argument here, but this is the first comment that I understood (not a front-end dev, grokked HTML when it was introduced, backed away for many years..have never used a JS framework/extension/component/whatever or browser API in anger).

It really feels like modern front end development is struggling to escape the document-oriented world of HTML, but has a paranoid fear of shipping code to customers. There have been several attempts in the past to ship portable code under the radar: Shockwave Flash, ActiveX (I lied about portability), Java Applets, Java Web Start, then it seems we got by with ECMAscript and ever-growing numbers of cross-browser APIs, but in that world we're stuck with the DOM, or going it alone in a Canvas?

Perhaps we'll see something akin to the X11/Wayland shift - the old API is too painful and we reach mass adoption of systems that are happy to do everything in OpenGL/3D rendering (three.js and similar are very performant these days), perhaps Web Assembly will help this along.. and folks can finally ship unfettered GUI apps & frameworks that work exactly as they wish - written in their preferred language.. in effect the browser has become a means to ship a runtime (could just as easily be Java, ECMA-335/.NET, WebAssembly, ECMA-262/JS), with a well-defined set of rules to load applications dynamically over a network. It's this last point that makes all the difference between joy and terror for users!

Is it time to re-think the structure of these beasts? Take the network loading rules (almost there with Fetch API I think) and package them up with the chosen runtime, then plug in an HTML renderer on the side, for those few occasions when a plain document arrives?

I'll stop ruminating at this point..

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/cghl)

 [   dsills22](https://dev.to/dsills22)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/dsills22)

 [ Jun 21](https://dev.to/dsills22/comment/c6b3)

"I think that websites should work without JavaScript wherever possible."

I stopped reading there. I mean I think babies should work without vaccines or society, but sorry brah, it is not going to happen. Live in the now. JS is a fuckin language interpreted by the browser, which is in turn compiled from some language. It is all code man, why do you insist on the masochistic view that code should "work" without being coded?

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6b3)

 [   Junk](https://dev.to/oenonono)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Oenonono)

 [ Jun 24](https://dev.to/oenonono/comment/c9b5)

Because not all code is the same, obviously? Otherwise why do we have so many languages?

Why are some developers so adamant about TypeScript? Why didn't the web start out with a single scripting language? (Please FFS, do not repeat that canard about "documents"). Why does Markdown exist?

IMO if you don't understand the strengths HTML has that JS can't and vice versa, you should spare some time and effort to doing so.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c9b5)

 [![f149a1f5-7a88-407e-9c24-dcec9a6f3616.png](../_resources/b15a1e3012470a8bb4c7bdde63d071e3.jpg)     Seanmclem](https://dev.to/seanmclem)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Seanmclem)

 [ Jun 20](https://dev.to/seanmclem/comment/c627)

You lost me at "websites should work without JavaScript wherever possible"...
Just wow

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c627)

 [   Austin Murphy](https://dev.to/ausmurp)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/ausmurp)

 [ Jun 20](https://dev.to/ausmurp/comment/c64o)

For 2, I keep my CSS in a CSS file and import it into my component. Also please please use Polymer to create web components. Yes your complaints are all valid it's still not very robust, but Polymer takes away like 80% of that boilerplate code.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c64o)

 [   Thomas Broyer](https://dev.to/tbroyer)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/tbroyer)

 [ Jun 21](https://dev.to/tbroyer/comment/c6ek)

I suppose you meant lit-html and lit-element rather than Polymer? :troll:

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6ek)

 [   JCorrivo](https://dev.to/jcorrivo)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/JCorrivo)

 [ Jun 25](https://dev.to/jcorrivo/comment/caoa)

I'm really surprised that no one has mentionned anything about tests.

I'm really not familiar with Svelte, it's actually the first time I read about it.

I'm curious and I'm wondering how you would write tests to ensure that the result of the add is right?

	<script>
	  export let a;
	  export let b;
	</script>

	<input type="number" bind:value={a}>
	<input type="number" bind:value={b}>

	<p>{a} + {b} = {a + b}</p>

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/caoa)

 [   Angel D. Munoz](https://dev.to/tunaxor)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Daniel_Tuna)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/AngelMunoz)

 [ Jun 21](https://dev.to/tunaxor/comment/c6m2)

Web components as they are defined in the spec, to me are just low level tools for others to chime in and do quality libraries/frameworks on top of that that allow shareable end products without having to write wrappers for your next favorite framework out there.

That being said, Stencil does an amazing job with web components I think they have nailed on how to produce web components, not even polymer is that good at the web components stuff in general (lit-html, lit-element are close to it).

Regarding the SSR stuff in there and the JS requirement I'll just leave this here

>
>
>   ![hfYqicUk_normal.jpg](../_resources/ffdcb02ebd0b2dea53c57220e74b8d9f.jpg)>
>  Adam Bradley
>
>  @adamdbradley
>

>   ![twitter-99c56e7c338b4d5c17d78f658882ddf18b0bbde5b3f42f84e7964689e7e8fb15.svg](../_resources/c18ec23a3c01d86cfa67394e730d657b.png)>

>
>

>  I just prerendered the entire > [> stenciljs.com](https://t.co/IONop3K3PL)>  website in less than a second. The site works without JS and is fully indexed by all crawlers, but also progressively clientside hydrates. Always comical to have it explained to me that none of that is possible. ‍♂️

>
>  12:29 PM - 21 Jun 2019
>

>   > [>   > ](https://twitter.com/intent/tweet?in_reply_to=1142046797205913600)>   > [>   > ](https://twitter.com/intent/retweet?tweet_id=1142046797205913600)>  9 > [>   > ](https://twitter.com/intent/like?tweet_id=1142046797205913600)>  50

>

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6m2)

 [   Roman Sandler](https://dev.to/romansndlr)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/RomanSndlr)

 [ Jun 29](https://dev.to/romansndlr/comment/cf3d)

I think you make some valid points, but my question is what are the alternatives? If i need to create ui components that can be added to any platform, be as light as possible and have them be highly customizable? I cant think of a better solution.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/cf3d)

 [   Šime Vidas](https://dev.to/simevidas)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/simevidas)

 [ Jun 21](https://dev.to/simevidas/comment/c6bj)

What are your thoughts on using third-party web components for some of your app’s functionality?

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6bj)

 [   Rich Harris](https://dev.to/richharris)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/Rich_Harris)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/Rich-Harris)  Author

 [ Jun 21](https://dev.to/richharris/comment/c6c4)

That's where web components potentially make sense (along with design systems). I haven't encountered such a situation yet, but in theory I'm all for it.

With a caveat, that is: it has to have been hand-coded, or built with a framework that produces very small bundles for standalone components (like Svelte!). If it was built with, say, lit-element, then it's a non-starter for distribution since it has a >20kb runtime dependency.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6c4)

 [   Andrea Giammarchi](https://dev.to/webreflection)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/WebReflection)

 [ Jun 21](https://dev.to/webreflection/comment/c6he)

would just 5.3K work? That's [HyperHTMLElement](https://unpkg.com/hyperhtml-element) size in CDN.

It has various handy helpers so it makes components creation more compact.

If not, does it make sense to complain about verbosity of Custom Elements and then also not accept any helper to simplify them?

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c6he)

 [   Daniel Way](https://dev.to/dwaypro)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/dwaypro)

 [ Jun 22](https://dev.to/dwaypro/comment/c7e9)

Great article, as someone that has deployed webcomponents in a production environment Im here to say that I've run into a lot of these frustrations. Yet I'm super greatfull for the technology. Simply, the ability to have a nested shadowdom I owe my career to. I can take the same web component application and deploy it as a module within many web applications.

Without having to spend weeks in development. I simply drop a tag... `<hello-world></hello-world>` and allow users to analyze financial statements... Webcomponents combined with other open source technologies like webpack which enable us to build/export a single includable file that comes with a framework like Vue... Can be the approach we've been searching for and allow re-usable code to prosper.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c7e9)

 [![07c081df-476f-4b95-af54-346bc6730628.jpeg](../_resources/94211e8af4bb64cca0b3602b81736c7e.jpg)     Thomas Lepérou](https://dev.to/tleperou)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/tleperou)

 [ Jun 25](https://dev.to/tleperou/comment/ca8p)

Nice presentation. I have to admit you know how to write controversial content.

I feel a bit uncomfortable to put **8. DOM is bad** into the perspective of the abstraction that frameworks provide with the native implementation. It might mislead juniors in their understanding.

**Worth to mention [GlimmerJS](https://www.glimmerjs.com/) to create easily web-components ;)**

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/ca8p)

 [   Israel Flores DGA](https://dev.to/israelfloresdga)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/israelfloresdga)

 [ Jun 25](https://dev.to/israelfloresdga/comment/cb2d)

1. *"I think that websites should work without JavaScript wherever possible."*

I believed in that five, six years ago when mobiles phones didn't supported JavaScript.

Today, I don't see why not use something that is native in the browsers (even when not all browser works the same)

2. Seriusly, then why lost time creating HTML5, CSS3 (and later), ES2016+, and the same Svelte. Only use html and your prefered backend

3. Well, or you implement polyfills, because they are common, or they are traspiled with babel.

4. ‍♂

5. Again, if that were the case not even Svelte need to exist. We could simply use vanilla JS (preES6), or if you prefer VB6 or symphony. (just to say a few examples)

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/cb2d)

 [   Brian Takita](https://dev.to/btakita)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/btakita)

 [ Jun 20](https://dev.to/btakita/comment/c63k)

The other cost of complexity imposed by browser standards is the size of the browser. In embedded devices, a large browser means slow load times.

Extra complexity also diffuses development energy, taking away focus on making browsers fast & low memory. It also raises the barriers of entry for new entrants.

Of course, features can be optional. An embedded device with a preloaded application could use a stripped down browser.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c63k)

 [   Darien Maillet Valentine](https://dev.to/bathos)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/bathos)

 [ Jun 21](https://dev.to/bathos/comment/c76l)

7 is interesting to me. The lifecycle callbacks are stored at definition time, not accessed dynamically when the lifecycle events occur, despite being implemented on a prototype. In other words, CustomElementRegistry.prototype.define’s constructor argument is doing double-duty: it’s both the element constructor and an (unusually nested) options object.

From my POV, this seems like a ‘dishonest’ API. On the other hand, I think I understand the decision: it permits subclasses of custom elements to delegate to the lifecycle hooks of their super class. I wouldn’t have made the same design choice personally, but it is possible to delete the public-properties-that-are-really-private-config-options immediately after definition — the leak can be entirely closed.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/c76l)

 [   George Katsanos](https://dev.to/katsanos_george)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/katsanos_george)

 [ Jun 25](https://dev.to/katsanos_george/comment/cb5a)

Rich, I love Svelte, it's really great. Nevertheless, I am a firm believer we should fix issues at their core and not by hiding them or abstracting them under a rug. I haven't worked with WC's but I will say this: The success of Web Components and any Native solution not driven by one single company, is probably not aligned with the interests of the Frameworks and the companies behind them (such as FB) which eventually have an agenda: to push their framework and benefit from the popularity amongst the engineering community, attract developers and eventually convert that power into cash and influence.

It should be obvious to all of us that if we would focus all our efforts in the Platform and stop reinveting the wheel in a series of API changes and rewrites and migrations, we would have a lot more free time to focus on the real reason we are in this job which is to deliver fast, stable, secure, user-friendly interfaces.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/cb5a)

 [   Sasa Blagojevic](https://dev.to/blackcat_dev)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/blackcat_dev)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/sasa-b)

 [ Jul 1](https://dev.to/blackcat_dev/comment/cg2d)

> This may be an increasingly old-fashioned view, but I think that websites should work without JavaScript wherever possible

Ah, you philosophy perfectly aligns with mine, I'm glad there are more prominent people than me who share these sentiments and can argue for our side. I have to check out Svetle now, currently I'm using a weird combo of Turbolinks and self-contained React components :D

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/cg2d)

 [   Joe Wilson](https://dev.to/joewilson0)  [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/b45a941562dca194657f3b61ad71bf74.png)](https://twitter.com/joewilson0)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/bbf13cfb10858d1a2b4d9b9a8a6930cc.png)](https://github.com/joewilson)

 [ Jun 24](https://dev.to/joewilson0/comment/ca57)

True. Web components have been the future for years now.

 [REPLY](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#/richharris/why-i-don-t-use-web-components-2cia/comments/new/ca57)

 [VIEW FULL DISCUSSION (89 COMMENTS)](https://dev.to/richharris/why-i-don-t-use-web-components-2cia/comments)  [code of conduct](https://dev.to/code-of-conduct)-[report abuse](https://dev.to/report-abuse?url=http://dev.to/richharris/why-i-don-t-use-web-components-2cia)