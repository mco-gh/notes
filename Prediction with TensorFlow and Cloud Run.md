Prediction with TensorFlow and Cloud Run

# Prediction with TensorFlow and Cloud Run

[![2*ZX7q1RNRQv0wO4CklPa3CA.jpeg](../_resources/ae8cbbde0ede21905b84fc96a8d66110.jpg)](https://medium.com/@guillaume.blaquiere?source=post_page-----669c1c73ebd1----------------------)

[guillaume blaquiere](https://medium.com/@guillaume.blaquiere?source=post_page-----669c1c73ebd1----------------------)

[Sep 5](https://medium.com/google-cloud/portable-prediction-with-tensorflow-and-cloud-run-669c1c73ebd1?source=post_page-----669c1c73ebd1----------------------) · 5 min read

![1*mPJi8FHvfnig4KuXyCI5XA.png](../_resources/09c8bd6f49a14caa6fa1f781358d5d0d.png)
![1*mPJi8FHvfnig4KuXyCI5XA.png](../_resources/bcb5041acdc4a71aff8d07381af66916.png)

AI-Platform is a Google Cloud Platform (GCP) **service which propose tools and serverless compute for ML pipeline**. You can share, build, train and serve models in **full serverless way** on GCP, or wherever your want on your Kubernetes cluster thanks to [**Kubeflow**](https://github.com/kubeflow/kubeflow)** project**. You only have to focus on your business, on your model and your data processing/transformation.

Machine Learning pipeline has internal and external parts. Internally, your data-scientists can share, build and train/hypertune models, with GPU, TPU and much more features. **Using a single platform for this internal process is more efficient, and AI-Platform is really great for that.**

The external/visible part of ML pipeline is for end-user: the prediction serving part. **AI-Platform is also very convenient for deploying models** on GCP: easy, quick, serverless, “pay-as-you-use”. Sounds perfect…

But the trend is to *multi-cloud, hybrid*  *deployment* or *not vendor lock-in*, with, most of time, common keywords: ***container.***

*What’s the challenge?*

> I would like to leverage of container portability, and of serverless prediction serving like with AI-Platform.

The problem is that AI-Platform is Google specific and kubeflow isn’t serverless. Here comes [Knative](https://knative.dev/), on top of Kubernetes, which propose to build and serve with serverless experience for developers. GCP proposes a managed implementation of Knative: [**Cloud Run**](https://cloud.google.com/run/)**. **You can **run serverless stateless container.**

*I only used TensorFlow 1.x for building my model, and I will speak about it. However, *[*AI-Platform supports more frameworks*](https://cloud.google.com/deep-learning-vm/)

# Build a Cloud Run/Knative compliant container

Where to start ? AI-Platform do all, I don’t know what is done, how it’s processed. It’s the magic part of serverless, but also the most confusing: you don’t know what is really done!

> How a TensorFlow model is serving ?

[TensorFlow Extended (TFX)](https://www.tensorflow.org/tfx)is a part of TensorFlow for building end-to-end ML pipeline. One of the components is [TensorFlowServing](https://www.tensorflow.org/tfx/guide/serving). Hmm, sounds good for my problem. Let’s go deeper.

## TensorFlowServing

TensorFlowServing component is a [binary to install on linux](https://www.tensorflow.org/tfx/serving/setup) environment to serve TensorFlow models. This binary start a server with gRPC and RestAPI endpoint, on 2 different ports. Thereby, provide the model and the 2 ports, that’s all, your model is served! Far easier than expected!

***In bonus****,* there is also a [Docker image](https://www.tensorflow.org/tfx/serving/docker). Nothing to install, just run the image! Perfect it will be* easy to run it on Cloud Run*!!

Let’s try it and read the documentation. To run the container, you have to run this command

docker run -t --rm -p 8501:8501 \
-v "$TESTDATA/saved_model_half_plus:/models/half_plus_two" \
-e MODEL_NAME=half_plus_two \
tensorflow/serving &

**First issue:** you have to mount a volume into the container with the model for serving it. This breaks the *stateless *part of [contract](https://cloud.google.com/run/docs/reference/container-contract).

*No problem,* with docker, you can use this TensorFlowServing docker image as base image and build something on top of this. For example, something like that:

- Copy model into the container
- Set the model folder as `MODEL_NAME` variable.

FROM tensorflow/serving
COPY tf_models /models/tf_models
ENV MODEL_NAME tf_models

*Simple*! Your model is embedded in your container, the env var is defined. And, inherited from base image, the `tensorflow/serving` image automatically run this command

tensorflow_model_server --port=8500 --rest_api_port=8501 \
--model_name=${MODEL_NAME} \
--model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME}

**Second issue:** The server don’t listen on the `$PORT` environment variable of Cloud Run/Knative, and it’s not customizable.

Finally, it’s **not possible to use built-in TensorFlowServing docker image with Cloud Run/Knative: **contracts aren’t respected.

## Build TensorFlowServing custom image

Thereby, we have to build a TensorFlow serving image compliant with Cloud Run/Knative by ourselves.

For this, we have to write a `[Dockerfile](https://github.com/guillaumeblaquiere/cloudrun-tensorflow-prediction/blob/master/Dockerfile)`, let’s start with a Ubuntu Xenial image

FROM ubuntu:xenial
Install TensorFlowServing

RUN apt update && \apt-get install -y curl && \echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add - && \apt update && \apt-get install tensorflow-model-server

Copy the model to serve
COPY exporter /models/tf_models
Run the `tensorflow_model_server` with the right parameters

CMD tensorflow_model_server --port=8500 --rest_api_port=${PORT} --model_base_path=/models/tf_models --model_name=consumption

That’s all. Docker build, Docker run, it’s working.

> Potential issue: it’s not possible to deactivate the gRPC port (here 8500, default value). If Cloud Run/Knative `*$PORT*`> value is set to gRPC port value, the container start will fail

# Integrate with AI-Platform training step

Great, container is built! But, there is a breach between the training on AI-Platform and the serving container:

> How to retrieve the trained model?

Indeed, I never mention how the model was retrieve after the training. For this, I wrote a `[cloudbuild.yaml](https://github.com/guillaumeblaquiere/cloudrun-tensorflow-prediction/blob/master/cloudbuild.yaml)` for using [Cloud build](https://cloud.google.com/cloud-build/) with the [existing Cloud Builders](https://github.com/GoogleCloudPlatform/cloud-builders).

The first step retrieve the model from Google Cloud Storage with `gsutil` command: thus, models are available for being copied in the container. Then, build and push the container with `docker` command.

steps:

- name: 'gcr.io/cloud-builders/gsutil'

args: [ 'cp', '-r', '${_EXPORT_BUCKET}', '.' ]

- name: 'gcr.io/cloud-builders/docker'

args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/predict', '.' ]

- name: 'gcr.io/cloud-builders/docker'

args: ['push', 'gcr.io/$PROJECT_ID/predict']
images:

- 'gcr.io/$PROJECT_ID/predict'

substitutions:
_EXPORT_BUCKET: gs://my-bucket/path/to/export/exporter

**Now the breach is filled.** The trained model is exported to Google Cloud Storage, and get at the build stage of the container.

Great! Job done, you have a portable container for serving your trained model. Now, **you can deploy it and predict where you want!**

# Deploy on Cloud Run

All the hard work is done. Time to test and to **deploy on GCP serverless container platform: Cloud Run.**

First, deploy on Cloud Run
gcloud beta run deploy predict --image gcr.io/<PROJECT_ID>/predict

Then perform a request with an `instances.json` file (in relation with your model)

curl -X "content-type: application/json" -X POST -d [@instances](http://twitter.com/instances).json [https://predict-<hash>.run.app/v1/models/consumption:predict](https://predict-vqg64v3fcq-uc.a.run.app/v1/models/default:predict)

And *boom*, here the prediction
{
"predictions": [
{
"predicted": [5.77138042]
}
]
}