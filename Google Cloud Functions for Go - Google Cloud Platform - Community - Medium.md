Google Cloud Functions for Go - Google Cloud Platform - Community - Medium

# Google Cloud Functions for Go

[![1*O8Ky4z8o_t8K0EwfnJ-M1A.jpeg](../_resources/94ceae5fa98a8c82d727b125bd3cf7cc.jpg)](https://medium.com/@rakyll?source=post_page-----57e4af9b10da----------------------)

[Jaana B. Dogan](https://medium.com/@rakyll?source=post_page-----57e4af9b10da----------------------)

[Sep 1, 2018](https://medium.com/google-cloud/google-cloud-functions-for-go-57e4af9b10da?source=post_page-----57e4af9b10da----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='195'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='196' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/57e4af9b10da/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='199'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='200' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/57e4af9b10da/share/facebook?source=post_actions_header---------------------------)

*In January 2019, Google Cloud Functions finally announced beta support for Go. Check out *[*the official blog post*](https://cloud.google.com/blog/products/application-development/cloud-functions-go-1-11-is-now-a-supported-language)* for more details.*

## Hello World

Let me start with a simple “hello world” to introduce you to the overall build+deploy experience. GCF expects an http.HandlerFunc to be the entry point. Create a package called “hello” and add a trivial handler:

$ cat hello/fn.go
package helloimport (
"fmt"
"net/http"
)func HelloWorld(w http.ResponseWriter, r *http.Request) {
fmt.Fprintf(w, "Hello, World!")
}

In order to deploy, use the following command. It will create a new function called hello and will use HelloWorld as the entry point. The Go runtime to be used will be Go.11.

$ gcloud functions deploy hello --entry-point HelloWorld --runtime go111 --trigger-http

Deploying function (may take a while - up to 2 minutes)...

Deploying may take a while as it is noted. Once deployed, you will be able to see the HTTP endpoints on your terminal. You can also view your functions at the [Cloud Console](https://console.cloud.google.com/functions/list).

![1*uOH3RWYZoOEarZvHAOxjJg.png](../_resources/b4ba476f2eeefe02321930e467e2483e.png)
![1*uOH3RWYZoOEarZvHAOxjJg.png](../_resources/a0e75534228d69fb45fe0a78ec6f6d26.png)

On the console, you can see “hello” function is deployed. You can access to logs and basic metrics such as number of invocations, execution time and memory usage.

## Dependencies

If you have external dependencies, go.mod file will be used to get the dependencies. You can also vendor them under the function module. I imported the golang.org/x/sync/errgroup package as an example. See [GCF guideline on dependencies](https://cloud.google.com/functions/docs/concepts/go-runtime#specifying_dependencies) if you need more information.

$ export GO111MODULE=on
$ cd hello
$ go mod init
$ tree
hello
├── fn.go
├── go.mod
├── go.sum
...
The dependency is going to be go-getted when I redeploy the function again.

$ gcloud functions deploy hello --entry-point HelloWorld --runtime go111 --trigger-http

Deploying function (may take a while - up to 2 minutes)...
availableMemoryMb: 256
entryPoint: HelloWorld
httpsTrigger:
url: https://us-central1-bamboo-shift-504.cloudfunctions.net/hello
...

Function is redeployed at https://us-central1-bamboo-shift-504.cloudfunctions.net/hello. See it yourself. You can also call the function from command line:

$ gcloud functions call hello
executionId: x71xpor7tasd
result: Hello, World!

I also generated some load from my laptop to the function to provide you a more realistic response time data. I made 1000 requests, 10 concurrently at a time. You can see that there are some outliers but most calls fall into the 213 milliseconds bucket.

![1*9b0hzD9A_n3RhB6tJKQCig.png](../_resources/57546760423aabdfa6d649eea4094fcb.png)
![1*9b0hzD9A_n3RhB6tJKQCig.png](../_resources/f9c5c19c632023bdcf74bac1271790b7.png)

## Code Organization

In Go, we organize packages by [responsibility](https://rakyll.org/style-packages/). This also fits well with serverless design patterns — a function is representing one responsibility. I create a new module for each function, provide function-specific other APIs from the same module.

The main entry point handler is always in **fn.go**, this helps me to quickly find the main handler the way main.go would help me to find the main function.

Common functionality lives in a separate module and vendored on the function package because GCF CLI uploads and deploys only one module at a time. We are thinking about how this situation can be improved but, currently a module should contain all of its dependencies itself.

An example tree is below. Package config contains configuration-related common functionality. It is a module and is imported and vendored by the other functions (hello and user).

$ tree
fns
├── config (commonly used module)
│ ├── config.go
│ ├── go.mod
│ └── go.sum
├── hello
│ ├── fn.go
│ ├── go.mod
│ ├── go.sum
│ └── vendor (contains all dependencies + config)
│ ├── ...
│ └── modules.txt
└── user
├── fn.go
├── go.mod
└── vendor (contains all dependencies + config)
├── ...
└── modules.txt

## Chaining Handlers

Unlike other providers, we decided to go with Go idiomatic handler APIs (func(ResponseWriter, *Request)) as the main entry point. This allows you to utilize existing middlewares available in the Go ecosystem more easily. For example, in the following example, I am using ochttp to automatically create traces for incoming HTTP requests.

package helloimport (
"fmt"
"net/http" "go.opencensus.io/plugin/ochttp"
)func HelloWorld(w http.ResponseWriter, r *http.Request) {
fn := func(w http.ResponseWriter, r *http.Request) {
fmt.Fprintln(w, "Hello world")
}
traced := &ochttp.Handler{
Handler: http.HandlerFunc(fn),
}
traced.ServeHTTP(w, r)
}

For each incoming request, an incoming trace span is created. If you register an exporter, you can upload the traces to [any backend](https://github.com/census-instrumentation/opencensus-go#exporters) we support including Stackdriver Trace of course.