How I’m learning “Machine Learning” – Hacker Noon

# How I’m learning “Machine Learning”

In the past year, I’ve become convinced that machine learning is not hype. Strong AI/AGI is no longer a requirement for complex tasks. It doesn’t matter that AGI is out of reach, since we don’t need it in order for automation to take over vast swathes of the job market. I now think that domain specific ML is going to take 10% to 50% of all jobs in the next few decades. The obvious ones are transportation and logistics. But almost every industry is going to be transformed. I have kids that are 1, 3, and 5. And I have no idea what will even exist when they enter the job market in 20+ years.

### My Approach

#### The Stanford Machine Learning Class

I’m 2 weeks in to Andrew Ng’s famous [Machine Learning class](https://www.coursera.org/learn/machine-learning) on Coursera. It just started last week, so if you hurry you can probably still take it this semester. This class is the one thing I’ve seen everyone involved in ML recommend. I want to learn first principles, so that I can go beyond tutorials and understand how to effectively use tools like [Tensor Flow](https://www.tensorflow.org/) and [Keras](https://keras.io/).

#### The Applications of AI — Email Newsletter

Rob May’s [**Technically Sentient**](https://www.producthunt.com/posts/technically-sentient) email newsletter has a Light Tech / Business Focus. It comes once a week at 7 AM central on Sunday mornings. He covers the one big idea from the week on topics like “whether or not the DOJ should breakup Google and Facebook over data-monopoly or AI talent-monopoly issues, and whether you will eventually be able to buy insurance against algorithmic bias.” Then he gives summaries of the 5 best articles from the week and gives another 5 that are worth a read.

#### Podcasts

I’m also supplementing with some podcasts. There’s the [**Machine Learning Guide**](https://itunes.apple.com/us/podcast/machine-learning-guide/id1204521130?mt=2) by OCDevel that gives you an introduction then gives audio commentary on each lesson covered in Andrew Ng’s class. He also gives a number of suggestions on how to break into a job in Machine Learning.

I also recommend listening to [**TWiML**](https://twimlai.com/) — This Week In Machine Learning. I listened to a long-winded [one with Xavier Amatriain](https://twimlai.com/twiml-talk-3-xavier-amatriain-engineering-practical-machine-learning-systems/) who is VPE at Quora and ran the ML group at Netflix. And every now and then the great Software Engineering Daily podcast has someone from the world of ML on the show. I enjoyed the “[Machine Learning is Hard](https://softwareengineeringdaily.com/2017/02/16/machine-learning-is-hard-with-zayd-enam/)” podcast with Zayd Enam from the Stanford AI lab. He talks about how ML is next to impossible to debug.

As for videos and slides, I found some [great slides](https://speakerdeck.com/bargava/introduction-to-deep-learning-for-natural-language-processing) that let me understand how neural networks work but I’m holding back on them until I finish the class.

![](../_resources/cca7b46629df246a16c3b4dbe0d1f022.png)![1*-P3nAIygmI8Ra3oWHw9uEQ.jpeg](../_resources/f8cd36b3915dd8371fc42d362247f7fd.jpg)

### The Class

I’ve been working on the class at night, sneaking in a video here or there during my lunch break. I’m going to talk about the class a good bit in the next few weeks and am going to pass along the high level concepts (no linear algebra or advanced math here) of what I’m learning. So here is what I’ve learned in the first two weeks:

#### **Brute Force Works**

We can throw hardware at large data sets and come up with very good predictions.

#### You don’t have to be an expert at math

I was really afraid about these requirements (I never took linear algebra), but ended up picking up the high level concepts quickly. The math is intimidating, but once you understand it at a high level, its just importing the data and running a few functions in Matlab.

#### Software is built for scale

Gradient Descent is not elegant. These problems can be solved with plain Calculus using the normal equation. However, normal equation doesn’t work on large data sets with 10,000+ features.

#### Get used to Uncertainty

Experts largely rely on rules of thumb. They don’t even fully understand how a lot of it works.

#### Debugging is damned near impossible

Neural networks are a black box and the length of time to complete an iteration means that you can’t get quick feedback.

#### Quizzes are kinda hard

They are strict about requiring 80% (4 out of 5) questions to pass. Save the PDF slides and review them before starting the test. Check and double-check your answers before submitting.

*Adios*! I hope you found this overview useful. I’ve got to do my first assignment using Octave, but there will be more to come.