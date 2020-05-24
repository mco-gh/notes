FPGAs Open Gates in Machine Learning

# FPGAs Open Gates in Machine Learning

[May 1, 2019](https://www.nextplatform.com/2019/05/)[Michael Feldman](https://www.nextplatform.com/author/michael/)

.

![ab_database_containers_blocks-678x381.jpg](../_resources/3a8a62258433b177cbf5cbc4810c5193.jpg)

[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/#)[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/#)[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/#)[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/mailto:?subject=FPGAs%20Open%20Gates%20in%20Machine%20Learning&body=https%3A%2F%2Fwww.nextplatform.com%2F2019%2F05%2F01%2Ffpgas-open-gates-in-machine-learning%2F).

Field Programmable Gate Arrays (FPGAs) have notched some noticeable wins as a platform for machine learning, [Microsoft’s embrace of the technology in Azure](https://www.nextplatform.com/2017/08/24/drilling-microsofts-brainwave-soft-deep-leaning-chip/) being the most notable example. But for this sort of work, competing architectures like GPUs, CPUs, and custom ASICs, means that the long-term prospects for FPGAs in this application category will depend upon how well vendors like Intel and Xilinx are able to make the most of these devices.

Gaurav Singh, Xilinx’s corporate VP of silicon architecture and verification talked to us in advance of his appearance for a live, on-stage interview at [The Next AI Platform event next week](https://www.nextplatform.com/the-next-ai-platform/) in San Jose about how his company sees the way forward for FPGAs in the machine learning space and what unique attributes they bring to bear. The most important element of this is playing to the strengths of these devices.  For machine learning applications, that means primarily using FPGAs for inference, rather than training.

The rationale here is pretty straightforward: inference requires lower precision and less computational intensity than training, which fits better with the more limited floating-point capabilities of FPGAs, at least compared to a modern GPU.  “For training, it’s an arms race in terms of who can build the biggest and baddest system,” observed Singh.

That said, he believes there are situations where FPGAs can be suitable devices for training. One is where it can be accomplished with less precision – FP16, or even INT16 and INT8. Singh noted that some Xilinx’s customers have found applications where this lower precision works just fine for building their neural networks. The other use case is where training is performed incrementally alongside inference, the idea being to refine the model on a continuous, albeit less intensive basis. “So while FPGAs don’t play much in training today, I wouldn’t rule it out for the future,” Singh told us.

One unappreciated advantage of FPGAs is that inference is usually part of a larger application that may have originated without any machine learning to guide it – things like video surveillance, signal filtering, and genome analysis, to name a few. So if a customer is already using the FPGA as a data throughput accelerator for a particular application, adding inference into the mix doesn’t require an additional device. It’s not exactly a free lunch – the inference logic still needs to be implemented – but from the customer’s point of view, the ROI looks rather attractive.

Also, with inference, sometimes accuracy can be relaxed below INT8, all the way to INT4 or even INT2. Here, the malleability of FPGA data types really pays off with significantly improved throughput for just a modest implementation effort. “Customers are not shy about optimizing the solution for their needs,” explained Singh. “They will happily take higher performance with lower precision if that meets their requirements.”

Programmability is still the biggest hurdle with FPGAs, but with better development tools and higher level approaches like OpenCL, it’s becoming less onerous. One interesting new development is overlay processors, such as [the company’s own Xilinx Deep Neural Network (xDNN)](https://www.nextplatform.com/2018/08/27/xilinx-unveils-xdnn-fpga-architecture-for-ai-inference/), a shrink-wrapped CNN engine that can be implemented on suitably large devices. In some cases, Xilinx customers are building their own overlay processors.

The means developers can use high-level machine learning frameworks like PyTorch or TensorFlow, and Xilinx will be able to compile it into an instruction stream that can run on an FPGA. “From that point of view, the FPGA looks like any other processor,” explained Singh. “So, customers can iterate very fast.”

Faster and easier application development will be key to the success of these devices going forward, not just for machine learning applications, but for data-demanding workloads in general. That includes all sorts of applications in the datacenter and at the edge that require both high throughput and a flexible computing substrate. The encouraging news is that machine learning has provided FPGAs a pathway to do that.

We will delve into this and other architectural and workload-specific topics with Gaurav and many others on May 9 in San Jose at The Next AI Platform. We hope you can join us, few seat left, [register today](https://www.nextplatform.com/the-next-ai-platform/).

[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/#)[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/#)[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/#)[**](https://www.nextplatform.com/2019/05/01/fpgas-open-gates-in-machine-learning/mailto:?subject=FPGAs%20Open%20Gates%20in%20Machine%20Learning&body=https%3A%2F%2Fwww.nextplatform.com%2F2019%2F05%2F01%2Ffpgas-open-gates-in-machine-learning%2F).

.

#### Sign up to our Newsletter

Featuring highlights, analysis, and stories from the week directly from us to your inbox with nothing in between.

[Subscribe now](https://www.nextplatform.com/register/)