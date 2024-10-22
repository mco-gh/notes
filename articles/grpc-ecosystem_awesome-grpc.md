grpc-ecosystem/awesome-grpc

# Awesome gRPC

> A curated list of useful resources for gRPC

## Contents

## Documentation

- [Website](https://grpc.io/) - Official documentation, libraries, resources, samples and FAQ
- [Technical documentation](https://github.com/grpc/grpc/tree/master/doc) - Collection of useful technical documentation
- [gRPC status codes](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md) - Status codes and their use in gRPC
- [gRPC status code mapping](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md) - HTTP to gRPC Status Code Mapping

## Community

- [Community links](https://grpc.io/community/) - Mailing list, Gitter, Twitter, Reddit

## Official Libraries and Tools

- [gRPC Core](https://github.com/grpc/grpc) - C, C++, Ruby, Node.js, Python, PHP, C#, Objective-C
- [gRPC Java](https://github.com/grpc/grpc-java) - The Java gRPC implementation. HTTP/2 based RPC
- [gRPC Node.js](https://github.com/grpc/grpc-node) - gRPC for Node.js
- [gRPC Go](https://github.com/grpc/grpc-go) - The Go language implementation of gRPC. HTTP/2 based RPC
- [gRPC Swift](https://github.com/grpc/grpc-swift) - The Swift language implementation of gRPC
- [gRPC Ecosystem](https://github.com/grpc-ecosystem) - gRPC Ecosystem that complements gRPC
- [gRPC contrib](https://github.com/grpc/grpc-contrib) - Known useful contributions around github
- [Homebrew gRPC](https://github.com/grpc/homebrew-grpc) - gRPC formulae repo for Homebrew
- [grpc_cli](https://github.com/grpc/grpc/blob/master/doc/command_line_tool.md) - gRPC CLI tool

## Other

### Tools

- [letmegrpc](https://github.com/gogo/letmegrpc) - Generate a web form gui from a grpc specification
- [grpcc](https://github.com/njpatel/grpcc) - Node.js grpc command-line client
- [gcall](https://github.com/bojand/gcall) - Simple Node.js gRPC command line interface
- [kafka-pixy](https://github.com/mwitkow/grpc-proxy) - gRPC/REST proxy for Kafka
- [ratelimit](https://github.com/lyft/ratelimit) - Go/gRPC service designed to enable generic rate limit scenarios from different types of applications
- [omgRPC](https://github.com/troylelandshields/omgrpc) - A GUI client for interacting with gRPC services, similar to what Postman is for REST APIs
- [ProfaneDB](https://gitlab.com/ProfaneDB/ProfaneDB) - A Protocol Buffers database with gRPC API, built in C++ on top of RocksDB
- [Evans](https://github.com/ktr0731/evans) - more expressive universal gRPC (CLI) client
- [grpcurl](https://github.com/fullstorydev/grpcurl) - Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers
- [danby](https://github.com/ericbets/danby) - A grpc proxy for the browser

### Go

- [go-GRPC Micro](https://github.com/micro/go-grpc) - [Micro](https://github.com/micro) based gRPC framework for microservices
- [go-kit gRPC](https://github.com/go-kit/kit/tree/master/transport/grpc) - [Go Kit](https://github.com/go-kit) with gRPC as transport
- [gRPC over NATS](https://github.com/rapidloop/nrpc) - nRPC is an RPC framework like gRPC, but for NATS.
- [grpc-web](https://github.com/improbable-eng/grpc-web) - gRPC Web implementation for Golang and TypeScript
- [rpcx](https://github.com/smallnest/rpcx) - A RPC service framework based on net/rpc like alibaba Dubbo and weibo Motan
- [grpclb](https://github.com/bsm/grpclb) - External Load Balancing Service solution for gRPC written in Go
- [grpc-proxy](https://github.com/mwitkow/grpc-proxy) - gRPC proxy is a Go reverse proxy that allows for rich routing of gRPC calls with minimum overhead
- [go-microservice-helpers](https://github.com/google/go-microservice-helpers) - A collection of handy snippets that simplify creation of gRPC servers and clients
- [lile](https://github.com/lileio/lile) - Easily create gRPC services in Go
- [proteus](https://github.com/src-d/proteus) - Generate .proto files from Go source code
- [protoc-gen-cobra](https://github.com/fiorix/protoc-gen-cobra) - command line tool generator for Go gRPC
- [gRPC over WebSocket](https://github.com/glerchundi/grpc-boomerang) - connect to a gRPC Server behind a firewall by using a pre-established WebSocket connection
- [yarpc](https://github.com/yarpc/yarpc-go) - A message passing platform for Go, including support for gRPC
- [promgrpc](https://github.com/piotrkowalczuk/promgrpc) - Prometheus instrumentation for gRPC based services
- [protoreflect](https://github.com/jhump/protoreflect) - Reflection (Rich Descriptors) for Go Protocol Buffers

### Node.js

- [Mali](https://github.com/malijs/mali) - A minimalistic gRPC microservice framework for Node.js
- [Condor Framework](https://github.com/devsu/condor-framework) - Framework for building gRPC services in Node JS
- [grpc-caller](https://github.com/bojand/grpc-caller) - An improved Node.js gRPC client
- [grpc-create-metadata](https://github.com/bojand/grpc-create-metadata) - Helper utility for creating gRPC `Metadata`
- [grpc-create-error](https://github.com/bojand/grpc-create-error) - Utility function for creating `Errors` for gRPC responses
- [grpc-error](https://github.com/bojand/grpc-error) - `GRPCError` class that wraps `create-grpc-error`
- [grpc-inspect](https://github.com/bojand/grpc-inspect) - gRPC protocol buffer inspection utility
- [Node.js Proto Files](https://github.com/googleapis/nodejs-proto-files) - All of the Google API's protocol buffer files
- [grpc-bus](https://github.com/paralin/grpc-bus) - Call gRPC services (even streams!) from the browser over any two-way socket to Node and soon Go
- [grpc-errors](https://github.com/ortoo/grpc-errors) - A quick and easy way of generating errors for use with grpc
- [grpc-client-promise](https://github.com/lvgithub/grpc-promise) - Grpc-promise also support Promise API. Which works very well with ES7 async await.

### Java

- [gax-java](https://github.com/googleapis/gax-java) - Google API Extensions for Java
- [Armeria](https://github.com/line/armeria) - Asynchronous RPC/REST library built on top of Java 8, Netty, HTTP/2, Thrift and gRPC
- [grpc-spring-boot-starter](https://github.com/yidongnan/grpc-spring-boot-starter) - Spring Boot starter module for gRPC framework
- [reactive-grpc](https://github.com/salesforce/reactive-grpc) - Integrates reactive programming with grpc-java
- [grpc-java-contrib](https://github.com/salesforce/grpc-java-contrib) - Useful extensions for the grpc-java library
- [rejoiner](https://github.com/google/rejoiner) - Generates a GraphQL schema from gRPC microservices

### Ruby

- [gruf](https://github.com/bigcommerce/gruf) - gRPC Ruby Framework

### Python

- [grpclib](https://github.com/vmagamedov/grpclib) - Pure-Python gRPC implementation, based on hyper-h2 project

### C#

- [MagicOnion](https://github.com/neuecc/MagicOnion) - gRPC based HTTP/2 RPC Streaming Framework for .NET, .NET Core and Unity

### Rust

- [grpc-rs](https://github.com/pingcap/grpc-rs) - The gRPC library for Rust built on C Core library and futures
- [grpc-rust](https://github.com/stepancheg/grpc-rust) - Rust implementation of gRPC

### Haskell

- [grpc-haskell](https://github.com/grpc/grpc-haskell) - gRPC library binding for Haskell

### Erlang

- [Erlang grpc](https://github.com/bluehouse-technology/grpc) - Erlang library for gRPC

### Elixir

- [grpc-elixir](https://github.com/tony612/grpc-elixir) - The Elixir implementation of gRPC

### Elm

- [elm-protobuf](https://github.com/tiziano88/elm-protobuf) - Protoc plugin generating elm code from proto definitions

### TypeScript

- [ts-protoc-gen](https://github.com/improbable-eng/ts-protoc-gen) - Protoc Plugin for TypeScript Declarations

### Scala

- [ScalaPB](https://scalapb.github.io/) - Protocol Buffer Compiler for Scala

### Dart

- [grpc-dart](https://pub.dartlang.org/packages/grpc) - Protocol Buffer Compiler for Dart

## Resources

### Tutorials

### Videos

- [gRPC: Google's high-performance, open-source RPC framework](https://www.youtube.com/watch?v=sZx3oZt7LVg) - GothamGo 2015 by Sameer Ajmani
- [Introduction to gRPC: A general RPC framework that puts mobile and HTTP/2 first](https://www.youtube.com/watch?v=kUz2zjkKxFg) - Devoxx by Mete Atamel
- [gRPC: The Story of Microservices at Square](https://www.youtube.com/watch?v=-2sWDr3Z0Wo) - Apigee webcast
- [Scalable Realtime Microservices with Kubernetes and gRPC](https://www.youtube.com/watch?v=xb8u2s7cxzg) - Mark Mandel @ Google
- [Text to Speech server with gRPC and Kubernetes](https://www.youtube.com/watch?v=XaMr--wAuSI) - justforfunc #12
- [GRPC Microservices 101](https://www.youtube.com/watch?v=-t57ZQZpjqs) - Google Developer Group Washington by Ray Tsang
- [Efficient Microservices w/ Binary Protocol - gRPC 101](https://www.youtube.com/watch?v=RqK-mwh3-aY) - By Ray Tsang
- [grpc: From Tutorial to Production](https://www.youtube.com/watch?v=7FZ6ZyzGex0) - GopherCon 2017 by Alan Shreve
- [Scalable Microservices with gRPC, Kubernetes, and Docker](https://www.youtube.com/watch?v=xsIwYL-N4vI) - Node Interactive 2016 by Sandeep Dinesh
- [Building Microservices w/gRPC & Kubernetes](https://www.youtube.com/watch?v=27swR9HACWU) - Philly ETE 2016 #49 by Kelsey Hightower
- [Building high performance microservices with Kubernetes, Go, and gRPC](https://www.youtube.com/watch?v=YiNt4kUnnIM) - Google Cloud Next '17 by Andrew Jessup
- [Modifying gRPC Services Over Time](https://www.youtube.com/watch?v=F2WYEFLTKEw) - Eric Anderson, Google at KubeCon + CloudNativeCon 2017 - Austin
- [Next Generation Services at Indeed Using gRPC](https://www.youtube.com/watch?v=aQ2d9iLDR8Y) - Jaye Pitzeruse, Indeed.com at KubeCon + CloudNativeCon 2017 - Austin
- [Generating Unified APIs with Protocol Buffers and gRPC](https://www.infoq.com/presentations/api-pb-grpc) - A video on Protocol Buffers, gRPC and Envoy from Lyft.
- [Intro to gRPC: A Modern Toolkit for Microservice Communication](https://www.youtube.com/watch?v=RoXT_Rkg8LA) - A video from Twilio's Signal Conference
- [gRPC and Go: Developing Efficient and Type-Safe Services](https://www.youtube.com/watch?v=J-NTfvYL_OE)
- [Best Practices for (Go) gRPC Services](https://www.youtube.com/watch?v=Z_yD7YPL2oE)
- [Creating GopherJS Apps with gRPC-Web](https://www.youtube.com/watch?v=R2HaxH7Et64) - At FOSDEM
- [justforfunc #31: gRPC Basics](https://www.youtube.com/watch?v=uolTUtioIrc) - JustForFunc: Programming in Go series Episode 31 covering gRPC

### Slides

- [gRPC Overview](http://www.slideshare.net/VarunTalwar4/grpc-overview) - An overview at gRPC: Talk at Slack by Varun Talwar
- [gRPC Design and Implementation](https://www.slideshare.net/VarunTalwar4/grpc-design-and-implementation) - April 2016 talk at Stanford by Varun Talwar
- [gRPC - boilerplate to high-performance scalable APIs](https://www.slideshare.net/AboutYouGmbH/robert-kubis-grpc-boilerplate-to-highperformance-scalable-apis-codetalks-2015) - code.talks 2015 by Robert Kubis
- [HTTP2 and gRPC](https://www.slideshare.net/GuoJing8/http2-and-grpc) - A simple introduction about HTTP2 and gRPC by Xin Gong Chang
- [gRPC and Microservices](https://www.slideshare.net/blinkingsquirrel/grpc-and-microservices) - Overview of Google's open source microservices framework - gRPC, based on HTTP2 and protocol buffers. Presented at Golang Melbourne, June 2016 by Jonathan Gomez
- [gRPC and Microservices](https://github.com/jonog/talks/blob/master/src/grpc/grpc-presentation.md) - Golang Melbourne - June 2016 Go Hack Night by Jonathan Gomez
- [Scalable Microservices with gRPC, Kubernetes, and Containers](https://speakerdeck.com/googlecloudplatform/scalable-microservices-with-grpc-kubernetes-and-containers-devfest-ukraine) - DevFest Ukraine
- [OpenAPI and gRPC Side by-Side](https://www.slideshare.net/timburks/openapi-and-grpc-side-byside) - APIStrat Conference - Tim Burks
- [Go+Microservices at Mercari](https://talks.godoc.org/github.com/tcnksm/talks/2017/11/gocon2017/gocon2017.slide) - Taichi Nakashima at Go Conference 2017

### Examples

- [gifinator](https://github.com/GoogleCloudPlatform/gifinator) - A sample application demonstrating Kubernetes, gRPC, Go and cute Gophers demoed at Google GCP Next 2017
- [Text to Speech server with gRPC and Kubernetes](https://github.com/campoy/justforfunc/tree/master/12-say-grpc) - justforfunc #12
- [Multiplayer Simon Says - A Game using gRPC and Kubernetes](https://github.com/grpc-ecosystem/grpc-simon-says) - Sample app with Go server and clients using Node.js (on Arduino and web), and Java (Android and CLI)
- [Go Microservices Example](https://github.com/harlow/go-micro-services) - HTTP up front, Protobufs in the rear
- [Streaming RPC's using gRPC](https://github.com/ridha/grpc-streaming-demo) - A quick demo of bi-directional streaming RPC's using grpc, Go and Python
- [gRPC Java Demos](https://github.com/saturnism/grpc-java-demos) - A collection of Java gRPC examples
- [gRPC/OpenCensus Demo](https://github.com/rakyll/opencensus-grpc-demo) - Export metrics and traces from gRPC servers and clients using Java, Go and Prometheus
- [go-micro-services](https://github.com/harlow/go-micro-services) - An demonstration of Golang micro-services that expose a HTTP/JSON frontend and then leverages gRPC for inter-service communication

### Miscellaneous

- [gRPC with Load Balancer or Proxy or on AWS](https://gist.github.com/bojand/6a604f7e369d7c7d8c39eb77878a42c2) - Various notes on doing gRPC behind a load balancer or proxy or on AWS
- [gRPC service upgrade, versioning](https://groups.google.com/forum/#!topic/grpc-io/LPsPg5ctQd4) - A short possibly useful discussion on gRPC service upgrade and versioning
- [Packaging Generated Code for gRPC Services](https://blog.bugsnag.com/libraries-for-grpc-services/) - An article demonstrating a strategy on how to version and package gRPC libraries

## Protocol Buffers

### Documentation

- [Website](https://developers.google.com/protocol-buffers/) - Official website an documentation

### Tools

- [prototools](https://github.com/sourcegraph/prototools) - Documentation generator & other tools for protobuf/gRPC
- [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc) - Documentation generator plugin for Google Protocol Buffers
- [openapi2proto](https://github.com/NYTimes/openapi2proto) - A tool for generating Protobuf v3 schemas and gRPC service definitions from OpenAPI specifications
- [Wireshark Protobuf Dissector](https://github.com/128technology/protobuf_dissector) - A Wireshark Lua plugin for decoding Google protobuf packets. [Relevant PR and discussion](https://github.com/google/protobuf/issues/3303).
- [protoc-gen-lint](https://github.com/ckaznocha/protoc-gen-lint) - A plug-in for Google's Protocol Buffers (protobufs) compiler to lint .proto files for style violations

### Similar

- [MessagePack](http://msgpack.org/index.html) - It's like JSON, but fast and small
- [Thrift](https://thrift.apache.org/) - Thrift is an interface definition language and binary communication protocol
- [TChannel](https://github.com/uber/tchannel) - Network multiplexing and framing protocol for RPC
- [Cap’n Proto](https://capnproto.org/) - Think Protocol Buffers, except faster
- [FlatBuffers](https://google.github.io/flatbuffers/) - An efficient cross platform serialization library
- [RSocket](http://rsocket.io/) - Application protocol providing Reactive Streams semantics
- [Twirp](https://github.com/twitchtv/twirp) - A simple RPC framework with protobuf service definitions
- [Greenpack](https://github.com/glycerine/greenpack) - Serialization format similar to MessagePack, but adds field versioning and type annotation

## Contribute

Contributions welcome! Read the [contribution guidelines](https://github.com/grpc-ecosystem/awesome-grpc/blob/master/contributing.md) first.

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).