> This simple example demonstrate how to plug TFDS into a Keras model.

# Training a neural network on MNIST with Keras  |  TensorFlow Datasets
This simple example demonstrate how to plug TFDS into a Keras model.

    import tensorflow.compat.v2 as tfimport tensorflow_datasets as tfdstfds.disable_progress_bar()tf.enable_v2_behavior()

Step 1: Create your input pipeline
----------------------------------

Build efficient input pipeline using advices from:

*   [TFDS performance guide](https://www.tensorflow.org/datasets/performances)
*   [tf.data performance guide](https://www.tensorflow.org/guide/data_performance#optimize_performance)

### Load MNIST

Load with the following arguments:

*   `shuffle_files`: The MNIST data is only stored in a single file, but for larger datasets with multiple files on disk, it's good practice to shuffle them when training.
*   `as_supervised`: Returns tuple `(img, label)` instead of dict `{'image': img, 'label': label}`

(ds_train, ds_test), ds_info = tfds.load(
        'mnist',
        split=['train', 'test'],
        shuffle_files=True,
        as_supervised=True,
        with_info=True,
    ) WARNING:absl:Dataset mnist is hosted on GCS. It will automatically be downloaded to your
local data directory. If you'd instead prefer to read directly from our public
GCS bucket (recommended if you're running on GCP), you can instead set
data\_dir=gs://tfds-data/datasets.


Downloading and preparing dataset mnist/3.0.1 (download: 11.06 MiB, generated: 21.00 MiB, total: 32.06 MiB) to /home/kbuilder/tensorflow\_datasets/mnist/3.0.1...
Dataset mnist downloaded and prepared to /home/kbuilder/tensorflow\_datasets/mnist/3.0.1. Subsequent calls will reuse this data. 

### Build training pipeline

Apply the following transormations:

*   `ds.map`: TFDS provide the images as tf.uint8, while the model expect tf.float32, so normalize images
*   `ds.cache` As the dataset fit in memory, cache before shuffling for better performance.  
    **Note:** Random transformations should be applied after caching
*   `ds.shuffle`: For true randomness, set the shuffle buffer to the full dataset size.  
    **Note:** For bigger datasets which do not fit in memory, a standard value is 1000 if your system allows it.
*   `ds.batch`: Batch after shuffling to get unique batches at each epoch.
*   `ds.prefetch`: Good practice to end the pipeline by prefetching [for performances](https://www.tensorflow.org/guide/data_performance#prefetching).

def normalize_img(image, label):
      """Normalizes images: `uint8` -> `float32`."""
      return tf.cast(image, tf.float32) / 255., label
    
    ds_train = ds_train.map(
        normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    ds_train = ds_train.cache()
    ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
    ds_train = ds_train.batch(128)
    ds_train = ds_train.prefetch(tf.data.experimental.AUTOTUNE) 

### Build evaluation pipeline

Testing pipeline is similar to the training pipeline, with small differences:

*   No `ds.shuffle()` call
*   Caching is done after batching (as batches can be the same between epoch)

ds_test = ds_test.map(
        normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    ds_test = ds_test.batch(128)
    ds_test = ds_test.cache()
    ds_test = ds_test.prefetch(tf.data.experimental.AUTOTUNE) 

Step 2: Create and train the model
----------------------------------

Plug the input pipeline into Keras.

model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
      tf.keras.layers.Dense(128,activation='relu'),
      tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer=tf.keras.optimizers.Adam(0.001),
        metrics=['accuracy'],
    )
    
    model.fit(
        ds_train,
        epochs=6,
        validation_data=ds_test,
    ) Epoch 1/6
469/469 \[==============================\] - 8s 16ms/step - loss: 0.3680 - accuracy: 0.8983 - val\_loss: 0.2064 - val\_accuracy: 0.9403
Epoch 2/6
469/469 \[==============================\] - 2s 3ms/step - loss: 0.1717 - accuracy: 0.9504 - val\_loss: 0.1426 - val\_accuracy: 0.9587
Epoch 3/6
469/469 \[==============================\] - 1s 3ms/step - loss: 0.1223 - accuracy: 0.9647 - val\_loss: 0.1139 - val\_accuracy: 0.9663
Epoch 4/6
469/469 \[==============================\] - 2s 3ms/step - loss: 0.0941 - accuracy: 0.9726 - val\_loss: 0.0960 - val\_accuracy: 0.9716
Epoch 5/6
469/469 \[==============================\] - 2s 3ms/step - loss: 0.0771 - accuracy: 0.9779 - val\_loss: 0.0854 - val\_accuracy: 0.9730
Epoch 6/6
469/469 \[==============================\] - 1s 3ms/step - loss: 0.0630 - accuracy: 0.9819 - val\_loss: 0.0833 - val\_accuracy: 0.9736

<tensorflow.python.keras.callbacks.History at 0x7f3fac166c18>