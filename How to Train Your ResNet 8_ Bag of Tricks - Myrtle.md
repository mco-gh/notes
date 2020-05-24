How to Train Your ResNet 8: Bag of Tricks - Myrtle

 [![Myrtle-Logo-3.png](../_resources/884bd9feb30668af959222b3cc97a7f0.png)](https://myrtle.ai/)

- [Home](https://myrtle.ai/)
- [Company](https://myrtle.ai/company/)
- [Partners](https://myrtle.ai/partners/)
- [Solutions](https://myrtle.ai/solutions/)
- [Learn](https://myrtle.ai/learn/)
- [Join](https://myrtle.ai/join/)

 [**](https://www.linkedin.com/company/myrtle-software)  [**](https://twitter.com/myrtlesoftware?lang=en)

# How to Train Your ResNet 8: Bag of Tricks

In the final post of the series we come full circle, speeding up our single-GPU training implementation to take on a field of multi-GPU competitors. We roll-out a bag of standard and not-so-standard tricks to reduce training time to 34s, or 26s with test-time augmentation.

 [![chevron-left-light.png](../_resources/2609b765453311c021015eb29034713a.png)](https://myrtle.ai/how-to-train-your-resnet-7-batch-norm/)  [![grid-light.png](../_resources/875ff7a2f09ffa47e0d269b1ecf22673.png)](https://myrtle.ai/learn)[![chevron-right-light.png](../_resources/6f246a3b8b15c1ce0d4577c157717a88.png)](https://myrtle.ai/wavenet/)

David Page

 Chief Scientist
August 19, 2019

Note: this post is also available as Colab notebook [here](https://colab.research.google.com/github/davidcpage/cifar10-fast/blob/master/bag_of_tricks.ipynb).

Whilst we’ve been otherwise occupied – investigating [hyperparameter tuning](https://myrtle.ai/learn/how-to-train-your-resnet-5-hyperparameters/), [weight decay](https://myrtle.ai/learn/how-to-train-your-resnet-6-weight-decay/) and [batch norm](https://myrtle.ai/learn/how-to-train-your-resnet-7-batch-norm/) – our entry for training CIFAR10 to 94% test accuracy has slipped five (!) places on the DAWNBench leaderboard:

![DAWNBench_leaderboard-768x443.jpg](../_resources/6ff41e9d8258875210b6314d9ce46894.jpg)

The top six entries all use 9-layer ResNets which are cousins – or twins – of the network we developed [earlier in the series](https://myrtle.ai/learn/how-to-train-your-resnet-4-architecture/). First place is a 4-GPU implementation from Kakao Brain which completes in an impressive 37s. The single-GPU version of the same comes in third with 68s, an apparent 7s improvement over our single-GPU entry from last year, although close inspection shows that these submissions are using test-time augmentation (TTA). We shall discuss the validity of this approach towards the end of the post (our conclusion is that any reasonable restriction should be based on total inference cost and that the form of mild TTA used here, along with a lightweight network, passes on that front.) Note that our earlier submission, allowing the same TTA, would achieve a time of 60s on a 19 epoch training schedule without further changes.

By the end of the post our single-GPU implementation surpasses the top multi-GPU times comfortably, reclaiming the coveted DAWNBench crown with a time of 34s and achieving a 10× improvement over the single-GPU state-of-the-art at the start of the series! Using the same TTA employed by the Kakao Brain submission, this drops to 26s. We achieve these times by accumulating a series of small (typically 0.1-0.3% in absolute test accuracy) improvements, which can be traded for shorter training times. These improvements are based on a collection of standard and not-so-standard tricks.

Our main weapon is statistical significance. The standard deviation in test accuracy for a single training run is roughly 0.15% and when comparing between two runs we need to multiply this by √22. This is larger than many of the effects that we are measuring. Given that training times soon drop below a minute, we can afford to run experiments 10s-100s of times to make sure that improvements are real and this allows us to make consistent progress.

Sharp experimental results are essential to advancing the field but if a baseline is poorly-tuned or the number of runs too few, experimental validation holds little value. The main goal of today’s post is to provide a well-tuned baseline on which to test novel techniques, allowing one to complete a statistically significant number of training runs within minutes on a single GPU. We confirm, at the end of the post, that improvements in training speed translate into improvements in final accuracy if training is allowed to proceed towards convergence.

### Preprocessing on the GPU (70s)

We start with the practical matter of some code optimisation. The logs from our earlier DAWNBench submission show three seconds wasted on data preprocessing, which counts towards training time. Recall that we are normalising, transposing and padding the dataset before training to avoid repeating the work at each epoch.

We can do better by transferring the data to the GPU, preprocessing there and then transferring back to the CPU for random data augmentation and batching. Moving the whole dataset (in uint8 format) to the GPU takes a negligible 40ms whilst completing the preprocessing steps on the GPU is even faster, completing in about 15ms. The bulk of the time is spent transferring the preprocessed dataset back to the CPU which takes nearly half-a-second. This is a big improvement over our previous 3s but also seems a little wasteful, since the data will need to cross to the GPU again after batching and augmentation, incurring a further delay at each training step. Can we remove overhead this by doing data augmentation on the GPU?

The answer is yes, but it requires a little care. If we naively apply augmentation to individual training examples, as on the CPU, we incur substantial overhead launching multiple GPU kernels to process each item. We can avoid this by applying the same augmentation to groups of examples and we can preserve randomness by shuffling the data beforehand.

For example, consider applying 8×8 cutout augmentation to CIFAR10 images. There are 625 possible 8×8 cutout regions in a 32×32 image, so we can achieve random augmentation by shuffling the dataset and splitting into 625 groups, one for each of the possible cutout regions. If we choose evenly-sized groups, this is not quite the same as making a random choice for each example (which leads to irregular group sizes) but it’s close enough. As a further optimisation, if the number of groups for an augmentation becomes too large, we can consider capping it at a reasonable limit – say 200 randomly selected groups per epoch.

Our basic implementation is rather simple, taking about 35 lines of code (without any Pytorch DataLoaders.) Here are two random augmentations of the same 4 images to show it in action:

![augmentations.jpg](../_resources/a4fbf768b4c2a95678b510604f743938.jpg)

More importantly it’s fast, taking under 400ms to iterate through 24 epochs of training data and apply random cropping, horizontal flipping and cutout data augmentation, shuffling and batching. This is less than the time taken to transfer the dataset once to the CPU! Moreover, since we are no longer racing CPU preprocessing queues against the GPU, we can stop worrying about data loading altogether, even as training gets faster.

Note: we are relying on the fact that the dataset is small enough to store and manipulate as a whole in GPU memory, but a more sophisticated implementation would work around this – or one could switch to an industrial strength solution such as [Nvidia DALI](https://github.com/NVIDIA/DALI).

If we rerun the network and training from our DAWNBench submission with the new GPU data processing, training time drops just under 70s, moving us up two places on the leaderboard!

#### Aside: mixed precision training

In our original DAWNBench submission and in the code for the test above, we simply converted the model to float16 without all the niceties of so-called [mixed precision training,](https://arxiv.org/abs/1710.03740)although we include a basic sort of ‘loss scaling’ by summing rather than averaging losses in a batch. It is straightforward to implement proper mixed precision training but this adds about a second to overall training time and we found it to have no effect on final accuracy, so we continue to do without it below.

### Moving max-pool layers (64s)

Max-pooling commutes with a monotonic-increasing activation function such as ReLU. It should be more efficient to apply pooling first. This is the sort of thing a friendly compiler might do for you, but for now let’s switch the order by hand. Here is a typical conv-pool block before:

![conv_pool_block-1.png-1.svg](../_resources/b92cd9aa9367d7e3a40c06c401a6d5c5.png)
and after:
![conv_pool_block_opt.png.svg](../_resources/102081b7b51c64d092fc4c56d9d9995f.png)

Switching the order leads to a further 3s reduction in 24 epoch training time with no change at all to the function that the network is computing! Perhaps we should try something more radical and move max-pooling before batch norm. This will achieve a further efficiency gain but will change the network so we need to test the effect on training.

![conv_pool_block_pre.png](../_resources/82872b9f0069d725eb53025c901cfd7c.png)

* * *

The result is a small negative effect on test accuracy which moves to 94.0% (mean of 50 runs) compared to our baseline of 94.1%. More positively, this achieves a substantial 5s reduction in training time. We can restore the previous accuracy by adding an extra epoch to training. This is the only time in the post that we select an ‘improvement’ that leads to worse accuracy! The 5s gain from a more efficient network more than compensates the 2.5s loss from the extra training epoch. The net effect brings our time to 64s, up to third place on the leaderboard.

* * *

### Label smoothing (59s)

[Label smoothing](https://arxiv.org/abs/1512.00567) is a well-established trick for improving the training speed and generalization of neural nets in classification problems. It involves blending the one-hot target probabilities with a uniform distribution over class labels inside the cross entropy loss. This helps to stabilise the output distribution and prevents the network from making overconfident predictions which might inhibit further training. Let’s give it a try – the label smoothing parameter of 0.2 has been very roughly hand-optimised but the result is not too sensitive to a range of choices.

![label_smoothing.png](../_resources/9c4d806708dbb9297f6836f0452626fe.png)
Label smoothing loss

Test accuracy improves to 94.2% (mean of 50 runs.) We can trade this for training time by reducing the number of epochs. As a rule of thumb, we reduce training by one epoch for each 0.1% of test accuracy improvement, since this roughly tracks the gain from an extra epoch of training. We reduce the warmup period – during which learning rates increase linearly – in proportion to the overall number of epochs.

Accuracy for 23 epochs of training is 94.1% and training time dips under a minute!

### CELU activations (52s)

We might hope to help the optimisation process by using a smooth activation function, rather than ReLU with its delta-function of curvature at the origin. This may also help generalisation since smoothed functions lead to a less expressive function class – in the large smoothing limit we recover a linear network.

We are otherwise happy with ReLU so we’re going to pick a simple smoothed-out alternative. Our choice is the Continuously Differentiable Exponential Linear Unit or [CELU](https://arxiv.org/abs/1704.07483) activation since it is smooth (unlike ELU) and the PyTorch implementation is faster than that of the otherwise perfectly adequate Softplus activation. In addition to smoothing, CELU applies an x- and y-shift to ReLU as shown below, but these are largely irrelevant given our use of batch norm.

![CELU-1.png](../_resources/f47657f85794b6bc07212474f764505d.png)
CELU activation

We roughly hand-tune the smoothing parameter αα to a value of 0.075 – note that this is much lower than the default value of 1. This gives an impressive improvement to 94.3% test accuracy (mean of 50 runs) allowing a further 3 epoch reduction in training and a 20 epoch time of 52s for 94.1% accuracy.

### Ghost batch norm (46s)

Batch norm seems to work best with batch size of around 32. The reasons presumably have to do with noise in the batch statistics and specifically a balance between a beneficial regularising effect at intermediate batch sizes and an excess of noise at small batches.

Our batches are of size 512 and we can’t afford to reduce them without taking a serious hit on training times, but we can apply batch norm separately to subsets of a training batch. This technique, known as ‘ghost’ batch norm, is usually used in a distributed setting but is just as useful when using large batches on a single node. It isn’t supported directly in PyTorch but we can roll our own easily enough.

This gives a healthy boost to the 20 epoch test accuracy of 94.2%. As training becomes ever shorter, it is occasionally helpful to increase the learning rate to compensate. If we raise the max learning rate by 50% we can achieve 94.1% accuracy in 18 epochs and a training time of 46s.

### Frozen batch norm scales (43s)

Batch norm standardises the mean and variance of each channel but is followed by a learnable scale and bias. Our batch norm layers are succeeded by (smoothed) ReLUs, so the learnable biases could allow the network to optimise the level of sparsity per channel. On the other hand, if channel scales vary substantially this might reduce the effective number of channels and introduce a bottleneck. Let’s have a look at the dynamics of these parameters during training:

![bias_params.png](../_resources/5c47dacd79f1d750066674b5ca15276d.png)
![weight_params.png](../_resources/81e6a1151a14a33a918e3e924251525d.png)

* * *

There’s a lot going on in these plots, but one thing that sticks out is that the scales are not doing much learning and evolve largely under the control of weight decay. Let’s try freezing these at a constant value of 1/4 – roughly their average at the midpoint of training. The learnable scale for the final layer is somewhat larger but we can adjust the scaling of the network output to compensate.

Actually we can fix the batch norm scales to 1 instead if we rescale the αα parameter of CELU by a compensating factor of 4 and the learning rate and weight decay for the batch norm biases by 4242 and 1/421/42 respectively. We prefer to do things this way since it makes the impact of the channel scales on the learning rate dynamics of the biases more explicit.

18 epoch test accuracy improves to 94.2%. Interestingly, had we not increased the learning rate of the batch norm biases, we would have achieved a substantially lower accuracy. This suggests that the learnable biases are indeed doing something useful – either learning appropriate levels of sparsity or perhaps just adding regularisation noise. Indeed we can improve things slightly by increasing the learning rate of the biases by another factor of 4 and dividing weight decay by a corresponding factor.

Finally we can use the increased accuracy to reduce training to 17 epochs. The new test accuracy is 94.1% and most importantly we’ve overtaken the 8 GPUs of BaiduNet9P with a time of 43s, placing us second on the leaderboard!

### Input patch whitening (36s)

Batch norm does a good job at controlling distributions of individual channels but doesn’t tackle covariance between channels and pixels. Controlling the covariance at internal layers, using a ‘whitening’ version of batch norm, might be helpful but would entail extra computation as well as non-trivial implementation effort. We are going to focus on the easier problem at the input layer.

The classic way to remove input correlations is to perform global PCA (or ZCA) whitening. We propose a patch-based approach which is agnostic to the total image size and more in keeping with the structure of a conv net. We are going to apply PCA whitening to 3×3 patches of inputs as an initial 3×3 convolution with fixed (non-learnable) weights. We will follow this with a learnable 1×1 convolution. The 27 input channels to this layer are a transformed version of the original 3×3×3 input patches whose covariance matrix is approximately the identity, which should make optimisation easier.

First let’s plot the leading eigenvectors of the covariance matrix of 3×3 patches of the input data. The numbers in brackets are the square root of the corresponding eigenvalues to show the relative scales of variation along these directions and we plot the eigenvector with both signs to illustrate the direction of variation. As we might expect, variations in local brightness dominate.

![eigens1.png](../_resources/7ff56653b58f21faae7a1debc3d81c15.png)
![eigens2.png](../_resources/e9ab5600b23ccd18450fe07b88277516.png)
![eigens3.png](../_resources/640ba9d5c3fe3d4a72fc5f01a9ca2e4b.png)

Now let’s replace the first 3×3 convolution of the network with a fixed 3×3 whitening convolution to equalise the scales of the eigenpatches above, followed by a learnable 1×1 convolution and see the effect on training.

17 epoch test accuracy jumps to 94.4% allowing a further 2 epoch reduction in training time. 15 epochs brings a test accuracy of 94.1% in 39s, closing in on the 4-GPU, test-time-augmentation assisted DAWNBench leader! If we increase the maximum learning rate by a further ~50% and reduce the amount of cutout augmentation, from 8×8 to 5×5 patches, to compensate for the extra regularisation that the higher learning rate brings, we can remove a further epoch and reach 94.1% test accuracy in 36s, moving us narrowly into top spot on the leaderboard!!

### Exponential moving averages (34s)

High learning rates are necessary for rapid training since they allow stochastic gradient descent to traverse the necessary distances in parameter space in a limited amount of time. On the other hand, learning rates need to be annealed towards the end of training to enable optimisation along the steeper and noisier directions in parameter space. Parameter averaging methods allow training to continue at a higher rate whilst potentially approaching minima along noisy or oscillatory directions by averaging over multiple iterates.

We shall investigate exponential moving averaging of parameters which is a standard approach. For efficiency reasons we update the moving average every 5 batches since we find that more frequent updates don’t improve things. We need to choose a new learning rate schedule with higher learning rates towards the end of training, and a momentum for the moving average. For the learning rate, a simple choice is to stick with the piecewise linear schedule that we’ve been using throughout, floored at a low fixed value for the last 2 epochs and we choose a momentum of 0.99 so that averaging takes place over a timescale of roughly the last epoch.

Test accuracy improves to 94.3% allowing us to trim a further epoch. 13 epoch training reaches a test accuracy of 94.1%, achieving a training time below 34s and a 10× improvement over the single-GPU state-of-the-art at the outset of the series!

### Test-time augmentation (26s)

Suppose that you’d like your network to classify images the same way under horizontal flips of the input. One possibility, that we’ve been using till now, is to present the network with a large amount of data, possibly augmented by label preserving left-right flips, and hope that the network will eventually learn the invariance through extensive training.

A second approach, which doesn’t leave things to chance, is to present both the input image and its horizontally flipped version and come to a consensus by averaging network outputs for the two versions, thus guaranteeing invariance. This eminently sensible approach goes by the name of test-time augmentation.

At training time, we still present the network with a single version of each image – potentially subject to random flipping as a data augmentation so that different versions are presented on different training epochs. An alternative, would be to use the same procedure at training time as at test time and present each image along with its mirror. In this case, we could claim to have changed the network by splitting into two identical branches, one of which sees the flipped image, and then merging at the end. Through this lens, the original training can be viewed as a stochastic training procedure for a weight-tied, two branch network in which a single branch is ‘dropped-out’ for each training example.

This dropout-training viewpoint makes it clear that any attempt to introduce a rule disallowing TTA from a benchmark is going to be fraught with difficulties. From this point of view, we have just introduced a larger network for which we have an efficient stochastic training methodology. On the other hand, if we don’t limit the amount of work that we are prepared to do at test time then there are some obvious degenerate solutions in which training takes as little time as is required to store the dataset!

These arguments are not only relevant to artificial benchmarks but also to end use-cases. In some applications, classification accuracy is all that is desired and in that case TTA should most definitely be used. In other cases, inference time is also a constraint and a sensible approach is to maximise accuracy subject to such constraints. This is probably a good approach for training benchmarks too.

In the case at hand, the Kakao Brain team has applied the simple form of TTA described here – presenting an image and its left-right mirror at inference time, thus doubling the computational load. More extensive forms of TTA are of course possible for other symmetries (such as translational symmetry, variations in brightness/colour etc.) but these would come at a higher computational cost.

Now because these entries are based of a computationally light 9-layer ResNet, *total inference time including TTA* is likely to be much lower for these than for some of the 100+ layer networks that have been entered at earlier stages of the competition! According to our discussion above, any reasonable rule to limit this kind of approach should be based on inference time constraints and not an arbitrary feature of the implementation and so from this point-of-view, we should accept the approach.

Let’s see what improvement TTA brings. We shall restrict ourselves to horizontal flip TTA for consistency with the current DAWNBench submissions and because this seems a sweet spot between accuracy and inference cost. With our current network and 13 epoch training setup, the test accuracy with TTA rises to 94.6%, making this the largest individual effect we’ve studied today.

If we remove the remaining cutout data augmentation – which is getting in the way on such a short training schedule – we can reduce training to 10 epochs (!) and achieve a TTA test accuracy of 94.1% in 26s!

### Training to convergence

Here is a simple experiment to investigate whether the gains in training speed that we have collected also translate into gains in final accuracy for the model if it is trained to convergence. We have every reason to believe that this should be the case, if only because many of the techniques that we have been using today were originally proposed as techniques to improve converged accuracy on ImageNet! If it is the case that the same techniques which speed up training time to 94% accuracy on CIFAR10 also improve converged accuracy on ImageNet, then this suggests a rather effective way to accelerate research on the latter problem!

* * *

Unlike the previous experiments, this is going to be very rough and ready and we leave it to future work to do this experiment more carefully. We are going to pick a fixed learning rate schedule with lower learning rates appropriate for longer training and increase the amount of cutout augmentation to 12×12 patches to allow training for longer without overfitting. We will fix the other hyperparameters as they were above and train both the baseline network and the final network for a range of different times from 24 to 100 epochs. Finally we’re going to break all the rules and only run each experiment 5 times! Here are the results:

![valid_acc_conv.png](../_resources/c4e0b59d2dc28decc6294a417e9f81cd.png)
![tta_acc_conv.png](../_resources/0303e850e6afe3b6b36946a6255a5f78.png)

Despite the lack of tuning of the various extra hyperparameters of the final training setup for longer runs, it appears to maintain a healthy lead over the baseline even out to 100 epochs of training and approximate convergence. The final TTA accuracy of our little 9-layer ResNet at 80 epochs is 96.1% even though we never optimised anything for training above 94% accuracy! We could presumably go quite a bit higher with proper hyperparameter optimisation.

It appears that 96% accuracy is reached in about 70 epochs and 3 minutes of total training time, answering a question that I’ve been asked several times by people who (perhaps rightly) believe that the 94% threshold of DAWNBench is too low. Note that we have made almost no attempt to optimise the 96% time and we would expect it to come down considerably from here.

### Final thoughts

We’ve reached the end of the series and a few words are in order. Thanks to everyone who contributed to, supported or provided feedback on the project. Special thanks to Sam Davis, to Thomas Read for his work last summer on what became the post on weight decay and to everyone at Myrtle.

It has been tremendous fun working on this project, exploring dynamics of neural network training and extending the work of others to bring training times to a level where rapid experimentation becomes possible. I hope that the reader will find this useful in their work and believe that training times have a long way to fall yet (or accuracies improve if that’s your thing!) through further algorithmic developments.

At the outset of the series I half joked that if we could achieve 100% compute efficiency, training should take 40s. I would have been surprised to find that target surpassed by the end of the series with compute efficiency little better than it ever was! There is much scope for improvement on that front as well.