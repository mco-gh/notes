cknadler/vim-anywhere

# vim-anywhere

Sometimes, you edit text outside of Vim. These are sad times. Enter vim-anywhere!

[(L)](https://github.com/cknadler/vim-anywhere/blob/master/assets/demo.gif)

[![demo](../_resources/a95982098a7317ddabda02364479866c.gif)](https://github.com/cknadler/vim-anywhere/blob/master/assets/demo.gif)

Once [invoked](https://github.com/cknadler/vim-anywhere#keybinding), vim-anywhere will open a buffer. Close it and it's contents are copied to your **clipboard** and your previous application is refocused.

## Installation

#### Requirements

**OSX:**

- MacVim (`brew install macvim`)

**Linux:**

- Gnome (or a derivative)
- gVim

#### Install

curl -fsSL https://raw.github.com/cknadler/vim-anywhere/master/install | bash

**OSX caveat:** key binding is unbound by default. See [keybinding](https://github.com/cknadler/vim-anywhere#keybinding)for details.

#### Update

~/.vim-anywhere/update

#### Uninstall

~/.vim-anywhere/uninstall

## Keybinding

**OSX:** ( default = unbound, suggested = `ctrl+cmd+v` )

The keyboard shortcut for invoking vim-anywhere is unbound by default on OSX. The installation script will automatically open`System Preferences > Keyboard > Shortcuts`. Fill in the following:

[(L)](https://github.com/cknadler/vim-anywhere/blob/master/assets/shortcut.png)

[![keyboard shortcut](../_resources/0fb25970ae8d23e6934adc33736dd4ed.png)](https://github.com/cknadler/vim-anywhere/blob/master/assets/shortcut.png)

**Linux:** ( default = `ctrl+alt+v` )
*Gnome*

$ gconftool -t str --set /desktop/gnome/keybindings/vim-anywhere/binding <custom binding>

*I3WM*

$ bindsym $mod+Alt+v exec ~/.vim-anywhere/bin/run" >> ~/.i3/config # remember to reload your config after

## History

vim-anywhere creates a temporary file in `/tmp/vim-anywhere` when invoked. These files stick around until you restart your system, giving you a temporary history.

View your history:
$ ls /tmp/vim-anywhere
Reopen your most recent file:
$ vim $( ls /tmp/vim-anywhere | sort -r | head -n 1 )

## Why?

I use Vim for *almost* everything. I wish I didn't have to say *almost*. My usual workflow is to open Vim, write, copy the text out of my current buffer and paste it into whatever applicaiton I was just using. vim-anywhere attempts to automate this process as much as possible, reducing the friction of using Vim to do more than just edit code.

## Contributing

Love vim-anywhere? Hate it? Want to change it completely? Email me or open an issue and lets talk. Pull requests, suggestions and issues of any kind are welcome with open arms.

## License

MIT.