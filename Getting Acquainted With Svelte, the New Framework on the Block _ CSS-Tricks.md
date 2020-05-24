Getting Acquainted With Svelte, the New Framework on the Block | CSS-Tricks

For the last six years, Vue, Angular, and React have run the world of front-end component frameworks. Google and Facebook have their own sponsored frameworks, but they might leave a bitter taste for anyone who advocates for an open and unbiased web. Vue is another popular framework that has multiple sponsors, but isn’t run by a single corporation, which may be attractive to some folks.

There’s another player in the framework space that’s gaining attention and operates very much in the same spirit as Vue as far adopting an open MIT license: Svelte.

Svelte has been covered here on CSS-Tricks before, like Ollie Williams’ excellent overview of [how it can be used to write more convenient, component-based CSS](https://css-tricks.com/what-i-like-about-writing-styles-with-svelte/). This article is going to zoom out a bit and provide a little more context about Svelt, as well as how it differentiates itself from other frameworks, and how to implement it in your own projects.

### [#](https://css-tricks.com/getting-acquainted-with-svelte-the-new-framework-on-the-block/#article-header-id-0)What makes Svelte different?

> open-quote*> I can confidently say that Svelte has been the easiest JavaScript component library to learn and start putting to use in a productive way.*

> — Jeff Delaney, from > [> Svelte Realtime Todo List with Firebase](https://fireship.io/lessons/svelte-v3-overview-firebase/)> close-quote

OK, so Svelte is a JavaScript component library. But so is React. And Angular. And Vue. What makes Svelte stand out from the bunch?

Svelte is trying to do a few things that are different from the rest:
1. 1.All the code is compiled ahead of time.
2. 2.There is no virtual DOM.
3. 3.CSS scoping is baked in.

Let’s break those down a bit because they significantly distinguish Svelte from other front-end frameworks.

#### All the code is compiled ahead of time.

Svelte is a *compiler*, meaning that the code in Svelte files gets converted from an easier-to-write hybrid language that mixes HTML, JavaScript, and CSS into lower-level optimized JavaScript, HTML, and CSS files.

This is very similar to the way C# gets compiled down to bytecode, or how Typescript compiles down to JavaScript. But where traditional compilers tend to go down to *one* language, Svelte mixes all three.

This makes writing code a lot more flexible, and benefits the client (web browser) as the computation is done when the application is built, not on every browser when the web app is visited.

#### There is no Virtual DOM.

A DOM (or Document Object Model) is an interface that defines the logical structure of a webpage. It takes HTML and converts it to a structure that can be manipulated and accessed. Chris has a classic post that [thoroughly explains it](https://css-tricks.com/dom/).

The Virtual DOM extends the concept of a DOM by creating a “second” DOM in memory. Like the DOM, this is manipulated and accessed by traditional frameworks (e.g. Angular, Vue, and React). At build, this second “virtual” DOM gets consolidated with the actual DOM, allowing the UI to render.

And what about the Shadow DOM? Well, the Shadow DOM is technically part of the “real” DOM, just in the shadows. As such it is a great tool for isolating chunks of code that don’t leak into or conflict with other elements on the page — a little bit like (but at the same time almost nothing like) an iframe. The shadow DOM is sorta the crux for most component-based front-end frameworks because they leverage the siloed nature of the Shadow DOM to serve specific code to specific elements.

While that isn’t exactly a key selling point of Svelte, it is possible to work with the Shadow DOM experimentally. The Shadow DOM hasn’t really quite caught on in progressive web practices, which is a shame, and probably due to the confusion between drafts and lack of support from IE and Edge.

So, where am I going with all this? The difference between Svelte and other JavaScript frameworks is **the lack of a Virtual DOM**. That’s important because it contributes to faster apps — faster than frameworks using a Virtual DOM. Yes, the Virtual DOM can be super fast because it only updates parts of the DOM when needed, but as applications grow, the impact of a duplicate DOM stored in memory can have an overall negative impact on performance.

Svelte takes a different approach and does a lot of these heavy calculations at build time. All that heavy lifting in advance, which allows Svelte to surgically insert changes only where needed.

#### CSS scoping is baked in.

Svelte has built-in styling, which is essential in other modern frameworks. The different between CSS in Svelte and CSS in other frameworks is that Svelte takes the CSS from each component and spits it out to a separate CSS file on build.

A personal gripe I have with most CSS-in-JS approaches is that it seems like an over-engineered solution. Svelte’s approach keeps things lean, vanilla, and encapsulated — while keeping everything where it should be.

For those who love preprocessors, there are plugins, whether it for Sass, Less or Gulp. But since Svelte is still in its infancy, I would recommend using plain ol’ CSS with a minified CSS framework of your choice so you can utilize Svelte’s handy dandy component scoping.

You could just as easily keep to your usual styling preferences and completely forgo Svelte’s CSS builder. However, I’d argue that is a massive shame, as Svelte’s solution has been extremely clean and enjoyable, at lease in my experience. But anyone who has to work with IE11 () and even older browsers will know that normalizing styles is a must. This is a good place to stop and check out Ollie’s post because he [dives much deeper into Svelte’s styling features and advantages](https://css-tricks.com/what-i-like-about-writing-styles-with-svelte/).

### [#](https://css-tricks.com/getting-acquainted-with-svelte-the-new-framework-on-the-block/#article-header-id-1)How Svelte stacks up to other frameworks

We just looked at what how Svelte has a different approach for compiling, interacting with DOM and writing CSS. You might be wondering: how does Svelte compare to other popular frameworks?

There are plenty of [comparisons](https://twitter.com/Rich_Harris/status/1065992585095929857) already out there, but suffice to say that Svelte is pretty darn fast. But speed isn’t the only basis for comparison. Instead, let’s do a side-by-side that looks at a broader overview in a format much loved by the development community: a table!

|     | Svelte | Vue | React | Angular (2+) |
| --- | --- | --- | --- | --- |
| What is it | Compiler | Framework | Framework | Framework |
| First Commit | Nov. 16, 2016 | Jul. 29, 2013 | May 24, 2013 | Sep. 18, 2014 |
| Backing | Open source | Multiple Sponsors | Facebook | Google |
| Community[¹](https://css-tricks.com/getting-acquainted-with-svelte-the-new-framework-on-the-block/#fn:1) | Small | Large | Massive | Large |
| Satisfaction[2](https://css-tricks.com/getting-acquainted-with-svelte-the-new-framework-on-the-block/#fn:2) | 88% | 87% | 89% | 38% |

Svelte is in a strong position considering its late entrance and small community. Developer satisfaction is high, while the big three have been seeing recent declines. The Svelte community is small, but growing, and the code is open source which is a huge plus for the overall web community.

**Let’s look at an example of using Svelte**

I hope that I have convinced you that Svelte is worth at least a try. If so, let’s fire up the terminal and try a real-world examples of an everyday use case: implementing the [Intersection Observer](https://css-tricks.com/an-explanation-of-how-the-intersection-observer-watches/). If you’ve ever [run a Lighthouse report](https://web.dev/measure/), it may have been shouted at you for not using [passive scroll events](https://developers.google.com/web/updates/2016/06/passive-event-listeners). That may be the most boring sentence I have written in my life, but it’s scores points for performance and isn’t overly complicated to do with the Intersection Observer in Svelte.

Let’s skip all the installation and setup stuff because we can avoid it with [REPL](https://svelte.dev/repl/hello-world?version=3.18.0), the online editor Svelte uses to demonstrate the framework on its site. The standard “Hello world” boilerplate is in there. Go ahead and download the ZIP file of the app, in the upper-right corner of the screen.

Now, unzip the file and cd into the folder from the terminal and run  npm -i to initialize the project. Once that’s done, do npm run build and you’ll get a copy of your lightweight miniature Svelte “Hello, world!” app.

Now we can get into the actual task of adding the IntersectionObserver.

First, we import the code that has already kindly been written by the Svelte team. It’s in the source code of the [svelte.dev git repo](https://github.com/sveltejs/svelte/blob/master/site/src/components/IntersectionObserver.svelte) (the inner cogs of which make for fascinating reading).

JavaScript	<script>

	  import { onMount } from 'svelte';
	  export let once = false;
	  export let top = 0;
	  export let bottom = 0;
	  export let left = 0;
	  export let right = 0;
	  let intersecting = false;
	  let container;

	  onMount(() => {
	    if (typeof IntersectionObserver !== 'undefined') {
	      const rootMargin = `${bottom}px ${left}px ${top}px ${right}px`;
	      const observer = new IntersectionObserver(entries => {
	        intersecting = entries[0].isIntersecting;
	        if (intersecting && once) {
	          observer.unobserve(container);
	        }
	        }, {
	          rootMargin
	      });
	        observer.observe(container);
	        return () => observer.unobserve(container);
	  }

	  function handler() {
	    const bcr = container.getBoundingClientRect();
	    intersecting = (
	      (bcr.bottom + bottom) > 0 &&
	      (bcr.right + right) > 0 &&
	      (bcr.top - top) < window.innerHeight &&
	      (bcr.left - left) < window.innerWidth
	    );
	    if (intersecting && once) {
	      window.removeEventListener('scroll', handler);
	    }
	  }

	  window.addEventListener('scroll', handler);
	    return () => window.removeEventListener('scroll', handler);
	  });
	</script>

	<style>
	  div {
	    width: 100%;
	    height: 100%;
	  }
	</style>

	<div bind:this={container}>
	  <slot {intersecting}></slot>
	</div>

Stick this in a file called `IntersectionObserver.svelte` in a `src/components` folder. Then, reference it from the main Svelte file: `App.svelte`.

JavaScript`import IntersectionObserver from "../components/IntersectionObserver.svelte";`

Now that we have the Intersection Observer available as a component, we can wrap other elements with it.

JavaScript	<IntersectionObserver let:intersecting top={400}>

	 {#if intersecting}
	    <section>
	      This message will Show if it is intersecting
	    </section>
	  {:else}
	    <section>
	      This message won't Show if it is intersecting
	    </section>
	 {/if}
	</IntersectionObserver>

That’s really it! You can see how the Intersection Observer component allows us to use `<IntersectionObserver>`  like a wrapper and define where the intersection should trigger, which is 400 pixels from the top in this example. As a reminder, this is all being exported as **vanilla JavaScript**! Super performant, no funny business. We’re sandwiching JavaScript and HTML together which is cool because we can see what the Intersection Observer is directly affecting, leaving no ambiguity and without being penalized for performance.

The `OnMount` function is necessary to tell Svelte that this code needs to run within the browser, as the Intersection Observer can’t be figured out ahead of time.

We’ll need to add some styling so that we can experience the observer in action, and we can do that directly in your `App.svelte` file. This might look super familiar if you have worked with any of the other front-end frameworks:

CSS	<style>

	  .somesection {
	    display: flex;
	    align-items: center;
	    justify-content: center;
	    width: 100%;
	    height: 100vh;
	  }

	  .somesection.even{
	    background: #ccc;
	  }

	  .content{
	    text-align: center;
	    width: 350px;
	  }
	</style>

Finally, we can copy and paste our Intersection Observer element four times to create more intersections. That gives us a mini web app that reactively adds and removes content as it comes into view — perfect to use with media, like [lazy-loading](https://css-tricks.com/lazy-loading-images-with-vue-js-directives-and-intersection-observer/). Check out a [demo of the final result](https://svelte.dev/repl/c461dfe7dbf84998a03fdb30785c27f3?version=3.16.7) and be sure to crack open DevTools to see the Intersection Observer

### [#](https://css-tricks.com/getting-acquainted-with-svelte-the-new-framework-on-the-block/#article-header-id-2)Some final thoughts

My personal recommendation is to give Svelte a try. We’ve only scratched the surface of the framework in this article, but having converted my personal website to Svelte, I can confidently say that it is a pleasure to work with. It is performant, [has a brilliant VSCode linter](https://marketplace.visualstudio.com/items?itemName=JamesBirtles.svelte-vscode), and best of all, is easy to use. It may be small and new on the block, but I have a keen feeling that it is the relief from bloated “Goliath” frameworks, the “David” that frontend-ers have been looking for.

So *should *you use Svelte in a real project? Comparing risk and reward definitely comes into play. The community is smaller than other frameworks, meaning you’re likely to find less support and fewer tutorials to guide your along. At the same time, Svelte is in its third generation, meaning most of the gremlins should have been driven away, leaving a lean and reliable framework.

As with anything new, common sense rules, try it out with something non-commercial, take it for a spin, and see how you go.

Is there anything else? Funny you should ask! There are two co-projects that live in the Svelte Ecosystem: [Sapper](https://sapper.svelte.dev/) and [Native](https://svelte-native.technology/). **Sapper **is a framework that utilizes Svelte for building full web applications, including routing, service workers, and all the good stuff you need to get started. I have used it to rebuild my personal website, and so far, I am a fan. **Svelte Native **is the most experimental of the Svelte projects, a NativeScript mobile app builder that utilizes Svelte under the hood. I confess that is where my knowledge on the subject ends. Luckily, it has [a website](https://svelte-native.technology/) with further information.

What do you think? Have you given Svelte a try? Do you think it stacks up to other frameworks? Let’s discuss it in the comments!

Footnotes

1. 1.[Based on a mix](https://gist.github.com/tkrotoff/b1caa4c3a185629299ec234d2314e190) of Github Contributions, NPM Downloads and StackOverflow topics

2. 2.[State of JS review 2019](https://2019.stateofjs.com/front-end-frameworks/)