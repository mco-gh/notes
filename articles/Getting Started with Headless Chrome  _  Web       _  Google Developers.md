Getting Started with Headless Chrome  |  Web       |  Google Developers

star_border
star_border
star_border
star_border
star_border

#  Getting Started with Headless Chrome

- [Contents](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)
- [Starting Headless (CLI)](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- [Command line features](https://developers.google.com/web/updates/2017/04/headless-chrome#command_line_features_features)
    - [Printing the DOM](https://developers.google.com/web/updates/2017/04/headless-chrome#printing_the_dom_dom)
    - [Create a PDF](https://developers.google.com/web/updates/2017/04/headless-chrome#create_a_pdf_dom)

    -
-
-
    -
    -
-
-
-

 ![Eric Bidelman](../_resources/1e8bc065b5d6955c1bb5b95a9bc4fdce.jpg)

 **By**    [EricBidelman](https://developers.google.com/web/resources/contributors#ericbidelman)

Engineer @ Google working on Lighthouse, Web Components, Chrome, and the web

### TL;DR

[Headless Chrome](https://chromium.googlesource.com/chromium/src/+/lkgr/headless/README.md)is shipping in Chrome 59. It's a way to run the Chrome browser in a headless environment. Essentially, running Chrome without chrome! It brings **all modern web platform features** provided by Chromium and the Blink rendering engine to the command line.

Why is that useful?

A headless browser is a great tool for automated testing and server environments where you don't need a visible UI shell. For example, you may want to run some tests against a real web page, create a PDF of it, or just inspect how the browser renders an URL.

error**Caution:** Headless mode is available on Mac and Linux in **Chrome 59**.[Windows support](https://bugs.chromium.org/p/chromium/issues/detail?id=686608) is coming soon! To check what version of Chrome you have, open `chrome://version`.

## [arrow_upward](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)Starting Headless (CLI)

The easiest way to get started with headless mode is to open the Chrome binary from the command line. If you've got Chrome 59+ installed, start Chrome with the `--headless` flag:

hdr_strong
content_copy

`chrome \[[NEWLINE]]  --headless \                   # Runs Chrome in headless mode.[[NEWLINE]]  --disable-gpu \                # Temporarily needed for now.[[NEWLINE]]  --remote-debugging-port=9222 \[[NEWLINE]]  https://www.chromestatus.com   # URL to open. Defaults to about:blank.[[NEWLINE]]`

star**Note:** Right now, you'll also want to include the `--disable-gpu` flag. That will eventually go away.

`chrome` should point to your installation of Chrome. The exact location will vary from platform to platform. Since I'm on Mac, I created convenient aliases for each version of Chrome that I have installed.

If you're on the stable channel of Chrome and cannot get the Beta, I recommend using `chrome-canary`:

hdr_strong
content_copy

`alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"[[NEWLINE]]alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"[[NEWLINE]]alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"[[NEWLINE]]`

Download Chrome Canary [here](https://www.google.com/chrome/browser/canary.html).

## [arrow_upward](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)Command line features

In some cases, you may not need to [programmatically script](https://developers.google.com/web/updates/2017/04/headless-chrome#node) Headless Chrome. There are some [useful command line flags](https://cs.chromium.org/chromium/src/headless/app/headless_shell_switches.cc)to perform common tasks.

### Printing the DOM

The `--dump-dom` flag prints `document.body.innerHTML` to stdout:
hdr_strong
content_copy

`chrome --headless --disable-gpu --dump-dom https://www.chromestatus.com/[[NEWLINE]]`

### Create a PDF

The `--print-to-pdf` flag creates a PDF of the page:
hdr_strong
content_copy

`chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/[[NEWLINE]]`

### Taking screenshots

To capture a screenshot of a page, use the `--screenshot` flag:
hdr_strong
content_copy

`chrome --headless --disable-gpu --screenshot https://www.chromestatus.com/[[NEWLINE]][[NEWLINE]]# Size of a standard letterhead.[[NEWLINE]]chrome --headless --disable-gpu --screenshot --window-size=1280,1696 https://www.chromestatus.com/[[NEWLINE]][[NEWLINE]]# Nexus 5x[[NEWLINE]]chrome --headless --disable-gpu --screenshot --window-size=412,732 https://www.chromestatus.com/[[NEWLINE]]`

Running with `--screenshot` will produce a file named `screenshot.png` in the current working directory. If you're looking for full page screenshots, things are a tad more involved. There's a great blog post from David Schnurr that has you covered. Check out [Using headless Chrome as an automated screenshot tool](https://medium.com/@dschnr/using-headless-chrome-as-an-automated-screenshot-tool-4b07dffba79a).

## [arrow_upward](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)Debugging Chrome without a browser UI?

When you run Chrome with `--remote-debugging-port=9222`, it starts an instance with the [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) enabled. The protocol is used to communicate with Chrome and drive the headless browser instance. It's also what tools like Sublime, VS Code, and Node use for remote debugging an application. #synergy

Since you don't have browser UI to see the page, navigate to `http://localhost:9222`in another browser to check that everything is working. You'll see a list of inspectable pages where you can click through and see what Headless is rendering:

 ![DevTools Remote ](../_resources/8ce6cd50ba7b4ed8d82a5a30386ea758.png)
DevTools remote debugging UI

From here, you can use the familiar DevTools features to inspect, debug, and tweak the page as you normally would. If you're using Headless programmatically, this page is also a powerful debugging tool for seeing all the raw DevTools protocol commands going across the wire, communicating with the browser.

## [arrow_upward](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)Using programmatically (Node)

### Launching Chrome

In the previous section, we [started Chrome manually](https://developers.google.com/web/updates/2017/04/headless-chrome#cli) using `--headless --remote-debugging-port=9222`. However, to fully automate tests, you'll probably want to spawn Chrome *from* your application.

One way is to use `child_process`:
hdr_strong
content_copy

`const exec = require('child_process').exec;[[NEWLINE]][[NEWLINE]]function launchHeadlessChrome(url, callback) {[[NEWLINE]]  // Assuming MacOSx.[[NEWLINE]]  const CHROME = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome';[[NEWLINE]]  exec(`${CHROME} --headless --disable-gpu --remote-debugging-port=9222 ${url}`, callback);[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]launchHeadlessChrome('https://www.chromestatus.com', (err, stdout, stderr) => {[[NEWLINE]]  ...[[NEWLINE]]});[[NEWLINE]]`

But things get tricky if you want a portable solution that works across multiple platforms. Just look at that hard-coded path to Chrome :(

#### Using Lighthouse's ChromeLauncher

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) is a marvelous tool for testing the quality of your web apps. One thing people don't realize is that it ships with some really nice helper modules for working with Chrome. One of those modules is `ChromeLauncher`. `ChromeLauncher` will find where Chrome is installed, set up a debug instance, launch the browser, and kill it when your program is done. Best part is that it works cross-platform thanks to Node!

star**Note:** The Lighthouse team is exploring a standalone package for `ChromeLauncher` with an improved API. Let us know if you have [feedback](https://github.com/GoogleChrome/lighthouse/issues/2092).

By default, **`ChromeLauncher` will try to launch Chrome Canary** (if it's installed), but you can change that to manually select which Chrome to use. To use it, first install Lighthouse from npm:

hdr_strong
content_copy
`yarn add lighthouse[[NEWLINE]]`
**Example** - using `ChromeLauncher` to launch Headless
hdr_strong
content_copy

`const {ChromeLauncher} = require('lighthouse/lighthouse-cli/chrome-launcher');[[NEWLINE]][[NEWLINE]]/**[[NEWLINE]] * Launches a debugging instance of Chrome on port 9222.[[NEWLINE]] * @param {boolean=} headless True (default) to launch Chrome in headless mode.[[NEWLINE]] *     Set to false to launch Chrome normally.[[NEWLINE]] * @return {Promise<ChromeLauncher>}[[NEWLINE]] */[[NEWLINE]]function launchChrome(headless = true) {[[NEWLINE]]  const launcher = new ChromeLauncher({[[NEWLINE]]    port: 9222,[[NEWLINE]]    autoSelectChrome: true, // False to manually select which Chrome install.[[NEWLINE]]    additionalFlags: [[[NEWLINE]]      '--window-size=412,732',[[NEWLINE]]      '--disable-gpu',[[NEWLINE]]      headless ? '--headless' : ''[[NEWLINE]]    ][[NEWLINE]]  });[[NEWLINE]][[NEWLINE]]  return launcher.run().then(() => launcher)[[NEWLINE]]    .catch(err => {[[NEWLINE]]      return launcher.kill().then(() => { // Kill Chrome if there's an error.[[NEWLINE]]        throw err;[[NEWLINE]]      }, console.error);[[NEWLINE]]    });[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]launchChrome(true).then(launcher => {[[NEWLINE]]  ...[[NEWLINE]]});[[NEWLINE]]`

Running this script doesn't do much, but you should see an instance of Chrome fire up in the task manager that loaded `about:blank`. Remember, there won't be any browser UI. We're headless.

To control the browser, we need the DevTools protocol!

### Retrieving information about the page

[chrome-remote-interface](https://www.npmjs.com/package/chrome-remote-interface)is a great Node package that provides usable APIs for the[DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/). You can use it to orchestrate Headless Chrome, navigate to pages, and fetch information about those pages.

warning**Warning:** The DevTools protocol can do a ton of interesting stuff, but it can be a bit daunting at first. I recommend spending a bit of time browsing the [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/), first. Then, move on to the `chrome-remote-interface` API docs to see how it wraps the raw protocol.

Let's install the library:
hdr_strong
content_copy
`yarn add chrome-remote-interface[[NEWLINE]]`

#### Examples

**Example** - print the user agent
hdr_strong
content_copy

`launchChrome().then(launcher => {[[NEWLINE]]  chrome.Version().then(version => console.log(version['User-Agent']));[[NEWLINE]]});[[NEWLINE]]`

Results in something like: `HeadlessChrome/60.0.3082.0`

**Example** - check if the site has a [web app manifest](https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/)

hdr_strong
content_copy

`const chrome = require('chrome-remote-interface');[[NEWLINE]][[NEWLINE]]function onPageLoad(Page) {[[NEWLINE]]  return Page.getAppManifest().then(response => {[[NEWLINE]]    if (!response.url) {[[NEWLINE]]      console.log('Site has no app manifest');[[NEWLINE]]      return;[[NEWLINE]]    }[[NEWLINE]]    console.log('Manifest: ' + response.url);[[NEWLINE]]    console.log(response.data);[[NEWLINE]]  });[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]launchChrome().then(launcher => {[[NEWLINE]][[NEWLINE]]  chrome(protocol => {[[NEWLINE]]    // Extract the parts of the DevTools protocol we need for the task.[[NEWLINE]]    // See API docs: https://chromedevtools.github.io/devtools-protocol/[[NEWLINE]]    const {Page} = protocol;[[NEWLINE]][[NEWLINE]]    // First, enable the Page domain we're going to use.[[NEWLINE]]     Page.enable().then(() => {[[NEWLINE]]      Page.navigate({url: 'https://www.chromestatus.com/'});[[NEWLINE]][[NEWLINE]]      // Wait for window.onload before doing stuff.[[NEWLINE]]      Page.loadEventFired(() => {[[NEWLINE]]        onPageLoad(Page).then(() => {[[NEWLINE]]          protocol.close();[[NEWLINE]]          launcher.kill(); // Kill Chrome.[[NEWLINE]]        });[[NEWLINE]]      });[[NEWLINE]]    });[[NEWLINE]][[NEWLINE]]  }).on('error', err => {[[NEWLINE]]    throw Error('Cannot connect to Chrome:' + err);[[NEWLINE]]  });[[NEWLINE]][[NEWLINE]]});[[NEWLINE]]`

**Example** - extract the `<title>` of the page using DOM APIs.
hdr_strong
content_copy

`const chrome = require('chrome-remote-interface');[[NEWLINE]][[NEWLINE]]function onPageLoad(Runtime) {[[NEWLINE]]  const js = "document.querySelector('title').textContent";[[NEWLINE]][[NEWLINE]]  // Evaluate the JS expression in the page.[[NEWLINE]]  return Runtime.evaluate({expression: js}).then(result => {[[NEWLINE]]    console.log('Title of page: ' + result.result.value);[[NEWLINE]]  });[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]launchChrome().then(launcher => {[[NEWLINE]][[NEWLINE]]  chrome(protocol => {[[NEWLINE]]    // Extract the parts of the DevTools protocol we need for the task.[[NEWLINE]]    // See API docs: https://chromedevtools.github.io/devtools-protocol/[[NEWLINE]]    const {Page, Runtime} = protocol;[[NEWLINE]][[NEWLINE]]    // First, need to enable the domains we're going to use.[[NEWLINE]]    Promise.all([[[NEWLINE]]      Page.enable(),[[NEWLINE]]      Runtime.enable()[[NEWLINE]]    ]).then(() => {[[NEWLINE]]      Page.navigate({url: 'https://www.chromestatus.com/'});[[NEWLINE]][[NEWLINE]]      // Wait for window.onload before doing stuff.[[NEWLINE]]      Page.loadEventFired(() => {[[NEWLINE]]        onPageLoad(Runtime).then(() => {[[NEWLINE]]          protocol.close();[[NEWLINE]]          launcher.kill(); // Kill Chrome.[[NEWLINE]]        });[[NEWLINE]]      });[[NEWLINE]][[NEWLINE]]    });[[NEWLINE]][[NEWLINE]]  }).on('error', err => {[[NEWLINE]]    throw Error('Cannot connect to Chrome:' + err);[[NEWLINE]]  });[[NEWLINE]][[NEWLINE]]});[[NEWLINE]]`

## [arrow_upward](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)Further resources

Here are some useful resources to get you started:
Docs

- [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/) - API reference docs

Tools

- [chrome-remote-interface](https://www.npmjs.com/package/chrome-remote-interface) - node module that wraps the DevTools protocol
- [Lighthouse](https://github.com/GoogleChrome/lighthouse) - automated tool for testing the quality of web apps

Demos

- "[The Headless Web](https://paul.kinlan.me/the-headless-web/)" - Paul Kinlan's great blog post on using Headless with api.ai.

## [arrow_upward](https://developers.google.com/web/updates/2017/04/headless-chrome#top_of_page)FAQ

**Do I need the `--disable-gpu` flag?**

Yes, for now. The `--disable-gpu` flag is a temporary requirement to work around a few bugs. You won't need this flag in future versions of Chrome. See [https://crbug.com/546953#c152](https://bugs.chromium.org/p/chromium/issues/detail?id=546953#c152) and [https://crbug.com/695212](https://bugs.chromium.org/p/chromium/issues/detail?id=695212) for more information.

**So I still need Xvfb?**

No. Headless Chrome doesn't use a window so a display server like Xvfb is no longer needed. You can happily run your automated tests without it.

What is Xvfb? Xvfb is an in-memory display server for Unix-like systems that enables you to run graphical applications (like Chrome) without an attached physical display. Many people use Xvfb to run earlier versions of Chrome to do "headless" testing.

**How do I create a Docker container that runs Headless Chrome?**

Check out [lighthouse-ci](https://github.com/ebidel/lighthouse-ci). It has an[example Dockerfile](https://github.com/ebidel/lighthouse-ci/blob/master/builder/Dockerfile)that uses Ubuntu as a base image, and installs + runs Lighthouse in an App Engine Flexible container.

**Can I use this with Selenium / WebDriver / ChromeDriver**?

Right now, Selenium opens a full instance of Chrome. In other words, it's an automated solution but not completely headless. However, Selenium could use`--headless` in the future.

If you want to bleed on the edge, I recommend [Running Selenium with Headless Chrome](https://intoli.com/blog/running-selenium-with-headless-chrome/) to set things up yourself.

star**Note:** you may encounter bugs using [ChromeDriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver). At the time of writing, the latest release (2.29) only supports Chrome 58. Headless Chrome requires Chrome 59 or later.

**How is this related to PhantomJS?**

Headless Chrome is similar to tools like [PhantomJS](http://phantomjs.org/). Both can be used for automated testing in a headless environment. The main difference between the two is that Phantom uses an older version of WebKit as its rendering engine while Headless Chrome uses the latest version of Blink.

At the moment, Phantom also provides a higher level API than the [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/).

**Where do I report bugs?**

For bugs against Headless Chrome, file them on [crbug.com](https://bugs.chromium.org/p/chromium/issues/entry?components=Blink&blocking=705916&cc=skyostil%40chromium.org&Proj=Headless).

For bugs in the DevTools protocol, file them at [github.com/ChromeDevTools/devtools-protocol](https://github.com/ChromeDevTools/devtools-protocol/issues/new).

45 comments

[![photo.jpg](../_resources/46d0e580386337d1385bccaa4ac6a5ad.jpg)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg.png](../_resources/93e516a36ba3f8171098f3d4e8623a0c.png)](https://apis.google.com/u/0/wm/1/106207080329016565093)

### [可可](https://apis.google.com/u/0/wm/1/106207080329016565093)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12ut5fjwlbkffdqh04ccb2grzvty5kh3qs0k)  -  Shared publicly

awsome
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/36362fdf879b25c000eba09556aa4e23.jpg)](https://apis.google.com/u/0/wm/1/115984864101389808197)

### [Андрей Лавров](https://apis.google.com/u/0/wm/1/115984864101389808197)

[2 weeks ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13vuroyamnnezwwf04cebx40wrxejvyij0)  -  Shared publicly

Can Google Chrome browser windows be accessed from other computer in normal (none headless) mode via DevTools protocol?

+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/609d80d458f59b988e9b3becb658b006.jpg)](https://apis.google.com/u/0/wm/1/105803916387944536602)

### [Siddharth Kulkarni](https://apis.google.com/u/0/wm/1/105803916387944536602)

[2 weeks ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12swdiysnz3jxni304cefdz1mfezlywxcw)  -  Shared publicly

Great write up. Need more content though.
+
1
2
1

 ·
Reply

[![uFp_tsTJboUY7kue5XAsGA=s46.png](../_resources/7edd40c55661866d46596dde591820ce.png)](https://apis.google.com/u/0/wm/1/107958118937265746400)

### [Chris LaRose](https://apis.google.com/u/0/wm/1/107958118937265746400)

[3 days ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12ucvibqvruz5okb22ntppwkof4en0y504)  -  Shared publicly

XVFB still seems to be required with chrome --headless for simulating keystrokes. See chromium issue here: https://bugs.chromium.org/p/chromedriver/issues/detail?id=1772

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/70f8446c16deadc1ed749de7bf59fce4.jpg)](https://apis.google.com/u/0/wm/1/104366587312747359979)

### [Kyriakos Ktorides](https://apis.google.com/u/0/wm/1/104366587312747359979)

[4 days ago (edited)](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13hupiigvqdfhuw404cjvsasm3jdrtxx1s)  -  Shared publicly

Is it possible to customize the PDF Header/Footer?

Are css print stylesheet rules obeyed? (e.g. page-breaks etc)
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/2a82a02dca553556ca2ed4064d8e4c77.jpg)](https://apis.google.com/u/0/wm/1/118266697593849669416)

### [Peter Lyons](https://apis.google.com/u/0/wm/1/118266697593849669416)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12syrjony2fflzc222ggpqqkyu3srn2h)  -  Shared publicly

Is there a way to disable the PDF header/footer (title, page number, url)?
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/313d2ce5b59890a23ce27fb917723c61.jpg)](https://plus.google.com/103365468132266305205)

[黄宇天](https://plus.google.com/103365468132266305205)

[5 days ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12syrjony2fflzc222ggpqqkyu3srn2h)

+
0
1
0

Add a style like this, '<style>@page{size: auto; margin: 0mm; body: {margin: 20mm 15mm;background: [#fff](https://apis.google.com/s/%23fff);}}</style>', That just put the header/footer behind the body, not really disable it.

[![photo.jpg](../_resources/30249e4ca0672ff1fe754a9e4da6f091.jpg)](https://apis.google.com/u/0/wm/1/109817888360233104491)

### [Richard Lee Gaas](https://apis.google.com/u/0/wm/1/109817888360233104491)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13fhhrpewz1frhub230uxqxkrjlul25u04)  -  Shared publicly

Nice
+
0
1
0

 ·
Reply

[(L)](https://apis.google.com/u/0/wm/1/106303849653090693845)

### [Rama Kunchanapalli](https://apis.google.com/u/0/wm/1/106303849653090693845)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13izjzj3mnxivpri04ceftgvkrsxroomgo)  -  Shared publicly

When I may expect chromedriver new version that supports headless? I tried latest chrome canary with Selenium and chromedriver 2.29 but have issues.?

+
0
1
0

[![photo.jpg](../_resources/e887dda721144d55588ba760b6a764d2.jpg)](https://apis.google.com/u/0/wm/1/113525015220376733647)

### [龚振华](https://apis.google.com/u/0/wm/1/113525015220376733647)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z120evsauqvdyf3iv04cinfpvpmdutiyip00k)  -  Shared publicly

good news.
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/9e50f354a796e312da8e9964721461c1.jpg)](https://apis.google.com/u/0/wm/1/115867327413773990570)

### [Washington Soares](https://apis.google.com/u/0/wm/1/115867327413773990570)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13sth4y0xqjixnb104cevvogoavj1oynzw0k)  -  Shared publicly

awesome!
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/cbaa7fa7e76be638469fa695223a0009.jpg)](https://apis.google.com/u/0/wm/1/111303854518568006628)

### [Sumit Pande](https://apis.google.com/u/0/wm/1/111303854518568006628)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z124i5gyuqy0sxeh304cc30xsp3xix2qhxw0k)  -  Shared publicly

Is there any timeline for availability of headless support on Windows?
+
2
3
2

 ·
Reply

[![photo.jpg](../_resources/713e26b83711368fc412f4224b992f1d.jpg)](https://apis.google.com/u/0/wm/1/100639469112143709011)

### [Ishmeet Singh](https://apis.google.com/u/0/wm/1/100639469112143709011)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12xdpahem2ozp1wr04ccd2wjwaqd1wzdr40k)  -  Shared publicly

Awesome work chrome team! You are making chrome omnipresent.
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/897e346f46841cb441021d9754dc84a9.jpg)](https://apis.google.com/u/0/wm/1/117096721201425635743)

### [Ivan Li](https://apis.google.com/u/0/wm/1/117096721201425635743)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12jdxdabtfwfbizm04cd1eoomz0dt24xgw)  -  Shared publicly

awesome!
1: can we launch multiple concurrent process to print web page to pdf?

2: do we have options to specify the output pdf name? it's always output.pdf for now

+
2
3
2

 ·
Reply

[![photo.jpg](:/33ccd442a961934e0d42b2a86a326181)](https://apis.google.com/u/0/wm/1/112983694407641081015)

### [Louis Lu](https://apis.google.com/u/0/wm/1/112983694407641081015)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12mildrsyv1upfqy04cdjuycp2yitsox5c)  -  Shared publicly

Scrapy's new backend is here.
+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/4959ec23071a8eaafa8c96a475e1b00c.png)](https://apis.google.com/u/0/wm/1/113331645312253432477)

### [Communist](https://apis.google.com/u/0/wm/1/113331645312253432477)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z130zlpp0qamcniip04cdx2wxljxxjdich0)  -  Shared publicly

Real good!
+
0
1
0

[![photo.jpg](../_resources/7b8d810a5a6717535acaa7b02b1e9580.jpg)](https://apis.google.com/u/0/wm/1/106653007438254140662)

### [Seth Westphal](https://apis.google.com/u/0/wm/1/106653007438254140662)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13ztjh5qw2eghqji04cflrqopqndp2asec)  -  Shared publicly

In the "print the user agent" example, where is the `chrome` variable coming from?

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/1ddda047666ed8e0c606d512759bb371.jpg)](https://plus.google.com/+SethWestphal92)

[Seth Westphal](https://plus.google.com/+SethWestphal92)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13ztjh5qw2eghqji04cflrqopqndp2asec)

+
0
1
0

It's `const chrome = require('chrome-remote-interface');`

[![photo.jpg](../_resources/d4c58f846899097ea38c4019154db300.jpg)](https://apis.google.com/u/0/wm/1/103974130702350532968)

### [noah grant.](https://apis.google.com/u/0/wm/1/103974130702350532968)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12vjtya5xitxlhja04cftjiuriwsbopfgw)  -  Shared publicly

Cool! How do you imagine this integrating with CI builds? Will we be able to add chrome as an npm devDependency?

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/db1e093ceff9ae9f8582c6906b906124.jpg)](https://apis.google.com/u/0/wm/1/118343599998075710887)

### [aljoša gomilšek (papak)](https://apis.google.com/u/0/wm/1/118343599998075710887)

[1 week ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12fhx34htnqehgjp04cctapzmz1zrzazyo0k)  -  Shared publicly

will gpu acceleration be (eventualy) enabled? as I can see "it is needed for now"

+
0
1
0

[![photo.jpg.png](../_resources/5f064ae532f7db2d889328a51659c2c8.png)](https://apis.google.com/u/0/wm/1/109546115122963288515)

### [Jeffrey McMahan](https://apis.google.com/u/0/wm/1/109546115122963288515)

[2 weeks ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z12ux5kplw3tgnbss23pyrfjeoroylork04)  -  Shared publicly

"It's also what tools like Sublime, VS Code, and Node use for remote debugging..." Sublime?

+
3
4
3

[![photo.jpg](../_resources/979255abdc8952a90170261097b765d1.jpg)](https://apis.google.com/u/0/wm/1/110830991477757973296)

### [naveen agarwal](https://apis.google.com/u/0/wm/1/110830991477757973296)

[2 weeks ago](https://developers.google.com/web/updates/2017/04/headless-chrome?google_comment_id=z13dcntjon2cfrxxp04ch54aivvdjzcwskc0k)  -  Shared publicly

How it is better than the already available testing frameworks like cucumber with selenium or poltergeist driver which provide all these features in nice wrapper?

+
1
2
1

 ·
Reply

Show more

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated May 12, 2017.