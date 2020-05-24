WildML

# [Learning Reinforcement Learning (with Code, Exercises and Solutions)](http://www.wildml.com/2016/10/learning-reinforcement-learning/)

**[October 2, 2016](http://www.wildml.com/2016/10/learning-reinforcement-learning/)[21 Comments](http://www.wildml.com/2016/10/learning-reinforcement-learning/#comments)**

[**Skip all the talk and go directly to the Github Repo with code and exercises.**](https://github.com/dennybritz/reinforcement-learning)

#### Why Study Reinforcement Learning

Reinforcement Learning is one of the fields I’m most excited about. Over the past few years amazing results like [learning to play Atari Games from raw pixels](http://ir.hit.edu.cn/~jguo/docs/notes/dqn-atari.pdf) and [Mastering the Game of Go](https://gogameguru.com/i/2016/03/deepmind-mastering-go.pdf) have gotten a lot of attention, but RL is also widely used in Robotics, Image Processing and Natural Language Processing.

Combining Reinforcement Learning and Deep Learning techniques works extremely well. Both fields heavily influence each other. On the Reinforcement Learning side Deep Neural Networks are used as function approximators to learn good representations, e.g. to process Atari game images or to understand the board state of Go. In the other direction, RL techniques are making their way into supervised problems usually tackled by Deep Learning. For example, RL techniques are used to implement attention mechanisms in image processing, or to optimize long-term rewards in conversational interfaces and neural translation systems. Finally, as Reinforcement Learning is concerned with making optimal decisions it has some extremely interesting parallels to human Psychology and Neuroscience (and many other fields).

With lots of open problems and opportunities for fundamental research I think we’ll be seeing multiple Reinforcement Learning breakthroughs in the coming years. And what could be more fun than teaching machines to play Starcraft and Doom?

#### How to Study Reinforcement Learning

There are many excellent Reinforcement Learning resources out there. Two I recommend the most are:

- [David Silver’s Reinforcement Learning Course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
- [Richard Sutton’s & Andrew Barto’s Reinforcement Learning: An Introduction (2nd Edition)](https://webdocs.cs.ualberta.ca/~sutton/book/bookdraft2016sep.pdf) book.

The latter is still work in progress but it’s ~80% complete. The course is based on the book so the two work quite well together. In fact, these two cover almost everything you need to know to understand most of the recent research papers. The prerequisites are basic Math and some knowledge of Machine Learning.

That covers the theory. But what about practical resources? What about actually implementing the algorithms that are covered in the book/course? That’s where this post and the [Github repository](https://github.com/dennybritz/reinforcement-learning) comes in. I’ve tried to implement most of the standard Reinforcement Algorithms using Python, [OpenAI Gym](https://gym.openai.com/) and Tensorflow. I separated them into chapters (with brief summaries) and exercises and solutions so that you can use them to supplement the theoretical material above. [All of this is in the Github repository](https://github.com/dennybritz/reinforcement-learning).

Some of the more time-intensive algorithms are still work in progress, so feel free to contribute. I’ll update this post as I implement them.

#### Table of Contents

- [Introduction to RL problems, OpenAI gym](https://github.com/dennybritz/reinforcement-learning/tree/master/Introduction/)
- [MDPs and Bellman Equations](https://github.com/dennybritz/reinforcement-learning/tree/master/MDP/)
- [Dynamic Programming: Model-Based RL, Policy Iteration and Value Iteration](https://github.com/dennybritz/reinforcement-learning/tree/master/DP/)
- [Monte Carlo Model-Free Prediction & Control](https://github.com/dennybritz/reinforcement-learning/tree/master/MC/)
- [Temporal Difference Model-Free Prediction & Control](https://github.com/dennybritz/reinforcement-learning/tree/master/TD/)
- [Function Approximation](https://github.com/dennybritz/reinforcement-learning/tree/master/FA/)
- [Deep Q Learning](https://github.com/dennybritz/reinforcement-learning/tree/master/DQN/) (WIP)
- [Policy Gradient Methods](https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient/) (WIP)
- Learning and Planning (WIP)
- Exploration and Exploitation (WIP)

#### List of Implemented Algorithms

- [Dynamic Programming Policy Evaluation](https://github.com/dennybritz/reinforcement-learning/tree/master/DP/Policy%20Evaluation%20Solution.ipynb)
- [Dynamic Programming Policy Iteration](https://github.com/dennybritz/reinforcement-learning/tree/master/DP/Policy%20Iteration%20Solution.ipynb)
- [Dynamic Programming Value Iteration](https://github.com/dennybritz/reinforcement-learning/tree/master/DP/Value%20Iteration%20Solution.ipynb)
- [Monte Carlo Prediction](https://github.com/dennybritz/reinforcement-learning/tree/master/MC/MC%20Prediction%20Solution.ipynb)
- [Monte Carlo Control with Epsilon-Greedy Policies](https://github.com/dennybritz/reinforcement-learning/tree/master/MC/MC%20Control%20with%20Epsilon-Greedy%20Policies%20Solution.ipynb)
- [Monte Carlo Off-Policy Control with Importance Sampling](https://github.com/dennybritz/reinforcement-learning/tree/master/MC/Off-Policy%20MC%20Control%20with%20Weighted%20Importance%20Sampling%20Solution.ipynb)
- [SARSA (On Policy TD Learning)](https://github.com/dennybritz/reinforcement-learning/tree/master/TD/SARSA%20Solution.ipynb)
- [Q-Learning (Off Policy TD Learning)](https://github.com/dennybritz/reinforcement-learning/tree/master/TD/Q-Learning%20Solution.ipynb)
- [Q-Learning with Linear Function Approximation](https://github.com/dennybritz/reinforcement-learning/tree/master/FA/Q-Learning%20with%20Value%20Function%20Approximation%20Solution.ipynb)
- [Deep Q-Learning for Atari Games](https://github.com/dennybritz/reinforcement-learning/tree/master/DQN/Deep%20Q%20Learning%20Solution.ipynb)
- [Double Deep-Q Learning for Atari Games](https://github.com/dennybritz/reinforcement-learning/tree/master/DQN/Double%20DQN%20Solution.ipynb)
- Deep Q-Learning with Prioritized Experience Replay (WIP)
- [Policy Gradient: REINFORCE with Baseline](https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient/CliffWalk%20REINFORCE%20with%20Baseline%20Solution.ipynb)
- [Policy Gradient: Actor Critic with Baseline](https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient/CliffWalk%20Actor%20Critic%20Solution.ipynb)
- [Policy Gradient: Actor Critic with Baseline for Continuous Action Spaces](https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient/Continuous%20MountainCar%20Actor%20Critic%20Solution.ipynb)
- Deterministic Policy Gradients for Continuous Action Spaces (WIP)
- Deep Deterministic Policy Gradients (DDPG) (WIP)
- Asynchronous Advantage Actor Critic (A3C) (WIP)