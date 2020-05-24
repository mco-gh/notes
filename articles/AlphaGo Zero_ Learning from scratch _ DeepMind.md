AlphaGo Zero: Learning from scratch | DeepMind

 ![AlphaGoZero-Illustration-WideScre.2e16d0ba.fill-1900x700_QZjBfoV.jpg](../_resources/125dee743c7bef37c6bcc615df972fff.jpg)

# AlphaGo Zero: Learning from scratch

**Artificial intelligence research has made rapid progress in a wide variety of domains from speech recognition and image classification to genomics and drug discovery. In many cases, these are specialist systems that leverage enormous amounts of human expertise and data.**

However, for some problems this human knowledge may be too expensive, too unreliable or simply unavailable. As a result, a long-standing ambition of AI research is to bypass this step, creating algorithms that achieve superhuman performance in the most challenging domains with no human input. In our most recent [paper](http://nature.com/articles/doi:10.1038/nature24270), published in the [journal Nature](https://www.nature.com/), we demonstrate a significant step towards this goal.

#        Starting from scratch

 ![AlphaGoZero-Illustration-WideScreen.width-1100_sbr8040.jpg](../_resources/8a0728a5d99a9ba087eba6d0ddf3043d.jpg)

The paper introduces AlphaGo Zero, the latest evolution of [AlphaGo](https://deepmind.com/research/alphago/), the first computer program to defeat a world champion at the ancient Chinese game of Go. Zero is even more powerful and is arguably the strongest Go player in history.

Previous versions of AlphaGo initially trained on thousands of human amateur and professional games to learn how to play Go. AlphaGo Zero skips this step and learns to play simply by playing games against itself, starting from completely random play. In doing so, it quickly surpassed human level of play and defeated the [previously published](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html?foxtrotcallback=true) champion-defeating version of AlphaGo by 100 games to 0.

 ![TrainingTime-Graph-171019-r01.gif](../_resources/325c09139703bdcdd62fbeaffd588447.gif)

It is able to do this by using a novel form of [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), in which AlphaGo Zero becomes its own teacher. The system starts off with a neural network that knows nothing about the game of Go. It then plays games against itself, by combining this neural network with a powerful search algorithm. As it plays, the neural network is tuned and updated to predict moves, as well as the eventual winner of the games.

This updated neural network is then recombined with the search algorithm to create a new, stronger version of AlphaGo Zero, and the process begins again. In each iteration, the performance of the system improves by a small amount, and the quality of the self-play games increases, leading to more and more accurate neural networks and ever stronger versions of AlphaGo Zero.

This technique is more powerful than previous versions of AlphaGo because it is no longer constrained by the limits of human knowledge. Instead, it is able to learn tabula rasa from the strongest player in the world: AlphaGo itself.

It also differs from previous versions in other notable ways.

- AlphaGo Zero only uses the black and white stones from the Go board as its input, whereas previous versions of AlphaGo included a small number of hand-engineered features.
- It uses one neural network rather than two. Earlier versions of AlphaGo used a “policy network” to select the next move to play and a ”value network” to predict the winner of the game from each position. These are combined in AlphaGo Zero, allowing it to be trained and evaluated more efficiently.
- AlphaGo Zero does not use “rollouts” - fast, random games used by other Go programs to predict which player will win from the current board position. Instead, it relies on its high quality neural networks to evaluate positions.

All of these differences help improve the performance of the system and make it more general. But it is the algorithmic change that makes the system much more powerful and efficient.

 ![AlphaGo%20Efficiency.width-1500_lNrnvzH.png](../_resources/0fb3c76e420fe212f810db9e073516df.png)

AlphaGo has become progressively more efficient thanks to hardware gains and more recently algorithmic advances

After just three days of self-play training, AlphaGo Zero emphatically defeated the previously [published version of AlphaGo](https://research.googleblog.com/2016/01/alphago-mastering-ancient-game-of-go.html) - which had itself [defeated 18-time world champion Lee Sedol](https://deepmind.com/research/alphago/alphago-korea/) - by 100 games to 0. After 40 days of self training, AlphaGo Zero became even stronger, outperforming the version of AlphaGo known as “Master”, which has defeated the world's best players and [world number one Ke Jie](https://deepmind.com/research/alphago/alphago-china/).

 ![Elo%20Ratings.width-1500_RlCX918.png](../_resources/68ea17e7e553652e90eb18528d02a7b8.png)

Elo ratings - a measure of the relative skill levels of players in competitive games such as Go - show how AlphaGo has become progressively stronger during its development

Over the course of millions of AlphaGo vs AlphaGo games, the system progressively learned the game of Go from scratch, accumulating thousands of years of human knowledge during a period of just a few days. AlphaGo Zero also discovered new knowledge, developing unconventional strategies and creative new moves that echoed and surpassed the novel techniques it played in the games against Lee Sedol and Ke Jie.

 ![Knowledge%20Timeline.gif](../_resources/1a4fd20fa6b60055aaf593d99b3536d2.gif)

These moments of creativity give us confidence that AI will be a multiplier for human ingenuity, helping us with [our mission](https://deepmind.com/about/) to solve some of the most important challenges humanity is facing.

#        Discovering new knowledge

 ![AlphaGoZero-Illustration-Square.width-1100_CHPOv4V.jpg](../_resources/f90cea159daf21d27e39dce8c7d7c57f.jpg)

While it is still early days, AlphaGo Zero constitutes a critical step towards this goal. If similar techniques can be applied to other structured problems, such as protein folding, reducing energy consumption or searching for revolutionary new materials, the resulting breakthroughs have the potential to positively impact society.

* * *

Read [the paper](https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ)

Read the accompanying [Nature News and Views article](https://www.nature.com/articles/550336a.epdf?shared_access_token=QbXlOw9nSIP_MS1moc_M0tRgN0jAjWel9jnR3ZoTv0PvinEKRXS2Dk736vL8i-Uo2-6AN8KRxOlLhDGorUgFzEgC3fwrX95r3LQ7u2FBwQ5axjmpMSZrWg4i6D7_g5rV5ze0zLhgo4jufsSKL-UZmw%3D%3D)

Download [AlphaGo Zero games](http://www.alphago-games.com/)
Read [more about AlphaGo](https://deepmind.com/research/alphago/)

***This work was done by David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy Lillicrap, Fan Hui, Laurent Sifre, George van den Driessche, Thore Graepel and Demis Hassabis.***

 Share Article

- [(L)](http://twitter.com/intent/tweet/?text=&url=https%3A//deepmind.com/blog/alphago-zero-learning-scratch/)

- [(L)](http://www.facebook.com/share.php?u=https%3A//deepmind.com/blog/alphago-zero-learning-scratch/&t=)

- [(L)](https://plus.google.com/share?url=https%3A//deepmind.com/blog/alphago-zero-learning-scratch/)

- [(L)](https://deepmind.com/blog/alphago-zero-learning-scratch/mailto:?subject=AlphaGo%20Zero%3A%20Learning%20from%20scratch&body=%0D%0A%0D%0Ahttps%3A//deepmind.com/blog/alphago-zero-learning-scratch/)

-

Authors
  Wednesday, 18 October 2017

- ![DemisHassabis.2e16d0ba.fill-80x80_sxeEpKu.jpg](../_resources/fcc6adf1e120f5dc93cbe36beff7f1e7.jpg)

 Demis Hassabis
 Co-Founder & CEO, DeepMind

- ![image.2e16d0ba.fill-80x80_qlergrD.png](../_resources/15a0aec6756265d0ebd79e6dbeeb09fc.png)

 David Silver
 Research Scientist, DeepMind