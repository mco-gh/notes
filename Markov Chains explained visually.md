Markov Chains explained visually

# Markov Chains

### Explained Visually

[**Tweet](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fsetosa.io%2Fev%2Fmarkov-chains%2F&ref_src=twsrc%5Etfw&text=Markov%20Chains%20explained%20visually&tw_p=tweetbutton&url=http%3A%2F%2Fsetosa.io%2Fev%2Fmarkov-chains%2F&via=setosaio)

|     |     |
| --- | --- |
|     | [(L)](https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fsetosa.io%2Fev%2Fmarkov-chains%2F&display=popup&ref=plugin&src=like&kid_directed_site=0) |

By [Victor Powell](http://twitter.com/vicapow)

with text by [Lewis Lehe](http://twitter.com/lewislehe)

Markov chains, named after [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov), are mathematical systems that hop from one "state" (a situation or set of values) to another. For example, if you made a Markov chain model of a baby's behavior, you might include "playing," "eating", "sleeping," and "crying" as states, which together with other behaviors could form a 'state space': a list of all possible states. In addition, on top of the state space, a Markov chain tells you the probabilitiy of hopping, or "transitioning," from one state to any other state---e.g., the chance that a baby currently playing will fall asleep in the next five minutes without crying first.

A simple, two-state Markov chain is shown below.

 speed
AB

With two states (A and B) in our state space, there are 4 possible transitions (not 2, because a state can transition back into itself). If we're at 'A' we could transition to 'B' or stay at 'A'. If we're at 'B' we could transition to 'A' or stay at 'B'. In this two state diagram, the probability of transitioning from any state to any other state is 0.5.

Of course, real modelers don't always draw out Markov chain diagrams. Instead they use a "transition matrix" to tally the transition probabilities. Every state in the state space is included once as a row and again as a column, and each cell in the matrix tells you the probability of transitioning from its row's state to its column's state. So, in the matrix, the cells do the same job that the arrows do in the diagram.

  speed

AB

A

B

A

P(A|A): 0.50

P(B|A): 0.50

B

P(A|B): 0.50

P(B|B): 0.50

If the state space adds one state, we add one row and one column, adding one cell to every existing column and row. This means the number of cells grows quadratically as we add states to our Markov chain. Thus, a transition matrix comes in handy pretty quickly, unless you want to draw a jungle gym Markov chain diagram.

One use of Markov chains is to include real-world phenomena in computer simulations. For example, we might want to check how frequently a new dam will overflow, which depends on the number of rainy days in a row. To build this model, we start out with the following pattern of rainy (R) and sunny (S) days:

RRRRRRRRSSSSSSSSSRSSSRRRRSR

One way to simulate this weather would be to just say "Half of the days are rainy. Therefore, every day in our simulation will have a fifty percent chance of rain." This rule would generate the following sequence in simulation:

RRSSRSSRRSRRSRSRRSSRRSSSRRS

Did you notice how the above sequence doesn't look quite like the original? The second sequence seems to jump around, while the first one (the real data) seems to have a "stickyness". In the real data, if it's sunny (S) one day, then the next day is also much more likely to be sunny.

We can minic this "stickyness" with a two-state Markov chain. When the Markov chain is in state "R", it has a 0.9 probability of staying put and a 0.1 chance of leaving for the "S" state. Likewise, "S" state has 0.9 probability of staying put and a 0.1 chance of transitioning to the "R" state.

  speed

RS

RRSSRRRRRRR

In the hands of metereologists, ecologists, computer scientists, financial engineers and other people who need to model big phenomena, Markov chains can get to be quite large and powerful. For example, the algorithm Google uses to determine the order of search results, called [PageRank](https://en.wikipedia.org/wiki/PageRank), is a type of Markov chain.

ABC

edit below this line

  speed

Above, we've included a Markov chain "playground", where you can make your own Markov chains by messing around with a transition matrix. Here's a few to work from as an example: [ex1](#), [ex2](#), [ex3](#) or generate one [randomly](#). The transition matrix text will turn red if the provided matrix isn't a valid transition matrix. *The rows of the transition matrix must total to 1.* There also has to be the same number of rows as columns.

You can also access a fullscreen version at [setosa.io/markov](http://setosa.io/markov/index.html)