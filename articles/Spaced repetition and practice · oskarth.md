Spaced repetition and practice · oskarth

# Spaced repetition and practice

 March 2016

How do we become fluent in skills quickly? How can we retain that knowledge with the minimum amount of effort?

The last few months I’ve been doing a bunch of experiments centered around practice and retention [1](https://www.oskarth.com/srspractice/#fn:0a3db678c83b7ddc490b6d6184b15cc8:1). We often learn how to do things and then forget. How can we avoid this? One solution is over-learning, which happens naturally for things we do a lot. I suspect this is one of the reasons fundamentals are often learned better once we do more advanced things. For example, if you grow up speaking German pronouns and cases will be ingrained, because you’ve dealt with sentences that depended on them for so long.

What about skills that are not naturally over-learned, for whatever reason? Perhaps you only use JavaScript, SQL or Awk every now and then. Can we learn things once and easily maintain that skill?

As I refined my experiments, I became curious about the possibility of retaining know-how (techne, or skills) using techniques that are usually used for know-what (episteme, or facts). The line between the two is sometimes blurry, but one distinction is that one can be codified and described, whereas the other is often implicit or “silent”. For example, the capital of France is Paris is know-what, whereas knowing how to hammer a nail into a piece of wood at an angle is know-how.

One thought that tickled my imagination is that as we are programming, we often make the same mistakes, or forget to ask ourselves certain questions that would let us get to the core of the problem. Perhaps it is possibly to reprogram oneself to remember these things, thus aiding in know-how fluency. At one extreme you have things like remembering standard library functions or syntax, and at another you have generalized heuristics about how to think about certain classes of problems in terms of trade offs, invariants to check, problem solving techniques etc.

## Spaced repetition background

A *spaced repetition system* (SRS) is a way of efficiently repeating things you don’t want to forget, usually by using electronic flashcards. A SRS exploits the fact that if you remember something well you don’t have to repeat it as often. Its basis in the literature is called the *forgetting curve* and was discovered by Hermann Ebbinghaus through laborious self-experimentation close to 150 years ago. The SRS I use is called Anki [2](https://www.oskarth.com/srspractice/#fn:0a3db678c83b7ddc490b6d6184b15cc8:2).

## Hypothesis

Given that I’ve *learned how to do something* and added multiple cards to my*spaced repetition system* (SRS), I’ll be able to:

(a) solve the same problem in roughly the same amount of time, regardless of how long it’s been since I did it the last time (a kind of time-invariance).

(b) solve problems I’ve previously learned to solve twice as fast as if I don’t use spaced repetition.

## Methodology

I worked on 10 small exercises from the book *Eloquent Javascript* that I couldn’t immediately produce an “optimal” solution for. I did this until I:

1. felt like I understood the problem
2. solved it in ~5-10m from scratch.

This was my criterion for what it means to *learn* something, not unlike what Ebbinghaus calls the *first errorless reproduction* in his studies on memory[3](https://www.oskarth.com/srspractice/#fn:0a3db678c83b7ddc490b6d6184b15cc8:3).

For each exercise I made a few (2-8) flash cards and added them to my SRS. I also precomputed a series of 5 As and 5 Bs in a random order that I was unaware of [4](https://www.oskarth.com/srspractice/#fn:0a3db678c83b7ddc490b6d6184b15cc8:4). After I added all the cards for that exercise, I checked the next draw in my random sequence. If I got an A I kept the cards, and if I got a B I suspended it (i.e. I won’t see it again).

As for the content of the cards, I tried a mix of cards that are all possible to do in one’s head. Examples of types of cards include:

1. Checks for conceptual understanding
2. Basic debugging: what’s wrong with this piece of quote
3. Complete a piece of tricky code
4. Listing exhaustive cases to check for some simple domain
5. Basic syntax and idioms questions

See my notebook [5](https://www.oskarth.com/srspractice/#fn:0a3db678c83b7ddc490b6d6184b15cc8:5) for more concrete examples. Doing this, I believe I eliminated any bias I have in the effort I put into learning each thing, and in making the cards. I believe the effect will be more pronounced with time, but I capped the delay from learning to testing to an average of three weeks. Each practice test was capped to 20 minutes.

Notice that the learning is a question of *know-how* whereas the repetition is a question of *know-what*. The *know-how* is tested by the actual act of writing code, whereas the *know-what* is tested by me judging how well I answered a flash card in my head.

## Result

Group A took 18 minutes in total, and all problems were solved in around 5m. Group B took 46m to solve in total. Group B includes one that I didn’t solve (counted as 20m) and one partial solution that took 11m. I decided to count the partial solution as a solution as it was mostly correct.

I was thus unable to falsify my hypothesis.

## Conclusion: caveats and reflection

What does this mean? To begin with, I want to mention two caveats with the results:

(1) Anki tracks the total time spent per card, and summing up all the cards I did the total time spent rehearsing was 19 minutes. This effort was spread out over the three weeks. If we were to include this the total time spent on group A would double. However, if the results indeed are time-invariant (i.e. it’ll take ~5m several months from now), the spacing effect would ensure that proportionally less time is spent reviewing.

(2) Capping a solution to 20 minutes doesn’t really make sense, as it’s really a non-solution. However, this makes the test “harder”, so the artifical cap might be fine. One way of getting around this difficulty is using a better non-binary test (i.e. not just solution and non-solution), such as what Ebbinghaus did when he looked at time for first errorless reproduction.

Taking the result at face-value, it seems as if it is indeed possible to retain practical skills by practicing know-what. There are a lot of questions that remain to be answered though. The first three are more practical and the latter three more philosophical, at least in their stated form:

1. Can other people reproduce it?
2. Does the effect remain the same after several months, or does it fall apart?
3. What happens when we ramp up the difficulty of the problems solved?

4. The elephant in the room: How much are we over-specializing for these specific problems when we are repeating? How transferable is the skill of learning to solve problem X for solving problem Y?

5. The second elephant: Is time better spent learning new things that build on previous things you learned, allowing for some forgetting, rather than clinging to remembering how to solve specific problem quickly?

6. The third elephant: How does this, if at all, relate to skills and problems that don’t have (clear) solutions? In a very real sense, those are the interesting problems in life.

I mention the elephants because (a) they are important and (b) I’m still thinking about them. But there’s nothing in my experiment that remotely touches on them, so I’m forced to keep silent on the matter.

That said, I was somewhat surprised to see how effective using SRS was for retaining practical know-how. It seems like this technique is useful for a lot of things, especially when there’s a premium on fluency.

## Do you want to reproduce?

I realize this is a long shot, especially since it takes quite a bit of effort to do, but if you are interested in this type of thing it’d be very interesting to see if this result is reproducible. Let me know on[Twitter](https://twitter.com/oskarth) or by [email](https://www.oskarth.com/srspractice/mailto:me@oskarth.com) if you want to chat about how to structure it and maybe extend it.

(If you liked this, you might enjoy [No Computer](http://oskarth.com/no-computer). To stay up to date on my experiments, consider[subscribing](https://oskarth.us10.list-manage.com/subscribe?u=eb9509b0e9820f2fc234227d6&id=6bb99e6219).)

* * *

1. If you are interested in reading about them in chronologial order, you can find them in my [experiments notebook](http://plan.oskarth.com/) (entry 17-25). [[return]](https://www.oskarth.com/srspractice/#fnref:0a3db678c83b7ddc490b6d6184b15cc8:1)

2. [Anki](http://ankisrs.net/). [[return]](https://www.oskarth.com/srspractice/#fnref:0a3db678c83b7ddc490b6d6184b15cc8:2)

3. Ebbinghaus’s *On Memory* is available [online](http://psychclassics.yorku.ca/Ebbinghaus/). [[return]](https://www.oskarth.com/srspractice/#fnref:0a3db678c83b7ddc490b6d6184b15cc8:3)

4. [Random secret sequence script](https://gist.github.com/oskarth/1d2a1772d11006f45a32). [[return]](https://www.oskarth.com/srspractice/#fnref:0a3db678c83b7ddc490b6d6184b15cc8:4)

5. [Examples of Anki cards](http://plan.oskarth.com/22). These cards are from previous experiment, but the principle is the same. [[return]](https://www.oskarth.com/srspractice/#fnref:0a3db678c83b7ddc490b6d6184b15cc8:5)