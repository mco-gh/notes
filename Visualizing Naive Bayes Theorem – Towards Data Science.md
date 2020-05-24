Visualizing Naive Bayes Theorem – Towards Data Science

# Visualizing Naive Bayes Theorem

## Bayesian Theorem visualized though Venn, Tree and Pie diagrams

[![2*YGkfgTb7E9kxK4JyEnM2KQ.jpeg](../_resources/b0695b4dce54678701af45977ce0afb6.jpg)](https://towardsdatascience.com/@eugene.chian?source=post_header_lockup)

[Hugegene](https://towardsdatascience.com/@eugene.chian)

May 4·5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='144'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

Ever needed to memorise the Bayesian Theorem formula? Visualise Bayesian Theorem through Venn diagram and do not need to memorise it again.

From the Venn diagram below, the probability that a randomly picked student is a girl in a class of 100, **P(Girl) **is the proportion of girls among 100 students:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*iwO_KSSX4abXUUqDbj5lyQ.png](../_resources/8ec9dc6d194e21e9fd0888f33e772d6d.png)

![](../_resources/4746cffa0354b77d2316770b6cf14e94.png)![1*ylJSz3_M55JNh7LsCTMutQ.png](../_resources/926a4a3a459cf617b5e543c7edf4c416.png)

The conditional probability of she wears pink given that the student is a girl, **P(Wearing pink| Girls)** is the proportion who wear pink among all girls:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*A_I7Pxh_0zc74xq8shIZSQ.png](../_resources/f6c227f0650a5a5f6f385c7a602c710d.png)

![](../_resources/9c265a9914c31303f49ae99aeb42e01c.png)![1*CdgL-YfngJu6v6uKwu13xw.png](../_resources/353769dc89f040432bc2c3e01bc72dcc.png)

The probability that the student is a girl and she wears pink, P(Wearing pink ∩ Girl) or **P(Girl ∩ Wearing pink)** is the proportion of girls and wear pink among 100 students:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*X6w2pHBSqcwhTNg3ytEqpA.png](../_resources/9db61aea1d0d1e8aa185ac09d17297a8.png)

![](../_resources/2d1dd20326efcfa968875c82e22370a4.png)![1*I-PhcqbOv0SAtD1Ow0yFtw.png](../_resources/d84d1e077d86e4d9d639d70159c67689.png)

Hence, the conditional probability of the student is a girl given that the student is wearing pink, **P(Girls|Wearing pink)** is the proportion of girls among all that wear pink and can be found by dividing the intersection by the probability of Wearing pink, P(Wearing pink):

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*2BwXFc_4PlmXbUBuScT6Jw.png](../_resources/2a0775ca71782ce7bb8bbaddc0adee06.png)

![](../_resources/745152398f3cd66b60aa98356bef09c4.png)![1*E7JO6eeZiX1iN_HfUq9ZIA.png](../_resources/66bb0406c95ab84387357c1a2a165da9.png)

More frequently, Bayesian probability can be calculated through a Tree Diagram:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*s1kJKMvz75vTDml9vxL5sA.png](../_resources/4bde80c5de35518946233bd83082937e.png)

The probability of any student wearing pink,** P(Wears pink)** = P(Girl and Wears pink)+ P(Boy and Wears pink) = 23/100 + 2/100 = 25/100 =** 0.25**

The conditional probability of she wears pink given that the student is a girl, **P(Wears pink|girl)** is 23/55 = **0.418**

Knowing that the student is a girl, the probability of her wearing pink (0.418) is larger than the probability of any student wearing pink on the whole(0.25). Hence **knowing that the student is a girl, it increases the probability of her wearing pink**. It can also be said that being a girl and wearing pink are associated and they are** not mutually independent events.**

On the other hand, the following example shows mutually independent events:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)![1*1mT6Qzzj_Izgx4pMBNcAiA.png](../_resources/0d81c70bd38b18e9b6218f394d56b24d.png)

The probability of any student who is free for dinner, **P(Free for dinner) **is P(Girl and Free for dinner)+ P(Boy and Free for dinner) = 22/100 + 18/100 = 40/100 = **0.4**

The conditional probability of she is free for dinner given that the student is a girl, **P(Free for dinner|girl)** is 22/55 = **0.4**

Knowing that it is a girl, the probability of she is free for dinner (0.4) is the same as the probability of people who are free for dinner on the whole (0.25). Hence **knowing that it is a girl, it did not increase or decrease the probability that she is free for dinner**. It can also be said that being a girl and being free for dinner are not associated and they **are mutually independent events.**

Assuming there is another conditional probability of the student is wearing shorts given that it is a girl, **P(Wears shorts|girl) **= 7/55 and P(Wears shorts|girl) is mutually independent of P(Wearing pink|girl):

![](:/2be9e459a2c05e5dc19d1e369f3a691a)![1*RVP2mm7PSnMPM4JLHESTuw.gif](../_resources/ac23ffe2483b47146b250331936bf4c4.gif)

Since P(Wears shorts|girl) is mutually independent of P(Wearing pink|girl), whether the girl is wearing pink does not affect the probability of the girl wearing shorts (it is always 7/55 =0.13). 0.13 of girls who wear pink wear shorts. 0.13 of girls who do not wear pink also wear shorts. Hence the conditional probability of the student wearing pink and shorts given that the student is a girl, P(Wears shorts, Wears pink|girl) is:

![](../_resources/2717cc8fd92b65399a89b495c8128799.png)![1*YCT6nQ24x__OdDC9naATiQ.png](../_resources/cf9b820ccdcf28836528bf769c9e8260.png)

where Xi refers to the different feature given that it is a girl. As mutual independence are assumed between P(Wears shorts|Girl) and P(Wears pink|Girl), this method for the extraction of conditional probability from multiple features given a class label is called Naive Bayes.

If mutual independence is not assumed between P(Wears shorts|Girl) and P(Wears pink|Girl), knowing the girl is wearing pink may decrease the probability of the girl wearing shorts. The conditional probability of the girl wears shorts given that she is a girl and wear pink, P(Wears shorts|Wears pink, Girl) needs to be found:

![](../_resources/5f030845ef99efd18414e750ba660207.png)![1*YSR3CwGd-WBn15Fk0bDwcA.png](../_resources/87626b024077b7ecf78fbc697298bab9.png)

The Naive Bayes Classifier formula to predict the probability of an example with features X1 to Xi belongs to class j is given:

![](../_resources/41ca6a688fc7cd7bce5ab7ae005bb13a.png)![1*P43rlkZdTQyXWLjAobfcSQ.png](../_resources/01a4138cfca32656b0d465860857cc82.png)

Where P(Cj|X1,..,Xi) is the posterior probability to be predicted, P(Xi|Cj) is the conditional probability of feature i given class j, P(Cj) is the prior probability of class j and P(Xi) is the probability of Xi.