Quantitative Brain Teaser: Brain Only

# Quantitative Brain Teaser: Brain Only

Sep 22, 2014

I've recently been working some atrophied mental muscles and came across a brain teaser that was pretty nifty:

**

> Find a **> 10-digit number**> , where each digit represents the number of that ordinal number in the whole number. So, the**> first digit represents the number of 0's**>  in the whole 10 digits. The second digit represents the number of 1's in the whole 10 digits. And so on. The first digit is not a 0.

**

#### Example

If we shortened from 10 digits to 4 digit, the number
**> 2> ,> 0> 2> 0> 2,020> 2> ,> 0> 2> 0**

works since we haved0=2d_0 = 2*d*0​=2and two 0's (in the second and fourth slots),d1=0d_1 = 0*d*1​=0since the number has no 1's,d2=2d_2 = 2*d*2​=2since the number has two 2's (in the first and third slots) andd3=0d_3 = 0*d*3​=0since the number has no 3's.

#### Shorthand Notation

In order to refer to each digit, for search we name them all:

**> n> => d> 0> ,> d> 1> d> 2> d> 3> ,> d> 4> d> 5> d> 6> ,> d> 7> d> 8> d> 9> n = d_0, d_1 d_2 d_3, d_4 d_5 d_6, d_7 d_8 d_9*> n*> =*> d*> 0> ​> ,*> d*> 1> ​*> d*> 2> ​*> d*> 3> ​> ,*> d*> 4> ​*> d*> 5> ​*> d*> 6> ​> ,*> d*> 7> ​*> d*> 8> ​*> d*> 9> ​**

We can see this in the above example when we refer to the digits in the four digit number

**> n> => d> 0> ,> d> 1> d> 2> d> 3> n = d_0, d_1 d_2 d_3*> n*> =*> d*> 0> ​> ,*> d*> 1> ​*> d*> 2> ​*> d*> 3> ​**

#### A Practical Approach, Breaking Into Subproblems

Our search space is massive, and with only our wits, we need to quickly find a way to focus on a small space of possibilities. Since the first digit allows us to place a number of 0's we try to set it equal to values starting from the largest. By doing this we only have a little wiggle room to find the places which don't hold a zero.

#### First Case: d0=9d_0 = 9*d*0​=9

In this case our only choice is

**> 9> ,> 0> 0> 0> ,> 0> 0> 0> ,> 0> 0> 0> 9,000,000,000> 9> ,> 0> 0> 0> ,> 0> 0> 0> ,> 0> 0> 0**

since we must have nine 0's. However since we have one 9,d9=0d_9 = 0*d*9​=0should not occur.

Thus we see **none of our choices are possible** whend0=9d_0 = 9*d*0​=9.

#### Second Case: d0=8d_0 = 8*d*0​=8

Here we must have eight 0's andd8>0d_8 > 0*d*8​>0so our possible solutions must look like

**> 8> ,> 0> 0> 0> ,> 0> 0> 0> ,> 0> ∗> 0> 8,000,000,0*0> 8> ,> 0> 0> 0> ,> 0> 0> 0> ,> 0> ∗> 0**

But this leaves us withd8=1d_8 = 1*d*8​=1as our only choice since we can't place any more 8's. But now the presence of a 1 in

**> 8> ,> 0> 0> 0> ,> 0> 0> 0> ,> 0> 1> 0> 8,000,000,010> 8> ,> 0> 0> 0> ,> 0> 0> 0> ,> 0> 1> 0**

can't coexist withd1=0d_1 = 0*d*1​=0so we again see **none of our choices are possible** whend0=8d_0 = 8*d*0​=8.

#### Third Case: d0=7d_0 = 7*d*0​=7

Here we have seven 0's and know thatd7=1d_7 = 1*d*7​=1It must be at least 1 since the first digit is a 7. It can't be 2 because the presence of another 7 would mean another digit (other than 0) would occur 7 times, which is impossible since there are only 10 total digits.

Since we knowd7=1d_7 = 1*d*7​=1our possible solutions must look like

**> 7> ,> ∗> 0> 0> ,> 0> 0> 0> ,> 1> 0> 0> 7,*00,000,100> 7> ,> ∗> 0> 0> ,> 0> 0> 0> ,> 1> 0> 0**

But again here we reach an impossible point. If we setd1=1d_1 = 1*d*1​=1then that digit would contradict itself since it is the second occurrence of 1. Ifd1=2d_1 = 2*d*1​=2it would contradictd2=0d_2 = 0*d*2​=0and so on for higher values. In addition, we have used all our digits, so can't increase the value ofd1d_1*d*1​by placing more 1's in our number.

Thus we see **none of our choices are possible** whend0=7d_0 = 7*d*0​=7.

#### Fourth Case: d0=6d_0 = 6*d*0​=6

Here we have six 0's and must haved6=1d_6 = 1*d*6​=1since (as above), two different digits can't occur six times among 10 digits.

Also as before we can't haved1=1d_1 = 1*d*1​=1but now have some extra freedom (an extra digit which doesn't have to be 0) so consider the cased1=2d_1 = 2*d*1​=2. This corresponds to an occurrence of the digit 2, hence we setd2=1d_2 = 1*d*2​=1.

Now we have 4 non-zero digits along with six 0's to place:

**> 6> ,> 2> 1> 0> ,> 0> 0> 1> ,> 0> 0> 0> 6,210,001,000> 6> ,> 2> 1> 0> ,> 0> 0> 1> ,> 0> 0> 0**

Thus **we have found a number** which satisfies the criteria! The zero digits in the 3, 4, 5, 7, 8, and 9 places correspond to the absence of those digits. The non-zero digits in the 0, 1, 2, and 6 places also are the correct counts of each of those digits.

As a math nerd, I was still curious to know how to find every possible number that satisfies the criteria, but that task is too tedious to handle with the brain alone (or at least to be worth reading about when solved by hand). In my follow up to this, I'll show how a combination of smarts and programming can perform an exhaustive search in under 10 seconds.

Posted by Danny Hermes (dhermes@bossylobster.com)•Sep 22, 2014  •[Brain Teaser](https://blog.bossylobster.com/tag/brain-teaser.html)[Combinatorics](https://blog.bossylobster.com/tag/combinatorics.html)[Digit Counting](https://blog.bossylobster.com/tag/digit-counting.html)[Interview Questions](https://blog.bossylobster.com/tag/interview-questions.html)[Mathematics](https://blog.bossylobster.com/tag/mathematics.html)

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fblog.bossylobster.com%2F2014%2F09%2Fquantitative-brain-teaser-brain-only.html&ref_src=twsrc%5Etfw&text=Quantitative%20Brain%20Teaser%3A%20Brain%20Only&tw_p=tweetbutton&url=https%3A%2F%2Fblog.bossylobster.com%2F2014%2F09%2Fquantitative-brain-teaser-brain-only.html&via=bossylobster)

[(L)](https://plus.google.com/share?app=110&url=https%3A%2F%2Fblog.bossylobster.com%2F2014%2F09%2Fquantitative-brain-teaser-brain-only.html)