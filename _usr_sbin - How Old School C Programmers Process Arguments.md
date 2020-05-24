/usr/sbin - How Old School C Programmers Process Arguments

# How Old School C Programmers Process Arguments

 **By Alex Beal**  **August 4, 2011**

Here’s a bit of code from Kernighan’s and Ritchie’s seminal text, [The C Programming Language](http://www.amazon.com/Programming-Language-2nd-Brian-Kernighan/dp/0131103628). I’m not sure I’d actually recommend coding this way (as written in the book, the entire program has only one comment), but it’s so darn clever and concise, I can’t help but post it. This snippet is part of a larger program called `find` that searches text for patterns, but the details aren’t important. I want to focus on the portion below that parses the arguments passed to the program. Don’t worry about understanding it just yet. I’ll step through it below:

	char *s;
	while (--argc > 0 && (*++argv)[0] == '-')
	    for(s = argv[0]+1; *s != '\0'; s++)
	        switch(*s) {
	            case 'x':
	                /* Set appropriate flags for 'x' option */
	                break;
	            case 'n':
	                /* Set appropriate flags for 'n' option */
	                break;
	            default:
	                printf("Illegal option %c\n", *s);
	                argc = 0;
	                break;
	        }
	if( argc != 1)
	    printf("Usage: find -x -n pattern\n");
	else
	    /* Main program logic goes here */

What’s so cool about this is its flexibility. Those two nested loops can process all of the following (and more):

	find -xn hello
	find -nx hello
	find -x -n hello
	find -n -x hello
	find hello
	find -x hello
	...

As you can see, the usage is `find [-x] [-n] PATTERN`. The nested loops above process the flags, `-x` and `-n`, in any order, and either separated or concatenated. Hopefully you’re as impressed as I was. Anyway, let’s dive into the code and begin by looking at the while statement.

## The while Loop

`while (--argc > 0 && (*++argv)[0] == '-')`

What’s going on here? First, the while loop decrements `argc` and checks that it’s greater than 0 (as dictated by convention, `argc` holds the number of arguments passed to the program). Whenever a flag is processed, `argc` is decremented, thus making it a running count of how many flags there are left to process. If it’s 0, then there’s nothing left to do. Notice that the decrement always occurs before the ‘>’ is evaluated. This would be true even if it were postfix (i.e., `argc-- > 0`).

If argc checks out, then we move on to `(*++argv)[0]=='-'`. Yikes. That’s a doozy. First remember that `argv` is a pointer to the strings that contain the arguments. So, `argv` points to the string containing the program name and `(argv+1)` points to the string containing the first argument. That means that `(*argv)[0]` is the first character of the program name and `(*argv)[1]` is the first character of the first argument. Putting that together, `(*++argv)[0]` increments `argv`, dereferences it to a string, and then gets the first character of that string. In other words, if `argv` was originally pointing to the string containing the program’s name, it’s now pointing to the string containing the first argument, and then grabbing the first character of that string and comparing it to ‘-’. Why’s it doing that? Because it wants to make sure it’s looking at a string containing a flag, and flags begin with the ‘-’ character.

Extra Credit: How is `*++argv[0] == '-'` different than `(*++argv)[0] == '-'`?

By the end of all of this, `argc` represents the number of arguments remaining and `argv` is pointing to the string containing the first argument. Wow.

That was a bit of a slog, but we’re not done yet. Let’s look at the for loop.

## The for Loop

	char *s;
	for(s = argv[0]+1; *s != '\0'; s++)

Oh boy. More pointer arithmetic on arrays of arrays. Well, what’s going on here? Remember that now `argv` is pointing to the string containing the first argument. Therefore, `argv[0]` is the pointer to the first character of that string and `argv[0]+1` is the pointer to the second character of that string. `argv[0]+1` is then assigned to `s`. The result is that, if `argv` was pointing to “-xn”, then s is now pointing to the “x” in that string. Lucky for us, the last half is much simpler. `*s != '\0'` checks to make sure that it hasn’t reached the end of the string yet, and `s++` increments the pointer (after the loop has finished its first run, of course). If the first run processed the “x” in “-xn”, then `s` is incremented and the “n” is processed. The third iterations sees the “” at the end of the string and exits. So, to bring this all together, the for loop traverses concatenated flags (i.e., it moves the pointer from the “x” to the “n” in “-xn”) and the while loop traverses separated flags (i.e., it moves the pointer from the “-x” to the “-n” in “-x -n”).

# The switch Statement

	switch(*s) {
	      case 'x':
	        /* Set appropriate flags for 'x' option */
	        break;
	    case 'n':
	         /* Set appropriate flags for 'n' option */
	        break;
	    default:
	        printf("Illegal option %c\n", *s);
	        argc = 0;
	        break;
	}

The switch is simple enough. It tests if `*s` is equal to one of the flags, and then does the necessary processing for that flag. Most likely it just sets an internal flag, which will be taken into account when the main part of the program runs (this is how it’s set up in the full program).

## The if Statement

	if( argc != 1)
	    printf("Usage: find -x -n pattern\n");
	else
	    /* Main program logic goes here */

The last and final part is the if statement. It prints an error/usage message if `argc` is not equal to 1. Why? Because there should always be one argument left after the flags are processed (the `PATTERN` argument). The error will also be printed if the program is given an unrecognized flag and the default case in the switch is executed. If there aren’t any problems, then it executes the else where the main part of the program is contained.

So there you have it. That’s how Kernigham and Ritchie did it in 1978. Nowadays they just haul in the software weenies with their fancy objects and methods. Lost is the subtle art of manipulating arrays of pointers to strings of characters. Alas. (Just kidding. After all, I’m probably one of those software weenies.)