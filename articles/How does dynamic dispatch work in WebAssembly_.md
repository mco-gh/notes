How does dynamic dispatch work in WebAssembly?

# How does dynamic dispatch work in WebAssembly?

  Apr 26, 2018

WebAssembly is a stack-based virtual machine and instruction set, designed such that implementations can be *fast* and *safe*. It is a portable target for the compilation of languages like C, C++, and Rust.

How does WebAssembly make control flow safe? Functions and executable code live in a different namespace from data. A WebAssembly `call` instruction has a static operand that specifies which function it is calling. WebAssembly implementations can emit native code without dynamic checks after validating these static operands. Furthermore, control flow is structured even within functions. Unlike most native instruction sets, like x86, there are no arbitrary, un-typed jumps.

But C, C++, and Rust all have some capability for dynamic dispatch: function pointers, virtual methods, and trait objects. On native targets like x86, all these forms compile down into a jump to a dynamic address. What do these forms compile down into when targeting WebAssembly?

## `call_indirect`

In addition to the `call` instruction, WebAssembly also has [a `call_indirect`instruction](https://webassembly.github.io/spec/core/exec/instructions.html#exec-call-indirect). The `call_indirect` instruction indexes into a table of functions to call a dynamically selected function.

The `call_indirect` instruction takes two static operands:

1.   The type of the function that will be called, e.g. `(i32, i32) -> nil`. This type is encoded as an index into the “Type” section of a `.wasm` binary, and is statically validated to be within bounds.

2.   The table of functions to index into. Again, this table is encoded as a statically validated index into the “Table” section of a `.wasm` binary.[0](http://fitzgeraldnick.com/2018/04/26/how-does-dynamic-dispatch-work-in-wasm.html#foot-0)

The index *into* the table of functions, selecting which function gets called, is provided dynamically via the stack. Any arguments to the function are passed via the stack as well. If the index is outside the table’s bounds, a trap is raised. If the function at that index has a different type from what is expected, a trap is raised. If these dynamic checks pass, then the function at the given index is invoked.

In pseudo-code, the `call_indirect` instruction’s semantics are approximately:

	call_indirect(const type_idx, const table_idx):
	    const expected_type = get_type(type_idx)
	    const table = get_table(table_idx)

	    let func_idx = pop()
	    if func_idx >= len(table):
	        raise trap

	    let func = table[func_idx]
	    if type(func) != expected_type:
	        raise trap

	    invoke func

Let’s reify this with an example Rust program that uses dynamic dispatch via trait objects, compiling it to both x86-64 and WebAssembly, and then inspecting the disassemblies.

## A Simple Trait Objects Example

To get dynamic dispatch in Rust, we must use [trait objects](https://doc.rust-lang.org/book/second-edition/ch17-02-trait-objects.html), which means we must begin by defining a trait:

	*// Some trait describing a generic class of behavior.*
	trait MyTrait {
	    fn my_trait_method(&self) -> u32;
	}

Next, we define a couple types that both implement that trait. We must define more than one, or else the optimizer will be sneaky and de-virtualize and inline everything, defeating the purpose of this exercise.

	*// The concrete `Uno` type implements `MyTrait`.*
	struct Uno(char);
	impl MyTrait for Uno {
	    fn my_trait_method(&self) -> u32 {
	        1
	    }
	}

	*// And the concrete `Dos` type also implements `MyTrait`.*
	struct Dos(char);
	impl MyTrait for Dos {
	    fn my_trait_method(&self) -> u32 {
	        2
	    }
	}

We define a function that takes a `&MyTrait` trait object and dynamically dispatches a call to the `my_trait_method` method. We cannot allow this function to be inlined, or else the all-too-helpful optimizer will rain on our parade again.

	#[inline(never)]
	fn dynamic_dispatch(thing: &MyTrait) {
	    thing.my_trait_method();
	}

Finally, to tie everything together, we construct an instance of `Uno` and of`Dos`, convert them into trait objects, and pass these trait objects to`dynamic_dispatch`. Since we will export this function from our shared library /`.wasm` binary, we mark it `extern` and annotate it as `#[no_mangle]`.

	#[no_mangle]
	pub extern fn tie_it_all_together() {
	    let uno = Uno('1');
	    let uno = &uno as &MyTrait;
	    dynamic_dispatch(uno);

	    let dos = Dos('2');
	    let dos = &dos as &MyTrait;
	    dynamic_dispatch(dos);
	}

## Comparing x86-64 and WebAssembly Disassembly

We can use this command to compile our example to native code (x86-64 for my machine), and view the disassembly:

	rustc -Og -C panic=abort -C lto=fat example.rs \
	    && objdump -M intel -d libexample.so

To do the same for WebAssembly, we provide an explicit target flag to `rustc`and switch out `objdump` for [`wasm-objdump`](https://github.com/WebAssembly/wabt):

	rustc -Og --target wasm32-unknown-unknown -C panic=abort -C lto=fat example.rs \
	    && wasm-objdump -xd example.wasm

Let’s dive in!

The code for `<Uno as MyTrait>::my_trait_method` and `<Dos as MyTrait>::my_trait_method`, which just return constant integers, are straightforward in both the native code and the WebAssembly.

Here is the x86-64 for `<Uno as MyTrait>::my_trait_method`:[1](http://fitzgeraldnick.com/2018/04/26/how-does-dynamic-dispatch-work-in-wasm.html#foot-1)

	<<example::Uno as example::MyTrait>::my_trait_method>:
	*;; Function prologue.*
	push   rbp
	mov    rbp,rsp

	*;; Move 1 into the return register.*
	mov    eax,0x1

	*;; Function epilogue.*
	pop    rbp
	ret

And here is the WebAssembly:

	<<example::Uno as example::MyTrait>::my_trait_method>:
	*;; Push 1 onto the stack.*
	i32.const 1

	*;; Return to the caller. The top of the stack is the return value.*
	end

The code for `<Dos as MyTrait>::my_trait_method` is identical except that it returns `2` instead of `1`.

Next, let’s look at the code for `tie_it_all_together`, which constructs two different trait objects and calls `dynamic_dispatch` with each of them.

Trait objects are represented as the pair of a pointer to the instance of the concrete type that implements the trait, and a pointer to the vtable for that instance’s type’s implementation of the trait. The x86-64 code breaks the trait object structure up into its component members when calling `dynamic_dispatch`, passing the pointer to the instance in the `rdi` register and the pointer to the vtable in the `rsi` register.[2](http://fitzgeraldnick.com/2018/04/26/how-does-dynamic-dispatch-work-in-wasm.html#foot-2)

	<tie_it_all_together>:
	*;; Function prologue, reserving two words of stack space for `uno` and `dos`.*
	push   rbp
	mov    rbp,rsp
	sub    rsp,0x10

	*;; Store the '1' character (0x31) in `uno`.*
	mov    DWORD PTR [rbp-0x4],0x31

	*;; Move a pointer to the `<Uno as MyTrait>` vtable into `rsi`.*
	lea    rsi,[rip+0x7a]

	*;; Move a pointer to `uno` into `rdi`.*
	lea    rdi,[rbp-0x4]

	*;; Call `dynamic_dispatch` with the `uno` trait object!*
	call   f60 <_example::dynamic_dispatch>

	*;; Store the '2' character (0x32) in `dos`.*
	mov    DWORD PTR [rbp-0x8],0x32

	*;; Move a pointer to the `<Dos as MyTrait>` vtable into `rsi`.*
	lea    rsi,[rip+0x83]

	*;; Move a pointer to `dos` into `rdi`.*
	lea    rdi,[rbp-0x8]

	*;; Call `dynamic_dispatch` with the `dos` trait object!*
	call   f60 <_example::dynamic_dispatch>

	*;; Function epilogue.*
	add    rsp,0x10
	pop    rbp
	ret

WebAssembly is a stack machine, rather than a register machine. To pass arguments to a function, we push them onto the WebAssembly stack rather than putting them in registers. A WebAssembly function may also have locals, which are sort of like registers, but have the restriction that they can’t be accessed across frames. They are like caller-save registers. If we need some stack frame’s member to be addressable, we need somewhere to put it. The Rust compiler emits instructions to maintain its own, *second* stack in linear memory, dedicated to addressable structures. This linear memory stack maintained by Rust should not be confused with the [WebAssembly stack](https://webassembly.github.io/spec/core/exec/runtime.html#stack). Rust’s linear memory stack is built on top of WebAssembly’s axioms, while the latter is a fundamental atom of WebAssembly’s semantics and execution model.

The `tie_it_all_together` function uses the linear memory stack to store the`uno` and `dos` variables in `tie_it_all_together`, because their addresses are taken to construct the trait objects:

	<tie_it_all_together>:
	*;; Function prologue. Global 0 contains the linear memory stack pointer. Because*
	*;; the stack grows down, subtracting 16 from it is reserving 16 bytes of space*
	*;; in the linear memory stack.*
	get_global 0
	i32.const 16
	i32.sub
	tee_local 0
	set_global 0
	*;; The wasm stack is now []*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Store the '1' character (49) into the first linear memory stack frame slot,*
	*;; which is `uno`.*
	get_local 0
	i32.const 49
	i32.store 2 8
	*;; The wasm stack is now []*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Push a pointer to `uno` onto the wasm stack.*
	get_local 0
	i32.const 8
	i32.add
	*;; The wasm stack is now [*mut uno]*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Push the pointer to the `<Uno as MyTrait>` vtable onto the wasm stack.*
	i32.const 1024
	*;; The wasm stack is now [*mut uno, *mut vtable]*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Call `dynamic_dispatch` with the `uno` trait object! This consumes both*
	*;; values on the wasm stack as its arguments.*
	call 4 <example::dynamic_dispatch>
	*;; The wasm stack is now []*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Store the '2' character (50) into the second linear memory stack frame slot,*
	*;; which is `dos`.*
	get_local 0
	i32.const 50
	i32.store 2 12
	*;; The wasm stack is now []*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Push the pointer to `dos` onto the wasm stack.*
	get_local 0
	i32.const 12
	i32.add
	*;; The wasm stack is now [*mut dos]*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Push the pointer to the `<Dos as MyTrait>` vtable onto the wasm stack.*
	i32.const 1040
	*;; The wasm stack is now [*mut dos, *mut vtable]*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Call `dynamic_dispatch` with the `dos` trait object!*
	call 4 <example::dynamic_dispatch>
	*;; The wasm stack is now []*
	*;; Locals:*
	*;;   0: linear memory stack pointer*

	*;; Function epilogue.*
	get_local 0
	i32.const 16
	i32.add
	set_global 0
	end

Finally, let’s examine the code for `dynamic_dispatch`, which takes the`&MyTrait` trait object argument and makes the dynamically dispatched call to the trait object’s `my_trait_method` function.

The x86-64 code indexes into the vtable with an offset of 24 (or three words) to get the appropriate `my_trait_method` function pointer and does a tail-call to it via a direct jump.

	<example::dynamic_dispatch>:
	*;; Function prologue.*
	push   rbp
	mov    rbp,rsp

	*;; Function epilogue, except we don't `ret` because we're doing a*
	*;; tail-call.*
	pop    rbp

	*;; Offset the vtable pointer by three words, load the function pointer at that*
	*;; location within the vtable, and jump to the function!*
	jmp    QWORD PTR [rsi+0x18]

Now let’s compare that to the WebAssembly. Here is the annotated WebAssembly code for the `dynamic_dispatch` function:

	*;; This function has the type (i32, i32) -> nil*
	<example::dynamic_dispatch>:
	*;; This gets the first parameter to the function, the pointer to the trait*
	*;; object's concrete instance, and pushes it onto the wasm stack.*
	get_local 0
	*;; The wasm stack is now [*mut instance]*

	*;; Push the second parameter, the pointer to the vtable, onto the wasm stack.*
	get_local 1
	*;; The wasm stack is now [*mut instance, *mut vtable]*

	*;; Pop the vtable pointer from the top of the stack, add 12 to it to offset for*
	*;; the vtable's `my_trait_method` member, load that location from memory, and*
	*;; push the result onto the stack.*
	i32.load 2 12
	*;; The wasm stack is now [*mut instance, index]*

	*;; Do an indirect call of type 1, which is (i32) -> i32, from function*
	*;; table 0. The `call_indirect` instruction directly consumes the index from the*
	*;; stack, and because the function type we're calling takes an argument, the*
	*;; instance pointer is popped off the stack as well. Because the function type*
	*;; has a return value, the return value will be pushed onto the stack when control*
	*;; returns to this function.*
	call_indirect 1 0
	*;; The wasm stack is now [return_value]*

	*;; Because the dynamic_dispatch function does not use the return value, it gets*
	*;; explicitly dropped.*
	drop
	*;; The wasm stack is now []*

	*;; Return!*
	end

It turns out that the WebAssembly and the x86-64 code to do dynamic dispatch are pretty similar:

- Just like the x86-64, the WebAssembly has also exploded the trait object into its component members.

- Just like the x86-64, the WebAssembly indexes into the vtable by three words (it uses an offset of 12, and a `wasm32` word is 4 bytes) to get the “function pointer” for the instance’s `my_trait_method` function.

But the similarities stop there.

The x86-64 code uses a single, familiar stack. The WebAssembly code has *two*stacks:

1. The WebAssembly stack directly manipulated by instructions, which is a fundamental part of WebAssembly’s semantics, and is maintained by the WebAssembly implementation.

2. A second stack for addressable Rust locals, which lives in the linear memory heap, and is maintained by function prologue and epilogue instructions emitted by the Rust compiler.

When WebAssembly does dynamic dispatch, it is rather different than what x86-64 does. There are essentially two different address spaces for data and functions, and the same 32 bit integers are used to index into both spaces, but this works because the instructions are typed and designed for static validation before execution begins. This multi-space design is forced by WebAssembly’s hard requirements for safety and portability. It is pretty neat that languages like C++ and Rust — despite being low-level and having historically targeted architectures with a single address space for both executable code and data — are still abstract enough that we can represent them with this alternative architecture that separates functions and data into distinct spaces!

Many thanks to [Alex Crichton](https://github.com/alexcrichton), [Jeena Lee](http://jeenalee.com/), and [Luke Wagner](https://blog.mozilla.org/luke/) for reading early drafts of this text!

* * *

0 Currently, there is only a single table of functions with heterogeneous types, so the only valid value for this operand is`0`. The WebAssembly engine’s embedder (e.g. a Web browser) can also expose APIs to mutate these tables, so it isn’t strictly true that the functions in a table are always present in the “Table” section of the `.wasm`binary. [↩](http://fitzgeraldnick.com/2018/04/26/how-does-dynamic-dispatch-work-in-wasm.html#back-foot-0)

1 It is a bit surprising that `rustc`/LLVM didn’t optimize this into `mov eax,0x1; ret`, and that it left some unnecessary prologue and epilogue instructions in there. As [Rothon pointed out](https://www.reddit.com/r/rust/comments/8f3jsw/how_do_trait_objects_work_in_webassembly/dy0u283/),`rustc` will currently [force-enable frame pointers when building with debug info](https://github.com/rust-lang/rust/issues/48785). [↩](http://fitzgeraldnick.com/2018/04/26/how-does-dynamic-dispatch-work-in-wasm.html#back-foot-1)

2 We can verify this pair-of-pointers representation is used by running `dwarfdump` to inspect the DWARF debugging information describing the physical layout of the trait object:

	...
	< 2><0x00000180>      DW_TAG_structure_type
	                        DW_AT_name                  &MyTrait
	                        DW_AT_byte_size             0x00000010
	                        DW_AT_alignment             0x00000008
	< 3><0x00000187>        DW_TAG_member
	                          DW_AT_name                  pointer
	                          DW_AT_type                  <GOFF=0x000002a9>
	                          DW_AT_alignment             0x00000008
	                          DW_AT_data_member_location  DW_OP_plus_uconst 0
	                          DW_AT_artificial            yes(1)
	< 3><0x00000199>        DW_TAG_member
	                          DW_AT_name                  vtable
	                          DW_AT_type                  <GOFF=0x000002ec>
	                          DW_AT_alignment             0x00000008
	                          DW_AT_data_member_location  DW_OP_plus_uconst 8
	                          DW_AT_artificial            yes(1)
	...

You can also use `dwarfdump` to double-check your reading of how parameters are passed to a given function. [↩](http://fitzgeraldnick.com/2018/04/26/how-does-dynamic-dispatch-work-in-wasm.html#back-foot-2)