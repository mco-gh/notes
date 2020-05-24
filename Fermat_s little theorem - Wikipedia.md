Fermat's little theorem - Wikipedia

# Fermat's little theorem

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#mw-head)[Jump to search](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#p-search)

For other theorems named after Pierre de Fermat, see [Fermat's theorem](https://en.wikipedia.org/wiki/Fermat%27s_theorem).

**Fermat's little theorem** states that if *p* is a [prime number](https://en.wikipedia.org/wiki/Prime_number), then for any [integer](https://en.wikipedia.org/wiki/Integer)  *a*, the number *a**p* − *a* is an integer multiple of *p*. In the notation of [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic), this is expressed as

   {\displaystyle a^{p}\equiv a{\pmod {p}}.}  ![76fcf163a7523f30b84bf09165eba0092b0ee32e](../_resources/7ebee8c7689b364a422b6a98f0c2783e.png)

For example, if *a* = 2 and *p* = 7, then 27 = 128, and 128 − 2 = 126 = 7 × 18 is an integer multiple of 7.

If *a* is not divisible by *p*, Fermat's little theorem is equivalent to the statement that *a**p* − 1 − 1 is an integer multiple of *p*, or in symbols:[[1]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-1)[[2]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-2)

   {\displaystyle a^{p-1}\equiv 1{\pmod {p}}.}  ![58a9e1a77254c598a3bbd20ee75962c540381c54](../_resources/930ffbca674dfcb85c0dfa5f64269173.png)

For example, if *a* = 2 and *p* = 7, then 26 = 64, and 64 − 1 = 63 = 7 × 9 is thus a multiple of 7.

Fermat's little theorem is the basis for the [Fermat primality test](https://en.wikipedia.org/wiki/Fermat_primality_test) and is one of the fundamental results of [elementary number theory](https://en.wikipedia.org/wiki/Elementary_number_theory). The theorem is named after [Pierre de Fermat](https://en.wikipedia.org/wiki/Pierre_de_Fermat), who stated it in 1640. It is called the "little theorem" to distinguish it from [Fermat's last theorem](https://en.wikipedia.org/wiki/Fermat%27s_last_theorem).[[3]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-Burton-3)

## Contents

[hide]

- [1  History](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#History)
    - [1.1  Further history](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Further_history)
- [2  Proofs](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Proofs)
- [3  Generalizations](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Generalizations)
- [4  Converse](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Converse)
- [5  Pseudoprimes](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Pseudoprimes)
- [6  Miller–Rabin primality test](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Miller%E2%80%93Rabin_primality_test)
- [7  See also](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#See_also)
- [8  Notes](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Notes)
- [9  References](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#References)
- [10  Further reading](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Further_reading)
- [11  External links](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#External_links)

## History[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=1)]

[![Pierre_de_Fermat.jpg](../_resources/831002545d1e8dba0218d12eeff3a6ce.jpg)](https://en.wikipedia.org/wiki/File:Pierre_de_Fermat.jpg)

[(L)](https://en.wikipedia.org/wiki/File:Pierre_de_Fermat.jpg)
Pierre de Fermat

[Pierre de Fermat](https://en.wikipedia.org/wiki/Pierre_de_Fermat) first stated the theorem in a letter dated October 18, 1640, to his friend and confidant [Frénicle de Bessy](https://en.wikipedia.org/wiki/Fr%C3%A9nicle_de_Bessy). His formulation is equivalent to the following:[[3]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-Burton-3)

> If *> p*>  is a prime and *> a*>  is any integer not divisible by *> p*> , then *> a*>   *> p*>  − 1>  − 1>  is divisible by *> p*> .

In fact, the original statement was

*> Tout nombre premier mesure infailliblement une des puissances – 1 de quelque progression que ce soit, et l'exposant de la dite puissance est sous-multiple du nombre premier donné – 1 ; et, après qu'on a trouvé la première puissance qui satisfait à la question, toutes celles dont les exposants sont multiples de l'exposant de la première satisfont tout de même à la question.*

This may be translated, with explanations and formulas added in brackets for easier understanding, as:

> Every prime number [*> p*> ] divides necessarily one of the powers minus one of any [geometric] > [> progression](https://en.wikipedia.org/wiki/Geometric_progression)>  [*> a*> , *> a*> 2> , *> a*> 3> , ... > ] [that is, there exists *> t*>  such that *> p*>  divides *> a> t*>  – 1> ], and the exponent of this power [*> t*> ] divides the given prime minus one [divides *> p*>  – 1> ]. After one has found the first power [*> t*> ] that satisfies the question, all those whose exponents are multiples of the exponent of the first one satisfy similarly the question [that is, all multiples of the first *> t*>  have the same property].

Fermat did not consider the case where *a* is a multiple of *p* nor prove his assertion, only stating:[[4]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-4)

*> Et cette proposition est généralement vraie en toutes progressions et en tous nombres premiers; de quoi je vous envoierois la démonstration, si je n'appréhendois d'être trop long.*

> (And this proposition is generally true for all series [*> sic*> ] and for all prime numbers; I would send you a demonstration of it, if I did not fear going on for too long.)> [> [5]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-5)

[Euler](https://en.wikipedia.org/wiki/Euler) provided the first published proof in 1736, in a paper titled "Theorematum Quorundam ad Numeros Primos Spectantium Demonstratio" in the *Proceedings* of the St. Petersburg Academy,[[6]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-6) but [Leibniz](https://en.wikipedia.org/wiki/Gottfried_Leibniz) had given virtually the same proof in an unpublished manuscript from sometime before 1683.[[3]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-Burton-3)

The term "Fermat's little theorem" was probably first used in print in 1913 in *Zahlentheorie* by [Kurt Hensel](https://en.wikipedia.org/wiki/Kurt_Hensel):

*> Für jede endliche Gruppe besteht nun ein Fundamentalsatz, welcher der kleine Fermatsche Satz genannt zu werden pflegt, weil ein ganz spezieller Teil desselben zuerst von Fermat bewiesen worden ist.*

> (There is a fundamental theorem holding in every finite group, usually called Fermat's little theorem because Fermat was the first to have proved a very special part of it.)

An early use in English occurs in [A.A. Albert](https://en.wikipedia.org/wiki/Abraham_Adrian_Albert)'s *Modern Higher Algebra* (1937), which refers to "the so-called 'little' Fermat theorem" on page 206.[[7]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-7)

### Further history[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=2)]

Main article: [Chinese hypothesis](https://en.wikipedia.org/wiki/Chinese_hypothesis)

Some mathematicians independently made the related hypothesis (sometimes incorrectly called the Chinese Hypothesis) that 2*p* ≡ 2 (mod *p*) if and only if *p* is prime. Indeed, the "if" part is true, and it is a special case of Fermat's little theorem. However, the "only if" part is false: For example, 2341 ≡ 2 (mod 341), but 341 = 11 × 31 is a [pseudoprime](https://en.wikipedia.org/wiki/Pseudoprime). See [below](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#Pseudoprimes).

## Proofs[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=3)]

Main article: [Proofs of Fermat's little theorem](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem)

Several proofs of Fermat's little theorem are known. It is frequently proved as a corollary of [Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem).

## Generalizations[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=4)]

[Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem) is a generalization of Fermat's little theorem: for any [modulus](https://en.wikipedia.org/wiki/Modular_arithmetic)      {\displaystyle n}  ![f067864064667dd5f8b2508b9cbf983d89788629](../_resources/6dcd69860d2a056a804d0cf4a7021515.png) and any integer *a*  [coprime](https://en.wikipedia.org/wiki/Coprime) to *n*, one has

   {\displaystyle a^{\varphi (n)}\equiv 1{\pmod {n}},}  ![7df8b551ba55ab6a7bd8fcf3a0572d1234c1a2a5](../_resources/aec25c75a6da0e7b81c7375bf6d114bb.png)

where     {\displaystyle \varphi (n)}  ![6b346e33e793d05d8f191992b649dc735629c674](../_resources/29ea2e0bb87874386ff9af466e0b437b.png) denotes [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function) (which counts the integers from 1 to *n* that are coprime to *n*). Fermat's little theorem is indeed a special case, because if     {\displaystyle n}  ![a601995d55609f2d9f5e233e36fbe9ea26011b3b](../_resources/6dcd69860d2a056a804d0cf4a7021515.png) is a prime number, then     {\displaystyle \varphi (n)=n-1}  ![2346a999a996e4a6f15819a49e41fc4ea3d6d39d](../_resources/6d3581fb78d31aabc652ad263600c5f9.png).

A corollary of Euler's theorem is: for every positive integer *n*, if the integer *a* is [coprime](https://en.wikipedia.org/wiki/Coprime_integers) with *n* then

   {\displaystyle x\equiv y{\pmod {\varphi (n)}}\quad {\text{implies}}\quad a^{x}\equiv a^{y}{\pmod {n}},}  ![7d013fb25ec7383e3f5db74a5ff77a0d6b902453](../_resources/49d246d38c342d387959bf4667c642a2.png)

for any integers *x* and *y*. This follows from Euler's theorem, since, if     {\displaystyle x\equiv y{\pmod {\varphi (n)}}}  ![545913dae25382fe807e0446a9bef0f4476fe10d](../_resources/83c8f81a5b55130caf40f5fc0f9420f9.png), then     {\displaystyle x=y+k\varphi (n)}  ![0fbee384b6cf1df49440becdfdfebb254cc9a261](../_resources/e48747219085eac16a27e8d5ba2ebd8b.png) for some integer *k*, and one has

   {\displaystyle a^{x}=a^{y+\varphi (n)k}=a^{y}(a^{\varphi (n)})^{k}\equiv a^{y}1^{k}\equiv a^{y}{\pmod {n}}.}  ![18d87d29c63bea9e9ec6d53486f4879069f08b7b](../_resources/d9892f45207c4143d2ad283fae50b8f9.png)

If *n* is prime, this is also a corollary of Fermat's little theorem. This is widely used in [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic), because this allows reducing [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation) with large exponents to exponents smaller than *n*.

If *n* is not prime, this is used in [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography), typically in the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_cryptosystem) in the following way:[[8]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-8) if

   {\displaystyle y=x^{e}{\pmod {n}},}  ![47589175c109aaffc498e3e4df641da930732428](../_resources/7071b20821f9289185818534dbd4316c.png)

retrieving *x* from the values of *e* and *n* is easy if one knows     {\displaystyle \varphi (n).}  ![c6d006519cb779bc5bce41ef8578a705c76ad4b8](../_resources/b3e4d21eaa59fb869b14a297b9354350.png) In fact, the [extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) allows computing the [modular inverse](https://en.wikipedia.org/wiki/Modular_inverse) of *e* modulo     {\displaystyle \varphi (n),}  ![32px-Nuvola_apps_edu_mathematics_blue-p.svg.png](../_resources/49ddcac483fc22211a79eb91ee6a4e16.png) that is the integer *f* such     {\displaystyle ef\equiv 1{\pmod {\varphi (n)}}.}  ![667887d7bc0e24f75989f0b13aa57cbda6989d81](../_resources/5b8f01688fbce58efa36d0cdf2e4aa38.png) It follows that

   {\displaystyle x\equiv x^{ef}\equiv (x^{e})^{f}\equiv y^{f}{\pmod {n}}.}  ![ec4f77950832c1693396db2bd01780ebfeb1996c](../_resources/c76e6ca0c2ee63e13edd0c0893c73ef6.png)

On the other hand, if *n* = *pq* is the product of two distinct prime numbers, then     {\displaystyle \varphi (n)=(p-1)(q-1).}  ![f0d8f5bbbee4ff3eb2425f7ba0dbffec0d7bfebd](../_resources/0ccaf0bf79030559c060ffa73512e13c.png) In this case, finding *f* from *n* and *e* needs knowing     {\displaystyle \varphi (n)}   (this is not proved, but no algorithm is known for computing *f* without knowing     {\displaystyle \varphi (n)}  ). If one knows *n* and     {\displaystyle \varphi (n),}   the factors *p* and *q* are easy to deduce, as one knows their product *n* and their sum     {\displaystyle n-\varphi (n)+1.}  ![5445bf33cc5b683e9ecc0e0a78a1bef69da86a2e](../_resources/3cdaf8b2e7f3f7b4d5ff06c52a80342b.png) The basic idea of RSA cryptosystem is thus: if a message *x* is encrypted as     {\displaystyle y=x^{e}{\pmod {n}},}  ![47589175c109aaffc498e3e4df641da930732428](../_resources/7071b20821f9289185818534dbd4316c.png) using public values of *n* and *e*, then, with the current knowledge, it cannot be decrypted without finding the (secret) factors *p* and *q* of *n*.

Fermat's little theorem is also related to the [Carmichael function](https://en.wikipedia.org/wiki/Carmichael_function) and [Carmichael's theorem](https://en.wikipedia.org/wiki/Carmichael%27s_theorem), as well as to [Lagrange's theorem in group theory](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)).

## Converse[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=5)]

The [converse](https://en.wikipedia.org/wiki/Logical_converse) of Fermat's little theorem is not generally true, as it fails for [Carmichael numbers](https://en.wikipedia.org/wiki/Carmichael_number). However, a slightly stronger form of the theorem is true, and it is known as Lehmer's theorem. The theorem is as follows:

If there exists an integer *a* such that

   {\displaystyle a^{p-1}\equiv 1{\pmod {p}}}  ![5b71e80b05f598bfd9ac9618c87a94323e41e688](../_resources/99de001bcfd7f5b2eb601842a18f4e92.png)

and for all primes *q* dividing *p* − 1 one has

   {\displaystyle a^{(p-1)/q}\not \equiv 1{\pmod {p}},}  ![670fe2e2d6cd2672eecdfda1d02392aef86b86f9](../_resources/7a8ef137de364a6668306c9d8655ade4.png)

then *p* is prime.

This theorem forms the basis for the [Lucas–Lehmer test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_test), an important [primality test](https://en.wikipedia.org/wiki/Primality_test).

## Pseudoprimes[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=6)]

Main article: [Pseudoprime](https://en.wikipedia.org/wiki/Pseudoprime)

If *a* and *p* are coprime numbers such that *a**p*−1 − 1 is divisible by *p*, then *p* need not be prime. If it is not, then *p* is called a *(Fermat) pseudoprime* to base *a*. The first pseudoprime to base 2 was found in 1820 by [Pierre Frédéric Sarrus](https://en.wikipedia.org/wiki/Pierre_Fr%C3%A9d%C3%A9ric_Sarrus): 341 = 11 × 31.[[9]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-9)[[10]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-10)

A number *p* that is a Fermat pseudoprime to base *a* for every number *a* coprime to *p* is called a [Carmichael number](https://en.wikipedia.org/wiki/Carmichael_number) (e.g. 561). Alternately, any number *p* satisfying the equality

   {\displaystyle \gcd \left(p,\sum _{a=1}^{p-1}a^{p-1}ight)=1}  ![9725156b187128ff35b4897885cb6bee6266c77b](../_resources/1f4f24ed02b683aea8ea0c306fc212a7.png)

is either a prime or a Carmichael number.

## Miller–Rabin primality test[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=7)]

The [Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) uses the following extension of Fermat's little theorem:[[11]](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_note-11)

> If *> p*>  is an odd prime number, and *> p*>  – 1 = 2*> s*>   *> d*> , with *> d*>  odd, then for every *> a*>  prime to *> p*> , either *> a**> d*>  ≡ 1 mod *> p*> , or there exists *> t*>  such that > 0 ≤ *> t*>  < s>  and *> a*> 2*> t**> d*>  ≡ −1 mod *> p*

This result may be deduced from Fermat's little theorem by the fact that, if *p* is an odd prime, then the integers modulo *p* form a [finite field](https://en.wikipedia.org/wiki/Finite_field), in which 1 has exactly two square roots, 1 and −1.

The Miller–Rabin test uses this property in the following way: given *p* = 2*s*  *d* + 1, with *d* odd, an odd integer for which primality has to be tested, choose randomly *a* such that 1 < *a* < *p*; then compute *b* = *a**d* mod *p*; if *b* is not 1 nor −1, then square it repeatedly modulo *p* until you get 1, −1, or have squared *s* times. If *b* ≠ 1 and −1 has not been obtained, then *p* is not prime. Otherwise, *p* may be prime or not. If *p* is not prime, the probability that this is proved by the test is higher than 1/4. Therefore, after *k* non-conclusive random tests, the probability that *p* is not prime is lower than (3/4)*k*, and may thus be made as low as desired, by increasing *k*.

In summary, the test either proves that a number is not prime, or asserts that it is prime with a probability of error that may be chosen as low as desired. The test is very simple to implement and computationally more efficient than all known deterministic tests. Therefore, it is generally used before starting a proof of primality.

## See also[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=8)]

- [Fermat quotient](https://en.wikipedia.org/wiki/Fermat_quotient)
- [Frobenius endomorphism](https://en.wikipedia.org/wiki/Frobenius_endomorphism)
- [*p*-derivation](https://en.wikipedia.org/wiki/P-derivation)
- [Fractions with prime denominators](https://en.wikipedia.org/wiki/Recurring_decimal#Fractions_with_prime_denominators): numbers with behavior relating to Fermat's little theorem
- [RSA](https://en.wikipedia.org/wiki/RSA_(algorithm))
- [Table of congruences](https://en.wikipedia.org/wiki/Table_of_congruences)
- [Modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

## Notes[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=9)]

1. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-1)**  [Long 1972](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#CITEREFLong1972), pp. 87–88.

2. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-2)**  [Pettofrezzo & Byrkit 1970](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#CITEREFPettofrezzoByrkit1970), pp. 110–111.

3. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-Burton_3-0)  [***b***](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-Burton_3-1)  [***c***](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-Burton_3-2)  [Burton 2011](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#CITEREFBurton2011), p. 514.

4. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-4)**  Fermat, Pierre (1894), Tannery, P.; Henry, C. (eds.), [*Oeuvres de Fermat. Tome 2: Correspondance*](https://archive.org/stream/oeuvresdefermat02ferm#page/206/mode/2up), Paris: Gauthier-Villars, pp. 206–212 (in French)

5. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-5)**  [Mahoney 1994](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#CITEREFMahoney1994), p. 295 for the English translation

6. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-6)**  [Ore 1988](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#CITEREFOre1988), p. 273

7. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-7)**  [Albert 2015](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#CITEREFAlbert2015), p. 206

8. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-8)**  Trappe, Wade; Washington, Lawrence C. (2002), *Introduction to Cryptography with Coding Theory*, Prentice-Hall, p. 78, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-13-061814-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-061814-6)

9. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-9)**  [Sloane, N. J. A.](https://en.wikipedia.org/wiki/Neil_Sloane) (ed.). ["Sequence A128311 (Remainder upon division of 2*n*−1−1 by *n*.)"](https://oeis.org/A128311). *The [On-Line Encyclopedia of Integer Sequences](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences)*. OEIS Foundation.

10. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-10)**  [Sarrus, Frédéric](https://en.wikipedia.org/wiki/Pierre_Fr%C3%A9d%C3%A9ric_Sarrus) (1819–1820). ["Démonstration de la fausseté du théorème énoncé á la page 320 du IXe volume de ce recueil"](http://www.numdam.org/item?id=AMPA_1819-1820__10__184_0) [Demonstration of the falsity of the theorem stated on page 320 of the 9th volume of this collection]. *Annales de Mathématiques Pures et Appliquées* (in French). **10**: 184–187.

11. **[^](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem#cite_ref-11)**  Rempe-Gillen, Lasse; Waldecker, Rebecca (2013-12-11). [*Primality Testing for Beginners*](https://books.google.com/?id=nQVZAgAAQBAJ&pg=PA144&lpg=PA144&dq=The+Miller%E2%80%93Rabin+primality+test+uses+the+following+extension+of+Fermat%27s+little+theorem#v=onepage&q&f=false). American Mathematical Soc. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [9780821898833](https://en.wikipedia.org/wiki/Special:BookSources/9780821898833).

## References[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=10)]

- [Albert, A. Adrian](https://en.wikipedia.org/wiki/Abraham_Adrian_Albert) (2015) [1938], [*Modern higher algebra*](https://books.google.com/books?id=iVwZCgAAQBAJ&pg=PA206), [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press), [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-1-107-54462-8](https://en.wikipedia.org/wiki/Special:BookSources/978-1-107-54462-8)
- Burton, David M. (2011), *The History of Mathematics / An Introduction* (7th ed.), McGraw-Hill, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-07-338315-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-07-338315-6)
- Long, Calvin T. (1972), *Elementary Introduction to Number Theory* (2nd ed.), Lexington: [D. C. Heath and Company](https://en.wikipedia.org/wiki/D._C._Heath_and_Company), [LCCN](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number) [77171950](https://lccn.loc.gov/77171950)
- Mahoney, Michael Sean (1994), *The Mathematical Career of Pierre de Fermat, 1601–1665* (2nd ed.), Princeton University Press, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-691-03666-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-691-03666-3)
- Ore, Oystein (1988) [1948], [*Number Theory and Its History*](https://archive.org/details/numbertheoryitsh0000orey), Dover, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-486-65620-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-65620-5)
- Pettofrezzo, Anthony J.; Byrkit, Donald R. (1970), *Elements of Number Theory*, Englewood Cliffs: [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall), [LCCN](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number) [71081766](https://lccn.loc.gov/71081766)

## Further reading[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=11)]

- [Paulo Ribenboim](https://en.wikipedia.org/wiki/Paulo_Ribenboim) (1995). *The New Book of Prime Number Records* (3rd ed.). New York: Springer-Verlag. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-387-94457-5](https://en.wikipedia.org/wiki/Special:BookSources/0-387-94457-5). pp. 22–25, 49.

## External links[[edit](https://en.wikipedia.org/w/index.php?title=Fermat%27s_little_theorem&action=edit&section=12)]

- [Fermat's theorem](https://www.britannica.com/EBchecked/topic/204696) at the *[Encyclopædia Britannica](https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica)*
- [János Bolyai and the pseudoprimes](https://web.archive.org/web/20041022022031/http://bolyai.port5.com/kisfermat.htm) (in Hungarian)
- [Fermat's Little Theorem](http://www.cut-the-knot.org/blue/Fermat.shtml) at [cut-the-knot](https://en.wikipedia.org/wiki/Cut-the-knot)
- [Euler Function and Theorem](http://www.cut-the-knot.org/blue/Euler.shtml) at cut-the-knot
- [Fermat's Little Theorem and Sophie's Proof](http://fermatslasttheorem.blogspot.com/2005/08/fermats-little-theorem.html)
- [Hazewinkel, Michiel](https://en.wikipedia.org/wiki/Michiel_Hazewinkel), ed. (2001) [1994], ["Fermat's little theorem"](https://www.encyclopediaofmath.org/index.php?title=p/f038400), *[Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics)*, Springer Science+Business Media B.V. / Kluwer Academic Publishers, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-1-55608-010-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-55608-010-4)
- [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein)  ["Fermat's Little Theorem"](http://mathworld.wolfram.com/FermatsLittleTheorem.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld)*.
- [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein)  ["Fermat's Little Theorem Converse"](http://mathworld.wolfram.com/FermatsLittleTheoremConverse.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld)*.
- [(L)](https://en.wikipedia.org/wiki/File:Nuvola_apps_edu_mathematics_blue-p.svg)[Mathematics portal](https://en.wikipedia.org/wiki/Portal:Mathematics)

[Categories](https://en.wikipedia.org/wiki/Help:Category):

- [Modular arithmetic](https://en.wikipedia.org/wiki/Category:Modular_arithmetic)
- [Theorems about prime numbers](https://en.wikipedia.org/wiki/Category:Theorems_about_prime_numbers)