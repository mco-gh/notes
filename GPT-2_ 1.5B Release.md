GPT-2: 1.5B Release

 [![](data:image/svg+xml,%3csvg id='openai-symbol' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 51 51' data-evernote-id='1012' class='js-evernote-checked'%3e%3cpath d='M47.21%2c20.92a12.65%2c12.65%2c0%2c0%2c0-1.09-10.38A12.78%2c12.78%2c0%2c0%2c0%2c32.36%2c4.41%2c12.82%2c12.82%2c0%2c0%2c0%2c10.64%2c9a12.65%2c12.65%2c0%2c0%2c0-8.45%2c6.13%2c12.78%2c12.78%2c0%2c0%2c0%2c1.57%2c15A12.64%2c12.64%2c0%2c0%2c0%2c4.84%2c40.51a12.79%2c12.79%2c0%2c0%2c0%2c13.77%2c6.13%2c12.65%2c12.65%2c0%2c0%2c0%2c9.53%2c4.25A12.8%2c12.8%2c0%2c0%2c0%2c40.34%2c42a12.66%2c12.66%2c0%2c0%2c0%2c8.45-6.13A12.8%2c12.8%2c0%2c0%2c0%2c47.21%2c20.92ZM28.14%2c47.57a9.46%2c9.46%2c0%2c0%2c1-6.08-2.2l.3-.17%2c10.1-5.83a1.68%2c1.68%2c0%2c0%2c0%2c.83-1.44V23.69l4.27%2c2.47a.15.15%2c0%2c0%2c1%2c.08.11v11.8A9.52%2c9.52%2c0%2c0%2c1%2c28.14%2c47.57ZM7.72%2c38.85a9.45%2c9.45%2c0%2c0%2c1-1.13-6.37l.3.18L17%2c38.49a1.63%2c1.63%2c0%2c0%2c0%2c1.65%2c0L31%2c31.37V36.3a.17.17%2c0%2c0%2c1-.07.13L20.7%2c42.33A9.51%2c9.51%2c0%2c0%2c1%2c7.72%2c38.85Zm-2.66-22a9.48%2c9.48%2c0%2c0%2c1%2c5-4.17v12a1.62%2c1.62%2c0%2c0%2c0%2c.82%2c1.43L23.17%2c33.2%2c18.9%2c35.67a.16.16%2c0%2c0%2c1-.15%2c0L8.54%2c29.78A9.52%2c9.52%2c0%2c0%2c1%2c5.06%2c16.8ZM40.14%2c25%2c27.81%2c17.84l4.26-2.46a.16.16%2c0%2c0%2c1%2c.15%2c0l10.21%2c5.9A9.5%2c9.5%2c0%2c0%2c1%2c41%2c38.41v-12A1.67%2c1.67%2c0%2c0%2c0%2c40.14%2c25Zm4.25-6.39-.3-.18L34%2c12.55a1.64%2c1.64%2c0%2c0%2c0-1.66%2c0L20%2c19.67V14.74a.14.14%2c0%2c0%2c1%2c.06-.13L30.27%2c8.72a9.51%2c9.51%2c0%2c0%2c1%2c14.12%2c9.85ZM17.67%2c27.35%2c13.4%2c24.89a.17.17%2c0%2c0%2c1-.08-.12V13a9.51%2c9.51%2c0%2c0%2c1%2c15.59-7.3l-.3.17-10.1%2c5.83a1.68%2c1.68%2c0%2c0%2c0-.83%2c1.44Zm2.32-5%2c5.5-3.17L31%2c22.35v6.34l-5.49%2c3.17L20%2c28.69Z' data-evernote-id='1013' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://openai.com/)

- [About](https://openai.com/about/)

- [Progress](https://openai.com/progress/)

- [Resources](https://openai.com/resources/)

- [Blog](https://openai.com/blog/)

* * *

 November 5, 2019 • 4 minute read

# GPT-2: 1.5B Release

As the final model release of [GPT-2](https://openai.com/blog/better-language-models/)’s [staged release](https://openai.com/blog/gpt-2-6-month-follow-up/), we’re releasing the largest version (1.5B parameters) of GPT-2 along with [code and model weights](https://github.com/openai/gpt-2-output-dataset) to facilitate detection of outputs of GPT-2 models. While there have been larger language models released since August, we’ve continued with our original staged release plan in order to provide the community with a test case of a full staged release process. We hope that this test case will be useful to developers of future powerful models, and we’re actively continuing the conversation with the AI community on responsible publication.

 [Report](https://d4mucfpksywv.cloudfront.net/papers/GPT_2_Report.pdf)  [GPT-2 Model](https://github.com/openai/gpt-2)  [Detector Model](https://github.com/openai/gpt-2-output-dataset/tree/master/detector)  [Model Card](https://github.com/openai/gpt-2/blob/master/model_card.md)

## Our findings

**1. Humans find GPT-2 outputs convincing.** Our partners at Cornell University surveyed people to assign GPT-2 text a credibility score across model sizes. People gave the 1.5B model a “credibility score” of 6.91 out of 10. This is marginally greater than outputs from the 774M model (6.72) and significantly above the medium 355M model (6.07). These results make us more inclined to release the 1.5B model, as the incremental increase in human-perceived credibility relative to 774M seems low.

**2. GPT-2 can be fine-tuned for misuse.** Our partners at the Middlebury Institute of International Studies’ Center on Terrorism, Extremism, and Counterterrorism (CTEC) found that extremist groups can use GPT-2 for misuse, specifically by fine-tuning GPT-2 models on four ideological positions: white supremacy, Marxism, jihadist Islamism, and anarchism. CTEC demonstrated that it’s possible to create models that can generate synthetic propaganda for these ideologies. They also show that, despite having low detection accuracy on synthetic outputs, ML-based detection methods can give experts reasonable suspicion that an actor is generating synthetic text.

**3. Detection is challenging.** We expect that content-based detection of synthetic text is a long-term challenge. To test whether machine learning approaches may help today, we conducted in-house detection research and developed a [detection model](https://github.com/openai/gpt-2-output-dataset) that has detection rates of ~95% for detecting 1.5B GPT-2-generated text.[[1]](https://openai.com/blog/gpt-2-1-5b-release/#fn1)

Specifically, we based a sequence classifier on RoBERTaBASE (125 million parameters) and RoBERTaLARGE (355 million parameters) and fine-tuned it to classify the outputs from the 1.5B GPT-2 model versus WebText, the dataset we used to train the GPT-2 model.

We believe this is not high enough accuracy for standalone detection and needs to be paired with metadata-based approaches, human judgment, and public education to be more effective. We are releasing this model to aid the study of research into the detection of synthetic text, although this does let adversaries with access better evade detection.

While we found detection accuracy depends heavily on the sampling methods used in training and testing, we also found detection to be more reliable when training across a range of sampling techniques. As seen in the figure below, we observed that larger models’ outputs are more difficult to classify, but training on larger models’ outputs makes detection results more accurate and robust. We expect this trend to continue and that detection will be more challenging with increased model size.

##### Transferred model accuracy (nucleus samples)

| Trained on down | Tested on right<br>Small (124M) | Medium (355M) | Large (774M) | XL (1.5B) |
| --- | --- | --- | --- | --- |
| Small (124M) | 99.3% | 96.6% | 90.9% | 79.3% |
| Medium (355M) | 99.0% | 98.5% | 96.9% | 91.8% |
| Large (774M) | 98.4% | 97.9% | 97.9% | 95.7% |
| XL (1.5B) | 96.9% | 96.7% | 96.6% | 96.0% |

**4. We’ve seen no strong evidence of misuse so far.** While we’ve seen some discussion around GPT-2’s potential to augment high-volume/low-yield operations like spam and phishing, we haven’t seen evidence of writing code, documentation, or instances of misuse. We think synthetic text generators have a higher chance of being misused if their outputs become more reliable and coherent. We acknowledge that we cannot be aware of all threats, and that motivated actors can replicate language models without model release.

**5. We need standards for studying bias.** Language models have biases. Working out how to study these biases, discuss them, and address them, is a challenge for the AI research community. We’ve approached the challenge of bias in two ways:

- •Publishing a [model card](https://github.com/openai/gpt-2/blob/master/model_card.md)[[2]](https://openai.com/blog/gpt-2-1-5b-release/#fn2)

Which we’ve based on “[Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)” by Mitchell et al.

alongside our models on GitHub to give people a sense of the issues inherent to language models such as GPT-2.

- •Performing a qualitative, in-house evaluation of some of the biases in GPT-2: We probed GPT-2 for some gender, race, and religious biases, using those findings to inform our model card. These probes are not comprehensive and raise the need for collaboration on bias analysis frameworks.

## Next Steps

Our experience with GPT-2 over the past 9 months has given us valuable insight into the challenges and opportunities for creating responsible publication norms in AI. We’re continuing our work on this issue via participation in the Partnership on AI’s “Responsible Publication Norms for Machine Learning” project and discussions with our colleagues in the research community.

*If you’d like to develop large-scale AI systems and think about their implications, [we’re hiring](https://openai.com/jobs/).*

* * *

Footnotes
1. 1.

Specifically, we based a sequence classifier on RoBERTaBASE (125 million parameters) and RoBERTaLARGE (355 million parameters) and fine-tuned it to classify the outputs from the 1.5B GPT-2 model versus WebText, the dataset we used to train the GPT-2 model. [↩︎](https://openai.com/blog/gpt-2-1-5b-release/#fnref1)

2. 2.

Which we’ve based on “[Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)” by Mitchell et al. [↩︎](https://openai.com/blog/gpt-2-1-5b-release/#fnref2)

* * *

Authors

 [Irene Solaiman](https://openai.com/blog/authors/irene/), [Jack Clark](https://openai.com/blog/authors/jack-clark/) & [Miles Brundage](https://openai.com/blog/authors/miles/)

* * *

Acknowledgments

Thanks to the following for feedback on this post: Greg Brockman, Jeffrey Wu, Alec Radford, Jong Wook Kim, Gretchen Krueger, Alex Newhouse, Jason Blazakis, Sarah Kreps, Miles McCain, Cody Wild, Mona Wang, Jeremy Gillula, Larissa Schiavo, Aviv Ovadya, Rebecca Crootof