wasmerio/go-ext-wasm

 [![logo.png](../_resources/7d2624a5024d530f76c5ae960ab44228.png)](https://wasmer.io/)

 [![68747470733a2f2f77697468737065637472756d2e6769746875622e696f2f62616467652f62616467652e737667](../_resources/ee2f5d690463eeeb7cf9b9c471aaea2a.png)](https://spectrum.chat/wasmer)  [![68747470733a2f2f676f646f632e6f72672f6769746875622e636f6d2f7761736d6572696f2f676f2d6578742d7761736d3f7374617475732e737667](../_resources/942b10558d95586a5618575f1c2b174e.png)](https://godoc.org/github.com/wasmerio/go-ext-wasm/wasmer)  [![68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f7761736d6572696f2f676f2d6578742d7761736d](../_resources/fe8274ba46a1f72ac58912c27757e5b8.png)](https://goreportcard.com/report/github.com/wasmerio/go-ext-wasm)  [![68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7761736d6572696f2f7761736d65722e737667](../_resources/c85751652fe3ebb6ca4d931bbb946094.png)](https://github.com/wasmerio/wasmer/blob/master/LICENSE)

Wasmer is a Go library for executing WebAssembly binaries.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='254'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1128' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#install)Install

To install the library, follow the classical:
$ CGO_ENABLED=1 go install github.com/wasmerio/go-ext-wasm/wasmer

The `CGO_ENABLED` part is very likely to be optional. `go install`will work on many macOS and Linux distributions. It will not work on Windows yet, we are working on it.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='255'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1132' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#documentation)Documentation

[The documentation can be read online on godoc.org](https://godoc.org/github.com/wasmerio/go-ext-wasm/wasmer). It contains function descriptions, short examples, long examples etc. Everything one need to start using Wasmer with Go!

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='256'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1134' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#examples)Examples

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='257'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1136' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#basic-example-exported-function)Basic example: Exported function

There is a toy program in `wasmer/test/testdata/examples/simple.rs`, written in Rust (or any other language that compiles to WebAssembly):

#[no_mangle]pub  extern  fn  sum(x: i32, y: i32) -> i32 {
x + y
}

After compilation to WebAssembly, the[`wasmer/test/testdata/examples/simple.wasm`](https://github.com/wasmerio/go-ext-wasm/blob/master/wasmer/test/testdata/examples/simple.wasm)binary file is generated. ([Download it](https://github.com/wasmerio/go-ext-wasm/raw/master/wasmer/test/testdata/examples/simple.wasm)).

Then, we can execute it in Go:

package mainimport ("fmt"wasm "github.com/wasmerio/go-ext-wasm/wasmer")func  main() {// Reads the WebAssembly module as bytes.bytes, _  := wasm.ReadBytes("simple.wasm")// Instantiates the WebAssembly module.instance, _  := wasm.NewInstance(bytes)defer instance.Close()// Gets the `sum` exported function from the WebAssembly instance.sum  := instance.Exports["sum"]// Calls that exported function with Go standard values. The WebAssembly// types are inferred and values are casted automatically.result, _  :=  sum(5, 37)

fmt.Println(result) // 42!}

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='258'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1143' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#imported-function)Imported function

A WebAssembly module can export functions, this is how to run a WebAssembly function, like we did in the previous example with`instance.Exports["sum"](1, 2)`. Nonetheless, a WebAssembly module can depend on “extern functions”, then called imported functions. For instance, let's consider the basic following Rust program:

extern { fn  sum(x: i32, y: i32) -> i32;
}

#[no_mangle]pub  extern  fn  add1(x: i32, y: i32) -> i32 { unsafe { sum(x, y) +  1 }

}

In this case, the `add1` function is a WebAssembly exported function, whilst the `sum` function is a WebAssembly imported function (the WebAssembly instance needs to *import* it to complete the program). Good news: We can write the implementation of the `sum`function directly in Go!

First, we need to declare the `sum` function signature in C inside a Go comment (with the help of [cgo](https://golang.org/cmd/cgo/)):

package main// #include <stdlib.h>//// extern int32_t sum(void *context, int32_t x, int32_t y);import  "C"

Second, we declare the `sum` function implementation in Go. Notice the`//export` which is the way cgo uses to map Go code to C code.

//export sumfunc  sum(context  unsafe.Pointer, x  int32, y  int32) int32 {return x + y

}
Third, we use `NewImports` to create the WebAssembly imports. In this code:

- `"sum"` is the imported function name,
- `sum` is the Go function pointer, and
- `C.sum` is the cgo function pointer.

imports, _  := wasm.NewImports().Append("sum", sum, C.sum)
Finally, we use `NewInstanceWithImports` to inject the imports:

bytes, _  := wasm.ReadBytes("imported_function.wasm")instance, _  := wasm.NewInstanceWithImports(bytes, imports)defer instance.Close()// Gets and calls the `add1` exported function from the WebAssembly instance.results, _  := instance.Exports["add1"](1, 2)

fmt.Println(result)// add1(1, 2)// = sum(1 + 2) + 1// = 1 + 2 + 1// = 4// QED

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='259'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1161' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#read-the-memory)Read the memory

A WebAssembly instance has a linear memory. Let's see how to read it. Consider the following Rust program:

#[no_mangle]pub  extern  fn  return_hello() -> *const  u8 { b"Hello, World!\0".as_ptr()

}

The `return_hello` function returns a pointer to a string. This string is stored in the WebAssembly memory. Let's read it.

bytes, _  := wasm.ReadBytes("memory.wasm")instance, _  := wasm.NewInstance(bytes)defer instance.Close()// Calls the `return_hello` exported function.// This function returns a pointer to a string.result, _  := instance.Exports["return_hello"]()// Gets the pointer value as an integer.pointer  := result.ToI32()// Reads the memory.memory  := instance.Memory.Data()

fmt.Println(string(memory[pointer : pointer+13])) // Hello, World!

In this example, we already know the string length, and we use a slice to read a portion of the memory directly. Notice that the string terminates by a null byte, which means we could iterate over the memory starting from `pointer` until a null byte is met; that's a similar approach.

For a more complete example, see the [Greet Example](https://godoc.org/github.com/wasmerio/go-ext-wasm/wasmer#example-package--Greet).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='260'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1169' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#development)Development

The Go library is written in Go and Rust.
To build both parts, run the following commands:
$ just rust
$ just go
To build the Go part, run:
(Yes, you need [`just`](https://github.com/casey/just/)).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='261'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1175' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#testing)Testing

Once the library is build, run the following command:
$ just test

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='262'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1178' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#benchmarks)Benchmarks

We quickly compared Wasmer to [Wagon](https://github.com/go-interpreter/wagon) and [Life](https://github.com/perlin-network/life). The benchmarks are in `benchmarks/`. We run [the n-body algorithm](https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/nbody.html#nbody)with N=100000. Here are the results:

| Runtime | Time (ms) | Ratio (smaller is better) |
| --- | --- | --- |
| Wasmer | 42.06ms | 1   |
| Wagon | 1812.15ms | 43.1 |
| Life | 2136.46ms | 50.8 |

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='263'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1199' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#what-is-webassembly)What is WebAssembly?

Quoting [the WebAssembly site](https://webassembly.org/):

> WebAssembly (abbreviated Wasm) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable target for compilation of high-level languages like C/C++/Rust, enabling deployment on the web for client and server applications.

About speed:

> WebAssembly aims to execute at native speed by taking advantage of> [> common hardware capabilities](https://webassembly.org/docs/portability/#assumptions-for-efficient-execution)> available on a wide range of platforms.

About safety:

> WebAssembly describes a memory-safe, sandboxed > [> execution environment](https://webassembly.org/docs/semantics/#linear-memory)>  […].

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='264'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/wasmerio/go-ext-wasm/#license)License

The entire project is under the MIT License. Please read [the`LICENSE` file](https://github.com/wasmerio/wasmer/blob/master/LICENSE).