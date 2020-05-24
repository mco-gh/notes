Enumerating Trees

Enumerating Trees
![](../_resources/7ebb791ae985e4f67bd381d41cc608c9.png)
https://www.cs.virginia.edu/~lat7h/blog/posts/434.html

Enumerating Trees © 13 Aug 2013 Luther Tychonievich Licensed under Creative Commons: other posts algorithm A one-to-one mapping between binary trees and nat­ural numbers. A binary tree is either empty, or it has two binary trees as chil­dren. Fol­low­ing is a technique for mapping non-neg­a­tive inte­gers to binary trees in an efficient mann­er. To de-interleave a number I write it in binary and cre­ate two numbers from it, one using the odd bits and the other the even bits. For exam­ple, to de-interleave 71 I’d write it in binary as 1000111 then I’d take the odd bits