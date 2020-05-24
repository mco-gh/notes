What Go Programming Language does and does not have

# What Go Programming Language does and does not have

[![1*YqUau3DC0FHSzoErxDmvFA.jpeg](../_resources/d216b1fc455cad90c220f2832cde97a4.jpg)](https://medium.com/@amritpandey?source=post_header_lockup)

[Amrit Pandey](https://medium.com/@amritpandey)
May 18·9 min read

![](../_resources/2420cb6fbda2407c39febb6004e23757.png)![1*_wxwNuxszA6vwQIUMbF-fw.gif](../_resources/5d890f40b04b28c23b1b74723ea0acbb.gif)

Go get ‘em

> Go has the benefit of hindsight, and basics are well done: it has a garbage collection, a package system, first class functions, lexical scope, a system call interface and immutable strings in which text are generally encoded in UTF-8. But it has comparatively few features and is unlikely to add more. For instance, it has no implicit numeric conversions, no constructors or destructors, no operator overloading, no default parameter values, no inheritance, no generics, no exceptions, no macros, no function annotations and no thread-local storage.

This above passage is from the book “The Go Programming Language” by *Alan A. A. Donovan *and* Brian W. Kernighan. *We will now try to understand each term in brief. As a beginner in core programming, having knowledge of these terms are important. The meaning of all these concepts apply in every programming language. These terms can help you distinguish various languages on a fundamental level.

### ✅ Things that Go has

#### Garbage Collection

It is an entity in any programming language that does automatic memory management. To understand garbage collection or memory management, first you need to understand how memory works. While working with a programming language, compiler assign various memory location in the system to store data e.g. creating a variable, looping over an array etc. The allocation and de-allocation of memory needs to be done in order to make program more efficient with memory.

In language like C, memory management is done manually, if you are familiar with C you know there is a function called *malloc* that dynamically allocate memory in the system. In a high level language like JavaScript or Python, these allocation are done automatically by program known as Garbage Collector. As the name suggest, their job is to manage memory, assign locations when needed and delete memory allocations when not. Go has garbage collection, so programmer do not have to worry about managing memory and space.

#### Package System

Packaging of a software is bundling up of all the source code and assets into one entity called as package. A software package is handy in many ways like easy installation, sharing, contributing, debugging etc. Go has a built in package system that bundle up documentations, binaries and source code files. The purpose of packaging is to be able to use other software projects in your software without having to manually copy over the source code.

#### First-class Functions

A First class function is a function that can be treated like any other variable i.e. it can be assigned, returned, exported, passed as a parameter etc. Take a look at following snippet below written in Go. A function that prints a string `hello world first class function`*  *is assigned to a variable `a`. The variable `a` acts as an actual value in the memory however it can also be called as a function by appending `()` at the end of it. You can also see that value of variable `a` is printed just like any other variable. This is a basic concept of first class functions.

`package main[[NEWLINE]][[NEWLINE]]import (  [[NEWLINE]]    "fmt"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main() {  [[NEWLINE]]    a := func() {[[NEWLINE]]        fmt.Println("hello world first class function")[[NEWLINE]]    }[[NEWLINE]]    a()[[NEWLINE]]    fmt.Printf("%T", a)[[NEWLINE]]}`

#### Lexical Scope

Scope in a program is like a block or area over which the definition of any variable/function is defined. For example, a variable declared inside of a function only has its meaning inside that function block i.e. between the curly braces `{ *}*`*.* If you try to access the value of such variable outside this function block, program will not be able to find it. This is a basic way to understand Lexical Scope, it is more of a method of scoping than the scope itself.

package main
import “fmt”
func main() {
{
v := 1
{
fmt.Println(v)
}
fmt.Println(v)
}
fmt.Println(v)
// “undefined: v” compilation error

}

In the above snippet, there are four scopes. One: the universal scope, two: function `main()`, three: first block inside function main and four: scope where `fmt.Println` is called for the first time. Out of three `Println`, the last one gives a compilation error. This is because the definition of variable `v` is only available in scope three and four. When `Println` is called with the `v` passed in as a parameter, the program first look for its definition in the current scope, when it fails to find it, it moves outwards in parent’s scope and it will keep doing that until it finds the definition of it. This is what lexical scoping does, program start to look for definition of variables and functions from the scope in which they are used/called and move inside out. In the last `fmt.Println `program is not able to find definition of `v` in current or any parent scopes hence gives a compilation error.

#### System call interface

Go is provided with system call interface, which serves as the link to system calls made available by the operating system. For example, opening and reading a file, input and output etc. It intercepts function calls in the API and invokes the necessary system call within the operating system.

#### Immutable Strings

Although Go syntax have similarity and simplicity of C, it has an improvement over it with immutable strings that are encoded in UTF-8. So programs written in Go can also utilize forming strings in multiple languages and symbols. In primitive sense strings are combination/array/list of characters in programming languages. As the strings are formed by combining characters, their composition can be changed. Characters can be appended, removed, moved etc. It is a way by which when strings are declared their composition cannot be changed(mutated). The concept of immutable strings are not new, In Python String object instances cannot be mutated, JavaScript too have immutable strings and Ruby added [Frozen String Literals](https://www.pluralsight.com/blog/software-development/ruby-2-3--working-with-immutable-strings-) in 2.3. But still, a great many popular languages like C++, PHP, Perl etc. do not have immutable strings.

### ❌ Things that Go does not have

#### Implicit numeric conversion

In programming type conversion refers to changing of data type of an entity to another. An implicit conversion means that this change takes place automatically by interpreter or compiler. For example, assigning an int value to a variable that was previously assigned to a float value. Such conversion is not available in Go. When the type is not mentioned while declaring a variable, it is assigned a suitable type like int, float, string etc. based on the syntactical composition of the literal. In the example given below, Go will thrown an error because it find two different data types and cannot perform operation on them. This occurs as Go compiler does not implicitly converts `int` to `float64` .

a := 1.0 // same as float64(1.0)
b := 1 // same as int(1)
fmt.Printf("%f", a*b)
// invalid operation: a * b (mismatched types float64 and int)

#### Constructors and Destructors

A job of constructors is to head start and initialize an object, whereas destructor is to destroy the object after its life time and free up memory. Unlike other object oriented programming, Go does not have classes. Hence the concept of constructors and destructors does not exist.

#### Operator Overloading

Operator overloading is a way in which the operators can be used to perform operations as defined by users. Operators behave according to the arguments passed. For example in C++ `+` operator can be used for string concatenation as well as addition of two integers. The meaning of `+` can also be defined by the user and changed according to program needs. In JavaScript and operation like `'1' + 1` would result in a string output of `"11"` due to higher precedence of strings. Such definitions are not allowed in Go, operators work strictly and only perform operations on specific argument data types.

#### Default Parameter Values

Go does not allow default values in function prototypes or function overloading. The Go language specification is remarkably small, and is purposefully maintained that way to keep the parser simple. Unlike other languages where you could pass default/optional parameter values in function, in Go you can only check if value was passed. A different approach to default values in Go will be something like this.

`func Concat1(a string, b int) string {`

`  if a == "" {[[NEWLINE]]    a = "default-a"[[NEWLINE]]  }[[NEWLINE]]  if b == 0 {[[NEWLINE]]    b = 5[[NEWLINE]]  }[[NEWLINE]][[NEWLINE]]  return fmt.Sprintf("%s%d", a, b)[[NEWLINE]]}`

#### Inheritance

Since Go does not follow conventional class hierarchy of objected oriented programming, structures in Go are not inherited from one another. In general, inheritance is a procedure in OOP languages in which one class inherits properties and method of its parents’ class. Inheritance can go deep into multiple levels. In Go however, a structure can be composed simply by providing a pointer or embedding to the collaborating structures. An example composition in Go is given below. A replacement to classes can be interfaces in Go. Interfaces do exist in other languages, however Go’s interfaces are satisfied implicitly.

type TokenType uint16
type Token struct {
Type TokenType
Data string
}

type IntegerConstant struct {
Token *Token
Value uint64
}

#### Generic Programming

Generic programming is a form in which we include templates known as generics which actually are not true source code but it is compiled by the compiler to transform them into source code. Lets try to understand templates in a simple way. Think of templates in programming as a *form. *We create a form where the crucial details of a template are left blank and is to be filled later during compilation. Then when we need to create something out of that template we just specify the details, for example `type`.

`template<typename T>[[NEWLINE]]class MyContainer[[NEWLINE]]{[[NEWLINE]]    // Container that deals with an arbitrary type T[[NEWLINE]]};[[NEWLINE]][[NEWLINE]]void main() [[NEWLINE]]{[[NEWLINE]]    // Make MyContainer take just ints.[[NEWLINE]]    **MyContainer<int> intContainer;**[[NEWLINE]]}`

In above snippet written in C++. The `template` is not provided a type, but it is provided one when `MyContainer` is initialized. We can also specify other types like `float`, `double` etc. according to the needs. Generics like templates are useful during running algorithms over set of data having multiple data types.

#### Exceptions

An exception indicates a condition which is reasonable and application might want to catch. Through exceptions we can resolve conditions for which program might fail to run. A checked exception does not bring execution to a complete stop, it can be caught and dealt with. Go does not have exceptions, it only has errors as interfaces and built-in errors. A crucial distinction among errors from exceptions are that they indicate a serious problem and which needs to be dealt with immediately, hence programming in Go become stricter. Errors in Go needs to be checked explicitly as they occur.

#### Macros

Macros stand for *macro instructions. *It is a way of minimizing repetitive task in programming by defining a preset output to a given set of inputs. For example, if we want a square of a number in C we can just do `x * x` where `x` is the variable, but we can also define a macro that return square of a number every time we need it. Macros are not functions. Macros are not available in Go.

#define square(x) ((x) * (x))
int main() {
int four = square(2); // same as 2 * 2
return 0;
}

#### Function Annotations

Annotations are a way of associating metadata to function parameters. In Python annotations are syntactically supported and are totally optional. Lets take a small example to describe what annotation are in Python.

def foo(a: int, b: 'description', c: float) -> float: print(a+b+c)
foo(1, 3, 2) // prints 6.0
foo('Hello ', , 'World!') // prints Hello World!

In above code, the parameters `a`, `b` and `c` are all annotated with some metadata. `a` and `c` are annotated with `int` and `float` types whereas `b` is provided with a string description. `foo` will print specific output despite the type of arguments mentioned in annotations.

#### Thread-local Storage

Thread-local storage is a computer programming method that uses static or global memory local to a thread. It is a static area where data gets copied for each thread in a program. When multiple thread utilize same static data for same task, they can copy it from TLS rather than storing it on their own.

### Conclusion

The creation of Go was focused on simplicity and elegance. It is fast, small and have simple syntax. There are less concepts to wrap your head around unlike other OOP languages. The creators of Go have solved simplicity of a language by not adding multiplicative complexity to adjacent parts of language. Hence Go does not have any feature that makes parser slower and bigger. Simplicity is the key to a good software. Go is certainly an anti cautionary tale to the bloated design of languages like C++ .

**NOTE**: Code snippets in this article are copied from various articles on web.