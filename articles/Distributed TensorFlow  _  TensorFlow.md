Distributed TensorFlow  |  TensorFlow

#  Distributed TensorFlow

- [Contents](https://www.tensorflow.org/deploy/distributed#top_of_page)
- [Hello distributed TensorFlow!](https://www.tensorflow.org/deploy/distributed#hello_distributed_tensorflow)
- [Create a cluster](https://www.tensorflow.org/deploy/distributed#create_a_cluster)
    - [Create a tf.train.ClusterSpec to describe the cluster](https://www.tensorflow.org/deploy/distributed#create_a_tftrainclusterspec_to_describe_the_cluster)
    - [Create a tf.train.Server instance in each task](https://www.tensorflow.org/deploy/distributed#create_a_tftrainserver_instance_in_each_task)

-
-
    -
-
-

This document shows how to create a cluster of TensorFlow servers, and how to distribute a computation graph across that cluster. We assume that you are familiar with the [basic concepts](https://www.tensorflow.org/get_started/index) of writing TensorFlow programs.

## [arrow_upward](https://www.tensorflow.org/deploy/distributed#top_of_page)Hello distributed TensorFlow!

To see a simple TensorFlow cluster in action, execute the following:
hdr_strong
content_copy

`# Start a TensorFlow server as a single-process "cluster".[[NEWLINE]]$ python[[NEWLINE]]>>> import tensorflow as tf[[NEWLINE]]>>> c = tf.constant("Hello, distributed TensorFlow!")[[NEWLINE]]>>> server = tf.train.Server.create_local_server()[[NEWLINE]]>>> sess = tf.Session(server.target)  # Create a session on the server.[[NEWLINE]]>>> sess.run(c)[[NEWLINE]]'Hello, distributed TensorFlow!'[[NEWLINE]]`

The[`tf.train.Server.create_local_server`](https://www.tensorflow.org/api_docs/python/tf/train/Server#create_local_server)method creates a single-process cluster, with an in-process server.

## [arrow_upward](https://www.tensorflow.org/deploy/distributed#top_of_page)Create a cluster

A TensorFlow "cluster" is a set of "tasks" that participate in the distributed execution of a TensorFlow graph. Each task is associated with a TensorFlow "server", which contains a "master" that can be used to create sessions, and a "worker" that executes operations in the graph. A cluster can also be divided into one or more "jobs", where each job contains one or more tasks.

To create a cluster, you start one TensorFlow server per task in the cluster. Each task typically runs on a different machine, but you can run multiple tasks on the same machine (e.g. to control different GPU devices). In each task, do the following:

1. **Create a `tf.train.ClusterSpec`** that describes all of the tasks in the cluster. This should be the same for each task.

2. **Create a `tf.train.Server`**, passing the `tf.train.ClusterSpec` to the constructor, and identifying the local task with a job name and task index.

### Create a `tf.train.ClusterSpec` to describe the cluster

The cluster specification dictionary maps job names to lists of network adresses. Pass this dictionary to the [`tf.train.ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)constructor. For example:

[object Object] construction
Available tasks
hdr_strong
tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
[object Object]
hdr_strong
tf.train.ClusterSpec({
"worker": [
"worker0.example.com:2222",
"worker1.example.com:2222",
"worker2.example.com:2222"
],
"ps": [
"ps0.example.com:2222",
"ps1.example.com:2222"
]})
[object Object]
[object Object]
[object Object]
[object Object]
[object Object]

### Create a `tf.train.Server` instance in each task

A [`tf.train.Server`](https://www.tensorflow.org/api_docs/python/tf/train/Server) object contains a set of local devices, a set of connections to other tasks in its`tf.train.ClusterSpec`, and a[`tf.Session`](https://www.tensorflow.org/api_docs/python/tf/Session) that can use these to perform a distributed computation. Each server is a member of a specific named job and has a task index within that job. A server can communicate with any other server in the cluster.

For example, to launch a cluster with two servers running on `localhost:2222`and `localhost:2223`, run the following snippets in two different processes on the local machine:

hdr_strong
content_copy

`# In task 0:[[NEWLINE]]cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})[[NEWLINE]]server = tf.train.Server(cluster, job_name="local", task_index=0)[[NEWLINE]]`

hdr_strong
content_copy

`# In task 1:[[NEWLINE]]cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})[[NEWLINE]]server = tf.train.Server(cluster, job_name="local", task_index=1)[[NEWLINE]]`

**Note:** Manually specifying these cluster specifications can be tedious, especially for large clusters. We are working on tools for launching tasks programmatically, e.g. using a cluster manager like[Kubernetes](http://kubernetes.io/). If there are particular cluster managers for which you'd like to see support, please raise a[GitHub issue](https://github.com/tensorflow/tensorflow/issues).

## [arrow_upward](https://www.tensorflow.org/deploy/distributed#top_of_page)Specifying distributed devices in your model

To place operations on a particular process, you can use the same[`tf.device`](https://www.tensorflow.org/api_docs/python/tf/device)function that is used to specify whether ops run on the CPU or GPU. For example:

hdr_strong
content_copy

`with tf.device("/job:ps/task:0"):[[NEWLINE]]  weights_1 = tf.Variable(...)[[NEWLINE]]  biases_1 = tf.Variable(...)[[NEWLINE]][[NEWLINE]]with tf.device("/job:ps/task:1"):[[NEWLINE]]  weights_2 = tf.Variable(...)[[NEWLINE]]  biases_2 = tf.Variable(...)[[NEWLINE]][[NEWLINE]]with tf.device("/job:worker/task:7"):[[NEWLINE]]  input, labels = ...[[NEWLINE]]  layer_1 = tf.nn.relu(tf.matmul(input, weights_1) + biases_1)[[NEWLINE]]  logits = tf.nn.relu(tf.matmul(layer_1, weights_2) + biases_2)[[NEWLINE]]  # ...[[NEWLINE]]  train_op = ...[[NEWLINE]][[NEWLINE]]with tf.Session("grpc://worker7.example.com:2222") as sess:[[NEWLINE]]  for _ in range(10000):[[NEWLINE]]    sess.run(train_op)[[NEWLINE]]`

In the above example, the variables are created on two tasks in the `ps` job, and the compute-intensive part of the model is created in the `worker`job. TensorFlow will insert the appropriate data transfers between the jobs (from `ps` to `worker` for the forward pass, and from `worker` to `ps` for applying gradients).

## [arrow_upward](https://www.tensorflow.org/deploy/distributed#top_of_page)Replicated training

A common training configuration, called "data parallelism," involves multiple tasks in a `worker` job training the same model on different mini-batches of data, updating shared parameters hosted in one or more tasks in a `ps`job. All tasks typically run on different machines. There are many ways to specify this structure in TensorFlow, and we are building libraries that will simplify the work of specifying a replicated model. Possible approaches include:

- **In-graph replication.** In this approach, the client builds a single `tf.Graph` that contains one set of parameters (in `tf.Variable` nodes pinned to `/job:ps`); and multiple copies of the compute-intensive part of the model, each pinned to a different task in `/job:worker`.
- **Between-graph replication.** In this approach, there is a separate client for each `/job:worker` task, typically in the same process as the worker task. Each client builds a similar graph containing the parameters (pinned to `/job:ps` as before using [`tf.train.replica_device_setter`](https://www.tensorflow.org/api_docs/python/tf/train/replica_device_setter) to map them deterministically to the same tasks); and a single copy of the compute-intensive part of the model, pinned to the local task in `/job:worker`.
- **Asynchronous training.** In this approach, each replica of the graph has an independent training loop that executes without coordination. It is compatible with both forms of replication above.
- **Synchronous training.** In this approach, all of the replicas read the same values for the current parameters, compute gradients in parallel, and then apply them together. It is compatible with in-graph replication (e.g. using gradient averaging as in the [CIFAR-10 multi-GPU trainer](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow_models/tutorials/image/cifar10/cifar10_multi_gpu_train.py)), and between-graph replication (e.g. using the [`tf.train.SyncReplicasOptimizer`](https://www.tensorflow.org/api_docs/python/tf/train/SyncReplicasOptimizer)).

### Putting it all together: example trainer program

The following code shows the skeleton of a distributed trainer program, implementing **between-graph replication** and **asynchronous training**. It includes the code for the parameter server and worker tasks.

hdr_strong
content_copy

`import argparse[[NEWLINE]]import sys[[NEWLINE]][[NEWLINE]]import tensorflow as tf[[NEWLINE]][[NEWLINE]]FLAGS = None[[NEWLINE]][[NEWLINE]]def main(_):[[NEWLINE]]  ps_hosts = FLAGS.ps_hosts.split(",")[[NEWLINE]]  worker_hosts = FLAGS.worker_hosts.split(",")[[NEWLINE]][[NEWLINE]]  # Create a cluster from the parameter server and worker hosts.[[NEWLINE]]  cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})[[NEWLINE]][[NEWLINE]]  # Create and start a server for the local task.[[NEWLINE]]  server = tf.train.Server(cluster,[[NEWLINE]]                           job_name=FLAGS.job_name,[[NEWLINE]]                           task_index=FLAGS.task_index)[[NEWLINE]][[NEWLINE]]  if FLAGS.job_name == "ps":[[NEWLINE]]    server.join()[[NEWLINE]]  elif FLAGS.job_name == "worker":[[NEWLINE]][[NEWLINE]]    # Assigns ops to the local worker by default.[[NEWLINE]]    with tf.device(tf.train.replica_device_setter([[NEWLINE]]        worker_device="/job:worker/task:%d" % FLAGS.task_index,[[NEWLINE]]        cluster=cluster)):[[NEWLINE]][[NEWLINE]]      # Build model...[[NEWLINE]]      loss = ...[[NEWLINE]]      global_step = tf.contrib.framework.get_or_create_global_step()[[NEWLINE]][[NEWLINE]]      train_op = tf.train.AdagradOptimizer(0.01).minimize([[NEWLINE]]          loss, global_step=global_step)[[NEWLINE]][[NEWLINE]]    # The StopAtStepHook handles stopping after running given steps.[[NEWLINE]]    hooks=[tf.train.StopAtStepHook(last_step=1000000)][[NEWLINE]][[NEWLINE]]    # The MonitoredTrainingSession takes care of session initialization,[[NEWLINE]]    # restoring from a checkpoint, saving to a checkpoint, and closing when done[[NEWLINE]]    # or an error occurs.[[NEWLINE]]    with tf.train.MonitoredTrainingSession(master=server.target,[[NEWLINE]]                                           is_chief=(FLAGS.task_index == 0),[[NEWLINE]]                                           checkpoint_dir="/tmp/train_logs",[[NEWLINE]]                                           hooks=hooks) as mon_sess:[[NEWLINE]]      while not mon_sess.should_stop():[[NEWLINE]]        # Run a training step asynchronously.[[NEWLINE]]        # See `tf.train.SyncReplicasOptimizer` for additional details on how to[[NEWLINE]]        # perform *synchronous* training.[[NEWLINE]]        # mon_sess.run handles AbortedError in case of preempted PS.[[NEWLINE]]        mon_sess.run(train_op)[[NEWLINE]][[NEWLINE]]if __name__ == "__main__":[[NEWLINE]]  parser = argparse.ArgumentParser()[[NEWLINE]]  parser.register("type", "bool", lambda v: v.lower() == "true")[[NEWLINE]]  # Flags for defining the tf.train.ClusterSpec[[NEWLINE]]  parser.add_argument([[NEWLINE]]      "--ps_hosts",[[NEWLINE]]      type=str,[[NEWLINE]]      default="",[[NEWLINE]]      help="Comma-separated list of hostname:port pairs"[[NEWLINE]]  )[[NEWLINE]]  parser.add_argument([[NEWLINE]]      "--worker_hosts",[[NEWLINE]]      type=str,[[NEWLINE]]      default="",[[NEWLINE]]      help="Comma-separated list of hostname:port pairs"[[NEWLINE]]  )[[NEWLINE]]  parser.add_argument([[NEWLINE]]      "--job_name",[[NEWLINE]]      type=str,[[NEWLINE]]      default="",[[NEWLINE]]      help="One of 'ps', 'worker'"[[NEWLINE]]  )[[NEWLINE]]  # Flags for defining the tf.train.Server[[NEWLINE]]  parser.add_argument([[NEWLINE]]      "--task_index",[[NEWLINE]]      type=int,[[NEWLINE]]      default=0,[[NEWLINE]]      help="Index of task within the job"[[NEWLINE]]  )[[NEWLINE]]  FLAGS, unparsed = parser.parse_known_args()[[NEWLINE]]  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)[[NEWLINE]]`

To start the trainer with two parameter servers and two workers, use the following command line (assuming the script is called `trainer.py`):

hdr_strong
content_copy

`# On ps0.example.com:[[NEWLINE]]$ python trainer.py \[[NEWLINE]]     --ps_hosts=ps0.example.com:2222,ps1.example.com:2222 \[[NEWLINE]]     --worker_hosts=worker0.example.com:2222,worker1.example.com:2222 \[[NEWLINE]]     --job_name=ps --task_index=0[[NEWLINE]]# On ps1.example.com:[[NEWLINE]]$ python trainer.py \[[NEWLINE]]     --ps_hosts=ps0.example.com:2222,ps1.example.com:2222 \[[NEWLINE]]     --worker_hosts=worker0.example.com:2222,worker1.example.com:2222 \[[NEWLINE]]     --job_name=ps --task_index=1[[NEWLINE]]# On worker0.example.com:[[NEWLINE]]$ python trainer.py \[[NEWLINE]]     --ps_hosts=ps0.example.com:2222,ps1.example.com:2222 \[[NEWLINE]]     --worker_hosts=worker0.example.com:2222,worker1.example.com:2222 \[[NEWLINE]]     --job_name=worker --task_index=0[[NEWLINE]]# On worker1.example.com:[[NEWLINE]]$ python trainer.py \[[NEWLINE]]     --ps_hosts=ps0.example.com:2222,ps1.example.com:2222 \[[NEWLINE]]     --worker_hosts=worker0.example.com:2222,worker1.example.com:2222 \[[NEWLINE]]     --job_name=worker --task_index=1[[NEWLINE]]`

## [arrow_upward](https://www.tensorflow.org/deploy/distributed#top_of_page)Glossary

**Client**

A client is typically a program that builds a TensorFlow graph and constructs a`tensorflow::Session` to interact with a cluster. Clients are typically written in Python or C++. A single client process can directly interact with multiple TensorFlow servers (see "Replicated training" above), and a single server can serve multiple clients.

**Cluster**

A TensorFlow cluster comprises a one or more "jobs", each divided into lists of one or more "tasks". A cluster is typically dedicated to a particular high-level objective, such as training a neural network, using many machines in parallel. A cluster is defined by a [`tf.train.ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec) object.

**Job**

A job comprises a list of "tasks", which typically serve a common purpose. For example, a job named `ps` (for "parameter server") typically hosts nodes that store and update variables; while a job named `worker` typically hosts stateless nodes that perform compute-intensive tasks. The tasks in a job typically run on different machines. The set of job roles is flexible: for example, a `worker` may maintain some state.

**Master service**

An RPC service that provides remote access to a set of distributed devices, and acts as a session target. The master service implements the`tensorflow::Session` interface, and is responsible for coordinating work across one or more "worker services". All TensorFlow servers implement the master service.

**Task**

A task corresponds to a specific TensorFlow server, and typically corresponds to a single process. A task belongs to a particular "job" and is identified by its index within that job's list of tasks.

**TensorFlow server** A process running a [`tf.train.Server`](https://www.tensorflow.org/api_docs/python/tf/train/Server) instance, which is a member of a cluster, and exports a "master service" and "worker service".

**Worker service**

An RPC service that executes parts of a TensorFlow graph using its local devices. A worker service implements [worker_service.proto](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/core/protobuf/worker_service.proto). All TensorFlow servers implement the worker service.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated April 26, 2017.