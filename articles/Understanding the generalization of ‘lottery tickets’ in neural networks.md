Understanding the generalization of ‘lottery tickets’ in neural networks

# Understanding the generalization of ‘lottery tickets’ in neural networks

November 25, 2019
Written by
Ari Morcos, Yuandong Tian

Share

[ ![49677251_224845165108670_5875028237406437376_n.png](../_resources/80b4ce80909efba0304d88969ac5f873.png)  ![49780062_2239882272955938_7957149939224543232_n.png](../_resources/544005436f43d734b3e9cdfb46eb3ed0.png)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fai.facebook.com%2Fblog%2Funderstanding-the-generalization-of-lottery-tickets-in-neural-networks%2F)

[ ![49661799_326312694636292_7293370538993385472_n.png](../_resources/b166a0e4487b7d111bd20a0038c00760.png)  ![49634112_369201477192293_9127330224449519616_n.png](../_resources/54b6ddfc9eae9f62c96d2b8254543cf7.png)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Ftext%3DUnderstanding%2Bthe%2Bgeneralization%2Bof%2B%25E2%2580%2598lottery%2Btickets%25E2%2580%2599%2Bin%2Bneural%2Bnetworks%2Bhttps%253A%252F%252Fai.facebook.com%252Fblog%252Funderstanding-the-generalization-of-lottery-tickets-in-neural-networks%252F&h=AT1mB__ffojn0KTeMEIeOMArLYCJyrRqPcYQ_xTQbCRfcYh1KsLOaA0y_Vr9mkcbWYsfdfi6z7o1ia6df_mMGZKmESuCnyx-d0E-gX8Bf8XsxyBqRMUOvlm4a_tznUlIYuSqBB8xec-uDPe5jlwAALp863M)

The lottery ticket hypothesis, initially proposed by researchers Jonathan Frankle and Michael Carbin at MIT, suggests that by training deep neural networks (DNNs) from [“lucky”](https://l.facebook.com/l.php?u=https%3A%2F%2Farxiv.org%2Fabs%2F1803.03635&h=AT3UPUFc0zmBHXeZFbIM8-Tov65XVefvrolhwcxHPHAIR6_5m1guWNR0hsFhqE1PZEMyJH8rJzVPmCeXlGNVZoXV6eO7H-EtoFkMlnb8uz2mO-3f_QAVeoeMgznUKs7bop0QbfldJbABpiriyUar1nzPCWg) initializations, often referred to as "winning lottery tickets,” we can train networks which are 10-100x smaller with minimal losses --- or even while achieving gains --- in performance. This work has exciting implications for potentially finding ways to not only train with fewer resources, but also run faster inference of models on smaller devices, like smartphones and VR headsets. But the lottery ticket hypothesis is not yet fully understood by the AI community. In particular, it has remained unclear whether winning tickets are dependent on specific factors or rather represent an intrinsic feature of DNNs.

New research from Facebook AI finds the first definitive evidence that lottery tickets generalize across related, but distinct datasets and can extend to reinforcement learning (RL) and natural language processing (NLP). We’re sharing details on the results of our experiments using winning tickets, and we’re also introducing a new theoretical framework on the formation of lottery tickets to help researchers advance toward a better understanding of lucky initializations.

## A brief primer on ‘winning lottery tickets’

The standard approach to training and compressing DNNs involves tweaking millions of parameters in a neural network and then removing or “pruning” the unnecessary weights to reduce the network structure to a more manageable size. Reducing the model size helps minimize its memory, inference, and computation requirements. A number of studies have found that many of the weights within a trained neural network can be pruned by sometimes as much as 99 percent, yielding much smaller, sparsified networks.

The lottery ticket hypothesis flips DNN pruning on its head with this core motivation: rather than training big networks and reducing them to smaller networks, can we identify and train the optimal small networks from the start?

0:00

To find the winning tickets, we train a full network using random initializations, prune the model while retaining its performance, and then reset (or rewind) the sub-network to the initializations before training began. To evaluate the winning tickets, we compare them with random tickets and find that the winning tickets (or lucky initializations) perform better.

As we increase the network size, we combinatorially increase the number of possible subnetworks, which means there’s a higher probability that a lucky subnetwork initialization exists. The lottery ticket hypothesis suggests that if we can find this lucky subnetwork, we can train small, sparsified networks to high performance, even when more than 90 percent of the full network’s parameters are removed. However, finding winning tickets requires significant computational resources since models must be trained and retrained many times, making generalization across problem settings a key criterion to be useful in improving deep neural networks.

## Generalizing across datasets and optimizers

Researchers have, thus far, only tested this hypothesis on the exact same problems used to find the winning tickets in the original research paper, partially because of the computational power required to find winning tickets under new settings.

[In a paper that we’re presenting at NeurIPS this year](https://l.facebook.com/l.php?u=https%3A%2F%2Farxiv.org%2Fabs%2F1906.02773&h=AT3iRlrqaC8HBzfJ7AeIIpAhc1cS-ALdc0PLpcr2_wqNLQcvA9IvoQsxEEb3grC6frJuSHUl_7hk_0jh5znpgGANPLLy2B-f8mzxWKYzPAIIUE82g7_9I4kAJnouqEh9Gc3U4ZQYDh5LoFWcpa1s7DXdfi8), we evaluated the generality of winning ticket initializations across six different natural image datasets and optimizers. Encouragingly, we found that winning tickets generalized across related, but distinct datasets. Similarly, we also found that winning tickets generalized across different optimizers, suggesting that winning ticket initializations are largely optimizer-independent.

In order to measure the generality of winning tickets, we generate winning tickets in one source training configuration and evaluate performance in a different target configuration. For example, we might generate a winning ticket using the CIFAR-10 dataset (the source configuration) and evaluate its performance on the ImageNet dataset (the target configuration). Through rigorous experiments across a range of different settings, we observed that winning tickets generalized across distinct image datasets. Interestingly, we also observed that winning tickets generated by large data sets (such as ImageNet and Places365) consistently transferred much better than on small data sets (such as CIFAR-10).

![75586226_512994716097669_4712646320005840896_n.jpg](../_resources/d6c0f4a7ab2927b8d38b71669f842d53.jpg)

These plots show how our object classification model’s winning tickets transfer across large (ImageNet and Places365) and small (CIFAR-10/CIFAR-100) datasets. Within each plot, each line represents a different source dataset for the winning ticket. Winning tickets generated on ImageNet and Places365 consistently outperformed those generated on smaller datasets.

These results suggest that larger data sets encourage more generic winning tickets than smaller data sets. We also found that winning tickets generated on data sets with the same number of training examples — but different numbers of classes — also varied in performance. More classes seems to generalize better (e.g., compare the performance of CIFAR-10 and CIFAR-100 winning tickets, which have 10 and 100 classes, respectively).

This research shows that winning tickets contain generic properties that improve deep neural network training, regardless of the precise problem. This unlocks the possibility of generating a small number of such winning tickets and using them across different tasks and environments for significantly more efficient training. (For more details, read the full paper: [One ticket to win them all: Generalizing lottery ticket initializations across data sets and optimizers)](https://arxiv.org/pdf/1906.02773.pdf).

## Generalizing to other domains and learning methods: RL and NLP

So far, the lottery ticket phenomenon has only been tested in the context of supervised learning for vision-centric classification tasks, which leaves a critical open question — do they only exist in supervised learning methods, or what if it’s merely a quirk of image classification domain? If the lottery ticket phenomenon represents a fundamental property of DNNs, winning tickets should be present in vastly different domains and learning settings.

[We recently explored these questions](https://l.facebook.com/l.php?u=https%3A%2F%2Farxiv.org%2Fabs%2F1906.02768&h=AT3y0y0siQhmbG-UE2jalW9h3KRQBxFJ-wkGTBps93rSYWUuYWQq4UjBDGqCt4jgti2Z_FaYXIR_7Qoe9F8eeiJye8M7WTwg0EfMakDOwlBOaBU0INd9dymhRInrqLyT6E1FiK1qzXm3GcWZeofECZfgYcw) and found the lottery ticket phenomenon is also present across both RL and NLP. For RL, we analyzed a set of classic control tasks and Atari games; for NLP, we studied classic long short-term memory (LSTM) language models and the more recently developed Transformer models trained on machine translation. We focused on tasks that have substantial differences from the initial paradigms and architectures used for image classification and supervised learning. For instance, in RL the data distribution shifts as the agent learns from often sparse reward signals, which significantly modifies the optimization process and the resultant networks. In NLP tasks, DNNs need to model temporal dynamics, which are absent in supervised image classification.

Consistent with prior work in supervised image classification, we confirm that winning tickets outperform the standard random subnetwork initializations for both RL and NLP problems, even at extreme pruning rates. For RL, we found that winning tickets substantially outperformed random tickets on classic control problems and on many, but not all, Atari games.

![75542605_945176592515240_5416705851979202560_n.jpg](../_resources/63039379358945515e0d61e454cf01f6.jpg)

Winning ticket initialization performance for Transformer models trained on machine translation

For NLP models, we found winning tickets to be present in both LSTMs trained on language modeling tasks and Transformers trained on machine translation tasks. Strikingly, we found that extremely large Transformer models with more than 200 million parameters can be trained from scratch to near-equivalent performance with only a third of the weights remaining. This result suggests that it may be possible to build and train from scratch attention-based language models that are substantially sparsified enough to fit on small devices.

Together, these results demonstrate that the lottery ticket phenomenon is not simply an artifact of image classification but rather represents a phenomenon in the broader field of deep neural networks (DNN). (For details on these experiments, read the full paper: [Playing the lottery with rewards and multiple languages: lottery tickets in RL and NLP.](https://arxiv.org/pdf/1906.02768.pdf))

## Advancing toward a deeper understanding of ‘winning tickets’

These research studies help demonstrate that lottery tickets can exist beyond their precise conditions in the original research paper, which provides more incentive to deepen our understanding of lucky initializations. Empirical experimentation, however, can be anecdotal. And there are many more open questions about the underlying properties and behaviors of neural networks, such as how do these winning tickets form, why do they exist, and how do they work?

To begin to analyze these questions in the context of deep ReLU networks, we used a student-teacher setting, in which a larger student network must learn to mimic exactly what the smaller teacher is doing. Since we can define the teacher network with fixed parameters in this setting, we can quantitatively measure the student network’s learning progress, and, critical to our investigation of lottery tickets, how the student network’s initialization affects the learning process.

In the student-teacher setting, we see that after training, the activity patterns of select student neurons correlate more strongly with those of teacher neurons than with the activity of other student neurons --- a concept that is referred to as “student specialization.” This stronger correlation suggests that, during training, the student network not only learns the teacher’s network output but also the internal structure of the teacher by mimicking individual teacher neurons.

In our analysis, [we show this occurrence happens](https://l.facebook.com/l.php?u=https%3A%2F%2Farxiv.org%2Fpdf%2F1905.13405.pdf&h=AT1Rj7bRFXJRLegvs-4GU7YOHHl7HxhVvoGWjlH-9otCE5uU_ovFuTCpSqCXiPIYFo_H3B2xhEhSJCrpKHj28K0t_9N-QWF7_6XO0aEAW1UzbWPWfR8j1zG3q0bz_db63-oBItD9KcaANP_2CKUOa05w0-w) locally in a 2-layer ReLU network: if the initial weights of a student neuron happen to be similar to those of some teacher neurons, then specialization will follow. The size of the neural network is important because the larger the student network, the more likely that one of the student neurons will start out close enough to a teacher neuron to learn to mimic its activity during training. What’s more, if a student neuron’s initial activation region has a more substantial overlap with a teacher neuron, then that student neuron specializes faster. This behavior corroborates the lottery ticket hypothesis, which similarly proposes that some lucky subset of initializations exist within neural networks, and “winning tickets” are the lucky student neurons that happen to be in the right location at the beginning of training.

[In our follow-up research,](https://l.facebook.com/l.php?u=https%3A%2F%2Farxiv.org%2Fabs%2F1909.13458&h=AT3aSL2AP_uuVBBajVfRxwYakrt3eIET7n2ce0ZfPReEbZCxMI0D1fYmY1mJ0hp3qwLvAmsrvfb4PbOj5SlPkkOwLxaVY01mzolzEwt1bds8b3p3Vy74ikjbmkaNfLaSohsMVSrI3iOsuuNbZy66glxN-X4)we strengthen our results by removing many mathematical assumptions, including independent activations and locality, and still prove that student specialization happens in the lowest layer in deep ReLU networks after training. From our analysis, we find certain mathematical properties in the training dynamics resonate with the lottery ticket phenomenon: those weights with a slight advantage in the initialization may have a greater chance of being the winning tickets after training converges.

With our teacher-student paradigm, we’ve been able to demonstrate the lottery ticket behavior of lucky initializations mathematically --- beyond empirical experimentation.

##  Future, open questions for the lottery ticket hypothesis

The lottery ticket hypothesis is an exciting and potentially powerful lens through which we can both better understand and improve DNNs.

Through this series of studies and theoretical analyses, we have demonstrated that the lottery ticket effect can occur across a variety of different domains, that winning ticket initializations have the capacity to generalize across distinct, related datasets, and, more generally, that they have more potential than researchers previously understood. If we can find a way to identify the winning tickets from the start of training, we could not only build powerful deep learning systems with a fraction of the computational resources we use today but also use these techniques to improve the performance of our largest networks.

While our research has demonstrated generalization and our theoretical framework helps more concretely corroborate this phenomenon, this is an active area of research, and many questions remain unanswered. Are winning tickets label-dependent or simply dependent on the data distribution? How can we generate winning tickets more efficiently? Is it possible to transfer winning tickets across architectures? And perhaps most interestingly, what makes winning tickets special? We hope that our work will spur future investigations, both by us and others, to explore these open questions.

## Written by

Ari Morcos
Research Scientist
Yuandong Tian
Research Scientist

## Related posts

[PHYRE: A new AI benchmark for physical reasoning](https://ai.facebook.com/blog/phyre-a-new-ai-benchmark-for-physical-reasoning/)

August 15, 2019

[Using AI to create thinner, more efficient anti-reflective coatings](https://ai.facebook.com/blog/using-ai-to-create-anti-reflective-coatings/)

August 09, 2019

[Making Transformer networks simpler and more efficient](https://ai.facebook.com/blog/making-transformer-networks-simpler-and-more-efficient/)

August 23, 2019

## Related Tags

[Research](https://ai.facebook.com/blog/results/research/)