A Closer Look at Go’s sync Package - Teiva Harsanyi - Medium

# A Closer Look at Go’s sync Package

[![1*PSFDOrIcwjBuyeJI96LKog.jpeg](../_resources/63be195899b50680e1b37914094df8ea.jpg)](https://medium.com/@teivah?source=post_page-----9f4e4a28c35a----------------------)

[Teiva Harsanyi](https://medium.com/@teivah?source=post_page-----9f4e4a28c35a----------------------)

[Nov 26](https://medium.com/@teivah/a-closer-look-at-go-sync-package-9f4e4a28c35a?source=post_page-----9f4e4a28c35a----------------------) · 5 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='160'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='161' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/9f4e4a28c35a/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' viewBox='0 0 29 29' fill='none' class='q js-evernote-checked' data-evernote-id='164'%3e%3cpath d='M5 6.36C5 5.61 5.63 5 6.4 5h16.2c.77 0 1.4.61 1.4 1.36v16.28c0 .75-.63 1.36-1.4 1.36H6.4c-.77 0-1.4-.6-1.4-1.36V6.36z' data-evernote-id='165' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.76 20.9v-8.57H7.89v8.58h2.87zm-1.44-9.75c1 0 1.63-.65 1.63-1.48-.02-.84-.62-1.48-1.6-1.48-.99 0-1.63.64-1.63 1.48 0 .83.62 1.48 1.59 1.48h.01zM12.35 20.9h2.87v-4.79c0-.25.02-.5.1-.7.2-.5.67-1.04 1.46-1.04 1.04 0 1.46.8 1.46 1.95v4.59h2.87v-4.92c0-2.64-1.42-3.87-3.3-3.87-1.55 0-2.23.86-2.61 1.45h.02v-1.24h-2.87c.04.8 0 8.58 0 8.58z' fill='%23fff' data-evernote-id='166' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/9f4e4a28c35a/share/linkedIn?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='169'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='170' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/9f4e4a28c35a/share/facebook?source=post_actions_header---------------------------)

![1*X4c7GE0f_mEunzHjpViAow.jpeg](../_resources/51e636bdc6be7ff033a483a4f6c8cea3.jpg)
![1*X4c7GE0f_mEunzHjpViAow.jpeg](../_resources/70c3bdfd0b440447e03d6d8adf8689bf.jpg)
This is not an analogy for the sync package quality :)

Let’s take a look at the Go package in charge to provide synchronization primitives: `sync`.

# sync.Mutex

`sync.Mutex` is probably the most widely used primitive of the `sync` package. It allows a mutual exclusion on a shared resource (no simultaneous access):

|     |     |
| --- | --- |
| 1   | mutex  := &sync.Mutex{} |
| 2   |     |
| 3   | mutex.Lock() |
| 4   | // Update shared variable (e.g. slice, pointer on a structure, etc.) |
| 5   | mutex.Unlock() |

 [view raw](https://gist.github.com/teivah/b2da65cf2efcb12d039295f044cf212f/raw/fccc37cacb7013d92e84cad1dde77434e1a6c9f7/mutex.go)  [mutex.go](https://gist.github.com/teivah/b2da65cf2efcb12d039295f044cf212f#file-mutex-go) hosted with ❤ by [GitHub](https://github.com/)

It must be pointed out that a `sync.Mutex`  **cannot be copied** (just like all the other primitives of `sync` package). If a structure has a `sync` field, **it must be passed by pointer**.

# sync.RWMutex

`sync.RWMutex` is a reader/writer mutex. It provides the same methods that we have just seen with `Lock()` and `Unlock()` (as both structures implement `sync.Locker` interface). Yet, it also allows concurrent reads using `RLock()` and `RUnlock()` methods:

|     |     |
| --- | --- |
| 1   | mutex  := &sync.RWMutex{} |
| 2   |     |
| 3   | mutex.Lock() |
| 4   | // Update shared variable |
| 5   | mutex.Unlock() |
| 6   |     |
| 7   | mutex.RLock() |
| 8   | // Read shared variable |
| 9   | mutex.RUnlock() |

 [view raw](https://gist.github.com/teivah/3d24a93ca0e04ec84156bf4e4019ee72/raw/f39e3f86d5980f89f1770c4ea8922ffff50d8085/rwmutex.go)  [rwmutex.go](https://gist.github.com/teivah/3d24a93ca0e04ec84156bf4e4019ee72#file-rwmutex-go) hosted with ❤ by [GitHub](https://github.com/)

A `sync.RWMutex` allows either **at least one reader** or **exactly one writer** whereas a `sync.Mutex` allows exactly one reader or writer.

Let’s run a quick benchmark to compare these methods:

|     |     |
| --- | --- |
| 1   | func  BenchmarkMutexLock(b *testing.B) { |
| 2   | m  := sync.Mutex{} |
| 3   | for  i  :=  0; i < b.N; i++ { |
| 4   | m.Lock() |
| 5   | m.Unlock() |
| 6   | }   |
| 7   | }   |
| 8   | func  BenchmarkRWMutexLock(b *testing.B) { |
| 9   | m  := sync.RWMutex{} |
| 10  | for  i  :=  0; i < b.N; i++ { |
| 11  | m.Lock() |
| 12  | m.Unlock() |
| 13  | }   |
| 14  | }   |
| 15  |     |
| 16  | func  BenchmarkRWMutexRLock(b *testing.B) { |
| 17  | m  := sync.RWMutex{} |
| 18  | for  i  :=  0; i < b.N; i++ { |
| 19  | m.RLock() |
| 20  | m.RUnlock() |
| 21  | }   |
| 22  | }   |

 [view raw](https://gist.github.com/teivah/a0ace25954f2fead474eaf1779b340d7/raw/d2948da0400ecc3a57a22774fbc69c2d7df8db9c/mutex.go)  [mutex.go](https://gist.github.com/teivah/a0ace25954f2fead474eaf1779b340d7#file-mutex-go) hosted with ❤ by [GitHub](https://github.com/)

BenchmarkMutexLock-4 83497579 17.7 ns/op
BenchmarkRWMutexLock-4 35286374 44.3 ns/op
BenchmarkRWMutexRLock-4 89403342 15.3 ns/op

As we can notice, read locking/unlocking a `sync.RWMutex` is faster than locking/unlocking a `sync.Mutex`. On the other end, calling `Lock()`/`Unlock()` on a `sync.RWMutex` is the slowest operation.

In conclusion, a `sync.RWMutex` should rather be used when we have **frequent reads and infrequent writes**.

# sync.WaitGroup

`sync.WaitGroup` tends also to be used quite frequently. It’s the idiomatic way for a goroutine to wait for the **completion of a collection of goroutines**.

`sync.WaitGroup` holds an internal counter. If this counter is equal to 0, the `Wait()` method returns immediately. Otherwise, it is blocked until the counter is 0.

To increment the counter we have to use `Add(int)`. To decrement it we can either use `Done()` (that will decrement by 1) or the same `Add(int)` method with a negative value.

In the following example, we will spin up eight goroutines and wait for their completion:

|     |     |
| --- | --- |
| 1   | wg  := &sync.WaitGroup{} |
| 2   |     |
| 3   | for  i  :=  0; i < 8; i++ { |
| 4   | wg.Add(1) |
| 5   |  go  func() { |
| 6   |  // Do something |
| 7   | wg.Done() |
| 8   | }() |
| 9   | }   |
| 10  |     |
| 11  | wg.Wait() |
| 12  | // Continue execution |

 [view raw](https://gist.github.com/teivah/b28b7ae5e86db291bcd4f1787624bd20/raw/d5e4730d1080cd7c18ad135f3f7155bac02b7a1b/waitgroup.go)  [waitgroup.go](https://gist.github.com/teivah/b28b7ae5e86db291bcd4f1787624bd20#file-waitgroup-go) hosted with ❤ by [GitHub](https://github.com/)

Each time we create a goroutine, we increment the `wg`‘s internal counter with `wg.Add(1)`. We could have also called `wg.Add(8)` outside of the for-loop.

Meanwhile, every time a goroutine completes, it decreases the `wg`‘s internal counter using `wg.Done()`.

The main goroutine continues its execution once the eight `wg.Done()` statements have been executed.

# sync.Map

`sync.Map` is a concurrent version of Go `map` where we can:

- Add elements with `Store(interface{}, interface{})`
- Retrieve elements with `Load(interface) interface{}`
- Remove elements with `Delete(interface{})`
- Retrieve or add an element if it did not exist before with `LoadOrStore(interface{}, interface{}) (interface, bool)`. The returned bool is true if the key was present in the map before.
- Iterate on the elements with `Range`

|     |     |
| --- | --- |
| 1   | m  := &sync.Map{} |
| 2   |     |
| 3   | // Put elements |
| 4   | m.Store(1, "one") |
| 5   | m.Store(2, "two") |
| 6   |     |
| 7   | // Get element 1 |
| 8   | value, contains  := m.Load(1) |
| 9   | if contains { |
| 10  | fmt.Printf("%s\n", value.(string)) |
| 11  | }   |
| 12  |     |
| 13  | // Returns the existing value if present, otherwise stores it |
| 14  | value, loaded  := m.LoadOrStore(3, "three") |
| 15  | if !loaded { |
| 16  | fmt.Printf("%s\n", value.(string)) |
| 17  | }   |
| 18  |     |
| 19  | // Delete element 3 |
| 20  | m.Delete(3) |
| 21  |     |
| 22  | // Iterate over all the elements |
| 23  | m.Range(func(key, value interface{}) bool { |
| 24  | fmt.Printf("%d: %s\n", key.(int), value.(string)) |
| 25  |  return  true |
| 26  | })  |

 [view raw](https://gist.github.com/teivah/a79042e92151a5e6eadfd83783c4db8a/raw/63d4058c86ad88b649623b988a1068e178ef5fef/map.go)  [map.go](https://gist.github.com/teivah/a79042e92151a5e6eadfd83783c4db8a#file-map-go) hosted with ❤ by [GitHub](https://github.com/)

Go Playground: https://play.golang.org/p/BO8IDVIDwsr
one
three
1: one
2: two

As you can see, the `Range` method takes a `func(key, value interface{}) bool` function. If we return false, the iteration is stopped. Interesting fact, the worst-case time-complexity remains O(n) even if we return false after a constant time ([more info](https://github.com/golang/go/blob/87805c92fd57d1535d0e497dd245ef783007b59d/src/sync/map.go#L313-L316)).

When shall we use `sync.Map` instead of a `sync.Mutex` on top of a classic `map`?

- When we have **frequent reads and infrequent writes** (in the same vein to `sync.RWMutex`)
- When *multiple goroutines read, write, and overwrite entries for disjoint sets of keys*. What does it mean concretely? For example, if we have a sharding implementation with a set of 4 goroutines and each goroutine in charge of 25% of the keys (**without collision**). In this case, `sync.Map` is also the preferred choice.

# sync.Pool

`sync.Pool` is a concurrent pool, in charge to hold safely a **set of objects**.

The public methods are:

- `Get() interface{}` to retrieve an element
- `Put(interface{})` to add an element

|     |     |
| --- | --- |
| 1   | pool  := &sync.Pool{} |
| 2   |     |
| 3   | pool.Put(NewConnection(1)) |
| 4   | pool.Put(NewConnection(2)) |
| 5   | pool.Put(NewConnection(3)) |
| 6   |     |
| 7   | connection  := pool.Get().(*Connection) |
| 8   | fmt.Printf("%d\n", connection.id) |
| 9   | connection = pool.Get().(*Connection) |
| 10  | fmt.Printf("%d\n", connection.id) |
| 11  | connection = pool.Get().(*Connection) |
| 12  | fmt.Printf("%d\n", connection.id) |

 [view raw](https://gist.github.com/teivah/4103791cedefb546aa6368de6ff8c2f6/raw/9c261d0143229e1477d9b308a66c3b7be0f8d0c8/pool.go)  [pool.go](https://gist.github.com/teivah/4103791cedefb546aa6368de6ff8c2f6#file-pool-go) hosted with ❤ by [GitHub](https://github.com/)

1
3
2

It worth noting that there is no guarantee in terms of ordering. The `Get` method specifies that it takes an **arbitrary** item from the pool.

It is also possible to specify a creator method:

|     |     |
| --- | --- |
| 1   | pool  := &sync.Pool{ |
| 2   |  New: func() interface{} { |
| 3   |  return  NewConnection() |
| 4   | },  |
| 5   | }   |
| 6   |     |
| 7   | connection  := pool.Get().(*Connection) |

 [view raw](https://gist.github.com/teivah/dcd1c79bcea7de5bea5a01db923515b9/raw/c3811862ba61581d385fec9590dbc1b2acc11b9c/pool.go)  [pool.go](https://gist.github.com/teivah/dcd1c79bcea7de5bea5a01db923515b9#file-pool-go) hosted with ❤ by [GitHub](https://github.com/)

Every time `Get()` is called, it will return an object (in this case a pointer) created by the function passed in `pool.New`.

When shall we use `sync.Pool`? There are two use-cases:

The first one is when we have to reuse **shared and long-live objects** like a DB connection for example.

The second one is to **optimize memory allocation**.

Let’s consider the example of a function that writes into a buffer and persists the result to a file. With `sync.Pool`, we can reuse the space allocated for the buffer by reusing the same object across the different function calls.

The first step is to retrieve the buffer previously allocated (or to create one if it’s the first call but this is abstracted). Then, the deferred action is to put the buffer back in the pool.

|     |     |
| --- | --- |
| 1   | func  writeFile(pool *sync.Pool, filename  string) error { |
| 2   | // Gets a buffer object |
| 3   | buf  := pool.Get().(*bytes.Buffer) |
| 4   | // Returns the buffer into the pool |
| 5   | defer pool.Put(buf) |
| 6   |     |
| 7   | // Reset buffer otherwise it will contain "foo" during the first call |
| 8   | // Then "foofoo" etc. |
| 9   | buf.Reset() |
| 10  |     |
| 11  | buf.WriteString("foo") |
| 12  |     |
| 13  | return ioutil.WriteFile(filename, buf.Bytes(), 0644) |
| 14  | }   |

 [view raw](https://gist.github.com/teivah/84519671f516a9acd20cdb7fb53e2de0/raw/a64ff6d271fc979828434729d909ebc7a78af25b/pool.go)  [pool.go](https://gist.github.com/teivah/84519671f516a9acd20cdb7fb53e2de0#file-pool-go) hosted with ❤ by [GitHub](https://github.com/)

Last point to mention with `sync.Pool`. Since a pointer can be put into the interface value returned by `Get()`  **without** any allocation, it is preferable to put pointers than structures in the pool.

This way, we can efficiently reuse the allocated memory as well as relieving the garbage collector if the variable was escaped to the heap.

# sync.Once

`sync.Once` is a simple and powerful primitive to guarantee that a function is **executed only once**.

In this example, there will be only one goroutine displaying the output message:

|     |     |
| --- | --- |
| 1   | once  := &sync.Once{} |
| 2   | for  i  :=  0; i < 4; i++ { |
| 3   | i  := i |
| 4   | go  func() { |
| 5   | once.Do(func() { |
| 6   | fmt.Printf("first %d\n", i) |
| 7   | })  |
| 8   | }() |
| 9   | }   |

 [view raw](https://gist.github.com/teivah/0d762d460da607df08ad9b54249f3d32/raw/b167490a60fb5248b543f5c8f06e851310cd4359/once.go)  [once.go](https://gist.github.com/teivah/0d762d460da607df08ad9b54249f3d32#file-once-go) hosted with ❤ by [GitHub](https://github.com/)

We have used the `Do(func())` method to specify the part that must be called only once.

# sync.Cond

Let’s finish by the primitive which is, most likely, the less frequently used: `sync.Cond`.

It is used to emit a signal (one-to-one) or broadcast a signal (one-to-many) to goroutine(s).

Let’s consider a scenario where we have to indicate to one goroutine that the first element of a shared slice has been updated.

Creating a `sync.Cond` requires a `sync.Locker` object (either a `sync.Mutex` or a `sync.RWMutex`):

|     |     |
| --- | --- |
| 1   | cond  := sync.NewCond(&sync.RWMutex{}) |

 [view raw](https://gist.github.com/teivah/22d70b47a6bac8e66aff515c9f80705d/raw/04b8055e6cf9037654626b9743dbe5451ff54969/cond.go)  [cond.go](https://gist.github.com/teivah/22d70b47a6bac8e66aff515c9f80705d#file-cond-go) hosted with ❤ by [GitHub](https://github.com/)

Then, let’s write the function in charge to display the first element of the slice:

|     |     |
| --- | --- |
| 1   | func  printFirstElement(s []int, cond *sync.Cond) { |
| 2   | cond.L.Lock() |
| 3   | cond.Wait() |
| 4   | fmt.Printf("%d\n", s[0]) |
| 5   | cond.L.Unlock() |
| 6   | }   |

 [view raw](https://gist.github.com/teivah/d677d8cbe1b00e0082b72d87111e0811/raw/b7e2339a0242958b9d6b7602e3636bca56dc86af/cond.go)  [cond.go](https://gist.github.com/teivah/d677d8cbe1b00e0082b72d87111e0811#file-cond-go) hosted with ❤ by [GitHub](https://github.com/)

As you can see, we can access the internal mutex using `cond.L`. Once the lock is acquired, we call `cond.Wait()` that is going to block as long as we don’t receive any signal.

Let’s get back to the main goroutine. We’ll create a pool of `printFirstElement` by passing a shared slice and the `sync.Cond` previously created. Then, we call a `get()` function, store the result in `s[0]` and emit a signal:

|     |     |
| --- | --- |
| 1   | s  :=  make([]int, 1) |
| 2   | for  i  :=  0; i < runtime.NumCPU(); i++ { |
| 3   | go  printFirstElement(s, cond) |
| 4   | }   |
| 5   |     |
| 6   | i  :=  get() |
| 7   | cond.L.Lock() |
| 8   | s[0] = i |
| 9   | cond.Signal() |
| 10  | cond.L.Unlock() |

 [view raw](https://gist.github.com/teivah/38d6e87f201ae8b805822149274b0f71/raw/c096ea787aafaa4694f4634d27c46fd8f561d6b4/cond.go)  [cond.go](https://gist.github.com/teivah/38d6e87f201ae8b805822149274b0f71#file-cond-go) hosted with ❤ by [GitHub](https://github.com/)

This signal will unblock one of the goroutine created that will display `s[0]`.

Nevertheless, if we take a step back we could argue that our code might break one of the most fundamental principles of Go:

> Do not communicate by sharing memory; instead, share memory by communicating.

Indeed, in this example, it would have been better to use a channel to communicate the value returned by `get()`.

Yet, we also mentioned that `sync.Cond` can also be used to **broadcast a signal**.

Let’s just modify the end of the previous example by calling `Broadcast()` instead of `Signal()`:

|     |     |
| --- | --- |
| 1   | i  :=  get() |
| 2   | cond.L.Lock() |
| 3   | s[0] = i |
| 4   | cond.Broadcast() |
| 5   | cond.L.Unlock() |

 [view raw](https://gist.github.com/teivah/f78f1f9a4ca75e144c418955143ff001/raw/e2d99b7eeeda6cedf1334a58aea4342a4a8ae731/cond.go)  [cond.go](https://gist.github.com/teivah/f78f1f9a4ca75e144c418955143ff001#file-cond-go) hosted with ❤ by [GitHub](https://github.com/)

In this scenario, **all of the goroutines** are going to be triggered.

As we know, channel elements are caught by only one goroutine. The only way to *simulate* a broadcast is to close a channel but this cannot be repeated. Thus, this is undeniably an interesting feature, despite being [quite controversial](https://github.com/golang/go/issues/21165).

**Update 27/11:**

There is another use case that is worth mentioning with `sync.Cond`, if not the most important one:

Go Playground of the example: https://play.golang.org/p/ap5qXF5DAg5