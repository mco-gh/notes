Gin Web Framework

# Gin Gonic

The fastest full-featured web framework for Golang. **Crystal clear.**

[github pagE](https://github.com/gin-gonic/gin)[API REFERENCE](http://godoc.org/github.com/gin-gonic/gin)

$ go get github.com/gin-gonic/gin

## Performance and productivity can work together

Gin is a web framework written in Golang. It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity, you will love Gin.

 ![Martini vs Gin](../_resources/51376658f0977894e54167557f249a3c.png)
2,3 GHz Intel Core i7 8 GB 1600 MHz DDR3,  OS X 10.9.3

[Check out the benchmark suite](https://github.com/gin-gonic/go-http-routing-benchmark)

## Low Overhead Powerful API

You can add global, per-group, and per-route middlewares, thousands of nested groups, nice JSON validation and rendering. And the performance will be still great. Gin uses **httprouter** internally, the fastest HTTP router for Golang. Httprouter was created by Julien Schmidt and it’s based in a [Radix Tree](http://en.wikipedia.org/wiki/Radix_tree) algorithm.

### Some cool middlewares

If you used Martini before, Gin will be familiar to you. If you don’t, you will need 10 minutes to learn everything.

[Check out the Sentry midDlEware](https://github.com/gin-gonic/gin-sentry)
More coming soon

### Crystal Clear

If you used Martini before, Gin will be familiar to you. If you don’t, you will need 10 minutes to learn everything.

 ![539f93b8f281585418675d91_sample1.png](../_resources/a6a99dacb25236fea59bf1fb3efbfe3b.png)
 ![539f93ccf281585418675d92_sample11.png](../_resources/ae391133828980dd290e29af74168d10.png)



[More examples in the README.md](https://github.com/gin-gonic/gin/blob/master/README.md)

## Full Featured

 **

### Fast

Radix tree based routing, small memory foot print. No reflection. Predictable API performance.

 **

### Middleware support

A incoming HTTP request can be handled by a chain of middlewares and the final action.

For example: Logger, Authorization, GZIP and finally post a message in the DB.

 **

### Crash-free

Gin can catch a panic occurred during a HTTP request and recover it. This way, your server will be always available. It’s also possible to report this panic to Sentry for example!

 **

### JSON validation

Gin can parse and validate the JSON of a request, checking for example the existence of required values.

 **

### Routes grouping

Organize your routes better. Authorization required vs non required, different API versions... In addition, the groups can be nested unlimitedly without degrading performance.

 **

### Error management

Gin provides a convenient way to collect all the errors occurred during a HTTP request. Eventually, a middleware can write them to a log file, to a database and send them through the network.

 **

### Rendering built-in

Gin provides a easy to use API for JSON, XML and HTML rendering.

 **

### Extendable

Creating a new middleware is so easy, just check out the sample codes.

## How to contribute?

Gin uses a MIT license, this means that you can do whatever you want, but please, keep the reference to the original authors! To contribute you should [fork it in Github](https://github.com/gin-gonic/gin), add some changes and start posting Pull Requests, we would love to merge them.

1. Fork

 ![539e4fca30eda3837a903182_Git-Icon-Black2.png](../_resources/3d31b74b5a6b03015e0f3b9429d8ff75.png)

2. Commit
 ![539e4fbbaa3db5690ebc0c8c_idea2.png](../_resources/e0ca4ab387df84d8cbcaa5b975f5560f.png)

3. Pull request
 ![539e4fadaa3db5690ebc0c8b_pull2.png](../_resources/f86931cd191530a3ce0b8088095df774.png)

Gin is developed and maintained by *[Manu Martinez-Almeida](https://github.com/manucorporat)*.

It uses the fantastic *[Julien Schmidt](https://github.com/julienschmidt) *’s httprouter.