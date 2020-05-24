jdan/cleaver

###    README.md

# [(L)](https://github.com/jdan/cleaver#cleaver)Cleaver

30-second Slideshows for Hackers. http://jdan.github.io/cleaver/

[[68747470733a2f2f62616467652e667572792e696f2f6a732f636c65617665722e737667](../_resources/af3359b6a330e8be6d21e0274c77bc30.bin)](https://travis-ci.org/jdan/cleaver)[[68747470733a2f2f7472617669732d63692e6f72672f6a64616e2f636c65617665722e737667](../_resources/bd617ff128f729eaabf5b6b2e40bedd8.bin)](http://badge.fury.io/js/cleaver)

## [(L)](https://github.com/jdan/cleaver#intro)Intro

Cleaver turns this:

	title: Basic Example
	author:
	  name: Jordan Scales
	  twitter: jdan
	  url: http://jordanscales.com
	output: basic.html
	controls: true

	--

	# Cleaver 101
	## A first look at quick HTML presentations

	--

	### A textual example

	Content can be written in **Markdown!** New lines no longer need two angle brackets.

	This will be in a separate paragraph

	--

	### A list of things

	* Item 1
	* Item B
	* Item gamma

	No need for multiple templates!

Into this:

[![68747470733a2f2f692e636c6f756475702e636f6d2f634973734b466a6342362e676966](../_resources/673e540999c8a43276a0b7761df09c44.gif)](https://camo.githubusercontent.com/131ce23a9c1861a06b13f09c6ea54285ee202f8e/68747470733a2f2f692e636c6f756475702e636f6d2f634973734b466a6342362e676966)

## [(L)](https://github.com/jdan/cleaver#quick-start)Quick Start

Get it [on NPM](https://npmjs.org/package/cleaver):
npm install -g cleaver# To update: npm update -g cleaver
And run it like so:
cleaver path/to/something.md
You can also watch for changes on a file and automatically recompile with:

cleaver watch path/to/something-changing.md# Watching for changes on presentation.md. Ctrl-C to abort.# Rebuilding: Thu Nov 07 2013 00:15:03 GMT-0500 (EST)# Rebuilding: Thu Nov 07 2013 00:15:21 GMT-0500 (EST)# Rebuilding: Thu Nov 07 2013 00:16:01 GMT-0500 (EST)# Rebuilding: Thu Nov 07 2013 00:16:09 GMT-0500 (EST)

Use the `--debug` flag to display debug information:
$ cleaver --debug examples/basic.md
cleaver loaded input document +0ms
helper read /Users/jordan/Projects/cleaver/templates/layout.mustache +0ms
helper read /Users/jordan/Projects/cleaver/templates/author.mustache +0ms
helper read /Users/jordan/Projects/cleaver/templates/default.mustache +0ms
cleaver loaded templates +3ms
cleaver parsed metadata +4ms
helper read /Users/jordan/Projects/cleaver/resources/default.css +13ms
helper read /Users/jordan/Projects/cleaver/resources/github.css +0ms
helper read /Users/jordan/Projects/cleaver/resources/script.js +0ms
cleaver loaded static assets +9ms
cleaver rendered slides +1ms
cleaver rendered presentation +1ms

## [(L)](https://github.com/jdan/cleaver#more-info)More Info

**Cleaver** is a one-stop shop for generating HTML presentations in record time. Using some spiced up markdown, you can produce good-looking, interactive presentations with a just a few lines of text.

Slides are written in [Markdown](http://daringfireball.net/projects/markdown/), and are separated by two dashes (`--`).

## [(L)](https://github.com/jdan/cleaver#options)Options

	title: Basic Example
	author:
	  name: Jordan Scales
	  twitter: jdan
	  url: http://jordanscales.com
	style: basic-style.css
	output: basic.html

Cleaver supports several basic options that allow you to further customize the look and feel of your presentation, including author info, stylesheets, and custom templates.

See the documentation on[options](https://github.com/jdan/cleaver/blob/master/docs/options.md) for more information.

Be sure to check out the [wiki](https://github.com/jdan/cleaver/wiki) as well.

## [(L)](https://github.com/jdan/cleaver#themes)Themes

Check out the [themes](https://github.com/jdan/cleaver/wiki/Theme-Index)page on our [wiki](http://github.com/jdan/cleaver/wiki).

	title: Theme Example
	output: theme.html
	theme: jdan/cleaver-retro

Cleaver has substantial theme support to give you more fine-grained control over your presentation, similar to [options](https://github.com/jdan/cleaver#options). Instead of manually specifying a stylesheet, template, layout, and others, you can specify a single theme containing each of these assets. More specifically, a theme may contain:

- style.css - styles for your presentation
- template.mustache - a template used to render the slides in your presentation
- layout.mustache - a template used to render the entire document of your presentation
- script.js - javascript to be included in your slideshow

A theme does not need to contain all of these files, only the ones present will be loaded into your slideshow.

### [(L)](https://github.com/jdan/cleaver#examples)Examples

- [jdan/cleaver-retro](http://github.com/jdan/cleaver-retro)

[![68747470733a2f2f692e636c6f756475702e636f6d2f484c7463504a574a4a6c2d3132303078313230302e706e67](../_resources/774dbeb79180372fd6e0819b402a8874.png)](https://camo.githubusercontent.com/f8090bcd22781ac5eaa845b6552683c4b293fed8/68747470733a2f2f692e636c6f756475702e636f6d2f484c7463504a574a4a6c2d3132303078313230302e706e67)

- [matmuchrapna/cleaver-ribbon](http://github.com/matmuchrapna/cleaver-ribbon)– [Shower](http://shwr.me/) implemented in cleaver.

[![68747470733a2f2f692e636c6f756475702e636f6d2f474543457835426d78492d3132303078313230302e706e67](../_resources/f2591f58e28f368e694778289f9db6eb.png)](https://camo.githubusercontent.com/4d1ec02bb46c1036244408ddf5f3104acbd4d5bf/68747470733a2f2f692e636c6f756475702e636f6d2f474543457835426d78492d3132303078313230302e706e67)

- [sudodoki/reveal-cleaver-theme](http://github.com/sudodoki/reveal-cleaver-theme)– cleaver meets [reveal.js](http://lab.hakim.se/reveal-js/#/).

[![68747470733a2f2f692e636c6f756475702e636f6d2f776c7a6973444c6533322d3132303078313230302e706e67](../_resources/83321d89b17d94070f4e32c74b45ed3a.png)](https://camo.githubusercontent.com/869ba61d71912115017c621801844c2f18840f5d/68747470733a2f2f692e636c6f756475702e636f6d2f776c7a6973444c6533322d3132303078313230302e706e67)

### [(L)](https://github.com/jdan/cleaver#specifying-themes)Specifying Themes

Themes may be specified by one of the following options:

- An absolute or relative path to a directory
- A URL to a directory
- A github repository in the form of *username/reponame*

### [(L)](https://github.com/jdan/cleaver#overriding-themes)Overriding Themes

By default, *style.css* and *script.js* will be **appended** to the default stylesheets and javascripts included in cleaver presentations. If you wish to completely override these defaults, you must include another file in your theme - settings.json - corresponding to the following:

{ "override": true}
Template files will automatically override the default templates.

### [(L)](https://github.com/jdan/cleaver#more-info-1)More Info

For more information on themes, check out[our documentation](https://github.com/jdan/cleaver/blob/master/docs/themes.md).

## [(L)](https://github.com/jdan/cleaver#markup)Markup

Cleaver slides are rendered using the following template:

{{#slides}} <div  class="slide{{#hidden}} hidden{{/hidden}}  {{classList}}"  id="slide-{{id}}">

<section  class="slide-content">{{{content}}}</section>
</div>{{/slides}}
And produce the following markup:

	+-------------------------------+
	| #slide-N                      |
	|     +-------------------+     |
	|     | .slide-content    |     |
	|     |                   |     |
	|     |                   |     |
	|     |                   |     |
	|     |                   |     |
	|     +-------------------+     |
	|                               |
	|                               |
	| (navigation)                  |
	+-------------------------------+

**#slide-N** (for example, *#slide-3*) allows you to identify a particular full-bleed slide by its position in the slideshow. It extends to the bounds of the page.

**.slide-content** is a smaller window which holds the actual content of the slide.

### [(L)](https://github.com/jdan/cleaver#class-list)Class List

A class list can be placed after each "slice" (denoted `--`) to help you style individual slides without worrying about their index.

	-- bg

	This slide will have a class "bg" associated with it

	-- bg blink

	This one, too, but it will also have the class "blink"

## [(L)](https://github.com/jdan/cleaver#slide-types)Slide Types

### [(L)](https://github.com/jdan/cleaver#title-slide)Title slide

	# Cleaver 101
	## A first look at quick HTML presentations

**h1** and **h2** elements (prefaced with *#* and *##* respectively), will automatically include padding to render a title slide.

### [(L)](https://github.com/jdan/cleaver#other-slides)Other slides

	### A list of things

	* Item 1
	* Item B
	* Item gamma

	No need for multiple templates!

Since slides are written in [Markdown](http://daringfireball.net/projects/markdown/), you can include things like lists, images, and arbitrary HTML.

**h3** tags (prefaced `###`) are automatically given a bottom border to represent a slide title.

## [(L)](https://github.com/jdan/cleaver#navigation)Navigation

Cleaver supports keyboard navigation for switching between slides. Alternatively, click the control buttons located below the presentation.

To navigate the slideshow:

- **forward**: K, L, UP, RIGHT, PgDn, and Space
- **reverse**: H, J, LEFT, DOWN, PgUp, and Backspace

The toggle fullscreen mode, press the **ENTER** key.

## [(L)](https://github.com/jdan/cleaver#contributing)Contributing

- Fork it
- Clone it
- Install dependencies (`npm install`)
- Checkout a release branch (`git checkout -b feature/cool-wordart`)
- Make changes, commit, and push (`npm test` and make sure it passes)
- Open a pull request!

With <3,
[@jdan](http://jordanscales.com/)
--
[MIT Licensed](https://github.com/jdan/cleaver/blob/master/LICENSE)