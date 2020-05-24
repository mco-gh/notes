keras-team/keras-tuner

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='508'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1383' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#keras-tuner)Keras Tuner

An hyperparameter tuner for [Keras](https://keras.io/), specifically for `tf.keras` with TensorFlow 2.0.

**Status: pre-alpha.**

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='509'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1387' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#installation)Installation

Requirements:

- Python 3.6
- TensorFlow 2.0 Beta

Installation process:

	git clone https://github.com/keras-team/keras-tuner.git
	cd keras-tuner
	pip install .

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='510'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1394' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#usage-the-basics)Usage: the basics

Here's how to perform hyperparameter tuning for a single-layer dense neural network using random search.

First, we define a model-building function. It takes an argument `hp` from which you can sample hyperparameters, such as `hp.Range('units', min_value=32, max_value=512, step=32)`(an integer from a certain range).

This function returns a compiled model.

from tensorflow import kerasfrom tensorflow.keras import layersfrom kerastuner.tuners import  RandomSearchdef  build_model(hp):

model = keras.Sequential()

model.add(layers.Dense(units=hp.Range('units', min_value=32, max_value=512, step=32), activation='relu')) model.add(layers.Dense(10, activation='softmax'))

model.compile( optimizer=keras.optimizers.Adam(

hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])), loss='sparse_categorical_crossentropy', metrics=['accuracy']) return model

Next, instantiate a tuner. You should specify the model-building function, the name of the objective to optimize (whether to minimize or maximize is automatically inferred for built-in metrics), the total number of trials (`max_trials`) to test, and the number of models that should be built and fit for each trial (`executions_per_trial`).

Available tuners are `RandomSearch` and `Hyperband`.

**Note:** the purpose of having multiple executions per trial is to reduce results variance and therefore be able to more accurately assess the performance of a model. If you want to get results faster, you could set `executions_per_trial=1` (single round of training for each model configuration).

tuner =  RandomSearch( build_model, objective='val_accuracy', max_trials=5, executions_per_trial=3, directory='my_dir', project_name='helloworld')

You can print a summary of the search space:
tuner.search_space_summary()

Then, start the search for the best hyperparameter configuration. The call to `search` has the same signature as `model.fit()`.

tuner.search(x, y, epochs=5, validation_data=(val_x, val_y))

Here's what happens in `search`: models are built iteratively by calling the model-building function, which populates the hyperparameter space (search space) tracked by the `hp` object. The tuner progressively explores the space, recording metrics for each configuration.

When search is over, you can retrieve the best model(s):
models = tuner.get_best_models(num_models=2)
Or print a summary of the results:
tuner.results_summary()

You will also find detailed logs, checkpoints, etc, in the folder `my_dir/helloworld`, i.e. `directory/project_name`.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='511'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1418' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#the-search-space-may-contain-conditional-hyperparameters)The search space may contain conditional hyperparameters

Below, we have a `for` loop creating a tunable number of layers, which themselves involve a tunable `units` parameter.

This can be pushed to any level of parameter interdependency, including recursion.

Note that all parameter names should be unique (here, in the loop over `i`, we name the inner parameters `'units_' + str(i)`).

def  build_model(hp):
model = keras.Sequential() for i in  range(hp.Range('num_layers', 2, 20)):

model.add(layers.Dense(units=hp.Range('units_'  +  str(i), min_value=32, max_value=512, step=32), activation='relu'))

model.add(layers.Dense(10, activation='softmax'))
model.compile( optimizer=keras.optimizers.Adam(

hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])), loss='sparse_categorical_crossentropy', metrics=['accuracy']) return model

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='512'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1424' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#you-can-use-a-hypermodel-subclass-instead-of-a-model-building-function)You can use a HyperModel subclass instead of a model-building function

This makes it easy to share and reuse hypermodels.
A `HyperModel` subclass only needs to implement a `build(self, hp)` method.

from kerastuner import HyperModelclass  MyHyperModel(HyperModel): def  __init__(self, num_classes): self.num_classes = num_classes def  build(self, hp):

model = keras.Sequential()

model.add(layers.Dense(units=hp.Range('units', min_value=32, max_value=512, step=32), activation='relu'))

model.add(layers.Dense(self.num_classes, activation='softmax'))
model.compile( optimizer=keras.optimizers.Adam(

hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])), loss='sparse_categorical_crossentropy', metrics=['accuracy']) return model

hypermodel = MyHyperModel(num_classes=10)
tuner = RandomSearch(

hypermodel, objective='val_accuracy', max_trials=10, directory='my_dir', project_name='helloworld')

tuner.search(x, y, epochs=5, validation_data=(val_x, val_y))

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='513'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1429' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#keras-tuner-includes-pre-made-tunable-applications-hyperresnet-and-hyperxception)Keras Tuner includes pre-made tunable applications: HyperResNet and HyperXception

These are ready-to-use hypermodels for computer vision.

They come pre-compiled with `loss="categorical_crossentropy"` and `metrics=["accuracy"]`.

from kerastuner.applications import HyperResnetfrom kerastuner.tuners import Hyperband

hypermodel = HyperResnet(input_shape=(128, 128, 3), num_classes=10)
tuner = Hyperband(

hypermodel, objective='val_accuracy', max_trials=40, directory='my_dir', project_name='helloworld')

tuner.search(x, y, epochs=20, validation_data=(val_x, val_y))

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='514'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1434' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#you-can-easily-restrict-the-search-space-to-just-a-few-parameters)You can easily restrict the search space to just a few parameters

If you have an existing hypermodel, and you want to search over only a few parameters (such as the learning rate), you can do so by passing a `hyperparameters` argument to the tuner constructor, as well as `tune_new_entries=False` to specify that parameters that you didn't list in `hyperparameters` should not be tuned. For these parameters, the default value gets used.

from kerastuner import HyperParameters
hypermodel = HyperXception(input_shape=(128, 128, 3), num_classes=10)

hp = HyperParameters()# This will override the `learning_rate` parameter with your# own selection of choiceshp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

tuner = Hyperband(

hypermodel, hyperparameters=hp, # `tune_new_entries=False` prevents unlisted parameters from being tuned  tune_new_entries=False, objective='val_accuracy', max_trials=40, directory='my_dir', project_name='helloworld')

tuner.search(x, y, epochs=20, validation_data=(val_x, val_y))
Want to know what parameter names are available? Read the code.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='515'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1439' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#about-parameter-default-values)About parameter default values

Whenever you register a hyperparameter inside a model-building function or the `build` method of a hypermodel, you can specify a default value:

hp.Range('units', min_value=32, max_value=512, step=32, default=128)

If you don't, hyperparameters always have a default default (for `Range`, it is equal to `min_value`).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='516'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1444' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#fixing-values-in-a-hypermodel)Fixing values in a hypermodel

What if you want to do the reverse -- tune all available parameters in a hypermodel, **except** one (the learning rate)?

Pass a `hyperparameters` argument with a `Fixed` entry (or any number of `Fixed` entries), and specify `tune_new_entries=True`.

hypermodel = HyperXception(input_shape=(128, 128, 3), num_classes=10)
hp = HyperParameters()
hp.Fixed('learning_rate', value=1e-4)
tuner = Hyperband(

hypermodel, hyperparameters=hp, tune_new_entries=True, objective='val_accuracy', max_trials=40, directory='my_dir', project_name='helloworld')

tuner.search(x, y, epochs=20, validation_data=(val_x, val_y))

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='517'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1449' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/keras-team/keras-tuner#overriding-compilation-arguments)Overriding compilation arguments

If you have a hypermodel for which you want to change the existing optimizer, loss, or metrics, you can do so by passing these arguments to the tuner constructor:

hypermodel = HyperXception(input_shape=(128, 128, 3), num_classes=10)
tuner = Hyperband(

hypermodel, optimizer=keras.optimizers.Adam(1e-3), loss='mse', metrics=[keras.metrics.Precision(name='precision'),

keras.metrics.Recall(name='recall')], objective='val_precision', max_trials=40, directory='my_dir', project_name='helloworld')

tuner.search(x, y, epochs=20, validation_data=(val_x, val_y))