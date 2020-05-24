Things I Wish Someone Had Told Me About Golang

[home](http://openmymind.net/)

# Things I Wish Someone Had Told Me About Golang

11 Mar 2013

### "Pointers"

Somehow I got it in my mind that Go had first-class support for pointers. Certainly, if you're coming from a language like Java or Ruby, pointers in Go have greater visibility. But, without pointer arithmetics or, despite many claims, pass-by-reference, Go's "pointers" feel like a more flexible form of Java/Ruby/Python/Node/....

Consider the following code which prints "Leto" twice:
type User struct {
Name string}func  main() {
u :=  &User{Name: "Leto"} println(u.Name) Modify(u) println(u.Name)
}func  Modify(u *User) {
u =  &User{Name: "Paul"}
}

(Since everyone has missed the point here, let me clarify. I'm saying that in a language that does pass by reference, the above *would* print Paul. I realize this isn't the norm, but it also isn't uncommon (C#). I had been under the impression that Go had taken this uncommon approach.)

This is what wikipedia calls *call by sharing*. The main difference I can see that Go offers is the ability to *Call by Value*, which can be used to ensure immutability. This slightly modified example (note that we're now passing a copy of the value, rather than a copy of the pointer) will also print "Leto" twice:

type User struct {
Name string}func  main() {
u := User{Name: "Leto"} println(u.Name) Modify(u) println(u.Name)
}func  Modify(u User) {
u.Name =  "Duncan"}
**update**
As has been pointed out, the above is possible in Go by doing:
func  main() {
u :=  &User{Name: "Leto"}
fmt.Println(u.Name) Modify(&u)
fmt.Println(u.Name)
}func  Modify(u **User) { *u =  &User{Name: "Bob"}
}

This is still not pass-by-reference. But, since you are able to dereference, you can achieve the same thing.

### The GoWay or The Highway

I imagine a lot of newcomers are going to try to bend Go into their own vision of a properly organized system. The sooner you forget virtualenv, node_package or rubies, the quicker you can be productive. Set your $GOROOT and $GOPATH and create the [recommended src/pkg/bin folders](http://golang.org/doc/code.html) under $GOPATH. Feels weird? Use symlinks to make it all transparent with how you probably organize the rest of your code.

It doesn't stop at high level organization. It might feel wrong at first, but tests side-by-side with code will make your life easier. First, you get access to package-visible members. Second, you avoid any ugly circular dependencies.

Also, my first reaction about Go was that its organizational structure wouldn't work well for large project. The solution is simple: adopt small, cohesive packages (just like Go's own libraries). One or two files per package is quite common. One way to monitor this is to track how many `NewXYZ` factories you have. Aiming for one, like `lazycache.New()` is much better than having multiple like `core.NewLazyCache()` and `core.NewProxy()`.

### Tip Or Don't Bother

Go 1.0.3 is roughly 6 months old. There's a bunch of bug fixes and performance enhancements in tip. Maybe I'm jaded because our first Go system used the immature image libraries, but if there's actually a reason I think you shouldn't use Go, it's this. At this early stage, making critical fixes and enhancements available in a stable package should be given greater priority. On the flip side, we are using tip successfully.

### Interface Pointers

Maybe it's just me, but it took me a while to understand this method from Go's net/http package:

func  ServeHTTP(res http.ResponseWriter, req *http.Request) {
...
}

Why is `req` passed as a reference, but `res` passed as a value? Why, I wondered, are they making me pay the performance penalty of passing a copy of an object?! That's not what's happening though. `http.ResponseWriter` is an interface and either a value-type or a reference-type can satisfy an interface. So, technically, you don't know whether the value being passed is a copy of a pointer or a copy of a value, but it's probably the former.

Given an interface:
type CacheItem interface { GetId() string}
Both an `Application` value and a `User` reference satisfy the interface:
type Application struct {
id string}func (a Application) GetId() string { return a.id
}type User struct {
name string}func (u *User) GetId() string { return u.name
}
And thus, both can be treated as a `CacheItem`:
func  main() { Store(&User{name: "Leto"}) Store(Application{id: "9001"})
}func  Store(item CacheItem) { *//do something with item.GetId()*}

So, as far as I know, you'll never see a pointer to an interface (i.e. `item *CacheItem`). I used to think the common Java pattern of a postfixing `Impl` or C#'s prefixing `I` was silly...now I'm not so sure.

### Implicit Interfaces Lead To Good Design

Interface's in Go are implicitly bound. The above `User` only had to implement the `GetId() string` function in order to implement `CacheItem`. It's a cool feature. And it isn't as superficial as you (or I) might think.

Go's interfaces tend to promote small and cohesive behavior. It's quite common to see interfaces with a single method. This is quite handy when dealing with Go library interfaces. Want to write to your own type from any `io.Reader`? Simply implement the `Write(p []byte) (n int, err error)` function and you can use `io.Copy`.

You should use this techniques for your own types and functions. Passing a focused interface to a function helps ensure that you aren't doing too much. It's one of the best tools I've seen that reduces the amount of refactoring you have to do.

[(L)](http://openmymind.net/Things-I-Wish-Someone-Had-Told-Me-About-Go/#)Window size:  x

Viewport size:  x