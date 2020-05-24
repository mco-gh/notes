Why 10 percent of all Google Search results are changing

Google is currently [rolling out a change to its core search algorithm](http://blog.google/products/search/search-language-understanding-bert) that it says could change the rankings of results for as many as one in ten queries. It’s based on cutting-edge natural language processing (NLP) techniques developed by Google researchers and applied to its search product over the course of the past 10 months.

In essence, Google is claiming that it is improving results by having a better understanding of how words relate to each other in a sentence. In one example Google discussed at a briefing with journalists yesterday, its search algorithm was able to parse the meaning of the following phrase: “Can you get medicine for someone pharmacy?”

The old Google search algorithm treated that sentence as a “bag of words,” according to Pandu Nayak, Google fellow and VP of search. So it looked at the important words, medicine and pharmacy, and simply returned local results. The new algorithm was able to understand the context of the words “for someone” to realize it was a question about whether you could pick up somebody else’s prescription — and it returned the right results.

"**Before, Google treated queries like “a bag of words”**"

The tweaked algorithm is based on [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html), which stands for “Bidirectional Encoder Representations from Transformers.” Every word of that acronym is a term of art in NLP, but the gist is that instead of treating a sentence like a bag of words, BERT looks at all the words in the sentence as a whole. Doing so allows it to realize that the words “for someone” shouldn’t be thrown away, but rather are essential to the meaning of the sentence.

The way BERT recognizes that it should pay attention to those words is basically by self-learning on a titanic game of Mad Libs. Google takes a corpus of English sentences and randomly removes 15 percent of the words, then BERT is set to the task of figuring out what those words ought to be. Over time, that kind of training turns out to be remarkably effective at making a NLP model “understand” context, according to Jeff Dean, Google senior fellow & SVP of research.

Another example Google cited was “parking on a hill with no curb.” The word “no” is essential to this query, and prior to implementing BERT in search Google’s algorithms missed that.

 [pasted_image_0.webp](../_resources/e6d2c74fcaccd931b77d108aa04c07e9.webp)

Google says that it has been rolling the algorithm change out for the past couple of days and that, again, it should affect about 10 percent of search queries made in English in the US. Other languages and countries will be addressed later.

All changes to search are run through a series of tests to ensure they’re actually improving results. One of those tests involves using Google’s cadre of human reviewers who train the company’s algorithms by rating the quality of search results — Google also conducts live live A/B tests.

Not every single query will be affected by BERT, it’s just the latest of many different tools Google uses to rank search results. How exactly all of it works together is a bit of a mystery. Some of that process is kept intentionally mysterious by Google to keep spammers from gaming its systems. But it’s also mysterious for another important reason: when a computer uses machine learning techniques to make a decision, it can be hard to know why it made those choices.

"**BERT could affect as many as 10 percent of all Google searches**"

That so-called “black box” of machine learning is a problem because if the results are wrong in some way, it can be hard to diagnose why. Google says that it has worked to ensure that adding BERT to its search algorithm doesn’t increase bias — a common problem with machine learning whose training models are themselves biased. Since BERT is trained on a giant corpus of English sentences, which are also inherently biased, it’s an issue to keep an eye on.

The company also says that it doesn’t anticipate significant changes in how much or where its algorithm will direct traffic, at least when it comes to large publishers. Any time Google signals a change in its search algorithm, the entire web sits up and takes notice. Companies have lived and died by Google’s search rank changes.

Everybody who makes money on web traffic absolutely should take notice. When it comes to the quality of its search results, Payak says that “this is the single biggest ... most positive change we’ve had in the last five years and perhaps one of the biggest since the beginning.”