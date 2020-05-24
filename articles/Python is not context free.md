Python is not context free

Python is not context free
October 10, 2012  [∞](http://trevorjim.com/python-is-not-context-free/)

I’ve [mentioned](http://trevorjim.com/parsing-not-solved/) that most programming languages are not context-free languages. Let’s take[Python](http://python.org/) as a first example.

The standard way to show that a language is not context free is to use[Ogden’s Lemma](http://en.wikipedia.org/wiki/Ogden%27s_lemma). I won’t bother to do so here. It’s pretty obvious that most programming languages are not context free if you consider them as languages over sequences of *characters*. It is more typical to consider them as languages over sequences of *tokens*:

![](../_resources/210fe8c71c870caa8989e1ec5bc72d3e.png)

The diagram above shows the usual two-stage process for parsing a programming language: a lexer transforms a sequence of characters into a sequence of tokens that is fed into a parser. We can then ask whether the language of tokens accepted by the parser is context free.

The problem with this is that nothing is said about the power of the lexer. If the lexer is arbitrarily powerful, it can effectively do all of the parsing, and emit a complete, unambiguous parse tree as a sequence of tokens. This can be an interesting and useful technique (I have [used it myself](http://trevorjim.com/papers/ldta-2011.pdf)), but it makes applying Ogden’s Lemma to the parser component a useless exercise.

Let’s see how this plays out for Python. The interesting thing about Python’s syntax is, of course, its use of indentation to indicate program structure.

for i in x:
for j in y:
print j
print i
print

Here the indentation indicates that `print i` belongs to the body of the inner for loop, while the final `print` belongs to the body of the outer loop. Notice that the indentation of the final`print` has to line up with the indentation of the third previous line—clearly this is a context-sensitive feature. Furthermore, a typical lexer will strip all whitespace from the token stream, so the parser never sees it. Something unusual must be going on in Python’s parser and lexer.

There is an additional complication: Python [ignores indentation inside parentheses, square brackets and curly braces](http://docs.python.org/reference/lexical_analysis.html#implicit-line-joining).

I can see two obvious ways to handle this.

### Handle everything in the lexer

In the official Python implementation, the lexer keeps track of indentation by treating whitespace containing newlines specially. If it sees increased indentation it issues a special INDENT token. If it sees decreased indentation it issues a DEDENT token. If the indentation is the same, it issues a NEWLINE token. The lexer keeps a stack of indentation levels that it pushes and pops as indentation changes. Moreover, the lexer keeps track of the nesting level of parentheses, square brackets, and curly braces so that it can omit NEWLINE, INDENT, and DEDENT tokens as necessary. Given this lexer, the parser is a context-free, LL(2) parser (see [here](http://www.antlr.org/grammar/1200715779785/Python.g)).

In this case, although the parser component is a context-free parser, I don’t think that is sufficient to call Python a context-free language. The lexer is too powerful.

A typical lexer is based on first-match, longest-match regular expressions. It is a finite state machine plus a single counter (holding the index in the input of the longest match so far).

The Python lexer keeps, in addition, a *stack* of counters for the indentation levels. Moreover, it keeps track of the nesting of parentheses; and the language of balanced parentheses is *the*canonical non-regular, context-free language! So in this design, there is no clear separation of the context-free part and the context-sensitive part, and the context-sensitive part goes well beyond what a typical lexer can do.

### Lexical feedback

A second way of handling Python’s indentation is to use *lexical feedback*. Instead of using the usual lexer-parser setup seen above, we add a feedback loop from the parser to the lexer:

![](../_resources/7225208ed80d6ac2db9ebb33ccdf62f8.png)

The feedback is used by the parser to tell the lexer the nesting level of parentheses; the lexer can then handle the indentation just as in the last strategy.

The advantage of this approach is that the nesting of parentheses is tracked in only one place, the parser, while in the previous approach both the lexer and parser tracked nesting.

I think, however, that this approach makes it even more obvious that the context-free part of parsing and the context-sensitive part are intertwined. That makes the language context sensitive, in my opinion.

### So what?

Does it matter that Python is not context free, given that we have a relatively nice parser for it?

Yes, it does matter, because Python is just one of many examples.*Most* languages of interest are context sensitive, and yet we are trying to use inappropriate tools (context-free grammars and context-free parser generators) to specify and parse them. This leads to bad specifications and bad implementations.

[← Newer](http://trevorjim.com/haskell-is-not-context-free/)
[Older →](http://trevorjim.com/parsing-not-solved/)

[research](http://trevorjim.com/research)   [papers](http://trevorjim.com/papers)   [projects](http://trevorjim.com/projects)   [archived posts](http://trevorjim.com/archive)