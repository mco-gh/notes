CI/CD for Jupyter Notebooks - Incipience of Technology

   [Incipience.io](https://www.incipience.io/blog/)

- [Home](https://www.incipience.io/blog/)

- [Archives](https://www.incipience.io/blog/archives)

# CI/CD for Jupyter Notebooks

 [#jupyter notebook](https://www.incipience.io/blog/tags/jupyter-notebook/)  [#ci/cd](https://www.incipience.io/blog/tags/ci-cd/)  [#continuous integration](https://www.incipience.io/blog/tags/continuous-integration/)  [#continuous delivery](https://www.incipience.io/blog/tags/continuous-delivery/)  [#deep learning](https://www.incipience.io/blog/tags/deep-learning/)  [#google cloud ai](https://www.incipience.io/blog/tags/google-cloud-ai/)

 [Machine Learning](https://www.incipience.io/blog/categories/machine-learning/)/ [Jupyter Notebook](https://www.incipience.io/blog/categories/machine-learning/jupyter-notebook/)

A long long time ago, when mammoths were still peacefully eating the grass, software industry has come to some best practices, in particular, Continuous Integration (CI) and Continuous Delivery/Deployment (CD). In fact, CI/CD is not just a collection of practices. It’s more a culture, set of operating principles, allowing teams to focus on the product excellence rather than on the operational work.

AI and ML space is still in the era of development of these best practices. This article demonstrates some of the use cases and considerations around Jupyter notebooks that you may find helpful.

## [(L)](https://www.incipience.io/blog/jupyter-notebooks-ci-cd/#Reproducible-Jupyter-Notebooks)Reproducible Jupyter Notebooks

The major difficulty of building CI/CD for Jupyter notebooks is the fact that generally the notebook will only work in the same environment where it was was created. There are many aspects of this problem, but the main one is the notebook dependencies.

So, the first step in building CI/CD for Jupyter notebooks is to make sure that we can reliably re-run the notebooks.

The topic of Jupyter notebooks reproducibility is big enough to deserve a dedicated post.

But the generic idea is that the Jupyter stores information about its Deep Learning environment, as well as list of additional dependencies into the notebook metadata.

(this functionality currently works only in the test Deep Learning images of Google Cloud AI)

## [(L)](https://www.incipience.io/blog/jupyter-notebooks-ci-cd/#Continuous-Integration-of-Jupyter-Notebooks)Continuous Integration of Jupyter Notebooks

Let’s assume that you store you notebooks in some code repository, like git.

Then, your logical wish would be to have some sort of CI which, at very least, validates that all committed notebooks are “functional” and don’t have syntax errors.

You can find an example of such a CI in [this sample project](https://github.com/gclouduniverse/notebooks-ci-showcase/tree/repro_nb_based_pipeline).

The major piece of this project is a [Cloud Build configuration file](https://github.com/gclouduniverse/notebooks-ci-showcase/blob/repro_nb_based_pipeline/cloudbuild.yaml).

This build configuration has just 3 steps.

First two steps clone the repository and checkout the commit which triggered the build:

|     |
| --- |
| - name: 'gcr.io/cloud-builders/git'<br>id: 'clone'<br>args: ['clone', '--recurse-submodules', '--branch', 'repro_nb_based_pipeline', 'https://github.com/gclouduniverse/notebooks-ci-showcase']<br>- name: 'gcr.io/cloud-builders/git'<br>id: 'checkout'<br>args: ['checkout', '$COMMIT_SHA']<br>dir: 'notebooks-ci-showcase' |

The last step installs the gcloud-notebook-training tool, and then submits Google Cloud AI Training Job for each of the notebooks from the commit.

|     |
| --- |
| - name: 'docker.io/library/python:3.7'<br>id: 'train'<br>args: ['bash', '-c', 'pip install gcloud-notebook-training && git show --name-only $COMMIT_SHA \| grep -i .ipynb \| xargs -I gcloud-notebook-training --input-notebook']<br>dir: 'notebooks-ci-showcase'<br>timeout: 7200s |

We are using python 3.7 Docker container here, and the gcloud-notebook-training tool.

gcloud-notebook-training is a simple tool which accepts the following parameters:

|     |
| --- |
| gcloud-notebook-training [-h] --input-notebook INPUT_NOTEBOOK<br>[--project-id PROJECT_ID]<br>[--output-notebook OUTPUT_NOTEBOOK]<br>[--job-id JOB_ID]<br>[--region REGION]<br>[--worker-machine-type WORKER_MACHINE_TYPE]<br>[--bucket-name BUCKET_NAME]<br>[--max-running-time MAX_RUNNING_TIME]<br>[--container-uri CONTAINER_URI]<br>[--accelerator-type ACCELERATOR_TYPE] |

You can find the sources of this tool as well as its description [here](https://github.com/gclouduniverse/notebook_training).

gcloud-notebook-training is able to read meta-information from the notebook about its environment. It allows the tool to submit the training job for the notebook with the same DL environment, that was used to create and run this notebook.

The last step is to hook this cloudbuild definition to our git repository.
It can be easily done on the GCP Cloud Build page.

## [(L)](https://www.incipience.io/blog/jupyter-notebooks-ci-cd/#Continuous-Delivery-of-Jupyter-Notebooks)Continuous Delivery of Jupyter Notebooks

Let’s consider a different scenario. We have notebooks which define different stages of some ML pipeline.

We can have separate notebooks for data cleaning, data processing, training the model, testing the model and so on.

And again, we want to run the entire chain of the notebooks every time when someone changes one of the notebooks.

We may also want to run the entire chain daily, based on a schedule.

[This example](https://github.com/gclouduniverse/notebooks-ci-showcase/blob/notebook_based_pipeline/cloudbuild.yaml) demonstrates Continuous Delivery solution based on the Jupyter notebooks.

We assume here that each of the notebooks in the chain is “self-contained”, meaning that it can run independently and that it downloads input and uploads output data to some external storage, in our example it’s GCS.

Like in the previous example we submit our notebooks to Cloud AI Training Job.

The only difference is that we submit them sequentially and then, at the end of the flow, we submit the result to Cloud AI Prediction services (inference).

|     |
| --- |
| - name: 'gcr.io/deeplearning-platform-release/base-cpu:m39'<br>id: 'deploy'<br>dir: 'notebooks-ci-showcase'<br>args: ['$COMMIT_SHA']<br>entrypoint: './deploy_model_for_inference.sh' |

The core part of the [deploy_model_for_inference.sh](https://github.com/gclouduniverse/notebooks-ci-showcase/blob/notebook_based_pipeline/deploy_model_for_inference.sh) is the following call:

|     |
| --- |
| gcloud ai-platform versions create "${VERSION_NAME}" \<br>--model "${MODEL_NAME}" \<br>--origin "${GCS_MODEL_DIR}" \<br>--runtime-version=1.14 \<br>--framework "${FRAMEWORK}" \<br>--python-version=3.5 \<br>--project "${PROJECT_ID}" |

The above example contains only two simple notebooks in the chain, but it demonstrates how Continuous Delivery can be built based on Jupyter notebooks.

Notebooks based Continuous Delivery may be not the optimal solution in big projects.

[Kubeflow Pipelines](https://www.kubeflow.org/docs/pipelines/), [TensorFlow Extended Pipelines](https://www.tensorflow.org/tfx) may be better solutions for many (or even most) cases.

However, in many scenarios Notebooks based Continuous Delivery has its own advantages, mainly due to its simplicity.

 [Share]()

Posted by Yuri Chernikov on 2020-03-24

* * *

### Comments:

0 Comments
Sort by

[Oldest**](https://www.facebook.com/plugins/feedback.php?app_id=552679615361057&channel=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D46%23cb%3Df2d46dcc6b88bc%26domain%3Dwww.incipience.io%26origin%3Dhttps%253A%252F%252Fwww.incipience.io%252Ff18eb6206009a%26relation%3Dparent.parent&color_scheme=light&container_width=778&height=100&href=https%3A%2F%2Fwww.incipience.io%2Fblog%2Fjupyter-notebooks-ci-cd%2Findex.html&locale=en_US&sdk=joey#)

.

[![odA9sNLrE86.jpg](../_resources/f04f15ed225fbf9390c6cac221a2fb85.jpg)](https://www.facebook.com/plugins/feedback.php?app_id=552679615361057&channel=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D46%23cb%3Df2d46dcc6b88bc%26domain%3Dwww.incipience.io%26origin%3Dhttps%253A%252F%252Fwww.incipience.io%252Ff18eb6206009a%26relation%3Dparent.parent&color_scheme=light&container_width=778&height=100&href=https%3A%2F%2Fwww.incipience.io%2Fblog%2Fjupyter-notebooks-ci-cd%2Findex.html&locale=en_US&sdk=joey)

.
\a

.

**

[Facebook Comments Plugin](https://developers.facebook.com/products/social-plugins/comments/?utm_campaign=social_plugins&utm_medium=offsite_pages&utm_source=comments_plugin)

.

* * *

© 2020 incipience.io