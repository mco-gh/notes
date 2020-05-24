Using Google Container Engine API

# Using Google Container Engine API

 [ Ahmet Alp Balkan](https://ahmet.im/blog), on  19 June 2017

 [](https://ahmet.im/blog/gke-api/#article)

With about [150 services and going strong](https://developers.google.com/apis-explorer/) authenticating to Google APIs can sometimes seem intimidating to program against. In this blog post, I will take [Container Engine (GKE)](https://cloud.google.com/container-engine/) as an example and show how to use its[REST  API](https://cloud.google.com/container-engine/reference/rest/) in **Go** and **Python**.

**> Note:**>  This article does not explain how to use > [> Kubernetes> API](https://kubernetes.io/docs/reference/)>  to manage Pods, Deployments etc. Container Engine > API>  can be used to create/update/delete container clusters on Google Cloud.

## Where to start?

If you need the GKE  API to replicate a `gcloud` command, I recommend you begin with learning what endpoints `gcloud` calls:

$ gcloud container clusters list --log-http

Then you can play with the API yourself using [API Explorer](https://developers.google.com/apis-explorer/#search/container/container/v1/) without writing any code.

In the example programs below, you can find how to list a GKE cluster and its Node Pools. Based on the given pattern, you should be able to look up documentation to fit it to your use case.

## Authentication

Examples provided in this article will work without any configuration on your workstation if you authenticated to `gcloud`  CLI.

However, to authenticate to the API properly in other runtime environments, you must set up a service account:

1. [create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts),

2. [create a key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) for the service account, and

3. [assign roles](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts) to the service account (in this case Container Engine Viewer (`roles/container.viewer`) is sufficient to query resources)

4. set the [`GOOGLE_APPLICATION_CREDENTIALS` environment variable](https://cloud.google.com/docs/authentication/production) to point to the key file.

## Using Container API from Go

Normally, the Container Engine API client for Go is available at[cloud.google.com/go/container](https://godoc.org/cloud.google.com/go/container)package, but **it is now deprecated**. (It has been a hand-written layer with idiomatic API on top of the auto-generated library, and it has been a challenge to keep it up to date). So for our purposes, you will directly use the auto-generated client library.

First, retrieve the following dependencies:
go get google.golang.org/api/container/v1
go get google.golang.org/api/transport

These packages come from the[google-api-go-client](https://github.com/google/google-api-go-client)repository, which is a kitchen sink of the auto-generated code for most of public Google APIs. The[`container/v1`](https://godoc.org/google.golang.org/api/container/v1) package contains API calls and request/response types used in these calls. The`transport` package is for handling authentication smoothly, without exposing many details to you.

To list a cluster, simply initialize a client:

oauthClient,  _,  err  :=  transport.NewHTTPClient(context.TODO(),  option.WithScopes(gkev1.CloudPlatformScope))if  err  !=  nil  {  log.Fatalf("failed to initalize http client: %+v",  err)}gkeSvc,  err  :=  gkev1.New(oauthClient)if  err  !=  nil  {  log.Fatalf("failed to initialize gke client: %+v",  err)}

Then make a call to ListClusters:

clusterSvc  :=  gkev1.NewProjectsZonesClustersService(gkeSvc)list,  err  :=  clusterSvc.List(projectID,  zone).Do()if  err  !=  nil  {  return  fmt.Errorf("failed to list clusters: %+v",  err)}for  _,  v  :=  range  list.Clusters  {  fmt.Println(v.Name)}

You can find a complete program at the[GoogleCloudPlatform/golang-samples](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/container/listclusters)repository ([mirror](https://gist.github.com/ahmetb/d358aaacd970d3e9baf0cb9a52e0b041)).

## Using Container API from Python

[Google API Python Client](https://developers.google.com/api-client-library/python/) dynamically discovers APIs, endpoints and request/response types in the runtime using the discovery API. It’s a bit complicated to write code against something that is discovered in the runtime, but with the help of the documentation, it is doable:

First, install google-api-python-client:
$ pip install google-api-python-client
Initialize an API client for Container Service using dynamic API discovery:

from  apiclient.discovery  import  build...service  =  build('container',  'v1')

Now you can [follow the service documentation](https://developers.google.com/resources/api-libraries/documentation/container/v1/python/latest/index.html)and initialize a client as follows:

cl  =  service.projects().zones().clusters()
Then query the clusters and print their names:

list_resp  =  cl.list(projectId=PROJECT_ID,  zone=ZONE).execute()for  c  in  list_resp['clusters']:  print  c['name']

You can find a complete program at the[GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/container_engine/api-client)repository ([mirror](https://gist.github.com/ahmetb/441a91ccaef7e13afe4660909751e0bc)).

To run this example:
$ pip install google-api-python-client
$ python sample.py list_clusters_and_nodepools PROJECT_NAME ZONE
Cluster "test"  (RUNNING)  master_version=1.6.4
-> Pool "default-pool"  (RUNNING)  machine_type=n1-standard-1 autoscaling=False

I hope you enjoyed it. Let me know if you build anything on top of the GKE  RESTAPI and I can mention here in this article!

*(Thanks to my amazing teammates [@jonparrott](https://twitter.com/jonparrott) and[@broady](https://twitter.com/broady) for reviewing the drafts of this and publishing the sample programs.)*

* * *

 * If you liked this post, you can [follow me on Twitter](https://twitter.com/ahmetb) or [subscribe by email](https://feedburner.google.com/fb/a/mailverify?uri=ahmet-alp-balkan) to my blog (no more than an article/month). *

© 1999-2017 [Ahmet Alp Balkan](https://ahmet.im/).

[(L)](https://ahmet.im/blog/gke-api/#)Window size:  x
Viewport size:  x