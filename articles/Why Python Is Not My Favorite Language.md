Why Python Is Not My Favorite Language

[Last time](https://zenhack.net/2016/12/11/on-python.html) I reflected on my reluctant continued use of the Python programming language, but I didn’t talk about *why* I dislike Python. This post is about that. Let’s get into it.

# Encapsulation?

Python makes it more annoying than it should be to wall things off behind an interface.

Most obviously, there’s no such thing as ‘private’. The convention is to prefix things with an underscore, as a way of saying to the user, “don’t touch.”

It isn’t quite true that this is just a convention, however. For instance, if you put this in `foo.py`:

	# foo.py

	one = 1
	_two = 2

…you get this at the Python interpreter:

	>>> from foo import *
	>>> one
	1
	>>> _two
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name '_two' is not defined

But you can still do:

	>>> import foo
	>>> foo._two
	2

And:

	>>> from foo import _two
	>>> _two
	2

Pydoc is also smart enough to not generate docs for names with a leading underscore.

So this is sane right? It doesn’t *prevent* you from accessing it, but it makes it hard to do so by accident, so we’re good. Right?

Well, let’s talk about inheritance. Suppose some library defines this class:

	class Foo(object):

	    def __init__(self, x):
	        self._bar = x

It has a conceptually-private field called `_bar`. The docs don’t tell you it’s there. So you go ahead and inherit from it, and your subclass defines its own private field:

	class Bar(Foo):

	    def __init__(self, bar):
	        self._bar = bar

Oops. Have fun debugging that.

So, there’s yet another level of willfully not fixing the problem in favor of stupid workarounds. If you put *two* underscores in front of a property, it mangles the name a bit:

	>>> class Foo(object):
	...     def __init__(self, x):
	...         self.__bar = x
	...
	>>> f = Foo(2)
	>>> f.__bar
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'Foo' object has no attribute '__bar'
	>>> f._Foo__bar
	2

That should cover us, right?
…

So I once wrote a library for dealing with pgp/mime emails. It was built on top of a module called `gnupg` that just wrapped GPG. That library exposed a single class called `GPG`, which had methods for `encrypt`,`decrypt`, etc.

I decided to keep the interface to my library pretty simple. I expose a sub-class of `GPG`. And I gave it the same name, since they’re namespaced by module, so why not? Instead of doing:

	from gnupg import GPG

	gpg = GPG()
	gpg.encrypt(...)

You would do:

	from gpgmime import GPG

	gpg = GPG()
	gpg.encrypt_email(...)

It just adds two methods and other than that the entire module interface is identical.

I didn’t actually stumble across this, but think about it: what would have happened if I’d happened to pick a name for a private variable that was the same as one used in the parent class?

As we will see, willfully avoiding real solutions is something of a theme.

# Anything But Lambdas

It’s pretty well known that Guido van Rossum isn’t big on functional programming. Python tries pretty hard to make functional programming painful, to a degree that seems rather extreme, given how simple the fixes for the pain points would be.

Python has lambdas, but they’re seriously hamstrung: They can only be a single expression. No statements. Furthermore, Python has a bunch of built-in language features that are totally obviated by adding a decent syntax for multi-statement lambdas. Examples:

## The `with` statement

Python has this handy-dandy thing called the `with` statement:

	with open('foo.txt') as f:
	    # Do stuff with f
	    ...

	# f is closed when we get here

Any type implementing the so-called context manager interface can be used in a with expression; its `__enter__` method will be called first, then the body of the `with` will be executed, then its `__exit__` method will be called. Typically, `__exit__` is used to clean up some resource. In the above example, the context manager is an open file, and its`__exit__` closes the file.

If you had multi-statement lambdas in the language, you could do something like:

	def with(ctx_mgr, fn):
	    c = ctx_mgr.__enter__()
	    try:
	        fn(c)
	    except Exception as e:
	        if not ctx_mgr.__exit__(type(e), e, sys.last_traceback):
	            raise
	    else:
	        ctx_mgr.__exit__(None, None, None)

And then use it like:

	with(open('foo.txt'), |f|:
	    # Do stuff with f
	    ...
	    )

(I have of course made up the multi-statement-lambda syntax).

`with` is a really useful construct. And there’s no good reason for it to be a core language feature.

## Decorators

`with` is a useful feature that shouldn’t need to be part of the core language (rather, it should be in the standard library). Decorators, on the other hand, are just a band-aid over the lack of multi-statement lambdas.

First let’s describe the feature itself. The Python code:

	@foo
	def bar(baz, quux):
	    ...

Is equivalent to:

	def bar(baz, quux):
	    ...

	bar = foo(bar)

This is *just* a tool to ease the pain of having to give the thing a name before manipulating it as a value. The lambda version of this would just be:

	bar = foo(|baz, quux|:
	    ...
	)

Which is maybe not very obviously a big deal, but it’s a little clearer how sub-optimal this is when looking at some real uses of this. Ruby has a popular web framework called [sinatra](http://www.sinatrarb.com/). Here’s your hello world app:

	require 'sinatra'

	get '/' do
	    'Hello, World!'
	end

The closest analogue in the Python world is Flask. Here’s the code for that:

	from flask import Flask

	app = Flask(__name__)

	@app.route('/'):
	def index():
	    return 'Hello, World!'

Especially once you get a bunch of these going, it starts to feel kinda silly to have to give them names. Go doesn’t encourage functional programming either, but even it doesn’t have this problem:

	http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
	    w.Write([]byte("Hello, World!"))
	})

This doesn’t hands-down ruin the language for me. But it’s frustrating to work with a tool that seems hell-bent on denying me what’s generally considered a no-brainer feature, which nearly every other language out there has, because… why?

# Does Anyone Even Know What A Duck Looks Like?

So duck typing: If it looks like a duck and it quacks like a duck, it’s a duck. Or, as a more concrete example, if it’s got a `next()` method that returns the next element and raises `StopIteration` when you’re done, it’s an iterator. No need to declare the type anywhere, or pass around specific types of objects, as long as they look and quack right, we’re good.

This is fine in theory, but I’ve found all too often that I’m asked to work with interfaces that are never actually defined. You’ve got a parameter that’s supposed to be some kind of bird, but you really haven’t described it in enough detail to be useful. It could be a duck or it could be a flamingo.

Having types based on interfaces is great, but all too often the interface isn’t documented. You could blame this on crappy libraries, claim that it’s independent of the language. But I’ve found that when I*do* fully document an interface, the easiest way to do it is often with the standard class notation:

	class Client(object):

	    def request(self, method, path, query, body):
	        """Make an HTTP request on `path`, relative to the api endpoint.

	        `method` is the HTTP method to use, e.g. 'GET', 'PUT', 'POST', etc.
	        `path` is the path part of the URL relative to the endpoint.
	        `query` is a dictionary whose keys and values are strings.
	                It represents the URL's query string.
	        `body` is the body of the request. This may either be a
	                string, or a readable file-like object.

	        Returns the http response, a `Response` object.
	        """

At which point, if I’m going to have a hard dependency on this library anyway, I may as well use abstract base classes:

	import abc

	class Client(object)

	    __metaclass__ = abc.ABCMeta

	    @abc.abstractmethod
	    def request(self, method, path, query, body):
	        ...

And if I inherit from this and make a typo:

	class MyClient(Client):

	    def reques(self, method, path, query, body):
	        ...

I get an error when I try to create an instance:

	>>> c = MyClient()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: Can't instantiate abstract class MyClient with abstract methods request

So if I’m going to be writing out that whole spec anyway, why not just add the abc stuff and do inheritance for the extra error checking? And now the ducks are gone.

Go’s interface types provide a nice solution for this. But it is all too common in Python to either use nominal types anyway, or pass around mystery poultry.

This brings me to my next grievance:

# My Kingdom For A Type System

I die a little inside every time I see `NameError` or `TypeError` in a server log. Even Javascript can catch undefined variables before runtime (with `use strict`), but not Python.

This is also why I tend to roll my eyes when people who care deeply about Python 3 talk about the fact that it’s more strict in its error checking than Python 2. If you care about sanity checks, Python is the wrong language.

And I *have* stumbled across stupid type errors in production software, out in the field, more times than I care to think about. Much of it has been written in Python.

There are a few things that I really want a type system for:

1. Catching bugs earlier. The earlier the better, and a good type system is your friend. You can debate how far to go with the type safety thing, but if you tell me with a straight face that not catching undefined variables at compile time is reasonable, I will judge you.

2. Refactoring. If I’ve got a type system and I’m faced with needing to clean things up, I can put stuff behind an interface and follow the type errors to find everything that needs updating. Often in dynamic languages, even with a decent test suite, extensive changes can be really difficult.

3. Documentation. There’s a common mis-conception that type systems make code verbose. Firstly, type inference is pretty doable and addresses the problems that give rise to these beliefs. Java and C++ aren’t verbose because they have type systems, they’re verbose (partially) because they have *bad* type systems. Second, in my experience, actually clearly documenting an interface in a language that doesn’t have types ends up being much more verbose than it would otherwise be. You need docstrings regardless, but if the type of the thing says it’s an integer, you don’t have to write “x is an integer” in the docstring too. And now you have a concise, agreed upon notation for that sort of fact.

There’s a project out there called [MyPy](http://mypy-lang.org/), which aims to bring static typing to Python. It’s not horrible, and I think it will improve as time goes on, but I’m less than excited about it right now for two reasons:

Firstly, not a lot of libraries actually have fleshed out types available for them. The default is for everything to be of type “Any,” which means their use for anything will silently be accepted in any context. When this is true of a large number of values floating around in my program, it basically becomes useless.

I tried adapting some of Iron Blogger to use MyPy, but the dynamic sanity checks wouldn’t type-check. In a language with a real static type system this might be a cause for celebration: I can’t even *check* if something horrible has happened, because the type system says it’s not possible. But, when there are all these “Any” values floating around, I’d rather have the dynamic checks.

Second, It really only does nominal typing. This basically means that most idiomatic Python code can’t be given types at all.

Go’s interface types represent a good way to capture “duck typing” while still having some semblance of type safety. OCaml’s object system wouldn’t be a bad place to look either. But right now, Python’s notion of types is all Java/C++.

The first bit may get better with time, but Python isn’t the sort of language that attracts people who care a lot about this stuff. I wouldn’t be surprised if MyPy just stayed a tool with only so-so usage.

The second is an easy enough thing for the developers to change, and I hope they do.

But I’ll be looking elsewhere if I want to write robust software.