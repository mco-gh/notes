The why and how of nonnegative matrix factorization

# The why and how of nonnegative matrix factorization

February 18, 2019

tags: [Data Science](https://blog.acolyer.org/tag/data-science/), [Machine Learning](https://blog.acolyer.org/tag/machine-learning/)

.

[The why and how of nonnegative matrix factorization](https://arxiv.org/abs/1401.5226) Gillis, *arXiv 2014* from: ‘[Regularization, Optimization, Kernels, and Support Vector Machines](https://www.crcpress.com/Regularization-Optimization-Kernels-and-Support-Vector-Machines/Suykens-Signoretto-Argyriou/p/book/9781482241396).’

Last week we looked at the paper ‘[Beyond news content](https://blog.acolyer.org/2019/02/13/beyond-news-contents-the-role-of-social-context-for-fake-news-detection/),’ which made heavy use of nonnegative matrix factorisation. Today we’ll be looking at that technique in a little more detail. As the name suggests, ‘The *Why* and *How* of Nonnegative matrix factorisation’ describes both why NMF is interesting (the intuition for how it works), and how to compute an NMF. I’m mostly interested in the intuition (and also out of my depth for some of the how!), but I’ll give you a sketch of the implementation approaches.

*> “*

>  Nonnegative matrix factorization (NMF) has become a widely used tool for the analysis of high dimensional data as it automatically extracts sparse and meaningful features from a set of nonnegative data vectors.

NMF was first introduced by Paatero andTapper in 1994, and popularised in a article by [Lee and Seung](http://www.columbia.edu/~jwp2128/Teaching/E4903/papers/nmf_nature.pdf) in 1999. Since then, the number of publications referencing the technique has grown rapidly:

![nmf-fig-5.jpeg](../_resources/2f011f7be49c870d3d4955146d149867.jpg)

### What is NMF?

NMF approximates a matrix ![latex.php](../_resources/661d2b178e88ba8e0b2869eda4cd4ff2.png) with a low-rank matrix approximation such that ![latex.php](../_resources/9cfac45bc6696433207bfa15b003ccab.png).

For the discussion in this paper, we’ll assume that ![latex.php](../_resources/661d2b178e88ba8e0b2869eda4cd4ff2.png) is set up so that there are ![latex.php](../_resources/d39f1b336f6107113272fe17287ecb8a.png) data points each with ![latex.php](../_resources/a9c51fd030a2908bb5427f5c79133542.png) dimensions, and every *column* of ![latex.php](../_resources/661d2b178e88ba8e0b2869eda4cd4ff2.png) is a data point, i.e. ![latex.php](../_resources/1dbd7f463392dc6a368466a7db197387.png).

![nmf-sketch-1.jpeg](../_resources/4e510899736a07ea8086ae5b0f280e88.jpg)

We want to reduce the ![latex.php](../_resources/a9c51fd030a2908bb5427f5c79133542.png) original dimensions to ![latex.php](../_resources/263ae2c1d997affd55de275b1ee60cbc.png) (aka, create a rank ![latex.php](../_resources/263ae2c1d997affd55de275b1ee60cbc.png) approximation). So we’ll have ![latex.php](../_resources/8ac2b828b62354218e72acc3ef4ce7ab.png) and ![latex.php](../_resources/6db9c3bba1f804dec40b4c7b1bece75a.png).

The interpretation of  is that each column is a *basis element*. By basis element we mean some component that crops up again and again in all of the  original data points. These are the fundamental building blocks from which we can reconstruct approximations to all of the original data points.

The interpretation of  is that each column gives the ‘coordinates of a data point’ in the basis . In other words, it tells you how to reconstruct an approximation to the original data point from a linear combination of the building blocks in

![nmf-sketch-2.jpeg](../_resources/4fc973ad0426576dd7f6c9fd2a34a35b.jpg)

A popular way of measuring how good the approximation  actually is, is the *Frobenius norm* (denoted by the F subscript you may have noticed). The Frobenius norm is:

![latex.php](../_resources/25ccb054104cfee19f0ed9473812a9c3.png).

An optimal approximation to the Frobenius norm can be computed through truncated Singular Value Decomposition (SVD).

### Why does it work? The intuition.

*> “*

>  The reason why NMF has become so popular is because of its ability to automatically extract sparse and easily interpretable factors.

The authors give three examples of NMF at work: in image processing, text mining, and hyperspectral imaging.

#### Image processing

Say we take a gray-level image of a face containing *p* pixels, and squash the data into a single vector such that the *ith* entry represents the value of the *ith* pixel. Let the rows of  represent the *p* pixels, and the *n* columns each represent one image.

NMF will produce two matrices W and H. The columns of W can be interpreted as images (the basis images), and H tells us how to sum up the basis images in order to reconstruct an approximation to a given face.

![nmf-fig-1.jpeg](../_resources/67b7716f5d63e55b328502431634da74.jpg)
*> “*

>  In the case of facial images, the basis images are features such as eyes, noses, moustaches, and lips, while the columns of H indicate which feature is present in which image.

#### Text mining

In text mining consider the bag-of-words matrix representation where each row corresponds to a word, and each column to a document (for the attentive reader, that’s the transpose of the bag-of-words matrix we looked at in ‘[Beyond news content](https://blog.acolyer.org/2019/02/13/beyond-news-contents-the-role-of-social-context-for-fake-news-detection/)’9).

NMF will produce two matrices W and H. The columns of W can be interpreted as basis documents (bags of words). What interpretation can we give to such a basis document in this case? They represent *topics*! Sets of words found simultaneously in different documents. H tells us how to sum contributions from different topics to reconstruct the word mix of a given original document.

![nmf-text-example.jpeg](../_resources/41d3e1be3c135e89a41345b1a5c571d5.jpg)
*> “*

>  Therefore, given a set of documents, NMF identifies topics and simultaneously classifies the documents among these different topics.

#### Hyperspectral unmixing

A hyperspectral image typically has 100 to 200 wavelength-indexed bands showing the fraction of incident light being reflected by the pixel at each of those wavelengths. Given such an image we want to identify the different materials present in it (e.g. grass, roads, metallic surfaces) – these are called the *endmembers*. Then we want to know which endmembers are present in each pixel, and in what proportion. For example, a pixel might be reflecting 0.3 x the spectral signal of grass, and 0.7 x the spectral signal of a road surface.

NMF will produce two matrices W and H. The columns of W can be interpreted as basis endmembers. H tells us how to sum contributions from different endmembers to reconstruct the spectral signal observed at a pixel.

![nmf-fig-2.jpeg](../_resources/40b18242f26a7e50b3d29d421c5e006e.jpg)
*> “*

>  …given a hyperspectral image, NMF is able to compute the spectral signatures of the endmembers, and simultaneously the abundance of each endmember in each pixel.

### Implementing NMF

For a rank *r* factorisation, we have the following optimisation problem:
![nmf-opt.jpeg](../_resources/f33e15a069dd8e458cc8a4bec3fc0fe0.jpg)

Though note that the Frobenius norm show here assumes Gaussian noise, and other norms may be used in practice depending on the distribution (e.g., Kullback-Leibler divergence for text-mining, the Itakura-Saito distance for music analysis, or the  norm to improve robustness against outliers).

So far everything to do with NMF sounds pretty good, until you reach the key moment in section 3:

*> “*

>  There are many issues when using NMF in practice. In particular, NMF is NP-hard. Unfortunately, as opposed to the unconstrained problem which can be solved efficiently using the SVD, NMF is NP-hard in general.

Fortunately there are heuristic approximations which have been proven to work well in many applications.

Another issue with NMF is that there is not guaranteed to be a single unique decomposition (in general, there might be many schemes for defining sets of basis elements). For example, in text mining you would end up with different topics and classifications. “*In practice, this issue is tackled using other priors on the factors W and H and adding proper regularization terms in the objective function*.”

Finally, it’s hard to know how to choose the factorisation rank, r. Some approaches include trial and error, estimation using SVD based of the decay of the singular values, and insights from experts (e.g., there are roughly so many endmembers you might expect to find in a hyperspectral image).

*> “*

>  Almost all NMF algorithms use a two-block coordinate descent scheme (exact or inexact), that is, they optimize alternatively over one of the two factors, W or H, while keeping the other fixed. The reason is that the subproblem in one factor is convex. More precisely, it is a nonnegative least squares problem (NNLS). Many algorithms exist to solve the NNLS problem; and NMF algorithms based on two-block coordinate descent differ by which NNLS algorithm is used.

![nmf-alg.jpeg](../_resources/db2f15d5768a8744be6a43754ef98c98.jpg)

Some NNLS algorithms that can be plugged in include multiplicative updates, alternating least squares, alternating nonnegative least squares, and hierarchical alternating least squares.

The following charts show the performance of these algorithms on a dense data set (left), and a sparse data set (right).

![nmf-fig-3.jpeg](../_resources/18347dcf17c067d7673f35b58b5e1c00.jpg)

You can initialise W and H randomly, but there are also alternate strategies designed to give better initial estimates in the hope of converging more rapidly to a good solution:

- Use some clustering method, and make the cluster means of the top *r* clusters as the columns of W, and H as a scaling of the cluster indicator matrix (which elements belong to which cluster).
- Finding the best rank-r approximation of X using SVD and using this to initialise W and H (see section 3.1.8)
- Picking *r* columns of X and just using those as the initial values for W.

Section 3.2 in the paper discusses an emerging class of polynomial time algorithms for NMF in the special case where the matrix X is r-separable. That is, there exist a subset of *r* columns such that all other columns of X can be reconstructed from them. In the text mining example for instance this would mean that each topic has at least one document focused solely on that topic.

*> “*
>  … we believe NMF has a bright future…

### Share this:

- [Twitter](https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/?share=twitter&nb=1)
- [LinkedIn](https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/?share=linkedin&nb=1)
- [Email](https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/?share=email&nb=1)
- [Print](https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/#print)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20180319#)

- [![c2fa163541ebfc2eeb295cb77b2969c6](../_resources/567383508d5e612a59af0a95a5493eed.jpg)](https://en.gravatar.com/eklausmeier)
- [![66558422eae62fd9efbad8d0c7b6644e](../_resources/468ae751e19b9e6e96508b322def8a5d.jpg)](https://en.gravatar.com/vikdutt)
- [![e64d9ecae40444f351e4907c3f86a078](../_resources/ccf432265f6f4083add3c9998571c9e1.jpg)](https://en.gravatar.com/edgarventurescreative)
- [![ba156781e766856ab8c2dc927a1637a5](../_resources/fcf7b686894cfd81633bf0fb74b6b089.png)](https://en.gravatar.com/marcinciura)
- [![e731cda92dd5d374409a6554b5ead719](../_resources/9699ba73c17bcfb913b3bd0ac13d84cc.png)](https://en.gravatar.com/operationxblog)

[5 bloggers](https://widgets.wp.com/likes/index.html?ver=20180319#) like this.

### *Related*

[Beyond news contents: the role of social context for fake news detection](https://blog.acolyer.org/2019/02/13/beyond-news-contents-the-role-of-social-context-for-fake-news-detection/)In "Social Networks"

[GloVe: Global Vectors for Word Representation](https://blog.acolyer.org/2016/04/22/glove-global-vectors-for-word-representation/)In "Machine Learning"

[The amazing power of word vectors](https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/)In "Machine Learning"

.
from → [Uncategorized](https://blog.acolyer.org/category/uncategorized/)