Memoization in JavaScript

# Memoization in JavaScript

## An introduction to memoization in JavaScript

 Published Mar 11, 2019

> Learning JavaScript? Download my free **> [> JavaScript Handbook](https://flaviocopes.com/page/ebooks/)**>

* * *

Memoization is one technique that lets you speed up considerably your applications.

It is not a technique unique to JavaScript, although I tagged this post as “JavaScript” because I will provide some JS examples.

Memoization is the act of storing the result of a function call after we run it, in the function itself. The next time we call the function, instead of performing its “regular” execution once again, it just returns us the stored result.

It’s **caching, for functions**.
Why is this useful?

Suppose our function takes 1 second to run, while caching lets us speed up the process to 2 milliseconds. There is a clear gain here.

Sounds pretty cool. Where is the catch?

Memoization works if the result of calling a function with the same set of arguments results in the same output. In other words, the function must be **pure**. Otherwise caching the result would not make sense.

So, database queries, network requests, writing to files and other non-pure operations cannot be optimized with memoization. For those, you will need to find other ways to optimize them. Or just live with their inefficiency, which sometimes is unavoidable.

Let’s create one example:

	// Calculate the factorial of num
	const fact = num => {
	  if (!fact.cache) {
	    fact.cache = {}
	  }
	  if (fact.cache[num] !== undefined) {
	    console.log(num + ' cached')
	    return fact.cache[num];
	  } else {
	    console.log(num + ' not cached')
	  }
	  fact.cache[num] = num === 0 ? 1 : num * fact(num - 1)
	  return fact.cache[num]
	}

calculating the factorial of a number. The first time `fact()` is run, it creates a `cache` object property on the function itself, where to store the result of its calculation.

Upon every call, if we don’t find the result of the number in the `cache` object, we perform the calculation. Otherwise we just return that.

Try to run it. I made a Codepen to make it easy to test, which uses `document.write()` to print to the HTML page (first time I used `document.write()` in ages, but this time it was useful).

- [JS](https://codepen.io/flaviocopes/embed/aMbbbP?height=419&theme-id=0&default-tab=js%2Cresult&user=flaviocopes&slug-hash=aMbbbP&pen-title=Memoization%20example%20factorial&name=cp_embed_1#js-box)

- [Result](https://codepen.io/flaviocopes/embed/aMbbbP?height=419&theme-id=0&default-tab=js%2Cresult&user=flaviocopes&slug-hash=aMbbbP&pen-title=Memoization%20example%20factorial&name=cp_embed_1#result-box)

 [EDIT ON![](data:image/svg+xml,%3csvg id='embed-codepen-logo' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 138 26' fill='none' stroke='%23000' stroke-width='2.3' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='11' class='js-evernote-checked'%3e %3cpath d='M80 6h-9v14h9 M114 6h-9 v14h9 M111 13h-6 M77 13h-6 M122 20V6l11 14V6 M22 16.7L33 24l11-7.3V9.3L33 2L22 9.3V16.7z M44 16.7L33 9.3l-11 7.4 M22 9.3l11 7.3 l11-7.3 M33 2v7.3 M33 16.7V24 M88 14h6c2.2 0 4-1.8 4-4s-1.8-4-4-4h-6v14 M15 8c-1.3-1.3-3-2-5-2c-4 0-7 3-7 7s3 7 7 7 c2 0 3.7-0.8 5-2 M64 13c0 4-3 7-7 7h-5V6h5C61 6 64 9 64 13z' data-evernote-id='34' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)](https://codepen.io/flaviocopes/pen/aMbbbP)

`// Calculate the factorial of num[[NEWLINE]]const fact = num => {[[NEWLINE]]  if (!fact.cache) {[[NEWLINE]]    fact.cache = {}[[NEWLINE]]  }[[NEWLINE]]  if (fact.cache[num] !== undefined) {[[NEWLINE]]    document.write(num + ' cached' + '<br>')[[NEWLINE]]    return fact.cache[num];[[NEWLINE]]  } else {[[NEWLINE]]    document.write(num + ' not cached' + '<br>')[[NEWLINE]]  }[[NEWLINE]]  fact.cache[num] = num === 0 ? 1 : num * fact(num - 1)[[NEWLINE]]  return fact.cache[num][[NEWLINE]]}[[NEWLINE]][[NEWLINE]]document.write(`Result #1: ${fact(4)} <br><br>`)[[NEWLINE]]document.write(`Result #2: ${fact(4)}`)`

4 not cached
3 not cached
2 not cached
1 not cached
0 not cached
Result #1: 24

4 cached
Result #2: 24

-
-
-

### External CSS

This Pen doesn't use any external CSS resources.

### External JavaScript

This Pen doesn't use any external JavaScript resources.

There are libraries that will add the memoization feature to any pure function, so you can skip the task of modifying the function itself, but you just decorate it with this functionality.

In particular I mention [fast-memoize](https://github.com/caiogondim/fast-memoize.js).

Lodash also has a [`memoize()` method](https://lodash.com/docs/4.17.11#memoize), if you are a Lodash fan.