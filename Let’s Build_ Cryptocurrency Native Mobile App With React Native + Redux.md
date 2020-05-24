Let’s Build: Cryptocurrency Native Mobile App With React Native + Redux

# Let’s Build: Cryptocurrency Native Mobile App With React Native + Redux

![](:/da8bc46fbe091ca087ed4d89061d846b)![1*qOezQp5s3C77rAkeAfJdKw.png](../_resources/af4a2cdde6e6a254b7f5cc6885a7710d.png)

#### Demo — What we will be building

![](../_resources/bfc8f4b03430219e9becd759997f62ee.png)![1*U9vDzwllsJcTBLZ988MURg.gif](../_resources/a72b4507ef4363083640b1404ccd7ed5.gif)

![](../_resources/23ae1c125e85772b5e6342a89b5366bc.png)![1*7MfXLCLmt-k6rQIPxay9IA.png](../_resources/3328f6c3f192f9ef9805b1f16099315c.png)

[The final product](https://expo.io/@indreklasn/react-native-redux-crypto-tracker)

* * *

*...*

Greetings fellow techies! It’s me, *Indrek*. I recently accepted a new job at Switzerland, Zurich **{Grotzi! — translation: Hi}** as a senior software engineer at one of the biggest banks. It’s been quite a challenge to move here but life has finally settled enough for me to write a new guide for you!

![](../_resources/c978f230b258427b8c6220a16472134d.png)![1*ZYZQw9V-piF9CMt-bLPpQQ.gif](../_resources/5b3e60f3f77a0553e764fc29823a43a8.gif)

P.S: *Switzerland *is a great choice if you’re looking for new adventures — recommend strongly! Food here is excellent and I love how patient and polite the people are.

* * *

*...*

I’m going to teach you how to write a native mobile app with**  **[**React Native**](https://facebook.github.io/react-native/docs/getting-started.html)and [**Redux**](http://redux.js.org/). Let’s dive in!

![](../_resources/5d5d065cb74462926d6b9e59cd7b292f.png)![1*EabXHpIAd7WwOu35w1PKcg.gif](../_resources/01718ac4a016d6f18ca5074ce9d7359e.gif)

* * *

*...*

### [What is React Native?](https://vuejs.org/v2/guide/#What-is-Vue-js)

> React Native lets you build mobile apps using only JavaScript. It uses the same design as React, letting you compose a rich mobile UI from declarative components

> [https://facebook.github.io/react-native/

[Not a problem if you’re not too comfortable with React — here’s a great React tutorial.](https://codeburst.io/learn-how-to-build-astronomy-picture-of-the-day-app-with-nasa-api-and-react-redux-e462ef0c806c?source=user_profile---------3-----------)

* * *

*...*

### Why are we using React Native instead of Swift, Kotlin, Java or Objective-C?

Well it all comes down to preference really. Here are the main scenarios.

- •Perhaps you already know some React — building React Native apps will be an absolute pleasure. RN tooling is great.
- •Cross platform. Learn once, write anywhere. Instead of writing your android app in Kotlin and your iOS app in Swift — you can write both of them in React Native and save a huge chunk of time and budget.
- •Easier to transition into mobile development from web background.
- •Javascript — one language to rule all.
- •Ability to quickly push updates directly to a published app — bypassing the app store review process and timeline. [Excellent post explaining how this is possible.](https://medium.com/react-native-training/understanding-react-native-deployments-6e54157920b7)

Please keep in mind — In the end, only one thing matters — whatever works **best for you **and **makes you happy.**

It’s fair to say React Native is mature by now. A lot of companies have adapted to RN (including Facebook native apps) — the demand is very high in the job market.

![](../_resources/58b460431954e03ca44e3330ccb30278.png)![1*jE48zbf7QkXWH0TAenRKbg.png](../_resources/c741c46c83934e1a63d9c8c0cc2b0202.png)

[RN Showcase](https://facebook.github.io/react-native/showcase.html)

* * *

*...*

### What is Redux?

> Redux is a predictable state container for JavaScript apps.
> [http://redux.js.org/

[If you’re not too familiar with Redux — here’s a nice walkthrough how to apply Redux to React apps.](https://medium.freecodecamp.org/learn-how-to-build-astronomy-picture-of-the-day-app-with-nasa-api-and-react-redux-part-ii-83f15970d0e3)

### Why are we using Redux?

- •Redux makes the complicated parts (state management) more predictable and easier to reason about.
- •Decouple state from views. What I mean by that exactly is let React handle the views and Redux handle the state of the app.
- •Clean code and best practices.
- •Great tooling and middleware to make developing more enjoyable.

* * *

*...*

### Get ready to boogie!

#### **Prerequisites:**

- •*NodeJS*
- •*NPM* or *Yarn*
- •*Bash command line/terminal.* By default Mac and Linux has it installed. If you’re on Windows — don’t worry —[ *follow this guide on how to install bash on Windows.*](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)*  ***Windows users — We won’t leave you behind! **😊
- •*Text Editor/IDE*
- •[Xcode](https://developer.apple.com/xcode/) (**iOS**) — *That’s all you need for the initial setup! — *[*Video Setup*](https://www.youtube.com/watch?v=K0y2tc38l2s)
- •[Android Studio](https://developer.android.com/studio/install.html) (**Android**) — [*Watch this tutorial to properly setup the android simulator!*](https://www.youtube.com/watch?v=Q0dERWCzoi0)
- •*Optional*: [Expo](https://expo.io/)— **recommended**!

[Watch this quick talk about “What is Expo?” ](https://facebook.github.io/react-native/blog/2017/03/13/introducing-create-react-native-app.html)— *mind-blowingly* innovative stuff!

Expo [Download link here.](https://expo.io/tools)

[Also recommend getting the expo-cli tooling!](https://docs.expo.io/versions/latest/guides/exp-cli.html)

Make sure you have everything required before continuing.

* * *

*...*

#### Begin by installing setting up our native app development environment.

Open our terminal and run couple commands for installing React Native and launching our preferred simulator.

`$ npm install -g create-react-native-app`

`$ create-react-native-app react-native-redux-crypto-tracker && cd react-native-redux-crypto-tracker`

You should end up with something close to this:

![](../_resources/08ea743173fec9a3425d468cdbe85d2e.png)
**Installing react-native and creating a react-native project**

We’re almost there. Next up we need to just serve our project. Type the next command in the terminal. You can choose between iOS or Android simulator. press **i** for **iOS** and **a** for **Android**. I have chosen **iOS** for this guide, but it works on both operating systems! I personally like both iPhone and Android phones (I’m not biased). Feel free to choose.

*(simulator) — *`$ npm run ios` — ***iOS***
*(simulator )— *`$ npm run android` — ***Android***

*(Physical Device )*— `$ npm run start` — **QR code **and** options**. Open your mobile camera and point it to the QR code. Also you’re going to need the [expo](http://expo.io/) app as well.

[Expo for Android](https://play.google.com/store/apps/details?id=host.exp.exponent&hl=en) — [Expo for iOS](https://itunes.apple.com/us/app/expo-client/id982107779?mt=8)

![](../_resources/a90a8c6f4fc51e40f4d31cd66cdb11c4.png)

![](../_resources/210ad6d47db3a5e6d92621b9b91bf582.png)

![](../_resources/e651fa38c81cb3ced2d88732a6e390d4.png)

the iPhone X simulator works beautifully in harmony with RN. Thanks Facebook team for the great, great implementation and execution! 👍

As we can see — there’s quite many things going on. From the top we can see
`import { StyleSheet, Text, View } from ‘react-native’;`
What is this exactly?

#### <Text>

`Text`>  is JSX - a syntax for embedding XML within JavaScript. Many frameworks use a special templating language which lets you embed code inside markup language. In React, this is reversed. JSX lets you write your markup language inside code. It looks like HTML on the web, except instead of web things like `<div>`>  or `<span>`> , you use React components. In this case, `<Text>`>  is a built-in component that just displays some text.

> TL;DR A React component for displaying text.

* * *

*...*

#### <View>

> The most fundamental component for building a UI, `View`>  is a container that supports layout with > [> flexbox](https://facebook.github.io/react-native/docs/flexbox.html)> , > [> style](https://facebook.github.io/react-native/docs/style.html)> , > [> some touch handling](https://facebook.github.io/react-native/docs/handling-touches.html)> , and > [> accessibility](https://facebook.github.io/react-native/docs/accessibility.html)>  controls. `View`>  maps directly to the native view equivalent on whatever platform React Native is running on, whether that is a `UIView`> , `<div>`> , `android.view`> , etc.

`View`>  is designed to be nested inside other views and can have 0 to many children of any type.

> This example creates a `View`>  that wraps two colored boxes and a text component in a row with padding.

* * *

*...*

#### StyleSheet

> A StyleSheet is an abstraction similar to CSS StyleSheets.
> Creates a new StyleSheet.

> Styling for RN is flex-box based. > [> Uses the Yoga layout engine.](https://facebook.github.io/yoga/)

> We pass styles to elements trough the `style`>  prop.

Not too comfortable with flexbox? No worries, [here are the best resources to master flexbox!](https://medium.com/@wesharehoodies/master-flexbox-with-these-3-fantastic-courses-for-free-432b1fcd4361)

* * *

*...*

![](../_resources/69c21a41d22076d20a9ed8d8b8e8842f.png)

* * *

*...*

### Building the app

Start by making a `src` directory where we place all our code.
`$ mkdir src && cd src`

inside src make a `components` directory. Inside the `components` we will be placing our views.

![](../_resources/72bf0135c3500b272b99ba07647e81c2.png)

#### Implementing the header

Make two files inside `src/components` — `Header.js `and `index.js`

`Header.js` is for the header of the app and `index.js` for making a import exports cleaner.

Inside `Header.js `— implement a stateless component — try to do it yourself, the most efficient way of learning is actually doing.

![](../_resources/329900b25040ff43cc3bba4fed4cadcd.png)

![](../_resources/fb25a69ea28d918f3944f405d601431e.png)

Next up — import the `Header.js` to the `App.js` and display it!

![](../_resources/ce59616d9cbd542a0d327bfcd52202e9.png)

Well how about that? It works! But wait... why is the title almost hidden by the iPhone default text? We will fix that in the next chapter!

### [Chapter 2 can be found here!](https://medium.com/@wesharehoodies/tutorial-react-native-redux-native-mobile-app-for-tracking-cryptocurrency-bitcoin-litecoin-810850cf8acc)

#### [In case you got lost, here’s the source code!](https://github.com/wesharehoodies/react-native-redux-crypto-tracker)

### Indrek