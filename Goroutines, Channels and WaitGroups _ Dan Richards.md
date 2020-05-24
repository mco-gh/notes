Goroutines, Channels and WaitGroups | Dan Richards

# Goroutines, Channels and WaitGroups

26 Mar 2018

Recently I came across a scenario where I needed to execute some long running functions and capture the results for later use. Of course to reduce the latency of this code I ran the functions concurrently with goroutines and a waitgroup. The kicker here was that to return the results from the goroutines I had to use channels and getting the complete data from the channel was more complex than I thought.

## The Problem

My first attempt at this problem looked like this (long running code replaced by a trivial string example, but you get the point):

	package main

	import (
	  "fmt"
	  "sync"
	)

	func getWords() []string {
	  ch := make(chan string)

	  var wg sync.WaitGroup
	  wg.Add(2)

	  go func() {
	    defer wg.Done()

	    ch <- "foo"
	    ch <- "bar"
	  }()

	  go func() {
	    defer wg.Done()

	    ch <- "baz"
	    ch <- "qux"
	  }()

	  wg.Wait()
	  close(ch)

	  var words []string
	  for word := range ch {
	    words = append(words, word)
	  }

	  return words
	}

	func main() {
	  fmt.Println(getWords())
	}

Now what happens when you run this code? If you guessed deadlocks…you’d be right!

	fatal error: all goroutines are asleep - deadlock!

	goroutine 1 [semacquire]:
	sync.runtime_Semacquire(0xc4200160ec)
		/usr/lib/go/src/runtime/sema.go:56 +0x39
	sync.(*WaitGroup).Wait(0xc4200160e0)
		/usr/lib/go/src/sync/waitgroup.go:129 +0x72
	main.getWords(0xc420053f78, 0x40423c, 0xc420084058)
		/home/dan/code/go/src/github.com/danmrichards/channels-waitgroup/broken/main.go:28 +0xe4
	main.main()
		/home/dan/code/go/src/github.com/danmrichards/channels-waitgroup/broken/main.go:40 +0x26

	goroutine 5 [chan send]:
	main.getWords.func1(0xc4200160e0, 0xc420084060)
		/home/dan/code/go/src/github.com/danmrichards/channels-waitgroup/broken/main.go:17 +0x61
	created by main.getWords
		/home/dan/code/go/src/github.com/danmrichards/channels-waitgroup/broken/main.go:14 +0xaa

	goroutine 6 [chan send]:
	main.getWords.func2(0xc4200160e0, 0xc420084060)
		/home/dan/code/go/src/github.com/danmrichards/channels-waitgroup/broken/main.go:24 +0x61
	created by main.getWords
		/home/dan/code/go/src/github.com/danmrichards/channels-waitgroup/broken/main.go:21 +0xd6
	exit status 2

## The Solution

The reason that the deadlock occurs here is due to the nature of channels. If you checkout the [Golang Tour](https://tour.golang.org/concurrency/2) you’ll see that unbuffered channels block on sends and receives. My code is blocking on sending to the channel hence the goroutines never complete and my receiving code never executes.

The solution here is initially a little confusing but once implemented makes a lot of sense:

	package main

	import (
	  "fmt"
	  "sync"
	)

	func getWords() []string {
	  ch := make(chan string)

	  var wg sync.WaitGroup
	  wg.Add(2)

	  go func() {
	    defer wg.Done()

	    ch <- "foo"
	    ch <- "bar"
	  }()

	  go func() {
	    defer wg.Done()

	    ch <- "baz"
	    ch <- "qux"
	  }()

	  go func() {
	    wg.Wait()
	    close(ch)
	  }()

	  var words []string
	  for word := range ch {
	    words = append(words, word)
	  }

	  return words
	}

	func main() {
	  fmt.Println(getWords())
	}

Notice that the `wg.Wait()` and `close(ch)` have been moved into another goroutine. This allows the receiving code and the waitgroup/channel management to run on separate goroutines. This allows the receiving code to run which unblocks the channel sends and as such the goroutines are able to complete. Worth noting that the waitgroup is only concerned with the first 2 goroutines where the work is happening.

## Taking Things Further

The solution that was applied here can be taken even further. We could extend the goroutines further to return data to additional channels. Say for example we wanted to return data but also capture any errors that occurred during the process. We could do the following:

	package main

	import (
	  "errors"
	  "fmt"
	  "sync"
	)

	func getWords() (words []string, err error) {
	  ch := make(chan string)
	  errs := make(chan error, 2)

	  var wg sync.WaitGroup
	  wg.Add(2)

	  go func() {
	    defer wg.Done()

	    ch <- "foo"
	    ch <- "bar"
	  }()

	  go func() {
	    defer wg.Done()

	    errs <- errors.New("well that didn't work")
	  }()

	  go func() {
	    wg.Wait()
	    close(ch)
	    close(errs)
	  }()

	  for word := range ch {
	    words = append(words, word)
	  }

	  for wordErr := range errs {
	    err = wordErr
	    return
	  }

	  return
	}

	func main() {
	  words, err := getWords()
	  if err != nil {
	    fmt.Printf("Oh dear, oh dear: %s\n", err)
	  }

	  fmt.Println(words)
	}

Notice that we have added a second channel of type `err`. We have also made this a buffered channel of length 2, this is because we know that a maximum of 2 errors could ever be returned here. Also unbuffered channels only block when the [buffer is full](https://tour.golang.org/concurrency/3). We can use that to our advantage here; as we don’t know how many errors will be occur (0, 1 or 2) we use a buffer to prevent the errors channel from blocking us and causing more deadlocks.