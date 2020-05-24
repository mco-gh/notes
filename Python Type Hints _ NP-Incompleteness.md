Python Type Hints | NP-Incompleteness

# Python Type Hints

Posted on [December 26, 2019](https://kunigami.blog/2019/12/26/python-type-hints/) by [kunigami](https://kunigami.blog/author/kunigami/)

Jukka Lehtosalo is a Finnish Software Engineer at Dropbox. He developed an optional type system for Python, mypy, during his PhD thesis in Cambridge. After meeting in a Python conference, Guido van Rossum (creator of Python) invited Lehtosalo to join him at Dropbox. They started adopting mypy in real use cases during a Hackathon, which led to mypy being one of the most popular Python type checkers [2].

In this post we’ll cover mypy in general terms as well many examples demonstrating the syntax and capabilities of this type checker.

## Introduction

**mypy** is a static type checker. This means it does not run during the code execution, so it’s mostly useful during development, much like tests. It relies on manual annotations in the code called type hints, which identify the types of arguments, return types, internal variables and member variables.

One simple example of such annotations is for a function to compute the length of a string:

|     |     |
| --- | --- |
| 1   | def  str_len(s: str) -> int: |
| 2   |  return  len(s) |

 [view raw](https://gist.github.com/kunigami/fd18f0d44a57bf62102086e5753aaa4e/raw/e6d3c812d6a10d784696af33f6ec47f53d3c3d05/strlen.py)  [strlen.py](https://gist.github.com/kunigami/fd18f0d44a57bf62102086e5753aaa4e#file-strlen-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

We are indicating that the input argument s is a string and it return an integer corresponding to its length. The main job of a type checker is to find inconsistencies in the annotations in our code (or in the libraries we use). For example, here’s an incorrect type annotation:

|     |     |
| --- | --- |
| 1   | def  invalid_inc(n: int) -> str: |
| 2   |  return n +  1 |

 [view raw](https://gist.github.com/kunigami/23b791d105bbcabf18dc3c947129a97d/raw/62771bf7338c01563b6084b99c71477fff8e8137/invalid_inc.py)  [invalid_inc.py](https://gist.github.com/kunigami/23b791d105bbcabf18dc3c947129a97d#file-invalid_inc-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

When both operands are integers, the operator + returns another integer, so n + 1 is an integer, which is a clear contradiction given we provided the return type as string.

### Type annotations are free unit tests

This contrived example doesn’t make the usefulness of a type checker obvious, but imagine a case where we implicitly make assumption on the argument type. For example, a small program to compute how much an exchange house would give a user for their cash.

|     |     |
| --- | --- |
| 1   | def  convert_currency(a): |
| 2   |  return  2*a |
| 3   |     |
| 4   |     |
| 5   | user_input =  '$10' |
| 6   | fee =  10 |
| 7   | value = convert_currency(user_input) - fee |

 [view raw](https://gist.github.com/kunigami/d31607cc4a97642f029d4ac12c13470b/raw/fe4d13fe4a0ae196696535b4b35b00c5a5b6b4b5/buggy.py)  [buggy.py](https://gist.github.com/kunigami/d31607cc4a97642f029d4ac12c13470b#file-buggy-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

If we don’t perform input validation correctly, the code above might work for the tested scenarios but would fail in production the moment the user provided a string. Of course good QA will cover scenarios like these, but this is to sort of guarantees one gets for free by making the types explicit:

|     |     |
| --- | --- |
| 1   | def  convert_currency(a: float) -> float: |
| 2   |  return  2*a |

 [view raw](https://gist.github.com/kunigami/85bd7248d6159b7f5e4464ead88303ec/raw/abb3d69202ca747b7c3eba770d6eff79d2b70568/convert_currency.py)  [convert_currency.py](https://gist.github.com/kunigami/85bd7248d6159b7f5e4464ead88303ec#file-convert_currency-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

The previous code would now fail the type checker validation.

### Type hints are optional and incremental

Most of the design of type annotations are well documented in [PEP 484](https://www.python.org/dev/peps/pep-0484/), the document claims:

> 

> Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention.

**

This also seems to imply that Python type hints will always be partial / gradual, since if full typing is required, it will make transition from non-typed to fully typed codebases prohibitive. Also, there are concrete benefits even with partial typing.

A partial type system makes it optional to add type annotations to variables, instead of it being fully mandatory (like Java or C++). The type checker then performs validation with whatever information it has in hands.

Incomplete typing can be dangerous if developers build trust on the type checker while it’s only performing partial checks due to incomplete information. Let’s consider an example:

|     |     |
| --- | --- |
| 1   | def  expects_string(a: str): |
| 2   |  return a |
| 3   |     |
| 4   | def  expects_int(a: int) -> int: |
| 5   |  return a +  1 |
| 6   |     |
| 7   | def  main(): |
| 8   | untyped = expects_string('a') |
| 9   | expects_int(untyped) |

 [view raw](https://gist.github.com/kunigami/f82b20f5cac5a7b86f8140e0ffa4312c/raw/f0c41d5f37b044a45605673433122e98f17bea42/incorrect.py)  [incorrect.py](https://gist.github.com/kunigami/f82b20f5cac5a7b86f8140e0ffa4312c#file-incorrect-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

At first glance it seems a well typed program and if we run the type checker it will pass. But if we run `main()`, we’ll have a runtime error. The problem is that `expect_string` is missing the return type, so in `main()`, the type checker cannot infer the type of `untyped`, so it doesn’t perform any validation on `expects_int()`.

### Local inference

The previous example also highlights an important aspect of the mypy type checker: it only performs inferences at the function boundary. In theory it should infer that `expects_string` returns `str` because we’re returning its argument and then infer that `untyped` is a string.

This is fine in this example but it could be very expensive to make these inferences, especially if we need to consider branching and recursive calls to other functions. In theory the type checker could go only a few levels deep in the function call but this would make the behavior of the type checker very hard to reason about.

For that reason, the type check will only consider the type of the functions being called. For example, it knows `expects_string()` expects a string and returns no type, so this is what it will assign to `untyped` no matter what happens inside `expects_string()`.

Now that we know the basics of the type checker, let’s cover some of the syntax and more advanced typing that mypy supports.

## Examples

### Setup

Before we start, it’s useful to be able to test the snippets. To do so, copy the code into a file, say `example.py` and run this command in the terminal:

`mypy example.py`

which will print any type errors that exist in `example.py`. mypy can be installed via Python packaging system, pip. Make sure to user Python 3:

`pip3 install mypy`

### Primitive types

`bool`, `int`, `str`, `float` are the types one will most likely use in functions. As seen above, we can use these to type arguments and return types:

|     |     |
| --- | --- |
| 1   | def  str_len(s: str) -> int: |
| 2   |  return  len(s) |

 [view raw](https://gist.github.com/kunigami/fd18f0d44a57bf62102086e5753aaa4e/raw/e6d3c812d6a10d784696af33f6ec47f53d3c3d05/strlen.py)  [strlen.py](https://gist.github.com/kunigami/fd18f0d44a57bf62102086e5753aaa4e#file-strlen-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Composed types

We’ll look into generics later, but it should be straightforward to understand the typing of composed types like lists, dictionaries and tuples:

|     |     |
| --- | --- |
| 1   | from typing import List, Dict, Tuple |
| 2   |     |
| 3   | def  list() -> List[int]: |
| 4   |  return [1, 2, 3] |
| 5   |     |
| 6   | def  dict() -> Dict[str, int]: |
| 7   |  return {'a': 1, 'b': 2} |
| 8   |     |
| 9   | def  tuple() -> Tuple[int, str]: |
| 10  |  return (1, 'a') |

 [view raw](https://gist.github.com/kunigami/feb92c80c29028ec03fb68f542b9b4c6/raw/53777b064850a81f92591137f63df236f54368ce/compost.py)  [compost.py](https://gist.github.com/kunigami/feb92c80c29028ec03fb68f542b9b4c6#file-compost-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

It’s worth noting that these types need to be explicitly imported from the typing module.

### None vs. NoReturn

`None` is used to indicate that no return value is to be expected from a function.

|     |     |
| --- | --- |
| 1   | def  my_print(s: str) -> None: |
| 2   |  print('>'  + s) |
| 3   |     |
| 4   | # error: "my_print" does not return a value |
| 5   | r = my_print('a') |

 [view raw](https://gist.github.com/kunigami/645a6cf5d34330e3b7f3298c6a02cc9a/raw/5722f12a96b8c970a9ab5c2e0ebae78449eaf2db/none.py)  [none.py](https://gist.github.com/kunigami/645a6cf5d34330e3b7f3298c6a02cc9a#file-none-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

`NoReturn` is to indicate the function should not return via the normal flow:

|     |     |
| --- | --- |
| 1   | def  ready(s: str) -> NoReturn: |
| 2   |  print('implemented') |
| 3   |  # error: implicit return |
| 4   |     |
| 5   | def  not_ready(s: str) -> NoReturn: |
| 6   |  print('not implemented') |
| 7   |  raise  # ok: always throws |

 [view raw](https://gist.github.com/kunigami/80855c99181bd43daa14f11803e5c08d/raw/fa8c2e521d1888f38f04580a7b7e0c8d4981649e/no_return.py)  [no_return.py](https://gist.github.com/kunigami/80855c99181bd43daa14f11803e5c08d#file-no_return-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Local Variables

The example below demonstrates the syntax for typing local variables. In general typing local variables is not necessary since their type can often be inferred from the assignment / initialization.

|     |     |
| --- | --- |
| 1   | b: bool  =  False |
| 2   | i: int  =  1 |
| 3   | s: str  =  'abc' |
| 4   | f: float  =  1.0 |

 [view raw](https://gist.github.com/kunigami/34598bc9cf858d49cd16cae19a74efb5/raw/a3d5ee485313d4a5c58448195632bc6095f5ebd2/primitive.py)  [primitive.py](https://gist.github.com/kunigami/34598bc9cf858d49cd16cae19a74efb5#file-primitive-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Optional and Union

`Optional[T]` is a generic type that indicates the type is either `T` or `None`. For example:

|     |     |
| --- | --- |
| 1   | def  first(xs: List[int]) -> Optional[int]: |
| 2   |  if  len(xs) ==  0: |
| 3   |  return  None |
| 4   |  return xs[0] |

 [view raw](https://gist.github.com/kunigami/f35e4ab4e4c0db3f68a1f8e338ab6973/raw/b66e0bb6713853e67611e37511f004f52bbe58ed/first.py)  [first.py](https://gist.github.com/kunigami/f35e4ab4e4c0db3f68a1f8e338ab6973#file-first-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

`Optional` is a special case of a more general concept of `Union` of types:

|     |     |
| --- | --- |
| 1   | def int_or_str() -> Union[str, int]: |
| 2   |  if(random.randint(0, 1) ==  0): |
| 3   |  return  1 |
| 4   |  return  'a' |

 [view raw](https://gist.github.com/kunigami/f178fc595717ed6d211691ecefee6b0e/raw/614a091759b8d7a60493247b16d0a03519b8a1b1/int_or_str.js)  [int_or_str.js](https://gist.github.com/kunigami/f178fc595717ed6d211691ecefee6b0e#file-int_or_str-js) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

My personal take is that `Union` should be avoided (except for special cases like `Optional`) because it makes the code harder to deal with (having to handle multiple types) and it’s often better via inheritance (base type representing the union).

### Any vs. object

`Any` is equivalent to not providing the type annotation. On the other hand, `object` is the base of all types, so it would be more like a `Union` of all the types. A variable of type object can be assigned a value of any type, but the value of an object variable can only be assigned to other object variables. It’s possible to refine the type of a variable to a more specific one. See *“Refining types”*.

|     |     |
| --- | --- |
| 1   | def  dummy(x: object) -> object: |
| 2   |  return x |
| 3   |     |
| 4   | def  inc(x: int) -> int: |
| 5   |  return x +  1 |
| 6   |     |
| 7   | foo(Square()) # ok |
| 8   | inc(foo(1)) # error - foo(1) returns object |

 [view raw](https://gist.github.com/kunigami/91cb65de62cef78b5a3e465019bd5579/raw/8b7568e7375568ff29d79e51a1d800f77df22f7c/object.py)  [object.py](https://gist.github.com/kunigami/91cb65de62cef78b5a3e465019bd5579#file-object-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Classes

There are three main things we need to consider when annotating variables in a class context:

- We can add types to the member variable (`_n` in this case).
- We don’t type `self`: it’s assumed to be the type of the class where it’s defined.
- The return type of `__init__` is `None`

|     |     |
| --- | --- |
| 1   | class  C: |
| 2   |     |
| 3   | _n: int |
| 4   |     |
| 5   |  def  __init__(self, n: int) -> None: |
| 6   |  self._n = n |
| 7   |     |
| 8   |  def  inc(self) -> None: |
| 9   |  self._n +=  1 |

 [view raw](https://gist.github.com/kunigami/fdfeea52c58dcd2510107d39221f4fa9/raw/e51a88624560b20f32ef4692268bafbab122ea4b/class.py)  [class.py](https://gist.github.com/kunigami/fdfeea52c58dcd2510107d39221f4fa9#file-class-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Callables

`Callables` can be used to type higher order functions. Here’s an example where we pass a function (lambda) as argument to a map function:

|     |     |
| --- | --- |
| 1   | def  typed_map(xs: List[int], f: Callable[[int], int]) -> List[int]: |
| 2   |  return [f(x) for x in xs] |
| 3   |     |
| 4   | print(typed_map([1, 2, 3], lambda  x: x*2)) |

 [view raw](https://gist.github.com/kunigami/0d301370f348fdb76cdb4fc2675e7b08/raw/7b5ac5c18a5b305b1a22e5ae2a45e9c702f68f08/callable.py)  [callable.py](https://gist.github.com/kunigami/0d301370f348fdb76cdb4fc2675e7b08#file-callable-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

The type of the function is `Callable`. The first element, `[int]` in the example above, is a list of the types of the arguments. The second argument is the return type.

As another example, if we want to define a reduce function on strings, our callback has now type `Callable[[str, str], str]` because it takes 2 arguments.

|     |     |
| --- | --- |
| 1   | def  typed_reduce(xs: List[str], f: Callable[[str, str], str], x0: str) -> str: |
| 2   | r = x0 |
| 3   |  for x in xs: |
| 4   | r = f(r, x) |
| 5   |  return r |
| 6   |     |
| 7   | print(typed_reduce(['a', 'b', 'c'], lambda  x, y: x + y, '')) |

 [view raw](https://gist.github.com/kunigami/7994d403827935cb065959b3accb121a/raw/1fa5ea8ece7988f211cc624265ec2611bef54b0b/typed_reduce.py)  [typed_reduce.py](https://gist.github.com/kunigami/7994d403827935cb065959b3accb121a#file-typed_reduce-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Generics: Type Variables

Type variables allow us to add constraints to the types of one or more argument and/or return types so that they share the same type. For example, the function below is typed such that if we pass `List[int]` as argument, it will return `Optional[int]`:

|     |     |
| --- | --- |
| 1   | T = TypeVar('T') |
| 2   |     |
| 3   |     |
| 4   | def  first(xs: List[T]) -> Optional[T]: |
| 5   |  if (len(xs) ==  0): |
| 6   |  return  None |
| 7   |  return xs[0] |

 [view raw](https://gist.github.com/kunigami/fde4b9553dcff1dc9927a403b2d9fd55/raw/8f44d9fb3fd26fd0641c53bf16dbdca73d49763d/type_var.py)  [type_var.py](https://gist.github.com/kunigami/fde4b9553dcff1dc9927a403b2d9fd55#file-type_var-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

Note that the string passed to the `TypeVar()` function must match the of the variable it is assigned to. This is an inelegant syntax but I’m imagining it’s the result of working around syntax limitations of Python (and the difficulties in changing the core Python syntax for annotations).

We can use multiple `TypeVar`s in a function:

|     |     |
| --- | --- |
| 1   | T1 = TypeVar('T1') |
| 2   | T2 = TypeVar('T2') |
| 3   |     |
| 4   | def  tuplify(a: T1, b: T2) -> Tuple[T1, T2]: |
| 5   |  return (a, b) |

 [view raw](https://gist.github.com/kunigami/321574a0dcbf5102c05629b2b3fb47df/raw/4cd2607289248c6af91115e9651fd1ef033bb9dc/tuplify.py)  [tuplify.py](https://gist.github.com/kunigami/321574a0dcbf5102c05629b2b3fb47df#file-tuplify-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

**Constraints.** According to [3] it’s also possible to limit the type var to be of a specific types:

> 

> TypeVar supports constraining parametric types to a fixed set of possible types (note: those types cannot be parametrized by type variables).

**
It also notes:
> 

> There should be at least two constraints, if any; specifying a single constraint is disallowed.

**

Which makes sense, if we were to restrict a `TypeVar` to a single type we might as well use that type directly.

In the example below we allow `Tmix` to be bound to either `int` or `str`. Note this is different from `Union[int, str]` because the latter is **both**  `int` and `str` at the same time, while the former is either `int` or `str`, depending on how it’s called. The third call to `fmix()` below would be valid for a `Union`.

|     |     |
| --- | --- |
| 1   | Tmix = TypeVar('Tmix', int, str) |
| 2   |     |
| 3   | def  fmix(a: Tmix, b: Tmix) -> Tmix: |
| 4   |  if(random.randint(0, 1) ==  0): |
| 5   |  return a |
| 6   |  return b |
| 7   |     |
| 8   | fmix('a', 'b') # ok |
| 9   | fmix(1, 2) # ok |
| 10  | fmix('a', 1) # error |

 [view raw](https://gist.github.com/kunigami/998372d338937e2fee9649d89385a0d6/raw/961fbbbf071dacd93f630a9b9d397b2b30b71a55/fmix.py)  [fmix.py](https://gist.github.com/kunigami/998372d338937e2fee9649d89385a0d6#file-fmix-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Parametrized Classes

We’ve just seen how to parametrize functions via `TypeVar`. We can also extend such functionality to classes via the `Generic` base class:

|     |     |
| --- | --- |
| 1   | class  Parametrized(Generic[T]): |
| 2   | value: T |
| 3   |     |
| 4   |  def  __init__(self, value: T) -> None: |
| 5   |  self.value = value |
| 6   |     |
| 7   |  def  getValue(self) -> T: |
| 8   |  return  self.value |

 [view raw](https://gist.github.com/kunigami/f29d41a27eac17932a7b12be1865e358/raw/f37b3f97b587965b887d579fef10a048f2f0b413/parametrized_class.py)  [parametrized_class.py](https://gist.github.com/kunigami/f29d41a27eac17932a7b12be1865e358#file-parametrized_class-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

### Ignoring type hints

During the transition from untyped to typed code, it might be necessary to temporarily turn off type checking in specific parts of the code. For example, imagine a scenario where types were added to a widely used function but many existing callers are passing incorrect types.

The comment `# type: ignore` makes the type checker skip the current line (if an inline comment) or the next line (if a line comment). Here’s an obvious type violation that is ignored by the type checker:

|     |     |
| --- | --- |
| 1   | pseudo_int: int  =  'a'  # type:  ignore |

 [view raw](https://gist.github.com/kunigami/f2eaa5e0659de5ea5c4bbd7c0913d19e/raw/334825fea306696267b63712adeb17cc69c969d9/pseudo_int.py)  [pseudo_int.py](https://gist.github.com/kunigami/f2eaa5e0659de5ea5c4bbd7c0913d19e#file-pseudo_int-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

It’s also possible to turn off type-checking completely for the file:
> 

> A # type: ignore comment on a line by itself at the top of a file, before any docstrings, imports, or other executable code, silences all errors in the file

**

### Refining types: isinstance() and cast()

In some cases we might receive values from untyped code or ambiguous types like Unions or object. Two ways of informing the type checker about the specific type is by explicit check via `isinstance()` or `cast()`. The `isinstance()` will be usually in a if clause:

|     |     |
| --- | --- |
| 1   | def  inc(x: int) -> int: |
| 2   |  return x +  1 |
| 3   |     |
| 4   | def  delegate(x: object) -> object: |
| 5   |  if (isinstance(x, int)): |
| 6   |  return inc(x) |

 [view raw](https://gist.github.com/kunigami/dd81b38c3e7f8190b5a8c3d00f41f575/raw/8e784016c202f74f972f4ecc40257e35c2c6b739/isinstance.py)  [isinstance.py](https://gist.github.com/kunigami/dd81b38c3e7f8190b5a8c3d00f41f575#file-isinstance-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

This allows the type checker to infer the type of x within the `x` block, so it won’t complain about the call of `inc(x)`.

|     |     |
| --- | --- |
| 1   | def  inc(x: int) -> int: |
| 2   |  return x +  1 |
| 3   |     |
| 4   | def  enforce(x: object) -> int: |
| 5   |  return inc(cast(int, x)) |

 [view raw](https://gist.github.com/kunigami/5cdc96b59a4c9ff07130e5fb542facdb/raw/2aa1be4d64d65dfd14ac5b138e71eaa02673e240/cast.py)  [cast.py](https://gist.github.com/kunigami/5cdc96b59a4c9ff07130e5fb542facdb#file-cast-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

Another, more drastic, approach is to use `cast([type], x)` which returns `x` if it has in runtime but otherwise throws an exception, but this allows the type checker to refine the type of x to statically. Here’s an example:

|     |     |
| --- | --- |
| 1   | def  inc(x: int) -> int: |
| 2   |  return x +  1 |
| 3   |     |
| 4   | def  enforce(x: object) -> int: |
| 5   |  return inc(cast(int, x)) |

 [view raw](https://gist.github.com/kunigami/5cdc96b59a4c9ff07130e5fb542facdb/raw/2aa1be4d64d65dfd14ac5b138e71eaa02673e240/cast.py)  [cast.py](https://gist.github.com/kunigami/5cdc96b59a4c9ff07130e5fb542facdb#file-cast-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

It’s a bummer that the order of arguments of `cast([type], var)` and `isisntance(var, [type])` are inconsistent.

### Arbitrary argument lists

It’s possible to type arbitrary argument lists, both the positional and named ones. In the example below, `args` has type `Tuple[str, ...]` and `kwds` has type `Dict[str, int]`. Note that the `...` in `Tuple[str, ...]` indicates an arbitrary-length tuple of strings. It’s unclear to me why it’s a tuple and not a list, but I’d guess it has to do with how it represents non-arbitrary argument lists (e.g. `foo(x: int, y: str)` would be `Tuple[int, str]`).

|     |     |
| --- | --- |
| 1   | def  foo(*args: str, **kwds: int): |
| 2   |  pass |

 [view raw](https://gist.github.com/kunigami/4363c84c01d5f049271aa48317793ca5/raw/8b1c39fb914b026c41d099437b9d6634257b9510/arg_list.py)  [arg_list.py](https://gist.github.com/kunigami/4363c84c01d5f049271aa48317793ca5#file-arg_list-py) hosted with ![2764.png](../_resources/fb7d6f34be3341f972471bea44d5e256.png) by [GitHub](https://github.com/)

## Conclusion

I really like Python and it’s my go-to language for small examples and automation scripts. However, having had to work with a large code base before, I was really displeased by its lack of types.

I’m also a big proponent of typed code, especially for large, multi-person code bases, but I understand the appeal of rapid development for prototypes and Python now offers both.

As we saw in some examples, the syntax is cumbersome at times but overall I find the mpyp type checker pretty expressive.

## References

[[1](http://mypy-lang.org/about.html)] mypy: About

[[2](https://blog.dropbox.com/topics/company/thank-you--guido)] Dropbox Blog: Thank you, Guido

[[3](https://www.python.org/dev/peps/pep-0484)] PEP 484 — Type Hints

ADVERTISING

Advertisements

Report this ad
Advertisements

Report this ad

### Share this:

- [Twitter](https://kunigami.blog/2019/12/26/python-type-hints/?share=twitter&nb=1)
- [Facebook](https://kunigami.blog/2019/12/26/python-type-hints/?share=facebook&nb=1)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)

- [![74231318b03600599b999e675a5c31b4](../_resources/228761f4be072afe1730dc650f881d72.png)](https://en.gravatar.com/joskid)

One blogger likes this.

### *Related*

[Revisiting Python: Basic Types](https://kunigami.blog/2015/02/20/revisiting-python-basic-types/)In "python"

[Revisiting Python: Object Oriented Programming](https://kunigami.blog/2015/03/07/revisiting-python-object-oriented-programming/)In "python"

[Revisiting Python: Functions](https://kunigami.blog/2015/02/22/revisiting-python-functions/)In "python"

This entry was posted in [Uncategorized](https://kunigami.blog/category/uncategorized/). Bookmark the [permalink](https://kunigami.blog/2019/12/26/python-type-hints/).

.