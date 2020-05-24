JavaScript Promises: an Introduction  |  Web Fundamentals       |  Google Developers

star_border
star_border
star_border
star_border
star_border

#  JavaScript Promises: an Introduction

 ![Jake Archibald](../_resources/35ace996b13ad5407e9ed3cc23697d90.jpg)

 **By**    [JakeArchibald](https://developers.google.com/web/resources/contributors#jakearchibald)

Human boy working on web standards at Google

Developers, prepare yourself for a pivotal moment in the history of web development.

*[Drumroll begins]*
Promises have arrived natively in JavaScript!
*[Fireworks explode, glittery paper rains from above, the crowd goes wild]*
At this point you fall into one of these categories:

- People are cheering around you, but you're not sure what all the fuss is about. Maybe you're not even sure what a "promise" is. You'd shrug, but the weight of glittery paper is weighing down on your shoulders. If so, don't worry about it, it took me ages to work out why I should care about this stuff. You probably want to begin at the [beginning](https://developers.google.com/web/fundamentals/primers/promises#whats-all-the-fuss-about).
- You punch the air! About time right? You've used these Promise things before but it bothers you that all implementations have a slightly different API. What's the API for the official JavaScript version? You probably want to begin with the [terminology](https://developers.google.com/web/fundamentals/primers/promises#promise-terminology).
- You knew about this already and you scoff at those who are jumping up and down like it's news to them. Take a moment to bask in your own superiority, then head straight to the [API reference](https://developers.google.com/web/fundamentals/primers/promises#promise-api-reference).

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)What's all the fuss about?

JavaScript is single threaded, meaning that two bits of script cannot run at the same time; they have to run one after another. In browsers, JavaScript shares a thread with a load of other stuff that differs from browser to browser. But typically JavaScript is in the same queue as painting, updating styles, and handling user actions (such as highlighting text and interacting with form controls). Activity in one of these things delays the others.

As a human being, you're multithreaded. You can type with multiple fingers, you can drive and hold a conversation at the same time. The only blocking function we have to deal with is sneezing, where all current activity must be suspended for the duration of the sneeze. That's pretty annoying, especially when you're driving and trying to hold a conversation. You don't want to write code that's sneezy.

You've probably used events and callbacks to get around this. Here are events:
hdr_strong
content_copy

`var img1 = document.querySelector('.img-1');[[NEWLINE]][[NEWLINE]]img1.addEventListener('load', function() {[[NEWLINE]]  // woo yey image loaded[[NEWLINE]]});[[NEWLINE]][[NEWLINE]]img1.addEventListener('error', function() {[[NEWLINE]]  // argh everything's broken[[NEWLINE]]});[[NEWLINE]]`

This isn't sneezy at all. We get the image, add a couple of listeners, then JavaScript can stop executing until one of those listeners is called.

Unfortunately, in the example above, it's possible that the events happened before we started listening for them, so we need to work around that using the "complete" property of images:

hdr_strong
content_copy

`var img1 = document.querySelector('.img-1');[[NEWLINE]][[NEWLINE]]function loaded() {[[NEWLINE]]  // woo yey image loaded[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]if (img1.complete) {[[NEWLINE]]  loaded();[[NEWLINE]]}[[NEWLINE]]else {[[NEWLINE]]  img1.addEventListener('load', loaded);[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]img1.addEventListener('error', function() {[[NEWLINE]]  // argh everything's broken[[NEWLINE]]});[[NEWLINE]]`

This doesn't catch images that error'd before we got a chance to listen for them; unfortunately the DOM doesn't give us a way to do that. Also, this is loading one image, things get even more complex if we want to know when a set of images have loaded.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Events aren't always the best way

Events are great for things that can happen multiple times on the same object—keyup, touchstart etc. With those events you don't really care about what happened before you attached the listener. But when it comes to async success/failure, ideally you want something like this:

hdr_strong
content_copy

`img1.callThisIfLoadedOrWhenLoaded(function() {[[NEWLINE]]  // loaded[[NEWLINE]]}).orIfFailedCallThis(function() {[[NEWLINE]]  // failed[[NEWLINE]]});[[NEWLINE]][[NEWLINE]]// and…[[NEWLINE]]whenAllTheseHaveLoaded([img1, img2]).callThis(function() {[[NEWLINE]]  // all loaded[[NEWLINE]]}).orIfSomeFailedCallThis(function() {[[NEWLINE]]  // one or more failed[[NEWLINE]]});[[NEWLINE]]`

This is what promises do, but with better naming. If HTML image elements had a "ready" method that returned a promise, we could do this:

hdr_strong
content_copy

`img1.ready().then(function() {[[NEWLINE]]  // loaded[[NEWLINE]]}, function() {[[NEWLINE]]  // failed[[NEWLINE]]});[[NEWLINE]][[NEWLINE]]// and…[[NEWLINE]]Promise.all([img1.ready(), img2.ready()]).then(function() {[[NEWLINE]]  // all loaded[[NEWLINE]]}, function() {[[NEWLINE]]  // one or more failed[[NEWLINE]]});[[NEWLINE]]`

At their most basic, promises are a bit like event listeners except:

- A promise can only succeed or fail once. It cannot succeed or fail twice, neither can it switch from success to failure or vice versa.
- If a promise has succeeded or failed and you later add a success/failure callback, the correct callback will be called, even though the event took place earlier.

This is extremely useful for async success/failure, because you're less interested in the exact time something became available, and more interested in reacting to the outcome.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Promise terminology

[Domenic Denicola](https://twitter.com/domenic) proof read the first draft of this article and graded me "F" for terminology. He put me in detention, forced me to copy out[States and Fates](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md)100 times, and wrote a worried letter to my parents. Despite that, I still get a lot of the terminology mixed up, but here are the basics:

A promise can be:

- **fulfilled** - The action relating to the promise succeeded
- **rejected** - The action relating to the promise failed
- **pending** - Hasn't fulfilled or rejected yet
- **settled** - Has fulfilled or rejected

[The spec](https://people.mozilla.org/~jorendorff/es6-draft.html#sec-promise-objects)also uses the term **thenable** to describe an object that is promise-like, in that it has a `then` method. This term reminds me of ex-England Football Manager [Terry Venables](https://en.wikipedia.org/wiki/Terry_Venables) so I'll be using it as little as possible.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Promises arrive in JavaScript!

Promises have been around for a while in the form of libraries, such as:

- [Q](https://github.com/kriskowal/q)
- [when](https://github.com/cujojs/when)
- [WinJS](https://msdn.microsoft.com/en-us/library/windows/apps/br211867.aspx)
- [RSVP.js](https://github.com/tildeio/rsvp.js)

The above and JavaScript promises share a common, standardized behaviour called [Promises/A+](https://github.com/promises-aplus/promises-spec). If you're a jQuery user, they have something similar called[Deferreds](https://api.jquery.com/category/deferred-object/). However, Deferreds aren't Promise/A+ compliant, which makes them[subtly different and less useful](https://thewayofcode.wordpress.com/tag/jquery-deferred-broken/), so beware. jQuery also has[a Promise type](https://api.jquery.com/Types/#Promise), but this is just a subset of Deferred and has the same issues.

Although promise implementations follow a standardized behaviour, their overall APIs differ. JavaScript promises are similar in API to RSVP.js. Here's how you create a promise:

hdr_strong
content_copy

`var promise = new Promise(function(resolve, reject) {[[NEWLINE]]  // do a thing, possibly async, then…[[NEWLINE]][[NEWLINE]]  if (/* everything turned out fine */) {[[NEWLINE]]    resolve("Stuff worked!");[[NEWLINE]]  }[[NEWLINE]]  else {[[NEWLINE]]    reject(Error("It broke"));[[NEWLINE]]  }[[NEWLINE]]});[[NEWLINE]]`

The promise constructor takes one argument, a callback with two parameters, resolve and reject. Do something within the callback, perhaps async, then call resolve if everything worked, otherwise call reject.

Like `throw` in plain old JavaScript, it's customary, but not required, to reject with an Error object. The benefit of Error objects is they capture a stack trace, making debugging tools more helpful.

Here's how you use that promise:
hdr_strong
content_copy

`promise.then(function(result) {[[NEWLINE]]  console.log(result); // "Stuff worked!"[[NEWLINE]]}, function(err) {[[NEWLINE]]  console.log(err); // Error: "It broke"[[NEWLINE]]});[[NEWLINE]]`

`then()` takes two arguments, a callback for a success case, and another for the failure case. Both are optional, so you can add a callback for the success or failure case only.

JavaScript promises started out in the DOM as "Futures", renamed to "Promises", and finally moved into JavaScript. Having them in JavaScript rather than the DOM is great because they'll be available in non-browser JS contexts such as Node.js (whether they make use of them in their core APIs is another question).

Although they're a JavaScript feature, the DOM isn't afraid to use them. In fact, all new DOM APIs with async success/failure methods will use promises. This is happening already with[Quota Management](https://dvcs.w3.org/hg/quota/raw-file/tip/Overview.html#idl-def-StorageQuota),[Font Load Events](http://dev.w3.org/csswg/css-font-loading/#font-face-set-ready),[ServiceWorker](https://github.com/slightlyoff/ServiceWorker/blob/cf459d473ae09f6994e8539113d277cbd2bce939/service_worker.ts#L17),[Web MIDI](https://webaudio.github.io/web-midi-api/#widl-Navigator-requestMIDIAccess-Promise-MIDIOptions-options),[Streams](https://github.com/whatwg/streams#basereadablestream), and more.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Browser support & polyfill

There are already implementations of promises in browsers today.

As of Chrome 32, Opera 19, Firefox 29, Safari 8 & Microsoft Edge, promises are enabled by default.

To bring browsers that lack a complete promises implementation up to spec compliance, or add promises to other browsers and Node.js, check out[the polyfill](https://github.com/jakearchibald/ES6-Promises#readme)(2k gzipped).

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Compatibility with other libraries

The JavaScript promises API will treat anything with a `then()` method as promise-like (or `thenable` in promise-speak *sigh*), so if you use a library that returns a Q promise, that's fine, it'll play nice with the new JavaScript promises.

Although, as I mentioned, jQuery's Deferreds are a bit … unhelpful. Thankfully you can cast them to standard promises, which is worth doing as soon as possible:

hdr_strong
content_copy
`var jsPromise = Promise.resolve($.ajax('/whatever.json'))[[NEWLINE]]`

Here, jQuery's `$.ajax` returns a Deferred. Since it has a `then()` method,`Promise.resolve()` can turn it into a JavaScript promise. However, sometimes deferreds pass multiple arguments to their callbacks, for example:

hdr_strong
content_copy

`var jqDeferred = $.ajax('/whatever.json');[[NEWLINE]][[NEWLINE]]jqDeferred.then(function(response, statusText, xhrObj) {[[NEWLINE]]  // ...[[NEWLINE]]}, function(xhrObj, textStatus, err) {[[NEWLINE]]  // ...[[NEWLINE]]})[[NEWLINE]]`

Whereas JS promises ignore all but the first:
hdr_strong
content_copy

`jsPromise.then(function(response) {[[NEWLINE]]  // ...[[NEWLINE]]}, function(xhrObj) {[[NEWLINE]]  // ...[[NEWLINE]]})[[NEWLINE]]`

Thankfully this is usually what you want, or at least gives you access to what you want. Also, be aware that jQuery doesn't follow the convention of passing Error objects into rejections.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Complex async code made easier

Right, let's code some things. Say we want to:
1. Start a spinner to indicate loading

2. Fetch some JSON for a story, which gives us the title, and urls for each chapter

3. Add title to the page
4. Fetch each chapter
5. Add the story to the page
6. Stop the spinner

… but also tell the user if something went wrong along the way. We'll want to stop the spinner at that point too, else it'll keep on spinning, get dizzy, and crash into some other UI.

Of course, you wouldn't use JavaScript to deliver a story,[serving as HTML is faster](https://jakearchibald.com/2013/progressive-enhancement-is-faster/), but this pattern is pretty common when dealing with APIs: Multiple data fetches, then do something when it's all done.

To start with, let's deal with fetching data from the network:

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Promisifying XMLHttpRequest

Old APIs will be updated to use promises, if it's possible in a backwards compatible way. `XMLHttpRequest` is a prime candidate, but in the mean time let's write a simple function to make a GET request:

hdr_strong
content_copy

`function get(url) {[[NEWLINE]]  // Return a new promise.[[NEWLINE]]  return new Promise(function(resolve, reject) {[[NEWLINE]]    // Do the usual XHR stuff[[NEWLINE]]    var req = new XMLHttpRequest();[[NEWLINE]]    req.open('GET', url);[[NEWLINE]][[NEWLINE]]    req.onload = function() {[[NEWLINE]]      // This is called even on 404 etc[[NEWLINE]]      // so check the status[[NEWLINE]]      if (req.status == 200) {[[NEWLINE]]        // Resolve the promise with the response text[[NEWLINE]]        resolve(req.response);[[NEWLINE]]      }[[NEWLINE]]      else {[[NEWLINE]]        // Otherwise reject with the status text[[NEWLINE]]        // which will hopefully be a meaningful error[[NEWLINE]]        reject(Error(req.statusText));[[NEWLINE]]      }[[NEWLINE]]    };[[NEWLINE]][[NEWLINE]]    // Handle network errors[[NEWLINE]]    req.onerror = function() {[[NEWLINE]]      reject(Error("Network Error"));[[NEWLINE]]    };[[NEWLINE]][[NEWLINE]]    // Make the request[[NEWLINE]]    req.send();[[NEWLINE]]  });[[NEWLINE]]}[[NEWLINE]]`

Now let's use it:
hdr_strong
content_copy

`get('story.json').then(function(response) {[[NEWLINE]]  console.log("Success!", response);[[NEWLINE]]}, function(error) {[[NEWLINE]]  console.error("Failed!", error);[[NEWLINE]]})[[NEWLINE]]`

[Click here to see that in action](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/story.json), check the console in DevTools to see the result. Now we can make HTTP requests without manually typing `XMLHttpRequest`, which is great, because the less I have to see the infuriating camel-casing of `XMLHttpRequest`, the happier my life will be.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Chaining

`then()` isn't the end of the story, you can chain `then`s together to transform values or run additional async actions one after another.

### Transforming values

You can transform values simply by returning the new value:
hdr_strong
content_copy

`var promise = new Promise(function(resolve, reject) {[[NEWLINE]]  resolve(1);[[NEWLINE]]});[[NEWLINE]][[NEWLINE]]promise.then(function(val) {[[NEWLINE]]  console.log(val); // 1[[NEWLINE]]  return val + 2;[[NEWLINE]]}).then(function(val) {[[NEWLINE]]  console.log(val); // 3[[NEWLINE]]})[[NEWLINE]]`

As a practical example, let's go back to:
hdr_strong
content_copy

`get('story.json').then(function(response) {[[NEWLINE]]  console.log("Success!", response);[[NEWLINE]]})[[NEWLINE]]`

The response is JSON, but we're currently receiving it as plain text. We could alter our get function to use the JSON[`responseType`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest#responseType), but we could also solve it in promises land:

hdr_strong
content_copy

`get('story.json').then(function(response) {[[NEWLINE]]  return JSON.parse(response);[[NEWLINE]]}).then(function(response) {[[NEWLINE]]  console.log("Yey JSON!", response);[[NEWLINE]]})[[NEWLINE]]`

Since `JSON.parse()` takes a single argument and returns a transformed value, we can make a shortcut:

hdr_strong
content_copy

`get('story.json').then(JSON.parse).then(function(response) {[[NEWLINE]]  console.log("Yey JSON!", response);[[NEWLINE]]})[[NEWLINE]]`

[See that in action here](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/story.json), check the console in DevTools to see the result. In fact, we could make a`getJSON()` function really easily:

hdr_strong
content_copy

`function getJSON(url) {[[NEWLINE]]  return get(url).then(JSON.parse);[[NEWLINE]]}[[NEWLINE]]`

`getJSON()` still returns a promise, one that fetches a url then parses the response as JSON.

### Queuing asynchronous actions

You can also chain `then`s to run async actions in sequence.

When you return something from a `then()` callback, it's a bit magic. If you return a value, the next `then()` is called with that value. However, if you return something promise-like, the next `then()` waits on it, and is only called when that promise settles (succeeds/fails). For example:

hdr_strong
content_copy

`getJSON('story.json').then(function(story) {[[NEWLINE]]  return getJSON(story.chapterUrls[0]);[[NEWLINE]]}).then(function(chapter1) {[[NEWLINE]]  console.log("Got chapter 1!", chapter1);[[NEWLINE]]})[[NEWLINE]]`

Here we make an async request to `story.json`, which gives us a set of URLs to request, then we request the first of those. This is when promises really start to stand out from simple callback patterns.

You could even make a shortcut method to get chapters:
hdr_strong
content_copy

`var storyPromise;[[NEWLINE]][[NEWLINE]]function getChapter(i) {[[NEWLINE]]  storyPromise = storyPromise || getJSON('story.json');[[NEWLINE]][[NEWLINE]]  return storyPromise.then(function(story) {[[NEWLINE]]    return getJSON(story.chapterUrls[i]);[[NEWLINE]]  })[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// and using it is simple:[[NEWLINE]]getChapter(0).then(function(chapter) {[[NEWLINE]]  console.log(chapter);[[NEWLINE]]  return getChapter(1);[[NEWLINE]]}).then(function(chapter) {[[NEWLINE]]  console.log(chapter);[[NEWLINE]]})[[NEWLINE]]`

We don't download `story.json` until `getChapter` is called, but the next time(s) `getChapter` is called we reuse the story promise, so `story.json`is only fetched once. Yay Promises!

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Error handling

As we saw earlier, `then()` takes two arguments, one for success, one for failure (or fulfill and reject, in promises-speak):

hdr_strong
content_copy

`get('story.json').then(function(response) {[[NEWLINE]]  console.log("Success!", response);[[NEWLINE]]}, function(error) {[[NEWLINE]]  console.log("Failed!", error);[[NEWLINE]]})[[NEWLINE]]`

You can also use `catch()`:
hdr_strong
content_copy

`get('story.json').then(function(response) {[[NEWLINE]]  console.log("Success!", response);[[NEWLINE]]}).catch(function(error) {[[NEWLINE]]  console.log("Failed!", error);[[NEWLINE]]})[[NEWLINE]]`

There's nothing special about `catch()`, it's just sugar for`then(undefined, func)`, but it's more readable. Note that the two code examples above do not behave the same, the latter is equivalent to:

hdr_strong
content_copy

`get('story.json').then(function(response) {[[NEWLINE]]  console.log("Success!", response);[[NEWLINE]]}).then(undefined, function(error) {[[NEWLINE]]  console.log("Failed!", error);[[NEWLINE]]})[[NEWLINE]]`

The difference is subtle, but extremely useful. Promise rejections skip forward to the next `then()` with a rejection callback (or `catch()`, since it's equivalent). With `then(func1, func2)`, `func1` or `func2` will be called, never both. But with `then(func1).catch(func2)`, both will be called if `func1` rejects, as they're separate steps in the chain. Take the following:

hdr_strong
content_copy

`asyncThing1().then(function() {[[NEWLINE]]  return asyncThing2();[[NEWLINE]]}).then(function() {[[NEWLINE]]  return asyncThing3();[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  return asyncRecovery1();[[NEWLINE]]}).then(function() {[[NEWLINE]]  return asyncThing4();[[NEWLINE]]}, function(err) {[[NEWLINE]]  return asyncRecovery2();[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  console.log("Don't worry about it");[[NEWLINE]]}).then(function() {[[NEWLINE]]  console.log("All done!");[[NEWLINE]]})[[NEWLINE]]`

The flow above is very similar to normal JavaScript try/catch, errors that happen within a "try" go immediately to the `catch()` block. Here's the above as a flowchart (because I love flowcharts):

Follow the blue lines for promises that fulfill, or the red for ones that reject.

### JavaScript exceptions and promises

Rejections happen when a promise is explicitly rejected, but also implicitly if an error is thrown in the constructor callback:

hdr_strong
content_copy

`var jsonPromise = new Promise(function(resolve, reject) {[[NEWLINE]]  // JSON.parse throws an error if you feed it some[[NEWLINE]]  // invalid JSON, so this implicitly rejects:[[NEWLINE]]  resolve(JSON.parse("This ain't JSON"));[[NEWLINE]]});[[NEWLINE]][[NEWLINE]]jsonPromise.then(function(data) {[[NEWLINE]]  // This never happens:[[NEWLINE]]  console.log("It worked!", data);[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  // Instead, this happens:[[NEWLINE]]  console.log("It failed!", err);[[NEWLINE]]})[[NEWLINE]]`

This means it's useful to do all your promise-related work inside the promise constructor callback, so errors are automatically caught and become rejections.

The same goes for errors thrown in `then()` callbacks.
hdr_strong
content_copy

`get('/').then(JSON.parse).then(function() {[[NEWLINE]]  // This never happens, '/' is an HTML page, not JSON[[NEWLINE]]  // so JSON.parse throws[[NEWLINE]]  console.log("It worked!", data);[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  // Instead, this happens:[[NEWLINE]]  console.log("It failed!", err);[[NEWLINE]]})[[NEWLINE]]`

### Error handling in practice

With our story and chapters, we can use catch to display an error to the user:
hdr_strong
content_copy

`getJSON('story.json').then(function(story) {[[NEWLINE]]  return getJSON(story.chapterUrls[0]);[[NEWLINE]]}).then(function(chapter1) {[[NEWLINE]]  addHtmlToPage(chapter1.html);[[NEWLINE]]}).catch(function() {[[NEWLINE]]  addTextToPage("Failed to show chapter");[[NEWLINE]]}).then(function() {[[NEWLINE]]  document.querySelector('.spinner').style.display = 'none';[[NEWLINE]]})[[NEWLINE]]`

If fetching `story.chapterUrls[0]` fails (e.g., http 500 or user is offline), it'll skip all following success callbacks, which includes the one in`getJSON()` which tries to parse the response as JSON, and also skips the callback that adds chapter1.html to the page. Instead it moves onto the catch callback. As a result, "Failed to show chapter" will be added to the page if any of the previous actions failed.

Like JavaScript's try/catch, the error is caught and subsequent code continues, so the spinner is always hidden, which is what we want. The above becomes a non-blocking async version of:

hdr_strong
content_copy

`try {[[NEWLINE]]  var story = getJSONSync('story.json');[[NEWLINE]]  var chapter1 = getJSONSync(story.chapterUrls[0]);[[NEWLINE]]  addHtmlToPage(chapter1.html);[[NEWLINE]]}[[NEWLINE]]catch (e) {[[NEWLINE]]  addTextToPage("Failed to show chapter");[[NEWLINE]]}[[NEWLINE]]document.querySelector('.spinner').style.display = 'none'[[NEWLINE]]`

You may want to `catch()` simply for logging purposes, without recovering from the error. To do this, just rethrow the error. We could do this in our `getJSON()` method:

hdr_strong
content_copy

`function getJSON(url) {[[NEWLINE]]  return get(url).then(JSON.parse).catch(function(err) {[[NEWLINE]]    console.log("getJSON failed for", url, err);[[NEWLINE]]    throw err;[[NEWLINE]]  });[[NEWLINE]]}[[NEWLINE]]`

So we've managed to fetch one chapter, but we want them all. Let's make that happen.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Parallelism and sequencing: getting the best of both

Thinking async isn't easy. If you're struggling to get off the mark, try writing the code as if it were synchronous. In this case:

hdr_strong
content_copy

`try {[[NEWLINE]]  var story = getJSONSync('story.json');[[NEWLINE]]  addHtmlToPage(story.heading);[[NEWLINE]][[NEWLINE]]  story.chapterUrls.forEach(function(chapterUrl) {[[NEWLINE]]    var chapter = getJSONSync(chapterUrl);[[NEWLINE]]    addHtmlToPage(chapter.html);[[NEWLINE]]  });[[NEWLINE]][[NEWLINE]]  addTextToPage("All done");[[NEWLINE]]}[[NEWLINE]]catch (err) {[[NEWLINE]]  addTextToPage("Argh, broken: " + err.message);[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]document.querySelector('.spinner').style.display = 'none'[[NEWLINE]]`

[Try it](https://googlesamples.github.io/web-fundamentals/fundamentals/primers/sync-example.html)

That works (see[code](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/sync-example.html))! But it's sync and locks up the browser while things download. To make this work async we use `then()` to make things happen one after another.

hdr_strong
content_copy

`getJSON('story.json').then(function(story) {[[NEWLINE]]  addHtmlToPage(story.heading);[[NEWLINE]][[NEWLINE]]  // TODO: for each url in story.chapterUrls, fetch &amp; display[[NEWLINE]]}).then(function() {[[NEWLINE]]  // And we're all done![[NEWLINE]]  addTextToPage("All done");[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  // Catch any error that happened along the way[[NEWLINE]]  addTextToPage("Argh, broken: " + err.message);[[NEWLINE]]}).then(function() {[[NEWLINE]]  // Always hide the spinner[[NEWLINE]]  document.querySelector('.spinner').style.display = 'none';[[NEWLINE]]})[[NEWLINE]]`

But how can we loop through the chapter urls and fetch them in order? This**doesn't work**:

hdr_strong
content_copy

`story.chapterUrls.forEach(function(chapterUrl) {[[NEWLINE]]  // Fetch chapter[[NEWLINE]]  getJSON(chapterUrl).then(function(chapter) {[[NEWLINE]]    // and add it to the page[[NEWLINE]]    addHtmlToPage(chapter.html);[[NEWLINE]]  });[[NEWLINE]]})[[NEWLINE]]`

`forEach` isn't async-aware, so our chapters would appear in whatever order they download, which is basically how Pulp Fiction was written. This isn't Pulp Fiction, so let's fix it.

### Creating a sequence

We want to turn our `chapterUrls` array into a sequence of promises. We can do that using `then()`:

hdr_strong
content_copy

`// Start off with a promise that always resolves[[NEWLINE]]var sequence = Promise.resolve();[[NEWLINE]][[NEWLINE]]// Loop through our chapter urls[[NEWLINE]]story.chapterUrls.forEach(function(chapterUrl) {[[NEWLINE]]  // Add these actions to the end of the sequence[[NEWLINE]]  sequence = sequence.then(function() {[[NEWLINE]]    return getJSON(chapterUrl);[[NEWLINE]]  }).then(function(chapter) {[[NEWLINE]]    addHtmlToPage(chapter.html);[[NEWLINE]]  });[[NEWLINE]]})[[NEWLINE]]`

This is the first time we've seen `Promise.resolve()`, which creates a promise that resolves to whatever value you give it. If you pass it an instance of `Promise` it'll simply return it (**note:** this is a change to the spec that some implementations don't yet follow). If you pass it something promise-like (has a `then()` method), it creates a genuine `Promise` that fulfills/rejects in the same way. If you pass in any other value, e.g., `Promise.resolve('Hello')`, it creates a promise that fulfills with that value. If you call it with no value, as above, it fulfills with "undefined".

There's also `Promise.reject(val)`, which creates a promise that rejects with the value you give it (or undefined).

We can tidy up the above code using[`array.reduce`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce):

hdr_strong
content_copy

`// Loop through our chapter urls[[NEWLINE]]story.chapterUrls.reduce(function(sequence, chapterUrl) {[[NEWLINE]]  // Add these actions to the end of the sequence[[NEWLINE]]  return sequence.then(function() {[[NEWLINE]]    return getJSON(chapterUrl);[[NEWLINE]]  }).then(function(chapter) {[[NEWLINE]]    addHtmlToPage(chapter.html);[[NEWLINE]]  });[[NEWLINE]]}, Promise.resolve())[[NEWLINE]]`

This is doing the same as the previous example, but doesn't need the separate "sequence" variable. Our reduce callback is called for each item in the array. "sequence" is `Promise.resolve()` the first time around, but for the rest of the calls "sequence" is whatever we returned from the previous call. `array.reduce`is really useful for boiling an array down to a single value, which in this case is a promise.

Let's put it all together:
hdr_strong
content_copy

`getJSON('story.json').then(function(story) {[[NEWLINE]]  addHtmlToPage(story.heading);[[NEWLINE]][[NEWLINE]]  return story.chapterUrls.reduce(function(sequence, chapterUrl) {[[NEWLINE]]    // Once the last chapter's promise is done…[[NEWLINE]]    return sequence.then(function() {[[NEWLINE]]      // …fetch the next chapter[[NEWLINE]]      return getJSON(chapterUrl);[[NEWLINE]]    }).then(function(chapter) {[[NEWLINE]]      // and add it to the page[[NEWLINE]]      addHtmlToPage(chapter.html);[[NEWLINE]]    });[[NEWLINE]]  }, Promise.resolve());[[NEWLINE]]}).then(function() {[[NEWLINE]]  // And we're all done![[NEWLINE]]  addTextToPage("All done");[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  // Catch any error that happened along the way[[NEWLINE]]  addTextToPage("Argh, broken: " + err.message);[[NEWLINE]]}).then(function() {[[NEWLINE]]  // Always hide the spinner[[NEWLINE]]  document.querySelector('.spinner').style.display = 'none';[[NEWLINE]]})[[NEWLINE]]`

[Try it](https://googlesamples.github.io/web-fundamentals/fundamentals/primers/async-example.html)

And there we have it (see[code](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/async-example.html)), a fully async version of the sync version. But we can do better. At the moment our page is downloading like this:

 ![promise1.gif](../_resources/8cc1ba80f51088489b5ca730c91b0860.gif)

Browsers are pretty good at downloading multiple things at once, so we're losing performance by downloading chapters one after the other. What we want to do is download them all at the same time, then process them when they've all arrived. Thankfully there's an API for this:

hdr_strong
content_copy

`Promise.all(arrayOfPromises).then(function(arrayOfResults) {[[NEWLINE]]  //...[[NEWLINE]]})[[NEWLINE]]`

`Promise.all` takes an array of promises and creates a promise that fulfills when all of them successfully complete. You get an array of results (whatever the promises fulfilled to) in the same order as the promises you passed in.

hdr_strong
content_copy

`getJSON('story.json').then(function(story) {[[NEWLINE]]  addHtmlToPage(story.heading);[[NEWLINE]][[NEWLINE]]  // Take an array of promises and wait on them all[[NEWLINE]]  return Promise.all([[NEWLINE]]    // Map our array of chapter urls to[[NEWLINE]]    // an array of chapter json promises[[NEWLINE]]    story.chapterUrls.map(getJSON)[[NEWLINE]]  );[[NEWLINE]]}).then(function(chapters) {[[NEWLINE]]  // Now we have the chapters jsons in order! Loop through…[[NEWLINE]]  chapters.forEach(function(chapter) {[[NEWLINE]]    // …and add to the page[[NEWLINE]]    addHtmlToPage(chapter.html);[[NEWLINE]]  });[[NEWLINE]]  addTextToPage("All done");[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  // catch any error that happened so far[[NEWLINE]]  addTextToPage("Argh, broken: " + err.message);[[NEWLINE]]}).then(function() {[[NEWLINE]]  document.querySelector('.spinner').style.display = 'none';[[NEWLINE]]})[[NEWLINE]]`

[Try it](https://googlesamples.github.io/web-fundamentals/fundamentals/primers/async-all-example.html)

Depending on connection, this can be seconds faster than loading one-by-one (see[code](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/async-all-example.html)), and it's less code than our first try. The chapters can download in whatever order, but they appear on screen in the right order.

 ![promise2.gif](../_resources/aad580cc8b9b2be0be40cc75997c4013.gif)

However, we can still improve perceived performance. When chapter one arrives we should add it to the page. This lets the user start reading before the rest of the chapters have arrived. When chapter three arrives, we wouldn't add it to the page because the user may not realize chapter two is missing. When chapter two arrives, we can add chapters two and three, etc etc.

To do this, we fetch JSON for all our chapters at the same time, then create a sequence to add them to the document:

hdr_strong
content_copy

`getJSON('story.json').then(function(story) {[[NEWLINE]]  addHtmlToPage(story.heading);[[NEWLINE]][[NEWLINE]]  // Map our array of chapter urls to[[NEWLINE]]  // an array of chapter json promises.[[NEWLINE]]  // This makes sure they all download in parallel.[[NEWLINE]]  return story.chapterUrls.map(getJSON)[[NEWLINE]]    .reduce(function(sequence, chapterPromise) {[[NEWLINE]]      // Use reduce to chain the promises together,[[NEWLINE]]      // adding content to the page for each chapter[[NEWLINE]]      return sequence.then(function() {[[NEWLINE]]        // Wait for everything in the sequence so far,[[NEWLINE]]        // then wait for this chapter to arrive.[[NEWLINE]]        return chapterPromise;[[NEWLINE]]      }).then(function(chapter) {[[NEWLINE]]        addHtmlToPage(chapter.html);[[NEWLINE]]      });[[NEWLINE]]    }, Promise.resolve());[[NEWLINE]]}).then(function() {[[NEWLINE]]  addTextToPage("All done");[[NEWLINE]]}).catch(function(err) {[[NEWLINE]]  // catch any error that happened along the way[[NEWLINE]]  addTextToPage("Argh, broken: " + err.message);[[NEWLINE]]}).then(function() {[[NEWLINE]]  document.querySelector('.spinner').style.display = 'none';[[NEWLINE]]})[[NEWLINE]]`

[Try it](https://googlesamples.github.io/web-fundamentals/fundamentals/primers/async-best-example.html)

And there we go (see[code](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/async-best-example.html)), the best of both! It takes the same amount of time to deliver all the content, but the user gets the first bit of content sooner.

 ![promise3.gif](../_resources/e835328738fc83158282fc20162a8c80.gif)

In this trivial example, all of the chapters arrive around the same time, but the benefit of displaying one at a time will be exaggerated with more, larger chapters.

Doing the above with [Node.js-style callbacks or events](https://gist.github.com/jakearchibald/0e652d95c07442f205ce) is around double the code, but more importantly isn't as easy to follow. However, this isn't the end of the story for promises, when combined with other ES6 features they get even easier.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Bonus round: promises and generators

This next bit involves a whole bunch of new ES6 features, but it's not something you need to understand to use promises in your code today. Treat it like a movie trailer for some upcoming blockbuster features.

ES6 also gives us[generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#Generators), which allow functions to exit at a particular point, like "return", but later resume from the same point and state, for example:

hdr_strong
content_copy

`function *addGenerator() {[[NEWLINE]]  var i = 0;[[NEWLINE]]  while (true) {[[NEWLINE]]    i += yield i;[[NEWLINE]]  }[[NEWLINE]]}[[NEWLINE]]`

Notice the star before the function name, this makes it a generator. The yield keyword is our return/resume point. We can use it like this:

hdr_strong
content_copy

`var adder = addGenerator();[[NEWLINE]]adder.next().value; // 0[[NEWLINE]]adder.next(5).value; // 5[[NEWLINE]]adder.next(5).value; // 10[[NEWLINE]]adder.next(5).value; // 15[[NEWLINE]]adder.next(50).value; // 65[[NEWLINE]]`

But what does this mean for promises? Well, you can use this return/resume behaviour to write async code that looks like (and is as easy to follow as) synchronous code. Don't worry too much about understanding it line-for-line, but here's a helper function that lets us use `yield` to wait for promises to settle:

hdr_strong
content_copy

`function spawn(generatorFunc) {[[NEWLINE]]  function continuer(verb, arg) {[[NEWLINE]]    var result;[[NEWLINE]]    try {[[NEWLINE]]      result = generator[verb](arg);[[NEWLINE]]    } catch (err) {[[NEWLINE]]      return Promise.reject(err);[[NEWLINE]]    }[[NEWLINE]]    if (result.done) {[[NEWLINE]]      return result.value;[[NEWLINE]]    } else {[[NEWLINE]]      return Promise.resolve(result.value).then(onFulfilled, onRejected);[[NEWLINE]]    }[[NEWLINE]]  }[[NEWLINE]]  var generator = generatorFunc();[[NEWLINE]]  var onFulfilled = continuer.bind(continuer, "next");[[NEWLINE]]  var onRejected = continuer.bind(continuer, "throw");[[NEWLINE]]  return onFulfilled();[[NEWLINE]]}[[NEWLINE]]`

… which I pretty much[lifted verbatim fromQ](https://github.com/kriskowal/q/blob/db9220d714b16b96a05e9a037fa44ce581715e41/q.js#L500), but adapted for JavaScript promises. With this, we can take our final best-case chapter example, mix it with a load of new ES6 goodness, and turn it into:

hdr_strong
content_copy

`spawn(function *() {[[NEWLINE]]  try {[[NEWLINE]]    // 'yield' effectively does an async wait,[[NEWLINE]]    // returning the result of the promise[[NEWLINE]]    let story = yield getJSON('story.json');[[NEWLINE]]    addHtmlToPage(story.heading);[[NEWLINE]][[NEWLINE]]    // Map our array of chapter urls to[[NEWLINE]]    // an array of chapter json promises.[[NEWLINE]]    // This makes sure they all download in parallel.[[NEWLINE]]    let chapterPromises = story.chapterUrls.map(getJSON);[[NEWLINE]][[NEWLINE]]    for (let chapterPromise of chapterPromises) {[[NEWLINE]]      // Wait for each chapter to be ready, then add it to the page[[NEWLINE]]      let chapter = yield chapterPromise;[[NEWLINE]]      addHtmlToPage(chapter.html);[[NEWLINE]]    }[[NEWLINE]][[NEWLINE]]    addTextToPage("All done");[[NEWLINE]]  }[[NEWLINE]]  catch (err) {[[NEWLINE]]    // try/catch just works, rejected promises are thrown here[[NEWLINE]]    addTextToPage("Argh, broken: " + err.message);[[NEWLINE]]  }[[NEWLINE]]  document.querySelector('.spinner').style.display = 'none';[[NEWLINE]]})[[NEWLINE]]`

[Try it](https://googlesamples.github.io/web-fundamentals/fundamentals/primers/async-generators-example.html)

This works exactly as before but is so much easier to read. This works in Chrome and Opera today (see[code](https://github.com/googlesamples/web-fundamentals/blob/gh-pages/fundamentals/primers/async-generators-example.html)), and works in Microsoft Edge by going to `about:flags` and turning on the **Enable experimental JavaScript features** setting. This will be enabled by default in an upcoming version.

This throws together a lot of new ES6 stuff: promises, generators, let, for-of. When we yield a promise, the spawn helper waits for the promise to resolve and returns the final value. If the promise rejects, spawn causes our yield statement to throw an exception, which we can catch with normal JavaScript try/catch. Amazingly simple async coding!

This pattern is so useful, it's coming to ES7 in the form of[async functions](https://jakearchibald.com/2014/es7-async-functions/). It's pretty much the same as above, but no need for a `spawn` method.

## [arrow_upward](https://developers.google.com/web/fundamentals/primers/promises#top_of_page)Promise API reference

All methods work in Chrome, Opera, Firefox, Microsoft Edge, and Safari unless otherwise noted. The[polyfill](https://github.com/jakearchibald/ES6-Promises#readme) provides the below for all browsers.

### Static Methods

Method summaries
[object Object]
Returns promise (only if [object Object])
[object Object]

Make a new promise from the thenable. A thenable is promise-like in as far as it has a `then()` method.

[object Object]
Make a promise that fulfills to [object Object]. in this situation.
[object Object]

Make a promise that rejects to [object Object]. For consistency and debugging (e.g. stack traces), [object Object] should be an [object Object].

[object Object]

Make a promise that fulfills when every item in the array fulfills, and rejects if (and when) any item rejects. Each array item is passed to [object Object], so the array can be a mixture of promise-like objects and other objects. The fulfillment value is an array (in order) of fulfillment values. The rejection value is the first rejection value.

[object Object]

Make a Promise that fulfills as soon as any item fulfills, or rejects as soon as any item rejects, whichever happens first.

star**Note:** I'm unconvinced of `Promise.race`'s usefulness; I'd rather have an opposite of `Promise.all` that only rejects if all items reject.

### Constructor

Constructor
[object Object]

 [object Object]
Your promise will be fulfilled/rejected with the outcome of [object Object]

 [object Object]
Your promise is fulfilled with [object Object]

 [object Object]

Your promise is rejected with [object Object]. For consistency and debugging (e.g., stack traces), obj should be an [object Object]. Any errors thrown in the constructor callback will be implicitly passed to [object Object].

### Instance Methods

Instance Methods
[object Object]

 [object Object] is called when/if "promise" resolves. [object Object] is called when/if "promise" rejects. Both are optional, if either/both are omitted the next [object Object]/[object Object] in the chain is called. Both callbacks have a single parameter, the fulfillment value or rejection reason. [object Object] returns a new promise equivalent to the value you return from [object Object]/[object Object] after being passed through [object Object]. If an error is thrown in the callback, the returned promise rejects with that error.

[object Object]
Sugar for [object Object]

Many thanks to Anne van Kesteren, Domenic Denicola, Tom Ashworth, Remy Sharp, Addy Osmani, Arthur Evans, and Yutaka Hirano who proofread this and made corrections/recommendations.

Also, thanks to [Mathias Bynens](https://mathiasbynens.be/) for[updating various parts](https://github.com/html5rocks/www.html5rocks.com/pull/921/files)of the article.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated October 10, 2017.