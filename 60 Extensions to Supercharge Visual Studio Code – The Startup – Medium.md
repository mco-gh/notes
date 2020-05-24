60 Extensions to Supercharge Visual Studio Code – The Startup – Medium

# 60 Extensions to *Supercharge* Visual Studio Code

[![1*hXzuBCvaHtOX6T6MzK-gyg.jpeg](../_resources/640c5e37fe273920045eb40f60f45c19.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='134' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@brandonburrus?source=post_header_lockup)

[Brandon Burrus](https://medium.com/@brandonburrus)

Jun 5·11 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='135'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

![](../_resources/d09aae26e30f526b8115f005fea7d52f.png)![0*EJJqHNu1lVK8LyLV](../_resources/45c0c4195883ce7429df70799494749d.jpg)

Photo by [Joshua Aragon](https://unsplash.com/@goshua13?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Visual Studio Code is absolutely awesome. Even out of the box, the editor can already do so much, especially for web developers. One of the major reasons that it’s so popular is that it has this unique ability to go from a strict text editor to a near full-blown IDE.

This is thanks to the fact that VSCode is *extremely* customizable. Every action you can think of in the editor? If it doesn’t already have a shortcut, you can definitely set one! Don’t like the color scheme? Yeah, there’s a setting for that too. But the real power of VSCode comes from its amazing extension marketplace.

Here’s a list of most of the extensions I make use of while using VSCode. I categorize them into four separate groups: general, specific, debugger, and snippet extensions. I definitely do not use all of these on a daily basis, but I’m also pretty good at getting rid of the ones I don’t need, or don’t make use of.

### General Extensions

These extensions are useful no matter what kind of language you’re writing code in!

#### [1. Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync)

If you work from multiple computers (like from work and home), this is a definite must-have. It doesn’t sync just your settings, it syncs all of your other extensions as well! It works by saving your complete VSCode setup to a GitHub Gist, and when you want to add another PC to sync with, all you have to do is put in your GitHub token and Gist ID!

#### [2. Intellicode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

If you take advantage of VSCode *Intellisense*, this extension makes that feature even better. The extension has AI-scanned a few languages and looks at the most common actions performed (for example, `array.length`). When VSCode actives *Intellisense*, it puts these common actions at the top of the list, denoting them with a star.

#### [3. Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

Collaboration is key! Live share lets you share a workspace (that includes both editors and terminals, too) with other people. It connects with your GitHub account, making working on a small group project, or doing pair coding incredibly easy. If you want to quickly sync everyone up during a hackathon, this is definitely the way to go.

#### [4. Code Time](https://marketplace.visualstudio.com/items?itemName=softwaredotcom.swdc-vscode)

Want to track your productivity? Code Time keeps stats on all kinds of things, from how long your coding sessions are, how many lines and words per day you average, even what your most productive time of day is. All of this presented either directly in VSCode, or from a neatly designed web dashboard. You can make a free account with them too, to keep track between multiple computers as well!

#### [5. Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)

If you want to find out who wrote the horrible line of code you’ve discovered in your codebase, Git History’s got you covered. It lets you see a color-coded history of any branch in the repository you’re currently in. It also lets you compare branches, search for specific changes and commits, and visually merge or rebase.

#### [6. TODO List](https://marketplace.visualstudio.com/items?itemName=TzachOvadia.todo-list)

Ever wonder if you’ve gotten to all of those *TODO*’s and *FIXME*’s before shipping that new feature to production? This extension’s got you covered, it adds a drawer to the Explorer view, listing out all of those to-do’s lying around your codebase. Oh, and you can export all of them to a Trello board or an email as well, did I mention that?

#### [7. Polacode](https://marketplace.visualstudio.com/items?itemName=pnp.polacode)

Ever want to take those slick looking screenshots of your code for twitter? That’s what this little extension does, and does *very well*. It uses the color scheme and font that you’re using to capture a stunning, high-resolution screenshot of whatever you currently have highlighted.

#### [8. Color Info](https://marketplace.visualstudio.com/items?itemName=bierner.color-info)

This one’s more for the designers, it adds a context menu popup that gives more info on selected color. Get the RGBA, CMYK, Hexadecimal, or HSL color info, or change the color directly using a nice color picker.

#### [9. Emoji Sense](https://marketplace.visualstudio.com/items?itemName=bierner.emojisense)

Emojis. Put them everywhere, hide them in your internal documentation for your coworkers to find, stick them in your README’s. Fairly straightforward, it lets you put emojis in whatever file you’re editing.

#### [10. SmoothType](https://marketplace.visualstudio.com/items?itemName=spikespaz.vscode-smoothtype)

SmoothType of those tiny tweaks that's barely noticeable, but is definitely one of those small *quality-of-life* changes that make your editing experience *better*. All it does is make the movements of your cursor animated, instead of that instant jump when your cursor moves to a different part of the page.

#### [11. Guides](https://marketplace.visualstudio.com/items?itemName=spywhere.guides)

VSCode actually has built-in guidelines (make sure you disable those after you install this one), but this makes those guidelines better. It’ll show you what indentation level you’re currently working at, hide guidelines when making a selection, and has better syntax support for various languages.

#### [12. Output Colorizer](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer)

Another one of those small quality-of-life extensions that doesn’t add any actual functionality, instead it adds some color to the output panel, as well as syntax coloring to log files. Just another small change, but definitely one that makes the editor just that much more enjoyable.

#### [13. Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

There’s a reason that I saved this one for the last of the general extensions, it’s a heavy hitter. This extension takes blazingly fast editing speed of the Vim editor and puts it right into VSCode. It’s great if you want to dip your toe into a bit of Vim, but personally, I love it because I get to get the speed of Vim combined with the power of VSCode. Not to mention that it still uses most of your `.vimrc` configuration, doubling the community of editor extensibility and plugins you can draw from.

### Specific Extensions

These are fairly language or file specific extensions. Personally, I write a lot of Javascript and Python, and so I have a lot of web and scripting related extensions!

#### [14. Auto Close Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag)

Insert an HTML tag, and this extension will automatically add the closing tag. This one alone can cut the time you have to spend writing HTML markup in half.

#### [15. Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)

Another HTML extension, except this one renames the matching tag if you change the other tag. This works no matter if you change the opening or closing tag as well.

#### [16. Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml)

Jinja is a templating language used by the Flask framework. *Better Jinja* takes your default syntax coloring scheme and applies it to every Jinja file format, including `.jinja`, `.jinja2`, and `.j2`.

#### [17. CDNjs](https://marketplace.visualstudio.com/items?itemName=JakeWilson.vscode-cdnjs)

Finding all of the CDNs for the quick libraries you want to pull in for that proof-of-concept you’re working on can be annoying. CDNjs takes care of all of that, adding in a search feature to find the right CDN you need. Especially useful for pulling in stuff like Bootstrap and Font Awesome.

#### [18. Docker](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker)

Make connecting to your containers easier than ever. Docker lets you add and manage all of your containers, images, and registries in a centralized location. (Especially useful for those of you who want to use your setup for work!)

#### [19. DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv)

Really straightforward extension, adds syntax highlighting to your `.env` files.

#### [20. ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

Using a linter can be the difference between good and great code. ESLint connects directly to your ESLint install, and integrations problem finding right into your editor. Write clean code, and catch those issues before you even know they’re issues.

#### [21. Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)

If you do any heavy lifting with data, especially with excel or `.csv` files, Excel Viewer is for you. It adds a nicely formatted viewing table for those types of files directly into VSCode.

#### [22. GI](https://marketplace.visualstudio.com/items?itemName=rubbersheep.gi)

Sometimes you forget to add that `.gitignore` file when you’re creating your repository. It happens to the best of us, and you sometimes don’t realize it until you’ve accidentally committed your `node_modules` folder to your repo. Gi lets you add that pesky `.gitignore` file directly from VSCode, and has presents for just about everything.

#### [23. GraphQL](https://marketplace.visualstudio.com/items?itemName=Prisma.vscode-graphql)

Syntax highlighting and more for GraphQL. Works in both `.gql` and `.graphql` files, as well as in ES6 `gql` template literal calls (for those of you who use Apollo). It also adds some really nice-to-haves, like definition jumping, schema validation, and snippets.

#### [24. Handlebars](https://marketplace.visualstudio.com/items?itemName=andrejunges.Handlebars)

Slightly obsolete now thanks to React, I do still find myself working in Handlebars from time to time. Handlebars adds two super simple things: syntax coloring, and some useful snippets.

#### [25. HTML Class Suggestions](https://marketplace.visualstudio.com/items?itemName=AndersEAndersen.html-class-suggestions)

If you’ve ever used a CSS framework, trying to remember even half a dozen of the many classes provided to you can be a nightmare. You end up having to keep a tab open to the documentation and have to constantly search around looking for a class you know the vague name of. No more, thanks to this one! This extension will put CSS class suggestions for you to use based on the linked stylesheets.

#### [26. HTML Tag Wrap](https://marketplace.visualstudio.com/items?itemName=bradgashler.htmltagwrap)

If I ever need to quickly surround a tag with another tag, `[surround.vim](https://github.com/tpope/vim-surround)` usually has me covered. This extension takes that idea to the next level, adding support for Emmet expansion. Make sure to set up a keybind for this one (I have mine set to `Opt + Shit + E`), and then proceed to edit HTML at the speed of thought.

#### [27. Image Minify](https://marketplace.visualstudio.com/items?itemName=axetroy.vscode-imagemin)

Quickly compress your pictures with this image minifier. You don’t lose quality and are able to deliver your content to the end-user faster. It’s a win-win situation.

#### [28. Lit It](https://marketplace.visualstudio.com/items?itemName=mohseenrm.lit-it)

Despite the cliché name, this extension helps you stub out *jsdoc* function docstrings. The generated stubs are usually pretty accurate too, as the extension looks at the method signature before generating the stub. All you have to do is write the important stuff.

#### [29. Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

If you’re a front-end developer of any sort, this extension is an absolute *must-have*. It spins up a dummy static server so you can test how content might actually look when it gets requested by the browser. Especially useful for when you run into those odd bugs just because you’re using the `file://` protocol in Chrome.

#### [30. Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

Write it in Markdown, export a PDF as output. Straight to the point, but surprisingly useful.

#### [31. Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)

Like most sane people, I have a dark color scheme for VSCode. Unfortunately, the built-in Markdown viewer for VSCode will take whatever your default background is for your editor, and use it as your Markdown background viewer. If you want to see what your README will actually look like directly in your editor, this one’s got you covered.

#### [32. Mongo Runner](https://marketplace.visualstudio.com/items?itemName=JoeyYiZhao.mongo-runner)

MongoDB is one of two databases that I’m almost always working with. Being able to run queries and do some basic database management from within VSCode without having to open Compass is such a time saver.

#### [33. MySQL](https://marketplace.visualstudio.com/items?itemName=formulahendry.vscode-mysql)

MySQL is the other database I’m usually working with. This extension isn’t as powerful as it’s Mongo counterpart, but it’s my preferred MySQL extension. It lets you add and manage multiple database connections, and run queries, which is usually all I need it for.

#### [34. Node TDD](https://marketplace.visualstudio.com/items?itemName=prashaantt.node-tdd)

Test-driven development has a nice output of producing very nice code that you already know is working, as you already have tests to tell you so. This extension lets you look to quickly see if your tests are passing at a glance.

#### [35. NPM](https://marketplace.visualstudio.com/items?itemName=eg2.vscode-npm-script)

Run NPM scripts directly from the command palette. The really interesting thing about this extension is that it connects to the touch bar on the new MacBooks Pros. It will also help you out by doing some preliminary `package.json` validation for you as well.

#### [36. NPM Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense)

Give Intellisense an upgrade and let it suggest what packages to import. This is especially useful for when you need to be efficient with what exactly you’re importing, in order to keep those bundle sizes down.

#### [37. Open in Browser](https://marketplace.visualstudio.com/items?itemName=techer.open-in-browser)

The majority of the time, you can just use Live Server to do the same thing. The reason I still keep this one installed is that it can also detect other browsers you have installed on your local machine, letting you quickly run and test your code quickly across various browsers.

#### [38. Paste JSON as Code](https://marketplace.visualstudio.com/items?itemName=quicktype.quicktype)

If you don’t write your backend with Node.js, defining the structure of a JSON response can be aggravating. This extension helps you out by letting you paste in a sample response (I like to use [Postman](https://www.getpostman.com/) for that), then generating the structure of the response that you need in your code.

#### [39. PDF](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf)

I didn’t even know I wanted to be able to view a PDF in VSCode until I found myself splitting my screen to write the code along with the book I was reading. The more I can stay in my editor, the happier I am!

#### [40. Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

This one can be a little tricky to get set up with ESLint, and will definitely require a bit of configuration to get the two working together smoothly. Once you do have the synced up, they make writing nice looking code a breeze!

#### [41. Random](https://marketplace.visualstudio.com/items?itemName=jrebocho.vscode-random)

Make writing random snapshot testing data a breeze with this one. This extension can generate random data for just about anything you can think of, names, cities, addresses, phone numbers, you name it.

#### [42. Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap)

Another one of those quality-of-life extensions, it’ll automatically wrap long lines of comments or documentation onto the next line. You can set exactly the amount of characters you want it to wrap too, to keep your formatting on point!

#### [43. Sass](https://marketplace.visualstudio.com/items?itemName=robinbentley.sass-indented)

Autocompletion and syntax highlighting for Sass files. Also comes with a couple of useful snippets, letting you write your sass code just a bit easier.

#### [44. Styled-Components](https://marketplace.visualstudio.com/items?itemName=jpoissonnier.vscode-styled-components)

Along the same school of thought as the GraphQL extension, this one instead adds CSS syntax highlighting for any styled-components template literals. I use a vibrant red color for strings that looks great until you get a giant wall of text, so this is a really nice extension to have. Just makes your component code look complete at a glance.

#### [45. SVG Viewer](https://marketplace.visualstudio.com/items?itemName=cssho.vscode-svgviewer)

VSCode has a built-in image viewer which is fantastic, but sometimes you need to view more than just JPEGs and PNGs.

#### [46. TSLint](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin)

Linting integration, but this one is for TypeScript instead of JavaScript. VSCode does the best it can with JavaScript IntelliSense, but with TypeScript, strong types just make it that much better.

#### [47. Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur)

Autocompletion, syntax coloring, Emmet support, and more for all of your markup, CSS, and JavaScript inside your `.vue` files. Without this extension, writing single-file-components in Vue can get quite messy.

#### [48. Vue Peek](https://marketplace.visualstudio.com/items?itemName=dariofuzinato.vue-peek)

Peeking is probably the most underrated feature of VSCode. This extension is for when you quickly need to look at references or definitions of something else inside your current file.

### Debugger Extensions

These extensions are very specific to what language you’re working in, I would definitely look to see if the language you code in has a debugger (spoiler alert: it probably does). Here are all the ones I personally use and recommend:

#### [49. Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome)

#### [50. Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

#### [51. React Native Tools](https://marketplace.visualstudio.com/items?itemName=msjsdiag.vscode-react-native)

### Snippet Extensions

These are also very specific to what environment you’re working in but are really useful. Snippets take care of all that structural and repetitive code that you end up writing for whatever you’re working on. The more snippets you know, the fast you can write the fun and important parts of your app!

#### [52. Django snippets](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)

#### [53. ES7/React/Redux/GraphQL snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets)

#### [54. Javascript/ES6+ snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets)

#### [55. jQuery snippets](https://marketplace.visualstudio.com/items?itemName=donjayamanne.jquerysnippets)

#### [56. MongoDB snippets for Node.js](https://marketplace.visualstudio.com/items?itemName=roerohan.mongo-snippets-for-node-js)

#### [57. Python snippets](https://marketplace.visualstudio.com/items?itemName=frhtylcn.pythonsnippets)

#### [58. React Apollo snippets](https://marketplace.visualstudio.com/items?itemName=leveluptutorials.react-apollo-snippets)

#### [59. Vue 2 snippets](https://marketplace.visualstudio.com/items?itemName=hollowtree.vue-snippets)

#### [60. Webpack snippets](https://marketplace.visualstudio.com/items?itemName=gogocrow.webpack-snippets)

### Conclusion

At the end of the day, my goal is to try and make VSCode as versatile as possible. Blazingly fast editing thanks to Vim, all the major boilerplate I need to write already done thanks to various snippets, and tooling for just about anything I need. All in one place, all thanks to Visual Studio Code.