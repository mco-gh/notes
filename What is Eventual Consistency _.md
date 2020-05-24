What is Eventual Consistency ?

### What is Eventual Consistency ?

On this post we're going to talk about Eventual Consistency in the context of lock-free and wait-free data structures, with focus on the C++ memory model, although most (or all) of what we're going to cover also applies to other memory models likes the ones in D, Java , Rust, C11, *<insert language here>*.

If you're looking for an explanation on what Eventual Consistency is in the context of databases then this (may or) may not be what you're looking for!

Before we explain what is eventual consistency in C++, we need to explain a little of what shared memory is and a what is a memory model.

Computers do many things: arithmetic computations, decide different things based on logical expressions, sending and receiving packets, putting pixels on a screen, etc. For this post, we care about reading from main memory and writing to main memory. This means "loads" and "stores".

The whole C++ memory model is about what happens when you do loads and stores from different threads, and all the other stuff that the computer does is pretty much out of the picture.

Obviously, stores are used to store a value in a certain memory location, and loads are used to read a value from a given memory location:

    x.store(value);
    value = x.load();

Also, from the memory model's point of view, all loads are indistinguishable, and so are all stores. CPU vendors have peculiarities, like some stores may re-order but others not (think stores on the same cache line), but the memory model doesn't really care about that, so for this post, we won't care either.

Ok, so this was really important. If you're not convinced that everything is about loads and stores then you better go and read the memory model of your favorite language and then come back.

Let me say it once more: *It's all about loads and stores*.

Combinatorically, if we have two different operations (loads and stores) we can define ordering constraints based on four cases:

**1. A load may not reorder with a subsequent load;
2. A store may not reorder with a subsequent store;
3. A load may not reorder with a subsequent store;
4. A store may not reorder with a subsequent load;**

When none of the four constraints above are set, and if we want to share data among threads or processes (remember, our context is lock-free and wait-free data structures) then in C++ this is called memory_order_relaxed. In this memory ordering any loads can reorder with any stores. Whatever the order of the code you wrote, the compiler may decide to reorder the loads and stores in whatever way it thinks is the best.

This has reduced synchronization and gives a lot of leeway to the compiler, thus resulting in high performance code. The downside is that most lock-free and wait-free algorithms were designed with a specific order in mind, and when this order is not respected, the algorithm no longer works.

To enforce constraint **1**, the first load has to be done with a memory_order_acquire or memory_order_seq_cst. In the C++ memory model, loads with memory_order_acquire can not be reordered with any subsequent load or store. Most of today's CPUs enforce this constraint by default already, which means that it needs no synchronization as well.

To enforce constraint** 2**, the second store has to be done with a memory_order_release or memory_order_seq_cst. In the C++ memory model, stores with a memory_order_release can not be reordered with any previous load or store. CPUs with Total-Store-Order (TSO) like x86, enforce this constraint by default already, which means it needs no explicit synchronization. In practice the CPU internally has synchronization to achieve this strong ordering, but that's out of scope.

To enforce constraint **3**, the first load has to be done with memory_order_acquire or memory_order_seq_cst. x86 CPUs provide this guarantee without explicit synchronization (barriers/fences).

To enforce constraint **4**, both the load and the store have to be memory_order_seq_cst. No practical CPU provides this by default (such a CPU would be too slow) and to have such a constraint requires costly synchronization, typically a *full fence* or at least a *store-load fence*.

Explaining why this requires such high synchronization would require an entire (large) post about this topic, so let's just accept it as it is.

To sum it up, if we want all four constraints, we have to use sequentially consistent memory ordering, while if we want only the first three constraints, then the acquire-release memory ordering is enough.

Notice that stores and loads are done at the *word* level, 64 bits let's say. Therefore, when we talk about sequential consistency we are talking about it at the word level. **Any object bigger than one word and this guarantee disappears** because it will take multiple stores (or multiple loads) to modify (or read) such an object.

So what about eventual consistency?

Roughly speaking, **eventual consistency guarantees if no new updates (stores) are made to a data item (word), then eventually all accesses (loads) to that item (word) will return the last updated value**.

In other words, if we stop doing stores in a certain variable, eventually, when we go and read it from another thread, we will see the last store that was made. Pop quiz: which memory ordering is the weakest that gives this guarantee?

Answer: It's memory_order_relaxed (memory_order_acq_rel and memory_order_seq_cst also provide this guarantee but at a greater cost).

You see, something I didn't say about memory_order_relaxed is that the end result must *look like* the code you wrote, which means that eventually it will have to keep whatever was the last store you wrote in your code. This is highly non-obvious from reading the specs, but that's how it works, otherwise it would let the compiler produce incorrect programs, even in single-threaded code.

Ok, so now that we know that in C++ memory_order_relaxed provides eventual consistency (at the word level), what can we do with that?

Well, the answer to that depends on how useful you think that eventual consistency is.

The term *eventual consistency* is meant as a consistency property of an item, or *object* in C++ parlance. If the object is the size of a word (64 bits or less) then just make it atomic<> and all stores and loads to/from it must be changed to use memory_order_relaxed.

If the object is larger than a word then things start to get more complicated because then we could have concurrent stores touching different words of the object and it would leave it in an inconsistent state. Example below:

struct myobject {

    atomic<uint64_t> a {0};  // Consistency for this object implies that a is equal to b

    atomic<uint64_t> b {0};
}

myobject obj;

Thread 1:
    obj.a.store(1, memory_order_relaxed);
    obj.b.store(1, memory_order_relaxed);

Thread 2:

    obj.a.store(2, memory_order_relaxed);  // May occur before a.store() in thread 1

    obj.b.store(2, memory_order_relaxed);  // May occur after b.store() in thread 1

Thread 3:
    while (true) {
        if (obj.a.load() == obj.b.load()) break; // This may loop forever
    }

In the above example, we defined the object to be consistent when having a and b members equal. The stores with Thread 1 may interleave with the stores in Thread 2, causing the object to be left in a inconsistent state permanently, with a=1 and b=2, which is not *eventually consistent* because the stores on the object have stopped but thread 3 will be in an infinite loop waiting for the object to be consistent.

Even without going into the topic of whether or when is eventual consistency useful, we still have to care about a subtle but extremely important detail in the definition of eventual consistency: **it refers to an object**.

Let me say this again because it's important: **Eventual Consistency requires you to define the item (or object) on where this consistency is being applied**.

This means that what you define to be the object affects the consistency.

Saying that you provide eventual consistency in your application is completely irrelevant unless you define at which *granularity* level you're providing such a guarantee.

If you're providing eventual consistency at the word level, then it's easy to implement, just make all accesses memory_order_relaxed;

If it's eventual consistent at the C++ object level, then each object must itself be atomic<>, which means that the underlying implementation is using a mutual exclusion lock to protect it, thus denying any benefit from doing eventual consistency. You might has well say you're providing strong consistency because you are in fact providing linearizability (at the object level);

In the context of data structures, if we say that a data structure is eventually consistent, it still needs to be atomic itself and all its nodes/whatever constitutes it. This means that the data structure itself needs to be consistent, or atomic. This is extremely hard to achieve without going into a fully linearizable (or at least sequentially consistent) algorithm, so perhaps this is not very useful in practice.

However, if we have multiple data structure instances, even if each of them is linearizable, doing operations or two or more of these data structures is not trivial to make them appear atomic (unless we're protecting everything with a global lock, or using a transactional memory). In such case, we can simply say that we're providing eventual consistency at the data structure level, and it would be correct to say so, because in each data structure instance we provide *atomicity* (linearizable consistency) but across data structure instances we only guarantee that eventually the modifications will be seen over all the instances.

If you take anything away from this post it should be this:

*Eventual Consistency only makes sense when we define what is the "object" where this consistency is being applied.*

Posted by[Pedro Ramalhete](https://www.blogger.com/profile/01340437958052998917)at[11:25 AM](http://concurrencyfreaks.blogspot.com/2017/07/what-is-eventual-consistency.html)

[Email This](https://www.blogger.com/share-post.g?blogID=8231772264325864647&postID=5945375595747378317&target=email)[BlogThis!](https://www.blogger.com/share-post.g?blogID=8231772264325864647&postID=5945375595747378317&target=blog)[Share to Twitter](https://www.blogger.com/share-post.g?blogID=8231772264325864647&postID=5945375595747378317&target=twitter)[Share to Facebook](https://www.blogger.com/share-post.g?blogID=8231772264325864647&postID=5945375595747378317&target=facebook)[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=8231772264325864647&postID=5945375595747378317&target=pinterest)

[(L)](https://plus.google.com/share?app=110&url=http%3A%2F%2Fconcurrencyfreaks.blogspot.com%2F2017%2F07%2Fwhat-is-eventual-consistency.html)

Labels:[C++](http://concurrencyfreaks.blogspot.com/search/label/C%2B%2B),[Eventual Consistency](http://concurrencyfreaks.blogspot.com/search/label/Eventual%20Consistency),[Linearizability](http://concurrencyfreaks.blogspot.com/search/label/Linearizability),[memory model](http://concurrencyfreaks.blogspot.com/search/label/memory%20model),[memory_order_relaxed](http://concurrencyfreaks.blogspot.com/search/label/memory_order_relaxed),[Sequential Consistency](http://concurrencyfreaks.blogspot.com/search/label/Sequential%20Consistency)