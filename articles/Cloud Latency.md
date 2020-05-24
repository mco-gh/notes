Cloud Latency

# Cross Cloud Latency

### Measure latency across cloud providers and regions

* * *

##### What is this?

At some point I wanted to know which [GCP region](https://cloud.google.com/compute/docs/regions-zones/regions-zones) was closest to a third party service I had to deal with. I didn't want to email the company because that means dealing with sales. Instead, I decided to write some scripts to spin up instances, do a few pings here and there and get the info I wanted. Later on, I thought a tool like this could come in handy to other people so I decided to build it. You can query this service using the `REST` endpoints or via `Websockets` in either case you can get started using the Guest API Key below:

 `Marc Cohen API Key : 5d305534-0d9f-4063-afd6-7c16dbf7989b` This key is [rate limited](https://en.wikipedia.org/wiki/Rate_limiting) on a on IP basis (100 calls per second). Alternatively, you can sign-in with Google or Github to get you own API Key that can also be used to create new streams.

* * *

##### How does it work?

I have a a few VM's running in GCP and AWS respectively. They are constantly sending pings to each other and other destinations. The results are piped to websockets.

* * *

##### Got it, how do I use this?

To get started, pull the list of available streams and either retrieve the last 100 ticks or open a websocket connection to get the feed data. In the case of `REST` calls you'll have to pass your API Key (or the Guest one) using the `CC-LATENCY-API-KEY` header. If you are using `Websockets` you'll pass it as part of the payload when requesting a feed.

Here is an example of how to get the available streams using the Guest API Key and [curl](https://curl.haxx.se/docs/manual.html)

 `> curl -H "CC-LATENCY-API-KEY: 985668cf-cfa0-49e9-b087-83f1743fe5c7" https://api.cclatency.com/stream`

Pick a stream key and fetch some ticks:

 `> curl -H "CC-LATENCY-API-KEY: 985668cf-cfa0-49e9-b087-83f1743fe5c7" https://api.cclatency.com/stream/fdb23edb4a2aeb7a6da840ac84a3cf5c`

Websockets come in very handy when creating charts. The chart below shows the current latency (yellow line) from GCP::europe-west1-b (Belgium) to AWS::us-east-1a (Virginia, USA) and vice-versa (green line).

 ![](../_resources/fee6f2b81293f9106ace417791a5d247.png)

If you decide to get your own API Key you can create new streams. There is a limit of 10 per user, if you want your limit raised, you can join the [slack](https://join.slack.com/cclatency/shared_invite/MTkyMjE1NzQwODgzLTE0OTY1MDY5MjUtOGI5ODUyYWFjYg) channel and ask for it. If too many people asks for more and the API server becomes a bottleneck I'll have to start charging a low monthly fee to cover my cloud expenses (no more than 5$ or something). Please be reasonable when asking to get your quota increased.

* * *

##### Documentation

 `REST``GET https://api.cclatency.com/stream`

Returns the list of available streams. If you forget to pass an API Key you'll get a 401 back, any other kind of error will return 500.

- [Node.js](https://cclatency.com/#streams-node)

- [Python](https://cclatency.com/#streams-python)

- [curl](https://cclatency.com/#streams-curl)

- [*Sample response*](https://cclatency.com/#streams-response)

|     |     |
| --- | --- |
| 1   | // Assumes that you have both request and request-promised installed. |
| 2   | // Tested on node.js v7.5.0 |
| 3   | const  rp  =  require('request-promise'); |
| 4   |     |
| 5   | const  opts  = { |
| 6   | uri:  'https://api.cclatency.com/stream', |
| 7   | headers: { |
| 8   |  'CC-LATENCY-API-KEY':  '985668cf-cfa0-49e9-b087-83f1743fe5c7' |
| 9   | }   |
| 10  | };  |
| 11  |     |
| 12  | rp(opts) |
| 13  | .then(response  =>  console.log(response)) |
| 14  | .catch(error  =>  console.error(error)); |

 [view raw](https://gist.github.com/rmanyari/9628c64dad45f22310815d646a3dc45a/raw/853430225655effac0b34003ab63f4f837c1509e/node-streams-example.js)  [node-streams-example.js](https://gist.github.com/rmanyari/9628c64dad45f22310815d646a3dc45a#file-node-streams-example-js) hosted with ❤ by [GitHub](https://github.com/)

 `REST``GET https://api.cclatency.com/stream/:streamKey `

Returns up to 100 ticks for `:streamKey`. If you forget to pass an API Key you'll get a 401 back, if the `:streamKey` does not exist you'll get a 404 back. Any other error will return 500.

- [Node.js](https://cclatency.com/#stream-node)

- [Python](https://cclatency.com/#stream-python)

- [curl](https://cclatency.com/#stream-curl)

- [*Sample response*](https://cclatency.com/#stream-response)

|     |     |
| --- | --- |
| 1   | // Assumes that you have both request and request-promised installed. |
| 2   | // Tested on node.js v7.5.0 |
| 3   | const  rp  =  require('request-promise'); |
| 4   |     |
| 5   | const  opts  = { |
| 6   | uri:  'https://api.cclatency.com/stream/fdb23edb4a2aeb7a6da840ac84a3cf5c', |
| 7   | headers: { |
| 8   |  'CC-LATENCY-API-KEY':  '985668cf-cfa0-49e9-b087-83f1743fe5c7' |
| 9   | }   |
| 10  | };  |
| 11  |     |
| 12  | rp(opts) |
| 13  | .then(response  =>  console.log(response)) |
| 14  | .catch(error  =>  console.error(error)); |

 [view raw](https://gist.github.com/rmanyari/933b65cba11a7b3272bd1c39a25dae2a/raw/09eeca4c1a3cfd1c9c4d8655c7ca31f2c627f73a/node-stream-example.js)  [node-stream-example.js](https://gist.github.com/rmanyari/933b65cba11a7b3272bd1c39a25dae2a#file-node-stream-example-js) hosted with ❤ by [GitHub](https://github.com/)

 `REST``GET https://api.cclatency.com/sources`

Returns the list of available sources. These can be used to create new streams. If you forget to pass an API Key you'll get a 401 back. Any other error will return 500.

- [Node.js](https://cclatency.com/#sources-node)

- [Python](https://cclatency.com/#sources-python)

- [curl](https://cclatency.com/#sources-curl)

- [*Sample response*](https://cclatency.com/#sources-response)

|     |     |
| --- | --- |
| 1   | // Assumes that you have both request and request-promised installed. |
| 2   | // Tested on node.js v7.5.0 |
| 3   | const  rp  =  require('request-promise'); |
| 4   |     |
| 5   | const  opts  = { |
| 6   | uri:  'https://api.cclatency.com/sources', |
| 7   | headers: { |
| 8   |  'CC-LATENCY-API-KEY':  '985668cf-cfa0-49e9-b087-83f1743fe5c7' |
| 9   | }   |
| 10  | };  |
| 11  |     |
| 12  | rp(opts) |
| 13  | .then(response  =>  console.log(response)) |
| 14  | .catch(error  =>  console.error(error)); |

 [view raw](https://gist.github.com/rmanyari/88ebf09c0026f272a71dd8f9fee01340/raw/ab504405e6196440dba7bf8aa8cf8e6bcb6a6e12/node-sources-example.js)  [node-sources-example.js](https://gist.github.com/rmanyari/88ebf09c0026f272a71dd8f9fee01340#file-node-sources-example-js) hosted with ❤ by [GitHub](https://github.com/)

 `REST``POST https://api.cclatency.com/stream `

Schedules a new stream from a known source to a valid target. If you forget to pass an API Key you'll get a 401 back. The payload must conform to the schema otherwise you'll get a 400 with some description of what is wrong. Of all the requests this one is the less trivial. Scheduled streams have to be stored, topics have to be created and we need confirmation from a node that it actually started to process the task. If you have exceeded your quota you'll get a 429 (Too many requests). If anything goes wrong you'll get a 500 back.

- [Node.js](https://cclatency.com/#schedule-node)

- [Python](https://cclatency.com/#schedule-python)

- [curl](https://cclatency.com/#schedule-curl)

- [*Payload Schema*](https://cclatency.com/#schedule-payload)

- [*Sample response*](https://cclatency.com/#schedule-response)

|     |     |
| --- | --- |
| 1   | // Assumes that you have both request and request-promised installed. |
| 2   | // Tested on node.js v7.5.0 |
| 3   | const  rp  =  require('request-promise'); |
| 4   |     |
| 5   | const  opts  = { |
| 6   | uri:  'https://api.cclantency.com/stream', |
| 7   | method:  'POST', |
| 8   | headers: { |
| 9   |  'CC-LATENCY-API-KEY':  '<Your private API Key>' |
| 10  | },  |
| 11  | json:  true, |
| 12  | body: { |
| 13  | source:  'GCP::us-east4-a', |
| 14  | target:  'news.ycombinator.com', |
| 15  | interval:  1000, |
| 16  | packetType:  'ping' |
| 17  | }   |
| 18  | };  |
| 19  |     |
| 20  | rp(opts) |
| 21  | .then(response  =>  console.log(response)) |
| 22  | .catch(error  =>console.error(error)); |

 [view raw](https://gist.github.com/rmanyari/039ed8a4324e47189ce7448939803fad/raw/f7c8c086bc1bcd7d3b814703fa92c25567f0fe16/node-schedule-example.js)  [node-schedule-example.js](https://gist.github.com/rmanyari/039ed8a4324e47189ce7448939803fad#file-node-schedule-example-js) hosted with ❤ by [GitHub](https://github.com/)

 `Websockets``Register to a stream`

Data going in and out of the stream is formatted in JSON. All the fields in the register payload are mandatory. The first message that you will receive will either be a confirmation or an error. In case of an error the description field will contain the cause of the error.

- [Node.js](https://cclatency.com/#websocket-node)

- [Python](https://cclatency.com/#websocket-python)

- [HTML5](https://cclatency.com/#websocket-html5)

- [*Payload Schema*](https://cclatency.com/#websocket-payload)

- [*Sample confirmation*](https://cclatency.com/#websocket-confirmation)

- [*Sample tick*](https://cclatency.com/#websocket-tick)

|     |     |
| --- | --- |
| 1   | // Assumes that you have websockets installed. |
| 2   | // Tested on node.js v7.5.0 |
| 3   | const  ws  =  new  WebSocketClient(); |
| 4   |     |
| 5   | ws.on('connect', (connection) => { |
| 6   |  connection.send(JSON.stringify({ |
| 7   |  "action":  "register", |
| 8   |  "key":  "f2afa502b8c08ac87748527f022303a5", |
| 9   |  "apiKey":  "985668cf-cfa0-49e9-b087-83f1743fe5c7" |
| 10  | })); |
| 11  |  connection.on('message', (msg) =>  console.log(msg)); |
| 12  | }); |
| 13  |     |
| 14  | ws.connect('wss://api.cclatency.com'); |

 [view raw](https://gist.github.com/rmanyari/9e847cd5e67b8f3f4c557ff323f87923/raw/15698c107dde5488936a3083540ad31dea0270a9/node-ws-register-example.js)  [node-ws-register-example.js](https://gist.github.com/rmanyari/9e847cd5e67b8f3f4c557ff323f87923#file-node-ws-register-example-js) hosted with ❤ by [GitHub](https://github.com/)

* * *

##### FAQ

 **Why do you require Google/Github sign-in to get an API Key?**

I need a way to enforce quotas per user. By using Google/Github OAuth I can have a user identity without having to store passwords or any other kind of secret (which is a good thing).

 **How many machines do you have running, can it get expensive?**

Other than the VM's in each cloud provider/region, I'm also running a few PubSub topics, and AppEngine instances to serve the API. It might sound like a lot of infrastructure but so far it's not too bad in terms of $ and management.

 **Do you support anything else other than ping?**

Not at the moment. At some point I thought of adding the capability to specify things like *Send 5 times 10 TCP packets of 512 bytes in parallel with and interval of 1 minute* or *Send UDP packets of size between 16 bytes and 32 bytes with an interval or 100 to 200ms*. Getting that to work properly would be a bit more complicated. If enough people asks for it I can implement it.

 **Do you persist historical data?**

Not anymore. Initially I was storing all the data in [Datastore](https://cloud.google.com/datastore/docs/concepts/overview) but it turns out that it can be expensive to write all these datapoints. To give you an idea, let's say I cover 10 regions in AWS and GCP each that means 480 streams (20 * 20 - 20). At 1 ping per second thats 60 * 60 * 24 * 480 which is roughly 41 million rows per day or 1.2 billion rows per month. If I were to do 1.2 billion writes per month, that's a whooping [2,158.9](https://cloud.google.com/products/calculator/#id=64838822-1021-4a8a-aeba-8626984fdd71)$. Now, I can batch the writes in chunks of let's say 1000 which would take the price down to 22$/month or so. This is just to cover the base case, if I were to store all the streams created it would easily add up to 100's of dollars. I can't really afford that for a side project. If enough people asks for this feature I can 1) find the right storage technology 2) implement something around it and pass the costs down to whoever wants historical data.

 **I have more questions, what do I do?**

You can join the [slack](https://join.slack.com/cclatency/shared_invite/MTkyMjE1NzQwODgzLTE0OTY1MDY5MjUtOGI5ODUyYWFjYg) channel and ask your questions there.

 © Copyright 2017 Rodrigo Manyari, All Rights Reserved