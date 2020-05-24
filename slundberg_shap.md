slundberg/shap

 [![shap_diagram.png](../_resources/fb85e68193e8aafde609d6909046e1c4.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/shap_diagram.png)

* * *

[![68747470733a2f2f7472617669732d63692e6f72672f736c756e64626572672f736861702e7376673f6272616e63683d6d6173746572](../_resources/087bbac58300ac5d38e541f4c3d661f2.png)](https://travis-ci.org/slundberg/shap)

**SHAP (SHapley Additive exPlanations)** is a unified approach to explain the output of any machine learning model. SHAP connects game theory with local explanations, uniting several previous methods [1-7] and representing the only possible consistent and locally accurate additive feature attribution method based on expectations (see our [papers](https://github.com/slundberg/shap#citations) for details).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='264'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1256' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#install)Install

SHAP can be installed from either [PyPI](https://pypi.org/project/shap) or [conda-forge](https://anaconda.org/conda-forge/shap):

pip install shap*or*conda install -c conda-forge shap

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='265'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1260' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#tree-ensemble-example-with-treeexplainer-xgboostlightgbmcatboostscikit-learn-models)Tree ensemble example with TreeExplainer (XGBoost/LightGBM/CatBoost/scikit-learn models)

While SHAP values can explain the output of any machine learning model, we have developed a high-speed exact algorithm for tree ensemble methods ([Tree SHAP arXiv paper](https://arxiv.org/abs/1802.03888)). Fast C++ implementations are supported for *XGBoost*, *LightGBM*, *CatBoost*, and *scikit-learn* tree models:

import xgboostimport shap# load JS visualization code to notebookshap.initjs()# train XGBoost modelX,y = shap.datasets.boston()

model = xgboost.train({"learning_rate": 0.01}, xgboost.DMatrix(X, label=y), 100)# explain the model's predictions using SHAP values# (same syntax works for LightGBM, CatBoost, and scikit-learn models)explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)# visualize the first prediction's explanation (use matplotlib=True to avoid Javascript)shap.force_plot(explainer.expected_value, shap_values[0,:], X.iloc[0,:])

 [![boston_instance.png](../_resources/388aabc9318855e327e570de00359744.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/boston_instance.png)

The above explanation shows features each contributing to push the model output from the base value (the average model output over the training dataset we passed) to the model output. Features pushing the prediction higher are shown in red, those pushing the prediction lower are in blue (these force plots are introduced in our [Nature BME paper](https://www.nature.com/articles/s41551-018-0304-0)).

If we take many explanations such as the one shown above, rotate them 90 degrees, and then stack them horizontally, we can see explanations for an entire dataset (in the notebook this plot is interactive):

# visualize the training set predictionsshap.force_plot(explainer.expected_value, shap_values, X)

 [![boston_dataset.png](../_resources/4855b959ae6e5c6974bcc1a3d304bf5c.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/boston_dataset.png)

To understand how a single feature effects the output of the model we can plot the SHAP value of that feature vs. the value of the feature for all the examples in a dataset. Since SHAP values represent a feature's responsibility for a change in the model output, the plot below represents the change in predicted house price as RM (the average number of rooms per house in an area) changes. Vertical dispersion at a single value of RM represents interaction effects with other features. To help reveal these interactions `dependence_plot` automatically selects another feature for coloring. In this case coloring by RAD (index of accessibility to radial highways) highlights that the average number of rooms per house has less impact on home price for areas with a high RAD value.

# create a SHAP dependence plot to show the effect of a single feature across the whole datasetshap.dependence_plot("RM", shap_values, X)

 [![boston_dependence_plot.png](../_resources/cf8863c5b4e8fb3c3775725507bc9be9.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/boston_dependence_plot.png)

To get an overview of which features are most important for a model we can plot the SHAP values of every feature for every sample. The plot below sorts features by the sum of SHAP value magnitudes over all samples, and uses SHAP values to show the distribution of the impacts each feature has on the model output. The color represents the feature value (red high, blue low). This reveals for example that a high LSTAT (% lower status of the population) lowers the predicted home price.

# summarize the effects of all the featuresshap.summary_plot(shap_values, X)

 [![boston_summary_plot.png](../_resources/348f9c1f4dd39c1c1b70cfe43241b2fd.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/boston_summary_plot.png)

We can also just take the mean absolute value of the SHAP values for each feature to get a standard bar plot (produces stacked bars for multi-class outputs):

shap.summary_plot(shap_values, X, plot_type="bar")

 [![boston_summary_plot_bar.png](../_resources/90b0a149f2ecda36e82ca0efe8236cd3.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/boston_summary_plot_bar.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='266'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1282' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#deep-learning-example-with-deepexplainer-tensorflowkeras-models)Deep learning example with DeepExplainer (TensorFlow/Keras models)

Deep SHAP is a high-speed approximation algorithm for SHAP values in deep learning models that builds on a connection with [DeepLIFT](https://arxiv.org/abs/1704.02685) described in the SHAP NIPS paper. The implementation here differs from the original DeepLIFT by using a distribution of background samples instead of a single reference value, and using Shapley equations to linearize components such as max, softmax, products, divisions, etc. Note that some of these enhancements have also been since integrated into DeepLIFT. TensorFlow models and Keras models using the TensorFlow backend are supported (there is also preliminary support for PyTorch):

# ...include code from https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.pyimport shapimport numpy as np# select a set of background examples to take an expectation overbackground = x_train[np.random.choice(x_train.shape[0], 100, replace=False)]# explain predictions of the model on four imagese = shap.DeepExplainer(model, background)# ...or pass tensors directly# e = shap.DeepExplainer((model.layers[0].input, model.layers[-1].output), background)shap_values = e.shap_values(x_test[1:5])# plot the feature attributionsshap.image_plot(shap_values, -x_test[1:5])

 [![mnist_image_plot.png](../_resources/13c0b9739258876c86b0ac1b23f094e6.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/mnist_image_plot.png)

The plot above explains ten outputs (digits 0-9) for four different images. Red pixels increase the model's output while blue pixels decrease the output. The input images are shown on the left, and as nearly transparent grayscale backings behind each of the explanations. The sum of the SHAP values equals the difference between the expected model output (averaged over the background dataset) and the current model output. Note that for the 'zero' image the blank middle is important, while for the 'four' image the lack of a connection on top makes it a four instead of a nine.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='267'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1288' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#deep-learning-example-with-gradientexplainer-tensorflowkeraspytorch-models)Deep learning example with GradientExplainer (TensorFlow/Keras/PyTorch models)

Expected gradients combines ideas from [Integrated Gradients](https://arxiv.org/abs/1703.01365), SHAP, and [SmoothGrad](https://arxiv.org/abs/1706.03825) into a single expected value equation. This allows an entire dataset to be used as the background distribution (as opposed to a single reference value) and allows local smoothing. If we approximate the model with a linear function between each background data sample and the current input to be explained, and we assume the input features are independent then expected gradients will compute approximate SHAP values. In the example below we have explained how the 7th intermediate layer of the VGG16 ImageNet model impacts the output probabilities.

from keras.applications.vgg16 import  VGG16from keras.applications.vgg16 import preprocess_inputimport keras.backend as Kimport numpy as npimport jsonimport shap# load pre-trained model and choose two images to explainmodel = VGG16(weights='imagenet', include_top=True)

X,y = shap.datasets.imagenet50()

to_explain = X[[39,41]]# load the ImageNet class namesurl =  "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"fname = shap.datasets.cache(url)with  open(fname) as f:

class_names = json.load(f)# explain how the input to the 7th layer of the model explains the top two classesdef  map2layer(x, layer):

feed_dict =  dict(zip([model.layers[0].input], [preprocess_input(x.copy())])) return K.get_session().run(model.layers[layer].input, feed_dict)

e = shap.GradientExplainer(
(model.layers[7].input, model.layers[-1].output),
map2layer(X, 7), local_smoothing=0  # std dev of smoothing noise)

shap_values,indexes = e.shap_values(map2layer(to_explain, 7), ranked_outputs=2)# get the names for the classesindex_names = np.vectorize(lambda  x: class_names[str(x)][1])(indexes)# plot the explanationsshap.image_plot(shap_values, to_explain, index_names)

 [![gradient_imagenet_plot.png](../_resources/3acab21469b2afd94b135923ec5e6d4c.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/gradient_imagenet_plot.png)

Predictions for two input images are explained in the plot above. Red pixels represent positive SHAP values that increase the probability of the class, while blue pixels represent negative SHAP values the reduce the probability of the class. By using `ranked_outputs=2` we explain only the two most likely classes for each input (this spares us from explaining all 1,000 classes).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='268'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1294' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#model-agnostic-example-with-kernelexplainer-explains-any-function)Model agnostic example with KernelExplainer (explains any function)

Kernel SHAP uses a specially-weighted local linear regression to estimate SHAP values for any model. Below is a simple example for explaining a multi-class SVM on the classic iris dataset.

import sklearnimport shapfrom sklearn.model_selection import train_test_split# print the JS visualization code to the notebookshap.initjs()# train a SVM classifierX_train,X_test,Y_train,Y_test = train_test_split(*shap.datasets.iris(), test_size=0.2, random_state=0)

svm = sklearn.svm.SVC(kernel='rbf', probability=True)

svm.fit(X_train, Y_train)# use Kernel SHAP to explain test set predictionsexplainer = shap.KernelExplainer(svm.predict_proba, X_train, link="logit")

shap_values = explainer.shap_values(X_test, nsamples=100)# plot the SHAP values for the Setosa output of the first instanceshap.force_plot(explainer.expected_value[0], shap_values[0][0,:], X_test.iloc[0,:], link="logit")

 [![iris_instance.png](../_resources/ab5501b24339428334087209e47450dc.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/iris_instance.png)

The above explanation shows four features each contributing to push the model output from the base value (the average model output over the training dataset we passed) towards zero. If there were any features pushing the class label higher they would be shown in red.

If we take many explanations such as the one shown above, rotate them 90 degrees, and then stack them horizontally, we can see explanations for an entire dataset. This is exactly what we do below for all the examples in the iris test set:

# plot the SHAP values for the Setosa output of all instancesshap.force_plot(explainer.expected_value[0], shap_values[0], X_test, link="logit")

 [![iris_dataset.png](../_resources/1f5192029ba22a9209ac40ee6526b2f4.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/iris_dataset.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='269'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1303' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#shap-interaction-values)SHAP Interaction Values

SHAP interaction values are a generalization of SHAP values to higher order interactions. Fast exact computation of pairwise interactions are implemented for tree models with `shap.TreeExplainer(model).shap_interaction_values(X)`. This returns a matrix for every prediction, where the main effects are on the diagonal and the interaction effects are off-diagonal. These values often reveal interesting hidden relationships, such as how the increased risk of death peaks for men at age 60 (see the NHANES notebook for details):

 [![nhanes_age_sex_interaction.png](../_resources/a636e18c1b0dfe0bb0792830b3035869.png)](https://raw.githubusercontent.com/slundberg/shap/master/docs/artwork/nhanes_age_sex_interaction.png)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='270'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1307' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#sample-notebooks)Sample notebooks

The notebooks below demonstrate different use cases for SHAP. Look inside the notebooks directory of the repository if you want to try playing with the original notebooks yourself.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='271'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1310' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#treeexplainer)TreeExplainer

An implementation of Tree SHAP, a fast and exact algorithm to compute SHAP values for trees and ensembles of trees.

- [**NHANES survival model with XGBoost and SHAP interaction values**](https://slundberg.github.io/shap/notebooks/NHANES%20I%20Survival%20Model.html) - Using mortality data from 20 years of followup this notebook demonstrates how to use XGBoost and `shap` to uncover complex risk factor relationships.
- [**Census income classification with LightGBM**](https://slundberg.github.io/shap/notebooks/Census%20income%20classification%20with%20LightGBM.html) - Using the standard adult census income dataset, this notebook trains a gradient boosting tree model with LightGBM and then explains predictions using `shap`.
- [**League of Legends Win Prediction with XGBoost**](https://slundberg.github.io/shap/notebooks/League%20of%20Legends%20Win%20Prediction%20with%20XGBoost.html) - Using a Kaggle dataset of 180,000 ranked matches from League of Legends we train and explain a gradient boosting tree model with XGBoost to predict if a player will win their match.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='272'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1320' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#deepexplainer)DeepExplainer

An implementation of Deep SHAP, a faster (but only approximate) algorithm to compute SHAP values for deep learning models that is based on connections between SHAP and the DeepLIFT algorithm.

- [**MNIST Digit classification with Keras**](https://slundberg.github.io/shap/notebooks/deep_explainer/Front%20Page%20DeepExplainer%20MNIST%20Example.html) - Using the MNIST handwriting recognition dataset, this notebook trains a neural network with Keras and then explains predictions using `shap`.
- [**Keras LSTM for IMDB Sentiment Classification**](https://slundberg.github.io/shap/notebooks/deep_explainer/Keras%20LSTM%20for%20IMDB%20Sentiment%20Classification.html) - This notebook trains an LSTM with Keras on the IMDB text sentiment analysis dataset and then explains predictions using `shap`.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='273'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1328' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#gradientexplainer)GradientExplainer

An implementation of expected gradients to approximate SHAP values for deep learning models. It is based on connections between SHAP and the Integrated Gradients algorithm. GradientExplainer is slower than DeepExplainer and makes different approximation assumptions.

- [**Explain an Intermediate Layer of VGG16 on ImageNet**](https://slundberg.github.io/shap/notebooks/gradient_explainer/Explain%20an%20Intermediate%20Layer%20of%20VGG16%20on%20ImageNet.html) - This notebook demonstrates how to explain the output of a pre-trained VGG16 ImageNet model using an internal convolutional layer.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='274'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1333' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#linearexplainer)LinearExplainer

For a linear model with independent features we can analytically compute the exact SHAP values. We can also account for feature correlation if we are willing to estimate the feature covaraince matrix. LinearExplainer supports both of these options.

- [**Sentiment Analysis with Logistic Regression**](https://slundberg.github.io/shap/notebooks/linear_explainer/Sentiment%20Analysis%20with%20Logistic%20Regression.html) - This notebook demonstrates how to explain a linear logistic regression sentiment analysis model.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='275'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1338' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#kernelexplainer)KernelExplainer

An implementation of Kernel SHAP, a model agnostic method to estimate SHAP values for any model. Because it makes not assumptions about the model type, KernelExplainer is slower than the other model type specific algorithms.

- [**Census income classification with scikit-learn**](https://slundberg.github.io/shap/notebooks/Census%20income%20classification%20with%20scikit-learn.html) - Using the standard adult census income dataset, this notebook trains a k-nearest neighbors classifier using scikit-learn and then explains predictions using `shap`.
- [**ImageNet VGG16 Model with Keras**](https://slundberg.github.io/shap/notebooks/ImageNet%20VGG16%20Model%20with%20Keras.html) - Explain the classic VGG16 convolutional nerual network's predictions for an image. This works by applying the model agnostic Kernel SHAP method to a super-pixel segmented image.
- [**Iris classification**](https://slundberg.github.io/shap/notebooks/Iris%20classification%20with%20scikit-learn.html) - A basic demonstration using the popular iris species dataset. It explains predictions from six different models in scikit-learn using `shap`.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='276'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1348' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#documentation-notebooks)Documentation notebooks

These notebooks comprehensively demonstrate how to use specific functions and objects.

- [`shap.dependence_plot`](https://slundberg.github.io/shap/notebooks/plots/dependence_plot.html)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='277'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1353' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#methods-unified-by-shap)Methods Unified by SHAP

1. *LIME:* Ribeiro, Marco Tulio, Sameer Singh, and Carlos Guestrin. "Why should i trust you?: Explaining the predictions of any classifier." Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 2016.

2. *Shapley sampling values:* Strumbelj, Erik, and Igor Kononenko. "Explaining prediction models and individual predictions with feature contributions." Knowledge and information systems 41.3 (2014): 647-665.

3. *DeepLIFT:* Shrikumar, Avanti, Peyton Greenside, and Anshul Kundaje. "Learning important features through propagating activation differences." arXiv preprint arXiv:1704.02685 (2017).

4. *QII:* Datta, Anupam, Shayak Sen, and Yair Zick. "Algorithmic transparency via quantitative input influence: Theory and experiments with learning systems." Security and Privacy (SP), 2016 IEEE Symposium on. IEEE, 2016.

5. *Layer-wise relevance propagation:* Bach, Sebastian, et al. "On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation." PloS one 10.7 (2015): e0130140.

6. *Shapley regression values:* Lipovetsky, Stan, and Michael Conklin. "Analysis of regression in game theory approach." Applied Stochastic Models in Business and Industry 17.4 (2001): 319-330.

7. *Tree interpreter:* Saabas, Ando. Interpreting random forests. http://blog.datadive.net/interpreting-random-forests/

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='278'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1377' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/slundberg/shap#citations)Citations

The algorithms and visualizations used in this package came primarily out of research in [Su-In Lee's lab](https://suinlee.cs.washington.edu/) at the University of Washington. If you use SHAP in your research we would appreciate a citation to the appropriate paper(s):

- For general use of SHAP you can read/cite our [NeurIPS paper](http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions) ([bibtex](https://raw.githubusercontent.com/slundberg/shap/master/docs/references/shap_nips.bib)).
- For TreeExplainer you can (for now) read/cite our [arXiv paper](https://arxiv.org/abs/1802.03888) ([bibtex](https://raw.githubusercontent.com/slundberg/shap/master/docs/references/treeshap_arxiv.bib)).
- For `force_plot` visualizations and medical applications you can read/cite our [Nature Biomedical Engineering paper](https://www.nature.com/articles/s41551-018-0304-0) ([bibtex](https://raw.githubusercontent.com/slundberg/shap/master/docs/references/nature_bme.bib); [free access](https://rdcu.be/baVbR)).

[![68747470733a2f2f7777772e66616365626f6f6b2e636f6d2f74723f69643d3138393134373039313835353939312665763d5061676556696577266e6f7363726970743d31](../_resources/b798f4ce7359fd815df4bdf76503b295.gif)](https://camo.githubusercontent.com/db8c6ffa9af4cf6d17c411a9f7ad56cc1b508c35/68747470733a2f2f7777772e66616365626f6f6b2e636f6d2f74723f69643d3138393134373039313835353939312665763d5061676556696577266e6f7363726970743d31)