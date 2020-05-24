The Go Play Space

# About Go Play Space

This is an experimental alternative [Go Playground](https://play.golang.org/) frontend that is built in Go itself (using [GopherJS](https://github.com/gopherjs/gopherjs), a Go→JavaScript transpiler, and[Vecty](https://github.com/gopherjs/vecty), a React-like frontend library for GopherJS).

[View source code on GitHub](https://github.com/iafan/goplayspace)

[Star](https://github.com/iafan/goplayspace/)  [231](https://github.com/iafan/goplayspace/stargazers)

Main differences from the official Go Playground:

1. Syntax highlighting, auto-closing braces and quotes, proper undo/redo, auto indentation

2. Smart help lookup: double-click on e.g. `package` keyword or `Println` function name in source code, and you will see the relevant help topic. Try it!

3. Live syntax error checking

4. Error line highlighting (both for syntax errors and for errors returned from the compiler)

5. Ability to highlight lines and blocks of code (like on Github, but better!) — just click on the line numbers. Use `Shift` and `Ctrl` to modify the selection

6. Keyboard shortcuts (see button captions)
7. Support for several UI themes and UI tweaks (see the Settings button)

8. Support for [Fira Code](https://github.com/tonsky/FiraCode) font (either the one installed in your system or a webfont)

9. `go imports` is always run before running your code, so you don't usually have to worry about imports at all

Code execution is proxied to the official Go Playground, so your programs will work the same. Shared snippets are also stored on golang.org servers. Any requests for content removal should be directed to [security@golang.org](https://goplay.space/?utm_source=golangweekly&utm_medium=emailmailto:security@golang.org). Please include the URL and the reason for the request.