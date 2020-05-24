Paxos made simple – the morning paper

# Paxos made simple

[March 4, 2015](https://blog.acolyer.org/2015/03/04/paxos-made-simple/) ~ [adriancolyer](https://blog.acolyer.org/author/adriancolyer/)

[Paxos made simple](http://research.microsoft.com/en-us/um/people/lamport/pubs/paxos-simple.pdf) – Lamport 2001

This is part 3 of a [10 part series](https://blog.acolyer.org/2015/03/01/cant-we-all-just-agree/) on consenus.

Yesterday we looked at [The Part-Time Parliament](https://blog.acolyer.org/2015/03/03/the-part-time-parliament/), Lamport’s first paper introducing the Paxos algorithm, which takes an allegorical form. In today’s choice, Lamport abandons the allegory and puts across the Paxos algorithm in plain english.

> ”

>  The Paxos algorithm for implementing a fault-tolerant distributed system has been regarded as difficult to understand, perhaps because the original presentation was Greek to many readers. In fact, it is among the simplest and most obvious of distributed algorithms. At its heart is a consensus algorithm—the “synod” algorithm of > [> The Part-Time Parliament](https://blog.acolyer.org/2015/03/03/the-part-time-parliament/)> .

The structure of the paper is familiar: first Lamport explains the core consensus protocol that enables a set of participants to agree on a value between them; then he shows how a distributed system can be implemented that keeps a set of servers in lock-step by running an instance of the consenus protocol for each decision they take.

At the core of the consensus algorithm is a simple fact that it might be worth dwelling on first. Imagine a set of coins that have all been tossed and are now lying flat on the surface of a table. If a majority of those coins show ‘heads’ then it is impossible for there to be a majority that show ‘tails’ at the same time! We can generalise this to any set *S* with members free to choose some value from *V*. If the majority of members choose some value *v : V*, then it is impossible for there to be a majority agreeing on any value other than *v*. Now let the members of S each choose a new value, and suppose that a majority choose some new value *v’*. At least one of the members in the new majority must also have been a member of the earlier majority. This follows straightforwardly from the definition of majority: if you substract from S the set of members in the original majority there are (by definition) not enough members left to form a majority. Therefore any new majority that does form, must do so by including a member from a previous majority.

### The Consensus Algorithm

> ”

>  Assume a collection of processes that can propose values. A consensus algorithm ensures that a single one among the proposed values is chosen. If no value is proposed, then no value should be chosen. If a value has been chosen, then processes should be able to learn the chosen value. The safety requirements for consensus are:

- Only a value that has been proposed may be chosen,
- Only a single value is chosen, and
- A process never learns that a value has been chosen unless it actually has been.

An asynchronous, non-Byzantine communications model is assumed.

There are three roles to be played in the consensus algorithm: proposer, acceptor, and learner. A single process may play multiple roles.

A *proposal* to agree on some value consists of a *proposal number* and the candidate *value*. Every proposal has a distinct proposal number, but more than one proposal can propose the same value. Agreeing to accept a proposal (proposed value) requires a majority of the acceptors. As we saw earlier, it is impossible to form a subsequent majority without including at least one of the acceptors from an earlier majority.

There is a very clear derivation of the core consensus protocol that shows step-by-step why it needs to be as it is. An outcome of this chain of reasoning is a constraint on the proposal number and proposal value that a proposer may put forward in any new proposal: before issuing a proposal with proposal number

*n*, a proposer must ask a majority of the acceptors for the proposal value of highest numbered proposal Learning about proposals already accepted is easy enough; predicting future acceptances is hard. Instead of trying to predict the future, the proposer controls it by extracting a promise that there won’t be any such acceptances. In other words, the proposer requests that the acceptors not accept any more proposals numbered less than n. .

The combined actions of proposers and acceptors results in the following 2-phase protocol:

### Prepare phase

1. A *proposer* selects a proposal number *n* and sends a *prepare* request with number *n* to a majority of acceptors. “If I make a proposal with number n, are there any constraints on the value I must propose?”

2. If an *acceptor* receives a prepare request with number *n*, where *n* is greater than any of the prepare requests it has already responded to, then it responds with a promise not to accept any more proposals numbered less than *n*, and with the highest numbered proposal (if any) that it has accepted. (Acceptors therefore need to maintain as reliable state the highest numbered proposal they have accepted, and the high watermark value of the largest *n* it has responded to in a prepare request).

[![paxos-prepare.jpg](../_resources/2327ceff3f31a2f6d737c61c37b617ba.jpg)](https://adriancolyer.files.wordpress.com/2015/03/paxos-prepare.jpg)

### Accept phase

Pre-condition: a proposer has received promise responses to its prepare request numbered *n* from a majority of acceptors.

1. The *proposer* sends an *accept* message for proposal *(n,v)*, where *v* is the proposal value of the highest numbered accepted proposal amongst the promise responses, or any value the proposer chooses if no prior acceptances are returned.

2. If an *acceptor* receives an *accept* message for a proposal numbered *n*, it accepts the proposal unless it has already responded to a prepare request with a value higher than *n*. (Several proposals may be circulating concurrently).

[![paxos-accept.jpg](../_resources/0e5c1e1947c4cfc855c048486d9be143.jpg)](https://adriancolyer.files.wordpress.com/2015/03/paxos-accept.jpg)

### Learners

We said that there were three roles: proposer, acceptor, and learner. A *learner* is someone that needs to discover what the proposal ultimately chosen by the majority of acceptors actually is. (Remember that these roles are often combined in a single agent).

> ”

>  The obvious algorithm is to have each acceptor, whenever it accepts a proposal, respond to all learners, sending them the proposal. This allows learners to find out about a chosen value as soon as possible, but it requires each acceptor to respond to each learner—a number of responses equal to the product of the numberof acceptors and the number of learners.

A less reliable model, but one that reduces communication, is to have one or more nominated ‘distinguished learners’ to which acceptors send their acceptance notifications, and these then broadcast to the rest of the learners.

[![paxos-learn.jpg](../_resources/bcadb7539ee113617163cc35c27b18fc.jpg)](https://adriancolyer.files.wordpress.com/2015/03/paxos-learn.jpg)

### Progress

> ”

>  To guarantee progress, a distinguished proposer must be selected as the only one to try issuing proposals. If the distinguished proposer can communicate successfully with a majority of acceptors, and if it uses a proposal with number greater than any already used, then it will succeed in issuing a proposal that is accepted. By abandoning a proposal and trying again if it learns about some request with a higher proposal number, the distinguished proposer will eventually choose a high enough proposal number

### Implementing a Distributed State Machine

So far we’ve looked at a single instance, or *round*, of the consensus protocol. This enables a set of participants to agree on a single value. From this building block we can construct more interesting distributed systems. Let the state at a given node in a distributed system be represented by a sequence of values (or a pure function of such a sequence) – the node is a *state machine*. If each value in the sequence was agreed by every node as a result of a round of the paxos protocol, and the sequencing itself (the order in which they appear) is also agreed, then we a model for achieving consistency amongst a set of nodes in a distributed system. Because there are multiple rounds of the Paxos protocol, this is sometimes called *multi-paxos*.

> ”

>  The Paxos algorithm assumes a network of processes. In its consensus algorithm, each process plays the role of proposer, acceptor, and learner. The algorithm chooses a leader, which plays the roles of the distinguished proposer and the distinguished learner.

Each process (node) is running the same state machine. Since this is deterministic, all servers produce the same sequences of states and outputs if they all execute the same sequence of commands.

> ”

>  To guarantee that all servers execute the same sequence of state machine commands, we implement a sequence of separate instances (rounds) of the Paxos consensus algorithm, the value chosen by the i-th instance (round) being the i-th state machine command in the sequence. Each server plays all the roles (proposer,acceptor, and learner) in each instance of the algorithm.

Clients send commands to the leader, which is responsible for deciding the overall sequence of commands. The selected command is given the next available sequence number, and the leader runs an instance of the Paxos consensus protocol proposing this command as the next ‘value’ to be agreed upon by the participants. Most of the time this will succeed, and the state machines in each participant can advance. Each round of the paxos protocol involves a number of round-trip messages, and the leader does not have to wait for each round to complete before initiating the next one – so long as there are client commands coming in the leader can keep assigning new sequence numbers and initiating rounds. We therefore will often have multiple rounds of consensus algorithm operating in parallel – each reaching agreement on “the command at sequence number *s* is *c*“.

Because any message may be delayed or undelivered, we can end up with gaps in the log / ledger recording the agreed commands. For example, the leader (which could be a newly elected leader if the previous leader has failed) may know the results of rounds 1 through 135, and rounds 138-140, but not yet rounds 136 and 137. At this point the state machine can execute commands up to number 135, but not yet 138-140 because of the missing commands in the sequence. Running phase 1 of the protocol for rounds 136 and 137 will either reveal a ‘highest numbered proposal accepted value’ for these rounds (which the leader then proposes), or that no acceptor accepted any proposal. In the latter case, the leader proceeds by proposing a special ‘no-op’ command which enables the ledger gap to be closed and the subsequent commands in the sequence (138-140) to now be executed.

> ”

>  Since failure of the leader and election of a new one should be rare events, the effective cost of executing a state machine command—that is, of achieving consensus on the command/value—is the cost of executing only phase 2 of the consensus algorithm. It can be shown that phase 2 of the Paxos consensus algorithm has the minimum possible cost of any algorithm for reaching agreement in the presence of faults. Hence, the Paxos algorithm is essentially optimal.

And for the final twist, what if the set of servers involved in these multiple paxos rounds can also change over time? Simple says Lamport! :

> ”

>  If the set of servers can change, then there must be some way of determining what servers implement what instances of the consensus algorithm. The easiest way to do this is through the state machine itself. The current set of servers can be made part of the state and can be changed with ordinary state-machine commands. We can allow a leader to get α commands ahead by letting the set of servers that execute instance i + α of the consensus algorithm be specified by the state after execution of the i-th state machine command. This permits a simple implementation of an arbitrarily sophisticated reconfiguration algorithm.

### Share this:

- [Twitter](https://blog.acolyer.org/2015/03/04/paxos-made-simple/?share=twitter&nb=1)
- [LinkedIn](https://blog.acolyer.org/2015/03/04/paxos-made-simple/?share=linkedin&nb=1)
- [Email](https://blog.acolyer.org/2015/03/04/paxos-made-simple/?share=email&nb=1)
- [Print](https://blog.acolyer.org/2015/03/04/paxos-made-simple/#print)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)

- [![851953365cb281e9ee10896f1e74a2d0](../_resources/0fdcbdc1ecd14d819057c2ce291ccc19.jpg)](https://en.gravatar.com/bendiken)
- [![53334a79d14643ce20353bb21c159edc](../_resources/77943c813ef786f862892d48247010d1.png)](https://en.gravatar.com/pisaruk)
- [![3bfb925deba2d92264357d6ec7c1ab61](../_resources/f20121e1c12785ba960db67f0ac94160.png)](https://en.gravatar.com/dgkim84)
- [![c2c176e9534562a653f6a545e9e85009](../_resources/44b2948a4bf3aa6483eccd06a63d3c37.png)](https://en.gravatar.com/jinhongc)
- [![215b080f9511b6e2d92ecbb4717999b6](../_resources/04b3f67af2fe6241c399b493b52b8869.jpg)](https://en.gravatar.com/slimbouguerra)

[5 bloggers](https://widgets.wp.com/likes/index.html?ver=20190321#) like this.

### *Related*

[Can't we all just agree?](https://blog.acolyer.org/2015/03/01/cant-we-all-just-agree/)In "Consistency"

[Paxos Made Live](https://blog.acolyer.org/2015/03/05/paxos-made-live/)In "Distributed Systems"

[Consensus on Transaction Commit](https://blog.acolyer.org/2016/01/13/consensus-on-transaction-commit/)In "Consistency"

Posted in [Distributed Systems](https://blog.acolyer.org/category/distributed-systems/)[Consistency](https://blog.acolyer.org/tag/consistency/)[Distributed Systems](https://blog.acolyer.org/tag/distributed-systems/)