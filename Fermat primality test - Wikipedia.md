Fermat primality test - Wikipedia

# Fermat primality test

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/Fermat_primality_test#mw-head)[Jump to search](https://en.wikipedia.org/wiki/Fermat_primality_test#p-search)

The **Fermat primality test** is a [probabilistic](https://en.wikipedia.org/wiki/Randomized_algorithm) test to determine whether a number is a [probable prime](https://en.wikipedia.org/wiki/Probable_prime).

## Contents

[hide]

- [1  Concept](https://en.wikipedia.org/wiki/Fermat_primality_test#Concept)
- [2  Example](https://en.wikipedia.org/wiki/Fermat_primality_test#Example)
- [3  Algorithm](https://en.wikipedia.org/wiki/Fermat_primality_test#Algorithm)
    - [3.1  Complexity](https://en.wikipedia.org/wiki/Fermat_primality_test#Complexity)
- [4  Flaw](https://en.wikipedia.org/wiki/Fermat_primality_test#Flaw)
- [5  Applications](https://en.wikipedia.org/wiki/Fermat_primality_test#Applications)
- [6  References](https://en.wikipedia.org/wiki/Fermat_primality_test#References)

## Concept[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=1)]

[Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem) states that if *p* is prime and *a* is not divisible by *p*, then

   {\displaystyle a^{p-1}\equiv 1{\pmod {p}}.}  ![58a9e1a77254c598a3bbd20ee75962c540381c54](../_resources/930ffbca674dfcb85c0dfa5f64269173.png)

If one wants to test whether *p* is prime, then we can pick random integers *a* not divisible by *p* and see whether the equality holds. If the equality does not hold for a value of *a*, then *p* is composite. This congruence is unlikely to hold for a random *a* if *p* is composite.[[1]](https://en.wikipedia.org/wiki/Fermat_primality_test#cite_note-PSW-1)Therefore, if the equality does hold for one or more values of *a*, then we say that *p* is [probably prime](https://en.wikipedia.org/wiki/Probable_prime).

However, note that for     {\displaystyle a\equiv 1{\pmod {p}}}  ![97ff3386a1b15a17a93ad185621384feb2de8266](../_resources/a1a363f492dfdb5bcccbc7234ef6a742.png), the above congruence holds trivially. It also holds trivially if *p* is odd and     {\displaystyle a\equiv -1{\pmod {p}}}  ![21d412c0593550f2c3b1b80b369cacfd21039bf8](../_resources/317955d7cb1f100b3adc7019279edc12.png). For this reason, one usually chooses a number *a* in the interval     {\displaystyle 1<a<p-1}  ![c10f48a5c1ef9c9a982fe7ae0fe123b5b9bfb39e](../_resources/bf7b869ea7b5249f2f824631301f74fa.png).

Any *a* such that

   {\displaystyle a^{n-1}\equiv 1{\pmod {n}}}  ![3bfc8625369c7558deadd61823842db06983423d](../_resources/d95291419025768ed8736cd86f82067c.png)

when *n* is composite *a* is known as a *Fermat liar*. In this case *n* is called [Fermat pseudoprime](https://en.wikipedia.org/wiki/Fermat_pseudoprime) to base *a*.

If we do pick an *a* such that

   {\displaystyle a^{n-1}\not \equiv 1{\pmod {n}}}  ![815e1cde47b2d07520bc906454239520561c96b5](../_resources/22bbe37d1fb581cf2c840751c4407f13.png)

then *a* is known as a *Fermat witness* for the compositeness of *n*.

## Example[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=2)]

Suppose we wish to determine whether *n* = 221 is prime. Randomly pick 1 < *a* < 221, say *a* = 38. We check the above equality and find that it holds:

   {\displaystyle a^{n-1}=38^{220}\equiv 1{\pmod {221}}.}  ![0a72724c2e4c77b21ea868ea87e6a3a0f80087d2](../_resources/19e2894604a286821e6f74efb64c1c99.png)

Either 221 is prime, or 38 is a Fermat liar, so we take another *a*, say 24:

   {\displaystyle a^{n-1}=24^{220}\equiv 81\not \equiv 1{\pmod {221}}.}  ![9350d89b58a0eb2c371bc5a082839857aad2cb5e](../_resources/bfdce0421d100b4c939e24ebe26bad8e.png)

So 221 is composite and 38 was indeed a Fermat liar. Furthermore, 24 is a Fermat witness for the compositeness of 221.

## Algorithm[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=3)]

The algorithm can be written as follows:

**Inputs**: *n*: a value to test for primality, *n*>3; *k*: a parameter that determines the number of times to test for primality

**Output**: *composite* if *n* is composite, otherwise *probably prime*
Repeat *k* times:
Pick *a* randomly in the range [2, *n* − 2]

If     {\displaystyle a^{n-1}\not \equiv 1{\pmod {n}}}  ![815e1cde47b2d07520bc906454239520561c96b5](../_resources/22bbe37d1fb581cf2c840751c4407f13.png), then return *composite*

If composite is never returned: return *probably prime*

The *a* values 1 and *n*-1 are not used as the equality holds for all *n* and all odd *n* respectively, hence testing them adds no value.

### Complexity[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=4)]

Using fast algorithms for [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation) and multiprecision multiplication, the running time of this algorithm is [O](https://en.wikipedia.org/wiki/Big_O_notation)(*k* log2*n* log log *n* log log log *n*) = [Õ](https://en.wikipedia.org/wiki/Big_O_notation#Extensions_to_the_Bachmann%E2%80%93Landau_notations)(*k* log2*n*), where *k* is the number of times we test a random *a*, and *n* is the value we want to test for primality; see [Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity) for details.

## Flaw[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=5)]

First, there are infinitely many [Fermat pseudoprimes](https://en.wikipedia.org/wiki/Fermat_pseudoprime).

A more serious flaw is that there are infinitely many [Carmichael numbers](https://en.wikipedia.org/wiki/Carmichael_number). These are numbers     {\displaystyle n}  ![270580da7333505d9b73697417d0543c43c98b9f](../_resources/6dcd69860d2a056a804d0cf4a7021515.png) for which *all* values of     {\displaystyle a}  ![a601995d55609f2d9f5e233e36fbe9ea26011b3b](../_resources/ea06e9c22282f535102f8239e2d7740d.png) with     {\displaystyle gcd(a,n)=1}  ![c520cddbfd9b9b2faaabb767fe6facdd15f280f5](../_resources/649661c965a2f09754cf7069e43e2d10.png) are Fermat liars. For these numbers, repeated application of the Fermat primality test performs the same as a simple random search for factors. While Carmichael numbers are substantially rarer than prime numbers (Erdös' upper bound for the number of Carmichael numbers is lower than the [prime number function n/log(n)](https://en.wikipedia.org/wiki/Prime_number_theorem))[[2]](https://en.wikipedia.org/wiki/Fermat_primality_test#cite_note-2) there are enough of them that Fermat's primality test is not often used in the above form. Instead, other more powerful extensions of the Fermat test, such as [Baillie–PSW](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test), [Miller–Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test), and [Solovay–Strassen](https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test) are more commonly used.

In general, if     {\displaystyle n}  ![1f0573bb76faf03c96f4f7f70f92ccba01ab0ce6](../_resources/6dcd69860d2a056a804d0cf4a7021515.png) is a composite number that is not a Carmichael number, then at least half of all

   {\displaystyle a\in (\mathbb {Z} /n\mathbb {Z} )^{*}}  ![5cd3d0634d5191ee7e899f8ef9796280a678b26e](../_resources/d08937b5af08c67d0b197023e0027485.png) (i.e.     {\displaystyle gcd(a,n)=1}  ![c520cddbfd9b9b2faaabb767fe6facdd15f280f5](../_resources/649661c965a2f09754cf7069e43e2d10.png))

are Fermat witnesses. For proof of this, let     {\displaystyle a}  ![bb28ea099468bc147ae33ec20d2096742563cc87](../_resources/ea06e9c22282f535102f8239e2d7740d.png) be a Fermat witness and     {\displaystyle a_{1}}  ![ffd2487510aa438433a2579450ab2b3d557e5edc](../_resources/67d08a77ea4e21aee5d80fa1d610a1ec.png),     {\displaystyle a_{2}}  ![bbf42ecda092975c9c69dae84e16182ba5fe2e07](../_resources/ad8281b8132c752c6fd35b467f378166.png), ...,     {\displaystyle a_{s}}   be Fermat liars. Then

   {\displaystyle (a\cdot a_{i})^{n-1}\equiv a^{n-1}\cdot a_{i}^{n-1}\equiv a^{n-1}\not \equiv 1{\pmod {n}}}  ![edfbcb0ec5d661f87060ba0f4a328697567840f4](:/3efa0383d8a466db10026646bedfa14e)

and so all     {\displaystyle a\times a_{i}}   for     {\displaystyle i=1,2,...,s}  ![0bd73b4a924de38ea4041c2cbb6d7bb3871ad3be](../_resources/4fff31548f24c6113f20e2e13d44a868.png) are Fermat witnesses.

## Applications[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=6)]

As mentioned above, most applications use a [Miller–Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) or [Baillie–PSW](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test) test for primality. Sometimes a Fermat test (along with some trial division by small primes) is performed first to improve performance. [GMP](https://en.wikipedia.org/wiki/GNU_Multiple_Precision_Arithmetic_Library) since version 3.0 uses a base-210 Fermat test after trial division and before running Miller–Rabin tests. [Libgcrypt](https://en.wikipedia.org/wiki/Libgcrypt) uses a similar process with base 2 for the Fermat test, but [OpenSSL](https://en.wikipedia.org/wiki/OpenSSL) does not.

In practice with most big number libraries such as GMP, the Fermat test is not noticeably faster than a Miller–Rabin test, and can be slower for many inputs.[[3]](https://en.wikipedia.org/wiki/Fermat_primality_test#cite_note-3)

As an exception, OpenPFGW uses only the Fermat test for probable prime testing. The program is typically used with multi-thousand digit inputs with a goal of maximum speed with very large inputs. Another well known program that relies only on the Fermat test is [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) where it is only used for testing of self-generated large random values (an open source counterpart, [GNU Privacy Guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard), uses a Fermat pretest followed by Miller–Rabin tests).

## References[[edit](https://en.wikipedia.org/w/index.php?title=Fermat_primality_test&action=edit&section=7)]

- [Thomas H. Cormen](https://en.wikipedia.org/wiki/Thomas_H._Cormen), [Charles E. Leiserson](https://en.wikipedia.org/wiki/Charles_E._Leiserson), [Ronald L. Rivest](https://en.wikipedia.org/wiki/Ronald_L._Rivest), [Clifford Stein](https://en.wikipedia.org/wiki/Clifford_Stein) (2001). "Section 31.8: Primality testing". *[Introduction to Algorithms](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)* (Second ed.). MIT Press; McGraw-Hill. p. 889–890. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7).

1. **[^](https://en.wikipedia.org/wiki/Fermat_primality_test#cite_ref-PSW_1-0)**  [Carl Pomerance](https://en.wikipedia.org/wiki/Carl_Pomerance); [John L. Selfridge](https://en.wikipedia.org/wiki/John_L._Selfridge); [Samuel S. Wagstaff, Jr.](https://en.wikipedia.org/wiki/Samuel_S._Wagstaff,_Jr.) (July 1980). ["The pseudoprimes to 25·109"](https://math.dartmouth.edu/~carlp/PDF/paper25.pdf)  (PDF). *Mathematics of Computation*. **35** (151): 1003–1026. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1090/S0025-5718-1980-0572872-7](https://doi.org/10.1090%2FS0025-5718-1980-0572872-7). [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [2006210](https://www.jstor.org/stable/2006210).

2. **[^](https://en.wikipedia.org/wiki/Fermat_primality_test#cite_ref-2)**  [Paul Erdős](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s) (1956). "On pseudoprimes and Carmichael numbers". *Publ. Math. Debrecen*. **4**: 201–206.

3. **[^](https://en.wikipedia.org/wiki/Fermat_primality_test#cite_ref-3)**  Joe Hurd (2003), [*Verification of the Miller–Rabin Probabilistic Primality Test*](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.105.3196), p. 2

| [[hide]()]<br>- [v](https://en.wikipedia.org/wiki/Template:Number-theoretic_algorithms) ·<br>- [t](https://en.wikipedia.org/w/index.php?title=Template_talk:Number-theoretic_algorithms&action=edit&redlink=1) ·<br>- [e](https://en.wikipedia.org/w/index.php?title=Template:Number-theoretic_algorithms&action=edit)<br>[Number-theoretic](https://en.wikipedia.org/wiki/Number_theory)  [algorithms](https://en.wikipedia.org/wiki/Algorithm) |
| --- |
| [Primality tests](https://en.wikipedia.org/wiki/Primality_test) | - [AKS](https://en.wikipedia.org/wiki/AKS_primality_test) ·<br>- [APR](https://en.wikipedia.org/wiki/Adleman%E2%80%93Pomerance%E2%80%93Rumely_primality_test) ·<br>- [Baillie–PSW](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test) ·<br>- [Elliptic curve](https://en.wikipedia.org/wiki/Elliptic_curve_primality) ·<br>- [Pocklington](https://en.wikipedia.org/wiki/Pocklington_primality_test) ·<br>- [Fermat]() ·<br>- [Lucas](https://en.wikipedia.org/wiki/Lucas_primality_test) ·<br>- *[Lucas–Lehmer](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test)* ·<br>- *[Lucas–Lehmer–Riesel](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer%E2%80%93Riesel_test)* ·<br>- *[Proth's theorem](https://en.wikipedia.org/wiki/Proth%27s_theorem)* ·<br>- *[Pépin's](https://en.wikipedia.org/wiki/P%C3%A9pin%27s_test)* ·<br>- [Quadratic Frobenius](https://en.wikipedia.org/wiki/Quadratic_Frobenius_test) ·<br>- [Solovay–Strassen](https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test) ·<br>- [Miller–Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) |
| [Prime-generating](https://en.wikipedia.org/wiki/Generating_primes) | - [Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin) ·<br>- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) ·<br>- [Sieve of Sundaram](https://en.wikipedia.org/wiki/Sieve_of_Sundaram) ·<br>- [Wheel factorization](https://en.wikipedia.org/wiki/Wheel_factorization) |
| [Integer factorization](https://en.wikipedia.org/wiki/Integer_factorization) | - [Continued fraction (CFRAC)](https://en.wikipedia.org/wiki/Continued_fraction_factorization) ·<br>- [Dixon's](https://en.wikipedia.org/wiki/Dixon%27s_factorization_method) ·<br>- [Lenstra elliptic curve (ECM)](https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization) ·<br>- [Euler's](https://en.wikipedia.org/wiki/Euler%27s_factorization_method) ·<br>- [Pollard's rho](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm) ·<br>- [*p* − 1](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm) ·<br>- [*p* + 1](https://en.wikipedia.org/wiki/Williams%27s_p_%2B_1_algorithm) ·<br>- [Quadratic sieve (QS)](https://en.wikipedia.org/wiki/Quadratic_sieve) ·<br>- [General number field sieve (GNFS)](https://en.wikipedia.org/wiki/General_number_field_sieve) ·<br>- *[Special number field sieve (SNFS)](https://en.wikipedia.org/wiki/Special_number_field_sieve)* ·<br>- [Rational sieve](https://en.wikipedia.org/wiki/Rational_sieve) ·<br>- [Fermat's](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) ·<br>- [Shanks's square forms](https://en.wikipedia.org/wiki/Shanks%27s_square_forms_factorization) ·<br>- [Trial division](https://en.wikipedia.org/wiki/Trial_division) ·<br>- [Shor's](https://en.wikipedia.org/wiki/Shor%27s_algorithm) |
| [Multiplication](https://en.wikipedia.org/wiki/Multiplication_algorithm) | - [Ancient Egyptian](https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication) ·<br>- [Long](https://en.wikipedia.org/wiki/Long_multiplication) ·<br>- [Karatsuba](https://en.wikipedia.org/wiki/Karatsuba_algorithm) ·<br>- [Toom–Cook](https://en.wikipedia.org/wiki/Toom%E2%80%93Cook_multiplication) ·<br>- [Schönhage–Strassen](https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm) ·<br>- [Fürer's](https://en.wikipedia.org/wiki/F%C3%BCrer%27s_algorithm) |
| [Euclidean](https://en.wikipedia.org/wiki/Euclidean_division)  [division](https://en.wikipedia.org/wiki/Division_algorithm) | - [Binary](https://en.wikipedia.org/wiki/Binary_division) ·<br>- [Chunking](https://en.wikipedia.org/wiki/Chunking_(division)) ·<br>- [Fourier](https://en.wikipedia.org/wiki/Fourier_division) ·<br>- [Goldschmidt](https://en.wikipedia.org/wiki/Goldschmidt_division) ·<br>- [Newton-Raphson](https://en.wikipedia.org/wiki/Newton%E2%80%93Raphson_division) ·<br>- [Long](https://en.wikipedia.org/wiki/Long_division) ·<br>- [Short](https://en.wikipedia.org/wiki/Short_division) ·<br>- [SRT](https://en.wikipedia.org/wiki/SRT_division) |
| [Discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm) | - [Baby-step giant-step](https://en.wikipedia.org/wiki/Baby-step_giant-step) ·<br>- [Pollard rho](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms) ·<br>- [Pollard kangaroo](https://en.wikipedia.org/wiki/Pollard%27s_kangaroo_algorithm) ·<br>- [Pohlig–Hellman](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm) ·<br>- [Index calculus](https://en.wikipedia.org/wiki/Index_calculus_algorithm) ·<br>- [Function field sieve](https://en.wikipedia.org/wiki/Function_field_sieve) |
| [Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) | - [Binary](https://en.wikipedia.org/wiki/Binary_GCD_algorithm) ·<br>- [Euclidean](https://en.wikipedia.org/wiki/Euclidean_algorithm) ·<br>- [Extended Euclidean](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) ·<br>- [Lehmer's](https://en.wikipedia.org/wiki/Lehmer%27s_GCD_algorithm) |
| [Modular square root](https://en.wikipedia.org/wiki/Quadratic_residue) | - [Cipolla](https://en.wikipedia.org/wiki/Cipolla%27s_algorithm) ·<br>- [Pocklington's](https://en.wikipedia.org/wiki/Pocklington%27s_algorithm) ·<br>- [Tonelli–Shanks](https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm) ·<br>- [Berlekamp](https://en.wikipedia.org/wiki/Berlekamp%27s_root_finding_algorithm) |
| Other algorithms | - [Chakravala](https://en.wikipedia.org/wiki/Chakravala_method) ·<br>- [Cornacchia](https://en.wikipedia.org/wiki/Cornacchia%27s_algorithm) ·<br>- [Exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) ·<br>- [Integer square root](https://en.wikipedia.org/wiki/Integer_square_root) ·<br>- [LLL](https://en.wikipedia.org/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm) ·<br>- [Modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation) ·<br>- [Montgomery reduction](https://en.wikipedia.org/wiki/Montgomery_reduction) ·<br>- [Schoof's](https://en.wikipedia.org/wiki/Schoof%27s_algorithm) |
| - *Italics* indicate that algorithm is for numbers of special forms |

[Categories](https://en.wikipedia.org/wiki/Help:Category):

- [Primality tests](https://en.wikipedia.org/wiki/Category:Primality_tests)
- [Modular arithmetic](https://en.wikipedia.org/wiki/Category:Modular_arithmetic)