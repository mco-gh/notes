tensorflow/tpu

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='172'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='833' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#object-detection-models-on-tpu)Object Detection Models on TPU

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='173'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='835' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#prerequsite)Prerequsite

To get started, make sure to use Tensorflow 1.13+ on Google Cloud. Also here are a few package you need to install to get started:

sudo apt-get install -y python-tk && \
pip install Cython matplotlib opencv-python-headless pyyaml Pillow && \

pip install 'git+https://github.com/cocodataset/cocoapi#egg=pycocotools&subdirectory=PythonAPI'

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='174'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='839' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#train-retinanet-on-tpu)Train RetinaNet on TPU

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='175'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='841' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#train-a-vanilla-resnet-50-based-retinanet)Train a vanilla ResNet-50 based RetinaNet.

TPU_NAME="<your GCP TPU name>"MODEL_DIR="<path to the directory to store model files>"RESNET_CHECKPOINT="<path to the pre-trained Resnet-50 checkpoint>"TRAIN_FILE_PATTERN="<path to the TFRecord training data>"EVAL_FILE_PATTERN="<path to the TFRecord validation data>"VAL_JSON_FILE="<path to the validation annotation JSON file>"python ~/tpu/models/official/detection/main.py \

--use_tpu=True \
--tpu="${TPU_NAME?}" \
--num_cores=8 \
--model_dir="${MODEL_DIR?}" \
--mode=train \
--eval_after_training=True \

--params_overrides="{ type: retinanet, train: { checkpoint: { path: ${RESNET_CHECKPOINT?}, prefix: resnet50/ }, train_file_pattern: ${TRAIN_FILE_PATTERN?} }, eval: { val_json_file: ${VAL_JSON_FILE?}, eval_file_pattern: ${EVAL_FILE_PATTERN?} } }"

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='176'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='844' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#train-a-custom-retinanet-using-the-config-file)Train a custom RetinaNet using the config file.

First, create a YAML config file, e.g. *my_retinanet.yaml*. This file specifies the parameters to be overridden, which should at least include the following fields.

# my_retinanet.yamltype: 'retinanet'train: train_file_pattern: <path to the TFRecord training data>eval: eval_file_pattern: <path to the TFRecord validation data>  val_json_file: <path to the validation annotation JSON file>

Once the YAML config file is created, you can launch the training using the following command.

TPU_NAME="<your GCP TPU name>"MODEL_DIR="<path to the directory to store model files>"python ~/tpu/models/official/detection/main.py \

--use_tpu=True \
--tpu="${TPU_NAME?}" \
--num_cores=8 \
--model_dir="${MODEL_DIR?}" \
--mode=train \
--eval_after_training=True \
--config_file="my_retinanet.yaml"

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='177'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='851' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#available-retinanet-templates)Available RetinaNet templates.

- NAS-FPN: [arXiv](https://arxiv.org/abs/1904.07392), [yaml](https://github.com/tensorflow/tpu/blob/master/models/official/detection/configs/yaml/retinanet_nasfpn.yaml)
- Auto-augument: arXiv, [yaml](https://github.com/tensorflow/tpu/blob/master/models/official/detection/configs/yaml/retinanet_autoaugment.yaml)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='178'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='856' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/tensorflow/tpu/tree/master/models/official/detection#export-to-savedmodel-for-serving)Export to SavedModel for serving

Once the training is finished, you can export the model in the SavedModel format for serving using the following command.

EXPORT_DIR="<path to the directory to store the exported model>"CHECKPOINT_PATH="<path to the pre-trained checkpoint>"USE_TPU=true

PARAMS_OVERRIDE=""  # if any.BATCH_SIZE=1

INPUT_TYPE="image_bytes"INPUT_NAME="input"INPUT_IMAGE_SIZE="640,640"OUTPUT_IMAGE_INFO=true

OUTPUT_NORMALIZED_COORDINATES=false
CAST_NUM_DETECTIONS_TO_FLOAT=true
python ~/tpu/models/official/detection/export_saved_model.py \
--export_dir="${EXPORT_DIR?}" \
--checkpoint_path="${CHECKPOINT_PATH?}" \
--use_tpu=${USE_TPU?} \
--params_override="${PARAMS_OVERRIDE?}" \
--batch_size=${BATCH_SIZE?} \
--input_type="${INPUT_TYPE?}" \
--input_name="${INPUT_NAME?}" \
--input_image_size="${INPUT_IMAGE_SIZE?}" \
--output_image_info=${OUTPUT_IMAGE_INFO?} \
--output_normalized_coordinates=${OUTPUT_NORMALIZED_COORDINATES?} \
--cast_num_detections_to_float=${CAST_NUM_DETECTIONS_TO_FLOAT?}