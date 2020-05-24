lutzroeder/netron

[![logo.png](../_resources/d0d573d3f25842b7bb27d069f0c8db03.png)](https://github.com/lutzroeder/netron)

Netron is a viewer for neural network, deep learning and machine learning models.

Netron supports **ONNX** (`.onnx`, `.pb`, `.pbtxt`), **Keras** (`.h5`, `.keras`), **Core ML** (`.mlmodel`), **Caffe** (`.caffemodel`, `.prototxt`), **Caffe2** (`predict_net.pb`, `predict_net.pbtxt`), **MXNet** (`.model`, `-symbol.json`), **TorchScript** (`.pt`, `.pth`), **NCNN** (`.param`) and **TensorFlow Lite** (`.tflite`).

Netron has experimental support for **PyTorch** (`.pt`, `.pth`), **Torch** (`.t7`), **CNTK** (`.model`, `.cntk`), **Deeplearning4j** (`.zip`), **PaddlePaddle** (`.zip`, `__model__`), **Darknet** (`.cfg`), **scikit-learn** (`.pkl`), **TensorFlow.js** (`model.json`, `.pb`) and **TensorFlow** (`.pb`, `.meta`, `.pbtxt`).

[![screenshot.png](../_resources/76d47d615285b486daaec933a2e207aa.png)](https://www.lutzroeder.com/ai)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1024' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/lutzroeder/netron#install)Install

**macOS**: [**Download**](https://github.com/lutzroeder/netron/releases/latest) the `.dmg` file or run `brew cask install netron`

**Linux**: [**Download**](https://github.com/lutzroeder/netron/releases/latest) the `.AppImage` or `.deb` file.

**Windows**: [**Download**](https://github.com/lutzroeder/netron/releases/latest) the `.exe` installer.

**Browser**: [**Start**](https://www.lutzroeder.com/ai/netron) the browser version.

**Python Server**: Run `pip install netron` and `netron [FILE]` or `import netron; netron.start('[FILE]')`.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='69'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1031' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/lutzroeder/netron#download-models)Download Models

Sample model files to download and open:

- **ONNX**: [resnet-18](https://s3.amazonaws.com/onnx-model-zoo/resnet/resnet18v1/resnet18v1.onnx)
- **Keras**: [tiny-yolo-voc](https://github.com/hollance/YOLO-CoreML-MPSNNGraph/raw/master/Convert/yad2k/model_data/tiny-yolo-voc.h5)
- **CoreML**: [faces_model](https://github.com/NovaTecConsulting/FaceRecognition-in-ARKit/files/1526806/faces_model.mlmodel.zip)
- **TensorFlow Lite**: [smartreply](https://storage.googleapis.com/download.tensorflow.org/models/tflite/smartreply_1.0_2017_11_01.zip)
- **MXNet**: [inception_v1](https://s3.amazonaws.com/model-server/models/onnx-inception_v1/inception_v1.model)
- **Caffe**: [mobilenet_v2](https://raw.githubusercontent.com/shicai/MobileNet-Caffe/master/mobilenet_v2.caffemodel)
- **TensorFlow**: [inception_v3](https://storage.googleapis.com/download.tensorflow.org/models/inception_v3_2016_08_28_frozen.pb.tar.gz)