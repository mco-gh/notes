marcacohen/fast-style-transfer

###    README.md

## [(L)](https://github.com/marcacohen/fast-style-transfer#fast-style-transfer-in-tensorflow)Fast Style Transfer in [TensorFlow](https://github.com/tensorflow/tensorflow)

Add styles from famous paintings to any photo in a fraction of a second! [You can even style videos!](https://github.com/marcacohen/fast-style-transfer#video-stylization)

[![udnie.jpg](../_resources/a35587cfdc24e867e3c1dd270d96ac17.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/udnie.jpg)[![stata.jpg](../_resources/81a86fa5e8adca9a8ad1f4d6d449f1d2.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/content/stata.jpg)[![stata_udnie_header.jpg](../_resources/02eaffbfa6f7691b59fd08bb526adcbc.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/stata_udnie.jpg)

It takes 100ms on a 2015 Titan X to style the MIT Stata Center (1024×680) like Udnie, by Francis Picabia.

Our implementation is based off of a combination of Gatys' [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576), Johnson's [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://cs.stanford.edu/people/jcjohns/eccv16/), and Ulyanov's [Instance Normalization](https://arxiv.org/abs/1607.08022).

## [(L)](https://github.com/marcacohen/fast-style-transfer#video-stylization)Video Stylization

Here we transformed every frame in a video, then combined the results. [Click to go to the full demo on YouTube!](https://www.youtube.com/watch?v=xVJwwWQlQ1o) The style here is Udnie, as above.

 [![Stylized fox video. Click to go to YouTube!](../_resources/e8c4ebda76d7ca6b65646a97c206010b.gif)](https://www.youtube.com/watch?v=xVJwwWQlQ1o)

See how to generate these videos [here](https://github.com/marcacohen/fast-style-transfer#stylizing-video)!

## [(L)](https://github.com/marcacohen/fast-style-transfer#image-stylization)Image Stylization

We added styles from various paintings to a photo of Chicago. Click on thumbnails to see full applied style images.

[![chicago.jpg](../_resources/8262bbf4546363eee19ee4f9c5cbcf14.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/content/chicago.jpg)

[![wave.jpg](../_resources/b7b152b1829a4fd34aa9792c7e3df546.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/wave.jpg)[![chicago_wave.jpg](../_resources/5087e02751e9704dfb2b57b05ad4d5d0.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/chicago_wave.jpg)[![chicago_udnie.jpg](../_resources/1d13dfdc8ee3cf30dd3fa17ba595dc5b.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/chicago_udnie.jpg)[![udnie.jpg](../_resources/10ad589f0ca03c9533881b899250cbb6.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/udnie.jpg)

[![rain_princess.jpg](../_resources/45cd2811d1849bc2136853f4ead438a4.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/rain_princess.jpg)[![chicago_rain_princess.jpg](../_resources/28cec9d6d4f0f5fbdad93ff3f50b0f94.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/chicago_rain_princess.jpg)[![chicago_la_muse.jpg](../_resources/1bcf97b0b01e41d76ad9a36131fd1b57.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/chicago_la_muse.jpg)[![la_muse.jpg](../_resources/bd1aeb22c7a59c4ff414da3b7040618c.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/la_muse.jpg)

[![the_shipwreck_of_the_minotaur.jpg](../_resources/a7e20a601cddc7a78352c18a442398d9.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/the_shipwreck_of_the_minotaur.jpg)[![chicago_wreck.jpg](../_resources/87d0f81626654d2049ae96564489f92d.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/chicago_wreck.jpg)[![chicago_the_scream.jpg](../_resources/781c6b85fc9f14801a492c853bae60de.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/results/chicago_the_scream.jpg)[![the_scream.jpg](../_resources/fa8019c97baf12b5f53aaf667e97bb8c.jpg)](https://github.com/marcacohen/fast-style-transfer/blob/master/examples/style/the_scream.jpg)

## [(L)](https://github.com/marcacohen/fast-style-transfer#implementation-details)Implementation Details

Our implementation uses TensorFlow to train a fast style transfer network. We use roughly the same transformation network as described in Johnson, except that batch normalization is replaced with Ulyanov's instance normalization, and the scaling/offset of the output ` tanh ` layer is slightly different. We use a loss function close to the one described in Gatys, using VGG19 instead of VGG16 and typically using "shallower" layers than in Johnson's implementation (e.g. we use ` relu1_1 ` rather than ` relu1_2 `). Empirically, this results in larger scale style features in transformations.

## [(L)](https://github.com/marcacohen/fast-style-transfer#documentation)Documentation

### [(L)](https://github.com/marcacohen/fast-style-transfer#training-style-transfer-networks)Training Style Transfer Networks

Use ` style.py ` to train a new style transfer network. Run ` python style.py ` to view all the possible parameters. Training takes 4-6 hours on a Maxwell Titan X. [More detailed documentation here](https://github.com/marcacohen/fast-style-transfer/blob/master/docs.md#style). **Before you run this, you should run ` setup.sh `**. Example usage:

	python style.py --style path/to/style/img.jpg \
	  --checkpoint-dir checkpoint/path \
	  --test path/to/test/img.jpg \
	  --test-dir path/to/test/dir \
	  --content-weight 1.5e1 \
	  --checkpoint-iterations 1000 \
	  --batch-size 20

### [(L)](https://github.com/marcacohen/fast-style-transfer#evaluating-style-transfer-networks)Evaluating Style Transfer Networks

Use ` evaluate.py ` to evaluate a style transfer network. Run ` python evaluate.py ` to view all the possible parameters. Evaluation takes 100 ms per frame (when batch size is 1) on a Maxwell Titan X. [More detailed documentation here](https://github.com/marcacohen/fast-style-transfer/blob/master/docs.md#evaluate). Takes several seconds per frame on a CPU. **Models for evaluation are [located here](https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ?usp=sharing)**. Example usage:

	python evaluate.py --checkpoint path/to/style/model.ckpt \
	  --in-path dir/of/test/imgs/ \
	  --out-path dir/for/results/

### [(L)](https://github.com/marcacohen/fast-style-transfer#stylizing-video)Stylizing Video

Use ` transform_video.py ` to transfer style into a video. Run ` python transform_video.py ` to view all the possible parameters. Requires ` ffmpeg `. [More detailed documentation here](https://github.com/marcacohen/fast-style-transfer/blob/master/docs.md#video). Example usage:

	python transform_video.py --in-path path/to/input/vid.mp4 \
	  --checkpoint path/to/style/model.ckpt \
	  --out-path out/video.mp4 \
	  --device /gpu:0 \
	  --batch-size 4

### [(L)](https://github.com/marcacohen/fast-style-transfer#requirements)Requirements

You will need the following to run the above:

- TensorFlow 0.11.0
- Python 2.7.9, Pillow 3.4.2, scipy 0.18.1, numpy 1.11.2
- If you want to train (and don't want to wait for 4 months):
    - A decent GPU
    - All the required NVIDIA software to run TF on a GPU (cuda, etc)
- ffmpeg 3.1.3 if you want to stylize video

### [(L)](https://github.com/marcacohen/fast-style-transfer#citation)Citation

	  @misc{engstrom2016faststyletransfer,
	    author = {Logan Engstrom},
	    title = {Fast Style Transfer},
	    year = {2016},
	    howpublished = {\url{https://github.com/lengstrom/fast-style-transfer/}},
	    note = {commit xxxxxxx}
	  }

### [(L)](https://github.com/marcacohen/fast-style-transfer#attributionsthanks)Attributions/Thanks

- This project could not have happened without the advice (and GPU access) given by [Anish Athalye](http://www.anishathalye.com/).
    - The project also borrowed some code from Anish's [Neural Style](https://github.com/anishathalye/neural-style/)
- Some readme/docs formatting was borrowed from Justin Johnson's [Fast Neural Style](https://github.com/jcjohnson/fast-neural-style)
- The image of the Stata Center at the very beginning of the README was taken by [Juan Paulo](https://juanpaulo.me/)

### [(L)](https://github.com/marcacohen/fast-style-transfer#license)License

Copyright (c) 2016 Logan Engstrom. Contact me for commercial use (email: engstrom at my university's domain dot edu). Free for research/noncommercial use, as long as proper attribution is given and this copyright notice is retained.