Support vector machine - Wikipedia

# Support vector machine

From Wikipedia, the free encyclopedia

Not to be confused with [Secure Virtual Machine](https://en.wikipedia.org/wiki/Secure_Virtual_Machine).

In [machine learning](https://en.wikipedia.org/wiki/Machine_learning), **support vector machines** (**SVMs**, also **support vector networks**[[1]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-CorinnaCortes-1)) are [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) models with associated learning [algorithms](https://en.wikipedia.org/wiki/Algorithm) that analyze data used for [classification](https://en.wikipedia.org/wiki/Statistical_classification) and [regression analysis](https://en.wikipedia.org/wiki/Regression_analysis). Given a set of training examples, each marked as belonging to one or the other of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making it a non-[probabilistic](https://en.wikipedia.org/wiki/Probabilistic_classification)  [binary](https://en.wikipedia.org/wiki/Binary_classifier)  [linear classifier](https://en.wikipedia.org/wiki/Linear_classifier) (although methods such as [Platt scaling](https://en.wikipedia.org/wiki/Platt_scaling) exist to use SVM in a probabilistic classification setting). An SVM model is a representation of the examples as points in space, mapped so that the examples of the separate categories are divided by a clear gap that is as wide as possible. New examples are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall.

In addition to performing linear classification, SVMs can efficiently perform a non-linear classification using what is called the [kernel trick](https://en.wikipedia.org/wiki/Kernel_trick), implicitly mapping their inputs into high-dimensional feature spaces.

When data are not labeled, supervised learning is not possible, and an [unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning) approach is required, which attempts to find natural [clustering of the data](https://en.wikipedia.org/wiki/Data_clustering) to groups, and then map new data to these formed groups. The **support vector clustering**[[2]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-HavaSiegelmann-2) algorithm created by [Hava Siegelmann](https://en.wikipedia.org/wiki/Hava_Siegelmann) and [Vladimir Vapnik](https://en.wikipedia.org/wiki/Vladimir_Vapnik), applies the statistics of support vectors, developed in the support vector machines algorithm, to categorize unlabeled data, and is one of the most widely used clustering algorithms in industrial applications.[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*]

## Motivation[]

[![220px-Svm_separating_hyperplanes_(SVG).svg.png](../_resources/118482e2a70a238dcff1bd4461c56d3e.png)](https://en.wikipedia.org/wiki/File:Svm_separating_hyperplanes_(SVG).svg)

H1 does not separate the classes. H2 does, but only with a small margin. H3 separates them with the maximum margin.

[Classifying data](https://en.wikipedia.org/wiki/Statistical_classification) is a common task in [machine learning](https://en.wikipedia.org/wiki/Machine_learning). Suppose some given data points each belong to one of two classes, and the goal is to decide which class a *new*  [Data point](https://en.wikipedia.org/wiki/Data_point) will be in. In the case of support vector machines, a data point is viewed as a         p      {\displaystyle p}  [p](../_resources/def00db8a472d01b3571111bbc647feb.bin)-dimensional vector (a list of         p      {\displaystyle p}  [p](../_resources/def00db8a472d01b3571111bbc647feb.bin) numbers), and we want to know whether we can separate such points with a         (  p  −  1  )      {\displaystyle (p-1)}  [(p-1)](../_resources/dd6bc83e41f5cfd7e26580d4a2c1a39d.bin)-dimensional [hyperplane](https://en.wikipedia.org/wiki/Hyperplane). This is called a [linear classifier](https://en.wikipedia.org/wiki/Linear_classifier). There are many hyperplanes that might classify the data. One reasonable choice as the best hyperplane is the one that represents the largest separation, or [margin](https://en.wikipedia.org/wiki/Margin_(machine_learning)), between the two classes. So we choose the hyperplane so that the distance from it to the nearest data point on each side is maximized. If such a hyperplane exists, it is known as the *[maximum-margin hyperplane](https://en.wikipedia.org/wiki/Maximum-margin_hyperplane)* and the linear classifier it defines is known as a *maximum [margin classifier](https://en.wikipedia.org/wiki/Margin_classifier)*; or equivalently, the *[perceptron](https://en.wikipedia.org/wiki/Perceptron) of optimal stability.*[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*]

## Definition[]

More formally, a support vector machine constructs a [hyperplane](https://en.wikipedia.org/wiki/Hyperplane) or set of hyperplanes in a [high-](https://en.wikipedia.org/wiki/High-dimensional_space) or infinite-dimensional space, which can be used for [classification](https://en.wikipedia.org/wiki/Statistical_classification), [regression](https://en.wikipedia.org/wiki/Regression_analysis), or other tasks like outliers detection[[3]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-3). Intuitively, a good separation is achieved by the hyperplane that has the largest distance to the nearest training-data point of any class (so-called functional margin), since in general the larger the margin the lower the [generalization error](https://en.wikipedia.org/wiki/Generalization_error) of the classifier[[4]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-4).

[![220px-Kernel_Machine.png](../_resources/8b159caa184524caa1fa51dde48039d9.png)](https://en.wikipedia.org/wiki/File:Kernel_Machine.png)

Kernel machine

Whereas the original problem may be stated in a finite dimensional space, it often happens that the sets to discriminate are not [linearly separable](https://en.wikipedia.org/wiki/Linear_separability) in that space. For this reason, it was proposed that the original finite-dimensional space be mapped into a much higher-dimensional space, presumably making the separation easier in that space. To keep the computational load reasonable, the mappings used by SVM schemes are designed to ensure that [dot products](https://en.wikipedia.org/wiki/Dot_product) may be computed easily in terms of the variables in the original space, by defining them in terms of a [kernel function](https://en.wikipedia.org/wiki/Positive-definite_kernel)          k  (  x  ,  y  )      {\displaystyle k(x,y)}  [k(x,y)](../_resources/a65d3247a1d148bcbcb96a60f08a3b1e.bin) selected to suit the problem.[[5]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-5) The hyperplanes in the higher-dimensional space are defined as the set of points whose dot product with a vector in that space is constant. The vectors defining the hyperplanes can be chosen to be linear combinations with parameters           α    i          {\displaystyle \alpha _{i}}  [\alpha _{i}](../_resources/3f1a9a732516ae5b4b441a7266e7e277.bin) of images of [feature vectors](https://en.wikipedia.org/wiki/Feature_vector)            x    i          {\displaystyle x_{i}}  [x_{i}](../_resources/f86443c88f689b6f2a82b63f41c8198b.bin) that occur in the data base[*[clarification needed](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)*]. With this choice of a hyperplane, the points         x      {\displaystyle x}  [x](../_resources/5264e1d4d820fc4756cf77faa96a3281.bin) in the [feature space](https://en.wikipedia.org/wiki/Feature_space) that are mapped into the hyperplane are defined by the relation:             ∑    i        α    i      k  (    x    i      ,  x  )  =    c  o  n  s  t  a  n  t    .        {\displaystyle \textstyle \sum _{i}\alpha _{i}k(x_{i},x)=\mathrm {constant} .}  [\textstyle \sum _{i}\alpha _{i}k(x_{i},x)=\mathrm {constant} .](../_resources/ecc5722b28f725191aad0e44c4ee74dc.bin) Note that if         k  (  x  ,  y  )      {\displaystyle k(x,y)}  [k(x,y)](../_resources/a65d3247a1d148bcbcb96a60f08a3b1e.bin) becomes small as         y      {\displaystyle y}  [y](../_resources/94cef7fab7db862daa2ff8054cbf1f65.bin) grows further away from         x      {\displaystyle x}  [x](../_resources/5264e1d4d820fc4756cf77faa96a3281.bin), each term in the sum measures the degree of closeness of the test point         x      {\displaystyle x}  [x](../_resources/5264e1d4d820fc4756cf77faa96a3281.bin) to the corresponding data base point           x    i          {\displaystyle x_{i}}  [x_{i}](../_resources/f86443c88f689b6f2a82b63f41c8198b.bin). In this way, the sum of kernels above can be used to measure the relative nearness of each test point to the data points originating in one or the other of the sets to be discriminated. Note the fact that the set of points         x      {\displaystyle x}  [x](../_resources/5264e1d4d820fc4756cf77faa96a3281.bin) mapped into any hyperplane can be quite convoluted as a result, allowing much more complex discrimination between sets which are not convex at all in the original space.

## Applications[]

SVMs can be used to solve various real world problems:

- SVMs are helpful in [text and hypertext categorization](https://en.wikipedia.org/wiki/Text_categorization) as their application can significantly reduce the need for labeled training instances in both the standard inductive and [transductive](https://en.wikipedia.org/wiki/Transduction_(machine_learning)) settings.
- [Classification of images](https://en.wikipedia.org/wiki/Image_classification) can also be performed using SVMs. Experimental results show that SVMs achieve significantly higher search accuracy than traditional query refinement schemes after just three to four rounds of relevance feedback. This is also true of [image segmentation](https://en.wikipedia.org/wiki/Image_segmentation) systems, including those using a modified version SVM that uses the privileged approach as suggested by Vapnik.[[6]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-6)[[7]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-7)
- Hand-written characters can be [recognized](https://en.wikipedia.org/wiki/Handwriting_recognition) using SVM[[8]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-8)[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*].
- The SVM algorithm has been widely applied in the biological and other sciences. They have been used to classify proteins with up to 90% of the compounds classified correctly. [Permutation tests](https://en.wikipedia.org/wiki/Permutation_test) based on SVM weights have been suggested as a mechanism for interpretation of SVM models.[[9]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-9)[[10]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-10) Support vector machine weights have also been used to interpret SVM models in the past.[[11]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-11) Posthoc interpretation of support vector machine models in order to identify features used by the model to make predictions is a relatively new area of research with special significance in the biological sciences.

## History[]

The original SVM algorithm was invented by [Vladimir N. Vapnik](https://en.wikipedia.org/wiki/Vladimir_N._Vapnik) and [Alexey Ya. Chervonenkis](https://en.wikipedia.org/wiki/Alexey_Chervonenkis) in 1963. In 1992, Bernhard E. Boser, Isabelle M. Guyon and [Vladimir N. Vapnik](https://en.wikipedia.org/wiki/Vladimir_N._Vapnik) suggested a way to create nonlinear classifiers by applying the [kernel trick](https://en.wikipedia.org/wiki/Kernel_trick) to maximum-margin hyperplanes.[[12]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-ReferenceA-12) The current standard incarnation (soft margin) was proposed by [Corinna Cortes](https://en.wikipedia.org/wiki/Corinna_Cortes) and Vapnik in 1993 and published in 1995.[[1]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-CorinnaCortes-1)

## Linear SVM[]

We are given a training dataset of         n      {\displaystyle n}  [n](../_resources/1137f9f87cbfe058c68bc172f8e8574f.bin) points of the form

       (          x  →          1      ,    y    1      )  ,  …  ,  (          x  →          n      ,    y    n      )      {\displaystyle ({\vec {x}}_{1},y_{1}),\,\ldots ,\,({\vec {x}}_{n},y_{n})}  [({\vec {x}}_{1},y_{1}),\,\ldots ,\,({\vec {x}}_{n},y_{n})](../_resources/4227ef5690e27cdb0b1860174e794801.bin)

where the           y    i          {\displaystyle y_{i}}  [y_{i}](:/b56a800b072bfed5464ea4ea44167b7f) are either 1 or −1, each indicating the class to which the point                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\vec {x}}_{i}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) belongs. Each                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\vec {x}}_{i}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) is a         p      {\displaystyle p}  [p](../_resources/def00db8a472d01b3571111bbc647feb.bin)-dimensional [real](https://en.wikipedia.org/wiki/Real_number) vector. We want to find the "maximum-margin hyperplane" that divides the group of points                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\vec {x}}_{i}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) for which           y    i      =  1      {\displaystyle y_{i}=1}  [y_{i}=1](../_resources/30d166dfd0dadb186beec050aef37a30.bin) from the group of points for which           y    i      =  −  1      {\displaystyle y_{i}=-1}  [y_{i}=-1](../_resources/68b68722b07f80b1e00af9776c60d966.bin), which is defined so that the distance between the hyperplane and the nearest point                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\vec {x}}_{i}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) from either group is maximized.

Any [hyperplane](https://en.wikipedia.org/wiki/Hyperplane) can be written as the set of points               x  →            {\displaystyle {\vec {x}}}  [{\vec {x}}](../_resources/39bd4a8997d529a40b3560f53122b4b9.bin) satisfying

             w  →        ⋅        x  →        −  b  =  0  ,      {\displaystyle {\vec {w}}\cdot {\vec {x}}-b=0,\,}  [{\vec {w}}\cdot {\vec {x}}-b=0,\,](:/6c70bb695b212a79c61c732c5442fb6e)

[![220px-Svm_max_sep_hyperplane_with_margin.png](../_resources/25d92a53b0a7e9373d2b07e51e9a52c5.png)](https://en.wikipedia.org/wiki/File:Svm_max_sep_hyperplane_with_margin.png)

Maximum-margin hyperplane and margins for an SVM trained with samples from two classes. Samples on the margin are called the support vectors.

where               w  →            {\displaystyle {\vec {w}}}  [{\vec {w}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin) is the (not necessarily normalized) [normal vector](https://en.wikipedia.org/wiki/Normal_(geometry)) to the hyperplane. This is much like [Hesse normal form](https://en.wikipedia.org/wiki/Hesse_normal_form), except that               w  →            {\displaystyle {\vec {w}}}  [{\vec {w}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin) is not necessarily a unit vector. The parameter               b    ‖        w  →        ‖              {\displaystyle {\tfrac {b}{\|{\vec {w}}\|}}}  [{\tfrac {b}{\|{\vec {w}}\|}}](../_resources/436f9c0353265d4b3bcd21d35866dd3d.bin) determines the offset of the hyperplane from the origin along the normal vector               w  →            {\displaystyle {\vec {w}}}  [{\vec {w}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin).

### Hard-margin[]

If the training data is [linearly separable](https://en.wikipedia.org/wiki/Linearly_separable), we can select two parallel hyperplanes that separate the two classes of data, so that the distance between them is as large as possible. The region bounded by these two hyperplanes is called the "margin", and the maximum-margin hyperplane is the hyperplane that lies halfway between them. With proper dataset rescaling these hyperplanes can be described by the following equations:

             w  →        ⋅        x  →        −  b  =  1      {\displaystyle {\vec {w}}\cdot {\vec {x}}-b=1\,}  [{\vec {w}}\cdot {\vec {x}}-b=1\,](../_resources/1a8ed4b6859fca718fa31a46968e303c.bin) (anything on or above this boundary is of one class, with label 1)

and

             w  →        ⋅        x  →        −  b  =  −  1.      {\displaystyle {\vec {w}}\cdot {\vec {x}}-b=-1.\,}  [{\vec {w}}\cdot {\vec {x}}-b=-1.\,](../_resources/af6b3676f2ad2937bb01ba777ce20114.bin) (anything on or below this boundary is of the other class, with label -1)

Geometrically, the distance between these two hyperplanes is               2    ‖        w  →        ‖              {\displaystyle {\tfrac {2}{\|{\vec {w}}\|}}}  [{\tfrac {2}{\|{\vec {w}}\|}}](../_resources/8b14730086dd88ff7e2c90e7d8c0297c.bin), so to maximize the distance between the planes we want to minimize         ‖        w  →        ‖      {\displaystyle \|{\vec {w}}\|}  [\|{\vec {w}}\|](../_resources/42240a15400fea2fd8745501262c96ba.bin). The distance is computed using the [distance from a point to a plane](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_plane) equation. We also have to prevent data points from falling into the margin, we add the following constraint: for each         i      {\displaystyle i}  [i](../_resources/f95208c1fbb067a6e60d3e53c1b7b690.bin) either

             w  →        ⋅          x  →          i      −  b  ≥  1  ,      {\displaystyle {\vec {w}}\cdot {\vec {x}}_{i}-b\geq 1,}  [{\vec {w}}\cdot {\vec {x}}_{i}-b\geq 1,](../_resources/811732edbc1278b29fe469ae96f94663.bin) if           y    i      =  1      {\displaystyle y_{i}=1}  [y_{i}=1](../_resources/30d166dfd0dadb186beec050aef37a30.bin)

or

             w  →        ⋅          x  →          i      −  b  ≤  −  1  ,      {\displaystyle {\vec {w}}\cdot {\vec {x}}_{i}-b\leq -1,}  [{\vec {w}}\cdot {\vec {x}}_{i}-b\leq -1,](../_resources/7cbb9b9286772947ea89b1c37591eaae.bin) if           y    i      =  −  1.      {\displaystyle y_{i}=-1.}  [y_{i}=-1.](:/14b6564a8d7828fdb8fe89c5c547a636)

These constraints state that each data point must lie on the correct side of the margin.

This can be rewritten as:

         y    i      (        w  →        ⋅          x  →          i      −  b  )  ≥  1  ,     for all     1  ≤  i  ≤  n  .  (  1  )      {\displaystyle y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)\geq 1,\quad {\text{ for all }}1\leq i\leq n.\qquad \qquad (1)}  [y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)\geq 1,\quad {\text{ for all }}1\leq i\leq n.\qquad \qquad (1)](../_resources/cd48acf886cdf3df1551c3ea514af338.bin)

We can put this together to get the optimization problem:

"Minimize         ‖        w  →        ‖      {\displaystyle \|{\vec {w}}\|}  [\|{\vec {w}}\|](../_resources/42240a15400fea2fd8745501262c96ba.bin) subject to           y    i      (        w  →        ⋅          x  →          i      −  b  )  ≥  1  ,      {\displaystyle y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)\geq 1,}  [{\displaystyle y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)\geq 1,}](../_resources/95035c4a3db1f0f36f0cf2744a4f7a72.bin) for         i  =  1  ,  …  ,  n      {\displaystyle i=1,\,\ldots ,\,n}  [{\displaystyle i=1,\,\ldots ,\,n}](../_resources/99873347bbdb749d92072251bf9cecc6.bin)"

The               w  →            {\displaystyle {\vec {w}}}  [{\vec {w}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin) and         b      {\displaystyle b}  [b](../_resources/5ece6b0eccf795fcaf772fbc926c4991.bin) that solve this problem determine our classifier,               x  →        ↦  sgn  ⁡  (        w  →        ⋅        x  →        −  b  )      {\displaystyle {\vec {x}}\mapsto \operatorname {sgn}({\vec {w}}\cdot {\vec {x}}-b)}  [{\displaystyle {\vec {x}}\mapsto \operatorname {sgn}({\vec {w}}\cdot {\vec {x}}-b)}](../_resources/b6103433fa9a62d2420a0cfc60504868.bin).

An easy-to-see but important consequence of this geometric description is that the max-margin hyperplane is completely determined by those                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\displaystyle {\vec {x}}_{i}}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) which lie nearest to it. These                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\displaystyle {\vec {x}}_{i}}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) are called *support vectors.*

### Soft-margin[]

To extend SVM to cases in which the data are not linearly separable, we introduce the *hinge loss* function,

       max    (    0  ,  1  −    y    i      (        w  →        ⋅          x  →          i      −  b  )    )    .      {\displaystyle \max \left(0,1-y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)ight).}  [{\displaystyle \max \left(0,1-y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)ight).}](../_resources/9fc62c6b53a4b9b2f51c73f3e91e1ff8.bin)

This function is zero if the constraint in (1) is satisfied, in other words, if                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\vec {x}}_{i}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) lies on the correct side of the margin. For data on the wrong side of the margin, the function's value is proportional to the distance from the margin.

We then wish to minimize

         [        1  n        ∑    i  =  1      n      max    (    0  ,  1  −    y    i      (        w  →        ⋅          x  →          i      −  b  )    )      ]    +  λ  ‖        w  →          ‖    2      ,      {\displaystyle \left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)ight)ight]+\lambda \lVert {\vec {w}}Vert ^{2},}  [{\displaystyle \left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)ight)ight\]+\lambda \lVert {\vec {w}}Vert ^{2},}](../_resources/26c1fb021fcee7e69c13f3ce7dd5b46f.bin)

where the parameter         λ      {\displaystyle \lambda }  [\lambda ](../_resources/da360063181034a86ae0bbefc2f89af8.bin) determines the tradeoff between increasing the margin-size and ensuring that the                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\vec {x}}_{i}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) lie on the correct side of the margin. Thus, for sufficiently small values of         λ      {\displaystyle \lambda }  [\lambda ](../_resources/da360063181034a86ae0bbefc2f89af8.bin), the soft-margin SVM will behave identically to the hard-margin SVM if the input data are linearly classifiable, but will still learn if a classification rule is viable or not.

## Nonlinear classification[]

[![220px-Kernel_Machine.png](../_resources/8b159caa184524caa1fa51dde48039d9.png)](https://en.wikipedia.org/wiki/File:Kernel_Machine.png)

Kernel machine

The original maximum-margin hyperplane algorithm proposed by Vapnik in 1963 constructed a [linear classifier](https://en.wikipedia.org/wiki/Linear_classifier). However, in 1992, [Bernhard E. Boser](https://en.wikipedia.org/w/index.php?title=Bernhard_E._Boser&action=edit&redlink=1), [Isabelle M. Guyon](https://en.wikipedia.org/w/index.php?title=Isabelle_M._Guyon&action=edit&redlink=1) and [Vladimir N. Vapnik](https://en.wikipedia.org/wiki/Vladimir_N._Vapnik) suggested a way to create nonlinear classifiers by applying the [kernel trick](https://en.wikipedia.org/wiki/Kernel_trick) (originally proposed by Aizerman et al.[[13]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-13)) to maximum-margin hyperplanes.[[12]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-ReferenceA-12) The resulting algorithm is formally similar, except that every [dot product](https://en.wikipedia.org/wiki/Dot_product) is replaced by a nonlinear [kernel](https://en.wikipedia.org/wiki/Kernel_(integral_operator)) function. This allows the algorithm to fit the maximum-margin hyperplane in a transformed [feature space](https://en.wikipedia.org/wiki/Feature_space). The transformation may be nonlinear and the transformed space high dimensional; although the classifier is a hyperplane in the transformed feature space, it may be nonlinear in the original input space.

It is noteworthy that working in a higher-dimensional feature space increases the [generalization error](https://en.wikipedia.org/wiki/Generalization_error) of support vector machines, although given enough samples the algorithm still performs well.[[14]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-14)

Some common kernels include:

- [Polynomial (homogeneous)](https://en.wikipedia.org/wiki/Homogeneous_polynomial):         k  (          x    i      →        ,          x    j      →        )  =  (          x    i      →        ⋅          x    j      →          )    d          {\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=({\vec {x_{i}}}\cdot {\vec {x_{j}}})^{d}}  [{\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=({\vec {x_{i}}}\cdot {\vec {x_{j}}})^{d}}](../_resources/112e7e24831db6862c737412d4841aa8.bin)
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial_kernel) (inhomogeneous):         k  (          x    i      →        ,          x    j      →        )  =  (          x    i      →        ⋅          x    j      →        +  1    )    d          {\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=({\vec {x_{i}}}\cdot {\vec {x_{j}}}+1)^{d}}  [{\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=({\vec {x_{i}}}\cdot {\vec {x_{j}}}+1)^{d}}](../_resources/350d27d6b90043f4919ad2091c59e0ec.bin)
- Gaussian [radial basis function](https://en.wikipedia.org/wiki/Radial_basis_function_kernel):         k  (          x    i      →        ,          x    j      →        )  =  exp  ⁡  (  −  γ  ‖          x    i      →        −          x    j      →          ‖    2      )      {\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=\exp(-\gamma \|{\vec {x_{i}}}-{\vec {x_{j}}}\|^{2})}  [{\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=\exp(-\gamma \|{\vec {x_{i}}}-{\vec {x_{j}}}\|^{2})}](../_resources/2a258657a9acd6f8aeab93d19a296773.bin), for         γ  >  0      {\displaystyle \gamma >0}  ![\gamma >0](../_resources/e0991ee4b7cc8f0cc3fd3bbd51e5da70.bin). Sometimes parametrized using         γ  =  1    /      2    σ    2            {\displaystyle \gamma =1/{2\sigma ^{2}}}  [\gamma =1/{2\sigma ^{2}}](../_resources/fea46b3bd5c784f2d7bc5f8ddb0c7612.bin)
- [Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function):         k  (          x    i      →        ,          x    j      →        )  =  tanh  ⁡  (  κ          x    i      →        ⋅          x    j      →        +  c  )      {\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=\tanh(\kappa {\vec {x_{i}}}\cdot {\vec {x_{j}}}+c)}  [{\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=\tanh(\kappa {\vec {x_{i}}}\cdot {\vec {x_{j}}}+c)}](../_resources/b7c97e15364b58fb4ce1fc11ad1fa007.bin), for some (not every)         κ  >  0      {\displaystyle \kappa >0}  [\kappa >0](../_resources/43ee0d32a63fd5f23e081abd8f46d0b2.bin) and         c  <  0      {\displaystyle c<0}  [c<0](../_resources/1b294df714fbae4c781537a3a5122148.bin)

The kernel is related to the transform         φ  (          x    i      →        )      {\displaystyle \varphi ({\vec {x_{i}}})}  [{\displaystyle \varphi ({\vec {x_{i}}})}](../_resources/2f0ac28c618973114570856ffd6cf6b2.bin) by the equation         k  (          x    i      →        ,          x    j      →        )  =  φ  (          x    i      →        )  ⋅  φ  (          x    j      →        )      {\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=\varphi ({\vec {x_{i}}})\cdot \varphi ({\vec {x_{j}}})}  [{\displaystyle k({\vec {x_{i}}},{\vec {x_{j}}})=\varphi ({\vec {x_{i}}})\cdot \varphi ({\vec {x_{j}}})}](../_resources/0196e39f8138160ac13abed235c3fdb7.bin). The value **w** is also in the transformed space, with                 w  →        =    ∑    i        α    i        y    i      φ  (          x  →          i      )        {\displaystyle \textstyle {\vec {w}}=\sum _{i}\alpha _{i}y_{i}\varphi ({\vec {x}}_{i})}  [{\displaystyle \textstyle {\vec {w}}=\sum _{i}\alpha _{i}y_{i}\varphi ({\vec {x}}_{i})}](../_resources/34c93c109c72d291938849534a85ac54.bin). Dot products with **w** for classification can again be computed by the kernel trick, i.e.                 w  →        ⋅  φ  (        x  →        )  =    ∑    i        α    i        y    i      k  (          x  →          i      ,        x  →        )        {\displaystyle \textstyle {\vec {w}}\cdot \varphi ({\vec {x}})=\sum _{i}\alpha _{i}y_{i}k({\vec {x}}_{i},{\vec {x}})}  [{\displaystyle \textstyle {\vec {w}}\cdot \varphi ({\vec {x}})=\sum _{i}\alpha _{i}y_{i}k({\vec {x}}_{i},{\vec {x}})}](../_resources/6de229d9fd7065cfd7b191974b98b7cb.bin).

## Computing the SVM classifier[]

Computing the (soft-margin) SVM classifier amounts to minimizing an expression of the form

         [        1  n        ∑    i  =  1      n      max    (    0  ,  1  −    y    i      (  w  ⋅    x    i      −  b  )    )      ]    +  λ  ‖  w    ‖    2      .  (  2  )      {\displaystyle \left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)ight]+\lambda \lVert wVert ^{2}.\qquad (2)}  [{\displaystyle \left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)ight\]+\lambda \lVert wVert ^{2}.\qquad (2)}](../_resources/e5aaf0a55a46e279e836f6cd87837bdb.bin)

We focus on the soft-margin classifier since, as noted above, choosing a sufficiently small value for         λ      {\displaystyle \lambda }  [\lambda ](../_resources/da360063181034a86ae0bbefc2f89af8.bin) yields the hard-margin classifier for linearly classifiable input data. The classical approach, which involves reducing (2) to a [quadratic programming](https://en.wikipedia.org/wiki/Quadratic_programming) problem, is detailed below. Then, more recent approaches such as sub-gradient descent and coordinate descent will be discussed.

### Primal[]

Minimizing (2) can be rewritten as a constrained optimization problem with a differentiable objective function in the following way.

For each         i  ∈  {  1  ,  …  ,  n  }      {\displaystyle i\in \{1,\,\ldots ,\,n\}}  [{\displaystyle i\in \{1,\,\ldots ,\,n\}}](../_resources/2788fffc6392595a8c32e7df31babbc9.bin) we introduce a variable           ζ    i      =  max    (    0  ,  1  −    y    i      (  w  ⋅    x    i      −  b  )    )        {\displaystyle \zeta _{i}=\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)}  [{\displaystyle \zeta _{i}=\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)}](../_resources/839df7d24f6bf4f685f52b4aef32f007.bin). Note that           ζ    i          {\displaystyle \zeta _{i}}  [{\displaystyle \zeta _{i}}](../_resources/696eb3f2ba3a7a31f422f877360ea080.bin) is the smallest nonnegative number satisfying           y    i      (  w  ⋅    x    i      −  b  )  ≥  1  −    ζ    i      .      {\displaystyle y_{i}(w\cdot x_{i}-b)\geq 1-\zeta _{i}.}  [{\displaystyle y_{i}(w\cdot x_{i}-b)\geq 1-\zeta _{i}.}](../_resources/c6f6be7d887d9f485ef68b3fcbb50325.bin)

Thus we can rewrite the optimization problem as follows

         minimize         1  n        ∑    i  =  1      n        ζ    i      +  λ  ‖  w    ‖    2          {\displaystyle {\text{minimize }}{\frac {1}{n}}\sum _{i=1}^{n}\zeta _{i}+\lambda \|w\|^{2}}  [{\displaystyle {\text{minimize }}{\frac {1}{n}}\sum _{i=1}^{n}\zeta _{i}+\lambda \|w\|^{2}}](../_resources/7f77235cb482a20ae3c59fbe17269521.bin)

         subject to       y    i      (  w  ⋅    x    i      −  b  )  ≥  1  −    ζ    i         and       ζ    i      ≥  0  ,    for all     i  .      {\displaystyle {\text{subject to }}y_{i}(w\cdot x_{i}-b)\geq 1-\zeta _{i}\,{\text{ and }}\,\zeta _{i}\geq 0,\,{\text{for all }}i.}  [{\displaystyle {\text{subject to }}y_{i}(w\cdot x_{i}-b)\geq 1-\zeta _{i}\,{\text{ and }}\,\zeta _{i}\geq 0,\,{\text{for all }}i.}](../_resources/4b67601e0d0a0a12cd68fe89b9b931f2.bin)

This is called the *primal* problem.

### Dual[]

By solving for the [Lagrangian dual](https://en.wikipedia.org/wiki/Duality_(optimization)) of the above problem, one obtains the simplified problem

         maximize    f  (    c    1      …    c    n      )  =    ∑    i  =  1      n        c    i      −      1  2        ∑    i  =  1      n        ∑    j  =  1      n        y    i        c    i      (    x    i      ⋅    x    j      )    y    j        c    j      ,      {\displaystyle {\text{maximize}}\,\,f(c_{1}\ldots c_{n})=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(x_{i}\cdot x_{j})y_{j}c_{j},}  [{\displaystyle {\text{maximize}}\,\,f(c_{1}\ldots c_{n})=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(x_{i}\cdot x_{j})y_{j}c_{j},}](../_resources/f7bd4af8dd7e8653293101ab6de5e180.bin)

         subject to       ∑    i  =  1      n        c    i        y    i      =  0  ,    and     0  ≤    c    i      ≤      1    2  n  λ          for all     i  .      {\displaystyle {\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.}  [{\displaystyle {\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.}](../_resources/8b9d2172a3ad9c788731475524b758e3.bin)

This is called the *dual* problem. Since the dual maximization problem is a quadratic function of the           c    i          {\displaystyle c_{i}}  [ c_i](../_resources/d23d2bf1e05b2ad4ad5e233f80608043.bin) subject to linear constraints, it is efficiently solvable by [quadratic programming](https://en.wikipedia.org/wiki/Quadratic_programming) algorithms.

Here, the variables           c    i          {\displaystyle c_{i}}  [ c_i](../_resources/d23d2bf1e05b2ad4ad5e233f80608043.bin) are defined such that

             w  →        =    ∑    i  =  1      n        c    i        y    i              x  →          i          {\displaystyle {\vec {w}}=\sum _{i=1}^{n}c_{i}y_{i}{\vec {x}}_{i}}  [{\displaystyle {\vec {w}}=\sum _{i=1}^{n}c_{i}y_{i}{\vec {x}}_{i}}](../_resources/bf3ca914dcf9ce3f1e418fa9207f6130.bin).

Moreover,           c    i      =  0      {\displaystyle c_{i}=0}  [{\displaystyle c_{i}=0}](../_resources/4c57f4b3fc108968b245731936b0ae0d.bin) exactly when                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\displaystyle {\vec {x}}_{i}}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) lies on the correct side of the margin, and         0  <    c    i      <  (  2  n  λ    )    −  1          {\displaystyle 0<c_{i}<(2n\lambda )^{-1}}  [{\displaystyle 0<c_{i}<(2n\lambda )^{-1}}](../_resources/adc9d99c05190c306b6e7f0424d9f8c2.bin) when                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\displaystyle {\vec {x}}_{i}}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) lies on the margin's boundary. It follows that               w  →            {\displaystyle {\vec {w}}}  [{\displaystyle {\vec {w}}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin) can be written as a linear combination of the support vectors.

The offset,         b      {\displaystyle b}  [ b](../_resources/5ece6b0eccf795fcaf772fbc926c4991.bin), can be recovered by finding an                 x  →          i          {\displaystyle {\vec {x}}_{i}}  [{\displaystyle {\vec {x}}_{i}}](../_resources/fc28b6c071096f597517c71c44c46e91.bin) on the margin's boundary and solving

         y    i      (        w  →        ⋅          x  →          i      −  b  )  =  1  ⟺  b  =        w  →        ⋅          x  →          i      −    y    i      .      {\displaystyle y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)=1\iff b={\vec {w}}\cdot {\vec {x}}_{i}-y_{i}.}  [{\displaystyle y_{i}({\vec {w}}\cdot {\vec {x}}_{i}-b)=1\iff b={\vec {w}}\cdot {\vec {x}}_{i}-y_{i}.}](../_resources/1ec24a914873a099580b6ae2de127dad.bin)

(Note that           y    i      −  1      =    y    i          {\displaystyle y_{i}^{-1}=y_{i}}  [{\displaystyle y_{i}^{-1}=y_{i}}](../_resources/fe9353424eda7a6110d99accc133eb75.bin) since           y    i      =  ±  1      {\displaystyle y_{i}=\pm 1}  [{\displaystyle y_{i}=\pm 1}](../_resources/79d76ccc23e649534951e9287eea19f6.bin).)

### Kernel trick[]

[![220px-Kernel_trick_idea.svg.png](../_resources/a1ceee0a767c003e5e2273071815bef3.png)](https://en.wikipedia.org/wiki/File:Kernel_trick_idea.svg)

A training example of SVM with kernel given by φ((*a*, *b*)) = (*a*, *b*, *a*2 + *b*2).

Suppose now that we would like to learn a nonlinear classification rule which corresponds to a linear classification rule for the transformed data points         φ  (          x  →          i      )  .      {\displaystyle \varphi ({\vec {x}}_{i}).}  [{\displaystyle \varphi ({\vec {x}}_{i}).}](../_resources/757e78f08a1170f75523be97526b8467.bin) Moreover, we are given a kernel function         k      {\displaystyle k}  [ k](../_resources/025264ffae679a930e5cbadbf88d8640.bin) which satisfies         k  (          x  →          i      ,          x  →          j      )  =  φ  (          x  →          i      )  ⋅  φ  (          x  →          j      )      {\displaystyle k({\vec {x}}_{i},{\vec {x}}_{j})=\varphi ({\vec {x}}_{i})\cdot \varphi ({\vec {x}}_{j})}  [{\displaystyle k({\vec {x}}_{i},{\vec {x}}_{j})=\varphi ({\vec {x}}_{i})\cdot \varphi ({\vec {x}}_{j})}](../_resources/a9357c86121cefdf1073dcb768b0c060.bin).

We know the classification vector               w  →            {\displaystyle {\vec {w}}}  [{\displaystyle {\vec {w}}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin) in the transformed space satisfies

             w  →        =    ∑    i  =  1      n        c    i        y    i      φ  (          x  →          i      )  ,      {\displaystyle {\vec {w}}=\sum _{i=1}^{n}c_{i}y_{i}\varphi ({\vec {x}}_{i}),}  [{\displaystyle {\vec {w}}=\sum _{i=1}^{n}c_{i}y_{i}\varphi ({\vec {x}}_{i}),}](../_resources/baf173bbc90b21d6fda0f0bd8a706fb9.bin)

where the           c    i          {\displaystyle c_{i}}  [{\displaystyle c_{i}}](../_resources/d23d2bf1e05b2ad4ad5e233f80608043.bin) are obtained by solving the optimization problem

                 maximize    f  (    c    1      …    c    n      )      =    ∑    i  =  1      n        c    i      −      1  2        ∑    i  =  1      n        ∑    j  =  1      n        y    i        c    i      (  φ  (          x  →          i      )  ⋅  φ  (          x  →          j      )  )    y    j        c    j              =    ∑    i  =  1      n        c    i      −      1  2        ∑    i  =  1      n        ∑    j  =  1      n        y    i        c    i      k  (          x  →          i      ,          x  →          j      )    y    j        c    j                  {\displaystyle {\begin{aligned}{\text{maximize}}\,\,f(c_{1}\ldots c_{n})&=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(\varphi ({\vec {x}}_{i})\cdot \varphi ({\vec {x}}_{j}))y_{j}c_{j}\\&=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}k({\vec {x}}_{i},{\vec {x}}_{j})y_{j}c_{j}\\\end{aligned}}}

[{\displaystyle {\begin{aligned}{\text{maximize}}\,\,f(c_{1}\ldots c_{n})&=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(\varphi ({\vec {x}}_{i})\cdot \varphi ({\vec {x}}_{j}))y_{j}c_{j}\\&=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}k({\vec {x}}_{i},{\vec {x}}_{j})y_{j}c_{j}\\\end{aligned}}}](../_resources/c2ae93684997915bdb23feccd0a94e57.bin)

         subject to       ∑    i  =  1      n        c    i        y    i      =  0  ,    and     0  ≤    c    i      ≤      1    2  n  λ          for all     i  .      {\displaystyle {\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.}  [{\displaystyle {\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.}](../_resources/8b9d2172a3ad9c788731475524b758e3.bin)

The coefficients           c    i          {\displaystyle c_{i}}  [ c_i](../_resources/d23d2bf1e05b2ad4ad5e233f80608043.bin) can be solved for using quadratic programming, as before. Again, we can find some index         i      {\displaystyle i}  [i](../_resources/f95208c1fbb067a6e60d3e53c1b7b690.bin) such that         0  <    c    i      <  (  2  n  λ    )    −  1          {\displaystyle 0<c_{i}<(2n\lambda )^{-1}}  [{\displaystyle 0<c_{i}<(2n\lambda )^{-1}}](../_resources/adc9d99c05190c306b6e7f0424d9f8c2.bin), so that         φ  (          x  →          i      )      {\displaystyle \varphi ({\vec {x}}_{i})}  [{\displaystyle \varphi ({\vec {x}}_{i})}](../_resources/5ce961e58b4c877c7e14c08ff9327756.bin) lies on the boundary of the margin in the transformed space, and then solve

               b  =        w  →        ⋅  φ  (          x  →          i      )  −    y    i          =    [      ∑    k  =  1      n        c    k        y    k      φ  (          x  →          k      )  ⋅  φ  (          x  →          i      )    ]    −    y    i              =    [      ∑    k  =  1      n        c    k        y    k      k  (          x  →          k      ,          x  →          i      )    ]    −    y    i      .              {\displaystyle {\begin{aligned}b={\vec {w}}\cdot \varphi ({\vec {x}}_{i})-y_{i}&=\left[\sum _{k=1}^{n}c_{k}y_{k}\varphi ({\vec {x}}_{k})\cdot \varphi ({\vec {x}}_{i})ight]-y_{i}\\&=\left[\sum _{k=1}^{n}c_{k}y_{k}k({\vec {x}}_{k},{\vec {x}}_{i})ight]-y_{i}.\end{aligned}}}

[{\displaystyle {\begin{aligned}b={\vec {w}}\cdot \varphi ({\vec {x}}_{i})-y_{i}&=\left[\sum _{k=1}^{n}c_{k}y_{k}\varphi ({\vec {x}}_{k})\cdot \varphi ({\vec {x}}_{i})ight\]-y_{i}\\&=\left[\sum _{k=1}^{n}c_{k}y_{k}k({\vec {x}}_{k},{\vec {x}}_{i})ight\]-y_{i}.\end{aligned}}}](../_resources/97b9a8a7f2130b18582f004448ca3113.bin)

Finally, new points can be classified by computing

             z  →        ↦  sgn  ⁡  (        w  →        ⋅  φ  (        z  →        )  −  b  )  =  sgn  ⁡    (      [      ∑    i  =  1      n        c    i        y    i      k  (          x  →          i      ,        z  →        )    ]    −  b    )    .      {\displaystyle {\vec {z}}\mapsto \operatorname {sgn}({\vec {w}}\cdot \varphi ({\vec {z}})-b)=\operatorname {sgn} \left(\left[\sum _{i=1}^{n}c_{i}y_{i}k({\vec {x}}_{i},{\vec {z}})ight]-bight).}  [{\displaystyle {\vec {z}}\mapsto \operatorname {sgn}({\vec {w}}\cdot \varphi ({\vec {z}})-b)=\operatorname {sgn} \left(\left[\sum _{i=1}^{n}c_{i}y_{i}k({\vec {x}}_{i},{\vec {z}})ight\]-bight).}](../_resources/0ab7448d9b210c0bf288de88b119d553.bin)

### Modern methods[]

Recent algorithms for finding the SVM classifier include sub-gradient descent and coordinate descent. Both techniques have proven to offer significant advantages over the traditional approach when dealing with large, sparse datasets—sub-gradient methods are especially efficient when there are many training examples, and coordinate descent when the dimension of the feature space is high.

#### Sub-gradient descent[]

[Sub-gradient descent](https://en.wikipedia.org/wiki/Subgradient_method) algorithms for the SVM work directly with the expression

       f  (        w  →        ,  b  )  =    [        1  n        ∑    i  =  1      n      max    (    0  ,  1  −    y    i      (  w  ⋅    x    i      −  b  )    )      ]    +  λ  ‖  w    ‖    2      .      {\displaystyle f({\vec {w}},b)=\left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)ight]+\lambda \lVert wVert ^{2}.}  [{\displaystyle f({\vec {w}},b)=\left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)ight\]+\lambda \lVert wVert ^{2}.}](../_resources/5319cb30753ad862808e2ea3241208c5.bin)

Note that         f      {\displaystyle f}  [f](../_resources/3eaf1904af5b1412d36adebc0bbe7040.bin) is a [convex function](https://en.wikipedia.org/wiki/Convex_function) of               w  →            {\displaystyle {\vec {w}}}  [{\vec {w}}](../_resources/0140134ae89e70c2a184b777bb96ad38.bin) and         b      {\displaystyle b}  [b](../_resources/5ece6b0eccf795fcaf772fbc926c4991.bin). As such, traditional [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) (or [SGD](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)) methods can be adapted, where instead of taking a step in the direction of the functions gradient, a step is taken in the direction of a vector selected from the function's [sub-gradient](https://en.wikipedia.org/wiki/Subderivative). This approach has the advantage that, for certain implementations, the number of iterations does not scale with         n      {\displaystyle n}  [n](../_resources/1137f9f87cbfe058c68bc172f8e8574f.bin), the number of data points.[[15]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-15)

#### Coordinate descent[]

[Coordinate descent](https://en.wikipedia.org/wiki/Coordinate_descent) algorithms for the SVM work from the dual problem

         maximize    f  (    c    1      …    c    n      )  =    ∑    i  =  1      n        c    i      −      1  2        ∑    i  =  1      n        ∑    j  =  1      n        y    i        c    i      (    x    i      ⋅    x    j      )    y    j        c    j      ,      {\displaystyle {\text{maximize}}\,\,f(c_{1}\ldots c_{n})=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(x_{i}\cdot x_{j})y_{j}c_{j},}  [{\displaystyle {\text{maximize}}\,\,f(c_{1}\ldots c_{n})=\sum _{i=1}^{n}c_{i}-{\frac {1}{2}}\sum _{i=1}^{n}\sum _{j=1}^{n}y_{i}c_{i}(x_{i}\cdot x_{j})y_{j}c_{j},}](../_resources/f7bd4af8dd7e8653293101ab6de5e180.bin)

         subject to       ∑    i  =  1      n        c    i        y    i      =  0  ,    and     0  ≤    c    i      ≤      1    2  n  λ          for all     i  .      {\displaystyle {\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.}  [{\displaystyle {\text{subject to }}\sum _{i=1}^{n}c_{i}y_{i}=0,\,{\text{and }}0\leq c_{i}\leq {\frac {1}{2n\lambda }}\;{\text{for all }}i.}](../_resources/8b9d2172a3ad9c788731475524b758e3.bin)

For each         i  ∈  {  1  ,  …  ,  n  }      {\displaystyle i\in \{1,\,\ldots ,\,n\}}  [{\displaystyle i\in \{1,\,\ldots ,\,n\}}](../_resources/2788fffc6392595a8c32e7df31babbc9.bin), iteratively, the coefficient           c    i          {\displaystyle c_{i}}  [ c_i](../_resources/d23d2bf1e05b2ad4ad5e233f80608043.bin) is adjusted in the direction of         ∂  f    /    ∂    c    i          {\displaystyle \partial f/\partial c_{i}}  [{\displaystyle \partial f/\partial c_{i}}](../_resources/b136a8eff90431268f265f3cf2797168.bin). Then, the resulting vector of coefficients         (    c    1    ′    ,  …  ,    c    n    ′    )      {\displaystyle (c_{1}',\,\ldots ,\,c_{n}')}  [{\displaystyle (c_{1}',\,\ldots ,\,c_{n}')}](../_resources/12e2f926f7300a629c39eac89fd874b5.bin) is projected onto the nearest vector of coefficients that satisfies the given constraints. (Typically Euclidean distances are used.) The process is then repeated until a near-optimal vector of coefficients is obtained. The resulting algorithm is extremely fast in practice, although few performance guarantees have been proven.[[16]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-16)

## Empirical risk minimization[]

The soft-margin support vector machine described above is an example of an [empirical risk minimization](https://en.wikipedia.org/wiki/Empirical_risk_minimization) (ERM) algorithm for the *[hinge loss](https://en.wikipedia.org/wiki/Hinge_loss)*. Seen this way, support vector machines belong to a natural class of algorithms for statistical inference, and many of its unique features are due to the behavior of the hinge loss. This perspective can provide further insight into how and why SVMs work, and allow us to better analyze their statistical properties.

### Risk minimization[]

In supervised learning, one is given a set of training examples           X    1      …    X    n          {\displaystyle X_{1}\ldots X_{n}}  [X_{1}\ldots X_{n}](../_resources/92cc8ea83ab33c48c789120e8121ced5.bin) with labels           y    1      …    y    n          {\displaystyle y_{1}\ldots y_{n}}  [y_{1}\ldots y_{n}](../_resources/dc7ec8382f985c729f013b7c8587bf9f.bin), and wishes to predict           y    n  +  1          {\displaystyle y_{n+1}}  [y_{n+1}](../_resources/adf52eb20d1e9e67ddcac5758804e88c.bin) given           X    n  +  1          {\displaystyle X_{n+1}}  [X_{{n+1}}](../_resources/e70c8d7db2e6b77ef20118cf67f0dfea.bin). To do so one forms a [hypothesis](https://en.wikipedia.org/wiki/Hypothesis),         f      {\displaystyle f}  [f](../_resources/3eaf1904af5b1412d36adebc0bbe7040.bin), such that         f  (    X    n  +  1      )      {\displaystyle f(X_{n+1})}  [{\displaystyle f(X_{n+1})}](../_resources/e6c8b0174031abce31ae9e1002df08e2.bin) is a "good" approximation of           y    n  +  1          {\displaystyle y_{n+1}}  [y_{n+1}](../_resources/adf52eb20d1e9e67ddcac5758804e88c.bin). A "good" approximation is usually defined with the help of a *[loss function](https://en.wikipedia.org/wiki/Loss_function),*          ℓ  (  y  ,  z  )      {\displaystyle \ell (y,z)}  [\ell (y,z)](../_resources/3c968c1adbf81b741c06493ba025ff78.bin), which characterizes how bad         z      {\displaystyle z}   is as a prediction of         y      {\displaystyle y}  . We would then like to choose a hypothesis that minimizes the *[expected risk](https://en.wikipedia.org/wiki/Loss_function#Expected_loss):*

       ε  (  f  )  =    E      [    ℓ  (    y    n  +  1      ,  f  (    X    n  +  1      )  )    ]    .      {\displaystyle \varepsilon (f)=\mathbb {E} \left[\ell (y_{n+1},f(X_{n+1}))ight].}

In most cases, we don't know the joint distribution of           X    n  +  1      ,    y    n  +  1          {\displaystyle X_{n+1},\,y_{n+1}}   outright. In these cases, a common strategy is to choose the hypothesis that minimizes the *empirical risk:*

             ε  ^        (  f  )  =      1  n        ∑    k  =  1      n      ℓ  (    y    k      ,  f  (    X    k      )  )  .      {\displaystyle {\hat {\varepsilon }}(f)={\frac {1}{n}}\sum _{k=1}^{n}\ell (y_{k},f(X_{k})).}

Under certain assumptions about the sequence of random variables           X    k      ,    y    k          {\displaystyle X_{k},\,y_{k}}   (for example, that they are generated by a finite Markov process), if the set of hypotheses being considered is small enough, the minimizer of the empirical risk will closely approximate the minimizer of the expected risk as         n      {\displaystyle n}   grows large. This approach is called *empirical risk minimization,* or ERM.

### Regularization and stability[]

In order for the minimization problem to have a well-defined solution, we have to place constraints on the set             H          {\displaystyle {\mathcal {H}}}   of hypotheses being considered. If             H          {\displaystyle {\mathcal {H}}}   is a [normed space](https://en.wikipedia.org/wiki/Normed_vector_space) (as is the case for SVM), a particularly effective technique is to consider only those hypotheses         f      {\displaystyle f}   for which         ‖  f    ‖      H        <  k      {\displaystyle \lVert fVert _{\mathcal {H}}<k}   . This is equivalent to imposing a *regularization penalty*              R      (  f  )  =    λ    k      ‖  f    ‖      H            {\displaystyle {\mathcal {R}}(f)=\lambda _{k}\lVert fVert _{\mathcal {H}}}  , and solving the new optimization problem

             f  ^        =    a  r  g      min    f  ∈      H                ε  ^        (  f  )  +      R      (  f  )  .      {\displaystyle {\hat {f}}=\mathrm {arg} \min _{f\in {\mathcal {H}}}{\hat {\varepsilon }}(f)+{\mathcal {R}}(f).}

This approach is called *[Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization).*

More generally,             R      (  f  )      {\displaystyle {\mathcal {R}}(f)}   can be some measure of the complexity of the hypothesis         f      {\displaystyle f}  , so that simpler hypotheses are preferred.

### SVM and the hinge loss[]

Recall that the (soft-margin) SVM classifier               w  ^        ,  b  :  x  ↦  sgn  ⁡  (        w  ^        ⋅  x  −  b  )      {\displaystyle {\hat {w}},b:x\mapsto \operatorname {sgn}({\hat {w}}\cdot x-b)}   is chosen to minimize the following expression:

         [        1  n        ∑    i  =  1      n      max    (    0  ,  1  −    y    i      (  w  ⋅    x    i      −  b  )    )      ]    +  λ  ‖  w    ‖    2      .      {\displaystyle \left[{\frac {1}{n}}\sum _{i=1}^{n}\max \left(0,1-y_{i}(w\cdot x_{i}-b)ight)ight]+\lambda \lVert wVert ^{2}.}

In light of the above discussion, we see that the SVM technique is equivalent to empirical risk minimization with Tikhonov regularization, where in this case the loss function is the hinge loss

       ℓ  (  y  ,  z  )  =  max    (    0  ,  1  −  y  z    )    .      {\displaystyle \ell (y,z)=\max \left(0,1-yzight).}

From this perspective, SVM is closely related to other fundamental classification algorithms such as [regularized least-squares](https://en.wikipedia.org/wiki/Regularized_least-squares) and [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression). The difference between the three lies in the choice of loss function: regularized least-squares amounts to empirical risk minimization with the [square-loss](https://en.wikipedia.org/wiki/Loss_functions_for_classification),           ℓ    s  q      (  y  ,  z  )  =  (  y  −  z    )    2          {\displaystyle \ell _{sq}(y,z)=(y-z)^{2}}  ; logistic regression employs the [log-loss](https://en.wikipedia.org/wiki/Loss_functions_for_classification),

         ℓ    log      (  y  ,  z  )  =  ln  ⁡  (  1  +    e    −  y  z      )  .      {\displaystyle \ell _{\log }(y,z)=\ln(1+e^{-yz}).}

#### Target functions[]

The difference between the hinge loss and these other loss functions is best stated in terms of *target functions -* the function that minimizes expected risk for a given pair of random variables         X  ,  y      {\displaystyle X,\,y}  .

In particular, let           y    x          {\displaystyle y_{x}}   denote         y      {\displaystyle y}   conditional on the event that         X  =  x      {\displaystyle X=x}  . In the classification setting, we have:

         y    x      =      {        1        with probability       p    x              −  1        with probability     1  −    p    x                    {\displaystyle y_{x}={\begin{cases}1&{\text{with probability }}p_{x}\\-1&{\text{with probability }}1-p_{x}\end{cases}}}

The optimal classifier is therefore:

         f    ∗      (  x  )  =      {        1        if       p    x      ≥  1    /    2          −  1        otherwise                  {\displaystyle f^{*}(x)={\begin{cases}1&{\text{if }}p_{x}\geq 1/2\\-1&{\text{otherwise}}\end{cases}}}

For the square-loss, the target function is the conditional expectation function,           f    s  q      (  x  )  =    E      [    y    x      ]        {\displaystyle f_{sq}(x)=\mathbb {E} \left[y_{x}ight]}  ; For the logistic loss, it's the logit function,           f    log      (  x  )  =  ln  ⁡    (      p    x        /    (    1  −    p    x        )    )        {\displaystyle f_{\log }(x)=\ln \left(p_{x}/({1-p_{x}})ight)}  . While both of these target functions yield the correct classifier, as         sgn  ⁡  (    f    s  q      )  =  sgn  ⁡  (    f    log      )  =    f    ∗          {\displaystyle \operatorname {sgn}(f_{sq})=\operatorname {sgn}(f_{\log })=f^{*}}  , they give us more information than we need. In fact, they give us enough information to completely describe the distribution of           y    x          {\displaystyle y_{x}}  .

On the other hand, one can check that the target function for the hinge loss is *exactly*            f    ∗          {\displaystyle f^{*}}  . Thus, in a sufficiently rich hypothesis space—or equivalently, for an appropriately chosen kernel—the SVM classifier will converge to the simplest function (in terms of             R          {\displaystyle {\mathcal {R}}}  ) that correctly classifies the data. This extends the geometric interpretation of SVM—for linear classification, the empirical risk is minimized by any function whose margins lie between the support vectors, and the simplest of these is the max-margin classifier.[[17]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-17)

## Properties[]

SVMs belong to a family of generalized [linear classifiers](https://en.wikipedia.org/wiki/Linear_classifier) and can be interpreted as an extension of the [perceptron](https://en.wikipedia.org/wiki/Perceptron). They can also be considered a special case of [Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization). A special property is that they simultaneously minimize the empirical *classification error* and maximize the *geometric margin*; hence they are also known as **maximum [margin classifiers](https://en.wikipedia.org/wiki/Margin_classifier)**.

A comparison of the SVM to other classifiers has been made by Meyer, Leisch and Hornik.[[18]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-18)

### Parameter selection[]

The effectiveness of SVM depends on the selection of kernel, the kernel's parameters, and soft margin parameter C. A common choice is a Gaussian kernel, which has a single parameter *        γ      {\displaystyle \gamma }  *. The best combination of *C* and         γ      {\displaystyle \gamma }   is often selected by a [grid search](https://en.wikipedia.org/wiki/Grid_search) with exponentially growing sequences of *C* and *        γ      {\displaystyle \gamma }  *, for example,         C  ∈  {    2    −  5      ,    2    −  3      ,  …  ,    2    13      ,    2    15      }      {\displaystyle C\in \{2^{-5},2^{-3},\dots ,2^{13},2^{15}\}}  ;         γ  ∈  {    2    −  15      ,    2    −  13      ,  …  ,    2    1      ,    2    3      }      {\displaystyle \gamma \in \{2^{-15},2^{-13},\dots ,2^{1},2^{3}\}}  . Typically, each combination of parameter choices is checked using [cross validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)), and the parameters with best cross-validation accuracy are picked. Alternatively, recent work in [Bayesian optimization](https://en.wikipedia.org/wiki/Bayesian_optimization) can be used to select *C* and *        γ      {\displaystyle \gamma }  * , often requiring the evaluation of far fewer parameter combinations than grid search. The final model, which is used for testing and for classifying new data, is then trained on the whole training set using the selected parameters.[[19]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-19)

### Issues[]

Potential drawbacks of the SVM include the following aspects:

- Requires full labeling of input data
- Uncalibrated [class membership probabilities](https://en.wikipedia.org/wiki/Class_membership_probabilities) -- SVM stems from Vapnik's theory which avoids estimating probabilities on finite data
- The SVM is only directly applicable for two-class tasks. Therefore, algorithms that reduce the multi-class task to several binary problems have to be applied; see the [multi-class SVM](https://en.wikipedia.org/wiki/Support_vector_machine#Multiclass_SVM) section.
- Parameters of a solved model are difficult to interpret.

## Extensions[]

### Support vector clustering (SVC)[]

SVC is a similar method that also builds on kernel functions but is appropriate for unsupervised learning and data-mining. It is considered a fundamental method in [data science](https://en.wikipedia.org/wiki/Data_science).[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*]

### Multiclass SVM[]

Multiclass SVM aims to assign labels to instances by using support vector machines, where the labels are drawn from a finite set of several elements.

The dominant approach for doing so is to reduce the single [multiclass problem](https://en.wikipedia.org/wiki/Multiclass_problem) into multiple [binary classification](https://en.wikipedia.org/wiki/Binary_classification) problems.[[20]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-duan2005-20) Common methods for such reduction include:[[20]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-duan2005-20)[[21]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-hsu2002-21)

- Building binary classifiers which distinguish (i) between one of the labels and the rest (*one-versus-all*) or (ii) between every pair of classes (*one-versus-one*). Classification of new instances for the one-versus-all case is done by a winner-takes-all strategy, in which the classifier with the highest output function assigns the class (it is important that the output functions be calibrated to produce comparable scores). For the one-versus-one approach, classification is done by a max-wins voting strategy, in which every classifier assigns the instance to one of the two classes, then the vote for the assigned class is increased by one vote, and finally the class with the most votes determines the instance classification.
- [Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) SVM (DAGSVM)[[22]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-22)
- [Error-correcting output codes](https://en.wikipedia.org/wiki/Error_correcting_code)[[23]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-23)

Crammer and Singer proposed a multiclass SVM method which casts the multiclass classification problem into a single optimization problem, rather than decomposing it into multiple binary classification problems.[[24]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-24) See also Lee, Lin and Wahba.[[25]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-25)[[26]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-26)

### Transductive support vector machines[]

Transductive support vector machines extend SVMs in that they could also treat partially labeled data in [semi-supervised learning](https://en.wikipedia.org/wiki/Semi-supervised_learning) by following the principles of [transduction](https://en.wikipedia.org/wiki/Transduction_(machine_learning)). Here, in addition to the training set             D          {\displaystyle {\mathcal {D}}}  , the learner is also given a set

             D        ⋆      =  {          x  →          i      ⋆      ∣          x  →          i      ⋆      ∈      R      p        }    i  =  1      k          {\displaystyle {\mathcal {D}}^{\star }=\{{\vec {x}}_{i}^{\star }\mid {\vec {x}}_{i}^{\star }\in \mathbb {R} ^{p}\}_{i=1}^{k}\,}

of test examples to be classified. Formally, a transductive support vector machine is defined by the following primal optimization problem:[[27]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-27)

Minimize (in                 w  →        ,  b  ,          y    ⋆      →              {\displaystyle {{\vec {w}},b,{\vec {y^{\star }}}}}  )

           1  2      ‖        w  →          ‖    2          {\displaystyle {\frac {1}{2}}\|{\vec {w}}\|^{2}}

subject to (for any         i  =  1  ,  …  ,  n      {\displaystyle i=1,\dots ,n}   and any         j  =  1  ,  …  ,  k      {\displaystyle j=1,\dots ,k}  )

         y    i      (        w  →        ⋅          x    i      →        −  b  )  ≥  1  ,      {\displaystyle y_{i}({\vec {w}}\cdot {\vec {x_{i}}}-b)\geq 1,\,}

         y    j      ⋆      (        w  →        ⋅          x    j      ⋆      →        −  b  )  ≥  1  ,      {\displaystyle y_{j}^{\star }({\vec {w}}\cdot {\vec {x_{j}^{\star }}}-b)\geq 1,}

and

         y    j      ⋆      ∈  {  −  1  ,  1  }  .      {\displaystyle y_{j}^{\star }\in \{-1,1\}.\,}

Transductive support vector machines were introduced by Vladimir N. Vapnik in 1998.

### Structured SVM[]

SVMs have been generalized to [structured SVMs](https://en.wikipedia.org/wiki/Structured_SVM), where the label space is structured and of possibly infinite size.

### Regression[]

[![220px-Svr_epsilons_demo.svg.png](../_resources/103f1129083e3556877e354cb4de32d8.png)](https://en.wikipedia.org/wiki/File:Svr_epsilons_demo.svg)

Support Vector Regression (prediction) with different thresholds *ε*. As *ε* increases, the prediction becomes less sensitive to errors.

A version of SVM for [regression](https://en.wikipedia.org/wiki/Regression_analysis) was proposed in 1996 by [Vladimir N. Vapnik](https://en.wikipedia.org/wiki/Vladimir_N._Vapnik), Harris Drucker, Christopher J. C. Burges, Linda Kaufman and Alexander J. Smola.[[28]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-28) This method is called support vector regression (SVR). The model produced by support vector classification (as described above) depends only on a subset of the training data, because the cost function for building the model does not care about training points that lie beyond the margin. Analogously, the model produced by SVR depends only on a subset of the training data, because the cost function for building the model ignores any training data close to the model prediction. Another SVM version known as [least squares support vector machine](https://en.wikipedia.org/wiki/Least_squares_support_vector_machine) (LS-SVM) has been proposed by Suykens and Vandewalle.[[29]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-29)

Training the original SVR means solving[[30]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-30)

minimize             1  2      ‖  w    ‖    2          {\displaystyle {\frac {1}{2}}\|w\|^{2}}

subject to             {          y    i      −  ⟨  w  ,    x    i      ⟩  −  b  ≤  ε          ⟨  w  ,    x    i      ⟩  +  b  −    y    i      ≤  ε                {\displaystyle {\begin{cases}y_{i}-\langle w,x_{i}angle -b\leq \varepsilon \\\langle w,x_{i}angle +b-y_{i}\leq \varepsilon \end{cases}}}

where           x    i          {\displaystyle x_{i}}   is a training sample with target value           y    i          {\displaystyle y_{i}}  . The inner product plus intercept         ⟨  w  ,    x    i      ⟩  +  b      {\displaystyle \langle w,x_{i}angle +b}   is the prediction for that sample, and         ε      {\displaystyle \varepsilon }   is a free parameter that serves as a threshold: all predictions have to be within an         ε      {\displaystyle \varepsilon }   range of the true predictions. Slack variables are usually added into the above to allow for errors and to allow approximation in the case the above problem is infeasible.

### Bayesian SVM[]

In 2011 it was shown by Polson and Scott that the SVM admits a [Bayesian](https://en.wikipedia.org/wiki/Bayesian_probability) interpretation through the technique of [data augmentation](https://en.wikipedia.org/wiki/Data_augmentation)[[31]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-31). In this approach the SVM is viewed as a [graphical model](https://en.wikipedia.org/wiki/Graphical_model) (where the parameters are connected via probability distributions). This extended view allows for the application of [Bayesian](https://en.wikipedia.org/wiki/Bayesian_probability) techniques to SVMs, such as flexible feature modeling, automatic [hyperparameter](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)) tuning, and [predictive uncertainty quantification](https://en.wikipedia.org/wiki/Posterior_predictive_distribution). Recently, a scalable version of the Bayesian SVM was developed by Wenzel et al. enabling the application of Bayesian SVMs to [big data](https://en.wikipedia.org/wiki/Big_data)[[32]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-32).

## Implementation[]

The parameters of the maximum-margin hyperplane are derived by solving the optimization. There exist several specialized algorithms for quickly solving the [QP](https://en.wikipedia.org/wiki/Quadratic_programming) problem that arises from SVMs, mostly relying on heuristics for breaking the problem down into smaller, more-manageable chunks.

Another approach is to use an [interior point method](https://en.wikipedia.org/wiki/Interior_point_method) that uses [Newton](https://en.wikipedia.org/wiki/Newton%27s_method)-like iterations to find a solution of the [Karush–Kuhn–Tucker conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions) of the primal and dual problems.[[33]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-33) Instead of solving a sequence of broken down problems, this approach directly solves the problem altogether. To avoid solving a linear system involving the large kernel matrix, a low rank approximation to the matrix is often used in the kernel trick.

Another common method is Platt's [sequential minimal optimization](https://en.wikipedia.org/wiki/Sequential_minimal_optimization) (SMO) algorithm, which breaks the problem down into 2-dimensional sub-problems that are solved analytically, eliminating the need for a numerical optimization algorithm and matrix storage. This algorithm is conceptually simple, easy to implement, generally faster, and has better scaling properties for difficult SVM problems.[[34]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-34)

The special case of linear support vector machines can be solved more efficiently by the same kind of algorithms used to optimize its close cousin, [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression); this class of algorithms includes [sub-gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (e.g., PEGASOS[[35]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-35)) and [coordinate descent](https://en.wikipedia.org/wiki/Coordinate_descent) (e.g., LIBLINEAR[[36]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-36)). LIBLINEAR has some attractive training time properties. Each convergence iteration takes time linear in the time taken to read the train data and the iterations also have a [Q-Linear Convergence](https://en.wikipedia.org/wiki/Rate_of_convergence) property, making the algorithm extremely fast.

The general kernel SVMs can also be solved more efficiently using [sub-gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (e.g. P-packSVM[[37]](https://en.wikipedia.org/wiki/Support_vector_machine#cite_note-37)), especially when [parallelization](https://en.wikipedia.org/wiki/Parallelization) is allowed.

Kernel SVMs are available in many machine learning toolkits, including [LIBSVM](https://en.wikipedia.org/wiki/LIBSVM), [MATLAB](https://en.wikipedia.org/wiki/MATLAB), [SAS](http://support.sas.com/documentation/cdl/en/whatsnew/64209/HTML/default/viewer.htm#emdocwhatsnew71.htm), SVMlight, [kernlab](https://cran.r-project.org/package=kernlab), [scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn), [Shogun](https://en.wikipedia.org/wiki/Shogun_(toolbox)), [Weka](https://en.wikipedia.org/wiki/Weka_(machine_learning)), [Shark](http://image.diku.dk/shark/), [JKernelMachines](https://mloss.org/software/view/409/), [OpenCV](https://en.wikipedia.org/wiki/OpenCV) and others.

## See also[]

## References[]

1. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-CorinnaCortes_1-0)  [***b***](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-CorinnaCortes_1-1)  [Cortes, Corinna](https://en.wikipedia.org/wiki/Corinna_Cortes); Vapnik, Vladimir N. (1995). "Support-vector networks". *[Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal))*. **20** (3): 273–297. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/BF00994018](https://doi.org/10.1007%2FBF00994018).

2. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-HavaSiegelmann_2-0)** Ben-Hur, Asa; Horn, David; Siegelmann, Hava; and Vapnik, Vladimir N.; "Support vector clustering"; (2001); *Journal of Machine Learning Research*, 2: 125–137

3. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-3)**  ["Archived copy"](http://scikit-learn.org/stable/modules/svm.html). [Archived](https://web.archive.org/web/20171108151644/http://scikit-learn.org/stable/modules/svm.html) from the original on 2017-11-08. Retrieved 2017-11-08.

4. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-4)** Trevor_Hastie,_Robert_Tibshirani,_Jerome_Friedman - The elements of Statistical Learning Pg. 134

5. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-5)** *Press, William H.; Teukolsky, Saul A.; Vetterling, William T.; Flannery, Brian P. (2007). ["Section 16.5. Support Vector Machines"](http://apps.nrbook.com/empanel/index.html#pg=883). *Numerical Recipes: The Art of Scientific Computing* (3rd ed.). New York: Cambridge University Press. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-521-88068-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-88068-8). [Archived](https://web.archive.org/web/20110811154417/http://apps.nrbook.com/empanel/index.html#pg=883) from the original on 2011-08-11.

6. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-6)** Vapnik, Vladimir N.: Invited Speaker. IPMU Information Processing and Management 2014)

7. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-7)** Barghout, Lauren. "[Spatial-Taxon Information Granules as Used in Iterative Fuzzy-Decision-Making for Image Segmentation](https://pdfs.semanticscholar.org/917f/15d33d32062bffeb6401eee9fe71d16d6a84.pdf)." Granular Computing and Decision-Making. Springer International Publishing, 2015. 285-318.

8. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-8)**  DeCoste, Dennis (2002). ["Training Invariant Support Vector Machines"](https://people.eecs.berkeley.edu/~malik/cs294/decoste-scholkopf.pdf) (PDF). *Machine Learning*. **46**: 161–190.

9. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-9)** Gaonkar, Bilwaj; Davatzikos, Christos; ["Analytic estimation of statistical significance maps for support vector machine based multi-variate image analysis and classification"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3767485/)

10. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-10)** Cuingnet, Rémi; Rosso, Charlotte; Chupin, Marie; Lehéricy, Stéphane; Dormont, Didier; Benali, Habib; Samson, Yves; and Colliot, Olivier; ["Spatial regularization of SVM for the detection of diffusion alterations associated with stroke outcome"](http://www.aramislab.fr/perso/colliot/files/media2011_remi_published.pdf), *Medical Image Analysis*, 2011, 15 (5): 729–737

11. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-11)** Statnikov, Alexander; Hardin, Douglas; & Aliferis, Constantin; (2006); ["Using SVM weight-based methods to identify causally relevant and non-causally relevant variables"](http://www.ccdlab.org/paper-pdfs/NIPS_2006.pdf), *Sign*, 1, 4

12. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-ReferenceA_12-0)  [***b***](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-ReferenceA_12-1)  Boser, Bernhard E.; Guyon, Isabelle M.; Vapnik, Vladimir N. (1992). "A training algorithm for optimal margin classifiers". *Proceedings of the fifth annual workshop on Computational learning theory – COLT '92*. p. 144. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1145/130385.130401](https://doi.org/10.1145%2F130385.130401). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [089791497X](https://en.wikipedia.org/wiki/Special:BookSources/089791497X).

13. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-13)**  Aizerman, Mark A.; Braverman, Emmanuel M. & Rozonoer, Lev I. (1964). "Theoretical foundations of the potential function method in pattern recognition learning". *Automation and Remote Control*. **25**: 821–837.

14. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-14)**  Jin, Chi; Wang, Liwei (2012). [*Dimensionality dependent PAC-Bayes margin bound*](http://papers.nips.cc/paper/4500-dimensionality-dependent-pac-bayes-margin-bound). Advances in Neural Information Processing Systems. [Archived](https://web.archive.org/web/20150402185336/http://papers.nips.cc/paper/4500-dimensionality-dependent-pac-bayes-margin-bound) from the original on 2015-04-02.

15. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-15)**  Shalev-Shwartz, Shai; Singer, Yoram; Srebro, Nathan; Cotter, Andrew (2010-10-16). ["Pegasos: primal estimated sub-gradient solver for SVM"](https://link.springer.com/article/10.1007/s10107-010-0420-4). *Mathematical Programming*. **127** (1): 3–30. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/s10107-010-0420-4](https://doi.org/10.1007%2Fs10107-010-0420-4). [ISSN](https://en.wikipedia.org/wiki/International_Standard_Serial_Number) [0025-5610](https://www.worldcat.org/issn/0025-5610).

16. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-16)**  Hsieh, Cho-Jui; Chang, Kai-Wei; Lin, Chih-Jen; Keerthi, S. Sathiya; Sundararajan, S. (2008-01-01). ["A Dual Coordinate Descent Method for Large-scale Linear SVM"](http://doi.acm.org/10.1145/1390156.1390208). *Proceedings of the 25th International Conference on Machine Learning*. ICML '08. New York, NY, USA: ACM: 408–415. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1145/1390156.1390208](https://doi.org/10.1145%2F1390156.1390208). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-1-60558-205-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-60558-205-4).

17. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-17)**  Rosasco, Lorenzo; De Vito, Ernesto; Caponnetto, Andrea; Piana, Michele; Verri, Alessandro (2004-05-01). ["Are Loss Functions All the Same?"](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=6789841&abstractAccess=no&userType=inst). *Neural Computation*. **16** (5): 1063–1076. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1162/089976604773135104](https://doi.org/10.1162%2F089976604773135104). [ISSN](https://en.wikipedia.org/wiki/International_Standard_Serial_Number) [0899-7667](https://www.worldcat.org/issn/0899-7667). [PMID](https://en.wikipedia.org/wiki/PubMed_Identifier) [15070510](https://www.ncbi.nlm.nih.gov/pubmed/15070510).

18. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-18)**  Meyer, David; Leisch, Friedrich; Hornik, Kurt (2003). "The support vector machine under test". *Neurocomputing*. **55**: 169. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1016/S0925-2312(03)00431-4](https://doi.org/10.1016%2FS0925-2312%2803%2900431-4).

19. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-19)**  Hsu, Chih-Wei; Chang, Chih-Chung & Lin, Chih-Jen (2003). [*A Practical Guide to Support Vector Classification*](http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf) (PDF) (Technical report). Department of Computer Science and Information Engineering, National Taiwan University. [Archived](https://web.archive.org/web/20130625201224/http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf) (PDF) from the original on 2013-06-25.

20. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-duan2005_20-0)  [***b***](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-duan2005_20-1)  Duan, Kai-Bo; Keerthi, S. Sathiya (2005). "Which Is the Best Multiclass SVM Method? An Empirical Study". *Multiple Classifier Systems*. [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science). **3541**. pp. 278–285. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1007/11494683_28](https://doi.org/10.1007%2F11494683_28). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-3-540-26306-7](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-26306-7).

21. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-hsu2002_21-0)**  Hsu, Chih-Wei & Lin, Chih-Jen (2002). ["A Comparison of Methods for Multiclass Support Vector Machines"](http://www.cs.iastate.edu/~honavar/multiclass-svm.pdf) (PDF). *IEEE Transactions on Neural Networks*.

22. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-22)**  Platt, John; [Cristianini, Nello](https://en.wikipedia.org/wiki/Nello_Cristianini); [Shawe-Taylor, John](https://en.wikipedia.org/wiki/John_Shawe-Taylor) (2000). "Large margin DAGs for multiclass classification". In Solla, Sara A.; Leen, Todd K.; and Müller, Klaus-Robert; eds. [*Advances in Neural Information Processing Systems*](http://www.wisdom.weizmann.ac.il/~bagon/CVspring07/files/DAGSVM.pdf) (PDF). MIT Press. pp. 547–553. [Archived](https://web.archive.org/web/20120616221540/http://www.wisdom.weizmann.ac.il/~bagon/CVspring07/files/DAGSVM.pdf) (PDF) from the original on 2012-06-16.CS1 maint: Uses editors parameter ([link](https://en.wikipedia.org/wiki/Category:CS1_maint:_Uses_editors_parameter))

23. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-23)**  Dietterich, Thomas G.; Bakiri, Ghulum (1995). ["Solving Multiclass Learning Problems via Error-Correcting Output Codes"](http://www.jair.org/media/105/live-105-1426-jair.pdf) (PDF). *Journal of Artificial Intelligence Research*. **2**: 263–286. [arXiv](https://en.wikipedia.org/wiki/ArXiv):[cs/9501101](https://arxiv.org/abs/cs/9501101) . [Bibcode](https://en.wikipedia.org/wiki/Bibcode):[1995cs........1101D](http://adsabs.harvard.edu/abs/1995cs........1101D). [Archived](https://web.archive.org/web/20130509061344/http://www.jair.org/media/105/live-105-1426-jair.pdf) (PDF) from the original on 2013-05-09.

24. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-24)**  Crammer, Koby & Singer, Yoram (2001). ["On the Algorithmic Implementation of Multiclass Kernel-based Vector Machines"](http://jmlr.csail.mit.edu/papers/volume2/crammer01a/crammer01a.pdf) (PDF). *Journal of Machine Learning Research*. **2**: 265–292. [Archived](https://web.archive.org/web/20150829102651/http://jmlr.csail.mit.edu/papers/volume2/crammer01a/crammer01a.pdf) (PDF) from the original on 2015-08-29.

25. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-25)**  Lee, Yoonkyung; Lin, Yi & Wahba, Grace (2001). ["Multicategory Support Vector Machines"](http://www.interfacesymposia.org/I01/I2001Proceedings/YLee/YLee.pdf) (PDF). *Computing Science and Statistics*. **33**. [Archived](https://web.archive.org/web/20130617093314/http://www.interfacesymposia.org/I01/I2001Proceedings/YLee/YLee.pdf) (PDF) from the original on 2013-06-17.

26. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-26)**  Lee, Yoonkyung; Lin, Yi; Wahba, Grace (2004). "Multicategory Support Vector Machines". *Journal of the American Statistical Association*. **99** (465): 67. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1198/016214504000000098](https://doi.org/10.1198%2F016214504000000098).

27. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-27)** Joachims, Thorsten; "[Transductive Inference for Text Classification using Support Vector Machines](http://www1.cs.columbia.edu/~dplewis/candidacy/joachims99transductive.pdf)", *Proceedings of the 1999 International Conference on Machine Learning (ICML 1999)*, pp. 200–209

28. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-28)** Drucker, Harris; Burges, Christopher J. C.; Kaufman, Linda; Smola, Alexander J.; and Vapnik, Vladimir N. (1997); "[Support Vector Regression Machines](http://papers.nips.cc/paper/1238-support-vector-regression-machines.pdf)", in *Advances in Neural Information Processing Systems 9, NIPS 1996*, 155–161, MIT Press.

29. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-29)** Suykens, Johan A. K.; Vandewalle, Joos P. L.; "[Least squares support vector machine classifiers](https://lirias.kuleuven.be/bitstream/123456789/218716/2/Suykens_NeurProcLett.pdf)", *Neural Processing Letters*, vol. 9, no. 3, Jun. 1999, pp. 293–300

30. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-30)**  Smola, Alex J.; Schölkopf, Bernhard (2004). ["A tutorial on support vector regression"](http://eprints.pascal-network.org/archive/00000856/01/fulltext.pdf) (PDF). *Statistics and Computing*. **14** (3): 199–222. [Archived](https://web.archive.org/web/20120131193522/http://eprints.pascal-network.org/archive/00000856/01/fulltext.pdf) (PDF) from the original on 2012-01-31.

31. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-31)**  Polson, Nicholas G.; Scott, Steven L. (2011). ["Data Augmentation for Support Vector Machines"](https://projecteuclid.org/download/pdf_1/euclid.ba/1339611936). *Bayesian Analysis*. **6** (1): 1–23.

32. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-32)**  Wenzel, Florian; Galy-Fajou, Theo; Deutsch, Matthäus; Kloft, Marius (2017). ["Bayesian Nonlinear Support Vector Machines for Big Data"](https://arxiv.org/pdf/1707.05532.pdf) (PDF). *Machine Learning and Knowledge Discovery in Databases (ECML PKDD)*. [Archived](https://web.archive.org/web/20170830194633/https://arxiv.org/pdf/1707.05532.pdf) (PDF) from the original on 2017-08-30.

33. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-33)**  Ferris, Michael C.; Munson, Todd S. (2002). ["Interior-Point Methods for Massive Support Vector Machines"](http://www.cs.wisc.edu/~ferris/papers/siopt-svm.pdf) (PDF). *SIAM Journal on Optimization*. **13** (3): 783. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1137/S1052623400374379](https://doi.org/10.1137%2FS1052623400374379). [Archived](https://web.archive.org/web/20081204224416/http://www.cs.wisc.edu/~ferris/papers/siopt-svm.pdf) (PDF) from the original on 2008-12-04.

34. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-34)**  Platt, John C. (1998). [*Sequential Minimal Optimization: A Fast Algorithm for Training Support Vector Machines*](http://research.microsoft.com/pubs/69644/tr-98-14.pdf) (PDF). NIPS. [Archived](https://web.archive.org/web/20150702075055/http://research.microsoft.com/pubs/69644/tr-98-14.pdf) (PDF) from the original on 2015-07-02.

35. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-35)**  Shalev-Shwartz, Shai; Singer, Yoram; Srebro, Nathan (2007). [*Pegasos: Primal Estimated sub-GrAdient SOlver for SVM*](http://ttic.uchicago.edu/~shai/papers/ShalevSiSr07.pdf) (PDF). ICML. [Archived](https://web.archive.org/web/20131215051700/http://ttic.uchicago.edu/~shai/papers/ShalevSiSr07.pdf) (PDF) from the original on 2013-12-15.

36. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-36)**  Fan, Rong-En; Chang, Kai-Wei; Hsieh, Cho-Jui; Wang, Xiang-Rui; Lin, Chih-Jen (2008). ["LIBLINEAR: A library for large linear classification"](https://www.csie.ntu.edu.tw/~cjlin/papers/liblinear.pdf) (PDF). *[Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research)*. **9**: 1871–1874.

37. **[Jump up ^](https://en.wikipedia.org/wiki/Support_vector_machine#cite_ref-37)**  Allen Zhu, Zeyuan; Chen, Weizhu; Wang, Gang; Zhu, Chenguang; Chen, Zheng (2009). [*P-packSVM: Parallel Primal grAdient desCent Kernel SVM*](http://people.csail.mit.edu/zeyuan/paper/2009-ICDM-Parallel.pdf) (PDF). ICDM. [Archived](https://web.archive.org/web/20140407095709/http://people.csail.mit.edu/zeyuan/paper/2009-ICDM-Parallel.pdf) (PDF) from the original on 2014-04-07.

## Bibliography[]

- Theodoridis, Sergios; and Koutroumbas, Konstantinos; *Pattern Recognition*, 4th Edition, Academic Press, 2009, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-1-59749-272-0](https://en.wikipedia.org/wiki/Special:BookSources/978-1-59749-272-0)
- Cristianini, Nello; and Shawe-Taylor, John; *[An Introduction to Support Vector Machines and other kernel-based learning methods](http://www.support-vector.net/)*, Cambridge University Press, 2000. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-521-78019-5](https://en.wikipedia.org/wiki/Special:BookSources/0-521-78019-5)  *(SVM Book)*
- Huang, Te-Ming; Kecman, Vojislav; and Kopriva, Ivica; (2006); "[Kernel Based Algorithms for Mining Huge Data Sets](http://learning-from-data.com/)", in *Supervised, Semi-supervised, and Unsupervised Learning*, Springer-Verlag, Berlin, Heidelberg, 260 pp. 96 illus., Hardcover, [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [3-540-31681-7](https://en.wikipedia.org/wiki/Special:BookSources/3-540-31681-7)
- Kecman, Vojislav; *[Learning and Soft Computing — Support Vector Machines, Neural Networks, Fuzzy Logic Systems](http://www.support-vector.ws/)*, The MIT Press, Cambridge, MA, 2001
- Schölkopf, Bernhard; and Smola, Alexander J.; *Learning with Kernels*, MIT Press, Cambridge, MA, 2002. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-262-19475-9](https://en.wikipedia.org/wiki/Special:BookSources/0-262-19475-9)
- Schölkopf, Bernhard; Burges, Christopher J. C.; and Smola, Alexander J. (editors); *[Advances in Kernel Methods: Support Vector Learning](https://web.archive.org/web/20071017030144/http://kernel-machines.org/nips97/book.html)*, MIT Press, Cambridge, MA, 1999. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-262-19416-3](https://en.wikipedia.org/wiki/Special:BookSources/0-262-19416-3)
- Shawe-Taylor, John; and Cristianini, Nello; *[Kernel Methods for Pattern Analysis](http://www.kernel-methods.net/)*, Cambridge University Press, 2004. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-521-81397-2](https://en.wikipedia.org/wiki/Special:BookSources/0-521-81397-2)  *(Kernel Methods Book)*
- Steinwart, Ingo; and Christmann, Andreas; *[Support Vector Machines](https://web.archive.org/web/20120220084913/http://www.staff.uni-bayreuth.de/~btms01/svm.html)*, Springer-Verlag, New York, 2008. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-387-77241-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-77241-7)  *(SVM Book)*
- Tan, Peter Jing; and [Dowe, David L.](http://www.csse.monash.edu.au/~dld) (2004); [*MML Inference of Oblique Decision Trees*](http://www.csse.monash.edu.au/~dld/David.Dowe.publications.html#TanDowe2004), Lecture Notes in Artificial Intelligence (LNAI) 3339, Springer-Verlag, [pp. 1082–1088](http://www.csse.monash.edu.au/~dld/Publications/2004/Tan+DoweAI2004.pdf)  *(This paper uses [minimum message length](https://en.wikipedia.org/wiki/Minimum_message_length) ([MML](https://en.wikipedia.org/wiki/Minimum_Message_Length)) and actually incorporates probabilistic support vector machines in the leaves of [decision trees](https://en.wikipedia.org/wiki/Decision_tree_learning))*
- Vapnik, Vladimir N.; *The Nature of Statistical Learning Theory*, Springer-Verlag, 1995. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-387-98780-0](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98780-0)
- Vapnik, Vladimir N.; and Kotz, Samuel; *Estimation of Dependences Based on Empirical Data*, Springer, 2006. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-387-30865-2](https://en.wikipedia.org/wiki/Special:BookSources/0-387-30865-2)  *(this is a reprint of Vapnik's early book describing philosophy behind SVM approach; the 2006 Appendix describes recent developments)*
- Fradkin, Dmitriy; and Muchnik, Ilya; "[Support Vector Machines for Classification](http://paul.rutgers.edu/~dfradkin/papers/svm.pdf)" in Abello, J.; and Carmode, G. (Eds); *Discrete Methods in Epidemiology*, DIMACS Series in Discrete Mathematics and Theoretical Computer Science, volume 70, pp. 13–20, 2006 *(Succinctly describes theoretical ideas behind SVM)*
- Bennett, Kristin P.; and Campbell, Colin; "[Support Vector Machines: Hype or Hallelujah?](http://kdd.org/exploration_files/bennett.pdf)", *SIGKDD Explorations*, 2, 2, 2000, 1–13 *(Excellent introduction to SVMs with helpful figures)*
- Ivanciuc, Ovidiu; "[Applications of Support Vector Machines in Chemistry](http://www.ivanciuc.org/Files/Reprint/Ivanciuc_SVM_CCR_2007_23_291.pdf)", in *Reviews in Computational Chemistry*, Volume 23, 2007, pp. 291–400
- Catanzaro, Bryan; Sundaram, Narayanan; and Keutzer, Kurt; "[Fast Support Vector Machine Training and Classification on Graphics Processors](https://web.archive.org/web/20120302180102/http://www.eecs.berkeley.edu/~catanzar/icml2008.pdf)", in *International Conference on Machine Learning*, 2008
- Campbell, Colin; and Ying, Yiming; *[Learning with Support Vector Machines](http://www.morganclaypool.com/doi/abs/10.2200/S00324ED1V01Y201102AIM010)*, Morgan and Claypool, 2011 [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-1-60845-616-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-60845-616-1)
- Ben-Hur, Asa; Horn, David; Siegelmann, Hava; and Vapnik, Vladimir; "Support vector clustering" (2001) *Journal of Machine Learning Research*, 2: 125–137

## External links[]

- [libsvm](http://www.csie.ntu.edu.tw/~cjlin/libsvm/), [LIBSVM](https://en.wikipedia.org/wiki/LIBSVM) is a popular library of SVM learners
- [liblinear](http://www.csie.ntu.edu.tw/~cjlin/liblinear/) is a library for large linear classification including some SVMs
- [SVM light](http://svmlight.joachims.org/) is a collection of software tools for learning and classification using SVM
- [SVMJS live demo](http://cs.stanford.edu/people/karpathy/svmjs/demo/) is a GUI demo for [JavaScript](https://en.wikipedia.org/wiki/JavaScript) implementation of SVMs