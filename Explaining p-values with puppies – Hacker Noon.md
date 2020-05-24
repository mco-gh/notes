Explaining p-values with puppies – Hacker Noon

# Explaining p-values with puppies

[![1*IL0mnvzNcpG2ZD0JBqo7zQ.jpeg](../_resources/a9a702b6b50deaca4c701bc207fa7828.jpg)](https://hackernoon.com/@kozyrkov?source=post_header_lockup)

[Cassie Kozyrkov](https://hackernoon.com/@kozyrkov)
Feb 21·3 min read

You’ll find p-values lurking all over [data science](http://bit.ly/quaesita_datasci) (and all the rest of science, for that matter). If you took STAT101, the explanation you probably heard runs something like this: *A p-value is the probability of observing a *[*statistic*](http://bit.ly/quaesita_statistics)* at least as extreme as ours, conditional on the null hypothesis.* No wonder that didn’t stick! Let’s try it with puppies instead…

![](../_resources/5300ecbe26924444fe7a4e30d3e59821.png)![0*QA2HyQSUy6HpKmtO.jpg](../_resources/6e7916d078fafc5be9c6e4f80468aba8.jpg)

Is p-value short for puppy-value?

### Setting the (crime) scene

Imagine coming home and discovering *this* in your kitchen:

![](../_resources/09931608f2f7474f45be00e014a8467b.png)![0*19c1lNjn-9-Bq_Of](../_resources/18e2d8b1295420bad78f85193ef1ce4b.png)

Let’s assume this is your dog and your kitchen, otherwise the example just became much stranger. Also, as far as their owners are concerned, dogs are always puppies even when they’re too big to carry around.

Let’s put this suspect on trial for the crime of sticking his head in the garbage bin!

We’ll work with a**  **[***default action***](http://bit.ly/quaesita_damnedlies) of *not yelling at Fido* and a corresponding [***null hypothesis***](http://bit.ly/quaesita_damnedlies) of “*Fido is innocent.” *If you’re new to these concepts or unsure how to set up hypotheses, read [this](http://bit.ly/quaesita_damnedlies).

![](../_resources/25dc5401f13e429fe7731d3bea0d8bd2.png)![1*TcA_HqULFfbfJCg7BAS5nA.png](../_resources/074bc330993bbf3f0ea64283842fe2af.png)

Our setup for the [hypothesis test](http://bit.ly/quaesita_fisher). Big words explained [here](http://bit.ly/quaesita_damnedlies). Also, yelling at puppies is probably not the way to go through life, but bear with me for the sake of the example.

### Describe the null world

The first step in calculating a p-value is to take a deep breath and say, *“Okay, Fido, I’m going to imagine that you are ****innocent****.”*

What we’re doing here is visualizing the null hypothesis world and figuring out how things work there so we can make a toy model of it. That’s what the [calculations are all about](http://bit.ly/quaesita_statistics).

### Does this evidence surprise you?

You’ve just finished imagining how your world works if **Fido never goes after garbage**.

> “How surprising would this evidence be if Fido’s innocent?”

It’s time to ask the big question: How likely is this world to cough up something at least as damning the evidence we saw in real life?

When you answer that question with a number, that number *is* the p-value itself!

![](../_resources/e4d46406ffad051cf971ba0da523c8e4.png)![0*Oty5V10DD90D-3ze.jpg](../_resources/47a076139eea668bf5053f2d7808cb1b.jpg)

### A verdict based on surprise

If you live with an eight year old (that special sort of mischief), it’s plausible that an innocent Fido gets decorated with new collar (made of bin lid) every now and then. Your p-value might not be such a small number. Since the evidence then looks plausible under Fido’s innocence, you’ll see no reason to change your mind about calling Fido a good dog.

If you live alone with Fido, you could still imagine a way to get evidence at least this damning. Maybe your crazy neighbor climbed in through your window, ran all around your apartment, put the bin lid on the dog’s head …and jumped out the window again!

This is possible. It’s just not very *probable*. When you squint at that probability, you find the p-value so teensy tiny that continuing to entertain the dog’s innocence makes *you* feel ridiculous. So you say, “I reject the null hypothesis. I find you guilty. BAD DOG, FIDO!”

> A p-value doesn’t *prove* anything. It’s simply a way to use surprise as a basis for making a reasonable decision.

It’s possible that you came to the wrong conclusion — uncertainty is a jerk that way. You won’t know whether you got it right until it’s too late. That’s life. We can only strive to do our best in an uncertain world. The p-value is simply a way to use surprise as a basis for making a reasonable decision. If you start expecting it to do something else for you, you’ll deserve [all the scorn the internet loves to throw at p-value abusers](http://bit.ly/uglyp).

### Summary

A p-value asks, *“If I’m living in a world where I should be taking my *[*default action*](http://bit.ly/quaesita_damnedlies)*, how unsurprising is my evidence?”* The higher the p-value, the less [ridiculous I’ll feel](http://bit.ly/quaesita_fisher) about persisting with my planned action. If the p-value is low enough, I’ll change my mind and do something else.