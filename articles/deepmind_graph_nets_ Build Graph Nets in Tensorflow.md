deepmind/graph_nets: Build Graph Nets in Tensorflow

[![graph-nets-deepmind-shortest-path0.gif](../_resources/a8d08bcd381dee1350dd4a85ca594856.gif)](https://github.com/deepmind/graph_nets/blob/master/images/graph-nets-deepmind-shortest-path0.gif)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='57'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='842' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#graph-nets-library)Graph Nets library

[Graph Nets](https://github.com/deepmind/graph_nets) is DeepMind's library for building graph networks in Tensorflow and Sonnet.

Contact [graph-nets@google.com](https://github.com/deepmind/graph_netsmailto:graph-nets@google.com) for comments and questions.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='58'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='846' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#what-are-graph-networks)What are graph networks?

A graph network takes a graph as input and returns a graph as output. The input graph has edge- (*E* ), node- (*V* ), and global-level (**u**) attributes. The output graph has the same structure, but updated attributes. Graph networks are part of the broader family of "graph neural networks" (Scarselli et al., 2009).

To learn more about graph networks, see our arXiv paper: [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261).

[![graph-network.png](../_resources/fc8ad7c76059ac26cbfffb9cb6a7de50.png)](https://github.com/deepmind/graph_nets/blob/master/images/graph-network.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='59'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='853' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#installation)Installation

The Graph Nets library can be installed from pip.
This installation is compatible with Linux/Mac OS X, and Python 2.7 and 3.4+.

The library will work with both the CPU and GPU version of TensorFlow, but to allow for that it does not list Tensorflow as a requirement, so you need to install Tensorflow separately if you haven't already done so.

To install the Graph Nets library and use it with TensorFlow 1 and Sonnet 1, run:

(CPU)

$ pip install graph_nets "tensorflow>=1.15,<2"  "dm-sonnet<2"  "tensorflow_probability<0.9"

(GPU)

$ pip install graph_nets "tensorflow_gpu>=1.15,<2"  "dm-sonnet<2"  "tensorflow_probability<0.9"

To install the Graph Nets library and use it with TensorFlow 2 and Sonnet 2, run:

(CPU)

$ pip install graph_nets "tensorflow>=2.1.0-rc1"  "dm-sonnet>=2.0.0b0" tensorflow_probability

(GPU)

$ pip install graph_nets "tensorflow_gpu>=2.1.0-rc1"  "dm-sonnet>=2.0.0b0" tensorflow_probability

The latest version of the library requires TensorFlow >=1.15. For compatibility with earlier versions of TensorFlow, please install v1.0.4 of the Graph Nets library.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='60'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='899' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#usage-example)Usage example

The following code constructs a simple graph net module and connects it to data.

import graph_nets as gnimport sonnet as snt# Provide your own functions to generate graph-structured data.input_graphs = get_graphs()# Create the graph network.graph_net_module = gn.modules.GraphNetwork( edge_model_fn=lambda: snt.nets.MLP([32, 32]), node_model_fn=lambda: snt.nets.MLP([32, 32]), global_model_fn=lambda: snt.nets.MLP([32, 32]))# Pass the input graphs to the graph network, and return the output graphs.output_graphs = graph_net_module(input_graphs)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='61'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='931' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#demo-jupyter-notebooks)Demo Jupyter notebooks

The library includes demos which show how to create, manipulate, and train graph networks to reason about graph-structured data, on a shortest path-finding task, a sorting task, and a physical prediction task. Each demo uses the same graph network architecture, which highlights the flexibility of the approach.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='62'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='934' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#try-the-demos-in-your-browser-in-colaboratory)Try the demos in your browser in [Colaboratory](https://colab.research.google.com/)

To try out the demos without installing anything locally, you can run the demos in your browser (even on your phone) via a cloud Colaboratory backend. Click a demo link below, and follow the instructions in the notebook.

* * *

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='63'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='937' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#run-shortest-path-demo-in-browser)[Run "shortest path demo" in browser](https://colab.research.google.com/github/deepmind/graph_nets/blob/master/graph_nets/demos/shortest_path.ipynb)

The "shortest path demo" creates random graphs, and trains a graph network to label the nodes and edges on the shortest path between any two nodes. Over a sequence of message-passing steps (as depicted by each step's plot), the model refines its prediction of the shortest path.

[![shortest-path.png](../_resources/e9f410c67cfadf0af91916af67e59c13.png)](https://github.com/deepmind/graph_nets/blob/master/images/shortest-path.png)

* * *

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='941' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#run-sort-demo-in-browser--run-tf2-version)[Run "sort demo" in browser](https://colab.research.google.com/github/deepmind/graph_nets/blob/master/graph_nets/demos/sort.ipynb)  [(Run TF2 version)](https://colab.research.google.com/github/deepmind/graph_nets/blob/master/graph_nets/demos_tf2/sort.ipynb)

The "sort demo" creates lists of random numbers, and trains a graph network to sort the list. After a sequence of message-passing steps, the model makes an accurate prediction of which elements (columns in the figure) come next after each other (rows).

[![sort.png](../_resources/0a66e3a302744edeec0bc31747a7a44d.png)](https://github.com/deepmind/graph_nets/blob/master/images/sort.png)

* * *

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='65'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='945' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#run-physics-demo-in-browser)[Run "physics demo" in browser](https://colab.research.google.com/github/deepmind/graph_nets/blob/master/graph_nets/demos/physics.ipynb)

The "physics demo" creates random mass-spring physical systems, and trains a graph network to predict the state of the system on the next timestep. The model's next-step predictions can be fed back in as input to create a rollout of a future trajectory. Each subplot below shows the true and predicted mass-spring system states over 50 steps. This is similar to the model and experiments in Battaglia et al. (2016)'s "interaction networks".

[![physics.png](../_resources/47bcd7899f65c5dceab95e06c19d0857.png)](https://github.com/deepmind/graph_nets/blob/master/images/physics.png)

* * *

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='66'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='949' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#run-graph-nets-basics-demo-in-browser)[Run "graph nets basics demo" in browser](https://colab.research.google.com/github/deepmind/graph_nets/blob/master/graph_nets/demos/graph_nets_basics.ipynb)

The "graph nets basics demo" is a tutorial containing step by step examples about how to create and manipulate graphs, how to feed them into graph networks and how to build custom graph network modules.

* * *

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='67'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='952' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#run-the-demos-on-your-local-machine)Run the demos on your local machine

To install the necessary dependencies, run:
$ pip install jupyter matplotlib scipy
To try the demos, run:
$ cd  <path-to-graph-nets-library>/demos
$ jupyter notebook
then open a demo through the Jupyter notebook interface.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='962' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/deepmind/graph_nets#other-graph-neural-network-libraries)Other graph neural network libraries

If you use PyTorch, check out these high-quality open-source libraries for graph neural networks:

- [pytorch_geometric](https://github.com/rusty1s/pytorch_geometric): See[MetaLayer](https://pytorch-geometric.readthedocs.io/en/latest/modules/nn.html#torch_geometric.nn.meta.MetaLayer)for an analog of our Graph Nets interface.
- [Deep Graph Library (DGL)](https://github.com/dmlc/dgl)