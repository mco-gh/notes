https://en.wikipedia.org/wiki/Rope_(data_structure)

> 

# Rope (data structure) - Wikipedia
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Vector_Rope_example.svg/427px-Vector_Rope_example.svg.png)](https://en.wikipedia.org/wiki/File:Vector_Rope_example.svg)

A simple rope built on the string of "Hello\_my\_name\_is\_Simon".

In [computer programming](https://en.wikipedia.org/wiki/Computer_programming "Computer programming"), a **rope**, or **cord**, is a [data structure](https://en.wikipedia.org/wiki/Data_structure "Data structure") composed of smaller [strings](https://en.wikipedia.org/wiki/String_(computer_science) "String (computer science)") that is used to efficiently store and manipulate a very long string. For example, a [text editing](https://en.wikipedia.org/wiki/Text_editing "Text editing") program may use a rope to represent the text being edited, so that operations such as insertion, deletion, and random access can be done efficiently.[\[1\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-Boehm-1)

Description\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=1 "Edit section: Description")\]
-----------------------------------------------------------------------------------------------------------------------------------------

A rope is a [binary tree](https://en.wikipedia.org/wiki/Binary_tree "Binary tree") where each leaf (end node) holds a string and a length (also known as a "weight"), and each node further up the tree holds the sum of the lengths of all the leaves in its left [subtree](https://en.wikipedia.org/wiki/Subtree "Subtree"). A node with two children thus divides the whole string into two parts: the left subtree stores the first part of the string, the right subtree stores the second part of the string, and node's weight is the sum of the left child's weight along with all of the nodes contained in its subtree.

For rope operations, the strings stored in nodes are assumed to be constant [immutable objects](https://en.wikipedia.org/wiki/Immutable_object "Immutable object") in the typical nondestructive case, allowing for some [copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write "Copy-on-write") behavior. Leaf nodes are usually implemented as [basic fixed-length strings](https://en.wikipedia.org/wiki/String_(computer_science) "String (computer science)") with a [reference count](https://en.wikipedia.org/wiki/Reference_counting "Reference counting") attached for deallocation when no longer needed, although other [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science) "Garbage collection (computer science)") methods can be used as well.

Operations\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=2 "Edit section: Operations")\]
---------------------------------------------------------------------------------------------------------------------------------------

In the following definitions, _N_ is the length of the rope.

### Index\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=3 "Edit section: Index")\]

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Vector_Rope_index.svg/427px-Vector_Rope_index.svg.png)](https://en.wikipedia.org/wiki/File:Vector_Rope_index.svg)

Figure 2.1: Example of index lookup on a rope.

_Definition:_ `Index(i)`: return the character at position _i_

_Time complexity:_ ![O(\log N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/14eea297b4387decf341763c39dc038e05744272)

To retrieve the _i_\-th character, we begin a [recursive](https://en.wikipedia.org/wiki/Recursion "Recursion") search from the root node:

function index(RopeNode node, integer i)
  if node.weight <= i and exists(node.right) then
    return index(node.right, i \- node.weight)
  end
  
  if exists(node.left) then
    return index(node.left, i)
  end
  
  return node.string\[i\]
end

For example, to find the character at `i=10` in Figure 2.1 shown on the right, start at the root node (A), find that 22 is greater than 10 and there is a left child, so go to the left child (B). 9 is less than 10, so subtract 9 from 10 (leaving `i=1`) and go to the right child (D). Then because 6 is greater than 1 and there's a left child, go to the left child (G). 2 is greater than 1 and there's a left child, so go to the left child again (J). Finally 2 is greater than 1 but there is no left child, so the character at index 1 of the short string "na", is the answer.

### Concat\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=4 "Edit section: Concat")\]

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Vector_Rope_concat.svg/254px-Vector_Rope_concat.svg.png)](https://en.wikipedia.org/wiki/File:Vector_Rope_concat.svg)

Figure 2.2: Concatenating two child ropes into a single rope.

_Definition:_ `Concat(S1, S2)`: concatenate two ropes, _S_1 and _S_2, into a single rope.

_Time complexity:_ ![O(1)](https://wikimedia.org/api/rest_v1/media/math/render/svg/e66384bc40452c5452f33563fe0e27e803b0cc21) (or ![O(\log N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/14eea297b4387decf341763c39dc038e05744272) time to compute the root weight)

A concatenation can be performed simply by creating a new root node with left = S1 and right = S2, which is constant time. The weight of the parent node is set to the length of the left child _S_1, which would take ![O(\log N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/14eea297b4387decf341763c39dc038e05744272) time, if the tree is balanced.

As most rope operations require balanced trees, the tree may need to be re-balanced after concatenation.

### Split\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=5 "Edit section: Split")\]

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Vector_Rope_split.svg/418px-Vector_Rope_split.svg.png)](https://en.wikipedia.org/wiki/File:Vector_Rope_split.svg)

Figure 2.3: Splitting a rope in half.

_Definition:_ `Split (i, S)`: split the string _S_ into two new strings _S_1 and _S_2, _S_1 = _C_1, …, _Ci_ and _S_2 = _C__i_ + 1, …, _Cm_.

_Time complexity:_ ![O(\log N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/14eea297b4387decf341763c39dc038e05744272)

There are two cases that must be dealt with:

1.  The split point is at the end of a string (i.e. after the last character of a leaf node)
2.  The split point is in the middle of a string.

The second case reduces to the first by splitting the string at the split point to create two new leaf nodes, then creating a new node that is the parent of the two component strings.

For example, to split the 22-character rope pictured in Figure 2.3 into two equal component ropes of length 11, query the 12th character to locate the node _K_ at the bottom level. Remove the link between _K_ and _G_. Go to the parent of _G_ and subtract the weight of _K_ from the weight of _D_. Travel up the tree and remove any right links to subtrees covering characters past position 11, subtracting the weight of _K_ from their parent nodes (only node _D_ and _A_, in this case). Finally, build up the newly orphaned nodes _K_ and _H_ by concatenating them together and creating a new parent _P_ with weight equal to the length of the left node _K_.

As most rope operations require balanced trees, the tree may need to be re-balanced after splitting.

### Insert\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=6 "Edit section: Insert")\]

_Definition:_ `Insert(i, S’)`: insert the string _S’_ beginning at position _i_ in the string _s_, to form a new string _C_1, …, _Ci_, _S'_, _C__i_ + 1, …, _Cm_.

_Time complexity:_ ![O(\log N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/14eea297b4387decf341763c39dc038e05744272).

This operation can be done by a `Split()` and two `Concat()` operations. The cost is the sum of the three.

### Delete\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=7 "Edit section: Delete")\]

_Definition:_ `Delete(i, j)`: delete the substring _Ci_, …, _C__i_ + _j_ − 1, from _s_ to form a new string _C_1, …, _C__i_ − 1, _C__i_ + _j_, …, _Cm_.

_Time complexity:_ ![O(\log N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/14eea297b4387decf341763c39dc038e05744272).

This operation can be done by two `Split()` and one `Concat()` operation. First, split the rope in three, divided by _i_\-th and _i+j_\-th character respectively, which extracts the string to delete in a separate node. Then concatenate the other two nodes.

### Report\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=8 "Edit section: Report")\]

_Definition:_ `Report(i, j)`: output the string _Ci_, …, _C__i_ + _j_ − 1.

_Time complexity:_ ![{\displaystyle O(j+\log N)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/17103234ff8d117128e909c8b62ec4f1a611d83d)

To report the string _Ci_, …, _C__i_ + _j_ − 1, find the node _u_ that contains _Ci_ and `weight(u) >= j`, and then traverse _T_ starting at node _u_. Output _Ci_, …, _C__i_ + _j_ − 1 by doing an [in-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#In-order "Tree traversal") of _T_ starting at node _u_.

Comparison with monolithic arrays\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=9 "Edit section: Comparison with monolithic arrays")\]
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Performance\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_\]

Operation

Rope

String

Index[\[1\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-Boehm-1)

O(log n)

O(1)

Split[\[1\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-Boehm-1)

O(log n)

O(1)

Concatenate (destructive)

O(log n) without rebalancing / O(n) worst case

O(n)

Concatenate (nondestructive)

O(n)

O(n)

Iterate over each character[\[1\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-Boehm-1)

O(n)

O(n)

Insert[\[2\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-:0-2)

O(log n) without rebalancing / O(n) worst case

O(n)

Append[\[2\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-:0-2)

O(log n) without rebalancing / O(n) worst case

O(1) amortized, O(n) worst case

Delete

O(log n)

O(n)

Report

O(j + log n)

O(j)

Build

O(n)

O(n)

Advantages:

*   Ropes enable much faster insertion and deletion of text than monolithic string arrays, on which operations have time complexity O(n).
*   Ropes don't require O(n) extra memory when operated upon (arrays need that for copying operations).
*   Ropes don't require large contiguous memory spaces.
*   If only nondestructive versions of operations are used, rope is a [persistent data structure](https://en.wikipedia.org/wiki/Persistent_data_structure "Persistent data structure"). For the text editing program example, this leads to an easy support for multiple [undo](https://en.wikipedia.org/wiki/Undo "Undo") levels.

Disadvantages:

*   Greater overall space use when not being operated on, mainly to store parent nodes. There is a trade-off between how much of the total memory is such overhead and how long pieces of data are being processed as strings. The strings in example figures above are unrealistically short for modern architectures. The overhead is always O(n), but the constant can be made arbitrarily small.
*   Increase in time to manage the extra storage
*   Increased complexity of source code; greater risk of bugs

This table compares the _algorithmic_ traits of string and rope implementations, not their _raw speed_. Array-based strings have smaller overhead, so (for example) concatenation and split operations are faster on small datasets. However, when array-based strings are used for longer strings, time complexity and memory use for inserting and deleting characters becomes unacceptably large. In contrast, a rope data structure has stable performance regardless of data size. Further, the space complexity for ropes and arrays are both O(n). In summary, ropes are preferable when the data is large and modified often.

See also\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=10 "Edit section: See also")\]
------------------------------------------------------------------------------------------------------------------------------------

*   The [Cedar](https://en.wikipedia.org/wiki/Cedar_(programming_language) "Cedar (programming language)") programming environment, which used ropes "almost since its inception"[\[1\]](https://en.wikipedia.org/wiki/Rope_(data_structure)#cite_note-Boehm-1)
*   The [Model T enfilade](https://en.wikipedia.org/wiki/Enfilade_(Xanadu) "Enfilade (Xanadu)"), a similar data structure from the early 1970s.
*   [Gap buffer](https://en.wikipedia.org/wiki/Gap_buffer "Gap buffer"), a data structure commonly used in text editors that allows efficient insertion and deletion operations clustered near the same location
*   [Piece table](https://en.wikipedia.org/wiki/Piece_table "Piece table"), another data structure commonly used in text editors

References\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=11 "Edit section: References")\]
----------------------------------------------------------------------------------------------------------------------------------------

External links\[[edit](https://en.wikipedia.org/w/index.php?title=Rope_(data_structure)&action=edit&section=12 "Edit section: External links")\]
------------------------------------------------------------------------------------------------------------------------------------------------

*   ["C cords" implementation of ropes within the Boehm Garbage Collector library](https://github.com/ivmai/bdwgc/)
*   [SGI C++ specification for ropes](https://web.archive.org/web/20121225183151/http://www.sgi.com/tech/stl/Rope.html) (supported by STLPort and [libstdc++](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.3/a00223.html))
*   [Ropes](https://github.com/thyer/Ropes) for [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language) "C Sharp (programming language)")
*   [ropes](https://github.com/Ramarren/ropes) for [Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp "Common Lisp")
*   [Ropes for Java](http://ahmadsoft.org/ropes/)
*   [Ropes for JavaScript](https://github.com/component/rope)
*   [Ropes](https://github.com/KenDickey/Limbo-Ropes) for [Limbo](https://en.wikipedia.org/wiki/Limbo_(programming_language) "Limbo (programming language)")
*   [Ropes](https://github.com/Chris00/ocaml-rope) for [OCaml](https://en.wikipedia.org/wiki/OCaml "OCaml")
*   [pyropes](http://sourceforge.net/projects/pyropes/files/?source=navbar) for [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python (programming language)")
*   [Ropes](https://github.com/KenDickey/Cuis-Smalltalk-Ropes) for [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk "Smalltalk")
*   ["Ropey"](https://docs.rs/ropey/1.0.1/ropey/) for [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language) "Rust (programming language)")