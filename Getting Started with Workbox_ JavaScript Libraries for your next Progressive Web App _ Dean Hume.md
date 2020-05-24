Getting Started with Workbox: JavaScript Libraries for your next Progressive Web App | Dean Hume

#  Getting Started with Workbox: JavaScript Libraries for your next Progressive Web App

When it comes to building Progressive Web Apps, my favourite library has to be the [Service Worker toolbox](https://github.com/GoogleChrome/sw-toolbox). I’ve previously written about this [great library](https://deanhume.com/Home/BlogPost/getting-started-with-the-service-worker-toolbox/10134) and how it can make life a lot easier for developers by removing boilerplate code and using proven caching strategies that help you build real world PWAs. The truth is, it *used* to be my favourite library until I discovered [Workbox](https://workboxjs.org/).

![Workbox JavaScript Library - Service Worker Progressive Web App](../_resources/90f4f7a73d0f08bfd0d7850f06fa7504.png)

Workbox that takes learnings from the Service Worker Toolbox and builds upon it, while at the same time providing a collection of loosely-coupled libraries and tools that focus on different service worker features and use-cases. The great thing about this library is that it helps you simplify your development by making it easy to take advantage of powerful service worker features and automating service worker generation.

At it’s core, Workbox is made up of a module called **workbox-sw**, which is a service worker library that makes makes fetch requests and caching as easy as possible. However, under the hood, there are a number of lower-level modules that can be used independently or mixed-and-matched depending on your use case. For example, there is a module called **workbox-cache-expiration** which expires cached responses based on age or a maximum number of entries. Another awesome module is **workbox-background-sync**, which queues failed requests and uses the Background Sync API to replay those requests when the user comes back online. Awesome stuff!

In this article, I am going to run through some of the basics of the Workbox library, including the Workbox CLI tool, custom caching, improved debugging as well as the offline Google Analytics module.

## Getting started

I wanted to experiment with Workbox using an existing Progressive Web App in order to compare the new library side by side. For this example, I am going to use a PWA that I have already built which is called [Awesome Typography](https://deanhume.github.io/typography/); essentially it’s a list of resources that help you build beautiful websites using Web Fonts.

![Workbox JavaScript - Awesome Web Typography](../_resources/2817f49ac9efcaca1764a4df8cfe8579.jpg)

The web pages in the Awesome Typography site are static which makes the content perfect for service worker caching. I also use Google Analytics which should plug in nicely with the **workbox-offline-analytics** package.

## The Workbox CLI tool makes life a lot easier

One of the things that I really like about Workbox is that it comes with a CLI tool that you can use to generate a service worker with some smart defaults. No need to manually create each file in your service worker, the CLI tool will loop through your files and add them to your service worker to be precached.

First off, start by installing the Workbox CLI. Open your terminal (or Command Prompt in Windows) and run the following code:

*$ npm install workbox-cli --global*

In order to generate a service worker and precache the files in your project, run the following code:

*$ workbox-cli generate:sw*

You’ll be prompted with a list of questions to determine your project’s setup and voilà, the tool will create a ready-to-use service worker that you can add to your project.

It took me less than five minutes to get this running on the Awesome Typography website. The best thing about the Workbox CLI tool is that you can apply this to any project in just a few steps.

## Custom caching and routing

Okay, so we’ve got precaching in place, but what about any HTTP requests that aren’t coming from the Awesome Typography site? This site is all about the web fonts, so it only makes sense that we include a few in each page! The fonts used on this site are from Google Fonts, which means if the user is offline or loses their connection, the site will look a bit funny without the fonts in place.

The CLI tool is great for files that exist on my hard drive, but ideally I want to cache these web fonts too. This is where routing comes into play.

In its most basic form, routing is the process of matching an incoming request with the most appropriate route. Once we have matched a request, we can then decide what we want to do with it. I’ve used the following code inside my service worker and included the Workbox library.

|     |     |
| --- | --- |
| 1   | importScripts('workbox-sw.prod.v1.1.0.js'); |
| 2   |     |
| 3   | const  workboxSW  =  new  self.WorkboxSW(); |
| 4   | workboxSW.precache(fileManifest); |
| 5   |     |
| 6   | // The route for any requests from the googleapis origin |
| 7   | workboxSW.router.registerRoute('https://fonts.googleapis.com/(.*)', |
| 8   |  workboxSW.strategies.cacheFirst({ |
| 9   | cacheName:  'googleapis', |
| 10  | cacheableResponse: { |
| 11  | statuses: [0, 200] |
| 12  | },  |
| 13  | networkTimeoutSeconds:  4 |
| 14  | })  |
| 15  | );  |

 [view raw](https://gist.github.com/deanhume/e5b8e0af6fad706bc04a04c0377efdf1/raw/0c10f7ec0ec78998144da2823d7c79b490eab0fc/workbox-sw.js)  [workbox-sw.js](https://gist.github.com/deanhume/e5b8e0af6fad706bc04a04c0377efdf1#file-workbox-sw-js) hosted with ❤ by [GitHub](https://github.com/)

Woah - that looks like a lot of code. Let’s break it down step by step.

Firstly, we are including the Workbox JavaScript file using *importScripts()*. Now that it is included in our service worker, we can start referencing the WorkboxSW() library.

Next, we register a new route for 'https://fonts.googleapis.com/(.*)', which will ensure that any HTTP requests that match the origin "fonts.googleapis.com" will be added to added to and retrieved from service worker cache. The code above won't cache anything that doesn't match our route and this kind of flexibility is great because it really gives you the control over what you would like cache.

You may also notice the *strategies.cacheFirst* function. Workbox takes a lot of the hard work out of writing your own caching logic. It comes with built-in caching strategies that you can mix and match depending on your own custom routes.

For example, you can choose from:

- Cache only
- Cache first, falling back to network
- Cache, with network update
- Network only
- Network first, falling back to cache

If you’d like to learn more about the different caching strategies support in Workbox, I recommend checking out [this link](https://workboxjs.org/reference-docs/latest/module-workbox-runtime-caching.html) for more information.

You can also choose to only cache certain HTTP response statuses. Here I am explicitly choosing 200 responses, but you could choose 404’s or other HTTP statuses depending on your needs.

Finally, and probably my favourite feature, is the ability to force the network to timeout after a certain amount of time using *networkTimeoutSeconds*. Using this is important because it ensures that if the network takes too long to respond, it will simply fallback and your user won’t be stuck waiting for a resource to load. This is also a great step forward in reducing [Single Point of Failure](https://deanhume.com/home/blogpost/frontend-single-point-of-failure/85) in your web apps.

## Improved Debugging

When it comes to debugging your service worker logic, it can be tricky at the best of times. If you include the development version of the Workbox library in your service worker, you’ll get detailed information logged to the console of your Developer Tools.

![Workbox JavaScript - Debugging Developer Tools](../_resources/ad464a388b1de05a8a560bcc31c7a6da.png)

This debugging information can be pretty handy when you are left scratching your head why a resource keeps on getting cached! To disable the debugging, simply switch back to the production version of Workbox.

## Offline Google Analytics

The first time I started experimenting with service workers and realised how easy it was to build offline web pages, I was blown away! If you have any of your own web apps that work offline, you might be interested in tracking how your users actually use your web app when they are without a network connection. Remember that without a network connection, analytics tools such as Google Analytics aren’t able to send offline usage.

However, Workbox includes a cool module called **workbox-offline-analytics** that ensures that any Google Analytics requests made while offline are saved using IndexedDB and retried the next time the service worker starts up.

To get started, add the following code to your service worker and include it before any other 'fetch' event handlers are defined.

|     |     |
| --- | --- |
| 1   | importScripts('path/to/offline-google-analytics-import.js'); |
| 2   |     |
| 3   | workbox.googleAnalytics.initialize(); |

 [view raw](https://gist.github.com/deanhume/7e6754420994ab2893500b9eb9ad1183/raw/51360cf8d25a99ea791124a889f4a8084ff6251a/workbox-ga.js)  [workbox-ga.js](https://gist.github.com/deanhume/7e6754420994ab2893500b9eb9ad1183#file-workbox-ga-js) hosted with ❤ by [GitHub](https://github.com/)

That’s it! Your web app will now start pushing any Google Analytics requests made offline as soon as it regains a network connection.

## Summary

All in all, the Workbox library is awesome. If I could find any fault, it’s only the slightly larger file size compared to the original sw-toolbox library, but hey, there is a ton of great functionality in Workbox and it’s a small price to pay! It’s also worth mentioning that the extra file size is less of a concern than the main JavaScript dependencies as it won’t block interactivity and the [critical rendering path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/).

If you’d like to experiment and see the code in this article in action, please head over to [deanhume.github.io/typography/index.html](https://deanhume.github.io/typography/index.html) to see this as a working example.

Whether you are looking to build a full blown PWA or simply use some of the service worker features of Workbox, you can mix and match and get started in no time. In this example, we’ve only looked at a few areas of the Workbox library, but if you’d like to learn more, I thoroughly recommend checking out the [Workbox](https://workboxjs.org/) website, it is jam packed with useful examples to get you up and running. Building powerful web applications using service workers doesn’t have to be tough - Workbox takes all the hard work out of it for you!

A big thank you to Robin Osborne, Addy Osmani and the Google team for their help in reviewing this article!

#####  Date:  Thursday, July 27, 2017

Tagged as: [Progressive Web Apps](https://deanhume.com/Home/Tagged/Progressive%20Web%20Apps)

* * *

##### Share

[Share on Twitter](https://twitter.com/intent/tweet?url=http://deanhume.com/home/blogpost/getting-started-with-workbox--javascript-libraries-for-your-next-progressive-web-app/10162&text=Getting%20Started%20with%20Workbox:%20JavaScript%20Libraries%20for%20your%20next%20Progressive%20Web%20App&via=deanohume) | [Share on Google+](https://plus.google.com/share?&hl=en&url=http://deanhume.com/home/blogpost/getting-started-with-workbox--javascript-libraries-for-your-next-progressive-web-app/10162)

* * *

## Comments

** Brian - 7/28/2017 **

Great article. Really got me interested in trying Workbox out. So much functionality to get excited and I'm curious how well the offline analytics works. Often thats more important to my clients than the app itself!

** Jecky Kumar - 7/28/2017 **

Can you give ajax example which returns the json data? In other words, if ajax calls are precached using cachefirst stategy then how will it work for offline?

** Šime Vidas - 7/28/2017 **

Google Fonts are served from fonts.gstatic.com, which means that in your current setup, you're caching the stylesheet with the @font-face rules, but not the actual fonts themselves. In Chrome DevTools Network panel, notice how the WOFF2 files are not coming from the service worker cache.

Could you update your code? I wasn't aware that you can cache cross-origin assets.

* * *

Add your comment
Name: (required)
Email: (will not be published) (required)
Comment:300 Characters left

Please fill this in to confirm that you are human

Recaptcha requires verification

I'm not a robot

reCAPTCHA

[Privacy](https://www.google.com/intl/en/policies/privacy/) - [Terms](https://www.google.com/intl/en/policies/terms/)