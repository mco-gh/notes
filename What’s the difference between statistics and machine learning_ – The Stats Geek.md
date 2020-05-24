What’s the difference between statistics and machine learning? – The Stats Geek

# What's the difference between statistics and machine learning?

[August 8, 2019](https://thestatsgeek.com/2019/08/08/whats-the-difference-between-statistics-and-machine-learning/)  by [Jonathan Bartlett](https://thestatsgeek.com/author/jwb133googlemail-com/)

I had an interesting discussion at work today (among people I think would all call themselves statisticians!) about the distinction(s) between statistics and machine learning. It is something I am still not very clear about myself, and have yet to find a satisfactory answer. It's a topic that seems to get particularly some statisticians hot under the collar, when machine learning courses apparently claim that methods statisticians tend to think are part of statistics are in fact part of machine learning:

This post is certainly not going to tell you what the difference machine learning and statistics is. Rather I hope that it spurs readers of the post to help me understand their differences.

Historically I think it's the case that machine learning algorithms were developed in computer science departments of universities, whereas statistics was developed within mathematics or statistics departments. But this is merely about the historical origins, rather than any fundamental distinction.

Machine learning (about which I know a lot less) tends I think to focus on algorithms, and a subset of these has as their objective to prediction some outcome based on a set of inputs (or predictors as we might call them in statistics). In contrast to parametric statistical models, these algorithms typically do not make rigid assumptions about the relationships between the inputs and the outcome, and therefore can perform well then the dependence of the outcome on the predictors is complex or non-linear. The potential to capture such complex relationships is however not unique to machine learning - within statistical models we have flexible parametric / semiparametric, and even non-parametric methods such as [non-parametric regression](https://en.wikipedia.org/wiki/Nonparametric_regression).

The Wikipedia page on [machine learning](https://en.wikipedia.org/wiki/Machine_learning#Relation_to_statistics) states:

**

> Machine learning and > [> statistics](https://en.wikipedia.org/wiki/Statistics)>  are closely related fields in terms of methods, but distinct in their principal goal: statistics draws population > [> inferences](https://en.wikipedia.org/wiki/Statistical_inference)>  from a > [> sample](https://en.wikipedia.org/wiki/Sample_(statistics))> , while machine learning finds generalizable predictive patterns.

**

So statistics is about using sample data to draw inferences or learn about a wider population from which the sample has been drawn, whereas machine learning finds patterns in the data that can be generalised. It's not clear from this quote alone to what machine learning will generalise to, but the natural thing that comes to mind is some broader collection or population which is similar to the sample at hand. So this apparent distinction seems quite subtle. Indeed the Wikipedia page goes on to say:

**

> A core objective of a learner is to generalize from its experience.> [> [2]](https://en.wikipedia.org/wiki/Machine_learning#cite_note-bishop2006-2)> [> [17]](https://en.wikipedia.org/wiki/Machine_learning#cite_note-17)>  Generalization in this context is the ability of a learning machine to perform accurately on new, unseen examples/tasks after having experienced a learning data set. The training examples come from some generally unknown probability distribution (considered representative of the space of occurrences) and the learner has to build a general model about this space that enables it to produce sufficiently accurate predictions in new cases.

**

To me, when one starts saying that the training data is considered representative of the space of occurrences, this sounds remarkably similar to the notion of the training data being a sample from some larger population, as would often be assumed by statistical models.

An interesting [short article in Nature Methods by Bzdok](https://doi.org/10.1038/nmeth.4642) and colleagues considers the differences between machine learning and statistics. The key distinction they draw out is that statistics is about inference, whereas machine learning tends to focus on prediction. They acknowledge that statistical models can often be used both for inference and prediction, and that while some methods fall squarely in one of the two domains, some methods, such as bootstrapping, are used by both. They write:

**

> ML makes minimal assumptions about the data-generating systems; they can be effective even when the data are gathered without a carefully controlled experimental design and in the presence of complicated nonlinear interactions. However, despite convincing prediction results, the lack of an explicit model can make ML solutions difficult to directly relate to existing biological knowledge.

**

The claim that ML methods can be effective even when the data are not collected through a carefully controlled experimental design is interesting. First it seems to imply that statistics is mainly useful only when the data are from an experiment, something which epidemiologists conducting observational studies or survey statisticians conducting national surveys would presumably take issue with. Second it seems to suggest that ML can give useful predictions for the future with minimal assumptions on how the training data arose. This seems problematic, and I cannot see why the importance of how the data arose should be different depending on whether you use a statistical method or a machine learning method. For example, if we collect data on the association between an exposure (e.g. alcohol consumption) and an outcome (e.g. blood pressure) from an observational (non-experimental) study, I cannot see how machine learning can without additional assumptions overcome the probable issue of confounding.

As I wrote earlier, I do not have a well formed view of the distinction between machine learning and statistics. My best attempt is the following: statistics starts with a model assumption, which could be more rigid (i.e. simple parametric models) or less so (i.e. semiparametric or nonparametric) which describes aspects of the data generating distribution in a way that answers a question of interest or could be used for prediction for the population from which the sample has been drawn. Uncertainty about parameters in the model or about predictions can be quantified. Machine learning doesn't assume a model, but is a collection of algorithms for building prediction rules or finding clustering in data. The prediction rules should work well at prediction future data. Uncertainty about predictions or clustering is presumably not possible or harder, given the absence of a model.

Please add your views in a comment and help me understand the distinction(s).

I posted this to the website Hacker News last night, and it picked up some interest. As a consequence there are lots of interesting comments from people available on the its[Hacker News thread](https://news.ycombinator.com/item?id=20650215).

### You may also be interested in:

- [Machine learning vs. traditional modelling techniques](https://thestatsgeek.com/2015/11/19/machine-learning-vs-traditional-modelling-techniques/)

Categories [Miscellaneous](https://thestatsgeek.com/category/miscellaneous/)
Post navigation

[Setting seeds when running R simulations in parallel](https://thestatsgeek.com/2019/06/21/setting-seeds-when-running-r-simulations-in-parallel/)