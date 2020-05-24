Statistics for people in a hurry - Towards Data Science

# Statistics for people in a hurry

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='188' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='189' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![1*IL0mnvzNcpG2ZD0JBqo7zQ.jpeg](../_resources/bdd198bb8510e1e6545d3079c7910a2b.jpg)](https://towardsdatascience.com/@kozyrkov?source=post_page-----a9613c0ed0b----------------------)

[Cassie Kozyrkov](https://towardsdatascience.com/@kozyrkov?source=post_page-----a9613c0ed0b----------------------)

[May 29, 2018](https://towardsdatascience.com/statistics-for-people-in-a-hurry-a9613c0ed0b?source=post_page-----a9613c0ed0b----------------------) · 8 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='208'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/a9613c0ed0b/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='217'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='218' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/a9613c0ed0b/share/facebook?source=post_actions_header---------------------------)

Ever wished someone would just tell you what the [point of statistics](http://bit.ly/quaesita_pointofstats) is and what the jargon means in plain English? Let me try to grant that wish for you! I’ll zoom through all the biggest ideas in statistics in 8 minutes! Or just 1 minute, if you stick to the large font bits.

![0*ZLXzv9g2gF3CfJfR.jpg](../_resources/68461bf2b9a178481db299424332cb33.jpg)
![0*Z56A_UHpgRDtwxgl.jpg](../_resources/45af32ed85de1b4399018fe0f8df1f04.jpg)

What’s a ***statistic***? It’s any old way of mushing up our data. Yup. 100% technically correct definition. Now let’s see what the discipline of *statistics* is [all about](http://bit.ly/quaesita_pointofstats).

> Statistics is the science of changing your mind.

Making decisions based on facts (***parameters***) is hard enough as it is, but -curses!- sometimes we don’t even have the facts we need. Instead, what we know (our [***sample***](http://bit.ly/quaesita_vocab)) is different from what we wish we knew (our [***population***](http://bit.ly/quaesita_popwrong)). That’s what it means to have [***uncertainty***](http://bit.ly/quaesita_savvy).

***Statistics*  **is the science of changing your mind under uncertainty. What might your mind be set to? A ***default action*** or a ***prior belief***. What if your mind’s a blank slate? [Read this instead](http://bit.ly/quaesita_pointofstats).

> Bayesians change their mind about beliefs.

**Bayesian statistics** is the school of thought that deals with incorporating data to update your beliefs. Bayesians like to report results using **credible intervals** (two numbers which are interpreted as, “I believe the answer lives between here and here”).

> Frequentists change their mind about actions.

***Frequentist statistics*** deals with changing your mind about actions. You don’t need to have a belief to have a [***default action***](http://bit.ly/quaesita_damnedlies)***,*** it’s simply what you’re [committed to doing](http://bit.ly/quaesita_inspired) if you don’t analyze any data. Frequentist (a.k.a. classical) statistics is the one you’re more likely to encounter in the wild and in your STAT101 class, so let’s keep it classical for the rest of this article.

> Hypotheses are descriptions of what the world might look like.

The [***null hypothesis***](http://bit.ly/quaesita_damnedlies) describes all worlds where doing the default action is a happy choice; the ***alternative hypothesis*** is all other worlds. If I convince you -with data!- that you don’t live in the null hypothesis world, then you had better change your mind and take the **alternative action**.

[For example](http://bit.ly/quaesita_fisher): “We can walk to class together (*default action*) if you usually take under 15 minutes to get ready (*null hypothesis*), but if the evidence (*data*) suggests it’s longer (*alternative hypothesis*), you can walk by yourself because I’m outta here (*alternative action*).”

> Testing in a nutshell: “Does our evidence make the null hypothesis look ridiculous?”

All of [***hypothesis testing***](http://bit.ly/quaesita_damnedlies) is all about asking: does our evidence make the null hypothesis look ridiculous? ***Rejecting the null*** hypothesis means we learned something and we should change our minds. Not rejecting the null means [***we learned nothing interesting***](http://bit.ly/quaesita_fisher), just like [going for a hike in the woods and seeing no humans](http://bit.ly/quaesita_yesbutton) doesn’t prove that there are no humans on the planet. It just means we didn’t learn anything interesting about humans existing. Does it make you sad to [learn nothing](http://bit.ly/quaesita_fisher)? It shouldn’t, because you have a lovely insurance policy: you know exactly what action to take. If you learned nothing, you have no reason to change your mind, so keep doing the [default action](http://bit.ly/quaesita_damnedlies).

So how do we know if we learned something interesting… something out of line with the world in which we want to keep doing our [default action](http://bit.ly/quaesita_inspired)? To get the answer, we can look at a [p-value](http://bit.ly/quaesita_puppies) or a confidence interval.

> The p-value’s on the periodic table: it’s the element of surprise.

The ***p-value*** says, “If I’m living in a world where I should be taking that default action, how unsurprising is my evidence?” The lower the [p-value](http://bit.ly/quaesita_p3), the more the data are yelling, “Whoa, that’s surprising, maybe you should change your mind!”

To perform the test, compare that p-value with a threshold called the [***significance level***](http://bit.ly/quaesita_p3). This is a knob you use to control how much risk you want to tolerate. It’s your maximum probability of stupidly leaving your cozy comfy default action. If you set the significance level to 0, that means you refuse to make the mistake of leaving your default incorrectly. Pens down! Don’t analyze any data, just take your default action. (But that means you might end up stupidly NOT leaving a bad default action.)

![1*LZwHBx6cMhGbsowpJWb5HA.png](../_resources/a94c7c1de7487da4bedd7792aaa3401c.png)
![1*LZwHBx6cMhGbsowpJWb5HA.png](../_resources/646402a9bc4ca155e7e4b285a20a18fa.png)

How to use p-values to get the outcome of your hypothesis test. (No one will suspect that my xkcd is a knockoff.)

A ***confidence interval*** is simply a way to report your hypothesis test results. To use it, check whether it overlaps with your null hypothesis. If it does overlap, learn nothing. If it doesn’t, change your mind.

> Only change your mind if the confidence interval doesn’t overlap with your null hypothesis.

While a confidence interval’s technical meaning is little bit weird (I’ll tell you all about it in a future post, it’s definitely not simple like the credible interval we met earlier, and wishing does not make it so), it also has two useful properties which analysts find helpful in describing their data: (1) the best guess is always in there and (2) it’s narrower when there’s more data. Beware that both it and the p-value weren’t designed to be nice to talk about, so don’t expect pithy definitions. They’re just ways to summarize test results. (If you took a class and found the definitions impossible to remember, that’s why. On behalf of statistics: it’s not you, it’s me.)

What’s the point? If you do your testing the way I just described, the math guarantees that your risk of making a mistake is capped at the [significance level](http://bit.ly/quaesita_p3) you chose (which is why it’s important that you, ahem, choose it… the math is there to guarantee you the risk settings you picked, which is kind of pointless if you don’t bother to pick ‘em).

> The math is all about building a toy model of the null hypothesis universe. That’s how you get the p-value.

![0*Z56A_UHpgRDtwxgl.jpg](../_resources/0818efb2bdbb2f05b1f5d9358718d1b7.jpg)
![0*ZLXzv9g2gF3CfJfR.jpg](../_resources/0b18ae98cf3d8841661a21be1a56799e.jpg)

The math is all about making and examining toy universes (how cool is that, fellow megalomaniacs!? So cool!) to see how likely they are to spawn datasets like yours. If your toy model of the null hypothesis universe is unlikely to give you data like the data you got from the real world, your p-value will be low and you’ll end up rejecting the null hypothesis… change your mind!

What’s with all those crazy formulas, those probabilities and [distributions](http://bit.ly/quaesita_hist)? They allow us to express the rules governing the [null hypothesis universe](http://bit.ly/quaesita_p2) so we can figure out whether that universe is the kind of place that coughs up data similar to what you got in real life. And if it isn’t, you shout: “Ridiculous! Off with its head!” If it is, you shrug and learn nothing. More on this in a future post. For now, just think of the math as building little toy worlds for us to poke at so we can see if our dataset looks reasonable in them. The [p-value](http://bit.ly/quaesita_puppies) and confidence interval are ways to summarize all that for you so you don’t need to squint at a long-winded description of a universe. They’re the endgame: use them to see whether or not to leave your [default action](http://bit.ly/quaesita_inspired). Job done!

> Did we do our homework? That’s what power measures.

Hang on, did we do our homework to make sure that we actually collected *enough* evidence to give ourselves a fair shot at changing our minds? That’s what the concept of ***power*** measures. It’s really easy not to find any mind-changing evidence… just don’t go looking for it. The more power you have, the more opportunity you’ve given yourself to change your mind if that’s the right thing to do. Power is the probability of correctly leaving your [default action](http://bit.ly/quaesita_damnedlies).

When we learn nothing and keep doing what we’re doing, we can feel better about our process if it happened with lots of power. At least we did our homework. If we had barely any power at all, we pretty much knew we weren’t going to change our minds. May as well not bother analyzing data.

> Use power analysis to check that you budgeted for enough data before you begin.

***Power analysis*** is a way to check how much power you expect for a given amount of data. You use it to plan your studies before you begin. (It’s pretty easy too; in a future post I’ll show you that all it takes is a few *for loops.*)

> Uncertainty means you can come to the wrong conclusion, even if you have the best math in the world.

What is statistics not? Magical magic that makes certainty out of uncertainty. There’s no magic that can do that; you can still make mistakes. Speaking of mistakes, here’s two mistakes you can make in Frequentist statistics. (Bayesians don’t make mistakes. Kidding! Well, sort of. Stay tuned for my Bayesian post.)

***Type I error*** is foolishly leaving your default action. Hey, you said you were comfortable with that [default action](http://bit.ly/quaesita_damnedlies) and now thanks to all your math you left it. Ouch! ***Type II error*** is foolishly not leaving your default action. (We statisticians are so creative at naming stuff. Guess which mistake is worse. Type I? Yup. So creative.)

> Type I error is changing your mind when you shouldn’t.
> Type II error is NOT changing your mind when you should.

Type I error is like convicting an innocent person and Type II error is like failing to convict a guilty person. These two error probabilities are in balance (making it easier to convict a guilty person also makes it easier to convict an innocent person), unless you get more evidence (data!), in which case both errors become less likely and everything becomes better. That’s why statisticians want you to have more, more, MOAR data! Everything becomes better when you have more data.

> More data means more protection against coming to the wrong conclusion.

What’s ***multiple comparisons correction***? You’ve got to do your testing in a different, adjusted way if you know you plan to ask multiple questions of the same dataset. If you keep putting innocent suspects on trial over and over again (if you keep fishing in your data) eventually something is going to look guilty by random accident. The term ***statistically significant*** doesn’t mean something important happened in the eyes of the universe. It simply means we changed our minds. Perhaps incorrectly. Curse that uncertainty!

> Don’t waste your time rigorously answering the wrong question. Apply statistics intelligently (and only where needed).

What’s a [***Type III error***](http://bit.ly/quaesita_wsai)? It’s kind of a statistics joke: it refers to correctly rejecting the wrong null hypothesis. In other words, using all the right math to answer the wrong question.

A cure for asking and answering the wrong question can be found in [Decision Intelligence](http://bit.ly/quaesita_gcpp), the new discipline that looks at applying data science to solving business problems and making decisions well. By mastering decision intelligence, you’ll build up your immunity to Type III error and useless [analytics](http://bit.ly/quaesita_datasci).

In summary, statistics is the science of changing your mind. There are two schools of thought. The more popular one - Frequentist statistics - is all about checking whether you should leave your default action. Bayesian statistics is all about having a prior opinion and updating that opinion with data. If your mind is truly blank before you begin, look at your data and [just go with your gut](http://bit.ly/quaesita_pointofstats).