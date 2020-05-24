Common Gotchas in Go - 0xDEADBEEF

# Common Gotchas in Go

Jan 1, 2018

- go

First thing is first. Happy New Years 🎉🎉

Now that’s out of the way, let’s talk about Go. I recently finished making my first real Go program. It’s called “Fix All Conflicts” or [fac](https://github.com/mkchoi212/fac) for short. It’s an easy-to-use console user interface for fixing git merge conflicts. I made it because I never found a merge tool that was intuitive enough to use.

The process was quite fun and I learned a lot about Go in the process. So, to wrap up my first official foray into Rob Pike’s mystical land of gophers, I decided to write down some of the common “Gotchas!” that any beginning Gopher - me - can run into.

![golang-1.jpg](../_resources/d51e22678c2b55d5ad38dc079019a00c.jpg)
>
> Gophers can be quite aggressive sometimes.

# ⚠️ #1. Range

The `range` function is one of the most commonly used functions in Go. Here’s a sample use case of the `range` function. Note that for some demented reason, we decided to make all the animals in the zoo have `999` legs.

	type Animal struct {
		name string
		legs int
	}

	func main() {
	  zoo := []Animal{ Animal{ "Dog", 4 },
	                   Animal{ "Chicken", 2 },
	                   Animal{ "Snail", 0 },
	                 }

	  fmt.Printf("-> Before update %v\n", zoo)

	  for _, animal := range zoo {
	    // 🚨 Oppps! `animal` is a copy of an element 😧
	    animal.legs = 999
	  }

	  fmt.Printf("\n-> After update %v\n", zoo)
	}

The above code looks innocent enough. However, you may be surprised to find that the two `fmt.Printf()` statements yield the same results.

	-> Before update [{Dog 4} {Chicken 2} {Snail 0}]
	-> After update 🚨🚨🚨 [{Dog 4} {Chicken 2} {Snail 0}]

#### Lesson

>

> Value property of `range`>  (stored here as `animal`> ) is a **> copy of the value from `zoo`> , not a pointer to the value in `zoo`> .**

#### 🛠️ The Fix

In order to modify an element within the array, we must change the element via its **pointer**.

	for idx, _ := range zoo {
	  zoo[idx].legs = 999
	}

This may look quite trivial but you may be surprised to find this as a one of the most common source of bugs; at least for me!

[» Go playground #1 for you to play around in](https://play.golang.org/p/jhL_MNbXnPC)

# ⚠️ #2. The … thingy

You may have used the `…` keyword in the C programming language to create a [variadic function](https://www.gnu.org/software/libc/manual/html_node/Variadic-Functions.html); variadic function is a function that takes a variable number or type of arguments.

In C, you have to successively call the `va_arg` macro in order to access the optional arguments. And if you use the variadic argument in any other way, the compiler will throw an error.

	int add_em_up (int count,...) {
	  ...
	  va_start (ap, count);         /* Initialize the argument list */
	  for (i = 0; i < count; i++)
	      sum += va_arg(ap, int);   /* Get the next argument value */
	  va_end (ap);                  /* Clean up */
	  return sum
	}

In Go however, things are similar but quite different at the same time. Here is a variadic function `myFprint` in Go. Notice how the variadic argument `a` is being used.

	func myFprint(format string, a ...interface{}) {
		if len(a) == 0 {
			fmt.Printf(format)
		} else {
			// ⚠️ `a` should be `a...`
			fmt.Printf(format, a)
			// ✅
			fmt.Printf(format, a...)
		}
	}

	func main() {
		myFprint("%s : line %d\n", "file.txt", 49)
	}

	[file.txt %!s(int=49)] : line %!d(MISSING)
	file.txt : line 49

You’d think that the compiler would throw an error here for using the variadic parameter `a` in a wrong way. But notice how `fmt.Sprintf` just used the first argument in `a ` without throwing a fit.

#### Lesson

>
> In Go, **> variadic parameters are converted to slices by the compiler**

This means that the variadic argument `a` is in fact, just a slice. Because of this, the code below is completely valid.

	// `a` is just a slice!
	for _, elem := range a {
	    fmt.Println(elem)
	}

#### 🛠️ The Fix

>
**> Remember to type ALL THREE DOTS whenever using variadic parameters!**

[» Go playground #2 for you to play around in](https://play.golang.org/p/303g8_1IVFD)

# ⚠️ #3. Slicing

If you have done your fair share of slicing in Python, you may remember that slicing in Python gives you a new list with just the references to the elements copied over. This property allows for code like this in Python.

	a = [1, 2, 3]
	b = a[:2]			# 👀 a completely new list!
	b[0] = 999
	>>> a
	[1, 2, 3]
	>>> b
	[999, 2]

However if you try the same thing in Go, you get something else.

	func main() {
	  data := []int{1,2,3}
	  slice := data[:2]
	  slice[0] = 999

	  fmt.Println(data)
	  fmt.Println(slice)
	}

	[999 2 3]
	[999 2]

#### Lesson

>

> In Go, **> a slice shares the same backing array and capacity as the original.**>  So if you change an element in the slice, the original contents are modified as well.

#### 🛠️ The Fix

If you want to get an independent slice, you have two options.

	// Option #1
	// appending elements to a nil slice
	// `...` changes slice to arguments for the variadic function `append`
	a := append([]int{}, data[:2]...)

	// Option #1
	// Create slice with length of 2
	// copy(dest, src)
	a := make([]int, 2)
	copy(a, data[:2]

And according to [StackOverflow](https://stackoverflow.com/a/44337887/4064189), the `append` option is slightly faster than the `make. + copy` option!

[» Go playground #3 for you to play around in](https://play.golang.org/p/HvVFmQZTcjp)

 **Previous** Dec 23, 2017

 [« Things we can learn from Microsoft](https://deadbeef.me/2017/12/learn-from-microsoft)

- [1 comment]()
- [**deadbeef.me**](https://disqus.com/home/forums/deadbeef-me/)
- [(L)](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  2](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)
- [⤤  Share](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/geertjohan/)

 [Geert-Johan](https://disqus.com/by/geertjohan/)    •  [an hour ago](https://deadbeef.me/2018/01/go-gotchas#comment-3687866885)

It's probably interesting to note that changing slice data only affects other slices of the same underlying array when you do not append values that require the underlying array to be copied.

See [https://play.golang.org/p/t...](https://disq.us/url?url=https%3A%2F%2Fplay.golang.org%2Fp%2FtH5Gd6TcAOE%3AbO_d5urbwyxjtulmYaol8fkUjXE&cuid=5209802)

Assuming that it does always change the same underlying array is yet another gotcha :)

    - [−](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)

## Also on **deadbeef.me**

- [

### RSS == Really Sucky Syndrome

    - 3 comments •

    - 18 days ago

[Jan van den Berg— Hi! I recognize a lot of what you said, I am also an avid HN refresher and RSS user :) However I am subscribed to …](https://disq.us/?url=https%3A%2F%2Fwww.deadbeef.me%2F2017%2F12%2Frss&key=9hYuGHT0cIRMaO2C3jffAQ)](https://disq.us/?url=https%3A%2F%2Fwww.deadbeef.me%2F2017%2F12%2Frss&key=9hYuGHT0cIRMaO2C3jffAQ)

- [

### Things we can learn from Microsoft

    - 7 comments •

    - 10 days ago

[Andrew— Apparently you can't handle facts or drugs. You can whine and complain you don't like what I've said, but you can't argue with …](https://disq.us/?url=https%3A%2F%2Fwww.deadbeef.me%2F2017%2F12%2Flearn-from-microsoft&key=Iczvq7jz1hbGydqPZZLGrQ)](https://disq.us/?url=https%3A%2F%2Fwww.deadbeef.me%2F2017%2F12%2Flearn-from-microsoft&key=Iczvq7jz1hbGydqPZZLGrQ)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=deadbeef-me&t_i=%2F2018%2F01%2Fgo-gotchas&t_u=https%3A%2F%2Fwww.deadbeef.me%2F2018%2F01%2Fgo-gotchas&t_d=Common%20Gotchas%20in%20Go&t_t=Common%20Gotchas%20in%20Go&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=deadbeef-me&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)