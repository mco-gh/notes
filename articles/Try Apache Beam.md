Try Apache Beam

# Try Apache Beam

You can try Apache Beam using our interactive notebooks, which are hosted in [Colab](https://colab.research.google.com/). The notebooks allow you to interactively play with the code and see how your changes affect the pipeline. You don’t need to install anything or modify your computer in any way to use these notebooks.

 **Adapt for:**

- Java SDK

- Python SDK

- Go SDK

## Interactive WordCount in Colab

This interactive notebook shows you what a simple, minimal version of WordCount looks like.

- [Python]()

	import apache_beam as beam
	import re

	inputs_pattern = 'data/*'
	outputs_prefix = 'outputs/part'

	with beam.Pipeline() as pipeline:
	  (
	      pipeline
	      | 'Read lines' >> beam.io.ReadFromText(inputs_pattern)
	      | 'Find words' >> beam.FlatMap(lambda line: re.findall(r"[a-zA-Z']+", line))
	      | 'Pair words with 1' >> beam.Map(lambda word: (word, 1))
	      | 'Group and sum' >> beam.CombinePerKey(sum)
	      | 'Format results' >> beam.Map(lambda word_count: str(word_count))
	      | 'Write results' >> beam.io.WriteToText(outputs_prefix)
	  )

[Run in Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/get-started/try-apache-beam-py.ipynb)[View on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/get-started/try-apache-beam-py.ipynb)

To learn how to install and run the Apache Beam Python SDK on your own computer, follow the instructions in the [Python Quickstart](https://beam.apache.org/get-started/quickstart-py).

For a more detailed explanation about how WordCount works, see the [WordCount Example Walkthrough](https://beam.apache.org/get-started/wordcount-example).

## Next Steps

- Walk through additional WordCount examples in the [WordCount Example Walkthrough](https://beam.apache.org/get-started/wordcount-example).

- Take a self-paced tour through our [Learning Resources](https://beam.apache.org/documentation/resources/learning-resources).

- Dive in to some of our favorite [Videos and Podcasts](https://beam.apache.org/documentation/resources/videos-and-podcasts).

- Join the Beam [users@](https://beam.apache.org/community/contact-us) mailing list.

- If you’re interested in contributing to the Apache Beam codebase, see the [Contribution Guide](https://beam.apache.org/contribute).

Please don’t hesitate to [reach out](https://beam.apache.org/community/contact-us) if you encounter any issues!