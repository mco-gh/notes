radovskyb/watcher: watcher is a Go package for watching for files or directory changes without using filesystem events.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='61'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='906' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#watcher)watcher

[![68747470733a2f2f7472617669732d63692e6f72672f7261646f76736b79622f776174636865722e7376673f6272616e63683d6d6173746572](../_resources/6e77b43080c94e06849fc7e456ad1329.png)](https://travis-ci.org/radovskyb/watcher)

`watcher` is a Go package for watching for files or directory changes (recursively or non recursively) without using filesystem events, which allows it to work cross platform consistently.

`watcher` watches for changes and notifies over channels either anytime an event or an error has occurred.

Events contain the `os.FileInfo` of the file or directory that the event is based on and the type of event and file or directory path.

[Installation](https://github.com/radovskyb/watcher#installation)
[Features](https://github.com/radovskyb/watcher#features)
[Example](https://github.com/radovskyb/watcher#example)
[Contributing](https://github.com/radovskyb/watcher#contributing)
[Watcher Command](https://github.com/radovskyb/watcher#command)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='62'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='916' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#update)Update

- Event.OldPath has been added [Aug 17, 2019]
- Added new file filter hooks (Including a built in regexp filtering hook) [Dec 12, 2018]
- Event.Path for Rename and Move events is now returned in the format of `fromPath -> toPath`

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='63'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='922' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#chmod-event-is-not-supported-under-windows)Chmod event is not supported under windows.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='923' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#installation)Installation

go get -u github.com/radovskyb/watcher/...

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='65'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='925' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#features)Features

- Customizable polling interval.
- Filter Events.
- Watch folders recursively or non-recursively.
- Choose to ignore hidden files.
- Choose to ignore specified files and folders.
- Notifies the `os.FileInfo` of the file that the event is based on. e.g `Name`, `ModTime`, `IsDir`, etc.
- Notifies the full path of the file that the event is based on or the old and new paths if the event was a `Rename` or `Move` event.
- Limit amount of events that can be received per watching cycle.
- List the files being watched.
- Trigger custom events.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='66'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='937' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#todo)Todo

- Write more tests.
- Write benchmarks.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='67'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='941' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#example)Example

package mainimport ("fmt""log""time""github.com/radovskyb/watcher")func  main() {w  := watcher.New()// SetMaxEvents to 1 to allow at most 1 event's to be received// on the Event channel per watching cycle.//// If SetMaxEvents is not set, the default is to send all events.w.SetMaxEvents(1)// Only notify rename and move events.w.FilterOps(watcher.Rename, watcher.Move)// Only files that match the regular expression during file listings// will be watched.r  := regexp.MustCompile("^abc$")

w.AddFilterHook(watcher.RegexFilterHook(r, false))go  func() {for {select {case  event  :=  <-w.Event:	fmt.Println(event) // Print the event's info.case  err  :=  <-w.Error:

log.Fatalln(err)case  <-w.Closed:return}
}
}()// Watch this folder for changes.if  err  := w.Add("."); err != nil {
log.Fatalln(err)

}// Watch test_folder recursively for changes.if  err  := w.AddRecursive("../test_folder"); err != nil {

log.Fatalln(err)

}// Print a list of all of the files and folders currently// being watched and their paths.for  path, f  :=  range w.WatchedFiles() {

fmt.Printf("%s: %s\n", path, f.Name())
}
fmt.Println()// Trigger 2 events after watcher started.go  func() {
w.Wait()
w.TriggerEvent(watcher.Create, nil)
w.TriggerEvent(watcher.Remove, nil)

}()// Start the watching process - it'll check for changes every 100ms.if  err  := w.Start(time.Millisecond * 100); err != nil {

log.Fatalln(err)
}
}

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1074' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#contributing)Contributing

If you would ike to contribute, simply submit a pull request.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='69'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1076' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#command)Command

`watcher` comes with a simple command which is installed when using the `go get` command from above.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='70'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1078' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/radovskyb/watcher#usage)Usage

	Usage of watcher:
	  -cmd string
	    	command to run when an event occurs
	  -dotfiles
	    	watch dot files (default true)
	  -ignore string
	        comma separated list of paths to ignore
	  -interval string
	    	watcher poll interval (default "100ms")
	  -keepalive
	    	keep alive when a cmd returns code != 0
	  -list
	    	list watched files on start
	  -pipe
	    	pipe event's info to command's stdin
	  -recursive
	    	watch folders recursively (default true)
	  -startcmd
	    	run the command when watcher starts

All of the flags are optional and watcher can also be called by itself:
watcher

(watches the current directory recursively for changes and notifies any events that occur.)

A more elaborate example using the `watcher` command:
watcher -dotfiles=false -recursive=false -cmd="./myscript" main.go ../

In this example, `watcher` will ignore dot files and folders and won't watch any of the specified folders recursively. It will also run the script `./myscript` anytime an event occurs while watching `main.go` or any files or folders in the previous directory (`../`).

Using the `pipe` and `cmd` flags together will send the event's info to the command's stdin when changes are detected.

First create a file called `script.py` with the following contents:
import sysfor line in sys.stdin:print (line +  " - python")
Next, start watcher with the `pipe` and `cmd` flags enabled:
watcher -cmd="python script.py" -pipe=true

Now when changes are detected, the event's info will be output from the running python script.