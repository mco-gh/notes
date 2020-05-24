Announcing TensorFlow 1.0

## [Announcing TensorFlow 1.0](https://developers.googleblog.com/2017/02/announcing-tensorflow-10.html)

Wednesday, February 15, 2017
 *Posted By: Amy McDonald Sandjideh, Technical Program Manager, TensorFlow*

In just its [first year](https://research.googleblog.com/2016/11/celebrating-tensorflows-first-year.html), TensorFlow has helped researchers, engineers, artists, students, and many others make progress with everything from [language translation](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html) to [early detection of skin cancer](http://news.stanford.edu/2017/01/25/artificial-intelligence-used-identify-skin-cancer/) and [preventing blindness in diabetics](https://www.wired.com/2016/11/googles-ai-reads-retinas-prevent-blindness-diabetics/). We're excited to see people using TensorFlow in over[6000 open-source repositories online](https://github.com/search?q=tensorflow).

Today, as part of the first annual [TensorFlow Developer Summit](https://events.withgoogle.com/tensorflow-dev-summit/), hosted in Mountain View and [livestreamed around the world](https://events.withgoogle.com/tensorflow-dev-summit/watch-the-videos/#content), we're announcing **[TensorFlow 1.0](https://github.com/tensorflow/tensorflow/releases/tag/v1.0.0)**:

**It's faster: **TensorFlow 1.0 is incredibly fast! [XLA](https://tensorflow.org/performance/xla) lays the groundwork for even more performance improvements in the future, and [tensorflow.org](https://tensorflow.org/) now includes [tips & tricks](https://tensorflow.org/performance/performance_guide)for tuning your models to achieve maximum speed. We'll soon publish updated implementations of several popular models to show how to take full advantage of TensorFlow 1.0 - including a 7.3x speedup on 8 GPUs for Inception v3 and 58x speedup for distributed Inception v3 training on 64 GPUs!

**It's more flexible:** TensorFlow 1.0 introduces a high-level API for TensorFlow, with tf.layers, tf.metrics, and tf.losses modules. We've also announced the inclusion of a new tf.keras module that provides full compatibility with [Keras](https://keras.io/), another popular high-level neural networks library.

**It's more production-ready than ever:** TensorFlow 1.0 promises Python API stability (details [here](https://tensorflow.org/programmers_guide/version_semantics)), making it easier to pick up new features without worrying about breaking your existing code.

Other highlights from [TensorFlow 1.0](https://github.com/tensorflow/tensorflow/releases/tag/v1.0.0):

- Python APIs have been changed to resemble NumPy more closely. For this and other backwards-incompatible changes made to support API stability going forward, please use our handy [migration guide](https://tensorflow.org/install/migration) and [conversion script](https://github.com/tensorflow/tensorflow/tree/r1.0/tensorflow/tools/compatibility).
- Experimental APIs for [Java](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/java)and [Go](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/go)
- Higher-level API modules tf.layers, tf.metrics, and tf.losses - brought over from [tf.contrib.learn](https://www.tensorflow.org/get_started/tflearn)after incorporating [skflow](https://github.com/tensorflow/skflow)and [TF Slim](https://github.com/tensorflow/models/blob/master/inception/inception/slim/README.md)
- Experimental release of [XLA](http://tensorflow.org/performance/xla), a domain-specific compiler for TensorFlow graphs, that targets CPUs and GPUs. XLA is rapidly evolving - expect to see more progress in upcoming releases.
- Introduction of the TensorFlow Debugger ([tfdbg](https://www.tensorflow.org/programmers_guide/debugger)), a command-line interface and API for debugging live TensorFlow programs.
- New [Android demos](https://github.com/tensorflow/tensorflow/tree/r1.0/tensorflow/examples/android) for object detection and localization, and camera-based image stylization.
- [Installation](https://www.tensorflow.org/install) improvements: Python 3 docker images have been added, and TensorFlow's pip packages are now PyPI compliant. This means TensorFlow can now be installed with a simple invocation of `pip install tensorflow`.

We're thrilled to see the pace of development in the TensorFlow community around the world. To hear more about TensorFlow 1.0 and how it's being used, you can watch the [TensorFlow Developer Summit talks on YouTube](https://www.youtube.com/playlist?list=PLOU2XLYxmsIKGc_NBoIhTn2Qhraji53cv), covering recent updates from higher-level APIs to TensorFlow on mobile to our new [XLA](https://www.tensorflow.org/performance/xla) compiler, as well as the exciting ways that TensorFlow is being used:

[TensorFlow: Machine Learning for Everyone](https://www.youtube.com/watch?list=PLOU2XLYxmsIKGc_NBoIhTn2Qhraji53cv&v=mWl45NkFBOc)

Click [here](https://www.youtube.com/playlist?list=PLOU2XLYxmsIKGc_NBoIhTn2Qhraji53cv)for a link to the livestream and video playlist (individual talks will be posted online later in the day).

The TensorFlow ecosystem continues to grow with new techniques like [Fold](https://research.googleblog.com/2017/02/announcing-tensorflow-fold-deep.html)for dynamic batching and tools like the [Embedding Projector](https://research.googleblog.com/2016/12/open-sourcing-embedding-projector-tool.html) along with [updatesto our existing tools like TensorFlow Serving](https://github.com/tensorflow/serving/releases/tag/0.5.0). We're incredibly grateful to the community of contributors, educators, and researchers who have made advances in deep learning available to everyone. We look forward to working with you on forums like [GitHub issues](https://github.com/tensorflow/tensorflow/issues), [Stack Overflow](http://stackoverflow.com/questions/tagged/tensorflow), [@TensorFlow](https://twitter.com/tensorflow), the [discuss@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/discuss)group, and at future events.

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

Labels:[Announcement](https://developers.googleblog.com/search/label/Announcement) , [featured](https://developers.googleblog.com/search/label/featured) , [TensorFlow](https://developers.googleblog.com/search/label/TensorFlow)