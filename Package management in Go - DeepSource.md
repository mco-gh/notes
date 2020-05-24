Package management in Go - DeepSource

# Package management in Go

## Brief overview of package management in Go — pre and post Go modules

 [Insights](https://deepsource.io/blog/category/insights)  [Go](https://deepsource.io/blog/category/go)

 ![](../_resources/f4a7b91f92327cd10f0f09c295fd06cc.png)

 By Jai on August 26, 2019

 [![](../_resources/c2722534567085c1afe2c25bfc1a4d1b.png)](https://twitter.com/intent/tweet?text=Package+management+in+Go+%7C+DeepSource+Blog&url=https%3A%2F%2Fdeepsource.io%2Fblog%2Fgo-modules%2F&via=DeepSourceHQ)  [![](../_resources/f1f9279d680a0a70a85d89fe8504ea65.png)](https://www.linkedin.com/shareArticle?mini=true&source=DeepSource&summary=Brief+overview+of+package+management+in+Go+%E2%80%94+pre+and+post+Go+modules&url=https%3A%2F%2Fdeepsource.io%2Fblog%2Fgo-modules%2F)

Package management is one of the things Go has always missed. One of the major drawbacks of the previous (pre 1.11) `go get` was lack of support for managing dependency versions and enabling reproducible builds. The community has developed package managers and tools like Glide, dep and [many others](https://github.com/golang/go/wiki/PackageManagementTools) serving as de-facto solutions for versioning dependencies.

> “I use go get for production builds.” — said no one ever.

Go’s implementation of package management traces its origins back to Google (which has a giant monolithic repository for all their source code). Let’s break down on what’s wrong with ‘pre - go module’ package management tooling.

1. Versioning dependencies
2. Vendoring dependencies
3. The necessity of `GOPATH`

## Versioning dependencies

`go get` by default didn’t support module versioning. The idea behind the first version of go’s package management was — no need for module versioning, no need for 3rd-party module repositories, you build everything from your current branch.

Pre Go 1.11, adding a dependency meant cloning that dependency’s source code repo in your `GOPATH`. That was about it. There was no concept of versions. Rather, it always pointed to the current master branch at the time of cloning. Another major issue cropped up when different projects needed different versions of a dependency — which wasn’t possible either.

## Vendoring dependencies

Package vendoring is commonly referred to as the case where dependent packages are stored in the same place as your project. That usually means your dependencies are checked into your source management system, such as Git.

Consider this case — A uses dependency B, which uses a feature of dependency C introduced in version 1.5 of C, B must be able to ensure that A’s build uses C 1.5 or later. Pre Go 1.5, there was no mechanism for carrying dependency code alongside commands without rewriting import paths.

## Necessity of `GOPATH`

`GOPATH` exists for two main reasons:

1. In Go, the `import` declaration references a package via its fully qualified import path. `GOPATH` exist so that from any directory inside `GOPATH/src` the go tool can compute the absolute import path of the package in question.

2. A location to store dependencies fetched by `go get.`
What’s wrong with this?

1. `GOPATH` doesn’t allow checking out the source of a project in a directory of choice like they are used to with other languages.

2. Additionally, `GOPATH` does not let the developer have more than one copy of a project (or its dependencies) checked out at the same time.

## Introducing Go Modules

Go 1.11 introduces preliminary support for Go modules. From Go Wiki,

> A *> module*>  is a collection of related Go packages that are versioned together as a single unit. Modules record precise dependency requirements and create reproducible builds.

Go modules brings three important features built-in,
1) `go.mod` file similar to `package.json` or `Pipfile`.
2) A machine-generated transitive dependency description - `go.sum`.
3) No more `GOPATH` limitation. Modules can be in any path.

	$ go help mod
	Go mod provides access to operations on modules.

	Note that support for modules is built into all the go commands,
	not just 'go mod'. For example, day-to-day adding, removing, upgrading,
	and downgrading of dependencies should be done using 'go get'.
	See 'go help modules' for an overview of module functionality.

	Usage:

		go mod <command> [arguments]

	The commands are:

		download    download modules to local cache
		edit        edit go.mod from tools or scripts
		graph       print module requirement graph
		init        initialize new module in current directory
		tidy        add missing and remove unused modules
		vendor      make vendored copy of dependencies
		verify      verify dependencies have expected content
		why         explain why packages or modules are needed

	Use "go help mod <command>" for more information about a command.

Relevant [discussion thread](https://groups.google.com/forum/#!topic/golang-dev/a5PqQuBljF4).

## Migrating to Go Modules

To use Go modules, update Go to version `>= 1.11`. Since `GOPATH` is going away, one can activate module support in one of these two ways:

- Invoke the `go` command in a directory outside of the `GOPATH/src` tree, with a valid `go.mod` file in the current directory.
- Go modules don’t work if source is under `GOPATH`. To override this behaviour, invoke the `go` command with `GO111MODULE=on` environment variable set.

Let’s start porting by following these simple steps:

- As `GOPATH` isn’t necessary anymore, move the module out of `GOPATH`.
- From the project root, create the initial module definition - `go mod init github.com/username/repository`. The best part is, `go mod` automatically converts dependencies from existing package managers like `dep`, `Gopkg`, `glide` and [six others](https://tip.golang.org/pkg/cmd/go/internal/modconv/?m=all#pkg-variables). This will create a file called `go.mod` with the module name and dependencies with its versions.

	$ cat go.mod
	module github.com/deepsourcelabs/cli

	go 1.12

	require (
		github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e
		github.com/getsentry/raven-go v0.2.0
		github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9

- Run `go build` to create a `go.sum` file which contains the expected cryptographic checksums of the content of specific module versions. This is to ensure that future downloads of these modules retrieve the same bits as the first download. Note that go.sum is not a lock file.

	$ cat go.sum
	github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e h1:9574pc8MX6rF/QyO14SPHhM5KKIOo9fkb/1ifuYMTKU=
	github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e/go.mod h1:GJKEexRPVJrBSOjoqN5VNOIKJ5Q3RViH6eu3puDRwx4=
	github.com/getsentry/raven-go v0.2.0 h1:no+xWJRb5ZI7eE8TWgIq1jLulQiIoLG0IfYxv5JYMGs=
	github.com/getsentry/raven-go v0.2.0/go.mod h1:KungGk8q33+aIAZUIVWZDr2OfAEBsO49PX4NzFV5kcQ=
	github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9 h1:dIsTcVF0w9viTLHXUEkDI7cXITMe+M/MRRM2MwisVow=
	github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=

> Note on versioning: To maintain backward compatibility, if the module is version v2 or higher, the major version of the module *> must*>  be included as a `/vN`>  at the end of the module paths used in `go.mod`> files (e.g., `module github.com/username/repository/v2`

## Everyday commands

### List dependencies

`go list -m all` lists the current module and all its dependencies.

	$ go list -m all
	github.com/deepsourcelabs/cli
	github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e
	github.com/getsentry/raven-go v0.2.0
	github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9

> In the `go list`>  output, the current module, also known as the *> main module*> , is always the first line, followed by dependencies sorted by module path.

### List available versions of a package

`go list -m -versions github.com/username/repository` lists available versions of a package.

	$ go list -m -versions github.com/getsentry/raven-go
	github.com/getsentry/raven-go v0.1.0 v0.1.1 v0.1.2 v0.2.0

### Add a dependency

Adding a dependency is implicit. After importing a dependency in code, running `go build` or `go test` command gets the latest version of the module and adds it to `go.mod` file. If you would like to add a dependency explicitly, run`go get github.com/username/repository`.

### Upgrade/downgrade a dependency

`go get github.com/username/repository@vx.x.x` downloads and sets the specific version of the dependency and updates `go.mod` file.

	$ go get github.com/getsentry/raven-go@v0.1.2
	go: finding github.com/getsentry/raven-go v0.1.2
	go: downloading github.com/getsentry/raven-go v0.1.2
	go: extracting github.com/getsentry/raven-go v0.1.2
	$ cat go.mod
	module github.com/deepsourcelabs/marvin-go

	go 1.12

	require (
		github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e
		github.com/getsentry/raven-go v0.1.2
		github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9
	)
	$ cat go.sum
	github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e h1:9574pc8MX6rF/QyO14SPHhM5KKIOo9fkb/1ifuYMTKU=
	github.com/certifi/gocertifi v0.0.0-20190410005359-59a85de7f35e/go.mod h1:GJKEexRPVJrBSOjoqN5VNOIKJ5Q3RViH6eu3puDRwx4=
	github.com/getsentry/raven-go v0.1.2 h1:4V0z512S5mZXiBvmW2RbuZBSIY1sEdMNsPjpx2zwtSE=
	github.com/getsentry/raven-go v0.1.2/go.mod h1:KungGk8q33+aIAZUIVWZDr2OfAEBsO49PX4NzFV5kcQ=
	github.com/getsentry/raven-go v0.2.0 h1:no+xWJRb5ZI7eE8TWgIq1jLulQiIoLG0IfYxv5JYMGs=
	github.com/getsentry/raven-go v0.2.0/go.mod h1:KungGk8q33+aIAZUIVWZDr2OfAEBsO49PX4NzFV5kcQ=
	github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9 h1:dIsTcVF0w9viTLHXUEkDI7cXITMe+M/MRRM2MwisVow=
	github.com/pkg/errors v0.0.0-20190227000051-27936f6d90f9/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=

### Vendoring dependencies

When using modules, the go command completely ignores vendor directories. For backward compatibility with older versions of Go, or to ensure that all files used for a build are stored together in a single file tree, run`go mod vendor`.

This creates a directory named `vendor` in the root directory of the main module and stores all the packages from dependency modules there.

> Note: To build using the main module’s top-level vendor directory, run ‘go build -mod=vendor’.

### Remove unused dependencies

`go mod tidy` trims unused dependencies and updates `go.mod` file.

## FAQs

#### Is `GOPATH` not needed anymore?

No. Farewell `GOPATH`.

#### Which version is pulled by default?

The go.mod file and the go command more generally use semantic versions as the standard form for describing module versions, so that versions can be compared to determine which should be considered earlier or later than another. A module version like `v1.2.3` is introduced by tagging a revision in the underlying source repository. Untagged revisions can be referred to using a “pseudo-version” like `v0.0.0-yyyymmddhhmmss-abcdefabcdef`, where the time is the commit time in UTC and the final suffix is the prefix of the commit hash.

#### Should `go.sum` be checked into version control?

Yes.

#  Want to keep your Go code healthy?

###  DeepSource flags 120+ types of issues in your Go code.

 [Create account](https://deepsource.io/signup/?utm_source=blog&utm_medium=post_cta)  [or contact sales](https://deepsource.io/schedule-demo/?utm_source=blog&utm_medium=post_cta)