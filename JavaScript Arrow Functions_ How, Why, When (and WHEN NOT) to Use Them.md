JavaScript Arrow Functions: How, Why, When (and WHEN NOT) to Use Them

# JavaScript Arrow Functions: How, Why, When (and WHEN NOT) to Use Them

Oct 1, 2018• [KBall](https://zendev.com/authors/kball.html)• Posted In [JavaScript](https://zendev.com/category/javascript.html)

 838   Shares
 ![facebook.png](:/b223dc24f104fdf6ef3e858420c968a1)  Share
 ![sharethis.png](:/089585375dadda9331ace04c0fcd426e)  Tweet
 ![twitter.png](../_resources/10224fa847590333c8b9c04b35ea7a62.png)  Email
 ![linkedin.png](../_resources/c3fcb5544dff071c42501dd2bc6e7d76.png)
 ![email.png](../_resources/edbe8b73a6cbcad6ae8fb8cea4d100bb.png)

One of the most heralded features in modern JavaScript is the introduction of arrow functions, sometimes called 'fat arrow' functions, utilizing the new token `=>`.

These functions two major benefits - a very clean concise syntax and more intuitive scoping and `this` binding.

Those benefits have sometimes led to arrow functions being strictly preferred over other forms of function declaration.

For example - the popular [airbnb eslint configuration](https://github.com/airbnb/javascript#arrow-functions) enforces the use of JavaScript arrow functions any time you are creating an anonymous function.

However, like anything in engineering, arrow functions come with positives and negatives. There are tradeoffs to their use.

Learning those tradeoffs is key to using arrow functions well.

In this article we'll first review how arrow functions work, then dig into examples of where arrow functions improve our code, and finally dig into a number of examples where arrow functions are *not* a good idea.

[![1545083324-1539370929-mailchimp-Yellow-260x200.png](../_resources/6b0cee8c67694cd00dc8bb75df0efd27.png)](https://srv.carbonads.net/ads/click/x/GTND42QUCAYDEK3WCVBLYKQMCASIPK3LCWYDEZ3JCWSI5237CTBDP2JKC6BI527JCVYDVK3EHJNCLSIZ?segment=placement:zendevcom;)[Track and manage your marketing campaigns from your phone.](https://srv.carbonads.net/ads/click/x/GTND42QUCAYDEK3WCVBLYKQMCASIPK3LCWYDEZ3JCWSI5237CTBDP2JKC6BI527JCVYDVK3EHJNCLSIZ?segment=placement:zendevcom;)[ads via Carbon](http://carbonads.net/?utm_source=zendevcom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

## So What Are JavaScript Arrow Functions Anyway?

JavaScript arrow functions are roughly the equivalent of [lambda functions in python](https://www.programiz.com/python-programming/anonymous-function) or [blocks in Ruby](http://ruby-for-beginners.rubymonstas.org/blocks.html).

These are anonymous functions with their own special syntax that accept a fixed number of arguments, and operate in the *context* of their *enclosing scope* - ie the function or other code where they are defined.

Let's break down each of these pieces in turn.

### Arrow Function Syntax

Arrow functions have a single overarching structure, and then an number of ways they can be simplified in special cases.

The core structure looks like this:

	(argument1, argument2, ... argumentN) => {
	  *// function body*
	}

A list of arguments within parenthesis, followed by a 'fat arrow' (`=>`), followed by a function body.

This is very similar to traditional functions, we just leave off the `function` keyword and add a fat arrow after the arguments.

However, there are a number of ways to 'sugar' this up that make arrow functions *dramatically* more concise for simple functions.

First, if the function body is a single expression, you can leave off the brackets and put it inline. The results of the expression will be returned by the function. For example:

`const add = (a, b) => a + b;`

Second, if there is only a single argument, you can even leave off the parenthesis around the argument. For example:

`const getFirst = array => array[0];`

As you can see, this can lead to some very concise syntax, which we'll highlight more benefits of later.

#### Advanced Syntax

There are a few pieces of advanced syntax that are useful to know.

First, if you're attempting to use the inline, single-expression syntax but the value you're returning is an object literal. You might think this would look like:

`(name, description) => {name: name, description: description};`

The problem is that this syntax is ambiguous - it looks as though you're trying to create a traditional function body.

To indicate that instead you want a single expression that happens to be an object, you wrap the object with parentheses:

`(name, description) => ({name: name, description: description});`

### Enclosing Scope Context

Unlike every other form of function, arrow functions do not have their own [execution context](https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0).

Practically, this means that both `this` and `arguments` are *inherited* from their parent function.

For example, compare the following code with and without arrow functions:

	const test = {
	  name: 'test object',
	  createAnonFunction: function() {
	    return function() {
	      console.log(this.name);
	      console.log(arguments);
	    };
	  },

	  createArrowFunction: function() {
	    return () => {
	      console.log(this.name);
	      console.log(arguments);
	    };
	  }
	};

We have a simple test object with two methods - each a function that creates and returns an anonymous function.

The difference is in the first case it uses a traditional function expression, while in the latter it uses an arrow function.

If we run these in a console with the same arguments however, we get very different results.

	> const anon = test.createAnonFunction('hello', 'world');
	> const arrow = test.createArrowFunction('hello', 'world');

	> anon();
	undefined
	{}

	> arrow();
	test object
	{ '0': 'hello', '1': 'world' }

The anonymous function has its own function context, so when you call it there is no reference available to the `this.name` of the test object, nor to the arguments called in creating it.

The arrow function, on the otherhand, has the exact same function context as the function that created it, giving it access to both the argumetns and the test object.

## Where Arrow Functions Improve Your Code

One of the primary usecases for traditional lambda functions, and now for arrow functions in JavaScript, is for functions that get applied over and over again to items in a list.

For example, if you have an array of values that you want to transform using a map, an arrow function is ideal:

	const words = ['hello', 'WORLD', 'Whatever'];
	const downcasedWords = words.map(word => word.toLowerCase());

An extremely common example of this is to pull out a particular value of an object:

`const names = objects.map(object => object.name);`

Similarly, when replacing old-style `for` loops with modern iterator-style loops using `forEach`, the fact that arrow functions keep `this` from the parent makes them extremely intuitive.

	this.examples.forEach(example => {
	  this.runExample(example);
	});

### Promises and Promise Chains

Another place arrow functions make for cleaner and more intuitive code is in managing asynchronous code.

[Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) make it far easier to manage async code (and even if you're excited to use async/await, you should [still understand promises](https://medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8) which is what async/await is built on top of!)

However, while using promises still requires defining functions that run after your asynchronous code or call completes.

This is an ideal location for an arrow function, especially if your resulting function is stateful, referencing something in your object. Example:

	this.doSomethingAsync().then((result) => {
	  this.storeResult(result);
	});

### Object Transformations

Another common and extremely powerful use for arrow functions is to encapsulate object transformations.

For example, in Vue.js there is a common pattern for [including pieces of a Vuex store directly into a Vue component using `mapState`](https://vuex.vuejs.org/guide/state.html#the-mapstate-helper).

This involves defining a set of "mappers" that will transform from the original complete state object to pull out exactly what is necessary for the component in question.

These sorts of simple transformations are an ideal and beautiful place to utilize arrow functions. Example:

	export default {
	  computed: {
	    ...mapState({
	      results: state => state.results,
	      users: state => state.users,
	    });
	  }
	}

## Where You Should Not Use Arrow Functions

There are a number of situations in which arrow functions are **not** a good idea. Places where they will not only help, but cause you trouble.

The first is in methods on an object. This is an example where function context and `this` are exactly what you want.

There was a trend for a little while to use a combination of the Class Properties syntax and arrow functions as a way to create "auto-binding" methods, e.g. methods that could be used by event handlers but that stayed bound to the class.

This looked something like:

	class Counter {
	  counter = 0;

	  handleClick = () => {
	    this.counter++;
	  }
	}

In this way, even if handleClick were called with by an event handler rather than in the context of an instance of `Counter`, it would still have access to the instance's data.

The downsides of this approach are multiple, documented well in [this post](https://medium.com/@charpeni/arrow-functions-in-class-properties-might-not-be-as-great-as-we-think-3b3551c440b1).

While using this approach does give you an ergonomic-looking shortcut to having a bound function, that function behaves in a number of ways that are not intuitive, inhibiting testing and creating problems if you attempt to subclass/use this object as a prototype.

Instead, use a regular function and if necessary bind it the instance in the constructor:

	class Counter {
	  counter = 0;

	  handleClick() {
	    this.counter++;
	  }

	  constructor() {
	    this.handleClick = this.handleClick.bind(this);
	  }
	}

### Deep Callchains

Another place where arrow functions can get you in trouble is when they are going to be used in many different combinations, particularly in deep chains of function calls.

The core reason is the same as with anonymous functions - they give [really bad stacktraces](https://hackernoon.com/three-reasons-i-avoid-anonymous-js-functions-like-the-plague-7f985c27a006).

This isn't too bad if your function only goes one level down, say inside of an iterator, but if you're defining all of your functions as arrow functions and calling back and forth between them, you'll be pretty stuck when you hit a bug and just get error messages like:

	{anonymous}()
	{anonymous}()
	{anonymous}()
	{anonymous}()
	{anonymous}()

### Functions With Dynamic Context

The last situation where arrow functions can get you in trouble is in places where `this` is bound dynamically.

If you use arrow functions in these locations, that dynamic binding will not work, and you (or someone else working with your code later) may get very confused as to why things aren't working as expected.

Some key examples of this:

- Event handlers are called with `this` set to the event's `currentTarget`attribute.
- If you're still using jQuery, most jQuery methods set `this` to the dom element that has been selected.
- If you're using Vue.js, methods and computed functions typically set `this` to be the Vue component.

Certainly you can use arrow functions deliberately to override this behavior, but especially in the cases of jQuery and Vue this will often interfere with normal functioning and leave you baffled why code that looks the same as other code nearby is not working.

## Wrapping Up

In summary: Arrow functions are a phenomenal addition to the JavaScript language, and enable far more ergonomic code in a number of situations.

However, like every other feature, they have advantages and disadvantages. We should use them as another tool in our toolchest, not as a blanket replacement for all functions.

* * *

Working on learning modern JavaScript? I recommend either [this course](https://click.linksynergy.com/deeplink?id=hIdOL5Z4eK4&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fthe-complete-javascript-course%2F) if you are new to JavaScript or [this one](https://click.linksynergy.com/deeplink?id=hIdOL5Z4eK4&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fjavascript-es6-tutorial%2F) focused on upgrading your skills from ES5 to ES6.

**Affiliate disclosure**: Those course links are affiliate links, which means I may receive a commission if you decide to buy them. But if you’d prefer I didn’t receive a commission, that’s cool too. Just search for 'The Complete JavaScript Course' or 'ES6 Javascript: The Complete Developer's Guide' on Udemy instead of using my links.

* * *

P.S. - If you're interested in these types of topics, I send out a weekly newsletter called the 'Friday Frontend'. Every Friday I send out 15 links to the best articles, tutorials, and announcements in CSS/SCSS, JavaScript, and assorted other awesome Front-end News. Sign up now!

## Popular Posts

[ ### CSS in JS is like replacing a broken screwdriver with your favorite hammer.](https://zendev.com/2017/09/11/css-in-js.html)

[ ### The Web Fundamentals Gap](https://zendev.com/2017/10/24/the-web-fundamentals-gap.html)

[ ### Front-end Development Kickstarter: All about the ZURB Template](https://zendev.com/2017/09/05/front-end-development-kickstarter-zurb-template.html)

## Recent Posts

[ ### Friday Frontend: End of 2019 Edition](https://zendev.com/2019/12/20/end-of-2019-edition.html)

[ ### Friday Frontend: Color Palettes and JS Performance Edition](https://zendev.com/2019/12/13/color-palettes-and-js-performance-edition.html)

[ ### Friday Frontend: CSS Subgrids Are Here Edition](https://zendev.com/2019/12/06/css-subgrids-are-here-edition.html)

What do you think?
13 Responses
![upvote-512x512.png](../_resources/828101660ed17b0761c95e89f9e367d4.png)
Upvote

![funny-512x512.png](../_resources/80ec843281e6130a88e665c83c2c12d5.png)
Funny

![love-512x512.png](../_resources/11d71f65e58bb5c9afb8534ba31c6f75.png)
Love

![surprised-512x512.png](../_resources/13431b9bca0ec3070b4277d7162d0755.png)
Surprised

![angry-512x512.png](../_resources/d2e29b214b10de327b89d7197a7b68e1.png)
Angry

![sad-512x512.png](../_resources/e84a77b79c9a1423d57ef6cf7f6bb2d9.png)
Sad

- [8 comments]()
- [**ZenDev.com**](https://disqus.com/home/forums/zen-dev/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  2](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

[(L)](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/tracker1/)

 [Tracker1](https://disqus.com/by/tracker1/)    •  [a year ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4124463768)

not actually calling the toLowerCase method in one of your examples...

const downcasedWords = [words.map](http://disq.us/url?url=http%3A%2F%2Fwords.map%3AN5uw2pegu4eueRRx0Dgx5uXl9z0&cuid=3226216)(word => word.toLowerCase());

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/kbal11/)

 [Kevin Ball](https://disqus.com/by/kbal11/)  Mod  [*>* Tracker1](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4124463768)  •  [a year ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4126148237)

Thanks, updated to fix!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/vijayhackr/)

 [Vijay Hackr](https://disqus.com/by/vijayhackr/)    •  [a year ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4156702388)

Nicely provided the information.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/abinayaa_r/)

 [Abinayaa R](https://disqus.com/by/abinayaa_r/)    •  [18 days ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4712791093)

Good blog! As you have mentioned that JavaScript arrow functions are roughly the equivalent of lambda functions in python, you can check out this article on [How to use Python Lambda Functions](https://disq.us/url?url=https%3A%2F%2Fwww.agiratech.com%2Fpython-lambda-functions%2F%3A7SX20ngIwRLoRosTxKjQkfDu0cg&cuid=3226216).

-

    - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_mtCblNJ6E0/)

 [Thiago +](https://disqus.com/by/disqus_mtCblNJ6E0/)    •  [2 months ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4672886796)

Excellent post.
Beginners believe they should code fully with arrow functions.

I always say that you should only use arrow functions when there is functional or semantic sense.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_8GHzbGqASa/)

 [John Hopkins](https://disqus.com/by/disqus_8GHzbGqASa/)    •  [a year ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4305592136)  •  edited

Nice article! In your 'advanced syntax' description you can make it even more concise.

(name, description) => ({name: name, description: description});
Could be shortened to
(name, description) => ({name, description})

-

    - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/faiwertest/)

 [Faiwer](https://disqus.com/by/faiwertest/)    •  [a year ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4134405093)

I think you can use =>-functions in React classes for event handlers. I've read that article that you linked. There're 3 problems described.

1 - mockability. Yep this problem is exist. I agree. But it isn't so bad. Just a small problem.

2 - inheritence. But in React ecosystem we usually don't use it at all.

3 - perfomance. But event handlers aren't bottlenecks, it's no use to optimize code this way, you can find much more important places in your code to optimize.

So... you can use it without worrying about it. It saves a lot of time and makes our codes cleaner. IMHO, that's much more important, than "mockability". Also you can use decorator for this case. Writing .bind wrappers in constructor manually is the worst way (IMHO).

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/victorlongon/)

 [Victor Longon](https://disqus.com/by/victorlongon/)    [*>* Faiwer](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4134405093)  •  [a year ago](https://zendev.com/2018/10/01/javascript-arrow-functions-how-why-when.html#comment-4152310041)

Exactly, besides binding methods in a constructor for a class component is just very ugly XD

## Also on **ZenDev.com**

- [

### How to Learn Vue.js in 2018

    - 3 comments •

    - a year ago

[
felipe_japm —

I would suggest this compilation of vue.js courses [the-complete-vuejs -course -bundle](http://disq.us/url?url=http%3A%2F%2Fquero.com%2Fthe-complete-vuejs-course-bundle%3A-9eN-15iT6rozRfBd2o0_4t_mOA&cuid=3226216)](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2018%2F10%2F18%2Fhow-to-learn-vue-js.html&key=SO0MW-ZNTlELrjN26XCsfw)](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2018%2F10%2F18%2Fhow-to-learn-vue-js.html&key=SO0MW-ZNTlELrjN26XCsfw)

- [

### Top 5 skills to learn as a junior JavaScript developers

    - 1 comment •

    - 7 months ago

[nomi bekaris— you wrote to learn vanilla js thorougly. What other courses you can suggest to go through before starting vue? Thanks!](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2019%2F06%2F04%2Ftop-skills-to-learn-junior-javascript-developer.html&key=WMS7V7IYwYCo2M1aL7CUWQ)](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2019%2F06%2F04%2Ftop-skills-to-learn-junior-javascript-developer.html&key=WMS7V7IYwYCo2M1aL7CUWQ)

- [

### CSS dismissal is about exclusion, not technology

    - 36 comments •

    - a year ago

[Trellis King— I'm a huge fan of CSS. As a frontend developer I understand that sometimes there are advantages to embedding CSS in JS in certain situations.  But maybe I need to check my privilege.](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2018%2F09%2F11%2Fcss-dismissal-is-about-exclusion-not-technology.html&key=TmDB7tS6N1OMK-qkOwIB3w)](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2018%2F09%2F11%2Fcss-dismissal-is-about-exclusion-not-technology.html&key=TmDB7tS6N1OMK-qkOwIB3w)

- [

### Friday Frontend: JavaScript Goes Everywhere Edition

    - 2 comments •

    - 7 months ago

[Kevin Ball— Yeah! I think it's a very nice solution, and since it's actually coming from inside MS where they more or less control both sides (the IE and the edge) it seems like it might be more sustainable than the "chrome frame"](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2019%2F05%2F10%2Fjavascript-goes-everywhere-edition.html&key=g0CDul_mJPwRYyLUl_RHzQ)](https://disq.us/?url=https%3A%2F%2Fzendev.com%2F2019%2F05%2F10%2Fjavascript-goes-everywhere-edition.html&key=g0CDul_mJPwRYyLUl_RHzQ)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=zen-dev&t_i=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_u=https%3A%2F%2Fzendev.com%2F2018%2F10%2F01%2Fjavascript-arrow-functions-how-why-when.html&t_d=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&t_t=JavaScript%20Arrow%20Functions%3A%20How%2C%20Why%2C%20When%20(and%20WHEN%20NOT)%20to%20Use%20Them&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=zen-dev&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)