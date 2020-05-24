How JavaScript works: Event loop and the rise of Async programming + 5 ways to better coding with…

# How JavaScript works: Event loop and the rise of Async programming + 5 ways to better coding with async/await

Welcome to post # 4 of the series dedicated to exploring JavaScript and its building components. In the process of identifying and describing the core elements, we also share some rules of thumb we use when building [SessionStack](https://www.sessionstack.com/), a JavaScript application that has to be robust and highly-performant in order to stay competitive.

Did you miss the first three chapters? You can find them here:

1. 1[An overview of the engine, the runtime, and the call stack](https://blog.sessionstack.com/how-does-javascript-actually-work-part-1-b0bacc073cf?source=collection_home---2------1----------------)

2. 2[Inside Google’s V8 engine + 5 tips on how to write optimized code](https://blog.sessionstack.com/how-javascript-works-inside-the-v8-engine-5-tips-on-how-to-write-optimized-code-ac089e62b12e?source=collection_home---2------2----------------)

3. 3[Memory management + how to handle 4 common memory leaks](https://blog.sessionstack.com/how-javascript-works-memory-management-how-to-handle-4-common-memory-leaks-3f28b94cfbec?source=collection_home---2------0----------------)

This time we’ll expand on our first post by reviewing the drawbacks to programming in a single-threaded environment and how to overcome them to build stunning JavaScript UIs. As the tradition goes, at the end of the article we’ll share 5 tips on how to write cleaner code with async/await.

#### **Why having a single thread is a limitation?**

In the [first post](https://blog.sessionstack.com/how-does-javascript-actually-work-part-1-b0bacc073cf) we launched, we pondered over the question *what happens when you have function calls in the Call Stack that take a huge amount of time to be processed*.

Imagine, for example, a complex image transformation algorithm that’s running in the browser.

While the Call Stack has functions to execute, the browser can’t do anything else — it’s being blocked. This means that the browser can’t render, it can’t run any other code, it’s just stuck. And here comes the problem — your app UI is no longer efficient and pleasing.

Your app **is stuck**.

In some cases, this might not be such a critical issue. But hey — here’s an even bigger problem. Once your browser starts processing too many tasks in the Call Stack, it may stop being responsive for a long time. At that point, a lot of browsers would take action by raising an error, asking whether they should terminate the page:

It’s ugly, and it completely ruins your UX:

![](../_resources/4ff2563a1354738e28cbe128219ff986.png)![1*MCt4ZC0dMVhJsgo1u6lpYw.jpeg](../_resources/a4f6b522304da4c47141450992997276.jpg)

#### **The building blocks of a JavaScript program**

You may be writing your JavaScript application in a single .js file, but your program is almost certainly comprised of several blocks, only one of which is going to execute *now*, and the rest will execute *later*. The most common block unit is the function.

The problem most developers new to JavaScript seem to have is understanding that *later* doesn’t necessarily happen strictly and immediately after *now*. In other words, tasks that cannot complete *now* are, by definition, going to complete asynchronously, which means you won’t have the above-mentioned blocking behavior as you might have subconsciously expected or hoped for.

Let’s take a look at the following example:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | // ajax(..) is some arbitrary Ajax function given by a library |
| 2   | var response =  ajax('https://example.com/api'); |
| 3   |     |
| 4   | console.log(response); |
| 5   | // `response` won't have the response |

 [view raw](https://gist.github.com/zlatkov/7a8b43e4fb8059bc810aa6aa4941148e/raw/720dc536574fb1bd7b7ed4073dca544dd907d637/sample1.js)  [sample1.js](https://gist.github.com/zlatkov/7a8b43e4fb8059bc810aa6aa4941148e#file-sample1-js) hosted with ❤ by [GitHub](https://github.com/)

You’re probably aware that standard Ajax requests don’t complete synchronously, which means that at the time of code execution the ajax(..) function does not yet have any value to return back to be assigned to a response variable.

A simple way of “waiting” for an asynchronous function to return its result is to use a function called **callback:**

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | ajax('https://example.com/api', function(response) { |
| 2   |  console.log(response); // `response` is now available |
| 3   | }); |

 [view raw](https://gist.github.com/zlatkov/cbd87df9ff2922512609a36d4155274a/raw/37264f186c51d5e5fbd8e48b3e4385518d4e1fc3/sample2.js)  [sample2.js](https://gist.github.com/zlatkov/cbd87df9ff2922512609a36d4155274a#file-sample2-js) hosted with ❤ by [GitHub](https://github.com/)

Just a note: you can actually make **synchronous** Ajax requests. Never, ever do that. If you make a synchronous Ajax request, the UI of your JavaScript app will be blocked — the user won’t be able to click, enter data, navigate, or scroll. This would prevent any user interaction. It’s a terrible practice.

This is how it looks like, but please, never do this — don’t ruin the web:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | // This is assuming that you're using jQuery |
| 2   | jQuery.ajax({ |
| 3   | url:  'https://api.example.com/endpoint', |
| 4   |  success:  function(response) { |
| 5   |  // This is your callback. |
| 6   | },  |
| 7   | async:  false  // And this is a terrible idea |
| 8   | }); |

 [view raw](https://gist.github.com/zlatkov/1b834ae5eb037f46347d71d4c497d43c/raw/2e16f80218d132ba250bee77a7dc6e5027dceaa5/sample3.js)  [sample3.js](https://gist.github.com/zlatkov/1b834ae5eb037f46347d71d4c497d43c#file-sample3-js) hosted with ❤ by [GitHub](https://github.com/)

We used an Ajax request just as an example. You can have any chunk of code execute asynchronously.

This can be done with the `setTimeout(callback, milliseconds)` function. What the `setTimeout` function does is to set up an event (a timeout) to happen later. Let’s take a look:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  first() { |
| 2   |  console.log('first'); |
| 3   | }   |
| 4   | function  second() { |
| 5   |  console.log('second'); |
| 6   | }   |
| 7   | function  third() { |
| 8   |  console.log('third'); |
| 9   | }   |
| 10  | first(); |
| 11  | setTimeout(second, 1000); // Invoke `second` after 1000ms |
| 12  | third(); |

 [view raw](https://gist.github.com/zlatkov/688a0b41ae10e45bd202d02bb12df264/raw/ff94a56e94a73882c192a70e0806ded04d4dfd37/sample4.js)  [sample4.js](https://gist.github.com/zlatkov/688a0b41ae10e45bd202d02bb12df264#file-sample4-js) hosted with ❤ by [GitHub](https://github.com/)

The output in the console will be the following:
first
third
second

#### **Dissecting the Event Loop**

We’ll start with a somewhat of an odd claim — despite allowing async JavaScript code (like the `setTimeout` we just discussed), until ES6, JavaScript itself has actually never had any direct notion of asynchrony built into it. The JavaScript engine has never done anything more than executing a single chunk of your program at any given moment.

For more details on how JavaScript engines work (Google’s V8 specifically), check one of our [previous articles](https://blog.sessionstack.com/how-javascript-works-inside-the-v8-engine-5-tips-on-how-to-write-optimized-code-ac089e62b12e) on the topic.

So, who tells the JS Engine to execute chunks of your program? In reality, the JS Engine doesn’t run in isolation — it runs inside a *hosting *environment, which for most developers is the typical web browser or Node.js. Actually, nowadays, JavaScript gets embedded into all kinds of devices, from robots to light bulbs. Every single device represents a different type of hosting environment for the JS Engine.

The common denominator in all environments is a built-in mechanism called the **event loop, **which handles the execution of multiple chunks of your program over time, each time invoking the JS Engine.

This means that the JS Engine is just an on-demand execution environment for any arbitrary JS code. It’s the surrounding environment that schedules the events (the JS code executions).

So, for example, when your JavaScript program makes an Ajax request to fetch some data from the server, you set up the “response” code in a function (the “callback”), and the JS Engine tells the hosting environment:

“Hey, I’m going to suspend execution for now, but whenever you finish with that network request, and you have some data, please *call* this function *back*.”

The browser is then set up to listen for the response from the network, and when it has something to return to you, it will schedule the callback function to be executed by inserting it into the *event loop*.

Let’s look at the below diagram:

![](:/b34415a5b02fadc5d2859af32d393f97)![1*FA9NGxNB6-v1oI2qGEtlRQ.png](../_resources/833fa9b4297875ee574ce9291e3690d1.png)

You can read more about the Memory Heap and the Call Stack in our [previous article](https://blog.sessionstack.com/how-does-javascript-actually-work-part-1-b0bacc073cf).

And what are these Web APIs? In essence, they are threads that you can’t access, you can just make calls to them. They are the pieces of the browser in which concurrency kicks in. If you’re a Node.js developer, these are the C++ APIs.

So what is the *event loop after all*?

![](../_resources/4295cf4bec283b20af7c2b2a2c3ea034.png)![1*KGBiAxjeD9JT2j6KDo0zUg.png](../_resources/cdb89b514d09d17ef33ed481da5f4b03.png)

The Event Loop has one simple job — to monitor the Call Stack and the Callback Queue. If the Call Stack is empty, it will take the first event from the queue and will push it to the Call Stack, which effectively runs it.

Such an iteration is called a **tick **in the Event Loop. Each event is just a function callback.

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | console.log('Hi'); |
| 2   | setTimeout(function  cb1() { |
| 3   |  console.log('cb1'); |
| 4   | }, 5000); |
| 5   | console.log('Bye'); |

 [view raw](https://gist.github.com/zlatkov/6d2e3006addd24cd73e5b576312a1c98/raw/40073efaac0baf8a6e7976f8bfea7cdc5d3b4b3b/sample5.js)  [sample5.js](https://gist.github.com/zlatkov/6d2e3006addd24cd73e5b576312a1c98#file-sample5-js) hosted with ❤ by [GitHub](https://github.com/)

Let’s “execute” this code and see what happens:

1. 1The state is clear. The browser console is clear, and the Call Stack is empty.

![](../_resources/b504fa47b688cab0970f95b39ef70dc0.png)![1*9fbOuFXJHwhqa6ToCc_v2A.png](../_resources/f2a18c376bc1deabed7a8893ec9c58a7.png)

2. `console.log('Hi')` is added to the Call Stack.

![](:/441f47028ec70804d0706fa95ffb7944)![1*dvrghQCVQIZOfNC27Jrtlw.png](../_resources/b91de8904afb76f99f55bc75eea33de5.png)

3. `console.log('Hi')` is executed.

![](../_resources/66bc91f673c503951860871d9618200f.png)![1*yn9Y4PXNP8XTz6mtCAzDZQ.png](../_resources/beaa0bea1f841ded68bb90d78eaef91b.png)

4. `console.log('Hi')` is removed from the Call Stack.

![](../_resources/8fbe6361934143f953c0e96c2230a7d9.png)![1*iBedryNbqtixYTKviPC1tA.png](../_resources/31819ca6031ca415b2212a3eb7fc25c3.png)

5. `setTimeout(function cb1() { ... })` is added to the Call Stack.

![](../_resources/6c915dad56f68b37ef6fc78c313cd5d6.png)![1*HIn-BxIP38X6mF_65snMKg.png](../_resources/040e935fe2abec466fb150af87087761.png)

6. `setTimeout(function cb1() { ... })` is executed. The browser creates a timer as part of the Web APIs. It is going to handle the countdown for you.

![](../_resources/238fb6b759b6c477f851cf722129c953.png)![1*vd3X2O_qRfqaEpW4AfZM4w.png](../_resources/84b728bd35e3bcadc1a8a0775ef78383.png)

7. The `setTimeout(function cb1() { ... })` itself is complete and is removed from the Call Stack.

![](../_resources/e0788ee4982f0170b4acac80aa12a622.png)![1*_nYLhoZPKD_HPhpJtQeErA.png](../_resources/f63f5e062e4fadb09f09fa6c8ca6dba8.png)

8. `console.log('Bye')` is added to the Call Stack.

![](../_resources/5d99f8b0cee942a9ae30a6679f61757f.png)![1*1NAeDnEv6DWFewX_C-L8mg.png](../_resources/54fe3141dfee31530c408867406937bb.png)

9. `console.log('Bye')` is executed.

![](../_resources/d7753b7ebf080d2433071681ea798017.png)![1*UwtM7DmK1BmlBOUUYEopGQ.png](../_resources/01efc6c8e3684ea4022eac5ed7a020af.png)

10. `console.log('Bye')` is removed from the Call Stack.

![](../_resources/2fcd15505473ab31971a06e07cd751de.png)![1*-vHNuJsJVXvqq5dLHPt7cQ.png](../_resources/a8cbd1f0f4f41aa2cee50e1e9fde2370.png)

11. After at least 5000 ms, the timer completes and it pushes the `cb1` callback to the Callback Queue.

![](../_resources/597a229087fcd35c4c3a17ef90b11192.png)![1*eOj6NVwGI2N78onh6CuCbA.png](../_resources/d17ed620c1d5c765673908714f8cbb25.png)

12. The Event Loop takes `cb1` from the Callback Queue and pushes it to the Call Stack.

![](../_resources/2703299ae4d427b497a3f198423c5c0f.png)![1*jQMQ9BEKPycs2wFC233aNg.png](../_resources/1ebbadaae06d29bd10fb4812ddb17818.png)

13. `cb1` is executed and adds `console.log('cb1')` to the Call Stack.

![](../_resources/034925f78f4721af5a3e3272fae41746.png)![1*hpyVeL1zsaeHaqS7mU4Qfw.png](../_resources/3df32e2f53bcd4f5ded5f1a9331e8c20.png)

14. `console.log('cb1')` is executed.

![](../_resources/0c6eb6f0902d2932ebd06ed0bcb05fb5.png)![1*lvOtCg75ObmUTOxIS6anEQ.png](../_resources/54d6ce0658204e9a897d492492be65ea.png)

15. `console.log('cb1')` is removed from the Call Stack.

![](../_resources/b8db5841b3af1927c03ac93bf7da0faa.png)![1*Jyyot22aRkKMF3LN1bgE-w.png](../_resources/10efa68ca1bd0a96d63226c2c078b2ba.png)

16. `cb1` is removed from the Call Stack.

![](../_resources/bfecfa46c4fbc5d03e2458bcccea2980.png)![1*t2Btfb_tBbBxTvyVgKX0Qg.png](../_resources/786822856bb749c888afcddce9ccc97a.png)

A quick recap:

![](../_resources/22701661095c00a7f4361356e0f45c4d.png)![1*TozSrkk92l8ho6d8JxqF_w.gif](../_resources/3baaa2030f404cf2375836958a3b2584.gif)

It’s interesting to note that ES6 specifies how the event loop should work, meaning that technically it’s within the scope of the JS engine’s responsibilities, which is no longer playing just a hosting environment role. One main reason for this change is the introduction of Promises in ES6 because the latter require access to a direct, fine-grained control over scheduling operations on the event loop queue (we’ll discuss them in a greater detail later).

#### How setTimeout(…) works

It’s important to note that `setTimeout(…)` doesn’t automatically put your callback on the event loop queue. It sets up a timer. When the timer expires, the environment places your callback into the event loop, so that some future tick will pick it up and execute it.Take a look at this code:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | setTimeout(myCallback, 1000); |

 [view raw](https://gist.github.com/zlatkov/9345a7c43b2407ddd1c52a6173a97dd9/raw/c4f093ba0b0acd40d7e9ea19f9dc8ad6e8ea9691/sample6.js)  [sample6.js](https://gist.github.com/zlatkov/9345a7c43b2407ddd1c52a6173a97dd9#file-sample6-js) hosted with ❤ by [GitHub](https://github.com/)

That doesn’t mean that `myCallback` will be executed in 1,000 ms but rather that, in 1,000 ms, `myCallback` will be added to the queue. The queue, however, might have other events that have been added earlier — your callback will have to wait.

There are quite a few articles and tutorials on getting started with async code in JavaScript that suggest doing a setTimeout(callback, 0). Well, now you know what the Event Loop does and how setTimeout works: calling setTimeout with 0 as a second argument just defers the callback until the Call Stack is clear.

Take a look at the following code:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | console.log('Hi'); |
| 2   | setTimeout(function() { |
| 3   |  console.log('callback'); |
| 4   | }, 0); |
| 5   | console.log('Bye'); |

 [view raw](https://gist.github.com/zlatkov/b12986d07676bc17fe51398847ebc917/raw/c52b71f76795c93d71b60723a9ac4322f335a9cd/sample7.js)  [sample7.js](https://gist.github.com/zlatkov/b12986d07676bc17fe51398847ebc917#file-sample7-js) hosted with ❤ by [GitHub](https://github.com/)

Although the wait time is set to 0 ms, the result in the browser console will be the following:

Hi
Bye
callback

#### What are Jobs in ES6 ?

A new concept called the “Job Queue” was introduced in ES6. It’s a layer on top of the Event Loop queue. You are most likely to bump into it when dealing with the asynchronous behavior of Promises (we’ll talk about them too).

We’ll just touch on the concept now so that when we discuss async behavior with Promises, later on, you understand how those actions are being scheduled and processed.

Imagine it like this: the Job Queue is a queue that’s attached to the end of every tick in the Event Loop queue. Certain async actions that may occur during a tick of the event loop will not cause a whole new event to be added to the event loop queue, but will instead add an item (aka Job) to the end of the current tick’s Job queue.

This means that you can add another functionality to be executed later, and you can rest assured that it will be executed right after, before anything else.

A Job can also cause more Jobs to be added to the end of the same queue. In theory, it’s possible for a Job “loop” (a Job that keeps adding other Jobs, etc.) to spin indefinitely, thus starving the program of the necessary resources needed to move on to the next event loop tick. Conceptually, this would be similar to just expressing a long-running or infinite loop (like `while (true)` ..) in your code.

Jobs are kind of like the `setTimeout(callback, 0)` “hack” but implemented in such a way that they introduce a much more well-defined and guaranteed ordering: later, but as soon as possible.

#### **Callbacks**

As you already know, callbacks are by far the most common way to express and manage asynchrony in JavaScript programs. Indeed, the callback is the most fundamental async pattern in the JavaScript language. Countless JS programs, even very sophisticated and complex ones, have been written on top of no other async foundation than the callback.

Except that callbacks don’t come with no shortcomings. Many developers are trying to find better async patterns. It’s impossible, however, to effectively use any abstraction if you don’t understand what’s actually under the hood.

In the following chapter, we’ll explore couple of these abstractions in depth to show why more sophisticated async patterns (that will be discussed in subsequent posts) are necessary and even recommended.

#### Nested Callbacks

Look at the following code:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | listen('click', function (e){ |
| 2   |  setTimeout(function(){ |
| 3   |  ajax('https://api.example.com/endpoint', function (text){ |
| 4   |  if (text ==  "hello") { |
| 5   |  doSomething(); |
| 6   | }   |
| 7   |  else  if (text ==  "world") { |
| 8   |  doSomethingElse(); |
| 9   | }   |
| 10  | }); |
| 11  | }, 500); |
| 12  | }); |

 [view raw](https://gist.github.com/zlatkov/cf5d201413729777fa6b8d5af1f8eaa4/raw/e6f6b0c1f1e4fc8b6cc39f44d1ce92df676e27e3/sample7.js)  [sample7.js](https://gist.github.com/zlatkov/cf5d201413729777fa6b8d5af1f8eaa4#file-sample7-js) hosted with ❤ by [GitHub](https://github.com/)

We’ve got a chain of three functions nested together, each one representing a step in an asynchronous series.

This kind of code is often called a “callback hell”. But the “callback hell” actually has almost nothing to do with the nesting/indentation. It’s a much deeper problem than that.

First, we’re waiting for the “click” event, then we’re waiting for the timer to fire, then we’re waiting for the Ajax response to come back, at which point it might get all repeated again.

At first glance, this code may seem to map its asynchrony naturally to sequential steps like:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | listen('click', function (e) { |
| 2   | // .. |
| 3   | }); |

 [view raw](https://gist.github.com/zlatkov/c279bb1865ad3a8ff8c890d842b105c1/raw/1b25b24fdc86cf5dae47ce64da26beca394cc5e2/sample8.js)  [sample8.js](https://gist.github.com/zlatkov/c279bb1865ad3a8ff8c890d842b105c1#file-sample8-js) hosted with ❤ by [GitHub](https://github.com/)

Then we have:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | setTimeout(function(){ |
| 2   |  // .. |
| 3   | }, 500); |

 [view raw](https://gist.github.com/zlatkov/8c9c5601ba6b35adf652b7a6797d1a14/raw/3fca364a6cc8d579a7534aa54e0ec68352bdabd3/sample9.js)  [sample9.js](https://gist.github.com/zlatkov/8c9c5601ba6b35adf652b7a6797d1a14#file-sample9-js) hosted with ❤ by [GitHub](https://github.com/)

Then later we have:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | ajax('https://api.example.com/endpoint', function (text){ |
| 2   |  // .. |
| 3   | }); |

 [view raw](https://gist.github.com/zlatkov/250ccf280b4f191f87bca3a0b8337a41/raw/b043f82671306ebb97a7d44ef68b331f119b295a/sample10.js)  [sample10.js](https://gist.github.com/zlatkov/250ccf280b4f191f87bca3a0b8337a41#file-sample10-js) hosted with ❤ by [GitHub](https://github.com/)

And finally:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | if (text ==  "hello") { |
| 2   |  doSomething(); |
| 3   | }   |
| 4   | else  if (text ==  "world") { |
| 5   |  doSomethingElse(); |
| 6   | }   |

 [view raw](https://gist.github.com/zlatkov/6dc48448f85e010542ac9ba86482f38d/raw/62c971bbed2b5650ec636b5fbd9f96a817b130fa/sample11.js)  [sample11.js](https://gist.github.com/zlatkov/6dc48448f85e010542ac9ba86482f38d#file-sample11-js) hosted with ❤ by [GitHub](https://github.com/)

So, such a sequential way of expressing your async code seems a lot more natural, doesn’t it? There must be such a way, right?

#### Promises

Take a look at the following code:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | var x =  1; |
| 2   | var y =  2; |
| 3   | console.log(x + y); |

 [view raw](https://gist.github.com/zlatkov/bf8888880822b83e4a9c1bfc4b21c6a9/raw/11b03ba69499c2ffed347d8e1fe5a262373a0ac3/sample12.js)  [sample12.js](https://gist.github.com/zlatkov/bf8888880822b83e4a9c1bfc4b21c6a9#file-sample12-js) hosted with ❤ by [GitHub](https://github.com/)

It’s all very straightforward: it sums the values of `x` and `y` and prints it to the console. What if, however, the value of `x` or `y `was missing and was still to be determined? Say, we need to retrieve the values of both `x` and `y` from the server, before they can be used in the expression. Let’s imagine that we have a function `loadX` and `loadY` that respectively load the values of `x` and `y` from the server. Then, imagine that we have a function `sum` that sums the values of `x` and `y` once both of them are loaded.

It could look like this (quite ugly, isn’t it):

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  sum(getX, getY, callback) { |
| 2   |  var x, y; |
| 3   |  getX(function(result) { |
| 4   | x = result; |
| 5   |  if (y !==  undefined) { |
| 6   |  callback(x + y); |
| 7   | }   |
| 8   | }); |
| 9   |  getY(function(result) { |
| 10  | y = result; |
| 11  |  if (x !==  undefined) { |
| 12  |  callback(x + y); |
| 13  | }   |
| 14  | }); |
| 15  | }   |
| 16  | // A sync or async function that retrieves the value of `x` |
| 17  | function  fetchX() { |
| 18  |  // .. |
| 19  | }   |
| 20  |     |
| 21  |     |
| 22  | // A sync or async function that retrieves the value of `y` |
| 23  | function  fetchY() { |
| 24  |  // .. |
| 25  | }   |
| 26  | sum(fetchX, fetchY, function(result) { |
| 27  |  console.log(result); |
| 28  | }); |

 [view raw](https://gist.github.com/zlatkov/1ffa6e00a2750217f1a168fe36deda08/raw/b989e84216145a442806af4d6237a39edfe96eb3/sample13.js)  [sample13.js](https://gist.github.com/zlatkov/1ffa6e00a2750217f1a168fe36deda08#file-sample13-js) hosted with ❤ by [GitHub](https://github.com/)

There is something very important here — in that snippet, we treated `x` and `y` as **future** values, and we expressed an operation `sum(…)` that (from the outside) did not care whether `x` or `y` or both were or weren’t available right away.

Of course, this rough callbacks-based approach leaves much to be desired. It’s just a first tiny step towards understanding the benefits of reasoning about *future values* without worrying about the time aspect of when they will be available.

#### Promise Value

Let’s just briefly glimpse at how we can express the` x + y` example with Promises:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  sum(xPromise, yPromise) { |
| 2   | // `Promise.all([ .. ])` takes an array of promises, |
| 3   | // and returns a new promise that waits on them |
| 4   | // all to finish |
| 5   | return  Promise.all([xPromise, yPromise]) |
| 6   |     |
| 7   | // when that promise is resolved, let's take the |
| 8   | // received `X` and `Y` values and add them together. |
| 9   | .then(function(values){ |
| 10  | // `values` is an array of the messages from the |
| 11  | // previously resolved promises |
| 12  | return values[0] + values[1]; |
| 13  | } ); |
| 14  | }   |
| 15  |     |
| 16  | // `fetchX()` and `fetchY()` return promises for |
| 17  | // their respective values, which may be ready |
| 18  | // *now* or *later*. |
| 19  | sum(fetchX(), fetchY()) |
| 20  |     |
| 21  | // we get a promise back for the sum of those |
| 22  | // two numbers. |
| 23  | // now we chain-call `then(...)` to wait for the |
| 24  | // resolution of that returned promise. |
| 25  | .then(function(sum){ |
| 26  |  console.log(sum); |
| 27  | }); |

 [view raw](https://gist.github.com/zlatkov/e7098be769383bac5336c54d952beb53/raw/8e505228f4fa6864de32344aac45ebec7b5a8991/sample14.js)  [sample14.js](https://gist.github.com/zlatkov/e7098be769383bac5336c54d952beb53#file-sample14-js) hosted with ❤ by [GitHub](https://github.com/)

There are two layers of Promises in this snippet.

`fetchX()` and `fetchY()` are called directly, and the values they return (promises!) are passed to `sum(...)`. The underlying values these promises represent may be ready *now* or *later*, but each promise normalizes its behavior to be the same regardless. We reason about `x` and `y` values in a time-independent way. They are *future values*, period.

The second layer is the promise that `sum(...)` creates

(via `Promise.all([ ... ])`) and returns, which we wait on by calling `then(...)`. When the `sum(...)`operation completes, our sum *future value* is ready and we can print it out. We hide the logic for waiting on the `x` and `y`  *future values* inside of `sum(...)` .

**Note**: Inside `sum(…)`, the `Promise.all([ … ])` call creates a promise (which is waiting on `promiseX` and `promiseY` to resolve). The chained call to `.then(...) `creates another promise, which the return

`values[0] + values[1]` line immediately resolves (with the result of the addition). Thus, the `then(...)` call we chain off the end of the `sum(...)` call — at the end of the snippet — is actually operating on that second promise returned, rather than the first one created by `Promise.all([ ... ])`. Also, although we are not chaining off the end of that second `then(...)`, it too has created another promise, had we chosen to observe/use it. This Promise chaining stuff will be explained in much greater detail later in this chapter.

With Promises, the `then(...)` call can actually take two functions, the first for fulfillment (as shown earlier), and the second for rejection:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | sum(fetchX(), fetchY()) |
| 2   | .then( |
| 3   |  // fullfillment handler |
| 4   |  function(sum) { |
| 5   |  console.log( sum ); |
| 6   | },  |
| 7   |  // rejection handler |
| 8   |  function(err) { |
| 9   | console.error( err ); // bummer! |
| 10  | }   |
| 11  | );  |

 [view raw](https://gist.github.com/zlatkov/33582dc127209706688796092e268772/raw/6edc6692b92d178804b4a499f9a6c8d3b3528d2a/sample15.js)  [sample15.js](https://gist.github.com/zlatkov/33582dc127209706688796092e268772#file-sample15-js) hosted with ❤ by [GitHub](https://github.com/)

If something went wrong when getting `x` or `y`, or something somehow failed during the addition, the promise that `sum(...) `returns would be rejected, and the second callback error handler passed to `then(...)` would receive the rejection value from the promise.

Because Promises encapsulate the time-dependent state — waiting on the fulfillment or rejection of the underlying value — from the outside, the Promise itself is time-independent, and thus Promises can be composed (combined) in predictable ways regardless of the timing or outcome underneath.

Moreover, once a Promise is resolved, it stays that way forever — it becomes an *immutable value* at that point — and can then be *observed* as many times as necessary.

It’s really useful that you can actually chain promises:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  delay(time) { |
| 2   |  return  new  Promise(function(resolve, reject){ |
| 3   |  setTimeout(resolve, time); |
| 4   | }); |
| 5   | }   |
| 6   |     |
| 7   | delay(1000) |
| 8   | .then(function(){ |
| 9   |  console.log("after 1000ms"); |
| 10  |  return  delay(2000); |
| 11  | })  |
| 12  | .then(function(){ |
| 13  |  console.log("after another 2000ms"); |
| 14  | })  |
| 15  | .then(function(){ |
| 16  |  console.log("step 4 (next Job)"); |
| 17  |  return  delay(5000); |
| 18  | })  |
| 19  | // ... |

 [view raw](https://gist.github.com/zlatkov/f94c8e16cbbb8b8940744b348c70de14/raw/c2d43e2f3ff27b964f5d9ff7e5ef3efcf07c6336/sample16.js)  [sample16.js](https://gist.github.com/zlatkov/f94c8e16cbbb8b8940744b348c70de14#file-sample16-js) hosted with ❤ by [GitHub](https://github.com/)

Calling `delay(2000)` creates a promise that will fulfill in 2000ms, and then we return that from the first `then(...)` fulfillment callback, which causes the second `then(...)`'s promise to wait on that 2000ms promise.

**Note**: Because a Promise is externally immutable once resolved, it’s now safe to pass that value around to any party, knowing that it cannot be modified accidentally or maliciously. This is especially true in relation to multiple parties observing the resolution of a Promise. It’s not possible for one party to affect another party’s ability to observe Promise resolution. Immutability may sound like an academic topic, but it’s actually one of the most fundamental and important aspects of Promise design, and shouldn’t be casually passed over.

#### **To Promise or not to Promise?**

An important detail about Promises is knowing for sure if some value is an actual Promise or not. In other words, is it a value that will behave like a Promise?

We know that Promises are constructed by the `new Promise(…)` syntax, and you might think that `p instanceof Promise` would be a sufficient check. Well, not quite.

Mainly because you can receive a Promise value from another browser window (e.g. iframe), which would have its own Promise, different from the one in the current window or frame, and that check would fail to identify the Promise instance.

Moreover, a library or framework may choose to vend its own Promises and not use the native ES6 Promise implementation to do so. In fact, you may very well be using Promises with libraries in older browsers that have no Promise at all.

#### Swallowing exceptions

If at any point in the creation of a Promise, or in the observation of its resolution, a JavaScript exception error occurs, such as a `TypeError` or `ReferenceError`, that exception will be caught, and it will force the Promise in question to become rejected.

For example:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | var p =  new  Promise(function(resolve, reject){ |
| 2   |  foo.bar(); // `foo` is not defined, so error! |
| 3   |  resolve(374); // never gets here :( |
| 4   | }); |
| 5   |     |
| 6   | p.then( |
| 7   |  function  fulfilled(){ |
| 8   |  // never gets here :( |
| 9   | },  |
| 10  |  function  rejected(err){ |
| 11  |  // `err` will be a `TypeError` exception object |
| 12  | // from the `foo.bar()` line. |
| 13  | }   |
| 14  | );  |

 [view raw](https://gist.github.com/zlatkov/ba13f1f0a37b0156417bc389785d37ea/raw/6e2845fdd627812bbc90e2b5e3c8c83218acdbdc/sample17.js)  [sample17.js](https://gist.github.com/zlatkov/ba13f1f0a37b0156417bc389785d37ea#file-sample17-js) hosted with ❤ by [GitHub](https://github.com/)

But what happens if a Promise is fulfilled yet there was a JS exception error during the observation (in a `then(…)` registered callback)? Even though it won’t be lost, you may find the way they’re handled a bit surprising. Until you dig a little deeper:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | var p =  new  Promise( function(resolve,reject){ |
| 2   | resolve(374); |
| 3   | }); |
| 4   |     |
| 5   | p.then(function  fulfilled(message){ |
| 6   |  foo.bar(); |
| 7   |  console.log(message); // never reached |
| 8   | },  |
| 9   |  function  rejected(err){ |
| 10  |  // never reached |
| 11  | }   |
| 12  | );  |

 [view raw](https://gist.github.com/zlatkov/2ab398f4d3eeccb80556de844de2cd92/raw/781b2bfdb4479d22a5582ff3565066cb0a8cee17/sample18.js)  [sample18.js](https://gist.github.com/zlatkov/2ab398f4d3eeccb80556de844de2cd92#file-sample18-js) hosted with ❤ by [GitHub](https://github.com/)

It looks like the exception from `foo.bar()` really did get swallowed. It wasn’t, though. There was something deeper that went wrong, however, which we failed to listen for. The `p.then(…)` call itself returns another promise, and it’s that*  *promise that will be rejected with the `TypeError` exception.

#### **Handling uncaught exceptions**

There are other approaches which many would say are *better*.

A common suggestion is that Promises should have a `done(…)` added to them, which essentially marks the Promise chain as “done.” `done(…)`doesn’t create and return a Promise, so the callbacks passed to `done(..)` are obviously not wired up to report problems to a chained Promise that doesn’t exist.

It’s treated as you might usually expect in uncaught error conditions: any exception inside a `done(..)` rejection handler would be thrown as a global uncaught error (in the developer console, basically):

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | var p =  Promise.resolve(374); |
| 2   |     |
| 3   | p.then(function  fulfilled(msg){ |
| 4   |  // numbers don't have string functions, |
| 5   |  // so will throw an error |
| 6   |  console.log(msg.toLowerCase()); |
| 7   | })  |
| 8   | .done(null, function() { |
| 9   |  // If an exception is caused here, it will be thrown globally |
| 10  | }); |

 [view raw](https://gist.github.com/zlatkov/ae156463adf288ca0ac9da9e8964fa18/raw/d6df62c95f5191c8d5b86f2b81c8264415a916e5/sample19.js)  [sample19.js](https://gist.github.com/zlatkov/ae156463adf288ca0ac9da9e8964fa18#file-sample19-js) hosted with ❤ by [GitHub](https://github.com/)

#### **What’s happening in ES8? Async/await**

JavaScript ES8 introduced `async/await`*  *that makes the job of working with Promises easier. We’ll briefly go through the possibilities `async/await` offers and how to leverage them to write async code.

So, let’s see how async/await works.

You define an asynchronous function using the `async` function declaration. Such functions return an [AsyncFunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction) object. The `AsyncFunction` object represents the asynchronous function which executes the code, contained within that function.

When an async function is called, it returns a `Promise` . When the async function returns a value, that’s not a `Promise` , a `Promise` will be automatically created and it will be resolved with the returned value from the function. When the `async` function throws an exception, the `Promise` will be rejected with the thrown value.

An `async` function can contain an `await` expression, that pauses the execution of the function and waits for the passed Promise’s resolution, and then resumes the async function’s execution and returns the resolved value.

You can think of a `Promise` in JavaScript as the equivalent of Java’s `Future` or `C#`'s Task.

> The purpose of `async/await`>  is to simplify the behavior of using promises.
Let’s take a look at the following example:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | // Just a standard JavaScript function |
| 2   | function  getNumber1() { |
| 3   |  return  Promise.resolve('374'); |
| 4   | }   |
| 5   | // This function does the same as getNumber1 |
| 6   | async  function  getNumber2() { |
| 7   |  return  374; |
| 8   | }   |

 [view raw](https://gist.github.com/zlatkov/8f74044b900d1ea4d365ca3992b50ea3/raw/98b53c07c22ac23ccc559f488c79c55510364399/sample20.js)  [sample20.js](https://gist.github.com/zlatkov/8f74044b900d1ea4d365ca3992b50ea3#file-sample20-js) hosted with ❤ by [GitHub](https://github.com/)

Similarly, functions that are throwing exceptions are equivalent to functions which return promises that have been rejected:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  f1() { |
| 2   |  return  Promise.reject('Some error'); |
| 3   | }   |
| 4   | async  function  f2() { |
| 5   |  throw  'Some error'; |
| 6   | }   |

 [view raw](https://gist.github.com/zlatkov/159929de0c27b2ddfc9c8e100ce51b43/raw/46dc76748d068f399b50f004edbf727f0c755405/sample21.js)  [sample21.js](https://gist.github.com/zlatkov/159929de0c27b2ddfc9c8e100ce51b43#file-sample21-js) hosted with ❤ by [GitHub](https://github.com/)

The `await` keyword can only be used in `async` functions and allows you to synchronously wait on a Promise. If we use promises outside of an `async` function, we’ll still have to use `then` callbacks:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | async  function  loadData() { |
| 2   |  // `rp` is a request-promise function. |
| 3   |  var promise1 =  rp('https://api.example.com/endpoint1'); |
| 4   |  var promise2 =  rp('https://api.example.com/endpoint2'); |
| 5   |     |
| 6   |  // Currently, both requests are fired, concurrently and |
| 7   |  // now we'll have to wait for them to finish |
| 8   |  var response1 =  await promise1; |
| 9   |  var response2 =  await promise2; |
| 10  |  return response1 +  '  '  + response2; |
| 11  | }   |
| 12  | // Since, we're not in an `async function` anymore |
| 13  | // we have to use `then`. |
| 14  | loadData().then(() =>  console.log('Done')); |

 [view raw](https://gist.github.com/zlatkov/448a79cab54330c062a13a84ebb06cf7/raw/0195eb1ab60225dabf111adffcf14702466e6fe6/sample22.js)  [sample22.js](https://gist.github.com/zlatkov/448a79cab54330c062a13a84ebb06cf7#file-sample22-js) hosted with ❤ by [GitHub](https://github.com/)

You can also define async functions using an “async function expression”. An async function expression is very similar to and has almost the same syntax as, an async function statement. The main difference between an async function expression and an async function statement is the function name, which can be omitted in async function expressions to create anonymous functions. An async function expression can be used as an IIFE (Immediately Invoked Function Expression) which runs as soon as it is defined.

It looks like this:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | var  loadData  =  async  function() { |
| 2   |  // `rp` is a request-promise function. |
| 3   |  var promise1 =  rp('https://api.example.com/endpoint1'); |
| 4   |  var promise2 =  rp('https://api.example.com/endpoint2'); |
| 5   |     |
| 6   |  // Currently, both requests are fired, concurrently and |
| 7   |  // now we'll have to wait for them to finish |
| 8   |  var response1 =  await promise1; |
| 9   |  var response2 =  await promise2; |
| 10  |  return response1 +  '  '  + response2; |
| 11  | }   |

 [view raw](https://gist.github.com/zlatkov/0873db2fd9f5883a2e1bae414e43a5cc/raw/34f619ddd8f5d4066905d3a5bc642d8f2cd8c345/sample23.js)  [sample23.js](https://gist.github.com/zlatkov/0873db2fd9f5883a2e1bae414e43a5cc#file-sample23-js) hosted with ❤ by [GitHub](https://github.com/)

More importantly, async/await is supported in all major browsers:

![](../_resources/514f8275c78e53f49c76dcf9232f0dee.png)![0*z-A-JIe5OWFtgyd2..png](../_resources/4cf024b4b74826a5ffe3d525196ef8d7.png)

If this compatibility is not what you are after, there are also several JS transpilers like [Babel](https://babeljs.io/docs/plugins/transform-async-to-generator/) and [TypeScript.](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-3.html)

At the end of the day, the important thing is not to blindly choose the “latest” approach to writing async code. It’s essential to understand the internals of async JavaScript, learn why it’s so critical and comprehend in-depth the internals of the method you have chosen. Every approach has pros and cons as with everything else in programming.

### 5 Tips on writing highly maintainable, non-brittle async code

1. 1**Clean code: **Using async/await allows you to write a lot less code. Every time you use async/await you skip a few unnecessary steps: write .then, create an anonymous function to handle the response, name the response from that callback e.g.

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | // `rp` is a request-promise function. |
| 2   | rp(‘https://api.example.com/endpoint1').then(function(data) { |
| 3   |  // … |
| 4   | }); |

 [view raw](https://gist.github.com/zlatkov/b66f922b26bb6d5fd701c7ba40ac81d7/raw/47e41ce5cd939a73a6050c9d7fd76952d0a6b350/sample24.js)  [sample24.js](https://gist.github.com/zlatkov/b66f922b26bb6d5fd701c7ba40ac81d7#file-sample24-js) hosted with ❤ by [GitHub](https://github.com/)

Versus:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | // `rp` is a request-promise function. |
| 2   | var response =  await  rp(‘https://api.example.com/endpoint1'); |

 [view raw](https://gist.github.com/zlatkov/f506c8de2c73ba1c4c9ec78c5871816c/raw/f6dedc67d53349f65b33f12015ec1823b251a831/sample25.js)  [sample25.js](https://gist.github.com/zlatkov/f506c8de2c73ba1c4c9ec78c5871816c#file-sample25-js) hosted with ❤ by [GitHub](https://github.com/)

2. **Error handling: **Async/await makes it possible to handle both sync and async errors with the same code construct — the well-known try/catch statements. Let’s see how it looks with Promises:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  loadData() { |
| 2   |  try { // Catches synchronous errors. |
| 3   |  getJSON().then(function(response) { |
| 4   |  var parsed =  JSON.parse(response); |
| 5   |  console.log(parsed); |
| 6   | }).catch(function(e) { // Catches asynchronous errors |
| 7   |  console.log(e); |
| 8   | }); |
| 9   | } catch(e) { |
| 10  |  console.log(e); |
| 11  | }   |
| 12  | }   |

 [view raw](https://gist.github.com/zlatkov/c5fc0706d2d37ce3bb9db75e8a991807/raw/f93f3f2f9c9029cfee73525da4e84c4bc481d729/sample26.js)  [sample26.js](https://gist.github.com/zlatkov/c5fc0706d2d37ce3bb9db75e8a991807#file-sample26-js) hosted with ❤ by [GitHub](https://github.com/)

Versus:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | async  function  loadData() { |
| 2   |  try { |
| 3   |  var data =  JSON.parse(await  getJSON()); |
| 4   |  console.log(data); |
| 5   | } catch(e) { |
| 6   |  console.log(e); |
| 7   | }   |
| 8   | }   |

 [view raw](https://gist.github.com/zlatkov/1f858a186da7d19fab77893e34e46adc/raw/1c276afa375dae4b99b208d3f2960d0d3dcf2608/sample27.js)  [sample27.js](https://gist.github.com/zlatkov/1f858a186da7d19fab77893e34e46adc#file-sample27-js) hosted with ❤ by [GitHub](https://github.com/)

3.** Conditionals: **Writing conditional code with `async/await` is a lot more straightforward:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  loadData() { |
| 2   |  return  getJSON() |
| 3   | .then(function(response) { |
| 4   |  if (response.needsAnotherRequest) { |
| 5   |  return  makeAnotherRequest(response) |
| 6   | .then(function(anotherResponse) { |
| 7   |  console.log(anotherResponse) |
| 8   |  return anotherResponse |
| 9   | })  |
| 10  | } else { |
| 11  |  console.log(response) |
| 12  |  return response |
| 13  | }   |
| 14  | })  |
| 15  | }   |

 [view raw](https://gist.github.com/zlatkov/30e8c04023639ed289a5d107b6989269/raw/7fb45ff5b3de6274bcdf83ea9a9cb36c8ccc8482/sample28.js)  [sample28.js](https://gist.github.com/zlatkov/30e8c04023639ed289a5d107b6989269#file-sample28-js) hosted with ❤ by [GitHub](https://github.com/)

Versus:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | async  function  loadData() { |
| 2   |  var response =  await  getJSON(); |
| 3   |  if (response.needsAnotherRequest) { |
| 4   |  var anotherResponse =  await  makeAnotherRequest(response); |
| 5   |  console.log(anotherResponse) |
| 6   |  return anotherResponse |
| 7   | } else { |
| 8   |  console.log(response); |
| 9   |  return response; |
| 10  | }   |
| 11  | }   |

 [view raw](https://gist.github.com/zlatkov/3dea9285325304af9a73aceb3beb6742/raw/596cedb0e8b5e084520427932dc684bad0cdc8b4/sample29.js)  [sample29.js](https://gist.github.com/zlatkov/3dea9285325304af9a73aceb3beb6742#file-sample29-js) hosted with ❤ by [GitHub](https://github.com/)

4. **Stack Frames: **Unlike with `async/await`, the error stack returned from a promise chain gives no clue of where the error happened. Look at the following:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | function  loadData() { |
| 2   |  return  callAPromise() |
| 3   | .then(callback1) |
| 4   | .then(callback2) |
| 5   | .then(callback3) |
| 6   | .then(() => { |
| 7   |  throw  new  Error("boom"); |
| 8   | })  |
| 9   | }   |
| 10  | loadData() |
| 11  | .catch(function(e) { |
| 12  |  console.log(err); |
| 13  | // Error: boom at callAPromise.then.then.then.then (index.js:8:13) |
| 14  | }); |

 [view raw](https://gist.github.com/zlatkov/8e728cc4d6ad1e302454e957fcce0580/raw/cc561786c14cedd3a9ce4dc10e47d515cf8ce758/sample30.js)  [sample30.js](https://gist.github.com/zlatkov/8e728cc4d6ad1e302454e957fcce0580#file-sample30-js) hosted with ❤ by [GitHub](https://github.com/)

Versus:

![](../_resources/ead493f58fc1ec8316f8e337eb7aeba5.png)

|     |     |
| --- | --- |
| 1   | async  function  loadData() { |
| 2   |  await  callAPromise1() |
| 3   |  await  callAPromise2() |
| 4   |  await  callAPromise3() |
| 5   |  await  callAPromise4() |
| 6   |  await  callAPromise5() |
| 7   |  throw  new  Error("boom"); |
| 8   | }   |
| 9   | loadData() |
| 10  | .catch(function(e) { |
| 11  |  console.log(err); |
| 12  |  // output |
| 13  |  // Error: boom at loadData (index.js:7:9) |
| 14  | }); |

 [view raw](https://gist.github.com/zlatkov/7282966e52cab3eee85794d5e8df6928/raw/fa6fb95f97335fba33539ba3deba1a4c806e9328/sample31.js)  [sample31.js](https://gist.github.com/zlatkov/7282966e52cab3eee85794d5e8df6928#file-sample31-js) hosted with ❤ by [GitHub](https://github.com/)

5. **Debugging: **If you have used promises, you know that debugging them is a nightmare. For example, if you set a breakpoint inside a .then block and use debug shortcuts like “stop-over”, the debugger will not move to the following .then because it only “steps” through synchronous code.

With `async/await` you can step through await calls exactly as if they were normal synchronous functions.

Writing **async JavaScript code is important** not only for the apps themselves but **for libraries as well**.

For example, the [SessionStack](https://www.sessionstack.com/) library records everything in your web app/website: all DOM changes, user interactions, JavaScript exceptions, stack traces, failed network requests, and debug messages.

And this all has to happen in your production environment without impacting any of the UX. We need to heavily optimize our code and make it asynchronous as much as possible so that we can increase the number of events that are being processed by the Event Loop.

And not just the library! When you replay a user session in SessionStack, we have to render everything that happened in your user’s browser at the time the problem occurred, and we have to reconstruct the whole state, allowing you to jump back and forth in the session timeline. In order to make this possible, we’re heavily employing the async opportunities that JavaScript provides.

There is a free plan that allows you to [get started for free](https://www.sessionstack.com/signup/).

![](../_resources/1020b4839a03cb7f54baafe1ccd60df8.png)![0*xSEaWHGqqlcF8g5H..png](../_resources/4dbd0d1e880f63eb7081bca449375023.png)

Resources:

- •https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch2.md
- •https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch3.md
- •http://nikgrozev.com/2017/10/01/async-await/