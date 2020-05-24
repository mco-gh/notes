CoreOS

## Overview

etcd is a distributed key value store that provides a reliable way to store data across a cluster of machines. It’s open-source and available on GitHub. etcd gracefully handles leader elections during network partitions and will tolerate machine failure, including the leader.

Your applications can read and write data into etcd. A simple use-case is to store database connection details or feature flags in etcd as key value pairs. These values can be watched, allowing your app to reconfigure itself when they change.

Advanced uses take advantage of the consistency guarantees to implement database leader elections or do distributed locking across a cluster of workers.

#### More Information

[etcd Getting Started Guide](https://coreos.com/etcd/docs/latest/getting-started-with-etcd.html)

- [etcd Documentation](https://coreos.com/etcd/docs/latest/)•
- [etcd on GitHub](https://github.com/coreos/etcd/)•
- [Projects Using etcd](https://github.com/coreos/etcd/blob/master/Documentation/libraries-and-tools.md)

[   ![0.jpg](../_resources/8e24cb18f3923e571659325dd6b51586.jpg)      Introduction to etcd v3.0(28:11) ![CoreOS CTO Brandon Philips](../_resources/4d9f0f4a099269cbadf3ee7a6f17a529.png) Brandon Philips CoreOS CTO](https://www.youtube.com/watch?v=hQigKX0MxPw)

* * *

Projects using etcd

* * *

[(L)](http://kubernetes.io/)

etcd is the backend for service discovery and stores cluster state and configuration

[![CloudFoundry](../_resources/1d4b414c1ec5abff2f4740eeeb35e00c.png)](https://github.com/cloudfoundry/hm9000/)

etcd stores cluster state and configuration and provides a global lock service
[500+ projects on GitHub](https://github.com/search?utf8=%E2%9C%93&q=etcd/)
Including projects build on etcd, client bindings and more.

### Simple Interface

Read and write values with curl and other HTTP libraries

### Key/Value Storage

Store data in directories, similar to a file system
/configapp2app1

### Watch for Changes

Watch a key or directory for changes and react to the new values

* * *



#### Optional SSL client cert authentication



#### Benchmarked at 1000s of writes/s per instance



#### Optional TTLs for keys expiration



#### Properly distributed via Raft protocol

## Technical Overview

etcd is written in Go which has excellent cross-platform support, small binaries and a great community behind it. Communication between etcd machines is handled via the Raft consensus algorithm.

Latency from the etcd leader is the most important metric to track and the built-in dashboard has a view dedicated to this. In our testing, severe latency will introduce instability within the cluster because Raft is only as fast as the slowest machine in the majority. You can mitigate this issue by [properly tuning](https://coreos.com/etcd/docs/latest/tuning.html) the cluster. etcd has been pre-tuned on [cloud](https://coreos.com/docs/running-coreos/cloud-providers/ec2/)  [providers](https://coreos.com/docs/running-coreos/cloud-providers/rackspace/) with highly variable networks.

#### More Information

[Presentation: How Raft Works](https://speakerdeck.com/benbjohnson/raft-the-understandable-distributed-consensus-protocol/)

[followerfollowerfollowerfollowerleaderM](https://coreos.com/assets/images/media/Etcd-Replication.png)

Logs replicated to each follower in the cluster.