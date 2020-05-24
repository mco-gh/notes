Bash $* and $@

# Bash $* and $@

Mar 29, 2017

In Bash, there are two closely related “special parameters” for accessing how the current script was invoked: `$*` and `$@`. For both variables, the behavior is affected by whether or not the variable is enclosed in double quotes. The following table summarizes all cases:

Form
Meaning
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
Easy, right?

Without double quotes, the two do the same thing: they expand to each positional argument, and additional word splitting will be done on each argument as usual. With double quotes, the two have an extremely subtle, but important difference. Consider the following two program invocations:

	*# invoke foo.sh with two arguments*
	$ ./foo.sh hello world

	*# invoke foo.sh with one argument*
	$ ./foo.sh "hello world"

If `foo.sh` is implemented using `$*` or `"$*"`, it won’t be able to distinguish between these two cases. If it’s using `$*`, then it will think there are two arguments in both cases, due to word splitting. If it’s using `"$*"`, it will look like one argument in both cases.

If instead `foo.sh` is implemented using `"$@"`, the two cases are distinguishable.

This usually comes up when writing a wrapper script that passes its arguments down to another program. Here’s a complete example:

	#!/bin/bash
	SHOWTIMES=0
	OPTIND=1
	while getopts "h?v" opt; do
	    case "$opt" in
	        h|\?)
	            echo "usage: $0 [-v]"
	            exit 0
	            ;;
	        v)
	            SHOWTIMES=1
	            ;;
	    esac
	done

	*# N.B. must use "$@" here, NOT $**
	run() {
	    if [ "$SHOWTIMES" -eq 1 ]; then
	        time "$@"
	    else
	        "$@"
	    fi
	}

	run cp "./expense report.xls" "./funny    name.txt" /tmp
	run dig www.google.com
	*# etc...*

If the script is run without any arguments, all of the lines that start with the`run` command will just run as usual. On the other hand, if the script is invoked with `-v`, all of the lines that start with `run` will be timed using the `time` shell builtin.

As shown in the example, it’s possible to call `run` with arguments containing whitespace. The only way to ensure that such arguments are handled correctly is to use the quoted form `"$@"`. As a fun bit of trivia: `$@` is the only bash variable that can be split into words when quoted.

It’s understandable if you find this confusing. My advice is to always use the quoted form `"$@"` if you’re unsure. It’s almost always what you want.