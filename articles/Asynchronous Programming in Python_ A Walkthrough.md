Asynchronous Programming in Python: A Walkthrough

# Asynchronous Programming in Python: A Walkthrough

[David Bolton](https://insights.dice.com/author/dhbolton/)April 23, 20198 min read

**  [Asynchronous](https://insights.dice.com/tag/asynchronous/)[Programming](https://insights.dice.com/tag/programming/)[Python](https://insights.dice.com/tag/python/)

 ![shutterstock_544641280-1-750x500.jpg](../_resources/835601bdb78ac9c3350b9554b6ed9056.jpg)

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

When we talk about program execution, “asynchronous” means that the program doesn’t wait for a particular process to complete, but carries on regardless. An example of asynchronous programming is a program writing to a log file: Although it’s possible it might fail (for instance, because the log filled up the disk space), most times it doesn’t, and you can write your program to call the log routines asynchronously (or ‘fire and forget,’ as I call it).

Asynchronous execution means the main program runs a little faster. Your logging code should be written so that if it does fill the disk, it just stops logging rather than crashing.

Running asynchronous code usually involves threading if it’s a single core; with multi-core, it might get handled by another process running on a different core. A single core can only read one set of instructions at a time and execute. It’s like reading a book; you can only read one book at a time.

If you’re reading one book, and someone passes you another book, and you switch to that second book? That’s analogous to threaded execution. And if a group of you are reading books side-by-side? That’s multi-processing.

If you can overlap different speeds of processing in a single core (for example, computation plus reading a file from disk), then the single core appears to do both tasks simultaneously.  Or say you want to download web pages from four different sites; if each download runs in its own thread, then it will be much faster to fetch all four sites at the same time than fetching them one by one. Downloading web pages is a lot slower than calculations, so having many download at once can prove quite efficient.

### **Asynchronous [Python](https://www.dice.com/jobs/q-Python-jobs)**

Before asyncio (sometimes written as async IO), which is a concurrent programming design in [Python](https://insights.dice.com/2019/01/18/how-much-can-a-python-developer-make/), there were generator-based co-routines; [Python](https://www.dice.com/jobs/q-Python-jobs) 3.10 removes those. The asyncio module was added in Python 3.4, followed by async/await in 3.5.

Here are a couple of asynchronous concepts that you should get your head around: **coroutines** and **tasks**. Let’s look at coroutines first.

### **Coroutines**

A coroutine is usually a function with an *async *definition.  It can also be an object returned from a coroutine function.

By marking a function as *async*, it can be called with the *await*statement like ***await say_after(1, ‘hello’)***. What *await *means is that the program will run up to the await statement, call the function, and suspend execution until the function completes; other coroutines now get a chance to run.

That suspension of execution means that control is returned to the event loop. When you use asyncio, an event loop runs all the asynchronous tasks, performs network IO and runs sub-processes. For the most part, when you write coroutines, you will use tasks to run them.

### **Tasks**

Tasks let you run a coroutine in an event loop; that simplifies managing the execution of several coroutines. Here’s an example that uses coroutines and tasks; note that anything defined with *async def *is a coroutine. This example is from the official [Python documentation](https://docs.python.org/3.7/library/asyncio-task.html):

import asyncio
import time
async def say_after(delay, what):
await asyncio.sleep(delay)
print(what)
async def main():
task1 = asyncio.create_task(
say_after(1, 'hello'))
task2 = asyncio.create_task(
say_after(2, 'world'))
print(f"started at {time.strftime('%X')}")

# Wait until both tasks are completed (should take

# around 2 seconds.)

await task1
await task2
print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
.

The say_after() function has async as a prefix and thus is a coroutine. Forgetting the example above for one second, you could call the say_after() function directly like this:

await say_after(1, 'hello')
await say_after(2, 'world')
.

But that runs the coroutines sequentially and takes three seconds. The larger example above runs them concurrently, using a task for each, and they take two seconds. Note that defining a main() function isn’t enough. With main being async, It needs to be run by asyncio.

When you run the large example, you get this output; note the two-second difference between the times. If you run the smaller example, the difference will be three seconds.

started at 20:19:39
hello
world
finished at 20:19:41
.

### **Another Example**

This next example determines how many operations are done in calculating the sum of the first ten elements, though it does it backwards. It’s very inefficient, and I used a sleep call ogf 0.1 seconds per task to help timing.

It starts with 10 and calls itself on 9 and 8 and adds those. This is the total of 1 to 10 = 55.

import time
def fib(n):
global count
count=count+1
time.sleep(0.1)
if n > 1:
return fib(n-1) + fib(n-2)
return n
start=time.time()
global count
count = 0
result =fib(10)
print(result,count)
print(time.time()-start)
.

Next, I redo the same calculation using asyncio concurrency, and it uses a function asyncio.gather(), which here runs two tasks and waits until both have completed.

import asyncio,time
async def fib(n):
global count
count=count+1
time.sleep(0.1)
event_loop = asyncio.get_event_loop()
if n > 1:
task1 = asyncio.create_task(fib(n-1))
task2 = asyncio.create_task(fib(n-2))
await asyncio.gather(task1,task2)
return task1.result()+task2.result() return n
.

This takes slightly longer because it’s all running in one thread, and the create_tasks and gather, etc., adds a slight overhead. But it shows how you can start off several tasks concurrently and wait until they’re all finished.

### **Conclusion**

Tasks and coroutines have their uses; if there is a mix of I/O and computation or different computations, then you can quite happily run them together and reduce processing time by having things run concurrently rather than sequentially.

But, this doesn’t let you run many similar calculations at the same time. For that you need multiprocessing—the focus of a future article.

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

-

 ** *  ***

### Related

- [![shutterstock_544641280-300x200.jpg](../_resources/45f7f5a62d937833479e60fc5944e304.jpg)](https://insights.dice.com/2017/09/12/python-worlds-fastest-growing-programming-language/)

[Python: World's Fastest-Growing Programming Language?](https://insights.dice.com/2017/09/12/python-worlds-fastest-growing-programming-language/)

- [![shutterstock_544641280-1-300x200.jpg](../_resources/e7e9e01e28cbd8449d68d9026f3d9dd2.jpg)](https://insights.dice.com/2019/01/18/how-much-can-a-python-developer-make/)

[How Much Can a Python Developer Make?](https://insights.dice.com/2019/01/18/how-much-can-a-python-developer-make/)

- [![Developer-Interview-Homework-Dice-300x188.jpg](../_resources/878ed93491f19477f3c9c18cd5973f74.jpg)](https://insights.dice.com/2018/08/14/python-c-employers-demand-programming-languages/)

[Python, C Top Employers' Most In-Demand Programming Languages](https://insights.dice.com/2018/08/14/python-c-employers-demand-programming-languages/)