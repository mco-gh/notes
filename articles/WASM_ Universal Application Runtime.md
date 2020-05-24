WASM: Universal Application Runtime

# WASM: universal application runtime

Last summer, fresh off my last freelance gig, I was catching up with my friend [Asim](https://twitter.com/chuhnk), the founder of the widely popular [microservices](https://en.wikipedia.org/wiki/Microservices) company, [Micro](https://micro.mu/) at one of our [favourite coffee shops in London](https://goo.gl/maps/nJBVFbDYgvQqPnPM8). We would end up meeting almost every week talking about the presence and the future of technology. But that day our conversation turned into something that we had not talked about for a long time: [Web assembly](https://webassembly.org/) (WASM).

> WebAssembly (abbreviated WASM) is a binary instruction format for a stack-based virtual machine. WASM is designed as a portable target for compilation of high-level languages like C/C++/Rust, enabling deployment on the web for client and server applications.

When we met that afternoon none of us had any real life hands-on experience with it, but both of us felt that there was something fundamentally important about it. Of course we weren’t the first ones to think that. WASM “train” had started picking up the speed a while back. What we agreed on, though, was the idea of WASM being the future universal application runtime.

By “universal runtime” we meant cross-language i.e. any application written in any language would end up being compiled into WASM and run in some WASM runtime environment. We couldn’t quite define what the “runtime environment” was going to be at the time, but I suspected that we would have several of them: from specialised ones for particular workloads (machine learning models or GPU intensive tasks) to the more generic ones that would run more generic workloads (such as simple HTTP services).

WASM started as an effort to make web faster (by making better use of modern HW etc.) and safer (type safety is a real thing!), so naturally the first WASM runtime turned out to be the internet browser itself. But both Asim and I felt, that’s not where the things would stop. Just like JavaScript didn’t stop in the browser and ended up crawling everywhere, we suspected so would WASM.

After spending a bit of time learning a bit more about WASM on and off over the past few months I now have a better idea about it than I had back then. This blog post attempts to sum up what I’ve learnt so far both by tinkering with and talking to various people about it.

# Assembly language for the web

Most of the software engineers know how the code gets run on machines, but many often don’t – this is surprisingly the case with a new generation of programmers who hardly ever get exposed to the low level parts of software stack. In my opinion, every developer should have at least some basic idea what’s going on underneath the code they write.

From a very high level point of view there are two basic ways how the code you ends up run by some sort of machine:

- **compiled languages:** you write some code, it gets compiled into some binary form
    - the binary can be run directly on a machine - by running I mean CPU executes the compiled binary by executing various instructions from its Instruction Set Architecture (ISA) (this is how `C/C++` programs work)
    - the binary gets decoded by some runtime and turned into machine code which can then be executed using the instructions from the machine ISA. (this is how java programs work)
- **interpreted languages:** you write some code and let the language interpreter do its job; it parses the code and then executes it on a machine in a similar fashion as described above
- **hybrids:** you write some code and the code gets, parsed, compiled and executed in one step; all this work is done by some [Just In Time](https://cybernetist.com/2019/04/25/wasm-universal-application-runtime/[Just-in-time%20compilation%20-%20Wikipedia](https://en.wikipedia.org/wiki/Just-in-time_compilation)) compilers; JITs do a lot of other things such as optimisation or whatnot, but the basic idea is the same (this is how LUA programs work)

The machine code which is executed by CPUs is literally a string of `0`s and `1`s, alas, if we need to, we normally inspect it in a more “condensed” hex format using tools like [objdump](http://man7.org/linux/man-pages/man1/objdump.1.html) or some hex editors like [Hex Fiend](https://ridiculousfish.com/hexfiend/). Of course these days nobody (I know of) writes [long] programs in raw machine code, though small modifications are still sometimes done manually by security or hardware engineers. However, we do occasionally write programs (or some highly optimised parts of them) in [assembly languages](https://en.wikipedia.org/wiki/Assembly_language). Assembly languages are still super low level so, usually developers don’t have to interact with them at all. Assembly languages also have compilers which turn the assembly code into machine code.

Assembly compilers are normally called transparently without our knowing about them, but as I already mentioned, some developers often do write assembly code for highly optimised code paths — this is for example the case in game development or [IoT](https://en.wikipedia.org/wiki/Internet_of_things) software run on embedded devices.

Now let’s get back to WASM. WASM creators wanted to make the web faster and I’m guessing by the way of connecting different mental models as we humans usually do, its creators probably thought of the idea of assembly [language] for the web. I don’t know if that were really the case, but I wouldn’t be surprised if it were. What I found out was that WASM started like a simplified binary representation for [asm.js](http://asmjs.org/). It was originally designed to be some sort of JavaScript, the dominant language of the web, alas more efficient representation of it:

> an extraordinarily optimizable, low-level subset of JavaScript

But as it often happens, when creating something new, you might end up opening a door to a whole new world. And that seemed to be the case with WASM. It has gone through quite some evolution since it was created: from an instruction set for a [register machine](https://en.wikipedia.org/wiki/Register_machine) to the current binary instruction set for a [stack machine](https://en.wikipedia.org/wiki/Stack_machine).

What’s great about WASM is that it has a full blown [mostly] [Apache License](https://www.apache.org/licenses/LICENSE-2.0)  [specification](https://github.com/WebAssembly/spec). Specifications are powerful weapons of innovations if they’re open to everyone which is exactly the case with WASM. Complying with specification leads to interoperability, which makes even more room for innovation to ever so wider group of people across wide spectrum of environments. Arguably, the best proof of how powerful specifications can be are the various protocol RFCs which define “how the internet works”. But this is not a blog post about specifications, so let’s move on, assuming WASM has one. This will be important later on.

# Virtual machines and runtimes

As I mentioned earlier some programming language compilers do not produce a binary which can be directly executed on machines. Instead, they produce some kind of [bytecode](https://en.wikipedia.org/wiki/Bytecode) which is then either turned into native machine code and then executed or the bytecode is executed in-flight in some [p-code machine](https://en.wikipedia.org/wiki/P-code_machine). Bytecode is a sort of instruction set just like the instruction set defined in ISA I had mentioned earlier. There are many reasons for “multistage program execution” via bytecode such as higher efficiency, execution safety, portability or whatnot. But how is this related to WASM?

As I said earlier, WASM specification defines a binary instruction set (besides other things such as the format of the WASM binary or even its text representation etc.). What this means is, WASM being a compilation target, any compiler which follows/complies with WASM specification can produce WASM binary “blobs” which can then be used by other tools which follow the specification. The huge deal here is we are finally agreeing on common [intermediate representation](https://en.wikipedia.org/wiki/Intermediate_representation)(IR) format for the web!

At the moment we’ve got big a mixture of different binaries and programs running on and off the web, each defining its own way of execution, which leads to a language runtime sprawl at the expense of interoperability and general operational headaches. Docker have helped to alleviate some of these issues a bit, but I feel it was just a first step.

Programming language runtimes have become the differentiating factor for choosing particular language stack. One thing which has often been annoying me was why couldn’t I run a program written in X in virtual machine for language Y to take advantage of the machines capabilities. Yes, there is [GraalVM](https://cybernetist.com/2019/04/25/wasm-universal-application-runtime/[GraalVM](https://www.graalvm.org/)), but it can we trust Oracle? Some scars run deep and heal long :-)

WASM having open IR specification the industry agrees on is a huge deal with regards to what I just said. This can be a big win not only for the end web users who will experience faster web, but more importantly this opens a whole new world of opportunities for innovation both on the web and its edge as well as on runtime/execution side of things! A lot of work needs to be done to make WASM successful, but I’m very optimistic!

Let’s have a look at WASM execution first. Up until recently WASM binaries could only be loaded an executed by browsers — more specifically by JavaScript runtimes (such as V8) built into/shipped with the browsers. General WASM workflow would look something like this:

- write code in some statically typed compiled programming language and compile it to WASM binary
- load the WASM binary using some high level JavaScript API and call the functions available in/exported by the loaded WASM binary

This process seems simple but it practice it used to be kinda clunky. When I played with WASM last year it was an interesting experience. Learning about WASM was a lot of fun and a tremendous learning experience despite its being a bit rough around the edges at the time. There was not (and probably still isn’t YET) a way to access [DOM](https://en.wikipedia.org/wiki/Document_Object_Model) directly from WASM (maybe there still isn’t). Equally, you only had access to a limited set of the Web APIs, but ultimately you couldn’t run WASM binaries on their own as standalone programs. You can have a look at my GitHub [repo](https://github.com/milosgajdos83/wasm-playground) for both simple and slightly more advanced `C` and `Rust` examples as well as in the raw WAST (WASM text representation). Fortunately a lot has changed since then…

First of all, Mozilla have made a lot of progress on their WASM JIT called [wasmtime](https://github.com/CraneStation/wasmtime) which does translation and execution of WASM in one pass. [wasmer.io](https://wasmer.io/) made WASM binaries executable “Docker style”. Their runtime currently support several languages. What’s cool about wasmer is you get the “Docker experience” i.e. you can run a WASM binary by simply executing something like `wasmer run foo/bar.wasm`. [Fastly](https://www.fastly.com/) recently open sourced [lucet](https://github.com/fastly/lucet) which is their WASM compiler and runtime and I’m sure [Cloudflare](https://www.cloudflare.com/) are cooking up some WASM goodness besides what’s already available in their [workers](https://developers.cloudflare.com/workers/) offering which can now run WASM binaries taking advantage of [V8](https://v8.dev/) engine as described in this [talk](https://www.infoq.com/presentations/cloudflare-v8) by [Kenton Varda](https://twitter.com/kentonvarda). You can see the common theme here: “Race to the edge”.

Besides all of these “commercial” offerings (commercial in a sense that they’re offered as a service or their development is funded by commercial entities), there is a lot of innovation happening in the WASM runtime space. Take [WAVM](https://github.com/WAVM/WAVM), WebAssembly Virtual Machine which can load both WASM binaries as well as their text representations and then execute them. Or [WASMVM](https://github.com/WASMVM/WASMVM) or even the [dotnet-webassembly](https://github.com/RyanLamansky/dotnet-webassembly) which lets you load and run WASM from `dotnet` programs. And I’m pretty sure there are and will be many many more out there hiding in dark corners of GitHub. One of the most interesting projects I’ve come across recently is [nebulet](https://github.com/nebulet/nebulet). Nebulet is a microkernel which can execute WASM binaries in [Ring0](https://en.wikipedia.org/wiki/Protection_ring). I mean this is super cool! Of course we can’t always avoid user space, but this is nevertheless a very interesting project as your WASM binary suddenly gains access to the features of OS directly inaccessible from user space.

All of this kind of validates what we suspected last summer: WASM will not stop on the web. It will crawl into everything. It will be on the web, it will be “embedded” in programs and embeddable by programs. It will run on mobile phones and embedded devices. This vision might seem kinda crazy and maybe it is, but with the recent announcement of [WebAssembly System Interface](https://hacks.mozilla.org/2019/03/standardizing-wasi-a-webassembly-system-interface/) (WASI) which attempts to standardise WASM interface to be run on arbitrary Operating Systems it might turn out to be the reality . WASI essentially means WASM will no longer be confined to browser sandboxes or specific runtime environments – in the future we might be able to run WASM everywhere.

# Interesting challenges

Of course all is not hunky dory. There are a lot of things that need to be addressed both in the specification as well as in the tooling space. For starters I’m still not sure if one can finally access DOM directly from WASM binary. Or what Web APIs are accessible by WASM directly? Sharing data is also a bit clunky and the decision whether to add [Garbage Collector](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) to WASM still does not seem to have been taken.

One interesting aspect of WASM is [security](https://webassembly.org/docs/security/). WASM specification allows to prevent a lot of well known runtime hijacking issues such as the infamous [stack overflow](https://en.wikipedia.org/wiki/Stack_buffer_overflow). But one particular aspect of WASM caught my attention: the security in the announced WASI specification takes a lot of inspiration from [Capability-based security](https://en.wikipedia.org/wiki/Capability-based_security).

I’ve been chatting to [Justin Cormack](https://en.wikipedia.org/wiki/Capability-based_security) about capability-based security occasionally after he had given a talk about what he referred to as “[an obscure whitepaper by HP](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.406.4684&rep=rep1&type=pdf)”. You can watch the talk [here](https://www.youtube.com/watch?v=G7VUR0Bi3BU). Capability-based security is super interesting. It sort of flips the traditional [Access Control List](https://en.wikipedia.org/wiki/Access_control_list) model on its head. With ACLs one attaches a list of permissions to an object which define the object access control — permissions have to be however validated by some authority which is usually underlying operating system. It turns out this does not scale that well as it requires a lot of maintenance and operational overhead.

Capability-based security on the other hand defines list of actions that can be taken on an object which is uniquely identifiable in the system. You are issued a “capability” (this can have a form of a token) which allows you to perform a particular set of actions on the object. This is more programmatically friendly: the objects are accessed via some sort of handle (a file descriptor or some other construct akin to it) and the owner of the capability can then even perform actions on the capabilities themselves such as restricting it more before passing it on to some other program which will then end up having fewer privileges. This is nothing new or groundbreakingIn fact FreeBSD have had OS capability and sandbox framework for a [while](https://www.freebsd.org/cgi/man.cgi?capsicum(4)) and most recently, [Google Fuchsia](https://en.wikipedia.org/wiki/Google_Fuchsia) has taken the same approach towards its security.

Capability-based security is especially interesting with regards to [ubiquitous computing](https://en.wikipedia.org/wiki/Ubiquitous_computing) – the future we are inevitably headed towards. Everything around us will end up having its own identity. With this form of security one will be issued a token with certain capabilities that will define a set of actions one can take on the objects around. It seems more natural to they physical space to me. If you are interested in this more, I found the following [free online book](https://homes.cs.washington.edu/~levy/capabook/) to be a great source of in-depth knowledge.

# What next

You might wonder now: what will happen to docker? After all, docker is the current universal application “runtime” alas it has different form: instead of compiling into WASM binaries we are building docker images; instead of running WASM binaries we run our applications inside docker containers. None of this will disappear any time soon in my opinion.

Even if we ever reach the tiny fraction of the future I’m imagining in this blog post we will still want to isolate our programs in their own namespaces and assign system resources to them. Until we come up with a different model to deal with isolation and resource management I can’t see docker or any other container runtime going away even with the brightest of WASM futures. Besides, we will still need some sort of API to manage the applications and their lifecycle, especially now that we have started chucking them into clusters and various cloud platforms. So, I think WASM+Docker = <3 for the foreseeable future.

Equally, what will happen to the industry proven and battle tested virtual machines/runtimes like [JVM](https://cybernetist.com/2019/04/25/wasm-universal-application-runtime/[Java%20virtual%20machine%20-%20Wikipedia](https://en.wikipedia.org/wiki/Java_virtual_machine)) or [BEAM](https://cybernetist.com/2019/04/25/wasm-universal-application-runtime/[BEAM%20(Erlang%20virtual%20machine)%20-%20Wikipedia](https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)))? To be honest, I don’t know. I feel like there are few possible futures:

- they might gain new “superpowers” in a sense they might incorporate WASM support into their specifications so they are be able to build and execute WASM binaries just like they execute java classes and erlang beams
- they won’t do anything about it and will carry on independently without WASM support; this will lead to random developers creating projects that will make WASM possible independently of official specs and that might, after WASM adoption gains critical mass, flip the equation.
- another potential scenario which I can’t think of right now – feel free to add it into comments

The strongest point in favour of WASM is we can achieve true portability which has so far been constrained to **within-language portability** i.e. we can run java programs across different architectures but only inside JVM; the same goes for Erlang programs etc.. WASM has a huge opportunity to change this and make true portability a thing!

There has never been a better time to join WASM movement — we are only getting started! Mozilla are [hiring](https://twitter.com/linclark/status/1120745455527317505)!

*Note: Early draft of this blog post was reviewed by [Asim](https://twitter.com/chuhnk) and [Justin](https://twitter.com/justincormack) both of whom I’m always grateful for their patience when answering my silly questions and endless conversations about tech*

Tags:   [#wasm](https://cybernetist.com/tags/wasm/)  [#WebAssembly](https://cybernetist.com/tags/webassembly/)

* * *

- [**](https://twitter.com/share?url=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f&text=WASM%3a%20Universal%20Application%20Runtime&via=milosgajdos)

- [**](https://plus.google.com/share?url=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f)

- [**](https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f)

- [**](https://reddit.com/submit?url=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f&title=WASM%3a%20Universal%20Application%20Runtime)

- [**](https://www.linkedin.com/shareArticle?url=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f&title=WASM%3a%20Universal%20Application%20Runtime)

- [**](https://www.stumbleupon.com/submit?url=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f&title=WASM%3a%20Universal%20Application%20Runtime)

- [**](https://www.pinterest.com/pin/create/button/?url=https%3a%2f%2fcybernetist.com%2f2019%2f04%2f25%2fwasm-universal-application-runtime%2f&description=WASM%3a%20Universal%20Application%20Runtime)