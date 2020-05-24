Reinforcement learning without gradients: evolving agents using Genetic Algorithms

# Reinforcement learning without gradients: evolving agents using Genetic Algorithms

[![1*LckTzKicHoE_xRRBRk1ThA.png](../_resources/dde010149d55818f24a2297be0c1457b.png)](https://towardsdatascience.com/@paraschopra?source=post_header_lockup)

[Paras Chopra](https://towardsdatascience.com/@paraschopra)
Jan 7·10 min read

During holidays I wanted to ramp up my reinforcement learning skills. Knowing absolutely nothing about the field, I did a [course](https://www.udemy.com/reinforcement-learning-with-pytorch/) where I was exposed to Q-learning and its “deep” equivalent (Deep-Q Learning). That’s where I got exposed to OpenAI’s [Gym](https://gym.openai.com/) where they have several environments for the agent to play in and learn from.

The course was limited to Deep-Q learning, so as I read more on my own. I realized there are now better algorithms such as policy gradients and its variations (such as Actor-Critic method). If this is your first time with Reinforcement Learning, I recommend following resources that I found helpful to build a good intuition:

- •Andrej Karpathy’s [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/). It’s a classic tutorial that sparked widespread interest in reinforcement learning. **Must read**.
- •[Diving deeper into Reinforcement Learning with Q-Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe). The post gives a **nice, illustrated overview of the most fundamental RL algorithm**: Q-learning.
- •[Introduction to Various Reinforcement Learning Algorithms](https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-i-q-learning-sarsa-dqn-ddpg-72a5e0cb6287). A **walkthrough through the world of RL algorithms**. (Interestingly, the algorithm that we’re going to discuss in this post — Genetic Algorithms — is missing from the list.
- •[Intuitive RL: Intro to Advantage-Actor-Critic (A2C)](https://hackernoon.com/intuitive-rl-intro-to-advantage-actor-critic-a2c-4ff545978752). **A really, really well-done comic **(yes, you heard it right) of the currently most advanced algorithm in RL.

I feel blessed that as a community, we share so much that within a couple of days of knowing nothing about reinforcement learning, I was able to replicate what was state of the art just 3 years ago: [playing Atari games using pixel data.](https://www.nature.com/articles/nature14236) Here’s a quick video of my agent (in green) playing Pong against AI using only pixel data.

![](../_resources/1c359dc353184c2f757e17ee2b9e3910.png)![1*slUhU0f7tQPjJtOSZ-uy-g.gif](../_resources/956f7d9273cc5c6afee5990bb7644157.gif)

This sort of feels like a personal achievement!

### The Problem with Reinforcement Learning

My agent trained just fine using policy gradients algorithm, but that took a full 2 days and nights of training on my laptop. And even after that, it wasn’t playing perfectly.

I know that in the grand scheme of things 2 days isn’t a lot but I was curious about why training in reinforcement learning is *so* slow. Reading and thinking more about this, I realized that **the reason reinforcement learning is slow is because gradients are (almost) non-existent and therefore not very useful**.

Gradients help in supervised learning tasks such as image classification by giving useful information on how parameters (weights, biases) of the network should be changed for better accuracy.

![](../_resources/69e7205d7133679381b7df165b7e7377.png)![1*GvTXn6RhZ20CloRCbbF0dw.gif](../_resources/2333cbb27fb50b84ef4139306aff46ac.gif)

Imagine this surface representing error for different combinations of weights and biases (the lower the better). Starting from a randomly initialized point (of weights and biases), we want to find the values that minimize the error (the lowest point). Gradients at each point represent the direction of downhill, so finding the lowest point is equivalent to following the gradient. (Wait, did I just describe the [stochastic gradient descent](https://medium.com/@hakobavjyan/stochastic-gradient-descent-sgd-10ce70fea389) algo?)

In image classification, after every mini-batch of training, backpropagation provides a clear gradient (direction) for each of the parameters in the network. However, in reinforcement learning, the gradient information only comes occasionally whenever environment gives a reward (or penalty). Most of the times our agent is taking actions not knowing whether they were useful or not. This lack of gradient information makes our error landscape look like this:

![](../_resources/a88be307074dda3668c7861b396f2e8b.png)![1*vbtNcLiKrR5vPkHPXUDN5A.jpeg](../_resources/93cdba205502ccb41446dd41c6447c37.jpg)

Image via the excellent blog post [Expressivity, Trainability, and Generalization in Machine Learning](https://blog.evjang.com/2017/11/exp-train-gen.html?spref=tw)

The surface of cheese represents parameters of our agent’s network where no matter what agent does, environment gives no reward and hence there’s no gradient (i.e. since there’s zero error/reward signal, we don’t know in which direction to change parameters for a better performance next time). The few holes on the surface represent low error/high reward corresponding to parameters corresponding to agents that perform well.

Do you see the issue with policy gradients now? A randomly initialized agent is likely to lie on the flat surface (rather than a hole). And if a randomly initialized agent is on a flat surface, it’s incredibly hard to move towards better performance because there’s no gradient information. And **because the (error) surface is flat, a randomly initialized agent does a more-or-less random walk and remains stuck with bad policy for a long time**. (This is why it took me days to train an agent. *Hint*: maybe policy gradient approach is no better than random search?)

As the article titled [why RL is flawed](https://thegradient.pub/why-rl-is-flawed/) clearly argued:

> What if the board game you were trying to learn was Go — how would *> you*>  start learning it? You would read the rules, learn some high-level strategies, recall how you played similar games in the past, get some advice… right? Indeed, it’s at least partially **> because of the learning from scratch limitation of AlphaGo Zero and OpenAI’s Dota bots that it is not truly impressive compared to human learning**> : they rely on seeing many orders of magnitude more games and using far more raw computational power than any human ever can.

I think the article hits the nail on its head. RL is inefficient because it doesn’t tell the agent what it is supposed to do. The agent not knowing what to do starts doing random things and only occasionally environment gives out a reward and now an agent must figure out which of the thousands of actions that it took led to environment giving the reward. That’s not how humans learn! **We’re told what needs to be done**, we develop skills and rewards play a relatively minor role in our learning.

![](../_resources/e284b59b123faf0fd000046c8300e6d9.png)![1*Wplg-cfexGp8OLr580ndVA.jpeg](../_resources/6bcedd2a7a18997ddc4291453d4484ce.jpg)

If we trained children through policy gradients, they’ll always be confused about what they did wrong and never learn anything. (Photo via [Pixabay](https://pixabay.com/en/portrait-child-hands-hide-317041/))

### Gradient-free approaches to Reinforcement Learning

As I was exploring alternatives to gradient-based approaches to RL, I hit upon a paper titled: [Deep Neuroevolution: Genetic Algorithms are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning](https://arxiv.org/abs/1712.06567). This paper combined what I was learning (reinforcement learning) and what I’ve always been excited about (evolutionary computing), so I went about implementing the algorithm in the paper and evolve an agent.

Note that strictly speaking, we didn’t even have to implement a genetic algorithm. As hinted above, the same paper found that **even completely random searches were able to discover good agents**. This means that even if you keep randomly generating agents, eventually, you’ll find (and sometimes *faster* than policy gradients) an agent that performs well. I know, it’s insane but this just illustrates our original point that RL is fundamentally flawed as it has very little information for us to use for training an algorithm.

#### What is a Genetic Algorithm?

The name sounds fancy but under the hood, it’s perhaps the simplest algorithm you can devise for exploring a landscape. Consider an agent in an environment (like Pong) that’s implemented via a neural network. It takes pixels in the input layer and outputs probabilities of actions available to it (move the paddle up, down or do nothing).

![](../_resources/305c54aae7f3323d7e6f76fd6501a53c.png)![1*05ExQKJ0nOoWV80SNVEyJg.png](../_resources/60aadc115026995fd1008398f012adc2.png)

Image via [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)

Our task in reinforcement learning is to find the parameters (weights and biases) of the neural network (weights and biases) that make the agent win more often and hence get more rewards. So far so good?

**Pseudocode for Genetic Algorithms**

- •Simply imagine the agent to be an organism,
- •Parameters will be its genes that specify its behavior (the policy)
- •Rewards will indicate the organism’s fitness (i.e. higher the rewards, higher the likelihood of survival)
- •In the first iteration, you start with *X* number of agents with randomly initialized parameters
- •Some of them by pure chance will perform better than others
- •And just like the natural evolution in the real world, you implement *survival of the fittest:* simply take the fittest 10% of agents and replicate them for the next iteration until you have *X* agents again for the next iteration. Kill the weakest 90% (if this sounds morbid, you can rename the kill function as give-[moksha](https://en.wikipedia.org/wiki/Moksha)!)
- •During replication of top 10% fittest agents, add a tiny random gaussian noise to its parameters so that in the next iteration, you get to explore the neighborhood around parameters of best agents
- •Keep the top performing agent *as is* (without adding noise) so that you always preserve the best of the best as insurance against Gaussian noise causing a probable reduction in performance

That’s it. You’ve understood the core of Genetic Algorithms (GA). There are many (fancy) variations of GA where there’s all sorts of (dirty) sex(ual recombination) between two agents but the paper on deep neuroevolution implemented the vanilla GA with pseudo-code above and that’s what I also implemented in my code. (You can access [the Jupyter notebook with code on my Github repository](https://github.com/paraschopra/deepneuroevolution)).

![](../_resources/3013b6c349b979641f82a7fd3eb5fd47.png)![1*OvvpYLoJxw09_RlAHyjwSQ.gif](../_resources/f9621464bde5fb94222713a4be0f7be4.gif)

Yellower regions are regions with lower error (higher rewards/performance). Blue dots are all agents. Green ones are the top 10% and the red dot is the best of the best. Notice how gradually the entire population moves towards the region with the lowest error. (Image via [Visual Guide to Evolutionary Strategies](http://blog.otoro.net/2017/10/29/visual-evolution-strategies/))

For more visualizations on how evolutionary algorithms work, I highly recommend going through this insanely well-done post: [A Visual Guide to Evolution Strategies](http://blog.otoro.net/2017/10/29/visual-evolution-strategies/).

#### Code for implementing Deep Neuroevolution for Reinforcement Learning

I t̸r̸a̸i̸n̸e̸d̸ evolved an agent balancing pole on a moving cart (aka [CartPole-v0](https://gym.openai.com/envs/CartPole-v0/)). Here’s the entire code: https://github.com/paraschopra/deepneuroevolution

Using PyTorch, we parametrize the agent through a 2 hidden-layer neural network (wanted to retain the “deep” part :), for CartPole a one layer network might also have done just fine).

![](../_resources/e631f5b89367147e5bb80f72a84ee17d.png)

|     |     |
| --- | --- |
| 1   | class  CartPoleAI(nn.Module): |
| 2   |  def  __init__(self): |
| 3   |  super().__init__() |
| 4   |  self.fc = nn.Sequential( |
| 5   | nn.Linear(4,128, bias=True), |
| 6   | nn.ReLU(), |
| 7   | nn.Linear(128,2, bias=True), |
| 8   | nn.Softmax(dim=1) |
| 9   | )   |
| 10  |     |
| 11  |     |
| 12  |  def  forward(self, inputs): |
| 13  | x =  self.fc(inputs) |
| 14  |  return x |

 [view raw](https://gist.github.com/paraschopra/cfdad4ee0f4fa96f328c883da22e2cfb/raw/b6fadfbfedac8e4056d8e1d0694aeacf45c72821/neuroevolution-cartpole-agent.py)  [neuroevolution-cartpole-agent.py](https://gist.github.com/paraschopra/cfdad4ee0f4fa96f328c883da22e2cfb#file-neuroevolution-cartpole-agent-py) hosted with ❤ by [GitHub](https://github.com/)

Here’s **the main loop** of evolution:

![](../_resources/e631f5b89367147e5bb80f72a84ee17d.png)

|     |     |
| --- | --- |
| 1   | game_actions =  2  #2 actions possible: left or right |
| 2   |     |
| 3   | #disable gradients as we will not use them |
| 4   | torch.set_grad_enabled(False) |
| 5   |     |
| 6   | # initialize N number of agents |
| 7   | num_agents =  500 |
| 8   | agents = return_random_agents(num_agents) |
| 9   |     |
| 10  | # How many top agents to consider as parents |
| 11  | top_limit =  20 |
| 12  |     |
| 13  | # run evolution until X generations |
| 14  | generations =  1000 |
| 15  | elite_index =  None |
| 16  |     |
| 17  | for generation in  range(generations): |
| 18  |  # return rewards of agents |
| 19  | rewards = run_agents_n_times(agents, 3) #return average of 3 runs |
| 20  |     |
| 21  |  # sort by rewards |
| 22  | sorted_parent_indexes = np.argsort(rewards)[::-1][:top_limit] #reverses and gives top values (argsort sorts by ascending by default) https://stackoverflow.com/questions/16486252/is-it-possible-to-use-argsort-in-descending-order |
| 23  |     |
| 24  |  # setup an empty list for containing children agents |
| 25  | children_agents, elite_index = return_children(agents, sorted_parent_indexes, elite_index) |
| 26  |     |
| 27  |  # kill all agents, and replace them with their children |
| 28  | agents = children_agents |

 [view raw](https://gist.github.com/paraschopra/293e6f46bc6c1e6ca1236584c2970dbf/raw/a256884f39b87d07f392e71dbdcd64446b98b074/neuroevolution-cartpole-main-loop.py)  [neuroevolution-cartpole-main-loop.py](https://gist.github.com/paraschopra/293e6f46bc6c1e6ca1236584c2970dbf#file-neuroevolution-cartpole-main-loop-py) hosted with ❤ by [GitHub](https://github.com/)

The code is pretty much self-explanatory and follows the pseudo-code that I wrote earlier in this post. Mapping specifics to the pseudo-code :

- •Our population size is 500 (*num_agents*) and we generate agents randomly in the first iteration (*return_random_agents*)
- •Out of 500, we only select top 20 as parents (*top_limit*)
- •The maximum number of iterations that we want to run the loop is 1000 (*generations*). Although usually for CartPole, a decently performing agent is found within a couple of iterations.
- •In each generation, we first run all randomly generated agents and get their average performance over 3 runs (once it could be lucky, so we want to average). This is done through the *run_agents_n_times *function.
- •We sort agents in descending order of their rewards (performance). The sorted indexes are stored in *sorted_parent_indexes*.
- •Then we take the top 20 agents and choose randomly among them to make children for the next iteration. This happens in the *return_children* function (see below). The function adds a small Gaussian noise to all parameters while copying an agent but retains one best-of-the-best elite agent (without adding any noise).
- •With the children agents as parents now, we iterate and run through the entire loop again, until all 1000 generations are done or we find an agent with good performance (in the Jupyter notebook, I print average performance of top 5 agents. When it’s good enough, I manually interrupt the loop)

The ***return_children*** function looks like this:

![](../_resources/e631f5b89367147e5bb80f72a84ee17d.png)

|     |     |
| --- | --- |
| 1   | def  return_children(agents, sorted_parent_indexes, elite_index): |
| 2   |     |
| 3   | children_agents = [] |
| 4   |     |
| 5   |  #first take selected parents from sorted_parent_indexes and generate N-1 children |
| 6   |  for i in  range(len(agents)-1): |
| 7   |     |
| 8   | selected_agent_index = sorted_parent_indexes[np.random.randint(len(sorted_parent_indexes))] |
| 9   | children_agents.append(mutate(agents[selected_agent_index])) |
| 10  |     |
| 11  |  #now add one elite |
| 12  | elite_child = add_elite(agents, sorted_parent_indexes, elite_index) |
| 13  | children_agents.append(elite_child) |
| 14  | elite_index=len(children_agents)-1  #it is the last one |
| 15  |     |
| 16  |  return children_agents, elite_index |

 [view raw](https://gist.github.com/paraschopra/7f40e444e4658228d012601cbaf5c623/raw/ff08a22dd18d91869924ccc657d6abe5e393d91f/neuroevolution-cartpole-return-children.py)  [neuroevolution-cartpole-return-children.py](https://gist.github.com/paraschopra/7f40e444e4658228d012601cbaf5c623#file-neuroevolution-cartpole-return-children-py) hosted with ❤ by [GitHub](https://github.com/)

You see that first, it selects a random agent out of the top 20 agents (with indexes contained in *sorted_parents_indexes*) and then calls the *mutate* function to add random Gaussian noise before appending it to the *children_agents* list. In the second part, it calls the *add_elite* function to add the best-of-the-best agent into the *children_agents* list.

Here’s the ***mutate*** function:

![](../_resources/e631f5b89367147e5bb80f72a84ee17d.png)

|     |     |
| --- | --- |
| 1   | def  mutate(agent): |
| 2   |     |
| 3   | child_agent = copy.deepcopy(agent) |
| 4   |     |
| 5   | mutation_power =  0.02  #hyper-parameter, set from https://arxiv.org/pdf/1712.06567.pdf |
| 6   |     |
| 7   |  for param in child_agent.parameters(): |
| 8   |     |
| 9   |  if(len(param.shape)==4): #weights of Conv2D |
| 10  |  for i0 in  range(param.shape[0]): |
| 11  |  for i1 in  range(param.shape[1]): |
| 12  |  for i2 in  range(param.shape[2]): |
| 13  |  for i3 in  range(param.shape[3]): |
| 14  |     |
| 15  | param[i0][i1][i2][i3]+= mutation_power * np.random.randn() |
| 16  |     |
| 17  |  elif(len(param.shape)==2): #weights of linear layer |
| 18  |  for i0 in  range(param.shape[0]): |
| 19  |  for i1 in  range(param.shape[1]): |
| 20  |     |
| 21  | param[i0][i1]+= mutation_power * np.random.randn() |
| 22  |     |
| 23  |  elif(len(param.shape)==1): #biases of linear layer or conv layer |
| 24  |  for i0 in  range(param.shape[0]): |
| 25  |     |
| 26  | param[i0]+=mutation_power * np.random.randn() |
| 27  |     |
| 28  |  return child_agent |

 [view raw](https://gist.github.com/paraschopra/bd2d591b90761e880a2c6ed6f6149dfc/raw/a40caab9ab83887efe1cc57caee25f1c5a33c603/neuroevolution-cartpole-mutate.py)  [neuroevolution-cartpole-mutate.py](https://gist.github.com/paraschopra/bd2d591b90761e880a2c6ed6f6149dfc#file-neuroevolution-cartpole-mutate-py) hosted with ❤ by [GitHub](https://github.com/)

You can see that we iterate through all parameters and simply add Gaussian noise (via *np.random.randn()*) that’s multiplied with a constant (*mutation_power*). The multiplicative factor is a hyper-parameter and loosely resembles the learning rate in gradient descent. (By the way, this method of iterating through all parameters is slow and inefficient. If you know a faster way in PyTorch, let me know in comments).

Finally, the function ***add_elite*** is as follows:

![](../_resources/e631f5b89367147e5bb80f72a84ee17d.png)

This code simply takes the top 10 agents and runs them 5 times to be doubly sure of which one is the elite based on average performance (via *return_average_score*). Then it copies the elite via *copy.deepcopy *and returns it as is (without mutation). As mentioned previously, the elite ensures that we always have a copy of our previous best and it prevents us from randomly drifting (via mutations) into a zone where there is no good agent.

**That’s it! Let’s see our evolved CartPole agent in action.**

![](../_resources/9c2918eae47b75c5285ab80fab61b248.png)![1*GnPiIBjBJjQFMrqDdj3vJw.gif](../_resources/57e0c21ffb7a6eb1fd30f4894ec3bd50.gif)

You, Sir, are a product of evolution.

Genetic Algorithms are not perfect. For example, there’s no guidance on how to choose multiplicative factor while adding Gaussian noise. You simply have to try a bunch of numbers and see which one works. Moreover, in many cases, it may fail completely. I tried multiple times evolving an agent for Pong but it was very slow and I gave up.

I contacted the author of the paper on deep neuroevolution, [Felipe Such](https://twitter.com/felipesuch?lang=en). He mentioned that for some games (including Pong) neuroevolution fails but for others (such as [Venture](https://en.wikipedia.org/wiki/Venture_%28video_game%29)) it is much faster than policy gradients.

#### What will YOU evolve?

The [code for deep neuroevolution in my repository](https://github.com/paraschopra/deepneuroevolution) is generic enough to work with any neural network implemented in PyTorch. I encourage you to try your hands at various different tasks and architectures. Please let me know if you succeed, fail or get stuck!

Good luck evolving your own world.

*PS: Check out my previous hands-on tutorials on a) *[*Generating Philosophy*](https://towardsdatascience.com/generating-new-ideas-for-machine-learning-projects-through-machine-learning-ce3fee50ec2)* from a small corpus and b) *[*Bayesian Neural Networks*](https://towardsdatascience.com/making-your-neural-network-say-i-dont-know-bayesian-nns-using-pyro-and-pytorch-b1c24e6ab8cd)

Thanks [Nirant Kasliwal](https://medium.com/@NirantK) and Felipe Such for reviewing the draft of this post.

#### Follow me on Twitter

I regularly tweet on AI, deep learning, startups, science and philosophy. Follow me on https://twitter.com/paraschopra

[**Paras Chopra (@paraschopra) | Twitter** *The latest Tweets from Paras Chopra (@paraschopra). Founder and Chairman of @Wingify | Writes on…*twitter.com](https://twitter.com/paraschopra)[(L)](https://twitter.com/paraschopra)