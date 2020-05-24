I Wrote The Fastest Hashtable

### I Wrote The Fastest Hashtable

#### by Malte Skarupke

I had to get there eventually. I had a blog post called “[I Wrote a Fast Hashtable](https://probablydance.com/2014/05/03/i-wrote-a-fast-hash-table/)” and another blog post called “[I Wrote a Faster Hashtable](https://probablydance.com/2014/05/31/i-wrote-a-faster-hash-table/).” Now I finally wrote the fastest hashtable. And by that I mean that I have the fastest lookups of any hashtable I could find, while my inserts and erases are also really fast. (but not the fastest)

The trick is to use Robin Hood hashing with an upper limit on the number of probes. If an element has to be more than X positions away from its ideal position, you grow the table and hope that with a bigger table every element can be close to where it wants to be. Turns out that this works really well. X can be relatively small which allows some nice optimizations for the inner loop of a hashtable lookup.

If you just want to try it, here is a [download link](https://github.com/skarupke/flat_hash_map/blob/master/flat_hash_map.hpp). Or scroll down to the bottom of the blog post to the section “Source Code and Usage.” If you want more details read on.

## Type of Hashtable

There are many types of hashtables. For this one I chose

- Open addressing
- Linear probing
- Robing hood hashing
- Prime number amount of slots (but I provide an option for using powers of two)
- With an upper limit on the probe count

I believe that the last of these points is a new contribution to the world of hashtables. This is the main source of my speed up, but first I need to talk about all the other points.

Open addressing means that the underlying storage of the hashtable is a contiguous array. This is not how std::unordered_map works, which stores every element in a separate heap allocation.

Linear probing means that if you try to insert an element into the array and the current slot is already full, you just try the next slot over. If that one is also full, you pick the slot next to that etc. There are known problems with this simple approach, but I believe that putting an upper limit on the probe count resolves that.

Robin Hood hashing means that when you’re doing linear probing, you try to position every element such that it is as close as possible to its ideal position. You do this by moving objects around whenever you insert or erase an element, and the method for doing that is that you take from rich elements and give to poor elements. (hence the name Robin Hood hashing) A “rich” element is an element that received a slot close to its ideal insertion point. A “poor” element is one that’s far from its ideal insert point. When you insert a new element using linear probing you count how far you are from your ideal position. If you are further from your ideal position than the current element, you swap the new element with the existing element and try to find a new spot for the existing element.

The prime number amount of slots means that the underlying array has a prime number size. Meaning it grows for example from 5 slots to 11 slots to 23 slots to 47 slots etc. Then to find the insertion point you simply use the modulo operator to assign the hash value of an element to a slot. The other most common choice is to use powers of two to size your array. Later in this blog post I will go more into why I chose prime numbers by default and when you want to use which.

## A Upper Limit for the Probe Count

With the basics out of the way, let’s talk about my new contribution: Limiting how many slots the table will look at before it gives up and grows the underlying array.

My first idea was to set this to a very low number, say 4. Meaning when inserting I try the ideal slot and if that doesn’t work I try the next slot over, the next slot over, the slot after that and if all of them are full I grow the table and try inserting again. This works great for small tables, but when I insert random values into a large table, I would get unlucky all the time and hit four probes and I would have to grow the table even though it was mostly empty.

Instead I found that using log2(n) as the limit, where n is the number of slots in the table, makes it so that the table only has to reallocate once it’s roughly two thirds full. That is when inserting random values. When inserting sequential values the table can be filled up completely before it needs to reallocate.

Even though I found that the table can fill up to roughly two thirds, every now and  then it would have to reallocate when it’s only 60% full. Or rarely even when it’s only 55% full. So I set the max_load_factor of the table to 0.5. Meaning the table will grow when its half full, even when it hasn’t reached the limit of the probe count. The reason for that is that I want a table that you can trust to reallocate only when you actually grow it: If you insert a thousand elements, then erase a couple elements and then insert that same number of elements again, you can be almost certain that the table won’t reallocate. I can’t put a number on the certainty, but I ran a simple test where I built thousands of tables of all kinds of sizes and filled them with random integers. Overall I inserted hundreds of billions of integers into the tables, and they only reallocated at a load factor of less than 0.5 once. (that time the table grew when it was 48% full, so it grew slightly too soon) So I think you can trust that this will very, very rarely reallocate when you weren’t expecting it.

That being said if you don’t need control over when the table grows, feel free to set the max_load_factor higher. It’s totally safe to set it to 0.9: Robin hood hashing combined with the maximum probe count will ensure that all operations remain fast. Don’t set it to 1.0 though: You can get into bad situations when inserting then because you might hit a case where every single element in the table has to be shifted around when inserting the last element. (say every element is in the slot it wants to be, except the very last slot is empty. Then you insert an element that wants to be in the first slot, but the first slot is already full. So it will go into the second slot, pushing the second element one over, which will push the third element one over etc. all the way through the table until the element in the second to last slot gets pushed into the last slot. You now have a table where every element except for the first is one slot from its ideal slot so lookups are still really fast, but that last insert took a long time) By keeping a few empty slots around you can ensure that newly inserted elements only have to move a few elements over until one of them finds an empty slot.

So if I set the max_load_factor so low that I never reach the probe count limit anyway, why have the limit at all? Because it allows a really neat optimization: Let’s say you rehash the table to have 1000 slots. My hashtable will then grow to 1009 slots because that’s the closest prime number. The log2 of that is 10, so I set the probe count limit to 10. The trick now is that instead of allocating an array of 1009 slots, I actually allocate an array of 1019 slots. But all other hash operations will still pretend that I only have 1009 slots. Now if two elements hash to index 1008, I can just go over the end and insert at index 1009. I never have to do any bounds checking because the probe count limit ensures that I will never go beyond index 1018. If I ever have eleven elements that want to go into the last slot, the table will grow and all those elements will hash to different slots. Without bounds checking, my inner loops are tiny. Here is what the find function looks like:

1
2
3
4
5
6
7
8
9
10
11
12
[object Object][object Object]  [object Object]
[object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]
[object Object]

It’s basically a linear search. The assembly of this code is beautiful. This is better than simple linear probing in two ways: 1. No bounds checking. Empty slots have -1 in their distance_from_desired value so the empty case is the same case as finding a different element. 2. This will do at most log2(n) iterations through the loop. Normally the worst case for looking things up in a hashtable is O(n). For me it’s O(log n). This makes a real difference. Especially since linear probing actually makes it pretty likely that you will hit the worst case since linear probing tends to bunch elements together.

My memory overhead on this is one byte per element. I store the distance_from_desired in an int8_t. That being said that one byte will be padded out to the alignment of the type that you insert. So if you insert ints, the one byte will get three bytes of padding so there is four bytes of overhead per element. If you insert pointers there will be 7 bytes of padding so you get eight bytes of overhead per element. I’ve thought about changing my memory layout to solve this, but my worry is that then I would have two cache misses for each lookup instead of one cache miss. So the memory overhead is one byte per element plus padding. Oh and with a max_load_factor of 0.5 (which is the default) your table will only be between 25% and 50% full, so there is more overhead there. (but once again it’s safe to increase the max_load_factor to 0.9 to save memory while only suffering a small decrease in speed)

## Lookup Performance

Measuring hash tables is actually not easy. You need to measure at least these cases:

1. Looking up an element that’s in the table
2. Looking up an element that can not be found in the table
3. Inserting a bunch of random numbers
4. Inserting a bunch of random numbers after calling reserve()
5. Erasing elements

And you need to run each of these with different keys and different sizes of values. I use an int or a string as the key, and I use value types of size 4, 32 and 1024. I will prefer to use int keys because with strings you’re mostly measuring the overhead of the hash function and the comparison operator, and that overhead is the same for all hash tables.

The reason for testing both successful lookups and unsuccessful lookups is that for some tables there is a huge difference in performance between these cases. For example I came across a really bad case when inserting all the numbers from 0 to 500000 into a google::dense_hash_map (meaning they were not random numbers) and then did unsuccessful lookups: The hashtable suddenly was five hundred times slower than it usually is. This is a edge case of using a power of two for the size of the table. I’ll go more into when you should pick powers of two and when you should pick prime numbers below. This example suggests that maybe I should measure each of these with random numbers and with sequential numbers, but that ended up being too many graphs. So I will only test tables with random numbers which should prevent bad cases caused by specific patterns.

The first graph is looking up an element that’s in the table:
![successful_lookup](../_resources/7482fc91f63962cfdacd73a44d159cb5.png)

This is a pretty dense graph so let’s spend some time on this one. flat_hash_map is the new hash table I’m presenting in this blog post. flat_hash_map_power_of_two is that same hash table but using powers of two for the array size instead of prime numbers. You can see that it’s much faster and I’ll explain why that is below. dense_hash_map is google::dense_hash_map which is the fastest hashtable I could find. sherwood_map is my old hashtable from my “I Wrote a Faster Hashtable” blog post. It’s embarrassingly slow… std::unordered_map and boost::unordered_map are self-explanatory. multi_index is boost::multi_index.

I want to talk about this graph a little. The Y-axis is the number of nanosecons that it takes to look up a single item. I use google benchmark and that calls table.find() over and over again for half a second, and then counts how many times it was able to call that function. You get nanoseconds by dividing the time that all iterations took together by the loop count. All the keys I’m looking for are guaranteed to be in the table. I chose to use a log scale for the X axis because performance tends to change on a log scale. Also this makes it possible to see the performance at different scales: If you care about small tables, you can look at the left side of the graph.

The first thing to notice is that all of the graphs are spiky. This is because all hashtables have different performance depending on the current load factor. Meaning depending on how full they are. When a table is 25% full lookups will be faster than when it’s 50% full. The reason for this is that there are more hash collisions when the table is more full. So you can see the cost go up until at some point the table decides that it’s too full and that it should reallocate, which makes lookups fast again.

This would be very clear if I were to plot the load factors of each of these tables. One more thing that would be clear is that the tables at the bottom have a max_load_factor of 0.5, the tables at the top have a max_load_factor of 1.0. This immediately raises the question of “wouldn’t those other tables also be faster if they used a max_load_factor of 0.5?” The answer is that they would only be a little faster, but I will answer that question more fully with a different graph further down. (but just from the graph above you can see that the lowest point of the upper graph, when those tables have just reallocated and have a load factor of just over 0.5 is far over the highest point of the lower graphs, just before they reallocate because their load factor is just under 0.5)

Another thing that we notice is that all the graphs are essentially flat on the left half of the screen. This is because the table fits entirely into the cache. Only when we get to the point where the data doesn’t fit into my L3 cache do we see the different graphs really diverge. I think this is a big problem. I think the numbers on the right are far more realistic than the numbers on the left. You will only get the numbers on the left if the element you’re looking for is already in the cache.

So I tried to come up with a test that would measure how fast the table would be if it wasn’t in the cache: I create enough tables so that they don’t all fit into L3 cache and I use a different table for every element that I look up. Let’s say I want to measure a table that has 32 elements in it and the elements in the table are 8 bytes in size. My L3 cache is 6 mebibytes so I can fit roughly 25000 of these tables into my L3 cache. To be sure that the tables won’t be in the cache I actually create three times that number, meaning 75000 tables. And each lookup is from a different table. That gives me this graph:

![successful_lookup_cache_miss.png](../_resources/9834aa8d4602e5a3b99c91cc664a5430.png)

First, I removed a couple of the lines because they didn’t add much information. boost::unordered_map is usually the same speed as std::unordered_map (sometimes it’s a little faster, but it’s still always above everything else) and nobody cares about my old slow hash table sherwood_map. So now we’re left with just the important ones: std::unordered_map as a normal node based container, boost::multi_index as a really fast node based container, (I believe that std::unordered_map could be this fast) google::dense_hash_map as a fast open addressing container, and my new container in its prime number version and its power of two version.

So in this new benchmark, where I try to force a cache miss, we can see big differences very early on. What we find is that the pattern that we saw at the end of the last graph emerges very early in this graph: Starting at ten elements in the table there are clear winners in terms of performance. This is actually pretty impressive: All of these hash tables maintain consistent performance across many different orders of magnitude.

Let’s also look at the graph for unsuccessful lookups: Meaning trying to find an item that is not in the table:

![unsuccessful_lookup_cache_miss](../_resources/10db80f8642884831dc3b8931756f451.png)

When it comes to unsuccessful lookups the graph is even more spiky: The load factor really matters here. The more full a table is the more elements the search has to look at before it can conclude that an item is not in the table. But I’m actually really happy about how my new table is doing here: Limiting the probe count seems to work. I get more consistent performance than any other table.

What I take from these graphs is that my new table is a really big improvement: The red line, with the powers of two, is my table configured the same way as dense_hash_map: With max_load_factor 0.5 and using a power of two to size the table so that a hash can be mapped to a slot just by looking at the lower bits.  The only big difference is that my table requires one byte of extra storage (plus padding) per slot in the table. So my table will use slightly more memory than dense_hash_map.

The surprising thing is that my table is as fast as dense_hash_map even when using prime numbers to size the table. So let me talk about that.

## Prime Numbers or Powers of Two

There are three expensive steps in looking up an item in a hashtable:
1. Hashing the key
2. Mapping the key to a slot
3. Fetching the memory for that slot

Step 1 can be really cheap if your key is an integer: You just cast the int to a size_t. But this step can be more expensive for other types, like strings.

Step 2 is just an integer modulo.

Step 3 is a pointer dereference, for std::unordered_map it’s actually multiple pointer dereferences.

Intuitively you would expect that if you don’t have a very slow hash function, step 3 is the most expensive of these three. But if you’re not getting cache misses for every single lookup, chances are that the integer modulo will end up being your most expensive operation. Integer modulo is really slow, even on modern hardware. The [Intel manual](https://software.intel.com/sites/default/files/managed/9e/bc/64-ia-32-architectures-optimization-manual.pdf) lists it as taking between 80 and 95 cycles.

This is the main reason why really fast hash tables usually use powers of two for the size of the array. Then all you have to do is mask off the upper bits, which you can do in one cycle.

There is however one big problem with using a power of two: There are many patterns of input data that result in lots of hash collisions when using powers of two. For example here is that last graph again, except I didn’t use random numbers:

![unsuccessful_sequential.png](../_resources/7d8bfe28c87b08e3a43d06a96b587c7f.png)

Yes you see correctly that google::dense_hash_map just takes off into the stratosphere. What pattern of inputs did I have to use to get such poor performance out of dense_hash_map? It’s just sequential numbers. Meaning I insert all numbers [0, 1, 2, …, n – 2, n – 1]. If you do that, trying to look up a key that’s not in the table will be super slow. Successful lookups will still be fine. But if some of your lookups are for keys that are in the table and some are for keys that are not, then you might find that some of your lookups are a thousand times slower than others.

Another example of bad performance due to using powers of two is how the standard hashtable in Rust was [accidentally quadratic](http://accidentallyquadratic.tumblr.com/post/153545455987/rust-hash-iteration-reinsertion) when inserting keys from one table into another. So using powers of two can bite you in non-obvious ways.

It just so happens that my hashtable doesn’t suffer from either of these problems: The limit of the probe count resolves both of these problems in the best way possible. The table doesn’t even have to reallocate unnecessarily. Does that mean that I’m immune against problems that come from using powers of two? No. For example one problem that I have personally experienced in the past is that when you insert pointers into a hash table that uses powers of two, some slots will never be used. The reason is heap allocations in my program were sixteen byte aligned and I used a hash function that just reinterpret_casted the pointer to a size_t. Because of that only one out of sixteen slots in my table was ever used. You would run into the same problem if you use the power of two version of my new hashtable.

All of these problems are solvable if you’re careful about choosing a hash function that’s appropriate for your inputs. But that’s not a good user experience: You now always have to be vigilant when using hashtables. Sometimes that’s OK, but sometimes you just want to not have to think too much about this. You just want something that works and doesn’t randomly get slow. That’s why I decided to make my hashtable use prime number sizes by default and to only give an option for using powers of two.

Why do prime numbers help? I can’t quite explain the math behind that, but the intuition is that since the prime number doesn’t share common divisors with anything, all numbers get different remainders. For example let’s say I’m using powers of two, my hashtable has 32 slots, and I am trying to insert pointers which are all sixteen byte aligned. (meaning all my numbers are multiples of sixteen) Now using integer modulo to find a slot in the table will only ever give me two possible slots: slot 0 or  slot 16. Since 32 is divisible by 16, you simply can’t get more possible values than that. If I use a prime numbered size instead I don’t run into that problem. For example if I use the prime number 37, then all divisions using multiples of sixteen give me different slots in the table, and I will use all 37 slots. (try doing the math and you will see that the first 37 multiples of 16 all would end up in different slots)

So then how do we solve the problem of the slow integer modulo? For this I’m using a trick that I copied from boost::multi_index: I make all integer modulos use a compile time constant. I don’t allow all possible prime numbers as sizes for the table. Instead I have a selection of pre-picked prime numbers and will always grow the table to the next largest one out of that list. Then I store the index of the number that your table has. When it later comes time to do the integer modulo to assign the hash value to a slot, you will see that my code does this:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
[object Object][object Object]
[object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]
[object Object]
[object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object]

Each of these cases is a integer modulo by a compile time constant. Why is this a win? Turns out if you do a modulo by a constant, the compiler knows a bunch of tricks to make this fast. You get custom assembly for each of these cases and that custom assembly will be much faster than an integer modulo would be. It looks kinda crazy but it’s a huge speed up.

You can see the difference in the graphs above: Using prime numbers is a little bit slower, but it’s still really fast when compared to other hash tables, and you’re immune against most bad cases of hash tables. Of course you’re never immune against all bad cases. If you really worry about that, you should use std::map with its strict upper bounds. But the difference is that when using powers of two, there are many bad cases and you have to be careful not to stumble into them. When using prime numbers you will basically only hit a bad case if you intentionally create bad keys.

That brings up security: A clever attack that you can do on hash tables is that you insert keys that all collide with each other. How might you do that? If you know that a website uses a hashtable in its internal caches, then you could engineer website requests such that all your requests will collide in that hashtable. Like that you can really slow down the internal cache of a webserver and possibly bring down the website. So for example if you know that google uses dense_hash_map internally and you see the graph above where it gets really slow if you insert sequential numbers, you could just request sequential websites and hope that that pollutes their cache. You might think that setting an upper limit on the probe count prevents attackers from filling up your table with bad keys. That is true: My hashtable will not suffer from this problem. However a new attack immediately presents itself: If you know which prime numbers I use internally you could insert keys in an order so that my table repeatedly hits the limit of the probe count and has to repeatedly reallocate. So the new attack is that you can make the server run out of memory. You can solve this by using a custom hash function, but I can’t give you advice for what such a hash function should look like. All I can tell you is that if you use the hashtable in an environment where users can insert keys, don’t use std::hash as your hash function and use something stateful instead that can’t be predicted ahead of time. On the other hand if you don’t think that people will be malicious, you can be confident that using the prime number version of my hashtable will result in an even spread of values and there will be no problems.

But let’s say you know that your hash function returns numbers that are well distributed and that you’re rarely going to get hash collisions even if you use powers of two. Then you should use the power of two version of my table. To do that you have to typedef a hash_policy in your hash function object. I decided to put this customization point into the hash function object because that is the place that actually knows the quality of the returned keys.

So you put this typedef into your custom hash function object:
1
2
3
4
5
6
7
8
9
10
11
[object Object]  [object Object]
[object Object]
[object Object][object Object]  [object Object][object Object]  [object Object]
[object Object][object Object]
[object Object][object Object]
[object Object][object Object]
[object Object][object Object]  [object Object]
[object Object]

[object Object]
[object Object][object Object][object Object]

In your custom hash function you typedef ska::power_of_two_hash_policy as hash_policy. Then my flat_hash_map will switch to using powers of two. Also if you know that std::hash is good enough in your case, I provide a type called power_of_two_std_hash that will just call std::hash but will use the power_of_two_hash_policy:

1
[object Object]

With either of these you can get a faster hashtable if you know that you won’t be getting too many hash collisions.

## Insert and Erase Performance

After that lengthy detour of talking about hash table theory let’s get back to the performance of my table. Here is a graph that measures how long it takes to insert an item into a map. The way I measure this is that I measure how long it takes to insert N elements, then I divide the time by N to get the time that the average element took. The first graph is the speed if I do not call reserve() before inserting:

![insert_no_reserve](../_resources/1cf1d7aceaa215aee266c8942165ea47.png)

This graph is also spiky, but the spikes point in the other direction. Any time that the table has to reallocate the average cost shoots up. Then that cost gets amortized until the table has to reallocate again.

The other point about this graph is that on the left half you once again only have tables that fit entirely in the L3 cache. I decided to not write a cache-miss-triggering test for this one because that would take time and we learned above that just looking at the right half is a good approximation for a cache miss.

Here google::dense_hash_map beats my new hash table, but not by much. My table is still very fast, just not quite as fast as dense_hash_map. The reason for this is that dense_hash_map doesn’t move elements around when inserting. It simply looks for an empty slot and inserts the element. The Robin Hood hashing that I’m using requires that I move elements around when inserting to keep the property that every node is as close to its ideal position as possible. It’s a trade-off where insertion becomes more expensive, but lookups will be faster. But I’m happy with how it seems to only have a small impact.

Next is the time it takes to insert elements if the table had reserve() called ahead of time:

![insert_with_reserve](../_resources/15fefe8eb2d6f1d58329085067b2c8df.png)

I don’t know what’s happening with the node-based containers at the end there. It might be fun to investigate what’s going on there, but I didn’t do that. I actually have a suspicion that that’s due to the malloc call in my standard library. (Linux gcc) I had several problems with it while measuring this graph and others because some operations would randomly take a long time.

But overall this graph looks similar to the last one, except less spiky because the reserve removes the need for reallocations. I have fast inserts, but they’re not as fast as those of google::dense_hash_map.

Finally let’s look at how long it takes to erase elements. For this I built a map of N elements, then measured how long it takes to erase every element in the map in a random order. Then I would divide the time it takes to erase all elements by N to get the cost per element:

![erase.png](../_resources/9ceab1257223979496835ee616ac40eb.png)

The node based containers are slow once again, and the flat containers are all roughly equally fast. dense_hash_map is slightly faster than my hash table, but not by much: It takes roughly 20 nanoseconds to erase something from dense_hash_map and it takes roughly 23 nanoseconds to erase something from my hash table. Overall these are both very fast.

But there is one big difference between my table and dense_hash_map: When dense_hash_map erases an element, it leaves behind a tombstone in the table. That tombstone will only be removed if you insert a new element in that slot. A tombstone is a requirement of the quadratic probing that google::dense_hash_map does on lookup: When an element gets erased, it’s very difficult to find another element to take its slot. In Robin Hood hashing with linear probing it’s trivial to find an element that should go into the now empty slot: just move the next element one forward if it isn’t already in its ideal slot. In quadratic probing it might have to be an element that’s four slots over. And when that one gets moved you have to again solve the problem of finding a node to insert into the newly vacated slot. So instead you insert a tombstone and then the table knows to ignore tombstones on lookup. And they will be replaced on the next insert.

What this means though is that the table will get slightly slower once you have tombstones in your table. So dense_hash_map has a fast erase at the cost of slowing down lookups after an erase. Measuring the impact of that is a bit difficult, but I believe I have found a test that works for this purpose: I insert and erase elements over and over again:

![inserts_and_erase](../_resources/47bc2263c5bd2ddbc3069076d3b2e27a.png)

The way this test works is that I first generate a million random ints. Then I insert these into the hashtable and erase them again and insert them again. The trick is that I do this in a random order: So let’s say I only had the four integers 1, 2, 3 and 4. Then a valid order for “insert, erase and insert again” would be insert 1, insert 3, erase 1, insert 2, insert 4, erase 4, insert 4, insert 1, erase 2, erase 3, insert 3, insert 2. Every element gets inserted, erased and inserted again. But the order is random. The graph above counts the number of inserts and measures how long the insert takes per element. The first data point, all the way on the left is just inserting a million elements. The second data point is inserting a million elements, erasing them and inserting them again in a random order like I explained. The next data point does insert, erase, insert, erase, insert. So three inserts in total. You get the idea.

What we see is that at first dense_hash_map is faster because its inserts are faster. At the second data point my hashtable has already caught up to it. At the third data point my hashtable is winning, and at six million inserts even my prime number version is winning. The reason why my tables keep on getting faster is that as there are more erases, you would expect the average load factor of the table to go down. If you insert and erase a million items often enough, the table will always have close to 500,000 elements in it. So as you get further to the right in this graph, the table will be less full on average. My hash table can take advantage of that, but dense_hash_map has a bunch of tombstones in the table which prevent it from going faster. That being said if we compare dense_hash_map against other hash tables, it’s still very fast:

![insert_and_erase_all.png](../_resources/aaf1ad027f68028c0530ecbb6918356f.png)

So from this angle it totally makes sense for dense_hash_map to use quadratic probing, even if that requires inserting tombstones into the table on erase. The table is still very fast, certainly much faster than any node based container. But the point remains that Robin Hood linear probing gives me a more elegant way of erasing elements because it’s easy to find which element should go into the empty slot. And if you have a table where you often erase and insert elements, that’s an advantage.

## Comparing Tables with Different max_load_factor()

One final graph that I promised above is a way to resolve the problem that std::unordered_map and boost::multi_index use a max_load_factor of 1.0, while my table and google::dense_hash_map use 0.5. Wouldn’t the other tables also be faster if they used a lower max_load_factor? To determine that I ran the same benchmark that I used to generate the very first graph (successful lookups) but I set the max_load_factor to 0.5 on each table. And then I took measurements just before a table reallocates. I’ll explain it a bit better after the graph:

![successful_lookup_fixed_load_factor.png](../_resources/07d653677ed9270e82ee4b77630cc7e5.png)

This is the same graph as the very first graph in this blog post, except all the tables use a max_load_factor of 0.5. And then I wanted to only measure these tables when they really do have the same load factor, so I measured each table just before it would reallocate its internal storage. So if you look back at the very first graph in this blog post, imagine that I drew lines from one peak to the next. If we want to directly compare performance of hashtables and we want to eradicate the effect of different hash tables using different max_load_factor values and different strategies for when they reallocate, I think this is the right graph.

In this graph we see that flat_hash_map is faster than dense_hash_map, just as it was in the initial graph. It’s now much clearer though because all the noisiness is gone. Btw that brief time where dense_hash_map is faster is a result of dense_hash_map using less memory: At that point dense_hash_map still fits in my L3 cache but my flat_hash_map does not. Knowing this I can also see the same thing in the first graph, but it’s much clearer here.

But the main point of this was to compare boost::multi_index and std::unordered_map, which use a max_load_factor of 1.0 to my flat_hash_map and dense_hash_map which use a max_load_factor of 0.5. As you can see even if we use the same max_load_factor for every table, the flat tables are faster.

This was expected, but I still think this was worth measuring. In a sense this is the truest measure of hash table performance because here all hash tables are configured the same way and have the same load factor: Every single data point has a current load factor of 0.5. That being said I did not use this method of measuring for my other graphs, because in the real world you probably will never change the max_load_factor. And in the real world you will see the spiky performance of the initial graph where similar tables can have very different performance, depending on how many hash collisions there are. (and the load factor is actually only one part of that, as I also discussed above when talking about powers of two vs prime numbers) And also this graph hides one benefit of my table: Limiting the probe count leads to more consistent performance, making the lines of my hash_map less spiky than the lines of other tables.

## Different Keys and Values

So far every graph was measuring performance of a map from int to int. However there might be differences in performance when using different keys or larger values. First, here are the graphs for successful lookups and unsuccessful lookups when using strings as keys:

![successful_lookup_string](../_resources/7dc7d4a1580db68931b288af82b4b1dd.png)

Yes, I went with the version of the graph where the table is already in the cache. It’s easier to generate. What we see here is that using a string is just moving all lines up a little. Which is expected, because the main cost here is that the hash function changed and the comparison is more expensive. Let’s look at unsuccessful lookups, too:

![unsuccessful_lookup_string.png](../_resources/c8e35972320c752c7f57eb985e6a7ad4.png)

This is very interesting: It looks like looking for an element that’s not in the table is more expensive in google::dense_hash_map than in boost::multi_index. The reason for this is interesting: When creating a dense_hash_map you have to provide a special key that indicates that a slot is empty, and a special key that indicates that a slot is a tombstone. I used std::string(1, 0) and std::string(1, 255) respectively. But what this means is that the table has to do a string comparison to see that the slot is empty. All the other tables just do an integer comparison to see that a slot is empty.

That being said a string comparison that only compares a single character should be really cheap. And indeed the overhead is not that big. It just looks big above because every lookup is a cache hit. The cache miss picture looks different:

![unsuccessful_lookup_string_cache_miss.png](../_resources/d81b14ef488b34ac1722cf5dbab86634.png)

In this we can see that when the table is not already in the cache, dense_hash_map remains faster. Except it gets slower when the table gets very big. (more than a million entries) I didn’t find out why that is.

The next thing I tried to vary was the size of the value. What happens if I don’t have a map from an int to an int, but from an int to a 32 byte struct? Or from an int to a 1024 byte struct. So for the lookups I have 12 graphs in total ([int value, 32 byte value, 1024 byte value] x [int key, string key] x [successful lookup, unsuccessful lookup]) and most of them look exactly like the graphs above: All string lookups look the same independent of value size, and most int lookups also look the same. Except for one: Unsuccessful lookup of an int key and a 1024 byte value:

![unsuccessful_lookup_1024.png](../_resources/e47313329d8ba086f61baed6a929ff92.png)

What we see here is that at a 1024 byte value, multi_index is actually competitive to the flat tables. The reason for this is that in an unsuccessful lookup you have to do the maximum number of probes, and with a value type that’s as huge as 1024 bytes, your prefetcher has to work hard. My table still seem to be winning, but for a value that’s this large, everything is essentially a node based container.

The reason why all other lookup graphs looked the same (and why I don’t show them) is this: For the node-based containers you don’t care how big the value is. Everything is a separate heap allocation anyway. For the flat containers you would expect that you would get more cache misses. But since the max_load_factor is 0.5, the element is usually found in the table pretty quickly. The most common case is exactly one lookup: Either you find it in the first probe or you know with the first probe that it won’t be in the table. Two probes also happen pretty often, but three probes are rare. Also at least in my table the lookups are just a linear search. CPUs are great at prefetching the next element in a linear search, no matter how big the item is.

So lookups mostly don’t change with the size of the type, the graph for inserts and erases changes a lot though. Here is inserting with an int as a key and a 32 byte struct as a value:

![insert_32_byte.png](../_resources/d0265f1373f9f41c6e2a7d7c3f056f6c.png)

All the graphs have moved up a bit, but the graphs of the flat tables have moved up the most and have become more spiky: Reallocations hurt more when you have to move more data. The node based containers are not affected by this, and boost::multi_index stays competitive for a very long time. Let’s see what this looks like for a really large type, a 1024 byte struct:

![insert_1024_byte.png](../_resources/df7afed31ce54556baf010459af22049.png)

Now the order has flipped completely: The flat containers are more expensive and very spiky, the node based containers keep their speed. At this point reallocation cost dominates completely.

One oddity is that it’s really expensive to insert a single element into a dense_hash_map. (all the way on the left of the yellow line) The reason for this is that dense_hash_map allocates 32 slots at first and it fills all of them with a default constructed value type. Since my value type is 1024 bytes in size, it has to set 32 kib of data to 0. This probably won’t affect you, but I felt like I should explain the strange shape of the line.

The other thing that happened is that dense_hash_map is now slower than my hashtable. I didn’t look into why that is, but I would assume it’s for the same reason as the above paragraph: dense_hash_map fills every slot with a default constructed value type, so reallocation is even more expensive because all the slots have to be initialized, even the ones that will never be used.

If reallocation is expensive, the solution is to call reserve() on the container ahead of time so that no reallocation has to happen. Let’s see what happens when we insert the same elements but call reserve first:

![insert_reserve_1024](../_resources/16fc144be46d66d8f32d876de43a3b67.png)

When calling reserve first, my container is faster than the node based containers at first, but at some point boost::multi_index is still faster. dense_hash_map is still slower and again I think that’s because it initializes more elements than necessary and with a value this big, even just initializing the whole table to the “empty” key/value pair takes a lot of time. They could probably optimize this by only initializing the key to the “empty” key and not initializing the value, but then again how often do you insert a value that’s 1024 bytes? It’s neat as a benchmark to test the behavior of containers as the stored values grow very large, but it might not happen in the real world.

My containers are faster until they get large: at exactly 16385 elements there is a sudden jump in the cost. At 16384 elements things are still at the normal speed. Since every element in the container is 1028 bytes, that means that if your container is more than 16 megabytes, it can suddenly get slower. At first I thought this was a random reallocation because I hit the probe count limit, which would have been embarrassing because I explained further up in this blog post about how rare that is, but luckily that’s not the case. The reason for this is interesting: At exactly that measuring point the amount of time I spend in clear_page_c_e goes up drastically. It’s not easy to find out what that is, but luckily Bruce Dawson wrote a [blog post](https://randomascii.wordpress.com/2014/12/10/hidden-costs-of-memory-allocation/) where he mentions the cost of zeroing out memory and that this happens in a function called clear_page_c_e. So for some reason at exactly that measuring point it takes the OS a lot longer to provide me with cleared pages of memory. So depending on your memory manager and your OS, this may or may not happen to you.

That also means though that this is a one time cost. Once you’ve grown the container, you will not hit that spike in cost again. So if your container is long lived this cost will be amortized.

Let’s try inserting strings:
![insert_strings](../_resources/2b93ea881559f542fd7149367380a50c.png)

dense_hash_map is surprisingly slow in this benchmark. The reason for that is that my version of dense_hash_map doesn’t support move semantics yet. So it makes unnecessary string copies. I’m using the version of dense_hash_map that comes with Ubuntu 16.04, which is probably a bit out of date. But I also can’t seem to find a version that does support move semantics, so I’ll stick with this version.

So we’ll use this graph mostly to compare my table against the node base containers, and my table loses. Once again I blame this on the higher cost of reallocation. So let’s try what happens if I reserve first:

![insert_reserve_strings.png](../_resources/0682535e9a45b02dcc964acae453f5df.png)

… Honestly, I can’t read anything from this. The cost of the string copy dominates and all tables look the same. The main lesson to learn from this is that when your type is expensive to copy, that will dominate the insertion time and you should probably pick your hash table based on the other measures, like lookup time. We can see a similar picture when I insert strings as key with a large value type:

![insert_reserve_strings_1024](../_resources/9df30ccc1868599895737a65e2acbb32.png)

Once again dense_hash_map is slow because it initializes all those bytes. The other tables are pretty much the same because the copying cost dominates. Except that my flat_hash_map_power_of_two has that same weird spike at exactly 16385 elements due to increased time spent in clear_page_c_e that I also had when inserting ints with a 1024 byte value.

Lesson learned from this: If you have a large type, inserts will be equally slow in all tables, you should call reserve ahead of time, and the node based containers are a much more competitive option for large types than they are for small types.

Let’s also measure erasing elements. Once again I ran three tests for ints as keys and three tests for strings as keys: Using a 4 byte value, a 32 byte value and a 1024 byte value. The four byte value picture is shown above. The 32 byte value picture looks identical, so I’m not even going to show it. The 1024 byte value picture looks like this:

![erase_1024](../_resources/a039784fbc50e03f1e2deeec57c694fd.png)

The main difference is that dense_hash_map got a lot slower. This is the same problem as in the others pictures with large value types: The other tables just consider an item deleted and call the destructor which is a no-op for my struct. dense_hash_map will overwrite the value with the “empty” key/value pair which is a large operation if you have 1024 bytes of data.

Otherwise the main difference here is that erasing from flat_hash_map has gotten much more spiky than it was in the other erase picture above, and the line has moved up considerably, getting almost as expensive as in the node based containers. I think the reason for this is that the flat_hash_map has to move elements around when an item gets erased, and that is expensive if each element is 1028 bytes of data.

The graphs for erasing strings look similar enough to the graphs for erasing ints that they’re almost not worth showing. Here is one though:

![erase_string.png](../_resources/e4e9adc92846749597d4f939f48f319e.png)

Looks very similar to erasing ints. If I make the value size 1024 bytes, the graph looks very similar to the one above this one, so just look at that one again.

The final test is the “insert, erase and insert again” test I ran above where I do inserts and erases in random orders. I reduced the number to 10,000 elements because I ran out of memory when running this with ten million 1028 byte elements. It’s also much faster to generate these graphs when I’m using fewer elements. Let’s start with a 32 byte value type:

![insert_and_erase_32.png](../_resources/1727592b97e6e391ba83f5f9cd4659da.png)

flat_hash_map actually beats dense_hash_map now. The difference gets bigger if we increase the size of the value even more:

![insert_and_erase_1024.png](../_resources/4461e46aa3f2180d8963054fead99eee.png)

With a really large value type my table beats dense_hash_map. However now the node based containers beat my hash table at first, but over time my table seems to catch up. The reason for this is that I’m not reserving in these graphs. So in the first insert the table has to reallocate a bunch of times and that is very expensive in the flat containers, and it’s cheaper for the node based containers. However as we erase a few elements and insert a few elements, the reallocation cost gets amortized and my tables beat unordered_map, and they would probably also beat multi_index at some point. If I reserve ahead of time they beat multi_index right away:

![reserve_insert_and_erase_1024.png](../_resources/6f2861eee4d17106af6f7af8927e189d.png)

I actually didn’t expect this because even though I reserve ahead of time, my container still has to move elements around, and that should be really expensive for 1028 bytes of data. My only explanation for why my container remains fast is that the load factor is pretty low and that collisions are rare. When I measure this test with strings, I do see that my container slows down as expected and multi_index is competitive:

![reserve_insert_erase_string](../_resources/8ec3337829f4e1c3130deaae33f52dcc.png)

The other pictures for inserting strings look similar to the above pictures: When inserting strings with a 32 byte value type, the graph looks like this last one. When inserting with a 1024 byte value type it looks like the graphs where I did the same thing with ints as a key, both for the case where I do reserve and the case where I don’t reserve.

## Performance Summary

That was quite a lot of measurements. Measuring hashtables is surprisingly complex. I’m still not entirely sure if I should measure all tables with the same load factors or with their default setting. I chose to go for the default setting here. And then there are so many different cases: Different keys, different value sizes, different table sizes, reserve or not etc. And there are a lot of different tests to do. I could have put thousands of graphs into this blog post, but at some point it just gets too much, so let me summarize:

- My new table has the fastest lookups of any table I could find
- It also has really fast insert and erase operations. Especially if you reserve the correct size ahead of time.
- For large types the node based containers can be faster if you don’t know ahead of time how many elements there will be. The cost of reallocations kills the flat containers. Without reallocation my flat container is the fastest in all benchmarks for large types.
- When inserting strings the cost of the string hashing, comparison and copy dominate and the choice of hashtable doesn’t matter much.
- google::dense_hash_map has some surprising cases where it slows down.
- boost::multi_index is a really impressive hash table. It has very good performance for a node based container.
- If you know that your hash function returns a good distribution of values, you can get a significant speed up by using the power_of_two version of my hashtable.

## Exception Safety

When using my table it’s safe for you to throw exceptions in your constructor, your copy constructor, in your hash function, in your equality function and in your allocator. You are not allowed to throw exceptions in a move constructor or in a destructor. The reason for this is that I have to move elements around and maintain invariants. And if you throw in a move constructor, I don’t know how to do that.

## Source Code and Usage

I’ve uploaded the source code to github. You can download it [here](https://github.com/skarupke/flat_hash_map/blob/master/flat_hash_map.hpp). It’s licensed under the boost license. It’s a single header that contains both ska::flat_hash_map and ska::flat_hash_set. The interface is the same as that of std::unordered_map and std::unordered_set.

There is one complicated bit if you want to use the power_of_two version of the table: I explain how to do that further up in this blog post. Search for “ska::power_of_two_hash_policy” to get to the explanation.

Also I want to point out that my default max_load_factor is 0.5. It’s safe to set it as high as 0.9. Just be aware that your table will probably reallocate before it hits that number. It tends to reallocate before it’s 70% full because it hits the probe count limit. But if you don’t care that your table might reallocate when you’re not expecting it, you can save a bit of memory by using a higher max_load_factor while only suffering a tiny loss of performance.

## Summary

I think I wrote the fastest hash table there is. It’s definitely the fastest for lookups, and it’s also really fast for insert and erase operations. The main new trick is to set an upper limit on the probe count. The probe count limit can be set to log2(n) which makes the worst case lookup time O(log(n)) instead of O(n). This actually makes a difference. The probe count limit works great with Robin Hood hashing and allows some neat optimizations in the inner loop.

The hash table is available under the boost license as both a hash_map and a hash_set version. Enjoy!

### Share this:

- [Twitter](https://probablydance.com/2017/02/26/i-wrote-the-fastest-hashtable/?share=twitter&nb=1)
- [Facebook236](https://probablydance.com/2017/02/26/i-wrote-the-fastest-hashtable/?share=facebook&nb=1)

-
[Like](https://widgets.wp.com/likes/#)

- [![vikdutt](../_resources/97a40500b2bca6b31af3bfa82b50948f.jpg)](http://en.gravatar.com/vikdutt)

One blogger likes this.

### *Related*

[I Wrote a Fast Hash Table](https://probablydance.com/2014/05/03/i-wrote-a-fast-hash-table/)In "Programming"

[I Wrote a Faster Hash Table](https://probablydance.com/2014/05/31/i-wrote-a-faster-hash-table/)In "Programming"

[Faster Sorting Algorithm Part 2](https://probablydance.com/2017/01/17/faster-sorting-algorithm-part-2/)In "Programming"