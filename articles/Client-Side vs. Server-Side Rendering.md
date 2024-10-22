Client-Side vs. Server-Side Rendering

[home](http://openmymind.net/)

# Client-Side vs. Server-Side Rendering

30 May 2012

Yesterday Twitter announced that it was [moving away from client-side rendering back to server-side rendering](http://engineering.twitter.com/2012/05/improving-performance-on-twittercom.html) in order to improve page load time. Today I found myself having to defend my position that server-side rendering will almost always be faster. I figured I'd blog about it.

I want to point out a couple things. First, I'm talking specifically about render performance and page speed. There might be other compelling advantages to thick-clients; I'm talking about performance. Secondly, I'm going to get on a high horse here and say that it **worries me that developers think client-side rendering is faster**. This is basic and fundamental knowledge about how the web and browsers work. Maybe I'll be proven wrong. If I am, I'll admit it. It'll be embarrassing because it means that I don't know the fundamentals. But I'll be glad to have learned (which is why I blog).

### How It Works

With client-side rendering, your initial request loads the page layout, CSS and JavaScript. It's all common except that some or all of the content isn't included. Instead, the JavaScript makes another request, gets a response (likely in JSON), and generates the appropriate HTML (likely using a templating library).

With server-side rendering, your initial request loads the page, layout, CSS, JavaScript and content.

For subsequent updates to the page, the client-side rendering approach repeats the steps it used to get the initial content. Namely, JavaScript is used to get some JSON data and templating is used to create the HTML.

Updates using server-side rendering is where a lot of developers start going off the deep end. They actually think *page refresh*. Instead, what I thought we've all been doing for the last half decade, is some form of:

$('#loadTweets').on('click', function(e) {  $.get('/tweets/person', {last_id: 239393939}, function(r) {  $('#tweets').prepend(r);

});
e.preventDefaults();
});

In other words, we are still only doing a partial update, but letting the server do the rendering and inserting that finalized output into our DOM.

So those are the two workflows. Let's see why client-side rendering is slower.

### Initial Load

Comparing the initial flow of the two approaches, it should be obvious that client-side rendering is going to be slower. It requires more JavaScript to be downloaded, which is more JavaScript to parse. It requires a 2nd HTTP request to load the content, and then requires more JavaScript to generate the template. Even if the initial JavaScript gets cached, it still needs to get parsed, and the 2nd request isn't going to happen until the document is loaded.

I could see bootstrapping the initial request to include the initial data as a JavaScript object. But I don't see many frameworks advocating this approach. I'm not sure I like it. And it would still be more JavaScript to download, parse and more cycles on the CPU to render it.

### Control

One of the biggest problem with client-side rendering is that you lose control over the experience. Developers are building sites with 8-core boxes and 16 gigs of ram, running the latest OS and latest non-IE browser. With the site running locally. They think "geez, this is fast!" Meanwhile I'm trying to load your site on my horrible Samsung Galaxy S or my underpowered air.

Parsing JavaScript is slow..especially on some still popular browsers. Even on modern browsers, parsing some JavaScript is going to be slower than parsing less JavaScript.. This is especially true when you consider mobile devices. If you do rendering on the server, you have a lot more control over how fast and how consistent that rendering is. Overloaded? Buy more hardware. The client still has to render the HTML (it has to do this either way), but it doesn't have the extra JavaScript and templating overhead.

### Caching

If your end points only return JSON, then all you'll be able to cache on the backend is JSON. The client will always have to spend time building the HTML elements from that data. If your end points return HTML, you can cache that instead. By rendering on the server, you can cache the final shape of your data. So not only does your client not have to generate templates, your server doesn't have to either.

And while we are at it, I want to point out that generating JSON on the server isn't a no-op operation. I'll admit that rendering JSON is probably quicker than rendering an ERB template, but people talk about it as though it just magically happens for free. (Although, if you are caching the HTML template, you can certainly cache the JSON as well).

### Bandwidth

With client-side rendering your initial load will be and feel heavier: again, more JavaScript and a 2nd request. However, subsequent updates will require less bandwidth. JSON is pretty verbose, but it's probably less verbose than HTML with classes and ids. This is an area where client-side rendering will be faster (if we ignore the fact that we client-side rendering still needs to spend time transforming the JSON to HTML).However, both HTML and JSON should compress quite well.

I'm legitimately drawing a blank trying to come up with a pattern where the JSON data would be significantly smaller. If it's a collection of data (like search results), it'll just be the same divs with the same class name...much like it'll be the same JSON fields. I guess client-side rendering might have a real edge if you are using Word to generate your html...

### A single API/Endpoint

I know I said I'd only talk about performance, but one argument that often gets brought up is that by consuming JSON, the browser is just another consumer your public API. The result is a single endpoint and clean routes.

Your server-side framework should let you respond to different requests types with minimal effort. In Rails this is done via [respond_to](http://apidock.com/rails/ActionController/MimeResponds/InstanceMethods/respond_to). If your framework doesn't support something similar, either build it, or change frameworks.

### Conclusion

Only considering performance, should you ever use client-side rendering? There's one obvious scenario where it makes sense: when you render based on existing data. That is, if you don't need to go to the server to render, say because you are going to display known data in a different perspective, client-side rendering makes sense.

Otherwise, client-side rendering requires a heavier initial load with a 2nd request, not being able to cache the final output and greater dependency on slower CPUs and rendering engines. Any one of those is a going to make client-side rendering slower. Combine them? Well, Twitter's server-side rendering takes 1/5 the time as client-side rendering.

If you are interested in learning more, I suggest you also check out [How Basecamp Next was built to be so fast](http://37signals.com/svn/posts/3112-how-basecamp-next-got-to-be-so-damn-fast-without-using-much-client-side-ui).

[(L)](http://openmymind.net/2012/5/30/Client-Side-vs-Server-Side-Rendering/#)Window size:  x

Viewport size:  x
![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[3 min to Spreed]()