Stanford DAWN Deep Learning Benchmark (DAWNBench) ·

   [DAWNBench](http://dawn.cs.stanford.edu/benchmark/index.html)

 [![](../_resources/08919698d372a7dfd8aac3b06d186aa5.png)](http://dawn.cs.stanford.edu/benchmark/index.html)

# DAWNBench

## An End-to-End Deep Learning Benchmark and Competition

- [Image Classification (ImageNet)](http://dawn.cs.stanford.edu/benchmark/index.html#imagenet)

- [Image Classification (CIFAR10)](http://dawn.cs.stanford.edu/benchmark/index.html#cifar10)

- [Question Answering (SQuAD)](http://dawn.cs.stanford.edu/benchmark/index.html#squad)

DAWNBench is a benchmark suite for end-to-end deep learning training and inference. Computation time and cost are critical resources in building deep models, yet many existing benchmarks focus solely on model accuracy. DAWNBench provides a reference set of common deep learning workloads for quantifying training time, training cost, inference latency, and inference cost across different optimization strategies, model architectures, software frameworks, clouds, and hardware.

 **Deadline: April 20, 2018 at 11:59 PM PDT.** All pull requests created on [dawn-bench-entries](https://github.com/stanford-futuredata/dawn-bench-entries) will be considered and reviewed over the following two weeks. Final results will be announced at the beginning of May.

 [Read the paper](http://dawn.cs.stanford.edu/benchmark/papers/nips17-dawnbench.pdf)

 [More information](http://dawn.cs.stanford.edu/benchmark/about.html)

 [Submit your results on GitHub](https://github.com/stanford-futuredata/dawn-bench-entries)

#   Image Classification on ImageNet

##    Training Time

 [](http://dawn.cs.stanford.edu/benchmark/index.html#imagenet-train-time)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/ImageNet/train.html)

**Objective:** Time taken to train an image classification model to a top-5 validation accuracy of 93% or greater on [ImageNet](http://www.image-net.org/).

| Rank | Time to 93% Accuracy | Model | Hardware | Framework |
| --- | --- | --- | --- | --- |
| 1<br>Apr 2018 | 0:30:43 | ResNet50<br>[Google](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:cloud-tpu-dawnbench@googlegroups.com)<br> [source](https://github.com/tensorflow/tpu/tree/dafdf3dbd057c49fffa9ea7d356a3a54d6e2fd68/models/official/resnet/benchmark) | Half of a TPUv2 Pod | TensorFlow 1.8.0-rc1 |
| 2<br>Apr 2018 | 1:06:32 | AmoebaNet-D N6F256<br>[Google](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:cloud-tpu-dawnbench@googlegroups.com)<br> [source](https://github.com/tensorflow/tpu/tree/e5c126d66aa3d25e0cb066bdf7fc46f98fe59901/models/experimental/amoeba_net/) | 1/4 of a TPUv2 Pod | TensorFlow 1.8.0-rc1 |
| 3<br>Apr 2018 | 1:58:24 | AmoebaNet-D N6F256<br>[Google](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:cloud-tpu-dawnbench@googlegroups.com)<br> [source](https://github.com/tensorflow/tpu/tree/e5c126d66aa3d25e0cb066bdf7fc46f98fe59901/models/experimental/amoeba_net/) | 1/16 of a TPUv2 Pod | TensorFlow 1.8.0-rc1 |

##    Training Cost

 [](http://dawn.cs.stanford.edu/benchmark/index.html#imagenet-train-cost)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/ImageNet/train.html)

**Objective:** Total cost of public cloud instances to train an image classification model to a top-5 validation accuracy of 93% or greater on [ImageNet](http://www.image-net.org/).

| Rank | Cost (USD) | Model | Hardware | Framework |
| --- | --- | --- | --- | --- |
| 1<br>Apr 2018 | $49.30 | AmoebaNet-D N6F256<br>[Google Cloud TPU](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:cloud-tpu-dawnbench@googlegroups.com)<br> [source](https://github.com/tensorflow/tpu/tree/1acd2c4d48013ea1623ddbf9f28166a85404213a/models/experimental/amoeba_net) | GCP n1-standard-2, Cloud TPU | TensorFlow 1.8.0-rc0 |
| 2<br>Apr 2018 | $58.53 | ResNet50<br>[Google Cloud TPU](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:cloud-tpu-dawnbench@googlegroups.com)<br> [source](https://github.com/tensorflow/tpu/blob/9de6656a779e73ac61995bd87044af21b3f37951/models/experimental/resnet_bfloat16/resnet_benchmark.py) | GCP n1-standard-2, Cloud TPU | TensorFlow v1.8rc1 |
| 3<br>Mar 2018 | $82.07 | ResNet50<br>[Google Cloud TPU](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:cloud-tpu-dawnbench@googlegroups.com)<br> [source](https://github.com/tensorflow/tpu/tree/b189540102d6b5b40b1730d7e5ad5c884bae323c/models/experimental/resnet_bfloat16) | GCP n1-standard-2, Cloud TPU | TensorFlow v1.7rc1 |

##    Inference Latency

 [](http://dawn.cs.stanford.edu/benchmark/index.html#imagenet-inference-time)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/ImageNet/inference.html)

**Objective:** Latency required to classify one [ImageNet](http://www.image-net.org/) image using a model with a top-5 validation accuracy of 93% or greater.

| Rank | 1-example Latency (milliseconds) | Model | Hardware | Framework |
| --- | --- | --- | --- | --- |
| 1<br>Apr 2018 | 9.9600 | ResNet50<br>[Intel(R) Corporation](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:daisy.deng@intel.com)<br> [source](https://github.com/intel/caffe/tree/DAWN_Bench) | Amazon EC2 [c5.18xlarge] | Intel(R) Optimized Caffe |
| 2<br>Apr 2018 | 12.4000 | ResNet50<br>[Intel(R) Corporation](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:daisy.deng@intel.com)<br> [source](https://github.com/intel/caffe/tree/DAWN_Bench) | Amazon EC2 [c5.4xlarge] | Intel(R) Optimized Caffe |
| 3<br>Apr 2018 | 17.3800 | ResNet50<br>[Intel(R) Corporation](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:daisy.deng@intel.com)<br> [source](https://github.com/intel/caffe/tree/DAWN_Bench) | Amazon EC2 [c5.2xlarge] | Intel(R) Optimized Caffe |

##    Inference Cost

 [](http://dawn.cs.stanford.edu/benchmark/index.html#imagenet-inference-cost)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/ImageNet/inference.html)

**Objective:** Average cost on public cloud instances to classify 10,000 validation images from [ImageNet](http://www.image-net.org/) using of an image classification model with a top-5 validation accuracy of 93% or greater.

| Rank | Cost (USD) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Apr 2018 | $0.02 | ResNet50<br>[Intel(R) Corporation](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:daisy.deng@intel.com)<br> [source](https://github.com/intel/caffe/tree/DAWN_Bench) | Intel(R) Optimized Caffe | Amazon EC2 [c5.2xlarge] |
| 2<br>Apr 2018 | $0.02 | ResNet50<br>[Intel(R) Corporation](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:daisy.deng@intel.com)<br> [source](https://github.com/intel/caffe/tree/DAWN_Bench) | Intel(R) Optimized Caffe | Amazon EC2 [c5.4xlarge] |
| 3<br>Nov 2017 | $0.07 | ResNet 152<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/deepakn94/mxnet-resnet) | MXNet 0.11.0 | 1 K80 / 61 GB / 4 CPU (Amazon EC2 [p2.xlarge]) |

#   Image Classification on CIFAR10

##    Training Time

 [](http://dawn.cs.stanford.edu/benchmark/index.html#cifar10-train-time)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/CIFAR10/train.html)

**Objective:** Time taken to train an image classification model to a test accuracy of 94% or greater on [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html).

| Rank | Time to 94% Accuracy | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Apr 2018 | 0:02:54 | Custom Wide Resnet<br>[fast.ai + students team: Jeremy Howard, Andrew Shaw, Brett Koonce, Sylvain Gugger](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:j@fast.ai)<br> [source](https://github.com/fastai/imagenet-fast/commit/1bc5aeec765572397c0ebe4a5d616d03beeeeec1) | fastai / pytorch | 8 * V100 (AWS p3.16xlarge) |
| 2<br>Apr 2018 | 0:05:41 | Resnet18 + minor modifications<br>[bkj](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:ben@canfield.io)<br> [source](https://github.com/bkj/basenet/tree/49b2b61e5b9420815c64227c5a10233267c1fb14/examples) | pytorch 0.3.1.post2 | V100 (AWS p3.2xlarge) |
| 3<br>Apr 2018 | 0:06:45 | Custom Wide Resnet<br>[fast.ai + students team: Jeremy Howard, Andrew Shaw, Brett Koonce, Sylvain Gugger](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:j@fast.ai)<br> [source](https://github.com/fastai/imagenet-fast/commit/a2ff907cd5e7315088324e1ff324fd25a1a67fe3) | fastai / pytorch | Paperspace Volta (V100) |

##    Training Cost

 [](http://dawn.cs.stanford.edu/benchmark/index.html#cifar10-train-cost)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/CIFAR10/train.html)

**Objective:** Total cost for public cloud instances to train an image classification model to a test accuracy of 94% or greater on [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html).

| Rank | Cost (USD) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Apr 2018 | $0.26 | Custom Wide Resnet<br>[fast.ai + students team: Jeremy Howard, Andrew Shaw, Brett Koonce, Sylvain Gugger](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:j@fast.ai)<br> [source](https://github.com/fastai/imagenet-fast/commit/a2ff907cd5e7315088324e1ff324fd25a1a67fe3) | fastai / pytorch | Paperspace Volta (V100) |
| 2<br>Apr 2018 | $0.29 | Resnet18 + minor modifications<br>[bkj](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:ben@canfield.io)<br> [source](https://github.com/bkj/basenet/tree/49b2b61e5b9420815c64227c5a10233267c1fb14/examples) | pytorch 0.3.1.post2 | V100 (AWS p3.2xlarge) |
| 3<br>Apr 2018 | $1.18 | Custom Wide Resnet<br>[fast.ai + students team: Jeremy Howard, Andrew Shaw, Brett Koonce, Sylvain Gugger](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:j@fast.ai)<br> [source](https://github.com/fastai/imagenet-fast/commit/1bc5aeec765572397c0ebe4a5d616d03beeeeec1) | fastai / pytorch | 8 * V100 (AWS p3.16xlarge) |

##    Inference Latency

 [](http://dawn.cs.stanford.edu/benchmark/index.html#cifar10-inference-time)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/CIFAR10/inference.html)

**Objective:** Latency required to classify one [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) image using a model with a test accuracy of 94% or greater.

| Rank | 1-example Latency (milliseconds) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Oct 2017 | 9.7843 | ResNet 56<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/pytorch/CIFAR10) | PyTorch v0.1.12 | 1 K80 / 61 GB / 4 CPU (Amazon EC2 [p2.xlarge]) |
| 2<br>Oct 2017 | 24.6291 | ResNet 164 (with bottleneck)<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/pytorch/CIFAR10) | PyTorch v0.1.12 | 1 P100 / 512 GB / 56 CPU (DAWN Internal Cluster) |
| 3<br>Oct 2017 | 24.9200 | ResNet 164 (without bottleneck)<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/CIFAR10) | TensorFlow v1.2 | 60 GB / 16 CPU (Google Cloud [n1-standard-16]) |

##    Inference Cost

 [](http://dawn.cs.stanford.edu/benchmark/index.html#cifar10-inference-cost)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/CIFAR10/inference.html)

**Objective:** Average cost on public cloud instances to classify 10,000 test images from [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) using an image classification model with a test accuracy of 94% or greater.

| Rank | Cost (USD) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Oct 2017 | $0.02 | ResNet 56<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/pytorch/CIFAR10) | PyTorch v0.1.12 | 1 K80 / 61 GB / 4 CPU (Amazon EC2 [p2.xlarge]) |
| 2<br>Oct 2017 | $0.04 | ResNet 164 (without bottleneck)<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/CIFAR10) | TensorFlow v1.2 | 60 GB / 16 CPU (Google Cloud [n1-standard-16]) |
| 3<br>Oct 2017 | $0.05 | ResNet 164 (with bottleneck)<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/CIFAR10) | TensorFlow v1.2 | 60 GB / 16 CPU (Google Cloud [n1-standard-16]) |

#   Question Answering on SQuAD

##    Training Time

 [](http://dawn.cs.stanford.edu/benchmark/index.html#squad-train-time)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/SQuAD/train.html)

**Objective:** Time taken to train a question answering model to a F1 score of 0.75 or greater on the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) development dataset.

| Rank | Time to 0.75 F1 | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Oct 2017 | 7:38:10 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 61 GB / 4 CPU (Amazon EC2 [p2.xlarge]) |
| 2<br>Oct 2017 | 7:51:22 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 P100 / 512 GB / 56 CPU (DAWN Internal Cluster) |
| 3<br>Oct 2017 | 8:43:40 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 30 GB / 8 CPU (Google Cloud) |

##    Training Cost

 [](http://dawn.cs.stanford.edu/benchmark/index.html#squad-train-cost)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/SQuAD/train.html)

**Objective:** Total cost for public cloud instances to train a question answering model to a F1 score of 0.75 or greater on the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) development dataset.

| Rank | Cost (USD) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Oct 2017 | $5.78 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 60 GB / 16 CPU (Google Cloud [n1-standard-16]) |
| 2<br>Oct 2017 | $6.87 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 61 GB / 4 CPU (Amazon EC2 [p2.xlarge]) |
| 3<br>Oct 2017 | $8.44 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 30 GB / 8 CPU (Google Cloud) |

##    Inference Latency

 [](http://dawn.cs.stanford.edu/benchmark/index.html#squad-inference-time)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/SQuAD/inference.html)

**Objective:** Latency required to answer one [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) question using a model with a F1 score of at least 0.75 on the development dataset.

| Rank | 1-example Latency (milliseconds) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Oct 2017 | 100.0000 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 60 GB / 16 CPU (Google Cloud [n1-standard-16]) |
| 2<br>Oct 2017 | 590.0000 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 30 GB / 8 CPU (Google Cloud) |
| 3<br>Oct 2017 | 638.1000 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 P100 / 512 GB / 56 CPU (DAWN Internal Cluster) |

##    Inference Cost

 [](http://dawn.cs.stanford.edu/benchmark/index.html#squad-inference-cost)

 [All Submissions](http://dawn.cs.stanford.edu/benchmark/SQuAD/inference.html)

**Objective:** Average cost on public cloud instances to answer 10,000 questions from the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) development dataset using a question answering model to a dev F1 score of 0.75% or greater.

| Rank | Cost (USD) | Model | Framework | Hardware |
| --- | --- | --- | --- | --- |
| 1<br>Oct 2017 | $0.15 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 60 GB / 16 CPU (Google Cloud [n1-standard-16]) |
| 2<br>Oct 2017 | $1.58 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 30 GB / 8 CPU (Google Cloud) |
| 3<br>Oct 2017 | $1.76 | BiDAF<br>[Stanford DAWN](http://dawn.cs.stanford.edu/benchmark/index.htmlmailto:dawn-benchmark@lists.stanford.edu)<br> [source](https://github.com/stanford-futuredata/dawn-bench-models/tree/master/tensorflow/SQuAD) | TensorFlow v1.2 | 1 K80 / 61 GB / 4 CPU (Amazon EC2 [p2.xlarge]) |

#   Join Us

DAWNBench is part of a larger community conversation about the future of machine learning infrastructure. Sound off on the [DAWNBench google group](https://groups.google.com/forum/#!forum/dawn-bench-community).

 ![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[3 min to Spreed]()