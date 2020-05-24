The Rule of 72 – BetterExplained

The Rule of 72 is a great [mental math shortcut](https://betterexplained.com/articles/mental-math-shortcuts/) to estimate the effect of any growth rate, from quick financial calculations to population estimates. Here’s the formula:

	Years to double = 72 / Interest Rate

This formula is useful for **financial estimates** and understanding the nature of compound interest. Examples:

- At 6% interest, your money takes 72/6 or 12 years to double.
- To double your money in 10 years, get an interest rate of 72/10 or 7.2%.
- If your country’s GDP grows at 3% a year, the economy doubles in 72/3 or 24 years.
- If your growth slips to 2%, it will double in 36 years. If growth increases to 4%, the economy doubles in 18 years. Given the speed at which technology develops, shaving years off your growth time could be very important.

You can also use the rule of 72 for **expenses like inflation or interest**:

- If inflation rates go from 2% to 3%, your money will lose half its value in 24 years instead of 36.
- If college tuition increases at 5% per year (which is faster than inflation), tuition costs will double in 72/5 or about 14.4 years. If you pay 15% interest on your credit cards, the amount you owe will **double** in only 72/15 or 4.8 years!

The rule of 72 shows why a “small” 1% difference in inflation or GDP expansion has a huge effect in forecasting models.

By the way, the Rule of 72 applies to anything that grows, including population. Can you see why a population growth rate of 3% vs 2% could be a huge problem for planning? Instead of needing to double your capacity in 36 years, you only have 24. Twelve years were shaved off your schedule with one percentage point.

## Deriving the Formula

Half the fun in using this magic formula is seeing how it’s made. Our goal is to figure out how long it takes for some money (or something else) to double at a certain interest rate.

Let’s start with $1 since it’s easy to work with (the exact value doesn’t matter). So, suppose we have $1 and a yearly interest rate R. After one year we have:

`1 * (1+R)`

For example, at 10% interest, we’d have $1 * (1 + 0.1) = $1.10 at the end of the year. After 2 years, we’d have

`1 * (1+R) * (1+R) = 1 * (1+R)^2`

And at 10% interest, we have $1 * (1.1)2 = $1.21 at the end of year 2. Notice how the dime we earned the first year starts earning money on its own (a penny). Next year we create another dime that starts making pennies for us, along with the small amount the first penny contributes. As Ben Franklin said: “The money that money earns, earns money”, or “The dime the dollar earned, earns a penny.” Cool, huh?

This deceptively small, cumulative growth makes compound interest extremely powerful – Einstein called it one of the most powerful forces in the universe.

Extending this year after year, after N years we have
`1 * (1+R)^N`

Now, we need to find how long it takes to double — that is, get to 2 dollars. The equation becomes:

`1 * (1+R)^N = 2`

Basically: How many years at R% interest does it take to get to 2? Not too hard, right? Let’s get to work on this sucka and find N:

	1: 1 * (1+R)^N = 2
	2: (1+R)^N = 2
	3: ln( (1+R)^N ) = ln(2) [natural log of both sides]
	4: N * ln(1+R) = .693
	5: N * R = .693 [For small R, ln(1+R) ~ R]
	6: N = .693 / R

There’s a little trickery on line 5. We use an approximation to say that ln(1+R) = R. It’s pretty close – even at R = .25 the approximation is 10% accurate ([check accuracy here](http://instacalc.com/22281)). As you use bigger rates, the accuracy will get worse.

Now let’s clean up the formula a bit. We want to use R as an integer (3) rather than a decimal (.03), so we multiply the right hand side by 100:

`N = 69.3 / R`

There’s one last step: 69.3 is nice and all, but not easily divisible. 72 is closeby, and has many more factors (2, 3, 4, 6, 12…). So the rule of 72 it is. Sorry 69.3, we hardly knew ye. (We could use 70, but again, 72 is nearby and even more divisible; for a mental shortcut, go with the number easiest to divide.)

## Extra Credit

Derive a similar rule for tripling your money – just start with
`1 * (1+R)^N = 3`

Give it a go – if you get stuck, [see the rule of 72 for any factor](http://instacalc.com/22282).

## Rule of 72 for any factor

3Rule of...110

[powered byinstacalc](https://instacalc.com/22282)[*open_in_new*](https://instacalc.com/22282)

Happy math.

## A Note On Accuracy

From Colin’s [comment](https://news.ycombinator.com/item?id=11959464) on Hacker News, the Rule of 72 works because it’s on the “right side” of `100*ln(2)`.

`100*ln(2)` is ~69.3, and 72 rounds up to the bigger side. This is a great choice because the [series expansion](https://www.wolframalpha.com/input/?i=taylor+series+ln(2)+%2F+ln(1+%2B+x)) of `r * ln(2) / ln(1 + r/100)` is:

![taylor_series_r___ln_2____ln_1___r_100__-_Wolfram_Alpha](../_resources/a3bca21da8af27af0d80bd508c0d6ad4.png)

This series expansion is the Calculus Way of showing how far the initial estimate strays from the actual result. The first correction term 12rlog(2)12rlog⁡(2) is small but grows with r. 72 is on the “right side” because it helps us stay in the accurate zone for longer. Neat insight!

### Join Over 450k Monthly Readers

![](../_resources/7b3283c8ed81b6abab772a1073853cbb.png)

Enjoy the article? There's plenty more to help you build a lasting, intuitive understanding of math. Join the newsletter and we'll turn Huh? to Aha!

## Other Posts In This Series

1. The Rule of 72

2. [Understanding Accounting Basics (ALOE and Balance Sheets)](https://betterexplained.com/articles/understand-accounting-basics-aloe-and-balance-sheets/)

3. [Understanding Debt, Risk and Leverage](https://betterexplained.com/articles/understanding-debt-risk-and-leverage/)

4. [What You Should Know About The Stock Market](https://betterexplained.com/articles/what-you-should-know-about-the-stock-market/)

5. [Understanding the Pareto Principle (The 80/20 Rule)](https://betterexplained.com/articles/understanding-the-pareto-principle-the-8020-rule/)

6. [Combining Simplicity and Complexity](https://betterexplained.com/articles/combining-simplicity-and-complexity/)

### Leave a Reply

78 Comments on "The Rule of 72"

Sort by:  newest |oldest| most voted

Pierre-Francois

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Thanks for the great explanation. It’s a neat tip for those of us who can’t calculate ln[2^(1/r)] mentally…

**Vote Up3**Vote Down ** Reply
**9 years 9 months ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

@Kar: Glad you liked it.

@Devin: Thanks, happy you’re enjoying the site! Yep, you got it: it’s the rule of 110 for tripling your money (if you need to remember it, think about “always giving 110 percent”).

Also, for quadrupling your money, you can use the rule of 72 twice to get the “Rule of 144”. Though at that point the rounding errors start to add up — the rule of 140 would be better :).

**Vote Up2**Vote Down ** Reply
**9 years 6 months ago

Taatna

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

why do we say that if an object travels the speed of light it will go into the future/past? Does this then mean that theoretical an object can never be created to travel faster than light?

**Vote Up1**Vote Down ** Reply
**9 years 9 months ago

Kar

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Your post rockks!!!!
**Vote Up1**Vote Down ** Reply
**9 years 8 months ago

[Financial Education: The Truth About the Rule of 72](http://cityscoop.us/bayarea-financialeducation/2009/04/14/financial-education-the-truth-about-the-rule-of-72/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] Financial planners get very excited about the Rule of 72. Personally, I don’t see the point. I don’t care how long it will take my money to double specifically. What I want to know is what it will take for me to reach my financial goals. What rate do I need to be making on my money? How much do I need invested? How much time do I need? […]

**Vote Up1**Vote Down ** Reply
**8 years 5 months ago

[Understanding the Birthday Paradox | BetterExplained](http://betterexplained.com/articles/understanding-the-birthday-paradox/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] But even after training, we get caught again. At 5% interest we’ll double our money in 14 years, rather than the “expected” 20. Did you naturally infer the Rule of 72 when learning about interest rates? Probably not. Understanding compound exponential growth with our linear brains is hard. […]

**Vote Up0**Vote Down ** Reply
**10 years 5 months ago

[Mental Math Shortcuts | BetterExplained](http://betterexplained.com/articles/mental-math-shortcuts/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] Rule of 72: Years To Double = 72/Interest Rate (derivation) […]
**Vote Up0**Vote Down ** Reply
**9 years 11 months ago

[test 12/14/2007 « Strange Kite](https://wind333.wordpress.com/2007/12/14/test-12142007/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] The Rule of 72 | BetterExplained  Annotated By the way, the Rule of 72 applies to anything that grows, including population. Can you see why a population growth rate of 3% vs 2% could be a huge problem for planning? Instead of needing to double your capacity in 36 years, you only have 24. Twelve years were shaved off your schedule with one percentage point. […]

**Vote Up0**Vote Down ** Reply
**9 years 9 months ago

[iCode Inc](http://icodeinc.com/blog/?p=303)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] Rule of 72: Years To Double = 72/Interest Rate (derivation) […]
**Vote Up0**Vote Down ** Reply
**9 years 9 months ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Thanks, glad you liked it :).
**Vote Up0**Vote Down ** Reply
**9 years 9 months ago

[A Visual Guide to Simple, Compound and Continuous Interest Rates | BetterExplained](http://betterexplained.com/articles/a-visual-guide-to-simple-compound-and-continuous-interest-rates/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] Treating interest in this funky way (trajectories and factories) will help us understand some of e’s cooler properties, which come in handy for calculus. Also, try the Rule of 72 for a quick way to compute the effect of interest rates mentally (that investment with 6% APY will double in 12 years). Happy math. […]

**Vote Up0**Vote Down ** Reply
**9 years 8 months ago

Devin

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Hey, I really love this site. I especially love the decryption of e on another page. But anyway, I did the extra credit, I think it would be 110/R.

N = ln(3)/ln(1+R) and as you said, for small R’s, the ln(1+R) approximates R. After multiplying by 100, it turns out to be about 109.86/R, which I rounded up for simplicity to 110/R. That was fun! hahaha.

**Vote Up0**Vote Down ** Reply
**9 years 7 months ago

[Enginerd](https://logicwrong.blogspot.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

I’m willing to bet that it was changed from 69 to 72 so people wouldn’t feel dirty talking about the “Rule of 69”.

On the other hand, the ln(1+R)~R approximation tends to underestimate the doubling time. Changing from 69 to 72 corrects for that. Doing a few test cases, 72 seems a bit more accurate than 69.

**Vote Up0**Vote Down ** Reply
**9 years 5 months ago

[Kalid](http://betterexplained.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Ah, good points. Also, 69 only has the factors 3 x 23 so it doesn’t divide that easily (for mental math).

**Vote Up0**Vote Down ** Reply
**9 years 5 months ago

Anonymous

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

i really love this site . it gives me all the information that i needed.
**Vote Up0**Vote Down ** Reply
**9 years 2 months ago

[Kalid](http://betterexplained.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

Thanks, glad you enjoyed it.
**Vote Up0**Vote Down ** Reply
**9 years 2 months ago

[Rule of 72 กฎของเลข 72 « My Weblog](https://teriyakichicken.wordpress.com/2008/09/10/rule-of-72-e0b881e0b88ee0b882e0b8ade0b887e0b980e0b8a5e0b882-72/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] ถ้าใครอยากทราบว่าสูตรนี้มีมาได้อย่างไร ลองเข้าไปดูที่ เว็บไซต์ นี้นะครับ เขาลองพิสูจน์สูตรให้ดู เผื่อคนที่ชอบตัวเลขลองเข้าไปดูกันครับ :) […]

**Vote Up0**Vote Down ** Reply
**9 years 1 month ago

[Top501 World: Rule Of 72](http://articles.top501.nu/2008/09/24/top501-world-rule/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

[…] http://betterexplained.com/articles/the-rule-of-72/ […]
**Vote Up0**Vote Down ** Reply
**9 years 19 days ago

No One

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

This did really help me understand the meaning better than all the other web sites that I went to for the Definition.

**Vote Up0**Vote Down ** Reply
**8 years 10 months ago

[kalid](https://betterexplained.com/articles/author/admin/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

@No One: Thanks.
**Vote Up0**Vote Down ** Reply
**8 years 9 months ago

linda

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

I loved it i found out alot
**Vote Up0**Vote Down ** Reply
**8 years 7 months ago

[Kalid](http://betterexplained.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

@linda: Glad it was helpful!
**Vote Up0**Vote Down ** Reply
**8 years 7 months ago

vikram sethia

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

i liked to read the description
**Vote Up0**Vote Down ** Reply
**8 years 5 months ago

[Bullish Trader](http://thegetwealthy.com/)

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

It’s considered as the 8th wonder of the world! Great invention of mankind!
Rule of 72 rules
[http://thegetwealthy.com](http://thegetwealthy.com/)
**Vote Up0**Vote Down ** Reply
**8 years 2 months ago

nitin

**Click to flag and open «Comment Reporting» form. You can choose reporting category and send message to website administrator. Admins may or may not choose to remove the comment or block the author. And please don't worry, your report will be anonymous.

thnx
**Vote Up0**Vote Down ** Reply
**8 years 1 month ago

[(L)](https://betterexplained.com/articles/the-rule-of-72/#!parentId=578)