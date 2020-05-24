minimaxir/download-tweets-ai-text-gen: Python script to download public Tweets from a given Twitter account into a format suitable for AI text generation.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='95'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='821' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#download-tweets-ai-text-gen)download-tweets-ai-text-gen

A small Python 3 script to download public Tweets from a given Twitter account into a format suitable for AI text generation tools (such as [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) for finetuning [GPT-2](https://openai.com/blog/better-language-models/)).

- Retrieves all tweets as a simple CSV with a single CLI command.
- Preprocesses tweets to remove URLs, extra spaces, and optionally usertags/hashtags.
- Saves tweets in batches (i.e. there is an error or you want to end collection early)

You can view examples of AI-generated tweets from datasets retrieved with this tool in the `/examples` folder.

Inspired by popular demand due to the success of [@dril_gpt2](https://twitter.com/dril_gpt2).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='96'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='830' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#usage)Usage

First, install the Python script dependencies:
pip3 install twint==2.1.4 fire tqdm
Then download the `download_tweets.py` script from this repo.

The script is interacted via a command line interface. After `cd`ing into the directory where the script is stored in a terminal, run:

python3 download_tweets.py <twitter_username>

e.g. If you want to download all tweets (sans retweets/replies/quote tweets) from Twitter user [@dril](https://twitter.com/dril_gpt2), run:

python3 download_tweets.py dril

The tweets will be downloaded to a single-column CSV titled `<username>_tweets.csv`.

The parameters you can pass to the command line interface (positionally or explicitly) are:

- username: Username of the account whose tweets you want to download [required]
- limit: Number of tweets to download [default: all tweets possible]
- include_replies: Include replies from the user in the dataset [default: False]
- strip_usertags: Strips out `@` user tags in the tweet text [default: False]
- strip_hashtags: Strips out `#` hashtags in the tweet text [default: False]

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='97'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='847' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#how-to-train-an-ai-on-the-downloaded-tweets)How to Train an AI on the downloaded tweets

[gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) has a special case for single-column CSVs, where it will automatically process the text for best training and generation. (i.e. by adding `<|startoftext|>` and `<|endoftext|>` to each tweet, allowing independent generation of tweets)

You can use [this Colaboratory notebook](https://colab.research.google.com/drive/1qxcQ2A1nNjFudAGN_mcMOnvV9sF_PkEb) (optimized from the original notebook for this use case) to train the model on your downloaded tweets, and generate massive amounts of Tweets from it. Note that without a lot of data, the model might easily overfit; you may want to train for fewer `steps` (e.g. `500`).

When generating, you'll always need to include certain parameters to decode the tweets, e.g.:

gpt2.generate(sess, length=200, temperature=0.7, prefix='<|startoftext|>', truncate='<|endoftext|>', include_prefix=False )

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='98'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='853' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#helpful-notes)Helpful Notes

- Retweets are not included in the downloaded dataset. (which is generally a good thing)
- You'll need *thousands* of tweets at minimum to feed to the input model for a good generation results. (ideally 1 MB of input text data, although with tweets that hard to achieve)
- The download will likely end much earlier than the theoetical limit (inferred from the user profile) as the limit includes retweets/replies/whatever cache shennanigans Twitter is employing.
- When downloading the tweets, you may hit a `Expecting value: line 1 column 1 (char 0) [x] run.Feed` warning in the terminal; it should be safe to ignore (there isn't a good way to surpress it unfortunately).
- The legalities of distributing downloaded tweets is ambigious, therefore it's recommended avoiding commiting raw Twitter data to GitHub, and is the reason examples of such data is not included in this repo. (AI-generated tweets themselves likely fall under derivative work/parody protected by Fair Use)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='99'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='862' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#maintainercreator)Maintainer/Creator

Max Woolf ([@minimaxir](https://minimaxir.com/))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir) and [GitHub Sponsors](https://github.com/sponsors/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='100'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='867' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#license)License

MIT

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='101'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='870' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/minimaxir/download-tweets-ai-text-gen#disclaimer)Disclaimer

This repo has no affiliation with Twitter Inc.