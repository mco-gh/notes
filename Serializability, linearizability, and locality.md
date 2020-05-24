Serializability, linearizability, and locality

# Serializability, linearizability, and locality

 2016/08/15

- [Software](https://aphyr.com/tags/software)
- [Concurrency](https://aphyr.com/tags/Concurrency)

In Herlihy and Wing’s seminal paper [introducing linearizability](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf), they mention an important advantage of this consistency model:

> Unlike alternative correctness conditions such as sequential consistency [31] or serializability [40], linearizability is a local property: a system is linearizable if each individual object is linearizable.

> Locality is important because it allows concurrent systems to be designed and constructed in a modular fashion; linearizable objects can be implemented, verified, and executed independently. A concurrent system based on a nonlocal correctness property must either rely on a centralized scheduler for all objects, or else satisfy additional constraints placed on objects to ensure that they follow compatible scheduling protocols.

This advantage is not shared by sequential consistency, or its multi-object cousin, serializability. This much, I knew–but Herlihy & Wing go on to mention, almost offhand, that *strict* serializability is also nonlocal!

Recall that strict serializability is essentially serializability plus linearizability’s real-time constraint: transactions cannot be arbitrarily re-ordered, but must appear to take place atomically at some time between their invocation and completion. When we add real-time constraints to sequential consistency, we get linearizability: a local property. Why can’t we add real-time constraints to serializability and obtain locality? Why don’t real-time multi-object transactions compose?

In the time-honored fashion of space-constrained academics, Herlihy and Wing present a beautifully-constructed history, affectionately named H8, as obvious evidence that sequential, serializable, and strict serializability all fail to provide locality. I’ve been staring at this history all morning, and would like to share it with you.

## Subhistories

Consider a FIFO queue x, in which objects are dequeued (deq) in the same order they are enqueued (enq). Two processes, A and B, enqueue and dequeue numbers to and from this queue. Each operation completes immediately, before the next operation begins.

`process  f     queue  value B        enq   x      2 A        enq   x      1 B        deq   x      1`

This history is sequential: we can reorder it to `(A enq x 1) (B enq x 2) (B deq x 1)`, which is a legal execution for a queue, without changing the order of any single process' operations. The same order proves this history is also serializable, if we take each operation as a separate transaction. It is not, however, strict serializable: every operation completed immediately, so we may not reorder them.

What if each process' operations took place in a single transaction: `[(A enq x 1)]`, and `[(B enq x 2) (B deq x 1)]`? These transactions overlap in time, which means a strict serializable system is free to order them either way. [A B] is legal, so *this* system is strict serializable (and therefore serializable as well).

By swapping A with B and 1 with 2, we can construct a second history, on a different queue y, with the same properties:

`process  f     queue  value A        enq   y      1 B        enq   y      2 A        deq   y      2`

So: both of these histories are independently sequential, serializable, and strict serializable, if we choose our transaction boundaries carefully. Now, let us consider their composition.

## Combined history

We can interleave the two histories to produce a single history, in which each key is independently sequential, serializable, and strict serializable (again, given our particular choice of transactions).

`process  f     queue  value A        enq   y      1 B        enq   x      2 A        enq   x      1 B        enq   y      2 A        deq   y      2 B        deq   x      1`

The combined history is no longer sequential. In order for A to (deq y 2), B must (enq y 2) before A begins–since A’s first action is to (enq y 1). Therefore (B enq x 2) also precedes A. Therefore x must begin with 2, which prevents B from dequeuing 1: a contradiction.

If we take each operation as a separate transaction, we can easily construct a serializable history: just move the conflicting enqueues after the dequeues. However, this history is not *strictly* serializable, because immediate returns prevent any reordering.

Curiously, our multi-op transactions from the subhistories satisfy strict serializability, even in the composite history: we can move the single-enqueue transactions to the beginning without violating their real-time order.

`(A enq x 1) (B enq y 2) (A enq y 1) (A deq y 2) (B enq x 2) (B deq x 1)`

However, the system of multiple objects allows us to construct *new* transactions. For instance, each process could perform a single transaction:

`(A enq y 1) (A enq x 1) (A deq y 2) (B enq x 2) (B enq y 2) (B deq x 1)`

There is no way to order these two transactions: A can’t run first, because it needs to dequeue 2, which comes from B–and vice-versa, for B. These transactions do not satisfy serializability.

## Interpretation

We often speak of locality as a property of subhistories for a particular object x: “H|x is strictly serializable, but H is not”. This is a strange thing to say indeed, because the transactions in H *may not meaningfully exist* in H|x. What does it mean to run `[(A enq y 1) (A enq x 1)]` on x alone? If we restrict ourselves to those transactions that *do* apply to a single object, we find that those transactions still serialize in the full history.

So in a sense, locality is about the *scope of legal operations*. If we take single enqueue and dequeue operations over two queues x and y, the space of operations on the *composite* system of x and y is just the union of operations on x and those on y. Linearizability can also encompass transactions, so long as they are restricted to a single system at a time. Our single-key, multi-operation transactions still satisfied strict serializability even in the composite system. However, the space of transactions on a composite system is *more* than the union of transactions on each system independently. It’s their *product*.

We can view strict serializability as linearizability plus the multi-object transactions of serializability. But in another sense, linearizability is strict serializability *with the constraint* that transactions are constrained to act on a single object, *because* that restriction provides locality. That object could be a single register or queue. It could be a set or map. It could be a table in a database, or *an entire database*. The scope of an object determines what operations we can perform when we glue two systems together: every key in a key-value store may be independently linearizable, but we cannot perform a read of two keys *together* in a linearizable fashion.

From an implementer’s perspective, locality is desirable: it means we can have an independent coordinator per system and still have all the systems comprise a linearizable whole. But from a users perspective, I have a hunch that locality is… almost tautological: it’s just the scope of objects you can use together. Just like you can’t glue two strict serializable systems together, you can’t set two linearizable systems side by side and use them together in a linearizable way. As if designing a linearizable system from scratch, we have to sit down, look at our transactions carefully, and prove that our algorithm prevents nonlinearizable histories. Linearizable systems may be “compositional”, but composing them remains nontrivial.

At least, that’s my read on things right now. I’m hoping someone with a better grasp of these papers can put me straight.