Paxos By Example » Angus Macdonald

# [Angus Macdonald](https://angus.nyc/)

## A Software Architect in NYC

- [Home](https://angus.nyc/)
- [About](https://angus.nyc/about/)
- [Code](https://angus.nyc/code/)
- [Popular Posts](https://angus.nyc/popular-posts/)

# Paxos By Example

[June 27, 2012](https://angus.nyc/2012/paxos-by-example/)

*This post describes a **decentralized consensus algorithm called Paxos, through a worked example.*

Distributed consensus algorithms are used to enable a set of computers to agree on a single value, such as the *commit* or *rollback* decision typically made using a two- or three-phase commit. It doesn’t matter to the algorithm what this value is, as long as only a single value is ever chosen.

In distributed systems this is hard, because messages between machines can be lost or indefinitely delayed, or the machines themselves can fail.

*Paxos* guarantees that nodes will only ever choose a single value (meaning it guarantees *safety*), but does not guarantee that a value will be chosen if a majority of nodes are unavailable (*progress*).

***General Approach***

A *Paxos* node can take on any or all of three roles: *proposer*, *acceptor*, and *learner*. A *proposer* proposes a value that it wants agreement upon. It does this by sending a proposal containing a value to the set of all *acceptors*, which decide whether to accept the value. Each acceptor chooses a value independently — it may receive multiple proposals, each from a different *proposer* — and sends its decision to *learners*, which determine whether any value has been accepted. For a value to be accepted by *Paxos*, a majority of acceptors must choose the same value. In practice, a single node may take on many or all of these roles, but in the examples in this section each role is run on a separate node, as illustrated below.

[![](../_resources/05afd7ca129ff8373996a57de527db24.gif)](http://angus.nyc/wp-content/uploads/2012/06/0.png)

Figure 1: Basic Paxos architecture. A number of proposers make proposals to acceptors. When an acceptor accepts a value it sends the result to learner nodes.

***Paxos By Example***

In the standard *Paxos* algorithm proposers send two types of messages to acceptors: *prepare* and *accept* requests. In the first stage of this algorithm a proposer sends a *prepare request* to each acceptor containing a proposed value, *v*, and a proposal number, *n*. Each proposer’s proposal number must be a positive, monotonically increasing, unique, natural number, with respect to other proposers’ proposal numbers[[1]](https://angus.nyc/2012/paxos-by-example/#_ftn1).

In the example illustrated below, there are two proposers, both making prepare requests. The request from *proposer A* reaches *acceptors X *and* Y* before the request from *proposer B*, but the request from *proposer B* reaches *acceptor Z* first.

[(L)](http://angus.nyc/wp-content/uploads/2012/06/2.png)

Figure 2: Paxos. Proposers A and B each send prepare requests to every acceptor. In this example proposer A’s request reaches acceptors X and Y first, and proposer B’s request reaches acceptor Z first.

If the acceptor receiving a *prepare*  *request* has not seen another proposal, the acceptor responds with a *prepare response* which promises never to accept another proposal with a lower proposal number. This is illustrated in Figure 3 below, which shows the responses from each acceptor to the first *prepare request* they receive.

[(L)](http://angus.nyc/wp-content/uploads/2012/06/3.png)

Figure 3: Paxos. Each acceptor responds to the first prepare request message that it receives.

Eventually, *acceptor Z* receives *proposer A’s* request[[2]](https://angus.nyc/2012/paxos-by-example/#_ftn2), and *acceptors X* and *Y* receive *proposer B’s* request. If the acceptor has already seen a request with a higher proposal number, the *prepare* request is ignored, as is the case with *proposer A’s* request to *acceptor Z*. If the acceptor has not seen a higher numbered request, it again promises to ignore any requests with lower proposal numbers, and sends back the highest-numbered proposal that it has accepted along with the value of that proposal. This is the case with *proposer B’s* request to *acceptors X* and *Y*, as illustrated below:

[(L)](http://angus.nyc/wp-content/uploads/2012/06/4.png)

Figure 4: Paxos. Acceptor Z ignores proposer A’s request because it has already seen a higher numbered proposal (4 > 2). Acceptors X and Y respond to proposer B’s request with the previous highest request that they acknowledged, and a promise to ignore any lower numbered proposals.

Once a proposer has received *prepare responses* from a majority of acceptors it can issue an *accept request*. Since *proposer A* only received responses indicating that there were no previous proposals, it sends an *accept request* to every acceptor with the same proposal number and value as its initial proposal (*n=2, v=8*). However, these requests are ignored by every acceptor because they have all promised not to accept requests with a proposal number lower than *4 *(in response to the *prepare request* from* proposer B*).

*Proposer B* sends an *accept request* to each acceptor containing the proposal number it previously used (*n=4*) and the value associated with the highest proposal number among the *prepare response* messages it received (*v=8*)[[3]](https://angus.nyc/2012/paxos-by-example/#_ftn3). Note that this is not the value that proposer *B* initially proposed, but the highest value from the *prepare response *messages it saw.

[(L)](http://angus.nyc/wp-content/uploads/2012/06/5.png)

Figure 5: Paxos. Proposer B sends an accept request to each acceptor, with its previous proposal number (4), and the value of the highest numbered proposal it has seen (8, from [n=2, v=8

If an acceptor receives an *accept*  *request* for a higher or equal proposal number than it has already seen, it accepts and sends a notification to every learner node. A value is chosen by the Paxos algorithm when a learner discovers that a majority of acceptors have accepted a value, as is illustrated below:

**[(L)](http://angus.nyc/wp-content/uploads/2012/06/6.png)
**

Once a value has been chosen by Paxos, further communication with other proposers cannot change this value. If another proposer, *proposer C*, sends a *prepare request* with a higher proposal number than has previously been seen, and a different value (for example, *n=6, v=7*), each acceptor responds with the previous highest proposal (*n=4, v=8*). This requires *proposer C* to send an *accept request* containing [n=6, v=8], which only confirms the value that has already been chosen. Furthermore, if some minority of acceptors have not yet chosen a value, this process ensures that they eventually reach consensus on the same value.

Various efficiency improvements to the standard *Paxos* algorithm are discussed in the papers by *Lamport* and *Baker et al.*. For example, a *prepare* request is not necessary if the proposer knows that it is the first to suggest a value. The proposal for such a request is numbered *0*, so that it will be ignored if any higher numbered requests have been received.

***References***

L. Lamport, **“Paxos Made Simple”** in ACM SIGACT News, vol. 32, no. 4, pp. 18–25, 2001.

Baker, J., Bond, C., Corbett, J. C., Furman, J., Khorlin, A., Larson, J., Léon, J. M., **“Megastore: Providing Scalable, Highly Available Storage for Interactive Services”** in Proceedings of the Conference on Innovative Data Systems Research, pp. 223-234, 2011.

T. D. Chandra, R. Griesemer, and J. Redstone, **“Paxos made live: an engineering perspective”**, in Proceedings of the twenty-sixth annual ACM Symposium on Principles of Distributed Computing, 2007, pp. 398–407.

* * *

[[1]](https://angus.nyc/2012/paxos-by-example/#ftn1) The method of ensuring the uniqueness of proposal numbers when there are multiple proposers is not specified in the Paxos algorithm itself.

[[2]](https://angus.nyc/2012/paxos-by-example/#ftn2) It may not, but the algorithm is resilient to this.

[[3]](https://angus.nyc/2012/paxos-by-example/#ftn3) Note that this is the highest proposal number that it received from *prepare response* messages. In this example, *proposer B* has a higher numbered proposal (*n=4*) than *proposer A* (*n=2*), but it has only received *proposer A’s* proposal in response to its *prepare request*. If no previous proposals were returned by the *prepare response* messages, *proposer B* would use its own proposal (*n=4*).

Updated (4/29/15): Updated text to address an ambiguity discussed in a [comment](http://angus.nyc/writing/paxos-by-example/#comment-23).

- [About](https://angus.nyc/2012/paxos-by-example/#abh_about)
- [Latest Posts](https://angus.nyc/2012/paxos-by-example/#abh_posts)

[(L)](http://angus.nyc/)
 [(L)](http://twitter.com/angusmacdonald)

### [Angus Macdonald](http://angus.nyc/)

Angus works in New York City for Google. He has a PhD in Computer Science from the University of St Andrews.

Posted in [Systems](https://angus.nyc/category/systems/)Tagged [algorithm](https://angus.nyc/tag/algorithm/), [distributed consensus](https://angus.nyc/tag/distributed-consensus/), [paxos](https://angus.nyc/tag/paxos/)

# Post navigation

[← Concurrency Control Mechanisms](https://angus.nyc/2011/concurrency-control-mechanisms/)

[PhD Thesis →](https://angus.nyc/2012/phd-thesis/)

## 18 thoughts on “Paxos By Example”

1. **Chaitanya**

[April 8, 2015 at 10:30 pm](https://angus.nyc/2012/paxos-by-example/#comment-23)

I think this statement of yours is incorrect:

“If the acceptor has not seen a higher numbered request, it again promises to ignore any requests with lower proposal numbers, and sends back the previous highest proposal number that it has seen along with the value of that proposal.”

From PAXOS made simple:
“If an acceptor receives a prepare request with number n greater
than that of any prepare request to which it has already responded,
then it responds to the request with a promise not to accept any more

proposals numbered less than n and with the highest-numbered proposal (if any) that it has accepted”

The response from the acceptor contains “the highest-numbered proposal ( if any ) that it has accepted” and not “the previous highest proposal number that it has seen”

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=23#respond)
    1. **amacdonald**

[April 30, 2015 at 12:57 am](https://angus.nyc/2012/paxos-by-example/#comment-36)

Thanks for the comment. You’re right, i’ll update the post.
[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=36#respond)
        1. **stephen**

[September 12, 2015 at 11:49 pm](https://angus.nyc/2012/paxos-by-example/#comment-425)

The figure 4 is incorrect. The value 8 is only been prepared, not been accepted. So acceptor x will not return [n=2,v=8], it will return [no previous].

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=425#respond)
            1. **[Angus Macdonald](http://angus.nyc/)**

[October 21, 2015 at 8:08 pm](https://angus.nyc/2012/paxos-by-example/#comment-557)

Hi Stephen,

My understanding of the algorithm is that this is correct. From the “Paxos Made Simple” paper:

> Suppose an acceptor receives a prepare request numbered n, but it has already responded to a prepare request numbered greater than n, thereby promising not to accept any new proposal numbered n.

This implies that the response from the prepare request counts as being “accepted” in that context.

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=557#respond)
                1. **stephen**

[January 15, 2016 at 1:47 pm](https://angus.nyc/2012/paxos-by-example/#comment-803)

From the “Paxos Made Simple” paper:

Phase 1. (a) A proposer selects a proposal number n and sends a prepare request with number n to a majority of acceptors.

(b) If an acceptor receives a prepare request with number n greater than that of any prepare request to which it has already responded, then it responds to the request with a promise not to accept any more proposals numbered less than n and with the highest-numbered pro- posal (if any) that it has accepted.

It responds to the request …… with the highest-numbered proposal ( if any ) that it has accepted.

2. **[Neil Moore](http://www.bigoh.co.uk/)**

[July 25, 2015 at 9:07 am](https://angus.nyc/2012/paxos-by-example/#comment-204)

Enjoyed reading this. Glad I just use existing DB systems now.

It’s left unspecified how nodes discover other nodes that are accepters and proposers. So how do they know when there is a majority. Aren’t the set of nodes also hard for nodes to agree upon?

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=204#respond)
    1. **[Angus Macdonald](http://angus.nyc/)**

[July 27, 2015 at 1:11 pm](https://angus.nyc/2012/paxos-by-example/#comment-231)

Thanks! That’s left unspecified by the original papers, but my understanding is that the initial set of machines is typical static, so you already inherently know what a majority is (and if you change membership, there’s possibly a downtime cost).

It gets complicated, because Paxos is often cited as a tool to *manage* group membership reliably, which pushes the problem down to (hopefully) a smaller, easier to maintain set of machines.

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=231#respond)
3. **Raghu**

[February 22, 2016 at 11:27 pm](https://angus.nyc/2012/paxos-by-example/#comment-872)

Hi ,

Can you let me know how to implement Paxos algorithm using any programming language?

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=872#respond)
    1. **[Angus Macdonald](http://angus.nyc/)**

[March 3, 2016 at 10:42 pm](https://angus.nyc/2012/paxos-by-example/#comment-879)

Hi Raghu, I don’t sorry.
[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=879#respond)
4. **[mateen](http://no/)**

[March 1, 2016 at 2:55 am](https://angus.nyc/2012/paxos-by-example/#comment-877)

hi

if a proposer send prepare request to acceptors and the acceptors have not accepted any prepare request before it will respond with the current proposer no which it receives from proposer with value nil because there is no previous prepare request that is accepted by acceptors so at this time the proposer will chose a value randomly and then will be sent to acceptors in it’s accept message

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=877#respond)
5. **kant**

[November 8, 2016 at 10:20 am](https://angus.nyc/2012/paxos-by-example/#comment-1448)

from the post it sounds like [n=6, v=8] gets accepted. which means v=8 is getting accepted twice (first time with n=4 and second time with n=6) by every acceptor ?

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1448#respond)
    1. **[Angus Macdonald](http://angus.nyc/)**

[November 12, 2016 at 9:15 pm](https://angus.nyc/2012/paxos-by-example/#comment-1471)

Paxos makes sure that only one value is chosen, it doesn’t matter which value or how many times that happens.

In the example you mentioned, it’s good that v=8 is accepted twice — that just means that each machine is in agreement!

But note that this example covers just a single instance of the Paxos algorithm, so if you had (for example) multiple transactions, each transaction would be using a separate instance of the algorithm. I think thats what you might be getting at in relation to v=8 being selected twice.

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1471#respond)
6. **kant**

[November 10, 2016 at 11:29 am](https://angus.nyc/2012/paxos-by-example/#comment-1459)

How does Acceptor Z in figure 4 knows it needs to send [n=4, v=8] ? is it(acceptors in general) keeping track of which proposer the proposals are coming from?

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1459#respond)
    1. **[Angus Macdonald](http://angus.nyc/)**

[November 12, 2016 at 9:15 pm](https://angus.nyc/2012/paxos-by-example/#comment-1472)

Acceptors keep track of what they’ve already seen, yes.
[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1472#respond)
7. **KUN CAO**

[December 6, 2016 at 2:39 am](https://angus.nyc/2012/paxos-by-example/#comment-1551)

Hi Angus, thanks for your illustrative explanation!
Just want to ask that
1. what does the abscissa represent? Is that time?
2. what is the physical meaning of proposal number?

3. which part of the algo shows the “majority”? the acceptors just choose to accept and ignore the request, they did not communicate with each other, how did they to do something like voting?

Sorry I am a beginner in this field, hope you can help me. Thanks!
[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1551#respond)
    1. **[Angus Macdonald](http://angus.nyc/)**

[January 21, 2017 at 3:11 am](https://angus.nyc/2012/paxos-by-example/#comment-1787)

Hey, sorry for the delayed response.
1. Yes, time.

2. It’s Application dependent but there are lots of examples of it being used to select a leader node. Also, two-phase commit is a degenerate version of Paxos, so it could represent agreement on a COMMIT/ROLLBACK decision or something similar.

3. That’s not defined, but if any acceptor sees a majority, the algorithm is designed so that nothing happens to make the other acceptors come to a different decision. So they don’t need coordination.

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1787#respond)
8. **Mahdi**

[February 3, 2017 at 3:11 pm](https://angus.nyc/2012/paxos-by-example/#comment-1831)

Hello,
Awesome example!
I don’t understand why proposers have to send the value of pervious attempts?
What happend to their own values?
In the example, B initially wanted to send v=5 but it sends v=8.
Best
[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1831#respond)
    1. **[Angus Macdonald](http://angus.nyc/)**

[February 12, 2017 at 6:31 pm](https://angus.nyc/2012/paxos-by-example/#comment-1862)

Thanks Mahdi. My understanding is that it is part of the approach that makes sure proposers eventually agree on a value.

It’s somewhat counter-intuitive, but it doesn’t matter to the proposer that *their* value is selected, it just matters that all of them eventually agree on a value. The algorithm doesn’t care what that value is.

[Reply](https://angus.nyc/2012/paxos-by-example/?replytocom=1862#respond)

### Leave a Reply

Your email address will not be published. Required fields are marked *
Comment
Name *
Email *
Website