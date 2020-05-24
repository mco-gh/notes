An analysis of the Tensorflow codebase

 [Engineering Observability](https://blog.sourced.tech/tag/engineering-observability/)

# An analysis of the Tensorflow codebase

By [DevRel team](https://blog.sourced.tech/author/devrel/) /  29 October 2019

Given our interest in Machine Learning on Code at source{d} and with Tensorflow World happening this week, we thought it would be fun to analyze all the Tensorflow git repositories with [source{d} Enterprise Edition](https://sourced.tech/products/enterprise-edition) (EE) to extract interesting insights for the Tensorflow community. source{d} EE not only saves us time through higher query performance but also allows us to showcase advanced metrics that are not (yet) available out of the box in [source{d} Community Edition](https://sourced.tech/products/community-edition/) (CE).

Follow [this link](https://instance-1.infra.tensorflow-summit.stg.srcd.host/superset/dashboard/tensorflow/) to view a read-only dashboard of the entire Tensorflow Project analysis. Keep on reading for a summary of our key findings.

# Release Cadence

Looking at the project release timeline below, it seems like the release cycles are not as consistent as other open-source projects such as [Kubernetes](https://blog.sourced.tech/post/an-analysis-of-the-kubernetes-codebase/). Although the release velocity looked quite high, with 8 releases in 2018, that velocity slowed down significantly in 2019. Note that version 1.13 had to be skipped due to a [bug](https://github.com/tensorflow/tensorflow/issues/26046) during the release process.

![OCV992FYYqmcZH3HdXTyurmiPdO2zI3ljgjmGClyHkrDwqgIcaEwh4JRWrq49vBYp2rc9AokaJ_X_pyQ5O7zPF4m797sm0riA2rUPvuTRSRsLsncV9q2nXsYkm__6-3TybM4jUq_](../_resources/7ab222ad30abbfdf1a2c0fea4c2f0d4b.png)

In fact, as we can see in the chart below, most of the 2019 releases are tied to other repositories in the Tensorflow Organization.

![WV-Ly6SMlCve8PrNTJwf8B1S9SRlrqZpvoW0slkey01PsDPcuJmNvlZLbc2CrV2Dq2yDeZ6VtMu67q1693gFjSu40O5oCgNA_U4cPzWxTz7sAcvmGVu_84vu-6FuqkadTPN0fhi6](../_resources/576f30100420dfa75fb96c697d07f45e.png)

# Files and lines of Codes by programing languages

With more than **17K files, 4M lines of code**, it is safe to say that the breadth and depth of the Tensorflow project have been growing significantly over the past few years. After 4 years of consistent growth and fast development, both the number of files and lines of code seem to be slowing down with significant refactoring efforts as part of the 2.0 release last month.

![VQv_w2D991wBSXOtb9TKrmEjaADDI-GJ1Zj3PbyxrY9TYH8fsgzrS2dlZ-PGyLTMwbOHQ4i-mc2Hss-go1Riy8fQV39eObn286r3la7lClgN7U2z45VhwNfRoxP47QWkk6RKJRQj](../_resources/4810226d1717e91a1f58ec4164b6c581.png)

The growing number of programming languages used in the [tensorflow](https://github.com/tensorflow/tensorflow) codebase which just reached 42 since the beginning of 2019 also confirms the growing project scope and complexity.

In the chart about programming languages below, we can see that Python and C++ are by far the dominant languages both in terms of the number of files and lines of code per language. The analysis also shows that Javascript, TypeScript and CSS have been extracted to separate GitHub projects while some others like Go and Java have been gaining momentum.

![OBb9hQjvlhDY75pQKAV6q2NL06zuwijY1Bl1qm-EiQXAdxAHgdgl4B_ye9YQ1zU531kaCpA6ZAR4cI36MSCMCIfKSAJ2erW5rfRFb9pid88i65HUoZmtru-4yb5MahjsywViNp6e](../_resources/7b4d63a3e379e6ac5f304e5d46e77ece.png)

By taking a closer look at the evolution of programming languages in the Tensorflow codebase, we can see that a lot of python code was removed right before the 2.0.0 release while the number of C++ lines remained the same. The fact that the low-level logic (like multiplication and so on) was written in C++ explains why it wasn’t affected while high-level logic in Python was significantly refactored.

![rqb2jIhsEZC3g24cMQvJzG5L-mmZmLrmj8eX2wOPNPwGAUqrPvTfW7caQjJUs75NBFWURl-0Z4aBuPJQp4J685dtnnhuPBJFlGpZON7uUHMLZVVvD3LBscuP3TIcMFcXdXUYKQYI](../_resources/e2767f453bd678fb3dfc14b7eea655a1.png)

# Commits activity and Contributions

![](../_resources/182f82aa4f81e09253aa659e028f1d2e.png)

The relatively small number of repositories (83) in contrast with a large number of contributors (5920), shows a strong focus on the core repositories *tensorflow, models *and* docs. *The evolution of the number of contributors per repository chart below shows that the project now has between 500 and 600 unique contributors per month.

![W4QgDPhnMoW_F2eeZsMroI9ZfG8aHBA_h8S6mFqHbG5RgZYpXXfbHwZBU6dR7EVCeqJOUz_w-CnCBpa2QF_mpvKOM-fdLUYcB_nadroh7Acwge8vCxJywNCjbtGBOyUSeB1kDRP5](../_resources/d3f4eaeeac0dfc8bdf9834ffd0f5cbb2.png)

Knowing that Tensorflow is a project that was open-sourced by Google, it is not surprising to see that tensorflow.org and Google are the biggest contributors by the number of commits. The number of contributions by individuals (those with @gmail.com and @github.com emails) is fairly high, a sign of a healthy open source project and community. Nvidia and Intel seem to be the only other organizations that made significant enough contributions to appear on this chart.

Excluding contributions from tensorflow-gardener, a bot to automate repo maintenance and Copybara, a tool for transforming and moving code between repositories, we can clearly see that the biggest individual contributors are also from Google. Big shout out to Shanqing Cai, Nikhil Thorat, Daniel Smilkovm and Yong Tang who clearly stand out as the top contributors.

![Screen-Shot-2019-10-29-at-10.57.01-AM.png](../_resources/3f63b7371c3a14e0c7e1d42f86cc13d5.png)

The nature of tensorflow-gardener's commits which highlights internal contributions from Google can be further plotted over time. We see that the heavy changes tend to happen during or right after releases.

![f9bkCaXzlHTjJ4dA-4kqEhkOJMc5F9xTDa-fL8QeWul0SiwZaZnLFVy25YjTzvN0NBT3cylnY52kNayaHYGDz-MiYLhwCejfwVIPySwhq7DcQoHMkbKCCbgFKmBWfIvjNsWM6qrW](../_resources/a848e8bdf18b340947d5fa1b482cbe43.png)

Number of commits and size of changes over time authored by tensorflow-gardener.

Nonetheless, the evolution of commits and lines of code authored by tensorflow-gardener vs others indicates that the project is also attracting more and more external contributors.

![Screen-Shot-2019-10-29-at-10.58.06-AM.png](../_resources/cdc2ebc2d5b2062c7e5f6fc68fa239aa.png)

With a range of 8,000 to 10,000 commits per month, the total number of commits remains quite high, a healthy sign of a very active open source project. Although that number looks high, we assume that Google has a lot of internal contributors that do not use GitHub directly and merge multiple commits into one, so these numbers could be even higher.  The fact that the commit velocity continues to grow confirms that trend as well as the popularity of the project. It’s worth pointing out the big surge in the number of commits right before Tensorflow 2.0 release.

![tbZ9fZt6PpY4Ex8JO51fCOLZiFlbSbUx8lduANQ7gkqW3dvicQkgIaT6BeQK08ncAAS1aLVlYpxq75CKFN3RHPMDxBzR0PiAMPrNmXm_MdHnBfIgvB6NtFQeFQ9IKtO0tkKRfXXM](../_resources/c1ce646fb33aeb06d53722b1981167b4.png)

If we look at the nature of these commits, we can see that the number of contributions to the core *tensorflow *repository now represents just over half of the total with most of the new contributions now directed to side projects, such as [*tfjs*](https://github.com/tensorflow/tfjs) a WebGL accelerated JavaScript library for training and deploying ML models, the official [documentation](https://github.com/tensorflow/docs) and the [*Tensorboard*](https://github.com/tensorflow/tensorboard) visualization toolkit. The commits evolution reveals that the core project is reaching maturity while Google and the community are focusing on the overall user experience both in terms of onboarding and actual deployments.

![SIuNgV1LkWjO8ojIHlYsv8pFlWRP2KGIR4cedF8e8A5dNJwwjkg1Hhq-kYZmj7KdRk3ntDYPqoGmO0BLcyjZz1c7d7TTi6LU2kmSyv6kDUJHu9TKfyqG5V9bptAyCdrKCoEZwPcC](../_resources/86eaea9ba4225a78fd1c8fc99d4d4d9b.png)

# of commits overtime on top repository in the github.com/tensorflow organization, detailed

By plotting the correlation between commit time series belonging to each project the following chart reveals the temporal changes coupling. Note that the brightness indicates the relative commit frequency. Commits to *tensorflow, tfjs, models* and *docs* often appear at roughly the same time. *tfjs-layers, tfjs-converter* and *hub* are also related. Besides, this plot indicates abandoned projects i.e *fold, playground, embedding projector*, etc

![ozfj_DwsM2dr9nZIYwgyP2zYmTg3IsGaIxWC9OPtlQhDhSn8-zNIb3zrBPYRGBYtzhbBu9bzb-johK16vW4mF6h41xEehawd5AcSU_lWJ1Wi8EGmUqpBdbPt36FnOxcWPcxI3prW](../_resources/07b1af4c0967a1acbd4fddfbe87125cc.png)

Aligned commit time series in the github.com/tensorflow organization

# Pull Requests and Issues activity

The chart below highlights the most active repositories based on the number of pull requests (PRs) over the past 4 years. Not surprisingly, we can see that most of the action happens on the TensorFlow repository itself with [*tensorflow/tfx*](https://github.com/tensorflow/tfx) (a Google-production-scale machine learning platform based on TensorFlow.) and [*tensoflow/docs*](https://github.com/tensorflow/docs) as the second and third most active repositories. The nature of these PRs and issues confirms the project focus on user experience and enterprise adoption.

![es4IPKvEtx8IHu99-syhOxfTyZeb3dRNM-5lJQF8FHSkyrUroS9_mMu7BHLW8IQ-WdIvyyiqu8TYdxSNIh1Bl-U1hTSt4n1r7V_KthojiC-V2LMpy7TPukek-c24N1MFKIl4nkJf](../_resources/ee4d3479ffcf2b9aaf237adda904cefa.png)

The table below highlights the top pending pull requests as of September 2019, including information about their age in days, the number of comments, as well as the number of lines of code modified. Excluding the Keras Resnet PR which is not intended to be merged, the oldest open PRs in the TensorFlow organization seem to be related to the swift-APIs and a community plea to make Tensorflow more modular by creating “more focused TensorFlow modules [that] can be created, maintained and released separately.”

![O8BiCOaJUsHKZ3SY5U3Yi1fSKYJGHVyguNRmE7V1HXrk_5wmhydsElafAx2rwjjsJX_kKGF8qHj-j0t6sykMo1s2fbp0L6hM95cLsKg3G8pWrLnYsa17ISHAs-_yKOQghBGuwyQ2](../_resources/31a2cd67f7265ccc4652703fa79d7d46.png)

The following chart confirms that the Tensorflow maintainers are super responsive with an average “Time to Merge” around 4 days with understandable productivity pitfalls in late December / early January with most contributors taking time off for the holidays. Surprisingly, the upward trend from the summer of 2018 did not happen over the summer of 2019 which reveals a clear sense of urgency in shipping the 1.14 release.

![aII2uYQK7-8vBYsCkfEWgZpcrowrguN9UplGK8YwZre-tTpRFoKEExHacpBV-483BnphwwZALuJJsa-9_p6UzVhzd7tFbuQeEIYXsSryEABAQxk7K_5VhUFrLMTkELy3RWNYoTnT](../_resources/8231bc2044c243a0d461616042e8b1dd.png)

The Tensorflow project throughput is another interesting metric to look at to further understand Open source project velocity. Throughput can be defined as the number of features added or bugs fixed within a given period. In this case, we’re measuring the number of closed GitHub issues. The following chart shows that the total number of closed issues has been growing consistently over the years with major drops right before and after major releases such as tensorflow 2.0 in September 2019.

![LkP88yORdA4nUxiu6V-rxSdjTwliri4jQ6jrLT0AuVZ0A4merFAbaYoP00rqxkRXGt9kTJBFgpZS5eSdTlOsHlYYJXysdomAOmTEWKhSWAPeO6IauXAiImGxm17_-nO_8ud-gCG6](../_resources/b30d3189f1577b8f4d8be2748582efd8.png)

A big thank you to Edd Wilder-James and Martin Wicke for reviewing this analysis and providing some feedback.

**Learn More:**

- Request a [source{d} EE demo](https://go.sourced.tech/enterprise-demo)
- Watch a [short overview video](https://www.youtube.com/watch?v=p1sZ_-P6FxA&feature=youtu.b)
- Sign up for [source{d} Newsletter](https://go.sourced.tech/newsletter)

 [Start Discussion](https://forum.sourced.tech/t/an-analysis-of-the-tensorflow-codebase/260)  0 replies

 ![](../_resources/9158bb7517cd70739162f676e47fad19.png)

[DevRel team](https://blog.sourced.tech/author/devrel/)

DevRel team at source{d}