ongoing by Tim Bray · Go Creeping In

# Go Creeping In

Search

I’ve seen the inside of the Google and Amazon tech stacks. There are common threads that run through them and also, I bet, through most BigTechCos. Here and there down the stack is a lot of C++ and vestigial remnants from earlier days, Perl or PHP or whatever. Out in front of humans, of course, JS. But in between, there are oceans and oceans of Java; to a remarkable degree, it runs the Internet. Except for, here and there, you find a small but steadily increasing proportion of Go.

![](../_resources/1cd3c4cb4c64ff98484716dbd15e53ce.png)

If you want to know what’s going on at Google, go follow[Brad Fitzpatrick](https://en.wikipedia.org/wiki/Brad_Fitzpatrick). If you want to know what’s going on at Amazon, I shouldn’t spill those beans without asking for permission, which I’ve never been good at. But I can write about what I’m hearing and seeing when I look around, both inside here and out there on the Internet.

I don’t know of any co-ordinated campaigns, here or anywhere else, aimed at walking away from Java or encouraging Go (or any other replacement) in a top-down way. I do notice good engineers just going ahead and standing up Go-based microservices.

There are a bunch of reasons for this, and lots of smart people have written wise words on the subject. But here are my perceptions.

Readability · I initially fell in love with Ruby because other people’s code was just easier to read than anything else I’d previously encountered. You needed to learn what how blocks work and what `|foo|` means, then it all just fell into place. Then when, based on that, you figured out[Enumerable](https://ruby-doc.org/core-2.6.3/Enumerable.html), you might have had heart palpitations.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#p-1)

Go takes it a step further. You need to get used to type declarations being backward and how[interfaces](https://tour.golang.org/methods/9) work. Then when you learn about channels and goroutines, you might experience shortness of breath.

It’s amazing —  *amazing* I say — how little generics are missed. To date, Go remains the small, simple language that fogies like me can remember Java being. I suppose that can’t last, but for now, I can pop open almost any `.go` file and if I can’t understand it pretty quick, the chances are very high that the problem is in the code not me.

Predictability · The Go runtime is garbage-collected, but the GC design is consciously optimized to be predictable and not induce latency; here’s[a nice deep-dive](https://blog.golang.org/ismmkeynote). There’s no free lunch, so that excellent latency probably carries a price in throughput. Which for a whole lot of online services is a good bargain.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#p-4)

Performance isn’t a simple subject. But there’s a perception among insiders that Go’s performance is good enough and its latency is low enough. Furthermore, that you can expect pretty similar numbers for P50 and P99.9 latencies. And a Go program starts up fast, which we in the Serverless tribe really like.

Goroutines · They make it easy and idiomatic to arrange that some parts of your computation be done in parallel with other parts. And unlike other concurrency frameworks I’ve fought with, you can pretty well just fling a (potentially huge) number of tasks at goroutines, and empirically, the runtime does a good job of keeping the cores busy and the work flowing through.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#p-2)

And (assuming a little care with buffer sizes) it’s very unlikely that you’ll get a deadlock or an annoying race-condition bug. I’ve *never* had one and I’ve seen plenty in certain other languages beginning with “J”.

Executables · The fact that Go generates statically linked binaries warms greybeards’ hearts, but I’ve noticed the young pups seem to like that too. And the first time I realized I could type `GOOS=linux go build` on my Mac and run the output as a Lambda function I grinned from ear to ear.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#p-3)

Speaking of Lambda, the Go runtime has pleased me every time I’ve tried it. Also I built a[custom Lambda runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html) in Go and that worked great on almost the first attempt, which impressed the hell out of me.

The future? · Nope, no language is, the future is obviously polyglot. But it’s a tool I’m turning to a whole lot, and I’m not the only one.[ ¶](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#p-5)

* * *

Please feel free to [contribute a comment](https://www.tbray.org/atompub/comment?frag=/ongoing/When/201x/2019/06/12/Go-Creeping-In&title=%20Tim%20Bray%20%C2%B7%20Go%20Creeping%20In) on this fragment.

**Updated: 2019/06/17**

* * *

## Contributions

Comment feed for *ongoing*:[![](../_resources/8e32700809f0dfb1a1f5b2dae473ec03.png)](https://www.tbray.org/ongoing/comments.atom)

From: [Gavin B](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-Inhttp:) (Jun 18 2019, at 02:47)

I guess, then, Go also beats Elixir/Erlang since it doesn't have any VM baggage to carry around.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#c1560851243.898338)]*

From: [JanB aka entity](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-Inhttp:) (Jun 18 2019, at 05:10)

I recently started coding go and started building my own database server using go. The only thing that i rlly can criticize is the handling of concurrent rw in golang. And sadly channels aren't the always fitting solution. In my case i got multiple goroutines to access a global storage (memory based database) so i had to find a way to manage concurrent rw access to it. I ended up using the rw mutex wich sadly isn't implemented very efficient. So from my pov the language is great and i gonne go on coding it but i hope they will implement any type of efficient designed concurrent container for use cases that channels can't handle.

*[[link](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#c1560859857.703560)]*

From: [Rob Sayre](http://https//sayrer.com) (Jun 18 2019, at 09:44)
There's a good paper on real-world concurrency bugs in Go. It's not all roses.

https://blog.acolyer.org/2019/05/17/understanding-real-world-concurrency-bugs-in-go/

*[[link](https://www.tbray.org/ongoing/When/201x/2019/06/12/Go-Creeping-In#c1560876242.473081)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](https://www.tbray.org/ongoing/WhatItIs) ·[(L)](https://www.tbray.org/ongoing/ongoing.atom)

[Truth](https://www.tbray.org/ongoing/Truth) ·[Biz](https://www.tbray.org/ongoing/Biz) ·[Tech](https://www.tbray.org/ongoing/Tech)

[author](https://www.tbray.org/ongoing/misc/Tim) ·[Dad](http://www.textuality.com/BillBray/) ·[software](https://www.tbray.org/ongoing/misc/Software) ·[colophon](https://www.tbray.org/ongoing/misc/Colophon) ·[rights](https://www.tbray.org/ongoing/misc/Copyright)

* * *

[June](https://www.tbray.org/ongoing/When/201x/2019/06/)  [12](https://www.tbray.org/ongoing/When/201x/2019/06/12/), [2019](https://www.tbray.org/ongoing/When/201x/2019/)

· [Technology](https://www.tbray.org/ongoing/What/Technology) (85 fragments)

· · [Software](https://www.tbray.org/ongoing/What/Technology/Software) (67 more)

By [Tim Bray](https://www.tbray.org/ongoing/misc/Tim)

I am an employee of Amazon.com, but the opinions expressed here are my own, and no other party necessarily agrees with them.

A full disclosure of my professional interests is on the [author](https://www.tbray.org/ongoing/misc/Tim) page.