> Ultimate Guide to Python Debugging

# Ultimate Guide to Python Debugging
Even if you write clear and readable code, even if you cover your code with tests, even if you are very experienced developer, weird bugs will inevitably appear and you will need to debug them in some way. Lots of people resort to just using bunch of `print` statements to see what's happening in their code. This approach is far from ideal and there are much better ways to find out what's wrong with your code, some of which we will explore in this article.

Logging is a Must
-----------------

If you write application without some sort of logging setup you will eventually come to regret it. Not having any logs from your application can make it very difficult to troubleshoot any bugs. Luckily - in Python - setting up basic logger is very simple:

    import logging
    logging.basicConfig(
        filename='application.log',
        level=logging.WARNING,
        format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    
    logging.error("Some serious error occurred.")
    logging.warning('Function you are using is deprecated.')

This is all you need to start writing logs to file which will look something like this (you can find path to the file using `logging.getLoggerClass().root.handlers[0].baseFilename`):

    [12:52:35] {<stdin>:1} ERROR - Some serious error occurred.
    [12:52:35] {<stdin>:1} WARNING - Function you are using is deprecated.

This setup might seem like it's good enough (and often it is), but having well configured, formatted, readable logs can make your life so much easier. One way to improve and expand the config is to use `.ini` or `.yaml` file that gets read by logger. As an example for what you could do in your config:

    version: 1
    disable_existing_loggers: true
    
    formatters:
      standard:
        format: "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
        datefmt: '%H:%M:%S'
    
    handlers:
      console:  
        class: logging.StreamHandler
        level: DEBUG
        formatter: standard  
        stream: ext://sys.stdout
      file:  
        class: logging.handlers.RotatingFileHandler
        level: WARNING
        formatter: standard  
        filename: /tmp/warnings.log
        maxBytes: 10485760 
        backupCount: 10
        encoding: utf8
    
    root:  
      level: ERROR
      handlers: [console, file]  
    
    loggers:  
      mymodule:  
        level: INFO
        handlers: [file]  
        propagate: no  

Having this kind of extensive config inside you python code would be hard to navigate, edit and maintain. Keeping things in YAML file makes it much easier to setup and tweak multiple loggers with very specific settings like the ones above.

If you are wondering where all these config fields came from, these are documented [here](https://docs.python.org/3.8/library/logging.config.html) and most of them are just _keyword arguments_ as shown in the first example.

So, having the config in the file now, means that we need to load is somehow. The simplest way to do so with YAML files:

    import yaml
    from logging import config
    
    with open("config.yaml", 'rt') as f:
        config_data = yaml.safe_load(f.read())
        config.dictConfig(config_data)

Python logger doesn't actually support YAML files directly, but it supports _dictionary_ configs, which can be easily created from YAML using `yaml.safe_load`. If you are inclined to rather use old `.ini` files, then I just want to point out that using _dictionary_ configs is the recommended approach for new application as per [docs](https://docs.python.org/3/howto/logging.html#configuring-logging). For more examples checkout the [logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html#an-example-dictionary-based-configuration).

Logging Decorators
------------------

Continuing with the previous logging tip, you might get into a situation where you need log calls of some buggy function. Instead of modifying body of said function you could employ logging decorator which would log every function call with specific log level and optional message. Let's look at the decorator:

    from functools import wraps, partial
    import logging
    
    def attach_wrapper(obj, func=None):  
        if func is None:
            return partial(attach_wrapper, obj)
        setattr(obj, func.__name__, func)
        return func
    
    def log(level, message):  
        def decorate(func):
            logger = logging.getLogger(func.__module__)  
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            log_message = f"{func.__name__} - {message}"
    
            @wraps(func)
            def wrapper(*args, **kwargs):  
                logger.log(level, log_message)
                return func(*args, **kwargs)
    
            @attach_wrapper(wrapper)  # Attaches "set_level" to "wrapper" as attribute
            def set_level(new_level):  
                nonlocal level
                level = new_level
    
            @attach_wrapper(wrapper)  # Attaches "set_message" to "wrapper" as attribute
            def set_message(new_message):  
                nonlocal log_message
                log_message = f"{func.__name__} - {new_message}"
    
            return wrapper
        return decorate
    
    
    @log(logging.WARN, "example-param")
    def somefunc(args):
        return args
    
    somefunc("some args")
    
    somefunc.set_level(logging.CRITICAL)  
    somefunc.set_message("new-message")  
    somefunc("some args")

Not gonna lie, this one might take a bit to wrap your head around (you might want to just _copy-paste_ it and use it). The idea here is that `log` function takes the arguments and makes them available to inner `wrapper` function. These arguments are then made adjustable by adding the accessor functions, which are attached to the decorator. As for the `functools.wraps` decorator - if we didn't use it here, name of the function (`func.__name__`) would get overwritten by name of the decorator. But that's a problem, because we want to print the name. This gets solved by `functools.wraps` as it copies function name, docstring and arguments list onto the decorator function.

Anyway, this is the output of above code. Pretty neat, right?

    2020-05-01 14:42:10,289 - __main__ - WARNING - somefunc - example-param
    2020-05-01 14:42:10,289 - __main__ - CRITICAL - somefunc - new-message

`__repr__` For More Readable Logs
---------------------------------

Easy improvement to your code that makes it more debuggable is adding `__repr__` method to your classes. In case you're not familiar with this method - all it does is return string representation of the an instance of a class. Best practice with `__repr__` method is to output text that could be used to recreate the instance. For example:

    class Circle:
        def __init__(self, x, y, radius):
            self.x = x
            self.y = y
            self.radius = radius
    
        def __repr__(self):
            return f"Rectangle({self.x}, {self.y}, {self.radius})"
    
    ...
    c = Circle(100, 80, 30)
    repr(c)
    

If representing object as shown above is not desirable or not possible, good alternative is to use representation using `<...>`, e.g. `<_io.TextIOWrapper name='somefile.txt' mode='w' encoding='UTF-8'>`.

Apart from `__repr__`, it's also a good idea to implement `__str__` method which is by default used when `print(instance)` is called. With these 2 methods you can get lots of information just by printing your variables.

`__missing__` Dunder Method For Dictionaries
--------------------------------------------

If you for whatever reason need to implement custom dictionary class, then you can expect some bugs arising from `KeyError`s when you try to access some key that doesn't actually exist. To avoid having to poke around in the code and see which _key_ is missing, you could implement special `__missing__` method, which is called every time `KeyError` is raised.

    class MyDict(dict):
        def __missing__(self, key):
            message = f'{key} not present in the dictionary!'
            logging.warning(message)
            return message  

The implementation above is very simple and only returns and logs message with the missing _key_, but you could also log other valuable information to give you more context as to what went wrong in the code.

Debugging Crashing Application
------------------------------

If your application crashes before you get a chance to see what is going on in it, you might find this trick quite useful.

Running the application with`-i` argument (`python3 -i app.py`) causes it to start interactive shell as soon as the program exits. At that point you can inspect variables and functions.

If that's not good enough, you can bring a bigger hammer - `pdb` - _Python Debugger_. `pdb` has quite a few features which would warrant an article on its own. But here is example and a rundown of the most important bits. Let's first see our little crashing script:

    
    SOME_VAR = 42
    
    class SomeError(Exception):
        pass
    
    def func():
        raise SomeError("Something went wrong...")
    
    func()

Now, if we run it with `-i` argument, we get a chance to debug it:

    # Run crashing application
    ~ $ python3 -i crashing_app.py
    Traceback (most recent call last):
      File "crashing_app.py", line 9, in <module>
        func()
      File "crashing_app.py", line 7, in func
        raise SomeError("Something went wrong...")
    __main__.SomeError: Something went wrong...
    >>> 
    >>> import pdb
    >>> pdb.pm()  
    > .../crashing_app.py(7)func()
    -> raise SomeError("Something went wrong...")
    (Pdb) # Now we are in debugger and can poke around and run some commands:
    (Pdb) p SOME_VAR  # Print value of variable
    42
    (Pdb) l  # List surrounding code we are working with
      2
      3   class SomeError(Exception):
      4       pass
      5
      6   def func():
      7  ->     raise SomeError("Something went wrong...")
      8
      9   func()
    [EOF]
    (Pdb)  # Continue debugging... set breakpoints, step through the code, etc.

Debugging session above shows very briefly what you could do with `pdb`. After program terminates we enter interactive debugging session. First, we import `pdb` and start the debugger. At that point we can use all the `pdb` commands. As an example above, we print variable using `p` command and list code using `l` command. Most of the time you would probably want to set breakpoint which you can do with `b LINE_NO` and run the program until the breakpoint is hit (`c`) and then continue stepping through the function with `s`, optionally maybe printing stacktrace with `w`. For a full listing of commands you can go over to [`pdb` docs](https://docs.python.org/3/library/pdb.html#debugger-commands).

Inspecting Stack Traces
-----------------------

Let's say your code is for example Flask or Django application running on remote server where you can't get interactive debugging session. In that case you can use `traceback` and `sys` packages to get more insight on what's failing in your code:

    import traceback
    import sys
    
    def func():
        try:
            raise SomeError("Something went wrong...")
        except:
            traceback.print_exc(file=sys.stderr)

When ran, the code above will print the last exception that was raised. Apart from printing exceptions, you can also use `traceback` package to print stacktrace (`traceback.print_stack()`) or extract raw stack frame, format it and inspect it further (`traceback.format_list(traceback.extract_stack())`).

Reloading Modules During Debugging
----------------------------------

Sometimes you might be debugging or experimenting with some function in interactive shell and making frequent changes to it. To make the cycle of running/testing and modifying easier, you can run `importlib.reload(module)` to avoid having to restart the interactive session after every change:

    >>> import func from module
    >>> func()
    "This is result..."
    
    
    >>> func()
    "This is result..."  
    >>> from importlib import reload; reload(module)  
    >>> func()
    "New result..."

This tip is more about efficiency than debugging. It's always nice to be able to skip a few unnecessary steps and make your workflow faster and more efficient. In general, reloading modules from time to time is good idea, as it can help you avoid trying to debug code that was already modified bunch of times in the meantime.

**_Debugging is an Art._**

Conclusion
----------

Most of the time, what programming really is - is just a lot of trial and error. Debugging on the other hand is - in my opinion - an _Art_ and becoming good at it takes time and experience - the more you know the libraries or framework you use, the easier it gets. Tips and tricks listed above can make your debugging a bit more efficient and faster, but apart from these Python specific tools you might want to familiarize yourself with general approaches to debugging - for example [The Art of Debugging](https://remysharp.com/2015/10/14/the-art-of-debugging) by Remy Sharp.