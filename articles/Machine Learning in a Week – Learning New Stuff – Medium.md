Machine Learning in a Week – Learning New Stuff – Medium

# Machine Learning in a Week

Getting into machine learning (ml) can seem like an unachievable task from the outside.

> And it definitely can be, if you attack it from the wrong end.

However, after dedicating one week to learning the basics of the subject, I found it to be much more accessible than I anticipated.

This article is intended to give others who’re interested in getting into ml a roadmap of how to get started, drawing from the experiences I made in my intro week.

### Background

Before my machine learning week, I had been reading about the subject for a while, and had gone through half of Andrew Ng’s course on Coursera and a few other theoretical courses. So I had a tiny bit of conceptual understanding of ml, though I was completely unable to transfer any of my knowledge into code. This is what I wanted to change.

I wanted to be able to solve problems with ml by the end of the week, even through this meant skipping a lot of fundamentals, and going for a top-down approach, instead of bottoms up.

After asking for [advice on Hacker News](https://news.ycombinator.com/item?id=9432952), I came to the conclusion that Python’s Scikit Learn-module was the best starting point. This module gives you a wealth of algorithms to choose from, reducing the actual machine learning to a few lines of code.

### Monday: Learning some practicalities

I started off the week by looking for video tutorials which involved Scikit Learn. I finally landed on [Sentdex’s tutorial](http://pythonprogramming.net/machine-learning-python-sklearn-intro/) on how to use ml for investing in stocks, which gave me the necessary knowledge to move on to the next step.

![](../_resources/a1c0194d71b545929febef6391013a41.png)

The good thing about the Sentdex tutorial is that the instructor takes you through all the steps of gathering the data. As you go along, you realize that fetching and cleaning up the data can be much more time consuming than doing the actually machine learning. So the ability to write scripts to scrape data from files or crawl the web are essential skills for aspiring machine learning geeks.

I have re-watched several of the videos later on, to help me when I’ve been stuck with problems, so I’d recommend you to do the same.

However, if you already know how to scrape data from websites, this tutorial might not be the perfect fit, as a lot of the videos evolve around data fetching. In that case, the [Udacity’s Intro to Machine Learning](https://www.udacity.com/course/intro-to-machine-learning--ud120) might be a better place to start.

### Tuesday: Applying it to a real problem

Tuesday I wanted to see if I could use what I had learned to solve an actual problem. As another developer in my coding cooperative was working on Bank of England’s data visualization competition, I teamed up with him to check out the datasets the bank has released. The most interesting data was their household surveys. This is an annual survey the bank perform on a few thousand households, regarding money related subjects.

The problem we decided to solve was the following:

> Given a persons education level, age and income, can the computer predict its gender?

I played around with the dataset, spent a few hours cleaning up the data, and used the [Scikit Learn map](http://scikit-learn.org/stable/tutorial/machine_learning_map/) to find a suitable algorithm for the problem.

![](../_resources/597eb175afdd00033615027e5b0937bc.png)

We ended up with a success ratio at around 63%, which isn’t impressive at all. But the machine did at least manage to guess a little better than flipping a coin, which would have given a success rate at 50%.

Seeing results is like fuel to your motivation, so I’d recommend you doing this for yourself, once you have a basic grasp of how to use Scikit Learn.

> It’s a pivotal moment when you realize that you can start using ml to solve in real life problems.

### Wednesday: From the ground up

After playing around with various Scikit Learn modules, I decided to try and write a linear regression algorithm from the ground up.

I wanted to do this, because I felt (and still feel) that I really don’t understand what’s happening on under the hood.

Luckily, the Coursera course goes into detail on how a few of the algorithms work, which came to great use at this point. More specifically, it describes the underlying concepts of using linear regression with gradient descent.

![](../_resources/a76c7770ecd3888e8bd0531e72d1af3d.png)

This has definitely been the most effective of learning technique, as it forces you to understand the steps that are going on ‘under the hood’. I strongly recommend you to do this at some point.

I plan to rewrite my own implementations of more complex algorithms as I go along, but I prefer doing this after I’ve played around with the respective algorithms in Scikit Learn.

### Thursday: Start competing

On Thursday, I started doing Kaggle’s [introductory tutorials.](https://www.kaggle.com/c/word2vec-nlp-tutorial) Kaggle is a platform for machine learning competitions, where you can submit solutions to problems released by companies or organizations .

I recommend you trying out Kaggle after having a little bit of a theoretical and practical understanding of machine learning. You’ll need this in order to start using Kaggle. Otherwise, it will be more frustrating than rewarding.

![](../_resources/630d0197ac1ba1e7538b412767d40860.png)

The [Bag of Words](https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words) tutorial guides you through every steps you need to take in order to enter a submission to a competition, plus gives you a brief and exciting introduction into Natural Language Processing (NLP). I ended the tutorial with much higher interest in NLP than I had when entering it.

### Friday: Back to school

Friday, I continued working on the Kaggle tutorials, and also started [Udacity’s Intro to Machine Learning.](https://www.udacity.com/course/intro-to-machine-learning--ud120) I’m currently half ways through, and find it quite enjoyable.

![](../_resources/fd5de3dfc8d22cab137f2bc0f89b030c.png)

It’s a lot easier the Coursera course, as it doesn’t go in depth in the algorithms. But it’s also more practical, as it teaches you Scikit Learn, which is a whole lot easier to apply to the real world than writing algorithms from the ground up in Octave, as you do in the Coursera course.

### The road ahead

Doing it for a week hasn’t just been great fun, it has also helped my awareness of its usefulness of machine learning in society. The more I learn about it, the more I see which areas it can be used to solve problems.

> If you’re interested in getting into machine learning, I strongly recommend you setting off a few days or evenings and simply dive into it.

Choose a top down approach if you’re not ready for the heavy stuff, and get into problem solving as quickly as possible.

Good luck!

* * *

*...*

Thanks for reading! My name is Per, I’m a co-founder of [Scrimba](https://scrimba.com/) — a better way to teach and learn code.

[![](../_resources/5ca9b2a765e7df329774f1ce36b03484.png)](https://scrimba.com/)

If you’ve read this far, I’d recommend you to [check out this demo!](https://scrimba.com/casts/cast-279)