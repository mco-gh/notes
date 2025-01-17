Writing type parametric functions in Go - Andrew Gallant's Blog

# Writing type parametric functions in Go

 *Apr 6, 2013*

Go’s only method of compile time safe polymorphism is structural subtyping, and this article will do nothing to change that. Instead, I’m going to present a package `ty` with facilities to write type parametric functions in Go that maintain **run time** type safety, while also being convenient for the caller to use.

By **run time type safety**, I mean that the types of a function’s arguments are consistent with its parametric type *or else the function predictably fails at run time* with a reasonable error message. Stated differently, a lack of run time type safety would permit arguments that are inconsistent with the function’s parametric type at the call site, but might fail with unrelated and hard to debug errors (or worse, not fail at all). Thus, run time type safety in this context is a statement about failure modes.

I will provide examples that clarify run time type safety later in the article.

### Warm up

Briefly, type parametric functions operate on their inputs without explicit knowledge of the types of their inputs. That is, they are parameterized on the types of their arguments.

If Go had parametric polymorphism available to users, here’s what a `Map`function *might* look like:

	// Forall A, B ...
	func Map(f func(A) B, xs []A) []B {
	    ys := make([]B, len(xs))
	    for i, x := range xs {
	        ys[i] = f(x)
	    }
	    return ys
	}
	Map(func(x int) int { return x * x }, []int{1, 2, 3})
	// Returns: [1, 4, 9]

Note: Go has several built in functions that use parametric polymorphism:[append](http://golang.org/pkg/builtin/#append),[close](http://golang.org/pkg/builtin/#close),[delete](http://golang.org/pkg/builtin/#delete),[copy](http://golang.org/pkg/builtin/#copy),[cap](http://golang.org/pkg/builtin/#cap)and[len](http://golang.org/pkg/builtin/#len).

### Purpose

The purpose of the `ty` package is to give the programmer the ability to write the aforementioned `Map` function such that

- It is easy for the caller to use.
- The `Map` function is not overly difficult to write.
- Type safety is maintained at run time.

### Motivation

Let’s skip the brouhaha and *assume* you buy into the notion that type parametric functions are useful in the hands of the user. The question remains: why is such an addition useful when Go already has powerful reflection tools? The answer is: working with reflection can be terribly inconvenient, and verifying the consistency of types can be complex and error prone.

I will attempt to convince you of this with code samples using the familiar`Map` function.

### An attempt without using reflection

In Go, the type `interface{}` corresponds to the set of types that implement the empty interface. Stated differently: all Go types. It is appropriate to think of an `interface{}` type as conceptually analogous to a `void *` in C, but there are important operational differences. For example, Go is memory safe, which prevents arbitrary conversion of a value from one type to another. This limitation in particular makes a `Map` function without reflection more clumsy than how you might write and use it in C. Also, in Go, a value with `interface{}` type still contains information about the value’s underlying type, which we will exploit later.

Let’s start with writing `Map` using `interface{}`:

	func Map(f func(interface{}) interface{}, xs []interface{}) []interface{} {
	  ys := make([]interface{}, len(xs))
	  for i, x := range xs {
	    ys[i] = f(x)
	  }
	  return ys
	}

This part isn’t so bad, but the burden on the caller is outrageous:

	square := func(x interface{}) interface{} {
	  return x.(int) * x.(int)
	}
	nums := []int{1, 2, 3, 4}

	gnums := make([]interface{}, len(nums))
	for i, x := range nums {
	  gnums[i] = x
	}
	gsquared := Map(square, gnums)
	squared := make([]int, len(gsquared))
	for i, x := range gsquared {
	  squared[i] = x.(int)
	}

Since we can’t do arbitrary type conversions, we need to allocate a new slice for the arguments, while also allocating a new slice for the return value of `interface{}` and type assert each element individually. (A type assertion in Go is a way to state knowledge about the underlying type of an interface value. In the above code, the type assertion will crash the program if it fails.) Moreover, the function `f` provided by the caller must *also* be generic. Anything with this much burden on the caller probably isn’t worth it.

With regard to run time type safety, most of it is contained inside the user-supplied `f` function, but error messages don’t address the underlying cause. For example, the following code

	Map(func(a interface{}) interface{} { return len(a.(string)) },
	    []interface{}{1, 2, 3})

fails with a stack trace and an error message: `interface conversion: interface is int, not string`.

### A reflective interlude

For those that haven’t worked with reflection in Go before,[The Laws of Reflection](http://blog.golang.org/2011/09/laws-of-reflection.html)is a great introduction to the topic. It is suitable even if you don’t know Go.

I don’t consider it to be a necessary read before moving on, but it is important to know this (from “The Laws of Reflection”):

> Reflection in computing is the ability of a program to examine its own structure, particularly through types; it’s a form of metaprogramming.

With that, let us move on to a `Map` that uses reflection.

### Reflection in Go 1.0.x

We can make the burden a bit easier on the caller using `Map` by wielding the power of reflection to examine and manipulate the structure of a program. We wield this power by exploiting the fact that `interface{}` values still contain information about the underlying type of the value it contains. But this exploitation comes with the price of a more painful `Map` function:

	func Map(f interface{}, xs interface{}) []interface{} {
	  vf := reflect.ValueOf(f)
	  vxs := reflect.ValueOf(xs)
	  ys := make([]interface{}, vxs.Len())

	  for i := 0; i < vxs.Len(); i++ {
	    ys[i] = vf.Call([]reflect.Value{vxs.Index(i)})[0].Interface()
	  }
	  return ys
	}

Here are the key differences between this `Map` and the last one:

- The type of `f` is now `interface{}` instead of `func(interface{}) interface{}`.
- The type of `xs` is now `interface{}` instead of `[]interface{}`.
- The user’s `f` function is now applied using reflection instead of a regular Go function application.
- The `xs` slice is accessed using reflection instead of the regular Go indexing operation.

The differentiating theme here is to move the entire world of `Map` into an `interface{}` type and rely on the[reflect](http://golang.org/pkg/reflect)package to operate on the structure of those unknown values. In particular, we’ve given up some compile time type safety in exchange for lifting some burdens from the caller:

	square := func(x int) int {
	  return x * x
	}
	nums := []int{1, 2, 3, 4}

	gsquared := Map(square, nums)
	squared := make([]int, len(gsquared))
	for i, x := range gsquared {
	  squared[i] = x.(int)
	}

Namely, the client is no longer mandated to write `f` as a generic function. It can use its own types without worrying about type assertions. Moreover, the client no longer needs to allocate a new slice for the *input* of the function.

But the caller still needs to type assert each element in the returned slice. How can we remove such a burden?

It turns out that it’s impossible using reflection in Go 1.0.x.

### Reflection in Go tip (soon to be Go 1.1)

The [release notes for Go 1.1](http://tip.golang.org/doc/go1.1) detail many welcomed changes, but for this article, we[care about the changes made to the reflect package](http://tip.golang.org/doc/go1.1#reflect). In particular, three new critical functions were added:[ChanOf](http://tip.golang.org/pkg/reflect/#ChanOf),[MapOf](http://tip.golang.org/pkg/reflect/#MapOf) and[SliceOf](http://tip.golang.org/pkg/reflect/#SliceOf). These functions allow the *creation of new types from existing types*. With Go 1.0.x, such operations were not possible (except with pointer types).

This now allows us to write a `Map` function that uses the return type of `f`to construct a new slice type, which we can then populate and return to the caller.

	func Map(f interface{}, xs interface{}) interface{} {
	  vf := reflect.ValueOf(f)
	  vxs := reflect.ValueOf(xs)

	  tys := reflect.SliceOf(vf.Type().Out(0))
	  vys := reflect.MakeSlice(tys, vxs.Len(), vxs.Len())

	  for i := 0; i < vxs.Len(); i++ {
	    y := vf.Call([]reflect.Value{vxs.Index(i)})[0]
	    vys.Index(i).Set(y)
	  }
	  return vys.Interface()
	}

Our `Map` function has gotten a bit more annoying, but after practice with the`reflect` package, it’s possible to see how most lines correspond to a regular Go operation. On the bright side, the caller’s obligations have dropped to nearly the level that we saw with the first generic `Map` example:

	squared := Map(func(x int) int { return x * x }, []int{1, 2, 3}).([]int)

The only burden on the caller is to type assert the return value of the function. Indeed, this is the best we can do in this regard: all type parametric functions that return a value from now on have this restriction and*only* this restriction unless stated otherwise.

### Run time type safety

The most recent iteration of the `Map` function is annoying to write, but not*quite* painful. Unfortunately, that’s about to change. Consider what happens when we try to subvert the parametric type of `Map`(which is `func(func(A) B, []A) []B`) by running this code:

	Map(func(a string) int { return len(a) }, []int{1, 2, 3}).([]int)

The program fails with a stack trace and an error message:`Call using int as type string`.

Since our program is small, it is easy to see where we went wrong. But in a larger program, such an error message can be confusing. Moreover, type failures could occur anywhere which might make them more confusing. Even worse, other type parametric functions (not `Map`) might not fail at all—which results in a total loss of type safety, even at run time.

Therefore, to provide useful and consistent error messages, we must check the invariants in the parametric type of `Map`. Why? Because the Go type of `Map`is `func(interface{}, interface{}) interface{}` while the parametric type of`Map` is `func(func(A) B, []A) []B`. Since an `interface{}` type can correspond to *any* type, we need to be exhaustive in our checking:

1. Map’s first parameter type must be `func(A) B`
2. Map’s second parameter type must be `[]A1` where `A == A1`.
3. Map’s return type must be `[]B1` where `B == B1`.

Given those invariants, here’s a `Map` function that enforces them and produces sane error messages. (I leave it to the reader to imagine better ones.)

	func Map(f interface{}, xs interface{}) interface{} {
	  vf := reflect.ValueOf(f)
	  vxs := reflect.ValueOf(xs)

	  ftype := vf.Type()
	  xstype := vxs.Type()

	  // 1) Map's first parameter type must be `func(A) B`
	  if ftype.Kind() != reflect.Func {
	    log.Panicf("`f` should be %s but got %s", reflect.Func, ftype.Kind())
	  }
	  if ftype.NumIn() != 1 {
	    log.Panicf("`f` should have 1 parameter but it has %d parameters",
	      ftype.NumIn())
	  }
	  if ftype.NumOut() != 1 {
	    log.Panicf("`f` should return 1 value but it returns %d values",
	      ftype.NumOut())
	  }

	  // 2) Map's second parameter type must be `[]A1` where `A == A1`.
	  if xstype.Kind() != reflect.Slice {
	    log.Panicf("`xs` should be %s but got %s", reflect.Slice, xstype.Kind())
	  }
	  if xstype.Elem() != ftype.In(0) {
	    log.Panicf("type of `f`'s parameter should be %s but xs contains %s",
	      ftype.In(0), xstype.Elem())
	  }

	  // 3) Map's return type must be `[]B1` where `B == B1`.
	  tys := reflect.SliceOf(vf.Type().Out(0))

	  vys := reflect.MakeSlice(tys, vxs.Len(), vxs.Len())
	  for i := 0; i < vxs.Len(); i++ {
	    y := vf.Call([]reflect.Value{vxs.Index(i)})[0]
	    vys.Index(i).Set(y)
	  }
	  return vys.Interface()
	}

The result is a lot of pain, but when one tries to subvert its type

	Map(func(a string) int { return len(a) }, []int{1, 2, 3}).([]int)

you’ll get a stack trace with a better error message:`type of f's parameter should be string but xs contains int`. The error message is better than what we’ve seen, but the type checking in `Map` has dwarfed the actual function of `Map`.

Fortunately, this pain can be avoided through abstraction.

### Unification

Recall the type constraints for `Map`, which has parametric type `func(func(A) B, []A) []B`:

1. Map’s first parameter type must be `func(A) B`
2. Map’s second parameter type must be `[]A1` where `A == A1`.
3. Map’s return type must be `[]B1` where `B == B1`.

We can interpret the above constraints as a *unification* problem, which in this case is the problem of finding a set of valid Go types that can replace all instances of `A`, `A1`, `B` and `B1` in the type of `Map`. We can view these Go types as a set of *substitutions*.

More generally, given a *parametric* type of a function and the*non-parametric* types of the function’s arguments at run time, find a set of substitutions that *unifies* the parametric type with its arguments. As a bonus, we can use those substitutions to construct new types that `Map` may use to make new values.

To be concrete, let’s restate the constraints of `Map` in terms of a unification problem. (Note that this isn’t really a traditional unification problem, since the types of the arguments are not allowed to be parametric.)

Assume that all types with the `Go` prefix are real Go types like `int`,`string` or `[]byte`.

1. Unify the type `func(A) B` with the first argument. The result is a substitution from `A` to `GoA` and a substitution from `B` to `GoB`.

2. Unify the type `[]A` with the second argument. The result is a substitution from `A` to `GoA1`  **such that `GoA1 == GoA`**.

3. Substitute `GoB` into `[]B` to get `[]GoB`.
So that if `Map` is invoked like so

	strlen := func(s string) int { return len(s) }
	lens := Map(strlen, []string{"abc", "ab", "a"}).([]int)

then `A = string` and `B = int`.

A generalized version of this algorithm is implemented in[ty.Check](https://github.com/BurntSushi/ty/blob/master/type-check.go#L130), which is too big to list here. The input of `ty.Check` is a pointer to the type of a parametric function and every argument. The output is a slice of reflection values of the arguments, a slice of reflection types of the return values and a type environment containing the substitutions.

### Writing `Map` with `ty.Check`

Here’s the code:

	// Map has a parametric type:
	//
	//  func Map(f func(A) B, xs []A) []B
	//
	// Map returns the list corresponding to the return value of applying
	// `f` to each element in `xs`.
	func Map(f, xs interface{}) interface{} {
	  chk := ty.Check(
	    new(func(func(ty.A) ty.B, []ty.A) []ty.B),
	    f, xs)
	  vf, vxs, tys := chk.Args[0], chk.Args[1], chk.Returns[0]

	  xsLen := vxs.Len()
	  vys := reflect.MakeSlice(tys, xsLen, xsLen)
	  for i := 0; i < xsLen; i++ {
	    vy := vf.Call([]reflect.Value{vxs.Index(i)})[0]
	    vys.Index(i).Set(vy)
	  }
	  return vys.Interface()
	}

The latter half of the function is something you ought to be deeply familiar with by now. But the first parts of the function are new and worth inspection:

	chk := ty.Check(
	  new(func(func(ty.A) ty.B, []ty.A) []ty.B),
	  f, xs)

The first argument to `ty.Check` is a `nil` function pointer with a parametric type. Even though it doesn’t point to a valid function, the `Check` function can still query the type information.

But wait. How am I writing a parametric type in Go? The trick is to define a type that can never be equal to any other type unless explicitly declared to be:

	type TypeVariable struct {
	    noImitation struct{}
	}

	type A TypeVariable
	type B TypeVariable

And by convention, the `ty.Check` function interprets those types (and only those types) to be parametric. You may define your own type variables too:

	type K ty.TypeVariable
	type V ty.TypeVariable

`ty.Check` has the following useful invariant: If `Check` returns, then the types of the arguments are consistent with the parametric type of the function, *and* the parametric return types of the function were made into valid Go types that are not parametric. Otherwise, there is a bug in `ty.Check`.

Let’s test that invariant. Using the above definition of `Map`, if one tries to run this code

	Map(func(a string) int { return len(a) }, []int{1, 2, 3}).([]int)

then you’ll get a stack trace and a descriptive error message

	Error type checking
	        func(func(ty.A) ty.B, []ty.A) []ty.B
	with argument types
	        (func(string) int, []int)
	Type error when unifying type '[]ty.A' and '[]int': Type variable A expected
	type 'string' but got 'int'.

### Can we write functions other than `Map`?

Sure. Let’s take a look at how to shuffle *any* slice in place.

	// Shuffle has a parametric type:
	//
	//  func Shuffle(xs []A)
	//
	// Shuffle shuffles `xs` in place using a default random number
	// generator.
	func Shuffle(xs interface{}) {
	  chk := ty.Check(
	    new(func([]ty.A)),
	    xs)
	  vxs := chk.Args[0]

	  // Used for swapping in the loop.
	  // Equivalent to `var tmp A`.
	  tmp := reflect.New(vxs.Type().Elem()).Elem()

	  // Implements the Fisher-Yates shuffle: http://goo.gl/Hb9vg
	  for i := vxs.Len() - 1; i >= 1; i-- {
	    j := rand.Intn(i + 1)

	    // Swapping is a bit painful.
	    tmp.Set(vxs.Index(i))
	    vxs.Index(i).Set(vxs.Index(j))
	    vxs.Index(j).Set(tmp)
	  }
	}

Or an implementation of set union, where a set is a map from any type that can be a key to a bool:

	// Union has a parametric type:
	//
	//  func Union(a map[A]bool, b map[A]bool) map[A]bool
	//
	// Union returns the union of two sets, where a set is represented as a
	// `map[A]bool`. The sets `a` and `b` are not modified.
	func Union(a, b interface{}) interface{} {
	  chk := ty.Check(
	    new(func(map[ty.A]bool, map[ty.A]bool) map[ty.A]bool),
	    a, b)
	  va, vb, tc := chk.Args[0], chk.Args[1], chk.Returns[0]

	  vtrue := reflect.ValueOf(true)
	  vc := reflect.MakeMap(tc)
	  for _, vkey := range va.MapKeys() {
	    vc.SetMapIndex(vkey, vtrue)
	  }
	  for _, vkey := range vb.MapKeys() {
	    vc.SetMapIndex(vkey, vtrue)
	  }
	  return vc.Interface()
	}

Which can be used like so:

	A := map[string]bool{
	  "springsteen": true,
	  "j. geils": true,
	  "seger": true,
	}
	B := map[string]bool{
	  "petty": true,
	  "seger": true,
	}
	AandB := Union(A, B).(map[string]bool)

### Sorts, parallel map, memoization, channels without a fixed buffer…

… and more can be[found in the documentation of the `ty/fun` package](http://godoc.org/github.com/BurntSushi/ty/fun).

Here’s a quick example of memoizing a recursive function that I think is pretty cool:

	// Memoizing a recursive function like `fibonacci`:
	// Write it like normal.
	var fib func(n int64) int64
	fib = func(n int64) int64 {
	  switch n {
	  case 0:
	    return 0
	  case 1:
	    return 1
	  }
	  return fib(n-1) + fib(n-2)
	}

	// Wrap it with a memoizing function.
	// The type assert here is the *only* burden on the caller.
	fib = fun.Memo(fib).(func(int64) int64)

	// Will keep your CPU busy for a long time
	// without memoization.
	fmt.Println(fib(80))

And here’s the[definition of `Memo`](https://github.com/BurntSushi/ty/blob/master/fun/func.go#L16).

### Back to reality

There’s no such thing as a free lunch. The price one must pay to write type parametric functions in Go is rather large:

1. Type parametric functions are ***SLOW***.
2. Absolutely *zero* compile time type safety.
3. Writing type parametric functions is annoying.
4. Unidiomatic Go.

I think that items `2`, `3` and `4` are fairly self-explanatory if you’ve been reading along. But I have been coy about `1`: the performance of type parametric functions.

As a general rule, they are slow because reflection in Go is slow. In most cases, slow means *at least an order of magnitude* slower than an equivalent implementation that is not type parametric (i.e., hard coded for a particular Go type). But, there is hope yet. Let’s take a look at some benchmarks comparing non-parametric (**builtin**) functions with their type parametric (**reflect**) counterparts.

	benchmark                    builtin ns/op  reflect ns/op        delta
	BenchmarkFibonacciMemo-12             5895          43896     +644.63%
	BenchmarkFibonacciNoMemo-12        6827001        6829859       +0.04%
	BenchmarkParMapSquare-12            408320         572307      +40.16%
	BenchmarkParMapPrime-12            5289594        5510075       +4.17%
	BenchmarkMapSquare-12                 8499         457844    +5287.03%
	BenchmarkMapPrime-12              34265372       32220176       -5.97%
	BenchmarkShuffle-12                 240036        1018408     +324.27%
	BenchmarkSample-12                  262565         271122       +3.26%
	BenchmarkSort-12                    137293        7716737    +5520.63%
	BenchmarkQuickSort-12                 6325        6051563   +95576.89%

Benchmarks were run on an Intel i7 3930K (12 threads), 32GB of memory, Linux 3.8.4 and Go tip on commit `c879a45c3389` with `GOMAXPROCS=12`. Code for all benchmarks can be found in[*test.go](https://github.com/BurntSushi/ty/tree/master/fun) files.

There is a lot of data in these benchmarks, so I won’t talk about everything. However, it is interesting to see that there are several data points where type parametric functions don’t perform measurably worse. For example, let’s look at our old friend `Map`. The type parametric version gets blown away in the `MapSquare` benchmark, which just squares a slice of integers. But the`MapPrime` benchmark has them performing similarly.

The key is what the benchmark `MapPrime` is doing: performing a very naive algorithm to find the prime factorization of every element in a slice of large integers. The operation itself ends up dwarfing the overhead of using reflection. From a performance perspective, this means `Map` is only useful when either performance doesn’t matter or when you know the operation being performed isn’t trivial.

But what about `ParMap`? `ParMap` is a function that spawns `N` goroutines and computes `f` over the slice concurrently. Even when not using reflection this approach bears a lot of overhead because of synchronization. Indeed, the`ParMapSquare` benchmark shows that the type parametric version is only slightly slower than the built in version. And of course, it is comparable in the `ParMapPrime` benchmark as well. This suggests that, from a performance perspective, the decision procedure for using a builtin `ParMap` is the same as the decision procedure for using a reflective `ParMap`.

If you have any questions about the benchmarks, I’d be happy to answer them in the comments.

### What’s next?

Tumbling down the rabbit hole with[parametric data types](http://godoc.org/github.com/BurntSushi/ty/data).

### Show me the code, dammit.

- Working examples of all code in this article can be found[in a gist](https://gist.github.com/BurntSushi/5298812). (Although you will need Go tip to run most of them.)
- [Repository](https://github.com/BurntSushi/ty) for the`ty` package, which includes `ty/fun` and `ty/data`.
- [Documentation](http://godoc.org/github.com/BurntSushi/ty)with many more details and examples than were provided in this article.