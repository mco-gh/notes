How do Unix pipes work?

 [Vegard Stikbakke](https://www.vegardstikbakke.com/)

# How do Unix pipes work?

March 21, 2020

Pipes are cool! We saw how handy they are in a [previous blog post](https://www.vegardstikbakke.com/unix). Let’s look at a typical way to use the pipe operator. We have some output, and we want to look at the first lines of the output. Let’s [download](https://www.gutenberg.org/files/28054/28054-0.txt)  [The Brothers Karamazov](https://en.wikipedia.org/wiki/Lazy_evaluation) by Fyodor Dostoevsky, a fairly long novel.

	> wc -l karamazov.txt
	  36484 karamazov.txt

If we `cat` this file, it will be printed to the terminal.

	> cat brothers_karamazov.txt
	... many lines of text!
	***FINIS***

It takes a noticeable amount of time to finish. Now let’s just look at the first two lines by piping it into `head`.

	> cat karamazov.txt | head -n 2
	The Project Gutenberg EBook of The Brothers Karamazov by Fyodor
	Dostoyevsky

Now it’s done in an instant. It seems that the `cat` operation terminates when `head` is done! Of course, `head -n 2` only needs two lines of input to output what it’s supposed to output. But how does `cat` know to stop when `head` is finished?

In this blog post, we’ll learn a bit about how pipes work, and write a small `cat` clone in Python and Go.

* * *

Processes in a pipeline are started simultaneously. We can confirm this by running

	> sleep 100 | head

in one terminal window, and taking a look at running processes with `ps` in another.

	> ps
	  PID TTY           TIME CMD
	52892 ttys007    0:00.00 sleep 100
	52893 ttys007    0:00.00 head

From the Unix manual page on pipes, [`man(7) pipe`](https://linux.die.net/man/7/pipe), we learn that if we pipe `process1` into `process2`, the second process will wait (block) until it receives input. Furthermore, if `process1` is finished, it closes its end of the pipe. This will cause a `SIGPIPE` signal to be generated for `process1`.

## Writing a `cat` clone in Python

Let’s try to write a simple `cat` clone that mimics this behavior. Instead of reading from file, let’s read from standard input. That means we should be able to pipe into it. In Python, standard input is found in [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin).

	# cat.py
	import sys

	for line in sys.stdin:
	    print(line, end='')

This behaves the same as the regular `cat` command if we pipe into it.

	cat karamazov | python cat.py
	... many lines of text!
	***FINIS*

But does it also stop when we pipe it into `head`?

	> cat karamazov | python cat.py | head -n 2
	The Project Gutenberg EBook of The Brothers Karamazov by Fyodor
	Dostoyevsky
	Traceback (most recent call last):
	  File "cat.py", line 4, in <module>
	    print(line, end='')
	BrokenPipeError: [Errno 32] Broken pipe
	Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
	BrokenPipeError: [Errno 32] Broken pipe

We see that we get an error `BrokenPipeError`. But if we look closely at the output here, we see that it’s printed twice. We can try catching the error with a `try`/`except`.

	# cat.py
	import sys

	for line in sys.stdin:
	    try:
	        print(line, end='')
	    except BrokenPipeError:
	        pass

Now we only get the second part of the error output from before.

	> cat karamazov.txt | python cat.py  | head -n 2
	The Project Gutenberg EBook of The Brothers Karamazov by Fyodor
	Dostoyevsky
	Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
	BrokenPipeError: [Errno 32] Broken pipe

Since we know that a terminated process to the right of a pipe sends a `SIGPIPE` when it’s done, maybe this means that this signal isn’t handled properly?

Indeed, a quick search leads us to a section of the Python documentation, namely [Note on `SIGPIPE`](https://docs.python.org/3/library/signal.html#note-on-sigpipe). It gives a recipe for handling it. Our program now becomes

	# cat.py
	import sys
	import os

	for line in sys.stdin:
	    try:
	        print(line, end='')
	    except BrokenPipeError:
	        devnull = os.open(os.devnull, os.O_WRONLY)
	        os.dup2(devnull, sys.stdout.fileno())

and it works as we want, by getting rid of the pesky error message.

	> cat karamazov.txt | python cat.py  | head -n 2
	The Project Gutenberg EBook of The Brothers Karamazov by Fyodor
	Dostoyevsky

But an explanation of how this works would be nice. The recipe has a comment saying that

>

> Python flushes standard streams on exit; redirect remaining output to devnull to avoid another `BrokenPipeError`>  at shutdown.

What we do here, apparently, is redirect the remaining error output to `/dev/null`.`/dev/null` refers to [https://en.wikipedia.org/wiki/Null_device](https://www.vegardstikbakke.com/how-do-pipes-work-sigpipe/the%20null%20device), which accepts output, but discards it all. In other words, to not print something, we can redirect output there.

The first line in the `except BrokenPipeError` block opens `/dev/null`. The second line calls [`os.dup2`](https://docs.python.org/3/library/os.html#os.dup2), which takes two file descriptors. It *“duplicate[s] file descriptor `fd` to `fd2`, closing the latter first if necessary.”*So in the second line we duplicate `/dev/null` into standard output, and possibly close standard output first.

But I don’t really understand this. It turns out that another way of silencing the output is to close standard error.

	import sys

	for line in sys.stdin:
	    try:
	        print(line, end='')
	    except BrokenPipeError:
	        sys.stderr.close()

## Writing a `cat` clone in Go

I want to learn some Go, so let’s try writing the same program in it. In Go, we can apparently simply copy from standard in to standard out. The first program becomes a tidy one liner.

	// cat.go
	package main

	import (
	    "os"
	    "io"
	)

	func main() {
	    io.Copy(os.Stdout, os.Stdin)
	}

When we run this, it also complains about `SIGPIPE`:

	> cat karamazov.txt | go run cat.go | head -n 2
	The Project Gutenberg EBook of The Brothers Karamazov by Fyodor
	Dostoyevsky
	signal: broken pipe

Turns out ignoring the `SIGPIPE` signal also is one line.

	// cat.go
	package main

	import (
	    "os"
	    "io"
	    "os/signal"
	    "syscall"
	)

	func main() {
	    signal.Ignore(syscall.SIGPIPE)
	    io.Copy(os.Stdout, os.Stdin)
	}

I hope you learned something reading this!

* * *

 **Do you want to get notified of new blog posts? Go [here](https://www.vegardstikbakke.com/feed.xml) for an RSS feed.**