dylanaraps/pywal

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='146'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='695' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/dylanaraps/pywal/wiki/Getting-Started#table-of-contents)Table of Contents

- [How to use `wal`](https://github.com/dylanaraps/pywal/wiki/Getting-Started#how-to-use-wal)
- [Applying the theme to new terminals](https://github.com/dylanaraps/pywal/wiki/Getting-Started#applying-the-theme-to-new-terminals)
- [Making the colorscheme persist on reboot](https://github.com/dylanaraps/pywal/wiki/Getting-Started#making-the-colorscheme-persist-on-reboot)
- [Using a custom wallpaper setter](https://github.com/dylanaraps/pywal/wiki/Getting-Started#using-a-custom-wallpaper-setter)
- [Further Reading: --> Customization](https://github.com/dylanaraps/pywal/wiki/Customization)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='147'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='703' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/dylanaraps/pywal/wiki/Getting-Started#how-to-use-wal)How to use `wal`

Run `wal` and point it to either a directory (`wal -i "path/to/dir"`) or an image (`wal -i "/path/to/img.jpg"`) and that's all. `wal` will change your wallpaper for you and also set your terminal colors.

usage: wal [-h] [-a "alpha"] [-b background] [-c] [-i "/path/to/img.jpg"]
[-f "/path/to/colorscheme/file"] [-n] [-o "script_name"] [-q] [-r]
[-R] [-s] [-t] [-v] [-e]
wal - Generate colorschemes on the fly
optional arguments:

-h, --help show this help message and exit -a "alpha" Set terminal background transparency. *Only works in URxvt* -b background Custom background color to use.

-c Delete all cached colorschemes.
-i "/path/to/img.jpg" Which image or directory to use.
-f "/path/to/colorscheme/file" Which colorscheme file to use.
-n Skip setting the wallpaper.
-o "script_name" External script to run after "wal".
-q Quiet mode, don't print anything and don't display
notifications.
-r Deprecated: Use (cat ~/.cache/wal/sequences &)
instead.
-R Restore previous colorscheme.
-s Skip changing colors in terminals.
-t Skip changing colors in ttys.
-v Print "wal" version.
-e Skip reloading gtk/xrdb/i3/sway/polybar

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='148'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='707' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/dylanaraps/pywal/wiki/Getting-Started#applying-the-theme-to-new-terminals)Applying the theme to new terminals

`wal` only applies the new colors to the currently open terminals. Any new terminal windows you open won't use the new theme unless you add a single line to your shell's start up file.

Add this line to your shell startup file. (`.bashrc`, `.zshrc`, `.mkshrc` etc.)

# Import colorscheme from 'wal' asynchronously# & # Run the process in the background.# ( ) # Hide shell job control messages.(cat ~/.cache/wal/sequences &)# Alternative (blocks terminal for 0-3ms)cat ~/.cache/wal/sequences# To add support for TTYs this line can be optionally added.source  ~/.cache/wal/colors-tty.sh

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='149'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='712' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/dylanaraps/pywal/wiki/Getting-Started#making-the-colorscheme-persist-on-reboot)Making the colorscheme persist on reboot

On reboot your new colorscheme won't be set or in use. To fix this you have to add a line to your `.xinitrc` or whatever file starts programs on your system. This `wal` command will set your wallpaper to the wallpaper that was set last boot and also apply the colorscheme again.

Without this you'll be themeless until you run `wal` again.

# Add this to your .xinitrc or whatever file starts programs on startup.# -R restores the last colorscheme that was in use.wal -R

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='150'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='717' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/dylanaraps/pywal/wiki/Getting-Started#using-a-custom-wallpaper-setter)Using a custom wallpaper setter

`wal` will detect which wallpaper setter you have installed and use it with the `fill` mode to set the wallpaper. If you'd like to override this and use either your own setter, a different mode or some different commandline flags you can do the following:

# -n tells `wal` to skip setting the wallpaper.wal -i img.jpg -n# Using feh to tile the wallpaper now.# We grab the wallpaper location from wal's cache so # that this works even when a directory is passed.feh --bg-tile "$(<  "${HOME}/.cache/wal/wal")"  # You can create a function for this in your shellrc (.bashrc, .zshrc).wal-tile() {

wal -n -i "$@" feh --bg-tile "$(<  "${HOME}/.cache/wal/wal")"}# Usage:wal-tile "~/Pictures/wall.jpg"wal-tile "~/Pictures/tiles"