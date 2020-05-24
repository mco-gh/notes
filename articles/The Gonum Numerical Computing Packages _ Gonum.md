The Gonum Numerical Computing Packages | Gonum

# The Gonum Numerical Computing Packages

    Sun, Jul 9, 2017       **  [intro](http://www.gonum.org/tags/intro), [philosophy](http://www.gonum.org/tags/philosophy)

## Gonum – The Basics

Gonum is a set of packages designed to make writing numeric and scientific algorithms productive, performant, and scalable.

Gonum is a set of packages written in the[Go programming language](https://www.golang.org/) (more on Go later), and is not a language on its own. This makes Gonum similar to [numpy](https://www.numpy.org/) and[scipy](https://www.scipy.org/), libraries built on top of[python](https://www.python.org/), and different from[Julia](https://julialang.org/) and [Matlab](https://www.mathworks.com/)which are full programming languages.

Gonum contains libraries for [matrices and linear algebra](https://godoc.org/gonum.org/v1/gonum/mat);[statistics](https://godoc.org/gonum.org/v1/gonum/stat),[probability](https://godoc.org/gonum.org/v1/gonum/stat/distuv)[distributions](https://godoc.org/gonum.org/v1/gonum/stat/distmv), and [sampling](https://godoc.org/gonum.org/v1/gonum/stat/sampleuv); tools for[function differentiation](https://godoc.org/gonum.org/v1/gonum/diff/fd),[integration](https://godoc.org/gonum.org/v1/gonum/integrate/quad), and [optimization](https://godoc.org/gonum.org/v1/gonum/optimize);[network](https://godoc.org/gonum.org/v1/gonum/graph) creation and analysis; and more.

## Why use Gonum

We encourage you to use Go and Gonum if

- You are tired of sluggish performance, and fighting C and vectorization.
- You are struggling with managing programs as they grow larger.
- You struggle to re-use – even the code you tried to make reusable.
- You would like easy access to parallel computing.
- You want code to be fully transparent, and want the ability to read the source code you use.
- You’d like a compiler to catch mistakes early, but hate fighting linker and unintelligible compile errors.

## Gonum Philosophy

The Gonum packages are designed to be simple, efficient and composable. There is a tension, especially in scientific computing, between ease and simplicity. Gonum, [like the Go language itself](https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html), aims first to provide reliable and predictable code, while maintaining ease-of-use. Gonum is different from other popular scientific libraries, in that the Go language does not allow operator or method overloading. On the surface, this often means that the same algorithm requires a few more lines of code in Go. We fully recognize that sexy one-liners are rare with Gonum.

We accept this cost because we believe it comes with an enormous benefit. The Gonum function and method signatures make the algorithmic outputs clear, and it is easy to identify the code being executed and examine the implementation. Science is built on understanding how an experiment was performed and what the results are. We believe scientific code should be no different. In fact, Gonum is partly distinguished from other libraries in that you only need one programming language to read Gonum code (that said, it is also easy to call into existing C and Fortran libraries). This philosophy of simplicity has many follow-on benefits. For example, dense one-liners can be hard to understand, creating a barrier for others to confirm correctness, and making future modifications difficult. Additionally, one-liners often obscure the necessary operations to execute that line of code. This creates a tension between code that is terse, and a targeted implementation that is efficient. The construction of Gonum encourages users to implement algorithms in a uniform style, making the code easy to read and consistent between users.

The use of Go as a base language has many benefits beyond simplicity. Go is fast, approaching the speed of C. Go’s language primitives are great for parallel computing, and in fact Gonum code can often be made to run in parallel by setting a flag. Go is designed for [“programming in the large”](https://talks.golang.org/2012/splash.article), a huge benefit for building an ecosystem of libraries that work with and build on top of one another. Go has extremely legible compile errors, full stack traces, trivial package downloading, automatic makefiles and import resolution, code formatting tools, easy code documentation, a race detector, and the list goes on.

We believe in a new foundation for scientific computing, and we hope you’ll join us. Please check back for more discussion on the philosophy of Gonum and the design decisions for specific packages.

## Getting started with Gonum

### Downloading the libraries

First, you need to [install Go](https://golang.org/doc/install) if it is not already installed on your machine. It is recommended that you use the most recent version of Go. Run

	go get -u -t gonum.org/v1/gonum/...

to download the main set of Gonum packages. That’s it!
You can test that everything is working properly with

	go test gonum.org/v1/...

This will take a few minutes. Packages should all have an “ok” or “?” next to them. While the tests are running, please feel free to browse the source code!

### Learning Go

The [Go tour](https://tour.golang.org/) is an excellent introduction to the Go programming language. For quick experiments with the language, the [Go playground](https://play.golang.org/)is a very nice sandbox, though unfortunately you cannot import the Gonum librares. We also recommend reading the [Go FAQ](https://golang.org/doc/faq) and[effective Go](https://golang.org/doc/effective_go.html) pages. If you have specific questions, check out the Go language[specification](https://golang.org/ref/spec), which provides an official description of the behavior of the language. The Go specification is remarkably short and legible compared with other language specifications, and a better situation than for the many languages without an official specification.

### Learning Gonum

The best way to learn about particular packages and functions is through the source code documentation. The godoc [website](https://godoc.org/) automatically generates documentation pages from publically available source code. For most Go packages (not just Gonum), going to `https://godoc.org/<package-import-path>`will give you documentation about that particular package. For example, `https://godoc.org/gonum.org/v1/gonum/mat` will give documentation about Gonum’s matrix package, as well as documentation for specific functions. Go to `https://godoc.org/gonum.org/v1/gonum/graph/topo` and you will see documentation about our graph topology routines, for example for finding the “strongly connected components” of a graph. Note that sometimes godoc lists functions below the relevant type, for example the function to create a new dense matrix `mat.NewDense`, is listed under the`Dense` type. At the bottom of the index you will see a list of specific code examples, and at the very bottom of the godoc page, you can see a list of subpackages, if any (for instance, scroll to the bottom of `https://godoc.org/gonum.org/v1/gonum/stat`).

Please also check future posts on this blog for extended commentary on Gonum packages and their effective use.

For questions on the Gonum libraries, please join us at the[Gonum-dev](https://groups.google.com/forum/#!forum/gonum-dev) mailing list.

## How can I help?

The Gonum contributors are a self-assembled group of scientists, engineers and programmers from around the world. If you’re worried that you don’t know us, don’t be! At the time of writing, none of the primary contributors have ever met in person, and until recently, we all lived in different time zones. Please file issues you find at our[github repository](https://github.com/gonum/gonum). Pull requests are encouraged, please see the [contributing guidelines](https://github.com/gonum/gonum/blob/master/CONTRIBUTING.md)for more details. Small changes can be proposed directly, larger changes should be discussed at the Gonum-dev mailing list (linked above).

*By Brendan Tracey*