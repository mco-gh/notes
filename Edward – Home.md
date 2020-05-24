Edward – Home

# [Edward](http://edwardlib.org/)

[![Edward](../_resources/6018704a7d7c85696e776988430b5165.png)](http://edwardlib.org/)[Getting Started](http://edwardlib.org/getting-started)[Tutorials](http://edwardlib.org/tutorials/)[API](http://edwardlib.org/api/)[Community](http://edwardlib.org/community)[Contributing](http://edwardlib.org/contributing)

[Github  ![Edward on Github](../_resources/4e757b3dc47013d1ba14815aeabe1066.png)](https://github.com/blei-lab/edward)

## A library for probabilistic modeling, inference, and criticism.

Edward is a Python library for probabilistic modeling, inference, and criticism. It is a testbed for fast experimentation and research with probabilistic models, ranging from classical hierarchical models on small data sets to complex deep probabilistic models on large data sets. Edward fuses three fields: Bayesian statistics and machine learning, deep learning, and probabilistic programming.

It supports **modeling** with

- Directed graphical models
- Neural networks (via libraries such as [Keras](http://keras.io/) and [TensorFlow Slim](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim))
- Implicit generative models
- Bayesian nonparametrics and probabilistic programs

It supports **inference** with

- Variational inference
    - Black box variational inference
    - Stochastic variational inference
    - Generative adversarial networks
    - Maximum a posteriori estimation
- Monte Carlo
    - Gibbs sampling
    - Hamiltonian Monte Carlo
    - Stochastic gradient Langevin dynamics
- Compositions of inference
    - Expectation-Maximization
    - Pseudo-marginal and ABC methods
    - Message passing algorithms

It supports **criticism** of the model and inference with

- Point-based evaluations
- Posterior predictive checks

Edward is built on [TensorFlow](https://www.tensorflow.org/). It enables features such as computational graphs, distributed training, CPU/GPU integration, automatic differentiation, and visualization with TensorBoard.

### Authors

Edward is led by [Dustin Tran](http://dustintran.com/) with guidance by [David Blei](http://www.cs.columbia.edu/~blei/). See the [full list of contributors](https://github.com/blei-lab/edward/graphs/contributors).

We are open to collaboration, and welcome researchers and developers to contribute. Check out the [contributing page](http://edwardlib.org/contributing) for how to improve Edward’s software. For broader research discussion, check out the [Forum](https://discourse.edwardlib.org/).

Edward has benefited enormously from the helpful feedback and advice of many individuals: Jaan Altosaar, Eugene Brevdo, Allison Chaney, Joshua Dillon, Matthew Hoffman, Kevin Murphy, Rajesh Ranganath, Rif Saurous, and other members of the Blei Lab, Google Brain, and Google Research.

### Citation

There are several articles to cite for Edward; also see Edward’s [license page](http://edwardlib.org/license).

The following article describes the API of Edward. It bundles the website’s documentation as a PDF. We recommend citing this article as a general default.

> Dustin Tran, Alp Kucukelbir, Adji B. Dieng, Maja Rudolph, Dawen Liang, and David M. Blei. 2016. > [*> Edward: A library for probabilistic modeling, inference, and criticism.*](https://arxiv.org/abs/1610.09787)>  arXiv preprint arXiv:1610.09787.

	@article{tran2016edward,
	  author = {Dustin Tran and Alp Kucukelbir and Adji B. Dieng and Maja Rudolph and Dawen Liang and David M. Blei},
	  title = {{Edward: A library for probabilistic modeling, inference, and criticism}},
	  journal = {arXiv preprint arXiv:1610.09787},
	  year = {2016}
	}

The following article describes the algorithmic foundations of Edward, with a [companion webpage here](http://edwardlib.org/iclr2017). We recommend citing this article if you are discussing Edward’s design and methodology.

> Dustin Tran, Matthew D. Hoffman, Rif A. Saurous, Eugene Brevdo, Kevin Murphy, and David M. Blei. 2017. > [*> Deep Probabilistic Programming.*](https://arxiv.org/abs/1701.03757)>  International Conference on Learning Representations.

	@inproceedings{tran2017deep,
	  author = {Dustin Tran and Matthew D. Hoffman and Rif A. Saurous and Eugene Brevdo and Kevin Murphy and David M. Blei},
	  title = {Deep probabilistic programming},
	  booktitle = {International Conference on Learning Representations},
	  year = {2017}
	}