ongoing by Tim Bray · Bits On the Wire

# Bits On the Wire

Search

Exactly 100% of everything on the Internet involves exchanging messages which represent items of interest to humans. These items can be classified into three baskets: One for “media” (images, sound, video), one for text (HTML, PDF, XML), and one for “objects” (chat messages, payments, love poems, order statuses). This is a survey of how Object data is encoded for transmission over the Internet. Discussed: JSON, binary formats like Avro and Protobufs, and the trade-offs. Much of what people believe to be true is not.

History sidebar · The first ever cross-systems data interchange format was[ASN.1](https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One), still used in some low-level Internet protocols and crypto frameworks. ASN.1 had a pretty good data-type story, but not much in the way of labeling. Unfortunately, this was in the days before Open Source, so the ASN.1 software I encountered was slow, buggy, and expensive.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-1)

Then XML came along in 1998. It had no data-typing at all but sensibly labeled nested document-like data structures. More important, it had lots of fast solid open-source software you could download and use for free, so everybody started using it for everything.

Then sometime after 2005, a lot of people noticed JSON. The “O” stands for “Object” and for shipping objects around the network, it was way slicker than XML. By 2010 or so, the virtuous wrath of the RESTafarians had swept away the pathetic remnants of the WS-* cabal. Most REST APIs are JSON, so the Internet’s wires filled up with media, text, and JSON.

On JSON · I think there’s still more of it out there than anything else, if only because there are so many incumbent REST CRUD APIs that are humming along staying out of the way and getting shit done.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-3)

JSON pros:

1. Readers and writers are implemented in every computer language known to humankind, and they tend to interoperate correctly and frictionlessly with each other, particularly if you follow the interoperability guidelines in[RFC 8259](https://tools.ietf.org/html/rfc8259), which all the software I use seems to.

2. It does a pretty good job of modeling nested-record structures.
3. It’s all-text, so humans can read it, which is super extra helpful.

4. You can receive a JSON message you know nothing about and pick it apart successfully without knowing its schema, assuming it has one, which it probably doesn’t. So you can accomplish a task like “Pull out the *item-count* and *item-price*fields that are nested in the top-level *order-detail* field” with pretty good results given just a blob of raw JSON.

5. You can reliably distinguish between numbers, strings, booleans, and *null*.
JSON cons:

1. The type system is impoverished. There is no timestamp type, no way to know whether a number should be treated as an integer or float or Bignum, no way to signal when string values are really enums, and so on.

2. Numbers are specially impoverished; in general you should assume that your repertoire is that of an IEEE double-precision float (but without NaN or ∞) which is adequate for most purposes, as long as you’re OK with an integer range of ±253(which you probably should be).

3. Since JSON is textual, there is a temptation to edit it by hand, and this is painful since it’s nearly impossible to get the commas in the right places. On top of which there are no comments.

4. JSON’s textuality, and the fact that it carries its field labels along, no matter how deeply nested and often repeated, suggest that it is unnecessarily verbose, particularly when numeric values are represented in textual form. Also, the text needs to be converted into binary form to be loaded into objects (or structs, or dicts) for processing by code in memory.

5. JSON doesn’t have a universally-accepted schema language. I have been publicly disappointed over “JSON Schema”, the leading contender in that space; it’s just not very good. For a long time, the popular Swagger (now OpenAPI) protocols for specifying APIs used a variant version of a years-old release of JSON Schema; those are stable and well-tooled.

![](../_resources/9084124b8239df2d7d33eb881a6a6afe.png)

Mainstream binary formats · I think that once you get past JSON,[Apache Avro](https://en.wikipedia.org/wiki/Apache_Avro) might be the largest non-text non-media consumer of network bandwidth. This is due to its being wired into Hadoop and, more recently, the surging volume of Kafka traffic. Confluent, the makers of Kafka, provide good Avro-specific tooling. Most people who use Avro seem to be reasonably happy with it.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-5)

![](../_resources/0af5e6cc3f1822cde9b44d208f593abe.png)

[Protobufs (short for “Protocol Buffers”)](https://developers.google.com/protocol-buffers) I think would be the next-biggest non-media eater of network bandwidth. It’s out of Google and is used in gRPC which, as an AWS employee, I occasionally get bitched at for not supporting. When I worked at Google I heard lots of whining about having to use Protobufs, and it’s fair to say that they are [not universally loved](http://reasonablypolymorphic.com/blog/protos-are-wrong/).

Next in line would be Thrift, which is kind of abstract and includes its own RPC protocol and is out of Facebook and I’ve never been near it.

JSON vs binary · This is a super-interesting topic. It is frequently declaimed that only an idiot would use JSON for anything because it’s faster to translate back and forth between data types in memory with Avro/Protobufs/Thrift/Whatever (hereinafter “binary”) than it is with JSON, and because binary is hugely more compact. Also binary comes with schemas, unlike JSON. And furthermore, binary lets you use gRPC, which must be brilliant since it’s from Google, and so much faster because it’s compact and can stream. So, get with it![ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-6)

Is binary more compact than JSON? · Yes, but it depends. In one respect, absolutely, because JSON carries all its field labels along with it.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-7)

Also, binary represents numbers as native hardware numbers, while JSON uses strings of decimal digits. Which must be faster, right? Except for your typical hardware number these days occupies 8 bytes if it’s a float, and I can write lots of interesting floats in less than 8 digits; or 4 bytes for integers, and I can… hold on, a smart binary encoder can switch between 1, 2, 4, and 8-byte representations. As for strings, they’re all just the same UTF-8 bytes either way. But binary *should* win big on enums, which can be represented as small numbers.

So let’s grant that binary is going to be more compact as long as your data isn’t mostly all strings, and the string values aren’t massively longer than the field labels. But maybe not as much as you thought.

Unless of course you compress. This changes the picture and there are a few more it-depends clauses, but compression, in those scenarios where you can afford it, probably reduces the difference dramatically. And if you really care about size enough that it affects your format choices, you should be seriously looking at compression, because there are lots of cases where you’ve got CPU to spare and are network-limited.

Is binary faster than JSON? · Yes, but it depends. Here’s[an interesting benchmark](https://auth0.com/blog/beating-json-performance-with-protobuf/) from Auth0 showing that if you’re working in JavaScript, the fact that JSON is built-in to the platform makes Protobuf’s advantages mostly disappear; but in an equivalent Java app, protobuf wins big-time.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-8)

Whether or not your data is number- or string-heavy matters in this context too, because serializing or deserializing strings is just copying UTF-8bytes.

I mentioned gRPC above, and one aspect of speed heavily touted by the binary tribe is in protobufs-on-gRPC which, they say, is*obviously much faster* than JSON over HTTP. Except for HTTP is increasingly HTTP/2, with longer-lived connections and interleaved requests. And is soon going to be QUIC, with UDP and no streams at all. And I wonder how “obvious” the speed advantage of gRPC is going to be in that world?

I linked to that one benchmark just now but that path leads to a slippery slope; the Web is positively stuffed with serialization/deserialization benchmarks, many of them suffering from various combinations of bias and incompetence. Which raises a question:

Do speed and size matter? · Can I be seriously asking that question? Sure, because lots of times the size and processing speed of your serialization format just don’t matter in the slightest, because your app is bottlenecked on database, or on garbage collection, or on a matrix inversion or an FFT or whatever.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-9)

What you should do about this · Start with the simplest possible thing that could possibly work. Then benchmark using *your data* with *your messaging patterns*. In the possible but not terribly likely case that your message transmission and serialization is a limiting factor in what you’re trying to do, go shopping for a better data encoding.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-11)

The data format long tail · [Amazon Ion](http://amzn.github.io/ion-docs/) has been around for years running big systems inside Amazon, and decloaked in 2015-16. It’s a JSON superset with a usefully-enriched type system that comes in fully interoperable binary and textual formats. It has a[schema facility](https://amzn.github.io/ion-schema/). I’ve never used Ion but people at Amazon whose opinion I respect swear by it. Among other things, it’s used heavily in[QLDB](https://aws.amazon.com/qldb/), which is my personal favorite new AWS service of recent years.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-14)

[CBOR](http://cbor.io/) is another binary format, also a superset of JSON. I am super-impressed with the encoding and tagging designs. It also has a schema facility called CDDL that I haven’t really looked at. CBOR has implementations in[really a lot](http://cbor.io/impls.html) of different languages.

I know of one very busy data stream at AWS that’s running at a couple of million objects a second where you inject JSON and receive JSON, but the data in the pipe is CBOR because at that volume size really starts to matter. It helped that the service is implemented in Java and the popular Jackson library handles CBOR in a way that’s totally transparent to the developer.

I hadn’t really heard much about [MessagePack](https://msgpack.org/index.html) until I was researching this piece. It’s yet another “efficient binary serialization format”. The thing that strikes me is that every single person who’s used it seems to have positive things to say, and I haven’t encountered a “why this sucks” rant of the form that it’s pretty easy to find for every other object encoding mentioned in this piece. Checking it out is on my to-do list.

While on the subject of efficient something something binary somethings, I should mention[Cap’n Proto](https://capnproto.org/) and[FlatBuffers](https://google.github.io/flatbuffers/), both of which seem to be like Avro only more so, and make extravagant claims about how you can encode/decode in negative nanoseconds. Neither seems to have swept away the opposition yet, though.

* [Shouldn’t you mention YAML? —Ed.]
 [No, this piece is about data on the *network*. —T.]*

On Schemas · Binary really needs schemas to work, because unless you know what those bits all snuggled up together mean, you can’t un-snuggle them into your software’s data structures. This creates a problem because the sender and receiver need to use the same (or at least compatible) schemas, and, well, they’re in different places, aren’t they? Otherwise what’s the point of having messaging software?[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-10)

Now there are some systems, for example Hadoop, where you deal with huge streams of records all of which are the same type. So you only have to communicate the schema once. A useful trick is to have the first record you send be the schema which then lets you reliably parse all the others.

Avro’s wire format on Kafka has a neat trick: The second through fifth byte encode a 4-byte integer that identifies the schema. The number has no meaning, the schema registry assigns them one-by-one as you add new schemas. So assuming both the sender and the receiver are using the same schema registry, everything should work out fine. One can imagine a world in which you might want to share schemas widely and give them globally-unique names. But those 32-bit numbers are deliciously compact and stylishly postmodern in their minimalism, no syntax to worry about.

Some factions of the developer population are disturbed and upset that a whole lot of JSON is processed by programmers who don’t trouble themselves much about schemas. Let me tell you a story about that.

Back in 2015, I was working on the AWS service that launched as CloudWatch Events and is now known as[EventBridge](https://aws.amazon.com/eventbridge/). It carries events from a huge number of AWS services in a huger number of distinct types. When we were designing it, I was challenged “Shouldn’t we require schemas for all the event types?” I made the call that no, we shouldn’t, because we wanted to make it super-easy for AWS services to onboard, and in a lot of cases the events were generated by procedural code and never had a schema anyhow.

We’ve taken a lot of flak for that, but I think it was the right call, because we did onboard all those services and now there are a huge number of customers getting good value out of EventBridge. Having said that, I think it’d be a good idea at some future point to have schemas for those events to make developers’ lives easier.

Not that most developers actually care about schemas as such. But they would like autocomplete to work in their IDEs, and they’d like to make it easy to transmogrify a JSON blob into a nice programming-language object. And schemas make that possible.

But let’s not kid ourselves; schemas aren’t free. You have to coördinate between sender and receiver, and you have to worry what happens when someone wants to add a new field to a message type — but in raw JSON, you don’t have to worry, you just toss in the new field and things don’t break. Flexibility is a good thing.

Events, pub/sub, and inertia · Speaking of changes in message formats, here’s something I’ve learned in recent years while working on AWS eventing technology:*It’s really hard to change them*. Publish/subscribe is basic to event-driven software, and the whole point of pub/sub is that the event generator needn’t know, and doesn’t have to care, about who’s going to be catching and processing those events. This buys valuable decoupling between services; the bigger your apps get and the higher the traffic volume, the more valuable the decoupling becomes. But it also means that you really *really* can’t make any backward-incompatible changes in your event formats because you will for damn sure break downstream software you probably never knew existed. I speak from bitter experience here.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-15)

Now, if your messages are in JSON, you can *probably* get away with throwing in new fields. But almost certainly not if you’re using a binary encoding.

What this means in practice is that if you have a good reason to update your event format, you can go ahead and do it, but then you probably have to emit a stream of new-style events while you keep emitting the old-style events too, because if you cut them off, cue more downstream breakage.

The take-away is that if you’re going to start emitting events from a piece of software, put just as much care into it as you would as you do in specifying an API. Because event formats are a contract, too. And never forget[Hyrum’s Law](https://www.hyrumslaw.com/):

> With a sufficient number of users of an API,
> it does not matter what you promise in the contract:
> all observable behaviors of your system
> will be depended on by somebody.
Messages too!

The single true answer to all questions about data encoding formats · “It depends.”[ ¶](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#p-16)

* * *

Please feel free to [contribute a comment](https://www.tbray.org/atompub/comment?frag=/ongoing/When/201x/2019/11/17/Bits-On-the-Wire&title=%20Tim%20Bray%20%C2%B7%20Bits%20On%20the%20Wire) on this fragment.

**Updated: 2019/11/21**

* * *

## Contributions

Comment feed for *ongoing*:[![](../_resources/dc47e7e765c384f1f65697bd1c9a7569.png)](https://www.tbray.org/ongoing/comments.atom)

From: [Johannes Rudolph](http://https//blog.virtual-void.net) (Nov 21 2019, at 01:29)

> Start with the simplest possible thing that could possibly work.

:+1: I guess that also explains why JSON is still going strong. It's so simple to use, so universal, and so easy to consume on the web.

> Is binary faster than JSON?

JSON parsers are really fast this days, often needing only a small number of cycles per byte parsed which can get you to the order of parsing one GB of JSON per second per core. And, although JSON parsing indeed means just copying UTF8 encoded strings around, the thing that is somewhat expensive in all text-based data formats is the scanning for the delimiters. E.g. in JSON, you need to skip over whitespace and find the ends of strings, in HTTP/1 you need to look for the CRLF at the end of header lines etc. These are the things that are cheaper with most binary formats because they will include explicit lengths for variable sized fields.

Including binary data inside of JSON is another thing that is not quite optimal. Using base64 encoding to put binary data in JSON is somewhat ok if you compress the JSON afterwards [1].

> Binary really needs schemas to work

Is that really accurate in general? If you compare JSON and CBOR, one is text-based and the other is binary. Even without having a schema, they both can represent a similar data set (basically nested key/value objects). Both are somewhat self-describing, you can read JSON in a simple editor while you need some tool to make CBOR readable. But in the end, you should be able to understand the data to some degree. Especially for longer-term storage you want some self-describing serialization formats.

On the other hand, there are many binary formats that are not self-describing in the same way. E.g. if you go to protobuf, you will still be able to parse the binary format even without a schema but you will be missing the mapping between field ids and field names. And then there are other binary formats where even more of the structure of data needs to be known just to parse the data.

[1] https://blog.virtual-void.net/base64-vs-gzip/

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574328559.363889)]*

From: [Osvaldo Doederlein](http://https//twitter.com/opinali) (Nov 21 2019, at 12:30)

"whining about Protobufs" - because we use it SO much at Google? To quote Stroustrup, "There are only two kinds of languages: the ones people complain about and the ones nobody uses."

"Do speed and size matter?" - Proto is also used for storage, messaging, logs... It makes a difference at scale. And you can very often push data between the whole stack, e.g. from persistent store to RPC or pubsub to a proxy task to an application's heap -- with minimal or no decoding/reencoding cost, but still allowing each stage of that pipeline to inspect or manipulate payloads if necessary; a universal data format creates virtuous-cycle effects. I'm skeptic that any bloated text format could do this, because its performance disadvantages would need to be insignificant in *every* part of the architecture.

"It’s really hard to change them" - Protobuf is specifically optimized for evolution, and that works pretty well. https://developers.google.com/protocol-buffers/docs/proto3#updating

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574368251.710000)]*

From: [r0y](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wirehttp:) (Nov 21 2019, at 15:21)

- ASN.1 may have been the first general-purpose serialization format (or maybe not?) but it definitely wasn't the first cross-systems data interchange format.
- The quality of ASN.1 implementations has nothing to do with open source, it has to do with the design of ASN.1. A friend who worked with ASN.1 opined that it's impossible to write a bug-free ASN.1 parser.
- You left out Sun XDR.
- "Everyone started using XML because there were open-source implementations" isn't how any of this happened.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574378485.497963)]*

From: [Rob Sayre](http://https//sayrer.com) (Nov 21 2019, at 17:12)

I think the big advantage of something like Protobuf (or Thrift, etc) is collaboration.

The documentation of the fields (and service endpoints) lives in the .proto file, from which all of the client and server code is generated. It's similar to the way "doctest" keeps examples working in Python and Rust.

This way, there's no need for a wiki documenting the JSON fields, and no need to write code that fishes around in JSON dictionaries.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574385136.952266)]*

From: [John Cowan](http://vrici.lojban.org/~cowan) (Nov 21 2019, at 17:24)

One of my current projects is the construction of an interchange format designed specially for the needs of Lisp-family languages, which (a) deal in S-expressions and (b) are dynamically typed. I wanted to provide both a textual representation close to classical S-expressions and a binary representation that would not require a schema to interpret it.

Using the ordinary Lisp syntax gave me exact and inexact real numbers and (with a choice of notations) complex numbers as well, strings, symbols, lists, and general vectors. For bytevectors I am using hex digits wrapped in braces, as the notation used by Scheme, "#u8(0x12 0x13 0x14) is too verbose. (I might switch to base64.) Finally, any of these notations can be prefixed by "#" and an identifier or hex number to indicate a particular type: for example, "2019-11-21" is a string, but #date"2019-11-21" is a date object.

The binary representation that goes with this is, surprise, ASN.1 DER, with explicit type-length-value representations of everything. (Sets don't have to be sorted, though DER prescribes it.) Bits in the type code tell the reader whether the value is a bytestring or a sequence of embedded objects, as well as whether it's standard ASN.1, a Lisp extensions type, or something private. Because of the possibility that you get an ASN.1 datum whose interpretation isn't known (say type 99), the S-expression form can have #99 followed by the content as a UTF-8 string, bytevector, or list, and it can be unpacked or converted without problem.

The downside of any length-value representation, of course, is that you can't do streaming output, though you can do streaming input. But that's also true of JSON and many other formats.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574385857.244828)]*

From: [Joac](http://blog.joac.com.ar/) (Nov 22 2019, at 04:55)
Some clarification about CBOR and MessagePack.

CBOR is just Message Pack with a spec on IETF. The said author of CBOR (C. Bormann) just wrote the spec and stole the protocol without credit for the original authors.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574427308.655258)]*

From: [name](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wirehttp:) (Nov 22 2019, at 11:21)

Another binary encoding that might be of passing interest would be Simple Binary Encoding, supposedly used in finance.

https://github.com/real-logic/simple-binary-encoding/wiki

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574450472.723191)]*

From: [Robert](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wirehttp:) (Nov 22 2019, at 17:19)

Great post as always. Something to consider in these things is the encoding standard for strings as well. Java and JSON don't line up here - Java encodes UTF-16 and JSON is encoded UTF-8. This is ok, but requires encoding. This can also be very very expensive depending on the structure of the document. Binary encodings tend to avoid a lot of this, especially if the UTF-i-ness of the runtime and standard line up.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574471948.567585)]*

From: [Miikka](http://https//quanttype.net/) (Nov 22 2019, at 23:14)

In the Clojure world, we use Transit a lot. It's a way to encode EDN ("Clojure data" in the same sense as JSON is "JavaScript data") as JSON. Because you can use the built-in JSON parsing in the browsers, it's way faster than using an EDN parser.

https://github.com/cognitect/transit-format

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574493247.606903)]*

From: [Rob Sayre](http://https//sayrer.com) (Nov 22 2019, at 23:53)

"Now, if your messages are in JSON, you can probably get away with throwing in new fields. But almost certainly not if you’re using a binary encoding."

I don't think this assertion is correct. You can add fields to most of the binary formats (including protobuf, thrift, etc) with the same restrictions you'd have with JSON.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574495592.686036)]*

From: [Robert](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wirehttp:) (Nov 23 2019, at 12:19)

To reinforce your point that it depends - we talk about compression. It’s a great thing, but it’s also expensive. If you can make yourself network bound with modern networking while doing compression, decompression, encoding changes, string operations and copying, etc before you hit CPU limits that’s impressive.

I think if compression ever matters to your for network efficiency it’s probably too late with today’s kit. You’re already cpu bound somewhere and you’re using distributed stuff for scale when you actually read and work on the data. There are probably some parts of your stack, like load balancers, that can really benefit from compression to de-scale.

I think this reflects a feature of computing that what becomes a bottleneck shifts as hardware paradigms shift. Networking bandwidths have become simply breathtaking compared to the past, with 100Gbps profiles being available with 25Gbps channels. These are amazing speeds. CPUs haven’t kept up with NICs, processing at line rate is becoming very much harder than it used to be.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/11/17/Bits-On-the-Wire#c1574540392.756735)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](https://www.tbray.org/ongoing/WhatItIs) ·[(L)](https://www.tbray.org/ongoing/ongoing.atom)

[Truth](https://www.tbray.org/ongoing/Truth) ·[Biz](https://www.tbray.org/ongoing/Biz) ·[Tech](https://www.tbray.org/ongoing/Tech)

[author](https://www.tbray.org/ongoing/misc/Tim) ·[Dad](http://www.textuality.com/BillBray/) ·[software](https://www.tbray.org/ongoing/misc/Software) ·[colophon](https://www.tbray.org/ongoing/misc/Colophon) ·[rights](https://www.tbray.org/ongoing/misc/Copyright)

* * *

[November](https://www.tbray.org/ongoing/When/201x/2019/11/)  [17](https://www.tbray.org/ongoing/When/201x/2019/11/17/), [2019](https://www.tbray.org/ongoing/When/201x/2019/)

· [Technology](https://www.tbray.org/ongoing/What/Technology) (85 fragments)

· · [Internet](https://www.tbray.org/ongoing/What/Technology/Internet) (114 more)

By [Tim Bray](https://www.tbray.org/ongoing/misc/Tim)

I am an employee of Amazon.com, but the opinions expressed here are my own, and no other party necessarily agrees with them.

A full disclosure of my professional interests is on the [author](https://www.tbray.org/ongoing/misc/Tim) page.