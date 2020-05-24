The Feynman Lectures on Physics Vol. I Ch. 22: Algebra

## 22Algebra

[[Special message](http://www.feynman.com/the-animated-feynman-lectures/) from Ralph Leighton, with audio from the lecture.]

![](../_resources/d8b8a4e56f99f69ee329a549e939e99e.png)

### 22–1Addition and multiplication

In our study of oscillating systems we shall have occasion to use one of the most remarkable, almost astounding, formulas in all of mathematics. From the physicist’s point of view we could bring forth this formula in two minutes or so, and be done with it. But science is as much for intellectual enjoyment as for practical utility, so instead of just spending a few minutes on this amazing jewel, we shall surround the jewel by its proper setting in the grand design of that branch of mathematics which is called elementary algebra.

Now you may ask, “What is mathematics doing in a physics lecture?” We have several possible excuses: first, of course, mathematics is an important tool, but that would only excuse us for giving the formula in two minutes. On the other hand, in theoretical physics we discover that all our laws can be written in mathematical form; and that this has a certain simplicity and beauty about it. So, ultimately, in order to understand nature it may be necessary to have a deeper understanding of mathematical relationships. But the real reason is that the subject is enjoyable, and although we humans cut nature up in different ways, and we have different courses in different departments, such compartmentalization is really artificial, and we should take our intellectual pleasures where we find them.

Another reason for looking more carefully at algebra now, even though most of us studied algebra in high school, is that that was the first time we studied it; all the equations were unfamiliar, and it was hard work, just as physics is now. Every so often it is a great pleasure to look back to see what territory has been covered, and what the great map or plan of the whole thing is. Perhaps some day somebody in the Mathematics Department will present a lecture on mechanics in such a way as to show what it was we were trying to learn in the physics course!

The subject of algebra will not be developed from the point of view of a mathematician, exactly, because the mathematicians are mainly interested in how various mathematical facts are demonstrated, and how many assumptions are absolutely required, and what is not required. They are not so interested in the result of what they prove. For example, we may find the Pythagorean theorem quite interesting, that the sum of the squares of the sides of a right triangle is equal to the square of the hypotenuse; that is an interesting fact, a curiously simple thing, which may be appreciated without discussing the question of how to prove it, or what axioms are required. So, in the same spirit, we shall describe qualitatively, if we may put it that way, the system of elementary algebra. We say*elementary* algebra because there is a branch of mathematics called *modern* algebra in which some of the rules such as ab=ba, are abandoned, and it is still called algebra, but we shall not discuss that.

To discuss this subject we start in the middle. We suppose that we already know what integers are, what zero is, and what it means to increase a number by one unit. You may say, “That is not in the middle!” But it is the middle from a mathematical standpoint, because we could go even further back and describe the theory of sets in order to *derive* some of these properties of integers. But we are not going in that direction, the direction of mathematical philosophy and mathematical logic, but rather in the other direction, from the assumption that we know what integers are and we know how to count.

If we start with a certain number a, an integer, and we count successively one unit b times, the number we arrive at we calla+b, and that defines *addition* of integers.

Once we have defined addition, then we can consider this: if we start with nothing and add a to it, b times in succession, we call the result *multiplication* of integers; we call it b  *times* a.

Now we can also have a *succession of multiplications:* if we start with 1 and multiply by a, b times in succession, we call that *raising to a power:* ab.

Now as a consequence of these definitions it can be easily shown that all of the following relationships are true:

(a)(c)(e)(g)(i)(k)a+b=b+aab=ba(ab)c=a(bc)abac=a(b+c)a+0=aa1=a(b)(d)(f)(h)(j)a+(b+c)=(a+b)+ca(b+c)=ab+ac(ab)c=acbc(ab)c=a(bc)a⋅1=a(22.1)

These results are well known and we shall not belabor the point, we merely list them. Of course, 1 and 0 have special properties; for example, a+0 is a, a times 1=a, and a to the first power is a.

In this discussion we must also assume a few other properties like continuity and ordering, which are very hard to define; we will let the rigorous theory do it. Furthermore, it is definitely true that we have written down too many “rules”; some of them may be deducible from the others, but we shall not worry about such matters.

### 22–2The inverse operations

In addition to the direct operations of addition, multiplication, and raising to a power, we have also the *inverse* operations, which are defined as follows. Let us assume that a and c are given, and that we wish to find what values of b satisfy such equations as a+b=c, ab=c, ba=c. If a+b=c, b is defined as c−a, which is called *subtraction*. The operation called division is also clear: if ab=c, then b=c/a defines division—a solution of the equation ab=c “backwards.” Now if we have a power ba=c and we ask ourselves, “What is b?,” it is called theath *root* of c: b=c√a. For instance, if we ask ourselves the following question, “What integer, raised to the third power, equals 8?,” then the answer is called the *cube root*of 8; it is 2. Because ba and ab are not equal, there are*two* inverse problems associated with powers, and the other inverse problem would be, “To what power must we raise 2 to get 8?” This is called taking the *logarithm*. Ifab=c, we write b=logac. The fact that it has a cumbersome notation relative to the others does not mean that it is any less elementary, at least applied to integers, than the other processes. Although logarithms come late in an algebra class, in practice they are, of course, just as simple as roots; they are just a different kind of solution of an algebraic equation. The direct and inverse operations are summarized as follows:

(a)(b)(c)(d)additiona+b=cmultiplicationab=cpowerba=cpowerab=c(a′)(b′)(c′)(d′)subtractionb=c−adivisionb=c/arootb=c√alogarithmb=logac(22.2)

Now here is the idea. These relationships, or rules, are correct for integers, since they follow from the definitions of addition, multiplication, and raising to a power. *We are going to discuss whether or not we can broaden the class of objects which a, b, and c represent so that they will obey these same rules*, although the processes for a+b, and so on, will not be definable in terms of the direct action of adding 1, for instance, or successive multiplications by integers.

### 22–3Abstraction and generalization

When we try to solve simple algebraic equations using all these definitions, we soon discover some insoluble problems, such as the following. Suppose that we try to solve the equation b=3−5. That means, according to our definition of subtraction, that we must find a number which, when added to 5, gives 3. And of course there*is* no such number, because we consider only positive integers; this is an insoluble problem. However, the plan, the great idea, is this: *abstraction and generalization*. From the whole structure of algebra, rules plus integers, we abstract the original definitions of addition and multiplication, but we leave the rules ([22.1](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI221)) and ([22.2](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI222)), and assume these to be true *in general* on a wider class of numbers, even though they are originally derived on a smaller class. Thus, rather than using integers symbolically to define the rules, we use the rules as the definition of the symbols, which then represent a more general kind of number. As an example, by working with the rules alone we can show that 3−5=0−2. In fact we can show that one can make *all* subtractions, provided we define a whole set of new numbers: 0−1, 0−2, 0−3, 0−4, and so on, called the *negative integers*. Then we may use all the other rules, like a(b+c)=ab+ac and so forth, to find what the rules are for multiplying negative numbers, and we will discover, in fact, that all of the rules can be maintained with negative as well as positive integers.

So we have increased the range of objects over which the rules work, but the meaning of the symbols is different.

One cannot say, for instance, that −2 times 5 really means to add 5 together successively −2 times. That means nothing. But nevertheless everything will work out all right according to the rules.

An interesting problem comes up in taking powers. Suppose that we wish to discover what a(3−5) means. We know only that 3−5 is a solution of the problem, (3−5)+5=3. Knowing that, we know thata(3−5)a5=a3. Therefore a(3−5)=a3/a5, by the definition of division. With a little more work, this can be reduced to 1/a2. So we find that the negative powers are the reciprocals of the positive powers, but 1/a2 is a meaningless symbol, because ifa is a positive or negative integer, the square of it can be greater than 1, and we do not yet know what we mean by 1 divided by a number greater than 1!

Onward! The great plan is to continue the process of generalization; whenever we find another problem that we cannot solve we extend our realm of numbers. Consider division: we cannot find a number which is an integer, even a negative integer, which is equal to the result of dividing 3 by 5. But if we suppose that all fractional numbers also satisfy the rules, then we can talk about multiplying and adding fractions, and everything works as well as it did before.

Take another example of powers: what is a3/5? We know only that(3/5)5=3, since that was the definition of 3/5. So we know also that (a(3/5))5=  a(3/5)(5)=  a3, because this is one of the rules. Then by the definition of roots we find that a(3/5)=a3−−√5.

In this way, then, we can define what we mean by putting fractions in the various symbols, by using the rules themselves to help us determine the definition—it is not arbitrary. It is a remarkable fact that all the rules still work for positive and negative integers, as well as for fractions!

We go on in the process of generalization. Are there any other equations we cannot solve? Yes, there are. For example, it is impossible to solve this equation: b=  21/2=  2–√. It is impossible to find a number which is rational (a fraction) whose square is equal to 2. It is very easy for us in modern days to answer this question. We know the decimal system, and so we have no difficulty in appreciating the meaning of an unending decimal as a type of approximation to the square root of 2. Historically, this idea presented great difficulty to the Greeks. To really define*precisely* what is meant here requires that we add some substance of continuity and ordering, and it is, in fact, quite the most difficult step in the processes of generalization just at this point. It was made, formally and rigorously, by Dedekind. However, without worrying about the mathematical rigor of the thing, it is quite easy to understand that what we mean is that we are going to find a whole sequence of approximate fractions, perfect fractions (because any decimal, when stopped somewhere, is of course rational), which just keeps on going, getting closer and closer to the desired result. That is good enough for what we wish to discuss, and it permits us to involve ourselves in irrational numbers, and to calculate things like the square root of 2 to any accuracy that we desire, with enough work.

### 22–4Approximating irrational numbers

The next problem comes with what happens with the irrational powers. Suppose that we want to define, for instance,102√. In principle, the answer is simple enough. If we approximate the square root of 2 to a certain number of decimal places, then the power is rational, and we can take the approximate root, using the above method, and get an *approximation*to 102√. Then we may run it up a few more decimal places (it is again rational), take the appropriate root, this time a much higher root because there is a much bigger denominator in the fraction, and get a better approximation. Of course we are going to get some enormously high roots involved here, and the work is quite difficult. How can we cope with this problem?

In the computations of square roots, cube roots, and other small roots, there is an arithmetical process available by which we can get one decimal place after another. But the amount of labor needed to calculate irrational powers and the logarithms that go with them (the inverse problem) is so great that there is no simple arithmetical process we can use. Therefore tables have been built up which permit us to calculate these powers, and these are called the tables of logarithms, or the tables of powers, depending on which way the table is set up. It is merely a question of saving time; if we must raise some number to an irrational power, we can look it up rather than having to compute it. Of course, such a computation is just a technical problem, but it is an interesting one, and of great historical value. In the first place, not only do we have the problem of solving x=102√, but we also have the problem of solving10x=2, or x=log102. This is not a problem where we have to define a new kind of number for the result, it is merely a computational problem. The answer is simply an irrational number, an unending decimal, not a new kind of a number.

Let us now discuss the problem of calculating solutions of such equations. The general idea is really very simple. If we could calculate 101, and 104/10, and 101/100, and 104/1000and so on, and multiply them all together, we would get101.414… or 102√, and that is the general idea on which things work. But instead of calculating 101/10 and so on, we shall calculate 101/2, 101/4, and so on. Before we start, we should explain why we make so much work with 10, instead of some other number. Of course, we realize that logarithm tables are of great practical utility, quite aside from the mathematical problem of taking roots, since with any base at all,

logb(ac)=logba+logbc.(22.3)

We are all familiar with the fact that one can use this fact in a practical way to multiply numbers if we have a table of logarithms. The only question is, with what base b shall we compute? It makes no difference what base is used; we can use the same principle all the time, and if we are using logarithms to any particular base, we can find logarithms to any other base merely by a change in scale, a multiplying factor. If we multiply Eq. ([22.3](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI223)) by 61, it is just as true, and if we had a table of logs with a base b, and somebody else multiplied all of our table by 61, there would be no essential difference. Suppose that we know the logarithms of all the numbers to the base b. In other words, we can solve the equation ba=c for any c because we have a table. The problem is to find the logarithm of the same number c to some other base, let us say the base x. We would like to solve xa′=c. It is easy to do, because we can always write x=bt, which defines t, knowing x and b. As a matter of fact, t=logbx. Then if we put that in and solve for a′, we see that (bt)a′=ba′t=c. In other words, ta′ is the logarithm of c in base b. Thus a′=a/t. Thus logs to base x are just 1/t, which is a constant, times the logs to the base, b. Therefore any log table is equivalent to any other log table if we multiply by a constant, and the constant is 1/logbx. This permits us to choose a particular base, and for convenience we take the base 10. (The question may arise as to whether there is any natural base, any base in which things are somehow simpler, and we shall try to find an answer to that later. At the moment we shall just use the base 10.)

Table 22–1Successive Square Roots of Ten

|     |     |     |     |
| --- | --- | --- | --- |
| Power s | 1024s | 10s | (10s−1)/s |
| 1/1024 | 1024 | 10.0000000 | 9.0000000 |
| 1/2000 | 1512 | 13.1622800 | 4.3200000 |
| 1/4000 | 1256 | 11.7782800 | 3.1130000 |
| 1/8000 | 1128 | 11.3335200 | 2.6680000 |
| 1/1600 | 1064 | 11.1547800 | 2.4760000 |
| 1/3200 | 1032 | 11.0746070 | 2.3874000 |
| 1/6400 | 1016 | 11.0366330 | 2.3445000 |
| 1/1280 | 1008 | 11.0181520 | 2.3234211 |
| 1/2560 | 1004 | 11.0090350 | 2.3130104 |
| 1/5120 | 1002 | 11.0045073 | 2.3077153 |
| 1/1024 | 1001 | 11.0022511 | 2.3051126 |
|     |     |     | 00⏐↓⏐26 |
| Δ/1024 | 102Δ | 1+0.0022486Δ←−− | ¯¯¯¯¯2.3025 |
| (Δ→0) |     |     |     |

Now let us see how to calculate logarithms. We begin by computing successive square roots of 10, by cut and try. The results are shown in Table [22–1](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T1). The powers of 10 are given in the first column, and the result, 10s, is given in the third column. Thus101=10. The one-half power of 10 we can easily work out, because that is the square root of 10, and there is a known, simple process for taking square roots of any number.[1](http://www.feynmanlectures.caltech.edu/I_22.html#footnote_1) Using this process, we find the first square root to be 3.16228. What good is that? It already tells us something, it tells us how to take 100.5, so we now know at least *one* logarithm, if we happen to need the logarithm of 3.16228, we know the answer is close to 0.50000. But we must do a little bit better than that; we clearly need more information. So we take the square root again, and find 101/4, which is 1.77828. Now we have the logarithm of more numbers than we had before, 1.250 is the logarithm of 17.78 and, incidentally, if it happens that somebody asks for 100.75, we can get it, because that is 10(0.5+0.25); it is therefore the product of the second and third numbers. If we can get enough numbers in column s to be able to make up almost any number, then by multiplying the proper things in column 3, we can get 10 to any power; that is the plan. So we evaluate ten successive square roots of 10, and that is the main work which is involved in the calculations.

Why don’t we keep on going for more and more accuracy? Because we begin to notice something. When we raise 10 to a very small power, we get 1 plus a small amount. The reason for this is clear, because we are going to have to take the 1000th power of 101/1000 to get back to 10, so we had better not start with too big a number; it has to be close to 1. What we notice is that the small numbers that are added to 1 begin to look as though we are merely dividing by 2each time; we see 1815 becomes 903, then 450, 225; so it is clear that, to an excellent approximation, if we take another root, we shall get 1.00112 something, and rather than actually *take*all the square roots, we *guess* at the ultimate limit. When we take a small fraction Δ/1024 as Δ approaches zero, what will the answer be? Of course it will be some number close to 1+0.0022511Δ. Not exactly 1+0.0022511Δ, however—we can get a better value by the following trick: we subtract the 1, and then divide by the power s. This ought to correct all the excesses to the same value. We see that they are very closely equal. At the top of the table they are not equal, but as they come down, they get closer and closer to a constant value. What is the value? Again we look to see how the series is going, how it has changed with s. It changed by 211, by 104, by 53, by26. These changes are obviously half of each other, very closely, as we go down. Therefore, if we kept going, the changes would be13, 7, 3, 2 and 1, more or less, or a total of 26. Thus we have only 26 more to go, and so we find that the true number is 2.3025. (Actually, we shall later see that the *exact* number should be 2.3026, but to keep it realistic, we shall not alter anything in the arithmetic.) From this table we can now calculate any power of 10, by compounding the power out of 1024ths.

Let us now actually calculate a logarithm, because the process we shall use is where logarithm tables actually come from. The procedure is shown in Table [22–2](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T2), and the numerical values are shown in Table [22–1](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T1) (columns 2 and 3).

Table 22–2Calculation of a logarithm: log102

|     |     |
| --- | --- |
|     | 2÷1.77828=1.124682 |
|     | 1.124682÷1.074607=1.046598, etc. |
| ∴   | 2=(1.77828)(1.074607)(1.036633)(1.0090350)(1.000573) |
|     | 2=10[11024(256+32+16+4+0.254)]=10[308.2541024] |
|     | 2=100.30103(256+32+16+4(5732249=0.254) |
| ∴   | log102=0.30103 |

Suppose we want the logarithm of 2. That is, we want to know to what power we must raise 10 to get 2. Can we raise 10 to the1/2 power? No; that is too big. In other words, we can see that the answer is going to be bigger than 1/4, and less than 1/2. Let us take the factor 101/4 out; we divide 2 by 1.778…, and get1.124…, and so on, and now we know that we have taken away0.250000 from the logarithm. The number 1.124…, is now the number whose logarithm we need. When we are finished we shall add back the 1/4, or 256/1024. Now we look in the table for the next number just below 1.124…, and that is 1.074607. We therefore divide by 1.074607 and get 1.046598. From that we discover that 2 can be made up of a product of numbers that are in Table [22–1](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T1), as follows:

2=(1.77828)(1.074607)(1.036633)(1.0090350)(1.000573).

There was one factor (1.000573) left over, naturally, which is beyond the range of our table. To get the logarithm of this factor, we use our result that 10Δ/1024≈1+2.3025Δ/1024. We find Δ=0.254. Therefore our answer is 10 to the following power: (256+32+16+4+0.254)/1024. Adding those together, we get 308.254/1024. Dividing, we get 0.30103, so we know that the log102=0.30103, which happens to be right to 5 figures!

This is how logarithms were originally computed by Mr. Briggs of Halifax, in 1620. He said, “I computed successively54 square roots of 10.” We know he really computed only the first 27, because the rest of them can be obtained by this trick with Δ. His work involved calculating the square root of 10 twenty-seven times, which is not much more than the ten times we did; however, it was more work because he calculated to sixteen decimal places, and then reduced his answer to fourteen when he published it, so that there were no rounding errors. He made tables of logarithms to fourteen decimal places by this method, which is quite tedious. But all logarithm tables for three hundred years were borrowed from Mr. Briggs’ tables by reducing the number of decimal places. Only in modern times, with the WPA and computing machines, have new tables been independently computed. There are much more efficient methods of computing logarithms today, using certain series expansions.

In the above process, we discovered something rather interesting, and that is that for very small powers ϵ we can calculate10ϵ easily; we have discovered that 10ϵ=1+2.3025ϵ, by sheer numerical analysis. Of course this also means that 10n/2.3025=1+n if n is very small. Now logarithms to any other base are merely multiples of logarithms to the base 10. The base 10 was used only because we have 10 fingers, and the arithmetic of it is easy, but if we ask for a mathematically natural base, one that has nothing to do with the number of fingers on human beings, we might try to change our scale of logarithms in some convenient and natural manner, and the method which people have chosen is to redefine the logarithms by multiplying all the logarithms to the base 10 by 2.3025… This then corresponds to using some other base, and this is called the *natural* base, or base e. Note that loge(1+n)≈n, or en≈1+n as n→0.

It is easy enough to find out what e is: e=101/2.3025…or 100.434310…, an irrational power. Our table of the successive square roots of 10 can be used to compute, not just logarithms, but also 10 to any power, so let us use it to calculate this natural base e. For convenience we transform 0.434310… into444.73/1024. Now, 444.73 is 256+128+32+16+8+4+0.73. Therefore e, since it is an exponent of a sum, will be a product of the numbers

(1.77828)(1.33352)(1.074607)(1.036633)(1.018152)(1.009035)(1.001643)=2.7184.

(The only problem is the last one, which is 0.73, and which is not in the table, but we know that if Δ is small enough, the answer is 1+0.0022486Δ.) When we multiply all these together, we get2.7184 (it should be 2.7183, but it is good enough). The use of such tables, then, is the way in which irrational powers and the logarithms of irrational numbers are all calculated. That takes care of the irrationals.

### 22–5Complex numbers

Now it turns out that after all that work we *still* cannot solve every equation! For instance, what is the square root of −1? Suppose we have to find x2=−1. The square of no rational, of no irrational, of *nothing* that we have discovered so far, is equal to −1. So we again have to generalize our numbers to a still wider class. Let us suppose that a specific solution of x2=−1 is called something, we shall call it i; i has the property, by definition, that its square is −1. That is about all we are going to say about it; of course, there is more than one root of the equation x2=−1. Someone could write i, but another could say, “No, I prefer−i. My i is minus your i.” It *is* just as good a solution, and since the only definition that i has is that i2=−1, it must be true that any equation we can write is equally true if the sign of iis changed everywhere. This is called taking the *complex conjugate*. Now we are going to make up numbers by adding successive i’s, and multiplying i’s by numbers, and adding other numbers, and so on, according to all of our rules. In this way we find that numbers can all be written in the form p+iq, where p and q are what we call *real* numbers, i.e., the numbers we have been defining up until now. The number i is called the *unit imaginary* number. Any real multiple of i is called *pure imaginary*. The most general number, a, is of the form p+iq and is called a*complex number*. Things do not get any worse if, for instance, we multiply two such numbers, let us say (r+is)(p+iq). Then, using the rules, we get

(r+is)(p+iq)=rp+r(iq)+(is)p+(is)(iq)=rp+i(rq)+i(sp)+(ii)(sq)=(rp−sq)+i(rq+sp),(22.4)

since ii=  i2=  −1. Therefore all the numbers that now belong in the rules ([22.1](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI221)) have this mathematical form.

Now you say, “This can go on forever! We have defined powers of imaginaries and all the rest, and when we are all finished, somebody else will come along with another equation which cannot be solved, like x6+3x2=−2. Then we have to generalize all over again!” But it turns out that *with this one more invention*, just the square root of −1, *every algebraic equation can be solved!*This is a fantastic fact, which we must leave to the Mathematics Department to prove. The proofs are very beautiful and very interesting, but certainly not self-evident. In fact, the most obvious supposition is that we are going to have to invent again and again and again. But the greatest miracle of all is that we do not. This is the last invention. After this invention of complex numbers, we find that the rules still work with complex numbers, and we are finished inventing new things. We can find the complex power of any complex number, we can solve any equation that is written algebraically, in terms of a finite number of those symbols. We do not find any new numbers. The square root of i, for instance, has a definite result, it is not something new; and ii is something. We will discuss that now.

We have already discussed multiplication, and addition is also easy; if we add two complex numbers, (p+iq)+(r+is), the answer is(p+r)+i(q+s). Now we can add and multiply complex numbers. But the real problem, of course, is to compute *complex powers of complex numbers*. It turns out that the problem is actually no more difficult than computing complex powers of real numbers. So let us concentrate now on the problem of calculating 10 to a complex power, not just an irrational power, but 10(r+is). Of course, we must at all times use our rules ([22.1](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI221)) and ([22.2](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI222)). Thus

10(r+is)=10r10is.(22.5)

But 10r we already know how to compute, and we can always multiply anything by anything else; therefore the problem is to compute only10is. Let us call it some complex number, x+iy. Problem: given s, find x, find y. Now if

10is=x+iy,
then the complex conjugate of this equation must also be true, so that
10−is=x−iy.

(Thus we see that we can deduce a number of things without actually computing anything, by using our rules.) We deduce another interesting thing by multiplying these together:

10is10−is=100=1=(x+iy)(x−iy)=x2+y2.(22.6)
Thus if we find x, we have y also.

Now the problem is *how* to compute 10 to an imaginary power. What guide is there? We may work over our rules until we can go no further, but here is a reasonable guide: if we can compute it for any particular s, we can get it for all the rest. If we know10is for any one s and then we want it for twice that s, we can square the number, and so on. But how can we find 10is for even one special value of s? To do so we shall make one additional assumption, which is not quite in the category of all the other rules, but which leads to reasonable results and permits us to make progress: when the power is small, we shall suppose that the “law”10ϵ=1+2.3025ϵ is right, as ϵ gets very small, not only for real ϵ, *but for complex ϵas well*. Therefore, we begin with the supposition that this law is true in general, and that tells us that 10is=1+2.3025⋅is, for s→0. So we assume that if s is very small, say one part in 1024, we have a rather good approximation to 10is.

Now we make a table by which we can compute *all* the imaginary powers of 10, that is, compute x and y. It is done as follows. The first power we start with is the 1/1024 power, which we presume is very nearly 1+2.3025i/1024. Thus we start with

10i/1024=1.00000+0.0022486i,(22.7)

and if we keep multiplying the number by itself, we can get to a higher imaginary power. In fact, we may just reverse the procedure we used in making our logarithm table, and calculate the square, 4th power, 8th power, etc., of ([22.7](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI227)), and thus build up the values shown in Table [22–3](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T3). We notice an interesting thing, that the x numbers are positive at first, but then swing negative. We shall look into that a little bit more in a moment. But first we may be curious to find for what number s the real part of 10is is *zero*. The y-value would be 1, and so we would have 10is=1i, or is=log10i. As an example of how to use this table, just as we calculated log102 before, let us now use Table [22–3](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T3) to find log10i.

Table 22–3Successive Squares of 10i/1024=1+0.0022486i

|     |     |     |
| --- | --- | --- |
| Power is | 1024s | 10is |
| i/1024 | 0001 | −1.00000+0.00225i* |
| i/5120 | 0002 | −1.00000+0.00450i |
| i/2560 | 0004 | −0.99996+0.00900i |
| i/1280 | 0008 | −0.99984+0.01800i |
| i/6400 | 0016 | −0.99936+0.03599i |
| i/3200 | 0032 | −0.99742+0.07193i |
| i/1600 | 0064 | −0.98967+0.14349i |
| i/8000 | 0128 | −0.95885+0.28402i |
| i/4000 | 0256 | −0.83872+0.54467i |
| i/2000 | 0512 | −0.40679+0.91365i |
| i/1000 | 1024 | −0.66928+0.74332i |
|     | * Should be 0.0022486i |

Which of the numbers in Table [22–3](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T3) do we have to multiply together to get a pure imaginary result? After a little trial and error, we discover that to reduce x the most, it is best to multiply “512” by “128.” This gives 0.13056+0.99159i. Then we discover that we should multiply this by a number whose imaginary part is about equal to the size of the real part we are trying to remove. Thus we choose “64” whose y-value is 0.14349, since that is closest to 0.13056. This then gives −0.01308+1.00008i. Now we have overshot, and must *divide* by 0.99996+0.00900i. How do we do that? By changing the sign of i and multiplying by 0.99996−0.00900i (which works if x2+y2=1). Continuing in this way, we find that the entire power to which10 must be raised to give i is i(512+128+64−4−2+0.20)/1024, or 698.20i/1024. If we raise 10 to that power, we can get i. Therefore log10i=0.68184i.

### 22–6Imaginary exponents

Table 22–4Successive Powers of 10i/8

|     |     |
| --- | --- |
| p=  power⋅8/i | 10ip/8 |
| 00  | −1.00000+0.00000i |
| 01  | −0.95882+0.28402i |
| 02  | −0.83867+0.54465i |
| 03  | −0.64944+0.76042i |
| 04  | −0.40672+0.91356i |
| 05  | −0.13050+0.99146i |
| 06  | −0.15647+0.98770i |
| 07  | −0.43055+0.90260i |
| 08  | −0.66917+0.74315i |
| 09  | −0.85268+0.52249i |
| 10  | −0.96596+0.25880i |
| 11  | −0.99969−0.02620i |
| 12  | −0.95104−0.30905i |
| 14  | −0.62928−0.77717i |
| 16  | −0.10447−0.99453i |
| 18  | +0.45454−0.89098i |
| 20  | +0.86648−0.49967i |
| 22  | +0.99884+0.05287i |
| 24  | +0.80890+0.58836i |

To further investigate the subject of taking complex imaginary powers, let us look at the powers of 10 taking *successive powers*, not doubling the power each time, in order to follow Table [22–3](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T3)further and to see what happens to those minus signs. This is shown in Table [22–4](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T4), in which we take 10i/8, and just keep multiplying it. We see that x decreases, passes through zero, swings almost to −1 (if we could get in between p=10 and p=11 it would obviously swing to −1), and swings back. The y-value is going back and forth too.

![](../_resources/d4291b139ca2c71433c24bffe9fce631.png)
Figure 22–1

In Fig. [22–1](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-F1) the dots represent the numbers that appear in Table [22–4](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-T4), and the lines are just drawn to help you visually. So we see that the numbers x and y oscillate; 10is*repeats itself*, it is a *periodic* thing, and as such, it is easy enough to explain, because if a certain power is i, then the fourth power of that would be i2  *squared*. It would be +1again, and therefore, since 100.68i is equal to i, by taking the fourth power we discover that 102.72i is equal to +1. Therefore, if we wanted 103.00i, for instance, we could write it as 102.72i times 100.28i. In other words, it has a period, it repeats. Of course, we recognize what the curves look like! They look like the sine and cosine, and we shall call them, for a while, the algebraic sine and algebraic cosine. However, instead of using the base 10, we shall put them into our natural base, which only changes the horizontal scale; so we denote 2.3025s by t, and write10is=eit, where t is a real number. Now eit=x+iy, and we shall write this as the algebraic cosine of t plus i times the algebraic sine of t. Thus

eit=cos−−−t+isin−−−t.(22.8)

What are the properties of cos−−−tand sin−−−t? First, we know, for instance, that x2+y2 must be 1; we have proved that before, and it is just as true for base e as for base 10. Thereforecos−−−2t+sin−−−2t=1. We also know that, for smallt, eit=1+it, and therefore cos−−−t is nearly 1, and sin−−−t is nearlyt, and so it goes, that *all of the various properties of these remarkable functions*, which come from taking imaginary powers,*are the same as the sine and cosine of trigonometry*.

Is the period the same? Let us find out. e to what power is equal to i? What is the logarithm of i to the base e? We worked it out before, in the base 10 it was 0.68184i, but when we change our logarithmic scale to e, we have to multiply by 2.3025, and if we do that it comes out 1.570. So this will be called “algebraicπ/2.” But, we see, it differs from the regular π/2 by only one place in the last point, and that, of course, is the result of errors in our arithmetic! So we have created two new functions in a purely algebraic manner, the cosine and the sine, which belong to algebra, and only to algebra. We wake up at the end to discover the very functions that are natural to geometry. So there is a connection, ultimately, between algebra and geometry.

We summarize with this, the most remarkable formula in mathematics:
eiθ=cosθ+isinθ.(22.9)
This is our jewel.

We may relate the geometry to the algebra by representing complex numbers in a plane; the horizontal position of a point is x, the vertical position of a point is y (Fig. [22–2](http://www.feynmanlectures.caltech.edu/I_22.html#Ch22-F2)). We represent every complex number, x+iy. Then if the radial distance to this point is called r and the angle is called θ, the algebraic law is that x+iy is written in the form reiθ, where the geometrical relationships between x, y, r, and θ are as shown. This, then, is the unification of algebra and geometry.

![](../_resources/5948817a6235f93d81b14172f83de741.png)
Fig. 22–2.x+iy=reiθ.

When we began this chapter, armed only with the basic notions of integers and counting, we had little idea of the power of the processes of abstraction and generalization. Using the set of algebraic “laws,” or properties of numbers, Eq. ([22.1](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI221)), and the definitions of inverse operations ([22.2](http://www.feynmanlectures.caltech.edu/I_22.html#mjx-eqn-EqI222)), we have been able here, ourselves, to manufacture not only numbers but useful things like tables of logarithms, powers, and trigonometric functions (for these are what the imaginary powers of real numbers are), all merely by extracting ten successive square roots of ten!

1.    There is a definite arithmetic procedure, but the easiest way to find the square root of any number N is to choose some a fairly close, find N/a, average a′=12[a+(N/a)], and use this average a′ for the next choice for a. The convergence is very rapid—the number of significant figures doubles each time. [↩](http://www.feynmanlectures.caltech.edu/I_22.html#footnote_source_1)

 [Copyright © 1963, 2006, 2013  by the California Institute of Technology,  Michael A. Gottlieb and Rudolf Pfeiffer](http://www.feynmanlectures.caltech.edu/I_copyright.html)