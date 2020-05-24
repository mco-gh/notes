The Svelte Compiler Handbook | Tan Li Hau

# The Svelte Compiler Handbook

April 05, 2020

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='103' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='282' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#who-is-this-for)Who is this for?

Anyone who

- is interested in the Svelte compilation process
- wants to get started in reading Svelte source code

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='104' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='288' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#overview)Overview

 [  ![overview.png](../_resources/8a5859f36c91be53fa928f81981e29c8.png)](https://lihautan.com/static/8ab733c6a095f91034a7e221221fcdb4/4f8eb/overview.png)

The Svelte compilation process can be broken down into 4-steps

- Parsing source code into Abstract Syntax Tree (AST)
- Tracking references and dependencies
- Creating code blocks and fragments
- Generate code

Which sums out by the following pseudocode:

	const source = fs.readFileSync('App.svelte');

	// parse source code into AST
	const ast = parse(source);

	// tracking references and dependencies
	const component = new Component(ast);

	// creating code blocks and fragments
	const renderer =
	  options.generate === 'ssr' ? SSRRenderer(component) : DomRenderer(component);

	// Generate code
	const { js, css } = renderer.render();

	fs.writeFileSync('App.js', js);
	fs.writeFileSync('App.css', css);

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='105' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='364' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#1-parsing-source-code-into-ast)1. Parsing source code into AST

 [  ![step-1.png](../_resources/396ec2aa18b462e65695e456cb353104.png)](https://lihautan.com/static/6f446bed0985ebf8426f93d997165343/7ef2e/step-1.png)

	// parse source code into AST
	const ast = parse(source);

The Svelte syntax is a superset of HTML. Svelte implements its own parser for the Svelte syntax, which handles:

- HTML syntax `<div>`
- Curly brackets `{ data }`
- Logic blocks `{#each list as item}`

The Svelte parser handles specially for `<script>` and `<style>` tags.

When the parser encounters a `<script>` tag, it uses [acorn](https://www.npmjs.com/package/acorn) to parse the content within the tag. When the parser sees a `<style>` tag, it uses [css-tree](https://www.npmjs.com/package/css-tree) to parse the CSS content.

Besides, the Svelte parser differentiates instance script, `<script>`, and module script, `<script context="module">`.

The Svelte AST look like:

	{
	  html: { type: 'Fragment', children: [...] },
	  css: { ... },
	  instance: { context: 'default', content: {...} },
	  module: { context: 'context', content: {...} },
	}

You can try out the Svelte parser in [ASTExplorer](https://astexplorer.net/#/gist/828907dd1600c208a4e315962c635b4a/e1c895d49e8899a3be849a137fc557ba66eb2423). You can find the Svelte parser under **HTML > Svelte**.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='106' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='428' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#where-can-i-find-the-parser-in-the-source-code)Where can I find the parser in the source code?

The parsing [starts here](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/index.ts#L79), which the parser is implemented in [src/compiler/parse/index.ts](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/parse/index.ts).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='107' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='431' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#where-can-i-learn-about-parsing-in-javascript)Where can I learn about parsing in JavaScript?

My previous article, [“JSON Parser with JavaScript”](https://lihautan.com/json-parser-with-javascript) introduces the terminology and guides you step-by-step on writing a parser for JSON in JavaScript.

If this is the your first time learning about parser, I highly recommend you to read that.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='108' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='435' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#2-tracking-references-and-dependencies)2. Tracking references and dependencies

 [  ![step-2.png](:/9c26f89e04cc16a90c1c9329d5c9bdec)](https://lihautan.com/static/b72ac678bfbb893f0087ea4bafa5f264/b89e5/step-2.png)

	// tracking references and dependencies
	const component = new Component(ast);

In this step, Svelte traverses through the AST to track all the variable declared and referenced and their depedencies.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='109' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='450' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#a-svelte-creates-a-code-classlanguage-textcomponentcode-instance)a. Svelte creates a `Component` instance.

The `Component` class stores information of the Svelte component, which includes:

- HTML fragment, [`fragment`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L52)
- instance script and module script AST and their lexical scopes, [`instance_scope`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L54) and [`module_scope`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L53)
- instance variables, [`vars`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L62)
- reactive variables, [`reactive_declarations`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L71)
- slots, [`slots`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L94)
- [used variable names](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L351) to prevent naming conflict when creating temporary variables
- [warnings](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L43) and [errors](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L396)
- [compile options](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L51) and [ignored warnings](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts#L44)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='110' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='462' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#b-traverse-the-instance-script-and-module-script-ast)b. Traverse the instance script and module script AST

`Component` traverses the instance script and module script AST to **find out all the variables declared, referenced, and updated** within the instance script and module script.

Svelte identifies all the variables available before traversing the template. When encountering the variable during template traversal, Svelte will mark the variable as `referenced` from template.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='111' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='466' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#c-traverse-the-template)c. Traverse the template

Svelte traverses through the template AST and creates a [Fragment](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Fragment.ts) tree out of the template AST.

Each fragment node contains information such as:
**- expression and dependencies**

Logic blocks, `{#if}`, and mustache tags, `{ data }`, contain expression and the dependencies of the expression.

**- scope**

`{#each}` and `{#await}` logic block and `let:` binding create new variables for the children template.

Svelte creates a different Fragment node for each type of node in the AST, as different kind of Fragment node handles things differently:

- [Element node](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Element.ts) validates the [attribute](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Element.ts#L280), [bindings](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Element.ts#L461), [content](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Element.ts#L647) and [event handlers](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Element.ts#L658).
- [Slot node](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/Slot.ts) registers the slot name to the `Component`.
- [EachBlock node](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/nodes/EachBlock.ts) creates a new scope and tracks the `key`, `index` and the name of the list to be iterated.
- …

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='112' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='480' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#d-traverse-the-instance-script-ast)d. Traverse the instance script AST

After traversing through the template, Svelte now knows whether a variable is ever being updated or referenced in the component.

With this information, Svelte tries make preparations for optimising the output, for example:

- determine which variables or functions can be safely hoisted out of the `instance` function.
- determine reactive declarations that does not need to be reactive

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='113' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='487' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#e-update-css-selectors-to-make-style-declarations-component-scope)e. Update CSS selectors to make style declarations component scope

Svelte updates the CSS selectors, by adding `.svelte-xxx` class to the selectors when necessary.

At the end of this step, Svelte has enough information to generate the compiled code, which brings us to the next step.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='114' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='491' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#where-can-i-find-this-in-the-source-code)Where can I find this in the source code?

You can start reading [from here](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/index.ts#L83-L90), which the `Component` is implemented in [src/compiler/compile/Component.ts](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/Component.ts).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='115' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='494' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#where-can-i-learn-about-traversing-in-javascript)Where can I learn about traversing in JavaScript?

Bear with my shameless plug, my previous article, [“Manipulating AST with JavaScript”](https://lihautan.com/manipulating-ast-with-javascript#traversing-an-ast) covers relevant knowledge you need to know about traversing AST in JavaScript.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='116' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='497' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#3-creating-code-blocks-and-fragments)3. Creating code blocks and fragments

 [  ![step-3.png](../_resources/e2856519e2375598fa17ef9b0d89a2eb.png)](https://lihautan.com/static/f3876e59140a31ded960358a9c5dfab8/363f6/step-3.png)

	// creating code blocks and fragments
	const renderer =
	  options.generate === 'ssr' ? SSRRenderer(component) : DomRenderer(component);

In this step, Svelte creates a `Renderer` instance which keeps track necessary information required to generate the compiled output. Depending on the whether to output DOM or SSR code *([see `generate` in compile options](https://svelte.dev/docs#svelte_compile))*, Svelte instantiates different `Renderer` respectively.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='117' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='520' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#dom-renderer)DOM Renderer

DOM Renderer keeps track of [a list of blocks](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_dom/Renderer.ts#L31) and [context](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_dom/Renderer.ts#L28).

A [Block](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_dom/Block.ts) contains code fragments for generate the [`create_fragment`](https://lihautan.com/compile-svelte-in-your-head-part-1/#create_fragment) function.

Context tracks a list of [instance variables](https://lihautan.com/compile-svelte-in-your-head-part-2/#ctx) which will be presented in the `$$.ctx` in the compiled output.

In the renderer, Svelte creates a [render tree](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_dom/wrappers/Fragment.ts) out of the Fragment tree.

Each node in the render tree implements the `render` function which generate codes that create and update the DOM for the node.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='118' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='527' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#ssr-renderer)SSR Renderer

SSR Renderer provide helpers to generate [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) in the compiled output, such as [`add_string(str)`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_ssr/Renderer.ts#L63) and [`add_expression(node)`](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_ssr/Renderer.ts#L67).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='119' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='530' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#where-can-i-find-the-code-classlanguage-textrenderercode-in-the-source-code)Where can I find the `Renderer` in the source code?

The DOM Renderer is implemented in [src/compiler/compile/render_dom/Renderer.ts](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_dom/Renderer.ts), and you can check out the SSR Renderer code in [src/compiler/compile/render_ssr/Renderer.ts](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_ssr/Renderer.ts).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='120' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='533' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#4-generate-code)4. Generate code

 [  ![step-4.png](../_resources/7941a9e3e2ca0cdf1c8192b5d2ebf896.png)](https://lihautan.com/static/adc36d2564cf00a8bb1e20058c100e29/6607e/step-4.png)

	// Generate code
	const { js, css } = renderer.render();

Different renderer renders differently.

**The DOM Renderer** traverses through the render tree and calls the `render` function of each node along the way. The `Block` instance is passed into the `render` function, so that each node inserts the code into the appropriate `create_fragment` function.

**The SSR Renderer**, on the other hand, relies on different [node handlers](https://github.com/sveltejs/svelte/blob/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/compiler/compile/render_ssr/Renderer.ts#L23-L40) to insert strings or expressions into the final template literal.

The render function returns `js` and `css` which will be consumed by the bundler, via [rollup-plugin-svelte](https://github.com/sveltejs/rollup-plugin-svelte) for rollup and [svelte-loader](https://github.com/sveltejs/svelte-loader) for webpack respectively.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' focusable='false' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='121' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='554' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://lihautan.com/the-svelte-compiler-handbook/#svelte-runtime)Svelte runtime

To remove duplicate code in the compiled output, Svelte provide util function which can be found in the [src/runtime/internal](https://github.com/sveltejs/svelte/tree/aa3dcc06d6b0fcb079ccd993fa6e3455242a2a96/src/runtime/internal), such as:

- dom related utils, eg: `append`, `insert`, `detach`
- scheduling utils, eg: `schedule_update`, `flush`
- lifecycle utils, eg: `onMount`, `beforeUpdate`
- animation utils, eg: `create_animation`