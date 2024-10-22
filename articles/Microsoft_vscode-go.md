Microsoft/vscode-go

# [(L)](https://github.com/Microsoft/vscode-go#go-for-visual-studio-code)Go for Visual Studio Code

[[Join the chat at https://gitter.im/Microsoft/vscode-go](../_resources/18b9c2d4d764e780706306a133785dc6.bin)](https://gitter.im/Microsoft/vscode-go?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)  [[Build Status](../_resources/af3359b6a330e8be6d21e0274c77bc30.bin)](https://travis-ci.org/Microsoft/vscode-go)

Read the [Release Notes](https://github.com/Microsoft/vscode-go/wiki/Release-Notes) to know what has changed over the last few versions of this extension

This extension adds rich language support for the Go language to VS Code, including:

- Completion Lists (using ` gocode `)
- Signature Help (using ` gogetdoc ` or ` godef `+` godoc `)
- Snippets
- Quick Info (using ` gogetdoc ` or ` godef `+` godoc `)
- Goto Definition (using ` gogetdoc ` or ` godef `+` godoc `)
- Find References (using ` guru `)
- Find implementations (using ` guru `)
- References CodeLens
- File outline (using ` go-outline `)
- Workspace symbol search (using ` go-symbols `)
- Rename (using ` gorename `. Note: For Undo after rename to work in Windows you need to have ` diff ` tool in your path)
- Build-on-save (using ` go build ` and ` go test `)
- Lint-on-save (using ` golint ` or ` gometalinter `)
- Format on save as well as format manually (using ` goreturns ` or ` goimports ` or ` gofmt `)
- Generate unit tests skeleton (using ` gotests `)
- Add Imports (using ` gopkgs `)
- Add/Remove Tags on struct fields (using ` gomodifytags `)
- Semantic/Syntactic error reporting as you type (using ` gotype-live `)
- Run Tests under the cursor, in current file, in current package, in the whole workspace (using ` go test `)
- Show code coverage
- Generate method stubs for interfaces (using ` impl `)
- [*partially implemented*] Debugging (using ` delve `)

### [(L)](https://github.com/Microsoft/vscode-go#ide-features)IDE Features

[![IDE](../_resources/dd99c8ac399072c7cfca0bb81d76755b.gif)](https://camo.githubusercontent.com/3fb1d62bbc7b1306da783f395c3589c3ae709b1c/68747470733a2f2f692e67697068792e636f6d2f785469546e64444856334765497936614e612e676966)

## [(L)](https://github.com/Microsoft/vscode-go#how-to-use-this-extension)How to use this extension?

Install and open [Visual Studio Code](https://code.visualstudio.com/). Press ` Ctrl+Shift+X ` or ` Cmd+Shift+X ` to open the Extensions pane. Find and install the Go extension. You can also install the extension from the [Marketplace](https://marketplace.visualstudio.com/items?itemName=lukehoban.Go).Open any ` .go ` file in VS Code. The extension is now activated.

This extension uses a set of Go tools to provide the various rich features. These tools are installed in your GOPATH by default. If you wish to have these tools in a separate location, provide the desired location in the setting ` go.toolsGopath `. Read more about this and the tools at [Go tools that the Go extension depends on](https://github.com/Microsoft/vscode-go/wiki/Go-tools-that-the-Go-extension-depends-on)

You will see ` Analysis Tools Missing ` in the bottom right, clicking this will offer to install all of the dependent Go tools. You can also run the command ` Go: Install/Update tools ` to install/update the same.

**Note 1**: Read [GOPATH in the VS Code Go extension](https://github.com/Microsoft/vscode-go/wiki/GOPATH-in-the-VS-Code-Go-extension) to learn about the different ways you can get the extension to set GOPATH.

**Note 2**: Users may want to consider turning ` Auto Save ` on in Visual Studio Code (` "files.autoSave": "afterDelay" `) when using this extension. Many of the Go tools work only on saved files, and error reporting will be more interactive with ` Auto Save ` turned on. If you do turn ` Auto Save ` on, you may also want to turn format-on-save off (` "go.formatOnSave": false `), so that it is not triggered while typing.

**Note 3**: This extension uses ` gocode ` to provide completion lists as you type. To provide fresh results, including against not-yet-built dependencies, the extension uses ` gocode `'s ` autobuild=true ` setting. If you experience any performance issues with autocomplete, you should try setting ` "go.gocodeAutoBuild": false ` in your VS Code settings.

### [(L)](https://github.com/Microsoft/vscode-go#customizing-the-go-extension-features)Customizing the Go extension features

The Go extension is ready to use on the get go. If you want to customize the features, you can edit the settings in your User or Workspace settings. Read [All Settings & Commands in Visual Studio Code Go extension](https://github.com/Microsoft/vscode-go/wiki/All-Settings-&-Commands-in-Visual-Studio-Code-Go-extension) for the full list of options and their descriptions.

### [(L)](https://github.com/Microsoft/vscode-go#go-language-server-experimental)Go Language Server (Experimental)

Set ` go.useLanguageServer ` to ` true ` to use the Go language server from [Sourcegraph](https://github.com/sourcegraph/go-langserver) for features like Hover, Definition, Find All References, Signature Help, Go to Symbol in File and Workspace.

- This is an experimental feature and is not available in Windows yet.
- If set to true, you will be prompted to install the Go language server. Once installed, you will have to reload VS Code window. The language server will then be run by the Go extension in the background to provide services needed for the above mentioned features.
- Everytime you change the value of the setting ` go.useLanguageServer `, you need to reload the VS Code window for it to take effect.
- To collect traces, set ` "go.languageServerFlags": ["-trace"] `
- To collect errors from language server in a logfile, set ` "go.languageServerFlags": ["-trace", "-logfile", "path to a text file that exists" ] `

### [(L)](https://github.com/Microsoft/vscode-go#linter)Linter

A linter is a tool giving coding style feedback and suggestions. By default this extension uses the official [golint](https://github.com/golang/lint) as a linter.

You can change the default linter and use the more advanced [Go Meta Linter](https://github.com/alecthomas/gometalinter)by setting ` go.lintTool ` to "gometalinter" in your settings.

Go meta linter uses a collection of various linters which will be installed for you by the extension.

Some of the very useful linter tools:

- [errcheck](https://github.com/kisielk/errcheck) checks for unchecked errors in your code.
- [varcheck](https://github.com/opennota/check) finds unused global variables and constants.
- [deadcode](https://github.com/tsenart/deadcode) finds unused code.

If you want to run only specific linters (some linters are slow), you can modify your configuration to specify them:

 "go.lintFlags": ["--disable-all", "--enable=errcheck"],

Alternatively, you can use [megacheck](https://github.com/dominikh/go-tools/tree/master/cmd/megacheck) which may have significantly better performance than ` gometalinter `, while only supporting a subset of the tools.

Finally, the result of those linters will show right in the code (locations with suggestions will be underlined), as well as in the output pane.

### [(L)](https://github.com/Microsoft/vscode-go#commands)Commands

In addition to integrated editing features, the extension also provides several commands in the Command Palette for working with Go files:

- ` Go: Add Import ` to add an import from the list of packages in your Go context
- ` Go: Current GOPATH ` to see your currently configured GOPATH
- ` Go: Test at cursor ` to run a test at the current cursor position in the active document
- ` Go: Test Package ` to run all tests in the package containing the active document
- ` Go: Test File ` to run all tests in the current active document
- ` Go: Test Previous ` to run the previously run test command
- ` Go: Test All Packages in Workspace ` to run all tests in the current workspace
- ` Go: Generates unit tests for package ` Generates unit tests for the current package
- ` Go: Generates unit tests for file ` Generates unit tests for the current file
- ` Go: Generates unit tests for function ` Generates unit tests for the selected function in the current file
- ` Go: Install Tools ` Installs/updates all the Go tools that the extension depends on
- ` Go: Add Tags ` Adds configured tags to selected struct fields.
- ` Go: Remove Tags ` Removes configured tags from selected struct fields.
- ` Go: Generate Interface Stubs ` Generates method stubs for given interface

You can access all of the above commands from the command pallet (` Cmd+Shift+P ` or ` Ctrl+Shift+P `).

Few of these are available in the editor context menu as an experimental feature as well. To control which of these commands show up in the editor context menu, update the setting ` go.editorContextMenuCommands `

### [(L)](https://github.com/Microsoft/vscode-go#optional-debugging)*Optional*: Debugging

To use the debugger, you must currently manually install ` delve `. See the [Installation Instructions](https://github.com/derekparker/delve/tree/master/Documentation/installation) for full details. On OS X it requires creating a self-signed cert to sign the ` dlv ` binary.

For more read [Debugging Go Code Using VS Code](https://github.com/Microsoft/vscode-go/wiki/Debugging-Go-code-using-VS-Code)

#### [(L)](https://github.com/Microsoft/vscode-go#remote-debugging)Remote Debugging

To remote debug using VS Code, read [Remote Debugging](https://github.com/Microsoft/vscode-go/wiki/Debugging-Go-code-using-VS-Code#remote-debugging)

## [(L)](https://github.com/Microsoft/vscode-go#building-and-debugging-the-extension)Building and Debugging the Extension

You can set up a development environment for debugging the extension during extension development. Read more at [Building, Debugging and Sideloading the extension in Visual Studio Code](https://github.com/Microsoft/vscode-go/wiki/Building,-Debugging-and-Sideloading-the-extension-in-Visual-Studio-Code)

## [(L)](https://github.com/Microsoft/vscode-go#tools-this-extension-depends-on)Tools this extension depends on

This extension uses a host of Go tools to provide the various rich features. These tools are installed in your GOPATH by default. If you wish to have the extension use a separate GOPATH for its tools, provide the desired location in the setting ` go.toolsGopath `. Read more about this and the tools at [Go tools that the Go extension depends on](https://github.com/Microsoft/vscode-go/wiki/Go-tools-that-the-Go-extension-depends-on)

## [(L)](https://github.com/Microsoft/vscode-go#license)License

[MIT](https://github.com/Microsoft/vscode-go/blob/master/LICENSE)