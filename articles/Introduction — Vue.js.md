Introduction — Vue.js

[![32052.png](:/f3666fdc4769edde502582022ae0820c)](https://srv.carbonads.net/ads/click/x/GTND423YF6SI42JWCWB4YKQWFTAIK2QECYBIVZ3JCEADL2Q7CK7D453KC6BDE5QUC6SDTK3EHJNCLSIZZRLCP7I35MNFV?segment=placement:vuejs;&encredirect=https%3A%2F%2Fslack.com%2Fis%3Fcvosrc%3Ddisplay.carbon.plain%20dev%26utm_source%3Dcarbon%26utm_medium%3Ddisplay%26utm_campaign%3Dplain%20dev%26c3ch%3DCarbon%20Networks%26c3nid%3DPlain%20Dev)[All the tools your team needs in one place. Slack: Where work happens.](https://srv.carbonads.net/ads/click/x/GTND423YF6SI42JWCWB4YKQWFTAIK2QECYBIVZ3JCEADL2Q7CK7D453KC6BDE5QUC6SDTK3EHJNCLSIZZRLCP7I35MNFV?segment=placement:vuejs;&encredirect=https%3A%2F%2Fslack.com%2Fis%3Fcvosrc%3Ddisplay.carbon.plain%20dev%26utm_source%3Dcarbon%26utm_medium%3Ddisplay%26utm_campaign%3Dplain%20dev%26c3ch%3DCarbon%20Networks%26c3nid%3DPlain%20Dev)[ads via Carbon](http://carbonads.net/)

# Introduction

 [

## [(L)](https://vuejs.org/v2/guide/index.html#What-is-Vue-js)What is Vue.js?](https://vuejs.org/v2/guide/index.html#What-is-Vue-js)

Vue (pronounced /vjuː/, like **view**) is a **progressive framework** for building user interfaces. Unlike other monolithic frameworks, Vue is designed from the ground up to be incrementally adoptable. The core library is focused on the view layer only, and is very easy to pick up and integrate with other libraries or existing projects. On the other hand, Vue is also perfectly capable of powering sophisticated Single-Page Applications when used in combination with [modern tooling](https://vuejs.org/v2/guide/single-file-components.html) and [supporting libraries](https://github.com/vuejs/awesome-vue#libraries--plugins).

If you are an experienced frontend developer and want to know how Vue compares to other libraries/frameworks, check out the [Comparison with Other Frameworks](https://vuejs.org/v2/guide/comparison.html).

[

## [(L)](https://vuejs.org/v2/guide/index.html#Getting-Started)Getting Started](https://vuejs.org/v2/guide/index.html#Getting-Started)

!The official guide assumes intermediate level knowledge of HTML, CSS, and JavaScript. If you are totally new to frontend development, it might not be the best idea to jump right into a framework as your first step - grasp the basics then come back! Prior experience with other frameworks helps, but is not required.

The easiest way to try out Vue.js is using the [JSFiddle Hello World example](https://jsfiddle.net/chrisvfritz/50wL7mdz/). Feel free to open it in another tab and follow along as we go through some basic examples. Or, you can simply create an `.html` file and include Vue with:

|     |
| --- |
| <script  src="https://unpkg.com/vue"></script><br>HTML |

The [Installation](https://vuejs.org/v2/guide/installation.html) page provides more options of installing Vue. Note that we **do not** recommend beginners to start with `vue-cli`, especially if you are not yet familiar with Node.js-based build tools.

[

## [(L)](https://vuejs.org/v2/guide/index.html#Declarative-Rendering)Declarative Rendering](https://vuejs.org/v2/guide/index.html#Declarative-Rendering)

At the core of Vue.js is a system that enables us to declaratively render data to the DOM using straightforward template syntax:

|     |
| --- |
| <div  id="app"><br>{{ message }}<br></div><br>HTML |

|     |
| --- |
| var app = new Vue({<br> el: '#app',<br> data: {<br> message: 'Hello Vue!'<br>}<br>})<br>JS |

Hello Vue!

We have already created our very first Vue app! This looks pretty similar to just rendering a string template, but Vue has done a lot of work under the hood. The data and the DOM are now linked, and everything is now **reactive**. How do we know? Just open your browser’s JavaScript console (right now, on this page) and set `app.message` to a different value. You should see the rendered example above update accordingly.

In addition to text interpolation, we can also bind element attributes like this:

|     |
| --- |
| <div  id="app-2"><br> <span  v-bind:title="message"><br>Hover your mouse over me for a few seconds<br>to see my dynamically bound title!<br> </span><br></div><br>HTML |

|     |
| --- |
| var app2 = new Vue({<br> el: '#app-2',<br> data: {<br> message: 'You loaded this page on ' + new  Date()<br>}<br>})<br>JS |

Hover your mouse over me for a few seconds to see my dynamically bound title!

Here we are encountering something new. The `v-bind` attribute you are seeing is called a **directive**. Directives are prefixed with `v-` to indicate that they are special attributes provided by Vue, and as you may have guessed, they apply special reactive behavior to the rendered DOM. Here it is basically saying “keep this element’s `title` attribute up-to-date with the `message` property on the Vue instance.”

If you open up your JavaScript console again and enter `app2.message = 'some new message'`, you’ll once again see that the bound HTML - in this case the `title` attribute - has been updated.

[

## [(L)](https://vuejs.org/v2/guide/index.html#Conditionals-and-Loops)Conditionals and Loops](https://vuejs.org/v2/guide/index.html#Conditionals-and-Loops)

It’s quite simple to toggle the presence of an element, too:

|     |
| --- |
| <div  id="app-3"><br> <p  v-if="seen">Now you see me</p><br></div><br>HTML |

|     |
| --- |
| var app3 = new Vue({<br> el: '#app-3',<br> data: {<br> seen: true<br>}<br>})<br>JS |

Now you see me

Go ahead and enter `app3.seen = false` in the console. You should see the message disappear.

This example demonstrates that we can bind data to not only text and attributes, but also the **structure** of the DOM. Moreover, Vue also provides a powerful transition effect system that can automatically apply [transition effects](https://vuejs.org/v2/guide/transitions.html) when elements are inserted/updated/removed by Vue.

There are quite a few other directives, each with its own special functionality. For example, the `v-for` directive can be used for displaying a list of items using the data from an Array:

|     |
| --- |
| <div  id="app-4"><br> <ol><br> <li  v-for="todo in todos"><br>{{ todo.text }}<br> </li><br> </ol><br></div><br>HTML |

|     |
| --- |
| var app4 = new Vue({<br> el: '#app-4',<br> data: {<br> todos: [<br>{ text: 'Learn JavaScript' },<br>{ text: 'Learn Vue' },<br>{ text: 'Build something awesome' }<br>]<br>}<br>})<br>JS |

1.  Learn JavaScript
2.  Learn Vue
3.  Build something awesome

In the console, enter `app4.todos.push({ text: 'New item' })`. You should see a new item appended to the list.

[

## [(L)](https://vuejs.org/v2/guide/index.html#Handling-User-Input)Handling User Input](https://vuejs.org/v2/guide/index.html#Handling-User-Input)

To let users interact with your app, we can use the `v-on` directive to attach event listeners that invoke methods on our Vue instances:

|     |
| --- |
| <div  id="app-5"><br> <p>{{ message }}</p><br> <button  v-on:click="reverseMessage">Reverse Message</button><br></div><br>HTML |

|     |
| --- |
| var app5 = new Vue({<br> el: '#app-5',<br> data: {<br> message: 'Hello Vue.js!'<br>},<br> methods: {<br> reverseMessage: function () {<br> this.message = this.message.split('').reverse().join('')<br>}<br>}<br>})<br>JS |

Hello Vue.js!

Note in the method we simply update the state of our app without touching the DOM - all DOM manipulations are handled by Vue, and the code you write is focused on the underlying logic.

Vue also provides the `v-model` directive that makes two-way binding between form input and app state a breeze:

|     |
| --- |
| <div  id="app-6"><br> <p>{{ message }}</p><br> <input  v-model="message"><br></div><br>HTML |

|     |
| --- |
| var app6 = new Vue({<br> el: '#app-6',<br> data: {<br> message: 'Hello Vue!'<br>}<br>})<br>JS |

Hello Vue!

[

## [(L)](https://vuejs.org/v2/guide/index.html#Composing-with-Components)Composing with Components](https://vuejs.org/v2/guide/index.html#Composing-with-Components)

The component system is another important concept in Vue, because it’s an abstraction that allows us to build large-scale applications composed of small, self-contained, and often reusable components. If we think about it, almost any type of application interface can be abstracted into a tree of components:

![Component Tree](../_resources/0585c0c916e0666d70533c2bf658fc42.png)

In Vue, a component is essentially a Vue instance with pre-defined options. Registering a component in Vue is straightforward:

|     |
| --- |
| // Define a new component called todo-item<br>Vue.component('todo-item', {<br> template: '<li>This is a todo</li>'<br>})<br>JS |

Now you can compose it in another component’s template:

|     |
| --- |
| <ol><br> <!-- Create an instance of the todo-item component --><br> <todo-item></todo-item><br></ol><br>HTML |

But this would render the same text for every todo, which is not super interesting. We should be able to pass data from the parent scope into child components. Let’s modify the component definition to make it accept a [prop](https://vuejs.org/v2/guide/components.html#Props):

|     |
| --- |
| Vue.component('todo-item', {<br> // The todo-item component now accepts a<br> // "prop", which is like a custom attribute.<br> // This prop is called todo.<br>props: ['todo'],<br> template: '<li>{{ todo.text }}</li>'<br>})<br>JS |

Now we can pass the todo into each repeated component using `v-bind`:

|     |
| --- |
| <div  id="app-7"><br> <ol><br> <!-- Now we provide each todo-item with the todo object --><br> <!-- it's representing, so that its content can be dynamic --><br> <todo-item  v-for="item in groceryList"  v-bind:todo="item"></todo-item><br> </ol><br></div><br>HTML |

|     |
| --- |
| Vue.component('todo-item', {<br> props: ['todo'],<br> template: '<li>{{ todo.text }}</li>'<br>})<br>var app7 = new Vue({<br> el: '#app-7',<br> data: {<br> groceryList: [<br>{ text: 'Vegetables' },<br>{ text: 'Cheese' },<br>{ text: 'Whatever else humans are supposed to eat' }<br>]<br>}<br>})<br>JS |

1. Vegetables
2. Cheese
3. Whatever else humans are supposed to eat

This is just a contrived example, but we have managed to separate our app into two smaller units, and the child is reasonably well-decoupled from the parent via the props interface. We can now further improve our `<todo-item>` component with more complex template and logic without affecting the parent app.

In a large application, it is necessary to divide the whole app into components to make development manageable. We will talk a lot more about components [later in the guide](https://vuejs.org/v2/guide/components.html), but here’s an (imaginary) example of what an app’s template might look like with components:

|     |
| --- |
| <div  id="app"><br> <app-nav></app-nav><br> <app-view><br> <app-sidebar></app-sidebar><br> <app-content></app-content><br> </app-view><br></div><br>HTML |

[

### [(L)](https://vuejs.org/v2/guide/index.html#Relation-to-Custom-Elements)Relation to Custom Elements#](https://vuejs.org/v2/guide/index.html#Relation-to-Custom-Elements)

You may have noticed that Vue components are very similar to **Custom Elements**, which are part of the [Web Components Spec](http://www.w3.org/wiki/WebComponents/). That’s because Vue’s component syntax is loosely modeled after the spec. For example, Vue components implement the [Slot API](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/Slots-Proposal.md) and the `is` special attribute. However, there are a few key differences:

1. The Web Components Spec is still in draft status, and is not natively implemented in every browser. In comparison, Vue components don’t require any polyfills and work consistently in all supported browsers (IE9 and above). When needed, Vue components can also be wrapped inside a native custom element.

2. Vue components provide important features that are not available in plain custom elements, most notably cross-component data flow, custom event communication and build tool integrations.

[

## [(L)](https://vuejs.org/v2/guide/index.html#Ready-for-More)Ready for More?](https://vuejs.org/v2/guide/index.html#Ready-for-More)

We’ve just briefly introduced the most basic features of Vue.js core - the rest of this guide will cover them and other advanced features with much finer details, so make sure to read through it all!

 ← [Installation](https://vuejs.org/v2/guide/installation.html)  [The Vue Instance](https://vuejs.org/v2/guide/instance.html) →

Caught a mistake or want to contribute to the documentation? [Edit this page on Github!](https://github.com/vuejs/vuejs.org/blob/master/src/v2/guide/index.md)