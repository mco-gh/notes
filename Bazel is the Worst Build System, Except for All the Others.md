Bazel is the Worst Build System, Except for All the Others

# Bazel is the Worst Build System, Except for All the Others

[![1*2ZROXpPfLOBNhdVI0cZjWg.jpeg](../_resources/eb221fc357294c821f7b6dc37ed6b045.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='101' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@nicksantos?source=post_header_lockup)

[Nick Santos](https://medium.com/@nicksantos)
Feb 5, 2018·5 min read

The Go community sometimes argues about whether Go projects should use `go build` or `bazel build`.

![](../_resources/426334451455fb34a227f3486302c010.png)

![](../_resources/889eecb9359975e71877a50845b36558.png)

We talk about this at Windmill Engineering too! We’ve been trying to reconcile two statements:

1. 1 "."Bazel is magic inside Google
2. 2 "."Bazel is a pain to integrate in open source projects
Why?

Before we start picking apart Bazel, it’s important to frame this discussion. We love Bazel! And we think our industry has problems with [contempt culture](https://blog.aurynn.com/2015/12/16-contempt-culture). We don’t want to shame Bazel so much as open up discussion on the design decisions that Bazel made. There are zero-sum trade-offs between supporting different types of projects. Even when it’s the right trade-off to make, it’s still useful to articulate the downsides.

### What is Bazel?

If you have no idea what I’m talking about, here’s a brief explanation of Bazel. (If you’ve already used Bazel, you can skip straight to the complaining below.)

Bazel is a tool for compiling large projects with multi-language dependencies. For example, you might have a Go server that depends on generated Thrift code, or a Python server that depends on transpiled JS. To use Bazel, we write `BUILD` files that declare rules. Each rule declares a target, the rules it depends on, the input files, and the output files. That’s it!

Bazel comes with built-ins for compiling C, Java, Python, etc. It also has `genrule` for generic rules. Here’s a toy example with generic rules:

genrule(
name = 'hello',
outs = ['hello.txt'],
cmd = 'echo hello > $(location hello.txt)')
genrule(
name = 'hello-world',
srcs = [':hello'],
outs = ['hello-world.txt'],
cmd = ('cat $(location :hello) > $(location hello-world.txt); ' +
'echo world >> $(location hello-world.txt)'))

If we squint, it looks like a Makefile. The first rule `hello` creates a file `hello.txt`. The second rule `hello-world` takes the first rule as an input, and creates a file `hello-world.txt`.

You can read more about Bazel at https://www.bazel.build/.

### What’s the Matter With Bazel?

We have lots of complaints! Some are small and fixable. Some are big and unfortunate.

#### Depends on the Java Runtime

I can’t believe it’s 2018 and managing a local Java installation is still painful.

#### No Easy Way to Version Bazel Itself

At my last job, one of the most common build errors was “you have the wrong version of Bazel.” We had to add a wrapper script around the build process that checked that you had the right version installed.

#### Distributed Builds

Google has a distributed build cluster! Slow builds can be parallelized! If two people are building the same file, they can share the same results!

Bazel-team wrote [instructions](https://docs.bazel.build/versions/master/remote-caching.html) on how to run a build cache yourself. It’s non-trivial. Bully for you if you have a dedicated Ops team to run and maintain your build cluster.

#### Explicit Dependency Bookkeeping

Bazel assumes we live in a world where we don’t know where our dependencies live on disk. We have to explicitly list them.

Meanwhile, modern languages have become super opinionated about where dependencies live! Go wants all your code in a rigidly formatted `src`  [tree](https://golang.org/doc/code.html#Workspaces). Our imports are paths into that tree. Rust and Maven have a local dependencies registry. NodeJS wants your dependencies to live in a relative `node_modules` directory.

The big idea is that we can read the source file and automatically figure out where the dependencies live. Bazel doesn’t exploit this information. It wants a strict separation between dependency information from the code. There are projects that [auto-generate Bazel rules](https://github.com/bazelbuild/rules_go#generating-build-files), but they don’t integrate cleanly with the rest of the tooling.

#### Step 1 to Adopting Bazel: Boil the Ocean

Bazel needs to know all the inputs and outputs of rules. The flip side of this is that to adopt Bazel, we need to give it a total description of our build process. It does not have good integration points for inter-operating with other build systems, or for “partial” adoption.

I’m conflicted about this! Walled gardens are nice. You can guarantee that everything in the garden is pretty and well-groomed. It’s nice that there’s a wall to keep you inside and protect you from O(n²) performance problems.

On the flip side, my friend Jason likes to say that the optimal time to adopt Bazel is before you need it. If you try it early, it doesn’t give much value. If you try it later, the migration is a massive engineering project.

#### Declarative Programming Languages are Hard To Debug

Bazel’s configuration is “declarative-ish.” The BUILD files declare rules in a build graph. There are ways to break out into imperative code, but most configuration is declarative.

We are still not good at building debuggers for declarative languages. CSS is the example that proves the rule: it took decades for good CSS debuggers to come out. CSS is still a struggle for many.

Too much of the Bazel configuration forces you to visualize build graphs in your head.

#### Local Build Systems are Inherently A Pain

This reminds me of a great joke:

![](../_resources/89812ff1d1b0e56fc1c2892066df30a0.png)

Running a local hermetic build system is like being a doctor in a medical drama, but you have the same infection and everything you do re-infects the patient.

Any engineering team with more than a few people needs processes to make sure that everyone has the same tools installed. Woe be to you if you install something to make the build work, but forget what you did.

Bazel tries to sandbox your build process to help make the build hermetic and reproducible across computers. But the sandboxing primitives are OS-specific and sometimes leaky. It’s often hard to debug things inside the sandbox.