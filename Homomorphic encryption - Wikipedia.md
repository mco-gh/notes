Homomorphic encryption - Wikipedia

# ![wikipedia-wordmark-en.png](../_resources/c3c7d3eaa24fa41cf516cec0bf591564.png)Homomorphic encryption

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/Homomorphic_encryption#mw-head)[Jump to search](https://en.wikipedia.org/wiki/Homomorphic_encryption#p-search)

**Homomorphic encryption** is a form of [encryption](https://en.wikipedia.org/wiki/Encryption) that allows [computation](https://en.wikipedia.org/wiki/Computation) on [ciphertexts](https://en.wikipedia.org/wiki/Ciphertext), generating an encrypted result which, when decrypted, matches the result of the operations as if they had been performed on the [plaintext](https://en.wikipedia.org/wiki/Plaintext).

Homomorphic encryption can be used for privacy-preserving outsourced [storage](https://en.wikipedia.org/wiki/Cloud_storage) and [computation](https://en.wikipedia.org/wiki/Cloud_computing). This allows data to be encrypted and out-sourced to commercial cloud environments for processing, all while encrypted. In highly regulated industries, such as health care, homomorphic encryption can be used to enable new services by removing privacy barriers inhibiting data sharing. For example, [predictive analytics](https://en.wikipedia.org/wiki/Predictive_analytics) in health care can be hard to apply due to [medical data privacy](https://en.wikipedia.org/wiki/Medical_privacy) concerns, but if the predictive analytics service provider can operate on encrypted data instead, these privacy concerns are diminished.

## Contents

[hide]

- [1  Description](https://en.wikipedia.org/wiki/Homomorphic_encryption#Description)
- [2  History](https://en.wikipedia.org/wiki/Homomorphic_encryption#History)
    - [2.1  Pre-FHE](https://en.wikipedia.org/wiki/Homomorphic_encryption#Pre-FHE)
    - [2.2  First-Generation FHE](https://en.wikipedia.org/wiki/Homomorphic_encryption#First-Generation_FHE)
    - [2.3  Second-Generation FHE](https://en.wikipedia.org/wiki/Homomorphic_encryption#Second-Generation_FHE)
    - [2.4  Third-Generation FHE](https://en.wikipedia.org/wiki/Homomorphic_encryption#Third-Generation_FHE)
- [3  Fully Homomorphic Encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption#Fully_Homomorphic_Encryption)
    - [3.1  Implementations](https://en.wikipedia.org/wiki/Homomorphic_encryption#Implementations)
    - [3.2  Standardization](https://en.wikipedia.org/wiki/Homomorphic_encryption#Standardization)
- [4  Partially homomorphic cryptosystems](https://en.wikipedia.org/wiki/Homomorphic_encryption#Partially_homomorphic_cryptosystems)
- [5  See also](https://en.wikipedia.org/wiki/Homomorphic_encryption#See_also)
- [6  References](https://en.wikipedia.org/wiki/Homomorphic_encryption#References)
- [7  External links](https://en.wikipedia.org/wiki/Homomorphic_encryption#External_links)

## Description[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=1)]

Homomorphic encryption is a form of [encryption](https://en.wikipedia.org/wiki/Encryption) with an additional evaluation capability for computing over encrypted data without access to the [secret key](https://en.wikipedia.org/wiki/Key_(cryptography)). The result of such a computation remains encrypted. Homomorphic encryption can be viewed as an extension of either [symmetric-key](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) or [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography). *Homomorphic* refers to [homomorphism](https://en.wikipedia.org/wiki/Homomorphism) in algebra: the encryption and decryption functions can be thought as homomorphisms between plaintext and ciphertext spaces.

Homomorphic encryption includes multiple types of encryption schemes that can perform different classes of computations over encrypted data.[[1]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-ABG15-1)Some common types of homomorphic encryption are **partially** homomorphic, **somewhat** homomorphic, **leveled**  **fully** homomorphic, and **fully** homomorphic encryption. The computations are represented as either Boolean or arithmetic circuits. *Partially homomorphic encryption* encompasses schemes that support the evaluation of circuits consisting of only one type of gate, e.g., addition or multiplication. *Somewhat homomorphic encryption* schemes can evaluate two types of gates, but only for a subset of circuits. *Leveled fully homomorphic encryption* supports the evaluation of arbitrary circuits of bounded (pre-determined) depth. *Fully homomorphic encryption* (FHE) allows the evaluation of arbitrary circuits of unbounded depth, and is the strongest notion of homomorphic encryption. For the majority of homomorphic encryption schemes, the multiplicative depth of circuits is the main practical limitation in performing computations over encrypted data.

Homomorphic encryption schemes are inherently [malleable](https://en.wikipedia.org/wiki/Malleability_(cryptography)). In terms of malleability, homomorphic encryption schemes have weaker security properties than non-homomorphic schemes.

## History[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=2)]

Homomorphic encryption schemes have been developed using different approaches. Specifically, fully homomomorphic encryption schemes are often grouped into generations corresponding to the underlying approach.[[2]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-2)

### Pre-FHE[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=3)]

The problem of constructing a fully homomorphic encryption scheme was first proposed in 1978, within a year of publishing of the RSA scheme.[[3]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-3) For more than 30 years, it was unclear whether a solution existed. During that period, partial results included the following schemes:

- [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem) cryptosystem (unbounded number of modular multiplications);
- [ElGamal cryptosystem](https://en.wikipedia.org/wiki/ElGamal_encryption) (unbounded number of modular multiplications);
- [Goldwasser–Micali cryptosystem](https://en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem) (unbounded number of [exclusive or](https://en.wikipedia.org/wiki/Exclusive_or) operations);
- [Benaloh cryptosystem](https://en.wikipedia.org/wiki/Benaloh_cryptosystem) (unbounded number of modular additions);
- [Paillier cryptosystem](https://en.wikipedia.org/wiki/Paillier_cryptosystem) (unbounded number of modular additions);
- Sander-Young-Yung system (after more than 20 years solved the problem for logarithmic depth circuits);[[4]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-4)
- Boneh–Goh–Nissim cryptosystem (unlimited number of addition operations but at most one multiplication);[[5]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-5)
- Ishai-Paskin cryptosystem (polynomial-size [branching programs](https://en.wikipedia.org/wiki/Branching_programs)).[[6]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-6)

### First-Generation FHE[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=4)]

[Craig Gentry](https://en.wikipedia.org/wiki/Craig_Gentry_(computer_scientist)), using [lattice-based cryptography](https://en.wikipedia.org/wiki/Lattice-based_cryptography), described the first plausible construction for a fully homomorphic encryption scheme.[[7]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-7) Gentry's scheme supports both addition and multiplication operations on ciphertexts, from which it is possible to construct circuits for performing arbitrary computation. The construction starts from a *somewhat homomorphic* encryption scheme, which is limited to evaluating low-degree polynomials over encrypted data; it is limited because each ciphertext is noisy in some sense, and this noise grows as one adds and multiplies ciphertexts, until ultimately the noise makes the resulting ciphertext indecipherable. Gentry then shows how to slightly modify this scheme to make it *bootstrappable*, i.e., capable of evaluating its own decryption circuit and then at least one more operation. Finally, he shows that any bootstrappable somewhat homomorphic encryption scheme can be converted into a fully homomorphic encryption through a recursive self-embedding. For Gentry's "noisy" scheme, the bootstrapping procedure effectively "refreshes" the ciphertext by applying to it the decryption procedure homomorphically, thereby obtaining a new ciphertext that encrypts the same value as before but has lower noise. By "refreshing" the ciphertext periodically whenever the noise grows too large, it is possible to compute an arbitrary number of additions and multiplications without increasing the noise too much. Gentry based the security of his scheme on the assumed hardness of two problems: certain worst-case problems over [ideal lattices](https://en.wikipedia.org/wiki/Ideal_lattice_cryptography), and the sparse (or low-weight) subset sum problem. Gentry's Ph.D. thesis[[8]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-8)provides additional details. The Gentry-Halevi implementation of Gentry's original cryptosystem reported timing of about 30 minutes per basic bit operation.[[9]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-GH11-9) Extensive design and implementation work in subsequent years have improved upon these early implementations by many orders of magnitude runtime performance.

In 2010, Marten van Dijk, [Craig Gentry](https://en.wikipedia.org/wiki/Craig_Gentry_(computer_scientist)), [Shai Halevi](https://en.wikipedia.org/wiki/Shai_Halevi) and Vinod Vaikuntanathan presented a second fully homomorphic encryption scheme,[[10]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-10)which uses many of the tools of Gentry's construction, but which does not require [ideal lattices](https://en.wikipedia.org/wiki/Ideal_lattice_cryptography). Instead, they show that the somewhat homomorphic component of Gentry's ideal lattice-based scheme can be replaced with a very simple somewhat homomorphic scheme that uses integers. The scheme is therefore conceptually simpler than Gentry's ideal lattice scheme, but has similar properties with regards to homomorphic operations and efficiency. The somewhat homomorphic component in the work of van Dijk et al. is similar to an encryption scheme proposed by Levieil and [Naccache](https://en.wikipedia.org/wiki/David_Naccache) in 2008,[[11]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-11) and also to one that was proposed by [Bram Cohen](https://en.wikipedia.org/wiki/Bram_Cohen) in 1998.[[12]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-12)[Cohen's method](https://en.wikipedia.org/wiki/Cohen%27s_cryptosystem) is not even additively homomorphic, however. The Levieil–Naccache scheme supports only additions, but it can be modified to also support a small number of multiplications. Many refinements and optimizations of the scheme of van Dijk et al. were proposed in a sequence of works by Jean-Sébastien Coron, Tancrède Lepoint, Avradip Mandal, [David Naccache](https://en.wikipedia.org/wiki/David_Naccache), and Mehdi Tibouchi.[[13]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CNT12-13)[[14]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CMNT11-14)[[15]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CLT13-15)[[16]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CLT14-16)Some of these works included also implementations of the resulting schemes.

### Second-Generation FHE[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=5)]

The homomorphic cryptosystems in current use are derived from techniques that were developed starting in 2011-2012 by Zvika Brakerski, [Craig Gentry](https://en.wikipedia.org/wiki/Craig_Gentry_(computer_scientist)), Vinod Vaikuntanathan, and others. These innovations led to the development of much more efficient somewhat and fully homomorphic cryptosystems. These include:

- The Brakerski-Gentry-Vaikuntanathan (BGV, 2011) scheme,[[17]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-BGV12-17) building on techniques of Brakerski-Vaikuntanathan;[[18]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-BV11b-18)
- The [NTRU](https://en.wikipedia.org/wiki/NTRU)-based scheme by Lopez-Alt, Tromer, and Vaikuntanathan (LTV, 2012);[[19]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-LTV12-19)
- The Brakerski/Fan-Vercauteren (BFV, 2012) scheme,[[20]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-FV12-20) building on Brakerski's *scale-invariant* cryptosystem;[[21]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-Bra12-21)
- The [NTRU](https://en.wikipedia.org/wiki/NTRU)-based scheme by Bos, Lauter, Loftus, and Naehrig (BLLN, 2013),[[22]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-BLLN13-22) building on LTV and Brakerski's scale-invariant cryptosystem;[[21]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-Bra12-21)
- The Cheon-Kim-Kim-Song (CKKS, 2016) scheme.[[23]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CKKS17-23)

The security of most of these schemes is based on the hardness of the [(Ring) Learning With Errors](https://en.wikipedia.org/wiki/Ring_learning_with_errors) (RLWE) problem, except for the LTV and BLLN schemes that rely on an *overstretched*[[24]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-ABD16-24) variant of the [NTRU](https://en.wikipedia.org/wiki/NTRU) computational problem. This NTRU variant was subsequently shown vulnerable to subfield lattice attacks,[[25]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CJL16-25)[[24]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-ABD16-24) which is why these two schemes are no longer used in practice.

All the second-generation cryptosystems still follow the basic blueprint of Gentry's original construction, namely they first construct a somewhat homomorphic cryptosystem and then convert it to a fully homomorphic cryptosystem using bootstrapping.

A distinguishing characteristic of the second-generation cryptosystems is that they all feature a much slower growth of the noise during the homomorphic computations. Additional optimizations by [Craig Gentry](https://en.wikipedia.org/wiki/Craig_Gentry_(computer_scientist)), [Shai Halevi](https://en.wikipedia.org/wiki/Shai_Halevi), and [Nigel Smart](https://en.wikipedia.org/wiki/Nigel_Smart_(cryptographer)) resulted in cryptosystems with nearly optimal asymptotic complexity: Performing     {\displaystyle T}  ![ec7200acd984a1d3a3d7dc455e262fbe54f7f6e0](../_resources/00a7a42d9a4208a0974958f7b64c6dfb.png) operations on data encrypted with security parameter     {\displaystyle k}  ![ac480bac73b35feac6a73cae3bea008e2bb54dfe](../_resources/683452ab77f422026d457c808010969b.png) has complexity of only     {\displaystyle T\cdot \mathrm {polylog} (k)}  ![0b40c294890a4ef79031a1e9911bf388ff5dccdb](../_resources/17b65a0da323b4f64d9f45b52414f53e.png).[[26]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-GHS12a-26)[[27]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-GHS12b-27)[[28]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-GHS12c-28)These optimizations build on the Smart-Vercauteren techniques that enables packing of many plaintext values in a single ciphertext and operating on all these plaintext values in a [SIMD](https://en.wikipedia.org/wiki/SIMD) fashion.[[29]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-SV11-29)Many of the advances in these second-generation cryptosystems were also ported to the cryptosystem over the integers.[[15]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CLT13-15)[[16]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CLT14-16)

Another distinguishing feature of second-generation schemes is that they are efficient enough for many applications even without invoking bootstrapping, instead operating in the leveled FHE mode.

### Third-Generation FHE[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=6)]

In 2013, [Craig Gentry](https://en.wikipedia.org/wiki/Craig_Gentry_(computer_scientist)), [Amit Sahai](https://en.wikipedia.org/wiki/Amit_Sahai), and [Brent Waters](https://en.wikipedia.org/wiki/Brent_Waters) (GSW) proposed a new technique for building FHE schemes that avoids an expensive "relinearization" step in homomorphic multiplication.[[30]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-GSW13-30)Zvika Brakerski and Vinod Vaikuntanathan observed that for certain types of circuits, the GSW cryptosystem features an even slower growth rate of noise, and hence better efficiency and stronger security.[[31]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-31)Jacob Alperin-Sheriff and Chris Peikert then described a very efficient bootstrapping technique based on this observation.[[32]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-AP14-32)

These techniques were further improved to develop efficient ring variants of the GSW cryptosystem: FHEW (2014)[[33]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-FHEW-33) and TFHE (2016).[[34]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-TFHE-34) The FHEW scheme was the first to show that by refreshing the ciphertexts after every single operation, it is possible to reduce the bootstrapping time to a fraction of a second. FHEW introduced a new method to compute Boolean gates on encrypted data that greatly simplifies bootstrapping, and implemented a variant of the bootstrapping procedure.[[32]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-AP14-32) The efficiency of FHEW was further improved by the TFHE scheme, which implements a ring variant of the bootstrapping procedure[[35]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-GINX16-35) using a method similar to the one in FHEW.

## Fully Homomorphic Encryption[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=7)]

A cryptosystem that supports *arbitrary computation* on ciphertexts is known as fully homomorphic encryption (FHE). Such a scheme enables the construction of programs for any desirable functionality, which can be run on encrypted inputs to produce an encryption of the result. Since such a program need never decrypt its inputs, it can be run by an untrusted party without revealing its inputs and internal state. Fully homomorphic cryptosystems have great practical implications in the outsourcing of private computations, for instance, in the context of [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing).[[36]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-36)

### Implementations[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=8)]

There are no actively developed implementations of first-generation schemes. There are several open-source implementations of second- and third-generation fully homomorphic encryption schemes. Second-generation FHE implementations typically operate in the leveled FHE mode (though bootstrapping is still available in some libraries) and support efficient [SIMD](https://en.wikipedia.org/wiki/SIMD)-like packing of data; they are typically used to compute on encrypted integers or real/complex numbers. Third-generation FHE implementations often bootstrap after each Boolean gate operation but have limited support for packing and efficient arithmetic computations; they are typically used to compute Boolean circuits over encrypted bits. The choice of using a second-generation vs. third-generation scheme depends on the input data types and the desired computation.

#### Second-generation FHE implementations[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=9)]

- HElib[[37]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-HElib-37) by [IBM](https://en.wikipedia.org/wiki/IBM) implements the BGV scheme with the GHS optimizations, and the CKKS scheme;
- Microsoft SEAL[[38]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-SEAL-38) implements the BFV[[20]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-FV12-20) and the CKKS[[23]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CKKS17-23) encryption schemes;
- PALISADE[[39]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-PALISADE-39) by a consortium of defense contractors and academics, including [New Jersey Institute of Technology](https://en.wikipedia.org/wiki/New_Jersey_Institute_of_Technology), [Duality Technologies](https://en.wikipedia.org/w/index.php?title=Duality_Technologies&action=edit&redlink=1), [Raytheon BBN Technologies](https://en.wikipedia.org/wiki/Raytheon_BBN_Technologies), [MIT](https://en.wikipedia.org/wiki/MIT), [University of California, San Diego](https://en.wikipedia.org/wiki/University_of_California,_San_Diego) and others. PALISADE is a general-purpose lattice cryptography library implementing the BFV[[20]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-FV12-20), BGV, and other schemes;
- HEAAN[[40]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-HEAAN-40) by [Seoul National University](https://en.wikipedia.org/wiki/Seoul_National_University) implements the CKKS[[23]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CKKS17-23) scheme along with bootstrapping.[[41]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-CHK+18-41)

#### Third-generation FHE implementations[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=10)]

- FHEW[[33]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-FHEW-33) by Leo Ducas and Daniele Micciancio implements the FHEW scheme.
- TFHE[[34]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-TFHE-34) by Ilaria Chillotti, Nicolas Gama, Mariya Georgieva and Malika Izabachene implements the TFHE scheme.

#### FHE Frameworks[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=11)]

- E3[[42]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-E3-42) by MoMA Lab at NYU Abu Dhabi implements TFHE, FHEW, HElib and SEAL.

### Standardization[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=12)]

A community standard for homomorphic encryption is maintained by the [HomomorphicEncryption.org](http://homomorphicencryption.org/) group, an open industry/government/academia consortium founded in 2017. The current [standard document](http://homomorphicencryption.org/standard) includes specifications of secure parameters for RLWE.

An up-to-date [list of homomorphic encryption implementations](http://homomorphicencryption.org/introduction/) is also maintained by the consortium.

## Partially homomorphic cryptosystems[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=13)]

In the following examples, the notation     {\displaystyle {\mathcal {E}}(x)}  ![0a07d98bb302f3856cbabc47b2b9016692e3f7bc](../_resources/a92b12d2b080bb8cd76d581517868c5d.png) is used to denote the encryption of the message     {\displaystyle x}  ![cd253103f0876afc68ebead27a5aa9867d927467](../_resources/cfd6bde62de4abd8608da873d74673c3.png).

**Unpadded RSA**

If the [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem) public key is modulus     {\displaystyle m}  ![c3c9a2c7b599b37105512c5d570edc034056dd40](../_resources/93cf2921fbff35206a93ae4b80e30535.png) and exponent     {\displaystyle e}  ![e7747e267654e52914dfc60df53fcf13045f84a9](../_resources/dcf5b1fa11167deee394a341bf0c466f.png), then the encryption of a message     {\displaystyle x}  ![87f9e315fd7e2ba406057a97300593c4802b53e4](../_resources/cfd6bde62de4abd8608da873d74673c3.png) is given by     {\displaystyle {\mathcal {E}}(x)=x^{e}\;{\bmod {\;}}m}  ![08785e1dbf38fdcfa1c23c1c23710da058d26445](../_resources/b3ad9bdbbb4b123084442bdf3e9b45eb.png). The homomorphic property is then

   {\displaystyle {\mathcal {E}}(x_{1})\cdot {\mathcal {E}}(x_{2})=x_{1}^{e}x_{2}^{e}\;{\bmod {\;}}m=(x_{1}x_{2})^{e}\;{\bmod {\;}}m={\mathcal {E}}(x_{1}\cdot x_{2})}  ![469e1a27f47c03e3f8a993c46440eec9d52aa54b](../_resources/efd38e498d091be76e28669d0aa56ec7.png)

**ElGamal**

In the [ElGamal cryptosystem](https://en.wikipedia.org/wiki/ElGamal_encryption), in a cyclic group     {\displaystyle G}  ![8b16e2bdaefee9eed86d866e6eba3ac47c710f60](../_resources/56411a68078a8b696490d4012a633f08.png) of order     {\displaystyle q}  ![f5f3c8921a3b352de45446a6789b104458c9f90b](../_resources/8c1033b70c06672cfedf526d057775b4.png) with generator     {\displaystyle g}  ![d3556280e66fe2c0d0140df20935a6f057381d77](../_resources/757377ef72c3defe7c65998c3d0142ee.png), if the public key is     {\displaystyle (G,q,g,h)}  ![da0ac9490f7f974c22c1a32d48d8df1458fd7111](../_resources/d5259e009d0c7a6cb964347e42e06425.png), where     {\displaystyle h=g^{x}}  ![06809d64fa7c817ffc7e323f85997f783dbdf71d](../_resources/6116a4f835aeb4ca6f0bacd1fe94e437.png), and     {\displaystyle x}   is the secret key, then the encryption of a message     {\displaystyle m}   is     {\displaystyle {\mathcal {E}}(m)=(g^{r},m\cdot h^{r})}  ![71e22fb123c84124e19c4912ecf1033c171ebb9a](../_resources/76a903be9a4afb2ac90d40fb75f99abb.png), for some random     {\displaystyle r\in \{0,\ldots ,q-1\}}  ![dcb3f33b191e2ac08e336a0c32d242d836158b74](../_resources/2c56a3802747dc912380bdbcb61f1d09.png). The homomorphic property is then

   {\displaystyle {\begin{aligned}&{\mathcal {E}}(m_{1})\cdot {\mathcal {E}}(m_{2})=(g^{r_{1}},m_{1}\cdot h^{r_{1}})(g^{r_{2}},m_{2}\cdot h^{r_{2}})\\[6pt]={}&(g^{r_{1}+r_{2}},(m_{1}\cdot m_{2})h^{r_{1}+r_{2}})={\mathcal {E}}(m_{1}\cdot m_{2}).\end{aligned}}}  ![b3e194a9c084269d38cf94c30ef174257a373db5](../_resources/1985a665d97691083106208839078702.png)

**Goldwasser–Micali**

In the [Goldwasser–Micali cryptosystem](https://en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem), if the public key is the modulus *m* and quadratic non-residue *x*, then the encryption of a bit *b* is     {\displaystyle {\mathcal {E}}(b)=x^{b}r^{2}\;{\bmod {\;}}m}  ![52fcf6b78cb718843b8766d5aa0204e7edc42e5b](../_resources/4e207fbd0fa56e2181583ade2ee8bbda.png), for some random     {\displaystyle r\in \{0,\ldots ,m-1\}}  ![8aa4b4e1b5f5c59441cc2bdd3940cbad2c41a9b6](../_resources/2d285199ead643c75ca689a33d25f33c.png). The homomorphic property is then

   {\displaystyle {\mathcal {E}}(b_{1})\cdot {\mathcal {E}}(b_{2})=x^{b_{1}}r_{1}^{2}x^{b_{2}}r_{2}^{2}\;{\bmod {\;}}m=x^{b_{1}+b_{2}}(r_{1}r_{2})^{2}\;{\bmod {\;}}m={\mathcal {E}}(b_{1}\oplus b_{2})}  ![5c0e028e528aeaec6768826744d53ee05a38af4e](../_resources/241e680d85099bd704eeafdc646995ba.png)

where     {\displaystyle \oplus }   denotes addition modulo 2, (i.e. [exclusive-or](https://en.wikipedia.org/wiki/Exclusive_disjunction)).

**Benaloh**

In the [Benaloh cryptosystem](https://en.wikipedia.org/wiki/Benaloh_cryptosystem), if the public key is the modulus *m* and the base *g* with a blocksize of *c*, then the encryption of a message *x* is     {\displaystyle {\mathcal {E}}(x)=g^{x}r^{c}\;{\bmod {\;}}m}  ![32fe5baaabd78669c94eed846c2693a31644a87a](../_resources/00fafcbd570257b91fcc3f99f5d42e64.png), for some random     {\displaystyle r\in \{0,\ldots ,m-1\}}  ![8aa4b4e1b5f5c59441cc2bdd3940cbad2c41a9b6](../_resources/2d285199ead643c75ca689a33d25f33c.png). The homomorphic property is then

   {\displaystyle {\mathcal {E}}(x_{1})\cdot {\mathcal {E}}(x_{2})\;{\bmod {\;}}m=(g^{x_{1}}r_{1}^{c})(g^{x_{2}}r_{2}^{c})\;{\bmod {\;}}m=g^{x_{1}+x_{2}}(r_{1}r_{2})^{c}={\mathcal {E}}(x_{1}+x_{2})}  ![8ab5287db24faba1d57eeddade08224d97b9947f](../_resources/44bbffa6307b6db57a7e38cc48144c01.png)

**Paillier**

In the [Paillier cryptosystem](https://en.wikipedia.org/wiki/Paillier_cryptosystem), if the public key is the modulus *m* and the base *g*, then the encryption of a message *x* is     {\displaystyle {\mathcal {E}}(x)=g^{x}r^{m}\;{\bmod {\;}}m^{2}}  ![f73836b00d4611307d90738b19b6791559991cb4](../_resources/4f1be4aee39022a1377626c13b066e84.png), for some random     {\displaystyle r\in \{0,\ldots ,m-1\}}  ![8aa4b4e1b5f5c59441cc2bdd3940cbad2c41a9b6](../_resources/2d285199ead643c75ca689a33d25f33c.png). The homomorphic property is then

   {\displaystyle {\mathcal {E}}(x_{1})\cdot {\mathcal {E}}(x_{2})=(g^{x_{1}}r_{1}^{m})(g^{x_{2}}r_{2}^{m})\;{\bmod {\;}}m^{2}=g^{x_{1}+x_{2}}(r_{1}r_{2})^{m}\;{\bmod {\;}}m^{2}={\mathcal {E}}(x_{1}+x_{2})}  ![b589edb1cb4aaff9deabd1f42a1fe4bdf7b672ce](../_resources/85d416ced70dff642a57986901e704c8.png)

**Other partially homomorphic cryptosystems**

- [Okamoto–Uchiyama cryptosystem](https://en.wikipedia.org/wiki/Okamoto%E2%80%93Uchiyama_cryptosystem)
- [Naccache–Stern cryptosystem](https://en.wikipedia.org/wiki/Naccache%E2%80%93Stern_cryptosystem)
- [Damgård–Jurik cryptosystem](https://en.wikipedia.org/wiki/Damg%C3%A5rd%E2%80%93Jurik_cryptosystem)
- Sander–Young–Yung encryption scheme
- Boneh–Goh–Nissim cryptosystem
- Ishai–Paskin cryptosystem
- Castagnos–Laguillaumie cryptosystem[[43]](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_note-43)

## See also[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=14)]

- [Homomorphic secret sharing](https://en.wikipedia.org/wiki/Homomorphic_secret_sharing)
- [Homomorphic signatures for network coding](https://en.wikipedia.org/wiki/Homomorphic_signatures_for_network_coding)
- [Private biometrics](https://en.wikipedia.org/wiki/Private_biometrics)
- [Verifiable computing using a fully homomorphic scheme](https://en.wikipedia.org/wiki/Verifiable_computing)
- [Client-side encryption](https://en.wikipedia.org/wiki/Client-side_encryption)
- [Secure multi-party computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation)
- [Format-preserving encryption](https://en.wikipedia.org/wiki/Format-preserving_encryption)
- [Polymorphic code](https://en.wikipedia.org/wiki/Polymorphic_code)

## References[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=15)]

1. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-ABG15_1-0)**  Armknecht, Frederik; Boyd, Colin; Gjøsteen, Kristian; Jäschke, Angela; Reuter, Christian; Strand, Martin (2015). ["A Guide to Fully Homomorphic Encryption"](https://eprint.iacr.org/2015/1192).

2. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-2)**  Vinod Vaikuntanathan. ["Homomorphic Encryption References"](https://people.csail.mit.edu/vinodv/FHE/FHE-refs.html)  (HTML).

3. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-3)**  R. L. Rivest, L. Adleman, and M. L. Dertouzos. On data banks and privacy homomorphisms. In *Foundations of Secure Computation*, 1978.

4. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-4)**  Sander, Tomas; Young, Adam L.; Yung, Moti (1999). *Non-Interactive CryptoComputing For NC1*. *Focs1991*. pp. 554–566. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1109/SFFCS.1999.814630](https://doi.org/10.1109%2FSFFCS.1999.814630). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-7695-0409-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-7695-0409-4).

5. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-5)**  D. Boneh, E. Goh, and K. Nissim. Evaluating 2-DNF Formulas on Ciphertexts. In *Theory of Cryptography Conference*, 2005.

6. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-6)**  Y. Ishai and A. Paskin. Evaluating branching programs on encrypted data. In *Theory of Cryptography Conference*, 2007.

7. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-7)**  Craig Gentry. [Fully Homomorphic Encryption Using Ideal Lattices](http://portal.acm.org/citation.cfm?id=1536414.1536440). In *the 41st ACM Symposium on Theory of Computing (STOC)*, 2009.

8. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-8)**  Craig Gentry. ["A Fully Homomorphic Encryption Scheme (Ph.D. thesis)"](http://crypto.stanford.edu/craig/)  (PDF).

9. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-GH11_9-0)**  Gentry, Craig; Halevi, Shai (2010). ["Implementing Gentry's fully-homomorphic encryption scheme"](http://eprint.iacr.org/2010/520). *Eurocrypt 2011*.

10. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-10)**  Marten, van Dijk; Gentry, Craig; Halevi, Shai; Vinod, Vaikuntanathan (2009). ["Fully Homomorphic Encryption over the Integers"](http://eprint.iacr.org/2009/616). *Eurocrypt 2010*.

11. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-11)**  Levieil, Eric; [Naccache, David](https://en.wikipedia.org/wiki/David_Naccache). ["Cryptographic Test Correction"](https://www.iacr.org/archive/pkc2008/49390088/49390088.pdf)  (PDF).

12. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-12)**  [Cohen, Bram](https://en.wikipedia.org/wiki/Bram_Cohen). ["Simple Public Key Encryption"](https://web.archive.org/web/20111007060226/http://bramcohen.com/simple_public_key.html). Archived from [the original](http://bramcohen.com/simple_public_key.html) on 2011-10-07.

13. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CNT12_13-0)**  Coron, Jean-Sébastien; Naccache, David; Tibouchi, Mehdi (2011). ["Public Key Compression and Modulus Switching for Fully Homomorphic Encryption over the Integers"](http://eprint.iacr.org/2011/440). *Eurocrypt 2012*.

14. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CMNT11_14-0)**  Coron, Jean-Sébastien; Mandal, Avradip; Naccache, David; Tibouchi, Mehdi (2011). ["Fully Homomorphic Encryption over the Integers with Shorter Public Keys"](http://eprint.iacr.org/2011/441). *Crypto 2011*. Lecture Notes in Computer Science. **6841**: 487–504. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/978-3-642-22792-9_28](https://doi.org/10.1007%2F978-3-642-22792-9_28). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-3-642-22791-2](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-22791-2).

15. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CLT13_15-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CLT13_15-1)  Coron, Jean-Sébastien; Lepoint, Tancrède; Tibouchi, Mehdi (2013). ["Batch Fully Homomorphic Encryption over the Integers"](http://eprint.iacr.org/2013/036). *Eurocrypt 2013*.

16. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CLT14_16-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CLT14_16-1)  Coron, Jean-Sébastien; Lepoint, Tancrède; Tibouchi, Mehdi (2014). ["Scale-Invariant Fully Homomorphic Encryption over the Integers"](http://eprint.iacr.org/2014/032). *PKC 2014*.

17. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-BGV12_17-0)**  Z. Brakerski, C. Gentry, and V. Vaikuntanathan. [Fully Homomorphic Encryption without Bootstrapping](http://eprint.iacr.org/2011/277), In *ITCS 2012*

18. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-BV11b_18-0)**  Z. Brakerski and V. Vaikuntanathan. [Efficient Fully Homomorphic Encryption from (Standard) LWE](http://eprint.iacr.org/2011/344). In *FOCS 2011* (IEEE)

19. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-LTV12_19-0)**  A. Lopez-Alt, E. Tromer, and V. Vaikuntanathan. [On-the-Fly Multiparty Computation on the Cloud via Multikey Fully Homomorphic Encryption](https://eprint.iacr.org/2013/094). In *STOC 2012* (ACM)

20. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-FV12_20-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-FV12_20-1)  [***c***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-FV12_20-2)  Fan, Junfeng; Vercauteren, Frederik (2012). ["Somewhat Practical Fully Homomorphic Encryption"](https://eprint.iacr.org/2012/144).

21. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-Bra12_21-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-Bra12_21-1)  Z. Brakerski. [Fully Homomorphic Encryption without Modulus Switching from Classical GapSVP](http://eprint.iacr.org/2012/078), In *CRYPTO 2012* (Springer)

22. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-BLLN13_22-0)**  J. Bos, K. Lauter, J. Loftus, and M. Naehrig. [Improved Security for a Ring-Based Fully Homomorphic Encryption Scheme](https://eprint.iacr.org/2013/075). In *IMACC 2013* (Springer)

23. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CKKS17_23-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CKKS17_23-1)  [***c***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CKKS17_23-2)  Cheon, Jung Hee; Kim, Andrey; Kim, Miran; Song, Yongsoo (2017). "Homomorphic encryption for arithmetic of approximate numbers". *Takagi T., Peyrin T. (eds) Advances in Cryptology – ASIACRYPT 2017*. ASIACRYPT 2017. Springer, Cham. pp. 409–437. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/978-3-319-70694-8_15](https://doi.org/10.1007%2F978-3-319-70694-8_15).

24. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-ABD16_24-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-ABD16_24-1)  M. Albrecht, S. Bai, and L. Ducas. [A subfield lattice attack on overstretched NTRU assumptions](https://eprint.iacr.org/2016/127), In *CRYPTO 2016* (Springer)

25. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CJL16_25-0)**  Cheon, J. H.; Jeong, J; Lee, C. (2016). "An algorithm for NTRU problems and cryptanalysis of the GGH multilinear map without a low-level encoding of zero". *LMS Journal of Computation and Mathematics*. **19** (1): 255–266. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1112/S1461157016000371](https://doi.org/10.1112%2FS1461157016000371).

26. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-GHS12a_26-0)**  C. Gentry, S. Halevi, and N. P. Smart. [Fully Homomorphic Encryption with Polylog Overhead](http://eprint.iacr.org/2011/566). In *EUROCRYPT 2012* (Springer)

27. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-GHS12b_27-0)**  C. Gentry, S. Halevi, and N. P. Smart. [Better Bootstrapping in Fully Homomorphic Encryption](http://eprint.iacr.org/2011/680). In *PKC 2012* (SpringeR)

28. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-GHS12c_28-0)**  C. Gentry, S. Halevi, and N. P. Smart. [Homomorphic Evaluation of the AES Circuit](http://eprint.iacr.org/2012/099). In *CRYPTO 2012* (Springer)

29. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-SV11_29-0)**  Smart, Nigel P.; Vercauteren, Frederik (2014). ["Fully Homomorphic SIMD Operations"](http://eprint.iacr.org/2011/133). *Designs, Codes and Cryptography*. **71** (1): 57–81. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/s10623-012-9720-4](https://doi.org/10.1007%2Fs10623-012-9720-4).

30. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-GSW13_30-0)**  C. Gentry, A. Sahai, and B. Waters. [Homomorphic Encryption from Learning with Errors: Conceptually-Simpler, Asymptotically-Faster, Attribute-Based](http://eprint.iacr.org/2013/340). In *CRYPTO 2013* (Springer)

31. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-31)**  Z. Brakerski and V. Vaikuntanathan. [Lattice-Based FHE as Secure as PKE](http://eprint.iacr.org/2013/541). In *ITCS 2014*

32. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-AP14_32-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-AP14_32-1)  J. Alperin-Sheriff and C. Peikert. [Faster Bootstrapping with Polynomial Error](http://eprint.iacr.org/2014/094). In *CRYPTO 2014* (Springer)

33. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-FHEW_33-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-FHEW_33-1)  Leo Ducas; Daniele Micciancio. ["FHEW: A Fully Homomorphic Encryption library"](https://github.com/lducas/FHEW). Retrieved 31 December 2014.

34. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-TFHE_34-0)  [***b***](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-TFHE_34-1)  Ilaria Chillotti; Nicolas Gama; Mariya Georgieva; Malika Izabachene. ["Faster Fully Homomorphic Encryption: Bootstrapping in less than 0.1 Seconds"](https://tfhe.github.io/tfhe). Retrieved 31 December 2016.

35. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-GINX16_35-0)**  N. Gama, M. Izabachène, P.Q. Nguyen, and X. Xie [Structural Lattice Reduction: Generalized Worst-Case to Average-Case Reductions and Homomorphic Cryptosystems](https://eprint.iacr.org/2014/283). In *EUROCRYPT 2016* (Springer)

36. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-36)**  Daniele Micciancio (2010-03-01). ["A First Glimpse of Cryptography's Holy Grail"](http://cacm.acm.org/magazines/2010/3/76275-a-first-glimpse-of-cryptographys-holy-grail/fulltext). [Association for Computing Machinery](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery). p. 96. Retrieved 2010-03-17.

37. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-HElib_37-0)**  Shai Halevi; Victor Shoup. ["HElib: An Implementation of homomorphic encryption"](https://github.com/homenc/HElib). Retrieved 31 December 2014.

38. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-SEAL_38-0)**  Microsoft Research. ["Microsoft SEAL"](https://www.microsoft.com/en-us/research/project/microsoft-seal). Retrieved 20 February 2019.

39. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-PALISADE_39-0)**  ["PALISADE Lattice Cryptography Library"](http://palisade-crypto.org/). Retrieved 1 January 2019.

40. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-HEAAN_40-0)**  Jung Hee Cheon; Kyoohyung Han; Andrey Kim; Miran Kim; Yongsoo Song. ["Homomorphic Encryption for Arithmetic of Approximate Numbers"](https://github.com/snucrypto/HEAAN). Retrieved 15 May 2016.

41. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-CHK+18_41-0)**  Jung Hee Cheon, Kyoohyung Han, Andrey Kim, Miran Kim and Yongsoo Song. [Bootstrapping for Approximate Homomorphic Encryption](https://eprint.iacr.org/2018/153). In *EUROCRYPT 2018 (Springer)*.

42. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-E3_42-0)**  MoMA Lab, New York University Abu Dhabi (2019-07-24). ["Encrypt-Everything-Everywhere (E3)"](https://github.com/momalab/e3). Retrieved 27 July 2019.

43. **[^](https://en.wikipedia.org/wiki/Homomorphic_encryption#cite_ref-43)**  Guilhem Castagnos and Fabien Laguillaumie (2015). ["Linearly Homomorphic Encryption from DDH"](https://eprint.iacr.org/2015/047.pdf)  (PDF).

## External links[[edit](https://en.wikipedia.org/w/index.php?title=Homomorphic_encryption&action=edit&section=16)]

- [HomomorphicEncryption.org](http://homomorphicencryption.org/); an open standardization effort for fully homomorphic encryption
- [Daniele Micciancio's FHE references](http://cseweb.ucsd.edu/~daniele/LatticeLinks/FHE.html)
- [Vinod Vaikuntanathan's FHE references](https://people.csail.mit.edu/vinodv/FHE/FHE-refs.html)
- ["Alice and Bob in Cipherspace"](https://www.americanscientist.org/article/alice-and-bob-in-cipherspace). *American Scientist*. September 2012. Retrieved 2018-05-08.
- [HElib](https://github.com/shaih/HElib), open-source homomorphic encryption library
- [Microsoft SEAL](https://www.microsoft.com/en-us/research/project/microsoft-seal), open-source homomorphic encryption library by Microsoft
- [PALISADE](http://palisade-crypto.org/), open-source lattice cryptography framework
- [HEAAN](https://github.com/snucrypto/HEAAN), open-source homomorphic encryption library
- [FHEW](https://github.com/lducas/FHEW), open-source homomorphic encryption library
- [TFHE](https://tfhe.github.io/tfhe), open-source homomorphic encryption library

[Categories](https://en.wikipedia.org/wiki/Help:Category):

- [Cryptographic primitives](https://en.wikipedia.org/wiki/Category:Cryptographic_primitives)
- [Public-key cryptography](https://en.wikipedia.org/wiki/Category:Public-key_cryptography)
- [Homeomorphisms](https://en.wikipedia.org/wiki/Category:Homeomorphisms)