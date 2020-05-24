wercker/stern

###    README.md

# [(L)](https://github.com/wercker/stern#stern)stern

[[wercker status](../_resources/21ef235be1e94d7f6282b9d44096e74e.bin)](https://app.wercker.com/project/byKey/fb1ed340ffed75c22dc301c38ab0893c)

Stern allows you to ` tail ` multiple pods on Kubernetes and multiple containers within the pod. Each result is color coded for quicker debugging.

The query is a regular expression so the pod name can easily be filtered and you don't need to specify the exact id (for instance omitting the deployment id). If a pod is deleted it gets removed from tail and if a new is added it automatically gets tailed.

When a pod contains multiple containers Stern can tail all of them too without having to do this manually for each one. Simply specify the ` container ` flag to limit what containers to show. By default all containers are listened to.

## [(L)](https://github.com/wercker/stern#installation)Installation

If you don't want to build from source go grab a [binary release](https://github.com/wercker/stern/releases)

[Govendor](https://github.com/kardianos/govendor) is required to install vendored dependencies.

	mkdir -p $GOPATH/src/github.com/wercker
	cd $GOPATH/src/github.com/wercker
	git clone git@github.com:wercker/stern.git && cd stern
	govendor sync
	go install

## [(L)](https://github.com/wercker/stern#usage)Usage

	stern pod-query [flags]

The ` pod ` query is a regular expression so you could provide ` "web-\w" ` to tail` web-backend ` and ` web-frontend ` pods but not ` web-123 `.

### [(L)](https://github.com/wercker/stern#cli-flags)cli flags

flag
default
purpose
[object Object]
[object Object]
Container name when multiple containers in pod (regular expression)
[object Object]

Print timestamps
[object Object]

Return logs newer than a relative duration like 52, 2m, or 3h. Displays all if omitted

[object Object]

Kubernetes context to use. Default to [object Object]
[object Object]

Log lines to exclude; specify multiple with additional [object Object]; (regular expression)

[object Object]

Kubernetes namespace to use. Default to namespace configured in Kubernetes context

[object Object]
[object Object]
Path to kubeconfig file to use
[object Object]

If present, tail across all namespaces. A specific namespace is ignored even if specified with --namespace.

[object Object]

Selector (label query) to filter on. If present, default to [object Object] for the pod-query.

[object Object]
[object Object]

The number of lines from the end of the logs to show. Defaults to -1, showing all logs.

[object Object]
[object Object]

Force set color output. [object Object]: colorize if tty attached, [object Object]: always colorize, [object Object]: never colorize

See ` stern --help ` for details

## [(L)](https://github.com/wercker/stern#examples)Examples:

Tail the ` gateway ` container running inside of the ` envvars ` pod on staging

	stern envvars --context staging --container gateway

Show auth activity from 15min ago with timestamps

	stern auth -t --since 15m

Follow the development of ` some-new-feature ` in minikube

	stern some-new-feature --context minikube

View pods from another namespace

	stern kubernetes-dashboard --namespace kube-system

Tail the pods filtered by ` run=nginx ` label selector across all namespaces

	stern --all-namespaces -l run=nginx

Follow the ` frontend ` pods in canary release

	stern frontend --selector release=canary

## [(L)](https://github.com/wercker/stern#completion)Completion

Stern supports command-line auto completion for bash or zsh. ` stern --completion=(bash|zsh) ` outputs the shell completion code which work by being evaluated in ` .bashrc `, etc for the specified shell.

If you use bash, stern bash completion code depends on the [bash-completion](https://github.com/scop/bash-completion). On the macOS, you can install it with homebrew as follows:

	$ brew install bash-completion

Note that bash-completion must be sourced before sourcing the stern bash completion code in ` .bashrc `.

source  <(brew --prefix)/etc/bash-completionsource  <(stern --completion=bash)
If you use zsh, just source the stern zsh completion code in ` .zshrc `.
source  <(stern --completion=zsh)