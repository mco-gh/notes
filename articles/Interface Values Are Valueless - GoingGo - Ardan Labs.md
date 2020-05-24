Interface Values Are Valueless - GoingGo - Ardan Labs

# Interface Values Are Valueless

Categories :Tags :  , [go](https://www.ardanlabs.com/blog/tags/go.html) ,

### Introduction

I’ve been seeing a lot of question about interfaces lately on Slack. Most of the time the answers are technical and focus on implementation details. Implementation is important to help with debugging, but implementation doesn’t help with design. When it comes to designing code with interfaces, behavior has to be the main focus.

In this post, I hope to provide a different way to think about interfaces and how to design code with them. I want you to stop focusing on the implementation details and focus on the relationship interfaces have with concrete data.

### Data Oriented Design

I believe in [Data Oriented Design](https://www.youtube.com/watch?v=rX0ItVEVjHc) over Object Oriented Design when it comes to writing code in Go. My first law of DOD is:

***If you don’t understand the data you are working with, you don’t understand the problem you are trying to solve.***

Every problem you solve is a data transformation problem. There is some input and you produce some output. This is what programs do. Every function you write is a smaller data transformation that helps solve the larger transformation.

Since the problems you solve are data transformation problems, the algorithms you write are based on concrete data. Concrete data is the physical state that you store in memory, send over a network, write to a file and essentially manipulate. [Mechanical sympathy](https://mechanical-sympathy.blogspot.com/) is based on concrete data and how effectively you allow the machine to perform these transformations.

A big caveat to DOD is dealing with change. My second law of DOD is:

***When the data is changing, your problem is changing. When the problem is changing, then the algorithms you wrote need to change.***

The algorithms you have need to change when the data is changing. This is the best way to maintain readability and performance. Unfortunately, too many of us have been taught to create multiple layers of abstraction and to generalize things to deal with change. I think this approach has [more cost](https://www.ardanlabs.com/blog/2018/02/focus-on-being-precise.html) than benefits when it comes to designing for change.

What you need is a way to allow your algorithms to remain small and precise for each data transformation that needs to be performed. You need a way to change those algorithms when the data is changing, without causing change to cascade throughout a large portion of the code base. This is where interfaces come in. When you focus on interfaces, you want to focus on behavior.

### Concrete Data

Since everything is about concrete data, you need to start here. Start with this concrete type.

**Listing 1**

	05 type file struct {
	06     name string
	07 }

The named type `file` declared on line 05 in listing 1 defines a type of concrete data thanks to the use of the keyword `struct`. With this concrete type declared, you can create a value of this type.

**Listing 2**

	13 func main() {
	14     var f file

Thanks to the variable declaration on line 14 in listing 2, you now have a value of type `file` stored in memory and referenceable through the variable `f`. This data referenced by the variable `f` is real and can be manipulated.

You can define a second piece of concrete data using the keyword `struct` again.

**Listing 3**

	09 type pipe struct {
	10     name string
	11 }

The named type `pipe` declared on line 09 in listing 3 also represents a concrete piece of data. Once again, with this type declaration you can create a different concrete value inside the program.

**Listing 4**

	01 package main
	02
	03 import "fmt"
	04
	05 type file struct {
	06     name string
	07 }
	08
	09 type pipe struct {
	10     name string
	11 }
	12
	13 func main() {
	14     var f file
	15     var p pipe
	16
	17     fmt.Println(f, p)
	18 }

Now this program has two distinct pieces of concrete data defined and a single value of each type has been created. On line 14 a value of type `file` is created and a value of type `pipe` is created on line 15. To complete the program, each value is displayed using the `fmt` package on line 17.

### Interfaces Are Valueless

You have been using the keyword `struct` to define the concrete data your program needs. There is another keyword you can use to define a type. That is the keyword `interface`.

**Listing 5**

	05 type reader interface {
	06     read(b []byte) (int, error)
	07 }

On line 05 in listing 5 an `interface` type has been declared. An `interface` type is the opposite of a `struct` type. An `interface` type can only declare a method set of behavior. This means there is nothing concrete about an `interface` type.

**Listing 6**

	var r reader

What is really interesting is that you can declare a variable of the `interface` type, which is what’s happening in listing 6. This is interesting because, if there is nothing concrete about an `interface` type, that means the variable `r` is valueless. An `interface` type defines and creates values that are valueless!

***Boom! Head Explodes.***
This is a critical concept to have and keep in your head. You must understand:

- There is nothing real about the variable `r`.
- There is nothing concrete about the variable `r`.
- The variable `r` is valueless.

There is an implementation detail that makes `r` real behind the scenes, but from our programming model, that does not exist.

When you recognize `interface` values are valueless, a whole world of possibility and understanding emerge.

**Listing 7**

	37 func retrieve(r reader) error {
	38     data := make([]byte, 100)
	39
	40     len, err := r.read(data)
	41     if err != nil {
	42         return err
	43     }
	44
	45     fmt.Println(string(data[:len]))
	46     return nil
	47 }

The function `retrieve` defined in listing 7 is what I call a polymorphic function. Before I continue, a definition of polymorphism is in order. This definition from the inventor of the programming language Basic, Tom Kurtz, gives you an incredible insight into what makes this polymorphic function so special.

***“Polymorphism means that you write a certain program and it behaves differently depending on the data that it operates on.”***

Everytime I read this quote I get chills. It’s brilliant in its simplicity and it drives an important point home. Polymorphism is driven from concrete data. Concrete data that has the ability to change the behavior of code. As I stated earlier, the problems you are solving are rooted in concrete data. Data Oriented Design is about the concrete.

***If you don’t understand the [concrete] data you are working with, you don’t understand the problem you are trying to solve.***

Tom’s quote is making it clear that the concrete data is the driver that allows for the abstraction of different behavior (polymorphism) to be designed and implemented. Brilliant stuff.

Go back to the code in Listing 7. I will repeat it again below.
**Listing 7 - Duplicated**

	37 func retrieve(r reader) error {
	38     data := make([]byte, 100)
	39
	40     len, err := r.read(data)
	41     if err != nil {
	42         return err
	43     }
	44
	45     fmt.Println(string(data[:len]))
	46     return nil
	47 }

When you look at the function declaration for `retrieve` on line 37, the function seems to say, pass me a value of type `reader`. But you know that’s impossible because there is no such thing as a value of type `reader`. Values of type `reader` do not exists because `reader` is an `interface` type. You know `interface` values are valueless.

Then what is the function declaration saying? It’s saying the following:

***I will accept any piece of concrete data (any value or pointer) that implements the `reader` contract. That implements the full method set of behavior defined by the `reader` interface.***

This is how you achieve polymorphism in Go. The `retrieve` function is not bound to a single piece of concrete data, but bound to any concrete data that exhibits the `read` behavior.

### Giving Data Behavior

The next question is, how can data exhibit behavior? This is where methods come in. Methods are the mechanism to give data behavior. Once a piece of data has behavior, then polymorphism can be realized.

***“Polymorphism means that you write a certain program and it behaves differently depending on the data that it operates on.”***

In Go, you have the ability to write functions and methods. One reason to choose a method over a function is when a piece of data needs behavior to satisfy the method set of a given `interface`.

**Listing 8**

	05 type reader interface {
	06     read(b []byte) (int, error)
	07 }
	08
	09 type file struct {
	10     name string
	11 }
	12
	13 func (file) read(b []byte) (int, error) {
	14     s := "<rss><channel><title>Going Go</title></channel></rss>"
	15     copy(b, s)
	16     return len(s), nil
	17 }
	18
	19 type pipe struct {
	20     name string
	21 }
	22
	23 func (pipe) read(b []byte) (int, error) {
	24     s := `{name: "bill", title: "developer"}`
	25     copy(b, s)
	26     return len(s), nil
	27 }

*Note: You might have noticed the receivers for the methods on line 13 and 23 have been declared without a variable name. This is a common practice when the method does not need to access anything from the receiver value.*

In listing 8, a method is declared on line 13 for the `file` type and line 23 for the `pipe` type. Each type now defines an act of behavior named `read` that matches the full method set of behavior defined by the `reader` interface. Because of these method declarations, the following can now be said.

***“The concrete type file and pipe now implement the reader interface using value receivers.”***

Every word I have said in that quote matters. If you have been reading my previous blog posts about value and pointer semantics, you know the behavior data can exhibit is defined by the semantic you are using. I won’t be going into all of that again in this post. But here is a link.

https://www.ardanlabs.com/blog/2017/06/design-philosophy-on-data-and-semantics.html

Once these methods are declared using value receivers, values and pointers of these concrete types can be passed into the polymorphic function `retrieve`.

**Listing 9**

	01 package main
	02
	03 import "fmt"
	04
	05 type reader interface {
	06     read(b []byte) (int, error)
	07 }
	08
	09 type file struct {
	10     name string
	11 }
	12
	13 func (file) read(b []byte) (int, error) {
	14     s := "<rss><channel><title>Going Go</title></channel></rss>"
	15     copy(b, s)
	16     return len(s), nil
	17 }
	18
	19 type pipe struct {
	20     name string
	21 }
	22
	23 func (pipe) read(b []byte) (int, error) {
	24     s := `{name: "bill", title: "developer"}`
	25     copy(b, s)
	26     return len(s), nil
	27 }
	28
	29 func main() {
	30     f := file{"data.json"}
	31     p := pipe{"cfg_service"}
	32
	33     retrieve(f)
	34     retrieve(p)
	35 }
	36
	37 func retrieve(r reader) error {
	38     data := make([]byte, 100)
	39
	40     len, err := r.read(data)
	41     if err != nil {
	42         return err
	43     }
	44
	45     fmt.Println(string(data[:len]))
	46     return nil
	47 }

Listing 9 provides a complete polymorphic example in Go and shows how `interface` values are valueless. The `retrieve` function can accept any piece of concrete data, any value or pointer, that implements the `reader` interface. That’s exactly what you see happening in the function calls on lines 33 and 34.

Now you have the highest level of decoupling you can achieve in Go and this decoupling is precise. You know exactly the behavior any piece of concrete data must exhibit to be passed into the function. This is not generalized or hidden when reading the code.

It all makes sense when you accept that `interface` values are valueless. This function is not asking for a `reader` value because they don’t exist. The function is asking for concrete data that exhibits the correct behaviors.

### Interface Value Assignments

This idea that `interface` values are valueless extend into `interface` value assignments. Take these `interface` types.

**Listing 10**

	05 type Reader interface {
	06     Read()
	07 }
	08
	09 type Writer interface {
	10     Write()
	11 }
	12
	13 type ReadWriter interface {
	14     Reader
	15     Writer
	16 }

With these interfaces declared, you can implement a concrete type that implements all three interfaces.

**Listing 11**

	18 type system struct{
	19     Host string
	20 }
	21
	22 func (*system) Read()  { /* ... */ }
	23 func (*system) Write() { /* ... */ }

Now you can see once again how `interface` values are valueless.
**Listing 12**

	25 func main() {
	26     var rw ReadWriter = &system{"127.0.0.1"}
	27     var r Reader = rw
	28     fmt.Println(rw, r)
	29 }

	// OUTPUT
	&{127.0.0.1} &{127.0.0.1}

In listing 12 on line 26, a variable named `rw` of the interface type `ReadWriter` is declared and assigned a piece of concrete data. The concrete data being a pointer to a `system` value. Then on line 27, a variable named `r` of the interface type `Reader` is declared. There is an assignment associated with this declaration. The `rw` variable of the interface type `ReadWriter` is being assigned to the newly declared variable `r` of interface type `Reader`.

This should cause pause for a second because the variable `rw` is not of the same named type as `r`. We know that you don’t get implicit type conversion in Go between two differently named types. But this is different. These variables are not based on concrete types but interface types.

If we go back to the understanding that interfaces declare valueless types, then `rw` and `r` are not real. Therefore, code can’t be assigning the `interface` values to each other. It’s assigning the only thing it can assign, the concrete data stored inside the `interface` values. Thanks to the type declarations for the interfaces, the compiler can validate if the concrete data inside of one interface also satisfies the other.

In the end, we can only work with concrete data. When working with interface values, we are still only working with the concrete data stored inside of them. When you pass the `interface` value to the `fmt` package for display, notice the concrete data is what is displayed. Again, it is the only thing that is real.

### Conclusion

I hope this post has provided a different way to think about interfaces and how to design code with them. I believe that once you get out of the implementation details and focus on the relationship interfaces have with concrete data, things become easier to reason about. Data Oriented Design is an important aspect to writing better algorithms but decoupling comes from the focus on behavior. Interfaces allow for decoupling through the use of behavior concrete data can exhibit.