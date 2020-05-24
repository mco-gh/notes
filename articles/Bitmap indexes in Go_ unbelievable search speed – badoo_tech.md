Bitmap indexes in Go: unbelievable search speed – badoo_tech

# Bitmap indexes in Go: unbelievable search speed

[![0*NsB-lfw_cUwbJXk4.jpg](../_resources/b34a85122b035805bc47a690d6c807e0.jpg)](https://badootech.badoo.com/@mkevac?source=post_header_lockup)

[Marko Kevac](https://badootech.badoo.com/@mkevac)

Jun 6·19 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='374'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![0*pOq88JTw3wgddB5m](../_resources/801d468582784844e905aa0f525dcbdc.png)

**Foreword**

My name is Marko and I gave a talk at [Gophercon Russia](https://www.gophercon-russia.ru/) this year about a very interesting kind of indexes called “bitmap indexes”. I wanted to share it with the community, not only in video format, but as an article too. Please enjoy!

*> Additional materials, slides and all the source code can be found here:
*> [***> http://bit.ly/bitmapindexes***](http://bit.ly/bitmapindexes)***

***> [***> https://github.com/mkevac/gopherconrussia2019***](https://github.com/mkevac/gopherconrussia2019)

Original video recording:

![](../_resources/b267fd6be59836584dff2c0b26f932e8.png)

Let’s begin!

### Introduction

![](../_resources/4ddf5090aa94ab92d04d4b97d7621c80.png)![0*n1sMEUqHPJNlWOcL](../_resources/106dac2d58770b59a91b545158f32eb0.png)

Today I am going to talk about

- •What indexes are.
- •What a bitmap index is.
- •Where it’s used. Why it’s not used where it’s not used.
- •We are going to see a simple implementation in Go and then have a go at the compiler.
- •Then we are going to look at a slightly less simple, but noticeably faster, implementation in Go assembly.
- •And after that, I am going to address the “problems” of bitmap indexes one by one.
- •And finally, we will see what existing solutions there are.

### So what are indexes?

![](../_resources/24e78e5df06a5251d3adb889b9d8675e.png)![0*jGEFduXMwpdQPLhm](../_resources/c26d37111475a38918506c67ed538a53.png)

An index is a distinct data structure that is kept updated in addition to main data, used to speed up search requests. Without indexes, the search would involve going through all the data (in a process also known as a “full scan”) and that process has linear algorithmic complexity. But databases usually contain huge amounts of data, so linear complexity is too slow. Ideally, we would like to achieve speeds of logarithmic or even constant complexity.

This is an enormous and complex topic involving a lot of tradeoffs, but looking back over decades of database implementations and research I would argue that there are only a few approaches that are commonly used:

![](../_resources/fc993de00d442cf370754e3fc2a0ebe9.png)![0*wIyJJPNPxoIZQmaw](../_resources/95ec8f8ad04bb737656f787dbabe44b3.png)

First, is reducing the search area by cutting the whole area into smaller parts, hierarchically.

Generally, this is achieved using trees. It is similar to having boxes of boxes in your wardrobe. Each box contains materials that are further sorted into smaller boxes, each for a specific use. If we need materials, we would do better to look for the box labelled “material” instead of a box labeled “cookies”.

![](../_resources/b09e69af30e0be9a57536cbac6220600.png)![0*fgZjSIrG7ltfk_76](../_resources/b6e35db650299085a86cf6c4b443208c.png)

Second is to instantly pinpoint a specific element or group of elements as in hash maps or reverse indexes. Using hash maps is similar to the previous example, but you use many smaller boxes which don’t contain boxes themselves, but rather end items.

![](../_resources/102b7035c4d2db54f39d84792df5299b.png)![0*Qp5LGibF9WcrWcc_](../_resources/bc12a90c44ddcc8d7e70a49d63ad01a1.png)

The third approach is removing the need to search at all as in bloom filters or cuckoo filters. Bloom filters can give you an answer straight away and save you the time otherwise spent on searching.

![](../_resources/985ed9353ef1294bed8e9ff5265d3456.png)![0*ls7m-q3im63tz6vo](../_resources/1b5cf67d5904a36eda97604d1c03d06e.png)

The last one is speeding up the search by making better use of our hardware capabilities as in bitmap indexes. Bitmap indexes do sometimes involve going through the whole index, yes, but it is done in a very, efficient manner.

As I already said, searching has a ton of tradeoffs, so often we would use several approaches to improve speed even more or to cover all our potential search types.

Today I would like to speak about one of these approaches that is lesser known: bitmap indexes.

### **But who am I to talk about this subject?**

![](../_resources/13ccd6cdc96003e6feef0e04f2f101d5.png)![0*7Jzwmi-AgrG5bZG0](../_resources/a995beb90913f03c753204e740fda676.png)

I am a team lead at Badoo (maybe you know another one of our brands: Bumble). We have more than 400 million users worldwide and a lot of the features that we have involve searching for the best match for you! For these tasks we use custom-made services that use bitmap indexes, among others.

#### **Now, what is a bitmap index?**

![](../_resources/79764ec96180b645075e64ea5306b8ab.png)![0*XNJVYsfn7S-9epbn](../_resources/1d704c380be96515892279ad5ae2b068.png)

As their name suggests, Bitmap indexes use bitmaps aka bitsets to implement search index. From a bird’s-eye viewpoint this index consists of one or several bitmaps that represent entities (e.g. people) and their parameters (e.g. age, or eye colour) and an algorithm to answer search queries using bitwise operations like AND, OR, NOT, etc.

![](../_resources/93ff3bfe2168beceeb122e5f5edec878.png)![0*zvn4g9zOHxO03XwK](../_resources/ea3f6c59dae3700d441d691036fa82df.png)

Bitmap indexes are considered very useful and high-performing if you have a search that has to combine queries by several columns with low cardinality (perhaps, eye color or marital status) versus something like distance to the city center which has infinite cardinality.

But later in the article I will show that bitmap indexes even work with high cardinality columns.

Let’s look at the simplest example of a bitmap index…

![](../_resources/6c88e87986c072be08c6eb8f1e4784ff.png)![0*YLcKQi16Zqb5ZBzR](../_resources/7649c377c5ca83557c3d7fa3c49a725d.png)

Imagine that we have a list of Moscow restaurants with binary characteristics:

- •near metro
- •has private parking
- •has terrace
- •accepts reservations
- •vegan-friendly
- •expensive

![](../_resources/db22663587a44465f6de7eee18f0e9c1.png)![0*DxX3nB41WMpokAMx](../_resources/fd47ccffb0e4fdc8ec6fc8876dc8a10c.jpg)

Let’s give each restaurant an index starting from 0 and allocate 6 bitmaps (one for each characteristic). Then we would fill these bitmaps according to whether the restaurant has a specific characteristic or not. If the restaurant number 4 has the terrace, then bit number 4 in “terrace” bitmap will be set to 1 (0 if not).

![](../_resources/f26e7fcdd28422efd452294f1c9218d6.png)![0*By4nsL3n7KxTjlIM](../_resources/c5b77167abbab07189ce7fd925b19cfc.png)

We now have the simplest bitmap index possible that we can use to answer questions like:

- •Give me restaurants that are vegan-friendly
- •Give me restaurants with a terrace that accept reservations, but are not expensive

![](../_resources/7367f3dc856c2b9a9a1f7bc49bc9b6cd.png)![0*1-kAgyyUxTGTUrNi](../_resources/c4a133dffd34535bff45db35e1dd742c.png)

![](../_resources/c7f086d1790e93641b39c9a5081c38ea.png)![0*vxu_WA82bnpbpM2P](../_resources/0020a521fde85668615754f20553ef9d.png)

How? Let’s see. The first question is a simple one. We just take “vegan-friendly” bitmap and return all indexes that have bit set.

![](../_resources/731a4cb80a8e50dbfaf210cbb01df905.png)![0*eN8q_wFoqH9DWYlJ](../_resources/61c3c8d2473937489b8a2d2d0d848a81.png)

![](../_resources/8733ec68e0bec91727c7792a41ebab2a.png)![0*McfOWT1qf3zvoteF](../_resources/c0fb5eb0fe5909a1b60e33c529fc55d2.jpg)

The second question is slightly more complicated. We will use bitwise operation NOT on “expensive” bitmap to get non-expensive restaurants, AND it with “accept reservation” bitmap and AND it with “has terrace bitmap”. The resulting bitmap will consist of restaurants that have all these characteristics that we wanted. Here we see that only Yunost has all these characteristics.

![](../_resources/2cb40699fec4271da66d0e23b173b96e.png)![0*8qjCTZwcVdQ7bm5k](../_resources/305d138050c46d30ca644f696aed7cab.jpg)

![](../_resources/da1e86438b5a58ffda4a9dbdc62a4557.png)![0*_27JG0Rqu0-4uyw7](../_resources/70ffbdcbc968a83690525dd4765043ff.jpg)

This may look bit theoretical but don’t worry, we’ll get to the code shortly.

### **Where bitmap indexes are used**

![](../_resources/da92f9910efbf22ca4624e863070573e.png)![0*trgA0G_MHopZAGvd](../_resources/ee0c81e9d29f0353c99fd1b01dfb2ce8.jpg)

If you google “bitmap index”, 90% of the results will point to Oracle DB which has basic bitmap indexes. But, surely, other DBMS use bitmap indexes as well, don’t they? No, actually, they don’t. Let’s go through the usual suspects one by one.

![](../_resources/eab20213f3e420367100d55337641391.png)![0*wkij0o4lpAddsgFz](../_resources/de9ce02ee954e1ba4b4333f856a1bbf1.png)

- •MySQL doesn’t have bitmap indexes yet, but there is a proposal for adding them (https://dev.mysql.com/worklog/task/?id=1524)
- •PostgreSQL doesn’t have bitmap indexes, but they use simple bitmaps and bitwise operations to combine the results of multiple different indexes.
- •Tarantool has bitset indexes and allows very simple searches with them.
- •Redis has bit fields[https://redis.io/commands/bitfield without search ability
- •MongoDB doesn’t have them yet, but there is also a proposal for adding them[(https://jira.mongodb.org/browse/SERVER-1723)](https://jira.mongodb.org/browse/SERVER-1723)
- •Elasticsearch use bitmaps[https://www.elastic.co/blog/frame-of-reference-and-roaring-bitmaps internally

![](../_resources/4ddf4b9dd1752b0c4fce148b47fbbc71.png)![0*-FIZi-YJIP7KsARg](../_resources/e22958af2e2e3afbe7bf7cc009ab13af.png)

- •But there is a new boy on the block: Pilosa. Pilosa is a new DBMS written in Go (notice there is no R, it’s not relational) that bases everything on bitmap indexes. And we will talk about Pilosa later.

#### **Implementation in Go**

But why? Why are bitmap indexes so rarely used? Before answering that question, I would like to walk you through basic bitmap index implementation in Go.

![](../_resources/cce01226b0fb0fbd3f9ce87fd470c742.png)![0*ZnjUaJW_kWhy54nM](../_resources/e988ac00103aaf17c882b974dcee6ef1.jpg)

Bitmap is represented as a chunk of memory. In Go let’s use slice of bytes for that.

We have one bitmap per restaurant characteristic. Each bit in a bitmap represents whether a particular restaurant has this characteristic or not.

![](../_resources/da062fb621ef79329dd529e4e5b1395c.png)![0*W1Af_uBuXVgeSiKJ](../_resources/1a5363f4f8bac9129700415b1b446a2d.jpg)

We would need two helper functions. One is used to fill the bitmap randomly, but with a specified probability of having the characteristic. For example, I think that there are very few restaurants that don’t accept reservations and approximately 20% are vegan-friendly.

Another function will give us the list of restaurants from a bitmap.

![](../_resources/dfe7c782c2e9cb4ad4191fa3c32df92f.png)![0*N9PwK3IwKc6BTLTk](../_resources/126b9db46cd66f1d4dd774da12f91fac.jpg)

![](../_resources/86539c835f1e45e09c047d7158bd523b.png)![0*MXi7UrtcjaSoZfqz](../_resources/c60c70c2730f397c21ea9edda684baaa.jpg)

In order to answer the question “give me restaurants with a terrace that accept reservations but are not expensive” we would need two operations: NOT and AND.

We can slightly simplify the code by introducing complex operation AND NOT.

We have the functions for each of these. Both functions go through our slices taking corresponding elements from each, doing the operation and writing the result to the resulting slice.

![](../_resources/1b06b0f2245582971076fa04002fbeca.png)![0*Tc7NCsEyMiH-vQg7](../_resources/8c9725dffdd92468ab48c14425d4b010.jpg)

And now we can use our bitmaps and our functions to get the answer.

![](../_resources/122995bbc1717b33e46bd25c9f4e1d77.png)![0*iQi8FKLPlaylzoCa](../_resources/4283748e93648478ea97029cc0f25bd0.jpg)

Performance is not so great here even though our functions are really simple and we saved a lot on allocations by not returning new slice on each function invocation.

After some profiling with pprof, I noticed that go compiler missed one of the very basic optimizations: function inlining.

![](../_resources/d576f4574f20c5f28d7b116ad7b86bf9.png)![0*H5BpdCbkoolovKba](../_resources/60a8800df92d4294e1101c7c10062ae0.jpg)

You see, Go compiler is pathologically afraid of loops through slices and refuses to inline any function that has those.

![](../_resources/6311dbdcaba9250d17a952afce9e89a5.png)![0*7MRKXbEdnDD_7efR](../_resources/a24c5e42e075348fdabe9a9925c617e3.jpg)

But I am not afraid of them and can fool the compiler by using goto for my loop.

![](../_resources/582fd7b4b1b9d2c7f70fde72728d5b6c.png)![0*KhvEPGDIoa8X_EGJ](../_resources/11b0a47a8a3921f42fa72c7b6617c8f1.jpg)

![](../_resources/0d098b082984da080998e5413192e6da.png)![0*zlPxeiC5dELjcrcw](../_resources/2691f23b6eed942e160e46b162c01596.jpg)

As you can see, inlining saved us about 2 microseconds. Not bad!

![](../_resources/95010c51f6e474c470779f4a0f7a5439.png)![0*xptehPooJI4Eerls](../_resources/d8593b07d36be2d46be79662014d26e2.jpg)

Another bottleneck is easy to spot when you take a closer look at assembly output. Go compiler included range checks in our loop. Go is a safe language and the compiler is afraid that my three bitmaps might have different lengths and there might be a buffer overflow.

Let’s calm the compiler down and show it that all my bitmaps are the same length. To do that, we can add a simple check at the beginning of the function.

![](../_resources/cb7e29b3a7fe95f5cc104a1b21b4d761.png)![0*wIFvhT8jz600wJbW](../_resources/00aae1e664c11630895e6c851cc3e4e1.jpg)

With this check, go compiler will happily skip range checks and we will save a few nanoseconds.

**Implementation in Assembly**

Alright, so we managed to squeeze a little bit more performance by our simple implementation, but this result is far, far worse than what is possible with current hardware.

You see, what we are doing are very basic bitwise operations and our CPUs are very effective with those.

Unfortunately, we are feeding our CPU with very small chunks of work. Our function does operations byte by byte. We can easily tweak our implementation to work with 8-byte chunks by using slices of uint64.

![](../_resources/1158d76fa1897a2ebba973e16be03eb4.png)![0*AU4aNcmV5G6wgiXQ](../_resources/162bb3631983174d98c304decd1b78ef.jpg)

As you can see here, we gained about 8x performance for 8x batch size, so the performance gains are pretty much linear.

![](../_resources/ce20b8a6a890ce4f74eaa38ef66b4714.png)![0*YBa4hEDmrERUbdEI](../_resources/cdd46ab54d5276d438c229f6c683e1ac.jpg)

![](../_resources/17df17caa9336c17e3466c86a8b5befd.png)![0*74BzjcX7F90kX8Jq](../_resources/1dd52f4680a334b5d5fe5538fb90de1a.jpg)

But this isn’t the end of the road. Our CPUs have the ability to work with chunks of 16-byte, 32-byte and even with 64-byte chunks. These operations are called SIMD (Single Instruction Multiple Data) and the process of using such CPU operations is called vectorization.

Unfortunately, Go compiler is not very good with vectorization. And the only thing we can do nowadays to vectorize our code is to use Go assembly and to add these SIMD instructions ourselves.

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![0*6CajDDgUmcB3QKD_](../_resources/71aa203172179628f42c1544faaec369.png)

Go assembly is a strange beast. You’d think that assembly is something that is tied to the architecture you are writing for, but Go’s assembly is more like IRL (intermediate representation language): it is platform-independent. Rob Pike gave an amazing talk on this a few years ago.

Additionally, Go uses an unusual plan9 format which is unlike both AT&T and Intel formats.

![](../_resources/6fbf3241e334507741606eac13f867b8.png)![0*OqoCE05VP9O-dUyx](../_resources/409fafe50f63dce1208e14f3bd8ddcfe.png)

It is safe to say that writing Go assembly code is no fun.

Luckily for us, there are already two higher-level tools to help with writing Go assembly: PeachPy and avo. Both of these generate go assembly from a higher-level code written in Python and Go respectively.

![](../_resources/06fa2ec4bb1612359d495fac6b2c73ef.png)![0*1CmGb76frO94QbFh](../_resources/083ae2fe4488e7afec57f8459fd1615d.jpg)

These tools simplify things like register allocation and loops and all in all reduce the complexity of entering the realm of assembly programming for Go.

We will use avo for this post so our programs look almost like ordinary Go code.

![](../_resources/fbddc36576d5224584d23cc70dabaff9.png)![0*GVXh4Rf4giKZ_yNq](../_resources/5560be11361b0d503bf5c246c9709d84.jpg)

This is the simplest example of an avo program. We have a main() function that defines a function called Add() that adds two numbers. There are helper functions to get parameters by name and to get one of the available general registers. There are functions for each assembly operation like ADDQ here, and there are helper functions to save the result from a register to the resulting value.

![](../_resources/4bc6a8603f5b91a2c94e47b5da3686b0.png)![0*ffE86wYHvnqZPwB-](../_resources/3ffc0dfa61351311d3a7969ed7d173af.jpg)

Calling go generate will execute this avo program and two files will be created

- •add.s with generated assembly code
- •stub.go with function headers that are needed to connect our go and assembly code

![](../_resources/5c9b974a45404e1f7854384e4efeedd9.png)![0*TlzQaUGxmnnONdj0](../_resources/b808383d7889cb555c2534c66f2cb835.jpg)

Now that we’ve seen what avo does, let’s look at our functions. I’ve implemented both scalar and SIMD (vector) versions of our functions.

Let’s see what the scalar version looks like first.

![](../_resources/0371deaf444faf25fe8c7586ec66d194.png)![0*VFZbVjm5w-vGKeum](../_resources/9f494768a304d601784600648ef00ce6.jpg)

As in a previous example, we can ask for a general register and avo gives us the right one that’s available. We don’t need to track offsets in bytes for our arguments, avo does this for us.

![](../_resources/2b5bfcb4df19f32dd0a7065fd8954639.png)![0*oM9YOBiljDW8nWkd](../_resources/406a6ba294d1cb45963ad1ed818a5a6c.jpg)

Previously we switched from loops to using goto for performance reasons and to deceive go compiler. Here, we are using goto (jumps) and labels right from the start because loops are higher-level constructs. In assembly we only have jumps.

![](../_resources/8e53c8baea656184af39baaeeba1952d.png)![0*OsTuVAKomzQ_y_J3](../_resources/ff3e00ddcad230f1a4ac869922a43022.jpg)

Other code should be pretty clear. We emulate the loop with jumps and labels, take a small part of our data from our two bitmaps, combine it using one of the bitwise operations and insert the result into the resulting bitmap.

![](../_resources/1de93d05c574870b48b96d21b8c58eae.png)![0*njtPyYz42QFqSc-G](../_resources/e0c43d517fa6450ab0ceb052026f518a.jpg)

This is a resulting asm code that we get. We didn’t have to calculate offsets and sizes (in green), we didn’t have to deal with specific registers (in red).

![](../_resources/3cfcb1774e4eb2a1bd65c63f9e9c6391.png)![0*d0DL2ok-t7RS45Hy](../_resources/6e672e06f8dc58102515497ef2810f79.jpg)

If we compared this implementation in assembly with the previous best one written in go we would see that the performance is the same as expected. We didn’t do anything differently.

Unfortunately, we cannot force Go compiler to inline our functions written in asm. It completely lacks support for it and the request for this feature has existed for some time now. That’s why small asm functions in go give no benefit. You either need to write bigger functions, use new package math/bits or skip asm altogether.

Let’s write vector version of our functions now.

![](../_resources/97ace2f5cb6df2f62dc0c3397e5d3bca.png)![0*Lm7HRr8aJQQjAMtX](../_resources/7f8272c6652471c04b70b84552a8ca0e.jpg)

I chose to use AVX2, so we are going to use 32-byte chunks. It is very similar to the scalar in structure. We load out parameters, ask for general registers, etc.

![](../_resources/4057ec54bd9943392ccc6ab9f3996e15.png)![0*FehNjUj2flg0DlcV](../_resources/f4ac46e0d7375e32e497ec0ede5ceefd.jpg)

One of the changes has to do with the fact that vector operations use specific wide registers. For 32 bytes they have Y prefix, this is why you see YMM() there. For 64-byte they would have had Z prefix.

Another difference has to do with the optimisation I performed called unrolling or loop unrolling. I chose to partially unroll our loop and to do 8 loop operations in sequence before looping back. This technique speeds up the code by reducing the branches we have and it’s pretty much limited by the number of registers we have available.

![](../_resources/162bf6f419db98c3df42ff17ff015b7a.png)![0*c4b4iZeU6e4e5RDB](../_resources/ad1766af1a97b5b5b68b3284a788c852.jpg)

As for performance… it’s amazing. We got about 7x improvement comparing to the previous best. Pretty impressive, right?

![](../_resources/cb29fd0600b0be72f5faf40920b0d4ed.png)![0*UDISXbkbUQilMDsu](../_resources/86161c30a87168da72a5d8ab0a496be6.jpg)

It should be possible to improve these results even more by using AVX512, prefetching and maybe even by using JIT (just in time) compilation instead of “manual” query plan builder, but that would be a subject for a totally different post.

### **Bitmap Index problems**

Now that we’ve seen the basic implementation and the impressive speed of asm implementation, let’s talk about the fact that bitmap indexes are not very widely used. Why is that?

![](../_resources/c7977fa6cc07e509270f3da14a1d6120.png)![0*5Oyi5qQgermJmXaH](../_resources/3f25ea914c24e4d0457fc40751011f80.png)

Older publications give us these three reasons. But I would argue that recent ones have been “fixed” or dealt with by now. I won’t go into a lot of detail on this here because we don’t have much time, but it’s certainly worth a quick look.

### **High-cardinality problem**

So, we’ve been told that bitmap indexes are feasible only for low-cardinality fields. i.e. fields that have few distinct values, such as gender or eye color. The reason is that common representation (one bit per distinct value) can get pretty big for high-cardinality values. And, as a result, bitmap can become huge even if sparsely populated.

![](../_resources/481b6edf3937fc199ba1e69ccf1d5348.png)![0*5dwdVCE3wSgY8u_d](../_resources/e4056e2b85d0781ae5d10d0198255f68.jpg)

![](../_resources/ad0a9374b91e1bcc2cfeae08afbbe793.png)![0*tr2yfC_csriJ-30Y](../_resources/e9c48122aef721b2d1332b598c769214.jpg)

Sometimes a different representation can be used for these fields such as a binary number representation as shown here, but the biggest game changer is a compression. Scientists have come up with amazing compression algorithms. Almost all are based on widespread run-length algorithms, but what is more amazing is that we don’t need to decompress bitmaps in order to do bitwise operations on them. Normal bitwise operations work on compressed bitmaps.

![](../_resources/658ece5f4b263b2f450aa188ed1c1587.png)![0*vIOfJqFPPzK9U19W](../_resources/296e29b18fe6f24d210382607e166ead.jpg)

Recently, we’ve seen hybrid approaches appear like “roaring bitmaps”. Roaring bitmaps use three separate representations for bitmaps: bitmaps, arrays and “bit runs” and they balance usage of these three representations both to maximise speed and to minimise memory usage.

Roaring bitmaps can be found in some of the most widely-used applications out there and there are implementations for a lot of languages, including several implementations for Go.

![](:/a2dc400c0e7acc90dab84c509aad610f)![0*Mmuse8C9LIXPrI2J](../_resources/4b38a21d8ba9e8f602c3e73b1be7c164.jpg)

Another approach that can help with high-cardinality fields is called binning. Imagine that we have a field representing a person’s height. Height is a float, but we don’t think of it that way. Nobody cares if your height is 185.2 or 185.3 cm. So we can use “virtual bins” to squeeze similar heights into the same bin: the 1 cm bin, in this case. And if you assume that there are very few people with a height of less than 50 cm, or more than 250 cm, we can convert our height into the field with approximately 200 element cardinality, instead of an almost infinite cardinality. If needed, we could do additional filtering on results later.

### **High-throughput problem**

Another reason why bitmap indexes are bad is that it can be expensive to update bitmaps.

Databases do updates and searches in parallel, so you must be able to update the data while there might be hundreds of threads going through bitmaps doing a search. Locks would be needed in order to prevent data races or data consistency problems. And where there’s a one big lock, there is lock contention.

![](../_resources/f38c4ac5b2c36c18814a8236c5022d20.png)![0*gGRUvAfmqxNjS8RY](../_resources/9396824cbf5d9f45ba80d2581db8aaa2.png)

This problem, if you do have it, can be fixed by sharding your indexes or by having index versions, if appropriate.

Sharding is straightforward. You shard them as you would shard users in a database and now, instead of one lock, you have multiple locks which greatly reduces your lock contention.

Another approach that is sometimes feasible is having versioned indexes. You have the index that you use for search and you have an index that you use for writes, for updates. And you copy and switch them at a low frequency, e.g. 100 or 500 ms.

But this approach is only feasible if your app is able to tolerate stale search indexes that are a bit stale.

Of course, these two approaches can also be used together. You can have sharded versioned indexes.

### **Non-trivial queries**

Another bitmap index problem has to do with using bitmap indexes with range queries. And at first glance bitwise operations like AND and OR don’t seems to be very useful for range queries like “give me hotel rooms that cost from 200 to 300 dollars a night”.

![](../_resources/e21a0ddf4e28ac7b8b7a48b026af2918.png)![0*XBlUS1TyqlChQ2QB](../_resources/eff18fc45f506faffea0a141b030e024.jpg)

A naive and very inefficient solution would be to get results for each price point from 200 to 300 and to OR the results.

![](../_resources/0801f19e74a4ff44c1d1400efa5ca786.png)![0*aQc9mk9xKIuldT6s](../_resources/7a7ea07b526526514023bdc721595f48.jpg)

A slightly better approach would be to use binning and to put our hotels into price ranges with range widths of, let’s say, 50 dollars. This approach would reduce our search expenses by approximately 50x.

But this problem can also be solved very easily by using a special encoding that makes range queries possible and fast. In the literature, such bitmaps are called range-encoded bitmaps.

![](../_resources/9a7b0cb739589d73060ba0ab311c130a.png)![0*uNarsAJElfdIqgC_](../_resources/3ba34a1e6021bc79473d3c07185e8df6.jpg)

In range-encoded bitmaps we don’t just set specific bit for, let’s say, value 200, but set all the bits at 200 and higher. The same for 300.

So, by using this range-encoded bitmap representation range query can be answered with only two passes through bitmap. We get all the hotels that cost less than, or equal to, 300 dollars and remove from the result all the hotels that cost less than, or equal to, 199 dollars. Done.

![](../_resources/c8faa37387aa892bc612038f263ae956.png)![0*aqU792i53SE0Rj-v](../_resources/c36221482347965c8bc2ea99d4e9c55f.jpg)

You would be amazed but even geo queries are possible using bitmaps. The trick is to use representation like Google S2 or similar that encloses a coordinate in a geometric figure that can be represented as three or more indexed lines. If you use such representation, you can then represent geo query as several range queries on these line indexes.

### **Ready solutions**

Well, I hope that I’ve piqued your interest a bit. You now have one more tool under your belt and if you ever need to implement something like this in your service, you’ll know where to look.

That’s all well and good, but not everybody has the time, patience and resources to implement bitmap index themselves, especially when it comes to more advanced stuff like SIMD instructions.

Fear not, there are two open source products that can help you in your endeavour.

![](../_resources/93172908c60b54366f62a6fb9c505e80.png)![0*pW5YxLNGgi65Wdjj](../_resources/6f5985984034d5d7aefcf6d50567911a.jpg)

### **Roaring bitmaps**

First, there is a library that I’ve already mentioned called “roaring bitmaps”. This library implements roaring “container” and all bitwise operations that you would need if you were to implement a full bitmap index.

![](../_resources/54d005b88f396c68d1210ff38edc8fef.png)![0*FI69GhuuD3iqmrD2](../_resources/179cc28df5cebb873633e4409e926760.jpg)

Unfortunately, go implementations don’t use SIMD, so they give a somewhat lesser performance than, say, C implementation.

### **Pilosa**

Another product is a DBMS called Pilosa that only has bitmap indexes. It’s a recent project, but it’s gained a lot of traction lately.

![](../_resources/de7bc88637325fdebd3038ea514990b3.png)![0*_qHPuDib55-Jt1j-](../_resources/cff9b43a64f937ddb092f824afac359c.jpg)

Pilosa uses roaring bitmaps underneath and gives, simplifies or explains almost all the things I’ve been telling you about today: binning, range-encoded bitmaps, the notion of fields, etc.

Let’s briefly look at an example of Pilosa in use…

![](../_resources/a8d7a8705c6b83a93d5f305f14e1bc25.png)![0*ECqPuiMZV1CQJsfU](../_resources/c61cbc890c343dafa1c8606fda0439ad.jpg)

The example you see is very, very similar to what we saw earlier. We create a client to the pilosa server, create an index and fields for our characteristics. We populate the fields with random data with some probabilities as we did earlier and then we execute our search query.

You see the same basic pattern here. NOT expensive intersected or AND-ed with terrace and intersected with reservations.

The result is as expected.

![](../_resources/0906b024c103030ef91e99a56ae149b6.png)![0*yOct2eN4zCGthgfZ](../_resources/86e22f4763bbb9237da2397a0881fab7.jpg)

And lastly, I am hoping that sometime in the future, databases like mysql and postgresql will get a new index type: bitmap index.

![](../_resources/9f690de46b649a89010c94d8d854c8b4.png)![0*G3u5gR32h4-TZ9YC](../_resources/b289c5f95069f0b8e7012b179f71b4b4.jpg)

**Closing words**

![](../_resources/b6917f5ec838da0cb6a87f935c00128d.png)![0*LT0Xh5LPnz_BzfQg](../_resources/ca0476fe0e0a7a9e7aef2223e8a0e2eb.jpg)

And if you are still awake, I thank you for that. Shortage of time has meant I’ve had to skim over a lot of the stuff in this post, but I hope it’s been useful and maybe even inspiring.

Bitmap indexes are a useful thing to know about and understand even if you don’t need them right now. Keep them as yet another tool in your portfolio.

During my talk, we’ve seen various performance tricks we can use and things which Go struggles with at the moment. These are definitely things that every Go programmer out there needs to know.

And this is all I have for you for now. Thank you very much!