didrocks/codelab-ubuntu-tools

# Codelabs command line tool

The program takes an input in form of a resource location, which can either be a Google Doc ID, local file path or an arbitrary URL. It then converts the input into a codelab format, HTML by default.

For more info run `claat help`.

## Install

The easiest way is to download pre-compiled binary. The binaries are available at

	https://claat.storage.googleapis.com/claat-darwin-amd64
	https://claat.storage.googleapis.com/claat-linux-386
	https://claat.storage.googleapis.com/claat-linux-amd64
	https://claat.storage.googleapis.com/claat-windows-386.exe
	https://claat.storage.googleapis.com/claat-windows-amd64.exe

Alternatively, if you have Go installed and `GOPATH` set properly:

	go get github.com/didrocks/codelab-ubuntu-tools/claat

If none of the above works, compile the tool from source following Dev workflow instructions below.

## Dev workflow

**Prerequisites**
1. Install [Go](https://golang.org/dl/) if you don't have it.

2. Make sure this directory is placed under`$GOPATH/src/github.com/didrocks/codelab-ubuntu-tools`.

3. Install package dependencies with `go get ./...` from this directory.

To build the binary run `make` or `make bin/claat`. The latter creates the target binary, while the former will also copy it to `$GOPATH/bin`.

Testing is done with `make test` or `go test ./...` if preferred.
Don't forget to run `make lint` or `golint ./...` before creating a new CL.

To create cross-compiled versions for all supported OS/Arch, run `make release`. It will place the output in `bin/claat-<os>-<arch>`.