nhooyr/websocket

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='165'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1225' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#websocket)websocket

[![68747470733a2f2f676f646f632e6f72672f6e686f6f79722e696f2f776562736f636b65743f7374617475732e737667](../_resources/942b10558d95586a5618575f1c2b174e.png)](https://godoc.org/nhooyr.io/websocket)[![68747470733a2f2f696d672e736869656c64732e696f2f636f6465636f762f632f6769746875622f6e686f6f79722f776562736f636b65742e7376673f636f6c6f723d627269676874677265656e](../_resources/efc31f221d22d51a83c9399464d41aa7.png)](https://codecov.io/gh/nhooyr/websocket)

websocket is a minimal and idiomatic WebSocket library for Go.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='166'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1229' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#install)Install

go get nhooyr.io/websocket@v1.0.0

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='167'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1232' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#features)Features

- Minimal and idiomatic API
- Tiny codebase at 1700 lines
- First class context.Context support
- Thorough tests, fully passes the [autobahn-testsuite](https://github.com/crossbario/autobahn-testsuite)
- Zero dependencies outside of the stdlib for the core library
- JSON and ProtoBuf helpers in the wsjson and wspb subpackages
- Highly optimized by default
- Concurrent writes out of the box

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='168'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1243' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#roadmap)Roadmap

- WebSockets over HTTP/2 [#4](https://github.com/nhooyr/websocket/issues/4)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='169'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1247' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#examples)Examples

For a production quality example that shows off the full API, see the [echo example on the godoc](https://godoc.org/nhooyr.io/websocket#example-package--Echo). On github, the example is at [example_echo_test.go](https://github.com/nhooyr/websocket/blob/master/example_echo_test.go).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='170'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1250' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#server)Server

http.HandlerFunc(func (w http.ResponseWriter, r *http.Request) {c, err  := websocket.Accept(w, r, websocket.AcceptOptions{})if err != nil {// ...}defer c.Close(websocket.StatusInternalError, "the sky is falling")ctx, cancel  := context.WithTimeout(r.Context(), time.Second*10)defer  cancel()var  v  interface{}

err = wsjson.Read(ctx, c, &v)if err != nil {// ...}
log.Printf("received: %v", v)
c.Close(websocket.StatusNormalClosure, "")
})

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='171'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1253' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#client)Client

The client side of this library requires at minimum Go 1.12 as it uses a [new feature in net/http](https://github.com/golang/go/issues/26937#issuecomment-415855861) to perform WebSocket handshakes.

ctx, cancel  := context.WithTimeout(context.Background(), time.Minute)defer  cancel()c, _, err  := websocket.Dial(ctx, "ws://localhost:8080", websocket.DialOptions{})if err != nil {// ...}defer c.Close(websocket.StatusInternalError, "the sky is falling")

err = wsjson.Write(ctx, c, "hi")if err != nil {// ...}
c.Close(websocket.StatusNormalClosure, "")

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='172'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1257' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#design-justifications)Design justifications

- A minimal API is easier to maintain due to less docs, tests and bugs
- A minimal API is also easier to use and learn
- Context based cancellation is more ergonomic and robust than setting deadlines
- net.Conn is never exposed as WebSocket over HTTP/2 will not have a net.Conn.
- Using net/http's Client for dialing means we do not have to reinvent dialing hooks and configurations like other WebSocket libraries
- We do not support the deflate compression extension because Go's compress/flate library is very memory intensive and browsers do not handle WebSocket compression intelligently. See [#5](https://github.com/nhooyr/websocket/issues/5)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='173'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1266' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#comparison)Comparison

Before the comparison, I want to point out that both gorilla/websocket and gobwas/ws were extremely useful in implementing the WebSocket protocol correctly so *big thanks* to the authors of both. In particular, I made sure to go through the issue tracker of gorilla/websocket to ensure I implemented details correctly and understood how people were using WebSockets in production.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='174'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1270' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#gorillawebsocket)gorilla/websocket

https://github.com/gorilla/websocket

This package is the community standard but it is 6 years old and over time has accumulated cruft. There are too many ways to do the same thing. Just compare the godoc of[nhooyr/websocket](https://godoc.org/github.com/nhooyr/websocket) side by side with[gorilla/websocket](https://godoc.org/github.com/gorilla/websocket).

The API for nhooyr/websocket has been designed such that there is only one way to do things which makes it easy to use correctly. Not only is the API simpler, the implementation is only 1700 lines whereas gorilla/websocket is at 3500 lines. That's more code to maintain, more code to test, more code to document and more surface area for bugs.

The future of gorilla/websocket is also uncertain. See [gorilla/websocket#370](https://github.com/gorilla/websocket/issues/370).

Moreover, nhooyr/websocket has support for newer Go idioms such as context.Context and also uses net/http's Client and ResponseWriter directly for WebSocket handshakes. gorilla/websocket writes its handshakes to the underlying net.Conn which means it has to reinvent hooks for TLS and proxies and prevents support of HTTP/2.

Some more advantages of nhooyr/websocket are that it supports concurrent writes and makes it very easy to close the connection with a status code and reason.

nhooyr/websocket also responds to pings, pongs and close frames in a separate goroutine so that your application doesn't always need to read from the connection unless it expects a data message. gorilla/websocket requires you to constantly read from the connection to respond to control frames even if you don't expect the peer to send any messages.

In terms of performance, the differences depend on your application code. nhooyr/websocket reuses buffers efficiently out of the box if you use the wsjson and wspb subpackages whereas gorilla/websocket does not. As mentioned above, nhooyr/websocket also supports concurrent writers out of the box.

The only performance con to nhooyr/websocket is that uses two extra goroutines. One for reading pings, pongs and close frames async to application code and another to support context.Context cancellation. This costs 4 KB of memory which is cheap compared to the benefits.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='175'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1281' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#xnetwebsocket)x/net/websocket

https://godoc.org/golang.org/x/net/websocket

Unmaintained and the API does not reflect WebSocket semantics. Should never be used.

See https://github.com/golang/go/issues/18152

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='176'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1286' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/nhooyr/websocket#gobwasws)gobwas/ws

https://github.com/gobwas/ws

This library has an extremely flexible API but that comes at the cost of usability and clarity.

This library is fantastic in terms of performance. The author put in significant effort to ensure its speed and I have applied as many of its optimizations as I could into nhooyr/websocket. Definitely check out his fantastic [blog post](https://medium.freecodecamp.org/million-websockets-and-go-cc58418460bb)about performant WebSocket servers.

If you want a library that gives you absolute control over everything, this is the library, but for most users, the API provided by nhooyr/websocket will fit better as it is nearly just as performant but much easier to use correctly and idiomatic.