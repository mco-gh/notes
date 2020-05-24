Damn Cool Algorithms: Log structured storage - Nick's Blog

Damn Cool Algorithms: Log structured storage - Nick's Blog
![](../_resources/b12f8b3e5a2cb8b8b1faaaef0982bb10.png)

[](../_resources/6dac4c4508b28ced2666d63b4f4caf64.bin)http://blog.notdot.net/2009/12/Damn-Cool-Algorithms-Log-structured-storage

Damn Cool Algorithms: Log structured storage Posted by Nick Johnson | Filed under tech , damn-cool-algorithms Typically, if you're designing a storage system - such as a filesystem, or a database - one of your major concerns is how to store the data on disk. You have to take care of allocating space for the objects to be stored, as well as storing the indexing data; you have to worry about what happens when you want to extend an existing object (eg, appending to a file), and you have to take care of fragmentation, which happens when old objects are deleted, and new ones take their place. All of this adds up to a lot of complexity, and the solutions are often buggy or inefficient.