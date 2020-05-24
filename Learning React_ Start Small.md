Learning React? Start Small.

# Learning React? Start Small.

 ** June 20, 2017
 [** Follow @dceddia](https://twitter.com/intent/follow?screen_name=dceddia)
 ![Learning React? Start Small.](../_resources/7bc2fc4c7225a208603c2306e9389222.png)
>

> I have been trying to learn React for the past year now, on and off. No matter how much I try, I just cannot seem to get off the tutorials. The code just isn’t intuitive.

It is *seriously* frustrating to work through a tutorial, come out with a glimmer of hope, and have that hope smashed to bits when you realize you *don’t really understand* enough to make your own app.

If that’s you, I have some advice: start small. I mean *really* small.

## Do Little Experiments

What kinds of things have you tried to build on your own? How “big” are they?

I didn’t fully grok props and state until I built a few *really* small apps with React. I think “experiments” would be a better term.

Experiments are throwaways. Experiments aren’t scary. There’s very little at stake. There’s no architecture to worry about, no design, no grand vision. There are only a handful of discrete steps and if you screw up badly enough you can literally delete the thing and start over.

Tiny little experiment apps like this:

- render “hello world”

- render a few nested plain old HTML elements to get a feel for JSX

- “refactor” hello world into 2 components, `Hello` and `World`. Nest them inside `HelloWorld`.

- make `World` accept an optional prop, the “name” to display, and render it.

- create a static array of things, like `const items = [{id: 1, name: "one"}, {id: 2, name: "two"}]`. Create a component that takes “items” as a prop and uses `items.map(...)` to render the list of items.

- Make a counter. Initial state: count = 0. Have a “+” button and a “-“ button that change the count by setting state.

- Put the counter state in the root component, and put the buttons that increment/decrement it in a child a few levels below. Pass the increment/decrement functions down as props so that the children can update the parent’s state.

You get the idea. Really small things. *Incremental* things. These barely qualify as “apps,” but they are exactly what will get you from the frustration of doing tutorials and having the knowledge slip through your fingers, to actually writing your own app.

These tiny experiments could even live under the same folder, as components within a larger app, but I like the idea of making separate ones because it drills the basics into your fingers.

## Muscle Memory

Nobody talks about this, and it might seem stupid, but I think it’s really important to learn the basic “React app” structure cold. I’m talking about the basic “boilerplate” to make an app:

	import React from 'react';
	import ReactDOM from 'react-dom';

	const Hello = () => <div>Hello</div>

	ReactDOM.render(<Hello/>, document.querySelector('#root'));

Sure, you can rely on `create-react-app` to generate it for you. But you can’t fool your brain. It *knows* that you have no idea what those `import`s do, and that if they suddenly vanished you wouldn’t know how to write them from scratch. That little bit of fear is paralyzing.

So shine a light in those dark corners: learn those lines cold, learn what they do, and make sure you can write them blindfolded.

Use `create-react-app`, but delete everything under src and recreate index.js by hand for 3-5 apps in a row until it sticks. I think there’s a lot of cognitive overhead when you look at a file and think “I can’t touch those generated lines because I don’t know what they do.”

## Go Practice!

React is a skill like any other, and nobody is born knowing how to be a frontend developer. Put in some quality time practicing, making little experiments, and you will improve. Then you’ll be ready to tackle the app idea in your head.

Any time you run into another tricky part, *practice it in isolation*.

Learning Redux? Spin up a little sandbox app where you can mess around without breaking anything.

Not sure how to make a layout with React Bootstrap? Don’t mangle up your main project – that’s just disheartening, and you have to undo all the failed work. Make an experiment app instead.

Practice new skills in isolation.

### Download a Timeline for Learning React

![content_Screen_Shot_2017-05-01_at_11.31.01_AM.png](../_resources/9a640d970b4b0ccb50f3119a2230607b.png)

Sign up and get my React Learning Timeline PDF and weekly articles about React and JavaScript.

 First Name

 Email Address

 We use this field to detect spam bots. If you fill this in, you will be marked as a spammer.

  Weekly-ish articles about React and JS. [Powered by ConvertKit](https://convertkit.com/?utm_campaign=poweredby)