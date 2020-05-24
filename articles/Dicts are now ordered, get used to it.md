Dicts are now ordered, get used to it

# Dicts are now ordered, get used to it

 [Ivan Sagalaev](https://softwaremaniacs.org/), February 2020

There were several moments over the last few weeks when I heard people discuss differences between Python [lists](https://docs.python.org/3/library/stdtypes.html#list) and [dicts](https://docs.python.org/3/library/stdtypes.html#dict) and one of the first ones mentioned was that lists are ordered and dicts are not.

Well, not anymore. Quoting the docs referenced above:

> Changed in version 3.7: Dictionary order is guaranteed to be insertion order. This behavior was an implementation detail of CPython from 3.6.

So if you want to discuss *fundamental* differences you can pretty much only point out that dict values are accessible by keys, which could be of any immutable type, while list values are indexed with integers. That's it :-)

## How and why

A plain hash table holds both keys and values in a pseudo random order determined by hashes calculated from keys. It is also sparse, with unoccupied holes in a pre-allocated array:

![](../_resources/0742548d00ce2a809ef09ee902a12fe4.png)

Since version 3.6 CPython holds keys and values in a separate dense array, while the hash table itself only holds *indexes* into that:

![](../_resources/affa3f0c24416d9964be6f02530583cf.png)

Since the entries array is populated sequentially, it naturally ensures the order.

As far as I know the initial reason for this change was saving space by sharing hash tables of multiple dicts with the same set of keys (which in Python means instances of the same class, for example). I don't know the exact politics of how this useful property progressed from an implementation detail to a guaranteed behavior.

## dict[int] vs. list

Does it mean that a dict with int keys is the same as list? There's still a few practical differences.

One obvious difference is the API. You'd have to always mention indexes explicitly when working with a dict[int], there's no such thing as `.append(value)` or `.pop()` with no argument. Frankly, I can't see any point in trying to make it work :-)

Also, dicts are bigger, by an order of magnitude:

	In [79]: getsizeof(['' for i in range(100000)])
	Out[79]: 824472

	In [80]: getsizeof({i: '' for i in range(100000)})
	Out[80]: 5242984

Surprisingly, I couldn't find any consistent difference in speed in neither insertion of new values in a list and a dict[int], nor in traversing them. My gut feeling tells me it's mostly due to the fact that a hash value of an int is the int itself, so there's no time wasted on hashing.

## Not sets though!

Yep, to my surprise sets are still unordered:

	In [3]: list({'one': True, 'two': True, 'three': True, 'four': True, 'five': True})
	Out[3]: ['one', 'two', 'three', 'four', 'five']

	In [4]: list({'one', 'two', 'three', 'four', 'five'})
	Out[4]: ['three', 'five', 'four', 'one', 'two']

Until this moment I thought of sets as basically thin wrappers around actual dicts operating on their keys and neglecting values. Turns out, they have their own implementation.

##  Comments: 27 (noteworthy: 3)

1.      Mitya

   Interesting! So it brings Python on par with PHP.

PHP (and Facebook Hack) is the only language I was aware of that has the ordered maps/dicts in the standard container toolkit.

When I was exposed to Hack, my initial instincts were not to rely on this feature, but when I got used to it I actually started to appreciate it. This helped to improve my code quite a few times!

Does any other popular language have that?

2.      Alyssa

   Mitya, Ruby has had ordered dicts for quite a while too.

3.      Steve
 Noteworthy comment
   There is a great talk on this topic: https://youtu.be/p33CVV29OG8

4.      Jonathan Hartley

   Python has had ordered dicts for a long time (in "containers.ordereddict" I think). The change described above, in Python 3.6 (from 2016) merely extends that "ordered" behavior to regular dicts as well.

5.      hoistbypetard

   Mitya: C++ `std::map` is ordered. If you want one that's unordered you have to use `std::unordered_map`. C# has OrderedDictionary. Java has SortedMap.

It's not uncommon.

6.      Ivan Sagalaev

   @hoistbypetard as far as I know, `std::map` is ordered by keys, not by insertion order. It probably doesn't matter often in practice, but still is something that's good to know!

7.      hoistbypetard

   @Ivan Sagalaev: That matches my recollection. I glossed over the "insertion order" part. Probably because that's never been important to me, where consistent ordering is sometimes important (or at least useful).

Nice analysis overall, btw.

8.      Ruslan Keba

   Welcome back to blogging! Nice to read you.

9.      Ivan Sagalaev

   @Ruslan Keba thanks! :-) I'm not promising anything though, last year I managed 2 posts overall. I have way too many drafts sitting in my queue.

10.      Eric

   Brandon Rhodes gave a good talk at PyCon 2017 about the evolution of Python dictionaries: https://www.youtube.com/watch?v=66P5FMkWoVU.

11.      Great commenting interface.

   Just testing, sorry. This is a good interface, the **markdown is nice**. How do you deal with spam (like mine)? I would love to have something like this for my blog. Also, are the commends db-backed, or do you do some static-site generation stuff with it?

12.      Austin

   @hoistbypetard In java you have LinkedHashMap to keep insertion order. SortedMap is used to order by the actual key itself.

13.      Mauro

   I think sets in Python will never be ordered due to the fact that while

	>>> list([1,2,3]) == list([1,3,2])
	False

	>>> set([1,2,3]) == set([1,3,2])
	True

that is, it must conform to the mathematical definition of equal sets:

> A set A is said to be equal to set B if both sets have the same elements or members of the sets. The order of elements in both sets is irrelevant.

14.      Andrej Shadura

   Tcl has ordered dicts by default as well.

15.      Raindeer

   One application where ordered dicts are really useful is when parsing JSON files. If you want read a JSON file, edit something and then write it back, ordered dicts ensure that the object attributes in the edited file are in the same order as in the original file.

16.      Arkadi Klepatch
 Noteworthy comment

   @hoistbypetard @Ivan Sagalaev C++ std::map is a tree, not a hash table. So order by key comes naturally. Entirely different data structure.

17.      Ama Aje My Fren

   There may be no `.pop()` but there is a `.popitem()` which does the same in guaranteed LIFO from Python 3.7.

18.      22

   [JavaScript Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) are also sorted in insertion order.

19.      Anonymous

   Mitya, in Tcl dictionaries have been ordered from the start. They are also immutable, something I wish was the default in other scripting languages.

20.      Somebody Somewhere

   @hoistbypetard std::map is ordered by value of the key and kept in insertion order. E.g. If you insert the following key/value pairs (in order left to right): {3, "three"}, {1, "one"}, {2, "two"}.

- std::map key order: { 1, 2, 3}
- Python 3.7 dict key order: {3, 1, 2}

21.      Ivan Sagalaev

> Just testing, sorry. This is a good interface, the markdown is nice. How do you deal with spam (like mine)? I would love to have something like this for my blog. Also, are the commends db-backed, or do you do some static-site generation stuff with it?

I deal with spam by manually approving all comments :-) There was a more complicated system in place at one point, but it relied on other services (Akismet) and was brittle than I wanted it. So I eventually simplified everything since my blog doesn't get a lot of traffic these days.

Also yes, it's a custom DB-backed software. [Write me](https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/mailto:maniac@softwaremaniacs.org) an email if you like more details!

22.      Alex Ambrioso

   Thanks for the nice article!
You wrote: Yep, to my surprise sets are still unordered!

I just want to point out that it is should not be a surprise that the set type is still unordered. The behavior of the set type is based on the mathematical idea that two sets are equivalent if they have the same elements. I suspect that the basic set type characteristics will never change.

23.      Alex

   I just noticed Mauro made the same point I did a few comments back. He included a definition of set that makes the point mor clearly than I did.

24.      Joseph Giralt

   Mitya, Ruby has had ordered hashes as the default since 2013.

25.      Babush

> The order of elements in both sets is irrelevant.

Well yes. Let's draw the correct conclusion from this. Sets can be ordered by an implementation, while raising no conflict with the mathematical definition. Perhaps you had in mind the equality operator with sets. Yes, the behavior of that operator should not change: set(1,2,3) should be equal to set(1,3,2) and also to set(3,1,2) etc. Were a language or library to dish the set elements out in a certain order, that would not change this rule. The ordering can be fixed, or random; either way, we still mathematically have a set.

26.      Joseph Giralt

   whoops, i take that back, since 2007. https://www.ruby-lang.org/en/news/2007/12/25/ruby-1-9-0-released/

27.      re:fi.64
 Noteworthy comment
   You can read the discussions at these two threads:

https://mail.python.org/pipermail/python-dev/2017-November/150142.htmlhttps://mail.python.org/pipermail/python-dev/2017-December/151263.html

## Add comment

 Name

 Text (format with Markdown)