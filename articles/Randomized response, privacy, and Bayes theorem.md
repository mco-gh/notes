Randomized response, privacy, and Bayes theorem

![](../_resources/5e11534210f3c39e40d93a97bc7d701d.png)

Suppose you want to gather data on an incriminating question. For example, maybe a statistics professor would like to know how many students cheated on a test. Being a statistician, the professor has a clever way to find out what he wants to know while giving each student deniability.

## Randomized response

Each student is asked to flip two coins. If the first coin comes up heads, the student answers the question truthfully, yes or no. Otherwise the student reports “yes” if the second coin came up heads and “no” it came up tails. Every student has deniability because each “yes” answer may have come from an innocent student who flipped tails on the first coin and heads on the second.

How can the professor estimate *p*, the proportion of students who cheated? Around half the students will get a head on the first coin and answer truthfully; the rest will look at the second coin and answer yes or no with equal probability. So the expected proportion of yes answers is *Y* = 0.5*p* + 0.25, and we can estimate *p* as 2*Y* – 0.5.

## Database anonymization

The calculations above assume that everyone complied with the protocol, which may not be reasonable. If everyone were honest, there’d be no reason for this exercise in the first place. But we could imagine another scenario. Someone holds a database with identifiers and answers to a yes/no question. The owner of the database could follow the procedure above to introduce randomness in the data before giving the data over to someone else.

## Information contained in a randomized response

What can we infer from someone’s randomized response to the cheating question? There’s nothing you can infer with *certainty*; that’s the point of introducing randomness. But that doesn’t mean that the answers contain no information. If we completely randomized the responses, dispensing with the first coin flip, *then* the responses would contain no information. The responses *do* contain information, but not enough to be incriminating.

Let *C* be a random variable representing whether someone cheated, and let *R* be their response, following the randomization procedure above. Given a response *R* = 1, what is the probability *p* that *C* = 1, i.e. that someone cheated? This is a classic application of Bayes’ theorem.

![](../_resources/0c0ef6b636dee5785b758bf9ab14a93d.png)

If we didn’t know someone’s response, we would estimate their probability of having cheated as *p*, the group average. But knowing that their response was “yes” we update our estimate to 3*p* / (2*p* + 1). At the extremes of *p* = 0 and *p* = 1 these coincide. But for any value of *p* strictly between 0 and 1, our estimate goes up. That is, the probability that someone cheated, conditional on knowing they responded “yes”, is higher than the unconditional probability. In symbols, we have

![](../_resources/271b9952c148e1ba76c34fb2e48d6a6e.png)

when 0 < *p *< 1. The difference between the left and right sides above is maximized when *p* = (√3 – 1)/2 = 0.366. That is, a “yes” response tells us the most when about 1/3 of the students cheated. When *p* = 0.366, *P*(*C *= 1 | *R*= 1) = 0.634, i.e. the posterior probability is almost twice the prior probability.

You could go through a similar exercise with Bayes theorem to show that *P*(*C* = 1 | *R* = 0) = *p*/(3 – 2*p*), which is less than *p* provided 0 < *p* < 1. So if someone answers “yes” to cheating, that does make it more likely that the actually cheated, but not so much more that you can justly accuse them of cheating. (Unless *p* = 1, in which case you’re in the realm of logic rather than probability: if everyone cheated, then you can conclude that any individual cheated.)

**Related**: [Data privacy consulting](https://www.johndcook.com/blog/data-privacy/)