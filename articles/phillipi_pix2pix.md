phillipi/pix2pix

# [(L)](https://github.com/phillipi/pix2pix#pix2pix)pix2pix

[[Project]](https://phillipi.github.io/pix2pix/)  [[Arxiv]](https://arxiv.org/pdf/1611.07004v1.pdf)

Torch implementation for learning a mapping from input images to output images, for example:

[![examples.jpg](../_resources/230f170a6c3b55c711ffd5751c281b71.jpg)](https://github.com/phillipi/pix2pix/blob/master/imgs/examples.jpg)

Image-to-Image Translation Using Conditional Adversarial Networks

 [Phillip Isola](http://web.mit.edu/phillipi/), [Jun-Yan Zhu](https://people.eecs.berkeley.edu/~junyanz/), [Tinghui Zhou](https://people.eecs.berkeley.edu/~tinghuiz/), [Alexei A. Efros](https://people.eecs.berkeley.edu/~efros/)

In arxiv, 2016.

On some tasks, decent results can be obtained fairly quickly and on small datasets. For example, to learn to generate facades (example shown above), we trained on just 400 images for about 2 hours (on a single Pascal Titan X GPU). However, for harder problems it may be important to train on far larger datasets, and for many hours or even days.

## [(L)](https://github.com/phillipi/pix2pix#setup)Setup

### [(L)](https://github.com/phillipi/pix2pix#prerequisites)Prerequisites

- Linux or OSX
- NVIDIA GPU + CUDA CuDNN (CPU mode and CUDA without CuDNN may work with minimal modification, but untested)

### [(L)](https://github.com/phillipi/pix2pix#getting-started)Getting Started

- Install torch and dependencies from https://github.com/torch/distro
- Install torch packages ` nngraph ` and ` display `

luarocks install nngraph

luarocks install https://raw.githubusercontent.com/szym/display/master/display-scm-0.rockspec

- Clone this repo:

git clone git@github.com:phillipi/pix2pix.gitcd pix2pix

- Download the dataset (e.g. [CMP Facades](http://cmp.felk.cvut.cz/~tylecr1/facade/)):

bash ./datasets/download_dataset.sh facades

- Train the model

DATA_ROOT=./datasets/facades name=facades_generation which_direction=BtoA th train.lua

- (CPU only) The same training command without using a GPU or CUDNN. Setting the environment variables ` gpu=0 cudnn=0 ` forces CPU only

DATA_ROOT=./datasets/facades name=facades_generation which_direction=BtoA gpu=0 cudnn=0 batchSize=10 save_epoch_freq=5 th train.lua

- (Optionally) start the display server to view results as the model trains. ( See [Display UI](https://github.com/phillipi/pix2pix#display-ui) for more details):

th -ldisplay.start 8000 0.0.0.0

- Finally, test the model:

DATA_ROOT=./datasets/facades name=facades_generation which_direction=BtoA phase=val th test.lua

The test results will be saved to an html file here: ` ./results/facades_generation/latest_net_G_val/index.html `.

## [(L)](https://github.com/phillipi/pix2pix#train)Train

DATA_ROOT=/path/to/data/ name=expt_name which_direction=AtoB th train.lua
Switch ` AtoB ` to ` BtoA ` to train translation in opposite direction.

Models are saved to ` ./checkpoints/expt_name ` (can be changed by passing ` checkpoint_dir=your_dir ` in train.lua).

See ` opt ` in train.lua for additional training options.

## [(L)](https://github.com/phillipi/pix2pix#test)Test

DATA_ROOT=/path/to/data/ name=expt_name which_direction=AtoB phase=val th test.lua

This will run the model named ` expt_name ` in direction ` AtoB ` on all images in ` /path/to/data/val `.

Result images, and a webpage to view them, are saved to ` ./results/expt_name ` (can be changed by passing ` results_dir=your_dir ` in test.lua).

See ` opt ` in test.lua for additional testing options.

## [(L)](https://github.com/phillipi/pix2pix#datasets)Datasets

Download the datasets using the following script:
bash ./datasets/download_dataset.sh dataset_name

- ` facades `: 400 images from [CMP Facades dataset](http://cmp.felk.cvut.cz/~tylecr1/facade/).
- ` cityscapes `: 2975 images from the [Cityscapes training set](https://www.cityscapes-dataset.com/).
- ` maps `: 1096 training images scraped from Google Maps
- ` edges2shoes `: 50k training images from [UT Zappos50K dataset](http://vision.cs.utexas.edu/projects/finegrained/utzap50k/). Edges are computed by [HED](https://github.com/s9xie/hed) edge detector + post-processing.
- ` edges2handbags `: 137K Amazon Handbag images from [iGAN project](https://github.com/junyanz/iGAN). Edges are computed by [HED](https://github.com/s9xie/hed) edge detector + post-processing.

## [(L)](https://github.com/phillipi/pix2pix#models)Models

Download the pre-trained models with the following script. You need to rename the model (e.g. ` facades_label2image ` to ` /checkpoints/facades/latest_net_G.t7 `) after the download has finished.

bash ./models/download_model.sh model_name

- ` facades_label2image ` (label -> facade): trained on the CMP Facades dataset.
- ` cityscapes_label2image ` (label -> street scene): trained on the Cityscapes dataset.
- ` cityscapes_image2label ` (street scene -> label): trained on the Cityscapes dataset.
- ` map2sat ` (map -> aerial photo): trained on Google maps.
- ` sat2map ` (aerial photo -> map): trained on Google maps.
- ` edges2shoes ` (edge -> photo): trained on UT Zappos50K dataset.
- ` edges2handbags ` (edge -> photo): train on Amazon handbags images.
- ` day2night ` (daytime scene -> nighttime scene): trained on around 100 [webcams](http://transattr.cs.brown.edu/).

## [(L)](https://github.com/phillipi/pix2pix#setup-training-and-test-data)Setup Training and Test data

### [(L)](https://github.com/phillipi/pix2pix#generating-pairs)Generating Pairs

We provide a python script to generate training data in the form of pairs of images {A,B}, where A and B are two different depicitions of the same underlying scene. For example, these might be pairs {label map, photo} or {bw image, color image}. Then we can learn to translate A to B or B to A:

Create folder ` /path/to/data ` with subfolders ` A ` and ` B `. ` A ` and ` B ` should each have their own subfolders ` train `, ` val `, ` test `, etc. In ` /path/to/data/A/train `, put training images in style A. In ` /path/to/data/B/train `, put the corresponding images in style B. Repeat same for other data splits (` val `, ` test `, etc).

Corresponding images in a pair {A,B} must be the same size and have the same filename, e.g. ` /path/to/data/A/train/1.jpg ` is considered to correspond to ` /path/to/data/B/train/1.jpg `.

Once the data is formatted this way, call:

python scripts/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data

This will combine each pair of images (A,B) into a single image file, ready for training.

### [(L)](https://github.com/phillipi/pix2pix#notes-on-colorization)Notes on Colorization

No need to run ` combine_A_and_B.py ` for colorization. Instead, you just need to prepare some natural images, and set ` preprocess=colorization ` in the script. The program will automatically convert each RGB image into Lab color space, and create ` L -> ab ` image pair during the training.

### [(L)](https://github.com/phillipi/pix2pix#extracting-edges)Extracting Edges

We provide python and Matlab scripts to extract coarse edges from photos. Run ` scripts/edges/batch_hed.py ` to compute [HED](https://github.com/s9xie/hed) edges. Run ` scripts/edges/PostprocessHED.m ` to simplify edges with additional post-processing steps. Check the code documentation for more details.

## [(L)](https://github.com/phillipi/pix2pix#display-ui)Display UI

Optionally, for displaying images during training and test, use the [display package](https://github.com/szym/display).

- Install it with: ` luarocks install https://raw.githubusercontent.com/szym/display/master/display-scm-0.rockspec `
- Then start the server with: ` th -ldisplay.start `
- Open this URL in your browser: [http://localhost:8000](http://localhost:8000/)

By default, the server listens on localhost. Pass ` 0.0.0.0 ` to allow external connections on any interface:

th -ldisplay.start 8000 0.0.0.0

Then open ` http://(hostname):(port)/ ` in your browser to load the remote desktop.

L1 error is plotted to the display by default. Set the environment variable ` display_plot ` to a comma-seperated list of values ` errL1 `, ` errG ` and ` errD ` to visualize the L1, generator, and descriminator error respectively. For example, to plot only the generator and descriminator errors to the display instead of the default L1 error, set ` display_plot="errG,errD" `.

## [(L)](https://github.com/phillipi/pix2pix#citation)Citation

If you use this code for your research, please cite our paper [Image-to-Image Translation Using Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004v1.pdf):

	normal@article{pix2pix2016,
	  title={Image-to-Image Translation with Conditional Adversarial Networks},
	  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
	  journal={arxiv},
	  year={2016}
	}
	normal

## [(L)](https://github.com/phillipi/pix2pix#cat-paper-collection)Cat Paper Collection

If you love cats, and love reading cool graphics, vision, and learning papers, please check out the Cat Paper Collection:

[[Github]](https://github.com/junyanz/CatPapers)  [[Webpage]](http://people.eecs.berkeley.edu/~junyanz/cat/cat_papers.html)

## [(L)](https://github.com/phillipi/pix2pix#acknowledgments)Acknowledgments

Code borrows heavily from [DCGAN](https://github.com/soumith/dcgan.torch). The data loader is modified from [DCGAN](https://github.com/soumith/dcgan.torch) and [Context-Encoder](https://github.com/pathak22/context-encoder).