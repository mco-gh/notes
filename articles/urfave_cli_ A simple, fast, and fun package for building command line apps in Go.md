urfave/cli: A simple, fast, and fun package for building command line apps in Go

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='132'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1511' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#cli)cli

[![68747470733a2f2f7472617669732d63692e6f72672f7572666176652f636c692e7376673f6272616e63683d6d6173746572](../_resources/6e77b43080c94e06849fc7e456ad1329.png)](https://travis-ci.org/urfave/cli)[![68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f7274676b3578756669393332706232763f7376673d74727565](../_resources/c241c28aa0a0d4586acb5fd42799d37b.png)](https://ci.appveyor.com/project/urfave/cli)

[![68747470733a2f2f676f646f632e6f72672f6769746875622e636f6d2f7572666176652f636c693f7374617475732e737667](../_resources/c0ae6d718a6ed6aa82e18bf73c19ef70.png)](https://godoc.org/github.com/urfave/cli)[![68747470733a2f2f636f6465626561742e636f2f6261646765732f30613866333061612d663937352d343034622d623837382d356661623361653163633566](../_resources/cb070832e2127f3fb2d5500627996dc9.png)](https://codebeat.co/projects/github-com-urfave-cli)[![68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f7572666176652f636c69](../_resources/c85ec881efaeed96c56f83d1588f2949.png)](https://goreportcard.com/report/urfave/cli)[![68747470733a2f2f636f6465636f762e696f2f67682f7572666176652f636c692f6272616e63682f6d61737465722f67726170682f62616467652e737667](../_resources/cacbd0aad3677642f534cc0b747d7c5d.png)](https://codecov.io/gh/urfave/cli)

cli is a simple, fast, and fun package for building command line apps in Go. The goal is to enable developers to write fast and distributable command line applications in an expressive way.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='133'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1516' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#usage-documentation)Usage Documentation

Usage documentation exists for each major version. Don't know what version you're on? You're probably using the version from the `master` branch, which is currently `v2`.

- `v2` - [./docs/v2/manual.md](https://github.com/urfave/cli/blob/master/docs/v2/manual.md)
- `v1` - [./docs/v1/manual.md](https://github.com/urfave/cli/blob/master/docs/v1/manual.md)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='134'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1522' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#using-v2-releases)Using `v2` releases

	$ GO111MODULE=on go get github.com/urfave/cli/v2

...import ( "github.com/urfave/cli/v2"  // imports as package "cli")
...

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='135'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1525' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#using-v1-releases)Using `v1` releases

	$ go get github.com/urfave/cli

...import ( "github.com/urfave/cli")
...

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='136'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1528' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#installation)Installation

Make sure you have a working Go environment. Go version 1.10+ is supported. [See the install instructions for Go](http://golang.org/doc/install.html).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='137'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1531' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#gopath)GOPATH

Make sure your `PATH` includes the `$GOPATH/bin` directory so your commands can be easily used:

	export PATH=$PATH:$GOPATH/bin

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='138'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1534' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/urfave/cli#supported-platforms)Supported platforms

cli is tested against multiple versions of Go on Linux, and against the latest released version of Go on OS X and Windows. This project uses Github Actions for builds. For more build info, please look at the [./.github/workflows/cli.yml](https://github.com/urfave/cli/blob/master/.github/workflows/cli.yml).