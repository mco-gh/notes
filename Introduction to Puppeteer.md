Introduction to Puppeteer

# Introduction to Puppeteer

## Introduction to programmatically controlling Chrome from Node.js

 Published Mar 04, 2019

Puppeteer is a Node library that we can use to control a [headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome) instance. We are basically use Chrome, but programmatically using JavaScript.

Using it, we can:

- scrape web pages
- automate form submissions
- perform any kind of browser automation
- track page loading performance
- create server-side rendered versions of single page apps
- make screenshots
- create automating testing
- generate PDF from web pages

It’s built by Google. It does not unlock anything new, per se, but it abstracts many of the nitty-gritty details we would have to deal with, without using it.

In short, it makes things very easy.

Since it spins up a new Chrome instance when it’s initialized, it might not be the most performant. It’s the most precise way to automate testing with Chrome though, since it’s using the *actual browser* under the hood.

To be precise, it uses Chromium the open source part of Chrome, which mostly means you don’t have the proprietary codecs that are licensed by Google and can’t be open sourced (MP3, AAC, H.264..) and you don’t have the integration with Google services like crash reports, Google update and more, but from a programmatic standpoint it should all be 100% similar to Chrome (except for media playing, as noted).

## Installing Puppeteer

Start by installing it using

	npm install puppeteer

in your project.
This will download and bundle the latest version of Chromium.

You can opt to make puppeteer run the local installation of Chrome you already have installed by installing `puppeteer-core` instead, which is useful in some special cases (see [puppeteer vs puppeteer-core](https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#puppeteer-vs-puppeteer-core)). Usually, you’d just go with `puppeteer`.

## Using Puppeteer

In a Node.js file, require it:

	const puppeteer = require('puppeteer');

then we can use the `launch()` method to create a browser instance:

	(async () => {
	  const browser = await puppeteer.launch()
	})()

We can write like this, too:

	puppeteer.launch().then(async browser => {
	  //...
	})

You can pass an object with options to `puppeteer.launch()`. The most common one is

	puppeteer.launch({ headless:false })

to show Chrome while Puppeteer is performing its operations. It can be nice to see what’s happening and debug.

We use `await`, and so we must wrap this method call in an [async function](https://flaviocopes.com/javascript-async-await/), which we [immediately invoke](https://flaviocopes.com/javascript-iife/).

Next we can use the `newPage()` method on the `browser` object to get the `page` object:

	(async () => {
	  const browser = await puppeteer.launch()
	  const page = await browser.newPage()
	})()

Next up we call the `goto()` method on the `page` object to load that page:

	(async () => {
	  const browser = await puppeteer.launch()
	  const page = await browser.newPage()
	  await page.goto('https://website.com')
	})()

We could use promises as well, instead of async/await, but using the latter makes things much more readable:

	(() => {
	  puppeteer.launch().then(browser => {
	    browser.newPage().then(page => {
	      page.goto('https://website.com').then(() => {
	        //...
	      })
	    })
	  })
	})()

## Getting the page content

Once we have a page loaded with a URL, we can get the page **content** calling the `evaluate()` method of `page`:

	(async () => {
	  const browser = await puppeteer.launch()
	  const page = await browser.newPage()
	  await page.goto('https://website.com')

		const result = await page.evaluate(() => {
	  	//...
		})
	})()

This method takes a callback function, where we can add the code needed to retrieve the elements of the page we need. We return a new object, and this will be the result of our `evaluate()` method call.

We can use the `page.$()` method to access the [Selectors API](https://flaviocopes.com/selectors-api/) method `querySelector()` on the document, and `page.$$()` as an alias to `querySelectorAll()`.

Once we are done with our calculations, we call the `close()` method on `browser`:

	browser.close()

## Page methods

We saw above the `page` object we get from calling `browser.newPage()`, and we called the `goto()` and `evaluate()` methods on it.

All methods return a promise, so they are normally prepended with the `await` keyword.

Let’s see *some* of the most common methods we will call. [You can see the full list on the Puppeteer docs](https://pptr.dev/#?product=Puppeteer&show=api-class-page).

### `page.$()`

Gives access to the [Selectors API](https://flaviocopes.com/selectors-api/) method `querySelector()` on the page

### `page.$$()`

Gives access to the [Selectors API](https://flaviocopes.com/selectors-api/) method `querySelectorAll()` on the page

### `page.$eval()`

Accepts 2 or more parameters. The first is a selector, the second a function. If there are more parameters, those are passed as additional arguments to the function.

It runs `querySelectorAll()` on the page, using the first parameter as selector, then it uses that parameter as the first argument to the function.

	const innerTextOfButton = await page.$eval('button#submit', el => el.innerText)

### `click()`

Perform a mouse click event on the element passed as parameter

	await page.click('button#submit')

We can pass an additional argument with an object of options:

- `button` can be set to `left` (default), `right` or `middle`
- `clickCount` is a number that defaults to 1 and sets how many times the element should be clicked
- `delay` is the number of milliseconds between the clicks. Default is `0`

### `content()`

Get the HTML source of a page

	const source = await page.content()

### `emulate()`

Emulates a device. It sets the user agent to a specific device, and sets the viewport accordingly.

The list of devices supported is available [in this file](https://github.com/GoogleChrome/puppeteer/blob/master/DeviceDescriptors.js).

Here’s how you emulate an iPhone X:
iPhone X

	const puppeteer = require('puppeteer');
	const device = require('puppeteer/DeviceDescriptors')['iPhone X'];

	puppeteer.launch().then(async browser => {
	  const page = await browser.newPage()
	  await page.emulate(device)

	  //do stuff

	  await browser.close()
	})

### `evaluate()`

Evaluates a function in the page context. Inside this function we have access to the `document` object, so we can call any DOM API:

	const puppeteer = require('puppeteer');

	(async () => {
	  const browser = await puppeteer.launch()
	  const page = await browser.newPage()
	  await page.goto('https://flaviocopes.com')

	  const result = await page.evaluate(() => {
	    return document.querySelectorAll('.footer-tags a').length
	  })

	  console.log(result)
	})()

Anything we call in here is executed in the page context, so if we run `console.log()`, we won’t see the result in the Node.js context because that’s executed in the headless browser.

We can calculate values here and return a JavaScript object, but if we want to return a DOM element and access it in the Node.js context, we must use a different method, `evaluateHandle()`. If we return a DOM element from evaluate(), we’ll just get an empty object.

### `evaluateHandle()`

Similar to evaluate(), but if we return a DOM element, we’ll get the proper object back rather than an empty object:

	const puppeteer = require('puppeteer');

	(async () => {
	  const browser = await puppeteer.launch()
	  const page = await browser.newPage()
	  await page.goto('https://flaviocopes.com')

	  const result = await page.evaluateHandle(() => {
	    return document.querySelectorAll('.footer-tags a')
	  })

	  console.log(result)
	})()

### `exposeFunction()`

This method allows you to add a new function in the browser context, that is executed in the Node.js context.

This means we can add a function that runs Node.js code inside the browser.

This example adds a test() function inside the browser context that reads an “app.js” file from the file system, with the path relative to the script:

	const puppeteer = require('puppeteer');
	const fs = require('fs');

	(async () => {
	  const browser = await puppeteer.launch()
	  const page = await browser.newPage()
	  await page.goto('https://flaviocopes.com')

	  await page.exposeFunction('test', () => {
	    const loadData = (path) => {
	      try {
	        return fs.readFileSync(path, 'utf8')
	      } catch (err) {
	        console.error(err)
	        return false
	      }
	    }
	    return loadData('app.js')
	  })

	  const result =  await page.evaluate(() => {
	    return test()
	  })

	  console.log(result)
	})()

### `focus()`

Focuses on the selector passed as parameter

	await page.focus('input#name')

### `goBack()`

Goes back in the page navigation history

	await page.goBack()

### `goForward()`

Goes forward in the page navigation history

	await page.goForward()

### `goto()`

Opens a new page.

	await page.goto('https://flaviocopes.com')

You can pass an object as a second parameter, with options. The `waitUntil` option, if passed the `networkidle2` value will wait until the navigation is complete:

	await page.goto('https://flaviocopes.com', {waitUntil: 'networkidle2'})

### `hover()`

Do a mouseover on the selector passed as parameter

	await page.hover('input#name')

### `pdf()`

Generate a PDF from a page. You can

	await page.pdf({ path: 'file.pdf })

You can pass many options to this method, to set the generated PDF details. [See the official docs](https://pptr.dev/#?product=Puppeteer&show=api-pagepdfoptions).

### `reload()`

Reload a page

	await page.reload()

### `screenshot()`

Takes a PNG screenshot of the page, saving it to the filename selected using `path`.

	await page.screenshot({path: 'screenshot.png'})

[See all the options](https://pptr.dev/#?product=Puppeteer&show=api-pagescreenshotoptions)

### `select()`

Select the DOM elements identified by the selector passed as parameter

	await page.select('input#name')

### `setContent()`

You can set the content of a page, rather than opening an existing web page.
Useful to programmatically generate PDFs or screenshots with existing HTML:

	const html = '<h1>Hello!</h1>'
	await page.setContent(html)
	await page.pdf({path: 'hello.pdf'})
	await page.screenshot({path: 'screenshot.png'})

### `setViewPort()`

By default the viewport is 800x600px. If you want to have a different viewport, maybe to take a screenshot, call `setViewport` passing an object with `width` and `height` properties.

	await page.setViewport({ width: 1280, height: 800 })

### `title()`

Get the page title

	await page.title()

### `type()`

Types into a selector that identifies a form element

	await page.type('input#name', 'Flavio')

The `delay` option allows to simulate typing like a real world user, adding delay between each character:

	await page.type('input#name', 'Flavio', {delay: 100})

### `url()`

Get the page URL

	await page.url()

### `viewport()`

Get the page viewport

	await page.viewport()

### `waitFor()`

Wait for something specific to happen. Has the following shortcut functions:

- `waitForFunction`
- `waitForNavigation`
- `waitForRequest`
- `waitForResponse`
- `waitForSelector`
- `waitForXPath`

Example:

	await page.waitFor(waitForNameToBeFilled)
	const waitForNameToBeFilled = () => page.$('input#name').value != ''

## Page namespaces

A page object gives you access to several different objects:

- [`accessibility`](https://pptr.dev/#?product=Puppeteer&show=api-class-accessibility)
- [`coverage`](https://pptr.dev/#?product=Puppeteer&show=api-class-coverage)
- [`keyboard`](https://pptr.dev/#?product=Puppeteer&show=api-class-keyboard)
- [`mouse`](https://pptr.dev/#?product=Puppeteer&show=api-class-mouse)
- [`touchscreen`](https://pptr.dev/#?product=Puppeteer&show=api-class-touchscreen)
- [`tracing`](https://pptr.dev/#?product=Puppeteer&show=api-class-tracing)

Each of those unlocks a whole lot of new functionality.

`keyboard` and `mouse` are most probably the ones you’ll use the most when trying to automate things.

For example this is how you trigger typing into an element (which should have been selected previously):

	await page.keyboard.type('hello!')

Other keyboard methods are

- `keyboard.down()` to send a keydown event
- `keyboard.press()` to send a keydown followed by a keyup (simulating a normal key type). Used mainly for modifier keys (shift, ctrl, cmd)
- `keyboard.sendCharacter()` sends a keypress event
- `keyboard.type()` sends a keydown, keypress and keyup event
- `keyboard.up()` to send a keyup event

All those receive a keyboard key code as defined in the US Keyboard Layout file: https://github.com/GoogleChrome/puppeteer/blob/master/lib/USKeyboardLayout.js. Normal characters and numbers are typed as-is, while special keys have a special code to define them.

`mouse` offers 4 methods:

- `mouse.click()` to simulate a click: `mousedown` and `mouseup` events
- `mouse.down()` to simulate a `mousedown` event
- `mouse.move()` to move to different coordinates
- `mouse.up()` to simulate a `mouseup` event