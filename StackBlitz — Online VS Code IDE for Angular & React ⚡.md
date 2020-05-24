StackBlitz — Online VS Code IDE for Angular & React ⚡

# StackBlitz — Online VS Code IDE for Angular & React ⚡

![](../_resources/4f8545f75ba4d3345b9d5ab27568eb4e.png)![1*v6EdE1Fqm73BIaYgpM46_g.png](../_resources/35affcb7c54a50cf7a2d6b9a9e59a4ee.png)

After six months of hard work, I’m excited to finally announce [**StackBlitz**](https://stackblitz.com/)**! **You can check it out now over at [https://stackblitz.com](https://stackblitz.com/) 🎉

StackBlitz is an online IDE where you can create Angular & React projects that are immediately online & shareable via link… *in just one click.* 😮 It automatically takes care of installing dependencies, compiling, bundling, and hot reloading as you type:

![](../_resources/5ea2f1c656cc03b4e9c874fe2c7212db.png)![1*uf0RA0ofJi0m_mqdJxkTTg.gif](../_resources/b9c78f78537e9e7f1cf1928cfd9a07b6.gif)

We currently support creating & exporting Angular apps (based on `@angular/cli`) and React apps (based on `create-react-app`) with support for Vue & custom templates landing shortly.

### Why?

There is no greater buzzkill than having to configure deployment & build tools before you can start hammering out a cool prototype or demo. 😒

[Vjeux](https://medium.com/@vjeux) originally identified this problem in his challenge for [the best Javascript app prototyping setup](http://blog.vjeux.com/2015/javascript/challenge-best-javascript-setup-for-quick-prototyping.html) and we intentionally designed StackBlitz to complete (and in many ways *exceed*) his challenge’s requirements.

### StackBlitz feels & functions exactly like your local dev environment.

#### VS Code’s state of the art editing experience—now in your browser. 🛠

Intellisense smart completions (w/ type definitions from npm), Project Search (Cmd+P), Go to Definition, and other key VS Code features “just work” out of the box:

![](../_resources/84e0e6469a6399786512f9c0ac0b00fb.png)

#### Install & use packages from NPM 📦

Importing libraries is a critical & common part of developing apps. That’s why StackBlitz includes an *in-browser* npm client that supports installing multiple packages at a time & specific versions (ex: `react react-dom redux@3.7.2`)

You can also copy & paste code snippets from docs/blogs/etc into the editor and it’ll automatically detect the packages you’re missing 👌

![](../_resources/84135fc43cbc27f01403928d63ce800a.png)

How does it install so fast? Instead of downloading & extracting entire tarballs like npm & yarn normally do, your browser is intelligently downloading only the files your app needs from [Unpkg](https://unpkg.com/#/)**  **on demand.

#### **Preview & debug in a separate window, **just like you do locally 🖥

Say goodbye to the janky iframes online playgrounds force you to use 👋 Every StackBlitz project gets it’s very own unique URL where you can preview & debug live (with hot reloading!)

![](../_resources/0fd77a350eee4b7ae58b653b4556a28b.png)

We intentionally don’t include any noisy code (like analytics calls) on your live app URL, so your console & network tabs always reflect* only what your application is doing* 🙌

#### Keep on editing, even if you go offline 😮

StackBlitz utilizes**  **[Progressive Web App API’s](https://developers.google.com/web/progressive-web-apps/) to run a **live dev server in-browser**, so you can keep on coding whether you’re in a plane, on a train, or backseat Uber-ing in the rain (!):

![](../_resources/3b39f6052d4373e06eaae7d213888f14.png)

#### Import existing files & folders by simply dragging & dropping them into the editor ✨

No more copy + pasting, uploading, or git commands. Your browser immediately parses local files & folders and rebundles your project in the blink of an eye:

![](../_resources/2ad3b359e43429fe82a2b32cd300c8bf.png)

#### Share & embed 👀

Every project can be shared with others to view/fork & also comes with a revolutionary embed view that puts the full power of VS Code in your Medium articles, blog posts, and docs.

#### Download & run locally 💾

Clicking the “Export” button will download a ZIP file of your project configured to run with either `create-react-app` or `@angular/cli` (for React & Angular projects, respectively)

#### Your apps are always online 🌎

Your apps never go to sleep and have no bandwidth limits. Share the URL with as many friends, colleagues, and communities as you’d like!

#### Edit applications both small & large 💪

StackBlitz is the only in-browser environment that can handle live editing “the mother of all demo apps”: [**RealWorld**](https://github.com/gothinkster/realworld) (view the [React](https://stackblitz.com/edit/react-redux-realworld) and [Angular](https://stackblitz.com/edit/angular-realworld) implementations). TodoMVC, one of the most popular demo apps, [also runs smooth as butter](https://stackblitz.com/edit/react-redux-todomvc).

* * *

*...*

### The future is bright ⚡️

We have a ton of awesome features coming down the pipeline (Vue/custom templates support, import/export from GitHub, OTA hot reloading across devices, discoverability/social features, etc) and we’re working on open sourcing the core tech powering StackBlitz! You can follow our progress over at our [Github repo](https://github.com/stackblitz/core).

#### **We can’t wait to hear your feedback on StackBlitz — please feel free to tweet me **[**@ericsimons40**](https://twitter.com/ericsimons40)** or @**[**stackblitz**](https://twitter.com/stackblitz)** with any questions, feedback, ideas, etc :)**

### Special thanks 🙏

None of this would’ve been possible without the incredible work done by Guy Bedford on [**SystemJS**](https://github.com/systemjs/systemjs) and by Michael Jackson on the [**Unpkg**](https://unpkg.com/#/) CDN service. These are the two key technologies that really enabled us to pack all of the functionality* inside of your web browser* with virtually no server-side involvement.

We’d also like to thank the VS Code team for their awesome editor — we ❤ Microsoft!

Finally, thanks so much to my best friends & StackBlitz co-creators [@iamalbertpai](https://twitter.com/iamalbertpai) and [@clayschneider](https://twitter.com/clayschneider) who worked tirelessly with me to build this amazing project ❤

Onwards!