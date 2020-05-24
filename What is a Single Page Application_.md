What is a Single Page Application?

# What is a Single Page Application?

## Modern Web Applications are also called Single Page Applications. What does this mean?

 Published Nov 11, 2018

> Learning JavaScript? Download my free **> [> JavaScript Handbook](https://flaviocopes.com/page/ebooks/)**>

* * *

In the past, when browsers were much less capable than today, and JavaScript performance was poor, every page was coming from a server. Every time you clicked something, a new request was made to the server and the browser subsequently loaded the new page.

Only very innovative products worked differently, and experimented with new approaches.

Today, popularized by modern frontend JavaScript frameworks like React, an app is usually built as a single page application: you only load the application code (HTML, [CSS](https://flaviocopes.com/css/), [JavaScript](https://flaviocopes.com/javascript/)) once, and when you interact with the application, what generally happens is that JavaScript intercepts the browser events and instead of making a new request to the server that then returns a new document, the client requests some JSON or performs an action on the server but the page that the user sees is never completely wiped away, and behaves more like a desktop application.

Single page applications are built in JavaScript (or at least compiled to JavaScript) and work in the browser.

The technology is always the same, but the philosophy and some key components of how the application works are different.

## Examples of Single Page Applications

Some notable examples:

- Gmail
- Google Maps
- Facebook
- Twitter
- Google Drive

## Pros and cons of SPAs

An SPA feels much faster to the user, because instead of waiting for the client-server communication to happen, and wait for the browser to re-render the page, you can now have instant feedback. This is the responsibility of the application maker, but you can have transitions and spinners and any kind of UX improvement that is certainly better than the traditional workflow.

In addition to making the experience faster to the user, the server will consume less resources because you can focus on providing an efficient API instead of building the layouts server-side.

This makes it ideal if you also build a mobile app on top of the API, as you can completely reuse your existing server-side code.

Single Page Applications are easy to transform into Progressive Web Apps, which in turn enables you to provide local caching and to support offline experiences for your services (or a better error message if your users need to be online).

SPAs are best used when there is no need for SEO (search engine optimization). For example for apps that work behind a login.

Search engines, while improving every day, still have trouble indexing sites built with an SPA approach rather than the traditional server-rendered pages. This is the case for blogs. If you are going to rely on search engines, don’t even bother with creating a single page application without having a server rendered part as well.

When coding an SPA, you are going to write a great deal of JavaScript. Since the app can be long-running, you are going to need to pay a lot more attention to possible memory leaks - if in the past your page had a lifespan that was counted in minutes, now an SPA might stay open for hours at a time and if there is any memory issue that’s going to increase the browser memory usage by a lot more and it’s going to cause an unpleasantly slow experience if you don’t take care of it.

SPAs are great when working in teams. Backend developers can just focus on the API, and frontend developers can focus on creating the best user experience, making use of the API built in the backend.

As a con, Single Page Apps rely heavily on JavaScript. This might make using an application running on low power devices a poor experience in terms of speed. Also, some of your visitors might just have JavaScript disabled, and you also need to consider accessibility for anything you build.

## Overriding the navigation

Since you get rid of the default browser navigation, URLs must be managed manually.

This part of an application is called the router. Some frameworks already take care of them for you (like Ember), others require libraries that will do this job (like [React Router](https://flaviocopes.com/react-router/)).

What’s the problem? In the beginning, this was an afterthought for developers building Single Page Applications. This caused the common “broken back button” issue: when navigating inside the application the URL didn’t change (since the browser default navigation was hijacked) and hitting the back button, a common operation that users do to go to the previous screen, might move to a website you visited a long time ago.

This problem can now be solved using the [History API](https://flaviocopes.com/history-api/) offered by browsers, but most of the time you’ll use a library that internally uses that API, like **React Router**.