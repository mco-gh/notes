HTTPie – command line HTTP client

[HTTPie](https://httpie.org/)

[Docs](https://httpie.org/doc)[Demo](https://httpie.org/run)[GitHub](https://github.com/jakubroztocil/httpie)[Twitter](https://twitter.com/clihttp)[Donate](https://paypal.me/roztocil)

HTTPie*—aitch-tee-tee-pie—*is a command line HTTP client with an intuitive UI, JSON support, syntax highlighting, wget-like downloads, plugins, and more.

![httpie.gif](../_resources/70bc5a5b7fdf2b4982ed18b364c32b11.gif)

[Install](https://httpie.org/#installation)[Try online](https://httpie.org/run)[Read docs](https://httpie.org/doc)

[Star](https://github.com/jakubroztocil/httpie/)  [44,337](https://github.com/jakubroztocil/httpie/stargazers)

![httpie2.png](../_resources/1f6219a5a07bb6e99aa7afd98d0e67ec.png)

HTTPie consists of a single `http` command designed for painless debugging and interaction with HTTP servers, RESTful APIs, and web services, which it accomplishes by:

- Sensible defaults
- Expressive and intuitive command syntax
- Colorized and formatted terminal output
- Built-in JSON support
- Persistent sessions
- Forms and file uploads
- HTTPS, proxies, and authentication support
- Support for arbitrary request data and headers
- Wget-like downloads
- Extensions
- Linux, macOS, and Windows support
- And more…

[See all features](https://httpie.org/doc)

## Installation

HTTPie can be installed on any operating system.
$<tool>install httpie
[Read more](https://httpie.org/doc#installation)

## Getting started

Custom [HTTP method](https://httpie.org/doc#http-method), [HTTP headers](https://httpie.org/doc#http-headers) and [JSON](https://httpie.org/doc#json) data:

$ http PUT example.org X-API-Token:123 name=John
Submitting [forms](https://httpie.org/doc#forms):
$ http -f POST example.org hello=World

See the request that is being sent using one of the [output options](https://httpie.org/doc#output-options):

$ http -v example.org

Use [Github API](https://developer.github.com/v3/issues/comments/#create-a-comment) to post a comment on an[issue](https://github.com/jakubroztocil/httpie/issues/83)with [authentication](https://httpie.org/doc#authentication):

$ http -a USERNAME POST https://api.github.com/repos/jakubroztocil/httpie/issues/83/comments body='HTTPie is awesome! :heart:'

Upload a file using [redirected input](https://httpie.org/doc#redirected-input):

$ http example.org < file.json

Download a file and save it via [redirected output](https://httpie.org/doc#redirected-output):

$ http example.org/file > file
Download a file `wget` style:
$ http --download example.org/file

Use named [sessions](https://httpie.org/doc#sessions) to make certain aspects or the communication persistent between requests to the same host:

$ http --session=logged-in -a username:password httpbin.org/get API-Key:123$ http --session=logged-in httpbin.org/headers

Set a custom `Host` header to work around missing DNS records:
$ http localhost:8000 Host:example.com
[Learn more](https://httpie.org/doc)

## Testimonials

More #love on[Twitter](https://twitter.com/search?vertical=default&q=httpie&src=typd),[GitHub](https://github.com/jakubroztocil/httpie/issues/83#issuecomment-7667482)

[Share on Twitter](https://twitter.com/intent/tweet?via=clihttp&related=jakubroztocil&text=HTTPie%20%E2%80%94%20CLI%20HTTP%20client%20with%20JSON%20support,%20syntax%20highlighting,%20plugins,%20and%20more!%20https://httpie.org)[Follow @clihttp](https://twitter.com/intent/follow?screen_name=clihttp)

## Newsletter

Join the occasional HTTPie newsletter for news and tips.

 © 2012–2019[Jakub Roztočil](https://roztocil.co/)