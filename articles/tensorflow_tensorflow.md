tensorflow/tensorflow

# Release 2.0.0

## Major Features and Improvements

TensorFlow 2.0 focuses on **simplicity** and **ease of use**, featuring updates like:

- Easy model building with Keras and eager execution.
- Robust model deployment in production on any platform.
- Powerful experimentation for research.
- API simplification by reducing duplication and removing deprecated endpoints.

For details on best practices with 2.0, see [the Effective 2.0 guide](https://www.tensorflow.org/beta/guide/effective_tf2)

For information on upgrading your existing TensorFlow 1.x models, please refer to our [Upgrade](https://medium.com/tensorflow/upgrading-your-code-to-tensorflow-2-0-f72c3a4d83b5) and [Migration](https://www.tensorflow.org/guide/migrate) guides. We have also released a collection of [tutorials and getting started guides](https://www.tensorflow.org/beta).

## Highlights

- TF 2.0 delivers Keras as the central high level API used to build and train models. Keras provides several model-building APIs such as Sequential, Functional, and Subclassing along with eager execution, for immediate iteration and intuitive debugging, and `tf.data`, for building scalable input pipelines. Checkout [guide](https://www.tensorflow.org/beta/guide/keras/overview) for additional details.
- Distribution Strategy: TF 2.0 users will be able to use the [`tf.distribute.Strategy`](https://www.tensorflow.org/beta/guide/distribute_strategy) API to distribute training with minimal code changes, yielding great out-of-the-box performance. It supports distributed training with Keras model.fit, as well as with custom training loops. Multi-GPU support is available, along with experimental support for multi worker and Cloud TPUs. Check out the [guide](https://www.tensorflow.org/beta/guide/distribute_strategy) for more details.
- Functions, not Sessions. The traditional declarative programming model of building a graph and executing it via a `tf.Session` is discouraged, and replaced with by writing regular Python functions. Using the `tf.function` decorator, such functions can be turned into graphs which can be executed remotely, serialized, and optimized for performance.
- Unification of `tf.train.Optimizers` and `tf.keras.Optimizers`. Use `tf.keras.Optimizers` for TF2.0. `compute_gradients` is removed as public API, use `GradientTape` to compute gradients.
- AutoGraph translates Python control flow into TensorFlow expressions, allowing users to write regular Python inside `tf.function`-decorated functions. AutoGraph is also applied in functions used with tf.data, tf.distribute and tf.keras APIs.
- Unification of exchange formats to SavedModel. All TensorFlow ecosystem projects (TensorFlow Lite, TensorFlow JS, TensorFlow Serving, TensorFlow Hub) accept SavedModels. Model state should be saved to and restored from SavedModels.
- API Changes: Many API symbols have been renamed or removed, and argument names have changed. Many of these changes are motivated by consistency and clarity. The 1.x API remains available in the compat.v1 module. A list of all symbol changes can be found [here](https://docs.google.com/spreadsheets/d/1FLFJLzg7WNP6JHODX5q8BDgptKafq_slHpnHVbJIteQ/edit#gid=0).
- API clean-up, included removing `tf.app`, `tf.flags`, and `tf.logging` in favor of [absl-py](https://github.com/abseil/abseil-py).
- No more global variables with helper methods like `tf.global_variables_initializer` and `tf.get_global_step`.
- Add toggles `tf.enable_control_flow_v2()` and `tf.disable_control_flow_v2()` for enabling/disabling v2 control flow.
- Enable v2 control flow as part of `tf.enable_v2_behavior()` and `TF2_BEHAVIOR=1`.
- Fixes autocomplete for most TensorFlow API references by switching to use relative imports in API `__init__.py` files.
- Auto Mixed-Precision graph optimizer simplifies converting models to `float16` for acceleration on Volta and Turing Tensor Cores. This feature can be enabled by wrapping an optimizer class with `tf.train.experimental.enable_mixed_precision_graph_rewrite()`.
- Add environment variable `TF_CUDNN_DETERMINISTIC`. Setting to `TRUE` or "1" forces the selection of deterministic cuDNN convolution and max-pooling algorithms. When this is enabled, the algorithm selection procedure itself is also deterministic.

## Breaking Changes

- Many backwards incompatible API changes have been made to clean up the APIs and make them more consistent.
- Toolchains:
    - TensorFlow 2.0.0 is built using devtoolset7 (GCC7) on Ubuntu 16. This may lead to ABI incompatibilities with extensions built against earlier versions of TensorFlow.
    - Tensorflow code now produces 2 different pip packages: tensorflow_core containing all the code (in the future it will contain only the private implementation) and tensorflow which is a virtual pip package doing forwarding to tensorflow_core (and in the future will contain only the public API of tensorflow). We don't expect this to be breaking, unless you were importing directly from the implementation.

Removed the `freeze_graph` command line tool; `SavedModel` should be used in place of frozen graphs.

- `tf.contrib`:
    - `tf.contrib` has been deprecated, and functionality has been either migrated to the core TensorFlow API, to an ecosystem project such as [tensorflow/addons](https://www.github.com/tensorflow/addons) or [tensorflow/io](https://www.github.com/tensorflow/io), or removed entirely.
    - Remove `tf.contrib.timeseries` dependency on TF distributions.
    - Replace contrib references with `tf.estimator.experimental.*` for apis in `early_stopping.py`.
- `tf.estimator`:
    - Premade estimators in the tf.estimator.DNN/Linear/DNNLinearCombined family have been updated to use `tf.keras.optimizers` instead of the `tf.compat.v1.train.Optimizer`s. If you do not pass in an `optimizer=` arg or if you use a string, the premade estimator will use the Keras optimizer. This is checkpoint breaking, as the optimizers have separate variables. A checkpoint converter tool for converting optimizers is included with the release, but if you want to avoid any change, switch to the v1 version of the estimator: `tf.compat.v1.estimator.DNN/Linear/DNNLinearCombined*`.
    - Default aggregation for canned Estimators is now `SUM_OVER_BATCH_SIZE`. To maintain previous default behavior, please pass `SUM` as the loss aggregation method.
    - Canned Estimators don’t support `input_layer_partitioner` arg in the API. If you have this arg, you will have to switch to `tf.compat.v1 canned Estimators`.
    - `Estimator.export_savedmodel` has been renamed to `export_saved_model`.
    - When saving to SavedModel, Estimators will strip default op attributes. This is almost always the correct behavior, as it is more forwards compatible, but if you require that default attributes to be saved with the model, please use `tf.compat.v1.Estimator`.
    - Feature Columns have been upgraded to be more Eager-friendly and to work with Keras. As a result, `tf.feature_column.input_layer` has been deprecated in favor of `tf.keras.layers.DenseFeatures`. v1 feature columns have direct analogues in v2 except for `shared_embedding_columns`, which are not cross-compatible with v1 and v2. Use `tf.feature_column.shared_embeddings` instead.
- `tf.keras`:
    - `OMP_NUM_THREADS` is no longer used by the default Keras config. To configure the number of threads, use `tf.config.threading` APIs.
    - `tf.keras.model.save_model` and `model.save` now defaults to saving a TensorFlow SavedModel. HDF5 files are still supported.
    - Deprecated `tf.keras.experimental.export_saved_model` and `tf.keras.experimental.function`. Please use `tf.keras.models.save_model(..., save_format='tf')` and `tf.keras.models.load_model` instead.
    - Layers now default to float32, and automatically cast their inputs to the layer's dtype. If you had a model that used float64, it will probably silently use float32 in TensorFlow 2, and a warning will be issued that starts with `Layer <layer-name>` is casting an input tensor from dtype float64 to the layer's dtype of float32. To fix, either set the default dtype to float64 with `tf.keras.backend.set_floatx('float64')`, or pass `dtype='float64'` to each of the Layer constructors. See `tf.keras.layers.Layer` for more information.
- `tf.lite`:
    - Removed `lite.OpHint`, `lite.experimental`, and `lite.constant` from 2.0 API.
- Tensors are no longer hashable, but instead compare element-wise with `==` and `!=`. Use `tf.compat.v1.disable_tensor_equality()` to return to the previous behavior.
- Performing equality operations on Tensors or Variables with incompatible shapes an exception is no longer thrown. Instead `__eq__` returns False and `__ne__` returns True.
- Removed `tf.string_split` from v2 API.
- Deprecated the use of `constraint=` and `.constraint` with ResourceVariable.
- Add `UnifiedGRU` as the new GRU implementation for tf2.0. Change the default recurrent activation function for GRU from `hard_sigmoid` to `sigmoid`, and `reset_after` to True in 2.0. Historically recurrent activation is `hard_sigmoid` since it is fast than 'sigmoid'. With new unified backend between CPU and GPU mode, since the CuDNN kernel is using sigmoid, we change the default for CPU mode to sigmoid as well. With that, the default GRU will be compatible with both CPU and GPU kernel. This will enable user with GPU to use CuDNN kernel by default and get a 10x performance boost in training. Note that this is checkpoint breaking change. If user want to use their 1.x pre-trained checkpoint, please construct the layer with GRU(recurrent_activation='hard_sigmoid', reset_after=False) to fallback to 1.x behavior.
- `CUDNN_INSTALL_PATH`, `TENSORRT_INSTALL_PATH`, `NCCL_INSTALL_PATH`, `NCCL_HDR_PATH` are deprecated. Use `TF_CUDA_PATHS` instead which supports a comma-separated list of base paths that are searched to find CUDA libraries and headers.

Refer to our [public project status tracker](https://github.com/orgs/tensorflow/projects/4) and [issues tagged with 2.0](https://github.com/tensorflow/tensorflow/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A%22TF+2.0%22+) on GitHub for insight into recent issues and development progress.

If you experience any snags when using TF 2.0, please let us know at the [TF 2.0 Testing User Group](https://groups.google.com/a/tensorflow.org/forum/?utm_medium=email&utm_source=footer#!forum/testing). We have a support mailing list as well as weekly testing meetings, and would love to hear your migration feedback and questions.

## Bug Fixes and Other Changes

- `tf.contrib`:
    - Expose `tf.contrib.proto.*` ops in `tf.io` (they will exist in TF2)
- `tf.data`:
    - Add support for TensorArrays to `tf.data Dataset`.
    - Integrate Ragged Tensors with `tf.data`.
    - All core and experimental tf.data transformations that input user-defined functions can span multiple devices now.
    - Extending the TF 2.0 support for `shuffle(..., reshuffle_each_iteration=True)` and `cache()` to work across different Python iterators for the same dataset.
    - Removing the `experimental_numa_aware` option from `tf.data.Options`.
    - Add `num_parallel_reads` and passing in a Dataset containing filenames into `TextLineDataset` and `FixedLengthRecordDataset`.
    - Add support for defaulting the value of `cycle_length` argument of `tf.data.Dataset.interleave` to the number of schedulable CPU cores.
    - Promoting `tf.data.experimental.enumerate_dataset` to core as `tf.data.Dataset.enumerate`.
    - Promoting `tf.data.experimental.unbatch` to core as `tf.data.Dataset.unbatch`.
    - Adds option for introducing slack in the pipeline to reduce CPU contention, via `tf.data.Options().experimental_slack = True`
    - Added experimental support for parallel batching to `batch()` and `padded_batch()`. This functionality can be enabled through `tf.data.Options()`.
    - Support cancellation of long-running `reduce`.
    - Now we use `dataset` node name as prefix instead of the op name, to identify the component correctly in metrics, for pipelines with repeated components.
    - Improve the performance of datasets using `from_tensors()`.
    - Promoting `unbatch` from experimental to core API.
    - Adding support for datasets as inputs to `from_tensors` and `from_tensor_slices` and batching and unbatching of nested datasets.
- `tf.distribute`:
    - Enable `tf.distribute.experimental.MultiWorkerMirroredStrategy` working in eager mode.
    - Callbacks are supported in `MultiWorkerMirroredStrategy`.
    - Disable `run_eagerly` and distribution strategy if there are symbolic tensors added to the model using `add_metric` or `add_loss`.
    - Loss and gradients should now more reliably be correctly scaled w.r.t. the global batch size when using a `tf.distribute.Strategy`.
    - Set default loss reduction as `AUTO` for improving reliability of loss scaling with distribution strategy and custom training loops. `AUTO` indicates that the reduction option will be determined by the usage context. For almost all cases this defaults to `SUM_OVER_BATCH_SIZE`. When used in distribution strategy scope, outside of built-in training loops such as `tf.keras`  `compile` and `fit`, we expect reduction value to be 'None' or 'SUM'. Using other values will raise an error.
    - Support for multi-host `ncclAllReduce` in Distribution Strategy.
- `tf.estimator`:
    - Replace `tf.contrib.estimator.add_metrics` with `tf.estimator.add_metrics`
    - Use `tf.compat.v1.estimator.inputs` instead of `tf.estimator.inputs`
    - Replace contrib references with `tf.estimator.experimental.*` for apis in early_s in Estimator
    - Canned Estimators will now use keras optimizers by default. An error will be raised if tf.train.Optimizers are used, and you will have to switch to tf.keras.optimizers or tf.compat.v1 canned Estimators.
    - A checkpoint converter for canned Estimators has been provided to transition canned Estimators that are warm started from `tf.train.Optimizers` to `tf.keras.optimizers`.
    - Losses are scaled in canned estimator v2 and not in the optimizers anymore. If you are using Estimator + distribution strategy + optimikzer v1 then the behavior does not change. This implies that if you are using custom estimator with optimizer v2, you have to scale losses. We have new utilities to help scale losses `tf.nn.compute_average_loss`, `tf.nn.scale_regularization_loss`.
- `tf.keras`:
    - Premade models (including Linear and WideDeep) have been introduced for the purpose of replacing Premade estimators.
    - Model saving changes
    - `model.save` and `tf.saved_model.save` may now save to the TensorFlow SavedModel format. The model can be restored using `tf.keras.models.load_model`. HDF5 files are still supported, and may be used by specifying `save_format="h5"` when saving.
    - Raw TensorFlow functions can now be used in conjunction with the Keras Functional API during model creation. This obviates the need for users to create Lambda layers in most cases when using the Functional API. Like Lambda layers, TensorFlow functions that result in Variable creation or assign ops are not supported.
    - Add support for passing list of lists to the `metrics` argument in Keras `compile`.
    - Add `tf.keras.layers.AbstractRNNCell` as the preferred implementation for RNN cells in TF v2. User can use it to implement RNN cells with custom behavior.
    - Keras training and validation curves are shown on the same plot when using the TensorBoard callback.
    - Switched Keras `fit/evaluate/predict` execution to use only a single unified path by default unless eager execution has been explicitly disabled, regardless of input type. This unified path places an eager-friendly training step inside of a `tf.function`. With this

    1. All input types are converted to `Dataset`.

    2. The path assumes there is always a distribution strategy. when distribution strategy is not specified the path uses a no-op distribution strategy.

    3. The training step is wrapped in `tf.function` unless `run_eagerly=True` is set in compile. The single path execution code does not yet support all use cases. We fallback to the existing v1 execution paths if your model contains the following:

    4. `sample_weight_mode` in compile
    5. `weighted_metrics` in compile
    6. v1 optimizer
    7. target tensors in compile

If you are experiencing any issues because of this change, please inform us (file an issue) about your use case and you can unblock yourself by setting `experimental_run_tf_function=False` in compile meanwhile. We have seen couple of use cases where the model usage pattern is not as expected and would not work with this change.

    8. output tensors of one layer is used in the constructor of another.

    9. symbolic tensors outside the scope of the model are used in custom loss functions.

The flag can be disabled for these cases and ideally the usage pattern will need to be fixed.

    - Mark Keras `set_session` as `compat.v1` only.
    - `tf.keras.estimator.model_to_estimator` now supports exporting to `tf.train.Checkpoint format`, which allows the saved checkpoints to be compatible with `model.load_weights`.
    - `keras.backend.resize_images` (and consequently, `keras.layers.Upsampling2D`) behavior has changed, a bug in the resizing implementation was fixed.
    - Add an `implementation=3` mode for `tf.keras.layers.LocallyConnected2D` and `tf.keras.layers.LocallyConnected1D` layers using `tf.SparseTensor` to store weights, allowing a dramatic speedup for large sparse models.
    - Raise error if `batch_size` argument is used when input is dataset/generator/keras sequence.
    - Update TF 2.0 `keras.backend.name_scope` to use TF 2.0 `name_scope`.
    - Add v2 module aliases for losses, metrics, initializers and optimizers: `tf.losses = tf.keras.losses` & `tf.metrics = tf.keras.metrics` & `tf.initializers = tf.keras.initializers` & `tf.optimizers = tf.keras.optimizers`.
    - Updates binary cross entropy logic in Keras when input is probabilities. Instead of converting probabilities to logits, we are using the cross entropy formula for probabilities.
    - Added public APIs for `cumsum` and `cumprod` keras backend functions.
    - Add support for temporal sample weight mode in subclassed models.
    - Raise `ValueError` if an integer is passed to the training APIs.
    - Added fault-tolerance support for training Keras model via `model.fit()` with `MultiWorkerMirroredStrategy`, tutorial available.
    - Custom Callback tutorial is now available.
    - To train with `tf.distribute`, Keras API is recommended over estimator.
    - `steps_per_epoch` and `steps` arguments are supported with numpy arrays.
    - New error message when unexpected keys are used in sample_weight/class_weight dictionaries
    - Losses are scaled in Keras compile/fit and not in the optimizers anymore. If you are using custom training loop, we have new utilities to help scale losses `tf.nn.compute_average_loss`, `tf.nn.scale_regularization_loss`.
    - `Layer` apply and add_variable APIs are deprecated.
    - Added support for channels first data format in cross entropy losses with logits and support for tensors with unknown ranks.
    - Error messages will be raised if `add_update`, `add_metric`, `add_loss`, activity regularizers are used inside of a control flow branch.
    - New loss reduction types:

        1. `AUTO`: Indicates that the reduction option will be determined by the usage context. For almost all cases this defaults to `SUM_OVER_BATCH_SIZE`. When used with `tf.distribute.Strategy`, outside of built-in training loops such as `tf.keras`  `compile` and `fit`, we expect reduction value to be `SUM` or `NONE`. Using `AUTO` in that case will raise an error.

        2. `NONE`: Weighted losses with one dimension reduced (axis=-1, or axis specified by loss function). When this reduction type used with built-in Keras training loops like `fit`/`evaluate`, the unreduced vector loss is passed to the optimizer but the reported loss will be a scalar value.

        3. `SUM`: Scalar sum of weighted losses. 4. `SUM_OVER_BATCH_SIZE`: Scalar `SUM` divided by number of elements in losses. This reduction type is not supported when used with `tf.distribute.Strategy` outside of built-in training loops like `tf.keras`  `compile`/`fit`.

    - Wraps losses passed to the `compile` API (strings and v1 losses) which are not instances of v2 `Loss` class in `LossWrapper` class. => All losses will now use `SUM_OVER_BATCH_SIZE` reduction as default.
    - `model.add_loss(symbolic_tensor)` should work in ambient eager.
    - Update metric name to always reflect what the user has given in compile. Affects following cases

        1. When name is given as 'accuracy'/'crossentropy'
        2. When an aliased function name is used eg. 'mse'
        3. Removing the `weighted` prefix from weighted metric names.

    - Allow non-Tensors through v2 losses.
    - Add v2 sparse categorical crossentropy metric.
    - Add v2 APIs for `AUCCurve` and `AUCSummationMethod` enums.
    - `add_update` can now be passed a zero-arg callable in order to support turning off the update when setting `trainable=False` on a Layer of a Model compiled with `run_eagerly=True`.
    - Standardize the LayerNormalization API by replacing the args `norm_axis` and `params_axis` with `axis`.
    - Fixed critical bugs that help with DenseFeatures usability in TF2
- `tf.lite`:
    - Added evaluation script for `COCO` minival
    - Add delegate support for `QUANTIZE`.
    - Add `GATHER` support to NN API delegate.
    - Added support for TFLiteConverter Python API in 2.0. Contains functions from_saved_model, from_keras_file, and from_concrete_functions.
    - Add `EXPAND_DIMS` support to NN API delegate TEST.
    - Add `narrow_range` attribute to QuantizeAndDequantizeV2 and V3.
    - Added support for `tflite_convert` command line tool in 2.0.
    - Post-training quantization tool supports quantizing weights shared by multiple operations. The models made with versions of this tool will use INT8 types for weights and will only be executable interpreters from this version onwards.
    - Post-training quantization tool supports fp16 weights and GPU delegate acceleration for fp16.
    - Add delegate support for `QUANTIZED_16BIT_LSTM`.
    - Extracts `NNAPIDelegateKernel` from nnapi_delegate.cc
- TensorRT
    - Add TensorFlow 2.0-compatible `TrtGraphConverterV2` API for TensorRT conversion.

TensorRT initialization arguments are now passed wrapped in a named-tuple,

`TrtConversionParams`, rather than as separate arguments as in `TrtGraphConverter`.

    - Changed API to optimize TensorRT enginges during graph optimization. This is now

done by calling `converter.build()` where previously `is_dynamic_op=False` would

be set.

    - `converter.convert()` no longer returns a `tf.function`. Now the funtion must be

accessed from the saved model.

    - The `converter.calibrate()` method has been removed. To trigger calibration, a

`calibration_input_fn` should be provided to `converter.convert()`.

- Other:
    - Fix accidental quadratic graph construction cost in graph-mode `tf.gradients()`.
    - ResourceVariable's gather op supports batch dimensions.
    - ResourceVariable support for `gather_nd`.
    - `ResourceVariable` and `Variable` no longer accepts `constraint` in the constructor, nor expose it as a [@Property](https://github.com/Property).
    - Added gradient for `SparseToDense` op.
    - Expose a flag that allows the number of threads to vary across Python benchmarks.
    - `image.resize` in 2.0 now supports gradients for the new resize kernels.
    - `image.resize` now considers proper pixel centers and has new kernels (incl. anti-aliasing).
    - Renamed `tf.image` functions to remove duplicate "image" where it is redundant.
    - Variadic reduce is supported on CPU Variadic reduce is supported on CPU
    - Remove unused `StringViewVariantWrapper`.
    - Delete unused `Fingerprint64Map` op registration
    - Add broadcasting support to `tf.matmul`.
    - Add C++ Gradient for `BatchMatMulV2`.
    - Add `tf.math.cumulative_logsumexp` operation.
    - Add ellipsis (...) support for `tf.einsum()`.
    - Add expand_composites argument to all `nest.*` methods.
    - Added `strings.byte_split`.
    - Add a new "result_type" parameter to `tf.strings.split`.
    - Add name argument to `tf.string_split` and `tf.strings_split`.
    - Extend `tf.strings.split` to support inputs with any rank.
    - Added `tf.random.binomial`.
    - Added `key` and `skip` methods to `random.experimental.Generator`.
    - Extend `tf.function` with basic support for CompositeTensors arguments (such as `SparseTensor` and `RaggedTensor`).
    - `parallel_for.pfor`: add converters for Softmax, LogSoftmax, IsNaN, All, Any, and MatrixSetDiag.
    - `parallel_for`: add converters for LowerTriangularSolve and Cholesky.
    - `parallel_for`: add converters for `LogMatrixDeterminant` and `MatrixBandPart`.
    - `parallel_for`: Add converter for `MatrixDiag`.
    - `parallel_for`: Add converters for `OneHot`, `LowerBound`, `UpperBound`.
    - `parallel_for`: add converter for `BroadcastTo`.
    - Add `pfor` converter for `Squeeze`.
    - Add `RaggedTensor.placeholder()`.
    - Add ragged tensor support to `tf.squeeze`.
    - Update RaggedTensors to support int32 row_splits.
    - Allow `LinearOperator.solve` to take a `LinearOperator`.
    - Allow all dtypes for `LinearOperatorCirculant`.
    - Introduce MaxParallelism method
    - Add `LinearOperatorHouseholder`.
    - Adds Philox support to new stateful RNG's XLA path.
    - Added `TensorSpec` support for CompositeTensors.
    - Added `tf.linalg.tridiagonal_solve` op.
    - Added partial_pivoting input parameter to `tf.linalg.tridiagonal_solve`.
    - Added gradient to `tf.linalg.tridiagonal_solve`.
    - Added `tf.linalg.tridiagonal_mul op`.
    - Added GPU implementation of `tf.linalg.tridiagonal_matmul`.
    - Added `LinearOperatorToeplitz`.
    - Upgraded LIBXSMM to version 1.11.
    - Uniform processing of quantized embeddings by Gather and EmbeddingLookup Ops.
    - Correct a misstatement in the documentation of the sparse softmax cross entropy logit parameter.
    - Add `tf.ragged.boolean_mask`.
    - `tf.switch_case` added, which selects a branch_fn based on a branch_index.
    - The C++ kernel of gather op supports batch dimensions.
    - Fixed default value and documentation for `trainable` arg of tf.Variable.
    - `EagerTensor` now supports numpy buffer interface for tensors.
    - This change bumps the version number of the `FullyConnected` Op to 5.
    - Added new op: `tf.strings.unsorted_segment_join`.
    - Added HW acceleration support for `topK_v2`.
    - CloudBigtable version updated to v0.10.0 BEGIN_PUBLIC CloudBigtable version updated to v0.10.0.
    - Expose `Head` as public API.
    - Added `tf.sparse.from_dense` utility function.
    - Improved ragged tensor support in `TensorFlowTestCase`.
    - Added a function `nested_value_rowids` for ragged tensors.
    - Added `tf.ragged.stack`.
    - Makes the a-normal form transformation in Pyct configurable as to which nodes are converted to variables and which are not.
    - `ResizeInputTensor` now works for all delegates.
    - `tf.cond` emits a StatelessIf op if the branch functions are stateless and do not touch any resources.
    - Add support of local soft device placement for eager op.
    - Pass partial_pivoting to the `_TridiagonalSolveGrad`.
    - Add HW acceleration support for `LogSoftMax`.
    - Add guard to avoid acceleration of L2 Normalization with input rank != 4
    - Fix memory allocation problem when calling `AddNewInputConstantTensor`.
    - Delegate application failure leaves interpreter in valid state
    - `tf.while_loop` emits a StatelessWhile op if the cond and body functions are stateless and do not touch any resources.
    - `tf.cond`, `tf.while` and if and while in AutoGraph now accept a nonscalar predicate if has a single element. This does not affect non-V2 control flow.
    - Fix potential security vulnerability where decoding variant tensors from proto could result in heap out of bounds memory access.
    - Only create a GCS directory object if the object does not already exist.
    - Introduce `dynamic` constructor argument in Layer and Model, which should be set to `True` when using imperative control flow in the `call` method.
    - Begin adding Go wrapper for C Eager API.
    - XLA HLO graphs can be inspected with interactive_graphviz tool now.
    - Add dataset ops to the graph (or create kernels in Eager execution) during the python Dataset object creation instead doing it during Iterator creation time.
    - Add `batch_dims` argument to `tf.gather`.
    - The behavior of `tf.gather` is now correct when `axis=None` and `batch_dims<0`.
    - Update docstring for gather to properly describe the non-empty `batch_dims` case.
    - Removing of dtype in the constructor of initializers and partition_info in call.
    - Add `tf.math.nextafter` op.
    - Turn on MKL-DNN contraction kernels by default. MKL-DNN dynamically dispatches the best kernel implementation based on CPU vector architecture. To disable them, build with `--define=tensorflow_mkldnn_contraction_kernel=0`.
    - `tf.linspace(start, stop, num)` now always uses "stop" as last value (for num > 1)
    - Added top-k to precision and recall to keras metrics.
    - Add a ragged size op and register it to the op dispatcher
    - Transitive dependencies on :`pooling_ops` were removed. Some users may need to add explicit dependencies on :`pooling_ops` if they reference the operators from that library.
    - Add `CompositeTensor` base class.
    - Malformed gif images could result in an access out of bounds in the color palette of the frame. This has been fixed now
    - Add templates and interfaces for creating lookup tables
    - `Tensor::UnsafeCopyFromInternal` deprecated in favor `Tensor::BitcastFrom`.
    - In `map_vectorization` optimization, reduce the degree of parallelism in the vectorized map node.
    - Add variant wrapper for `absl::string_view`.
    - Add OpKernels for some stateless maps.
    - DType is no longer convertible to an int. Use `dtype.as_datatype_enum` instead of `int(dtype)` to get the same result.
    - Support both binary and -1/1 label input in v2 hinge and squared hinge losses.
    - Added `LinearOperator.adjoint` and `LinearOperator.H` (alias).
    - Expose CriticalSection in core as `tf.CriticalSection`.
    - Enhanced graphviz output.
    - Add opkernel templates for common table operations.
    - Fix callbacks do not log values in eager mode when a deferred build model is used.
    - `SignatureDef` util functions have been deprecated.
    - Update `Fingerprint64Map` to use aliases
    - Add legacy string flat hash map op kernels.
    - Add support for `add_metric` in the graph function mode.
    - Updating cosine similarity loss - removed the negate sign from cosine similarity.
    - Changed default for gradient accumulation for TPU embeddings to true.
    - Adds summary trace API for collecting graph and profile information.
    - The `precision_mode` argument to `TrtGraphConverter` is now case insensitive.

## Thanks to our Contributors

This release contains contributions from many people at Google, as well as:

1e100, a6802739, 4d55397500, a6802739, Abdullah Selek, abenmao, Abolfazl Shahbazi, Adam Richter, Adam Weiss, Ag Ramesh, Alan Du, Albin Joy, Alex, Alex Itkes, Alex Sergeev, Alexander Pivovarov, Alexey Romanov, alhkad, Aman Patel, Amit, Amit Kumar Jaiswal, Amit Srivastava, amoitra, Andreas Eberle, Andrew Lihonosov, Andy Craze, Anshuman Tripathy, Anthony Hsu, Anthony Platanios, Anuj Rawat, arp95, Arpit Shah, Armen Poghosov, armenpoghosov, Astropeak, Ashwin Ramaswami, Arpit Shah, Augustina Ragwitz, Aurelien Geron, AuréLien Geron, avasid, aweers, awesomealex1, Ayush Agrawal, Bas Aarts, Bastian Eichenberger, Bairen Yi, Bayberry Z, Ben Barsdell, Benjamin Peterson, bhack, Bharat Raghunathan, Bhavani Subramanian, Bin Fan, blairhan, BléNesi Attila, Bodin-E, Brandon Carter, Bryan Cutler, candy.dc, Cao Zongyan, Casper Da Costa-Luis, Chao Liu, Chen Guoyin, chenchc, chengchingwen, chie8842, Christian Hansen, Christoph Boeddeker, Christopher Yeh, Clayne Robison, Coady, Patrick, crafet, csukuangfj, ctiijima, Dan Jarvis, Dan Lazewatsky, Daniel Ingram, Daniel Rasmussen, Daniel Salvadori, Dave Airlie, David Norman, Dayananda V, delock, Denis Khalikov, Deven Desai, Dheeraj Rajaram Reddy, Diego Caballero, dmitrievanthony, Donovan Ong, Drew Szurko, Duncan Dean, Duncan Riach, Dustin Neighly, Dwight J Lyle, Eamon Ito-Fisher, eashtian3, Edward Forgacs, EFanZh, ejot, Elroy Ashtian Jr, Eric Schweitz, Evgeniy Polyakov, Fangjun Kuang, Federico Martinez, Fei Hu, Felix Lemke, Filip Matzner, FlashTek, fo40225, formath, FrançOis Chollet, frreiss, Fred Reiss, Frederic Bastien, Fredrik Knutsson, G. Hussain Chinoy, Gabriel, Gautam, gehring, Geoffrey Irving, George Grzegorz Pawelczak, Grzegorz Pawelczak, George Sterpu, Gianluca Varisco, Gleb Popov, Greg Peatfield, Guillaume Klein, Gurpreet Singh, Gustavo Lima Chaves, Gyoung-Yoon Ryoo, haison, Hanton Yang, HanGuo97, Haraldur TóMas HallgríMsson, Hari Shankar, hehongliang, Heungsub Lee, Hoeseong Kim, Huan Li (李卓桓), HåKon Sandsmark, I-Hong, I-Hong Jhuo, Ilham Firdausi Putra, Ilango R, Imran Salam, Innovimax, Jacky Ko, Irene Dea, Ivan Habernal, Jakub Lipinski, Jacky, Jason Zaman, Jason Zavaglia, jayhpark530, jcf94, jefby, Jeff Daily, Jeff Poznanovic, Jeffrey Poznanovic, Jekyll Lai, jer, Jeroen BéDorf, jerryyin, jhalakp, jiakai, Jia Qingtong, Jiankang, JiangXIAO, Joe Bowser, Joe Q, Joe Quadrino, Joel Shapiro, Johan Gunnarsson, Jojimon Varghese, Jonas Rauber, Jonathan Kyl, Jonathan, Joon, Joppe Geluykens, Joseph Friedman, Josh Beal, jtressle, Julian Niedermeier, Junqin Zhang, Justin Dujardin, Justin Tunis, jwu, K. Hodges, kaixih, Kaixi Hou, kjopek, Karl Lessard, Karl Weinmeister, Karthik Muthuraman, Kashif Rasul, Kay Zhu, Kbhute-Ibm, KDR, Keno Fischer, Kevin Mader, khanhlvg, Kilaru Yasaswi Sri Chandra Gandhi, Koan-Sin Tan, Koock Yoon, kouml, ktaebum, Kyuwon Kim, Lakshay Tokas, Laurent Le Brun, leike666666, leonard951, Leslie-Fang, Letian Kang, Li, Guizi, Loo Rong Jie, Lucas Hendren, Lukas Folle, Lukas Geiger, Luke Han, luxupu, lvli, Ma, Guokai, Mahmoud Abuzaina, Maksym Kysylov, Mandar Deshpande, manhyuk, Manraj Singh Grover, Marco Gaido, Marek Drozdowski, Margaret Maynard-Reid, Mark Ryan, mars20, Mateusz Chudyk, Matt Conley, mbhuiyan, mdfaijul, Mei Jie, Melissa Grueter, merturl, MichaelKonobeev, Michael KäUfl, Michal W. Tarnowski, MickaëL Schoentgen, Miguel Morin, Mihail Salnikov, Mikalai Drabovich, Mike Arpaia, Mike Holcomb, minds, monklof, Moses Marin, mpppk, Mr. Metal, Mshr-H, musikisomorphie, nammbash, Natalia Gimelshein, Nathan Luehr, Nayana-Ibm, Nayana Thorat, neargye, Neeraj Pradhan, Nehal J Wani, Neil, Nick, Nick Lewycky, Niels Ole Salscheider, Niklas SilfverströM, Niranjan Hasabnis, Nuka-137, Nutti, ocjosen, olicht, omeir1, P Sudeepam, Paige Bailey, Palmer Lao, Pan Daoxin, Pariksheet Pinjari, Pasquale Minervini, Patrick J. Lopresti, Patrik Gustavsson, Pavel Akhtyamov, Pavel Samolysov, PENGWA, per1234, PeterLee, Phan Van Nguyen Duc, Philipp Jund, Phillip Kravtsov, Pooya Davoodi, Pranav Marathe, Putra Manggala, Qingqing Cao, R S Nikhil Krishna, Rajeshwar Reddy T, Ramon ViñAs, Rasmus Diederichsen, Reuben Morais, robert, Rohit Gupta, Roland Zimmermann, Roman Soldatow, RonLek, Ruizhe, Ryan Jiang, saishruthi, Saleem Abdulrasool, Samantha Andow, Sami Kama, Sami Kama, Sana-Damani, Saurabh Deoras, sdamani, Sean Morgan, seanshpark, Sebastien Iooss, Serv-Inc, Severen Redwood, Shahzad Lone, Shashank Gupta, shashvat, Shashvat Chand Shahi, Shubham Goyal, Shashi, Sigrid Keydana, Siju, Siju Samuel, sleighsoft, smilu97, Snease-Abq, Son Tran, Spencer Schaber, sremedios, Srini511, srinivasan.narayanamoorthy, Steve Lang, Steve Nesae, Subin, Sumesh Udayakumaran, Sungmann Cho, sunway513, Supriya Rao, sxwang, Tae-Hwan Jung, Taehoon Lee, Takeo Sawada, Taylor Jakobson, Taylor Thornton, Ted Chang, TengLu, terryky, ThisIsIsaac, ThisIsPIRI, Thomas Deegan, Thomas Hagebols, tianyapiaozi, Till Hoffmann, Tim Zaman, tomguluson92, Tongxuan Liu, Trent Lo, Trevor Morris, TungJerry, Tyorden, Uday Bondhugula, v1incent, Vagif, Vasileios Lioutas, vbvg2008, vcarpani, Vijay Ravichandran, Vikram Tiwari,Viktor Gal, Vishwak Srinivasan, Vincent, Vishnuvardhan Janapati, Vitor-Alves, Vivek Suryamurthy, wangsiyu, wateryzephyr, WeberXie, Wei Wang, WeijieSun, Wen-Heng (Jack) Chung, wenxizhu, Will Battel, William D. Irons, winstonq, wyzhao, Xiaoming (Jason) Cui, Xiaoquan Kong, Xin, Xinping Wang, Yan Facai (颜发才), Yann-Yy, Yasir Modak, Yasuhiro Matsumoto, ymodak, Yong Tang, Yongfeng Gu, Younes Khoudli, Yuan Lin, Yuan (Terry) Tang, Yuchen Ying, Yves-Noel Weweler, zhangyujing, zjjott, zyeric, 王振华 (Zhenhua Wang), 黄鑫