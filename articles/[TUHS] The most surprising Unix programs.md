[TUHS] The most surprising Unix programs

# [TUHS] The most surprising Unix programs

 **Doug McIlroy**  [doug at cs.dartmouth.edu](https://minnie.tuhs.org/pipermail/tuhs/2020-March/020664.htmlmailto:tuhs%40minnie.tuhs.org?Subject=Re%3A%20%5BTUHS%5D%20The%20most%20surprising%20Unix%20programs&In-Reply-To=%3C202003132331.02DNVaxN061501%40tahoe.cs.Dartmouth.EDU%3E)

 *Sat Mar 14 09:31:36 AEST 2020*

- Previous message (by thread): [[TUHS] Command options and complexity](https://minnie.tuhs.org/pipermail/tuhs/2020-March/020663.html)

- Next message (by thread): [[TUHS] The most surprising Unix programs](https://minnie.tuhs.org/pipermail/tuhs/2020-March/020665.html)

- **Messages sorted by:**  [[ date ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/date.html#20664)  [[ thread ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/thread.html#20664)  [[ subject ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/subject.html#20664)  [[ author ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/author.html#20664)

* * *

Once in a while a new program really surprises me. Reminiscing a while
ago, I came up with a list of eye-opening Unix gems. Only a couple of
these programs are indispensable or much used. What singles them out is
their originality. I cannot imagine myself inventing any of them.
What programs have struck you similarly?
PDP-7 Unix
The simplicity and power of the system caused me to turn away from big
iron to a tiny machine. It offered the essence of the hierarchical
file system, separate shell, and user-level process control that Multics
had yet to deliver after hundreds of man-years' effort. Unix's lacks
(e.g. record structure in the file system) were as enlightening and
liberating as its novelties (e.g. shell redirection operators).
dc
The math library for Bob Morris's variable-precision desk calculator
used backward error analysis to determine the precision necessary at
each step to attain the user-specified precision of the result. In
my software-components talk at the 1968 NATO conference on software
engineering, I posited measurement-standard routines, which could deliver
results of any desired precision, but did not know how to design one. dc
still has the only such routines I know of.
typo
Typo ordered the words of a text by their similarity to the rest of the
text. Typographic errors like "hte" tended to the front (dissimilar) end
of the list. Bob Morris proudly said it would work as well on Urdu as it
did on English. Although typo didn't help with phonetic misspellings,
it was a godsend for amateur typists, and got plenty of use until the
advent of a much less interesting, but more precise, dictionary-based
spelling checker.
Typo was as surprising inside as it was outside. Its similarity
measure was based on trigram frequencies, which it counted in a 26x26x26
array. The small memory, which had barely room enough for 1-byte counters,
spurred a scheme for squeezing large numbers into small counters. To
avoid overflow, counters were updated probabilistically to maintain an
estimate of the logarithm of the count.
eqn
With the advent of phototypesetting, it became possible, but hideously
tedious, to output classical math notation. Lorinda Cherry set out to
devise a higher-level description language and was soon joined by Brian
Kernighan. Their brilliant stroke was to adapt oral tradition into written
expression, so eqn was remarkably easy to learn. The first of its kind,
eqn has barely been improved upon since.
struct
Brenda Baker undertook her Fortan-to-Ratfor converter against the advice
of her department head--me. I thought it would likely produce an ad hoc
reordering of the orginal, freed of statement numbers, but otherwise no
more readable than a properly indented Fortran program. Brenda proved
me wrong. She discovered that every Fortran program has a canonically
structured form. Programmers preferred the canonicalized form to what
they had originally written.
pascal
The syntax diagnostics from the compiler made by Sue Graham's group at
Berkeley were the mmost helpful I have ever seen--and they were generated
automatically. At a syntax error the compiler would suggest a token that
could be inserted that would allow parsing to proceed further. No attempt
was made to explain what was wrong. The compiler taught me Pascal in
an evening, with no manual at hand.
parts
Hidden inside WWB (writer's workbench), Lorinda Cherry's Parts annotated
English text with parts of speech, based on only a smidgen of English
vocabulary, orthography, and grammar. From Parts markup, WWB inferred
stylometrics such as the prevalance of adjectives, subordinate clauses,
and compound sentences. The Today show picked up on WWB and interviewed
Lorinda about it in the first TV exposure of anything Unix.
egrep
Al Aho expected his deterministic regular-expression recognizer would beat
Ken's classic nondeterministic recognizer. Unfortunately, for single-shot
use on complex regular expressions, Ken's could finish while egrep was
still busy building a deterministic automaton. To finally gain the prize,
Al sidestepped the curse of the automaton's exponentially big state table
by inventing a way to build on the fly only the table entries that are
actually visited during recognition.
crabs
Luca Cardelli's charming meta-program for the Blit window system released
crabs that wandered around in empty screen space nibbling away at the
ever more ragged edges of active windows.
Some common threads
Theory, though invisible on the surface, played a crucial role in the
majority of these programs: typo, dc, struct, pascal, egrep. In fact
much of their surprise lay in the novelty of the application of theory.
Originators of nearly half the list--pascal, struct, parts, eqn--were
women, well beyond women's demographic share of computer science.
Doug McIlroy March, 2020

* * *

- Previous message (by thread): [[TUHS] Command options and complexity](https://minnie.tuhs.org/pipermail/tuhs/2020-March/020663.html)
- Next message (by thread): [[TUHS] The most surprising Unix programs](https://minnie.tuhs.org/pipermail/tuhs/2020-March/020665.html)

- **Messages sorted by:**  [[ date ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/date.html#20664)  [[ thread ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/thread.html#20664)  [[ subject ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/subject.html#20664)  [[ author ]](https://minnie.tuhs.org/pipermail/tuhs/2020-March/author.html#20664)

* * *

[More information about the TUHS mailing list](https://minnie.tuhs.org/cgi-bin/mailman/listinfo/tuhs)