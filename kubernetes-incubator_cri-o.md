kubernetes-incubator/cri-o

[[cri-o logo](../_resources/cd14095f683599e39cf1b35bad9bfee0.bin)](https://camo.githubusercontent.com/2a1e5926e2bfebcfdf818bdabf39a08f053aa2f5/68747470733a2f2f63646e2e7261776769742e636f6d2f6b756265726e657465732d696e63756261746f722f6372692d6f2f6d61737465722f6c6f676f2f6372696f2d6c6f676f2e737667)

# [(L)](https://github.com/kubernetes-incubator/cri-o#cri-o---oci-based-implementation-of-kubernetes-container-runtime-interface)cri-o - OCI-based implementation of Kubernetes Container Runtime Interface

[[Build Status](../_resources/6cead764a62ad58f63a7e41a5c104243.bin)](https://travis-ci.org/kubernetes-incubator/cri-o)[[Go Report Card](../_resources/77d3f4c898af0d9d24d39ad81e118024.bin)](https://goreportcard.com/report/github.com/kubernetes-incubator/cri-o)

### [(L)](https://github.com/kubernetes-incubator/cri-o#status-pre-alpha)Status: pre-alpha

## [(L)](https://github.com/kubernetes-incubator/cri-o#what-is-the-scope-of-this-project)What is the scope of this project?

cri-o is meant to provide an integration path between OCI conformant runtimes and the kubelet. Specifically, it implements the Kubelet Container Runtime Interface (CRI) using OCI conformant runtimes. The scope of cri-o is tied to the scope of the CRI.

At a high level, we expect the scope of cri-o to be restricted to the following functionalities:

- Support multiple image formats including the existing Docker image format
- Support for multiple means to download images including trust & image verification
- Container image management (managing image layers, overlay filesystems, etc)
- Container process lifecycle management
- Monitoring and logging required to satisfy the CRI
- Resource isolation as required by the CRI

## [(L)](https://github.com/kubernetes-incubator/cri-o#what-is-not-in-scope-for-this-project)What is not in scope for this project?

- Building, signing and pushing images to various image storages
- A CLI utility for interacting with cri-o. Any CLIs built as part of this project are only meant for testing this project and there will be no guarantees on the backwards compatibility with it.

This is an implementation of the Kubernetes Container Runtime Interface (CRI) that will allow Kubernetes to directly launch and manage Open Container Initiative (OCI) containers.

The plan is to use OCI projects and best of breed libraries for different aspects:

- Runtime: [runc](https://github.com/opencontainers/runc) (or any OCI runtime-spec implementation) and [oci runtime tools](https://github.com/opencontainers/runtime-tools)
- Images: Image management using [containers/image](https://github.com/containers/image)
- Storage: Storage and management of image layers using [containers/storage](https://github.com/containers/storage)
- Networking: Networking support through use of [CNI](https://github.com/containernetworking/cni)

It is currently in active development in the Kubernetes community through the [design proposal](https://github.com/kubernetes/kubernetes/pull/26788). Questions and issues should be raised in the Kubernetes [sig-node Slack channel](https://kubernetes.slack.com/archives/sig-node).

## [(L)](https://github.com/kubernetes-incubator/cri-o#communication)Communication

For async communication and long running discussions please use issues and pull requests on the github repo. This will be the best place to discuss design and implementation.

For sync communication we have an IRC channel #cri-o, on chat.freenode.net, that everyone is welcome to join and chat about development.

## [(L)](https://github.com/kubernetes-incubator/cri-o#getting-started)Getting started

### [(L)](https://github.com/kubernetes-incubator/cri-o#prerequisites)Prerequisites

Latest verion of ` runc ` is expected to be installed on the system. It is picked up as the default runtime by crio.

### [(L)](https://github.com/kubernetes-incubator/cri-o#build-dependencies)Build Dependencies

**Required**
Fedora, CentOS, RHEL, and related distributions:
yum install -y \
btrfs-progs-devel \
device-mapper-devel \
glib2-devel \
glibc-devel \
glibc-static \
gpgme-devel \
libassuan-devel \
libgpg-error-devel \
libseccomp-devel \
libselinux-devel \
pkgconfig \
runc
Debian, Ubuntu, and related distributions:
apt install -y \
btrfs-tools \
libassuan-dev \
libdevmapper-dev \
libglib2.0-dev \
libc6-dev \
libgpgme11-dev \
libgpg-error-dev \
libseccomp-dev \
libselinux1-dev \
pkg-config \
runc

If using an older release or a long-term support release, be careful to double-check that the version of ` runc ` is new enough, or else build your own.

**Optional**
Fedora, CentOS, RHEL, and related distributions:
(no optional packages)
Debian, Ubuntu, and related distributions:
apt install -y \
libapparmor-dev

### [(L)](https://github.com/kubernetes-incubator/cri-o#get-source-code)Get Source Code

As with other Go projects, cri-o must be cloned into a directory structure like:

	GOPATH
	└── src
	    └── github.com
	        └── kubernetes-incubator
	            └── cri-o

First, configure a ` GOPATH ` (if you are using go1.8 or later, this defaults to ` ~/go `).

export GOPATH=~/go
mkdir -p $GOPATH
Next, clone the source code using:

mkdir -p $GOPATH/src/github.com/kubernetes-incubatorcd  $_  # or cd $GOPATH/src/github.com/kubernetes-incubatorgit clone https://github.com/kubernetes-incubator/cri-o # or your forkcd cri-o

### [(L)](https://github.com/kubernetes-incubator/cri-o#build)Build

make install.tools
make
sudo make install

Otherwise, if you do not want to build ` cri-o ` with seccomp support you can add ` BUILDTAGS="" ` when running make.

make BUILDTAGS=""sudo make install

#### [(L)](https://github.com/kubernetes-incubator/cri-o#build-tags)Build Tags

` cri-o ` supports optional build tags for compiling support of various features. To add build tags to the make option the ` BUILDTAGS ` variable must be set.

make BUILDTAGS='seccomp apparmor'

| Build Tag | Feature | Dependency |
| --- | --- | --- |
| seccomp | syscall filtering | libseccomp |
| selinux | selinux process and mount labeling | libselinux |
| apparmor | apparmor profile support | libapparmor |

### [(L)](https://github.com/kubernetes-incubator/cri-o#running-pods-and-containers)Running pods and containers

Follow this [tutorial](https://github.com/kubernetes-incubator/cri-o/blob/master/tutorial.md) to get started with CRI-O.

### [(L)](https://github.com/kubernetes-incubator/cri-o#setup-cni-networking)Setup CNI networking

A proper description of setting up CNI networking is given in the[` contrib/cni ` README](https://github.com/kubernetes-incubator/cri-o/blob/master/contrib/cni/README.md). But the gist is that you need to have some basic network configurations enabled and CNI plugins installed on your system.

### [(L)](https://github.com/kubernetes-incubator/cri-o#running-with-kubernetes)Running with kubernetes

You can run a local version of kubernetes with cri-o using ` local-up-cluster.sh `:

1. Clone the [kubernetes repository](https://github.com/kubernetes/kubernetes)
2. Start the cri-o daemon (` crio `)

3. From the kubernetes project directory, run: ` CONTAINER_RUNTIME=remote CONTAINER_RUNTIME_ENDPOINT='/var/run/crio.sock --runtime-request-timeout=15m' ./hack/local-up-cluster.sh `

To run a full cluster, see [the instructions](https://github.com/kubernetes-incubator/cri-o/blob/master/kubernetes.md).

### [(L)](https://github.com/kubernetes-incubator/cri-o#current-roadmap)Current Roadmap

1. Basic pod/container lifecycle, basic image pull (done)
2. Support for tty handling and state management (done)
3. Basic integration with kubelet once client side changes are ready (done)

4. Support for log management, networking integration using CNI, pluggable image/storage management (done)

5. Support for exec/attach (done)

6. Target fully automated kubernetes testing without failures [e2e status](https://github.com/kubernetes-incubator/cri-o/issues/533)

7. Release 1.0
8. Track upstream k8s releases