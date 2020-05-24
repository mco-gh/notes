benhoyt/goawk: GoAWK: an AWK interpreter written in Go

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='72'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1046' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/benhoyt/goawk#goawk-an-awk-interpreter-written-in-go)GoAWK: an AWK interpreter written in Go

[![68747470733a2f2f676f646f632e6f72672f6769746875622e636f6d2f62656e686f79742f676f61776b3f7374617475732e706e67](../_resources/c80fee96635ca5c9245a0ebcbf21bcf4.png)](https://godoc.org/github.com/benhoyt/goawk)[![68747470733a2f2f7472617669732d63692e6f72672f62656e686f79742f676f61776b2e737667](../_resources/6e77b43080c94e06849fc7e456ad1329.png)](https://travis-ci.org/benhoyt/goawk)[![68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f6769746875622f62656e686f79742f676f61776b3f6272616e63683d6d6173746572267376673d74727565](../_resources/c241c28aa0a0d4586acb5fd42799d37b.png)](https://ci.appveyor.com/project/benhoyt/goawk)

AWK is a fascinating text-processing language, and somehow after reading the delightfully-terse [*The AWK Programming Language*](https://ia802309.us.archive.org/25/items/pdfy-MgN0H1joIoDVoIC7/The_AWK_Programming_Language.pdf) I was inspired to write an interpreter for it in Go. So here it is, feature-complete and tested against "the one true AWK" test suite.

[**Read more about how GoAWK works and performs here.**](https://benhoyt.com/writings/goawk/)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='73'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1052' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/benhoyt/goawk#basic-usage)Basic usage

To use the command-line version, simply use `go get` to install it, and then run it using `goawk` (assuming `$GOPATH/bin` is in your `PATH`):

$ go get github.com/benhoyt/goawk
$ goawk 'BEGIN { print "foo", 42 }'foo 42
$ echo 1 2 3 | goawk '{ print $1 + $3 }'4

On Windows, `"` is the shell quoting character, so use `"` around the entire AWK program on the command line, and use `'` around AWK strings -- this is a non-POSIX extension to make GoAWK easier to use on Windows:

C:\> goawk "BEGIN { print 'foo', 42 }"foo 42

To use it in your Go programs, you can call `interp.Exec()` directly for simple needs:

input  := bytes.NewReader([]byte("foo bar\n\nbaz buz"))err  := interp.Exec("$0 { print $1 }", "  ", input, nil)if err != nil {

fmt.Println(err) return}// Output:// foo// baz

Or you can use the `parser` module and then `interp.ExecProgram()` to control execution, set variables, etc:

src  :=  "{ print NR, tolower($0) }"input  :=  "A\naB\nAbC"prog, err  := parser.ParseProgram([]byte(src), nil)if err != nil {

fmt.Println(err) return}config  := &interp.Config{ Stdin: bytes.NewReader([]byte(input)), Vars: []string{"OFS", ":"},

}
_, err = interp.ExecProgram(prog, config)if err != nil {
fmt.Println(err) return}// Output:// 1:a// 2:ab// 3:abc

Read the [GoDoc documentation](https://godoc.org/github.com/benhoyt/goawk) for more details.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='74'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1153' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/benhoyt/goawk#differences-from-awk)Differences from AWK

The intention is for GoAWK to conform to `awk`'s behavior and to the [POSIX AWK spec](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html), but this section describes some areas where it's different.

Additional features GoAWK has over AWK:

- It's embeddable in your Go programs! You can even call custom Go functions from your AWK scripts.
- I/O-bound AWK scripts (which is most of them) are significantly faster than `awk`, and on a par with `gawk` and `mawk`.
- The parser supports `'single-quoted strings'` in addition to `"double-quoted strings"`, primarily to make Windows one-liners easier (the Windows `cmd.exe` shell uses `"` as the quote character).

Things AWK has over GoAWK:

- CPU-bound AWK scripts are slightly slower than `awk`, and about twice as slow as `gawk` and `mawk`.
- AWK is written by Brian Kernighan.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='75'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1165' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/benhoyt/goawk#stability)Stability

This project has a good suite of tests, and I've used it a bunch personally, but it's certainly not battle-tested or heavily used, so please use at your own risk. I intend not to change the Go API in a breaking way.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1168' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/benhoyt/goawk#license)License

GoAWK is licensed under an open source [MIT license](https://github.com/benhoyt/goawk/blob/master/LICENSE.txt).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='77'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1171' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/benhoyt/goawk#the-end)The end

Have fun, and please [contact me](https://benhoyt.com/) if you're using GoAWK or have any feedback!