kubernetes/helm

###    README.md

# [(L)](https://github.com/kubernetes/helm#kubernetes-helm)Kubernetes Helm

[[CircleCI](../_resources/c20090eb7d0fdaaf86420df402bcf48f.bin)](https://circleci.com/gh/kubernetes/helm)[[Go Report Card](../_resources/6ac4d9948bd755f8116f3a3192a36819.bin)](https://goreportcard.com/report/github.com/kubernetes/helm)

Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

Use Helm to...

- Find and use [popular software packaged as Kubernetes charts](https://github.com/kubernetes/charts)
- Share your own applications as Kubernetes charts
- Create reproducible builds of your Kubernetes applications
- Intelligently manage your Kubernetes manifest files
- Manage releases of Helm packages

## [(L)](https://github.com/kubernetes/helm#helm-in-a-handbasket)Helm in a Handbasket

Helm is a tool that streamlines installing and managing Kubernetes applications. Think of it like apt/yum/homebrew for Kubernetes.

- Helm has two parts: a client (` helm `) and a server (` tiller `)
- Tiller runs inside of your Kubernetes cluster, and manages releases (installations) of your charts.
- Helm runs on your laptop, CI/CD, or wherever you want it to run.
- Charts are Helm packages that contain at least two things:
    - A description of the package (` Chart.yaml `)
    - One or more templates, which contain Kubernetes manifest files
- Charts can be stored on disk, or fetched from remote chart repositories (like Debian or RedHat packages)

## [(L)](https://github.com/kubernetes/helm#install)Install

Binary downloads of the Helm client can be found at the following links:

- [OSX](https://kubernetes-helm.storage.googleapis.com/helm-v2.4.1-darwin-amd64.tar.gz)
- [Linux](https://kubernetes-helm.storage.googleapis.com/helm-v2.4.1-linux-amd64.tar.gz)
- [Linux 32-bit](https://kubernetes-helm.storage.googleapis.com/helm-v2.4.1-linux-386.tar.gz)

Unpack the ` helm ` binary and add it to your PATH and you are good to go! macOS/[homebrew](https://brew.sh/) users can also use ` brew install kubernetes-helm `.

To rapidly get Helm up and running, start with the [Quick Start Guide](https://github.com/kubernetes/helm/blob/master/docs/quickstart.md).

See the [installation guide](https://github.com/kubernetes/helm/blob/master/docs/install.md) for more options, including installing pre-releases.

## [(L)](https://github.com/kubernetes/helm#docs)Docs

Get started with the [Quick Start guide](https://github.com/kubernetes/helm/blob/master/docs/quickstart.md) or plunge into the [complete documentation](https://github.com/kubernetes/helm/blob/master/docs/index.md)

## [(L)](https://github.com/kubernetes/helm#roadmap)Roadmap

The [Helm roadmap is currently located on the wiki](https://github.com/kubernetes/helm/wiki/Roadmap).

## [(L)](https://github.com/kubernetes/helm#community-discussion-contribution-and-support)Community, discussion, contribution, and support

You can reach the Helm community and developers via the following channels:

- [Kubernetes Slack](https://slack.k8s.io/):
    - #helm-users
    - #helm-dev
- Mailing List: https://groups.google.com/forum/#!forum/kubernetes-sig-apps
- Developer Call: Thursdays at 9:30-10:00 Pacific. https://zoom.us/j/4526666954

### [(L)](https://github.com/kubernetes/helm#code-of-conduct)Code of conduct

Participation in the Kubernetes community is governed by the [Kubernetes Code of Conduct](https://github.com/kubernetes/helm/blob/master/code-of-conduct.md).