Latacora

#  Cryptographic Right Answers

We’re less interested in empowering developers and a lot more pessimistic about the prospects of getting this stuff right.

There are, in the literature and in the most sophisticated modern systems, “better” answers for many of these items. If you’re building for low-footprint embedded systems, you can use STROBE and a sound, modern, authenticated encryption stack entirely out of a single SHA-3-like sponge constructions. You can use NOISE to build a secure transport protocol with its own AKE. Speaking of AKEs, there are, like, 30 different password AKEs you could choose from.

But if you’re a developer and not a cryptography engineer, you shouldn’t do any of that. You should keep things simple and conventional and easy to analyze; “boring”, as the Google TLS people would say.

## Cryptographic Right Answers

### Encrypting Data

*Percival, 2009:* AES-CTR with HMAC.

*Ptacek, 2015:* (1) NaCl/libsodium’s default, (2) ChaCha20-Poly1305, or (3) AES-GCM.

*Latacora, 2018:* KMS or XSalsa20+Poly1305
*You care about this if:* you’re hiding information from users or the network.

If you are in a position to use KMS, Amazon’s (or Google’s) Hardware Security Module time share, use KMS. If you could use KMS but encrypting is just a fun weekend project and you might be able to save some money by minimizing your KMS usage, use KMS. If you’re just encrypting secrets like API tokens for your application at startup, use SSM Parameter Store, which is KMS. You don’t have to understand how KMS works.

Otherwise, what you want ideally is “AEAD”: authenticated encryption with additional data (the option for plaintext authenticated headers).

The mainstream way to get authenticated encryption is to use a stream cipher (usually: AES in CTR mode) composed with a polynomial MAC (a cryptographic CRC).

The problem you’ll run into with all those mainstream options is nonces: they want you to come up with a unique (usually random) number for each stream which can never be reused. It’s simplest to generate nonces from a secure random number generator, so you want a scheme that makes that easy.

Nonces are particularly important for AES-GCM, which is the most popular mode of encryption. Unfortunately, it’s particularly tricky with AES-GCM, where it’s just-barely-but-maybe-not-quite on the border of safe to use random nonces.

So we recommend you use XSalsa20-Poly1305. This is a species of “ChaPoly” constructions, which, put together, are the most common encryption constructions outside of AES-GCM. Get XSalsa20-Poly1305 from libsodium or NaCl.

The advantage to XSalsa20 over ChaCha20 and Salsa20 is that XSalsa supports an extended nonce; it’s big enough that you can simply generate a big long random nonce for every stream and not worry about how many streams you’re encrypting.

There are “NMR” or “MRAE” schemes in the pipeline that promise some degree of security even if nonces are mishandled; these include GCM-SIV (all the SIVs, really) and CAESAR-contest-finalist Deoxys-II. They’re interesting, but nobody really supports or uses them yet, and with an extended nonce, the security win is kind of marginal. They’re not boring. Stay boring for now.

*Avoid:* AES-CBC, AES-CTR by itself, block ciphers with 64-bit blocks — most especially Blowfish, which is inexplicably popular, OFB mode. Don’t ever use RC4, which is comically broken.

### Symmetric key length

*Percival, 2009*: Use 256-bit keys.
*Ptacek, 2015*: Use 256-bit keys.
*Latacora, 2018:* Go ahead and use 256 bit keys.
*You care about this if:* you’re using cryptography.

But remember: your AES key is far less likely to be broken than your public key pair, so the latter key size should be larger if you’re going to obsess about this.

*Avoid:* constructions with huge keys, cipher “cascades”, key sizes under 128 bits.

### Symmetric “Signatures”

*Percival, 2009*: Use HMAC.
*Ptacek, 2015*: Yep, use HMAC.
*Latacora, 2018:* Still HMAC.

*You care about this if:* you’re securing an API, encrypting session cookies, or are encrypting user data but, against medical advice, not using an AEAD construction.

If you’re authenticating but not encrypting, as with API requests, don’t do anything complicated. There is a class of crypto implementation bugs that arises from how you feed data to your MAC, so, if you’re designing a new system from scratch, Google “crypto canonicalization bugs”. Also, use a secure compare function.

If you use HMAC, people will feel the need to point out that SHA3 (and the truncated SHA2 hashes) can do “KMAC”, which is to say you can just concatenate the key and data and hash them and be secure. This means that in theory HMAC is doing unnecessary extra work with SHA-3 or truncated SHA-2. But who cares? Think of HMAC as cheap insurance for your design, in case someone switches to non-truncated SHA-2.

*Avoid:* custom “keyed hash” constructions, HMAC-MD5, HMAC-SHA1, complex polynomial MACs, encrypted hashes, CRC.

### Hashing algorithm

*Percival, 2009*: Use SHA256 (SHA-2).
*Ptacek, 2015*: Use SHA-2.
*Latacora, 2018:* Still SHA-2.
*You care about this if:* you always care about this.

If you can get away with it: use SHA-512/256, which truncates its output and sidesteps length extension attacks.

We still think it’s less likely that you’ll upgrade from SHA-2 to SHA-3 than it is that you’ll upgrade from SHA-2 to something faster than SHA-3, and SHA-2 still looks great, so get comfortable and cuddly with SHA-2.

*Avoid:* SHA-1, MD5, MD6.

### Random IDs

*Percival, 2009*: Use 256-bit random numbers.
*Ptacek, 2015*: Use 256-bit random numbers.
*Latacora, 2018:* Use 256-bit random numbers.
*You care about this if:* you always care about this.
From /dev/urandom.

*Avoid:* userspace random number generators, the OpenSSL RNG, havaged, prngd, egd, /dev/random.

### Password handling

*Percival, 2009*: scrypt or PBKDF2.

*Ptacek, 2015*: In order of preference, use scrypt, bcrypt, and then if nothing else is available PBKDF2.

*Latacora, 2018:* In order of preference, use scrypt, argon2, bcrypt, and then if nothing else is available PBKDF2.

*You care about this if:* you accept passwords from users or, anywhere in your system, have human-intelligible secret keys.

But, seriously: you can throw a dart at a wall to pick one of these. Technically, argon2 and scrypt are materially better than bcrypt, which is much better than PBKDF2. In practice, it mostly matters that you use a real secure password hash, and not as much which one you use.

Don’t build elaborate password-hash-agility schemes.
*Avoid:* SHA-3, naked SHA-2, SHA-1, MD5.

### Asymmetric encryption

*Percival, 2009*: Use RSAES-OAEP with SHA256 and MGF1+SHA256 bzzrt pop ffssssssst exponent 65537.

*Ptacek, 2015*: Use NaCl/libsodium (box / crypto_box).
*Latacora, 2018:* Use Nacl/libsodium (box / crypto_box).

*You care about this if*: you need to encrypt the same kind of message to many different people, some of them strangers, and they need to be able to accept the message asynchronously, like it was store-and-forward email, and then decrypt it offline. It’s a pretty narrow use case.

Of all the cryptographic “right answers”, this is the one you’re least likely to get right on your own. Don’t freelance public key encryption, and don’t use a low-level crypto library like OpenSSL or BouncyCastle.

Here are several reasons you should stop using RSA and switch to elliptic curve:

- RSA (and DH) drag you towards “backwards compatibility” (ie: downgrade-attack compatibility) with insecure systems.

- RSA begs implementors to encrypt directly with its public key primitive, which is usually not what you want to do

- RSA has too many knobs. In modern curve systems, like Curve25519, everything is pre-set for security.

NaCl uses Curve25519 (the most popular modern curve, carefully designed to eliminate several classes of attacks against the NIST standard curves) in conjunction with a ChaPoly AEAD scheme. Your language will have bindings (or, in the case of Go, its own library implementation) to NaCl; use them. Don’t try to assemble this yourself.

Don’t use RSA.

*Avoid:* Systems designed after 2015 that use RSA, RSA-PKCS1v15, RSA, ElGamal, I don’t know, Merkle-Hellman knapsacks? Just avoid RSA.

### Asymmetric signatures

*Percival, 2009*: Use RSASSA-PSS with SHA256 then MGF1+SHA256 in tricolor systemic silicate orientation.

*Ptacek, 2015*: Use Nacl, Ed25519, or RFC6979.
*Latacora, 2018:* Use Nacl or Ed25519.

*You care about this if*: you’re designing a new cryptocurrency. Or, a system to sign Ruby Gems or Vagrant images, or a DRM scheme, where the authenticity of a series of files arriving at random times needs to be checked offline against the same secret key. Or, you’re designing an encrypted message transport.

The allegations from the previous answer are incorporated herein as if stated in full.

The two dominating use cases within the last 10 years for asymmetric signatures are cryptocurrencies and forward-secret key agreement, as with ECDHE-TLS. The dominating algorithms for these use cases are all elliptic-curve based. Be wary of new systems that use RSA signatures.

In the last few years there has been a major shift away from conventional DSA signatures and towards misuse-resistent “deterministic” signature schemes, of which EdDSA and RFC6979 are the best examples. You can think of these schemes as “user-proofed” responses to the Playstation 3 ECDSA flaw, in which reuse of a random number leaked secret keys. Use deterministic signatures in preference to any other signature scheme.

Ed25519, the NaCl/libsodium default, is by far the most popular public key signature scheme outside of Bitcoin. It’s misuse-resistant and carefully designed in other ways as well. You shouldn’t freelance this either; get it from NaCl.

*Avoid:* RSA-PKCS1v15, RSA, ECDSA, DSA; really, especially avoid conventional DSA and ECDSA.

### Diffie-Hellman

*Percival, 2009*: Operate over the 2048-bit Group #14 with a generator of 2.
*Ptacek, 2015*: Probably still DH-2048, or Nacl.
*Latacora, 2018:* Probably nothing. Or use Curve25519.

*You care about this if:* you’re designing an encrypted transport or messaging system that will be used someday by a stranger, and so static AES keys won’t work.

The 2015 version of this document confused the hell out of everyone.

Part of the problem is that our “Right Answers” are a response to Colin Percival’s “Right Answers”, and his included a “Diffie-Hellman” answer, as if “Diffie-Hellmanning” was a thing developers routinely do. In reality, developers simply shouldn’t freelance their own encrypted transports. To get a sense of the complexity of this issue, read the documentation for the Noise Protocol Framework. If you’re doing a key-exchange with DH, you probably want an authenticated key exchange (AKE) that resists key compromise impersonation (KCI), and so the primitive you use for DH is not the only important security concern.

But whatever.

It remains the case: if you can just use NaCl, use NaCl. You don’t even have to care what NaCl does. That’s the point of NaCl.

Otherwise: use Curve25519. There are libraries for virtually every language. In 2015, we were worried about encouraging people to write their own Curve25519 libraries, with visions of Javascript bignum implementations dancing in our heads. But really, part of the point of Curve25519 is that the entire curve was carefully chosen to minimize implementation errors. Don’t write your own! But really, just use Curve25519.

Don’t do ECDH with the NIST curves, where you’ll have to carefully verify elliptic curve points before computing with them to avoid leaking secrets. That attack is very simple to implement, easier than a CBC padding oracle, and far more devastating.

The 2015 document included a clause about using DH-1024 in preference to sketchy curve libraries. You know what? That’s still a valid point. Valid and stupid. The way to solve the “DH-1024 vs. sketchy curve library” problem is, the same as the “should I use Blowfish or IDEA?” problem. Don’t have that problem. Use Curve25519.

*Avoid:* conventional DH, SRP, J-PAKE, handshakes and negotiation, elaborate key negotiation schemes that only use block ciphers, srand(time()).*

### Website security

*Percival, 2009*: Use OpenSSL.
*Ptacek, 2015*: Remains: OpenSSL, or BoringSSL if you can. Or just use AWS ELBs
*Latacora, 2018:* Use AWS ALB/ELB or OpenSSL, with LetsEncrypt
*You care about this if:* you have a website.
If you can pay AWS not to care about this problem, we recommend you do that.

Otherwise, there was a dark period between 2010 and 2016 where OpenSSL might not have been the right answer, but that time has passed. OpenSSL has gotten better, and, more importantly, OpenSSL is on-the-ball with vulnerability disclosure and response.

Using anything besides OpenSSL will drastically complicate your system for little, no, or even negative security benefit. So just keep it simple.

Speaking of simple: LetsEncrypt is free and automated. Set up a cron job to re-fetch certificates regularly, and test it.

*Avoid:* offbeat TLS libraries like PolarSSL, GnuTLS, and MatrixSSL.

### Client-server application security

*Percival, 2009*: Distribute the server’s public RSA key with the client code, and do not use SSL.

*Ptacek, 2015*: Use OpenSSL, or BoringSSL if you can. Or just use AWS ELBs
*Latacora, 2018:* Use AWS ALB/ELB or OpenSSL, with LetsEncrypt

*You care about this if:* the previous recommendations about public-key crypto were relevant to you.*

It seems a little crazy to recommend TLS given its recent history:

- The Logjam DH negotiation attack

- The FREAK export cipher attack

- The POODLE CBC oracle attack

- The RC4 fiasco

- The CRIME compression attack

- The Lucky13 CBC padding oracle timing attack

- The BEAST CBC chained IV attack

- Heartbleed

- Renegotiation

- Triple Handshakes

- Compromised CAs

- DROWN (though personally we’re warped and an opportunity to play with attacks like DROWN would be in our “pro” column)

Here’s why you should still use TLS for your custom transport problem:

- In custom protocols, you don’t have to (and shouldn’t) depend on 3rd party CAs. You don’t even have to use CAs at all (though it’s not hard to set up your own); you can just use a whitelist of self-signed certificates — which is approximately what SSH does by default, and what you’d come up with on your own.

- Since you’re doing a custom protocol, you can use the best possible TLS cipher suites: TLS 1.2+, Curve25519, and ChaPoly. That eliminates most attacks on TLS. The reason everyone doesn’t do this is that they need backwards-compatibility, but in custom protocols you don’t need that.

- Many of these attacks only work against browsers, because they rely on the victim accepting and executing attacker-controlled Javascript in order to generate repeated known/chosen plaintexts.

*Avoid:* designing your own encrypted transport, which is a genuinely hard engineering problem; using TLS but in a default configuration, like, with “curl”; using “curl”, IPSEC.

### Online backups

*Percival, 2009*: Use Tarsnap.
*Ptacek, 2015*: Use Tarsnap.

*Latacora, 2018:* Store PMAC-SIV-encrypted arc files to S3 and save fingerprints of your backups to an ERC20-compatible blockchain.

*You care about this if:* you bother backing things up.
Just kidding. You should still use Tarsnap.

 [03 April 2018](http://latacora.singles/2018/04/03/cryptographic-right-answers.html)