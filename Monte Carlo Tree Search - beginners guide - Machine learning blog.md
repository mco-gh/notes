Monte Carlo Tree Search - beginners guide - Machine learning blog

# Monte Carlo Tree Search

![monte carlo tree search - tic tac toe game tree ](../_resources/f77010dc5192b987f7a67440b20251da.png)

Let’s try to describe the tic-tac-toe game tree you (partially) see:

- at the very top, you can see the **root** of the tree, representing the **initial state** of the tic-tac-toe game, empty board (marked green)
- any transition from one node to another represents **a move**
- **branching factor** of tic-tac-toe varies – it depends on tree depth
- game ends in a **terminal node** (marked red)
- the tree traversal from the root to the terminal node represents a single game playout

to limit a game tree size, only visited states are **expanded**, unexpanded nodes are marked gray

Game tree is a recursive data structure, therefore after choosing the best move you end up in a child node which is in fact a root node for its subtree. Therefore you can think of a game as a sequence of “the most promising next move” problems represented by a game tree everytime (with different root node). Very often in practice, you do not have to remember the path leading to your current state, as it is not a concern in a current game state.

#### What is the most promising next move? Very shortly about minimax and alpha-beta pruning

Once again, our ultimate goal is to find **the most promising next move** assuming given game state and the game tree implied. But what would that actually mean?

There is no straight answer to this. First of all you do not know your opponent strategy in advance – he/she may play the perfect game or may be far from a good player. Let’s assume Chess. Knowing that your opponent is an amateur (mathematician would say “knowing you opponent **mixed strategy**“) you may choose simple **strategy **to try trick him and win quickly. But the same **strategy ** against a strong opponent would turn against you. That’s obvious.

If you don’t know your opponent at all there is one very radical strategy called **minimax** that maximizes your payoff assuming your opponent plays the best possible game. In two person finite zero-sum sequential game between A and B (where A maximizes his utility and B tries to minimize it) **, the minimax algorithm** may be described by the following recursive formula:

vA(si)vB(si)=maxaivB(move(si,ai))vA(ŝ )=eval(ŝ )=minaivA(move(si,ai))vB(ŝ )=−eval(ŝ )vA(si)=maxaivB(move(si,ai))vA(s^)=eval(s^)vB(si)=minaivA(move(si,ai))vB(s^)=−eval(s^)

where

- vAvA and vBvB are utility functions for players A and B respectively (utility = gain, payoff)
- movemove is a function that produces the next game state (one of the current node children) given current state sisi and action at that state aiai
- evaleval is a function that evaluates the final game state (at terminal node)
- and ŝ s^ is any final game state (a terminal node)
- minus sign at vBvB for terminal state is to indicate that game is a zero-sum game – no need to worry!

Simply speaking, given state ss you want to find a move aiai that will result in the biggest reward assuming your opponent tries to minimize your reward (maximize his). Hence the name **minimax**. This sounds almost good. All we need is** to expand the whole game tree** and backpropagate the value with respect to rules given by our recursive formula.

![minimax tree simple game ](../_resources/e54c863cb87670db1ddb925aa6b359bf.png)

The game tree above illustrates the choice of **the best move** in minimax algorithm. The white queen wants the game result to be as dark (cold) as possible (reward = pixel intensity) while dark queen will folow the paths leading to the lightest (warmest) colors. Every choice on every level is optimal in minimax sense. We can start from the bottom terminal nodes where the choice is a obvious. Dark queen will always pick the lightest color. Then the white queen will chase her maximal reward and choose the path leading to the darkest color. And so on.. up to the node representing the current game state. This is how basic **minimax algorithm** works.

The **biggest weakness of minimax** algorithm is the necessity to expand the whole game tree. For games with high branching factor (like Go or Chess) it leads to enormous game trees and so certain failure.

Is there a remedy for this?

There is a few. One way to go is to **expand our game tree only up to certain threshold depth d **. But then we are not guaranteed that any node at our threshold tree level d is terminal. Therefore we need a function that evaluates a non-terminal game state. This is very natural for humans: [by looking at Chess or Go board you may be able to predict the winner](https://int8.io/chess-position-evaluation-with-convolutional-neural-networks-in-julia/) even though the game still continues. For example: It is rather formality to end the games below

![](../_resources/e45663c077aaf16d6f3e4a8e9c16a58c.jpg)
![](../_resources/fbf1798478b219dd0bc0e178fc9604ff.jpg)
![](../_resources/bfaa12d3e305b29e71c6556fc31df582.jpg)

Another way to overcome game tree size problem is to prune the game tree via [alpha-beta pruning algorithm](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). Alpha-beta pruning is boosted minimax. It traverse the game tree in minimax-fashion avoiding expansion of some tree branches. The result is at best the same as minimax – alpha-beta pruning guarantees improvement by reduction of the search space, though.

The intuitive introduction to minimax and alpha-beta pruning can be found [here](https://www.youtube.com/watch?v=STjW3eH0Cik). Minimax/Alpha-beta pruning is already very mature solution and is being used in various successful game engines nowadays like [Stockfish](https://github.com/official-stockfish/Stockfish) – the main rival of Alpha Zero in a set of games [played](https://www.chess.com/news/view/google-s-alphazero-destroys-stockfish-in-100-game-match) at the end of 2017 in [somehow controversial](https://www.chess.com/news/view/alphazero-reactions-from-top-gms-stockfish-author) tone.

### Monte Carlo Tree Search – basic concepts

In Monte Carlo Tree Search algorithm – the scope of our post today – **the most promising move** is computed in a sightly different fashion. As the name suggests (especially its monte-carlo component) – Monte Carlo Tree Search simulates the games many times and tries to predict the most promising move based on the simulation results.

The main concept of monte carlo tree search is a **search**. Search is a set of traversals down the game tree. Single **traversal **is a path from a root node (current game state) to a node that is **not fully expanded**. Node being not-fully expanded means at least one of its children is **unvisited**, not explored. Once not fully expanded node is encountered, one of its unvisited children is chosen to become a root node for a single **playout/simulation**. The result of the simulation is then **propagated back** up to the current tree root updating game tree nodes **statistics**. Once the search (constrained by time or computational power) terminates, the move is chosen based on the gathered statistics.

Lots of dots not clearly connected together, right?

Let’s try to ask crucial questions regarding the simplified description above to slowly understand all the pieces:

- what are expanded or **not fully unexpanded **game tree nodes?
- what it means ‘**to traverse down**‘ during **search**? How is the next (child) node **selected**?
- what is a **simulation**?
- what is the **backpropagation**?
- what **statistics **are back-propagated and updated in expanded game tree nodes ?
- How is the final move even chosen ?

Again, stay focused, we will get there soon, bit by bit.

#### Simulation/Playout

Let’s focus on **simulation** (or **playout **equivalently) first as it does not rely on other terms’ definitions heavily. Playout/simulation is a single act of a game play – a sequence of moves that starts in current node (representing game state) and ends in a terminal node where game result can be computed. Simulation is a game tree node **evaluation approximation** computed by running somehow** random game starting at that node**.

How are the moves chosen during simulation?

During simulation the moves are chosen with respect to a function called **rollout policy function**:

RolloutPolicy:si→aiRolloutPolicy:si→ai

that consumes a game state and produces the next move/action. In practice it is designed to be fast to allow many simulations being played quickly – default rollout policy function is a **uniform random**.

![monte carlo tree search playout/simulation](../_resources/001d1a5c0ac01dcb217c34579b4aa52e.png)

#####  Playout/Simulation is Alpha Go and Alpha Zero

In **Alpha Go Lee** evaluation of the leaf SLSL is a weighted sum of two components:

- standard rollout evaluation zLzL with custom **fast rollout policy** that is a shallow softmax neural network with handcrafted features
- position evaluation given by 13-layer convolutional neural network v0v0 called **Value Network** trained on 30mln of distinct (no two positions come from the same game) positions extracted from Alpha Go self-plays

V(SL)=(1−α)v0(SL)+αzLV(SL)=(1−α)v0(SL)+αzL

In **Alpha Zero** Deepmind’s engineers went a step further, they **do not perform playouts at all**, but directly evaluate the current node with a 19-layer CNN Residual neural network (In Alpha Zero they have one network f0f0 that outputs position evaluation and moves probability vector at once)

V(SL)=f0(SL)V(SL)=f0(SL)

Simulation/rollout in a simplest form is then just a random sequence of moves that starts at given game state and terminates. Simulation always results in an evaluation – for the games we talked about it is a win, loss or a draw, but generally any value is a legit result of a simulation.

In Monte Carlo Tree Search simulation always starts at the node that has not been **visisted **previously – we will learn what visited node means in a minute.

####  Game tree node expansion – fully expanded and visited nodes

Let’s think about how humans think about the games such as Go or Chess.

Given a root node plus the rules of the game the rest of the game tree is already implied. It pops up and we can traverse it without storing the whole tree in the memory. In its initial form though it is not expanded at all. In the very initial game state we are at the root of the game tree and the remaining nodes are unvisited. Once we consider a move we imagine a position a move would result in. Somehow we visit a node analyzing (evaluating) position a move would bring. Game states that you never even considered visiting remain unvisited and their potential is undicovered.

The same distinction applies to Monte Carlo Tree Search game tree. Nodes are considered visited or unvisited. What it means for a node to be visited? Node is considered visited **if a playout has been started in that node** – meaning it has been evaluated at least once. If all children nodes of a node are visited node is considered **fully expanded**, otherwise – well – it is not fully expanded and further expansion is possible.

![visited and unvisited nodes in monte carlo tree search](../_resources/d3c057cf009fcdaf0fbb7c90b8df7190.png)

In practice then, at the very beginning of a search all of the root node children are unvisited – one is **picked **and first simulation (evaluation) starts right away.

Please be aware that **nodes chosen** by rollout policy function **during simulation** are **not considered visited**. They remain univisited even though a rollout passes through them, only the node where simulation starts is marked visited.

####  Backpropagation – propagating back the simulation result

Once simulation for a freshly visisted node (sometimes called a **leaf**) is finished, its result is **ready to be propagated back** up to the current game tree root node. The node where simulation started is marked **visited**.

![monte carlo tree search - backprop](../_resources/3c0dbca641e856014d9cbc14593b3037.png)

Backpropagation is a traversal back from the leaf node (where simulation started) up to the root node. Simulation result is carried up to the root node and for every node on the backpropagation path certain **statistics **are computed/updated. Backpropagation guarantees that every node’s statistics will reflect results of simulation started in all its descendants (as the simulation results are carried up to the game tree root node)

####  Nodes’ statistics

The motivation for back-propagating simulation result is to update the **total simulation reward**  Q(v)Q(v) and **total number of visits**  N(v)N(v) for all nodes vv on backpropagation path (including the node where the simulation started).

- Q(v)Q(v) – **Total simulation reward** is an attribute of a node vv and in a simplest form is a sum of simulation results that passed through considered node.
- N(v)N(v) – **Total number of visits ** is another atribute of a node vv representing a counter of how many times a node has been on the backpropagation path (and so how many times it contributed to the total simulation reward)

These two values are maintained for every visited node, once certain number of simulation is finished visited nodes will store information indicating how expolited/explored they are.

In other words, if you look at random node’s statistics these two values will reflect how promising the node is (total simulation reward) and how intensively explored it has been (number of visits). Nodes with high reward are good candidates to follow (**exploitation**) but those with low amount of visits may be interesting too (because they are not **explored **well)

One puzzle is still missing. How do we get from a root node to the unvisited node to start a simulation?

####  Game tree traversal

Well, at the very beginning of the search, since we have not started any simulations yet, **unvisited nodes are chosen first**. Single **simulation **starts at each of them, results are **backpropagated **to the root node and then root is considered **fully expanded**.

But what do we do next? How do we now navigate from a fully expanded node to an unvisited node? We have to go through the layers of visisted nodes and so far there is no recipe how to proceed.

To pick the next node on our path to starting the next simulation via fully expanded node vv we need to consider information about all children of vv: v1,v2,…,vkv1,v2,…,vk and the information about the node vv itself. Let’s think what information is available now:

![monte carlo tree search - UCT](../_resources/9bb773fb75c5b6ba4f23984a21a32909.png)

Our current node – marked blue – is fully expanded so it must have been visisted and so stores its node statistics: total simulation reward and total number of visits, same applies to its children. These values are compounds of our last piece: **Upper Confidence Bound applied to trees** or shortly **UCT **

####  Upper Confidence Bound applied to trees

UCT is a function that lets us choose the next node among visited nodes to traverse through – the core function of Monte Carlo Tree Search

𝕌ℂ𝕋(vi,v)=Q(vi)N(vi)+clog(N(v))N(vi)‾‾‾‾‾‾‾‾‾‾√UCT(vi,v)=Q(vi)N(vi)+clog⁡(N(v))N(vi)

**Node maximizing UCT is the one to follow **during Monte Carlo Tree Search tree traversal. Let’s see what UCT function does:

First of all our function is defined for a child node vivi of a node vv. It is a sum of two components – the first component of our function Q(vi)N(vi)Q(vi)N(vi), also called **exploitation component**, can be read as a winning/losing rate – we have total simulation reward divided by total number of visits which etimates win ratio in the node vivi. This already looks promising – at the end of the day we might want to traverse through the nodes that have high winning rate.

Why can’t we use exploitation component only? Because we would very quickly end up **greedily exploring only those nodes that bring a single winning playout** very early at the beginning of the search.

Quick example:

Let’s assume we start Monte Carlo Tree Search routine using exploitation UCT component only. Starting from a root node we run a simulation for all children and then in the next steps only visit those for which simulation result is at least one win. Nodes for which first simulation was **unlucky **(please recall default policy function that is very often random in practice) would be **abandoned **right away without any chance to improve.

Therefore we have a second component of UCT called **exploration component **. Exploration component favor nodes that have not been explored – those that have been relatively rarely visited (those for which N(vi)N(vi) is lower). Let’s take a look at the shape of exploration component of UCT function – it decreases with numbers of visits in a node and will give high chance of selection for less-visited nodes directing the search towards **exploration**

![monte carlo tree search - exploration ](../_resources/6490ed338665bc703b9c21d8edb6a623.png)

Finally, parameter cc in the UCT formula controls the trade-off between expolitation and exploration in Monte Carlo Tree Search.

#####  UCT in Alpha Go and Alpha Zero

In both **Alpha Go Lee** and **Alpha Zero** the tree traversal follows the nodes that maximize the following UCT variant:

𝕌ℂ𝕋(vi,v)=Q(vi)N(vi)+cP(v,vi)N(v)1+N(vi)‾‾‾‾‾‾‾‾‾‾√UCT(vi,v)=Q(vi)N(vi)+cP(v,vi)N(v)1+N(vi)

where P(vi,v)P(vi,v) is prior probability of the move (transition from vv to vivi ), its value comes from the output of deep neural network called **Policy Network **. Policy Network is a function that consumes game state and produce probability distribution over possible moves (please note this one is different from fast rollout policy). The purpose here is to reduce the search space to the moves that are reasonable – adding it to exploration component directs exploration towards the reasonable moves.

#####  Policy network training in Alpha Go and Alpha Zero

There are two policy networks in **Alpha Go**

- **SL Policy Network** that is trained in a supervised fashion based on human games dataset.
- **RL Policy Network ** – boosted SL Policy Network – it has the same architecture but is further trained via **Reinforcement Learning** (self-plays)

Interestingly – in Deepmind’s Monte Carlo Tree Search variant – SL Policy Network output is chosen for prior move probability estimation P(v,vi)P(v,vi) as it performs better in practice (authors suggest that human-based data is richer in explorative moves). What is the purpose of the RL Policy Network then? The stronger RL Policy Network is used to generate 30 mln positions dataset for Value Network training (the one used for game state evaluation)

In **Alpha Zero** on the other hand there is only one network f0f0 that is both Value and Policy Network. It is trained entirely via self-play starting from random initialization. There is a number of networks trained in parallel and the best one is chosen for training data generation every checkpoint after evaluation against best current neural network.

One important remark on UCT function: in competitive games its **exploitaion component **QiQi is always **computed relative to player who moves** at node ii – it means that while traversing the game tree **perspective changes depending on a node being traversed through**: for any two consecutive nodes this perspective is opposite.

####  Terminating Monte Carlo Tree Search

We now know almost all the pieces needed to successfully implement Monte Carlo Tree Search, there are few questions we need to answer though. First of all** when do we actually end the MCTS procedure? **. The answer to this one is: it depends on the context. If you build a game engine then your “thinking time” is probably limited, plus your computational capacity has its boundaries, too. Therefore the safest bet is to run MCTS routine as long as your resources let you.

Once the MCTS routine is finished, the best move is usually the one with the** highest number of visits **N(vi)N(vi) since it’s value has been estimated best (the value estimation itself must have been high as it’s been explored most often, too)

![best move - monte carlo tree search](../_resources/f7202a039d8e2cbc19bfcca0bdf7069d.png)

After picking your move using Monte Carlo Tree Search, your node of choice will become a game state for your opponent to move from. Once he picks his move – again – you will start Monte Carlo Tree Search routine starting from a node representing a game state chosen by your opponent. Some statistics from previous MCTS rounds may still be in that new branch you are now considering. This brings an idea of re-using the statistics instead of building new tree from scratch – and in fact this is what creators of Alpha Go / Alpha Zero did, too.

###  Monte Carlo Tree Search – summary

Having all the bits together, let’s try to recall the very first [simplified description](https://int8.io/monte-carlo-tree-search-beginners-guide/?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI#Monte_Carlo_Tree_Search_8211_basic_concepts) of Monte Carlo Tree Search and enclose it in **pseudo-code**:

def monte_carlo_tree_search(root):while resources_left(time, computational power):

leaf = traverse(root)# leaf = unvisited node simulation_result = rollout(leaf)

backpropagate(leaf, simulation_result)return best_child(root)def traverse(node):while fully_expanded(node):

node = best_uct(node)return pick_univisted(node.children)or node # in case no children are present / node is terminal def rollout(node):while non_terminal(node):

node = rollout_policy(node)return result(node)def rollout_policy(node):return pick_random(node.children)def backpropagate(node, result):if is_root(node)return node.stats = update_stats(node, result) backpropagate(node.parent)def best_child(node):

pick child with highest number of visits

As you can see it reduces to very few set of functions that could work for any game of your choice, not only Go or Chess. Actually, you can find example implementation of Monte Carlo Tree Search for Tic-Tac-Toe [here](https://github.com/int8/monte-carlo-tree-search).

That would be all folks, I hope you enjoyed the read and the content here helped you understand Monte Carlo Tree Search – writing it definitely helped me wrap my head around it.

The very next step (hopefully material for the next post) is trying to implement a simple chess bot with components similar to AlphaGo: Value and Policy Network plus MCTS (some work on that – still in progress though – can be found [here](https://github.com/int8/chess-position-evaluation))