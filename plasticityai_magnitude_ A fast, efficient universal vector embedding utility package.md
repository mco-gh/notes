plasticityai/magnitude: A fast, efficient universal vector embedding utility package.

[![68747470733a2f2f6769746c61622e636f6d2f506c61737469636974792f6d61676e69747564652f7261772f6d61737465722f696d616765732f6d61676e69747564652e706e67](../_resources/45e13ec22f366bb6a145f01e2c3f353b.png)](https://camo.githubusercontent.com/b7b6b208050841cb4e8b917ab7407c29f8a9f9d3/68747470733a2f2f6769746c61622e636f6d2f506c61737469636974792f6d61676e69747564652f7261772f6d61737465722f696d616765732f6d61676e69747564652e706e67)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='816'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2217' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#magnitude-a-fast-simple-vector-embedding-utility-library)

Magnitude: a fast, simple vector embedding utility library

[![68747470733a2f2f6769746c61622e636f6d2f506c61737469636974792f6d61676e69747564652f6261646765732f6d61737465722f706970656c696e652e737667](../_resources/6035aa2c7a1ab4fc14ad3da626b5ceb8.png)](https://gitlab.com/Plasticity/magnitude/commits/master)   [![68747470733a2f2f7472617669732d63692e6f72672f706c617374696369747961692f6d61676e69747564652e7376673f6272616e63683d6d6173746572](../_resources/6e77b43080c94e06849fc7e456ad1329.png)](https://travis-ci.org/plasticityai/magnitude)   [![68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f37326c776832673761396464626e74322f6272616e63682f6d61737465723f7376673d74727565](../_resources/c241c28aa0a0d4586acb5fd42799d37b.png)](https://ci.appveyor.com/project/plasticity-admin/magnitude/branch/master)

[![68747470733a2f2f62616467652e667572792e696f2f70792f70796d61676e69747564652e737667](../_resources/2faef555d1b48577b954eb2f4c905ee3.png)](https://pypi.python.org/pypi/pymagnitude/)   [![68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d6173686170652f6170697374617475732e7376673f6d61784167653d32353932303030](../_resources/06e339dc91b1a05960bbf043dae8b85b.png)](https://gitlab.com/Plasticity/magnitude/blob/master/LICENSE.txt)   [![68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f70796d61676e69747564652e737667](../_resources/0d02a7fa6f436c85b5ecff0850b239d8.png)](https://pypi.python.org/pypi/pymagnitude/)    [![68747470733a2f2f7a656e6f646f2e6f72672f62616467652f3132323731353433322e737667](../_resources/04dbd7b5fa3f65b9fd97cdc8710e96e2.png)](https://zenodo.org/badge/latestdoi/122715432)    [![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d313831302e31313139302d2532334234314131412e737667](../_resources/1846fad8c31bbfb65804322bda0c7e0b.png)](https://arxiv.org/abs/1810.11190)

A feature-packed Python package and vector storage file format for utilizing vector embeddings in machine learning models in a fast, efficient, and simple manner developed by [Plasticity](https://www.plasticity.ai/). It is primarily intended to be a simpler / faster alternative to [Gensim](https://radimrehurek.com/gensim/), but can be used as a generic key-vector store for domains outside NLP. It offers unique features like [out-of-vocabulary lookups](https://github.com/plasticityai/magnitude#advanced-out-of-vocabulary-keys) and [streaming of large models over HTTP](https://github.com/plasticityai/magnitude#remote-streaming-over-http). Published in our paper at [EMNLP 2018](http://aclweb.org/anthology/D18-2021) and available on [arXiv](https://arxiv.org/abs/1810.11190).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='817'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2224' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#table-of-contents)Table of Contents

- [Installation](https://github.com/plasticityai/magnitude#installation)
- [Motivation](https://github.com/plasticityai/magnitude#motivation)
- [Benchmarks and Features](https://github.com/plasticityai/magnitude#benchmarks-and-features)
- [Pre-converted Magnitude Formats of Popular Embeddings Models](https://github.com/plasticityai/magnitude#pre-converted-magnitude-formats-of-popular-embeddings-models)
- [Using the Library](https://github.com/plasticityai/magnitude#using-the-library)
    - [Constructing a Magnitude Object](https://github.com/plasticityai/magnitude#constructing-a-magnitude-object)
    - [Querying](https://github.com/plasticityai/magnitude#querying)
    - [Basic Out-of-Vocabulary Keys](https://github.com/plasticityai/magnitude#basic-out-of-vocabulary-keys)
    - [Advanced Out-of-Vocabulary Keys](https://github.com/plasticityai/magnitude#advanced-out-of-vocabulary-keys)
        - [Handling Misspellings and Typos](https://github.com/plasticityai/magnitude#handling-misspellings-and-typos)
    - [Concatenation of Multiple Models](https://github.com/plasticityai/magnitude#concatenation-of-multiple-models)
    - [Additional Featurization (Parts of Speech, etc.)](https://github.com/plasticityai/magnitude#additional-featurization-parts-of-speech-etc)
    - [Using Magnitude with a ML library](https://github.com/plasticityai/magnitude#using-magnitude-with-a-ml-library)
        - [Keras](https://github.com/plasticityai/magnitude#keras)
        - [PyTorch](https://github.com/plasticityai/magnitude#pytorch)
        - [TFLearn](https://github.com/plasticityai/magnitude#tflearn)
    - [Utils](https://github.com/plasticityai/magnitude#utils)
- [Concurrency and Parallelism](https://github.com/plasticityai/magnitude#concurrency-and-parallelism)
- [File Format and Converter](https://github.com/plasticityai/magnitude#file-format-and-converter)
- [Remote Loading](https://github.com/plasticityai/magnitude#remote-loading)
- [Remote Streaming over HTTP](https://github.com/plasticityai/magnitude#remote-streaming-over-http)
- [Other Documentation](https://github.com/plasticityai/magnitude#other-documentation)
- [Other Languages](https://github.com/plasticityai/magnitude#other-languages)
- [Other Programming Languages](https://github.com/plasticityai/magnitude#other-programming-languages)
- [Other Domains](https://github.com/plasticityai/magnitude#other-domains)
- [Contributing](https://github.com/plasticityai/magnitude#contributing)
- [Roadmap](https://github.com/plasticityai/magnitude#roadmap)
- [Other Notable Projects](https://github.com/plasticityai/magnitude#other-notable-projects)
- [Citing this Repository](https://github.com/plasticityai/magnitude#citing-this-repository)
- [LICENSE and Attribution](https://github.com/plasticityai/magnitude#license-and-attribution)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='818'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2260' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#installation)Installation

You can install this package with `pip`:
pip install pymagnitude # Python 2.7pip3 install pymagnitude # Python 3

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='819'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2264' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#motivation)Motivation

Vector space embedding models have become increasingly common in machine learning and traditionally have been popular for natural language processing applications. A fast, lightweight tool to consume these large vector space embedding models efficiently is lacking.

The Magnitude file format (`.magnitude`) for vector embeddings is intended to be a more efficient universal vector embedding format that allows for lazy-loading for faster cold starts in development, LRU memory caching for performance in production, multiple key queries, direct featurization to the inputs for a neural network, performant similiarity calculations, and other nice to have features for edge cases like handling out-of-vocabulary keys or misspelled keys and concatenating multiple vector models together. It also is intended to work with large vector models that may not fit in memory.

It uses [SQLite](http://www.sqlite.org/), a fast, popular embedded database, as its underlying data store. It uses indexes for fast key lookups as well as uses memory mapping, SIMD instructions, and spatial indexing for fast similarity search in the vector space off-disk with good memory performance even between multiple processes. Moreover, memory maps are cached between runs so even after closing a process, speed improvements are reaped.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='820'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2269' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#benchmarks-and-features)Benchmarks and Features

**Metric**
**Magnitude Light**
**Magnitude Medium**
**Magnitude Heavy**

**Magnitude [Stream](https://github.com/plasticityai/magnitude#remote-streaming-over-http)**

Initial load time
**0.7210s**
━ 1
━ 1
7.7550s
Cold single key query
**0.0001s**
━ 1
━ 1
1.6437s
Warm single key query
*(same key as cold query)*
**0.00004s**
━ 1
━ 1
**0.0004s**
Cold multiple key query
*(n=25)*
**0.0442s**
━ 1
━ 1
1.7753s
Warm multiple key query
*(n=25) (same keys as cold query)*
**0.00004s**
━ 1
━ 1
**0.0001s**
First [object Object] search query
*(n=10) (worst case)*
247.05s
━ 1
━ 1
-
First [object Object] search query
*(n=10) (average case) (w/ disk persistent cache)*
**1.8217s**
━ 1
━ 1
-
Subsequent [object Object] search
*(n=10) (different key than first query)*
**0.2434s**
━ 1
━ 1
-
Warm subsequent [object Object] search
*(n=10) (same key as first query)*
**0.00004s**
**0.00004s**
**0.00004s**
-
First [object Object] search query
*(n=10, effort=1.0) (worst case)*
N/A
N/A
**29.610s**
-
First [object Object] search query
*(n=10, effort=1.0) (average case) (w/ disk persistent cache)*
N/A
N/A
**0.9155s**
-
Subsequent [object Object] search
*(n=10, effort=1.0) (different key than first query)*
N/A
N/A
**0.1873s**
-
Subsequent [object Object] search
*(n=10, effort=0.1) (different key than first query)*
N/A
N/A
**0.0199s**
-
Warm subsequent [object Object] search
*(n=10, effort=1.0) (same key as first query)*
N/A
N/A
**0.00004s**
-
File size
4.21GB
5.29GB
10.74GB
**0.00GB**
Process memory (RAM) utilization
**18KB**
━ 1
━ 1
1.71MB
Process memory (RAM) utilization after 100 key queries
**168KB**
━ 1
━ 1
1.91MB
Process memory (RAM) utilization after 100 key queries + similarity search
**342KB**2
━ 1
━ 1

Integrity checks and tests
✅
✅
✅
✅

Universal format between word2vec ([object Object], [object Object]), GloVe ([object Object]), fastText ([object Object]), and ELMo ([object Object]) with converter utility

✅
✅
✅
✅
Simple, Pythonic interface
✅
✅
✅
✅
Few dependencies
✅
✅
✅
✅
Support for larger than memory models
✅
✅
✅
✅
Lazy loading whenever possible for speed and performance
✅
✅
✅
✅
Optimized for [object Object] and [object Object]
✅
✅
✅
✅

Bulk and multiple key lookup with padding, truncation, placeholder, and featurization support

✅
✅
✅
✅
Concatenting multiple vector models together
✅
✅
✅
✅
Basic out-of-vocabulary key lookup
(character n-gram feature hashing)
✅
✅
✅
✅
Advanced out-of-vocabulary key lookup with support for misspellings
(character n-gram feature hashing to similar in-vocabulary keys)
❌
✅
✅
✅

Approximate most similar search with an [annoy](https://github.com/plasticityai/magnitude#other-notable-projects) index

❌
❌
✅
✅
Built-in training for new models
❌
❌
❌
❌
1: *same value as previous column*

2: *uses `mmap` to read from disk, so the OS will still allocate pages of memory when memory is available, but it can be shared between processes and isn't managed within each process for extremely large files which is a performance win*

*: All [benchmarks](https://gitlab.com/Plasticity/magnitude/blob/master/tests/benchmark.py) were performed on the Google News pre-trained word vectors (`GoogleNews-vectors-negative300.bin`) with a MacBook Pro (Retina, 15-inch, Mid 2014) 2.2GHz quad-core Intel Core i7 @ 16GB RAM on SSD over an average of trials where feasible.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='821'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2497' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#pre-converted-magnitude-formats-of-popular-embeddings-models)Pre-converted Magnitude Formats of Popular Embeddings Models

Popular embedding models have been pre-converted to the `.magnitude` format for immmediate download and usage:

**Contributor**
**Data**
**Light**

(basic support for out-of-vocabulary keys)
**Medium**
*(recommended)*

(advanced support for out-of-vocabulary keys)
**Heavy**

(advanced support for out-of-vocabulary keys and faster [object Object])
Google - [word2vec](https://code.google.com/archive/p/word2vec/)
Google News 100B

[300D](http://magnitude.plasticity.ai/word2vec/light/GoogleNews-vectors-negative300.magnitude)

[300D](http://magnitude.plasticity.ai/word2vec/medium/GoogleNews-vectors-negative300.magnitude)

[300D](http://magnitude.plasticity.ai/word2vec/heavy/GoogleNews-vectors-negative300.magnitude)

Stanford - [GloVe](https://nlp.stanford.edu/projects/glove/)
Wikipedia 2014 + Gigaword 5 6B

[50D](http://magnitude.plasticity.ai/glove/light/glove.6B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/light/glove.6B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/light/glove.6B.200d.magnitude), [300D](http://magnitude.plasticity.ai/glove/light/glove.6B.300d.magnitude)

[50D](http://magnitude.plasticity.ai/glove/medium/glove.6B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/medium/glove.6B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/medium/glove.6B.200d.magnitude), [300D](http://magnitude.plasticity.ai/glove/medium/glove.6B.300d.magnitude)

[50D](http://magnitude.plasticity.ai/glove/heavy/glove.6B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/heavy/glove.6B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/heavy/glove.6B.200d.magnitude), [300D](http://magnitude.plasticity.ai/glove/heavy/glove.6B.300d.magnitude)

Stanford - [GloVe](https://nlp.stanford.edu/projects/glove/)
Wikipedia 2014 + Gigaword 5 6B
(lemmatized by Plasticity)

[50D](http://magnitude.plasticity.ai/glove/light/glove-lemmatized.6B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/light/glove-lemmatized.6B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/light/glove-lemmatized.6B.200d.magnitude), [300D](http://magnitude.plasticity.ai/glove/light/glove-lemmatized.6B.300d.magnitude)

[50D](http://magnitude.plasticity.ai/glove/medium/glove-lemmatized.6B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/medium/glove-lemmatized.6B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/medium/glove-lemmatized.6B.200d.magnitude), [300D](http://magnitude.plasticity.ai/glove/medium/glove-lemmatized.6B.300d.magnitude)

[50D](http://magnitude.plasticity.ai/glove/heavy/glove-lemmatized.6B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/heavy/glove-lemmatized.6B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/heavy/glove-lemmatized.6B.200d.magnitude), [300D](http://magnitude.plasticity.ai/glove/heavy/glove-lemmatized.6B.300d.magnitude)

Stanford - [GloVe](https://nlp.stanford.edu/projects/glove/)
Common Crawl 840B
[300D](http://magnitude.plasticity.ai/glove/light/glove.840B.300d.magnitude)
[300D](http://magnitude.plasticity.ai/glove/medium/glove.840B.300d.magnitude)
[300D](http://magnitude.plasticity.ai/glove/heavy/glove.840B.300d.magnitude)
Stanford - [GloVe](https://nlp.stanford.edu/projects/glove/)
Twitter 27B

[25D](http://magnitude.plasticity.ai/glove/light/glove.twitter.27B.25d.magnitude), [50D](http://magnitude.plasticity.ai/glove/light/glove.twitter.27B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/light/glove.twitter.27B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/light/glove.twitter.27B.200d.magnitude)

[25D](http://magnitude.plasticity.ai/glove/medium/glove.twitter.27B.25d.magnitude), [50D](http://magnitude.plasticity.ai/glove/medium/glove.twitter.27B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/medium/glove.twitter.27B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/medium/glove.twitter.27B.200d.magnitude)

[25D](http://magnitude.plasticity.ai/glove/heavy/glove.twitter.27B.25d.magnitude), [50D](http://magnitude.plasticity.ai/glove/heavy/glove.twitter.27B.50d.magnitude), [100D](http://magnitude.plasticity.ai/glove/heavy/glove.twitter.27B.100d.magnitude), [200D](http://magnitude.plasticity.ai/glove/heavy/glove.twitter.27B.200d.magnitude)

Facebook - [fastText](https://fasttext.cc/docs/en/english-vectors.html)
English Wikipedia 2017 16B

[300D](http://magnitude.plasticity.ai/fasttext/light/wiki-news-300d-1M.magnitude)

[300D](http://magnitude.plasticity.ai/fasttext/medium/wiki-news-300d-1M.magnitude)

[300D](http://magnitude.plasticity.ai/fasttext/heavy/wiki-news-300d-1M.magnitude)

Facebook - [fastText](https://fasttext.cc/docs/en/english-vectors.html)
English Wikipedia 2017 + subword 16B

[300D](http://magnitude.plasticity.ai/fasttext/light/wiki-news-300d-1M-subword.magnitude)

[300D](http://magnitude.plasticity.ai/fasttext/medium/wiki-news-300d-1M-subword.magnitude)

[300D](http://magnitude.plasticity.ai/fasttext/heavy/wiki-news-300d-1M-subword.magnitude)

Facebook - [fastText](https://fasttext.cc/docs/en/english-vectors.html)
Common Crawl 600B
[300D](http://magnitude.plasticity.ai/fasttext/light/crawl-300d-2M.magnitude)
[300D](http://magnitude.plasticity.ai/fasttext/medium/crawl-300d-2M.magnitude)
[300D](http://magnitude.plasticity.ai/fasttext/heavy/crawl-300d-2M.magnitude)
AI2 - [AllenNLP ELMo](https://allennlp.org/elmo)
[ELMo Models](https://github.com/plasticityai/magnitude/blob/master/ELMo.md)
[ELMo Models](https://github.com/plasticityai/magnitude/blob/master/ELMo.md)
[ELMo Models](https://github.com/plasticityai/magnitude/blob/master/ELMo.md)
[ELMo Models](https://github.com/plasticityai/magnitude/blob/master/ELMo.md)
Google - [BERT](https://github.com/google-research/bert)
[Coming Soon...](https://github.com/plasticityai/magnitude#roadmap)
[Coming Soon...](https://github.com/plasticityai/magnitude#roadmap)
[Coming Soon...](https://github.com/plasticityai/magnitude#roadmap)
[Coming Soon...](https://github.com/plasticityai/magnitude#roadmap)

There are instructions [below](https://github.com/plasticityai/magnitude#file-format-and-converter) for converting any `.bin`, `.txt`, `.vec`, `.hdf5` file to a `.magnitude` file.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='822'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2579' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#using-the-library)Using the Library

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='823'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2581' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#constructing-a-magnitude-object)Constructing a Magnitude Object

You can create a Magnitude object like so:
from pymagnitude import  *vectors = Magnitude("/path/to/vectors.magnitude")

If needed, and included for convenience, you can also open a `.bin`, `.txt`, `.vec`, `.hdf5` file directly with Magnitude. This is, however, less efficient and very slow for large models as it will convert the file to a `.magnitude` file on the first run into a temporary directory. The temporary directory is not guaranteed to persist and does not persist when your computer reboots. You should [pre-convert `.bin`, `.txt`, `.vec`, `.hdf5` files with `python -m pymagnitude.converter`](https://github.com/plasticityai/magnitude#file-format-and-converter) typically for faster speeds, but this feature is useful for one-off use-cases. A warning will be generated when instantiating a Magnitude object directly with a `.bin`, `.txt`, `.vec`, `.hdf5`. You can supress warnings by setting the `supress_warnings` argument in the constructor to `True`.

* * *

- By default, lazy loading is enabled. You can pass in an optional `lazy_loading` argument to the constructor with the value `-1` to disable lazy-loading and pre-load all vectors into memory (a la Gensim), `0` (default) to enable lazy-loading with an unbounded in-memory LRU cache, or an integer greater than zero `X` to enable lazy-loading with an LRU cache that holds the `X` most recently used vectors in memory.
- If you want the data for the `most_similar` functions to be pre-loaded eagerly on initialization, set `eager` to `True`.
- Note, even when `lazy_loading` is set to `-1` or `eager` is set to `True` data will be pre-loaded into memory in a background thread to prevent the constructor from blocking for a few minutes for large models. If you really want blocking behavior, you can pass `True` to the `blocking` argument.
- By default, [unit-length normalized](https://en.wikipedia.org/wiki/Unit_vector) vectors are returned unless you are loading an ELMo model. Set the optional argument `normalized` to `False` if you wish to recieve the raw non-normalized vectors instead.
- By default, NumPy arrays are returned for queries. Set the optional argument `use_numpy` to `False` if you wish to recieve Python lists instead.
- By default, querying for keys is case-sensitive. Set the optional argument `case_insensitive` to `True` if you wish to perform case-insensitive searches.
- Optionally, you can include the `pad_to_length` argument which will specify the length all examples should be padded to if passing in multple examples. Any examples that are longer than the pad length will be truncated.
- Optionally, you can set the `truncate_left` argument to `True` if you want the beginning of the the list of keys in each example to be truncated instead of the end in case it is longer than `pad_to_length` when specified.
- Optionally, you can set the `pad_left` argument to `True` if you want the padding to appear at the beginning versus the end (which is the default).
- Optionally, you can pass in the `placeholders` argument, which will increase the dimensions of each vector by a `placeholders` amount, zero-padding those extra dimensions. This is useful, if you plan to add other values and information to the vectors and want the space for that pre-allocated in the vectors for efficiency.
- Optionally, you can pass in the `language` argument with an [ISO 639-1 Language Code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), which, if you are using Magnitude for word vectors, will ensure the library respects stemming and other language-specific features for that language. The default is `en` for English. You can also pass in `None` if you are not using Magnitude for word vectors.
- Optionally, you can pass in the `dtype` argument which will let you control the data type of the NumPy arrays returned by Magnitude.
- Optionally, you can pass in the `devices` argument which will let you control the usage of GPUs when the underlying models supports GPU usage. This argument should be a list of integers, where each integer represents the GPU device number (`0`, `1`, etc.).
- Optionally, you can pass in the `temp_dir` argument which will let you control the location of the temporary directory Magnitude will use.
- Optionally, you can pass in the `log` argument which will have Magnitude log progress to standard error when slow operations are taking place.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='824'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2602' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#querying)Querying

You can query the total number of vectors in the file like so:
len(vectors)

* * *

You can query the dimensions of the vectors like so:
vectors.dim

* * *

You can check if a key is in the vocabulary like so:
"cat"  in vectors

* * *

You can iterate through all keys and vectors like so:
for key, vector in vectors: ...

* * *

You can query for the vector of a key like so:
vectors.query("cat")

* * *

You can index for the n-th key and vector like so:
vectors[42]

* * *

You can query for the vector of multiple keys like so:
vectors.query(["I", "read", "a", "book"])
A 2D array (keys by vectors) will be returned.

* * *

You can query for the vector of multiple examples like so:
vectors.query([["I", "read", "a", "book"], ["I", "read", "a", "magazine"]])

A 3D array (examples by keys by vectors) will be returned. If `pad_to_length` is not specified, and the size of each example is uneven, they will be padded to the length of the longest example.

* * *

You can index for the keys and vectors of multiple indices like so:
vectors[:42] # slice notationvectors[42, 1337, 2001] # tuple notation

* * *

You can query the distance of two or multiple keys like so:
vectors.distance("cat", "dog")
vectors.distance("cat", ["dog", "tiger"])

* * *

You can query the similarity of two or multiple keys like so:
vectors.similarity("cat", "dog")
vectors.similarity("cat", ["dog", "tiger"])

* * *

You can query for the most similar key out of a list of keys to a given key like so:

vectors.most_similar_to_given("cat", ["dog", "television", "laptop"]) # dog

* * *

You can query for which key doesn't match a list of keys to a given key like so:

vectors.doesnt_match(["breakfast", "cereal", "dinner", "lunch"]) # cereal

* * *

You can query for the most similar (nearest neighbors) keys like so:

vectors.most_similar("cat", topn  =  100) # Most similar by keyvectors.most_similar(vectors.query("cat"), topn  =  100) # Most similar by vector

Optionally, you can pass a `min_similarity` argument to `most_similar`. Values from [-1.0-1.0] are valid.

* * *

You can also query for the most similar keys giving positive and negative examples (which, incidentally, solves analogies) like so:

vectors.most_similar(positive  = ["woman", "king"], negative  = ["man"]) # queen

* * *

Similar to `vectors.most_similar`, a `vectors.most_similar_cosmul` function exists that uses the 3CosMul function from [Levy and Goldberg](http://www.aclweb.org/anthology/W14-1618):

vectors.most_similar_cosmul(positive  = ["woman", "king"], negative  = ["man"]) # queen

* * *

You can also query for the most similar keys using an approximate nearest neighbors index which is much faster, but doesn't guarantee the exact answer:

vectors.most_similar_approx("cat")
vectors.most_similar_approx(positive  = ["woman", "king"], negative  = ["man"])

Optionally, you can pass an `effort` argument with values between [0.0-1.0] to the `most_similar_approx` function which will give you runtime trade-off. The default value for `effort` is 1.0 which will take the longest, but will give the most accurate result.

* * *

You can query for all keys closer to a key than another key is like so:
vectors.closer_than("cat", "rabbit") # ["dog", ...]

* * *

You can access all of the underlying vectors in the model in a large `numpy.memmap` array of size (`len(vectors) x vectors.emb_dim`) like so:

vectors.get_vectors_mmap()

* * *

You can clean up all associated resources, open files, and database connections like so:

vectors.close()

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='825'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2648' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#basic-out-of-vocabulary-keys)Basic Out-of-Vocabulary Keys

For word vector representations, handling out-of-vocabulary keys is important to handling new words not in the trained model, handling mispellings and typos, and making models trained on the word vector representations more robust in general.

Out-of-vocabulary keys are handled by assigning them a random vector value. However, the randomness is deterministic. So if the *same* out-of-vocabulary key is encountered twice, it will be assigned the same random vector value for the sake of being able to train on those out-of-vocabulary keys. Moreover, if two out-of-vocabulary keys share similar character n-grams ("uberx", "uberxl") they will placed close to each other even if they are both not in the vocabulary:

vectors = Magnitude("/path/to/GoogleNews-vectors-negative300.magnitude")"uberx"  in vectors # False"uberxl"  in vectors # Falsevectors.query("uberx") # array([ 5.07109939e-02, -7.08248823e-02, -2.74812328e-02, ... ])vectors.query("uberxl") # array([ 0.04734962, -0.08237578, -0.0333479, -0.00229564, ... ])vectors.similarity("uberx", "uberxl") # 0.955000000200815

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='826'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2654' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#advanced-out-of-vocabulary-keys)Advanced Out-of-Vocabulary Keys

If using a Magnitude file with advanced out-of-vocabulary support (Medium or Heavy), out-of-vocabulary keys will also be embedded close to similar keys (determined by string similarity) that *are in* the vocabulary:

vectors = Magnitude("/path/to/GoogleNews-vectors-negative300.magnitude")"uberx"  in vectors # False"uberification"  in vectors # False"uber"  in vectors # Truevectors.similarity("uberx", "uber") # 0.7383483267618451vectors.similarity("uberification", "uber") # 0.745452837882727

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='827'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2659' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#handling-misspellings-and-typos)Handling Misspellings and Typos

This also makes Magnitude robust to a lot of spelling errors:

vectors = Magnitude("/path/to/GoogleNews-vectors-negative300.magnitude")"missispi"  in vectors # Falsevectors.similarity("missispi", "mississippi") # 0.35961736624824003"discrimnatory"  in vectors # Falsevectors.similarity("discrimnatory", "discriminatory") # 0.8309152561753461"hiiiiiiiiii"  in vectors # Falsevectors.similarity("hiiiiiiiiii", "hi") # 0.7069775034853861

Character n-grams are used to create this effect for out-of-vocabulary keys. The inspiration for this feature was taken from Facebook AI Research's [Enriching Word Vectors with Subword Information](https://arxiv.org/pdf/1607.04606.pdf), but instead of utilizing character n-grams at train time, character n-grams are used at inference so the effect can be somewhat replicated (but not perfectly replicated) in older models that were not trained with character n-grams like word2vec and GloVe.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='828'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2664' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#concatenation-of-multiple-models)Concatenation of Multiple Models

Optionally, you can combine vectors from multiple models to feed stronger information into a machine learning model like so:

from pymagnitude import  *word2vec = Magnitude("/path/to/GoogleNews-vectors-negative300.magnitude")

glove = Magnitude("/path/to/glove.6B.50d.magnitude")

vectors = Magnitude(word2vec, glove) # concatenate word2vec with glovevectors.query("cat") # returns 350-dimensional NumPy array ('cat' from word2vec concatenated with 'cat' from glove)vectors.query(("cat", "cats")) # returns 350-dimensional NumPy array ('cat' from word2vec concatenated with 'cats' from glove)

You can concatenate more than two vector models, simply by passing more arguments to constructor.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='829'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2669' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#additional-featurization-parts-of-speech-etc)Additional Featurization (Parts of Speech, etc.)

You can automatically create vectors from additional features you may have such as parts of speech, syntax dependency information, or any other information using the `FeaturizerMagnitude` class:

from pymagnitude import  *pos_vectors = FeaturizerMagnitude(100, namespace  =  "PartsOfSpeech")

pos_vectors.dim # 4 - number of dims automatically determined by Magnitude from 100pos_vectors.query("NN") # - array([ 0.08040417, -0.71705252, 0.61228951, 0.32322192]) pos_vectors.query("JJ") # - array([-0.11681135, 0.10259253, 0.8841201 , -0.44063763])pos_vectors.query("NN") # - array([ 0.08040417, -0.71705252, 0.61228951, 0.32322192]) (deterministic hashing so the same value is returned every time for the same key)dependency_vectors = FeaturizerMagnitude(100, namespace  =  "SyntaxDependencies")

dependency_vectors.dim # 4 - number of dims automatically determined by Magnitude from 100dependency_vectors.query("nsubj") # - array([-0.81043793, 0.55401352, -0.10838071, 0.15656626])dependency_vectors.query("prep") # - array([-0.30862918, -0.44487267, -0.0054573 , -0.84071788])

Magnitude will use the [feature hashing trick](https://en.wikipedia.org/wiki/Feature_hashing) internally to directly use the hash of the feature value to create a unique vector for that feature value.

The first argument to `FeaturizerMagnitude` should be an approximate upper-bound on the number of values for the feature. Since there are < 100 [parts of speech tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) and < 100 [syntax dependencies](http://universaldependencies.org/u/dep/all.html), we choose 100 for both in the example above. The value chosen will determine how many dimensions Magnitude will automatically assign to the particular the `FeaturizerMagnitude` object to reduce the chance of a hash collision. The `namespace` argument can be any string that describes your additional feature. It is optional, but highly recommended.

You can then concatenate these features for use with a standard Magnitude object:

from pymagnitude import  *word2vec = Magnitude("/path/to/GoogleNews-vectors-negative300.magnitude")

pos_vectors = FeaturizerMagnitude(100, namespace  =  "PartsOfSpeech")

dependency_vectors = FeaturizerMagnitude(100, namespace  =  "SyntaxDependencies")

vectors = Magnitude(word2vec, pos_vectors, dependency_vectors) # concatenate word2vec with pos and dependenciesvectors.query([

("I", "PRP", "nsubj"), ("saw", "VBD", "ROOT"), ("a", "DT", "det"), ("cat", "NN", "dobj"), (".", ".", "punct")

]) # array of size 5 x (300 + 4 + 4) or 5 x 308# Or get a unique vector for every 'buffalo' in:# "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"# (https://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo)vectors.query([

("Buffalo", "JJ", "amod"), ("buffalo", "NNS", "nsubj"), ("Buffalo", "JJ", "amod"), ("buffalo", "NNS", "nsubj"), ("buffalo", "VBP", "rcmod"),

("buffalo", "VB", "ROOT"),
("Buffalo", "JJ", "amod"),
("buffalo", "NNS", "dobj")
]) # array of size 8 x (300 + 4 + 4) or 8 x 308

A machine learning model, given this output, now has access to parts of speech information and syntax dependency information instead of just word vector information. In this case, this additional information can give neural networks stronger signal for semantic information and reduce the need for training data.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='830'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2678' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#using-magnitude-with-a-ml-library)Using Magnitude with a ML library

Magnitude makes it very easy to quickly build and iterate on models that need to use vector representations by taking care of a lot of pre-processing code to convert a dataset of text (or keys) into vectors. Moreover, it can make these models more robust to [out-of-vocabulary words](https://github.com/plasticityai/magnitude#advanced-out-of-vocabulary-keys) and [misspellings](https://github.com/plasticityai/magnitude#handling-misspellings-and-typos).

There is example code available using Magnitude to build an intent classification model for the [ATIS (Airline Travel Information Systems) dataset](https://catalog.ldc.upenn.edu/docs/LDC93S4B/corpus.html) ([Train](http://magnitude.plasticity.ai/data/atis/atis-intent-train.txt)/[Test](http://magnitude.plasticity.ai/data/atis/atis-intent-test.txt)), used for chatbots or conversational interfaces, in a few popular machine learning libraries below.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='831'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2682' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#keras)Keras

You can access a guide for using Magnitude with Keras (which supports TensorFlow, Theano, CNTK) at this [Google Colaboratory Python notebook](https://colab.research.google.com/drive/1lOcAhIffLW8XC6QsKzt5T_ZqPP4Y9eS4).

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='832'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2685' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#pytorch)PyTorch

*The PyTorch guide is coming soon.*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='833'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2689' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#tflearn)TFLearn

*The TFLearn guide is coming soon.*

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='834'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2693' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#utils)Utils

You can use the `MagnitudeUtils` class for convenient access to functions that may be useful when creating machine learning models.

You can import MagnitudeUtils like so:
 from pymagnitude import MagnitudeUtils
You can download a Magnitude model from a remote source like so:

vecs = Magnitude(MagnitudeUtils.download_model('word2vec/heavy/GoogleNews-vectors-negative300'))

By default, `download_model` will download files from `http://magnitude.plasticity.ai` to a `~/.magnitude` folder created automatically. If the file has already been downloaded, it will not be downloaded again. You can change the directory of the local download folder using the optional `download_dir` argument. You can change the domain from which models will be downloaded with the optional `remote_path` argument.

You can create a batch generator for `X` and `y` data with `batchify`, like so:
X = [.3, .2, .7, .8, .1]
y = [0, 0, 1, 1, 0]

batch_gen = MagnitudeUtils.batchify(X, y, 2) for X_batch, y_batch in batch_gen: print(X_batch, y_batch) # Returns:  # 1st loop: X_batch = [.3, .2], y_batch = [0, 0]  # 2nd loop: X_batch = [.7, .8], y_batch = [1, 1]  # 3rd loop: X_batch = [.1], y_batch = [0]  # next loop: repeats infinitely...

You can encode class labels to integers and back with `class_encoding`, like so:

add_class, class_to_int, int_to_class = MagnitudeUtils.class_encoding()

add_class("cat") # Returns: 0 add_class("dog") # Returns: 1 add_class("cat") # Returns: 0 class_to_int("dog") # Returns: 1 class_to_int("cat") # Returns: 0 int_to_class(1) # Returns: "dog" int_to_class(0) # Returns: "cat"

You can convert categorical data with class integers to one-hot NumPy arrays with `to_categorical`, like so:

y = [1, 5, 2]

MagnitudeUtils.to_categorical(y, num_classes  =  6) # num_classes is optional  # Returns:   # array([[0., 1., 0., 0., 0., 0.]   # [0., 0., 0., 0., 0., 1.]   # [0., 0., 1., 0., 0., 0.]])

You can convert from one-hot NumPy arrays back to a 1D NumPy array of class integers with `from_categorical`, like so:

y_c = [[0., 1., 0., 0., 0., 0.],
[0., 0., 0., 0., 0., 1.]]
MagnitudeUtils.from_categorical(y_c) # Returns:   # array([1., 5.])

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='835'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2709' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#concurrency-and-parallelism)Concurrency and Parallelism

The library is thread safe (it uses a different connection to the underlying store per thread), is read-only, and it never writes to the file. Because of the light-memory usage, you can also run it in multiple processes (or use `multiprocessing`) with different address spaces without having to duplicate the data in-memory like with other libraries and without having to create a multi-process shared variable since data is read off-disk and each process keeps its own LRU memory cache. For heavier functions, like `most_similar` a shared memory mapped file is created to share memory between processes.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='836'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2712' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#file-format-and-converter)File Format and Converter

The Magnitude package uses the `.magnitude` file format instead of `.bin`, `.txt`, `.vec`, or `.hdf5` as with other vector models like word2vec, GloVe, fastText, and ELMo. There is an included command-line utility for converting word2vec, GloVe, fastText, and ELMo files to Magnitude files.

You can convert them like so:

python -m pymagnitude.converter -i <PATH TO FILE TO BE CONVERTED> -o <OUTPUT PATH FOR MAGNITUDE FILE>

The input format will automatically be determined by the extension / the contents of the input file. You should only need to perform this conversion once for a model. After converting, the Magnitude file format is static and it will not be modified or written to make concurrent read access safe.

The flags for `pymagnitude.converter` are specified below:

- You can pass in the `-h` flag for help and to list all flags.
- You can use the `-p <PRECISION>` flag to specify the decimal precision to retain (selecting a lower number will create smaller files). The actual underlying values are stored as integers instead of floats so this is essentially [quantization](https://www.tensorflow.org/performance/quantization) for smaller model footprints.
- You can add an approximate nearest neighbors index to the file (increases size) with the `-a` flag which will enable the use of the `most_similar_approx` function. The `-t <TREES>` flag controls the number of trees in the approximate neigherest neighbors index (higher is more accurate) when used in conjunction with the `-a` flag (if not supplied, the number of trees is automatically determined).
- You can pass the `-s` flag to disable adding subword information to the file (which will make the file smaller), but disable advanced out-of-vocabulary key support.
- If converting a model that has no vocabulary like ELMo, you can pass the `-v` flag along with the path to another Magnitude file you would like to take the vocabulary from.

Optionally, you can bulk convert many files by passing an input folder and output folder instead of an input file and output file. All `.txt`, `.bin`, `.vec`, `.hdf5` files in the input folder will be converted to `.magnitude` files in the the output folder. The output folder must exist before a bulk conversion operation.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='837'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2726' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#remote-loading)Remote Loading

You can instruct Magnitude download and open a model from Magnitude's remote repository instead of a local file path. The file will automatically be downloaded locally on the first run to `~/.magnitude/` and subsequently skip the download if the file already exists locally.

vecs = Magnitude('http://magnitude.plasticity.ai/word2vec/heavy/GoogleNews-vectors-negative300.magnitude') # full url vecs = Magnitude('word2vec/heavy/GoogleNews-vectors-negative300') # or, use the shorthand for the url

For more control over the remote download domain and local download directory, see how to use [`MagnitudeUtils.download_model`](https://github.com/plasticityai/magnitude#utils).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='838'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2731' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#remote-streaming-over-http)Remote Streaming over HTTP

Magnitude models are generally large files (multiple GB) that take up a lot of disk space, even though the `.magnitude` format makes it fast to utilize the vectors. Magnitude has an option to stream these large files over HTTP. This is explicitly different from the [remote loading feature](https://github.com/plasticityai/magnitude#remote-loading), in that the model doesn't even need to be downloaded at all. You can begin querying models immediately with no disk space used at all.

vecs = Magnitude('http://magnitude.plasticity.ai/word2vec/heavy/GoogleNews-vectors-negative300.magnitude', stream=True) # full url vecs = Magnitude('word2vec/heavy/GoogleNews-vectors-negative300', stream=True) # or, use the shorthand for the url vecs.query("king") # Returns: the vector for "king" quickly, even with no local model file downloaded

You can play around with a demo of this in a [Google Colaboratory Python Notebook](https://colab.research.google.com/drive/1zkPhoNM1NvbTmEk9gr0Jnt8hONrca1Fv).

This feature is extremely useful if your computing environment is resource constrainted (low RAM and low disk space), you want to experiment quickly with vectors without downloading and setting up large model files, or you are training a small model. While there is some added network latency since the data is being streamed, Magnitude will still use an in-memory cache as specified by the [`lazy_loading`](https://github.com/plasticityai/magnitude#constructing-a-magnitude-object) constructor parameter. Since languages generally have a [Zipf-ian distribution](https://en.wikipedia.org/wiki/Zipf%27s_law), the network latency should largely not be an issue after the cache is warmed after being queried a small number of times.

They will be queried directly off a static HTTP web server using [HTTP Range Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests) headers. All Magnitude methods support streaming, however, `most_similar` and `most_similar_approx`may be slow as they are not optimized for streaming [yet](https://github.com/plasticityai/magnitude#roadmap). You can see how this streaming mode [performs currently in the benchmarks](https://github.com/plasticityai/magnitude#benchmarks-and-features), however, it will get faster as we [optimize it in the future](https://github.com/plasticityai/magnitude#roadmap)!

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='839'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2738' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#other-documentation)Other Documentation

Other documentation is not available at this time. See the source file directly (it is well commented) if you need more information about a method's arguments or want to see all supported features.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='840'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2741' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#other-languages)Other Languages

Currently, we only provide English word vector models on this page pre-converted to the `.magnitude` format. You can, however, still use Magnitude with word vectors of other languages. Facebook has trained their [fastText vectors for many different languages](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md). You can down the `.vec` file for any language you want and then convert it to `.magnitude` with the [converter](https://github.com/plasticityai/magnitude#file-format-and-converter).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='841'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2744' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#other-programming-languages)Other Programming Languages

Currently, reading Magnitude files is only supported in Python, since it has become the de-facto language for machine learning. This is sufficient for most use cases. Extending the file format to other languages shouldn't be difficult as SQLite has a native C implementation and has bindings in most languages. The file format itself and the protocol for reading and searching is also fairly straightforward upon reading the source code of this repository.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='842'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2747' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#other-domains)Other Domains

Currently, natural language processing is the most popular domain that uses pre-trained vector embedding models for word vector representations. There are, however, other domains like computer vision that have started using pre-trained vector embedding models like [Deep1B](https://github.com/arbabenko/GNOIMI) for image representation. This library intends to stay agnostic to various domains and instead provides a generic key-vector store and interface that is useful for all domains.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='843'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2750' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#contributing)Contributing

The main repository for this project can be found on [GitLab](https://gitlab.com/Plasticity/magnitude). The [GitHub repository](https://github.com/plasticityai/magnitude) is only a mirror. Pull requests for more tests, better error-checking, bug fixes, performance improvements, or documentation or adding additional utilties / functionalities are welcome on [GitLab](https://gitlab.com/Plasticity/magnitude).

You can contact us at [opensource@plasticity.ai](https://github.com/plasticityai/magnitudemailto:opensource@plasticity.ai).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='844'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2754' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#roadmap)Roadmap

- Speed optimizations on remote streaming and exposing stream cache configuration options
- Make `most_similar_approx` optimized for streaming
- In addition to the "Light", "Medium", and "Heavy" flavors, add a "Ludicrous" flavor that will be of an even larger file size but removes the constraint of the initially slow `most_similar` lookups.
- Add Google BERT support
- Support fastText `.bin` format

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='845'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2762' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#other-notable-projects)Other Notable Projects

- [spotify/annoy](https://github.com/spotify/annoy) - Powers the approximate nearest neighbors algorithm behind `most_similar_approx` in Magnitude using random-projection trees and hierarchical 2-means. Thanks to author [Erik Bernhardsson](https://github.com/erikbern) for helping out with some of the integration details between Magnitude and Annoy.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='846'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2766' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#citing-this-repository)Citing this Repository

If you'd like to [cite our paper at EMNLP 2018](http://aclweb.org/anthology/D18-2021), you can use the following BibTeX citation:

@inproceedings{patel2018magnitude,

title={Magnitude: A Fast, Efficient Universal Vector Embedding Utility Package},

author={Patel, Ajay and Sands, Alexander and Callison-Burch, Chris and Apidianaki, Marianna},

booktitle={Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},

pages={120--126},
year={2018}
}

or follow the [Google Scholar link](https://scholar.google.com/scholar?cluster=5916903042122216495&hl=en&as_sdt=0,5) for other ways to cite the paper.

If you'd like to cite this repository you can use the following DOI badge:  [![68747470733a2f2f7a656e6f646f2e6f72672f62616467652f3132323731353433322e737667](../_resources/04dbd7b5fa3f65b9fd97cdc8710e96e2.png)](https://zenodo.org/badge/latestdoi/122715432)

Clicking on the badge will lead to a page that will help you generate proper BibTeX citations, JSON-LD citations, and other citations.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='847'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2773' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/plasticityai/magnitude#license-and-attribution)LICENSE and Attribution

This repository is licensed under the license found [here](https://github.com/plasticityai/magnitude/blob/master/LICENSE.txt).

“[Seismic](https://thenounproject.com/ziman.jan/collection/weather/?i=1518266)” icon by JohnnyZi from the [Noun Project](https://thenounproject.com/).