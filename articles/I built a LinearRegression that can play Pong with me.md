I built a LinearRegression that can play Pong with me.

# I built a LinearRegression that can play Pong with me.

A naive way of creating something towards AI. It’s pretty cool.

Do you remember that vintage video game pong? Just two pads and a ball that wasn’t actually round? It looked a bit like this.

![](../_resources/7d82dfa4413b7062e2ebf2c57eb93614.png)![1*YUE6mc-PzTlnkZYFZi5zlw.jpeg](../_resources/0211873e999bc9d07032928046bf9435.jpg)

Starting positions of the three main objects in Pong. RetroFun.

Some years ago, DeepMind built a super cool [model](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) that could play 7 different Atari classics. What they did was awesome mainly because they used raw pixel data. This is a very purist approach, skipping the handcrafting feature phase in traditional Machine Learning, on Deep Learning that I find fascinating. With the right tools, this is a more powerful way than building handcrafted features.

This breakthrough got me wondering: “This super deep complex model can actually play a video game and outperform humans. But! Can a very simple model be enough to play decently against another human?”

#### Timeline note

Back when I had this idea, my skills were not enough to bring this to code but now things are different and thanks to amazing Python I could tackle it in little under seven days.

* * *

*...*

### Enter Linear Regression and Pong.

Let’s think simple. A very simple game: Pong. A very simple, if not the most simple, model: Linear Regression. Good. It actually seemed pretty straight forward:

- •Input data: Raw pixels of the screen at each frame.
- •Variable to predict: Position of the pad at each frame.
- •Model: ElasticNet* Linear Regression

* (fancy way of saying linear combination of Lasso and Ridge regularization)

In my head this sounded like a classical supervised learning problem. So, how should I go about it?

1. 1Get a working Pong framework.

2. 2Adapt code to gather data, train the model and deploy it the video game environment.

3. 3Gather the, all mighty, data by actually playing a couple of games.
4. 4Train a linear regression model.
5. 5Test the model with validation data.

6. 6Deploy it on the video game’s, naturally dynamic, environment and find out if it can perform.

Simple? Yes and no. Indeed I did all that but there were some interesting plot twists I found interesting and worth sharing.

#### Plot twist 1: Data Gathering

While requesting the pixel raw data using [***pygame***](https://www.pygame.org/news) is quite easy, gathering the right data required a bit more thought. After gathering raw data out of a few games. I set myself to train the linear regression. Even though the model was *‘big’, *flattened images of 400 x 400, the cool [SciKit-Learn](http://scikit-learn.org/stable/) module was up for the challenge of fitting the data and even do [cross-validation](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html). But as I would realize after releasing it on the dynamic environment, this first model would not be enough to have a smart opponent. The opponent would actually move very little from it’s original position. Why? The answer in the following plot twists.

#### Plot twist 2: Raw not so raw data

Given that the first model did not succeed (I wasn’t expecting it to but I wasn’t expecting to basically stay put in the initial position!), I conditioned the data gathering a little bit. You see, raw data and the purist approach is good but not for these traditional ML techniques, you have to do a bit of work for them. So, the tricks I implemented to help it out:

- •Remove noise in the data caused by the opponent’s pad.
- •Gather data only when the ball is on one half of the court, the player to replicate’s half.

These conditions seemed fair enough so that I could tell myself I wasn’t building handcrafted features but also enough so that the model could fairly play. While my first point could be true, the latter one wasn’t. The model would, again, stay very close to the initial position in the dynamic environment! What’s going on?! This was really confusing me since, on the static environment, outside of the game, the mean absolute error wasn’t big enough for the pad not to hit the ball.

#### Plot twist3: The answer is in the data

In ML you always hope that the answer/variable you are trying to predict is* ‘inside’* the data you’ll use as predictors or independent variables (if that wasn’t the case then why use them at all?). And while that might be true, sometimes, like this time, you don’t always want to provide it in a way that it’s actually biasing your model. That was my case until this point, the variable to predict was the position of the pad and the *‘answer’* was always encoded in the data: the pixels provided. So when deployed on the dynamic environment (predict position, draw frame, predict position, draw frame…) this was causing the model to stay really close to the initial position. It’s kind of counter intuitive but it makes sense to why the pad wouldn’t move enough to bounce the ball away.

By removing the pixels that included both pads from the input data, [*caeteris paribus*](https://en.wikipedia.org/wiki/Ceteris_paribus)*, *the model would move more ‘*freely*’ in the dynamic environment. Success! Only not yet, it still didn’t play well enough so that you could play against it and not beat it like you would a one year old.

#### Plot twist 4: Is it coming or going?

After thinking what else did the model need to play fairly good (hit the ball in most angles) I realized that by feeding a single frame as input data, it’s difficult (more like impossible, even for you) to tell if the ball is moving towards or away from the end zone. This was causing the model to make a best guess but since it’s basically learning from previous behaviors (my behaviors) it can only do so much.

![](../_resources/9081602f9d3be7e9fa978892a934d302.png)![1*AgkGG3opLuSQdZr_0ZL-Ig.jpeg](../_resources/a05560abb939eaf8e69c5b04e4bc0245.jpg)

Away or towards the pad?

What does the model need to capture that sense of direction? More data, sequential data: windows of frames. Instead of feeding a single frame to the model, I transformed the dataset into a sequential one: providing the model three consecutive frames per training example.

This really hit the nail on the head, this last conditioning of the data made the model work quite ok for my purposes: demonstrate that a simple model can play against a human. It’s a bit choppy but does the job. As you can imagine, I’m the one on the right playing agains the guy on the left.

![](../_resources/95d60e6cdb0b29954245ee17803e8569.png)

Me vs a Linear Regression

#### A few final thoughts

- •Since this is a supervised approach, the performance depends on the data you gather and then train your model with it. But what if the data is from someone that sucks at playing pong? Well the model won’t perform very well, this is why using a [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning) approach makes a lot of sense for video game playing “AIs”.
- •The formulation / model I present here actually has a bit of an advantage against a human, theoretically, : it can predict a position for the pad to move and the pad controlled by a human is limited to how much can the pad move given the speed of the pad when pressing a key.
- •Following on the previous point, an alternative (more “fair” approach) could be to formulate the problem as classification one. Predict one out of three options: press the key to move up, press the key to move down or not move at all at each frame.

This was a very interesting and complete problem from a Data Science / Machine Learning point of view:

1. 1You need to write code.
2. 2Analyze data and transform data.
3. 3Train, validate and choose models

4. 4Deploy them into an application to react intelligently in order to perform a task.

You can find the code [**here**](https://github.com/DiegoAgher/learnPongPython) to play, gather data, train a model and play against an artificial player that imitates your pong style!

PS: PR’s are welcomed (: