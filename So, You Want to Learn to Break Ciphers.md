So, You Want to Learn to Break Ciphers

# So, You Want to Learn to Break Ciphers

[September 28, 2015](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/) | [crazycontini](https://littlemaninmyhead.wordpress.com/author/crazycontini/)

Every now and then, I read a question about learning how to break ciphers, or more generally how to become a cryptographer/cryptologist.  From my viewpoint, the most important part of learning this skill is not advanced mathematics, but instead first learning how to think like a cryptographer.  When you go to break a cipher, there are no instructions on how to do it.  You simply need to get your hands dirty with the function under consideration and look for things that do not seem desirable for a secure function of that type.  While having a bag of tricks is going to help, ultimately it’s your creativity, persistence, and skills that are more likely going to make the difference.

I believe that there are a number of hackers out there that already know how to think the right way, and it is simply a matter of exercising that thought process on some reasonable, non-contrived examples to begin to understand what it takes to be a cryptologist.  You should not need to know advanced mathematics or advanced cryptographic techniques (such as linear or differential cryptanalysis) to get started.  So welcome to my blog post, which provides a number of exercise for you to practice on.  These examples mostly come from cryptanalysis that I have done, largely because I know the results, I was able to dig them up, and attacking them did not use advanced techniques.  I am building a list of other examples at the bottom of this blog, and invite other readers to add to it.

Before we begin, I want to point out some other resources on this topic:

- Schneier’s [Self-Study Course in Block Cipher Cryptanalysis](https://www.schneier.com/paper-self-study.html) is a great resource, but in my mind it is not the ideal place to start — from my viewpoint, it is the next step after you prove you can break ciphers such as what I have below.  By the way, you absolutely should read Schneier’s article [So, You Want to be a Cryptographer](https://www.schneier.com/crypto-gram/archives/1999/1015.html#SoYouWanttobeaCryptographer).
- [The Matasano Crypto Challenges](http://cryptopals.com/).  While they are similar in same spirit of what I am writing here, my focus is at a lower level — breaking specific [cryptographic primitives](https://en.wikipedia.org/wiki/Cryptographic_primitive) rather than constructs from these primitives.  Regardless, the Matasano challenges are another great place to start.
- The [Simon Singh Cipher Challenges](http://simonsingh.net/cryptography/cipher-challenge/)from his book, [The Code Book](http://www.amazon.com/The-Code-Book-Science-Cryptography/dp/0385495323).  This book is really fun to read, and will get you into the spirit of breaking his challenges.  But the first challenges are too easy and the last ones are very hard: it is really the middle ones that are most interesting.

I’m adding to existing resources because I thought I have a nice, small collection of my own that I have accumulated over the years.  Like the Matasano challenges, my focus is on providing modern examples that are easy to break without complex mathematics or advanced cryptographic techniques.  These examples illustrate how to think like a cryptographer without requiring all the complex background in the most advanced cryptanalytic techniques.  If you can solve these problems (and your solutions may not necessarily be the same as mine), then you have the right type of thinking to become a cryptographer.  **This blog post is written for computer scientists without deep mathematics skills that want to learn how to do cryptanalysis, and teachers of cryptography for computer science students**.

The examples come from different sources.  For example, I have a few proposals by amateurs that were easily cracked, including a couple from the old sci.crypt Google group (it was a popular meeting place for crypto-geeks before Google took over).  I have at least one proposal by an expert in some other field that was attempting to apply his skills to cryptography despite having little background in crypto.  I have one design that was built into software and relied upon for real-world security.  And then I have one example of something that was not intended for cryptographic purposes yet sometimes is misused by developers who do not understand that.  So let’s get started!

# PHP’s lcg_value( )

PHP’s [lcg_value( )](http://php.net/manual/en/function.lcg-value.php) is a pseudo random number generator (PRNG) that is not intended to provide cryptographic security.  Nevertheless, it occasionally gets used in ways that it should not be used.

The internal state of the PRNG has a total possibility of 2^62 combinations, which is too much to brute force this day in age.  However, **one technique that is often employed in cryptanalysis is trying all possibilities for half of the bits** (2^31 combinations here) **and for each candidate, see if you can compute the remaining bits in constant time**.  You then check whether the candidate is right by computing future outputs of the assumed internal state to to see whether or not it matches.  If it does, then you presume you have the right state, and if it does not match, then you know the candidate is wrong.

It turns out that this technique does work for lcg_value( ), and thus it can be cracked in 2^31 operations.  The details are [here](http://www.crypto-world.com/lcg_value.html) (the page describes the algorithm, how to attack it, and then provides a link to my solution).  This could take anywhere from a half-day to two days, depending upon your experience.  As a bonus, there is an advanced topic at the end of the link — how to crack lcg_value( ) if you only get a fraction of the output bits per iteration: this is a bit harder.

# Chaotic hash function

Every year there is the Crypto conference in Santa Barbara that has a light-hearted “rump session” where participants can present research-in-progress or anything of interest to the cryptographic community.  In the Crypto 2005 rump session, a researcher presented his new hash function based upon chaos theory.  The researcher was unknown to the cryptographic community.  He put up lots of graphs of his hash function, which might have been intimidating to one with no cryptographic experience, but that was not most of the audience, and hence hardly anybody listened to his presentation.  But I listened carefully, because I suspected an easy target that I wanted to have a go at.

Why did I suspect it an easy target?  I knew absolutely zero about chaos theory, and had no intention to learning it.  But what I saw was a guy who did not know anything about cryptography and how ciphers were attacked, and I was pretty sure I could find collisions in his hash function regardless of any graphs or mathematics behind his design.  The only trick was getting an exact specification so that I can demonstrate that I can break it.  This obstacle is often encountered in cryptanalysis — non-experts do not nail down their specification for whatever reason, but the cryptanalyst needs something concrete to demonstrate his attack.  So I exchanged email with him a few times and we finally agreed that the following C code represents his hash function (where ROTL and ROTR are circular left and right bit rotations):

void hash( unsigned int *input, int len, unsigned int output[4] )
{
unsigned int x, y, z, u, X, Y, Z, U, A, B, C, D, RV1, RV2, RV3, RV4;
unsigned int M = 0xffff;
int i, offset;
x = 0x0124fdce; y = 0x89ab57ea; z = 0xba89370a; u = 0xfedc45ef;
A = 0x401ab257; B = 0xb7cd34e1; C = 0x76b3a27c; D = 0xf13c3adf;
RV1 = 0xe12f23cd; RV2 = 0xc5ab6789; RV3 = 0xf1234567; RV4 = 0x9a8bc7ef;

for (i=0; i < len; ++i) { offset = 4*i; X = input[offset + 0] ^ x; Y = input[offset + 1] ^ y; Z = input[offset + 2] ^ z; U = input[offset + 3] ^ u; /* compute chaos */ x = (X & 0xffff)*(M-(Y>>16)) ^ ROTL(Z,1) ^ ROTR(U,1) ^ A;

y = (Y & 0xffff)*(M-(Z>>16)) ^ ROTL(U,2) ^ ROTR(X,2) ^ B;
z = (Z & 0xffff)*(M-(U>>16)) ^ ROTL(X,3) ^ ROTR(Y,3) ^ C;
u = (U & 0xffff)*(M-(X>>16)) ^ ROTL(Y,4) ^ ROTR(Z,4) ^ D;
RV1 ^= x; RV2 ^= y; RV3 ^= z; RV4 ^= u;
}
/* now run 4 more times */

for (i=0; i < 4; ++i) { X = x; Y = y; Z = z; U = u; /* compute chaos */ x = (X & 0xffff)*(M-(Y>>16)) ^ ROTL(Z,1) ^ ROTR(U,1) ^ A;

y = (Y & 0xffff)*(M-(Z>>16)) ^ ROTL(U,2) ^ ROTR(X,2) ^ B;
z = (Z & 0xffff)*(M-(U>>16)) ^ ROTL(X,3) ^ ROTR(Y,3) ^ C;
u = (U & 0xffff)*(M-(X>>16)) ^ ROTL(Y,4) ^ ROTR(Z,4) ^ D;
RV1 ^= x; RV2 ^= y; RV3 ^= z; RV4 ^= u;
}
output[0] = RV1; output[1] = RV2; output[2] = RV3; output[3] = RV4;
}

Does it look intimidating?  Well, once you start to get your hands dirty, you will see that it is not that bad at all.  The loop at the bottom does not involve any inputs, so if we can create a collision in the top loop, then it will give a collision in the hash.  The top loop takes blocks of 4 input words (128-bits) per iteration and mixes them into the existing state.  Here’s the real killer: **for any iteration, the attacker can make (X, Y, Z, U)  to be whatever he wants because he can compute (x, y, z, u) at the beginning of that iteration**  **(simply by processing the previous inputs) and choose the next inputs accordingly**.  Now there is still some ugly multiply and rotation stuff in there, but given that you can control (X, Y, Z, U), you can then make those multiplies and rotations behave in a convenient way for your attack.  Suddenly, what seemed to be a ferocious looking lion is nothing more than a tiny kitty cat.  Have a go yourself before you look at [my attacks](https://eprint.iacr.org/2005/403.pdf).  This one was easy and really fun to break.

By the way, after breaking this one, you should have decent insight into why algorithms of the MD and SHA families have a pre-processing phase that involves the message length, and use a message expansion that makes sure that functions of the input words get mixed in multiple times per iteration.

# Hash Function with “Technique in Overlapping Sums”

[Here](http://www.derkeiler.com/Newsgroups/sci.crypt/2004-09/0786.html) is another easy one from amateur on the good old sci.crypt group.  The author forgot to both declare and initialise the hash variable, so I fix-up the code below:

#define UL unsigned long
#define LEFT 13
#define RIGHT 19
UL hash[5];
void round() {

hash[4] += hash[0] >> RIGHT; hash[0] += hash[0] << LEFT; hash[0] += hash[1] >> RIGHT; hash[1] += hash[1] << LEFT; hash[1] += hash[2] >> RIGHT; hash[2] += hash[2] << LEFT; hash[2] += hash[3] >> RIGHT; hash[3] += hash[3] << LEFT; hash[3] += hash[4] >> RIGHT; hash[4] += hash[4] << LEFT;

}
void processBlock(const UL in[25])
{
int i, j, r, s;
memset( hash, 0, sizeof(hash) );
for (i = 0; i < 5; i++) {
s = 0;
for (r=0; r<5; r++) {
for (j = 0; j < 5; j++) {
hash[j] ^= in[j+s];
hash[j]++;
}
round();
s += 5;
}
}
}

It seems to only be a [compression function](https://en.wikipedia.org/wiki/One-way_compression_function) (processBlock( )) that takes a 25 word input and produces a 5 word output.  For the r’th round, he is mixing in inputs from in[5*r], … , in[5*r+4] into hash[0], …, hash[4]; seemingly unaware that we could compute the state of hash at any point and choose our next inputs accordingly (similar to the way we broke chaotic hash).  This one falls trivially, but for fun, I made my collisions to be [preimages of the all zero output](http://www.derkeiler.com/Newsgroups/sci.crypt/2004-09/0857.html).

# FastFlex

When FastFlex [was proposed](http://www.derkeiler.com/Newsgroups/sci.crypt/2006-04/msg00211.html)in 2006, the author made bold claims on the sci.crypt newsgroup about it not being resistant to linear or differential cryptanalysis, and wondered if there might be any other issues that he needs to worry about.  When somebody talks about these cryptanalysis techniques, you assume they know a little bit about cryptography, but it just goes to show: learning the techniques without knowing how to think like a cryptographer is of little value.  I took a look at the code the author had, and it had basic problems such as not initialising variables.  Within about a half hour, [I found collisions](http://www.derkeiler.com/Newsgroups/sci.crypt/2006-04/msg00238.html) (it may seem like I am always sending in zero words for the functions I break, but I didn’t need to for this one) in the hash function using techniques similar to how I broke the chaotic hash function above, and such collisions could easily be produced regardless of how variables were initialised.  The amusing reply from the author [acknowledged the problem but somehow concluded that FastFlex is still safe](http://www.derkeiler.com/Newsgroups/sci.crypt/2006-04/msg00252.html)!

After my reply, the author modified his design and sent it for publication, carefully making sure that the sci.crypt people didn’t see his updated design in the time frame of the publication attempt.  The author [claims that the paper was published](http://fastflex.sourceforge.net/) (see bottom of page), but the [updated paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.91.8810&rep=rep1&type=pdf) made no acknowledgement of the insecurity of the previous version or my finding.  The evidence for the security in the updated paper is pretty bad.

Unfortunately, the original specification seems to be no longer around, so breaking the new version remains open.  But let’s just say that how I broke it had a lot of similarities to how I broke the chaotic hash function, so first prepare yourself accordingly, and then take out the new FastFlex!  FastFlex is designed to build a number of cryptographic constructs from it.  I recommend starting with the hash functions, and after you break those, go after the random number generator.  If you are like me, you’ll start by going directly after the implementation rather than trying to waste too much time trying to read the author’s research paper.

If FastFlex was indeed published, then you should be able to get a publication out of breaking it provided that you write it up well.  I’d be most delighted to hear successful attacks on this one.  Note to attackers: make sure you save a copy of his code and pdf description after you break it so that the author cannot hide the history.

# R.A.T.

Amateurs are never shy to come up with their own cryptographic solutions, and often are generous enough to give them to the world unencumbered by patents.  While their hearts are in the right place, it is just not that easy to build a secure cryptosystem.  At the bottom of [this linked page](https://www.mail-archive.com/cryptography-digest@senator-bedfellow.mit.edu/msg02114.html), you can read about the R.A.T. encoding and decoding system.

I’m pretty sure there are numerous ways to attack this one (especially if you want to use linear algebra, but I didn’t), but my solution is in [this link](https://www.mail-archive.com/cryptography-digest%40senator-bedfellow.mit.edu/msg02116.html).  Don’t look at it until you found your own solution!

But here’s two hints to start you out:

1. Always give yourself the advantage by starting out with a [chosen plaintext attack](https://en.wikipedia.org/wiki/Chosen-plaintext_attack)(or chosen ciphertext attack), and then it can likely be converted into other types of attacks later.

2. It makes things easier if you write it out in terms of arrays (for A and B) so you can keep track of the relation between things from iteration to iteration.

To elaborate on point 2, the cipher would look something like this (where  A, B, and X are byte arrays of the length of the input size, and key is a byte array of length 256 — how it was generated does not really matter in my attack):

initialise: A[0] = 0, B[0] = 128
for i = 1 to the number of plaintext bytes {
Let X[i] = i'th plaintext byte
A1 = X[i] ^ key[ B[i-1] ]
B[i] = A1 ^ key[ A[i-1] ]
output B[i] as the i'th byte of the ciphertext
A[i] = A1
}

My break revealed bytes of the key when a certain condition happens, but I bet you can generalise it to do better.

# “Multiswap”

In 2001, “Beale Screamer” reverse engineered and broke Microsoft’s Digital Rights Scheme — see [link](http://cryptome.org/ms-drm.htm).  The scheme involved a cipher that he named “multiswap” (described in the link), because it used multiplication and swapped halves of computer words around.  Beale Screamer’s break of the DRM scheme did not touch the cryptography, which made it a prime target for cryptographers.

I immediately had a look at the cipher, and it didn’t take me long before I found a way to recover two words of the key (k[5] and k[11]) simply by choosing my plaintexts in such a way that made the multiplies disappear (hint hint).  I went to sleep thinking I will return to it the next day for attacking more of the cipher.  Unfortunately, my plans were preempted by a fast team of Berkley cryptographers who had the entire cipher broke by the next day — their solution is [here](http://www3.cs.stonybrook.edu/~rob/multiswap/).

Unsurprisingly, I started my attack the exact same way as the the Berkeley team to recover two words of the key.  You should be able to do the same thing.  After that, they used differential cryptanalysis to get the rest.  Since I assume that the reader is new to cryptography, I am not going to expect that he/she derives the remaining parts of the key similar to the Berkeley team.  However, there are various approaches one can play with in order to refine their cryptographic skills.  For example, knowing the plaintext allows you to compute s0′ and s1′ (from Berkeley description, which I believe is easier to work from). Then, one can try to deduce k[0], …, k[4] independently of k[6], … , k[10].  We could almost attempt the same technique that we used to break the lcg_value( ) here, except that’s still too many key bits to guess in a practical implementation.  However, if you reduce the size of the cipher in half (half of the number of key words, half of the number of rounds), then such a technique should work.  Give it a try!

Finally, one of the cutest parts of the Berkeley attack was showing how to convert the chosen plaintext attack into a known plaintext attack.  As we said before, give yourself the best advantage to start out with, and then worry about converting it to other forms of attacks later!

# Other targets to play around with

Over many years on sci.crypt, I saw a number of ciphers broken by members of the group.  I also occasionally see new ones that I think must be trivially breakable.  Nowadays, [reddit](https://www.reddit.com/r/crypto/) seems to be the place to go.  It is impossible for me to dig up all of the easily broken designs, but here are a few that I remember:

- The hash function Shahaha was proposed [here](http://www.derkeiler.com/Newsgroups/sci.crypt/2011-03/msg00322.html), and broken by Scott Fluhrer [here](http://www.derkeiler.com/Newsgroups/sci.crypt/2011-03/msg00326.html).  Can you come up with your own break?  (Scott Fluhrer broke a number of amateur designs in the sci.crypt days, but this is the only one I found so far).
- Just as I was trying to dig up old sci.crypt examples of ciphers, somebody on reddit’s crypto group posted an [I designed my own crypto thread](https://www.reddit.com/r/crypto/comments/3or80y/i_designed_my_own_crypto/).  This is a block cipher called XCRUSH. The full design is [here](http://arxiv.org/pdf/1509.02584v2.pdf).  The author claims that it is purely an academic exercise and makes no security claims at all in the paper, so his motivation is entirely for learning.  It’s also written up nicely, which is an advantage if you want people to look at your design.  Upon posting it on reddit, a character by the identity of bitwiseshiftleft found theoretical weaknesses quite soon (like in many of the examples above, the magic zero comes into play here again).  See the comments in the reddit thread for more detail. There was also some interesting analysis based upon [SAT solvers](https://gist.github.com/TomMD/b3747c747fc1c839bb11), but this is outside my expertise so I leave the reference for interested parties.
- This one might require a little bit of math, who knows how much (can’t be sure — I have not tried attacking it yet).  [Here](https://cryptome.org/2014/11/fast-pk-crypto.pdf) is a public key cryptosystem that seems too good to be true.  However, the author made a pretty basic mistake in his analysis (first observed by [rosulek](https://www.reddit.com/r/crypto/comments/3lbe0o/on_a_new_fast_public_key_cryptosystem/cv4zs0b)): the author claims to have proven that you can break it by solving circuit satisfiability (SAT).  Ummm, you can break every cryptosystem if you can solve SAT efficiently!  What would have been more interesting was showing the contrapositive: (i.e. if you could break his cryptosystem, then you can solve SAT).  The simple fact that the author did not know which direction to do the security reduction is indicative of his lack of experience, and hints that it can easily be broken.
- I was debating whether or not to include the first attacks on the original SecurId in the main list above, but ultimately I decided that it is too much detail.  However if anybody wants to have a go, [here](http://seclists.org/bugtraq/2000/Dec/459) is the code reverse-engineered from “I.C. Wiener”, [here](http://eprint.iacr.org/2003/162) is the description of the function from Belgian cryptographers (My coauthor and I worked from the original version that they posted on eprint, which has since been updated), and [here](http://www.derkeiler.com/Newsgroups/sci.crypt/2003-09/0439.html) is the first attack I found.  Read through section 1 of my attack, and then try to attack it with the following information in mind: the vanishing differentials (collisions) happen in the first 32-subrounds, so key search can be expedited by computing only part of the function rather than the full thing (so what fraction of the function do you need to compute in order to test for a collision?)  But there is even more you can do here: only the first 32-bits of the key are involved in the first 32-subrounds, and many of these permutations on the data overlap, leading to more speedups. Two important notes: (1) although the term “vanishing differential” suggests differential cryptanalysis (not suitable for a beginner), the term really just means hash collision here, and (2) RSA has since discontinued that function and is now using something more standard in their design.

If you know of any other good ones (including a sample break), then please provide the link and I will try to regularly update the list.

Advertisements

### Share this:

- [Twitter](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?share=twitter&nb=1)
- [Facebook101](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?share=facebook&nb=1)
- [Google](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?share=google-plus-1&nb=1)

-
[Like](https://widgets.wp.com/likes/#)

- [![vikdutt](../_resources/97a40500b2bca6b31af3bfa82b50948f.jpg)](http://en.gravatar.com/vikdutt)
- [![Simon](../_resources/ac378e3a3a2aa73a13499f5a46465045.jpg)](http://en.gravatar.com/simonorlovsky)
- [![yanapermana](../_resources/70776a9a9a2c3951b2ba1b98d60fb11e.png)](http://en.gravatar.com/yanapermana)

[3 bloggers](https://widgets.wp.com/likes/#) like this.

# Post navigation

[< A Retrospective on Ashely Madison and the Value of Threat Modeling](https://littlemaninmyhead.wordpress.com/2015/09/08/a-retrospective-on-ashely-madison-and-the-value-of-threat-modeling/)

[Cautionary note: UUIDs generally do not meet security requirements >](https://littlemaninmyhead.wordpress.com/2015/11/22/cautionary-note-uuids-should-generally-not-be-used-for-authentication-tokens/)

## 10 thoughts on “So, You Want to Learn to Break Ciphers”

1. Pingback: [Cautionary note: UUIDs should generally not be used for authentication tokens |](https://littlemaninmyhead.wordpress.com/2015/11/22/cautionary-note-uuids-should-generally-not-be-used-for-authentication-tokens/)

2. Pingback: [TECNOLOGÍA » Cautionary note: UUIDs generally do not meet security requirements](http://tecnologia.revistacocktel.com/cautionary-note-uuids-generally-do-not-meet-security-requirements/)

3. Pingback: [So, You Want to Learn to Break Ciphers – Evil Bits](https://vesselinux.wordpress.com/2017/02/01/so-you-want-to-learn-to-break-ciphers/)

4. ![ff125b88a22f3b075f1ac5f316b64e03.png](../_resources/c4845393809c92d6ef0ab800ebf4d1c9.png)**[John NoNotReally](http://john.almost.got.you/)**

[May 19, 2017 at 11:49 pm](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/#comment-237)

FYI, your first bolded statement has a grammatical error: “This blog post is written for and [missing “by”?] computer scientists without deep mathematics skills that want to learn how to do cryptanalysis, and teachers of cryptography for computer science students.”

Thanks for the read!

[](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?like_comment=237&_wpnonce=c5eda08006)Like

[Reply](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?replytocom=237#respond)

5. ![9fbd55908990c598fcf122e02a41bb8a.png](../_resources/770a7ad63348319065edb1a642106ce9.png)**Oscar**

[May 20, 2017 at 1:20 am](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/#comment-239)

> If you know of any other good ones (including a sample break), then please provide the link

> But I listened carefully, because I suspected an easy target that I wanted to have a go at.

This was my easy target.
https://github.com/ed770878/HohhaDynamicXOR

[](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?like_comment=239&_wpnonce=e3ba54e891)Like

[Reply](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?replytocom=239#respond)

6. Pingback: [So, You Want to Learn to Break Ciphers | ExtendTree](http://blog.extendtree.com/2017/05/19/so-you-want-to-learn-to-break-ciphers/)

7. ![6c0aaab2616b91ad7558a331d8d80e2c.png](../_resources/1c63fd45bddede90ef467255691a6429.png)**Foo**

[May 20, 2017 at 6:42 am](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/#comment-241)

Half of 2^62 is not 2^31, it’s 2^61.

[](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?like_comment=241&_wpnonce=c525c15941)Like

[Reply](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?replytocom=241#respond)

    1. ![f13fd0e1365753c8c3eb8e1e6072198c.jpg](../_resources/1d5cdb9c90a2cf01e6f8b847efb473e1.jpg)**[crazycontini](https://littlemaninmyhead.wordpress.com/)**

[May 20, 2017 at 11:54 am](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/#comment-243)

Correct. Not seeing where that matches up in the blog. In only place I talk about “half of the bits”, which is different than half of the complexity. Please clarify where you believe there is a mistake. Thanks.

[](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?like_comment=243&_wpnonce=6225556ce5)Like

[Reply](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?replytocom=243#respond)

8. ![d002c960c299dded41a9c6fe4b4d1e78.png](../_resources/072dc62b34052b0e98c635486d28baab.png)**Nivritatma**

[May 20, 2017 at 1:00 pm](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/#comment-244)

Can you tell how a mathematics student can learn cryptogrophy.
Thank you.

[](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?like_comment=244&_wpnonce=5f786d5d29)Like

[Reply](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?replytocom=244#respond)

    1. ![f13fd0e1365753c8c3eb8e1e6072198c.jpg](../_resources/1d5cdb9c90a2cf01e6f8b847efb473e1.jpg)**[crazycontini](https://littlemaninmyhead.wordpress.com/)**

[May 20, 2017 at 7:54 pm](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/#comment-246)

I would say first take a class on cryptography to find out what part of cryptography interests you. Once you know that, then you need to find where there are Professors who do research in the area that interests you, and try to become a graduate student under them, That way you would get guidance on where the field is going and understand better the skills you need to develop to understand and potentially contribute to the field.

There are many online courses for cryptography, but if you are good at mathematics, then you might look at Dan Boneh’s class: https://www.coursera.org/learn/crypto . I don’t think he’ll get into breaking symmetric ciphers like I have done above (a computer science algorithmic approach), but he will instead focus more on mathematical properties of ciphers, which will include application of mathematics to breaking ciphers.

You might also have a look at my recent blog on how I became a cryptographer: https://littlemaninmyhead.wordpress.com/2017/05/18/how-i-became-a-cryptographer/

and also Seny Kamara’s blog on How Not to Learn Cyrptography
http://outsourcedbits.org/2014/11/11/how-not-to-learn-cryptography/

[](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?like_comment=246&_wpnonce=8df010e595)Like

[Reply](https://littlemaninmyhead.wordpress.com/2015/09/28/so-you-want-to-learn-to-break-ciphers/?replytocom=246#respond)

### Leave a Reply