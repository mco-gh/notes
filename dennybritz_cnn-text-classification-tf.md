dennybritz/cnn-text-classification-tf

  Convolutional Neural Network for Text Classification in Tensorflow

- [  74 commits](https://github.com/dennybritz/cnn-text-classification-tf/commits/master)

- [  1 branch](https://github.com/dennybritz/cnn-text-classification-tf/branches)

- [  0 releases](https://github.com/dennybritz/cnn-text-classification-tf/releases)

- [  11 contributors](https://github.com/dennybritz/cnn-text-classification-tf/graphs/contributors)

- [ Apache-2.0](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/LICENSE)

1.   [  Python  100.0%](https://github.com/dennybritz/cnn-text-classification-tf/search?l=python)

 Python

Clone or download

 [Upload files](https://github.com/dennybritz/cnn-text-classification-tf/upload/master)  [Find file](https://github.com/dennybritz/cnn-text-classification-tf/find/master)

 [New pull request](https://github.com/dennybritz/cnn-text-classification-tf/pull/new/master)

  Latest commit [4e24742](https://github.com/dennybritz/cnn-text-classification-tf/commit/4e24742e6f42eeed7f09a6e36e54d84344a1bb98)  on Dec 4, 2017

 [![403133](../_resources/baedfea3ac501d591b4ff376521ca58c.jpg)](https://github.com/dennybritz)  dennybritz

 [dennybritzView all commits by dennybritz](https://github.com/dennybritz/cnn-text-classification-tf/commits?author=dennybritz) committed on Dec 4, 2017  [Merge pull request](https://github.com/dennybritz/cnn-text-classification-tf/commit/4e24742e6f42eeed7f09a6e36e54d84344a1bb98)  [#120](https://github.com/dennybritz/cnn-text-classification-tf/pull/120)  [from RoshanTanisha/master](https://github.com/dennybritz/cnn-text-classification-tf/commit/4e24742e6f42eeed7f09a6e36e54d84344a1bb98)

|     |     |     |     |
| --- | --- | --- | --- |
|     |  [data/rt-polaritydata](https://github.com/dennybritz/cnn-text-classification-tf/tree/master/data/rt-polaritydata) |    [Make code Python 3 compatible. Change data to UTF-8](https://github.com/dennybritz/cnn-text-classification-tf/commit/a0d0e9742b3dc42194955e78858f7be93027c75e) |  2 years ago |
|     |  [.gitignore](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/.gitignore) |    [Code updates](https://github.com/dennybritz/cnn-text-classification-tf/commit/5e9a1436d937a25bbdb104e675099a74c0595a5a) |  2 years ago |
|     |  [LICENSE](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/LICENSE) |    [Add license](https://github.com/dennybritz/cnn-text-classification-tf/commit/b780bd31025c62b92e16ece2c0a539dfe09c150d) |  2 years ago |
|     |  [README.md](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/README.md) |    [Fixes the required TF version.](https://github.com/dennybritz/cnn-text-classification-tf/commit/422a348c926620fbf71733a743b2bb41b453c6d3) |  a year ago |
|     |  [data_helpers.py](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/data_helpers.py) |    [fix bug for batch_iter](https://github.com/dennybritz/cnn-text-classification-tf/commit/7c704491a41d85290c350f392f9253568190d8d9) |  a year ago |
|     |  [eval.py](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/eval.py) |    [Minor typo](https://github.com/dennybritz/cnn-text-classification-tf/commit/9e70c241fca51c493268e2dad341cc4a855ffa40) |  7 months ago |
|     |  [text_cnn.py](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/text_cnn.py) |    [Minor fix to comment typo](https://github.com/dennybritz/cnn-text-classification-tf/commit/e52f275ee60c3a60a4e30b476e5358d23b509171) |  7 months ago |
|     |  [train.py](https://github.com/dennybritz/cnn-text-classification-tf/blob/master/train.py) |    [fixed memory leak](https://github.com/dennybritz/cnn-text-classification-tf/commit/6de4fee941695b3de9f5eff3f40ed1f95cfec135) |  5 months ago |

###    README.md

**[This code belongs to the "Implementing a CNN for Text Classification in Tensorflow" blog post.](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)**

It is slightly simplified implementation of Kim's [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882) paper in Tensorflow.

## [(L)](https://github.com/dennybritz/cnn-text-classification-tf#requirements)Requirements

- Python 3
- Tensorflow > 0.12
- Numpy

## [(L)](https://github.com/dennybritz/cnn-text-classification-tf#training)Training

Print parameters:
./train.py --help

	optional arguments:
	  -h, --help            show this help message and exit
	  --embedding_dim EMBEDDING_DIM
	                        Dimensionality of character embedding (default: 128)
	  --filter_sizes FILTER_SIZES
	                        Comma-separated filter sizes (default: '3,4,5')
	  --num_filters NUM_FILTERS
	                        Number of filters per filter size (default: 128)
	  --l2_reg_lambda L2_REG_LAMBDA
	                        L2 regularizaion lambda (default: 0.0)
	  --dropout_keep_prob DROPOUT_KEEP_PROB
	                        Dropout keep probability (default: 0.5)
	  --batch_size BATCH_SIZE
	                        Batch Size (default: 64)
	  --num_epochs NUM_EPOCHS
	                        Number of training epochs (default: 100)
	  --evaluate_every EVALUATE_EVERY
	                        Evaluate model on dev set after this many steps
	                        (default: 100)
	  --checkpoint_every CHECKPOINT_EVERY
	                        Save model after this many steps (default: 100)
	  --allow_soft_placement ALLOW_SOFT_PLACEMENT
	                        Allow device soft device placement
	  --noallow_soft_placement
	  --log_device_placement LOG_DEVICE_PLACEMENT
	                        Log placement of ops on devices
	  --nolog_device_placement

Train:
./train.py

## [(L)](https://github.com/dennybritz/cnn-text-classification-tf#evaluating)Evaluating

./eval.py --eval_train --checkpoint_dir="./runs/1459637919/checkpoints/"

Replace the checkpoint dir with the output from the training. To use your own data, change the `eval.py` script to load your data.

## [(L)](https://github.com/dennybritz/cnn-text-classification-tf#references)References

- [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882)
- [A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1510.03820)