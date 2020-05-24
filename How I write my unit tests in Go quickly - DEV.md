How I write my unit tests in Go quickly - DEV

 [lnwiefo399sxg015t94k.webp](../_resources/57235c17aeb685c0807540b9cb3eddad.webp)

#  How I write my unit tests in Go quickly

###     [![ac351b11-6853-4fd1-97c6-d4507b30167c.jpg](../_resources/4c25a95c461f75ba60d909d8c0ec65d6.jpg)  Ilya Kaznacheev](https://dev.to/ilyakaznacheev)    [![github-logo-28d89282e0daa1e2496205e2f218a44c755b0dd6536bbadf5ed5a44a7ca54716.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](http://github.com/ilyakaznacheev)  Apr 30  *Updated on May 03, 2020*  ・10 min read

 [#go](https://dev.to/t/go)  [#testing](https://dev.to/t/testing)  [#bdd](https://dev.to/t/bdd)  [#mocks](https://dev.to/t/mocks)

*Photo by [Veri Ivanova](https://unsplash.com/@veri_ivanova)*

We all love unit tests because they help us to keep our software workable. And we all hate them because they don't appear magically - someone needs to write them. And when it comes to writing, it often takes a huge amount of time to cover the simplest cases.

But I found my way to do that without pain (okay, with less pain). And I will share it with you like a simple illustrated guide.

##   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#separate-layers) Separate layers

The principle isn't new, but it is still useful. Nowadays it comes with different names - hexagonal architecture, onion architecture, separation of concerns, etc. The main idea is that different parts (and I mean *logically* different parts) of your application should be separated into independent parts.

It's very important because you can't just test the whole app you're building. Ok, technically you can. But it will require an enormous amount of time and it will be a nightmare from a long-term perspective.

Instead, make it as independent as possible. But the app or at least the microservice cannot be independent of himself! It can, and we call it **dependency injection**. And it never was so easy as now in Go because we have...

###   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#duck-typing-interfaces) Duck typing interfaces

That means that if some type has the methods described in the interface, we can use it via that interface. So there is no need to do a lot of paperwork at the beginning of the project and draw a huge UMLs with all possible interactions and relationships - just write an interface for your layer with its *minimal requirements* and pass the dependencies into it.

> Example: you have a business-logic package that has to save some data into a database. No need to create or get a database connection somewhere in this package - just define a `Repository`>  or a `Storage`>  interface (or any more suitable name) and put there all actions you want to perform with the database - save, update, read, delete, increment a counter, etc. Then you just have to put the database object, that can perform that actions - it will contain the **> exact**>  database query language code and database-specific logic. You also will handle the database connection and possible connection errors **> outside of the business-logic layer**> . The layer will become **> independent**>  of the database layer.

###   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#inject-unmanaged-resources) Inject unmanaged resources

There are many unmanaged resources like random number generators, time, random-based hashes an so on. They don't require outside injection because they have no outside dependencies. But they still can do unpredictable impacts on test results. So instead of trying to work around them in tests, just use the same approach - inject them as an isolated dependency. Bus since they are not provided from the outside, do that from the inside!

Example:

	type Example struct {}

	func NewExample() *Example {
	    ...
	    return &Example{}
	}

	func (e *Example) TimeToGo() string {
	    now := time.Now()
	    return fmt.Sprintf("its time to go! %s", now.String())
	}

Here you can't predict the `TimeToGo` method response in the test - each time `time.Now()` will return a new value. But you can take charge of it:

	type Example struct {
	    now func() time.Time
	}

	func NewExample() *Example {
	    ...
	    return &Example{time.Now}
	}

	func (e *Example) TimeToGo() string {
	    return fmt.Sprintf("its time to go! %s", e.now().String())
	}

Will work as before, but `time.Now` is now under your control! You can easily mock it in the test:

	nowMock := func() time.Time {
	    t, _ := time.Parse(time.Kitchen, time.Kitchen)
	    return t
	}

	e := Example{nowMock}

	if e.TimeToGo() != "its time to go! 0000-01-01 15:04:00 +0000 UTC" {
	    t.Errorf("test failed")
	}

So try to avoid any dependency in your logical entity. Even such a small as a current time or a random value. It's ok to hide them under interfaces or function types.

##   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#8020) 80/20

100% coverage is a dream of any Open-Source developer. It's so nice to look at a green badge in your project's readme! But within productive projects, things work a different way.

Normally you just don't have enough time or resources to do a 100% test coverage. End even if you'll do so, during the active development phase you will change the logic so many times, so the number of test changes will be enormous.

But in fact, the 80/20 principle works here too: the 20% coverage of the "hottest" or most important code will cover 80% of the app's usage and dataflow. That means, start with the "hottest" code coverage. If you will have time and motivation you will write tests for less important parts and slowly will increase the coverage.

For example, if you're building a web search service, test the search engine first. If it really works as expected, you can cover autocomplete, translation, and live preview next. But without the reliable **core feature** you will fail.

##   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#dont-write-your-code) Don't write your code

Now you have a well isolated and pretty important part of your application ready. You need to fit your test into that frame. And thankfully your app consumes interfaces instead of exact implementations. That means, we can mock them in tests!

But writing mocks is a salt mine job. We don't have to rob a robot's job - let them do what they are designed for!

So I don't write test mocks, I generate them instead. To do that I use Mockery.

##   ![github-logo-28d89282e0daa1e2496205e2f218a44c755b0dd6536bbadf5ed5a44a7ca54716.svg](../_resources/2d294d0612a1a14776f872a7b07c05ec.png)  [vektra](https://github.com/vektra) / [mockery](https://github.com/vektra/mockery)

###  A mock code autogenerator for golang

Say we have a database interface:

	package repo

	type Storage interface {
	    GetOrder(id string) (*Order, error)
	    CreateOrder(order Order) error
	    DeleteOrder(id string) error
	}

And a code that uses it:

	type AccountManager struct {
	    storage repo.Storage
	}

We can generate the mock simply by calling the following command:

	# if the interface is in the internal/repo package
	mockery -name=Storage -dir=internal/repo

And it will generate a perfect fitting mock for your interface! It will be stored in the `/mocks` directory regarding the interface package directory (you can change it by specifying `-output` parameter). Then you only need to use it in your test:

	var testOrder repo.Order
	//...
	storageMock := new(mocks.Storage)
	storageMock.On("GetOrder", "12345").
	    Return(&testOrder, nil)

	// and then inject it into your code under the test
	am := AccountManager{storageMock}

	// execute test cases with mocked dependency ...

I normally use either the go-generate to run the mock generation:

	//go:generate mockery -name=Storage

	type Storage interface { ... }

And then run `go generate ./...`. Or I just put them as a list in the `Makefile` with an absolute path. Or you can even generate mocks for all exported interfaces in your directory recursively. See the library details for more information.

##   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#use-shortcuts) Use shortcuts

The test case writing is hard and boring work. You have to prepare a lot of data samples, do a boring work of setting the environment up, preparing infrastructure like HTTP requests and response writers, mock servers, stub data, etc. And it's really tedious to write every got and want data check and corresponding errors.

But you can save some time by using shortcuts. And with shortcuts, I mean test libraries as Testify to wrap repetitive parts of tests in clean and handy helpers!

##   ![github-logo-28d89282e0daa1e2496205e2f218a44c755b0dd6536bbadf5ed5a44a7ca54716.svg](../_resources/2d294d0612a1a14776f872a7b07c05ec.png)  [stretchr](https://github.com/stretchr) / [testify](https://github.com/stretchr/testify)

###  A toolkit with common assertions and mocks that plays nicely with the standard library

Let's say you have a common HTTP response with something like this:

	w := httptest.NewRecorder()
	//... function under test call ...

	// assertion
	gotBody, _ := ioutil.ReadAll(rr.Body)
	gotStatus := rr.Result().StatusCode

	if string(gotBody) != tt.bodyWant {
	    t.Errorf("wrong response body %s want %s", string(gotBody), tt.bodyWant)
	}

	if gotStatus != tt.statusWant {
	    t.Errorf("wrong respose status %d want %d", gotStatus, tt.statusWant)
	}

Simple, huh? But when you have to do that 100+ times it becomes a little bit boring... You don't have to wait 'till a [boreout](https://en.wikipedia.org/wiki/Boreout)! Just use shortcuts:

	import "github.com/stretchr/testify/assert"

	w := httptest.NewRecorder()
	//... function under test call ...

	// assertion
	gotBody, _ := ioutil.ReadAll(rr.Body)
	gotStatus := rr.Result().StatusCode

	assert.Equal(t, string(gotBody), tt.bodyWant, "wrong response body")
	assert.Equal(t, gotStatus, tt.statusWant,. "wrong response status")

It may be used in more interesting ways. Say, you have a method that returns a pointer and an error (a common pattern in Go). So you don't want to assert a returned value in case of error because it will cause a nil pointer to dereference. So you have to build a messy condition with a nil check and error check and so on... You don't have to:

	want := "we want to get this exact value"

	got, err := GiveMeMyData(input)

	// if error is nill, NotNil will return true
	// otherwise it will write an error message to testing.T
	if assert.NotNil(t, err, "unexpected function error") {
	    // here we assert the expected value
	    // but only if the error is nil!
	    assert.Equal(t, got, want, "unexpected function output)
	}

You can make in *even shorter* by passing `testing.T` to the assert structure:

	assert := assert.New(t)

	/// now you don't have to pass t to each function, 500 milliseconds saved!
	assert.Equal(123, 123, "they should be equal")

It may look simple, but trust me, it will give you enough saved time during unit testing to drink a cup of coffee. Even to brew a coffee!

##   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#make-test-meaningful) Make test meaningful

I like tests, but when it comes to testing output, it getting harder to keep on track what's going on and which test was failed and why. It's ok when you have 10 or 20 test cases, but if you have hundreds of tests (or at least test sets, if you're using table tests for example) it's really hard to understand what's wrong just looking on the test output.

To make it more readable you have to give a proper description. But do you **really** want your test cases to be looking like this?

	if got != want {
	    t.Errorf("by calling a function A when there is no data in the DB table a_data and at the same time there is no incoming messages from the MQ and no idle workers in the worker pool, it returns %s but we want %s", got, want)
	}

I hope you not. Otherwise please stop reading. Because this is my favorite part.

To achieve readability in test output and make it easy to navigate you can use [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) approach to testing. I use it for many reasons:

1. it helps to structure the test as a sequence of steps or a story;

2. it's nice to read in test output because it is a complete story of your test fail;

3. you can build your test cases as a tree from a root common input to different results;

4. it's possible to go outside of unit tests and write a multi-step (or not) test for a real business story. So instead of testing abstract parts of your app, you can go ahead and cover a real business-process as works in real life! It's also a good way to focus on really necessary tests first because you can open a spec and write a test for it!

So let's take a closer look. For this kind of testing I use [ginkgo](https://github.com/onsi/ginkgo) library. It is paired with a [gomega](https://github.com/onsi/gomega) test matcher library, with a lot of test helpers and wrappers (more shortcuts!).

##   ![github-logo-28d89282e0daa1e2496205e2f218a44c755b0dd6536bbadf5ed5a44a7ca54716.svg](../_resources/2d294d0612a1a14776f872a7b07c05ec.png)  [onsi](https://github.com/onsi) / [ginkgo](https://github.com/onsi/ginkgo)

###  BDD Testing Framework for Go

I'm not a fan of BDD itself, but I really like to use this approach in tests. So let me show you a couple of examples.

> You need to > [> set up a test suite](http://onsi.github.io/ginkgo/#getting-started-writing-your-first-test)> . Normally I do that once in a package.

The example above may look like this:

	import (
	    . "github.com/onsi/ginkgo"
	    . "github.com/onsi/gomega"
	)

	var _ = Describe("Function A", func() {
	    When("I call the function", func() {
	        Context("and there is no data in the DB table a_data", func() {
	            Context("and there is no incoming messages from the MQ", func() {
	                Context("and no idle workers in the worker pool", func() {
	                    It("should return 123", func() {
	                        got, _ := A("123")
	                        Expect(got).To(Equal("123"))
	                    })
	                    It("should work without errors", func() {
	                        _, err := A("123")
	                        Expect(err).To(BeNil())
	                    })
	                })
	            })
	        })
	    })
	})

Looks more like a real spec, right?
And the error output will look like this:

[![kq9z6twvrmvch6y5zc0e.png](../_resources/fd082626bcdb7928591e57e7ba5a51fa.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--3XCCBd9r--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/kq9z6twvrmvch6y5zc0e.png)

You can also add some data into any step, and it will be added each time your test will reach this node of the test tree.

A pseudocode example:

	Describe some test entity
	├─With data X
	│ ├─And with data B
	│ │ └─And with data C
	│ │   ├─It should do this
	│ │   └─And this
	│ └─But with data D
	│     └─It should do this
	└─With data Y
	  ├─And with data E
	  │   └─It should do this
	  └─And with data E*
	      └─It should error

So here is a whole story, and you can describe it using ginkgo! In this case, for example, the node `And with data B` will be executed 3 times:

- With data X -> **And with data B** -> And with data C -> It should do this
- With data X -> **And with data B** -> And with data C -> And this
- With data X -> **And with data B** -> But with data D -> It should do this

You can use `BeforeEach()` to set up some context for each step (set some variables, functions, fill mocks, and so on). And also you can use `AftrrEach()` to cleanup at the end of the node.

The library has a lot of other useful functions - `BeforeSuite` and `AfterSuite` and many variations to help you organize your test better.

So the main idea here is to use it both as a meaningful description of the process under the test, and the test sequence and context of each step.

##   [(L)](https://dev.to/ilyakaznacheev/how-i-write-my-unit-tests-in-go-quickly-4bd5#putting-it-all-together) Putting it all together

So how to do it quickly? Let's summarize:
1. separate layers by means of DI;
2. use interfaces to do that;
3. start with hottest 20% of your code;
4. mock these interfaces with generated mocks;
5. use shortcuts to speed-up simple tests;
6. use the BDD test suite to describe and organize complex tests.
In the end, it may look like this:

	import (
	    "errors"
	    "temp"
	    "temp/mocks"

	    . "github.com/onsi/ginkgo"
	    . "github.com/onsi/gomega"
	    "github.com/stretchr/testify/mock"
	)

	var _ = Describe("Function A", func() {
	    var (
	        storageMock *mocks.Storage
	        testOrder   temp.Order
	        testErr     error
	    )

	    BeforeEach(func() {
	        storageMock = new(mocks.Storage)
	        testOrder = temp.Order("my test order")
	        testErr = errors.New("test error")
	    })

	    When("we want to get some order", func() {
	        Context("and the order exists", func() {
	            BeforeEach(func() {
	                storageMock.On("GetOrder", "12345").
	                    Return(&testOrder, nil)
	            })

	            It("should return my test order without error", func() {
	                sk := temp.NewStorekeeper(storageMock)
	                got, err := sk.GetMyOrder("12345")

	                Expect(*got).To(BeEquivalentTo("my test order"))
	                Expect(err).To(BeNil())
	            })
	        })

	        Context("and there is no order", func() {
	            BeforeEach(func() {
	                storageMock.On("GetOrder", mock.Anything).
	                    Return(nil, testErr)
	            })

	            It("should return empty order with error", func() {
	                sk := temp.NewStorekeeper(storageMock)
	                got, err := sk.GetMyOrder("12345")

	                Expect(got).To(BeNil())
	                Expect(err).To(HaveOccurred())
	            })
	        })
	    })
	})

Pretty quick to write. And so easy read in CI logs!