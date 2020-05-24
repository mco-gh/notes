A Comprehensive Guide of Arrays and Slices in Golang (and their differences)

# A Comprehensive Guide of Arrays and Slices in Golang (and their differences)

June 21, 2019

At first, it’s easy to see arrays and slices as the same thing: a data structure to represent collections. However, they are actually quite different from one another.

In this post we will explore their differences and implementation in Go.

We will then look at some examples so that you can make a more informed decision on when to use them.

[

     [banner.webp](../_resources/1d2662c8d137499842703cfa9eba3f39.webp)](https://www.sohamkamani.com/static/dd0335320a35cb62fecb945fadcd5994/3b243/banner.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='75' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='189' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#arrays)Arrays

An array is a fixed collection of data. The emphasis here is on *fixed*, because once you set the length of an array, it cannot be changed.

Lets take an example of declaring an array of four integers:
`arr := [4]int{3, 2, 5, 4}`

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='76' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#length-and-type)Length and type

The `arr` variable we defined in the above example is of type `[4]int`, which is an array of size 4. What’s important to note here, is that the `4` is included in the type definition.

What this means is that two arrays of different lengths are actually *two separate types.* You cannot equate arrays of different lengths, and you also cannot assign the value of one to the other:

	longerArr := [5]int{5, 7, 1, 2, 0}

	longerArr = arr
	// This gives a compilation error

	longerArr == arr
	// This gives a compilation error

I found that a good way to think of arrays is in terms of structs. If we could construct the `struct` equivalent of arrays, it would probably look like this:

	// Struct equivalent for an array of length 4
	type int4 struct {
	  e0 int
	  e1 int
	  e2 int
	  e3 int
	}

	// Struct equivalent for an array of length 5
	type int5 struct {
	  e0 int
	  e1 int
	  e2 int
	  e3 int
	  e5 int
	}

	arr := int4{3, 2, 5, 4}
	longerArr := int5{5, 7, 1, 2, 0}

> It’s not recommended to actually do this, but it’s a good way to get an idea of how arrays of different lengths are different types altogether.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='77' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='280' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#memory-representation)Memory representation

An array is stored as a sequence of `n` blocks of the type specified:

![](https://www.sohamkamani.com/array-representation-f504431a3689d4f363307dec9a581199.svg)

This memory is allocated as soon as you initialize a variable of the array type.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='78' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='285' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#reference-passing)Reference passing

In Go, there is no such thing as passing by reference. Everything is passed by value. If you assign the value of an array to another variable, the *entire value is copied.*

![](https://www.sohamkamani.com/array-assignment-cd364be92ea8ab668de726ee74240e96.svg)

If you want to pass just the “reference” to the array, you can use pointers:

![](https://www.sohamkamani.com/array-pointers-b0858cea1687796e01c574070d1e9779.svg)

In memory allocation, and in function, the array is actually a really simple data type, and works in much the same way as structs.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='79' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='293' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#slices)Slices

You can think of slices as an advanced implementation on top of arrays.

Slices were implemented in Go to cover some of the more common use cases faced by developers when working with collections, like dynamically changing their size.

Declaring a slice is almost the same as declaring an array, except that you must omit the length specifier:

`slice := []int{4, 5, 3}`

By looking at the code, slices and arrays look pretty similar, but there are actually significant differences in their implementation and uses.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='80' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='311' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#memory-representation-1)Memory representation

A slice is allocated differently from an array, and is actually a modified pointer. Each slice contains three pieces of information:

1. The pointer to the sequence of data
2. The length: which denotes the total number of elements currently contained.
3. The capacity: which is the total number of memory locations provisioned.

![](https://www.sohamkamani.com/slice-representation-b58621b4b931e0cd4ac76077ed7e40fc.svg)

It follows then that slices of different lengths *can* be assigned each other’s values. Their type is the same, with the pointer, length, and capacity changing:

	slice1 := []int{6, 1, 2}
	slice2 := []int{9, 3}

	// slices of any length can be assigned to other slice types
	slice1 = slice2

A slice, unlike an array, does not allocate the memory of the data blocks during initialization. In fact, slices are initialized with the `nil` value.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='81' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='345' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#reference-passing-1)Reference passing

When you assign a slice to another variable, you *still* pass by value. The value here refers to just the pointer, length, and capacity, and *not* the memory occupied by the elements themselves.

![](https://www.sohamkamani.com/slice-assignment-860c715a14ca11d6921be9f599078439.svg)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='82' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='351' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#adding-new-elements)Adding new elements

To add elements to a slice, you normally use the `append` function.

	nums := []int{8, 0}
	nums = append(nums, 8)

Internally, this assigns the value specified to a new element, and returns a new slice. This new slice has it’s length increased by one.

![](https://www.sohamkamani.com/slice-append-be5d1170b1814d00efd0eff301a23249.svg)

If adding an element would need to increase the length beyond the available capacity, new capacity needs to be provisioned (the current capacity is normally doubled in this case).

This is why it’s often recommended to create a slice with the length and capacity specified beforehand (especially if you have a good idea of what it’s size might be):

	arr := make([]int, 0, 5)
	// This creates a slice with length 0 and capacity 5

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='83' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='387' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#should-you-use-arrays-or-slices)Should you use Arrays or Slices?

Arrays and slices are quite different, and consequently, their use cases are quite different as well.

Let’s go through some examples from open source and the Go standard library, to see where they are used.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='84' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='391' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#case-1-uuids)Case 1: UUIDs

[UUIDs](https://www.sohamkamani.com/blog/2016/10/05/uuid1-vs-uuid4/) are 128-bit pieces of data that are often used to uniquely tag an object or entity. They are often represented in dash-separated hex values:

`e39bdaf4-710d-42ea-a29b-58c368b0c53c`

In [Google’s UUID library](https://github.com/google/uuid/blob/c2e93f3ae59f2904160ceaab466009f965df46d6/uuid.go#L19), a UUID is represented as an array of 16 bytes:

`type UUID [16]byte`

This makes sense, since we *know* that a UUID is made out of 128 bits (16 bytes). We are not going to add or remove any bytes from a UUID, and so using an array to represent it makes much more sense that a slice.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='85' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='404' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#case-2-sorting-integers)Case 2: Sorting integers

In this next example, we’re going to look at the `sort.Ints` function from the [sort standard library](https://golang.org/pkg/sort/#Ints):

	s := []int{5, 2, 6, 3, 1, 4} // unsorted
	sort.Ints(s)
	fmt.Println(s)
	// [1 2 3 4 5 6]

The `sort.Ints` function takes a slice of integers and sorts them in place. Slices are preferred here for two reasons:

1. The number of integers is unspecified (there could be any number of integers to sort).

2. The numbers need to be sorted in place. Using an array would pass the entire collection of integers as a value, and so the function would only sort it’s own copy, and not the one passed to it.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='86' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='439' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#conclusion)Conclusion

Now that we’ve covered the key differences between arrays and slices, and their use cases, here are some tips to decide which construct is more suitable:

1. If the entity is described by a set of non-empty items of a fixed length: use arrays.

2. When describing a general collection that you would add or remove elements from, use slices.

3. If a collection can contain any number of elements, use slices.
4. Will you be modifying the collection in some way? If yes, then use slices

As we can see, slices cover the majority of scenarios for creating an application in Go. Still, arrays do have their place, and are incredibly useful when the use case requires them.

Are there any use cases I missed? Are there any interesting use cases where you prefer arrays over slices (or vice-versa)? Let me know in the comments below

- Share this on:
- [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48cGF0aCBmaWxsPSJyZ2IoMjksMTYxLDI0MikiIGQ9Ik00MDAgMzJINDhDMjEuNSAzMiAwIDUzLjUgMCA4MHYzNTJjMCAyNi41IDIxLjUgNDggNDggNDhoMzUyYzI2LjUgMCA0OC0yMS41IDQ4LTQ4VjgwYzAtMjYuNS0yMS41LTQ4LTQ4LTQ4em0tNDguOSAxNTguOGMuMiAyLjguMiA1LjcuMiA4LjUgMCA4Ni43LTY2IDE4Ni42LTE4Ni42IDE4Ni42LTM3LjIgMC03MS43LTEwLjgtMTAwLjctMjkuNCA1LjMuNiAxMC40LjggMTUuOC44IDMwLjcgMCA1OC45LTEwLjQgODEuNC0yOC0yOC44LS42LTUzLTE5LjUtNjEuMy00NS41IDEwLjEgMS41IDE5LjIgMS41IDI5LjYtMS4yLTMwLTYuMS01Mi41LTMyLjUtNTIuNS02NC40di0uOGM4LjcgNC45IDE4LjkgNy45IDI5LjYgOC4zYTY1LjQ0NyA2NS40NDcgMCAwIDEtMjkuMi01NC42YzAtMTIuMiAzLjItMjMuNCA4LjktMzMuMSAzMi4zIDM5LjggODAuOCA2NS44IDEzNS4yIDY4LjYtOS4zLTQ0LjUgMjQtODAuNiA2NC04MC42IDE4LjkgMCAzNS45IDcuOSA0Ny45IDIwLjcgMTQuOC0yLjggMjktOC4zIDQxLjYtMTUuOC00LjkgMTUuMi0xNS4yIDI4LTI4LjggMzYuMSAxMy4yLTEuNCAyNi01LjEgMzcuOC0xMC4yLTguOSAxMy4xLTIwLjEgMjQuNy0zMi45IDM0eiIvPjwvc3ZnPg==)](https://twitter.com/share?url=https://www.sohamkamani.com/blog/golang/arrays-vs-slices/&text=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&via=sohamkamani&hashtags=)
- [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48cGF0aCBmaWxsPSIjM0M1QTk5IiBkPSJNNDQ4IDgwdjM1MmMwIDI2LjUtMjEuNSA0OC00OCA0OGgtODUuM1YzMDIuOGg2MC42bDguNy02Ny42aC02OS4zVjE5MmMwLTE5LjYgNS40LTMyLjkgMzMuNS0zMi45SDM4NFY5OC43Yy02LjItLjgtMjcuNC0yLjctNTIuMi0yLjctNTEuNiAwLTg3IDMxLjUtODcgODkuNHY0OS45SDE4NHY2Ny42aDYwLjlWNDgwSDQ4Yy0yNi41IDAtNDgtMjEuNS00OC00OFY4MGMwLTI2LjUgMjEuNS00OCA0OC00OGgzNTJjMjYuNSAwIDQ4IDIxLjUgNDggNDh6Ii8+PC9zdmc+)](https://facebook.com/sharer.php?u=https://www.sohamkamani.com/blog/golang/arrays-vs-slices/)

* * *

Like what I write? Join my mailing list, and I'll let you know whenever I write another post

Email Address:

## Comments

- [3 comments]()
- [**www.sohamkamani.com**](https://disqus.com/home/forums/sohamkamani/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

[![attach.03c320b14aa9c071da30c904d0a0827f.png](../_resources/e1832a588b49918e9acc6d7c3c680534.png)](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)

![gif-picker.df38180f2d048c25fe42a2b440ff863e.png](../_resources/5006a22ded0c9cbb1ffb485f61457686.png)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)

[![avatar92.jpg](../_resources/a9287176bb4fc13410b560db793a16dd.jpg)](https://disqus.com/by/gophreak/)

 [Raymond](https://disqus.com/by/gophreak/)    •  [8 days ago](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#comment-4515217113)

This is a really good description of the differences between arrays and slices. I think there is also another important distinction to make in terms of iterating too. Something interesting I found out:

When you range over an array, it takes a copy of the array however when you range over a slice it simply references the elements.

Take a look at this example, in each of the functions we are modifying the third element in the array/slice on the first iteration. This means, by the time we are on the third iteration we should get the updated value. When using range and a slice, we do. When using range and an array, we do not.

[https://play.golang.org/p/d...](https://disq.us/url?url=https%3A%2F%2Fplay.golang.org%2Fp%2Fd7Z_44ei2WC%3AdDmySD0AYAVgiqOnuuaQe6wMne8&cuid=3764043)

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)

[![avatar92.jpg](../_resources/95e8ee5503a27af5d9dc0c93553001a5.jpg)](https://disqus.com/by/sohamkamani/)

 [Soham Kamani](https://disqus.com/by/sohamkamani/)  Mod  [*>* Raymond](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#comment-4515217113)  •  [2 days ago](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#comment-4522650192)

Thats a very interesting observation! I think this has to do with the internals of range and how it copies over values in each iteration as opposed to for loops. I will definitely need to dig into this a bit more

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)

[![avatar92.jpg](../_resources/605d966b6983e15cbbcf1f0a4665ca9d.jpg)](https://disqus.com/by/disqus_l47DNpEvhT/)

 [Yayu](https://disqus.com/by/disqus_l47DNpEvhT/)    [*>* Raymond](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#comment-4515217113)  •  [5 days ago](https://www.sohamkamani.com/blog/golang/arrays-vs-slices/#comment-4520340831)

It is intresting! Why?

## Also on **www.sohamkamani.com**

- [

### An introduction to using and visualizing channels in Go ➡️

    - 8 comments •

    - 2 years ago

[![avatar92.jpg](../_resources/bffab483cedf4f22dfe9b0b73457c628.jpg) Hay Trần — GREATE ARTICLE! CAREFULLY EXPLAINATION!!!!!](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2F2017%2F08%2F24%2Fgolang-channels-explained%2F&key=Z3nGz-JvMqmn2j4zzYXynA)](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2F2017%2F08%2F24%2Fgolang-channels-explained%2F&key=Z3nGz-JvMqmn2j4zzYXynA)

- [

###  How to communicate between Python and NodeJs PythonとNodeJ間の通信方法

    - 34 comments •

    - 2 years ago

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Divya Lakshmi Sri — I am having same issue that no result can be printed. I used correct print () syntax even no output](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2F2015%2F08%2F21%2Fpython-nodejs-comm%2F&key=e-TJBgixSLP3fuwx2FLbmQ)](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2F2015%2F08%2F21%2Fpython-nodejs-comm%2F&key=e-TJBgixSLP3fuwx2FLbmQ)

- [

### Implementing JWT based authentication in Golang

    - 11 comments •

    - 5 months ago

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Mayuresh Gaitonde —  actually the only way to invalidate the token on the server side is to change the key. You could technically cycle through a list of …](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2F2019-01-01-jwt-authentication%2F&key=p3cGv4KoxepfK0n389oo_A)](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2F2019-01-01-jwt-authentication%2F&key=p3cGv4KoxepfK0n389oo_A)

- [

### Password authentication and storage in Go (Golang)

    - 3 comments •

    - a year ago

[![avatar92.jpg](../_resources/230fd5d38f29cc57f68f7e69b66e4081.jpg) Andre Tzermias —  Thanks for the tutorial!Is there any reason why you chose to fetch the password for the user and compare it in go-land instead of bcrypting …](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2F2018%2F02%2F25%2Fgolang-password-authentication-and-storage%2F&key=eC1WRGYvmoNAC1cmuInHpg)](https://disq.us/?url=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2F2018%2F02%2F25%2Fgolang-password-authentication-and-storage%2F&key=eC1WRGYvmoNAC1cmuInHpg)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=sohamkamani&t_u=https%3A%2F%2Fwww.sohamkamani.com%2Fblog%2Fgolang%2Farrays-vs-slices%2F&t_d=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&t_t=A%20Comprehensive%20Guide%20of%20Arrays%20and%20Slices%20in%20Golang%20(and%20their%20differences)&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=sohamkamani&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)

![](../_resources/f049e115afda667a7b72930ac7ade239.jpg)

Written by **Soham Kamani**, an [author](https://www.packtpub.com/books/info/authors/soham-kamani),and a full-stack developer who has extensive experience in the JavaScript ecosystem, and building large scale applications in Go. He is an [open source enthusiast](https://github.com/sohamkamani) and an avid blogger. You should [follow him on Twitter](https://twitter.com/sohamkamani)