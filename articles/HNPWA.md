HNPWA

 [![HN PWA](../_resources/1f64ae9165166f2591c2f24e05ac9462.png)](https://hnpwa.com/)

# Hacker News readers as Progressive Web Apps

 [(L)](https://github.com/tastejs/hacker-news-pwas)

##  A spiritual successor to TodoMVC

TodoMVC has helped thousands of developers select an MV* framework for their JavaScript applications. However, the web ecosystem has evolved in the past few years allowing us to build powerful applications using modern browser capabilities.

To provide developers with examples, we collected a list of unofficial Hacker News clients built with a number of popular JavaScript frameworks and libraries. Each implementation is a complete [Progressive Web App](https://developers.google.com/web/progressive-web-apps/) that utilizes different progressive technologies to provide a fast, reliable and engaging experience.

Our implementations aim to follow a loose specification. They are primarily a learning tool and should not be used to compare the performance of one PWA to another. They can differ based on server infrastructure, performance patterns used and other factors.

## React HN

###   [kristoferbaxter/react-hn](https://github.com/kristoferbaxter/react-hn)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170926_C4_2e99e0bda1db48cfd3b8139722cbc108&run=1)

Interactive (Emerging Markets):

 [2.57s](https://www.webpagetest.org/result/170926_C4_2e99e0bda1db48cfd3b8139722cbc108/)

Interactive (Faster 3G):

 [2.09s](https://www.webpagetest.org/result/170926_MZ_61d634db2106167b89704d43d49d1ee2/)

Framework/UI libraries:

React, React Router

Module bundling:

Webpack

Service Worker:

Application Shell with OfflinePlugin

Performance patterns:

HTTP/2 with Server Push, Brotli and Zopfli static assets

Server-side rendering:

Yes

API:

In-memory cached Hacker News Firebase API

Hosting:

Webfaction + Cloudflare

Author:

 [![Kristofer](../_resources/59ac48080243d7ec88c3c517be579753.jpg)](https://github.com/kristoferbaxter)

 [VIEW APP](https://react-hn.kristoferbaxter.com/)  [SOURCE CODE](https://github.com/kristoferbaxter/react-hn)

## React HN

###   [insin/react-hn](https://github.com/insin/react-hn)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170511_QV_f71a12eb44f1f058b0741db2eac3d85a&run=3)

Interactive (Emerging Markets):

 [6.2s](https://www.webpagetest.org/result/170511_Y7_3a354dfc36f824229a1ae2b1ac93fdbf/)

Interactive (Faster 3G):

 [4.0s](https://www.webpagetest.org/result/170511_QV_f71a12eb44f1f058b0741db2eac3d85a/)

Framework/UI libraries:

React, React Router

Module bundling:

Webpack

Service Worker:

Application Shell + data caching with Workbox

Performance patterns:

PRPL, route-based chunking

Server-side rendering:

Yes

API:

Hacker News Firebase API + Node-hnapi (unoffical)

Hosting:

Google App Engine

Other details:

Asynchronously loaded routes

Authors:

 [![Jonny](../_resources/66fdea5d4ac020a345ade81a80c9765a.jpg)](https://github.com/insin)  [![Addy](../_resources/6584c2ef931fd29bdb01b6edc9dcc3e9.png)](https://github.com/addyosmani)

 [VIEW APP](https://react-hn.appspot.com/)  [SOURCE CODE](https://github.com/insin/react-hn)

## Preact HN

###   [kristoferbaxter/preact-hn](https://github.com/kristoferbaxter/preact-hn)

Lighthouse:

 [93/100](https://www.webpagetest.org/lighthouse.php?test=171009_R6_14208c102da44d9b2c10d78825ea128a&run=1)

Interactive (Emerging Markets):

 [1.9s](https://www.webpagetest.org/result/171009_R6_14208c102da44d9b2c10d78825ea128a/)

Interactive (Faster 3G):

 [1.5s](https://www.webpagetest.org/result/171009_KZ_4637d4705732307a8d01e2fc0869bde3/)

Framework/UI libraries:

Preact

Module bundling:

Webpack

Service Worker:

Application Shell with SW Precache

Performance patterns:

HTTP/2 with Server Push, Brotli and Zopfli static assets

Server-side rendering:

Yes

API:

In-memory cached Hacker News Firebase API

Hosting:

Webfaction + Cloudflare

Author:

 [![Kristofer](../_resources/59ac48080243d7ec88c3c517be579753.jpg)](https://github.com/kristoferbaxter)

 [VIEW APP](https://hn.kristoferbaxter.com/)  [SOURCE CODE](https://github.com/kristoferbaxter/preact-hn)

## Svelte Hacker News

###   [sveltejs/svelte-hackernews](https://github.com/sveltejs/svelte-hackernews)

Lighthouse:

 [73/100](https://www.webpagetest.org/lighthouse.php?test=170611_K5_aaca06336e5608c4a825246b383dc663&run=2)

Interactive (Emerging Markets):

 [2.5s](https://www.webpagetest.org/result/170611_K5_aaca06336e5608c4a825246b383dc663/)

Interactive (Faster 3G):

 [2.2s](https://www.webpagetest.org/result/170611_BP_6fc0112b1b7a2862e4aedef7c9277416/)

Framework/UI libraries:

Svelte

Module bundling:

Rollup

Service Worker:

Application Shell + data caching

Server-side rendering:

Yes

API:

Hacker News Firebase API

Hosting:

Now

Author:

 [![Rich](../_resources/cd44b7a6e0ba6ca46ef4f2e43598da9e.jpg)](https://github.com/Rich-Harris)

 [VIEW APP](https://hn.svelte.technology/)  [SOURCE CODE](https://github.com/sveltejs/svelte-hackernews)

## Vue Hacker News 2.0

###   [vuejs/vue-hackernews-2.0](https://github.com/vuejs/vue-hackernews-2.0)

Lighthouse:

 [93/100](https://www.webpagetest.org/lighthouse.php?test=170919_Q2_655690ac651cba872483ecc93ac6efe9&run=1)

Interactive (Emerging Markets):

 [6.7s](https://www.webpagetest.org/result/170919_ME_f239125bd17ccfed31eb2f81ef860567/)

Interactive (Faster 3G):

 [5.85s](https://www.webpagetest.org/result/170919_Q2_655690ac651cba872483ecc93ac6efe9/)

Framework/UI libraries:

Vue, vue-router, Vuex

Module bundling:

Webpack

Service Worker:

Application Shell + data caching with SWPrecachePlugin

Performance patterns:

Server-side data pre-fetching, preload/prefetch resources

Server-side rendering:

Yes

API:

Hacker News Firebase API

Hosting:

Now

Other details:

Inlined CSS used by rendered components

Author:
 [![Evan](../_resources/d2984f22a19a44dc01e5dbd87c00ac30.jpg)](https://github.com/yyx990803)

 [VIEW APP](https://vue-hn.now.sh/)  [SOURCE CODE](https://github.com/vuejs/vue-hackernews-2.0)

## Angular HN

###   [housseindjirdeh/angular2-hn](https://github.com/housseindjirdeh/angular2-hn)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170612_BV_5cd2c04584152647e2e556f5af8f5eba&run=3)

Interactive (Emerging Markets):

 [6.0s](https://www.webpagetest.org/result/170612_N2_7f979f17312d8feaa1709697d388c1ab/)

Interactive (Faster 3G):

 [4.4s](https://www.webpagetest.org/result/170612_BV_5cd2c04584152647e2e556f5af8f5eba/)

Framework/UI libraries:

Angular

Scaffolding:

Angular CLI

Module bundling:

Webpack

Service Worker:

Application Shell + data caching with sw-precache

Performance patterns:

Lazy loaded modules

Server-side rendering:

None

API:

Node-hnapi (unofficial)

Hosting:

Firebase

Author:

 [![Houssein](../_resources/42c1e7213518c1ba543ac9c2836ccd9a.jpg)](https://github.com/housseindjirdeh)

 [VIEW APP](https://angular2-hn.firebaseapp.com/)  [SOURCE CODE](https://github.com/housseindjirdeh/angular2-hn)

## Viper-news

###   [WebReflection/viper-news](https://github.com/WebReflection/viper-news)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170613_FW_cef11c2c115a07b997263a2866203934&run=2)

Interactive (Emerging Markets):

 [1.9s](https://www.webpagetest.org/result/170613_FW_cef11c2c115a07b997263a2866203934/)

Interactive (Faster 3G):

 [1.5s](https://www.webpagetest.org/result/170613_68_d3066ab1bec95a18e3f9c13a0789ef14/)

Framework/UI libraries:

viperHTML

Module bundling:

Browserify

Service Worker:

Application Shell + data caching

Performance patterns:

Asynchronous Partial Outputs

Server-side rendering:

Yes

API:

Hacker News Firebase API

Hosting:

Google App Engine

Author:

 [![Andrea](../_resources/5f025a4c7e2703082ece34a911c1af27.png)](https://github.com/WebReflection)

 [VIEW APP](https://viperhtml-164315.appspot.com/)  [SOURCE CODE](https://github.com/WebReflection/viper-news)

## Polymer HN

###   [Polymer/hn-polymer-2](https://github.com/polymer/hn-polymer-2)

Lighthouse:

 [92/100](https://www.webpagetest.org/lighthouse.php?test=170919_XJ_de74b35584767efef8fa98087562e749&run=1)

Interactive (Emerging Markets):

 [2.34s](https://www.webpagetest.org/result/170919_0Q_d6fdc6e80104db2e359f6c1e74da1ac7/)

Interactive (Faster 3G):

 [1.8s](https://www.webpagetest.org/result/170919_XJ_de74b35584767efef8fa98087562e749/)

Framework/UI libraries:

Polymer

Scaffolding:

Polymer CLI & Polymer Starter Kit

Module bundling:

Polymer-build with HTML Imports

Service Worker:

Application Shell + data caching with sw-precache

Performance patterns:

PRPL, code-splitting for granular loading

Server-side rendering:

None

API:

Node-hnapi (unofficial)

Hosting:

Firebase functions over HTTP/2 with Server Push + edge-caching

Other details:

Route-specific pushing

Authors:

 [![Dan](../_resources/f63b0305e358d8bc1081d673e897ab5f.jpg)](https://github.com/azakus)  [![Kevin](../_resources/1dda81086a125fbfee86c46b9fefdbbc.png)](https://github.com/kevinpschaaf)  [![Steve](../_resources/0feb35e708f45989d8720b99ca00b567.png)](https://github.com/sorvell)

 [VIEW APP](https://hn-polymer-2.firebaseapp.com/)  [SOURCE CODE](https://github.com/polymer/hn-polymer-2)

## HackerNews.io

###   [ivanvanderbyl/ember-hackernews-pwa](https://github.com/ivanvanderbyl/ember-hackernews-pwa)

Lighthouse:

 [100/100](https://googlechrome.github.io/lighthouse/viewer/?gist=c358a609038f463cb06741b2847f5315)

Interactive (Emerging Markets):

 [4.727s](https://www.webpagetest.org/result/171007_GJ_52584ab4b5e5cf2978d2a20cb28a74e8/)

Interactive (Faster 3G):

 [4.254s](https://www.webpagetest.org/result/171007_3Q_d90b70ffa917bf4ff7300d71575c4262/)

Framework/UI libraries:

Ember.js, Ember Server Worker, Ember Web App, Ember Fetch

Module bundling:

Broccoli + Critical + HTMLMin + Imagemin + gzip

Service Worker:

Application Shell + data caching

Performance patterns:

Prefetch/Preload JS + DNS, Critical CSS, HTTP/2 Server Push

Server-side rendering:

None

API:

Node-hnapi (unofficial) + CloudFront

Hosting:

Cloudfront

Author:

 [![Ivan](../_resources/21acaaa6ce2cbed7f3f7d21020324c69.jpg)](https://github.com/ivanvanderbyl)

 [VIEW APP](https://hackernews.io/)  [SOURCE CODE](https://github.com/ivanvanderbyl/ember-hackernews-pwa)

## Mithril HN

###   [chimon2000/mithril-hn](https://github.com/chimon2000/mithril-hn)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170615_KW_cc7ce98d7be5f17a1381b42aebc6b69d&run=2)

Interactive (Emerging Markets):

 [4.9s](https://www.webpagetest.org/result/170615_51_48fa6a90be213da908a150776c040326/)

Interactive (Faster 3G):

 [4.2s](https://www.webpagetest.org/result/170615_9W_b966e04a3cdec211f0c723bf8a453779/)

Framework/UI libraries:

Mithril, typestyle

Module bundling:

fuse-box

Service Worker:

Application Shell

Performance patterns:

HTTP/2 with Server Push

Server-side rendering:

None

API:

Node-hnapi (unofficial)

Hosting:

Firebase functions over HTTP/2 with Server Push + edge-caching

Author:
 [![Ryan](../_resources/219e074416c923f6e79b95bbd7480413.png)](https://github.com/chimon2000)

 [VIEW APP](https://mithril-hn.firebaseapp.com/)  [SOURCE CODE](https://github.com/chimon2000/mithril-hn)

## HNPWA with Vue.js

###   [codebusking/vue-hn-pwa-guide-kit](https://github.com/codebusking/vue-hn-pwa-guide-kit)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170606_8F_9a74ddc961724a98e92b71ea0ad1443e&run=2)

Interactive (Emerging Markets):

 [5.1s](https://www.webpagetest.org/result/170606_AY_901bc2310bcc8fc640315092d0f0de6b/)

Interactive (Faster 3G):

 [3.9s](https://www.webpagetest.org/result/170606_8F_9a74ddc961724a98e92b71ea0ad1443e/)

Framework/UI libraries:

Vue, vue-router, vue-pwa-boilerplate, firebase-hackernews

Module bundling:

Webpack

Service Worker:

Application Shell + data caching with SWPrecachePlugin

Performance patterns:

Server-side data pre-fetching, preload/prefetch and lazy loading for rest of routes

Server-side rendering:

Yes

API:

Hacker News Firebase API via firebase-hackernews

Hosting:

Now

Author:

 [![Jimmy](../_resources/7816f9211b19483f4429d4984d75c03d.jpg)](https://github.com/ragingwind)

 [VIEW APP](https://vue-hn-pwa.now.sh/)  [SOURCE CODE](https://github.com/codebusking/vue-hn-pwa-guide-kit)

## HNPWA with Next.js

###   [codebusking/next-hnpwa-guide-kit](https://github.com/codebusking/next-hnpwa-guide-kit)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170615_8A_f6ee37ba2caadbb9139e35cf97129673)

Interactive (Emerging Markets):

 [3.3s](https://www.webpagetest.org/result/170615_8A_f6ee37ba2caadbb9139e35cf97129673/)

Interactive (Faster 3G):

 [3.0s](https://www.webpagetest.org/result/170615_TK_5f9791787bb3bf5916205d05a150cb94/)

Framework/UI libraries:

Next.js, Preact, firebase-hackernews

Module bundling:

Webpack

Service Worker:

Application Shell + data caching with Workbox

Performance patterns:

Server-side data pre-fetching, preload/prefetch

Server-side rendering:

Yes

API:

Hacker News Firebase API via firebase-hackernews running on service worker

Hosting:

Now

Author:

 [![Jimmy](../_resources/7816f9211b19483f4429d4984d75c03d.jpg)](https://github.com/ragingwind)

 [VIEW APP](https://next-hnpwa.now.sh/)  [SOURCE CODE](https://github.com/codebusking/next-hnpwa-guide-kit)

## HNPWA with Nuxt.js

###   [nuxt/hackernews](https://github.com/nuxt/hackernews)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170620_PG_a2a9feaf4ace07a61b2c6c2a171b1c79&run=1)

Interactive (Emerging Markets):

 [3.8s](https://www.webpagetest.org/result/170620_B1_0b83d61272c77c16c3f3f1f16fb72d2e/)

Interactive (Faster 3G):

 [3.5s](https://www.webpagetest.org/result/170620_PG_a2a9feaf4ace07a61b2c6c2a171b1c79/)

Framework/UI libraries:

Vue, Nuxt, PWA Module

Module bundling:

Webpack

Service Worker:

Workbox

Performance patterns:

PRPL, Prefetch/Preload JS + DNS + Data, Critical Path CSS, Server Side Caching

Server-side rendering:

Yes

API:

Hacker News Firebase API

Hosting:

Now + CloudFlare CDN

Authors:

 [![Pooya](../_resources/6f925250c6a601cbb64d911dd3b61924.jpg)](https://github.com/pi0)  [![Sebastien](../_resources/1fbc3bd6a6eb4d1c224d06bab8af1450.jpg)](https://github.com/atinux)  [![Alexandre](../_resources/06a3389032ba25addf4438c42c78bf8a.jpg)](https://github.com/alexchopin)

 [VIEW APP](https://hn.nuxtjs.org/)  [SOURCE CODE](https://github.com/nuxt/hackernews)

## HNPWA Vue

###   [anubhav7495/hnpwa-vue](https://github.com/anubhav7495/hnpwa-vue)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170717_C8_230384878d6c07f66bb59cf11f15ad24&run=3)

Interactive (Emerging Markets):

 [4.3s](https://www.webpagetest.org/result/170717_TC_8b6a7c9d33d6687172ff9104a78cbae3/)

Interactive (Faster 3G):

 [3.4s](https://www.webpagetest.org/result/170717_C8_230384878d6c07f66bb59cf11f15ad24/)

Framework/UI libraries:

Vue, vue-router, vue-pwa-boilerplate

Module bundling:

Webpack

Service Worker:

Application Shell with SWPrecachePlugin

Performance patterns:

preload/prefetch resources, client-side data preload, lazy loaded routes, dns-prefetch

Server-side rendering:

None

API:

Node-hnapi (unofficial)

Hosting:

Github Pages

Author:

 [![Anubhav](../_resources/11b9c8feeac06481c64abdf465ad2148.jpg)](https://github.com/anubhav7495)

 [VIEW APP](https://anubhav7495.github.io/hnpwa-vue/)  [SOURCE CODE](https://github.com/anubhav7495/hnpwa-vue)

## HNPWA Firebase

###   [davideast/hnpwa-firebase](https://github.com/davideast/hnpwa-firebase)

Lighthouse:

 [98/100](https://www.webpagetest.org/lighthouse.php?test=170712_FR_5ea158fd9c684d6d8dee49f833093289&run=2)

Interactive (Emerging Markets):

 [1.3s](https://www.webpagetest.org/result/170712_FR_5ea158fd9c684d6d8dee49f833093289/)

Interactive (Faster 3G):

 [0.7s](https://www.webpagetest.org/result/170712_88_101P/)

Framework/UI libraries:

HTML/CSS

Scaffolding:

Firebase CLI

Module bundling:

N/A

Service Worker:

Workboxjs

Performance patterns:

CDN Cache

Server-side rendering:

Yes

API:

hnpwa.com/api/v0

Hosting:

Firebase

Author:
 [![David](../_resources/9ab096deda411de5b502dec19bbc48ad.png)](https://github.com/davideast)

 [VIEW APP](https://hnpwa-firebase.firebaseapp.com/)  [SOURCE CODE](https://github.com/davideast/hnpwa-firebase)

## Angular Hacker News

###   [sebastianm/angular-hacker-news](https://github.com/SebastianM/angular-hacker-news)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170711_54_532be7068a1836a1647889ad4ac5c1f2&run=3)

Interactive (Emerging Markets):

 [4.3s](https://www.webpagetest.org/result/170711_91_727a71056a80d4dd71e3a2cbd904a6b9/)

Interactive (Faster 3G):

 [3.2s](https://www.webpagetest.org/result/170711_54_532be7068a1836a1647889ad4ac5c1f2/)

Framework/UI libraries:

Angular, Angular Router, Angular HTTP

Module bundling:

Webpack

Service Worker:

Application Shell + sw-precache

Performance patterns:

Lazy loaded modules

Server-side rendering:

Angular Universal

API:

Firebase Hacker News API + Node-hnapi (unofficial)

Hosting:

Digitalocean

Author:

 [![Sebastian](../_resources/639aaebf8d3673b5e124db3c97aecfcf.jpg)](https://github.com/SebastianM)

 [VIEW APP](https://angularhn.sebastian-mueller.net/)  [SOURCE CODE](https://github.com/SebastianM/angular-hacker-news)

## Next.js HN

###   [chrisdwheatley/nextjs-hn](https://github.com/chrisdwheatley/nextjs-hn)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170715_KJ_1f08f67beb3451497c196a02e67dd71d&run=3)

Interactive (Emerging Markets):

 [5.75s](https://www.webpagetest.org/result/170715_6V_90471cfb419635b88ed2da5d77fa5f75/)

Interactive (Faster 3G):

 [4.83s](https://www.webpagetest.org/result/170715_KJ_1f08f67beb3451497c196a02e67dd71d/)

Framework/UI libraries:

Next.js, Preact

Module bundling:

Next.js with additional Webpack config

Service Worker:

Application & data caching with sw-precache

Performance patterns:

In memory LRU cache, DNS prefetch, preact-compat alias in production

Server-side rendering:

Yes

API:

Node-hnapi (unofficial)

Hosting:

Digital Ocean & Cloudflare

Author:

 [![Chris](../_resources/18c71432d82c5e9020199b210debe92b.png)](https://github.com/chrisdwheatley)

 [VIEW APP](https://nextjs-hn.chrisdwheatley.com/)  [SOURCE CODE](https://github.com/chrisdwheatley/nextjs-hn)

## Zuix HN

###   [genielabs/zuix-hn](https://github.com/g-labs-sw/zuix-hackernews)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170724_JT_fc286336283f4594b5e9a14ee486d437&run=3)

Interactive (Emerging Markets):

 [6.2s](https://www.webpagetest.org/result/170724_F6_c37ad291bb720b8c203da685d8a704b4/)

Interactive (Faster 3G):

 [4.8s](https://www.webpagetest.org/result/170724_JT_fc286336283f4594b5e9a14ee486d437/)

Framework/UI libraries:

ZUIX

Module bundling:

zuix-bundler

Service Worker:

Application Shell + Workbox data caching

Performance patterns:

Lazy loaded components with caching

Server-side rendering:

None

API:

Hacker News Firebase API

Hosting:

Firebase

Author:
 [![Gene](../_resources/f0f6456fd988e4e86c9500634d798f70.jpg)](https://github.com/genemars)

 [VIEW APP](https://zuix-hn.firebaseapp.com/)  [SOURCE CODE](https://github.com/g-labs-sw/zuix-hackernews)

## Vanilla HN

###   [cristianbote/hnpwa-vanilla](https://github.com/cristianbote/hnpwa-vanilla)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170712_QD_1962982caa117830d68f99b8e218bb67&run=3)

Interactive (Emerging Markets):

 [3.0s](https://www.webpagetest.org/result/170712_MJ_9eda2ffea1034eaf6426dfc6c5dec60f/)

Interactive (Faster 3G):

 [2.4s](https://www.webpagetest.org/result/170712_QD_1962982caa117830d68f99b8e218bb67/)

Module bundling:

Webpack

Service Worker:

Application Shell

Server-side rendering:

No

API:

hnpwa.com/api

Hosting:

Firebase static files hosting + preload/prefetch link headers

Author:

 [![Cristian](../_resources/6b9331c8a9a9273671c83262bb541a97.png)](https://github.com/cristianbote)

 [VIEW APP](https://hnpwa-vanilla.firebaseapp.com/)  [SOURCE CODE](https://github.com/cristianbote/hnpwa-vanilla)

## Glimmer HN

###   [mhadaily/glimmer-hn-pwa](https://github.com/mhadaily/glimmer-hn-pwa)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170920_JG_f68db76d6ecdfc19c30be596eab755a2&run=2)

Interactive (Emerging Markets):

 [4.12s](https://www.webpagetest.org/result/170920_TT_f75f4bf5930c888202f1c40443a9f4ec/)

Interactive (Faster 3G):

 [2.81s](https://www.webpagetest.org/result/170920_JG_f68db76d6ecdfc19c30be596eab755a2/)

Framework/UI libraries:

Glimmer.js

Scaffolding:

Ember CLI

Module bundling:

Broccoli

Service Worker:

Application Shell + data caching with ESW

Performance patterns:

Prefetch/Preload JS + DNS, Critical CSS, HTTP/2 Server Push

Server-side rendering:

None

API:

Node-hnapi (unofficial)

Hosting:

Firebase

Author:
 [![Majid](../_resources/970d6be542ab2195370fc7a168bcb322.jpg)](https://github.com/mhadaily)

 [VIEW APP](https://glimmer-hn-pwa.firebaseapp.com/)  [SOURCE CODE](https://github.com/mhadaily/glimmer-hn-pwa)

## Angular Hacker News

###   [alfredoperez/ngx-hn](https://github.com/alfredoperez/ngx-hn)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170726_49_9abc8ecb776d6d5081136f0867638dec&run=2)

Interactive (Emerging Markets):

 [5.5s](https://www.webpagetest.org/result/170726_49_9abc8ecb776d6d5081136f0867638dec/)

Interactive (Faster 3G):

 [4.5s](https://www.webpagetest.org/result/170726_7R_1c883338d59f1d6065984619829f3f3f/)

Framework/UI libraries:

Angular, ngu-pwa-tools

Scaffolding:

Angular CLI

Module bundling:

Angular CLI

Service Worker:

Application shell generated with ng-pwa-tools and service worker from @angular/service-worker

Performance patterns:

Lazy loaded modules

Server-side rendering:

None

API:

Node-hnapi (unofficial)

Hosting:

Firebase with HTTP/2 Server Push

Author:

 [![Alfredo](../_resources/177068eef9ef444a47bb745a26a60cb6.jpg)](https://github.com/alfredoperez)

 [VIEW APP](https://ngx-hn.firebaseapp.com/)  [SOURCE CODE](https://github.com/alfredoperez/ngx-hn)

## React HN

###   [stephenkingsley/hackerNews-pwa](https://github.com/stephenkingsley/hackerNews-pwa)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170826_0V_8516618e5aaa2650da5aabbc773c8929&run=3)

Interactive (Emerging Markets):

 [3.1s](https://www.webpagetest.org/result/170826_1T_9823f5188c7a02b16c87c1bb00826991/)

Interactive (Faster 3G):

 [2.41s](https://www.webpagetest.org/result/170826_8P_f18463655253ad388a2f129f75095afe/)

Framework/UI libraries:

React, React Router

Module bundling:

Webpack

Service Worker:

Application Shell

Server-side rendering:

No

API:

Node-hnapi (unoffical)

Hosting:

Firebase

Other details:

create-react-app

Author:

 [![Stephen](../_resources/6536ff9c291ac63cf6038f04b1b7c2c2.jpg)](https://github.com/stephenkingsley)

 [VIEW APP](https://hn-pwa-d8b2e.firebaseapp.com/)  [SOURCE CODE](https://github.com/stephenkingsley/hackerNews-pwa)

## Stencil HN

###   [ionic-team/ionic-stencil-hn-app](https://github.com/ionic-team/ionic-stencil-hn-app)

Lighthouse:

 [91/100](https://www.webpagetest.org/lighthouse.php?test=170913_V3_44c6e4792285dd5509e6c95fdc3188f3&run=3)

Interactive (Emerging Markets):

 [2.97s](https://www.webpagetest.org/result/170824_31_d8b43867baae06562c35baf8ea575c77/)

Interactive (Faster 3G):

 [1.92s](https://www.webpagetest.org/result/170913_V3_44c6e4792285dd5509e6c95fdc3188f3/)

Framework/UI libraries:

,

Service Worker:

Application Shell

Server-side rendering:

No

API:

HNPWA api

Hosting:

Firebase

Author:
 [![Justin](../_resources/740f40606388aae8b68f9eb73b96ee7f.jpg)](https://github.com/jgw96)

 [VIEW APP](https://corehacker-10883.firebaseapp.com/)  [SOURCE CODE](https://github.com/ionic-team/ionic-stencil-hn-app)

##  Submit your Hacker News Progressive Web App

If your Hacker News implementation meets the [specifications](https://github.com/tastejs/hacker-news-pwas#specification), feel free to submit a summary of it here! HNPWA serves as a reference for building PWAs with different libraries so the more examples we have the better. Don't worry if there's already one with the same UI library or framework as yours.

 [SUBMIT](https://github.com/tastejs/hacker-news-pwas/blob/master/CONTRIBUTING.md)

### Brought to you by

 [![Addy](../_resources/6584c2ef931fd29bdb01b6edc9dcc3e9.png)](https://github.com/addyosmani)

#### Addy

 [![Jonny](../_resources/66fdea5d4ac020a345ade81a80c9765a.jpg)](https://github.com/insin)

#### Jonny

 [![Kristofer](../_resources/59ac48080243d7ec88c3c517be579753.jpg)](https://github.com/kristoferbaxter)

#### Kristofer

 [![Rich](../_resources/cd44b7a6e0ba6ca46ef4f2e43598da9e.jpg)](https://github.com/Rich-Harris)

#### Rich

 [![Evan](../_resources/d2984f22a19a44dc01e5dbd87c00ac30.jpg)](https://github.com/yyx990803)

#### Evan

 [![Houssein](../_resources/42c1e7213518c1ba543ac9c2836ccd9a.jpg)](https://github.com/housseindjirdeh)

#### Houssein

 [![Andrea](../_resources/5f025a4c7e2703082ece34a911c1af27.png)](https://github.com/WebReflection)

#### Andrea

 [![Dan](../_resources/f63b0305e358d8bc1081d673e897ab5f.jpg)](https://github.com/azakus)

#### Dan

 [![Kevin](../_resources/1dda81086a125fbfee86c46b9fefdbbc.png)](https://github.com/kevinpschaaf)

#### Kevin

 [![Steve](../_resources/0feb35e708f45989d8720b99ca00b567.png)](https://github.com/sorvell)

#### Steve

 [![Chris](../_resources/18c71432d82c5e9020199b210debe92b.png)](https://github.com/chrisdwheatley)

#### Chris

 [![Ivan](../_resources/21acaaa6ce2cbed7f3f7d21020324c69.jpg)](https://github.com/ivanvanderbyl)

#### Ivan Vanderbyl

 [![Ryan](../_resources/219e074416c923f6e79b95bbd7480413.png)](https://github.com/chimon2000)

#### Ryan

 [![Gene](../_resources/f0f6456fd988e4e86c9500634d798f70.jpg)](https://github.com/genemars)

#### Gene

 [![Jimmy](../_resources/7816f9211b19483f4429d4984d75c03d.jpg)](https://github.com/ragingwind)

#### Jimmy

 [![Pooya](../_resources/6f925250c6a601cbb64d911dd3b61924.jpg)](https://github.com/pi0)

#### Pooya

 [![Sebastien](../_resources/1fbc3bd6a6eb4d1c224d06bab8af1450.jpg)](https://github.com/atinux)

#### Sebastien

 [![Alexandre](../_resources/06a3389032ba25addf4438c42c78bf8a.jpg)](https://github.com/alexchopin)

#### Alexandre

 [![Anubhav](../_resources/11b9c8feeac06481c64abdf465ad2148.jpg)](https://github.com/anubhav7495)

#### Anubhav

 [![Majid](../_resources/970d6be542ab2195370fc7a168bcb322.jpg)](https://github.com/mhadaily)

#### Majid

 [![Sebastian](../_resources/639aaebf8d3673b5e124db3c97aecfcf.jpg)](https://github.com/SebastianM)

#### Sebastian

 [![Cristian](../_resources/6b9331c8a9a9273671c83262bb541a97.png)](https://github.com/cristianbote)

#### Cristian

 [![David](../_resources/9ab096deda411de5b502dec19bbc48ad.png)](https://github.com/davideast)

#### David

 [![Alfredo](../_resources/177068eef9ef444a47bb745a26a60cb6.jpg)](https://github.com/alfredoperez)

#### Alfredo

 [![Justin](../_resources/740f40606388aae8b68f9eb73b96ee7f.jpg)](https://github.com/jgw96)

#### Justin

 [![Stephen](../_resources/6536ff9c291ac63cf6038f04b1b7c2c2.jpg)](https://github.com/stephenkingsley)

#### Stephen