WebSockets for fun and profit - Stack Overflow Blog

# WebSockets for fun and profit

[![v5Nvpo3H.jpg](../_resources/07fb1d6e8f46d46a9f6aae5d872b5cf0.jpg)](https://stackoverflow.blog/authors/maxpekarsky/)[(L)](https://stackoverflow.blog/authors/maxpekarsky/)by [Max Pekarsky](https://stackoverflow.blog/authors/maxpekarsky/) on December 18, 2019

 AddThis Sharing Buttons

[Share to Twitter![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-twitter-1' style='fill: rgb(255%2c 255%2c 255)%3b width: 16px%3b height: 16px%3b' class='at-icon at-icon-twitter js-evernote-checked' data-evernote-id='145'%3e%3ctitle id='at-svg-twitter-1' data-evernote-id='146' class='js-evernote-checked'%3eTwitter%3c/title%3e%3cg data-evernote-id='147' class='js-evernote-checked'%3e%3cpath d='M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336' fill-rule='evenodd' data-evernote-id='148' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to LinkedIn![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-linkedin-2' style='fill: rgb(255%2c 255%2c 255)%3b width: 16px%3b height: 16px%3b' class='at-icon at-icon-linkedin js-evernote-checked' data-evernote-id='153'%3e%3ctitle id='at-svg-linkedin-2' data-evernote-id='154' class='js-evernote-checked'%3eLinkedIn%3c/title%3e%3cg data-evernote-id='155' class='js-evernote-checked'%3e%3cpath d='M26 25.963h-4.185v-6.55c0-1.56-.027-3.57-2.175-3.57-2.18 0-2.51 1.7-2.51 3.46v6.66h-4.182V12.495h4.012v1.84h.058c.558-1.058 1.924-2.174 3.96-2.174 4.24 0 5.022 2.79 5.022 6.417v7.386zM8.23 10.655a2.426 2.426 0 0 1 0-4.855 2.427 2.427 0 0 1 0 4.855zm-2.098 1.84h4.19v13.468h-4.19V12.495z' fill-rule='evenodd' data-evernote-id='156' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to Facebook![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-facebook-3' style='fill: rgb(255%2c 255%2c 255)%3b width: 16px%3b height: 16px%3b' class='at-icon at-icon-facebook js-evernote-checked' data-evernote-id='161'%3e%3ctitle id='at-svg-facebook-3' data-evernote-id='162' class='js-evernote-checked'%3eFacebook%3c/title%3e%3cg data-evernote-id='163' class='js-evernote-checked'%3e%3cpath d='M22 5.16c-.406-.054-1.806-.16-3.43-.16-3.4 0-5.733 1.825-5.733 5.17v2.882H9v3.913h3.837V27h4.604V16.965h3.823l.587-3.913h-4.41v-2.5c0-1.123.347-1.903 2.198-1.903H22V5.16z' fill-rule='evenodd' data-evernote-id='164' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)218]()

![iStock-485474145-945x630.jpg](../_resources/5804d2581f5d6631f7d302e9b7bb7364.jpg)

Seamless communication is a must on the modern web. As internet speeds increase, we expect our data in real time. To address this need, WebSocket, a popular communication protocol finalized in 2011, enables websites to send and receive data without delay. With WebSockets, you can build multiplayer games, chat apps, and collaboration software that work on the open web.

I built several projects with WebSockets before I started to wonder what exactly was happening under the hood. That question took me down a research rabbit hole, and I am excited to share what I’ve learned with you. In this article, we will:

1. explore the problem WebSockets solve and look at alternatives
2. look under the hood to understand how WebSockets work
3. review some simple code for a WebSocket-powered app
4. talk through some real-world implementations

By the end of this piece, you should feel comfortable discussing how WebSockets work, and maybe even inspired to use it in your next project.

## **Messaging on the internet**

Let’s start with the basics: **WebSocket **is a technology that allows a client to establish two-way (“[full-duplex](https://en.wikipedia.org/wiki/Duplex_(telecommunications)#FULL-DUPLEX)”) communication with the server. (A quick review: the client is the application on a user’s computer, and the server is the remote computer that stores the website and associated data).

The key word in that definition is *two-way*: with WebSocket, both the client *and* the server can trigger communication with one another, and both can send messages, at the same time. Why is this a big deal? To fully appreciate the power of WebSocket, let’s take a step back and look at a few common ways that computers can fetch data from the server.

### **Request-response**

In a traditional HTTP system, which is used by the majority of websites today, a web server is designed to receive and respond to requests from clients via [HTTP messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages). This traditional communication can only be initiated in one direction: from the client to the server. Server code defines what type of requests the server should expect and how to respond to each of them. A common metaphor for this type of communication is a restaurant kitchen. It goes something like this:

1. You (the client) places an order (an HTTP request) that a waiter takes to the kitchen (the server).

2. The kitchen receives the order and checks if they know how to make it (the server processes the request).

3. If the kitchen knows how to make the dish, they prepare the order (the server fetches data from a database or assets from the server).

4. If the kitchen doesn’t recognize the order or isn’t allowed to serve it, they send the waiter back with bad news (if the server doesn’t know how to or isn’t allowed to respond to the request, it sends back an error code, like a [404](https://en.wikipedia.org/wiki/HTTP_404)).

5. Either way, the waiter returns back to you (you get an HTTP response with an associated code, like 200 OK or 403 Forbidden).

The important thing to note here is that the kitchen has no idea who the order is coming from. The technical way to say this is that “HTTP is stateless”: it treats each new request as completely independent. We do have ways around that—for example, clients can send along cookies that help the server identify the client, but the HTTP messages themselves are distinct and are read and fulfilled independently.

Here’s the problem: the kitchen can’t send a waiter to you; it can only give the waiter a dish, or bad news, when *you* send the waiter over. The kitchen has no concept of *you*—only the orders that come in. In server-speak, **the only way for clients to get updated information from the server is to send requests**.

Imagine a chat app where you’re talking to a friend. You send a message to the server, as a request with some text as a payload. The server receives your request and stores the message. But, it has no way to reach out to your friend’s computer. Your friend’s computer *also* needs to send a request to check for new messages; only then can the server send over your message.

As it stands, you and your friend—both clients—need to constantly check the server for updates, introducing awkward delays between every message. That’s silly, right? When you send a message, you want the server to ping your friend immediately to say “Hey, you got a message! Here it is!” HTTP request-response works just fine when you need to load a static page, but it’s insufficient when your communication is time-sensitive.

### **Short polling**

One dead simple solution to this problem is a technique called short polling. Just have the client ping the server repeatedly, say, every 500ms (or over some fixed delay). That way, you get new data every 500ms. There are a few obvious downsides to this: there’s a 500ms delay, it consumes server resources with a barrage of requests, and most requests will return empty if the data isn’t frequently updated.

### **Long polling**

Another workaround to the delay in receiving data is a technique called long polling. In this method, the server receives a request, but doesn’t respond to it until it gets new data from another request. Long polling is more efficient than pinging the server repeatedly since it saves the hassle of parsing request headers, querying for new data, and sending often-empty responses. However, the server must now keep track of multiple requests and their order. Also, requests can time out, and new requests need to be issued periodically.

### **Server-Sent Events (SSE) / EventSource**

Another technique for sending messages is the**  **[Server-Sent Events API](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events), which allows the server to push updates to the client by leveraging the JavaScript [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) interface. EventSource opens a persistent, one-directional connection with the server over HTTP using a special text/event-stream header and listens for messages, which are treated like JavaScript events by your code.

This is *almost* what we’re looking for—we can now receive updates from the server! Because they’re one-directional, Server-Sent Events (SSE) are great for apps where you don’t need to send the server any data—for example, a Twitter-style news feed or a real-time dashboard of stock quotes. Another pro is that Server-Sent Events work over HTTP and the API is relatively easy to use. However, SSE is [not supported](https://caniuse.com/#feat=eventsource) by older browsers, and most browsers limit the number of SSE connections you can make at the same time. But, that’s still not quite enough for our chat app: it’s great to receive real-time updates, but we’d like to be able to send them too.

### **WebSockets**

So, we need a way to send information to the server, and receive updates from the server when updates come in. This brings us back to the two-way (“full-duplex”) communication we mentioned earlier. Enter WebSocket! [Supported by almost all modern browsers](https://caniuse.com/#feat=websockets), the WebSocket API allows us to open exactly that kind of two-way connection with the server. Moreover, the server can keep track of each client and push messages to a subset of clients. Great! With this capability we can invite all of our friends to our chat app and send messages to all of them, some of them, or only your best friend.

## **WebSockets under the hood**

So, how exactly does this magic work? Don’t be intimidated by the setup—modern WebSocket libraries like [socket.io](https://socket.io/) abstract away much of the setup, but it’s still helpful to understand how the technology works. If, at the end of this section, you’re interested in even *more* detail, check out the surprisingly readable [WebSocket RFC](https://tools.ietf.org/html/rfc6455).

In the last section, we mentioned HTTP several times. HTTP is a *protocol*, a set of rules for how computers communicate on the web. It’s made up of the requests and responses, each of which contains a request line (“GET /assets/icon.png”), headers, and an optional message body (used in, for example, POST requests to send some data to the server).

WebSocket is another protocol for sending and receiving messages. Both HTTP and WebSockets send messages over a TCP (Transmission Control Protocol) connection, which is a transport-layer standard that ensures streams of bytes, sent over in packets, are delivered reliably and predictably from one computer to another. So, HTTP and WebSockets use the same delivery mechanism at the packet/byte level, but the protocols for structuring the messages are different.

In order to establish a WebSocket connection with the server, the client first sends an HTTP [“handshake” request](https://en.wikipedia.org/wiki/WebSocket#Protocol_handshake) with an upgrade header, specifying that the client wishes to establish a WebSocket connection. The request is sent to a **ws:** or **wss::** URI (analogous to http or https). If the server is capable of establishing a WebSocket connection and the connection is allowed (for example, if the request comes from an authenticated or whitelisted client), the server sends a successful handshake response, indicated by HTTP code [101 Switching Protocols](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/101).

Once the connection is upgraded, the protocol switches from HTTP to WebSocket, and while packets are still sent over TCP, the communication now conforms to the WebSocket message format. Since TCP, the underlying protocol that transmits data packets, is a full-duplex protocol, both the client and the server can send messages at the same time. Messages can be fragmented, so it’s possible to send a huge message without declaring the size beforehand. In that case, WebSockets breaks it up into frames. Each frame contains a small header that indicates the length and type of payload and whether this is the final frame.

A server can open WebSocket connections with multiple clients—even multiple connections with the *same* client. It can then message one, some, or all of these clients. Practically, this means multiple people can connect to our chat app, and we can message some of them at a time.

Finally, when it’s ready to close the connection, either the client or the server can send over a “close” message.

*Whew*—nice job following along! Let’s take a quick break to stretch, and then look at some sample code.

## **A short example**

Now that you’re all loose from stretching (I wasn’t kidding before!), let’s switch gears from a technical overview to looking over some code. This will be much less complex—as I mentioned before, modern tooling saves us from having to worry about handshaking or frame OpCodes.

On the front end, we’ll use JavaScript to establish a connection to a WebSockets-enabled server, and then listen for messages as JavaScript events—the same way you’d listen to user-generated events like clicks and keypresses. [In vanilla JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket#Examples), we do this by creating a new **WebSocket **object and adding event listeners for **open**, **message, and close** events. We also use the **send **method to send data to the server.

	const socket = new WebSocket('ws://localhost:8080');
	socket.addEventListener('open', function (event) {
	  socket.send('Hello Server!');
	});

	socket.addEventListener('message', function (event) {
	  console.log('Message from server ', event.data);
	});

	socket.addEventListener('close', function (event) {
	  console.log('The connection has been closed');
	});

On the server, we similarly need to listen for WebSocket requests. In Node.js, for example, we can use the popular [ws](https://github.com/websockets/ws#usage-examples) package to open a connection and listen for messages:

	const WebSocket = require('ws');
	const ws = new WebSocket.Server({ port: 8080 });

	ws.on('connection', function connection(wsConnection) {
	  wsConnection.on('message', function incoming(message) {
	    console.log(`server received: ${message}`);
	  });

	  wsConnection.send('got your message!');
	});

Although in this example, we’re sending strings, a common use case of WebSockets is to send stringified JSON data or even [binary data](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/send), allowing you to structure your messages in the format convenient to you.

For a more complete example, [Socket.io](https://socket.io/), a popular front-end framework for making and managing WebSocket connections, has [a fantastic walkthrough](https://socket.io/get-started/chat/#The-web-framework) for building a Node/JavaScript chat app. This library automatically switches between WebSockets and long polling, and also simplifies broadcasting messages to [groups](https://socket.io/get-started/chat/#Broadcasting) of connected users.

## **In the wild**

Although you can manually write WebSocket server code, WebSockets is conveniently already built into popular frameworks. We’ve already touched on the Socket.io library on the front end. A few other implementations of WebSockets in larger projects are:

- [ActionCable](https://edgeguides.rubyonrails.org/action_cable_overview.html) in Ruby on Rails, a full-stack Ruby framework
- [Channels](https://channels.readthedocs.io/en/latest/) in Django, a full-stack Python framework
- [Gorilla](https://github.com/gorilla/websocket) in the Go language
- [Meteor](https://guide.meteor.com/methods.html), a full-stack JavaScript framework based on WebSockets instead of HTTP
- [Apollo](https://www.apollographql.com/), a GraphQL server that helps fetch data in real time using WebSockets

So, what types of projects can benefit from WebSockets? Any project that requires real-time, two-way communication is a great use case. Here are just a few kinds of applications often powered by WebSockets:

1. **Chat Apps:** a conceptually simple implementation WebSockets; users send messages to a server, which instantly pushes these messages to the recipient. No delay! The server can also store groups of connections in channels, allowing you to message multiple people at once, or see messages from multiple people in a room, like a Slack channel.

2. **Multiplayer Games:** A common pattern for multiplayer games is to have a server store a game state that serves as the source of truth. Players will take actions or make moves that are sent to the server, which updates the game state, and pushes it out to all players. With HTTP, each player needs to regularly request the game state. With WebSockets, each move is instantly relayed to all players.

3. **Collaboration Apps:** Need to work on a shared document or canvas? You can follow the pattern above to allow multiple users to draw or type in a document and instantly update it for everyone connected.

4. **Developer Tools:** Continuous Integration tools like CircleCI use WebSockets to instantly notify you when a build has finished. Need to send your client metrics around site performance and visitor count? Open a WebSocket connection and send updates as soon as the server receives them.

5. **Location-dependent apps**: Update your server when the user’s GPS coordinates have changed, then send the user new data based on their current coordinates.

## **A real-time recap**

Hopefully by now you’re sold on WebSockets! We’ve covered a lot of ground: we traced the problem WebSockets solves and the alternate solutions, explored how WebSockets operates under the hood, and even looked over some sample code and common use cases.

The WebSocket protocol is a wonderful tool to build real-time communication apps, but like all tools, it’s not a silver bullet. A WebSocket connection is meant to be persisted, so can be overkill for simpler apps. For a one-directional news feed, metrics feed, or any app where you need to update the client but not receive information in return, Server Sent Events or plain old HTTP calls are quicker and simpler to set up. However, for multiplayer games and collaborative apps, WebSockets opens up a world of possibilities. The real-time web is evolving, and the WebSocket protocol is a crucial cog in its evolution. Go forth and use it for good!

## Author

![v5Nvpo3H.jpg](../_resources/07fb1d6e8f46d46a9f6aae5d872b5cf0.jpg)
Max Pekarsky
Software Engineer

Max is a software engineer at Bonus.ly. In the past, he worked on product and engineering teams at Codecademy, the NYC Mayor's Office, and Indiegogo. He attended the Recurse Center in 2019.

[Author Archives](https://stackoverflow.blog/authors/maxpekarsky/)[Website](https://maximpekarsky.com/)[Twitter](https://twitter.com/@maxverse)

## Tags

- [Bulletin](https://stackoverflow.blog/tags/bulletin/)
- [Code for a Living](https://stackoverflow.blog/code-for-a-living/)
- [Stackoverflow](https://stackoverflow.blog/tags/stackoverflow/)

## Related Articles

![stack-overflow-podcast-social-3-300x158.png](../_resources/ad557fdd557700364dadbf97896dd7af.png)

## [Podcast: Time For Some Major League Hacking](https://stackoverflow.blog/2019/12/17/podcast-time-for-some-major-league-hacking/)

[(L)](https://stackoverflow.blog/authors/benpopper/)by [Ben Popper](https://stackoverflow.blog/authors/benpopper/) on December 17, 2019

To kick things off, we talk about Yap, a fun new project from Paul’s company, Postlight. Employees get to partake in a Labs program where they can pursue side projects...

[Continue reading](https://stackoverflow.blog/2019/12/17/podcast-time-for-some-major-league-hacking/)

![iStock-1027116394-1200x630.jpg](../_resources/eab9aa66552340a2c909b87b81bf0f91.jpg)

## [This || this: Whiteboard interviews](https://stackoverflow.blog/2019/12/16/this-this-whiteboard-interviews/)

[(L)](https://stackoverflow.blog/authors/sreynolds/)by [Scott C Reynolds](https://stackoverflow.blog/authors/sreynolds/) on December 16, 2019

Ed note: This is a part of series where an author plays both sides of an issue, one of which is obviously terrible. Can you guess which is which?

[Continue reading](https://stackoverflow.blog/2019/12/16/this-this-whiteboard-interviews/)

![iStock-647630956-1200x630.jpg](../_resources/37a83f7d833129e3f2bcc0a172db2382.jpg)

## [Preventing the Top Security Weaknesses Found in Stack Overflow Code Snippets](https://stackoverflow.blog/2019/12/02/preventing-the-top-security-weaknesses-found-in-stack-overflow-code-snippets/)

[(L)](https://stackoverflow.blog/authors/rdonovan/)by [Ryan Donovan](https://stackoverflow.blog/authors/rdonovan/) on December 2, 2019

Last week, we told you about research that found a number of security vulnerabilities in code snippets in Stack Overflow answers, and how some of those flaws had migrated into...

[Continue reading](https://stackoverflow.blog/2019/12/02/preventing-the-top-security-weaknesses-found-in-stack-overflow-code-snippets/)