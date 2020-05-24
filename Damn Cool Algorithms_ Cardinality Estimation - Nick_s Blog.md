Damn Cool Algorithms: Cardinality Estimation - Nick's Blog

## Damn Cool Algorithms: Cardinality Estimation

Posted by Nick Johnson | Filed under [python](http://blog.notdot.net/tag/python), [cardinality-estimation](http://blog.notdot.net/tag/cardinality-estimation), [damn-cool-algorithms](http://blog.notdot.net/tag/damn-cool-algorithms)

Suppose you have a very large dataset - far too large to hold in memory - with duplicate entries. You want to know how many duplicate entries, but your data isn't sorted, and it's big enough that sorting and counting is impractical. How do you estimate how many *unique* entries the dataset contains? It's easy to see how this could be useful in many applications, such as query planning in a database: the best query plan can depend greatly on not just how many values there are in total, but also on how many *unique* values there are.

I'd encourage you to give this a bit of thought before reading onwards, because the algorithms we'll discuss today are quite innovative - and while simple, they're far from obvious.

### A simple and intuitive cardinality estimator

Let's launch straight in with a simple example. Suppose someone generate a dataset with the following procedure:

1. Generate `n` evenly distributed random numbers
2. Arbitrarily replicate some of those numbers an unspecified number of times
3. Shuffle the resulting set of numbers arbitrarily

How can we estimate how many unique numbers there are in the resulting dataset? Knowing that the original set of numbers was random and evenly distributed, one very simple possibility occurs: simply find the smallest number in the set. If the maximum possible value is `m`, and the smallest value we find is `x`, we can then estimate there to be about `m/x` unique values in the total set. For instance, if we scan a dataset of numbers between 0 and 1, and find that the smallest value in the set is 0.01, it's reasonable to assume there are roughly 100 unique values in the set; any more and we would expect to see a smaller minimum value. Note that it doesn't matter how many times each value is repeated: it is the nature of aggregates like `min` that repetitions do not affect the output value.

This procedure has the advantage of being extremely straightforward, but it's also very inaccurate. It's not hard to imagine a set with only a few distinct values containing an unusually small number; likewise a set with many distinct values could have a smallest value that is larger than we expect. Finally, few datasets are so well behaved as to be neatly random and evenly distributed. Still, this proto-algorithm gives us some insight into one possible approach to get what we want; what we need is further refinements.

### Probabilistic counting

The first set of refinements comes from the paper [Probabilistic Counting Algorithms for Data Base Applications](http://www.cse.unsw.edu.au/~cs9314/07s1/lectures/Lin_CS9314_References/fm85.pdf) by Flajolet and Martin, with further refinements in the papers [LogLog counting of large cardinalities](http://www.ic.unicamp.br/~celio/peer2peer/math/bitmap-algorithms/durand03loglog.pdf) by Durand-Flajolet, and [HyperLogLog: The analysis of a near-optimal cardinality estimation algorithm](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf) by Flajolet et al. It's interesting to watch the development and improvement of the ideas from paper to paper, but I'm going to take a slightly different approach and demonstrate how to build and improve a solution from the ground up, omitting some of the algorithm from the original paper. Interested readers are advised to read through all three; they contain a lot of mathematical insights I won't go into in detail here.

First, Flajolet and Martin observe that given a good hash function, we can take any arbitrary set of data and turn it into one of the sort we need, with evenly distributed, (pseudo-)random values. With this simple insight, we can apply our earlier procedure to whatever data we want, but they're far from done.

Next, they observe that there are other patterns we can use to estimate the number of unique values, and some of them perform better than recording the minimum value of the hashed elements. The metric Flajolet and Martin pick is counting the number of 0 bits at the beginning of the hashed values. It's easy to see that in random data, a sequence of `k` zero bits will occur once in every `2k` elements, on average; all we need to do is look for these sequences and record the length of the longest sequence to estimate the total number of unique elements. This still isn't a great estimator, though - at best it can give us a power of two estimate of the number of elements, and much like the min-value based estimate, it's going to have a huge variance. On the plus side, our estimate is very small: to record sequences of leading 0s of up to 32 bits, we only need a 5 bit number.

As a side note, the original Flajolet-Martin paper deviates here and uses a bitmap-based procedure to get a more accurate estimate from a single value. I won't go into this in detail, since it's soon obsoleted by improvements in subsequent papers; interested readers can read the original paper for more details.

So we now have a rather poor estimate of the number of values in the dataset based on bit patterns. How can we improve on it? One straightforward idea is to use multiple independent hash functions. If each hash produces its own set of random outputs, we can record the longest observed sequence of leading 0s from each; at the end we can average our values for a more accurate estimate.

This actually gives us a pretty good result statistically speaking, but hashing is expensive. A better approach is one known as *stochastic averaging*. Instead of using multiple hash functions, we use just a single hash function, but use part of its output to split values into one of many buckets. Supposing we want 1024 values, we can take the first 10 bits of the hash function as a bucket number, and use the remainder of the hash to count leading 0s. This loses us nothing in terms of accuracy, but saves us a lot of redundant computation of hashes.

Applying what we've learned so far, here's a simple implementation. This is equivalent to the LogLog algorithm in the Durand-Flajolet paper; for convenience and clarity, though, I'm counting trailing (least-significant) 0 bits rather than leading ones; the result is exactly equivalent.

def trailing_zeroes(num):
  """Counts the number of trailing 0 bits in num."""
  if num ==  0:
    return  32  # Assumes 32 bit integer inputs!
  p =  0
  while  (num >> p)  &  1  ==  0:
    p +=  1
  return p

def estimate_cardinality(values, k):
  """Estimates the number of unique elements in the input set values.

  Arguments:
    values: An iterator of hashable elements to estimate the cardinality of.

    k: The number of bits of hash to use as a bucket number; there will be 2**k buckets.

  """
  num_buckets =  2  ** k
  max_zeroes =  [0]  * num_buckets
  for value in values:
    h = hash(value)

    bucket = h &  (num_buckets -  1)  # Mask out the k least significant bits as bucket ID

    bucket_hash = h >> k
    max_zeroes[bucket]  = max(max_zeroes[bucket], trailing_zeroes(bucket_hash))

  return  2  **  (float(sum(max_zeroes))  / num_buckets)  * num_buckets *  0.79402

This is all pretty much as we just described: we keep a bunch of counts of number of leading (or trailing) zeroes; at the end we average the counts; if our average is x, our estimate is 2x, multiplied by the number of buckets. Not mentioned previously is this magic number `0.79402`. Statistical analysis shows that our procedure introduces a predictable bias towards larger estimates; this magic constant is derived in the paper by Durand-Flajolet to correct that bias. The actual figure varies with the number of buckets used, but with larger numbers of buckets (at least 64), it converges on the estimate we use in the above algorithm. See the complete paper for *lots* more information, including the derivation of that number.

This procedure gives us a pretty good estimate - for m buckets, the average error is about `1.3/sqrt(m)`. Thus with 1024 buckets (for 1024 * 5 = 5120 bits, or 640 bytes), we can expect an average error of about 4%; 5 bits per bucket is enough to estimate cardinalities up to 227 per the paper). That's pretty good for less than a kilobyte of memory!

Let's try it ourselves on some random data:

>>>  [100000/estimate_cardinality([random.random()  for i in range(100000)],  10)  for j in range(10)]

[0.9825616152548807,  0.9905752876839672,  0.979241749110407,  1.050662616357679,  0.937090578752079,  0.9878968276629505,  0.9812323203117748,  1.0456960262467019,  0.9415413413873975,  0.9608567203911741]

Not bad! Some of the estimates are off by more than the predicted 4%, but all in all they're pretty good. If you're trying this experiment yourself, one caution: Python's builtin `hash()` hashes integers to themselves. As a result, running something like `estimate_cardinality(range(10000), 10)` will give wildly divergent results, because `hash()` isn't behaving like a good hash function should. Using random numbers as in the example above works just fine, however.

### Improving accuracy: SuperLogLog and HyperLogLog

While we've got an estimate that's already pretty good, it's possible to get a lot better. Durand and Flajolet make the observation that outlying values do a lot to decrease the accuracy of the estimate; by throwing out the largest values before averaging, accuracy can be improved. Specifically, by throwing out the 30% of buckets with the largest values, and averaging only 70% of buckets with the smaller values, accuracy can be improved from `1.30/sqrt(m)` to only `1.05/sqrt(m)`! That means that our earlier example, with 640 bytes of state and an average error of 4% now has an average error of about 3.2%, with no additional increase in space required.

Finally, the major contribution of Flajolet et al in the HyperLogLog paper is to use a different type of averaging, taking the *harmonic mean instead of the *geometric mean* we just applied. By doing this, they're able to edge down the error to `1.04/sqrt(m)`, again with no increase in state required. The complete algorithm is somewhat more complicated, however, as it requires corrections for both small and large cardinalities. Interested readers should - you guessed it - read the entire paper for details.*

*

### Parallelization

One really neat attribute that all these schemes share is that they're really easy to parallelize. Multiple machines can independently run the algorithm with the same hash function and the same number of buckets; at the end results can be combined by taking the maximum value of each bucket from each instance of the algorithm. Not only is this trivial to do, but the resulting estimate is exactly identical to the result we'd get running it on a single machine, while we only needed to transfer less than a kilobyte of data per instance to achieve this.

### Conclusion

Cardinality estimation algorithms like the ones we've just discussed make it possible to get a very good estimate - within a few percent - of the total number of unique values in a dataset, typically using less than a kilobyte of state. We can do this regardless of the nature of the data, and the work can be distributed over multiple machines with minimum coordination overhead and data transfer. The resulting estimates can be useful for a range of things, such as traffic monitoring (how many unique IPs is a host contacting?) and database query optimization (should we sort and merge, or construct a hashtable of unique values?).

Got an algorithm that you think is Damn Cool? Post it in the comments and perhaps I'll write about it in a future post!

 07 September, 2012

 [Previous Post](http://blog.notdot.net/2012/08/Damn-Cool-Algorithms-Homomorphic-Hashing)  [Next Post](http://blog.notdot.net/2012/09/Penny-for-your-thoughts)

### Comments

- [30 comments]()
- [**Nick's Blog**](https://disqus.com/home/forums/notdot-blog/)
- [Login](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend  6](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
- [⤤  Share](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/7b2fde640943965cc88df0cdee365907.png)
Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

###### Log in with

-
-
-
-

######  or sign up with Disqus

?

### Disqus is a discussion network

- Disqus never moderates or censors. The rules on this community are its own.
- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

brxx  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643476480)

The initial estimator function is inverted, it should be: carnality ~ m/x (max/min).

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/6bb07a2112f2a040dc7bb813109fc9de.jpg)](https://disqus.com/by/Arachnid/)

 [Nick Johnson](https://disqus.com/by/Arachnid/)  Mod  [*>* brxx](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643476480)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643478608)

Quite right; fixed. I like the idea of a carnality estimator, by the way.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/7f07b8371c792d6792de8258946dca66.jpg)](https://disqus.com/by/dwmkerr/)

 [Dave Kerr](https://disqus.com/by/dwmkerr/)    [*>* Nick Johnson](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643478608)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-647508001)

gave me chuckles too

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](:/4501eb5bb5a826b2e97c6e610bf28f62)](https://disqus.com/by/timothypeierls/)

 [Timothy Peierls](https://disqus.com/by/timothypeierls/)    [*>* Nick Johnson](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643478608)  •  [3 months ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-3264992059)

Good for measuring whether the flesh is weak.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/64d223031cc831470dcb3f40976453f6.jpg)](https://disqus.com/by/ascetics/)

 [ascetics](https://disqus.com/by/ascetics/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643598009)

Probabilistic data-structures are totally some of the most clever critters in the CS menagerie.

A few years back, we needed to count hundreds of billions of sets with highly variable cardinality; understandably, it mattered if we could shave a few bytes off the serialization of each. We implemented Linear Counting, Hyper/LogLog, and a bunch of other related estimation utilities in a stream library, including a little guy you might be interested in: AdaptiveCounter (from "Fast and Accurate Traffic Matrix Measurement Using Adaptive Cardinality Counting" -- Cai, Pan, Kwok, and Hwang). It selects the most space-efficient strategy within your error tolerance, and upconverts the observation data before saturation.

The source is pretty well-documented, so check it out for more details. It's in Java. [https://github.com/clearspr...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Fclearspring%2Fstream-lib%3AritwuX7inHBfHEQCillt7pnytBU&cuid=208679)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/abramsm/)

 [abramsm](https://disqus.com/by/abramsm/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643601771)

[https://github.com/clearspr...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Fclearspring%2Fstream-lib%3AritwuX7inHBfHEQCillt7pnytBU&cuid=208679) - java implementations of several estimators

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/robgrzywinski/)

 [Rob Grzywinski](https://disqus.com/by/robgrzywinski/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-692229707)

We have made a HyperLogLog simulation available at [http://blog.aggregateknowle...](http://disq.us/url?url=http%3A%2F%2Fblog.aggregateknowledge.com%2F2012%2F10%2F25%2Fsketch-of-the-day-hyperloglog-cornerstone-of-a-big-data-infrastructure%2F%3AZuX47g5p9ZWrYtnlZ799twtjqKc&cuid=208679) if you are interested in learning more about the algorithm.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

decix  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-651153264)

This paper seems to be the cutting edge algorithm now: [http://citeseerx.ist.psu.ed...](http://disq.us/url?url=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fsummary%3Fdoi%3D10.1.1.163.375%3A0zFSFhXxpWVc47KgYNtYytW6tKs&cuid=208679)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ithinkihaveacat/)

 [ithinkihaveacat](https://disqus.com/by/ithinkihaveacat/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643661022)

Damn Cool algorithm suggestion: the Burrows-Wheeler transform [http://en.wikipedia.org/wik...](http://disq.us/url?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBurrows%25E2%2580%2593Wheeler_transform%3A2rnwljjpmyt9eDipYVLNIpT6eeQ&cuid=208679). This (reversibly) transforms a string into another of the same length, but with more sequences of identical bytes. (Useful for compression.) One amazing aspect of this algorithm is that the transformation is reversible, despite involving a sorting phase.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/Arachnid/)

 [Nick Johnson](https://disqus.com/by/Arachnid/)  Mod  [*>* ithinkihaveacat](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643661022)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643694558)

Yup, I've been pondering writing about the BWT for a while. Doing a really in-depth post about it requires that I take the time to get a better understanding of it, though, so that I can hopefully convey some new insight.

One really cool thing you can do with the BWT: [http://www.drdobbs.com/arch...](http://disq.us/url?url=http%3A%2F%2Fwww.drdobbs.com%2Farchitecture-and-design%2Ffull-text-searching-the-burrows-wheeler%2F184405504%3AXvWWrZFFnGaecbGMwNgRpOhK-pY&cuid=208679)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Guest  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643564822)

[https://github.com/sedictor...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Fsedictor%2Floglog%3ATI_GXrWWHZGqH00VedE05jWN9SA&cuid=208679) — implementations of loglog and hyperloglog in javascript and php

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/gui11aume/)

 [Guillaume Filion](https://disqus.com/by/gui11aume/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643681195)

The whole Damn Cool Algorithm series is an aweome idea!! Really. Here is a suggestion: use radix tries [http://en.wikipedia.org/wik...](http://disq.us/url?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRadix_tree%3AFowxDQKIf9V3UYsgIumHEt7f43M&cuid=208679) for matching/substituting large numbers of keywords in text streams. For each character read, you perform only a small number of comparisons to know whether there is a match.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ajoybhatia/)

 [Ajoy Bhatia](https://disqus.com/by/ajoybhatia/)    •  [2 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-2216091861)

Quoting: "...taking the harmonic mean instead of the geometric mean we just applied"

The mean that was computed in the pseudo-code was the arithmetic mean, not the geometric mean. Geometric mean of x & y = sqrt(x * y)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/Algorithmic_Complexity/)

 [Algorithmic_Complexity](https://disqus.com/by/Algorithmic_Complexity/)    •  [2 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-1793421808)

Awesome discussion about cardinality estimation algorithms. Very handy. Another awesome generalized algorithm resource I have found is [www.algorithmiccomplexity.com](http://disq.us/url?url=http%3A%2F%2Fwww.algorithmiccomplexity.com%3A6XkfpsPEIYi4UjSDMfh7CBhLZyU&cuid=208679)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Rt7o4k8hMQ/)

 [Дмитрий Шалашов](https://disqus.com/by/disqus_Rt7o4k8hMQ/)    •  [3 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-1360639401)

If you have 32 bit hashes and use 10 bits as a bucket index (1024 = 2^10), then you have 22 bits left and you can't count values up to 2^27 with them... Only up to 2^22. Right?

You should use 64 bit hashes then.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/yati_itay/)

 [yati_itay](https://disqus.com/by/yati_itay/)    •  [3 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-1314503818)

Thank you for a great explanation :)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Valentin  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-654838186)

How about a Simhash. It's another probabilistic beast for finding near duplicates.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/xaprb/)

 [Baron Schwartz](https://disqus.com/by/xaprb/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-654746909)

You've shifted 10 bits off the right-hand side of the hash in your example, so the value you're passing to trailing_zeroes is only 22 bits long. If the value is 0, then should you return 22 from that function, not 32?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Lin Hailue  [*>* Baron Schwartz](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-654746909)  •  [4 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-820801678)

I have the same doubt too

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/odwyerrob/)

 [Rob O'Dwyer](https://disqus.com/by/odwyerrob/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-649231658)

Could a Bloom Filter be used for a similar purpose? A large enough array / set of hash functions would give a relatively low false positive rate and allow us to estimate the cardinality in O(n), right?

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/Arachnid/)

 [Nick Johnson](https://disqus.com/by/Arachnid/)  Mod  [*>* Rob O'Dwyer](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-649231658)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-649233104)

Yup, but it would be much less efficient, since the bloom filter stores a lot more information.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Lin Hailue  [*>* Nick Johnson](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-649233104)  •  [4 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-820803348)

With Bloom Filter I can get more accurate result, the main problem is it is hard to be parallelized. I don't know how to combine two bloom filters and calculate a final result. Does anyone know?

            -

                - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
                - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/Arachnid/)

 [Nick Johnson](https://disqus.com/by/Arachnid/)  Mod  [*>* Lin Hailue](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-820803348)  •  [4 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-820846815)

Sure - just OR them together.

                -

                    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
                    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Lin Hailue   [*>* Nick Johnson](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-820846815)  •  [4 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-820881175)

And estimate the final count?

But anyway I found what I what, the Linear Counter mentioned in [[http://highscalability.com/...](http://disq.us/url?url=http%3A%2F%2Fhighscalability.com%2Fblog%2F2012%2F4%2F5%2Fbig-data-counting-how-to-count-a-billion-distinct-objects-us.html%3AbCu51g0GBDm4_JmINso_bx04cDM&cuid=208679)]. It is similar to bloom filter, but simpler and composable.

thanks, I really love the Damn Cool Algorithms~

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/gprasant/)

 [prasanth](https://disqus.com/by/gprasant/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-644105013)

I dont understand what you mean in the simple estimator. When you say that the dataset contains random numbers evenly spaced, are they an arithmetic progression?

Lets take the case of 1, 2,3,...10 . In this case number of unique elements = 10/1 = 10

But in the case of 2, 3, 4, 5....11. 11/2 = 5.5 But the number of unique elements is 10.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/Arachnid/)

 [Nick Johnson](https://disqus.com/by/Arachnid/)  Mod  [*>* prasanth](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-644105013)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-644138147)

If they followed an arithmetic progression, they wouldn't be random. By evenly spaced, I mean that the random distribution doesn't cluster - the probability of any given number being produced is the same.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_WN8KAR7YV1/)

 [John Byrd](https://disqus.com/by/disqus_WN8KAR7YV1/)    •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643549735)

Okay, I'll be the cranky old man here... If you're taking the time to generate hash values, which is arguably the most expensive part of the operation by far (because it requires reading the entire data set anyway), then why not simply put those hashes into a hash of hashes, while counting dupes in the hash-hash table? That seems pretty O(n) to me, and you still don't need to have the entire data set in memory... just hashes thereof. The idea is academically interesting but practically, this seems like a lot of work to generate a result that is guaranteed to be incorrect while a faster, exact solution exists.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

John Smith  [*>* John Byrd](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643549735)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643582328)

The reason building a hash table is not a solution to this problem is because the dataset in question is "far too large to hold in memory". The brilliance of the algorithm is in the miniscule memory footprint.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/jackrae/)

 [Jack Rae](https://disqus.com/by/jackrae/)    [*>* John Byrd](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643549735)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643822678)

John - the whole point of Flajolet's algorithm is that it works relatively fast in poly-logarithmic space. The crucial point here, as you are pointing out is that in this instance, n is the RANGE of the data variables and not the number of data variables. In this instance, the range of possible values is too large to possibly hold in linear space.

This may sound esoteric, but this is becoming a reality in many situations involving fast and diverse data. For instance we may need to be computing the number of distinct connections that are being opened through the passage of a router - i.e. pairs of IP6 addresses for example, we have (2^128)^2 = 2^256 bits of possible storage. This may be too vast for a smallish router. It may be preferable to use an algorithm that requires maybe 4 x longer at each update (i.e. not muuuch longer) but only uses say... 50 * 256 bits of storage to get an accurate prediction.

The nice thing about Flajolet's algorithm is that does work in practice and is used. The bad thing about it is that it's not well justified theoretically, it makes unjustified assumptions of independence within its hash values. It works in practice, but there isn't sufficient theory to make assurances of such performance.

For the more theoretically justified algorithm, to perform the same thing, see [http://people.seas.harvard....](http://disq.us/url?url=http%3A%2F%2Fpeople.seas.harvard.edu%2F%7Eminilek%2Fpapers%2Ff0.pdf%3AhO51RSTq7VvmrA5QtYKxyygx7xo&cuid=208679) which is THE theoretically optimal solution to the problem. In practice, it's too expensive however.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Anonymous  [*>* John Byrd](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643549735)  •  [5 years ago](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation#comment-643701428)

You can leave out the hash function then, he's only using it to make an analogous data set that can be probabilistically analyzed, it doesn't help you count anything. Of course checking the entire data set for dupes would get you the exact number. The premise is that this is impractical.

## Also on **Nick's Blog**

- [

### 7400 Competition Winners Announced

    - 2 comments •

    - 5 years ago•

[Nick Johnson—Good catch. Fixed, thanks.](http://disq.us/url?url=http%3A%2F%2Fblog.notdot.net%2F2012%2F11%2F7400-Competition-Winners-Announced%3AhRNGXs3z8QmDO95gheCcjbLv524&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=921076236&zone=thread&area=bottom&object_type=thread&object_id=921076236)](http://disq.us/url?url=http%3A%2F%2Fblog.notdot.net%2F2012%2F11%2F7400-Competition-Winners-Announced%3AhRNGXs3z8QmDO95gheCcjbLv524&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=921076236&zone=thread&area=bottom&object_type=thread&object_id=921076236)

- [

### asdfsdfasdfasdfasd

    - 1 comment •

    - 3 years ago•

[jiazhe xu—test](http://disq.us/url?url=http%3A%2F%2Fbloggart.woxujiazhe.appspot.com%2F2014%2F12%2Fasdfsdfasdfasdfasd%3A8U56Zt9FWcHiBdOunH6Dl5bQ14U&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=3306037470&zone=thread&area=bottom&object_type=thread&object_id=3306037470)](http://disq.us/url?url=http%3A%2F%2Fbloggart.woxujiazhe.appspot.com%2F2014%2F12%2Fasdfsdfasdfasdfasd%3A8U56Zt9FWcHiBdOunH6Dl5bQ14U&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=3306037470&zone=thread&area=bottom&object_type=thread&object_id=3306037470)

- [

### Introducing Arachnid Labs and the Loki

    - 1 comment •

    - 4 years ago•

[Spud— Congrats on getting Arachnid labs going.I went over to tindie, I didn't see your stack able motor shield, will that be available …](http://disq.us/url?url=http%3A%2F%2Fblog.notdot.net%2F2013%2F01%2FIntroducing-Arachnid-Labs-and-the-Loki%3Ag6XyNPsXhoICDfnySoz0tjJ9uyo&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=1042924707&zone=thread&area=bottom&object_type=thread&object_id=1042924707)](http://disq.us/url?url=http%3A%2F%2Fblog.notdot.net%2F2013%2F01%2FIntroducing-Arachnid-Labs-and-the-Loki%3Ag6XyNPsXhoICDfnySoz0tjJ9uyo&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=1042924707&zone=thread&area=bottom&object_type=thread&object_id=1042924707)

- [

### my first blog post - mehmettekn

    - 1 comment •

    - 5 years ago•

[tekinme—hello world disqus](http://disq.us/url?url=http%3A%2F%2Fmehmetsapp2.appspot.com%2F2011%2F04%2F24%2Fmy-first-blog-post%2F%3AQrMjd8dU2tV-Y69kCit24sza__M&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=959495300&zone=thread&area=bottom&object_type=thread&object_id=959495300)](http://disq.us/url?url=http%3A%2F%2Fmehmetsapp2.appspot.com%2F2011%2F04%2F24%2Fmy-first-blog-post%2F%3AQrMjd8dU2tV-Y69kCit24sza__M&imp=8m5ijqu3k1sva&prev_imp=8m5g96vr9ufdm&forum_id=208679&forum=notdot-blog&thread_id=834623383&thread=959495300&zone=thread&area=bottom&object_type=thread&object_id=959495300)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=notdot-blog&t_u=http%3A%2F%2Fblog.notdot.net%2F2012%2F09%2FDam-Cool-Algorithms-Cardinality-Estimation&t_d=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&t_t=Damn%20Cool%20Algorithms%3A%20Cardinality%20Estimation%20-%20Nick%27s%20Blog&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=notdot-blog&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)

*