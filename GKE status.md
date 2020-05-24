GKE status

The team posts slides to [go/gke-slides](https://goto.google.com/gke-slides).

I don't think we have a comprehensive concise description of the current state.

1.6 hopefully will ship this month. It will (officially) scale to 5000 nodes and support etcd3. Spark integration is coming. A bunch of scheduling features will advance to beta (pod and node affinity/anti-affinity, taints and tolerations+forgiveness, multiple schedulers). DaemonSet rolling updates. Service catalog (fronting the Open Service Broker API) will be alpha, I think. Cluster federation is coming along.

You can see some top features of 1.5 here:
http://blog.kubernetes.io/2016/12/five-days-of-kubernetes-1.5.html

and 1.4:

http://blog.kubernetes.io/2016/09/kubernetes-1.4-making-it-easy-to-run-on-kuberentes-anywhere.html