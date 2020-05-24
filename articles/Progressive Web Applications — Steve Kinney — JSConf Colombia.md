Progressive Web Applications — Steve Kinney — JSConf Colombia

# Building Your First Progressive Web Application: A Journey

## Abstract

> A few years ago, pundits were trumpeting the demise of the mobile web. Apps had won the day. In retrospect, that announcement hasn’t aged well. The mobile web is alive and well. Progressive Web Applications (PWA) provide native qualities with the ease of access and distribution of the web. But PWAs are not built on a single technology and it can be a bit tricky to wrap your head around a PWA is exactly. It turns out, there are a bunch of technologies that go into building a PWA. In this talk, we’ll explore the ecosystem, how the technologies that support PWAs differ from some similar attempts in the past, and some of the challenges for the mobile web that PWAs have yet to tackle.

## Administrivia, disclaimers, and legal stuff

### Who even am I?

Hi! My name is Steve and I’m a principal engineer at [SendGrid](https://sendgrid.com/).

- I’m the organizer of [DinosaurJS](http://dinosaurjs.org/)—a JSConf in Denver.
- I’m the author of [Electron in Action](http://bit.ly/electronjs).
- I do some workshops with [Frontend Masters](https://frontendmasters.com/) in my copious free time.

We can be friends at any of the following places:

- [Twitter](https://twitter.com/stevekinney)
- [Github](https://github.com/stevekinney)

SendGrid is a company that has an *awesome* API that handles sending over 35 billion emails a month. Setting up an SMTP server is no fun and—trust me—email is hard. There are some super great people at my company that work hard on making for a great developer experience. You can check out:

- [SendGrid’s Github](https://github.com/sendgrid)
- [The documentation](https://sendgrid.com/docs)

Pull requests accepted! Also: please come talk to me about this stuff.

I work on our Marketing Campaigns product. Basically, my job to take all of the power of the API and build a sophisticated client-side application for people who aren’t technically and/or don’t want to write their own code to interact with the API.

### Usage license

I worked on this content with the wonderful [Mike North](https://twitter.com/michaellnorth). It has [a license](https://github.com/mike-north/pwa-fundamentals#license) that you should totally check out if you want to use this material. The short version is that you can use everything included to learn or copy/paste into your own personal projects. You just can’t go and teach course or write a book based on this stuff. I’m going to take a *very* long nap after this and then go back to my day job as an engineer. But, if you’re interested in having a hands-on workshop, [you should totally hire Mike to come in and do the deep dive](https://mike.works/). Unlike me, he is a consumate professional and does this stuff for a living.

### Important disclaimer

We have 90 minutes together today, so we’re not going to be able to cover everything, but we’ll get you started down the road to building a Progressive Web Application.

Are you excited? I am. I’ve written this guide to not only serve as my lesson plan for the morning, but also as a reference for you to come back to later on. I’d encourage that you save this link or bookmark it or tattoo onto your left arm. Whatever works best for you. Very cool. Let’s get into it.

## What even is a Progressive Web Application™?

That’s a good question. Thanks for asking. Honestly. We spend all of our time together musing on the nuances, but time is limited. I’ll cute to the chase. Progressive Web Applications have the following features:

- They’re **applications** usually. Although, you can definitely use some of these techniques for content pages.
    - They work offline.
- They’re on the **web**. This one is a bit of a no-brainer. But, I’m going with a theme here.
    - They’re linkable.
    - They’re responsive.
    - You don’t need to install them.
    - You don’t need to update them.
- They’re **progressive**. By this, I mean they leverage progressive enhancement. You’re application might have amazing super powers in the latest version of Chrome or Firefox. But, it should still work in *less enlightened* browsers as well.

## But, first—let’s talk about asynchronous JavaScript!

You might be a 1990s kid if you remember:

	const xhr = new XMLHttpRequest();
	xhr.open('GET', url);
	xhr.responseType = 'json';

	xhr.onload = () => { console.log(xhr.response); };

	xhr.onerror = () => { console.error(""); };

	xhr.send();

Js
[Copy]()
Ugh. jQuery gave us a slightly better way to do this.

	$.ajax('http://example.com').then((data) => {
	  console.log('Definitely better', data);
	});

Js
[Copy]()
But this still has some problems, right?

- It’s a browser only thing.
- You don’t have a ton of control over the request and the response.
- `XMLHttpRequest` wasn’t really made for how we typically use it.
- It’s limited to text and usually just JSON and XML. (Gross.)

### Introducing the Fetch API

It looks kind of like what we saw before with the jQuery AJAX request, but it has some subtle differences.

	fetch('http://example.com/')
	  .then((response) => response.json())
	  .then((jsonData) => {
	    // ...
	  });

Js
[Copy]()
Some fun facts about `fetch()`:

- It can be polyfilled today.
- You get first-class treatment of request/response objects (I’ll totally explain this if I have time!)
- It’s more Node.js-friendly.
- It’s one of those rare cases where it is both lower-level *and* less terrible than the thing it’s replacing.
    - In fact, `XMLHttpRequest` now uses `fetch` under the hood. That’s something you typically only see in weird time travel movies.

Oh, did I mention it works super nicely with that fancy new `async`/`await` syntax that all of the cool kids are talking about these days? Behold:

	const getData = async (url) => {
	  try {
	    const response =  await fetch(url);
	    const data = await response.json();
	    // Do stuff…
	  } catch (error) {
	    // Handle error…
	  }
	}

Js
[Copy]()

#### Yea, but why are you telling me about this?

Well, we’re going to use it and it is a little bit different in some important ways that we should probably understand before moving forward.

- The promises returned by a `fetch` request will not reject if the response has a 400- or 500-level status code.
- It only rejects on network failure. (This is actually a good thing for us today.)
- By default, `fetch` does not send or receive any cookies.
- `fetch` can do some wild stuff like fetch things that aren’t just JSON or XML.

#### Anatomy of a `fetch` request

Okay, let’s squint and take a look at another example.

	const imageElement = document.querySelector('img');

	fetch('beatles.jpg').then(response => {
	  return response.blob();
	}).then(response => {
	  const objectURL = URL.createObjectURL(response);
	  imageElement.src = objectURL;
	});

Js
[Copy]()

Hmm… so, we have an image. That’s cool. Then we do this intermediate step. Where we parse it. (*Also*: This looks like a very cool example of how to use fetch to get an image and replace it’s `src` attribute. I wonder if we’ll need this in a future exercise? I don’t know I’m just thinking aloud. Hence the parentheses.)

### Request and Response Objects

We’re not done with `fetch` just yet. We need to pull back the layers of the onion a bit more.

That string I passed in? The URL? Remember that from like 1 minute ago?
So, that’s a nice short-hand. What `fetch` really wants is a `Response` object.

	const headers = new Headers();

	const options = { method: 'GET',
	                  headers: headers,
	                  mode: 'cors',
	                  cache: 'default' };

	const request = new Request('beatles.jpg', options);

	fetch(request).then(response => {
	  return response.blob();
	}).then(response => {
	  const objectURL = URL.createObjectURL(response);
	  imageElement.src = objectURL;
	});

Js
[Copy]()

That’s longer and does the exact same thing. I get that. But, I promise you that we’re going to be working a bit more with `Response` objects.

And then look! That response we get back isn’t just the JSON or an image in this case. It’s some kind of `Response` object with methods like `response.json()` and `response.blob()`. Interesting!

**HEY!** Please, please make a mental bookmark here. I’m going to tie this all together in bit.

#### Working with Responses

	fetch(request)
	  .then(response => response.json())
	  .then(doStuffWithResponse);

Js
[Copy]()

`fetch` can work with all sorts of data types. So, we need to parse the response. You could write your own parser. Or, you could use one of the built-in ones.

- `response.blob();`
- `response.json();`
- `response.text();`
- `response.formData();`
- `response.arrayBuffer();`

## Introducing service worker

A lot of technologies make up Progressive Web Applications. That is very true. But, if I had to pick a favorite child, it would totally be service worker.

So, what is a service worker? Very good question.

- Service workers run on their own thread just like a Web Worker or Shared Worker.
- They can intercept network requests.
- This means you can catch the request if the client is offline and either provide a fallback or use a resource from cache.
- A service worker can run the background, even when the web application is not open.

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Without Service Worker](../_resources/9106832c479f7b8018250a276b63d363.jpg)

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/With Service Worker](../_resources/f564c6fa6b749a3b10da420e39bd78a7.jpg)

### Register a service worker

	if ('ServiceWorker' in navigator) {
	  // Okay, the browser supports service workers.
	  navigator.ServiceWorker.register('service-worker.js')
	    .then(registration => {
	      // The service worker is registered.
	    })
	    .catch(err => {
	      // No dice.
	    });
	} else {
	  // ServiceWorker is not a thing, apparently.
	}

Js
[Copy]()

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Screenshot 2017-11-01 20.00.36.png](../_resources/a40b93f50b04ee356e9cb35cda550491.png)

**Try Together**: Let’s go explore the Application pane in the Chrome developer tools together. Head over to [this exercise](https://wire-up-this-service-worker.glitch.me/). Your job is to:

- Open up `public/client.js` and register the service worker.
- Open up the “Application” pane in Chrome’s developer tools.
    - Make sure “Update on Reload” is *not* clicked.
    - Reload the page a few times.
    - Check the box next to “Update on Reload”.
    - Reload the page a few more times for good measure.

### The service worker Lifecycle

Why have a lifecycle?

- Make offline-first something that’s possible
- Allow the new service worker to get installed and ready without disturbing the current one
- Ensure that there is one and only one active service worker
- Imagine if two open tabs were running two different service workers.

Here is a diagram:

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/ServiceWorker Life Cycle](../_resources/92705c88803078a2a345f7e12b9a8550.jpg)

	self.addEventListener('install', event => {
	  // Do the stuff needed at install time.
	  // This may not be the active service worker yet.
	});

	self.addEventListener('activate', event => {
	  // We are ready to take the stage.
	});

	self.addEventListener('fetch', event => {
	  // Intercept a network request.
	});

Js
[Copy]()

Whoa—did I just slip and extra on in there? Weird, it’s like I’m going to tie it all together in a bit. Creepy.

#### Conditions for Replacing a service worker

Imagine this, you update your wonderful service worker.

- You proudly reload your page. Nothing changes.
- Your new service worker will not take over until all other instances of the application have been closed.
- It’s like when a desktop application auto-updates. You don’t get the new one until you totally quit out of the application and start it back up.

This is literally one of the most confusing parts about working with service workers. So, let me go back to using pictures—but this time [moving pictures](https://cdn.glitch.com/0c080a9e-d71d-4194-aeae-a2ba00ea21f9%2FReplacing%20a%20ServiceWorker.m4v?1509588829587)!

(There should be a video here. Bummer.)

This is what it looks like in the Chrome Developer Tools when we have a service worker waiting around.

- If you don’t want this in your application for some reason, you can call `event.skipWaiting()`.
- If you only want this in development, then the Chrome Developer Tools are your friend.

What does this look like?

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/A ServiceWorker in Waiting](../_resources/88204f2838e3bcf7ed2403bcf46874e4.png)

**Let’s Explore Together**: Let’s take a tour of [this *very* simple example](https://super-simple-service-worker.glitch.me/).

**Try this**: Take a look at [this example](https://glitch.com/edit/#!/super-simple-service-worker?path=public/service-worker.js:7:3). Go ahead and add a listen for the “fetch” events. Just `console.log` the event for now. We’ll peak in and take a look at each event.

(You can peak below if you get stuck, but try it on your own.)

## Intercepting Network Requests with a service worker

	self.addEventListener('fetch', event => {
	  console.log(event.request.url);
	});

Js
[Copy]()

As we saw in the last exercise, listening for the “fetch” events will not only give us XHR requests, but all network requests. Whoa.

That includes images, CSS, HTML, and other JavaScript.

### Working with `FetchEvent`

- `event.request` → the request object
- `event.request.url` → the original URL request
- `event.request.method` → the HTTP method used
- `event.respondWith` → allows you to respond with something other than what was being requested

That last one has super powers. Trust me on this.

	self.addEventListener('fetch', event => {
	  if (event.request.url === location.origin + '/') {
	    event.respondWith(
	      new Response('<p>Hello!</p>', {
	        headers: {'Content-Type': 'text/html'}
	      })
	    )
	  }
	});

Js
[Copy]()
**Quick Demonstration**: https://intercepting-fetch.glitch.me/

**Your Turn**: Look at the example above. Can you intercept the CSS stylesheet with some custom styles? (5-10 minutes.)

Here are some hints:

- You should look at the code sample right above this.
- The `Content-Type` header for CSS is `text/css`.
- If you’re at a loss for what to be in your stylesheet, I recommend `body { background-color: red; }`.
- Maybe play with that “Bypass for Network” button for a bit.

### Introducing the Cache API

Hmm… caching? What exactly is the Cache API?

It’s very cool that we can intercept requests, but that doesn’t get us any closer to the Progressive Web App™ stamp of approval. The Cache API gives us fine-grain, programatic control over caching assets from inside of a service worker.

Tell me more. What does it look like?

	const cacheName = 'assets-v1';

	caches.open(cacheName).then(cache => {
	  // Do stuff with the cache.
	});

Js
[Copy]()

*TL;DR*: You can tell your cache about a bunch of things you’d like it to hold on to.

Okay, let’s see a real world example.

	const cacheName = 'assets-v1';

	self.addEventListener('install', event => {
	  event.waitUntil(
	    caches.open(cacheName).then(cache => {
	      return cache.addAll(
	        [
	          '/index.html',
	          '/style.css',
	          '/client.js',
	        ]
	      );
	    })
	  );
	});

Js
[Copy]()

- The budding Service Worker can be killed at any time by the browser.
- `event.waitUntil()` keeps the “install” process going until the promise it was handed resolves.
    - This allows us to be assured that by the time the activate event is fired, the preceding install process has completed successfully.
    - If the promise it was given rejects, the Service Worker installation will fail, it will be abandoned, and the currently-active worker—if any—will remain in charge.

**Hey!** Remember when I told you to make that mental bookmark? Okay, now’s the time to pull that back up.

The Cache API stores pairs of request and response objects.

#### The Cache API and its relationship to the Fetch API

- Under the hood, the Cache API is a Map where `Request` objects are the keys and `Response` objects are the values.
- Put another way: this means that you can store responses and just serve them back if you receive a another matching request.

	caches.open('band-assets').then(cache => {
	  const request = new Request('/beatles.png');
	  const response = new Response('/oasis.png');
	  cache.put(request, response);
	});

Js
[Copy]()

This usually unnecessary. We’re probably better off with this kind of shorthand.

	caches.open('band-assets').then(cache => {
	  const request = new Request('/beatles.png');
	  cache.add(request);
	});

Js
[Copy]()
How do I get something out of the cache?

	const request = new Request('/beatles.png');

	caches.match(event.request);

Js
[Copy]()
When should you do any of this?

	self.addEventListener('install', event => {
	  console.log(`
	    This is a great time to set up any caches
	    that your new service worker will need.
	  `);
	});

	self.addEventListener('activate', event => {
	  console.log(`
	    This is a great time to remove any caches
	    that your retired service worker was using.
	  `);
	});

Js
[Copy]()

#### The Cache API: Not just for service workers anymore

- You can access the Cache API from the browser context as well.
- This can be useful if you want to allow users to manually add items to the cache. (Think: “Save for Offline”)

#### Out with the old and in with the new

	const currentCache = 'assets-v2';

	self.addEventListener('install', event => {
	  event.waitUntil(
	    caches.open(currentCache).then(cache => {
	      return cache.addAll(
	        [
	          '/index.html',
	          '/style.css',
	          '/client.js',
	        ]
	      );
	    })
	  );
	});

	self.addEventListener('activate', event => {
	  event.waitUntil(
	    caches.keys().then(cacheNames => Promise.all(
	      cacheNames.filter(cacheName => {
	        return cacheName !== currentCache
	      }).map(cacheName => caches.delete(cacheName))
	    ))
	  );
	});

Js
[Copy]()

#### Your Turn

Take a look at this: [https://decidedly-not-offline.glitch.me](https://decidedly-not-offline.glitch.me/)

Here we have a website. While the conference Wi-Fi is pretty good here, but it could down at any time. It would be great if we could make the site work offline.

Here are some hints:

- You know how to use `event.respondWith`.
- `event.request` is a `Request` object.
- `caches.match` can pull things from the cache.

**Extension**: You got it already? Very cool. But, I helped you set it up. So, that’s not totally fair. Can you get *this page* to work offline?

## Caching Strategies

We [have some problems](https://cache-money.glitch.me/). This will intercept and any all requests. Even when we have a perfectly good Internet connection.

That’s—let’s just say—*sub-optimal*.

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/could-should.jpg](../_resources/ed19a92b6c9b73037ebc733cc857ed3e.jpg)

We know *how* to cache assets, but we really don’t have a strategy, right?

### Cache only

This is what we did earlier and it’s even worse than it sounds.

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Cache Only](../_resources/1d7b72163f4cc075ab5e3cc4e65ab5d7.jpg)

	self.addEventListener('fetch', event => {
	  event.respondWith(caches.match(event.request));
	});

Js
[Copy]()

- I hope you like being offline, because this service worker will try to pull everything from cache and never get to the network.
- It’s supposed to be “offline-first” not “offline-only.”

### Network only

Wait, what?

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Network Only](../_resources/5bad9a83044bf309b3c17dc31f41da86.jpg)

	self.addEventListener('fetch', event => {
	  event.respondWith(fetch(event.request));
	});

Js
[Copy]()
I’m going somewhere with this. I promise.

I’ve been overusing bulleted lists. So, I think I’ll go with a ordered list this time.

1. We know that `fetch()` can either take a string or a `Request` object.
2. `event.request` happens to be a `Request` object.
3. `event.waitUntil` expects a promise that resolves with a `Response` object.

4. `fetch()` happens to return a promise that resolves with a `Response` object.

It’s like they were made to work together or something.

### Cache with a network backup

Now we’re getting somewhere.

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Progressive Web Apps, Develop Denver.089.jpeg](../_resources/a66872494a66f3fec041c34c4c9b6d7c.jpg)

	self.addEventListener('fetch', event => {
	  event.respondWith(
	    caches.match(event.request).then(response => {
	      return response || fetch(event.request);
	    })
	  );
	});

Js
[Copy]()
**Try this**: Can you update the offline example we created before?

### Network with a cache backup

Try to get something from the network and if that doesn’t work, then go check the cache.

	self.addEventListener('fetch', event => {
	  event.respondWith(
	    fetch(event.request).catch(() {
	      return caches.match(event.request);
	    })
	  );
	});

Js
[Copy]()

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Network then Cache](../_resources/2a38ac3a9bd26a986f7517c918df8724.jpg)

**Try this**: Can you refactor the previous exercise?

### Cache *then* network

So far we’ve just been iterating through all of the combinations. What makes all of this stuff super powerful is that we have the full power of the JavaScript programming language at our finger-tips.

This means that we have stuff like conditionals. Wild!

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Cache then Network](../_resources/4776c9547fe21bd7b4be66d21b2a945b.jpg)

	let didWeReceiveFreshNetworkData = false;
	const doSomethingWithData = () => { … };

	const fetchFromNetwork = fetch('/very-important-data.json')
	  .then(response => {
	    return response.json();
	  }).then(data => {
	    didWeReceiveFreshNetworkData = true;
	    doSomethingWithData(data);
	  });

	caches.match('/very-important-data.json')
	  .then(response => {
	    return response.json();
	  }).then(data => {
	    if (!didWeReceiveFreshNetworkData) {
	      doSomethingWithData(data);
	    }
	  }).catch(() => {
	    return fetchFromNetwork;
	  });

Js
[Copy]()

### Generic fallback

This is good for stuff like user avatars. Try the network and cache. If neither of those pan out. Then use a generic default

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Progressive Web Apps, Develop Denver.099.jpeg](../_resources/4c5823db07f52e7c759ec68fbe8591c3.jpg)

	self.addEventListener('fetch', event => {
	  event.respondWith(
	    caches.match(event.request).then(response => {
	      return response || fetch(event.request);
	    }).catch(() => {
	      return caches.match('/placeholder.png');
	    })
	  );
	});

Js
[Copy]()
You *could* do the following:
1. Fetch the resource.
2. If that fails, check the cache.

3. If you don’t have the avatar for that user. Fall back to a placeholder image that you *definitely* have cached.

### Working with Different Types of Assets

We don’t necessarily want to handle all of the different file types the same way. Earlier in this workshop, we did a dark thing where we checked for the URL of the stylesheet. It worked, but it was kind of gross.

Typically, it’s better to look at the request header to get a sense of what kind of resource we’re asking for and then take the appropriate action.

Again, this is some of the cool things that happen when you have the full power of a programming language underneath your finger tips.

	self.addEventListener('fetch', event => {
	  const acceptHeader = event.request.headers.get('accept');
	  console.log('Fetching', acceptHeader, event.request.url);

	  event.respondWith(
	    caches.match(event.request).then(response => {
	      return response || fetch(event.request);
	    })
	  );
	});

Js
[Copy]()

If you check out [this example](https://cache-money.glitch.me/), you can see I am logging each `accept` header of the request to the console.

This is super useful to determining what kind of resource we’re requesting.

	if (acceptHeader.indexOf("image/*")) {
	  'I am an image.';
	}
	if (acceptHeader.indexOf('text/css')) {
	  'I am a CSS file.';
	}
	if (acceptHeader.indexOf('text/html')) {
	  'I am an HTML file.';
	}
	if (acceptHeader.indexOf('*/*')) {
	  'YOLO!';
	}

Js
[Copy]()

Again, you have the full power of the JavaScript programming language. You can get as granular as you want or need to.

## Notifications

Let’s start with [an example](https://notify-the-authorities.glitch.me/) and work backwards.

**Try this**: Take this for a spin in your console.

	console.log(Notification.permission);

	Notification.requestPermission().then(permission => {
	  console.log(permission);
	});

Js
[Copy]()
What happened?

![0c080a9e-d71d-4194-aeae-a2ba00ea21f9/Screenshot 2017-11-02 16.44.48.png](../_resources/8b6e93323764352b504227c15d7ca6bc.png)

Erm, so—what about progressive enhancement? Good point. Let’s do some feature detection to make sure we’re not calling methods on objects that don’t exist.

	if ('Notification' in window) {
	  // Now do your notification stuff…
	}

Js
[Copy]()
Neat. So, let’s say you get permission—how do you actually send a message?

	if ('Notification' in window) {
	  if (Notification.permission === 'default') {
	    Notification.requestPermission().then(permission => {
	      const notification = new Notification(
	        'Thanks for granting permission!',
	        {
	          body: 'We promise not to abuse it.',
	        }
	      );
	    });
	  }
	}

Js
[Copy]()

If you look closely, we have this `new Notification()` constructor. Creating one will just trigger the notification automatically. This is only partially true. It’s a bit different when you’re working with it in a service worker.

For example, this won’t work:

	self.addEventListener('activate', event => {
	  const notification = new Notification();
	  // You will never hear from me.
	});

Js
[Copy]()

	self.addEventListener('activate', event => {
	  self.registration.showNotification('Hello World');
	});

Js
[Copy]()

The above takes for granted that the user has already given your service worker permission.

Notifications take two arguments:

- A string for the title
- An object full of options

As you can see, I’m really into bulleted lists lately. Here is another bulleted list of all of the options you can pass in. Fair warning: a lot of them won’t do anything on the desktop.

- `body` (string, effectively the subtitle of the notification)
- `icon` (URL, a small image to go along with your notification)
- `image` (URL, a larger image)
- `badge` (URL, only used on Chrome for Android)
- `vibrate`
- `sound`
- `dir` (for left-to-right or right-to-left text, “auto” is also a valid option)
- `tag` (a short string, used for grouping notifications)
- `data` (anything)
- `requireInteraction` (boolean)
- `renotify` (boolean, forces the notification to stay visible)
- `silent` (boolean)

**Try together**: Let’s take a look at that [example again](https://notify-the-authorities.glitch.me/), but this time with the console open. I want to dig into the event and the notification itself and review some topics.

## Doing stuff in the background

So, we’ve talked a lot about what happens when you have no connection to the network, but we haven’t dealt with a much more incidious issue: what happens when you have a *bad* connection.

The “cache then network” strategy handles this from perspective of you requesting files from the server, but what about when you want to send some data?

Oh. You’re just now noticing that I totally skirted around that issue. How sneaky of me. Well, nevermind. I’ll address it now.

But first, let’s think about what makes something an “application.” (Imagine I’m using air quotes here.)

We expect it to be installable on our devices and to at least open when we’re online. But, some of the better applications still allow us to take actions that when we’re offline and sync stuff up later.

Consider the native Twitter application:

- If the Twitter application is offline and you like a tweet, the application will optimistically assume that everything is going to work out.
- It might keep a reference to each tweet that you liked in IndexedDB and replay your actions when it connects. (It doesn’t because it’s a native application, but you get the idea.)
- It can do this silently, without alerting you.

Allow me to belabor this point some more: For something like a news application, it might be good enough to sync up with the latest news every once in a while—but what about a to do list? Your significant other asks you to put up some vegan ham on the way home. The application should capture that, even if your connection isn’t very good.

In traditional web application, you’d fire a `POST` request, but if it didn’t make it to the server, you’d be out of luck.

What if we could tell the application to try to do something and if it can’t connect in a timely fashion to keep trying in the background until it finally works?

We can!
In order to get this working, we need to register a sync event.

	if ('service worker' in navigator) {
	  navigator.service worker.ready.then(registration => {
	    registration.sync.register('your-event-name');
	  });
	}

Js
[Copy]()

We would use this instead of sending a `POST` request. So, you’ll probably want a fallback here for both browsers that don’t support service workers as well as if that promise rejects, but bear with me here.

Just like caching, there is no one-size-fits-all solution for syncing.

- In some situations, we might only want to schedule a sync if the network fails.
    - In other words, start with a `fetch` and if that promise rejects, then try to register a sync event.
- In other situations, this might be our first choice.

We’ve registered a sync event. This is very cool. But we also need to do something upon registration. Maybe something along the lines of:

	self.addEventListener('sync', event => {
	  if (event.tag === 'your-event-name') {
	    event.waitUntil(handleYourEvent());
	  }
	});

Js
[Copy]()

Before we get too excited, there are some considerations that we need to—umm—consider.

- You can’t pass in any state when you register your background sync.
    - IndexedDB is a great choice as a place to store this data.
    - When your Service Worker attempts a sync, read the data out of IndexedDB.
- If you register multiple sync events with the same tag, the most recent will override the previous.
    - This could be a good thing. (See above.)

Let’s take a look at it in action!

**Try together**: We’re going to take a tour of [an application](https://dream-catcher.glitch.me/) that allows users to enter and save data even when they’re offline. Well almost. We’ll have to add some funcitonality.

*Pro-tip*: I have to actually shut my Wi-Fi off to get the real offline experience. For some reason, it doesn’t work if I just hit the “Offline” button in the checkbox in the Chrome developer tools. I should probably report this as a bug or something.

What are we going to do?

- Add a fallback to optimistically store the dream in IndexDB if the network request fails.
- Register a sync event to send the request to the network when we reconnect.
- When we reconnect, `POST` all of the synced events to the server.
- If we can’t connect when loaded the page, get everything from IndexedDB.

If we have time, you’ll implement the ability to remove a dream if the user is offline. Otherwise, this will be homework.

## Fin.

I hope that was useful for you! Please reach out on [Twitter](https://twitter.com/stevekinney), if there is anything else you’d like me to add or cover!

 [Remix this in Glitch](https://glitch.com/)