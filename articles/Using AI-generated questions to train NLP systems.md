Using AI-generated questions to train NLP systems

[Research](https://ai.facebook.com/blog/results/research/)|
[Open Source](https://ai.facebook.com/blog/results/open-source/)

# Using AI-generated questions to train NLP systems

September 20, 2019

Share

[ ![49634112_369201477192293_9127330224449519616_n.png](../_resources/80b4ce80909efba0304d88969ac5f873.png)  ![49661799_326312694636292_7293370538993385472_n.png](../_resources/544005436f43d734b3e9cdfb46eb3ed0.png)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fai.facebook.com%2Fblog%2Fresearch-in-brief-unsupervised-question-answering-by-cloze-translation%2F)

[ ![49677251_224845165108670_5875028237406437376_n.png](../_resources/b166a0e4487b7d111bd20a0038c00760.png)  ![49780062_2239882272955938_7957149939224543232_n.png](../_resources/54b6ddfc9eae9f62c96d2b8254543cf7.png)](https://l.facebook.com/l.php?u=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Ftext%3DUsing%2BAI-generated%2Bquestions%2Bto%2Btrain%2BNLP%2Bsystems%2Bhttps%253A%252F%252Fai.facebook.com%252Fblog%252Fresearch-in-brief-unsupervised-question-answering-by-cloze-translation%252F&h=AT2oSUALLEy5RMmaAe1smRzgvmDrI3FzxL9JRkVgm5FRJQ6fWBZOIM7x34CseRUBFdw5HJLp8RkCSlY4MC2qp-8knRMLcrLnL2m39peZYD_YekGNdeMwwSOSsiRrUCmSyCSXBh-wpnI8i28FZLlD6D7JxCI)

### **What the research is:**

A recent approach to the popular extractive question answering (extractive QA) task that generates its own training data instead of requiring existing annotated question answering examples. Extractive QA is a popular task for natural language processing (NLP) research, where models must extract a short snippet from a document in order to answer a natural language question. Though supervised models perform well at extractive QA, they require thousands — sometimes hundreds of thousands — of annotated examples for training, and their performance suffers when tested outside of the textual domains and language they were trained on. By approaching extractive QA as a self-supervised task, our technique outperformed early supervised models on the widely used SQuAD data set while requiring no annotated question answering training data. The code for our method is now [available to download](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebookresearch%2FUnsupervisedQA&h=AT2Pc1bXXAbGHOnI5fU7VpBWi42txu4C0b4wC4pJM2LIsrlpy0XDOkqueKxF1x5z6NMKrPLYEcXaBVto5MMnl76XJHEowHylEnTUahYzGkdUDLm5UvYBfEGnyZAG7KkW_6XPfs0NZ6_k3AeI96JxpWqmSLw).

### **How it works:**

Our two-step method starts by training a model to create fill-in-the-blank (also referred to as cloze) questions from sample documents. This generation pipeline consists of first identifying potential answers from text, then formulating a cloze question, and finally reframing that question in natural language. For example, the model could be presented with this text:

*The Broncos took an early lead in Super Bowl 50 and never trailed. [...] Denver linebacker Von Miller was named Super Bowl MVP, recording five solo tackles, two and a half sacks, and two forced fumbles.*

The system might first identify “Broncos,” “Denver” or various numbers (such as “five” and “two”) as probable answers. For the answer “Broncos,” the model would create the cloze question “The _____ took an early lead in Super Bowl 50 and never trailed,” followed by a final, non-cloze version of the question: “Who took an early lead in Super Bowl 50?”

In our method’s second step, we take a standard extractive QA model architecture, which usually requires human-annotated QA data to train on, and instead train it with data from our question-generating model. To evaluate our approach, we measured the resulting model’s performance on test data from the SQuAD benchmark and found that it scored 56.4 F1, beating an early supervised model.

### **Why it matters:**

Our results demonstrate that self-supervised extractive QA is not only achievable but already competitive with some supervised systems. And since our two-step method is able to generate its own training examples without requiring existing annotated training data in a specific domain or language, this work can bring us closer to creating extractive QA models that can generalize to more kinds of tasks and work with more languages, potentially increasing the accessibility of virtual assistant systems. By releasing the code for our technique, we believe this research will contribute to Facebook AI’s broader efforts to advance the state of self-supervised learning, and also help the wider AI community explore methods that are less reliant on resource-intensive annotated data sets.

### **Read the full paper:**

[Unsupervised question answering by cloze translation](https://research.fb.com/publications/unsupervised-question-answering-by-cloze-translation/)

## Related posts

[A new generative QA model that learns to answer the whole question](https://ai.facebook.com/blog/a-new-generative-qa-model-that-learns-to-answer-the-whole-question/)

July 02, 2019

[Introducing long-form question answering](https://ai.facebook.com/blog/longform-qa/)

July 25, 2019

[Teaching AI systems to learn language from letters, not words](https://ai.facebook.com/blog/teaching-ai-systems-to-learn-language-from-letters/)

July 15, 2019

## Related Tags

[Research](https://ai.facebook.com/blog/results/research/)
[Open Source](https://ai.facebook.com/blog/results/open-source/)