Go Goroutines and Apis · blog.gnoack.org

# Go Goroutines and Apis

Go programming notes
 November 18, 2019

Goroutines are a unusual and powerful programming language feature, so they are a tempting toy to play with, and they get a bit overused.

There is some indication that the following Go principle holds true:
> Strive to provide synchronous APIs,
> let the caller start goroutines.
To put this advice into a more concrete code example:
Do this:

	func (t *type) Run(ctx context.Context) {
	    // Implementation of background task
	}

Instead of this:

	func (t *type) Start() {
	    t.wg.Add(1)
	    go func() {
	      // Implementation of background task
	      t.wg.Done()
	    }
	}

	func (t *type) Cancel() {
	    // Somehow cancel the background task
	    t.wg.Wait()
	}

Upsides for `Run()`:

- The caller gets to decide how the “background” code gets run.
    - Spawning Goroutines is easy for the caller too.
    - `go` statements move towards the application’s top-level. Goroutine coordination becomes simpler to reason about when goroutines are started in fewer places.
    - Callers can also run it without goroutine and just block on the call, if there is no other work to be done.
- Background task cancellation is provided through the context.
- Waiting for the background task has a trivial API (when the function returns), and can be done with the mechanism the caller prefers (waitgroups, channels, …)
- It’s on the safe side API-wise: There is no `Close()` method which callers can forget to call (leaking resources).

Another great discussion of this was in the [Go Time: On application design](https://changelog.com/gotime/102#transcript-91) podcast (starting around minute 47, Mat Ryer’s explanation really resonated with me)

## Comments

Jacob

2019-11-19

A talk which goes into this topic in some detail is https://www.youtube.com/watch?v=LHe1Cb_Ud_M

Name

 Captcha ![](../_resources/27549190c88803029a72db029d8c39b9.png)

Text