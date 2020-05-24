Continuous Profiling of Go programs - Google Cloud - Community - Medium

# Continuous Profiling of Go programs

[![1*O8Ky4z8o_t8K0EwfnJ-M1A.jpeg](../_resources/94ceae5fa98a8c82d727b125bd3cf7cc.jpg)](https://medium.com/@rakyll?source=post_page-----96d4416af77b----------------------)

[Jaana Dogan](https://medium.com/@rakyll?source=post_page-----96d4416af77b----------------------)

[Apr 25, 2018](https://medium.com/google-cloud/continuous-profiling-of-go-programs-96d4416af77b?source=post_page-----96d4416af77b----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='199'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='200' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/96d4416af77b/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='208'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/96d4416af77b/share/facebook?source=post_actions_header---------------------------)

One of the most interesting parts of Google is our fleet-wide continuous profiling service. We can see who is accountable for CPU and memory usage, we can continuously monitor our production services for contention and blocking profiles, and we can generate analysis and reports and easily can tell what are some highly impactful optimization projects we can work on.

I briefly worked on [Google Cloud Profiler](https://cloud.google.com/profiler/), our new product that is filling the cloud-wide profiling gap for Cloud users. Note that you DON’T need to run your code on Google Cloud Platform in order to use it. Actually, I use it at development time on a daily basis now. It also supports Java and Node.js.

## Profiling in production

pprof is safe to use in production. We target an additional 5% overhead for CPU and heap allocation profiling. The collection is happening for 10 seconds for every minute from a single instance. If you have multiple replicas of a Kubernetes pod, we make sure we do amortized collection. For example, if you have 10 replicas of a pod, the overhead will be 0.5%. This makes it possible for users to keep the profiling always on.

We currently support CPU, heap, mutex and thread profiles for Go programs.

## Why?

Before explaining how you can use the profiler in production, it would be helpful to explain why you would ever want to profile in production. Some very common cases are:

- Debug performance problems only visible in production.
- Understand the CPU usage to reduce billing.
- Understand where the contention cumulates and optimize.
- Understand the impact of new releases, e.g. seeing the difference between canary and production.
- Enrich your distributed traces by [correlating](https://rakyll.org/profiler-labels/) them with profiling samples to understand the root cause of latency.

## Enabling

Stackdriver Profiler doesn’t work with the *net/http/pprof* handlers and require you to install and configure a one-line agent in your program.

go get [cloud.google.com/go/profiler](http://cloud.google.com/go/profiler)
And in your main function, start the profiler:
if err := profiler.Start(profiler.Config{
Service: "indexing-service",
ServiceVersion: "1.0",
ProjectID: "bamboo-project-606", // optional on GCP
}); err != nil {
log.Fatalf("Cannot start the profiler: %v", err)
}

Once you start running your program, the profiler package will report the profilers for 10 seconds for every minute.

## Visualization

As soon as profiles are reported to the backend, you will start seeing a flamegraph at https://console.cloud.google.com/profiler. You can filter by tags and change the time span, as well as break down by service name and version. The data will be around up to 30 days.

![1*JdCm1WwmTgExzee5-ZWfNw.gif](../_resources/b6ef6526b48ee9b1e1f1d913c3fb313f.jpg)
![1*JdCm1WwmTgExzee5-ZWfNw.gif](../_resources/7aeed5bde73baf08ca51055b53b17fe0.gif)

You can choose one of the available profiles; break down by service, zone and version. You can move in the flame and filter by tags.

## Reading the flame

Flame graph visualization is explained by [Brendan Gregg](http://www.brendangregg.com/flamegraphs.html) very comprehensively. Stackdriver Profiler adds a little bit of its own flavor.

![1*QqzFJlV9v7U1s1reYsaXog.png](../_resources/8e8c6daa09c381d9e95aa06cd760a3c9.png)
![1*QqzFJlV9v7U1s1reYsaXog.png](../_resources/2785c774f455d66b2d6b08ef7c33a115.png)
We will examine a CPU profile but all also applies to the other profiles.

1. The top-most x-axis represents the entire program. Each box on the flame represents a frame on the call path. The width of the box is proportional to the CPU time spent to execute that function.

2. Boxes are sorted from left to right, left being the most expensive call path.

3. Frames from the same package have the same color. All runtime functions are represented with green in this case.

4. You can click on any box to expand the execution tree further.
![1*1jCm6f-Fl2mpkRe3-57mTg.png](../_resources/c4440d72aaee7d49b81ffb1e05871808.png)
![1*1jCm6f-Fl2mpkRe3-57mTg.png](../_resources/ddab4d41fcf5b8c1668ce4035671e515.png)
You can hover on any box to see detailed information for any frame.

## Filtering

You can show, hide and highlight by symbol name. These are extremely useful if you specifically want to understand the cost of a particular call or package.

![1*ka9fA-AAuKggAuIBq_uhGQ.png](../_resources/5aac29beafe187623e6b9e42344d428f.png)
![1*ka9fA-AAuKggAuIBq_uhGQ.png](../_resources/017218972fb16e5e1dc88632e46fe46e.png)

1. Choose your filter. You can combine multiple filters. In this case, we are highlighting runtime.memmove.

2. The flame is going to filter the frames with the filter and visualize the filtered boxes. In this case, it is highlighting all runtime.memmove boxes.