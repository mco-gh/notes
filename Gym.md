Gym

###

Open source interface to reinforcement learning tasks.

The [gym](https://github.com/openai/gym) library provides an easy-to-use suite of reinforcement learning tasks.

	import gym
	env = gym.make(["CartPole-v1"](https://gym.openai.com/envs/CartPole-v1))
	observation = env.reset()
	for _ in range(1000):
	  env.render()
	  **action = env.action_space.sample() *# your agent here (this takes random actions)***
	  observation, reward, done, info = env.step(action) if done:

observation = env.reset()
env.close()

###

We provide the environment; you provide the algorithm.

You can write your agent using your existing numerical computation library, such as TensorFlow or Theano.