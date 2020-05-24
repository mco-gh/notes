The Data Science Puzzle, Explained

# The Data Science Puzzle, Explained

The puzzle of data science is examined through the relationship between several key concepts in the data science realm. As we will see, far from being concrete concepts etched in stone, divergent opinions are inevitable; this is but another opinion to consider.

* * *

**By [Matthew Mayo](https://www.kdnuggets.com/author/matt-mayo), KDnuggets.**

![c](../_resources/91e49986ce2ed93d56273367299d3594.gif)  [comments](https://www.kdnuggets.com/2016/03/data-science-puzzle-explained.html#comments)

There is no dearth of articles around the web comparing and contrasting data science terminology. There are all sorts of articles written by all types of people relaying their opinions to anyone who will listen. It's almost overwhelming.

So let me set the record straight, for those wondering if this is one of those types of posts. Yes. Yes it is.

Why another one? I think that, while there may be an awful lot of opinion pieces defining and comparing these related terms, the fact is that much of this terminology is fluid, is not entirely agreed-upon, and, frankly, being exposed to other peoples' views is one of the best ways to test and refine your own.

So, while one may not agree entirely (or even minimally) with my opinion on much of this terminology, there may still be something one can get out of this. Several concepts central to data science will be examined. Or, at least, central *in my opinion*. I will do my best to put forth how they relate to one another and how they fit together as individual pieces of a larger puzzle.

As an example of somewhat divergent opinions, and prior to considering any of the concepts individually, KDnuggets' Gregory Piatetsky-Shapiro has put together the following Venn diagram which outlines the relationship between the very same data science terminology we will be considering herein. The reader is encouraged to compare this Venn diagram with Drew Conway's now famous [data science Venn diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram), as well as my own discussion below and modified process/relationship diagram near the bottom of the post. I think that, while differences exist, the concepts line up with some degree of similarity (see the previous few paragraphs).

![Data science Venn diagram](../_resources/66cf2193f16bddcd055e3b6d7ed81add.jpg)

We will now give treatment to the same 6 selected core concepts as depicted in the above Venn diagram, and provide some insight as to how they fit together into a data science puzzle. First, we quickly dispense with one of the biggest buzz terms of the past decade.

**Big Data**

There are all sorts of articles available defining big data, and I won't spend much time on this concept here. I will simply state that big data could very generally be defined as datasets of a size "[beyond the ability of commonly used software tools to capture, manage, and process](http://www.amazon.com/Mastering-Cloud-Computing-Foundations-Applications-ebook/dp/B00CMQJZWE)." Big data is a moving target; this definition is both vague and accurate enough to capture its central characteristic.

[(L)](https://i.imgur.com/lvOOzEm.jpg)

[![Data mining N-grams](../_resources/3b9b264ffddbd00d8858f989141976d4.jpg)](https://i.imgur.com/lvOOzEm.jpg)

[(L)](https://i.imgur.com/lvOOzEm.jpg)

As for the remaining concepts we will investigate, it's good to gain some initial understanding of their search term popularities and N-gram frequencies, in order to help separate the hard fact from the hype. Given that a pair of these concepts are relatively new, the N-gram frequencies for our 'older' concepts from 1980 to 2008 are shown above.

The more recent Google Trends show the rise of 2 new terms, the continued upward trend of 2 others, and the gradual, but noticeable, decline of the last. Note that **big data** was not included in the above graphics due to it already being quantitatively analyzed to death. Read on for further insights into the observations.

**Machine Learning**

According to [Tom Mitchell](http://www.cs.cmu.edu/~tom/) in his [seminal book on the subject](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/mitchell/ftp/mlbook.html), machine learning is "concerned with the question of how to construct computer programs that automatically improve with experience." Machine learning is interdisciplinary in nature, and employs techniques from the fields of computer science, statistics, and artificial intelligence, among others. The main artifacts of machine learning research are algorithms which facilitate this automatic improvement from experience, algorithms which can be applied in a variety of diverse fields.

I don't think there is anyone who would doubt that machine learning is a central aspect of data science. I give the term *data science* detailed treatment below, but if you consider that at a very high level its goal is to extract insight from data, machine learning is the engine which allows this process to be automated. Machine learning has a lot in common with classical statistics, in that it uses samples to infer and make generalizations. Where statistics has more of a focus on the descriptive (though it *can*, by extrapolation, be predictive), machine learning has very little concern with the descriptive, and employs it only as an intermediate step in order to be able to make predictions. Machine learning is often thought to be synonymous with pattern recognition; while that really won't get much disagreement from me, I believe that the term *pattern recognition* implies a much less sophisticated and more simplistic set of processes than machine learning actually is, which is why I tend to shy away from it.

Machine learning has a complex relationship with data mining.

*Page 2*

**By [Matthew Mayo](https://www.kdnuggets.com/author/matt-mayo), KDnuggets.**

**Data Mining**

[Fayyad, Piatetsky-Shapiro & Smyth](http://www.csd.uwo.ca/faculty/ling/cs435/fayyad.pdf) define data mining as "the application of specific algorithms for extracting patterns from data." This demonstrates that, in data mining, the emphasis is on the application of algorithms, as opposed to on the algorithms themselves. We can define the relationship between machine learning and data mining as follows: data mining is a **process**, during which machine learning algorithms are utilized as **tools** to extract potentially-valuable patterns held within datasets.

Data mining, as a sister term of machine learning, is also critical to data science. Before the explosion of the term data science, in fact, data mining enjoyed much greater success as a Google search term. Having a look at Google Trends stretching back a further 5 years than those shown in the above graphic, data mining was once much more popular. Today, however, data mining seems to be split as a concept between machine learning and data science itself. If one was to endorse the above explanation, that data mining is a *process*, then it makes sense to view data science as both a superset of data mining as well as a successor term.

**Deep Learning**

Deep learning is a relatively new term, although it has existed prior to the dramatic uptick in online searches of late. Enjoying a surge in research and industry, due mainly to its incredible successes in a number of different areas, deep learning is the process of applying deep neural network technologies - that is, neural network architectures with multiple hidden layers - to solve problems. Deep learning is a process, like data mining, which employs deep neural network architectures, which are particular types of machine learning algorithms.

Deep learning has racked up an impressive collection of accomplishments of late. In light of this, it's important to keep a few things in mind, at least in my opinion:

- Deep learning is not a panacea - it is not an easy one-size-fits-all solution to every problem out there
- It is not the fabled master algorithm - deep learning will not displace all other machine learning algorithms and data science techniques, or, at the very least, it has not yet proven so
- Tempered expectations are necessary - while great strides have recently been made in all types of classification problems, notably computer vision and natural language processing, as well as reinforcement learning and other areas, contemporary deep learning does not scale to working on very complex problems such as "solve world peace"
- Deep learning and artificial intelligence are not synonymous

Deep learning can provide an awful lot to data science in the form of additional processes and tools to help solve problems, and when observed in that light, deep learning is a very valuable addition to the data science landscape.

**Artificial Intelligence**

Most people find a precise, and often times even a broad, definition of artificial intelligence difficult to put their finger on. I am not an artificial intelligence researcher, and so my answer here may wildly differ from someone who is, or may even upset folks in other fields. I have philosophized on the idea of AI a lot over the years, and I have come to the conclusion that artificial intelligence, at least the concept of it which we generally think of when we **do** think of it, does not actually exist.

In my opinion, AI is a yardstick, a moving target, an unattainable goal. Whenever we get on a path toward AI achievements, somehow these accomplishments seem to morph into being referred to as something else.

I once read something like the following: If you asked an AI researcher in the 1960s what their idea of AI was, they would probably agree that a small device that fit in our pockets, which could help anticipate our next moves and desires, and had the entirety of human knowledge readily available at will, there would probably be consensus that said device was true AI. But we all carry smartphones today, a very few of us would refer to them as artificial intelligence.

Where does AI fit into data science? Well, as I have stated that I don't believe that AI is really anything tangible, I guess it's hard to say that it fits in anywhere. But there are a number of areas related to data science and machine learning where AI has provided **motivation**, which at times is just as valuable as the tangible; computer vision certainly comes to mind, as does contemporary deep learning research, which have both benefited from the *Artificial Intelligence Ethos* at some point, if not indefinitely.

AI may well be the research and development apparatus with the deepest pockets which never actually produces anything in its namesake industry. While I would say that drawing a straight line from AI to data science may not be the best way to view the relationship between the 2, many of the intermediary steps between the 2 entities have been developed and refined by AI in some form.

**Data Science**

So, after discussing these related concepts and their place within data science, what exactly **is** data science? To me, this is the toughest concept of the lot to attempt to define precisely. Data science is a multifaceted discipline, which encompasses machine learning and other analytic processes, statistics and related branches of mathematics, increasingly borrows from high performance scientific computing, all in order to ultimately extract insight from data and use this new-found information to tell stories. These stories are often accompanied by pictures (we call them visualizations), and are aimed at industry, research, or even just at ourselves, with the purpose of gleaning some new idea from The Data.

Data science employs all sorts of different tools from a variety of related areas (see everything you've read above here). Data science is both synonymous with data mining, as well as a superset of concepts which **includes** data mining.

Data science yields all sorts of different outcomes, but they all share the common aspect of insight. Data science is all of this and more, and to you it may be something else completely... and we haven't even covered acquiring, cleaning, wrangling, and pre-processing data yet! And by the way, what even **is** data? And is it always big?

I think my idea of the data science puzzle, at least, the version of it which can be represented by the above diagram, jives well with Piatetsky-Shapiro's Venn diagram at the top of this post. I would also suggest that it is also mostly in agreement with with Drew Conway's [data science Venn diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram), though I would add one caveat: I believe his very well-reasoned and useful graphic is actually referring to **data scientists**, as opposed to data science. This may be splitting hairs, but I don't think the { field | discipline | concept } of data science, itself, encompasses hacking skills; I believe this is a skill that scientists possess in order to allow the to **do** data science. Admittedly, this may be quibbling over semantics, but it makes sense in my mind.

Of course, this is not a full picture of the landscape, which is constantly evolving. For example, I recall reading, not very long ago, that data mining was a sub-field of business intelligence! Even with differences in opinions, I really can't imagine this being a valid idea today (it was difficult to accept a few years ago, to be honest).

And there you have it: some of your favorite terms bent out of shape in new ways you won't forgive me for. If you're furious right now and can't wait to tell me how wrong I am, remember the point of this post: you have just read one man's opinion. In that spirit, feel free to sound off in the comments with your (potentially heated and sharply) contrasting views. Otherwise, I hope that this has either exposed new readers to the puzzle which is data science or forced them to look at their own version of this puzzle in their heads.

**Related**: