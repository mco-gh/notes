Getting started with Python testing

# Getting started with Python testing

**>

> “People also underestimate the time they spend debugging. They underestimate how much time they can spend chasing a long bug. With testing, I know straight away when I added a bug. That lets me fix the bug immediately, before it can crawl off and hide.” – Martin Fowler

**

Testing your code is a common practice that I feel requires more attention. During my degree there was a period where unit tests were emphasized as an appropriate thing to do, and other times where they were completely ignored. Similarly, during my high school years I competed in a number of programming competitions, often over a number of weeks where the solutions I was producing was being marked against some test but I was only manually testing my code before having it marked. While testing is brought up in high school curriculums as well as university, I believe it is generally only discussed as an idea and not actually implemented in class. The aim of this post is to give you a general introduction to how we might be able to test a function in Python 3.

## Our Plan

There is a process used in the software industry called [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) or TDD for short. While it’s not always followed, it does provide a nice way of developing software small and large. Simply stated, TDD requires the developer to write their tests first, and then write the actual product code. Today, I will demonstrate this practice in this blog post.

## The Problem Space

I have decided to pick a non-trivial problem for this demonstration, writing a function that returns the nth [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number). While this function is not particularly difficult to implement, I have chosen it so that people of all experience levels can follow along.

The Fibonacci sequence begins as follows:
`1, 1, 2, 3, 5, 8, 13, 21, ...`

where we start with the numbers `1, 1` and then get the next number in the sequence by adding the two previous numbers together. For example, the next number in our example after `21` would be `13 + 21 = 34`.

## Initial Requirements

When we approach a problem that requires tests, we need to come up with some requirements that we want to test are satisfied. Looking at the fibonacci sequence we have a few requirements, namely:

1. When we pass the function some number `n` we expect it to return the number that is in position `n` in the sequence, with the zeroth number being `1`.

2. Our function should raise a `ValueError` if we pass in a number less than `0` because it makes no sense to have anything before the zeroth position in the sequence.

## Our First Test

I use [pytest](https://docs.pytest.org/en/latest/) when writing tests as I find it produces nice output and together with a number of plugins can lead to a very enjoyable testing experience. Using `pip` you can install pytest from the command line:

`pip install pytest`

Testing in Python doesn’t strictly require pytest but I find it makes testing a lot nicer.

Now opening a new file called `test_fibonacci.py` we can begin writing our tests. I like to start by importing `TestCase` from the `unittest` module included in the Python standard library:

	from unittest import TestCase

This class will allow us to write subclasses to test different parts of our code, in this tutorial we will only write one. You can also write individual tests as functions as shown on the [pytest homepage](https://docs.pytest.org/en/latest/) however by writing your tests as classes you can group your tests in a more pleasing fashion. To begin with, lets create a `FibonacciTests` class:

	from unittest import TestCase

	class FibonacciTests(TestCase):
	    pass

This snippet has created a new class that gives us all the utilities available to [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase) which we will cover as we go. Now to write some tests, `unittest` requires that we write our method names begining with `test`. The first test we will write is to check our first condition, that the fibonacci function will return the correct fibonacci number at the position. Our first test looks something like this:

	from unittest import TestCase

	class FibonacciTests(TestCase):
	    def test_returns_correct_fibonacci_number(self):
	        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	        for index in range(len(correct_sequence)):
	            response = fibonacci(index)
	            self.assertEqual(response, correct_sequence[index])

This test, `test_returns_correct_fibonacci_number` follows a common testing pattern:

- Setup your initial expected data

- Run the code that you are testing

- Check that the tested code did the right thing (in this case, returned the correct fibonacci number)

Disclaimer, the fibonacci sequence is an [infinite sequence](https://en.wikipedia.org/wiki/Sequence#Finite_and_infinite) and so we can’t test all values but we can be reasonably sure of the correctness. The general advice is to try to test any edge cases, for us that’s positions less than `0`, and also test the general case as best you can. While we could have tested hundreds or thousands more numbers, tests are often part of a test suite which might contain hundreds or thousands of tests which each require some time to run. This is a choice that the developer and potentially a QA team need to make as to how quickly you want tests to run versus how sure you need to be about the correctness of the code. Your tests may not ever be complete, even if you have full code coverage, and ultimately it is about reducing the risk that a user is going to come across a bug, that is we want our test suites to find bugs before we release any software to our actual users.

Back to the test and following the advice from above, we choose to test `12` different inputs to the function `fibonacci` (which we are yet to write). For each on of the positions we pass it to the `fibonacci` function and then test that the response from that call matches the expected result from our `correct_sequence` list using the `assertEqual` method that comes along with `TestCase`. `assertEqual` will simply check that the two arguments, the response and the expected response, are actually equal and if not will fail the test.

## Our Second Test

The second requirement we had for our `fibonacci` function is that it raises a `ValueError` if we pass it any position less than 0. Again, we can’t possibly test all numbers less than 0 but it is probably fine for us to just test `-1` in this case since we have already tested `0` in `test_returns_correct_fibonacci_number`. Our code now looks like this:

	from unittest import TestCase

	class FibonacciTests(TestCase):
	    def test_returns_correct_fibonacci_number(self):
	        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	        for index in range(len(correct_sequence)):
	            response = fibonacci(index)
	            self.assertEqual(response, correct_sequence[index])

	    def test_raise_value_error_on_negative_input(self):
	        self.assertRaises(ValueError, fibonacci, -1)

All we need to do to test that `fibonacci` raises a `ValueError` on `-1` is to use the `assertRaises` method, generously provided by `TestCase`. As the name suggests, it checks that the first argument (an exception type) is raised by calling the second argument (some callable) with the remaining arguments provided.

## Running Our Tests

Now that we have our initial tests, it’s time to run them. To do this, simply run:

`pytest`
in your command line. By running this, we have stumbled across our first bug:

	test_fibonacci.py FF                                                                                                                                                                                 [100%]

	================================================================================================= FAILURES =================================================================================================
	_________________________________________________________________________ FibonacciTests.test_raise_value_error_on_negative_input __________________________________________________________________________

	self = <test_fibonacci.FibonacciTests testMethod=test_raise_value_error_on_negative_input>

	    def test_raise_value_error_on_negative_input(self):
	>       self.assertRaises(ValueError, fibonacci, -1)
	E       NameError: name 'fibonacci' is not defined

	test_fibonacci.py:11: NameError
	___________________________________________________________________________ FibonacciTests.test_returns_correct_fibonacci_number ___________________________________________________________________________

	self = <test_fibonacci.FibonacciTests testMethod=test_returns_correct_fibonacci_number>

	    def test_returns_correct_fibonacci_number(self):
	        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	        for index in range(len(correct_sequence)):
	>           response = fibonacci(index)
	E           NameError: name 'fibonacci' is not defined

	test_fibonacci.py:7: NameError
	========================================================================================= 2 failed in 0.07 seconds =========================================================================================

Looking at the pytest output, we can see the obvious issue, we have no `fibonacci` function yet. Lets fix that in a file called `main.py`:

	def fibonacci(position):
	    if position == 1 or position == 2:
	        return 1
	    return fibonacci(position - 2) + fibonacci(position - 1)

Before we run our tests we will need to import this function at the top of our `test_fibonacci.py` file like so:

	from main import fibonacci

## Debugging `fibonacci`

Running our tests again, we get a `RecursionError` which means that our function called recusively too many times. Looking at our code, we notice we have accidentally forgotten to `0`-index our positions. This can be fixed as follows:

	def fibonacci(position):
	    if position == 0 or position == 1:
	        return 1
	    return fibonacci(position - 2) + fibonacci(position - 1)

Now when we run `pytest` we notice that we have actually passed the first test but failed `test_raise_value_error_on_negative_input`:

	test_fibonacci.py F.                                                                                                                                                                                 [100%]

	================================================================================================= FAILURES =================================================================================================
	_________________________________________________________________________ FibonacciTests.test_raise_value_error_on_negative_input __________________________________________________________________________

	self = <test_fibonacci.FibonacciTests testMethod=test_raise_value_error_on_negative_input>

	    def test_raise_value_error_on_negative_input(self):
	>       self.assertRaises(ValueError, fibonacci, -1)

	test_fibonacci.py:13:
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
	main.py:12: in fibonacci
	    return fibonacci(position - 2) + fibonacci(position - 1)
	main.py:12: in fibonacci
	    return fibonacci(position - 2) + fibonacci(position - 1)
	E   RecursionError: maximum recursion depth exceeded in comparison
	!!! Recursion detected (same locals & position)
	==================================================================================== 1 failed, 1 passed in 0.08 seconds ====================================================================================

While we still have to fix our second test, congratulations on passing your first! It’s that pesky `RecursionError` again, how could that have happened? Well, looking at the last line of the function `return fibonacci(position - 2) + fibonacci(position - 1)` if we pass `-1` as the `position` it will keep hitting this line and never exit, so there’s our issue. We can fix this by adding a check for negative numbers:

	def fibonacci(position):
	    if position <= 0:
	        raise ValueError('position must be non-negative')
	    if position == 0 or position == 1:
	        return 1
	    return fibonacci(position - 2) + fibonacci(position - 1)

We re-run `pytest` and oops, we broke our first test:

	test_fibonacci.py .F                                                                                                                                                                                 [100%]

	================================================================================================= FAILURES =================================================================================================
	___________________________________________________________________________ FibonacciTests.test_returns_correct_fibonacci_number ___________________________________________________________________________

	self = <test_fibonacci.FibonacciTests testMethod=test_returns_correct_fibonacci_number>

	    def test_returns_correct_fibonacci_number(self):
	        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	        for index in range(len(correct_sequence)):
	>           response = fibonacci(index)

	test_fibonacci.py:9:
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

	position = 0

	    def fibonacci(position):
	        if position <= 0:
	>           raise ValueError('position must be non-negative')
	E           ValueError: position must be non-negative

	main.py:17: ValueError
	==================================================================================== 1 failed, 1 passed in 0.06 seconds ====================================================================================

What a sneaky mistake, we accidently raised the `ValueError` when `position` is `0` as well. A quick fix should get everything passing:

	def fibonacci(position):
	    if position < 0:
	        raise ValueError('position must be non-negative')
	    if position == 0 or position == 1:
	        return 1
	    return fibonacci(position - 2) + fibonacci(position - 1)

and TA-DA!!! We passed all our tests:

	test_fibonacci.py ..                                                                                                                                                                                 [100%]

	========================================================================================= 2 passed in 0.01 seconds =========================================================================================

## Well Done!

Well that brings us to the end of testing our `fibonacci` function. I hope you have now covered:

- The fundamentals of Test-Driven Development

- How to use pytest to run simple tests

- How to use testing as a means to find bugs and describe requirements

The next thing you would need to do if this was production code, is assume that you will get bug reports about this code, perhaps we missed a requirement. When a new issue comes in, you would add another test case, run the tests to make sure that it fails, and then make any changes to the function to make that test pass. Once you again have reason to believe the code is correct, you can go ahead and re-release it.

You can find all the code related to this post [here on GitHub](https://github.com/mattjegan/getting-started-with-python-testing).

Written on April 22, 2018

 [inShare.](#)