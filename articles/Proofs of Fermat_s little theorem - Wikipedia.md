Proofs of Fermat's little theorem - Wikipedia

# Proofs of Fermat's little theorem

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#mw-head)[Jump to search](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#p-search)

This article collects together a variety of [proofs](https://en.wikipedia.org/wiki/Mathematical_proof) of [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem), which states that

   {\displaystyle a^{p}\equiv a{\pmod {p}}}  ![7ff656f721894b9a50a2b1d18538463a6a4ec15f](../_resources/682334393633629c1a316a54b6eb3b52.png)

for every [prime number](https://en.wikipedia.org/wiki/Prime_number)  *p* and every [integer](https://en.wikipedia.org/wiki/Integer)  *a* (see [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)).

## Contents

[hide]

- [1  Simplifications](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Simplifications)
- [2  Combinatorial proofs](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Combinatorial_proofs)
    - [2.1  Proof by counting necklaces](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_by_counting_necklaces)
        - [2.1.1  Necklaces](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Necklaces)
        - [2.1.2  Completing the proof](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Completing_the_proof)
    - [2.2  Proof using dynamical systems](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_using_dynamical_systems)
    - [2.3  Multinomial proofs](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Multinomial_proofs)
        - [2.3.1  Proof using the binomial theorem](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_using_the_binomial_theorem)
        - [2.3.2  Proof using the multinomial expansion](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_using_the_multinomial_expansion)
    - [2.4  Proof using power product expansions](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_using_power_product_expansions)
- [3  Proof using modular arithmetic](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_using_modular_arithmetic)
    - [3.1  An example](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#An_example)
    - [3.2  The cancellation law](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#The_cancellation_law)
    - [3.3  The rearrangement property](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#The_rearrangement_property)
    - [3.4  Applications to Euler's theorem](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Applications_to_Euler's_theorem)
- [4  Proofs using group theory](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proofs_using_group_theory)
    - [4.1  Standard proof](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Standard_proof)
    - [4.2  Euler's proof](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Euler's_proof)
- [5  Notes](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Notes)

## Simplifications[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=1)]

Some of the **proofs of Fermat's little theorem** given below depend on two simplifications.

The first is that we may assume that *a* is in the range 0 ≤ *a* ≤ *p* − 1. This is a simple consequence of the laws of [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic); we are simply saying that we may first reduce *a* modulo *p*. This is consistent with reducing     {\displaystyle a^{p}}  ![37d19011bc97a33d35d6ca73f028cfeb87b4a3cf](../_resources/9dee27b38c101a6838b4ac93c2fdbd91.png) modulo *p*, as one can check.

Secondly, it suffices to prove that

   {\displaystyle a^{p-1}\equiv 1{\pmod {p}}}  ![5b71e80b05f598bfd9ac9618c87a94323e41e688](../_resources/99de001bcfd7f5b2eb601842a18f4e92.png)

for *a* in the range 1 ≤ *a* ≤ *p* − 1. Indeed, if the previous assertion holds for such *a*, multiplying both sides by *a* yields the original form of the theorem,

   {\displaystyle a^{p}\equiv a{\pmod {p}}}  ![7ff656f721894b9a50a2b1d18538463a6a4ec15f](../_resources/682334393633629c1a316a54b6eb3b52.png)

On the other hand, if *a* = 0, the theorem holds trivially.

## Combinatorial proofs[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=2)]

### Proof by counting necklaces[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=3)]

This is perhaps the simplest known proof, requiring the least mathematical background. It is an attractive example of a [combinatorial proof](https://en.wikipedia.org/wiki/Combinatorial_proof) (a proof that involves [counting a collection of objects in two different ways](https://en.wikipedia.org/wiki/Double_counting_(proof_technique))).

The proof given here is an adaptation of [Golomb](https://en.wikipedia.org/wiki/Solomon_W._Golomb)'s proof.[[1]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-1)

To keep things simple, let us assume that *a* is a [positive integer](https://en.wikipedia.org/wiki/Positive_integer). Consider all the possible [strings](https://en.wikipedia.org/wiki/String_(computer_science)) of *p* symbols, using an [alphabet](https://en.wikipedia.org/wiki/Alphabet) with *a* different symbols. The total number of such strings is *ap*, since there are *a* possibilities for each of *p* positions (see [rule of product](https://en.wikipedia.org/wiki/Rule_of_product)).

For example, if *p* = 5 and *a* = 2, then we can use an alphabet with two symbols (say *A* and *B*), and there are 25 = 32 strings of length 5:

*AAAAA*, *AAAAB*, *AAABA*, *AAABB*, *AABAA*, *AABAB*, *AABBA*, *AABBB*,
*ABAAA*, *ABAAB*, *ABABA*, *ABABB*, *ABBAA*, *ABBAB*, *ABBBA*, *ABBBB*,
*BAAAA*, *BAAAB*, *BAABA*, *BAABB*, *BABAA*, *BABAB*, *BABBA*, *BABBB*,
*BBAAA*, *BBAAB*, *BBABA*, *BBABB*, *BBBAA*, *BBBAB*, *BBBBA*, *BBBBB*.

We will argue below that if we remove the strings consisting of a single symbol from the list (in our example, *AAAAA* and *BBBBB*), the remaining *ap* − *a* strings can be arranged into groups, each group containing exactly *p* strings. It follows that *ap* − *a* is divisible by *p*.

#### Necklaces[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=4)]

[![166px-Proofs-of-Fermats-Little-Theorem-bracelet1.svg.png](../_resources/f2f810f25dfeb98d0ad7edf7156246f2.png)](https://en.wikipedia.org/wiki/File:Proofs-of-Fermats-Little-Theorem-bracelet1.svg)

Necklace representing seven different strings (*ABCBAAC*, *BCBAACA*, *CBAACAB*, *BAACABC*, *AACABCB*, *ACABCBA*, *CABCBAA*)

[![166px-Proofs-of-Fermats-Little-Theorem-bracelet2.svg.png](../_resources/0650483b038795c339be44b56cc1cc71.png)](https://en.wikipedia.org/wiki/File:Proofs-of-Fermats-Little-Theorem-bracelet2.svg)

Necklace representing only one string (*AAAAAAA*)

Let us think of each such string as representing a [necklace](https://en.wikipedia.org/wiki/Necklace_(combinatorics)). That is, we connect the two ends of the string together and regard two strings as the same necklace if we can [rotate](https://en.wikipedia.org/wiki/Circular_shift) one string to obtain the second string; in this case we will say that the two strings are *friends*. In our example, the following strings are all friends:

*AAAAB*, *AAABA*, *AABAA*, *ABAAA*, *BAAAA*.
Similarly, each line of the following list corresponds to a single necklace.
*AAABB*, *AABBA*, *ABBAA*, *BBAAA*, *BAAAB*,
*AABAB*, *ABABA*, *BABAA*, *ABAAB*, *BAABA*,
*AABBB*, *ABBBA*, *BBBAA*, *BBAAB*, *BAABB*,
*ABABB*, *BABBA*, *ABBAB*, *BBABA*, *BABAB*,
*ABBBB*, *BBBBA*, *BBBAB*, *BBABB*, *BABBB*,
*BAAAA*, *AAAAB*, *AAABA*, *AABAA*, *ABAAA*,
*AAAAA*,
*BBBBB*.

Notice that in the above list, some necklaces are represented by 5 different strings, and some only by a single string, so the list shows very clearly why 32 − 2 is divisible by 5.

One can use the following rule to work out how many friends a given string *S* has:

If *S* is built up of several copies of the string *T*, and *T* cannot itself be broken down further into repeating strings, then the number of friends of *S* (including *S* itself) is equal to the *length* of *T*.

For example, suppose we start with the string *S* = *ABBABBABBABB*, which is built up of several copies of the shorter string *T* = *ABB*. If we rotate it one symbol at a time, we obtain the following 3 strings:

*ABBABBABBABB*,
*BBABBABBABBA*,
*BABBABBABBAB*.

There aren't any others, because *ABB* is exactly 3 symbols long and cannot be broken down into further repeating strings.

#### Completing the proof[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=5)]

Using the above rule, we can complete the proof of Fermat's little theorem quite easily, as follows. Our starting pool of *a p* strings may be split into two categories:

- Some strings contain *p* identical symbols. There are exactly *a* of these, one for each symbol in the alphabet. (In our running example, these are the strings *AAAAA* and *BBBBB*.)
- The rest of the strings use at least two distinct symbols from the alphabet. If we can break up *S* into repeating copies of some string *T*, the length of *T* must divide the length of *S*. But, since the length of *S* is the prime *p*, the only possible length for *T* is also *p*. Therefore, the above rule tells us that *S* has exactly *p* friends (including *S* itself).

The second category contains *a p* − *a* strings, and they may be arranged into groups of *p* strings, one group for each necklace. Therefore, *a p* − *a* must be divisible by *p*, as promised.

### Proof using dynamical systems[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=6)]

This proof uses some basic concepts from [dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system).[[2]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-2)

We start by considering a family of [functions](https://en.wikipedia.org/wiki/Function_(mathematics))  *T**n*(*x*), where *n* ≥ 2 is an [integer](https://en.wikipedia.org/wiki/Integer), mapping the [interval](https://en.wikipedia.org/wiki/Interval_(mathematics)) [0, 1] to itself by the formula

   {\displaystyle T_{n}(x)={\begin{cases}\{nx\}&0\leq x<1,\\1&x=1,\end{cases}}}  ![8b801514162b9b87d27cc2fa1e270342da1a4b1c](../_resources/8de70a5b4c095632837f46dd1074f9ed.png)

where {*y*} denotes the [fractional part](https://en.wikipedia.org/wiki/Fractional_part) of *y*. For example, the function *T*3(*x*) is illustrated below:

[![Proofs-of-Fermats-Little-Theorem-dynamic1.png](../_resources/93a81466268d83bb1aec9922082e4c71.png)](https://en.wikipedia.org/wiki/File:Proofs-of-Fermats-Little-Theorem-dynamic1.png)

A number *x*0 is said to be a *[fixed point](https://en.wikipedia.org/wiki/Fixed_point_(mathematics))* of a function *f*(*x*) if *f*(*x*0) = *x*0; in other words, if *f* leaves *x*0 fixed. The fixed points of a function can be easily found graphically: they are simply the *x* coordinates of the points where the [graph](https://en.wikipedia.org/wiki/Graph_of_a_function) of *f*(*x*) intersects the graph of the line *y* = *x*. For example, the fixed points of the function *T*3(*x*) are 0, 1/2, and 1; they are marked by black circles on the following diagram:

[![270px-Proofs-of-Fermats-Little-Theorem-dynamic2.png](:/b760eacbb658fc02d11a9da778aa46fa)](https://en.wikipedia.org/wiki/File:Proofs-of-Fermats-Little-Theorem-dynamic2.png)

We will require the following two lemmas.

**Lemma 1.** For any *n* ≥ 2, the function *T**n*(*x*) has exactly *n* fixed points.

**Proof.** There are 3 fixed points in the illustration above, and the same sort of geometrical argument applies for any *n* ≥ 2.

**Lemma 2.** For any positive integers *n* and *m*, and any 0 ≤ x ≤ 1,

   {\displaystyle T_{m}(T_{n}(x))=T_{mn}(x).}  ![9d2ce61264a30682bf304b68d970237fd124143d](../_resources/b2d17ed2bccc16498883d1b74513480d.png)

In other words, *T**mn*(*x*) is the [composition](https://en.wikipedia.org/wiki/Function_composition) of *T**n*(*x*) and *T**m*(*x*).

**Proof.** The proof of this lemma is not difficult, but we need to be slightly careful with the endpoint *x* = 1. For this point the lemma is clearly true, since

   {\displaystyle T_{m}(T_{n}(1))=T_{m}(1)=1=T_{mn}(1).}  ![965fee3ec25fd1891c52a791a150c67e17cfaa14](../_resources/e3bdf5981da8f2295680292064d53056.png)

So let us assume that 0 ≤ *x* < 1. In this case,

   {\displaystyle T_{n}(x)=\{nx\}<1,}  ![63be9a2cac9167a67f31f698ece4469c182d940a](../_resources/0e02e168d3a33be3e8f56098bfebac45.png)

so *T**m*(*T**n*(*x*)) is given by

   {\displaystyle T_{m}(T_{n}(x))=\{m\{nx\}\}.}  ![a7842e3555f31a906056c9358ad35b89bf2e60f7](../_resources/ed4ef766e86738d35b78d16a81091797.png)

Therefore, what we really need to show is that

   {\displaystyle \{m\{nx\}\}=\{mnx\}.}  ![01052de6f8b0df66d369f2fa51c61ff15b278486](../_resources/b0eb7969906535a7dc8d04676c819a1d.png)

To do this we observe that {*nx*} = *nx* − *k*, where *k* is the [integer part](https://en.wikipedia.org/wiki/Integer_part) of *nx*; then

   {\displaystyle \{m\{nx\}\}=\{mnx-mk\}=\{mnx\},}  ![af1a1c019ea87ce57776c240b28d35bb5f1c3678](../_resources/c189989754d7a07b2717a48c852b66f6.png)

since *mk* is an integer.

Now let us properly begin the proof of Fermat's little theorem, by studying the function *T**a**p*(*x*). We will assume that *a* ≥ 2. From Lemma 1, we know that it has *a**p* fixed points. By Lemma 2 we know that

   {\displaystyle T_{a^{p}}(x)=\underbrace {T_{a}(T_{a}(\cdots T_{a}(x)\cdots ))} _{p{\text{ times}}},}  ![05d57ec30bc8b7e566b6f256b6e6906763d4288f](../_resources/d04dd043770bb7482771888636985069.png)

so any fixed point of *T**a*(*x*) is automatically a fixed point of *T**a**p*(*x*).

We are interested in the fixed points of *T**a**p*(*x*) that are *not* fixed points of *T**a*(*x*). Let us call the set of such points *S*. There are *a**p* − *a* points in *S*, because by Lemma 1 again, *T**a*(*x*) has exactly *a* fixed points. The following diagram illustrates the situation for *a* = 3 and *p* = 2. The black circles are the points of *S*, of which there are 32 − 3 = 6.

[![Proofs-of-Fermats-Little-Theorem-dynamic3.png](../_resources/df6c74b170175b9e669b49e469383ec8.png)](https://en.wikipedia.org/wiki/File:Proofs-of-Fermats-Little-Theorem-dynamic3.png)

The main idea of the proof is now to split the set *S* up into its [orbits](https://en.wikipedia.org/wiki/Orbit_(dynamics)) under *T**a*. What this means is that we pick a point *x*0 in *S*, and repeatedly apply *T**a*(x) to it, to obtain the sequence of points

   {\displaystyle x_{0},T_{a}(x_{0}),T_{a}(T_{a}(x_{0})),T_{a}(T_{a}(T_{a}(x_{0}))),\ldots .}  ![632c5bfcb7f1e5c945c6baf0304cdbd9077a23aa](../_resources/bcc4f13a036e7f23989c72d23acbbfff.png)

This sequence is called the orbit of *x*0 under *T**a*. By Lemma 2, this sequence can be rewritten as

   {\displaystyle x_{0},T_{a}(x_{0}),T_{a^{2}}(x_{0}),T_{a^{3}}(x_{0}),\ldots .}  ![862c8fd9526c12253f02c2d1fc92f5ba7a7bd62a](../_resources/b3669ec02a73e97a8c59d41dfbe8378e.png)

Since we are assuming that *x*0 is a fixed point of *T**a*  *p*(*x*), after *p* steps we hit *T**a**p*(*x*0) = *x*0, and from that point onwards the sequence repeats itself.

However, the sequence *cannot* begin repeating itself any earlier than that. If it did, the length of the repeating section would have to be a divisor of *p*, so it would have to be 1 (since *p* is prime). But this contradicts our assumption that *x*0 is not a fixed point of *T**a*.

In other words, the orbit contains exactly *p* distinct points. This holds for every orbit of *S*. Therefore, the set *S*, which contains *a**p* − *a* points, can be broken up into orbits, each containing *p* points, so *a**p* − *a* is divisible by *p*.

(This proof is essentially the same as the [necklace-counting proof](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_by_counting_necklaces) given above, simply viewed through a different lens: one may think of the interval [0, 1] as given by sequences of digits in base *a* (our distinction between 0 and 1 corresponding to the familiar distinction between representing integers as ending in ".0000..." and ".9999..."). *T**a**n* amounts to shifting such a sequence by *n* many digits. The fixed points of this will be sequences that are cyclic with period dividing *n*. In particular, the fixed points of *T**a**p* can be thought of as the necklaces of length *p*, with *T**a**n* corresponding to rotation of such necklaces by *n* spots.

This proof could also be presented without distinguishing between 0 and 1, simply using the half-open interval [0, 1); then *T**n* would only have *n* − 1 fixed points, but *T**a**p* − *T**a* would still work out to *a**p* − *a*, as needed.)

### Multinomial proofs[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=7)]

#### Proof using the binomial theorem[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=8)]

This proof, due to [Euler](https://en.wikipedia.org/wiki/Leonhard_Euler),[[3]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-Dickson-3) uses [induction](https://en.wikipedia.org/wiki/Mathematical_induction) to prove the theorem for all integers *a* ≥ 0.

The base step, that 0*p* ≡ 0 (mod *p*), is trivial. Next, we must show that if the theorem is true for *a* = *k*, then it is also true for *a* = *k* + 1. For this inductive step, we need the following lemma.

**Lemma**. For any integers *x* and *y* and for any prime *p*, (*x* + *y*)*p* ≡ *xp* + *yp* (mod *p*).

The lemma is a case of the [freshman's dream](https://en.wikipedia.org/wiki/Freshman%27s_dream). Leaving the proof for later on, we proceed with the induction.

**Proof**. Assume *k**p* ≡ *k* (mod *p*), and consider (*k*+1)*p*. By the lemma we have

   {\displaystyle (k+1)^{p}\equiv k^{p}+1^{p}{\pmod {p}}.}  ![ab6062f0cb72618004f0c2b18a4e6eec145b0673](../_resources/461c9bbbd39673f0f228af3b8ac382c9.png)

Using the induction hypothesis, we have that *k**p* ≡ *k* (mod *p*); and, trivially, 1*p* = 1. Thus

   {\displaystyle (k+1)^{p}\equiv k+1{\pmod {p}},}  ![7867472f159ec87a648ba8e47735c843d0bb0a66](../_resources/dcbd62010c83307f6368c5dceaab1828.png)

which is the statement of the theorem for *a* = *k*+1. ∎

In order to prove the lemma, we must introduce the [binomial theorem](https://en.wikipedia.org/wiki/Binomial_theorem), which states that for any positive integer *n*,

   {\displaystyle (x+y)^{n}=\sum _{i=0}^{n}{n \choose i}x^{n-i}y^{i},}  ![82e754436d23740062af927bc5455382b28bbff7](../_resources/cee224641f1525ae3363c68c75accadc.png)

where the coefficients are the [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficients),

   {\displaystyle {n \choose i}={\frac {n!}{i!(n-i)!}},}  ![6eb9f4c5fd4123a75f60dc0d2f838a8a1f6638f1](../_resources/29ce787dbd35263470261c15c6d489fc.png)

described in terms of the [factorial](https://en.wikipedia.org/wiki/Factorial) function, *n*! = 1×2×3×⋯×*n*.

**Proof of Lemma.** We consider the binomial coefficient when the exponent is a prime *p*:

   {\displaystyle {p \choose i}={\frac {p!}{i!(p-i)!}}}  ![0b2c564483df8926efa79a6d8e061e2d6b675b7d](../_resources/c0a776ce968400037ac32b5553b6f630.png)

The binomial coefficients are all integers. The numerator contains a factor *p* by the definition of factorial. When 0 < *i* < *p*, neither of the terms in the denominator includes a factor of *p* (relying on the primality of *p*), leaving the coefficient itself to possess a prime factor of *p* from the numerator, implying that

   {\displaystyle {p \choose i}\equiv 0{\pmod {p}},\qquad 0<i<p.}  ![412dcd0f6c05188606b6d8b84aa54ad659dbed35](../_resources/091a7b24643a3f28427ea7e74d8eacc5.png)

Modulo *p*, this eliminates all but the first and last terms of the sum on the right-hand side of the binomial theorem for prime *p*. ∎

The primality of *p* is essential to the lemma; otherwise, we have examples like

   {\displaystyle {4 \choose 2}=6,}  ![aeda28ae4d8d79f46a848d6abf2b9850e86da950](../_resources/c547b2cbdca572f9e48db2ddbe16a251.png)

which is not divisible by 4.

#### Proof using the multinomial expansion[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=9)]

The proof, which was first discovered by [Leibniz](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) (who did not publish it)[[4]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-4) and later rediscovered by [Euler](https://en.wikipedia.org/wiki/Leonhard_Euler),[[3]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-Dickson-3) is a very simple application of the [multinomial theorem](https://en.wikipedia.org/wiki/Multinomial_theorem) which is brought here for the sake of simplicity.

   {\displaystyle (x_{1}+x_{2}+\cdots +x_{m})^{n}=\sum _{k_{1},k_{2},\ldots ,k_{m}}{n \choose k_{1},k_{2},\ldots ,k_{m}}x_{1}^{k_{1}}x_{2}^{k_{2}}\cdots x_{m}^{k_{m}}.}  ![79e053209e40b8779abf1bc172e9654726ca1cc2](../_resources/cbde450eab5394b35087078b4a90cb08.png)

The summation is taken over all sequences of nonnegative integer indices *k*1 through *km* such the sum of all *ki* is *n*.

Thus if we express *a* as a sum of 1s (ones), we obtain

   {\displaystyle a^{p}=\sum _{k_{1},k_{2},\ldots ,k_{a}}{p \choose k_{1},k_{2},\ldots ,k_{a}}}  ![f99da27ea158b6103dc8aee8e58e0deb09790694](../_resources/96304993a8a735a06ca46fe9ff7f16ed.png)

Clearly, if *p* is prime, and if *kj* is not equal to *p* for any *j*, we have

   {\displaystyle {p \choose k_{1},k_{2},\ldots ,k_{a}}\equiv 0{\pmod {p}}}  ![025def543bc6ffa36f3354a5df831ef9842e509c](../_resources/bf34ca7cd8f052ee1a3f0e8506ef157d.png)

and

   {\displaystyle {p \choose k_{1},k_{2},\ldots ,k_{a}}\equiv 1{\pmod {p}}}  ![ac95f118a2cb0aeb87851821928ac4ff43906c8c](../_resources/a3fc6e544fbbd6e65af35f62f8f0a79d.png)

if *kj* is equal to *p* for some *j*.
Since there are exactly *a* elements such that *kj* = *p*, the theorem follows.

(This proof is essentially a coarser-grained variant of the [necklace-counting proof](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_by_counting_necklaces) given earlier; the multinomial coefficients count the number of ways a string can be permuted into arbitrary anagrams, while the necklace argument counts the number of ways a string can be rotated into cyclic anagrams. That is to say, that the nontrivial multinomial coefficients here are divisible by *p* can be seen as a consequence of the fact that each nontrivial necklace of length *p* can be unwrapped into a string in *p* many ways.

This multinomial expansion is also, of course, what essentially underlies the [binomial theorem-based proof](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_using_the_binomial_theorem) above)

### Proof using power product expansions[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=10)]

An additive-combinatorial proof based on formal power product expansions was given by Giedrius Alkauskas.[[5]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-5) This proof uses neither the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) nor the [binomial theorem](https://en.wikipedia.org/wiki/Binomial_theorem), but rather it employs [formal power series](https://en.wikipedia.org/wiki/Formal_power_series) with rational coefficients.

## Proof using modular arithmetic[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=11)]

This proof,[[3]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-Dickson-3)[[6]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-6) discovered by [James Ivory](https://en.wikipedia.org/wiki/James_Ivory_(mathematician))[[7]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-7) and rediscovered by [Dirichlet](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet)[[8]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-8) requires some background in [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic).

Let us assume that *a* is positive and not divisible by *p*. The idea is that if we write down the sequence of numbers

   {\displaystyle a,2a,3a,\ldots ,(p-1)a}  ![8688edd30d98265d7619cc0933aa293c9ee909a8](../_resources/429f1389f868e8d8ba7430a9f670ef6a.png)

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |

**(A)**

and reduce each one modulo *p*, the resulting sequence turns out to be a rearrangement of

   {\displaystyle 1,2,3,\ldots ,p-1.}  ![455131f385e159aa59c3307c38231c97ac33bc5f](../_resources/da4ea719afdd51f73fe1106fe5f804be.png)

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |

**(B)**

Therefore, if we multiply together the numbers in each sequence, the results must be identical modulo *p*:

   {\displaystyle a\times 2a\times 3a\times \cdots \times (p-1)a\equiv 1\times 2\times 3\times \cdots \times (p-1){\pmod {p}}.}  ![ccfaf374f459a7b9c49c05215782e671089eb31a](../_resources/b70d24f654350fd4a912cb6be7dbbe63.png)

Collecting together the *a* terms yields

   {\displaystyle a^{p-1}(p-1)!\equiv (p-1)!{\pmod {p}}.}  ![d4655a192086de5a8c7546eda59be1b74c0c36e9](../_resources/b53b63995d82dffeb0de8a6936ec9efe.png)

Finally, we may “cancel out” the numbers 1, 2, ..., *p* − 1 from both sides of this equation, obtaining

   {\displaystyle a^{p-1}\equiv 1{\pmod {p}}.}  ![58a9e1a77254c598a3bbd20ee75962c540381c54](../_resources/930ffbca674dfcb85c0dfa5f64269173.png)

There are two steps in the above proof that we need to justify:

- Why the elements of the sequence (**[A](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#math_A)**), reduced modulo *p*, are a rearrangement of (**[B](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#math_B)**), and
- Why it is valid to “cancel” in the setting of modular arithmetic.

We will prove these things below; let us first see an example of this proof in action.

### An example[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=12)]

If *a* = 3 and *p* = 7, then the sequence in question is

   {\displaystyle 3,6,9,12,15,18;}  ![51dc67cf9ed0adfc90c974534708981aeb30f817](../_resources/e98548d778eb08f6609f8d60516c3b47.png)

reducing modulo 7 gives

   {\displaystyle 3,6,2,5,1,4,}  ![91e334d25d6ef5847e522b88d8c9266756ed6915](../_resources/70978d1f91a40a47f7e0337a768b44ad.png)

which is just a rearrangement of

   {\displaystyle 1,2,3,4,5,6.}  ![13424f2c75bd0abaeefded67b6fa9b06754e2d3a](../_resources/4dc95be81d6907b320487c9603bfe595.png)

Multiplying them together gives

   {\displaystyle 3\times 6\times 9\times 12\times 15\times 18\equiv 3\times 6\times 2\times 5\times 1\times 4\equiv 1\times 2\times 3\times 4\times 5\times 6{\pmod {7}};}  ![56d7a5107199555a580816b9d6a61aa545b049f1](../_resources/8e60f31b28a863f54acd953bad51ec77.png)

that is,

   {\displaystyle 3^{6}(1\times 2\times 3\times 4\times 5\times 6)\equiv (1\times 2\times 3\times 4\times 5\times 6){\pmod {7}}.}  ![bf0401c8f80a231fa604d7338847fb2312aefd56](../_resources/a3a41aac84ed18fd608bf7333bcbe9a1.png)

Canceling out 1 × 2 × 3 × 4 × 5 × 6 yields

   {\displaystyle 3^{6}\equiv 1{\pmod {7}},}  ![c1ed1be152bab93fb03e553d72d001215febf7e1](../_resources/cb0bdcc48b910fc0390e5b53c480b096.png)

which is Fermat's little theorem for the case *a* = 3 and *p* = 7.

### The cancellation law[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=13)]

Let us first explain why it is valid, in certain situations, to “cancel”. The exact statement is as follows. If *u*, *x*, and *y* are integers, and *u* is not divisible by a prime number *p*, and if

   {\displaystyle ux\equiv uy{\pmod {p}},}  ![7dfb6d57a41c98d65a87487e2a5023e00c2dedde](../_resources/9276c4e00a2c8675864bc9ce331ef324.png)

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |

**(C)**
then we may “cancel” *u* to obtain

   {\displaystyle x\equiv y{\pmod {p}}.}  ![0aa15f21005c1c068194355f89c1f24406975655](../_resources/9aa96ced6c8e35b15f62e272d44c02b2.png)

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |

**(D)**

Our use of this **cancellation law** in the above proof of Fermat's little theorem was valid, because the numbers 1, 2, ..., *p* − 1 are certainly not divisible by *p* (indeed they are *smaller* than *p*).

We can prove the cancellation law easily using [Euclid's lemma](https://en.wikipedia.org/wiki/Euclid%27s_lemma), which generally states that if a prime *p* divides a product *ab* (where *a* and *b* are integers), then *p* must divide *a* or *b*. Indeed, the assertion (**[C](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#math_C)**) simply means that *p* divides *ux* − *uy* = *u*(*x* − *y*). Since *p* is a prime which does not divide *u*, Euclid's lemma tells us that it must divide *x* − *y* instead; that is, (**[D](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#math_D)**) holds.

Note that the conditions under which the cancellation law holds are quite strict, and this explains why Fermat's little theorem demands that *p* is a prime. For example, 2×2 ≡ 2×5 (mod 6), but it is not true that 2 ≡ 5 (mod 6). However, the following generalization of the cancellation law holds: if *u*, *x*, *y*, and *z* are integers, if *u* and *z* are [relatively prime](https://en.wikipedia.org/wiki/Coprime_integers), and if

   {\displaystyle ux\equiv uy{\pmod {z}},}  ![5aba3324a5a3505a1147d8e1365987f90f8af151](../_resources/5ebca0af37ffb2ae804109dbff9bb15c.png)

then we may “cancel” **u** to obtain

   {\displaystyle x\equiv y{\pmod {z}}.}  ![029f8948ea5cd18fdd109688c25423b00b566c4b](../_resources/619ca4ac2e14ab59e291dc006af76d08.png)

This follows from a [generalization of Euclid's lemma](https://en.wikipedia.org/wiki/Euclid%27s_lemma#Proof).

### The rearrangement property[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=14)]

Finally, we must explain why the sequence

   {\displaystyle a,2a,3a,\ldots ,(p-1)a,}  ![888b8d2ff5b9f0640eafb928e1328c6e4462673b](../_resources/e78c791b82a19ce8d67141a42cc5a66d.png)

when reduced modulo *p*, becomes a rearrangement of the sequence

   {\displaystyle 1,2,3,\ldots ,p-1.}  ![455131f385e159aa59c3307c38231c97ac33bc5f](../_resources/da4ea719afdd51f73fe1106fe5f804be.png)

To start with, none of the terms *a*, 2*a*, ..., (*p* − 1)*a* can be congruent to zero modulo *p*, since if *k* is one of the numbers 1, 2, ..., *p* − 1, then *k* is relatively prime with *p*, and so is *a*, so [Euclid's lemma](https://en.wikipedia.org/wiki/Euclid%27s_lemma) tells us that *ka* shares no factor with *p*. Therefore, at least we know that the numbers *a*, 2*a*, ..., (*p* − 1)*a*, when reduced modulo *p*, must be found among the numbers 1, 2, 3, ..., *p* − 1.

Furthermore, the numbers *a*, 2*a*, ..., (*p* − 1)*a* must all be *distinct* after reducing them modulo *p*, because if

   {\displaystyle ka\equiv ma{\pmod {p}},}  ![ba5d8842ed71d88150def6f434ddeb0f8accc13b](../_resources/eeda713f94dea15428f1cc5a54ba90c4.png)

where *k* and *m* are one of 1, 2, ..., *p* − 1, then the cancellation law tells us that

   {\displaystyle k\equiv m{\pmod {p}}.}  ![13b1ed2e51222f6c88783e24d094cb3319dc7edd](../_resources/5ce306d24c6dfcc81adb7f8916b5a33d.png)

Since both *k* and *m* are between 1 and *p* − 1, they must be equal. Therefore, the terms *a*, 2*a*, ..., (*p* − 1)*a* when reduced modulo *p* must be distinct. To summarise: when we reduce the *p* − 1 numbers *a*, 2*a*, ..., (*p* − 1)*a* modulo *p*, we obtain distinct members of the sequence 1, 2, ..., *p* − 1. Since there are exactly *p* − 1 of these, the only possibility is that the former are a rearrangement of the latter.

### Applications to Euler's theorem[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=15)]

This method can also be used to prove [Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem), with a slight alteration in that the numbers from 1 to *p* − 1 are substituted by the numbers less than and coprime with some number *m* (not necessarily prime). Both the rearrangement property and the cancellation law (under the generalized form mentioned [above](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#The_cancellation_law)) are still satisfied and can be utilized.

For example, if *m* = 10, then the numbers less than *m* and coprime with *m* are 1, 3, 7, and 9. Thus we have:

   {\displaystyle a\times 3a\times 7a\times 9a\equiv 1\times 3\times 7\times 9{\pmod {10}}.}  ![c3a20173026509d1ed5e6c126752f6ef2e546d5d](../_resources/7360413c41064e09860aa5e802931784.png)

Therefore,

   {\displaystyle {a^{\varphi (10)}}\equiv 1{\pmod {10}}.}  ![f0db6d5f4387c80d09ae1df2454c164680e5fa23](../_resources/a01bbf13b3b4d58a12003095e2aa6639.png)

## Proofs using group theory[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=16)]

### Standard proof[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=17)]

This proof[[9]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-9) requires the most basic elements of [group theory](https://en.wikipedia.org/wiki/Group_theory).

The idea is to recognise that the set *G* = {1, 2, …, *p* − 1}, with the operation of multiplication (taken modulo *p*), forms a [group](https://en.wikipedia.org/wiki/Group_(mathematics)). The only group axiom that requires some effort to verify is that each element of *G* is invertible. Taking this on faith for the moment, let us assume that *a* is in the range 1 ≤ *a* ≤ *p* − 1, that is, *a* is an element of *G*. Let *k* be the [order](https://en.wikipedia.org/wiki/Order_(group_theory)) of *a*, that is, *k* is the smallest positive integer such that *ak* ≡ 1 (mod *p*). Then the numbers 1, *a*, *a*2, ..., *a**k* −1 reduced modulo *p* form a [subgroup](https://en.wikipedia.org/wiki/Subgroup) of *G* whose [order](https://en.wikipedia.org/wiki/Order_(group_theory)) is *k* and therefore, by [Lagrange's theorem](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)), *k* divides the order of *G*, which is *p* − 1. So *p* − 1 = *km* for some positive integer *m* and then

   {\displaystyle a^{p-1}\equiv a^{km}\equiv (a^{k})^{m}\equiv 1^{m}\equiv 1{\pmod {p}}.}  ![d4b07637f11a227d7b52ddeae35facaef8ae6625](../_resources/7708c01a8e3ea6a6b40d4dd8dc753a0a.png)

To prove that every element *b* of *G* is invertible, we may proceed as follows. First, *b* is [coprime](https://en.wikipedia.org/wiki/Coprime_integers) to *p*. Thus [Bézout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity) assures us that there are integers *x* and *y* such that *bx* + *py* = 1. Reading this equality modulo *p*, we see that *x* is an inverse for *b*, since *bx* ≡ 1 (mod *p*). Therefore, every element of *G* is invertible. So, as remarked earlier, *G* is a group.

For example, when *p* = 11, the inverses of each element are given as follows:

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *a* | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| *a* −1 | 1   | 6   | 4   | 3   | 9   | 2   | 8   | 7   | 5   | 10  |

### Euler's proof[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=18)]

If we take the previous proof and, instead of using Lagrange's theorem, we try to prove it in this specific situation, then we get Euler's third proof, which is the one that he found more natural.[[10]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-10)[[11]](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_note-11) Let *A* be the set whose elements are the numbers 1, *a*, *a*2, ..., *a**k* − 1 reduced modulo *p*. If *A* = *G*, then *k* = *p* − 1 and therefore *k* divides *p* −1. Otherwise, there is some *b*1 ∈ *G*\*A*.

Let *A*1 be the set whose elements are the numbers *b*1, *ab*1, *a*2*b*1, …, *a**k* − 1*b*1 reduced modulo *p*. Then *A*1 has *k* distinct elements, because otherwise there would be two distinct numbers *m*, *n* ∈ {0, 1, ..., *k* − 1} such that *amb*1 ≡ *anb*1 (mod *p*), which is impossible, since it would follow that *am* ≡ *an* (mod *p*). On the other hand, no element of *A*1 can be an element of *A*, because otherwise there would be numbers *m*, *n* ∈ {0, 1, …, *k* − 1} such that *amb*1 ≡ *an* (mod *p*), and then *b*1 ≡ *ana**k* − *m* ≡ *a**n* + *k* − *m* (mod *p*), which is impossible, since *b*1 ∉ *A*.

So, the set *A*∪*A*1 has 2*k* elements. If it turns out to be equal to *G*, then 2*k* = *p* −1 and therefore *k* divides *p* −1. Otherwise, there is some *b*2 ∈ *G*\(*A*∪*A*1) and we can start all over again, defining *A*2 as the set whose elements are the numbers *b*2, *ab*2, *a*2*b*2, ..., *a**k* − 1*b*2 reduced modulo *p*. Since *G* is finite, this process must stop at some point and this proves that *k* divides *p* − 1.

For instance, if *a* = 5 and *p* = 13, then, since

- 52 = 25 ≡ 12 (mod 13),
- 53 = 125 ≡ 8 (mod 13),
- 54 = 625 ≡ 1 (mod 13),

we have *k* = 4 and *A* = {1, 5, 8, 12}. Clearly, *A* ≠ *G* = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}. Let *b*1 be an element of *G*\*A*; for instance, take *b*1 = 2. Then, since

- 2×1 = 2,
- 2×5 = 10,
- 2×8 = 16 ≡ 3 (mod 13),
- 2×12 = 24 ≡ 11 (mod 13),

we have *A*1 = {2, 3, 10, 11}. Clearly, *A*∪*A*1 ≠ *G*. Let *b*2 be an element of *G*\(*A*∪*A*1); for instance, take *b*2 = 4. Then, since

- 4×1 = 4,
- 4×5 = 20 ≡ 7 (mod 13),
- 4×8 = 32 ≡ 6 (mod 13),
- 4×12 = 48 ≡ 9 (mod 13),

we have *A*2 = {4, 6, 7, 9}. And now *G* = *A*∪*A*1∪*A*2.

Note that the sets *A*, *A*1, and so on are in fact the [cosets](https://en.wikipedia.org/wiki/Coset) of *A* in *G*.

## Notes[[edit](https://en.wikipedia.org/w/index.php?title=Proofs_of_Fermat%27s_little_theorem&action=edit&section=19)]

1. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-1)**  [Golomb, Solomon W.](https://en.wikipedia.org/wiki/Solomon_W._Golomb) (1956), ["Combinatorial proof of Fermat's "Little" Theorem"](http://www.cimat.mx/~mmoreno/teaching/spring08/Fermats_Little_Thm.pdf)  (PDF), *[American Mathematical Monthly](https://en.wikipedia.org/wiki/American_Mathematical_Monthly)*, **63** (10): 718, [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.2307/2309563](https://doi.org/10.2307%2F2309563), [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [2309563](https://www.jstor.org/stable/2309563)

2. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-2)**  Iga, Kevin (2003), "A Dynamical Systems Proof of Fermat's Little Theorem", *[Mathematics Magazine](https://en.wikipedia.org/wiki/Mathematics_Magazine)*, **76** (1): 48–51, [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.2307/3219132](https://doi.org/10.2307%2F3219132), [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [3219132](https://www.jstor.org/stable/3219132)

3. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-Dickson_3-0)  [***b***](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-Dickson_3-1)  [***c***](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-Dickson_3-2)  [Dickson, Leonard Eugene](https://en.wikipedia.org/wiki/Leonard_Eugene_Dickson) (2005) [1919], "Fermat's and Wilson's theorems, generalizations, and converses; symmetric funcions of 1, 2, ..., *p* − 1 modulo *p*", [*History of the Theory of Numbers*](https://en.wikipedia.org/wiki/History_of_the_Theory_of_Numbers), **I**, [Dover](https://en.wikipedia.org/wiki/Dover_Publications), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-486-44232-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-44232-7), [Zbl](https://en.wikipedia.org/wiki/Zentralblatt_MATH) [1214.11001](https://zbmath.org/?format=complete&q=an:1214.11001)

4. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-4)**  [Vacca, Giovanni](https://en.wikipedia.org/wiki/Giovanni_Vacca_(mathematician)) (1894), "Intorno alla prima dimostrazione di un teorema di Fermat", *Bibliotheca Mathematica*, 2nd series (in Italian), **8** (2): 46–48

5. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-5)**  Alkauskas, Giedrius (2009), "A Curious Proof of Fermat's Little Theorem", *[American Mathematical Monthly](https://en.wikipedia.org/wiki/American_Mathematical_Monthly)*, **116** (4): 362–364, [arXiv](https://en.wikipedia.org/wiki/ArXiv):[0801.0805](https://arxiv.org/abs/0801.0805), [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.4169/193009709x470236](https://doi.org/10.4169%2F193009709x470236), [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [40391097](https://www.jstor.org/stable/40391097)

6. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-6)**  [Hardy, G. H.](https://en.wikipedia.org/wiki/G._H._Hardy); [Wright, E. M.](https://en.wikipedia.org/wiki/E._M._Wright) (2008), "Fermat's Theorem and its Consequences", [*An Introduction to the Theory of Numbers*](https://en.wikipedia.org/wiki/An_Introduction_to_the_Theory_of_Numbers) (6th ed.), [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-19-921986-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-921986-5)

7. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-7)**  [Ivory, James](https://en.wikipedia.org/wiki/James_Ivory_(mathematician)) (1806), "Demonstration of a theorem respecting prime numbers", *New Series of the Mathematical Depository*, **1** (II): 6–8

8. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-8)**  [Lejeune Dirichlet, Peter Gustav](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet) (1828), "Démonstrations nouvelles de quelques théorèmes relatifs aux nombres", *[Journal für die reine und angewandte Mathematik](https://en.wikipedia.org/wiki/Crelle%27s_Journal)* (in French), **3**: 390–393

9. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-9)**  [Weil, André](https://en.wikipedia.org/wiki/Andr%C3%A9_Weil); [Rosenlicht, Maxwell](https://en.wikipedia.org/wiki/Maxwell_Rosenlicht) (1979), "§ VIII", [*Number Theory for beginners*](https://archive.org/details/numbertheoryforb0000weil), [Springer-Verlag](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/978-1-4612-9957-8](https://doi.org/10.1007%2F978-1-4612-9957-8), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-387-90381-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-90381-1), [Zbl](https://en.wikipedia.org/wiki/Zentralblatt_MATH) [0405.10001](https://zbmath.org/?format=complete&q=an:0405.10001)

10. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-10)**  [Weil, André](https://en.wikipedia.org/wiki/Andr%C3%A9_Weil) (2007) [1984], "§ III.VI", *Number theory: An approach through history; from Hammurapi to Legendre*, [Birkhäuser](https://en.wikipedia.org/wiki/Birkh%C3%A4user), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-8176-4565-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8176-4565-6), [Zbl](https://en.wikipedia.org/wiki/Zentralblatt_MATH) [1149.01013](https://zbmath.org/?format=complete&q=an:1149.01013)

11. **[^](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#cite_ref-11)**  [Euler, Leonhard](https://en.wikipedia.org/wiki/Leonhard_Euler) (1761), ["Theoremata circa residua ex divisione potestatum relicta"](http://math.dartmouth.edu/~euler/docs/originals/E262.pdf)  (PDF), *Novi Commentarii Academiae Scientiarum Petropolitanae* (in Latin), **7**: 49–82

[Categories](https://en.wikipedia.org/wiki/Help:Category):

- [Modular arithmetic](https://en.wikipedia.org/wiki/Category:Modular_arithmetic)
- [Number theory](https://en.wikipedia.org/wiki/Category:Number_theory)
- [Article proofs](https://en.wikipedia.org/wiki/Category:Article_proofs)