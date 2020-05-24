willmcgugan/rich: Rich is a Python library for rich text and beautiful formatting in the terminal.

[![68747470733a2f2f62616467652e667572792e696f2f70792f726963682e737667](../_resources/5f3158708c825622ec43f16d9131b38f.png)](https://badge.fury.io/py/rich)[![68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f726963682e737667](../_resources/2f895ba1d1617c951297e493d4e206c8.png)](https://pypi.org/project/rich/)[![68747470733a2f2f706570792e746563682f62616467652f726963682f6d6f6e7468](../_resources/89169d9c4474ed96e93143fccf9f3f45.png)](https://pepy.tech/project/rich/month)[![68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667](../_resources/93d5d18b4e145f195386c6dec5e2b6a9.png)](https://awesome-python.com/#command-line-interface-development)[![68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f77696c6c6d63677567616e2e7376673f7374796c653d736f6369616c](../_resources/f213f1495b4dda051815772fcbe9f546.png)](https://twitter.com/willmcgugan)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='73'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1108' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#rich)Rich

Rich is a Python library for rendering *rich* text and beautiful formatting to the terminal.

The [Rich API](https://rich.readthedocs.io/en/latest/) makes it easy to add colorful text (up to 16.7 million colors) with styles (bold, italic, underline etc.) to your script or application. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, and tracebacks -- out of the box.

[![features.png](../_resources/ae44b599bf3577c56374c3e76e3e6132.png)](https://github.com/willmcgugan/rich/raw/master/imgs/features.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='74'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1114' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#compatibility)Compatibility

Rich works with Linux, OSX, and Windows. True color / emoji works with new Windows Terminal, classic terminal is limited to 8 colors.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='75'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1117' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#installing)Installing

Install with `pip` or your favorite PyPi package manager.

	pip install rich

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1120' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#rich-print-function)Rich print function

To effortlessly add rich output to your application, you can import the [rich print](https://rich.readthedocs.io/en/latest/introduction.html#quick-start) method, which has the same signature as the builtin Python function. Try this:

from rich import  printprint("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

[![print.png](../_resources/f3b4f3ca58c850d871282731e74d0d11.png)](https://github.com/willmcgugan/rich/raw/master/imgs/print.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='77'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1136' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#using-the-console)Using the Console

For more control over rich terminal content, import and construct a [Console](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console) object.

from rich.console import Console
console = Console()

The Console object has a `print` method which has an intentionally similar interface to the builtin `print` function. Here's an example of use:

console.print("Hello", "World!")

As you might expect, this will print `"Hello World!"` to the terminal. Note that unlike the builtin `print` function, Rich will word-wrap your text to fit within the terminal width.

There are a few ways of adding color and style to your output. You can set a style for the entire output by adding a `style` keyword argument. Here's an example:

console.print("Hello", "World!", style="bold red")
The output will be something like the following:

[![hello_world.png](../_resources/e7cdf06b952367d441729f3a8766dee5.png)](https://github.com/willmcgugan/rich/raw/master/imgs/hello_world.png)

That's fine for styling a line of text at a time. For more finely grained styling, Rich renders a special markup which is similar in syntax to [bbcode](https://en.wikipedia.org/wiki/BBCode). Here's an example:

console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

[![where_there_is_a_will.png](../_resources/cfad135c453b944d834cbbebe93e66e6.png)](https://github.com/willmcgugan/rich/raw/master/imgs/where_there_is_a_will.png)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='78'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1173' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#console-logging)Console logging

The Console object has a `log()` method which has a similar interface to `print()`, but also renders a column for the current time and the file and line which made the call. By default Rich will do syntax highlighting for Python structures and for repr strings. If you log a collection (i.e. a dict or a list) Rich will pretty print it so that it fits in the available space. Here's an example of some of these features.

from rich.console import Console
console = Console()
test_data = [

{"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},

{"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
]def  test_log():
enabled =  False context = { "foo": "bar",
}
movies = ["Deadpool", "Rise of the Skywalker"]
console.log("Hello from", console, "!")
console.log(test_data, log_locals=True)
test_log()
The above produces the following output:

[![log.png](../_resources/3854dd170a7a5c0ea4afb2b2e29a3272.png)](https://github.com/willmcgugan/rich/raw/master/imgs/log.png)

Note the `log_locals` argument, which outputs a table containing the local variables where the log method was called.

The log method could be used for logging to the terminal for long running applications such as servers, but is also a very nice debugging aid.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='79'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1278' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#logging-handler)Logging Handler

You can also use the builtin [Handler class](https://rich.readthedocs.io/en/latest/logging.html) to format and colorize output from Python's logging module. Here's an example of the output:

[![logging.png](../_resources/fa738a29483eecd76b01574fa12262c0.png)](https://github.com/willmcgugan/rich/blob/master/imgs/logging.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='80'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1282' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#emoji)Emoji

To insert an emoji in to console output place the name between two colons. Here's an example:

>>> console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")
Please use this feature wisely.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='81'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1292' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#progress-bars)Progress Bars

Rich can render multiple flicker-free [progress](https://rich.readthedocs.io/en/latest/progress.html) bars to track long-running tasks.

For basic usage, wrap any sequence in the `track` function and iterate over the result. Here's an example:

from rich.progress import trackfor step in track(range(100)):
do_step(step)

It's not much harder to add multiple progress bars. Here's an example taken from the docs:

[![progress.gif](../_resources/4271460b3016f10b6e1ff6b4f4e80d27.gif)](https://github.com/willmcgugan/rich/raw/master/imgs/progress.gif)

The columns may be configured to show any details you want. Built-in columns include percentage complete, file size, file speed, and time remaining. Here's another example showing a download in progress::

[![downloader.gif](../_resources/3a6369cbdc5c01910360b08d5feb3546.gif)](https://github.com/willmcgugan/rich/raw/master/imgs/downloader.gif)

To try this out yourself, see [examples/downloader.py](https://github.com/willmcgugan/rich/blob/master/examples/downloader.py) which can download multiple URLs simultaneously while displaying progress.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='82'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1308' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#markdown)Markdown

Rich can render markdown and does a reasonable job of translating the formatting to the terminal.

To render markdown import the `Markdown` class and construct it with a string containing markdown code. Then print it to the console. Here's an example:

from rich.console import Consolefrom rich.markdown import Markdown
console = Console()with  open("README.md") as readme:
markdown = Markdown(readme.read())
console.print(markdown)
This will produce output something like the following:

[![markdown.png](../_resources/9ad3e92f04ed2388ec6336f67d711db4.png)](https://github.com/willmcgugan/rich/raw/master/imgs/markdown.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='83'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1327' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#syntax-highlighting)Syntax Highlighting

Rich uses the [pygments](https://pygments.org/) library to implement syntax highlighting. Usage is similar to rendering markdown; construct a `Syntax` object and print it to the console. Here's an example:

from rich.console import Consolefrom rich.syntax import Syntax

my_code =  '''def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]: """Iterate and generate a tuple with a flag for first and last value.""" iter_values = iter(values) try: previous_value = next(iter_values) except StopIteration: return first = True for value in iter_values: yield first, False, previous_value first = False previous_value = value yield first, True, previous_value'''syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)

console = Console()
console.print(syntax)
This will produce the following output:

[![syntax.png](../_resources/1db1a4c43d1988f86117a9ca9304bd01.png)](https://github.com/willmcgugan/rich/raw/master/imgs/syntax.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='84'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1368' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#tables)Tables

Rich can render flexible tables with unicode box characters. There is a large variety of formatting options for borders, styles, cell alignment etc. Here's a simple example:

from rich.console import Consolefrom rich.table import Column, Table
console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")

table.add_row( "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,0000", "$375,126,118")

table.add_row( "May 25, 2018", "[red]Solo[/red]: A Star Wars Story", "$275,000,0000", "$393,151,347",

)

table.add_row( "Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$262,000,000", "[bold]$1,332,539,889[/bold]",

)
console.print(table)
This produces the following output:

[![table.png](../_resources/3af1cba63e2b5e1ab2d00d46b6606cca.png)](https://github.com/willmcgugan/rich/raw/master/imgs/table.png)

Note that console markup is rendered in the same was as `print()` and `log()`. In fact, anything that is renderable by Rich may be included in the headers / rows (even other tables).

The `Table` class is smart enough to resize columns to fit the available width of the terminal, wrapping text as required. Here's the same example, with the terminal made smaller than the table above:

[![table2.png](../_resources/777b6a51cb46dec49f500c1ac204f9d7.png)](https://github.com/willmcgugan/rich/raw/master/imgs/table2.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='85'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1457' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/willmcgugan/rich#tracebacks)Tracebacks

Rich can render beautiful tracebacks which are easier to read and show more code than standard Python tracebacks. You can set Rich as the default traceback handler so all uncaught exceptions will be rendered by Rich.

Here's what it looks like on OSX (similar on Linux):

[![traceback.png](../_resources/00108380ac377e65b3bb8d870cabd6ef.png)](https://github.com/willmcgugan/rich/raw/master/imgs/traceback.png)

Here's what it looks like on Windows:

[![traceback_windows.png](../_resources/559524ea1c188f9b9e75cb802ed45401.png)](https://github.com/willmcgugan/rich/raw/master/imgs/traceback_windows.png)

See the [rich traceback](https://rich.readthedocs.io/en/latest/traceback.html) documentation for the details.