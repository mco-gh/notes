Fundamental theorem of arithmetic - Wikipedia

# Fundamental theorem of arithmetic

From Wikipedia, the free encyclopedia

Not to be confused with [Fundamental theorem of algebra](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra).

In [number theory](https://en.wikipedia.org/wiki/Number_theory), the **fundamental theorem of arithmetic**, also called the **unique factorization theorem** or the **unique-prime-factorization theorem**, states that every [integer](https://en.wikipedia.org/wiki/Integer) greater than 1[[3]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-3) either is a [prime number](https://en.wikipedia.org/wiki/Prime_number) itself or can be represented as the product of prime numbers; moreover, this representation is unique, [up to](https://en.wikipedia.org/wiki/Up_to) (except for) the order of the factors.[[4]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-4)[[5]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-5)[[6]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-6) For example,

1200 = 24 × 31 × 52 = 5 × 2 × 5 × 2 × 3 × 2 × 2 = ...

The theorem is stating two things: first, that 1200 *can* be represented as a product of primes, and second, no matter how this is done, there will always be four 2s, one 3, two 5s, and no other primes in the product.

The requirement that the factors be prime is necessary: factorizations containing [composite numbers](https://en.wikipedia.org/wiki/Composite_number) may not be unique (e.g., 12 = 2 × 6 = 3 × 4).

This theorem is one of the main [reasons why 1 is not considered a prime number](https://en.wikipedia.org/wiki/Prime_number#Primality_of_one): if 1 were prime, then factorization into primes would not be unique; for example, 2 = 2×1 = 2×1×1 = ...

## Euclid's original version[]

Book VII, propositions 30, 31 and 32, and Book IX, proposition 14 of [Euclid](https://en.wikipedia.org/wiki/Euclid)'s *[Elements](https://en.wikipedia.org/wiki/Euclid%27s_Elements)* are essentially the statement and proof of the fundamental theorem.

> If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

> — > Euclid, > [> Elements Book VII](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFEuclidHeath1956)> , Proposition 30

(In modern terminology: if a prime *p* divides the product *ab*, then *p* divides either *a* or *b* or both.) Proposition 30 is referred to as [Euclid's lemma](https://en.wikipedia.org/wiki/Euclid%27s_lemma). And it is the key in the proof of the fundamental theorem of arithmetic.

> Any composite number is measured by some prime number.

> — > Euclid, > [> Elements Book VII](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFEuclidHeath1956)> , Proposition 31

(In modern terminology: every integer greater than one is divided evenly by some prime number.) Proposition 31 is proved directly by [infinite descent](https://en.wikipedia.org/wiki/Proof_by_infinite_descent).

> Any number either is prime or is measured by some prime number.

> — > Euclid, > [> Elements Book VII](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFEuclidHeath1956)> , Proposition 32

Proposition 32 is derived from proposition 31, and proves that the decomposition is possible.

> If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

> — > Euclid, > [> Elements Book IX](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFEuclidHeath1956)> , Proposition 14

(In modern terminology: a [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple) of several prime numbers is not a multiple of any other prime number.) Book IX, proposition 14 is derived from Book VII, proposition 30, and prove partially that the decomposition is unique – a point critically noted by [André Weil](https://en.wikipedia.org/wiki/Andr%C3%A9_Weil).[[7]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-7) Indeed, in this proposition the exponents are all equal to one, so nothing is said for the general case.

Article 16 of [Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss)' *[Disquisitiones Arithmeticae](https://en.wikipedia.org/wiki/Disquisitiones_Arithmeticae)* is an early modern statement and proof employing [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic).[[1]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-Gauss1801.loc=16-1)

## Applications[]

### Canonical representation of a positive integer[]

Every positive integer *n* > 1 can be represented in exactly one way as a product of prime powers:

       n  =    p    1        n    1            p    2        n    2          ⋯    p    k        n    k          =    ∏    i  =  1      k        p    i        n    i              {\displaystyle n=p_{1}^{n_{1}}p_{2}^{n_{2}}\cdots p_{k}^{n_{k}}=\prod _{i=1}^{k}p_{i}^{n_{i}}}  [{\displaystyle n=p_{1}^{n_{1}}p_{2}^{n_{2}}\cdots p_{k}^{n_{k}}=\prod _{i=1}^{k}p_{i}^{n_{i}}}](../_resources/879d76b4d7bb16aa633365b498fca8fa.bin)

where *p*1 < *p*2 < ... < *p*k are primes and the *n**i* are positive integers. This representation is commonly extended to all positive integers, including 1, by the convention that the [empty product](https://en.wikipedia.org/wiki/Empty_product) is equal to 1 (the empty product corresponds to *k* = 0).

This representation is called the **canonical representation**[[8]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-8) of *n*, or the **standard form**[[9]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-9)[[10]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-10) of *n*. For example,

999 = 33×37,
1000 = 23×53,
1001 = 7×11×13.

Note that factors *p*0 = 1 may be inserted without changing the value of *n* (e.g., 1000 = 23×30×53).

In fact, any positive integer can be uniquely represented as an [infinite product](https://en.wikipedia.org/wiki/Infinite_product) taken over all the positive prime numbers:

       n  =    2      n    1            3      n    2            5      n    3            7      n    4          ⋯  =    ∏    i  =  1      ∞        p    i        n    i          ,      {\displaystyle n=2^{n_{1}}3^{n_{2}}5^{n_{3}}7^{n_{4}}\cdots =\prod _{i=1}^{\infty }p_{i}^{n_{i}},}  [{\displaystyle n=2^{n_{1}}3^{n_{2}}5^{n_{3}}7^{n_{4}}\cdots =\prod _{i=1}^{\infty }p_{i}^{n_{i}},}](../_resources/84bf7c9b5e5e7be443b32936e47ef050.bin)

where a finite number of the *n**i* are positive integers, and the rest are zero. Allowing negative exponents provides a canonical form for positive [rational numbers](https://en.wikipedia.org/wiki/Rational_number).

### Arithmetic operations[]

The canonical representations of the product, [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) (GCD), and [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple) (LCM) of two numbers *a* and *b* can be expressed simply in terms of the canonical representations of *a* and *b* themselves:

               a  ⋅  b      =    2      a    1      +    b    1            3      a    2      +    b    2            5      a    3      +    b    3            7      a    4      +    b    4          ⋯      =  ∏    p    i        a    i      +    b    i          ,          gcd  (  a  ,  b  )      =    2    min  (    a    1      ,    b    1      )        3    min  (    a    2      ,    b    2      )        5    min  (    a    3      ,    b    3      )        7    min  (    a    4      ,    b    4      )      ⋯      =  ∏    p    i      min  (    a    i      ,    b    i      )      ,          lcm  ⁡  (  a  ,  b  )      =    2    max  (    a    1      ,    b    1      )        3    max  (    a    2      ,    b    2      )        5    max  (    a    3      ,    b    3      )        7    max  (    a    4      ,    b    4      )      ⋯      =  ∏    p    i      max  (    a    i      ,    b    i      )      .              {\displaystyle {\begin{alignedat}{2}a\cdot b&{}={}2^{a_{1}+b_{1}}3^{a_{2}+b_{2}}5^{a_{3}+b_{3}}7^{a_{4}+b_{4}}\cdots &&{}={}\prod p_{i}^{a_{i}+b_{i}},\\\gcd(a,b)&{}={}2^{\min(a_{1},b_{1})}3^{\min(a_{2},b_{2})}5^{\min(a_{3},b_{3})}7^{\min(a_{4},b_{4})}\cdots &&{}={}\prod p_{i}^{\min(a_{i},b_{i})},\\\operatorname {lcm} (a,b)&{}={}2^{\max(a_{1},b_{1})}3^{\max(a_{2},b_{2})}5^{\max(a_{3},b_{3})}7^{\max(a_{4},b_{4})}\cdots &&{}={}\prod p_{i}^{\max(a_{i},b_{i})}.\end{alignedat}}}

[{\displaystyle {\begin{alignedat}{2}a\cdot b&{}={}2^{a_{1}+b_{1}}3^{a_{2}+b_{2}}5^{a_{3}+b_{3}}7^{a_{4}+b_{4}}\cdots &&{}={}\prod p_{i}^{a_{i}+b_{i}},\\\gcd(a,b)&{}={}2^{\min(a_{1},b_{1})}3^{\min(a_{2},b_{2})}5^{\min(a_{3},b_{3})}7^{\min(a_{4},b_{4})}\cdots &&{}={}\prod p_{i}^{\min(a_{i},b_{i})},\\\operatorname {lcm} (a,b)&{}={}2^{\max(a_{1},b_{1})}3^{\max(a_{2},b_{2})}5^{\max(a_{3},b_{3})}7^{\max(a_{4},b_{4})}\cdots &&{}={}\prod p_{i}^{\max(a_{i},b_{i})}.\end{alignedat}}}](../_resources/b822138db19ab9e986d731c8db2a97a2.bin)

However, [integer factorization](https://en.wikipedia.org/wiki/Integer_factorization), especially of large numbers, is much more difficult than computing products, GCDs, or LCMs. So these formulas have limited use in practice.

### Arithmetic functions[]

Main article: [Arithmetic function](https://en.wikipedia.org/wiki/Arithmetic_function)

Many arithmetic functions are defined using the canonical representation. In particular, the values of [additive](https://en.wikipedia.org/wiki/Additive_function) and [multiplicative](https://en.wikipedia.org/wiki/Multiplicative_function) functions are determined by their values on the powers of prime numbers.

## Proof[]

The proof uses [Euclid's lemma](https://en.wikipedia.org/wiki/Euclid%27s_lemma) (*Elements* VII, 30): if a prime *p*  [divides](https://en.wikipedia.org/wiki/Divisor) the product of two [natural numbers](https://en.wikipedia.org/wiki/Natural_number)  *a* and *b*, then *p* divides *a* or *p* divides *b*.

### Existence[]

We need to show that every integer greater than 1 is either prime or a product of primes. For the base case, note that 2 is prime. By [strong induction](https://en.wikipedia.org/wiki/Strong_induction): assume true for all numbers between 1 and *n*. If *n* is prime, there is nothing more to prove. Otherwise, there are integers *a* and *b*, where *n* = *ab* and 1 < *a* ≤ *b* < *n*. By the induction hypothesis, *a* = *p*1*p*2...*p**j* and *b* = *q*1*q*2...*q**k* are products of primes. But then *n* = *ab* = *p*1*p*2...*p**j**q*1*q*2...*q**k* is a product of primes.

### Uniqueness[]

Assume that *s* > 1 is the product of prime numbers in two different ways:

               s      =    p    1        p    2      ⋯    p    m              =    q    1        q    2      ⋯    q    n      .              {\displaystyle {\begin{aligned}s&=p_{1}p_{2}\cdots p_{m}\\&=q_{1}q_{2}\cdots q_{n}.\end{aligned}}}  [{\begin{aligned}s&=p_{1}p_{2}\cdots p_{m}\\&=q_{1}q_{2}\cdots q_{n}.\end{aligned}}](../_resources/a54700e4ebcd0cc83ca3212fb979fbf0.bin)

We must show *m* = *n* and that the *q**j* are a rearrangement of the *p**i*.

As *p*1 divides *s*, [Euclid's lemma](https://en.wikipedia.org/wiki/Euclid%27s_lemma) implies that *p*1 divides one of the *q**j*; relabeling the *q**j* if necessary, say that *p*1 divides *q*1. But *q*1 is prime, so its only divisors are itself and 1. Therefore, *p*1 = *q*1, so that

                   s    p    1              =    p    2      ⋯    p    m              =    q    2      ⋯    q    n      .              {\displaystyle {\begin{aligned}{\frac {s}{p_{1}}}&=p_{2}\cdots p_{m}\\&=q_{2}\cdots q_{n}.\end{aligned}}}  [{\begin{aligned}{\frac {s}{p_{1}}}&=p_{2}\cdots p_{m}\\&=q_{2}\cdots q_{n}.\end{aligned}}](../_resources/c74811c583f84df3e1764aee71df4c63.bin)

Reasoning the same way, *p*2 must equal one of the remaining *q**j*. Relabeling again if necessary, say *p*2 = *q*2. Then

                   s      p    1        p    2                =    p    3      ⋯    p    m              =    q    3      ⋯    q    n      .              {\displaystyle {\begin{aligned}{\frac {s}{p_{1}p_{2}}}&=p_{3}\cdots p_{m}\\&=q_{3}\cdots q_{n}.\end{aligned}}}  [{\begin{aligned}{\frac {s}{p_{1}p_{2}}}&=p_{3}\cdots p_{m}\\&=q_{3}\cdots q_{n}.\end{aligned}}](../_resources/8e56d7fbd35a3382776f8ff475061d92.bin)

This can be done for each of the *m*  *p**i*'s, showing that *m* ≤ *n* and every *p**i* is a *q**j*. Applying the same argument with the         p      {\displaystyle p}  [p](../_resources/def00db8a472d01b3571111bbc647feb.bin)'s and         q      {\displaystyle q}  [q](../_resources/281e2b283fde8023424a7bd9631164d4.bin)'s reversed shows *n* ≤ *m* (hence *m* = *n*) and every *q**j* is a *p**i*.

### Elementary proof of uniqueness[]

The fundamental theorem of arithmetic can also be proved without using Euclid's lemma, as follows:

Assume that *s* > 1 is the smallest positive integer which is the product of prime numbers in two different ways. If *s* were prime then it would factor uniquely as itself, so there must be at least two primes in each factorization of *s*:

               s      =    p    1        p    2      ⋯    p    m              =    q    1        q    2      ⋯    q    n      .              {\displaystyle {\begin{aligned}s&=p_{1}p_{2}\cdots p_{m}\\&=q_{1}q_{2}\cdots q_{n}.\end{aligned}}}  [{\begin{aligned}s&=p_{1}p_{2}\cdots p_{m}\\&=q_{1}q_{2}\cdots q_{n}.\end{aligned}}](../_resources/a54700e4ebcd0cc83ca3212fb979fbf0.bin)

If any *p**i* = *q**j* then, by cancellation, *s*/*p**i* = *s*/*q**j* would be another positive integer, different from s, which is greater than 1 and also has two distinct factorizations. But *s*/*p**i* is smaller than *s*, meaning *s* would not actually be the smallest such integer. Therefore every *p**i* must be distinct from every *q**j*.

Without loss of generality, take *p*1 < *q*1 (if this is not already the case, switch the *p* and *q* designations.) Consider

       t  =  (    q    1      −    p    1      )  (    q    2      ⋯    q    n      )  ,      {\displaystyle t=(q_{1}-p_{1})(q_{2}\cdots q_{n}),}  [t=(q_{1}-p_{1})(q_{2}\cdots q_{n}),](../_resources/812c746ef74c3d08dd92fc0d4ace134c.bin)

and note that 1 < *q*2 ≤ *t* < *s*. Therefore *t* must have a unique prime factorization. By rearrangement we see,

               t      =    q    1      (    q    2      ⋯    q    n      )  −    p    1      (    q    2      ⋯    q    n      )          =  s  −    p    1      (    q    2      ⋯    q    n      )          =    p    1      (  (    p    2      ⋯    p    m      )  −  (    q    2      ⋯    q    n      )  )  .              {\displaystyle {\begin{aligned}t&=q_{1}(q_{2}\cdots q_{n})-p_{1}(q_{2}\cdots q_{n})\\&=s-p_{1}(q_{2}\cdots q_{n})\\&=p_{1}((p_{2}\cdots p_{m})-(q_{2}\cdots q_{n})).\end{aligned}}}  [{\displaystyle {\begin{aligned}t&=q_{1}(q_{2}\cdots q_{n})-p_{1}(q_{2}\cdots q_{n})\\&=s-p_{1}(q_{2}\cdots q_{n})\\&=p_{1}((p_{2}\cdots p_{m})-(q_{2}\cdots q_{n})).\end{aligned}}}](../_resources/e3b74ec4ddf83ced01a48adbc08bbb03.bin)

Here *u* = ((*p*2 ... *p**m*) - (*q*2 ... *q**n*)) is positive, for if it were negative or zero then so would be its product with *p**1*, but that product equals *t* which is positive. So *u* is either 1 or factors into primes. In either case, *t* = *p*1*u* yields a prime factorization of *t*, which we know to be unique, so *p*1 appears in the prime factorization of *t*.

If (*q*1 - *p*1) equaled 1 then the prime factorization of *t* would be all *q'*s, which would preclude *p*1 from appearing. Thus (*q*1 - *p*1) is not 1, but is positive, so it factors into primes: (*q*1 - *p*1) = (*r*1 ... *r**h*). This yields a prime factorization of

       t  =  (    r    1      ⋯    r    h      )  (    q    2      ⋯    q    n      )  ,      {\displaystyle t=(r_{1}\cdots r_{h})(q_{2}\cdots q_{n}),}  [t=(r_{1}\cdots r_{h})(q_{2}\cdots q_{n}),](../_resources/e858788c741176b758fd5010952e16e0.bin)

which we know is unique. Now, *p*1 appears in the prime factorization of *t*, and it is not equal to any *q*, so it must be one of the *r'*s. That means *p*1 is a factor of (*q*1 - *p*1), so there exists a positive integer *k* such that *p*1*k* = (*q*1 - *p*1), and therefore

         p    1      (  k  +  1  )  =    q    1      .      {\displaystyle p_{1}(k+1)=q_{1}.}  [p_{1}(k+1)=q_{1}.](../_resources/59401b473e88f7a9b9cc040018372ee7.bin)

But that means *q*1 has a proper factorization, so it is not a prime number. This contradiction shows that *s* does not actually have two different prime factorizations. As a result, there is no smallest positive integer with multiple prime factorizations, hence all positive integers greater than 1 factor uniquely into primes.

## Generalizations[]

The first generalization of the theorem is found in Gauss's second monograph (1832) on [biquadratic reciprocity](https://en.wikipedia.org/wiki/Biquadratic_reciprocity). This paper introduced what is now called the [ring](https://en.wikipedia.org/wiki/Ring_theory) of [Gaussian integers](https://en.wikipedia.org/wiki/Gaussian_integer), the set of all [complex numbers](https://en.wikipedia.org/wiki/Complex_number)  *a* + *bi* where *a* and *b* are integers. It is now denoted by           Z    [  i  ]  .      {\displaystyle \mathbb {Z} [i].}  [\mathbb {Z} [i\].](../_resources/bdbbb8c00e7f14be7958721c46e2ed1f.bin) He showed that this ring has the four units ±1 and ±*i*, that the non-zero, non-unit numbers fall into two classes, primes and composites, and that (except for order), the composites have unique factorization as a product of primes.[[11]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-11)

Similarly, in 1844 while working on [cubic reciprocity](https://en.wikipedia.org/wiki/Cubic_reciprocity), [Eisenstein](https://en.wikipedia.org/wiki/Gotthold_Eisenstein) introduced the ring           Z    [  ω  ]      {\displaystyle \mathbb {Z} [\omega ]}  [\mathbb {Z} [\omega \]](../_resources/0c87ccbb96e2798add84cc30ecf08e78.bin), where         ω  =        −  1  +      −  3        2      ,      {\displaystyle \omega ={\frac {-1+{\sqrt {-3}}}{2}},}  [\omega ={\frac {-1+{\sqrt {-3}}}{2}},](../_resources/26fcbad4471025a04f3f50dad710c93c.bin)             ω    3      =  1      {\displaystyle \omega ^{3}=1}  [\omega ^{3}=1](../_resources/2656865a067617dfa870892c324974fe.bin) is a cube [root of unity](https://en.wikipedia.org/wiki/Root_of_unity). This is the ring of [Eisenstein integers](https://en.wikipedia.org/wiki/Eisenstein_integer), and he proved it has the six units         ±  1  ,  ±  ω  ,  ±    ω    2          {\displaystyle \pm 1,\pm \omega ,\pm \omega ^{2}}  [\pm 1,\pm \omega ,\pm \omega ^{2}](../_resources/e1d625e8c8855bb118f669076d6f177f.bin) and that it has unique factorization.

However, it was also discovered that unique factorization does not always hold. An example is given by           Z    [      −  5      ]      {\displaystyle \mathbb {Z} [{\sqrt {-5}}]}  [\mathbb {Z} [{\sqrt {-5}}\]](../_resources/836dd80acbd29962c6487bb7c638463d.bin). In this ring one has[[12]](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_note-12)

       6  =  2  ⋅  3  =  (  1  +      −  5      )  (  1  −      −  5      )  .      {\displaystyle 6=2\cdot 3=(1+{\sqrt {-5}})(1-{\sqrt {-5}}).}  [{\displaystyle 6=2\cdot 3=(1+{\sqrt {-5}})(1-{\sqrt {-5}}).}](../_resources/4d83980f43690da7840ca48f9e410dd0.bin)

Examples like this caused the notion of "prime" to be modified. In           Z    [      −  5      ]      {\displaystyle \mathbb {Z} [{\sqrt {-5}}]}  [\mathbb {Z} [{\sqrt {-5}}\]](../_resources/836dd80acbd29962c6487bb7c638463d.bin) it can be proven that if any of the factors above can be represented as a product, e.g., 2 = *ab*, then one of *a* or *b* must be a unit. This is the traditional definition of "prime". It can also be proven that none of these factors obeys Euclid's lemma; e.g., 2 divides neither (1 + √−5) nor (1 − √−5) even though it divides their product 6. In [algebraic number theory](https://en.wikipedia.org/wiki/Algebraic_number_theory) 2 is called **irreducible** in           Z    [      −  5      ]      {\displaystyle \mathbb {Z} [{\sqrt {-5}}]}  [\mathbb {Z} [{\sqrt {-5}}\]](../_resources/836dd80acbd29962c6487bb7c638463d.bin) (only divisible by itself or a unit) but not **prime** in           Z    [      −  5      ]      {\displaystyle \mathbb {Z} [{\sqrt {-5}}]}  [\mathbb {Z} [{\sqrt {-5}}\]](../_resources/836dd80acbd29962c6487bb7c638463d.bin) (if it divides a product it must divide one of the factors). The mention of           Z    [      −  5      ]      {\displaystyle \mathbb {Z} [{\sqrt {-5}}]}  [\mathbb {Z} [{\sqrt {-5}}\]](../_resources/836dd80acbd29962c6487bb7c638463d.bin) is required because 2 is prime and irreducible in           Z    .      {\displaystyle \mathbb {Z} .}   Using these definitions it can be proven that in any ring a prime must be irreducible. Euclid's classical lemma can be rephrased as "in the ring of integers           Z        {\displaystyle \mathbb {Z} }   every irreducible is prime". This is also true in           Z    [  i  ]      {\displaystyle \mathbb {Z} [i]}   and           Z    [  ω  ]  ,      {\displaystyle \mathbb {Z} [\omega ],}   but not in           Z    [      −  5      ]  .      {\displaystyle \mathbb {Z} [{\sqrt {-5}}].}

The rings in which factorization into irreducibles is essentially unique are called [unique factorization domains](https://en.wikipedia.org/wiki/Unique_factorization_domain). Important examples are [polynomial rings](https://en.wikipedia.org/wiki/Polynomial_ring) over the integers or over a [field](https://en.wikipedia.org/wiki/Field_(mathematics)), [Euclidean domains](https://en.wikipedia.org/wiki/Euclidean_domain) and [principal ideal domains](https://en.wikipedia.org/wiki/Principal_ideal_domain).

In 1843 [Kummer](https://en.wikipedia.org/wiki/Ernst_Kummer) introduced the concept of [ideal number](https://en.wikipedia.org/wiki/Ideal_number), which was developed further by [Dedekind](https://en.wikipedia.org/wiki/Richard_Dedekind) (1876) into the modern theory of [ideals](https://en.wikipedia.org/wiki/Ideal_(ring_theory)), special subsets of rings. Multiplication is defined for ideals, and the rings in which they have unique factorization are called [Dedekind domains](https://en.wikipedia.org/wiki/Dedekind_domain).

There is a version of [unique factorization for ordinals](https://en.wikipedia.org/wiki/Ordinal_arithmetic), though it requires some additional conditions to ensure uniqueness.

## See also[]

## Notes[]

1. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-Gauss1801.loc=16_1-0)  [***b***](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-Gauss1801.loc=16_1-1)  [Gauss & Clarke (1986](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFGaussClarke1986), Art. 16)

2. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-2)**  [Gauss & Clarke (1986](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFGaussClarke1986), Art. 131)

3. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-3)** Using the [empty product rule](https://en.wikipedia.org/wiki/Empty_product) one need not exclude the number 1, and the theorem can be stated as: every positive integer has unique prime factorization.

4. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-4)**  [Long (1972](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFLong1972), p. 44)

5. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-5)**  [Pettofrezzo & Byrkit (1970](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFPettofrezzoByrkit1970), p. 53)

6. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-6)**  [Hardy & Wright (2008](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFHardyWright2008), Thm 2)

7. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-7)**  [Weil (2007](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFWeil2007), p. 5): "Even in Euclid, we fail to find a general statement about the uniqueness of the factorization of an integer into primes; surely he may have been aware of it, but all he has is a statement (Eucl.IX.I4) about the l.c.m. of any number of given primes."

8. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-8)**  [Long (1972](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFLong1972), p. 45)

9. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-9)**  [Pettofrezzo & Byrkit (1970](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFPettofrezzoByrkit1970), p. 55)

10. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-10)**  [Hardy & Wright (2008](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFHardyWright2008), § 1.2)

11. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-11)**  [Gauss, BQ, §§ 31–34](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFGauss1832)

12. **[Jump up ^](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#cite_ref-12)**  [Hardy & Wright (2008](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#CITEREFHardyWright2008), § 14.6)

## References[]

The *[Disquisitiones Arithmeticae](https://en.wikipedia.org/wiki/Disquisitiones_Arithmeticae)* has been translated from Latin into English and German. The German edition includes all of his papers on number theory: all the proofs of quadratic reciprocity, the determination of the sign of the Gauss sum, the investigations into biquadratic reciprocity, and unpublished notes.

- Gauss, Carl Friedrich; Clarke, Arthur A. (translator into English) (1986), [*Disquisitiones Arithemeticae (Second, corrected edition)*](https://www.springer.com/mathematics/algebra/book/978-0-387-96254-2), New York: [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-387-96254-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-96254-2)
- Gauss, Carl Friedrich; Maser, H. (translator into German) (1965), *Untersuchungen über hohere Arithmetik (Disquisitiones Arithemeticae & other papers on number theory) (Second edition)*, New York: Chelsea, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-8284-0191-8](https://en.wikipedia.org/wiki/Special:BookSources/0-8284-0191-8)

The two monographs Gauss published on biquadratic reciprocity have consecutively numbered sections: the first contains §§ 1–23 and the second §§ 24–76. Footnotes referencing these are of the form "Gauss, BQ, § *n*". Footnotes referencing the *Disquisitiones Arithmeticae* are of the form "Gauss, DA, Art. *n*".

- Gauss, Carl Friedrich (1828), *Theoria residuorum biquadraticorum, Commentatio prima*, Göttingen: Comment. Soc. regiae sci, Göttingen 6
- Gauss, Carl Friedrich (1832), *Theoria residuorum biquadraticorum, Commentatio secunda*, Göttingen: Comment. Soc. regiae sci, Göttingen 7

These are in Gauss's *Werke*, Vol II, pp. 65–92 and 93–148; German translations are pp. 511–533 and 534–586 of the German edition of the *Disquisitiones*.

- Baker, Alan (1984), *A Concise Introduction to the Theory of Numbers*, Cambridge, UK: Cambridge University Press, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-521-28654-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-28654-1)
- [Euclid](https://en.wikipedia.org/wiki/Euclid) (1956), [*The thirteen books of the Elements*](http://store.doverpublications.com/0486600890.html), 2 (Books III-IX), Translated by [Thomas Little Heath](https://en.wikipedia.org/wiki/Thomas_Little_Heath) (Second Edition Unabridged ed.), New York: [Dover](https://en.wikipedia.org/wiki/Dover), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-486-60089-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-60089-5)
- [Hardy, G. H.](https://en.wikipedia.org/wiki/G._H._Hardy); [Wright, E. M.](https://en.wikipedia.org/wiki/E._M._Wright) (2008) [1938]. *An Introduction to the Theory of Numbers*. Revised by [D. R. Heath-Brown](https://en.wikipedia.org/wiki/Roger_Heath-Brown) and [J. H. Silverman](https://en.wikipedia.org/wiki/Joseph_H._Silverman). Foreword by [Andrew Wiles](https://en.wikipedia.org/wiki/Andrew_Wiles). (6th ed.). Oxford: [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-19-921986-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-921986-5). [MR](https://en.wikipedia.org/wiki/Mathematical_Reviews) [2445243](https://www.ams.org/mathscinet-getitem?mr=2445243). [Zbl](https://en.wikipedia.org/wiki/Zentralblatt_MATH) [1159.11001](https://zbmath.org/?format=complete&q=an:1159.11001).
- A. Kornilowicz; P. Rudnicki (2004), "Fundamental theorem of arithmetic", *[Formalized Mathematics](https://en.wikipedia.org/w/index.php?title=Formalized_Mathematics&action=edit&redlink=1)*, **12** (2): 179–185
- Long, Calvin T. (1972), *Elementary Introduction to Number Theory* (2nd ed.), Lexington: [D. C. Heath and Company](https://en.wikipedia.org/wiki/D._C._Heath_and_Company), [LCCN](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number) [77-171950](https://lccn.loc.gov/77-171950).
- Pettofrezzo, Anthony J.; Byrkit, Donald R. (1970), *Elements of Number Theory*, Englewood Cliffs: [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall), [LCCN](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number) [77-81766](https://lccn.loc.gov/77-81766).
- Riesel, Hans (1994), *Prime Numbers and Computer Methods for Factorization (second edition)*, Boston: Birkhäuser, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-8176-3743-5](https://en.wikipedia.org/wiki/Special:BookSources/0-8176-3743-5)
- Weil, André (2007) [1984]. *[Number Theory: An Approach through History from Hammurapi to Legendre](https://en.wikipedia.org/wiki/Number_Theory:_An_Approach_through_History_from_Hammurapi_to_Legendre)*. Modern Birkhäuser Classics. Boston, MA: Birkhäuser. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-817-64565-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-817-64565-6).
- [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein)  ["Abnormal number"](http://mathworld.wolfram.com/AbnormalNumber.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld)*.
- [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein)  ["Fundamental Theorem of Arithmetic"](http://mathworld.wolfram.com/FundamentalTheoremofArithmetic.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld)*.

## External links[]

| [[show](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic#)]<br>Divisibility-based sets of integers |
| --- |