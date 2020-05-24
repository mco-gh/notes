Package trace

   [**go:**](https://github.com/GoogleCloudPlatform/gcloud-golang)  [cloud.google.com/go](https://godoc.org/cloud.google.com/go)/trace    [Index](https://godoc.org/cloud.google.com/go/trace#pkg-index)  |  [Examples](https://godoc.org/cloud.google.com/go/trace#pkg-examples)  |  [Files](https://godoc.org/cloud.google.com/go/trace#pkg-files)  |  [Directories](https://godoc.org/cloud.google.com/go/trace#pkg-subdirectories)

## package trace

`import "cloud.google.com/go/trace"`
Package trace is a Google Stackdriver Trace library.
This package is still experimental and subject to change.

See https://cloud.google.com/trace/api/#data_model for a discussion of traces and spans.

To initialize a client that connects to the Stackdriver Trace server, use the NewClient function. Generally you will want to do this on program initialization.

import "cloud.google.com/go/trace"
...
traceClient, err = trace.NewClient(ctx, projectID)

Calling SpanFromRequest will create a new trace span for an incoming HTTP request. If the request contains a trace context header, it is used to determine the trace ID. Otherwise, a new trace ID is created.

func handler(w http.ResponseWriter, r *http.Request) {
span := traceClient.SpanFromRequest(r)
defer span.Finish()
...
}

SpanFromRequest and NewSpan returns nil if the *Client is nil, so you can disable tracing by not initializing your *Client variable. All of the exported functions on *Span do nothing when the *Span is nil.

If you need to start traces that don't correspond to an incoming HTTP request, you can use NewSpan to create a root-level span.

span := traceClient.NewSpan("span name")
defer span.Finish()

Although a trace span object is created for every request, only a subset of traces are uploaded to the server, for efficiency. By default, the requests that are traced are those with the tracing bit set in the options field of the trace context header. Ideally, you should override this behaviour by calling SetSamplingPolicy. NewLimitedSampler returns an implementation of SamplingPolicy which traces requests that have the tracing bit set, and also randomly traces a specified fraction of requests. Additionally, it sets a limit on the number of requests traced per second. The following example traces one in every thousand requests, up to a limit of 5 per second.

p, err := trace.NewLimitedSampler(0.001, 5)
traceClient.SetSamplingPolicy(p)
You can create a new span as a child of an existing span with NewChild.
childSpan := span.NewChild(name)
...
childSpan.Finish()

When sending an HTTP request to another server, NewRemoteChild will create a span to represent the time the current program waits for the request to complete, and attach a header to the outgoing request so that the trace will be propagated to the destination server.

childSpan := span.NewRemoteChild(&httpRequest)
...
childSpan.Finish()

Alternatively, if you have access to the X-Cloud-Trace-Context header value but not the underlying HTTP request (this can happen if you are using a different transport or messaging protocol, such as gRPC), you can use SpanFromHeader instead of SpanFromRequest. In that case, you will need to specify the span name explicility, since it cannot be constructed from the HTTP request's URL and method.

func handler(r *somepkg.Request) {
span := traceClient.SpanFromHeader("span name", r.TraceContext())
defer span.Finish()
...
}

Spans can contain a map from keys to values that have useful information about the span. The elements of this map are called labels. Some labels, whose keys all begin with the string "trace.cloud.google.com/", are set automatically in the following ways:

- SpanFromRequest sets some labels to data about the incoming request.
- NewRemoteChild sets some labels to data about the outgoing request.
- Finish sets a label to a stack trace, if the stack trace option is enabled in the incoming trace header.
- The WithResponse option sets some labels to data about a response. You can also set labels using SetLabel. If a label is given a value automatically and by SetLabel, the automatically-set value is used.

span.SetLabel(key, value)
The WithResponse option can be used when Finish is called.
childSpan := span.NewRemoteChild(outgoingReq)
resp, err := http.DefaultClient.Do(outgoingReq)
...
childSpan.Finish(trace.WithResponse(resp))

When a span created by SpanFromRequest or SpamFromHeader is finished, the finished spans in the corresponding trace -- the span itself and its descendants -- are uploaded to the Stackdriver Trace server using the *Client that created the span. Finish returns immediately, and uploading occurs asynchronously. You can use the FinishWait function instead to wait until uploading has finished.

err := span.FinishWait()

Using contexts to pass *trace.Span objects through your program will often be a better approach than passing them around explicitly. This allows trace spans, and other request-scoped or part-of-request-scoped values, to be easily passed through API boundaries. Various Google Cloud libraries will retrieve trace spans from contexts and automatically create child spans for API requests. See https://blog.golang.org/context for more discussion of contexts. A derived context containing a trace span can be created using NewContext.

span := traceClient.SpanFromRequest(r)
ctx = trace.NewContext(ctx, span)

The span can be retrieved from a context elsewhere in the program using FromContext.

func foo(ctx context.Context) {
span := trace.FromContext(ctx).NewChild("in foo")
defer span.Finish()
...
}

### Index

- [Constants](https://godoc.org/cloud.google.com/go/trace#pkg-constants)

- [Variables](https://godoc.org/cloud.google.com/go/trace#pkg-variables)

- [func GRPCClientInterceptor() grpc.UnaryClientInterceptor](https://godoc.org/cloud.google.com/go/trace#GRPCClientInterceptor)
- [func GRPCServerInterceptor(tc *Client) grpc.UnaryServerInterceptor](https://godoc.org/cloud.google.com/go/trace#GRPCServerInterceptor)
- [func NewContext(ctx context.Context, s *Span) context.Context](https://godoc.org/cloud.google.com/go/trace#NewContext)

- [type Client](https://godoc.org/cloud.google.com/go/trace#Client)

    - [func NewClient(ctx context.Context, projectID string, opts ...option.ClientOption) (*Client, error)](https://godoc.org/cloud.google.com/go/trace#NewClient)

    - [func (c *Client) HTTPHandler(h http.Handler) http.Handler](https://godoc.org/cloud.google.com/go/trace#Client.HTTPHandler)
    - [func (c *Client) NewHTTPClient(orig *http.Client) *HTTPClient](https://godoc.org/cloud.google.com/go/trace#Client.NewHTTPClient)
    - [func (c *Client) NewSpan(name string) *Span](https://godoc.org/cloud.google.com/go/trace#Client.NewSpan)
    - [func (c *Client) SetSamplingPolicy(p SamplingPolicy)](https://godoc.org/cloud.google.com/go/trace#Client.SetSamplingPolicy)
    - [func (c *Client) SpanFromHeader(name string, header string) *Span](https://godoc.org/cloud.google.com/go/trace#Client.SpanFromHeader)
    - [func (c *Client) SpanFromRequest(r *http.Request) *Span](https://godoc.org/cloud.google.com/go/trace#Client.SpanFromRequest)

- [type Decision](https://godoc.org/cloud.google.com/go/trace#Decision)

- [type FinishOption](https://godoc.org/cloud.google.com/go/trace#FinishOption)

    - [func WithResponse(resp *http.Response) FinishOption](https://godoc.org/cloud.google.com/go/trace#WithResponse)

- [type HTTPClient](https://godoc.org/cloud.google.com/go/trace#HTTPClient)

    - [func (c *HTTPClient) Do(req *http.Request) (*http.Response, error)](https://godoc.org/cloud.google.com/go/trace#HTTPClient.Do)

- [type Parameters](https://godoc.org/cloud.google.com/go/trace#Parameters)

- [type SamplingPolicy](https://godoc.org/cloud.google.com/go/trace#SamplingPolicy)

    - [func NewLimitedSampler(fraction, maxqps float64) (SamplingPolicy, error)](https://godoc.org/cloud.google.com/go/trace#NewLimitedSampler)

- [type Span](https://godoc.org/cloud.google.com/go/trace#Span)

    - [func FromContext(ctx context.Context) *Span](https://godoc.org/cloud.google.com/go/trace#FromContext)

    - [func (s *Span) Finish(opts ...FinishOption)](https://godoc.org/cloud.google.com/go/trace#Span.Finish)
    - [func (s *Span) FinishWait(opts ...FinishOption) error](https://godoc.org/cloud.google.com/go/trace#Span.FinishWait)
    - [func (s *Span) NewChild(name string) *Span](https://godoc.org/cloud.google.com/go/trace#Span.NewChild)
    - [func (s *Span) NewRemoteChild(r *http.Request) *Span](https://godoc.org/cloud.google.com/go/trace#Span.NewRemoteChild)
    - [func (s *Span) SetLabel(key, value string)](https://godoc.org/cloud.google.com/go/trace#Span.SetLabel)
    - [func (s *Span) TraceID() string](https://godoc.org/cloud.google.com/go/trace#Span.TraceID)

#### Examples

- [Client.HTTPHandler](https://godoc.org/cloud.google.com/go/trace#example-Client-HTTPHandler)
- [HTTPClient.Do](https://godoc.org/cloud.google.com/go/trace#example-HTTPClient-Do)

####   [Package Files](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace)

[grpc.go](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/grpc.go)  [http.go](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/http.go)  [sampling.go](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/sampling.go)  [trace.go](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go)

### Constants

const ( // ScopeTraceAppend grants permissions to write trace data for a project.  ScopeTraceAppend = "https://www.googleapis.com/auth/trace.append" // ScopeCloudPlatform grants permissions to view and manage your data

// across Google Cloud Platform services.  ScopeCloudPlatform = "https://www.googleapis.com/auth/cloud-platform"

)

### Variables

var EnableGRPCTracing  [option](https://godoc.org/google.golang.org/api/option).[ClientOption](https://godoc.org/google.golang.org/api/option#ClientOption) = [option](https://godoc.org/google.golang.org/api/option).[WithGRPCDialOption](https://godoc.org/google.golang.org/api/option#WithGRPCDialOption)([grpc](https://godoc.org/google.golang.org/grpc).[WithUnaryInterceptor](https://godoc.org/google.golang.org/grpc#WithUnaryInterceptor)([GRPCClientInterceptor](https://godoc.org/cloud.google.com/go/trace#GRPCClientInterceptor)()))

EnableGRPCTracing automatically traces all outgoing gRPC calls from cloud.google.com/go clients.

The functionality in gRPC that this relies on is currently experimental.

Deprecated: Use option.WithGRPCDialOption(grpc.WithUnaryInterceptor(GRPCClientInterceptor())) instead.

### func [GRPCClientInterceptor](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/grpc.go#L34)

func GRPCClientInterceptor() [grpc](https://godoc.org/google.golang.org/grpc).[UnaryClientInterceptor](https://godoc.org/google.golang.org/grpc#UnaryClientInterceptor)

GRPCClientInterceptor returns a grpc.UnaryClientInterceptor that traces all outgoing requests from a gRPC client. The calling context should already have a *trace.Span; a child span will be created for the outgoing gRPC call. If the calling context doesn't have a span, the call will not be traced.

The functionality in gRPC that this feature relies on is currently experimental.

### func [GRPCServerInterceptor](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/grpc.go#L68)

func GRPCServerInterceptor(tc *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) [grpc](https://godoc.org/google.golang.org/grpc).[UnaryServerInterceptor](https://godoc.org/google.golang.org/grpc#UnaryServerInterceptor)

GRPCServerInterceptor returns a grpc.UnaryServerInterceptor that enables the tracing of the incoming gRPC calls. Incoming call's context can be used to extract the span on servers that enabled this option:

span := trace.FromContext(ctx)

The functionality in gRPC that this feature relies on is currently experimental.

### func [NewContext](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L436)

func NewContext(ctx [context](https://godoc.org/golang.org/x/net/context).[Context](https://godoc.org/golang.org/x/net/context#Context), s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) [context](https://godoc.org/golang.org/x/net/context).[Context](https://godoc.org/golang.org/x/net/context#Context)

NewContext returns a derived context containing the span.

### type [Client](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L258)

type Client struct { // contains filtered or unexported fields}
Client is a client for uploading traces to the Google Stackdriver Trace server.

#### func [NewClient](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L266)

func NewClient(ctx [context](https://godoc.org/golang.org/x/net/context).[Context](https://godoc.org/golang.org/x/net/context#Context), projectID [string](https://godoc.org/builtin#string), opts ...[option](https://godoc.org/google.golang.org/api/option).[ClientOption](https://godoc.org/google.golang.org/api/option#ClientOption)) (*[Client](https://godoc.org/cloud.google.com/go/trace#Client), [error](https://godoc.org/builtin#error))

NewClient creates a new Google Stackdriver Trace client.

#### func (*Client) [HTTPHandler](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/http.go#L82)

func (c *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) HTTPHandler(h [http](https://godoc.org/net/http).[Handler](https://godoc.org/net/http#Handler)) [http](https://godoc.org/net/http).[Handler](https://godoc.org/net/http#Handler)

HTTPHandler returns a http.Handler from the given handler that is aware of the incoming request's span. The span can be extracted from the incoming request in handler functions from incoming request's context:

span := trace.FromContext(r.Context())
The span will be auto finished by the handler.

[Example](https://godoc.org/cloud.google.com/go/trace#ex-Client-HTTPHandler)

#### func (*Client) [NewHTTPClient](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/http.go#L54)

func (c *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) NewHTTPClient(orig *[http](https://godoc.org/net/http).[Client](https://godoc.org/net/http#Client)) *[HTTPClient](https://godoc.org/cloud.google.com/go/trace#HTTPClient)

NewHTTPClient creates a new HTTPClient that will trace the outgoing requests using tc. The attributes of this client are inherited from the given http.Client. If orig is nil, http.DefaultClient is used.

#### func (*Client) [NewSpan](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L397)

func (c *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) NewSpan(name [string](https://godoc.org/builtin#string)) *[Span](https://godoc.org/cloud.google.com/go/trace#Span)

NewSpan returns a new trace span with the given name.

A new trace and span ID is generated to trace the span. Returned span need to be finished by calling Finish or FinishWait.

#### func (*Client) [SetSamplingPolicy](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L307)

func (c *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) SetSamplingPolicy(p [SamplingPolicy](https://godoc.org/cloud.google.com/go/trace#SamplingPolicy))

SetSamplingPolicy sets the SamplingPolicy that determines how often traces are initiated by this client.

#### func (*Client) [SpanFromHeader](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L334)

func (c *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) SpanFromHeader(name [string](https://godoc.org/builtin#string), header [string](https://godoc.org/builtin#string)) *[Span](https://godoc.org/cloud.google.com/go/trace#Span)

SpanFromHeader returns a new trace span, based on a provided request header value. See https://cloud.google.com/trace/docs/faq.

It returns nil iff the client is nil.

The trace information and identifiers will be read from the header value. Otherwise, a new trace ID is made and the parent span ID is zero.

The name of the new span is provided as an argument.

If a non-nil sampling policy has been set in the client, it can override the options set in the header and choose whether to trace the request.

If the header doesn't have existing tracing information, then a *Span is returned anyway, but it will not be uploaded to the server, just as when calling SpanFromRequest on an untraced request.

Most users using HTTP should use SpanFromRequest, rather than SpanFromHeader, since it provides additional functionality for HTTP requests. In particular, it will set various pieces of request information as labels on the *Span, which is not available from the header alone.

#### func (*Client) [SpanFromRequest](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L372)

func (c *[Client](https://godoc.org/cloud.google.com/go/trace#Client)) SpanFromRequest(r *[http](https://godoc.org/net/http).[Request](https://godoc.org/net/http#Request)) *[Span](https://godoc.org/cloud.google.com/go/trace#Span)

SpanFromRequest returns a new trace span for an HTTP request.
It returns nil iff the client is nil.

If the incoming HTTP request contains a trace context header, the trace ID, parent span ID, and tracing options will be read from that header. Otherwise, a new trace ID is made and the parent span ID is zero.

If a non-nil sampling policy has been set in the client, it can override the options set in the header and choose whether to trace the request.

If the request is not being traced, then a *Span is returned anyway, but it will not be uploaded to the server -- it is only useful for propagating trace context to child requests and for getting the TraceID. All its methods can still be called -- the Finish, FinishWait, and SetLabel methods do nothing. NewChild does nothing, and returns the same *Span. TraceID works as usual.

### type [Decision](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/sampling.go#L41)

type Decision struct { Trace  [bool](https://godoc.org/builtin#bool)  // Whether to trace the request.  Sample  [bool](https://godoc.org/builtin#bool)  // Whether the trace is included in the random sample.  Policy  [string](https://godoc.org/builtin#string)  // Name of the sampling policy.  Weight  [float64](https://godoc.org/builtin#float64)  // Sample weight to be used in statistical calculations.}

Decision is the value returned by a call to a SamplingPolicy's Sample method.

### type [FinishOption](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L693)

type FinishOption interface { // contains filtered or unexported methods}

#### func [WithResponse](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L703)

func WithResponse(resp *[http](https://godoc.org/net/http).[Response](https://godoc.org/net/http#Response)) [FinishOption](https://godoc.org/cloud.google.com/go/trace#FinishOption)

WithResponse returns an option that can be passed to Finish that indicates that some labels for the span should be set using the given *http.Response.

### type [HTTPClient](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/http.go#L37)

type HTTPClient struct { [http](https://godoc.org/net/http).[Client](https://godoc.org/net/http#Client)  // contains filtered or unexported fields}

HTTPClient is an HTTP client that enhances http.Client with automatic tracing support.

#### func (*HTTPClient) [Do](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/http.go#L47)

func (c *[HTTPClient](https://godoc.org/cloud.google.com/go/trace#HTTPClient)) Do(req *[http](https://godoc.org/net/http).[Request](https://godoc.org/net/http#Request)) (*[http](https://godoc.org/net/http).[Response](https://godoc.org/net/http#Response), [error](https://godoc.org/builtin#error))

Do behaves like (*http.Client).Do but automatically traces outgoing requests if tracing is enabled for the current request.

If req.Context() contains a traced *Span, the outgoing request is traced with the existing span. If not, the request is not traced.

[Example](https://godoc.org/cloud.google.com/go/trace#ex-HTTPClient-Do)

### type [Parameters](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/sampling.go#L36)

type Parameters struct { HasTraceHeader  [bool](https://godoc.org/builtin#bool)  // whether the incoming request has a valid X-Cloud-Trace-Context header.}

Parameters contains the values passed to a SamplingPolicy's Sample method.

### type [SamplingPolicy](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/sampling.go#L28)

type SamplingPolicy interface { // Sample returns a Decision.
// If Trace is false in the returned Decision, then the Decision should be

// the zero value.  Sample(p [Parameters](https://godoc.org/cloud.google.com/go/trace#Parameters)) [Decision](https://godoc.org/cloud.google.com/go/trace#Decision)}

#### func [NewLimitedSampler](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/sampling.go#L92)

func NewLimitedSampler(fraction, maxqps [float64](https://godoc.org/builtin#float64)) ([SamplingPolicy](https://godoc.org/cloud.google.com/go/trace#SamplingPolicy), [error](https://godoc.org/builtin#error))

NewLimitedSampler returns a sampling policy that randomly samples a given fraction of requests. It also enforces a limit on the number of traces per second. It tries to trace every request with a trace header, but will not exceed the qps limit to do it.

### type [Span](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L562)

type Span struct { // contains filtered or unexported fields}
Span contains information about one span of a trace.

#### func [FromContext](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L444)

func FromContext(ctx [context](https://godoc.org/golang.org/x/net/context).[Context](https://godoc.org/golang.org/x/net/context#Context)) *[Span](https://godoc.org/cloud.google.com/go/trace#Span)

FromContext returns the span contained in the context, or nil.

#### func (*Span) [Finish](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L724)

func (s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) Finish(opts ...[FinishOption](https://godoc.org/cloud.google.com/go/trace#FinishOption))

Finish declares that the span has finished.
If s is nil, Finish does nothing and returns nil.

If the option trace.WithResponse(resp) is passed, then some labels are set for s using information in the given *http.Response. This is useful when the span is for an outgoing http request; s will typically have been created by NewRemoteChild in this case.

If s is a root span (one created by SpanFromRequest) then s, and all its descendant spans that have finished, are uploaded to the Google Stackdriver Trace server asynchronously.

#### func (*Span) [FinishWait](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L736)

func (s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) FinishWait(opts ...[FinishOption](https://godoc.org/cloud.google.com/go/trace#FinishOption)) [error](https://godoc.org/builtin#error)

FinishWait is like Finish, but if s is a root span, it waits until uploading is finished, then returns an error if one occurred.

#### func (*Span) [NewChild](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L584)

func (s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) NewChild(name [string](https://godoc.org/builtin#string)) *[Span](https://godoc.org/cloud.google.com/go/trace#Span)

NewChild creates a new span with the given name as a child of s. If s is nil, does nothing and returns nil.

#### func (*Span) [NewRemoteChild](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L609)

func (s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) NewRemoteChild(r *[http](https://godoc.org/net/http).[Request](https://godoc.org/net/http#Request)) *[Span](https://godoc.org/cloud.google.com/go/trace#Span)

NewRemoteChild creates a new span as a child of s.
Some labels in the span are set from the outgoing *http.Request r.

A header is set in r so that the trace context is propagated to the destination. The parent span ID in that header is set as follows: - If the request is being traced, then the ID of s is used. - If the request is not being traced, but there was a trace context header

in the incoming request for this trace (the request passed to
SpanFromRequest), the parent span ID in that header is used.

- Otherwise, the parent span ID is zero. The tracing bit in the options is set if tracing is enabled, or if it was set in the incoming request.

If s is nil, does nothing and returns nil.

#### func (*Span) [SetLabel](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L671)

func (s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) SetLabel(key, value [string](https://godoc.org/builtin#string))

SetLabel sets the label for the given key to the given value. If the value is empty, the label for that key is deleted. If a label is given a value automatically and by SetLabel, the automatically-set value is used. If s is nil, does nothing.

SetLabel shouldn't be called after Finish or FinishWait.

#### func (*Span) [TraceID](https://github.com/GoogleCloudPlatform/gcloud-golang/tree/master/trace/trace.go#L657)

func (s *[Span](https://godoc.org/cloud.google.com/go/trace#Span)) TraceID() [string](https://godoc.org/builtin#string)

TraceID returns the ID of the trace to which s belongs.

### Directories

| Path | Synopsis |
| --- | --- |
| [apiv1](https://godoc.org/cloud.google.com/go/trace/apiv1) | Package trace is an experimental, auto-generated package for the trace API. |

Package trace imports [22 packages](https://godoc.org/cloud.google.com/go/trace?imports) ([graph](https://godoc.org/cloud.google.com/go/trace?import-graph)) and is imported by [7 packages](https://godoc.org/cloud.google.com/go/trace?importers). Updated a day ago. [Refresh now](#). [Tools](https://godoc.org/cloud.google.com/go/trace?tools) for package owners.