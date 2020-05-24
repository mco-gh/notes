Blockchains from the ground up: Part 1 - John Mathews

#  Blockchains from the ground up: Part 1

Using a scenario that begins with the exchange of apples for oranges, understand the essential concepts and advantages of blockchains.

By John Mathews

May 25 2017

# How to maintain a reliable list across a small network without a central authority

This is part 1 of an introduction to the key features of a generalised blockchain. I haven’t included references to Bitcoin or any particular digital currencies or blockchain implementations. This is because a digital currency is just one application of blockchain technology.

## Create a financial document that cannot be forged or disputed

Let’s imagine there is a village somewhere where people still trade by bartering. John has some apples whilst Lizzie has some oranges. John would like an orange, and offers Lizzie an apple in exchange. She accepts, and writes John a receipt.

Date: 1234From: LizzieTo: John What: 1 Orange Price: 1 Apple

So far, so good. The receipt is evidence of the transaction. The next day John wants an orange but doesn’t have anything to exchange. He offers to write Lizzie a note saying he owes Lizzie 1 orange (an [IOU](https://en.wikipedia.org/wiki/IOU)). They think about this and agree that John should sign the note so that Lizzie can prove that John owes her 1 orange.

Date: 1234From: JohnTo: LizzieWhat: 1 OrangeSigned: John's signature, Lizzie's signature

This IOU is a nice gesture, but it’s simple to forge. Lizzie has the only copy of the IOU and once Lizzie has seen Johns signature, she could easily copy it and create more IOU’s. She could also change this IOU from 1 orange to 11 oranges (for example) and John couldn’t prove what the original amount was. If Lizzie and John disagreed over what was owed it would be impossible to know who was telling the truth. Its one persons word against the other.

Lizzie realises this and suggests an improvement - they will find a witness and make 3 copies of the IOU. Each copy will be signed by Lizzie, John and the Witness. Lets call this witness “Walter”.

Date: 1234From: JohnTo: LizzieWhat: 1 OrangeWitness: WalterSigned: "John's signature", "Lizzie's signature", "Walter's signature"""

This is a much stronger document and is more difficult to forge. If Lizzie changes the “What:” to “11 Oranges”, both John and Walter will have copies of the original with her signature on it. It will be 2 pieces of evidence against Lizzie’s 1. Lizzie will be laughed out of court. Hahaha.

3 Party transactions work pretty well, and this is how most transactions are recorded today. But there is a weakness: If Lizzie can bribe Walter then the transaction can be falsified! John would rely on Walter to verify his version of the transaction but would be let down by Walters lack of integrity. Lizzie and Walter could change 1 orange to 11 oranges and if Lizzie offered Walter some of the extra oranges this would give them both an incentive to forge the documentation. If Walter liked oranges enough, he might not care that his career as a witness will be ruined.

This is a problem for modern financial systems and a great deal of time, money and regulation is devoted to trying to ensure that third parties are trustworthy. E.g. If I buy a car and my bank is in cahoots with the car dealership, I could be defrauded. Reducing this risk to an acceptably low level makes financial services slower and more expensive than they would otherwise need to be.

The solution is [public-key infrastructure](https://en.wikipedia.org/wiki/Public-key_cryptography) (which is introduced in my [previous post](http://johnmathews.eu/encryption.html)). In this system, each individual generates their own public-private key pair. They keep their private key private and make their public key freely available. A detailed description of public-key cryptography is out of scope for this post, but briefly:

A public key is derived from a private key, and this pair together have a set of unique mathematical properties. Either key can be used to encrypt a message but only the other key can be used to decrypt it. You cannot use the same key to encrypt and decrypt a message. If the private key is used to encrypt then anybody can decrypt (because the public key is publicly available) and whilst this is clearly a terrible way to keep a secret it’s a great way to verify who encrypted the message, because only one person has the private key. Because of this, using a private key to encrypt a message is effectively creating a digital signature which cannot be forged. (If the public key is used to encrypt a message then only the private key can be used to decrypt it, and this approach is used to transfer secret data securely).

Back to the fruit. If Lizzie wants to accept Johns IOU she can use public-key cryptography and no-one needs to worry about Walter. There are 3 steps to the transaction.

1] Create the IOU stating that John owes Lizzie 1 orange.
Date: 1234 From: John To: Lizzie What: 1 Orange

2] John creates a public private key pair and encrypts the IOU using his private key. He adds an unencrypted “From” line.

From: John Date: 1234 To: Lizzie, What: 1 Orange <- Signed and encrypted by John using his private key

3] John makes his public key freely available to anyone who wants it.

This will work because anybody (not just Lizzie) can check that John signed the IOU. The transaction can be verified by looking at the “From” part of that transaction, noticing that this transaction is supposedly from John and then using John’s public key to decrypt the encoded “signature” line.

The signature can only be decrypted using John’s public key if his private key was used to encrypt it. Because John is the only person with his private key, that proves the transaction is valid, and Lizzie isn’t dishonestly creating a debt for John to pay.

Clearly if John discloses his private key (or its stolen) then he will make the system insecure, but this is a problem with John and his security protocols, not with public-key cryptography.

## Create and maintain an accurate list of transactions

So far we’ve seen how 1 IOU (for an orange) can be securely created, signed and verified. This process can extended to be used by more people to exchange more fruit. For example.

The original note:

From: JohnDate: 1234, To: Lizzie, What: 1 Orange <- Signed and encrypted by John using his private key

Then some additional transactions:

From: Lizzie // Date: 1235, To: John, What: 2 Apples <- Signed and encrypted by Lizzie using her private keyFrom: John // Date: 1236, To: Chris, What: 1 Banana <- Signed and encrypted by John using his private keyFrom: Chris // Date: 1237, To: Lizzie, What: 2 Bananas <- Signed and encrypted by Chris using his private key

After these 4 transactions, between John, Chris and Lizzie:

- John owes 1 orange to Lizzie and 1 banana to Chris
- Lizzie owes 2 apples to John
- Chris owes 2 bananas to Lizzie.

This is confusing, (and ridiculous). It is not possible to know who is the most in debt or who is the most wealthy. Lizzie owes 2 apples, but is owed 2 bananas and 1 apple. Does that mean her fruit business is losing money or making money? We cannot say. To be able to know we need to use the same unit of value for all the fruits. Lets say that an orange is worth 2 apples, and a banana is also worth 2 apples (therefore 1 banana = 1 orange.), also lets invent a currency called “coins” and say 1 apple is worth 1 coin. The 4 transactions can now be rewritten as:

From: John // Date: 1234, To: Lizzie, What: 2 coins <- Signed and encrypted by John using his private keyFrom: Lizzie // Date: 1235, To: John, What: 2 coins <- Signed and encrypted by Lizzie using her private keyFrom: John // Date: 1236, To: Chris, What: 2 coins <- Signed and encrypted by John using his private keyFrom: Chris // Date: 1237, To: Lizzie, What: 4 coins <- Signed and encrypted by Chris using his private key

By going through the list of transactions we can see that:

- John owes Lizzie and Chris 2 coins each, and is owed 2 coins from Lizzie. His net amount is -2
- Lizzie owes John 2 coins but is owed 4 coins from Chris. Her net amount is +2
- Chris owes Lizzie 4 coins but is owed 2 coins from John. His net amount is -2

So far Lizzie is the only person who appears to have any business skills.

What if Lizzie wanted to use the 4 coins that she is owed by Chris to buy something from John? Could she use this system to transfer Chris’ promise to pay her 4 coins so that Chris would pay John instead? The fact that everyone can be sure that the record of the transactions is accurate and authentic allows a debt to be used as payment. Lizzie’s transaction would look like this:

From: Lizzie // Date: 1235, To: John, What: ba781... <- Signed and encrypted by Lizzie using her private key

The “What” section contains a [hash](http://www.movable-type.co.uk/scripts/sha256.html) of the original transaction (with Chris) that she wants to transfer to John. A hash is the signature for a file or some text and in this case it is the signature for Lizzie’s transaction with Chris. The signature is unique to each transaction and identifies which transaction is being used as payment. Because both transactions are signed using Lizzie’s private key, it is simple to verify that Lizzie has the right to use this previous transaction where she is owed (or paid) some coins as payment to another person.

This shows how public-private key infrastructure can be used to securely record transactions and enable trade between a group of people, - under certain conditions. Blockchains can be used to transfer units of value like in this example, but we could just as easily put selfies or certificates of ownership (for houses, financial instruments, diamonds, etc) inside the “What” part of the transaction. If we make two other changes - removing the “To” part of the transaction, and including a hash of the transaction as part of the text which is signed using a private key. If we do this, then a record would be:

From: Chris // Date: 2345, What: "A photo of me" <- Signed and encrypted by Chris using his private key

This would create a reliable record of what Chris claims he looks like. He can confidently send anyone this record and if they have his public key then they can verify that it is Chris himself who signed it and is asserting that the photo is him. If somebody changed the photo then the data in the transaction would change and the transaction will have a new hash value. The new hash value will not match the hash value contained within the signature, and the text in the signature cannot be changed because it can only be encrypted using Chris’ private key, which only Chris has. Therefore it will be simple to show that someone other than Chris is trying to change the photo.

Another use for public-key cryptography arises if Chris were an employee in a bank, and the “What” contained documents about a customer the bank is providing financial services for. In this scenario, Chris (representing the bank) is effectively confirming the customer’s true identity and documenting the evidence that’s been collected to show that the bank knows who their customer really is. If the transaction included a new section called “Customer ID” (for example) then a database of all customers whose identity checks have been successfully completed can be made. This can be shared with other departments (or banks) easily and immutably. This is the concept behind KYC on a blockchain.

Back to our fruit traders: At the moment a participant is allowed to carry a net negative balance. For this system to work in reality, the creation of “coins” will need to be controlled in order to maintain their value. In the example above, people can freely create “coins” and can also carry negative amounts of “coins”. This would result in the value of a “coin” plummeting. Therefore their creation (and conversion from fruit) must be controlled in a predictable manner.

Our examples so far only include 3 people. If there are a lot of people in the network it wouldn’t be feasible to insist that everyone is present or online each time a new transaction is added to the list (the chain) of transactions. However if we allow transactions to be added whilst some people are offline we create an opportunity for fraud. The reasons why, and the solution to this and other problems will be described in part 2.

Thanks for reading! If you'd like to know when I publish something new, please [subscribe!](http://johnmathews.eu/pages/subscribe)

- Previous:  [London Rent vs. London Salaries](http://johnmathews.eu/london.html)

- [9 comments]()
- [**johnmathews**](https://disqus.com/home/forums/johnmathews/)
- [Login](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend5](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
- [⤤Share](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

![Avatar](../_resources/7b2fde640943965cc88df0cdee365907.png)
Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/7cc658e1d604235d3633e824e66ca01f.jpg)](https://disqus.com/by/QWAK/)

[QWAK](https://disqus.com/by/QWAK/)•[a day ago](http://johnmathews.eu/blockchain-introduction.html#comment-3327661472)

""Signed by John" <- John encrypts this line using his private key"

John has to sign whole message - not just one line. Otherwise, forgery is still possible (just copy encrypted, constant line) to a new transaction.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/mthwsjc/)

[John Mathews](https://disqus.com/by/mthwsjc/)Mod[*>* QWAK](http://johnmathews.eu/blockchain-introduction.html#comment-3327661472)•[11 hours ago](http://johnmathews.eu/blockchain-introduction.html#comment-3328430425)

Corrected. Thank you!

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/mthwsjc/)

[John Mathews](https://disqus.com/by/mthwsjc/)Mod[*>* QWAK](http://johnmathews.eu/blockchain-introduction.html#comment-3327661472)•[a day ago](http://johnmathews.eu/blockchain-introduction.html#comment-3327737393)

Ooh, Thanks I will make a correction.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/72d8e9364d01e70ab308d25a0d642add.jpg)](https://disqus.com/by/disqus_U8gvk34xQD/)

[Clay Ferguson](https://disqus.com/by/disqus_U8gvk34xQD/)•[a day ago](http://johnmathews.eu/blockchain-introduction.html#comment-3327669344)

Great intro to explain blockchain. Thanks for posting this!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/3aa10c2ab0e033c4d9e8981dc764d034.jpg)](https://disqus.com/by/vizaysoni/)

[Vizay Soni](https://disqus.com/by/vizaysoni/)•[a day ago](http://johnmathews.eu/blockchain-introduction.html#comment-3327621319)

Very good intro. to blockchain, Thanks.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/dc627cc9a01aa656f458fb9ae70fe26a.jpg)](https://disqus.com/by/tonymountifield/)

[Tony Mountifield](https://disqus.com/by/tonymountifield/)•[5 hours ago](http://johnmathews.eu/blockchain-introduction.html#comment-3328767823)

Very interesting and a good intro. I understand PKC, but never got a handle on blockchain. Couple of questions.

1. What is KYC? You mention it without saying.

2. When you describe Lizzie using Chris's promise to pay John, it says "because both transactions are signed with Lizzie's private key", but it says further up that the promise was signed by Chris. Am I missing a step?

Btw, I recognised all the names except Walter!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/kushankpoddar/)

[Kushank Poddar](https://disqus.com/by/kushankpoddar/)•[13 hours ago](http://johnmathews.eu/blockchain-introduction.html#comment-3328365796)

Succinctly explained, thanks John!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/charles_muzonzini/)

[Charles Muzonzini](https://disqus.com/by/charles_muzonzini/)•[14 hours ago](http://johnmathews.eu/blockchain-introduction.html#comment-3328337966)

Great explanation, thanks!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/chris_derose/)

[Chris DeRose](https://disqus.com/by/chris_derose/)•[a day ago](http://johnmathews.eu/blockchain-introduction.html#comment-3327918706)

this is absurd. Where is the great scandal whereby someone doesn't trust themself with their own data in a way that logging and backups doesn't solve better? Why do you even need a block, because it's a 'folder'?

## Also on **johnmathews**

- [ ### Encryption       - 1 comment•      - 2 months ago•](http://disq.us/url?url=http%3A%2F%2Fjohnmathews.eu%2Fencryption.html%3AHKTC0sSDxAxOHsRp4E4d42cJq7I&imp=5hrl1902ck1n8q&prev_imp=5hrkho4hilktk&forum_id=5055125&forum=johnmathews&thread_id=5855678706&thread=5678264752&zone=thread&area=bottom&object_type=thread&object_id=5678264752)[Tony Mountifield— "Factoring prime numbers is a super famous mathematical problem, it was studied by Eratosthenes 3 in the 3rd century BC and more …](http://disq.us/url?url=http%3A%2F%2Fjohnmathews.eu%2Fencryption.html%3AHKTC0sSDxAxOHsRp4E4d42cJq7I&imp=5hrl1902ck1n8q&prev_imp=5hrkho4hilktk&forum_id=5055125&forum=johnmathews&thread_id=5855678706&thread=5678264752&zone=thread&area=bottom&object_type=thread&object_id=5678264752)
- [ ### London Rent vs. London Salaries       - 6 comments•      - 15 days ago•](http://disq.us/url?url=http%3A%2F%2Fjohnmathews.eu%2Flondon.html%3A5-fnvSfuo8pA_PZInyaQ90l8Wqs&imp=5hrl1902ck1n8q&prev_imp=5hrkho4hilktk&forum_id=5055125&forum=johnmathews&thread_id=5855678706&thread=5814564455&zone=thread&area=bottom&object_type=thread&object_id=5814564455)[David Howe— In Canada 15-20 years ago you were able to do no down payment option with your mortgage guaranteed by a Federal Housing Agency, CMHC. …](http://disq.us/url?url=http%3A%2F%2Fjohnmathews.eu%2Flondon.html%3A5-fnvSfuo8pA_PZInyaQ90l8Wqs&imp=5hrl1902ck1n8q&prev_imp=5hrkho4hilktk&forum_id=5055125&forum=johnmathews&thread_id=5855678706&thread=5814564455&zone=thread&area=bottom&object_type=thread&object_id=5814564455)
- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=johnmathews&t_i=blockchain-introduction.html&t_u=http%3A%2F%2Fjohnmathews.eu%2Fblockchain-introduction.html&t_d=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&t_t=%20Blockchains%20from%20the%20ground%20up%3A%20Part%C2%A01%20&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=johnmathews&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)