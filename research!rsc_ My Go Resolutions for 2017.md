research!rsc: My Go Resolutions for 2017

# My Go Resolutions for 2017

Posted on Wednesday, January 18, 2017.

’Tis the season for resolutions, and I thought it would make sense to write a little about what I hope to work on this year as far as Go is concerned.

My goal every year is to *help Go developers*. I want to make sure that the work we do on the Go team has a significant, positive impact on Go developers. That may sound obvious, but there are a variety of common ways to fail to achieve that: for example, spending too much time cleaning up or optimizing code that doesn’t need it; responding only to the most common or recent complaints or requests; or focusing too much on short-term improvements. It’s important to step back and make sure we’re focusing our development work where it does the most good.

This post outlines a few of my own major focuses for this year. This is only my personal list, not the Go team’s list.

One reason for posting this is to gather feedback. If these spark any ideas or suggestions of your own, please feel free to comment below or on the linked GitHub issues.

Another reason is to make clear that I’m aware of these issues as important. I think too often people interpret lack of action by the Go team as a signal that we think everything is perfect, when instead there is simply other, higher priority work to do first.

## Type aliases

There is a recurring problem with moving types from one package to another during large codebase refactorings. We tried to solve it last year with [general aliases](https://golang.org/issue/16339), which didn’t work for at least two reasons: we didn’t explain the change well enough, and we didn’t deliver it on time, so it wasn’t ready for Go 1.8. Learning from that experience, I [gave a talk](https://www.youtube.com/watch?v=h6Cw9iCDVcU)and [wrote an article](https://talks.golang.org/2016/refactor.article)about the underlying problem, and that started a [productive discussion](https://golang.org/issue/18130)on the Go issue tracker about the solution space. It looks like more limited [type aliases](https://golang.org/design/18130-type-alias)are the right next step. I want to make sure those land smoothly in Go 1.9. [#18130](https://golang.org/issue/18130).

## Package management

I designed the Go support for downloading published packages (“goinstall”, which became “go get”) in February 2010. A lot has happened since then. In particular, other language ecosystems have really raised the bar for what people expect from package management, and the open source world has mostly agreed on[semantic versioning](http://semver.org/), which provides a useful base for inferring version compatibility. Go needs to do better here, and a group of contributors have been[working on a solution](https://blog.gopheracademy.com/advent-2016/saga-go-dependency-management/). I want to make sure these ideas are integrated well into the standard Go toolchain and to make package management a reason that people love Go.

## Build improvements

There are a handful of shortcomings in the design of the go command’s build system that are overdue to be fixed. Here are three representative examples that I intend to address with a bit of a redesign of the internals of the go command.

Builds can be too slow, because the go command doesn’t cache build results as aggressively as it should. Many people don’t realize that `go`  `install` saves its work while `go`  `build` does not, and then they run repeated `go`  `build` commands that are slow because the later builds do more work than they should need to. The same for repeated `go`  `test` without `go`  `test`  `-i` when dependencies are modified. All builds should be as incremental as possible.[#4719](https://golang.org/issue/4719).

Test results should be cached too: if none of the inputs to a test have changed, then usually there is no need to rerun the test. This will make it very cheap to run “all tests” when little or nothing has changed.[#11193](https://golang.org/issue/11193).

Work outside GOPATH should be supported nearly as well as work inside GOPATH. In particular, it should be possible to `git`  `clone` a repo,`cd` into it, and run `go` commands and have them work fine. Package management only makes that more important: you’ll need to be able to work on different versions of a package (say, v1 and v2) without having entirely separate GOPATHs for them.[#17271](https://golang.org/issue/17271).

## Code corpus

I think it helped to have concrete examples from real projects in the talk and article I prepared about codebase refactoring (see [above](https://research.swtch.com/go2017#alias)). We’ve also defined that [additions to vet](https://golang.org/src/cmd/vet/README)must target problems that happen frequently in real programs. I’d like to see that kind of analysis of actual practice—examining the effects on and possible improvements to real programs—become a standard way we discuss and evaluate changes to Go.

Right now there’s not an agreed-upon representative corpus of code to use for those analyses: everyone must first create their own, which is too much work. I’d like to put together a single, self-contained Git repo people can check out that contains our official baseline corpus for those analyses. A possible starting point could be the top 100 Go language repos on GitHub by stars or forks or both.

## Automatic vet

The Go distribution ships with this powerful tool,[`go`  `vet`](https://golang.org/cmd/vet/), that points out correctness bugs. We have a high bar for checks, so that when vet speaks, you should listen. But everyone has to remember to run it. It would be better if you didn’t have to remember. In particular, I think we could probably run vet in parallel with the final compile and link of the test binary during `go`  `test` without slowing the compile-edit-test cycle at all. If we can do that, and if we limit the enabled vet checks to a subset that is essentially 100% accurate, we can make passing vet a precondition for running a test at all. Then developers don’t need to remember to run `go`  `vet`. They run `go`  `test`, and once in a while vet speaks up with something important and avoids a debugging session.[#18084](https://golang.org/issue/18084),[#18085](https://golang.org/issue/18085).

## Errors & best practices

Part of the intended contract for error reporting in Go is that functions include relevant available context, including the operation being attempted (such as the function name and its arguments). For example, this program:

	err := os.Remove("/tmp/nonexist")
	fmt.Println(err)

prints this output:

	remove /tmp/nonexist: no such file or directory

Not enough Go code adds context like `os.Remove` does. Too much code does only

	if err != nil {
	    return err
	}

all the way up the call stack, discarding useful context that should be reported (like `remove`  `/tmp/nonexist:` above). I would like to try to understand whether our expectations for including context are wrong, or if there is something we can do to make it easier to write code that returns better errors.

There are also various discussions in the community about agreed-upon interfaces for stripping error context. I would like to try to understand when that makes sense and whether we should adopt an official recommendation.

## Context & best practices

We added the new [context package](https://golang.org/pkg/context/)in Go 1.7 for holding request-scoped information like[timeouts, cancellation state, and credentials](https://blog.golang.org/context). An individual context is immutable (like an individual string or int): it is only possible to derive a new, updated context and pass that context explicitly further down the call stack or (less commonly) back up to the caller. The context is now carried through APIs such as[database/sql](https://golang.org/pkg/database/sql)and[net/http](https://golang.org/pkg/net/http), mainly so that those can stop processing a request when the caller is no longer interested in the result. Timeout information is appropriate to carry in a context, but—to use a [real example we removed](https://golang.org/issue/18284)—database options are not, because they are unlikely to apply equally well to all possible database operations carried out during a request. What about the current clock source, or logging sink? Is either of those appropriate to store in a context? I would like to try to understand and characterize the criteria for what is and is not an appropriate use of context.

## Memory model

Go’s [memory model](https://golang.org/ref/mem) is intentionally low-key, making few promises to users, compared to other languages. In fact it starts by discouraging people from reading the rest of the document. At the same time, it demands more of the compiler than other languages: in particular, a race on an integer value is not sufficient license for your program to misbehave in arbitrary ways. But there are some complete gaps, in particular no mention of the [sync/atomic package](https://golang.org/pkg/sync/atomic/). I think the core compiler and runtime developers all agree that the behavior of those atomics should be roughly the same as C++ seqcst atomics or Java volatiles, but we still need to write that down carefully in the memory model, and probably also in a long blog post.[#5045](https://golang.org/issue/5045),[#7948](https://golang.org/issue/7948),[#9442](https://golang.org/issue/9442).

## Immutability

The [race detector](https://golang.org/doc/articles/race_detector.html)is one of Go’s most loved features. But not having races would be even better. I would love it if there were some reasonable way to integrate[reference immutability](https://www.google.com/search?q=%22reference+immutability%22) into Go, so that programmers can make clear, checked assertions about what can and cannot be written and thereby eliminate certain races at compile time. Go already has one immutable type, `string`; it would be nice to retroactively define that`string` is a named type (or type alias) for `immutable`  `[]byte`. I don’t think that will happen this year, but I’d like to understand the solution space better. Javari, Midori, Pony, and Rust have all staked out interesting points in the solution space, and there are plenty of research papers beyond those.

In the long-term, if we could statically eliminate the possibility of races, that would eliminate the need for most of the memory model. That may well be an impossible dream, but again I’d like to understand the solution space better.

## Generics

Nothing sparks more [heated arguments](https://research.swtch.com/dogma)among Go and non-Go developers than the question of whether Go should have support for generics (or how many years ago that should have happened). I don’t believe the Go team has ever said “Go does not need generics.” What we *have* said is that there are higher-priority issues facing Go. For example, I believe that better support for package management would have a much larger immediate positive impact on most Go developers than adding generics. But we do certainly understand that for a certain subset of Go use cases, the lack of parametric polymorphism is a significant hindrance.

Personally, I would like to be able to write general channel-processing functions like:

	// Join makes all messages received on the input channels
	// available for receiving from the returned channel.
	func Join(inputs ...<-chan T) <-chan T

	// Dup duplicates messages received on c to both c1 and c2.
	func Dup(c <-chan T) (c1, c2 <-chan T)

I would also like to be able to write Go support for high-level data processing abstractions, analogous to[FlumeJava](https://research.google.com/pubs/archive/35650.pdf) or C#’s [LINQ](https://en.wikipedia.org/wiki/Language_Integrated_Query), in a way that catches type errors at compile time instead of at run time. There are also any number of data structures or generic algorithms that might be written, but I personally find these broader applications more compelling.

We’ve [struggled](https://research.swtch.com/generic) off and on[for years](https://golang.org/design/15292-generics)to find the right way to add generics to Go. At least a few of the past proposals got hung up on trying to design something that provided both general parametric polymorphism (like `chan`  `T`) and also a unification of `string` and `[]byte`. If the latter is handled by parameterization over immutability, as described in the previous section, then maybe that simplifies the demands on a design for generics.

When I first started thinking about generics for Go in 2008, the main examples to learn from were C#, Java, Haskell, and ML. None of the approaches in those languages seemed like a perfect fit for Go. Today, there are newer attempts to learn from as well, including Dart, Midori, Rust, and Swift.

It’s been a few years since we ventured out and explored the design space. It is probably time to look around again, especially in light of the insight about mutability and the additional examples set by newer languages. I don’t think generics will happen this year, but I’d like to be able to say I understand the solution space better.