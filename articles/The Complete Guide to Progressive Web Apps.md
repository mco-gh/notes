The Complete Guide to Progressive Web Apps

# The Complete Guide to Progressive Web Apps

## A Progressive Web App is an app that can provide additional features based on the device support, including offline capabilities, push notifications and almost native app look and speed, and local caching of resources

 Published Jan 25, 2018

> Learning JavaScript? Download my free **> [> JavaScript Handbook](https://flaviocopes.com/page/javascript-handbook/)**>

* * *

[   Sponsored by Microsoft Azure            ![1569598119-Microsoft-logo_rgb_c-wht-250x100.png](../_resources/b8ba4676da3bbad1feb077b53fabea86.png)      Build Machine Learning and AI Solutions    Easily train your machine learning models in Azure.    Learn More](https://srv.buysellads.com/ads/click/x/GTND42QUCTAI453WCE7LYKQMCAYIT277CVSDPZ3JCWSI4K3UCVBIC2JKC6BI5K37CYYDEK3EHJNCLSIZ?segment=placement:flaviocopescom;)

- [Introduction](https://flaviocopes.com/progressive-web-apps/#introduction)
- [What is a Progressive Web App](https://flaviocopes.com/progressive-web-apps/#what-is-a-progressive-web-app)
- [Progressive Web Apps alternatives](https://flaviocopes.com/progressive-web-apps/#progressive-web-apps-alternatives)
    - [Native Mobile Apps](https://flaviocopes.com/progressive-web-apps/#native-mobile-apps)
    - [Hybrid Apps](https://flaviocopes.com/progressive-web-apps/#hybrid-apps)
    - [Apps built with React Native](https://flaviocopes.com/progressive-web-apps/#apps-built-with-react-native)
- [Progressive Web Apps features](https://flaviocopes.com/progressive-web-apps/#progressive-web-apps-features)
    - [Features](https://flaviocopes.com/progressive-web-apps/#features)
    - [Benefits](https://flaviocopes.com/progressive-web-apps/#benefits)
    - [Core concepts](https://flaviocopes.com/progressive-web-apps/#core-concepts)
- [Service Workers](https://flaviocopes.com/progressive-web-apps/#service-workers)
- [The App Manifest](https://flaviocopes.com/progressive-web-apps/#the-app-manifest)
    - [Example](https://flaviocopes.com/progressive-web-apps/#example)
- [The App Shell](https://flaviocopes.com/progressive-web-apps/#the-app-shell)
    - [Caching](https://flaviocopes.com/progressive-web-apps/#caching)

## Introduction

Progressive Web Apps (PWA) are the latest trend of **mobile application development** using web technologies, at the time of writing (march 2018) work on Android and iOS devices with iOS 11.3 or higher, and macOS 10.13.4 or higher.

PWA is a term that identifies a bundle of techniques that have the goal of creating a better experience for web-based apps.

## What is a Progressive Web App

A Progressive Web App is an app that *can*  **provide additional features based on the device support**, providing offline capability, push notifications and almost native app look and speed, and local caching of resources.

This technique was originally introduced by Google in 2015, and proves to bring many advantages to both the developer and the users.

Developers have access to building **almost-first-class** applications using a web stack, which is always considerably easier and cheaper than building native applications, especially when considering the implications of building and maintaining cross-platform apps.

Devs can benefit from a **reduced installation friction**, at a time when having an app in the store does not actually bring anything in terms of discoverability for 99.99% of the apps, and Google search can provide the same benefits if not more.

A Progressive Web App is a website which is developed with certain technologies that make the mobile experience much more pleasant than a normal mobile-optimized website, to a point that it’s almost working like a native app, as it offers the following features:

- Offline support
- Loads fast
- Is secure
- Is capable of emitting push notifications
- Has an immersive, full-screen user experience without the URL bar

Mobile platforms (Android at the time of writing, but it’s not technically limited to that) offer an increasing support for Progressive Web Apps to the point of asking the user to **add the app to the home screen** when they detect a site a user is visiting is a PWA.

But first, a little clarification on the name. *Progressive Web App* can be a **confusing term**, and a good definition is *web apps that take advantage of modern browsers features (like [web workers](https://flaviocopes.com/web-workers/) and the web app manifest) to let their mobile devices “upgrade” the app to the role of a first-class citizen app*.

## Progressive Web Apps alternatives

How does a PWA stand compared to the alternatives when it comes to building a mobile experience?

Let’s focus on the pros and cons of each, and let’s see where PWAs are a good fit.

### Native Mobile Apps

Native mobile apps are the most obvious way to build a mobile app. Objective-C or Swift on iOS, Java / Kotlin on Android and C# on Windows Phone.

Each platform has its own UI and UX conventions, and the native widgets provide the experience that the user expects. They can be deployed and distributed through the platform App Store.

The main pain point with native apps is that cross-platform development requires learning, mastering and keeping up to date with many different methodologies and best practices, so if for example you have a small team or even you’re a solo developer building an app on 3 platforms, you need to spend a lot of time learning the technology but also the environment, manage different libraries, and use different workflows (for example, iCloud only works on iOS devices, there’s no Android version).

### Hybrid Apps

Hybrid applications are built using Web Technologies, but deployed to the App Store. In the middle sits a framework or some way to package the application so it’s possible to send it for review to the traditional App Store.

Most common platforms are Phonegap, Xamarin, Ionic Framework, and many others, and usually what you see on the page is a WebView that essentially loads a local website.

The key aspect of Hybrid Apps is the **write once, run anywhere** concept, the different platform code is generated at build time, and you’re building apps using [JavaScript](https://flaviocopes.com/javascript/), HTML and CSS, which is amazing, and the device capabilities (microphone, camera, network, gps…) are exposed through JavaScript APIs.

The bad part of building hybrid apps is that unless you do a great job, you might settle on providing a common denominator, effectively creating an app that’s sub-optimal on all platforms because the app is ignoring the platform-specific human-computer interaction guidelines.

Also, performance for complex views might suffer.

### Apps built with React Native

React Native exposes the native controls of the mobile device through a JavaScript API, but you’re effectively creating a native application, not embedding a website inside a WebView.

Their motto, to distinguish this approach from hybrid apps, is **learn once, write anywhere**, meaning that the approach is the same across platforms, but you’re going to create completely separate apps in order to provide a great experience on each platform.

Performance is comparable to native apps, since what you build is essentially a native app, which is distributed through the App Store.

## Progressive Web Apps features

In the last section you saw the main *competitors* of Progressive Web Apps. So how do PWAs stand compared to them, and what are their main features?

> Remember, currently Progressive Web Apps are Android-only IOS support was added in March 2019

### Features

Progressive Web Apps have one thing that separates them completely from the above approaches: **they are not deployed to the app store.**.

This is a key advantage, since the app store is beneficial if you have the reach and luck to be featured, which can make your app go viral, but unless you’re in the 0,001% you’re not going to get much benefits from having your little place on the App Store.

Progressive Web Apps are **discoverable using Search Engines**, and when a user gets to your site which has PWAs capabilities, **the browser in combination with the device asks the user if they want to install the app to the home screen**. This is huge because regular SEO can apply to your PWA, leading to much less reliance on paid acquisition.

Not being in the App Store means **you don’t need the Apple or Google approval** to be in the users pockets, and you can release updates when you want, without having to go through the standard approval process which is typical of iOS apps.

PWAs are basically HTML5 applications / responsive websites on steroids, with some key technologies that were recently introduced that make some of the key features possible. If you remember the original iPhone came without the option to develop native apps, and developers were told to develop HTML5 mobile apps, that could be installed to the home screen, but the tech back then was not ready for this.

Progressive Web Apps **run offline**.

The use of **service workers** allow the app to always have fresh content, and download it in the background, and provide support for **push notifications** to provide greater re-engagement opportunities.

Also, shareability makes for a much nicer experience for users that want to share your app, as they just need a URL.

### Benefits

So why should users and developers care about Progressive Web Apps?

1. PWA are lighter. Native Apps can weight 200MB or more, while a PWA could be in the range of the KBs.

2. No native platform code

3. Lower the cost of acquisition (it’s much more hard to convince a user to install an app than to visit a website to get the first-time experience)

4. Significant less effort is needed to build and release updates
5. Much more support for deep links than regular app-store apps

### Core concepts

- **Responsive**: the UI adapts to the device screen size
- **App-like feel**: it doesn’t feel like a website, but rather as an app as much as possible
- **Offline support**: it will use the device storage to provide offline experience
- **Installable**: the device browser prompts the user to install your app
- **Re-engaging**: push notifications help users re-discover your app once installed
- **Discoverable**: search engines and SEO optimization can provide a lot more users than the app store
- **Fresh**: the app updates itself and the content once online
- **Safe**: uses HTTPS
- **Progressive**: it will work on any device, even older one, even if with less features (e.g. just as a website, not installable)
- **Linkable**: easy to point to it, using URLs

## Service Workers

Part of the Progressive Web App definition is that it must work offline.

Since the thing that allows the web app to work offline is the Service Worker, this implies that **Service Workers are a mandatory part of a Progressive Web App**.

See http://caniuse.com/#feat=serviceworkers for updated data on browsers support.

> TIP: Don’t confuse Service Workers with Web Workers. They are a completely different thing.

A Service Worker is a JavaScript file that acts as a middleman between the web app and the network. Because of this it can provide cache services and speed the app rendering and improve the user experience.

Because of security reasons, only HTTPS sites can make use of Service Workers, and this is part of the reasons why a Progressive Web App must be served through HTTPS.

Service Workers are not available on the device the first time the user visits the app. What happens is that the first visit the web worker is installed, and then on subsequent visits to separate pages of the site will call this Service Worker.

> Check out the > [> complete guide to Service Workers](https://flaviocopes.com/service-workers)

## The App Manifest

The App Manifest is a JSON file that you can use to provide the device information about your Progressive Web App.

You add a link to the manifest in **all** your web site pages header:

	<link rel="manifest" href="/manifest.webmanifest">

This file will tell the device how to set:

- The name and short name of the app
- The icons locations, in various sizes
- The starting URL, relative to the domain
- The default orientation
- The splash screen

### Example

	{
	  "name": "The Weather App",
	  "short_name": "Weather",
	  "description": "Progressive Web App Example",
	  "icons": [{
	    "src": "images/icons/icon-128x128.png",
	      "sizes": "128x128",
	      "type": "image/png"
	    }, {
	      "src": "images/icons/icon-144x144.png",
	      "sizes": "144x144",
	      "type": "image/png"
	    }, {
	      "src": "images/icons/icon-152x152.png",
	      "sizes": "152x152",
	      "type": "image/png"
	    }, {
	      "src": "images/icons/icon-192x192.png",
	      "sizes": "192x192",
	      "type": "image/png"
	    }, {
	      "src": "images/icons/icon-256x256.png",
	      "sizes": "256x256",
	      "type": "image/png"
	    }],
	  "start_url": "/index.html?utm_source=app_manifest",
	  "orientation": "portrait",
	  "display": "standalone",
	  "background_color": "#3E4EB8",
	  "theme_color": "#2F3BA2"
	}

The App Manifest is a W3C Working Draft, reachable at https://www.w3.org/TR/appmanifest/

## The App Shell

The App Shell is not a technology but rather a **design concept** aimed at loading and rendering the web app container first, and the actual content shortly after, to give the user a nice app-like impression.

This is the equivalent of the Apple HIG (Human Interface Guidelines) suggestions to use a splash screen that resembles the user interface, to give a psychological hint that was found to lower the perception of the app taking a long time to load.

### Caching

The App Shell is cached separately from the contents, and it’s setup so that retrieving the shell building blocks from the cache takes very little time.

Find out more on the App Shell at https://developers.google.com/web/updates/2015/11/app-shell

* * *

[Found a typo or problem? Edit this page](https://github.com/flaviocopes/website-content/blob/content/post/web-platform-api/progressive-web-apps/index.md)