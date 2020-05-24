HTTP/2 comes to Firebase Hosting

## [HTTP/2 comes to Firebase Hosting](http://firebase.googleblog.com/2016/09/http2-comes-to-firebase-hosting.html)

September 21, 2016

 ![Michael Bleigh](../_resources/839cd015cc7c176c1be80f25899e42f4.jpg)

 **
Michael Bleigh
**  *Engineer*

Today we're excited to announce the availability of HTTP/2 on Firebase Hosting. HTTP/2 is a new version of the HTTP protocol that is already supported by [77% of browsers](http://caniuse.com/#feat=http2) worldwide. It offers some exciting advantages for web developers:

- Multiple requests can be sent over a single connection. With HTTP/2, it's less necessary to concatenate resources together.
- It's a binary protocol, which means headers can be compressed and data can generally be sent more efficiently.
- Servers can proactively "push" content to clients.

Taken together, these add up to significant performance advantages and lots of opportunity to make your web applications load faster on mobile devices with slow connections.

HTTP/2 is currently enabled for all `*.firebaseapp.com` traffic as well as newly-provisioned custom domains. If you already have a custom domain on Firebase, see **Custom Domain Migration** below.

## Leveraging HTTP/2 on Firebase Hosting

**To utilize HTTP/2 on Firebase Hosting, you don't have to do anything!** It will automatically be served if the user's browser supports it. However, there are some best practices you should keep in mind if you want to optimize for HTTP/2:

1. Because a single connection can be used to multiplex simultaneous requests, there is no longer an advantage to concatenate lots of resources together. Since browsers do a good job of caching resources, it's actually better to serve more files that change less often. Be aware though that by more files, we mean in the tens, as hundreds [can still carry significant overhead.](http://stackoverflow.com/questions/28630108/does-minifying-and-concatenating-js-css-files-and-using-sprites-for-images-stil/28631462#28631462)

2. It is no longer necessary (or desirable) to "split" assets up between many domains. Firebase Hosting is already served over a fast CDN, and HTTP/2 makes it advantageous to serve all of your files from the same domain.

3. Only load the assets you need! With fewer round trips, you should optimize your site to load only the files you need to bootstrap your application shell. Other resources should be loaded on-demand based on user interaction.

The above guidelines aren't hard and fast rules -- as with any performance optimization, you should experiment with different combinations of optimizations to see which ones deliver the best result for your app's specific needs.

## Experimenting with Server Push

Firebase Hosting has experimental support for HTTP/2 server push using [Link headers](https://w3c.github.io/preload/#server-push-http-2). Server push allows a server to automatically send the contents for additional resources when an initial request is made. The most common use for server push is to send down associated assets (like JavaScript or CSS files) when a page is loaded.

To configure server push on Firebase Hosting, you need to add the Link header to your `firebase.json` configuration like so:

{  "hosting":  {  "headers":  [  {  "source":  "/",  "headers":  [{"key":  "Link",  "value":  "</js/app.js>;rel=preload;as=script,</css/app.css>;rel=preload;as=style"}]  },  {  "source":  "/users/*",  "headers":  [{"key":  "Link",  "value":  "</js/app.js>;rel=preload;as=script,</css/app.css>;rel=preload;as=style;nopush,</css/users.css>;rel=preload;as=style"}]  }  ]  }}

Here we are using server push to preload `/js/app.js` and `/css/app.css` on the root path, and additionally `/css/users.css` on any path matching `/users/*`. You can use the nopush directive (like on `app.css` in the second example) to preload the asset without HTTP/2 push for files that are likely to already be in the browser cache.

It's still early days for server push, and there are a few things to keep in mind:

1. Be careful with wildcards in setting Link headers. Resources should never be set to preload themselves.

2. Server push is a tradeoff between performance and bandwidth usage -- if you push assets that are already cached by the browser you'll be sending unnecessary data. Try to keep pushed assets to small, critical-to-performance assets and be aware that your users may have to pay for that extra data on their mobile devices!

3. Preloading is great for performance even without push! If you add `;nopush` to your preload Link header, it will tell the browser to preload it without server push. This is great for assets you think may already be cached in the browser.

We're excited about HTTP/2's potential to improve that first-load experience, and we're still exploring additional ways to make server push simple, reliable, and effective for your site.

## Custom Domain Migration

With our migration to HTTP/2 we're also moving to Server Name Indication (SNI) for our SSL certificates. SNI enables us to continue to scale our infrastructure more reliably and is supported by nearly [98% of browsers worldwide](http://caniuse.com/#feat=sni). Because this change has the possibility of affecting user traffic, we are not automatically switching over existing custom domains until December 2016.

If you have a custom domain on Firebase Hosting from before August 11, 2016, you will need to update your DNS records to take advantage of HTTP/2. You can check if you're already on SNI by running `dig <your-site>.firebaseapp.com`. If you see `s-sni.firebaseapp.com` in the result, your site is already migrated.

To migrate if you're using a CNAME, update your DNS to point to `s-sni.firebaseapp.com`. If you're using A records, update them to:

151.101.1.195151.101.65.195

Once you've changed over your DNS and it's had the chance to propagate, your site will be live with HTTP/2! We will be transitioning all Firebase Hosting traffic to HTTP/2 and SNI by the end of the year, so please [reach out to support](https://firebase.google.com/support/) if you're worried about how SNI might affect your users.

Our goal with Firebase Hosting is to bring the best practices of Progressive Web App development within reach of everyone. HTTP/2 is another step along that path, and we're excited to see what you build with it!