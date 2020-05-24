Weights & Biases - Sudo Write Me a Program: GitHub Releases the ImageNet for Code

26
Sep
2019
/
Stacey Svetlichnaya, Deep Learning Engineer

# Sudo Write Me a Program: GitHub Releases the ImageNet for Code

TL;DR GitHub’s [CodeSearchNet](https://app.wandb.ai/github/CodeSearchNet/benchmark) provides large datasets, tools, and benchmarks via Weights & Biases to inspire and support broader community research on source code as a language (for semantic search, understanding, translation, & more) — you can [join this collaboration here](https://app.wandb.ai/github/CodeSearchNet/benchmark).

## Search by meaning not phrasing

Search engines have taught us how to ask for what we want: “lunch near me”, “salad mission open now”, and even “what’s a place nearby I can go for lunch today?” or just “food”, all show the best nearby restaurants, even in a non-English-speaking city. However, try a simple search for source code—or the right way to do something in a computer program, like “copy a file code”—and you’ll need to repeatedly scroll, skim, and evaluate options on different pages.  The syntax for a function, the right pattern in a new language you’re learning, a general problem-solving algorithm—such searches are crucial to efficient collaboration and a daily if not hourly task for software developers, but they require an annoying degree of precision in word choice (or many reformulations). Computers haven’t seen enough labeled examples to generalize from all the possible sequences of letters (“cp file1 file2”, “def copy(src, dest):…”, “private static void copyFile(File src, File dest) {...”) to the simple shared goal (copy a file). With 14 million annotated examples, [ImageNet](http://www.image-net.org/) famously enabled breakthroughs in object detection and image understanding. In the same spirit, GitHub’s CodeSearchNet project offers the training data and tools to accelerate research on semantic retrieval, understanding, and translation of source code.

## ImageNet for code

The CodeSearchNet corpus contains 6 million functions, 2 million of them documented, from open source projects on GitHub in 6 languages (Go, Java, JavaScript, PHP, Python, and Ruby). It can be downloaded raw from Amazon S3 or more conveniently accessed via Docker[as described in the main repository](https://github.com/github/CodeSearchNet). The Docker container includes the data preprocessing pipeline and a set of models leveraging [past work on semantic code search](https://github.blog/2018-09-18-towards-natural-language-semantic-code-search/). These examples learn to represent code and descriptive comments in a shared semantic (vector) space where similar meanings are closer together and different meanings are further apart. The available encoders range from baseline to state-of-the-art approaches: convolutional sequence, RNN, neural bag-of-words, and [BERT](https://arxiv.org/abs/1810.04805)-like self-attention (see[the research paper](https://arxiv.org/abs/1909.09436)for details). We hope these serve as useful starting points and inspiration to explore the latest advances in language learning like the [Transformer](https://openai.com/blog/better-language-models/) architecture.

## Collaborative benchmark for code retrieval

A large dataset and starter scripts are necessary but not sufficient to galvanize a research effort—as we’ve seen with ImageNet, this takes extensive community building through conference workshops, curated benchmarks, tool development and maintenance, yearly evaluation contests, etc. To support and structure future work, GitHub is launching the [CodeSearchNet Challenge, hosted by Weights & Biases (W&B)](https://app.wandb.ai/github/CodeSearchNet/benchmark). This benchmark tracks and compares models trained on the CodeSearchNet dataset by the global machine learning research community. The leaderboard evaluates submissions on code retrieval using an expert-labeled set of natural language queries with relevant code snippet results (i.e., given a query like “copy a file”, how relevant is this function on a scale from 0, totally irrelevant, to 3, exact match?). W&B makes collaborative deep learning easy for teams by organizing experiments and notes in a shared workspace, tracking all the code and hyperparameters, and visualizing results. Our Benchmarks feature enables such collaboration for open public projects, and we hope it lets CodeSearchNet participants coordinate all their efforts in one place and easily share and discuss workflows and insights.

## Leveling up developers

Software development is inherently self-automating: as coders notice themselves doing redundant manual tasks, they write an algorithm for them, and apply this at increasing levels of abstraction to build functions, classes, packages, APIs, integrations, and so on. Work-accelerating tools like find&replace and autocomplete evolve from custom macros and keyboard shortcuts to convenient buttons in modern development environments. This allows us to massively scale mental effort and replicate it on similar problems without re-solving them. What if we could automate not only the tedious tasks of looking up correct syntax or explaining mysterious error messages, but also the search for functions in a large new repository, without knowing any of the relevant keywords or even speaking the same language as the original developers? What if we could give program specifications in conversational style: “I’d like to order these files by timestamp and copy the newest one to a new directory”, “I’d like a small website where my friends can share reading recommendations”, “show me the best model on this dataset with the fewest parameters”, “retrain this base architecture with an extra residual layer after every major convolutional block and find the optimal learning rate”… ?

## Join the CodeSearchNet challenge

While this is only the beginning, the potential applications of semantic code understanding are vast. Immediate extensions of the current work include semantically parsing code in the encoder, quantifying code quality or clarity, inferring structure or control flow from repositories, and removing redundancy or recommending better abstractions to programmers. We invite you to contribute to this new frontier of developer tools by [joining the CodeSearchNet Challenge here](https://app.wandb.ai/github/CodeSearchNet/benchmark). You will see simple instructions to clone the repo, download the data, and train the baselines in a few commands. You can use the benchmark to see what others have tried, discuss ideas, and synthesize different approaches. GitHub plans to continue growing the CodeSearchNet dataset and tools see the [GitHub post](https://github.blog/2019-09-26-introducing-the-codesearchnet-challenge/)for details. We can’t wait to see what this community builds together.

Enter your email to get updates about new blog posts and feature updates.

# Weights & Biases

We're building lightweight, flexible experiment tracking tools for deep learning. Add a couple of lines to your python script, and we'll keep track of your hyperparameters and output metrics, making it easy to compare runs and see the whole history of your progress. Think of us like GitHub for deep learning.**

**

# Partner Program

We are building our library of deep learning articles, and we're delighted to feature the work of community members. [Contact Carey](https://www.wandb.com/articles/codesearchnetmailto:carey@wandb.com?subject=W%26B%20Partner%20Program) to learn about opportunities to share your research and insights.**

**
[Try our free tools for experiment tracking →](http://app.wandb.ai/)

Contact us at info@wandb.com       [Privacy Policy       ](https://www.wandb.com/privacy)[Terms of Service      ](https://www.wandb.com/terms) [Cookie Settings](https://www.wandb.com/articles/codesearchnet#)