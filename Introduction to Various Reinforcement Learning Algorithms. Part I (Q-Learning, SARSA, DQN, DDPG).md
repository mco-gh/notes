Introduction to Various Reinforcement Learning Algorithms. Part I (Q-Learning, SARSA, DQN, DDPG)

# Introduction to Various Reinforcement Learning Algorithms. Part I (Q-Learning, SARSA, DQN, DDPG)

![1*MiN803ThUoqdCKwklZ8wwA.png](../_resources/350da7812fb3ee4067684d9074611cde.png)
![1*MiN803ThUoqdCKwklZ8wwA.png](../_resources/2d4a1898f37d7fa5c5ff01b7f9a13f11.png)

Reinforcement Learning (RL) refers to a kind of Machine Learning method in which the agent receives a delayed reward in the next time step to evaluate its previous action. It was mostly used in games (e.g. Atari, Mario), with performance on par with or even exceeding humans. Recently, as the algorithm evolves with the combination of Neural Networks, it is capable of solving more complex tasks, such as the pendulum problem:

![1*rWapNlIa0C1bXV8RgaTEmA.png](../_resources/e30b34129fb63e101c21f1be635960bc.jpg)
Deep Deterministic Policy Gradient (DDPG) Pendulum OpenAI Gym using Tensorflow

Although there are a great number of RL algorithms, there does not seem to be a comprehensive comparison between each of them. It gave me a hard time when deciding which algorithms to be applied to a specific task. This article aims to solve this problem by briefly discussing the RL setup, and providing an introduction for some of the well-known algorithms.

### 1. Reinforcement Learning 101

Typically, a RL setup is composed of two components, an agent and an environment.

![1*c3pEt4pFk0Mx684DDVsW-w.png](../_resources/f0f751b05424869a8854b37d15448d57.png)
![1*c3pEt4pFk0Mx684DDVsW-w.png](../_resources/98f1a4f564cd36fa778b8fbd245803df.png)
Reinforcement Learning Illustration (https://i.stack.imgur.com/eoeSq.png)

Then environment refers to the object that the agent is acting on (e.g. the game itself in the Atari game), while the agent represents the RL algorithm. The environment starts by sending a state to the agent, which then based on its knowledge to take an action in response to that state. After that, the environment send a pair of next state and reward back to the agent. The agent will update its knowledge with the reward returned by the environment to evaluate its last action. The loop keeps going on until the environment sends a terminal state, which ends to episode.

Most of the RL algorithms follow this pattern. In the following paragraphs, I will briefly talk about some terms used in RL to facilitate our discussion in the next section.

#### Definition

1. Action (A): All the possible moves that the agent can take
2. State (S): Current situation returned by the environment.

3. Reward (R): An immediate return send back from the environment to evaluate the last action.

4. Policy (π): The strategy that the agent employs to determine next action based on the current state.

5. Value (V): The expected long-term return with discount, as opposed to the short-term reward R.* Vπ(s)* is defined as the expected long-term return of the current state sunder policy π.

6. Q-value or action-value (Q): Q-value is similar to Value, except that it takes an extra parameter, the current action *a*. *Qπ(s, a)* refers to the long-term return of the current state *s*, taking action *a* under policy π.

#### Model-free v.s. Model-based

The model stands for the simulation of the dynamics of the environment. That is, the model learns the transition probability *T(s1|(s0, a))* from the pair of current state s*0 *and action a to the next state s*1*. If the transition probability is successfully learned, the agent will know how likely to enter a specific state given current state and action. However, model-based algorithms become impractical as the state space and action space grows (S * S * A, for a tabular setup).

On the other hand, model-free algorithms rely on trial-and-error to update its knowledge. As a result, it does not require space to store all the combination of states and actions. All the algorithms discussed in the next section fall into this category.

#### On-policy v.s. Off-policy

An on-policy agent learns the value based on its current action a, whereas its off-policy counter part learns it based on the greedy action a*. (We will talk more on that in Q-learning and SARSA)

### 2. Illustration of Various Algorithms

#### 2.1 Q-Learning

Q-Learning is an off-policy, model-free RL algorithm based on the well-known Bellman Equation:

![1*JPn8KZr7yxbQdPcr90qheA.png](../_resources/1685c3de61da5818d77b640886877106.png)
Bellman Equation (https://zhuanlan.zhihu.com/p/21378532?refer=intelligentunit)

E in the above equation refers to the expectation, while ƛ refers to the discount factor. We can re-write it in the form of Q-value:

![1*kwLmPgagp0o31nD8PmRjmg.png](../_resources/6930464b07985fb585af3f892b36a924.png)

Bellman Equation In Q-value Form (https://zhuanlan.zhihu.com/p/21378532?refer=intelligentunit)

The optimal Q-value, denoted as Q* can be expressed as:
![1*vA87bBl9ZKfsEa3W--1L6Q.png](../_resources/4315c8ea54fe6f3827ea999665a87abb.png)
Optimal Q-value (https://zhuanlan.zhihu.com/p/21378532?refer=intelligentunit)

The goal is to maximize the Q-value. Before diving into the method to optimize Q-value, I would like to discuss two value update methods that are closely related to Q-learning.

**Policy Iteration**
Policy iteration runs an loop between policy evaluation and policy improvement.
![1*PkQDd3IdcDXI4vUVwMAqKA.png](../_resources/1e5e5adc9ed2ed3eeaf2660d0a8477ba.png)

Policy Iteration (http://blog.csdn.net/songrotek/article/details/51378582)

Policy evaluation estimates the value function V with the greedy policy obtained from the last policy improvement. Policy improvement, on the other hand, updates the policy with the action that maximizes V for each of the state. The update equations are based on Bellman Equation. It keeps iterating till convergence.

![1*XuyjK3QfRqV04y--hYK87w.png](../_resources/46462cab7705800eedf4dd6ec5ea1dff.png)

Pseudo Code For Policy Iteration (http://blog.csdn.net/songrotek/article/details/51378582)

**Value Iteration**

Value Iteration only contains one component. It updates the value function V based on the Optimal Bellman Equation.

![1*py-aIXySIL28u_1_cRrHqg.png](../_resources/f76c259fd94b12ce1c7130b3c9c1462c.png)

Optimal Bellman Equation (http://blog.csdn.net/songrotek/article/details/51378582)

![1*S-a_T-k5hXYhinq9758xCQ.png](../_resources/81273770f54f4b2c5f11c79cf258d779.png)

Pseudo Code For Value Iteration (http://blog.csdn.net/songrotek/article/details/51378582)

After the iteration converges, the optimal policy is straight-forwardly derived by applying an argument-max function for all of the states.

Note that these two methods require the knowledge of the transition probability *p*, indicating that it is a model-based algorithm. However, as I mentioned earlier, model-based algorithm suffers from scalability problem. So how does Q-learning solves this problem?

![1*n9yjEWqBVZ0jw2bff9hRBw.png](../_resources/a3dd3d998c4d3eba91ca7e6df301a5d1.png)

Q-Learning Update Equation (https://www.quora.com/What-is-the-difference-between-Q-learning-and-SARSA-learning)

α refers to the learning rate (i.e. how fast are we approaching the goal). The idea behind Q-learning is highly relied on value iteration. However, the update equation is replaced with the above formula. As a result, we do not need to worry about the transition probability anymore.

![1*B8tGarFYboV9maL93sF45Q.png](../_resources/af1bd0f74b466bdb7a7755ddfed787a1.png)

Q-learning Pseudo Code (https://martin-thoma.com/images/2016/07/q-learning.png)

Note that the next action *a’* is chosen to maximize the next state’s Q-value instead of following the current policy. As a result, Q-learning belongs to the off-policy category.

#### 2.2 State-Action-Reward-State-Action (SARSA)

SARSA very much resembles Q-learning. The key difference between SARSA and Q-learning is that SARSA is an on-policy algorithm. It implies that SARSA learns the Q-value based on the action performed by the current policy instead of the greedy policy.

![1*DVtlBC0pNsW6LbDM25y7qw.png](../_resources/e61405be69a5c5323153886f8467a714.png)

SARSA Update Equation (https://www.quora.com/What-is-the-difference-between-Q-learning-and-SARSA-learning)

The action a_(t+1) is the action performed in the next state s_(t+1) under current policy.

![1*NdEQk3LeJfkzImOiQij_NA.png](../_resources/7dd5e6b10dfa9d3f23f78aaab362bc3c.png)

SARSA Pseudo Code (https://martin-thoma.com/images/2016/07/sarsa-lambda.png)

From the pseudo code above you may notice two action selection are performed, which always follows the current policy. By contrast, Q-learning has no constraint over the next action, as long as it maximizes the Q-value for the next state. Therefore, SARSA is an on-policy algorithm.

#### 2.3 Deep Q Network (DQN)

Although Q-learning is a very powerful algorithm, its main weakness is lack of generality. If you view Q-learning as updating numbers in a two-dimensional array (Action Space * State Space), it, in fact, resembles dynamic programming. This indicates that for states that the Q-learning agent has not seen before, it has no clue which action to take. In other words, Q-learning agent does not have the ability to estimate value for unseen states. To deal with this problem, DQN get rid of the two-dimensional array by introducing Neural Network.

DQN leverages a Neural Network to estimate the Q-value function. The input for the network is the current, while the output is the corresponding Q-value for each of the action.

![1*4antxYinbORGPNUElrzOUA.png](../_resources/e7367e7e674d8ee30ae35a2086cfacc0.png)

DQN Atari Example (https://zhuanlan.zhihu.com/p/25239682)

In 2013, DeepMind applied DQN to [Atari game](https://arxiv.org/pdf/1312.5602.pdf), as illustrated in the above figure. The input is the raw image of the current game situation. It went through several layers including convolutional layer as well as fully connected layer. The output is the Q-value for each of the actions that the agent can take.

The question boils down to: **How do we train the network?**

The answer is that we train the network based on the Q-learning update equation. Recall that the target Q-value for Q-learning is:

![1*VcgBin7pa2eERUxjVwvg1Q.png](../_resources/fd4f3dd834ac161f04f5df0d50ce1c36.png)

Target Q-value (https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)

The ϕ is equivalent to the state s, while the 𝜽 stands for the parameters in the Neural Network, which is not in the domain of our discussion. Thus, the loss function for the network is defined as the Squared Error between target Q-value and the Q-value output from the network.

![1*nb61CxDTTAWR1EJnbCl1cA.png](../_resources/13a3b0cb33ed344103f34377ad2c441a.png)

DQN Pseudo Code (https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)

Another two techniques are also essential for training DQN:

1. **Experience Replay**: Since training samples in typical RL setup are highly correlated, and less data-efficient, it will leads to harder convergence for the network. A way to solve the sample distribution problem is adopting experience replay. Essentially, the sample transitions are stored, which will then be randomly selected from the “transition pool” to update the knowledge.

2. **Separate Target Network**: The target Q Network has the same structure as the one that estimates value. Every C steps, according to the above pseudo code, the target network is reset to another one. Therefore, the fluctuation becomes less severe, resulting in more stable trainings.

#### 2.4 Deep Deterministic Policy Gradient (DDPG)

Although DQN achieved huge success in higher dimensional problem, such as the Atari game, the action space is still discrete. However, many tasks of interest, especially physical control tasks, the action space is continuous. If you discretize the action space too finely, you wind up having an action space that is too large. For instance, assume the degree of free random system is 10. For each of the degree, you divide the space into 4 parts. You wind up having 4¹⁰ =1048576 actions. It is also extremely hard to converge for such a large action space.

DDPG relies on the actor-critic architecture with two eponymous elements, actor and critic. An actor is used to tune the parameter 𝜽 for the policy function, i.e. decide the best action for a specific state.

![resize.jpg](../_resources/d5c0165988337787a8c3ae39a788ecc4.png)
Policy Function (https://zhuanlan.zhihu.com/p/25239682)

A critic is used for evaluating the policy function estimated by the actor according to the temporal difference (TD) error.

![1*-LcAiv5h_LEVdqIwkPNaUA.png](../_resources/867911d11aaab47b68c3a1d332574795.png)
Temporal Difference Error (http://proceedings.mlr.press/v32/silver14.pdf)

Here, the lower-case *v* denotes the policy that the actor has decided. Does it look familiar? Yes! It looks just like the Q-learning update equation! TD learning is a way to learn how to predict a value depending on future values of a given state. Q-learning is a specific type of TD learning for learning Q-value.

![1*IgGdMLe12MeWoQNkDhm0mg.png](../_resources/5d76d76234cca2a2424ccb149751b85f.png)

Actor-critic Architecture (https://arxiv.org/pdf/1509.02971.pdf)

DDPG also borrows the ideas of **experience replay** and **separate target network **from DQN **. **Another issue for DDPG is that it seldom performs exploration for actions. A solution for this is adding noise on the parameter space or the action space.

![1*kQOZZfjgTMg7fiqNOXTsOg.png](../_resources/573cfe963a481f781da6ebec81b6ed30.png)

Action Noise (left), Parameter Noise (right) (https://blog.openai.com/better-exploration-with-parameter-noise/)

It is claimed that adding on parameter space is better than on action space, according to this [article](https://blog.openai.com/better-exploration-with-parameter-noise/) written by OpenAI. One commonly used noise is [Ornstein-Uhlenbeck Random Process](http://math.stackexchange.com/questions/1287634/implementing-ornstein-uhlenbeck-in-matlab).

![1*qV8STzz6mEYIKjOXyibtrQ.png](../_resources/ed256f48e04fb2a1ca4bcec3de7a6560.png)

DDPG Pseudo Code (https://arxiv.org/pdf/1509.02971.pdf)

### 3. Conclusion

I have discussed some basic concepts of Q-learning, SARSA, DQN , and DDPG. In the next article, I will continue to discuss other state-of-the-art Reinforcement Learning algorithms, including NAF, A3C… etc. In the end, I will briefly compare each of the algorithms that I have discussed. Should you have any problem or question regarding to this article, please do not hesitate to leave a comment below or send an email to me: khuangaf@connect.ust.hk.