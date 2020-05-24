Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing

## [Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing](http://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html)

Friday, November 2, 2018

 Posted by Jacob Devlin and Ming-Wei Chang, Research Scientists, Google AI Language

One of the biggest challenges in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) (NLP) is the shortage of training data. Because NLP is a diversified field with many distinct tasks, most task-specific datasets contain only a few thousand or a few hundred thousand human-labeled training examples. However, modern deep learning-based NLP models see benefits from much larger amounts of data, improving when trained on millions, or *billions*, of annotated training examples. To help close this gap in data, researchers have developed a variety of techniques for training general purpose language representation models using the enormous amount of unannotated text on the web (known as *pre-training*). The pre-trained model can then be *fine-tuned* on small-data NLP tasks like [question answering](https://en.wikipedia.org/wiki/Question_answering) and [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis), resulting in substantial accuracy improvements compared to training on these datasets from scratch.

This week, we [open sourced](https://goo.gl/language/bert) a new technique for NLP pre-training called **B**idirectional **E**ncoder **R**epresentations from [**T**ransformers](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html), or **BERT**. With this release, anyone in the world can train their own state-of-the-art question answering system (or a variety of other models) in about 30 minutes on a single [Cloud TPU](https://cloud.google.com/tpu/), or in a few hours using a single GPU. The release includes source code built on top of [TensorFlow](https://www.tensorflow.org/) and a number of pre-trained language representation models. [In our associated paper](https://arxiv.org/abs/1810.04805), we demonstrate state-of-the-art results on 11 NLP tasks, including the very competitive [Stanford Question Answering Dataset](https://rajpurkar.github.io/SQuAD-explorer/) (SQuAD v1.1).

**What Makes BERT Different? **

BERT builds upon recent work in pre-training contextual representations — including [Semi-supervised Sequence Learning](https://arxiv.org/abs/1511.01432), [Generative Pre-Training](https://blog.openai.com/language-unsupervised/), [ELMo](https://allennlp.org/elmo), and [ULMFit](http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html). However, unlike these previous models, BERT is the first *deeply bidirectional*, *unsupervised* language representation, pre-trained using only a plain text corpus (in this case, [Wikipedia](https://www.wikipedia.org/)).

Why does this matter? Pre-trained representations can either be *context-free* or *contextual*, and *contextual* representations can further be *unidirectional* or *bidirectional*. Context-free models such as [word2vec](https://en.wikipedia.org/wiki/Word2vec) or [GloVe](https://nlp.stanford.edu/projects/glove/) generate a single [word embedding](https://www.tensorflow.org/tutorials/representation/word2vec) representation for each word in the vocabulary. For example, the word “*bank*” would have the same context-free representation in “*bank account*” and “*bank of the river.*” Contextual models instead generate a representation of each word that is based on the other words in the sentence. For example, in the sentence “*I accessed the bank account*,” a unidirectional contextual model would represent “*bank*” based on “*I accessed the*” but not “*account*.” However, BERT represents “*bank*” using both its previous and next context — “*I accessed the* ... *account*” — starting from the very bottom of a deep neural network, making it deeply bidirectional.

A visualization of BERT’s neural network architecture compared to previous state-of-the-art contextual pre-training methods is shown below. The arrows indicate the information flow from one layer to the next. The green boxes at the top indicate the final contextualized representation of each input word:

|     |
| --- |
| [![image3.png](../_resources/20eb24a91b6add43a3bdc86d1717be00.png)](https://1.bp.blogspot.com/-RLAbr6kPNUo/W9is5FwUXmI/AAAAAAAADeU/5y9466Zoyoc96vqLjbruLK8i_t8qEdHnQCLcBGAs/s1600/image3.png) |
| BERT is deeply bidirectional, OpenAI GPT is unidirectional, and ELMo is shallowly bidirectional. |

**The Strength of Bidirectionality**

If bidirectionality is so powerful, why hasn’t it been done before? To understand why, consider that unidirectional models are efficiently trained by predicting each word conditioned on the previous words in the sentence. However, it is not possible to train bidirectional models by simply conditioning each word on its previous *and* next words, since this would allow the word that’s being predicted to indirectly “see itself” in a multi-layer model.

To solve this problem, we use the straightforward technique of masking out some of the words in the input and then condition each word bidirectionally to predict the masked words. For example:

[![f1.png](../_resources/0f02706281e22cf7d1d1b09214a3bbc5.png)](https://2.bp.blogspot.com/-pNxcHHXNZg0/W9iv3evVyOI/AAAAAAAADfA/KTSvKXNzzL0W8ry28PPl7nYI1CG_5WuvwCLcBGAs/s1600/f1.png)

While this idea has been around for a [very long time](http://psycnet.apa.org/record/1955-00850-001), BERT is the first time it was successfully used to pre-train a deep neural network.

BERT also learns to model relationships between sentences by pre-training on a very simple task that can be generated from any text corpus: Given two sentences A and B, is B the actual next sentence that comes after A in the corpus, or just a random sentence? For example:

[![f2.png](../_resources/06b31c53863650bcf6f4fc5dba05c23d.png)](https://4.bp.blogspot.com/-K_7yu3kjF18/W9iv-R-MnyI/AAAAAAAADfE/xUwR_G1iTY0vq9X-Z3LnW5t4NLS9BQzdgCLcBGAs/s1600/f2.png)

**Training with Cloud TPUs**

Everything that we’ve described so far might seem fairly straightforward, so what’s the missing piece that made it work so well? [Cloud TPUs](https://cloud.google.com/tpu/docs/tpus). Cloud TPUs gave us the freedom to quickly experiment, debug, and tweak our models, which was critical in allowing us to move beyond existing pre-training techniques. The [Transformer model architecture](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html), developed by researchers at Google in 2017, also gave us the foundation we needed to make BERT successful. The Transformer is implemented in our [open source release](https://goo.gl/language/bert), as well as the [tensor2tensor library](https://github.com/tensorflow/tensor2tensor).

**Results with BERT**

To evaluate performance, we compared BERT to other state-of-the-art NLP systems. Importantly, BERT achieved all of its results with almost no task-specific changes to the neural network architecture. On [SQuAD v1.1](https://rajpurkar.github.io/SQuAD-explorer/), BERT achieves 93.2% F1 score (a measure of accuracy), surpassing the previous state-of-the-art score of 91.6% and human-level score of 91.2%:

[![image3.png](../_resources/27129d1c9abc2c22f9068608ceab04b2.png)](https://4.bp.blogspot.com/-iQZIsE3lbVY/W9i8Tc-F7RI/AAAAAAAADfU/DrxjBoDfqrwe6GJUxENqWuzQ0IPlgT3TgCLcBGAs/s1600/image3.png)

BERT also improves the state-of-the-art by 7.6% absolute on the very challenging [GLUE benchmark](https://gluebenchmark.com/), a set of 9 diverse Natural Language Understanding (NLU) tasks. The amount of human-labeled training data in these tasks ranges from 2,500 examples to 400,000 examples, and BERT substantially [improves upon the state-of-the-art](https://gluebenchmark.com/leaderboard) accuracy on all of them:

[![image1.png](../_resources/eca7681bb7ecc62f65a8a1ae43cf7b5c.png)](https://1.bp.blogspot.com/-LF3fzlLXOjI/W9i8hcEKTxI/AAAAAAAADfY/HG-K6NGNNRIIfnojh_9G_83DkauwiSz3gCLcBGAs/s1600/image1.png)

**Making BERT Work for You**

The models that we are releasing can be fine-tuned on a wide variety of NLP tasks in a few hours or less. The open source release also includes code to run pre-training, although we believe the majority of NLP researchers who use BERT will never need to pre-train their own models from scratch. The BERT models that we are releasing today are English-only, but we hope to release models which have been pre-trained on a variety of languages in the near future.

The open source TensorFlow implementation and pointers to pre-trained BERT models can be found at [http://goo.gl/language/bert](https://goo.gl/language/bert). Alternatively, you can get started using BERT through [Colab](https://colab.sandbox.google.com/) with the notebook “[BERT FineTuning with Cloud TPUs](https://colab.sandbox.google.com/github/tensorflow/tpu/blob/master/tools/colab/bert_finetuning_with_cloud_tpus.ipynb).”

You can also read our paper "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)" for more details.

![post_twitter_black_24dp.png](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![post_facebook_black_24dp.png](../_resources/a4a815e062b3a04ad2cb425115438650.png)