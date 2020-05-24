The concept of probability is not as simple as you think – Nevin Climenhaga | Aeon Ideas

The gambler, the quantum physicist and the juror all reason about probabilities: the probability of winning, of a radioactive atom decaying, of a defendant’s guilt. But despite their ubiquity, experts dispute just what probabilities *are*. This leads to disagreements on how to reason about, and with, probabilities – disagreements that our cognitive biases can exacerbate, such as our [tendency](http://psy2.ucsd.edu/~mckenzie/nickersonConfirmationBias.pdf) to ignore evidence that runs counter to a hypothesis we favour. Clarifying the nature of probability, then, can help to improve our reasoning.

Three popular theories analyse probabilities as either *frequencies*, *propensities* or *degrees of belief*. Suppose I tell you that a coin has a 50 per cent probability of landing heads up. These theories, respectively, say that this is:

- The *frequency* with which that coin lands heads;
- The *propensity*, or tendency, that the coin’s physical characteristics give it to land heads;
- How *confident* I am that it lands heads.

But each of these interpretations faces problems. Consider the following case:

> Adam flips a fair coin that self-destructs after being tossed four times. Adam’s friends Beth, Charles and Dave are present, but blindfolded. After the fourth flip, Beth says: ‘The probability that the coin landed heads the first time is 50 per cent.’

> Adam then tells his friends that the coin landed heads three times out of four. Charles says: ‘The probability that the coin landed heads the first time is 75 per cent.’

> Dave, despite having the same information as Charles, says: ‘I disagree. The probability that the coin landed heads the first time is 60 per cent.’

## Subscribe to our newsletter

### Updates on everything new at Aeon.

DailyWeekly

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' width='12' height='12' viewBox='0 0 24 24' data-evernote-id='533' class='js-evernote-checked'%3e%3cpath d='M0 0h24v24H0z' fill='none' data-evernote-id='534' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z' data-evernote-id='535' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

### See our newsletter privacy policy [here](https://aeon.co/ideas/the-concept-of-probability-is-not-as-simple-as-you-think)

The frequency interpretation struggles with Beth’s assertion. The frequency with which the coin lands heads is three out of four, and it can never be tossed again. Still, it seems that Beth was right: the probability that the coin landed heads the first time is 50 per cent.

Meanwhile, the propensity interpretation falters on Charles’s assertion. Since the coin is fair, it had an equal propensity to land heads or tails. Yet Charles also seems right to say that the probability that the coin landed heads the first time is 75 per cent.

The confidence interpretation makes sense of the first two assertions, holding that they express Beth and Charles’s confidence that the coin landed heads. But consider Dave’s assertion. When Dave says that the probability that the coin landed heads is 60 per cent, he says something false. But if Dave really is 60 per cent confident that the coin landed heads, then on the confidence interpretation, he has said something true – he has truly reported how certain he is.

Some philosophers think that such cases support a pluralistic approach in which there are multiple kinds of probabilities. My own view is that we should adopt a fourth interpretation – a *degree-of-support* interpretation.

Here, probabilities are understood as *relations of evidential support* between propositions. ‘The probability of X given Y’ is the degree to which Y *supports* the truth of X. When we speak of ‘the probability of X’ on its own, this is [shorthand](http://joelvelasco.net/teaching/3865/hajek%20-the%20reference%20class%20problem.pdf) for the probability of X conditional on any background information we have. When Beth says that there is a 50 per cent probability that the coin landed heads, she means that this is the probability that it lands heads conditional on the information that it was tossed and some information about its construction (for example, it being symmetrical).

Relative to different information, however, the proposition that the coin landed heads has a different probability. When Charles says that there is a 75 per cent probability that the coin landed heads, he means this is the probability that it landed heads relative to the information that three of four tosses landed heads. Meanwhile, Dave says there is a 60 per cent probability that the coin landed heads, relative to this same information – but since this information in fact supports heads more strongly than 60 per cent, what Dave says is false.

The degree-of-support interpretation incorporates what’s right about each of our first three approaches while correcting their problems. It captures the connection between probabilities and degrees of confidence. It does this not by identifying them – instead, it takes degrees of belief to be *rationally constrained* by degrees of support. The reason I should be 50 per cent confident that a coin lands heads, if all I know about it is that it is symmetrical, is because this is the degree to which my evidence supports this hypothesis.

Similarly, the degree-of-support interpretation allows the information that the coin landed heads with a 75 per cent frequency to make it 75 per cent probable that it landed heads on any particular toss. It captures the connection between frequencies and probabilities but, unlike the frequency interpretation, it denies that frequencies and probabilities are *the same thing*. Instead, probabilities sometimes relate claims about frequencies to claims about specific individuals.

Finally, the degree-of-support interpretation analyses the *propensity* of the coin to land heads as a relation between, on the one hand, propositions about the construction of the coin and, on the other, the proposition that it lands heads. That is, it concerns the degree to which the coin’s construction predicts the coin’s behaviour. More generally, propensities link claims about causes and claims about effects – eg, a description of an atom’s intrinsic characteristics and the hypothesis that it decays.

Because they turn probabilities into different kinds of entities, our four theories offer divergent advice on how to figure out the values of probabilities. The first three interpretations (frequency, propensity and confidence) try to make probabilities things we can *observe* – through counting, experimentation or introspection. By contrast, degrees of support seem to be what philosophers call ‘abstract entities’ – neither in the world nor in our minds. While we know that a coin is symmetrical by observation, we know that the proposition ‘this coin is symmetrical’ supports the propositions ‘this coin lands heads’ and ‘this coin lands tails’ to equal degrees in the same way we know that ‘this coin lands heads’ entails ‘this coin lands heads or tails’: by [thinking](https://aeon.co/ideas/philosophical-intuition-just-what-is-a-priori-justification).

But a skeptic might point out that coin tosses are easy. Suppose we’re on a jury. How are we supposed to figure out the probability that the defendant committed the murder, so as to see whether there can be reasonable doubt about his guilt?

Answer: think more. First, ask: what is our evidence? What we want to figure out is how strongly *this* evidence supports the hypothesis that the defendant is guilty. Perhaps our salient evidence is that the defendant’s fingerprints are on the gun used to kill the victim.

Then, ask: can we use the mathematical rules of probability to break down the probability of our hypothesis in light of the evidence into more tractable probabilities? Here we are concerned with the probability of a cause (the defendant committing the murder) given an effect (his fingerprints being on the murder weapon). [Bayes’s theorem](https://aeon.co/essays/it-s-time-for-science-to-abandon-the-term-statistically-significant) lets us calculate this as a function of three further probabilities: the prior probability of the cause, the probability of the effect *given* this cause, and the probability of the effect *without* this cause.

Since this is all relative to any background information we have, the first probability (of the cause) is informed by what we know about the defendant’s motives, means and opportunity. We can get a handle on the third probability (of the effect without the cause) by breaking down the possibility that the defendant is innocent into other possible causes of the victim’s death, and asking how probable each is, and how probable they make it that the defendant’s fingerprints would be on the gun. We will eventually reach probabilities that we cannot break down any further. At this point, we might search for general principles to guide our assignments of probabilities, or we might rely on intuitive judgments, as we do in the coin cases.

When we are reasoning about criminals rather than coins, this process is unlikely to lead to convergence on precise probabilities. But there’s no alternative. We can’t resolve disagreements about how much the information we possess supports a hypothesis just by gathering more information. Instead, we can make progress only by way of philosophical reflection on the space of possibilities, the information we have, and how strongly it supports some possibilities over others.