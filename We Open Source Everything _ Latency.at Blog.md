We Open Source Everything | Latency.at Blog

# We Open Source Everything

March 28, 2018

[Infrastructure Diagram](../_resources/cc19e14174606e6ebb93d63edf6b4142.bin)

At Latency.at we measure performance and availability of your sites and services from multiple global locations and provides the results as Prometheus metrics.

We do so, by builting upon the [Prometheus Blackbox Exporter](https://github.com/prometheus/blackbox_exporter). Although we contributed back all additional features, like the per phase timings for HTTP(s) requests, we haven’t released our own components so far.

We believe in Open Source and that you should use Latency.at because we provide a reliable service, not because there is a lack of Open Source tools.

We also believe that we can do good beyond helping you to understand your sites performance and availability by sharing what we’ve learned and how we built our service.

**So I’m happy to announce that we make all components that make up our service available as Open Source!**

## Components

### Backend

You can find our golang based backend here: https://gitlab.com/latency.at/latencyAt

It contains the following binaries in `cmd/`:

- `api` api server
- `balancer` to reset free account balance each month
- `booker` receives pub/sub messages and decrements balance

#### Frontend

Here you can find our react frontend: https://gitlab.com/latency.at/web

The `aws/` directory contains a CloudFormation template to create the S3 buckets and CloudFront distribution for hosting the frontend

#### Probe

https://gitlab.com/latency.at/latency_exporter contains code for the probes. It’s a thin wrapper around the official [Prometheus Blackbox Exporter](https://github.com/prometheus/blackbox_exporter), which adds mainly two things:

- Validating `Authorization` Header by talking to our API server and caching the response for some time.
- Logging the request to Google Pub/Sub for updating the account balance

We use Pub/Sub instead of updating the balance via the API because eventually we’ll deploy a postgres read replica on each probe to do the validation of the Authorization Header locally. This will increase reliability and make it easier to scale.

## Next?

That’s not all! We will also Open Source all our Docker images and Kubernetes manifests. The plan is to release everything that is needed to deploy our complete infrastructure, including our [Public Prometheus Performance Metrics](https://pub.latency.at/) and our [Twitter Bot](https://twitter.com/LatencyAt/status/951107120174379008).

[Follow us on Twitter](https://twitter.com/LatencyAt) to get notified when we release the remaining components.