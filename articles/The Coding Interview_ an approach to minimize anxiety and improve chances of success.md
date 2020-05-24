The Coding Interview: an approach to minimize anxiety and improve chances of success

# The Coding Interview: an approach to minimize anxiety and improve chances of success

[![0*TE0s_KqKZnEVmTLy.jpeg](../_resources/e386d175a6509b902271eab6dd445359.jpg)](https://medium.com/@mylesborins?source=post_header_lockup)

[Myles Borins](https://medium.com/@mylesborins)
Apr 9, 2018·10 min read
*A framework for those who whiteboarding code doesn’t come naturally to*

![](../_resources/366cf71538b9f9736d0bd1edea897fa7.png)![1*tU5VTdzTqHYoqcfCQ65hvQ.jpeg](../_resources/98cd7334237770943031011dd0c8883f.jpg)

The Dreaded Whiteboard

### TLDR;

1. 1.Ask questions to define the problem space
2. 2.Implement a terrible solution
3. 3.Test that solution
4. 4.Optimize that solution

### Note

This essay primarily targets mid to senior level individuals who already have a vast skillset but have trouble presenting them in the “whiteboard interview”. Perhaps you came from a non-traditional background, or perhaps you simply don’t perform well under pressure. I will be writing assuming that you are an amazing hire, have the skills for the job you are interviewing for, and simply need help presenting those skills in an interview that doesn’t feel designed to help you succeed.

### Technical interviews are hard

I come from a non traditional background. My undergraduate degree was in Fine Art, and my Masters Degree was in Music Technology. While both programs had a fairly rigorous amount of technical focus, I did not end up taking the majority of fundamental CS courses that prepare you for the technical interview.

> Want to discuss internal implementations of Malloc?
Sure!
> Fourier transforms for signal analysis of complex analog systems?
Why not?
> How to build successful open source communities at scale?
Let’s talk all day!
> Analyze this algorithm and tell me the complexity and how to improve it
Can we not?

### Interview Reform

It is easy to criticize interview processes that rely on whiteboarding and technical programming “challenges”. I have feelings about it. I’m not going to explore those feelings in this write-up, rather I am going to focus on how to succeed within the existing system. I support those that choose not to participate in an interviewing culture they disagree with, and I definitely have the utmost of respect for those experimenting with new models.

The purpose of this write-up is to share my experiences and hopefully help those that find themselves in a technical interview have a better chance at success.

### How did you do it?

For my current role as a Developer Advocate on Google Cloud Platform I had to go through a number of technical screening interviews that included coding problems. To say I was nervous is an understatement. I had previously interviewed at Google 4 times, and only once been invited to an on-site interview. That on-site… didn’t go very well. To prepare for the Developer Advocate interview I spent some time reviewing what had worked in past interviews, I read a bunch of advice online, and I came up with a framework to answering questions. Without this framework I don’t believe I would have been successful in the last round of technical interviews.

### A quick note about standardized tests

To get into graduate school I had to write the GRE. This was a similarly painful exercise in monotonous study; it felt like wasted time. These kinds of standardized tests are designed to test one thing in particular, how good you are at taking the test. Studying for the GRE leaves you with one very particular skill set, taking the GRE.

To say that I felt the time I invested in the GRE was wasted is an understatement. To be frank I resented having to pay a bunch of money to study and participate in what I viewed as a fairly toxic and limiting institutional ritual. The only thing I learned was “how to take the GRE”.

For example, rather than learn every dang word in the dictionary, I learned how to guess the “charge” of a word. Knowing if a word is “Positively” or “Negatively” charged can help you answer a good chunk of the GRE vocabulary questions when you don’t know the answer. In fact the biggest trick to the GRE was figuring out how to identify “Wrong Answers” rather than trying to find the “Right” ones.

### An abstraction for success

Inspired by the monotony that is the GRE I attempted to make a similar framework for answering technical interview questions. A pattern that can be applied to any technical question on any topic. An abstraction to help me succeed, to get that job I really wanted.

To build this abstraction I needed to untangle what these technical interviews are trying to accomplish. From a distance it can appear to be insiders baseball, a song and dance to identify those who have “done the work”. A technical sphinx stopping the unwanted outsiders from entering the field of a high paying tech job.

The technical interview at many companies can be described as a “toy” problem that is easy to “solve” if you know the “trick”. Through a number of conversations with friends who had been interviewers at Google I came to learn that this is not the intention of the technical interview. Rather interviewers are giving interviewees carefully planned questions to identify certain signals. A panel of interviewers are attempting to collect enough signal to give the recruiter and a hiring committee enough confidence to move your application forward.

*What types of signal?*

Intelligence, thoughtfulness, experience in a technology, leadership, and any number of other factors that are important in identifying a good hire.

*What is not a signal?*

Your ability to regurgitate an answer to a specific problem you already know. In fact, interviewers are likely hoping to ask you questions that you will not know in order to see how you work towards a solution.

**The first thing to do in any interview is to figure out what signal the interviewer is measuring for**.

### Step 1: Ask questions to define the problem space

Even if you know exactly how to solve a problem you need to ensure that you are going to spend your time implementing the parts of that solution your interviewer cares about.

Asking pointed question can help you determine what to *not focus on*. You need to ask clarifying questions to make sure you are answering the right problem. Many times interview questions will be asked with purposefully missing details to see if you can figure out the right questions to ask.

Another mistake is assuming that you need to write all the code necessary to solve the problem. If you begin to design your solution from an extremely high level, you can check in with the interviewer to see if you can be provided certain APIs as helpers rather than implementing it yourself.

For example, in an interview a problem involved taking a string with a combination of characters and returning a new string of only lower case characters in sorted order. This transformation was an implementation detail to my solution, and not a direct requirement of the original question. I asked the interviewer if I could be provided a function `*sanitizeString(input)`, *I defined the behavior verbally, and outlined an interface. The interviewer was comfortable with that contract and I moved forward with the solution without having to implement a sort or a regular expression.

Some important notes from the above interaction:

- •It identified that Sorting and Regular expressions were not signals this question was measuring
- •It showed that I could define an interface that solved my problem
- •It saved me time from implementing unnecessary code

Make sure to keep track of how much time you are spending in this phase. I’ve personally made the mistake of asking too many questions and then not leaving enough time to actually write any code. Even if you and the interviewer have an amazing conversation they will need to show evidence that you coded a solution to the problem.

### Step 2: Implement a terrible solution

It is possible to begin this step while still asking lots of questions. High level pseudocode API signatures can help you grasp a higher level architecture of what your eventual solution will look like. That being said no number of questions or excellent pseudocode will allow you to avoid coding.

When embarking on your initial implementation it is important not to overthink it. The goal here is to get code on the board. It is possible that your initial solution won’t even work, we’ll deal with that later. The worst thing you can do in a technical interview is not write any code. The easiest way to not write any code is to overthink it.

Don’t attempt to optimize your solution yet. Do let your interviewer know about the concessions you’ve made. You can show that you have an understanding of complexity without having to do a proof. Is the first way you think of solving a problem involve a slow for loop that makes your heart sad? That is actually a great sign! Implement something that you think will work, let the interviewer know that this code makes you sad, and move on.

I know what you are thinking, “If I write bad code they’ll never hire me”. This is not true. You are working in an artificial environment, with artificial constraints. They want to see those signals of a good hire. A good programmer knows when they are making concessions and documents it to fix later. A good hire knows that perfect is the enemy of good, that shipping nothing is worse than iterative improvements.

Bang out that terrible code, make notes of every place that can improve, and move on.

### Step 3: Test that solution

Now that you’ve banged out some absolutely horrendous and potentially embarrassing code we are going to do some manual testing to ensure it does what it is saying it does. This is a place where your errors can shine! No one writes perfect code, especially not under pressure.

There are a couple type of input you are going to want to test for:

- •small valid input
- •large valid input
- •small invalid input
- •large invalid input
- •OMG WHO EVER THOUGHT THIS WOULD BE INPUT

For each of these types of input manually walk through your code and ensure that it does all the things it promises to. This is where you will likely find that you didn’t properly validate some input, or made an off by one error. Feel free to keep a ledger to the side of the code to keep track of the state of the code while you are stepping through.

If you find an error, explain what the error was, fix it, and move on.

During this step you will have multiple opportunities to discuss your extensive knowledge of automated testing. How would you generate all sorts of input? How would you stub parts of the code? What test runner would you use? What CI would you use? These are great signals to show an interviewer that could easily be completely missed if you simply “coded a perfect solution” right away.

So now we’ve tested our code, found some bugs and fixed them. We’ve humble-bragged about all the best practices we love, and there is still some time left. It is now time to make like a prime and optimize.

### Step 4: Optimize that solution

Remember how earlier when your gut was telling you that certain code was “icky” and you wanted to make it better but I urged you to just “bang it out” and move on? It is now time to revisit it, but with a twist. Rather than deciding which parts of the code to optimize we’ll lean on our interviewer to leak a bit more of the signal they are measuring for.

> “So it looks like we have a bit of time left, there were a couple places in the solution I wasn’t happy with earlier, do you have a preference in what I optimize?”

At this point the interviewer will let you know if it even makes sense to continue on this particular problem. It is very possible that after your brute-force solution and testing they have gathering all of the important information about you. If not, this is when they will let you know. Having identified earlier which parts of your code are slow will help you be successful here.

The interviewer may want to do a complexity analysis of the part of your solution you have identified for optimization, this is where a bit of practice understanding how to measure the O(n) of an algorithm will come in handy. Even without being able to perfectly analyze an algorithm you might be able to get away with relying on your gut. Is a for loop iterating over an entire list? O(n). Is a for loop iterating over a list and then iterating over the list again for each item? O(n^2).

One way to optimize a problem is to consider pre-processing data and putting it into a lookup table or hash-map. If part of your problem involves transforming data consider the time + space tradeoffs. Can any of the transformation that needs to be applied to the data be done in advance? If you can pre-process data you can turn an extreme complex operation into an O(1) lookup, trading time for space on disk.

There are many problems in which the computational complexity of the solution vanishes the moment you are no longer processing data in a hot path. Writing a script for processing data does not have the same requirements as production code, and offers another opportunity to gauge the signal your interviewer is trying to measure.

### Bringing it all together

Please take everything I’ve said with a grain of salt. Some questions do not require this framework, while others may only require a subset. It may make sense to optimize some pseudocode before implementation, and it may not make sense to test at all. Like anything, paint outside the lines when it makes sense, but don’t forget the overall pattern.

The biggest take away I would like to impart is that a good interviewer is looking for a “signal” of a good hire, not the “answer” to an arbitrary problem. If you can learn to identify which signals they are not looking for, you can focus your time on the right things.

You still need to study and practice. You still need to be damn good at what you do. What you don’t need is a Computer Science degree to succeed.