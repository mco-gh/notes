An Intuitive (and Short) Explanation of Bayes’ Theorem – BetterExplained

Bayes’ theorem was the subject of [a detailed article](http://www.yudkowsky.net/rational/bayes). The essay is good, but over 15,000 words long — here’s the condensed version for Bayesian newcomers like myself:

- **Tests are not the event.** We have a cancer *test*, separate from the event of actually having cancer. We have a *test* for spam, separate from the event of actually having a spam message.
- **Tests are flawed.** Tests detect things that don’t exist (false positive), and miss things that do exist (false negative).
- **Tests give us test probabilities, not the real probabilities.** People often consider the test results directly, without considering the errors in the tests.
- **False positives skew results.** Suppose you are searching for something really rare (1 in a million). Even with a good test, it’s likely that a positive result is really a *false positive* on somebody in the 999,999.
- **People prefer natural numbers.** Saying “100 in 10,000″ rather than “1%” helps people work through the numbers with fewer errors, especially with multiple percentages (“Of those 100, 80 will test positive” rather than “80% of the 1% will test positive”).
- **Even science is a test**. At a philosophical level, scientific experiments can be considered “potentially flawed tests” and need to be treated accordingly. There is a *test* for a chemical, or a phenomenon, and there is the *event* of the phenomenon itself. Our tests and measuring equipment have some inherent rate of error.

**Bayes’ theorem converts the results from your test into the real probability of the event.** For example, you can:

- **Correct for measurement errors**. If you know the real probabilities and the chance of a false positive and false negative, you can correct for measurement errors.
- **Relate the actual probability to the measured test probability.** Bayes’ theorem lets you relate Pr(A|X), the chance that an event A happened given the indicator X, and Pr(X|A), the chance the indicator X happened given that event A occurred. Given mammogram test results and known error rates, you can predict the actual chance of having cancer.

[Bayes' Theorem Intuition](https://www.youtube.com/watch?v=YBvilAYd5sE)

Contents [[hide](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#)]

- [Anatomy of a Test](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#Anatomy_of_a_Test)
- [How Accurate Is The Test?](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#How_Accurate_Is_The_Test)
- [Bayes’ Theorem](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#Bayes_Theorem)
- [Intuitive Understanding: Shine The Light](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#Intuitive_Understanding_Shine_The_Light)
- [Bayesian Spam Filtering](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#Bayesian_Spam_Filtering)
- [Further Reading](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#Further_Reading)
- [Other Posts In This Series](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#Other_Posts_In_This_Series)

## Anatomy of a Test

The article describes a cancer testing scenario:

- 1% of women have breast cancer (and therefore 99% do not).
- 80% of mammograms detect breast cancer when it is there (and therefore 20% miss it).
- 9.6% of mammograms detect breast cancer when it’s **not** there (and therefore 90.4% correctly return a negative result).

Put in a table, the probabilities look like this:
![bayes_table.png](../_resources/032f9813dc19543c9aee460b74d53997.png)
How do we read it?

- 1% of people have cancer
- If you **already have cancer**, you are in the first column. There’s an 80% chance you will test positive. There’s a 20% chance you will test negative.
- If you **don’t have cancer**, you are in the second column. There’s a 9.6% chance you will test positive, and a 90.4% chance you will test negative.

## How Accurate Is The Test?

Now suppose you get a positive test result. What are the chances you have cancer? 80%? 99%? 1%?

Here’s how I think about it:

- Ok, we got a positive result. It means we’re somewhere in the top row of our table. Let’s not assume anything — it could be a true positive or a false positive.
- The chances of a *true positive* = chance you have cancer * chance test caught it = 1% * 80% = .008
- The chances of a *false positive* = chance you don’t have cancer * chance test caught it anyway = 99% * 9.6% = 0.09504

The table looks like this:
![bayes_table_computed.png](../_resources/6b39f01a7cde780fd40fb1bab07007c2.png)

And what was the question again? Oh yes: what’s the chance we really have cancer if we get a positive result. The chance of an event is the number of ways it could happen given all possible outcomes:

`Probability = desired event / all possibilities`

The chance of getting a real, positive result is .008. The chance of getting any type of positive result is the chance of a true positive plus the chance of a false positive (.008 + 0.09504 = .10304).

So, our chance of cancer is .008/.10304 = 0.0776, or about 7.8%.

Interesting — a positive mammogram only means you have a 7.8% chance of cancer, rather than 80% (the supposed accuracy of the test). It might seem strange at first but it makes sense: the test gives a false positive 9.6% of the time (quite high), so there will be **many** false positives in a given population. For a rare disease, **most** of the positive test results will be wrong.

Let’s test our intuition by drawing a conclusion from simply eyeballing the table. If you take 100 people, only 1 person will have cancer (1%), and they’re most likely going to test positive (80% chance). Of the 99 remaining people, about 10% will test positive, so we’ll get roughly 10 false positives. Considering all the positive tests, just 1 in 11 is correct, so there’s a 1/11 chance of having cancer given a positive test. The real number is 7.8% (closer to 1/13, computed above), but we found a reasonable estimate without a calculator.

## Bayes’ Theorem

We can turn the process above into an equation, which is Bayes’ Theorem. It lets you take the test results and correct for the “skew” introduced by false positives. You get the real chance of having the event. Here’s the equation:

![\displaystyle{\Pr(\mathrm{A}|\mathrm{X}) = \frac{\Pr(\mathrm{X}|\mathrm{A})\Pr(\mathrm{A})}{\Pr(\mathrm{X|A})\Pr(\mathrm{A})+ \Pr(\mathrm{X | not \ A})\Pr(\mathrm{not \ A})}}](../_resources/555ac979cf381699239e50860f0282b1.png)

And here’s the decoder key to read it:

- Pr(A|X) = Chance of having cancer (A) given a positive test (X). This is what we want to know: How likely is it to have cancer with a positive result? In our case it was 7.8%.
- Pr(X|A) = Chance of a positive test (X) given that you had cancer (A). This is the chance of a true positive, 80% in our case.
- Pr(A) = Chance of having cancer (1%).
- Pr(not A) = Chance of not having cancer (99%).
- Pr(X|not A) = Chance of a positive test (X) given that you didn’t have cancer (~A). This is a false positive, 9.6% in our case.

Try it with any number:

## Bayes Theorem

0.010.80.096Chance positive test means positive result7.76397515528%

[powered byinstacalc](https://instacalc.com/11220)[*open_in_new*](https://instacalc.com/11220)

It all comes down to the chance of a **true positive result** divided by the **chance of any positive result**. We can simplify the equation to:

![\displaystyle{\Pr(\mathrm{A}|\mathrm{X}) = \frac{\Pr(\mathrm{X}|\mathrm{A})\Pr(\mathrm{A})}{\Pr(\mathrm{X})}}](../_resources/826668299bb140b589fb2f6df3df30a2.png)

Pr(X) is a normalizing constant and helps scale our equation. Without it, we might think that a positive test result gives us an 80% chance of having cancer.

Pr(X) tells us the chance of getting *any* positive result, whether it’s a real positive in the cancer population (1%) or a false positive in the non-cancer population (99%). It’s a bit like a weighted average, and helps us compare against the overall chance of a positive result.

In our case, Pr(X) gets really large because of the potential for false positives. Thank you, normalizing constant, for setting us straight! This is the part many of us may neglect, which makes the result of 7.8% counter-intuitive.

## Intuitive Understanding: Shine The Light

The article mentions an intuitive understanding about shining a light through your real population and getting a test population. The analogy makes sense, but it takes a few thousand words to get there :).

Consider a real population. You do some tests which “shines light” through that real population and creates some test results. If the light is completely accurate, the test probabilities and real probabilities match up. Everyone who tests positive is actually “positive”. Everyone who tests negative is actually “negative”.

But this is the real world. Tests go wrong. Sometimes the people who have cancer don’t show up in the tests, and the other way around.

Bayes’ Theorem lets us look at the skewed test results and correct for errors, recreating the original population and finding the real chance of a true positive result.

## Bayesian Spam Filtering

One clever application of Bayes’ Theorem is in [spam filtering](https://en.wikipedia.org/wiki/Bayesian_spam_filtering). We have

- Event A: The message is spam.
- Test X: The message contains certain words (X)

Plugged into a more readable formula (from Wikipedia):

![\displaystyle{\Pr(\mathrm{spam}|\mathrm{words}) = \frac{\Pr(\mathrm{words}|\mathrm{spam})\Pr(\mathrm{spam})}{\Pr(\mathrm{words})}}](../_resources/d73eca5660a588ae27233882c45d662f.png)

Bayesian filtering allows us to predict the chance a message is really spam given the “test results” (the presence of certain words). Clearly, words like “viagra” have a higher chance of appearing in spam messages than in normal ones.

Spam filtering based on a blacklist is flawed — it’s too restrictive and false positives are too great. But Bayesian filtering gives us a middle ground — we use *probabilities*. As we analyze the words in a message, we can compute the chance it is spam (rather than making a yes/no decision). If a message has a 99.9% chance of being spam, it probably is. As the filter gets trained with more and more messages, it updates the probabilities that certain words lead to spam messages. Advanced Bayesian filters can examine multiple words in a row, as another data point.

## Further Reading

There’s a lot being said about Bayes:

- [Bayes’ Theorem on Wikipedia](https://en.wikipedia.org/wiki/Bayes%27s_theorem)
- [Discussion on coding horror](https://www.codinghorror.com/blog/archives/000850.html)
- [The big essay on Bayes’ Theorem](http://www.yudkowsky.net/rational/bayes)

Have fun!

### Join Over 450k Monthly Readers

![](../_resources/7b3283c8ed81b6abab772a1073853cbb.png)

Enjoy the article? There's plenty more to help you build a lasting, intuitive understanding of math. Join the newsletter and we'll turn Huh? to Aha!

## Other Posts In This Series

1. [A Brief Introduction to Probability & Statistics](https://betterexplained.com/articles/a-brief-introduction-to-probability-statistics/)

2. An Intuitive (and Short) Explanation of Bayes' Theorem

3. [Understanding Bayes Theorem With Ratios](https://betterexplained.com/articles/understanding-bayes-theorem-with-ratios/)

4. [Understanding the Monty Hall Problem](https://betterexplained.com/articles/understanding-the-monty-hall-problem/)

5. [How To Analyze Data Using the Average](https://betterexplained.com/articles/how-to-analyze-data-using-the-average/)

6. [Understanding the Birthday Paradox](https://betterexplained.com/articles/understanding-the-birthday-paradox/)

### Leave a Reply

 186 Comments on "An Intuitive (and Short) Explanation of Bayes’ Theorem"

Sort by:   newest | oldest | most voted

Gavrilo Princep

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

you have a typo, in …

9.6% of mammograms miss breast cancer when it is there (and therefore 90.4% say it is there when it isn’t).

… you meant to say somthing like :

9.6% of mammograms incorrectly indicate breast cancer when it isn’t there, and the other 90.4% correctly say it is not there when, well, it is not there.

**Vote Up0**Vote Down ** Reply
**10 years 1 month ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Thanks Gavrilo — I just fixed it.
**Vote Up0**Vote Down ** Reply
**10 years 1 month ago

Amal

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hey, here’s an interesting bayes problem i came across first in a book (The curious incident of the dog in the night time).

Suppose you are in a game show. You are given the choice of three doors – one of which conceals a valuable prize and the

others conceal a goat.

After you make a choice, the host opens one of the other doors (–one without a prize).

He then gives you the option of staying with the initial choice of door or switching to the other door. The door finally chosen is then opened.

Should you switch, not switch, or does it make no difference what the contestant does?

_____________________________________________
ANSWER
by Bayes theorum you can see that if you switch u’d have a 2:1 advantage.
**Vote Up2**Vote Down ** Reply
**10 years 1 month ago

[Kalid](http://betterexplained.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hi Amal, thanks for dropping by. Yes, I like that question too, it was presented to us as “The Monty Hall” problem when studying computer science.

It’s pretty amazing how counter-intuitive the results can be — switching your choice after you’ve picked “shouldn’t” change your chances, right? I plan on writing about this paradox, too :)

**Vote Up0**Vote Down ** Reply
**10 years 1 month ago

Ed

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Oddly useful! I’ve been reading Bayes explanations for a while, and this one really hit home for me for some reason.

One thing that you might consider adding (something I’ve never seen) is a pie-chart visualization of what’s going on. Basically, you have a pie of 100% of people. 1% of that pie has cancer, so that’s a tiny slice. The test will produce a positive for 80% of that 1% slice + 9.6% of the remaining 99% slice– you can imagine that as a little blue translucent piece of appropriate size that covers most of the 1% slice and a chunk of the 99% slice. From that mental image, it’s obvious what’s going on– there’s a lot more blue on the 99% than on the 1%. Might be too complicated, but hey. :) Anyways, thanks.

**Vote Up2**Vote Down ** Reply
**9 years 10 months ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hey Ed, thanks for the comment. I agree — some type of chart may make the relationship that much clearer. Appreciate the suggestion, I’ll put one together.

**Vote Up0**Vote Down ** Reply
**9 years 9 months ago

Lee

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Bayes theorem can also be thought of as
True Positives
——————————–
True Positivees + False Positives

So a large number of false positives reduces the accuracy of the test because the denominator increases.

**Vote Up6**Vote Down ** Reply
**9 years 8 months ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Thanks Lee! That’s a great way to put it.
**Vote Up0**Vote Down ** Reply
**9 years 8 months ago

[Randy](http://randy.strausses.net/tech/montyhall.htm)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

About Monty Hall- the Bayes application to this seems very forced. The Monty Hall problem is a simple probability problem, or it can be viewed as a partitioning problem. See:

 http://randy.strausses.net/tech/montyhall.htm
Using Bayes for this makes it needlessly complex, not “betterExplained”.

Similarly, the article above is needlessly complex- nuke the first equation and leave the simpler one. You just pulled it out of thin air anyway- it doesn’t help anyone.

The usual diagram, given in HS stats classes, is a rectangle, with A, ~A on the top, B, ~B on the side. Say A is .9 and B is .2. The area of the small quadrant (.02), is the probability of A and B both happening. This area can be also viewed as P(A|B)*P(B) or P(B|A)*P(A). You have to explain why, but it’s pretty evident from the diagram. Then just equate these two and divide by P(B) and you have the simpler equation.

**Vote Up0**Vote Down ** Reply
**9 years 7 months ago

[Kalid](http://instacalc.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hi Randy, Bayes may be overkill for the Monty Hall problem, but it’s interesting to see that it can apply there as well.

Yes, the diagram you mention may be a helpful addition to the discussion above, appreciate the feedback.

**Vote Up1**Vote Down ** Reply
**9 years 7 months ago

[numerodix](http://www.matusiak.eu/numerodix/blog/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Just wanna say thank you for writing this. I know about the original article and I tried reading it but somewhere along the way I got lost and couldn’t follow it.

**Vote Up0**Vote Down ** Reply
**9 years 7 months ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hi numerodix, you’re welcome — I found the original article interesting but a bit long as well, so I decided to summarize it here.

**Vote Up0**Vote Down ** Reply
**9 years 7 months ago

[Проверенный чёрт](http://ivbeg.livejournal.com/83393.html)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

**Пример ведения IT блога…**

Я редко выделяю какой-то отдельный англоязычный блог, но вот этот, BetterExplained , заслуживает внимания….

**Vote Up0**Vote Down ** Reply
**9 years 7 months ago

[Иван Бегтин | Пример ведения IT блога](http://ivan.begtin.name/2007/11/28/primer-vedeniya-it-bloga/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] An Intuitive (and Short) Explanation of Bayes’ Theorem […]
**Vote Up0**Vote Down ** Reply
**9 years 7 months ago

Matteo

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hello, I just came upon this site and I’m finding it beautiful. I think I spotted an error in this article, though.

When you say:

“”Of those 100, 80 will test positive” rather than “80% of the 1% will test positive”).”,

you probably wanted to say: “rather than ‘80% of the 100% will test positive'”.
**Vote Up0**Vote Down ** Reply
**9 years 2 months ago
**

Tobby

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

I think the author probably got it right.
**Vote Up0**Vote Down ** Reply
**9 days 1 hour ago

[Kalid](http://instacalc.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hi Matteo, thanks for the comment. The statement actually refers to the original 1%, so it’s giving a way of giving compound percentages (80% of 1% vs. 80 out of 10,000).

**Vote Up0**Vote Down ** Reply
**9 years 2 months ago

Anonymous

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

wow thank you so much for this, you really did a good job explaining it, i have my AP statistics exam today at noon so this might save me :)

**Vote Up0**Vote Down ** Reply
**9 years 1 month ago

John D Stackpole

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Randy, back on Nov 7 2007, suggested using overlapping rectangles – Venn diagrams – to help clarify the Rev. Bayes. In their book “Chances Are…” (Viking Penguin, 2006), Kaplan & Kaplan did so on pp. 184 ff. Indeed it does help.

**Vote Up0**Vote Down ** Reply
**8 years 5 months ago

Anonymous

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

you. are. the. best.
**Vote Up0**Vote Down ** Reply
**8 years 2 months ago

patty

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

oh my god this is the dogs bollocks for my molecular phylogenetics revision!
**Vote Up0**Vote Down ** Reply
**8 years 2 months ago

[Kalid](http://betterexplained.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

@Anonymous: Thanks!

@John: Appreciate the reference. Another explanation with a venn diagram: http://blog.oscarbonilla.com/2009/05/visualizing-bayes-theorem/

@Anonymous: Thank you!
@Patty: Glad it helps :)
**Vote Up0**Vote Down ** Reply
**8 years 1 month ago

[Better Explained « Xavier Seton’s Blog](https://xavierseton.wordpress.com/2009/05/07/better-explained/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] Statistics: Combinations & permutations, Birthday Paradox, Bayes’ Theorem, […]

**Vote Up0**Vote Down ** Reply
**8 years 1 month ago

Dan Weisberg

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

This is one of the best explanations I’ve found. Perhaps we can see if I really understand it by trying a real world problem I’m wrestling with.

Here’s the data:
– The odds of a chest pain (CP) being caused by a heart attack is 40%.

– The odds of a CP being caused by other factors (anxiety, depression, etc.) is 60%.

– The odds of a heart attack occurring to a female above age 50 is 80%.
– The odds of a heart attack occurring to a female under age 50 is 20%.

I am presented with a 24 year old female who says she is having chest pain. What is the probability that her chest pain is caused by a heart attack? Is it 0.4 x 0.2 = 0.08?

Also, 78% of patients having heart attacks present with diaphoresis (sweating), so 22% of patients having heart attacks don’t sweat. This female is not sweating, so are the odds of her having a heart attack 0.22 x 0.08 = 0.0176?

Thank you!
**Vote Up2**Vote Down ** Reply
**7 years 8 months ago

Emily Riley

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Thanks for writing this!! Even my stats prof was making this too difficult for everyone, but you have simplified it for me. I now have an understanding of the Bayes formula (enough to write my midterm this morning :D ).

**Vote Up1**Vote Down ** Reply
**7 years 7 months ago

AYUSH

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

thanks! finally got the concept behind bayes rule
**Vote Up0**Vote Down ** Reply
**7 years 6 months ago
**

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

@Ayush: Glad it helped!
**Vote Up0**Vote Down ** Reply
**7 years 6 months ago

 [(L)](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/#!parentId=2979)