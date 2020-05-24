github/CodeSearchNet

[![](../_resources/933e2514a2a971e9872ea33bd0a5113d.png)](https://github.com/github/CodeSearchNet/workflows/Smoke%20Test/badge.svg)[![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667](../_resources/9b5aed7d8c8503fa4c7c77c8bdabf941.png)](https://opensource.org/licenses/MIT)  [![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e362d626c75652e737667](../_resources/c22ff1c8093a9ab63c150bde7cad3276.png)](https://www.python.org/downloads/release/python-360/)[![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f57656967687473253230262532304269617365732d626c61636b2e7376673f6c6f676f3d676f6f676c652d616e616c7974696373](../_resources/8e8dc33ecabdd3d6821f8d6c24fdbea2.png)](https://app.wandb.ai/github/CodeSearchNet/benchmark)

**Table of Contents**

- [Quickstart](https://github.com/github/CodeSearchNet#quickstart)
- [Introduction](https://github.com/github/CodeSearchNet#introduction)
    - [Project Overview](https://github.com/github/CodeSearchNet#project-overview)
    - [Data](https://github.com/github/CodeSearchNet#data)
    - [Evaluation](https://github.com/github/CodeSearchNet#evaluation)
        - [Annotations](https://github.com/github/CodeSearchNet#annotations)
    - [Setup](https://github.com/github/CodeSearchNet#setup)
- [Data Details](https://github.com/github/CodeSearchNet#data-details)
    - [Data Acquisition](https://github.com/github/CodeSearchNet#data-acquisition)
    - [Schema & Format](https://github.com/github/CodeSearchNet#schema-format)
    - [Downloading Data from S3](https://github.com/github/CodeSearchNet#downloading-data-from-s3)
- [Running our Baseline Model](https://github.com/github/CodeSearchNet#running-our-baseline-model)
    - [Model Architecture](https://github.com/github/CodeSearchNet#model-architecture)
    - [Training](https://github.com/github/CodeSearchNet#training)
- [References](https://github.com/github/CodeSearchNet#references)
    - [Benchmark](https://github.com/github/CodeSearchNet#benchmark)
    - [How to Contribute](https://github.com/github/CodeSearchNet#how-to-contribute)
    - [Other READMEs](https://github.com/github/CodeSearchNet#other-readmes)
    - [W&B Setup](https://github.com/github/CodeSearchNet#wb-setup)
    - [Licenses](https://github.com/github/CodeSearchNet#licenses)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='72'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1037' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#quickstart)Quickstart

**If this is your first time reading this, we recommend skipping this section and reading the following sections.** The below commands assume you have [Docker](https://docs.docker.com/get-started/) and [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker), as well as a GPU that supports [CUDA 9.0](https://developer.nvidia.com/cuda-90-download-archive) or greater. Note: you should only have to run `script/setup` once to download the data.

# clone this repositorygit clone https://github.com/github/CodeSearchNet.gitcd CodeSearchNet/# download data (~3.5GB) from S3; build and run the Docker containerscript/setup# this will drop you into the shell inside a Docker containerscript/console# optional: log in to W&B to see your training metrics,# track your experiments, and submit your models to the benchmarkwandb login# verify your setup by training a tiny modelpython train.py --testrun# see other command line options, try a full training run with default values,# and explore other model variants by extending this baseline scriptpython train.py --help

python train.py# generate predictions for model evaluationpython predict.py -r github/CodeSearchNet/0123456 # this is the org/project_name/run_id

Finally, you can submit your run to the [community benchmark](https://app.wandb.ai/github/CodeSearchNet/benchmark) by following these [instructions](https://github.com/github/CodeSearchNet/blob/master/BENCHMARK.md).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='73'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1041' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#introduction)Introduction

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='74'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1043' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#project-overview)Project Overview

[CodeSearchNet](https://arxiv.org/abs/1909.09436) is a collection of datasets and benchmarks that explore the problem of code retrieval using natural language. This research is a continuation of some ideas presented in this [blog post](https://githubengineering.com/towards-natural-language-semantic-code-search/) and is a joint collaboration between GitHub and the [Deep Program Understanding](https://www.microsoft.com/en-us/research/project/program/) group at [Microsoft Research - Cambridge](https://www.microsoft.com/en-us/research/lab/microsoft-research-cambridge/). We aim to provide a platform for community research on semantic code search via the following:

1. Instructions for obtaining large corpora of relevant data

2. Open source code for a range of baseline models, along with pre-trained weights

3. Baseline evaluation metrics and utilities

4. Mechanisms to track progress on a [shared community benchmark](https://app.wandb.ai/github/CodeSearchNet/benchmark) hosted by [Weights & Biases](https://www.wandb.com/)

We hope that CodeSearchNet is a step towards engaging with the broader machine learning and NLP community regarding the relationship between source code and natural language. We describe a specific task here, but we expect and welcome other uses of our dataset.

More context regarding the motivation for this problem is in this [technical report](https://arxiv.org/abs/1909.09436).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='75'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1053' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#data)Data

The primary dataset consists of 2 million (`comment`, `code`) pairs from open source libraries. Concretely, a `comment` is a top-level function or method comment (e.g. [docstrings](https://en.wikipedia.org/wiki/Docstring) in Python), and `code` is an entire function or method. Currently, the dataset contains Python, Javascript, Ruby, Go, Java, and PHP code. Throughout this repo, we refer to the terms docstring and query interchangeably. We partition the data into train, validation, and test splits such that code from the same repository can only exist in one partition. Currently this is the only dataset on which we train our model. Summary statistics about this dataset can be found in [this notebook](https://github.com/github/CodeSearchNet/blob/master/notebooks/ExploreData.ipynb)

For more information about how to obtain the data, see [this section](https://github.com/github/CodeSearchNet#data-details).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1057' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#evaluation)Evaluation

The metric we use for evaluation is [Normalized Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG). Please reference [this paper](https://arxiv.org/abs/1909.09436) for further details regarding model evaluation.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='77'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1060' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#annotations)Annotations

We manually annotated retrieval results for the six languages from 99 general [queries](https://github.com/github/CodeSearchNet/blob/master/resources/queries.csv). This dataset is used as groundtruth data for evaluation *only*. Please refer to [this paper](https://arxiv.org/abs/1909.09436) for further details on the annotation process.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='78'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1064' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#setup)Setup

You should only have to perform the setup steps once to download the data and prepare the environment.

1. Due to the complexity of installing all dependencies, we prepared Docker containers to run this code. You can find instructions on how to install Docker in the [official docs](https://docs.docker.com/get-started/). Additionally, you must install [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker) to satisfy GPU-compute related dependencies. For those who are new to Docker, this [blog post](https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5) provides a gentle introduction focused on data science.

2. After installing Docker, you need to download the pre-processed datasets, which are hosted on S3. You can do this by running `script/setup`.

	script/setup

This will build Docker containers and download the datasets. By default, the data is downloaded into the `resources/data/` folder inside this repository, with the directory structure described [here](https://github.com/github/CodeSearchNet/blob/master/resources/README.md).

**The datasets you will download (most of them compressed) have a combined size of only ~ 3.5 GB.**

1. To start the Docker container, run `script/console`:

	script/console

This will land you inside the Docker container, starting in the `/src` directory. You can detach from/attach to this container to pause/continue your work.

For more about the data, see [Data Details](https://github.com/github/CodeSearchNet#data-details) below, as well as [this notebook](https://github.com/github/CodeSearchNet/blob/master/notebooks/ExploreData.ipynb).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='79'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1076' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#data-details)Data Details

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='80'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1078' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#data-acquisition)Data Acquisition

If you have run the [setup steps](https://github.com/github/CodeSearchNet#setup) above you will already have the data, and nothing more needs to be done. The data will be available in the `/resources/data` folder of this repository, with [this directory structure](https://github.com/github/CodeSearchNet/blob/master/resources/README.md).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='81'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1081' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#schema--format)Schema & Format

Data is stored in [jsonlines](http://jsonlines.org/) format. Each line in the uncompressed file represents one example (usually a function with an associated comment). A prettified example of one row is illustrated below.

- **repo:** the owner/repo
- **path:** the full path to the original file
- **func_name:** the function or method name
- **original_string:** the raw string before tokenization or parsing
- **language:** the programming language
- **code:** the part of the `original_string` that is code
- **code_tokens:** tokenized version of `code`
- **docstring:** the top-level comment or docstring, if it exists in the original string
- **docstring_tokens:** tokenized version of `docstring`
- **sha:** this field is not being used [TODO: add note on where this comes from?]
- **partition:** a flag indicating what partition this datum belongs to of {train, valid, test, etc.} This is not used by the model. Instead we rely on directory structure to denote the partition of the data.
- **url:** the url for the code snippet including the line numbers

Code, comments, and docstrings are extracted in a language-specific manner, removing artifacts of that language.

	{
	  'code': 'def get_vid_from_url(url):\n'
	          '        """Extracts video ID from URL.\n'
	          '        """\n'
	          "        return match1(url, r'youtu\\.be/([^?/]+)') or \\\n"
	          "          match1(url, r'youtube\\.com/embed/([^/?]+)') or \\\n"
	          "          match1(url, r'youtube\\.com/v/([^/?]+)') or \\\n"
	          "          match1(url, r'youtube\\.com/watch/([^/?]+)') or \\\n"
	          "          parse_query_param(url, 'v') or \\\n"
	          "          parse_query_param(parse_query_param(url, 'u'), 'v')",
	  'code_tokens': ['def',
	                  'get_vid_from_url',
	                  '(',
	                  'url',
	                  ')',
	                  ':',
	                  'return',
	                  'match1',
	                  '(',
	                  'url',
	                  ',',
	                  "r'youtu\\.be/([^?/]+)'",
	                  ')',
	                  'or',
	                  'match1',
	                  '(',
	                  'url',
	                  ',',
	                  "r'youtube\\.com/embed/([^/?]+)'",
	                  ')',
	                  'or',
	                  'match1',
	                  '(',
	                  'url',
	                  ',',
	                  "r'youtube\\.com/v/([^/?]+)'",
	                  ')',
	                  'or',
	                  'match1',
	                  '(',
	                  'url',
	                  ',',
	                  "r'youtube\\.com/watch/([^/?]+)'",
	                  ')',
	                  'or',
	                  'parse_query_param',
	                  '(',
	                  'url',
	                  ',',
	                  "'v'",
	                  ')',
	                  'or',
	                  'parse_query_param',
	                  '(',
	                  'parse_query_param',
	                  '(',
	                  'url',
	                  ',',
	                  "'u'",
	                  ')',
	                  ',',
	                  "'v'",
	                  ')'],
	  'docstring': 'Extracts video ID from URL.',
	  'docstring_tokens': ['Extracts', 'video', 'ID', 'from', 'URL', '.'],
	  'func_name': 'YouTube.get_vid_from_url',
	  'language': 'python',
	  'original_string': 'def get_vid_from_url(url):\n'
	                      '        """Extracts video ID from URL.\n'
	                      '        """\n'
	                      "        return match1(url, r'youtu\\.be/([^?/]+)') or \\\n"
	                      "          match1(url, r'youtube\\.com/embed/([^/?]+)') or "
	                      '\\\n'
	                      "          match1(url, r'youtube\\.com/v/([^/?]+)') or \\\n"
	                      "          match1(url, r'youtube\\.com/watch/([^/?]+)') or "
	                      '\\\n'
	                      "          parse_query_param(url, 'v') or \\\n"
	                      "          parse_query_param(parse_query_param(url, 'u'), "
	                      "'v')",
	  'partition': 'test',
	  'path': 'src/you_get/extractors/youtube.py',
	  'repo': 'soimort/you-get',
	  'sha': 'b746ac01c9f39de94cac2d56f665285b0523b974',
	  'url': 'https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/youtube.py#L135-L143'
	}

Summary statistics such as row counts and token length histograms can be found in [this notebook](https://github.com/github/CodeSearchNet/blob/master/notebooks/ExploreData.ipynb)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='82'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1099' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#downloading-data-from-s3)Downloading Data from S3

The shell script `/script/setup` will automatically download these files into the `/resources/data` directory. Here are the links to the relevant files for visibility:

The s3 links follow this pattern:

> [> https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/{python,java,go,php,javascript,ruby}.zip](https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/%7Bpython,java,go,php,javascript,ruby%7D.zip)

For example, the link for the `java` is:
> [https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/java.zip

The size of the dataset is approximately 20 GB. The various files and the directory structure are explained [here](https://github.com/github/CodeSearchNet/blob/master/resources/README.md).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='83'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1108' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#running-our-baseline-model)Running Our Baseline Model

We encourage you to reproduce and extend these models, though most variants take several hours to train (and some take more than 24 hours on an [AWS P3-V100](https://aws.amazon.com/ec2/instance-types/p3/) instance).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='84'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1111' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#model-architecture)Model Architecture

Our baseline models ingest a parallel corpus of (`comments`, `code`) and learn to retrieve a code snippet given a natural language query. Specifically, `comments` are top-level function and method comments (e.g. docstrings in Python), and `code` is an entire function or method. Throughout this repo, we refer to the terms docstring and query interchangeably.

The query has a single encoder, whereas each programming language has its own encoder. The available encoders are Neural-Bag-Of-Words, RNN, 1D-CNN, Self-Attention (BERT), and a 1D-CNN+Self-Attention Hybrid.

The diagram below illustrates the general architecture of our baseline models:

[![architecture.png](../_resources/eb24c7324330266d4f3d7ea743f382c2.png)](https://github.com/github/CodeSearchNet/blob/master/images/architecture.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='85'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1117' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#training)Training

This step assumes that you have a suitable Nvidia-GPU with [Cuda v9.0](https://developer.nvidia.com/cuda-90-download-archive) installed. We used [AWS P3-V100](https://aws.amazon.com/ec2/instance-types/p3/) instances (a `p3.2xlarge` is sufficient).

1. Start the model run environment by running `script/console`:

	script/console

This will drop you into the shell of a Docker container with all necessary dependencies installed, including the code in this repository, along with data that you downloaded earlier. By default, you will be placed in the `src/` folder of this GitHub repository. From here you can execute commands to run the model.

2. Set up [W&B](https://docs.wandb.com/docs/started.html) (free for open source projects) [per the instructions below](https://github.com/github/CodeSearchNet#wb-setup) if you would like to share your results on the community benchmark. This is optional but highly recommended.

3. The entry point to this model is `src/train.py`. You can see various options by executing the following command:

	python train.py --help

To test if everything is working on a small dataset, you can run the following command:

	python train.py --testrun

4. Now you are prepared for a full training run. Example commands to kick off training runs:

- Training a neural-bag-of-words model on all languages

	python train.py --model neuralbow

The above command will assume default values for the location(s) of the training data and a destination where you would like to save the output model. The default location for training data is specified in `/src/data_dirs_{train,valid,test}.txt`. These files each contain a list of paths where data for the corresponding partition exists. If more than one path specified (separated by a newline), the data from all the paths will be concatenated together. For example, this is the content of `src/data_dirs_train.txt`:

	$ cat data_dirs_train.txt
	../resources/data/python/final/jsonl/train
	../resources/data/javascript/final/jsonl/train
	../resources/data/java/final/jsonl/train
	../resources/data/php/final/jsonl/train
	../resources/data/ruby/final/jsonl/train
	../resources/data/go/final/jsonl/train

By default, models are saved in the `resources/saved_models` folder of this repository.

- Training a 1D-CNN model on Python data only:

	python train.py --model 1dcnn /trained_models ../resources/data/python/final/jsonl/train ../resources/data/python/final/jsonl/valid ../resources/data/python/final/jsonl/test

The above command overrides the default locations for saving the model to `trained_models` and also overrides the source of the train, validation, and test sets.

Additional notes:

- Options for `--model` are currently listed in `src/model_restore_helper.get_model_class_from_name`.
- Hyperparameters are specific to the respective model/encoder classes. A simple trick to discover them is to kick off a run without specifying hyperparameter choices, as that will print a list of all used hyperparameters with their default values (in JSON format).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='86'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1144' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#references)References

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='87'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1146' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#benchmark)Benchmark

We are using a community benchmark for this project to encourage collaboration and improve reproducibility. It is hosted by [Weights & Biases](https://www.wandb.com/) (W&B), which is free for open source projects. Our entries in the benchmark link to detailed logs of our training and evaluation metrics, as well as model artifacts, and we encourage other participants to provide as much detail as possible.

We invite the community to submit their runs to this benchmark to facilitate transparency by following [these instructions](https://github.com/github/CodeSearchNet/blob/master/BENCHMARK.md).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='88'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1150' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#how-to-contribute)How to Contribute

We anticipate that the community will design custom architectures and use frameworks other than Tensorflow. Furthermore, we anticipate that additional datasets will be useful. It is not our intention to integrate these models, approaches, and datasets into this repository as a superset of all available ideas. Rather, we intend to maintain the baseline models and links to the data in this repository as a central place of reference. We are accepting PRs that update the documentation, link to your project(s) with improved benchmarks, fix bugs, or make minor improvements to the code. Here are [more specific guidelines for contributing to this repository](https://github.com/github/CodeSearchNet/blob/master/CONTRIBUTING.md); note particularly our [Code of Conduct](https://github.com/github/CodeSearchNet/blob/master/CODE_OF_CONDUCT.md). Please open an issue if you are unsure of the best course of action.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='89'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1153' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#other-readmes)Other READMEs

- [Submitting to the benchmark](https://github.com/github/CodeSearchNet/blob/master/BENCHMARK.md)
- [Data structure](https://github.com/github/CodeSearchNet/blob/master/resources/README.md)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='90'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1158' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#wb-setup)W&B Setup

To initialize W&B:
1. Navigate to the `/src` directory in this repository.
2. If it's your first time using W&B on a machine, you will need to log in:

	$ wandb login

3. You will be asked for your API key, which appears on your [W&B profile settings page](https://app.wandb.ai/settings).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='91'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1168' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/github/CodeSearchNet#licenses)Licenses

The licenses for source code used as data for this project are provided with the [data download](https://github.com/github/CodeSearchNet#downloading-data-from-s3) for each language in `_licenses.pkl`  [files](https://github.com/github/CodeSearchNet/blob/master/resources/README.md#directory-structure).

This code and documentation for this project are released under the [MIT License](https://github.com/github/CodeSearchNet/blob/master/LICENSE).