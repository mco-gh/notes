How do I run kubectl after image push? · Issue #22 · GoogleCloudPlatform/cloud-builders

 [New issue](https://github.com/GoogleCloudPlatform/cloud-builders/issues/new)

#    How do I run kubectl after image push?   #22

  Closed

 [DocBradfordSoftware](https://github.com/DocBradfordSoftware) opened this Issue  on Mar 20 · 19 comments

## Comments

Assignees
  No one assigned

Labels

None yet

Projects
  None yet

Milestone
No milestone

Notifications

You’re not receiving notifications from this thread.

6 participants

 [![@DocBradfordSoftware](../_resources/0302f97accc780bbcc2521d87098256c.jpg)  DocBradfordSoftware](https://github.com/DocBradfordSoftware)  [![@skelterjohn](../_resources/82d1b4b9efa9b041a8caf503ffca7286.png)  skelterjohn](https://github.com/skelterjohn)  [![@bussyjd](../_resources/9db335fd108cf01f9182489ee48503f9.png)  bussyjd](https://github.com/bussyjd)  [![@Philmod](../_resources/a7bce2295062c45952e59909e61525e2.jpg)  Philmod](https://github.com/Philmod)  [![@hamx0r](../_resources/ab3558f5948dea183783e964f762b99b.jpg)  hamx0r](https://github.com/hamx0r)  [![@dlsniper](../_resources/6ab79f44a9fc26b4dd7031a235866942.jpg)  dlsniper](https://github.com/dlsniper)

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [on Mar 20](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issue-215499264)

|     |
| --- |
| It would seem that a CI/CD pipeline would require the ability to deploy an image into the gke cluster after it was built/tested/pushed.<br>Without this, it seems like Builder is incomplete. |

 [![@skelterjohn](../_resources/82d1b4b9efa9b041a8caf503ffca7286.png)](https://github.com/skelterjohn)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [skelterjohn](https://github.com/skelterjohn)  ** commented [on Mar 20](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-287840853)

At the moment, you will have trouble using [object Object] from within the container builder service, since the credentials used do not have the proper scopes. We will address this issue soon.

For pushing before running another step, you can always run [object Object] as its own step (either instead of or in addition to listing the image in the [object Object] field).

[object Object]
(for an upcoming [object Object] step that is waiting on the scope issue)

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [on Mar 20](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-287880266)

|     |
| --- |
| Yes, that would work. Any idea if the scopes have to be added to the cluster and will it be able to be done after the fact.<br>I Built the gke/jenkins integration and I had to create a new cluster with the proper scope. |

 [![@skelterjohn](../_resources/82d1b4b9efa9b041a8caf503ffca7286.png)](https://github.com/skelterjohn)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [skelterjohn](https://github.com/skelterjohn)  ** commented [on Mar 20](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-287881733)

The scopes I'm referring to, which are used to create credentials for your builder service account (https://cloud.google.com/container-builder/docs/permissions), don't apply to any resources outside of the container builder service. So, scopes you use with your cluster are unrelated.

What's missing at this point is the ability to use the GKE cluster API to list your clusters and get the auth secrets necessary for talking to the cluster master. Once those secrets are acquired, you can use [object Object] to talk to the cluster master directly (and schedule pods, etc).

 [![@bussyjd](../_resources/f89c28aa5edeb4ef2573dc7965995e35.png)](https://github.com/bussyjd)

###   **  [bussyjd](https://github.com/bussyjd)  ** commented [on Mar 22](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-288323486)

|     |
| --- |
| I am very interested in this capability.<br>When can we expect to have the scope issue solved? Thanks a lot. |

 [![@Philmod](../_resources/502888eb79f76f3817735772d6d58e1d.jpg)](https://github.com/Philmod)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [Philmod](https://github.com/Philmod)  ** commented [on Mar 24](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-289064594)

The other solution is to create a Google Cloud Function that listens to the [object Object] PubSub feed, and update the appropriate deployment of your Kubernetes cluster.

In this [example](https://gist.github.com/Philmod/290fdabf386646dbbc0b57b00952b944), I have two repositories that map to two different deployments in a same namespace.

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [on Mar 25](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-289214839)

|     |
| --- |
| Well, that's pretty cool, [@Philmod](https://github.com/philmod), that should work in the interim. |

 [![@Philmod](../_resources/502888eb79f76f3817735772d6d58e1d.jpg)](https://github.com/Philmod)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [Philmod](https://github.com/Philmod)  ** commented [on Mar 26](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-289291987)

|     |
| --- |
| There is a second solution: store your GKE credentials in GCS that can be pulled and used as part of the build to deploy to Kubernetes. [Here](https://gist.github.com/Philmod/e18056caac485549bb5339ffa4fd31b5) is how you could pull and use the credentials in the build. |

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [on Apr 14](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-294215342) •  edited DocBradfordSoftware edited this comment 2 months ago

To expand on the above solution, I think these steps will work at this time.

In addition to the above link, this thread was useful [Here](https://github.com/kubernetes/kubernetes/issues/30617). In particular a comment by jlowdermilk.

You begin by going to IAM > Service accounts and creating a creating a service account and downloading the json key file. ex. [cloudbuild@my-project.iam.gserviceaccount.com](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-294215342mailto:cloudbuild@my-project.iam.gserviceaccount.com)

Then you add this service account to IAM and give it project editor access (the same as cloud builder, the difference is that later on this account will have the missing scopes).

1. On a machine with gcloud:
[object Object]

1. Copy these this file and the json key file to Cloud Storage. I removed all privleges except 'Owner' and then granted the service account ([cloudbuild@my-project.iam.gserviceaccount.com](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-294215342mailto:cloudbuild@my-project.iam.gserviceaccount.com)) read access. Not that this matters because this whole process is not very secure.

2. Then add a build step to cloudbuild.yaml
[object Object]
That seemed to work for me at this time.

###        This was referenced on Apr 20

    Open

####   [add docker-compose #10](https://github.com/GoogleCloudPlatform/cloud-builders/issues/10)

    Open

####   [Install kubectl in gcloud builder #2](https://github.com/GoogleCloudPlatform/cloud-builders/issues/2)

 [![@hamx0r](../_resources/b98534a89d885bd2de15c8d8cd60d261.jpg)](https://github.com/hamx0r)

###   **  [hamx0r](https://github.com/hamx0r)  ** commented [on Apr 28](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-297895581)

I found [this example](https://github.com/kelseyhightower/gif-maker-infrastructure/blob/master/cloudbuild-production-deploy.yaml) pretty helpful too. I'm using a custom cloudbuild.yaml which builds and pushes using [object Object] (a la [@skelterjohn](https://github.com/skelterjohn) 's suggestion), and then copies my kubernetes objects (yaml files) and kubeconfig file (also yaml) to a Bucket, and then from there to [object Object]. Now, I can use [object Object] build steps to run [object Object] commands where my credentials are available per the kubeconfig file. This snippet assumes all my kubeconfig and Kubernetes object YAML files are in a "kubernetes" folder/bucket:

[object Object]

 [![@Philmod](../_resources/502888eb79f76f3817735772d6d58e1d.jpg)](https://github.com/Philmod)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [Philmod](https://github.com/Philmod)  ** commented [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-306922677)

Hey!
Good news, the up-scoping feature is now live.

That means that you can add permission for Container Engine to your Cloudbuild service account, and then you can use kubectl directly in your build step:

[object Object]
Enjoy!

###         ![818310.jpg](../_resources/ef9c7fc7b179904adcbbc9c2b97bce40.jpg)  [Philmod](https://github.com/Philmod) closed this [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#event-1114430111)

 [![@dlsniper](../_resources/309ff7633bd1ff28f1357b5a33618e66.jpg)](https://github.com/dlsniper)

###   **  [dlsniper](https://github.com/dlsniper)  ** commented [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-306923349)

|     |
| --- |
| Awesome! Thank you! |

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-306924559)

|     |
| --- |
| This is good news, Thanks.<br>I assume that the minimum permission to add would be "Container Engine Developer" or is there something else? |

 [![@Philmod](../_resources/502888eb79f76f3817735772d6d58e1d.jpg)](https://github.com/Philmod)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [Philmod](https://github.com/Philmod)  ** commented [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-306925850)

|     |
| --- |
| Depends what you try to do, but for the example I posted, "Container Engine Developer" permission is indeed sufficient. |

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-306927084)

If we wanted to use hyperkube, because it was a lot faster, would the kubeconfig be located at /root/.kube/config?

[object Object]

 [![@Philmod](../_resources/502888eb79f76f3817735772d6d58e1d.jpg)](https://github.com/Philmod)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [Philmod](https://github.com/Philmod)  ** commented [7 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-306928290)

I'm not sure about hyperkube.

But I would guess you still need to authenticate to your cluster somehow. That's why I'm using:

[object Object]

 [![@skelterjohn](../_resources/82d1b4b9efa9b041a8caf503ffca7286.png)](https://github.com/skelterjohn)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [skelterjohn](https://github.com/skelterjohn)  ** commented [6 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-307109629)

hyperkube is the binary you use to run a local kubernetes cluster, right? In that case I bet it doesn't need authentication. If it does, the [object Object] command won't be able to fetch it - that command only talks to the GKE service which won't know about your hyperkube instance.

Regarding the example step you pasted, is that how hyperkube works? Do you really run [object Object]? I suspect you run [object Object] by itself, and then run [object Object] in another shell/process.

I don't have the time to try this myself, but a starting point might be...
[object Object]

I don't know how you tell kubectl to talk to the hyperkube, so you'd need to add that in the script in the second step.

 [![@hamx0r](../_resources/b98534a89d885bd2de15c8d8cd60d261.jpg)](https://github.com/hamx0r)

###   **  [hamx0r](https://github.com/hamx0r)  ** commented [6 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-307111433)

[@DocBradfordSoftware](https://github.com/docbradfordsoftware)  [@skelterjohn](https://github.com/skelterjohn) If you refer to my comment from on Apr 27, I link to a full working example of how to pass credentials to hypercube. It's done by passing a YAML file to hyperkube via Environment variable:

[object Object]

 [![@skelterjohn](../_resources/82d1b4b9efa9b041a8caf503ffca7286.png)](https://github.com/skelterjohn)

  Member This user is a member of the Google Cloud Platform organization.

###   **  [skelterjohn](https://github.com/skelterjohn)  ** commented [6 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-307114485)

Very nice, thank you. It looks like for hyperkube the right thing to do is indeed to run kubectl from within that image.

Though, in your example I don't understand why you first copy into GCS and then into /workspace. Why not [object Object]? Or better yet, forget the copy and set [object Object]?

 [![@DocBradfordSoftware](../_resources/6dc36288fbaf379ad857625c0432e8bf.jpg)](https://github.com/DocBradfordSoftware)

###   **  [DocBradfordSoftware](https://github.com/DocBradfordSoftware)  ** commented [6 days ago](https://github.com/GoogleCloudPlatform/cloud-builders/issues/22#issuecomment-307118797)

[@skelterjohn](https://github.com/skelterjohn) the reason we copy from gs to /workspace is because ~/.kube/config doesn't exist in the image. and until yesterday

[object Object]
wouldn't get the correct credentials to modify our deployments.
So now we just have to find .kube/config in order to pass it to hyperkube.

 [![@marcacohen](../_resources/c3a2ffa44015d8c7503ed773b9db1ffe.jpg)](https://github.com/marcacohen)

  Attach files by dragging & dropping, selecting them, or pasting from the clipboard.

 [ Styling with Markdown is supported](https://guides.github.com/features/mastering-markdown/)