Programming language from scratch: 3 easy steps to an interpreter

![screen-shot-2017-08-16-at-19-30-28.png](../_resources/03e08d4fd36ea26936388eacfdc7e71e.png)
August 16, 2017

# Programming language from scratch: 3 easy steps to an interpreter

A little while ago [I wrote about 16bitjs](https://francisstokes.wordpress.com/2017/07/20/16-bit-vm-in-javascript/), a 16 bit virtual machine written in javascript. It implemented a custom CPU architecture and assembly language, assembler, and debugger. I had the thought at some point that it would be pretty awesome to create a programming language from scratch that would compile to 16bitjs assembly and run on the VM. I’ve since found out this is a monumentally complicated task, but I still went ahead and created a programming language anyway (though not one that compiles to 16bitjs) and the result is Lel. This article will delve into the steps that go into writing a creating an interpreter for a programming language – without unnecessary layers of complexity or the magic status people who are skilled at this kind of thing like to bestow on it. By the end you’ll have a pretty decent grasp on how you could go about the same task. All the code for Lel is open and available on [github](https://github.com/francisrstokes/Lisp-esque-language). And if you’re itching for more, keep an eye on this blog where in the next week or so I’ll post about a little compiler that *I did end up writing* that targets the 16bitjs VM, but for a much more basic language.

## The elements of an interpreter

We might as well start out by defining exactly what an interpreter is. Basically its a program that reads the source code, and runs it right there and then, without having to first compile that source code into machine language. Easy enough. However there are still a couple of steps that need to take place before it can run that source code. Loosely speaking, these are:

1. Tokenisation
2. Parsing (treeification)
3. Evaluation

Tokensiation takes your source code and turns it into a big flat list of *tokens*, where each token represents a type of thing (a number, variable name, bracket etc) and a value (42, “hello”, true etc).

Parsing, or treeification as I like to think of it, is the process of taking a flat list of tokens and ordering them into a tree structure. Why do they need to be in a tree? Well, think of anytime you have a function for instance. A function contains a function body – all the stuff *inside* the function. A for loop, or an if statement, or a class all have a body with stuff inside. Typically the body is referred to as a block, and blocks very often contain other blocks. This is where the tree comes it: It let’s you organise those tokens – which don’t mean anything on their own – into the things they represent, e.g. a function with a body, containing 3 different if statements with their own bodies etc. That naturally forms a tree structure.

Finally we’ve got evaluation, which takes your tree and goes through it, branch by branch, and *actually does the stuff*.

That’s the essence right there – just 3 steps. Now with that in mind let me introduce you to Lel, so we’ve got some context to talk about each of those steps and how they work.

## Introducing: Lel

Lel, or the “Lisp-esque language”, is based on the syntax of lisp, a 50+ year old programming language with some very cool ideas in it. Let’s take a look at how familiar concepts look in Lel.

Here is assigning a variable, and declaring a function.
1
2
3
4
5
6
7
[object Object][object Object]  [object Object]

[object Object][object Object]  [object Object]
[object Object][object Object]
[object Object][object Object]  [object Object][object Object]  [object Object]
[object Object][object Object]
[object Object]

‘let’ is the assignment keyword. Here we’re saying “creat a variable called ‘lifeUniverseAndEverything’ and set its value to 42. Just below that is a function definition for ‘sayHello’, which takes one argument and then print’s out a message.

To run that function:
1
2
3
[object Object][object Object][object Object]

[object Object][object Object]

I’ll stop here and point out the obvious. There’s a lot of parentheses going on here. The reason why is because Lel, like all lisp derived languages, uses S-expressions. To explain what an *S-expression*, it’s handy to first know what an *expression* is in general. An expression is a piece of code, that when it runs eventually turns into some kind of primitive value. Here a primitive can be something like a number, a string, or in a slightly more complex case a function reference. An S-expression then is an expression that is encased in parentheses, and can contain other S-expressions.

Another interesting thing is that whitespace is completely irrelevant. That means:

1

[object Object][object Object]  [object Object][object Object]  [object Object][object Object]  [object Object]

and
1
2
3
4
5
6
7
8
9
[object Object][object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]

Are both valid in Lel, though I definitely wouldn’t recommend formatting code like either of those. Using the whitespace to group logical parts together makes the most sense. As a side note: if Lel ever becomes popular enough that people argue about tabs vs spaces, or if function bodies belong on a newline always, that will absolutely make my life.

Anyway, let’s look at conditionals:
1
2
3
4
[object Object][object Object]  [object Object]
[object Object][object Object][object Object][object Object]
[object Object][object Object][object Object][object Object]
[object Object]

That says that if *1 < 3*, print “1 is less than 3.”, otherwise print “1 is NOT less than 3.”. The ordering of that conditional is probably looking a bit strange to you, because the operator comes before the numbers it operates on. That’s because *<* is literally a function. 1 and 3 are its arguments. The same goes for all the comparrison functions, and actually, the same goes for everything in Lel. It’s functions all the way down.

OK so with all that in mind, we can take a look at the first step in the interpreter: turning code into tokens.

## Tokenisation

Let’s start out with a really simple program that calculates cubes.
1
2
3
4
5
6
7
[object Object][object Object]  [object Object]
[object Object][object Object]
[object Object]

[object Object][object Object]  [object Object]

[object Object]

The goal here is to take this program and get an array of tokens out. Those tokens should describe the breakdown of everything we need to construct the tree – also known as the *abstract syntax tree*. During tokenisation Lel recognises 8 token types:

- SKIP – whitespace and comments
- LPAREN – left parenthesis
- RPAREN – right parenthesis
- NUMBER – any kind of supported number (10, -23, 1.0, etc)
- STRING – Anything in double quotes (e.g. “hello”)
- BOOLEAN – true and false
- IDENTIFIER – things like language keywords and variable names
- RANGE – a special operator that makes generating lists easier (I’ll get to lists in a little while)

Each of these token types are associated with a regular expression or a literal pattern. If you don’t know what a regular expression is, then the simplest short explaination is that it’s a way of describing patterns of text, and you should read up on them a bit for the next part to make sense.

Whitespace for example is matched with
**
>  /^[\s\n]+$/
**
and comments with
**
>  /^;.+?\n$/
**

The tokeniser takes a single character at a time and checks if it matches any of the patterns. If it finds a match, it keeps adding characters until it doesn’t match the pattern anymore. When it stops matching , everything before the failed match is the tokens value. A token ends up with the following structure:

1
2
3
4
[object Object]
[object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object]

Simple right? Well actually it does need to be just a tiny bit more complicated than that. For instance, because an identifier can be any characters that match the regular expression

**
>  /^[a-zA-Z+-\/*\%_\>\<=]*$/
**

something like -10 will actually match the negative sign as an identifier before it matches as a number. So to recognise a number, at least 2 characters are needed in order to find a correct match. To deal with these types of ambiguities in Lel, there are a special set of “ambiguous” patterns that are run first. If character matches an ambiguous pattern, the tokeniser goes into a mode for resolving the ambiguity. For instance, to ensure numbers match properly, the pattern

**
>  /^-$/`
**

is used as an ambiguous pattern. If it matches, it will then add a character and see if it matches an associated ambiguous pattern, which in this case is only the regular number pattern. If it doesn’t match, it goes back to the first character and just tries to match using the normal patterns.

The very astute reader will notice that with the system I’ve described above, matching the words “true” or “false” as a boolean will never work. This is because for true to match, it has to be four characters, and literally the word “true”. A match for the more general IDENTIFIER will occur way before the tokeniser has added enough characters to get that match. So there have to be a set of patterns which are “exact”. The tokeniser checks these patterns first, and reads exactly the number of characters it would need to get that match.

The actual order of checks is:
1. Exact matches
2. Ambiguous matches
3. Regular matches

That is tokenisation in a nutshell, or at the very least that is Lel’s tokeniser – there are many different ways you could approach this problem. I recommend taking a look at the code to get a real sense for this. So if we go back to the original example cube code, the tokenised output will look like the following:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
[object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object]

In the Lel interpreter the SKIP tokens generated by whitespace and comments are not even added to the token list, so only the important information appears here. This is the barest information needed to tokenise input, but often you will see a lot more information associated with a token, such as line number and character position. This kind of information is important when you are enforcing a coding style for instance – you can see if it has been correctly indented, or the standard practices of the language have been used (think linting).

## Treeification, or more boringly “parsing”

Parsing tokens into a tree basically involves matching tokens to sequences that are valid in the language. In the case of Lel, that’s a relatively straightforward process, because there is only one kind of thing the language can express – which is function execution. This isn’t always the case with every language, and parsing becomes more involved the more different kinds of special things your language can do; in most languages you have a special way to handle assignment, a special way to handle a switch statement, a special way to declare or execute a function etc.

The basic idea here is going to be that the root of the tree is an empty array. Every time we hit a left parenthesis token, that signifies the beginning of a new branch, which is a new empty array at the current point in the branch (in the beginning this is the root). Conversely when we hit a right parenthesis token, that signifies the end of that branch. Every other token is going to be added to which ever branch we happen to be in at the time. When all the tokens are processed the tree is returned.

So converting those tokens using the process described above will yield:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
[object Object]
[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]
[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]
[object Object][object Object]
[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object][object Object]
[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]
[object Object]

So now the LPAREN and RPAREN tokens are all gone, and only INDENTIFIERS and a NUMBER remain, all correctly nested into a nice tree. That ready to be evaluated, completing the final piece in this trifecta.

Before we move on to that, it;s good to reiterate that if you want to up the game in terms of the kind of things the language can express, then the parser is going to get a much bigger role. Instead of just going through the tokens one by one, choosing what to do on that information alone, we might need to look ahead one or two tokens to see what kind of expression or statement we’re dealing with. And just placing into deeper levels of arrays probably won’t cut it either, since we will need some information to say if what follows is an assignment or a function call or whatever. But fundamentally it’s pretty much always going to be a tree structure.

## Evaluation

This is going to be where the real heavy lifting of the interpreter happens. In Lel, there is one function that rules them all, and that is the *evaluateExpr(…)* function.

At the beginning of the program, the whole tree is passed into this function. The function take a look at what kind of content it got as the “expression” and works out what to do with it. If what it got is an array (i.e. a branch of the tree), then it call’s *evaluateExpr* for every expression inside that branch. If those branches contain branches, the same happens. Eventually all these nested calls to *evaluateExpr* will end up on a “primitive” – basically a number, string, boolean, function or list reference. When that happens, the final value is returned all the way back up the chain.

It obviously won’t always be the case that every expression just contains an array of more expressions. More often than not it’s going to be something like a function call, or a variable or function assignment, or a reference to an existing variable. Let’s take a look at a variable assignment:

1
[object Object][object Object]  [object Object]

Which will come out of the tokeniser and parser as an array with tokens inside. In this case, the *evaluateExpr* function will see that the expression is an array with tokens, and take a look at the first token. The order of checks is:

- Is it a primitive value?
- Is it a variable?
- Is it an empty block?
- Is it a non-empty block?
- Is it a core language function?
- Is it a defined function?

So in our current case, *let* is considered to be a core language function, and so the *evaluateExpr* is going to return the value that come from passing this expression to a function that handles *let*. The let function will perform further evaluations if it needs to (imagine setting a variable to the sum of two other variables) by calling *evaluateExpr* itself, and eventually will return the newly assigned value. From now on, inside the current *scope*, there is a variable called ‘a’.

### Scope

I nonchalantly threw in the word scope there. Chances are you’ve heard that word before, and if you’re from a javascript background – especially from the old ES5 days – you’ve probably pulled your hair our trying to work out what the scope of ‘this’ is. So what exactly is a scope? Well it’s the context you’re evaluating any given expression under. By context I mean all the variables and functions that have been described that can sanely be accessed within some section of code.

We talk about different scopes and contexts because every function that’s declared get’s its own scope. Every time a function runs it get’s a new execution scope. All these scopes are chained together in a parent-child kind of relationship called a data structure that can be loosely defined as a singly linked list. That’s a fancy way of saying that a scope has all of its own stuff, as well as a way to access its parent’s scope (which has a way to access it’s parent scope…).

Just as all roads lead to Rome, all scopes eventually lead to what’s known as the global scope, or root scope. This is the scope that people often tell you it’s bad to “pollute” without reason. Well the reason is that it’s a kind of sacred shared space. If you were living in a neighbourhood that had a shared park in the middle, it’s pretty fair to say you can’t go and build a shed with all your tools there, because it’s not fair to everyone else. And you definitely cannot go into someone else’s shed and start using their tools!

![scope.png](../_resources/31b043051d5d51ac78ab2049bf618991.png)

To complete the picture, when *evaluateExpr* is called, it’s signature looks like: *evaluateExpr(scope, expr)*. If a variable is assigned, it’s going into that scope. If a function is declared, the new scope it gets is linked with the scope passed to *evaluateExpr*.

### Evaluating the tree

With all of that now burned into our minds, we can finally take a look at what happens to our little cube example tree when we evaluate it. The next few paragraphs we’re going to follow the execution along, just like watching it in a debugger to see exactly how the different expressions break down.

First things first, we create the global scope. It’s parent scope is null since it doesn’t have one, and it’s list of variables and functions is empty. The whole tree is going to be passed to *evaluateExpr* like so:

1
[object Object]

*evaluateExpr* is going to figure out that this expression is a “non-empty block”, and call *evaluateExpr* on each item inside the block, one after another. So then we get:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
[object Object]
[object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]
[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]
[object Object]

[object Object]

Now *evaluateExpr* is going to look at the first token in the expression recognise this expression as a “core language function”, whose name is “function”, meaning it needs to call the function associated with the keyword “function” (something something inception). That’s going to be called with the current scope and the current expression, the end result of which is the global scope now contains a member called “cube”, which is a function definition. That function definition has its own scope (let’s call it *cubeScope* for illustration purposes), which has access to the global scope. That’s it for this branch expression – now execution goes back to executing the blocks of the tree.

1
2
3
4
5
6
7
8
9
10
11
[object Object]
[object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object]

[object Object]

Our next branch is a *let*, and will be recognised just like before as a “core language function”. All the information will be passed to the function associated with *let*. Here’s where it get’s interesting, because the variable being created here is the result of running the function we just defined. Before let can do anything else, it needs to first evaluate the inner function call to *cube*, so it calls *evaluateExpr* itself:

1
2
3
4
5
6
[object Object]
[object Object]

[object Object][object Object][object Object][object Object][object Object]  [object Object]

[object Object][object Object][object Object][object Object]
[object Object]
[object Object]

Which is interpreted as a “defined function”. When that kind of expression is encountered, first resolves the function definition for *cube* by finding it in scope, and then passes the execution to a specialised function that deals with calling defined functions, boringly named *callFunction*. *callFunction* takes our function definition for *cube* and our value of 3, creates an *cubeExecutionScope* out of the *cubeScope* that is on our function definition. Execution scope is the place where we place any arguments to this function, in this case the value 3. That 3 is matched to the *x* that *cube* takes as an argument. Now all that happens is *evaluateExpr* is called one more time like so:

1
2
3
4
5
6
7
8
[object Object]
[object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object]
[object Object]

You’ll notice that *branch* is just the body of our *cube* function, and we’re using the scope where *x = 3*. In the end this evaluates to 27 as expected, and that value is passed all the way back to our original *let*.

So now *let* has it’s value, it knows to use the name “threeCubed”, and it places it as a variable into the global scope with the value 27. Control returns to the original block we were evaluating, and the next and final expression is:

1
2
3
4
5
6
[object Object]
[object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object]
[object Object]

Home stretch! *print* is recognised as a “core language function” type expression, which predictably writes it’s argument’s value to stdout. That value first needs to be evaluated so we can get the 27 our of the *threeCubed* variable, so another call is made:

1
2
3
[object Object]
[object Object][object Object][object Object][object Object][object Object]
[object Object]

Which of course is 27. That’s passed back to *print* which finally writes that value out. That was our final expression, so the program is complete. Congratulations, you have just walked through the entire process of interpretation!

## Putting it all together

We’ve seen how the tokeniser converts source code into a stream of tokens, and how the parser treeifies the tokens it receives, and finally how the evaluator takes the tree and all of its little branches, and all of their little branches, and gives it to one function that can work out which specialised function it should pass it on to. That is an interpreter in a nutshell! I hope that it’s provided some tangible perspective on a topic which can seem magical without context. If you want to try out Lel you can install it through npm:

1
2
[object Object][object Object]  [object Object]
[object Object][object Object]

If you want to read the code or clone the repo, you can find all that on the github page. And if you end up making your own programming language using something you’ve learned here, I’d love to hear about it. Hit me up in the comments or on github and I’ll be sure to check it out.

**Awesome programmer looking for new challenges? [We’re always looking for talented people at WARP](http://wearereasonablepeople.nl/).**

Advertisements

### Share this:

- [Twitter](https://francisstokes.wordpress.com/2017/08/16/programming-language-from-scratch/?share=twitter&nb=1)
- [Facebook102](https://francisstokes.wordpress.com/2017/08/16/programming-language-from-scratch/?share=facebook&nb=1)
- [Google](https://francisstokes.wordpress.com/2017/08/16/programming-language-from-scratch/?share=google-plus-1&nb=1)

-
[Like](https://widgets.wp.com/likes/#)

- [![joskid](../_resources/e2b528c93c8716c47bb16a835270293e.png)](https://en.gravatar.com/joskid)
- [![vikdutt](../_resources/97a40500b2bca6b31af3bfa82b50948f.jpg)](https://en.gravatar.com/vikdutt)
- [![Tanmay Chandane](../_resources/830a288ff37b32e3e9376eb62352de0c.jpg)](https://en.gravatar.com/tanmaynchandane)

[3 bloggers](https://widgets.wp.com/likes/#) like this.

[10 Comments](https://francisstokes.wordpress.com/2017/08/16/programming-language-from-scratch/#comments)