Deploy machine learning models in production - Cortex

Cortex is an open source platform for deploying machine learning models as production web services.

![v0.13_2.gif](../_resources/f88146d29d1d9f256da866ddd5f7a5ad.gif)
Demo

#

Key features[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='469'%3e%3cg data-evernote-id='470' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='471' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='472' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#key-features)

- **Multi framework:** Cortex supports TensorFlow, PyTorch, scikit-learn, XGBoost, and more.
- **Autoscaling:** Cortex automatically scales APIs to handle production workloads.
- **CPU / GPU support:** Cortex can run inference on CPU or GPU infrastructure.
- **Spot instances:** Cortex supports EC2 spot instances.
- **Rolling updates:** Cortex updates deployed APIs without any downtime.
- **Log streaming:** Cortex streams logs from deployed models to your CLI.
- **Prediction monitoring:** Cortex monitors network metrics and tracks predictions.
- **Minimal configuration:** Cortex deployments are defined in a single `cortex.yaml ` file.

#

Spinning up a cluster[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='553'%3e%3cg data-evernote-id='554' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='555' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='556' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#spinning-up-a-cluster)

Cortex is designed to be self-hosted on any AWS account. You can spin up a cluster with a single command:

![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='569'%3e%3cg data-evernote-id='570' class='js-evernote-checked'%3e%3crect x='9' y='9' width='13' height='13' rx='2' ry='2' data-evernote-id='571' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' data-evernote-id='572' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)Copy

1# install the CLI on your machine

2$ bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/0.13/get-cli.sh)"

3​
4# provision infrastructure on AWS and spin up a cluster
5$ cortex cluster up
6​
7aws region: us-west-2
8aws instance type: p2.xlarge
9spot instances: yes
10min instances: 0
11max instances: 10
12​
13￮ spinning up your cluster ...
14your cluster is ready!

#

Deploying a model[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='651'%3e%3cg data-evernote-id='652' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='653' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='654' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#deploying-a-model)

##

Implement your predictor[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='667'%3e%3cg data-evernote-id='668' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='669' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='670' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#implement-your-predictor)

![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='674'%3e%3cg data-evernote-id='675' class='js-evernote-checked'%3e%3crect x='9' y='9' width='13' height='13' rx='2' ry='2' data-evernote-id='676' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' data-evernote-id='677' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)Copy

15# predictor.py
16​
17class  PythonPredictor:
18  def  __init__(self, config):
19 self.model = download_model()
20​
21  def  predict(self, payload):
22  return model.predict(payload["text"])

##

Configure your deployment[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='768'%3e%3cg data-evernote-id='769' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='770' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='771' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#configure-your-deployment)

![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='775'%3e%3cg data-evernote-id='776' class='js-evernote-checked'%3e%3crect x='9' y='9' width='13' height='13' rx='2' ry='2' data-evernote-id='777' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' data-evernote-id='778' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)Copy

23# cortex.yaml
24​
25-  name: sentiment-classifier
26  predictor:
27  type: python
28  path: predictor.py
29  tracker:
30  model_type: classification
31  compute:
32  gpu:  1
33  mem: 4G

##

Deploy to AWS[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='865'%3e%3cg data-evernote-id='866' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='867' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='868' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#deploy-to-aws)

![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='872'%3e%3cg data-evernote-id='873' class='js-evernote-checked'%3e%3crect x='9' y='9' width='13' height='13' rx='2' ry='2' data-evernote-id='874' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' data-evernote-id='875' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)Copy

34$ cortex deploy
35​
36creating sentiment-classifier

##

Serve real-time predictions[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='894'%3e%3cg data-evernote-id='895' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='896' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='897' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#serve-real-time-predictions)

![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='901'%3e%3cg data-evernote-id='902' class='js-evernote-checked'%3e%3crect x='9' y='9' width='13' height='13' rx='2' ry='2' data-evernote-id='903' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' data-evernote-id='904' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)Copy

37$ curl http://***.amazonaws.com/sentiment-classifier \
38 -X POST -H "Content-Type: application/json" \
39 -d '{"text": "the movie was amazing!"}'
40​
41positive

##

Monitor your deployment[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='940'%3e%3cg data-evernote-id='941' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='942' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='943' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#monitor-your-deployment)

![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='947'%3e%3cg data-evernote-id='948' class='js-evernote-checked'%3e%3crect x='9' y='9' width='13' height='13' rx='2' ry='2' data-evernote-id='949' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' data-evernote-id='950' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)Copy

42$ cortex get sentiment-classifier --watch
43​
44status up-to-date requested last update avg inference 2XX
45live 1 1 8s 24ms 12
46​
47class count
48positive 8
49negative 4

#

What is Cortex similar to?[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='985'%3e%3cg data-evernote-id='986' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='987' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='988' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#what-is-cortex-similar-to)

Cortex is an open source alternative to serving models with SageMaker or building your own model deployment platform on top of AWS services like Elastic Kubernetes Service (EKS), Elastic Container Service (ECS), Lambda, Fargate, and Elastic Compute Cloud (EC2) and open source projects like Docker, Kubernetes, and TensorFlow Serving.

#

How does Cortex work?[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='1005'%3e%3cg data-evernote-id='1006' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='1007' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='1008' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#how-does-cortex-work)

The CLI sends configuration and code to the cluster every time you run `cortex deploy `. Each model is loaded into a Docker container, along with any Python packages and request handling code. The model is exposed as a web service using Elastic Load Balancing (ELB), TensorFlow Serving, and ONNX Runtime. The containers are orchestrated on Elastic Kubernetes Service (EKS) while logs and metrics are streamed to CloudWatch.

#

Examples of Cortex deployments[![](data:image/svg+xml,%3csvg preserveAspectRatio='xMidYMid meet' height='1em' width='1em' fill='none' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' stroke='currentColor' class='icon-7f6730be--text-3f89f380 js-evernote-checked' data-evernote-id='1028'%3e%3cg data-evernote-id='1029' class='js-evernote-checked'%3e%3cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71' data-evernote-id='1030' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71' data-evernote-id='1031' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://www.cortex.dev/#examples-of-cortex-deployments)

- ​[Sentiment analysis](https://github.com/cortexlabs/cortex/tree/0.13/examples/tensorflow/sentiment-analyzer): deploy a BERT model for sentiment analysis.
- ​[Image classification](https://github.com/cortexlabs/cortex/tree/0.13/examples/tensorflow/image-classifier): deploy an Inception model to classify images.
- ​[Search completion](https://github.com/cortexlabs/cortex/tree/0.13/examples/pytorch/search-completer): deploy Facebook's RoBERTa model to complete search terms.
- ​[Text generation](https://github.com/cortexlabs/cortex/tree/0.13/examples/pytorch/text-generator): deploy Hugging Face's DistilGPT2 model to generate text.
- ​[Iris classification](https://github.com/cortexlabs/cortex/tree/0.13/examples/sklearn/iris-classifier): deploy a scikit-learn model to classify iris flowers.