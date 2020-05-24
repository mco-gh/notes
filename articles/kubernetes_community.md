kubernetes/community

###    README.md

# [(L)](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel#kubernetes-developer-guide)Kubernetes Developer Guide

The developer guide is for anyone wanting to either write code which directly accesses the Kubernetes API, or to contribute directly to the Kubernetes project. It assumes some familiarity with concepts in the [User Guide](http://kubernetes.io/docs/user-guide/) and the [Cluster Admin Guide](http://kubernetes.io/docs/admin/).

## [(L)](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel#the-process-of-developing-and-contributing-code-to-the-kubernetes-project)The process of developing and contributing code to the Kubernetes project

- **On Collaborative Development** ([collab.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/collab.md)): Info on pull requests and code reviews.
- **GitHub Issues** ([issues.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/issues.md)): How incoming issues are reviewed and prioritized.
- **Pull Request Process** ([pull-requests.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/pull-requests.md)): When and why pull requests are closed.
- **Kubernetes On-Call Rotations** ([on-call-rotations.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/on-call-rotations.md)): Descriptions of on-call rotations for build and end-user support.
- **Faster PR reviews** ([faster_reviews.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/faster_reviews.md)): How to get faster PR reviews.
- **Getting Recent Builds** ([getting-builds.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/getting-builds.md)): How to get recent builds including the latest builds that pass CI.
- **Automated Tools** ([automation.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/automation.md)): Descriptions of the automation that is running on our github repository.

## [(L)](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel#setting-up-your-dev-environment-coding-and-debugging)Setting up your dev environment, coding, and debugging

- **Development Guide** ([development.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/development.md)): Setting up your development environment.
- **Hunting flaky tests** ([flaky-tests.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/flaky-tests.md)): We have a goal of 99.9% flake free tests. Here's how to run your tests many times.
- **Logging Conventions** ([logging.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/logging.md)): Glog levels.
- **Profiling Kubernetes** ([profiling.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/profiling.md)): How to plug in go pprof profiler to Kubernetes.
- **Instrumenting Kubernetes with a new metric**([instrumentation.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/instrumentation.md)): How to add a new metrics to the Kubernetes code base.
- **Coding Conventions** ([coding-conventions.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/coding-conventions.md)): Coding style advice for contributors.
- **Document Conventions** ([how-to-doc.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/how-to-doc.md)) Document style advice for contributors.
- **Running a cluster locally** ([running-locally.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/running-locally.md)): A fast and lightweight local cluster deployment for development.

## [(L)](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel#developing-against-the-kubernetes-api)Developing against the Kubernetes API

- The [REST API documentation](http://kubernetes.io/docs/reference/) explains the REST API exposed by apiserver.
- **Annotations** ([Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)): are for attaching arbitrary non-identifying metadata to objects. Programs that automate Kubernetes objects may use annotations to store small amounts of their state.
- **API Conventions** ([api-conventions.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/api-conventions.md)): Defining the verbs and resources used in the Kubernetes API.
- **API Client Libraries** ([client-libraries.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/client-libraries.md)): A list of existing client libraries, both supported and user-contributed.

## [(L)](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel#writing-plugins)Writing plugins

- **Authentication** ([Authentication](http://kubernetes.io/docs/admin/authentication/)): The current and planned states of authentication tokens.
- **Authorization Plugins** ([Authorization](http://kubernetes.github.io/docs/admin/authorization/)): Authorization applies to all HTTP requests on the main apiserver port. This doc explains the available authorization implementations.
- **Admission Control Plugins** ([admission_control](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/admission_control.md))

## [(L)](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel#building-releases)Building releases

See the [kubernetes/release](https://github.com/kubernetes/release) repository for details on creating releases and related tools and helper scripts.

[![Analytics](../_resources/c2196de8ba412c60c22ab491af7b1409.gif)](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel)