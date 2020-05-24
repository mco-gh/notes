The Twelve-Factor App

# [The Twelve-Factor App](https://12factor.net/)

# Introduction

In the modern era, software is commonly delivered as a service: called *web apps*, or *software-as-a-service*. The twelve-factor app is a methodology for building software-as-a-service apps that:

- Use **declarative** formats for setup automation, to minimize time and cost for new developers joining the project;
- Have a **clean contract** with the underlying operating system, offering **maximum portability** between execution environments;
- Are suitable for **deployment** on modern **cloud platforms**, obviating the need for servers and systems administration;
- **Minimize divergence** between development and production, enabling **continuous deployment** for maximum agility;
- And can **scale up** without significant changes to tooling, architecture, or development practices.

The twelve-factor methodology can be applied to apps written in any programming language, and which use any combination of backing services (database, queue, memory cache, etc).

# Background

The contributors to this document have been directly involved in the development and deployment of hundreds of apps, and indirectly witnessed the development, operation, and scaling of hundreds of thousands of apps via our work on the [Heroku](http://www.heroku.com/) platform.

This document synthesizes all of our experience and observations on a wide variety of software-as-a-service apps in the wild. It is a triangulation on ideal practices for app development, paying particular attention to the dynamics of the organic growth of an app over time, the dynamics of collaboration between developers working on the app’s codebase, and [avoiding the cost of software erosion](http://blog.heroku.com/archives/2011/6/28/the_new_heroku_4_erosion_resistance_explicit_contracts/).

Our motivation is to raise awareness of some systemic problems we’ve seen in modern application development, to provide a shared vocabulary for discussing those problems, and to offer a set of broad conceptual solutions to those problems with accompanying terminology. The format is inspired by Martin Fowler’s books *[Patterns of Enterprise Application Architecture](https://books.google.com/books/about/Patterns_of_enterprise_application_archi.html?id=FyWZt5DdvFkC)* and *[Refactoring](https://books.google.com/books/about/Refactoring.html?id=1MsETFPD3I0C)*.

# Who should read this document?

Any developer building applications which run as a service. Ops engineers who deploy or manage such applications.

# The Twelve Factors

## [I. Codebase](https://12factor.net/codebase)

### One codebase tracked in revision control, many deploys

## [II. Dependencies](https://12factor.net/dependencies)

### Explicitly declare and isolate dependencies

## [III. Config](https://12factor.net/config)

### Store config in the environment

## [IV. Backing services](https://12factor.net/backing-services)

### Treat backing services as attached resources

## [V. Build, release, run](https://12factor.net/build-release-run)

### Strictly separate build and run stages

## [VI. Processes](https://12factor.net/processes)

### Execute the app as one or more stateless processes

## [VII. Port binding](https://12factor.net/port-binding)

### Export services via port binding

## [VIII. Concurrency](https://12factor.net/concurrency)

### Scale out via the process model

## [IX. Disposability](https://12factor.net/disposability)

### Maximize robustness with fast startup and graceful shutdown

## [X. Dev/prod parity](https://12factor.net/dev-prod-parity)

### Keep development, staging, and production as similar as possible

## [XI. Logs](https://12factor.net/logs)

### Treat logs as event streams

## [XII. Admin processes](https://12factor.net/admin-processes)

### Run admin/management tasks as one-off processes

[Italiano (it)](https://12factor.net/it/) | [Deutsch (de)](https://12factor.net/de/) | [Français (fr)](https://12factor.net/fr/) | [Turkish (tr)](https://12factor.net/tr/) | [日本語 (ja)](https://12factor.net/ja/) | [Brazilian Portuguese (pt_br)](https://12factor.net/pt_br/) | [Polski (pl)](https://12factor.net/pl/) | [Español (es)](https://12factor.net/es/) | [한국어 (ko)](https://12factor.net/ko/) | [Русский (ru)](https://12factor.net/ru/) | [简体中文 (zh_cn)](https://12factor.net/zh_cn/) | [Українська (uk)](https://12factor.net/uk/) | English (en)

Written by Adam Wiggins

Last updated Jan 30, 2012

[Sourcecode](https://github.com/heroku/12factor)

[Download ePub Book](https://12factor.net/12factor.epub)

[Privacy Policy](https://www.heroku.com/policy/privacy)
[(L)](https://12factor.net/#)Window size:  x
Viewport size:  x