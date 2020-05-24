What’s wrong with Bayes « Statistical Modeling, Causal Inference, and Social Science

« [Hey—the 2nd-best team in baseball is looking for a Bayesian!](https://statmodeling.stat.columbia.edu/2019/12/02/hey-the-2nd-best-team-in-baseball-is-looking-for-a-bayesian/)

[“Would Republicans pay a price if they vote to impeach the president? Here’s what we know from 1974.”](https://statmodeling.stat.columbia.edu/2019/12/03/would-republicans-pay-a-price-if-they-vote-to-impeach-the-president-heres-what-we-know-from-1974/) »

## What’s wrong with Bayes

Posted by [Andrew](https://statmodeling.stat.columbia.edu/author/andrew/) on3 December 2019, 9:38 am

[My problem](https://statmodeling.stat.columbia.edu/2019/12/02/whats-wrong-with-bayes-whats-wrong-with-null-hypothesis-significance-testing/) is not just with the methods—although I do have problems with the method—but also with the ideology.

**My problem with the method**

It’s the usual story. Bayesian inference is model-based. Your model will never be perfect, and if you push hard you can find the weak points and magnify them until you get ridiculous inferences.

One example we’ve talked about a lot is the simple case of the estimate,
theta_hat ~ normal(theta, 1)
that’s one standard error away from zero:
theta_hat = 1.

Put a flat prior on theta and you end up with an 84% posterior probability that theta is greater than 0. Step back a bit, and it’s saying that you’ll offer 5-to-1 odds that theta>0 after seeing an observation that is statistically indistinguishable from noise. That can’t make sense. Go around offering 5:1 bets based on pure noise and you’ll go bankrupt real fast. [See here](https://statmodeling.stat.columbia.edu/2013/11/21/hidden-dangers-noninformative-priors/) for more discussion of this example.

That was easy. More complicated examples will have more complicated problems, but the way probability works is that you can always find some chink in the model and exploit it to result in a clearly bad prediction.

What about non-Bayesian methods: they’re based on models too, so they’ll also have problems? For sure. But Bayesisan inference can be worse because it is so open: you can get the posterior probability for *anything*.

Don’t get me wrong. I still think Bayesian methods are great, and I think the proclivity of Bayesian inferences to tend toward the ridiculous is just fine—as long as we’re willing to take such poor predictions as a reason to improve our models. But Bayesian inference can lead us astray, and we’re better statisticians if we realize that.

**My problem with the ideology**

As the saying goes, the problem with Bayes is the Bayesians. It’s the whole religion thing, the people who say that Bayesian reasoning is just rational thinking, or that rational thinking is necessarily Bayesian, the people who refuse to check their models because subjectivity, the people who try to talk you into using a “reference prior” because objectivity. Bayesian inference is a tool. It solves some problems but not all, and I’m exhausted by the ideology of the Bayes-evangelists.

Tomorrow: What’s wrong with null hypothesis significance testing.
AddThis Sharing Buttons

[Share to Facebook![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-facebook-1' style='width: 32px%3b height: 32px%3b' class='at-icon at-icon-facebook js-evernote-checked' data-evernote-id='1135'%3e%3ctitle id='at-svg-facebook-1'%3eFacebook%3c/title%3e%3cg%3e%3cpath d='M22 5.16c-.406-.054-1.806-.16-3.43-.16-3.4 0-5.733 1.825-5.733 5.17v2.882H9v3.913h3.837V27h4.604V16.965h3.823l.587-3.913h-4.41v-2.5c0-1.123.347-1.903 2.198-1.903H22V5.16z' fill-rule='evenodd'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to Twitter![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-twitter-2' style='width: 32px%3b height: 32px%3b' class='at-icon at-icon-twitter js-evernote-checked' data-evernote-id='1136'%3e%3ctitle id='at-svg-twitter-2'%3eTwitter%3c/title%3e%3cg%3e%3cpath d='M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336' fill-rule='evenodd'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to Print![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-print-3' style='width: 32px%3b height: 32px%3b' class='at-icon at-icon-print js-evernote-checked' data-evernote-id='1137'%3e%3ctitle id='at-svg-print-3'%3ePrint%3c/title%3e%3cg%3e%3cpath d='M24.67 10.62h-2.86V7.49H10.82v3.12H7.95c-.5 0-.9.4-.9.9v7.66h3.77v1.31L15 24.66h6.81v-5.44h3.77v-7.7c-.01-.5-.41-.9-.91-.9zM11.88 8.56h8.86v2.06h-8.86V8.56zm10.98 9.18h-1.05v-2.1h-1.06v7.96H16.4c-1.58 0-.82-3.74-.82-3.74s-3.65.89-3.69-.78v-3.43h-1.06v2.06H9.77v-3.58h13.09v3.61zm.75-4.91c-.4 0-.72-.32-.72-.72s.32-.72.72-.72c.4 0 .72.32.72.72s-.32.72-.72.72zm-4.12 2.96h-6.1v1.06h6.1v-1.06zm-6.11 3.15h6.1v-1.06h-6.1v1.06z'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to Email![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-email-4' style='width: 32px%3b height: 32px%3b' class='at-icon at-icon-email js-evernote-checked' data-evernote-id='1138'%3e%3ctitle id='at-svg-email-4'%3eEmail%3c/title%3e%3cg%3e%3cg fill-rule='evenodd'%3e%3c/g%3e%3cpath d='M27 22.757c0 1.24-.988 2.243-2.19 2.243H7.19C5.98 25 5 23.994 5 22.757V13.67c0-.556.39-.773.855-.496l8.78 5.238c.782.467 1.95.467 2.73 0l8.78-5.238c.472-.28.855-.063.855.495v9.087z'%3e%3c/path%3e%3cpath d='M27 9.243C27 8.006 26.02 7 24.81 7H7.19C5.988 7 5 8.004 5 9.243v.465c0 .554.385 1.232.857 1.514l9.61 5.733c.267.16.8.16 1.067 0l9.61-5.733c.473-.283.856-.96.856-1.514v-.465z'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()[Share to More![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 32 32' version='1.1' role='img' aria-labelledby='at-svg-addthis-5' style='width: 32px%3b height: 32px%3b' class='at-icon at-icon-addthis js-evernote-checked' data-evernote-id='1139'%3e%3ctitle id='at-svg-addthis-5'%3eAddThis%3c/title%3e%3cg%3e%3cpath d='M18 14V8h-4v6H8v4h6v6h4v-6h6v-4h-6z' fill-rule='evenodd'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)]()24

Filed under [Bayesian Statistics](https://statmodeling.stat.columbia.edu/category/bayesian-statistics/), [Miscellaneous Statistics](https://statmodeling.stat.columbia.edu/category/miscellaneous-statistics/), [Sociology](https://statmodeling.stat.columbia.edu/category/sociology/)

[Comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#respond) ([RSS](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/feed/)) |  [Permalink](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/)

### 83 Comments

1. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Anonymous  says:

[December 3, 2019 at 12:36 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199360)

“exploit it to result in a clearly bad prediction.”
Three points:

(1) The goal isn’t to make a good prediction. That is usually impossible given the information put into the problem. The goal is “to do the best you can with the information used, however good that may be”.

(2) If it’s that “clearly” then you haven’t used all the information available. There’s been a long history of mass producing “bad Bayes” examples this way. Simply do a bayesian analysis without using all the information that one’s intuition uses, and then claim Bayes doesn’t agree with the intuitive answer. It’s a favorite strategy of frequentist fanatics.

(3) I wont go through a lengthy analysis of your example (it’s been done before and had no impact). Just let me say that in your example, I believe you’re confusing two very different states of information. You can have either (a) “the frequency distribution of a changing lambda is normal” or (b) “lambda is fixed with an uncertainty described a normal”. If you’re frequentist or worse yet, half-frequentist/half-baysian then you’re liable to confuse these two very different types of information and easily generate problems/paradoxes.

Perhaps it would be more accurate to say “the problem with Bayes is half-frequentists/half-bayesians”

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199360#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 1:01 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199393)

Anon:

1. Whether or not the goal is to make a good prediction, I do think we want to avoid clearly bad predictions.

2. Exactly: In the example above, there is available information that’s not used in the model. The concern is that we are often in this situation. Researchers commonly make Bayesian statements (or give classical confidence intervals with an implicit Bayesian implication) that don’t make use of relevant information. When above I wrote, “What’s wrong with Bayes,” I was talking about what’s wrong with Bayesian methods as they are used, not what’s wrong with ideal Bayesian methods.

3. Yes, indeed, a few years ago I gave this example at a conference where someone said that Bayesians should be more frequentist and that frequentists should be more Bayesians. I replied that I’d be happy if Bayesians were more Bayesian (including more real information in their models) and if frequentists were more frequentist (evaluating procedures as they are actually done, including forking paths etc).

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199393#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)student  says:

[December 3, 2019 at 1:48 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199449)

>In the example above, there is available information that’s not used in the model.

Sorry if this extremely basic/is an example you’ve expanded on elsewhere, but what additional information is available for this model but not incorporated? I assume that this effects the choice of prior, but I don’t see what prior would be more appropriate in this example.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199449#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 3, 2019 at 3:25 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199556)

You need just slightly more context before you can apply prior information. I mean, what are we measuring? There’s always some information we have once we know that information. For example suppose we’re measuring the number of gallons of milk in people’s fridges… it can’t be negative, and people don’t often buy more than a couple gallons at a time, so an exponential(1) prior might be appropriate. Or we’re measuring the vote differential in percentage points for some relatively close election… maybe normal(0,5) is appropriate… etc

I think the point was an infinitely wide uniform prior is never a good model for any real world problem… but which alternative can’t be specified without knowing something about the actual problem.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199556#respond)

                - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Richard Kennaway  says:

[December 4, 2019 at 11:30 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200358)

If you ask a different question, it will have a different answer. I am not seeing a problem with the original answer to the original question.

If the problem is that an infinite flat prior fails to encode the available information, that is a problem for the original question. There is no sense in complaining that the machine answered the question you actually asked, and not the one that you should have asked.

Besides, the unrealism of the infinite prior is a red herring, at least in this problem. You get a similar posterior probability for theta > 0 from a flat prior on [-10,10]. Or flat on [-50,5]. Or N(-5,10). (Calculated from simulation.) Your prior has to be pretty informative about the sign of theta in the region where most of N(1,1) lies before you get a posterior outside 0.8 to 0.9.

And finally, who estimates the sign of a variable from one observation?

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200358#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 11:58 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200364)

I agree that the example should be a better example. I’ve never liked this example because it obviously seems meaningful to Andrew, but it isn’t that meaningful to me. Basically I’m with you.

Nevertheless, it’s a very typical thing in the recent past at least that people will use some kind of default or “non-informative” prior on problems where information is available, then get posterior inference that makes not very good sense, and then assert that it “must be right” because they followed the rubric.

This is particularly true when the parameter vector is moderate to high dimensional and the “uninformative priors” tend to overwhelmingly pick out stupid unrealistic prior predictive data values.

For example, the “uninformative prior” which is say uniform(-very_big_number, very_big_number) is actually *extremely informative*… it tells you that there’s a 95% chance that the value is outside the range (-very_big_number/20, very_big_number/20). So if “very_big_number” is something like the largest possible float at 1.79e308 or so you’re saying that there’s a really good chance your parameter is bigger than about 9e306

The only sense in which it’s not informative, is that it says nothing about which values within the range where the likelihood is appreciable are more or less likely.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200364#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 4, 2019 at 9:09 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200649)

Richard:

Indeed, the problem is not that the original prior is improper, it’s that it’s too weak.

Also, if you look at the statement of the problem, we’re not estimating from one observation. Theta-hat is an estimate, not a single data point. Imagine an experiment is conducted with unbiased estimate theta-hat with standard error of 1.

Finally, you write, “There is no sense in complaining that the machine answered the question you actually asked, and not the one that you should have asked.” My problem is not with the Bayesian math, it’s with the entire “machine” which includes the social structure by which a uniform or very weak prior is the default. This entire procedure, prior and all, will routinely give bad answers if it is taken seriously. Indeed, the only reason these Bayesian inferences are not so horrible in practice is that practitioners *don’t* go around making those 5:1 bets.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200649#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Corey](http://itschancy.wordpress.com/)  says:

[December 3, 2019 at 1:32 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199432)

Regarding point (2), even if we take the argument on its own terms we can say that however indistinguishable the observation is from noise it is equally indistinguishable from what would be expected if theta = 2. Maybe 5-to-1 odds for theta > 0 don’t seem so bad in that light.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199432#respond)

2. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Carlos Ungil  says:

[December 3, 2019 at 1:13 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199407)

> I replied that I’d be happy [..] if frequentists were more frequentist (evaluating procedures as they are actually done, including forking paths etc).

Would you? You told us the other day who when someone asked you for a clarification on frequentist methods your response was “Statistical significance doesn’t answer any relevant question. Forget statistical significance and p-values. The goal is not to reject a null hypothesis; the goal is to estimate the treatment effect or some other parameter of your model.”

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199407#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 1:35 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199435)

Carlos:

“Frequentist” described the approach of choosing and understanding statistical procedures based on their frequency properties, i.e. how they would work on repeated use. So, if I do a frequency analysis and determine that classical null hypothesis significance testing has poor frequency properties, in the sense that if it is applied repeatedly it will often lead to bad estimates and bad decisions, then I’m being frequentist.

To put it another way: “frequentist” != null hypothesis significance testing.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199435#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Carlos Ungil  says:

[December 3, 2019 at 2:04 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199470)

Ok.

By the way, talking about “an observation that is statistically indistinguishable from noise” sounds a bit null-hypothesis-significance-testingy.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199470#respond)

3. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Nick Adams  says:

[December 3, 2019 at 1:53 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199457)

Is this a test?
The 84% is one minus the one sided p-value but you shouldn’t bet using that.
For betting you need the likelihood ratio which is about 1.6.

If you have no other information then the prior odds equal one and the post odds are 1.6.

So a bookmaker would offer 3/2 not 5/1.
(Disclaimer: I often bet on the horses and usually lose)

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199457#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 5:29 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199714)

Nick:

I can see why you usually lose when you bet! The math in my above post is correct, as I’m talking about a bet on theta being positive. In this example, Pr(theta>0|y) = 0.84, i.e., Pr(theta>0|y) / Pr(theta<0|y) = 5.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199714#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Nick Adams  says:

[December 3, 2019 at 6:30 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199804)

But doesn’t likelihood give a more plausible answer?

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199804#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 3, 2019 at 7:04 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199856)

so I think you’re doing dnorm(1,1,1) / dnorm(0,1,1) which is about 1.65, so you’re comparing the likelihood of mu = 1 to mu = 0 but the bet isn’t if mu = 0 we pay 1.65 and if mu = 1 we keep your dollar, the bet is “if mu is less than 0 we pay 5 vs if mu is greater than 0 we keep your dollar”

the likelihood ratio answers the wrong question, there are a continuum of possible mu values.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199856#respond)

                - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Nick Adams  says:

[December 3, 2019 at 7:30 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199890)

I’m using generalised maximum likelihood of a composite hypothesis, mu=0 being the supremum of mu less than 0 compared with mu=1 being the supremum of mu greater than zero.

See:
A Law of Likelihood for Composite Hypotheses, Zhiwei Zhang.

The Strength of Statistical Evidence for Composite Hypotheses: Inference to the Best Explanation David R. Bickel.

Both preprints, easily googled.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199890#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 7:36 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199894)

Nick:

This seems super-complicated, given that I just want to know Pr(theta>0|y), which I can compute directly from the posterior distribution with no supremums etc. needed. I’m not interested in the probability that theta=1. y=1 is just the point estimate, that’s all.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199894#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 3, 2019 at 7:55 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199919)

Doesn’t this totally break down if you have a high thin spike in your likelihood… like p(mu|data) ~ 10% uniform[.9999,1.0001] mixed with say 90% [-10,10]

The maximum likelihood for it to be positive is 500 (0.1 * 1/.0002) and the max likelihood for negative is .9/20 = .045 giving you 11111 to 1 odds?

whereas the probability to be positive if you normalize this likelihood is about .9 * 1/2 + .1 = 0.55

I don’t see why we should care about that first calculation.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199919#respond)

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Nick Adams  says:

[December 3, 2019 at 8:16 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199942)

I guess for most real-world problems the likelihood function is reasonably smooth without discontinuities. If you have a really weird likelihood function (and you’re not aware of such) it’s probably going to cause a lot of problems for any method: Bayesian, frequentist or maximum likelihood.

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 3, 2019 at 9:32 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199998)

This was just a way to point out that your calculation is only sensitive to the value at a single point. The general problem still holds for any function. Probability depends both on the density and the width of the interval, where supremum of likelihood depends only on a point density.

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 3, 2019 at 9:56 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200013)

For example, suppose you have something like dgamma(x+1,2,1) which has a peak at x=0.

about 26% of the probability mass is left of 0, and 74% is to the right of 0.

which is the better bet? 50/50 which you get for the likelihood ratio thing, or 25/75 for the probability?

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Keith O'Rourke](https://statmodeling.stat.columbia.edu/author/keithor/)  says:

[December 4, 2019 at 8:14 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200265)

Nick:

For “most real-world problems the likelihood function is reasonably smooth without discontinuities” no, actually it is discrete unless some day someone finds a way to determine observations to all decimal places (not finite).

Thinking one can can actually observe _continuous_ outcomes leads to all sorts of anomalies.

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 8:55 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200281)

Keith, although I agree that all real world problems involve data measured to finite precision (it’s usually not even that many decimal places, between say 2 and 6) nonstandard analysis shows us that discrete and continuous aren’t really that different provided precision is sufficiently high. My example with a high peak could easily be made continuous, even infinitely smooth, just convolve my function with a normal distribution of width .00000001 ![1f609.png](../_resources/999d8ac1c57fd24fe65f70fab48dbc6d.png)

it’s not the rapid change I create that makes Nick’s suggested method problematic, that’s just a device to amplify the problem to make it more visible, it’s the fact that he makes a global decision on the basis of local information.

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Corey](http://itschancy.wordpress.com/)  says:

[December 3, 2019 at 8:44 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199962)

Those are about formalizing measures of evidence, but for bets you need a decision theory — something like this, I imagine: https://projecteuclid.org/euclid.ejs/1385995295

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199962#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 7:05 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199857)

Nick:

Likelihood gives you the answer to the question, what are the relative probabilities of theta=1 and theta=0. But that’s not typically a question of direct interest. Pr(theta>0) is what I’m after here.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199857#respond)

                - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[wolf vanpaemel](https://twitter.com/wolfvanpaemel)  says:

[December 4, 2019 at 5:05 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200543)

If you are assuming the prior is symmetric around 0 (which I think you are doing), Pr(theta>0|y)/Pr(theta0″ vs “theta0” vs “theta without inequality restriction” is (again assuming a symmetric prior around 0) equal to 2*.84, which seems to be a less counterintuitive result. (I am aware of the fact that you hate Bayes factors, but given that Pr(theta>0|y)/Pr(theta<0|y) can be interpreted as a Bayes factor, you might as well consider a more relevant Bayes factor.)

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200543#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Anonymous  says:

[December 4, 2019 at 5:12 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200549)

(something went wrong here. new try)

If you are assuming the prior is symmetric around 0 (which I think you are doing), Pr(theta>0|y)/Pr(theta0 vs theta0 vs theta without inequality restriction is (again assuming a symmetric prior around 0) equal to 2*.84, which seems to be a less counterintuitive result.

(I am aware of the fact that you hate Bayes factors, but given that Pr(theta>0|y)/Pr(theta<0|y) can be interpreted as a Bayes factor, you might as well consider a more relevant Bayes factor.)

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200549#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 4, 2019 at 9:05 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200643)

Wolf:

I don’t quite understand your comment. I think it is a very reasonable question to ask: What is the probability that the average treatment effect is positive? In this model, that is Pr(theta>0) and the posterior probability Pr(theta>0|y) is 0.84 in this case. If you believe your model, you’ll be willing to say that there’s a 5/6 chance that theta is positive, that is, you’d bet 5:1 on this. It’s just a probability. You can call it a Bayes factor if you want; it doesn’t really matter one way or the other!

It’s funny to see how many comments this example received. I think the problem is that I’ve thought about this example a lot, but I’ve never formally written it up. Because the example is so familiar to me, I presented it in abbreviated form, which led to confusion.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200643#respond)

4. ![77f083909d955b715846250a33340a14](../_resources/586a0fbaba0f5cfeef47b09881cbccde.jpg)[Bob Carpenter](https://bob-carpenter.github.io/)  says:

[December 3, 2019 at 3:03 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199536)

In your example, is the model just
y ~ normal(theta, 1)

with data y and parameter theta and an improper uniform prior on theta and a single observation y = 1? Then the claim is Pr[theta > 0 | y] = 0.84 given the model?

If so, I don’t see a problem unless it’s the improper prior, which will defeat running calibration tests as there is no way to generate fake data. Otherwise, you just seem to be saying the model is wrong.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199536#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 3, 2019 at 3:20 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199552)

I think at least part of the point was the improper prior makes no sense.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199552#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 5:27 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199711)

Bob:

What Daniel said. The improper prior typically makes no sense in these situations, which is why it would a ludicrously bad idea to be betting 5:1 or anything like that on Pr(theta > 0|y) based on seeing an estimate that’s 1 standard error away from zero. The fact that the bet looks so wrong is telling us that we have prior information not in the model, and Bayesians typically duck this problem by just not thinking hard about the implications of this posterior.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199711#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Keith O'Rourke](https://statmodeling.stat.columbia.edu/author/keithor/)  says:

[December 3, 2019 at 5:58 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199754)

> Bayesians typically duck this problem by just not thinking hard about the implications of this posterior.

That seems all too common.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199754#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Luke  says:

[December 3, 2019 at 9:15 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199981)

So the problem with Bayes is not being Bayes enough.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199981#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Keith O'Rourke](https://statmodeling.stat.columbia.edu/author/keithor/)  says:

[December 4, 2019 at 2:08 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200435)

Not being Bayesian enough in the sense of fully appreciating how to do good empirical inquiry utilizing Bayes theorem and/or not have a truly scientific attitude but just wanting to pull the Bayesian crank and submitting an invoice or claiming to have made aa academic contribution.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200435#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Richard Kennaway  says:

[December 4, 2019 at 4:43 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200531)

Can you say why “the bet looks so wrong”? Because I do not see anything wrong with it (see my other comment).

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200531#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 4, 2019 at 9:07 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200645)

Richard:

The bet looks so wrong because it’s a strong statement (Pr(theta>0) = 5/6) based on data that are indistinguishable from noise. If you go around making 5:1 bets based on noise, you’re just overreacting all the time.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200645#respond)

                - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Richard Kennaway  says:

[December 5, 2019 at 12:31 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201089)

According to the simulation I made, confirmed by considering what it is telling me about the underlying mathematics, any prior that is flattish over the bulk of N(1,1) (say, 1 +/- 3) will give a posterior probability for theta > 0 of around 5 to 1. Betting at those odds is fair. If someone is offering even money on that bet, bet that theta > 0. You will win 5 times out of 6.

It does not matter what the prior looks like outside that range. In fact, the wider the prior, the less like noise a single observation of 1 (or anything else) looks like. By the definition of the puzzle, a single observed value t narrows the posterior down to something very close to N(t,1), and exactly so in the limit of the infinite flat prior.

In what sort of situation do you know the standard deviation and shape of a distribution, but not its mean? The example that I am imagining is measuring something of unknown length, with a device whose measurement errors are distributed as N(0,1). For convenience I take the standard error as the unit of length. Let us suppose it is a micrometer gauge. I measure an object that I can see is about an inch long, but the gauge is far more accurate than my feeling for what an inch looks like, so my prior range of uncertainty might be a few thousand standard deviations of the gauge. The gauge reads 1 inch plus 1 standard deviation. Is the object more or less than one inch long? 5:1 that it’s greater.

When statistics is being applied to some practical end, a single observation almost always is indistinguishable from noise. This hypothetical puzzle is not such a situation. A single measurement from a micrometer is very much distinguishable from noise.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1201089#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Keith O'Rourke](https://statmodeling.stat.columbia.edu/author/keithor/)  says:

[December 5, 2019 at 1:16 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201117)

Richard:

Agree you will win 5 times out of 6 IFF the “truth” is a random draw from a prior that is flattish over the bulk of N(1,1).

A reassurance for it being roughly like that, would require a large amount of credible background knowledge that you don’t have.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1201117#respond)

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 5, 2019 at 1:41 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201137)

To even say “5 times out of 6” is problematic. In a given instance, you will either win, if after collecting a lot of data everyone agrees that the “truth” is a positive number. Or you will lose, if after a lot of data, the truth is a negative number.

To say 5 times out of 6 you have to define some population over which you will use this procedure. And then, the population of truth values shouldn’t be uniform over the bulk of N(1,1) but rather more or less contained in some reasonably flat distribution over the true values of the problems this procedure will be put to use to detect…

In which case the Bayesian model is also a Frequency model.

But if the procedure is “ask some people about what they’re doing, then formulate a prior for that problem, and then collect one data point, and apply the likelihood to that problem and then use the posterior to make bets” then the actual frequency with which you win will be a function of how well you set your priors for each individual problem.

With this Bayesian procedure, the frequency of actually winning is not the same as the credence you give to the idea that you will win because there is no real world frequency based probability for “the uses you will put your procedure to”… except of course when there is, like if you’re an analytical chemistry lab and doing the same water quality test day in and day out…

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 5, 2019 at 11:18 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201487)

Richard:

You speak of “any prior that is flattish over the bulk of N(1,1).” My point is that such a prior is really strong; it assumes a high possibility of very large effects, enough so to yield that very strong 5:1 odds.

To put it another way: if, after seeing theta-hat = 1 with that model, you’re really willing to bet 5:1 that theta>0, then, yeah, that flat prior might be reasonable. If not, you should be concerned. What I’m saying is that in the typical examples we see, we are not and should not feel comfortable with that 5:1 bet, hence we should not be comfortable with that flat prior.

Finally, in my example it’s not a single observation. Theta-hat is an estimate. It’s often reasonable to suppose that theta-hat has an approximately normal sampling distribution with standard deviation approximately equal to the standard error.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1201487#respond)

                        - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 6, 2019 at 3:09 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201618)

Just to try to clear up some possible confusion: In an earlier comment you wrote:

> Indeed, the problem is not that the original prior is improper, it’s that it’s too weak.

You mean a flat prior is weak in the sense that it doesn’t do much shrinkage.

In this comment you’re saying a flat prior is strong in the sense that it yields a strong conclusion (5:1 odds).

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Richard Kennaway  says:

[December 6, 2019 at 7:07 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201740)

Every prior is “strong”, for being that prior and no other. In this discussion we have seen that Uniform(-BIGNUM,BIGNUM) is “strong” because it is so broad, while Uniform(-2,4) is “strong” because it is so narrow. But this deprives the word “strong” of any meaning. What is a “strong” posterior? 5:1 odds is weak for making a one-off high-value decision, and you would be better to hold off, if you can, while you collect better data. But if you’re a professional gambler on the horses, those sorts of odds are literally your bread and butter.

Is the problem with the original example that in realistic applications of statistics you have no way to express your prior knowledge in terms of exact numbers, and therefore you want your posterior to be robust to any reasonable choice of prior? Then how robust that 5:1 result is will depend on the range of reasonable priors. For the micrometer example, the naked eye gives me no information on the scale of thousandths of an inch, so every reasonable prior is flattish everywhere that matters. In situations where one does use statistics practically, with so little data you could find a reasonable-looking prior to obtain any conclusion you want, and parlaying a single data point into 5:1 odds is not useful.

The Bayesian machine is indifferent to these considerations. It will answer the question you ask of it.

                        - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 6, 2019 at 7:18 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201747)

Richard: I just wanted to point out that Andrew has called the flat (or flattish) prior both too weak and too strong in this discussion. I was only trying to clear up some linguistic confusion.

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 6, 2019 at 8:50 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201790)

Erik: Yes, exactly.

Richard: It is a Bayesian principle that if a model consistency gives predictions that are wrong in a particular direction, that model should be fixed. If I were to consistently bet on the sign of effects whose estimates are 1 se from 0, I’m pretty sure I’d get the sign wrong more than 1/6 of the time. Hence there’s a problem with the model.

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Keith O'Rourke](https://statmodeling.stat.columbia.edu/author/keithor/)  says:

[December 6, 2019 at 7:59 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1201772)

The prior here is simply just too wrong.

(Too weak in not reflecting the usual reality of smallish effects and too strong by being so wrong).

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1201772#respond)

5. ![f781bed2b34563423d4b2cabfbe3f049](../_resources/4902a9776c04108bf809a16b6fbd76db.png)Danielle Navarro  says:

[December 3, 2019 at 9:21 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1199986)

I tend to agree. I’m not opposed to the idea of inverse probability, and to the extent I trust any statistical inference procedure I tend toward Bayesianism. In principle I think it ought to be possible to write down the model and prior that properly captures what the data analyst knows or believes, update that knowledge via Bayes rule, and so on. In practice, I think Bayesian data analysts are prone to specifying models poorly, not doing sufficient model checking, and relying on summary measures (most egregiously, the Bayes factor) that can be very sensitive to uninteresting or unimportant characteristics of the prior, the model and even the data.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1199986#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 9:40 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200002)

Danielle:
Your comment makes me think of an analogy between the following two things:
– Model checking in Bayesian statistics, and
– The self-correcting nature of science.

The story of model checking in Bayesian statistics is that the fact that Bayesian inference can give ridiculous answers is a good thing, in that, when we see the ridiculous answer, this signals to us that there’s a problem with the model, and we can go fix it. This is the idea that we would rather have our methods fail loudly than fail quietly. But this all only works if, when we see a ridiculous result, we confront the anomaly. It doesn’t work if we just accept the ridiculous conclusion without questioning it, and it doesn’t work if we shunt the ridiculous conclusion aside and refuse to consider its implications.

Similarly with the self-correcting nature of science. Science makes predictions which can be falsified. Scientists make public statements, many (most?) of which will eventually be proved wrong. These failures motivate re-examination of assumptions. That’s the self-correcting nature of science. But it only works if individual scientists do this (notice anomalies and explore them) and it only works if the social structure of science allows it. Science doesn’t self-correct if scientists continue to stand by refuted claims, and it doesn’t work if they attack or ignore criticism.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200002#respond)

        - ![f781bed2b34563423d4b2cabfbe3f049](../_resources/4902a9776c04108bf809a16b6fbd76db.png)Danielle Navarro  says:

[December 3, 2019 at 9:53 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200011)

Under the circumstances I think it would be best if I did not comment much on this analogy. Suffice it to say I agree with much of what you’re saying here but would also argue that there are relevant respects in which the two scenarios are quite different. Perhaps another time, or in another forum :-)

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200011#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 3, 2019 at 10:16 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200020)

Danielle:

Sure, these are two completely different situations. My point with the analogy is that if a system produces failure, this can be bad (if the failures are not recognized as failures, or if the failures are avoided), or it can be good (if the failures are used as opportunities for improvement. Bayesian inference can easily fail spectacularly. I’m with Jaynes that these failures are good news as they can be great opportunities for learning. But if someone were to perform a Bayesian inference, get ridiculous conclusions, and then bet on these conclusions or otherwise act as if they are real, this can cause problems. Or if people perform Bayesian inferences and then just ignore the inferences that don’t make sense, then the result is a sort of minefield where later researchers have to step carefully to avoid the bad conclusions.

It’s similar with scientific research in general, I think. But I agree that, in other ways, the society of scientific research is different than a single statistical model, Bayesian or otherwise. I don’t want the details of the imperfect analogy to distract from whatever understanding we have of each situation.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200020#respond)

                - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Phil  says:

[December 4, 2019 at 1:13 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200085)

I’m sure everyone already knows this anecdote: Supposedly some famous physicists — Einstein and Pauli? Bell? Dirac? — were once arguing about the consistency of quantum mechanics. They kept proposing thought experiments, working out the answers, and finding that everything worked out and gave sensible answers. It seemed like an afternoon wasted until they stumbled on two different ways of solving a problem that gave different answers. “Aha!”, said one of them, “now we’re getting somewhere.”

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200085#respond)

6. ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 8:02 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200256)

Since we’re interested in P(theta > 0 | y), the value zero is apparently special. To make this explicit, reparameterize theta into its sign and absolute value. Put a uniform prior on the sign, i.e. P(theta 0)=1/2, but don’t put a prior on the absolute value. Now if you observe y=1 then the MLE of |theta| is zero! I think it’s kind of interesting how much information is in that prior on the sign.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200256#respond)

    - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 8:06 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200259)

The prior on the sign should read: P(theta less than 0)=P(theta bigger than 0)=1/2.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200259#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 9:02 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200282)

Can you explicate this a bit. I don’t see how the maximum likelihood estimate for the absolute value is zero. it still seems like it should be 1.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200282#respond)

7. ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 9:24 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200293)

Sure. Since there’s a prior on the sign of theta, the only parameter is |theta|. The likelihood is

lik(|theta|)= 0.5 * phi(y+|theta|) + 0.5 * phi(y-|theta|),

where phi is the standard normal density. If you put any value for y between -1 and 1 and plot the likelihood, you’ll see it’s decreasing.

y=1
abs.theta=seq(0,2,0.01)
lik=0.5*dnorm(y,abs.theta,1) + 0.5*dnorm(y,-abs.theta,1)
plot(abs.theta,lik)
abs.theta[which.max(lik)] # mle
I could send you the proof if you’re interested.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200293#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 10:00 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200312)

As Carlos points out, there are two parameters, one is p(positive) which has a prior of 0.5 but the posterior will be something else. Without thinking too hard about it I’d expect it to be around the tail probability of normal(1,1) to be positive.

basically I don’t expect your reparameterization to change the inference at all,

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200312#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Carlos Ungil  says:

[December 4, 2019 at 3:15 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200475)

> Since there’s a prior on the sign of theta, the only parameter is |theta|. The likelihood is

> lik(|theta|)= 0.5 * phi(y+|theta|) + 0.5 * phi(y-|theta|),

That’s not a y ~ N(theta,1) model with “a prior on the sign of theta”. That’s a 50/50 mixture of two normals N(theta,1) and N(-theta,1).

There is not such a thing as “the sign of theta” because both |theta| and -|theta| define the same model.

That likelihood function is symetric on both |theta| and y, the sign of the data doesn’t matter either.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200475#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 3:45 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200495)

It’s definitely confusing, a weird model. The weird features are only seen in the absolute value of the theta though, you can do perfectly fine inference on the abs(theta),sign pair itself (which together define theta) and get what’s expected: MAP estimate is theta=1.

I think I have this right below:

https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200465

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200495#respond)

8. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Carlos Ungil  says:

[December 4, 2019 at 9:36 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200298)

> there’s a prior on the sign of theta

What does that mean? If you mean that there is a parameter with possible values {+,-} and prior {1/2, 1/2} then the posterior won’t be the same.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200298#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Carlos Ungil  says:

[December 4, 2019 at 10:54 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200338)

If I’m not mistaken, in the « standard » problem, the likelihood L(theta) is proportional to exp[-1/2*(1-theta)^2] and the MLE is theta=1.

If we separate the sign and absolute value the likelihood L(sign,abs) is proportional to exp[-1/2*(1-sign*abs)^2] and the MLE is sign=+1, abs=1.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200338#respond)

        - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 12:11 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200370)

Carlos, Daniel:

Suppose you observe y ~ N(theta,1) and you’re interested in the sign of theta. You can choose not to put a prior on theta and do frequentist inference, for example test H0 : theta > 0. Or you can put a prior on theta (proper or not) and compute P(theta > 0 |y). I just wanted to point out something in between, namely putting a prior on the sign of theta but not its absolute value. This “semi-Bayesian” approach has some interesting features. For instance, contrary to the purely frequentist approach we can talk about P(theta > 0 |y). If you observe y=1, then the MLE of |theta| is zero and hence the MLE of P(theta > 0 |y=1) is 1/2.

I’m not saying that the semi-Bayesian approach is better or anything. I just think it’s kind of interesting. I got the term “semi-Bayes” from Greenland, S. (1992). “A semi‐Bayes approach to the analysis of correlated multiple associations, with an application to an occupational cancer‐mortality study” Statistics in medicine.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200370#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 12:20 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200374)

So in this case it seems like you aren’t creating a continuous parameter that represents the probability that theta is greater than 0, which means that your prior probability of 1/2 remains as the posterior probability as well, a constant no matter how much data you observe. So if you observe the data {10.1,9.9,11.2,8.4,9.2,11.6} you will still say there’s a 50% chance theta is less than 0.

which is obviously silly.

rather than this, the only sane model is a likelihood like you wrote, but with the parameter p,

so L(theta) = p*dnorm(theta,1,1) + (1-p)*dnorm(-theta,1,1)

where theta is the magnitude parameter, and p is the probability of a positive theta.

Your model is equivalent to putting a prior on p that is a delta-function at 1/2, whereas a more reasonable prior on p is beta(1,1) or the same as uniform(0,1), where the expected value is 1/2 but it could range over any logically possible value.

It’s not surprising that if you insist that there will always and forever be a 50% chance that the parameter is negative no matter how much data you collect, that you will find it “kind of interesting how much information is in that prior on the sign.”

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200374#respond)

9. ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 12:31 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200378)

No, that’s not I’m saying. If the observation y is greater than 1 (or less than -1) then the MLE of |theta| is greater than zero. If |y| is very large then the MLE of |theta| will be approximately equal to |y|, and there will be near certainty about the sign of theta.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200378#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 12:37 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200381)

You have only one parameter, the absolute value of theta. How can you learn the sign?

after seeing data like 900 you may learn that the absolute value of the theta is about 900 but you still are 50/50 on it being positive or negative

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200381#respond)

        - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 1:36 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200417)

No, that’s not true.

P(theta > 0 |y) = dnorm(y,|theta|,1) / [ dnorm(y,|theta|,1) + dnorm(y,-|theta|,1) ]

We get the MLE of P(theta > 0 |y) by plugging in the MLE of |theta|. If the observed |y| is large, then the MLE of |theta| will be approximately equal to |y|. If y is large and positive then P(theta > 0 |y) will be approximately 1, and if y is large and negative it will be approximately 0.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200417#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 2:12 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200438)

p(theta > 0 | y) = 0.5 by definition of your prior, which is independent of y.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200438#respond)

                - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 2:19 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200442)

Another way to put this: there’s no possibility for the probability of the sign to be negative vs positive to ever change in your model, it’s not a parameter that has any uncertainty associated with it, it’s a constant.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200442#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 2:25 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200445)

Ok, I’m not sure I’m understanding this correctly, so I take back the previous statements and am now going to analyze this more carefully…

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200445#respond)

            - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 2:58 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200465)

let sign be either -1 or 1 with 50/50 chance. Let atheta be the absolute value parameter. Let p(y | atheta,sign) be the probability of seeing the data if atheta,sign are true.

p(y | atheta,sign) = dnorm(y,sign*atheta,1)

p(atheta,sign | y , background) \propto p(y | atheta,sign,background)p(atheta | backgorund)p(sign | background)

suppose p(atheta | background) = uniform(0,maxfloat)… it’s a constant… drop it
p(atheta,sign=1 | y,background) \propto dnorm(y,atheta,1) * 0.5
p(atheta,sign=-1 | y,background) \propto dnorm(y,-atheta,1) * 0.5

p(atheta,sign=1 | y,background) = dnorm(y,atheta,1)*0.5/ (dnorm(y,atheta,1)*0.5 + dnorm(y,-atheta,1)*0.5)

drop the 0.5s…

so for y large and positive, only the first one has any component and the answer is as you said for the atheta, the MAP estimate is 0.

However, the probability for theta itself looks like a mixture model with two bumps, one around 1, and another around -1.

The MAP estimate for theta itself doesn’t change, I think, since sign=1 is the MAP for sign, and when we plug that in, p(theta | y) = dnorm(y,theta,1) which has a bump around theta and is truncated at theta=0.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200465#respond)

                - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 3:43 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200492)

Sure. If you let sign be either -1 or 1 with probability 1/2 and you put the uniform(0,infty) prior on atheta, then that’s the same as the usual flat prior on theta.

But the semi-Bayesian model I’m talking about does ~not~ have a prior on atheta. So while sign is random, atheta is not. We can talk about p(sgn=1|y) but not about p(atheta|y).

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200492#respond)

                    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 3:55 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200508)

I really don’t know what you mean. I think you’re talking about a hybrid model in which you allow that 50/50 on the sign is a reasonable thing, but you are only allowing inference on atheta using maximum likelihood.

In that model, you can’t do coherent inference on the sign either. I mean, in the Bayesian model you get about 80-90% probability for a positive theta after seeing 1. But in your model, you have to plug in atheta=0 since it’s the max likelihood estimate. At this point you have theta=0 precisely, there is no probability on the sign…

basically that kind of model is incoherent.

also, when you supply the prior on atheta, you don’t get the inference on the theta that’s the same as the uniform prior… because you have this little shadow lump on the symmetric side that only asymptotically for large theta goes away.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200508#respond)

                        - ![91ab0bb8ee0e1b0322630a01dbe76663](../_resources/8ce672e59e3c2a1e341cddabd8b6020c.jpg)Erik  says:

[December 4, 2019 at 4:19 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200519)

Yes, I just put 50/50 on the sign of theta. Then I have a (single) observation from

f(y | atheta)= 0.5*dnorm(y,atheta,1) + 0.5*dnorm(y,-atheta,1).

Now I can do frequentist inference – nothing special. For example, I can try to estimate atheta or p(sign=1|y=1,atheta). Maybe even put confidence intervals around them. Again, I’m not saying this is a great model though.

I’m not sure, but I don’t think you’re right about that “shadow lump”. You can think about a prior that’s symmetric around zero as independently choosing the sign (50/50) and the magnitude.

                        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 4:47 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200535)

RE the shadow lump… well I don’t know what all you’re up to with your inference procedure, but at least in the Bayesian model with a flat prior on atheta, you always have

p(y | atheta, sign)

as two different functions depending on whether sign=1 or sign=-1… unless p(sign=1) = 1 or p(sign=-1) = 1 then you’ve got some posterior probability in a lump symmetrically opposite whatever the main lump is.

so, if you see y = 900 you’ll have essentially nothing… but if you see y=1 you’ll have posterior predictive distribution for future data which are 80 or 90% distributed around the area of 1, and 10-20% distributed around the area of -1

that’s what posterior probability of say 80% that sign greater than 0 means… it means you’ve got future data predicted to be out around the region of atheta 80%, and around the region of -atheta 20%

until posterior probability of sign is near 1, you’ll always have that shadow lump in your posterior predictive distribution.

10. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)TAS  says:

[December 4, 2019 at 3:32 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200481)

Here’s a contextualized example of this problem that’s interesting to think about. Say we randomly sample a school and we’re interested in the probability that the average IQ of this school is higher than 100 (the known standard deviation being 15). We test one student and get 115. So we have:

y ~ normal(theta, 15)
y1 = 115
P(theta > 100|y1)?

So the flat prior gives P ~ 0.84 which indeed seems silly. But what would be a better prior? Given that there are schools for the gifted as well as schools for the intellectually challenged, we shouldn’t pick something too narrow. But if we go with N(100, 20) or something similarr we still get P ~ 0.80, so not that different.

What would be a good prior in this example? I suppose something multimodal (corresponding to normal schools, schools for the gifted, and schools for the intellectually challenged) but relatively narrow around the modes?

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200481#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 4, 2019 at 3:38 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200488)

Although the standard deviation of the population is 15, the standard deviation of the school is not necessarily that at all, nor is the probability of the data particularly symmetric around an average for a school for the gifted or for the challenged… gifted schools should tail off to the right, and be truncated on the left… challenged schools opposite.

so it’s not just the prior that’s problematic here, but also the likelihood.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200488#respond)

        - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)TAS  says:

[December 5, 2019 at 3:58 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200818)

Yeah, I kept the SD fixed as in the original problem which is indeed not realistic, although I’m not sure how important that is here. Good point about the likelihood.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200818#respond)

11. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Ben  says:

[December 4, 2019 at 5:27 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200561)

You say “the people who say that Bayesian reasoning is just rational thinking, or that rational thinking is necessarily Bayesian” and contrast this with your view that “Bayesian inference is a tool. It solves some problems but not all”.

This reminds me of an essay from last year by such a bayesian called “Toolbox-thinking and Law-thinking” which tries to point at the source of such disagreements directly.

Key quote:

> I’ve noticed a dichotomy between “thinking in toolboxes” and “thinking in laws”.

>

> Msr. Toolbox: “It’s important to know how to use a broad variety of statistical tools and adapt them to context. The many ways of calculating p-values form one broad family of tools; any particular tool in the set has good uses and bad uses, depending on context and what exactly you do. Using likelihood ratios is an interesting statistical technique, and I’m sure it has its good uses in the right contexts. But it would be very surprising if that one weird trick was the best calculation to do in every paper and every circumstance. If you claim it is the universal best way, then I suspect you of blind idealism, insensitivity to context and nuance, ignorance of all the other tools in the toolbox, the sheer folly of callow youth. You only have a hammer and no real-world experience using screwdrivers, so you claim everything is a nail.”

>

> Msr. Lawful: “On complex problems we may not be able to compute exact Bayesian updates, but the math still describes the optimal update, in the same way that a Carnot cycle describes a thermodynamically ideal engine even if you can’t build one. You are unlikely to find a superior viewpoint that makes some other update even more optimal than the Bayesian update, not without doing a great deal of fundamental math research and maybe not at all. We didn’t choose that formalism arbitrarily! We have a very broad variety of coherence theorems all spotlighting the same central structure of probability theory, saying variations of ‘If your behavior cannot be viewed as coherent with probability theory in sense X, you must be executing a dominated strategy and shooting off your foot in sense Y’.”

>

> I currently suspect that when Msr. Law talks like this, Msr. Toolbox hears “I prescribe to you the following recipe for your behavior, the Bayesian Update, which you ought to execute in every kind of circumstance.”

Post is by Eliezer Yudkowsky, here: https://www.lesswrong.com/posts/CPP2uLcaywEokFKQG/toolbox-thinking-and-law-thinking

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200561#respond)

12. ![67eedf422dc2da68f98e5fd15857018e](../_resources/ca935e28fd603f1aec44afe97f7d7c83.png)[Jesse Ray Nichols](http://infinitedays.org/)  says:

[December 4, 2019 at 7:00 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200598)

“What Bayes theorem cannot do is actually perform the function that scientists and philosophers who call themselves Bayesian say it can: to be a philosophy of inferring the best explanation. It cannot possibly create new explanations (which is, and should be the focus of science as much as gathering new evidence) and nor can it tell us what we should do. If we have a problem and we have no actual solution to it, Bayes’ theorem cannot possibly help. All it can do is assign probabilities to existing ideas (none of which are regarded as actual solutions). But why would one want to assign probabilities to possible solutions, none of which are known to work? There can be no reason other than if one wanted, to say, wager on which idea is likely to be falsified first, perhaps. But we must know – following Faraday and Popper, and Feynman and Deutsch: we must expect all of them will be falsified eventually. Your theories should be held on the tips of your fingers, so said Faraday, so that the merest breath of fact can blow them away. So no amount of assigning 99% probabilities to the truth of them makes them anymore “certain” or “likely to be true”. We need to have a pragmatic approach: take the best theory seriously as an explanation of reality and use it to solve problems and create solutions and technology – but don’t pretend that the content is “certain” to any degree. Just useful with some truth more than those other theories that have gone before and fallen to the sword of criticism and testing.

When we have actual solutions in science they go by a generic honorific title. We call them “The scientific theory of…”. So for example we have “The scientific theory of gravity” (it’s given name is General Relativity). We don’t need to assign a probability to it being true. We regard it as provisionally true knowing it is superior to all other rivals (insofar as there are any (and there are not!)) and we use it as if it’s true (this is pragmatic). But actually we expect that one day we will find it false. Just as we did with Newton. But this philosophy that our best theories are likely misconceptions in some way has no practical effect on what we do with them. We take them seriously as conditional truths about the world. As David Deutsch has said: it would have been preferable if long ago we’d all just decided to call scientific theories “scientific misconceptions” instead. It would save much in the way of so many of these debates. We’d all know that our best explanations, though better and closer to true than others that went before, are nonetheless able to be superseded by better ideas eventually.”

– http://www.bretthall.org/bayesian-epistemology.html

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200598#respond)

13. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Andrew (not Gelman)  says:

[December 4, 2019 at 10:02 pm](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200678)

> Go around offering 5:1 bets based on pure noise and you’ll go bankrupt real fast

If, after the first bet that you have lost, wouldn’t you update your estimate of the posterior probability and change the odds accordingly?

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200678#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 5, 2019 at 12:34 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200737)

Andrew (not Gelman):

Yes, I’d hope that people would do so! But standard Bayesian practice is to use weak priors unless absolutely forced to do otherwise. Again, practitioners avoid the worst excesses by simply not focusing on obviously stupid bets such as the 5/6 probability of theta>0 based on an estimate that’s one standard error from zero—but the concern remains that other bets, just as stupid but not so obviously stupid, are being made all the time.

It’s like . . . remember that study from a few years ago claiming that North Korea was (less) more democratic than North Carolina? What a joke that was. But what did the researchers do on that one? They just removed North Korea and maybe a couple other countries from their dataset. They didn’t use their failure with that country to face up to the underlying problems with their methods; instead, they brushed aside the obvious failure and moved on.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200737#respond)

14. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Carlos Ungil  says:

[December 5, 2019 at 1:39 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200760)

> remember that study from a few years ago claiming that North Korea was less democratic than North Carolina?

That’s indeed a ridiculous claim. It’s obvious that North Korea is more democratic, it’s even in the name of the country.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200760#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Daniel Lakeland](http://models.street-artists.org/)  says:

[December 5, 2019 at 2:19 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200773)

I guess it really is true that sometimes less is more ![1f600.png](../_resources/f3ad81fcd0670b45fc89475ffbb6e75b.png)

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200773#respond)

    - ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)[Andrew](http://statmodeling.stat.columbia.edu/)  says:

[December 5, 2019 at 9:42 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200996)

ulp! I went into my comment and fixed that, just so future generations of blog readers won’t be confused on my point.

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200996#respond)

15. ![087d4b749e60debf59b5e01898364a91](../_resources/7d6ff87ab26a35cc6737340da24b4067.jpg)Christian Hennig  says:

[December 5, 2019 at 8:23 am](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/#comment-1200951)

I agree with pretty much all of this posting. Of course Bayesians respond that the prior is bad and we need information to create a better prior. That’s fair enough. However I think they underestimate how difficult this often is in practice, particularly if you don’t want to go for the first impulsive idea you have like “I know it can’t be negative so an exponential(1) prior could be fine” but actually try to put together all information you have in a sensible way and on top of that try to convince yourself that you couldn’t get fundamentally different outcomes with other priors that are compatible with the same information.

Most “information” doesn’t come in the form of probabilities for some parameters to be true or even indirectly tell you how bets on future events should be affected by it. Some information has to do with what the analyst wants (e.g. how much of a problem it is in practice to have too many variables in a regression model – which is not only about overfitting and prediction errors), some other is very imprecise – chances are missing values are almost always NMAR but very often there is very little information about how they deviate from MAR etc.

I appreciate a thought through and well argued Bayesian model that comes with some sensitivity analysis, but we rarely see that, and surely it is a very sophisticated task to build one that cannot be done by many people who want to run statistical analyses – who then either will do NHST or bad Bayes…

[Reply to this comment](https://statmodeling.stat.columbia.edu/2019/12/03/whats-wrong-with-bayes/?replytocom=1200951#respond)

### Leave a Reply

Name
Mail (will not be published)
Website

« [Hey—the 2nd-best team in baseball is looking for a Bayesian!](https://statmodeling.stat.columbia.edu/2019/12/02/hey-the-2nd-best-team-in-baseball-is-looking-for-a-bayesian/)

[“Would Republicans pay a price if they vote to impeach the president? Here’s what we know from 1974.”](https://statmodeling.stat.columbia.edu/2019/12/03/would-republicans-pay-a-price-if-they-vote-to-impeach-the-president-heres-what-we-know-from-1974/) »