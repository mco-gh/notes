jakubroztocil/httpie: As easy as HTTPie /aitch-tee-tee-pie/ 🥧 Modern command line HTTP client – user-friendly curl alternative with intuitive UI, JSON support, syntax highlighting, wget-like downloads, extensions, etc. https://twitter.com/clihttp

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='490'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2309' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#httpie-a-cli-curl-like-tool-for-humans)HTTPie: a CLI, cURL-like tool for humans

HTTPie (pronounced *aitch-tee-tee-pie*) is a command line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible. It provides a simple `http` command that allows for sending arbitrary HTTP requests using a simple and natural syntax, and displays colorized output. HTTPie can be used for testing, debugging, and generally interacting with HTTP servers.

[![68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6874747069652e7376673f7374796c653d666c61742d737175617265266c6162656c3d6c6174657374253230737461626c6525323076657273696f6e](../_resources/c77347c95abfdddefc970a2c3da1f84d.png)](https://pypi.python.org/pypi/httpie)  [![](../_resources/1a9cb950d3a48f5062750b7b5bc3f548.png)](https://github.com/jakubroztocil/httpie/actions)  [![68747470733a2f2f696d672e736869656c64732e696f2f636f6465636f762f632f6769746875622f6a616b7562726f7a746f63696c2f6874747069653f7374796c653d666c61742d737175617265](../_resources/5352472887d89b3c08810838c0bbc3be.png)](https://codecov.io/gh/jakubroztocil/httpie)  [![68747470733a2f2f706570792e746563682f62616467652f687474706965](../_resources/d04970a01ad9a155563117307f308b98.png)](https://pepy.tech/project/httpie)  [![68747470733a2f2f696d672e736869656c64732e696f2f6769747465722f726f6f6d2f6a6b62727a742f6874747069652e7376673f7374796c653d666c61742d737175617265](../_resources/3918900675fb4eb33505c7cc3de87879.png)](https://gitter.im/jkbrzt/httpie)

[![httpie.gif](../_resources/70bc5a5b7fdf2b4982ed18b364c32b11.gif)](https://raw.githubusercontent.com/jakubroztocil/httpie/master/httpie.gif)

Contents

- [1   Main features](https://github.com/jakubroztocil/httpie#main-features)
- [2   Installation](https://github.com/jakubroztocil/httpie#installation)
    - [2.1   macOS](https://github.com/jakubroztocil/httpie#macos)
    - [2.2   Linux](https://github.com/jakubroztocil/httpie#linux)
    - [2.3   Windows, etc.](https://github.com/jakubroztocil/httpie#windows-etc)
    - [2.4   Python version](https://github.com/jakubroztocil/httpie#python-version)
    - [2.5   Unstable version](https://github.com/jakubroztocil/httpie#unstable-version)
- [3   Usage](https://github.com/jakubroztocil/httpie#usage)
    - [3.1   Examples](https://github.com/jakubroztocil/httpie#examples)
- [4   HTTP method](https://github.com/jakubroztocil/httpie#http-method)
- [5   Request URL](https://github.com/jakubroztocil/httpie#request-url)
    - [5.1   Querystring parameters](https://github.com/jakubroztocil/httpie#querystring-parameters)
    - [5.2   URL shortcuts for `localhost`](https://github.com/jakubroztocil/httpie#url-shortcuts-for-localhost)
    - [5.3   Other default schemes](https://github.com/jakubroztocil/httpie#other-default-schemes)
- [6   Request items](https://github.com/jakubroztocil/httpie#request-items)
    - [6.1   Escaping rules](https://github.com/jakubroztocil/httpie#escaping-rules)
- [7   JSON](https://github.com/jakubroztocil/httpie#json)
    - [7.1   Default behaviour](https://github.com/jakubroztocil/httpie#default-behaviour)
    - [7.2   Explicit JSON](https://github.com/jakubroztocil/httpie#explicit-json)
    - [7.3   Non-string JSON fields](https://github.com/jakubroztocil/httpie#non-string-json-fields)
- [8   Forms](https://github.com/jakubroztocil/httpie#forms)
    - [8.1   Regular forms](https://github.com/jakubroztocil/httpie#regular-forms)
    - [8.2   File upload forms](https://github.com/jakubroztocil/httpie#file-upload-forms)
- [9   HTTP headers](https://github.com/jakubroztocil/httpie#http-headers)
    - [9.1   Default request headers](https://github.com/jakubroztocil/httpie#default-request-headers)
    - [9.2   Empty headers and header un-setting](https://github.com/jakubroztocil/httpie#empty-headers-and-header-un-setting)
    - [9.3   Limiting response headers](https://github.com/jakubroztocil/httpie#limiting-response-headers)
- [10   Cookies](https://github.com/jakubroztocil/httpie#cookies)
- [11   Authentication](https://github.com/jakubroztocil/httpie#authentication)
    - [11.1   Basic auth](https://github.com/jakubroztocil/httpie#basic-auth)
    - [11.2   Digest auth](https://github.com/jakubroztocil/httpie#digest-auth)
    - [11.3   Password prompt](https://github.com/jakubroztocil/httpie#password-prompt)
    - [11.4   `.netrc`](https://github.com/jakubroztocil/httpie#netrc)
    - [11.5   Auth plugins](https://github.com/jakubroztocil/httpie#auth-plugins)
- [12   HTTP redirects](https://github.com/jakubroztocil/httpie#http-redirects)
    - [12.1   Follow `Location`](https://github.com/jakubroztocil/httpie#follow-location)
    - [12.2   Showing intermediary redirect responses](https://github.com/jakubroztocil/httpie#showing-intermediary-redirect-responses)
    - [12.3   Limiting maximum redirects followed](https://github.com/jakubroztocil/httpie#limiting-maximum-redirects-followed)
- [13   Proxies](https://github.com/jakubroztocil/httpie#proxies)
    - [13.1   Environment variables](https://github.com/jakubroztocil/httpie#environment-variables)
    - [13.2   SOCKS](https://github.com/jakubroztocil/httpie#socks)
- [14   HTTPS](https://github.com/jakubroztocil/httpie#https)
    - [14.1   Server SSL certificate verification](https://github.com/jakubroztocil/httpie#server-ssl-certificate-verification)
    - [14.2   Custom CA bundle](https://github.com/jakubroztocil/httpie#custom-ca-bundle)
    - [14.3   Client side SSL certificate](https://github.com/jakubroztocil/httpie#client-side-ssl-certificate)
    - [14.4   SSL version](https://github.com/jakubroztocil/httpie#ssl-version)
- [15   Output options](https://github.com/jakubroztocil/httpie#output-options)
    - [15.1   What parts of the HTTP exchange should be printed](https://github.com/jakubroztocil/httpie#what-parts-of-the-http-exchange-should-be-printed)
    - [15.2   Viewing intermediary requests/responses](https://github.com/jakubroztocil/httpie#viewing-intermediary-requests-responses)
    - [15.3   Conditional body download](https://github.com/jakubroztocil/httpie#conditional-body-download)
- [16   Redirected Input](https://github.com/jakubroztocil/httpie#redirected-input)
    - [16.1   Request data from a filename](https://github.com/jakubroztocil/httpie#request-data-from-a-filename)
- [17   Terminal output](https://github.com/jakubroztocil/httpie#terminal-output)
    - [17.1   Colors and formatting](https://github.com/jakubroztocil/httpie#colors-and-formatting)
    - [17.2   Binary data](https://github.com/jakubroztocil/httpie#binary-data)
- [18   Redirected output](https://github.com/jakubroztocil/httpie#redirected-output)
- [19   Download mode](https://github.com/jakubroztocil/httpie#download-mode)
    - [19.1   Downloaded filename](https://github.com/jakubroztocil/httpie#downloaded-filename)
    - [19.2   Piping while downloading](https://github.com/jakubroztocil/httpie#piping-while-downloading)
    - [19.3   Resuming downloads](https://github.com/jakubroztocil/httpie#resuming-downloads)
    - [19.4   Other notes](https://github.com/jakubroztocil/httpie#other-notes)
- [20   Streamed responses](https://github.com/jakubroztocil/httpie#streamed-responses)
    - [20.1   Disabling buffering](https://github.com/jakubroztocil/httpie#disabling-buffering)
    - [20.2   Examples use cases](https://github.com/jakubroztocil/httpie#examples-use-cases)
- [21   Sessions](https://github.com/jakubroztocil/httpie#sessions)
    - [21.1   Named sessions](https://github.com/jakubroztocil/httpie#named-sessions)
    - [21.2   Anonymous sessions](https://github.com/jakubroztocil/httpie#anonymous-sessions)
    - [21.3   Readonly session](https://github.com/jakubroztocil/httpie#readonly-session)
- [22   Config](https://github.com/jakubroztocil/httpie#config)
    - [22.1   Config file location](https://github.com/jakubroztocil/httpie#config-file-location)
    - [22.2   Configurable options](https://github.com/jakubroztocil/httpie#configurable-options)
        - [22.2.1   `default_options`](https://github.com/jakubroztocil/httpie#default-options)
        - [22.2.2   `__meta__`](https://github.com/jakubroztocil/httpie#meta)
    - [22.3   Un-setting previously specified options](https://github.com/jakubroztocil/httpie#un-setting-previously-specified-options)
- [23   Scripting](https://github.com/jakubroztocil/httpie#scripting)
    - [23.1   Best practices](https://github.com/jakubroztocil/httpie#best-practices)
- [24   Meta](https://github.com/jakubroztocil/httpie#id1)
    - [24.1   Interface design](https://github.com/jakubroztocil/httpie#interface-design)
    - [24.2   User support](https://github.com/jakubroztocil/httpie#user-support)
    - [24.3   Related projects](https://github.com/jakubroztocil/httpie#related-projects)
        - [24.3.1   Dependencies](https://github.com/jakubroztocil/httpie#dependencies)
        - [24.3.2   HTTPie friends](https://github.com/jakubroztocil/httpie#httpie-friends)
        - [24.3.3   Alternatives](https://github.com/jakubroztocil/httpie#alternatives)
    - [24.4   Contributing](https://github.com/jakubroztocil/httpie#contributing)
    - [24.5   Change log](https://github.com/jakubroztocil/httpie#change-log)
    - [24.6   Artwork](https://github.com/jakubroztocil/httpie#artwork)
    - [24.7   Licence](https://github.com/jakubroztocil/httpie#licence)
    - [24.8   Authors](https://github.com/jakubroztocil/httpie#authors)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='491'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2428' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#1main-features)[1   Main features](https://github.com/jakubroztocil/httpie#id2)

- Expressive and intuitive syntax
- Formatted and colorized terminal output
- Built-in JSON support
- Forms and file uploads
- HTTPS, proxies, and authentication
- Arbitrary request data
- Custom headers
- Persistent sessions
- Wget-like downloads
- Linux, macOS and Windows support
- Plugins
- Documentation
- Test coverage

[![httpie.png](../_resources/1f6219a5a07bb6e99aa7afd98d0e67ec.png)](https://raw.githubusercontent.com/jakubroztocil/httpie/master/httpie.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='492'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2445' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#2installation)[2   Installation](https://github.com/jakubroztocil/httpie#id3)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='493'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2447' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#21macos)[2.1   macOS](https://github.com/jakubroztocil/httpie#id4)

On macOS, HTTPie can be installed via [Homebrew](https://brew.sh/)(recommended):

$ brew install httpie
A MacPorts *port* is also available:
$ port install httpie

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='494'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2454' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#22linux)[2.2   Linux](https://github.com/jakubroztocil/httpie#id5)

Most Linux distributions provide a package that can be installed using the system package manager, for example:

# Debian, Ubuntu, etc.$ apt-get install httpie

# Fedora$ dnf install httpie

# CentOS, RHEL, ...$ yum install httpie

# Arch Linux$ pacman -S httpie

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='495'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2461' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#23windows-etc)[2.3   Windows, etc.](https://github.com/jakubroztocil/httpie#id6)

A universal installation method (that works on Windows, Mac OS X, Linux, …, and always provides the latest version) is to use [pip](https://pip.pypa.io/en/stable/installing/):

# Make sure we have an up-to-date version of pip and setuptools:$ pip install --upgrade pip setuptools

$ pip install --upgrade httpie

(If `pip` installation fails for some reason, you can try`easy_install httpie` as a fallback.)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='496'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2466' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#24python-version)[2.4   Python version](https://github.com/jakubroztocil/httpie#id7)

Starting with version 2.0.0 (currently under development) Python 3.6+ is required.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='497'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2469' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#25unstable-version)[2.5   Unstable version](https://github.com/jakubroztocil/httpie#id8)

You can also install the latest unreleased development version directly from the `master` branch on GitHub. It is a work-in-progress of a future stable release so the experience might be not as smooth.

[![](../_resources/1a9cb950d3a48f5062750b7b5bc3f548.png)](https://github.com/jakubroztocil/httpie/actions)

On macOS you can install it with Homebrew:
$ brew install httpie --HEAD
Otherwise with `pip`:

$ pip install --upgrade https://github.com/jakubroztocil/httpie/archive/master.tar.gz

Verify that now we have the[current development version identifier](https://github.com/jakubroztocil/httpie/blob/0af6ae1be444588bbc4747124e073423151178a0/httpie/__init__.py#L5)with the `-dev` suffix, for example:

$ http --version
1.0.0-dev

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='498'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2479' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#3usage)[3   Usage](https://github.com/jakubroztocil/httpie#id9)

Hello World:
$ http httpie.org
Synopsis:
$ http [flags] [METHOD] URL [ITEM [ITEM]]
See also `http --help`.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='499'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2486' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#31examples)[3.1   Examples](https://github.com/jakubroztocil/httpie#id10)

Custom [HTTP method](https://github.com/jakubroztocil/httpie#http-method), [HTTP headers](https://github.com/jakubroztocil/httpie#http-headers) and [JSON](https://github.com/jakubroztocil/httpie#json) data:

$ http PUT example.org X-API-Token:123 name=John
Submitting [forms](https://github.com/jakubroztocil/httpie#forms):
$ http -f POST example.org hello=World

See the request that is being sent using one of the [output options](https://github.com/jakubroztocil/httpie#output-options):

$ http -v example.org

Use [Github API](https://developer.github.com/v3/issues/comments/#create-a-comment) to post a comment on an[issue](https://github.com/jakubroztocil/httpie/issues/83)with [authentication](https://github.com/jakubroztocil/httpie#authentication):

$ http -a USERNAME POST https://api.github.com/repos/jakubroztocil/httpie/issues/83/comments body='HTTPie is awesome! :heart:'

Upload a file using [redirected input](https://github.com/jakubroztocil/httpie#redirected-input):

$ http example.org < file.json

Download a file and save it via [redirected output](https://github.com/jakubroztocil/httpie#redirected-output):

$ http example.org/file > file
Download a file `wget` style:
$ http --download example.org/file

Use named [sessions](https://github.com/jakubroztocil/httpie#sessions) to make certain aspects or the communication persistent between requests to the same host:

$ http --session=logged-in -a username:password httpbin.org/get API-Key:123
$ http --session=logged-in httpbin.org/headers
Set a custom `Host` header to work around missing DNS records:
$ http localhost:8000 Host:example.com

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='500'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2506' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#4http-method)[4   HTTP method](https://github.com/jakubroztocil/httpie#id11)

The name of the HTTP method comes right before the URL argument:
$ http DELETE example.org/todos/7
Which looks similar to the actual `Request-Line` that is sent:
DELETE /todos/7 HTTP/1.1

When the `METHOD` argument is omitted from the command, HTTPie defaults to either `GET` (with no request data) or `POST` (with request data).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='501'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2513' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#5request-url)[5   Request URL](https://github.com/jakubroztocil/httpie#id12)

The only information HTTPie needs to perform a request is a URL. The default scheme is, somewhat unsurprisingly, `http://`, and can be omitted from the argument – `http example.org` works just fine.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='502'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2516' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#51querystring-parameters)[5.1   Querystring parameters](https://github.com/jakubroztocil/httpie#id13)

If you find yourself manually constructing URLs with querystring parameters on the terminal, you may appreciate the `param==value` syntax for appending URL parameters. With that, you don't have to worry about escaping the `&`separators for your shell. Also, special characters in parameter values, will also automatically escaped (HTTPie otherwise expects the URL to be already escaped). To search for `HTTPie logo` on Google Images you could use this command:

$ http www.google.com search=='HTTPie logo' tbm==isch
GET /?search=HTTPie+logo&tbm=isch HTTP/1.1

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='503'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2521' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#52url-shortcuts-for-localhost)[5.2   URL shortcuts for `localhost`](https://github.com/jakubroztocil/httpie#id14)

Additionally, curl-like shorthand for localhost is supported. This means that, for example `:3000` would expand to `http://localhost:3000`If the port is omitted, then port 80 is assumed.

$ http :/foo
GET /foo HTTP/1.1Host: localhost
$ http :3000/bar
GET /bar HTTP/1.1Host: localhost:3000
$ http :
GET / HTTP/1.1Host: localhost

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='504'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2530' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#53other-default-schemes)[5.3   Other default schemes](https://github.com/jakubroztocil/httpie#id15)

When HTTPie is invoked as `https` then the default scheme is `https://`(`$ https example.org` will make a request to `https://example.org`).

You can also use the `--default-scheme <URL_SCHEME>` option to create shortcuts for other protocols than HTTP (possibly supported via plugins). Example for the [httpie-unixsocket](https://github.com/httpie/httpie-unixsocket) plugin:

# Before$ http http+unix://%2Fvar%2Frun%2Fdocker.sock/info

# Create an alias$ alias http-unix='http --default-scheme="http+unix"'

# Now the scheme can be omitted$ http-unix %2Fvar%2Frun%2Fdocker.sock/info

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='505'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2537' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#6request-items)[6   Request items](https://github.com/jakubroztocil/httpie#id16)

There are a few different *request item* types that provide a convenient mechanism for specifying HTTP headers, simple JSON and form data, files, and URL parameters.

They are key/value pairs specified after the URL. All have in common that they become part of the actual request that is sent and that their type is distinguished only by the separator used:`:`, `=`, `:=`, `==`, `@`, `=@`, and `:=@`. The ones with an`@` expect a file path as value.

Item Type
Description
HTTP Headers[object Object]
Arbitrary HTTP header, e.g. [object Object].
URL parameters[object Object]

Appends the given name/value pair as a query string parameter to the URL. The [object Object] separator is used.

Data Fields[object Object],[object Object]

Request data fields to be serialized as a JSON object (default), or to be form-encoded ([object Object]).

Raw JSON fields[object Object],[object Object]

Useful when sending JSON and one or more fields need to be a [object Object], [object Object], nested [object Object], or an [object Object], e.g.,[object Object] or [object Object](note the quotes).

Form File Fields[object Object]

Only available with [object Object]. For example [object Object]. The presence of a file field results in a [object Object] request.

Note that data fields aren't the only way to specify request data:[Redirected input](https://github.com/jakubroztocil/httpie#redirected-input) is a mechanism for passing arbitrary request data.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='506'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2564' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#61escaping-rules)[6.1   Escaping rules](https://github.com/jakubroztocil/httpie#id17)

You can use `\` to escape characters that shouldn't be used as separators (or parts thereof). For instance, `foo\==bar` will become a data key/value pair (`foo=` and `bar`) instead of a URL parameter.

Often it is necessary to quote the values, e.g. `foo='bar baz'`.

If any of the field names or headers starts with a minus (e.g., `-fieldname`), you need to place all such items after the special token `--` to prevent confusion with `--arguments`:

$ http httpbin.org/post -- -name-starting-with-dash=foo -Unusual-Header:bar

POST /post HTTP/1.1-Unusual-Header: barContent-Type: application/json{ "-name-starting-with-dash": "foo"}

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='507'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2571' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#7json)[7   JSON](https://github.com/jakubroztocil/httpie#id18)

JSON is the *lingua franca* of modern web services and it is also the**implicit content type** HTTPie uses by default.

Simple example:
$ http PUT example.org name=John email=john@example.org

PUT / HTTP/1.1Accept: application/json, */*Accept-Encoding: gzip, deflateContent-Type: application/jsonHost: example.org{ "name": "John", "email": "john@example.org"}

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='508'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2578' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#71default-behaviour)[7.1   Default behaviour](https://github.com/jakubroztocil/httpie#id19)

If your command includes some data [request items](https://github.com/jakubroztocil/httpie#request-items), they are serialized as a JSON object by default. HTTPie also automatically sets the following headers, both of which can be overwritten:

[object Object]
[object Object]
[object Object]
[object Object]

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='509'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2589' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#72explicit-json)[7.2   Explicit JSON](https://github.com/jakubroztocil/httpie#id20)

You can use `--json, -j` to explicitly set `Accept`to `application/json` regardless of whether you are sending data (it's a shortcut for setting the header via the usual header notation:`http url Accept:'application/json, */*'`). Additionally, HTTPie will try to detect JSON responses even when the`Content-Type` is incorrectly `text/plain` or unknown.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='510'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2592' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#73non-string-json-fields)[7.3   Non-string JSON fields](https://github.com/jakubroztocil/httpie#id21)

Non-string fields use the `:=` separator, which allows you to embed raw JSON into the resulting object. Text and raw JSON files can also be embedded into fields using `=@` and `:=@`:

$ http PUT api.example.com/person/1 \
name=John \

age:=29 married:=false hobbies:='["http", "pies"]'  \   # Raw JSON description=@about-john.txt \   # Embed text file bookmarks:=@bookmarks.json # Embed JSON file

PUT /person/1 HTTP/1.1Accept: application/json, */*Content-Type: application/jsonHost: api.example.com{ "age": 29, "hobbies": [ "http", "pies" ], "description": "John is a nice guy who likes pies.", "married": false, "name": "John", "bookmarks": { "HTTPie": "https://httpie.org",

}
}

Please note that with this syntax the command gets unwieldy when sending complex data. In that case it's always better to use [redirected input](https://github.com/jakubroztocil/httpie#redirected-input):

$ http POST api.example.com/person/1 < person.json

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='511'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2601' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#8forms)[8   Forms](https://github.com/jakubroztocil/httpie#id22)

Submitting forms is very similar to sending [JSON](https://github.com/jakubroztocil/httpie#json) requests. Often the only difference is in adding the `--form, -f` option, which ensures that data fields are serialized as, and `Content-Type` is set to,`application/x-www-form-urlencoded; charset=utf-8`. It is possible to make form data the implicit content type instead of JSON via the [config](https://github.com/jakubroztocil/httpie#config) file.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='512'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2604' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#81regular-forms)[8.1   Regular forms](https://github.com/jakubroztocil/httpie#id23)

$ http --form POST api.example.org/person/1 name='John Smith'

POST /person/1 HTTP/1.1Content-Type: application/x-www-form-urlencoded; charset=utf-8name=John+Smith

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='513'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2608' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#82file-upload-forms)[8.2   File upload forms](https://github.com/jakubroztocil/httpie#id24)

If one or more file fields is present, the serialization and content type is`multipart/form-data`:

$ http -f POST example.com/jobs name='John Smith' cv@~/Documents/cv.pdf
The request above is the same as if the following HTML form were submitted:

<form  enctype="multipart/form-data"  method="post"  action="http://example.com/jobs">

<input  type="text"  name="name" />
<input  type="file"  name="cv" />
</form>

Note that `@` is used to simulate a file upload form field, whereas`=@` just embeds the file content as a regular text field value.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='514'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2615' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#9http-headers)[9   HTTP headers](https://github.com/jakubroztocil/httpie#id25)

To set custom headers you can use the `Header:Value` notation:
$ http example.org User-Agent:Bacon/1.0 'Cookie:valued-visitor=yes;foo=bar' \
X-Foo:Bar Referer:https://httpie.org/

GET / HTTP/1.1Accept: */*Accept-Encoding: gzip, deflateCookie: valued-visitor=yes;foo=barHost: example.orgReferer: https://httpie.org/User-Agent: Bacon/1.0X-Foo: Bar

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='515'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2620' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#91default-request-headers)[9.1   Default request headers](https://github.com/jakubroztocil/httpie#id26)

There are a couple of default headers that HTTPie sets:

GET / HTTP/1.1Accept: */*Accept-Encoding: gzip, deflateUser-Agent: HTTPie/<version>Host: <taken-from-URL>

Any of these except `Host` can be overwritten and some of them unset.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='516'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2625' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#92empty-headers-and-header-un-setting)[9.2   Empty headers and header un-setting](https://github.com/jakubroztocil/httpie#id27)

To unset a previously specified header (such a one of the default headers), use `Header:`:

$ http httpbin.org/headers Accept: User-Agent:
To send a header with an empty value, use `Header;`:
$ http httpbin.org/headers 'Header;'

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='517'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2631' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#93limiting-response-headers)[9.3   Limiting response headers](https://github.com/jakubroztocil/httpie#id28)

The `--max-headers=n` options allows you to control the number of headers HTTPie reads before giving up (the default `0`, i.e., there’s no limit).

$ http --max-headers=100 httpbin.org/get

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='518'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2635' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#10cookies)[10   Cookies](https://github.com/jakubroztocil/httpie#id29)

HTTP clients send cookies to the server as regular [HTTP headers](https://github.com/jakubroztocil/httpie#http-headers). That means, HTTPie does not offer any special syntax for specifying cookies — the usual`Header:Value` notation is used:

Send a single cookie:
$ http example.org Cookie:sessionid=foo

GET / HTTP/1.1Accept: */*Accept-Encoding: gzip, deflateConnection: keep-aliveCookie: sessionid=fooHost: example.orgUser-Agent: HTTPie/0.9.9

Send multiple cookies (note the header is quoted to prevent the shell from interpreting the `;`):

$ http example.org 'Cookie:sessionid=foo;another-cookie=bar'

GET / HTTP/1.1Accept: */*Accept-Encoding: gzip, deflateConnection: keep-aliveCookie: sessionid=foo;another-cookie=barHost: example.orgUser-Agent: HTTPie/0.9.9

If you often deal with cookies in your requests, then chances are you'd appreciate the [sessions](https://github.com/jakubroztocil/httpie#sessions) feature.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='519'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2645' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#11authentication)[11   Authentication](https://github.com/jakubroztocil/httpie#id30)

The currently supported authentication schemes are Basic and Digest (see [auth plugins](https://github.com/jakubroztocil/httpie#auth-plugins) for more). There are two flags that control authentication:

[object Object]

Pass a [object Object] pair as the argument. Or, if you only specify a username ([object Object]), you'll be prompted for the password before the request is sent. To send an empty password, pass [object Object]. The [object Object] URL syntax is supported as well (but credentials passed via [object Object]have higher priority).

[object Object]

Specify the auth mechanism. Possible values are[object Object] and [object Object]. The default value is[object Object] so it can often be omitted.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='520'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2656' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#111basic-auth)[11.1   Basic auth](https://github.com/jakubroztocil/httpie#id31)

$ http -a username:password example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='521'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2659' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#112digest-auth)[11.2   Digest auth](https://github.com/jakubroztocil/httpie#id32)

$ http -A digest -a username:password example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='522'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2662' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#113password-prompt)[11.3   Password prompt](https://github.com/jakubroztocil/httpie#id33)

$ http -a username example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='523'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2665' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#114netrc)[11.4   `.netrc`](https://github.com/jakubroztocil/httpie#id34)

Authentication information from your `~/.netrc`file is by default honored as well.

For example:
$ cat ~/.netrc
machine httpbin.org
login httpie
password test
$ http httpbin.org/basic-auth/httpie/test
HTTP/1.1 200 OK
[...]
This can be disable with the `--ignore-netrc` option:
$ http --ignore-netrc httpbin.org/basic-auth/httpie/test
HTTP/1.1 401 UNAUTHORIZED
[...]

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='524'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2673' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#115auth-plugins)[11.5   Auth plugins](https://github.com/jakubroztocil/httpie#id35)

Additional authentication mechanism can be installed as plugins. They can be found on the [Python Package Index](https://pypi.python.org/pypi?%3Aaction=search&term=httpie&submit=search). Here's a few picks:

- [httpie-api-auth](https://github.com/pd/httpie-api-auth): ApiAuth
- [httpie-aws-auth](https://github.com/httpie/httpie-aws-auth): AWS / Amazon S3
- [httpie-edgegrid](https://github.com/akamai-open/httpie-edgegrid): EdgeGrid
- [httpie-hmac-auth](https://github.com/guardian/httpie-hmac-auth): HMAC
- [httpie-jwt-auth](https://github.com/teracyhq/httpie-jwt-auth): JWTAuth (JSON Web Tokens)
- [httpie-negotiate](https://github.com/ndzou/httpie-negotiate): SPNEGO (GSS Negotiate)
- [httpie-ntlm](https://github.com/httpie/httpie-ntlm): NTLM (NT LAN Manager)
- [httpie-oauth](https://github.com/httpie/httpie-oauth): OAuth
- [requests-hawk](https://github.com/mozilla-services/requests-hawk): Hawk

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='525'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2686' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#12http-redirects)[12   HTTP redirects](https://github.com/jakubroztocil/httpie#id36)

By default, HTTP redirects are not followed and only the first response is shown:

$ http httpbin.org/redirect/3

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='526'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2690' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#121follow-location)[12.1   Follow `Location`](https://github.com/jakubroztocil/httpie#id37)

To instruct HTTPie to follow the `Location` header of `30x` responses and show the final response instead, use the `--follow, -F` option:

$ http --follow httpbin.org/redirect/3

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='527'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2694' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#122showing-intermediary-redirect-responses)[12.2   Showing intermediary redirect responses](https://github.com/jakubroztocil/httpie#id38)

If you additionally wish to see the intermediary requests/responses, then use the `--all` option as well:

$ http --follow --all httpbin.org/redirect/3

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='528'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2698' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#123limiting-maximum-redirects-followed)[12.3   Limiting maximum redirects followed](https://github.com/jakubroztocil/httpie#id39)

To change the default limit of maximum `30` redirects, use the`--max-redirects=<limit>` option:

$ http --follow --all --max-redirects=5 httpbin.org/redirect/3

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='529'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2702' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#13proxies)[13   Proxies](https://github.com/jakubroztocil/httpie#id40)

You can specify proxies to be used through the `--proxy` argument for each protocol (which is included in the value in case of redirects across protocols):

$ http --proxy=http:http://10.10.1.10:3128 --proxy=https:https://10.10.1.10:1080 example.org

With Basic authentication:
$ http --proxy=http:http://user:pass@10.10.1.10:3128 example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='530'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2708' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#131environment-variables)[13.1   Environment variables](https://github.com/jakubroztocil/httpie#id41)

You can also configure proxies by environment variables `ALL_PROXY`,`HTTP_PROXY` and `HTTPS_PROXY`, and the underlying Requests library will pick them up as well. If you want to disable proxies configured through the environment variables for certain hosts, you can specify them in `NO_PROXY`.

In your `~/.bash_profile`:

export HTTP_PROXY=http://10.10.1.10:3128export HTTPS_PROXY=https://10.10.1.10:1080export NO_PROXY=localhost,example.com

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='531'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2713' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#132socks)[13.2   SOCKS](https://github.com/jakubroztocil/httpie#id42)

Homebrew-installed HTTPie comes with SOCKS proxy support out of the box. To enable SOCKS proxy support for non-Homebrew installations, you'll might need to install `requests[socks]` manually using `pip`:

$ pip install -U requests[socks]

Usage is the same as for other types of [proxies](https://github.com/jakubroztocil/httpie#proxies):

$ http --proxy=http:socks5://user:pass@host:port --proxy=https:socks5://user:pass@host:port example.org

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='532'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2719' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#14https)[14   HTTPS](https://github.com/jakubroztocil/httpie#id43)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='533'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2721' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#141server-ssl-certificate-verification)[14.1   Server SSL certificate verification](https://github.com/jakubroztocil/httpie#id44)

To skip the host's SSL certificate verification, you can pass `--verify=no`(default is `yes`):

$ http --verify=no https://example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='534'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2725' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#142custom-ca-bundle)[14.2   Custom CA bundle](https://github.com/jakubroztocil/httpie#id45)

You can also use `--verify=<CA_BUNDLE_PATH>` to set a custom CA bundle path:
$ http --verify=/ssl/custom_ca_bundle https://example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='535'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2729' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#143client-side-ssl-certificate)[14.3   Client side SSL certificate](https://github.com/jakubroztocil/httpie#id46)

To use a client side certificate for the SSL communication, you can pass the path of the cert file with `--cert`:

$ http --cert=client.pem https://example.org

If the private key is not contained in the cert file you may pass the path of the key file with `--cert-key`:

$ http --cert=client.crt --cert-key=client.key https://example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='536'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2735' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#144ssl-version)[14.4   SSL version](https://github.com/jakubroztocil/httpie#id47)

Use the `--ssl=<PROTOCOL>` to specify the desired protocol version to use. This will default to SSL v2.3 which will negotiate the highest protocol that both the server and your installation of OpenSSL support. The available protocols are `ssl2.3`, `ssl3`, `tls1`, `tls1.1`, `tls1.2`, `tls1.3`. (The actually available set of protocols may vary depending on your OpenSSL installation.)

# Specify the vulnerable SSL v3 protocol to talk to an outdated server:$ http --ssl=ssl3 https://vulnerable.example.org

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='537'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2739' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#15output-options)[15   Output options](https://github.com/jakubroztocil/httpie#id48)

By default, HTTPie only outputs the final response and the whole response message is printed (headers as well as the body). You can control what should be printed via several options:

[object Object]
Only the response headers are printed.
[object Object]
Only the response body is printed.
[object Object]

Print the whole HTTP exchange (request and response). This option also enables [object Object] (see below).

[object Object]
Selects parts of the HTTP exchange.

`--verbose` can often be useful for debugging the request and generating documentation examples:

$ http --verbose PUT httpbin.org/put hello=world
PUT /put HTTP/1.1
Accept: application/json, */*Accept-Encoding: gzip, deflate
Content-Type: application/json
Host: httpbin.org
User-Agent: HTTPie/0.2.7dev
{ "hello": "world"}
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 477
Content-Type: application/json
Date: Sun, 05 Aug 2012 00:25:23 GMT
Server: gunicorn/0.13.4
{
[…]
}

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='538'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2758' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#151what-parts-of-the-http-exchange-should-be-printed)[15.1   What parts of the HTTP exchange should be printed](https://github.com/jakubroztocil/httpie#id49)

All the other [output options](https://github.com/jakubroztocil/httpie#output-options) are under the hood just shortcuts for the more powerful `--print, -p`. It accepts a string of characters each of which represents a specific part of the HTTP exchange:

Character
Stands for
[object Object]
request headers
[object Object]
request body
[object Object]
response headers
[object Object]
response body
Print request and response headers:
$ http --print=Hh PUT httpbin.org/put hello=world

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='539'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2781' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#152viewing-intermediary-requestsresponses)[15.2   Viewing intermediary requests/responses](https://github.com/jakubroztocil/httpie#id50)

To see all the HTTP communication, i.e. the final request/response as well as any possible intermediary requests/responses, use the `--all`option. The intermediary HTTP communication include followed redirects (with `--follow`), the first unauthorized request when HTTP digest authentication is used (`--auth=digest`), etc.

# Include all responses that lead to the final one:$ http --all --follow httpbin.org/redirect/3

The intermediary requests/response are by default formatted according to`--print, -p` (and its shortcuts described above). If you'd like to change that, use the `--history-print, -P` option. It takes the same arguments as `--print, -p` but applies to the intermediary requests only.

# Print the intermediary requests/responses differently than the final one:$ http -A digest -a foo:bar --all -p Hh -P H httpbin.org/digest-auth/auth/foo/bar

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='540'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2787' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#153conditional-body-download)[15.3   Conditional body download](https://github.com/jakubroztocil/httpie#id51)

As an optimization, the response body is downloaded from the server only if it's part of the output. This is similar to performing a `HEAD`request, except that it applies to any HTTP method you use.

Let's say that there is an API that returns the whole resource when it is updated, but you are only interested in the response headers to see the status code after an update:

$ http --headers PATCH example.org/Really-Huge-Resource name='New Name'

Since we are only printing the HTTP headers here, the connection to the server is closed as soon as all the response headers have been received. Therefore, bandwidth and time isn't wasted downloading the body which you don't care about. The response headers are downloaded always, even if they are not part of the output

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='541'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2793' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#16redirected-input)[16   Redirected Input](https://github.com/jakubroztocil/httpie#id52)

The universal method for passing request data is through redirected `stdin`(standard input)—piping. Such data is buffered and then with no further processing used as the request body. There are multiple useful ways to use piping:

Redirect from a file:
$ http PUT example.com/person/1 X-API-Token:123 < person.json
Or the output of another program:

$ grep '401 Unauthorized' /var/log/httpd/error_log | http POST example.org/intruders

You can use `echo` for simple data:
$ echo  '{"name": "John"}'  | http PATCH example.com/person/1 X-API-Token:123
You can also use a Bash *here string*:
$ http example.com/ <<<'{"name": "John"}'
You can even pipe web services together using HTTPie:

$ http GET https://api.github.com/repos/jakubroztocil/httpie | http POST httpbin.org/post

You can use `cat` to enter multiline data on the terminal:
$ cat | http POST example.com<paste>^D
$ cat | http POST example.com/todos Content-Type:text/plain

- buy milk
- call parents

^D
On OS X, you can send the contents of the clipboard with `pbpaste`:
$ pbpaste | http PUT example.com

Passing data through `stdin` cannot be combined with data fields specified on the command line:

$ echo  'data'  | http POST example.org more=data # This is invalid

To prevent HTTPie from reading `stdin` data you can use the`--ignore-stdin` option.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='542'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2815' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#161request-data-from-a-filename)[16.1   Request data from a filename](https://github.com/jakubroztocil/httpie#id53)

An alternative to redirected `stdin` is specifying a filename (as`@/path/to/file`) whose content is used as if it came from `stdin`.

It has the advantage that the `Content-Type`header is automatically set to the appropriate value based on the filename extension. For example, the following request sends the verbatim contents of that XML file with `Content-Type: application/xml`:

$ http PUT httpbin.org/put @/data/file.xml

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='543'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2820' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#17terminal-output)[17   Terminal output](https://github.com/jakubroztocil/httpie#id54)

HTTPie does several things by default in order to make its terminal output easy to read.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='544'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2823' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#171colors-and-formatting)[17.1   Colors and formatting](https://github.com/jakubroztocil/httpie#id55)

Syntax highlighting is applied to HTTP headers and bodies (where it makes sense). You can choose your preferred color scheme via the `--style` option if you don't like the default one (see `$ http --help` for the possible values).

Also, the following formatting is applied:

- HTTP headers are sorted by name.
- JSON data is indented, sorted by keys, and unicode escapes are converted to the characters they represent.

One of these options can be used to control output processing:
[object Object]
Apply both colors and formatting. Default for terminal output.
[object Object]
Apply colors.
[object Object]
Apply formatting.
[object Object]
Disables output processing. Default for redirected output.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='545'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2845' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#172binary-data)[17.2   Binary data](https://github.com/jakubroztocil/httpie#id56)

Binary data is suppressed for terminal output, which makes it safe to perform requests to URLs that send back binary data. Binary data is suppressed also in redirected, but prettified output. The connection is closed as soon as we know that the response body is binary,

$ http example.org/Movie.mov
You will nearly instantly see something like this:

HTTP/1.1  200 OKAccept-Ranges: bytesContent-Encoding: gzipContent-Type: video/quicktimeTransfer-Encoding: chunked+-----------------------------------------+

| NOTE: binary data not shown in terminal |

+-----------------------------------------+

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='546'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2851' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#18redirected-output)[18   Redirected output](https://github.com/jakubroztocil/httpie#id57)

HTTPie uses a different set of defaults for redirected output than for[terminal output](https://github.com/jakubroztocil/httpie#terminal-output). The differences being:

- Formatting and colors aren't applied (unless `--pretty` is specified).
- Only the response body is printed (unless one of the [output options](https://github.com/jakubroztocil/httpie#output-options) is set).
- Also, binary data isn't suppressed.

The reason is to make piping HTTPie's output to another programs and downloading files work with no extra flags. Most of the time, only the raw response body is of an interest when the output is redirected.

Download a file:
$ http example.org/Movie.mov > Movie.mov
Download an image of Octocat, resize it using ImageMagick, upload it elsewhere:

$ http octodex.github.com/images/original.jpg | convert - -resize 25% - | http example.org/Octocats

Force colorizing and formatting, and show both the request and the response in`less` pager:

$ http --pretty=all --verbose example.org | less -R

The `-R` flag tells `less` to interpret color escape sequences included HTTPie`s output.

You can create a shortcut for invoking HTTPie with colorized and paged output by adding the following to your `~/.bash_profile`:

function  httpless { # `httpless example.org' http --pretty=all --print=hb "$@"  | less -R;}

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='547'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2868' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#19download-mode)[19   Download mode](https://github.com/jakubroztocil/httpie#id58)

HTTPie features a download mode in which it acts similarly to `wget`.

When enabled using the `--download, -d` flag, response headers are printed to the terminal (`stderr`), and a progress bar is shown while the response body is being saved to a file.

$ http --download https://github.com/jakubroztocil/httpie/archive/master.tar.gz

HTTP/1.1  200 OKContent-Disposition: attachment; filename=httpie-master.tar.gzContent-Length: 257336Content-Type: application/x-gzipDownloading 251.30 kB to "httpie-master.tar.gz"Done. 251.30 kB in 2.73862s (91.76 kB/s)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='548'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2874' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#191downloaded-filename)[19.1   Downloaded filename](https://github.com/jakubroztocil/httpie#id59)

There are three mutually exclusive ways through which HTTPie determines the output filename (with decreasing priority):

1. You can explicitly provide it via `--output, -o`. The file gets overwritten if it already exists (or appended to with `--continue, -c`).

2. The server may specify the filename in the optional `Content-Disposition`response header. Any leading dots are stripped from a server-provided filename.

3. The last resort HTTPie uses is to generate the filename from a combination of the request URL and the response `Content-Type`. The initial URL is always used as the basis for the generated filename — even if there has been one or more redirects.

To prevent data loss by overwriting, HTTPie adds a unique numerical suffix to the filename when necessary (unless specified with `--output, -o`).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='549'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2882' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#192piping-while-downloading)[19.2   Piping while downloading](https://github.com/jakubroztocil/httpie#id60)

You can also redirect the response body to another program while the response headers and progress are still shown in the terminal:

$ http -d https://github.com/jakubroztocil/httpie/archive/master.tar.gz | tar zxf -

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='550'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2886' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#193resuming-downloads)[19.3   Resuming downloads](https://github.com/jakubroztocil/httpie#id61)

If `--output, -o` is specified, you can resume a partial download using the`--continue, -c` option. This only works with servers that support`Range` requests and `206 Partial Content` responses. If the server doesn't support that, the whole file will simply be downloaded:

$ http -dco file.zip example.org/file

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='551'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2890' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#194other-notes)[19.4   Other notes](https://github.com/jakubroztocil/httpie#id62)

- The `--download` option only changes how the response body is treated.
- You can still set custom headers, use sessions, `--verbose, -v`, etc.
- `--download` always implies `--follow` (redirects are followed).
- HTTPie exits with status code `1` (error) if the body hasn't been fully downloaded.
- `Accept-Encoding` cannot be set with `--download`.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='552'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2898' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#20streamed-responses)[20   Streamed responses](https://github.com/jakubroztocil/httpie#id63)

Responses are downloaded and printed in chunks which allows for streaming and large file downloads without using too much memory. However, when[colors and formatting](https://github.com/jakubroztocil/httpie#colors-and-formatting) is applied, the whole response is buffered and only then processed at once.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='553'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2901' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#201disabling-buffering)[20.1   Disabling buffering](https://github.com/jakubroztocil/httpie#id64)

You can use the `--stream, -S` flag to make two things happen:

1. The output is flushed in much smaller chunks without any buffering, which makes HTTPie behave kind of like `tail -f` for URLs.

2. Streaming becomes enabled even when the output is prettified: It will be applied to each line of the response and flushed immediately. This makes it possible to have a nice output for long-lived requests, such as one to the Twitter streaming API.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='554'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2907' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#202examples-use-cases)[20.2   Examples use cases](https://github.com/jakubroztocil/httpie#id65)

Prettified streamed response:

$ http --stream -f -a YOUR-TWITTER-NAME https://stream.twitter.com/1/statuses/filter.json track='Justin Bieber'

Streamed output by small chunks alá `tail -f`:

# Send each new tweet (JSON object) mentioning "Apple" to another# server as soon as it arrives from the Twitter streaming API:$ http --stream -f -a YOUR-TWITTER-NAME https://stream.twitter.com/1/statuses/filter.json track=Apple \|  while  read tweet;  do  echo  "$tweet"  | http POST example.org/tweets ;  done

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='555'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2913' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#21sessions)[21   Sessions](https://github.com/jakubroztocil/httpie#id66)

By default, every request HTTPie makes is completely independent of any previous ones to the same host.

However, HTTPie also supports persistent sessions via the `--session=SESSION_NAME_OR_PATH` option. In a session, custom [HTTP headers](https://github.com/jakubroztocil/httpie#http-headers) (except for the ones starting with `Content-` or `If-`),[authentication](https://github.com/jakubroztocil/httpie#authentication), and [cookies](https://github.com/jakubroztocil/httpie#cookies)(manually specified or sent by the server) persist between requests to the same host.

# Create a new session$ http --session=/tmp/session.json example.org API-Token:123# Re-use an existing session — API-Token will be set:$ http --session=/tmp/session.json example.org

All session data, including credentials, cookie data, and custom headers are stored in plain text. That means session files can also be created and edited manually in a text editor—they are regular JSON. It also means that they can be read by anyone who has access to the session file.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='556'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2919' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#211named-sessions)[21.1   Named sessions](https://github.com/jakubroztocil/httpie#id67)

You can create one or more named session per host. For example, this is how you can create a new session named `user1` for `example.org`:

$ http --session=user1 -a user1:password example.org X-Foo:Bar

From now on, you can refer to the session by its name. When you choose to use the session again, any previously specified authentication or HTTP headers will automatically be set:

$ http --session=user1 example.org
To create or reuse a different session, simple specify a different name:
$ http --session=user2 -a user2:password example.org X-Bar:Foo

Named sessions' data is stored in JSON files in the directory`~/.httpie/sessions/<host>/<name>.json`(`%APPDATA%\httpie\sessions\<host>\<name>.json` on Windows).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='557'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2928' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#212anonymous-sessions)[21.2   Anonymous sessions](https://github.com/jakubroztocil/httpie#id68)

Instead of a name, you can also directly specify a path to a session file. This allows for sessions to be re-used across multiple hosts:

$ http --session=/tmp/session.json example.org
$ http --session=/tmp/session.json admin.example.org
$ http --session=~/.httpie/sessions/another.example.org/test.json example.org
$ http --session-read-only=/tmp/session.json example.org

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='558'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2932' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#213readonly-session)[21.3   Readonly session](https://github.com/jakubroztocil/httpie#id69)

To use an existing session file without updating it from the request/response exchange once it is created, specify the session name via`--session-read-only=SESSION_NAME_OR_PATH` instead.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='559'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2935' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#22config)[22   Config](https://github.com/jakubroztocil/httpie#id70)

HTTPie uses a simple JSON config file.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='560'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2938' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#221config-file-location)[22.1   Config file location](https://github.com/jakubroztocil/httpie#id71)

The default location of the configuration file is `~/.httpie/config.json`(or `%APPDATA%\httpie\config.json` on Windows). The config directory location can be changed by setting the `HTTPIE_CONFIG_DIR`environment variable. To view the exact location run `http --debug`.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='561'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2941' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#222configurable-options)[22.2   Configurable options](https://github.com/jakubroztocil/httpie#id72)

The JSON file contains an object with the following keys:

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='562'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2944' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#2221default_options)[22.2.1   `default_options`](https://github.com/jakubroztocil/httpie#id73)

An `Array` (by default empty) of default options that should be applied to every invocation of HTTPie.

For instance, you can use this option to change the default style and output options: `"default_options": ["--style=fruity", "--body"]` Another useful default option could be `"--session=default"` to make HTTPie always use [sessions](https://github.com/jakubroztocil/httpie#sessions) (one named `default` will automatically be used). Or you could change the implicit request content type from JSON to form by adding `--form` to the list.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='563'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2948' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#2222__meta__)[22.2.2   `__meta__`](https://github.com/jakubroztocil/httpie#id74)

HTTPie automatically stores some of its metadata here. Please do not change.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='564'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2951' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#223un-setting-previously-specified-options)[22.3   Un-setting previously specified options](https://github.com/jakubroztocil/httpie#id75)

Default options from the config file, or specified any other way, can be unset for a particular invocation via `--no-OPTION` arguments passed on the command line (e.g., `--no-style` or `--no-session`).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='565'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2954' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#23scripting)[23   Scripting](https://github.com/jakubroztocil/httpie#id76)

When using HTTPie from shell scripts, it can be handy to set the`--check-status` flag. It instructs HTTPie to exit with an error if the HTTP status is one of `3xx`, `4xx`, or `5xx`. The exit status will be `3` (unless `--follow` is set), `4`, or `5`, respectively.

#!/bin/bashif http --check-status --ignore-stdin --timeout=2.5 HEAD example.org/health &> /dev/null;  then  echo  'OK!'else  case  $?  in 2) echo  'Request timed out!' ;;

3) echo  'Unexpected HTTP 3xx Redirection!' ;;
4) echo  'HTTP 4xx Client Error!' ;;
5) echo  'HTTP 5xx Server Error!' ;;

6) echo  'Exceeded --max-redirects=<n> redirects!' ;; *) echo  'Other Error!' ;; esacfi

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='566'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2958' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#231best-practices)[23.1   Best practices](https://github.com/jakubroztocil/httpie#id77)

The default behaviour of automatically reading `stdin` is typically not desirable during non-interactive invocations. You most likely want to use the `--ignore-stdin` option to disable it.

It is a common gotcha that without this option HTTPie seemingly hangs. What happens is that when HTTPie is invoked for example from a cron job,`stdin` is not connected to a terminal. Therefore, rules for [redirected input](https://github.com/jakubroztocil/httpie#redirected-input) apply, i.e., HTTPie starts to read it expecting that the request body will be passed through. And since there's no data nor `EOF`, it will be stuck. So unless you're piping some data to HTTPie, this flag should be used in scripts.

Also, it might be good to set a connection `--timeout` limit to prevent your program from hanging if the server never responds.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='567'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2963' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#24meta)[24   Meta](https://github.com/jakubroztocil/httpie#id78)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='568'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2965' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#241interface-design)[24.1   Interface design](https://github.com/jakubroztocil/httpie#id79)

The syntax of the command arguments closely corresponds to the actual HTTP requests sent over the wire. It has the advantage that it's easy to remember and read. It is often possible to translate an HTTP request to an HTTPie argument list just by inlining the request elements. For example, compare this HTTP request:

POST /collection HTTP/1.1X-API-Key: 123User-Agent: Bacon/1.0Content-Type: application/x-www-form-urlencodedname=value&name2=value2

with the HTTPie command that sends it:
$ http -f POST example.org/collection \
X-API-Key:123 \
User-Agent:Bacon/1.0 \
name=value \
name2=value2

Notice that both the order of elements and the syntax is very similar, and that only a small portion of the command is used to control HTTPie and doesn't directly correspond to any part of the request (here it's only `-f`asking HTTPie to send a form request).

The two modes, `--pretty=all` (default for terminal) and `--pretty=none`(default for redirected output), allow for both user-friendly interactive use and usage from scripts, where HTTPie serves as a generic HTTP client.

As HTTPie is still under heavy development, the existing command line syntax and some of the `--OPTIONS` may change slightly before HTTPie reaches its final version `1.0`. All changes are recorded in the[change log](https://github.com/jakubroztocil/httpie#change-log).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='569'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2974' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#242user-support)[24.2   User support](https://github.com/jakubroztocil/httpie#id80)

Please use the following support channels:

- [GitHub issues](https://github.com/jkbr/httpie/issues)for bug reports and feature requests.
- [Our Gitter chat room](https://gitter.im/jkbrzt/httpie)to ask questions, discuss features, and for general discussion.
- [StackOverflow](https://stackoverflow.com/)to ask questions (please make sure to use the[httpie](https://stackoverflow.com/questions/tagged/httpie) tag).
- Tweet directly to [@clihttp](https://twitter.com/clihttp).
- You can also tweet directly to [@jakubroztocil](https://twitter.com/jakubroztocil).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='570'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2983' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#243related-projects)[24.3   Related projects](https://github.com/jakubroztocil/httpie#id81)

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='571'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2985' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#2431dependencies)[24.3.1   Dependencies](https://github.com/jakubroztocil/httpie#id82)

Under the hood, HTTPie uses these two amazing libraries:

- [Requests](https://python-requests.org/)— Python HTTP library for humans
- [Pygments](https://pygments.org/)— Python syntax highlighter

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='572'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2991' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#2432httpie-friends)[24.3.2   HTTPie friends](https://github.com/jakubroztocil/httpie#id83)

HTTPie plays exceptionally well with the following tools:

- [jq](https://stedolan.github.io/jq/)— CLI JSON processor that works great in conjunction with HTTPie
- [http-prompt](https://github.com/eliangcs/http-prompt)— interactive shell for HTTPie featuring autocomplete and command syntax highlighting

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='573'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2997' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#2433alternatives)[24.3.3   Alternatives](https://github.com/jakubroztocil/httpie#id84)

- [httpcat](https://github.com/jakubroztocil/httpcat) — a lower-level sister utility of HTTPie for constructing raw HTTP requests on the command line.
- [curl](https://curl.haxx.se/) — a "Swiss knife" command line tool and an exceptional library for transferring data with URLs.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='574'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='3002' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#244contributing)[24.4   Contributing](https://github.com/jakubroztocil/httpie#id85)

See [CONTRIBUTING.rst](https://github.com/jakubroztocil/httpie/blob/master/CONTRIBUTING.rst).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='575'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='3005' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#245change-log)[24.5   Change log](https://github.com/jakubroztocil/httpie#id86)

See [CHANGELOG](https://github.com/jakubroztocil/httpie/blob/master/CHANGELOG.rst).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='576'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='3008' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#246artwork)[24.6   Artwork](https://github.com/jakubroztocil/httpie#id87)

- [Logo](https://github.com/claudiatd/httpie-artwork) by [Cláudia Delgado](https://github.com/claudiatd).
- [Animation](https://raw.githubusercontent.com/jakubroztocil/httpie/master/httpie.gif) by [Allen Smith](https://github.com/loranallensmith) of GitHub.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='577'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='3013' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#247licence)[24.7   Licence](https://github.com/jakubroztocil/httpie#id88)

BSD-3-Clause: [LICENSE](https://github.com/jakubroztocil/httpie/blob/master/LICENSE).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='578'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='3016' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jakubroztocil/httpie#248authors)[24.8   Authors](https://github.com/jakubroztocil/httpie#id89)

[Jakub Roztocil](https://roztocil.co/) ([@jakubroztocil](https://twitter.com/jakubroztocil)) created HTTPie and [these fine people](https://github.com/jakubroztocil/httpie/contributors)have contributed.