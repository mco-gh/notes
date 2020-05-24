Global Mutable State

#  Global Mutable State

###   [![ericnormand profile image](../_resources/e04e0c9c52a788244e5cf0e41838c805.jpg) Eric Normand](https://dev.to/ericnormand)  [(L)](http://twitter.com/ericnormand)  [(L)](http://github.com/ericnormand)  Sep 18, 2017

 [#fp](https://dev.to/t/fp)  [#javascript](https://dev.to/t/javascript)

One of the biggest problems in software is global mutable state. It makes your code difficult to work with, and once you go down the road, it keeps getting worse. Reducing the amount of global mutable state in your program is one of the best ways to improve the quality of your code, regardless of whether it's procedural or functional.

### Definition

Global mutable state has three words, and each is important:

***Global*** means that it's accessible from any other point in your code. This ties all of your code together. You have to reason about the whole program instead of reasoning about a small part, because any other part can touch it.

***Mutable*** means that it can be changed. You'll usually see that anyone who can read the value can also change it. Two reads right next to each other in the code might return different values. Or, worse, the data structures they return themselves are changing, even after a read.

***State*** is harder to define. But it basically means that the value depends on the history of the program. How far into the history? Well, in the worst case (namely, global mutable state), it means the entire history. **You have to know everything about how the program was executed**, including how threads were interleaved.

When you combine global, mutable, and state, you get a big mess. When people say "it's [hard to reason about](http://www.lispcast.com/reasoning-about-code)", **what they really mean is "it's got bugs and you can't tell by reading the code"**.

The nice thing is that you can systematically remove those same three aspects. And you can remove them more or less separately. I like to say that **it's possible to [program functionally in any language](http://www.lispcast.com/fp-in-my-language)**, even the most procedural languages out there. One way to do that is to reduce the amount of global mutable state as close to zero as you can.

### Identifying Global Mutable State

Some telltale signs: multiple variables in the global scope (in Clojure: multiple atoms in the toplevel of a namespace), reading and writing to the globals with no clear patterns (or reading from the globals multiple times in a small piece of code). The variable could have changed values between reads.

### Cleaning up

It's actually hard to get rid of global mutable state once it's in there. Its usage will spread if it's not tied down. Global mutable state is so useful that it can actually be used for many different purposes. After a while, it's hard to see what the usage patterns are and how you would go about replacing them. But we can tackle each of the naughty aspects in turn.

#### 1) Does the variable need to be global?

Maybe you can rework the code so that an object is passed into

functions instead of being a global variable. That would mean you can create a new instance each time you run the code, which at least guarantees that it is starting from a known value each time and that you are encapsulating the mutation in different executions.

In other words, **turn global variables into local variables**. The best is local to the function doing the mutation (or smaller scope, if possible). Next best is an instance variable on a local object.

It's very tempting to use globals because they're an easy way for different parts of the code to work together. Here's an example:

var  file;  // the dreaded global variablesvar  recordCount;function  readFile()  {  file  =  openFile("input.txt");  // global mutation here}function  countRecords()  {  recordCount  =  0;  for(var  c  in  file.lines())  {  // global read  recordCount++;  // global mutation here  }}function  generateOutput()  {  for(var  c  in  file.lines())  {  print(c  +  ","  +  recordCount);  }}function  processFile()  {  readFile();  // these lines have to be in this order  countRecords();  generateOutput();}

Let's try to make the variables less global using the technique above.

// got rid of the globalsfunction  readFile(state)  {  // functions now take the state  state.file  =  openFile("input.txt");}function  countRecords(state)  {  // see, the state is now an argument  var  x  =  0;  // use a local here, instead of storing  for(var  c  in  state.file.lines())  {  // intermediate values in the global  x++;  }  state.recordCount  =  x;  // then assign the state once}function  generateOutput(state)  {  // state as argument, again  for(var  c  in  state.file.lines())  {  print(c  +  ","  +  state.recordCount);  }}function  processFile()  {  var  state  =  {};  // the state is now local (still mutable)  readFile(state);  countRecords(state);  generateOutput(state);}

The biggest transformation we do is to pass a `state` object to each of the methods. It is no longer global. Each time we run `processFile` we will generate a new instance. We start from a known initial state and we know we won't have any contention for that object.

The other transformation we did was to rely more on local variables for accumulating intermediate values. This may seem trivial, but it means that at no point does our state object contain inconsistent data. **It either does not contain the data or it's correct.**

#### 2) Does it need to be mutable?

Are there functions that read from but don't write to the variable? They could be changed to take the current value as an

argument. Reducing the amount of code that relies on those particular variables is a good thing.

In other words, do as much work as possible using only the arguments and return values of your functions. Isolate the mutation of the variable to a small portion of your code.

Let's apply this technique to code we just modified.

function  readFile()  {  return  openFile("input.txt");  // instead of mutating state,}  // just return the valuefunction  countRecords(file)  {  // take just the state you need as arguments  var  x  =  0;  for(var  c  in  file.lines())  {  x++;  }  return  x;  // return the value you calculate}function  generateOutput(file,  recordCount)  {  // take the two values you need  for(var  c  in  file.lines())  {  // as arguments  print(c  +  ","  +  recordCount);  }}function  processFile()  {  var  file  =  readFile();  // then use local variables  // (initialized but never mutated)  var  recordCount  =  countRecords(file);  generateOutput(file,  recordCount);}

We've translated code that wrote to a mutable argument into code that merely returns the value it calculates. Then we use local variables to hold the return values for later. Notice how `readFile` is doing so little work now (it's just a function call) that maybe we will want to remove it and just call the `openFile` directly. That is up to you to decide, but it's one of the things I notice a lot when removing mutation: functions become trivial to read and write, and often they are so trivial you will want to inline them.

function  countRecords(file)  {  var  x  =  0;  for(var  c  in  file.lines())  {  x++;  }  return  x;}function  generateOutput(file,  recordCount)  {  for(var  c  in  file.lines())  {  print(c  +  ","  +  recordCount);  }}function  processFile()  {  var  file  =  openFile("input.txt");  // we can just inline this one-liner  var  recordCount  =  countRecords(file);  generateOutput(file,  recordCount);}

#### 3) Does it need to be state?

Can the algorithms be reworked so that their natural input and outputs (arguments and return values) are used instead of writing to a location? For instance, maybe you're using the variable to count stuff. Instead of the function adding to a variable, maybe it could just return the total count instead.

Programs need state. But do we need to rely on the state to get the right answer? And does our state need to depend on the whole history of the program?

Let's go through step by step in our code, removing state.

function  countRecords(file)  {  var  x  =  0;  // here's our state  for(var  c  in  file.lines())  {  x++;  // it changes each time through the loop  }  return  x;}

The variable `x` is state. Its value depends on how many times the loop body has executed. Usually, this kind of counting loop is unnecessary because the standard library can already count a

collection.

function  countRecords(file)  {  return  file.lines().length();  // we prefer not having to deal with the state}

Wow! There's no state, now. And in fact, it's so short we can just inline it. It's called once in `processFile`. Let's inline it there.

function  processFile()  {  var  file  =  openFile("input.txt");  var  recordCount  =  file.lines().length();  // inline the one-liner (optional)  generateOutput(file,  recordCount);}

That's better. But we still have state. It's not terribly much, but let's continue with the exercise. Notice how we rely on the state of `recordCount` to pass to `generateOutput`. What's to guarantee that the count we provide isn't different from the count of `file`? One possible direction to go is to move the `recordCount` calculation into `generateOutput`. Why should `generateOutput` trust someone else when it could just calculate it itself?

function  generateOutput(file)  {  // eliminate an argument that needed to be kept in sync  var  recordCount  =  file.lines().length();  // calculate it ourselves  for(var  c  in  file.lines())  {  print(c  +  ","  +  recordCount);  }}function  processFile()  {  // now our process is two steps  var  file  =  openFile("input.txt");  generateOutput(file);}

And now we don't need that little local variable called `file`.

function  processFile()  {  generateOutput(openFile("input.txt"));  // it can be written as one step}

### Conclusion

I've taken this simple example to an extreme. And, yes, this was a trivial example. But my experience with real world code tells me that **you see the same kind of improvements when you remove global mutable state in real systems**. The code becomes easier to reason about (because you're reasoning locally). It becomes easier to refactor. It becomes easier to eliminate code.

Reducing global mutable state is one of the hallmarks of functional programming. But it's also just *good* coding. You can (and should) do this kind of refactoring in any programming language or paradigm. If you're interested in going deeper with functional programming, I recommend the [PurelyFunctional.tv Newsletter](http://www.purelyfunctional.tv/newsletter/). It's a weekly email about Functional Programming, with a focus on Clojure. I'll also send you some great information about learning Clojure.

 [![ericnormand profile](../_resources/7700f3dc1ec1d8d1d2bac403233dea2b.jpg)](https://dev.to/ericnormand)

#### [Eric Normand](https://dev.to/ericnormand)

Eric Normand is a long time functional programmer, writer, and teacher. He teaches Clojure and Functional Programming at PurelyFunctional.tv.

 [![twitter](../_resources/82fc7d7179170bd29bf81d640a6cb697.png) ericnormand](http://twitter.com/ericnormand)  [![github](../_resources/43298f53fbd00b8582fd1a9a7adf1197.png) ericnormand](http://github.com/ericnormand)  [![link](../_resources/b5b447835a04fca6fe7559db1f40b440.png) purelyfunctional.tv](https://purelyfunctional.tv/)