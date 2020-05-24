Virtual Lorenz

## What was the Lorenz SZ and how did it work?

The Lorenz SZ40, SZ42A and SZ24B were a range of teleprinter cipher attachment machines developed by C. Lorenz AG in Berlin during World War II. The SZ model name is from the German "Schlüssel-Zusatz" which means cipher attachment.

The Enigma cipher machine was portable enough for front line troops but it required two operators each end of the link - one to encipher the message one letter at a time and another to transmit it via Morse code. What was required by the German high command was something faster and even more secure to transmit messages directly between Berlin and the front line generals and this is what Lorenz built

##

###

[Lorenz: Hitler's "Unbreakable" Cipher Machine](https://www.youtube.com/watch?v=GBsfWSQVtYA)

[  Fishy Codes: Bletchley's Other Secret - Computerphile  Computerphile • 82K views  15:57](https://www.youtube.com/watch?v=Ou_9ntYRzzw)[  158,962,555,217,826,360,000 (Enigma Machine) - Numberphile  Numberphile • 2.8M views  11:52](https://www.youtube.com/watch?v=G2_Q9FoD-oQ)[  Lorenz, Colossus and the Dream of a Universal Machine for Cryptanalysis  tnmoc • 2.4K views  36:41](https://www.youtube.com/watch?v=VnzjPmNDom4)[  Flaw in the Enigma Code - Numberphile  Numberphile • 2M views  10:59](https://www.youtube.com/watch?v=V4V2bpZlqx8)[  Top 10 Unbreakable Ciphers and Codes — TopTenzNet  TopTenz • 77K views  10:49](https://www.youtube.com/watch?v=xtRaZR-dPwQ)[  25 Famously Unsolved Ciphers And Codes That You Won't Be Able To Break  list25 • 195K views  7:15](https://www.youtube.com/watch?v=RVYtxrm9yRA)[  Greatest Mysteries of World War 2 Hitler's Engima  TheNaziGermany1945 • 311K views  1:49:23](https://www.youtube.com/watch?v=y_BL0M08-B4)[  The Enigma Code  UCDavis • 263K views  1:05:16](https://www.youtube.com/watch?v=ncL2Fl6prH8)[  Colossus at 70  tnmoc • 19K views  51:08](https://www.youtube.com/watch?v=QcaHpvznC7g)[  Bletchley Park Tour [docu in full]  PA3DMI • 84K views  1:13:52](https://www.youtube.com/watch?v=OuEHcJ7CCzg)[  Encryption and HUGE numbers - Numberphile  Numberphile • 842K views  9:22](https://www.youtube.com/watch?v=M7kEpw1tn50)

1:08 / 11:42
[(L)](https://www.youtube.com/watch?v=GBsfWSQVtYA)

**Dr James Grime introduces the Lorenz**

To understand what the Lorenz machine did, we need to go back to understand how a teleprinter machine works.

### Teleprinters and the Baudot Code

The teleprinter was already in use pre-war and used the Baudot code (also called the Baudot-Murray Code), which was invented by Émile Baudot in 1870 and altered by Donald Murray in 1901 for use with teleprinters. This was a way of sending electrical impulses to represent letters of the alphabet. Each letter can be represented by a 5-bit code of impulses or their absence. This signal can be encoded onto a punched paper tape as a series of holes or no-holes where an impulse was required. At Bletchley Park, they would record these impulses as either an X for a hole or a . for a no-hole character.

![Tpcode.gif](../_resources/f05ed3a671fabe1253884d044b67fc27.gif)

This gave a total of 32 symbols available which is not enough to encode the alphabet and numbers together so there were a number of control codes available. There were two special control codes to switch between letter and figure modes. Therefore depending on the last control code sent, the signal **x·····** could either be E or 3.

### The Vernam cipher

In 1918, Gilbert Vernam in America, invented a way of encoding teleprinter information by adding a random string of letters to the text using modulo-2 (the same as XOR). This meant that adding the same set of letters a second time would return the cipher string back to it's original format.

| Adding | Result |
| --- | --- |
| X   | +   | X   | =   | ·   |
| ·   | +   | ·   | =   | ·   |
| ·   | +   | X   | =   | X   |
| X   | +   | ·   | =   | X   |

To add two characters in modulo-2, take each of the 5 impulses for that character and use the following rules: If the symbols are the same, return ., if they are different, return x

#### Example encoding letter "A" then decoding using a fixed key letter "S"

| Letter | Impulses |
| --- | --- |
| A   | X   | X   | ·   | ·   | ·   |
| S   | X   | ·   | X   | ·   | ·   |
| ?   | ·   | X   | X   | ·   | ·   |

**Enciphered Letter ? = I**

| Letter | Impulses |
| --- | --- |
| I   | ·   | X   | X   | ·   | ·   |
| S   | X   | ·   | X   | ·   | ·   |
| ?   | X   | X   | ·   | ·   | ·   |

**Deciphered letter ? = A**

Vernam proposed having pre-prepared random strings of characters available each of which would be used up one at a time and discarded as your message was encoded. Your receiving party would have the same set of characters available as well and when added to the enciphered message would give the original plain text message. Used correctly in this way (a one-time pad system) would make the message unbreakable.

### The Lorenz method

Lorenz decided to use the Vernam method to encode their teleprinter signals, but especially in a war situation, there was a difficult problem that to ensure each end of the link had the same set of random encoded tapes available would have been practically impossible so they decided to create a machine which would generate a random sequence of characters and add that to the message being sent. As long as the receiving end had a similar machine and could set the same start point, the same set of generated characters woudld be added to the message, revealing the message

Each obscuring character would be generated by a set of five rotating wheels which either add a · or X for each of the 5 impulses. Each letter of the plaintext entered would move the five wheels on one setting changing the next obscuring character.

To make sure that the random generated string of characters did not repeat too often, it was decided to have two sets of wheels so it is essentially adding two seperate letters to the initial letter to get the final cipher character to send. Finally, to enable even more differences to the mix, two seperate motor wheels were added which changed how often the second character wheels turned.

At Bletchley Park, one set of 5 wheels were called the Chi (or X) wheels which all moved together for each character encoded, the other set were called the Psi (or ψ) wheels which moved in a staggered motion dependant on the result of the final two motor (Mu or μ) wheels. One motor wheel turned each character, the second moved only when the first wheel had an X result and the result of this told the Psi wheels when to turn.

![](../_resources/336fc8e6ec488c3bbf1124ccd85ffaa9.jpg)

This means the number of possible ways of setting the wheels without even touching the pins is the product of the number of positions for all wheels which is 43 × 47 × 51 × 53 × 59 × 37 × 61 × 41 × 31 × 29 × 26 × 23 = 1.6034 × 1019 while taking into account the pin settings too makes a total of 1.0 x 10170 which is more combinations than there are particles in the universe.