VSCodeVim/Vim

###    README.md

# [(L)](https://github.com/VSCodeVim/Vim#vim---)Vim [[Version](../_resources/3cf6927c8b278a775a292d63ed7b266b.bin)](http://aka.ms/vscodevim)  [[Build Status](../_resources/af3359b6a330e8be6d21e0274c77bc30.bin)](https://travis-ci.org/VSCodeVim/Vim)  [[Slack Status](../_resources/b9e23c7705cc0d781904c9c0375df351.bin)](https://vscodevim-slackin.azurewebsites.net/)

VSCodeVim is a [Visual Studio Code](https://code.visualstudio.com/) extension that enables Vim keybindings, including:

- Modes: normal, insert, command, visual, visual line, visual block (with ` useCtrlKeys `, see below)
- Command combinations (` c3w `, ` daw `, ` 2dd `, etc)
- Highly versatile command remapping (` jj ` to esc, ` : ` to command panel, etc.)
- Incremental search with ` / ` and ` ? `
- Marks
- Vim settings similar to those found in .vimrc
- Multi-cursor support. Allows multiple simultaneous cursors to receive Vim commands (e.g. allows ` / ` search, each cursor has independent clipboards, etc.).
- The [EasyMotion plugin](https://github.com/VSCodeVim/Vim#how-to-use-easymotion)!
- The [Surround.vim plugin](https://github.com/VSCodeVim/Vim#how-to-use-surround)!
- And much more! Refer to the [roadmap](https://github.com/VSCodeVim/Vim/blob/master/ROADMAP.md) or everything we support.

Please [report missing features/bugs on GitHub](https://github.com/VSCodeVim/Vim/issues), which will help us get to them faster.

Ask us questions, talk about contributing, or just say hi on [Slack](https://vscodevim-slackin.azurewebsites.net/)!

## [(L)](https://github.com/VSCodeVim/Vim#donations)Donations

[![Donate](../_resources/48d99fdb79bd5d74e8129dc0062e827a.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=FNUBXQADN5VG4)

[Make a donation to VSCodeVim here!](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=FNUBXQADN5VG4)

Donations help convince me to work on this project rather than my other (non-open-source) projects. I'd love to work on VSCodeVim full time, but I need money to live!

## [(L)](https://github.com/VSCodeVim/Vim#configuring-vscodevim)Configuring VSCodeVim

Below is an example of a [settings.json](https://code.visualstudio.com/Docs/customization/userandworkspace) file for VSCode settings applicable to this extension. The following section goes over some supported options in more detail.

	{
	    "vim.easymotion": true,
	    "vim.incsearch": true,
	    "vim.useSystemClipboard": true,
	    "vim.useCtrlKeys": true,
	    "vim.hlsearch": true,
	    "vim.insertModeKeyBindings": [
	        {
	            "before": ["j","j"],
	            "after": ["<Esc>"]
	        }
	    ],
	    "vim.otherModesKeyBindingsNonRecursive": [
	        {
	            "before": ["<leader>","d"],
	            "after": ["d", "d"]
	        }
	    ],
	    "vim.leader": "<space>",
	    "vim.handleKeys":{
	        "<C-a>": false,
	        "<C-f>": false
	    }
	}

## [(L)](https://github.com/VSCodeVim/Vim#supported-options)Supported Options

The following is a subset of the supported configurations; the full list is described in the ` Contributions ` tab for this extension, or in our [package.json](https://github.com/VSCodeVim/Vim/blob/master/package.json#L175).

#### [(L)](https://github.com/VSCodeVim/Vim#usectrlkeys)useCtrlKeys

- Enable Vim ctrl keys overriding common VS Code operations (eg. copy, paste, find, etc). Setting this option to true will enable:
    - ` ctrl+c `, ` ctrl+[ ` => ` <Esc> `
    - ` ctrl+f ` => Full Page Forward
    - ` ctrl+d ` => Half Page Back
    - ` ctrl+b ` => Half Page Forward
    - ` ctrl+v ` => Visual Block Mode
    - etc.
- Type: Boolean (Default: ` true `)
- *Example:*

	"vim.useCtrlKeys": true

#### [(L)](https://github.com/VSCodeVim/Vim#handlekeys)handleKeys

- Allows user to select certain modifier keybindings and delegate them back to VSCode so that VSCodeVim does not process them.
- Complete list of keys that can be delegated back to VSCode can be found in our [package.json](https://github.com/VSCodeVim/Vim/blob/master/package.json#L44). Each key that has a vim.use<C-...> in the when argument can be delegated back to vscode by doing "<C-...>":false.
- An example would be if a user wanted to continue to use ctrl + f for find, but wants to have useCtrlKeys set to true so that other vim bindings work.

	"vim.handleKeys":{
	    "<C-a>": false,
	    "<C-f>": false
	}

#### [(L)](https://github.com/VSCodeVim/Vim#insertmodekeybindingsothermodeskeybindings)insertModeKeyBindings/otherModesKeyBindings

- Keybinding overrides to use for insert and other (non-insert) modes.

Bind ` jj ` to ` <Esc> ` in insert mode:

	  "vim.insertModeKeyBindings": [
	       {
	           "before": ["j", "j"],
	           "after": ["<Esc>"]
	       }
	  ]

Bind ` : ` to show the command palette:

	"vim.otherModesKeyBindingsNonRecursive": [
	   {
	       "before": [":"],
	       "after": [],
	       "commands": [
	           {
	               "command": "workbench.action.showCommands",
	               "args": []
	           }
	       ]
	   }
	]

Bind ` ZZ ` to save and close the current file:

	    "vim.otherModesKeyBindingsNonRecursive": [
	        {
	            "before": ["Z", "Z"],
	            "after": [],
	            "commands": [
	                {
	                    "command": "workbench.action.files.save",
	                    "args": []
	                },
	                {
	                    "command": "workbench.action.closeActiveEditor",
	                    "args": []
	                }
	            ]
	        }
	    ]

Or bind ` <leader>w ` to save the current file:

	    "vim.otherModesKeyBindingsNonRecursive": [
	        {
	            "before": ["leader", "w"],
	            "after": [],
	            "commands": [
	                {
	                    "command": "workbench.action.files.save",
	                    "args": []
	                }
	            ]
	        }
	    ]

#### [(L)](https://github.com/VSCodeVim/Vim#insertmodekeybindingsnonrecursiveothermodeskeybindingsnonrecursive)insertModeKeyBindingsNonRecursive/otherModesKeyBindingsNonRecursive

- Non-recursive keybinding overrides to use for insert and other (non-insert) modes (similar to ` :noremap `)
- *Example:* Bind ` j ` to ` gj `. Notice that if you attempted this binding normally, the j in gj would be expanded into gj, on and on forever. Stop this recursive expansion using insertModeKeyBindingsNonRecursive and/or otherModesKeyBindingNonRecursive.

	"vim.otherModesKeyBindingsNonRecursive": [
	{
	    "before": ["j"],
	    "after": ["g", "j"]
	}]

#### [(L)](https://github.com/VSCodeVim/Vim#startininsertmode)startInInsertMode

- Have VSCodeVim start in Insert Mode rather than Normal Mode.
- We would be remiss in our duties as Vim users not to say that you should really be staying in Normal mode as much as you can, but hey, who are we to stop you?

### [(L)](https://github.com/VSCodeVim/Vim#overridecopy)overrideCopy

- Override VSCode's copy command with our own, which works correctly with VSCodeVim.
- If cmd-c or ctrl-c is giving you issues, set this to false and complain at https://github.com/Microsoft/vscode/issues/217.
- Type: Boolean (Default: ` true `)

#### [(L)](https://github.com/VSCodeVim/Vim#usesystemclipboard)useSystemClipboard

- Enable yanking to the system clipboard by default
- Type: Boolean (Default: ` false `)
- Note: Linux users must have xclip installed

#### [(L)](https://github.com/VSCodeVim/Vim#searchhighlightcolor)searchHighlightColor

- Set the color of search highlights.
- Type: Color String (Default: ` rgba(150, 150, 150, 0.3) `)

#### [(L)](https://github.com/VSCodeVim/Vim#usesolidblockcursor)useSolidBlockCursor

- Use a non-blinking block cursor
- Type: Boolean (Default: ` false `)

### [(L)](https://github.com/VSCodeVim/Vim#vim-settings-we-support)Vim settings we support

#### [(L)](https://github.com/VSCodeVim/Vim#ignorecase)ignorecase

- Ignore case in search patterns
- Type: Boolean (Default: ` true `)

#### [(L)](https://github.com/VSCodeVim/Vim#smartcase)smartcase

- Override the 'ignorecase' option if the search pattern contains upper case characters
- Type: Boolean (Default: ` true `)

#### [(L)](https://github.com/VSCodeVim/Vim#hlsearch)hlsearch

- When there is a previous search pattern, highlight all its matches
- Type: Boolean (Default: ` false `)

#### [(L)](https://github.com/VSCodeVim/Vim#incsearch)incsearch

- Show the next search match while you're searching.
- Type: Boolean (Default: ` true `)

#### [(L)](https://github.com/VSCodeVim/Vim#autoindent)autoindent

- Copy indent from current line when starting a new line
- Type: Boolean (Default: ` true `)

#### [(L)](https://github.com/VSCodeVim/Vim#timeout)timeout

- Timeout in milliseconds for remapped commands
- Type: Number (Default: ` 1000 `)

#### [(L)](https://github.com/VSCodeVim/Vim#showcmd)showcmd

- Show the text of any command you are in the middle of writing.
- Type: Boolean (Default: ` true `)

#### [(L)](https://github.com/VSCodeVim/Vim#textwidth)textwidth

- Width to word-wrap to when using ` gq `.
- Type: number (Default: ` 80 `)

#### [(L)](https://github.com/VSCodeVim/Vim#leader)leader

- What key should ` <leader> ` map to in key remappings?
- Type: string (Default: ` \ `)

## [(L)](https://github.com/VSCodeVim/Vim#configure)Configure

Vim options are loaded in the following sequence:
1. ` :set {option} `
2. ` vim.{option} ` from user/workspace settings.
3. VSCode configuration
4. VSCodeVim default values

## [(L)](https://github.com/VSCodeVim/Vim#multi-cursor-mode)Multi-Cursor Mode

Multi-Cursor mode is currently in beta. Please report things you expected to work but didn't [to our feedback thread.](https://github.com/VSCodeVim/Vim/issues/824)

#### [(L)](https://github.com/VSCodeVim/Vim#getting-into-multi-cursor-mode)Getting into multi-cursor mode

You can enter multi-cursor mode by:

- Pressing cmd-d on OSX.
- Running "Add Cursor Above/Below" or the shortcut on any platform.
- Pressing ` gc `, a new shortcut we added which is equivalent to cmd-d on OSX or ctrl-d on Windows. (It adds another cursor at the next word that matches the word the cursor is currently on.)

#### [(L)](https://github.com/VSCodeVim/Vim#doing-stuff)Doing stuff

Now that you have multiple cursors, you should be able to use Vim commands as you see fit. Most of them should work. There is a list of things I know of which don't [here](https://github.com/VSCodeVim/Vim/pull/587). If you find yourself wanting one of these, please [add it to our feedback thread.](https://github.com/VSCodeVim/Vim/issues/824)

Each cursor has its own clipboard.

Pressing Escape in Multi-Cursor Visual Mode will bring you to Multi-Cursor Normal mode. Pressing it again will return you to Normal mode.

## [(L)](https://github.com/VSCodeVim/Vim#faq)F.A.Q.

#### [(L)](https://github.com/VSCodeVim/Vim#j-k-and-others-dont-repeat-when-i-hold-them-down)` j `, ` k ` and others don't repeat when I hold them down.

On OS X, open Terminal and run the following command:

defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false  # For VS Codedefaults write com.microsoft.VSCodeInsiders ApplePressAndHoldEnabled -bool false  # For VS Code Insider

#### [(L)](https://github.com/VSCodeVim/Vim#help-none-of-the-vim-ctrl-eg-ctrlf-ctrlv-commands-work)Help! None of the vim ` ctrl ` (e.g. ` ctrl+f `, ` ctrl+v `) commands work

Configure the ` useCtrlKeys ` option (see [configurations#useCtrlKeys](https://github.com/VSCodeVim/Vim#usectrlkeys)) to true.

#### [(L)](https://github.com/VSCodeVim/Vim#how-to-use-easymotion)How to use easymotion

Easymotion is based on [easymotion-vim](https://github.com/easymotion/vim-easymotion)To activate easymotion, you need to make sure that ` easymotion ` is set to ` true ` in settings.json. Now that easymotion is active, you can initiate motions using the following commands. Once you initiate the motion, text decorators will be displayed and you can press the keys displayed to jump to that position. ` leader ` is configurable and is ` \ ` by default.

If you set ` vim.easymotionChangeBackgroundColor = true ` you can use the searchHightlightColor as the background color for the text decorations, however you then lose the red/orange indicators on whether it is a one key or two key combination since the font color needs to stay readable.

Motion Command
Description
[object Object]
Search character
[object Object]
Find character forwards
[object Object]
Find character backwards
[object Object]
Til character forwards
[object Object]
Til character backwards
[object Object]
Start of word forwards
[object Object]
End of word forwards
[object Object]
End of word backwards
[object Object]
Start of word backwards

#### [(L)](https://github.com/VSCodeVim/Vim#how-to-use-surround)How to use surround

Surround plugin based on tpope's [surround.vim](https://github.com/tpope/vim-surround) plugin is used to work with surrounding characters like parenthesis, brackets, quotes, and XML tags.

t or < as or will do tags and enter tag entry mode.
Surround Command
Description
[object Object]
Delete existing surround
[object Object]
Change surround existing to desired
[object Object]
Surround something with something using motion (as in "you surround")
[object Object]
Surround when in visual modes (surrounds full selection)
Some examples:

- ` "test" ` with cursor inside quotes type cs"' to end up with ` 'test' `
- ` "test" ` with cursor inside quotes type ds" to end up with ` test `
- ` "test" ` with cursor inside quotes type cs"t and enter 123> to end up with ` <123>test</123> `
- ` test ` with cursor on word test type ysaw) to end up with ` (test) `

## [(L)](https://github.com/VSCodeVim/Vim#contributing)Contributing

This project is maintained by a group of awesome [people](https://github.com/VSCodeVim/Vim/graphs/contributors) and contributions are extremely welcome ❤️. For a quick tutorial on how you can help, see our [contributing guide](https://github.com/VSCodeVim/Vim/blob/master/.github/CONTRIBUTING.md).

## [(L)](https://github.com/VSCodeVim/Vim#awesome-features-you-might-not-know-about)Awesome Features You Might Not Know About

Vim has a lot of nooks and crannies. VSCodeVim preserves some of the coolest nooks and crannies of Vim. And then we add some of our own! Some of our favorite include:

- ` gd ` - jump to definition. *Astoundingly* useful in any language that VSCode provides definition support for. I use this one probably hundreds of times a day.
- ` gq ` on a visual selection - Reflow and wordwrap blocks of text, preserving commenting style. Great for formatting documentation comments.
- ` gc `, which adds another cursor on the next word it finds which is the same as the word under the cursor.
- ` af `, a command that I added in visual mode, which selects increasingly large blocks of text. e.g. if you had "blah (foo [bar 'ba|z'])" then it would select 'baz' first. If you pressed az again, it'd then select [bar 'baz'], and if you did it a third time it would select "(foo [bar 'baz'])".
- ` gh `, another custom VSCodeVim command. This one is equivalent to hovering your mouse over wherever the cursor is. Handy for seeing types and error messages without reaching for the mouse!

(The mnemonic: selecting blocks is fast af! 😉)

## [(L)](https://github.com/VSCodeVim/Vim#special-shoutouts-to-cool-contributors)Special Shoutouts to Cool Contributors

- Thanks to @xconverge for making over 100 commits to the repo. If you're wondering why your least favorite bug packed up and left, it was probably him.
- Thanks to @Metamist for implementing EasyMotion!
- Thanks to @sectioneight for implementing text objects!
- Special props to [Kevin Coleman](http://kevincoleman.io/), who created our awesome logo!

## [(L)](https://github.com/VSCodeVim/Vim#release-notes)Release Notes

Our recent releases and update notes are available [here](https://github.com/VSCodeVim/Vim/releases).